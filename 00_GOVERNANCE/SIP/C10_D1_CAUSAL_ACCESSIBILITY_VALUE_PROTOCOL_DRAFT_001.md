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
