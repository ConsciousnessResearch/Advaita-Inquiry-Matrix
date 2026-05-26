# AIM Corpus Ontology Schema (v1.2)

This schema defines the structural and pedagogical contract for all corpus files in the
AIM system. It applies uniformly across all text types: Upaniṣads, prakaraṇas, and smṛti.

Core principles encoded:

- Every teaching unit must function as removal of ignorance (adhyāsa)
- No unit is merely ethical — ethical instruction resolves ontologically
- Devotional units are not ontologically inferior
- Category distinctions must never be absolutized
- Identity statements are linguistic gestures toward the unsayable
- Karma is never ontologically ultimate

---

# I. Text-Level Metadata (Required at Top of Every File)

Text-level metadata is defined in a fenced YAML block at the top of each `.md` file:

~~~yaml
text_role:
macro_prakriyā:
interaction_mode:
epistemic_model:
ontology_model:
doubt_resolution:
karma_status:
immortality_model:
macro_arc:
~~~

---

## text_role

The primary pedagogical function of the text as a whole.

Allowed values:

- `participatory-self-revelation` — text enacts the teaching by being read
- `progressive-unveiling` — teaching unfolds through sequential exposition
- `ontological-destabilization` — dismantles false identity systematically
- `relational-consummation` — resolves inquiry through devotional recognition

---

## macro_prakriyā

The global movement of the text. Short descriptive phrase.

Examples:

- `progressive-deobjectification`
- `paradox-to-recognition`
- `discrimination-to-identity`
- `sṛṣṭi-to-pratyāhāra`

---

## interaction_mode

Defines the student–text relationship.

Allowed values:

- `participatory-revelation`
- `destabilizing-dialogue`
- `guided-discrimination`
- `contemplative-invocation`

---

## epistemic_model

How knowledge functions in this text.

Allowed values:

- `recognition-not-acquisition`
- `scope-clarification`
- `deconstruction-of-categories`
- `linguistic-indication`

---

## ontology_model

The brahman–world relationship as framed by this text.

Allowed values:

- `non-diminishing-fullness`
- `apparent-superimposition`
- `relational-expression`
- `category-transcendent`

---

## doubt_resolution

How the text handles student doubt.

Allowed values:

- `argumentative-resolution`
- `dialectical-resolution`
- `participatory-dissolution`
- `apophatic-collapse`

---

## karma_status

How karma is framed in this text.

Allowed values:

- `binding-mechanism`
- `provisional-discipline`
- `relational-field`
- `expressive-of-fullness`
- `pragmatically-operative-nonbinding`

---

## immortality_model

How the text handles the question of death and continuity.

Allowed values:

- `post-mortem-continuity`
- `rebirth-cessation`
- `unborn-recognition`
- `rasa-of-fullness`
- `dual-register`

---

## macro_arc

A short arrow chain summarizing the text's movement.

Example:
`fullness → pervasion → non-binding action → category transcendence → linguistic exhaustion`

---

# II. Unit-Level Schema

Each teaching unit must include all mandatory fields. Optional fields are included
where applicable.

## Mandatory fields

~~~yaml
id:               # unique identifier (e.g. KATHA_1_1_1, ATMABODHA_12)
sanskrit:         # Sanskrit text; empty string "" for prose-only units
transliteration:  # IAST transliteration; empty string "" for prose-only units
translation:      # English translation or rendering
status:           # see Status Values below
prakriyā:         # teaching method applied in this unit
pedagogical_role: # function of this unit in the teaching arc
adhikāra_level:   # student qualification tier
cognitive_mode:   # how knowledge is accessed in this unit
pedagogical_stage: # stage in the śravaṇa–manana–nididhyāsana arc
ontological_scope: # ontological register of this unit
~~~

## Optional fields

~~~yaml
dependencies:     # list of unit IDs that are prerequisites
concepts:         # list of concept IDs linked to the concept graph
relational_mode:  # Advaita–Bhakti dynamic; include where Bhakti is relevant
note:             # brief pedagogical annotation; not displayed to student
~~~

---

## status

~~~yaml
VERIFIED          # reviewed and confirmed correct
UNCERTAIN         # content present but metadata confidence is low
REVIEW_REQUIRED   # flagged for human review before use
FAILED            # parsing or ingestion error; do not use
~~~

---

## prakriyā

The specific teaching method applied in this unit. Values from the canonical
prakriyā library (see `pedagogy/advaita_framework/prakriya_library.md`).

Core values:

- `identity` — direct mahāvākya-style identity assertion
- `negation` — neti-neti removal of superimposition
- `adhyāropa-apavāda` — superimposition then retraction
- `avasthā-traya` — three-state analysis (waking/dream/deep sleep)
- `dṛg-dṛśya-viveka` — seer–seen discrimination
- `sṛṣṭi-prakriyā` — creation sequence as teaching device
- `integration` — synthesis of prior moves
- `distinction` — viveka between real and apparent
- `paradox` — contradiction pointing beyond logic
- `invocation` — devotional gesture with ontological content
- `inquiry` — directed self-investigation

---

## pedagogical_role

The function this unit serves in the teaching arc. Examples:

- `establish-subject` — introduces the primary topic
- `compressed-totality` — states the conclusion at the outset
- `diagnosis` — identifies the student's error
- `ontological-grounding` — anchors the teaching in brahman
- `negation-of-false-self` — removes a specific superimposition
- `perceptual-reframing` — shifts the student's frame of reference
- `existential-warning` — flags the consequences of continued error
- `participatory-recognition` — invites direct recognition
- `integration` — synthesizes prior moves
- `culmination` — brings the teaching arc to completion

---

## adhikāra_level

Student qualification tier for this unit.

Allowed values:

- `sarva` — accessible to all levels
- `madhyama` — intermediate; requires prior conceptual grounding
- `uttama` — advanced; presupposes śravaṇa and manana stages

---

## cognitive_mode

How knowledge is accessed in this unit.

Allowed values:

- `logical-paradox` — knowledge arises through contradiction
- `analytic-contemplative` — discursive reasoning toward contemplation
- `metaphysical-contemplative` — direct metaphysical reflection
- `participatory` — knowing through enactment
- `apophatic` — knowing through negation
- `dialogical` — knowledge emerges through question and answer

---

## pedagogical_stage

Position in the śravaṇa–manana–nididhyāsana arc.

Allowed values:

- `śravaṇa` — initial hearing; establishing the teaching
- `manana` — reflection; working through objections and doubt
- `nididhyāsana` — deep contemplation; stabilizing recognition
- `integration` — synthesis across stages
- `culmination` — resolution of the inquiry

---

## ontological_scope

The ontological register in which this unit operates.

Allowed values:

- `pāramārthika` — absolute level; brahman as the only reality
- `vyāvahārika` — conventional level; empirical world taken as real
- `dual-register` — unit operates simultaneously at both levels
- `scope-clarification` — unit defines or corrects the operative level

---

## relational_mode (optional)

The Advaita–Bhakti dynamic in this unit. Include for texts where devotional
content is structurally present (Gītā, Īśā, devotional sections of Upaniṣads).

Allowed values:

- `advaita-explicit` — non-dual framing predominates
- `bhakti-explicit` — devotional framing predominates
- `performative-transition` — moves between registers
- `non-differentiable` — the two are indistinguishable in this unit

---

# III. Structural Types

Texts are typed at the file level. All must conform to the unit-level schema above.

- `revelatory` — e.g., Īśā: compressed, participatory, self-revealing
- `dialogical` — e.g., Kaṭha, Chāndogya: student–teacher exchange
- `compressed` — e.g., Māṇḍūkya: maximum density, minimal verse count
- `expansive-metaphysical` — e.g., Taittirīya: systematic layered exposition
- `discriminative` — e.g., Bṛhadāraṇyaka: extended seer–seen analysis
- `instructional-layered` — e.g., Upadeśa-sāhasrī: prose and verse interleaved
- `synthetic-smṛti` — e.g., Gītā: integrates action, devotion, and knowledge

---

# IV. Corpus-Wide Design Axioms

1. No unit is merely ethical — ethical instruction must resolve ontologically.
2. Devotional units are not ontologically inferior.
3. Category distinctions must never be absolutized within a unit.
4. Identity statements are linguistic gestures toward the unsayable.
5. Units operating in dual-register default to that designation unless
   clearly operating at one level only.
6. Karma is never ontologically ultimate, regardless of vyāvahārika framing.
7. `status: VERIFIED` requires all mandatory fields to be populated.

---

# Version

AIM Corpus Ontology Schema v1.2
Supersedes v1.1 (filename) / v1.0 (internal label).

Changes from v1.1:
- Unit-level structure standardized to flat (no nested `metadata` dict)
- `adhikāra_level`, `cognitive_mode`, `pedagogical_stage` promoted to mandatory
- `ontological_scope` promoted to mandatory (was Māṇḍūkya-only)
- `relational_mode` demoted to optional
- `tags` retired from unit schema (governed by tag taxonomy schema)
- Text-level `advaita_bhakti_dynamic` field retired (redundant with `relational_mode`)
- `structural_type` vocabulary formalized
- `status: VERIFIED` now requires all mandatory fields populated
