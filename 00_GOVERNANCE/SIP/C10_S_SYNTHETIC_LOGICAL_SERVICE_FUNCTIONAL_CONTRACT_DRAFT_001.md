# C10-S — Contrato funcional del servicio lógico sintético de referencia

**ID:** C10-S-SYNTHETIC-SERVICE-CONTRACT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-06  
**Estado:** ACEPTADO CONCEPTUALMENTE POR DEC-C10-068; contrato funcional de referencia para C10-S. No es aún Design Freeze, mapping físico implementado, inventario real, implementación ni ejecución.

## 1. Propósito y relación con decisiones vigentes

Este documento especializa, sin sustituirlas, las decisiones ya registradas: DEC-C10-051 (microdominio de migración de configuración entre dos entornos software), DEC-C10-052 (clase A: paquete de configuración de servicio software), DEC-C10-057/058 (perímetros P0/P1/P2 y unidad lógica de servicio) y DEC-C10-056 (CMP≥1, PAR≥1, RUL≥1; MET obligatorio).

No se elige producto, proveedor, lenguaje, formato, plataforma ni servicio real. Se define un **servicio lógico sintético de referencia** para que el DGP tenga semántica funcional conocida y falsable. Es una especificación estipulada del mundo sintético, no una afirmación empírica sobre servicios reales ni una generalización a toda configuración software.

## 2. Unidad lógica y función de referencia

Unidad: una instancia lógica versionada de un servicio software de procesamiento de solicitudes. Su función abstracta es aceptar solicitudes cuando está habilitado y exponer un perfil operativo declarado. La identidad funcional no depende de host, proceso, contenedor ni ubicación.

El objeto migrado P0 es el paquete declarativo de configuración de esa unidad. P1 contiene runtime, binarios, infraestructura, permisos efectivos, recursos y estado del entorno. P2 conserva rutas, provisión B, dependencias, alternativas, agentes, observación, ejecución y posibles vías colaterales. Se mantiene la clasificación de DEC-C10-058.

## 3. Parámetros lógicos del núcleo

Se proponen dos parámetros obligatorios para esta instancia sintética:

| Clave lógica | Tipo | Dominio finito | Semántica |
|---|---|---|---|
| PAR-SVC-ENABLED | BOOL | {false,true} | Declara si el servicio debe aceptar solicitudes |
| PAR-SVC-PROFILE | ENUM | {STANDARD, READ_ONLY, DISABLED} | Declara el modo funcional deseado |

Los símbolos ENUM son identificadores semánticos abstractos del DGP, no valores de un producto. STANDARD y READ_ONLY son perfiles operativos habilitados; DISABLED es el perfil que declara inactividad. No se infiere que estos perfiles existan en una plataforma real.

PAR-SVC-RETRY-COUNT queda fuera del núcleo mínimo hasta que se justifique su pertenencia al contrato funcional de esta unidad. No se traslada a P0 una variable de capacidad, cuota o consumo de recursos P1.

## 4. Regla constitutiva candidata

**ID lógico:** RUL-SVC-ENABLE-PROFILE-01  
**Owner:** CMP-SERVICE-LOGIC (identidad lógica provisional; debe asignarse al CMP concreto de la instancia).  
**Scope:** configuración declarativa completa de la unidad lógica de servicio.  
**Efecto:** REQUIRE.  
**Condición:** si PAR-SVC-ENABLED=true, PAR-SVC-PROFILE debe pertenecer a {STANDARD, READ_ONLY}.

Metalenguaje compatible con el núcleo aprobado:

`OR(NEQ(PAR-SVC-ENABLED,true), IN(PAR-SVC-PROFILE,{STANDARD,READ_ONLY}))`

La regla tiene contraste no tautológico dentro del dominio declarado:
- ENABLED=true, PROFILE=STANDARD → satisface.
- ENABLED=true, PROFILE=READ_ONLY → satisface.
- ENABLED=true, PROFILE=DISABLED → viola.
- ENABLED=false, cualquier PROFILE declarado → no queda restringido por esta regla.

La última condición es deliberada: esta RUL impone una implicación, no una equivalencia. No se infiere que ENABLED=false obligue a PROFILE=DISABLED. Si se desea esa segunda dirección, requerirá justificación y regla separada, no se añadirá por simetría.

La regla no codifica Outcome, Value, permisos efectivos, disponibilidad de recursos, ejecución ni éxito de la migración. Su fuente funcional es este contrato sintético, fijado ex ante para el DGP. Por tanto, su validez es interna al mundo sintético definido aquí; no se presenta como norma de ingeniería externa.

## 5. Semántica de evaluación

La evaluación usa TRUE/FALSE/UNKNOWN. Si falta un valor, hay NULL/ABSENT no admisible, conflicto de identidad/versión o cobertura insuficiente, la regla no se fuerza a TRUE/FALSE: resultado UNKNOWN salvo que evidencia suficiente confirme una violación independiente.

Una evaluación FALSE acredita incumplimiento de la regla en el objeto/versión evaluados; no implica por sí sola F*=0 si la agregación contractual y la suficiencia de evidencia no están cerradas. UNKNOWN permanece indeterminado. No se imputan estados ni se confunde verdad DGP con observación del analizador.

## 6. Conservación y aplicación en rutas

F1/A1 deben preservar la identidad semántica de la regla, sus operandos, dominio ENUM, scope, versión y efecto en el mapping intermedio. F2/A2 deben aplicar el paquete/regla en destino bajo el mismo contrato funcional. El mapping puede cambiar etiquetas físicas, pero debe preservar los símbolos semánticos y la condición; su equivalencia requiere tabla de correspondencia explícita y evidencia del estado aplicado.

La adjudicación distingue:
- FP-03: preservación semántica de condición, operandos, scope y efecto;
- FP-06: aplicación efectiva del paquete/regla en destino;
- FP-07: verificación post-aplicación;
- FP-08: trazabilidad y procedencia probatoria.

La igualdad textual del AST no basta si el mapping altera el significado. La preservación del AST tampoco prueba que la regla se haya aplicado.

## 7. Casos adversariales mínimos para el DGP

El generador deberá incluir, al menos conceptualmente, estos contrastes conocidos:
1. regla y parámetros preservados: condición satisfecha;
2. ENABLED=true con PROFILE=DISABLED: violación;
3. inversión de NEQ/IN o ampliación indebida del conjunto permitido: mutación semántica;
4. cambio de scope o de owner: pérdida de aplicabilidad;
5. REQUIRE cambiado a FORBID: inversión del efecto;
6. regla preservada en representación intermedia pero no aplicada en destino;
7. valor ausente/conflictivo o evidencia incompleta: UNKNOWN;
8. cambio de etiqueta física con mapping semántico correcto: equivalencia preservada;
9. igualdad de etiquetas físicas con mapping semántico incorrecto: no equivalencia.

Los casos no son fixtures serializados ni pruebas ejecutadas. Los resultados futuros deberán separar hidden_truth del input accesible al analizador y del oráculo evaluador.

## 8. Límites y gates pendientes

La especialización funcional y RUL descritas quedan aceptadas conceptualmente por DEC-C10-068 como contrato de referencia del DGP sintético. No cierra:
- identidad CMP concreta, versión de instancia, procedencia detallada y serialización final;
- identidad CMP definitiva, versión, procedencia y serialización;
- tabla concreta de mapping fuente/destino;
- obligatoriedad/aplicabilidad IAM de cada predicado;
- contrato completo de F*, oráculo y errores de medición;
- unidad de asignación/interferencia y estimandos;
- fixtures, implementación, validadores, simulación o ejecución.

**Estado final:** contrato funcional sintético aceptado por DEC-C10-068; DEC-C10-056 sigue siendo la fuente de cardinalidad. La aceptación no congela el diseño completo ni autoriza implementación o ejecución.

## 9. Registro de aceptación

DEC-C10-068 acepta el servicio lógico sintético, los parámetros PAR-SVC-ENABLED/PAR-SVC-PROFILE y RUL-SVC-ENABLE-PROFILE-01 con la semántica y contrastes de §§2–4. CMP-SERVICE-LOGIC permanece como owner lógico provisional; identidad/versionado concretos, IAM de instancia, mapping físico, tolerancias y oráculo siguen abiertos. PAR-SVC-RETRY-COUNT continúa excluido del núcleo. No hay fixtures ni ejecución.

## 10. Clarificación de owner lógico e identidad CMP

En DEC-C10-068, `CMP-SERVICE-LOGIC` se usó como owner/rol lógico provisional. No es por sí mismo un `component_id` único, un `instance_id` ni una versión. La propuesta `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md` separa esas entidades y somete a aceptación los candidatos `C10S-SVC-REQUEST-PROCESSOR`, `C10S-SVC-REQUEST-PROCESSOR-001` y `CMP-SERVICE-LOGIC-001`.

La semántica funcional de ENABLED/PROFILE/RUL permanece aceptada por DEC-C10-068; los IDs/versiones candidatos no quedan aceptados por esa decisión. No se asigna hash hasta congelar formato canónico. El contrato no fija valores de escenario, instancia serializada ni mapping físico.


## 11. Mapping semántico de la instancia y la regla RUL entre rutas (2026-11-10)

Esta sección integra el contrato funcional aceptado por DEC-C10-068 con las decisiones posteriores DEC-C10-069/071/082/083. No redefine el dominio ni crea un formato.

1. La identidad CMP es CMP-SERVICE-LOGIC-001/SERVICE_LOGIC, bajo contrato C10S-SVC-REQUEST-PROCESSOR v1.0.0 e instancia C10S-SVC-REQUEST-PROCESSOR-001 rev1. Su NODE anchor se resuelve por snapshot exacto, no por igualdad de record IDs entre snapshots.
2. ENABLED y PROFILE mantienen sus identidades, tipos y dominios aceptados. DEC-C10-083 rige su presencia VALUE en las posiciones declarativas, preservación independiente F1/A1 y observación aplicada F2/A2.
3. RUL-SVC-ENABLE-PROFILE-01 conserva owner, scope, AST, operadores, constantes, dos bindings tipados a PAR y efecto REQUIRE. La expresión semántica no cambia entre C_SRC, S2/S1, destino declarado y estado aplicado.
4. Los bindings AST→PAR no son REF. REF sigue OPEN hasta inventario exhaustivo; no se presume REF=0.
5. M_F_sem y M_A_sem son composiciones distintas de mappings de etapa. La equivalencia de contrato no demuestra independencia técnica de la ruta A respecto de B.
6. CMP/PAR/RUL/MET reutilizan NODE, manifiesto PAR/COVERAGE_SCOPE, PREDICATE y metadatos/evidencia U_G existentes. No se añade una entidad PAR ni tabla MET.

El encoding físico, mapping_id/version, canonicalización, escaping, hash, snapshots observados, evidencia de aplicación y validación del oráculo permanecen OPEN. JCS UDG-01 no se extrapola. No hay instancia serializada, parser ni ejecución.


## 12. Límite del contrato funcional respecto del ciclo de petición B1 (2026-11-11)

El contrato funcional define que la unidad lógica de servicio procesa solicitudes cuando está habilitada y expone el perfil operativo declarado. No define por sí solo un protocolo de petición completo. Para evitar sobreinterpretación, se distinguen como conceptos de integración aún no especificados: oportunidad de petición, intento externo, recepción en frontera de ingreso, admisión/rechazo funcional, procesamiento, respuesta y consecuencia para la entidad solicitante.

La regla RUL-SVC-ENABLE-PROFILE-01 y los parámetros PAR-SVC-ENABLED/PAR-SVC-PROFILE conservan exactamente su semántica aceptada. No se infiere de este addendum un payload, esquema, cola, política de reintentos, timeout, SLA, idempotencia, concurrencia, prioridad ni contrato de errores. Tampoco se equipara el estado de admisión o procesamiento con F1/F2, ejecución transformacional, O-CONF o Value.

La especificación B1 §11 es un crosswalk conceptual de ciclo de vida, no una extensión normativa de la interfaz ni un contrato físico. Su recomendación de carga estandarizada requiere aceptación y posterior especificación antes de cualquier implementación.


## Decisión aceptada DEC-C10S-B1-REQUEST-MODE-001 (2026-11-11)

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.


## DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 — una oportunidad estandarizada por UE (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta **N_opportunities = 1 por unidad experimental (UE)** como configuración primaria candidata del probe estandarizado de servicio en el núcleo confirmatorio mínimo de C10-S. La oportunidad se define ex ante antes de Z y se presenta después del snapshot de accesibilidad t3/t4 mediante el mismo harness externo y bajo las mismas reglas en ambos brazos. El harness registra Request_attempt aunque no exista recepción por el servicio.

La identidad y el contenido de la oportunidad deberán ser comunes, trazables y versionados entre brazos. No recepción, rechazo, error o estado pendiente permanecen como estados observables; no se recodifican automáticamente como ausencia de necesidad, fallo transformacional, Outcome negativo ni Value=0. La población ITT no se condiciona a intento, recepción, admisión, procesamiento o respuesta post-Z.

Las oportunidades repetidas o cargas de mayor intensidad quedan reservadas a escenarios secundarios/adversariales; si se estudian, sus observaciones se anidan en la UE y no incrementan el número de unidades experimentales independientes. Esta configuración de una oportunidad no demuestra capacidad bajo carga sostenida ni demanda natural, preferencia revelada o Value del beneficiario.

Se mantienen abiertos: ventana/calendario exacto; definición final del payload y protocolo; identidad/versionado de B1 y servicio; cardinalidad request_id↔trajectory_id; tratamiento técnico de timeout, errores y pendientes; outcome técnico de respuesta; consecuencia independiente de B1 y horizonte; perspectiva/autoridad de valoración; población/soporte e integración exacta con ITT y mediación. No se equiparan eventos de petición con t5/t6/t7, ejecución transformacional, Outcome o Value, ni se amplía el reloj t−1/t0…t9.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación main/PR #116.

## DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 — contrato semántico de enlace (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como arquitectura candidata que la relación entre `request_id` y `trajectory_id` sea explícita, tipada y versionada, sin imponer una cardinalidad funcional 1:1. Se distinguen tres tipos no intercambiables:

1. `TEMPORAL_ASSOCIATION`: coexistencia temporal u orden compatible entre petición y trayectoria; no demuestra trazabilidad ni contribución causal.
2. `TRACEABILITY_LINK`: referencia técnica/documental verificable entre registros; no demuestra que la petición haya causado o modificado la trayectoria.
3. `CAUSAL_CONTRIBUTION`: relación causal definida por el DGP generador; debe distinguirse la verdad conocida por el generador de la evidencia observable y disponible para el analizador.

El modelo debe poder representar petición sin trayectoria atribuible, trayectoria sin petición atribuible, una petición que contribuya a varias trayectorias y, en escenarios con múltiples peticiones, varias peticiones que contribuyan a una trayectoria. La configuración primaria mantiene una oportunidad estandarizada por UE; por tanto, no genera múltiples request_id estandarizados dentro de esa UE, pero no impone que solo pueda existir una trayectoria ni que toda trayectoria tenga origen en esa petición. Las relaciones de escenarios secundarios con peticiones repetidas quedan anidadas en UE y no crean unidades experimentales independientes.

La existencia de cualquier enlace temporal o de trazabilidad no puede promoverse automáticamente a contribución causal. Las contribuciones causales se establecen por la verdad del DGP y se contrastan mediante los mecanismos/contrafactuales pertinentes; no se adjudican por proximidad temporal, coincidencia de IDs, respuesta del servicio o éxito técnico. Los registros observados no deben revelar al analizador la etiqueta de verdad del DGP salvo que ese conocimiento forme parte explícita del diseño de medición.

El enlace no define elegibilidad, inclusión poblacional, ITT, Outcome ni Value, y no puede usarse para excluir UE por eventos post-Z. No equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9; tampoco amplía el reloj t−1/t0…t9 ni la profundidad H. Los eventos de petición y sus enlaces se mantienen en subledger con timestamps, identidad/versionado y procedencia.

**OPEN:** reglas de generación de contribuciones, mecanismo de adjudicación, unidad temporal de atribución, tratamiento de contribuciones concurrentes y colaterales, evidencia observable para el analizador, cardinalidad de enlaces por tipo en cada DGP, y relación exacta con los estimandos ITT/mediación. No se congela schema físico ni protocolo técnico.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. D2 continúa como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren; main no se modifica.