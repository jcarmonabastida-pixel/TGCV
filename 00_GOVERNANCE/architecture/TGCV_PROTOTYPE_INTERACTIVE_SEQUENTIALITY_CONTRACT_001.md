# Prototipo Interactivo TGCV — Contrato mínimo de secuencialidad 001

- **Estado:** PROPUESTA DE DISEÑO / CONTRATO DE INGENIERÍA; pendiente de revisión y pruebas.
- **Fecha:** 2026-10-14.
- **Ámbito:** demostrador sintético, pequeño, determinista y reproducible.
- **Efecto canónico:** ninguno por sí solo. Este documento no modifica el núcleo científico TGCV, no canoniza una arquitectura y no sustituye silenciosamente el contrato propuesto en `TGCV_COLLECTIVE_TOY_MINIMAL_MATHEMATICAL_FUNCTIONAL_CONTRACT_001.md` (PR #45).
- **Ejecución científica:** no autorizada. No se admiten datos reales ni el artefacto Rust-derived \(U_t\) en este prototipo.

## 1. Decisión de diseño

La siguiente iteración debe formalizar y probar la **secuencialidad mínima de las trayectorias** antes de añadir el puente experimental a outcomes y valor.

El motor no se limitará a enumerar caminos como conjuntos o listas de nodos. Debe representar cada trayectoria como una secuencia ordenada de transformaciones aplicadas a estados sucesivos, respetando las condiciones de aplicabilidad y las dependencias declaradas por el perfil de reglas.

Se conserva la línea base de rendimiento existente como referencia de ingeniería. No se emprenderá una nueva optimización salvo que se observe un problema reproducible de rendimiento en uso real.

## 2. Límites conceptuales no negociables

- \(S\) representa los estados/configuraciones del modelo de ingeniería.
- \(T_{acc}\) sigue siendo el objeto de nivel sistema del marco de trabajo TGCV; **no** se identifica automáticamente con las transiciones habilitadas en un escenario.
- Una transición declarada en el modelo no tiene por qué ser aplicable en todo estado ni estar habilitada en todos los escenarios.
- Una **trayectoria posible** es una secuencia que satisface las reglas del modelo y los límites de exploración.
- Una **trayectoria ejecutada** es el registro de una secuencia seleccionada y efectivamente recorrida durante una ejecución concreta. La enumeración de posibilidades no se presentará como ejecución.
- Los resultados computacionales del prototipo no validan por sí solos TGCV ni demuestran causalidad, creación de valor o inteligencia.
- Outcomes y evaluaciones contextuales del observador pertenecen a una capa separada y quedan fuera del primer contrato de secuencialidad. Ampliar \(T_{acc}\) no implica automáticamente aumentar el valor.

## 3. Modelo mínimo de ingeniería

El perfil inicial trabaja con un sistema finito y determinista:

- **Estado:** identificador técnico estable generado por el prototipo y nombre visible editable.
- **Transformación:** identificador estable, nombre visible, estado de origen y estado de destino.
- **Condición de aplicabilidad:** regla explícita que determina si una transformación puede aplicarse en el paso actual. En el perfil mínimo, exige que el estado actual coincida con el origen declarado y que la transformación esté habilitada en el escenario.
- **Dependencia secuencial operativa:** una transformación puede declarar identificadores de transformaciones que deben haber aparecido antes en la misma secuencia. No se consideran satisfechas por el mero hecho de que estén dibujadas o declaradas en el sistema.
- **Relación descriptiva:** se conserva como documentación y no altera la ejecución.
- **Relación operativa:** solo tiene efecto cuando pertenece a un tipo admitido por una versión explícita del perfil de reglas. En el perfil mínimo, el tipo admitido es la dependencia «requiere que otra transformación haya ocurrido antes». Otros tipos permanecen descriptivos hasta que se especifiquen y prueben.
- **Escenario:** configuración de intervención sobre un modelo común. Puede deshabilitar una transformación o cambiar una condición/dependencia admitida. No reescribe silenciosamente las definiciones base.
- **Punto inicial:** estado desde el que se explora o ejecuta una secuencia.

Las condiciones arbitrarias expresadas en lenguaje natural no se interpretarán automáticamente. Una condición nueva solo será operativa si se representa mediante una regla tipada y versionada.

## 4. Contrato de una secuencia

Una trayectoria finita \(\tau\) se representa como:

\[
\tau = (s_0, t_1, s_1, t_2, s_2, \ldots, t_n, s_n)
\]

Para cada paso \(i\), el motor debe comprobar, en el orden de ejecución:

1. El estado actual es el origen de \(t_i\).
2. \(t_i\) no está deshabilitada por el escenario activo.
3. Se satisfacen todas las dependencias secuenciales operativas de \(t_i\) según el perfil de reglas activo.
4. Se aplica el efecto determinista declarado por \(t_i\), llevando el sistema a su estado destino.
5. Se registra el paso y el estado resultante en el orden real de la secuencia.

Si falla una condición, el paso no se ejecuta. El motor debe indicar qué condición o dependencia impidió aplicarlo; no debe producir una trayectoria válida omitiendo silenciosamente el paso.

Los ciclos están permitidos en el modelo, pero la exploración de secuencias debe respetar los límites explícitos de profundidad y número máximo de trayectorias, e informar si se truncó. La semántica de orden de exploración debe ser determinista y estar versionada.

## 5. Posibilidades, ejecución y procedencia

El motor y la interfaz deben distinguir al menos:

1. **Espacio explorado:** estados y secuencias posibles hallados bajo un modelo, escenario, perfil y límites concretos.
2. **Ejecución concreta:** secuencia seleccionada y recorrida, con sus pasos ordenados y su estado final.
3. **Comparación:** diferencias entre una ejecución o exploración base y la intervención correspondiente.

Cada ejecución conserva una instantánea inmutable de:
- modelo y definiciones de estados, transformaciones y relaciones usados;
- escenario/intervención y condiciones activas;
- perfil de reglas y versión del motor;
- estado inicial y, si aplica, secuencia seleccionada;
- límites de exploración y política de recorrido;
- resultado, errores y aviso de truncamiento;
- identificadores de ejecución, revisión de código disponible y huellas de integridad de las representaciones canónicas.

Una nueva intervención genera una nueva configuración y una nueva ejecución; no sobrescribe el registro anterior. La comparación solo atribuye diferencias a la intervención cuando el resto de las condiciones relevantes se mantiene igual y queda registrado.

Los identificadores de ejecución y las marcas de tiempo son metadatos de procedencia, no propiedades científicas del resultado. Los hashes solo acreditan la identidad de la representación canónica que se haya definido.

## 6. Contrato de experimentación interactiva

Flujo mínimo:

1. El usuario construye un sistema base.
2. El prototipo valida el modelo y presenta su grafo automáticamente.
3. El usuario ejecuta la exploración base y, si lo desea, selecciona una trayectoria concreta para ejecutarla.
4. El usuario crea una intervención: por ejemplo, deshabilitar una transformación o modificar una dependencia operativa admitida.
5. El motor ejecuta de nuevo la configuración intervenida.
6. La interfaz compara estados alcanzables, secuencias posibles, secuencias eliminadas/conservadas, pasos bloqueados y trayectorias concretamente ejecutadas.
7. Ambos registros quedan disponibles para revisión y reproducción.

La interfaz no debe afirmar que una trayectoria «desapareció» sin indicar el límite de exploración aplicado. Si alguno de los resultados está truncado, la comparación debe advertirlo.

## 7. Interfaz UX/UI mínima

El nombre visible pasa a ser **Prototipo Interactivo** (o denominación equivalente aprobada), no «Juguete Colectivo».

La entrada principal es un formulario visual; el usuario describe el sistema, no su formato interno.

- Añadir, editar y eliminar estados mediante controles visuales.
- Añadir, editar y eliminar transformaciones eligiendo origen, destino y nombre.
- Elegir el estado inicial de una lista.
- Añadir relaciones descriptivas o dependencias del tipo admitido, indicando su tipo y elementos relacionados.
- Crear una intervención a partir del escenario base y volver a ejecutar.
- Ver el grafo generado automáticamente para cada escenario.
- Comparar resultados y abrir una secuencia para inspeccionar sus pasos ordenados.
- Mantener profundidad máxima y máximo de secuencias como opciones avanzadas con valores por defecto y aviso de truncamiento.
- Generar automáticamente los identificadores técnicos.

No se exige escribir ni conocer JSON. La edición/importación JSON puede conservarse como vía avanzada o de intercambio, pero no como flujo obligatorio. La importación de grafos e imágenes se incorpora después como otra vía de creación del mismo modelo, siempre con revisión humana antes de validar.

## 8. Outcomes y valor: capa posterior separada

Esta iteración no define una función de valor ni un outcome automático.

Una fase posterior podrá especificar una capa que registre:
- outcome observado o declarado;
- contexto y horizonte temporal;
- identidad y perspectiva del observador;
- criterio de evaluación y justificación;
- incertidumbre y procedencia de la evaluación.

La evaluación contextual no se confundirá con una propiedad intrínseca de la trayectoria. La relación entre transformaciones, trayectoria, outcome y valor deberá someterse a una especificación y evaluación empírica independientes.

## 9. Pruebas reproducibles mínimas antes de aceptar el contrato

La implementación deberá incluir fixtures sintéticos pequeños y expectativas exactas para, al menos:

1. **Orden de pasos:** una secuencia registra transformaciones y estados en el orden aplicado; permutar los pasos no conserva una trayectoria válida si rompe la aplicabilidad.
2. **Continuidad:** no se permite aplicar una transformación cuyo origen no coincida con el estado actual.
3. **Intervención:** deshabilitar una transformación elimina las secuencias que la necesitan y no modifica las definiciones del modelo base.
4. **Dependencia satisfecha:** una transformación con dependencia operativa solo puede aplicarse después de la transformación requerida en la misma secuencia.
5. **Dependencia no satisfecha:** la transformación se bloquea con una explicación explícita; no se genera una trayectoria que la incluya.
6. **Relación descriptiva:** añadir o modificar una relación descriptiva no cambia estados alcanzables ni secuencias.
7. **Repetibilidad:** mismo modelo, escenario, perfil, límites y versión del motor producen los mismos resultados canónicos.
8. **Procedencia:** dos intervenciones generan registros separados que conservan sus configuraciones originales.
9. **Posible frente a ejecutada:** explorar secuencias no crea por sí mismo un registro de trayectoria ejecutada; la ejecución concreta conserva los pasos realmente recorridos.
10. **Límites:** profundidad/cantidad máxima generan un indicador explícito de truncamiento, y la comparación no presenta el resultado incompleto como exhaustivo.
11. **Errores:** referencias desconocidas, dependencias inválidas o condiciones mal formadas producen errores legibles y no un falso PASS.
12. **Concordancia:** cuando existan implementaciones Python y navegador, ambas deben concordar en los fixtures compartidos, incluidos los pasos ordenados y la procedencia semántica del resultado.

Las pruebas deberán documentar entrada, resultado esperado, versión del perfil y criterio de PASS/FAIL. Un PASS acredita conformidad con esos casos, no validez científica general.

## 10. Límites de esta iteración

Incluido:
- contrato mínimo de secuencialidad;
- reglas de aplicabilidad y dependencias explícitas;
- separación entre secuencias posibles y ejecuciones concretas;
- comparación de escenarios con procedencia;
- pruebas sintéticas reproducibles;
- UX basada en formulario.

Fuera de alcance:
- modificación del núcleo científico estabilizado;
- afirmaciones de equivalencia entre el modelo de grafo y el \(T_{acc}\) de nivel sistema;
- procesamiento de datos reales o de \(U_t\);
- inferencia automática de relaciones o condiciones arbitrarias;
- función de valor, reward o utilidad;
- nueva optimización de rendimiento sin problema observable;
- aceptación de OCR/importación de imágenes como vía fiable sin sus propias pruebas estructurales y revisión humana.

## 11. Reconciliación y siguiente gate

Este documento es un **addendum propuesto** al contrato anterior. Antes de implementarlo, revisar expresamente las diferencias con la PR #45 y las capacidades ya presentes en la PR #63, reutilizando los componentes y pruebas compatibles. No reescribir artefactos históricos ni tratar esta propuesta como contrato congelado.

Siguiente gate:
1. revisión del contrato y de sus ambigüedades;
2. mapa de cada regla a una o más pruebas reproducibles;
3. implementación mínima en rama de desarrollo;
4. ejecución de pruebas sintéticas y, cuando proceda, concordancia Python/navegador;
5. revisión de resultados y de la procedencia antes de proponer promoción.

No modificar `main`, no ejecutar experimentos científicos y no optimizar rendimiento como parte de este gate.

## 12. Estado

- Dirección UX/UI: **PROPUESTA REGISTRADA**.
- Contrato mínimo de secuencialidad: **PROPUESTO; PENDIENTE DE REVISIÓN**.
- Pruebas: **ESPECIFICADAS COMO CRITERIOS; TODAVÍA NO EJECUTADAS POR ESTE DOCUMENTO**.
- Implementación: **PENDIENTE DE RECONCILIACIÓN CON LAS PR #45 Y #63**.
- Núcleo científico TGCV: **SIN CAMBIOS**.
- Ejecución científica y uso de datos reales: **NO AUTORIZADOS**.
