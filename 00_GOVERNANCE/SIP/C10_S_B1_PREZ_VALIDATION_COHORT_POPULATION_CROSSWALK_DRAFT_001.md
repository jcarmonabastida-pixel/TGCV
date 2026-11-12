# C10-S — Crosswalk de cohorte de validación Need_preZ, roster B1 y poblaciones causales

**ID:** C10-S-B1-PREZ-VALIDATION-POPULATION-CROSSWALK-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / DEC-C10-095_COMPOSITION_CONSTRAINT_ACCEPTED / DEC-C10-096_COHORT_CENSUS_SCOPE_ACCEPTED / E1_E2_NEED_TASK_ONLY / ROSTER_NOT_APPROVED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Pregunta de reconciliación

El contrato de composición de truth Need_preZ exige soporte de truth=1 y truth=0 en una cohorte de validación del procedimiento de adjudicación. La arquitectura C10-S ya distingue, sin embargo, el roster de unidades experimentales, la población causal primaria C1, su subpoblación secundaria y las poblaciones/denominadores de validación.

Este crosswalk evita que el requisito técnico de evaluar la clasificación Need se convierta inadvertidamente en una nueva regla de elegibilidad, un filtro ITT o una alteración de la precedencia poblacional aceptada.

## 2. Fuentes rectoras reutilizadas

- `DEC-C10S-C1-POPULATION-PRECEDENCE-001.md`: P*_{τ2} es la población objetivo primaria candidata de C1; P*_F es la subpoblación secundaria de apertura funcional exclusiva. La decisión no cierra composición, soporte ni identificación.
- `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`, §§15 y 15.1–15.2: C1 es ITT de asignación D2; Need_preZ y E_req_preZ son distintos de E_i y de elegibilidad experimental.
- `C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md`: Need_preZ no es elegibilidad experimental; P*, q_X*, positividad y soporte siguen sin materializarse.
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`: paquete B1/Need separado de U_G y de Evidence→Claim Matrix, con seis artefactos lógicos y segregación Generator/Analyzer/Evaluator.
- `C10_S_B1_PREZ_TRUTH_COMPOSITION_AND_SUPPORT_REVIEW_DRAFT_001.md`: soporte binario para evaluar clasificación Need, sin prevalencias ni balance arbitrarios.
- `DEC-C10-095_B1_NEED_PREZ_EXPLICIT_STIPULATION_COMPOSITION_ACCEPTANCE.md`: estipulación explícita y reservada por B1/UE, mapping determinista, soporte 1/0 como gate y prohibición de selección post hoc por Need.

No se reabre ninguna decisión aceptada ni se crea una población causal nueva.

## 3. Distinciones de conjuntos

| Conjunto | Función | Relación con Need_preZ |
|---|---|---|
| Roster DGP de UE/B1 | Marco de unidades sintéticas definido por el diseño | Cada UE incluida tendrá su B1 vinculada según DEC-C10S-B1-UNIT-001; Need se estipula en t−1 |
| Cohorte de validación Need | Conjunto pre-Z sobre el que se evalúa la capacidad de adjudicar Need desde evidencia observable | Su objetivo es evaluar clasificación Need; requiere soporte 1 y 0 para métricas binarias |
| P*_{τ2} | Población causal primaria candidata para C1 ITT D2 | Se define por sus condiciones constitutivas, C_dep,0 y A_f,0*; Need no es criterio de pertenencia |
| P*_F | Subpoblación secundaria de apertura funcional exclusiva | Subconjunto de P*_{τ2} según F_alt,0; Need no es criterio de pertenencia |
| Población/denominador de cada ITT | Población y resultado concretos de cada variante × outcome/dimensión × horizonte | Se rige por C1 y los contratos de resultado; no por soporte de clases Need |
| Subconjunto truth binaria | Unidades de la cohorte Need con truth válida 1 o 0 | Denominador de métricas binarias de clasificación; truth=? se informa aparte |

Estos conjuntos no se presumen idénticos ni intercambiables.

## 4. Regla de alcance propuesta para la validación Need

La cohorte de validación Need debe definirse ex ante a partir del roster DGP B1/UE, antes de Z, con identidad y binding válidos, y sin seleccionarla por el valor de Need, por Z, por tratamiento recibido, por elegibilidad P*, por accesibilidad o por resultados posteriores.

**Alcance aceptado por DEC-C10-096, sujeto todavía a aprobación del roster material:** usar como cohorte el censo de todas las UE del roster DGP/paquete B1 aprobado al que aplique el paquete Need, sin subcohorte ni selección por Need; evaluar el soporte 1/0 sobre ese marco completo. La pertenencia se resuelve por identidad/binding y versión del roster antes de truth, evidencia y Z. Si los rosters A/B permanecen separados, se toma el roster exacto del paquete B1; no se presupone un roster conjunto. Si falta una clase, el diseño queda bloqueado, sin reparación post hoc. El flujo debe distinguir explícitamente:
- unidades roster elegibles para el paquete por identidad/binding;
- unidades con estipulación truth íntegra 1/0/?;
- unidades bloqueadas por defectos de integridad/materialización;
- unidades con evidencia observacional disponible, parcial o ausente;
- unidades con adjudicación E1/E2/Analyzer sellada;
- unidades que contribuyen a métricas binarias (truth 1/0) y unidades truth=? reportadas separadamente.

La pertenencia a la cohorte no debe depender de que el expediente observable sea completo o de que el adjudicador alcance un resultado determinado: hacerlo produciría selección por observabilidad/adjudicación y podría ocultar fallos del propio procedimiento. Los defectos de identidad o integridad se registran como bloqueos y permanecen visibles en el flujo; no se recodifican como truth=? ni se eliminan silenciosamente.

Esta propuesta no afirma que el roster actual exista ni que esté aprobado. Tampoco fija si el marco DGP de B1 coincidirá finalmente con el roster experimental completo; esa relación debe resolverse al aprobar el roster y el contrato de población.

## 5. Consecuencias para P*_{τ2}, P*_F e ITT

1. **No filtrar C1 por Need.** Ni truth=1, ni truth=0, ni truth=? determinan por sí solos inclusión o exclusión de P*_{τ2}.
2. **No exigir soporte Need 1/0 dentro de cada brazo Z.** La truth se fija en t−1; la validación Need no estratifica ni altera la asignación experimental.
3. **No exigir soporte Need 1/0 en P*_{τ2} como requisito automático de identificación de C1.** C1 es ITT de política D2 sobre los resultados/dimensiones y horizonte especificados; Need no forma parte de la definición aceptada de P*_{τ2}.
4. **No exigir soporte Need 1/0 en P*_F.** P*_F es un subobjetivo causal definido por rutas alternativas; no es una cohorte de validación de Need.
5. Si un análisis futuro plantea heterogeneidad del ITT por Need o un efecto de Value condicionado a Need, ese será un análisis adicional: requiere estimando, población, soporte, medición y tratamiento de truth=? especificados ex ante. No se deriva de este contrato.
6. Si la generalización del rendimiento del adjudicador Need a P*_{τ2} fuese un objetivo científico explícito, se deberá informar el soporte 1/0 y la cobertura dentro de P*_{τ2}; si falta, se limitará esa afirmación. Esto no autoriza reequilibrar, alterar etiquetas ni cambiar P*.

El ITT continúa en la población pre-Z asignada que defina el contrato C1, sin condicionamiento por Request_event, recepción, admisión, procesamiento, instalación, accesibilidad post-Z, selección, ejecución, Outcome o Value.

## 6. Tratamiento de truth=? y de ausencia

La cohorte Need conserva las unidades truth=? y las incidencias de observación/integridad en flujos separados:
- truth=? es indeterminación semántica explícita de la estipulación;
- observed=? puede reflejar insuficiencia, ambigüedad, conflicto o cobertura incompleta conforme al protocolo;
- MISSING/NONE/PARTIAL son estados de disponibilidad/cobertura, no etiquetas truth;
- integridad inválida bloquea el registro, no crea una clase adicional de truth.

Las métricas binarias se limitan a truth=1/0 y deben acompañarse de denominadores, cobertura y flujo de exclusiones/bloqueos. Los casos truth=? se describen por separado. No se afirma representatividad de la métrica binaria respecto del roster, P* o Value sin una justificación adicional.

## 7. Gates de cierre pendientes

Antes de aprobar este crosswalk se requiere:

1. recuperar y fijar el alcance del roster DGP B1/UE y su relación con la población experimental, sin inventar unidades;
2. el objetivo de validación Need queda delimitado a adjudicación E1/E2 por el crosswalk Generator/Analyzer/Evaluator existente; Analyzer PE no se convierte en clasificador Need. Definir los denominadores E1/E2;
3. decidir si la cohorte de validación es el roster B1 completo aplicable o una subcohorte pre-Z justificada; DEC-C10-095 exige que cualquier subcohorte tenga regla aprobada independiente de Need, Z, observabilidad y resultado, y que el soporte 1/0 se compruebe sin reparación post hoc;
4. cruzar los denominadores con C1 y las variantes A/B sin alterar P*_{τ2}/P*_F;
5. reconciliar las reglas de exclusión/bloqueo con el paquete de seis artefactos, el protocolo E1/E2 y las pruebas PKG/PREZ ya existentes;
6. especificar cómo se reportará rendimiento Need fuera del soporte observado, incluyendo límites de generalización;
7. mantener abiertos el soporte de q_X*, la positividad D2, la asignación y la interferencia; el soporte de clases Need no los demuestra.
8. mantener la evaluación PE del Analyzer separada, contra oráculos DGP por constructo/estimando; no usar el consenso E1/E2 como verdad de referencia ni inyectar las adjudicaciones en Analyzer por defecto.

No se requiere volver a decidir la precedencia P*_{τ2}/P*_F ni crear una nueva matriz de población.

## 8. Dictamen

**NO CONFLATION: NEED-VALIDATION COHORT ≠ P*_{τ2} ≠ P*_F ≠ ITT DENOMINATOR.**

El soporte truth 1/0 propuesto en el documento de composición es un requisito para evaluar la clasificación del constructo Need en su propia cohorte de validación. No es una condición de elegibilidad causal ni prueba positividad/soporte para D2, q_X*, C1, C3 o C4. La recomendación es definir la cohorte como censo del roster DGP/paquete B1 aprobado, sin selección por Need, Z, observabilidad o resultados, y conservar un flujo transparente de bloqueos y estados indeterminados. La evaluación de Need se limita a E1/E2; Analyzer PE mantiene su evaluación separada.

Este crosswalk incorpora el alcance de cohorte aceptado por DEC-C10-096 y las reglas de composición/soporte de DEC-C10-095; no aprueba todavía el roster material ni autoriza materialización. No modifica DEC-C10S-C1-POPULATION-PRECEDENCE-001, P*_{τ2}, P*_F, estimandos, asignación, RMA, Evidence→Claim Matrix, STATUS ni main. No crea roster, truth, evidencia, cobertura, schema físico, fixtures o código. No ejecuta validadores, DGP, simulación, replay o análisis estadístico.

`scientific_execution=false`; `execution_authorized=false`.
