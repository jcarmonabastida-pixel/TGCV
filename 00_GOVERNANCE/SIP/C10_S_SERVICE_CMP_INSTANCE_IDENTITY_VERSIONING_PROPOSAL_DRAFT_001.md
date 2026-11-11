# C10-S — Propuesta de identidad y versionado de la instancia CMP del servicio sintético

**ID:** C10-S-SVC-CMP-ID-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-07  
**Estado:** ACEPTADA DOCUMENTALMENTE POR DEC-C10-069 para IDs y política de versionado; MET físico, serialización, IAM/mapping y evidencia siguen OPEN; no implementada.  
**Ámbito:** C10-S / Opción A / DGP sintético / identidad MET de la instancia de servicio.  
**No autoriza:** serialización ejecutable, fixtures, parser, validación técnica, simulación ni ejecución científica.

## 1. Reconstrucción y reutilización obligatoria

Este documento especializa, no reemplaza:
- DEC-C10-053/056: CMP/PAR/RUL constitutivos y cardinalidades CMP≥1, PAR≥1, RUL≥1; MET obligatorio.
- `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`: esquema `C=(ID_C,V_C,CMP,PAR,REF,RUL,POL?,MET)`, campos de MET, estructura de CMP/PAR/RUL y separación C_src/M/C_dst declarado/C_dst aplicado/E_dst.
- DEC-C10-068 y `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`: servicio sintético, parámetros ENABLED/PROFILE y RUL-SVC-ENABLE-PROFILE-01 aceptados conceptualmente.
- `C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md`: identidad semántica separada de versiones/realizaciones/hashes y matching explícito; sus TID/SID/RID/EID son identidades del espacio transformacional, no IDs CMP y no se reutilizan para componentes.
- `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`: IAM sellado antes de Z/B con identidad/versiones, C_src/C_dst, M, oráculo, cobertura y hash.

No se crea una segunda ontología de identidad ni una capa semántica persistida adicional.

## 2. Distinciones que el contrato debe preservar

| Campo/concepto | Qué identifica | Regla |
|---|---|---|
| `contract_id` | Contrato funcional de referencia | Estable; no cambia por una revisión de contenido |
| `contract_version` | Revisión de semántica/estructura del contrato | Versionado separado de la instancia y del artefacto |
| `instance_id` | Instancia lógica de servicio cuya continuidad se estudia | Persistente entre revisiones comparables |
| `instance_version` | Revisión inmutable del paquete/instancia | Incrementa ante cualquier cambio de contenido declarado |
| `component_id` | Componente CMP concreto dentro de la instancia | Estable en la continuidad declarada; no se deriva del nombre ni del hash |
| `component_class` | Rol semántico del CMP | Clasifica el componente; no es su identidad |
| `owner_component_id` | CMP propietario de un PAR | Referencia resoluble al componente de la instancia |
| `parameter_key` / `rule_id` | Identidad de parámetro/regla dentro del contrato | Persistente y no reutilizable para otro significado |
| `mapping_id/version` | Mapping evaluativo M | Artefacto independiente y versionado |
| `IAM_id/version/hash` | Manifiesto de aplicabilidad/cobertura | Sellado ex ante y enlazado a la instancia y contratos |
| `artifact_hash` | Bytes de una serialización concreta | Identifica artefacto, nunca demuestra equivalencia funcional |

El owner lógico `CMP-SERVICE-LOGIC` usado en DEC-C10-068 es una etiqueta de rol provisional, no un `component_id` único ni un `instance_id`. No debe reutilizarse como si resolviera la identidad concreta.

## 3. Propuesta de identidad de referencia

Se propone fijar para la instancia sintética de referencia:

| Campo | Valor candidato | Alcance |
|---|---|---|
| `contract_id` | `C10S-SVC-REQUEST-PROCESSOR` | Contrato funcional sintético |
| `contract_version` | `1.0.0` | Primera revisión del contrato aceptado conceptualmente; no versión de software real |
| `instance_id` | `C10S-SVC-REQUEST-PROCESSOR-001` | Identidad lógica persistente de la instancia |
| `instance_version` | `1` | Revisión inicial abstracta; no fija valores de escenario |
| `component_id` | `CMP-SERVICE-LOGIC-001` | Único CMP lógico de referencia inicialmente declarado |
| `component_class` | `SERVICE_LOGIC` | Rol semántico |
| `rule_id` | `RUL-SVC-ENABLE-PROFILE-01` | Identificador ya aceptado por DEC-C10-068 |

Los valores anteriores son candidatos de diseño para aprobación, no IDs canónicos ya aceptados. La instancia de referencia contiene al menos un CMP, los dos PAR obligatorios y la RUL aceptada; no se afirma que REF sea cero hasta que IAM y cobertura lo declaren. POL permanece ausente por diseño conforme a DEC-C10-053, salvo módulo secundario predeclarado.

El valor de `component_id` se separa del owner lógico histórico `CMP-SERVICE-LOGIC`: este último puede conservarse como `component_class`/alias de rol, pero no como clave única de instancia.

## 4. Política de versionado propuesta

1. `contract_version` usa MAJOR.MINOR.PATCH:
   - MAJOR: cambio incompatible en unidad funcional, frontera P0/P1, dominios/semántica de parámetros, regla constitutiva o significado contractual.
   - MINOR: extensión compatible declarada del contrato (p. ej., nueva propiedad opcional o regla adicional compatible), siempre con revisión de IAM y análisis de comparabilidad.
   - PATCH: corrección editorial/metadato que no altera semántica, dominios, obligatoriedad, frontera ni resultados de evaluación.
2. `instance_version` es entero positivo monotónico por `instance_id`; cada paquete inmutable nuevo incrementa la revisión. No se sobrescribe una versión histórica.
3. Un cambio de valor/estado de PAR produce nueva revisión de instancia, no nueva identidad de instancia, si conserva continuidad funcional y contrato.
4. Un cambio de significado de una clave, de la función esencial del CMP o de la unidad funcional requiere nueva versión MAJOR del contrato y revisión explícita de continuidad; si rompe identidad semántica, se crea nuevo `instance_id` y se registra sucesión, no se fuerza matching.
5. Cambios de serialización o hash sin cambio semántico no crean por sí solos nueva identidad funcional; se registran como nuevos artefactos/procedencia.
6. `mapping_id/version`, versiones de esquema fuente/destino, IAM y oráculo evolucionan independientemente. No se deducen de `instance_version`.
7. Ningún ID incluye brazo Z/B, tiempo, resultado, outcome, value, plataforma o ubicación física.

La regla de versionado no permite comparar snapshots automáticamente: se requiere matching explícito de identidad, frontera, granularidad, catálogo, contrato y cobertura conforme al contrato de snapshots.

## 5. Contrato mínimo de MET para la instancia

MET deberá enlazar, como mínimo:
- `contract_id`, `contract_version`;
- `instance_id`, `instance_version`;
- `component_id`, `component_class` y referencias de owner;
- IDs/versiones de C_src y C_dst, incluyendo esquema/representación;
- `mapping_id`, `mapping_version`;
- `IAM_id`, `IAM_version`, `IAM_hash`;
- identidad/versión del oráculo y criterio de adjudicación;
- `provenance_refs`, actor/proceso, timestamps y registro de cambios;
- hash del artefacto serializado, una vez fijado el formato exacto.

Los hashes no se inventan ni se calculan sobre una representación todavía no definida. El hash se genera solo después de congelar serialización canónica, codificación, normalización y campos incluidos.

## 6. Reglas de matching y comparabilidad

- Mismo `instance_id` y versiones distintas: continuidad candidata, no equivalencia automática; comparar diffs y reglas de versionado.
- Distinto `instance_id`: no asumir continuidad; exigir relación de sucesión/matching justificada.
- Mismo `component_class` con distinto `component_id`: no prueba identidad del CMP.
- Mismo `component_id` con cambio incompatible de función/contrato: conflicto de identidad; resolver con nueva identidad o sucesión explícita.
- Igualdad de nombre, clave, serialización o hash: insuficiente por sí sola para equivalencia semántica.
- Identidad, frontera, versión, mapping o cobertura no resueltos: `UNKNOWN/NOT_COMPARABLE`, no cero ni ausencia.
- C_src, C_dst declarado y C_dst aplicado siguen siendo entidades/estados separados; E_dst/runtime permanece fuera del objeto P0.

## 7. Relación con F1/A1 y F2/A2

F1/A1 reciben la misma identidad funcional de instancia/contrato y producen representaciones intermedias propias, sin crear una nueva identidad de servicio por el mero cambio de formato. F2/A2 deben aplicar el paquete destino y registrar C_dst declarado y C_dst aplicado por separado.

El mapping M deberá declarar correspondencias para:
- CMP: `component_id`, clase/rol, scope y cardinalidad;
- PAR: `parameter_key`, `owner_component_id`, tipo, estado, dominio y valor;
- RUL: `rule_id`, scope, AST, operandos, dominio y efecto;
- MET: IDs/versiones contractuales y procedencia.

El mapping puede traducir identificadores físicos, pero exige una tabla total/versionada y evidencia de preservación/aplicación. La equivalencia de IDs no sustituye FP-03; FP-06/07 y FP-08 siguen separados.

## 8. Pendientes y no-claims

Aceptado por DEC-C10-069:
- los identificadores y valores de §3;
- la política de versionado de §4;

Pendiente:
- el roster CMP/PAR/RUL completo y la cardinalidad REF con cobertura IAM;
- la forma serializada de MET y el esquema de artefacto;
- identidad/versionado concreto de C_src/C_dst, M, IAM y oráculo;
- predicados, tolerancias, evidencia y adjudicación FP-03/06/07/08.

No se ha elegido plataforma/formato físico, no se ha generado hash, no hay instancia serializada, IAM sellado, mapping implementado, fixture, parser, oráculo validado ni prueba ejecutada. La propuesta no constituye Design Freeze ni autoriza implementación o ejecución científica.

## 9. Dictamen

La propuesta concreta el hueco entre el contrato abstracto de instancia y el servicio sintético aceptado por DEC-C10-068. Distingue rol lógico, identidad de componente, identidad de instancia, versiones contractuales, revisión de paquete y hashes de artefacto. Su aceptación permitiría instanciar documentalmente MET y pasar al mapping semántico por familia, manteniendo abiertos los valores de escenario y la evidencia.


## 10. Estado tras DEC-C10-069

Los valores de §3 y la política de §4 quedan ACCEPTED por `00_GOVERNANCE/decisions/DEC-C10-069_SERVICE_CMP_IDENTITY_AND_VERSIONING_ACCEPTANCE.md`. No se acepta por extensión un formato físico, hash, IAM sellado, mapping implementado ni oráculo validado. No Design Freeze ni autorización de implementación/ejecución.


## 11. Reconciliación PB — identidad de instancia frente a aislamiento por UE (2026-11-11)

DEC-C10-069 acepta C10S-SVC-REQUEST-PROCESSOR-001 como instancia lógica de referencia. DEC-C10S-B1-UNIT-001 establece como requisito una instancia de servicio aislada/versionada por UE. Para evitar reutilizar un mismo instance_id en varias instancias aisladas, PB recomienda interpretar el ID de DEC-C10-069 como instancia ejemplar de referencia y mantener contract_id/version + definición CMP como plantilla común; cada UE recibirá un instance_id único/versionado. component_id será local a la instancia y su clave de referencia será compuesta por instance_id + component_id. La regla de versionado aceptada por DEC-C10-069 se conserva para cada instancia.

**Estado:** propuesta de armonización pendiente de aceptación expresa. No modifica por sí sola DEC-C10-069 ni genera IDs por UE. No hay serialización física, MET material, IAM sellado, hash, parser, fixture ni implementación. La decisión de identidad no autoriza ejecución.


## 12. Decisión aceptada — armonización de instancia única por UE (2026-11-11)

La propuesta de §11 queda **ACCEPTED** mediante `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001`, con aprobación expresa del responsable científico.

- `contract_id=C10S-SVC-REQUEST-PROCESSOR` y `contract_version=1.0.0` son comunes a las UE mientras compartan semántica contractual.
- La definición CMP/PAR/RUL se reutiliza como plantilla funcional común versionada por contrato; no implica estado mutable compartido.
- Cada UE dispone de `instance_id` único en el roster C10-S y de `instance_version` monotónica e independiente.
- `component_id` es local a la instancia; toda referencia inequívoca usa la clave compuesta `(instance_id, component_id)`.
- `C10S-SVC-REQUEST-PROCESSOR-001` se conserva como instancia ejemplar de referencia DEC-C10-069, no como ID común de todas las UE.
- Se conserva la política de versionado MAJOR.MINOR.PATCH del contrato y el versionado independiente de instancia.

La decisión resuelve identidad lógica/documental. No prueba aislamiento material, independencia de recursos/estado/credenciales/colas/infraestructura, ni define roster/IDs concretos por UE, serialización MET, schema físico, IAM/ACL o pruebas. Esos cierres siguen abiertos en PB/PE. No autoriza implementación ni ejecución.
