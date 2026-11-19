# C10-S — Gate 123: corrección del encuadre de aislamiento y evidencia para el experimento sintético

**ID:** C10-S-SYNTHETIC-ISOLATION-REINTERPRETATION-123  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** HISTORICAL_MISSCOPING_IDENTIFIED / SYNTHETIC_SCOPE_RESTORED / GATE_121_122_EXTERNAL_INFRASTRUCTURE_REQUIREMENTS_SUPERSEDED / DGP_AND_HARNESS_EVIDENCE_CROSSWALK_DEFINED / DESIGN_OPEN / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** gobernanza canónica de main; DEC-C10-095, DEC-C10-103; C10-S Synthetic Harness Integrated Specification; PE Integrated Technical Specification; DGP Temporal and Role Contract; Gate 120; Gates 121–122, solo como registros históricos corregidos en alcance.

## 1. Dictamen

Gate 121 y Gate 122 aplicaron una interpretación material-operativa de aislamiento: exigían identificar un sistema B1/D2 externo, sus hosts, runtimes, pools, IAM efectivo, custodios, servicios, snapshots y fuentes técnicas reales. Esa interpretación no corresponde al objeto del programa C10-S.

C10-S es un **experimento sintético**. Su Generator construye mundos experimentales, unidades, dependencias, recursos, permisos, estados, rutas, interferencia, potenciales y verdad conforme a un DGP versionado. El Sealer/Projector deriva y sella la evidencia observable. El Analyzer trabaja únicamente con esa evidencia permitida. El Evaluator compara la salida sellada del Analyzer con la verdad del DGP después del sellado.

Por tanto:

- No se necesita localizar ni acceder a infraestructura productiva externa para definir o evaluar el aislamiento sintético.
- No son precondiciones de este diseño la existencia de hosts productivos, servicios externos, custodios de infraestructura, IAM real, credenciales, snapshots de un despliegue ni autorización de un proveedor.
- Sí se necesita especificar y, en una fase futura autorizada, verificar que el DGP representa correctamente la arquitectura de aislamiento/interferencia prevista y que el harness materializa esa especificación sin fugas ni contaminación.
- La verdad conocida por Generator no demuestra que Analyzer pueda identificar el efecto a partir de la evidencia observada. Esa capacidad es precisamente una propiedad que el experimento debe evaluar.

**Resultado:** se corrige el objeto probatorio de Gates 121–122. No se declara aislamiento demostrado, no se declara identificación de θ_A, no se cierra el diseño y no se autoriza implementación ni ejecución.

## 2. Reconstrucción histórica y precedencia

| Artefacto | Contenido que se conserva | Corrección de alcance |
|---|---|---|
| DEC-C10-095 | A y B son variantes DGP separadas; B es la extensión de Value | No se modifica |
| DEC-C10-103 | Asignación individual por UE preferida condicionalmente; cluster/exposure map requieren contrato propio si hay interferencia; no mapeable → bounds/abstención | La condición de aislamiento se adjudica primero en el DGP sintético y en la fidelidad del harness, no mediante una auditoría de infraestructura externa |
| Synthetic Harness Integrated Specification | Generator, Sealer, Analyzer y Evaluator; truth restringida, evidencia observada, análisis ciego y evaluación posterior | Es la especificación rectora para el experimento sintético |
| PE Integrated Technical Specification | Responsabilidades, interfaces lógicas, procedencia y firewall entre roles | Se reutiliza; su descripción documental no acredita todavía implementación efectiva |
| DGP Temporal and Role Contract | Unidades, asignación, mecanismos, potenciales, reloj, truth y separación de roles | Se reutiliza en el alcance exacto de sus contratos |
| Gate 121 | IS-1…IS-8, distinción entre compartición, transmisión y consecuencia causal; reglas 1/0/?; alternativas individual/cluster/exposición/bounds | Se conserva como taxonomía conceptual; se descarta la exigencia de inventario de infraestructura productiva |
| Gate 122 | Crosswalk por claim, procedencia, cobertura, triangulación, estados de evidencia y separación de roles | Se conserva como estructura documental adaptable a artefactos sintéticos; se descarta el expediente de adquisición de fuentes externas |

No se reescriben ni borran los Gates 121–122. Permanecen como historial de una interpretación incorrectamente encuadrada. Este Gate 123 los corrige y los sustituye **solo** en cuanto a objeto de evidencia, precondiciones y siguiente operación.

## 3. Cuatro capas probatorias que no deben colapsarse

### 3.1 Verdad estructural del DGP — dominio Generator

El DGP debe definir, antes de generar resultados:

- roster causal de UE y su identidad/versionado;
- unidad de asignación UA y relación UE–UA;
- grafo de dependencias y relaciones entre unidades;
- recursos compartidos/asignados, capacidades, colas, prioridades y reglas de contención;
- agentes, canales, información, estado mutable, side effects y carryover;
- mecanismos de transmisión potencial entre UE;
- reglas de exposición y, cuando proceda, mapa G_i(Z_-i);
- potenciales y funciones estructurales bajo las asignaciones pertinentes;
- condiciones que hacen que una asignación sea aislada, clusterizada o sujeta a interferencia;
- horizonte, ventanas, resets, semillas y versiones del mundo.

La ausencia de interferencia no se define por la mera ausencia de un evento observado en una réplica. Para una arquitectura individual aislada, el DGP debe establecer que los potenciales relevantes de una UE no varían con las asignaciones de otras UE, dentro del alcance definido, o especificar explícitamente las condiciones bajo las cuales esa invariancia se sostiene.

La compartición de un objeto no implica automáticamente interferencia; pero una ruta de transmisión posible que el DGP no haya especificado deja la propiedad como desconocida, no como aislada.

### 3.2 Fidelidad de materialización — dominio del harness

Debe poder establecerse que el mundo generado corresponde al DGP declarado. La evidencia pertinente será sintética y reproducible:

- scenario/DGP manifest y parámetros tipados;
- roster y asignaciones generados;
- grafo sintético de nodos, dependencias y relaciones de exposición;
- configuración efectiva del escenario;
- semillas, streams RNG, versiones y hashes;
- eventos, estados y transiciones generados;
- snapshots/diffs sintéticos cuando el contrato temporal los requiera;
- trazas de procedencia de Generator y del pipeline;
- registros de integridad, cobertura y validación de la correspondencia DGP→artefactos.

Esta capa responde: **¿el harness generó el mundo especificado?** No responde todavía si Analyzer puede recuperar el efecto.

No se presupone que existan todos esos artefactos ya materializados. Su especificación y su eventual verificación deben respetar los gates de autorización vigentes. Este documento no genera mundos, datos ni artefactos.

### 3.3 Evidencia observada y sellada — dominio Sealer/Projector

El Sealer aplica el contrato de observación y produce el bundle permitido para Analyzer. Debe conservarse la distinción entre:

- truth_dgp restringida;
- estados/eventos generados;
- mediciones imperfectas;
- observed_evidence liberada;
- metadatos de procedencia que sí pueden revelarse;
- parámetros, semillas, potenciales y etiquetas verdaderas que deben permanecer reservados.

La cobertura, pérdida, error, lag, aliasing, censura y missingness pertenecen al proceso de observación y no pueden resolverse consultando truth desde Analyzer.

### 3.4 Recuperación y evaluación — dominios Analyzer/Evaluator

Analyzer recibe únicamente el bundle sellado y los contratos permitidos. Debe:

- estimar cuando las observaciones y supuestos identifican el estimando;
- producir bounds o abstención cuando no lo identifican;
- declarar los supuestos y límites que condicionan su salida;
- no acceder a truth, potenciales, semillas secretas ni parámetros reservados.

Evaluator accede a truth solo después de que la salida de Analyzer esté cerrada y sellada. Compara estimandos, intervalos, bounds, abstenciones y errores con la verdad del DGP, sin modificar retroactivamente la salida de Analyzer.

La capacidad de recuperación es un resultado del experimento, no una propiedad que pueda inferirse del conocimiento del Generator.

## 4. Reinterpretación de IS-1…IS-8 para el mundo sintético

| Condición histórica | Objeto correcto en C10-S | Evidencia sintética pertinente | Qué no debe exigirse |
|---|---|---|---|
| IS-1 — Frontera | Universo DGP: roster, unidades, versiones, escenarios, tiempo y límites del mundo generado | DGP manifest, roster versionado, definición de escenarios y ventanas | Inventario de hosts, proveedores o entornos productivos |
| IS-2 — Inventario | Componentes y relaciones del mundo sintético | Grafo DGP, nodos/aristas tipados, dependencias, consumidores, provenance | Descubrimiento runtime de un sistema externo |
| IS-3 — Transmisión | Mecanismos de interferencia potencial y exposición entre UE | Funciones estructurales, grafo de transmisión, potenciales, mapa G_i cuando aplique | Logs reales para inferir si el DGP contiene interferencia |
| IS-4 — Recursos | Compartición, capacidad, rivalidad y contención definidas por el DGP | Parámetros de capacidad/demanda, colas, prioridades, asignación de recursos y efectos cruzados generados | Cuotas o consumo de pools productivos |
| IS-5 — Permisos/datos | Reglas sintéticas de acceso, visibilidad y separación de roles | Contratos de acceso, proyección de campos, allow/deny, manifests de truth/observed y registros de acceso del harness | IAM, credenciales o ACL de producción |
| IS-6 — Alternativas/medición | Invariancia o variación definida ex ante de alternativas, F*, medición y oráculos | Versiones/hash de reglas y oráculos, configuración de medición, escenarios de no-afectación y controles | Auditoría de sistemas externos A1/A2/F2 desplegados |
| IS-7 — Tiempo/rollback | Dinámica temporal, persistencia, reset y carryover entre unidades/réplicas | Eventos temporales, snapshots sintéticos, estado inicial/final, reglas de reset y semillas | Snapshots productivos pre/post/rollback |
| IS-8 — Adjudicación | Firewall lógico y efectivo entre Generator, Sealer, Analyzer y Evaluator | Contratos de interfaz, bundles sellados, hashes, trazas de acceso, orden temporal y evaluación posterior | Custodios externos o revisión humana ficticia |

Las condiciones mantienen la regla de que una propiedad no especificada o no cubierta no se convierte en ausencia. Pero deben distinguirse dos niveles de estado:

1. **Truth del DGP:** valor definido por la especificación generativa para una propiedad estructural dentro del alcance.
2. **Conocimiento del Analyzer:** estado recuperable desde observed_evidence, que puede ser 1/0/? o bounds/abstención según cobertura e identificación.

Un truth conocido por Generator puede coexistir con Analyzer=? o NOT_IDENTIFIED. No es contradicción: es un resultado central que el benchmark debe poder detectar.

## 5. Reinterpretación de las clases S1…S8 y U_G

Las clases de fuente S1…S8 de Gate 122 pueden conservarse como taxonomía de artefactos, con esta adaptación:

| Clase | Uso en experimento sintético |
|---|---|
| S1 — declarativa | DGP manifest, scenario manifest, roster, versiones, parámetros tipados, semillas declaradas cuando sean revelables |
| S2 — configuración/control | Configuración efectiva del Generator/harness, políticas de asignación, reglas de visibilidad y permisos sintéticos |
| S3 — runtime | Eventos, trazas y métricas producidos por la ejecución sintética futura, cuando esté autorizada |
| S4 — snapshots/integridad | Estados y snapshots sintéticos, hashes, diffs y referencias temporales |
| S5 — contrato/interfaz | Schemas, contratos de Generator→Sealer→Analyzer→Evaluator y formatos de evidencia |
| S6 — funcional independiente | Oráculos, controles de conformidad y verificaciones cegadas del comportamiento del harness, según contrato |
| S7 — documentación | Especificaciones, decisiones, mappings, rationale y límites del DGP |
| S8 — inferencia analítica | Análisis estático del grafo DGP, cierre de dependencias, comprobaciones de invariantes y análisis de trazas |

U_G puede reutilizarse como vocabulario de procedencia, identidad, cobertura y adjudicación **solo cuando sus contratos vigentes admitan el objeto sintético correspondiente**. Este Gate no declara que todos los tipos U_G puedan representar cualquier artefacto del harness; no crea campos, schemas, registros físicos ni nuevas filas. Cualquier incompatibilidad real debe documentarse y resolverse mediante el proceso de gobernanza aplicable antes de cambiar U_G.

## 6. Criterio de adjudicación de aislamiento e interferencia

La arquitectura de asignación individual UE=UA de DEC-C10-103 se evalúa dentro del DGP, no mediante la inspección de un sistema externo.

- **Aislado por construcción:** el DGP define las relaciones entre unidades y establece invariancia de los potenciales relevantes respecto de asignaciones ajenas, con límites de alcance explícitos.
- **Interferencia estructural especificada:** el DGP incorpora rutas de transmisión, recursos/estados compartidos o funciones de exposición. Se requiere UA/cluster o mapa G_i y su contrato propio antes de usar estimandos compatibles.
- **Interferencia no especificada o incompleta:** la arquitectura individual no se considera demostrada. El diseño debe permanecer OPEN o generar escenarios explícitos de incertidumbre; no se asume SUTVA por omisión.
- **Interferencia no mapeable:** Analyzer debe producir bounds/abstención o no identificación según el contrato; el Evaluator determina si esa abstención es correcta frente a truth.
- **Fidelidad del harness no verificada:** aunque el DGP describa aislamiento, no se declara que el mundo materializado cumpla esa especificación hasta que exista evidencia autorizada de correspondencia DGP→harness.

No se exige que todos los escenarios del benchmark sean aislados. Para evaluar robustez del Analyzer, el diseño puede incluir escenarios aislados, escenarios con interferencia conocida y escenarios con interferencia parcial/no identificable, siempre que estén preespecificados y versionados. La elección de escenarios y su papel confirmatorio requieren el cierre de los contratos DGP/estimandos correspondientes; no se introducen parámetros por defecto aquí.

## 7. Reglas de no contaminación y validez

1. Generator mantiene truth y parámetros secretos fuera del dominio de Analyzer.
2. Sealer no modifica truth y solo libera campos autorizados por el contrato de observación.
3. Analyzer no accede a truth ni a identificadores/metadatos que permitan reconstruirla indebidamente.
4. La salida de Analyzer se congela y sella antes de que Evaluator abra truth.
5. Evaluator no reescribe la salida ni permite feedback retroactivo a Analyzer dentro de la misma evaluación.
6. Seeds, streams RNG y versiones deben permitir reproducibilidad sin convertir semillas secretas en observables.
7. Las pruebas futuras de firewall deben distinguir presencia de contrato, implementación del control y evidencia de su funcionamiento; un diagrama o especificación no equivale a PASS técnico.
8. Los controles de recuperación estadística deben incluir escenarios donde la verdad sea conocida pero la observación insuficiente, para verificar bounds/abstención en vez de recuperación artificial.

## 8. Estado corregido de Gates 121–122

| Afirmación anterior | Dictamen corregido |
|---|---|
| No se ha identificado un sistema externo B1/D2 | No es un prerequisito del experimento sintético; se retira como bloqueo |
| No hay hosts, runtimes, IAM, custodios ni fuentes productivas identificados | No pertinente para el alcance sintético; no buscar ni inventariar |
| No existe inventario material de infraestructura | Sustituir por el estado de especificación/materialización de artefactos DGP y harness, sin asumir que ya estén generados |
| IS-1…IS-8 no pasan porque no hay evidencia runtime externa | Dictamen inválido para C10-S sintético; deben adjudicarse con truth DGP, fidelidad del harness, evidencia sellada y firewall por separado |
| UE=UA es condicional hasta auditoría de infraestructura material | UE=UA se evalúa por escenario DGP y por fidelidad de materialización; DEC-C10-103 sigue siendo condicional, no se convierte en PASS automático |
| Debe identificarse un sistema y custodios antes del siguiente gate | Se elimina; el siguiente trabajo es reconciliación documental de contratos sintéticos existentes |

Los Gates 121–122 no deben citarse como prueba de que el aislamiento sintético ha fallado ni como prueba de que el aislamiento está demostrado. Su resultado útil es la taxonomía de riesgos, cobertura, procedencia y adjudicación, una vez reinterpretada.

## 9. Consecuencias para estimandos y diseño

No se modifica la jerarquía aceptada por DEC-C10-103:

- ITT-D2 sigue siendo el efecto total de asignación al paquete.
- θ_A(q_X*, r_common; V_cont) sigue siendo el objetivo focal de atribución sobre el vector completo ΔT_acc*, condicionado a intervención factible, soporte e identificación.
- C4 sigue siendo mediación interventional longitudinal secundaria y condicionada.
- No se calcula un efecto directo o residual por resta.

El escenario DGP debe hacer explícito qué arquitectura de asignación/interferencia hace válido cada estimando. Un DGP aislado puede permitir evaluar el target UE-promedio; un DGP con clusters o exposición requiere sus propios potenciales, probabilidades, soporte y unidad de inferencia. El hecho de que el Generator conozca el estimando verdadero no prueba que el Analyzer lo pueda recuperar.

## 10. Gobernanza, límites y siguiente operación

- No se modifican DEC-C10-103, DEC-C10-095, C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni main.
- No se reescriben los Gates 121–122; se conserva su historial y se limita su validez mediante esta corrección.
- No se crean nuevos test IDs, schemas, columnas ni registros U_G.
- No se generan DGP, fixtures, datos, snapshots ni bundles.
- No se modifica código, Generator, Sealer, Analyzer o Evaluator.
- No se ejecutan tests, validadores, workflows, simulaciones, estimaciones, calibraciones o experimentos.
- PR #116 permanece Draft.
- scientific_execution=false; execution_authorized=false.

**Siguiente operación:** Gate 124 — auditoría de cobertura del DGP/harness sintético existente frente a IS-1…IS-8, reutilizando la especificación integrada del harness, PE, DGP temporal/roles, matriz temporal y contratos de evidencia. El objetivo será identificar qué propiedades ya están especificadas, cuáles están parcialmente especificadas y cuáles siguen OPEN, sin inventar parámetros ni implementar o ejecutar.

**Resultado:** GATE_123_SYNTHETIC_SCOPE_CORRECTED / GATE_121_122_EXTERNAL_SYSTEM_FRAMING_SUPERSEDED / DGP_TRUTH_SEPARATED_FROM_ANALYZER_IDENTIFICATION / HARNESS_FIDELITY_OPEN / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION.
