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
- Las importaciones Mermaid/DOT/GraphML reconocen un subconjunto de sintaxis y extraen identificadores de nodos y extremos de conexiones dirigidas; no conservan el diseño visual, las etiquetas descriptivas de nodos, los metadatos ni las condiciones. El estado inicial se asigna al primer estado encontrado, por lo que debe revisarse. Si la estructura de origen usa etiquetas, subgrafos o sintaxis no reconocida, revisa y corrige el grafo en el editor o utiliza JSON explícito. La prueba automatizada cubre grafos sencillos, no compatibilidad completa con todas las variantes de esos formatos.
- Hay tres vías de entrada al mismo editor: importar grafos Mermaid/DOT/GraphML, importar el modelo JSON explícito o describir el sistema en lenguaje natural. La tercera vía usa patrones lingüísticos locales y limitados para proponer transiciones explícitas, incluidas bifurcaciones y retornos formulados claramente. Las frases con condiciones (por ejemplo, «si» o «cuando») y las frases no interpretadas quedan pendientes y no se incorporan al grafo: no se deben dar por comprendidas ni se debe descartar su condición. El modelo ejecutable actual no representa condiciones en las transiciones. La interfaz permite reformular en un panel separado las frases pendientes y sustituir solo esas frases en la descripción original, conservando las relaciones que sí se reconocieron; después vuelve a proponer el grafo localmente. La reformulación no se interpreta como validación automática y el usuario debe revisar el nuevo borrador. Como el modelo actual no representa condiciones en las transiciones, no debe eliminarse una condición esencial para forzar la aceptación de una frase; si afecta al significado del sistema, la limitación debe quedar explícita y el borrador no debe ejecutarse como si esa condición estuviera representada. El borrador requiere revisión humana de estados, conexiones, direcciones y estado inicial antes de ejecutar. No requiere una API externa.

La versión del paquete se identifica por el SHA del commit que lo produjo en GitHub Actions. Este paquete no es una validación científica de TGCV.
