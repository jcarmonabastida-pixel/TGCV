# C10-S — Reconciliación del modelo de observación B1/Need_preZ con el bundle observable PE

**ID:** C10-S-B1-PREZ-OBSERVATION-PE-BUNDLE-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / PE_BUNDLE_BOUNDARY_PROPOSED / COHORT_SCOPE_ACCEPTED_BY_DEC-C10-096 / OBSERVATION_OPERATIONAL_RULES_ACCEPTED_BY_DEC-C10-097 / PE_BUNDLE_MAPPING_NOT_APPROVED / NOT_IMPLEMENTED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Propósito y resultado

Este documento cierra la siguiente frontera documental: cómo se relaciona la evidencia sintética B1/Need_preZ con el bundle observable que recibe el Analyzer PE, sin fusionar tareas, filtrar truth ni duplicar ledgers.

La reconciliación de los contratos existentes y DEC-C10-096 conduce a cuatro conclusiones:

1. El modelo de observación B1/Need ya está definido en lo esencial en `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md` §6. No se crea otro modelo ni se vuelven a definir sus mecanismos.
2. El Analyzer PE recibe el bundle observable autorizado por el contrato PE y el estimando. El conjunto B1/Need no se añade automáticamente como entrada universal.
3. Cuando una variable o evidencia B1/Need sea necesaria para un estimando PE, se proyecta como dato observado con su semántica, tiempo, provenance, cobertura e incertidumbre; nunca como truth, truth_basis_ref ni adjudicación E1/E2 por defecto.
4. E1/E2 siguen siendo adjudicadores de Need observada. El Analyzer PE no se convierte en clasificador Need por el mero hecho de recibir una parte del bundle observable.

Este documento es un crosswalk de interfaces lógicas, no un schema físico ni autorización de ejecución.

## 2. Artefactos históricos y precedencia

Se reutilizan:

- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md` §§3–9: seis artefactos, campos mínimos de EVIDENCE_LEDGER, mecanismos de observación, adjudicación, cobertura y firewall.
- `C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md`: inventario documental; no se encontraron fuentes observadas por unidad, roster ni truth materializados. Los tipos candidatos no son fuentes disponibles.
- `C10_S_B1_PREZ_PE_GENERATOR_ANALYZER_EVALUATOR_INTERFACE_CROSSWALK_DRAFT_001.md`: separación de tareas Need E1/E2 y Analyzer PE; outputs separados.
- `C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md` §§3–4 y §5: interfaces Generator→Proyector/Sealer→Analyzer→Evaluator y Artifact/Provenance Store.
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`: reloj t−1/t0…, separación de truth/observed y roles.

La auditoría de fuentes sigue teniendo el estado `UNIT_LEVEL_PREZ_EVIDENCE_NOT_FOUND_IN_REVIEWED_ARTIFACTS / COVERAGE_NONE`. DEC-C10-096 acepta el censo del roster aplicable y la tarea E1/E2, pero no cambia ese estado. Las reglas operativas de emisión, captura, contenido, admisibilidad y cobertura han sido aceptadas como diseño de trabajo por DEC-C10-097 y se detallan en `C10_S_B1_PREZ_OBSERVATION_MECHANISM_AND_COVERAGE_RULES_RECONCILIATION_DRAFT_001.md`. El presente crosswalk sigue definiendo la proyección sintética, no afirma que exista evidencia.

## 3. Capas y objetos: no colapsar

| Capa | Objeto existente | Contenido | Consumidor |
|---|---|---|---|
| Verdad generadora | `TRUTH_LEDGER` | `need_truth_state`, regla/versión, base reservada y sellos | Generator; Evaluator después del sellado |
| Fuente sintética | `EVIDENCE_LEDGER` | Artefacto/contenido observado, clase, emisor/autoridad, tiempo, scope, disponibilidad, integridad y lineage | E1/E2; Proyector/Sealer; solo proyección autorizada al Analyzer |
| Cobertura | Manifest/alcances del `EVIDENCE_LEDGER` | Universo pertinente, fuentes esperadas/examinadas/válidas/excluidas/opacas, método y limitaciones | E1/E2; Analyzer cuando sea relevante al estimando |
| Adjudicación | `ADJUDICATION_LEDGER` | Resultados independientes E1/E2, rationale, referencias, cobertura y sellos | Evaluator tras sellado |
| Bundle PE observado | Proyección sellada de evidencia PE | Subconjunto autorizado y normalizado de observaciones, mediciones, versiones, provenance, ausencia e incertidumbre | Analyzer PE |
| Output PE | Objeto de salida PE existente / Artifact-Provenance Store | Estimación/dictamen por constructo/estimando, incertidumbre, supuestos, diagnósticos, cobertura y digest | Evaluator PE |
| Evaluación Need | `EVALUATION_LEDGER` del paquete B1 | Comparación de E1/E2 con truth Need | Evaluator B1 |
| Evaluación PE | Evaluator assessments PE existentes | Comparación del output PE con oráculo DGP por estimando/constructo | Evaluator PE |

No se crea un ledger adicional ni se copia el payload del output PE dentro del paquete Need. El manifiesto/artefacto PE puede referenciar el bundle y su digest conforme al contrato PE.

## 4. Tipos de fuente B1 y semántica admisible

Los tipos de fuente siguientes proceden del inventario existente. Son clases candidatas del modelo generador, no una declaración de que existan registros materiales ni un catálogo cerrado adicional.

| Clase/candidata | Afirmación que puede respaldar | Límite semántico |
|---|---|---|
| Declaración/objetivo operativo basal de B1 | Inclusión/exclusión focal del objetivo Need, si la fuente es autorizada, vigente, pre-Z y vinculada | Es la fuente más directamente alineada; no copiar truth como etiqueta |
| Requisito funcional/contrato de servicio específico de B1 | Función/objetivo que la B1 declara mantener mediante el servicio | Un contrato genérico de plantilla no prueba adopción por B1 |
| Binding B1–UE–instancia y registro de identidad | Identidad, cardinalidad y alcance del servicio | No demuestra Need |
| Configuración declarada, ENABLED/PROFILE, IAM/ACL | Estado técnico/configuracional declarado en el baseline | No demuestra por sí sola objetivo funcional |
| Snapshot e integridad basal | Estado/versionado del objeto capturado en t−1 | Integridad del snapshot no prueba la semántica del objetivo |
| Tickets, manuales, entrevistas o registros históricos | Contexto o declaración, según autoridad, fecha y vigencia | No convertir ausencia de solicitudes en Need=0; controlar retrospectividad |
| SBOM, lockfile, manifiesto, inventario | Identidad/dependencias del servicio | No demuestra objetivo de B1 |
| Logs, trazas, métricas, pruebas funcionales | Uso, operación, admisión, procesamiento o capacidad técnica | No prueban Need_preZ; si son post-Z no pueden retrotraerse como verdad basal |

La adjudicación observed=1/0 exige evidencia afirmativa que satisfaga las reglas existentes. El estado técnico puede ser contexto corroborativo, nunca sustituto de una fuente semánticamente alineada al objetivo basal.

## 5. Modelo de observación: separación generativa

El modelo de observación ya requiere mecanismos diferenciados para:
- emisión/ausencia de declaración;
- sensibilidad semántica;
- falsos positivos y falsos negativos;
- ambigüedad y conflicto;
- corrupción;
- error temporal;
- pérdida/captura;
- cobertura.

No se fijan probabilidades, tasas, distribuciones, prevalencias, dependencia ni parámetros. Esos valores necesitan un DGP completo y justificación posterior.

### 5.1 Dependencia permitida

La truth puede causar la probabilidad y el contenido de que se emita una declaración auténtica y semánticamente alineada. Esto es una relación del mecanismo de medición, no una copia de la etiqueta.

Las fuentes también pueden depender de covariables basales y de propiedades observables de la fuente —autoridad, canal, versión, custodio, clase documental— cuando esas dependencias se especifiquen ex ante en el DGP.

No se presume independencia entre fuentes. La dependencia compartida por emisor, plantilla, canal, custodio o proceso de captura debe representarse si forma parte del DGP.

### 5.2 Restricciones temporales y causales

- Need_truth se estipula en t−1; Z ocurre en t0.
- La emisión/captura de evidencia usada para adjudicar Need debe referirse al estado/objetivo basal y su tiempo de evento debe ser pre-Z.
- Un documento capturado después de t0 solo puede usarse si el contrato demuestra que es una copia íntegra de un registro creado y fijado antes de Z; su tiempo de captura no sustituye al tiempo del evento.
- Z, política D2, provisión, instalación, C_dep, accesibilidad, Reach, trayectoria, petición, admisión, ejecución, Outcome y Value no determinan Need_truth ni alteran retrospectivamente la evidencia basal.
- La observabilidad puede depender de características basales preespecificadas, pero no de variables post-Z ni de resultados.
- No introducir una asociación artificial entre truth y Z por el orden de generación, el roster, la semilla compartida, el orden de registros o la codificación de IDs.

### 5.3 No codificación indirecta de truth

Además de excluir `need_truth_state` y `truth_basis_ref`, el Generator/Proyector debe evitar que truth se reconstruya trivialmente mediante:
- IDs, prefijos, orden de unidades o de fuentes;
- nombres de escenario, rutas, filenames, clases de fixture o etiquetas de ejecución;
- timestamps, secuencias, tamaños de payload o campos opcionales;
- semillas, claves, logs, errores, contadores, metadata de cobertura o patrones de ausencia;
- diferencias de schema o versiones asociadas exclusivamente a una clase.

La auditoría de filtraciones debe examinar también correlaciones indirectas, no solo nombres de campos. Un canal que permita predecir truth por construcción constituye fuga aunque no exponga la etiqueta literal.

## 6. Proyección al bundle PE

El Proyector/Sealer no entrega el EVIDENCE_LEDGER bruto completo por defecto. Construye el bundle PE desde los registros observados autorizados por el contrato de análisis y por estimando.

Cada elemento proyectado conserva, cuando resulte pertinente:
- referencia exacta al registro fuente y digest;
- identidad/unidad/versión no sensible;
- semántica de la observación y constructo al que se refiere;
- event_time y capture_time separados;
- método, autoridad y provenance;
- disponibilidad/ausencia, cobertura y limitaciones;
- estado de validez e incertidumbre de medición;
- transformación de proyección y versión del contrato.

No se proyectan:
- truth, truth_basis_ref, potenciales ni parámetros estructurales reservados;
- claves/semillas secretas o metadatos que reconstruyan el escenario;
- salidas E1/E2 o racionales de adjudicación Need por defecto;
- campos de evaluación que comparen observed con truth;
- artefactos que no sean necesarios para el estimando y cuya presencia amplíe el riesgo de fuga.

Si un estimando requiere una variable Need observada o evidencia B1, el contrato del estimando debe identificarla expresamente, definir su semántica/tiempo, reglas de ausencia y rol analítico. La entrada será la observación/proyección permitida, no la truth ni el resultado adjudicado E1/E2 por defecto. No se incorpora Need solo porque esté disponible en el paquete.

## 7. Separación de outputs y evaluación

### 7.1 E1/E2

E1 y E2 reciben el conjunto de evidencia B1 autorizado, regla pública, binding no sensible y cobertura. Emiten `need_observed_state ∈ {1,0,?}` y rationale. Se sellan individualmente antes de abrir truth.

### 7.2 Analyzer PE

Recibe el bundle observado PE conforme a los contratos/estimandos. Emite el resultado analítico estructurado. No emite `need_observed_state` a menos que se apruebe en el futuro un contrato explícito de tarea clasificadora separado.

### 7.3 Evaluators

- Evaluator B1 compara E1 y E2, por separado, con Need_truth y registra clasificación, indeterminación, cobertura y fiabilidad interevaluador.
- Evaluator PE compara el output PE con los oráculos DGP por constructo/estimando.
- Ningún Evaluator reemplaza los outputs originales por consenso ni abre truth antes del sellado.
- Un resultado de adjudicación B1 puede ser referencia contextual para análisis solo si el estimando lo especifica y si la información se libera simétricamente y sin revelar truth. No se habilita como feature de entrenamiento/calibración del Analyzer sobre el mismo conjunto confirmatorio.

## 8. Casos adversariales que el diseño debe conservar

Sin crear nuevas familias de pruebas ni asignar IDs nuevos, el mapeo debe poder representar los mecanismos adversariales ya incluidos en el registro de tests:

- truth=1 sin declaración emitida o con declaración perdida;
- truth=0 con documento positivo falso o declaración espuria;
- documento genuino pero ambiguo respecto al objetivo focal;
- fuentes contradictorias con autoridad/temporalidad diferentes;
- documento íntegro asociado a B1/UE/servicio incorrectos;
- registro válido capturado después de Z cuyo event_time sí es pre-Z;
- snapshot técnico íntegro que no acredita el objetivo de B1;
- fuentes múltiples dependientes de un mismo emisor/canal;
- cobertura PARTIAL/NONE u opacidad de una superficie pertinente;
- metadatos/IDs que filtran truth aunque no incluyan la etiqueta.

Estos casos prueban el contrato de observación y el firewall. No deben convertirse en prevalencias ni tasas de error sin diseño estadístico aprobado.

## 9. Gates pendientes antes de implementación

1. Aprobar la frontera propuesta y la inclusión condicional de campos Need observados en bundles PE.
2. Cerrar el catálogo de fuentes sintéticas realmente necesario para el microdominio y su mapeo al contrato funcional B1, sin promover clases candidatas a fuentes disponibles.
3. Completar el diccionario variable×tiempo×rol y el crosswalk exacto de campos de EVIDENCE_LEDGER al bundle PE.
4. Definir dependencias del modelo de observación y parámetros únicamente en el DGP maestro, con truth 1/0/? y fuentes separadas.
5. Resolver cómo se generan los casos de emisión, omisión, falsos positivos/negativos, ambigüedad, conflicto, pérdida y corrupción sin tasas arbitrarias.
6. Especificar pruebas del firewall para IDs, orden, timestamps, semillas, logs, exports, schema, metadata y canales laterales.
7. Confirmar que los contratos de test existentes cubren los casos adversariales; si falta alguno, documentar el gap antes de crear IDs.
8. Aprobar población/roster y suficiencia estadística antes de cualquier evaluación confirmatoria.
9. Obtener aprobación de implementación y autorización de ejecución por separado.

El alcance de cohorte y la frontera E1/E2 vs Analyzer PE quedan aceptados por DEC-C10-096. El modelo operativo de observación/cobertura está aceptado por DEC-C10-097; la aprobación de esta proyección PE sigue pendiente y no se considera aceptada por extensión.

## 10. Dictamen

**RECOMENDACIÓN:** mantener el modelo de observación B1 existente; proyectar al Analyzer PE solo observaciones necesarias y permitidas por estimando; no entregar truth ni adjudicaciones E1/E2 por defecto; mantener E1/E2 y Analyzer como tareas distintas. El bundle PE es una proyección controlada del conjunto de evidencia observado, no un duplicado del EVIDENCE_LEDGER.

Este documento no crea nuevos artefactos lógicos, entidades U_G, claims, decisiones, tests ni parámetros. No modifica RMA, Evidence→Claim Matrix, STATUS, P*, ITT, D2 ni el contrato PE. No materializa roster, truth, fuentes, bundles, salidas, fixtures, schema físico, APIs, permisos ni código.

`scientific_execution=false`; `execution_authorized=false`.



## 11. Incorporación de la estructura lógica S7 (referencia §14)

La estructura lógica de emisión/contenido/captura y sus estados no colapsables se especifica en §14 de C10_S_B1_PREZ_OBSERVATION_MECHANISM_AND_COVERAGE_RULES_RECONCILIATION_DRAFT_001.md. Este crosswalk la adopta como referencia conceptual para evitar que la proyección PE reduzca todo a availability_status.

El bundle PE, cuando un estimando justifique incluir alguna observación B1/Need, solo podrá recibir campos observables autorizados: contenido declarativo visible si fue emitido y capturado, estado de captura/ausencia pertinente, provenance/autoridad no sensible, integridad, tiempo, binding, alcance y cobertura. Nunca recibe el estado interno del canal, truth, truth_basis_ref, la regla reservada de composición, semillas reconstructivas o salidas E1/E2 por defecto.

La secuencia lógica no implica que todas las etapas sean variables independientes. El DGP podrá definir dependencias conjuntas, pero deberá declararlas explícitamente y evitar canales laterales. La enumeración EXPECTED de la oportunidad no equivale a emisión ni captura.

Esta referencia no aprueba la proyección PE pendiente ni incorpora Need automáticamente al bundle. La decisión de incluirlo sigue siendo específica del estimando. No se añaden artefactos, roles, variables causales ni pruebas.
