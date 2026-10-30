# VALUE — Protocolo de autoevaluación estructurada de usabilidad

**Versión:** 0.5  
**Estado:** BORRADOR DE PROTOCOLO; revisión individual guiada en curso, con cobertura parcial documentada  
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

**Estado al actualizar este protocolo (v0.3):** revisión individual guiada iniciada y en curso. Hay observaciones del usuario y decisiones documentadas en el log, junto con revisiones de coherencia asistidas. La cobertura del procedimiento no está completa y no se declara cierre de la autoevaluación.


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

### Actividades diferenciadas y pendientes

- **Primera revisión individual guiada:** iniciada; observaciones y decisiones están registradas en el log. No debe describirse como una prueba independiente de usabilidad.
- **Repetición intraevaluador diferida y ciega:** pendiente, según SR-052. Debe conservar un registro nuevo y no consultar la primera pasada hasta cerrar la segunda.
- **Revisión auxiliar ciega por IA:** pendiente, según SR-052. Debe registrarse por separado y no contarse como segundo evaluador humano.
- **Reproducibilidad interevaluador humana:** diferida hasta que exista una comunidad/evaluadores independientes; no realizada.
- **Prueba externa exploratoria opcional:** no iniciada ni comprometida; no es requisito para cerrar la revisión documental actual.

### Regla de cierre

No declarar completado el protocolo hasta:
1. completar o marcar explícitamente como no aplicables las tareas/subtareas pendientes de la primera revisión;
2. realizar la síntesis global prevista en la sección 8 y completar la plantilla de la sección 9;
3. ejecutar y comparar la repetición intraevaluador y la revisión auxiliar ciega acordadas en SR-052, o registrar una decisión explícita y justificada de diferirlas sin presentarlas como realizadas.

El cierre de estas actividades solo podrá respaldar conclusiones formativas sobre esta revisión y consistencia intraevaluador. No demostrará usabilidad independiente, validez empírica, causalidad ni eficacia de VALUE/TGCV.



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
- **Tareas pendientes:** completar las subtareas del primer recorrido sin evidencia formal de intento/observación/contraste; repetición intraevaluador diferida y ciega; revisión auxiliar ciega por IA; comparación y conclusión final.
- **Hallazgos del usuario:** observaciones y decisiones registradas en SR-001–SR-061; SR-062 descartado como nuevo hallazgo.
- **Hallazgos del contraste documental asistido:** desproporción inicial de A3; necesidad de trazabilidad A3→A4→A5; ambigüedad en la separación entre selección, autorización, ejecución y resultados; corrección del estado del protocolo.
- **Ambigüedades o redundancias:** detalle operativo excesivo en A3; duplicidad sustancial SR-062/SR-061; riesgo de interpretar una secuencia contrafactual como registro de ejecución; riesgo de confundir datos fabricados con resultados observados.
- **Cambios aceptados y fundamento:** consolidación A3; IDs y relaciones estables y trazabilidad de opciones/evidencia; separación de estados A6–A8; regla explícita DECIDE→ACT. Cambios limitados a aclaraciones necesarias y sin inventar datos.
- **Cuestiones abiertas:** brechas de evidencia de A5, criterios/umbrales previos no acordados, autorización de ejecución inexistente, repetición ciega y revisión auxiliar pendientes.
- **Limitaciones de esta autoevaluación:** revisión individual guiada y contraste documental asistido; sin participantes independientes, métricas de usabilidad, prueba real ni evidencia empírica de VALUE/TGCV.
- **Decisión:** mantener y continuar la revisión; no declarar cierre ni validación; no ampliar A3.
- **Responsable y fecha:** autor/usuario, con apoyo documental asistido; 2026-10-30.

### Estado tras la síntesis

La síntesis de la primera revisión está realizada y registrada. Esto no significa que la primera revisión formal esté completa en todos sus pasos ni que el protocolo esté cerrado. La siguiente actividad prevista es preparar y ejecutar la repetición intraevaluador diferida y ciega, respetando la separación respecto de los resultados de la primera pasada. La revisión auxiliar ciega por IA se realizará por separado y no se contará como evaluación humana independiente.


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

