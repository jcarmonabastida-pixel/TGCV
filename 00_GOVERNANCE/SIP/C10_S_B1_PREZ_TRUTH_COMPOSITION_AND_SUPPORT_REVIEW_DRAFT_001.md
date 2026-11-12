# C10-S — Revisión del mecanismo de composición y soporte de truth Need_preZ

**ID:** C10-S-B1-PREZ-TRUTH-COMPOSITION-REVIEW-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_DESIGN_REVIEW / CORE_COMPOSITION_RULES_ACCEPTED_BY_DEC-C10-095 / REMAINING_GATES_OPEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Objeto y alcance

Este documento cierra parcialmente el gate de composición abierto en la reconciliación de exclusión focal. Especifica cómo debe entenderse la composición de `need_truth_state ∈ {1,0,?}`, qué soporte mínimo necesita la evaluación confirmatoria del Analyzer y qué no debe decidirse todavía.

Se apoya en:
- `C10_S_B1_PREZ_EXCLUSION_RECONCILIATION_DRAFT_001.md`;
- `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md`;
- `C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md`;
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`;
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`.

No sustituye estos contratos ni congela el DGP. DEC-C10-095 acepta configuración explícita versionada por B1/UE y mapping determinista; no define una distribución, prevalencia, proporción, tamaño muestral, estrato, parámetro, semilla ni roster.

## 2. Principio de composición: estipulación explícita por unidad, no imputación

La composición no se obtiene deduciendo Need de covariables, condiciones técnicas, solicitudes o resultados. Para cada B1/UE válida del roster que se apruebe, el Generator debe conservar una estipulación basal explícita, versionada y reservada del objetivo focal en t−1. La regla de derivación ya reconciliada traduce esa estipulación a:

| Estipulación basal reservada | `need_truth_state` |
|---|---:|
| Inclusión focal explícita del objetivo funcional | 1 |
| Exclusión focal explícita dentro del alcance focal cerrado | 0 |
| Indeterminación semántica explícita de la propia estipulación | ? |

La unidad de composición es la pareja B1/UE vinculada a la instancia lógica de servicio versionada. No se compone por solicitud, oportunidad, evento de servicio, trayectoria ni resultado.

La estipulación debe existir como contenido semántico válido; un valor ausente, null, lista vacía, documento no generado, fallo de escritura, referencia rota o binding inválido es un defecto de integridad/materialización y bloquea el registro. Nunca se convierte automáticamente en truth=0 o truth=?.

## 3. Soporte requerido y significado de “composición”

### 3.1 Soporte binario mínimo

La evaluación confirmatoria de la capacidad del Analyzer para distinguir inclusión de exclusión requiere soporte de ambos estados:
- al menos una unidad válida con truth=1;
- al menos una unidad válida con truth=0.

Este es un requisito lógico de soporte, no una propuesta de balance ni de prevalencia. La suficiencia estadística, precisión, potencia, número de unidades y estabilidad de métricas requieren el contrato estadístico/poblacional y no quedan resueltos por este mínimo.

El soporte debe comprobarse en la población o cohorte de validación del Analyzer que se defina ex ante. No se presume que esa cohorte sea idéntica a la población ITT, a una población de Value o a cualquier subpoblación analítica distinta. Sus denominadores y reglas de inclusión deben quedar explícitos antes de materializar.

### 3.2 No imponer soporte por brazo o estrato sin justificación

No se exige aquí presencia de ambos estados en cada brazo Z, estrato, combinación de covariables o escenario. Esa exigencia sería una decisión adicional de diseño que podría alterar la composición basal, la asignación o la población objetivo. Solo podrá imponerse si el contrato de población/estimandos o un plan de validación estratificada demuestra que es necesario y define su alcance ex ante.

La truth se estipula en t−1, antes de Z. El mecanismo de composición no consulta ni condiciona la estipulación a Z, a la política D2, a la asignación observada, al cumplimiento, a la instalación ni a ninguna variable post-Z. No se reequilibra el roster después de conocer Z.

Si la composición natural del roster aprobado no proporciona soporte 1 y 0 en la cohorte de validación, el resultado es **SUPPORT_FAILURE / DESIGN_BLOCKED**. No se crean unidades ad hoc, no se cambian etiquetas ni se altera el roster silenciosamente para conseguir una métrica calculable.

## 4. Tratamiento de truth=?

Truth=? se conserva exclusivamente cuando la estipulación generadora válida deja semánticamente indeterminada la pertenencia del objetivo. No es una tercera categoría de conveniencia para equilibrar el conjunto, simular missingness ni representar incertidumbre del Analyzer.

Regla de evaluación propuesta:
- Las métricas binarias de clasificación truth 1 frente a truth 0 se calculan únicamente sobre unidades con truth binaria válida (1 o 0), con sus denominadores y cobertura declarados.
- Las unidades truth=? no se recodifican como 0/1 y no entran en los denominadores de falsos positivos, falsos negativos, sensibilidad o especificidad binarias.
- Las unidades truth=? se informan por separado: número/cobertura de casos, distribución de observed E1/E2/Analyzer (1/0/?), discrepancias y razones de indeterminación cuando estén disponibles.
- No se afirma que el rendimiento binario observado en el subconjunto 1/0 caracterice automáticamente a toda la población si truth=? existe o si la selección de unidades binarias limita la generalización.
- La presencia de truth=? no autoriza excluir esas UE de ITT ni de otros análisis poblacionales. Need_preZ no es un filtro ITT; la elegibilidad de cada estimando se rige por su contrato propio.

La conveniencia de un análisis adicional de clasificación ternaria o de límites/sensibilidad para unidades truth=? queda OPEN; no se presume que exista una métrica única válida para ello.

## 5. Independencia, temporalidad y ausencia de circularidad

La composición debe satisfacer conjuntamente:

1. **Precedencia:** estipulación y truth fijadas y selladas en t−1, antes del evento Z en t0.
2. **No derivación causal/técnica:** no deducir truth de X/H/C/L, C_dep, A_f, T_acc, Reach, configuración CMP/PAR/REF/RUL, instalación, disponibilidad, capacidad, petición, recepción, admisión, procesamiento, ejecución, Outcome o Value.
3. **No dependencia de asignación:** no usar Z, brazo, política D2 ni variables de cumplimiento para generar, seleccionar o corregir truth.
4. **No filtración:** la estipulación, truth, truth_basis_ref, semillas y metadatos que permitan reconstruirla permanecen fuera del expediente visible para E1/E2 y Analyzer.
5. **Observación separada:** el modelo de observación puede producir evidencia condicionada por la estipulación verdadera, pero debe hacerlo mediante su propio mecanismo versionado; no copia la etiqueta ni crea un proxy transparente.
6. **Inmutabilidad:** cambiar Z o cualquier estado post-Z manteniendo el baseline estipulado debe dejar `need_truth_state` inalterado.

La independencia aquí es una restricción de generación/derivación, no una afirmación de independencia estadística de Need respecto de toda característica basal. Cualquier asociación estadística planificada debe justificarse y revisarse antes de freeze; no se introduce por conveniencia ni se infiere de proxies.

## 6. Procedimiento lógico propuesto (sin algoritmo ni parámetros)

El orden mínimo de diseño es:

1. Definir y aprobar el roster y la población/cohorte de validación, con identidades B1/UE/servicio válidas y cardinalidades ya aceptadas.
2. Para cada unidad, crear en el espacio reservado la estipulación explícita de inclusión, exclusión focal o indeterminación semántica; registrar regla, versión, alcance y ancla t−1.
3. Derivar `need_truth_state` exclusivamente de esa estipulación y sellar el registro reservado.
4. Comprobar integridad y soporte 1/0 en la cohorte de validación predefinida. La comprobación es un gate; no modifica la composición.
5. Generar por separado las fuentes observables mediante el modelo de observación que se especifique y apruebe posteriormente.
6. Sellar las salidas E1/E2/Analyzer antes de permitir al Evaluator abrir truth y calcular resultados.

DEC-C10-095 resuelve este punto: las estipulaciones se introducen como configuración explícita, versionada y reservada por B1/UE; una regla determinista las traduce a 1/0/?; no se usa un mecanismo estocástico para asignar Need en el núcleo confirmatorio. Esto no modifica ni sustituye la asignación aleatoria de Z. El modelo de observación puede contener mecanismos estocásticos propios, sujetos a especificación separada.

## 7. Gates y pruebas estáticas propuestas

Antes de materializar deberán poder verificarse, como mínimo:

- **TC-01 — Cardinalidad:** una estipulación válida por B1/UE/baseline/versión de paquete.
- **TC-02 — Dominio:** solo 1/0/? como estados válidos; los defectos de integridad se reportan como errores, no como estados truth.
- **TC-03 — Inclusión:** truth=1 requiere inclusión focal explícita.
- **TC-04 — Exclusión:** truth=0 requiere exclusión focal explícita y alcance cerrado.
- **TC-05 — Indeterminación:** truth=? requiere indeterminación semántica explícita.
- **TC-06 — Soporte:** la cohorte confirmatoria definida ex ante contiene ambos estados 1 y 0; de lo contrario, bloqueo sin reparación automática.
- **TC-07 — No postratamiento:** alterar Z y variables post-Z no altera la estipulación ni truth.
- **TC-08 — No derivación por proxy:** cambios aislados de covariables o configuración técnica no cambian truth por regla automática.
- **TC-09 — Cegamiento:** Analyzer/E1/E2 no pueden acceder a truth ni a metadatos reconstructivos.
- **TC-10 — Evaluación segregada:** truth=? se informa separadamente y no se imputa en métricas binarias.
- **TC-11 — Denominadores:** población ITT, cohorte de validación binaria y casos truth=? se reportan como conjuntos distintos cuando no coincidan.
- **TC-12 — Sellado:** la evaluación no abre truth antes del sellado de todas las adjudicaciones requeridas.

Son pruebas propuestas, no ejecutadas. Su mapeo final con PKG-01…14 y PREZ-T01…10 debe evitar duplicar pruebas existentes.

## 8. Decisiones que permanecen abiertas

| Cuestión | Estado |
|---|---|
| Mecanismo para producir estipulaciones por unidad | ACCEPTED BY DEC-C10-095: configuración explícita versionada; mapping determinista; no stochastic Need generator |
| Población y cohorte exacta de validación, denominadores y relación con ITT | OPEN |
| Alcance de cualquier soporte adicional por brazo/estrato | OPEN; no requerido por este mínimo |
| Inclusión o no de casos truth=? en el escenario confirmatorio y objetivo de generalización | OPEN |
| Métricas ternarias, límites o sensibilidad para truth=? | OPEN |
| Tamaño muestral, potencia/precisión y estabilidad por clase | OPEN |
| Dependencias estadísticas justificadas con características basales | OPEN |
| Modelo de observación, fuentes, tasas y cobertura | OPEN |
| Representación física, permisos, almacenamiento y sellado | OPEN |

## 9. Dictamen

**COMPOSITION RULE ACCEPTED BY DEC-C10-095 / EXPLICIT PER-UNIT CONFIGURATION + DETERMINISTIC MAPPING / BINARY SUPPORT GATE ACCEPTED / POPULATION AND ROSTER REMAIN OPEN.**

El cierre alcanzado evita tanto asignar Need=1 a todas las unidades como fabricar una prevalencia o balance arbitrario. Exige estipulaciones válidas y soporte real de ambas clases en la cohorte confirmatoria, pero convierte la falta de soporte en un bloqueo explícito, no en una licencia para sintetizar casos adicionales.

No se materializa roster, estipulación, truth, fuente, cobertura, ID, fixture, schema físico ni código. No se ejecutan validadores, DGP, simulación, replay o análisis estadístico. No se modifican main, RMA, Evidence→Claim Matrix, STATUS, población, estimandos ni contratos congelados.

`scientific_execution=false`; `execution_authorized=false`.
