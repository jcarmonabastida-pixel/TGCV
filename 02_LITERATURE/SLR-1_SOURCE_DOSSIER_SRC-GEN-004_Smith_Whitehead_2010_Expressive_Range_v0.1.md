# SLR-1 Source Dossier — SRC-GEN-004

**Source:** Gillian Smith & Jim Whitehead (2010), *Analyzing the Expressive Range of a Level Generator*, DOI `10.1145/1814256.1814260`.

## Family

**Generativity and Combinatorial Possibility Approaches**  
**Status:** INCLUDED — substantive comparison

## Analytical construction found

The paper defines and analyzes the **expressive range** of a procedural generator as the variety of content it can produce. Its method explicitly visualizes the generator's generative space, identifies holes/biases, and studies how changing input parameters changes the space of generated content. citeturn1search1turn1search3

The paper therefore provides strong prior art for treating the space produced by a generative system as an explicit analytical object whose structure can change when system parameters change.

## TGCV mapping

| TGCV element | Prior-art correspondence | Assessment |
|---|---|---|
| `S` | generator + parameter configuration | Strong analogue |
| possible outputs | generative/expressive range | Direct |
| transformation | generation procedure | Strong |
| accessibility | producibility by generator | Strong analogue |
| `T_acc` | not transformations, but generated-content space | Partial |
| change in accessible space | parameter-induced expressive-range change | Strong analogue |
| `P_τ(S,C,L)` | no generic transformation accessibility predicate | Missing |
| reachability/trajectory | not central | Missing |
| outcome/value | content quality/metrics | Partial |
| full TGCV architecture | no | Not established |

## Absorption classification

**AC2 — VERY STRONG / NEAR-DIRECT STRUCTURAL ANTECEDENT**  
**AC3 — NOT ESTABLISHED**

This is an important boundary because it directly establishes that a generative system's **space of producible possibilities can be represented and compared across changes in the generator or its parameters**. Consequently, TGCV cannot claim novelty merely for making a system-dependent possibility/generative space explicit or for analyzing its change.

The remaining distinction is that expressive range concerns **generated outputs/content**, whereas TGCV's candidate object is the space of **accessible transformations** themselves, with `ΔT_acc` explicitly central and linked to downstream reachability and trajectories. The paper does not provide that cross-domain architecture.

## Decision

Retain as a major AC2 prior-art boundary. No AC3 architectural absorption established.

- Core: unchanged.
- TR-130–TR-140: not reopened.
- EXT-1.1: not used.
