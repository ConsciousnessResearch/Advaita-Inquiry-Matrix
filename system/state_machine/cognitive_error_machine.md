> **DEPRECATED** — Superseded by `system/state_machine/AIM_state_machine_v3.md` (2026-05-01).
> This file is retained for historical reference only. Do not use for implementation.

# Advaita Student State Machine (ASSM)

This document defines a minimal pedagogical state machine modeling the
cognitive transformation of a student in Advaita Vedānta.\
The states represent **epistemic conditions of the student**, not
textual structure.\
A teacher (human or AIM system) diagnoses the student's state and
selects appropriate teaching moves.

------------------------------------------------------------------------

## State Diagram

Naive Realism\
↓\
Ethical Discrimination\
↓\
Epistemic Humility\
↓\
Instrument Disidentification\
↓\
Witness Recognition\
↓\
Nondual Integration\
↓\
Stabilization\
↓\
Liberation

------------------------------------------------------------------------

## State Machine Definition

``` yaml
advaita_student_state_machine:

  naive_realism:
    description: >
      Student assumes body-mind identity and treats the world as unquestioned reality.
    symptoms:
      - identity_with_body
      - reliance_on_external_success
      - unexamined_assumptions
    pedagogical_moves:
      - existential_destabilization
      - mortality_confrontation
      - karma_inadequacy
    transitions:
      -> ethical_discrimination

  ethical_discrimination:
    description: >
      Student recognizes the difference between śreyas (ultimate good) and preyas (immediate pleasure).
    symptoms:
      - dissatisfaction_with_worldly_pursuits
      - moral_reflection
      - openness_to_inquiry
    pedagogical_moves:
      - śreyas_preyas_teaching
      - impermanence_analysis
      - value_reorientation
    transitions:
      -> epistemic_humility

  epistemic_humility:
    description: >
      Student understands the limits of personal reasoning and recognizes the need for qualified instruction.
    symptoms:
      - recognition_of_intellectual_limits
      - willingness_to_listen
      - trust_in_teaching_tradition
    pedagogical_moves:
      - teacher_necessity
      - transmission_structure
      - sravana_preparation
    transitions:
      -> instrument_disidentification

  instrument_disidentification:
    description: >
      Student begins distinguishing the Self from body, senses, mind, and intellect.
    symptoms:
      - observing_thoughts
      - reduced_identification_with_mind
      - beginning_of_self_inquiry
    pedagogical_moves:
      - chariot_metaphor
      - drg_drshya_viveka
      - kosha_analysis
    transitions:
      -> witness_recognition

  witness_recognition:
    description: >
      Student recognizes the witnessing consciousness behind all experience.
    symptoms:
      - awareness_of_witness
      - contemplative_interest
      - decreased psychological reactivity
    pedagogical_moves:
      - waking_dream_sleep_analysis
      - consciousness_as_knower
      - experiential_inquiry
    transitions:
      -> nondual_integration

  nondual_integration:
    description: >
      Student understands that the witnessing consciousness is identical with Brahman.
    symptoms:
      - dissolution_of_subject_object_boundary
      - recognition_of_self_luminosity
      - decreasing_fear_of_death
    pedagogical_moves:
      - mahavakya_teaching
      - universalization_of_self
      - non_objectifiability_clarification
    transitions:
      -> stabilization

  stabilization:
    description: >
      Knowledge stabilizes; residual conditioning weakens.
    symptoms:
      - reduced_reactivity
      - stable_awareness
      - minimal existential confusion
    pedagogical_moves:
      - nididhyasana
      - doubt_resolution
      - life_integration
    transitions:
      -> liberation

  liberation:
    description: >
      Adhyāsa collapses. The student recognizes ātman = brahman.
    characteristics:
      - heart_knot_cut
      - freedom_from_rebirth_compulsion
      - freedom_while_living
```

------------------------------------------------------------------------

## Mapping to Kaṭha Upaniṣad

  Student State                  Kaṭha Section
  ------------------------------ ---------------
  Naive Realism                  1.1
  Ethical Discrimination         1.2.1--2
  Epistemic Humility             1.2.6--8
  Instrument Disidentification   1.3
  Witness Recognition            2.1
  Nondual Integration            2.2
  Stabilization                  2.3.10--14
  Liberation                     2.3.15

------------------------------------------------------------------------

## Recommended File Location

Place this file in the AIM project structure:

    AIM/state_machine/advaita_student_state_machine.md

This keeps the **student cognition model** separate from:

-   corpus texts
-   text teaching maps
-   pedagogy libraries
