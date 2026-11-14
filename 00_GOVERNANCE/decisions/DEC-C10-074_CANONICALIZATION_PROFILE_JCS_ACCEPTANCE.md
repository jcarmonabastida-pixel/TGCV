# DEC-C10-074 — Aceptación de perfil de canonicalización JCS para UDG-01

- **Estado:** ACEPTADA
- **Fecha:** 2026-11-07
- **Ámbito:** C10-S / UDG-01 / envelope U1 de universe_definition
- **Autoridad:** aceptación explícita del usuario

## Decisión

Se acepta C1: RFC 8785 JSON Canonicalization Scheme (JCS) con prevalidación TGCV como política documental de canonicalización del envelope U1, con las restricciones que siguen.

## Reglas aceptadas

1. **Entrada:** UTF-8 válido, JSON válido, sin nombres de propiedad duplicados, lone surrogates ni valores fuera de I-JSON. Rechazar NaN e Infinity.
2. **Unicode:** JCS no reescribe ni normaliza cadenas. Los campos identificadores declarados NFC-required se validan previamente; incumplimiento = FAIL, sin autocorrección. Identificadores case-sensitive; no trim ni case-folding.
3. **Propiedades:** orden recursivo de propiedades conforme a RFC 8785/JCS, no orden local/locale/UTF-8.
4. **Arrays:** arrays declarados como conjuntos se ordenan antes de JCS por clave de identidad estable. Para member_refs: (object_class, object_id, object_record_id). Arrays secuenciales conservan su orden. No ordenar arrays sin clasificación explícita en schema.
5. **Números:** campos numéricos UDG-01 restringidos a enteros seguros no negativos (0…2^53−1); sin floats, -0, NaN o Infinity. Boolean no es entero. Extensiones fuera de rango requerirán representación string tipada.
6. **Null/omisión:** null prohibido en UDG-01. Campo opcional ausente significa no declarado; obligatorio ausente = FAIL. Ausencia de array es distinta de array vacío. EXPLICIT requiere member_refs; [] solo con count=0 y evidencia exhaustiva. RULE_DEFINED requiere inclusion_rule_ref y omite member_refs.
7. **Hash:** SHA-256 sobre bytes UTF-8 canónicos del envelope completo; hash y metadatos de integridad quedan fuera del contenido hasheado. Distinguir source_artifact_hash de canonical_content_hash.
8. **Perfil:** identificador documental `TGCV-C10S-JCS-1`. Cambios de prevalidación, clasificación/orden de arrays, reglas numéricas o tratamiento de campos requieren nueva versión y evaluación de compatibilidad. No sobrescribir hashes históricos.

## Interpretación y límites

- Igual canonical_content_hash bajo el mismo perfil acredita igualdad de bytes canónicos, sujeto a las propiedades criptográficas de SHA-256; no prueba equivalencia semántica, exhaustividad, verdad de las fuentes ni validez causal.
- Distinto source_artifact_hash con mismo canonical_content_hash indica distintas representaciones físicas del mismo contenido canónico bajo el perfil.
- Distinto canonical_content_hash indica distinto contenido canónico, no necesariamente distinto universo semántico.
- Perfiles diferentes no son directamente comparables; se requiere recanonicalización desde fuente preservada bajo perfil común compatible. Si no existe fuente, UNKNOWN/NOT_COMPARABLE.
- Igualdad semántica requiere evaluación explícita separada.

## Alcance de la aceptación

Esta decisión cierra la política documental de canonicalización e integridad de UDG-01. No autoriza ni ejecuta implementación de parser/validator, fixtures, hash de producción, modificación del schema físico, Design Freeze ni ejecución científica. No cierra mapping físico CMP/PAR/REF/RUL/MET ni el control C0 independiente implementado/auditado.

`scientific_execution=false`; `execution_authorized=false`.

## Fuente normativa

RFC 8785, JSON Canonicalization Scheme (JCS): https://www.rfc-editor.org/rfc/rfc8785.html. Es RFC Informational, no Internet Standards Track.

## Propagación requerida

Protocolo de evidencia §20.13; plantilla U_G §18.18; matriz de mapping §20.15; maestro C10-S §192; plan de cierre §16.47; matriz de control §65; Decision Log §71.
