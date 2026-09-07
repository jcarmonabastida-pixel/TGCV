# SLR-1 Source Dossier — SRC-SCI-001

**Status:** RECONSTRUCTED / WORKING
**Source:** Petersen, M. G., Rasmussen, M. K., & Trettvik, J. (2020), *Affordances of Shape-Changing Interfaces: An Information Perspective on Transformability and Movement*, DIS 2020, pp. 1959–1971. DOI: 10.1145/3357236.3395521.
**Classification:** **AC2 — STRONG STRUCTURAL EQUIVALENCE; AC3 NOT ESTABLISHED**

## Why this source is relevant

This source directly tests the narrower TGCV novelty claim because it links **system transformation** to **changes in affordances/action possibilities**. The paper states that affordances change as a shape-changing interface alters its shape, with the user continuously informed about the state of the interface and the functions it can perform. It also explicitly discusses “dynamic affordances” as perceived action possibilities that change with changes in shape. citeturn1search35turn1search0

## Evidence extraction

### E1 — changing system conditions alter action possibilities

The paper's central domain is shape-changing interfaces. Its analysis treats interface transformation as changing what the interface can do and what action possibilities it presents. The full-text record states that affordances change as the interface alters its shape. citeturn1search35

### E2 — explicit state/function relation

The authors frame affordances as information concerning the interface's ability to transform its shape and the way movement communicates its state/animacy. The paper therefore links the changing physical/configurational condition of the system to the functions/actions that can be performed. citeturn1search0

### E3 — dynamic affordance concept

The paper situates shape-changing affordances within the broader dynamic-affordance literature and reports the definition of dynamic affordances as perceived action possibilities that change with changes in shape. citeturn1search35

### E4 — transformation is not merely an external transition

Unlike sources that simply execute a fixed transformation rule, this source explicitly studies how the system's changing form alters the affordances available to the user. This makes the direction relevant to TGCV:

`system transformation/change → changed action possibilities`.

### E5 — analytical limitation

The paper's contribution is conceptual/design-oriented: it proposes an information perspective and design strategies for communicating transformability and movement. It does not provide a general formal set `T_acc`, a predicate `P_τ(S,C,L)`, or a quantitative/structural delta `ΔT_acc` over the complete action space. citeturn1search0

## TGCV mapping

| TGCV element | SCI analogue | Assessment |
|---|---|---|
| `S` | current physical/configurational state of the interface | explicit conceptually |
| `T_acc` | functions/action possibilities afforded by the interface | strong analogue |
| accessibility predicate | whether a function/action is afforded by current interface form | implicit/conceptual |
| `ΔT_acc` | change in affordances when shape changes | **explicit phenomenon, but not formalized as a set delta** |
| `Reach` | possible user actions/functions after configuration change | partial |
| `Trajectory` | sequences of interaction/shape change | partial |
| `Outcome` | interaction/function achieved | partial |
| `Value` | user-facing utility/information/design quality | not equivalent to TGCV value architecture |
| mechanism | shape transformation/movement of interface | explicit domain mechanism |

## AC2 assessment

**AC2 — STRONG STRUCTURAL EQUIVALENCE CONFIRMED.**

The source establishes a direct structural correspondence:

`system state/shape → affordances/action possibilities`.

It additionally treats changes in the system's shape as producing changes in affordances. This is materially closer to TGCV's `ΔT_acc` proposition than the MDE cluster, because the **change in action possibilities is itself part of the phenomenon being discussed**, not merely an incidental consequence of executing a rule. citeturn1search35

## AC3 assessment

**AC3 — NOT ESTABLISHED.**

Three gaps remain decisive.

### 1. No complete accessible-transformation object

The source discusses affordances/action possibilities, but does not construct a general object corresponding to the complete accessible transformation space `T_acc`.

### 2. No transversal formal change operator

Although the phenomenon “affordances change when shape changes” is explicit, there is no general analytical operator or representation of:

`ΔT_acc = T_acc(S_{t+1},C_{t+1},L) − T_acc(S_t,C_t,L)`.

The change is conceptual and domain-specific rather than a transversal analytical variable.

### 3. No general downstream architecture

The source does not establish the complete TGCV relation:

`mechanism → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

The contribution concerns affordance information and interaction design in shape-changing interfaces rather than a cross-domain theory of value construction.

## Falsification significance

This source **falsifies a stronger version of TGCV novelty**: TGCV cannot claim to be the first literature to observe that changes in a system can change the action possibilities it affords.

It also strengthens the case that the empirical phenomenon underlying `ΔT_acc` is already recognizable in several distinct traditions:

- model transformation / state-space exploration;
- robotics affordance foresight;
- dynamic affordances;
- shape-changing interfaces.

However, the current source does **not** establish that any of those traditions already contain the transversal analytical construction proposed by TGCV.

## Current SLR-1 decision

- `AC2`: confirmed.
- `AC3`: not established.
- Broad novelty claim about “state change can alter action possibilities”: **absorbed / rejected**.
- Narrow TGCV proposition about a transversal explicit analytical object `ΔT_acc` and its downstream relation: **still unresolved**.
- TGCV Core: unchanged.
- EXT-1.1 result: not used.

## Next controlled operation

The next search should move one level higher and test **formal/general theories of affordance landscapes or possibility-space change**, especially work that explicitly models the landscape/set itself as a dynamical object rather than discussing individual affordances. The Rietveld/Kiverstein “landscape/field of affordances” tradition is an immediate candidate cluster, followed by formal possibility-space or action-space representations.

## Integrity note

This dossier is a current reconstructed research record, not a recovered historical dossier. Evidence and architectural interpretation are kept separate.