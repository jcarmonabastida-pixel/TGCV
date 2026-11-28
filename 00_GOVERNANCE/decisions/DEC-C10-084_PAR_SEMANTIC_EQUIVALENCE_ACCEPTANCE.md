# DEC-C10-084 — Aceptación del contrato de equivalencia semántica de los PAR nucleares

**Fecha:** 2026-11-08  
**Estado:** ACEPTADA  
**Ámbito:** C10-S — equivalencia semántica y composición de mappings de `PAR-SVC-ENABLED` y `PAR-SVC-PROFILE`.

## 1. Decisión

Se acepta como contrato lógico documental la especificación de la matriz abstracta de mapping §15.1, referenciada desde el crosswalk IAM↔U_G §10.11, para los dos parámetros P0 aceptados en DEC-C10-068 y adjudicados por etapa en DEC-C10-083.

### 1.1. Separación de estado y valor

La equivalencia de estado se adjudica separadamente de la equivalencia de valor. Un valor coincidente no compensa estado, tipo, dominio u owner incorrectos. La ausencia de registro/evidencia no se recodifica como ABSENT. En las posiciones declarativas de las siete etapas se exige VALUE tipado; no existe DEFAULT contractual aceptado.

### 1.2. PAR-SVC-ENABLED — BOOL

Se acepta identidad semántica exacta en el dominio lógico `{false,true}`:
- `false → false`;
- `true → true`.

No se admite inversión de polaridad, colapso, coerción implícita, decodificación ambigua ni dependencia no declarada del entorno. Una representación física distinta solo es admisible mediante regla total, determinista y versionada que decodifique a exactamente uno de los dos valores lógicos.

### 1.3. PAR-SVC-PROFILE — ENUM

Se acepta una biyección total, inyectiva y versionada entre los tres significados lógicos `STANDARD`, `READ_ONLY` y `DISABLED`. La grafía física de origen y destino puede diferir, pero cada símbolo admisible debe resolverse explícitamente a un único significado y a su equivalente destino. No se admite mapping parcial, fusión de significados, expansión silenciosa del dominio ni conversión de valor desconocido a un valor conocido.

### 1.4. Regla constitutiva

Debe conservarse independientemente la regla `RUL-SVC-ENABLE-PROFILE-01`:
`ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}`,
con efecto `REQUIRE`, mismo scope de unidad lógica y sin inferir la implicación inversa. La equivalencia individual de los parámetros no prueba la preservación ni la aplicación de esta regla.

### 1.5. Composición por etapas y rutas

- `C_SRC → F1_S2` y `C_SRC → A1_S1` se adjudican independientemente.
- Cada salida intermedia se compara con la configuración declarada de destino de su propia ruta.
- `F2_DST_DECL → F2_DST_APPLIED` y `A2_DST_DECL → A2_DST_APPLIED` requieren evidencia independiente de aplicación efectiva.
- La comparación se realiza mediante composición explícita de mappings versionados. No se presume transitividad entre mappings incompatibles ni equivalencia por igualdad de literales físicos.

## 2. Adjudicación

- `PASS`: estado y valor semántico conformes, con owner, snapshot, mapping exactos y evidencia/cobertura suficientes.
- `FAIL`: contradicción demostrada, incluyendo inversión BOOL, pérdida/fusión ENUM, estado indebido, alteración de regla o valor semántico distinto.
- `UNKNOWN`: evidencia, cobertura, owner, snapshot, mapping o decodificación insuficientes.
- `NOT_COMPARABLE`: identidades/versiones incompatibles sin mapping aprobado.
- `NA`: solo no aplicabilidad ex ante; no se deriva de falta de datos y no se admite para estos dos PAR en las siete etapas del contrato base.

## 3. Límites

La aceptación no fija codificaciones físicas, nombres de campo, tablas de conversión, valores por escenario, tolerancias, oráculo ni mediciones. No adjudica mappings ni resultados observados de F1/A1/F2/A2; no completa mappings físicos ni sella IAM.

No crea registros, tablas, columnas, FK, fixtures, parser, validator ni código; no autoriza Design Freeze, implementación, validación técnica ni ejecución científica. No modifica TGCV Core, RMA, Evidence→Claim Matrix ni claims. `scientific_execution=false`; `execution_authorized=false`.

**Aprobación:** aceptación explícita del responsable científico en la conversación del 2026-11-08.
