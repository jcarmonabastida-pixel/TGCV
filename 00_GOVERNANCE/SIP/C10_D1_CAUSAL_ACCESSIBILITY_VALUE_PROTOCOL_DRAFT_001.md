# C10-D1 — Protocolo de identificación causal de la contribución de la accesibilidad a Value

**Estado:** PROPUESTA METODOLÓGICA DE TRABAJO — NO APROBADA / NO EJECUTADA  
**Ámbito:** C10 — vínculo causal entre cambios en transformaciones accesibles y construcción de valor  
**Naturaleza del registro:** consolidación metodológica de trabajo derivada de C10-D1.1.a–s  
**Efecto sobre el estado científico:** ninguno. No modifica TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims, cierres experimentales ni criterios de falsación vigentes.  
**Restricción operativa:** este documento no autoriza selección definitiva de caso, descarga/procesamiento de datos, ejecución experimental ni cambios adicionales de gobernanza.

---

## 1. Propósito y pregunta

C10 investiga si, en sistemas generativos y bajo condiciones delimitables, los cambios en el espacio de transformaciones accesibles contribuyen causalmente a cambios de valor.

La pregunta de atribución es más exigente que estimar el efecto total de una intervención:

> ¿Qué contribución causal al cambio de Value puede atribuirse específicamente a una modificación del espacio de transformaciones accesibles, distinguiéndola de cambios en condiciones habilitadoras, mecanismos alternativos y otras vías de la intervención?

El protocolo debe permitir tres desenlaces científicos legítimos:

1. contribución causal identificada en un ámbito delimitado;
2. evidencia adversa que limite o refute la hipótesis en el ámbito preespecificado;
3. identificación insuficiente, sin presentar esta última como confirmación ni refutación.

## 2. Formulación condicional de trabajo

En determinados sistemas generativos y bajo condiciones contextuales y evaluativas especificables, los cambios en el espacio de transformaciones accesibles contribuyen causalmente a los cambios de valor, a través de los mecanismos y trayectorias que esos cambios hacen posibles. La magnitud, dirección y distribución de esa contribución dependen de la composición del espacio transformacional, de las condiciones del sistema y de la regla de construcción de valor.

Esta formulación es una hipótesis de trabajo para diseñar pruebas falsables; no es una modificación del Core ni una afirmación de teoría consolidada.

## 3. Modelo causal y notación

- (X): contexto y características basales.
- (Z): intervención o asignación exógena.
- (L): condiciones habilitadoras y confusores posteriores a la intervención que pueden afectar accesibilidad y Value.
- (A): cambio en el espacio de transformaciones accesibles, operacionalizado como ΔT_acc.
- (M): mecanismos posteriores, incluidos Reach y Trayectoria.
- (O): outcomes observables.
- (V): Value, evaluado mediante una regla independiente.

DAG de trabajo (no una estructura causal universal):

`X → (Z,A,L,M,O,V)` en la medida en que corresponda al diseño; `Z → (L,A,M,O,V)`; `L → (A,M,O,V)`; `A → M → O → V`, con posibles vías alternativas `A → V`, `Z → O/V`, interacciones y confusión no medida.

La aleatorización de (Z) no aleatoriza automáticamente (A) ni (M), y no identifica por sí sola la mediación específica por accesibilidad. Una variable (L) inducida por (Z) que afecte tanto (A) como (V) impide una identificación simple por ajuste convencional.

## 4. Fronteras de medición: no sustituibilidad

La cadena de medición debe preservar constructos distintos:

1. **Estado/contexto/condiciones:** describen el sistema y sus restricciones, recursos y capacidades.
2. **Transformaciones accesibles ((T_{acc})):** conjunto estructurado de transformaciones realizables bajo condiciones especificadas; no es una lista de outcomes, adopciones o acciones observadas.
3. **Reach:** estados/configuraciones alcanzables mediante composiciones admisibles de transformaciones.
4. **Trayectoria:** secuencia efectivamente realizada. Debe derivarse de transformaciones TGCV, no identificarse sin más con transiciones observadas de estados.
5. **Outcome:** resultado observado.
6. **Value:** evaluación independiente con beneficiario/entidad, objetivo, regla, dirección, horizonte, costes, beneficios, compensaciones e incertidumbre.

Take-up, uso, inversión, empleo, ingresos, pobreza u otros resultados convencionales no son sustitutos automáticos de (T_{acc}), Reach ni Value.

### 4.1 Operacionalización de ΔT_acc

La unidad candidata de transformación es:

`τ=(S_o,S_d,M,P_τ,K,E)`

donde se representan origen, destino, mecanismo, predicado de admisibilidad, condiciones/dependencias/restricciones y evidencia.

La comparación entre escenarios requiere un universo común de transformaciones y una relación de equivalencia explícita `≡T`. Como mínimo, distinguir:

- `A⁺ = T_acc,1 \ T_acc,0`: transformaciones/configuraciones que pasan a ser accesibles;
- `A⁻ = T_acc,0 \ T_acc,1`: transformaciones/configuraciones que dejan de ser accesibles;
- `ΔT_acc = (A⁺, A⁻)`.

No reducir el objeto a cardinalidad neta: altas y bajas pueden compensarse numéricamente ocultando cambios de composición. Registrar por separado cambios de identidad, relaciones y configuraciones cuando la representación relacional sea necesaria. No contar dos veces transformaciones compuestas ni inferir una transformación nueva por la mera aparición de una relación.

Estados epistemológicos: accesible respaldada, inaccesible respaldada e indeterminada por evidencia insuficiente. Separar clasificación estimada de confianza/calidad de evidencia. La evidencia respalda la clasificación, pero no constituye por sí misma la condición causal de accesibilidad.

La accesibilidad requiere evidencia de realizabilidad y de precondiciones, recursos, admisibilidad y dependencias; no exige ejecución efectiva. Declaraciones de intención o resultados de Value no bastan como prueba.

## 5. Estimandos

### 5.1 Efecto total de la intervención

`TE = E[V(1)-V(0)]`

Describe el efecto total de (Z) sobre Value en el diseño y población definidos. No atribuye ese efecto a accesibilidad.

### 5.2 Efecto indirecto interventional específico de accesibilidad

Estimando de trabajo, condicionado a un régimen común (q(L)):

`θ_A(q) = E[V | do(L~q), do(A~G₁(·|L))] - E[V | do(L~q), do(A~G₀(·|L))]`

(G₁) y (G₀) representan distribuciones contrafactuales de cambios estructurales de accesibilidad inducidas por intervención y referencia, respectivamente, condicionadas por (L). Deben describirse mediante intervenciones concretas y realizables; no basta con ordenar un índice abstracto de accesibilidad.

La definición exacta del estimando, población, horizonte, régimen (q), distribuciones (G₁/G₀) y estrategia de identificación debe fijarse antes de observar outcomes/Value. No tratar la fórmula como identificada por defecto.

### 5.3 Efecto conjunto y heterogeneidad

Un estimando conjunto sobre distribuciones coherentes de (L,A), `θ_{L,A}`, puede recoger la contribución coordinada de condiciones y accesibilidad, pero no atribuye todo el efecto a (A).

Examinar modificación del efecto e interacciones (A×L), además de componentes de accesibilidad. No asumir aditividad ni descomposición automática:

`θ_A ≠ θ_U + θ_R + θ_C` en general.

Los componentes candidatos de la representación son transformaciones/unidades (U), relaciones (R) y configuraciones (C). Las combinaciones contrafactuales imposibles o incoherentes no deben estimarse por extrapolación.

El residual (TE-θ_A) solo puede calcularse si ambos estimandos son compatibles, están identificados en la misma población/escala y comparten la descomposición pertinente. No denominarlo efecto directo puro: puede contener vías alternativas, interacciones y mecanismos no observados.

## 6. Régimen común de condiciones y confusión post-treatment

No hay un régimen (q(L)) universalmente preferible. (q_0(L)=P(L|Z=0)), (q_1(L)=P(L|Z=1)) y un régimen objetivo (q^*(L)) responden a preguntas diferentes. La elección debe justificarse científicamente y fijarse antes del análisis; no elegirla retrospectivamente por sus resultados.

Dos familias de estimandos deben distinguirse:

- **Específico de accesibilidad bajo condiciones comunes:** compara (G₁) y (G₀) bajo el mismo régimen (q(L)). Puede excluir parte de la vía por la que la intervención cambia (L) y, a través de ella, (A).
- **Conjunto (L+A):** compara distribuciones conjuntas coherentes de condiciones y accesibilidad. Captura una vía más amplia, pero no es una atribución exclusiva a (A).

No restar automáticamente estos estimandos para obtener un supuesto efecto puro de (L). Verificar soporte/positividad para las distribuciones de accesibilidad en cada condición; no extrapolar fuera del soporte. Si (L) es inducido por (Z), no tratarlo como covariable basal ordinaria ni ajustar mecánicamente por él.

## 7. Requisitos de identificación

Antes de estimar (θ_A(q)), documentar:

1. **Consistencia y definición de intervención:** versiones suficientemente especificadas de (Z), (A), (L) y Value.
2. **Temporalidad:** orden defendible entre condiciones, accesibilidad, mecanismos, outcomes y Value.
3. **Medición independiente:** (A) y (V) no definidos a partir de los mismos outcomes ni uno del otro.
4. **Intercambiabilidad/ausencia de confusión relevante:** justificar para cada asignación o mediador según el diseño; declarar confusores no medidos plausibles.
5. **Positividad y soporte:** verificar que las distribuciones contrafactuales comparadas son realizables en los estratos relevantes.
6. **Tratamiento de confusión inducida por tratamiento:** especificar estrategia causal para (L), sin ajuste convencional que introduzca sesgo.
7. **Interferencia y unidad de asignación:** considerar spillovers, agrupación y correspondencia entre unidad de intervención, medición y análisis.
8. **Sensibilidad:** cuantificar cuánto dependerían los resultados de confusión no medida, error de medición, clasificación indeterminada y decisiones de modelado.
9. **Incertidumbre:** intervalos, precisión, potencia y límites de identificación; no basarse solo en significación estadística.

La aleatorización de (Z) identifica, bajo los supuestos del diseño, el efecto de la asignación/intervención. No garantiza exclusión, no aleatoriza (A) y no identifica por sí sola el efecto indirecto específico.

## 8. Jerarquía de diseños

Preferencia metodológica, no exclusión absoluta:

1. **Preferente:** variación experimental independiente de accesibilidad, manteniendo comparables las condiciones habilitadoras relevantes.
2. **Alternativa:** diseño factorial o por componentes que separe cambios en (A) y (L), siempre que las combinaciones sean realizables y la asignación esté justificada.
3. **Alternativa condicionada:** diseño cuasiexperimental u observacional con contrafactual defendible, supuestos explícitos, pruebas de falsación y sensibilidad.

Un efecto total causal de una intervención sobre Value no basta para afirmar C10 si no se identifica la contribución específica de accesibilidad.

## 9. Protocolo operativo y puertas de decisión

### Fase 0 — Delimitación y preregistro
- Definir sistema, unidad, población, contexto, horizonte y pregunta.
- Formular DAG/hipótesis alternativas y predicciones.
- Fijar estimando principal, (q(L)), (G₁/G₀), escala de Value y criterio de relevancia.
- Declarar qué resultados limitarían o contradirían la hipótesis.

**Puerta 0:** no avanzar si la pregunta, población, estimando o regla de Value son ambiguos.

### Fase 1 — Elegibilidad del caso
Evaluar sin puntuación compensatoria los requisitos esenciales:
- reconstrucción independiente de (T_{acc});
- variación causalmente defendible;
- separación de (L);
- medición independiente de Value;
- temporalidad;
- contrafactual identificable.

Clasificar los casos como:
- Tipo I: prueba metodológica;
- Tipo II: candidato de identificación que requiere reconstrucción/datos adicionales;
- Tipo III: caso probatorio que supera requisitos de medición e identificación.

**Puerta 1:** si falta un requisito esencial, no clasificar el caso como probatorio. Puede conservarse como prueba metodológica o candidato condicionado.

### Fase 2 — Reconstrucción y validación de mediciones
- Inventariar transformaciones y configuraciones con universo común.
- Reconstruir (T_{acc}) en escenarios comparables.
- Registrar altas, bajas, relaciones, configuraciones, condiciones y evidencia.
- Evaluadores independientes, idealmente ciegos a outcomes y Value.
- Auditar cobertura, desacuerdos, equivalencia, fiabilidad y clasificación indeterminada.
- Medir (L), Reach, Trayectoria, Outcome y Value por separado.

**Puerta 2:** no avanzar si (A) depende circularmente de outcomes/Value, si la cobertura impide comparar escenarios o si las condiciones de realizabilidad no están respaldadas.

### Fase 3 — Auditoría de identificación
- Especificar el mecanismo de asignación/variación.
- Revisar DAG, vías alternativas, confusión basal y post-treatment.
- Justificar (q(L)), soporte, positividad, consistencia e interferencia.
- Seleccionar estrategia de estimación y análisis de sensibilidad.
- Documentar qué parámetros son identificables y cuáles solo acotables.

**Puerta 3:** si (θ_A(q)) no está identificado, detener la atribución específica. Puede informarse TE u otros resultados claramente etiquetados, pero no presentarlos como evidencia de C10.

### Fase 4 — Estimación y análisis
- Estimar TE y (θ_A(q)) por separado cuando ambos sean identificables.
- Evaluar efectos conjuntos (L+A), interacciones y heterogeneidad preespecificada.
- Examinar mecanismos Reach/Trayectoria sin confundir mediación descriptiva con identificación causal.
- Informar estimaciones absolutas, intervalos y sensibilidad.
- Calcular residual solo si la descomposición es compatible.

### Fase 5 — Falsación, equivalencia y robustez
- Definir antes del análisis el efecto mínimo relevante (δ) y margen de equivalencia (ε), justificados por la regla de Value y la entidad evaluada.
- No fijar umbrales universales ni elegirlos después de conocer resultados.
- Si el intervalo queda dentro del margen de equivalencia, concluir ausencia de efecto relevante en el ámbito estudiado.
- Si el intervalo es amplio e incluye efectos relevantes, concluir imprecisión, no ausencia.
- Comprobar signos contrarios a predicciones direccionales preespecificadas, vías alternativas, falsificaciones y sensibilidad.

### Fase 6 — Síntesis y decisión científica
Clasificar el resultado en uno de tres estados:
- **Contribución causal identificada:** atribución de (A) a (V) defendible, con alcance delimitado.
- **Contribución limitada/refutada en el ámbito:** evidencia adversa precisa y robusta respecto a predicciones/umbrales preespecificados.
- **Identificación insuficiente:** no se puede resolver la atribución; no confirma ni refuta.

La generalización debe ser gradual:
- **A — Existencial:** contribución causal en al menos un ámbito delimitado.
- **B — Condicional:** condiciones que delimitan cuándo aparece, desaparece o cambia la contribución.
- **C — Generalización:** replicación y diversidad de dominios, con heterogeneidad explicada.

El objetivo de investigación propuesto es el nivel B; no se presupone que todos los sistemas presenten el mismo signo o magnitud.

## 10. Heterogeneidad y límites de alcance

Estudiar heterogeneidad según:
- composición de transformaciones;
- relaciones y configuraciones;
- condiciones (L);
- estado inicial (S_0);
- horizonte (H);
- beneficiario, objetivo y regla de Value.

La heterogeneidad explicable puede apoyar una hipótesis condicional. La heterogeneidad no explicada limita la generalización. Efectos sistemáticamente contrarios en contextos que cumplen condiciones preespecificadas son evidencia adversa para esa versión de la hipótesis.

No añadir condiciones retrospectivamente solo para excluir resultados desfavorables. Las condiciones de alcance deben declararse antes del análisis.

## 11. Criterios de selección de casos

No elegir por volumen de datos, familiaridad ni resultados favorables previos. Evaluar:

| Criterio | Prueba de elegibilidad |
|---|---|
| C1 — (T_{acc}) | Reconstrucción independiente antes/después |
| C2 — Variación | Intervención o variación defendible |
| C3 — (L) | Separación de condiciones habilitadoras |
| C4 — Mecanismos | Reach/Trayectoria derivados de transformaciones TGCV |
| C5 — Value | Regla independiente y operacionalizable |
| C6 — Temporalidad | Orden temporal verificable |
| C7 — Contrafactual | Estimando identificable y soporte suficiente |

Los requisitos esenciales no se compensan mediante una puntuación agregada.

## 12. Prueba de estrés: KGFS y límites de la evidencia actual

KGFS se conserva como caso de prueba metodológica de referencia, no como caso probatorio de C10 con la documentación actual.

- La asignación aleatoria de expansión temprana de infraestructura bancaria por área de servicio identifica el efecto del paquete de intervención dentro del alcance del diseño.
- El paquete introduce capacidades y condiciones (sucursal, préstamos, ahorro, seguros, asesoramiento) que pueden afectar simultáneamente (L), (A), outcomes y mecanismos.
- La evidencia existente respalda C09 en un alcance causal acotado sobre accesibilidad/infraestructura y trayectorias; no demuestra (ΔT_{acc}→ΔV).
- No consta reconstrucción independiente suficiente de (ΔT_{acc}) TGCV para el estimando, ni medición independiente de Value TGCV, ni estimación de (θ_A(q)).
- Take-up/uso, inversión, empleo, ingresos y pobreza no sustituyen (T_{acc}) ni Value.
- El cierre VSL-KGFS-02 `COMPATIBILITY_NOT_ESTABLISHED` permanece cerrado y no se reabre ni se reinterpreta mediante este protocolo.
- La auditoría 74/74 de variables de trayectoria no equivale a medición independiente de (T_{acc}) ni a evidencia C10.

Conclusión de la prueba: KGFS muestra por qué la aleatorización de una intervención compuesta no identifica automáticamente la mediación específica por accesibilidad. Con la documentación actual, (θ_A(q)) no es estimable. Esto no refuta C10; delimita requisitos y límites.

## 13. Estado de los casos conocidos

Evaluación preliminar basada en la documentación ya revisada; no constituye nueva auditoría de datos:

| Caso | Uso metodológico actual | Límite para C10 |
|---|---|---|
| KGFS | Tipo I — prueba metodológica | Sin (T_{acc}) independiente ni Value TGCV; (A) y (L) no separados para (θ_A(q)) |
| México C10C-002 | Caso de frontera para reconstrucción/medición | ITT sobre indicador cardinal (T_{acc}^*) no detectable; Value no estimado; no refuta toda C10 |
| Marruecos C10C-004 | Reconstrucción operacional acotada | Empoderamiento no equivale a (T_{acc}) ni Value TGCV |
| VSL sintético | Prueba de operacionalización/metodología | No proporciona causalidad empírica real ni confirmación/refutación general |
| Casos solares examinados | Casos de frontera | No superaron requisitos de reconstrucción estructural |

No se designa aún ningún caso Tipo III.

## 14. Requisitos de registro y reproducibilidad

Para cada estudio conservar:
- protocolo y versión preregistrada;
- definición de población, unidad, tratamiento y estimandos;
- diccionario y procedencia de variables;
- fichas de transformación y evidencia de admisibilidad;
- reglas de equivalencia y comparación de escenarios;
- instrumentos/reglas de Value;
- DAG, supuestos, código, configuración, logs y hashes;
- resultados completos, incertidumbre, sensibilidad y desviaciones del protocolo;
- decisión de alcance y límites de interpretación.

No almacenar datos personales/sensibles ni grandes datasets en Git. Aplicar la auditoría de privacidad/identificabilidad y las reglas de datos del repositorio antes de descargar o procesar fuentes externas.

## 15. Límites de esta persistencia

Este documento:
- consolida una propuesta metodológica desarrollada en conversación;
- no es un protocolo preregistrado ni aprobado;
- no demuestra validez de los estimandos ni suficiencia de los datos de ningún caso;
- no modifica Core, RMA, Matrix, STATUS ni claims;
- no autoriza ejecución, adquisición de datos ni cambios experimentales;
- no cambia cierres previos, en particular C09 ni VSL-KGFS-02.

## 16. Próxima operación metodológica

Antes de seleccionar un caso o ejecutar trabajo empírico:
1. revisión crítica del protocolo para detectar incompatibilidades entre estimandos, DAG y fases;
2. formalización de la estrategia de identificación de (θ_A(q)), en especial bajo confusión (L) inducida por tratamiento;
3. definición de la ficha mínima de medición de (T_{acc}), Reach, Trayectoria, Outcome y Value;
4. aplicación documental de los filtros de elegibilidad a candidatos, sin descargar ni procesar datos;
5. decisión explícita sobre si existe algún candidato Tipo II que merezca una auditoría de identificabilidad adicional.

**No iniciar selector predictivo ni trabajo de predictor en paralelo mientras C10 mantenga prioridad científica.**


---

## 17. Addendum metodológico — interacción, temporalidad y definición de las intervenciones (01-11-2026)

**Estado:** refinamiento metodológico pendiente de revisión; no aprobado, no preregistrado y no ejecutado.  
**Precedencia:** este addendum precisa y, donde se indica, restringe las formulaciones provisionales de las secciones 3, 5, 6, 7, 8, 9 y 16. No debe interpretarse la notación anterior como una definición causal ya cerrada.

### 17.1 Condiciones constitutivas y otras condiciones variables

La notación agregada (L) es insuficiente para todos los diseños. Debe descomponerse analíticamente, caso por caso, al menos en:

- **(L_c): condiciones constitutivas o habilitadoras de accesibilidad.** Recursos, capacidades, permisos, dependencias, restricciones y otras condiciones que participan en la determinación de qué transformaciones son realizables. Pueden formar parte de la función que genera el espacio accesible, por ejemplo (T_{acc,t}=F(S_t,C_t,L_{c,t})).
- **(L_m): otras condiciones variables en el tiempo** que pueden afectar accesibilidad, mecanismos, outcomes o Value y desempeñar funciones de confusión, mediación o vías alternativas.

La clasificación depende de la estructura del sistema y del momento temporal, no del nombre de una variable. Una misma variable puede cambiar de papel entre momentos o contextos; cada papel debe justificarse mediante el modelo causal y la evidencia del caso.

No se debe ajustar mecánicamente por (L_c) como si fuera siempre un confusor externo a (T_{acc}). Mantener fija una condición constitutiva mientras se modifica accesibilidad puede definir una intervención imposible o incoherente. Tampoco se debe clasificar automáticamente toda variable post-treatment como (L_m) ni asumir que basta con condicionarla estadísticamente.

### 17.2 Factibilidad de las políticas y soporte común

Las políticas sobre accesibilidad deben respetar las condiciones de realizabilidad del sistema. Para una historia/contexto (h_t), defínase conceptualmente el conjunto factible (\mathcal{A}_{fact}(h_t)). Una política (g_j) solo puede asignar configuraciones de accesibilidad pertenecientes a ese conjunto:

(g_j(A_t\mid h_t)=0) para (A_t\notin\mathcal{A}_{fact}(h_t)).

La comparación de dos políticas bajo un régimen común de condiciones solo es interpretable cuando ambas políticas tienen soporte factible en la población/historias a las que se aplica el contraste. Si la variación de (L_c) es constitutiva del cambio de accesibilidad y no existe soporte común para variar (A) manteniendo un régimen comparable, no debe forzarse una atribución aislada mediante extrapolación. En tal caso, el objeto defendible puede ser una intervención conjunta sobre condiciones y accesibilidad.

El régimen común no tiene por qué fijar todas las condiciones en un valor constante. Puede ser una distribución conjunta explícita sobre historias o condiciones, condicionada por covariables basales, siempre que sea causalmente interpretable, realizable y fijada ex ante.

### 17.3 Efectos condicionados e interacción (A × L)

Cuando existan combinaciones factibles, se pueden definir efectos de accesibilidad bajo regímenes concretos de condiciones:

(θ_A(q_0)=E[V^{q_0,g_1}]-E[V^{q_0,g_0}])

(θ_A(q_1)=E[V^{q_1,g_1}]-E[V^{q_1,g_0}]).

La interacción aditiva entre políticas de accesibilidad y regímenes de condiciones es:

(I_{A,L}=[E[V^{q_1,g_1}]-E[V^{q_1,g_0}]]-[E[V^{q_0,g_1}]-E[V^{q_0,g_0}]]).

(I_{A,L}) expresa cuánto cambia el contraste de accesibilidad entre los dos regímenes de condiciones en la escala aditiva de Value preespecificada. No es una interacción universal independiente de la escala, ni una descomposición automática del efecto total. La escala, los regímenes, el margen de relevancia y las combinaciones factibles deben fijarse antes del análisis.

Si las cuatro combinaciones no son realizables o carecen de soporte, no estimar las celdas contrafactuales imposibles ni extrapolar para completar un factorial aparente. Informar el límite de identificación y, si procede, estimar solo contrastes conjuntos factibles.

### 17.4 Estructura longitudinal y actualización del espacio accesible

La secuencia debe indexarse temporalmente. Como esquema de trabajo:

- en (t), el sistema tiene estado y condiciones (S_t,C_t,L_{c,t},L_{m,t});
- se reconstruye (T_{acc,t}) a partir de esa configuración;
- se ejecuta, o no, una transformación (τ_t) perteneciente a las posibilidades admisibles;
- la ejecución puede modificar el estado y las condiciones;
- en (t+1), se vuelve a reconstruir (T_{acc,t+1}) a partir de la nueva configuración.

Representación conceptual:

((S_t,C_t,L_{c,t},L_{m,t}) → T_{acc,t} → τ_t → (S_{t+1},C_{t+1},L_{c,t+1},L_{m,t+1}) → T_{acc,t+1}).

Reach y Trayectoria deben derivarse de las transformaciones TGCV admisibles y de su actualización a lo largo de la secuencia; no deben reducirse a transiciones observadas entre estados ni calcularse necesariamente sobre un espacio fijo.

La medición debe registrar para cada variable relevante identidad, momento/intervalo, papel causal en ese momento, dependencias previas, consecuencias posteriores, procedencia y calidad de evidencia. No asignar papeles causales solo por conveniencia del modelo estadístico.

Value debe tener horizonte explícito. Puede representar valor realizado, acumulado o diferido, según una regla independiente que contemple costes, beneficios, compensaciones, beneficiario y posibles efectos intermedios. No elegir el horizonte después de observar los resultados.

Cuando existan confusores variables en el tiempo afectados por tratamiento previo, una regresión convencional con ajuste indiscriminado puede bloquear vías causales o introducir sesgo. G-computation, modelos estructurales marginales o TMLE longitudinal son opciones condicionadas a supuestos defendibles; ningún método resuelve automáticamente confusión no medida, mala medición, falta de positividad o mala especificación temporal.

### 17.5 Intervención manipulable, respuesta estructural y ejecución

No definir “aumentar (T_{acc})” como tratamiento causal abstracto. Distinguir:

1. **Intervención/política (Z o π):** acción asignable o mecanismo realizable sobre el sistema, especificado por componente, unidad afectada, intensidad/alcance, momento/duración, población y condiciones de implementación.
2. **Respuesta estructural (A=ΔT_{acc}):** cambio en las transformaciones accesibles producido por la intervención, medido independientemente de su ejecución y de Value.
3. **Ejecución (τ):** transformación concreta efectivamente realizada, que puede modificar el estado y la accesibilidad futura.

Una política dinámica puede representarse como (π:h_t→Z_t), donde (h_t) es la historia disponible hasta (t). La secuencia de espacios accesibles inducida por la política debe medirse en cada momento; el efecto de una política dinámica no es intercambiable con el efecto de un cambio puntual de accesibilidad.

La especificación de la intervención debe permitir identificar versiones relevantes: mecanismo/componente, elemento del sistema, intensidad, temporalidad, población/unidad y condiciones de implementación. La asignación aleatoria de (Z) puede identificar el efecto total de la asignación bajo los supuestos del diseño, pero no aleatoriza automáticamente (A), no garantiza exclusión y no identifica por sí sola la contribución específica de accesibilidad.

### 17.6 Versiones de tratamiento y equivalencia de políticas

Dos políticas que producen el mismo (ΔT_{acc}) medido no son automáticamente equivalentes causalmente. Pueden diferir en costes, tiempos, calidad, riesgos, distribución de beneficios u otras vías hacia Value. Por tanto, igualdad de accesibilidad observada no implica igualdad de resultados potenciales de Value.

Distinguir:

- **Equivalencia de accesibilidad:** mismo cambio estructural bajo un universo, representación, equivalencia (≡T), contexto y horizonte comunes.
- **Equivalencia de vías relevantes para Value:** además, las diferencias entre políticas no introducen vías alternativas relevantes para Value, o estas quedan separadas por un diseño/estimando defendible. Es el requisito más importante para una atribución específica.
- **Equivalencia de versión de tratamiento:** las versiones agrupadas bajo una misma política satisfacen una definición de intervención y consistencia previamente justificada.

No agrupar políticas distintas solo porque comparten un indicador o cardinalidad de (ΔT_{acc}). Si no puede defenderse equivalencia de versiones o separarse sus vías alternativas, informar el efecto de la política concreta o del paquete, no un efecto puro de accesibilidad.

### 17.7 Notación de estimandos precisada

La notación de la sección 5.2 debe leerse como abreviatura provisional. La formulación de trabajo más explícita es:

(θ_A(q)=E[V^{q,g_1}]-E[V^{q,g_0}]).

Aquí (q) define un régimen común y factible de condiciones/historias, y (g_1) y (g_0) son políticas estocásticas concretas sobre cambios de accesibilidad, condicionadas por covariables basales e historia relevante y restringidas a (\mathcal{A}_{fact}). La respuesta posterior de Reach, Trayectoria, Outcome y Value evoluciona bajo cada política; por tanto, el contraste puede incluir las consecuencias de accesibilidad a través de esos mecanismos.

Este contraste no es automáticamente un efecto indirecto natural, no es una fracción del efecto total y no queda identificado por sustituir (g_j) por distribuciones observadas (P(A\mid Z,L)). Su identificación exige justificar consistencia/versiones, temporalidad, ausencia de confusión relevante para la asignación de la política sobre (A), tratamiento de confusión inducida por tratamiento, positividad/soporte, interferencia y medición. Si esos supuestos no son defendibles, declarar (θ_A(q)) no identificado.

Un contraste conjunto puede expresarse como:

(θ_{L,A}=E[V^{q_1,g_1}]-E[V^{q_0,g_0}]).

Este recoge el efecto de un cambio coordinado de régimen de condiciones y política de accesibilidad; no atribuye todo el contraste a (A). Los contrastes simples e interacción de la sección 17.3 solo se interpretan cuando sus políticas/regímenes son coherentes y factibles.

No asumir que (TE=θ_A(q)+θ_{L,A}), ni que (TE-θ_A(q)) es un efecto directo puro. Cualquier descomposición del efecto total requiere definir una secuencia explícita de intervenciones y contrastes compatibles; puede depender del orden de intervención y de las interacciones.

### 17.8 Consecuencias para la interpretación científica

- Un efecto total de (Z) sobre Value demuestra, como máximo, un efecto de esa intervención en el ámbito estudiado; no establece atribución específica a (A).
- Un (θ_A(q)) identificado respalda una contribución de accesibilidad bajo las políticas, condiciones, población, horizonte y regla de Value especificados.
- Un (θ_{L,A}) identificado respalda una contribución conjunta de condiciones y accesibilidad, no una atribución exclusiva a accesibilidad.
- Un (θ_A(q)) nulo bajo un régimen concreto no demuestra que accesibilidad sea irrelevante bajo otros regímenes, ni descarta una contribución conjunta o una interacción.
- La ausencia de soporte, las combinaciones imposibles o la falta de identificación deben informarse como límites, no como evidencia confirmatoria o refutatoria.
- Un efecto adverso solo limita/refuta la versión de la hipótesis y el ámbito definidos ex ante, con precisión suficiente y criterios de relevancia preespecificados.

### 17.9 Consecuencia operativa y estado

Antes de seleccionar un caso o ejecutar análisis empírico, el protocolo debe:

1. clasificar (L_c) y (L_m) y justificar sus papeles temporales;
2. especificar intervenciones/políticas concretas y versiones relevantes;
3. definir el conjunto de configuraciones de accesibilidad factibles bajo cada historia;
4. comprobar soporte común para los contrastes específicos y conjuntos;
5. preespecificar horizonte y regla independiente de Value;
6. decidir si el estimando es puntual, condicionado o dinámico;
7. documentar identificación y límites antes de estimar.

Este addendum no selecciona caso, no autoriza descarga/procesamiento de datos ni ejecución experimental. No cambia TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims, cierres C09 o VSL-KGFS-02, ni reanuda el predictor. El PR permanece como borrador metodológico pendiente de revisión.


---

## 18. Addendum metodológico — medición longitudinal y separación ontológico-epistemológica de T_acc (01-11-2026)

**Estado:** propuesta metodológica pendiente de revisión; no constituye validación empírica ni cambio de Core.

### 18.1 Dos objetos distintos

Separar en cada momento:
- **Estado transformacional del sistema:** qué transformaciones son realmente realizables bajo el estado, contexto, condiciones, recursos, dependencias y restricciones existentes.
- **Estado epistemológico:** qué transformaciones han sido identificadas y qué evidencia permite clasificarlas.

Un cambio en el conocimiento o en la cobertura de observación no demuestra por sí mismo un cambio en el espacio accesible. No inferir accesibilidad a partir de outcomes, ejecución observada o declaraciones de intención.

### 18.2 Estados epistemológicos

Para cada transformación candidata y momento de referencia, registrar:
- accesible respaldada;
- inaccesible respaldada;
- indeterminada.

La confianza/calidad de evidencia se registra en campos separados; no es un cuarto estado de accesibilidad. Ausencia de evidencia no equivale a evidencia de inaccesibilidad. Una transformación indeterminada no se computa automáticamente como ganancia ni pérdida.

### 18.3 Cambio ontológico estimado y cambio epistemológico

Distinguir analíticamente:
- cambio ontológico estimado de accesibilidad: diferencia entre los espacios que se infieren para dos momentos, bajo condiciones y criterios comparables;
- cambio epistemológico: diferencia en conocimiento, identificación, cobertura, calidad o clasificación de evidencia.

Una transformación descubierta en t1 puede haber sido accesible ya en t0. La reconstrucción retrospectiva de t0 es admisible solo si la evidencia se refiere a las condiciones y capacidades existentes entonces; no proyectar hacia atrás capacidades adquiridas después. Registrar cuándo se obtuvo la evidencia y a qué momento del sistema se refiere.

### 18.4 Comparabilidad longitudinal

Para comparar T_acc,t0 y T_acc,t1:
1. fijar universo de transformaciones candidatas, identidad y equivalencia ≡T comunes;
2. documentar estado, contexto, condiciones y horizonte de cada evaluación;
3. utilizar evidencia fechada o retrospectivamente atribuible al momento correcto;
4. evaluar accesibilidad independientemente de Outcome y Value;
5. registrar cobertura, fuentes, incertidumbre y cambios de procedimiento;
6. separar cambios de clasificación debidos a nueva evidencia de cambios atribuibles a una modificación del sistema.

Si el universo candidato, los criterios de identidad, la cobertura o el procedimiento cambian, documentar el cambio y realizar análisis de sensibilidad/reconstrucción; no interpretar directamente el recuento de nuevas transformaciones identificadas como ΔT_acc.

### 18.5 Registro mínimo por transformación y momento

Registrar identidad/mecanismo, origen y destino, condiciones y recursos, precondiciones y restricciones, momento del sistema evaluado, momento de obtención de evidencia, estado epistemológico, calidad/confianza, fuente/procedencia, cobertura de búsqueda, evaluador y justificación de revisiones.

Los evaluadores deben, cuando sea viable, desconocer Outcomes y Value para reducir sesgo de clasificación. La independencia de evaluación y el acuerdo entre evaluadores deben documentarse; el acuerdo no sustituye la validez de la evidencia.

### 18.6 Estimación de ΔT_acc

No reducir el cambio a una diferencia de cardinalidades. Bajo un universo común y una equivalencia explícita, registrar al menos:
- transformaciones nuevas respaldadas como accesibles;
- transformaciones previamente accesibles que dejan de serlo;
- transformaciones cuya accesibilidad se reconfigura por cambios de mecanismo, condiciones o dependencias;
- casos indeterminados en cualquiera de los momentos.

La comparación debe preservar composición y relaciones, no solo el número neto. Los casos indeterminados deben reflejarse como incertidumbre o límites, no imputarse silenciosamente. Si no existe comparabilidad suficiente, declarar ΔT_acc no estimable con la evidencia disponible.

### 18.7 Consecuencia para identificación causal

El error de medición de accesibilidad puede sesgar estimandos de C10; si la calidad de medición cambia con la intervención, el sesgo puede ser diferencial. Por ello, la evaluación de T_acc debe ser independiente del proceso que mide Outcome/Value, con protocolo estable, cobertura comparable, trazabilidad y análisis de sensibilidad a clasificación errónea.

No utilizar la misma evidencia de Value para inferir retrospectivamente qué era accesible y luego afirmar que accesibilidad explica Value. Esa circularidad invalidaría la separación de constructos.

Este addendum no selecciona caso, no autoriza datos ni ejecución. No modifica Core, RMA, Matrix, STATUS, claims, cierres previos ni el predictor. El PR permanece draft y pendiente de revisión.


---

## 19. Addendum metodológico — fiabilidad, equivalencia y reproducibilidad de la medición de T_acc (01-11-2026)

**Estado:** propuesta metodológica pendiente de revisión; no aprobada, no preregistrada y no ejecutada. Complementa los apartados 17 y 18. El acuerdo entre evaluadores no se considera por sí solo prueba de validez del constructo.

### 19.1 Unidad de análisis e identidad transformacional

La unidad candidata de registro es (τ=(S_o,S_d,M,P_τ,K,E)): origen, destino, mecanismo, precondiciones/admisibilidad, recursos/dependencias/restricciones y evidencia de realizabilidad.

La identidad no debe depender solo de etiquetas, descripciones textuales ni resultados observados. Dos descripciones pueden referirse a una misma transformación; dos mecanismos distintos pueden producir un mismo resultado y seguir siendo transformaciones diferentes. Las reglas de identidad y equivalencia (≡T) deben considerar mecanismo, condiciones y estructura, y aplicarse consistentemente entre momentos y evaluadores.

### 19.2 Composición, variantes y doble conteo

Registrar explícitamente:
- duplicados descriptivos que deben resolverse como una identidad;
- transformaciones distintas que comparten resultado pero difieren en mecanismo;
- transformaciones compuestas y sus componentes;
- variantes cuyo mecanismo común tiene condiciones de realización diferentes.

Una transformación compuesta no se contará automáticamente como una transformación independiente adicional si ello duplica sus componentes o altera artificialmente la cardinalidad. La regla de composición, granularidad y equivalencia debe fijarse antes de comparar momentos. Si cambia, reconstruir retrospectivamente ambos momentos con la regla común o declarar la comparación no directamente comparable.

### 19.3 Evaluación independiente y ciega

Cuando sea viable, dos evaluadores clasificarán independientemente el mismo expediente, sin conocer Outcome ni Value. Para cada transformación y momento registrarán por separado:
- identidad y equivalencia;
- accesibilidad (accesible respaldada, inaccesible respaldada, indeterminada);
- admisibilidad y precondiciones;
- suficiencia/calidad de evidencia;
- justificación y fuentes.

La confianza de evidencia no sustituye el estado epistemológico. El acuerdo se calcula por dimensión, no mediante un único indicador agregado. Documentar entrenamiento, instrucciones, casos de calibración, cegamiento, orden de evaluación y posibles conflictos de interés.

### 19.4 Fiabilidad interevaluador

Informar matriz de desacuerdos, acuerdo observado y, cuando proceda, estadísticos como kappa o alfa de Krippendorff seleccionados según número de evaluadores, escala, datos faltantes y diseño. Informar prevalencia de categorías y distribución de casos indeterminados, ya que un coeficiente aislado puede resultar engañoso con categorías desequilibradas.

No fijar umbrales universales sin estudio piloto y justificación. Los umbrales de aceptación, reglas de recalibración y criterios para suspender la medición deben preespecificarse. Un acuerdo elevado no demuestra que la clasificación corresponda a la accesibilidad real: requiere además validez de contenido/constructo y evidencia de realizabilidad.

### 19.5 Desacuerdo, adjudicación y trazabilidad

Conservar sin sobrescribir:
1. clasificaciones independientes originales;
2. adjudicación motivada mediante tercer evaluador o procedimiento previamente definido;
3. desacuerdo residual no resoluble con la evidencia disponible.

La adjudicación no puede transformar una clasificación indeterminada en accesible sin nueva evidencia suficiente. Cada cambio debe registrar evaluador, fecha, motivo, evidencia nueva y versión del criterio aplicado. Mantener historial de cambios y posibilidad de reconstruir resultados anteriores.

### 19.6 Error de clasificación y sensibilidad causal

Evaluar falsos positivos, falsos negativos, indeterminación y error diferencial entre brazos, momentos o condiciones. Una intervención puede cambiar la visibilidad/documentación de capacidades y generar una diferencia aparente en T_acc sin modificar la accesibilidad real.

La sensibilidad debe examinar cómo reglas plausibles de clasificación y tasas de error afectan:
- transformaciones nuevas/perdidas y reconfiguradas;
- estimación de ΔT_acc;
- soporte y asignación de políticas g;
- estimandos θ_A(q) y θ_A^dyn, cuando se pretendan estimar.

Si la calidad de medición depende de intervención, momento, evaluador o resultado, una fiabilidad global no basta. Considerar subestudio de validación, fuentes independientes, revisión ciega o cotas/análisis de sensibilidad. No corregir error de medición mediante supuestos no contrastados ni usar Value para resolver retrospectivamente la accesibilidad.

### 19.7 Reproducibilidad del procedimiento

Conservar protocolo e instrucciones de evaluación versionados, universo candidato, reglas de identidad/equivalencia, expedientes de evidencia, formularios de clasificación, resultados originales, adjudicaciones, scripts de cálculo, parámetros, versiones de herramientas y hashes de artefactos. Una repetición independiente debe poder reconstruir las clasificaciones y los cambios de accesibilidad a partir de esos registros.

### 19.8 Puerta de decisión

Antes de aceptar una medición longitudinal para C10:
- identidad, granularidad y equivalencia están definidas y son estables;
- cobertura y evidencia son comparables o sus diferencias están modelizadas;
- evaluaciones independientes y desacuerdos están preservados;
- la fiabilidad se informa por dimensión y no se confunde con validez;
- el error diferencial y su impacto en ΔT_acc/estimandos se han evaluado;
- las transformaciones indeterminadas no se imputan silenciosamente.

Si falla una condición esencial, calificar la medición como insuficiente/no comparable y limitar la inferencia causal. No interpretar automáticamente desacuerdo, falta de cobertura o error de medición como ausencia de cambio real.

Este addendum no selecciona caso, no autoriza adquisición/procesamiento de datos ni ejecución experimental. No modifica Core, RMA, Matrix, STATUS, claims, cierres C09 o VSL-KGFS-02, ni reanuda el predictor. El PR permanece draft, pendiente de revisión.


---

## 20. Addendum metodológico — validez externa, transportabilidad y alcance de C10 (01-11-2026)

**Estado:** propuesta metodológica pendiente de revisión; no aprobada, no preregistrada y no validada empíricamente. Este apartado define criterios para interpretar y extender evidencia causal; no eleva claims ni modifica el Core.

### 20.1 Niveles de conclusión

Distinguir:
- **Efecto localizado:** contribución causal identificada en un sistema/población, configuración, horizonte, política y regla de Value delimitados.
- **Regularidad condicional:** contribución reproducida en más de un contexto y asociada a condiciones/modificadores especificados previamente.
- **Generalización de alcance:** evidencia acumulada que respalda una regularidad condicional en una clase delimitada de sistemas generativos, con límites explícitos.

No inferir universalidad a partir de un efecto localizado. No confundir una colección de réplicas estructuralmente similares con evidencia de diversidad de sistemas. El nivel de conclusión debe reflejar la unidad de evidencia y la heterogeneidad observada.

### 20.2 Dimensiones de comparabilidad y modificación del efecto

Antes de transportar o generalizar, caracterizar por sistema:
- composición y estructura de T_acc, transformaciones nuevas/perdidas/reconfiguradas;
- relaciones, dependencias y configuraciones transformacionales;
- estado inicial y dinámica del sistema;
- condiciones constitutivas y otras condiciones habilitadoras/restrictivas;
- mecanismos de ejecución, Reach y Trayectoria;
- política/intervención, sus versiones, intensidad y vías alternativas;
- regla de Value, beneficiario, objetivo, costes, beneficios, compensaciones y horizonte;
- calidad y comparabilidad de la medición, cobertura y error de clasificación.

Estas dimensiones no son todas simples covariables de ajuste. Algunas constituyen la definición del sistema transformacional; otras pueden modificar el efecto o la respuesta al tratamiento. Su papel debe justificarse causal y temporalmente. Una diferencia de efecto entre sistemas no implica automáticamente contradicción: puede reflejar modificación del efecto por composición, condiciones, mecanismos o regla de Value.

### 20.3 Replicación, reproducción contextual, transporte y generalización

Separar cuatro operaciones:
1. **Replicación:** repetir el contraste en condiciones y estructura similares.
2. **Reproducción contextual:** repetirlo en otro entorno con mecanismos y arquitectura comparables.
3. **Transporte:** estimar el efecto en una población/sistema objetivo diferente a partir de evidencia de origen y supuestos explícitos.
4. **Generalización teórica:** establecer una regularidad condicional en una clase de sistemas delimitada.

El número de casos no sustituye a la diversidad estructural. Varias réplicas del mismo tipo pueden precisar la reproducibilidad local, pero no necesariamente identificar los límites de validez externa.

### 20.4 Estimando de transporte

Sea (S=1) el sistema/población de origen y (S=0) la población objetivo, y sea (W) el conjunto de características basales o estructurales que modifican el efecto y que se miden de forma comparable. El estimando objetivo es:

(theta_target=E_target[V^{g_1}-V^{g_0}]).

La estimación a partir del origen puede requerir estimar efectos condicionales por (W) y estandarizarlos a la distribución objetivo, o usar ponderación/estimadores de transporte. No asumir que (theta_target=theta_source).

La identificación requiere, según el diseño:
- consistencia y versiones de política comparables;
- intercambiabilidad interna en el estudio de origen;
- intercambiabilidad de selección/transporte condicionada a modificadores suficientes (no quedan diferencias origen-destino que alteren el efecto tras condicionar por W);
- positividad de selección y soporte común: perfiles relevantes del objetivo están representados en el origen;
- medición comparable de W, accesibilidad, mecanismos y outcome;
- interferencia ausente o modelizada en ambos contextos.

Estos supuestos no son demostrables solo con los datos observados. Deben justificarse por conocimiento del sistema, diseño, diagnóstico de soporte y análisis de sensibilidad. Si no son defendibles, no presentar una estimación puntual transportada como identificada.

### 20.5 Regla de Value y comparabilidad evaluativa

Value no es necesariamente una escala universal intercambiable entre sistemas. Beneficiarios, objetivos, costes, compensaciones, umbrales y horizontes pueden diferir legítimamente.

Antes de comparar efectos:
- especificar si la pregunta usa una regla de Value común o reglas contextuales distintas;
- si se usa una regla común, justificar su validez y significado en cada sistema;
- si las reglas son distintas, no comparar directamente magnitudes como si estuvieran en la misma escala;
- cuando sea posible, informar resultados bajo la regla local y bajo una regla común explícitamente justificada;
- documentar distribución de costes/beneficios y heterogeneidad entre beneficiarios, no solo un promedio agregado.

Si la regla de Value cambia, puede cambiar el signo o magnitud del efecto sin que cambie la accesibilidad. Esto es una diferencia evaluativa que debe hacerse visible, no tratarse como ruido ni corregirse retrospectivamente para obtener homogeneidad.

### 20.6 Modificación del efecto y heterogeneidad

Preespecificar modificadores plausibles antes de observar los resultados comparativos: estructura/composición de T_acc, dependencias, estado inicial, condiciones habilitadoras, mecanismos, política, horizonte y regla de Value. Distinguir:
- heterogeneidad del efecto causal;
- heterogeneidad de la medición;
- heterogeneidad de la definición/regla de Value;
- heterogeneidad de implementación y versiones de política.

No buscar subgrupos retrospectivamente para excluir efectos negativos ni seleccionar solo contextos favorables. Informar efectos por contexto, incertidumbre, distribución y límites de soporte. Un promedio agregado puede ocultar efectos nulos o adversos en subpoblaciones relevantes.

### 20.7 Programa de evidencia multi-sistema

Una secuencia prudente sería:
1. Identificación causal en un caso con medición independiente y diseño defendible.
2. Replicación en condiciones próximas para comprobar reproducibilidad.
3. Reproducción contextual en sistemas con arquitectura transformacional comparable pero entorno diferente.
4. Contraste deliberado en sistemas estructuralmente distintos para identificar modificadores y límites.
5. Síntesis de efectos y heterogeneidad, sin imponer un efecto común si no está justificado.
6. Formulación de una regularidad condicional que indique población/clase, condiciones, políticas, mecanismos, horizonte y regla de Value.

Los casos deben seleccionarse por capacidad de probar mecanismos y límites, no por probabilidad de producir un efecto positivo. Conservar resultados nulos, adversos y no identificados.

### 20.8 Puerta de decisión y lenguaje de conclusión

Antes de afirmar transporte/generalización, documentar:
- población/sistema origen y objetivo;
- estimando en ambos;
- modificadores del efecto y distribución;
- soporte común y positividad;
- equivalencia/compatibilidad de políticas y mediciones;
- regla de Value y horizonte;
- supuestos de transporte y sensibilidad;
- heterogeneidad, efectos adversos y límites.

Lenguaje permitido:
- «Se identificó una contribución causal en el sistema y ámbito estudiados».
- «La contribución se reprodujo en los contextos evaluados».
- «La evidencia respalda una regularidad condicional en la clase delimitada».
- «El efecto no pudo transportarse/identificarse con los datos y supuestos disponibles».

No afirmar «C10 es universal» ni convertir una estimación localizada en validación general. Una falta de transporte puede indicar diferencias estructurales, evaluativas o falta de soporte; no refuta automáticamente la contribución local ni confirma una regularidad alternativa.

Este addendum no selecciona casos, no autoriza adquisición/procesamiento de datos ni ejecución experimental. No modifica Core, RMA, Matrix, STATUS, claims, cierres C09 o VSL-KGFS-02, ni reanuda el predictor. El PR permanece draft y pendiente de revisión.


---

## 21. Addendum metodológico — falsabilidad, equivalencia práctica y tratamiento de evidencia adversa (01-11-2026)

**Estado:** propuesta metodológica pendiente de revisión; no aprobada, no preregistrada ni ejecutada. No establece todavía valores numéricos de efecto mínimo, margen de equivalencia, potencia o tamaño muestral: estos dependen de la regla de Value y del diseño concreto.

### 21.1 Alcance falsable y versión de hipótesis

Cada prueba debe delimitar antes de observar resultados:
- sistema, población/unidades y periodo;
- estado inicial, contexto y condiciones relevantes;
- política/intervención y versiones;
- cambio de accesibilidad que se pretende inducir y cómo se medirá;
- mecanismos/mediadores y secuencia temporal esperada;
- estimando primario (efecto de política, θ_A(q), θ_A^dyn o efecto conjunto);
- regla independiente de Value, beneficiario, escala y horizonte;
- dirección esperada, si está justificada;
- modificadores, exclusiones y límites de generalización;
- efecto mínimo relevante δ y margen de equivalencia ε, con justificación previa.

La hipótesis condicional no autoriza a introducir después del resultado nuevas condiciones para excluir el caso. Una condición o moderador descubierto posteriormente puede originar una hipótesis nueva y una prueba posterior; no reinterpreta retroactivamente la prueba original.

### 21.2 Estimando primario y separación de preguntas

No mezclar:
- efecto total de asignación/intervención sobre Value (TE);
- contribución de una política específica de accesibilidad bajo régimen definido (θ_A(q));
- contribución de política dinámica de accesibilidad (θ_A^dyn);
- efecto conjunto de condiciones y accesibilidad (θ_L,A);
- efectos sobre Reach, Trayectoria u Outcome.

El estimando primario y la escala deben fijarse antes del análisis. Los demás son secundarios o mecanísticos, con su propio alcance. Un efecto positivo de TE o θ_L,A no sustituye evidencia de θ_A. Un efecto nulo de θ_A(q) limita esa política y régimen; no demuestra que toda política de accesibilidad sea irrelevante.

### 21.3 δ y ε: relevancia y equivalencia

Definir por separado:
- **δ:** efecto mínimo de Value considerado científicamente/prácticamente relevante en la escala y horizonte elegidos.
- **ε:** margen de equivalencia práctica alrededor de cero, justificado por la regla de Value, incertidumbre de medición y consecuencias de decisión.

No asumir que δ=ε. Justificar ambos antes de observar los resultados mediante criterios sustantivos, participación de beneficiarios/decisores pertinentes, propiedades de la medición y consecuencias de errores. No elegirlos para acomodar el tamaño del efecto observado.

Para una hipótesis direccional positiva, la interpretación orientativa es:
- intervalo de incertidumbre completamente por encima de δ: evidencia de efecto positivo relevante;
- intervalo completamente dentro de [-ε,+ε]: evidencia de equivalencia práctica con cero en el ámbito;
- intervalo completamente por debajo de -δ: evidencia de efecto adverso relevante;
- intervalo que cruza umbrales o incluye regiones relevantes distintas: resultado inconcluso.

La regla exacta de decisión, nivel de error, intervalo y procedimiento (incluidos métodos de equivalencia) debe preespecificarse. Un p-valor no significativo no demuestra equivalencia; un intervalo amplio que incluye cero no es evidencia de ausencia.

### 21.4 Falsación por eslabón de la cadena

Evaluar la cadena completa, manteniendo separado el fallo de manipulación del contraste causal sobre Value:

1. **Intervención/política no modifica T_acc como estaba previsto:** fallo de manipulación/implementación o de la hipótesis sobre esa intervención; no estima la contribución causal del cambio de accesibilidad que no ocurrió.
2. **T_acc cambia, pero Reach no responde como se preespecificó:** evidencia adversa para el vínculo accesibilidad–Reach en ese sistema y horizonte, si ambas mediciones son válidas.
3. **Reach cambia, pero Trayectoria no responde como se preespecificó:** evidencia adversa para el mecanismo dinámico propuesto en ese ámbito.
4. **Trayectoria/Outcome cambian, pero Value no:** evidencia adversa para el vínculo con la regla de Value y horizonte especificados; no equivale por sí sola a un θ_A nulo si el estimando específico no está identificado.
5. **θ_A(q) o θ_A^dyn está identificado y es equivalente a cero con precisión suficiente:** evidencia directa contra una contribución relevante de la política de accesibilidad en el ámbito delimitado.
6. **Estimando identificado con signo contrario a la dirección preespecificada y magnitud relevante:** evidencia adversa para esa predicción direccional.
7. **Medición, identificación o soporte insuficientes:** resultado no concluyente; no confirmar ni refutar.

Un resultado adverso en un eslabón no autoriza a reescribir retrospectivamente la cadena. Debe registrarse qué proposición concreta queda cuestionada y cuáles permanecen no evaluadas.

### 21.5 Evidencia contra la hipótesis y alcance de la conclusión

Una equivalencia práctica bien identificada de θ_A en un contexto limita la hipótesis para esa población, política, régimen, horizonte y regla de Value. No refuta automáticamente todos los contextos condicionales de C10.

Para cuestionar una regularidad condicional más amplia, se requiere replicación/contraste en los contextos que la hipótesis afirmaba cubrir, con medición e identificación comparables. Si la formulación de alcance es tan amplia que no especifica contextos donde se espera un efecto, no es suficientemente falsable y debe precisarse antes de probarla.

No se puede proteger la hipótesis invocando un moderador no medido o descubierto solo después de un resultado adverso. Las hipótesis modificadas reciben nueva versión, predicciones y prueba independiente.

### 21.6 Multiplicidad, selección y análisis

Preespecificar hipótesis primaria, estimando, resultado primario, momentos, subgrupos y análisis. Controlar o declarar multiplicidad cuando se prueben numerosos resultados, horizontes, políticas, escalas o subgrupos. Distinguir análisis confirmatorios de exploratorios. No seleccionar la regla de Value, el horizonte, el modelo o la subpoblación por producir el resultado más favorable.

Conservar protocolo fechado/versionado, plan analítico, desviaciones, datos derivados autorizados, código, resultados completos, intervalos, diagnósticos y análisis de sensibilidad. Publicar/reportar resultados nulos, negativos, adversos y no identificados con el mismo rigor que los positivos.

### 21.7 Criterios de detención y suficiencia

Antes de ejecutar, definir qué precisión se necesita para discriminar δ y ε, tamaño muestral/potencia o precisión objetivo, pérdidas esperadas, reglas de parada y tratamiento de análisis intermedios. No detener por significación favorable ni prolongar selectivamente un estudio hasta obtenerla. Si la precisión prevista no permite distinguir efecto relevante de equivalencia, el diseño no es una prueba concluyente de ausencia.

### 21.8 Registro de resultados y lenguaje permitido

Clasificar cada resultado como:
- contribución positiva relevante identificada;
- equivalencia práctica con cero identificada;
- efecto adverso relevante identificado;
- efecto de intervención/paquete identificado pero atribución a accesibilidad no identificada;
- mecanismo parcial/no confirmado;
- resultado impreciso;
- no identificación;
- fallo de implementación/manipulación;
- medición insuficiente/no comparable.

El informe debe indicar estimando, población, política, régimen, regla de Value, horizonte, δ/ε, incertidumbre, supuestos, sensibilidad y alcance. No resumir categorías distintas como «C10 confirmada» o «C10 refutada» sin especificar qué versión y ámbito se evaluaron.

Este addendum no selecciona caso, no fija valores numéricos de δ/ε, no autoriza adquisición/procesamiento de datos ni ejecución experimental. No modifica Core, RMA, Matrix, STATUS, claims, cierres C09 o VSL-KGFS-02, ni reanuda el predictor. El PR permanece draft, pendiente de revisión.


---

## 22. Addendum metodológico — arquitectura de diseños experimentales para C10-D1 (01-11-2026)

**Estado:** propuesta de diseño pendiente de revisión; no es protocolo de ejecución ni preregistro. No selecciona un caso ni autoriza intervención, adquisición o procesamiento de datos.

### 22.1 Principio de diseño

No se aleatoriza T_acc como variable abstracta. Se asignan intervenciones/componentes implementables que pretenden modificar condiciones o accesibilidad; posteriormente se verifica de forma independiente si cambiaron T_acc. Distinguir siempre:
- efecto por intención de tratar de cada componente asignado;
- efecto de la intervención/paquete sobre Value;
- efecto causal atribuible a la política de accesibilidad;
- efecto sobre T_acc, Reach, Trayectoria y Outcome como resultados mecanísticos separados.

La asignación aleatoria de un componente que pretende cambiar accesibilidad no demuestra que su efecto sobre Value esté mediado exclusivamente por ΔT_acc. Deben diseñarse y evaluar vías alternativas.

### 22.2 Factorial de componentes

Sean B_A una intervención concreta diseñada para modificar accesibilidad y B_L una intervención sobre condiciones habilitadoras. Si las combinaciones son factibles, un diseño factorial 2×2 puede asignar (B_L,B_A)=(0,0),(0,1),(1,0),(1,1). Permite estimar efectos de asignación de cada componente y su interacción en la escala preespecificada de Value.

El contraste de interacción aditiva entre componentes asignados puede expresarse como:
I_B = [E(V|B_L=1,B_A=1)-E(V|B_L=1,B_A=0)] - [E(V|B_L=0,B_A=1)-E(V|B_L=0,B_A=0)].
Con asignación aleatoria, adherencia/consistencia y diseño adecuados, este contraste identifica interacción de los componentes asignados en esa escala; no es automáticamente interacción causal entre L y T_acc ni identifica θ_A.

La factibilidad de las cuatro celdas es una condición sustantiva. Si B_A=1 requiere necesariamente B_L=1, la celda (0,1) no existe o no representa una intervención coherente. No extrapolar a combinaciones imposibles ni imputar contrafactuales fuera del soporte. Usar un factorial restringido, diseño secuencial o contraste conjunto factible y limitar la interpretación.

### 22.3 Variación experimental específica de accesibilidad

La opción más informativa para C10 sería una intervención implementable que cambie el conjunto de transformaciones realizables, con medición independiente de T_acc antes de Outcome/Value y sin modificar directamente otras vías relevantes, o con esas vías separadas por diseño.

La exclusión de vías directas no se presume por denominar la intervención «de accesibilidad». Una nueva herramienta, permiso, recurso, información o incentivo puede modificar simultáneamente costes, preferencias, capacidades, ejecución y Value. Inventariar las vías alternativas y justificar cuáles se mantienen constantes, se miden o se identifican.

Si solo se aleatoriza un estímulo/encouragement para cambiar T_acc, el efecto de asignación es ITT del estímulo. Interpretarlo como efecto de accesibilidad requeriría supuestos adicionales (por ejemplo, exclusión y, para IV, relevancia, independencia y condiciones propias del estimando); no asumirlos por la aleatorización.

### 22.4 Diseño secuencial y políticas dinámicas

Cuando las condiciones habilitadoras y accesibilidad evolucionan o dependen de la historia, considerar asignación secuencial:
1. medir historia basal y condiciones;
2. asignar intervención habilitadora factible;
3. medir de forma independiente T_acc y condiciones posteriores;
4. asignar, entre opciones factibles, intervención/política de accesibilidad;
5. volver a medir estado, T_acc, mecanismos, Reach y Trayectoria;
6. medir Outcome y Value en el horizonte predefinido;
7. repetir decisiones si el sistema y la política lo requieren.

Diseños secuenciales aleatorizados (incluidos factoriales secuenciales o diseños adaptativos cuando proceda) pueden identificar efectos de asignación de estrategias dinámicas bajo sus probabilidades de asignación y supuestos. Para efectos de políticas dinámicas observadas/estimadas, aplicar métodos g longitudinales solo si la historia relevante, intercambiabilidad secuencial, positividad, consistencia, interferencia y censura están justificadas. La aleatorización inicial no resuelve la confusión de decisiones posteriores no aleatorizadas.

### 22.5 Diseños por componentes y mecanismos

Cuando el paquete contenga componentes separables, utilizar diseños de desmantelamiento, factoriales parciales o variación por componentes si cada intervención es realizable y su asignación permite contrastes interpretables. No dividir artificialmente un mecanismo indivisible. Los efectos de componentes no equivalen automáticamente a mediación por T_acc; medir cambios de accesibilidad y mecanismos por separado.

### 22.6 Jerarquía de diseños y alcance de inferencia

- Intervención compuesta aleatorizada: identifica efecto de asignación del paquete sobre Value, no atribución específica a accesibilidad.
- Factorial aleatorizado factible: identifica efectos e interacciones de componentes asignados en la escala y población estudiadas; no necesariamente θ_A.
- Intervención/variación de accesibilidad estrechamente definida, con vías alternativas controladas o identificadas: puede acercarse a θ_A; requiere supuestos de mediación/identificación defendibles.
- Diseño secuencial aleatorizado: identifica efectos de estrategias dinámicas asignadas; atribución a accesibilidad requiere separar componentes y verificar T_acc.
- Cuasiexperimental/observacional: solo permite atribución si su contrafactual y supuestos específicos son defendibles; incluir sensibilidad y falsaciones.

### 22.7 Puertas de diseño antes de elegir un caso

Un candidato no pasa a diseño experimental hasta documentar:
1. intervención y componentes implementables, con versiones precisas;
2. mapa de vías causales alternativas y condiciones constitutivas de accesibilidad;
3. combinaciones posibles/imposibles y soporte;
4. asignación/unidad experimental, contaminación e interferencia;
5. medición independiente y temporal de T_acc, Reach, Trayectoria, Outcome y Value;
6. estimando primario (ITT, θ_A(q), θ_A^dyn o efecto conjunto) y contraste correspondiente;
7. supuestos de identificación, plan analítico, potencia/precisión, δ/ε y reglas de parada;
8. riesgos éticos, operativos, de equidad y de daño por resultados adversos.

Si solo se puede identificar el efecto del paquete o el efecto conjunto, el caso puede ser útil para otra pregunta, pero no se presentará como prueba de atribución específica C10. Si las combinaciones necesarias no son factibles, redefinir el estimando/diseño antes de recoger datos, no después de ver resultados.

Este addendum no designa un caso, no reabre KGFS ni otros casos previamente delimitados, no autoriza datos o ejecución y no modifica Core, RMA, Matrix, STATUS, claims ni el estado de C09/VSL-KGFS-02. El PR permanece draft, pendiente de revisión.


---

## 23. Addendum metodológico — puerta de selección y clasificación de casos C10-D1 (01-11-2026)

**Estado:** marco de cribado propuesto, pendiente de revisión. No selecciona ni designa un caso empírico. No autoriza adquisición/procesamiento de datos ni ejecución.

### 23.1 Principio de selección

Seleccionar casos por su capacidad de identificar la contribución causal de una política de accesibilidad a Value, no por volumen de datos, notoriedad del programa, disponibilidad de outcomes o probabilidad de encontrar un resultado favorable.

Las puertas excluyentes no se compensan mediante una puntuación agregada. Un buen registro de Value no compensa ausencia de medición independiente de T_acc; una asignación aleatoria no compensa que solo se identifique el efecto de un paquete inseparable.

### 23.2 Puertas excluyentes

**G1 — Medición independiente de accesibilidad.** ¿Puede reconstruirse T_acc en momentos pertinentes, con transformaciones identificables, condiciones/precondiciones, evidencia de realizabilidad y clasificación independiente de Outcome/Value? Si solo hay acciones adoptadas, capacidades declaradas, transiciones observadas o outcomes, no supera la puerta.

**G2 — Variación causal defendible.** ¿Existe una intervención/política o fuente de variación con contraste y contrafactual defendibles que pueda modificar accesibilidad? Si solo hay correlación o cambio descriptivo, no es candidato probatorio.

**G3 — Separación de condiciones y vías alternativas.** ¿Pueden distinguirse las condiciones constitutivas de realizabilidad, otras condiciones habilitadoras/confusoras y las vías directas/alternativas hacia Value? Si solo se identifica un paquete inseparable, puede estudiarse su efecto total/conjunto, pero no atribuirlo específicamente a T_acc.

**G4 — Mecanismos y dinámica TGCV.** ¿Pueden derivarse Reach y Trayectoria desde transformaciones accesibles y sus dependencias, con actualización dinámica y temporalidad coherente? Una secuencia de estados observados no sustituye por sí sola una trayectoria TGCV.

**G5 — Medición independiente de Value.** ¿Existe una regla de Value explícita, con entidad/beneficiario, objetivo, dirección, costes, beneficios, compensaciones, horizonte e incertidumbre, separada de Outcome? Si Value se infiere retrospectivamente de los resultados, no supera la puerta.

**G6 — Contrafactual y estimando identificables.** ¿El diseño permite estimar el contraste pertinente (θ_A(q), θ_A^dyn o, si procede, solo TE/θ_LA), con supuestos, positividad, consistencia, interferencia y confusión tratados explícitamente? Identificar TE o el efecto del paquete no satisface por sí solo la atribución C10.

**G7 — Precisión, viabilidad y ética.** ¿Puede alcanzarse precisión para discriminar efecto relevante, equivalencia práctica y efecto adverso, con δ/ε justificados y reglas de parada? ¿Es viable y ético asignar la intervención, medir resultados y gestionar daños, equidad, contaminación y pérdidas? Si no, no se presenta como prueba concluyente.

### 23.3 Resultado del cribado

Para cada puerta registrar uno de estos estados:
- **Superada:** evidencia y justificación suficientes, con fuente/procedencia.
- **Condicional:** existe una ruta concreta, verificable y factible para resolver la carencia antes de diseñar/ejecutar.
- **No superada:** la carencia impide la inferencia probatoria o no existe ruta defendible conocida.
- **No evaluada:** información insuficiente para juzgarla.

No confundir «no evaluada» con «superada». Una puerta condicional debe incluir tarea, evidencia requerida, responsable, coste/viabilidad y criterio de cierre. No se avanza a diseño probatorio mientras una puerta esencial siga no superada o no evaluada.

### 23.4 Clasificación de utilidad científica

Mantener tres tipos, sin confundir utilidad metodológica con evidencia causal:
- **Tipo I — metodológico:** útil para desarrollar/probar mediciones, procedimientos, mecanismos o métodos; no acredita por ello la atribución C10.
- **Tipo II — candidato a identificación:** tiene potencial probatorio, pero una o más puertas están condicionales; requiere resolverlas antes de designarlo probatorio.
- **Tipo III — probatorio:** supera las puertas y permite formular un diseño cuyo estimando primario identifica específicamente la contribución de accesibilidad a Value.

El paso de Tipo II a Tipo III exige evidencia nueva y cierre documentado de las puertas, no solo más documentación ni una valoración subjetiva de potencial. La clasificación no es una puntuación ni un ranking de atractivo.

### 23.5 Hoja de evaluación por caso

La ficha de cribado debe conservar:
- identidad, sistema, población/unidad, periodo y contexto;
- pregunta causal y estimando que se pretende identificar;
- política/intervención y versiones;
- estado G1–G7, evidencia que lo sustenta y carencias;
- condiciones constitutivas de T_acc y otras condiciones habilitadoras;
- mapa de vías alternativas y contrafactual;
- medición de Reach/Trayectoria, Outcome y Value;
- soporte/positividad, interferencia, pérdidas y precisión;
- riesgos éticos/operativos;
- tipo I/II/III y justificación;
- tareas necesarias para avanzar, límites y decisión de no avanzar cuando corresponda.

La evaluación inicial puede realizarse con documentación ya disponible y sin descargar ni procesar datos. Toda adquisición, acceso, vinculación o procesamiento adicional requiere autorización y revisión previa conforme a la gobernanza del repositorio.

### 23.6 Aplicación a casos ya examinados

Esta puerta no cambia clasificaciones históricas ni reabre casos cerrados. KGFS permanece como Tipo I metodológico en el estado documentado; no se eleva a Tipo III ni se utiliza como evidencia de ΔT_acc→ΔV. México C10C-002 y Marruecos C10C-004 conservan sus límites documentados. VSL-KGFS-02 permanece cerrado como COMPATIBILITY_NOT_ESTABLISHED. Cualquier reevaluación futura requiere una decisión explícita y evidencia nueva.

### 23.7 Regla de decisión

- Tipo I: conservar como referencia metodológica, sin claim causal C10.
- Tipo II: especificar una única ruta de resolución de carencias y reevaluar; no iniciar diseño probatorio mientras persistan puertas esenciales abiertas.
- Tipo III: preparar un protocolo de diseño específico, preregistro y evaluación ética; la clasificación Tipo III no autoriza por sí sola ejecución ni adquisición de datos.

Este addendum no selecciona un caso, no autoriza datos o experimentos, y no modifica Core, RMA, Matrix, STATUS, claims, C09 o VSL-KGFS-02. El PR permanece draft y pendiente de revisión.


---

## 24. Addendum de auditoría — reconciliación de notación, precedencia y flujo metodológico (01-11-2026)

**Estado:** corrección de coherencia interna del borrador; pendiente de revisión científica. No añade evidencia, no aprueba el protocolo y no modifica Core, RMA, Matrix, STATUS ni claims.

### 24.1 Precedencia normativa interna

Para evitar que formulaciones provisionales antiguas se utilicen como especificaciones vigentes, aplicar esta precedencia:
1. El apartado 17 prevalece sobre las formulaciones iniciales de los apartados 3, 5, 6, 7, 8, 9 y 16 cuando precisa condiciones constitutivas, factibilidad, temporalidad, políticas y estimandos.
2. Los apartados 18–21 precisan medición, fiabilidad, transportabilidad y falsabilidad; no sustituyen la definición causal de 17.
3. El apartado 22 precisa la arquitectura de diseños y prevalece sobre la jerarquía genérica inicial del apartado 8 cuando se elija un diseño concreto.
4. El apartado 23 precisa la elegibilidad y clasificación de casos y prevalece sobre la ficha abreviada de selección del apartado 11.
5. El apartado 24 aclara la notación y el orden de uso; no crea estimandos ni cambia decisiones científicas.

Las secciones iniciales conservan el contexto histórico y conceptual, pero no deben leerse como especificaciones independientes cuando exista una precisión posterior.

### 24.2 Notación causal vigente para accesibilidad

La fórmula inicial de 5.2, escrita como distribuciones G₁/G₀ condicionadas únicamente por L, es una abreviatura histórica y no una especificación suficiente para análisis. La formulación de trabajo vigente es la de 17.7:

(θ_A(q)=E[V^{q,g_1}]-E[V^{q,g_0}]).

Aquí:
- q define un régimen común, explícito y factible de condiciones/historias, condicionado por covariables basales cuando corresponda;
- g₁ y g₀ son políticas estocásticas implementables sobre cambios de accesibilidad, condicionadas por covariables basales e historia pertinente;
- las políticas respetan el conjunto de configuraciones de accesibilidad factibles bajo cada historia;
- las condiciones constitutivas de accesibilidad (L_c) no se fijan artificialmente en valores incompatibles con la transformación;
- otras variables temporales (L_m) se clasifican por su papel causal en cada momento, no por una etiqueta permanente;
- los mecanismos posteriores y Value evolucionan bajo cada política.

No sustituir g₁/g₀ por distribuciones observadas P(A|Z,L) sin una estrategia causal que justifique esa operación. No interpretar θ_A(q) como efecto indirecto natural ni como fracción de TE. Si las políticas no comparten soporte factible, el contraste específico no está identificado para esa población/régimen; considerar un contraste conjunto factible y limitar la atribución.

En consecuencia, donde las fases 0, 3 y 4 de la sección 9 mencionen q(L) y G₁/G₀, deben entenderse como referencias abreviadas a la especificación completa de 17.7 y este apartado. La ficha de preregistro deberá recoger la versión completa.

### 24.3 Estado de θ_A^dyn

La notación θ_A^dyn utilizada en los apartados 19, 21, 22 y 23 es por ahora **un marcador de estimando longitudinal pendiente de formalización**, no un estimando ya definido ni disponible para estimación.

Antes de utilizarlo se deberá especificar, como mínimo:
- población y tiempo inicial;
- historia longitudinal h_t y variables observadas antes de cada decisión;
- políticas dinámicas comparadas y sus versiones;
- conjunto factible de acciones/configuraciones de accesibilidad en cada historia;
- régimen de condiciones y tratamiento de variables afectadas por decisiones previas;
- resultado potencial de Value, regla evaluativa y horizonte;
- contraste contrafactual y estrategia de identificación;
- supuestos de consistencia, intercambiabilidad secuencial, positividad, interferencia, censura y medición.

Hasta completar esta definición, usar θ_A(q) para el contraste estocástico bajo régimen común cuando sea defendible, o describir el efecto de asignación de la estrategia dinámica sin llamarlo efecto causal específico de accesibilidad. La mera existencia de una política π:h_t→Z_t no define por sí sola θ_A^dyn.

### 24.4 DAG y mecanismo de asignación

La expresión de la sección 3 que incluye X→Z debe interpretarse según el diseño, no como una flecha universal:
- **Ensayo aleatorizado:** Z se asigna por el mecanismo aleatorio especificado; no dibujar X→Z como relación causal. X puede ser usado para estratificación/ajuste de precisión, sin que ello convierta la asignación en confusa.
- **Diseño observacional/cuasi-experimental:** representar X→Z cuando las covariables basales influyen en la asignación/exposición, además de las demás relaciones justificadas.
- **Diseño por conglomerados, secuencial o adaptativo:** representar unidad, calendario y probabilidades de asignación en cada momento, incluyendo la historia que gobierna las decisiones.

El DAG debe reflejar el mecanismo real de asignación y la temporalidad del caso; el DAG inicial es solo un esquema general de posibles vías y no sustituye el DAG específico preregistrado.

### 24.5 Relación entre fases de investigación y puertas de elegibilidad

Mantener dos instrumentos distintos y conectados:
- **Fases 0–6 de la sección 9:** orden del trabajo de investigación desde delimitación/preregistro hasta síntesis científica.
- **Puertas G1–G7 de la sección 23:** cribado de la capacidad probatoria de un caso antes de diseñar o ejecutar un estudio.

La clasificación de cada G1–G7 (superada, condicional, no superada, no evaluada) informa la Fase 1 y determina si el caso puede avanzar. Las puertas de diseño del apartado 22 se aplican después de la elegibilidad y antes de diseñar/ejecutar. Superar G1–G7 no sustituye la auditoría de identificación ni autoriza ejecución. Una puerta condicional requiere evidencia de cierre antes de tratar el caso como Tipo III.

### 24.6 Catálogo de selección y diseños: versión vigente

La tabla C1–C7 del apartado 11 es una ficha histórica abreviada. Para el cribado vigente usar G1–G7 del apartado 23, que incorporan explícitamente mecanismos TGCV, medición independiente de Value, precisión, viabilidad y ética.

La jerarquía inicial del apartado 8 es orientativa. Para especificar un diseño utilizar el apartado 22, distinguiendo ITT de componentes, factorial factible, variación específica de accesibilidad, política secuencial y efecto conjunto. Ninguno de esos diseños identifica automáticamente θ_A(q); debe demostrarse para el diseño concreto.

### 24.7 Resultado de la auditoría de coherencia

La auditoría identifica:
- **Resuelto por precedencia/aclaración:** formulación inicial de θ_A frente a la precisión del apartado 17; relación entre fases y puertas; jerarquía de selección y diseños.
- **Pendiente de formalización antes de uso:** θ_A^dyn.
- **Requiere adaptación por estudio, no una fórmula universal:** DAG, clasificación de L_c/L_m, q y políticas g, soporte y versiones de intervención.
- **No autorizado por esta auditoría:** selección de caso, descarga/procesamiento de datos, preregistro o ejecución.

El protocolo puede continuar como marco metodológico de trabajo, pero no debe considerarse todavía listo para preregistro ni para ejecución. El siguiente paso es completar la especificación formal de los estimandos longitudinales solo si el diseño candidato realmente los necesita; no añadir complejidad dinámica por defecto. Después deberá realizarse una revisión final de ecuaciones, variables, referencias cruzadas y consistencia de las puertas.

Este addendum no altera clasificaciones previas de casos, C09, VSL-KGFS-02 ni ningún claim. El PR permanece draft y pendiente de revisión.


## 25. Auditoría global de consistencia y reglas de interpretación

### 25.1 Resultado de la auditoría

La revisión conjunta de los bloques metodológicos desarrollados después del apartado 24 no identifica una contradicción que invalide la arquitectura general de C10-D1. Sí identifica ambigüedades de notación y alcance que deben resolverse antes de seleccionar un caso, preregistrar o ejecutar un estudio.

Este apartado establece reglas de lectura y precedencia para evitar que propuestas metodológicas condicionales se interpreten como decisiones científicas aprobadas. No reemplaza la especificación particular del DAG, las intervenciones, los estimandos ni el plan de análisis de un estudio.

### 25.2 Variables y temporalidad: separar generación de accesibilidad y condiciones

Para describir un diseño, distinguir explícitamente:

- **X:** covariables basales y contexto previo a la intervención.
- **B_t:** componentes manipulables o asignables en el momento t, cuya intervención puede modificar el sistema.
- **C_{c,t}:** condiciones constitutivas o habilitadoras necesarias para que determinadas transformaciones sean realizables en t.
- **L_t:** otras condiciones que varían en el tiempo. Su papel debe clasificarse según la historia causal concreta: pueden ser confusoras, mediadoras, consecuencias de intervenciones previas o condiciones habilitadoras de transformaciones futuras.
- **A_t:** cambio de accesibilidad reconstruido como diferencia entre espacios de transformaciones accesibles pertinentes en t; no es una asignación abstracta independiente de las condiciones que lo hacen posible.
- **M_t:** mecanismos posteriores, incluidos Reach y Trayectoria derivados del espacio transformacional.
- **O:** outcomes observables.
- **V:** Value, construido mediante una regla evaluativa independiente.

La expresión T_acc=F(S,C,L) recuerda que la accesibilidad depende del estado y de condiciones del sistema; no implica que C y L sean variables homogéneas ni que deban mantenerse todas constantes. Una condición puede ser constitutiva en un momento y convertirse en variable temporal que afecta accesibilidad futura en otro. Clasificar por función causal y temporal, no por etiqueta permanente.

No incluir indiscriminadamente todas las variables L en q. El régimen q solo puede especificar condiciones/historias no constitutivas que sea coherente intervenir o estandarizar para la pregunta causal. Las condiciones constitutivas deben conservar configuraciones compatibles con las transformaciones comparadas. Cuando una condición y la accesibilidad solo puedan cambiar conjuntamente, el contraste identificable puede ser conjunto y no específico de A.

### 25.3 Interpretación operativa de θ_A(q)

La formulación de trabajo θ_A(q)=E[V^{q,g_1}]-E[V^{q,g_0}] representa un contraste entre dos políticas factibles sobre cambios de accesibilidad bajo un régimen común q de condiciones/historias admisibles.

V^{q,g} debe entenderse como Value bajo un régimen conjunto y coherente: q no fija condiciones constitutivas en valores incompatibles y g no asigna A fuera del conjunto factible dado el estado y la historia. Las políticas g_1 y g_0 deben especificar cómo se generan cambios de accesibilidad mediante configuraciones/intervenciones realizables; no son una intervención metafísica sobre un índice ni se identifican automáticamente con P(A|Z,L).

Bajo cada política, Reach, Trayectoria, Outcome y Value posteriores evolucionan como consecuencias del régimen. No ajustar mecánicamente por M_t u O cuando son mecanismos posteriores que forman parte de la vía cuyo efecto se pretende incluir. Si se condiciona o interviene sobre ellos, se habrá definido otro estimando y deberá explicitarse.

Este contraste es específico de las políticas, población, horizonte y régimen q definidos. No representa una contribución universal de toda variación de T_acc. Si los componentes B que generan A también afectan Value por vías alternativas, la atribución específica exige separar o identificar esas vías; si no es posible, informar el efecto de la intervención/paquete o el efecto conjunto, no atribuirlo exclusivamente a accesibilidad.

### 25.4 Contraste conjunto, interacción y factibilidad

θ_{L,A}=E[V^{q_1,g_1}]-E[V^{q_0,g_0}] solo debe interpretarse cuando (q_1,g_1) y (q_0,g_0) definen regímenes conjuntos bien especificados, consistentes y factibles. Es un contraste entre políticas conjuntas de condiciones y accesibilidad; no es por sí mismo el efecto de A ni una descomposición del efecto total.

Una interacción aditiva entre políticas puede definirse mediante las cuatro medias contrafactuales correspondientes a (q_0,g_0), (q_0,g_1), (q_1,g_0) y (q_1,g_1). Solo está definida e identificable si las cuatro combinaciones tienen significado causal, son realizables y cuentan con soporte suficiente en la población objetivo. Su interpretación es interacción en la escala aditiva entre los regímenes comparados; no debe describirse automáticamente como interacción ontológica entre L y T_acc. Si alguna celda es imposible o incoherente, no calcularla por extrapolación ni interpretar la interacción.

### 25.5 Efecto total, residual y descomposición

TE es el efecto de la intervención Z especificada sobre Value. No equivale a θ_A(q), y la aleatorización de Z no aleatoriza automáticamente A.

La resta TE−θ_A(q) no es, en general, un efecto directo ni el efecto de todas las vías distintas de accesibilidad. Solo tiene interpretación como componente de una descomposición si ambos contrastes pertenecen a una arquitectura contrafactual compatible, con misma población, escala, horizonte y escenarios de referencia. Una descomposición secuencial puede depender del orden cuando hay interacción y requiere que los escenarios intermedios sean factibles. Las vías de Z que no estén representadas por los regímenes q y g impiden interpretar esa descomposición como partición completa de TE.

No presentar porcentajes de mediación o atribución cuando los estimandos no sean componentes complementarios, el efecto total esté cerca de cero, haya signos opuestos o la incertidumbre impida una interpretación estable.

### 25.6 Diseños de intervención: qué identifica cada uno

La intervención experimental debe asignarse a componentes B implementables, no a T_acc como variable abstracta. El factorial de componentes es una opción de diseño, no un requisito universal; solo procede si sus combinaciones son factibles y coherentes.

La aleatorización de B identifica, bajo los supuestos del diseño, efectos de asignación de esos componentes (por ejemplo, ITT) y sus interacciones en la escala definida. No identifica automáticamente el efecto mediado por A. Una intervención que cambia accesibilidad puede modificar también condiciones, preferencias, costes, capacidades u otras vías relevantes para Value.

La variación experimental de componentes combinada con una estrategia mediacional o políticas factibles sobre accesibilidad es una familia de estrategias prometedora, no un método universal ni garantía de identificación. La variación secuencial/aleatorización repetida puede ayudar cuando las decisiones y confusores evolucionan en el tiempo, pero requiere su propio protocolo. IV solo es defendible cuando relevancia, independencia, exclusión y demás supuestos del estimando elegido son plausibles y justificables; no presumir exclusión por la etiqueta de la intervención.

Si no puede separarse el cambio de accesibilidad de condiciones que también afectan Value, el resultado válido puede ser una contribución conjunta o un efecto de paquete. Debe conservarse esa limitación, no resolverla por definición.

### 25.7 Medición, identificación y sensibilidad son puertas distintas

La medición independiente de T_acc, Reach, Trayectoria, Outcome y Value es necesaria para evitar circularidad y confusión de constructos, pero no basta para identificación causal. Deben auditarse por separado:

1. validez y fiabilidad de cada constructo y de sus unidades;
2. temporalidad y reconstrucción del espacio de transformaciones;
3. consistencia de versiones de intervención y políticas;
4. confusión basal y post-intervención, incluida la afectada por decisiones previas;
5. positividad y soporte de las políticas comparadas;
6. interferencia, censura y datos faltantes cuando proceda;
7. vías alternativas y supuestos de identificación;
8. sensibilidad a confusión no medida, error de medición de T_acc y definición de Value.

Cuando sea viable, quienes reconstruyan T_acc deben desconocer Outcome y Value; la regla de Value debe especificar beneficiario, objetivo, dirección, horizonte, costes, beneficios y compensaciones sin derivarse de T_acc ni del outcome usado como mediador.

El efecto mínimo relevante δ y el margen de equivalencia ε deben fijarse antes del análisis. Un intervalo amplio que incluye cero y efectos relevantes indica incertidumbre, no ausencia de efecto. Solo un intervalo suficientemente preciso dentro del margen predefinido respalda ausencia de efecto relevante en el ámbito estudiado. Los controles negativos y análisis de sensibilidad deben preespecificarse cuando sea posible; no usarlos para seleccionar retrospectivamente especificaciones favorables.

### 25.8 Alcance longitudinal y heterogeneidad

La notación θ_A^dyn sigue siendo un marcador pendiente de formalización. No introducir θ_dyn ni otra variante como estimando disponible sin especificar historia h_t, secuencia temporal, políticas dinámicas factibles, conjunto de acciones admisibles, régimen de condiciones, resultado potencial de Value, horizonte, población, contraste y supuestos de identificación. No sumar contrastes estáticos para simular una estimación longitudinal.

La heterogeneidad puede depender de la composición de T_acc, relaciones y dependencias, condiciones del sistema, estado inicial, horizonte y regla de Value. Los modificadores relevantes deben preespecificarse. Los niveles de evidencia se mantienen: A, existencia local; B, contribución condicional bajo condiciones delimitadas (objetivo principal); C, generalización/transportabilidad. Un resultado local no implica universalidad, monotonicidad ni que toda expansión de accesibilidad aumente Value.

### 25.9 Estado de decisión

La auditoría global permite conservar los trece bloques como desarrollo metodológico condicionado, con las reglas de interpretación anteriores. No convierte los diseños, políticas, estimandos dinámicos ni estrategias de identificación en decisiones aprobadas. No selecciona un caso Tipo III, no identifica un régimen q universal, no valida empíricamente los constructos y no demuestra ni refuta C10.

Antes de preregistro o ejecución siguen siendo necesarias la selección justificada del caso, la especificación de su DAG temporal, la definición de intervenciones y versiones factibles, la elección del estimando compatible con ese diseño, el plan de medición independiente y la auditoría de identificación/precisión. Este apartado no autoriza descarga o procesamiento de datos ni ejecución experimental.



## 26. Precisión de la notación de intervención sobre accesibilidad

### 26.1 Lectura de do(A~G) y relación con componentes implementables

Las expresiones de las secciones 5.2 y 17.7 que utilizan do(A~G_j) son notación abreviada para un régimen estocástico sobre cambios de accesibilidad, no una afirmación de que A pueda asignarse directamente con independencia de la estructura generativa del sistema.

Para cualquier aplicación concreta, especificar una intervención o política implementable sobre componentes manipulables B (o una secuencia de ellos) y la distribución de cambios A que esa intervención induce bajo cada historia/contexto. La política g_j debe corresponder a esa distribución inducida, respetar el conjunto de configuraciones factibles y conservar la dependencia de A respecto del estado y de las condiciones constitutivas. No basta con definir una distribución matemática sobre valores de A si no existe una intervención realizable que la genere o una estrategia de identificación defendible para el contraste estocástico.

La notación V^{q,g_j} representa Value bajo el régimen conjunto coherente formado por q y la política de accesibilidad g_j, incluyendo la respuesta posterior de mecanismos, outcomes y Value. Cuando g_j se implementa mediante componentes B, documentar la correspondencia B→A y las versiones de intervención. Si B tiene vías directas o alternativas hacia Value que no pueden separarse o identificarse, el contraste no permite atribución específica a A: informar el efecto de B/paquete o un efecto conjunto, según el diseño.

### 26.2 Condición para interpretar θ_A(q)

Interpretar θ_A(q) como contribución causal específica de accesibilidad solo cuando se sostengan conjuntamente:
- una definición operacional de las políticas g_1 y g_0 y de las intervenciones realizables que las inducen;
- compatibilidad de cada política con estado, condiciones constitutivas e historia;
- soporte suficiente para la comparación en la población objetivo;
- consistencia y equivalencia defendible de versiones;
- identificación de confusión relevante entre cambios de accesibilidad y Value, incluida la confusión afectada por intervenciones previas;
- separación o identificación de vías alternativas desde los componentes B hacia Value.

Si alguna condición falla, no reinterpretar el efecto de asignación de B como θ_A(q). Puede seguir siendo válido estimar el ITT de B, el efecto de un paquete o un contraste conjunto, etiquetándolo correctamente. La insuficiencia de identificación no constituye por sí misma evidencia a favor ni en contra de C10.

### 26.3 Auditoría de ecuaciones: estado

Las expresiones TE=E[V(1)-V(0)], θ_A(q), θ_{L,A}, la interacción aditiva entre regímenes y las descomposiciones secuenciales se conservan como notación de trabajo, sujetas a las poblaciones, escalas, horizontes, políticas y condiciones de factibilidad definidas en este protocolo. V(1)-V(0) es una abreviatura para los valores potenciales bajo los dos niveles de la intervención Z especificada; no presupone que toda intervención tenga necesariamente dos niveles.

La interacción I_{A,L} del apartado 17.3 y las interacciones descritas en los apartados 25.4 y 22.2 se refieren a contrastes distintos: la primera compara políticas de accesibilidad bajo regímenes de condiciones; la segunda, cuando se utiliza, compara componentes asignados en un diseño factorial. No intercambiar sus interpretaciones ni tratarlas como una misma interacción.

La auditoría no convierte estas ecuaciones en estimandos identificados para un caso concreto. La selección de la parametrización final y del estimando primario queda condicionada al diseño, a la factibilidad de las intervenciones y a la estrategia de identificación que pueda defenderse.


## 27. Especificación operacional de ΔT_acc, Reach y Trayectoria

### 27.1 Representación estructurada y comparación de T_acc

Para la medición de C10, T_acc debe tratarse como un conjunto estructurado de transformaciones accesibles bajo un estado, condiciones, recursos, dependencias y restricciones especificados. Cuando sea útil para el caso, puede representarse analíticamente como T_acc,t=(U_acc,t,R_acc,t,C_acc,t): unidades/transformaciones accesibles, relaciones/dependencias y configuraciones admisibles. Esta representación es instrumental para medir composición y estructura; no modifica el Core ni establece una nueva ontología canónica.

La comparación entre momentos requiere un universo candidato común, reglas preespecificadas de identidad y equivalencia (≡T), granularidad estable y evidencia referida al momento correcto. La unidad candidata τ=(S_o,S_d,M,P_τ,K,E) debe permitir reconocer origen, destino, mecanismo, admisibilidad, condiciones/dependencias/recursos y evidencia de realizabilidad.

Con esa correspondencia, distinguir:
- **A⁺:** transformaciones que pasan a estar respaldadas como accesibles en t1 y no lo estaban en t0;
- **A⁻:** transformaciones respaldadas como accesibles en t0 que dejan de estarlo en t1;
- **A^reconf:** transformaciones emparejadas bajo la regla de identidad/equivalencia cuya accesibilidad se conserva, pero cambia de forma material su mecanismo, precondiciones, recursos, dependencias o restricciones;
- **ΔR:** cambios en relaciones/dependencias entre transformaciones;
- **ΔC:** cambios en configuraciones admisibles y sus restricciones.

La representación ampliada de trabajo es ΔT_acc=(A⁺,A⁻,A^reconf,ΔR,ΔC), cuando las dimensiones relacionales y configuracionales sean pertinentes y medibles. Es una ficha de comparación analítica, no una nueva definición del Core. Si una modificación cambia la identidad de la transformación según ≡T, no registrarla como mera reconfiguración: clasificarla como pérdida y alta correspondientes. Evitar doble conteo entre A^reconf, ΔR y ΔC, y documentar qué cambios son atributos de una transformación y cuáles afectan a la estructura del conjunto.

Las diferencias epistemológicas —nueva evidencia, mayor cobertura, cambio de evaluador o revisión de clasificación— deben mantenerse separadas de esos cambios estimados del sistema. Una transformación recién descubierta no es necesariamente una transformación recién accesible.

### 27.2 Trayectorias factibles y trayectorias realizadas

La palabra Trayectoria debe desambiguarse en dos objetos relacionados pero distintos:

1. **Trayectoria factible/candidata:** secuencia ordenada de transformaciones TGCV que podría realizarse desde una configuración inicial, si en cada paso se satisfacen las condiciones, precondiciones, recursos, dependencias y reglas de admisibilidad. Es un objeto del espacio de posibilidades, no evidencia de ejecución.
2. **Trayectoria realizada:** secuencia de transformaciones que efectivamente se ejecutó, reconstruida con evidencia de ejecución y trazabilidad temporal. Es una realización observada del sistema, no el conjunto de todas sus posibilidades.

Una secuencia de estados observados no basta para identificar ninguna de las dos: debe reconstruirse qué transformación TGCV conecta cada paso, con qué mecanismo y bajo qué condiciones. La trayectoria realizada debe vincularse a las transformaciones correspondientes; no inferir automáticamente que una transición observada prueba que toda transformación equivalente era accesible en otros momentos o contextos.

### 27.3 Composición admisible y actualización dinámica

Sea S_0 la configuración inicial y H un horizonte definido. Una trayectoria factible candidata puede representarse como σ=(τ_0,...,τ_{k-1}), junto con sus configuraciones intermedias. Para cada paso i, τ_i debe pertenecer al espacio accesible T_acc(S_i,C_i,L_i) y satisfacer sus condiciones y dependencias. La ejecución hipotética de τ_i produce una configuración posterior compatible (S_{i+1},C_{i+1},L_{i+1}); por tanto, la accesibilidad se vuelve a evaluar en el siguiente paso. No asumir que T_acc permanece fijo durante la composición.

El conjunto Reach_H(S_0,C_0,L_0) se define, para el estudio, como el conjunto de configuraciones terminales alcanzables desde la configuración inicial mediante al menos una secuencia factible de transformaciones TGCV, de longitud/tiempo dentro del horizonte H y respetando la actualización de estado y condiciones en cada paso. El horizonte, la granularidad temporal, las reglas de composición, las restricciones de recursos y los criterios de equivalencia deben especificarse para cada aplicación. Esta definición es una especificación operacional de trabajo, no una formalización universal ya validada.

Las trayectorias factibles son las secuencias que satisfacen esas reglas; la trayectoria realizada es la secuencia efectivamente seguida. Una transformación puede pertenecer a T_acc sin haber sido ejecutada. Un estado/configuración puede pertenecer a Reach sin haber sido alcanzado en la trayectoria observada. Una trayectoria realizada es una de las posibles realizaciones del sistema, no una medición exhaustiva de Reach.

### 27.4 Consecuencias para la prueba causal C10

La cadena de medición y análisis debe preservar el orden conceptual y temporal:

configuración/condiciones → T_acc,t → trayectorias factibles y Reach_H → selección/ejecución de transformaciones → trayectoria realizada → Outcome → Value.

La cadena no implica que cada eslabón sea determinista ni que todos los efectos estén mediados exclusivamente por el eslabón anterior. Deben medirse por separado las posibilidades, la ejecución, los resultados y la evaluación de valor.

Para estimar la contribución causal de accesibilidad:
- medir T_acc antes de la ejecución y sin inferirlo de la trayectoria realizada, Outcome o Value;
- reconstruir Reach y trayectorias factibles mediante composición TGCV admisible y actualización dinámica;
- registrar por separado qué trayectoria se realizó y qué transformaciones no fueron elegidas o ejecutadas;
- medir Outcome y Value con procedimientos independientes;
- considerar que la ejecución puede modificar estado, condiciones y T_acc futuro, generando confusión temporal y retroalimentación;
- si el diseño no permite separar el cambio de posibilidades del proceso de selección/ejecución, limitar la interpretación al efecto de la política o paquete estudiado.

La medición independiente de estos constructos mejora la validez de la prueba, pero no identifica por sí sola el efecto causal. La identificación sigue sujeta a las condiciones de los apartados 25 y 26.

### 27.5 Estado y límites

Las definiciones de este apartado son especificaciones operacionales propuestas para hacer medibles y comparables los constructos en un estudio C10-D1. No constituyen validación empírica, no convierten la representación T_acc=(U_acc,R_acc,C_acc) en Core, no cierran las decisiones pendientes sobre formalización general de Reach/Trayectoria y no autorizan selección de caso, adquisición de datos, preregistro ni ejecución.



## 28. Procedimiento reproducible de enumeración de trayectorias factibles

### 28.1 Objeto y separación de funciones

Este procedimiento construye, para una configuración inicial y un horizonte definidos, el conjunto de trayectorias TGCV factibles respaldadas por el modelo y la evidencia disponible. No selecciona la trayectoria preferida, no predice cuál se ejecutará y no asigna valor a las trayectorias. Enumerar posibilidades, seleccionar una opción y ejecutar una transformación son operaciones distintas y deben conservar registros separados.

La enumeración se realiza sobre transformaciones TGCV identificadas y sus condiciones de admisibilidad, no sobre una lista de transiciones de estado observadas. La salida primaria es un inventario reproducible de secuencias factibles, sus configuraciones intermedias y su estado de evidencia.

### 28.2 Entradas mínimas

Antes de iniciar, versionar y fijar:
- configuración inicial S_0 y condiciones/recursos relevantes;
- inventario candidato de transformaciones y sus identidades bajo ≡T;
- mecanismo, origen/destino, precondiciones, restricciones, dependencias y evidencia de cada transformación;
- reglas de composición, incompatibilidades y efectos sobre estado/condiciones;
- función o procedimiento para reconstruir T_acc después de cada transformación hipotética;
- horizonte H y su unidad (pasos, tiempo, coste u otra magnitud), así como límites de recursos;
- criterio de equivalencia entre configuraciones y entre trayectorias;
- tratamiento de transformaciones no deterministas, resultados alternativos y admisibilidad indeterminada.

Si falta una entrada esencial, la enumeración se declara parcial o no ejecutable; no se completan silenciosamente las reglas ausentes.

### 28.3 Expansión paso a paso

Para cada nodo de exploración, conservar al menos configuración actual, condiciones y recursos disponibles, T_acc reconstruido para esa configuración, secuencia de transformaciones que conduce al nodo, horizonte consumido y procedencia de las reglas/evidencias aplicadas.

En cada iteración:

1. reconstruir o recuperar T_acc para la configuración actual mediante la regla versionada;
2. identificar las transformaciones candidatas respaldadas como accesibles y comprobar sus precondiciones, dependencias, compatibilidad y recursos;
3. crear una rama por cada transformación admisible que respete el horizonte;
4. aplicar el modelo de respuesta de esa transformación para obtener cada configuración posterior factible; si hay varios resultados estructurales posibles, conservar ramas separadas;
5. actualizar estado, condiciones, recursos y T_acc para cada nueva configuración;
6. registrar la secuencia y continuar hasta alcanzar el horizonte, una condición terminal preespecificada o la ausencia de transformaciones admisibles.

La expansión debe ser determinista respecto de las mismas entradas, versiones, reglas y orden canónico de procesamiento. El orden de enumeración no expresa preferencia ni ranking.

### 28.4 Incertidumbre, ciclos y equivalencias

Las transformaciones con admisibilidad indeterminada no se incorporan al conjunto primario de trayectorias factibles confirmadas. Se registran en una colección separada de ramas condicionales o indeterminadas, indicando qué evidencia o condición permitiría resolverlas. Puede realizarse análisis de sensibilidad incorporándolas bajo supuestos explícitos, sin mezclarlas con el resultado principal.

Los ciclos se permiten cuando sean conceptualmente admisibles, pero la enumeración debe terminar mediante un horizonte finito o reglas de terminación justificadas. Si se utiliza deduplicación de configuraciones, esta no puede eliminar secuencias distintas que difieran en mecanismo, orden, dependencias o consecuencias relevantes. Conservar identificadores de trayectoria y relación con sus nodos/configuraciones; la equivalencia de destinos no implica equivalencia de caminos.

Si el horizonte o el espacio de ramificación no es finito, o se imponen límites computacionales, informar el truncamiento, criterio de parada, cobertura alcanzada y ramas no exploradas. No declarar exhaustividad cuando solo se haya obtenido una enumeración parcial.

### 28.5 Salidas y reproducibilidad

La salida mínima debe contener:
- identificador y versión de configuración inicial, horizonte y reglas;
- inventario de transformaciones candidatas y clasificación de admisibilidad;
- trayectorias factibles respaldadas, con secuencia ordenada de transformaciones;
- ramas condicionales/indeterminadas, separadas de las confirmadas;
- configuraciones intermedias y terminales, con actualización de condiciones y T_acc;
- conjunto Reach derivado de los destinos de trayectorias factibles dentro del horizonte;
- ciclos, duplicados resueltos, ramas truncadas y razones de terminación;
- procedencia, hashes, versiones, parámetros y registro de ejecución del enumerador.

Una repetición con las mismas entradas y reglas debe reproducir las mismas trayectorias, clasificaciones, destinos y razones de terminación. Si existen componentes estocásticos, conservar semillas cuando proceda y distinguir enumeración de resultados posibles de simulación probabilística bajo una política.

### 28.6 Límites de interpretación

La enumeración describe posibilidades estructuralmente respaldadas bajo el modelo, condiciones y horizonte especificados. No demuestra que una trayectoria vaya a seleccionarse, ejecutarse o producir un Outcome/Value determinado. Tampoco equivale a una distribución de probabilidad de ejecución: para obtenerla se requiere un modelo o política de selección/ejecución independiente, validado y explícito.

La completitud solo puede afirmarse respecto del inventario, reglas, horizonte y límites computacionales declarados. La omisión de una transformación candidata, una condición o una rama puede reducir Reach y el conjunto de trayectorias enumeradas. La sensibilidad a granularidad, equivalencia, incertidumbre y cobertura debe informarse.

Este procedimiento no incorpora heurísticas de puntuación, optimización, ranking ni predicción. No activa ni reanuda la capa predictiva o el selector del prototipo. La selección de trayectoria queda fuera del enumerador y requiere especificación y evaluación independientes.

### 28.7 Estado y límites

Este procedimiento es una propuesta metodológica para evaluar si la enumeración de trayectorias TGCV puede hacerse reproducible en un estudio delimitado. No constituye validación empírica ni certifica que exista ya un enumerador implementado. No modifica Core, RMA, Matrix, STATUS, claims o cierres previos, ni autoriza selección de caso, adquisición/procesamiento de datos, preregistro o ejecución experimental. El PR permanece draft y pendiente de revisión.


## 29. Selección, no ejecución y sesgo post-tratamiento

### 29.1 Estados diferenciados de una trayectoria

La relación entre posibilidades y resultados requiere registrar por separado, para cada trayectoria factible o candidata:
1. **Factible respaldada:** satisface las condiciones TGCV bajo la configuración e historia especificadas.
2. **Considerada/conocida:** fue identificada y estuvo disponible para los agentes o decisores pertinentes. Una trayectoria puede ser factible sin haber sido conocida por ellos.
3. **Seleccionada:** fue elegida frente a otras opciones, con registro de quién decide, cuándo, bajo qué información, preferencias, reglas y restricciones.
4. **Iniciada/intento de ejecución:** comenzó una acción dirigida a realizarla.
5. **Ejecutada:** se realizaron una o más transformaciones de la secuencia, con evidencia de cada una.
6. **Completada:** se alcanzó el criterio terminal preespecificado de esa trayectoria.
7. **No seleccionada, no iniciada, interrumpida o fallida:** registrar la categoría y, cuando pueda establecerse, el motivo.

Estas categorías no son equivalentes ni necesariamente estados mutuamente excluyentes de una única variable: una trayectoria puede ser parcialmente ejecutada y luego interrumpida. Conservar el historial temporal y el nivel de avance, sin codificar todos los casos como simple ejecución/no ejecución.

La factibilidad TGCV es una propiedad del sistema bajo condiciones especificadas; el conocimiento, la consideración y la selección son propiedades del proceso de decisión de agentes concretos. La falta de conocimiento o de selección no convierte por sí misma una transformación en inaccesible para el sistema. Si la información o el permiso de acceso son condiciones constitutivas de realizabilidad, deben modelarse explícitamente en T_acc y no confundirse con la mera visibilidad de una opción.

### 29.2 Proceso de selección y variables relevantes

La selección de una trayectoria puede depender de información disponible, preferencias, objetivos, expectativas, costes percibidos y reales, capacidades de los agentes, reglas institucionales, restricciones, coordinación, riesgos y alternativas conocidas. Algunas de estas variables pueden ser basales; otras pueden cambiar como consecuencia de la intervención que modifica T_acc o de transformaciones ejecutadas previamente.

Por ello, el protocolo del caso debe:
- identificar quién selecciona y cuál es la unidad de decisión;
- fechar disponibilidad de información, consideración, selección, inicio, interrupción y finalización;
- registrar alternativas factibles conocidas y desconocidas cuando pueda establecerse;
- documentar razones de selección/no selección y de fallo/interrupción sin tratarlas automáticamente como causas identificadas;
- distinguir costes/restricciones reales de percepciones y expectativas;
- identificar variables que afectan tanto selección/ejecución como Outcome o Value;
- representar la retroalimentación: selección y ejecución pueden cambiar estado, recursos, información y T_acc futuro.

La selección observada no es una muestra aleatoria de trayectorias factibles. Las trayectorias ejecutadas pueden diferir sistemáticamente de las no ejecutadas en características de agentes, contextos, expectativas y restricciones.

### 29.3 Implicaciones para estimandos de C10

El estimando θ_A(q), cuando se defina mediante políticas factibles g_1 y g_0 sobre cambios de accesibilidad, debe aclarar qué proceso posterior de conocimiento, consideración, selección y ejecución queda bajo cada régimen.

Si el objetivo es la contribución total de una política de accesibilidad, las respuestas posteriores de agentes y organizaciones —incluidas selección, no selección, ejecución parcial y abandono— forman parte de las consecuencias del régimen y no deben eliminarse mediante ajuste indiscriminado. En ese caso, no ajustar mecánicamente por selección o ejecución si son mediadores posteriores: hacerlo puede bloquear parte de la vía que se pretende incluir.

Si se desea estimar una contribución bajo una política de selección/ejecución fijada o intervenida, debe definirse un estimando distinto, especificando:
- la política de selección y la unidad decisora;
- la información e historia disponibles en cada momento;
- la intervención sobre ejecución, adherencia o finalización, si procede;
- las combinaciones factibles y el soporte;
- el Outcome/Value potencial y horizonte;
- los supuestos de identificación secuencial y tratamiento de confusión afectada por intervenciones previas.

No interpretar ese contraste condicionado como el efecto total de accesibilidad. Tampoco asumir que comparar seleccionados con no seleccionados identifica el efecto de ejecutar una trayectoria: la selección puede estar confundida por causas basales y post-treatment, y condicionar por ella puede abrir asociaciones espurias.

La selección puede ser un mediador de la contribución de accesibilidad, pero también un punto de selección estadística. Su papel depende del DAG temporal y del estimando, no de una etiqueta fija. La aleatorización de la intervención inicial no aleatoriza automáticamente la selección ni la ejecución.

### 29.4 Datos faltantes, no ejecución y resultados contrafactuales

La ausencia de ejecución no es un dato faltante de trayectoria ejecutada: puede ser un resultado del proceso que debe registrarse. La falta de información sobre si una trayectoria era factible, conocida, seleccionada o ejecutada sí es incertidumbre de medición y debe clasificarse como tal.

No imputar que una trayectoria factible habría producido el Outcome/Value observado en otra unidad o bajo otra trayectoria. No atribuir un Value nulo a una trayectoria no ejecutada salvo que la regla de Value y la pregunta evaluativa definan explícitamente ese resultado. Diferenciar:
- Value observado bajo la trayectoria realizada;
- Value observado bajo la política de accesibilidad asignada, incluyendo no selección/no ejecución;
- Value potencial bajo una política alternativa de selección/ejecución, que requiere un estimando y supuestos adicionales.

El análisis principal debe preservar el contraste de asignación/política que corresponda al diseño. Los análisis por trayectoria seleccionada o ejecutada son secundarios y requieren estrategia explícita para sesgo de selección, confusión temporal, adherencia y positividad. Informar límites de identificación cuando esas condiciones no puedan defenderse.

### 29.5 Requisito de reporte

El informe de C10 debe presentar, al menos, el flujo desde trayectorias factibles enumeradas hasta conocimiento/consideración, selección, inicio, ejecución, interrupción y finalización; las razones conocidas de cada transición; la cobertura de medición; y las diferencias basales y post-treatment relevantes entre trayectorias seleccionadas y no seleccionadas.

No reducir este flujo a una tasa de adopción ni usarlo como sustituto de T_acc. No usar la distribución de trayectorias realizadas como estimación directa del conjunto de trayectorias factibles. Las probabilidades de selección/ejecución solo se estimarán si existe un modelo/política explícito y una estrategia de identificación defendible.

### 29.6 Estado y límites

Este apartado establece requisitos analíticos para separar posibilidad, conocimiento, decisión y ejecución y para evitar sesgos de selección en C10. No identifica por sí mismo efectos de selección o ejecución, no establece un nuevo estimando primario ni decide un modelo de agentes. No modifica Core, RMA, Matrix, STATUS, claims o cierres previos, ni autoriza selección de caso, adquisición/procesamiento de datos, preregistro o ejecución experimental. El PR permanece draft y pendiente de revisión.
