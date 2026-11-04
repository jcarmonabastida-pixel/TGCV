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

`Z_i ∈ {0,1}` asigna la política técnica `B_g0` o `B_g1`. La asignación no es accesibilidad ni ejecución.

- `B_g0`: provisión técnica de menor probabilidad objetivo, `p0=.20`.
- `B_g1`: provisión técnica de mayor probabilidad objetivo, `p1=.80`.

Estos valores se conservan como parámetros ilustrativos de §30.2, sujetos a calibración del estado final verificado. Ambas ramas son políticas de provisión; g0 no significa necesariamente ausencia de provisión.

### 3.2 Intento, éxito y estado final

[
W_{attempt,i} \sim Bernoulli(\omega_{Z_i})
]

[
S_{install,i} \sim Bernoulli(s_{Z_i}(W_{attempt,i},X_i,H_{i0}))
]

[
C_{dep,i1}=C_{install,i1}\land C_{integrity,i1}\land C_{compat,i1}\land C_{oper,i1}
]

`ω_z` es probabilidad de intento; `s_z` modela éxito condicional. La probabilidad final de C_dep no se iguala a ω_z salvo que el procedimiento haga idénticos intento y éxito. Para preservar la verdad analítica de §30.5, el generador debe calibrar:

[
P(C_{dep,i1}=1\mid Z=0,P^*_{\tau2})=.20,\quad
P(C_{dep,i1}=1\mid Z=1,P^*_{\tau2})=.80
]

Si las condiciones restantes están satisfechas, estas probabilidades pueden coincidir con las probabilidades finales de accesibilidad focal. Si no, calcular `P(A_f,post*=1|Z=z)` desde todas las condiciones, no desde C_dep solamente.

### 3.3 Accesibilidad focal y cambio completo

[
A_{f,i0}^*=I(\text{todas las condiciones focales basales satisfechas})
]

[
A_{f,i1}^*=I(C_{dep,i1}=1\land C_{auth,base}=1\land C_{resource}=1\land C_{capacity}=1\land C_{info}=1\land C_{domain}=1\land C_{other}=1)
]

[
D_{f,i}=I(A_{f,i0}^*=0\land A_{f,i1}^*=1)
]

La población de apertura requiere `A_f,i0*=0` preasignación. `D_f` es la apertura basal→post; `A_f,post*` es el estado focal posterior. No intercambiar ambos cuando existan unidades con acceso basal.

El cambio completo del espacio se conserva como:

[
\Delta T_{acc,i}=T_{acc,i1}\ominus T_{acc,i0}
=(\Delta U_i,\Delta R_i,\Delta C_i,\Delta Validity_i,\Delta State_i)
]

[
A_{f,i}=h_f(\Delta T_{acc,i})
]

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
]

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
]

Bajo aleatorización y supuestos de diseño, estima el efecto de asignar las políticas de provisión. No se restringe a quienes cumplen, abren τ2, seleccionan o ejecutan.

### 5.2 Contraste de políticas de accesibilidad focal

[
\theta_{Af}(q^*)=E[V^{q^*,g_1}]-E[V^{q^*,g_0}]
]

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
]

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
]

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
