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
