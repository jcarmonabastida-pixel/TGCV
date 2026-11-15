# C10-S — Gate 124: auditoría de cobertura de los dos carriles sintético y material D2

**ID:** C10-S-DUAL-LANE-SCOPE-COVERAGE-AUDIT-124  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** DUAL_LANE_SCOPE_RECONCILED / SYNTHETIC_DGP_HARNESS_COVERAGE_AUDITED_DOCUMENTALLY / MATERIAL_D2_REQUIREMENTS_RETAINED / GATE_123_SCOPE_NARROWED / DESIGN_OPEN / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** gobernanza canónica de main; DEC-C10-095, DEC-C10-103; C10-S Synthetic Harness Integrated Specification §§1, 6–9; PE §§8–14 y 15–20; DGP Temporal and Role Contract §§6–10 y 15–17; PD §§1–9 y 15; finite DGP inventory §§14–15; Test Contract Register §§10–12, 17, 22–23; PB Material D2 Reconciliation; Gates 120–123.

## 1. Dictamen ejecutivo

La reconstrucción documental identifica dos carriles que comparten arquitectura causal y vocabulario, pero no comparten el mismo objeto de evidencia ni los mismos criterios de cierre:

**Carril S — experimento sintético / harness metodológico.** Generator crea mundos DGP, unidades, asignación, dependencias, recursos, permisos abstractos, interferencia, potenciales y truth; Projector/Sealer genera y sella evidencia observada imperfecta; Analyzer opera sin truth; Evaluator compara la salida sellada con truth. El objetivo es probar recuperación, límites de identificación, bounds y abstención correctos. No requiere localizar una instancia productiva B1/D2 ni recuperar SBOM, IAM, runtime, logs o snapshots reales.

**Carril M — instancia confirmatoria material D2/B1.** La evaluación confirmatoria de una intervención material necesita identidad y roster reales, IAM/C_SRC, snapshots, dependencias, operación B1, alternativas, recursos, aislamiento/interferencia y soporte observados. Los requisitos materiales de Gate 121 y el expediente de fuentes de Gate 122 pertenecen a este carril. No se satisfacen con artefactos sintéticos ni con el hecho de que el harness conozca truth.

**Conclusión de precedencia:** Gate 123 acertó al corregir la aplicación de los requisitos de infraestructura externa al carril sintético, pero excedió su alcance al declarar supersedidos Gates 121–122 de forma general y eliminar el bloqueo de identificación material B1/D2 del camino C10-S completo. Gate 124 estrecha esa conclusión: Gates 121–122 quedan no aplicables al carril S como requisito de fieldwork, pero se conservan vigentes como contratos documentales de preparación del carril M. Gate 123 no los sustituye en ese carril.

No se ha demostrado todavía aislamiento material D2, fidelidad ejecutada del harness, seguridad efectiva del firewall, recuperación estadística ni identificación de θ_A. No se declara Design Freeze, implementación ni ejecución.

## 2. Evidencia documental reconstruida

| Artefacto | Aporte relevante | Límite explícito |
|---|---|---|
| Synthetic Harness Integrated Specification §§1, 6–9 | Define harness metodológico sintético, DGP con truth conocida, evidencia imperfecta, Analyzer ciego, Evaluator posterior y matriz de gates S/M | No es especificación de instancia confirmatoria material D2; parámetros/escenarios y Value/Outcome permanecen abiertos; harness completo no implementado/ejecutado |
| Finite DGP Inventory §§14–15 | Confirma mundos generados; E1–E4 y B-M01…15 son evidencia sintética; no hay fieldwork ni recuperación de activos reales | Universo finito y reglas generativas no están cerrados ni instanciados |
| PD Reconciliation §§2, 4–9, 15 | Separa truth/observed/evaluation; define familias adversariales, incluido aislamiento e interferencia; fija controles positivos/negativos y límites de atribución | Parámetros, contrastes, soporte, efectos, N/R, potencia, tolerancias y DGP cuantitativo siguen abiertos |
| DGP Temporal and Role Contract §§6–10, 15–17 | Define roles, cegamiento, invariantes DGP-01…16, UE/UA/clúster, potenciales y mapa de exposición | Contrato propuesto; no aprobado íntegramente, sin fixtures ni pruebas |
| PE §§8–14, 16–20 | Define capas V0–V8, firewall lógico, roles y gates técnicos; SR-13 CONDITIONAL, SR-19/20 NOT_ASSESSED | Firewall no implementado; schema físico, ACL, custodia, threat model, logs y pruebas siguen abiertos |
| Test Contract Register §§10–12, 17, 22–23 | Reutiliza contratos adversariales y UNIT-01…14, BND-10…12, BACT-17 | Contratos propuestos; no implementados ni ejecutados |
| PB Material D2 Reconciliation §§1, 8, 11–13 | Conserva el carril material de identidad B1, IAM/C_SRC, dependencias, snapshots e interferencia | MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED |
| Gates 121–122 | Definen suficiencia y fuentes para aislamiento material y su expediente de adquisición | Su lenguaje de sistema B1/D2 concreto no debe trasladarse al harness sintético |

## 3. Crosswalk IS-1…IS-8 por carril

Los estados de esta tabla son una auditoría documental de cobertura de contratos, no resultados de ejecución. "Parcial" significa que existe semántica o contrato reutilizable, pero falta especificación completa, instanciación o verificación. No equivale a PASS.

| IS | Carril S — DGP/harness sintético | Estado S | Carril M — D2 material | Estado M |
|---|---|---|---|---|
| IS-1 Frontera | DGP manifest, scenario_id/version, roster UE/UA, microdominio, universo de unidades, tiempo y versiones. La frontera puede ser declarada por cada mundo sintético; no requiere host/servicio real. | PARTIAL — universo, cardinalidades, escenarios y parámetros aún abiertos | Frontera B1/D2, instancias, entornos, dependencias externas, pools, ventanas y custodios reales | OPEN / NOT MATERIALIZED |
| IS-2 Inventario | Grafo DGP de nodos, aristas, rutas, predicados, recursos, permisos y relaciones de exposición; U_G como modelo lógico y procedencia sintética | PARTIAL — tipos y plantillas definidos; mundo/roster/relaciones aún no instanciados y mappings físicos abiertos | Inventario real por UE/instance, dependencias transitivas, consumidores, snapshots y provenance | OPEN / NO MATERIAL INVENTORY |
| IS-3 Transmisión | Funciones estructurales y potenciales sin interferencia; escenarios con pools, colas, canales, spillovers y mapa G_i; UNIT-02…10 | PARTIAL — familias adversariales definidas; mapas, potenciales y parámetros cuantitativos abiertos | No-transmisión real entre UE, canales, estado mutable, agentes y efectos cruzados | OPEN / NOT EVIDENCED |
| IS-4 Recursos | DGP declara recursos asignados/compartidos, capacidad, demanda, colas, reserva y efectos cruzados; escenarios aislados y rivales | PARTIAL — semántica de recursos y adversarios existe; reglas/cantidades/distribuciones y contrastes aún no fijados | Pools, cuotas, consumo, demanda, prioridad, ventanas y consumidores observados | OPEN / NOT EVIDENCED |
| IS-5 Permisos/datos | Separación lógica Generator/Sealer/Analyzer/Evaluator; proyección allowlist/denylist y permisos del entorno de harness | PARTIAL — contrato lógico definido; firewall efectivo, almacenamiento, ACL, secretos, canales laterales y pruebas no implementados | IAM/ACL, principals, acciones, objetos, namespaces, credenciales y permisos efectivos reales | OPEN / NOT MATERIALIZED |
| IS-6 Alternativas/medición | F*, rutas alternativas, oráculos, medición, missingness, observación diferencial y escenarios adversariales | PARTIAL — familias y reglas candidatas definidas; F*, oráculos, medición, tolerancias y parámetros incompletos | A1/A2/F2, dataset, oráculo y medición reales invariantes/no afectados por B | OPEN / CONTRACTS ONLY |
| IS-7 Tiempo/rollback | Reloj t0–t9, snapshots versionados, eventos, carryover, crossover, resets y replay sintético | PARTIAL — estructura temporal definida; reglas concretas de reset/rollback, ventanas, eventos y replay aún abiertos/no ejecutados | Snapshots pre-B/post-B/rollback comparables, residuos y carryover materiales | OPEN / NONE |
| IS-8 Adjudicación | Truth restringida, observed_evidence sellada, AnalyzerResult inmutable y Evaluator posterior; E1/E2/adjudicación según protocolo | PARTIAL — secuencia lógica definida; firewall efectivo, pruebas, integridad y adjudicación independiente no demostrados | Permisos/custodia reales, bundle material, adjudicación E1/E2 y firewall aplicado a instancia D2 | OPEN / NOT PERFORMED |

## 4. Lectura correcta de los estados y de la evidencia

1. El DGP puede estipular truth estructural de aislamiento para un escenario, pero eso no acredita por sí solo que el harness haya materializado fielmente ese escenario.
2. La fidelidad DGP→artefactos generados requiere correspondencia versionada entre RunManifest, configuración, roster/asignación, grafo, eventos/estados, semillas/compromisos, hashes y provenance.
3. El Sealer debe liberar solo la proyección observacional autorizada; la observación puede ser incompleta, ruidosa, censurada o diferencial.
4. Analyzer puede devolver IDENTIFIED, PARTIALLY_IDENTIFIED, NOT_IDENTIFIED o INDETERMINATE según contrato; un resultado correcto de no-identificación/abstención cuenta como recuperación metodológica correcta.
5. Evaluator solo compara con truth después del sellado inmutable del AnalyzerResult.
6. La ausencia de ejecución de UNIT-02…14 o de pruebas V0–V8 no demuestra interferencia ni ausencia de interferencia: deja sin validar la implementación.
7. Los registros E1…E4 y B-M01…15 del inventario finito son clases de evidencia generada/sintética en el carril S. No son una lista de activos reales a localizar.
8. En el carril M, las fuentes S1…S8 y los requisitos de Gate 122 siguen siendo materiales; una plantilla o un escenario sintético no sustituye una fuente real.

## 5. Corrección de alcance de Gate 123

Se conserva Gate 123 como corrección válida del error de aplicar requisitos de infraestructura externa al experimento sintético. Se limita expresamente su alcance:

- La afirmación "no se necesita localizar infraestructura productiva externa" es válida para construir y evaluar el harness sintético.
- La afirmación "se elimina el bloqueo de identificar sistema externo B1/D2 del camino crítico" solo es válida para el carril S; no para la confirmación material D2.
- "Gates 121–122 supersedidos" debe leerse como "no aplicables como precondición de fieldwork al carril S; conservados como contratos de suficiencia y materialización del carril M".
- La reinterpretación sintética de IS-1…IS-8 y S1…S8 no sustituye el crosswalk material de Gate 122.
- El expediente de Gate 122 no se utiliza para exigir al harness hosts, IAM productivo, custodios, proveedores ni snapshots reales.
- La auditoría documental de Gate 124 no actualiza ni cierra la evidencia material M.

Esta precisión no reescribe Gates 121–123 ni cambia decisiones aceptadas. Establece precedencia interpretativa para su uso posterior.

## 6. Bloqueos del carril sintético que sí impiden Design Freeze

Aunque no se requiera infraestructura externa, el diseño sintético no está cerrado. Permanecen al menos:

- Universo finito definitivo, perfiles R0–R3 y selección mínima no redundante de overlays PD.
- Definición/versionado de escenarios, roster, UE/UA/clúster, mecanismo de asignación y soporte.
- Funciones estructurales, potenciales y contrastes contrafactuales cuantitativos; distribuciones conjuntas, dependencias e interacciones.
- Reglas generativas de recursos, permisos sintéticos, capacidad, canales, carryover y mapas de exposición.
- Parametrización de observación, error, cobertura, pérdida, lag, missingness y censura.
- F*, G, H, ventanas, rutas y oráculos.
- Outcome/Value: Value sigue bloqueado por PA; no inventar dimensiones, escalas, pesos, perspectiva ni horizonte.
- P177/P178/P179/P182/P183: estimandos, supuestos, tolerancias, potencia, N/R y error Monte Carlo.
- Contrato físico, serialización, almacenamiento, control de acceso, secretos y reproducibilidad.
- Firewall efectivo y tests UNIT/GEN/MEAS/MISS/POL/VER/TRJ/INT/PM/SNAP/REACH/PROV/GC aplicables.
- Implementación completa del harness y evidencia de pruebas, bajo autorización específica.

La matriz temporal de predicados sigue siendo propuesta documental, no DGP cuantitativo ni fixture. No se asignan valores truth/observed por escenario por conveniencia.

## 7. Ruta de cierre diferenciada

**Carril S — siguiente trabajo documental:** consolidar el ledger de parámetros y escenarios existentes, cruzando DGP/PD/inventario finito/test register con los cuatro roles y los estimandos. El objetivo es cerrar qué mundos y contrastes son necesarios, cuáles son redundantes y qué parámetros son imprescindibles, sin asignar valores no aprobados. Después se puede evaluar si el diseño queda suficientemente determinado para congelar especificación, sin confundirlo con autorización de implementación.

**Carril M — trabajo posterior separado:** conservar el bloqueo material de Gate 121/122 y PB. Solo cuando exista instancia B1/D2, roster y autorización adecuados se podrá materializar el expediente y adjudicar aislamiento real. No se abre ahora una operación de captura.

No se mezclan resultados ni se permite que un PASS sintético se convierta en PASS material o evidencia empírica de C10.

## 8. Gobernanza y límites

- No se modifica DEC-C10-103, DEC-C10-095/096, C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni main.
- No se cambia el schema U_G ni se crean nuevos IDs de tests/escenarios; se reutilizan los contratos ya citados.
- No se generan mundos, fixtures, datos, seeds, snapshots o bundles.
- No se modifica código ni se ejecuta el harness.
- No se ejecutan validadores, tests, simulaciones, estimaciones, calibraciones o replay.
- No se declara que la porción de implementación focal mencionada en la especificación esté validada por esta auditoría.
- PR #116 permanece Draft.
- scientific_execution=false; execution_authorized=false.

**Resultado:** DUAL_LANE_SCOPE_RECONCILED / SYNTHETIC_IS1_IS8_PARTIALLY_SPECIFIED / MATERIAL_D2_ISOLATION_REMAINS_OPEN / GATE_123_SCOPE_NARROWED / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION.
