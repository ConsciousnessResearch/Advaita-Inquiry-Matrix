# Advaita Pedagogical Loop Algorithm

This document formalizes the **recursive teaching loop** observed across
the Advaita Vedānta corpus. Rather than operating as a linear
curriculum, Advaita instruction proceeds through repeated cycles of
diagnosis, clarification, recognition, and deeper refinement.

The pattern appears in multiple texts including:

-   Kaṭha Upaniṣad
-   Chāndogya Upaniṣad
-   Taittirīya Upaniṣad
-   Māṇḍūkya Upaniṣad
-   Upadeśa-sāhasrī

The repetition of this structure suggests the presence of a **canonical
teaching algorithm** used in the guru--śiṣya tradition.

------------------------------------------------------------------------

# Core Loop Structure

The pedagogical cycle can be expressed as:

    student assertion
        ↓
    diagnose cognitive error
        ↓
    select appropriate prakriyā
        ↓
    apply teaching passage
        ↓
    recognition glimpse
        ↓
    emergence of subtler doubt
        ↓
    loop restarts with deeper clarification

Each iteration removes a **subtler layer of misidentification**.

------------------------------------------------------------------------

# Algorithmic Representation

    while ignorance persists:

        detect_student_claim()

        error_type = classify_error()

        stage = determine_teaching_stage()

        prakriya = select_prakriya(error_type, stage)

        passage = retrieve_scripture(prakriya)

        present_teaching(passage)

        if recognition_stabilized:
            exit loop
        else:
            continue with deeper clarification

------------------------------------------------------------------------

# Loop Manifestations in the Upaniṣads

## Kaṭha Upaniṣad

Loop 1

-   Kaṭha 1.1 --- existential disturbance (death confrontation)
-   Kaṭha 1.2 --- ethical discrimination (śreyas vs preyas)
-   Kaṭha 1.3 --- instrument analysis (chariot metaphor)

Loop 2

-   Kaṭha 2.1 --- inward turning of perception
-   Kaṭha 2.2 --- ontological clarification of Self
-   Kaṭha 2.3 --- transcendence of objectification

------------------------------------------------------------------------

## Chāndogya Upaniṣad 6

Each analogy introduces a new cycle:

    analogy
    → doubt
    → clarification
    → tat tvam asi

Analogical cycles include:

-   clay and pots
-   gold and ornaments
-   salt dissolved in water
-   banyan seed

------------------------------------------------------------------------

## Taittirīya Upaniṣad

The pañca-kośa method forms a recursive identity-negation loop:

    annamaya
    → prāṇamaya
    → manomaya
    → vijñānamaya
    → ānandamaya

At each stage:

    identify layer
    → negate identity
    → move inward

------------------------------------------------------------------------

## Māṇḍūkya Upaniṣad

The analysis of states forms another recursive refinement:

    waking
    → dream
    → deep sleep
    → turīya

Subsequent reasoning re-examines the same states from deeper
perspectives.

------------------------------------------------------------------------

# Relationship to AIM Architecture

The Advaita Pedagogical Loop connects multiple AIM subsystems.

    student_state_machine
            ↓
    error classification
            ↓
    prakriyā_selection_engine
            ↓
    corpus passage retrieval
            ↓
    dialogue protocol
            ↓
    updated student state
            ↓
    loop continues

This design mirrors the **traditional Advaita teaching dynamic**, where
each clarification elicits a subtler misunderstanding until the root
misidentification collapses.

------------------------------------------------------------------------

# Significance

The recursive loop suggests that the Advaita corpus encodes not only
doctrine, but also a **method for dissolving ignorance through iterative
inquiry**.

Modeling this loop allows AIM to approximate the decision process used
by traditional Advaita teachers.

------------------------------------------------------------------------

# Recommended Location

Place this file in:

AIM/pedagogy/advaita_framework/advaita_pedagogical_loop_algorithm.md
