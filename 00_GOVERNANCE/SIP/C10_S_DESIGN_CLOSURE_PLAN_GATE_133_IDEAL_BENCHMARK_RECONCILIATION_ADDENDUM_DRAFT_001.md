# C10-S — Addendum al plan de cierre: Gate 133, benchmark ideal y semántica temporal

**Fecha:** 2026-11-16  
**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_IDEAL_BENCHMARK_AND_TEMPORAL_SEMANTICS_RECONCILIATION_GATE_133_DRAFT_001.md`  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** IDEAL_BENCHMARK_SCOPE_BOUNDED / TEMPORAL_SEMANTICS_PARTIAL / WORKFLOW_VALIDATION_OPEN / NO_FREEZE / NO_EXECUTION.

Gate 133 concluye que el harness ofrece un benchmark ideal de asignación ITT-Z/ITT-G bajo outcome V_cont binario por intervalos y S3 perfecto/completo. R0_MEASUREMENT_ADVERSE es STATUS_ONLY para los cuatro estimandos y dispone de test fuente que comprueba abstención, no recuperación numérica. Gates 200–205 ya gobiernan EP-01/02/03; Gate 205 deja pendiente validación integral YAML/actionlint.

La correspondencia temporal con DEC-C10-100…102 es parcial: hay ventana común, intervalos iguales y truth por unidad/régimen/intervalo, pero no estado UNKNOWN en truth, eventos intraintervalo, event/observation/ingestion time ni bounds para UNKNOWN. No confundir missingness observacional S3 con UNKNOWN funcional.

**Gate 134:** determinar, contra DEC-C10-100…102 y el contrato integrado, si el benchmark debe incorporar UNKNOWN/continuidad estricta completa o si su alcance binario intervalizado está explícitamente autorizado como benchmark acotado. No modificar código ni ejecutar.
