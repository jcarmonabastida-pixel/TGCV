# C10-S — B1: auditoría de compatibilidad del contrato Need_preZ con DGP temporal y U_G

**ID:** C10-S-B1-PREZ-DGP-UG-COMPATIBILITY-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** READ_ONLY_COMPATIBILITY_AUDIT / PARTIAL_COMPATIBILITY / SCHEMA_TARGET_GAP_OPEN / NO_SCHEMA_CHANGE / NOT_APPROVED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Entradas:** `C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md`; `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`; `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md`; protocolo U_G de evidencia/adjudicación; decisiones B1/UE/instancia.

## 1. Resultado ejecutivo

La separación conceptual truth DGP / evidencia observada / adjudicación es compatible con los contratos existentes. También son compatibles la procedencia normalizada, la regla 1/0/?, la cobertura negativa y el almacenamiento restringido de truth.

**No existe, sin embargo, un destino U_G actualmente aprobado para registrar una afirmación Need_preZ por B1/UE con evaluación E1/E2 y adjudicación.** Los enums de `CLAIM_EVIDENCE_LINK`, `EVALUATOR_ASSESSMENT` y `ADJUDICATION_REGISTER` limitan el target a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE. El registro PREDICATE actual es de predicados del grafo/ruta y no se puede reutilizar sin más para una afirmación basal sobre B1. Los scopes de cobertura están definidos en la captura C10-S para dimensiones de configuración CMP/PAR/REF/RUL/MET, no para el objetivo del beneficiario.

No se amplía el enum, no se crea tabla/clase nueva y no se fuerza Need dentro de PREDICATE. Este es un gate de decisión de representación, no una razón para fabricar un esquema provisional.

## 2. Matriz de compatibilidad

| Requisito del contrato Need | Fuente/esquema vigente | Resultado | Observación |
|---|---|---|---|
| UE, B1 y servicio con identidad separada | DEC-C10S-B1-UNIT-001 y DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | COMPATIBLE / MATERIAL OPEN | Las reglas de identidad están aceptadas; IDs y roster no están materializados. |
| Ancla temporal basal antes de Z | DGP temporal §2, t−1 antes de t0 | PARCIAL | Orden temporal disponible; el reloj no incorpora explícitamente el objetivo B1/Need como objeto basal ni su baseline_record_id. El contrato Need propone ese vínculo sin cambiar el reloj. |
| Truth DGP segregada | U_G §12.6 DGP_TRUTH_SECURE; DGP temporal §§6–7 | COMPATIBLE CONDICIONAL | La separación está documentada; el contrato temporal está en Draft/no aprobado. DGP_TRUTH_SECURE no está creado ni poblado y la plantilla prohíbe exponerlo al Analyzer. |
| Evidencia y provenance | EVIDENCE_REGISTER + CLAIM_EVIDENCE_LINK | PARCIAL | EVIDENCE_REGISTER puede conservar origen, método, alcance, tiempo, integridad y limitaciones. El vínculo de afirmación no dispone de target B1/UE/Need. |
| Estado observado 1/0/? | Registros U_G y protocolo UG | PARCIAL | Las reglas son compatibles; no hay registro de objeto/target aprobado donde guardar Need_observed_state sin sobrecargar PREDICATE. |
| Cobertura por unidad/denominador | COVERAGE_REGISTER | PARCIAL | El envelope versionado soporta universo/denominador; la dimensión C10S_CONFIG_* actual es de configuración. No existe dimensión/afirmación Need aceptada ni scope C0 materializado. |
| E1/E2 independientes | EVALUATOR_ASSESSMENT | INCOMPATIBLE EN TARGET | object_type no admite B1/UE/Need; no hay target FK para la afirmación basal. |
| Adjudicación de discrepancias | ADJUDICATION_REGISTER | INCOMPATIBLE EN TARGET | Mismo límite de tipos/FK; no puede registrar la decisión Need sin destino válido. |
| Comparación truth-observed sellada | DGP temporal §6 + DGP_TRUTH_SECURE | COMPATIBLE CONDICIONAL | La secuencia de roles es coherente, pero debe añadirse Need al diccionario variable×tiempo×rol y definirse el output evaluador. |

## 3. Hallazgos de representación

### 3.1 No forzar Need a PREDICATE

PREDICATE representa una condición evaluable de una ruta, con route_id/step/time y familias técnicas ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT. Need_preZ es una afirmación sobre el objetivo basal de B1, no una condición de ruta. Reutilizar PREDICATE exigiría asignar route_id ficticio, alterar semántica o introducir una sobrecarga que afectaría Reach y el grafo. No procede.

### 3.2 No usar COVERAGE_SCOPE como sustituto del target

COVERAGE_SCOPE representa el universo/denominador de cobertura, no la identidad de la B1 ni el objetivo que se adjudica. Puede describir cobertura de una dimensión si se acepta un scope apropiado, pero no sustituye un target individual para E1/E2 y adjudicación.

### 3.3 EVIDENCE_REGISTER puede reutilizarse, pero no resuelve el vínculo

Las fuentes Need-bearing pueden registrarse en EVIDENCE_REGISTER sin tabla nueva. La brecha no es la procedencia del archivo, sino el destino tipado de la afirmación B1/UE/Need y sus registros de evaluación. No crear evidence_id si el artefacto no existe.

### 3.4 El reloj t−1 es suficiente como precedencia, no como registro

El DGP temporal sitúa variables basales en t−1 y asignación en t0. Se puede anclar Need en t−1 sin inventar un nuevo tiempo causal. Pero el diccionario de variables/roles debe incluir Need_truth, Need_evidence y Need_observed con permisos distintos, así como la referencia a la unidad B1.

## 4. Decisión requerida antes de schema/fixtures

Debe elegirse documentalmente una representación válida, conservando las entidades tipadas y sin abrir una tabla/clase nueva por defecto. Las alternativas que merecen evaluación son:

1. **Claim extension sobre entidad existente:** ampliar de forma explícita y controlada el modelo de claim para admitir una afirmación basal sobre B1/UE, si el contrato canónico de claims y su FK pueden representarla sin romper U_G.
2. **Registro de adjudicación externo a U_G:** mantener EVIDENCE_REGISTER para las fuentes y definir un registro específico del módulo B1/Need, vinculado a UE/B1 y a CLAIM_EVIDENCE_LINK mediante una extensión aprobada. Esto añade un objeto de módulo, no una clase de grafo; requiere decisión de gobernanza y schema.
3. **No persistir clasificación Need en U_G:** conservarla en un artefacto analítico B1 separado y versionado, con provenance/coverage y separación de roles propias, si se demuestra que no necesita interoperar con EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER.

No se recomienda ninguna alternativa todavía. Antes debe revisarse el contrato canónico de claims y el alcance normativo de U_G; no basta con que una opción sea técnicamente posible.

## 5. Correcciones documentales requeridas al contrato Need

Antes de aprobación:
- añadir un crosswalk explícito a t−1 (baseline) y t0 (Z), sin alterar el reloj;
- incorporar Need al diccionario variable×tiempo×rol del DGP temporal, diferenciando truth reservada, evidencia observada y salida adjudicada;
- especificar qué rol produce cada artefacto y cuándo se sella;
- resolver el target de claim, evaluator, adjudication y coverage sin forzar PREDICATE ni declarar un nuevo enum;
- mantener separadas la cobertura del objetivo B1 y la cobertura técnica IAM/configuración del servicio.

## 6. Dictamen

`CONCEPTUAL_ROLE_SEPARATION_COMPATIBLE / EVIDENCE_PROVENANCE_REUSABLE / BASELINE_CLOCK_PARTIAL / U_G_TARGET_TYPE_GAP / NO_SCHEMA_CHANGE / NOT_IMPLEMENTED / NOT_EXECUTED`.

El contrato de materialización Need_preZ queda como propuesta documental pendiente de reconciliación de representación. No se crean tablas, clases, enums, FK, columnas, registros, IDs ni fixtures. No se ejecuta validación técnica, simulación o experimento. `scientific_execution=false`; `execution_authorized=false`.

**Siguiente dependencia:** inspeccionar el contrato canónico de claims y las decisiones U_G de tipos de target para determinar si existe una representación admitida sin ampliar el esquema. Solo después debe elegirse la alternativa y, si procede, actualizar el contrato Need.
