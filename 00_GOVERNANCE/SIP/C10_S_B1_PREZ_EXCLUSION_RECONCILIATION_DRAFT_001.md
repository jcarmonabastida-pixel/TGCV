# C10-S — Reconciliación de la exclusión focal Need_preZ con el paquete analítico y el DGP temporal

**ID:** C10-S-B1-PREZ-EXCLUSION-RECONCILIATION-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** USER_ACCEPTED_DESIGN_CHOICE / DOCUMENTARY_RECONCILIATION / CONTRACTS_NOT_FROZEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Decisión de diseño aceptada e incorporada

El usuario acepta la recomendación de adoptar la **exclusión focal explícita como mecanismo mínimo suficiente y único requerido para estipular Need_preZ=0 en la truth reservada del DGP**. La enumeración exhaustiva de todos los objetivos B1–servicio no será requisito del generador.

La afirmación focal se refiere exclusivamente al objetivo funcional Need_preZ ya definido, respecto de la relación versionada B1–UE–instancia lógica de servicio en t−1. No convierte el servicio en sujeto de la necesidad ni confunde B1, UE e instancia de servicio.

La aceptación resuelve la elección conceptual entre las dos vías de truth=0; no equivale a aprobar íntegramente los contratos, congelar el diseño, seleccionar prevalencias, autorizar materialización ni autorizar ejecución.

## 2. Contratos reconciliados

Se revisaron en la rama de investigación:
- `C10_S_B1_PREZ_EXCLUSION_MECHANISM_REVIEW_DRAFT_001.md`.
- `C10_S_B1_PREZ_EXCLUSION_SCOPE_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_PREZ_DGP_U_G_COMPATIBILITY_AUDIT_DRAFT_001.md`.
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_REQUESTING_ENTITY_CANDIDATE_SPEC_DRAFT_001.md`.
- `C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md`.

La reconciliación es documental. No modifica retroactivamente el contenido ni el estado de aprobación de esos contratos.

## 3. Regla semántica consolidada de truth

Se mantiene sin cambios la definición funcional focal Need_preZ del contrato de adjudicación B1. Para cada B1/UE con identidad y binding válidos, la estipulación basal reservada del generador adopta uno de estos significados:

| Estipulación reservada | Truth | Regla |
|---|---:|---|
| Inclusión focal explícita | 1 | El objetivo funcional Need_preZ pertenece a los objetivos basales de B1 en t−1 |
| Exclusión focal explícita | 0 | El objetivo funcional Need_preZ no pertenece a los objetivos basales de B1 respecto del servicio vinculado en t−1 |
| Indeterminación semántica explícita | ? | La propia estipulación válida no determina pertenencia ni exclusión |

La exclusión focal explícita es la única vía mínima requerida para truth=0. No se exige catálogo completo de objetivos ni enumeración exhaustiva. Un eventual documento de enumeración completa podría ser una fuente observable si satisface su contrato, pero no constituye una segunda vía generadora necesaria.

### 3.1 No son estados de truth

No asignan truth=0 ni truth=?:
- ausencia de campo, registro, fuente o declaración;
- lista vacía, registro no materializado o fallo de escritura;
- falta de petición, intento, recepción, admisión, procesamiento o respuesta;
- falta de instalación, habilitación, disponibilidad, capacidad o accesibilidad;
- ausencia de déficit o interrupción;
- identidad, versión, vínculo B1–UE–servicio o integridad irresueltos.

Los defectos de integridad, identidad o versionado bloquean el caso. La ausencia observacional se refleja en observed=?, no cambia la truth reservada.

## 4. Mapeo al paquete analítico existente — sin nuevos artefactos lógicos

La estipulación focal se integra en los seis artefactos lógicos ya propuestos en el contrato del paquete. No se añade una séptima entidad ni una nueva clase U_G.

| Artefacto existente | Uso reconciliado |
|---|---|
| `PACKAGE_MANIFEST` | Referencia versiones/hashes de definición funcional Need, regla de estipulación, DGP y paquete |
| `UNIT_BINDING` | Resuelve UE↔B1↔contrato/instancia de servicio y `baseline_record_id`; no codifica por sí mismo la truth |
| `TRUTH_LEDGER` | Conserva `need_truth_state`, `truth_rule_id/version`, `truth_basis_ref`, tiempo basal, sellos y digest. `truth_basis_ref` apunta a la estipulación reservada de inclusión/exclusión/indeterminación, no a una fuente observada |
| `EVIDENCE_LEDGER` | Contiene fuentes generadas por el modelo de observación; nunca la etiqueta truth, la referencia reservada ni metadatos que permitan reconstruirla |
| `ADJUDICATION_LEDGER` | Conserva E1/E2 y sus salidas observed independientes, rationale, fuentes y cobertura; no consulta TRUTH_LEDGER |
| `EVALUATION_LEDGER` | Compara truth y observed después del sellado de las adjudicaciones |

La estipulación focal es el significado de `truth_basis_ref`; no se propone añadir `objective_catalog`, `objective_universe`, una tabla de objetivos, un campo de enumeración exhaustiva ni una clase de grafo.

Los nombres/campos ya descritos en el contrato del paquete siguen siendo una propuesta lógica, no un schema físico aprobado.

## 5. Crosswalk temporal y de roles

No se introduce un nuevo instante causal. La estipulación y la truth Need_preZ se fijan en t−1, en el mismo baseline que las demás condiciones basales; Z se asigna en t0. El objetivo no se redefine ni se reescribe después de Z.

| Objeto | Tiempo | Generador | Analyzer / E1-E2 | Evaluador |
|---|---|---|---|---|
| Especificación basal focal reservada y `need_truth_state` | t−1, sellada antes de Z | Crear y sellar | Sin acceso | Acceso solo después del sellado observed |
| Fuente(s) observacional(es) pre-Z | Contenido/evento pre-Z; captura con timestamp propio | Generar según modelo de observación separado | Acceso al subconjunto permitido | Acceso para auditoría tras sellos conforme a protocolo |
| `need_observed_state` y rationale E1/E2 | Adjudicación posterior sobre expediente pre-Z | No clasifica | Cada rol adjudica de forma independiente y sella | No interviene antes del sellado |
| Comparación truth–observed | Después del sellado de E1/E2 | No reescribe | Sin acceso a truth durante adjudicación | Compara y evalúa |

La tabla amplía el diccionario variable×tiempo×rol del contrato temporal a efectos de Need_preZ; no altera la secuencia t−1/t0 ni la cadena causal-transformacional.

## 6. Frontera entre truth=0 y observed=0

La decisión aceptada resuelve solo la forma de crear truth=0. No rebaja el umbral de evidencia de observed=0.

- **Truth=0:** el generador conserva una afirmación focal explícita de no pertenencia en la estipulación reservada.
- **Observed=0:** E1/E2 requieren evidencia observable afirmativa, pre-Z, semánticamente pertinente, admisible, vinculada a la B1/UE/servicio y con autoridad, alcance, integridad y cobertura suficiente conforme al contrato de adjudicación.

La fuente observable no es el registro reservado ni una copia de su etiqueta. La cobertura no se infiere de que el generador conozca la truth. Si no hay evidencia afirmativa o no se demuestra cobertura suficiente, observed=? aunque truth=0.

La exclusión focal explícita puede inspirar el contenido de una fuente sintética negativa, pero el modelo de observación debe generarla separadamente y especificar su autoridad, visibilidad, posible error y cobertura. No se ha elegido aún tipo concreto de fuente.

## 7. Compatibilidad con U_G y Evidence→Claim Matrix

Se conserva el dictamen de compatibilidad:
- no ampliar DEC-C10-061 ni sus seis destinos tipados;
- no forzar Need_preZ en PREDICATE ni usar COVERAGE_SCOPE como identidad de B1;
- reutilizar provenance/EVIDENCE_REGISTER solo donde el esquema lo permita, sin asumir que los targets E1/E2 actuales admiten B1/UE/Need;
- mantener el paquete analítico B1/Need separado de U_G, versionado y con referencias/hash de evidencia;
- no crear claim C17 ni modificar Evidence→Claim Matrix v1.47: Need_preZ es una variable del diseño C10-S, no una nueva afirmación teórica TGCV.

La aceptación de la regla de exclusión no resuelve ni reabre el gap de target U_G; la representación separada sigue siendo la opción documental de menor impacto pendiente de su cierre de gobernanza.

## 8. Gates que permanecen abiertos

1. **Contrato de estipulación:** integrar formalmente esta regla en el contrato de objetivo basal y resolver su crosswalk con el paquete, sin cambiar campos lógicos por duplicación.
2. **Representación lógica/física y permisos:** cerrar la ubicación y el control técnico de TRUTH_LEDGER, export observable y sellos; ningún secreto en GitHub.
3. **Composición de estados:** definir el mecanismo de generación de 1/0/? y soporte de ambas clases 1 y 0 para evaluación binaria, sin prevalencias, proporciones, estratos, parámetros o semilla inventados.
4. **Modelo de observación:** especificar tipos de fuente, autoridad, emisión/omisión, falsos positivos/negativos, ambigüedad, conflicto, corrupción, temporalidad, pérdida y cobertura, sin fijar tasas arbitrarias.
5. **Diccionario y pruebas:** incorporar Need al diccionario variable×tiempo×rol y convertir PKG-01…14 / PREZ-T01…10 en pruebas verificables, sin afirmar que están ejecutadas.
6. **Revisión integral:** comprobar coherencia con el DGP maestro y con la población/estimandos antes de cualquier autorización de materialización.

## 9. Estado y límites

**USER ACCEPTED: EXPLICIT FOCAL EXCLUSION AS THE SOLE REQUIRED MINIMUM TRUTH=0 MECHANISM / EXHAUSTIVE OBJECTIVE ENUMERATION NOT REQUIRED.**

No se modifica main, RMA, Evidence→Claim Matrix, STATUS, DEC-C10-061, contratos congelados, población ni estimandos. No se crean unidades, roster, truth, fuentes, cobertura, IDs, fixtures, schema físico o código. No se ejecutan validadores, DGP, simulación ni replay.

`scientific_execution=false`; `execution_authorized=false`.
