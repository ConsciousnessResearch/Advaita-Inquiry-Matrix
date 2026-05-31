# Task 2 — Pedagogical Accuracy Assessment

*AIM's current pedagogical accuracy, expressed in terms of the Scherf library
(the General Theory). Final deliverable for Task 2. 2026-06-01.*

---

## 1. What this assessment covers

This assessment evaluates AIM's **diagnostic logic and prakriyā selection** against
the Scherf library's formal model. It does not attempt to assess AIM's longitudinal
stage and qualification machinery (*sādhana-catuṣṭaya*), which lies outside the
formal scope of the library (see design doc §9 boundary).

The yardstick is the Scherf library (Task 1): 129 axioms, verified in Lean 4. Findings
are expressed as: *fidelity* (AIM's design matches the formal model), *gap* (something
the library requires that AIM was missing — now corrected), or *outside scope* (AIM
operates legitimately beyond what the library can validate).

---

## 2. Diagnostic vocabulary — the adhyāsa taxonomy

**After Task 2 corrections, AIM's error taxonomy is formally complete.**

| Error type | Kośa / layer | Scherf correlate | Assessment |
|---|---|---|---|
| `deha-adhyasa` | *annamaya*, gross | `Superimposed(Annamaya, Y)` | Correct |
| `prana-adhyasa` | *prāṇamaya*, vital | `Superimposed(Pranamaya, Y)` | Correct |
| `manas-adhyasa` | *manomaya*, mental | `Superimposed(Manomaya, Y)` | Correct |
| `vijnana-adhyasa` | *vijñānamaya*, intellectual | `Superimposed(Vijnanamaya, Y)` | Correct |
| `ananda-adhyasa` | *ānandamaya*, causal | `Superimposed(Anandamaya, Y)` + AV15 border-flag | **Added — gap now closed** |
| `saksi-adhyasa` | (witness) | A13/AV18 violation | Correct; avoidance confirmed |
| `visaya-adhyasa-moksa` | liberation | Outside library scope | Retained on pedagogical authority |

The ānandamaya gap — the only diagnostic category the library revealed as missing —
is now corrected. AIM's taxonomy maps cleanly onto the full pañca-kośa as the library
models it.

---

## 3. Prakriyā selection — correctness by error type

### 3.1 Gross-body and vital errors (deha, prana)

**Verdict: correct.** The primary prakriyā at *sravana*/*adhikari* is `drg-drsya-viveka`
(seer-seen discrimination) — the classical pointing away from the gross body. The
*manana*-stage shift to `panca-kosa-viveka` is correct: the body-error at the
questioning stage calls for systematic kośa analysis. The *nididhyāsana* routing to
`witness-stabilization` is appropriate here (unlike the subtler errors) — at this
gross layer, establishing the witness is the correct direction.

### 3.2 Mental error (manas-adhyasa)

**Verdict: correct.** The *manana* routing to `witness-stabilization` is appropriate
for a student who has resolved the body-identity but is still caught in mind-identity.
The supporting `subject-object-analysis` and `svaprakasa-pointing` (the self-luminous
nature of awareness) are classically correct moves here.

### 3.3 Intellectual error (vijnana-adhyasa)

**Verdict: correct, with one important note.** The `avoid: ["mahavakya-analysis"]`
constraint is precisely right — the *vijñānamaya* identification is the understander
("I am the one who understands the teaching") and *more* analysis of the mahāvākya
reinforces rather than dissolves it. The primary `understander-inquiry` and
`seeker-inquiry` correctly turn the inquiry back on the understander-self. The
*nididhyāsana* routing to `seeker-dissolution` is appropriate.

*Note:* `vijnana-adhyasa` has no `sravana` or `adhikari` entries — it is correctly
restricted to *manana*/*nididhyāsana*, since identifying as the intellect requires a
student who has moved past gross misidentifications. The `select()` fallback for an
earlier-stage call returns an empty default rather than a routing — this is correct
behavior (confirmed by Task 2 tests).

### 3.4 Causal-body / bliss error (ananda-adhyasa) — NEW

**Verdict: correct (routing confirmed by philosophical authority, 2026-06-01).**

The *manana* routing to `avastha-traya` (three-states analysis) is the classical
approach: the causal body is precisely what "remains" in deep sleep, and the
deep-sleep analysis (Māṇḍūkya Upaniṣad / Śaṅkara's Māṇḍūkya Bhāṣya) is what
exposes the *ānandamaya* identification. The student who says "I slept happily, I
knew nothing" is identifying with the causal sheath.

The `avoid: bliss-as-goal-framing` constraint is essential: the characteristic
confusion at this layer is treating the bliss experienced in deep sleep (or in
*samādhi*) as the goal or as the Self. Śaṅkara is explicit (*ānandamayo'bhyāsāt*,
Brahma Sūtra 1.1.12): *ānandamaya* is a kośa rooted in *avidyā*, not Brahman.

The *nididhyāsana* avoidance of `witness-stabilization` mirrors `saksi-adhyasa`:
at this subtlest layer, stabilizing the witness-as-object would reinforce a refined
but still conditioned position. The dissolution (`anandamaya-negation`, `neti-neti`,
`witness-brahman-identity`) is the correct direction.

This error type is the root case — it borders the *mūlāvidyā* limit (Scherf library
§17.2(3), *anādi-avidyā*). The library marks it with `borders_limit`; AIM now
recognizes it as the subtlest and most fundamental diagnostic category.

### 3.5 Witness error (saksi-adhyasa)

**Verdict: correct — independently confirms library ruling 1.**

The routing avoids `witness-stabilization` and routes to `witness-brahman-identity`.
This is the precise correction: a student who has identified with the witness-position
("I am the witness") needs the dissolution of *that* position into non-dual identity,
not reinforcement of the witness as a refined object. AIM and the Scherf library
arrived at this independently and agree.

### 3.6 visaya-adhyasa-moksa

**Verdict: outside library scope; retained on AIM's pedagogical authority.**

The routing to `nitya-mukta-pointing` and the avoidance of `progressive-path-framing`
are pedagogically sound — pointing to the *nitya-mukta* (eternally free) nature of
the Self corrects the implicit assumption that liberation is something yet to be
produced. The library cannot validate this (§11(4): *mokṣa* as recognition, not
produced state, is outside formal scope), but the pedagogical direction is correct.

---

## 4. State machine — correctness of diagnostic logic

**Session open / active error probing:** correct. The engine probes the
highest-priority active error at session open; the priority ordering (high confidence,
recurring preferred) is pedagogically appropriate — persistent errors deserve
consistent attention.

**Stage-0 advancement logic** (`is_ready_for_adhikari`): correct. The decisive
qualifications (*mumukṣutva*, *viveka*, *śraddhā*, *śama*) mirror the classical
*sādhana-catuṣṭaya* prerequisites. The two-session minimum before advancement is
conservative in the right direction.

**Stage 1+ progression** (I2 — now corrected): the stub has been replaced with
conservative logic that advances only when characteristic errors for the current
stage are all weakening and at least two sessions have passed. This is formally
adequate though intentionally minimal; the progression logic is in the
*sādhana*-scaffolding zone outside formal scope.

**Resistance handling:** softening challenge level when resistance is detected is
pedagogically correct — the Advaita tradition consistently teaches that forcing
produces contraction.

---

## 5. Current pedagogical accuracy — summary

**Diagnostic categories:** now complete (all five sheaths + sākṣi + mokṣa marker).

**Prakriyā selection:** correct across all seven error types. The `avoid` constraints
are the most philosophically sensitive element — all are confirmed correct:
- `avoid: mahavakya-analysis` for vijnana-adhyasa ✓
- `avoid: witness-stabilization` for saksi-adhyasa ✓ (independently confirmed)
- `avoid: witness-stabilization` for ananda-adhyasa at nididhyāsana ✓ (confirmed)
- `avoid: bliss-as-goal-framing` for ananda-adhyasa ✓ (confirmed)
- `avoid: progressive-path-framing` for visaya-adhyasa-moksa ✓

**Gaps remaining** (structural, not correctness failures):
- The `anandamaya-negation` prakriyā name is new (no corpus entries for it yet). The
  `pancakosa-viveka` corpus fallback will serve until corpus entries are tagged with
  this prakriyā. This is a corpus coverage gap, not a logic error.
- AIM's corpus does not yet have entries specifically addressing the
  `karana-sarira-analysis` prakriyā (supporting, ananda-adhyasa/manana). Again, a
  corpus gap, not a routing error.

**Out-of-scope items** (noted but not evaluated):
- Stage/qualification progression logic (*sādhana-catuṣṭaya*)
- visaya-adhyasa-moksa routing (pedagogical authority, not formally validatable)
- Dialogue generation and tone calibration (LLM layer, outside the state machine)

---

## 6. What Task 3 validation will cover

With both the library (Task 1) and the corrected AIM (Task 2) in hand, Task 3 will
validate:
- All five sheath diagnostics (including *ānandamaya*) against the library's
  `check_sheath_superimposition()`
- The epistemic-level classification of AIM's corpus routing (`ontological_scope`
  → `Level_of` Vyav/Prat vs. Param)
- The sākṣi and *nididhyāsana* constraints against library AV18/A13 checks
- Edge cases: what happens when errors co-present, when regression is observed,
  when the corpus returns no results

Task 3 will **not** cover: stage/qualification logic, visaya-adhyasa-moksa routing,
or the LLM layer.

---

*Author: Dev Bhagavān / SpecStudio. Drafted with Claude Sonnet 4.6.*
