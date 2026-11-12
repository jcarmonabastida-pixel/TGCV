# C10-S — Crosswalk de interfaz B1/Need_preZ con PE Generator–Analyzer–Evaluator

**ID:** C10-S-B1-PREZ-PE-INTERFACE-CROSSWALK-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / PROPOSED_BOUNDARY / NOT_APPROVED / NOT_IMPLEMENTED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Hallazgo principal: hay dos tareas diferentes que no deben fusionarse

La recuperación del contrato PE integrado y del contrato del paquete B1/Need revela una ambigüedad que debe resolverse antes de especificar una interfaz:

- El **Analyzer PE de C10-S** reconstruye constructos, estima y emite dictámenes a partir de un bundle observable y de contratos/estimandos permitidos. Su salida es un resultado analítico estructurado por estimando/constructo, con estado, incertidumbre, supuestos, diagnósticos, cobertura y trazas. No recibe truth ni potenciales.
- La **adjudicación B1/Need_preZ E1/E2** determina, a partir de evidencia basal admisible, el estado observado `need_observed_state ∈ {1,0,?}` sobre el objetivo funcional de B1. Sus reglas y sus registros están definidos en el paquete B1/Need y son independientes entre evaluadores.

No hay en los contratos recuperados una decisión que convierta la clasificación de Need_preZ en una salida del Analyzer PE, ni un contrato que establezca que el Analyzer de reconstrucción causal deba clasificar Need. El hecho de que ambos consuman evidencia observable no los convierte en la misma tarea.

**Recomendación:** no añadir al Analyzer PE una tarea de clasificación Need ni medir su exactitud como clasificador Need. Mantener la adjudicación Need como tarea E1/E2 separada. El Analyzer PE podrá usar el contexto observable B1/Need únicamente si un contrato de análisis concreto lo requiere para un estimando, y siempre como dato observado permitido, nunca como truth ni como una etiqueta adjudicada que revele información no prevista.

Esta recomendación evita ampliar silenciosamente el alcance del Analyzer y evita que un objetivo de adjudicación basal sustituya la tarea científica central de C10-S: reconstrucción/estimación de constructos y recuperación de dictámenes causales bajo DGPs conocidos.

## 2. Contratos recuperados y precedencia

1. `C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md`, §§3–4: separa Generator, Proyector/Sealer, Analyzer, Evaluator/Adjudicator y Artifact/Provenance Store; define entradas/salidas del Analyzer PE.
2. `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`, §§3, 6–10: separa TRUTH_LEDGER, EVIDENCE_LEDGER, ADJUDICATION_LEDGER y EVALUATION_LEDGER; define E1/E2 y el firewall.
3. `C10_S_B1_PREZ_COHORT_SCOPE_AND_EVALUATION_DENOMINATORS_RECONCILIATION_DRAFT_001.md`, §4: distingue E1, E2, Analyzer y Evaluator, pero deja la tarea exacta del Analyzer y la ubicación de su salida pendientes.
4. `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, §16.80 y pasajes PE: Generator conserva truth/potenciales; Analyzer recibe observed_evidence y contratos permitidos; Evaluator accede a truth tras sellar la salida inmutable del Analyzer.

El contrato PE es el anclaje de la interfaz del Analyzer. El paquete B1/Need no puede reinterpretar unilateralmente esa interfaz.

## 3. Matriz de responsabilidades y objetos

| Rol/tarea | Entrada permitida | Salida | Verdad disponible | Ubicación lógica |
|---|---|---|---|---|
| Generator B1/DGP | Especificación DGP, roster aprobado, reglas/versión | Truth Need_preZ y registros/eventos que alimentan observación | Sí, truth reservada | TRUTH_LEDGER + PACKAGE_MANIFEST restringido |
| Proyector/Sealer | Registros generados y contrato de observación | Bundle observable B1 y evidencia sellada | No debe exportarla | EVIDENCE_LEDGER / proyección PE observada |
| Adjudicador E1 | Evidencia B1 pre-Z, regla pública, binding y cobertura permitidos | `need_observed_state`, rationale, referencias, cobertura y digest | No | ADJUDICATION_LEDGER |
| Adjudicador E2 | Igual que E1, sin salida de E1 | Salida independiente equivalente | No | ADJUDICATION_LEDGER |
| Analyzer PE | Bundle observado completo permitido, contratos/estimandos y documentación visible simétrica | Resultado analítico estructurado por constructo/estimando, estado/dictamen, incertidumbre, supuestos, diagnósticos, cobertura, trazas y digest | No | Objeto de salida PE existente / Artifact-Provenance Store |
| Evaluator PE | Truth DGP restringida, salida Analyzer PE sellada y contrato de evaluación | Recuperación/error/abstención por estimando, diagnósticos y evaluación | Sí, después del sellado | Evaluator assessments / registros PE de evaluación |
| Evaluator B1/Need | Truth Need reservada y salidas E1/E2 selladas | Comparación por adjudicador, errores/indeterminación y cobertura | Sí, después del sellado | EVALUATION_LEDGER del paquete B1/Need |

La tabla expresa roles lógicos; no demuestra aislamiento técnico implementado. La segregación de metadatos, IDs, nombres de escenarios, orden, semillas, logs, errores, exports, APIs y canales laterales continúa siendo un gate PE.

## 4. Consecuencia para la cohorte y los denominadores B1/Need

La cohorte censo del roster B1 propuesta en el crosswalk anterior valida el procedimiento de adjudicación Need E1/E2 y la calidad del modelo de observación, no convierte automáticamente a la cohorte en un benchmark de clasificación del Analyzer PE.

Por tanto:

- El soporte truth=1 y truth=0 del paquete Need es requisito para evaluar la clasificación observada E1/E2 y el modelo de observación en el ámbito que corresponda.
- No se impone ese soporte como requisito del Analyzer PE ni se interpreta como soporte causal/positividad de C1/C2.
- La concordancia E1–E2 es fiabilidad interevaluador; la comparación individual E1/Truth y E2/Truth es validez frente al oráculo DGP.
- La exactitud causal del Analyzer PE se evalúa con sus propios outputs estructurados y oráculos por estimando/constructo del DGP, no con `need_observed_state` salvo que un contrato específico lo establezca expresamente.
- No se permite entrenar, ajustar o seleccionar el Analyzer con TRUTH_LEDGER, salidas E1/E2 ni resultados truth-versus-observed de la misma cohorte de evaluación. Si en el futuro se necesita calibración, requerirá diseño de entrenamiento/calibración separado y preespecificado, no incluido aquí.

## 5. Contrato de intercambio mínimo

### 5.1 Generator → Proyector/Sealer

- Mantener `truth_dgp`/Need_truth y potenciales en el ámbito restringido.
- Producir por separado eventos/estados/fuentes observables a través del modelo de observación.
- No codificar truth en IDs, orden, nombres, timestamps, semillas visibles, errores ni metadatos laterales.
- No usar Z ni variables post-Z para estipular Need_preZ o alterar evidencia pre-Z ya generada.

### 5.2 Proyector/Sealer → E1/E2

- Entregar evidencia B1 pre-Z, identidad/binding no sensible, reglas públicas de adjudicación, referencias de provenance y cobertura/limitaciones.
- Excluir truth, truth_basis_ref, claves/semillas, nombres de escenario y cualquier campo que permita reconstruir la etiqueta.
- Aplicar exactamente las restricciones de evidencia afirmativa para observed=1/0; mantener ? cuando proceda.

### 5.3 Proyector/Sealer → Analyzer PE

- Entregar el bundle observado autorizado por el contrato PE y el contrato del estimando.
- No añadir una columna `need_truth_state`, referencia reservada, clase de truth, etiqueta E1/E2 o metadato que permita reconstruirlos.
- La inclusión de Need observada solo se permite si el contrato del estimando la declara como entrada necesaria, con semántica y momento explícitos; la adjudicación E1/E2 no se inyecta por defecto.

### 5.4 E1/E2 y Analyzer → Evaluator

- Cada adjudicación E1/E2 se sella por separado con identidad de evaluador, versión de regla, evidencia revisada, rationale, cobertura, tiempo y digest.
- Analyzer PE sella su resultado estructurado con versión, configuración permitida, estimando, población/unidad, entradas exactas, estimación/clasificación, incertidumbre, supuestos, dictamen, diagnósticos, cobertura, limitaciones y digest.
- Evaluator abre truth solo tras verificar los sellos. Evalúa E1, E2 y Analyzer por separado, cada uno contra su propio contrato/oráculo. No reemplaza outputs por consenso ni modifica resultados sellados.

## 6. Ubicación de salida y no creación de artefactos

Se mantiene la arquitectura de seis artefactos lógicos B1/Need, sin séptimo ledger:

- E1/E2 y sus referencias de evidencia permanecen en `ADJUDICATION_LEDGER`.
- La comparación de E1/E2 con Need_truth permanece en `EVALUATION_LEDGER`.
- El output general del Analyzer PE permanece en el objeto de salida PE ya previsto por el contrato PE y en el Artifact/Provenance Store; no se duplica como una nueva entidad del paquete Need.
- Si una evaluación PE necesita referenciar el run/output en el paquete B1, `PACKAGE_MANIFEST` o `EVALUATION_LEDGER` podrá contener una referencia externa tipada (run ID + digest + contrato/versión), no el payload duplicado. La elección de campo exacto se difiere al mapping físico y no se inventa aquí.
- `EVALUATION_LEDGER` no se convierte en almacén de outputs analíticos primarios; conserva comparaciones y métricas con referencia al output sellado.

## 7. Contrato de abstención y estados de salida: no homogeneizar dominios

Se deben mantener dominios diferentes:

**Adjudicación Need E1/E2**
- `need_observed_state ∈ {1,0,?}`.
- `?` representa indeterminación observacional/semántica conforme a reglas; motivos y cobertura se registran.
- Ausencia de evidencia, cobertura insuficiente, conflicto o ambigüedad no se recodifican como 0.

**Analyzer PE**
- Emite estimación/estado por estimando y dictamen conforme al contrato PE: identificado, no identificado, indeterminado o efecto de paquete, según corresponda.
- La abstención analítica no equivale a `need_observed_state=?`.
- Un fallo de ejecución/schema o ausencia de output no equivale a abstención científica; se registra como error/ausencia técnica.
- No se traduce automáticamente un dictamen PE a la escala 1/0/? de Need.

**Evaluator**
- Distingue error de clasificación, abstención científicamente correcta, output no evaluable, ausencia/fallo técnico y fallo de integridad.
- No recompensa una abstención como acierto binario ni la penaliza como error binario sin regla explícita; informa cobertura y rendimiento condicional por separado.

## 8. Gates y decisión pendiente

1. Aceptar o rechazar la recomendación de mantener Need como adjudicación E1/E2 y no como tarea nativa del Analyzer PE.
2. Si se propone que Analyzer clasifique Need, redactar un contrato de tarea adicional explícito: objetivo, entradas, semántica, salida, abstención, entrenamiento/calibración, oráculo y evaluación. No asumir que existe por el contrato PE actual.
3. Aprobar roster B1 y representación del paquete analítico.
4. Resolver mapping externo de outputs PE al manifiesto/provenance/evaluation sin duplicación.
5. Cerrar reglas de adjudicación y observación, suficiencia estadística y gates P177/P178/P179/P182/P183.
6. Verificar técnicamente firewall Generator/Proyector/Analyzer/Evaluator antes de implementación/ejecución.

## 9. Dictamen

**RECOMENDACIÓN:** mantener dos validaciones separadas: (A) adjudicación B1/Need E1/E2 contra Need_truth; (B) recuperación del Analyzer PE contra oráculos DGP por constructo/estimando. No atribuir al Analyzer una tarea de clasificación Need no especificada. No crear un séptimo artefacto ni alterar U_G, RMA, Evidence→Claim Matrix, STATUS, P*, ITT, D2 o el contrato PE.

Documento documental propuesto, no decisión aceptada ni interfaz congelada. No se materializan datos, outputs, fixtures, schema físico, APIs, código ni permisos. No se ejecutan validadores, DGP, simulación, replay ni análisis.

`scientific_execution=false`; `execution_authorized=false`.



## 10. Alineación con el canal S7 y preservación de la frontera de tareas

La estructura lógica de estados del canal S7 queda descrita en §14 de C10_S_B1_PREZ_OBSERVATION_MECHANISM_AND_COVERAGE_RULES_RECONCILIATION_DRAFT_001.md. Se mantiene la frontera ya establecida en §§1–9 de este crosswalk:

- E1/E2 adjudican Need_preZ a partir del expediente observable autorizado y producen sus propios need_observed_state.
- El Analyzer PE no es un tercer adjudicador Need ni recibe los estados internos del canal o la truth.
- El Evaluator B1 abre TRUTH_LEDGER solo después del sellado de E1/E2.
- El Evaluator PE evalúa el Analyzer contra sus propios oráculos por constructo/estimando y solo después del sellado PE.

La separación lógica entre emisión, contenido, captura, admisibilidad y cobertura no crea una tarea adicional ni un nuevo output PE. La inclusión de observaciones B1/Need en el bundle PE sigue condicionada a que un estimando la requiera expresamente, conforme al crosswalk de bundle; no se inyectan E1/E2 ni su consenso por defecto.

No se crean artefactos, test IDs ni autorizaciones. Esta alineación documental no resuelve los gates estadísticos ni técnicos.
