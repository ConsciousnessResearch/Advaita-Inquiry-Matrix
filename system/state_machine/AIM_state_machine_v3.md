# AIM State Machine v3 — Consolidated Design

**Supersedes:** `AIM_student_state_machine_v2.md`, `initial_state_model_v2.md`,
`cognitive_error_machine.md`  
**Status:** Canonical  
**Date:** 2 May 2026

---

## 1. Design Principles

**The goal of AIM is avidyā-nivṛtti — the removal of ignorance — not
philosophical education.** This distinction governs every design decision in
this document.

A curriculum model asks: where is the student in the sequence of teachings?
AIM asks: which specific form of superimposition (adhyāsa) is obscuring the
Self right now, and what removes it?

The traditional parallel is the Āyurvedic physician. He does not run through
the anatomy curriculum. He diagnoses the specific condition of this patient
and prescribes accordingly. The Upaniṣadic guru does the same: Yājñavalkya
teaches Maitreyī differently than he teaches Janaka, not because they are at
different stages of a curriculum, but because the specific veil is different.

Three corollaries follow from this:

1. **The primary diagnostic input is the presenting error**, not the student's
   stage. Stage constrains the register of the correction; the error determines
   its target.

2. **Progress is measured by weakening of ignorance**, not by accumulation of
   understanding. A student who correctly articulates the teaching may still be
   fully identified. Verbal understanding is not a completion signal.

3. **The state machine tracks two things simultaneously**: the student's
   longitudinal position across sessions (which layer of ignorance is
   predominantly operative overall), and the presenting error within a session
   (which specific form of adhyāsa is active right now). These can differ.

---

## 2. System Architecture

AIM operates as three coordinated layers. The state machine is the middle layer.

```
Student (natural language, any language)
        ↕  natural language
  ┌─────────────────────────────┐
  │     LLM Chat Layer          │  — understands idiom, tone, language
  │  (frontier-class model)     │  — extracts structured signals (inbound)
  │                             │  — generates natural responses (outbound)
  └─────────────────────────────┘
        ↕  structured signals / directives
  ┌─────────────────────────────┐
  │     State Machine (this doc)│  — diagnoses longitudinal state
  │                             │  — identifies presenting error
  │                             │  — selects prakriyā
  │                             │  — routes to corpus
  │                             │  — manages student record
  └─────────────────────────────┘
        ↕  queries / records
  ┌─────────────────────────────┐
  │  Corpus + Student Records   │  — corpus_database.json
  │                             │  — students/{id}.json
  └─────────────────────────────┘
```

**The LLM layer is not a pass-through.** It performs two substantive jobs:

- **Inbound**: converts the student's natural language into structured signal
  payloads the state machine can reason over — error markers, recognition
  markers, resistance patterns, register assessment.

- **Outbound**: converts the state machine's structured directives into
  natural, pedagogically calibrated language — appropriate tone, register,
  integration of corpus passages.

The state machine never touches natural language directly. It reasons over
structured inputs and returns structured outputs. This is why a frontier-class
LLM is required: the inbound extraction task — detecting vijñānamaya-adhyāsa
from idiomatic English, or sākṣi-adhyāsa from spiritual language — requires
genuine domain comprehension, not pattern matching.

The state machine is called **multiple times per session** (event-driven),
not only at open and close.

---

## 3. Interfaces

### 3.1 LLM → State Machine (Input Signal Payload)

Every call from the LLM to the state machine sends a typed event payload.

```yaml
# --- SESSION OPEN ---
event_type: session_open
student_id: string
session_id: string
timestamp: ISO-8601

# --- MID-SESSION SIGNAL ---
event_type: signal
student_id: string
session_id: string

signal:

  # What form of adhyāsa is presenting
  error_markers:
    - type: >
        deha-adhyasa | prana-adhyasa | manas-adhyasa |
        vijnana-adhyasa | saksi-adhyasa | visaya-adhyasa-moksa
      confidence: high | medium | low
      evidence: string   # brief description: what in the exchange triggered this

  # Signs that ignorance may be weakening
  recognition_markers:
    - type: >
        verbal_understanding | spontaneous_application |
        resistance_absent | question_layer_shifted | seeker_loosening
      confidence: high | medium | low
      evidence: string

  # Resistance patterns
  resistance:
    present: boolean
    type: >
      deflection | spiritual_bypass | topic_shift |
      intellectual_counter | rehearsed_acceptance | silence

  # Apparent adhikāra from this exchange
  register:
    adhikara_apparent: sarva | madhyama | uttama
    emotional_tone: distressed | curious | engaged | resistant | open | absorbed

  # What the student did
  student_statement_type: question | assertion | objection | recognition | request | silence
  student_content_summary: string   # LLM-generated 1-2 sentence summary

# --- SESSION CLOSE ---
event_type: session_close
student_id: string
session_id: string

session_summary:
  errors_presented:
    - type: string
      status_at_close: active | weakening | possibly_resolved
  prakriyas_applied:
    - name: string
      target_error: string
      apparent_effect: receptive | resistant | partial | unclear
  new_errors_surfaced: [string]
  regression_observed: boolean
  recognition_events: [string]   # any aparokṣa moments observed
  notes: string
```

**Critical constraint on error_markers:** The LLM must distinguish between
a student *articulating* a correct understanding and a student *presenting*
de-identification. The former is `verbal_understanding` in recognition_markers;
the latter is the absence of an active error_marker. These are not the same.
A student who says "I understand I am not the body" while exhibiting
fear-of-death language is still presenting deha-adhyāsa. The LLM must
report both simultaneously and let the state machine resolve the conflict.

---

### 3.2 State Machine → LLM (Output Directive Payload)

```yaml
# Returned on session_open or signal events

longitudinal_state:
  stage: adhikari | sravana | manana | nididhyasana | jnana-nistha
  confidence: high | medium | low
  last_updated: ISO-8601

presenting_error:
  type: string         # from error taxonomy (Section 6)
  layer: gross | vital | mental | intellectual | subtle | liberation
  status: active | weakening | resolved | none
  is_recurring: boolean  # seen in prior sessions

prakriya:
  primary: string      # from prakriyā vocabulary (Section 7)
  supporting: [string]
  avoid: [string]      # prakriyās contraindicated for this error/stage combination

corpus_routing:
  pedagogical_stage: sravana | manana | nididhyasana
  prakriya: string
  adhikara_level: sarva | madhyama | uttama
  ontological_scope: dual-register | paramarathika
  preferred_unit_ids: [string]   # optional; specific IDs when precision matters

intervention:
  tone: orientation | explanation | debate | contemplative | affirmation
  depth: gross | subtle
  challenge_level: gentle | moderate | direct
  use_analogy: boolean
  use_scripture: boolean

session_directive:
  type: continue | open_probe | flag_regression | redirect | close_session
  probe_target: string      # if open_probe: which error to test
  probe_rationale: string
  redirect_domain: string   # if redirect: which qualification(s) are deficient
  notes: string
```

---

## 4. Student Record Schema

One JSON file per student, stored at `students/{student_id}.json`.

```json
{
  "student_id": "string",
  "created": "ISO-8601",
  "last_session": "ISO-8601",

  "longitudinal_state": {
    "stage": "purva-adhikari | adhikari | sravana | manana | nididhyasana | jnana-nistha",
    "confidence": "high | medium | low",
    "last_updated": "ISO-8601",
    "basis": "string — what evidence this assessment rests on"
  },

  "qualification_status": {
    "viveka": {
      "status": "absent | developing | present",
      "last_assessed": "ISO-8601",
      "evidence": ["string"],
      "corpus_applied": ["string"]
    },
    "vairagya": {
      "status": "absent | developing | present",
      "last_assessed": "ISO-8601",
      "evidence": ["string"],
      "corpus_applied": ["string"]
    },
    "sat_sampat": {
      "sama":       { "status": "absent | developing | present", "evidence": ["string"] },
      "dama":       { "status": "absent | developing | present", "evidence": ["string"] },
      "uparama":    { "status": "absent | developing | present", "evidence": ["string"] },
      "titiksa":    { "status": "absent | developing | present", "evidence": ["string"] },
      "sraddhа":    { "status": "absent | developing | present", "evidence": ["string"] },
      "samadhana":  { "status": "absent | developing | present", "evidence": ["string"] }
    },
    "mumuksutva": {
      "status": "absent | developing | present",
      "last_assessed": "ISO-8601",
      "evidence": ["string"],
      "corpus_applied": ["string"]
    }
  },

  "active_errors": [
    {
      "error_type": "string",
      "layer": "string",
      "first_observed": "ISO-8601",
      "last_observed": "ISO-8601",
      "observation_count": "integer",
      "status": "active | weakening | resolved",
      "weakening_evidence": ["string"],
      "prakriyas_applied": ["string"]
    }
  ],

  "resolved_errors": [
    {
      "error_type": "string",
      "resolved": "ISO-8601",
      "resolution_basis": "string — what markers indicated resolution"
    }
  ],

  "session_history": [
    {
      "session_id": "string",
      "date": "ISO-8601",
      "errors_presented": ["string"],
      "prakriyas_applied": ["string"],
      "qualification_focus": "string",
      "response_quality": "receptive | resistant | mixed",
      "recognition_events": ["string"],
      "state_at_close": "string",
      "summary": "string"
    }
  ],

  "notes": "string"
}
```

**On the `basis` field in longitudinal_state:** The state machine must not
advance the longitudinal state on the basis of a single session. The `basis`
field records what cross-session evidence supports the current assessment.
Stage advancement requires sustained markers across at least two sessions.

---

## 5. Session Lifecycle

### 5.1 Session Open

On receiving `event_type: session_open`:

1. Load student record from `students/{student_id}.json`. If no record exists,
   create one with longitudinal_state: `purva-adhikari`, confidence: low, and
   all qualification_status fields initialized to `absent`.

2. **Branch on longitudinal stage:**

   **If stage is `purva-adhikari`:**
   - Review `qualification_status`. Identify which qualifications are `absent`
     or `developing`.
   - Priority order for the opening probe: mumukṣutva → śraddhā → viveka →
     vairāgya → ṣaṭ-sampat (target the most decisive deficiency first).
   - Issue `session_directive: redirect` with `redirect_domain` set to the
     highest-priority deficient qualification.
   - The LLM conducts the probe as warm, open conversation — not as an
     assessment. The goal is to understand where the student is, not to
     evaluate or correct them immediately.
   - If all qualifications are `present`, update stage to `adhikari` and
     proceed as below.

   **If stage is `adhikari` or later:**
   - Review `active_errors` from prior sessions. Identify any errors with
     status: `active` that were not resolved at last close.
   - Issue `session_directive: open_probe` with probe_target set to the
     highest-priority unresolved error.
   - The LLM conducts the probe as natural conversation — not as a test.

3. Return the full directive payload with current longitudinal_state and
   the opening directive.

**Purpose of the opening probe:** For Stage 0 students, the opening
exchanges orient the session toward the qualification most in need of
support, based on what was recorded at the last close. For Stage 1+
students, the probe tests whether previously-active errors are still
present. In both cases, the LLM reads the student's responses without
announcing what it is looking for.

### 5.2 Session Run (Event-Driven)

The LLM calls the state machine whenever it detects a significant signal:
- A new error pattern emerges that wasn't in the active_errors list
- A recognition marker appears (possible weakening)
- The student's resistance changes materially
- The register shifts (adhikāra apparent changes)
- A regression signal appears

The state machine processes the signal and returns updated directives.
The LLM does not wait for a session end to get new routing — it calls
the state machine in real time as the conversation develops.

**The state machine does not update the student record mid-session.**
Record updates happen only at session close, based on the full session
summary. Mid-session calls update the directive but not the persistent record.

### 5.3 Session Close

On receiving `event_type: session_close`:

1. Process the session_summary from the LLM.

2. **Branch on longitudinal stage:**

   **If stage is `purva-adhikari`:**
   - Update `qualification_status` for each qualification that was engaged
     this session:
     - If new evidence of the qualification operating: update status toward
       `developing` or `present`, append evidence.
     - If the qualification remained absent despite gentle probing: status
       remains `absent`, append session note.
     - Update `corpus_applied` with any passage IDs used this session.
   - Record `qualification_focus` in session_history entry.
   - Assess stage transition: if mumukṣutva, śraddhā, viveka, and sufficient
     śama are all `present` or `developing` with consistent positive evidence
     across at least two sessions, advance to `adhikari`. Update
     longitudinal_state with basis.

   **If stage is `adhikari` or later:**
   - Update `active_errors`:
     - For each error presented: update `last_observed`, increment
       `observation_count`, add any new prakriyās applied.
     - For errors showing weakening evidence: update status to `weakening`,
       append weakening_evidence.
     - For errors with strong resolution indicators: update status to
       `resolved`, move to `resolved_errors` at next session open if
       no recurrence.
   - Assess longitudinal_state update:
     - Do not advance stage on one session alone.
     - Advance only when: (a) the errors characteristic of the current
       stage show weakening or resolution across multiple sessions, AND
       (b) the markers characteristic of the next stage have appeared.
     - Regression: if errors characteristic of an earlier stage appear
       persistently, update stage downward with basis noted.

3. Append session to `session_history`.

4. Write updated record to `students/{student_id}.json`.

---

## 6. Longitudinal State Model

The five stages are not curriculum phases. They describe which layer of
ignorance is predominantly operative. A student's stage tells the engine
**how to deliver** the correction; the presenting error tells it **what**
to correct.

---

### Stage 0: Pūrva-adhikāri (Pre-Qualification)

**Ignorance operative:** The four prerequisites for Vedāntic inquiry
(sādhana-catuṣṭāya) are absent or insufficiently established. The student
may be sincere, but the teaching cannot function as a pramāṇa for someone
who has not yet developed the ground on which it can land.

This is not a judgment on the student's worth or potential. Delivering the
non-dual teaching at this stage risks intellectual appropriation — the student
collects the concepts without transformation, which can harden the error.
The engine recognizes the gap without dismissing the student.

**Diagnostic signals by qualification:**

**(i) Viveka — discrimination between nitya and anitya:**
- No operative sense that worldly gains are impermanent
- Material success, relationships, or experiences sought as genuinely
  satisfying and complete; their transience not confronted
- Pleasure and pain treated as the final standard of value
- The question "is this pursuit ultimately satisfying?" has not arisen
  or generates no pull

**(ii) Vairāgya — dispassion from the fruits of action (here and hereafter):**
- Spiritual interest is instrumental: seeking peace, health, performance,
  relationships, powers, or relief from suffering — not Self-knowledge
- Spirituality is supplementary to worldly pursuit, not its replacement
- Attachment to outcomes strong and unquestioned; no operative dispassion
- Mokṣa or enlightenment conceived as a superior experience or altered
  state, not as the removal of ignorance
- Motivation remains clearly experiential even after the correct goal
  has been introduced

**(iii) Ṣaṭ-sampat — sixfold inner disciplines:**
- **Śama (tranquility):** Mind grossly agitated; unable to sustain
  reflection for more than a few exchanges; constant stimulation-seeking;
  no capacity to sit with a question
- **Dama (sense restraint):** Gross sense indulgence that is not
  questioned; addictive patterns operative and ego-syntonic
- **Uparama (equanimity):** Unable to hold any view without high
  reactivity; every exchange becomes personal or emotionally volatile
- **Titikṣā (endurance):** Cannot sit with discomfort or uncertainty;
  immediate relief-seeking at any friction; difficulty in the teaching
  generates withdrawal rather than inquiry
- **Śraddhā (receptivity to śāstra):** Hostility or indifference to
  scriptural authority; āgama-pramāṇa not accepted as a valid means of
  knowledge; the student approaches the teaching as a skeptical consumer
  of ideas rather than as a mumukṣu
- **Samādhāna (sustained application):** Cannot sustain attention on a
  single inquiry; frequent topic-shifting; conversation remains scattered
  across unrelated concerns

**(iv) Mumukṣutva — intensity of desire for liberation:**
- No genuine jijñāsā for the nature of Self; Self-inquiry feels abstract
  or irrelevant
- Liberation not conceived as the primary goal, nor even a clear secondary goal
- No existential urgency around bondage; suffering is practical, not ontological
- Spiritual seeking is social, therapeutic, or intellectual — not aimed at
  Self-knowledge
- "What am I?" generates no pull

**Assessment threshold:** The engine does not require all four to be absent
before redirecting. The two decisive indicators are:

1. **Mumukṣutva absent or purely instrumental** — without genuine desire
   for Self-knowledge, no other routing is effective.
2. **Śraddhā absent** — if pramāṇa as a means of knowledge is rejected,
   the teaching cannot land regardless of other factors.

If mumukṣutva is genuinely present but other qualifications are weak, the
student is borderline: partial engagement with the teaching alongside
orientation to the preliminaries is appropriate. The engine does not issue
a hard redirect in this case — it interlaces.

**What the engine does:**
- Does not deliver the central Vedāntic teaching (ātman = Brahman,
  non-dual consciousness)
- Identifies which specific qualifications are deficient from the
  diagnostic signals and routes `redirect_domain` accordingly
- Issues `session_directive: redirect` with the deficient qualification named
- Routes to corpus passages that:
  (a) arouse viveka by pointing at impermanence (Katha, Gītā 2.14-2.16)
  (b) describe the qualified seeker so the student can self-assess
      (Vivekacūḍāmaṇi opening verses)
  (c) orient toward karma-yoga as the path of purification (Gītā 2.47, 3.19)
  (d) establish what the inquiry is actually for and why it matters
- Uses the Naciketas narrative (Katha 1.1-1.29) as a primary orientation
  passage: the student who passes through Yama's worldly offers and asks
  for the teaching anyway is the model of mumukṣutva

**Transition to Stage 1 (Adhikāri):**
- Mumukṣutva operative: genuine jijñāsā for Self-knowledge, not instrumental
- Śraddhā present: willingness to engage śāstra as pramāṇa
- Sufficient śama that inquiry can be sustained across exchanges
- Viveka operative: impermanence has been personally confronted
- Vairāgya at minimum intellectually established (full vairāgya is rare
  and not required for inquiry to begin)

---

### Stage 1: Adhikāri (Pre-Inquiry)

**Ignorance operative:** Gross superimposition fully active. The teaching
(ātman = Brahman, non-dual nature of consciousness) has not been heard in
a way that challenges identification. Pramāṇa (scriptural testimony as a
valid means of Self-knowledge) not yet accepted.

**Structural markers:**
- Deha-bhāvana (body-feeling) is the primary self-sense, unexamined
- Doership (kartṛtva) and enjoyership (bhoktṛtva) unquestioned
- External validation-seeking active
- Death treated as annihilation of self
- Spiritual interest may be present but is experiential in motive
  (seeking states, peace, powers) rather than inquiry into the nature of Self

**What the engine does:**
- Establishes existential urgency (saṃvega) without inducing despair
- Problematizes body-identification through analogy and reflection
- Introduces pramāṇa as a valid epistemological tool
- Does NOT deliver the central non-dual teaching prematurely —
  the student is not yet positioned to receive it

**Transition to śravaṇa:**
- Student accepts śāstra-pramāṇa as a valid means of Self-knowledge
- Jijñāsā (desire to know the Self) is genuine, not experiential
- Body-identification has been problematized even if not removed

**Regression from śravaṇa back to adhikāri:**
- Withdrawal of śraddhā; rejection of pramāṇa
- Major existential disruption that fully reasserts gross identification
- Return to purely experiential or worldly orientation

---

### Stage 2: Śravaṇa (Hearing)

**Ignorance operative:** The central teaching has not yet been correctly
understood at the intellectual level. Śravaṇa is not merely "the student is
listening" — it describes a condition in which the correct knowledge is
simply absent from the mind, or present in distorted form.

Paradoxically, the transition out of śravaṇa is signaled by the arising
of doubts and objections. You can only doubt what you have heard.

**Structural markers:**
- Student can engage the teaching but cannot yet articulate it cleanly
- Questions are about what the teaching is, not objections to it
- Philosophical dualism is present but not yet interrogated
- Analogy and scripture are needed before direct pointing lands

**What the engine does:**
- Delivers the teaching clearly using the appropriate prakriyā for
  the student's background and apparent adhikāra
- Uses analogy, scripture, phenomenological pointing
- Does not debate until the teaching has been heard — debate before
  hearing consolidates the wrong position

**Transition to manana:**
- Student can articulate the central teaching accurately
- Doubts and objections begin to arise (the signal śravaṇa is complete)
- The question shifts from "what is this teaching?" to "but how can this be?"

**Regression:**
- Return to śravaṇa from manana: intellectualization without any
  personal engagement; student returns to concept-collection mode

---

### Stage 3: Manana (Reflection)

**Ignorance operative:** The teaching has been heard but not settled.
Intellectual non-assimilation. The mind generates doubts and objections
from prior conditioning, competing worldviews, habitual dualism.

This stage is characterized by the intellect (vijñāna) as the primary
site of conflict. The student knows the teaching but the mind keeps
producing counter-arguments: "But I feel so limited"; "What about
individuality?"; "Doesn't this make ethics meaningless?"

**Structural markers:**
- Student can state the teaching but it hasn't overridden the felt
  sense of separation
- Philosophical objections arise with genuine force
- The intellect is engaged and active — this is correct; it should be
- Vijñāna-adhyāsa is prominent: the understander-identity is strong

**What the engine does:**
- Engages objections directly; does not bypass or dismiss them
- Logical refutation, ontological investigation, debate where appropriate
- Addresses the vijñāna-adhyāsa that is typical of this stage
- Does not move to nididhyāsana prematurely — unresolved doubt
  resurfaces and blocks contemplation

**Transition to nididhyāsana:**
- Intellectual objections addressed and settled
- No significant philosophical counter-arguments remain
- The student says something like: "I understand this intellectually
  but it doesn't hold in daily life / I don't feel it"
  (this is the exact signal: understanding without de-identification)

**Regression:**
- To śravaṇa: student needs the teaching restated before objections
  can be engaged
- New subtle objections requiring fresh intellectual work before
  contemplation can proceed

---

### Stage 4: Nididhyāsana (Contemplation)

**Ignorance operative:** Intellectual doubt resolved, but the living
identification persists as a habitual functional reality. The understanding
hasn't penetrated to the level where misidentification actually lives.

This is the subtlest and often longest stage. The student applies the
teaching in contemplation but reverts to identification under stress, in
relationships, in embodied experience. The errors are now subtler:
vijñāna-adhyāsa (the seeker-identity), sākṣi-adhyāsa (witness
reification), and viṣaya-adhyāsa on mokṣa (liberation as future object).

**Structural markers:**
- Student reports understanding the teaching but "not living it"
- Recognition events (aparokṣa glimpses) may occur but don't stabilize
- Under stress, identification reasserts
- Spiritual seeking may intensify — the seeker-identity is strong
- "When will I realize?" type questions appear

**What the engine does:**
- Sustained contemplative guidance; attention reversal
- Neti-neti at subtler levels (not body, but witness, understander)
- Addresses sākṣi-adhyāsa: the witness cannot be witnessed
- Addresses viṣaya-adhyāsa: liberation is not a future event
- Helps the student observe identification arising in real time
- Guards against ego-reconstitution around "awakening" or insight

**Transition to jñāna-niṣṭhā:**
- Recognition event with sustained aftermath (S5a → S5b distinction)
- Under stress, the center of gravity holds
- The student stops seeking liberation as a future experience
- The seeker-identity loses its grip without effort

**Note on regression from this stage:**
What appears as regression from nididhyāsana is often the surfacing of
a subtler layer of identification that was previously obscured. The engine
must distinguish genuine regression (return to gross identification with
no contemplative access) from layer-peeling (subtler adhyāsa becoming
visible as grosser ones thin).

---

### Stage 5: Jñāna-niṣṭhā (Stabilized Knowledge)

**Ignorance operative:** The fundamental misidentification has been removed.
Residual vāsanās (conditioning patterns) may still be active functionally,
but they no longer constitute an ontological error. Adhyāsa has collapsed.

**Structural markers:**
- Functional engagement with the world without ontological confusion
- Fear of death no longer operative at the identity level
- No longer seeking liberation as a future event or experience
- Emotional reactivity may remain but is not identity-constituting
- The student no longer needs to be convinced — they are established

**What the engine does:**
- Minimal intervention; poetic affirmation
- Addresses remaining vāsanās without treating them as ignorance
- The relationship shifts from corrective to celebratory and refining

---

### Transition and Regression Summary

```
Forward:
  purva-adhikari → adhikari  : mumukṣutva operative + śraddhā present + sufficient śama
  adhikari → sravana         : jijñāsā established + pramāṇa accepted
  sravana → manana           : teaching heard + doubts arising
  manana → nididhyasana      : objections resolved + identification persisting
  nididhyasana → jnana       : recognition event + sustained de-identification

Regression:
  Any stage → purva-adhikari : collapse of śraddhā + vairāgya + mumukṣutva simultaneously
                               (rare; usually only one or two qualifications regress)
  Any stage → adhikari       : severe trauma / ego-reconstitution / śraddhā withdrawal
  sravana → adhikari         : pramāṇa rejected
  manana → sravana           : concept-collection mode; no personal engagement
  nididhyasana → manana      : new subtle objections requiring intellectual work
  nididhyasana → nididhyasana (layer-shift): subtler adhyāsa surfacing — not regression
```

---

## 7. Error Taxonomy

The six forms of adhyāsa, organized by the layer of identification they
concern. Each has a gross and subtle form. The longitudinal stage determines
which form is presenting and which register of correction is accessible.

---

### 7.1 Deha-adhyāsa — Body Superimposition

**Gross form:** Explicit body-identity. "I am this body."

**Subtle form:** Somatic-referenced identity. Emotional states are
experienced as physically located and identity-constituting. Health,
appearance, and physical fate are felt as threats to self.

**Diagnostic signals:**
- Fear of pain, illness, aging, death as existential (not merely practical)
- Physical appearance as self-defining
- "What will happen to me when I die?"
- Health anxiety that functions as identity-anxiety
- Strong reactivity to bodily change or limitation

**Correction by stage:**
- Adhikāri/Śravaṇa: gross seer-seen discrimination; the body is an
  object of perception — what perceives is not what is perceived;
  chariot metaphor (body as chariot, Self as rider)
- Manana: pañcakośa-viveka — annamaya layer is the outermost sheath,
  not the Self; avasthātraya — body is absent in dreamless sleep,
  yet "I" persist
- Nididhyāsana: sustained witness-of-body contemplation; neti-neti
  at the somatic level; under what conditions does body-identification
  reassert, and what is aware of that?

**Weakening indicators:**
- Fear of death/illness no longer generates existential panic (practical
  concern may remain; ontological panic diminishes)
- Body problems no longer feel like threats to identity
- Under physical stress, the identification doesn't fully reassert
- The student stops conflating body-fate with Self-fate

---

### 7.2 Prāṇa-adhyāsa — Vital-Force Superimposition

**Description:** Identification with the life-force: survival anxiety not
tied to specific physical threat; existential terror without clear object;
clinging to continuation as an identity-stake.

**Diagnostic signals:**
- Survival anxiety as background hum, not tied to specific physical threat
- "What if everything falls away?" — existential without object
- Breathwork or aliveness-practices that reinforce the life-force as self
- Fear of unconsciousness, deep sleep, dissolution

**Correction:**
- Prāṇa as object of perception; the witness of prāṇa is not prāṇa
- Prāṇa absent in dreamless sleep; the "I" persists across that absence
- Avasthātraya: which "I" is present in each state?

**Weakening indicators:**
- The existential terror around dissolution diminishes
- The student can contemplate deep sleep or cessation without panic

---

### 7.3 Manas-adhyāsa — Mind/Emotional Superimposition

**Description:** Identification with mental states and emotional experience.
Emotions are felt as identity-constituting. Mental quietude is sought as
a prerequisite for Self-knowledge.

**Diagnostic signals:**
- "I feel anxious/sad/angry — that is what I am right now"
- Emotions treated as evidence about the Self
- "My mind is too scattered to realize"; "when my mind is quiet I will know"
- Mood-tracking as self-tracking
- Strong identification with psychological history and narrative

**Common trap:** The student who seeks a quiet mind as prerequisite for
Self-knowledge is presenting manas-adhyāsa. The mind is still central —
the error is that the Self depends on the mind's condition. This is subtle
because it appears as a spiritual practice rather than an error.

**Correction:**
- Thoughts and emotions as objects in awareness; the observer of thoughts
  is not the thoughts
- Waking-dream comparison: emotional states arise and pass like dream objects
- The Self is self-luminous (svaprakāśa) — its nature does not depend on
  the mental weather
- Neti-neti: "not this emotion, not that thought — what remains?"

**Weakening indicators:**
- Emotional states no longer feel identity-constituting
- Strong emotions arise without "I am this state"
- The student stops seeking mental quietude as prerequisite
- The student reports watching emotions without being them
- Questions shift from "how do I calm my mind?" to "what is aware of the mind?"

---

### 7.4 Vijñāna-adhyāsa — Intellect/Understander Superimposition

**Description:** Identification with the intellect, the understanding
function, or the seeker-identity. This is the dominant error of the manana
stage and the primary obstacle to transition into nididhyāsana.

**Gross form:** "I understand Advaita" — treating comprehension as arrival.

**Subtle form:** The seeker-identity — "I am the one who is inquiring /
practicing / seeking liberation." The spiritual project as self-definition.

**Diagnostic signals:**
- Intellectual enthusiasm for Advaita as a philosophical system
- "I think I understand this now" as a satisfaction-statement
- "I need to understand this better before I can realize"
- The seeker-identity is strong and stable ("my practice", "my path",
  "my inquiry")
- Treating Advaita as a body of knowledge to master rather than
  a pointing toward what one already is
- Slight pride or confidence in the understanding

**The critical diagnostic:** The student can articulate the teaching
fluently. This is not a sign of de-identification — it may be vijñāna-adhyāsa
in its most sophisticated form. The question is not whether the student
can explain the teaching but whether the understander-identity is loosening.

**Correction:**
- "Who understands?" — directing attention to the understander rather
  than the understanding
- The intellect is an instrument, not the Self; instruments do not
  know themselves
- The Self is svaprakāśa — it does not need to understand itself
- The teaching is not a door to pass through but a mirror; once the
  face is seen, the mirror is set down
- Seeker inquiry: "What is the nature of the one who seeks?"

**Weakening indicators:**
- The student stops placing emphasis on understanding and starts
  inquiring into the understander
- "I don't know" is said without anxiety
- Questions shift from "how does this work?" to "what am I?"
- The seeker-identity becomes less fixed; the student can hold the
  inquiry lightly without it becoming a project

---

### 7.5 Sākṣi-adhyāsa — Witness Reification

**Description:** Having disidentified from body, emotions, and mind, the
student stabilizes in the witness-position and reifies it as a separate
standpoint. "I am the witness" becomes a new identity.

This appears after genuine progress. It is a subtle error because the
witness-pointing IS a valid and necessary prakriyā. The error is stopping
there — treating the witness as a destination rather than a pointer toward
Brahman.

**Diagnostic signals:**
- "I am the witness"; "I rest as the witness"; "I observe from a distance"
- A subtle sense of being a separate entity that is watching experience
- The witness is described as something achieved, maintained, or accessed
- Spiritual language that emphasizes the stability of the witness-position
  as an attainment
- A subtle sense of distance from experience that has a slight quality
  of detachment rather than non-separation

**The key distinction:** Non-identification with experience (correct,
this is the direction) vs. a subtle watcher that stands apart from experience
(sākṣi-adhyāsa). The difference is in whether the witness is felt as a
position being held or as the natural, effortless nature of awareness.

**Correction:**
- The witness cannot be witnessed — what is aware of the awareness?
- Sākṣi is a pointer, not a destination; having used the pointer, now
  investigate the pointer itself
- Witness-Brahman identity: the witness is not a thing that watches,
  but the non-dual nature of knowing itself
- "Who is the witness?" — not as a question to answer conceptually,
  but as a direction of attention

**Weakening indicators:**
- "I am the witness" language gives way to "awareness is" or "there is
  knowing" language
- The subtle sense of a separate watcher dissolves into awareness
  being the very texture of experience
- No longer maintaining a witness-position; instead, noticing that
  awareness is simply present without needing to be maintained

---

### 7.6 Viṣaya-adhyāsa on Mokṣa — Liberation as Object

**Description:** Treating liberation as a future attainment, an experience
to be had, or a state to be reached. The Self is conceptually identified as
Brahman but the seeking continues because the realization is not felt as
"now." This error can appear at any stage but is most prominent in
nididhyāsana.

**Diagnostic signals:**
- "When will I realize?"; "Why haven't I realized yet?"
- "I want to experience Brahman / non-dual awareness"
- "I haven't had the experience yet"
- Treating liberation as a project with a timeline
- Comparing one's state to descriptions of enlightenment and finding
  oneself lacking
- The seeker-project directed specifically at mokṣa as an object

**The structural error:** This is a superimposition of the viṣaya-viṣayin
(object-subject) structure onto mokṣa itself. Liberation is treated as
an object the subject will one day possess. But the Self is already free
(nitya-mukta). What is sought is already the seeker.

**Correction:**
- Nitya-mukta teaching: the Self is eternally free; there is no moment
  at which it becomes free
- Liberation is not a future experience — experience is precisely what
  the Self witnesses, not what it is
- The seeking is itself a form of not-finding: who seeks? From what
  does the seeker wish to be liberated?
- The one who expects a future realization has not yet understood that
  the Self is the knowing in which all experience, including future
  experience, appears

**Weakening indicators:**
- The future-orientation of seeking diminishes
- The student stops comparing their current state to descriptions of
  liberation
- "What am I right now?" replaces "when will I realize?"
- The seeker-project around mokṣa loosens

---

## 8. Prakriyā Map

The primary matrix: for each (stage × error) combination, the indicated
prakriyā and the corpus routing fields.

```yaml
prakriya_map:

  # DEHA-ADHYASA
  deha_adhyasa:
    adhikari_sravana:
      primary: drg-drsya-viveka       # seer-seen discrimination
      supporting:
        - adhyaropa-apavada           # superimpose/negate
        - analogy-based-pointing      # chariot, snake-rope
      corpus:
        prakriya: drig-drishya-viveka
        pedagogical_stage: sravana
        adhikara_level: sarva

    manana:
      primary: panca-kosa-viveka      # five-sheath analysis
      supporting:
        - avastha-traya               # three-state analysis
        - neti-neti
      corpus:
        prakriya: panca-kosa-viveka
        pedagogical_stage: manana
        adhikara_level: madhyama

    nididhyasana:
      primary: witness-stabilization
      supporting:
        - neti-neti                   # at somatic level
        - avastha-traya               # body absent in sleep
      corpus:
        prakriya: atman-as-witness-pointing
        pedagogical_stage: nididhyasana
        adhikara_level: uttama

  # MANAS-ADHYASA
  manas_adhyasa:
    sravana:
      primary: drg-drsya-viveka       # applied to mental contents
      supporting:
        - consciousness-self-evidence
        - dream-waking-analogy
      corpus:
        prakriya: drig-drishya-viveka
        pedagogical_stage: sravana
        adhikara_level: madhyama

    manana:
      primary: witness-identification
      supporting:
        - subject-object-analysis
        - svaprakasa-pointing          # self-luminosity
      corpus:
        prakriya: atman-as-witness-pointing
        pedagogical_stage: manana
        adhikara_level: madhyama

    nididhyasana:
      primary: neti-neti              # applied to mental states
      supporting:
        - attention-reversal
      corpus:
        prakriya: neti-neti-negation
        pedagogical_stage: nididhyasana
        adhikara_level: uttama

  # VIJNANA-ADHYASA
  vijnana_adhyasa:
    manana:
      primary: understander-inquiry   # who understands?
      supporting:
        - svaprakasa-pointing
        - seeker-inquiry
      corpus:
        prakriya: inquiry-opening
        pedagogical_stage: manana
        adhikara_level: uttama

    nididhyasana:
      primary: seeker-dissolution
      supporting:
        - mahavakya-contemplation
        - direct-pointing
      corpus:
        prakriya: atman-as-brahman
        pedagogical_stage: nididhyasana
        adhikara_level: uttama

  # SAKSI-ADHYASA
  saksi_adhyasa:
    nididhyasana:
      primary: witness-brahman-identity
      supporting:
        - beyond-known-unknown        # kena 1.4 style
        - apophatic-pointing
      corpus:
        prakriya: atman-as-witness-pointing
        pedagogical_stage: nididhyasana
        adhikara_level: uttama
      note: >
        Do not use witness-stabilization prakriyā here — it consolidates
        the error. Use witness-Brahman identity instead.

  # VISAYA-ADHYASA ON MOKSA
  visaya_adhyasa_moksa:
    any_stage:
      primary: nitya-mukta-pointing   # already free
      supporting:
        - seeker-dissolution
        - mahavakya-direct-pointing
      corpus:
        prakriya: mahavakya-direct-pointing
        pedagogical_stage: nididhyasana
        adhikara_level: uttama

  # STAGE 0: QUALIFICATION ROUTING
  # These are not prakriyās — they are orientation directives for pūrva-adhikāri.
  # The engine issues redirect_domain from this map and routes to these passages.
  qualification_routing:

    viveka_absent:
      goal: arouse discrimination between nitya and anitya
      approach: point at impermanence of worldly objects; do not argue — evoke
      corpus:
        passages:
          - Katha 1.1.23-1.1.29    # Naciketas rejects Yama's worldly offers
          - BG_2_14                 # transience of pleasure and pain
          - BG_2_16                 # the unreal has no being; the real never ceases
          - BG_2_20                 # the Self is not born and does not die
        pedagogical_stage: sravana
        adhikara_level: sarva
        ontological_scope: dual-register

    vairagya_absent:
      goal: orient toward dispassion; problematize instrumental seeking
      approach: karma-yoga as purification, not suppression; action without
                attachment loosens the grip of rāga — do not demand vairāgya,
                cultivate the conditions for it
      corpus:
        passages:
          - BG_2_47                 # action without attachment to fruit
          - BG_3_19                 # niṣkāma karma
          - BG_3_35                 # one's own dharma, though imperfect
          - VCM_1 to VCM_14         # Vivekacūḍāmaṇi opening: adhikāra described
        pedagogical_stage: sravana
        adhikara_level: sarva
        ontological_scope: dual-register

    sat_sampat_deficient:
      goal: identify the specific deficiency and orient toward its cultivation
      note: >
        Route to the most acutely absent quality first; do not enumerate all
        six at once. The student needs one clear direction, not a virtue list.
      sub_routing:
        sama_absent:
          corpus: [YS_1_32, YS_1_33]   # ekāgratā; cultivation of equanimity
        dama_absent:
          corpus: [BG_2_58, BG_2_68]   # withdrawal of senses; sthita-prajña
        titiksa_absent:
          corpus: [BG_2_14, BG_2_15]   # endurance of the pairs of opposites
        sraddhа_absent:
          corpus:
            - KATHA_1_1               # Naciketas as model of śraddhā in the teaching
            - MUNDAKA_1_2_12          # pramāṇa established; the student who goes to a teacher
        samadhana_absent:
          corpus: [YS_1_02, YS_2_29]  # definition of yoga; aṣṭāṅga as foundation
      pedagogical_stage: sravana
      adhikara_level: sarva
      ontological_scope: dual-register

    mumuksutva_absent:
      goal: arouse genuine longing through viveka and direct confrontation with
            impermanence; this is the most critical deficiency
      approach: >
        Do not argue for liberation or explain what it is. Use the Naciketas
        narrative: a student who had everything offered and asked for the Self
        anyway. Arouse saṃvega — the urgency that arises when impermanence
        is faced without escape. Let the student feel the question, not just
        think it.
      corpus:
        passages:
          - KATHA_1_1 to KATHA_1_29  # full Naciketas narrative
          - BG_2_11 to BG_2_13       # Kṛṣṇa's opening: you grieve for what is not
          - VCM_1 to VCM_14          # the stakes of adhikāra
        pedagogical_stage: sravana
        adhikara_level: sarva
        ontological_scope: dual-register

  # CONTRAINDICATIONS
  contraindicated:
    - error: saksi-adhyasa
      avoid: witness-stabilization    # consolidates rather than removes
    - error: vijnana-adhyasa
      avoid: mahavakya-analysis       # gives more content to the understander
    - error: visaya-adhyasa-moksa
      avoid: progressive-path-framing # reinforces future-orientation
```

---

## 9. Weakening Assessment Protocol

**The fundamental rule:** Verbal understanding is not a completion signal.
The test is behavioral and reactive, not declarative.

The LLM assesses weakening through observation of the conversation —
not through direct testing or quiz-style checking. The four indicators:

**1. Resistance absent:** A challenge that previously generated deflection,
counter-argument, or discomfort now lands without reactivity. The student
engages the pointing directly.

**2. Spontaneous application:** The student applies the corrective view
without being prompted. They use the teaching to navigate a situation
rather than waiting to receive the teaching.

**3. Question layer shifted:** The student's questions have moved to a
subtler level. The gross error is no longer the edge. This is the most
reliable indicator — the error that was primary is no longer generating
questions.

**4. Seeker loosening:** Where the student previously said "I understand"
with satisfaction (vijñāna-adhyāsa), they now hold the inquiry more lightly.
The understanding-project has less grip.

**The opening probe at session start** is the primary cross-session
assessment tool. The LLM introduces the prior session's error domain into
natural conversation (not as a test). If the error is still fully active,
the same patterns appear. If it has weakened, the student engages differently.
This is reported as recognition_markers in the signal payload.

**On resolution:** An error moves from `weakening` to `resolved` only when:
- It has not appeared in two consecutive sessions despite the opening probe
- The student's questions have consistently moved to a subtler layer
- No regression to this error appears under stress within sessions

Resolution is conservative. The state machine does not mark an error resolved
on insufficient evidence.

---

## 11. Ontology

The engine is constrained by a semantic ontology. It cannot generate
speculative doctrine or bypass pramāṇa structure. Every concept the engine
reasons over belongs to a tier; every assertion it makes carries an epistemic
status tag.

### 11.1 Concept Tiers

**Tier −1 — Qualification Prerequisites (Sādhana-Catuṣṭāya)**
- viveka (nitya-anitya-vastu-viveka)
- vairāgya (ihāmutra-phala-bhoga-virāga)
- ṣaṭ-sampat: śama, dama, uparama, titikṣā, śraddhā, samādhāna
- mumukṣutva

These are prerequisites to the pedagogical process, not part of it.
The engine operates at Tier −1 only while the student is in Stage 0.

**Tier 0 — Absolute Terms**
- brahman
- ātman
- turīya
- satya

**Tier 1 — Error Structure**
- adhyāsa
- avidyā
- kartṛtva
- bhoktṛtva
- dehātma-buddhi

**Tier 2 — Pedagogical Frameworks (Prakriyās)**
- avasthā-traya
- pañca-kośa
- dṛg-dṛśya-viveka
- kārya-kāraṇa analysis
- adhyāropa-apavāda
- lakṣaṇā-based methods

**Tier 3 — Soteriological Process**
- śravaṇa
- manana
- nididhyāsana
- jīvanmukti

### 11.2 Typed Relationships

Edges between concepts must be semantically explicit:

- reveals
- negates
- provisionally-asserts
- rescinds
- depends-on
- resolves
- misidentifies-as
- transcends

### 11.3 Epistemic Status Tags

Every assertion the engine makes must carry one of:

- śruti-primary
- bhāṣya-interpretive
- yukti-supportive
- provisional (adhyāropa)
- rescinded (apavāda)
- final (non-dual resolution)

This preserves pramāṇa integrity and prevents the engine from presenting
speculative interpretation as authoritative teaching.

---

## 12. Prakriyā Execution Engine

### 12.1 Stack-Based Architecture

- Only one prakriyā active at a time.
- Completion required before exit.
- No lateral framework mixing.
- Escalation allowed only upward in abstraction.

This prevents conceptual fragmentation — the error of the student who has
heard five prakriyās and settled none of them.

### 12.2 Prakriyā Module Structure

Each prakriyā must define:

1. **Push condition** — what error/stage combination activates this prakriyā
2. **Internal stages** — the sequence of moves within the prakriyā
3. **Micro-variation strategies** — how to rephrase without changing framework
4. **Loop detection patterns** — specific signals that indicate stagnation
5. **Escalation criteria** — conditions under which a higher abstraction is warranted
6. **Completion test** — what constitutes genuine completion (behavioral, not declarative)
7. **Rescission logic** — how the provisional scaffold is dissolved
8. **Exit state definition** — the epistemic state the student is in after stack pop

All prakriyā modules are specified in the companion document:
**`system/state_machine/AIM_prakriya_modules.md`**

Stage 0 orientation modes (saṃvega-arousal, viveka-arousal, karma-yoga-orientation)
and eleven prakriyā modules (B.1–B.11) are defined there. This document governs
the structural rules; the companion governs the content of each module.

### 12.3 Adhyāropa-Apavāda Staging

Staging is prakriyā-specific, not global. Each module encodes:

- Provisional assertions (adhyāropa phase)
- Built-in negation sequence (apavāda phase)
- Termination collapse (the scaffold is let go, not preserved)
- Explicit anti-reification safeguards

**Completion requires dissolution of the scaffold — not stabilization within
it.** A student who is comfortable in the witness-position has not completed
the prakriyā; they have reified it. The prakriyā completes when the pointing
is no longer needed.

### 12.4 Micro-Variation Logic

Within a single active prakriyā, the engine may:

- Rephrase distinctions
- Shift from logical to phenomenological framing
- Introduce metaphor
- Increase abstraction precision
- Apply śruti or yukti emphasis

It may NOT introduce a different framework unless escalation criteria are met.
Variation is within the current tool, not between tools.

### 12.5 Loop Detection

Loop detection monitors for:

- Semantic redundancy (student restates same position in different words)
- Oscillation between two positions without resolution
- Reassertion of provisional identity after negation
- Defensive resistance to negation (not ignorance-based resistance, which is expected)
- Conceptual stagnation across multiple exchanges

When threshold exceeded, the engine chooses:

- **A. Internal refinement** — a different micro-variation within the prakriyā
- **B. Escalation upward** — move to the next abstraction level if criteria are met

Escalation must never function as avoidance of a genuinely stuck student.

### 12.6 Escalation Criteria

Escalation permitted only when all of the following hold:

- The internal distinctions of the current level are grasped
- Scaffold reification persists at the current level
- Resistance is structural (the tool has been applied correctly and still doesn't resolve), not ignorance-based (the tool hasn't landed yet)
- The student's abstraction tolerance is sufficient for the next level

Escalation hierarchy (indicative, not exhaustive):

```
Level 1 — Differentiation-based pointing (gross seer-seen)
Level 2 — Subject-object abstraction (witness of mental contents)
Level 3 — Ontological causality (kārya-kāraṇa, no independent existence)
Level 4 — Meta adhyāropa-apavāda (the teaching itself is pointed at and released)
```

Movement is upward only within a session. The engine does not descend an
escalation level to re-explain what has already been grasped.

### 12.7 Stability Testing

When rapid assent or high abstraction is detected — the student agrees
quickly or speaks in advanced Advaitic language — the engine triggers a
stability test before proceeding:

- Reapply the discrimination in a new, concrete context
- Introduce a perturbation (a counter-scenario that should unsettle the error)
- Request reformulation in the student's own words
- Stress-test the provisional identity under a different modality

If stable → proceed.
If unstable → remain at current level.

A maximum test limit prevents over-refinement. The engine does not test
indefinitely; at some point it accepts the student's assimilation and moves.

### 12.8 Completion Criteria

A prakriyā completes only when:

1. The internal distinctions are clear (the student can articulate them)
2. The provisional stage is stabilized (not oscillating)
3. Rescission is accepted (the scaffold can be let go)
4. No reification remains (the student does not treat the pointer as the destination)
5. The student does not depend on the scaffold (they can engage without it)

The stack pops only after full collapse. Partial completion is not completion.

### 12.9 Post-Completion Phase

After stack pop, the engine enters **Contemplative Pause Mode**:

- No immediate prakriyā push.
- Allow cognitive integration — the understanding needs time to settle.
- Monitor for residual confusion or re-arising of the prior error.

Only after this pause does the engine assess whether a new prakriyā is
necessary. The pause is not a gap — it is part of the process.

---

## 13. Adhikāra Modeling

Adhikāra is inferred continuously from behavioral signals. It is never
declared by the student and never directly tested by the engine.

### 13.1 Adhikāra Vector

The engine maintains a persistent vector of adhikāra indicators, updated
after each significant exchange:

- `conceptual_clarity` — can the student track and articulate distinctions?
- `reification_index` — how readily does the student freeze a pointer into a position?
- `abstraction_tolerance` — can the student operate at higher ontological levels?
- `attachment_intensity` — how strongly do identity-stakes resist negation?
- `existential_stability` — can the student engage de-identification without distress?
- `resistance_pattern` — what form does resistance take (deflection, bypass, counter, silence)?

### 13.2 Behavioral Signals

The vector is updated through observation of:

- Logical consistency across exchanges
- Stability under negation (does the understanding hold when challenged?)
- Reaction to rescission (can the scaffold be let go?)
- Ability to articulate the teaching without jargon dependency
- Cross-context coherence (does the understanding transfer to new situations?)

**Vocabulary sophistication is not treated as evidence of assimilation.**
A student who speaks fluent Advaitic terminology while exhibiting every
marker of vijñāna-adhyāsa is assessed by behavior, not language.

### 13.3 Stage 0 Behavior

When the student record indicates `stage: purva-adhikari`:

- Prakriyā stack execution is **suspended**.
- The adhikāra vector is read against `qualification_status` (Section 4),
  not the error taxonomy (Section 7).
- The engine issues `redirect` directives, not prakriyā push events.
- Loop detection and escalation logic are inactive; the engine monitors
  qualification development instead.
- The stability test module is inactive; the engine does not test assimilation
  of a teaching that has not yet been delivered.
- Prakriyā execution resumes only when `longitudinal_state.stage` advances
  to `adhikari`.

---

## 14. System Integrity Constraints

The engine must never:

- Generate speculative metaphysics not grounded in śruti-pramāṇa
- Collapse provisional stages prematurely (apavāda before adhyāropa is complete)
- Allow partial assimilation stacking (pushing a new prakriyā before the prior completes)
- Bypass apavāda (leaving a scaffold standing)
- Absolutize any intermediate identity (witness, understander, seeker)
- Treat verbal understanding as completion
- Advance longitudinal stage on insufficient evidence

All teaching remains:

- Pramāṇa-governed — constrained by śruti, bhāṣya, yukti in that order
- Śruti-constrained — the engine does not generate novel doctrine
- Error-removal oriented — the goal is avidyā-nivṛtti, not knowledge-accumulation

---

## 10. Source Files Superseded

The following files are superseded by this document and should be treated
as archived:

- `system/state_machine/AIM_student_state_machine_v2.md` — pedagogical
  map subsumed into Section 8 (Prakriyā Map)
- `system/state_machine/initial_state_model_v2.md` — ontological state
  model subsumed into Section 6 (Longitudinal State Model)
- `system/state_machine/cognitive_error_machine.md` — error taxonomy and
  symptom lists subsumed into Section 7 (Error Taxonomy)
- `archive/student_state_machine.md` — earlier version, superseded
- `system/architecture/core/agent_spec_addendum.md` — ontology, prakriyā
  execution engine, and adhikāra modeling subsumed into Sections 11–14;
  architectural framing updated from two-layer to three-layer; Stage 0
  behavior added to adhikāra modeling

The pedagogical content of these files has been preserved; the naming
inconsistencies, YAML formatting errors, and architectural gaps have been
resolved. All source files carry a deprecation notice at the top.
