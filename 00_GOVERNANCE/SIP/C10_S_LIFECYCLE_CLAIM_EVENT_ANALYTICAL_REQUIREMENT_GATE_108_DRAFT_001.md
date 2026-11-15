# C10-S — Gate 108: necesidad analítica de identidad claim/event y unidad de observación

**Estado:** HISTORICAL RECONSTRUCTION COMPLETED / D2 AND B1 ESTIMAND REQUIREMENTS MAPPED / UNIT-OF-OBSERVATION LEVELS DISTINGUISHED / GLOBAL CLAIM ID NOT JUSTIFIED / EVENT ID CONDITIONALLY REQUIRED FOR EPISODE-LEVEL OPERATIONS / PHYSICAL UNIT MAPPING OPEN / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Precedencia:** README/bootstrap de main; DEC-C10-066/067/069/070/071/083/088/095/099/100/101/102; C10-S master §§277–289; Plan Draft 004 §§16.185, 16.188, 16.199–16.200 y 16.253–16.257; DGP Temporal and Role Contract §§2–8, 14–29 y 48–59; Gates 94–107; U_G Inventory Register Template y U_G Evidence/Provenance/Adjudication Protocol. No modifica DEC ni contratos aceptados.

---

## 1. Pregunta y alcance

Gate 108 determina qué operaciones científicas del diseño C10-S requieren:
- identidad de una afirmación lifecycle compartida por varias evidencias (claim_id/claim_group_id);
- identidad de una ocurrencia runtime/procedimental (event_id);
- una afirmación agregada por unidad y ventana, sin normalizar episodios;
- o únicamente el vínculo probatorio existente (claim_evidence_id).

El gate también distingue la unidad causal/experimental, la unidad de asignación, la unidad lógica U_G, el objeto NODE versionado, el episodio y el intervalo de agregación. No se presume que sean la misma unidad.

**Límite:** se evalúa necesidad analítica documental; no se selecciona un esquema físico ni se aprueba PROCESS_EVENT, una ampliación de DEC-C10-061, un claim_id o nuevas columnas.

## 2. Fuentes y reconstrucción histórica

Se recuperaron:
1. 00_GOVERNANCE/README.md y STATUS.md en main, junto con los punteros canónicos a RMA v3.38, Evidence→Claim Matrix v1.47 y trazabilidad v3.38.
2. C10-S master Draft 004 §§277–289, con precedencia reciente para V_cont, O-CONF, reloj temporal, D2, q_X* y ΔX*.
3. Plan integrado Draft 004 §§16.185, 16.188, 16.199–16.200 y Gates 90–107 (§§16.240–16.257).
4. DGP Temporal and Role Contract, en especial la secuencia t−1…t9, estimandos, truth/observed, ausencia, unidad/interferencia, D2 y B1.
5. Gate 107 y la plantilla/protocolo U_G para claims, evidencia, evaluación y adjudicación.

La reconstrucción confirma una limitación sustantiva: la cadena causal D2 todavía no está materializada en el harness; Gate 92 identificó ITT-Z y ITT-G como estimadores actuales del Analyzer, sin etapas D2 ni θ_A materializados. Gates 90–91 confirmaron cobertura C1 parcial y C3 no materializada. Gate 108 no atribuye capacidades ejecutables a un contrato de diseño.

## 3. Jerarquía de objetos y unidades

| Nivel | Unidad o identidad | Función analítica | Estado |
|---|---|---|---|
| Mundo sintético | world_id/versión y funciones estructurales compartidas | Define DGP, potenciales y mecanismos | Esquema conceptual; cardinalidades/parametrización abiertas |
| Unidad experimental (UE) | Índice i del DGP | Unidad sobre la que se definen potenciales, elegibilidad y resultados | Conceptual; clave física abierta |
| Unidad de asignación (UA) | Unidad o clúster que recibe Z | Determina aleatorización, inferencia e interferencia | OPEN; no asumir UE=UA |
| Unidad lógica U_G | unit_id = NODE.node_id | Servicio lógico dentro de la frontera U_G | Definida estructuralmente |
| Revisión exacta de unidad | unit_object_record_id/object_record_id y object_version; snapshot exacto cuando aplique | Fija la versión estructural a la que se refiere el claim | Contrato documental; matching DGP→U_G OPEN |
| Instancia/entorno | instance_id + versión, cuando el contrato aplica | Contexto de realización técnica | No sustituye UE, UA ni unit_id |
| Ocurrencia | event_id propuesto en Gate 98; revisión de registro separada | Identifica un episodio individual y sus correcciones | No implementado; PROCESS_EVENT no aceptado |
| Claim | Identidad semántica de una proposición | Agrupa una proposición entre fuentes/revisiones si el análisis lo necesita | No existe clave claim-level aprobada |
| Vínculo claim-evidence | claim_evidence_id | Identifica una relación concreta entre claim textual, target y evidence | Definido en plantilla; no es claim_id ni event_id |
| Intervalo B1 | (UE i, k) dentro de la rejilla común [t0,T*] | Unidad de adjudicación funcional de A_B1 | DEC-C10-100/102; K/Δ/ventana aún abiertos |
| Ruta O-CONF | (instancia, route_id) | Unidad de adjudicación terminal F* | DEC-C10-083…088 y master §279; contrato parcialmente operacionalizado |

**Regla:** una unidad de resultado por UE no implica que todas las observaciones/episodios sean una fila por UE. Los snapshots, claims, vínculos de evidencia, eventos e intervalos tienen granularidades propias.

## 4. Estimandos y variables que realmente consume el diseño

### 4.1 Efectos de asignación D2

El escenario primario candidato D2 conserva potenciales separados por etapa:

Z → B_gZ → W_programmed → W_attempt → receipt → S_install → C_dep* → A_f*/D_f* → T_acc*/ΔT_acc* → Reach/Π → K/Consider → Sel/Start → Exec → O-CONF / V_cont.

- Z asigna política D2; W_programmed(z)=z es la única función de etapa fijada explícitamente en el master §289.
- Intento efectivo, recepción, instalación, componentes y éxito conjunto, accesibilidad, cambio transformacional, Reach y etapas downstream no heredan éxito ni tasas por defecto.
- El ITT D2 es efecto total del paquete por resultado. El mapping D2→g_A no está demostrado.
- θ_A(q) y g_A1/g_A0 sobre distribuciones factibles de ΔT_acc* son una pregunta distinta; no se deducen del ITT D2.
- El LATE focal de apertura D_f* solo se considera bajo sus supuestos IV y población de apertura; no se identifica por registrar eventos.

Las variables de etapa son necesarias para reconstruir mecanismos, comprobar exclusión/contaminación, medir primeras etapas y clasificar identificación, pero no todas son estimandos primarios por sí mismas.

### 4.2 Outcome terminal O-CONF

O-CONF adjudica el criterio terminal de ruta completa F*, con unidad (instancia × route_id) anclada en la aplicación final F2/A2 según DEC-C10-083…088. Es un resultado terminal distinto de V_cont, no un evento de ejecución ni una afirmación lifecycle genérica de NODE.

Su unidad exige identidad de instancia y versión, route_id y definición F* versionada, ancla terminal y evidencia de aplicación/post-check, predicados FP-01…07 con regla no compensatoria y FP-08 separado, snapshot/binding exacto cuando aplique, cobertura y adjudicación 1/0/?.

No requiere contar cada INVOKED/EXECUTED salvo que una regla FP concreta o la auditoría de secuencia lo exija. La tabla O-CONF no debe convertirse en ledger de eventos.

### 4.3 Value temporal V_cont

Por DEC-C10-099/100/101/102:
- V_cont es la dimensión mínima provisional de Value para la extensión sintética B; no equivale a O-CONF, Outcome técnico, uptime exacto ni ΔT_acc.
- V_cont_truth(i) es la fracción de intervalos de igual duración dentro de una rejilla/ventana post-Z común en los que se cumple íntegramente B1.
- Cada intervalo se adjudica por A_B1(i,k). UNKNOWN se conserva y propaga a bounds [n1/K,(n1+n?)/K]; no se imputa cero ni se elimina del denominador.
- La ventana comienza en t0 e incluye provisión/instalación. Cualquier incumplimiento funcional confirmado afecta todos los intervalos intersectados; no hay gracia ni duración funcional mínima.
- Truth se genera a partir de transiciones/estados funcionales; S3 es un canal pasivo imperfecto posterior, no truth ni una media sustitutiva.
- K, Δ, ventana, frecuencia, soporte de transiciones, T*, τ_follow, calibración S3, error y punto confirmatorio siguen OPEN.

**Implicación:** para calcular truth V_cont, el generador necesita conservar internamente la identidad y temporalidad de cada transición que cambia A_B1, o una representación funcional equivalente que permita derivar sin ambigüedad los intervalos afectados. Eso no obliga a crear una tabla U_G PROCESS_EVENT ni a exponer esas identidades al Analyzer. Para recuperar V_cont desde observaciones S3, el canal debe permitir localizar y ordenar episodios relevantes con reloj comparable y límites de cobertura; si no, Analyzer entrega bounds/abstención.

## 5. Matriz variable × unidad × granularidad × identidad

| Variable/constructo | Papel | Unidad analítica requerida | Granularidad temporal | Identidad mínima necesaria | ¿claim_id/event_id? |
|---|---|---|---|---|---|
| Z | Asignación causal | UA; potenciales por UE con mapping explícito | t0 | Identidad/versionado del mecanismo/vector Z y binding UE→UA | No event_id por el valor Z; sí ocurrencia Z_ASSIGNED solo si se necesita auditar el acto individual |
| B_assigned/offered/received | Política y cumplimiento | UE (y destinatario/instancia cuando corresponda) | t1; estados separados | policy_contract_id + policy_version; versión ofrecida/recibida; evidencia de recepción | No claim_id global; event_id solo si se analiza el acto individual de recepción/vinculación |
| W_programmed | Prescripción de política | UE por asignación | t1/tiempo programado | Política/version y UE/UA; scheduled_time si es ocurrencia individual | No event_id obligatorio si deriva determinísticamente de la política; sí si múltiples programaciones/reeschedules son objeto |
| W_attempt | Intento efectivo | UE × intento | event_time; reintentos distintos | Identidad de intento, actor, versión, unidad y relación con Z/B | event_id requerido si contar/deduplicar/reintentar/enlazar episodios; no si solo se conserva un estado agregado por UE/ventana |
| receipt | Recepción material | UE × entrega/recepción | received/event_time | Identidad de entrega/recepción y artefacto/versión/destino | event_id condicional a múltiples entregas, reintentos, orden o auditoría por episodio |
| S_install | Acto/resultado de instalación | UE × intento/instancia técnica | event_time y estado post | Identidad de intento/instalación; versión del artefacto y destino | event_id condicional si hay múltiples intentos, rollback, instalación parcial o secuencia |
| C_install, C_integrity, C_compat, C_oper | Predicados de verificación | UE × dependencia/componente × versión/scope | t2 / snapshot de verificación | target NODE exacto, regla y scope; evidencia individual por predicado | Claim de estado por vínculo puede bastar para una fuente; claim_id solo si varias fuentes se agrupan como una proposición |
| C_dep* | Constructo compuesto derivado | UE × dependencia focal | t2/post; 1/0/? | Identidad de los componentes y regla de conjunción versionada | No event_id por el constructo; eventos subyacentes solo si análisis de episodios lo requiere |
| A_f,base*, A_f,post*, D_f* | Accesibilidad focal y apertura basal→post | UE × τ2 × frontera/versión | Basal pre-Z y post provisión antes de K/Sel/Exec | NODE/estructura y snapshots pre/post exactos; fórmula/predicados; matching de unidad | Claim de estado por vínculo puede bastar para fuente única; no event_id. Claim compartido si se agregan varias evidencias |
| A_f,obs | Estimación observada de accesibilidad | UE × τ2 × scope observado | t3 | Evidencia, cobertura, snapshot y regla/versión | No event_id salvo que la observación sea una serie de episodios; claim identity condicional |
| T_acc, ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*) | Estado/cambio transformacional | UE × frontera/versiones y objetos/relaciones | snapshots pre/post comparables | NODE/EDGE/ROUTE y snapshot exacto; reglas/matching; ΔE_T separado | No event_id por el cambio agregado; cada transformación concreta puede tener TID/SID/RID/EID según contrato, no un event_id genérico |
| Reach_H, Π_H | Alcanzabilidad y trayectorias candidatas | UE × estado inicial × objetivo × horizonte H | derivado de t3 y profundidad k=1…H | grafo/route_id, reglas, horizonte y versión exactos | No event_id; rutas son estructuras/posibilidades, no episodios ejecutados |
| K, Consider | Conocimiento/consideración | UE × agente × posibilidad | t5 / ventana | Identidad de agente, posibilidad y observación/medición | Event_id solo si el proceso se modela como episodios temporales; no exigido por estimandos actuales |
| Sel, Start | Selección e inicio | UE × agente × ruta/posibilidad | t6; instante/ventana | Ruta seleccionada e inicio identificable; actor/tiempo | Event_id si interesa secuencia/reintentos o conteo; estado agregado basta si el estimando solo usa cualquier inicio por UE |
| Exec_partial, Exec_complete, Interrupt, Fail, End_reason | Ejecución longitudinal | UE × route_id × episodio/attempt | t7 y episodios; orden y duración | Identidad de episodio/ejecución y ruta, actor, tiempos, resultado | Event_id requerido para contar, secuenciar, enlazar interrupción/reintento y evaluar por episodio; no requerido para indicador terminal agregado si la fuente soporta el claim y no se analiza multiplicidad |
| O-CONF | Outcome terminal técnico F* | Instancia × route_id | terminal/post-check | instance/version, route_id, F* rule/version, ancla terminal y evidencia | No event_id por resultado; se referencia el acto terminal/snapshot exacto si corresponde |
| A_B1(i,k) | Estado funcional por intervalo | UE × intervalo k | Cada bloque igual dentro de [t0,T*] | UE, límites del intervalo, regla B1 y estado funcional truth/observado | No claim_id global; event_id interno de transición necesario cuando transiciones determinan intervalos afectados; no exige PROCESS_EVENT U_G |
| V_cont_truth(i) | Value temporal | UE | Agregación sobre K intervalos | UE, rejilla/ventana común, K, vector A_B1 y regla DEC-C10-100/102 | No event_id como unidad de estimando; requiere identidad de transiciones en el generador o equivalente determinista |
| V_cont_obs(i) / S3 | Evidencia observacional de Value | UE × canal × componente × tiempo/captura | Serie S3 en ventana; lag/pérdida/fase | source/evidence id y versión, locator, clock domain, capture/observation metadata y coverage | event_id/episode locator si logs/trazas reconstruyen episodios; si snapshots/métricas agregadas, claim por ventana y bounds según calibración |
| R_j / missingness | Observabilidad por bloque | UE × bloque/variable × ventana | Tiempo de ausencia y recuperación | Código de motivo, fuente, momento, recuperabilidad y scope | No claim_id/event_id por sí mismos; evento de pérdida solo si el DGP lo modela como episodio |
| F* / predicados FP-01…08 | Regla de conformidad | Instancia × ruta × etapa/objeto | pasos de ruta y terminal | predicate/rule version, route_id, target exacto, snapshot/evidence | No claim_id global salvo agregación de múltiples fuentes; no event_id salvo necesidad de secuencia de actos |
| DECLARED | Estado de declaración | NODE exacto × versión/ámbito | Basal o vigencia documental | object_record_id/version, scope, fuente/versión | Claim documental por vínculo; no event_id |
| INSTALLED | Estado técnico de instalación | NODE/artefacto exacto × instancia/destino | t2 / valid-time | objeto/versión, destino, snapshot/evidence | Claim documental por vínculo para estado; event_id si se estudian intentos de instalación individuales |
| DEPLOYED | Estado de despliegue | NODE exacto × instancia/entorno | intervalo de despliegue | objeto/versión, entorno, scope, snapshot/evidence | Claim documental por vínculo; event_id si interesa cada despliegue/rollback |
| LOADED | Estado o episodio de carga, según fuente | NODE/instancia × ventana o episodio | Estado por ventana o event_time | fuente/localizador y definición explícita de estado vs carga individual | OPEN; event_id solo si episodio/multiplicidad es unidad |
| INVOKED | Ocurrencia de invocación | NODE/operación × invocación | event_time | episodio/invocación, actor/correlación/resultado | event_id si se cuenta, deduplica, correlaciona o enlaza con ejecución |
| EXECUTED | Ocurrencia/episodio de ejecución | NODE/operación × ejecución | event_time/intervalo | episodio, actor, ruta/operación, correlación, resultado | event_id si se analiza por episodio; estado agregado por ventana si solo interesa existencia y cobertura adecuada |

La matriz no crea una taxonomía de campos ni autoriza materialización. “Event_id interno” en truth DGP no equivale a aceptar el registro U_G PROCESS_EVENT.

## 6. Resultados por necesidad analítica

### 6.1 Identidad de claim

**No se justifica un claim_id global para todas las dimensiones lifecycle.**

La necesidad se activa solo si una operación requiere que varias filas CLAIM_EVIDENCE_LINK sean tratadas como la misma proposición a través de varias fuentes, revisiones o ventanas, y que evaluación/adjudicación opere sobre ese conjunto como unidad única. En ese caso la igualdad textual de claim_statement/relevance_scope no basta; se requiere identidad compartida y semántica de versión/scope, o mantener la adjudicación OPEN.

Para un claim de estado con una sola fuente/paquete exacto, Gate 107 permite documentación condicional mediante un vínculo por proposición, NODE/revisión, dimensión, scope/ventana y evaluación alineada. No convierte la ruta a adjudicación en exclusividad claim-target ni en validación física.

**Regla de decisión:** no añadir claim_id/type/revision salvo que el contrato de análisis requiera una operación multi-evidencia/versionada que no pueda realizarse de forma inequívoca con los vínculos existentes. No fusionar por texto repetido. Si la identidad compartida es necesaria y no existe, no adjudicar el agregado; emitir OPEN/UNKNOWN.

### 6.2 Identidad de evento

**No se justifica event_id para todo estado o toda fila de evidencia.** Se requiere identidad de episodio cuando el análisis necesita contar ocurrencias distintas, distinguir reintentos/duplicados/fallos parciales/rollback, enlazar programación-intento-recepción-instalación-resultado, correlacionar invocación con ejecución, ordenar transiciones, medir duración/interrupción/recuperación/censura o evaluar verdad por episodio.

Si el estimando solo requiere un estado por UE/ventana (por ejemplo, existencia de al menos una invocación en una ventana), puede usarse un claim agregado sobre NODE con fuente S3, localizador, cobertura y limitaciones explícitas. Si la cobertura no permite sostener 1 o 0, mantener ?/bounds/abstención. La agregación no puede ocultar episodios múltiples cuando estos cambian la clasificación o la temporalidad.

Para V_cont, el generador necesita identidad interna o una función de transición equivalente para determinar qué intervalos quedan afectados; el estimando final sigue siendo por UE. En observación, logs/trazas episódicos requieren localizador y temporalidad recuperables; un snapshot/métrica agregada puede apoyar el estado por ventana si la calibración S3 permite identificarlo. Ninguna de estas condiciones aprueba PROCESS_EVENT en U_G.

### 6.3 Unidad experimental y mapping U_G

La unidad de potenciales y resultados es UE i en el DGP. La unidad de asignación puede ser UA o cluster; interferencia y exposición deben resolverse antes de inferencia. U_G unit_id identifica una unidad lógica raíz LOGICAL_SERVICE_UNIT, y unit_object_record_id su revisión exacta. No está demostrado UE=UA=U_G unit. El mapping DGP→U_G queda OPEN.

No se deben utilizar unit_id como PK de asignación, object_record_id como identidad de UE, ni instance_id como sustituto de clúster. El mismo NODE puede tener múltiples revisiones, instancias, entornos o ejecuciones.

## 7. Dictamen por variable y suficiencia del esquema actual

| Requisito | Conclusión Gate 108 |
|---|---|
| ITT-Z por resultado | Requiere asignación/versionado y outcome por UE/UA; no exige claim_id ni event_id genérico |
| Primera etapa de W/C_dep/A_f/D_f | Requiere estado por UE y tiempos/versión; eventos individuales solo si intento/recepción/reintentos se analizan como episodios |
| LATE_f | Requiere D_f y supuestos IV; identidad de episodio no sustituye medición de tratamiento ni identificación |
| θ_A(q) / g_A | No materializado; requiere contraste de políticas sobre ΔT_acc* completo, q_X*, soporte y vías; no se obtiene normalizando eventos |
| Reach/Π_H | Requiere grafo/rutas/reglas/snapshot y horizonte; no event_id |
| O-CONF | Requiere instancia × route_id y adjudicación terminal; no event_id salvo reglas de secuencia |
| V_cont | Resultado por UE a partir de K intervalos; identidad de transiciones en truth y evidencia S3 temporalmente identificable, sin exigir tabla PROCESS_EVENT |
| Claims de estado lifecycle | Un vínculo por proposición/fuente puede bastar documentalmente; claim_id solo si se agrupan varias fuentes/revisiones |
| INVOKED/EXECUTED por episodio | event_id necesario si hay conteo, correlación, secuencia, retries o adjudicación episódica |
| Ausencia/cobertura | C0 y COVERAGE_REGISTER exactos; ausencia de evento no equivale a evento 0 ni se crea scope artificial |

**Resultado global:** el diseño actual no requiere una identidad claim-level universal ni una tabla de eventos universal para producir sus estimandos finales por unidad. Sí requiere granularidad intermedia por etapa y ventana, y requiere identidad episódica en aquellos mecanismos donde multiplicidad, orden, duración, retry o transición cambian la verdad/medición. La implementación física permanece bloqueada por los gates y decisiones correspondientes.

## 8. Decisiones y límites

1. No aprobar claim_id, claim_group_id, claim_type ni claim_revision.
2. No aprobar event_id/PROCESS_EVENT como esquema U_G; Gate 98 sigue candidato y DEC-C10-061 intacta.
3. Reconocer claim_evidence_id solo como identidad de vínculo claim-evidence.
4. Mantener una afirmación lifecycle por vínculo cuando se use la convención documental Gate 107.
5. No agrupar varias evidencias por igualdad textual; sin identidad común necesaria, mantener OPEN.
6. Para operaciones episódicas, exigir identidad interna/locator estable, pero decidir su representación física en un gate posterior solo si la operación científica concreta lo necesita.
7. Para V_cont, preservar transiciones internas truth y S3 observado; no confundir identidad de transición con unidad de estimando.
8. Mantener separadas UE, UA/cluster, unit_id, unit_object_record_id, instancia, route_id, evento, claim, vínculo y bloque k.
9. No mapear automáticamente INVOKED/EXECUTED a seis estados NODE ni convertirlos en PREDICATE.
10. C0/DEC-C10-070 y snapshots DEC-C10-065 permanecen intactos.
11. No cambiar DEC-C10-061/067/069/071/083/088/095/099/100/101/102.
12. No crear inventario material, DDL, parser, validator, fixtures, código, tests ni workflows.

## 9. Gaps que permanecen abiertos

| ID | Gap | Estado |
|---|---|---|
| G108-01 | UE→UA/cluster y unidad de inferencia/interferencia | OPEN |
| G108-02 | UE→U_G unit_id / unit_object_record_id | OPEN |
| G108-03 | Identidad física y versionado de vector/mecanismo Z | OPEN |
| G108-04 | Identidad concreta de policy_contract_id/version y artefacto | OPEN |
| G108-05 | Identidad de intento/recepción/instalación para multiplicidad y retry | OPEN; event_id solo si requerido |
| G108-06 | Mapping temporal entre event_time, observed/capture/emission/recorded y clocks | OPEN |
| G108-07 | Identidad de claim común para multi-evidencia/versionado | OPEN; extensión no justificada aún |
| G108-08 | LOADED estado vs episodio | OPEN |
| G108-09 | Definición operativa y uso de INVOKED en estimandos actuales | OPEN; no estimando directo localizado |
| G108-10 | Unidad/episodios EXEC y relación con Exec_partial/complete | OPEN |
| G108-11 | K, Δ, T*, τ_follow, δ_det y calibración S3 de V_cont | OPEN |
| G108-12 | Mapping D2→g_A y estimando θ_A(q) | OPEN / NOT MATERIALIZED |
| G108-13 | Matching de snapshots y cobertura por dimensión lifecycle | OPEN; C0 intacto |
| G108-14 | Validación de cardinalidades/FKs y separación Generator/Analyzer/Evaluator | NOT EXECUTED |

## 10. Siguiente operación

**Gate 109 — cierre del crosswalk unidad experimental–unidad de asignación–unidad lógica U_G–instancia–ruta, con requisitos de interferencia y exposición.**

Recuperar DEC-C10-059/065/069, el contrato de unidad del DGP, la especificación de aleatorización, el inventario de instancias/rutas y las identidades PE/test/fixture. Determinar qué entidades son UE, UA, clúster, unidad lógica U_G e instancia; si existe mapping 1:1, 1:N o N:1; cuál es la unidad de aleatorización, inferencia y exposición; qué estructura de interferencia y potenciales compartidos exige el diseño; qué claves ya existen y cuáles siguen sin valor físico; y qué relación es necesaria para ITT-Z, D_f, O-CONF y V_cont.

No generar identificadores ad hoc ni convertir unit_id en assignment_id. No tocar C0, DEC-C10-061 ni PROCESS_EVENT. Sin implementación ni ejecución.

## 11. Límites y dictamen final

Auditoría documental asistida, no independiente. Los resultados describen requisitos analíticos de los contratos; no validan el harness ni demuestran que las variables estén implementadas, observadas o medidas. No se inspeccionaron registros poblados ni fuentes runtime. No se calcularon estimandos, potencias, tasas, parámetros ni cobertura empírica.

scientific_execution=false; execution_authorized=false.

**Dictamen:** GATE_108_ANALYTICAL_IDENTITY_REQUIREMENTS_MAPPED / GLOBAL_CLAIM_ID_NOT_JUSTIFIED / EVENT_ID_CONDITIONALLY_REQUIRED_FOR_EPISODE_LEVEL_OPERATIONS / UE_UA_UG_UNIT_MAPPING_OPEN / D2_TO_G_A_NOT_ESTABLISHED / V_CONT_TRANSITION_IDENTITY_INTERNAL_REQUIREMENT / C0_UNCHANGED / DECISIONS_UNCHANGED / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_DESIGN_FREEZE.
