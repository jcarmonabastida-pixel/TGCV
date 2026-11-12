# C10-S — Reconciliación B1/Need_preZ con el DGP temporal y de roles

**ID:** C10-S-B1-PREZ-TEMPORAL-RECONCILIATION-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / PROPOSED / NOT_APPROVED / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Precedencia:** contrato funcional de adjudicación B1/Need_preZ (Draft 001; estado FUNCTIONAL_WORKING_CONTRACT_ACCEPTED); contrato DGP temporal y roles (Draft 001); contrato mínimo DGP B1/Need_preZ (Draft 001); contrato del paquete analítico B1/Need_preZ (Draft 001); DEC-C10-068/069 y decisiones B1/UE/instancia de servicio/oportunidad estandarizada aceptadas.

## 1. Objeto

Reconciliar la semántica, el tiempo y los permisos de `Need_preZ` entre el contrato funcional de B1, el DGP temporal/roles y el nuevo paquete analítico B1/Need. Este documento no modifica las decisiones aceptadas, no redefine el servicio, no introduce variables de resultado ni fija parámetros.

La reconciliación confirma que Need_preZ es una característica/objetivo basal de B1, no un estado técnico del servicio, no un evento de solicitud y no una consecuencia post-Z. Su truth debe generarse por una estipulación basal explícita y versionada del DGP para cada B1/UE; la evidencia observada se produce mediante un proceso de observación distinto.

## 2. Fuente semántica autoritativa

La definición funcional de trabajo aceptada es la del contrato B1/Need_preZ, §3:

> Antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

`Need_preZ` indica si ese objetivo existe para la B1 concreta antes de Z. No indica si el servicio está habilitado, instalado, disponible, accesible, si una petición se formula o admite, ni si el objetivo se alcanza.

La función del servicio descrita en DEC-C10-068 y su contrato de trabajo es una definición del servicio. No es por sí misma evidencia de que cada B1 tenga ese objetivo. La oportunidad estandarizada (`N_opportunities=1` por UE) es un probe post-snapshot común y no genera ni demuestra Need.

## 3. Regla de generación de truth: contrato sin parámetros

### 3.1 Unidad y ancla

- La truth pertenece a B1, vinculada unívocamente a UE conforme a la decisión aceptada de cardinalidad.
- La instancia lógica de servicio vinculada a esa B1/UE debe ser propia, única y versionada.
- La truth se fija en el baseline `t−1`, antes de Z en `t0`, con referencias a la versión del objetivo basal y a la instancia de servicio pertinente.
- No se añade un nuevo tiempo al reloj t−1/t0…t9.

### 3.2 Mecanismo generador requerido

El DGP deberá materializar, en su espacio reservado, una **especificación basal del objetivo de B1 por unidad**. Esta especificación constituye la fuente generadora de truth, no una fuente observacional para el Analyzer.

La regla de generación debe:
1. producir un estado explícito por B1/UE a partir de una regla basal versionada y reproducible;
2. permitir, en el soporte del diseño que finalmente se apruebe, unidades cuyo objetivo focal exista y unidades para las que esté afirmativamente excluido;
3. reservar `?` para indeterminación explícita de la estipulación generadora, no para falta de evidencia observacional;
4. evitar la asignación automática de Need=1 por pertenencia al microdominio, existencia de B1, disponibilidad de instancia de servicio, función genérica del servicio u oportunidad estandarizada;
5. evitar Need=0 por ausencia de solicitud, documento, registro o actividad;
6. no derivar truth de Z, D2, provisión, instalación, estados técnicos, C_dep, A_f, ΔT_acc, Reach, petición, admisión, procesamiento, respuesta, ejecución, Outcome o Value.

El contrato no selecciona aún qué atributos basales o regla de asignación determinan la especificación por unidad. Esa elección exige reconciliación explícita con el maestro DGP y con el universo cerrado de B1; no se inventan atributos, prevalencias, proporciones, distribuciones, semillas ni parámetros en este documento.

### 3.3 Criterio para truth=0

Truth=0 no significa que no se haya encontrado una declaración. La especificación basal generadora debe establecer afirmativamente que el objetivo definido en §2 no forma parte de los objetivos de esa B1 dentro del universo cerrado del DGP. El modo de representar esa exclusión y su soporte de diseño quedan abiertos.

Truth=? solo se usa cuando la propia especificación basal generadora no determina si el objetivo existe. No se utiliza para ocultar falta de cobertura del proceso de observación.

## 4. Modelo de observación separado

El modelo de observación toma la especificación basal oculta y genera un conjunto de fuentes/evidencias que simula lo que estaría disponible para un adjudicador. La dependencia generativa entre truth y evidencia es admisible y necesaria para que la evidencia pueda informar sobre Need; lo prohibido es copiar la etiqueta de truth, su campo, ID o referencia reservada al paquete visible.

El modelo de observación debe ser especificado separadamente y declarar, sin fijar aún valores:
- probabilidad/regla de emisión de una fuente afirmativa cuando el objetivo existe;
- emisión de una declaración negativa explícita cuando el objetivo está excluido;
- omisión/no disponibilidad de fuentes;
- falsos positivos y falsos negativos;
- ambigüedad semántica y conflictos entre fuentes;
- pérdida, corrupción, captura y error temporal;
- cobertura y universo documental/declarativo que se considera cerrado;
- autoridad, rol, versión y vinculación de cada fuente a B1/UE/servicio.

No se presupone independencia entre fuentes ni una única fuente por unidad. Las fuentes técnicas del servicio solo acreditan hechos técnicos; no acreditan el objetivo de B1 salvo que contengan una afirmación basal explícita y semánticamente pertinente, con autoridad, versión, identidad y temporalidad admisibles.

## 5. Reglas observadas 1/0/?

Se conservan sin modificación las reglas del contrato B1/Need_preZ, §4.2:

- **Observed=1:** evidencia afirmativa admisible, pre-Z, vinculada sin ambigüedad a B1/UE y a la versión pertinente, que respalda el objetivo basal.
- **Observed=0:** evidencia afirmativa admisible y suficiente de que el objetivo no forma parte de la especificación basal de esa unidad, dentro de un universo documental/declarativo cerrado y con cobertura demostrada.
- **Observed=?:** evidencia ausente, incompleta, contradictoria, no versionada, temporalmente ambigua, de alcance incierto o insuficiente.

Una búsqueda sin resultados no permite observed=0. El silencio, la ausencia de petición, la no admisión, la falta de procesamiento o la falta de respuesta tampoco permiten observed=0. La ausencia o insuficiencia de evidencia produce observed=?, no truth=?.

## 6. Inserción en el reloj temporal t−1/t0…t9

| Tiempo existente | Integración de Need_preZ | Restricción |
|---|---|---|
| t−1 / basal | Especificación basal oculta del objetivo B1; truth Need_preZ; vínculo B1–UE–instancia de servicio/versiones; evidencia pre-Z que el modelo de observación consiga producir | Fijar y sellar antes de Z; separar truth y evidencia |
| t0 / asignación | Z y su probabilidad | Z no modifica ni determina retrospectivamente Need |
| t1–t4 | Política, intento, instalación, accesibilidad, ΔT_acc y Reach | Ninguna variable de esta fase redefine Need |
| t5–t9 | Conocimiento, selección, inicio, ejecución, Outcome y Value | No utilizar eventos/resultados para reconstruir Need |

La fila t−1 del contrato temporal deberá tratar Need como atributo/objetivo basal de B1, no como componente de `S_T^*`, `T_acc`, `A_f^*`, `C_dep^*` o `E_T`. La evidencia sobre Need pertenece al expediente epistémico B1/Need; no debe confundirse con evidencia estructural de accesibilidad.

No se introduce un nuevo nodo temporal ni se cambia el orden de la cadena causal. La posición exacta de Request_event sigue la reconciliación ya abierta en el contrato B1; no se desplaza a t−1 por esta propuesta.

## 7. Roles y segregación de información

| Objeto | Generador | Analyzer/adjudicadores E1/E2 | Evaluador |
|---|---|---|---|
| Especificación basal del objetivo y truth Need_preZ | Crear y sellar | Sin acceso | Acceso tras sellado de adjudicación |
| Modelo de observación y semillas/parámetros reservados | Crear y sellar | Sin acceso a truth ni parámetros que revelen la etiqueta | Acceso tras sellado |
| Fuentes/evidencias observables pre-Z | Generar | Acceso al paquete observable permitido | Acceso |
| Reglas públicas de adjudicación y cobertura | Versionar | Acceso | Acceso |
| Adjudicación E1/E2 | No participa en adjudicación | Producir independientemente y sellar | Acceso tras sellado |
| Comparación truth/observed | No reescribe | Sin acceso durante adjudicación | Ejecutar tras sellado |

E1/E2 no reciben truth ni la salida del otro antes de sellar. La apertura de truth para evaluación no puede preceder al sellado inmutable de las salidas que se evalúan.

## 8. Relación con población y análisis causal

Need_preZ no sustituye `E_i`, `P^*_{τ2}`, `App^*(τ2,S0)`, `C_dep,0` o `A_f,0^*`. No es filtro de inclusión ITT ni criterio postratamiento. La población ITT primaria candidata permanece definida por sus reglas propias y no se condiciona a Need=1 ni a solicitud/admisión/procesamiento post-Z.

Si Need se utiliza para estratificación, heterogeneidad, descripción, análisis de consecuencias o definición de una población de Value, ese uso deberá estar declarado ex ante y reconciliado con los contratos de estimandos y población. Este documento no autoriza ajuste, exclusión ni modificación de estimandos.

## 9. Invariantes de reconciliación propuestos

1. Need_truth está vinculado a B1/UE y baseline t−1, antes de Z.
2. La especificación basal es la fuente generadora de truth; no se confunde con evidencia observada.
3. La generación de truth no usa variables post-Z ni estados técnicos derivados de la intervención.
4. No se asigna Need=1 a todas las unidades por defecto.
5. Need=0 requiere exclusión afirmativa dentro del universo cerrado del DGP.
6. Need=? generador no se confunde con observed=? por falta de evidencia.
7. El modelo de observación es separado, versionado y no expone la etiqueta de truth.
8. Observed=0 exige evidencia negativa afirmativa y cobertura suficiente.
9. El silencio y la ausencia de petición no se convierten en Need=0.
10. La oportunidad estandarizada no genera ni demuestra Need.
11. E1/E2 son independientes y sus resultados se sellan antes de evaluar truth.
12. Need no redefine accesibilidad, Reach, elegibilidad ni la población ITT.
13. La evaluación conserva por separado errores de clasificación, indeterminación y cobertura.
14. Ningún registro, parámetro, unidad o fuente se materializa hasta cerrar los gates y obtener autorización.

Estas son pruebas contractuales propuestas; no se han ejecutado.

## 10. Pendientes que no deben cerrarse por inferencia

| Pendiente | Estado |
|---|---|
| Regla concreta que genera la especificación basal por unidad | OPEN |
| Atributos basales que pueden alimentar esa regla | OPEN; requieren fuente en maestro/decisiones |
| Soporte de truth=1/0 y eventual truth=? | OPEN; sin prevalencias ni proporciones |
| Universo cerrado que permite representar exclusión afirmativa | OPEN |
| Catálogo de fuentes semánticamente admisibles | OPEN |
| Mecanismos/parámetros del modelo de observación | OPEN |
| Cobertura/denominadores por unidad y dimensión | OPEN |
| Ubicación técnica y permisos efectivos del paquete | OPEN |
| Reconciliación formal en el maestro temporal/roles | Propuesta pendiente; este documento no lo modifica |

## 11. Dictamen

**TEMPORAL/ROLE RECONCILIATION PROPOSED; BASELINE TRUTH-GENERATION RULE AND OBSERVATION MODEL STILL OPEN.**

La reconciliación inserta Need_preZ en el baseline t−1 como objetivo basal de B1, mantiene separadas truth y evidencia, y asigna permisos coherentes con generador, Analyzer y evaluador. No resuelve qué regla concreta produce heterogeneidad entre unidades ni cómo se generan las fuentes; hacerlo requiere volver a la especificación maestra del DGP y a las decisiones basales pertinentes.

No se crean roster, IDs, truth, fuentes, cobertura, adjudicaciones, código ni fixtures. No se ejecutan validadores, DGP, replay, simulación ni análisis. No se modifica main, RMA, Evidence→Claim Matrix, STATUS, decisiones aceptadas ni estimandos.

`scientific_execution=false`; `execution_authorized=false`.
