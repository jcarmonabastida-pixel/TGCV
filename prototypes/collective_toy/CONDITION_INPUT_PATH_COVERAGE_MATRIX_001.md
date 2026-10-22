# Matriz de cobertura de entrada de condiciones 001

**Estado:** COBERTURA BÁSICA VERIFICADA; gate contractual completo **PENDIENTE**  
**Rama:** `integration/condition-evaluator-dual-graph-001-20261022`  
**Commit de evidencia:** `5cc4015073694e9ae060700c385c4184f398d652`  
**Suite principal:** [`web/cross_runtime_test.cjs`](https://github.com/jcarmonabastida-pixel/TGCV/blob/5cc4015073694e9ae060700c385c4184f398d652/prototypes/collective_toy/web/cross_runtime_test.cjs)  
**CI navegador:** [PASS — run 39833858134](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39833858134)  
**CI motor sintético:** [PASS — run 39833858162](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39833858162)

## 1. Matriz de aceptación

| Vía | Caso comprobado | Resultado | Alcance y límite |
|---|---|---|---|
| JSON | Importar una transición con condición; conservar el texto exactamente y mantener la versión de esquema compatible con condiciones. | **PASS** | La importación no crea una evaluación de condición que no venga acreditada. No demuestra por sí sola todas las variantes de esquemas JSON. |
| Transcriptor en español | «Si hay autorización, el sistema pasa de espera a acceso autorizado». Se genera una transición con la condición «hay autorización». | **PASS** | La condición queda como metadato, no como resultado evaluado; el resultado permanece como borrador que requiere revisión humana. La cobertura se limita a la formulación de prueba, no a todo el español natural. |
| Editor visual | Crear/editar una condición y después borrarla; comprobar que se conserva el texto y se invalida la evaluación previa. | **PASS** | Comprueba el ciclo básico del editor visual, no todas las interacciones posibles ni todas las clases de condición. |

## 2. Invariantes comunes comprobados

- Las condiciones se conservan como información del modelo, separadas de su evaluación.
- Ninguna de las tres vías inventa automáticamente un resultado evaluado.
- La transcripción produce un borrador revisable por una persona.
- Al modificar o eliminar una condición en el editor visual, la evaluación anterior deja de considerarse válida.
- Las pruebas de navegador y del motor sintético pasan en el mismo commit de evidencia.

## 3. Interpretación del resultado

La cobertura de las tres vías queda **verificada solo para los casos explícitos de esta matriz**. Esta matriz registra pruebas básicas de humo/regresión; no cierra la aceptación contractual completa de la sección 10 del contrato vigente. No equivale a demostrar equivalencia semántica exhaustiva entre todas las expresiones JSON, todas las formulaciones del transcriptor y todas las operaciones del editor.

La evaluación de condiciones continúa sujeta a sus propias pruebas de resultado y a la regla de no ejecutar expresiones no evaluables. Un PASS de CI acredita los casos automatizados, no una garantía general sobre todas las entradas posibles.

## 4. Brechas contractuales todavía abiertas

La sección 10 del contrato vigente requiere más que los casos básicos anteriores. Permanecen **PENDIENTES** y no deben interpretarse como aprobados por estos PASS:

- JSON: importación/exportación/replay de condición y procedencia de evaluación; rechazo de evaluaciones mal formadas u obsoletas; comparación equivalente navegador/Python.
- Transcriptor: casos positivos, negativos, ambiguos y adversariales agrupados; negación/dirección no soportadas deben quedar pendientes y nunca simplificarse a una transición incondicional; persistencia de condición y procedencia en revisión, ejecución y exportación/importación.
- Editor visual: recorrido add/change/clear con exportación/importación/replay, manteniendo IDs estables donde sea posible y actualizando ambas vistas.
- Rutas cruzadas: transición condicional e incondicional en cada vía; cambio de condición invalida la evaluación ligada al texto anterior; modelos incondicionales y comportamiento histórico siguen siendo compatibles.
- Integración: demostrar que el derivador de correspondencias y la representación TGCV solo consumen el modelo validado y las correspondencias efectivas, sin que propuestas, rechazos o entradas obsoletas cambien el grafo TGCV, T_acc, alcanzabilidad o resultados de ejecución.

## 5. Siguiente control

Implementar la suite agrupada de aceptación contractual (o separar formalmente el alcance como follow-up revisado, manteniendo visibles estos bloqueos). Verificar también que la cobertura añadida no altera el flujo de ejecución ni los dos grafos fuera de los cambios explícitamente probados. La PR debe seguir en borrador y sin fusionar hasta resolver o dividir explícitamente estos puntos.
