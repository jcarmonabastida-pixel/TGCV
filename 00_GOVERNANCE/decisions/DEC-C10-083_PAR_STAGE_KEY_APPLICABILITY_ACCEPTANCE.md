# DEC-C10-083 — Aceptación de aplicabilidad PAR por stage_key

**Fecha:** 2026-11-08  
**Estado:** ACEPTADA  
**Ámbito:** C10-S — propiedades `PAR-SVC-ENABLED` y `PAR-SVC-PROFILE` del CMP focal.

## 1. Decisión

Se acepta la adjudicación documental de los dos parámetros P0 REQUIRED en las siete etapas `stage_key` de DEC-C10-071, según matriz de aplicabilidad §18.6 y crosswalk §10.9.

| stage_key | Posición | Obligación aceptada |
|---|---|---|
| `C_SRC` | Configuración fuente declarada | Ambos parámetros presentes como `VALUE` tipado |
| `F1_S2` | Intermedio F1 | Preservación semántica independiente por mapping versionado |
| `A1_S1` | Intermedio A1 | Preservación semántica independiente por mapping versionado |
| `F2_DST_DECL` | Configuración destino declarada F2 | Ambos presentes como `VALUE` tipado |
| `A2_DST_DECL` | Configuración destino declarada A2 | Ambos presentes como `VALUE` tipado |
| `F2_DST_APPLIED` | Estado aplicado F2 | Evidencia independiente del estado/valor realmente aplicado |
| `A2_DST_APPLIED` | Estado aplicado A2 | Evidencia independiente del estado/valor realmente aplicado |

La aceptación se limita a `PAR-SVC-ENABLED` (BOOL) y `PAR-SVC-PROFILE` (ENUM), conservando sus definiciones contractuales de DEC-C10-068. No reabre sus dominios, tipos ni la regla `RUL-SVC-ENABLE-PROFILE-01`.

## 2. Reglas transversales

1. Ambos parámetros son P0 REQUIRED en las siete etapas del contrato base; la obligatoriedad no demuestra que exista una observación ni que esté adjudicada.
2. No existe DEFAULT contractual aceptado. En posiciones declarativas, se espera estado `VALUE` tipado.
3. `ABSENT` y `NULL` no son admisibles para estos parámetros REQUIRED cuando la ausencia se demuestra mediante universo y cobertura suficientes. La ausencia de registro/evidencia por sí sola no prueba ABSENT.
4. F1 y A1 se evalúan independientemente; cualquier cambio de representación física requiere mapping explícito, total y versionado que preserve semántica, tipo, dominio, estado y valor conforme al contrato.
5. F2/A2 declarados no prueban aplicación. F2/A2 aplicados requieren evidencia del estado efectivo y snapshot exacto; no se infieren de declaraciones, paquetes preparados ni `DEFAULT_ENV_RESOLVED`.
6. Falta de snapshot, mapping, inspección o cobertura suficiente → `UNKNOWN` / `?`. Contradicción demostrada con evidencia suficiente → `FAIL` para el predicado predeclarado (o `0` en la representación Reach correspondiente). `NA` requiere no aplicabilidad ex ante y no se admite para estos dos parámetros en las siete etapas del contrato base.
7. Cada observación se vincula a CMP owner exacto, NODE anchor por snapshot conforme a DEC-C10-082, snapshot, `stage_key`, ruta/scope, `coverage_scope_id`, `parameter_key`, mapping/version y evidencia.
8. `E_dst/runtime` permanece fuera del vocabulario `stage_key`; evidencia ambiental/runtime no sustituye configuración declarativa P0.

## 3. Límites

Esta decisión acepta el contrato de aplicabilidad/adjudicación, no observaciones concretas. No asigna valores por escenario, no especifica conversiones físicas F1/A1/F2/A2, no adjudica preservación ya ejecutada, no completa cobertura por snapshot, no sella IAM ni aprueba mappings físicos.

No crea tablas/columnas/FK, fixtures, parser, validator ni código; no autoriza Design Freeze, implementación, validación técnica ni ejecución científica. No modifica TGCV Core, RMA, Evidence→Claim Matrix ni claims. `scientific_execution=false`; `execution_authorized=false`.

**Aprobación:** aceptación explícita del responsable científico en la conversación del 2026-11-08.
