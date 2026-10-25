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
### Rechazo aislado: invariancia de ejecución y persistencia — PASS

Commit `c8df92afc376925259ed84be8135ec5c1e6877be`: motor sintético PASS ([run 39955722967](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39955722967)) y navegador/concordancia PASS ([run 39955722941](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39955722941)). En un contexto de navegador nuevo, la prueba parte de una ejecución de referencia, rechaza una propuesta sin otras decisiones, vuelve a ejecutar y compara los estados alcanzables y las trayectorias por escenario. Verifica además que la propuesta rechazada no entra en el conjunto estructurado de correspondencias efectivas y que el rechazo persiste al regenerar propuestas. La CI de navegador completó capturas, ZIP autónomo, verificación del artefacto y replay desde fuente limpia.

**Alcance:** queda validado el rechazo aislado en el flujo probado. La cobertura exhaustiva de estados obsoletos y la equivalencia formal de correspondencias efectivas con `T_acc` siguen pendientes. PR #95 permanece en borrador.

### Invalidación aislada por cambio del modelo de origen — PASS

Commit `fe6866176a25d9becbe972735d33a9dfae72d289`: motor sintético PASS ([run 39958782198](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39958782198)) y navegador/concordancia PASS ([run 39958782194](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39958782194)). En contexto de navegador independiente, la prueba crea una correspondencia aceptada y aplicada por la interfaz, modifica el modelo de origen y verifica la persistencia de `STALE` con motivo, la ausencia de correspondencias actuales activas y efectivas, la ejecución del modelo editado, la exclusión de la transformación obsoleta del grafo TGCV y que la propuesta regenerada no restaura la decisión anterior. El workflow de navegador completa también capturas, ZIP autónomo, verificación del artefacto y replay desde fuente limpia.

**Alcance:** valida el ciclo aislado cubierto por este escenario. No demuestra por sí solo la equivalencia formal global entre las correspondencias efectivas y `T_acc`; esa cuestión permanece separada. PR #95 sigue en borrador.

### Ciclo de revisión tras invalidación del modelo de origen — PASS

Commit `44961cc00b22da59a2d0666a174330081743853c`: motor sintético PASS ([run 39959862621](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39959862621)) y navegador/concordancia PASS ([run 39959863200](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39959863200)). La prueba de navegador continúa el escenario aislado: tras aceptar y aplicar una correspondencia, cambiar el modelo y verificar su invalidación, deriva una propuesta nueva, registra un rechazo humano explícito, vuelve a derivar y comprueba que el rechazo persiste, no quedan correspondencias actuales activas y efectivas, y la transformación obsoleta sigue ausente del grafo TGCV. La suite de navegador y Python también se reproduce desde un archivo fuente limpio.

**Alcance:** valida la secuencia de revisión concreta ejercitada. No sustituye una verificación formal de todas las transiciones de estado ni prueba por sí sola la equivalencia global entre las correspondencias efectivas y `T_acc`. PR #95 sigue en borrador.

### Auditoría de transiciones del ciclo de correspondencias — estado de cobertura

Auditoría documental del contrato `TGCV_FULL_CHAIN_DEMONSTRATOR_CONTRACT_001.md` frente a `web/cross_runtime_test.cjs`, revisada en el head `cdf9b11faa9a784327b6532e8534bae042cfc7c8`.

| Transición/propiedad | Evidencia localizada | Estado |
|---|---|---|
| Propuesta → aceptación humana | Prueba de navegador acepta una propuesta y verifica procedencia/revisión | Cubierta en los escenarios existentes |
| Aceptada → efectiva | Aplicación explícita por UI y comprobación de una correspondencia activa | Cubierta en el escenario de materialización probado |
| Rechazada → sin efecto operativo | Rechazo aislado; comprueba que no entra en el conjunto efectivo y persiste al regenerar | PASS en CI del commit `c8df92afc376925259ed84be8135ec5c1e6877be` |
| Efectiva → obsoleta por cambio de modelo | Invalida con motivo persistido, excluye estado efectivo y grafo TGCV | PASS en CI del commit `fe6866176a25d9becbe972735d33a9dfae72d289` |
| Obsoleta → nueva propuesta pendiente → rechazo nuevo | Regeneración, rechazo explícito y segunda regeneración; sin reactivación | PASS en CI del commit `44961cc00b22da59a2d0666a174330081743853c` |
| Restaurar el modelo anterior tras invalidación | El test integrado verifica que no se restaura automáticamente la aceptación ni la transformación en el grafo | Cubierta por el escenario integrado; no sustituye la prueba aislada anterior |
| Importar/reproducir decisiones sin activar automáticamente | El contrato exige snapshot de auditoría y acción explícita; hay validaciones de paquete, pero no se identifica aquí una matriz exhaustiva de todas las transiciones importadas | Brecha de cobertura por transición |
| Conflicto entre mapping declarado y mapping derivado / dos mappings efectivos incompatibles | El contrato exige `CONFLICT_NEEDS_REVIEW` y preservar el mapping declarado | Hay evidencia específica de no sobrescritura/no duplicación y de invariancia de ejecución tras restaurar explícitamente el modelo; la matriz exhaustiva por pares y la persistencia nativa de esta declaración siguen sin demostrarse |

**Conclusión de auditoría:** están validadas varias secuencias concretas de revisión, aplicación, rechazo e invalidación; no existe evidencia suficiente para marcar completa la matriz global de transiciones. Los estados contractuales `PENDING_REVIEW`, `ACCEPTED_NOT_APPLIED`, `EFFECTIVE`, `CONFLICT_NEEDS_REVIEW`, `STALE` y `REJECTED` deben mantenerse diferenciados; los nombres internos observados en las pruebas no autorizan a tratarlos como estados equivalentes. Siguiente brecha prioritaria: añadir pruebas aisladas para import/replay sin activación y para conflictos de mappings, empezando por el caso de importación sin mutación del estado local. No cambiar el motor ni promover PR #95 mientras estos gates sigan abiertos.

### Evaluación de paquete importado sin mutación de decisiones locales — PASS

Commit `c93a56e66c904e5f40e692f601d02d6d1a67318d`: motor sintético PASS ([run 39994457805](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39994457805)) y navegador/concordancia PASS ([run 39994457766](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39994457766)). En contexto de navegador independiente se establece primero un rechazo humano local, se captura el estado persistido de revisión y las correspondencias efectivas, se evalúa un paquete JSON válido y se compara el estado posterior. La prueba exige que la evaluación se verifique por replay, que las decisiones locales y las correspondencias efectivas no cambien y que el rechazo siga visible. La reproducción desde archivo fuente limpio también pasó.

**Alcance:** este control valida la evaluación del paquete en el flujo probado; no demuestra por sí solo que toda modalidad de importación/replay o toda clase de paquete carezca de efectos secundarios. La cobertura de conflictos entre mappings sigue pendiente. PR #95 continúa en borrador.

### Colisión con correspondencia derivada ya efectiva — PASS

Commit `ac894914b650e5db2f3a47a3e5c2bdc5447957df`: motor sintético PASS ([run 39996754232](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39996754232)) y navegador/concordancia PASS ([run 39996754253](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39996754253)). El test usa un modelo aislado con transiciones `A→B` y `A→C`, y verifica que una propuesta aceptada que reutiliza una transformación ya asignada por otra correspondencia efectiva no se materializa y devuelve `CONFLICT_NEEDS_REVIEW` con el motivo esperado. La reproducción desde archivo fuente limpio, la distribución autónoma y la verificación del ZIP también pasaron.

**Alcance:** esto cubre una colisión efectiva-efectiva por reutilización de transformación. No demuestra aún todos los pares de conflicto del contrato ni la resolución humana persistente para cada clase de conflicto. PR #95 sigue en borrador; no se ha fusionado.

### Persistencia del rechazo humano de propuesta NEEDS_REVIEW — PASS

Commit `bf160d494729170c69fb6dee7254df23972c3d13`: motor sintético PASS ([run 39998114312](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39998114312)) y navegador/concordancia PASS ([run 39998114360](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39998114360)). La prueba del navegador genera propuestas ambiguas `NEEDS_REVIEW`, registra el rechazo humano explícito, comprueba su persistencia en almacenamiento local y verifica que la decisión y el contenido persistido permanecen iguales tras regenerar propuestas. También pasa la reproducción desde archivo fuente limpio y la verificación del paquete autónomo.

**Alcance:** demuestra persistencia del rechazo para el escenario de propuestas ambiguas del test; no demuestra todavía todas las clases de resolución de conflictos ni una aprobación general de la integración del derivador. PR #95 permanece abierta, en borrador y sin fusionar.

### Integridad de mapping declarado tras rechazo de propuesta derivada — PASS

Commit de prueba `df211d77e9ded682ec2d9727949bdadd6f0903e6`: motor sintético PASS ([run 39998776768](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39998776768)) y navegador/concordancia PASS ([run 39998776906](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/39998776906)). La prueba compara el mapping TGCV declarado por el usuario antes y después de rechazar una propuesta derivada y exige igualdad exacta; también verifica que el rechazo no cambie estados alcanzables ni trayectorias. La reproducción desde archivo fuente limpio, la distribución autónoma y la verificación del ZIP pasaron.

**Alcance:** evidencia de integridad del mapping declarado para este escenario de rechazo. No equivale a cobertura completa de todas las clases de conflicto ni a validación científica de TGCV. PR #95 continúa en borrador y sin fusionar.

### Aceptación humana no activa ni altera mappings declarados/efectivos — PASS

Commit de prueba `857d18f5197e00a442356c336f7839e5323bc019`: motor sintético PASS ([run 40000012125](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40000012125)) y navegador/concordancia PASS ([run 40000012112](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40000012112)). La prueba registra la decisión humana `ACCEPTED` y verifica que aceptar la propuesta, sin ejecutar la acción separada de aplicación, no modifica el mapping TGCV declarado ni las correspondencias efectivas. La reproducción desde archivo fuente limpio y la distribución autónoma verificada también pasaron.

**Alcance:** demuestra la separación entre aceptación de revisión y aplicación para el escenario probado; no acredita por sí sola todos los tipos de incompatibilidad ni el ciclo completo de aplicación. PR #95 sigue abierta, en borrador y sin fusionar.

### Control de persistencia de conflictos tras recarga — PASS

Commit de prueba: `032c142f67ad108fd3bd36abae3da85f58b1e4e3`. Los workflows de navegador/cross-runtime y motor sintético finalizaron `success` sobre ese SHA (runs [40142786964](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40142786964) y [40142786941](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40142786941)). La prueba del navegador resuelve explícitamente un conflicto entre dos candidatas, comprueba que la aplicación repetida no duplica la correspondencia efectiva, recarga la página y reconstruye el mismo ámbito modelo/catálogo. Después de derivar de nuevo, verifica que se restauran las decisiones `ACCEPTED` y `REJECTED`; al volver a aplicar, exige exactamente una correspondencia efectiva (`t_ab_primary`) y confirma que la candidata rechazada no se reactiva.

**Alcance y límite:** esto cierra el caso automatizado de persistencia de decisiones y no-resurrección tras recarga para ese fixture. No demuestra todos los conflictos posibles ni cierra la brecha más amplia señalada arriba: una comparación directa del conjunto estructurado `T_acc` y de los resultados de ejecución para estados `PENDING_REVIEW`, `REJECTED` y `STALE`. La PR #95 sigue en borrador y sin fusionar hasta que esos controles se cubran o se acote formalmente su aceptación.

### Correspondencias efectivas obsoletas tras cambio del modelo de origen — PASS

Commit de prueba: `652b6008a9e2976485763b49ee116418cce9e4db`. Los workflows de motor sintético y navegador/cross-runtime finalizaron `success` para el head de la PR (runs [40143239635](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40143239635) y [40143239667](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40143239667)). El test integrado comprueba, tras un cambio del modelo de origen que invalida una correspondencia previamente efectiva, que la ejecución sigue completándose, que estados alcanzables y trayectorias se mantienen si no cambia el conjunto de transiciones, que la correspondencia obsoleta no aparece en el grafo y que el conjunto estructurado de mappings efectivos/`T_acc` la excluye.

**Alcance y límite:** PASS para este escenario automatizado de invalidación por cambio del modelo de origen, junto con las comprobaciones previas de invalidación por catálogo. No cierra por sí solo todas las combinaciones de conflicto ni las tres vías de entrada de condiciones; la aceptación global de correspondencias sigue PARTIAL según el contrato §10.6. PR #95 permanece abierta, en borrador y sin fusionar.

## 13. Integrated direct `T_acc` / execution consistency and application-time conflict — 2026-10-25

Commit `f0cd9edd0870fdc33f70fbbf270f4bb51deb461e` adds grouped assertions to the browser suite that compare the structured operational `T_acc` transformations with the mappings of transitions present in the selected scenario's enumerated trajectories. The assertions cover pending-only review, pending plus rejected review, an active effective mapping, invalidation after target-catalogue change, invalidation after source-model change, and the application-time conflict lifecycle.

The application-time conflict fixture contains two system transitions (`t_ab_primary` and `t_ab_duplicate`) competing for the same TGCV target. The integrated test verifies: baseline execution with no fabricated TGCV mapping; fail-closed behavior while the conflict is unresolved (zero effective mappings); persistence of accepted/rejected decisions; explicit rejection leaving only `t_ab_primary` effective; consistency of structured `T_acc` with execution after resolution; idempotent reapplication; and restoration of accepted/rejected decisions after reload without resurrecting the rejected candidate.

**Exact-head CI:** browser/cross-runtime PASS — [run 40144746690](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40144746690); synthetic engine PASS — [run 40144746683](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40144746683).

**Scope limit:** this closes the specific direct-equivalence and conflict-resolution scenarios above; it does not establish a formal mathematical proof of the canonical scientific definition of `T_acc`, exhaustive coverage of every pair/type of conflict, or complete import/replay non-activation behavior for every decision state. Audit-only package assessment/import isolation is already covered by the existing browser suite: it compares persisted local review/effective state before and after package assessment and verifies that the visible local rejection remains intact; the review-snapshot replay tests also preserve the snapshot without activating it. The next grouped gate is therefore not a duplicate of that coverage: it is a general user-facing conflict-resolution matrix across conflict types and candidate order, with each unresolved case fail-closed and each explicit resolution checked for effective-set, T_acc, execution, persistence and reload invariants. PR #95 remains draft, open and unmerged; `main` is untouched, and no scientific execution is authorized.

### Ambigüedad de destino para una transición de origen: invariancia de ejecución — PASS

Commit `4c65ae409f2d58da73e520d5691a17c626adacb4`: motor sintético PASS ([run 40187429450](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40187429450)) y navegador/concordancia PASS ([run 40187429511](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40187429511)). La prueba establece una ejecución de referencia antes de derivar candidatas para una transición con dos transformaciones de destino compatibles. Después de la derivación, comprueba que ambas candidatas siguen en `NEEDS_REVIEW`, que no se habilita su aceptación, que no se materializan mappings efectivos y que la ejecución conserva los mismos estados alcanzables y trayectorias. En ambos puntos compara también el `T_acc` estructurado con las transformaciones reflejadas por la ejecución.

**Alcance:** cierra la invariancia de ejecución para este fixture de ambigüedad de origen/destino. No cierra la matriz general de resolución humana para todos los tipos de conflicto: el escenario de conflicto efectivo-efectivo y su resolución persistente ya tiene evidencia separada, pero no deben inferirse de estos tests todas las combinaciones cruzadas posibles. PR #95 sigue abierta, en borrador y sin fusionar; `main` permanece intacta.

### Resolución explícita de ambigüedad de destino con persistencia y recarga — PASS

Commit de prueba `334b38f5b1ab7e2b12827e4af51cae3cb2b33639`: navegador/concordancia PASS ([run 40188192474](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40188192474)) y motor sintético PASS ([run 40188192444](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40188192444)). La prueba deriva dos candidatas con la misma frontera exacta y confirma `NEEDS_REVIEW`; después reduce el catálogo a una única transformación, acepta explícitamente la propuesta, aplica la correspondencia y compara el conjunto efectivo `T_acc` con la ejecución. Tras recargar, comprueba que la correspondencia continúa efectiva y que se conservan los estados alcanzables y las trayectorias.

**Límite:** el resultado cubre esta ruta de desambiguación mediante refinamiento del catálogo y aceptación explícita. No demuestra todas las clases de conflicto ni todos los caminos de resolución. La PR #95 continúa abierta y en borrador; no se ha fusionado y `main` permanece intacta.

### Colisión de candidata con una correspondencia ya efectiva: rechazo explícito y persistencia — PASS

Commit `3ad79524c2b842348487d45431738b009b396024`: navegador/cross-runtime PASS ([run 40189464294](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40189464294)) y motor sintético PASS ([run 40189464043](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40189464043)). La prueba establece primero `t_ab_first → T_SHARED_AB` como correspondencia efectiva. Al aceptar y aplicar una segunda candidata `t_ab_second` que compite por la misma transformación, exige el estado `conflict-needs-review` y cero correspondencias efectivas mientras la colisión siga sin resolver (fail-closed). Tras rechazar explícitamente la segunda candidata, vuelve a aplicar y exige que solo `t_ab_first → T_SHARED_AB` quede efectiva; después compara `T_acc` estructurado con la ejecución y verifica la conservación de las correspondencias y trayectorias después de recargar.

**Alcance y límite:** PASS para este escenario de colisión contra una correspondencia que ya era efectiva y para su resolución explícita. Combinado con las pruebas existentes de conflicto por lote, ambigüedad de destino y persistencia tras recarga, amplía la evidencia, pero no prueba exhaustivamente todas las combinaciones de conflictos entre mappings declarados, derivados y efectivos. La PR #95 sigue abierta, en borrador y sin fusionar; `main` permanece intacta.

**Siguiente gate integrado:** matriz cruzada de tipos de conflicto y orden de candidatas. Para cada fixture, registrar el estado previo, verificar que el conflicto sin resolver no deja un conjunto parcial efectivo, comprobar la resolución humana correspondiente y comparar mapping declarado, mappings efectivos, `T_acc`, estados alcanzables y trayectorias antes/después de recarga. No rebajar aserciones ni inferir validez científica a partir del PASS de CI.

### Colisión integrada con orden de aceptación inverso — PASS

Commit `f7f8a79535b9e81f56b51ed1af1e1f3bf56d2b92`: navegador/cross-runtime PASS ([run 40190003417](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40190003417)) y motor sintético PASS ([run 40190003487](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40190003487)). La prueba UI invierte qué candidata se acepta y luego conserva: acepta primero `t_ab_duplicate`, provoca una colisión con `t_ab_primary`, exige cero mappings efectivos hasta resolver, rechaza explícitamente la candidata principal y verifica que solo `t_ab_duplicate → T_SHARED_AB` queda efectiva. Comprueba la concordancia entre `T_acc` y ejecución, recarga y confirma la misma correspondencia y las mismas trayectorias.

**Alcance:** el caso inverso de resolución humana ya tiene evidencia automatizada en ambos workflows. No equivale a una prueba exhaustiva de todas las permutaciones ni de todas las clases de conflicto. La PR #95 sigue abierta, en borrador y sin fusionar; `main` permanece intacta.

## 6. Matriz contractual integrada de conflictos de correspondencia

**Base de evidencia:** suite `web/cross_runtime_test.cjs`, commit `a0a9b2fc3907ad5aa5d1fbd9193f1d3b8c198ad3`; ambos workflows PASS ([navegador](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40190227625), [motor sintético](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40190227644)). Esta matriz clasifica evidencia existente; no declara aceptación exhaustiva del contrato.

| Clase de conflicto | Detección/abstención | Orden de entrada | Resolución explícita en UI | Persistencia/recarga | `T_acc` vs ejecución y trayectorias | Estado |
|---|---|---|---|---|---|---|
| Lote: dos transiciones distintas compiten por una transformación | **PASS**: cero mappings; ambas candidatas reciben `CONFLICT_NEEDS_REVIEW` | **PASS**: lote directo y lote invertido generan los mismos IDs de conflicto | **PASS**: aceptación de ambas bloqueada como lote; se prueba rechazo explícito de una y aplicación de la otra | **PASS**: decisión ACCEPTED/REJECTED y mapping seleccionado se conservan tras recarga | **PASS**: comparación estructurada de `T_acc` con ejecución y trayectorias antes/después de recarga | Cubierto en los fixtures probados |
| Ambigüedad: una transición fuente tiene varios destinos exactos posibles | **PASS**: ambas candidatas `NEEDS_REVIEW`; ninguna se materializa | **PASS**: invertir candidatas no cambia el conjunto de conflictos | **PASS, con refinamiento del catálogo**: la suite elimina la ambigüedad, obtiene una única candidata `PROPOSED`, exige aceptación humana y aplica explícitamente | **PASS**: tras recarga se vuelve a derivar y se conserva la decisión/mapping efectivo | **PASS en el fixture probado**: compara `T_acc` estructurado con ejecución, alcanzabilidad y trayectorias antes/después de recarga | Ciclo integrado cubierto para resolución mediante refinamiento del catálogo |
| Colisión con una correspondencia efectiva previa | **PASS**: la aplicación conflictiva falla cerrada y no deja mappings efectivos parciales | **PASS** para la secuencia de conflicto probada; no equivale a enumerar todas las permutaciones | **PASS**: rechazar explícitamente la candidata conflictiva permite aplicar la selección no conflictiva | **PASS**: el mapping elegido se conserva y se reaplica tras recarga | **PASS**: `T_acc` estructurado concuerda con la ejecución y las trayectorias se conservan en el fixture probado | Cubierto en ambos órdenes de selección probados |
| Correspondencia declarada por el usuario frente a derivación | **PASS**: derivar no reescribe la declaración exacta ni crea mappings derivados efectivos duplicados | **PASS dentro del fixture declarado↔declarado**: C12/C13/C23 y 60 permutaciones; los conflictos declarada↔derivada tienen pruebas específicas de orden, aún no integradas en la matriz cruzada | **Parcial**: no se acepta una propuesta para sobrescribir la declaración; falta el ciclo cruzado común de resolución humana para los conflictos declarada↔derivada | **PASS** para recuperar el borrador local tras `reload()` sin reinyección manual (commit `51fa006fcd186b1903e6e7947e728c37e17f0ebd`) | **PASS en fixtures individuales**: se compara `T_acc` con ejecución y se verifican invariantes; falta consolidar esas aserciones en un único ciclo cruzado entre clases | Integridad, permutaciones declarada↔declarada y recarga básica cubiertas; matriz cruzada entre clases pendiente |

### Evidencia adicional: destino alternativo para una transición declarada — PASS

Commit `52220126663025ac0b650b89a6bdf69f2981e0b2`; ambos workflows PASS: [motor sintético, run 40192742484](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40192742484) y [navegador/concordancia, run 40192742284](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40192742284).

La prueba UI declara `t_ac → T_CONFLICT_AB` y presenta una transformación alternativa `T_CONFLICT_AC` para el mismo límite de estados. Verifica que la declaración exacta permanece intacta, no se genera una propuesta derivada alternativa ni se materializa un mapping efectivo, y la interfaz informa del conflicto con la declaración del usuario. Además, ejecuta el modelo antes y después de la derivación conflictiva y compara estados alcanzables y trayectorias; la aserción estructurada de `T_acc` debe concordar con la ejecución.

**Límite de alcance:** esta evidencia cierra el fixture de destino alternativo para una transición declarada y su invariancia de ejecución. La recuperación del borrador local tras recarga sin reinyección manual se valida separadamente en el commit `51fa006fcd186b1903e6e7947e728c37e17f0ebd`. Lo pendiente no es repetir esa prueba básica, sino integrar los conflictos declarada↔derivada en la matriz cruzada y comparar en un ciclo común las decisiones, mappings efectivos, `T_acc`, ejecución y trayectorias.

### Inventario de pares de conflicto — corte verificable

Este inventario separa clases semánticas de conflicto de permutaciones exhaustivas. Los estados se asignan solo a los fixtures localizados en `web/cross_runtime_test.cjs`; no implican que todas las variantes de datos o los órdenes posibles estén cubiertos.

| Par / relación en conflicto | Evidencia localizada | Estado del fixture | Falta para cerrar la clase completa |
|---|---|---|---|
| Derivada ↔ derivada: dos transiciones fuente compiten por una transformación TGCV | Ciclo integrado de conflicto por lote; inversión del orden y resolución explícita | **PASS** | Enumerar todas las permutaciones/candidatas equivalentes no es parte del fixture actual |
| Derivada ↔ derivada: una transición fuente tiene más de un destino exacto candidato | Ambigüedad, abstención, refinamiento de catálogo, aceptación y recarga | **PASS** en el ciclo probado | Variantes adicionales de catálogo fuera del fixture |
| Derivada ↔ efectiva: la nueva candidata colisiona con un mapping efectivo ya activo | Validación de materialización y ciclo de conflicto de UI | **PASS** en los casos probados | No asumir exhaustividad de todas las combinaciones/órdenes |
| Declarada ↔ derivada: misma transición fuente, destino alternativo | Test UI `t_ac → T_CONFLICT_AB` frente a destino alternativo; ambos workflows PASS en commit `52220126663025ac0b650b89a6bdf69f2981e0b2` | **PASS**: preserva declaración, no propone/materializa alternativa y mantiene invariantes de ejecución | La variante inversa de orden de candidatas se comprueba además en commit `37c4f526ce66acbbd8346fe886dd154642919cd7`; no equivale a enumerar todas las variantes de datos/catálogo |
| Declarada ↔ derivada: otra transición fuente reclama el destino TGCV declarado | Test UI de colisión con destino declarado; exige cero propuestas y cero mappings efectivos | **PASS** en el fixture localizado | Falta integrar este fixture en la matriz cruzada común con la clase anterior y verificar `T_acc`/ejecución/recarga en el mismo ciclo; no se afirma exhaustividad de todos los datos posibles |
| Declarada ↔ declarada: dos transiciones comparten destino TGCV o una transición declara destinos múltiples | Suite agrupada en commit `2ae4829273f81ab27209a52640c4fd3a3489d271`; Motor sintético PASS ([run 40195539421](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40195539421)) y Navegador/concordancia PASS ([run 40195539418](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40195539418)). Incluye C12/C13/C23 y las 60 permutaciones únicas del fixture, comparando firma semántica normalizada, preservación exacta del orden de cada entrada y cero propuestas | **PASS** para las tres combinaciones y las 60 permutaciones de este fixture | No quedan permutaciones pendientes dentro de este fixture; el pendiente es la interacción con otras clases de conflicto |
| Declarada ↔ declarada: invariancia al invertir el orden de los mappings conflictivos | Test integrado añadido en `58cb4a39e1ecee988cec381714ac3b5a4d7b51d4`; ambos workflows PASS. Comprueba que el número de clases de conflicto no cambia, no se generan propuestas y la lista declarada conserva el orden de entrada invertido | **PASS** para la inversión de orden de los cuatro mappings del fixture | No reabrir las 60 permutaciones ya cerradas; falta integrar esta evidencia en la matriz cruzada global |
| Declarada ↔ derivada aceptada: aparece o cambia la declaración después de revisar la candidata | Test de validación antes de aplicar; se fuerza el guard de conflicto declarado manteniendo actualizado el hash de fuente | **PASS** en validación de materialización | No equivale a un ciclo UI persistido de extremo a extremo |
| Efectiva ↔ efectiva: un cambio de modelo invalida una correspondencia efectiva previa | Test de invalidación por cambio de modelo y control de decisión obsoleta | **PASS** en el fixture | Variantes de cambio fuera del caso cubierto |
| Declaración ↔ recarga de página: recuperar el modelo declarado sin volver a inyectarlo | Commit `51fa006fcd186b1903e6e7947e728c37e17f0ebd`; test Playwright compara el modelo completo tras `reload()` sin reinyección manual; ambos workflows PASS | **PASS** para la recuperación del borrador local tras recarga | Perfiles/orígenes distintos o almacenamiento borrado solo son pendientes si están dentro del contrato de persistencia; no abrirlos por defecto |

**Conteo del inventario:** 10 clases con evidencia de fixture (PASS dentro del alcance descrito). La clase declarada ↔ declarada incluye C12/C13/C23 y 60 permutaciones únicas validadas en ambos workflows. El borrador local se recupera tras recarga sin reinyección manual. El pendiente global son las interacciones entre clases distintas, no las 60 permutaciones ya cerradas.

### Criterios para cerrar el gate

1. Mantener separados los resultados de detección, materialización, resolución humana, persistencia y ejecución. Un PASS de una columna no implica PASS de las restantes.
2. Para cada fila que se declare cerrada, conservar evidencia de: estado previo, estado en conflicto, decisión explícita, conjunto de mappings efectivos, `T_acc` estructurado, alcanzabilidad, trayectorias y repetición tras recarga.
3. Para los casos de orden, comparar los resultados normalizados (IDs de candidatos/conflictos y mapping final), no solo que ambos órdenes terminen sin excepción.
4. Mantener la evidencia del ciclo de ambigüedad resuelta por refinamiento del catálogo. Para mappings declarados, mantener la prueba de recuperación del borrador local tras recarga (sin reinyección manual) y completar las colisiones por pares antes de afirmar que la matriz completa de clases de conflicto está cerrada.
5. No rebajar aserciones, no convertir automáticamente `NEEDS_REVIEW` en `PROPOSED`, y no usar los resultados de CI como evidencia de validez científica general de TGCV.

**Conclusión del gate:** cobertura fuerte para lote competitivo, colisión contra mapping efectivo, ciclo de ambigüedad resuelto por refinamiento del catálogo, integridad del mapping declarado durante derivación/ejecución, los patrones declarada ↔ declarada con C12/C13/C23 y sus 60 permutaciones, los dos patrones declarada ↔ derivada identificados y recuperación del borrador local tras recarga. El pendiente real es integrar los tipos de conflicto entre sí en una matriz cruzada común y completar en ese ciclo las comparaciones de mappings declarados/efectivos, `T_acc`, ejecución, alcanzabilidad, trayectorias, decisiones y recarga. No se reabre la suite de 60 permutaciones. Los límites de perfiles/orígenes y borrado de almacenamiento quedan condicionados al contrato de producto. El gate contractual integrado permanece **PENDIENTE**. La PR #95 permanece abierta, en borrador y sin fusionar.



## 6. Evidencia del bloque final de integración cruzada — 2026-10-25

**Resultado del bloque ejecutado:** **PASS en ambos workflows**, commit `17ac9e28f182dee6707eeb6cb31cb1bfd23de858`.

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40198397842)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40198397820)

El caso integrado nuevo comprueba una colisión entre una correspondencia declarada y una candidata derivada que intenta reclamar la misma transformación TGCV: la declaración permanece sin cambios; la candidata incompatible se excluye con evidencia visible; una candidata independiente puede aceptarse y materializarse; y el modelo declarado se recupera tras recarga nativa sin reinyección manual.

**Límite de la evidencia:** el fixture de colisión contiene aristas duplicadas deliberadamente no ejecutables. Por ello, no se usa este caso para afirmar invariantes de ejecución, alcanzabilidad o trayectorias. Esas aserciones permanecen en el caso de ciclo de vida integrado independiente. Este PASS tampoco demuestra exhaustividad de todas las combinaciones entre clases de conflicto.

**Estado del gate global:** **PENDIENTE**. Se cierra este bloque concreto, sin reabrir las 60 permutaciones declarada↔declarada. Para cerrar el gate global sigue siendo necesario consolidar y comprobar la matriz cruzada común de todas las clases de conflicto y sus invariantes conjuntas.


## 7. Gate de cierre consolidado — un único bloque, dos workflows

Esta sección sustituye la lectura dispersa de las brechas descritas en los apartados anteriores. **No se abren pruebas individuales ni se repiten permutaciones ya aprobadas.**

### Cobertura reutilizable ya acreditada

- Las 60 permutaciones declarada↔declarada: PASS; no reabrir.
- Colisión declarada↔derivada y conservación de la declaración tras recarga: PASS en el bloque documentado arriba.
- Ciclo de vida de correspondencias efectivas, aplicación explícita, idempotencia, conflicto fail-closed, decisión explícita de rechazo y restauración tras recarga: existen pruebas integradas previas.
- El helper `assertStructuredTAccMatchesExecution` compara el `T_acc` operacional estructurado con las transformaciones de las transiciones que aparecen en las trayectorias enumeradas. Esta comprobación no equivale a una demostración formal independiente de todas las transformaciones accesibles.

### Único bloque de cierre pendiente

Consolidar en la suite integrada existente una secuencia con el mismo fixture controlado y comparar snapshots semánticos en estos estados:

| Estado | Aserciones mínimas |
|---|---|
| Baseline, antes de derivar | Modelo validado, mappings declarados/efectivos, `T_acc`, resultado de ejecución, alcanzabilidad y trayectorias |
| Propuestas pendientes | Mismos resultados operacionales que baseline; cero efecto de propuestas |
| Propuesta rechazada | Mismos resultados operacionales que baseline; decisión rechazada persistida; ningún mapping rechazado efectivo |
| Mapping aplicado y después obsoleto por cambio de ámbito | `T_acc`, grafo, resultado, alcanzabilidad y trayectorias coherentes con la retirada del mapping; historial `STALE` preservado |
| Recarga/reaplicación permitida | Sin reinyección del modelo; decisiones restauradas; ningún rechazo ni mapping obsoleto reactivado; reaplicación idempotente |

Los snapshots se comparan por contenido normalizado (IDs de mappings y transformaciones, resultados por escenario, estados alcanzables y secuencias de trayectorias), no por texto de estado ni por contadores de UI. Los resultados de ejecución, `T_acc` y alcanzabilidad se mantienen como dimensiones separadas.

**Presupuesto de cierre: 1 bloque automatizado agrupado y 2 ejecuciones de CI** sobre el mismo commit: Navegador y concordancia + Motor sintético. Las variantes se iteran dentro de la suite; no son workflows separados. Solo se repite el workflow afectado si el bloque falla.

**Estado real:** PENDIENTE de implementar/verificar esta comparación consolidada y obtener PASS en ambos workflows. La evidencia existente se reutiliza, pero no se declara que cubra esta matriz conjunta hasta que la aserción agrupada se ejecute. PR #95 permanece en borrador; `main` no se modifica.


## 8. Resultado de CI del bloque agrupado — 2026-10-25

**PASS en ambos workflows** para el bloque implementado en `d12bb02f40ac0ec841ae33bfc0fa3c445ade8aa0`:

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40199349994)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40199350007)

El bloque verifica snapshots del estado base y propuestas pendientes; la invalidación de mappings efectivos por cambio de catálogo; la conservación de historial `STALE`; coherencia de `T_acc`, alcanzabilidad y trayectorias después de invalidar; y que restaurar el catálogo no reactive mappings obsoletos sin una nueva aceptación.

**Alcance preciso:** el PASS valida estas aserciones ejecutadas. No se interpreta como evidencia de que todas las fases del gate propuesto quedaron agrupadas: la comparación explícita de una decisión rechazada contra el baseline y la idempotencia de la reaplicación no están ambas afirmadas por este nuevo tramo. Deben considerarse cubiertas solo si la suite existente correspondiente se identifica y su evidencia se referencia; no se deben declarar como parte de este bloque por inferencia.

**Estado del gate:** bloque agrupado implementado y PASS; cierre global pendiente de resolver documentalmente la trazabilidad de las aserciones de rechazo e idempotencia, sin reabrir las 60 permutaciones declarada↔declarada.


## 9. Cierre de las dos aserciones residuales — implementadas, CI pendiente

Commit de implementación: `520b82d43506cf141c880787b6713d835b897913`.

En el mismo fixture agrupado, tras restaurar el ámbito de catálogo:

1. Se rechaza explícitamente `t_ab` y se compara con el snapshot operacional previo: mapping declarado, overlay efectivo, `T_acc`, grafo, alcanzabilidad y trayectorias deben permanecer idénticos. Se comprueba además que la decisión `REJECTED` está persistida.
2. Se acepta explícitamente `t_cd`, se aplica una vez y se repite la aplicación. El conjunto efectivo y el almacenamiento persistido deben permanecer idénticos entre ambas aplicaciones; la decisión rechazada debe seguir presente.

**Estado:** las aserciones están implementadas en el bloque agrupado; pendiente obtener PASS en Navegador y concordancia y Motor sintético sobre este commit. No declarar el gate cerrado hasta comprobar ambos resultados.


## 10. Rechazo e idempotencia — PASS confirmado

Commit probado: `6b5ee82bb9935a051a312ea12b4bc3233c27e943`.

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40203256337)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40203256339)

La suite del navegador ejecutó las aserciones agrupadas de rechazo sin cambio del snapshot operacional, persistencia de `REJECTED`, y reaplicación idempotente (conjunto efectivo y almacenamiento persistido sin cambios entre la primera y segunda aplicación). El motor sintético también pasa.

**Resultado:** los dos aspectos residuales quedan cubiertos por evidencia de CI en este commit. Esto cierra este bloque de cobertura agrupada; no equivale a afirmar validez científica general de TGCV ni recuperación automática de declaraciones desde persistencia nativa. PR #95 sigue en borrador; no se ha fusionado a `main`.


## 11. Reconciliación de estado — fuente de verdad vigente (2026-10-25)

Esta sección prevalece sobre los estados históricos de “CI pendiente” de las secciones 7–9, que describían commits anteriores.

**Último commit de pruebas verificado:** `f12bf81214f90807cb8d6ce0a5f743a096ce424f`.

- [Navegador y concordancia — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40204075921)
- [Motor sintético — PASS](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40204075929)

La CI confirma el bloque de invariancia al invertir el orden del catálogo en la colisión declarada↔derivada: preservación exacta del mapping declarado, conjunto normalizado de candidatas/conflictos, evidencia de exclusión y ausencia de mappings efectivos antes de aceptación. También siguen vigentes los PASS previos del bloque de rechazo sin alteración operacional e idempotencia (commit `6b5ee82bb9935a051a312ea12b4bc3233c27e943`, runs 40203256337 y 40203256339).

### Pendiente exacto dentro de este gate

**Queda 1 bloque de integración cruzada agrupado, con 2 ejecuciones CI** (Navegador y concordancia + Motor sintético), no una batería por permutación. No se reabren las 60 permutaciones declarada↔declarada.

El bloque pendiente debe unir en una sola secuencia/fixture controlado las fases que hoy tienen evidencia en pruebas separadas: baseline → propuestas pendientes → rechazo explícito → mapping efectivo → cambio de catálogo que lo vuelve `STALE` → restauración/recarga/reaplicación. En cada fase debe comparar por separado mapping declarado/overlay efectivo y procedencia, `T_acc`, grafo TGCV, resultados por escenario, estados alcanzables y trayectorias normalizadas; verificar persistencia de decisiones y que ni `REJECTED` ni `STALE` se reactiven indebidamente. La idempotencia ya tiene PASS separado, pero debe quedar incluida en esa secuencia integrada para cerrar el gate contractual tal como está definido.

Esto es el conteo preciso del gate de integración cruzada documentado aquí; no significa que se hayan cerrado todos los límites de alcance enumerados en el contrato de aceptación §10.6.

## 12. Reconciliación contractual vigente — 2026-10-25

Esta sección prevalece sobre el estado histórico “queda 1 bloque” de §11, que se escribió antes de ejecutar la integración final.

### Gate de integración cruzada de correspondencias: CERRADO

El bloque agrupado quedó implementado y pasó los dos workflows sobre el mismo commit de código `1491c2dce624e42da3ef6fb682a4645700612764`:

- Navegador y concordancia: **PASS** — [run 40208152055](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40208152055).
- Motor sintético: **PASS** — [run 40208152054](https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/40208152054).

La secuencia agrupada cubre propuestas/decisiones, conflicto de aplicación fail-closed, suspensión de la correspondencia previa sin confundirla con revocación, invalidación `STALE`, historial persistido y revisión/reaplicación. La aserción añadida exige que un conflicto temporal no escriba una falsa invalidación `STALE`. El rechazo sin efecto operacional y la idempotencia tienen además evidencia agrupada previa referenciada en §10 (runs 40203256337 y 40203256339). No se reabren las 60 permutaciones declarada↔declarada.

**Recuento conciliado de este gate:** 1 bloque automatizado agrupado, 2 ejecuciones de CI, ambas PASS. No hay ejecuciones correctivas pendientes para este gate.

### Estado contractual global de PR #95: PARCIAL / NO PROMOCIONABLE

El cierre del bloque anterior no equivale a cerrar todos los criterios de aceptación del contrato del demostrador. Se mantienen visibles los blockers de §10.6 del contrato y las brechas de cobertura de esta matriz:

1. **Entrada de condiciones por tres vías:** JSON, transcriptor de texto y editor visual; la matriz de aceptación adversarial completa de los tres caminos continúa pendiente/parcial.
2. **Resolución general de conflictos:** existe cobertura integrada para los fixtures y órdenes enumerados, pero no está verificado un flujo de usuario general que resuelva todos los tipos de `CONFLICT_NEEDS_REVIEW`.
3. **Restauración tras reinicio del navegador:** la restauración de las decisiones de resolución de conflicto tras reiniciar el contexto del navegador sigue sin verificar; no confundirla con `reload()` cubierto en los fixtures.
4. **Límite del derivador:** la generación sigue siendo coincidencia exacta de fronteras; no se reclama inferencia semántica general ni validez científica a partir de CI.

Los controles ya PASS de equivalencia operacional `T_acc`/ejecución, rechazo, idempotencia, invalidación y recarga se reutilizan; no se repiten por separado para cerrar el bloque ya aprobado.

**Decisión de gobernanza:** PR #95 permanece abierta y en borrador. No fusionar ni promover sobre la base del cierre del gate mínimo. Los blockers restantes deben cerrarse con evidencia o separarse mediante una aceptación de alcance explícita que los mantenga como tareas rastreables; no se eliminan por reconciliación documental. `main` permanece intacta y no se autoriza ejecución científica.
