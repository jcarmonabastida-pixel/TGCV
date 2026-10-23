# Matriz de cobertura de entrada de condiciones 001

**Estado:** COBERTURA BÁSICA VERIFICADA; gate contractual completo **PENDIENTE**  
**Rama:** `integration/condition-evaluator-dual-graph-001-20261022`  
**Commit de evidencia vigente:** `3ca748e86cc611117a1706d03f11b08158ed3c79`  
**Suite principal:** [`web/cross_runtime_test.cjs`](https://github.com/jcarmonabastida-pixel/TGCV/blob/3ca748e86cc611117a1706d03f11b08158ed3c79/prototypes/collective_toy/web/cross_runtime_test.cjs)  
**CI navegador:** [PASS — run 39839359797](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39839359797)  
**CI motor sintético:** [PASS — run 39839359823](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39839359823)

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

- JSON: la importación de condición está cubierta para el caso básico. El ciclo de exportación/importación/replay con condición y hash de procedencia ya pasa en navegador (commit `36268dd`). La prueba negativa de paquete manipulado pasa en navegador y Python: cambiar la condición exportada sin actualizar la procedencia provoca rechazo, no `replay-verified` (commit `36772cb`). La prueba Python recalcula el hash exterior para aislar y verificar el fallo del hash de entrada; ambos workflows pasan. Se añadió una prueba negativa explícita para un paquete con hash exterior, hash de entrada y hash de resultado recalculados, pero con evaluación que conserva el texto de condición anterior. La prueba de evaluación obsoleta pasa en ambos entornos (commit `b03971f`; navegador y motor sintético PASS).
- Transcriptor: pasan los casos positivo, negado, ambiguo y el nuevo adversarial de dirección no soportada añadido en `bbfcffd` (CI de ese commit pendiente). La frase «El acceso autorizado precede a la espera» debe quedar pendiente y no crear una arista adivinada ni invertida. Sigue pendiente verificar persistencia de condición y procedencia en revisión, ejecución y exportación/importación.
- Editor visual: recorrido add/change/clear con exportación/importación/replay, manteniendo IDs estables donde sea posible y actualizando ambas vistas.
- Rutas cruzadas: transición condicional e incondicional en cada vía; cambio de condición invalida la evaluación ligada al texto anterior; modelos incondicionales y comportamiento histórico siguen siendo compatibles.
- Integración: demostrar que el derivador de correspondencias y la representación TGCV solo consumen el modelo validado y las correspondencias efectivas, sin que propuestas, rechazos o entradas obsoletas cambien el grafo TGCV, T_acc, alcanzabilidad o resultados de ejecución.

## 5. Siguiente control

El rechazo explícito de una evaluación condicional obsoleta dentro de un paquete íntegro a nivel de hashes ya pasa en navegador y Python (commit `b03971f`). El siguiente control es el transcriptor adversarial de dirección no soportada, incorporado en `bbfcffd`: con una transición explícita válida junto a una frase direccional no soportada, solo debe representarse la transición explícita y la otra frase debe quedar pendiente. Las pruebas existentes de estado TRUE/FALSE/UNKNOWN y evaluación obsoleta son controles de modelo/ejecución; no sustituyen estas pruebas del paquete importado. La PR debe seguir en borrador y sin fusionar hasta resolver o dividir explícitamente estos puntos.
