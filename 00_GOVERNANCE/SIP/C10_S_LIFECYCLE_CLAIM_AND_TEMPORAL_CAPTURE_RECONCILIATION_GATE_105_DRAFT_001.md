# C10-S — Gate 105: reconciliación de claims de lifecycle y captura temporal

**Estado:** LIFECYCLE CONCEPTUAL DIMENSIONS RECOVERED / STRUCTURED CLAIM MODEL INCOMPLETE / STATE-AND-OCCURRENCE DISTINCTION REQUIRED / S3 CAPTURE SEMANTICS RECOVERED / CROSS-REGISTER CLOCK MAPPING OPEN / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Precedencia:** U_G Inventory Register Template §§2, 5, 12.1–12.9, 13, 18–19; U_G Evidence/Provenance/Adjudication Protocol §§1–13, 17–20; Gate 98 successor §§3–8; Gate 104 (corregido mediante este gate); Temporal Horizon and S4R Integration Audit §§11–18; DEC-C10-065/070/071/083/088. DEC-C10-061 permanece intacta.

---

## 1. Pregunta y dictamen ejecutivo

Resolver dos cuestiones que Gate 104 dejó abiertas:
1. ¿Los seis estados de lifecycle de NODE están representados por el modelo U_G existente, y cómo pueden observarse/adjudicarse sin confundir propiedades de estado con ocurrencias?
2. ¿El contrato existente distingue de forma suficiente event_time, emisión, captura/recepción, observed_at, recorded_at y SNAPSHOT.timestamp, con relojes comparables?

**Corrección de antecedente:** la lectura de Gate 104 omitió U_G Template §12.7, que sí enumera expresamente la extensión NODE «estado declarado/instalado/desplegado/cargado/invocado/ejecutado». Por tanto, no es correcto afirmar que la plantilla no contempla conceptualmente los seis estados. Sin embargo, §12.7 no los define como seis campos tipados ni aporta dominio, identidad de claim, temporalidad, evidencia requerida o reglas de evaluación por dimensión. El encabezado de NODE (§2) mantiene observed_state genérico y no desglosa esos seis atributos. La intención conceptual existe; la representación estructurada y ejecutable no está cerrada.

**Dictamen principal:**
- Los seis conceptos están expresamente previstos en §12.7; Gate 103 fue correcto al identificar su separación conceptual. Gate 104 debe quedar corregido.
- No se deben convertir los seis conceptos en seis booleanos/estados planos de NODE: no son todos propiedades homogéneas. Declarado/instalado/desplegado describen estados de configuración/ubicación del objeto en un scope; cargado/invocado/ejecutado pueden describir estados runtime o episodios temporales, con ventana y evidencia de observación.
- CLAIM_EVIDENCE_LINK permite varios claim_statement para un NODE, y EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER pueden apuntar al NODE, pero no proporcionan identidad tipada/versionada de cada claim ni una FK inequívoca claim-level para evaluaciones y adjudicaciones. No queda garantizada la evaluación separada de seis dimensiones sobre un mismo NODE.
- Los 14 predicados U_G existentes no incluyen una familia lifecycle; no se reutilizan ID/DEP/REL/AUTH por analogía ni se amplía su catálogo aquí.
- PROCESS_EVENT Gate 98 es candidato no aceptado; su catálogo actual tampoco incluye de forma general LOAD/INVOKE/EXECUTE runtime. No se fuerza esos actos dentro de tipos de provisión ni se crean eventos sin fuente/identidad.
- El protocolo S3 define métricas y modos que distinguen emisión, captura, pérdida, duplicación, desorden y timestamp, y define lag capture_time−event_time. Pero EVIDENCE_REGISTER solo tiene timestamp_start/end_tz genérico; no hay campos tipados separados para source_event_time, emission_time, capture_time ni clock metadata compartida. La definición metodológica está más avanzada que el mapping físico.
- No se ha demostrado un mapping universal entre capture_time, observed_at, EVIDENCE_REGISTER.timestamp_start/end_tz, PROCESS_EVENT.recorded_at y SNAPSHOT.timestamp. No son intercambiables.

**Resultado:** GATE_105_LIFECYCLE_CONCEPTS_PRESENT / CLAIM_LEVEL_STRUCTURE_INCOMPLETE / STATE_VS_OCCURRENCE_SEPARATION_REQUIRED / S3_CAPTURE_METHOD_DEFINED_BUT_FIELD_MAPPING_OPEN / CROSS_REGISTER_CLOCK_CONTRACT_INCOMPLETE / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.

## 2. Reconstrucción histórica y corrección de Gate 104

### 2.1. Fuente omitida

U_G Inventory Register Template §12.7, extensión NODE, dice expresamente:

> TID/SID/RID, boundary_class, estado declarado/instalado/desplegado/cargado/invocado/ejecutado, owner/boundary, consumers, dependencias.

La frase se encuentra dentro de la lista de extensiones de NODE. Por tanto:
- los seis conceptos no son una invención de Gate 103;
- la plantilla sí los contempla como intención de diseño;
- no se demuestra que estén ya formalizados como seis columnas/campos independientes.

El encabezado abreviado NODE de §2 contiene observed_state (1/0/?), timestamp, evidencia, cobertura y metadatos de revisión/snapshot, pero no seis campos lifecycle separados. §12.7 no especifica nombres físicos, tipos, cardinalidad, clave, obligatoriedad, temporalidad ni constraints para esos estados. §12.9 tampoco define un dominio lifecycle. §12.10 no presenta esos campos como una estructura desglosada.

### 2.2. Rectificación exacta

La afirmación de Gate 104 «la plantilla NODE no contiene seis estados de lifecycle explícitos» se corrige así:

**Redacción corregida:** «La plantilla U_G §12.7 enumera expresamente seis dimensiones conceptuales de lifecycle para NODE. No obstante, no están desglosadas ni especificadas como seis atributos tipados en el encabezado y diccionario normalizado, y carecen de contrato claim-level para identidad, tiempo, evidencia y adjudicación independiente».

La frase de Gate 104 que atribuía a Gate 103 haber sobreafirmado que NODE ya representaba los seis estados queda retirada. Gate 103 reconoció una extensión conceptual existente; lo que permanecía sin demostrar era su formalización estructurada y observabilidad. Gate 104 permanece histórico y se actualiza con esta rectificación, sin borrado de su historial Git.

## 3. Ontología de las seis dimensiones: no son seis estados equivalentes

| Dimensión | Naturaleza primaria | Afirmación que se intenta respaldar | Fuente pertinente candidata | Límite |
|---|---|---|---|---|
| DECLARED | Existencia/identidad declarada en contrato, manifiesto o paquete | El objeto/versión figura en la definición declarativa exacta | S1; S5/S7 como contexto | No acredita instalación ni presencia efectiva |
| INSTALLED | Estado material de instalación en unidad/entorno | El objeto/versión está instalado en el entorno y scope declarados | S1 inventario/paquete + S2; S4 según captura | Manifiesto o lockfile no basta por sí solo |
| DEPLOYED | Estado de despliegue/ubicación efectiva | El objeto/versión está desplegado en destino/scope concreto | S2 configuración efectiva + S4; S3 corroboración cuando proceda | Configuración deseada no demuestra despliegue efectivo |
| LOADED | Estado runtime de carga en proceso/instancia/ventana | El módulo/componente fue cargado en runtime identificado | S3 procesos/módulos/trazas; S4 como contexto | Observación puntual no acredita continuidad fuera de ventana |
| INVOKED | Ocurrencia de invocación | Hubo una llamada/uso concreto, con origen/destino y tiempo | S3 LOG_TRACE_EVENT; PROCESS_EVENT solo si tipo y contrato futuro lo permiten | Configuración de endpoint no prueba invocación |
| EXECUTED | Ocurrencia de ejecución efectiva | La operación/componente ejecutó una acción identificable | S3 traza/log/runtime + resultado/artefacto pertinente | Invocación no demuestra ejecución completada; ejecución no implica éxito funcional |

### 3.1. Consecuencias semánticas

1. DECLARED, INSTALLED y DEPLOYED pueden ser afirmaciones de estado relativas a una unidad, entorno, versión y captura/scope.
2. LOADED puede expresarse como estado runtime en una ventana o como transición/episodio de carga; la modalidad debe fijarse por fuente y pregunta.
3. INVOKED y EXECUTED son, en su forma más fuerte, ocurrencias/eventos, no estados persistentes del NODE. Deben tener tiempo/ventana, actor/emisor, contexto y evidencia de ocurrencia.
4. Los seis conceptos no forman una cadena determinista. DECLARED no implica INSTALLED; INSTALLED no implica DEPLOYED; DEPLOYED no implica LOADED; LOADED no implica INVOKED; INVOKED no implica EXECUTED; EXECUTED no implica éxito funcional.
5. Un objeto puede ser cargado varias veces, invocado múltiples veces y ejecutar múltiples operaciones. Un único valor booleano por NODE perdería multiplicidad, secuencia, actor, versión y ventana.
6. El silencio de S3 no prueba que no fue cargado/invocado/ejecutado salvo cobertura/detectabilidad suficiente para ese evento, familia, fase, duración y versión. La ausencia no se convierte en 0 por defecto.

Por tanto, no se recomienda seis columnas booleanas ni una enum única lifecycle_state como solución. La semántica mezcla claims de estado y ocurrencias.

## 4. Reconciliación de las estructuras existentes

| Estructura | Capacidad real | Carencia para lifecycle |
|---|---|---|
| NODE | Identidad/versión de objeto y snapshot exacto; observed_state genérico; §12.7 declara la intención de seis dimensiones | No separa seis claims, temporalidad, tipo estado/ocurrencia ni sus claves |
| PREDICATE | predicate_id, route/step/time/snapshot, predicate_type, observed_state y adjudication_rule | Catálogo de 14 predicados no incluye lifecycle; no forzar familias por analogía |
| CLAIM_EVIDENCE_LINK | Varios claims/evidencias por objeto mediante claim_statement, support_type y relevance_scope | claim_statement es texto; no hay claim_id/claim_type/claim_revision ni clave tipada para dimensión |
| EVIDENCE_REGISTER | Fuente, provenance, método, scope, versión, timestamp_start/end_tz, integridad, limitaciones | No tiene semántica separada de timestamp fuente/emisión/captura ni clock_domain |
| EVALUATOR_ASSESSMENT | Evaluación independiente E1/E2 de NODE/PREDICATE/etc., observed_state, rule_version, scope y rationale | Target es objeto, no claim exacto; dos claims distintos sobre el mismo NODE no quedan ligados inequívocamente |
| ADJUDICATION_REGISTER | Discrepancia y decisión sobre objeto tipado | Tampoco referencia claim lifecycle exacto; riesgo de adjudicar el objeto global en lugar de una dimensión |
| PROCESS_EVENT (Gate 98) | Ocurrencias operativas candidatas, identidad/revisión, event_time, intervalos, scheduled_time, recorded_at, clock_domain opcional | Opción B no aceptada; catálogo se centra en Z/provisión/instalación/rollback y no formaliza eventos runtime LOADED/INVOKED/EXECUTED |
| SNAPSHOT | Estado capturado, versión, timestamp, scope y pinning DEC-C10-065 | Estado acotado a captura; no acredita por sí solo eventos o continuidad entre snapshots |

### 4.1. ¿Puede reutilizarse PREDICATE?

No con el contrato actual sin nueva decisión:
- los 14 códigos U_G (ID-τ2, REL-τ2, COND-τ2, AUTH-τ2, RES-τ2, DEP-τ2, BLOCK-τ2, APP-τ2, ALT-A1, ALT-A2, ALT-DEP, ALT-F*, ORACLE, EXT) tienen semánticas y momentos definidos;
- predicate_type solo admite ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT;
- predicate_id conserva el código completo, pero no hay código lifecycle aprobado;
- reutilizar DEP para LOADED o REL para INVOKED alteraría el significado de los predicados y su función causal.

PREDICATE podría ser destino de una futura extensión versionada si se demuestra que su semántica ruta/paso/tiempo y su granularidad son apropiadas. No queda aceptado ahora.

### 4.2. ¿Puede reutilizarse CLAIM_EVIDENCE_LINK?

Puede documentar múltiples afirmaciones textuales sobre un mismo NODE exacto, pero no proporciona por sí solo:
- identidad estable de la afirmación;
- dimensión lifecycle controlada;
- versión de la definición de claim;
- distinción estructurada STATE vs OCCURRENCE;
- ventana/tiempo de validez con semántica;
- relación inequívoca entre cada claim y su evaluación/adjudicación E1/E2.

La tabla es una base reutilizable, no prueba de que el problema claim-level esté resuelto.

## 5. Contrato de observabilidad por dimensión

Las fuentes son candidatas y dependen del objeto y del método concreto; no se asigna una fuente universal a cada estado.

| Dimensión | Evidencia positiva mínima candidata | Evidencia negativa requerida | Resultado ante límites |
|---|---|---|---|
| DECLARED | Fuente S1 autoritativa, identidad/versión y ámbito exactos | Universo declarativo completo y enumeración cerrada | ? si alias, fuentes o versiones incompletos |
| INSTALLED | Evidencia de inventario instalado en entorno exacto, corroborada según riesgo por S2/S4 | Enumeración completa de ubicaciones/paquetes posibles y capacidad de detección | ? si capas/paquetes embebidos u opacos |
| DEPLOYED | Evidencia de despliegue efectivo y destino, no solo manifiesto deseado | Enumeración de destinos/superficies de despliegue | ? si drift o reconciliación no examinada |
| LOADED | S3 evidencia de proceso/módulo cargado, con instancia y ventana | Captura con sensibilidad y cobertura suficientes en todas las instancias/ventanas relevantes | ? ante muestreo, reinicio, carga tardía o pérdida |
| INVOKED | Traza/log/telemetría S3 con invocación, emisor/destino y correlación válida | Cobertura de canal y detección de invocaciones, incluidos caminos alternativos | ? ante sampling, filtros, rutas no activadas |
| EXECUTED | Evidencia de operación ejecutada, con identidad/correlación y resultado cuando corresponda | Cobertura de ejecuciones y canales relevantes, más regla de deduplicación | ? si solo se observa solicitud/invocación o respuesta ambigua |

Un claim 1/0/? es relativo a NODE exacto, versión, unidad, entorno, ruta cuando aplique, ventana y regla. Un 0 exige argumento de cobertura negativa de U_G Protocol §§6–7 y COMPLETE aplicable; COMPLETE no es universal fuera de su universo declarado. Los estados del DGP Generator permanecen segregados de las observaciones S3 del Analyzer.

## 6. Reconciliación temporal: emisión, ocurrencia, captura, observación y registro

### 6.1. Campos y significados recuperados

| Concepto | Artefacto/campo existente | Semántica |
|---|---|---|
| Tiempo atribuido a ocurrencia | PROCESS_EVENT.event_time o event_start_time/event_end_time | Cuándo ocurrió según fuente |
| Emisión del mensaje/señal | LOG_TRACE_EVENT, protocolo temporal S3 §17.2 | Cuándo emisor produjo/señaló el registro; no hay campo físico común identificado |
| Captura/recepción por colector | capture_time en métrica de lag S3; LOG_TRACE_EVENT contempla captura | Cuándo canal capturó/recibió la señal; no hay campo físico común identificado |
| Observación adjudicada de evidencia | observed_at referido en Gate 98/Gate 104 como ubicación conceptual EVIDENCE_REGISTER | Instante de observación/captura atribuido a la evidencia; no existe columna literal observed_at en EVIDENCE_REGISTER |
| Ventana de evidencia | EVIDENCE_REGISTER.timestamp_start/end_tz | Inicio/fin del alcance temporal de la evidencia; no equivale automáticamente a un instante de captura |
| Registro de revisión de evento | PROCESS_EVENT.recorded_at | Cuándo se incorporó esa revisión al registro |
| Captura de estado estructural | SNAPSHOT.timestamp | Tiempo del snapshot concreto; no es event_time ni necesariamente capture_time de un log |

### 6.2. Hallazgo de campo

Gate 98 afirma que observed_at se ubica en EVIDENCE_REGISTER y no debe duplicarse en PROCESS_EVENT. Sin embargo, el encabezado físico de EVIDENCE_REGISTER (§12.1) contiene timestamp_start/end_tz, no un campo llamado observed_at. El protocolo §4 define un timestamp genérico de captura/intervalo, pero no desglosa:
- timestamp de fuente;
- emisión del emisor;
- recepción/captura del colector;
- observación adjudicada;
- registro de evidencia/revisión.

Por ello, la regla de no duplicación es conceptualmente válida, pero el mapping observed_at → timestamp_start/end_tz no está formalizado. No se debe asumir que timestamp_start es observed_at o capture_time ni que un intervalo degenerado representa un instante sin contrato.

### 6.3. S3 y localización temporal

Temporal Horizon and S4R Integration Audit §17:
- define capture_time−event_time como distribución de lag/localización;
- diferencia emisión, captura, pérdida, duplicación, desorden, timestamp y validez para LOG_TRACE_EVENT;
- separa reloj S3, reloj truth y rejilla Δ;
- no presupone mecanismo de captura (periódico, continuo o event-driven), independencia, cobertura ni tasa de detección;
- exige caracterizar lag, pérdida, cobertura, error y dependencia;
- mantiene abiertos parámetros y calibración.

Esta definición metodológica es explícita, pero no fija un mapping físico entre sus timestamps y los campos de EVIDENCE_REGISTER/PROCESS_EVENT/SNAPSHOT. El modo híbrido debe preservar dependencia conjunta; no se suman evidencias como independientes.

## 7. Relojes y comparabilidad entre registros

PROCESS_EVENT propone clock_domain_id y clock_uncertainty opcionales. EVIDENCE_REGISTER no contiene esos campos; SNAPSHOT solo tiene timestamp. No se localiza una definición común para:
- clock_domain_id y su versión/autoridad;
- offset, deriva, sincronización y precisión;
- unidad/distribución de incertidumbre;
- timestamp de emisor frente a colector;
- conversión de zona/offset y preservación del valor original;
- reglas para comparar relojes distintos;
- buffering, reordenamiento, pérdida y duplicación.

**Regla de no inferencia:** no ordenar eventos ni calcular lag entre registros con relojes incomparables o semántica de timestamp desconocida. PRECEDES requiere orden sustentado por reloj comparable o evidencia independiente; CAUSES nunca se deriva de precedencia. recorded_at puede ordenar incorporación al registro, no la ocurrencia subyacente.

## 8. Mapping documental provisional (sin crear campos ni registros)

| Claim/tiempo | Target documental existente | Binding admisible | Lo que no se debe hacer |
|---|---|---|---|
| DECLARED/INSTALLED/DEPLOYED sobre objeto | NODE exacto por object_record_id + node_id, snapshot exacto | CLAIM_EVIDENCE_LINK con statement explícito y relevance_scope; E1/E2 solo como evaluación del objeto hasta resolver claim-level | Tratar observed_state global de NODE como seis resultados |
| LOADED/INVOKED/EXECUTED como ocurrencia | PROCESS_EVENT candidato solo si Opción B se acepta y event_type/fuente cumplen contrato; evidencia S3 en EVIDENCE_REGISTER | Referencia a NODE exacto cuando exista crosswalk y evidencia de acto | Crear evento desde ausencia/presencia de configuración o extender catálogo implícitamente |
| Predicado de lifecycle | PREDICATE solo tras decisión de catálogo y compatibilidad | predicate_id/familia versionados, ruta/paso/tiempo/snapshot exactos | Reutilizar DEP/REL/AUTH por parecido verbal |
| Evidencia de emisión/captura | EVIDENCE_REGISTER + referencia segura al artefacto S3 | timestamp_start/end_tz solo cuando su semántica de ventana esté declarada; captura puntual requiere mapping explícito | Copiar capture_time en observed_at sin regla |
| Estado capturado | SNAPSHOT exacto y su timestamp | Pinning DEC-C10-065 | Equiparar snapshot.timestamp con captura de log o event_time |
| Revisión de evento | PROCESS_EVENT.recorded_at | Record-time de revisión | Usarlo como tiempo de ocurrencia/captura |

Este mapping es una guía de no-confusión, no un contrato de materialización ni un esquema aceptado. No crea una nueva tabla, claim_id, evento, campo o FK.

## 9. Gaps y decisión

| ID | Gap | Estado |
|---|---|---|
| G105-01 | Semántica STATE vs OCCURRENCE para las seis dimensiones | RESOLVED CONCEPTUALLY; mapping por fuente |
| G105-02 | §12.7 seis lifecycle dimensions | PRESENT AS DESIGN INTENT; not structured |
| G105-03 | Identidad/versión/tipo de claim lifecycle | OPEN |
| G105-04 | E1/E2/adjudicación por claim y no solo por NODE | OPEN |
| G105-05 | Adecuación de PREDICATE o CLAIM_EVIDENCE_LINK como target claim-level | OPEN; no reuse accepted |
| G105-06 | LOADED/INVOKED/EXECUTED event typing | OPEN; PROCESS_EVENT not accepted |
| G105-07 | Capture/emission/source timestamps mapping to EVIDENCE_REGISTER | OPEN |
| G105-08 | observed_at physical mapping | OPEN; no literal field in current register header |
| G105-09 | Clock domain/uncertainty across PROCESS_EVENT/EVIDENCE/SNAPSHOT | OPEN |
| G105-10 | Snapshot timestamp to S3 capture | OPEN; no automatic equality |
| G105-11 | S3 mode, sensitivity, lag, loss and coverage calibration | STRUCTURE DEFINED; NUMERIC/EMPIRICAL OPEN |

### 9.1. Decisión de Gate 105

1. Se reconoce §12.7 como inclusión conceptual explícita de las seis dimensiones; Gate 104 queda corregido.
2. No se aprueban seis columnas booleanas ni una enum lifecycle única.
3. No se amplía ahora el catálogo de 14 predicados ni el enum event_type de Gate 98.
4. No se crea un registro paralelo de lifecycle claims o telemetría.
5. No se declara que el esquema actual ya permite adjudicación independiente claim-level. CLAIM_EVIDENCE_LINK ofrece claims textuales múltiples, pero no identidad tipada/versionada; EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER apuntan a objeto, no a claim inequívoco.
6. No se aprueba aún una extensión. La siguiente operación debe comparar alternativas mínimas reutilizando los registros existentes: (A) claim tipado/versionado en CLAIM_EVIDENCE_LINK con evaluación ligada a claim; (B) especialización de PREDICATE si se demuestra compatibilidad con su semántica; (C) separación de estado en NODE y ocurrencia en PROCESS_EVENT bajo aceptación independiente de Opción B. Cualquier alternativa debe preservar identidad de NODE, snapshot exacto, evidencia, tiempo, cobertura, E1/E2 y DGP truth firewall.
7. Para tiempos, mantener event_time, emission_time, capture_time, observed_at, recorded_at y SNAPSHOT.timestamp como roles conceptuales distintos hasta aprobar un crosswalk por fuente/método y clock domain. timestamp_start/end_tz no se reinterpreta globalmente.
8. Mantener C0 y DEC-C10-070 intactos. Ninguna cobertura de eventos sin snapshot se resuelve aquí.

**Siguiente operación recomendada — Gate 106:** comparación adversarial de tres alternativas de representación claim-level (CLAIM_EVIDENCE_LINK enriquecido; PREDICATE especializado; NODE state + PROCESS_EVENT occurrence) y especificación del crosswalk temporal mínimo S3→EVIDENCE_REGISTER/PROCESS_EVENT/SNAPSHOT. Evaluar identidad, cardinalidad, temporalidad, E1/E2, adjudicación, queryability, versionado, snapshots y no circularidad. No modificar DEC-C10-061/065/070/071/083/088; no DDL ni implementación.

## 10. Límites y control

Auditoría documental asistida, no revisión independiente. No se inspeccionaron sistemas reales, runtime, logs, snapshots ni artefactos fuente. No se generaron filas, eventos, claims, evaluaciones o capturas. No se ejecutaron parsers, constraints, tests, workflows, simulaciones, calibraciones ni experimentos.

scientific_execution=false; execution_authorized=false.

**Dictamen final:** GATE_105_LIFECYCLE_CONCEPTS_PRESENT / CLAIM_LEVEL_STRUCTURE_INCOMPLETE / STATE_VS_OCCURRENCE_SEPARATION_REQUIRED / S3_CAPTURE_METHOD_DEFINED_BUT_FIELD_MAPPING_OPEN / CROSS_REGISTER_CLOCK_CONTRACT_INCOMPLETE / C0_UNCHANGED / NO_DECISION_AMENDMENT / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.
