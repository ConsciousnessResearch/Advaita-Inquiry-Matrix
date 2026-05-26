> **DEPRECATED** — Superseded by `system/state_machine/AIM_state_machine_v3.md` (2026-05-01).
> This file is retained for historical reference only. Do not use for implementation.

# AIM Student State Machine v1.0

## Purpose

The **Student State Machine** models the developmental position of a
student in the Advaita learning process. It allows AIM to determine:

-   which **prakriyā** should be used
-   which **scripture clusters** should be activated
-   which **dialogue tone** should be adopted

This state model is inspired by the traditional Advaita progression:

adhikāri → śravaṇa → manana → nididhyāsana → jñāna-niṣṭhā

The system does not assume linear progress. Students may move **forward,
stall, regress, or oscillate** between states.

------------------------------------------------------------------------

# Core Student States

\`\`\`yaml student_states student_states:

adhikari_preparation: description: \> Student is curious but not yet
stable in inquiry. Identity strongly tied to body, mind, and life
narrative. dominant_errors: - body_identification - ritual_dependence
recommended_prakriya: - adhyaropa_apavada - drg_drsya_viveka
dialogue_mode: contemplative

sravana_stage: description: \> Student is actively listening to the
teaching and learning core concepts. dominant_errors: -
philosophical_dualism - experience_brahman recommended_prakriya: -
mahavakya_analysis - phenomenological_analysis dialogue_mode:
contemplative

manana_stage: description: \> Student is intellectually engaging the
teaching and raising objections. dominant_errors: -
epistemic_regress_confusion - dualistic_reasoning
recommended_prakriya: - ontological_debate - logical_refutation
dialogue_mode: ontological_combat

nididhyasana_stage: description: \> Student has recognized the teaching
conceptually and is integrating it. dominant_errors: -
post_insight_instability - subtle_identification recommended_prakriya: -
neti_neti - witness_stabilization dialogue_mode: stabilization

jnana_nistha: description: \> Knowledge of the Self is stable. Dialogue
shifts from correction to refinement and celebration. dominant_errors: -
none_primary recommended_prakriya: - contemplative_affirmation -
poetic_expression dialogue_mode: poetic


    ---
    
    # Transition Signals
    
    Transitions occur when AIM detects linguistic or conceptual markers.
    
    ```yaml state_transitions
    state_transitions:
    
      curiosity_trigger:
        from: adhikari_preparation
        to: sravana_stage
        signal: genuine_inquiry
    
      conceptual_understanding:
        from: sravana_stage
        to: manana_stage
        signal: philosophical_questions
    
      recognition_event:
        from: manana_stage
        to: nididhyasana_stage
        signal: insight_language
    
      stabilization_event:
        from: nididhyasana_stage
        to: jnana_nistha
        signal: stable_nondual_language
    
      drift_event:
        from: nididhyasana_stage
        to: manana_stage
        signal: return_of_identification

------------------------------------------------------------------------

# Recognition Signals

AIM detects recognition through characteristic expressions.

Examples:

-   "Awareness seems to be always present."
-   "The witness is unaffected."
-   "Experience changes but the knower does not."

These trigger **recognition_signal: true** in the engine.

------------------------------------------------------------------------

# Integration With Other AIM Components

The Student State Machine interacts with the rest of the system as
follows:

    student_input  
    → objection_ontology  
    → error_pattern_detection  
    → student_state_update  
    → prakriya_selection_engine  
    → scripture_cluster_routing  
    → dialogue_generation

------------------------------------------------------------------------

# Pedagogical Principle

The student state determines **how strongly AIM intervenes**.

  State          AIM Style
-------------- ------------------------
  adhikāri       gentle orientation
  śravaṇa        explanation
  manana         debate
  nididhyāsana   contemplative guidance
  jñāna-niṣṭhā   poetic affirmation

------------------------------------------------------------------------

# Architectural Role

The Student State Machine provides the **temporal dimension** of the AIM
system.

Without it, AIM would respond only to individual statements.

With it, AIM can track:

-   intellectual maturation
-   recognition events
-   regressions
-   stabilization of insight

This allows the system to approximate the traditional **guru--śiṣya
progression** in an adaptive digital environment.

------------------------------------------------------------------------

# Prakriyā Map

The following map defines which pedagogical methods are appropriate for
each student state detected by AIM.

```yaml prakriya_map 
prakriya_map:

adhikari_preparation:

    primary_prakriya:
      - adhyaropa_apavada
      - drg_drsya_viveka
      - atma_anatma_viveka
    
    supporting_prakriya:
      - karma_limit_analysis
      - impermanence_reflection
      - existential_inquiry
    
    pedagogical_goal: >
      Establish the intuition that the self is distinct from objects,
      experiences, and changing conditions.

sravana_stage:

    primary_prakriya:
      - mahavakya_analysis
      - phenomenological_analysis
      - ontological_pointing
    
    supporting_prakriya:
      - scripture_authority_invocation
      - consciousness_self_evidence
      - witness_identification
    
    pedagogical_goal: >
      Introduce the central teaching that the Self is nondual consciousness
      and that it is already present as the knower of all experience.

manana_stage:

    primary_prakriya:
      - logical_refutation
      - epistemic_collapse
      - ontological_debate
    
    supporting_prakriya:
      - dualism_dissolution
      - subject_object_analysis
      - knower_known_inquiry
    
    pedagogical_goal: >
      Remove intellectual objections and collapse philosophical dualities
      that prevent recognition of the Self.

nididhyasana_stage:

    primary_prakriya:
      - neti_neti
      - witness_stabilization
      - nondual_contemplation
    
    supporting_prakriya:
      - identification_release
      - attention_reversal
      - experiential_silence
    
    pedagogical_goal: >
      Stabilize recognition by dissolving subtle identification with
      mind, experience, and personal narrative.

jnana_nistha:

    primary_prakriya:
      - contemplative_affirmation
      - poetic_expression
      - paradoxical_teaching
    
    supporting_prakriya:
      - spontaneous_pointing
      - playful_dialogue
      - silence_invocation
    
    pedagogical_goal: >
      Reinforce stable knowledge through subtle reminders, poetic
      expression, and non-conceptual pointing.
