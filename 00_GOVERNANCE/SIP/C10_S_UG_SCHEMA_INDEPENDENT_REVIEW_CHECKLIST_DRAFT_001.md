# C10-S — Paquete de revisión independiente del esquema U_G

**ID:** C10-S-UG-SCHEMA-REVIEW-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PREPARADO PARA REVISIÓN / NO REVISADO / NO APROBADO / NO EJECUTADO.  
**Ámbito:** consistencia, semántica, integridad y aptitud de captura de la plantilla U_G y su protocolo de evidencia.

## 1. Propósito

Preparar una revisión externa e independiente del esquema normalizado U_G tras las auditorías documentales FCM-01…20. Este paquete define qué debe revisar el revisor, qué artefactos gobiernan cada criterio, qué evidencia debe aportar y cómo emitir un dictamen sin confundir revisión documental, validación ejecutable, seguridad, inventario real o cierre científico.

Este documento no constituye una revisión independiente ni sustituye una validación con parser/constraints. Su creación no autoriza implementar el esquema, inspeccionar sistemas, poblar truth DGP, generar datos, simular ni ejecutar C10-S.

## 2. Artefactos de revisión

| Artefacto | Función | Revisión requerida |
|---|---|---|
| C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md | Esquema físico de objetos, evidencia, cobertura, evaluación y adjudicación | Principal |
| C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md | Reglas de fuentes, procedencia, evidencia negativa, cobertura y adjudicación | Principal |
| C10_S_SYSTEM_BOUNDARY_AND_GRAPH_GRANULARITY_CONTRACT_DRAFT_001.md | Frontera, granularidad y universo operativo | Semántica U_G |
| C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md | Catálogo y estados trivalentes | Correspondencia U_G |
| C10_S_TRANSFORMATIONAL_SNAPSHOT_AND_DELTA_RECONCILIATION_DRAFT_001.md | Snapshots y cambios estructurales/epistémicos | Temporalidad/versionado |
| C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md | TID/SID/RID/EID e identidad | Identidad |
| C10_S_REACHABILITY_AND_TRAJECTORY_PROPAGATION_CONTRACT_DRAFT_001.md | Propagación trivalente a Reach/Trayectoria | Semántica de estados |
| C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md | Roles, reloj y truth DGP | Firewall causal/epistémico |

Los hashes/commits deben recuperarse de la rama y fijarse en el expediente de revisión al iniciarla; no se consideran congelados por esta lista.

## 3. Perfil de independencia

Se propone como mínimo:

- **R1 — revisor de modelo de datos/ingeniería:** independiente de la autoría del esquema; evalúa normalización, cardinalidades, claves, tipos, dominios, integridad, versionado y aptitud de validación.
- **R2 — revisor metodológico/causal:** independiente de la autoría del DGP; evalúa separación de constructos, trivalencia, cobertura negativa, cegamiento, no circularidad, independencia de evidencia y propagación a A_f*, F_alt y Reach.
- Un mismo revisor no debe adjudicar sus propias discrepancias. Si R1/R2 discrepan en un control crítico, se designa un tercer adjudicador.
- Registrar conflictos de interés, participación previa, acceso a hipótesis, Outcome/Value y asignación Z/B.
- Los revisores no reciben truth DGP, ni valores ocultos que permitan reconstruirla. Deben permanecer cegados a Outcome/Value y, cuando sea viable, a Z/B.

Este perfil es una propuesta, no una exigencia aprobada. La autoridad de gobernanza debe confirmar el número y perfil antes de solicitar la revisión.

## 4. Lista de controles

Estados permitidos por control: PASS / FAIL / CONDITIONAL / NOT_ASSESSED. Cada resultado requiere fundamento, artefacto/versión, referencia exacta, impacto y acción correctiva.

| ID | Control | Criterio de aceptación |
|---|---|---|
| SR-01 | Identidad de cada registro | object_record_id único por fila versionada; IDs semánticos separados |
| SR-02 | Claves y referencias | Todas las FK resuelven; no hay huérfanos ni colisiones |
| SR-03 | Cardinalidad de evidencia | CLAIM_EVIDENCE_LINK representa relaciones múltiples sin listas serializadas |
| SR-04 | Evidencia por evaluador | E1/E2/adjudicador se enlazan a evidencia revisada de forma reconstruible |
| SR-05 | Cobertura | COMPLETE siempre tiene universo versionado, denominador, fuentes válidas, excepciones y regla |
| SR-06 | Trivalencia | observed_state, evidence_status y coverage_status son independientes |
| SR-07 | Evidencia negativa | Ningún 0 se asigna sin argumento de cobertura negativa suficiente |
| SR-08 | Rutas | parent_route_class usa exactamente las cinco clases U_G; subtype separado |
| SR-09 | Dependencias | Directas/transitivas, dinámicas, externas, compartidas y opacas quedan diferenciadas |
| SR-10 | Identidad/versionado | TID/SID/RID/EID y supersession preservan continuidad y cambios materiales |
| SR-11 | Snapshots | Unidad, fase, tiempo, scope, hash, método y cobertura permiten comparabilidad |
| SR-12 | Cegamiento | Evaluadores no reciben Outcome/Value ni truth; ruptura registrada |
| SR-13 | Truth firewall | Ningún campo/artefacto accesible al analizador expone DGP_TRUTH_SECURE |
| SR-14 | No circularidad | F*, oráculo y ruta substituible se definen ex ante e independientemente de Outcome/Value |
| SR-15 | Propagación | La indeterminación en dependencias/rutas se propaga correctamente a A_f*, F_alt, Reach |
| SR-16 | Correspondencia U_G | N01–N23, E01–E23, predicados y clases de ruta se mapean sin inventar objetos |
| SR-17 | Tipos y dominios | Enums, timestamps, hashes, conteos, NA y cegamiento tienen tipos y reglas no ambiguos |
| SR-18 | Historial | Revisiones crean nuevos registros y conservan supersedes_record_id |
| SR-19 | Seguridad y custodia | Secretos/datos personales quedan fuera de GitHub; referencias seguras y permisos trazables |
| SR-20 | Aptitud operativa | El esquema permite poblar, consultar, revisar y reconstruir el expediente sin pérdida semántica |

## 5. Revisión estática ya realizada por autoría

Se ha realizado una comprobación estática limitada del Markdown remoto:

- Diez tablas revisadas: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER.
- Encabezado, separador y fila de esquema tienen el mismo número de columnas en las diez tablas.
- Las cinco tablas de objetos contienen los campos comunes exigidos.
- La tabla analítica de predicados no contiene campo truth_dgp.
- Se corrigieron FCM-01…20 en la documentación.

Esta comprobación no valida FK, unicidad, tipos, dominios, cardinalidades reales, parser, seguridad, permisos, cegamiento, ni compatibilidad con un motor de datos. No es independiente y no debe puntuarse como revisión SR-01…20.

## 6. Procedimiento de revisión propuesto

1. Fijar commit SHA y hashes de todos los artefactos incluidos.
2. Confirmar independencia, roles, conflictos de interés y cegamiento de R1/R2.
3. Revisar cada control SR-01…20 contra la versión exacta, registrar PASS/FAIL/CONDITIONAL/NOT_ASSESSED y referencias.
4. Ejecutar revisión manual del modelo relacional y, solo tras autorización, validadores no destructivos de tipos, FK, unicidad, dominios y serialización.
5. No usar datos técnicos reales ni truth DGP durante la revisión documental.
6. Registrar discrepancias por control; adjudicar las críticas con un tercero.
7. Emitir dictamen global:
   - **ACCEPTABLE FOR SCHEMA FREEZE:** todos los controles críticos PASS; ningún FAIL; CONDITIONAL solo con límites explícitos no bloqueantes.
   - **CONDITIONAL:** faltan controles no críticos o hay limitaciones acotadas.
   - **REVISE:** cualquier fallo crítico de integridad, trivalencia, truth firewall, cobertura, identidad o trazabilidad.
   - **NOT ASSESSABLE:** artefactos/commits incompletos, independencia/cegamiento no demostrables o evidencia insuficiente.
8. El dictamen no autoriza por sí solo inspección técnica, generación, simulación o experimento; se requiere autorización separada.

## 7. Evidencia que debe producir la revisión

- Identidad de revisores y declaración de independencia/conflictos.
- Commit SHA y hashes de artefactos.
- Matriz SR-01…20 con estado y justificación.
- Registro de comentarios y discrepancias.
- Adjudicaciones y posiciones minoritarias.
- Resultado de validación ejecutable, si se autoriza, separado de la revisión documental.
- Dictamen y límites.
- Lista de cambios requeridos y decisión explícita sobre freeze.

## 8. Estado y límites

**Estado actual:** paquete preparado; revisión independiente NO INICIADA. No se han designado revisores. No se han ejecutado validadores ni tests de esquema. No existe instancia poblada, inventario real ni cobertura técnica. A_f*, F_alt,0 y Reach_H siguen indeterminados.

La revisión independiente y validación ejecutable son gates previos a declarar el esquema congelado. La selección del microdominio y el inventario se mantienen posteriores a esos gates. XSYNC-138-01 y FCM-01…20 no se declaran cerrados por la mera creación de este paquete.

No modifica main, RMA, Evidence→Claim Matrix, STATUS, TGCV Core, ni claim-level statuses. No cambia la autorización científica.


## 9. Addendum de alcance — Opción A / ROUTE_STEP (2026-11-05)

La sección 5 documenta una revisión estática histórica de diez tablas, anterior a DEC-C10-064. No debe interpretarse como control de la plantilla vigente. La versión actual incluye además ROUTE_STEP (19 tablas Markdown totales, 11 registros operativos si se cuenta ROUTE_STEP como relación normalizada adicional) y nuevos campos snapshot_id y referencias exactas.

Antes de iniciar la revisión independiente R1/R2, incorporar OAS-01…07 del informe `C10_S_UG_OPTION_A_RECONCILIATION_AUDIT_DRAFT_001.md`, fijar el commit exacto de todos los artefactos y resolver OAS-02. La revisión independiente continúa NOT STARTED; el addendum no cambia ningún estado SR-01…20 ni acredita PASS técnico.
