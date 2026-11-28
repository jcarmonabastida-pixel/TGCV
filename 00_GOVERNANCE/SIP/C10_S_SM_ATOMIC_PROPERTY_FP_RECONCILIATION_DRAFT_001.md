# C10-S — Reconciliación SM-01…SM-10, catálogo atómico y familias FP

**ID:** C10-S-SM-FP-RECON-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** RECONCILIACIÓN DOCUMENTAL PROPUESTA — NO APROBADA COMO CATÁLOGO CONFIRMATORIO.  
**Fuentes:** catálogo atómico CMP/PAR/REF/RUL/POL/MET; contrato FP-03; matriz F*; matriz abstracta C_src→C_dst/M; DEC-C10-052/053/054.

## 1. Hallazgo principal

La reconciliación revela una discrepancia real entre la primera matriz de mapping y el catálogo atómico: la matriz asignó algunas propiedades semánticas a FP-01/FP-02 como familia primaria, mientras que el catálogo las había descrito como FP-03. La solución no es elegir una familia única para una propiedad compuesta; es descomponer el criterio en predicados distintos según qué se está afirmando.

Regla de separación:
- **FP-01:** validez formal del esquema, tipos declarados, AST, cardinalidades estructurales y versiones/contratos de representación.
- **FP-02:** integridad estructural/relacional de referencias, extremos y multiplicidades.
- **FP-03:** preservación del significado funcional entre origen y destino bajo mapping.
- **FP-04:** compatibilidad con entorno/versión destino.
- **FP-05:** cumplimiento de seguridad; no inferible de preservar fielmente POL.
- **FP-06:** aplicación efectiva del paquete.
- **FP-07:** verificación post-aplicación contra el contrato; no reemplaza FP-01…05.
- **FP-08:** procedencia, identidad de artefacto y reproducibilidad.

La misma evidencia puede informar varias familias, pero un mismo fallo no se contará dos veces en el agregado confirmatorio: se identifica un predicado primario y los vínculos secundarios/dependencias.

## 2. Matriz de reconciliación SM → propiedades → FP

| Dimensión | Propiedades del catálogo | Predicado primario propuesto | Familia secundaria / frontera | Aplicabilidad |
|---|---|---|---|---|
| SM-01 identidad/significado | CMP-01, CMP-02, PAR-01 | SEM-CMP-IDENTITY; SEM-PAR-KEY-MEANING | FP-01 cobertura de entidades/claves; FP-08 identidad de artefacto ≠ funcional | Constitutiva, pero obligatoriedad por instancia |
| SM-02 valores/tipos/dominios | PAR-02, PAR-03, PAR-04 | SEM-PAR-VALUE-DOMAIN | FP-01 TYPE/DOMAIN-SCHEMA; FP-04 soporte del destino | PAR-02/03 constitutivas; PAR-04 condicional a unidad/escala |
| SM-03 relaciones/referencias | REF-01, REF-02, REF-04, REF-05 | SEM-REF-MEANING | FP-02 endpoint/integridad; FP-04 dependencia disponible; C_dep separado | Constitutiva para referencias declaradas; instalación es entorno |
| SM-04 ausencia/null/default | PAR-05, PAR-06 | SEM-PAR-STATE-SEMANTICS | FP-01 estado permitido/cardinalidad | Constitutiva; diferencias significativas fijadas ex ante |
| SM-05 cardinalidad/multiplicidad | CMP-03, REF-03 | STRUCT-CARDINALITY / REL-MULTIPLICITY | FP-03 solo si altera identidad/función | Condicional a colecciones/relaciones |
| SM-06 orden/precedencia | RUL-04 | SEM-RULE-PRECEDENCE | FP-01 AST/representación; FP-02 orden relacional si estructural | Condicional a orden funcional |
| SM-07 reglas operativas | RUL-01, RUL-02, RUL-03, RUL-04 | SEM-RULE-LOGIC-SCOPE-EFFECT | FP-01 AST válido; FP-02 referencias de operandos | Condicional a presencia de reglas; en DGP base reglas constitutivas |
| SM-08 tiempo/vigencia | RUL-05 | SEM-RULE-TEMPORAL | FP-01 tipo/forma temporal; FP-04 reloj/runtime | Condicional a semántica temporal |
| SM-09 permisos/control | POL-01, POL-02, POL-03, POL-04 | SEM-POLICY-DECLARED-SEMANTICS | FP-05 seguridad efectiva; FP-04/entorno permisos efectivos | Condicional; POL fuera del núcleo confirmatorio por DEC-C10-053 |
| SM-10 extensiones desconocidas | MET-03 | SEM-UNKNOWN-EXTENSION-HANDLING | FP-01 esquema/versión; FP-08 procedencia | Condicional a extensibilidad; requiere política ex ante |

La etiqueta “constitutiva” no declara automáticamente cada fila obligatoria ni fija NA. El contrato de instancia deberá declarar aplicabilidad y obligatoriedad antes de observar Outcome/Value.

## 3. Matriz atómica → predicado primario y doble conteo

| ID atómico | Predicado primario | Familia | Tratamiento de doble conteo / frontera |
|---|---|---|---|
| CMP-01 | SEM-CMP-IDENTITY | FP-03 | FP-01 solo comprueba presencia/forma del componente |
| CMP-02 | SEM-CMP-CLASS | FP-03 | FP-01 valida tipo estructural; no su significado |
| CMP-03 | STRUCT-CMP-CARDINALITY | FP-01/02 (según contrato) | FP-03 solo si duplicación/omisión cambia significado funcional; no contar de nuevo el mismo fallo |
| PAR-01 | SEM-PAR-KEY-MEANING | FP-03 | MAP-PAR-KEY-COVERAGE es control de cobertura FP-01, no equivalencia semántica |
| PAR-02 | TYPE-SCHEMA-CONFORMANCE + SEM-PAR-TYPE | FP-01 primario para validez formal; FP-03 separado para equivalencia de significado | Igualdad de etiquetas de tipo no prueba equivalencia funcional |
| PAR-03 | SEM-PAR-VALUE-DOMAIN | FP-03 | FP-01 valida dominio/rango declarado, no preservación del valor |
| PAR-04 | SEM-PAR-UNIT-SCALE | FP-03 | FP-01 valida representación numérica; no contar redondeo funcional dos veces |
| PAR-05 | SEM-PAR-STATE | FP-03 | FP-01 comprueba estado permitido; FP-03 si la distinción significativa se preserva |
| PAR-06 | STRUCT-PAR-REQUIREDNESS / SEM-PAR-OPTIONALITY | FP-01 para esquema; FP-03 para cambio de significado contractual | Dos predicados distintos, no duplicar el mismo incumplimiento |
| REF-01 | SEM-REF-ENDPOINT-MEANING | FP-03 | FP-02 valida que el extremo resuelva y sea íntegro |
| REF-02 | SEM-REF-ROLE-DIRECTION | FP-03 | FP-02 solo valida forma/dirección de arista si el contrato lo requiere |
| REF-03 | REL-REF-MULTIPLICITY | FP-02 | FP-03 secundario solo si la multiplicidad cambia la función |
| REF-04 | REL-REF-INTEGRITY | FP-02 | FP-07 observa estado aplicado; no duplicar fallo de integridad |
| REF-05 | SEM-DECLARED-DEPENDENCY | FP-03 | Disponibilidad/instalación real es C_dep/FP-04, nunca se infiere de la declaración |
| RUL-01 | SEM-RULE-LOGIC | FP-03 | FP-01 valida AST tipado/acíclico/límites 4/16/16 |
| RUL-02 | SEM-RULE-SCOPE | FP-03 | FP-01 valida estructura/identificadores del ámbito |
| RUL-03 | SEM-RULE-EFFECT | FP-03 | Efectos permitidos REQUIRE/FORBID fijados por DEC-C10-054 |
| RUL-04 | SEM-RULE-PRECEDENCE | FP-03 | Solo aplicable si orden afecta resultado; sintaxis en FP-01 |
| RUL-05 | SEM-RULE-TEMPORAL | FP-03 | Representación válida FP-01; ejecución/reloj destino FP-04 |
| POL-01 | SEM-POLICY-ROLE | FP-03 (condicional) | POL fuera del núcleo base; no inferir rol efectivo |
| POL-02 | SEM-POLICY-SCOPE | FP-03 (condicional) | Permiso efectivo/entorno fuera de FP-03 |
| POL-03 | SEM-POLICY-ALLOW-DENY | FP-03 (condicional) | FP-05 evalúa seguridad, no equivalencia |
| POL-04 | DECLARED-VS-EFFECTIVE-SEPARATION | FP-03 como frontera interpretativa | No es un resultado de seguridad; permiso efectivo pertenece a entorno/FP-05 |
| POL-05 | SECURITY-COMPLIANCE | FP-05 | Excluir del agregado FP-03 |
| MET-01 | CONTRACT-VERSION-VALIDITY | FP-01/04 | FP-01 validez del contrato; FP-04 compatibilidad destino |
| MET-02 | PROVENANCE-TRACEABILITY | FP-08 | No es preservación funcional FP-03 |
| MET-03 | SEM-UNKNOWN-EXTENSION | FP-03 (condicional) | FP-01 reconoce versión/esquema; FP-08 registra evidencia/procedencia |
| MET-04 | ARTIFACT-VS-FUNCTIONAL-IDENTITY | FP-08 | Hash/nombre no prueba identidad semántica; FP-03 adjudica equivalencia funcional |

La asignación dual de PAR-02, PAR-06 y CMP-03 se resuelve mediante predicados separados: estructura/esquema frente a significado funcional. No se duplicará una misma observación como dos fallos si ambos predicados dependen de la misma condición subyacente; se reportará una causa primaria y el predicado secundario como diagnóstico.

## 4. Correcciones a la matriz abstracta C_src→C_dst/M

La primera matriz se conserva como propuesta de mapping, pero necesita estas precisiones:
1. CMP-01/02 son principalmente FP-03; FP-01 solo cubre presencia y forma.
2. PAR-02 debe separarse en validez formal FP-01 y preservación semántica FP-03.
3. REF-01/02 semánticos FP-03; REF-04 integridad FP-02; REF-03 multiplicidad FP-02 con impacto FP-03 solo si funcional.
4. RUL-01…05 son semánticos FP-03, mientras RULE-AST-WELLFORMED es FP-01.
5. POL-01…04 solo módulo condicional FP-03; POL-05 seguridad FP-05.
6. MET-01 versión/esquema FP-01/FP-04; MET-02/04 FP-08; MET-03 condicional FP-03.
7. APPLIED-STATE-SEMANTICS no debe tratarse como predicado semántico atómico adicional: FP-06 acredita aplicación; FP-07 observa post-aplicación; las propiedades FP-01…05 se evalúan sobre C_dst^applied. Evita contar el mismo fallo semántico una segunda vez por ser observado post-aplicación.
8. MAP-CMP-COVERAGE y MAP-PAR-KEY-COVERAGE son cobertura estructural FP-01; no sustituyen CMP-01/PAR-01 semánticos FP-03.

## 5. Perfil de aplicabilidad del DGP base según DEC-C10-053

- Constitutivos del objeto: CMP, PAR, REF y RUL. Esto no significa que cada subpropiedad condicional (unidad, cardinalidad, precedencia, tiempo) esté presente u obligatoria en toda instancia.
- POL: fuera del núcleo confirmatorio mínimo; módulo/escenario condicional. Su ausencia debe declararse ex ante.
- MET: identidad contractual, versión y procedencia obligatorias para trazabilidad; MET-03 extensiones desconocidas condicional a que existan extensiones/formato extensible; MET-04 regla de interpretación.
- E_dst, C_dep, permisos efectivos, recursos, runtime y estado aplicado no se incorporan como propiedades internas del paquete migrado. Se registran como condiciones/mediciones externas y etapas FP-04/05/06/07.

## 6. Predicados agregados y regla de adjudicación

No se recomienda sumar puntuaciones. Para cada familia y propiedad:
- 1 = conformidad confirmada con evidencia/cobertura suficiente;
- 0 = incumplimiento confirmado;
- ? = evidencia, mapping o cobertura insuficientes;
- NA = no aplicabilidad declarada y justificada ex ante.

FP-03=0 si alguna propiedad semántica obligatoria aplicable falla; FP-03=? si no hay fallo confirmado y alguna obligatoria no puede adjudicarse; FP-03=1 solo si todas las obligatorias aplicables son 1. F* integra FP-01…FP-08 conforme a su matriz y conserva perfiles por propiedad; no compensa fallos.

Un defecto formal puede impedir evaluar semántica y conducir a FP-03=? (no automáticamente FP-03=0), salvo que la pérdida funcional se demuestre. La causa formal se registra primariamente en FP-01/02.

## 7. Cuestiones abiertas tras reconciliación

1. Revisar y aceptar esta asignación de predicados primarios/secundarios.
2. Resolver obligatoriedad/NA de cada propiedad constitutiva dentro de un contrato de instancia abstracto.
3. Definir cardinalidades y roles de CMP/REF, sin valores arbitrarios.
4. Concretar claves abstractas de parámetros y dominios por clave.
5. Cerrar mapping y conversión de valores/estados.
6. Delimitar las reglas y predicados RUL que realmente existen en el paquete mínimo.
7. Determinar si extensiones desconocidas son parte del formato de escenario o quedan fuera.
8. Definir C_dst^applied y su evidencia/sello.
9. Reconciliar los predicados de F1/F2/A1/A2 con el mismo F* y oráculo.
10. Definir doble evaluación, cegamiento, cobertura y error del oráculo.

## 8. Dictamen

La reconciliación identifica y corrige solapamientos de familia. Separa semántica de estructura, integridad, compatibilidad, seguridad, aplicación y procedencia. No declara predicados confirmatorios ni obligatoriedad final, y no convierte el catálogo candidato en un inventario de propiedades presentes.

**Estado:** RECONCILIACIÓN DOCUMENTAL PROPUESTA; DEC-C10-052/053/054 vigentes; mapping inicial requiere las precisiones §4; obligatoriedad/NA ABIERTAS; F1/F2/A1/A2 y oráculo ABIERTOS; no validación técnica, revisión independiente, evidencia empírica ni ejecución.


## 9. Estado decisional — DEC-C10-055 (2026-11-05)

**ACEPTADA POR EL USUARIO** la arquitectura de reconciliación SM-01…SM-10 ↔ CMP/PAR/REF/RUL/POL/MET ↔ FP-01…FP-08. La aceptación cubre la separación de responsabilidades, predicados primarios/secundarios y regla anti-doble-conteo. No convierte las propiedades candidatas en requisitos confirmatorios ni cierra obligatoriedad/NA por instancia. La operacionalización de esa dimensión se desarrolla en `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`.
