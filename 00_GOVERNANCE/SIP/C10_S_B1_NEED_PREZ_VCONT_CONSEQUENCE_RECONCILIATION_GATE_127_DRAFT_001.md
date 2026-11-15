# C10-S — Gate 127: reconciliación de Need_preZ, función B1 y consecuencia representable por V_cont

**ID:** C10-S-B1-NEED-PREZ-VCONT-CONSEQUENCE-127  
**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** B1_FUNCTIONAL_PURPOSE_ACCEPTED / NEED_PREZ_CLASS_DEFINED / PER_UE_TRUTH_OPEN / VCONT_DIMENSION_PROVISIONALLY_SELECTED / CONSEQUENCE_MAPPING_PARTIALLY_ADMISSIBLE / VALUE_VALUATION_RULE_CONDITIONAL / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** DEC-C10-051, DEC-C10-068, DEC-C10-095…103; B1 Valuation Case §§4–5, 12–17; B1 Pre-Z Adjudication/Consequence reconciliation; B2–B3 §§3, 5–7; Outcome/Value reconciliation §§2, 4–6; Gate 126; plan §§16.182–16.183, 16.218.

## 1. Dictamen ejecutivo

Gate 127 corrige una sobreextensión potencial de Gate 126: no es correcto describir la función/propósito basal de B1 como enteramente indefinido. La reconstrucción histórica ya contiene una especialización funcional aceptada como contrato de trabajo:

> B1 tiene el objetivo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo ENABLED y exponer el perfil PROFILE.

La operación de negocio posterior, el significado diferenciado de STANDARD/READ_ONLY y la semántica de las solicitudes pueden permanecer abstractos en el mundo sintético. No es necesario inventar una operación adicional para definir el referente funcional mínimo de C10-S.

La brecha que permanece es más precisa:
- la pertenencia/verdad Need_preZ por UE y su evidencia pre-Z no están materializadas;
- V_cont_truth mide cumplimiento temporal de la función de servicio estipulada, no procesamiento exitoso ni satisfacción de una solicitud concreta;
- la interpretación de V_cont como dimensión de Value requiere delimitar el alcance de la consecuencia que representa y la regla de valoración interna del DGP;
- no se ha demostrado que esa dimensión agote Value contextual, ni que su efecto se transfiera a una afirmación general de creación de valor.

**Dictamen:** el puente funcional mínimo es documentalmente admisible para el experimento sintético, sujeto a completar verdad basal por UE, parámetros/medición y una regla de interpretación valorativa explícita y simétrica en el DGP. No se requiere una autoridad humana o externa real: la autoridad puede ser una estipulación normativa versionada del mundo sintético, representativa de la perspectiva B1 ya aceptada. No se debe inventar ahora su contenido final ni confundirla con validación empírica de preferencias reales.

## 2. Reconstrucción histórica: qué está ya definido

### 2.1 Propósito y función basal

B1 Valuation Case contiene una secuencia de precisiones posteriores que deben leerse con precedencia, no quedarse en los estados OPEN históricos:

- §§4–7: estructura Need_preZ, envolvente de consecuencias y criterios de admisibilidad.
- §12: aceptación de la clase de propósito basal: mantener operativa una función de servicio dependiente de la configuración en destino.
- §13: reconstrucción del contrato lógico de procesamiento de solicitudes; no autoriza inferir semántica de negocio.
- §14: aceptación de la especialización funcional mínima: entrada de solicitud; admisión según ENABLED; exposición de PROFILE; salida inmediata de admisión/no admisión. No implica procesamiento posterior, respuesta, transformación o SF.
- §17: precedencia funcional integrada: el objetivo es mantener disponible el servicio capaz de admitir solicitudes conforme a ENABLED y exponer PROFILE; V_cont representa cumplimiento temporal de esa función, no Need_preZ ni el resultado de la oportunidad única.

Por tanto, las frases anteriores que reclamaban nombrar una operación de negocio adicional quedan limitadas por §§14 y 17. No se debe reabrir esa cuestión salvo nueva evidencia de contradicción en el contrato funcional.

### 2.2 Need_preZ

Need_preZ tiene una definición estructural pre-Z: existencia del objetivo basal de B1, independiente de Z, provisión, accesibilidad, Reach, oportunidad, petición, procesamiento, Outcome y ejecución. Estados 1/0/? permanecen distintos; falta de Request_event o evidencia no demuestra 0.

La clase de propósito está definida, pero no se asigna automáticamente Need_preZ=1 a todas las UE. La verdad por UE, regla de pertenencia y evidencia/adjudicación pre-Z siguen abiertas para el roster sintético. No se debe condicionar la población ITT a eventos post-Z.

### 2.3 V_cont y función medida

DEC-C10-099 selecciona V_cont como dimensión mínima provisional única para la extensión sintética B. DEC-C10-100…102 fijan la regla de truth temporal, ventana desde t0 y continuidad estricta por intervalos; parámetros y medición S3 permanecen abiertos. V_cont es la fracción temporal de cumplimiento de la función ENABLED/PROFILE en el horizonte, no el éxito de la oportunidad estandarizada.

Esto permite una lectura acotada: V_cont es la dimensión de continuidad/disponibilidad funcional que representa el cumplimiento temporal del propósito basal estipulado. No mide por sí sola la calidad del procesamiento posterior, el éxito de negocio, la satisfacción de una solicitud, los costes, el riesgo o todas las consecuencias de B1.

## 3. Crosswalk semántico sin equivalencias indebidas

| Objeto | Definición admisible en C10-S | Lo que no implica |
|---|---|---|
| Need_preZ | Propósito basal pre-Z de mantener disponible la función de admisión B1 | Demanda post-Z, petición o éxito técnico |
| A_B1(i,k) | Cumplimiento funcional ENABLED/PROFILE en intervalo k | Procesamiento o respuesta |
| V_cont_truth | Fracción temporal de intervalos conformes | Outcome terminal O-CONF o Value global |
| Consecuencia B1 focal | Disponibilidad temporal de la capacidad de admisión que B1 necesita mantener | Satisfacción de una solicitud particular o éxito de negocio |
| Value dimensión seleccionada | Valoración acotada de esa continuidad funcional desde la perspectiva B1 | Valor total, multi-dimensional o general de la migración |

La consecuencia focal puede definirse en el DGP como disponibilidad temporal de la capacidad de admisión. Esta definición no requiere que se genere una solicitud ni que el Analyzer observe un evento de petición. La oportunidad estandarizada sigue siendo un probe común del servicio, no la necesidad basal ni la consecuencia misma.

La equivalencia entre la consecuencia focal y V_cont solo es admisible si el DGP estipula expresamente que la dimensión seleccionada valora la continuidad de esa capacidad y conserva separados los procesos posteriores y las vías colaterales. No se debe derivar tal equivalencia únicamente del nombre V_cont ni de la verdad técnica.

## 4. Regla de valoración: alcance sintético y límite de inferencia

B2–B3 establece perspectiva primaria B1 y una autoridad/regla normativa explícita ex ante. En un experimento sintético, esto no requiere identificar un stakeholder real: la regla puede estar estipulada en truth_dgp como parte del mundo sintético, versionada y aplicada simétricamente por el Evaluator. Su carácter normativo debe quedar explícito y no presentarse como preferencia empírica real.

La regla aún debe precisar qué significa valorar la continuidad de la capacidad de admisión respecto del propósito basal. Gate 127 no fija una función numérica, pesos, umbrales, escala, compensación ni una relación monotónica por conveniencia. Tampoco afirma que la continuidad sea la única consecuencia relevante para B1 fuera del endpoint provisional seleccionado.

Tres niveles de afirmación deben mantenerse separados:

1. **Resultado causal sobre V_cont:** contribución de ΔT_acc* a continuidad funcional, si θ_A es identificable y V_cont está medido válidamente.
2. **Resultado causal sobre la dimensión Value seleccionada:** admisible solo si la regla DGP define V_cont como esa dimensión de valoración, con perspectiva B1 y mapping no circular ex ante.
3. **Afirmación de Value contextual más amplia:** no se sigue de los dos anteriores sin cobertura de otras consecuencias relevantes, justificación del alcance y límites explícitos.

No se debe definir Value como una transformación automática de ΔT_acc*, Reach, trayectoria, ejecución, Outcome o telemetría. La regla de valoración no puede depender del brazo, de la verdad contrafactual reservada ni del resultado observado por Analyzer.

## 5. Vías colaterales y pruebas de discriminación

El DGP debe preservar la posibilidad de que la disponibilidad funcional y la situación de B1 diverjan por:
- necesidad basal ausente o desconocida;
- vías alternativas que mantengan la capacidad de servicio;
- costes, demora, riesgo o esfuerzo de recuperación;
- fallos de procesamiento posteriores a la admisión;
- efectos contextuales que cambien la consecuencia sin cambiar V_cont.

No se convierten estas clases en nuevas dimensiones o variables sin justificación. Se reutilizan los contrastes adversariales ya presentes en B1 Valuation Case §6 y los contratos P179/P182/P183. En particular, deben permanecer posibles casos de O-CONF favorable con consecuencia no favorable, y de consecuencia preservada por ruta alternativa aunque cambie la accesibilidad focal.

Si el DGP no representa una vía colateral en un escenario, esa ausencia debe ser una propiedad explícita de ese escenario, no una suposición general del Analyzer.

## 6. Separación Generator / Sealer / Analyzer / Evaluator

- **Generator / truth_dgp:** contiene Need_preZ por UE, función B1, A_B1 por intervalo, V_cont_truth, consecuencias potenciales, regla normativa y mecanismos/alternativas.
- **Sealer / observed_evidence:** entrega solo señales y evidencia permitidas, con error, cobertura, missingness y provenance. No expone truth, etiquetas contrafactuales, regla secreta ni autoridad de valoración reservada.
- **Analyzer:** estima el estimando permitido sobre V_cont o se abstiene/bounds. No infiere Need_preZ ni Value completo a partir de Request_event, O-CONF o logs sin contrato de medición.
- **Evaluator:** después de sellar la salida del Analyzer, compara recuperación y errores contra truth, y adjudica si la interpretación de Value era admisible conforme a la regla DGP congelada.

El hecho de que Generator y Evaluator conozcan la regla y truth no demuestra que Analyzer pueda recuperar V_cont desde S3. La validez de medición y la identificación causal permanecen gates independientes.

## 7. Dependencias abiertas y criterio de cierre

| Dependencia | Estado tras Gate 127 |
|---|---|
| Propósito funcional B1 | ACCEPTED AT WORKING-CONTRACT LEVEL |
| Contrato ENABLED/PROFILE | DEFINED AT MINIMUM FUNCTIONAL LEVEL |
| Operación de negocio posterior / semántica de perfiles | OPEN, no bloquea la función mínima |
| Need_preZ conceptual pre-Z | DEFINED |
| Need_preZ truth/roster por UE | OPEN |
| Consecuencia focal: continuidad de capacidad de admisión | ADMISSIBLE CANDIDATE, mapping DGP not frozen |
| V_cont como dimensión mínima provisional | SELECTED BY DEC-C10-099 |
| Regla de valoración sintética ex ante | OPEN |
| Parámetros temporales, S3 y recuperación | OPEN |
| Vías colaterales/alternativas por escenario | OPEN per DGP |
| θ_A sobre V_cont | Estimando seleccionado; identificación OPEN |
| θ_A como efecto sobre Value acotado | CONDITIONAL on DGP valuation rule and measurement validity |
| Value contextual general | NOT ESTABLISHED |
| Design Freeze | NOT READY |

Para cerrar el puente no se requiere una nueva operación de negocio ni un beneficiario real. Se requiere una especificación DGP versionada que vincule el propósito B1 aceptado con la consecuencia focal, declare la regla normativa de valoración de V_cont y delimite las vías no representadas. La verdad por UE, soporte, medición S3, identificación de θ_A, sensibilidad y criterios cuantitativos permanecen dependencias independientes.

## 8. Dictamen final

Gate 127 resuelve la ambigüedad de alcance: B1 sí tiene un referente funcional mínimo definido y V_cont puede representar la continuidad temporal de la capacidad de admisión que ese referente requiere. No obstante, la interpretación como dimensión de Value depende de una regla normativa sintética explícita y no circular. La afirmación que puede llegar a sostenerse es acotada a esa dimensión, no una afirmación general de creación de valor.

Gate 126 se conserva, precisando que “consecuencia no operacionalizada” no equivale a “función B1 no definida”. No se reabren DEC-C10-099…103 ni se selecciona una dimensión nueva.

No se crean parámetros, escalas, pesos, umbrales, instrumentos, IDs de test, roster, fixtures o schemas. No se ejecutan validadores, tests, workflows, generación, simulaciones, calibraciones, estimaciones ni experimentos. No se modifican DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o `main`. PR #116 permanece Draft.

`scientific_execution=false`  
`execution_authorized=false`
