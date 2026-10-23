# Matriz de cobertura de entrada de condiciones 001

**Estado:** COBERTURA DE CASOS EXPLÍCITOS EN PROGRESO; gate contractual completo **PENDIENTE**  
**Rama:** `integration/condition-evaluator-dual-graph-001-20261022`  
**Último commit de pruebas con ambos workflows PASS:** `1d4de6fb048f2c8a6208857f590efab4d470e161`  
**Suite principal:** [`web/cross_runtime_test.cjs`](https://github.com/jcarmonabastida-pixel/TGCV/blob/1d4de6fb048f2c8a6208857f590efab4d470e161/prototypes/collective_toy/web/cross_runtime_test.cjs)  
**CI navegador:** [PASS — run 39886203041](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39886203041)  
**CI motor sintético:** [PASS — run 39886203056](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39886203056)

## 1. Matriz de aceptación

| Vía | Caso comprobado | Resultado | Alcance y límite |
|---|---|---|---|
| JSON | Importar una transición con condición; conservar el texto exactamente y mantener la versión de esquema compatible con condiciones. | **PASS** | La importación no crea una evaluación de condición que no venga acreditada. No demuestra por sí sola todas las variantes de esquemas JSON. |
| Transcriptor en español | Caso positivo con «Si hay autorización…»; caso negativo «No pasa de ejecución a resultado»; caso ambiguo «Si quizá hay autorización…». | **PASS** | El caso positivo conserva la condición como metadato y el borrador requiere revisión humana. Negación y ambigüedad quedan pendientes y no se simplifican a una transición aceptada. Alcance limitado a estas formulaciones de prueba, no a todo el español natural. |
| Editor visual | Crear/editar una condición y después borrarla; comprobar que se conserva el texto y se invalida la evaluación previa. | **PASS** | Comprueba el ciclo básico del editor visual, no todas las interacciones posibles ni todas las clases de condición. |

## 2. Invariantes comunes comprobados

- Las condiciones se conservan como información del modelo, separadas de su evaluación.
- Ninguna de las tres vías inventa automáticamente un resultado evaluado.
- La transcripción produce un borrador revisable por una persona.
- Las frases negativas no se convierten en transiciones afirmativas y la condición explícitamente ambigua «quizá» permanece pendiente de aclaración.
- Al modificar o eliminar una condición en el editor visual, la evaluación anterior deja de considerarse válida.
- Las pruebas de navegador y del motor sintético pasan en el mismo commit de evidencia.

## 3. Interpretación del resultado

La cobertura de las tres vías queda **verificada solo para los casos explícitos de esta matriz**. Esta matriz registra pruebas básicas de humo/regresión; no cierra la aceptación contractual completa de la sección 10 del contrato vigente. No equivale a demostrar equivalencia semántica exhaustiva entre todas las expresiones JSON, todas las formulaciones del transcriptor y todas las operaciones del editor.

La evaluación de condiciones continúa sujeta a sus propias pruebas de resultado y a la regla de no ejecutar expresiones no evaluables. Un PASS de CI acredita los casos automatizados, no una garantía general sobre todas las entradas posibles.

## 4. Brechas contractuales todavía abiertas

La sección 10 del contrato vigente requiere más que los casos básicos anteriores. Permanecen **PENDIENTES** y no deben interpretarse como aprobados por estos PASS:

- JSON: la importación de condición está cubierta para el caso básico. El ciclo de exportación/importación/replay con condición y hash de procedencia ya pasa en navegador (commit `36268dd`). La prueba negativa de paquete manipulado pasa en navegador y Python: cambiar la condición exportada sin actualizar la procedencia provoca rechazo, no `replay-verified` (commit `36772cb`). La prueba Python recalcula el hash exterior para aislar y verificar el fallo del hash de entrada; ambos workflows pasan. Se añadió una prueba negativa explícita para un paquete con hash exterior, hash de entrada y hash de resultado recalculados, pero con evaluación que conserva el texto de condición anterior. La prueba de evaluación obsoleta dentro de un paquete íntegro pasa en navegador y motor sintético (commit `b03971f`). La prueba directa de entrada JSON con evaluación obsoleta también pasa en ambos entornos (`1d4de6f`).
- Transcriptor: pasan los casos positivo, negado, ambiguo y el nuevo adversarial de dirección no soportada añadido en `bbfcffd` (CI de ese commit pendiente). La frase «El acceso autorizado precede a la espera» debe quedar pendiente y no crear una arista adivinada ni invertida. El recorrido integrado condición transcrita→ejecución→exportación/importación/replay está cubierto en la suite de navegador: verifica texto exacto, ausencia de alcanzabilidad mientras no se evalúe y reproducción verificada. El control se conserva como cobertura de navegador; no amplía el alcance de la validez general del transcriptor. La persistencia de la procedencia a través de la revisión humana requiere aún un caso específico. El control JSON negativo para evaluación obsoleta pasa en ambos entornos en `1d4de6f`: si cambia el texto de condición y se conserva una evaluación TRUE vinculada al texto anterior, la ejecución rechaza el modelo.
- Editor visual: recorrido add/change/clear y exportación/importación/replay de la condición editada (`humidity is extremely low`); ambos workflows PASS en `5c772a0`. Se prueba que, tras cambiar el modelo fuente y volver a derivar, el paquete puede incluir propuestas nuevas solo si cada candidata conserva la procedencia del modelo vigente; ninguna decisión `ACCEPTED` del alcance anterior puede sobrevivir. La aserción inicial que exigía omitir toda revisión era demasiado estricta: confundía propuestas pendientes nuevas con decisiones aceptadas obsoletas. Corrección de prueba en `7150903`, CI pendiente.
- Rutas cruzadas: transición condicional e incondicional en cada vía; cambio de condición invalida la evaluación ligada al texto anterior; modelos incondicionales y comportamiento histórico siguen siendo compatibles.
- Integración: demostrar que el derivador de correspondencias y la representación TGCV solo consumen el modelo validado y las correspondencias efectivas, sin que propuestas, rechazos o entradas obsoletas cambien el grafo TGCV, T_acc, alcanzabilidad o resultados de ejecución.

## 5. Siguiente control

El rechazo explícito de una evaluación condicional obsoleta dentro de un paquete íntegro a nivel de hashes ya pasa en navegador y Python (commit `b03971f`). El recorrido del editor visual por exportación/importación/replay pasa en el commit `5c772a0`. El control de exportación tras cambiar el modelo fuente pasa en ambos entornos en `7150903`: permite propuestas nuevas con procedencia actual y prohíbe conservar decisiones ACCEPTED del modelo anterior. El control de revisión/aceptación humana ya verifica persistencia de decisión, alcance modelo/catálogo, aplicación explícita, idempotencia, conflictos con declaraciones del usuario, invalidación e historial. Se añade un caso de regresión: después de aceptar y aplicar, cambiar el modelo y restaurar exactamente el modelo anterior no debe resucitar la decisión ni la correspondencia efectiva; commit `0851ee1`, CI pendiente. Las pruebas de evaluación obsoleta no sustituyen este control de procedencia. La PR debe seguir en borrador y sin fusionar hasta resolver o dividir explícitamente estos puntos.


### Incidencia de sincronización en pruebas de importación JSON

El control añadido para importar un JSON con una condición `TRUE` y rutas incondicionales independientes no llegó a evaluar ese escenario: la suite de navegador falló antes, porque una espera genérica por `Archivo cargado y validado` podía satisfacerse con el mensaje de una importación anterior. La aserción posterior leía entonces el modelo previo (`humidity is low`) en vez del archivo recién seleccionado (`conditional-model.json`). No hay evidencia en ese fallo de un defecto del importador. Se cambió la sincronización para esperar el nombre exacto de cada archivo. Corrección en `ee111d287d9bd9205a09528cb1627165b90f7a3b`; workflows pendientes.


### Estado de validación más reciente

Los workflows de navegador y motor sintético pasan para `ee111d287d9bd9205a09528cb1627165b90f7a3b`. La prueba de importación JSON espera el nombre exacto del archivo y verifica que una condición TRUE vinculada correctamente habilita su transición sin bloquear rutas incondicionales independientes.
