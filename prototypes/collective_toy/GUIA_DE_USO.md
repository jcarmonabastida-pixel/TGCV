# Guía de uso — Demostrador interactivo Full Chain de TGCV

**Versión de la guía:** {{GUIDE_VERSION}}  
**Versión del paquete:** {{PACKAGE_VERSION}}  
**Commit fuente del paquete:** `{{SOURCE_COMMIT}}`

Esta guía pertenece al paquete ejecutable que contiene este archivo. La versión HTML equivalente está en `GUIA_DE_USO.html`. El paquete es una demostración de software sintética: no constituye validación científica de TGCV.

## 1. Requisitos y apertura

- Sistema operativo con un navegador moderno actualizado (por ejemplo, Google Chrome, Microsoft Edge o Firefox).
- No se necesita instalar Node.js, Python ni dependencias para usar la aplicación.
- Descomprime el ZIP en una carpeta local y conserva juntos todos sus archivos.
- Abre `index.html` con el navegador. Si Windows abre otro programa, usa **Abrir con** y selecciona el navegador.

No muevas `index.html` fuera de la carpeta: el README, la guía y el ejemplo forman parte de la distribución.

## 2. Qué hace el demostrador

El demostrador permite inspeccionar un modelo de sistema sintético y recorrer una cadena de etapas: modelo, transformaciones y relaciones, conjunto de transformaciones accesibles según reglas explícitas del prototipo, comparación entre escenario base e intervención, estados alcanzables, trayectorias posibles, ejecución ordenada, registro explícito de resultado, evaluación contextual opcional y exportación/reproducción de un paquete auditable.

La implementación usa una aproximación operativa para hacer visible la cadena. No implementa por sí misma la definición científica canónica de TGCV ni demuestra causalidad o creación de valor.

## 3. Las tres modalidades de entrada

Las tres modalidades llevan al mismo editor de modelo. Tras importar o describir un sistema, revisa el borrador antes de ejecutarlo.

### A. Importar un grafo Mermaid, DOT o GraphML

1. Selecciona la opción de importar grafo e introduce o carga el contenido admitido por la interfaz.
2. Revisa la lista de estados y conexiones generada.
3. Comprueba especialmente los extremos y la dirección de cada conexión.
4. Verifica y corrige el estado inicial en el editor.

**Límites:** se reconoce un subconjunto de cada formato. No se conserva necesariamente el diseño visual, las etiquetas descriptivas, los metadatos, subgrafos ni condiciones. Los identificadores de nodos y los extremos de las conexiones dirigidas son lo principal que se extrae. La prueba automatizada cubre grafos sencillos, no toda la especificación de Mermaid, DOT o GraphML. Si el resultado es incompleto, corrige el grafo o usa JSON explícito.

### B. Importar un modelo JSON explícito

1. Abre la opción JSON avanzado.
2. Pega el modelo o carga un archivo JSON.
3. Valida la sintaxis y revisa estados, transición inicial, identificadores, perfil de reglas, escenarios y relaciones.
4. Usa `example-diamond.json` como modelo sintético inicial.

JSON es la modalidad más explícita y adecuada cuando necesitas controlar con precisión el modelo y sus metadatos. El ejemplo es didáctico; no representa datos reales.

### C. Describir el sistema en lenguaje natural

1. Escribe una descripción breve con estados y cambios explícitos, por ejemplo: “A puede pasar a B. Desde A también se puede ir a C. Desde B se vuelve a A”.
2. Pide al demostrador que proponga un grafo.
3. Revisa manualmente nodos, conexiones, direcciones y estado inicial.
4. Examina las frases que queden pendientes y, si procede, reformúlalas en el panel específico.
5. Vuelve a generar la propuesta y revisa de nuevo el resultado completo.

Esta modalidad usa patrones lingüísticos locales y limitados; no es un modelo general de comprensión del lenguaje. Las bifurcaciones y retornos se pueden reconocer si están formulados claramente. Las frases no interpretadas y las que contienen condiciones como “si” o “cuando” quedan pendientes y no se incorporan al grafo. El modelo ejecutable actual no representa condiciones en las transiciones. **No elimines una condición esencial para forzar la aceptación de una frase.** Si la condición afecta al significado del sistema, conserva explícita la limitación y no ejecutes el borrador como si la condición estuviera representada. La reformulación es una ayuda, no una validación automática.

## 4. Revisar y preparar el modelo

Antes de ejecutar:

- Comprueba que cada estado necesario está presente y no hay nodos duplicados o espurios.
- Comprueba cada conexión, sus extremos y su dirección.
- Verifica el estado inicial.
- Comprueba el significado de las transformaciones y relaciones representadas.
- Corrige el modelo en el editor y valida de nuevo.
- No confundas un borrador importado con un modelo revisado y aceptado por ti.

La responsabilidad de confirmar que el grafo representa la descripción de partida recae en la persona usuaria.

## 5. Recorrido Full Chain

Los nombres y paneles concretos pueden variar ligeramente según el estado de la interfaz, pero el significado de las etapas es el siguiente:

1. **Modelo:** inspecciona estados, transiciones y contexto declarado.
2. **Transformaciones y relaciones:** identifica las transformaciones modeladas y las relaciones explícitas.
3. **Transformaciones accesibles (`T_acc`):** ejecuta las reglas del prototipo y revisa por qué una transición aparece accesible o bloqueada. Es una aproximación sintética, no la función científica canónica.
4. **Escenario base e intervención:** conserva el escenario base y define la intervención como un escenario separado. No interpretes la comparación como prueba causal.
5. **Cambio de alcanzabilidad (`ΔReach`):** inspecciona estados y transformaciones añadidos o retirados según las reglas seleccionadas. No es una puntuación de valor.
6. **Trayectorias posibles:** explora las secuencias candidatas. La enumeración puede estar limitada por profundidad o número de trayectorias; revisa cualquier aviso de truncamiento.
7. **Ejecución concreta:** selecciona o introduce una secuencia ordenada. Comprueba cada paso, el estado anterior y posterior, y los motivos de bloqueo. Una trayectoria posible no equivale a una trayectoria ejecutada.
8. **Resultado (`outcome`):** registra explícitamente un resultado sintético u observado y su procedencia. No se infiere de la cantidad de caminos ni del éxito de ejecución.
9. **Evaluación contextual de valor:** solo se evalúa si declaras observador, criterio, contexto y regla de valoración. Si faltan, el resultado debe quedar como no evaluado. El demostrador no deriva automáticamente valor de `ΔReach`.
10. **Auditoría, exportación y reproducción:** exporta el paquete, vuelve a importarlo y revisa la integridad y la reproducción determinista que declare la interfaz.

## 6. Exportar e importar el paquete de ejecución

1. Completa las etapas que quieras documentar.
2. Exporta el paquete desde la interfaz y guarda el archivo resultante.
3. Importa ese archivo en el demostrador.
4. Comprueba el resultado de la validación de integridad y la reproducción.
5. Si la validación falla, no interpretes el paquete como verificado; conserva el mensaje de error para el diagnóstico.

Los hashes y la reproducción ayudan a comprobar consistencia interna. Por sí solos no autentican el origen del archivo ni demuestran que un evento real ocurriera.

## 7. Solución de problemas

- **El archivo HTML se abre con una aplicación incorrecta:** usa el menú contextual del sistema operativo y elige un navegador moderno.
- **No se carga el ejemplo:** confirma que `example-diamond.json` está en la misma carpeta del paquete y que no has renombrado su extensión.
- **Un grafo importado está incompleto:** el importador reconoce un subconjunto de sintaxis; corrige el modelo o usa JSON.
- **Una frase natural queda pendiente:** revisa la frase en el panel de pendientes. No elimines condiciones importantes para que sea aceptada.
- **La ejecución se bloquea:** inspecciona el paso exacto, el estado actual y los requisitos temporales indicados por el prototipo.
- **La reproducción no coincide o falla la integridad:** conserva el archivo y el mensaje de validación; no edites manualmente el contenido exportado.

## 8. Trazabilidad de la distribución

Los metadatos al principio de esta guía identifican la versión de guía, la versión del paquete y el commit fuente exacto usado en la construcción. `VERSION_DISTRIBUCION.txt` repite esa identidad para facilitar comprobaciones automáticas. El HTML se genera desde la copia de Markdown ya completada con esos metadatos.

Para informar de un problema, indica esos valores y describe los pasos mínimos para reproducirlo.

## 9. Límites y uso responsable

- La distribución opera sobre modelos y escenarios sintéticos.
- No autoriza ejecuciones científicas ni análisis de datos reales.
- Las reglas operativas del prototipo no deben confundirse con las definiciones científicas canónicas de TGCV.
- Una prueba automatizada satisfactoria verifica el contrato de software cubierto por esa prueba; no demuestra causalidad, creación de valor, generalidad, superioridad ni validez científica de TGCV.
- Revisa siempre el grafo generado por importación o lenguaje natural antes de ejecutarlo.

---
**Fin de la guía.** Para empezar rápidamente, vuelve a `README.md`, abre `index.html` y carga `example-diamond.json`.
