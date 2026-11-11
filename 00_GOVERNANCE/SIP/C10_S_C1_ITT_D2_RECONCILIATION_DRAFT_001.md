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
