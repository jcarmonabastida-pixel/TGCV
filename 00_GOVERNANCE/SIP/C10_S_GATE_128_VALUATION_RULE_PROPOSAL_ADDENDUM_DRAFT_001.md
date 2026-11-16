# C10-S — Gate 128: propuesta de regla normativa mínima para V_cont

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** PROPOSAL_ONLY / EXPLICIT_ACCEPTANCE_REQUIRED / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION  
**Registro rector:** `00_GOVERNANCE/SIP/C10_S_VCONT_MINIMUM_SYNTHETIC_VALUATION_RULE_GATE_128_DRAFT_001.md`.

Gate 128 concluye que DEC-C10-099 ya selecciona V_cont como dimensión unitaria mínima provisional y DEC-C10-100 fija su truth temporal. No obstante, DEC-C10-099 exige un criterio normativo y mecanismo de valoración estipulados ex ante. Esa condición no se satisface automáticamente con la definición técnica ENABLED/PROFILE ni con la fórmula de agregación.

Se propone VCONT-B1-MIN: desde la perspectiva sintética B1, la consecuencia focal de esta dimensión es la continuidad temporal de la capacidad de admisión conforme a ENABLED y exposición de PROFILE; dentro de esta dimensión, mayor continuidad se valora débilmente mejor y niveles iguales reciben igual valoración. No se introduce función cardinal, peso, umbral, compensación o dimensión adicional. El alcance se limita a Value en la dimensión de continuidad funcional; no representa Value global, beneficio neto ni todas las consecuencias B1.

La propuesta es metodológicamente mínima, pero su preferencia ordinal es normativa y requiere aceptación explícita. Si se rechaza, V_cont permanece resultado/constructo seleccionado sin interpretación confirmatoria como Value. Si se exige valorar costes, riesgos, demoras u otras consecuencias dentro del mismo endpoint, la dimensión unitaria es insuficiente y habría que reabrir formalmente el alcance.

No se actualiza el plan integrado porque el artefacto completo de gran tamaño no pudo recuperarse íntegramente en esta operación; no se modifica a ciegas. El presente addendum y el registro Gate 128 quedan como documentos independientes hasta su reconciliación posterior con el plan. No se modifican DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o main. `scientific_execution=false`; `execution_authorized=false`.
