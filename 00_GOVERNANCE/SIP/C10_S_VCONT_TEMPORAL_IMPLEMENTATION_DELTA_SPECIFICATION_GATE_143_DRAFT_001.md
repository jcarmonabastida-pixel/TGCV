# C10-S — Gate 143: delta único de implementación temporal para V_cont

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Base normativa:** Gate 142; DEC-C10-100…104; Gate 139; DGP temporal §§48–50, 52–55 aceptados parcialmente como especificación de trabajo.  
**Estado:** IMPLEMENTATION_DELTA_SPECIFIED / CURRENT_BENCHMARK_RETAINED_AS_LIMITED_BASELINE / NO_CODE_CHANGE / NO_TEST_EXECUTION / NO_DESIGN_FREEZE / IMPLEMENTATION_AUTHORIZATION_REQUIRED.

## 1. Objeto y alcance

Preparar un único delta trazable para que el harness sintético integrado represente la semántica temporal aceptada de V_cont. El delta se limita al carril sintético y al harness integrado:

- 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py
- 03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py
- contratos y schemas directamente consumidos por estos componentes, solo si el preflight demuestra que es necesario.

No modifica el carril material D2, no convierte la simulación en evidencia material, no cambia ITT-Z/ITT-G por θ_A y no resuelve las cuestiones abiertas de q_X*, g_A, r_common o identificación de θ_A.

## 2. Reconstrucción de implementación existente

Inspección estática del blob actual de vcont_integrated_harness.py (SHA 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002):

1. ScenarioConfig obliga a n_intervals ≥ 2, window_start, last_transition_support y follow_up numéricos, y calcula una rejilla uniforme de intervalos. Exige que el soporte de transición termine en frontera de intervalo.
2. Generator crea potenciales [unit][z][g]. Para cada régimen genera ENABLED y PROFILE por intervalo mediante sorteos u_enabled/u_profile; luego deriva estado de intervalo como conjunción binaria y V_cont como media de esos estados.
3. provision_ok se genera como un indicador binario por régimen; no conserva una cronología de programación, intento, recepción, instalación y transición funcional.
4. TruthBundle conserva potential_interval_truth, potential_enabled_truth y potential_profile_truth, pero no un EventHistory ni un estado funcional trivalente adjudicado a partir de eventos.
5. S3 se genera separadamente: observaciones 0/1 o None y status OBSERVED/MISSING. Esta missingness ya es distinta de los arrays de truth.
6. Sealer valida una allowlist cerrada y conserva únicamente evidencia observacional y asignaciones; Analyzer comprueba integridad, completitud y estado S3, y se abstiene cuando no se cumplen sus condiciones de identificación.
7. Evaluator abre TruthBundle después de recibir AnalyzerResult sellado y evalúa los estimandos de asignación ITT-Z/ITT-G y sus estados. No contiene todavía una adjudicación EventHistory→A_B1→V_cont con bounds de verdad temporal.

La baseline es por tanto una implementación funcional de benchmark limitada, no una representación de continuidad estricta intraintervalo.

## 3. Delta propuesto — una única cadena de materialización

### D1. EventHistory generado por régimen potencial

Extender la salida interna del Generator con una historia de eventos sintéticos para cada unidad y régimen potencial (z,g), manteniendo las exógenas compartidas y la coherencia entre potenciales.

La historia debe distinguir, como mínimo:
- eventos de proceso: W_programmed, W_attempt, receipt y S_install;
- eventos de estado funcional que cambian ENABLED y/o PROFILE;
- identificador de unidad, régimen potencial, identidad/versión del objeto funcional, orden del evento, tiempo efectivo y provenance sintética;
- tiempo de evento (event_time) separado de captura, observación e ingestión S3.

Los eventos de proceso no son automáticamente fallos B1. Solo las transiciones efectivas de ENABLED/PROFILE y las condiciones funcionales constitutivas de admisión afectan A_B1. Los estados persistentes se mantienen hasta una transición posterior explícita.

No fijar en este delta unidad física de tiempo, coordenada normalizada, cadencia, resolución, Δ, K, T* ni τ_follow. Hasta que esos parámetros se aprueben, la representación temporal debe preservar orden/comparación exactos y permitir la asignación posterior a fronteras, sin asumir una escala numérica concreta. La materialización final depende de la resolución de §51 y del soporte común.

### D2. Adjudicador de truth temporal

Añadir una capa determinista que consuma EventHistory y el contrato temporal versionado y produzca para cada unidad/régimen/intervalo:
- truth de ENABLED y PROFILE;
- A_B1 ∈ {1,0,?};
- razón y eventos causales que soportan la adjudicación;
- cobertura de la historia temporal necesaria para afirmar 1 o 0.

Aplicar DEC-C10-102: continuidad estricta; cualquier incumplimiento funcional confirmado en cualquier instante del intervalo adjudica A_B1=0 en ese intervalo. El estado 1 requiere evidencia completa del DGP/historia de que la función se mantuvo conforme durante todo el intervalo. Aplicar fronteras y regla UNKNOWN de DEC-C10-104 sin reinterpretarlas.

El valor ? solo puede emitirse por la estipulación explícita de indeterminación funcional del Generator/DGP autorizada por DEC-C10-104. Un hueco en S3, un evento de observación tardío, un error de medición o una historia truncada por defecto de implementación no se convierten en ? funcional: son missingness/defecto de observación o de harness y deben producir un estado de canal/validación separado.

### D3. TruthBundle versionado y V_cont bounds

Preservar la estructura y el contrato de TruthBundle actual para la baseline histórica. Para la nueva ruta temporal, añadir una representación versionada que transporte:
- EventHistory o su referencia/hash íntegro;
- adjudicación A_B1 por intervalo para cada potencial (unit,z,g);
- conteos n1, n0, n? y K por unidad/régimen;
- V_cont truth puntual cuando no hay UNKNOWN y bounds cuando exista UNKNOWN explícito;
- versiones de decisiones, DGP, regla temporal, Generator y adjudicador.

Por DEC-C10-100, con K fijado por un contrato futuro:
V_cont ∈ [n1/K, (n1+n?)/K].
No imputar ? como 0, 1 ni como missing S3. Si K o la rejilla no están aprobados, no calcular un número confirmatorio: conservar los conteos y la expresión simbólica, y marcar el estimando temporal como no materializable.

No duplicar los potenciales existentes ni crear una segunda verdad independiente: el nuevo V_cont se deriva de EventHistory y se convierte en la fuente de verdad temporal de la versión sucesora del benchmark. El benchmark actual queda preservado como baseline limitada y comparador histórico.

### D4. S3 y Sealer: canal de observación independiente

Mantener el canal S3 separado de EventHistory y truth. Las observaciones deben permitir distinguir event_time (si está disponible como señal), capture_time, observation_time y ingestion_time; además, status OBSERVED/MISSING/DELAYED/INVALID y provenance/versiones.

El Sealer conserva allowlist estricta de datos observacionales, asignaciones y metadatos autorizados. Rechaza EventHistory oculto, A_B1 truth, potenciales, n1/n0/n? y cualquier parámetro secreto. No pasar truth ni referencias que permitan recuperarla al Analyzer.

No convertir una observación ausente/tardía en verdad funcional desconocida. La falta de cobertura S3 debe seguir siendo condición de identificación del Analyzer.

### D5. Analyzer inicial: ruta ideal y abstención

Conservar el alcance aceptado en Gate 140/142:
- estimación puntual solo cuando S3 sea perfecto, completo, coherente en versión y el estimando de asignación correspondiente esté identificado;
- ante missingness, lag, error o soporte/condiciones no satisfechos sin corrección aprobada, emitir INDETERMINATE/abstención;
- no implementar complete-case substitution;
- no implementar bounds de Analyzer en este delta.

No relabelar ITT-Z ni ITT-G como θ_A. Los bounds de truth de DEC-C10-100 son un producto del Generator/Evaluator y no equivalen a bounds inferidos por Analyzer.

### D6. Evaluator: adjudicación posterior al sellado

Después de validar identidad, hashes, versiones y sellado de AnalyzerResult, Evaluator abre TruthBundle temporal y:
- compara el estimando de asignación implementado con la truth temporal correspondiente, nunca con un target de distinta identidad/versión/régimen;
- evalúa estimación puntual, abstención esperada y errores de medición por separado;
- reporta por separado truth bounds (si hay ? explícito) y salida/estado del Analyzer;
- no trata un resultado Analyzer INDETERMINATE como error numérico ni como recuperación;
- conserva resultados previos ITT-Z/ITT-G como controles del benchmark, sin atribuirlos a θ_A ni a mediación causal.

## 4. Orden de implementación y dependencias

Orden mínimo de la futura intervención, una vez autorizada:

1. congelar/identificar la versión del contrato temporal de implementación y resolver §51/los parámetros necesarios para materializar tiempo y fronteras;
2. EventHistory y generador de eventos por potencial;
3. adjudicador estricto A_B1;
4. TruthBundle temporal versionado y bounds de truth;
5. proyección S3 y allowlist del Sealer;
6. Analyzer ideal/abstención;
7. Evaluator y reportes;
8. tests de conformidad, firewall, fronteras, episodios breves, unknown explícito, S3 missing/delayed/error y replay/provenance.

Los tests de la lista son requisitos futuros, no se ejecutaron ni se crearon en Gate 143. No se debe codificar una rejilla numérica provisional para sortear §51 abierto. Si el orden temporal exacto no puede materializarse sin resolver una decisión pendiente, detenerse en el preflight y elevar solo esa dependencia.

## 5. Reutilización y preservación

- Reutilizar DEC-C10-100…104, DGP temporal parcialmente aceptado, Gate 139, Path Predicate Temporal Evidence Matrix, Integrated V_cont Analysis Contract, P182/P183 y MEAS/MISS.
- Reutilizar los perfiles adversariales y los IDs de pruebas ya registrados; no crear nuevos escenarios/IDs salvo gap probado en el preflight.
- Preservar la baseline actual y sus resultados/hashes. La versión temporal sucesora debe tener identidad y hashes independientes; no sobrescribir los artefactos de benchmark anteriores.
- Mantener Generator/TruthBundle ocultos al Analyzer; Evaluator accede después del sellado.
- Separar evidencia de fidelidad del DGP/harness de evidencia de recuperación estadística del Analyzer.

## 6. Criterios de aceptación del delta (preflight futuro)

El preflight deberá demostrar documentalmente, antes de ejecutar:
- trazabilidad campo/función → decisión/contrato;
- que todo evento funcional que pueda cambiar A_B1 está representado y ordenado;
- que los eventos de provisión/instalación no se confunden con fallo funcional;
- que la adjudicación de continuidad estricta respeta las fronteras versionadas;
- que ? funcional no puede derivarse de S3 missingness ni de un defecto del harness;
- que truth bounds y Analyzer bounds no se mezclan;
- que el Sealer bloquea cualquier truth oculta;
- que la ruta ideal y la abstención no contaminan el estimando ni la salida;
- que la baseline anterior permanece reproducible e intacta.

El preflight y las pruebas requieren autorización independiente. Gate 143 no declara PASS.

## 7. Dependencias que impiden implementación inmediata

No está autorizado implementar todavía. Además, la materialización completa depende de:
- resolución explícita del §51 (coordenada, anclaje, soporte temporal y mecanismo S3) o de una especificación alternativa aprobada;
- selección de unidad temporal y forma exacta de event_time;
- T*, Δ y K, incluido soporte común y τ_follow;
- reglas de captura/observación/ingestión y calibración S3 para cualquier ruta no ideal;
- confirmación de que el contrato temporal sucesor conserva compatibilidad con el benchmark y los estimandos actuales.

No se deben inferir estos parámetros desde n_intervals, H, t0…t9 ni cadencia de S3.

## 8. Resultado y límites

Gate 143 deja preparado un delta único, aditivo y versionado. No modifica código, tests, schemas físicos, DGP original, DEC, Decision Log, RMA, Evidence→Claim Matrix, STATUS, main ni PR base. No se ejecutaron pruebas, simulaciones, calibración, workflows ni experimentos.

La preparación no es autorización. Antes de código debe aprobarse la versión final del contrato de implementación, resolver dependencias temporales y emitir autorización explícita.

scientific_execution=false  
execution_authorized=false
