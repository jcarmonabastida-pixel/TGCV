# DEC-C10-069 — Aceptación de identidad y versionado CMP del servicio sintético

**Fecha:** 2026-11-07  
**Estado:** ACCEPTED — decisión de diseño documental para C10-S  
**Ámbito:** Opción A, DGP sintético, instancia lógica de servicio aceptada por DEC-C10-068.  
**Base:** contrato abstracto de instancia, contrato de matching de snapshots y propuesta C10-S-SVC-CMP-ID-001.  
**Autorización de ejecución científica:** `false`  
**Autorización de implementación/fixtures/validación ejecutable/simulación:** `false`

## 1. Decisión

Se acepta la propuesta de identidad y versionado contenida en `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md`, con los identificadores y política que siguen, como contrato documental de referencia de la instancia sintética.

| Campo | Valor aceptado |
|---|---|
| `contract_id` | `C10S-SVC-REQUEST-PROCESSOR` |
| `contract_version` | `1.0.0` |
| `instance_id` | `C10S-SVC-REQUEST-PROCESSOR-001` |
| `instance_version` | `1` |
| `component_id` | `CMP-SERVICE-LOGIC-001` |
| `component_class` | `SERVICE_LOGIC` |

`CMP-SERVICE-LOGIC`, utilizado en DEC-C10-068, permanece como etiqueta provisional de owner/rol lógico, no como ID único de componente o instancia. `CMP-SERVICE-LOGIC-001` es el ID del CMP lógico de referencia en esta instancia.

Los IDs de parámetros y regla aceptados en DEC-C10-068 permanecen sin cambio: `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` y `RUL-SVC-ENABLE-PROFILE-01`. `PAR-SVC-RETRY-COUNT` permanece excluido del núcleo.

## 2. Política de versionado aceptada

1. `contract_version` usa MAJOR.MINOR.PATCH. MAJOR para cambios incompatibles de unidad funcional, frontera, dominios/semántica de PAR o reglas constitutivas; MINOR para extensiones compatibles declaradas con revisión IAM/comparabilidad; PATCH solo para correcciones sin efecto semántico.
2. `instance_version` es entero positivo, monotónico e inmutable por `instance_id`; todo paquete nuevo incrementa la revisión y no sobrescribe una anterior.
3. Cambios de valores/estados PAR generan nueva revisión de instancia si preservan continuidad funcional y contrato.
4. Cambio de significado de clave, función esencial CMP o unidad funcional exige nueva MAJOR y revisión explícita de continuidad; si rompe identidad semántica, se crea nuevo `instance_id` y se registra sucesión.
5. Cambios de serialización/hash sin cambio semántico crean un artefacto/procedencia nueva, no una identidad funcional nueva.
6. Versiones de C_src/C_dst, M, IAM y oráculo evolucionan independientemente de `instance_version`.
7. IDs no codifican brazo Z/B, tiempo, resultado, outcome, value, plataforma ni ubicación física.

## 3. MET, hashes y matching

MET debe enlazar IDs/versiones de contrato, instancia y CMP; C_src/C_dst y sus esquemas; M; IAM; oráculo/adjudicación; procedencia; actor/proceso y timestamps. Hash del artefacto solo se generará después de definir serialización canónica, codificación, normalización y campos incluidos.

La aceptación no declara equivalencia automática entre versiones o snapshots. Matching exige identidad, frontera, granularidad, catálogo, contrato y cobertura comparables. Identidad/frontera/mapping/cobertura no resueltos producen UNKNOWN/NOT_COMPARABLE. C_src, C_dst declarado y C_dst aplicado permanecen separados; E_dst/runtime fuera del objeto P0.

## 4. Efectos y límites

Esta decisión cierra los identificadores y la política documental de identidad/versionado de la instancia sintética de referencia. Permite continuar con la tabla de mapping semántico por CMP/PAR/RUL y con la instanciación documental de MET/IAM.

No acepta una plataforma o formato físico; no define valores por escenario; no sella IAM ni mapping; no fija REF=0; no valida parser, oráculo, preservación o aplicación; no crea serialización, fixtures ni pruebas; no constituye Design Freeze ni autoriza implementación o ejecución científica.

## 5. Continuidad y precedencia

DEC-C10-069 especializa DEC-C10-068 sin modificar su contrato funcional. El documento de propuesta queda aceptado en los apartados cubiertos por esta decisión; los campos, mappings, oráculo y evidencia enumerados como pendientes conservan estado OPEN. En caso de discrepancia, esta decisión gobierna los IDs y la política de versionado aceptados; no reescribe contratos históricos ni las identidades TID/SID/RID/EID del espacio transformacional.
