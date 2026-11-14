# C10-S — Reconciliación integrada del contrato de asignación D2, población y soporte

**ID:** C10-S-D2-ASSIGN-POP-SUPPORT-001  
**Fecha:** 2026-11-11  
**Estado:** DESIGN_CONTRACT_RECONCILED_PARTIALLY / RANDOMIZATION_NOT_SPECIFIED / POPULATION_NOT_MATERIALIZED / SUPPORT_NOT_ESTABLISHED / NOT_DESIGN_FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Propósito y precedencia

Este ciclo cierra documentalmente lo que puede especificarse del contrato confirmatorio de asignación D2, población y soporte, reutilizando PA/C1, C1.3–C1.4, PB-MAT, DEC-C10-066/067, DEC-C10S-C1-POPULATION-PRECEDENCE-001, DEC-C10S-D2-ESTIMAND-SEPARATION-001 y el DGP temporal/roles. No recrea decisiones ni crea un diseño numérico.

No se reabren: D2 primario candidato/D1 secundario; P*_{τ2} primaria candidata/P*_F secundaria; identidad B1 por UE; una oportunidad estandarizada por UE; separación UE/UA/UO; definiciones de políticas D2 y estimandos C1/C2/C3/C4.

## 2. Distinciones de asignación que quedan explícitas

Se separan cuatro mecanismos que no son intercambiables:

1. **Asignación experimental:** (p_i=P(Z_i=1\mid\mathcal S_i,UA_i)), probabilidad de que la unidad de asignación reciba Z=1 dentro del estrato/bloque/régimen correspondiente. Este mecanismo, sus probabilidades, algoritmo, semilla, hash, bloques y desviaciones NO ESTÁN ESPECIFICADOS.
2. **Programación de provisión bajo la política D2:** DEC-C10-066/067 fija (P(W_{programmed}=1\mid Z=0,D2)=0) y (P(W_{programmed}=1\mid Z=1,D2)=1). Son reglas de la política condicionales a Z, no probabilidades de aleatorización.
3. **Intento efectivo/recepción:** (c_{z,D}(X,H)) representa cumplimiento/recepción hacia intento efectivo y (b_{z,D}(X,H)) intento de fondo cuando no se programa. Ambos permanecen OPEN; no se presume cumplimiento perfecto ni ausencia de provisión de fondo.
4. **Éxito técnico:** (s=0.80) es hipótesis algebraica no aprobada/validada. No equivale a probabilidad de apertura A_f*, D_f* ni ΔT_acc*.

La asignación Z conserva intención de tratar. No se reemplaza por W_programmed, W_attempt, recepción, instalación, C_dep*, A_f*, D_f* o ΔT_acc*.

## 3. Contrato mínimo que debe quedar fijado antes de cualquier asignación

| Dominio | Elementos pre-Z obligatorios | Estado |
|---|---|---|
| Marco y unidad | roster elegible, ID/version UE, UA, relación UE–UA–UO, clúster/pool si aplica | OPEN; sin roster |
| Población | definición y versión de E_i, P*_{τ2}, criterio de P*_F, regla UNKNOWN, momento de sellado | precedencia aceptada; composición/materialización OPEN |
| Estratos/bloques | variables basales, regla de estratificación, tamaños y tratamiento de estratos vacíos | OPEN |
| Asignación | mecanismo (p.ej. aleatorización individual o por clúster), (p_i), ratio/targets, algoritmo, semilla, hash, código/versión y provenance | OPEN; no presumir 1:1 |
| Consistencia | política/artefacto/versiones asignadas y recibidas, desviación, crossover, contaminación | semántica D2 aceptada; protocolo operativo OPEN |
| Temporalidad | sello de elegibilidad, tiempo Z, ventanas de programación/recepción/verificación y horizonte | reloj t−1/t0…t9; ventanas/duración OPEN |
| Integridad | ocultación/concealment si procede, acceso a secuencia, registro inmutable, reconciliación de asignaciones | OPEN |
| Interferencia | recursos/agentes/estado/información/infraestructura/canales compartidos, carryover y mapa de exposición | aislamiento no demostrado |
| Resultados | O_k/V_j, horizonte, fuente, adjudicación, missingness/censura | no operacionalizados |

No se elige aquí un algoritmo de aleatorización, ratio, semilla, estrato, N, R o ventana: no existe base aceptada para fijarlos. Su ausencia es un bloqueo de especificación, no permiso para completarlos por conveniencia.

## 4. Elegibilidad basal y composición de E_i

Se preserva la precedencia aceptada:

[
P^*_{\tau2}=\{i:E_i=1,\ C_{dep,i0}=0,\ A^*_{f,i0}=0\}
]

y (P^*_F) como subpoblación secundaria para apertura funcional exclusiva, con criterio de alternativa basal respaldada. (F_{alt,0}) no excluye de (P^*_{\tau2}). No hay condicionamiento por variables/eventos post-Z.

Se mantiene la separación:

- (E_{scope}): gate de alcance/validez de la instancia basal en el universo DGP; no se convierte en filtro de selección adicional dentro del universo salvo que el DGP incluya deliberadamente unidades fuera de alcance.
- (App^*(\tau2,S_0)): aplicabilidad semántica de τ2 desde S0; no implica acceso o ruta realizable.
- (C_{dep,0}=0): ausencia basal verificada de dependencia focal.
- (A^*_{f,0}=0): inaccesibilidad focal basal verdadera bajo todos los predicados aplicables.
- (Need_{preZ}) y (E_{req,preZ}): necesidad de B1 y admisión de petición; no son elegibilidad experimental.

La composición (E_i=E_{scope}\land App^*(\tau2,S_0)) sigue siendo propuesta NO ACEPTADA. La regla de aplicabilidad no se puede cerrar con las fuentes actuales sin mapping semántico y truth DGP por unidad. No se recupera (C_{other}), no se agregan predicados comodín y no se infieren (C_{dep,0}) o (A^*_{f,0}) entre sí.

### Regla pre-Z para indeterminación

Se fija como requisito del contrato confirmatorio:

- Estados 1/0/?; NA solo por no aplicabilidad justificada ex ante.
- Ausencia de registro, cobertura parcial o mapping ambiguo producen ?, no 0.
- El Generator conserva truth; el Analyzer recibe solo observaciones/evidencia disponible.
- La clasificación utilizada para asignar debe sellarse antes de Z.
- Una unidad ? no se excluye silenciosamente ni se recodifica como inelegible.

Antes de Z, el diseño confirmatorio deberá elegir y justificar una de estas rutas, según evidencia disponible: (a) resolver la indeterminación con fuente independiente; (b) definir un marco observable más amplio y su estimando, con cotas/sensibilidad justificadas; o (c) restringir a población pre-Z confirmada, declarando que no representa automáticamente la población verdadera P*_{τ2}. Esta elección sigue OPEN; no se simula truth como si fuera observación.

## 5. q_X*, q_L* y soporte: contrato interpretativo

Se reutiliza la definición candidata de DGP:

[
q_X^*=P^*(X,H_0,C_c\mid E=1,C_{dep,0}=0,A^*_{f,0}=0)
]

(q_X^*) es la distribución objetivo de historias basales dentro de la población definida; no es la probabilidad de asignación Z ni una intervención sobre covariables. (C_c) reúne condiciones basales no focales versionadas (autorización, recursos, capacidad, información, dominio y otras precondiciones pertinentes), sin comodines ni doble conteo.

Condición de soporte: para toda historia con masa positiva bajo (q_X^*), ambas políticas D2 deben ser factibles y la asignación a ambos brazos debe tener probabilidad positiva en la unidad realmente aleatorizada. La factibilidad de la política no garantiza cumplimiento, apertura focal o respuesta. Si una política no es factible en una historia, se restringe ex ante la población con nuevo estimando justificado o se declara no identificación; no se extrapola.

La distribución efectiva de (q_X^*), sus pesos, cobertura, soporte común, tamaño y positividad NO están materializados porque no hay roster, IAM/C_SRC, snapshots ni truth/evidence por UE.

(q_L^*) no se introduce como ajuste marginal automático. En el DGP base, (L_m) post-asignación no se trata como confusor común. Solo si una historia longitudinal con confusores variables en el tiempo inducidos por Z resulta indispensable, deberá especificarse una intervención secuencial (q_L^*), con historia, momento, regla implementable, soporte e identificación longitudinal; si no puede sostenerse, el efecto correspondiente queda no identificado. La necesidad y especificación de (q_L^*) siguen OPEN, no se presume necesaria ni disponible.

## 6. Unidad de asignación e interferencia

La regla de diseño se conserva como condicional:

- UE = instancia sintética completa.
- UA = entidad a la que se asigna Z.
- UO = observaciones repetidas t−1…t9; no incrementan N independiente.
- UE=UA es admisible solo si cada instancia no comparte recursos, agentes, información, infraestructura, estado ni canales con otras UE y no existe carryover.
- Si hay recursos/pools/agentes/estado/canales compartidos, se debe definir clúster y asignar/inferir al nivel compatible, o fijar un mapa de exposición (G_i(Z_{-i})) y potenciales (Y_i(z_i,g_i)) con estimando identificable.
- Si el mapa de exposición es incompleto/desconocido, no se interpreta ITT individual ni Wald individual como efecto causal focal.

Una B1 por UE y una oportunidad por UE no prueban no interferencia. El tamaño muestral efectivo depende del número de unidades/clústeres realmente aleatorizados, no del número de observaciones UO.

## 7. Estimandos y límites de identificación

- **C1:** (ITT^{D2}_{Y_j}(P,h)) es efecto total de asignación de la política/paquete por resultado/dimensión y horizonte; requiere mecanismo Z, población, UA/interferencia, medición Y_j y seguimiento completos.
- **C2:** primeras etapas se estiman por separado para W_programmed, W_attempt, recepción, C_dep*, A_f*, D_f* y ΔT_acc*. Una primera etapa técnica no demuestra primera etapa focal.
- **C3 focal/LATE_f:** la primera etapa relevante para IV focal es D_f*, no W_attempt ni C_dep*. Requiere mapping, relevancia, exclusión, monotonicidad, consistencia, independencia, no interferencia y tratamiento de error de medida.
- **C3 general:** θ_A(q) requiere políticas de accesibilidad y régimen común identificables; D2 no equivale automáticamente a g^Af.
- **C4:** mediación interventional requiere intervención mediadora, historia longitudinal, soporte y estrategia para confusión mediador–resultado inducida por Z; no se obtiene por ajuste convencional.
- No se calcula efecto directo/residual por resta entre estimandos no equivalentes.

Ninguno de estos efectos pasa a identificado por este contrato documental. Outcome sigue sin operacionalizar y Value sigue sin instanciar; incluso un ITT de política no prueba ΔT_acc→ΔV.

## 8. Matriz de salida del ciclo

| Elemento | Estado tras reconciliación |
|---|---|
| Semántica Z vs política D2 | RECONCILED |
| Probabilidades de programación D2 (0/1 condicionales a Z) | ACCEPTED BY DEC-C10-066/067 |
| Probabilidad de asignación Z, ratio, estratos, algoritmo/semilla | OPEN / NOT SPECIFIED |
| E_i / App / E_scope | PARTIAL / NOT ACCEPTED / NOT OPERATIONALIZED |
| Regla de estados pre-Z 1/0/?/NA | REQUIREMENT RECONCILED; análisis de ? OPEN |
| P*_{τ2}/P*_F precedence | ACCEPTED; not re-opened |
| q_X* distribution and support | OPEN / NOT MATERIALIZED |
| q_L* | CONDITIONAL NEED; NOT SPECIFIED |
| UE=UA | CONDITIONAL ON ISOLATION; NOT DEMONSTRATED |
| Cluster/exposure alternative | OPEN |
| IAM/C_SRC/roster/snapshots | NONE / MATERIAL BLOCKED |
| Outcome/Value and horizons | NOT OPERATIONALIZED / NOT INSTANTIATED |
| Design Freeze / execution | BLOCKED / NOT AUTHORIZED |

## 9. Siguiente dependencia y autorización

La siguiente dependencia material es una fuente aprobada que permita fijar roster/unidad, IAM/C_SRC, snapshots y cobertura pre-Z. Sin ella no se adjudica E_i, no se calcula q_X*, no se demuestra soporte y no se prueba aislamiento. La autorización para capturar/materializar esos elementos no existe en este ciclo.

Este artefacto cierra la reconciliación documental de las distinciones y condiciones del contrato; no cierra los parámetros ni la factibilidad material. No crea Decision Record, no cambia decisiones aceptadas, no altera main/Core/RMA/Matrix/STATUS/claims y no autoriza captura, schema físico, fixtures, implementación, generación de datos, simulación, estimación o ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.



## 10. Integración con el crosswalk causal C+D (2026-11-12)

El plan §16.185 integra este contrato con los estimandos y los resultados sin alterar las condiciones aquí establecidas:

- P*τ2 primaria candidata y P*_F secundaria; la composición material E_i/App no se declara cerrada. Need_preZ no es elegibilidad.
- q_X* es distribución basal común objetivo, no probabilidad de Z. Su distribución, pesos y soporte no están materializados. q_L* solo procede si se necesita una intervención secuencial longitudinal para confusión mediador–resultado inducida por Z.
- Z se asigna en UA; UE=UA solo bajo aislamiento completo. UO repetidas no incrementan N. Sin mapa de exposición/cluster cuando existe interferencia, no se interpreta ITT individual.
- π_h, estratos, ratio, algoritmo, semilla/hash, N y mecanismo de asignación siguen OPEN. W_programmed bajo D2 es regla de política condicional a Z, no aleatorización; c/b y éxito técnico no se fijan.
- ITT_Z^D2 se mantiene como efecto total del paquete por resultado. θ_A/θ_Af requiere g_A, régimen común y soporte; C4 requiere intervención mediadora longitudinal. No se transfieren ni se restan estimandos.
- O-CONF_r y V_cont son resultados separados; su verdad no resuelve elegibilidad ni asignación. Los requisitos de observación y missingness permanecen independientes.

**Estado:** contrato de distinciones integrado; roster/IAM, E_i, q_X*, soporte, asignación y no interferencia material siguen OPEN/BLOCKED. No se materializa ni autoriza captura, schema, fixtures o ejecución.
