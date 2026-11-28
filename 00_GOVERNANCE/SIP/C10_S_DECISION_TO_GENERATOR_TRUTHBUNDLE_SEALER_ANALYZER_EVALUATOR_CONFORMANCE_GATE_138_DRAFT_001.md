# C10-S — Gate 138: crosswalk de conformidad DEC → Generator → TruthBundle → Sealer → Analyzer → Evaluator

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** DEC-C10-104_ACCEPTED / CURRENT_HARNESS_PARTIAL_BASELINE_ONLY / EVENT_LEVEL_TRUTH_NOT_MATERIALIZED / TRI_VALUED_VCONT_NOT_MATERIALIZED / OBSERVATION_FIREWALL_REUSABLE / ANALYZER_BOUNDS_NOT_IMPLEMENTED / EVALUATOR_VCONT_BOUNDS_NOT_IMPLEMENTED / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Objeto y base de inspección

Gate 138 traduce las decisiones aceptadas a obligaciones de conformidad por componente. Reutiliza Gate 135 y el contrato integrado; no crea otra semántica temporal ni una nueva familia de escenarios.

Fuentes: DEC-C10-100…104; Decision Log C10-S; Gate 135; Gate 137 y su aceptación; plan integrado §§16.193–198; DGP temporal §§48–55; contrato integrado V_cont; Test Contract Register P182/P183/MEAS/MISS; y lectura estática de:
- 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py — blob 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002.
- 03_EXPERIMENTS/C10-S/harness/focal_harness.py — blob 8ff4e66f04cbd6f28e95313cf3b8250c29ebe9e2.
- Gate 135 — blob f029a0b90289085007f17e1124636ea8dd9c82bb.

No se ejecutó código, tests, simulaciones, validadores ni workflows.

## 2. Dictamen

El harness integrado ya proporciona una arquitectura útil de DGP sintético con potenciales Z/G, TruthBundle separado, proyección observacional, sellado, Analyzer y Evaluator. Es reutilizable como baseline metodológico para los estimandos y escenarios que realmente implementa.

**No es todavía conforme con la semántica confirmatoria completa de V_cont aceptada por DEC-C10-100…104.** Las discrepancias principales permanecen antes de TruthBundle (la truth se genera como vector binario por intervalo sin event history), en el Analyzer (solo ruta puntual bajo S3 perfecto/completo o abstención) y en el Evaluator (comparación de estimandos ITT escalares, sin bounds de V_cont tri-valuado).

La decisión DEC-C10-104 ya resuelve la asignación de fronteras y la regla conservadora de UNKNOWN. No quedan abiertas esas decisiones; queda implementar y acreditar su representación.

## 3. Crosswalk por capa

| Capa | Estado observado en el harness | Obligación aceptada | Dictamen |
|---|---|---|---|
| Generator — DGP y potenciales | Genera potenciales por unidad y regímenes (Z,G), con exógenas compartidas; calcula ENABLED/PROFILE por intervalos | Construir truth funcional completa por potencial, unidad e intervalo, con identidad/versionado | REUTILIZABLE COMO DGP BASE; SEMÁNTICA TEMPORAL PARCIAL |
| Generator — eventos | No conserva transiciones funcionales fechadas; usa arrays por slot y prolonga el último estado hasta el follow-up | Event history de estados efectivos, event_time, estado previo/posterior, familia, componente, versión y provenance | NO CONFORME |
| Generator — provisión/instalación | provision_ok es un sorteo binario que afecta a delta_vector; no hay cronología diferenciada de provisión e instalación | Ventana desde t0 post-Z que incluye ambos procesos; sus eventos y consecuencias deben estar dentro del soporte | NO CONFORME / MAPPING INCOMPLETO |
| Generator — adjudicación A_B1 | ENABLED AND PROFILE se combina con int(en and pr); truth actual es binaria 0/1 | DEC-100 tri-valuada; DEC-102 continuidad estricta; DEC-104 no fabricar ? y aplicar fronteras versionadas | PARCIAL; 1/0 actual no demuestra continuidad intraintervalo |
| TruthBundle | potential_interval_truth, potential_enabled_truth y potential_profile_truth son arrays Any con valores actuales binarios; contiene potenciales por régimen | Preservar event history, estados componentes, truth por intervalo, potenciales, ventana/fronteras, provenance y bounds individuales | FRONTERA CORRECTA REUTILIZABLE; PAYLOAD TEMPORAL INCOMPLETO |
| Projector / EvidenceCandidate | Filtra TruthBundle; expone asignaciones, observaciones S3, estado de observación, Delta T_acc y provenance | Solo observaciones permitidas; nunca verdad potencial ni provenance privilegiada del Generator | REUTILIZABLE; verificar allowlist contra el contrato de observación al implementar |
| Sealer | Valida allowlist, cardinalidad, estados S3, provenance y hashes; no recibe TruthBundle | Sellar solo proyección observacional, sin exponer truth ni bounds reservados | REUTILIZABLE; mantener el firewall |
| Analyzer | Consume SealedEvidence; exige evidencia completa para calcular; con S3 missingness/medición no identificada añade razones de indeterminación y no estima punto | Punto si identificado; bounds cuando el conjunto identificado lo permite; abstención si no; nunca acceso a TruthBundle | PARCIAL: abstención ideal/adversa existe; bounds de V_cont y corrección por error no |
| Evaluator | Verifica hash/sellos, identidad/provenance y contrasta ITT-Z/ITT-G con verdades escalares | Abrir TruthBundle después de Analyzer; evaluar recuperación de V_cont, cobertura de bounds y abstención correcta | PARCIAL: firewall y comparación ITT reutilizables; adjudicación V_cont tri-valuada ausente |

## 4. Requisitos de representación por componente

### 4.1 Generator

Debe conservar, para cada unidad y cada régimen potencial relevante:
- historia funcional de ENABLED y PROFILE como estados efectivos y transiciones fechadas;
- transiciones con event_time, identidad de componente, familia/causa, estado previo y posterior, versión y provenance;
- eventos de provisión e instalación dentro de la ventana post-Z, sin tratarlos automáticamente como fallo B1;
- estado funcional derivado en cada intervalo conforme DEC-C10-102 y frontera DEC-C10-104;
- truth ? únicamente si una futura estipulación DGP explícita autoriza una indeterminación intrínseca de A_B1.

No se exige inventar un evento si el proceso no cambia de estado; el estado basal y la continuidad deben quedar reconstruibles. No se fija granularidad física, Δ, K o T*. El modelo debe poder detectar cualquier evento representado por su DGP; una limitación de resolución no se convierte en UNKNOWN funcional.

### 4.2 TruthBundle

TruthBundle sigue siendo la frontera privilegiada correcta. Su extensión futura debe preservar identidad, versión y procedencia de la historia; la truth por intervalo no puede derivarse únicamente de la señal S3.

Para cada unidad y régimen, se deben conservar n1, n0, n? y los bounds individuales de DEC-C10-100:

V_cont ∈ [n1/K, (n1+n?)/K]

Bajo DEC-C10-104, una historia completa y determinada no contiene ? por defecto, por lo que sus bounds individuales colapsan a un punto. El soporte de bounds sigue siendo necesario para una futura indeterminación funcional expresamente definida.

No se define aquí un cálculo de bounds para θ_A, ITT-D2 o contrastes causales: no se obtienen restando extremos marginales sin el contrato conjunto correspondiente.

### 4.3 Projector, Sealer y firewall

La frontera de roles actual es valiosa y debe preservarse:
1. Generator produce TruthBundle y datos fuente reservados.
2. Projector expone únicamente evidencia S3 permitida.
3. Sealer valida allowlist, provenance e integridad de la evidencia observada.
4. TruthBundle no entra en Sealer ni Analyzer.

La missingness, lag, error y cobertura de S3 permanecen en el canal observacional. La ausencia de una observación no modifica la truth funcional que Generator conoce. Los tests de firewall existentes pueden reutilizarse como fuente de cobertura, sin declarar que han sido ejecutados o que acreditan el nuevo contrato.

### 4.4 Analyzer

Analyzer debe recibir solo evidencia sellada y contrato público. Para V_cont:
- estimación puntual únicamente cuando medición, cobertura, soporte e identificación lo permiten;
- bounds cuando el conjunto identificado está determinado por el contrato y la evidencia;
- abstención cuando no se puede recuperar ni acotar válidamente.

La ruta actual que exige sensibilidad/especificidad perfectas y missingness cero es una ruta ideal restringida, no una solución general a S3 imperfecto. No se prescribe todavía el método de calibración o corrección ni los bounds de estimandos causales.

### 4.5 Evaluator

Evaluator debe validar primero la integridad del resultado Analyzer y la correspondencia de identidades/versiones/provenance. Solo después abre la truth reservada.

Para V_cont, la evaluación futura debe distinguir:
- recuperación puntual cuando truth y estimación son puntuales;
- cobertura y validez de bounds cuando truth/estimación son interval-valued;
- abstención correcta ante no identificación o evidencia insuficiente;
- errores de Generator/harness, que son fallos de conformidad y nunca UNKNOWN funcional.

El Evaluator actual de ITT-Z/ITT-G se conserva para sus targets escalares; no se presenta como evaluación de bounds V_cont.

## 5. Baseline ideal: alcance que se conserva

Puede reutilizarse:
- la estructura de asignación Z/G y los potenciales comunes del DGP actual;
- TruthBundle como objeto separado de la evidencia;
- Projector/Sealer y sus allowlists, hashes y provenance;
- Analyzer bajo S3 perfecto/completo para los estimandos puntuales ya implementados;
- Evaluator y comparación puntual para ITT-Z/ITT-G;
- perfiles adversariales de S3 y abstención como base para futura ampliación.

No puede afirmarse que ese baseline demuestre:
- continuidad estricta en cualquier instante;
- conformidad con la regla de fronteras DEC-C10-104;
- ventana post-Z con event history separado de provisión e instalación;
- truth funcional tri-valuada y bounds V_cont;
- recuperación de V_cont con S3 imperfecto;
- bounds causales de θ_A o identificación de θ_A.

## 6. Secuencia mínima antes de cualquier cambio de código

1. Reconciliar la representación de tiempo y estados efectivos con DEC-C10-101/102/104: ancla t0, soporte, eventos y asignación de frontera.
2. Especificar el payload lógico de event history y su derivación determinista de A_B1; no añadir UNKNOWN funcional sin un contrato DGP posterior.
3. Especificar la proyección por intervalo a TruthBundle y el cálculo de n1/n0/n? y bounds individuales.
4. Especificar el contrato Analyzer para punto/bounds/abstención bajo S3 ideal e imperfecto, sin filtración de truth.
5. Especificar el contrato Evaluator para recuperación puntual, cobertura de bounds y abstención, preservando el orden del firewall.
6. Reconciliar el conjunto con los contratos existentes y preparar un plan de implementación/versionado separado.

Esta secuencia es diseño de conformidad. No constituye autorización para modificar código, schemas, tests o workflows. No se fijan parámetros temporales ni se ejecuta ninguna operación.

## 7. Estado y autorización

DEC-C10-104 está aceptada y versionada. DEC-C10-100…103 permanecen vigentes. Gate 138 es una auditoría documental y de lectura de código fuente.

No se modifican código, schemas, fixtures, tests, workflows, IDs de test, DGP ledger, RMA, Evidence→Claim Matrix, STATUS, main ni PR base. No se ejecuta código, validadores, workflows, generación, simulación, calibración, estimación ni experimento.

scientific_execution=false  
execution_authorized=false
