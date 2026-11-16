# C10-S — misión ejecutable y regla de no-dispersión

**Estado:** OPERATIVE RESEARCH-DIRECTION RECORD — 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Ámbito:** exclusivamente el experimento sintético C10-S (carril S).  
**Precedencia científica:** DEC-C10-066/067, DEC-C10-095, DEC-C10-099…104, DEC-C10-103, Gates 145–154, 206–208, Paquetes A y B aceptados, maestro C10-S §§16–324 y contratos especializados vigentes.

## 1. Objeto único e invariable

**El objeto de C10-S es cerrar la materialización del mundo sintético completo y completar el software necesario para ejecutar un experimento sintético reproducible que pueda demostrar, limitar o refutar la contribución causal de la accesibilidad al Value contextual.**

El experimento debe construir mundos con verdad conocida, aplicar intervenciones diferenciadas, producir observaciones potencialmente imperfectas, impedir que el Analyzer acceda a la verdad reservada y permitir que un Evaluator independiente determine si el análisis:
- recupera la contribución causal de accesibilidad cuando el estimando está identificado;
- distingue el efecto total de asignación/paquete del efecto atribuible a accesibilidad y de vías alternativas o directas;
- detecta efectos nulos, positivos, negativos, heterogeneidad, interacciones, interferencia, falta de soporte y no-identificación;
- produce bounds o abstención cuando no existe identificación;
- conecta la contribución a accesibilidad con Outcome y Value contextual. Aplica expresamente VCONT-B1-MIN, aceptada en Gate 128: V_cont es la dimensión sintética acotada de continuidad funcional valorada desde la perspectiva B1; no equivale a Value general, beneficio neto ni a otras dimensiones no instanciadas.

El resultado no está predeterminado. C10-S debe poder producir evidencia favorable, limitante, refutatoria o no concluyente para la hipótesis causal, conforme a los estimandos y criterios preespecificados.

## 2. Qué significa mundo sintético completo

Una instancia ejecutable debe enlazar, por unidad/cluster, escenario, mundo, réplica y potencial:

X, H0, C_c, Need_preZ
→ población objetivo y asignación Z
→ política D2/B y etapas W_programmed, W_attempt, receipt, S_install
→ dependencias técnicas C_dep*
→ admisión funcional A_f*, D_f*
→ T_acc,base*, T_acc,post*, ΔT_acc*=(ΔU*, ΔR*, ΔC*, ΔX*)
→ Reach_H/Π y alternativas/rutas
→ selección/ejecución y trayectoria
→ Outcome técnico y consecuencia
→ Value contextual y sus dimensiones/horizonte.

El mismo mundo debe generar potenciales coherentes para las intervenciones/estimandos registrados. EventHistory y su adjudicación temporal producen la verdad funcional temporal; S3 proyecta esa verdad a evidencia observada sin modificarla. Generator, TruthBundle, Sealer, Analyzer y Evaluator deben intercambiar objetos/versiones compatibles. El Evaluator conserva el oráculo y potenciales reservados; el Analyzer solo recibe evidencia sellada admisible.

D2, EventHistory, S3, q_X*, g_A0/g_A1 y r_common no son módulos demostrativos aislados: deben quedar conectados en una ruta de ejecución de extremo a extremo.

## 3. Disciplina de trabajo obligatoria

1. **Implementar e integrar, no seguir reanalizando el diseño ya aceptado.** Reutilizar el maestro §§16–324, la matriz 13×52, los ledgers, los contratos, el harness, los workflows, los tests y los resultados P178 en su alcance válido.
2. No abrir nuevos Gates, micro-Gates, matrices, registros paralelos ni documentos explicativos por cada campo o función. No repetir auditorías cerradas ni reconstrucciones ya persistidas.
3. La documentación nueva solo se justifica si es estrictamente necesaria para: (a) registrar una decisión científica realmente nueva; (b) especificar una interfaz/cambio de código no determinado por contratos vigentes; o (c) registrar una ejecución, auditoría o resultado material. En los demás casos, actualizar el artefacto rector existente o el propio código/tests.
4. Ante una cuestión ya resuelta por DEC, contrato o aceptación, aplicar directamente la regla. Si el código contradice el contrato, corregir el código; no reabrir la semántica por conveniencia.
5. Elegir parámetros numéricos sintéticos explícitos y versionados cuando sean necesarios para una fixture o escenario. Distinguir parámetros de diseño/fixture de evidencia material; no presentar candidatos históricos como defaults aprobados. No mantener un parámetro eternamente abierto cuando el DGP puede fijarlo como elección sintética falsable y someterlo a sensibilidad.
6. Separar las operaciones: verdad generada, evidencia observada, análisis sellado y adjudicación. Probar la ausencia de fuga de verdad, no limitarse a afirmarla.
7. Mantener separado el carril M. Ningún roster, IAM, snapshot, credencial, evidencia real ni auditoría material es requisito para completar C10-S.
8. No confundir código escrito con código integrado, tests definidos con tests ejecutados, ni ejecución técnica con conclusión científica.

## 4. Orden de implementación por dependencias, no por Gates

La secuencia de trabajo es una ruta de ingeniería única; cada bloque debe cerrarse de forma integrada y con el mínimo de iteraciones:

**I. World builder end-to-end.** Completar el Generator sintético con población/roster, D2 por etapas, potenciales, vector completo ΔT_acc*, Reach/rutas, trayectoria, Outcome y Value contextual. Conectar EventHistory y V_cont a la verdad temporal. Hacer que los objetos sean una instancia coherente, versionada y reproducible.

**II. Intervenciones y verdad causal.** Materializar Z/ITT de paquete, las políticas conjuntas g_A0/g_A1, q_X*, soporte/factibilidad, r_common y potenciales de resultado. Calcular en el Evaluator los estimandos registrados —incluido θ_A cuando sus condiciones se cumplen— a partir de funciones del DGP, no de frecuencias de asignación ni de la salida del Analyzer.

**III. Observación y firewall.** Integrar S3 temporal (cadencia/fase, captura/ingestión, error, missingness, censura y dependencia conjunta) con Sealer y allowlist de evidencia. El Analyzer no recibe truth, potenciales, seeds reservadas, parámetros generadores ni proxies que revelen el mundo/escenario.

**IV. Analyzer y Evaluator.** Implementar estimación e identificación para los estimandos focales sobre evidencia observada; separar ITT-Z, ITT-G/efecto de paquete, efecto de intervención de accesibilidad y mediación si aplica. Incorporar positividad, confusión inducida, vías directas/colaterales, heterogeneidad, interferencia, medición y sensibilidad. El Evaluator compara con truth independiente y adjudica recuperación, bounds, abstención o no-identificación.

**V. Suite integrada y dimensionamiento.** Completar los escenarios nulos, positivos, negativos, directos, colaterales, alternativos, interacción, heterogeneidad, soporte fallido, S3 degradado, missingness, censura e interferencia. Reutilizar P177–P183, el seed-bank protocol, P178 y el paquete v2 donde correspondan; justificar N/R/MCSE para el estimando focal, sin transferir automáticamente el N=700 de P178.

**VI. Preflight y experimento.** Congelar código, configuraciones, parámetros, seeds, dependencias, contratos, hashes y criterios; ejecutar tests, primary/replay y experimento solo bajo la autorización específica que corresponda; auditar integridad y después la conclusión científica.

## 5. Criterio de finalización

C10-S no se considerará completo porque existan documentos o componentes aislados. El objeto estará logrado cuando exista un comando/protocolo reproducible que genere el mundo sintético completo, ejecute la intervención y el pipeline Generator → S3/Sealer → Analyzer → Evaluator, y entregue un paquete auditable que permita concluir, por estimando y escenario:

- contribución causal recuperada dentro de criterios preespecificados;
- contribución limitada o parcialmente identificada;
- ausencia de contribución bajo el DGP y estimando probados;
- no-identificación/abstención correctamente detectada;
- fallo de método o del experimento.

La interpretación final debe distinguir el efecto de asignación/paquete, la contribución de accesibilidad y el puente a Value contextual. No se extrapola a causalidad empírica general ni a todo TGCV sin evidencia adicional.

## 6. Estado y autorización

Esta directriz fija el propósito y la disciplina de trabajo; no modifica estimandos, DEC, DGP congelados, claim status ni Core. La autorización ya registrada en el Paquete B permite implementar y modificar código/tests del carril sintético S en esta rama research.

- implementation_authorized=true — integración y materialización de software S.
- technical_test_execution_authorized=false
- workflow_dispatch_authorized=false
- calibration_authorized=false
- scientific_execution=false
- execution_authorized=false
- material_lane_authorized=false
- main_promotion_authorized=false

La directriz prevalece sobre la inercia conversacional: la continuidad debe recuperarse desde este registro y el código del repositorio. El siguiente trabajo es el siguiente bloque ejecutable pendiente, no otra ronda de documentación.
