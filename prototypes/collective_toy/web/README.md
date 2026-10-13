# Juguete Colectivo — arranque y verificación del MVP

Este directorio contiene la interfaz de navegador y sus pruebas automatizadas. El MVP ejecuta **grafos finitos sintéticos**; no es una implementación validada de (T_{acc}), no demuestra causalidad ni construcción de valor y no debe ejecutarse con datos reales.

## Abrir la interfaz

Requisitos para la forma más simple: Python 3 instalado y un navegador moderno.

Desde la raíz del repositorio:

```bash
python -m http.server 8000 --directory prototypes/collective_toy/web
```

Abre [http://localhost:8000](http://localhost:8000). Para detener el servidor, pulsa `Ctrl+C` en la terminal.

En Windows se puede usar `py -m http.server 8000 --directory prototypes/collective_toy/web` si el comando `python` no está disponible.

La interfaz es un HTML autónomo y no necesita compilarse. Sirve la página desde `localhost` para disponer de un contexto de navegador consistente para Web Crypto y la generación de hashes. No publiques el servidor en una red ni lo expongas a Internet.

## Recorrido manual de humo

Haz este recorrido con el ejemplo sintético predeterminado:

1. Pulsa **Cargar ejemplo** y comprueba que el JSON contiene los estados `A, B, C, D`.
2. Pulsa **Ejecutar escenarios**. Revisa el grafo, los resultados de `baseline` y `block_ac`, y los avisos de exploración acotada.
3. Cambia el escenario visualizado y comprueba que la vista se actualiza.
4. Cambia al **Perfil 2**, añade una relación de disponibilidad entre dos transiciones y vuelve a ejecutar. Comprueba que la regla es local al escenario y que no se interpreta recursivamente.
5. Exporta el paquete JSON. Importa ese mismo archivo y pulsa **Validar paquete importado**; la reproducción independiente debe coincidir.
6. Importa un paquete incompatible o manipulado en una copia de prueba y confirma que se rechaza o queda en modo de inspección, sin presentarse como replay verificado.
7. Repite el recorrido con una pantalla estrecha/móvil y con escritorio. Comprueba que los controles son utilizables, que los errores son visibles y que no hay desplazamiento horizontal involuntario.

No uses un paquete de datos reales ni interpretes los resultados como evidencia científica.

## Pruebas automatizadas

Requisitos: Python 3.12 recomendado, Node.js 22 y npm.

Desde el directorio `prototypes/collective_toy/web`:

```bash
npm install
npx playwright install --with-deps chromium
npm test
```

`npm test` ejecuta concordancia Python–JavaScript y pruebas del contrato de interfaz mediante Playwright. Las pruebas de motor Python se ejecutan desde `prototypes/collective_toy`:

```bash
python -m unittest -v test_collective_toy_engine_001.py
```

Los benchmarks se ejecutan por separado en GitHub Actions mediante `workflow_dispatch`:

- [Benchmark de navegador](https://github.com/jcarmonabastida-pixel/TGCV/actions/workflows/collective-toy-browser-performance.yml)
- [Benchmark del motor](https://github.com/jcarmonabastida-pixel/TGCV/actions/workflows/collective-toy-performance-benchmark.yml)

Un workflow que no se haya ejecutado sobre el commit evaluado no debe marcarse como validado para ese commit. Los umbrales de rendimiento aún son diagnósticos; no constituyen un SLO de producto.

## Límites actuales

- Perfil 1: las relaciones son metadatos descriptivos.
- Perfil 2: relaciones explícitas y experimentales de disponibilidad de transiciones; semántica local al escenario y no recursiva.
- `T_enabled` es una salida local del modelo y **no equivale** a (T_{acc}) sistémico.
- Las trayectorias son enumeraciones acotadas del grafo configurado; no hay aún una semántica general de secuencialidad, taxonomía de outcomes ni función de valor dependiente del observador/contexto.
- La interpretación científica está desactivada; la ejecución con datos reales sigue desautorizada.

## Informe de problemas

Al reportar un defecto, incluye el navegador/SO, pasos para reproducirlo, JSON sintético mínimo, resultado esperado y observado, y si falla también la prueba automatizada. No incluyas datos personales ni datos reales del sistema estudiado.
