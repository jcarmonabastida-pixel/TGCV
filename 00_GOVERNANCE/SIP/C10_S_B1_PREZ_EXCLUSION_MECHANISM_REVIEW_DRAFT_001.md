# C10-S — Revisión de alternativas para estipular la exclusión focal de Need_preZ

**ID:** C10-S-B1-PREZ-EXCLUSION-MECHANISM-REVIEW-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_REVIEW / RECOMMENDATION / NOT_USER_APPROVED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Pregunta

Determinar si la estipulación basal reservada de Need_preZ=0 debe admitir:
- una exclusión focal explícita del objetivo definido para B1; y/o
- una enumeración exhaustiva del universo de objetivos B1–servicio que no contenga el objetivo focal.

La revisión reutiliza el contrato funcional y las reglas ya definidos. No redefine Need_preZ ni la adjudicación observada.

## 2. Base documental reconstruida

1. `C10_S_B1_REQUESTING_ENTITY_CANDIDATE_SPEC_DRAFT_001.md`, §§1, 3, 10–11 y decisiones B1: Need_preZ es necesidad/objetivo basal de la entidad solicitante; existe antes de Z; no se define por solicitud, uso, admisión, consumo o resultado. La entidad B1, la UE y el servicio son referentes distintos.
2. `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`, §§3–4: la definición funcional focal ya está establecida; truth=0 requiere afirmación positiva de que B1 no tiene ese objetivo en el universo cerrado del DGP; observed=0 requiere evidencia afirmativa y cobertura documental/declarativa cerrada y demostrada.
3. `C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md`, §§3, 5–8: truth reservada y evidencia observacional separadas; ausencia de registro o solicitud no es cero; una fuente Need-bearing y un alcance de cobertura son requisitos para adjudicación.
4. `C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md`, §§2–7: los documentos actuales son artefactos de diseño, no fuentes individuales; no hay roster ni fuentes por unidad; cobertura material NONE y adjudicación bloqueada.
5. `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md`: el usuario aceptó el principio de estipulación explícita por B1, pero la representación y los criterios de exclusión no están aprobados.

## 3. Distinción que gobierna la elección

Hay dos problemas distintos:

**Truth del DGP:** el generador debe estipular el estado semántico del objetivo basal de B1, en el espacio reservado. No necesita fingir que ha descubierto evidencia externa. La estipulación es la definición de verdad del caso sintético.

**Observed=0:** el adjudicador no conoce esa estipulación. Solo puede asignar cero si recibe evidencia observable afirmativa, pre-Z, admisible, vinculada a B1/UE/servicio y con autoridad, versión, alcance y cobertura suficientes. La etiqueta interna, el campo reservado o el hecho de que el generador haya seleccionado truth=0 no son evidencia para E1/E2.

Por tanto, la simplicidad del mecanismo de truth no puede reducir los requisitos probatorios del modelo de observación.

## 4. Comparación de mecanismos

| Criterio | Exclusión focal explícita | Enumeración exhaustiva B1–servicio |
|---|---|---|
| Determina directamente el constructo Need_preZ | Sí | Sí, mediante ausencia dentro de un conjunto declarado completo |
| Requiere universo de todos los objetivos | No; solo delimitar el objetivo focal | Sí; definir y cerrar el universo enumerado |
| Evita inferir desde silencio | Sí, si la exclusión es una afirmación semántica explícita | Sí, si completitud y enumeración son afirmaciones explícitas |
| Complejidad del generador | Menor | Mayor |
| Nuevos conceptos necesarios | Exclusión focal, identidad, versión, tiempo | Además, semántica de catálogo, completitud y cierre de enumeración |
| Riesgo de alcance accidentalmente incompleto | Bajo si la afirmación focal está bien delimitada | Mayor si el catálogo se declara exhaustivo sin serlo |
| Necesidad para evaluar clasificación 1/0 | Suficiente para truth=0 | No añade soporte lógico indispensable |
| Necesidad para observed=0 | No basta por sí sola; requiere una fuente negativa observable independiente | Tampoco basta por sí sola; requiere una fuente observable y cobertura |

## 5. Recomendación

**Adoptar la exclusión focal explícita como única vía mínima necesaria para estipular truth=0 en el DGP. No exigir enumeración exhaustiva.**

La estipulación afirmará, en el espacio reservado, que el objetivo funcional exacto de Need_preZ no pertenece a los objetivos basales de la B1 identificada respecto de su vínculo versionado con la instancia lógica de servicio, en t−1.

La relación con el servicio funciona como delimitación referencial del objetivo focal y control de identidad/versionado. No convierte el servicio en sujeto de la necesidad ni confunde B1, UE e instancia de servicio.

La enumeración exhaustiva se deja fuera del núcleo mínimo. Solo debería reabrirse si un futuro mecanismo de fuente observable requiere una declaración de completitud como forma probatoria y se demuestra que una exclusión focal explícita no puede representarse de manera admisible. Incluso entonces, sería una alternativa de evidencia/representación, no una obligación de enumerar todos los objetivos de B1 en la truth interna.

## 6. Requisitos mínimos de una exclusión focal válida

Una futura estipulación reservada solo será interpretable si identifica:
1. B1 y UE inequívocas, con vínculo versionado según el roster que se apruebe;
2. la instancia lógica de servicio vinculada, su contrato y versión, solo como ancla referencial;
3. la definición funcional y versión exactas del objetivo focal;
4. el tiempo basal t−1 y su precedencia respecto de Z;
5. una afirmación explícita de no pertenencia del objetivo focal;
6. la regla/versión de generación y provenance reservada.

No se aceptan como exclusión: campo ausente, lista vacía, omisión, falta de fuente, falta de solicitud, no instalación, no habilitación, no disponibilidad, no accesibilidad, falta de déficit ni error técnico. Los defectos de identidad/versionado/integridad bloquean la unidad; no se recodifican como cero o ?.

## 7. Requisitos separados para evidencia observada negativa

La futura fuente que permita observed=0 debe expresar afirmativamente la exclusión focal o un hecho documental equivalente cuyo alcance sea suficiente. Debe ser una fuente distinta de la truth reservada, con:
- emisor/autoridad y rol admisibles;
- fecha y vigencia pre-Z;
- identidad B1/UE y binding de servicio no ambiguos;
- definición funcional/versiones aplicables;
- alcance explícito de la afirmación;
- integridad, provenance y lineage;
- cobertura de las fuentes relevantes y tratamiento de contradicciones.

La cobertura no puede deducirse del mero hecho de que el DGP conozca la truth. Si no se dispone de una fuente observable admisible o no se demuestra su alcance, observed=? aunque truth=0.

## 8. Límites y gates

Esta recomendación no:
- aprueba por sí misma el contrato de exclusión;
- fija prevalencia, proporciones, estratos, número de unidades, parámetros o semilla;
- especifica cómo se generan truth=1 y truth=? más allá de las reglas semánticas ya propuestas;
- define tipos concretos de fuentes, autoridad, errores o missingness;
- resuelve permisos técnicos ni almacenamiento físico;
- crea roster, truth, fuentes, registros, fixtures o código.

Siguientes gates, en orden:
1. aceptar/rechazar la recomendación de exclusión focal como única vía mínima de truth=0;
2. reconciliar el contrato de estipulación con el paquete analítico y el DGP temporal/roles;
3. definir la composición de estados 1/0/? y su soporte sin prevalencias arbitrarias;
4. diseñar el modelo de observación y sus fuentes de forma independiente;
5. verificar integridad, cegamiento y separación de roles antes de cualquier autorización de materialización.

## 9. Dictamen

**EXPLICIT FOCAL EXCLUSION RECOMMENDED AS SUFFICIENT MINIMUM TRUTH MECHANISM / EXHAUSTIVE ENUMERATION NOT REQUIRED / OBSERVED NEGATIVE STILL REQUIRES INDEPENDENT AFFIRMATIVE EVIDENCE AND DEMONSTRATED COVERAGE.**

No se modifican main, RMA, Evidence→Claim Matrix, STATUS, decisiones aceptadas, población, estimandos ni DGP ejecutable. No se declara cerrado el contrato de exclusión. No se materializan unidades, truth, fuentes o cobertura. No se ejecutan validadores, DGP, simulaciones ni replay.

`scientific_execution=false`; `execution_authorized=false`.
