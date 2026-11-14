# C10-S — Informe de recuperación histórica y trazabilidad
**Registro de coordinación documental — borrador 001**

**Estado:** DRAFT / RECUPERACIÓN DOCUMENTAL — NO APROBADO  
**Repositorio canónico:** `jcarmonabastida-pixel/TGCV`  
**Rama de trabajo:** `research/c10-s-consolidation-draft`  
**PR de continuidad:** #116 (Draft)  
**Fecha de revisión:** 2026-11-04

## 1. Propósito y límites

Este informe registra la reconstrucción documental disponible de C10-D1 y C10-S, identifica qué material está efectivamente persistido y qué partes del desarrollo conversacional no se han podido recuperar en forma íntegra.

No es una transcripción del historial de ChatGPT. No convierte resúmenes en texto original, no completa lagunas mediante inferencias y no introduce decisiones científicas nuevas. Su finalidad es cumplir la regla de reconstrucción histórica previa a cualquier nueva operación, conservar la trazabilidad y evitar repetir o sustituir silenciosamente trabajo anterior.

No se ha ejecutado código, simulación, estimación, procesamiento de datos ni experimento. No se modifica el Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres científicos.

## 2. Fuentes canónicas inspeccionadas

| Artefacto | Estado / identidad verificada | Alcance |
|---|---|---|
| `README.md` en `main` | SHA `962ab503bf835b6e1a4f45c80a396f3eb2fe4c6c` | Repositorio canónico y regla de freeze/inmutabilidad |
| `00_GOVERNANCE/README.md` | SHA `f4871301c70e98a0b1b91d2253d0e937768c75d8` | Operativa, fuente de verdad y reconstrucción histórica obligatoria |
| `00_GOVERNANCE/CHATGPT_BOOTSTRAP.md` | SHA `7acf632f6296d88eaaafb8283faad571f608b385` | Continuidad de sesión y prioridad C10 |
| `HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md` | SHA `c01b0cc3b2a7d6bcf56893a0665f09fd2c8ddba4` | Reglas de recuperación, reutilización y no sustitución semántica |
| `GOVERNANCE_OPERATING_PRINCIPLES_v0.1.md` | SHA `acd83326a0f9ce6509c7e87e4bf49c94169b5c87` | Mantenimiento documental sin crear estados científicos artificiales |
| `CANONICAL_STATE.json` en `main` | SHA `054edafe068cb38d5e6708aa650840d80524b2df` | RMA v3.37, Matrix v1.47 y punteros vigentes |
| `STATUS.md` en `main` | Estado declara RMA v3.37 y Matrix v1.47 | C10 Value linkage permanece abierto; C09 es evidencia causal acotada |
| `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` | v1.47 | C10 no recibe atribución causal de Value por la evidencia actual |
| `00_GOVERNANCE/rma/TGCV_RMA_current.md` | Puntero a v3.37 | Estado RMA |
| `TECHNICAL_EXECUTION_WORKFLOW_v0.1.md` | SHA `66810b5aad08be4667480b13382c019577f93790` | Secuencia de ejecución gobernada; no aplicable como autorización de ejecución C10 |

## 3. Cadena documental C10 recuperada

### 3.1 C10-D1 — protocolo causal

- PR #115: [C10-D1 causal accessibility-to-value protocol](https://github.com/jcarmonabastida-pixel/TGCV/pull/115).
- Estado: abierto, Draft, no aprobado ni preregistrado.
- Rama: `research/c10-d1-protocol-draft`.
- Base: `main`, SHA registrado por PR: `e0bae45aa9e1ea79eb739f5856672ec59657690a`.
- Head: `4b19038cb89c09b755d4e6c895e463fa2823df15`.
- Archivo: `00_GOVERNANCE/SIP/C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`.
- Blob SHA: `bf25f6ec8965166e5fa52ff18e6d07613bad0eb3`; 193.672 caracteres; 38 secciones principales.
- PR registra 23 commits y un archivo modificado. No hay comentarios ni revisiones registradas.

El protocolo separa el efecto total de la intervención (TE), la contribución de una política específica de accesibilidad bajo un régimen común, los efectos conjuntos de condiciones y accesibilidad, y el residual solo cuando la descomposición es compatible. Exige medición independiente de T_acc, Reach, Trayectoria, Outcome y Value; trata confusión post-tratamiento, soporte/positividad, interferencia, temporalidad, error de medición, falsación, equivalencia, heterogeneidad y límites de identificación.

El documento incorpora addenda hasta las secciones 38, incluidas las puertas G1–G7 de selección de casos y una exploración documental inicial de dominios. Mantiene expresamente que un ITT de una intervención no demuestra por sí solo la contribución específica de accesibilidad.

### 3.2 C10-S — experimento sintético

- PR #116: [C10-S consolidated synthetic experiment specification](https://github.com/jcarmonabastida-pixel/TGCV/pull/116).
- Estado: abierto, Draft, no aprobado, implementado ni ejecutado.
- Rama: `research/c10-s-consolidation-draft`.
- Base: rama `research/c10-d1-protocol-draft`, SHA `4b19038cb89c09b755d4e6c895e463fa2823df15`.
- Head: `c18a91c25bbe50c537362f395d2a85bf0788fd05`.
- PR incluye cuatro archivos: documento consolidado y tres auditorías/propuestas documentales.
- No hay comentarios ni revisiones registradas.

Documento principal:
- Ruta: `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`.
- Blob SHA: `d75b4ffc2be057ae7ac61478e3d27a0c53c1fc1d`.
- Longitud: 355.336 caracteres; 415 encabezados Markdown; 51 secciones principales.
- La sección 51 corresponde expresamente a la sección conversacional 164.

La consolidación cubre arquitectura causal y transformacional, generador, Value, escenarios, contratos de datos y pruebas EQ/EX/TG/SR/CV/V; posteriormente incorpora la secuencia conversacional 130–164: auditorías XAUD/XSYNC, S4-O/S4-R, DGP, estimandos, IV/LATE, exclusión, monotonicidad, cumplimiento, versiones, inferencia débil, medición de accesibilidad, datos ausentes, unidades/interferencia, elegibilidad, accesibilidad basal, rutas alternativas, poblaciones P*_τ2/P*_F y matriz S4-R.

### 3.3 Auditorías y propuestas incluidas en PR #116

1. `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md`, SHA `d3ffa9ed0670764c339dc390423f435e6da0fc9b`: identifica dos bloqueos estructurales, AUD-C10S-001 (definición de A respecto a ΔT_acc) y AUD-C10S-002 (falta de contrato generativo integrado); recomienda revisión mayor y no implementar todavía.
2. `C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md`, SHA `5a3a2fa061fe146d9df9d4cdfbb803c5ee274d65`: propuesta de accesibilidad focal A_f, T_acc completo y ΔT_acc; separa asignación, autorización, accesibilidad verdadera/observada, aplicabilidad y ejecución. Sigue pendiente de revisión/armonización.
3. `C10_S_AUD001_AUD002_CROSS_AUDIT_DRAFT_001.md`, SHA `ce53c902fb39820e976eed5cb2a87e5eacace31c`: identifica XAUD-001 a XAUD-006 y XAUD-007 editorial; concluye que AUD-001/002 siguen abiertos y que la intervención física y la atribución específica a accesibilidad no están cerradas.

La existencia de propuestas de resolución no equivale a aceptación de los hallazgos ni a cierre de auditoría.

## 4. Estado exacto de S4-R al último registro canónico

La sección 51 (conversacional 164) propone, sin congelarlo:
- ITT de la política aleatorizada en P*_τ2 como objetivo primario de diseño;
- IV/LATE focal como análisis secundario, solo si se sostienen relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia y medición válida;
- P*_F como subpoblación funcionalmente exclusiva y análisis secundario/heterogeneidad, no filtro automático de la población primaria;
- escenarios S4R-A (sin alternativa basal), S4R-B (alternativa basal no afectada), S4R-C (la provisión modifica alternativas y compromete exclusión focal) y S4R-D (no cumplimiento/fallo de provisión).

Pendientes explícitos: política B y versiones; contradicción p0=.20 frente a C_dep,0=0; estatuto de S4R-C; formalización con C10-D1; F*, q_X*, horizonte y Value; medición de alternativas y efectos colaterales; reglas de primera etapa nula/débil; revisión independiente XSYNC. No se congela S4-R.

## 5. Recuperación del desarrollo conversacional posterior a la sección 164

La búsqueda realizada no ha localizado una fuente canónica íntegra para las secciones conversacionales 165–183. La situación debe registrarse por niveles de fidelidad:

| Secciones | Recuperación disponible | Tratamiento permitido |
|---|---|---|
| 165–173 | Resúmenes temáticos parciales; no texto íntegro | Inventariar temas y decisiones solo si pueden atribuirse; no reconstruir prosa original |
| 174–176 | Resúmenes de decisiones, fórmulas y protocolos; no texto íntegro | Mantener como referencias pendientes de cotejo |
| 177 | Resumen de arquitectura de estimación que separa ITT, LATE, Outcome, Value y mecanismos | Puede registrarse como resumen secundario, no como especificación completa |
| 178–181 | Información insuficiente para reconstrucción fiel | No asignar contenido ni numeración temática por inferencia |
| 182 | Resumen disponible de «Validez de constructo y sensibilidad de las medidas»: separación A/O/V, validez, fiabilidad, error de medición, invariancia, sensibilidad y pruebas P182-01 a P182-12 | El resumen no sustituye el texto íntegro ni permite certificar las fichas de prueba |
| 183 | Resumen disponible de «Datos ausentes, censura y mediciones incompletas de A, O y V»: MCAR/MAR/MNAR, censura, selección postasignación, ITT/mediación/LATE, cotas y pruebas P183-01 a P183-13 | El resumen no sustituye el texto íntegro ni permite certificar las fichas de prueba |

**Conclusión de recuperación:** las secciones 182–183 están descritas en el contexto de continuidad, pero su texto literal y sus fichas completas no se han recuperado desde un artefacto canónico. Las secciones 165–181 presentan una brecha mayor. No se debe afirmar que 165–183 estén persistidas en GitHub ni reescribirlas como si se hubieran recuperado.

## 6. Incidencias de trazabilidad y consistencia documental

1. **Metadato de cobertura corregido.** El encabezado original declaraba cobertura hasta la sección conversacional 129, aunque el contenido, la sección 51 y el PR #116 acreditaban cobertura hasta 164. Se corrigió únicamente ese metadato en el borrador 004 mediante commit `12dfcb1d29eabdba3e392f4c2a0137cae8acacb7`; no se modificó contenido científico. La versión anterior queda trazable por su blob SHA `d75b4ffc2be057ae7ac61478e3d27a0c53c1fc1d`.
2. **Dependencia entre PRs.** PR #116 se basa en la rama de PR #115, no directamente en `main`. Debe mantenerse visible esa dependencia y revisarse la cadena de integración antes de cualquier promoción.
3. **No existe revisión independiente registrada en PR #115/#116.** Ambos siguen Draft y no tienen comentarios/revisiones.
4. **No hay evidencia de implementación o ejecución de C10-S.** Los contratos, escenarios, valores numéricos y tamaños muestrales descritos en el borrador son propuestas/ilustraciones, no resultados ni parámetros validados.
5. **No se ha verificado el cierre de XSYNC.** El propio PR #116 mantiene XSYNC-138-01 abierto y los hallazgos posteriores sujetos a revisión.
6. **STATUS conserva una fecha declarada anterior a algunos registros que referencia.** Sus versiones RMA v3.37 y Matrix v1.47 coinciden con CANONICAL_STATE, pero la fecha visible del documento debe tratarse como metadato a revisar, no como prueba de actualización temporal completa.

## 7. Decisiones de recuperación y no-regresión

- Reutilizar PR #115 como protocolo causal rector de C10-D1; no recrearlo.
- Reutilizar PR #116 como consolidación sintética histórica hasta la sección conversacional 164; no reemplazarlo.
- Mantener las auditorías y propuestas como abiertas hasta revisión explícita.
- No equiparar ITT con efecto de accesibilidad ni Wald/LATE con ATE.
- No reducir ΔT_acc a A_f*: preservar la estructura completa de transformaciones, relaciones y configuraciones.
- No tratar ausencia de evidencia como inaccesibilidad ni ausencia de ejecución como prueba de inaccesibilidad.
- Mantener Outcome y Value separados, con regla Value independiente.
- No reabrir selección de caso ni iniciar búsqueda de datasets como sustituto de cerrar la estrategia de atribución causal.
- No implementar, simular, preregistrar ni ejecutar sin autorización expresa.
- No actualizar STATUS, RMA ni Evidence→Claim Matrix: esta recuperación no cambia estado científico ni claim.

## 8. Próxima secuencia documental mínima

1. Recuperar cualquier fuente íntegra disponible de 165–183 (exportación de chat, notas o artefacto adjunto) y cotejarla contra la matriz de cobertura de este informe.
2. Reconciliar 165–181 con el protocolo C10-D1 y la consolidación C10-S sin crear decisiones nuevas por inferencia.
3. Incorporar 182–183 solo cuando se disponga de texto y pruebas completos; mientras tanto mantenerlos como resúmenes no verificados.
4. Corregir el metadato de cobertura de documento 004 y registrar la corrección sin reescribir el contenido científico.
5. Ejecutar una auditoría cruzada final C10-D1 ↔ C10-S que resuelva precedencia, estimandos, variables, población, medición y criterios de decisión.
6. Solo después determinar si el diseño está suficientemente cerrado para congelación documental. La congelación no autoriza implementación ni simulación.

## 9. Dictamen

**RECUPERACIÓN PARCIAL VERIFICADA / CONTINUIDAD DOCUMENTAL ABIERTA.**

Está recuperada y verificada la cadena canónica C10-D1 (PR #115) → C10-S (PR #116) hasta la sección conversacional 164, junto con sus auditorías y límites. No se ha recuperado íntegramente el material conversacional 165–183. La documentación disponible permite continuar la reconciliación sin reiniciar el trabajo, pero no permite certificar que el protocolo completo posterior a la sección 164 esté persistido ni congelar el diseño.

Este informe es un registro documental de recuperación. No constituye aceptación científica, auditoría independiente, freeze, preregistro, implementación ni ejecución.


## 10. Ampliación de la recuperación y matriz maestra de cierre (2026-11-04)

Se ha realizado una nueva revisión de PR #115 y PR #116, de los cinco archivos incluidos en PR #116, del historial de comentarios, revisiones e hilos del PR #116 (sin registros), y búsquedas en el repositorio para referencias de las pruebas P182/P183 y material C10-S posterior a la sección 164. No se ha localizado una fuente primaria íntegra adicional para 165–183 ni el texto íntegro de XSYNC-138-01…10.

Se ha creado el artefacto de control:

- `00_GOVERNANCE/SIP/C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`
- Commit de creación: `15e5dfe577909705eec067bb8b182def64e1a96c`
- Rama: `research/c10-s-consolidation-draft`
- PR: #116.

La matriz reúne:
1. inventario de fuentes y cobertura;
2. estado de recuperación 165–183;
3. reconciliación C10-D1 ↔ C10-S;
4. registro AUD-001…012 y XAUD-001…007;
5. decisiones y contradicciones abiertas de S4-R;
6. inventario de contratos EQ/EX/TG/SR/CV/V, INT, S4R y P182/P183;
7. límites de recuperación XSYNC;
8. gates G0–G7 y secuencia de cierre.

La matriz no transforma resúmenes en fuentes originales ni cierra hallazgos por inferencia. El estado global permanece **CIERRE DOCUMENTAL NO ALCANZADO**. En particular, la contradicción entre p0=.20 y C_dep,0=0, la coherencia q/g, la distinción ITT frente a efecto específico de accesibilidad, los contratos de pruebas y la revisión independiente siguen abiertos.

La cabecera histórica de la sección 3.2 conserva el corte inicial de la recuperación. Tras las nuevas incorporaciones, PR #116 contiene seis archivos modificados; su SHA head y número de commits son datos dinámicos que deben consultarse directamente en la ficha del PR, no duplicarse aquí.\n\nLa nueva búsqueda no permite afirmar que las fuentes 165–183 no existan fuera de GitHub; únicamente que no se han recuperado desde las fuentes consultadas. Para cerrar la recuperación literal se necesita la exportación original de las conversaciones o los artefactos fuente que contengan esas secciones y los hallazgos XSYNC.

No se ha ejecutado código, simulación ni experimento. No se ha autorizado implementación, selección de caso real, adquisición/procesamiento de datos o preregistro. No se han modificado Core, RMA, Evidence→Claim Matrix, STATUS ni claims.


## 11. Reconciliación causal C10-D1 ↔ S4-R y registro de decisiones (2026-11-04)

La lectura íntegra de C10-D1 §§5, 17, 24–26 y 30–34 y de C10-S §§43 y 51 confirma que el ITT de la asignación a provisión no sustituye al estimando científico de accesibilidad. Se han añadido dos documentos a PR #116:

- `00_GOVERNANCE/SIP/C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`: propone conservar `θ_A(q)` como pregunta científica C10-D1, `ITT_Z` como objetivo primario del diseño S4-R y `LATE_f` como efecto local focal condicionado a IV. Explicita que S4-R no identifica por sí solo `θ_A(q)` poblacional ni el efecto de todo `ΔT_acc`. Propone separar un DGP limpio (`p0=0`) de otro adversarial con contaminación explícita (`p0>0`) y precisar la elegibilidad basal.
- `00_GOVERNANCE/SIP/C10_S_DECISION_LOG_DRAFT_001.md`: registra DEC-C10-001…010, decisiones abiertas y alternativas no admisibles, diferenciando propuestas de decisiones aceptadas.

La matriz maestra se actualizó para reflejar esta reconciliación sin marcar como cerrados AUD/XAUD/S4-R. PR #116 se verificó con ocho archivos modificados y permanecía abierto en estado Draft. El número de commits y SHA head son dinámicos y se consultan en el propio PR.

**Dictamen de esta etapa:** la jerarquía de estimandos queda reconciliada como propuesta documental coherente, no aprobada. La contradicción `p0=.20` / `C_dep,base=0` queda convertida en dos alternativas de DGP explícitas, pendientes de decisión. No se ha ejecutado simulación ni experimento.


## 12. Corrección de la recuperación XSYNC y búsqueda ampliada (2026-11-04)

Se corrige expresamente la afirmación de la sección 10 según la cual no se había recuperado el texto íntegro XSYNC. La búsqueda de contexto dentro del documento canónico C10-S consolidado identificó el texto de los diez hallazgos en §25.2, así como las respuestas/estados en §§25.3–25.4, 26.6–26.10, 27.6–27.8 y 28.8–28.9.

Se ha creado `C10_S_XSYNC_138_CLOSURE_TRACKER_DRAFT_001.md`, que registra los diez hallazgos, severidad, respuesta ya incorporada, pendiente de cierre y criterio de aceptación. Dictamen corregido: **texto XSYNC-138-01…10 recuperado en GitHub; cierre formal no alcanzado; pruebas no ejecutadas**.

También se revisó el conjunto de ramas disponible en el repositorio. Las ramas de investigación C10 visibles son `research/c10-d1-protocol-draft` y `research/c10-s-consolidation-draft`; no se identificó una rama adicional de C10-S que contuviera secciones conversacionales 165–183. El documento C10-S consolidado inspeccionado llega a la sección conversacional 164. La búsqueda de XSYNC no debe confundirse con recuperación de 165–183: son lagunas documentales distintas.

La corrección no altera los límites históricos: las secciones 165–183 siguen sin fuente íntegra identificada en las ramas y PR consultados. No se ha inferido su contenido ni se han reconstruido como texto original.


## 13. Precisión adicional sobre p0 y estado basal (2026-11-04)

La revisión de C10-S §§30.2, 30.4–30.5, 31.4 y 32.4–32.5 corrige una interpretación demasiado fuerte de la primera propuesta de reconciliación. El documento fuente define `B_g0` como política técnica de provisión con probabilidad objetivo `p0=.20` y `B_g1` con `p1=.80`. Por tanto, `p0=.20` no contradice por sí mismo `C_dep,base=0`: puede ser la probabilidad de instalación/accesibilidad después de la asignación bajo la política de control de menor intensidad, mientras el estado basal antes de Z es cero.

La ambigüedad que permanece es otra: el contrato debe distinguir intento (`W_attempt`), éxito de instalación (`S_install`), estado verificado (`C_dep,post`) y accesibilidad basal/post (`A_f,base*`, `A_f,post*`). Los valores .20/.80 deben corresponder a probabilidades finales verificadas para mantener la verdad analítica ilustrativa; si son probabilidades de intento, la verdad debe recalcularse. La reconciliación y el decision log se actualizaron para mantener p0=.20/p1=.80 en el DGP aislado principal y reservar la contaminación/vías colaterales para escenarios adversariales separados.

Esta corrección preserva la intención del contrato §30; no se introduce p0=0 como reemplazo del diseño principal. El valor p0=0 solo podría representar un diseño alternativo de no provisión y requeriría especificación independiente.


## 14. Normalización de contratos de prueba (2026-11-04)

Se ha creado `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` en PR #116. El registro normaliza los contratos conocidos de S4R-01…18, MEAS-01…14, MISS-01…15, VER-01…06, TRJ-01…07, INT-01…02 y GEN-01…12, con fixtures/perturbaciones, truth oculta, resultados esperados, aserciones y condiciones de fallo.

El registro aclara la interpretación temporal del DGP principal: `p0=.20` y `p1=.80` son probabilidades finales post-asignación objetivo de B_g0/B_g1; `C_dep,base=0` es basal. Se exige distinguir intento, éxito de instalación y estado final verificado. Si las probabilidades se refieren solo a intentos, la verdad analítica debe recalcularse.

Este artefacto es una especificación documental. No contiene implementación ni evidencia de ejecución. Las tolerancias, N, réplicas, δ/ε, fixtures exactos y códigos finales de fallo siguen pendientes de justificación y revisión independiente.


## 15. Búsqueda ampliada de fuentes 165–183 y estado del PR (2026-11-04)

La búsqueda de fuentes se amplió a las ramas disponibles del repositorio, PR abiertos/cerrados localizados por C10, y búsquedas de commits con referencias distintivas `P182`, `P183`, `C10-S 165/183` y términos asociados. No aparecieron artefactos originales adicionales de las secciones conversacionales 165–183 ni contratos originales P182/P183. Esta búsqueda no cubre exportaciones privadas de ChatGPT, archivos locales no subidos ni fuentes externas al repositorio.

El texto XSYNC sí quedó localizado y documentado en la sección 12 y en el tracker específico; no debe seguir figurando como laguna de recuperación. La laguna 165–183 permanece separada y abierta.

Verificación final de este corte: PR #116 abierto y Draft, diez archivos modificados, 68 commits; sin comentarios, reviews ni hilos de revisión registrados. Head observado en la consulta: `d444825916d3a34e0c518db3542017cb1258bfd8`. Estos datos son una instantánea y deben consultarse en la ficha del PR para cualquier corte posterior.


## 16. Ampliación de contratos de atribución y cobertura XSYNC (2026-11-04)

El registro `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` se amplió con POL-01…10 para convertir en pruebas discriminantes las condiciones de atribución del ITT_Z a `θ_Af(q*)`, la detección de vías directas/paquete, factibilidad y soporte, separación de q/Value, el estado no formalizado de `θ_A^dyn`, la separación de dictámenes C10-S/C10-D1, la regla δ/ε y los límites de cobertura del enumerador.

Se actualizó la matriz maestra para mapear estos contratos a los hallazgos XSYNC. El mapeo no implica cierre: los tests siguen sin fixtures ejecutables, implementación, tolerancias aprobadas o ejecución.


## 17. Contrato integrado del DGP temporal y separación de roles (2026-11-04)

Se ha creado `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md` en PR #116. Integra en una misma unidad la secuencia basal→asignación→política/provisión→intento→éxito→estado técnico verificado→accesibilidad focal→ΔT_acc completo→Reach/trayectorias→conocimiento/selección/ejecución→Outcome→Value. Incluye matriz de variable×momento, separación generador/analizador/evaluador, indicadores de ausencia por bloque e invariantes DGP-01…16.

El contrato se propone para armonizar AUD-002, AUD-010/011 y XAUD-003…006. La matriz maestra actualiza estos hallazgos a “propuesta integrada/parcial”, no a cerrados. Siguen pendientes la revisión matemática global, el diccionario final, unidad de asignación/interferencia, F*, q*, Value, tolerancias y pruebas/fixtures.


## 18. Recuperación efectiva de la fuente conversacional 165–183 (2026-11-04)

Se recibió el archivo `Notes_261104_163033.docx` y se leyó su contenido completo mediante Files. La fuente contiene 4.366 líneas de texto extraído y cubre desde la sección 165 hasta inmediatamente antes de la 184. Esto corrige el estado previo de “fuente original no localizada”: el contenido primario ya está disponible en la conversación y se ha inventariado en `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`.

La fuente recupera la reconstrucción D1/D2 de la primera etapa, exclusión IV y sus adversariales, sensibilidad δ/γ, LATE y heterogeneidad de compliers, perfiles basales, matriz de potenciales, DGP adversariales, arquitectura de estimación, potencia/reproducibilidad, Value multidimensional, medición A/O/V, validez de constructo y datos ausentes/censura. El registro distingue explícitamente lo propuesto de lo aceptado y enumera alertas para la reconciliación.

**Límite de persistencia:** el DOCX original y la transcripción literal completa aún no están incorporados como archivos en GitHub. La fuente fue recibida y examinada, no se afirma que se haya subido íntegramente. Las tablas se pueden transcribir estructuralmente, pero no conservar su maquetación visual. El nuevo registro de recuperación es una síntesis trazable, no sustituto de la fuente primaria.

Cambio de estado G0: fuente 165–183 **RECUPERADA EN LA CONVERSACIÓN**; persistencia primaria en GitHub **PENDIENTE**; cotejo/reconciliación científica **EN CURSO**. No se declara D1/D2 aceptado, pruebas P181/P182/P183 ejecutadas, revisión independiente, freeze ni autorización de ejecución. La sección 184 permanece fuera del intervalo recuperado y no debe desarrollarse hasta completar la integración.
