# C10-S — Registro de recuperación de las secciones 165–183

**Estado:** fuente conversacional recuperada en archivo aportado; contenido examinado; registro de decisiones y pendientes incorporado a la rama de trabajo.  
**Fuente primaria recibida:** `Notes_261104_163033.docx` (DOCX, 263.845 bytes; 4.366 líneas de texto extraído por Files).  
**Intervalo recuperado:** desde el encabezado 165 hasta inmediatamente antes del encabezado 184.  
**PR:** #116, rama `research/c10-s-consolidation-draft`.  
**Naturaleza:** recuperación documental; no equivale a aprobación metodológica, cierre de auditoría ni ejecución.

## 1. Integridad y límites de la recuperación

El DOCX contiene las secciones 165–183 y material intercalado de continuidad conversacional, dictámenes y transiciones. En varios puntos aparecen primero encabezados-resumen de 174–180 y después el desarrollo detallado; ambos se conservan como parte de la fuente. El contenido de tablas se puede transcribir a filas Markdown, pero esa conversión no conserva la maquetación original. La recuperación no debe presentarse como reproducción visual idéntica del DOCX.

El archivo fuente está disponible como adjunto de esta conversación. Este registro y los artefactos relacionados en GitHub documentan su contenido; **la copia íntegra del DOCX y una transcripción literal completa aún deben incorporarse al repositorio**. No se afirma que se haya subido el DOCX a GitHub.

## 2. Inventario de secciones recuperadas

| Sección | Contenido efectivamente presente en la fuente | Estado de decisión |
|---|---|---|
| 165 | Problema de compatibilidad entre dependencia basal ausente, provisión en control y primera etapa p0=.20/p1=.80 | Pregunta de trabajo; resuelta provisionalmente en 166–168, no aprobada |
| 166 | Cadena Z→B→W→componentes técnicos→C_dep,1→A_f*; C_dep,0=0; mecanismo de provisión ordinaria en control | Desarrollo matemático propuesto |
| 167 | Mantener D1 (provisión ordinaria en control, primera etapa .60) y D2 (sin provisión en control, primera etapa .80); D1 recomendado como principal condicionado | Dictamen provisional; aceptación explícita pendiente |
| 168 | Contrato elemental D1/D2, umbrales latentes, U_K compartida, componentes técnicos conservados y estratos de cumplimiento | Especificación propuesta; revisar distribución conjunta y consistencia |
| 169 | Independencia instrumental, relevancia, monotonicidad individual, exclusión, versiones/consistencia y no interferencia | Supuestos a auditar; no demostrados |
| 170 | Matriz de potenciales V_i(a,z), efecto directo δ, interacción γ, vías alternativas y seis pruebas adversariales E1–E6 | Diseño adversarial propuesto |
| 171 | Sensibilidad a δ y γ, sesgo IV, umbrales de cambio de signo, cotas y clasificación robusta/condicionada/insuficiente | Fórmulas y ejemplos ilustrativos; rangos plausibles y precisión pendientes |
| 172 | Heterogeneidad τ_i, interpretación LATE, diferencias de compliers D1/D2 y límites de extrapolación a ATE | Desarrollo conceptual; no extrapolar LATE al ATE |
| 173 | Condiciones iniciales, selección/composición de compliers, perfiles TGCV, aproximación a ATE y consecuencias de diseño | Desarrollo conceptual; especificación final pendiente |
| 174 | Matriz de identificación causal por perfiles basales X_i, P*_τ2/P*_F, identificación condicionada, agregación y reglas de decisión | Propuesta; perfiles, positividad y agregación pendientes |
| 175 | Matriz de potenciales A_i(z), O_i(a,z), F_alt,i(z), V_i(a,z), verdad del generador vs datos del analizador | Arquitectura de verdad propuesta |
| 176 | DGP adversariales integrados, verdad oculta, respuestas esperadas y pruebas de aceptación | Catálogo propuesto; DGP/fixtures y límites epistemológicos pendientes |
| 177 | Arquitectura de estimación: ITT-A/O/V, LATE, errores estándar, intervalos, covariables, ATE/ATT, multiplicidad y recuperación | Protocolo propuesto; parámetros y tolerancias pendientes |
| 178 | Protocolo de simulación, N, potencia, réplicas Monte Carlo, semillas, pérdidas, escenarios, aceptación y artefactos | Especificación no ejecutada; N/replicaciones/precisión sin justificación final |
| 179 | Value escalar vs vectorial, cinco dimensiones candidatas, Outcome≠Value, observador/contexto/criterio, antes/después | Recomendación provisional: vector multidimensional como principal |
| 180 | Selección de dimensiones y escalas; separación de accesibilidad de transformación y acceso de destinatarios; evitar agregación prematura | Desarrollo propuesto; escalas e indicadores requieren aceptación |
| 181 | Medición independiente de A/O/V, temporalidad T0–T6, separación generador/analizador, cegamiento y P181-01…12 | Protocolo conceptual; pruebas no ejecutadas |
| 182 | Validez de constructo A/O/V, fiabilidad, error de medición, invariancia, sensibilidad y P182-01…12 | Desarrollo conceptual completado según la fuente; pruebas no ejecutadas |
| 183 | Datos ausentes, MCAR/MAR/MNAR, diferencias A/O/V, ITT, mediación, censura, selección, cotas, sensibilidad y P183-01…13 | Desarrollo conceptual completado según la fuente; pruebas no ejecutadas |

## 3. Decisiones y relaciones que deben preservarse

### 3.1 DGP S4R-D1 y D2

- D1: provisión ordinaria posterior a la asignación en el control, con intento (w_0=0.25), (w_1=1), éxito técnico conjunto objetivo 0.80; (p_0=0.20), (p_1=0.80), primera etapa 0.60.
- D2: sin provisión ordinaria en control, (w_0=0), (w_1=1); (p_0=0), (p_1=0.80), primera etapa 0.80.
- En ambos, la ausencia de dependencia basal (C_{dep,0}=0) no excluye instalación posterior a la asignación.
- La fuente recomienda D1 como escenario principal condicionado a justificar el régimen ordinario de control; D2 queda como contraste.
- El control no debe llamarse contaminado si la provisión ordinaria pertenece al régimen comparador previsto. Si recibe componentes reservados al tratamiento, registrar crossover/contaminación.
- Los componentes instalación, integridad, compatibilidad y operatividad deben conservarse, no quedar ocultos en K.
- La independencia entre latentes es una decisión del generador, no requisito lógico de monotonicidad.

### 3.2 Identificación IV y sensibilidad

- La primera etapa no demuestra exclusión.
- Con efecto directo δ, el Wald se desvía de τ; con interacción γ, el efecto de accesibilidad depende del régimen.
- Si la exclusión falla, el ITT de Z puede seguir representando el efecto de la política, pero no el efecto focal aislado de accesibilidad.
- El LATE representa a compliers del instrumento/política estudiada; D1 y D2 pueden tener composiciones y LATE diferentes.
- La aleatorización no identifica automáticamente ATE ni autoriza extrapolar el LATE.
- La verdad de estratos y potenciales del generador no puede filtrarse al analizador.

### 3.3 Medición y Value

- Mantener A (accesibilidad), O (Outcome) y V (Value) conceptualmente separados, sin exigir independencia estadística.
- A no se define por éxito de ejecución; O no se define por valoración; V no se deriva mecánicamente de A ni de O.
- La fuente recomienda inicialmente V multidimensional y posponer índice agregado hasta justificar ponderaciones y reglas de compensación.
- Distinguir accesibilidad de transformación de acceso de destinatarios.
- Mantener temporalidad, fuentes, instrumentos, cegamiento, fiabilidad, invariancia y trazabilidad.

### 3.4 Ausencia, censura y selección

- No convertir automáticamente ausencia de A en inaccesibilidad; no imputar cero a O o V.
- Distinguir ausencia de registro, fallo técnico, abandono, censura temporal, indefinición estructural y medición inválida.
- Conservar la población aleatorizada para ITT; auditar selección postasignación.
- La mediación por accesibilidad requiere supuestos adicionales; ausencia de datos puede impedir identificar el mecanismo aunque el efecto total siga siendo identificable.
- Utilizar cotas y sensibilidad cuando proceda; declarar no identificación cuando no sean defendibles.
- Separar censura administrativa e informativa, MAR/MNAR y horizontes temporales.

## 4. Inventario de pruebas recuperadas

- P181-01…12: medición independiente, circularidad, fuentes, cegamiento, temporalidad, ausencias, invariancia, reproducibilidad, no filtración y contaminación.
- P182-01…12: cobertura/circularidad de A, especificación O, separación O/V, reproducibilidad, acuerdo interevaluador, error A y O/V, invariancia, sensibilidad de Value, separación generador/analizador y trazabilidad.
- P183-01…13: el inventario recuperado en la fuente abarca ITT, selección postasignación, mediación, censura, sensibilidad MAR/MNAR, cotas, dictamen por estimando y trazabilidad. La tabla completa de P183 debe cotejarse con el registro de contratos para preservar la formulación exacta de cada ficha.
- Todas son propuestas: no se han ejecutado ni constituyen evidencia.

## 5. Alertas de reconciliación antes de cerrar

1. No confundir (p_0) (acceso final postasignación bajo régimen de control) con acceso basal. En D1 la fuente plantea (C_{dep,0}=0) y provisión ordinaria posterior.
2. La fuente usa tanto (A_f^*), (A_{	au2}) y (A); armonizar notación sin borrar su procedencia.
3. En 168 se simplifica (A_f^*=C_{dep,1}) solo porque (C_{other}=1) en esa versión; no generalizar esa igualdad.
4. En 170–171, las fórmulas de Wald con δ/γ se presentan en un modelo simplificado; revisar la expresión bajo heterogeneidad y los supuestos del DGP antes de convertirlas en contrato general.
5. En 172–174, no equiparar LATE de D1 y D2 ni agregar perfiles sin justificar población objetivo y pesos.
6. En 177–178, N, réplicas, potencia, tolerancias y multiplicidad no están fijados con justificación definitiva.
7. En 179–182, no aceptar un índice escalar de Value sin regla previa, ponderaciones y sensibilidad.
8. En 183, los mecanismos MAR/MNAR y las cotas dependen de supuestos explícitos; no convertir el catálogo en garantía de identificación.
9. La sección 184 aparece solo como siguiente paso propuesto y queda fuera del intervalo recuperado.

## 6. Estado de aceptación

| Elemento | Estado |
|---|---|
| Fuente DOCX recibida y leída | RECUPERADO |
| Cobertura de secciones 165–183 | RECUPERADA |
| Transcripción estructurada y extracción de tablas | REALIZADA EN EL ENTORNO DE TRABAJO |
| Copia íntegra DOCX persistida en GitHub | PENDIENTE |
| Reconciliación completa con matriz/decision log/test register | EN CURSO |
| Decisiones científicas aceptadas | DEC-C10-066: D2 primario candidato / D1 secundario; no implica aprobación de parámetros o ejecución |
| P181/P182/P183 ejecutadas | NO |
| Revisión independiente | PENDIENTE |
| Freeze C10-S | NO ALCANZADO |

## 7. Criterio de continuación

El trabajo siguiente no es desarrollar una nueva sección teórica. Es integrar esta fuente con los artefactos existentes, contrastar ecuaciones/estimandos y completar las fichas P182/P183. La sección 184 solo se abordará después de cerrar esa integración y decidir si realmente queda una incertidumbre no cubierta.

## 4. Nota de supersesión de precedencia — DEC-C10-066 (2026-11-06)

Las filas y el resumen de §§2–3.1 reproducen fielmente la recomendación histórica de la fuente recuperada: D1 principal condicionado y D2 contraste. Esa recomendación es evidencia histórica de lo que proponía la fuente, no el estado de decisión vigente. DEC-C10-066 la supersede exclusivamente en la selección del escenario primario candidato: D2 primario candidato y D1 secundario. Se conserva el registro fuente sin reescritura para mantener trazabilidad.

La legitimidad de D2 sigue requiriendo verificación de ausencia basal y ausencia de provisión focal de fondo. D1 requiere justificar el régimen ordinario si se interpreta como contraste incremental. Ningún parámetro de la fuente queda validado por DEC-C10-066.
