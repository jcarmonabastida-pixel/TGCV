# TGCV — WP2-C03 Production AI Agents / Coupa Sentinel Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.12 / RMA traceability v3.35

## 1. Evidence boundary

AWS's current public case study describes Coupa's Sentinel as a production internal AI-agent solution. It reports agents operating across engineering tools and taking real actions including opening pull requests, creating tickets and querying live databases. The same source describes secure authentication, session persistence, governance, tool calling, model routing and knowledge grounding as parts of the production architecture. AWS reports that Sentinel runs hundreds of agents across many workflows and that agent invocations flow through Amazon Bedrock AgentCore. These are vendor/customer-reported architectural and operational facts, not TGCV evidence. citeturn0search0

AWS's current architecture guidance independently describes agent systems as requiring interaction among users, foundation models, tools and knowledge sources, with access control, authentication, session persistence, tool discovery and multi-agent coordination. Tool access is dynamically selected by agents at runtime, rather than being a fixed sequence of API calls. citeturn0search1turn0search2

## 2. Decision-time boundary

The most informative TGCV boundary is an agent decision point immediately before tool selection/execution for a concrete engineering task.

Frozen variables would include:

- current task/request state;
- agent identity and delegated user identity;
- available tool catalogue;
- tool versions and operational availability;
- authorization policies and scopes;
- current session/memory context;
- accessible knowledge sources;
- model-routing state and relevant resource constraints;
- security/governance policies;
- state of the downstream engineering systems.

This boundary is substantially more explicit than in C01 because AWS documents authorization, tool discovery, runtime selection and persistent context as distinct architectural concerns. It nevertheless does not provide a frozen production decision trace sufficient to reconstruct an empirical `T_acc` without additional data.

## 3. Candidate state representation

A bounded analytical representation is:

`S_t = {agent state, task state, downstream engineering-system state, available tools, permissions}`

`C_t = {session/memory context, policies, identity context, tool availability, model/resource constraints}`

`L = {tool-specific and platform-level admissibility rules}`

This is a TGCV screening representation, not a claim that Sentinel internally represents its state in these terms.

## 4. Candidate transformations

The documented production functions imply concrete candidate transformations such as:

- query a live database;
- inspect or retrieve engineering information;
- create a ticket;
- open a pull request;
- modify code through an authorized development tool;
- invoke another agent/tool;
- retrieve knowledge-base context;
- route a task to a model with different capabilities/cost characteristics;
- continue a task using persisted session or memory context.

These are candidate transformations, not an exhaustive `Uτ`.

## 5. Accessibility/admissibility hypothesis

C03 provides a particularly clean mechanism-first hypothesis:

`identity / permission / tool / system-state change → admissibility of agent action changes → accessible agent transformation space changes`

For a concrete action `τ`, the relevant rule can be expressed as:

`Pτ(S_t,C_t,L)=1`

only when the required tool exists, the agent has the required authorization, the downstream system is available and policy constraints are satisfied.

Then:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

A change such as granting/revoking a permission, registering/de-registering a tool, changing a policy scope, or changing the downstream system state can therefore potentially alter `T_acc`.

This is a stronger fit to the TGCV accessibility concept than merely observing that an AI agent uses many technologies: the candidate transformation set is directly conditioned on external state and governance.

## 6. The critical distinction

There are two competing interpretations.

### A. Conventional agent orchestration

The system is adequately described as an agent runtime plus tools, IAM/OAuth, policy enforcement, memory and workflow orchestration. Changes in available actions are simply consequences of authorization and system state. No additional transformation-space layer is needed.

### B. Transformational coupling

The same changes can be represented as systematic changes in the agent's future accessible transformation space. For example:

`permission granted → τ_write_repository becomes admissible`

`database access revoked → τ_query_live_db becomes inadmissible`

`tool registered → new transformation family becomes accessible`

`policy tightened → subset of previously accessible transformations closes`

`downstream system state changes → some transformations become unavailable while alternatives remain accessible`

The scientific/application question is not whether these facts occur—they plainly do in ordinary agent systems—but whether a common `T_acc` representation yields additional explanatory or operational information about **future action possibilities and trajectories**.

## 7. Multidomain coexistence vs transformational coupling

The domains involved include AI reasoning/model infrastructure, engineering tools, databases, identity/security, knowledge sources and production systems. Public documentation establishes their interaction. citeturn0search0turn0search9

The stronger coupling hypothesis survives conceptually if a transition in one domain changes the admissibility of transformations in another:

`identity/policy → tool accessibility → engineering action → downstream system state → subsequent agent options`

That is a genuine cross-domain chain of changing future action possibilities.

However, this may still be fully captured by conventional access-control, capability-based security, workflow and state-machine representations. Therefore multidomain coupling is **plausible but not yet differentially demonstrated**.

## 8. Stronger TGCV test opportunity

C03 offers a more controlled experimental route than C01 because the candidate transformation space can be deliberately made finite.

A synthetic benchmark could define, for example:

- 4–8 agent actions;
- 3–5 tools;
- explicit permission policies;
- a small database/repository/ticket system state;
- a finite set of task states;
- controlled state transitions that grant/revoke capabilities or alter downstream availability.

Then independently reconstruct:

`T_acc,0`

and

`T_acc,1`

after each controlled change.

This permits testing whether a cross-domain state change produces a reproducible transformation-space change without relying on outcome performance.

## 9. Alternative-explanation test

The baseline should explicitly include conventional models already natural to agentic systems:

- access-control matrices;
- capability/permission models;
- finite-state workflows;
- tool registries;
- policy engines;
- dependency graphs.

A TGCV demonstration is informative only if its transformation-space representation exposes a property that these baselines do not represent equivalently, for example a systematic relationship between state transitions, newly accessible action families and subsequent trajectory possibilities across domain boundaries.

If the baseline captures the same information with equal clarity, C03 remains a multidomain applicability case but not evidence of a distinct TGCV contribution.

## 10. Minimum next proof

**Agent Accessible-Transformation Mapper — synthetic benchmark.**

Required components:

1. frozen agent/task state;
2. finite tool/action catalogue;
3. explicit identity and permission state;
4. outcome-independent admissibility predicates;
5. `T_acc,0` reconstruction;
6. controlled cross-domain transition, such as permission/tool/backend change;
7. `T_acc,1` reconstruction;
8. trajectory generated after the accessibility change;
9. conventional access-control/workflow baseline;
10. comparison of explanatory information, reproducibility and operational interpretability.

A useful first intervention is deliberately simple:

`permission P: denied → granted`

with all other variables frozen.

The expected structural test is whether the change opens a defined subset of transformations and whether those newly accessible transformations alter the subsequent trajectory in a way that can be reconstructed independently of the final outcome.

## 11. Maturation route

**Primary route: Applied Demonstration.**

C03 is unusually suitable for a small synthetic demonstrator because tools, permissions and downstream systems can be represented as explicit finite objects.

A scientific route becomes interesting only if the demonstrator identifies a non-trivial property that warrants an empirical study beyond a conventional capability/permission model.

## 12. Current disposition

**WP2-C03 — COUPLING-CANDIDATE.**

The candidate has stronger conceptual reconstructability than C01 because the accessible action space can be bounded explicitly through tools, permissions and backend state. However, the current public evidence does not demonstrate that TGCV's transformation-space representation adds information beyond established agent orchestration, access-control and workflow representations.

**No scientific claim upgrade.** No change to Core, RMA, Evidence→Claim Matrix, C09 or existing evidence state.

## 13. Cross-case observation after C01 + C03

The same TGCV hypothesis appears in two structurally different forms:

- **C01:** federated technical orchestration where network/compute/security state may alter service transformations.
- **C03:** agent action orchestration where identity/tool/backend state may alter executable transformations.

This is useful for WP2 because the candidate mechanism is not tied to one technology family. At the same time, both cases currently admit strong conventional explanations. The next screens should therefore test whether this recurring pattern survives in a physical-digital case (C04) and a resource/constraint case (C05).

**Next case:** WP2-C04 — Cross-domain digital twin predictive maintenance.
