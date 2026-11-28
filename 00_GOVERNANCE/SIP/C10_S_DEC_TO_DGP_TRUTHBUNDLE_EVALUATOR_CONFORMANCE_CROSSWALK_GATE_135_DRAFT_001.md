# C10-S — Gate 135: crosswalk DEC → DGP → TruthBundle → Evaluator

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** SOURCE_CROSSWALK_COMPLETED / TRUTH_UNKNOWN_NOT_REPRESENTED / STRICT_EVENT_ADJUDICATION_NOT_REPRESENTED / EVALUATOR_TRUTH_BOUNDS_NOT_IMPLEMENTED / IDEAL_BASELINE_RETAINABLE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.  
**Precedencia:** DEC-C10-100…102; contrato integrado V_cont; Gates 131–134; vcont_integrated_harness.py (blob 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002); test_vcont_integrated_harness.py (blob 1933f9b17cedce919adb3d60ac138d18320ef35e); DGP temporal y de roles.

## 1. Pregunta y dictamen

¿Dónde se rompe la correspondencia entre la semántica temporal aceptada y el recorrido Generator → TruthBundle → Sealer → Analyzer → Evaluator, y qué puede reutilizarse?

**Dictamen:** el punto principal de pérdida está en la construcción de la truth del Generator: los estados ENABLED y PROFILE se generan como secuencias binarias por slot y se combinan mediante la expresión de conjunción entera. No existe un estado funcional tri-valuado ni una secuencia de eventos fechados que permita adjudicar todo incumplimiento intraintervalo. TruthBundle tipa los campos como Any, pero su contenido actual sigue siendo binario. Evaluator compara estimandos de asignación puntuales; no calcula bounds de V_cont derivados de UNKNOWN.

No es una carencia del Sealer: su función es preservar el firewall y no debe recibir TruthBundle. Tampoco se debe introducir UNKNOWN funcional a partir de None de S3.

## 2. Crosswalk de conformidad

| Capa | Implementación recuperada | Requisito DEC | Dictamen |
|---|---|---|---|
| Generator — componentes | ENABLED/PROFILE potenciales por unidad, (Z,G) e intervalo | Truth funcional por intervalo | PARCIAL |
| Generator — conjunción | Conjunción binaria ENABLED AND PROFILE | 1/0/?; 0 ante incumplimiento confirmado; ? solo si Generator no determina truth | NO CONFORME |
| Tiempo | n_intervals, transition_slots, estados por slot | Continuidad estricta en cualquier instante; t0 post-Z y ventana común | PARCIAL; no hay event log ni mapping completo de provisión/instalación acreditado aquí |
| TruthBundle | potential_interval_truth, potential_enabled_truth, potential_profile_truth como arrays de valores actuales binarios | Preservar truth tri-valuada por unidad, régimen e intervalo y provenance | ESTRUCTURA REUTILIZABLE; SEMÁNTICA INCOMPLETA |
| EvidenceCandidate / Sealer | S3 observado con valores 0/1/None; allowlist sin truth | Missingness observacional separada; truth fuera del Analyzer | CONFORME EN PRINCIPIO |
| Analyzer | Ruta puntual condicionada a S3 perfecto/completo; abstención en adversidad | Punto solo si identificado; bounds/abstención cuando proceda | ABSTENCIÓN PARCIAL; BOUNDS NO IMPLEMENTADOS |
| Evaluator | Verifica sello y compara ITT-Z/ITT-G con truths escalares | Abrir truth tras sellado; preservar bounds UNKNOWN | FIREWALL/COMPARACIÓN PUNTUAL EXISTENTES; BOUNDS NO IMPLEMENTADOS |

## 3. Dónde se pierde UNKNOWN y continuidad estricta

### 3.1 UNKNOWN funcional

La pérdida ocurre antes de construir TruthBundle. Las variables aleatorias y los estados ENABLED/PROFILE del código producen valores binarios. La conjunción con int(en and pr) fuerza 0/1. El tipo Any de TruthBundle no añade semántica tri-valuada.

La regla de conjunción que se desprende de DEC-C10-102 es: 0 si existe al menos un incumplimiento funcional confirmado; 1 si ambos componentes están confirmados durante todo el intervalo; ? si no hay incumplimiento confirmado pero el Generator no puede determinar el cumplimiento completo. No debe confundirse con una ausencia de observación.

### 3.2 Continuidad estricta

El código conserva estados por intervalo, no una cronología de transiciones funcionales intraintervalo. transition_slots y la extensión del último estado a slots posteriores no sustituyen un event log. Un evento breve entre slots podría no afectar al estado almacenado y, por tanto, no adjudicarse.

La representación conceptual necesaria, sin fijar parámetros, es una secuencia versionada de transiciones/estados efectivos con tiempo de evento en el reloj normalizado, identidad de componente y procedencia. La adjudicación posterior proyecta esa secuencia sobre los intervalos comunes: cualquier incumplimiento confirmado que intersecte un intervalo lo hace 0; si la secuencia no permite determinar el estado durante todo el intervalo, queda ?. La convención de frontera debe ser determinista, única y versionada como exige DEC-C10-102; Gate 135 no inventa esa convención.

### 3.3 UNKNOWN funcional frente a missingness S3

- Truth ?: incertidumbre del propio Generator sobre el estado funcional verdadero del intervalo, por la definición de DEC-C10-100/102.
- S3 None/MISSING: no hay observación disponible en el canal sellado.
- S3 observado pero erróneo: observación disponible que puede discrepar de truth.
- Lag: separación entre event-time, observation-time e ingestion-time; no cambia retroactivamente truth.

La falta de señal no puede convertir una truth conocida por Generator en ?; tampoco la observación S3 positiva prueba por sí sola cumplimiento continuo.

## 4. TruthBundle y bounds

TruthBundle ya es el contenedor reservado correcto para truth potencial. Puede conservarse como frontera lógica, pero su payload temporal requiere semántica explícita tri-valuada y versionada. Debe mantener separados al menos: estados efectivos/componentes, truth funcional derivada por intervalo, potenciales por régimen, ventana/rejilla y provenance. No se añade ningún campo ni schema en este Gate.

Para cada unidad y régimen, DEC-C10-100 exige conservar:
- n1: número de intervalos con truth 1;
- n0: número con truth 0;
- n?: número con truth ?;
- bounds de V_cont: [n1/K, (n1+n?)/K].

No se imputa UNKNOWN como cero, no se elimina del denominador y no se calcula un punto por complete-case. Los bounds de un contraste causal agregado no se obtienen automáticamente restando extremos marginales sin especificar la estructura conjunta de potenciales, población, soporte e interferencia. Esa cuestión pertenece al contrato de estimando/identificación y permanece abierta; este Gate no prescribe un método.

## 5. Evaluator, sellado y firewall

La secuencia correcta se mantiene:
1. Generator construye la verdad sintética reservada y sus potenciales.
2. Sealer sella únicamente evidencia observacional permitida; no recibe ni expone TruthBundle.
3. Analyzer produce punto, bounds o abstención usando solo evidencia sellada y contrato aprobado.
4. Evaluator verifica el sello y solo entonces abre TruthBundle para adjudicar recuperación/cobertura de punto o bounds.

El Evaluator actual ya verifica el hash del output Analyzer y contrasta los estimandos ITT-Z/ITT-G con verdades escalares. No contiene cálculo ni adjudicación de bounds tri-valuados de V_cont. La comparación puntual existente puede reutilizarse para el baseline binario ideal; no es un oráculo de conformidad completa DEC-C10-100…102.

## 6. Qué se conserva y qué queda pendiente

**Reutilizable sin cambios de alcance:** asignación y potenciales Z/G del benchmark, TruthBundle como frontera de truth reservada, S3/Sealer allowlist, hash y provenance, Analyzer ideal bajo S3 perfecto/completo, test fuente de abstención adversarial y Evaluator para los estimandos de asignación actualmente definidos.

**No acreditado:** truth funcional ?; continuidad estricta mediante eventos intraintervalo; mapping inequívoco t0/provisión/instalación y fronteras; bounds por unidad/régimen en TruthBundle/Evaluator; bounds/recuperación ante S3 imperfecto; bounds causales de θ_A; recuperación de θ_A (sigue theta_a_truth=None).

## 7. Decisiones y límites

Gate 135 no cambia DEC-C10-100…102, contrato integrado, schemas, código, tests, workflows, test register, DGP ledger, RMA, Evidence→Claim Matrix, STATUS, main ni PR base. No fija T*, Δ, K, cadencia, tolerancias, modelo de UNKNOWN, calibración ni método para bounds causales. No crea escenarios ni IDs de test.

**Siguiente operación mínima:** Gate 136 debe auditar los contratos temporales ya existentes (DGP temporal/roles, §16.195–198 y P182/P183/MEAS/MISS) para determinar si ya especifican: fuente legítima de UNKNOWN del Generator, formato/provenance de transiciones, regla de frontera, mapping t0 y forma de adjudicación/bounds. Solo los vacíos reales deberán pasar a decisión de diseño; no se debe saltar directamente a implementación.

## 8. Autorización

Auditoría estática de artefactos GitHub y lectura de código fuente; no se importó ni ejecutó código. No se ejecutaron tests, validadores, workflows, generación, simulación, calibración, estimación o benchmark. No se modificó código ni schema.

scientific_execution=false  
execution_authorized=false
