# Guía de uso completa — Demostrador Interactivo TGCV Full Chain 001

- **Estado:** guía de usuario propuesta para revisión.
- **Aplicación de referencia:** distribución autónoma Full Chain, archivo `index.html`.
- **Ejemplo de referencia:** grafo sintético de tipo diamante, estados A, B, C y D.
- **Alcance:** uso del software y sus artefactos de demostración. No constituye validación científica de TGCV.
- **Fuente de continuidad:** `prototypes/collective_toy/DISTRIBUTION_README_001.md`, contrato Full Chain, registro de aceptación manual y paquete distribuido.

## 1. Qué es el demostrador

El Demostrador Interactivo TGCV permite construir o importar un pequeño grafo dirigido, explorar transformaciones bajo reglas explícitas del prototipo, comparar escenarios, inspeccionar trayectorias posibles, ejecutar una secuencia concreta, registrar un resultado y una valoración contextual por separado y exportar/importar un paquete auditable.

La aplicación es una demostración de software sobre sistemas sintéticos. No implementa por sí sola la función científica canónica de TGCV (T_{acc}=F(S,C,L)), no procesa datos empíricos y no demuestra causalidad, creación de valor real ni validez científica de TGCV.

## 2. Abrir la distribución

1. Descomprime el ZIP de distribución en una carpeta local.
2. Abre `index.html` con Google Chrome o un navegador moderno compatible. Si Windows intenta abrirlo con otra aplicación, usa **Abrir con → Google Chrome**. No es necesario instalar Node.js para utilizar la aplicación.
3. Comprueba que aparece el título **Demostrador Interactivo TGCV** y el aviso sobre el alcance sintético.
4. La distribución está pensada para funcionar localmente en el navegador. No ejecutes comandos de desarrollo para el uso normal.

## 3. Cargar el ejemplo de referencia

En el panel **1 · Define el sistema**, pulsa **Cargar ejemplo**. El ejemplo de referencia es un grafo dirigido pequeño con cuatro estados:

- **A:** estado inicial.
- **B** y **C:** estados intermedios que ofrecen rutas alternativas.
- **D:** estado final común de las dos rutas.

Sus transiciones principales son:

- `t_ab`: A → B.
- `t_ac`: A → C.
- `t_bd`: B → D.
- `t_cd`: C → D.

El ejemplo contiene los escenarios `baseline` y `block_ac`. En el segundo, la transición `t_ac` está deshabilitada. Por tanto, se puede comparar el escenario base con una intervención que elimina una de las salidas de A. El ejemplo es deliberadamente pequeño para que los resultados puedan inspeccionarse manualmente.

Pulsa **Ejecutar escenarios** para validar y calcular el modelo cargado. Revisa el mensaje de estado antes de interpretar los paneles de resultados.

## 4. Inspeccionar y editar el grafo

El panel **2 · Grafo del sistema** presenta los estados y las transiciones dirigidas. Las flechas atenuadas representan transiciones deshabilitadas en el escenario visualizado.

- **Escenario visualizado:** selecciona `baseline` o una intervención disponible.
- **Disposición:** cambia entre automática, circular, cuadrícula y por niveles. Estos controles cambian la presentación, no la semántica del modelo.
- **Zoom + / −:** amplía o reduce el grafo.
- **Encuadrar todo:** ajusta la vista para mostrar el grafo completo.
- **Editor visual:** permite añadir estados y conexiones, marcar el estado inicial y revisar/eliminar conexiones.
- **Importar grafo (DOT / Mermaid / GraphML):** carga una representación estructurada compatible y genera un modelo que debe revisarse.
- **Importar JSON avanzado:** carga un archivo JSON del esquema esperado por el prototipo.
- **JSON avanzado:** permite inspeccionar o editar directamente el modelo. Es una opción para usuarios que necesitan controlar el esquema; no es necesaria para seguir el recorrido normal.

Después de cambiar el modelo, vuelve a pulsar **Ejecutar escenarios** para recalcular los resultados. No asumas que una edición ya recalculó todos los paneles si la interfaz indica que debes ejecutar de nuevo.

### Revisión antes de ejecutar

Comprueba que:
- cada estado tenga un identificador coherente;
- las conexiones tengan origen y destino correctos;
- la dirección de cada flecha coincida con el modelo que quieres representar;
- no haya conexiones duplicadas o conexiones omitidas;
- el estado inicial sea el correcto;
- los escenarios y las transiciones deshabilitadas reflejen la intervención pretendida.

Los avisos automáticos de revisión son heurísticos: ayudan a localizar posibles problemas, pero no sustituyen la revisión humana.

## 5. Explorar escenarios y transformaciones accesibles

La ejecución del modelo calcula los resultados del prototipo bajo el perfil de reglas declarado. Revisa las transformaciones disponibles, los estados alcanzables y los cambios entre el escenario base y las intervenciones.

Mantén separadas estas ideas:

- **Transición declarada:** figura en el modelo, pero puede estar deshabilitada por el escenario o por las reglas.
- **Transformación accesible bajo el prototipo:** el motor la considera utilizable bajo la configuración y reglas operativas seleccionadas.
- **Estado alcanzable:** puede alcanzarse desde el estado inicial siguiendo las transiciones habilitadas.
- **Trayectoria posible:** secuencia candidata enumerada por la exploración.
- **Ejecución concreta:** secuencia específica que el usuario solicita ejecutar y cuya traza registra el motor.

La aproximación del prototipo a la accesibilidad de transformaciones es operativa y sintética. No debe presentarse como una medición empírica ni como implementación definitiva de la función científica de TGCV.

## 6. Comparar escenario base e intervención

El escenario `baseline` sirve como referencia del modelo, no como una ejecución previa de un sistema real. `block_ac` es un escenario separado que deshabilita `t_ac`.

Compara ambos escenarios para observar cómo cambia el conjunto de transiciones disponibles, los estados alcanzables y las trayectorias enumeradas. Interpreta la diferencia como resultado del modelo sintético y de la intervención codificada. No la interpretes como efecto causal observado en el mundo real, como puntuación de valor ni como evidencia de validez científica.

Al editar escenarios, conserva conceptualmente la distinción entre la configuración base y la intervención; no sobrescribas la referencia con una modificación que después no puedas identificar.

## 7. Navegar por las trayectorias posibles

La sección de trayectorias permite inspeccionar rutas alternativas. Cuando esté disponible el navegador visual de trayectorias:

1. Examina la ruta seleccionada y sus estados/transiciones.
2. Usa los controles anterior/siguiente para comparar alternativas.
3. Observa los recuentos y cualquier aviso de límite o truncamiento.
4. Selecciona la trayectoria que quieras probar como ejecución concreta.

La enumeración de una trayectoria no significa que se haya ejecutado. Si la exploración alcanza un límite de profundidad o de número de rutas, trata los resultados como limitados y conserva el aviso de truncamiento.

## 8. Ejecutar una secuencia concreta

Selecciona una trayectoria disponible o introduce la secuencia exacta según los controles presentados por la aplicación. Ejecuta los pasos en el orden elegido y revisa el resultado.

Una ejecución válida debe registrar la secuencia y los estados recorridos. Si un paso incumple una condición o un prerrequisito temporal del perfil, la ejecución debe detenerse en el paso bloqueado y explicar el motivo. No interpretes un bloqueo como un fallo de la interfaz sin revisar la secuencia y la condición que no se satisfizo.

La traza de ejecución es diferente de la lista de trayectorias posibles. Conserva esa diferencia al comparar ejecuciones y al exportar el paquete. Los identificadores internos, los prerrequisitos y los códigos de motivo pueden formar parte de la traza auditable aunque la vista principal muestre una explicación más sencilla.

## 9. Registrar un resultado (*outcome*)

Después de una ejecución concreta, registra el resultado en la sección destinada a resultados. Utiliza datos explícitos y coherentes con el propósito de la demostración. En el ejemplo de referencia, cualquier resultado introducido es ilustrativo y sintético.

Un resultado debe quedar vinculado a la ejecución correspondiente. No lo infieras del número de trayectorias, del número de estados alcanzables, de que una secuencia haya terminado o de una etiqueta PASS del software. Si no se dispone de un resultado, deja constancia de que no se ha evaluado en vez de inventar uno.

## 10. Evaluar valor según observador y contexto

La evaluación contextual es una etapa distinta del registro del resultado. Para realizarla, especifica los campos que solicite la interfaz, incluidos los elementos aplicables de:

- observador;
- contexto;
- objetivo o criterio;
- regla de valoración;
- justificación;
- puntuación, cuando proceda.

La valoración responde a un criterio contextual declarado; no es una propiedad universal deducida automáticamente del grafo. Dos valoraciones solo son directamente comparables si se revisa que sus contextos, observadores, criterios y reglas sean compatibles. Si la aplicación advierte que los contextos son distintos, no ignores el aviso ni presentes las puntuaciones como si midieran necesariamente lo mismo.

Mantén separados el resultado registrado y la valoración que alguien hace de ese resultado. Una ejecución correcta no implica por sí misma que el resultado tenga valor positivo.

## 11. Comparar ejecuciones

Cuando la interfaz permita comparar dos ejecuciones, selecciona los registros pertinentes y revisa:
- las secuencias ejecutadas;
- los estados finales y el estado de terminación;
- los resultados asociados;
- las valoraciones contextuales;
- las diferencias de configuración y de contexto;
- los avisos sobre comparabilidad.

La comparación describe diferencias entre registros sintéticos bajo sus configuraciones declaradas. No establece por sí sola causalidad ni prueba que una intervención produzca un resultado real.

## 12. Exportar un paquete

Usa la acción de exportación disponible para descargar el paquete JSON de la ejecución. Si estás comprobando una valoración contextual, verifica que exportas la ejecución deseada y no otra.

El paquete puede contener, según la etapa alcanzada, el modelo, el escenario, la configuración del motor, la traza, el resultado, la valoración, la información de procedencia y los campos de integridad. Los paquetes pueden corresponder a etapas distintas; la ausencia de una valoración no significa necesariamente que un paquete de exploración o ejecución sea inválido.

Guarda el archivo con un nombre reconocible y conserva el original si necesitas repetir la comprobación. El nombre de archivo por sí solo no garantiza su integridad ni su procedencia.

## 13. Importar y validar un paquete

1. En **Importar paquete exportado**, selecciona el archivo JSON.
2. Pulsa **Validar paquete importado**.
3. Lee el estado completo que muestra la interfaz.
4. Si se informa que la integridad está verificada y que la reproducción independiente coincide, registra ese resultado como verificación del paquete bajo el contrato declarado.

La validación comprueba las propiedades de integridad y reproducción que soporta el esquema y motor de la aplicación. Un mensaje satisfactorio no autentica por sí solo quién creó el archivo, no demuestra que el contenido corresponda a un evento real y no valida afirmaciones científicas de TGCV. Tampoco debe confundirse la verificación de integridad con la reproducción semántica: son comprobaciones relacionadas, pero distintas.

## 14. Importación desde imagen: capacidad experimental

La importación desde imagen es una extensión experimental, no un requisito del recorrido Full Chain aceptado. En la distribución actual, el panel de imagen permite introducir una transcripción obtenida externamente o transcribir manualmente las conexiones; no ejecuta OCR automáticamente.

El procedimiento de transcripción crea un **borrador de grafo**. Antes de utilizarlo:
1. revisa todos los nodos;
2. revisa cada conexión, dirección y bifurcación;
3. busca conexiones omitidas, inventadas o duplicadas;
4. confirma las condiciones o etiquetas de transición que puedan afectar a la ejecución;
5. corrige el modelo y vuelve a validarlo antes de ejecutar escenarios.

No asumas que las flechas o su dirección se detectan automáticamente. La integración de PaddleOCR y la evaluación de OpenCV para recuperar la estructura del grafo están pendientes de evaluación separada.

## 15. Solución de problemas

- **Windows intenta abrir el archivo con una aplicación incorrecta:** usa el menú contextual **Abrir con → Google Chrome**.
- **El ejemplo no aparece o los resultados no se actualizan:** pulsa **Cargar ejemplo** y después **Ejecutar escenarios**; lee el mensaje de estado.
- **Un archivo JSON no se importa:** comprueba que sea un JSON válido y que corresponda al esquema de entrada o de paquete esperado. No todos los JSON representan el mismo tipo de artefacto.
- **Una trayectoria queda bloqueada:** revisa el paso exacto, el estado actual y los prerrequisitos indicados en la traza.
- **No aparece una trayectoria esperada:** revisa el escenario seleccionado, las transiciones deshabilitadas y los límites de exploración.
- **La validación del paquete rechaza el archivo:** conserva el archivo original y el mensaje de error. No edites el paquete para eliminar la señal de fallo; investiga la incompatibilidad, la integridad o la versión del esquema.
- **La valoración advierte contextos distintos:** revisa las definiciones de observador, criterio y contexto antes de comparar puntuaciones.

## 16. Qué puede y qué no puede concluirse

**Sí permite comprobar:** que el prototipo acepta un modelo sintético, calcula los resultados que definen sus reglas operativas, permite explorar trayectorias, ejecutar secuencias, registrar resultados y valoraciones por separado y exportar/importar paquetes con las verificaciones implementadas.

**No permite concluir por sí solo:** que el modelo represente fielmente un sistema real; que el resultado sintético haya ocurrido empíricamente; que una diferencia sea causal; que una puntuación sea valor objetivo; que el prototipo implemente la definición científica canónica de (T_{acc}); ni que TGCV haya quedado validada científicamente.

## 17. Recorrido de referencia recomendado

Para una primera demostración reproducible:

1. Abre `index.html` en Chrome.
2. Pulsa **Cargar ejemplo**.
3. Pulsa **Ejecutar escenarios**.
4. Inspecciona el grafo y el escenario `baseline`.
5. Selecciona `block_ac` y compara los cambios.
6. Revisa las trayectorias posibles y selecciona una.
7. Ejecuta la secuencia y revisa la traza.
8. Registra un resultado sintético explícito.
9. Completa una valoración contextual declarando observador, criterio y contexto.
10. Compara las ejecuciones/valoraciones cuando proceda.
11. Exporta el paquete.
12. Importa el archivo exportado y pulsa **Validar paquete importado**.
13. Guarda el paquete y el resultado de validación junto con la versión de la distribución si necesitas conservar la evidencia.

**Criterio de cierre de esta guía:** cada paso descrito debe contrastarse con los controles y textos del paquete exacto que se distribuirá. Si una etiqueta o flujo difiere entre el paquete y la rama de código, debe corregirse la guía o identificarse explícitamente la versión; no se debe asumir equivalencia entre artefactos distintos.
