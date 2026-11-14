# DEC-C10-071 — Aceptación del vocabulario controlado stage_key C10-S

**Fecha:** 2026-11-07  
**Estado:** ACCEPTED — decisión de diseño documental  
**Ámbito:** C10-S; vocabulario de etapa de captura asociado al binding C0 aceptado por DEC-C10-070.  
**Base histórica:** plantilla U_G §18.2; reconciliación del crosswalk C0↔U_G en maestro §186, protocolo de evidencia §20.4 y matriz de control §59.  
**Autorización de implementación/validación ejecutable/ejecución científica:** `false`

## 1. Decisión aceptada

Se acepta como vocabulario controlado de `stage_key` C10-S, exactamente con los siguientes siete valores:

| stage_key | Significado |
|---|---|
| `C_SRC` | Snapshot de configuración fuente |
| `F1_S2` | Estado S2 producido por F1 |
| `A1_S1` | Estado S1 producido por A1 |
| `F2_DST_DECL` | Configuración destino declarada para F2, antes de aplicar |
| `A2_DST_DECL` | Configuración destino declarada para A2, antes de aplicar |
| `F2_DST_APPLIED` | Estado destino observado tras aplicación de F2 |
| `A2_DST_APPLIED` | Estado destino observado tras aplicación de A2 |

No se admiten sinónimos, variantes de capitalización ni valores implícitos. Un stage no aplicable o no observable no se inventa ni se sustituye por otro valor; se trata según la semántica trivalente y las reglas de cobertura del contrato correspondiente.

## 2. Separación de ejes temporales

La aceptación no fusiona los siguientes ejes:

1. `stage_key`: etapa del proceso de captura/migración C10-S, conforme a esta decisión.
2. Reloj DGP `t−1…t9`: tiempo causal/analítico del DGP. Cualquier correspondencia entre stage y tiempo DGP requiere regla explícita en el universo versionado; no se deriva del nombre.
3. `SNAPSHOT.phase`: contexto/tipo de captura conforme a su dominio existente (`baseline`, `post-B`, `rollback`, `route-test`). No es sinónimo ni almacenamiento alternativo de stage_key.
4. `SNAPSHOT.timestamp`: instante efectivo de captura; no identifica por sí solo la etapa.

## 3. Binding C0 y límites de esta aceptación

`stage_key` es el componente de etapa de la tupla C0 aceptada por DEC-C10-070 y se declara en `COVERAGE_REGISTER.universe_definition/version`.

Esta decisión **no** acepta:
- codificar o parsear `stage_key` desde `SNAPSHOT.scope`;
- la serialización ilustrativa de §18.2 (`program=...`, `stage_key=...`, `route=NONE|F|A`, `object_class=CONFIG`);
- `NONE/F/A` como valores de `route_id`;
- `CONFIG` como `object_class`;
- token global de ruta, gramática completa, canonicalización o hash de `universe_definition/version);
- mapping físico/por propiedad entre CMP/PAR/REF/RUL/MET y registros U_G;
- creación de scopes, snapshots, fixtures, schema, parser, controles ejecutables u oráculo.

Las etiquetas `F/A` pueden mantenerse como metadato auxiliar de familia de ruta si se define y versiona por separado; no sustituyen route_id exacto. La clase C0 sigue siendo CMP/PAR/REF/RUL/MET y `dimension` permanece fuera de la tupla C0, como atributo de COVERAGE_REGISTER.

## 4. Consecuencia y estado

El vocabulario de `stage_key` pasa de CANDIDATE/OPEN a ACCEPTED DOCUMENTAL. El mapping de cada stage a snapshots concretos, el route_id exacto o token global, la gramática de `universe_definition/version`, el crosswalk por propiedad y el enforcement C0 permanecen OPEN/CONDITIONAL según sus gates.

Esta decisión no modifica schema, no crea datos, no constituye Design Freeze y no autoriza implementación, validación ejecutable, simulación ni ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.

## 5. Precedencia

DEC-C10-071 especializa DEC-C10-070 únicamente en el vocabulario permitido de `stage_key). No modifica DEC-C10-065/Opción A, DEC-C10-068 ni DEC-C10-069. La sección histórica U_G §18.2 se conserva; cualquier serialización o mapping no cubierto expresamente por esta decisión permanece propuesta/no aceptada.
