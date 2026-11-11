# C10-S — Contrato integrado del DGP causal-transformacional, temporalidad y roles
**Propuesta de armonización de AUD-002 / XAUD-003…006 / AUD-010…011 — borrador 001**

**Estado:** DRAFT / CONTRATO PROPUESTO — NO APROBADO / NO IMPLEMENTADO  
**Fuentes:** C10-S §§26–32, 38–43, 47–51; C10-D1 §§17–19, 25–30, 32–33.  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116.

---

## 1. Propósito y límites

Este contrato integra en una sola unidad del DGP la asignación de política, provisión técnica, accesibilidad focal, cambio completo del espacio transformacional, Reach, trayectorias, selección, ejecución, Outcome y Value. También define qué información pertenece al generador, al analizador y al evaluador.

No introduce una nueva teoría ni modifica los estimandos de C10-D1. Es una propuesta para armonizar el diseño sintético S4-R y cerrar los contratos documentales AUD-002, AUD-010, AUD-011 y XAUD-003…006.

No fija todavía la unidad final de asignación, los parámetros de inferencia, la regla completa de Value, F*, q*, horizonte, tolerancias ni tratamiento final de interferencia.

## 2. Unidad, población y reloj temporal

La unidad experimental y la unidad de asignación deben declararse por separado. El contrato se expresa para una unidad i; si existe asignación por clúster o interferencia, la indexación y los estimandos deben ampliarse antes de implementar.

| Momento | Evento | Variables/objetos | Regla temporal |
|---|---|---|---|
| t−1 / basal | Delimitación de población | X_i, H_i0, C_c,i0, L_m,i0, C_dep,i0, A_f,i0*, T_acc,i0, F_alt,i0 | Todo ocurre antes de Z; elegibilidad y alternativas no pueden usar datos posteriores |
| t0 | Asignación | Z_i, probabilidad de asignación | Aleatorización conforme al diseño; conservar intención de tratar |
| t1 | Política ofrecida/recibida | B_i, version_B, W_attempt,i | Registrar versión asignada y recibida; intento no equivale a instalación |
| t2 | Instalación/verificación | S_install,i, C_install, C_integrity, C_compat, C_oper, C_dep,i1 | Verificación independiente, ciega a O/V; estados desconocidos no se fuerzan |
| t3 | Accesibilidad post | A_f,i1*, A_f,i1,obs, App_f,i1, T_acc,i1, ΔT_acc,i | Snapshot después de verificación y antes de conocimiento/selección/ejecución |
| t4 | Espacio de posibilidades | Reach_H,i, Π_H,cand,i, precondiciones y relaciones | Derivado de T_acc y reglas de composición/horizonte; no de ejecuciones observadas |
| t5 | Conocimiento/consideración | K_i, Consider_i | Registrar por separado si los agentes conocen y consideran cada posibilidad |
| t6 | Selección/inicio | Sel_i, Start_i, actor, fecha, razón | Selección no equivale a inicio; conservar no seleccionada |
| t7 | Ejecución | Exec_partial, Exec_complete, Interrupt, Fail, End_reason | Eventos longitudinales; no reconstruir accesibilidad retrospectivamente |
| t8 | Resultado | O_i y R_O,i | Outcome definido ex ante y medido independientemente |
| t9 | Valor | V_i, regla/version, beneficiario, horizonte, R_V,i | Value evaluado bajo regla fija e independiente; ausencia no equivale a cero |

Los snapshots posteriores a una ejecución que altere el sistema se registran como nuevos tiempos t+1, t+2…; nunca se sobrescriben los snapshots anteriores.

## 3. Definiciones y ecuaciones generadoras

### 3.1 Asignación y política

`Z_i ∈ {0,1}` asigna una política material indexada por escenario: `B_{g0}^{D1}/B_{g1}^{D1}` o `B_{g0}^{D2}/B_{g1}^{D2}`. La asignación no es intento, recepción, accesibilidad ni ejecución.

- **D2 primario candidato (DEC-C10-066/067):** `B_{g0}^{D2}` mantiene la configuración basal y no programa intento focal; `B_{g1}^{D2}` programa provisión técnica focal estandarizada para unidades elegibles. No se modifica la autorización normativa basal.
- **D1 secundario:** `B_{g0}^{D1}` representa provisión ordinaria de baja frecuencia; `B_{g1}^{D1}` programa el mismo procedimiento para las unidades elegibles. No se redefine D1 como ausencia de provisión.

La probabilidad de programación, el intento efectivo y el estado final verificado se derivan del escenario y del mecanismo técnico; no son una única probabilidad genérica `p0/p1`. Los valores candidatos se detallan en §24 y no están validados.

### 3.2 Intento, éxito y estado final

[
W_{programmed,i} \sim Bernoulli(π_{z,D}^{prog})
]
[
P(W_{attempt,i}=1|W_{programmed,i}=1,Z,D,X,H)=c_{z,D}(X,H)
]
[
P(W_{attempt,i}=1|W_{programmed,i}=0,Z,D,X,H)=b_{z,D}(X,H)
]

[
C_{dep,i1}^{*}=C_{install,i1}^{*}\land C_{integrity,i1}^{*}\land C_{compat,i1}^{*}\land C_{oper,i1}^{*}
]

`π_{z,D}^{prog}` es la probabilidad de programar el intento bajo la política asignada; `c_{z,D}` representa cumplimiento/recepción que lleva al intento efectivo y `b_{z,D}` representa intento de fondo cuando no se programó. Ambos mecanismos permanecen abiertos y deben medirse; no se presume `c=1` ni `b=0`. El éxito técnico condicional candidato `s=0.80` se refiere a la probabilidad conjunta de que la ruta técnica complete los cuatro componentes tras un intento elegible, bajo protocolo, actor, versión, recursos y ventana fijados. No se presume independencia entre componentes.

En el DGP candidato, las probabilidades de **programación** son:
- D1: `P(W_programmed=1|Z=0)=.25`; `P(W_programmed=1|Z=1)=1.00`.
- D2: `P(W_programmed=1|Z=0)=0`; `P(W_programmed=1|Z=1)=1.00`.

El intento efectivo `W_attempt` depende de recepción/cumplimiento y debe registrarse por separado. También se registra cualquier intento de fondo cuando `W_programmed=0`. El estado final `C_dep*` se deriva del intento efectivo y del éxito técnico conjunto; no se fija marginalmente.

Solo bajo una idealización adicional de cumplimiento perfecto (`W_attempt=W_programmed`), una oportunidad, ausencia de provisión de fondo y `s=.80`, se obtendrían como expectativas algebraicas `P(C_dep*=1)` de `.20/.80` en D1 y `0/.80` en D2. Esas cifras no son tasas empíricas ni parámetros aprobados. En particular, el `.80` de D2 no se deriva de programar un intento si este no llega a iniciarse o no se recibe. No implica automáticamente `P(A_f,post*=1)` ni `P(D_f*=1)`; ambos se calculan desde todos sus predicados constitutivos y condiciones basales.

### 3.3 Accesibilidad focal y cambio completo

[
A_{f,i0}^*=I(\text{todas las condiciones focales basales satisfechas})
\\]

[
A_{f,i1}^*=I(C_{dep,i1}=1\land C_{auth,base}=1\land C_{resource}=1\land C_{capacity}=1\land C_{info}=1\land C_{domain}=1\land C_{other}=1)
\\]

[
D_{f,i}=I(A_{f,i0}^*=0\land A_{f,i1}^*=1)
\\]

La población de apertura requiere `A_f,i0*=0` preasignación. `D_f` es la apertura basal→post; `A_f,post*` es el estado focal posterior. No intercambiar ambos cuando existan unidades con acceso basal.

El cambio completo del espacio se conserva como:

[
\Delta T_{acc,i}=T_{acc,i1}\ominus T_{acc,i0}
=(\Delta U_i,\Delta R_i,\Delta C_i,\Delta X_i) — conforme a la precedencia de §30; ΔValidity_e se registra en ΔE_T y no forma parte de ΔT_acc.
\\]

[
A_{f,i}=h_f(\Delta T_{acc,i})
\\]

`h_f` es una proyección focal definida para τ2. No es una identidad entre A_f y ΔT_acc. La representación conserva altas, pérdidas, reconfiguraciones, relaciones, configuraciones, equivalencias, versiones e indeterminación.

### 3.4 Condiciones comunes y factibilidad

- `X,H0` son basales.
- `C_c` contiene condiciones constitutivas que deben conservar configuraciones compatibles con τ2.
- `L_m` contiene otras condiciones temporales según su papel causal en el DGP.
- `q*` es el régimen común explícito sobre condiciones/historias admisibles, no una regla de Value.
- `B_g0/B_g1` deben ser factibles en la población y las historias incluidas; el soporte se verifica por estrato.
- Si una política es imposible en una historia, no se asigna artificialmente; se restringe ex ante la población o se emite no-identificación para el contraste original.

La distribución ilustrativa `P(L_m=1|X,H0)=.5` no sustituye la especificación conjunta de q* ni demuestra positividad.

## 4. Cadena transformacional y de ejecución

[
Z\rightarrow B\rightarrow W_{attempt}\rightarrow S_{install}\rightarrow C_{dep}\rightarrow A_f^*\rightarrow \Delta T_{acc}\rightarrow Reach_H\rightarrow \Pi_H^{cand}\rightarrow K/Consider\rightarrow Sel\rightarrow Start\rightarrow Exec\rightarrow O\rightarrow V
\\]

Esta cadena es un orden generativo de trabajo. No implica que todas las relaciones sean mediación exclusiva ni que no existan vías alternativas B→Value. Esas vías deben figurar en el DGP adversarial y en el contrato de exclusión.

| Predicado/estado | Definición | No implica |
|---|---|---|
| Acc_f | τ2 realizable desde el estado/condiciones | Aplicable, conocida, seleccionada o ejecutada |
| App_f | Precondiciones de estado para aplicar τ2 satisfechas | Accesibilidad nueva o ejecución |
| Reach_H | Estado objetivo alcanzable por secuencia válida dentro de H | Conocimiento/selección/ejecución |
| Known/Considered | Agente conoce/considera la posibilidad | Selección |
| Selected | Agente elige la trayectoria | Inicio |
| Started | Ejecución iniciada | Finalización |
| Exec_partial | Ejecución parcial | Éxito o finalización |
| Exec_complete | Criterio terminal preespecificado satisfecho | Value positivo |

La ausencia de evento y la ausencia de observación se codifican por separado.

## 5. Estimandos y reglas de atribución

### 5.1 Efecto de asignación

[
ITT_Z=E[V\mid Z=1]-E[V\mid Z=0]
\\]

Bajo aleatorización y supuestos de diseño, estima el efecto de asignar las políticas de provisión. No se restringe a quienes cumplen, abren τ2, seleccionan o ejecutan.

### 5.2 Contraste de políticas de accesibilidad focal

[
\theta_{Af}(q^*)=E[V^{q^*,g_1}]-E[V^{q^*,g_0}]
\\]

El ITT_Z puede interpretarse como este contraste solo si:
1. Z asigna efectivamente g1/g0 o las versiones B que las implementan;
2. q* es común, coherente y factible;
3. las políticas difieren solo en la distribución de accesibilidad focal;
4. no hay vías directas/diferenciales hacia Value fuera de A_f;
5. consistencia/versiones, medición, interferencia y ausencia están resueltas;
6. población, horizonte y regla Value son comunes.

Si falla una condición, el resultado es efecto de política/paquete ψ_policy, no θ_Af.

### 5.3 Efecto local focal

[
LATE_f=\frac{ITT_Z}{ITT_{D_f}}
\\]

Solo se interpreta bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia y medición adecuada. Es local a compliers y no es ATE ni θ_Af poblacional. Si la primera etapa es nula, no calcular Wald; si es débil, usar inferencia robusta o declarar INDETERMINATE.

### 5.4 Alcance general C10-D1

S4-R focaliza τ2. No sustituye el estimando general `θ_A(q)` sobre políticas que cambian el espacio transformacional completo. La extensión al espacio completo requiere un diseño adicional y medición de ΔU/ΔR/ΔC, soporte y políticas factibles.

## 6. Contrato de roles y cegamiento

| Dato | Generador | Analizador | Evaluador independiente |
|---|---|---|---|
| Z, B, W_attempt, versión asignada/recibida | Sí | Sí, observables | Sí |
| S_install y C_dep verificados | Sí | Registro observable | Sí |
| A_f,base*, A_f,post*, D_f verdaderos | Sí | No | Sí |
| A_f,obs y snapshots observados | Sí | Sí | Sí |
| T_acc verdadero, ΔT_acc verdadero, relaciones ocultas | Sí | No | Sí |
| T_acc observado, evidencia, indeterminados | Sí | Sí | Sí |
| Parámetros estructurales, errores y potenciales | Sí | No | Sí |
| Reach/Π_H observados/derivados | Sí | Sí | Sí |
| Truth de rutas alternativas y vías directas ocultas | Sí | No | Sí |
| Selección/ejecución/Outcome/Value observados | Sí | Sí | Sí |
| Value potencial y regla verdadera | Sí | Solo regla pública/observada fijada | Sí |
| Indicadores de ausencia R_j | Sí | Sí | Sí |

El evaluador independiente compara la salida del analizador con truth oculta después de congelar el resultado del analizador. No puede editar el resultado ni revelar parámetros antes del análisis.

## 7. Contrato de observación y ausencia

Definir un indicador de observación por bloque:

[
R_Z,R_B,R_C,R_A,R_T,R_{Reach},R_{K},R_{Sel},R_{Exec},R_O,R_V,R_{val}
\\]

Cada ausencia registra motivo, momento, fuente, recuperabilidad y relación temporal con Z, A_f, selección, ejecución y Outcome. No se convierte automáticamente en cero, inaccesibilidad, no ejecución ni Value nulo.

El ITT permanece definido en la población asignada. Casos completos, población observable y submuestra de validación son estimandos/poblaciones distintos; no sustituir uno por otro sin supuestos.

## 8. Invariantes de aceptación propuestos

| ID | Invariante | Criterio |
|---|---|---|
| DGP-01 | Baseline antes de Z | Ninguna variable de elegibilidad basal usa información posterior |
| DGP-02 | Asignación preservada | ITT por Z; no reclasificación por recepción/cumplimiento |
| DGP-03 | Intento ≠ éxito ≠ estado final | Campos y probabilidades separados |
| DGP-04 | Accesibilidad derivada | A_f* se calcula de condiciones verificadas; no se asigna directamente |
| DGP-05 | Apertura focal | D_f exige A_f,base*=0 y A_f,post*=1 |
| DGP-06 | ΔT_acc completo | Se conserva estructura multidimensional; A_f es proyección |
| DGP-07 | q* / Value separados | Value no forma parte del régimen q |
| DGP-08 | Soporte por historia | Ninguna política se asigna fuera del conjunto factible |
| DGP-09 | App/Reach/K/Sel/Exec separados | No hay implicaciones automáticas entre estados |
| DGP-10 | Snapshots inmutables | Cada cambio crea versión/tiempo nuevo |
| DGP-11 | No filtración | Analizador no recibe truth/estados potenciales |
| DGP-12 | Vías alternativas explícitas | Si hay B→Value no mediada por A_f, ITT es paquete |
| DGP-13 | Value independiente | Beneficiario, criterio, escala y horizonte fijados ex ante |
| DGP-14 | Ausencia por bloque | R_j separado; falta no equivale a cero |
| DGP-15 | Interferencia explícita | Unidad de asignación y spillovers declarados |
| DGP-16 | Dictámenes separados | Estado sintético C10-S no se convierte en conclusión científica C10-D1 |

## 9. Correspondencia con auditorías

| Hallazgo | Respuesta propuesta en este contrato | Qué queda para cierre |
|---|---|---|
| AUD-002 | Una unidad, una secuencia causal-transformacional, truth/observed y roles | Alinear todas las ecuaciones, diccionario y fixtures |
| AUD-010 | Matriz variable×tiempo×rol §§2 y 6 | Añadir cada variable del diccionario final y códigos de ausencia |
| AUD-011 | Separación C_c/L_m y predicados §3.4 | Clasificar cada condición concreta por momento y papel causal |
| XAUD-003 | Acc_f/App_f/Reach/K/Sel/Exec separados §4 | Revisar todos los outputs y pruebas para evitar colapsos |
| XAUD-004 | Z/B/W/S/C_dep/A_f*/A_f,obs separados §§2–3 | Cerrar estados indeterminados y medición |
| XAUD-005 | Ejecución solo tras precondiciones y selección válida §4 | Añadir fixtures de no aplicabilidad/no selección/no ejecución |
| XAUD-006 | Snapshots temporales y secuencia §§2–4 | Definir política de actualización, versionado y eventos simultáneos |
| XSYNC-138-03 | A_f como proyección de ΔT_acc | Auditoría global de no sustitución |
| XSYNC-138-04 | q*, L_c/L_m y soporte por historia | Formalizar conjunto factible y positividad |
| XSYNC-138-07/10 | Estados K/Consider/Sel/Start/Exec | Cobertura de pruebas por cada estado |

## 10. Pendientes que impiden aprobación

1. Confirmar que el DGP aislado realmente implementa B_g0/B_g1 como políticas factibles sobre A_f, y que .20/.80 son probabilidades finales verificadas.
2. Formalizar q* como distribución/regla de intervención sobre historias no constitutivas, con C_c compatible.
3. Definir unidad de asignación, UE, clúster y ausencia/interferencia.
4. Completar F*, catálogo de alternativas y regla de equivalencia funcional.
5. Definir Value: beneficiario, criterio, escala, dimensiones, pesos, horizonte, costes/beneficios y distribución.
6. Completar el diccionario variable×tiempo×rol, estados de ausencia y códigos de error.
7. Justificar N, réplicas, tolerancias, precisión, δ/ε.
8. Cotejar el contrato con C10-D1 y realizar revisión independiente.
9. Obtener aprobación explícita antes de implementación; autorización de ejecución separada.

## 11. Dictamen

**Contrato integrado propuesto, no aprobado.** Reduce la fragmentación documental y hace explícitas las dependencias causales, transformacionales, temporales y de información. No cierra AUD-002, AUD-010/011 ni XAUD-003…006 hasta que todas las definiciones se armonicen y las pruebas se conviertan en fixtures verificables.

No se ha implementado ni ejecutado. No se ha simulado, estimado ni analizado dato empírico. No se modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS o claims.


## 12. Armonización con auditoría integral (2026-11-04) — antecedente supersedido en precedencia

La especificación candidata común está definida en el capítulo 53 del documento maestro y en `C10_S_INTEGRATED_RECONCILIATION_AUDIT_DRAFT_001.md`.

**La precedencia de este párrafo es histórica y queda supersedida por DEC-C10-066 (2026-11-06): D2 es el escenario primario candidato y D1 el secundario.** Se conserva aquí la formulación anterior para trazabilidad: D1 principal condicionado y D2 contraste. Los valores C_dep de .20/.80 (D1) y 0/.80 (D2), así como las primeras etapas .60/.80, siguen siendo objetivos candidatos del DGP, no parámetros validados. La justificación del régimen ordinario D1 pasa a ser una condición para interpretar D1 como comparador secundario, no para seleccionar el primario.

(W_{attempt}), (S_{install}), componentes técnicos y (C_{dep,post}) permanecen separados. La distribución conjunta de intento y éxito debe calibrarse a las probabilidades finales verificadas; no se presume independencia. (A_{f,post}^*) solo tiene la misma probabilidad que (C_{dep,post}) si todas las demás condiciones focales están satisfechas. (D_f=I(A_{f,base}^*=0\land A_{f,post}^*=1)) es la apertura basal→post y primera etapa focal.

(q^*) se define sobre condiciones/historias comunes no manipuladas por (g); (g_0/g_1) implementan provisión focal. (C_c) delimita factibilidad. El soporte de ambas políticas se verifica por estrato/historia. Esta armonización es propuesta documental, no aceptación ni autorización de ejecución.


## 13. Propuesta operativa de B y calibración D1/D2

La especificación de §30.2 y la tabla recuperada en el capítulo 52 del maestro separan probabilidad de intento y estado final. Se propone la siguiente factorización candidata:

| Escenario | P(W_attempt=1 dado Z=0) | P(W_attempt=1 dado Z=1) | P(C_dep=1 dado Z=0) | P(C_dep=1 dado Z=1) |
|---|---:|---:|---:|---:|
| D1 | .25 | 1.00 | .20 | .80 |
| D2 | 0 | 1.00 | 0 | .80 |

En ambos escenarios, (P(C_{dep}=1\mid W_{attempt}=1)=.80). Este .80 es una factorización algebraicamente coherente para obtener los estados finales recuperados, no un parámetro literal de la fuente ni un resultado empírico. (C_{dep}) sigue siendo la conjunción de instalación, integridad, compatibilidad y operatividad. No se presupone independencia de esos componentes; se especifica su probabilidad conjunta de éxito.

La política B es la regla de provisión del mismo módulo, procedimiento, recursos y verificación; la diferencia focal es la probabilidad de iniciar el intento. B_g0 en D1 representa provisión ordinaria de baja frecuencia, no ausencia. B_g0 en D2 representa ausencia de provisión focal. B_g1 es provisión programada a todas las unidades elegibles. El actor que inicia el intento, la recepción, las reglas de elegibilidad técnica, el versionado, crossover y los códigos de fallo siguen pendientes.

La asignación Z, B asignada/ofrecida/recibida, W_attempt, éxito técnico, componentes verificados, C_dep, A_f*, A_f,obs y D_f se registran por separado. El ITT conserva Z. No se infiere accesibilidad desde asignación ni desde intento.

Esta propuesta concreta OPEN-C10-001, pero no la cierra ni autoriza implementación. La aceptación requiere justificación de D1 como comparador, definición de versiones/actor/recepción, protocolo de verificación y revisión de vías colaterales.


## 14. q_X*, población y soporte por historia: contrato candidato

Para el DGP primario S4-R se propone (q_X^*=P^*(X,H_0,C_c\mid E=1,C_{dep,0}=0,A_{f,0}^*=0)). Es la distribución objetivo basal sobre la población preasignación, no una intervención que fuerce covariables. (C_c) recoge autorización basal no focal, recursos, capacidad, información, dominio y otras precondiciones esenciales; cada condición conserva ficha versionada y cuatro estados. (C_{dep,0}=0) es la ausencia basal de la dependencia focal, no una condición constitutiva.

El orden es: fijar dominio/unidad/versión; medir X, H0 y Cc; verificar elegibilidad y ausencia/accesibilidad focal basal; cerrar población y qX; aleatorizar Z; aplicar B; medir provisión, intento, éxito, C_dep, A_f*, D_f, trayectorias, O y V. No se selecciona por variables posteriores a Z.

En cada historia basal con masa positiva bajo qX deben ser implementables ambas políticas B_g0/B_g1 y existir probabilidad positiva de asignación a ambos brazos. Esto no implica que cada unidad pueda alcanzar ambos estados de D_f ni que cumpla la provisión. Si una política no es factible, se restringe la población antes de Z con justificación y nuevo estimando, o se declara no identificación; no hay extrapolación silenciosa.

El DGP primario excluye L_m post-asignación como confusor común, según §44.4. Si es indispensable, requiere q_L* secuencial con historia, momento, regla implementable, soporte e identificación longitudinal; no se sustituye por ajuste marginal. La distribución concreta P*, estratos, pesos, unidad/interferencia, inventario y umbrales completos de Cc y ventanas permanecen abiertos. Propuesta documental; no freeze ni ejecución.


## 15. Unidad experimental, asignación e interferencia

La UE es la instancia sintética completa cuyo estado transformacional, trayectorias, Outcome y Value se generan. La UA es la entidad aleatorizada a B. La UO son las mediciones longitudinales T0–T9; observaciones repetidas no son unidades independientes.

**Configuración primaria candidata:** UE=UA=una instancia sintética independiente, una asignación Z y una versión B durante el horizonte. Solo es admisible si no comparte recursos, agentes, información, infraestructura, estado ni canales de transmisión con otras instancias.

Si hay recursos/actores compartidos, definir clúster. Se permite asignación individual dentro de clúster solo con ausencia de spillover justificada o exposición modelada; alternativamente asignar por clúster y ajustar estimando e inferencia a la UA clúster. El N efectivo depende de clústeres, no del número bruto de UE.

Bajo no interferencia, potenciales V_i(z_i), D_f,i(z_i). Si hay interferencia, fijar mapa de exposición G_i(Z_-i) antes de generar resultados y usar potenciales V_i(z_i,g_i), D_f,i(z_i,g_i). Si el mapa es incompleto/desconocido, no interpretar el ITT individual ni Wald individual como efecto causal focal. Distinguir correlación basal por clúster de spillover causado por tratamiento.

Registrar UE, UA, UO, clúster, marco/estratos de aleatorización, probabilidades, versión B, algoritmo/semilla/hash, relaciones de recursos y exposición. La positividad se evalúa en la unidad realmente aleatorizada. El LATE individual requiere no interferencia; con interferencia hace falta estimando IV de exposición/clúster y supuestos adicionales. OPEN-C10-005 sigue abierta hasta auditar recursos compartidos y aprobar unidad.


## 16. F*, alternativas y poblaciones: contrato candidato armonizado

La definición candidata de F* debe fijar, antes de Z y sin Outcome/Value: objetivo funcional observable, entrada/S0, salida técnica, restricciones, tolerancias, horizonte H, granularidad G, contexto C0, evidencia y adjudicación. No se inventan umbrales numéricos. Para cada ruta π se juzgan por separado accesibilidad, aplicabilidad desde S0, substituibilidad Sub(π,F*,G,H,C0), identidad/versión, recursos, coste, latencia, calidad, seguridad y fiabilidad. Substituibilidad no implica identidad ni equivalencia causal.

F_alt,0 conserva tres estados: respaldado ausente (cobertura suficiente y ninguna ruta substituible), respaldado presente (al menos una) e indeterminado (cobertura/evidencia insuficiente o desacuerdo pendiente). La búsqueda fija universo, catálogo, composición, reglas, recursos, horizonte y criterio antes de evaluar; registra rutas rechazadas/indeterminadas y límites. La evaluación es ciega a Z/B/selección/ejecución/O/V.

Se reconcilian dos poblaciones: P*_τ2 estudia apertura de identidad focal y no excluye automáticamente alternativas; P*_F es el subconjunto sin alternativa substituible respaldada y estudia apertura funcional exclusiva. El ITT primario propuesto permanece en P*_τ2; P*_F es subobjetivo/heterogeneidad. Una alternativa basal estable no viola automáticamente exclusión; si B la modifica o activa, la vía adicional compromete LATE focal y el resultado se interpreta como paquete salvo identificación adicional. La definición, cobertura, umbrales, horizonte, pesos y sensibilidad permanecen abiertos.


## 17. Contrato de medición y separación truth/observed para A_f*, C_dep y ΔT_acc

**Estado:** propuesta documental; no aprobada ni implementada. Complementa §§2–8 y 16, sin reemplazar las definiciones históricas.

1. **Truth vs observación.** El generador conserva A_f*, C_dep*, D_f*, T_acc* y ΔT_acc* verdaderos. El analizador solo recibe evidencias, snapshots y clasificaciones observadas (A_f_obs, App_f_obs, T_acc_obs) con estados 1/0/?. El evaluador independiente accede a truth solo después de congelar la salida del analizador.
2. **C_dep.** C_dep*=C_install*∧C_integrity*∧C_compat*∧C_oper*. Cada componente se verifica y versiona por separado; no se presume independencia ni se equipara intento con éxito. Indeterminado no es fallo ni éxito.
3. **A_f*.** A_f*=1 solo si la identidad/version de τ2 es válida y C_dep y todos los predicados de acceso focal previamente clasificados están satisfechos. No se incorpora automáticamente App_f ni ejecución. La clasificación de cada condición como acceso, aplicabilidad, constitutiva, provisión o postratamiento permanece abierta hasta justificación explícita.
4. **App_f.** Se evalúa desde S0 y sus precondiciones, separada de A_f. Puede ser 0 cuando A_f=1. No inferir accesibilidad de la aplicabilidad ni viceversa.
5. **Apertura.** D_f*=I(A_f*,base=0∧A_f*,post=1). D_f_obs conserva los estados observados e indeterminados; no se sustituye la primera etapa verdadera por la observada. El error de clasificación se evalúa con validación conocida o sensibilidad/límites.
6. **ΔT_acc.** Cada snapshot conserva U_acc (identidad+versión), R_acc (relaciones tipadas), C_acc (condiciones/configuraciones), Validity y State. La diferencia registra altas/bajas/cambios de versión, relaciones añadidas/retiradas/reconfiguradas, condiciones modificadas, validez/cobertura y cambios de estado. Se requieren snapshots comparables; los indeterminados se propagan. ΔT_acc es estructurado, no escalar; A_f es solo proyección focal.
7. **Temporalidad.** Baseline y elegibilidad se sellan antes de Z. El snapshot post se toma tras verificación y antes de conocimiento, selección, inicio o ejecución. Cambios posteriores generan nuevos snapshots inmutables.
8. **Cegamiento/validación.** Clasificación independiente de Z/B cuando sea factible y ciega a selección, ejecución, Outcome y Value. La submuestra de validación debe tener selección conocida; una referencia imperfecta aporta incertidumbre propia.
9. **Población observada.** La elegibilidad verdadera del DGP y la clasificación basal observada se reportan por separado. Los indeterminados no se convierten en inaccesibles confirmados. Un estimando restringido a casos observados confirmados se etiqueta como tal; no se equipara automáticamente a P*_τ2.
10. **Pendientes.** Clasificación de predicados, definición/versionado de τ2, estándares E1–E4, adjudicación, concordancia, tamaño de validación, error diferencial, cobertura y reglas de correspondencia de snapshots siguen abiertos. AUD-004, XAUD-003/004 y OPEN-C10-004 no se cierran.

Este contrato no fija umbrales ni tolerancias, no declara validez de constructo, no autoriza freeze, código, simulación ni ejecución.


## 18. Matriz provisional de clasificación de condiciones de τ2

**Estado:** propuesta, no aprobada. Complementa §§2–8 y 17.

| Condición | Papel candidato | Regla de separación |
|---|---|---|
| C_install, C_integrity, C_compat, C_oper | Componentes técnicos de C_dep y condiciones constitutivas de realizabilidad focal | Verificar cada componente; intento, instalación declarada y operación comprobada no son equivalentes |
| C_auth_base | Autorización constitutiva basal de acceso | Mantener fijada/satisfecha en S4-R modalidad A; si B la manipula, el tratamiento es política de autorización y puede abrir vías adicionales |
| C_resource | Acceso si es disponibilidad ex ante persistente; aplicabilidad/ejecución si es insumo consumido por instancia | Descomponer disponibilidad, asignación, demanda y consumo |
| C_capacity | Acceso si es capacidad instalada/slots ofrecidos; aplicabilidad si es margen requerido por S0/carga puntual | Separar stock, disponibilidad por unidad/tiempo y precondición |
| C_info | Acceso solo si es información técnica integrada que habilita invocación; conocimiento/formación/mensajes son mediadores de conocimiento/consideración | Separar configuración técnica de información al agente |
| C_domain | Acceso si es compatibilidad del dominio/objeto con τ2; aplicabilidad si es precondición del estado S0 | Separar clase de objeto de estado concreto |
| C_other | No admisible como comodín | Descomponer en predicados identificados, temporales, verificables y causalmente clasificados |
| S0/precondiciones | Aplicabilidad App_f | No incorporarlas a A_f* por defecto |
| K/consideración/selección/ejecución | Eventos posteriores separados | No definen accesibilidad |

Regla: la clasificación depende del nivel, objeto, unidad, versión, historia y tiempo. Los nombres no determinan el rol. En S4-R aislado, B_g modifica solo la provisión técnica focal y C_dep; los demás predicados de acceso deben estar fijados/satisfechos antes de Z. Si la política cambia autorización, recursos, capacidad, información, conocimiento, coste, calidad u otra vía, se interpreta como paquete salvo diseño adicional.

La ecuación candidata depurada se documenta en el capítulo 59 del maestro. No se cierra la definición universal de A_f*, ni AUD-011/XAUD-003/004/OPEN-C10-004.


## 19. Nivel de sistema, unidad de análisis y recursos en la medición de T_acc

**Estado:** propuesta, no aprobada. Complementa §§2–8 y 17–18.

1. La accesibilidad se indexa por unidad y tiempo cuando la unidad no coincide con el sistema completo: T_acc(i,t | B_sys,B_i,S_sys,t,R_pool,t,R_i,t,C_sys,t,C_i,t,V_t,G,H).
2. Se distingue auxiliarmente T_cap(sys,t | B_sys,S_sys,t,C_sys,t,V_t,G,H), capacidad estructural del sistema, de T_acc(i,t), disponibilidad efectiva para la unidad. En condiciones de identidad/versionado/granularidad compatibles, se espera T_acc(i,t) ⊆ T_cap(sys,t).
3. T_cap no sustituye el T_acc del Core ni añade un tercer componente. El Core permanece Core=(S,T_acc); la descomposición aclara frontera y nivel de indexación.
4. Fijar B_sys, unidad i, B_i, recursos compartidos R_pool, recursos asignados R_i, condiciones de sistema/unidad, instante, horizonte, granularidad y versiones.
5. Infraestructura/capacidad nominal es nivel sistema; pool compartido requiere disponibilidad temporal y concurrencia; asignación/reserva es relación sistema-unidad; consumo durante ejecución no define acceso basal; precondiciones de S0 pertenecen a aplicabilidad.
6. Si la disponibilidad depende de otras unidades, modelar interferencia; no asumir ausencia de interferencia. Si la asignación experimental y la medición se realizan en niveles distintos, especificar estructura multinivel.
7. ΔT_acc(i) y ΔT_cap se registran separadamente. Cambio de capacidad no garantiza acceso de cada unidad; cambio de asignación puede modificar T_acc sin cambiar T_cap.
8. No agregar por unión ni promedio sin estimando/regla explícitos. Outcome/Value de sistema requieren regla de agregación independiente.
9. Pendientes: frontera, unidad, recursos, rivalidad, proveedores externos, nivel de Z/B y Outcome/Value, interferencia y agregación. No cierra AUD-010/011, XAUD-001…004 ni OPEN-C10-004.


## 20. Contrato candidato de frontera, unidad e intervención primaria

**Estado:** propuesta de armonización de §§14–15 y 19; no aprobada.

1. **Unidad:** para el DGP primario aislado, UE=UA=unidad causal i=instancia sintética completa e independiente; UO son snapshots T0–T9 de esa misma instancia.
2. **Frontera:** B_sys contiene arquitectura, dependencia τ2, interfaces, autorización basal, recursos/capacidad pertinentes e información técnica integrada. Toda dependencia externa se incorpora explícitamente o se declara con proveedor, versión, disponibilidad y contrato.
3. **Niveles:** T_cap y T_acc pueden coincidir operacionalmente solo si la instancia completa es la unidad y no hay subunidades con acceso diferenciado. La igualdad no se generaliza; si aparecen subunidades, se reabre el diseño multinivel.
4. **Intervención:** Z_i asigna B_i; B es la política material de provisión técnica focal. W_attempt, instalación, C_dep, A_f*, A_f_obs y D_f son variables separadas.
5. **Aislamiento:** B no cambia autorización basal, recursos compartidos, capacidad, conocimiento, incentivos, prioridad, coste, latencia ni calidad/seguridad de ejecución. Si cambia, se declara efecto de paquete salvo diseño adicional.
6. **q_X*:** distribución objetivo de historias basales; condiciones constitutivas se verifican antes de Z. Ambas políticas deben ser factibles y tener soporte en cada historia con masa positiva; si no, restringir ex ante o declarar no identificación.
7. **Poblaciones:** P*_τ2 y P*_F se determinan con datos basales pre-Z; P*_F es subconjunto funcional exclusivo.
8. **Interferencia:** el generador primario no comparte recursos, agentes, información, estado ni canales entre instancias. Escenarios con spillover se mantienen adversariales y requieren clúster/mapa de exposición y estimando compatible.
9. No se acepta la configuración hasta verificar frontera, mecanismo material de B, q_X*, no interferencia, poblaciones y vías colaterales. OPEN-C10-005 y XAUD-001/002 permanecen abiertos.


## 21. Contrato material candidato de B0/B1

**Estado:** propuesta, no aprobada ni congelada.

- **B0:** mantener configuración basal durante H; no desplegar ni habilitar la dependencia focal τ2. No retirar capacidades basales.
- **B1:** aplicar protocolo versionado de despliegue/configuración de la dependencia focal τ2 y habilitar su interfaz técnica; verificar instalación, integridad, compatibilidad y operación.
- **Actor/destinatario/objeto:** rol ejecutor sintético; instancia i; identidad canónica y versión de τ2/dependencia.
- **Registro:** versión del protocolo/artefacto/configuración, actor, unidad, tiempos, pasos, estado, fallos, reintentos, rollback, desviaciones, contaminación, snapshots y hashes.
- **Cadena:** Z asigna B; B_received/W_attempt/S_install/C_dep*/A_f*/A_f_obs/D_f*/App_f/Exec_f permanecen variables distintas.
- **C_dep*:** conjunción de C_install*, C_integrity*, C_compat* y C_oper*. Cada componente requiere evidencia/tiempo/regla propios. C_oper acredita disponibilidad del canal técnico, no ejecución funcional de τ2.
- **Aislamiento:** autorización basal no focal, recursos no focales, conocimiento/formación, incentivos, atención, selección, rutas alternativas, costes/calidad/seguridad y medición se mantienen invariantes. Si cambian, reclasificar B como paquete.
- **Incumplimiento:** fallos, parcialidad, rollback y contaminación no cambian Z ni la clasificación ITT. Indeterminado no equivale a fallo ni éxito.
- **Interpretación:** ITT identifica asignación de política B; no demuestra mediación ni efecto específico de A_f. Exclusión y atribución permanecen sujetos a C10-D1/S4-R.
- **Pendiente:** fijar identidad/versiones, pasos, tiempos, fixtures, estándares de evidencia, invariantes y revisión independiente. No freeze/ejecución.


## 22. Contrato candidato de medición A_f*, A_f,obs, D_f* y ΔT_acc*

**Estado:** propuesta; no aprobada ni congelada.

1. C_dep* es el estado técnico compuesto de provisión; no define por sí solo accesibilidad.
2. A_f* se determina desde snapshot estructural completo y predicados ID, REL, COND, AUTH, RES, DEP, BLOCK y VALID.
3. A_f,obs es salida del analizador con estados 1/0/?; verdad del DGP permanece separada y oculta.
4. App_f, conocimiento, consideración, selección, inicio y ejecución son variables distintas de A_f*.
5. D_f*=1 solo si A_f,base*=0 y A_f,post*=1; elegibilidad basal exige ausencia respaldada pre-Z.
6. ITT_Df* y ITT_Df,obs se reportan separadamente; primera etapa de C_dep* no sustituye primera etapa de accesibilidad.
7. ΔT_acc* se conserva como diff estructurado de U_acc, R_acc, C_acc, Validity y State/context; snapshots incompatibles producen indeterminado o requieren correspondencia versionada.
8. h_f(ΔT_acc*)=D_f* es proyección focal, no equivalencia con el objeto completo.
9. Analizador ciego a Z/B, selección, ejecución, Outcome y Value; validación imperfecta exige límites/sensibilidad.
10. Alternativas funcionales F* y accesibilidad de τ2 se clasifican separadamente.
11. Si B modifica AUTH/RES/capacidad/conocimiento/rutas alternativas u otras vías, reclasificar como paquete o efecto conjunto.
12. No fijar umbrales, fixtures, cobertura ni error de medición sin protocolo ex ante. No freeze/ejecución.


## 23. Reconciliación temporal-causal de condiciones y roles

**Estado:** propuesta, no aprobada ni congelada. Complementa §§2–4 y 17–22.

1. Clasificar por componente, unidad, objeto, nivel, tiempo, versión y rol causal. Una condición puede ser constitutiva de A_f* y ser basal en t−1 o mediadora si cambia después de Z.
2. t−1 sella población, frontera, versión τ2, q_X*, alternativas, condiciones basales, elegibilidad, A_f,base* y T_acc,base*. Nunca reconstruirlos desde post-Z.
3. t0 asigna Z; t1 registra B asignada/recibida, intento y versión; t2 verifica provisión y registra separadamente C_dep, C_auth, recursos, capacidad, información y co-intervenciones; t3 mide A_f,post*/A_f,obs, T_acc y App_f antes de conocimiento, selección, inicio y ejecución.
4. t4 Reach/Π_H; t5 conocimiento/consideración; t6 selección/inicio; t7 ejecución; t8 Outcome; t9 Value. Cambios posteriores crean snapshots nuevos e inmutables.
5. C_dep puede ser afectado por B; C_auth, recursos, capacidad no focal, información técnica no focal y dominio se mantienen basales/invariantes en el primario. Si cambian, registrar mediación/co-intervención y revisar interpretación como paquete.
6. Recursos: separar stock, disponibilidad/asignación, demanda y consumo. Capacidad: instalada, slots, disponibilidad temporal y carga. Información: configuración técnica frente a mensajes/formación/conocimiento. Dominio: tipo de objeto frente a precondiciones S0.
7. Precondiciones S0 pertenecen a App_f, no A_f*. K/consideración/selección/ejecución son downstream.
8. VALID/cobertura pertenece al proceso epistémico; si B cambia observabilidad, modelar missingness/error diferencial.
9. No ajustar ITT por mediadores post-Z. Confusores temporales afectados por tratamiento requieren método/estimando longitudinal explícito.
10. **Pendiente B:** §62 describe B0/B1 como ausencia frente a provisión, mientras §3.1 conserva políticas probabilísticas con p0=.20 y p1=.80. Decidir entre políticas estocásticas de distinta intensidad o brazos deterministas con incumplimiento estocástico; alinear asignación, recepción, intento, éxito, C_dep y estimandos.
11. La intervención histórica sobre C_auth es alternativa distinta; no mezclarla con provisión focal primaria mientras C_auth sea basal/invariante.
12. No modificar .20/.80 ni asumir equivalencia entre contratos sin decisión explícita.

No cierra AUD-011, XAUD-003/004/006, OPEN-C10-004/005 ni la especificación material de B. No freeze/ejecución.


## 24. Reconciliación explícita de B: escenarios D1/D2, intento y estado final

**Estado:** propuesta documental; complementa y aclara §§3.1–3.2 y 21–23, sin aprobación ni freeze.

1. La discrepancia aparente se resuelve distinguiendo dos escenarios candidatos ya definidos en maestro §§53.4–54:
   - D1: control ordinario con provisión de baja frecuencia frente a provisión programada; escenario secundario.
   - D2: control sin provisión frente a provisión programada; escenario primario candidato por DEC-C10-066.
2. **Supersedido por DEC-C10-067:** la lectura de p0=.20 y p1=.80 como probabilidades genéricas de política/estado final no gobierna D2. Las probabilidades vigentes de §3.1/§24 son de programación (`W_programmed`); el intento efectivo y C_dep se derivan de cumplimiento, provisión de fondo y éxito técnico.
3. Probabilidades candidatas de **programación** de §54:
   | Parámetro | D1 Z=0 | D1 Z=1 | D2 Z=0 | D2 Z=1 |
   |---|---:|---:|---:|---:|
   | P(W_programmed=1) | .25 | 1.00 | 0 | 1.00 |
   El intento efectivo W_attempt depende de recepción/cumplimiento y se observa por separado; la provisión de fondo cuando W_programmed=0 también debe medirse.
4. El éxito técnico condicional candidato s=.80 se aplica solo a un intento efectivo elegible. Las probabilidades marginales de C_dep se derivan de programación, cumplimiento, intentos de fondo y éxito conjunto; no son parámetros independientes. Solo con cumplimiento perfecto, una oportunidad y ausencia de provisión de fondo se reproducen .20/.80 en D1 y 0/.80 en D2. No se presume independencia entre componentes técnicos de C_dep.
5. La descripción de B0 como mantenimiento sin provisión focal y B1 como provisión programada en §21 corresponde a D2. No debe usarse como definición general de B0/B1 ni como descripción de D1.
6. En D1, B_g0 programa provisión ordinaria de baja frecuencia; B_g1 programa el mismo procedimiento para todas las unidades elegibles. En D2, B_g0 no programa provisión focal; B_g1 la programa para todas. El inicio efectivo se observa por separado.
7. Z asigna política; B_assigned/offered/received, W_programmed, W_attempt, S_success, componentes técnicos, C_dep, A_f*, D_f*, App_f y Exec_f permanecen separados.
8. Las diferencias .60 (D1) y .80 (D2) en C_dep solo se reproducen bajo cumplimiento perfecto, una oportunidad, ausencia de provisión de fondo y s=.80. No son primeras etapas aprobadas; las primeras etapas efectivas se calculan desde W_attempt y C_dep observados/verdaderos por separado.
9. **Supersedido por DEC-C10-066:** D2 ya es el escenario primario candidato y D1 el secundario. La legitimidad de D2 sigue condicionada a verificar ausencia basal y ausencia de provisión focal de fondo; la legitimidad de D1 requiere justificar el régimen ordinario. Esta precedencia no cierra población, soporte, estimandos, parámetros ni identificación.
10. Esta sección aclara la ambigüedad registrada en §23.10; no altera silenciosamente el texto histórico ni declara aprobadas las políticas.
11. Permanecen abiertos: actor/disparador, recepción, hash/versión, evidencia, distribución conjunta de componentes, crossover/contaminación, calibración de A_f*, exclusión y aprobación del comparador.
12. No freeze, implementación, simulación ni ejecución.


## 25. Regla de selección del comparador D1/D2

**Estado histórico de la regla:** recomendación de diseño condicionada, supersedida en cuanto a precedencia por DEC-C10-066. Las condiciones de legitimidad de cada comparador siguen vigentes.

1. D1 responde al efecto incremental de provisión programada frente a provisión ordinaria de baja frecuencia. Solo es un comparador ordinario legítimo si la frecuencia de intento .25 y el estado final .20 están justificados para la población/contexto objetivo mediante fuente independiente y especificación ex ante.
2. El expediente actual no contiene todavía esa justificación. La recomendación histórica D1-principal-condicionado no equivale a selección aprobada.
3. D2 responde a provisión programada frente a ausencia de intento focal. Para el objetivo mecanístico sintético de apertura focal, D2 es el candidato preferente provisional mientras no se acredite el régimen ordinario D1.
4. D1 se conserva como escenario secundario de política incremental; no se llama contaminación a la provisión ordinaria que forma parte de B_g0^D1. Crossover significa recepción fuera de la política/version asignada.
5. Los ITT_D1 e ITT_D2 son estimandos distintos; no se agrupan ni promedian como si compartieran el mismo comparador.
6. Las primeras etapas de C_dep, A_f,post*, D_f y ΔT_acc se estiman por separado y para cada escenario. Los Wald/LATE no se consideran automáticamente transportables entre D1 y D2.
7. D2 exige verificar C_dep,base=0, A_f,base*=0, ausencia de provisión focal de fondo, condiciones no focales comunes e interferencia controlada.
8. D1 exige documentar régimen ordinario, fuente de .25/.20, población/periodo/contexto, equivalencia de módulo/protocolo/recursos y vías colaterales.
9. DEC-C10-066 ya selecciona D2 como escenario primario candidato y D1 como secundario. Esta regla conserva únicamente las condiciones de legitimidad de cada comparador; no aprueba el .80 condicional ni cierra los gates restantes.
10. No freeze, implementación, simulación ni ejecución.


## 26. Calibración conjunta de componentes técnicos y derivación de A_f*

**Estado:** propuesta documental; no aprobada ni congelada. Complementa §§17–25 y maestro §67.

1. **Componentes verdaderos:** para cada intento se registran (C_{install}^*, C_{integrity}^*, C_{compat}^*, C_{oper}^*). Respectivamente: instalación efectiva de identidad/versión autorizada; integridad del artefacto/configuración verificada; compatibilidad de interfaces/dependencias; disponibilidad operativa del canal de invocación. (C_{oper}=1) no significa que τ2 haya sido ejecutada.
2. **Conjunción:** (C_{dep}^*=C_{install}^*\land C_{integrity}^*\land C_{compat}^*\land C_{oper}^*). En verdad DGP, cada componente es 0/1. En observación, cada uno es 1/0/?: conjunción observada 1 si todos son 1; 0 si al menos uno es 0 respaldado; ? en los demás casos.
3. **Dependencia estadística:** no se presume independencia entre componentes. El parámetro candidato (s=.80) es (P(C_{dep}^*=1\mid W_{attempt}=1,E,D,\mathcal H)), es decir, probabilidad conjunta de éxito de la ruta técnica tras intento elegible bajo contexto, versión, protocolo, actor, recursos y ventana fijados. No significa que cada componente tenga probabilidad .80 ni autoriza multiplicar cuatro marginales.
4. **Estatus de .80:** es una factorización algebraica propuesta para reproducir los estados finales D1/D2, no una tasa empírica, fuente de ingeniería o valor histórico validado. Un DGP reproducible debe declarar la distribución conjunta o mecanismo equivalente y analizar sensibilidad a valores y dependencias alternativos.
5. **Accesibilidad estructural:** (A_f^*=I(ID_f^*\land REL_f^*\land COND_f^*\land AUTH_f^*\land RES_f^*\land DEP_f^*\land\neg BLOCK_f^*)). ID, REL, COND, AUTH, RES, DEP y BLOCK deben tener definición operativa, unidad, tiempo, versión y evidencia. VALID/cobertura pertenece al proceso de medición, no a la verdad causal. App_f y precondiciones de S0 no se incorporan por defecto.
6. **Ruta única vs rutas alternativas:** en el DGP aislado primario se estipula una única ruta focal inventariada y (DEP_f^*=C_{dep}^*). En el contrato general (DEP_f^*) significa al menos una ruta válida; por tanto (C_{dep}^*=0) no implica necesariamente (A_f^*=0). D2 requiere inventario/cobertura que descarte rutas equivalentes no registradas.
7. **Primeras etapas:** por escenario informar (FS_{Cdep}), (FS_{Af}), (FS_{Df}), cada componente técnico y el cambio estructurado ΔT_acc por separado. Solo si la población tiene (A_{f,base}^*=0), la ruta es única y todos los demás predicados se mantienen satisfechos/invariantes, las cifras candidatas coinciden: D1 .60 y D2 .80. En general, calcular la probabilidad conjunta de C_dep y los demás predicados; no transferir automáticamente .60/.80 a A_f/D_f.
8. **Fallos e indeterminación:** intento no iniciado no es fallo técnico; un componente falso basta para C_dep=0; componente desconocido sin fallo conocido produce C_dep,obs=?; fallo parcial/rollback/crossover se registra como evento; evidencia insuficiente no se convierte en inaccesibilidad. La verdad del generador permanece oculta al analizador.
9. **Medición:** A_f,obs y C_dep,obs conservan 1/0/?; validación ciega y error diferencial por brazo/componente/escenario se tratan separadamente. Si sensibilidad/especificidad no están identificadas, usar límites/sensibilidad, no corrección puntual ficticia.
10. Esta sección no valida .80, no fija distribución conjunta, no cierra OPEN-C10-001/007/008 ni AUD/XSYNC asociados, y no autoriza freeze, implementación, simulación o ejecución.


## 27. Distribución conjunta de los cuatro componentes técnicos

**Estado:** propuesta del DGP, no aprobada ni congelada; complementa §26 y maestro §68.

1. Orden fijo: C_install, C_integrity, C_compat, C_oper. Para cada intento elegible se define una distribución conjunta de 16 patrones (p_{abcd}=P(C=(a,b,c,d)mid W_attempt=1,E,D,H)), no negativa y con suma uno. (s=p_{1111}).
2. s=.80 fija solo la celda de éxito total. No identifica marginales, fallos parciales, asociaciones ni las otras 15 celdas.
3. Dos distribuciones con el mismo s pueden tener perfiles de fallo distintos. Ejemplo ilustrativo: (A) p1111=.80 y p0000=.20; (B) p1111=.80 y .05 en cada patrón con exactamente un componente fallido. La segunda tiene marginales .95 por componente; la primera presenta choque común. No son intercambiables.
4. Con marginales m_i, los límites de Fréchet son max(0,Σm_i−3) ≤ s ≤ min(m_i). Bajo independencia, s=∏m_i; no asumirlo. Cuatro marginales .80 bajo independencia producen .4096, no .80.
5. Sensibilidad propuesta: familias de choque común, fallos parciales dispersos, bottleneck por componente, dependencia mixta, heterogeneidad basal y deriva de versión/tiempo. Cada familia requiere tabla completa o mecanismo que reconstruya las 16 celdas.
6. Malla exploratoria inicial s∈{.60,.70,.80,.90}; no es elección confirmatoria ni dato empírico. No confundir s (éxito condicional por intento) con FS (diferencia entre brazos).
7. Por escenario/réplica se reportan semilla, versión generador, tabla 16 celdas, denominadores de intentos/no intentos, marginales, patrones parciales, asociaciones, reintentos, rollback, versiones y heterogeneidad. Truth permanece oculta al analizador.
8. D1 y D2 se calibran y reportan por separado. Cambios en s no pueden alterar implícitamente tasa de intento, recursos, autorización o vías colaterales; cualquier cambio debe declararse como parte del mecanismo.
9. No se selecciona tabla ni distribución confirmatoria, no se valida s, no se aprueba independencia y no se autoriza freeze, implementación, simulación o ejecución.


## 28. Fixtures conjuntos y propagación analítica a las primeras etapas

**Estado:** propuesta matemática no aprobada; complementa §§26–27 y maestro §69.

1. Orden binario: C_install, C_integrity, C_compat, C_oper. Se especifican cuatro tablas completas de 16 patrones para s=.80: choque común (p1111=.80, p0000=.20); fallos simples dispersos (p1111=.80 y .05 en cada patrón de fallo simple 0111,1011,1101,1110); bottleneck instalación (p1111=.80, p0111=.20); fallos emparejados (p1111=.80, p0011=.10, p1100=.10). Celdas restantes cero.
2. Marginales respectivas: choque común (.80,.80,.80,.80); fallos simples (.95,.95,.95,.95); bottleneck (.80,1,1,1); emparejados (.90,.90,.90,.90). Igual s no implica iguales marginales.
3. Para generalizar a s, conservar el patrón de masa residual y sustituir p1111=s, masa de fallo=1−s. Es una familia que permite variar marginales; no mantiene marginales fijas.
4. Con una oportunidad, sin dependencia basal ni rutas alternativas, D1 q0=.25/q1=1 y D2 q0=0/q1=1, y éxito condicional s común a brazos: D1 control=.25s, tratamiento=s, FS=.75s; D2 control=0, tratamiento=s, FS=s.
5. Para s=.60/.70/.80/.90, D1 control=.15/.175/.20/.225; FS=.45/.525/.60/.675. D2 control=0; FS=.60/.70/.80/.90.
6. Por tanto, el .20 de control D1 es consecuencia de q0=.25 y s=.80. No debe mantenerse constante al variar s salvo que se modifique otro mecanismo.
7. Estas son expectativas analíticas de C_dep, no de A_f*/D_f* salvo inaccesibilidad basal, ruta única, predicados no técnicos invariantes y condiciones de medición de §67. Múltiples intentos requieren modelo secuencial; no aplicar automáticamente 1−(1−s)^n.
8. No se selecciona fixture, no se estima potencia/tamaño muestral, no se ejecuta simulación y no se aprueba distribución confirmatoria.


## 29. Reconciliación de población, elegibilidad y notación de apertura

**Estado:** propuesta de armonización; no aprobada ni congelada. Vinculada al maestro §70 y a C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md.

1. Población focal de apertura de identidad: P*_{τ2}={i:E_i=1, C_dep,i0=0, A_f,i0*=0}; todas las condiciones y clasificaciones son pre-Z.
2. Población de apertura funcional exclusiva: P*_F={i∈P*_{τ2}:F_alt,i0=0 respaldado}; por construcción es subconjunto de P*_{τ2}.
3. La alternativa basal presente o indeterminada no excluye automáticamente de P*_{τ2}; impide confirmar pertenencia a P*_F cuando F_alt,0 no es ausencia respaldada.
4. Se normaliza la notación nueva: C_dep,0 es disponibilidad basal técnica; A_f,0* y A_f,1* son accesibilidad verdadera basal/post; D_f*=I(A_f,0*=0 ∧ A_f,1*=1) es transición de apertura. Evitar D_f,0 para disponibilidad basal.
5. F* se mantiene como función/capacidad funcional focal y requiere objetivo, S0, criterios de aceptación, restricciones, tolerancias, H/G/C0, recursos y evidencia E1–E4. No derivar F* de Outcome o Value.
6. D1 y D2 son comparadores distintos. D1 requiere evidencia independiente para el régimen ordinario .25/.20; D2 requiere objetivo explícito ausencia-vs-provisión y ausencia de provisión focal de fondo. No combinar ITT ni LATE.
7. La propuesta no fija el comparador primario, no valida .80, no cierra OPEN-C10-001/003/005/007 y no autoriza implementación, simulación o ejecución.


## 30. Separación de snapshot estructural y paquete de evidencia

**Estado:** propuesta; crosswalk del maestro §71 y de C10_S_TRANSFORMATIONAL_SNAPSHOT_AND_DELTA_RECONCILIATION_DRAFT_001.md.

1. Truth estructural: S_T*(i,b,c,t)=(U_t*,R_t*,C_t*,X_t*).
2. Evidencia/observación: E_T=(Sources,Coverage,Validity_e,Provenance,Version,Timestamp,Adjudication).
3. ΔT_acc*=Diff_{G,M}(S_T*(t0),S_T*(t1))=(ΔU*,ΔR*,ΔC*,ΔX*).
4. ΔE_T registra cambios de fuentes, cobertura, validez epistémica, procedencia, versiones de evidencia y adjudicación.
5. ΔValidity_e no es componente de la verdad causal de ΔT_acc*. La validez semántica/operativa estructural pertenece a C*/R*.
6. No calcular diff sin identidad, frontera, granularidad, catálogo y mapping de versiones compatibles; mapping incierto produce ?.
7. Truth permanece oculta al analizador; observación T_acc,obs/ΔT_acc,obs conserva 1/0/? y se valida después.
8. Esta regla supersede las formulaciones históricas de §3.3 de este contrato y del maestro §63.7 que incluían ΔValidity en la tupla causal; no borra el historial.
9. No cierra AUD-001/004/005/007, XAUD-003/004/006 ni XSYNC-138-03/06. No autoriza freeze ni ejecución.


## 31. Identidad, versión y matching de snapshots

**Estado:** propuesta; crosswalk del maestro §72 y de `C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md`.

1. Separar TID (identidad semántica), SID (especificación), RID (realización técnica) y EID (evento/instancia).
2. Mantener IDs persistentes y opacos; versión, hash, estado, fecha y brazo son atributos/provenance, no identidad.
3. Evaluar continuidad mediante firma semántica pre/post, operación nuclear, invariantes, restricciones y semántica de fallo.
4. Un cambio de RID/SID no implica TID nueva; cambio material del contrato puede requerir nueva TID; mapping no resoluble produce ?.
5. Matching por ID exacto, alias documentado, mapping de versión, candidato semántico y adjudicación ciega; sin auto-fusión fuzzy.
6. Split/merge requiere mapping explícito, composición y granularidad G común; no equivalencia automática.
7. Diff exige frontera, unidad/contexto, catálogo, G y mapping compatibles. Sin ello, diff parcial o DIFF_NOT_COMPARABLE.
8. Registrar eventos ADD/REMOVE/MODIFY_STRUCTURAL/VERSION_CHANGE/SPLIT/MERGE/REWIRE/STATE_CHANGE/UNKNOWN/OUT_OF_SCOPE.
9. Si la identidad focal τ2 no corresponde entre t0 y t1, D_f* no es una transición de la misma transformación y no se calcula como tal.
10. No cierra AUD-004 ni XSYNC-138-03/06; faltan catálogo, esquema, tolerancias, reglas por clase, fixtures, oráculos y revisión independiente.


## 32. Reach_H, trayectorias y propagación 1/0/? (crosswalk C10-S §73)

**Estado:** propuesta; contrato detallado en C10_S_REACHABILITY_AND_TRAJECTORY_PROPAGATION_CONTRACT_DRAFT_001.md.

1. Reach_H* es alcanzabilidad estructural verdadera; Reach_H,obs es clasificación observada. No usar Reach_possible sin declarar truth/obs.
2. Una ruta exige T_acc*, App* desde estado intermedio, relaciones de composición, recursos/autorización/condiciones, temporalidad y snapshots/versiones compatibles.
3. App* condiciona recorrido desde un estado, pero no redefine accesibilidad T_acc*.
4. Conjunción por ruta: 1 si todos los necesarios 1; 0 si alguno necesario 0; ? si no hay 0 y alguno ?.
5. Disyunción de rutas: una ruta confirmada basta para Reach=1; Reach=0 exige cobertura exhaustiva y todas las rutas refutadas; en otro caso ?.
6. Truncamiento, catálogo incompleto, cobertura basal insuficiente o mapping no resuelto no permiten Reach=0.
7. H, G, ciclos, duraciones, recursos, concurrencia y terminación se fijan ex ante.
8. Selección, ejecución, Outcome y Value son downstream; no definen Reach.
9. No confundir ΔT_acc≠0 con ΔReach_H≠0.
10. AUD-005/007 permanecen abiertos hasta catálogo DGP, fixtures/oráculos, evaluación de cobertura/error y revisión independiente.


## 33. Inventario finito candidato y cobertura de rutas

**Estado:** propuesta de fixture, no aprobada; contrato detallado en C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md.

1. Universo abstracto candidato: S0 inicial, S1 intermedio alternativo, S2 intermedio focal, SF objetivo; F1=τ2 (S0→S2), F2 (S2→SF), A1 (S0→S1), A2 (S1→SF); composiciones F1→F2 y A1→A2. Los IDs son aliases locales, no TID canónicas.
2. Escenarios: R0 focal exclusiva; R1 alternativa basal estable; R2 alternativa afectada por B; R3 intento/provisión fallida. No se agrupan poblaciones/ITT ni se asume exclusión en R2.
3. G atómica, H=3 pasos y ciclos prohibidos en el fixture base son propuestas que requieren ratificación. H=3 no es un límite computacional intercambiable con el horizonte científico.
4. Abrir F1 no basta para Reach(SF): F2 debe ser accesible, aplicable y componible. La ruta A1→A2 puede mantener Reach(SF)=1 con F1 cerrada.
5. La ausencia de alternativas solo se declara con cobertura exhaustiva de catálogo, relaciones, condiciones, universo funcional, recursos, tiempo, identidad/versiones y observación.
6. Truth DGP permanece oculta al analizador; cada predicado conserva observed_state 1/0/? y evidencia/procedencia/cobertura. Outcome y Value no definen estado, aristas, accesibilidad ni Reach.
7. No se seleccionan comparador, población confirmatoria, F*, G/H ni parámetros; no se autoriza implementación, simulación o ejecución.


## 34. Reconciliación de H, reloj t0–t9 y S4-R

La auditoría C10_S_TEMPORAL_HORIZON_AND_S4R_INTEGRATION_AUDIT_DRAFT_001.md propone separar (i) reloj del estudio t0–t9, (ii) profundidad de ruta k=0…H y (iii) tiempo/ventanas internas de factibilidad. H=3 queda como profundidad máxima candidata, no como tres unidades temporales. Reach_H se calcula en t4 sobre snapshot postintervención t3, antes de conocimiento/selección/ejecución. App se evalúa desde el estado hipotético de entrada de cada paso; relación, recursos, autorización, ventanas y bloqueos se evalúan por prefijo. Si hay dinámica se requieren snapshots hipotéticos de rama inmutables; sin regla de actualización no se inventa dinámica.

Crosswalk propuesto: R0↔S4R-A; R1↔S4R-B; R2↔S4R-C; R3↔S4R-D. R0 requiere cobertura exhaustiva para declarar ausencia funcional. R2 introduce vía colateral; R3 no permite inferir accesibilidad desde asignación/intento. Propuesta no aprobada; no cierra AUD-005/007 ni selecciona D1/D2.


## 35. Matriz de predicados por paso y rama

La matriz C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md operacionaliza ID, ACC, APP, REL, COND, AUTH, RES, DEP, BLOCK, WIN y COV. En el fixture base, T_acc y las condiciones estructurales de snapshot se fijan en t3; APP se reevalúa desde el estado hipotético de entrada de cada paso; REL se comprueba por arista; RES/AUTH/WIN/BLOCK solo varían dentro de rama si una regla explícita lo permite. Las ramas F1→F2 y A1→A2 se evalúan por separado como alternativas potenciales, no como ejecuciones concurrentes.

Se introduce taxonomía I/S/T/R/D/E para invariancia, dependencia de estado, temporalidad, recursos, dinámica explícita y evidencia epistémica. La ausencia de regla de transición impide inventar cambios; se conserva snapshot o se propaga ?. Los valores por escenario, F*, recursos, ventanas, dinámica y cobertura siguen abiertos. Documento propuesto, no aprobado ni ejecutado.


## 36. Reconciliación semántica de transformaciones del fixture

La auditoría histórica C10_S_TRANSFORMATION_CARDS_HISTORICAL_RECONCILIATION_DRAFT_001.md reutiliza §§47–51 y 57–69. F1 es τ2 focal parcialmente especificada por B/§§62–63/67; su provisión técnica no equivale a aplicabilidad, ejecución ni éxito. F2 (S2→SF), A1 (S0→S1) y A2 (S1→SF) permanecen aliases topológicos sin función, precondiciones, recursos, permisos, ventanas o evidencia propios. SF es marcador formal y no define F* por sí mismo.

No se permite atribuir semánticas técnicas inventadas a F2/A1/A2. Antes de completar el DGP se requiere seleccionar explícitamente un microdominio sintético neutral y definir F* común, mecanismo focal, continuación y ruta alternativa. No se asignan valores generadores. Propuesta documental, no aprobada ni ejecutable.


## 37. Microdominio candidato para dar semántica a las transformaciones

La comparación C10_S_SYNTHETIC_MICRODOMAIN_OPTIONS_AND_SELECTION_RECOMMENDATION_DRAFT_001.md propone Opción A (migración de configuración entre entornos software) frente a integración de datos y flujo organizativo. Recomendación no aprobada: F1/τ2 convertiría configuración fuente con adaptador focal provisionado por B; F2 aplicaría y validaría en destino; A1 exportaría a formato neutral preexistente; A2 importaría/aplicaría mediante mecanismo nativo y validaría bajo el mismo F*. F* sería conformidad técnica de esquema, integridad y compatibilidad.

Las fichas son ilustrativas; no hay formatos, IDs, tolerancias, recursos ni predicados truth fijados. B no ejecuta F1/F2; la ruta alternativa debe ser mecanísticamente independiente en R0/R1; R2 representa afectación colateral. La selección del microdominio sigue pendiente de decisión explícita.


## 38. Auditoría de roles causales del microdominio Opción A

Se incorpora la distinción operativa: B=provisión/configuración del adaptador; C_dep=estado técnico de dependencia; A_f*=accesibilidad focal de τ2; F1=conversión ejecutada con adaptador disponible; App(F1,S0)=aplicabilidad a la configuración concreta; F2=aplicación/validación en destino; F*=criterio funcional común de la ruta completa. La expresión previa “F1 habilita y utiliza adaptador” es ambigua y no debe persistir en la especificación final: habilitar corresponde a B, convertir a F1/ejecución.

La política B no debe alterar C_auth, F*, dataset/oráculo, configuración fuente/destino, A1/A2, costes, latencia, seguridad, información o recursos pertinentes en el escenario focal aislado, salvo que se declaren y modelen como vías adicionales. La primera etapa debe evaluarse por separado para C_dep, A_f,1*, D_f*, ΔT_acc y Reach. Un cambio en C_dep no implica automáticamente cambio en los demás.

A1/A2 requieren mecanismo y dependencias propios; el oráculo F* común puede ser compartido como medición, no como mecanismo generador. R2 representa afectación de alternativa por B y compromete exclusión focal. Contrato propuesto, no aprobado.


## 39. Manifiesto de provisión y grafo de dependencias

El contrato C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md establece B como provisión/configuración aislada del adaptador, sin ejecutar F1/F2/A1/A2 ni modificar F*, oráculo, datos funcionales, C_auth basal o ruta alternativa. Se requiere separar C_dep (estado técnico) de A_f* (accesibilidad completa), y no inferir una primera etapa focal desde la primera etapa de C_dep.

La arquitectura candidata ARCH-B1 es sidecar/runtime aislado, aditivo, versionado, con permisos mínimos y cuotas; es recomendación para evaluación, no decisión ni implementación. B-M01…15 permanecen no inventariados hasta identificar componentes reales. Snapshots preB/postB/rollback y pruebas de comportamiento A1/A2 pre/post son requisitos de evidencia. Los nodos/aristas desconocidos propagan cobertura incompleta; la ausencia de un nodo no se deduce de que no aparezca en un inventario parcial.


## 40. Cobertura del grafo y estados de evidencia

El contrato C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md define U_G como universo candidato de nodos, aristas, predicados y rutas. Sus 23 nodos y 23 aristas son roles de inspección, no evidencia de existencia ni inventario exhaustivo. Se separan verdad estructural, cobertura, estado de evidencia e intención contractual. Los nodos/aristas desconocidos permanecen ?; cobertura parcial no permite declarar ausencia.

Predicados requeridos: ID, REL, COND, AUTH, RES, DEP, BLOCK, APP, ALT-A1, ALT-A2, ALT-DEP, ALT-F*, ORACLE y EXT. Las rutas candidatas Rτ2, RA12, Rshared, Rexternal y Runknown permanecen ?. Reach=0 y F_alt,0=0 requieren cobertura exhaustiva del universo relevante. El estado actual no permite clasificar R0/R1; R2 es posibilidad causal no observada.


## 41. Frontera, granularidad y dependencias de U_G (crosswalk C10-S §82)

**Estado:** propuesta documental; no inventario técnico observado ni aprobación del DGP.

1. Se aplica el contrato C10_S_SYSTEM_BOUNDARY_AND_GRAPH_GRANULARITY_CONTRACT_DRAFT_001.md. U_G de §§33/40 y C10-S §§81–82 es un catálogo de inspección, no un inventario real/exhaustivo.
2. Separar nodos cuando exista diferencia material de intervención, TID/SID/RID, versión, fallo/sustitución, interfaz, permisos, recursos, exposición causal, ruta o evidencia. Agregar solo si no se ocultan vías diferenciales ni dependencias compartidas; en duda, mantener separados o ?.
3. Registrar aristas dirigidas con tipo, ventana temporal, condición, brazos, versión, evidencia y cobertura. Calcular dependencias transitivas y marcar ciclos, carga dinámica, fallback, consumidores y nodos desconocidos. La independencia de A1/A2 respecto de B requiere análisis transitivo y evidencia pre/post; aislamiento nominal no basta.
4. Evaluar rutas alternativas respecto de una F* común, entrada admisible, C0, G, H, restricciones y tolerancias. F_alt,0=0 exige descarte exhaustivo dentro del universo operativo declarado; una búsqueda sin hallazgos no basta.
5. Registrar servicios externos y opacos como dependencias explícitas, con contrato observable y exposición a B. La opacidad mantiene incertidumbre y no elimina vías colaterales.
6. Separar capacidad instalada, disponibilidad compartida temporal, reserva/asignación por unidad/ruta y consumo en ejecución. No retrotraer consumo post-ejecución a accesibilidad basal.
7. Hash/build distinto no implica nueva identidad; cambios materiales en función, contrato, precondiciones, composición, permisos, recursos, fallos o criterio de resultado exigen snapshot/mapping y revisión de continuidad.
8. Cobertura COMPLETE se refiere solo al universo operativo delimitado y versionado, no a exhaustividad ontológica absoluta. MISSING/NO INVENTARIADO no equivale a 0; PARTIAL no equivale a COMPLETE.
9. Si dependencia crítica, servicio externo, ruta alternativa o dimensión de cobertura queda desconocida, conservar ?. No declarar Reach_H=0, F_alt,0=0 ni independencia de B. Si B puede afectar rutas/recursos/permiso/servicio compartido, mantener vía colateral y estimando de paquete salvo identificación adicional.
10. La plantilla de inventario y el protocolo de evidencia son artefactos documentales; no autorizan inspección/instalación ni ejecución técnica. A_f*, F_alt,0 y Reach_H siguen indeterminados hasta que exista evidencia válida y adjudicada.


## 42. Plantilla documental de inventario U_G y evidencia (crosswalk C10-S §83)

La plantilla C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md define registros separados de nodos, aristas, rutas, predicados por paso/tiempo, snapshots/fuentes y cobertura. Exige identidad/versionado, procedencia, evidencia, cobertura, evaluador/cegamiento y motivo de indeterminación. Las filas ilustrativas son solo esquema: no acreditan componentes ni relaciones reales.

La columna truth_dgp queda restringida al generador/evaluador independiente y no se expone al analizador. Sin inventario observado, los estados técnicos permanecen ?. NONE/PARTIAL/COMPLETE describen cobertura y no truth estructural. La plantilla no autoriza inspección, instalación ni ejecución.


## 43. Crosswalk U_G §81 con plantilla de inventario (C10-S §84)

La plantilla registra 23/23 roles de nodo, 23/23 IDs padre de arista, 14/14 predicados y 5/5 clases de ruta. Las relaciones mult destino se normalizan en filas binarias enlazadas al ID padre; E07 se representa como regla lógica, no arista técnica. El esquema contempla 39 filas binarias candidatas, no observadas.

Se señalan tres problemas que el DGP deberá resolver antes del freeze: E22 referencia selección/ejecución sin nodos/eventos explícitos; N16 agrupa F*, oráculo y adjudicación; N23 agrupa ejecución, Outcome y Value. Se separan además las clases primarias Rτ2/RA12/Rshared/Rexternal/Runknown de subtipos native/manual/fallback/recovery. El código completo de predicado se conserva separado de su familia.

No se asigna truth ni observación. Cobertura NONE; no se declara inventario ni topología completa. Esta reconciliación no modifica el reloj t0–t9 ni los roles causales.


## 44. Protocolo de procedencia y adjudicación U_G

C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md define S1–S8, los campos de procedencia, evidencia mínima por objeto, cobertura negativa, cobertura por dimensión/denominador, doble evaluación cegada, adjudicación y reglas trivalentes. Separa evidencia declarativa de configuración/runtime/funcional; no permite inferir ausencia por falta de logs o búsqueda sin cobertura.

Para el DGP, el protocolo exige separar truth_dgp_restricted de observed_state; la truth queda en generador/evaluador independiente y no se expone al analizador. Los evaluadores de inventario se mantienen cegados a Outcome/Value y, cuando sea viable, a Z/B. Una discrepancia no resuelta mantiene ?. Las reglas de evidencia no cambian el reloj t0–t9 ni convierten C_dep en A_f*.

Protocolo documental no aplicado; no añade observaciones, parámetros ni truth. Cobertura NONE; A_f*, F_alt,0 y Reach_H siguen ?.


## 45. Esquema de captura normalizado y segregación de truth DGP

La plantilla U_G §§12–13 establece registros separados EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER con denominadores, EVALUATOR_ASSESSMENT por evaluador y ADJUDICATION_REGISTER. Cada clasificación se enlaza a evidencia por cadena de IDs, con alcance, versión y tiempo compatibles.

La truth del DGP se elimina de la tabla de predicados analítica y queda segregada en el entorno del generador/evaluador autorizado, fuera del acceso del analizador. El esquema no altera roles causales ni reloj t0–t9. Se preservan observed_state, evidence_status y coverage_status como dimensiones distintas.

Especificación documental, no implementación ni prueba de seguridad. No hay truth poblada ni evidencia real; cobertura NONE y estados técnicos ?.


## 46. Consistencia de esquema y separación de registros

La plantilla U_G §§12.9–12.10 fija dominios candidatos para observed_state, evidence_status, coverage_status y review_adjudication_status, además de tipos de ID, timestamps, hashes, conteos y cegamiento. CLAIM_EVIDENCE_LINK es relación 1:N y apunta a object_record_id; los evaluadores E1/E2 permanecen en filas separadas. La truth del DGP sigue segregada y no se incorpora al esquema analítico.

Especificación documental, no parser ni validación de seguridad ejecutados. El esquema no está aprobado ni implementado.


## 47. Referencias de evidencia por evaluador y adjudicación

EVALUATOR_ASSESSMENT utiliza evaluator_record_id singular y object_record_id. ADJUDICATION_REGISTER enlaza E1/E2 por sus IDs de evaluación. CLAIM_EVIDENCE_LINK permite reconstruir la evidencia revisada por evaluador/adjudicador mediante relaciones, sin listas serializadas. Los registros de objeto mantienen evaluator_record_ids solo como navegación, no como sustituto del registro independiente.

La comprobación estática de alineación de las diez tablas es documental; no prueba FKs, unicidad, tipos, seguridad ni cegamiento. No se altera truth DGP ni reloj causal.


## 15. Propuesta de fichas transformacionales Opción A — referencia de diseño

Se incorpora como propuesta externa al contrato temporal/rol `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md`. Para el escenario de migración de configuración entre entornos software, F1/τ2 es conversión focal S0→S2; F2 aplicación/verificación S2→SF; A1 exportación neutral S0→S1; A2 importación/aplicación nativa S1→SF. F* es el contrato común de conformidad técnica, independiente de Outcome/Value.

Esta semántica es candidata y no modifica retroactivamente truth, ecuaciones ni roles del DGP. La Opción A no consta como formalmente seleccionada/aprobada; los valores generadores, H/G/C0, recursos, ventanas, versiones, mappings y tolerancias siguen abiertos. La apertura de F1 no implica accesibilidad/aplicabilidad de F2 ni Reach(SF)=1; la ruta A1→A2 solo es substituible si satisface el mismo F* con cobertura y oráculo válidos. B no ejecuta F1/F2/A1/A2.


## 16. Microdominio seleccionado y F* de trabajo — DEC-C10-051

Opción A —migración de configuración entre dos entornos software— queda seleccionada para el diseño C10-S. F* se adopta como contrato funcional de trabajo candidato: la ruta completa debe producir y aplicar una configuración en el entorno destino conforme a propiedades obligatorias de esquema, integridad, compatibilidad, preservación funcional y seguridad.

Las fichas F1/F2/A1/A2 se interpretan según el documento `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md`. Esta decisión no fija aún mappings, versiones, TID/SID/RID, H/G/C0, recursos, ventanas, tolerancias ni oráculo; no modifica truth del DGP ni autoriza generación/ejecución. D1/D2 y R0–R3 permanecen separados y abiertos.


## 17. Matriz operacional de F* y límites de adjudicación

La evaluación de conformidad de las rutas se rige, como diseño candidato, por `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md`. F* se adjudica mediante propiedades obligatorias aplicables y regla no compensatoria: 1 solo si todas cumplen; 0 si alguna incumple; ? si falta evidencia concluyente y no existe fallo confirmado. NA exige no aplicabilidad preespecificada y justificada.

Esta regla de medición no sustituye los mecanismos causales del DGP. El truth generador, la observación del analizador, accesibilidad, aplicabilidad, ejecución, Outcome y Value permanecen separados. La matriz no autoriza asignar valores truth ni completar parámetros sin decisión/evidencia.


## 18. Preservación semántica FP-03

La evaluación de preservación semántica se especifica en `C10_S_FP03_SEMANTIC_PRESERVATION_CONTRACT_DRAFT_001.md`. Las dimensiones SM-01…SM-10 son candidatas; el DGP no debe asignarles truth hasta que se delimiten el objeto de configuración, las propiedades obligatorias, mappings y cobertura. El analizador solo recibe observaciones permitidas; no se filtra truth generador.

La selección de Opción A no basta para inferir mecanismos técnicos de F1/F2/A1/A2. Las fichas actuales describen roles candidatos, no identidades TID ni contratos implementables. La semántica funcional concreta deberá derivarse de una decisión de diseño explícita antes de completar R0–R3.


## 19. Alcance candidato del DGP base y contratos abstractos de configuración

La propuesta `C10_S_BASE_DGP_SCOPE_AND_ABSTRACT_CONFIGURATION_CONTRACT_PROPOSAL_DRAFT_001.md` deriva de DEC-C10-051/052 una partición candidata: componentes, parámetros tipados, referencias y reglas/restricciones como familias constitutivas del DGP base; políticas asociadas como módulo condicional; metadatos contractuales como soporte de identidad/procedencia, con extensiones desconocidas en escenarios condicionales.

Esta partición no modifica la estructura conceptual de seis elementos seleccionada por DEC-C10-052 ni convierte POL en inexistente: propone que el DGP base pueda declarar ex ante ausencia de políticas migrables y que escenarios secundarios estudien su preservación y su separación de FP-05.

Se estructuran tres contratos: C_src (contenido y semántica de origen), C_dst (representación y restricciones de destino) y M (mapping versionado para evaluación, no capa operativa persistida adicional). Se enumeran predicados BASE-CMP/PAR/REF/RULE/MAP-COVERAGE/APPLIED-STATE como candidatos, sin truth ni valores.

**Estado:** propuesta no aprobada; gramática de reglas, dominios, cardinalidad, ausencia/null/default, mappings, alcance de POL, oráculo y obligatoriedad siguen abiertos. No se asigna truth ni se autoriza generación/ejecución.


## 20. Partición aprobada del DGP base — DEC-C10-053

La partición descrita en §19 queda aprobada por decisión explícita del usuario: componentes, parámetros tipados, referencias y reglas/restricciones de gramática mínima son constitutivos del DGP base; POL queda como módulo/escenario condicional secundario; metadatos contractuales son soporte obligatorio de identidad, versionado y procedencia, con extensiones desconocidas condicionales.

La estructura conceptual de seis elementos de DEC-C10-052 permanece intacta. POL no se elimina del objeto; el escenario base declarará ex ante si no contiene políticas migrables. Esta decisión no fija todavía gramática, dominios, cardinalidad, mappings, tolerancias, oráculo ni truth.


## 21. Gramática mínima y dominio de tipos — propuesta posterior a DEC-C10-053

Se crea `C10_S_MINIMAL_RULE_GRAMMAR_AND_PARAMETER_TYPE_DOMAIN_PROPOSAL_DRAFT_001.md`. Propone tipos abstractos BOOL, INT, DECIMAL, ENUM, STRING y REF; estados de parámetro ABSENT/NULL/DEFAULT/VALUE; operadores comparativos, pertenencia, estado y referencia; composición AND/OR/NOT; y efectos declarativos finitos sin ejecución arbitraria.

Se propone semántica de expresión TRUE/FALSE/UNKNOWN, que deberá distinguirse de la adjudicación de evidencia 1/0/?. Límites de dominio, tamaño/profundidad, efectos, política UNKNOWN y conversión siguen abiertos. No se asigna truth ni se ejecuta.


## 22. Perfil aprobado de dominios finitos y complejidad — DEC-C10-054

El DGP base adopta el perfil estructural aprobado: dominios finitos por clave; tipos BOOL/INT/DECIMAL/ENUM/STRING/REF con restricciones declaradas; estados ABSENT/NULL/DEFAULT/VALUE y subtipos de DEFAULT; AST declarativo acíclico sin ejecución arbitraria; operadores tipados y composición NOT/AND/OR; presupuesto máximo 4 niveles, 16 átomos/regla y 16 reglas/paquete; efectos REQUIRE/FORBID; SELECT_ENUM_VALUE excluido del núcleo. UNKNOWN no se transforma silenciosamente en TRUE/FALSE.

Los límites concretos de valores, escalas, catálogos y cadenas se especificarán por clave una vez definido el contrato abstracto. No se asignan valores ni truth en este contrato. Mapping, conflictos, tolerancias y oráculo siguen abiertos. DEC-C10-054 aprueba perfil de diseño, no implementación, validación o ejecución.


## 23. Matriz abstracta de parámetros y mapping C_src→C_dst/M

La operacionalización del perfil aprobado se desarrolla en `C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md`. El contrato por clave deberá declarar tipo, dominio, unidad, estados, obligatoriedad, default, normalización, conversiones, versiones y requisito de evidencia. M será mapping de evaluación versionado, no capa persistida adicional.

La comparación distinguirá C_src, C_dst declarado, C_dst realmente aplicado y E_dst (entorno externo al objeto). FP-01 cubre estructura/tipos, FP-02 integridad relacional y FP-03 preservación semántica; cada discrepancia deberá declarar predicado primario para evitar doble conteo. Los predicados de la matriz son candidatos, no aceptados ni validados. Claves, valores, dominios concretos, obligatoriedad/NA, mappings, oráculo y evidencia siguen abiertos. Sin truth ni ejecución.

## 24. Reconciliación con el protocolo científico autocontenido y la arquitectura vigente (2026-11-05)

1. La separación Generador/Analizador/Evaluador es una separación de roles computacionales y de acceso a datos. «Evaluador independiente» significa independiente del analizador y con acceso a truth solo después de congelar la salida; no implica ni exige un revisor humano externo.
2. La continuidad científica se audita como AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT. No se requiere R1/R2 para avanzar; la ausencia de revisores externos no bloquea el diseño ni una ejecución sintética autorizada.
3. La cadena del DGP se interpreta junto con la arquitectura relacional de §60 del maestro: T_cap(sys,t) y T_acc(i,t) no se colapsan; frontera, recursos compartidos/asignados y unidad deben indexarse explícitamente.
4. La definición focal A_f* de §§59 y 63 del maestro sigue siendo candidata y requiere clasificación de predicados; App_f* es separada.
5. Para snapshots, §71 del maestro prevalece sobre la formulación histórica que incorporaba ΔValidity en ΔT_acc: S_T* y E_T son objetos separados; ΔT_acc* es estructural y ΔE_T epistémico.
6. Reach_H* y Reach_H,obs, propagación 1/0/? y Reach_H−/Reach_H+ siguen el contrato del maestro §§73–75. H=3 es profundidad candidata, no duración temporal.
7. La estadística se cierra según la fuente 165–183 y el plan Draft 004: estimandos ITT-A/O/V, LATE por resultado, heterogeneidad/compliers, sensibilidad δ/γ, potencia/precisión por estimando, búsqueda de N, R por error Monte Carlo y reproducibilidad.
8. Este addendum no aprueba fórmulas, comparador D1/D2, Value, parámetros, implementación, simulación ni ejecución.


## 26. Precedencia material D2 por DEC-C10-067

DEC-C10-067 acepta el contrato conceptual de las políticas (B_{g0}^{D2}) y (B_{g1}^{D2}). El control no programa ni inicia provisión focal; el tratamiento programa provisión técnica focal con artefacto/versionado identificados y verificación separada de los cuatro componentes técnicos. Asignación, intento programado/efectivo, recepción, éxito, (C_{dep}^{*}), (A_f^{*}) y (D_f^{*}) no se sustituyen entre sí.

Se mantienen comunes (C_{auth,base}=1), elegibilidad, recursos no focales, capacidad, información basal y medición/adjudicación en el DGP aislado. Cualquier cambio diferencial de permisos, recursos, costes, latencia, calidad, seguridad, información, incentivos o alternativas debe registrarse como vía colateral. El ITT de Z sigue siendo efecto de política/paquete; no se etiqueta automáticamente como efecto puro de accesibilidad.

Permanecen abiertos actor, artefacto/hash, recepción, ventanas, reintentos, rollback, evidencia de componentes, detección de provisión de fondo y rutas alternativas. (s=0.80) no está validado. No se aprueban parámetros ni DGP, ni se autoriza freeze, implementación, simulación o ejecución científica.


## 27. Regla trivalente de agregación de A_f* y D_f observado — reconciliación C10-S (2026-11-06)

**Fuente:** `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md §10`.  
**Estado:** reconciliación documental asistida; no aprobada, no congelada, no ejecutada.

1. Se preservan como dominios ortogonales `observed_state={1,0,?}`, `evidence_status={AVAILABLE,MISSING,CONFLICTING}`, `coverage_status={NONE,PARTIAL,COMPLETE}`, adjudicación y `truth_dgp` restringida. No convertir MISSING/NONE/PARTIAL/no inventariado en 0.
2. Para la conjunción candidata `ID∧REL∧COND∧AUTH∧RES∧DEP∧¬BLOCK`: un predicado necesario adjudicado 0 con evidencia válida, alcance compatible y cobertura suficiente basta para `A_f^{obs}=0`; todos los términos necesarios 1 con matching/comparabilidad y cobertura adecuados permiten 1; en los demás casos, ?.
3. `DEP_f^{obs}` es disyunción de rutas admisibles: una ruta confirmada 1 basta para 1; 0 exige todas las rutas del universo operativo declarado refutadas y cobertura COMPLETE, incluida resolución de Runknown/rutas externas/compartidas/alternativas; en otro caso ?.
4. Un `C_dep=0` no implica `DEP=0) si existe ruta alternativa admisible. La equivalencia solo rige bajo ruta única estipulada e inventario/cobertura demostrados.
5. `D_f^{obs}=1) solo para baseline 0 y post 1; es 0 si baseline=1 o post=0; en los demás casos ?. Snapshots no comparables o identidad τ2 unresolved producen NOT_COMPARABLE/?; nunca 0.
6. La elegibilidad verdadera focal exige `A_{f,base}^*=0) pre-Z; `A_{f,base}^{obs}=0) no la sustituye sin tratamiento explícito del error de clasificación.

La regla formal y sus tablas de casos están en el documento de referencia. No cierra MEAS-G2…G8, UG-SCH-10, XSYNC, PROV, MD-C1/MD-C4 o IV; no cambia la fórmula, decisiones, autorización ni estimandos.



## 28. Crosswalk temporal y de roles para escenarios adversariales Opción A (2026-11-06)

**Estado:** addendum de integración documental; no congela la semántica funcional ni el DGP. Reutiliza el reloj t−1/t0–t9 de §2, la separación de roles de §6, la reconciliación temporal-causal de §23, el contrato Opción A de §§37–38 y los escenarios C10-S-IV-AUD-001 §12. No crea un segundo reloj.

### 28.1 Mapa común variable×tiempo×rol

| Tiempo | Variables/objetos a mantener separados | Papel causal/medición | Generador | Analizador | Evaluador independiente |
|---|---|---|---|---|---|
| t−1 | X,H0, unidad/clúster, frontera, identidad/versiones τ2/F1/F2/A1/A2, A_f,base*, T_acc,base*, C_dep,base, F_alt,base, recursos/capacidad disponibles, C_auth,base, datos S0/SF, F*, oráculo y regla O/V basales | Elegibilidad, soporte, comparabilidad, alternativas basales y covariables; nunca reconstruir desde post-Z | Truth y observaciones simuladas | Solo observaciones basales y evidencia accesible; no truth | Truth, parámetros, potenciales y observaciones |
| t0 | Z, probabilidad y unidad de asignación, estrato/cluster | Asignación de política; no es recepción, intento ni tratamiento recibido | Sí | Sí | Sí |
| t1 | B_assigned/offered/received, versión/hash, actor/disparador, W_programmed, W_attempt, comunicaciones/formación iniciales, exposición a otros tratamientos | Política e intento; inicio de vías colaterales, recursos y conocimiento; registrar incumplimiento y provisión de fondo | Sí | Registros observables | Sí |
| t2 | S_install, C_install/integrity/compat/oper, C_dep*, snapshots B-M01…15, ACL técnica vs C_auth, recursos disponibles/reservados/consumidos, capacidad, datos/mapping/App, estado A1/A2 y dependencias, seguridad/coste/latencia | Estado técnico y cambios colaterales posteriores a B; no equivalen a A_f*, Reach ni ejecución | Truth y observación | Evidencia observable, nunca truth oculta | Sí |
| t3 | A_f,post*, A_f,obs, D_f*, T_acc,post*, ΔT_acc*, App_f*, snapshot F1/τ2; evidencia/cobertura de medición | Apertura focal y estructura accesible antes de K/selección/ejecución; observabilidad diferencial se registra aparte en ΔE_T | Truth y observación | A_f,obs/T_acc,obs/evidencia; no truth ni ΔT_acc* oculto | Sí |
| t4 | Reach_H*, Reach_H,obs, Π_H, rutas Rτ2/RA12/Rshared/Rexternal/Runknown y condiciones de composición | Consecuencias estructurales de accesibilidad y alternativas; no usar ejecución observada para reconstruir Reach | Truth y observación | Reach/Π observables o derivados con estados 1/0/? | Sí |
| t5 | K, Consider, mensajes recibidos, conocimiento de F1 y A1/A2, observabilidad del agente | Mediación epistémica downstream; no ajustar mecánicamente ITT por K post-Z | Sí | Medidas observadas | Sí |
| t6 | Sel, Start, actor, motivo, fecha y posibilidad considerada | Selección e inicio separados; posibles mediadores | Sí | Sí | Sí |
| t7 | Exec parcial/completa, fallos/interrupciones, F1/F2/A1/A2 realmente ejecutadas, recursos consumidos, residuos | Ejecución no redefine retrospectivamente T_acc ni Reach basal | Sí | Sí | Sí |
| t8 | O* y O_obs, R_O, regla/dataset/oráculo/versionado, latencia/calidad/seguridad relevantes para Outcome | Estado verdadero de resultado separado de observación y de la definición del oráculo | Sí | O_obs y procedencia pública; no O* oculto | Sí |
| t9 | V* y V_obs, R_V, regla/versionado, beneficiario/horizonte, coste/riesgo/recursos | Valor verdadero y observado separados; puede cambiar aunque O* permanezca constante | Sí | V_obs y regla pública; no V* oculto | Sí |
| t+1… | snapshots post-ejecución, caché/índice/estado residual, rollback, recursos y exposición de unidades/periodos siguientes | Carryover/spillover; nunca sobrescribir t−1…t9 | Sí | Evidencia observable y cobertura | Sí |

La notación O*/O_obs y V*/V_obs se introduce aquí como separación explícita de truth y observación para los contratos adversariales; no sustituye silenciosamente O_i/V_i en §§2–7. Antes de freeze se deberá fijar el nombre de campo canónico y el oráculo, sin mezclar estado de resultado con regla de medición. F* funcional de conformidad de transformación y el oráculo de O/V son objetos distintos.

### 28.2 Crosswalk por escenario

| Escenario | Manipulación principal y momento | Variables/tiempos afectados | Variables que deben permanecer invariantes en el contraste aislado | Diagnóstico esperado |
|---|---|---|---|---|
| R0 / EXC-F0 | B provisiona adaptador en t1; éxito técnico se verifica en t2 | C_dep* (t2) → A_f,post*/D_f*/ΔT_acc* (t3) → Reach/Π (t4) → O (t8), V (t9) | F2, A1/A2, F*, datos, C_auth, recursos no focales, K, costes/riesgos y observación/oráculo; verificar no solo estipular | Control positivo de ruta focal; LATE_f solo candidato tras gates IV completos |
| R1 | A1→A2 ya factible en t−1 y no cambia tras B | F_alt,base (t−1), snapshots alternativos t2/t3, Reach/Π t4 | B no modifica A1/A2, dependencias, recursos ni medición | No es violación por mera existencia de alternativa; puede bloquear cambio en Reach o generar heterogeneidad |
| R2 / EXC-B14 | B modifica A1/A2 o dependencias en t2 | Snapshot/diff alternativo t−1→t2/t3; Reach/Π t4; Exec t7; O/V t8/t9 | Mantener focal D_f* y las otras superficies fijas para aislar esta vía | Vía colateral/efecto de paquete; no LATE_f focal bajo exclusión violada |
| R3 | Intento W_attempt en t1; provisión no alcanza C_dep* en t2 | W_programmed/W_attempt (t1), C_dep* (t2), D_f* (t3); consumo/residuo t2/t+1 si aplica | Sin otras vías en subcaso base; separar subcaso con consumo/residuo | Primera etapa focal nula/débil; no asumir ITT nulo si hay coste o residuo |
| EXC-B06 | B cambia S0/datos/mapping/App/F* técnico fuera de D_f* en t2 | Datos/App/F* (t−1,t2), Exec (t7), O* (t8) | D_f* fijo; oráculo de O invariante | Vía directa a Outcome; exclusión focal violada |
| EXC-B09/B12 | B cambia riesgo/coste/latencia/recursos relevantes en t2/t7 | Métricas de coste/riesgo/latencia (t2,t7), O* (t8), V* (t9) | Subcaso Value: O* constante; regla V y observación invariantes | Vía directa a Value; no inferir O→V completo |
| EXC-B10-K | B comunica/formación en t1; cambia K/Consider en t5 | Mensajes (t1), K/Consider (t5), Sel/Start (t6), Exec/O/V (t7–t9) | D_f* y observabilidad fijos para aislar K | Vía epistémica no focal; no ajustar por K post-Z |
| EXC-B10-OBS | B cambia logs/permisos/retención/cobertura en t2/t3/t8/t9 | ΔE_T y R_A/R_O/R_V por brazo/tiempo; estados verdaderos constantes | Truth estructural y O*/V* constantes | Error/missingness diferencial; gate IV-G6, no confundir con vía causal verdadera |
| EXC-B13 | B altera oráculo/dataset/regla de O o V en t8/t9 | Versiones y definición de resultado/valor por brazo | Mecanismo de estado subyacente constante | No comparabilidad del resultado; no estimar contraste común sin armonización válida |
| EXC-B07 / interferencia | B consume/reserva recursos compartidos desde t1/t2 | Pool y mapa de exposición por unidad/cluster t1–t2; Reach/Exec/O/V t4/t7–t9 | Contraste individual aislado solo si pool no compartido o exposición modelada | SUTVA/independencia individual no sostenibles sin régimen de exposición o cluster |
| EXC-B11/B15 / carryover | B deja estado tras rollback/fin de periodo | Snapshot t+1… y exposición de siguientes unidades/periodos | Sin residuo solo en control negativo explícito y verificado | Consistencia temporal/interferencia; no Wald individual estándar |

### 28.3 Reglas de rol y de no fuga

1. El generador produce truth, potenciales y observaciones simuladas; mantiene truth de rutas, D_f*, O*, V*, mecanismos colaterales y parámetros fuera del analizador.
2. El analizador recibe Z/B/W, snapshots y evidencia observables, A_f,obs, T_acc,obs, Reach/Π observables, K/Sel/Exec observados, O_obs/V_obs y reglas públicas versionadas. No recibe truth, potenciales, mecanismos ocultos ni flags de escenario que revelen la respuesta.
3. El evaluador accede a truth y parámetros solo después de congelar la salida del analizador; calcula recuperación, clasificación de gates y errores por estimando y escenario.
4. La manipulación del oráculo (B-M13) no debe confundirse con la manipulación del estado de Outcome/Value; la manipulación de cobertura (B-M10-OBS) no debe cambiar truth.
5. Escenarios de interferencia requieren indexación por unidad i, unidad expuesta j, cluster/pool y tiempo. No codificar el spillover como una simple covariable individual.
6. Los controles negativos deben comprobar que las variables declaradas invariantes realmente permanecen invariantes dentro del DGP; el contrato no autoriza afirmar invariancia en sistemas reales.

### 28.4 Huecos detectados antes de parametrizar

- F1=τ2 y su relación con el artefacto/adaptador, F2 y la semántica exacta de A1/A2 aún requieren contrato funcional único y versionado; las etiquetas no son fixtures técnicos.
- Precedencia de selección: DEC-C10-051 (Decision Log §45; recomendación de microdominio §13) selecciona Opción A como microdominio de trabajo y adopta F* como contrato funcional candidato. Por tanto, las frases históricas de §37 y de la auditoría de compatibilidad que describen Opción A como no seleccionada quedan supersedidas solo respecto al estado de selección. No quedan supersedidas sus reservas sobre el cierre operacional: F1/τ2, adaptador, F2, A1/A2, propiedades de F*, mappings, identidades/versiones, tolerancias y oráculo siguen pendientes. La selección del microdominio no equivale a aprobación de esas fichas ni a freeze.
- Los campos O*/O_obs y V*/V_obs, regla de Value, horizonte y beneficiario requieren nombres/esquemas canónicos y matching con los contratos estadísticos existentes.
- t+1… requiere unidad temporal y regla de washout/rollback por escenario; no asumir ausencia de carryover.
- La unidad de interferencia, pool compartido, mapa de exposición y régimen de asignación por cluster deben fijarse antes de parametrizar escenarios de spillover.
- F* técnico, oráculo de Outcome y regla de Value deben ser tres artefactos diferenciados, versionados y cegados al analizador salvo sus especificaciones públicas.

**Dictamen:** crosswalk documental integrado; los escenarios siguen sin parametrizar, serializar ni ejecutar. No cierra exclusión, IV-G6, consistencia, interferencia, Value ni Design Freeze. No autoriza implementación ni ejecución.


### 3.3.1. Nota de precedencia (2026-11-10)

La tupla de verdad estructural de esta sección se interpreta conforme a §30: ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*). ΔValidity_e es epistémica y pertenece a ΔE_T. La antigua mención ΔValidity/ΔState no constituye una definición alternativa vigente. El crosswalk de ΔX* con C10-D1 §27.1 permanece pendiente; no asignar equivalencia automática.


### 3.3.2. Tipado semántico de X* y precedencia de crosswalk (2026-11-10)

X_t* representa el estado/contexto efectivo del sistema-unidad-entorno-tiempo que es constitutivo de la relación de accesibilidad en ese momento, excluyendo transformaciones (U*), relaciones (R*), reglas/predicados/configuraciones de realizabilidad (C*) y evidencia (E_T). Su diff ΔX* no es una transformación adicional ni una sexta coordenada analítica C10-D1.

Clasificar cada campo por función semántica:
- U*: identidad/estado de una transformación.
- R*: relación tipada/dependencia entre objetos o transformaciones.
- C*: condición, predicado, restricción o configuración de realizabilidad.
- X*: valor/estado contextual efectivo constitutivo que condiciona accesibilidad, pero no es por sí mismo regla/relación/transformación.
- E_T: evidencia, cobertura, validez epistémica, provenance y adjudicación.

Si un campo X resulta ser una regla o predicado, reclasificarlo en C* con mapping explícito. Si es historia no constitutiva, evaluar su pertenencia a q según factibilidad y soporte. Si no altera accesibilidad dentro de la frontera/horizonte, queda fuera del mediador. Si no puede decidirse, estado UNKNOWN/?.

Para el crosswalk con C10-D1 §27.1, ΔX* se conserva como contexto causal del DGP; sus consecuencias sobre accesibilidad se reflejan en A⁺/A⁻/A^reconf/ΔR/ΔC, sin doble conteo. Un campo que mezcle valor contextual y regla debe descomponerse o permanecer UNKNOWN. Cada campo requiere field_id, definición, unidad/frontera, tiempo, tipo, regla de diff, mapping, event_id, truth/observed, overlap y adjudicación.

Esta regla no completa el roster del microdominio ni convierte el crosswalk en aprobado. MED-02c/d permanecen OPEN.


### 3.3.3. DAG Opción A/D2 y regla de no doble mediación (2026-11-10)

Aplicar el DAG integrado del maestro §233. El orden temporal es t−1 basal; t0 Z; t1 B/W_programmed/W_attempt; t2 S_install/componentes/C_dep*; t3 snapshot U*/R*/C*/X* y T_acc/A_f/ΔT_acc; t4 Reach/Π_H; t5 K/consideración; t6 selección/inicio; t7 ejecución focal F1→F2 o alternativa A1→A2; t8 Outcome; t9 Value. La observación E_T discurre en canal paralelo y no integra truth estructural.

A_f,1* es predicado/proyección focal de T_acc,1 y D_f* es indicador derivado de A_f,0*/A_f,1*. No tratarlos como mediadores seriales independientes de ΔT_acc*. Para mediación secundaria, el objeto candidato es la distribución conjunta y factible de ΔT_acc*; se preservan sus dependencias y se requiere orden temporal, positividad y estrategia para confusores mediador–Outcome inducidos por B.

B-M01…15 siguen siendo superficies de inspección; el DAG enumera rutas colaterales que deben auditarse, pero no afirma que estén presentes o ausentes. Si B cambia diferencialmente recursos, capacidad, permisos/seguridad, A1/A2, costes/latencia/calidad, información/incentivos, medición o condiciones comunes, el ITT sigue siendo efecto de política/paquete. No ajustar el ITT por variables post-Z. La correspondencia B→g^Af y la interpretación de ITT como θ_A(q) requieren demostrar régimen común, soporte, consistencia y exclusión.

Estado: DAG candidato definido; inventario de campo, valores truth/observed, invariancia, soporte, unidad/interferencia y estimandos finales OPEN. Sin freeze ni autorización de ejecución.


## 13. Especialización propuesta de t9 para la variante B — C10S-B-VALUE-MIN-001 (2026-11-11)

El evento t9 (Value) mantiene su contrato genérico: V_i, regla/versión, beneficiario, horizonte y R_V,i; Value se evalúa bajo regla fija e independiente. Para B, C10S-B-VALUE-MIN-001 propone requisitos previos de admisibilidad: identidad/tipo sintético versionado; relación con unidad de servicio y unidad experimental; elegibilidad y demanda pre-Z; consecuencia valorada; perspectiva/autoridad; población/horizonte, cardinalidad y provenance. Se mantienen separados unidad experimental, unidad lógica de servicio, beneficiario, actor ejecutor y evaluador. No inferir beneficiario de CMP.owner, CMP-SERVICE-LOGIC-001, LOGICAL_SERVICE_UNIT ni actor. Demanda basal no equivale a selección/uso/ejecución. V_j no puede recodificar A_f/ΔT_acc, Reach ni Outcome técnico ni incorporar circularmente el efecto que se quiere estimar. Vías alternativas B→consecuencia/Value deben permanecer explícitas; si existen, ITT_Z se interpreta como efecto de política/paquete salvo identificación adicional. El vector P179, §224, P182/P183 y el firewall Generator/Analyzer/Evaluator se preservan. Esta sección es propuesta documental para B: no selecciona beneficiario, demanda, perspectiva, dimensión, regla, escala ni parámetro; no altera A ni aprueba el contrato integrado.


## 14. Reconciliación temporal propuesta de necesidad B1 y solicitud (2026-11-11)

La aceptación del tipo B1 añade un constructo basal del beneficiario sin sustituir el reloj ni los eventos ya definidos en §2 y §§17–22.

- Need_preZ (verdad DGP) y cualquier E_req_preZ se estipulan/clasifican en t−1, antes de Z. Son distintos de la elegibilidad experimental P* y de las condiciones constitutivas de accesibilidad.
- La solicitud efectivamente formulada/registrada (Request_event) es un evento distinto de la necesidad basal. Su ventana y posición temporal exactas siguen OPEN.
- No se asigna por conveniencia Request_event a t5 Knowledge/Consider, t6 Selection/Start o t7 Execution. La relación semántica con esos eventos debe reconciliarse antes de extender el DAG o el esquema temporal.
- D_resource permanece la demanda operativa de recursos/capacidad del servicio, diferenciada de Need_preZ. Separar stock, disponibilidad/asignación, demanda operativa y consumo, como ya requiere el contrato.
- La operación/aceptación/rechazo/procesamiento de la solicitud, el estado técnico del servicio y la consecuencia del beneficiario son eventos/constructos distintos. No inferir satisfacción de la necesidad desde procesamiento correcto.
- Truth del Generator, evidencia observada del Analyzer y adjudicación del Evaluator siguen separados. Need_preZ=? o evidencia insuficiente no se imputa a 0. No se condiciona ITT a Request_event ni a variables post-Z.
- No se altera la secuencia t−1/t0…t9, el DAG aprobado/candidato, DEC-C10-066/067, D2/D1, ni se introduce un tiempo, variable física, fixture o parámetro.

Estado: propuesta documental de especialización B1; solicitud y su posición en el reloj OPEN; no implementación ni ejecución.


## 15. Ciclo de solicitud B1 como subregistro de eventos, sin ampliar el reloj DGP (2026-11-11)

La propuesta B1 §11 descompone el ciclo de solicitud en Request_opportunity, Request_attempt, Request_received, Request_admitted/rejected, Request_processing, Request_response y Beneficiary_consequence. Son eventos/estados del servicio y del beneficiario, no nuevas etapas transformacionales.

1. Se conserva el reloj basal t−1 y t0…t9. No se añade t5a/t6a/t7a ni se reinterpreta t5/t6/t7.
2. t5 K/Consider no equivale al intento de envío; t6 Sel/Start no equivale a admisión de la petición; t7 Exec transformacional no equivale a procesamiento del servicio.
3. El enlace entre request_id y transformación/trajectory_id puede ser 0:1, 1:1 o 1:N según contrato aún OPEN. No se presupone que cada petición desencadene transformación ni que una transformación corresponda a una sola petición.
4. Los eventos pueden registrarse en un subledger temporal con timestamps y referencias a snapshots existentes, preservando identidad/versionado y orden parcial. No se establece schema físico ni regla de orden total.
5. El contrato funcional aceptado de ENABLED/PROFILE/RUL orienta la admisión, pero no proporciona protocolo completo de recepción, payload, colas, errores, respuesta o SLA. No añadir semántica no aprobada.
6. En el primario sintético se recomienda evaluar una carga de oportunidades/peticiones estandarizada ex ante, presentada mediante harness externo idéntico después del snapshot de accesibilidad. El intento se registra aun cuando no exista recepción. Es un probe de carga, no demanda natural ni preferencia validada. Una rama de envío endógeno puede ser adversarial/secundaria.
7. No condicionar ITT ni población a intento, recepción, admisión, procesamiento o respuesta post-Z. No tratar no recepción como ausencia de necesidad ni respuesta técnica como Value.
8. La consecuencia del beneficiario se mantiene distinta de O técnico y de estado del servicio; regla y horizonte permanecen abiertos.

Estado: propuesta de subregistro de eventos; no cambia DAG, reloj, estimandos, parámetros, políticas ni autorización.
