# VALUE — Protocolo de autoevaluación estructurada de usabilidad

**Versión:** 0.7  
**Estado:** FASE DE AUTOEVALUACIÓN INDIVIDUAL CERRADA CON COBERTURA PARCIAL DOCUMENTADA; evaluación externa e interevaluador diferida, no bloqueante para el prototipo  
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
- No se han realizado sesiones independientes ni externas. El trabajo registrado corresponde a una revisión individual guiada en conversación; no debe confundirse con sesiones de prueba formalizadas ni con una evaluación independiente.
- La autoevaluación no es un piloto clínico ni autoriza una intervención real.
- No valida empíricamente VALUE ni la teoría científica TGCV.
- Cualquier futura prueba en una organización real requerirá autorización, salvaguardas y tratamiento de datos adecuados al contexto.

**Nota histórica (estado registrado en v0.3):** en esa fecha la revisión individual guiada estaba iniciada y no se declaraba cerrada. Ese estado fue actualizado por las actividades registradas en las secciones 15 y 16; prevalece la decisión de cierre con cobertura parcial de la versión 0.7.


## 12. Estado de ejecución del protocolo — 2026-10-30

Esta sección registra el estado real conocido de la revisión. No modifica el procedimiento previsto en las secciones anteriores ni convierte los hallazgos en una puntuación de usabilidad.

| Tarea prevista | Evidencia documental disponible | Estado |
|---|---|---|
| 1. Comprensión inicial | SR-001 registra explicación del propósito y salvaguardas por el usuario | REALIZADA para la comprensión inicial; no equivale a evaluación independiente |
| 2. Recorrido A1–A3 | SR-001–SR-013 documentan observaciones de A1/A2; A3 fue ampliado, revisado y posteriormente consolidado | REALIZADA PARCIALMENTE; A1/A2 revisados en el caso y A3 consolidado; no se acredita que cada subactividad se completara con un registro formal de intento/relectura |
| 3. Hipótesis y evidencia A4–A5 | Revisiones de coherencia A3→A4→A5 y ajustes en el caso v1.0 | CONTRASTE DOCUMENTAL REALIZADO; no se acredita una pasada independiente completa del usuario siguiendo todos los pasos de la tarea |
| 4. Decisión y autorización A6 | Revisión A6→A7→A8 y regla DECIDE→ACT aprobada e incorporada al maestro v0.3 | CONTRASTE DOCUMENTAL REALIZADO; la comprensión y decisión están registradas, pero no se ha repetido todavía como tarea ciega/diferida |
| 5. Plan y aprendizaje A7–A8 | Separación documentada entre diseño, autorización, ejecución y datos inventados; sin ejecución real | CONTRASTE DOCUMENTAL REALIZADO; no es prueba de implementación ni aprendizaje empírico |
| 6. Revisión global | Auditorías de coherencia A1–A8 y registro acumulado de hallazgos SR-001–SR-061; SR-062 se descartó como duplicado de SR-061 | PARCIALMENTE REALIZADA; falta una pasada final explícita de duplicidades, términos y campos transversales |

### Actividades diferenciadas y estado

- **Primera revisión individual guiada por el autor/usuario:** REALIZADA con cobertura parcial. Existen observaciones y decisiones registradas en SR-001–SR-061 y en la síntesis. Algunas subtareas no conservan evidencia formal suficiente de intento propio, observación y contraste; se mantienen como no acreditadas, sin convertir esa ausencia de registro en un fallo del evaluador.
- **Repetición intraevaluador diferida con ocultación documental:** REALIZADA y registrada en `VALUE_INTRA_REVIEW_REPEAT_MOBILE_2026-10-30.md`. No fue ciega en sentido estricto.
- **Revisión auxiliar documental por IA:** REALIZADA y registrada por separado en `VALUE_AUXILIARY_AI_REVIEW_CLINIC_001_2026-10-30.md`. No es un participante humano independiente ni una revisión estrictamente ciega.
- **Comparación de las fuentes:** REALIZADA y registrada en `VALUE_REVIEW_COMPARISON_CLINIC_001_2026-10-30.md`.
- **Evaluación por otro evaluador humano / reproducibilidad interevaluador:** NO REALIZADA; se difiere a una fase posterior con colaboradores o comunidad. No es requisito para cerrar esta autoevaluación ni para construir o publicar un prototipo web identificado como implementación de referencia.
- **Prueba externa con usuarios potenciales:** NO REALIZADA; queda como actividad posterior de aprendizaje y evolución comunitaria. No es requisito previo para iniciar el prototipo.

### Regla de cierre aplicada

La fase actual se cierra como **autoevaluación individual formativa con cobertura parcial documentada**. Las subtareas de la primera pasada sin evidencia suficiente quedan marcadas como **no acreditadas**, sin repetir preguntas ni presentarlas como completadas. La repetición, la revisión auxiliar y la comparación se consideran realizadas con las limitaciones descritas.

Este cierre no equivale a validación independiente de usabilidad, fiabilidad interevaluador, validez empírica, causalidad o eficacia de VALUE/TGCV. La ausencia de evaluación externa no bloquea la promoción de una versión documental suficientemente definida ni la construcción del prototipo; sí obliga a comunicar con claridad que se trata de una metodología propuesta y en evolución, abierta a evaluación y mejora por usuarios y comunidad.



## 13. Síntesis de la primera revisión — 2026-10-30

**Referencia:** `VALUE_FIRST_REVIEW_SYNTHESIS_CLINIC_001_v0.1.md`.

### Conclusión de la síntesis

- Se han consolidado documentalmente 61 registros SR-001–SR-061; SR-062 se ha dispuesto como duplicado sustancial de SR-061, no como hallazgo independiente.
- Los registros se han clasificado por naturaleza y destino. No equivalen a 61 defectos ni a 61 tareas de usabilidad completadas.
- A3 se ha consolidado a nivel sistémico y queda cerrada la generación de nuevos escenarios A3 en esta ronda.
- Las revisiones documentales A3→A4→A5 y A6→A7→A8 están registradas; las brechas de evidencia ficticia permanecen explícitas.
- La regla DECIDE→ACT está incorporada en el documento maestro v0.3.
- Las fichas A1–A8 y el protocolo no se consideran validados por estos cambios.

### Plantilla de conclusión — cumplimentación provisional

- **Fecha y versiones revisadas:** 2026-10-30; caso CLINIC-001 v1.1; maestro VALUE Lifecycle v0.3; fichas A1–A8 v0.1; protocolo v0.4; log de autoevaluación vigente en PR #114.
- **Tareas recorridas:** comprensión inicial; revisión guiada A1–A3; contrastes documentales A3→A4→A5 y A6→A7→A8; revisión de coherencia A1–A8; consolidación y clasificación de hallazgos.
- **Tareas pendientes en la fecha de esta síntesis:** completar o delimitar las subtareas sin evidencia formal; realizar la repetición diferida; efectuar la revisión auxiliar; comparar las fuentes y adoptar una conclusión. Las actividades posteriores y su estado final se registran en las secciones 15 y 16.
- **Hallazgos del usuario:** observaciones y decisiones registradas en SR-001–SR-061; SR-062 descartado como nuevo hallazgo.
- **Hallazgos del contraste documental asistido:** desproporción inicial de A3; necesidad de trazabilidad A3→A4→A5; ambigüedad en la separación entre selección, autorización, ejecución y resultados; corrección del estado del protocolo.
- **Ambigüedades o redundancias:** detalle operativo excesivo en A3; duplicidad sustancial SR-062/SR-061; riesgo de interpretar una secuencia contrafactual como registro de ejecución; riesgo de confundir datos fabricados con resultados observados.
- **Cambios aceptados y fundamento:** consolidación A3; IDs y relaciones estables y trazabilidad de opciones/evidencia; separación de estados A6–A8; regla explícita DECIDE→ACT. Cambios limitados a aclaraciones necesarias y sin inventar datos.
- **Cuestiones abiertas:** brechas de evidencia de A5, criterios/umbrales previos no acordados, autorización de ejecución inexistente, repetición ciega y revisión auxiliar pendientes.
- **Limitaciones de esta autoevaluación:** revisión individual guiada y contraste documental asistido; sin participantes independientes, métricas de usabilidad, prueba real ni evidencia empírica de VALUE/TGCV.
- **Decisión:** mantener y continuar la revisión; no declarar cierre ni validación; no ampliar A3.
- **Responsable y fecha:** autor/usuario, con apoyo documental asistido; 2026-10-30.

### Estado tras la síntesis

La síntesis de la primera revisión quedó realizada y registrada en esta fase histórica. La previsión de repetir y revisar con IA fue posteriormente ejecutada con las limitaciones documentadas en la sección 15. La decisión final de cierre de la autoevaluación individual se encuentra en la sección 16 y prevalece sobre esta previsión provisional.


## 14. Adaptación temporal de la repetición a trabajo exclusivamente móvil — 2026-10-30

**Restricción comunicada por el usuario:** temporalmente no dispone de acceso al ordenador; participa desde un teléfono móvil.

### Adaptación operativa

- No se exige acceso a ordenador, edición local de archivos, terminal, hojas de cálculo ni navegación simultánea por múltiples documentos.
- La repetición se realizará en bloques breves, secuenciales y legibles en móvil. Cada bloque presentará únicamente el material necesario para la tarea y solicitará una respuesta concreta.
- El asistente recuperará los documentos canónicos de GitHub, preparará los extractos y registrará las respuestas y resultados en la rama del PR. El usuario no tendrá que copiar, editar ni subir archivos.
- Se evitarán formularios largos, tablas extensas y tareas que requieran comparar varias ventanas. Se conservará una pregunta o decisión por turno cuando sea posible.
- La revisión auxiliar ciega por IA se ejecutará por separado, sobre copias de los artefactos y sin acceso al log ni a los resultados de la primera revisión.

### Alcance de la ceguera

El usuario ya estuvo expuesto a los resultados de la primera pasada. Por ello, la segunda revisión no puede calificarse como plenamente ciega respecto de la memoria del evaluador. Se denominará **repetición intraevaluador diferida con ocultación documental de la primera pasada**: durante la repetición no se mostrarán ni consultarán el log, las auditorías ni la síntesis previa. Esta medida reduce el sesgo de recuerdo documental, pero no elimina el conocimiento previo ni garantiza ceguera estricta.

La revisión auxiliar por IA sí podrá mantenerse separada de los resultados anteriores si se prepara con instrucciones neutrales y únicamente los documentos fuente autorizados.

### Secuencia

1. Preparar un paquete de revisión móvil con el caso, las fichas y las instrucciones estrictamente necesarias; excluir log, síntesis y auditorías.
2. Ejecutar la repetición por bloques, sin revelar resultados anteriores y registrando respuestas originales antes de cualquier contraste.
3. Cerrar y preservar el registro de esta repetición.
4. Ejecutar por separado la revisión auxiliar por IA sin facilitarle la primera pasada ni la repetición del usuario.
5. Comparar ambas revisiones con el registro histórico, clasificar coincidencias y discrepancias y actualizar la conclusión.

La restricción de dispositivo es temporal y no altera los criterios metodológicos ni constituye una razón para declarar realizada una actividad pendiente. No se fija fecha de finalización ni se exige acceso al ordenador.



## 15. Repetición diferida, revisión auxiliar y comparación — 2026-10-30

### Actividades realizadas y registros

- **Repetición intraevaluador diferida con ocultación documental:** realizada desde móvil y preservada en `VALUE_INTRA_REVIEW_REPEAT_MOBILE_2026-10-30.md`. No se denomina ciega en sentido estricto porque el usuario ya conocía la primera pasada.
- **Revisión auxiliar documental por IA:** realizada y registrada en `VALUE_AI_AUXILIARY_REVIEW_CLINIC_001_2026-10-30.md`. Se mantuvo separada de las respuestas como material de análisis, pero no se califica como estrictamente ciega ni como segundo evaluador humano.
- **Comparación:** realizada y registrada en `VALUE_REVIEW_COMPARISON_CLINIC_001_2026-10-30.md`, contrastando primera revisión, repetición y revisión auxiliar.

### Resultado comparativo

- Se observa convergencia temática entre ambas pasadas en propósito, salvaguardas, análisis de proceso, evidencia, criterios de decisión, gobernanza, seguimiento y aprendizaje.
- Las diferencias son principalmente de cobertura y granularidad; no se identifican contradicciones sustantivas.
- La primera pasada aporta mayor detalle sobre horario/alcance, criticidad e impacto asistencial, estacionalidad, histórico de doce meses, camino crítico y casuística operativa.
- La repetición vuelve a expresar el núcleo y hace más explícitos presupuesto, recursos/sistemas, demanda por franja, Owner, SLAs y seguimiento.
- La revisión auxiliar confirma la coherencia general y aporta una aclaración nueva de medición: definir cómo se tratan las solicitudes aún abiertas y sin asignación al corte en el indicador de demora. Otros puntos identificados por IA ya estaban sustancialmente atendidos en la revisión documental previa o son mejoras editoriales de baja prioridad.

### Estado del protocolo

La comparación de las tres fuentes está realizada. La decisión de cierre adoptada en la versión 0.7 es no reabrir la entrevista ni repetir preguntas para completar retrospectivamente registros que no existen. Las subtareas de primera pasada sin evidencia formal suficiente se clasifican como **no acreditadas**. Con ello se cierra la fase actual con cobertura parcial, no como evaluación completa de todas las tareas previstas.

### Límites y continuidad

El conjunto constituye una autoevaluación humana individual, repetida de forma diferida, acompañada de análisis documental asistido por IA. No equivale a una prueba con usuarios independientes ni demuestra reproducibilidad interevaluador, validez empírica, causalidad o eficacia de VALUE/TGCV.

La evaluación por otras personas y la prueba con usuarios potenciales quedan como actividades posteriores, especialmente adecuadas para el prototipo web y su apertura comunitaria. No son puertas de bloqueo para desarrollar una implementación de referencia, siempre que se identifiquen su versión, alcance, límites y carácter evolutivo.


## 16. Decisión de cierre de la fase actual — 2026-10-30

**Decisión:** cerrar la fase de autoevaluación individual con cobertura parcial documentada.

### Qué se considera realizado

1. Primera revisión humana individual guiada: realizada; cobertura parcial y algunas subtareas no acreditadas.
2. Repetición intraevaluador diferida con ocultación documental: realizada, sin ceguera estricta.
3. Revisión auxiliar documental por IA: realizada; no constituye evaluación humana independiente.
4. Comparación cualitativa de las tres fuentes: realizada y registrada.

### Qué queda diferido

- Evaluación por otro evaluador humano y reproducibilidad interevaluador.
- Pruebas de usabilidad con usuarios potenciales y evaluación comunitaria.
- Validación empírica de resultados, causalidad o eficacia.

Estas actividades son líneas posteriores de evaluación y mejora. No constituyen requisitos previos para construir el prototipo web ni para promocionar una versión documental de VALUE que supere la revisión de integridad y los controles de gobernanza del repositorio.

### Condiciones de comunicación

El prototipo deberá presentarse como implementación de referencia de una metodología propuesta, no como producto validado. Deberá hacer visibles las incertidumbres, los estados incompletos y los límites conocidos, y facilitar que usuarios y comunidad aporten observaciones y propuestas de evolución.

Esta decisión cierra únicamente la fase de autoevaluación descrita en este protocolo. No declara VALUE validado ni altera el estado científico de TGCV.
