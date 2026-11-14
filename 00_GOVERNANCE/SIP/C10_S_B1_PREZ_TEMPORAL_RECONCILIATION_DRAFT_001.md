# C10-S — Reconciliación B1/Need_preZ con el DGP temporal y de roles

**ID:** C10-S-B1-PREZ-TEMPORAL-RECONCILIATION-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / PROPOSED / NOT_APPROVED / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Precedencia:** contrato funcional de adjudicación B1/Need_preZ (Draft 001; estado FUNCTIONAL_WORKING_CONTRACT_ACCEPTED); contrato DGP temporal y roles (Draft 001); contrato mínimo DGP B1/Need_preZ (Draft 001); contrato del paquete analítico B1/Need_preZ (Draft 001); DEC-C10-068/069 y decisiones B1/UE/instancia de servicio/oportunidad estandarizada aceptadas.

## 1. Objeto

Reconciliar la semántica, el tiempo y los permisos de `Need_preZ` entre el contrato funcional de B1, el DGP temporal/roles y el nuevo paquete analítico B1/Need. Este documento no modifica las decisiones aceptadas, no redefine el servicio, no introduce variables de resultado ni fija parámetros.

La reconciliación confirma que Need_preZ es una característica/objetivo basal de B1, no un estado técnico del servicio, no un evento de solicitud y no una consecuencia post-Z. Su truth debe generarse por una estipulación basal explícita y versionada del DGP para cada B1/UE; la evidencia observada se produce mediante un proceso de observación distinto.

## 2. Fuente semántica autoritativa

La definición funcional de trabajo aceptada es la del contrato B1/Need_preZ, §3:

> Antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

`Need_preZ` indica si ese objetivo existe para la B1 concreta antes de Z. No indica si el servicio está habilitado, instalado, disponible, accesible, si una petición se formula o admite, ni si el objetivo se alcanza.

La función del servicio descrita en DEC-C10-068 y su contrato de trabajo es una definición del servicio. No es por sí misma evidencia de que cada B1 tenga ese objetivo. La oportunidad estandarizada (`N_opportunities=1` por UE) es un probe post-snapshot común y no genera ni demuestra Need.

## 3. Regla de generación de truth: contrato sin parámetros

### 3.1 Unidad y ancla

- La truth pertenece a B1, vinculada unívocamente a UE conforme a la decisión aceptada de cardinalidad.
- La instancia lógica de servicio vinculada a esa B1/UE debe ser propia, única y versionada.
- La truth se fija en el baseline `t−1`, antes de Z en `t0`, con referencias a la versión del objetivo basal y a la instancia de servicio pertinente.
- No se añade un nuevo tiempo al reloj t−1/t0…t9.

### 3.2 Mecanismo generador requerido

El DGP deberá materializar, en su espacio reservado, una **especificación basal del objetivo de B1 por unidad**. Esta especificación constituye la fuente generadora de truth, no una fuente observacional para el Analyzer.

La regla de generación debe:
1. producir un estado explícito por B1/UE a partir de una regla basal versionada y reproducible;
2. permitir, en el soporte del diseño que finalmente se apruebe, unidades cuyo objetivo focal exista y unidades para las que esté afirmativamente excluido;
3. reservar `?` para indeterminación explícita de la estipulación generadora, no para falta de evidencia observacional;
4. evitar la asignación automática de Need=1 por pertenencia al microdominio, existencia de B1, disponibilidad de instancia de servicio, función genérica del servicio u oportunidad estandarizada;
5. evitar Need=0 por ausencia de solicitud, documento, registro o actividad;
6. no derivar truth de Z, D2, provisión, instalación, estados técnicos, C_dep, A_f, ΔT_acc, Reach, petición, admisión, procesamiento, respuesta, ejecución, Outcome o Value.

El contrato no selecciona aún qué atributos basales o regla de asignación determinan la especificación por unidad. Esa elección exige reconciliación explícita con el maestro DGP y con el universo cerrado de B1; no se inventan atributos, prevalencias, proporciones, distribuciones, semillas ni parámetros en este documento.

### 3.3 Criterio para truth=0

Truth=0 no significa que no se haya encontrado una declaración. La especificación basal generadora debe establecer afirmativamente que el objetivo definido en §2 no forma parte de los objetivos de esa B1 dentro del universo cerrado del DGP. El modo de representar esa exclusión y su soporte de diseño quedan abiertos.

Truth=? solo se usa cuando la propia especificación basal generadora no determina si el objetivo existe. No se utiliza para ocultar falta de cobertura del proceso de observación.

## 4. Modelo de observación separado

El modelo de observación toma la especificación basal oculta y genera un conjunto de fuentes/evidencias que simula lo que estaría disponible para un adjudicador. La dependencia generativa entre truth y evidencia es admisible y necesaria para que la evidencia pueda informar sobre Need; lo prohibido es copiar la etiqueta de truth, su campo, ID o referencia reservada al paquete visible.

El modelo de observación debe ser especificado separadamente y declarar, sin fijar aún valores:
- probabilidad/regla de emisión de una fuente afirmativa cuando el objetivo existe;
- emisión de una declaración negativa explícita cuando el objetivo está excluido;
- omisión/no disponibilidad de fuentes;
- falsos positivos y falsos negativos;
- ambigüedad semántica y conflictos entre fuentes;
- pérdida, corrupción, captura y error temporal;
- cobertura y universo documental/declarativo que se considera cerrado;
- autoridad, rol, versión y vinculación de cada fuente a B1/UE/servicio.

No se presupone independencia entre fuentes ni una única fuente por unidad. Las fuentes técnicas del servicio solo acreditan hechos técnicos; no acreditan el objetivo de B1 salvo que contengan una afirmación basal explícita y semánticamente pertinente, con autoridad, versión, identidad y temporalidad admisibles.

## 5. Reglas observadas 1/0/?

Se conservan sin modificación las reglas del contrato B1/Need_preZ, §4.2:

- **Observed=1:** evidencia afirmativa admisible, pre-Z, vinculada sin ambigüedad a B1/UE y a la versión pertinente, que respalda el objetivo basal.
- **Observed=0:** evidencia afirmativa admisible y suficiente de que el objetivo no forma parte de la especificación basal de esa unidad, dentro de un universo documental/declarativo cerrado y con cobertura demostrada.
- **Observed=?:** evidencia ausente, incompleta, contradictoria, no versionada, temporalmente ambigua, de alcance incierto o insuficiente.

Una búsqueda sin resultados no permite observed=0. El silencio, la ausencia de petición, la no admisión, la falta de procesamiento o la falta de respuesta tampoco permiten observed=0. La ausencia o insuficiencia de evidencia produce observed=?, no truth=?.

## 6. Inserción en el reloj temporal t−1/t0…t9

| Tiempo existente | Integración de Need_preZ | Restricción |
|---|---|---|
| t−1 / basal | Especificación basal oculta del objetivo B1; truth Need_preZ; vínculo B1–UE–instancia de servicio/versiones; evidencia pre-Z que el modelo de observación consiga producir | Fijar y sellar antes de Z; separar truth y evidencia |
| t0 / asignación | Z y su probabilidad | Z no modifica ni determina retrospectivamente Need |
| t1–t4 | Política, intento, instalación, accesibilidad, ΔT_acc y Reach | Ninguna variable de esta fase redefine Need |
| t5–t9 | Conocimiento, selección, inicio, ejecución, Outcome y Value | No utilizar eventos/resultados para reconstruir Need |

La fila t−1 del contrato temporal deberá tratar Need como atributo/objetivo basal de B1, no como componente de `S_T^*`, `T_acc`, `A_f^*`, `C_dep^*` o `E_T`. La evidencia sobre Need pertenece al expediente epistémico B1/Need; no debe confundirse con evidencia estructural de accesibilidad.

No se introduce un nuevo nodo temporal ni se cambia el orden de la cadena causal. La posición exacta de Request_event sigue la reconciliación ya abierta en el contrato B1; no se desplaza a t−1 por esta propuesta.

## 7. Roles y segregación de información

| Objeto | Generator | Proyector/Sealer | Adjudicador E1 | Adjudicador E2 | Analyzer PE | Evaluator B1/Need | Evaluator PE |
|---|---|---|---|---|---|---|---|
| Especificación basal del objetivo y `need_truth_state` | Crear y sellar en ámbito reservado | Sin acceso a la base reservada | Sin acceso | Sin acceso | Sin acceso | Acceso tras sellado E1/E2 | Sin acceso salvo que el contrato de evaluación PE lo requiera expresamente |
| Modelo de observación y parámetros/semillas reservados | Crear y sellar | Acceso solo a reglas de proyección autorizadas, no a secretos reconstructivos | Sin acceso a truth ni secretos | Sin acceso a truth ni secretos | Sin acceso a parámetros/semillas que revelen truth o escenario | Acceso tras sellado | Acceso tras sellado, conforme al contrato PE |
| Fuentes/evidencias observables pre-Z | Generar por mecanismo separado | Proyectar y sellar subconjunto autorizado | Acceso a expediente B1 permitido y cobertura | Acceso independiente al mismo expediente autorizado y cobertura | Solo proyección necesaria y autorizada por estimando | Acceso tras sellado, conforme a evaluación | Acceso conforme al contrato PE |
| Reglas públicas de adjudicación y cobertura | Versionar | Publicar versión autorizada | Acceso | Acceso | Solo contratos/documentación analítica permitidos | Acceso | Acceso conforme al contrato PE |
| Adjudicación E1 | No participa | No adjudica | Producir y sellar sin ver E2 | Sin acceso antes de sellar | Sin acceso por defecto | Acceso tras sellado | Sin acceso por defecto |
| Adjudicación E2 | No participa | No adjudica | Sin acceso antes de sellar | Producir y sellar sin ver E1 | Sin acceso por defecto | Acceso tras sellado | Sin acceso por defecto |
| Output Analyzer PE | No consulta ni modifica | No adjudica | Sin acceso por defecto | Sin acceso por defecto | Producir y sellar output estructurado por estimando | Sin acceso, salvo referencia necesaria para evaluar tarea B1 | Evaluar tras sellado contra oráculos DGP |
| Comparación truth/observed Need | No reescribe | No evalúa | Sin acceso durante adjudicación | Sin acceso durante adjudicación | Sin acceso | Comparar E1 y E2 por separado con truth tras sellado | No aplica |
| Comparación output PE/truth DGP | No reescribe | No evalúa | No aplica | No aplica | Sin acceso a truth | No aplica | Comparar output PE sellado con oráculos por estimando |

E1 y E2 no reciben truth, la estipulación reservada ni la salida del otro antes de sellar. El Analyzer PE no recibe truth, potenciales, parámetros/semillas reservados ni outputs E1/E2 por defecto; solo consume observaciones expresamente permitidas por el contrato del estimando. El Evaluator B1/Need compara E1 y E2 por separado con truth. El Evaluator PE evalúa la salida PE sellada contra los oráculos DGP por constructo/estimando. La apertura de truth para cada evaluación no puede preceder al sellado inmutable de la salida que se evalúa.

La separación describe responsabilidades lógicas; no afirma que existan servicios físicos independientes ni que el firewall esté técnicamente implementado o verificado.

## 8. Relación con población y análisis causal

Need_preZ no sustituye `E_i`, `P^*_{τ2}`, `App^*(τ2,S0)`, `C_dep,0` o `A_f,0^*`. No es filtro de inclusión ITT ni criterio postratamiento. La población ITT primaria candidata permanece definida por sus reglas propias y no se condiciona a Need=1 ni a solicitud/admisión/procesamiento post-Z.

Si Need se utiliza para estratificación, heterogeneidad, descripción, análisis de consecuencias o definición de una población de Value, ese uso deberá estar declarado ex ante y reconciliado con los contratos de estimandos y población. Este documento no autoriza ajuste, exclusión ni modificación de estimandos.

## 9. Invariantes de reconciliación propuestos

1. Need_truth está vinculado a B1/UE y baseline t−1, antes de Z.
2. La especificación basal es la fuente generadora de truth; no se confunde con evidencia observada.
3. La generación de truth no usa variables post-Z ni estados técnicos derivados de la intervención.
4. No se asigna Need=1 a todas las unidades por defecto.
5. Need=0 requiere exclusión afirmativa dentro del universo cerrado del DGP.
6. Need=? generador no se confunde con observed=? por falta de evidencia.
7. El modelo de observación es separado, versionado y no expone la etiqueta de truth.
8. Observed=0 exige evidencia negativa afirmativa y cobertura suficiente.
9. El silencio y la ausencia de petición no se convierten en Need=0.
10. La oportunidad estandarizada no genera ni demuestra Need.
11. E1/E2 son independientes y sus resultados se sellan antes de evaluar truth.
12. Need no redefine accesibilidad, Reach, elegibilidad ni la población ITT.
13. La evaluación conserva por separado errores de clasificación, indeterminación y cobertura.
14. Ningún registro, parámetro, unidad o fuente se materializa hasta cerrar los gates y obtener autorización.

Estas son pruebas contractuales propuestas; no se han ejecutado.

## 10. Pendientes que no deben cerrarse por inferencia

| Pendiente | Estado |
|---|---|
| Regla concreta que genera la especificación basal por unidad | OPEN |
| Atributos causales basales que pueden alimentar esa regla | Ninguno autorizado por los contratos revisados; X/H/C/L y variables técnicas no son proxies ni generadores automáticos |
| Soporte de truth=1/0 y eventual truth=? | OPEN; sin prevalencias ni proporciones |
| Universo cerrado que permite representar exclusión afirmativa | OPEN |
| Catálogo de fuentes semánticamente admisibles | OPEN |
| Mecanismos/parámetros del modelo de observación | OPEN |
| Cobertura/denominadores por unidad y dimensión | OPEN |
| Ubicación técnica y permisos efectivos del paquete | OPEN |
| Reconciliación formal en el maestro temporal/roles | Propuesta pendiente; este documento no lo modifica |

## 11. Dictamen

**TEMPORAL/ROLE RECONCILIATION PROPOSED; ROLE SPLIT RECONCILED; BASELINE STIPULATION MECHANISM AND OBSERVATION MODEL STILL OPEN.**

La reconciliación inserta Need_preZ en el baseline t−1 como objetivo basal de B1, mantiene separadas truth y evidencia, y asigna permisos coherentes con generador, Analyzer y evaluador. No resuelve qué regla concreta produce heterogeneidad entre unidades ni cómo se generan las fuentes; hacerlo requiere volver a la especificación maestra del DGP y a las decisiones basales pertinentes.

No se crean roster, IDs, truth, fuentes, cobertura, adjudicaciones, código ni fixtures. No se ejecutan validadores, DGP, replay, simulación ni análisis. No se modifica main, RMA, Evidence→Claim Matrix, STATUS, decisiones aceptadas ni estimandos.

`scientific_execution=false`; `execution_authorized=false`.


## 8. Reconciliación funcional B1/V_cont y límite de derivación temporal (2026-11-12)

La función de servicio no permanece abierta. Prevalecen el contrato funcional de adjudicación B1 §2, la reconciliación de valoración §13 y DEC-C10-068: admitir solicitudes cuando ENABLED=true, no admitirlas cuando ENABLED=false y exponer PROFILE declarado. STANDARD/READ_ONLY no reciben semántica de negocio adicional.

Para V_cont, la verdad latente por intervalo representa conformidad con esa regla de capacidad/admisión y exposición de perfil. No es el número de solicitudes, el éxito de procesamiento ni una respuesta. La ausencia de solicitud en un intervalo no es fallo. La falta de señal observacional tampoco cambia truth; se trata en S3 y en sus cotas de identificación.

El reloj t−1/t0…t9 es un orden de etapas causales y no define intervalos iguales. H=3 es profundidad de trayectoria; S7 (una oportunidad declarativa pre-Z por UE) es parte del paquete Need_preZ; ninguna de estas cantidades determina K ni la ventana de V_cont. La agregación igualitaria DEC-C10-100 sigue aceptada.

Como recomendación aún no aprobada, se propone iniciar la ventana en t0 para incluir posibles interrupciones durante provisión/instalación y cerrarla en un horizonte post-Z fijo y común. Duración, unidad temporal, resolución, K y tratamiento de transitorios permanecen OPEN; no se derivan de t9 ni se inventan. El inicio t0 es recomendación, no decisión normativa.

**Estado:** FUNCTIONAL_REFERENCE_REUSED / INTERVAL_TRUTH_DEFINED_AT_CONSTRUCT_LEVEL / WINDOW_AND_GRID_OPEN / NO_MATERIALIZATION / NO_EXECUTION_AUTHORIZED.

## 9. Aceptación de t0 y contrato temporal S3 de V_cont (2026-11-12)

El usuario acepta iniciar la ventana post-Z de V_cont en t0, inmediatamente después de la asignación, incluyendo provisión e instalación. La ventana no queda condicionada a intento, recepción, instalación, C_dep, A_f, Reach, selección o ejecución. Se aplica simétricamente a los brazos comparados.

Se representa W_V=[t0,T*]. T* es un horizonte final común y preespecificado, todavía OPEN. No se identifica automáticamente con t9: t0…t9 ordena etapas causales y no define duración física. H=3 es profundidad transformacional; S6/S7 son oportunidades de petición/declaración con cardinalidad propia; ninguno determina K.

La rejilla contiene K intervalos de igual duración y conserva la agregación DEC-C10-100. Permanecen OPEN duración, unidad temporal, K, tolerancia de timestamps y tratamiento de eventos que cruzan fronteras. No se fija una duración mínima de interrupción ni se concede tolerancia de gracia por defecto.

Para la observación se reutiliza S3 pasivo y no mutante: proceso/módulo, listener/socket/superficie de recepción, dependencias, capacidad/recursos si están definidos, y perfil runtime. Es un vector de señales imperfectas, no un verificador. S4 fija identidad/versión/integridad y S5 aporta el contrato ENABLED/PROFILE, sin sustituir S3. No se envían solicitudes adicionales ni se activan rutas para observar.

El proceso de observación se separa de truth: P(O_S3|A_B1,M), con M explícito para emisión, captura/pérdida, cobertura, validez, error, censura, alineación temporal y dependencia entre señales. No se presume independencia, tasas constantes ni MCAR/MAR/MNAR. El Analyzer recibe solo señales observadas, tiempos, cobertura/provenance y calibración permitida; nunca truth, potenciales o secretos. Sin identificación, bounds o abstención.

Cobertura por UE×intervalo×componente. Silencio, no captura, lag, muestreo o ruta no activada no equivalen a señal 0. Las observaciones repetidas se anidan en UE y no aumentan N experimental.

**Estado:** WINDOW_START_T0_ACCEPTED / TSTAR_AND_K_OPEN / S3_VECTOR_MODEL_RECONCILED / SIGNAL_VALIDITY_AND_CALIBRATION_OPEN / NO_EXECUTION_AUTHORIZED.


## 10. Criterio candidato para truth de continuidad dentro de cada intervalo (2026-11-12)

La interpretación recomendada del contrato “mantener disponible” es estricta dentro de cada intervalo: A_B1=1 si ENABLED/PROFILE se cumple durante todo el intervalo; A_B1=0 si existe un incumplimiento funcional positivo confirmado en cualquier momento del intervalo; A_B1=? solo si el Generator no puede determinar la truth funcional. La falta de S3 es incertidumbre observacional, no UNKNOWN de truth.

Esta lectura no introduce periodo de gracia ni duración mínima de interrupción. Si se desea tolerar transitorios de duración hasta δ, será necesaria una decisión normativa explícita y una justificación de δ. No se diluyen fallos confirmados mediante promedios de señales. S3 debe tener resolución/cobertura suficiente para detectar los eventos estipulados; si no, Analyzer produce bounds/abstención.

**Estado:** STRICT_WITHIN_INTERVAL_RECOMMENDED / TRANSIENT_TOLERANCE_NOT_APPROVED / K_DEPENDS_ON_EVENT_SCALE_AND_S3_RESOLUTION.


## 11. DEC-C10-102: continuidad estricta por intervalo y consecuencia temporal (2026-11-12)

El usuario acepta la continuidad estricta dentro de cada intervalo, sin periodo de gracia para interrupciones funcionales confirmadas.

A_B1(i,k)=1 si ENABLED/PROFILE se cumple durante todo el intervalo; A_B1(i,k)=0 si ocurre al menos un incumplimiento funcional confirmado en cualquier instante; A_B1(i,k)=? solo si la truth funcional no queda determinada por el Generator. La falta de S3 es incertidumbre observacional, no UNKNOWN de truth.

No se introduce duración mínima de fallo, periodo de gracia ni cuota tolerada. Los eventos exactamente en una frontera se asignarán de forma determinista y versionada a un único intervalo. La resolución de truth del Generator debe poder representar los eventos que el DGP declare relevantes. Si S3 no puede detectarlos, Analyzer informa bounds/abstención; no afirma detección exhaustiva.

La ventana comienza en t0 (DEC-C10-101) y termina en T* común, cubriendo provisión/instalación y seguimiento hasta el último evento causal capaz de modificar el cumplimiento dentro del estimando. t0…t9 es orden causal, no duración física. Se recomienda reloj explícito de tiempo transcurrido con unidad normalizada declarada, eventos fechados y rejilla regular. No se asigna duración igual por etapa ni se usa el número de etapas como K.

K=(T*−t0)/Δ con Δ constante; si no hay divisibilidad exacta, se ajusta T* antes de generar, sin intervalo residual desigual. Unidad, eventos relevantes, duración mínima representable, T*, Δ, K, regla de cierre y calibración S3 siguen OPEN.

**Estado:** STRICT_INTERVAL_CONTINUITY_ACCEPTED / NO_GRACE_PERIOD / EVENT_CLOCK_AND_GRID_SPECIFIED_AS_DESIGN_ROUTE / TSTAR_DELTA_K_OPEN / NOT_DESIGN_FROZEN / NO_EXECUTION_AUTHORIZED.

## 12. Inventario funcional de eventos y separación de relojes (2026-11-12)

La función de servicio se reutiliza sin ampliación: ENABLED=true implica admitir solicitudes; ENABLED=false implica no admitirlas; PROFILE debe exponerse conforme a su valor declarado. STANDARD/READ_ONLY no adquieren semántica adicional.

### 12.1 Eventos/estados del DGP

| Grupo | Elementos | Relación con V_cont |
|---|---|---|
| Provisión | programación, intento, recepción/disponibilidad de componentes | Antecedentes causales, no truth funcional por sí mismos |
| Instalación | aplicación, verificación, integridad, compatibilidad, operabilidad, rollback | Pueden cambiar el estado efectivo del servicio |
| Configuración | ENABLED efectivo, PROFILE efectivo, versión/identidad de instancia/configuración | Determinantes directos o de binding de la regla |
| Runtime | proceso/módulo, listener/socket/superficie de recepción, dependencias, capacidad/recursos cuando afecten admisión, caída/reinicio/recuperación | Pueden impedir/restaurar la capacidad funcional; S3 solo los observa imperfectamente |
| Petición | oportunidad, intento, recepción, admisión/rechazo, procesamiento/respuesta | Evento discreto; no monitor continuo. Ausencia de petición no es fallo |
| Transformación/valor | Reach, selección, ejecución, F*, O-CONF, Outcome, Value | No definen A_B1 ni sustituyen S3 |

La truth se genera a partir del estado funcional efectivo y de sus transiciones. Un evento de provisión/instalación o runtime solo determina A_B1 cuando el estado funcional resultante incumple o restituye la regla B1. La solicitud estandarizada única por UE no se reutiliza como sonda repetida.

### 12.2 Tres relojes distintos

1. **Truth/event_time:** momento en que cambia el estado funcional efectivo en el Generator.
2. **Rejilla V_cont:** partición común de [t0,T*] en K intervalos iguales para aplicar la regla estricta.
3. **Observación S3:** timestamps de captura, lag, cobertura y pérdida del canal pasivo.

Δ no equivale a la frecuencia S3. S3 reutiliza los componentes ya definidos (proceso/módulo, listener/socket/superficie, dependencias, capacidad/recursos cuando estén definidos y perfil runtime). No se añaden probes activos. Snapshots periódicos aislados no garantizan detección de episodios breves; sin identificación del canal se conservan bounds o abstención.

### 12.3 Interpretación correcta de la agregación aceptada

La combinación DEC-C10-100/102 hace que V_cont_truth sea la proporción de intervalos completamente conformes, no la fracción exacta de tiempo de uptime. Cualquier incumplimiento confirmado, por breve que sea, convierte el intervalo afectado en 0. El valor depende de Δ y de la alineación de la rejilla. Se preservan fórmula y decisiones aceptadas; no se altera el endpoint por inferencia. Medir la fracción exacta de tiempo requeriría una operacionalización distinta y aprobación expresa.

### 12.4 Fronteras y T*

Convención recomendada: intervalos internos [b_k,b_{k+1}); un evento exactamente en frontera interna pertenece al intervalo que comienza allí; el último intervalo incluye T*. Un episodio que cruza una frontera afecta a cada intervalo cuyo interior intersecta el episodio. La regla se versionará antes de materializar.

T* debe incluir provisión/instalación y un seguimiento común posterior al último evento causal capaz de modificar A_B1. Puede expresarse T*=t_last+τ_follow. No se fija τ_follow, T*, Δ ni K hasta cerrar catálogo de eventos, mínimo episodio representado y capacidad de captura S3.

**Dictamen:** EVENT_INVENTORY_RECONCILED / TRUTH_GRID_AND_S3_CLOCK_SEPARATED / V_CONT_IS_FULLY_COMPLIANT_BLOCK_SHARE / TSTAR_DELTA_K_OPEN / NOT_DESIGN_FROZEN.

## 13. Catálogo funcional B1 y dominio de detección S3 (2026-11-12)

El contrato de trabajo B1 §2 determina la función que se evalúa: admitir cuando ENABLED=true, no admitir cuando ENABLED=false y exponer PROFILE declarado. STANDARD/READ_ONLY no reciben semántica diferenciada. RUL-SVC-ENABLE-PROFILE-01 conserva su alcance declarativo como implicación; no se transforma en equivalencia.

Las transiciones causales se agrupan en cinco familias finitas: (1) cambios efectivos ENABLED/PROFILE; (2) pérdida/recuperación de proceso o módulo; (3) pérdida/recuperación de listener/socket/superficie de ingreso; (4) pérdida/recuperación de dependencias solo si impiden/restauran admisión; (5) insuficiencia/restauración de capacidad/recursos solo si impiden/restauran admisión. Provisión, instalación, verificación, rollback y reinicio son antecedentes/transiciones, no fallos automáticos. El resultado funcional efectivo, no la etiqueta técnica, determina A_B1.

La regla DEC-C10-102 no admite duración mínima de fallo ni gracia: cualquier incumplimiento confirmado afecta a todos los intervalos que intersecte. Se separa de ello δ_det, duración mínima de episodio para la que S3 demuestre detectabilidad bajo su modelo de captura/cobertura calibrado. δ_det no modifica truth ni excusa episodios menores; delimita cuándo Analyzer puede recuperar puntualmente la verdad. Por debajo de ese dominio, bounds o abstención, salvo evidencia pasiva adicional identificable.

Δ (rejilla de agregación), cadencia/resolución/cobertura S3 y δ_det son magnitudes distintas. No se presume telemetría event-driven ni polling regular. t_last es la última transición causal que pueda cambiar A_B1, incluida la recuperación final; T*=t_last+τ_follow con cola común. Si el episodio sigue activo al cierre, no se imputa recuperación.

**Dictamen:** FINITE_CAUSAL_FAMILIES_BOUNDED / TRUTH_STRICT / DETECTION_DOMAIN_SEPARATE / S3_UNCALIBRATED / TSTAR_DELTA_K_OPEN.

## 14. Cierre del universo finito de estados y eventos funcionales B1 por mundo (2026-11-12)

**Alcance:** cierre documental del universo funcional que puede alterar A_B1/V_cont; reutiliza DEC-C10-068/100/101/102 y las familias de §13. No materializa estados por UE, episodios, distribuciones, parámetros, fixtures ni observaciones. No añade escenarios ni IDs de prueba.

### 14.1 Estado funcional finito

La unidad de adjudicación es UE×instancia B1×versión×intervalo. La truth se deriva del estado funcional efectivo, nunca del nombre de un evento técnico. El estado suficiente queda representado por el vector:

- `ENABLED_eff ∈ {true,false,?}`;
- `PROFILE_eff` y `PROFILE_declared`, comparados por identidad/versión exacta: `MATCH`, `MISMATCH` o `UNKNOWN` (se conserva el valor enumerado original; no se colapsan perfiles);
- estado de proceso/módulo, superficie de ingreso, dependencias requeridas y capacidad: `FUNCTIONAL`, `NONFUNCTIONAL` o `UNKNOWN`, solo para componentes aplicables y cuya relación con la función B1 esté declarada en la versión del servicio.

Un componente no requerido no se convierte en fallo ni se introduce como requisito por defecto. Si su aplicabilidad no está determinada, no se trata como no requerido: se propaga `UNKNOWN`.

**Regla funcional:**

1. `A_B1=1` cuando se cumple la regla B1 completa: si `ENABLED_eff=true`, la función admite solicitudes; si `ENABLED_eff=false`, no las admite; y en ambos casos expone el `PROFILE` declarado, con la cadena runtime y los componentes requeridos funcionales.
2. `A_B1=0` cuando existe al menos una violación funcional positiva confirmada: admisión/rechazo contrario a ENABLED, PROFILE no expuesto o distinto del declarado, o pérdida de un componente requerido que impide la función.
3. `A_B1=?` cuando no hay violación positiva confirmada pero uno o más elementos necesarios no pueden adjudicarse. `ENABLED=false` por sí solo no es fallo: el rechazo de solicitudes es el comportamiento requerido.
4. La ausencia de solicitudes no permite inferir ni admisión ni fallo. No se añaden sondas activas; la truth la produce el Generator a partir de estados y transiciones estipulados.

### 14.2 Universo finito de transiciones causales

| Familia | Evento de transición | Condición para afectar A_B1 | Lo que no basta |
|---|---|---|---|
| CFG | Cambio efectivo de ENABLED; cambio efectivo de PROFILE; divergencia entre declarado y efectivo | El cambio altera la regla esperada, su exposición o el comportamiento de admisión | Programación o escritura de configuración sin cambio efectivo |
| PROC | Proceso/módulo deja de funcionar; vuelve a funcionar; reinicio con estado resultante | La pérdida/recuperación impide/restaura la función B1 | Reinicio o instalación por sí solos |
| INGRESS | Listener/socket/superficie de recepción cae o se restaura | La transición impide/restaura recibir y admitir/rechazar conforme a ENABLED | Cambio de endpoint sin efecto funcional demostrado |
| DEP | Dependencia requerida deja de funcionar o se recupera | Solo si la dependencia pertenece al conjunto requerido versionado y su estado impide/restaura la función | Cambio de dependencia no requerida o mera modificación de manifiesto |
| CAP | Capacidad/recurso cruza el umbral funcional de suficiencia y se recupera | Solo si la insuficiencia impide/restaura la admisión conforme a la regla B1 | Variación de uso/carga sin efecto funcional |

Estas cinco familias son exhaustivas para el nivel de abstracción funcional del servicio definido en el contrato B1. Nuevas clases de transición requieren revisión explícita del contrato funcional; no se incorporan silenciosamente al DGP.

### 14.3 Eventos antecedentes, observacionales y no constitutivos

| Clase | Eventos | Tratamiento |
|---|---|---|
| Antecedentes de política/provisión | asignación Z, programación, intento, recepción, disponibilidad de artefactos/componentes | Causas potenciales; no alteran truth hasta que produzcan una transición funcional efectiva |
| Aplicación/recuperación | instalación, verificación, rollback, reinicio | Se registran con tiempo y versión; solo afectan A_B1 por el estado funcional resultante |
| Interacción de servicio | oportunidad, solicitud, intento, recepción, admisión/rechazo, procesamiento/respuesta | Evidencia discreta de comportamiento; ausencia de solicitud no es fallo y una solicitud aislada no sustituye la continuidad temporal |
| Transformacional/resultado | C_dep, A_f, D_f, ΔT_acc, Reach, trayectoria, selección, ejecución, F*, O-CONF, Outcome | Constructos/resultados separados; no definen A_B1 ni V_cont |
| Observación | emisión/captura S3, snapshot, log, lag, pérdida, censura, cobertura | Cambian evidencia observada, nunca la truth funcional |

### 14.4 Dependencias temporales y orden de eventos

- Cada transición de truth tiene `event_time`, identidad de unidad/instancia, versión antes/después, familia causal, estado anterior y posterior, y vínculo causal explícito al régimen/política cuando corresponda.
- Se permiten recurrencia y recuperación: `FUNCTIONAL→NONFUNCTIONAL→FUNCTIONAL`; también cambio de configuración sin caída runtime y cambio runtime sin modificación de configuración. No se presume que las familias sean independientes.
- Un episodio que cruza una frontera afecta a cada intervalo cuyo interior intersecta el episodio. La continuidad es estricta: cualquier incumplimiento confirmado hace `A_B1=0` en el intervalo afectado, sin gracia ni duración mínima.
- La observación S3 tiene reloj separado (captura/lag/cobertura); no se usa para crear, fechar retrospectivamente ni eliminar transiciones de truth.
- El cierre temporal es común y ex ante: `T* = t_c,max + τ_follow`, donde `t_c,max` es el límite superior del soporte de transiciones posibles declarado para el conjunto de mundos/ambos brazos. Si ese soporte no puede acotarse, T* no queda cerrado y el episodio activo al final se trata como terminal/censurado, nunca como recuperado.
- La rejilla V_cont conserva K intervalos iguales y `K=(T*−t0)/Δ`; T* se ajusta antes de generación para evitar un intervalo residual desigual. Δ no es la cadencia S3 ni la duración mínima funcional.

### 14.5 Crosswalk por mundos ya existentes R0–R3

| Mundo | Mecanismo relevante para B1 | Regla de no atribución / contraste |
|---|---|---|
| R0 — focal limpio | Las transiciones B1 solo pueden ocurrir por el mecanismo focal declarado y sus consecuencias funcionales efectivas. El mundo puede estipular estabilidad o interrupción; no se fuerza una respuesta por construcción. | El efecto de Z sobre V_cont es ITT de paquete. La atribución a ΔT_acc exige que el mecanismo funcional esté mediado por la intervención focal identificable, no por la mera secuencia de provisión. |
| R1 — alternativa basal estable | La ruta alternativa permanece estable en el bloque transformacional. Su existencia no cambia por sí misma ENABLED/PROFILE ni el runtime B1. | No imputar a B1 ni a ΔT_acc focal efectos de la alternativa. La alternativa puede mantener Reach aunque la ruta focal no cambie; Reach y V_cont siguen separados. |
| R2 — alternativa afectada/colateral | Z puede alterar A1/A2 o recursos/dependencias compartidos. Solo genera transición B1 si el componente compartido pertenece efectivamente a la cadena funcional B1 y cambia su estado. | Si el cambio afecta solo la alternativa, se registra como vía colateral transformacional, no como fallo/beneficio B1. Si afecta B1 por componente compartido, es vía no focal explícita y bloquea atribución focal no separada. |
| R3 — fallo por etapas | Intento, recepción, instalación o rollback pueden fallar. B1 solo cambia si el resultado produce una transición CFG/PROC/INGRESS/DEP/CAP efectiva. | Fallo de intento/recepción/instalación no equivale automáticamente a A_B1=0; un servicio previo puede seguir funcional. C_dep, A_f y V_cont permanecen separados. |

Las clases directas, heterogéneas, de interferencia, observación adversarial y soporte del roster existente se aplican como modificadores de esos mundos, no como mundos nuevos: una vía directa solo altera V_cont si tiene una función generadora explícita sobre estados B1; la interferencia requiere exposición/recursos compartidos definidos; la observación adversarial altera E_S3 pero no truth.

### 14.6 Clasificación de parámetros y decisiones temporales

| Elemento | Clase | Estado de cierre |
|---|---|---|
| Inicio t0 e inclusión de provisión/instalación | Regla normativa aceptada | CERRADO (DEC-C10-101) |
| Igual duración de intervalos y media no ponderada de A_B1∈{1,0,?} | Regla de agregación aceptada | CERRADO (DEC-C10-100) |
| Continuidad estricta; sin gracia ni mínimo funcional; frontera determinista | Regla normativa aceptada; asignación a intervalo inicial en frontera interna según contrato temporal | CERRADO en semántica; convención exacta [b_k,b_{k+1}) debe versionarse antes de materializar |
| ENABLED/PROFILE y cinco familias causales | Dominio funcional finito derivado del contrato | CERRADO documentalmente para este nivel de abstracción |
| Recurrente, persistencia, recuperación, duración/fase de episodios | Dominio de sensibilidad con soporte por mundo pendiente | OPEN; no fijar distribuciones ni cifras |
| t_c,max, τ_follow y T* común | Decisión de soporte/horizonte | OPEN; debe justificarse ex ante y ser común |
| Unidad de tiempo normalizada, Δ y K | Decisión de diseño/precisión temporal | OPEN; K entero, sin residuo desigual; no derivar de t0…t9 ni H |
| Cadencia, cobertura, lag, pérdida, error y dependencia S3; snapshots/logs/híbrido | Modelo de observación y calibración | OPEN; δ_det es detectabilidad, no mínimo funcional |
| Umbral p* para resumir detectabilidad y criterio de error/precisión | Decisión normativa/metrológica | OPEN; no inventar |

### 14.7 Dictamen del subgate

**CLOSED_DOCUMENTARILY:** universo finito de estados funcionales, cinco familias de transición causal, eventos antecedentes/no constitutivos, reglas de propagación de truth y correspondencia R0–R3. El cierre es semántico y de alcance; no afirma que los estados o transiciones hayan sido materializados ni observados.

**OPEN:** soporte de episodios/persistencia/recuperación; horizonte común T*; τ_follow; unidad temporal; Δ/K y versionado exacto de fronteras; modelo/calibración S3 y δ_det/p*; factibilidad/soporte de g_A y r_common; q_X*; F*/oráculo O-CONF. Estos pendientes no reabren el universo funcional cerrado; son gates posteriores de temporalización, medición e identificación.

**No autorizado:** instanciar episodios, seleccionar distribuciones, generar datos, ejecutar calibración/simulación/estimación, implementar código o declarar Design Freeze. `scientific_execution=false`; `execution_authorized=false`.
## 15. Contrato de soporte temporal finito y horizonte común T* (2026-11-12)

**Objeto:** resolver la estructura del soporte temporal exigible al DGP sin asignar duraciones, tasas, distribuciones ni números. Se aplica al universo cerrado de §14 y a los mundos R0–R3 existentes; no añade clases de mundo.

### 15.1 Contrato de soporte por configuración de mundo

Cada configuración ejecutable deberá declarar, antes de generar truth, un soporte temporal acotado y versionado para todos los procesos que puedan producir transiciones CFG/PROC/INGRESS/DEP/CAP:

- límite superior de inicio/delayed onset de episodios;
- límite superior de número de episodios/transiciones recurrentes por UE e instancia B1;
- límite superior de duración de cada estado no funcional y de cada episodio;
- límite superior de latencia hasta recuperación funcional, si la recuperación está permitida;
- límite superior de cualquier transición tardía inducida por Z, provisión, instalación, rollback, dependencia, capacidad, interacción o vía directa/colateral que pueda afectar B1;
- límite superior de lag/captura del canal S3, separado del soporte de truth;
- régimen de dependencia entre episodios y componentes; no se presume independencia ni renovación.

Los límites son de soporte, no medias, percentiles ni valores típicos. No se aceptan límites derivados de t0…t9, H, K, cadencia S3 o de la duración de etapas causales. La configuración falla cerrada si algún proceso causal carece de cota o si la cota no es común/comparable entre brazos.

### 15.2 Definición de t_c,max y T*

Para cada mundo/configuración m y brazo/regímen z, `t_c,max(m,z)` es la cota superior del tiempo transcurrido desde t0 en que puede ocurrir la última transición causal permitida capaz de cambiar A_B1, incluyendo la transición de recuperación final. Se calcula como el máximo de las cotas declaradas para todas las familias y vías aplicables, no como el último evento observado en una realización.

`t_c,max = max_{m,z} t_c,max(m,z)` sobre el roster confirmatorio y los brazos que pertenecen al mismo estimando. El horizonte común queda definido estructuralmente como `T* = t_c,max + τ_follow`.

`τ_follow` no es un periodo de gracia ni tolerancia funcional. Es una cola posterior al último cambio causal permitido, necesaria para cubrir el estado terminal y el retraso máximo del canal de observación. Debe ser al menos tan largo como la cota conjunta necesaria para que el S3 declarado pueda capturar/fechar el estado terminal después de `t_c,max`; la regla concreta depende del modelo de captura/lag y permanece pendiente de calibración. La ausencia de señal no demuestra recuperación.

Todos los brazos, escenarios confirmatorios y unidades comparadas usan la misma ventana `[t0,T*]`, la misma rejilla y el mismo criterio de cierre. Si un escenario de sensibilidad requiere soporte más largo, se amplía T* para todo el contraste o se informa como estimando/horizonte distinto preespecificado; nunca se recorta selectivamente por brazo.

### 15.3 Episodios, recurrencia y terminalidad

- La generación primaria debe tener número finito y acotado de transiciones por unidad dentro de `[t0,t_c,max]`; la cota se declara por configuración y cubre recurrencias, no solo el primer fallo.
- Se permite más de un episodio y recuperación parcial/total. Cada transición se ordena por `event_time`; empates y eventos en frontera se resuelven por regla determinista versionada, sin depender del orden de iteración del código.
- Después de `t_c,max` no puede existir una nueva transición causal de truth en esa configuración. La trayectoria funcional permanece en el estado alcanzado al final de la última transición; la cola `τ_follow` observa ese estado, no introduce nuevas oportunidades de intervención.
- Si el mecanismo teórico que se quiere representar no admite una cota superior defendible (p. ej. recurrencia sin límite o hazard con soporte no acotado), no se fuerza un T* artificial: ese mundo no pertenece al contraste finito puntual. Se conserva como análisis de horizonte/censura o como límite de identificación, y el Analyzer debe abstenerse o informar bounds cuando el horizonte no captura el resultado definido.
- Un episodio que sigue activo al final de T* no se clasifica como recuperado. La truth terminal se conserva, y la observación incompleta produce censura/bounds, no imputación.

### 15.4 Regla de construcción de Δ y K una vez cerrado el soporte

El orden de decisión queda fijado: (1) soporte de transiciones por configuración; (2) máximo común `t_c,max`; (3) modelo/cota de captura S3 y `τ_follow`; (4) `T*`; (5) resolución temporal mínima necesaria para representar los eventos admitidos y el dominio de detección S3; (6) elección de `Δ` compatible; (7) `K=(T*−t0)/Δ` entero. No se elige Δ para hacer cómodo K ni se elige K para ocultar eventos que la regla estricta exige representar.

Un Δ más grueso no altera truth funcional ni convierte episodios cortos en conformes: cambia qué intervalos de la agregación estricta quedan afectados y, por tanto, el estimando operativo V_cont. Por eso Δ/K deben quedar congelados antes de generar potenciales. La resolución interna del Generator debe representar los tiempos de evento con precisión suficiente respecto de Δ y del soporte declarado; no se presume que coincida con S3.

### 15.5 Criterios de admisión y salida fail-closed

| Comprobación previa | Aceptación | Fallo/abstención requerida |
|---|---|---|
| Soporte de cada familia causal aplicable | Cota superior explícita, versionada y trazable a la regla generadora | Configuración inválida; no generar |
| Recurrencia y número de transiciones | Cota finita que incluye todos los episodios permitidos | Excluir del contraste puntual finito o clasificar como sensibilidad/censura; nunca truncar silenciosamente |
| Comparabilidad entre brazos/mundos | T* común cubre la unión de soportes del estimando | No comparar V_cont como si compartiera horizonte |
| Recuperación y terminalidad | Última transición posible, incluida recuperación, dentro de t_c,max | Estado terminal desconocido/censurado; bounds o abstención |
| S3 | Cota de lag/captura y cobertura definida para el estado terminal | No inferir recuperación por silencio; bounds/NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT |
| Δ/K | Rejilla común, intervalos iguales y resolución suficiente para el soporte declarado | No materializar la configuración ni generar datos |

### 15.6 Estado del gate temporal

**CERRADO COMO REGLA ESTRUCTURAL:** soporte por configuración explícito y acotado; recurrencia incluida en la cota; máximo común sobre brazos/mundos; `T*=t_c,max+τ_follow`; separación entre transición causal final, cola de observación, rejilla V_cont y reloj S3; tratamiento fail-closed de soporte no acotado.

**NO CERRADO NUMÉRICAMENTE:** valores de las cotas por familia/mundo, máximo de recurrencias, duración/recuperación, cota S3, `τ_follow`, unidad, Δ y K. No existe base documental autorizada para asignarlos sin una elección de sensibilidad/precisión y calibración. El siguiente paso no es escoger cifras arbitrarias: es resolver conjuntamente el dominio temporal de episodios que el DGP pretende representar y la capacidad de detección S3, y después seleccionar Δ/K.

**Dictamen:** `FINITE_TEMPORAL_SUPPORT_RULE_CLOSED / COMMON_HORIZON_CONSTRUCTION_DEFINED / NUMERIC_SUPPORT_AND_S3_CALIBRATION_OPEN / DELTA_K_OPEN / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN`.