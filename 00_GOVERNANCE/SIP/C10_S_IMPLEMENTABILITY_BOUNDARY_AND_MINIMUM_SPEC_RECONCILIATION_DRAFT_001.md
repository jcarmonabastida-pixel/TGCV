# C10-S — Frontera de implementabilidad y reconciliación mínima de especificación

**ID:** C10-S-IMPLEMENTABILITY-BOUNDARY-001  
**Versión:** 001  
**Fecha:** 2026-11-11  
**Estado:** WORKING RECONCILIATION / NOT DESIGN-FROZEN / NOT AN IMPLEMENTATION AUTHORIZATION  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Propósito

Resolver una ambigüedad de los gates PE: la especificación del experimento sintético C10-S se ha evaluado conjuntamente con la factibilidad material de una instancia confirmatoria D2. Esa conjunción sobredimensiona los bloqueos para construir el harness sintético.

Este registro separa dos objetivos que deben conservarse relacionados, pero no confundirse:

1. **Harness metodológico sintético C10-S:** software que genera DGP con verdad conocida, proyecta evidencia imperfecta, analiza sin acceso a truth y evalúa la recuperación/abstención después del sellado.
2. **Instancia confirmatoria material D2:** aplicación de las políticas D2 a unidades, servicios, IAM, snapshots, recursos y resultados con evidencia material suficiente para sostener estimandos confirmatorios.

La separación no cambia el objetivo científico de C10 ni declara identificado el efecto de accesibilidad sobre Value. Es una delimitación de qué evidencia es necesaria para cada objetivo.

## 2. Regla de implementabilidad

La ausencia de roster real, IAM/C_SRC material, snapshots observados, inventario material B o prueba empírica de aislamiento **bloquea la instancia confirmatoria material**, pero no bloquea por sí misma un harness sintético cuyo Generator crea unidades, roster, estados, asignaciones, dependencias y truth bajo un DGP explícito y versionado.

En el harness, esos objetos son datos sintéticos generados y etiquetados como tales; no se presentan como evidencia observada de sistemas reales. La observación imperfecta se genera en un plano separado. El Analyzer solo recibe el bundle observado permitido. El Evaluator accede a truth después de que la salida del Analyzer haya sido sellada.

Por tanto:

- No exigir IAM/snapshots reales para implementar el Generator de escenarios sintéticos.
- Sí exigir que el DGP represente explícitamente las superficies, dependencias, asignaciones, alternativas e interferencias relevantes para cada escenario.
- No inferir que el aislamiento existe en D2 real porque el DGP incluya un escenario aislado.
- No utilizar resultados del harness como evidencia empírica de identificación en D2 material.
- Mantener separados el gate de preparación del harness y el gate de factibilidad confirmatoria.

## 3. Base cerrada que se reutiliza — no reabrir

Los siguientes elementos se consideran decisiones o contratos documentales ya aceptados dentro de su alcance. No se convierten en tareas nuevas:

| Elemento | Estado que se conserva | Límite que no debe borrarse |
|---|---|---|
| Políticas D2 | D2 primario candidato; D1 secundario. B_g0^D2 y B_g1^D2 son políticas asignadas distintas | La asignación experimental Z no está definida por las reglas 0/1 condicionales a Z |
| Población | P*_{τ2} precedencia primaria aceptada; P*_F subpoblación secundaria | La composición material E_i/App y su soporte siguen abiertos |
| B1/UE | Una B1 por UE; identidad de servicio única/versionada por UE; una oportunidad estandarizada por UE | No demuestra aislamiento material ni ausencia de interferencia |
| Propósito basal B1 | Mantener disponible una función de servicio dependiente de la configuración migrada al destino | No asigna Need_preZ=1 a todas las unidades |
| Servicio B1 | Contrato de trabajo de admisión según ENABLED y exposición de PROFILE | No define contenido ni procesamiento posterior de solicitudes, respuesta o éxito de negocio |
| Need_preZ | Baseline pre-Z, truth_dgp separada de observed_evidence, estados 1/0/?; ausencia de registro no prueba 0 | No hay adjudicación material por UE; unknown no equivale a ausencia |
| Cadena causal | B, intento/recepción, instalación, C_dep*, A_f*, D_f*, ΔT_acc*, Reach, trayectoria, Outcome y Value diferenciados | No usar proxies ni derivar un efecto residual por resta |
| Estimandos | ITT de política, primeras etapas, θ_A, θ_Af, LATE_f e IIE C4 separados | No transferir identificación entre ellos |
| Planos computacionales | truth_dgp / observed_evidence / evaluation-adjudication separados | El Analyzer no recibe truth, potenciales ni semillas secretas |
| Roles lógicos | Orquestador, Generator, Proyector/Sealer, Analyzer, Evaluator/Adjudicator y Store | La separación nominal no demuestra permisos efectivos |
| Canonicalización | RFC8785 JCS / TGCV-C10S-JCS-1 solo para envelope U1 de UDG-01 | No generalizarlo a otros bundles o registros |

Fuentes rectoras: secuencia de cierre §19–21; PE; PB-MAT; B2–B3; contratos B1-PREZ; reconciliaciones PA–PD; DEC-C10-066/067/074/095 y decisiones B1 registradas en la secuencia. La precedencia de decisiones aceptadas se conserva.

## 4. Ledger único de implementabilidad

### 4.1 Cerrado documentalmente

- Arquitectura lógica y separación de responsabilidades Generator–Sealer–Analyzer–Evaluator.
- Firewall semántico de truth y regla de sellado previo a evaluación.
- Identidad lógica de servicio por UE y vocabulario de entidades/eventos ya aceptado.
- Estructura basal de Need_preZ y adjudicación trivalente.
- Jerarquía de estimandos y prohibición de atribuciones automáticas.
- Catálogo conceptual de familias adversariales y reutilización de P177–P183, S4R, MEAS y MISS.
- Alcance de JCS en UDG-01/U1.

Estos cierres son reutilizables; no requieren otra ronda de aprobación.

### 4.2 Bloqueos reales para cerrar una especificación ejecutable del harness

Se agrupan en **tres cierres integrados**, no en una lista de paquetes independientes:

**A. Contrato científico ejecutable del DGP y de los estimandos**

Debe quedar escrito, de forma parametrizada y versionable:

- ecuaciones/reglas generativas y orden temporal de los estados/eventos;
- variables exógenas, distribuciones conjuntas, dependencias y parámetros por escenario;
- mecanismo de asignación Z, separado de las reglas de política D2;
- potenciales/contrafactuales necesarios para establecer la verdad de cada estimando;
- escenarios con efecto focal positivo, nulo y adverso; vías colaterales/directas; heterogeneidad; alternativas; interferencia; instrumento débil/defiers; medición imperfecta; missingness y censura;
- condiciones bajo las cuales cada estimando es identificado, parcialmente identificado o no identificado.

La falta de parámetros numéricos confirmatorios no impide definir un DGP parametrizado; sí impide declarar un fixture confirmatorio o validar recuperación cuantitativa hasta que se fijen valores de prueba explícitos y etiquetados como sintéticos.

**B. Contrato de observación, resultados y salida analítica**

Debe quedar implementable sin inventar semántica sustantiva:

- mapping de truth_dgp a observed_evidence, con cobertura, error, missingness, contradicción, procedencia y cegamiento;
- registro genérico de Outcome y de Value vectorial, conservando identificadores y metadatos de cada resultado/dimensión sin seleccionar dimensiones sustantivas V_j por defecto;
- reglas de admisibilidad y propagación 1/0/?/NA, incluida la distinción entre truth y adjudicación observada;
- contrato de salida del Analyzer por estimando y resultado: estimación, incertidumbre, población/soporte, supuestos, diagnóstico de identificación, sensibilidad y abstención;
- contrato del Evaluator para comparar la salida sellada con truth y clasificar recuperación, error y abstención.

El uso de slots genéricos para resultados/dimensiones permite construir el mecanismo de datos, pero no equivale a operacionalizar Outcome o Value ni a validar una afirmación sustantiva ΔT_acc→Value. Para esto último siguen siendo necesarias fichas §224 completas por resultado/dimensión.

**C. Contrato técnico y verificable**

Debe quedar especificado en conjunto:

- schemas físicos/versionados de run, unidad, asignación, eventos, snapshots sintéticos, dependencias, truth, evidencia observada, salida Analyzer y evaluación;
- IDs, claves, cardinalidades, referencias, orden temporal, estados, reglas de ausencia y migraciones;
- serialización/canonicalización por tipo de objeto, sin extender JCS fuera de U1 sin decisión;
- interfaces y errores entre Orquestador, Generator, Sealer, Analyzer, Evaluator y Store;
- controles efectivos de separación/custodia de truth y secretos, aunque la primera implementación sea local;
- contratos de prueba, oráculos, aserciones, tolerancias, criterios de abstención y pruebas de fuga;
- parámetros de reproducibilidad del harness: versiones, semillas, configuración, manifiestos, N/R y error Monte Carlo para los ensayos que lo requieran.

Estos tres cierres son dependencias del mismo contrato integrado. No deben convertirse en ciclos documentales separados si pueden resolverse conjuntamente.

### 4.3 Fuera del bloqueo del harness; necesario para confirmación material

Se mantiene OPEN/BLOCKED, pero no se exige como precondición para construir el harness sintético:

- roster material de UE/B1/servicio;
- IAM/C_SRC, snapshots reales y cobertura de fuentes por unidad;
- inventario real B-M01…15, grafo transitivo, ACL, recursos y evidencia de provisión;
- demostración material de aislamiento/no interferencia o definición de clúster/exposición para D2 real;
- probabilidades/estratos/algoritmo/semilla de la asignación material D2;
- q_X*, positividad y soporte empíricos;
- fichas completas y mediciones materiales de Outcome y Value;
- identificación de θ_A/θ_Af/LATE_f/IIE en la instancia D2 material.

La asignación Z y los escenarios de soporte/interferencia sí deben estar representados en el DGP sintético; lo que se difiere es la afirmación de que esos parámetros/condiciones describen una instancia material real.

### 4.4 Posterior a la especificación

No forma parte del cierre documental actual:

- autorización explícita de implementación;
- implementación y pruebas técnicas;
- ejecución de fixtures/simulaciones;
- auditoría primaria, replay y auditoría final;
- validación científica de recuperación y cierre de claims.

La autorización de implementación y la autorización de ejecución científica son distintas. Este registro no concede ninguna de las dos.

## 5. Relectura de los gates PE

Los gates PE deben leerse según el objeto al que se aplican:

| Gate PE | Harness sintético | Confirmación material D2 |
|---|---|---|
| G-SCI | Requiere DGP y estimandos parametrizados para escenarios sintéticos; puede incluir escenarios identificados y no identificados | Requiere estimandos, resultados y supuestos materialmente defendibles |
| G-MAT | Se satisface mediante fixtures/roster/dependencias generados por el DGP y etiquetados como sintéticos | Requiere roster, IAM, snapshots, provisión, recursos y soporte reales |
| G-SCHEMA | Requiere contratos físicos completos y validables para el harness | Reutiliza schemas y añade mapping/provenance material |
| G-ROLE | Requiere separación efectiva de truth/evidence/evaluation y pruebas de acceso/fuga en el entorno elegido | Añade custodia y seguridad acordes al entorno material |
| G-TEST | Requiere fixtures sintéticos, oráculos, tolerancias y criterios de abstención | Requiere además cobertura y validez de medición confirmatoria |
| G-REPRO | Requiere reproducibilidad de DGP, semillas, versiones, configuración y artefactos | Añade provenance de inputs/materiales reales |
| G-AUTH | Autorización explícita para implementar el harness | Autorización específica para captura/implementación/ejecución confirmatoria |

**Corrección:** G-MAT no puede operar como bloqueo universal de la implementación sintética. Tampoco se debe declarar G-SCI cerrado para el harness si solo existen escenarios cualitativos sin ecuaciones, parámetros y verdad contrafactual explícitos.

## 6. Dictamen actual

- **Especificación lógica:** avanzada y reutilizable; no reiniciar PA–PE.
- **Harness sintético:** todavía no tiene especificación ejecutable completa. Los bloqueos se concentran en A, B y C de §4.2.
- **Confirmación material D2:** no factible/identificada con el inventario actual; sus bloqueos de §4.3 permanecen.
- **Implementación:** no autorizada y no iniciada.
- **Ejecución científica:** no autorizada.

No se afirma que la falta de evidencia material sea ausencia de los objetos, ni que la no-identificación actual sea un efecto nulo.

## 7. Siguiente operación única

Realizar una **reconciliación integrada A–B–C de cierre de especificación ejecutable**, reutilizando los contratos existentes y produciendo un único contrato versionado que contenga:

1. DGP parametrizado y estimandos/condiciones de identificación;
2. contratos de observación, Outcome/Value genéricos y salida Analyzer/Evaluator;
3. schemas físicos, interfaces, roles, pruebas, tolerancias y reproducibilidad.

La operación debe resolver explícitamente qué elementos se parametrizan en fixtures sintéticos y cuáles quedan como extensión material confirmatoria. No volver a abrir B1, D2, población, cardinalidad, identidad de servicio, arquitectura de roles o decisiones JCS ya aceptadas. No añadir requisitos de revisión externa.

**Criterio de salida:** una persona técnica puede implementar el harness sintético sin tener que inferir semántica, inventar campos, elegir estimandos, completar reglas de DGP o decidir cómo se evalúa una salida. Si algo no puede cerrarse sin una decisión científica, debe quedar identificado como una única decisión concreta y acotada, no como una nueva lista de subpaquetes.

No se modifica main, Core, RMA, Evidence→Claim Matrix, STATUS ni claims. No se crean fixtures ni datos y no se autoriza código, simulación o ejecución.  
`scientific_execution=false`; `execution_authorized=false`.
