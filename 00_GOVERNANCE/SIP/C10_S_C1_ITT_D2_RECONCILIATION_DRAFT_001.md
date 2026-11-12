# C10-S — Reconciliación C1: ITT de asignación D2

**ID:** C10-S-C1-ITT-RECON-001  
**Versión:** Draft 001  
**Fecha:** 2026-11-11  
**Estado:** RECONCILIACIÓN DOCUMENTAL / C1 OPEN / NOT DESIGN-FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Alcance:** primera operación de la secuencia C10-S-CLOSURE-SEQUENCE-001.  
**No autoriza:** Design Freeze, schemas físicos, fixtures, implementación, simulación ni ejecución.

## 1. Dictamen ejecutivo

C1 puede formularse conceptualmente como efecto total de asignación a las dos políticas D2 aceptadas, pero todavía no puede declararse estimando confirmatorio completo ni identificado. La política comparada está mejor definida que la población, la unidad efectiva bajo interferencia, el resultado y el horizonte.

El hallazgo decisivo es que **C1 no tiene un único resultado ya disponible para todo el experimento**:
- En la variante A, el dominio base permite estudiar accesibilidad, Reach, trayectorias y Outcomes técnicos. Value contextual no está instanciado.
- En la variante B, separada y versionada, se podrá estudiar Value solo cuando la instancia B1, su consecuencia, perspectiva y fichas V_j estén materializadas y cumplan P179/P182/P183 y §224.

Por ello el objeto de C1 debe tratarse como una familia de ITT por resultado/dimensión y por variante/población, no como un escalar único ni como un ITT sobre Value supuesto. El presente documento reconcilia el estado y propone una formulación de trabajo; no acepta una nueva población ni cierra el estimando.

## 2. Fuentes reutilizadas y precedencia

| Fuente | Estado/decisión reutilizada | Uso en C1 |
|---|---|---|
| `C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md` (blob `b370c2f9d88bad044cfc98555b10ce8ede9ee534`) | P*_τ2 y P*_F; elegibilidad basal; D2 primario candidato | Define candidatos de población y condiciones pre-Z, no una población aprobada |
| `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md` (blob `88a9b2b57878c7172aa59d7610634233d7c6ff94`) | Distingue ITT_Z^D2, LATE_f^D2, θ_Af(q_X*) y θ_A(q) | Evita transferir interpretación entre estimandos |
| `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md` (blob `9dd0d08aad6eb0132f794dd6df0c51fb28c779cc`) | UE/UA/UO, reloj, q_X*, interferencia, Outcome y Value | Reutiliza la estructura y localiza sus aperturas |
| `C10_S_TEMPORAL_HORIZON_AND_S4R_INTEGRATION_AUDIT_DRAFT_001.md` (blob `764f16b8643ea077b6bf23162416e2112dfbac1c`) | H=3 es profundidad candidata; no duración | Impide usar H como horizonte de seguimiento |
| `C10_S_VALUE_MINIMUM_CORE_RECONCILIATION_MATRIX_DRAFT_001.md` (blob `86e22703287a3a560911d532078a2c9972d0f2a0`) | Outcome/Value A/B y estados históricos reconciliados | Evita afirmar Value ya instanciado |
| `C10_S_B_VARIANT_MINIMUM_BENEFICIARY_VALUE_CONTRACT_DRAFT_001.md` (blob `ce94c119b83bf460909c835d6cb21e336bb2b646`) | Requisitos mínimos B-BEN/B-VAL; B1 tipo candidato | Delimita qué falta para un ITT sobre V_j |
| DEC-C10-066/067 | D2 primario candidato; políticas materiales D2 aceptadas | Fija el contraste de asignación, no la población ni la identificación |
| DEC-C10-095 | A/B aceptadas como arquitectura; B extensión separada | Separa Outcomes A de Value B |
| DEC-C10S-B1-UNIT-001 y decisiones B1 posteriores | Una B1 por UE; una oportunidad por UE; harness común; enlace y adjudicación separados | Afecta roles y subledger, no define población ITT ni Outcome/Value |

## 3. Contraste de asignación D2

Se conserva la definición material vigente:
- `B_g0^D2`: política que no programa/inicia el intento focal de provisión.
- `B_g1^D2`: política que programa un intento estandarizado de provisión técnica focal.
- `Z`: asignación a una de esas políticas.
- La asignación no asigna directamente provisión recibida, `C_dep*`, `A_f*`, `D_f*` ni `ΔT_acc*`.

**Interpretación C1:** efecto total de asignar la política. Incluye las vías que esa política active. Si existen vías colaterales diferenciales, C1 continúa siendo un ITT de política/paquete; no se transforma en efecto puro de accesibilidad.

La recepción, instalación, respuesta, accesibilidad posterior, solicitud recibida, admisión, procesamiento, selección y ejecución son variables postasignación. Ninguna puede sustituir Z en el ITT ni usarse para excluir UE del denominador.

## 4. Población y elegibilidad

### 4.1 Candidato existente P*_τ2

POP-CMP-001 propone como población de apertura de identidad transformacional las unidades que, antes de Z:
- cumplen las condiciones constitutivas basales definidas ex ante;
- tienen `C_dep,0=0`;
- tienen inaccesibilidad basal respaldada de τ2, `A_f,0*=0`;
- tienen clasificación basal suficiente.

La expresión histórica candidata `P*_{τ2}={i:E_i=1,C_dep,i0=0,A_f,i0*=0}` es una representación abreviada, no una regla final implementable: la composición de `E_i`, los predicados constitutivos, evidencia, indeterminación y adjudicación todavía no están cerrados.

### 4.2 P*_F no es la población primaria por defecto

`P*_F` añade ausencia respaldada de rutas alternativas funcionalmente substituibles y es un subconjunto de `P*_{τ2}`. Se reserva para apertura funcional exclusiva o análisis secundario/heterogeneidad. No se debe sustituir `P*_{τ2}` por `P*_F` sin una decisión explícita que cambie el objetivo causal y la población.

### 4.3 Dictamen

- D2 como comparador primario candidato: **ACCEPTED** por DEC-C10-066.
- `P*_{τ2}` como población C1: **CANDIDATE / NOT ACCEPTED OR FROZEN** en las fuentes revisadas.
- Composición operativa de elegibilidad basal: **OPEN**.
- `P*_F` como población primaria: **NOT PRESUMED**; subobjetivo distinto.
- Distribución objetivo `q_X*`: **CANDIDATE**; población exacta, variables, estratos, pesos y soporte siguen OPEN.

No se propone inventar otra población. La recomendación es continuar sobre `P*_{τ2}` como candidato histórico principal y cerrar su composición antes de cualquier implementación.

## 5. Unidad experimental, unidad de asignación e interferencia

El contrato temporal distingue:
- **UE:** instancia sintética completa cuya configuración, estados, trayectorias y resultados se generan.
- **UA:** entidad a la que se asigna Z.
- **UO:** observaciones longitudinales; no incrementan N independiente.

La configuración UE=UA=una instancia sintética autónoma es una estipulación candidata, admisible solo si se sostiene aislamiento de recursos, agentes, información, infraestructura, estado y canales. Si hay compartición, debe definirse clúster, mapa de exposición y estimando compatible.

Decisiones posteriores ya aceptadas:
- una entidad B1 por UE, vinculada de forma explícita/versionada a una instancia lógica de servicio;
- una oportunidad estandarizada por UE como candidata primaria;
- harness externo común que registra el intento aunque no haya recepción.

Estas decisiones **no prueban aislamiento**. La relación UE–B1–servicio está mejor acotada, pero la identidad material del servicio/B1 y la independencia entre UE siguen pendientes. La interferencia no puede declararse ausente por diseño nominal.

## 6. Resultado: Outcome técnico y Value

### 6.1 Variante A

La arquitectura aceptada A conserva el dominio base. Puede estudiar Outcome técnico independiente de A/Reach/trayectoria. O-CONF tiene el anclaje conceptual más desarrollado en F*/FP-01…08, pero no existe ficha §224 completa: faltan predicados, mapping, tolerancias, oráculo, snapshots, cobertura y adjudicación. Ningún Outcome candidato se encuentra operacionalizado.

**C1 sobre Outcome en A:** posible como objetivo de diseño, pero aún no especificable completamente hasta seleccionar y completar al menos una ficha O. No se infiere Value de O-CONF ni de otro Outcome técnico.

### 6.2 Variante B

DEC-C10-095 acepta B como extensión sintética independiente para instanciar Value. B1 está aceptada como tipo candidato solicitante-beneficiario y una B1 por UE como decisión de diseño. No hay aún instancia B materializada ni consecuencia valorable especificada.

Permanecen OPEN: identidad/versión y relación concreta B1–UE–servicio; Need_preZ y elegibilidad de petición; consecuencia; perspectiva/autoridad; dimensiones V_j; indicadores, fuentes, escalas, baseline, horizonte, regla de valoración, error, ausencia y trade-offs.

**C1 sobre Value en B:** solo podrá formularse por cada dimensión V_j después de cumplir el contrato B-BEN/B-VAL y §224. No crear escalar, ponderaciones ni dimensiones por defecto.

### 6.3 Regla de no transferencia

Un ITT identificado sobre un Outcome técnico no identifica ITT sobre Value. La identificación de una dimensión V_j no se transfiere a otra. No se agrupan resultados A y B ni se intercambian sus poblaciones.

## 7. Horizonte y seguimiento

- El reloj de trabajo `t−1/t0…t9` permanece como secuencia de estados/eventos del DGP.
- `H=3` es una profundidad máxima candidata de composición transformacional, no tres unidades temporales ni un horizonte de duración.
- La ventana/calendario de la oportunidad estandarizada está OPEN.
- La duración de seguimiento, el horizonte de Outcome, el horizonte de Value, la ventana terminal y las reglas de censura están OPEN.
- No se debe asignar el ciclo de petición a t5/t6/t7 ni ampliar H por conveniencia.

C1 requiere un horizonte temporal/terminal definido por resultado y población; la especificación existente no permite derivarlo de H.

## 8. Esqueleto formal de C1 — propuesta de trabajo, no fórmula aprobada

Para una población preasignación P, resultado/dimensión Y y horizonte h, la forma conceptual del ITT es:

`ITT^{D2}_{Y}(P,h)=E[Y_i(Z=1;D2,h)-Y_i(Z=0;D2,h)\mid i\in P]`.

Donde:
- Z=1/0 denota asignación a `B_g1^D2`/`B_g0^D2`, no tratamiento recibido;
- Y puede ser un Outcome técnico O_k en A o una dimensión Value V_j en B;
- P, h y la versión de Y deben estar definidos antes de resultados;
- el efecto es total respecto de las vías activadas por la política.

Esta notación solo fija la estructura de asignación. No presupone que P, h, Y o los potenciales estén ya operacionalizados, ni que el efecto esté identificado. Para resultados vectoriales se reportan contrastes por dimensión, sin agregación no justificada.

## 9. Identificación y condiciones todavía no verificadas

Para cada combinación variante × población × resultado/dimensión × horizonte, se debe adjudicar:
1. mecanismo y probabilidades de asignación, estratos/clúster y positividad;
2. consistencia y versiones de políticas asignadas/recibidas;
3. unidad de asignación y ausencia de interferencia, o mapa de exposición y estimando alternativo;
4. integridad del baseline y clasificación pre-Z de elegibilidad;
5. medición válida e independiente del resultado;
6. observación, missingness, censura y selección, con dictamen P183;
7. precisión y sensibilidad bajo P177/P178/P182/P183;
8. vías colaterales y alcance de interpretación de política/paquete.

La aleatorización, si se confirma el contrato material, identifica el ITT de asignación bajo los supuestos pertinentes; no identifica automáticamente C3, C4, LATE ni un efecto específico de accesibilidad.

## 10. Matriz de estado C1

| Elemento | Estado | Dictamen/acción |
|---|---|---|
| D2 y contraste de políticas | ACCEPTED AS DESIGN DECISION | Reutilizar DEC-C10-066/067 |
| ITT por asignación Z | DEFINED CONCEPTUALLY | Formalizar por resultado/dimensión |
| P*_τ2 | CANDIDATE | Mantener como candidato principal; cerrar E_i y predicados pre-Z |
| P*_F | CANDIDATE SUBPOPULATION | No usar como población primaria por defecto |
| q_X* | CANDIDATE | Cerrar distribución, pesos, estratos y soporte |
| UE=UA | CANDIDATE | Verificar aislamiento; si no, clúster/exposición |
| B1 por UE | ACCEPTED AS DESIGN DECISION | Instancia/relación concreta aún OPEN |
| Una oportunidad por UE | ACCEPTED AS DESIGN DECISION | Ventana, payload/protocolo OPEN; no afecta inclusión ITT |
| Outcome A | NOT OPERATIONALIZED | O-CONF mejor anclado; completar §224 |
| Value B | NOT INSTANTIATED | B1 es tipo candidato; completar B-BEN/B-VAL |
| Horizonte temporal | OPEN | No usar H=3 como duración |
| Asignación/positividad/versión | PARTIAL / OPEN | Recuperar y completar contrato de randomización |
| Interferencia | OPEN | Aislamiento o mapa de exposición |
| Missingness/censura | CONTRACTS AVAILABLE / MATERIAL OPEN | Aplicar P183 por Y |
| Identificación C1 | NOT YET ADJUDICATED | Dictamen separado por Y, P y h |

## 11. Conclusión de C1.1 y siguiente operación

C1.1 logra reconciliar las piezas existentes sin reiniciar la arquitectura. El resultado no es cierre de C1: el contraste D2 está definido como política asignada, pero el contrato de población, unidad efectiva bajo interferencia, resultado y horizonte no está completo.

**Recomendación de continuidad:** mantener `P*_{τ2}` como candidato histórico para C1 y no reabrir `P*_F` como alternativa primaria. La siguiente operación documental debe resolver la composición de elegibilidad basal `E_i` y su evidencia/indeterminación, cotejándola con los predicados constitutivos actuales y sin inventar una fórmula nueva. En paralelo, recuperar la especificación exacta de aleatorización D2 y verificar si ya existe una regla de estratificación/semilla/versión.

No se solicita una nueva decisión sobre D2, B1 por UE, una oportunidad por UE ni A/B: esas decisiones ya están aceptadas en su alcance correspondiente. C1 continúa OPEN; no hay Design Freeze ni autorización de implementación/ejecución.


## 12. C1.2 — auditoría focal de elegibilidad y asignación

### 12.1 Composición de E_i: qué puede reutilizarse

La reconstrucción de POP-CMP-001 y DGP temporal/roles permite conservar estas reglas:
- La elegibilidad experimental es basal y se determina antes de Z.
- La fórmula histórica que agregaba `C_auth`, `C_resource`, `C_capacity`, `C_info`, `C_domain` y `C_other` se retiró como regla operativa. `C_other` no es un residual admisible.
- Para D2, `C_auth,base=1` es condición basal común e invariante respecto de B. Se corresponde con `AUTH_f*`; no debe contarse como un segundo factor independiente.
- `C_dep,0=0` es ausencia basal de dependencia técnica focal; no equivale por sí sola a elegibilidad ni a inaccesibilidad basal.
- `A_f,0*=0` requiere evaluación independiente de la accesibilidad focal completa, no se deriva de `C_dep,0=0`.
- `E_req_preZ` (elegibilidad de una petición B1) es distinta de `E_i` (elegibilidad experimental) y de pertenencia a `P*_{τ2}`/`P*_F`.
- Need_preZ, Request_event y D_resource son objetos distintos. Ninguno de los eventos post-Z de petición altera retrospectivamente la elegibilidad C1.

**No existe todavía una composición cerrada de E_i.** Las condiciones constitutivas actuales deben mapearse una a una, con identidad/versionado, predicado, evidencia y estados 1/0/?/NA justificado. No se debe recuperar por inercia la fórmula retirada ni sumar condiciones duplicadas.

### 12.2 Flujo de clasificación admisible

El orden documental que ya existe es coherente y se reutiliza:
1. fijar frontera, unidad, catálogo/versiones de τ2, granularidad y reglas de composición;
2. medir baseline y condiciones constitutivas antes de Z;
3. verificar `C_dep,0` por protocolo común;
4. adjudicar `A_f,0*` independientemente;
5. evaluar `F_alt,0` solo para la población/subobjetivo `P*_F`;
6. resolver o registrar indeterminaciones con regla pre-Z;
7. sellar el registro basal y determinar población/estratos;
8. asignar Z y aplicar la política D2.

La verdad DGP y la clasificación observada permanecen separadas. Los indeterminados no se convierten en inaccesibilidad confirmada ni se imputan como cero. Si la clasificación observada excluye casos, cualquier estimando restringido debe etiquetarse como población observada/confirmada y no como `P*_{τ2}` verdadero sin supuestos adicionales.

### 12.3 Asignación D2: contrato incompleto

El DGP temporal/roles requiere registrar UA, clúster, marco/estratos, probabilidades de asignación, versión B, algoritmo/semilla/hash y relaciones de recursos/exposición. Sin embargo, en los contratos revisados no se ha encontrado una especificación material completa de:
- mecanismo de aleatorización y nivel efectivo;
- ratio/probabilidades de asignación;
- estratificación/bloques y reglas de balance;
- algoritmo, semilla, reproducibilidad y registro de asignación;
- manejo de desviaciones, duplicados, reasignación o fallos de aplicación.

No se infiere asignación 1:1 ni una semilla. La decisión D2 fija los brazos de política, pero no basta para completar el mecanismo de asignación.

### 12.4 Dictamen C1.2

| Elemento | Estado |
|---|---|
| Elegibilidad basal antes de Z | DEFINED AS REQUIREMENT |
| Fórmula histórica E_i con C_other | SUPERSEDED / NOT TO REUSE |
| C_auth,base=1 común e invariante D2 | ACCEPTED DESIGN CONDITION |
| C_dep,0=0 | COMPONENT OF POPULATION CANDIDATE; NOT SUFFICIENT |
| A_f,0*=0 | REQUIRED BY P*_τ2 CANDIDATE; OPERATIONALIZATION OPEN |
| P*_τ2 | HISTORICAL PRIMARY CANDIDATE; NOT ACCEPTED/FROZEN |
| P*_F | DISTINCT SUBPOPULATION; NOT PRIMARY BY DEFAULT |
| q_X* | CANDIDATE; distribution/support/weights OPEN |
| Randomization mechanism | NOT MATERIALIZED IN THE CONTRACTS REVIEWED |
| Pre-Z handling of indeterminates | RULE REQUIRED; material rule OPEN |

### 12.5 Recomendación y única decisión pendiente de usuario

Para no reabrir el diseño innecesariamente, la recomendación es **conservar P*_τ2 como población objetivo candidata de C1**, tal como ya propone POP-CMP-001 y el DGP temporal/roles. `P*_F` quedaría como subpoblación secundaria para la afirmación de apertura funcional exclusiva. Esto no acepta aún una composición de `E_i`, ni autoriza excluir indeterminados sin regla pre-Z.

La única decisión de arquitectura que conviene confirmar ahora es si se mantiene esa precedencia poblacional para C1: **P*_τ2 como población objetivo primaria candidata, con P*_F como subpoblación secundaria**, sujeta a cerrar la composición de E_i y la factibilidad/soporte. La especificación del mecanismo de aleatorización se completará documentalmente a partir del contrato existente; no requiere elegir ahora un ratio o algoritmo sin justificación.

**Estado:** C1.2 RECONCILIATION DOCUMENTED / C1 OPEN. Sin Design Freeze, schemas, fixtures, implementación, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`.


## 13. Decisión de precedencia poblacional aceptada

Por `DEC-C10S-C1-POPULATION-PRECEDENCE-001`, se acepta `P*_{τ2}` como población objetivo primaria candidata C1 y `P*_F` como subpoblación secundaria para apertura funcional exclusiva. No se acepta todavía la composición de `E_i`, la regla de indeterminados, el soporte, la medición observada, la ausencia exhaustiva de alternativas, la unidad efectiva bajo interferencia, el mecanismo de asignación, el horizonte ni los resultados.

Esta decisión resuelve la pregunta de precedencia planteada al final de §12.5. No debe volver a solicitarse confirmación de P*τ2/P*F. La siguiente operación C1.3 debe trabajar directamente sobre la composición de `E_i` y la evidencia pre-Z usando los contratos vigentes del DGP/IAM y los predicados constitutivos ya aceptados; no puede inventar una nueva lista ni recuperar la fórmula histórica con `C_other`. Debe distinguir validez/admisibilidad de la instancia DGP, aplicabilidad de la transformación `τ2`, accesibilidad basal y elegibilidad de petición B1.


## 14. C1.3 — resultado del crosswalk de E_i

El análisis se registra en `C10_S_C1_BASELINE_ELIGIBILITY_CROSSWALK_DRAFT_001.md`. La documentación permite distinguir admisibilidad de la instancia DGP (`E_scope`) y aplicabilidad semántica de `τ2` desde `S0` (`App*(τ2,S0)`), separadas de `C_dep,0=0` y `A_f,0*=0). El inventario finito ya describe S0 como elegible y requiere `App*(τ2,S0)=1` para el paso focal F1, pero sigue siendo candidato no aprobado.

Se propone, no se acepta todavía, `E_i=E_scope,i ∧ App*(τ2,S0_i)`. El contrato abstracto de configuración (CMP≥1, PAR≥1, RUL≥1, REF=0 solo con cobertura exhaustiva, MET obligatorio, POL ausente por diseño) define el alcance de la instancia, pero no es por sí solo una regla de pertenencia P*. El roster mínimo de servicio CMP/PAR/RUL tampoco es inventario exhaustivo de cada UE. El IAM por snapshot fuente, sus mappings P0/P1 y evidencia material no están sellados.

**Siguiente C1.4:** crosswalk por predicado/registro IAM pre-Z del snapshot `C_SRC`, cruzado con `App*(τ2,S0)`, `C_dep,0` y términos de `A_f,0*`; identificar duplicidades y unknowns. No crear IAM ficticio ni declarar E_i cerrada.


## 15. C1.4 — crosswalk IAM/C_SRC: resultado y límite material

El crosswalk queda documentado en `C10_S_C1_PREZ_IAM_CROSSWALK_C10S_001.md`. Se especifican las clases CMP/PAR/REF/RUL/MET y su papel potencial en `E_scope`, así como la separación de App, C_dep, A_f, F_alt, Need_preZ y E_req_preZ. El overlay IAM/U_G confirma que no existen snapshots C10-S observados ni captura material de C_SRC; los scopes 7×5 son etiquetas lógicas de planificación, no filas físicas. El roster de servicio conocido es mínimo, no exhaustivo.

**Dictamen C1.4: PARTIAL / MATERIAL BLOCKED BY ABSENT IAM AND SNAPSHOTS.** No es posible clasificar unidades ni cerrar E_i sin inventar registros/truth. La propuesta `E_i=E_scope∧App*(τ2,S0)` permanece NO ACEPTADA. Siguiente C1.5: cerrar definición/medición de App y su frontera con A_f; decidir rol de E_scope y selección; regla pre-Z para unknowns; y recuperar mecanismo de asignación D2. No se necesita nueva aprobación de P*τ2/P*F.


## 15. PA — resolución integrada del paquete C1 (2026-11-11)

**Dictamen del ciclo:** `PA_RECONCILED_DOCUMENTALLY / C1_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN`. Se ha realizado una reconciliación integrada de población, elegibilidad, asignación, unidad/interferencia, estimando, horizonte, Outcome y Value. No se abre una secuencia de subgates ni se solicita una decisión de preferencia al usuario: los elementos que impiden cerrar C1 son ausencias materiales verificables.

### 15.1 Contrato causal que sí queda fijado

1. **Tratamiento/contraste:** se conserva D2 conforme a DEC-C10-066/067. `Z` asigna a `B_g1^D2` (programar un intento estandarizado de provisión focal) o `B_g0^D2` (no programar/iniciar intento focal). La asignación no equivale a provisión recibida, instalación, dependencia, accesibilidad ni cambio de `T_acc`.
2. **Estimando:** C1 es el efecto total de asignación a la política D2. Incluye las vías que active el paquete; si hay vías colaterales no aisladas, la interpretación es efecto de política/paquete, no efecto puro de accesibilidad.
3. **Familia, no escalar:** C1 se define por combinación de variante × población × resultado/dimensión × horizonte. No existe un único `Y` ya operacionalizado para todo C10-S.
4. **Población:** `P*_{τ2}` queda como población objetivo primaria candidata por DEC-C10S-C1-POPULATION-PRECEDENCE-001; `P*_F` queda como subpoblación secundaria de apertura funcional exclusiva. La alternativa funcional basal no excluye de `P*_{τ2}`; solo afecta a `P*_F` cuando está respaldada. Esta precedencia no se reabre.
5. **No condicionamiento post-Z:** intento, recepción, admisión, procesamiento, instalación, accesibilidad postratamiento, trayectoria, selección, ejecución, Outcome y Value no redefinen retrospectivamente la población ITT.
6. **A/B:** variante A puede evaluar Outcomes técnicos; variante B es la extensión separada para instanciar Value contextual. No se transfieren automáticamente poblaciones, resultados ni efectos entre variantes.

La notación conceptual compatible es `ITT^{D2}_{Y_j}(P,h)=E[Y_j(Z=1;D2,h)-Y_j(Z=0;D2,h) | i∈P]`. No se declara estimando completo/identificado hasta que `P`, `Y_j`, `h`, asignación, versiones, interferencia y medición estén especificados para la combinación correspondiente.

### 15.2 Elegibilidad basal: reconciliación y límite

Se mantienen separadas:
- `E_scope`: admisibilidad/alcance de la instancia y su configuración basal dentro del universo DGP, según contrato constitutivo e IAM;
- `App*(τ2,S0)`: aplicabilidad semántica de la transformación focal desde el estado basal;
- `C_dep,0=0`: ausencia basal de dependencia técnica focal;
- `A_f,0*=0`: inaccesibilidad basal verdadera de τ2 según la conjunción completa de predicados;
- `F_alt,0`: existencia/ausencia de ruta alternativa, relevante para `P*_F` y no para excluir de `P*_{τ2}`;
- `Need_preZ` y `E_req_preZ`: necesidad del solicitante y admisión de petición, distintas de la elegibilidad experimental.

**Dictamen sobre `E_i`:** la fórmula candidata `E_i=E_scope∧App*(τ2,S0)` no se acepta ni se congela. Se recomienda tratar `E_scope` primariamente como gate de pertenencia al universo/alcance válido del DGP, no como filtro adicional de selección dentro de ese universo, salvo que el generador incluya deliberadamente unidades fuera de alcance en el marco candidato. `App*(τ2,S0)` es una condición candidata de aplicabilidad de τ2 para definir el objetivo focal. Esta recomendación no sustituye el contrato faltante ni permite adjudicar unidades sin IAM/snapshots. `C_dep,0=0` y `A_f,0*=0` siguen siendo condiciones separadas de `P*_{τ2}`, no componentes que puedan inferirse entre sí.

El crosswalk C1.4 confirma ausencia de snapshots `C_SRC`, filas IAM por UE y cobertura material. Por ello no se puede cerrar el roster de condiciones, declarar `REF=0`, calcular pertenencia material a `P*_{τ2}` ni estimar su tamaño/soporte.

### 15.3 Regla de indeterminación pre-Z

Queda fijado como requisito metodológico:
- usar estados trivalentes `1/0/?`; `NA` solo por no aplicabilidad justificada ex ante;
- ausencia de evidencia, cobertura incompleta o mapping ambiguo no equivalen a `0`;
- truth basal del Generator y clasificación observada del Analyzer deben permanecer segregadas;
- la clasificación de elegibilidad usada para la asignación debe estar sellada antes de `Z` y no puede depender de eventos post-Z.

**Regla de análisis aún no congelada:** si una unidad permanece `?` antes de Z, no se la excluirá silenciosamente ni se la recodificará como inelegible. Debe conservarse en el registro de cribado. El protocolo confirmatorio tendrá que optar, antes de asignar, entre resolver la indeterminación, definir un marco observable más amplio con estimando explícito y análisis de cotas/sensibilidad, o restringir el estimando a una población pre-Z confirmada y reconocer que no representa automáticamente la población verdadera `P*_{τ2}`. En C10-S el Evaluator podrá comparar contra truth DGP segregada; esa truth no se entrega al Analyzer ni se usa como si fuera observación disponible.

### 15.4 Unidad, asignación e interferencia

- UE es la instancia sintética completa; UA es la entidad a la que se asigna `Z`; UO son observaciones longitudinales/anidadas y no aumentan el número de unidades independientes.
- UE=UA continúa siendo candidato condicionado a aislamiento efectivo.
- Una entidad B1 por UE y una oportunidad estandarizada por UE son decisiones de diseño aceptadas en su alcance; no demuestran aislamiento ni ausencia de interferencia.
- La instancia de servicio debe ser aislada respecto de otras UE en recursos, agentes, información, infraestructura, estado y canales. Si no se sostiene, habrá que especificar clúster/exposición y un estimando compatible antes de interpretar el ITT.
- No se ha recuperado un contrato material de aleatorización D2 con probabilidades/ratio, estratos/bloques, nivel de asignación, algoritmo, semilla/hash, reproducibilidad ni tratamiento de desviaciones. No se presupone 1:1.
- La legitimidad material de D2 requiere verificar ausencia de provisión focal de fondo en control y condiciones basales; la aceptación de la política no prueba esos hechos.
- `q_X*`, `q_L*`, positividad y soporte no están materializados.

### 15.5 Horizonte

Se conserva el reloj lógico `t−1/t0…t9` y la distinción entre profundidad de ruta y tiempo. `H=3` es profundidad máxima candidata, no duración ni horizonte de seguimiento. El calendario/ventana de la oportunidad B1, duración de seguimiento y horizonte terminal de Outcome y Value deben fijarse por separado y ex ante. No se asignan eventos de petición a `t5/t6/t7` ni se amplía H.

### 15.6 Outcome y Value

**Variante A — Outcome técnico.**
- `O-CONF` es el candidato con mejor anclaje conceptual en `F*`/FP-01…08, pero no tiene ficha operacional completa.
- Faltan predicados, mapping, tolerancias justificadas, oráculo independiente/cego, snapshots, cobertura y regla de adjudicación.
- `O-MIG/O-SVC/O-REC/O-BUR` tampoco constituyen medidas operacionales actuales.
- Por tanto, C1 sobre Outcome técnico es una familia de estimandos candidata, todavía sin `Y_j` confirmatorio cerrado.

**Variante B — Value contextual.**
- B1 por UE, su rol candidato solicitante-beneficiario y la oportunidad estandarizada única están aceptados como decisiones de diseño; no existe aún una instancia material B1/servicio-beneficiario completa.
- Faltan identidad/tipo y relación B1–UE–servicio, `Need_preZ`, consecuencia independiente, perspectiva y autoridad de valoración, dimensiones `V_j`, indicadores, fuentes, unidades/escalas, baseline, horizonte y adjudicación.
- P179 exige preservar Value como vector durante identificación y mantener trade-offs; no se eligen por defecto las cinco dimensiones históricas, no se reduce a un escalar ni se introducen pesos.
- `V_j` no puede ser una recodificación de accesibilidad, Reach, ejecución u Outcome técnico ni incorporar mecánicamente `ΔT_acc`, lo que haría circular la atribución.
- Las decisiones de petición y enlace petición–trayectoria no crean por sí mismas consecuencia valorable ni Value.

En consecuencia, **no existe actualmente un Outcome ni una dimensión Value operacionalizados que permitan cerrar un ITT confirmatorio completo**. Un ITT sobre Outcome técnico no sustituye el ITT sobre Value ni prueba la relación causal `ΔT_acc→ΔV`.

### 15.7 Identificación y dictamen final del paquete

Un ITT de asignación D2 solo podría interpretarse bajo mecanismo de asignación verificable, consistencia/versiones, positividad, población pre-Z definida, unidad/interferencia resuelta y medición válida del resultado/horizonte, con tratamiento explícito de missingness/censura. Aun si C1 fuese identificado, no identificaría automáticamente C3, C4, LATE ni el efecto específico de accesibilidad.

| Componente | Dictamen PA |
|---|---|
| D2 y políticas asignadas | ACCEPTED AS DESIGN ARCHITECTURE; material delivery/control checks OPEN |
| Precedencia P*τ2/P*_F | ACCEPTED; no reabrir |
| E_i / IAM / App / unknowns | PARTIAL; MATERIAL BLOCKED |
| UE/UA / interferencia | CONDITIONAL; isolation unverified |
| Aleatorización / positivity / q_X* | NOT MATERIALIZED / OPEN |
| Horizonte temporal | OPEN; H no es duración |
| Outcome A | NOT OPERATIONALIZED |
| Value B | NOT INSTANTIATED |
| ITT C1 completo/identificado | NOT YET IDENTIFIABLE FROM CURRENT SPECIFICATION |
| Decisiones nuevas del usuario requeridas en este ciclo | NONE: las lagunas actuales son materiales/documentales, no elecciones de preferencia |

**Estado del paquete:** reconciliado integralmente en esta iteración; no equivale a cierre científico de C1. Los bloqueos materiales se arrastran a PB (servicio/B1, snapshots y provisión), PC (soporte/estimandos de accesibilidad) y a la consolidación posterior de PA (asignación, Outcome/Value y horizonte una vez disponibles los contratos materiales). No se reinicia C1.1–C1.4 ni se vuelve a solicitar P*τ2/P*_F.

No se modifica D1/D2, DEC-C10-066/067, el Core, main, RMA, Evidence→Claim Matrix ni claims. `scientific_execution=false`; `execution_authorized=false`. No Design Freeze, schemas físicos, fixtures, implementación, simulación o ejecución.


## 16. Reconciliación integrada D2 — asignación, población y soporte (2026-11-11)

**Artefacto rector:** C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md. Este ciclo concreta la separación entre asignación Z, programación D2, intento/recepción, éxito técnico y apertura focal; integra elegibilidad pre-Z, q_X*/q_L*, soporte y unidad/interferencia.

La probabilidad experimental P(Z=1 | estrato,UA), ratio, estratos, algoritmo, semilla/hash, provenance y desviaciones siguen NOT SPECIFIED. No se confunde con las reglas D2 ya aceptadas P(W_programmed=1 | Z=0)=0 y P(W_programmed=1 | Z=1)=1. c/b (cumplimiento/intento de fondo) siguen OPEN; s=0.80 no aprobado.

P*τ2/P*_F se preservan. E_i y App siguen sin operacionalización; C_dep,0 y A_f,0* no se infieren entre sí. UNKNOWN pre-Z no se recodifica como 0 ni se excluye silenciosamente; el manejo analítico debe decidirse antes de Z. q_X* no es propensión de asignación y su distribución/soporte no están materializados; q_L* solo procede si se necesita régimen secuencial sobre historia post-Z con identificación longitudinal. UE=UA solo con aislamiento; de lo contrario clúster/exposición y estimando compatible.

**Resultado:** contrato documental de distinciones y condiciones reconciliado; asignación, población, soporte e interferencia permanecen OPEN/BLOCKED. No se reinician C1.1–C1.4, PA ni PB. Sin Design Freeze ni autorización de captura/implementación/ejecución.


## 17. Reconciliación de medición confirmatoria Outcome/Value (2026-11-11)

Artefacto rector: `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md`; maestro §276. Se aclara la separación F* (criterio funcional) / O-CONF (resultado adjudicado de conformidad destino) / Value (consecuencia valorada para B1). F* y O-CONF no se cuentan como endpoints independientes. O-CONF sigue candidato, sin predicados, mapping, snapshots, H, evento terminal ni oráculo validado.

Value mantiene vector P179; B1/Need_preZ como base, sin autoridad/criterio/Consecuencia V_j ni dimensión seleccionada. Las medidas O/V requieren fichas §224 independientes, P182/P183 y observación/provenance. ITT_Z^D2(O-CONF) y ITT_Z^D2(V_j) no transfieren identificación entre sí. Sin resultado confirmatorio completo, no hay C1 estimable ni Design Freeze. No duplicar P179/P182/P183/MEAS/MISS ni autorizar ejecución.



## 18. Crosswalk C1–C+D y separación de resultados (2026-11-12)

El plan §16.185 integra C1 con la jerarquía C2–C5 y con los contratos Outcome/Value. Se preserva:

- C1 ITT_Z^D2 por asignación a política material, estimado separadamente para O-CONF_r y V_cont solo si cada resultado supera su propia ficha de medida/validez. No transferir identificación entre resultados.
- C2 primeras etapas separadas para programación, intento, recepción, instalación, C_dep*, A_f*, D_f* y ΔT_acc*. Ninguna sustituye a otra.
- C3 θ_A(q)/θ_Af(q_X*) requiere políticas g_A factibles, distribución basal común, mapping cuando se invoque D2, régimen común, soporte y control/identificación de vías colaterales.
- LATE_f sigue secundario y condicionado a IV válido para D_f*, no a W_attempt ni C_dep*. No calcular Wald causal sin sus supuestos.
- C4 es mediación interventional por ΔT_acc* completo, con estrategia para confusión post-Z y soporte longitudinal. No es ITT menos efecto focal.
- C5 sigue como contraste de contribución por etapa petición–trayectoria; no redefine elegibilidad ni Value.

P*τ2/P*_F, UNKNOWN pre-Z, unidad/interferencia y asignación conservan los límites del contrato D2. O-CONF es outcome técnico terminal; V_cont es candidata de Value temporal B1, con discriminación todavía pendiente. Estado: C1_CONTRACT_RECONCILED / OUTCOME_VALUE_MEASUREMENT_CONDITIONAL / CAUSAL_IDENTIFICATION_NOT_ESTABLISHED / NO_EXECUTION_AUTHORIZED.


## 19. Gate 68 — contrato sintético de identificación y soporte C1/C3 (2026-11-12)

Esta sección complementa §§15–18 y prevalece sobre los pasajes históricos que describían Value de la variante B como no instanciado. La precedencia vigente de B1/V_cont está en el plan integrado §§16.221–16.222 y DEC-C10-095/099–102.

### 19.1. C1 — ITT-D2 sobre V_cont

En el benchmark sintético, cada mundo versionado define una cohorte finita P_w por truth basal pre-Z. El mundo limpio puede estipular por construcción que sus unidades satisfacen las condiciones de la población objetivo candidata P*_{τ2}; E_scope y App*(τ2,S0) se conservan como predicados separados y no se ratifica la fórmula universal E_i=E_scope∧App. Esta construcción sintética no materializa IAM real ni autoriza transportar la población.

El estimando es el efecto total de asignación D2 sobre V_cont en la ventana común T*. Su identificación exige asignación aleatoria en la unidad UA, probabilidad positiva de ambos brazos por estrato/historia objetivo, consistencia/versiones, cohorte sellada pre-Z, tratamiento de interferencia y observación/missingness compatibles. UA=UE solo en mundos aislados; los mundos con spillovers requieren clúster o mapa de exposición. La recepción, instalación, C_dep*, A_f*, D_f* y ΔT_acc* no sustituyen Z ni filtran el ITT.

Si la evidencia pre-Z no permite clasificar pertenencia o el canal S3 no identifica V_cont, el Analyzer debe producir bounds/INDETERMINATE/NOT_IDENTIFIED conforme al mecanismo; el conocimiento de Generator no se transfiere al Analyzer.

### 19.2. C3 — θ_A sobre ΔT_acc* completo

θ_A(q_X*,r_common;V_cont) se evalúa mediante intervenciones g_A1/g_A0 directas y factibles sobre el vector completo (ΔU*,ΔR*,ΔC*,ΔX*), estandarizadas a la misma distribución basal finita q_X*. Para cada historia con masa positiva ambas políticas deben ser factibles y tener soporte; r_common fija explícitamente los mecanismos no focales. Una vía directa/colateral diferencial no separada, soporte fallido o versión inconsistente impide atribución puntual.

El contraste g_A se genera y evalúa directamente; no se deduce del ITT-D2. El mapping B_g^D2→g_A sigue no demostrado. Solo se probará en mundos que estipulen y verifiquen esa correspondencia, sin generalizarla.

### 19.3. Cuadrículas separadas

G_ITT y G_A son cuadrículas distintas. Ambas incluyen nulo, signo positivo y negativo, señal débil y efectos más amplios dentro del rango factible de V_cont∈[0,1]; incluyen heterogeneidad con efectos condicionales de signos opuestos y mundos donde el ITT del paquete difiere del efecto focal. Los niveles se parametrizan relativamente a la media basal y al rango disponible, con κ predeclarado. Los valores de κ, masas de q_X*, pesos, parámetros y N/R siguen abiertos y no se inventan.

No se exige un MDE sustantivo de usuarios reales. δ_min,e será el primer nivel no nulo de la cuadrícula para el que se exige potencia; w_max,e será una meta de resolución inferencial del benchmark, ambos por estimando y fijados antes de calibrar.

### 19.4. Dictamen

ITT_AND_THETA_A_IDENTIFICATION_SUPPORT_CONTRACT_CLOSED_STRUCTURALLY / SEPARATE_EFFECT_GRIDS_DEFINED / NUMERIC_GRID_AND_SUPPORT_OPEN / D2_TO_GA_MAPPING_NOT_DEMONSTRATED / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

La identificación material sigue condicionada a la parametrización, al mecanismo de asignación, al soporte y a la observación de cada celda. C4 y LATE_f permanecen en sus contratos separados y no quedan cerrados por esta sección.
