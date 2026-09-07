# SLR-1 Source Dossier — SRC-SSR-002

**Source:** Gabel, T.; Riedmiller, M. (2008), *Reinforcement Learning for DEC-MDPs with Changing Action Sets and Partially Ordered Dependencies*, AAMAS 2008, pp. 1333–1336, DOI `10.1145/1402821.1402865`.

## Family

**State-space and reachability approaches**  
**Status:** INCLUDED — substantive comparison

## Analytical construction found

The source defines decentralized Markov decision processes with explicit state space `S`, joint action space `A`, transition function `P(s'|s,a)` and reward `R(s,a,s')`. Its target subclass explicitly has **changing action sets** and partially ordered transition dependencies. In the job-shop scheduling application, a resource's local state is represented by the changing set of jobs waiting for processing; after an operation is completed, the job moves to another resource, which changes that resource's local action set. citeturn1search47turn1search49

## TGCV mapping

| TGCV element | Prior-art correspondence | Assessment |
|---|---|---|
| `S` | DEC-MDP world state | Direct |
| transformation/action `τ` | agent action | Direct domain-specific analogue |
| accessibility | changing/state-dependent action set | Direct |
| accessible transformation space | current action set | Very strong structural analogue |
| change in accessible space | changing action set | Very strong / direct |
| mechanism causing change | state transitions and inter-agent dependencies | Strong |
| reachability/trajectory | transition function and sequential decision process | Strong |
| outcome/value | reward and task objective | Strong but domain-specific |
| domain-independent `T_acc` | not established | TGCV remainder |
| central `ΔT_acc` as transversal analytical object | not established as such | TGCV remainder |
| full `ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value` architecture | partial distributed-MDP analogue, not transversal architecture | TGCV remainder |

## Absorption classification

**AC2 — VERY STRONG / NEAR-DIRECT**  
**AC3 — NOT ESTABLISHED**

This is stronger than ordinary reachability prior art because it explicitly combines changing action sets with state transitions and dependencies that modify other agents' future action sets. It therefore directly absorbs the claim that accessible actions can change as a consequence of system evolution and that those changes affect subsequent decision trajectories.

It still does not establish the TGCV architecture as a domain-independent analytical layer. The action set is embedded in the MDP/agent formalism, and `ΔT_acc` is not isolated as the transversal object of analysis.

## Decision

Retain as a major prior-art boundary for the state-space/reachability family. It materially strengthens the AC2 case but does not establish AC3 or trigger a TGCV Core change.

- Core: unchanged.
- TR-130–TR-140: not reopened.
- EXT-1.1: not used.
