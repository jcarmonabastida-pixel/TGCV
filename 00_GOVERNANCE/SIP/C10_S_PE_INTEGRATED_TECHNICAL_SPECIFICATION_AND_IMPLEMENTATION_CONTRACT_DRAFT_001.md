# C10-S — PE: especificación técnica integrada y contrato de implementación

**ID:** C10-S-PE-TECH-CONTRACT-001 · **Fecha:** 2026-11-11  
**Estado:** PE_RECONCILED_DOCUMENTALLY / TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY / NOT_IMPLEMENTED / NOT_EXECUTED  
**Ámbito:** PR #116 · `research/c10-s-consolidation-draft`  
**Precedencia:** gobernanza canónica de `main`; decisiones aceptadas aplicables; maestro C10-S §§0.5, 213 y 269; PA–PD; contratos especializados vigentes.

## 1. Dictamen ejecutivo

PE completa la reconciliación documental de la arquitectura técnica y del contrato de implementación que puede especificarse sin inventar decisiones científicas. No convierte el diseño en un sistema implementable todavía. El resultado es una arquitectura lógica integrada, un mapa de contratos de datos e interfaces, un modelo de control de roles, un pipeline de validación y un conjunto de gates objetivos.

**Dictamen:** `PE_RECONCILED_DOCUMENTALLY / TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY`.

La arquitectura puede prepararse conceptualmente; no procede escribir código, crear fixtures confirmatorios, poblar IAM/U_G, generar datos, simular, estimar ni ejecutar. Siguen `scientific_execution=false` y `execution_authorized=false`.

## 2. Reconstrucción histórica y regla de no duplicación

PE reutiliza y armoniza, sin crear un segundo modelo de datos:

1. `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`: reloj t−1/t0…t9, unidad y asignación diferenciadas, roles, cegamiento, truth/observed, captura normalizada y subledger de petición.
2. `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md` y `C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md`: registros NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER.
3. Contratos U_G de identidad de registro, versionado/supersession, referencias tipadas, integridad referencial, snapshots exactos y control de cobertura.
4. `C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md`, `C10_S_TRANSFORMATIONAL_SNAPSHOT_AND_DELTA_RECONCILIATION_DRAFT_001.md`, manifiesto B/grafo de dependencias y matriz de predicados temporal.
5. `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md`, familias S4R, MEAS, MISS, POL, VER, TRJ, INT, GEN, PM, SNAP, REACH, PROV, GC, U_G y P177/P178/P179/P182/P183.
6. Decisiones aceptadas: DEC-C10-061/062/065/068/069/070/071/074–088, DEC-C10-095 y DEC-C10S-B1-REQUEST-MODE-001, DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001, DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 y DEC-C10S-B1-CAUSAL-ADJUDICATION-001, dentro de su alcance exacto.

La aceptación documental de esos contratos no equivale a esquema físico congelado, implementación, integridad ejecutable, prueba de seguridad ni autorización. Las decisiones UDG/JCS y PAR se aplican solo a sus objetos y alcances declarados; no se generalizan automáticamente a todos los registros C10-S.

## 3. Arquitectura lógica de componentes y fronteras

La arquitectura de referencia tiene seis responsabilidades separadas. Son interfaces lógicas, no servicios desplegados ni una selección tecnológica.

| Componente lógico | Responsabilidad | Entradas permitidas | Salidas |
|---|---|---|---|
| Orquestador de ejecución | Seleccionar contrato/escenario autorizado, fijar identidad de run, ordenar etapas y controlar gates | Test contract, autorización, versiones fijadas | Run envelope, orden de trabajo y referencias |
| Generator | Construir DGP, estados estructurales, mecanismos, potenciales y verdad contrafactual | Parámetros DGP aprobados, semillas/estado generador, contratos científicos | Paquete truth restringido y proyección observacional derivada |
| Proyector/Sealer de evidencia | Aplicar el contrato de observación, retirar campos reservados, comprobar integridad y sellar bundle del Analyzer | Observaciones generadas y reglas de medición | `observed_evidence` con hash/manifest y registro de liberación |
| Analyzer | Reconstruir constructos, estimar y emitir dictámenes solo con información permitida | Bundle observado, contratos/estimandos y documentación permitida | Resultado analítico estructurado, estado por estimando y trazas |
| Evaluator/Adjudicator | Comparar salida sellada con truth, medir recuperación/error/abstención | Truth restringido + salida Analyzer sellada + contrato de evaluación | Evaluator assessments, adjudicación y métricas |
| Artifact/provenance store | Conservar objetos inmutables, referencias, versiones, hashes, logs y reportes | Artefactos de cada etapa | Grafo reproducible de procedencia |

El Orquestador no debe convertirse en un canal de fuga de truth. El Proyector/Sealer no puede modificar truth ni adjudicar resultados científicos. El Analyzer no puede leer truth, potenciales, parámetros generadores, semilla secreta ni etiquetas causales verdaderas. El Evaluator no modifica retroactivamente la salida sellada del Analyzer. Las credenciales y permisos efectivos se implementarán como controles verificables; una separación nominal de módulos no prueba aislamiento.

## 4. Contratos de intercambio entre roles

### 4.1 Generator → Proyector/Sealer

El Generator produce dos productos conceptualmente separados:

- `truth_dgp`: estados verdaderos, potenciales por régimen, parámetros, mecanismos, interacciones, rutas, contribuciones y resultados potenciales.
- Registros generados de eventos/estados/mediciones a partir de los cuales se deriva la evidencia observable.

La salida de truth debe permanecer en un ámbito restringido. La evidencia observada no se construye copiando etiquetas ocultas ni exponiendo identificadores, orden, nombres de escenario, logs, errores o metadatos que permitan inferirlas de forma trivial.

### 4.2 Proyector/Sealer → Analyzer

El bundle observable contiene únicamente:
- registros y mediciones autorizados por el contrato de observación;
- identidad, versión, timestamps y snapshots necesarios;
- procedencia, cobertura, validez, incertidumbre y estados de ausencia;
- referencias a evidencia resolubles y hashes verificables;
- asignación/tratamiento solo cuando el diseño lo permita y resulte necesario para el estimando.

No contiene truth, potenciales contrafactuales, etiquetas verdaderas de contribución, parámetros del generador, reglas secretas del escenario ni semillas que permitan reconstruirlos. La documentación visible al Analyzer debe ser simétrica entre escenarios y no revelar la clase adversarial.

### 4.3 Analyzer → Evaluator

Antes de abrir truth, el Analyzer emite y sella una salida inmutable con:
- identidad de run y contrato de análisis;
- versión del Analyzer y configuración analítica permitida;
- estimando/constructo y población/unidad a los que se refiere;
- estimación o clasificación, incertidumbre y supuestos;
- dictamen: identificado, no identificado, indeterminado o efecto de paquete cuando proceda;
- diagnósticos, cobertura y limitaciones;
- hash del resultado y referencias exactas a las entradas observadas.

La ausencia de estimación puntual no es un error si el dictamen correcto es abstenerse. No se exige una respuesta causal positiva en todos los escenarios.

### 4.4 Evaluator → Adjudicación

El Evaluator accede a truth solo después del sellado de la salida analítica. La comparación se hace por estimando, dimensión, escenario y criterio de aceptación. Debe distinguir:
- recuperación numérica/estructural;
- clasificación correcta de identificación y no-identificación;
- falsos positivos/negativos;
- calibración, cobertura y precisión;
- cumplimiento del firewall;
- integridad y reproducibilidad del artefacto.

El Evaluator no se presenta como revisión humana independiente. La modalidad actual sigue siendo autoauditoría asistida cuando la misma autoría diseña y adjudica.

## 5. Modelo lógico de datos y trazabilidad

No se crea una nueva tabla universal ni se reemplaza U_G. El modelo lógico se compone de dominios y registros existentes:

| Dominio | Objetos/identificadores ya previstos | Función |
|---|---|---|
| Experimento | test_id/version, fixture_id/hash, run identity, scenario identity | Identificar contrato, fixture y ejecución sin inferir semántica de nombres |
| Unidad y asignación | unit_id, UE/UA/UO, Z, brazo/política y versión | Mantener unidad experimental, asignación y observación separadas |
| Servicio/instancia | contract_id/version, instance_id/version, component_id/class | Identidad contractual aceptada por DEC-C10-068/069 |
| Transformaciones | TID, SID, RID, EID | Separar identidad semántica, especificación, realización e instancia/evento |
| Snapshots/U_G | snapshot_id + snapshot_object_record_id; object_record_id/version; NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT | Fijar la revisión observacional exacta e impedir resolución por “latest” |
| Peticiones/trayectorias | request_id, trajectory_id y relación tipada | Registrar temporalidad, trazabilidad y contribución causal como relaciones distintas |
| Evidencia | evidence_id, coverage_scope_id, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER | Trazabilidad, cobertura y evidencia por objeto/afirmación |
| Evaluación | evaluator_record_id, object_record_id, adjudication records | Conservar evaluaciones separadas por evaluador y adjudicación |
| Resultado analítico | estimando, salida, incertidumbre, supuestos, dictamen, hash | Registrar la salida sellada que se compara con truth |

Los nombres de arriba describen identidades/campos ya presentes en los contratos referenciados o categorías lógicas. No autorizan a añadir columnas, enums, tablas, FKs ni claves físicas nuevas. Todo campo nuevo requeriría crosswalk, revisión de impacto y decisión cuando altere semántica.

### 5.1 Identidad y versionado

- IDs semánticos, IDs de registro, versiones de software/configuración y hashes son dimensiones distintas.
- `object_record_id` identifica una fila inmutable; `object_version` ordena revisiones de una misma identidad semántica según el contrato U_G.
- `manifest_record_id` y supersession siguen DEC-C10-079; binding probatorio PAR sigue DEC-C10-080/081.
- Las referencias tipadas y resolución exacta siguen DEC-C10-076 y el contrato U_G correspondiente.
- SNAPSHOT se fija por `snapshot_id + snapshot_object_record_id` conforme DEC-C10-065. No se resuelve por timestamp, orden de inserción ni “última versión”.
- TID/SID/RID/EID no se colapsan; un hash/build distinto no implica por sí solo identidad semántica distinta.
- Los objetos son append-only cuando el contrato aplicable así lo exige; no sobrescribir historia ni adjudicaciones.

### 5.2 Tiempo y eventos

Se conservan tres ejes no intercambiables:
1. reloj causal DGP t−1/t0…t9;
2. `stage_key` de captura/migración, con sus siete valores cerrados por DEC-C10-071;
3. SNAPSHOT.phase y step_k/ruta del proceso transformacional.

El ciclo B1 de petición se registra como subledger temporal relacionado con snapshots y con el reloj existente; no crea otro reloj ni amplía H. La oportunidad estandarizada por UE no implica que el servicio haya actuado. Orden parcial y timestamps se conservan; no se inventa un orden total ni una cardinalidad 1:1. request_id↔trajectory_id se tipa como TEMPORAL_ASSOCIATION, TRACEABILITY_LINK o CAUSAL_CONTRIBUTION conforme a las decisiones B1 aceptadas.

### 5.3 Estado trivalente y ausencia

Se mantienen ortogonales:
- `observed_state ∈ {1,0,?}`;
- `evidence_status`;
- `coverage_status`;
- adjudicación/revisión.

MISSING, NONE, PARTIAL, no inventariado o una referencia inaccesible no equivalen a 0. UNKNOWN no se convierte en fallo ni éxito. Las categorías y reglas ya aceptadas de U_G y de cada predicado tienen precedencia; PE no redefine enums globales.

## 6. Serialización, canonicalización y hashes

1. DEC-C10-074 acepta RFC 8785/JCS con prevalidación TGCV para el envelope U1 de UDG-01 y solo dentro de ese alcance. No es una decisión de serialización global para todo C10-S.
2. DEC-C10-075 rige la comparación semántica de universos U1 por sus siete niveles; no reduce identidad, igualdad canónica, igualdad de miembros y equivalencia definicional a un único booleano.
3. DEC-C10-076 rige referencias tipadas y resolución exacta.
4. Para otros registros, eventos, bundles Generator/Analyzer/Evaluator, logs y salidas, el perfil físico de serialización/canonicalización permanece OPEN. No se calcula un hash reproducible antes de fijar bytes, codificación, normalización, campos incluidos y tratamiento de arrays.
5. Un hash demuestra integridad de los bytes bajo el procedimiento declarado; no demuestra corrección semántica, verdad, independencia, causalidad ni autenticidad del origen sin cadena de custodia.

## 7. Manifiestos, reproducibilidad y almacenamiento

Se requieren conceptualmente manifiestos separados, no una bolsa única que mezcle roles:
- manifiesto del contrato/test y su versión;
- manifiesto del fixture/escenario y su identidad;
- manifiesto de run con commit, configuración, versión de componentes y referencias;
- manifiesto de snapshots/evidencia y procedencia;
- manifiesto restringido de truth;
- manifiesto del bundle observable liberado al Analyzer;
- manifiesto de salida sellada del Analyzer;
- informe de evaluación/adjudicación.

La relación entre ellos debe permitir reconstruir el linaje completo sin exponer truth al Analyzer. La semilla completa y parámetros que codifiquen truth quedan restringidos a Generator/Evaluator; el Analyzer recibe solo información necesaria para el análisis. Si se usa compromiso/hash de semilla, el procedimiento y el momento de revelación deben definirse antes de ejecutar.

**OPEN:** formato físico, almacenamiento, motor de persistencia, política de acceso, cifrado, custodia de secretos, retención, backups, exportación, logs de acceso y procedimiento de sellado. No se selecciona tecnología ni se colocan secretos o truth en GitHub.

## 8. Contrato de validación y pruebas

Las pruebas futuras se organizarán por capas, reutilizando los IDs existentes y sin crear familias duplicadas:

| Capa | Qué valida | Evidencia de aceptación futura |
|---|---|---|
| V0 — contrato estático | Consistencia de vocabularios, campos obligatorios, precedencia y crosswalks | Informe estático con versión/hash |
| V1 — schema/serialización | Tipos, dominios, cardinalidades, unicidad, claves y canonicalización dentro de su alcance | Parser/validator y casos válidos/inválidos |
| V2 — integridad referencial | FKs tipadas, referencias exactas, snapshots, supersession y ausencia de huérfanos/ciclos | Validación de integridad sobre fixture no confirmatorio |
| V3 — temporalidad | Baseline pre-Z, orden de eventos, snapshots inmutables, no retrocausalidad y ejes temporales distintos | Casos de secuencia, simultaneidad, missing y crossover |
| V4 — firewall de roles | No acceso de Analyzer a truth, potenciales, semillas o metadatos reveladores; Evaluator solo tras sellado | Threat model, permisos efectivos, pruebas de acceso/fuga y logs |
| V5 — reconstrucción semántica | T_acc/ΔT_acc, A_f, App, Reach, rutas, petición y contribución sin colapsos | Oráculos y aserciones por contrato |
| V6 — recuperación causal/estadística | ITT, primeras etapas, IV/LATE válido, mediación solo cuando identificable, sensibilidad y abstención | P177–P183 y contratos asociados con tolerancias predefinidas |
| V7 — reproducibilidad | Mismo contrato, inputs, entorno, semillas y hashes producen el resultado definido | Replay controlado y auditoría de diferencias |
| V8 — rendimiento/operabilidad | Capacidad de poblar, consultar, reconstruir y auditar sin pérdida | Perfil técnico y revisión operativa |

No se ejecuta ninguna capa en PE. La autoauditoría U_G SR-01…20 ya clasifica 8 PASS_STATIC, 10 CONDITIONAL y 2 NOT_ASSESSED; no declara aceptación global. En particular SR-13 (firewall) es CONDITIONAL, SR-19 (seguridad/custodia) y SR-20 (aptitud operativa) son NOT_ASSESSED. PE conserva estos límites y no los convierte en PASS técnico.

## 9. Contrato de salida del Analyzer

La salida debe ser estructurada por estimando y dimensión, no un único veredicto global. Como mínimo debe permitir registrar:
- estimando/constructo y versión del contrato;
- población, unidad, brazo/régimen y horizonte aplicables;
- estado de identificación y supuestos evaluados;
- estimación/intervalo cuando proceda, método y precisión;
- dictamen `EFFECT_OF_POLICY/PACKAGE`, `IDENTIFIED_UNDER_ASSUMPTIONS`, `NOT_IDENTIFIED` o `INDETERMINATE`, según vocabulario final aprobado;
- cobertura, missingness, censura, soporte e interferencia;
- vías colaterales, exclusión y sensibilidad;
- referencias exactas a observaciones y hash de salida.

Los literales anteriores son etiquetas conceptuales para discutir; salvo los estados ya definidos por los contratos vigentes, no se convierten en enums físicos cerrados en este documento. En particular, no se fuerza una salida para Value mientras Value no esté instanciado ni se interpreta el ITT de D2 como efecto puro de accesibilidad.

## 10. Matriz de preparación técnica y bloqueos

| Elemento | Estado PE | Qué puede hacerse ahora | Qué bloquea implementación confirmatoria |
|---|---|---|---|
| Arquitectura de roles | CONCEPTUALLY_RECONCILED | Especificar responsabilidades y flujos | Diseño/validación de permisos y firewall real |
| Relojes y eventos | LOGICALLY_RECONCILED | Mantener ejes existentes y subledger | Formato de eventos, orden parcial, timestamps y cardinalidades físicas |
| Identidad/versionado | PARTIALLY_ACCEPTED | Reutilizar TID/SID/RID/EID, U_G y DEC-065/069/079 | Crosswalk completo y prueba de integridad ejecutable |
| U_G lógico | DOCUMENTED / PARTIAL | Reutilizar plantillas y decisiones 061–065/070–088 | SR-03/09/11–14/18–20, validación física, seguridad y custodia |
| Serialización | PARTIAL | Aplicar JCS solo a UDG-01/U1 | Perfil canónico para otros registros/bundles |
| Truth firewall | CONCEPTUALLY_DEFINED | Definir roles y artefactos segregados | Threat model, almacenamiento separado, ACL, pruebas de fuga |
| DGP y fixtures | SCIENTIFICALLY_OPEN | Mapear contratos existentes y escenarios | Parámetros, contrastes, soportes, Value/Outcome, tolerancias y gates PD |
| Analyzer/estimandos | SCIENTIFICALLY_OPEN | Especificar contrato de salida sin fijar campos finales | PC no identifica θ_A, θ_Af ni C4 en D2 actual; Outcome/Value y medición incompletos |
| Tests/oráculos | DOCUMENTED / NOT_IMPLEMENTED | Reutilizar P177–P183 y S4R/MEAS/MISS/POL | Fixtures, oráculos, N/R, potencia, precisión y tolerancias |
| Seguridad/operación | NOT_ASSESSED | Enumerar controles y riesgos | Arquitectura técnica, acceso, custodia, retención, threat review |
| Ejecución/replay | NOT_AUTHORIZED | Documentar gates | Autorización explícita, executable/input/config hashes y workflow canónico |

## 11. Dependencias científicas heredadas de PA–PD

PE no puede cerrar por diseño técnico lo que sigue siendo una decisión o evidencia científica:

1. PA: Value no instanciado; Outcome técnico candidato y no operacionalizado; población material/eligibilidad limitada por ausencia de IAM/snapshots y reglas de valoración.
2. PB: D2/B1 y servicio tienen contratos documentales, pero no existe IAM material sellado ni snapshots observados; mapping de política a accesibilidad, ausencia de provisión focal de fondo y no-afectación colateral no están demostrados.
3. PC: ITT de política conserva alcance de paquete; θ_A(q), θ_Af(q_X*) y mediación interventional no están identificados en el D2 material actual. No se inventa mediador intervenible, soporte longitudinal ni Value.
4. PD: arquitectura truth/evidence/evaluation y mapa adversarial están reconciliados documentalmente, pero parámetros conjuntos, contrastes contrafactuales D2, reglas de transición, soporte/interferencia, tolerancias, N/R, potencia y error Monte Carlo siguen abiertos.
5. F*, G, H, ventanas, rutas y mapping semántico mantienen estados candidatos/abiertos donde así conste; no se transforman en constantes de software por conveniencia.
6. B1 como tipo de entidad solicitante sintética no cierra demanda, cardinalidad, consecuencia ni regla Value; no se confunde entidad solicitante/beneficiaria con UE/UA/UO, servicio, actor o evaluador.

## 12. Gates para pasar de contrato documental a implementación

No se autoriza implementación confirmatoria hasta que concurran todos los siguientes gates, con evidencia trazable:

- **G-SCI:** PA–PD cierran los constructos/estimandos necesarios o limitan formalmente el alcance confirmatorio; Value/Outcome y DGP se instancian sin contradicciones.
- **G-MAT:** IAM/snapshots/inventario material y mapping de B, versiones, dependencias, alternativas, unidad/cluster y soporte quedan resueltos en el alcance declarado.
- **G-SCHEMA:** modelo físico, formatos, dominios, cardinalidades, constraints, canonicalización por objeto y migraciones se especifican y aceptan; U_G SR pendientes tienen dictamen.
- **G-ROLE:** threat model, almacenamiento/ACL, secreto/semilla, logs, sealer y prueba del firewall Generator/Analyzer/Evaluator.
- **G-TEST:** contratos P177–P183 y fichas aplicables cruzados a fixtures/oráculos, aserciones, tolerancias, errores y criterios de abstención; validadores y replay especificados.
- **G-REPRO:** entorno, dependencias, versiones, semillas, inputs, comandos, hashes y manifiestos fijados; no se ejecuta con identidades flotantes.
- **G-AUTH:** autorización explícita y acotada para la operación concreta, rama/entorno/alcance y límites; una aceptación documental no sustituye esta autorización.

La secuencia de ejecución, cuando y solo cuando esté autorizada, seguirá el workflow canónico: recuperar diseño → preflight de integridad → ejecución primaria → auditoría → gate de replay → replay → auditoría final → cierre científico. No se adelanta replay ni se usa un PASS técnico como claim científico.

## 13. Decisiones y asuntos abiertos

**Decisiones reutilizadas, no reabiertas:** identidades de servicio/instancia DEC-C10-068/069; snapshot exacto DEC-C10-065; vocabulario stage_key DEC-C10-071; JCS/UDG-01 DEC-C10-074; comparación semántica UDG-03 DEC-C10-075; referencias UDG-04 DEC-C10-076; PAR/IAM DEC-C10-079…088; decisiones B1 de oportunidad, enlace y adjudicación causal; DEC-C10-095 dentro de su alcance.

**No se crea una decisión científica nueva en PE.** Se propone la arquitectura lógica de seis responsabilidades y el mapa de gates como síntesis técnica derivada; cualquier aceptación formal de contratos físicos, formatos, seguridad, infraestructura o nuevos campos requerirá decisión explícita según gobernanza.

Asuntos que permanecen OPEN: formato de run envelope y eventos; cardinalidad/orden temporal físico; serialización fuera de UDG-01; schema físico y motor; mapping exacto IAM↔U_G para todos los objetos; almacenamiento/custodia y permisos; perfil de seguridad; contrato de Analyzer output; Value/Outcome; parámetros y fixtures DGP; tolerancias/potencia; threat model y revisión operativa.

## 14. Criterios de aceptación documental de PE

PE se considera reconciliado documentalmente porque:
1. localiza y reutiliza las arquitecturas y decisiones existentes;
2. define fronteras lógicas Generator/Proyector/Analyzer/Evaluator/Orquestador/Store sin colapsar roles;
3. define contratos de intercambio y reglas de sellado sin revelar truth;
4. mantiene identidad, versionado, snapshots, temporalidad, procedencia y estados trivalentes;
5. limita JCS a UDG-01/U1 y no generaliza decisiones locales;
6. reutiliza registros U_G y contratos de prueba sin crear duplicados;
7. distingue qué está definido, condicionado, abierto y no evaluado;
8. establece gates científicos, materiales, de schema, roles, tests, reproducibilidad y autorización;
9. preserva no implementación/no ejecución y el estado Draft de PR #116.

**Dictamen final:** `PE_RECONCILED_DOCUMENTALLY / TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY / NOT_IMPLEMENTED / NOT_EXECUTED`.

No se ha modificado `main`, Core, RMA, Evidence→Claim Matrix, STATUS, claims ni autorizaciones. No se ha escrito código ni creado fixture/dato alguno.

## 15. Cross-reference PB — identidad material, IAM y aislamiento D2

La reconciliación de identidad B1 por UE y el contrato material D2 se integra en `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md`. La arquitectura técnica PE debe consumir ese contrato sin crear un modelo IAM paralelo: U_G y sus registros tipados permanecen como inventario/procedencia; contract_id/contract_version son comunes; instance_id/instance_version son propios de cada UE; el adaptador P1 se identifica separadamente.

La ausencia de roster, IAM/C_SRC, snapshots, grafo de dependencias, artefacto/runtime y evidencia de aislamiento impide declarar G-MAT satisfecho. B-M01…15 y PROV-01…12 son requisitos de inventario/verificación, no resultados. B-M13/oráculo y B-M14/A1-A2 no pueden ser modificados por B. El firewall lógico PE no prueba permisos/custodia efectivos ni aislamiento material.

No se aprueba schema físico, formato, motor, API, ACL, parser, fixtures ni captura. G-MAT/G-SCHEMA/G-ROLE permanecen abiertos; no implementación ni ejecución.


## 16. E+F — perfil técnico agnóstico y gates efectivos (2026-11-12)

Referencia rectora: plan C10-S §16.186. PE permanece TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY. Esta integración precisa evidencia de aceptación futura sin seleccionar tecnología ni añadir arquitectura:

- Generator conserva truth/potenciales/parámetros/semillas en dominio restringido y genera la proyección observacional sin copiar etiquetas reservadas.
- Proyector/Sealer es la única frontera de liberación; valida identidad, versión, timestamps, cobertura, integridad y campos permitidos; produce bundle observable inmutable y manifiesto/hash.
- Analyzer recibe solo bundle liberado y contratos públicos; no tiene credenciales, rutas, logs o metadatos que permitan reconstruir truth.
- Evaluator accede a truth solo tras el sellado inmutable de la salida Analyzer y no altera retroactivamente salida/evidencia.
- Store conserva separación de dominios, referencias exactas, versionado, retención y trazabilidad; Orquestador valida autorización y versiones y no es canal de truth.

Cualquier implementación física o equivalente debe justificar serialización por objeto (JCS solo en el alcance previamente aceptado), estructura/cardinalidades, reloj y orden parcial, fronteras de confianza, autenticación/autorización, custodia de secretos, ACL de mínimo privilegio/deny-by-default, sealer, logs, retención/backups y threat model que incluya fugas por contenido, nombres, tamaños, tiempos, orden, errores, hashes y metadatos. No se elige motor, nube, lenguaje, base de datos ni formato.

Evidencia futura mínima: matriz de roles/permisos efectivos; pruebas negativas de acceso y exfiltración; allowlist/denylist de proyección; prueba de no filtración; integridad/hash/referencias; orden temporal y replay; backup/restore y audit trail. G-SCHEMA, G-ROLE y G-REPRO siguen BLOCKED hasta evidencia verificable. La separación nominal de módulos no constituye firewall probado.

No se añade schema, campo, clase U_G, test, fixture ni ejecución. scientific_execution=false; execution_authorized=false.

## 17. Contrato PE para verdad temporal B1 y cobertura S3 (2026-11-12)

La implementación futura debe preservar la distinción entre:
- verdad reservada del Generator: estado funcional efectivo B1 por UE×intervalo y sus transiciones con event_time;
- evidencia S3 proyectada: señales pasivas, timestamps de captura, cobertura, lag, pérdida, binding y provenance por UE×intervalo×componente;
- salida del Analyzer: estimación, bounds o abstención por intervalo y V_cont;
- Evaluator: comparación con truth únicamente después del sellado del output.

El contrato de datos debe poder representar la familia causal de transición (ENABLED/PROFILE; proceso/módulo; ingreso/listener/socket; dependencia funcional; capacidad/recursos funcionalmente limitantes), sin convertir la causa técnica en truth. Provisión/instalación/reinicio se conservan como antecedentes. Una ausencia de señal nunca se interpreta como continuidad.

δ_det debe figurar como límite de dominio de medición calibrado, no como tolerancia del servicio. Δ, cadencia/resolución S3 y δ_det deben conservar campos/roles conceptualmente distintos si posteriormente se materializan. No se prescribe aquí un schema físico ni se autoriza implementación. Sin cobertura/detección identificada, la salida será bounds/abstención.

Los episodios que sigan activos en T* se registran como terminales/censurados; no se imputan como recuperados. El firewall debe impedir que Analyzer acceda a truth, potenciales, parámetros/semillas reservados o metadata que reconstruya estados.

**Estado:** TEMPORAL_TRUTH_OBSERVATION_SPLIT_DEFINED / PHYSICAL_SCHEMA_OPEN / FIREWALL_NOT_IMPLEMENTED / NO_EXECUTION_AUTHORIZED.


## 18. Contrato de normalización temporal y captura S3 (2026-11-12)

El schema lógico futuro debe poder expresar, sin imponer aún campos físicos: (a) reloj de truth/event_time; (b) coordenada adimensional x=(t−t0)/W_c con t0=0, t_c,max=1; (c) episodios y familia causal; (d) rejilla V_cont [0,1+ρ_follow], K y Δ; (e) captura S3 por componente, mecanismo, timestamp, fase, cobertura, lag, pérdida y provenance; (f) estados observados 1/0/?; y (g) terminal/censura.

S3 permanece pasivo y separado de truth. Los mecanismos snapshots/métricas, logs/trazas/eventos e híbrido son variantes de captura dentro de S3 existente, no fuentes nuevas. No se presume independencia entre componentes ni completitud. Analyzer solo recibe la proyección S3 permitida; no recibe W_c físico, truth, potenciales, semillas ni parámetros reservados que permitan reconstrucción.

El contrato debe preservar d_min,DGP como frontera del soporte sintético, nunca tolerancia funcional; δ_det como curva condicionada al canal y umbral p*; y Δ/cadencia S3/τ_follow como parámetros separados. Sin umbral aprobado o canal identificable, salida bounds/abstención. No se fija schema físico, tecnología, tasa, K ni frecuencia, y no se autoriza implementación.

**Estado:** LOGICAL_TIME_SCHEMA_DEFINED / PHYSICAL_SCHEMA_OPEN / S3_CHANNEL_UNCALIBRATED / FIREWALL_NOT_IMPLEMENTED / NO_EXECUTION_AUTHORIZED.


## 19. Crosswalk PE de captura temporal y recuperación (2026-11-12)

El contrato PE reutiliza el canal S3 existente y las aserciones P182/P183/MEAS/MISS; no crea fuente, actor, endpoint, probe, rol ni prueba nueva. La proyección de S3 conserva por componente mecanismo (snapshot/métrica, log/traza/evento o híbrido), timestamp/fase, cobertura, lag, pérdida, validez, versión, unidad/instancia, provenance y dependencia. Los estados observados 1/0/? no se confunden con A_B1 truth.

El Generator mantiene en zona reservada eventos/estados funcionales; el Sealer libera solo la evidencia S3 permitida; Analyzer no recibe truth, potenciales, semillas, parámetros reservados ni metadatos reconstruibles; Evaluator compara después del sellado. P182-11/12 gobiernan separación y trazabilidad; P183-01/02/04/07/09/10/11 gobiernan ausencia, mecanismo, no observado≠cero, pérdida diferencial, censura y bounds; P182-07/08/04/10 cubren error y discriminación.

La salida por intervalo y V_cont será puntual solo con identificación del canal; de otro modo bounds/abstención. Los mecanismos híbridos deben conservar dependencia entre componentes; no se asume independencia ni se agregan señales con reglas no validadas.

**Estado:** PE_TEMPORAL_CAPTURE_CROSSWALK_DEFINED / PHYSICAL_SCHEMA_OPEN / FIREWALL_NOT_IMPLEMENTED / NO_EXECUTION_AUTHORIZED.


## 20. Matriz PE de cobertura temporal y seguimiento (2026-11-12)

El contrato lógico conserva r_c=d_e/c_j, r_Δ=d_e/Δ, fase de captura, lag y r_f=τ_follow/τ_recovery,max. Se deben poder reconstruir los estratos menor/igual/mayor que 1 y los estados capturado, no emitido/perdido, retrasado, válido, inválido y censurado. La matriz dirigida cubre controles negativos, aliasing, cruce de fronteras, errores diferenciales/correlacionados, recuperación y terminalidad, reutilizando perfiles DGP y P182/P183 existentes.

El Sealer preserva la evidencia y cobertura; Analyzer no recibe verdad ni parámetros reservados. K/Δ no se codifican como cadencia S3. Un horizonte sin soporte acotado de recuperación debe preservar censura. No se materializa schema físico ni se autoriza ejecución.

**Estado:** TEMPORAL_COVERAGE_LOGICAL_CONTRACT_DEFINED / PHYSICAL_SCHEMA_OPEN / FIREWALL_NOT_IMPLEMENTED / NO_EXECUTION_AUTHORIZED.
