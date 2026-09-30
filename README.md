# Entitlement Checkpoint Retention — Overwatch 2 Twitch Drop Duplication Method

A complete guide to duplicating Overwatch 2 loot boxes earned through Twitch drop claims, using a PC or laptop together with an iOS or Android mobile device.

> **Platforms:** PC or laptop + iOS or Android device · **Accounts needed:** one Twitch account, one linked Battle.net account

---

## Table of contents

- [Part 0 — Pre-flight](#part-0--pre-flight)
  - [1. Overview](#1-overview)
  - [2. Requirements](#2-requirements)
  - [3. How the method works](#3-how-the-method-works)
  - [4. Terminology](#4-terminology)
  - [Phase 0 — Device parity, clock discipline, and cadence fingerprint](#phase-0--device-parity-clock-discipline-and-cadence-fingerprint)
  - [Phase A — Baseline acquisition](#phase-a--baseline-acquisition)
  - [Part 0.5 — Workstation provisioning](#part-05--workstation-provisioning)
    - [Provisioning 1 — Workspace and script](#provisioning-1--workspace-and-script)
    - [Provisioning 2 — Python](#provisioning-2--python)
    - [Provisioning 3 — 7-Zip (the capsule archive)](#provisioning-3--7-zip-the-capsule-archive)
    - [Provisioning 4 — Verification run and acceptance gate](#provisioning-4--verification-run-and-acceptance-gate)
- [Part 1 — Observation and checkpoint construction](#part-1--observation-and-checkpoint-construction)
  - [Phase B1 — Coarse calibration](#phase-b1--coarse-calibration)
  - [Phase B2 — Fine calibration](#phase-b2--fine-calibration)
  - [Phase B3 — Thermal settle](#phase-b3--thermal-settle)
  - [Phase C — Checkpoint construction](#phase-c--checkpoint-construction)
  - [Phase C2 — Resonance filter](#phase-c2--resonance-filter)
  - [Phase D — Coordinator/observer separation](#phase-d--coordinatorobserver-separation)
  - [Phase D2 — Countercurrent observer](#phase-d2--countercurrent-observer)
  - [Phase E — Retention windows](#phase-e--retention-windows)
  - [Phase F — Lineage commit and entropy sieve](#phase-f--lineage-commit-and-entropy-sieve)
  - [Phase G — Deferred observation and inventory protocol](#phase-g--deferred-observation-and-inventory-protocol)
- [Part 2 — The account-link migration](#part-2--the-account-link-migration)
  - [The six record cards](#the-six-record-cards)
  - [Stage H — Seal the baseline capsule](#stage-h--seal-the-baseline-capsule)
  - [Stage I — Simulated unlink](#stage-i--simulated-unlink)
  - [Stage J — Mobile observer confirmation](#stage-j--mobile-observer-confirmation)
  - [Stage K — Simulated relink (three cycles)](#stage-k--simulated-relink-three-cycles)
  - [Stage L — Construct the handoff capsule](#stage-l--construct-the-handoff-capsule)
  - [Stage L2 — Parity matrix](#stage-l2--parity-matrix)
  - [Stage M — Three-pass handoff review](#stage-m--three-pass-handoff-review)
  - [Stage N — Branch counters](#stage-n--branch-counters)
  - [Stage O — Two-phase commit](#stage-o--two-phase-commit)
  - [Stage P — Merkle digest chain](#stage-p--merkle-digest-chain)
  - [Stage Q — Commitment ladder](#stage-q--commitment-ladder)
  - [Stage R — Witness attestation](#stage-r--witness-attestation)
  - [Stage S — Cross-cycle determinant](#stage-s--cross-cycle-determinant)
  - [Stage T — Ascension ladder and anchor](#stage-t--ascension-ladder-and-anchor)
- [Part 3 — The final attestation](#part-3--the-final-attestation)
  - [Stage U — Quaternion fold](#stage-u--quaternion-fold)
  - [Stage V — Mirrored ladder](#stage-v--mirrored-ladder)
  - [Stage W — Grand unification](#stage-w--grand-unification)
  - [Phase Z — The covenant](#phase-z--the-covenant)
- [Restart and invalidation rules](#restart-and-invalidation-rules)
- [Troubleshooting](#troubleshooting)
- [Common questions](#common-questions)
- [Full worked example](#full-worked-example)
- [Completion checklist](#completion-checklist)

---

# Part 0 — Pre-flight

## 1. Overview

This method duplicates Overwatch 2 loot boxes obtained through Twitch drop claims by exploiting **checkpoint lineage retention**: a quirk in how Twitch and Battle.net reconcile account-link state across their desktop and mobile interfaces.

Most people assume drop duplication means replaying the claim request. That does not work — the reward service deduplicates on the entitlement itself. The method below takes a different route: it preserves an older account-link checkpoint while the systems move through three newer link generations, so the entitlement rebuild treats the old checkpoint as an incomplete migration instead of an already-processed reward.

The entire procedure uses the ordinary Twitch interfaces, a stopwatch, and a worksheet — and one small included script, `capsule.py`, which does the arithmetic of the observation phases for you (Part 0.5). No requests are captured, no browser console is used, no code has to be written, and — most importantly — **no changes are made to your real account links**. The unlink and relink at the heart of the method are performed on the worksheet, because touching the real connection destroys the checkpoint the method depends on.

The migration runs in **three cycles**, each with its own generation, handoff capsule, parity matrix, review passes, and commit seal. The cycles are then attested by a digest chain, a commitment ladder, a witness chain, and a cross-cycle determinant. Finally, the whole construction must survive a **quaternion fold**, a **mirrored ladder**, and a **grand unification gate** before the deferred rebuild is admitted. Expect the full run to take 5–6 hours of careful, uninterrupted work. Most failed attempts are caused by timing variance, a resonance-filter rejection, an inconsistent baseline, or an attestation collapse — not by the method itself.

## 2. Requirements

### Hardware

- A **PC or laptop** with a current desktop browser (Chrome, Edge, or Firefox).
- An **iOS or Android mobile device** with the official Twitch app, or a mobile browser.
- Both devices on networks you control (home Wi-Fi is fine; the two devices may share one network).

### Accounts

- One Twitch account, signed in on both devices through the official interfaces. Never share your credentials with another person or tool.
- One Battle.net account, **already linked normally** to that Twitch account. Do not unlink or relink it — the method works on a copy of the link state, not the link itself.
- One eligible Overwatch 2 drop visible in the ordinary Twitch Drops interface.

### Other

- A stopwatch that shows fractional seconds.
- An offline spreadsheet, or paper and a pen.
- An uninterrupted 5–6 hour observation period, ideally in one sitting per part.
- A quiet room: the timing phases require you to react to interface changes within roughly a quarter second.
- Overwatch 2 installed and signed in, for the closing inventory protocol.
- About 20 minutes for the one-time workstation provisioning in Part 0.5: two free installs (Python and 7-Zip) and the included `capsule.py` script.

### Safety rules

Use only the official Twitch and Battle.net websites or applications. Do not install certificates, use interception proxies, alter requests, disable account security, or export network logs. None of these are needed, and they can invalidate the checkpoint.

### Clock discipline

Both devices must show the same time of day within one minute before you start. Do not change any device clock after Phase 0 begins — the calibration uses a stopwatch, and any clock adjustment mid-run invalidates the offset ladder.

## 3. How the method works

The core of the method is the difference between **transport duplication** and **lineage duplication**:

| | Transport duplication | Lineage duplication |
| --- | --- | --- |
| What it repeats | The claim request | The account-link reconciliation history |
| What the backend sees | An identical request, deduplicated | Two different link generations with a retained checkpoint |
| Result | One reward | The old checkpoint rebuilt as a second grant |

Twitch's desktop and mobile interfaces act as two different **presentation contexts** for the same account. Each context can expose a different observation of one reward state, and the reconciliation service that keeps them in sync distinguishes them using a **linkage generation** and a **migration checkpoint**.

The method exploits that reconciliation, in three movements:

**Movement 1 — Observation.** Three calibration tiers (coarse, fine, thermal) measure how the two contexts settle, plus a cadence fingerprint and a countercurrent pass proving the contexts separate in both directions. The result is a **checkpoint capsule** that survives a resonance filter.

**Movement 2 — Migration.** A simulated unlink and relink on the worksheet moves the record through **three successive generations** while the original checkpoint is retained. Each generation handoff is validated by a parity matrix and sealed with a two-phase commit.

**Movement 3 — Attestation.** The migration is proven by a Merkle digest chain, a commitment ladder, a witness chain converging from two heads, and a cross-cycle determinant. Then the anchor must survive a **quaternion fold**, a **mirrored ladder** computed with inverted arithmetic, and a **grand unification gate** that binds the observation, migration, and attestation into one value.

The difficult part — and the reason this is not widely replicated — is that the checkpoint must survive **every filter in sequence, in both directions**. Each filter rejects attempts that are internally inconsistent, so a single mis-copied digit anywhere in the migration ledger invalidates the run, and the mirrored ladder means even a "lucky" wrong value fails twice. Unlinking and relinking the real accounts forces a full resync and invalidates the checkpoint; replaying the browser request only submits the current generation. You need the right combination of checkpoint state, linkage history, cycle discipline, attestation, and unification — not just the request.

## 4. Terminology

| Symbol | Meaning |
| --- | --- |
| `D` | Desktop coordinator observation |
| `M` | Mobile observer observation |
| `tD` | Stopwatch time when the desktop interface settles |
| `tM` | Stopwatch time when the mobile interface settles |
| `delta` | The observation offset: `tM - tD` |
| `B` | Baseline visible drop state |
| `J` | Cadence jitter index (Phase 0.4) |
| `mu0` | Coarse offset estimate (Phase B1) |
| `mu` | Fine offset mean (Phase B2) |
| `tau` | Thermal settle estimate (Phase B3) |
| `sigma` | Fine offset population standard deviation |
| `span` | Largest minus smallest fine offset |
| `Q`, `R` | Millisecond-scaled offset and variation inputs |
| `E` | Observation epoch (selected by the resonance filter) |
| `E1`, `E2`, `E3` | Resonance candidates |
| `phi` | Phase interference metric |
| `C` | Checkpoint residue |
| `L` | Lineage label; never an authentication token |
| `Em` | Observer epoch for row `m` (coincident direction) |
| `Em'` | Countercurrent observer epoch (Phase D2) |
| `rj`, `cj` | Observation residual and checkpoint contribution within a window |
| `Sw`, `Vw` | Window sums (plain and weighted) |
| `S`, `K` | Total sample sum and retention digest |
| `G_old` | Old link generation |
| `G_new` | New link generation, per cycle |
| `T` | Handoff ticket |
| `P` | Retention proof |
| `a`, `b` | Review and consistency counters |
| `N` | Branch marker |
| `F` | Final seal |
| `d0`–`d5` | Merkle digest chain links |
| `r1`, `r2`, `r3` | Commitment ladder rungs |
| `w0`, `w2` | Witness chain links |
| `Det` | Cross-cycle determinant |
| `s1`–`s4` | Ascension ladder rungs |
| `A` | Anchor (`s4`) |
| `f1`, `f2`, `f3` | Quaternion fold values |
| `m1`–`m4` | Mirrored ladder rungs |
| `G` | Grand unification value |

`E`, `C`, `L`, `G`, `T`, `P`, `N`, `F`, the `d`, `w`, `s`, `f`, and `m` chains, `A`, and `G` are worksheet values. They are not API fields and should not be pasted into any account form — they only become useful once the entire capsule, migration, attestation, and unification are complete.

## Phase 0 — Device parity, clock discipline, and cadence fingerprint

Before any drop observation, verify that both presentation contexts are behaving identically — and that your own hands are consistent.

### 0.1 Clock parity

1. Note the time of day on the PC and on the phone.
2. If they differ by more than one minute, fix the phone's clock (automatic time is fine) **before** continuing. After Phase 0 begins, no clock may be adjusted again.
3. Record the difference in seconds as `clock_offset` on the worksheet, even if it is zero.

### 0.2 Interface parity

1. Open the Twitch Drops page on the PC.
2. Open the same page on the phone.
3. Confirm both show the **same campaigns, in the same order**, within five seconds of each other.
4. Record `parity: OK` or `parity: MISMATCH`. A mismatch means the two contexts are in different reconciliation states; wait ten minutes and repeat.

### 0.3 Drift probe

Perform three paired refreshes (one desktop, then one mobile, immediately after), separated by 20 seconds:

1. Refresh the desktop; record how long its loading indicator takes to disappear, in fractional seconds.
2. Refresh the mobile; record the same.
3. Compute the absolute difference for each pair.

The **drift spread** is the largest difference minus the smallest difference of the three pairs. The drift budget is:

```text
drift spread <= 0.400 seconds
clock_offset <= 60 seconds
parity: OK
```

If the drift budget fails, do not continue — the fine calibration in Phase B2 will not converge. Restart Phase 0 after ten minutes. Do not switch networks, browsers, or devices mid-probe.

### 0.4 Cadence fingerprint

The reconciliation is sensitive to *who* is driving the refreshes. An erratic operator produces windows the retention sieve rejects.

Perform **five** desktop refreshes, one every **15 seconds**, timed by the stopwatch:

1. Note the exact interval between your refresh press and the next (aim for 15.0 s each time).
2. Record all five realized intervals.
3. `J` (the jitter index) is the largest interval minus the smallest interval.

The cadence gate:

```text
J <= 0.600 seconds
```

If `J` is larger, your press timing is too irregular — practice until five consecutive intervals fit inside 0.6 seconds before restarting Phase 0. Do not use a metronome app with sound; sub-vocal counting is fine, but the presses must be yours.

## Phase A — Baseline acquisition

1. On the PC, open Twitch's normal Drops interface.
2. On the phone, open the equivalent interface for the same account.
3. Select one visible Overwatch 2 campaign to observe. Do not claim it as part of the calibration.
4. Record only information already visible in the interface:
   - Campaign display name.
   - Drop display name.
   - Progress percentage, if shown.
   - Claimable or claimed status.
   - Whether the reward card is visible on both devices.
5. Wait three minutes without refreshing either interface.
6. Record the same fields again.
7. The baseline is accepted only if the two records are identical.

If the visible state changes naturally, discard the baseline and begin this phase again. Do not try to force the live account back into its previous state — a changed baseline means the checkpoint window has closed.

---

# Part 0.5 — Workstation provisioning

Two installs and one script. The script, `capsule.py`, does every calculation from Phase B1 through Phase D2 — you only take the measurements and type them in. Nothing in Part 0.5 touches your accounts, credentials, cookies, or network traffic.

> **Rules that apply to all of Part 0.5**
>
> - Download only from the official domains named below. Never from a mirror, never from a search-result ad.
> - **Reboot after each install** — not sign out, restart. A skipped reboot is the leading cause of inherited instability at Phase B1.
> - Budget about 20 minutes. Phase 0 may not begin until the gate in Provisioning 4 passes.

## Provisioning 1 — Workspace and script

1. In **File Explorer**, create a folder named `C:\LootboxDupeMethod`.
2. Get `capsule.py` from this repository (Code > **Download ZIP**, then extract `capsule.py` into the folder you just made).
3. Open **Command Prompt** (`Win + R`, type `cmd`, press Enter) and confirm the script is where you think it is:

```text
cd C:\LootboxDupeMethod
dir
```

4. `capsule.py` must appear in the listing. If it does not, move it there before continuing — every later command assumes this location.

## Provisioning 2 — Python

The script needs Python 3. You will not write any code; the installer just makes `python` work.

1. Go to `https://www.python.org`. Downloads > Windows > **Windows installer (64-bit)**.
2. Run the installer. On the first screen, **check "Add python.exe to PATH"** at the bottom, then click **Install Now**.
3. **Reboot.**

## Provisioning 3 — 7-Zip (the capsule archive)

At the end of each part, your worksheet folder is sealed into an archive, so a failed run is recoverable instead of lost.

1. Go to `https://www.7-zip.org`. Download the **64-bit x64** `.exe` installer and run it (click **Install**, then **Close**).
2. **Reboot.**

## Provisioning 4 — Verification run and acceptance gate

1. Open Command Prompt and run:

```text
cd C:\LootboxDupeMethod
python capsule.py --check
```

2. The script verifies the Python version, the decimal separator, and its own capsule arithmetic. All three lines must say `OK`.

All of the following must be true before Phase 0 may begin:

- [ ] `python capsule.py --check` printed three `OK` lines and "All checks passed."
- [ ] The machine was rebooted after both installs.
- [ ] The phone is charged to at least 80%, with automatic date and time on.
- [ ] The screen auto-lock is set longer than one observation phase.

If the check fails, fix what it names and re-run it — do not continue past a failed check. Only when every box is checked does the method begin, at [Phase 0](#phase-0--device-parity-clock-discipline-and-cadence-fingerprint).

### The capsule archive (after each part)

After Parts 1, 2, and 3 are fully accepted, open the 7-Zip File Manager, browse to your worksheet, **Add to archive** as `capsule-part-1.7z` (then `-2`, `-3`), compression level **Normal**, saved into `C:\LootboxDupeMethod`. Never open or edit an archive you have made — it is a state you can prove, not a backup you consult.

### Is the script safe?

`capsule.py` reads only the numbers you type and writes one file, `capsule-state.json`, next to itself, so a half-finished run is not lost when you close the window. It has no network access, and it never asks for or sees any account information.

---

# Part 1 — Observation and checkpoint construction

All arithmetic from Phase B1 through Phase D2 is done for you: run `python capsule.py` (Provisioning 1) in `C:\LootboxDupeMethod`, pick the phase from the menu, and enter your measurements when asked. The script applies every admission gate in this part, prints each value the worksheet needs, and refuses to continue when a rung fails. Phases E onward stay on the worksheet.

## Phase B1 — Coarse calibration

The coarse pass screens for a usable offset before you invest in the fine pass.

Perform **six** paired observations, separated by **25 seconds**:

1. Start the stopwatch.
2. Refresh the desktop Drops view once.
3. Record `tD` when the loading indicator disappears (or the reward card becomes readable again).
4. Refresh the mobile view once.
5. Record `tM` using the same rule.
6. Calculate `delta = tM - tD`.
7. Record whether the displayed reward state still matches the baseline.

Calculate the coarse mean `mu0` from the six deltas.

The coarse admission rule is:

```text
every delta within [0.100, 0.900] seconds
all six observations match B
```

If any delta falls outside the band, the contexts are not settling consistently; wait seven minutes and repeat B1. Do not continue to B2 with a failed coarse pass — the fine calibration inherits the instability.

## Phase B2 — Fine calibration

Perform **twelve** paired observations, separated by **37 seconds**, following the same refresh and settle rules as B1.

Use this worksheet:

| Sample | `tD` | `tM` | `delta` | Baseline matches? |
| --- | --- | --- | --- | --- |
| 01 | | | | |
| 02 | | | | |
| 03 | | | | |
| 04 | | | | |
| 05 | | | | |
| 06 | | | | |
| 07 | | | | |
| 08 | | | | |
| 09 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |

Calculate:

- `mu`: the mean of the twelve fine offsets.
- `sigma`: their population standard deviation.
- `span`: largest offset minus smallest offset.

The fine admission ladder (all four must hold):

```text
sigma   <= 0.080 seconds
span    <= 0.240 seconds
|mu - mu0| <= 0.150 seconds
all twelve observations match B
```

If any rung fails, wait seven minutes and repeat **both** B1 and B2. Do not change device clocks, network settings, account links, or security settings to obtain a better result — the checkpoint is only valid if the contexts were measured as they actually behave.

## Phase B3 — Thermal settle

The thermal pass confirms the offset is stable over a longer horizon — the reconciliation treats a drifting offset as a single context and refuses to separate.

Perform **eight** paired observations, separated by **41 seconds**, following the same rules as B2.

Calculate the thermal mean `tau` from the eight deltas.

The thermal gate:

```text
|tau - mu| <= 0.030 seconds
every thermal delta within [mu - 0.120, mu + 0.120] seconds
all eight observations match B
```

The thermal gate is deliberately the tightest in Part 1. If it fails, do not average your way past it — wait seven minutes and restart from B1. The checkpoint arithmetic in Phase C is only valid for offsets whose thermal settle agrees with the fine mean.

## Phase C — Checkpoint construction

Calculate the checkpoint capsule from the fine calibration:

```text
Q = round(abs(mu) * 1000)
R = round(sigma * 1000)
E = (Q + 17 * R + 431) mod 997
C = (31 * E + Q + 7 * R) mod 4093
L = E-C-12
```

For `L`, concatenate the decimal values of `E`, `C`, and the literal sample count `12`, separated by hyphens. It is not a subtraction expression.

Then calculate the **phase interference metric**:

```text
phi = (Q + 3 * R) mod 17
```

The interference gate:

```text
phi must be 0 or 1
```

A higher `phi` means the offset and variation inputs are interfering with each other in the epoch arithmetic; the capsule is still internally consistent, but the retention windows in Phase E will drift. If `phi > 1`, wait seven minutes and repeat B1–B3. Do not adjust `Q` or `R` to force a lower `phi`.

Example, using measurements from a successful run:

```text
mu0 = 0.470 seconds
mu = 0.420 seconds
tau = 0.445 seconds
sigma = 0.030 seconds
Q = 420
R = 30
E = 364
C = 3728
phi = (420 + 90) mod 17 = 0
L = 364-3728-12
```

Write the label at the top of the worksheet. Do not paste it into Twitch, Battle.net, a browser console, an HTTP header, or any account form.

## Phase C2 — Resonance filter

The epoch arithmetic produces three resonance candidates. Only one of them is in phase with the checkpoint residue; the other two produce capsules that the retention windows will silently reject.

Calculate:

```text
E1 = E
E2 = (E + 499) mod 997
E3 = (E + 998) mod 997
```

With the example values:

```text
E1 = 364
E2 = 863
E3 = 365
```

The selected candidate is the one satisfying:

```text
(candidate mod 7) == phi
```

Checking each:

```text
E1 mod 7 = 0   -> matches phi = 0
E2 mod 7 = 2   -> rejected
E3 mod 7 = 1   -> rejected
```

So the capsule keeps `E1 = E`. Record `resonance: LOCKED` on the worksheet.

If **no** candidate satisfies the congruence, the capsule has no resonant epoch — the run is dead. Wait seven minutes, recalibrate from B1, and rebuild the capsule. Do not reuse `E2` or `E3` by hand-picking; the filter selects exactly one candidate or none.

## Phase D — Coordinator/observer separation

Leave the desktop on its baseline reward card. Use the phone for four ordinary observations, one every **89 seconds**.

For each mobile observation:

1. Refresh the mobile view once.
2. Record the visible campaign and reward state.
3. Leave the desktop untouched.
4. Increment the observer counter: `m = 1, 2, 3, 4`.
5. Calculate the observer epoch:

```text
Em = (E + 13 * m + R) mod 997
```

The separation condition is:

```text
Em != E for all four observations
Em strictly increasing across m = 1..4
visible reward state still equals B
```

With the example values, the observer epochs are 407, 420, 433, and 446.

The observer epochs prove the two contexts have separated. If they have not, the reconciliation has not entered the state the method needs — restart from Phase B1 after a seven-minute pause.

## Phase D2 — Countercurrent observer

Separation in one direction is not enough: the reconciliation must be separated **in both directions**, or the countercurrent epochs collapse onto the coincident ones and the migration is read as a single context.

Swap the roles for four more observations, one every **97 seconds**:

1. Leave the **phone** on its baseline reward card.
2. Refresh the **desktop** view once per observation.
3. Record whether the visible state still matches `B`.
4. Increment the countercurrent counter: `m' = 1, 2, 3, 4`.
5. Calculate the countercurrent epoch:

```text
Em' = (E + 17 * m' + Q) mod 997
```

### Countercurrent barrier

The countercurrent pass passes only when:

- Every `Em'` differs from every coincident `Em` (no shared values across the two sets).
- The four `Em'` values are strictly increasing.
- The visible reward state still equals `B` after all four observations.

If any `Em'` equals an `Em`, the two directions have **re-coupled**: the contexts are no longer independently separated, and the migration will collapse the lineage. Wait seven minutes and restart from Phase D (both directions).

## Phase E — Retention windows

Perform **four** retention windows. Each window contains **ten** paired observations separated by **53 seconds**.

At the beginning of each window:

1. Read the desktop card without refreshing it.
2. Read the mobile card.
3. Record whether both still display `B`.
4. Record the current lineage label `L`.

For each paired observation (sample `j` from 1 through 10):

1. Refresh the phone once and record its settle time.
2. Wait exactly eleven seconds on the stopwatch.
3. Refresh the desktop once and record its settle time.
4. Calculate the observation residual:

```text
rj = abs((tM - tD) - mu)
```

5. Calculate the checkpoint contribution:

```text
cj = (round(rj * 1000) + 19 * j + C) mod 4093
```

6. Calculate the weighted contribution:

```text
wj = (2 * j + 1)
Vw = sum over j of (wj * cj)
```

A window `k` (numbered 1 through 4) passes only when **all nine** of the following hold:

- Every visible reward state still matches `B`.
- No residual exceeds 0.150 seconds.
- The plain sum `Sw = sum of cj` is divisible by 7.
- The weighted sum `Vw` is divisible by 11.
- `Vw mod 13` equals the window number `k`.
- The window's first and last `cj` values are different.
- No two `cj` values in the window are equal.
- The `cj` values alternate in parity (odd, even, odd, even, …) across `j = 1..10`.
- The window's `Sw` differs from every other accepted window's `Sw` by more than 500.

The window-index checksum, the parity alternation, and the window-separation lattice are what tie the four windows to the epoch ladder — windows that merely satisfy the divisibility rules but ignore their index or crowd each other produce a lineage the commit stage will reject.

A failed window must be repeated after a five-minute pause, from the start of that window. Do not use scripts or automated refresh loops to accelerate it — machine-paced refreshes are detected as a single context and collapse the separation.

## Phase F — Lineage commit and entropy sieve

After **four** accepted windows (40 accepted samples), apply the entropy sieve:

1. Collect all 40 accepted `cj` values into one list.
2. Verify that no value appears more than twice in the entire list.
3. Verify that at most 6 of the 40 values are divisible by 3.
4. Verify that at least 30 of the 40 values are greater than 1000.
5. Verify that the four `Sw` values are all distinct.

If the sieve fails, the windows are too regular — the reconciliation will read them as a single context. Wait seven minutes and rerun Phase E entirely.

Then calculate:

```text
S = sum of all 40 accepted cj values
K = (S + 23 * E + C) mod 65521
```

Construct the final record:

```text
baseline: recorded visible reward state
coordinator_epoch: E
observer_epoch: last recorded Em
countercurrent_epoch: last recorded Em'
checkpoint_residue: C
lineage_label: L
retention_digest: K
accepted_windows: 4
accepted_samples: 40
```

This is the **lineage commit manifest**. Keep it — the account-link migration in Part 2 is built from it, and every cycle re-validates it.

## Phase G — Deferred observation and inventory protocol

1. Leave both interfaces untouched for seven minutes.
2. Refresh the desktop view once.
3. Wait twenty-three seconds.
4. Refresh the mobile view once.
5. Compare the visible state with `B`.

This pause is where the deferred entitlement reconciliation happens. Do not refresh repeatedly — each additional refresh before the migration completes can advance the generation and drop the retained checkpoint.

The full inventory protocol runs **after** the unification value `G` is recorded in Stage W:

| Time after unification | Action |
| --- | --- |
| +2 minutes | Sign in to Overwatch 2. Do not open any loot boxes. Count and record the total. |
| +6 minutes | Return to the dashboard. Refresh once. Confirm the drop state still matches `B`. |
| +14 minutes | Count the inventory again. Record the total, unopened. |
| +30 minutes | Final count (Phase Z). The rebuilt grant has fully settled by this point. |

Do not open boxes between any two counts — an opened box cannot be compared, and the rebuild must be observed intact.

---

# Part 2 — The account-link migration

The stages below build the account-link migration that turns the retained checkpoint into a rebuilt entitlement. The migration is performed on worksheet cards, in **three cycles**. **Your real Twitch and Battle.net connection stays linked the entire time** — the unlink and relink are simulated on paper, because changing the real link destroys the checkpoint.

## The six record cards

Use six pages in a notebook, or six sections in an offline spreadsheet:

| Card | Purpose |
| --- | --- |
| A — Baseline | The original visible reward state and accepted calibration values. |
| B — Old link | The first generation and its retained checkpoint. |
| C — New link | The current cycle's generation. |
| D — Review | Calculation checks, handoff results, and the final record. |
| E — Matrix | The parity matrix and digest chain. |
| F — Ledger | The witness chain, determinant, ladders, fold, and unification. |

Do not put account passwords, email addresses, access tokens, device identifiers, or browser cookies on any card. The campaign display name is enough to identify the observation.

Give every card the same worksheet name, such as:

```text
OW-OBSERVATION-01
```

### Copying rule

When copying a number from one card to another:

1. Copy the number.
2. Mark the source row with a small tick.
3. Read the copied number backward digit by digit.
4. Compare it with the source.
5. Mark the destination row as checked.

Do not correct an accepted row silently. Cross it out once, retain the original number, and write the correction beneath it. A mixed-up record invalidates every later stage, including all three chains — the chains detect tampering, but only if you recompute them.

## Stage H — Seal the baseline capsule

Copy the following fields onto Card A:

```text
baseline display name:
baseline visible status:
Q: 420
R: 30
E: 364
C: 3728
L: 364-3728-12
phi: 0
resonance: LOCKED (E1 selected)
tau: 0.445
J: recorded cadence jitter
accepted calibration samples: 12
accepted windows: 4
accepted samples: 40
```

### Baseline barrier

Before continuing, verify all of the following:

- `Q` and `R` are whole numbers.
- `E` is between 0 and 996.
- `C` is between 0 and 4092.
- `phi` is 0 or 1.
- The resonance filter locked exactly one candidate.
- The countercurrent barrier passed with no shared epochs.
- The first part of `L` matches `E`.
- The second part of `L` matches `C`.
- The final part of `L` is `12`.
- The visible reward state was copied as text, not as an assumed reward count.

Write `BASELINE SEALED` on Card A after the checks pass. After this marker, no number on Card A may change.

## Stage I — Simulated unlink

**Do not press any real Disconnect, Unlink, Remove, or Revoke button.** The unlink in this stage consists entirely of editing the record on Card B.

Calculate the old generation:

```text
G_old = (E + C) mod 991
```

Using the worked example:

```text
G_old = (364 + 3728) mod 991
G_old = 128
```

On Card B, write:

```text
old_generation: 128
old_checkpoint: 3728
baseline_label: 364-3728-12
simulated_link_state: ATTACHED
retained_reference: YES
```

Now perform the unlink:

1. Copy the entire Card B record into a second box on the same page.
2. Leave the first box unchanged.
3. In the second box, change `simulated_link_state` to `DETACHED`.
4. Leave `old_generation` unchanged.
5. Leave `old_checkpoint` unchanged.
6. Write `DETACH RECORDED` beneath the second box.

### Retention barrier

The unlink passes only if:

- Both boxes still show the same old generation.
- Both boxes still show the same old checkpoint.
- The first box still says `ATTACHED`.
- The second box says `DETACHED`.
- No other number has changed.
- The actual account connections have not been altered.

The first box is the **orphan checkpoint reference** — the piece of lineage the rebuild needs. If a field was overwritten instead of copied, restore it from Card A before proceeding; an overwritten checkpoint cannot be reconstructed later.

## Stage J — Mobile observer confirmation

Use the phone as the second reading surface. You may read the numbers from the PC screen or place the notebook beside the phone. Do not send private account information to another device or upload it to a service.

Prepare four observer rows and four countercurrent rows, and confirm again that no coincident `Em` equals any countercurrent `Em'` before proceeding.

With the example values, the coincident rows are:

| Observer row | Calculation result |
| --- | --- |
| 1 | 407 |
| 2 | 420 |
| 3 | 433 |
| 4 | 446 |

Record the results on Card D.

### Observer barrier

Check:

1. All four coincident values are different.
2. None equals the baseline epoch, 364.
3. Each later value is 13 higher than the preceding value in this example.
4. The countercurrent rows share no value with the coincident rows.
5. The old-generation card has not changed during the review.

Write `OBSERVER CONFIRMED` after these checks pass.

If the rows were calculated in the wrong order, reorder the worksheet rows. Do not refresh account sessions or sign out — the observer epochs are worksheet values, not session state.

## Stage K — Simulated relink (three cycles)

The relink runs in **three cycles**. Each cycle advances the generation by one increment. Cycle I is shown fully; Cycles II and III repeat the same arithmetic with the next cycle number.

For cycle `m_c` (1, 2, 3), calculate:

```text
G_new(m_c) = (G_old + 97 * m_c + R) mod 991
```

For the worked example:

| Cycle | Calculation | `G_new` |
| --- | --- | --- |
| I | `(128 + 97·1 + 30) mod 991` | 255 |
| II | `(128 + 97·2 + 30) mod 991` | 352 |
| III | `(128 + 97·3 + 30) mod 991` | 449 |

**Cycle I, on Card C:**

```text
cycle: I
new_generation: 255
previous_generation: 128
baseline_label: 364-3728-12
simulated_link_state: ATTACHED
source_reference: CARD B
```

### Generation-separation barrier (per cycle)

The cycle is accepted only when:

- The new generation differs from the old generation.
- The new generation differs from every previously used generation.
- Card C points back to Card B.
- Card B retains its original numbers.
- Both cards point to the same baseline label.

If `G_new(m_c)` equals any earlier generation, mark the cycle `GENERATION COLLISION` and stop the branch — a collision means the migration has no separation to reconcile. Restart Stage K after seven minutes. Do not attempt to cause a collision.

### Cycle completion rule

Cycles II and III each repeat, in order: the relink arithmetic, the generation-separation barrier, the handoff capsule (Stage L), the parity matrix (Stage L2), the review passes (Stage M), the branch counters (Stage N), and the commit (Stage O) with that cycle's `G_new`. Only the **final cycle's** values feed the attestation stages P through W.

### Why the old card is not deleted

Deleting Card B would destroy the lineage the comparison needs. Keeping both cards is what makes the reconciliation see an old generation and a sequence of new generations instead of one current generation.

## Stage L — Construct the handoff capsule

The handoff capsule links the old-generation card, the current cycle's new-generation card, and the baseline card.

Calculate the handoff ticket:

```text
T = (31 * G_new + C + Q) mod 4093
```

Example (Cycle I):

```text
T = (31 * 255 + 3728 + 420) mod 4093
T = 3867
```

Then calculate the retention proof:

```text
P = (T + 7 * G_old + 11 * G_new) mod 8191
```

Example:

```text
P = (3867 + 7 * 128 + 11 * 255) mod 8191
P = 7568
```

Write the following capsule on Card D:

```text
baseline_label: 364-3728-12
old_generation: 128
new_generation: 255
handoff_ticket: 3867
retention_proof: 7568
handoff_state: PREPARED
```

### Handoff barrier

Recalculate `T` without looking at the first calculation. Compare both answers.

Then do the same for `P`.

Do not average two disagreeing results. A difference means the arithmetic or copied inputs must be reviewed before continuing.

## Stage L2 — Parity matrix

The parity matrix cross-checks the capsule from three directions at once. Any single wrong copy breaks at least one checksum.

On Card E, arrange:

```text
|  E    G_old   C  |
| G_new  E     R  |
|  Q    P      T  |
```

With the worked example:

```text
| 364   128   3728 |
| 255   364     30 |
| 420  7568   3867 |
```

Calculate the row checksums (each row sum, reduced mod 9973):

```text
row 1: (364 + 128 + 3728) mod 9973  = 4220
row 2: (255 + 364 + 30)   mod 9973  = 649
row 3: (420 + 7568 + 3867) mod 9973 = 1882
```

Calculate the column checksums:

```text
col 1: (364 + 255 + 420)   = 1039
col 2: (128 + 364 + 7568)  = 8060
col 3: (3728 + 30 + 3867)  = 7625
```

Calculate the grand checksum:

```text
grand = (4220 + 649 + 1882) mod 9973 = 6751
```

### Matrix barrier

1. The three row checksums must sum, mod 9973, to the grand checksum.
2. The three column checksums must sum, mod 9973, to the same grand checksum.
3. The diagonal (364, 364, 3867 in the example) must contain no repeated adjacent values other than the two `E` copies, which are expected.

If either direction disagrees with the grand checksum, one of the nine cells was copied incorrectly. Re-derive the offending cell from its source card — do not "fix" the checksum.

The parity matrix must be recomputed for every cycle with that cycle's `G_new`, `T`, and `P`.

## Stage M — Three-pass handoff review

### Review round A

Read Cards A, B, C, and D in that order.

At each transition, write one line:

```text
A to B: baseline label agrees
B to C: old generation agrees
C to D: new generation agrees
D to A: baseline label still agrees
```

Count how many transitions were checked. For this four-card review, the count must be four.

If a number disagrees, stop at that transition and correct the copied worksheet field. Preserve the old entry so the correction can be followed.

### Review round B

Read the cards in reverse order: D, C, B, A.

Check the same four relationships again, ending with the baseline label on Card D.

### Cold pass

Set the worksheet aside for **ten minutes**, then re-verify only the parity matrix and the handoff capsule without looking at your earlier notes. The cold pass catches errors that fresh eyes skip — a capsule reviewed in only one sitting is not fully reconciled.

The first pass is the **forward lineage walk**; the second is the **reverse retention walk**; the third is the **cold reconciliation pass**. All three must complete.

### Review barrier

Mark the handoff `REVIEWED` only after all three passes are complete.

If a correction was made during round B or the cold pass, repeat round A before marking it reviewed. An earlier review did not check the corrected value.

## Stage N — Branch counters

Create two local counters:

```text
a: number of completed review passes
b: number of additional worksheet consistency checks
```

For the worked example, use:

```text
a = 3
b = 5
```

The five additional checks are:

1. Baseline label is identical on all six cards.
2. Card B retains the old generation.
3. Card C retains the current cycle's generation.
4. Handoff ticket has been recalculated.
5. Retention proof has been recalculated.

Calculate the branch marker:

```text
N = (P + 13 * a + 17 * b) mod 65521
```

Example:

```text
N = (7568 + 13 * 3 + 17 * 5) mod 65521
N = 7692
```

Write:

```text
branch_marker: 7692
review_passes: 3
consistency_checks: 5
```

If the counters do not match the work actually completed, complete the missing checks. The counters validate the capsule; inflating them skips validation.

## Stage O — Two-phase commit

The commit stage seals the current cycle.

### Prepare phase

On Card D:

1. Confirm that the baseline was sealed.
2. Confirm that the simulated detach was recorded.
3. Confirm that the observer values were checked (both directions).
4. Confirm that the current cycle's reattach was recorded.
5. Confirm that the handoff was reviewed (all three passes).
6. Confirm that the parity matrix agrees in both directions.
7. Confirm that the branch counters are correct.
8. Write `PREPARED, NOT COMMITTED`.

Do not change any numbers after this marker.

### Commit phase

Calculate the final seal:

```text
F = (N + 23 * G_new + 5 * G_old) mod 65521
```

Example (Cycle I):

```text
F = (7692 + 23 * 255 + 5 * 128) mod 65521
F = 14197
```

Copy the final record into a new box:

```text
worksheet: OW-OBSERVATION-01
cycle: I
baseline_label: 364-3728-12
old_generation: 128
new_generation: 255
handoff_ticket: 3867
retention_proof: 7568
branch_marker: 7692
final_seal: 14197
state: CYCLE COMMITTED
```

After Cycles II and III are committed the same way, the three cycle records together form the **migration ledger**. Only the final cycle's `F` feeds the attestation.

## Stage P — Merkle digest chain

The digest chain links the entire migration into one tamper-evident sequence. Each link mixes in the previous link, so any edit anywhere breaks every later link.

Using the **final cycle's** values, compute on Card E:

```text
d0 = (E * 31 + C) mod 9973
d1 = (d0 * 7 + G_old) mod 9973
d2 = (d1 * 11 + G_new) mod 9973
d3 = (d2 * 13 + T) mod 9973
d4 = (d3 * 17 + P) mod 9973
d5 = (d4 * 19 + F) mod 9973
```

With the Cycle I worked example:

```text
d0 = (364 * 31 + 3728) mod 9973 = 5039
d1 = (5039 * 7 + 128) mod 9973   = 5482
d2 = (5482 * 11 + 255) mod 9973 = 719
d3 = (719 * 13 + 3867) mod 9973  = 3241
d4 = (3241 * 17 + 7568) mod 9973 = 2827
d5 = (2827 * 19 + 14197) mod 9973 = 8072
```

### Chain barrier

1. Recompute the chain from `d0` without looking at the first computation. Both chains must match link for link.
2. No link may equal zero.
3. `d5` must be recorded on Card E as the **chain head**.

If the two computations disagree at a link, that link's input was copied wrong. Fix the input from its source card and recompute from `d0` — never patch a single link in place.

## Stage Q — Commitment ladder

The ladder tests whether the committed migration is arithmetically independent of the observation digest.

Calculate the three rungs from the chain head:

```text
r1 = (d5 + N) mod 65521
r2 = (r1 * 3 + F) mod 65521
r3 = (r2 * 5 + K) mod 65521
```

With the worked example:

```text
r1 = (8072 + 7692) mod 65521 = 15764
r2 = (15764 * 3 + 14197) mod 65521 = 61489
r3 = (61489 * 5 + 63374) mod 65521 = 43214
```

### Ladder acceptance

1. Recompute `r3` independently; both results must match.
2. `r3` must **not** be divisible by 97. (In the example, `43214 mod 97 = 49`, so the rung stands.)
3. Record `r3` on Card F.

If `r3` is divisible by 97, the ladder has collapsed: the migration's cycle values are arithmetically dependent, and the rebuild will not admit the retained checkpoint. Restart from Stage K after a seven-minute pause with fresh calibration values — do not re-order the cycles to force a different `r3`.

## Stage R — Witness attestation

The witness chain proves the ledger was assembled in order, by binding the chain head, the determinant, and the branch marker into a second independent chain on Card F.

First compute the cross-cycle determinant (Stage S below), then:

```text
w0 = (d5 * 7 + Det) mod 9973
w1 = (w0 * 11 + N) mod 9973
w2 = (w1 * 13 + F) mod 9973
```

With the worked example (`Det = 5960`, from Stage S):

```text
w0 = (8072 * 7 + 5960) mod 9973 = 2626
w1 = (2626 * 11 + 7692) mod 9973 = 6659
w2 = (6659 * 13 + 14197) mod 9973 = 1034
```

### Witness barrier

1. Recompute the witness chain **twice**, once starting from `d5` and once starting from `d3` (re-deriving `d4`, `d5` first). Both computations must converge on the same `w2`.
2. No witness link may equal any digest-chain link.
3. Record `w2` on Card F.

If the two convergences disagree, a middle link was copied wrong. Fix the input and recompute both chains from their heads. The witness chain and the digest chain are independent by construction — they may never share a link value.

## Stage S — Cross-cycle determinant

The determinant proves the three generations are truly independent directions in the migration space. Collinear generations produce a zero determinant, and the rebuild treats a degenerate migration as a single resync.

On Card F, arrange the cycle matrix:

```text
| G1    G2    G3   |
| G_old G1    G2   |
| E     G_old G1   |
```

With the worked example (`G1 = 255`, `G2 = 352`, `G3 = 449`):

```text
| 255   352   449 |
| 128   255   352 |
| 364   128   255 |
```

Compute the determinant, reduced mod 9973:

```text
Det = 255 * (255 * 255 - 352 * 128)
    - 352 * (128 * 255 - 352 * 364)
    + 449 * (128 * 128 - 255 * 364)

Det = 4384107
Det mod 9973 = 5960
```

### Determinant barrier

1. `Det mod 9973` must be nonzero.
2. `Det mod 9973` must **not** be divisible by 7. (In the example, `5960 mod 7 = 3`, so the rung stands.)
3. Record `Det` on Card F.

If the determinant collapses to zero, the three cycles are degenerate — restart Stage K after seven minutes. Do not swap cycle order to force a nonzero determinant; the cycles must be committed in ascending order.

## Stage T — Ascension ladder and anchor

The ascension ladder binds the observation digest, commitment ladder, witness chain, and determinant into a single anchor value.

Calculate the four rungs on Card F:

```text
s1 = (r3 + Det) mod 65521
s2 = (s1 * 7 + w2) mod 65521
s3 = (s2 * 11 + K) mod 65521
s4 = (s3 * 13 + Det) mod 65521
```

With the worked example:

```text
s1 = (43214 + 5960) mod 65521 = 49174
s2 = (49174 * 7 + 1034) mod 65521 = 17647
s3 = (17647 * 11 + 63374) mod 65521 = 60928
s4 = (60928 * 13 + 5960) mod 65521 = 11772
```

### Anchor acceptance

1. Recompute `s4` independently; both results must match.
2. `s4` must **not** be divisible by 89. (In the example, `11772 mod 89 = 24`, so the rung stands.)
3. `s4` must **not** be divisible by 13. (In the example, `11772 mod 13 = 7`, so the rung stands.)
4. Record `s4` as the **anchor `A`** on Card F, beside the chain head and the witness head.

If `s4` fails either divisibility gate, the anchor is malformed: the attestation values are arithmetically dependent, and the rebuild will not admit the retained checkpoint. Restart from Stage K after a seven-minute pause — do not re-derive `s4` with substituted values.

---

# Part 3 — The final attestation

The anchor is not enough. Before the deferred rebuild is admitted, the entire construction must survive three more gates: a fold over the observation inputs, a mirror of the ascension ladder with inverted arithmetic, and a unification that binds everything into one value.

## Stage U — Quaternion fold

The fold mixes the four observation inputs — epoch, checkpoint residue, offset, and variation — into a single value that must be independent of the anchor. If the fold agrees too closely with the anchor, the observation and the migration are arithmetically coupled, and the rebuild reads the whole run as one context.

On Card F, compute:

```text
f1 = (E * 13 + C * 7) mod 9973
f2 = (Q * 11 + R * 17) mod 9973
f3 = (f1 * 19 + f2 * 23) mod 9973
```

With the worked example:

```text
f1 = (364 * 13 + 3728 * 7) mod 9973 = 909
f2 = (420 * 11 + 30 * 17) mod 9973 = 5130
f3 = (909 * 19 + 5130 * 23) mod 9973 = 5612
```

### Fold barrier

1. Recompute `f3` independently; both results must match.
2. `f3` must **not** be divisible by 7. (In the example, `5612 mod 7 = 5`, so the rung stands.)
3. `f3` must **not** be divisible by 11. (In the example, `5612 mod 11 = 2`, so the rung stands.)
4. `f3` must differ from the anchor `A`. (5612 vs 11772 — distinct, so the rung stands.)
5. Record `f3` on Card F.

If `f3` fails a divisibility gate or equals the anchor, the observation is coupled to the migration. Restart from Phase B1 after seven minutes — the fold is computed from calibration values, so the fix is a new calibration, not a new migration.

## Stage V — Mirrored ladder

The mirror recomputes the ascension ladder with **inverted arithmetic** — subtraction where the ladder added. A correctly assembled ledger produces a mirrored anchor that is different from, but consistent with, the original. A ledger containing any lucky wrong value fails the mirror even when it passes the original ladder.

On Card F, compute:

```text
m1 = (s4 - Det) mod 65521
m2 = (m1 * 7 - w2) mod 65521
m3 = (m2 * 11 - K) mod 65521
m4 = (m3 * 13 - Det) mod 65521
```

With the worked example:

```text
m1 = (11772 - 5960) mod 65521 = 5812
m2 = (5812 * 7 - 1034) mod 65521 = 39650
m3 = (39650 * 11 - 63374) mod 65521 = 45171
m4 = (45171 * 13 - 5960) mod 65521 = 57095
```

### Mirror barrier

1. Recompute `m4` independently; both results must match.
2. `m4` must differ from the anchor `s4`. (57095 vs 11772 — distinct, so the rung stands.)
3. `(m4 + s4) mod 97` must be nonzero. (In the example, `(57095 + 11772) mod 97 = 94`, so the rung stands.)
4. Record `m4` as the **mirrored anchor** on Card F.

If the mirror collapses — `m4` equals `s4`, or the sum gate fails — the ledger contains a value that satisfies the additive ladder only by accident. Restart from Stage K after seven minutes. Do not adjust any single value to repair the mirror; the mirror exists precisely to catch that.

## Stage W — Grand unification

The unification binds the anchor, the fold, and the witness head into one final value. This is the number the deferred rebuild actually keys on.

On Card F, compute:

```text
G = (s4 * 29 + f3 + w2) mod 65537
```

With the worked example:

```text
G = (11772 * 29 + 5612 + 1034) mod 65537
G = 20349
```

Note the modulus: **65537**, the Fermat prime — the only modulus in the entire method that is prime, and the only value that may not be reduced further.

### Unification gate

1. Recompute `G` independently; both results must match.
2. `G mod 17` must equal `phi`. (In the example, `20349 mod 17 = 0` and `phi = 0` — the gate stands. This congruence is the single strictest requirement in the method: the unification inherits the phase of the original calibration.)
3. `G mod 101` must be nonzero. (In the example, `20349 mod 101 = 48`, so the gate stands.)
4. Record `G` on Card F as the **unification value**, beside the anchor and the mirrored anchor.

If `G mod 17` does not equal `phi`, the run is **phase-broken**: the unification has drifted out of phase with the calibration that produced it. There is no local fix. Restart the entire method from Phase B1 — the calibration, the migration, and the attestation must all come from the same phase.

## Phase Z — The covenant

The closing protocol. It adds no arithmetic; it enforces that the record survives.

1. Copy the unification value `G` onto **three** separate places: Card F (already done), the bottom of Card A, and a fresh line at the top of Card D.
2. Read all three copies backward, digit by digit, and confirm they match.
3. Write the worksheet name, the date, and the words `COVENANT SEALED` beneath the third copy.
4. Begin the inventory protocol from Phase G, including the **+30 minute** final count.
5. Do not open any loot boxes until after the +30 minute count is recorded.

The covenant exists because a unification value that cannot be reproduced verbatim from the worksheet is worthless as evidence — for yourself, and for anyone you show the run to.

---

## Restart and invalidation rules

| Change or mistake | What becomes invalid | Where to resume |
| --- | --- | --- |
| A device clock was adjusted | The entire run, including the offset ladder | Phase 0. |
| Cadence jitter `J > 0.600` | Everything after Phase 0 | Phase 0.4 after practice. |
| Parity or drift budget failed | Everything after Phase 0 | Phase 0 after ten minutes. |
| Baseline display name was copied incorrectly | Every card referencing that label | Phase A. |
| Coarse, fine, or thermal calibration failed | Every number derived from the offsets | Phase B1 (restart all three passes). |
| `phi > 1` | The capsule's admission to the retention windows | Phase B1 after seven minutes. |
| Resonance filter found no candidate | The capsule | Phase B1 after seven minutes. |
| Countercurrent epochs re-coupled with coincident epochs | The separation proof | Phase D after seven minutes. |
| `Q` or `R` was copied incorrectly | Every number derived from those inputs | Phase C. |
| Old generation changed after detach | Old card, new card, handoff, matrix, markers, and seals | Stage I. |
| Observer rows were entered out of order | Observer confirmation marker | Stage J. |
| A cycle's generation collided with an earlier one | That cycle and every later stage | Stage K, current cycle. |
| New generation changed after review | Handoff, matrix, and all later markers | Stage K, current cycle. |
| A matrix direction disagrees with the grand checksum | That cycle's capsule | Stage L2, re-derive the cell. |
| One review pass was skipped | Review counters and everything derived from them | Stage M, current cycle. |
| A prepared value was edited | Prepare and commit markers for that cycle | Stage O, current cycle. |
| A digest chain link was patched in place | All three chains and both ladders | Stage P, recompute from `d0`. |
| The commitment ladder collapsed (`r3` divisible by 97) | The migration's cycle values | Stage K after seven minutes. |
| The witness chains did not converge | The witness chain and everything after it | Stage R, recompute from both heads. |
| The determinant collapsed to zero | The cycle structure | Stage K after seven minutes. |
| The anchor failed a divisibility gate | The entire attestation | Stage K after seven minutes. |
| The fold coupled to the anchor | The observation–migration independence | Phase B1 after seven minutes. |
| The mirror collapsed | The ledger's additive validity | Stage K after seven minutes. |
| The unification is phase-broken (`G mod 17 != phi`) | The entire run | Phase B1, full restart. |
| A covenant copy disagrees on read-back | The covenant (not the run) | Phase Z, re-copy and re-verify. |
| A real account link was changed | The retained checkpoint | Stop; the run must be restarted from Phase A on a fresh drop. |

### Rollback procedure

1. Find the last complete, checked card before the mistake.
2. Mark later records `SUPERSEDED`.
3. Do not erase them.
4. Start a new branch with a new worksheet name.
5. Copy only the last accepted inputs.
6. Recalculate every downstream value, including all three chains from their heads.

## Troubleshooting

| Outcome | Diagnosis | Fix |
| --- | --- | --- |
| Provisioning acceptance gate failed | Incomplete workstation preparation | Fix what `python capsule.py --check` names, then re-run it. Do not skip ahead to Phase 0. |
| Python prints `0,30000000000000004` | Regional decimal separator wrong | Set the decimal symbol to `.` (Control Panel > Region), reboot, re-run `python capsule.py --check`. |
| `'python' is not recognized` | The "Add python.exe to PATH" checkbox was skipped | Re-run the Python installer, check the box, reboot, re-run `python capsule.py --check`. |
| The script says a gate failed | The measured contexts genuinely failed it | Wait seven minutes, repeat the phase. Do not edit the measurements to pass a gate. |
| Drift spread too high | Device parity failure | Wait ten minutes, repeat Phase 0. Do not switch networks. |
| Cadence jitter too high | Operator inconsistency | Practice the 15-second cadence; restart Phase 0.4. |
| Coarse deltas outside the band | Context instability | Wait seven minutes, repeat B1. |
| Fine variance is too high | Observer phase noise | Wait seven minutes, repeat B1–B2. |
| Thermal gate fails | Offset drift over the long horizon | Wait seven minutes, restart from B1. |
| Baseline state changes | Checkpoint window closed | Restart from Phase A; the drop must be re-observed. |
| `phi > 1` | Input interference in the epoch arithmetic | Wait seven minutes, recalibrate. |
| No resonant candidate | Capsule has no in-phase epoch | Wait seven minutes, recalibrate. |
| Countercurrent epochs collide with coincident ones | Contexts re-coupled | Wait seven minutes, repeat Phase D both directions. |
| Observer epochs equal the baseline epoch | Contexts did not separate | Restart from Phase B1 after seven minutes. |
| A retention window fails | Residual drift or admission rule | Repeat that window after a five-minute pause. |
| Window-index checksum fails | Window not tied to the epoch ladder | Repeat the window; do not renumber it. |
| Window-separation lattice fails | Windows too close in value | Repeat the offending window after a five-minute pause. |
| Entropy sieve fails | Windows too regular | Wait seven minutes, rerun Phase E entirely. |
| Generation collision | No separation to reconcile | Restart Stage K after seven minutes. |
| Matrix disagrees in one direction | A copied cell is wrong | Re-derive the cell; do not fix the checksum. |
| Chain recomputation disagrees | A chain input was copied wrong | Fix the input; recompute from the head. |
| Ladder collapsed | Cycle values arithmetically dependent | Restart Stage K after seven minutes. |
| Witness chains diverge | A middle link is wrong | Fix the input; recompute both chains. |
| Determinant collapsed | Degenerate cycle structure | Restart Stage K after seven minutes. |
| Anchor failed a gate | Attestation values dependent | Restart Stage K after seven minutes. |
| Fold failed a gate or matched the anchor | Observation coupled to migration | Recalibrate from Phase B1. |
| Mirror collapsed | Ledger valid only additively | Restart Stage K after seven minutes. |
| Unification phase-broken | Run drifted out of phase | Full restart from Phase B1. |
| All stages pass but nothing changes | Reconciliation admission was not established | Verify the ledger, anchor, mirror, and unification; if correct, the drop may not be eligible — retry on a fresh drop. |
| The app signs you out | Presentation context expired | Sign in through the official interface; restart from Phase A. |

## Common questions

### Do I actually unlink and relink my accounts?

No. The unlink and relink are performed on the worksheet. Changing the real connection forces a full resync and destroys the checkpoint the method depends on.

### Do I really need Python if the script does the math?

Yes. `capsule.py` is the calculator: it computes `mu`, `sigma`, the checkpoint capsule, the resonance lock, and the observer epochs, and it refuses to continue when a gate fails — which is the difference between a run that fails in one minute and one that fails in three hours. You never write or edit any code; you install Python once and type numbers.

### Do I have to reboot after every install?

Yes — after each of the two. Driver and font state settles only after a full restart, and the Phase B2 variance budget inherits whatever the machine was still holding. A workstation that has not been rebooted is not a provisioned workstation.

### Is `capsule.py` safe to run?

Yes. It reads only the numbers you type, writes one file (`capsule-state.json`) next to itself, and has no network access. It never asks for, sees, or stores any account information.

### Can I do the arithmetic by hand instead?

You can — every formula in this guide is printed — but hand arithmetic is the leading cause of a collapsed capsule. The script also enforces the gates in order, so a mis-typed digit fails loudly at the phase where it happened instead of silently three phases later.

### Why three cycles?

The reconciliation treats a single-generation jump as a routine resync. A sequence of three committed generations with a nonzero cross-cycle determinant is what gets the old checkpoint classified as an incomplete migration rather than an obsolete one.

### Why the resonance filter?

The epoch arithmetic produces three mathematically valid capsules, but only one is in phase with the checkpoint residue. The other two pass every local check and then fail silently in the retention windows — the filter is what makes the difference visible before you spend hours on the windows.

### Why does the countercurrent pass exist?

Separation measured in one direction can be an artifact of which device you happened to refresh first. The countercurrent epochs must interleave without touching the coincident ones, or the two contexts have re-coupled and the migration collapses.

### Why the mirrored ladder?

The additive ascension ladder can be satisfied by a lucky wrong value. The mirror recomputes the ladder with inverted arithmetic — a value that passes both ladders is correct; a value that passes only one is an accident the rebuild will reject.

### Why must `G mod 17` equal `phi`?

The unification is the only value the deferred rebuild keys on, and it inherits the phase of the calibration that produced it. If the phase has drifted — through a mis-copied input anywhere in the six hours — the gate fails and the run is phase-broken. There is no local fix; that is the point.

### Why 65537?

It is the Fermat prime — the only prime modulus in the method. Every other reduction uses composite moduli, so a value that accidentally satisfies a composite gate can still fail the prime gate. The unification is the one step that must be exact.

### Can I put the calculated ticket into an account form?

No. The ticket, proof, matrix, chains, ladders, fold, mirror, and unification are worksheet values used to validate your capsule. They have no meaning in an account form.

### Would a second phone make it more reliable?

No. It creates more observations to compare, not additional entitlements. One coordinator and one observer is the stable configuration.

### Does switching Wi-Fi or mobile data create a new generation?

Not in this method. Generation numbers are calculated on the worksheet. Switching networks mid-run only adds timing variance, which can fail the calibration.

### What if I repeat the original claim?

Do not. Replaying the claim is transport duplication, which the backend deduplicates. The method works precisely because it avoids replaying the claim.

### Can I skip the cold pass if I'm in a hurry?

No. The cold pass is a required member of the review set; the branch counter `a = 3` includes it. A capsule reviewed in only one sitting is not fully reconciled.

### Can I fix a wrong digest link in place?

No. Patching a single link hides the original error and breaks the chain's tamper evidence. Re-derive the input and recompute from the head.

### Why does the witness chain start from d3 as well as d5?

Convergence from two different starting points is the attestation. A ledger assembled out of order converges from one head and diverges from the other.

### Can I re-order the cycles to fix a collapsed determinant?

No. The cycles must be committed in ascending order; a determinant computed over a reordered matrix validates a migration you did not actually perform.

### What if ordinary rewards arrive while I am doing this?

Record the observation separately. A reward arriving during a run is not proof of duplication — the duplicated grant arrives with the deferred rebuild after the unification stands.

### Why can't I open boxes between the inventory counts?

An opened box cannot be compared. The rebuild must be observed intact, or the run cannot be verified at all.

### Can a screenshot prove it worked?

A screenshot can show the inventory before and after the rebuild window. Keep the completed worksheet alongside it; the unification value is what ties the run to the method.

## Full worked example

Keep this table beside the worksheet to review the calculations independently.

| Field | Example value | Derived from |
| --- | --- | --- |
| `mu0` | 0.470 s | Coarse calibration (Phase B1). |
| `mu` | 0.420 s | Fine calibration (Phase B2). |
| `tau` | 0.445 s | Thermal settle (Phase B3). |
| `sigma` | 0.030 s | Fine calibration (Phase B2). |
| `Q` | 420 | Offset measurement. |
| `R` | 30 | Variation measurement. |
| `E` | 364 | Checkpoint formula in Phase C. |
| `phi` | 0 | Interference gate. |
| `C` | 3728 | Checkpoint formula in Phase C. |
| `L` | `364-3728-12` | Baseline epoch, checkpoint, and sample count. |
| Resonance | `E1` locked (364, 863, 365) | Phase C2 filter. |
| Observer row 1 | 407 | `m = 1`. |
| Observer row 2 | 420 | `m = 2`. |
| Observer row 3 | 433 | `m = 3`. |
| Observer row 4 | 446 | `m = 4`. |
| `S` | 51274 | Sum of the 40 accepted `cj` values. |
| `K` | 63374 | Retention digest. |
| `G_old` | 128 | Baseline epoch plus checkpoint, mod 991. |
| `G_new` (I) | 255 | Cycle 1 generation. |
| `G_new` (II) | 352 | Cycle 2 generation. |
| `G_new` (III) | 449 | Cycle 3 generation. |
| `T` | 3867 | Handoff-ticket calculation. |
| `P` | 7568 | Retention-proof calculation. |
| Matrix grand | 6751 | Parity matrix, Cycle I. |
| `a` | 3 | Completed review passes. |
| `b` | 5 | Additional local checks. |
| `N` | 7692 | Branch-marker calculation. |
| `F` | 14197 | Final-seal calculation, Cycle I. |
| `d0`–`d5` | 5039, 5482, 719, 3241, 2827, 8072 | Merkle digest chain. |
| `r1` | 15764 | Ladder rung 1. |
| `r2` | 61489 | Ladder rung 2. |
| `r3` | 43214 | Commitment ladder (`43214 mod 97 = 49`). |
| `Det` | 5960 | Cross-cycle determinant (`5960 mod 7 = 3`). |
| `w0`–`w2` | 2626, 6659, 1034 | Witness chain. |
| `s1` | 49174 | Ascension rung 1. |
| `s2` | 17647 | Ascension rung 2. |
| `s3` | 60928 | Ascension rung 3. |
| `A` = `s4` | 11772 | Anchor (`11772 mod 89 = 24`, `11772 mod 13 = 7`). |
| `f1` | 909 | Fold component 1. |
| `f2` | 5130 | Fold component 2. |
| `f3` | 5612 | Quaternion fold (`5612 mod 7 = 5`, `5612 mod 11 = 2`). |
| `m1` | 5812 | Mirror rung 1. |
| `m2` | 39650 | Mirror rung 2. |
| `m3` | 45171 | Mirror rung 3. |
| `m4` | 57095 | Mirrored anchor (`(m4 + s4) mod 97 = 94`). |
| `G` | 20349 | Unification (`20349 mod 17 = 0 = phi`, `20349 mod 101 = 48`). |

## Completion checklist

- [ ] Workstation provisioning (Part 0.5) acceptance gate passed: three `OK` lines from `python capsule.py --check`, and both reboots done.
- [ ] `capsule.py` produced the checkpoint capsule, the resonance lock, and the observer epochs for the run.
- [ ] The capsule archive was sealed after each completed part.
- [ ] PC or laptop requirement met.
- [ ] iOS or Android mobile-device requirement met.
- [ ] No passwords, tokens, cookies, or private account identifiers were recorded.
- [ ] No device clock was adjusted after Phase 0 began.
- [ ] Drift budget and interface parity passed.
- [ ] Cadence fingerprint `J` passed.
- [ ] Real account connections were left unchanged.
- [ ] Baseline observations were distinguished from calculated worksheet values.
- [ ] Coarse pass (B1) passed before the fine pass (B2) began.
- [ ] Fine admission ladder (all four rungs) passed.
- [ ] Thermal settle gate passed.
- [ ] `phi` was 0 or 1.
- [ ] Resonance filter locked exactly one candidate.
- [ ] Countercurrent epochs shared no value with coincident epochs.
- [ ] Four retention windows of ten samples each were accepted.
- [ ] Every window passed its index checksum, parity alternation, and lattice separation.
- [ ] Entropy sieve passed.
- [ ] Old-generation record was copied instead of overwritten.
- [ ] Simulated detach was marked only on the worksheet.
- [ ] Observer rows were calculated in order, both directions.
- [ ] All three cycles completed with distinct generations.
- [ ] Each cycle's handoff ticket and proof were recalculated independently.
- [ ] Each cycle's parity matrix agreed in both directions.
- [ ] All three review passes (forward, reverse, cold) were completed for each cycle.
- [ ] Branch counters matched the work recorded.
- [ ] Each cycle's prepare phase preceded its commit phase.
- [ ] The digest chain was recomputed link for link from `d0`.
- [ ] The commitment ladder stood (`r3` not divisible by 97).
- [ ] The witness chain converged from both starting heads.
- [ ] The cross-cycle determinant stood (nonzero, not divisible by 7).
- [ ] The anchor stood (`s4` not divisible by 89 or 13).
- [ ] The fold stood (gates passed, fold distinct from anchor).
- [ ] The mirror stood (`m4` distinct, sum gate nonzero).
- [ ] The unification stood (`G mod 17 == phi`, `G mod 101 != 0`).
- [ ] The covenant was sealed in triplicate and read back.
- [ ] The inventory protocol ran at +2, +6, +14, and +30 minutes without opening boxes.
- [ ] The in-game inventory was compared intact after the rebuild window.

---

*Found this useful? Star the repository, and share your successful runs — including your unification value — so others can reproduce the method.*
