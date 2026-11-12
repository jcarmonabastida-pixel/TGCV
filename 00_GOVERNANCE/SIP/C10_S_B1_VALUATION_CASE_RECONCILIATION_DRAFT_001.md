# C10-S — Reconciliación del caso de valoración B1 en el microdominio de migración de configuración

**ID:** C10-S-B1-VALUATION-CASE-001  
**Fecha:** 2026-11-11  
**Estado:** CASE_FRAMEWORK_RECONCILED / NEED_CONTENT_OPEN / CONSEQUENCE_ENVELOPE_CANDIDATE / NO_VJ_SELECTED / NOT_DESIGN_FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Objeto, alcance y precedencia

Este documento desarrolla el caso semántico de valoración de B1 que faltaba para avanzar desde la arquitectura B2–B3 hacia fichas §224 admisibles. Reutiliza:
- DEC-C10-095 y DEC-C10-051 (arquitectura A/B y microdominio de migración de configuración entre dos entornos software);
- DEC-C10S-B1-UNIT-001, DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001, DEC-C10S-B1-REQUEST-MODE-001, DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 y DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001;
- C10S-B-VALUE-MIN-001 §§13, 15–16; C10S-B1-REQUESTER-CANDIDATE-001 §§1–11;
- contrato funcional F*, cards F1/F2/A1/A2 y matriz FP-01…FP-08;
- DGP temporal/roles, PB-MAT, C-Value §§264–265, B2–B3, P179/P182/P183 y §224;
- reconciliación integrada de factibilidad y ciclos D2 y Outcome/Value.

No reabre decisiones aceptadas, no sustituye el DGP, no crea un beneficiario real ni inventa una operación de negocio, no selecciona dimensiones V_j, Outcome confirmatorio, indicadores, escalas, pesos, instrumentos, ventanas o parámetros. Es una reconciliación semántica candidata, no una decisión científica nueva.

## 2. Instancia lógica que el caso debe respetar

El caso conserva identidades separadas:
- **UE:** instancia sintética completa a la que se asigna Z.
- **B1:** una entidad solicitante-beneficiaria sintética por UE, referente de Need_preZ y de la consecuencia valorada.
- **Servicio:** una instancia lógica versionada por UE de C10S-SVC-REQUEST-PROCESSOR, bajo plantilla/contrato funcional común.
- **Oportunidad:** una oportunidad estandarizada por UE, definida ex ante y presentada después del snapshot de accesibilidad t3/t4 por harness externo común.
- **Trayectoria:** objeto distinto de la petición; los enlaces request↔trajectory son tipados y versionados (asociación temporal, trazabilidad o contribución causal).
- **Ejecutor y Evaluator:** roles separados de B1; el Evaluator aplica la regla de adjudicación, no representa las preferencias de B1.

La modalidad endógena de solicitud permanece secundaria/adversarial. La oportunidad estandarizada es un probe común de servicio: no representa demanda natural, preferencia revelada, uso real ni valor por sí misma. No se condiciona la población ITT a intento, recepción, admisión, procesamiento, respuesta, selección o ejecución post-Z.

## 3. Caso de uso y frontera funcional

El escenario de diseño es la migración de una configuración declarativa desde un entorno software de origen a otro de destino:
- F1/τ2 convierte la representación de origen S0 en una representación intermedia S2;
- F2 aplica y verifica la configuración en el destino, produciendo el estado SF si satisface el contrato;
- A1/A2 constituyen la ruta alternativa candidata de exportación/importación;
- F* juzga la conformidad funcional de la ruta completa bajo el contrato, contexto y propiedades aplicables;
- el servicio lógico recibe y procesa la oportunidad/petición según su contrato.

F* y O-CONF evalúan conformidad técnica de la configuración aplicada. No describen por sí mismos qué propósito tenía B1, si ese propósito se alcanzó, qué consecuencias sufrió B1 ni cómo las valora. El caso de valoración comienza en la necesidad/objetivo basal de B1 y termina en la consecuencia para esa entidad, no en el estado técnico SF.

## 4. Formulación candidata de Need_preZ — sin instanciar su contenido

La formulación mínima compatible con el microdominio es:

> Antes de Z, B1 tiene un objetivo operativo focal, definido independientemente de la intervención, relacionado con disponer de una configuración utilizable en el entorno de destino para sostener una operación de servicio previamente declarada.

Esta frase delimita el tipo de relación entre B1, la configuración y el servicio, pero **no identifica todavía cuál es la operación de servicio ni el contenido sustantivo de la necesidad**. No debe convertirse en verdad de DGP hasta que ese contenido sea especificado y aceptado. En particular:
- Need_preZ no es «necesita que se instale el adaptador» ni «necesita que τ2 sea accesible»;
- no se define por Request_event, respuesta, O-CONF, F*, selección o ejecución;
- no se infiere de que B haya sido asignado ni de que el servicio haya procesado la oportunidad;
- se representa en truth_dgp antes de Z con estados 1/0/?; unknown no equivale a ausencia;
- E_req_preZ, elegibilidad experimental, demanda de recursos y solicitud efectiva permanecen distintas.

Los casos Need_preZ=0 son candidatos a controles negativos/adversariales, no se incorporan automáticamente al estimando primario de Value. La población confirmatoria B1 y la regla de inclusión de Need_preZ deben quedar definidas pre-Z; no se filtra por eventos postratamiento.

## 5. Consecuencia B1: objeto de valoración distinto del proceso técnico

La consecuencia relevante es el cambio posterior en la situación de B1 respecto del objetivo basal, con independencia de que el servicio:
- no reciba la oportunidad;
- rechace o deje pendiente la petición;
- la procese técnicamente;
- produzca una respuesta técnicamente conforme;
- o permita que una ruta transformacional alcance SF.

El caso debe poder representar tanto progreso/resolución del objetivo como no resolución y consecuencias adversas. Como **envolvente de consecuencias a investigar**, no como roster de dimensiones, quedan diferenciadas:
1. logro, progreso o no logro del objetivo basal;
2. continuidad, interrupción o degradación de la operación dependiente;
3. demora o pérdida de oportunidad;
4. esfuerzo adicional de recuperación/intervención externa;
5. exposición a fallos, riesgo o reversibilidad insuficiente.

Estas clases no son V_j aprobadas, no son exhaustivas y no se convierten en variables/indicadores por su mera inclusión. Su función es evitar que el caso describa solo el éxito técnico y que se omitan efectos negativos o vías colaterales. Cada clase solo podrá promoverse a dimensión si supera los criterios de §7.

## 6. Mapa causal del caso y pruebas de no circularidad

El DGP debe permitir, sin imponerlas como relaciones empíricas, al menos estas rutas:

1. **Ruta focal candidata:** Z/política D2 → provisión/instalación → C_dep* → A_f*/D_f*/ΔT_acc* → Reach/posibilidades → respuesta/uso transformacional → consecuencia B1 → V_j.
2. **Ruta técnica:** Z/política → estado del servicio/proceso → O-CONF u otro Outcome técnico → consecuencia B1 → V_j, si el mecanismo se especifica.
3. **Vías directas/colaterales:** Z/política → recursos, coste, latencia, seguridad, información, prioridad, alternativas o carga de recuperación → consecuencia B1 → V_j.
4. **Ruta alternativa basal:** A1→A2 puede permitir el objetivo de B1 sin apertura de τ2; su equivalencia e independencia deben demostrarse, no suponerse.
5. **Vías no técnicas externas:** circunstancias del contexto DGP pueden modificar la consecuencia de B1 sin modificar F* ni O-CONF.

Pruebas adversariales necesarias:
- O-CONF favorable y consecuencia B1 nula o desfavorable;
- O-CONF desfavorable y consecuencia B1 favorable por ruta alternativa o recuperación;
- ΔT_acc* positivo sin cambio en Reach, respuesta o consecuencia;
- consecuencia B1 distinta entre brazos aun con O-CONF constante;
- misma consecuencia B1 con distintos estados O-CONF;
- oportunidad no recibida/no procesada sin recodificar Need_preZ ni V_j a cero;
- vías colaterales diferenciales que obliguen a interpretar ITT como efecto de paquete.

Estas son condiciones de discriminación del diseño; no afirman que todos los escenarios estén ya cuantificados ni crean IDs de test nuevos. Se reutilizan P179/P182/P183 y MEAS/MISS.

## 7. Regla de perspectiva y admisibilidad de futuras V_j

La perspectiva primaria continúa siendo la de B1, conforme a la base aceptada en B2–B3. Esto no significa que el Evaluator adopte preferencias humanas ni que se presuma una preferencia empírica. La autoridad de valoración debe ser una regla normativa explícita del mundo sintético, fijada ex ante, versionada y aplicada simétricamente por un Evaluator independiente.

Una clase de consecuencia solo podrá convertirse en V_j si su ficha §224 establece:
1. constructo y frontera frente a F*, O-CONF, accesibilidad, trayectoria, ejecución y otras V_k;
2. relación con Need_preZ y con la entidad B1/UE correspondiente;
3. perspectiva B1 y autoridad/regla de valoración;
4. fuente/instrumento independiente, evidencia y provenance;
5. unidad, escala, dirección, baseline, horizonte y ventana;
6. regla de adjudicación, casos limítrofes, ausencia, unknown, disputa y censura;
7. validez, fiabilidad, error, acuerdo, invariancia y sensibilidad (P182);
8. trade-offs con otras dimensiones, sin pesos ni compensación por defecto (P179);
9. mecanismo causal y estimando por resultado/dimensión, con vías directas/colaterales (P183 y PC).

No se selecciona ninguna dimensión histórica (eficiencia, calidad, acceso, robustez, sostenibilidad) por defecto. Tampoco se crea un índice escalar. ΔT_acc*, Reach, ejecución, O-CONF, logs, CPU/RAM, consumo de recursos o coste técnico no son Value ni proxies automáticos.

## 8. Relación con Outcome, petición y horizonte

Se conservan tres resultados distintos:
- **Outcome técnico:** resultado del servicio/proceso, con O-CONF como candidato no operacionalizado;
- **Beneficiary_consequence:** cambio en la situación de B1 respecto de Need_preZ;
- **Value V_j:** valoración de esa consecuencia conforme a perspectiva y regla ex ante.

La oportunidad estandarizada permite comparar el servicio bajo un estímulo común, pero no prueba demanda natural ni la satisfacción de una necesidad real. Request_attempt/received/admitted/processing/response son eventos distintos; ninguno adjudica por sí solo Beneficiary_consequence.

El horizonte de valoración debe permitir que la consecuencia ocurra y sea observada, pero no se identifica con H=3 (profundidad transformacional candidata) ni se asigna automáticamente a t9. La ancla temporal, duración, ventana de respuesta y horizonte de consecuencia permanecen OPEN y deben reconciliarse con el reloj t−1/t0…t9 sin añadir un reloj incompatible.

## 9. Dictamen de factibilidad y dependencias abiertas

| Componente | Resultado del ciclo |
|---|---|
| Microdominio | Migración de configuración entre entornos software, aceptado |
| Tipo B1 | Entidad solicitante-beneficiaria sintética, aceptado |
| Cardinalidad B1/UE | Una por UE, aceptada como decisión de diseño |
| Servicio | Instancia lógica por UE bajo contrato/plantilla común, identidad material pendiente |
| Oportunidad | Una estandarizada por UE, aceptada como diseño candidato |
| Need_preZ | Definición semántica; contenido/operación focal OPEN |
| Consecuencia B1 | Envolvente contextual formulada; instancia/medida OPEN |
| Perspectiva | B1 como referente, aceptada como base |
| Autoridad de valoración | OPEN |
| Dimensiones V_j/k | Ninguna seleccionada |
| Instrumentos/escalas/fuentes | OPEN |
| Outcome O-CONF | Candidato técnico; no operacionalizado |
| Horizonte | OPEN; no confundir con H=3 |
| Causalidad C1–C4 | ITT por resultado/dimensión separado; identificación no establecida |

**Bloqueos materiales independientes:** el roster UE, IAM/C_SRC observado, snapshots comparables, inventario B-M01…15, grafo transitivo, provisión real, no-afectación de alternativas, mecanismo/probabilidades de asignación y soporte siguen ausentes o no demostrados en PB-MAT/PA/D2. Este documento no los reemplaza ni permite pasar G-MAT.

## 10. Siguiente decisión mínima y ruta de cierre

La única decisión sustantiva que debe solicitarse antes de concretar el caso es el contenido de la operación basal de B1. La formulación candidata de §4 puede aceptarse como estructura, pero requiere nombrar qué operación de servicio pretende sostener B1 en el entorno de destino. Sin ese objeto, no es científicamente válido seleccionar una consecuencia ni una dimensión V_j.

Una vez resuelto ese punto, la secuencia es:
1. completar la definición de Need_preZ y su regla truth/observación pre-Z;
2. derivar consecuencias potenciales y adversariales para B1 sin seleccionarlas por conveniencia;
3. identificar qué consecuencias tienen criterio valorativo legítimo desde B1;
4. decidir qué clases merecen ficha V_j §224, sin forzar un número;
5. completar fuente, instrumento, escala, baseline, horizonte, adjudicación y P182/P183;
6. reconciliar DAG y estimandos por dimensión con PC y la factibilidad D2;
7. solo entonces reevaluar G-SCI/G-MAT/G-TEST y Design Freeze.

## 11. No-regresión y autorización

Este ciclo desarrolla el caso semántico de B1 sin alterar DEC-C10-095, DEC-C10-051, decisiones B1 aceptadas, D2, población, F*, Opción A, TGCV Core, RMA, Evidence→Claim Matrix, STATUS o claims. No crea dimensiones, medidas, parámetros, decisiones científicas ni IDs de pruebas.

No autoriza captura/materialización, schema físico, fixtures, implementación, generación de datos, simulación, estimación, Design Freeze o ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.


## 12. Aceptación de la clase de propósito basal B1 y cierre parcial de Need_preZ (2026-11-11)

Se registra la aceptación expresa de la siguiente formulación como **clase de propósito operativo basal** de B1:

> B1 tiene un objetivo operativo basal consistente en mantener operativa una función de servicio que depende de la configuración que se migra al entorno de destino.

La aceptación resuelve la objeción semántica anterior sobre la relación entre B1, la configuración migrada y el servicio: el propósito de B1 no es «instalar el adaptador», «abrir τ2» ni «completar F1/F2»; es sostener una función de servicio dependiente de la configuración en destino. No obstante, **la función/operación concreta aún no está nombrada**. Por tanto, esta formulación no es todavía una instancia completa de Need_preZ ni puede cargarse como truth concreta de un DGP confirmatorio.

### 12.1 Definición estructural vigente

`Need_preZ` representa la existencia, antes de Z, de ese propósito operativo basal de B1, especificado sin referencia a la asignación, provisión, accesibilidad, petición, procesamiento, Outcome o consecuencia post-Z. La unidad de referencia sigue siendo B1/UE, con una B1 por UE conforme a la decisión aceptada.

- `1`: el objetivo basal concreto, una vez nombrado y versionado, forma parte de la verdad pre-Z de B1.
- `0`: ese objetivo basal concreto no existe para B1 según la definición del DGP.
- `?`: su existencia o clasificación no está determinada por la verdad disponible o no puede adjudicarse; no equivale a 0.

La clase de propósito aceptada no autoriza a asignar automáticamente `Need_preZ=1` a todas las UE. La pertenencia de cada unidad y el roster de verdad del DGP requieren una especificación basal concreta, versionada y pre-Z. La evidencia observada sobre Need_preZ se conserva separada de truth_dgp; falta de evidencia, ausencia de Request_event o falta de procesamiento no demuestran `Need_preZ=0`.

### 12.2 Regla de no circularidad y elegibilidad

La clasificación de Need_preZ y cualquier regla de elegibilidad asociada se fijan antes de Z. No se permite:
- inferir necesidad a partir de la asignación a D2, la programación o la provisión;
- inferirla de C_dep*, A_f*, D_f*, ΔT_acc*, Reach o existencia de una ruta;
- inferirla de la oportunidad estandarizada, Request_attempt/received/admitted, procesamiento o respuesta;
- excluir de la población ITT unidades por no solicitar, no recibir, no procesar, no seleccionar o no ejecutar;
- recodificar ausencia, unknown, censura o falta de evidencia como cero.

`E_req_preZ`, elegibilidad experimental, demanda de recursos `D_resource` y `Request_event` siguen siendo objetos distintos. Los casos `Need_preZ=0` y `Need_preZ=?` se conservan para los análisis de límites/controles/adversariales que el diseño justifique; no se incorporan ni excluyen automáticamente del estimando de Value sin una regla poblacional ex ante.

### 12.3 Consecuencias potenciales para B1: estructura, no dimensiones

Para cada estado de Need_preZ, el DGP deberá poder representar la consecuencia de B1 respecto del propósito basal, separada del proceso técnico:

- si `Need_preZ=1`, la consecuencia expresa si y cómo cambia la capacidad de sostener la función concreta, incluyendo no logro, interrupción, degradación o recuperación;
- si `Need_preZ=0`, no se presume una consecuencia beneficiosa por el mero éxito técnico; el caso puede servir como control negativo/adversarial si la pregunta y el estimando lo permiten;
- si `Need_preZ=?`, la consecuencia/valoración no se fuerza a una categoría definida: la incertidumbre basal debe propagarse conforme a las reglas de ausencia, unknown y sensibilidad.

La envolvente de §5 se mantiene como repertorio analítico no exhaustivo (logro/progreso; continuidad/interrupción/degradación; demora/pérdida de oportunidad; esfuerzo de recuperación; riesgo/reversibilidad). No es una selección de V_j, un outcome compuesto, ni una escala. Cada consecuencia potencial deberá definirse respecto de la operación concreta cuando esta se especifique. El proceso de servicio, la respuesta, F*, O-CONF y la consecuencia de B1 permanecen separados; una ruta alternativa puede preservar la función aunque τ2 no sea accesible, y el éxito técnico puede no mejorar la situación de B1.

### 12.4 Qué queda aceptado y qué sigue abierto

| Elemento | Estado tras aceptación |
|---|---|
| Clase de propósito basal B1 | ACCEPTED AS WORKING SEMANTIC BASIS |
| Relación propósito–configuración destino–función de servicio | ACCEPTED AT CLASS LEVEL |
| Operación/función concreta | OPEN — MUST BE NAMED AND VERSIONED |
| Need_preZ truth por UE | OPEN — no roster ni clasificación material |
| Regla estructural 1/0/? y no circularidad | DEFINED DOCUMENTALLY; evidence/adjudication OPEN |
| Consecuencia B1 respecto del propósito | STRUCTURE DEFINED; instance/measure OPEN |
| Autoridad/criterio de valoración | OPEN |
| Dimensiones V_j, escalas e instrumentos | NOT SELECTED / OPEN |
| Horizonte de consecuencia | OPEN; no equivalencia con H=3 ni t9 |
| C1–C4 por Value | NOT IDENTIFIED / NOT EVALUABLE ON CURRENT MATERIAL STATE |

La siguiente dependencia sustantiva es identificar, a partir del contrato funcional/servicio ya existente en el microdominio, la operación concreta que hace operativa esa función. No se debe inventar ahora una operación por conveniencia narrativa ni sustituirla por un predicado técnico de F*. Después podrá cerrarse la especificación de truth_preZ y derivarse la consecuencia candidata sin seleccionar todavía V_j.

Esta aceptación no crea un Decision Record nuevo, no modifica decisiones previas ni autoriza roster, schema físico, fixtures, captura/materialización, implementación, generación de datos, simulación, estimación, Design Freeze o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.

## 13. Resultado de la reconstrucción del contrato de servicio — operación concreta aún no determinada (2026-11-11)

La comprobación histórica del maestro (§§174–178 y §216.2–216.3), DEC-C10-068/069 y el contrato funcional vigente confirma que el servicio sintético se define como **servicio lógico de procesamiento de solicitudes**. Su núcleo aceptado se limita a:
- PAR-SVC-ENABLED: BOOL requerido;
- PAR-SVC-PROFILE: ENUM {STANDARD, READ_ONLY, DISABLED} requerido;
- RUL-SVC-ENABLE-PROFILE-01: ENABLED=true implica PROFILE∈{STANDARD, READ_ONLY}; no se establece la implicación inversa.

Esto permite identificar la clase funcional general del servicio (procesamiento de solicitudes) y su habilitación/perfil. **No especifica qué solicitud se procesa, qué operación realiza sobre la configuración migrada, qué resultado operativo espera B1 ni qué parte de esa operación depende de la configuración de destino.** El nombre REQUEST-PROCESSOR y los parámetros ENABLED/PROFILE no autorizan inferir semántica de negocio, tipo de petición, efecto ni consecuencia para B1.

Por tanto, la reconstrucción histórica no resuelve la operación concreta. No debe sustituirse por «instalar adaptador», «ejecutar F1/F2», «alcanzar SF» ni por una descripción inventada de la petición. El cierre sigue siendo: clase de propósito basal aceptada; clase general de servicio conocida; operación/semántica de petición pendiente. Para completar Need_preZ se necesita especificar qué operación/solicitud del servicio es la que B1 necesita mantener operativa y qué dependencia tiene de la configuración migrada.

**Estado:** SERVICE_CLASS_RECOVERED / REQUEST_SEMANTICS_OPEN / CONCRETE_OPERATION_OPEN / NEED_PREZ_NOT_MATERIALIZED.



## 14. Aceptación de la especialización funcional mínima del servicio B1 (2026-11-11)

Se registra la aceptación expresa del usuario de la especialización funcional mínima propuesta para continuar el cierre de B1. Se integra como **contrato funcional de trabajo**, subordinado a DEC-C10-068 y sin alterar su núcleo constitutivo.

### 14.1 Función aceptada a nivel de trabajo

- **Entrada:** una solicitud dirigida a la instancia lógica del servicio por o en representación de B1.
- **Operación mínima:** el servicio comprueba el estado declarativo de habilitación de la instancia en destino y, cuando está habilitado, puede aceptar solicitudes; cuando no está habilitado, no las acepta.
- **Perfil:** el servicio expone el perfil operativo declarado por `PAR-SVC-PROFILE`. No se atribuye todavía semántica de negocio diferenciada a STANDARD frente a READ_ONLY, más allá de que ambos son perfiles compatibles con ENABLED=true según RUL-SVC-ENABLE-PROFILE-01.
- **Salida inmediata:** estado de admisión/no admisión de la solicitud. Este evento no equivale a procesamiento completado, respuesta, operación de negocio realizada, satisfacción de Need_preZ, Beneficiary_consequence ni Value.

Esta especialización concreta la clase de servicio ya aceptada —procesamiento de solicitudes— mediante una puerta mínima de admisión vinculada al estado declarativo en destino. No define el contenido de la solicitud ni el procesamiento posterior. Tampoco añade una regla constitutiva nueva ni convierte la descripción de trabajo en prueba de comportamiento implementado.

### 14.2 Límites semánticos y técnicos

1. `PAR-SVC-ENABLED` informa la habilitación declarada; la observación de admisión debe seguir siendo un evento distinto y requerirá evidencia propia cuando se operacionalice.
2. `PAR-SVC-PROFILE` se expone como perfil declarado. No se inventan capacidades, permisos, efectos ni diferencias funcionales entre STANDARD y READ_ONLY.
3. No se establece que una solicitud admitida se procese con éxito, produzca una respuesta, ejecute una transformación o alcance SF.
4. No se establece que la operación consista en instalar adaptadores, ejecutar F1/F2, modificar la configuración ni aplicar una regla de configuración.
5. La oportunidad estandarizada sigue siendo un probe común post-snapshot; no acredita demanda natural ni define por sí sola Need_preZ.
6. La admisión, el procesamiento, la respuesta, O-CONF/F*, la consecuencia B1 y Value permanecen separados.

### 14.3 Consecuencia para Need_preZ

La clase de propósito basal aceptada se especializa así, a nivel de trabajo:

> Antes de Z, B1 tiene el objetivo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

Esta formulación puede estructurar el contenido funcional de `Need_preZ`, pero **no asigna automáticamente `Need_preZ=1` a todas las UE**. La verdad por unidad, su versión, los criterios de pertenencia y la evidencia observada deben fijarse antes de Z. Se mantienen los estados 1/0/? y la separación truth_dgp/observed_evidence.

La consecuencia basal para B1 puede ahora referirse a la disponibilidad de la capacidad de admisión que constituye su objetivo, sin equiparar admisión puntual con mantenimiento efectivo de la función ni con logro del propósito. La continuidad, interrupción, degradación, demora, recuperación y riesgo siguen siendo clases analíticas candidatas, no dimensiones V_j.

### 14.4 Estado y siguiente dependencia

| Elemento | Estado |
|---|---|
| Clase de propósito B1 | ACCEPTED |
| Servicio lógico de procesamiento de solicitudes | ACCEPTED por DEC-C10-068 |
| Especialización mínima: admitir según ENABLED y exponer PROFILE | ACCEPTED AS WORKING FUNCTIONAL CONTRACT |
| Semántica diferenciada de STANDARD/READ_ONLY | OPEN |
| Contenido y procesamiento posterior de la solicitud | OPEN |
| Need_preZ truth por UE y adjudicación observada | OPEN |
| Consecuencia B1 concreta, autoridad y horizonte | OPEN |
| Dimensiones, escalas e instrumentos Value | NO SELECCIONAN |
| DGP, implementación y ejecución | NO AUTORIZADOS |

**Siguiente trabajo:** cerrar de forma integrada la ficha pre-Z por UE (verdad, evidencia, adjudicación y unknown), las consecuencias potenciales correspondientes y las reglas de separación respecto de admisión/procesamiento/Outcome. Si para ello se necesita semántica adicional de STANDARD/READ_ONLY o del procesamiento posterior, se tratará como dependencia explícita y no se inferirá.

No se crea un Decision Record nuevo ni se modifica DEC-C10-068. No se autoriza roster, schema físico, fixtures, captura/materialización, implementación, generación de datos, simulación, estimación, Design Freeze o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## 15. Reconciliación integrada de Need_preZ y consecuencias B1 (2026-11-11)

La definición funcional de trabajo, las reglas de adjudicación 1/0/? y la envolvente de consecuencias se desarrollan de forma integrada en `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`.

Este artefacto tiene precedencia para la especificación documental de Need_preZ y sus reglas de evidencia. Actualiza la lectura de §13: la operación mínima de servicio ya no permanece completamente abierta, pues el usuario aceptó como contrato de trabajo la admisión conforme a ENABLED y la exposición de PROFILE. Siguen abiertos el contenido de la solicitud, el procesamiento posterior y la semántica diferenciada de STANDARD/READ_ONLY.

El cierre es documental, no material: no hay roster ni evidencia observada por UE con cobertura demostrada. La consecuencia B1 está estructurada, pero no medida ni valorada. No se seleccionan dimensiones V_j ni horizonte. No se modifica DEC-C10-068, no se congela el DGP ni se autoriza implementación o ejecución.


## 13. Precedencia del contrato funcional B1 y su relación con V_cont (2026-11-12)

La formulación de §4 que describía la operación concreta como todavía no identificada queda precisada por el contrato B1 de Need_preZ, versión vigente, §2: el objetivo es mantener disponible en destino un servicio capaz de admitir solicitudes conforme al estado declarativo ENABLED y exponer el PROFILE operativo declarado. La función del servicio, por tanto, sí está definida a nivel del contrato sintético. Puede permanecer abstracto el contenido de negocio de la solicitud o el contenido específico del perfil; no se añade otra operación para cerrar el constructo.

La truth de V_cont se refiere al cumplimiento temporal de esa función (admisión cuando ENABLED=true, no admisión cuando ENABLED=false, y exposición del PROFILE aplicable), no a la existencia de Need_preZ, la ocurrencia de la oportunidad estandarizada ni su resultado. La selección provisional de V_cont se rige por DEC-C10-099. Su medición S3 y los límites de identificación se rigen por el plan §16.182; la frontera y los contrastes frente a F*/O-CONF se rigen por §16.183.

Esta precisión supera el estado histórico NEED_CONTENT_OPEN solo en cuanto a la función de servicio definida. No instancia perfiles materiales, roster, solicitud de negocio, instrumento, agregación, ventana, O-CONF ni criterio final de valoración. Se mantiene `V_CONT_SELECTED_PROVISIONALLY / FUNCTIONAL_REFERENCE_SPECIFIED / MEASUREMENT_CONDITIONAL / O_CONF_NOT_OPERATIONALIZED / NO_DESIGN_FREEZE`.
