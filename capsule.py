#!/usr/bin/env python3
"""Checkpoint capsule calculator for the Overwatch 2 Twitch drop duplication method.

Guided arithmetic for Phases B1 through D2. You take the stopwatch
measurements; this script computes every gate, prints each value the
worksheet needs, and refuses to continue when a rung fails.

It reads only the numbers you type and writes capsule-state.json next to
itself. It never touches accounts, credentials, or the network.
"""

import json
import math
import os
import sys

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "capsule-state.json")

DIVIDER = "-" * 62


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as fh:
        json.dump(state, fh, indent=2)


def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, encoding="utf-8") as fh:
                return json.load(fh)
        except (OSError, ValueError):
            return {}
    return {}


def ask(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\nInterrupted. Run again; completed phases are kept in capsule-state.json.")
        sys.exit(1)


def ask_yes_no(prompt):
    while True:
        reply = ask(prompt + " (y/n): ").strip().lower()
        if reply in ("y", "n"):
            return reply == "y"
        print("  Please answer y or n.")


def ask_numbers(count, prompt):
    while True:
        raw = ask(prompt)
        parts = raw.replace(",", " ").split()
        try:
            values = [float(p) for p in parts]
        except ValueError:
            print("  Enter numbers only, separated by spaces (for example 0.42 0.44 0.41).")
            continue
        if len(values) != count:
            print("  Expected exactly %d values, got %d. Try again." % (count, len(values)))
            continue
        return values


def fail(message, retry_hint):
    print(DIVIDER)
    print("GATE FAILED: " + message)
    print(retry_hint)
    print(DIVIDER)


def phase_b1(state):
    print(DIVIDER)
    print("PHASE B1 - COARSE CALIBRATION")
    print("Six paired observations, separated by 25 seconds.")
    print("For each pair, the offset is delta = tM - tD in fractional seconds.")
    print(DIVIDER)
    deltas = ask_numbers(6, "Enter the six coarse deltas: ")
    if any(d < 0.100 or d > 0.900 for d in deltas):
        fail("a delta fell outside the admission band [0.100, 0.900].",
             "Wait seven minutes and repeat B1. Do not continue to B2 with a failed coarse pass.")
        return
    if not ask_yes_no("Did all six observations still match the baseline B?"):
        fail("the displayed reward state drifted from the baseline.",
             "The baseline window has closed. Restart from Phase A.")
        return
    mu0 = sum(deltas) / 6.0
    state["mu0"] = mu0
    save_state(state)
    print("mu0 = %.3f s  ->  GATE PASSED. Record mu0 on the worksheet." % mu0)


def phase_b2(state):
    if "mu0" not in state:
        print("Run Phase B1 first.")
        return
    print(DIVIDER)
    print("PHASE B2 - FINE CALIBRATION")
    print("Twelve paired observations, separated by 37 seconds.")
    print(DIVIDER)
    deltas = ask_numbers(12, "Enter the twelve fine deltas: ")
    mu = sum(deltas) / 12.0
    sigma = math.sqrt(sum((d - mu) ** 2 for d in deltas) / 12.0)
    span = max(deltas) - min(deltas)
    print("mu    = %.3f s" % mu)
    print("sigma = %.3f s" % sigma)
    print("span  = %.3f s" % span)
    gates = [
        (sigma <= 0.080, "sigma <= 0.080 s"),
        (span <= 0.240, "span <= 0.240 s"),
        (abs(mu - state["mu0"]) <= 0.150, "|mu - mu0| <= 0.150 s"),
    ]
    for ok, label in gates:
        print("  %-22s %s" % (label, "OK" if ok else "FAILED"))
    if not all(ok for ok, _ in gates):
        fail("the fine admission ladder did not hold.",
             "Wait seven minutes and repeat BOTH B1 and B2. Do not change device clocks, "
             "network settings, or account links to obtain a better result.")
        return
    if not ask_yes_no("Did all twelve observations still match the baseline B?"):
        fail("the displayed reward state drifted from the baseline.",
             "The baseline window has closed. Restart from Phase A.")
        return
    state["mu"] = mu
    state["sigma"] = sigma
    save_state(state)
    print("GATE PASSED. Record mu and sigma on the worksheet.")


def phase_b3(state):
    if "mu" not in state:
        print("Run Phase B2 first.")
        return
    print(DIVIDER)
    print("PHASE B3 - THERMAL SETTLE")
    print("Eight paired observations, separated by 41 seconds.")
    print(DIVIDER)
    deltas = ask_numbers(8, "Enter the eight thermal deltas: ")
    tau = sum(deltas) / 8.0
    mu = state["mu"]
    print("tau = %.3f s" % tau)
    ok_band = all(mu - 0.120 <= d <= mu + 0.120 for d in deltas)
    print("  %-30s %s" % ("|tau - mu| <= 0.030 s", "OK" if abs(tau - mu) <= 0.030 else "FAILED"))
    print("  %-30s %s" % ("every delta within mu +/- 0.120 s", "OK" if ok_band else "FAILED"))
    if abs(tau - mu) > 0.030 or not ok_band:
        fail("the thermal gate did not hold.",
             "Do not average your way past it. Wait seven minutes and restart from B1.")
        return
    if not ask_yes_no("Did all eight observations still match the baseline B?"):
        fail("the displayed reward state drifted from the baseline.",
             "The baseline window has closed. Restart from Phase A.")
        return
    state["tau"] = tau
    save_state(state)
    print("GATE PASSED. Record tau on the worksheet.")


def phase_c(state):
    if "mu" not in state or "sigma" not in state:
        print("Run Phases B2 and B3 first.")
        return
    print(DIVIDER)
    print("PHASE C - CHECKPOINT CONSTRUCTION")
    print(DIVIDER)
    mu, sigma = state["mu"], state["sigma"]
    Q = int(round(abs(mu) * 1000))
    R = int(round(sigma * 1000))
    E = (Q + 17 * R + 431) % 997
    C = (31 * E + Q + 7 * R) % 4093
    phi = (Q + 3 * R) % 17
    print("Q   = %d" % Q)
    print("R   = %d" % R)
    print("E   = %d" % E)
    print("C   = %d" % C)
    print("phi = %d" % phi)
    if phi not in (0, 1):
        fail("phi = %d. The offset and variation inputs are interfering." % phi,
             "Wait seven minutes and repeat B1-B3. Do not adjust Q or R to force a lower phi.")
        return
    L = "%d-%d-12" % (E, C)
    state.update({"Q": Q, "R": R, "E": E, "C": C, "phi": phi, "L": L})
    save_state(state)
    print("GATE PASSED (phi is 0 or 1).")
    print("Write the label L = %s at the top of the worksheet." % L)
    print("Do not paste it into Twitch, Battle.net, a browser console, or any account form.")


def phase_c2(state):
    if "E" not in state or "phi" not in state:
        print("Run Phase C first.")
        return
    print(DIVIDER)
    print("PHASE C2 - RESONANCE FILTER")
    print(DIVIDER)
    E, phi = state["E"], state["phi"]
    candidates = [E, (E + 499) % 997, (E + 998) % 997]
    print("E1 = %d" % candidates[0])
    print("E2 = %d" % candidates[1])
    print("E3 = %d" % candidates[2])
    matched = [c for c in candidates if c % 7 == phi]
    for c, name in zip(candidates, ("E1", "E2", "E3")):
        verdict = "matches phi" if c % 7 == phi else "rejected"
        print("  %s mod 7 = %d  ->  %s" % (name, c % 7, verdict))
    if len(matched) == 1:
        print("resonance: LOCKED (E = %d). Record it on the worksheet." % matched[0])
        state["resonance"] = matched[0]
        save_state(state)
    else:
        fail("the filter selected %d candidates instead of exactly one." % len(matched),
             "The capsule has no unique resonant epoch. Wait seven minutes, recalibrate from "
             "B1, and rebuild the capsule. Do not hand-pick E2 or E3.")


def phase_d(state):
    if "E" not in state or "R" not in state:
        print("Run Phase C first.")
        return
    print(DIVIDER)
    print("PHASE D - COORDINATOR/OBSERVER SEPARATION")
    print("Four mobile observations, one every 89 seconds. Desktop untouched.")
    print(DIVIDER)
    E, R = state["E"], state["R"]
    epochs = [(E + 13 * m + R) % 997 for m in (1, 2, 3, 4)]
    for m, em in zip((1, 2, 3, 4), epochs):
        print("  Em (m = %d) = %d" % (m, em))
    ok_distinct = all(em != E for em in epochs)
    ok_increasing = all(a < b for a, b in zip(epochs, epochs[1:]))
    print("  %-30s %s" % ("every Em differs from E", "OK" if ok_distinct else "FAILED"))
    print("  %-30s %s" % ("Em strictly increasing", "OK" if ok_increasing else "FAILED"))
    if not (ok_distinct and ok_increasing):
        fail("the two contexts have not separated.",
             "Restart from Phase B1 after a seven-minute pause.")
        return
    if not ask_yes_no("After all four observations, does the visible state still equal B?"):
        fail("the displayed reward state drifted from the baseline.",
             "The baseline window has closed. Restart from Phase A.")
        return
    state["Em"] = epochs
    save_state(state)
    print("GATE PASSED. Record the four observer epochs on the worksheet.")


def phase_d2(state):
    if "Em" not in state:
        print("Run Phase D first.")
        return
    print(DIVIDER)
    print("PHASE D2 - COUNTERCURRENT OBSERVER")
    print("Four desktop observations, one every 97 seconds. Phone untouched.")
    print(DIVIDER)
    E, Q = state["E"], state["Q"]
    epochs = [(E + 17 * m + Q) % 997 for m in (1, 2, 3, 4)]
    for m, em in zip((1, 2, 3, 4), epochs):
        print("  Em' (m' = %d) = %d" % (m, em))
    coincident = state["Em"]
    ok_disjoint = all(em not in coincident for em in epochs)
    ok_increasing = all(a < b for a, b in zip(epochs, epochs[1:]))
    print("  %-42s %s" % ("no Em' shared with the coincident Em set", "OK" if ok_disjoint else "FAILED"))
    print("  %-42s %s" % ("Em' strictly increasing", "OK" if ok_increasing else "FAILED"))
    if not (ok_disjoint and ok_increasing):
        fail("the two directions have re-coupled.",
             "Wait seven minutes and restart from Phase D (both directions).")
        return
    if not ask_yes_no("After all four observations, does the visible state still equal B?"):
        fail("the displayed reward state drifted from the baseline.",
             "The baseline window has closed. Restart from Phase A.")
        return
    state["Em_counter"] = epochs
    save_state(state)
    print("GATE PASSED. Record the four countercurrent epochs on the worksheet.")
    print("The capsule is complete. Phases E onward stay on the worksheet.")


def run_check():
    print("capsule.py environment check")
    ok = True
    if sys.version_info >= (3, 6):
        print("OK   Python %d.%d.%d" % sys.version_info[:3])
    else:
        print("FAIL Python 3.6 or newer is required (found %d.%d)" % sys.version_info[:2])
        ok = False
    if repr(0.1 + 0.2) == "0.30000000000000004":
        print("OK   decimal discipline (0.1 + 0.2 = 0.30000000000000004)")
    else:
        print("FAIL decimal discipline: 0.1 + 0.2 printed %r" % (0.1 + 0.2))
        ok = False
    # Worked example from the guide: mu=0.420, sigma=0.030, mu0=0.470.
    Q, R = 420, 30
    E = (Q + 17 * R + 431) % 997
    C = (31 * E + Q + 7 * R) % 4093
    phi = (Q + 3 * R) % 17
    em = [(E + 13 * m + R) % 997 for m in (1, 2, 3, 4)]
    if E == 364 and C == 3728 and phi == 0 and em == [407, 420, 433, 446]:
        print("OK   capsule arithmetic (E=364, C=3728, phi=0, Em=407 420 433 446)")
    else:
        print("FAIL capsule arithmetic: E=%d C=%d phi=%d Em=%s" % (E, C, phi, em))
        ok = False
    print("All checks passed." if ok else "One or more checks failed. Fix what is named above.")
    return ok


def main():
    if "--check" in sys.argv[1:]:
        sys.exit(0 if run_check() else 1)
    state = load_state()
    print(DIVIDER)
    print("Checkpoint capsule calculator")
    print("Phases B1 through D2. Enter your measurements when asked.")
    print("Progress is kept in capsule-state.json next to this script.")
    print(DIVIDER)
    while True:
        print("\nMenu: 1=B1 coarse  2=B2 fine  3=B3 thermal  4=C checkpoint")
        print("       5=C2 resonance  6=D observer  7=D2 countercurrent  s=show  q=quit")
        choice = ask("Phase to run: ").strip().lower()
        if choice == "1":
            phase_b1(state)
        elif choice == "2":
            phase_b2(state)
        elif choice == "3":
            phase_b3(state)
        elif choice == "4":
            phase_c(state)
        elif choice == "5":
            phase_c2(state)
        elif choice == "6":
            phase_d(state)
        elif choice == "7":
            phase_d2(state)
        elif choice == "s":
            print(json.dumps(state, indent=2))
        elif choice == "q":
            return
        else:
            print("Choose 1-7, s, or q.")


if __name__ == "__main__":
    main()
