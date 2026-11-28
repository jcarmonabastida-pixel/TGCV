# DEC-C10-078 — Aceptación del contrato lógico de filas IAM

**Fecha:** 2026-11-07  
**Estado:** ACEPTADA — contrato documental lógico  
**Ámbito:** C10-S / Instance Applicability Manifest (IAM)  
**Rama de registro:** `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta como base documental la estructura de cuatro capas del IAM y el contrato lógico de filas descrito en esta decisión y propagado a la matriz C10-S. La aceptación permite desarrollar la especificación documental de aplicabilidad; no equivale a congelación de schema, roster exhaustivo, instancia IAM poblada ni autorización de implementación.

## 2. Cuatro capas aceptadas

- **L1 — Membership del universo:** pertenencia de objetos CMP/PAR/REF/RUL/MET al universo declarado, con identidad lógica y referencia exacta al registro/versionado correspondiente.
- **L2 — Referencias del envelope UDG:** referencias tipadas usadas por el envelope para declarar membresía, ownership, source, reglas de inclusión/exclusión, dependencias o procedencia. Los ejemplos `MEMBER`, `OWNER`, `SOURCE`, `INCLUSION_RULE`, `EXCLUSION_RULE`, `DEPENDENCY` y `PROVENANCE` siguen siendo ilustrativos; un `ref_role` no crea automáticamente un objeto REF.
- **L3 — Extremos funcionales REF:** un objeto REF posee identidad propia y extremos funcionales tipados. SOURCE/TARGET se acepta como patrón binario de extremo, no como catálogo cerrado de roles; una relación n-aria exige representación/grupo explícito que conserve sus extremos.
- **L4 — FK/vínculos estructurales U_G:** relaciones estructurales entre registros/tablas U_G. No se contabilizan como objetos REF por defecto; solo podrían serlo mediante declaración de dominio independiente, explícita y justificada.

Las capas no comparten automáticamente universo, denominador, obligatoriedad ni reglas de cardinalidad.

## 3. Contrato lógico de fila IAM

La fila lógica incluye los siguientes campos, con semántica contextual por capa:

`iam_rule_id`, `layer`, `source_class`, `source_identity_rule`, `role_namespace`, `role_key`, `endpoint_position`, `target_domain`, `min_cardinality`, `max_cardinality`, `requiredness`, `applicability_trigger`, `stage_key`, `scope_mode`, `route_binding`, `version_snapshot_binding`, `integrity_rule`, `mapping_rule`, `evidence_rule`, `adjudication` y `rationale/provenance`.

El contrato es lógico: no exige que todos los campos tengan valor en todas las capas ni define todavía una serialización física. La aplicabilidad de cada campo depende de la capa, clase, rol, extremo, etapa y scope.

## 4. Límites explícitos de la aceptación

No se aceptan ni fijan en esta decisión:

- un vocabulario cerrado de roles o namespaces;
- cardinalidades numéricas concretas;
- valores o semántica final REQUIRED/OPTIONAL/CONDITIONAL;
- endpoints externos o sus dominios;
- un enum de `relation_type`;
- un mapping M concreto, ni reglas concretas split/merge;
- schema físico, DDL, tablas, FKs adicionales, API, registry o resolver;
- roster exhaustivo, IAM de instancia poblado, fixtures, parser o validator.

Se reutilizan los siete `stage_key` ya aceptados por DEC-C10-071: `C_SRC`, `F1_S2`, `A1_S1`, `F2_DST_DECL`, `A2_DST_DECL`, `F2_DST_APPLIED`, `A2_DST_APPLIED`. El scope global reutiliza `C10S_SCOPE_GLOBAL` según DEC-C10-072; no es un `route_id`. Estos valores no se reabren ni amplían aquí.

## 5. Consecuencias y estado

1. La matriz C10-S §19.12 incorpora la estructura de capas y el contrato lógico de fila.
2. El Decision Log recibe el asiento §78.
3. El trabajo siguiente puede desarrollar vocabularios candidatos por capa, distinguiendo roles UDG de roles funcionales REF, sin convertir propuestas en enums aceptados.
4. Las cardinalidades, obligatoriedad, endpoints externos, mapping M y reglas de integridad/evidencia/adjudicación concretas permanecen OPEN.
5. No se modifica DEC-C10-077 ni se reinterpreta su aceptación conceptual REF↔UDG-04.
6. No se autoriza implementación, validación ejecutable, fixtures, simulación, experimento, Design Freeze ni ejecución científica.

**Naturaleza:** aceptación de contrato documental lógico; no constituye cierre del IAM ni del diseño C10-S.
