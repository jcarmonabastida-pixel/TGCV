# DEC-C10-077 — Aceptación de la reconciliación conceptual REF↔UDG-04

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-07
- **Ámbito:** C10-S / UDG-04 / catálogo REF / correspondencia REF↔U_G
- **Autoridad:** aceptación explícita del usuario
- **Predecesora:** DEC-C10-076

## Decisión

Se acepta como base conceptual documental la reconciliación REF↔UDG-04 presentada en la propuesta de §76 del Decision Log y propagada en los artefactos C10-S. Esta aceptación fija distinciones semánticas y límites de correspondencia; no cierra el catálogo REF, los roles, cardinalidades, obligatoriedad, IAM ni el esquema físico.

## Distinciones aceptadas

1. **REF de configuración** es un objeto del dominio con identidad propia; no es sinónimo de EDGE, FK estructural U_G ni CLAIM_EVIDENCE_LINK.
2. **Referencia tipada UDG-04** identifica un target exacto mediante rol, clase, identidad lógica y object_record_id; el rol de referencia no crea por sí mismo un objeto REF.
3. **FK/vínculo estructural U_G** mantiene su función de integridad de registros y no se cuenta como miembro REF del universo salvo declaración de dominio independiente, explícita y justificada.
4. REF tiene extremos tipados y conserva dirección, tipo/rol de relación, multiplicidad e integridad. Se admiten relaciones binarias; una estructura n-aria debe modelarse explícitamente, sin aplanamiento silencioso.
5. REF→EDGE es una correspondencia candidata únicamente mediante mapping M explícito y versionado. No se presume correspondencia 1:1: split/merge o n-aria requiere identidad parent/group y conservación verificable de extremos, dirección, tipo/rol, multiplicidad e integridad. EDGE→REF no se infiere automáticamente.
6. Los roles MEMBER, OWNER, SOURCE, INCLUSION_RULE, EXCLUSION_RULE, DEPENDENCY y PROVENANCE de DEC-C10-076 siguen siendo ilustrativos; no se convierten en enum físico cerrado. Se distingue pertenencia del envelope de las relaciones funcionales declaradas por objetos REF.

## Límites y pendientes explícitos

- Permanecen abiertos: vocabulario/semántica final de roles; dominios de origen y destino; endpoints internos/externos; cardinalidad y obligatoriedad por clase, rol, extremo, stage_key y scope; reglas de ciclos; aplicabilidad IAM; mapping M concreto; relación con registros externos; evidencia y adjudicación por escenario.
- No se asignan cardinalidades numéricas ni REQUIRED/OPTIONAL a clases/roles concretos mediante esta decisión.
- Resolver extremos no demuestra pertenencia al universo, equivalencia semántica, disponibilidad/instalación de dependencia ni ejecución.
- Las FKs Opción A, ROUTE_STEP y CLAIM_EVIDENCE_LINK conservan los contratos U_G previos; no se reinterpretan como REF de configuración.
- Esta aceptación no modifica el schema normalizado ni autoriza DDL, enum físico, registry concreto, resolver/API, parser, validator, comparator, fixtures, implementación, Design Freeze ni ejecución científica.

scientific_execution=false; execution_authorized=false.
