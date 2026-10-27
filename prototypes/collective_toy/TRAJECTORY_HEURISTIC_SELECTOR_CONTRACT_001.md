# Contrato del selector heurístico de trayectorias TGCV (propuesta 001)

**Estado:** propuesta de diseño; pendiente de revisión.  
**Alcance:** capa aislada del demostrador Full Chain. No modifica el motor TGCV, la evaluación de condiciones, la enumeración de trayectorias ni la ejecución concreta.  
**Naturaleza:** contrato de software para una heurística explicable; no es una teoría validada, un predictor empírico ni una afirmación causal.

## 1. Propósito

Ordenar un conjunto explícito de trayectorias posibles según criterios declarados por el usuario antes de ejecutar una trayectoria. El resultado debe ayudar a comparar alternativas sin presentar el ranking como una predicción validada del éxito ni como una medida universal de valor.

El selector solo consume resultados ya calculados por el motor. No genera trayectorias, no cambia su admisibilidad y no ejecuta la trayectoria elegida.

## 2. Separaciones obligatorias

El sistema debe mantener diferenciados estos objetos:

1. **Trayectoria posible:** recorrido producido por el explorador bajo el modelo, escenario, condiciones resueltas y límites declarados.
2. **Ranking heurístico:** orden relativo derivado de criterios explícitos. No equivale a una probabilidad.
3. **Predicción de resultado:** estimación sobre un resultado futuro, que queda fuera de este contrato y exige un modelo y validación propios.
4. **Ejecución concreta:** recorrido realmente ejecutado y registrado en una traza.
5. **Resultado:** observación vinculada a una ejecución, con su procedencia.
6. **Valor contextual:** valoración ligada a un observador, contexto, criterio y regla de valoración explícitos.

No inferir valor a partir de `T_acc`, `ΔReach`, cantidad de trayectorias, longitud del recorrido o éxito de ejecución. No reinterpretar `NOT_EVALUABLE` como verdadero ni convertir condiciones pendientes en transiciones habilitadas.

## 3. Entrada conceptual

El selector recibe una instantánea de solo lectura que incluya:

- identificador y hash del modelo/resultado de exploración;
- identificador del escenario y estado inicial;
- lista de trayectorias enumeradas por el motor, con sus estados y transiciones ordenados;
- límites de exploración y señal explícita de truncamiento;
- estado de exploración y prerrequisitos temporales tal como aparecen en el resultado del motor; los metadatos condicionales del transcriptor, si existen fuera de ese resultado, no se interpretan aquí como condiciones evaluadas;
- conjunto versionado de criterios heurísticos elegidos por el usuario, con parámetros y unidades cuando proceda.

La interfaz de datos concreta debe reutilizar el esquema vigente en lugar de crear una segunda representación paralela. Los campos ausentes no se completan por inferencia. Si no puede establecerse la correspondencia entre una trayectoria y el resultado de exploración que la originó, el selector debe abstenerse. La implementación debe reutilizar la forma actual del resultado: `scenario_results[scenario_id].trajectories`, junto con `truncated`, `exploration_bounds` y `temporal_prerequisites`; no debe crear una segunda enumeración de trayectorias.

## 4. Criterios permitidos en la primera versión

Cada criterio debe declarar: identificador estable, descripción, tipo (minimizar, maximizar o restricción), fuente de datos, unidad si aplica, tratamiento de ausencia y parámetro configurado por el usuario.

Criterios admisibles si los datos están disponibles:

- número de pasos/transiciones;
- presencia o ausencia de transiciones identificadas explícitamente por el usuario;
- atributos numéricos de coste que estén presentes en el modelo y tengan unidad/semántica documentadas;
- restricciones explícitas configuradas por el usuario y comprobables con los datos disponibles.

No se permite introducir de forma predeterminada pesos de riesgo, probabilidades de éxito, costes monetarios, recompensas o valor percibido que no estén presentes y justificados. La longitud del recorrido no debe etiquetarse como «mejor» en términos absolutos: solo es una preferencia si el usuario selecciona minimizar pasos.

## 5. Ranking y explicación

- La versión inicial usa **ordenación lexicográfica determinista** según el orden de prioridad explícito de los criterios configurados por el usuario. No se implementa puntuación ponderada en esta versión.
- La configuración de criterios, su prioridad, parámetros y unidades debe quedar visible y versionada.
- Las restricciones explícitas son filtros de admisibilidad, no preferencias compensables: una trayectoria que incumpla una restricción se marca `INELIGIBLE` y no puede superar a una admisible por otros criterios. Si ninguna trayectoria es admisible, el selector se abstiene con motivo `NO_ADMISSIBLE_TRAJECTORIES`.
- Para cada trayectoria, el selector devuelve valores de criterios calculados, restricciones satisfechas/incumplidas, clave lexicográfica aplicada y explicación legible de su posición.
- Los criterios de preferencia (minimizar/maximizar) se comparan en el orden configurado; no se agregan magnitudes ni se combinan unidades.
- Los empates sustantivos se conservan como empates. Puede usarse un identificador estable solo para presentar resultados de forma reproducible, indicándolo como desempate técnico sin superioridad sustantiva.
- La ausencia de datos de un criterio activo no se convierte en cero ni en resultado favorable. Salvo que el criterio declare de forma explícita una política de ausencia válida, la comparación afectada queda no evaluable y el selector debe abstenerse de producir un ranking total.
- El ranking es reproducible para la misma instantánea, configuración y versión del selector.

## 6. Abstención y límites

El selector debe emitir estado de abstención o ranking parcial, con motivo explícito, cuando ocurra cualquiera de estos casos:

- exploración truncada: puede ofrecer un ranking de las trayectorias observadas, con estado `PARTIAL_TRUNCATED`, pero debe advertir que el conjunto puede estar incompleto y no afirmar optimalidad global;
- datos obligatorios ausentes o malformados;
- criterio activo que no puede evaluarse para una o más trayectorias y no tiene una política explícita de ausencia;
- incoherencia entre los prerrequisitos declarados en el modelo y los que figuran en el resultado de exploración; el selector no debe crear un estado de condición evaluada que el motor no haya emitido;
- ausencia de trayectorias admisibles (`NO_ADMISSIBLE_TRAJECTORIES`);
- entrada inconsistente o procedencia/hash no verificable (`INVALID_INPUT_PROVENANCE`).

La abstención no debe bloquear ni alterar la ejecución manual normal del demostrador. El selector no debe seleccionar ni ejecutar automáticamente una trayectoria en esta primera versión.

## 7. Salida conceptual y trazabilidad

La salida debe incluir como mínimo:

- versión del contrato y del selector;
- hash/identificador de la instantánea de entrada;
- escenario y estado de exploración (incluido truncamiento y límites);
- criterios, parámetros y política de combinación utilizados;
- lista ordenada de identificadores de trayectoria;
- métricas de cada criterio por trayectoria;
- explicación del orden y de los empates;
- avisos y estado de abstención/ranking parcial;
- declaración explícita: `HEURISTIC_RANKING_NOT_PREDICTION`.

La salida debe poder exportarse o incluirse en el paquete de auditoría sin modificar los artefactos originales de exploración o ejecución. Debe quedar claro que la recomendación fue producida antes de la ejecución, con sello temporal o secuencia de evento y hash de configuración/entrada. No se debe sobrescribir retroactivamente una recomendación cuando se registre el resultado observado.

## 8. Relación con predicción y evaluación posterior

Este contrato no define `P(éxito | trayectoria, condiciones iniciales)`, no entrena modelos y no declara que el primer elemento del ranking vaya a obtener mejores resultados.

Una futura capa predictiva debe tener contrato separado y especificar: definición operacional del resultado de éxito, población/escenarios de referencia, datos de entrenamiento y evaluación, separación entre entrenamiento y prueba, calibración de probabilidades, incertidumbre, baseline comparativo y condiciones de abstención. Las predicciones previas deben conservarse inmutables para compararlas con los resultados posteriores.

La valoración contextual debe continuar separada: `observador + contexto + criterio + regla de valoración + justificación`. Una puntuación contextual no debe tratarse automáticamente como etiqueta objetiva para entrenar un predictor.

## 9. Criterios de aceptación del contrato

La implementación futura debe demostrar, mediante pruebas focalizadas y agrupadas, que:

1. el selector no muta la entrada ni los resultados del motor;
2. con entrada y configuración idénticas produce un ranking idéntico;
3. cambiar la prioridad o dirección de un criterio declarado puede cambiar el orden de forma explicable;
4. la primera versión aplica orden lexicográfico y no usa pesos ni normalizaciones;
5. las restricciones incumplidas producen `INELIGIBLE` y no pueden compensarse con preferencias;
6. datos ausentes o criterios no evaluables producen advertencia/abstención, nunca una ventaja silenciosa;
7. el truncamiento impide declarar que se encontró la mejor trayectoria global;
8. condiciones no evaluables no se tratan como verdaderas;
9. los empates y desempates técnicos se representan explícitamente;
10. el ranking queda ligado por procedencia a la instantánea exacta de trayectorias y a la configuración;
11. la ejecución concreta y la valoración de valor siguen siendo etapas separadas;
12. ninguna salida presenta el ranking como probabilidad, predicción validada, prueba causal o validación científica de TGCV;
13. no se modifica el flujo de ejecución existente para incorporar esta capa.

Estas pruebas validan el contrato de software y la integración, no la validez científica de la heurística.

## 10. Fuera de alcance

- agente LLM como dependencia del selector;
- inferencia semántica general de objetivos del usuario;
- estimación inventada de probabilidades, costes o riesgos;
- optimización global cuando la exploración está truncada;
- ejecución automática de la alternativa mejor clasificada;
- modificación de la arquitectura Core de TGCV;
- afirmaciones de causalidad, valor universal o validación empírica.

## 11. Revisión de compatibilidad con la implementación actual

La inspección de `collective_toy_engine_001.py`, `web/index.html`, `web/cross_runtime_test.cjs` y `web/ui_contract_test.cjs` confirma estas interfaces y límites relevantes:

- El motor devuelve por escenario `scenario_id`, `disabled_transitions`, `enabled_transitions_at_initial_state`, `reachable_states`, `trajectories`, `truncated`, `exploration_bounds` y `temporal_prerequisites`.
- Cada trayectoria es una secuencia ordenada de pasos con estado y, salvo el paso inicial, identificador de transición. El orden de los pasos es semántico y debe conservarse.
- El resultado actual ya expone si la exploración fue truncada y sus límites; el selector debe consumir esos campos en vez de recalcularlos.
- El perfil de motor actual modela prerrequisitos temporales de tipo `requires_prior_execution`. Los metadatos condicionales de la transcripción son un mecanismo distinto: el selector no debe asumir que el motor los evaluó ni debe convertirlos en condiciones verdaderas.
- Las pruebas de navegador y de concordancia entre runtimes ya protegen semánticas de exploración, ejecución y correspondencia TGCV. Las pruebas nuevas del selector deberán añadirse de forma focalizada y evitar duplicar las comprobaciones existentes del motor.
- La UI ya separa trayectorias exploradas, ejecución concreta y valoración contextual. El selector deberá consumir el resultado de exploración y producir su propio artefacto, sin modificar esas etapas.

Esta revisión es de lectura estática de archivos y contratos; no equivale a ejecutar las pruebas ni a demostrar la validez científica del ranking.

## 12. Próximo paso propuesto

Con estas correspondencias fijadas, implementar el selector en un módulo aislado que consuma el resultado existente, seguido de un conjunto pequeño de pruebas deterministas agrupadas. No cambiar el motor, el transcriptor, el evaluador de condiciones ni el flujo de ejecución; no lanzar campañas científicas.

## 13. Corrección de compatibilidad tras la promoción de PR #101

Esta sección prevalece sobre cualquier formulación anterior de las secciones 3, 11 y 12 que pueda interpretarse como autorización para seleccionar trayectorias de estados del sistema.

- **Objeto que se ordena:** exclusivamente las trayectorias de transformaciones TGCV que el demostrador ya haya derivado del grafo TGCV y de las correspondencias efectivas aceptadas. No se ordenan las trayectorias de transiciones del grafo del sistema.
- **Frontera de integración:** el selector no debe consumir directamente `scenario_results[scenario_id].trajectories` del motor de estados como si esas secuencias fueran trayectorias TGCV. Ese resultado solo puede aportar metadatos de exploración/prerrequisitos cuando exista una correspondencia explícita y verificable; nunca sustituye la secuencia de transformaciones TGCV.
- **Entrada requerida:** instantánea inmutable de candidatos TGCV emitidos por el flujo integrado de PR #101, con identificadores ordenados de transformaciones, escenario, procedencia/hash, estado de condiciones y requisitos temporales relevantes, límites y señal de truncamiento si aplica. Si el flujo actual no expone esos datos con procedencia verificable, el selector debe abstenerse; no debe reconstruirlos ni enumerar candidatos por su cuenta.
- **Criterios v1:** limitarse a atributos derivados de la propia trayectoria de transformaciones o a atributos explícitos del modelo que tengan semántica documentada. No trasladar automáticamente el número de pasos o los IDs de transición del grafo de estados al grafo TGCV. Las restricciones sobre transformaciones deben referirse a IDs TGCV explícitos.
- **Separación de etapas:** ranking heurístico previo a la ejecución; ejecución concreta de la trayectoria TGCV elegida; resultado observado; valoración contextual. Ninguna etapa se infiere de otra ni el selector altera la ejecución existente.
- **Condiciones:** una condición pendiente o `NOT_EVALUABLE` nunca equivale a verdadera ni hace admisible una transformación. El selector no implementa ni sustituye el evaluador de condiciones.
- **Pruebas de aceptación adicionales:** (a) una trayectoria de estados del sistema no puede entrar como candidato TGCV por semejanza de estructura; (b) cada candidato conserva el orden y los IDs TGCV de origen; (c) la ausencia de correspondencia/procedencia entre candidatos y grafo TGCV produce abstención; (d) el selector no invoca la enumeración de trayectorias de estados ni vuelve a enumerar transformaciones; (e) la ejecución y la valoración contextual siguen intactas.

**Decisión de integración:** antes de promover la implementación, comprobar que el contrato de entrada coincide con la interfaz real de candidatos TGCV de PR #101. Si esa interfaz no existe aún como artefacto estructurado verificable, detenerse en la revisión del contrato y definir el adaptador mínimo como tarea separada; no asumir que el resultado de exploración del motor de estados satisface el contrato.
