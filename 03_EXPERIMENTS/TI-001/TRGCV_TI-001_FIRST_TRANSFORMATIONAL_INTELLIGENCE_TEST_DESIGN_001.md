# TGCV — First Transformational Intelligence Test
## TI-001 Conceptual Experimental Design

**Date:** 2026-09-24  
**Status:** DESIGN ONLY — SCIENTIFIC EXECUTION NOT AUTHORIZED  
**Purpose:** Define the first falsifiable test of the Transformational Intelligence hypothesis without measuring or assuming "intelligence" directly.

## 1. Research question

Can a system use information about the structure or evolution of its accessible transformation space to alter subsequent transformation handling in a way that cannot be explained solely by the transformations currently executable from its present state?

## 2. Core distinction

The test separates three things:

- current executable transformations;
- information about present/future transformation-space structure;
- subsequent transformation handling.

The test therefore does not infer intelligence from the existence of a rich transformation space.

## 3. Minimal causal design

Let S_t be the current system state and T_acc,t its currently accessible transformations.

Construct matched conditions in which the immediately executable transformation set is held constant, while information available to the system about the structure/evolution of the transformation space differs.

**Control condition:** the system receives only information required to execute currently available transformations.

**Treatment condition:** the system additionally receives structured information about transformation-space evolution, such as possible successor accessibility, branching structure, persistence, turnover, or anticipated reconfiguration.

The subsequent transformation-handling policy is then observed.

## 4. Critical control

The treatment must not simply provide additional task-relevant information that directly reveals which action has the highest payoff.

The manipulated information should concern transformation-space structure/evolution rather than an explicit recommendation or outcome label.

Otherwise the test would measure ordinary information-assisted decision making rather than the hypothesised capability.

## 5. Observable variables

For each decision point record:

- S_t
- T_acc,t
- transformation-space information exposed to the system
- T_real,t or selected transformation
- S_t1
- T_acc,t1
- subsequent transformation choice
- trajectory segment
- whether behaviour changes between matched conditions

Transformation-space descriptors may include A, G, L, P, R and D, but no scalar TI score is required.

## 6. Primary test

The primary comparison is behavioural:

**Does additional information about transformation-space structure/evolution change transformation handling when current executable transformations are otherwise held constant?**

A positive result would support **transformation-space use**.

A null result would leave the TI hypothesis unsupported at this level.

Neither result by itself establishes a general Transformational Intelligence construct.

## 7. Stronger anticipatory test

A second stage may expose information about a future transformation-space consequence that is not directly observable from the current state.

The system must then choose a transformation before that consequence materialises.

Evidence that the choice systematically incorporates the future transformation-space consequence would support the **anticipation** dimension of the hypothesis.

## 8. Adaptation test

A third stage may change the transformation-space dynamics over episodes while keeping the task family constant.

The question becomes whether the system changes its transformation-handling policy as the transformation space evolves.

This targets the **adaptation** dimension.

## 9. Capability decomposition

The programme therefore proceeds in increasing evidential strength:

1. Representation — can the system access a representation of transformation-space structure?
2. Sensitivity — does behaviour respond to changes in that structure?
3. Use — does the system use that information in transformation handling?
4. Anticipation — does it incorporate expected future transformation-space consequences?
5. Adaptation — does its handling policy change as transformation-space dynamics change?
6. Generalisation — does the capability persist across contexts or domains?

These are research stages, not a scoring rubric.

## 10. Falsification conditions

The hypothesis should not be credited if:

- treatment and control differ in current executable transformations;
- treatment information directly identifies the preferred action;
- behavioural differences disappear after controlling for ordinary task information;
- the system merely executes a supplied transformation-space recommendation;
- effects occur only in one fixed instance with no transfer;
- the observed behaviour can be fully explained by current-state reaction without transformation-space information.

## 11. Independence and reconstruction

A future execution package should freeze:

- system/domain;
- state representation;
- transformation identity rules;
- accessibility computation;
- transformation-space information supplied under each condition;
- randomisation;
- task instances;
- outcome-independent primary metrics;
- executor scripts;
- reconstruction protocol.

At least two independent executors should reconstruct the frozen experimental records before scientific interpretation.

## 12. Metrics

The primary metrics should concern transformation handling, not value:

- transformation-choice divergence between matched conditions;
- use of transformations whose relevance depends on future accessibility;
- anticipatory selection consistency;
- policy adaptation across controlled transformation-space changes;
- cross-instance generalisation.

No aggregate "TI score" should be introduced in the first test.

## 13. Value firewall

Value, reward, utility, performance and business outcome measures are excluded from the primary TI test.

They may be introduced later as external outcome variables in a separate study.

This preserves the distinction between:

transformation-space dynamics -> transformational capability -> outcomes/value.

## 14. Relationship to TR-131

TR-131 supplies the representational substrate needed for the new programme:

`S_t -> T_acc,t -> T_real,t -> S_t1 -> T_acc,t1`

V007 demonstrates that this substrate can reveal different transformation-space dynamics across VisitAll and PRISM.

TI-001 therefore does not reopen TR-131 and does not require modifying its Core conclusions.

## 15. First candidate implementation

A particularly clean first implementation would use a finite-state synthetic environment in which:

- current T_acc is identical across treatment and control;
- future T_acc differs according to the transformation selected;
- the system can receive either no information or structured information about that future reconfiguration;
- transformation choices are recorded before future states are revealed;
- multiple independent instances are generated from a frozen protocol.

This isolates the hypothesised capability more cleanly than starting with a real-world application.

## 16. Decision gate

TI-001 should not be executed until a preflight confirms that the treatment manipulation changes only access to transformation-space information and not the current action set, direct outcome information, or task difficulty in an uncontrolled manner.

Scientific interpretation remains conditional on independent reconstruction and integrity audit.

## 17. Current status

TI-001 is a **falsifiable experimental design**, not an executed experiment.

It does not establish Transformational Intelligence.

It establishes the next empirical question needed to determine whether the capability hypothesised by TGCV can be distinguished from ordinary transformation execution and ordinary information-assisted decision making.
