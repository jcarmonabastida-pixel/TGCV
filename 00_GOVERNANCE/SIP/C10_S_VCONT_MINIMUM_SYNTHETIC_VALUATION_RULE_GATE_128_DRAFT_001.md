# C10-S — Gate 128: regla mínima de valoración sintética para V_cont

**ID:** C10-S-VCONT-MINIMUM-SYNTHETIC-VALUATION-RULE-128  
**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** DEC-C10-099_102_PRESERVED / VCONT_B1_MIN_EXPLICITLY_ACCEPTED_IN_CHAT / SYNTHETIC_ORDINAL_RULE_ACCEPTED_FOR_BOUNDED_DIMENSION / VALUE_GENERAL_OUT_OF_SCOPE / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** DEC-C10-068, DEC-C10-095…103; B1 Valuation Case §§12–17; B2–B3 §§3–7; Outcome/Value reconciliation §§2, 4; P179/P182/P183; Gates 126–127. Aceptación explícita de VCONT-B1-MIN: 2026-11-16.

## 1. Dictamen ejecutivo

DEC-C10-099 ya selecciona provisionalmente `V_cont` como única dimensión mínima de Value para la extensión sintética B y declara `V=(V_cont)`, sin índice compuesto, pesos ni compensación. DEC-C10-100 fija su truth como fracción temporal de cumplimiento funcional por intervalos iguales y conserva bounds cuando existen intervalos desconocidos. No corresponde volver a seleccionar la dimensión ni inventar una segunda transformación numérica.

Sin embargo, DEC-C10-099 exige que el criterio normativo del DGP, las consecuencias potenciales y el mecanismo de valoración estén estipulados ex ante. Esa condición no está satisfecha por el mero hecho de que el Generator conozca `V_cont_truth`, ni por la fórmula temporal de DEC-C10-100. El DGP necesita declarar qué significa valorar la continuidad desde la perspectiva B1 y cuál es el alcance exacto de esa valoración.

**Dictamen:** la regla puede ser una estipulación normativa interna del mundo sintético. No requiere una autoridad humana o externa real ni una función de utilidad cardinal. Pero su contenido no puede deducirse de ENABLED/PROFILE ni ser introducido unilateralmente como decisión aceptada. Se formula una propuesta mínima para aprobación explícita; hasta entonces, la interpretación de `V_cont` como dimensión de Value permanece condicional.

## 2. Decisiones y límites ya fijados

### 2.1 Lo que no se reabre

- DEC-C10-099: `V_cont` es la única dimensión mínima provisional de Value para B; vector unitario, sin índice, pesos o compensación.
- DEC-C10-100: `V_cont_truth(i)=(1/K)Σ A_B1(i,k)`, con estados 1/0/? y bounds ante desconocidos.
- DEC-C10-101/102: ventana post-Z desde t0 y continuidad estricta por intervalo; los parámetros temporales siguen abiertos.
- DEC-C10-103: `θ_A(q_X*,r_common;V_cont)` es el estimando focal seleccionado; no está identificado por la selección del estimando.
- P179: preservar vectorialidad/trade-offs durante identificación; la especialización provisional de B como vector unitario no autoriza agregar dimensiones ni un escalar compuesto.

### 2.2 Lo que no se puede inferir

La función técnica B1 (admitir conforme a ENABLED y exponer PROFILE) especifica el comportamiento del servicio. No determina por sí misma:
- que toda UE tenga `Need_preZ=1`;
- que la continuidad sea siempre beneficiosa en cualquier contexto;
- que continuidad sea equivalente a satisfacción de una solicitud o éxito de negocio;
- que no existan costes, riesgos, demoras, rutas alternativas o consecuencias colaterales;
- que la dimensión seleccionada agote Value contextual general.

DEC-C10-095 fija una estipulación basal explícita, versionada y reservada por UE para la truth de `Need_preZ`; DEC-C10-096 fija el censo de validación de la población aplicable. Esas decisiones no definen una regla de valoración de V_cont ni deben confundirse con ella.

## 3. Regla normativa mínima VCONT-B1-MIN — aceptada para la dimensión acotada

Se registra la aceptación explícita del usuario, recibida el 2026-11-16 en la conversación de trabajo, de la siguiente estipulación para el endpoint sintético focal, limitada estrictamente a la única dimensión seleccionada:

> **Regla propuesta VCONT-B1-MIN:** En el mundo sintético B, desde la perspectiva normativa de B1 y respecto del propósito basal versionado, la consecuencia focal valorada es la continuidad temporal de la capacidad efectiva del servicio para admitir solicitudes conforme a ENABLED y exponer PROFILE. Para esta dimensión y solo para esta dimensión, un nivel mayor de continuidad no se valora peor que uno menor; niveles iguales representan la misma valoración en la dimensión. `V_cont_truth` es la representación completa de esa dimensión. No se añade transformación cardinal, peso, umbral, compensación ni agregación con otras consecuencias.

Esta propuesta contiene únicamente:
1. **Referente:** propósito basal B1 ya aceptado.
2. **Consecuencia focal:** continuidad temporal de la capacidad funcional de admisión.
3. **Perspectiva:** B1, conforme a B2–B3.
4. **Criterio ordinal mínimo:** preferencia débil por mayor continuidad dentro de esta dimensión; igualdad de V_cont implica igualdad de valoración en esta dimensión.
5. **Medida:** la truth temporal de DEC-C10-100, sujeta a medición válida.
6. **Alcance:** una dimensión sintética acotada; no Value global ni valoración completa de todas las consecuencias.

La regla no afirma que el servicio deba admitir cuando ENABLED=false, ni que el procesamiento posterior tenga éxito. La conformidad de A_B1 sigue anclada al contrato funcional versionado.

## 4. Prueba de no circularidad y límites de la propuesta

La regla propuesta no define Value como función de `ΔT_acc*`, Reach, trayectoria, instalación, asignación D2, selección, ejecución, O-CONF o señales S3. Esos objetos no aparecen en el criterio normativo. El mecanismo causal puede hacer que accesibilidad afecte a continuidad, pero no se impone esa relación por definición.

La regla tampoco demuestra que V_cont sea suficiente para toda consecuencia B1. Si el DGP pretende representar costes, riesgo, demora, daño, preferencias contextuales o rutas alternativas como parte de la valoración focal, entonces V_cont por sí sola no agota esa valoración. En tal caso:
- esos mecanismos pueden permanecer como vías causales colaterales y ser analizados separadamente;
- pero no pueden incorporarse tácitamente a la dimensión unitaria V_cont;
- si cambian la valoración manteniendo V_cont constante, la interpretación de V_cont como dimensión completa de Value contextual resulta insuficiente para ese alcance.

Por ello, la propuesta es admisible solo si el alcance de la afirmación se limita expresamente a la dimensión de continuidad funcional seleccionada. No permite afirmar “Value total”, “beneficio neto” o “creación de valor general”.

## 5. Qué queda fuera y cómo se adjudica

- `Need_preZ` truth se genera por la estipulación basal explícita DEC-C10-095; no se deriva de la continuidad observada ni de resultados post-Z.
- `A_B1(i,k)` y `V_cont_truth` permanecen en truth_dgp reservada.
- Sealer produce observaciones S3 permitidas, con error, cobertura, missingness y provenance.
- Analyzer no recibe truth, regla secreta, potenciales ni parámetros reservados; estima, presenta bounds o se abstiene.
- Evaluator aplica la regla normativa ya fijada y compara la salida sellada con truth después del sellado.
- La regla de valoración no resuelve validez de medida, identificación de θ_A, soporte, interferencia, sensibilidad, potencia ni recuperación de bounds.

No se crean nuevos indicadores, escalas, pesos, umbrales, IDs de test, parámetros, roster, fixtures o schemas.

## 6. Alternativas y condición de decisión explícita

| Alternativa | Consecuencia |
|---|---|
| A. Aceptar VCONT-B1-MIN | Cierra el criterio ordinal mínimo solo para la dimensión de continuidad funcional; Value general sigue fuera de alcance |
| B. Rechazar la preferencia débil por mayor continuidad | V_cont permanece como resultado técnico/constructo seleccionado, pero su interpretación valorativa queda sin regla; θ_A no sustenta Value |
| C. Exigir que el endpoint represente consecuencias más amplias | El alcance unitario V_cont es insuficiente; habría que reabrir formalmente la selección/alcance de Value, sin añadir dimensiones por conveniencia |

La aceptación conversacional resuelve la condición de aprobación de trabajo de Gate 128. No constituye por sí sola un nuevo Decision Record formal ni modifica DEC-C10-099; la regla queda aceptada como estipulación normativa del DGP para la dimensión unitaria acotada.

## 7. Dictamen y autorización

**Resultado:** VCONT_B1_MIN_ACCEPTED_FOR_BOUNDED_SYNTHETIC_VALUE_DIMENSION / VALUE_INTERPRETATION_CLOSED_ONLY_AT_THIS_SCOPE / VALUE_CONTEXTUAL_GENERAL_NOT_ESTABLISHED.

La aceptación confirma la opción A: conserva DEC-C10-099, evita un índice o función cardinal inventada y limita la afirmación a la dimensión realmente seleccionada. El Generator deberá codificar la regla como estipulación normativa ex ante, versionada y separada de los mecanismos de accesibilidad; el Analyzer no recibirá truth ni parámetros reservados. El Evaluator podrá usarla en la adjudicación post-sellado.

No Design Freeze, implementación ni ejecución. No se modifica main, DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS o TGCV Core. No se ejecutan validadores, tests, generación, simulaciones, calibraciones o estimaciones.

`scientific_execution=false`  
`execution_authorized=false`
