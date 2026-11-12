# C10-S — Auditoría de integración B1/Need_preZ en el mapa DGP variable×tiempo×rol

**ID:** C10-S-B1-PREZ-MASTER-TIME-ROLE-INTEGRATION-AUDIT-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_AUDIT / TARGETED_CORRECTION_PROPOSED / NOT_APPROVED / NOT_IMPLEMENTED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Resultado: el crosswalk temporal ya existe; no debe recrearse

La reconstrucción histórica encuentra que el trabajo solicitado está parcialmente realizado y que redactar otro diccionario variable×tiempo×rol sería redundante:

- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md` §2 contiene el reloj común t−1/t0…t9.
- Su §14 incorpora Need_preZ y E_req_preZ en t−1, separándolos de Request_event, D_resource, P* y condiciones de accesibilidad.
- Su §16 define el firewall PE: Generator conserva truth/potenciales; Analyzer recibe observed_evidence; Evaluator accede a truth tras sellar el output.
- Su §28.1 contiene el mapa general variable×tiempo×rol, con truth y observaciones basales en t−1, Analyzer limitado a observaciones y Evaluator con truth.
- `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md` §§3–7 especializa la truth, la observación, la ubicación temporal y los roles B1.
- El crosswalk PE B1 de esta misma línea separa ya las tareas de adjudicación Need E1/E2 y Analyzer PE.

Por tanto, no falta un nuevo reloj ni un nuevo mapa general. La tarea pendiente es una **corrección de granularidad de roles y un enlace explícito** entre el mapa general y la especialización B1.

## 2. Discrepancia concreta que sí requiere corrección

La tabla de roles de `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md` §7 agrupa en una sola columna la expresión “Analyzer/adjudicadores E1/E2”. Esa agrupación contradice la separación establecida por el contrato PE y por el crosswalk B1/PE:

- E1 y E2 son adjudicadores de `Need_preZ`, consumen evidencia B1 autorizada y producen `need_observed_state`.
- Analyzer PE reconstruye/estima constructos y dictámenes por estimando; no es un adjudicador Need por defecto.
- Evaluator B1 compara E1 y E2, cada uno por separado, con `need_truth_state`.
- Evaluator PE compara la salida PE sellada con los oráculos DGP por constructo/estimando.

La ambigüedad no altera por sí sola la semántica de truth ni los estimandos, pero sí puede inducir una implementación incorrecta de permisos, entradas y denominadores. Debe corregirse antes de congelar la interfaz.

## 3. Crosswalk focal variable×tiempo×rol

| Variable/objeto | Tiempo | Generador | Proyector/Sealer | E1/E2 | Analyzer PE | Evaluator |
|---|---|---|---|---|---|---|
| Especificación basal del objetivo B1 | t−1 | Genera y sella en ámbito reservado | Sin exposición de base reservada | Sin acceso | Sin acceso | Acceso tras sellos, para evaluación Need |
| `need_truth_state` y `truth_basis_ref` | t−1 | Genera/sella | Excluye del bundle observable | Sin acceso | Sin acceso | Solo tras sellado de las salidas a evaluar |
| `Need_preZ` como constructo basal | t−1 | Estipula por B1/UE | No lo convierte en etiqueta observada | No recibe truth | No es input universal; solo observación expresamente requerida por estimando | Evalúa contra truth según tarea |
| Fuentes B1/Need y `EVIDENCE_LEDGER` | Referidas a t−1; event_time pre-Z | Genera mediante modelo de observación separado | Selecciona, proyecta y sella el subconjunto permitido | Recibe evidencia autorizada y cobertura | Solo proyección expresamente necesaria para estimando | Acceso conforme al contrato de evaluación |
| `need_observed_state` | Adjudicación después de generar/cerrar evidencia pre-Z; evidencia refiere a t−1 | No adjudica | No adjudica | E1 y E2 emiten independientemente 1/0/? y sellan | No lo emite por defecto ni recibe salidas E1/E2 por defecto | Evalúa E1 y E2 por separado |
| `Z` y asignación | t0 | Genera verdad de asignación según diseño | Proyecta registro observable | Sin papel en adjudicación Need basal | Entrada PE solo conforme al contrato de estimando | Conoce truth de asignación y evalúa según contrato |
| Variables post-Z (B, intento, instalación, accesibilidad, Reach, trayectoria, ejecución, Outcome, Value) | t1–t9 | Genera truth/observaciones según DGP | Proyecta observaciones permitidas | No pueden redefinir Need basal | Recibe observaciones permitidas; no truth/potenciales | Acceso a truth tras sellado |
| `Request_event` y ciclo de solicitud | Ventana exacta aún OPEN; no reasignar a t5/t6/t7 por conveniencia | Genera eventos cuando el contrato temporal lo determine | Proyecta eventos observables | No prueba Need basal | Solo si un estimando lo requiere | Evalúa conforme a contrato |

La tabla es una lectura de interfaz lógica y no un schema físico. La fecha de evaluación/sellado de adjudicaciones no mueve el tiempo semántico de la evidencia: los registros pueden generarse/adjudicarse en fases posteriores, pero la afirmación que soportan se refiere al baseline t−1 y su event_time debe ser pre-Z.

## 4. Enlace correcto con el mapa general §28.1

La fila t−1 del mapa general §28.1 ya cubre el dominio basal y su separación truth/observación. Debe leerse con la especialización B1:

- añadir conceptualmente `Need_preZ` y `E_req_preZ` como constructos/estados basales B1, sin convertirlos en componentes de T_acc, A_f, C_dep o elegibilidad P*;
- mantener `Need_truth_state` reservado al Generator/Evaluator y las fuentes observables en EVIDENCE_LEDGER;
- no ampliar la lista de variables basales por inferencia: `E_req_preZ` sigue siendo distinto de Need y su definición/uso no queda cerrado por este documento;
- preservar que Request_event es un evento separado y que su ventana/posición siguen OPEN;
- mantener Analyzer PE como consumidor de observaciones permitidas, no como consumidor de truth.

No se necesita una segunda tabla temporal general ni una nueva entidad U_G.

## 5. Corrección mínima recomendada

No editar el contrato temporal maestro ni sobrescribir la reconciliación histórica en este paso. Antes de integración formal, proponer una revisión de `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md` §7 que sustituya la columna fusionada “Analyzer/adjudicadores E1/E2” por roles separados:

1. Generator.
2. Proyector/Sealer.
3. Adjudicador E1.
4. Adjudicador E2.
5. Analyzer PE.
6. Evaluator B1/Need.
7. Evaluator PE.

Esta descomposición es de responsabilidades, no obliga a siete servicios físicos ni siete artefactos. El almacenamiento sigue usando los seis artefactos lógicos B1/Need y los objetos PE ya definidos.

La revisión debe conservar las restricciones de cegamiento: E1/E2 no ven truth ni la salida del otro; Analyzer no ve truth, potenciales, parámetros/semillas reservados ni E1/E2 por defecto; Evaluators abren truth tras verificar el sellado de la salida que evalúan.

## 6. Dependencias que permanecen abiertas

Este crosswalk no resuelve:
- atributos basales o regla concreta que genera heterogeneidad de Need por unidad;
- mecanismo/parametrización de emisión, omisión, falsos positivos/negativos, ambigüedad, conflicto, pérdida y corrupción;
- catálogo final de fuentes sintéticas y su autoridad;
- roster B1 y soporte truth=1/0/?;
- mapping físico de EVIDENCE_LEDGER a observed_evidence;
- ventana y semántica final de Request_event;
- suficiencia estadística, potencia, precisión y tolerancias;
- implementación y verificación técnica del firewall.

No se asignan parámetros, tasas, prevalencias, semillas, unidades, IDs, fuentes ni fixtures.

## 7. Dictamen

**REUSE_EXISTING_TIME_ROLE_MAP / TARGETED_ROLE_SPLIT_REQUIRED / NO_NEW_GENERAL_DICTIONARY.**

El mapa general y la especialización temporal B1 ya existen. El gap verificable es la fusión textual de Analyzer con E1/E2 en la tabla de roles de la reconciliación B1. La acción mínima es separar esos roles en la revisión documental correspondiente y conservar los contratos existentes como fuentes autoritativas. Este documento no acepta por sí mismo esa revisión ni modifica el maestro, RMA, Evidence→Claim Matrix, STATUS o decisiones aceptadas.

No se materializa ningún dato, paquete, bundle, fixture, schema, permiso o código. No se ejecutan validadores, DGP, simulación, replay ni análisis estadístico.

`scientific_execution=false`; `execution_authorized=false`.
