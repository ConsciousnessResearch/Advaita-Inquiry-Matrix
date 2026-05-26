# Kaṭha Upaniṣad --- Pedagogical Teaching Graph

This file encodes the pedagogical progression of the **Kaṭha Upaniṣad**
as a sequence of epistemic states. The structure is designed to support
reasoning within the AIM (Advaita Instruction Model) system.

------------------------------------------------------------------------

## Overview

Existential Shock\
↓\
Ethical Discrimination\
↓\
Transmission Recognition\
↓\
Instrument Disidentification\
↓\
Witness Recognition\
↓\
Cosmic Identity Expansion\
↓\
Self‑Luminosity Recognition\
↓\
Non‑Objectifiability\
↓\
Stillness / Yoga Stabilization\
↓\
Desire Collapse\
↓\
Liberation

------------------------------------------------------------------------

## Pedagogical State Graph

``` yaml
katha_teaching_graph:

  existential_shock:
    text: 1.1
    function: destabilize_naive_worldview
    description: >
      Nachiketas confronts death and the inadequacy of ritual and wealth.
    next: ethical_discrimination

  ethical_discrimination:
    text: 1.2.1–2
    function: value_axis_sorting
    concept: śreyas_vs_preyas
    description: >
      Student learns to distinguish ultimate good from immediate pleasure.
    next: transmission_recognition

  transmission_recognition:
    text: 1.2.6–8
    function: teacher_dependency_established
    description: >
      Knowledge of the Self requires qualified instruction and humility.
    next: instrument_disidentification

  instrument_disidentification:
    text: 1.3
    function: subject_instrument_separation
    teaching_device: chariot_metaphor
    description: >
      Body, senses, mind, and intellect are recognized as instruments rather than the Self.
    next: witness_recognition

  witness_recognition:
    text: 2.1.3–4
    function: recognize_witness_consciousness
    description: >
      The Self is the knower of all experiences.
    next: cosmic_identity

  cosmic_identity:
    text: 2.1
    function: expand_identity_scope
    marker: etad_vai_tat
    description: >
      The witnessing Self is recognized as the universal ground of experience.
    next: self_luminosity

  self_luminosity:
    text: 2.2.15
    function: recognize_self_luminosity
    description: >
      Consciousness reveals all phenomena and is not illuminated by anything else.
    next: non_objectifiability

  non_objectifiability:
    text: 2.3.9
    function: collapse_object_seeking
    description: >
      The Self cannot be perceived as an object.
    next: stillness

  stillness:
    text: 2.3.10–11
    function: stabilize_attention
    description: >
      Yoga defined as the stilling of senses, mind, and intellect.
    next: desire_collapse

  desire_collapse:
    text: 2.3.14
    function: vasana_dissolution
    description: >
      When desires fall away, the mortal becomes immortal.
    next: liberation

  liberation:
    text: 2.3.15
    function: adhyasa_terminated
    description: >
      The knots of the heart are cut and Brahman is realized.
```
