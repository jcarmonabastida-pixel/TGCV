# TGCV graph derivation contract 001 — mapping from the system graph

**Status:** design proposal; not implemented or approved as canonical TGCV semantics.
**Scope:** define how the second graph is populated after the user has seen the familiar system graph.
**Scientific boundary:** no mapping rule in this document is evidence that TGCV is empirically valid, and no mapping should imply value causality.

## 1. Governing rule

The system graph and the TGCV graph answer different questions. Therefore, **do not automatically convert every system state into a transformation, every transition into an accessible transformation, or every execution condition into a constraint on T_acc**.

The TGCV graph may be populated only from:
1. explicit TGCV-specific information supplied by the user or included in a curated example; or
2. a documented, versioned mapping rule whose inputs and outputs can be inspected and reproduced.

If neither is available, the demonstrator must ask for the missing information or show an explicitly incomplete TGCV graph. It must not fabricate a complete graph.

## 2. Three supported mapping outcomes

Every system-to-TGCV mapping should have one of these statuses:

- **Declared:** supplied directly by the user or included explicitly in the loaded example.
- **Derived:** produced by a named/versioned mapping rule, with source elements and output recorded.
- **Unresolved:** there is insufficient information or no applicable rule. Show what is missing; do not infer a value.

These are provenance statuses, not confidence scores and not claims about empirical truth. A derived mapping is reproducible relative to its declared inputs and rule, but is not thereby scientifically validated.

## 3. Derivation workflow

### Step 1 — preserve the system graph

Render Graph 1 as today, including system states, transitions, and any execution conditions or temporal prerequisites supported by the model. Do not mutate its semantics to make it resemble TGCV.

### Step 2 — inspect mapping availability

Check whether the loaded model/example includes explicit TGCV mapping data. If not, check whether a documented mapping rule applies to the available fields. Never infer a mapping merely from similar names or labels.

### Step 3 — build the TGCV graph from supported information

The second graph should identify, as applicable:

- the represented system/domain and scenario;
- transformations and their identifiers/descriptions;
- relations among transformations and their declared meanings;
- the basis for including each transformation in T_acc;
- interactions/mechanisms and the explicit rule by which they may change T_acc or relations;
- before/after accessibility and derived differences, when a rule and inputs support them;
- reachable transformation trajectories, only when the relation and trajectory semantics are specified.

Each element or derived result must expose whether it is declared, derived, or unresolved, and its source/rule.

### Step 4 — ask only for essential missing information

When the system graph is not sufficient, do not force the user to fill a large form or enter JSON. Explain the specific gap in plain language and ask for the smallest next piece of information that permits progress.

For example:
- If the transformation set is unknown: ask which operations/capabilities the system can currently perform, not which state labels to reuse.
- If a proposed relation has no defined meaning: ask what the relation means and under what rule it holds.
- If a change in T_acc is asserted without a mechanism/rule: ask what interaction is supposed to change accessibility and how the change is specified.
- If only state-transition execution conditions are available: explain that these determine when a system transition can execute, but do not by themselves specify which transformations belong to T_acc.

### Step 5 — validate and present the result

Before presenting a complete TGCV graph, check identifiers, relation endpoints, duplicate elements, required provenance, rule applicability, and consistency between declared and derived sets. Invalid or unresolved items should be visible and should not silently become valid transformations or paths.

## 4. Minimal information contract for Graph 2

The exact serialized schema remains open. Functionally, the demonstrator needs the following information when it cannot be derived from an explicit mapping:

| Information | Why it is needed | If missing |
|---|---|---|
| System/domain and scenario reference | Establishes what the TGCV graph is about | Ask which system/scenario the graph describes |
| Accessible transformations for the chosen reference | Defines the initial transformation set | Ask for the currently accessible operations/capabilities |
| Relation types and their meanings | Makes edges interpretable rather than decorative | Ask for the intended relation meaning |
| Interaction/mechanism under consideration | Specifies what could change the transformation space | Leave change analysis unresolved |
| Explicit rule or declared before/after sets | Makes ΔT_acc and changed relations reproducible | Do not derive ΔT_acc |
| Trajectory/reachability rule | Defines which transformation sequences count as reachable | Show transformations/relations only; do not claim trajectories |

This is a functional information contract, not a final ontology or schema. It does not prescribe that every example must contain every field: fields may be derived only when an applicable, documented rule exists.

## 5. Conditions: strict boundary

- In Graph 1, a condition/guard answers whether a system transition may execute in a given context.
- In Graph 2, membership in T_acc answers whether a transformation is considered accessible under the declared TGCV representation.
- The two may be related only by an explicit mapping rule that specifies how a system guard affects transformation accessibility.
- The condition evaluator proposal remains paused. Do not make its typed predicate schema a prerequisite for the TGCV graph unless a reviewed requirement shows that a specific condition is part of the accessibility model.
- A transition being executable does not prove that it represents one TGCV transformation; a blocked transition does not automatically prove that a transformation is absent from T_acc.

## 6. Example loading and user entry

Both entry paths follow the same provenance rule:

- **User-created system graph:** preserve the graph, then request or derive TGCV-specific data through documented mapping rules.
- **Loaded example:** prefer examples that include a reviewed TGCV mapping and provenance. If the example contains only a system graph, do not present a complete TGCV graph without asking for missing inputs or clearly marking an illustrative mapping as such.

The UI should distinguish a **demonstration mapping** (stipulated to explain the concept) from a **mapping asserted about the user's actual system**. The former must be labeled illustrative; the latter needs explicit inputs/rules and provenance.

## 7. Acceptance criteria

1. The same system graph can be displayed without requiring a TGCV mapping.
2. The TGCV graph is generated only from declared inputs or a documented mapping rule.
3. Every TGCV element and derived result exposes declared/derived/unresolved status and provenance.
4. A system transition, a TGCV transformation, and a relation affecting accessibility are never silently treated as equivalent.
5. System execution conditions are not converted into T_acc rules unless an explicit mapping rule states how.
6. When information is insufficient, the UI asks a targeted plain-language question or shows a clearly incomplete graph; it does not fabricate edges, transformations, or ΔT_acc.
7. The demonstrator distinguishes illustrative example mappings from mappings asserted about a real user-described system.
8. Edits invalidate affected derived results and preserve provenance across export/import.
9. Synthetic acceptance tests validate implementation behavior only; they do not establish scientific validity of TGCV.

## 8. Change boundary and next gate

This document is design-only. It does not change main, executable code, model schemas, the TGCV Core, or scientific execution.

**Next gate:** review whether this information contract is understandable and sufficient. Only after explicit acceptance should the team define the serialized model schema and a small end-to-end test. Do not implement a general inference engine or a condition evaluator as a shortcut to filling missing TGCV information.
