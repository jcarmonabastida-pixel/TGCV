# C10-S — Gate 147: aceptación de separación entre configuración declarativa y disponibilidad operativa efectiva

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** R147-A_ACCEPTED_FOR_SYNTHETIC_DGP_LOGICAL_SEMANTICS / MECHANISM_COVERAGE_AUDIT_OPEN / MATERIALIZATION_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_TESTS / NO_EXECUTION.

## 1. Acto de aceptación

Se registra la aceptación expresa del usuario de R147-A. La aceptación es semántica y lógica para el DGP sintético. No crea DEC-C10, no modifica decisiones DEC existentes, no altera el DGP original ni promueve contenido a `main`.

## 2. R147-A — separación de planos funcionales

Se mantienen diferenciados:

1. **Configuración declarativa:** ENABLED/PROFILE, que conserva su semántica propia de configuración.
2. **Disponibilidad operativa efectiva:** condiciones runtime y mecanismos (proceso/módulo, listener/socket/superficie de ingreso, dependencias y capacidad/recursos) cuando su estado altere realmente la capacidad funcional de admisión B1.

Ambos planos pueden evolucionar de manera distinta. Cuando un cambio de cualquiera de ellos altere la función B1 conforme al contrato, su cambio verdadero debe quedar representado en la historia truth pertinente. No se infiere automáticamente que toda señal runtime sea una transición truth: cada mecanismo debe clasificarse según su papel causal/funcional y su relación con el estado de admisión.

Los antecedentes de provisión, instalación, verificación, rollback, reinicio y otros eventos de proceso no constituyen por sí mismos incumplimiento ni transición truth. Solo se consideran antecedentes o evidencia de proceso salvo que el mecanismo funcional correspondiente cambie efectivamente.

## 3. Separación truth / observed_evidence / evaluation

- **Truth:** estado y cambios funcionales verdaderos generados por el DGP, incluidos los planos declarativo y operativo efectivo cuando sean funcionalmente relevantes.
- **Observed evidence:** señales y registros observables (incluida la observación S3) que pueden ser incompletos, tardíos o imperfectos.
- **Evaluation:** derivaciones y adjudicaciones efectuadas por el Evaluator conforme a reglas versionadas, después del sellado del Analyzer.

La detectabilidad S3 no define ni limita la verdad funcional. La falta de observación no convierte por sí misma un estado truth en UNKNOWN. Los defectos de historia/harness siguen siendo defectos de generación o representación conforme a R144-A y R146-D.

## 4. Límite de esta aceptación

R147-A establece la separación conceptual, pero no cierra la auditoría de cobertura de mecanismos ni determina exhaustivamente qué cambios runtime son variables de estado, condiciones causales antecedentes o evidencia observacional. Esa clasificación debe realizarse contra §§49–50 y los contratos existentes, sin ampliar silenciosamente el DGP.

No se definen schema, campos, IDs físicos, serialización, reloj, rejilla, unidad temporal, soporte numérico, T*, Δ, K, calibración S3, fixtures, código, pruebas ni algoritmos ejecutables.

## 5. Continuación de Gate 147

La auditoría pendiente debe reconciliar, al menos:
- cambios ENABLED/PROFILE;
- proceso/módulo;
- listener/socket/superficie de ingreso;
- dependencias que afecten admisión;
- capacidad/recursos que afecten admisión;
- antecedentes de provisión/instalación/verificación/rollback/reinicio;
- ciclo discreto de solicitud, distinguiendo ausencia de solicitud de fallo.

Debe identificar solapamientos, vías funcionales omitidas, duplicaciones de transición y mecanismos sin clasificación suficiente. La aceptación de R147-A no anticipa el resultado de esa auditoría.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
