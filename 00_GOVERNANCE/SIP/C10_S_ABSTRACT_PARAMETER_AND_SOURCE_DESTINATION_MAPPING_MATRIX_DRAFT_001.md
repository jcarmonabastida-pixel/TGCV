# C10-S — Matriz abstracta de parámetros y correspondencias fuente/destino

**ID:** C10-S-MAPPING-MATRIX-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA DOCUMENTAL — NO APROBADA / NO CONGELADA / NO IMPLEMENTADA.  
**Base decisional:** DEC-C10-052, DEC-C10-053 y DEC-C10-054.  
**Dependencias:** catálogo atómico CMP/PAR/REF/RUL/POL/MET; FP-01, FP-02, FP-03; contrato DGP temporal y de roles; perfil de dominios finitos.

## 1. Propósito y límites

Esta matriz convierte el perfil aprobado en una estructura de mapping abstracto entre paquete fuente C_src, paquete destino C_dst y relación de correspondencia M. No selecciona una tecnología, formato, producto, parámetro real, valor, dependencia, entorno o transformación concreta.

M es un artefacto de evaluación/versionado para comparar origen y destino; no constituye una capa semántica persistida adicional del sistema. El destino evaluado es el estado realmente aplicado, no solo el fichero/paquete preparado.

## 2. Contrato mínimo por clave de parámetro

Cada clave abstracta de parámetro deberá declarar antes de generar cualquier escenario:

| Campo | Obligación |
|---|---|
| parameter_key | Identificador estable dentro del ámbito del componente |
| component_key | Componente al que pertenece |
| type | BOOL / INT / DECIMAL / ENUM / STRING / REF |
| value_domain | Dominio finito o límites cerrados y escala |
| unit | Unidad/dimensión o NA justificado |
| allowed_states | Subconjunto explícito de ABSENT/NULL/DEFAULT/VALUE |
| requiredness | REQUIRED / OPTIONAL / CONDITIONAL |
| default_contract | Tipo/origen del default, si aplica |
| normalization | IDENTICAL por defecto; regla explícita si distinta |
| conversion_policy | Tabla/regla tipada de conversión o NONE |
| source_version / target_version | Versiones contractuales aplicables |
| evidence_requirement | Evidencia necesaria para adjudicar el predicado |
| mapping_status | MAPPED / UNMAPPED / AMBIGUOUS / NOT_APPLICABLE |

Los valores concretos y dominios se fijarán por clave después de seleccionar el contrato abstracto de servicio y antes de definir/generar casos. No se rellenan aquí.

## 3. Matriz de mapping por familia

| Familia | Correspondencia mínima en M | FP primario | FP secundario | Criterio de conformidad |
|---|---|---|---|---|
| CMP — componente | component_key_src → component_key_dst; identidad/clase funcional y cardinalidad | FP-01 | FP-03 | componente requerido representado y tipo/clase contractual preservados |
| PAR — parámetro | clave, tipo, dominio, unidad, allowed_states, requiredness, default y valor/estado | FP-01 | FP-03 | esquema/tipo válido y semántica de valor/estado preservada |
| REF — referencia | reference_key, source_endpoint, target_endpoint, direction, multiplicity, integrity_rule | FP-02 | FP-01/03 | extremos corresponden y cardinalidad/integridad se conserva |
| RUL — regla | rule_key, scope, typed_AST, operators, operands, precedence, effect, validity | FP-03 | FP-01/02 | expresión y significado contractual preservados bajo gramática aprobada |
| POL — política | policy_key, scope, declared roles/rules/effects | FP-03 (condicional) | FP-01/02/FP-05 | solo escenarios secundarios; preservación declarada no prueba seguridad efectiva |
| MET — metadatos | identity, contract_version, provenance, extension_policy | FP-01 (trazabilidad) | FP-03 | identidad/versionado/procedencia íntegros; extensión desconocida tratada según contrato |

La asignación primaria evita contar una misma discrepancia como varios fallos confirmatorios independientes. La evidencia puede apoyar predicados secundarios, pero la tabla de resultados deberá declarar el predicado primario y las dependencias.

## 4. Mapping de estados de parámetro

| Estado fuente | Correspondencia por defecto | Condición para equivalencia |
|---|---|---|
| ABSENT | ABSENT | misma ausencia bajo contrato |
| NULL | NULL | null explícito preservado; no equivale a ausencia |
| DEFAULT_DECLARED | DEFAULT_DECLARED | misma declaración o equivalencia contractual demostrada |
| DEFAULT_INHERITED | DEFAULT_INHERITED | misma regla de herencia y ámbito |
| DEFAULT_ENV_RESOLVED | estado de entorno fuera de C_src/C_dst | evaluar como condición externa/snapshot; no colapsar en default del paquete |
| VALUE | VALUE | valor equivalente bajo tipo, unidad, dominio y conversión declarada |

No hay equivalencia automática entre ABSENT, NULL, DEFAULT y VALUE. Una conversión admitida debe especificar función, dominio, codominio, pérdida permitida, redondeo y evidencia. La conversión no puede redefinir F*.

## 5. Reglas de conversión por tipo

- BOOL: igualdad exacta; conversión desde otros tipos solo con tabla explícita y completa.
- INT: enteros en intervalo/conjunto declarado; overflow fuera del dominio es fallo estructural.
- DECIMAL: escala fija por clave; conversión exacta o redondeo contractual explícito. Sin float binario implícito.
- ENUM: correspondencia completa para valores obligatorios; valor sin mapping es fallo si se demuestra pérdida, UNKNOWN si no se puede adjudicar.
- STRING: comparar según regla de normalización versionada; no aplicar trim/case-fold/Unicode normalization tácitamente.
- REF: mapear extremos por identidad contractual y comprobar integridad; conservar texto del identificador no basta.

## 6. Predicados atómicos candidatos

### FP-01 — estructura y tipos
- MAP-CMP-COVERAGE: cobertura de componentes obligatorios.
- MAP-PAR-KEY-COVERAGE: cobertura de claves obligatorias.
- PAR-TYPE-COMPAT: compatibilidad de tipos y dominios.
- PAR-STATE-VALID: estado de parámetro permitido por contrato.
- RULE-AST-WELLFORMED: AST acíclico, tipado y dentro de 4/16/16.
- MET-IDENTITY-VERSION: metadatos obligatorios completos y coherentes.

### FP-02 — integridad relacional
- REF-ENDPOINT-MAP: correspondencia de ambos extremos.
- REF-DIRECTION: dirección preservada.
- REF-MULTIPLICITY: multiplicidad preservada.
- REF-INTEGRITY: referencia resuelta dentro del universo permitido.
- COMPONENT-RELATION-CONSISTENCY: integridad de relaciones componentes/referencias.

### FP-03 — preservación semántica
- PAR-VALUE-SEMANTICS: valor preservado bajo tipo/unidad/conversión.
- PAR-STATE-SEMANTICS: ABSENT/NULL/DEFAULT/VALUE no colapsados.
- RULE-LOGIC-SEMANTICS: ámbito, operadores, operandos, precedencia y efecto preservados.
- DEFAULT-SEMANTICS: origen y resolución del default preservados según contrato.
- APPLIED-STATE-SEMANTICS: el estado aplicado en destino satisface los predicados anteriores, no solo el paquete preparado.

Estos identificadores son candidatos para reconciliación con los predicados ya existentes. No se consideran nuevos predicados confirmatorios aceptados hasta revisar duplicidad con el catálogo atómico y FP-01/02/03.

## 7. Lógica de adjudicación

Para cada predicado obligatorio:
- 1: conformidad confirmada con evidencia suficiente y mapping definido;
- 0: incumplimiento o pérdida confirmados;
- ?: evidencia insuficiente, mapping ambiguo/incompleto o cobertura no suficiente;
- NA: propiedad fuera de alcance con justificación ex ante.

Para F*:
- F*=0 si al menos un predicado obligatorio falla de forma confirmada;
- F*=? si no hay fallo confirmado pero al menos uno obligatorio es ?;
- F*=1 si todos los predicados obligatorios aplicables son 1.

La lógica de F* no reemplaza el estado de cobertura ni la adjudicación independiente. La falta de mapping no se convierte automáticamente en 0: depende de si existe pérdida demostrada o indeterminación.

## 8. Origen, destino y estado aplicado

Se distinguen:
1. C_src: contrato/paquete de origen congelado.
2. C_dst^decl: contrato/paquete destino declarado/preparado.
3. C_dst^applied: configuración realmente aplicada en destino.
4. E_dst: estado del entorno destino (dependencias, permisos efectivos, recursos, runtime), externo al objeto migrado.
5. M: mapping versionado de evaluación.

FP-01/02/03 comparan C_src con C_dst^applied mediante M. C_dst^decl no sustituye C_dst^applied. E_dst informa FP-05/compatibilidad/condiciones de ejecución, pero no se incorpora silenciosamente al objeto de configuración.

## 9. Cuestiones abiertas antes del contrato confirmatorio

1. Reconciliar predicados candidatos con SM-01…SM-10 y el catálogo atómico para evitar duplicidades.
2. Determinar obligatoriedad/NA por propiedad, sin elegir valores posteriores a Outcome.
3. Definir claves abstractas y dominios por clave, con justificación y cobertura.
4. Resolver cardinalidad y direccionalidad de CMP/REF.
5. Especificar tablas de conversión permitidas y tolerancias.
6. Definir cómo se observa y sella C_dst^applied.
7. Resolver conflictos entre reglas y errores de evaluación.
8. Fijar evidencia, cobertura, doble evaluación, cegamiento y adjudicación.
9. Reconciliar F1/F2/A1/A2 y el oráculo funcional F*.
10. Comprobar separación FP-05: permisos efectivos y seguridad no se infieren de preservar POL.

## 10. Dictamen

Matriz abstracta creada como puente documental entre DEC-C10-054 y la especialización de FP-01/02/03. No cierra el contrato de configuración ni el DGP. No contiene valores concretos, truth, fixtures, resultados o evidencia empírica.

**Estado:** DEC-C10-052/053/054 aprobadas en sus alcances; perfil estructural aprobado; matriz de mapping PROPUESTA; dominios concretos por clave ABIERTOS; predicados por reconciliar; C_dst^applied/oráculo NO CERRADOS; validación técnica NO REALIZADA; revisión independiente NO REALIZADA; ejecución NO AUTORIZADA.


## 11. Reconciliación de familias y predicados

La asignación inicial de §3 y §6 debe interpretarse con la reconciliación posterior `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`. En particular, CMP-01/02 y PAR-01 tienen primacía semántica FP-03; PAR-02 se desdobla en esquema FP-01 y significado FP-03; REF-01/02 son FP-03 y REF-04 FP-02; RUL semántica FP-03 y AST FP-01; POL condicional FP-03, seguridad FP-05; MET-01 FP-01/04, MET-02/04 FP-08, MET-03 condicional FP-03. La cobertura MAP-CMP/PAR es FP-01, no sustituto de equivalencia semántica.

APPLIED-STATE-SEMANTICS se descompone: FP-06 verifica aplicación, FP-07 observa el estado aplicado y las familias FP-01…05 evalúan las propiedades correspondientes sobre ese estado. No se contará un mismo defecto semántico dos veces.
