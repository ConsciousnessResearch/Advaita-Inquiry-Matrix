# AIM Advaita Pedagogy Specification

*A State-Machine-Oriented Teaching Model Based on the Upaniṣads and
Śaṅkara's Commentaries*

------------------------------------------------------------------------

## 1. Purpose

This document specifies the pedagogical structure underlying Advaita
Vedānta teaching as found in the Upaniṣads and traditional commentaries,
particularly those of Śaṅkarācārya.

The goal is to describe the teaching process in a form suitable for
implementation in a **state-machine-based inquiry system** such as the
Advaita Inquiry Matrix (AIM).

The specification extracts recurrent **prakriyās (teaching procedures)**
and **student-state transitions** evident in classical Advaitic
instruction.

Advaita teaching is not merely philosophical explanation but a **guided
epistemic transformation** that removes ignorance (*avidyā*) regarding
the nature of the Self (*ātman*).

------------------------------------------------------------------------

# 2. Core Assumption: The Human Problem

Advaita begins from the doctrine of **adhyāsa (superimposition)**.

Śaṅkara states in the introduction to the *Brahma‑sūtra bhāṣya*:

> "The superimposition of the Self and the not-Self is beginningless."

This produces the default human condition:

-   identification with body
-   identification with mind
-   identification with doership
-   perception of separation

The pedagogical task is **removal of this error through knowledge**.

------------------------------------------------------------------------

# 3. Pedagogical Principle

The Upaniṣads consistently employ **dialogical inquiry** between teacher
and student.

Example: *Kaṭha Upaniṣad*

> "This doubt concerning the person after death---some say he exists,
> others say he does not---teach me the truth."

The teacher does not merely answer questions but **guides the student
through structured inquiry**.

Thus Advaita pedagogy functions as a **progressive cognitive
realignment**.

------------------------------------------------------------------------

# 4. State Machine Overview

The Advaita teaching process can be represented as the following
conceptual state machine.

INITIAL_STATE: Ignorance (Avidyā)

1.  Existential Inquiry
2.  Qualification (Adhikāritva)
3.  Dialectical Analysis
4.  Cognitive Disruption
5.  Self‑Knowledge Recognition
6.  Stabilization of Knowledge

FINAL_STATE: Knowledge Established (Jñāna‑niṣṭhā)

------------------------------------------------------------------------

# 5. State Descriptions

## 5.1 Ignorance (Avidyā)

Default condition of identification with body and mind.

Symptoms:

-   suffering
-   fear of death
-   search for fulfillment

Scriptural reference:

Īśa Upaniṣad:

> "Into blinding darkness enter those who are devoted to ignorance."

------------------------------------------------------------------------

## 5.2 Existential Inquiry

The teaching process begins when a student develops genuine inquiry.

Example: Nachiketas in the *Kaṭha Upaniṣad*.

> "This doubt regarding the person after death---teach me."

Inquiry represents the **trigger event** for the teaching system.

------------------------------------------------------------------------

## 5.3 Qualification (Adhikāritva)

The student must demonstrate readiness.

Yama tests Nachiketas by offering wealth, pleasure, and long life.

Nachiketas replies:

> "Ephemeral are these pleasures. Even the longest life is short."

This establishes the student's commitment to **śreyaḥ (the good)**
rather than **preyaḥ (the pleasant)**.

------------------------------------------------------------------------

## 5.4 Dialectical Analysis

Once qualified, the teacher deploys **prakriyā-based reasoning**.

Common methods include:

-   Neti Neti (negation)
-   Seer--Seen analysis
-   Three-state analysis
-   Five-sheath analysis

Example: Māṇḍūkya Upaniṣad

> "This Self has four quarters."

This introduces structured philosophical analysis.

------------------------------------------------------------------------

## 5.5 Cognitive Disruption

Advaita pedagogy intentionally destabilizes conceptual frameworks.

Example: Īśa Upaniṣad

> "It moves and it moves not; it is far and it is near."

These paradoxical statements break habitual categories of thought.

------------------------------------------------------------------------

## 5.6 Self‑Knowledge Recognition

The culmination of inquiry is identity recognition.

Example:

> "This Self is Brahman."

Or:

> "That Person there---That am I."

This knowledge removes ignorance.

------------------------------------------------------------------------

## 5.7 Stabilization (Nididhyāsana)

Even after insight, habitual identification may persist.

Thus the tradition prescribes continued contemplation.

Goal:

stable knowledge free from doubt.

------------------------------------------------------------------------

# 6. Core Teaching Procedures (Prakriyās)

The Upaniṣads repeatedly employ specific pedagogical methods.

## 6.1 Neti Neti (Negation)

Source: Bṛhadāraṇyaka Upaniṣad.

Procedure:

-   negate body
-   negate senses
-   negate mind
-   negate intellect

Principle:

The knower cannot be the known.

------------------------------------------------------------------------

## 6.2 Dṛg--Dṛśya Viveka (Seer--Seen Analysis)

Procedure:

objects → senses → mind → awareness

Conclusion:

awareness is the ultimate seer.

------------------------------------------------------------------------

## 6.3 Avasthā‑traya (Three-State Analysis)

Source: Māṇḍūkya Upaniṣad.

States analyzed:

-   waking
-   dream
-   deep sleep

Conclusion:

The Self transcends all three.

------------------------------------------------------------------------

## 6.4 Pañca‑Kośa (Five Sheaths)

Source: Taittirīya Upaniṣad.

Layers examined:

-   physical body
-   vital energy
-   mind
-   intellect
-   causal sheath

The Self is beyond all layers.

------------------------------------------------------------------------

## 6.5 Sarvātma Bhāva (Universal Self)

Source: Īśa Upaniṣad.

> "He who sees all beings in the Self and the Self in all beings."

Purpose:

remove separation.

------------------------------------------------------------------------

## 6.6 Mahāvākya Teaching

Examples:

-   tat tvam asi
-   ahaṁ brahmāsmi
-   ayam ātmā brahma
-   prajñānam brahma

These statements reveal identity between Self and Absolute.

------------------------------------------------------------------------

## 6.7 Cause--Effect Analysis

Example:

clay → pot

Effect cannot exist apart from cause.

Thus the world depends on Brahman.

------------------------------------------------------------------------

# 7. Dialogue Control Logic

In a pedagogical system such as AIM, the following control logic may be
implemented.

detect_student_state()

IF ignorance: provoke inquiry

IF inquiry present: test qualification

IF qualified: select prakriyā

apply teaching sequence

observe student response

repeat until recognition occurs

------------------------------------------------------------------------

# 8. Termination Condition

The teaching process concludes when the student clearly recognizes:

Self ≠ body Self ≠ mind Self = Brahman

This recognition eliminates ignorance.

------------------------------------------------------------------------

# 9. Implementation Implications for AIM

AIM should therefore include:

1.  Student state detection
2.  Prakriyā selection engine
3.  Dialogue-based inquiry
4.  Recursive reasoning loops
5.  Stabilization guidance

The system should behave as a **dialectical guide**, not merely an
information provider.

------------------------------------------------------------------------

# 10. Summary

Advaita pedagogy is a structured teaching system consisting of:

-   diagnostic inquiry
-   philosophical analysis
-   cognitive disruption
-   identity recognition

The Upaniṣads provide the **canonical dataset** from which these
procedures are derived.

This document formalizes that pedagogy for computational implementation.
