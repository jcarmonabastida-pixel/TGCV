# DEC-C10-087 — Aceptación de aplicación efectiva y verificación post-aplicación F/A

**Fecha:** 2026-11-08  
**Estado:** ACCEPTED — DOCUMENTAL  
**Ámbito:** C10-S, rama `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta el contrato documental de la matriz abstracta §15.7 y del crosswalk IAM §10.17 para las transiciones independientes:

- F: `F2_DST_DECL → F2_DST_APPLIED`.
- A: `A2_DST_DECL → A2_DST_APPLIED`.

Se reutilizan exclusivamente las familias FP-06, FP-07 y FP-08 ya definidas en la reconciliación SM/FP vigente. No se crean familias ni predicados confirmatorios paralelos.

## 2. Funciones no intercambiables

- **FP-06 — aplicación efectiva:** acredita que el paquete/configuración declarada exacta fue objeto de una operación de aplicación identificable sobre el destino previsto, con evidencia trazable del evento, artefacto, versión/hash/provenance, target/environment identity, alcance y resultado. Intención, plan, comando preparado, existencia del artefacto, declaración no trazable o exit code aislado no bastan.
- **FP-07 — verificación post-aplicación:** acredita mediante observación/captura del destino y snapshot exactos que el estado realmente observado satisface el contrato, con cobertura suficiente. Se aplican FP-01…05 según propiedad: validez formal, integridad relacional, preservación funcional, compatibilidad ambiental y seguridad. FP-07 no los reemplaza.
- **FP-08 — procedencia, identidad y reproducibilidad:** asegura identificación, versionado, integridad y trazabilidad del paquete, evento, destino, snapshot y evidencia. Soporta FP-06/07, pero no sustituye ni la evidencia del evento ni la observación del estado.

La misma evidencia puede informar más de una familia cuando corresponda; cada afirmación conserva su predicado primario y vínculos secundarios. Un mismo defecto no se contabiliza dos veces en el agregado confirmatorio.

## 3. Unidad y reglas sustantivas

F y A se adjudican independientemente, por ruta, parámetro/regla y familia. Se fijan contrato/instancia y versiones, CMP owner/NODE anchor, artefacto declarado y registro exactos, evento, destino/environment, snapshot post-aplicación y registro, stage_key, ruta/scope, mapping/versiones y evidencia.

En el contrato base:
- Los dos PAR nucleares se observan como VALUE; ENABLED exige BOOL exacto y PROFILE la biyección ENUM total/versionada sobre STANDARD/READ_ONLY/DISABLED conforme a DEC-C10-084.
- `RUL-SVC-ENABLE-PROFILE-01` conserva identidad y semántica REQUIRE, operandos y scope; la preservación declarativa no demuestra evaluación efectiva.
- FP-04 y FP-05 permanecen diferenciadas: conformidad de configuración no demuestra compatibilidad ambiental ni seguridad.

FP-06 PASS no implica FP-07 PASS. FP-07 PASS no reconstruye por sí solo la procedencia ni qué operación aplicó el paquete.

## 4. Adjudicación

- `PASS`: la afirmación concreta de aplicación o conformidad post-aplicación está demostrada con identidad, mapping, cobertura y evidencia suficientes.
- `FAIL`: no aplicación/aplicación a destino equivocado demostrada con evidencia autoritativa y cobertura exhaustiva, o estado observado que contradice propiedad obligatoria.
- `UNKNOWN`: falta evento, destino, snapshot, observación, cobertura, mapping, oráculo o evidencia suficiente.
- `NOT_COMPARABLE`: incompatibilidad de versiones/namespaces sin mapping aprobado.
- `NA`: inaplicabilidad ex ante justificada; no admisible para FP-06/FP-07 ni los PAR/RUL del contrato base en ambas rutas.

La ausencia de registro no demuestra no aplicación. FAIL por no aplicación requiere registro autoritativo y exhaustivo del universo de operaciones/target o evidencia positiva de contradicción; de lo contrario UNKNOWN. Un log o exit code sin observación independiente del estado no permite FP-07 PASS.

Se reportan por separado FP06_APPLY, FP07_POSTCHECK, validez probatoria FP-08 y vector FP-01…05 aplicable. Cualquier FAIL obligatorio permanece visible; en ausencia de FAIL, UNKNOWN impide conformidad global PASS. La cobertura se informa separadamente del estado semántico.

## 5. Límites y no autorizaciones

Decisión documental. No selecciona herramienta/comando, protocolo de observación, oráculo, tolerancias, método de captura, runtime ni mapping físico. No crea observaciones, fixtures, columnas/FK o predicados FP nuevos. No sella IAM ni autoriza parser, validator, scripts, implementación, Design Freeze, validación técnica, ejecución del control ni experimento científico.

`scientific_execution=false`; `execution_authorized=false`.
