# VALUE — Protocolo de autoevaluación estructurada de usabilidad

**Versión:** 0.2  
**Estado:** BORRADOR DE PROTOCOLO; revisión no iniciada  
**Modo previsto en esta fase:** una persona (autor/usuario), con acompañamiento conversacional para revisar documentos  
**Ámbito:** comprensión y usabilidad documental del estándar VALUE. No es validación científica de TGCV ni prueba de eficacia de una intervención.

## 1. Objetivo

Realizar una primera revisión estructurada de VALUE recorriendo A1–A8 con el caso ficticio CLINIC-001. El objetivo es detectar ambigüedades, duplicidades, lagunas, dificultades de navegación y rupturas de trazabilidad antes de considerar una evaluación externa.

Esta fase se adapta a la situación actual: el usuario trabaja solo. No se requiere reclutar participantes externos para avanzar.

## 2. Qué puede y qué no puede concluirse

Esta autoevaluación puede producir hallazgos formativos sobre la comprensión del propio autor/usuario, y una revisión documental complementaria de coherencia. No demuestra que otras personas usarían el estándar sin ayuda, no valida métricas ni hipótesis, no demuestra causalidad y no prueba eficacia.

ChatGPT puede ayudar a localizar contradicciones, contrastar documentos y registrar hallazgos, pero **no es un participante humano independiente** y su análisis no sustituye una prueba independiente de usabilidad.

## 3. Preguntas de revisión

1. ¿Se entiende el propósito y la decisión que debe apoyar el caso?
2. ¿Se distingue A1 (Value Intent) de A2 (Value Opportunity Brief)?
3. ¿Se entiende el Value System Model (A3) como modelo integrado con vistas, no como una colección de modelos independientes?
4. ¿Se distinguen hechos, fuentes, inferencias, hipótesis, supuestos, decisiones y resultados?
5. ¿Se puede seguir la trazabilidad entre A4–A6 y entender por qué DECIDE no equivale a autorización para ejecutar?
6. ¿Se distingue el Value Discovery Sprint de una prueba operativa posterior?
7. ¿Queda claro que los datos ficticios de CLINIC-001 no prueban causalidad ni eficacia?
8. ¿Hay campos ambiguos, redundantes, difíciles de completar o que requieren explicaciones que el estándar debería proporcionar?

## 4. Materiales

- `VALUE_METHODOLOGY_LIFECYCLE_001.md` (estándar maestro).
- `VALUE_ARTIFACT_MASTER_SPECS_v0.1.md` (especificaciones A1–A8).
- `VALUE_DISCOVERY_SPRINT_v0.1.md`.
- `VALUE_FICTIONAL_CASE_CLINIC_001_v0.1.md`, identificado siempre como caso y datos ficticios.
- Este protocolo y el registro de hallazgos que se complete durante la revisión.

## 5. Procedimiento de autoevaluación guiada

No se presupone una sesión única de 45–60 minutos. La revisión puede realizarse en varios turnos, una tarea cada vez, para no sobrecargar el proceso.

Para cada tarea:

1. **Primero, intento propio:** el usuario interpreta el documento o intenta completar la tarea con la información disponible, antes de recibir una solución sugerida.
2. **Registro:** se anota qué resultó claro, qué bloqueó el avance, qué hubo que releer y qué información faltaba.
3. **Contraste documental:** ChatGPT ayuda a comparar la observación con el estándar maestro, las especificaciones y el caso; diferencia contradicción textual de posible dificultad de uso.
4. **Decisión:** clasificar el hallazgo como corregir, investigar más, mantener con justificación o posponer.
5. **Cambio controlado:** si se acuerda una modificación, actualizar los documentos en la rama de trabajo y comprobar que no crea contradicciones en otras partes.

### Secuencia de tareas

1. **Comprensión inicial:** explicar con palabras propias el problema ficticio, la decisión que debe apoyar y las restricciones.
2. **Recorrido A1–A3:** localizar intención, oportunidad y modelo del sistema; anotar solapamientos o información difícil de ubicar.
3. **Hipótesis y evidencia:** seguir un ejemplo por A4 y A5, distinguiendo evidencia de hipótesis y supuestos.
4. **Decisión y autorización:** recorrer A6 y explicar qué se ha decidido, qué no está autorizado y qué condiciones siguen pendientes.
5. **Plan y aprendizaje:** distinguir el Sprint de descubrimiento, el plan A7 y cualquier prueba operativa posterior; comprobar qué puede afirmarse en A8.
6. **Revisión global:** identificar campos repetidos, términos no definidos, lagunas y cambios prioritarios.

El caso es ficticio. No se pide emitir juicios asistenciales ni validar una intervención clínica.

## 6. Registro de hallazgos

Usar un ID por hallazgo (por ejemplo, `USAB-VALUE-F001`) y registrar:

- Fecha y versión exacta de los documentos.
- Tarea y artefacto afectados.
- **Intento/observación del usuario:** qué intentó hacer, qué entendió, dónde se bloqueó y qué tuvo que releer.
- **Análisis documental asistido:** contradicción, ambigüedad o laguna detectada al contrastar documentos.
- **Interpretación provisional:** explicación posible, claramente separada de la observación.
- Tipo: redacción / estructura / redundancia / trazabilidad / concepto sin definir / ejemplo insuficiente / otro.
- Gravedad para comprender o tomar una decisión: baja / media / alta, con justificación.
- Propuesta: aceptar / comprobar más / rechazar con motivo / posponer.
- Estado y referencia al cambio documental, si lo hay.

No registrar inferencias como observaciones directas. No inventar sesiones, participantes, tiempos ni resultados. Si una tarea no se ha realizado, mantenerla como pendiente.

## 7. Criterios formativos

No se calculará una puntuación global ni se tratarán estos criterios como métricas validadas. En cada tarea se comprobará si:

- La información necesaria se localiza sin que la respuesta se proporcione de antemano.
- Los conceptos críticos se pueden explicar con palabras propias.
- La relación entre hipótesis, evidencia, decisión y aprendizaje resulta trazable.
- Las lagunas del estándar se pueden distinguir de información que el caso ficticio simplemente no aporta.
- Los límites de los datos ficticios y de la autorización se interpretan correctamente.

Una dificultad detectada por el propio autor/usuario es una señal para investigar, no una medida independiente de usabilidad. Una ausencia de dificultad tampoco prueba que otros usuarios entenderían el material.

## 8. Síntesis y decisión

Al cerrar el recorrido:

1. Agrupar hallazgos por artefacto y tipo.
2. Separar defectos documentales de preguntas abiertas que requieren evidencia externa.
3. Priorizar por gravedad para la decisión, claridad de la evidencia y coste de corrección; explicar cada prioridad.
4. Registrar las decisiones y su fundamento.
5. Modificar los documentos de forma controlada y volver a recorrer las tareas afectadas.
6. Dejar explícito qué partes se han revisado y cuáles siguen pendientes.

No cambiar el estándar solo para que coincida con la interpretación esperada. Si el documento no permite responder una pregunta, registrar la posible laguna.

## 9. Plantilla de conclusión

- Fecha y versiones revisadas:
- Tareas recorridas:
- Tareas pendientes:
- Hallazgos del usuario:
- Hallazgos del contraste documental asistido:
- Ambigüedades o redundancias:
- Cambios aceptados y fundamento:
- Cuestiones abiertas:
- Limitaciones de esta autoevaluación:
- Decisión: mantener / revisar / ampliar revisión:
- Responsable y fecha:

## 10. Evaluación externa futura (opcional)

Cuando existan colaboradores o usuarios potenciales, podrá plantearse una prueba independiente con 3–5 personas como primer sondeo exploratorio. No es requisito para continuar la revisión documental ni debe presentarse como validación estadística. El diseño de esa futura prueba se concretará cuando haya participantes y contexto disponibles.

## 11. Límites y estado

- CLINIC-001 y sus datos son ficticios.
- No se han realizado ni simulado sesiones de evaluación.
- La autoevaluación no es un piloto clínico ni autoriza una intervención real.
- No valida empíricamente VALUE ni la teoría científica TGCV.
- Cualquier futura prueba en una organización real requerirá autorización, salvaguardas y tratamiento de datos adecuados al contexto.

**Estado al actualizar este protocolo:** procedimiento adaptado a una revisión individual guiada; revisión todavía no iniciada.
