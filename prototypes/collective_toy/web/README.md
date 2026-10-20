# Juguete Colectivo — guía de uso del MVP

Esta guía corresponde a la rama de desarrollo del demostrador Full Chain. El MVP ejecuta **grafos finitos sintéticos**; no es una implementación científicamente validada de (T_{acc}), no demuestra causalidad ni construcción de valor y no debe usarse para inferencias científicas.

## 1. Abrir el demostrador

Requisitos: Python 3 y un navegador moderno.

Desde la raíz del repositorio:

```bash
python -m http.server 8000 --directory prototypes/collective_toy/web
```

Abre http://localhost:8000. En Windows también puedes usar:

```powershell
py -m http.server 8000 --directory prototypes/collective_toy/web
```

Para detener el servidor, pulsa `Ctrl+C`. Mantén el servidor en localhost; no lo publiques en una red ni lo expongas a Internet.

## 2. Crear un grafo desde un archivo

Pulsa **Importar grafo (DOT / Mermaid / GraphML)** y selecciona un archivo compatible. La importación crea un borrador de modelo, no una reconstrucción verificada de la imagen o del sistema original.

Si partes de una imagen:

1. Pulsa **Cargar imagen** y elige una imagen PNG, JPEG o WebP (máximo 5 MiB).
2. Opcionalmente, pulsa **Reconocer texto (OCR)**. El OCR extrae texto; **no detecta de forma fiable la topología, las conexiones ni la dirección de las flechas**.
3. Revisa el texto extraído y las posibles confusiones literales. No des por válida una conexión porque aparezca en la transcripción.
4. Puedes corregir la transcripción o escribir las conexiones manualmente, una por línea, por ejemplo `A --> B` o `B --- C` cuando la dirección no esté clara.
5. Pulsa **Convertir en borrador de grafo**. La conversión no equivale a una validación de la imagen original.

**Límite conocido:** la ruta de imagen disponible combina OCR textual y revisión manual. No debe describirse como un reconocedor visual completo de grafos. La detección geométrica de nodos, trazos, cruces y puntas de flecha sigue siendo experimental; las pruebas sintéticas actuales no acreditan generalización a diagramas reales.

## 3. Revisar y corregir el grafo

Antes de ejecutar:

1. Compara visualmente el grafo dibujado con la imagen de referencia.
2. Comprueba cada nodo, bifurcación, convergencia, conexión y extremo.
3. Lee **Conexiones del modelo** y el **Resumen de revisión estructural**. Los avisos son heurísticos: pueden señalar algo que está bien y no garantizan que se hayan encontrado todas las omisiones.
4. Si una conexión es incorrecta, pulsa **Eliminar conexión**. Para reconstruirla, selecciona el origen en **Desde**, el destino en **Hasta** y pulsa **Conectar estados**.
5. Si la dirección de una flecha es ambigua, **no la adivines**. Conserva la conexión como no dirigida/sin resolver cuando el formato lo permita (por ejemplo, `B --- C` en una transcripción Mermaid), o déjala fuera del modelo hasta poder verificarla. En otros formatos, no presupongas que la falta de flecha se conservará como estado sin resolver. Si conoces la dirección, elimina la conexión incorrecta y créala con el origen y destino correctos.
6. Revisa también el estado inicial. El primer estado importado puede no ser el estado inicial real.
7. Sólo cuando hayas terminado la revisión, pulsa **Ejecutar escenarios**.

El editor actual permite añadir estados, eliminar conexiones y crear conexiones dirigidas mediante origen y destino. No realiza una comparación automática concluyente entre el grafo reconstruido y los píxeles de la imagen. Conserva la imagen original para la comprobación visual.

## 4. Ejecutar y exportar

Con el ejemplo sintético:

1. Pulsa **Cargar ejemplo**.
2. Pulsa **Ejecutar escenarios**.
3. Revisa el grafo y los resultados de `baseline` y `block_ac`.
4. Comprueba los avisos de exploración acotada y el escenario seleccionado.
5. Exporta el paquete JSON si necesitas conservar una ejecución reproducible.

El estado PASS de la interfaz indica que el modelo superó la validación de entrada y que se ejecutó la simulación local. **No** significa que el grafo coincida con la imagen, que el modelo represente un sistema real o que TGCV haya sido validada científicamente.

## 5. Importar formatos estructurados y JSON

- Usa **Importar grafo (DOT / Mermaid / GraphML)** para los formatos de grafo admitidos.
- Usa **Importar JSON avanzado** para un modelo estructurado compatible con el contrato del demostrador.
- El bloque **JSON avanzado (editable)** sirve para inspección y edición técnica. No es necesario para el flujo normal de uso.

Si la importación detecta etiquetas o condiciones de transición que el modelo actual no puede preservar, debe detenerse en vez de descartar silenciosamente esa semántica. Revisa el archivo y prepara una versión compatible antes de volver a importarlo.

## 6. Pruebas automatizadas

Requisitos: Python 3.12 recomendado, Node.js 22 y npm.

Desde `prototypes/collective_toy/web`:

```bash
npm install
npx playwright install --with-deps chromium
npm test
```

Pruebas del motor Python, desde `prototypes/collective_toy`:

```bash
python -m unittest -v test_collective_toy_engine_001.py
```

Un workflow debe haber terminado sobre el commit exacto evaluado antes de considerarlo validado para ese commit. Las pruebas sintéticas validan los casos cubiertos por esos tests, no la recuperación general de grafos desde imágenes reales.

## 7. Límites actuales y criterio de aceptación de la importación

El criterio práctico del MVP es **imagen de referencia → borrador de grafo → revisión/corrección humana → ejecución del grafo revisado**. No es necesario resolver primero toda la dirección automática de flechas.

- Las etiquetas OCR son provisionales y se pueden corregir.
- La topología debe revisarse independientemente de la calidad de las etiquetas.
- Una dirección dudosa no debe aceptarse por una diferencia aislada de soporte geométrico.
- La automatización puede proponer candidatos, pero no debe autoaceptar conexiones.
- Los casos no resueltos deben permanecer visibles para revisión; no se deben convertir en certeza silenciosamente.
- Las pruebas con imágenes sintéticas son diagnósticas. No constituyen una validación con diagramas reales ni evidencia científica TGCV.
- No se autoriza por esta guía ninguna ejecución científica, uso de datos reales, cambio del Core ni promoción a `main`.
