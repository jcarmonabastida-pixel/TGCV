# Matriz de cobertura de entrada de condiciones 001

**Estado:** COBERTURA DE CASOS EXPLÍCITOS EN PROGRESO; gate contractual completo **PENDIENTE**  
**Rama:** `integration/condition-evaluator-dual-graph-001-20261022`  
**Último commit con ambos workflows PASS:** `6c0329bf8abd546e5597153b2d7a7fb3ac9f2caf`  
**Suite principal:** [`web/cross_runtime_test.cjs`](https://github.com/jcarmonabastida-pixel/TGCV/blob/6c0329bf8abd546e5597153b2d7a7fb3ac9f2caf/prototypes/collective_toy/web/cross_runtime_test.cjs)  
**CI navegador:** [PASS — run 39947686882](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39947686882)  
**CI motor sintético:** [PASS — run 39947686918](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39947686918)

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
- Transcriptor: pasan los casos positivo, negado, ambiguo y el nuevo adversarial de dirección no soportada añadido en `bbfcffd` (CI de ese commit pendiente). La frase «El acceso autorizado precede a la espera» debe quedar pendiente y no crear una arista adivinada ni invertida. El recorrido integrado condición transcrita→ejecución→exportación/importación/replay está cubierto en la suite de navegador: verifica texto exacto, ausencia de alcanzabilidad mientras no se evalúe y reproducción verificada. El control se conserva como cobertura de navegador; no amplía el alcance de la validez general del transcriptor. La persistencia de la procedencia a través de la revisión humana está siendo probada ahora específicamente para el modelo generado por el transcriptor: candidato con condición exacta, decisión humana `ACCEPTED`, hash del modelo fuente y exportación del paquete (`1fe4ae8`, CI pendiente). El control JSON negativo para evaluación obsoleta pasa en ambos entornos en `1d4de6f`: si cambia el texto de condición y se conserva una evaluación TRUE vinculada al texto anterior, la ejecución rechaza el modelo.
- Editor visual: recorrido add/change/clear y exportación/importación/replay de la condición editada (`humidity is extremely low`); ambos workflows PASS en `5c772a0`. Se prueba que, tras cambiar el modelo fuente y volver a derivar, el paquete puede incluir propuestas nuevas solo si cada candidata conserva la procedencia del modelo vigente; ninguna decisión `ACCEPTED` del alcance anterior puede sobrevivir. El control pasa en `7150903` (navegador y motor sintético). La regresión adicional de restauración exacta del modelo tras invalidación pasa en `0851ee1` (navegador y motor sintético).
- Rutas cruzadas: transición condicional e incondicional en cada vía; cambio de condición invalida la evaluación ligada al texto anterior; modelos incondicionales y comportamiento histórico siguen siendo compatibles.
- Integración: demostrar que el derivador de correspondencias y la representación TGCV solo consumen el modelo validado y las correspondencias efectivas, sin que propuestas, rechazos o entradas obsoletas cambien el grafo TGCV, T_acc, alcanzabilidad o resultados de ejecución.

## 5. Siguiente control

El rechazo explícito de una evaluación condicional obsoleta dentro de un paquete íntegro a nivel de hashes ya pasa en navegador y Python (commit `b03971f`). El recorrido del editor visual por exportación/importación/replay pasa en el commit `5c772a0`. El control de exportación tras cambiar el modelo fuente pasa en ambos entornos en `7150903`: permite propuestas nuevas con procedencia actual y prohíbe conservar decisiones ACCEPTED del modelo anterior. El control de revisión/aceptación humana verifica persistencia de decisión, alcance modelo/catálogo, aplicación explícita, idempotencia, conflictos con declaraciones del usuario, invalidación e historial. La regresión de restauración del modelo tras invalidación pasa en `0851ee1` (navegador y motor sintético). El control específico para procedencia de una decisión humana derivada del transcriptor pasa en ambos workflows en `6c0329b` (runs `39947686882` y `39947686918`): verifica condición exacta `hay autorización`, hash del modelo transcrito, aceptación humana explícita, persistencia en exportación y replay independiente del paquete. La sincronización del test espera una propuesta `T_TRANSCRIBED_` y la UI expone la condición original en la evidencia. Las pruebas de evaluación obsoleta no sustituyen este control de procedencia. La PR debe seguir en borrador y sin fusionar hasta resolver o dividir explícitamente estos puntos.


### Incidencia de sincronización en pruebas de importación JSON

El control añadido para importar un JSON con una condición `TRUE` y rutas incondicionales independientes no llegó a evaluar ese escenario: la suite de navegador falló antes, porque una espera genérica por `Archivo cargado y validado` podía satisfacerse con el mensaje de una importación anterior. La aserción posterior leía entonces el modelo previo (`humidity is low`) en vez del archivo recién seleccionado (`conditional-model.json`). No hay evidencia en ese fallo de un defecto del importador. Se cambió la sincronización para esperar el nombre exacto de cada archivo. Corrección en `ee111d287d9bd9205a09528cb1627165b90f7a3b`; workflows pendientes.


### Estado de validación más reciente

**Invalidación de correspondencia efectiva y `T_acc` mostrado — PASS:** commit `ff44534bd96e17c18566eb92d9b46cf069d817de`; navegador y concordancia PASS ([run 39951762149](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39951762149)) y motor sintético PASS ([run 39951762111](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39951762111)). La prueba verifica que `T_HUMIDITY` está presente en la representación mientras la correspondencia efectiva está aplicada y desaparece después de invalidarla/restaurar el catálogo; conserva además comparaciones de estados alcanzables y trayectorias y comprueba que la correspondencia obsoleta no se reactiva. El workflow terminó capturas, paquete ZIP autónomo, verificación del artefacto y replay desde fuente limpia.

**Límite de evidencia:** el control valida la representación visible de `T_acc`, no la igualdad de un objeto formal independiente que enumere matemáticamente todas las transformaciones accesibles. Tampoco cierra por sí solo todos los casos de decisiones pendientes/rechazadas/obsoletas sobre cada resultado de ejecución. PR #95 permanece en borrador.

**Invalidación de correspondencia efectiva y restauración del catálogo — PASS:** commit `d5779dbe6c80dd2f4014b2b8eab0f2fae2fffde8`; navegador y concordancia PASS ([run 39951072166](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39951072166)) y motor sintético PASS ([run 39951072157](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39951072157)). La prueba captura los estados alcanzables con la correspondencia aceptada aplicada, cambia el catálogo para invalidarla, restaura el catálogo original, vuelve a ejecutar y exige que los estados alcanzables permanezcan iguales y que `T_HUMIDITY` no se reactive automáticamente. El workflow también completó capturas, verificación del ZIP autónomo y replay desde fuente limpia.

**Límite pendiente:** la prueba compara estados alcanzables antes y después de invalidar/restaurar el catálogo, pero no compara directamente `T_acc` ni todos los resultados de ejecución para cada estado (pendiente, rechazado y obsoleto). Mantener la PR #95 en borrador hasta completar esos controles o delimitar expresamente el alcance de aceptación.

**Invariancia de propuestas pendientes/rechazadas — corrección del baseline:** commit `5663ae56f3dff3e2fc09571a11ded36b3845daaa`; navegador y concordancia PASS ([run 39950514596](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39950514596)) y motor sintético PASS ([run 39950514626](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39950514626)). La prueba captura el grafo y los estados alcanzables después de una ejecución inicial, y compara la alcanzabilidad después de derivar propuestas, aceptar una y rechazar otra. La primera versión fallaba porque capturaba el grafo antes de ejecutar; se corrigió el orden del baseline sin retirar las aserciones. La suite de navegador terminó también las capturas, la verificación del ZIP autónomo y el replay desde fuente limpia.

**Límite pendiente:** el control compara los estados alcanzables del sistema para propuestas pendientes/rechazadas, pero aún no constituye una aserción directa sobre el conjunto `T_acc`, ni cubre en esta misma comparación la invalidez por decisiones obsoletas y sus resultados de ejecución. Mantener PR #95 en borrador hasta completar o acotar explícitamente esos controles.

**Invariancia de alcanzabilidad antes de aplicación explícita:** commit `06dea7d9b32a6155a060cbb2c773d6b8511f645b`; navegador y concordancia PASS ([run 39949816099](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39949816099)) y motor sintético PASS ([run 39949816249](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39949816249)). La prueba captura los estados alcanzables de la ejecución base, restaura/deriva la decisión ACCEPTED sin aplicarla, vuelve a ejecutar y exige igualdad de los conjuntos alcanzables. El workflow también terminó capturas, ZIP autónomo, verificación del paquete y replay desde fuente limpia.

**Límite pendiente:** la comparación demuestra invariancia al recuperar una decisión aceptada aún no aplicada. Falta una aserción equivalente sobre propuestas pendientes/rechazadas y decisiones obsoletas, además de una comprobación explícita de resultados de ejecución y del conjunto de transformaciones accesibles `T_acc`. La PR debe seguir en borrador hasta resolver ese alcance.

**Control de aislamiento de propuestas:** commit `5037a3c959fd31876538621604598b47cf4bf42d`; navegador y concordancia PASS ([run 39949103171](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39949103171)) y motor sintético PASS ([run 39949103170](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39949103170)). La regresión compara el grafo TGCV con su estado inicial después de derivar propuestas y después de aceptar una propuesta; también conserva el control de rechazo aprobado en `fd5b5f1`. La suite completa de navegador terminó además con capturas, ZIP autónomo verificado y replay desde fuente limpia.

**Cobertura adicional comprobada en la suite existente** (`web/cross_runtime_test.cjs`, mismo commit `5037a3c`): la aplicación explícita activa exactamente una correspondencia aceptada; la segunda aplicación no duplica el registro ni cambia su identidad; el mapeo efectivo queda separado de `model.tgcv_mapping`; los cambios del catálogo marcan los mapeos anteriores `STALE`, preservan historial y no reactivan una decisión aceptada al restaurar el catálogo; un cambio del modelo de origen también invalida los mapeos efectivos y conserva el motivo en el historial. La prueba vuelve a ejecutar el sistema tras los cambios de ámbito y comprueba que `T_HUMIDITY` no se muestra como activo cuando el catálogo anterior se restaura sin nueva aceptación.

**Límite de la evidencia:** estos son controles de ciclo de vida y ejecución del mapeo en el demostrador, no una comparación formal de conjuntos `T_acc` o de alcanzabilidad antes/después. Sigue pendiente una aserción directa sobre el conjunto de transformaciones accesibles y los resultados de ejecución para propuestas pendientes/rechazadas y decisiones obsoletas. La PR debe seguir en borrador y sin fusionar hasta resolver o dividir explícitamente ese punto.

Los workflows de navegador y motor sintético pasan para `6c0329bf8abd546e5597153b2d7a7fb3ac9f2caf`. Además del control de importación JSON de `ee111d2`, la suite verifica la procedencia de una correspondencia derivada del transcriptor: condición exacta, hash del modelo fuente, aceptación humana explícita, exportación y replay independiente.


### Estado posterior de los controles de importación

La importación de JSON con una condición `TRUE` vinculada y una ruta incondicional independiente pasa en navegador y motor sintético (`ee111d2`). La sincronización de la prueba espera el nombre exacto del archivo importado, evitando reutilizar un mensaje de estado anterior.
### Validación de correspondencias efectivas estructuradas

El commit `30ea6abf8d5d60d61cf91221ad72396fcd4eab9c` pasa los dos workflows: motor sintético ([run 39952347843](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39952347843)) y navegador/concordancia ([run 39952348144](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39952348144)). La prueba verifica en la capa estructurada de correspondencias efectivas que `T_HUMIDITY` está presente mientras la correspondencia aceptada es efectiva y ausente después de invalidarla y restaurar el catálogo; conserva además las comprobaciones de alcanzabilidad, trayectorias y no reactivación automática. El workflow de navegador completó capturas, construcción/verificación del ZIP y replay desde fuente limpia.

**Alcance:** esto verifica el conjunto estructurado de correspondencias efectivas derivadas; no debe describirse como prueba exhaustiva de la definición formal completa de `T_acc`. Siguen pendientes de cobertura explícita los efectos de decisiones pendientes/rechazadas/obsoletas sobre cada resultado de ejecución. PR #95 permanece en borrador.
### Propuestas aceptadas sin aplicar y rechazadas — control de correspondencias efectivas

Commit `632a808366ecf92e847f32dba37384593fdcb6f1`: motor sintético PASS ([run 39952705673](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39952705673)) y navegador/concordancia PASS ([run 39952705789](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39952705789)). La prueba exige que las propuestas aceptadas pero aún no aplicadas y las rechazadas no incorporen `T_HUMIDITY` al conjunto estructurado de correspondencias efectivas, además de conservar la invariancia de estados alcanzables. El workflow de navegador completó capturas de escritorio/móvil, distribución ZIP autónoma, verificación del artefacto y replay desde fuente limpia.

**Alcance pendiente:** la prueba valida la separación entre estado de revisión y correspondencias efectivas; no sustituye una matriz completa de resultados de ejecución para todos los estados de revisión, ni demuestra por sí sola la equivalencia formal de las correspondencias efectivas con `T_acc`. PR #95 sigue en borrador.
### Propuestas pendientes/rechazadas: invariancia de ejecución — PASS

Commit `52305ceb878b00aa587e69a7d1ecb39977ce108b`: motor sintético PASS ([run 39953076116](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39953076116)) y navegador/concordancia PASS ([run 39953076040](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39953076040)). La regresión compara, por escenario, los estados alcanzables y las trayectorias (estado y transición) antes y después de registrar propuestas pendientes/rechazadas, y mantiene la comprobación de que no se incorporan al conjunto estructurado de correspondencias efectivas. El workflow de navegador completó capturas de escritorio/móvil, ZIP autónomo, verificación del artefacto y replay desde fuente limpia.

**Alcance:** confirma invariancia para los estados de revisión cubiertos por esta prueba; no constituye todavía una matriz exhaustiva de todos los estados (incluida obsolescencia) ni prueba por sí sola la equivalencia formal entre correspondencias efectivas y `T_acc`. PR #95 sigue en borrador.
### Estados de revisión aislados: pendiente y aceptada sin aplicar — PASS

Commit `e83e7e35b2caeccd6984b4651728dfd319567d25`: motor sintético PASS ([run 39954841145](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39954841145)) y navegador/concordancia PASS ([run 39954841140](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39954841140)). La prueba ejecuta el sistema con propuestas pendientes y, por separado, después de aceptar una propuesta sin aplicarla; compara por escenario los estados alcanzables y las trayectorias respecto de la línea base. El workflow terminó capturas de escritorio/móvil, construcción y verificación del ZIP autónomo y replay desde fuente limpia.

**Alcance:** los estados pendientes y aceptada-sin-aplicar quedan cubiertos de forma aislada en ejecución. El estado rechazado continúa cubierto por el control combinado previo; la matriz completa de todos los estados de revisión y la equivalencia formal con `T_acc` siguen siendo cuestiones separadas. PR #95 permanece en borrador.
