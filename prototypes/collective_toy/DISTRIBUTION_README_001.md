# Juguete Colectivo — distribución Full Chain

Esta distribución es un demostrador web autónomo de la cadena Full Chain de TGCV. Abre `index.html` en un navegador moderno. No requiere instalar Node.js para usar la aplicación; Node.js y Playwright solo se necesitan para ejecutar las pruebas de desarrollo.

## Recorrido sugerido

1. Inspecciona el sistema sintético y sus estados/transiciones.
2. Revisa las transformaciones accesibles bajo el perfil operativo seleccionado.
3. Ejecuta el escenario base y compáralo con una intervención separada.
4. Inspecciona estados alcanzables y trayectorias posibles; no los confundas con una ejecución concreta.
5. Ejecuta una secuencia ordenada y revisa la traza y cualquier paso bloqueado.
6. Registra un resultado explícito vinculado a esa ejecución.
7. Realiza una evaluación contextual solo si defines observador, criterio y contexto.
8. Exporta el paquete, vuelve a importarlo y verifica la reproducción.

El archivo `example-diamond.json` contiene un sistema sintético pequeño en forma de diamante. Impórtalo desde el botón de JSON avanzado.

## Límites

- Solo grafos y escenarios sintéticos; no se autoriza ejecución científica ni se procesan datos reales.
- La aproximación operativa de transformaciones accesibles es una regla del prototipo, no la función científica canónica de TGCV.
- Los hashes y la reproducción apoyan consistencia y reproducibilidad; no autentican el origen ni prueban que un evento real ocurriera.
- Hay tres vías de entrada al mismo editor: importar grafos Mermaid/DOT/GraphML, importar el modelo JSON explícito o crear un borrador mediante transcripción asistida de texto a grafo. Las conexiones importadas o transcritas deben revisarse antes de ejecutar. La transcripción de texto funciona localmente y no requiere una API externa.

La versión del paquete se identifica por el SHA del commit que lo produjo en GitHub Actions. Este paquete no es una validación científica de TGCV.
