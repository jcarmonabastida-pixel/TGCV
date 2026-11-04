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
