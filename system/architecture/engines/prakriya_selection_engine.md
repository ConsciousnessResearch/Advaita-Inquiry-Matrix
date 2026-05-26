# AIM Prakriyā Selection Engine

## Purpose

The **Prakriyā Selection Engine** connects three parts of the AIM
system:

1.  Student stage (pedagogical progression)
2.  Cognitive error state (type of misunderstanding)
3.  Appropriate Advaita teaching method (*prakriyā*)

This engine allows AIM to dynamically choose **how to teach**, rather
than simply providing explanations.

------------------------------------------------------------------------

# Conceptual Pipeline

student_input\
↓\
error_pattern_detection\
↓\
cognitive_error_state\
↓\
student_stage\
↓\
prakriyā_selection\
↓\
scripture_cluster_activation\
↓\
dialogue_generation

------------------------------------------------------------------------

# Core Engine Logic

``` yaml
prakriya_selection_engine:

  body_identification:
    recommended_prakriya:
      - drg_drshya_viveka
      - kosha_analysis
    scripture_clusters:
      - taittiriya_kosha_section
      - drg_drshya_viveka_text

  instrument_confusion:
    recommended_prakriya:
      - chariot_metaphor
      - sense_analysis
    scripture_clusters:
      - katha_1_3

  witness_confusion:
    recommended_prakriya:
      - avastha_traya
      - witness_inquiry
    scripture_clusters:
      - mandukya_upanishad
      - katha_2_1

  subject_object_duality:
    recommended_prakriya:
      - mahavakya_analysis
      - etad_vai_tat_recognition
    scripture_clusters:
      - chandogya_6
      - brihadaranyaka_identity_passages

  brahman_objectification:
    recommended_prakriya:
      - neti_neti
      - non_objectifiability_teaching
    scripture_clusters:
      - brihadaranyaka_netineti
      - katha_2_3

  residual_vasana:
    recommended_prakriya:
      - nididhyasana_guidance
      - contemplative_stabilization
    scripture_clusters:
      - upanishadic_meditative_sections
```

------------------------------------------------------------------------

# Interaction With Student Stage Machine

The **stage machine controls dialogue tone**, while the prakriyā engine
controls **teaching method**.

Example:

``` yaml
stage: manana
error: witness_confusion
prakriya: avastha_traya
dialogue_mode: ontological_combat
```

Example response pattern:

1.  Challenge assumption
2.  Introduce waking--dream--deep sleep analysis
3.  Show that the witness is not a mental object

------------------------------------------------------------------------

# Example Decision Table

  Error                   Prakriyā            Scripture
  ----------------------- ------------------- ---------------
  body = self             dṛg--dṛśya viveka   Taittirīya
  mind = witness          avasthā‑traya       Māṇḍūkya
  brahman = experience    mahāvākya           Chāndogya
  brahman = object        neti‑neti           Bṛhadāraṇyaka
  residual conditioning   nididhyāsana        multiple

------------------------------------------------------------------------

# Architectural Role

The Prakriyā Selection Engine acts as the **bridge between diagnosis and
teaching**.

Without it, AIM can only identify confusion.

With it, AIM can perform **targeted Advaita pedagogy**, approximating
the traditional guru--śiṣya teaching dynamic.

------------------------------------------------------------------------

# Recommended File Location

    AIM/teaching_engine/prakriya_selection_engine.md

This keeps the engine distinct from:

-   state machines
-   text teaching maps
-   raw scriptural corpus
