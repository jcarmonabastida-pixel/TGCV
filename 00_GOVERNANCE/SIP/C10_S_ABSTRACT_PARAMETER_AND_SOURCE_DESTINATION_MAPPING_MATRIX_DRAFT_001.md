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


## 12. Estado de reconciliación y aplicabilidad

La arquitectura SM/FP de esta matriz ha sido aceptada por DEC-C10-055. Los predicados de mapping se interpretan conforme a la reconciliación aceptada; la obligatoriedad/NA por instancia no queda resuelta por dicha aceptación y se desarrolla en `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`. La asignación de O/C/NA requiere IAM sellado ex ante, cobertura y cardinalidad declarada.



## 13. Crosswalk M con contrato abstracto y transformaciones Opción A (2026-11-06)

M es un artefacto versionado de evaluación, no una capa semántica persistida. Su dominio es C_src→S2→C_dst declarado→C_dst aplicado para F1/F2 y C_src→S1→C_dst declarado→C_dst aplicado para A1/A2. S1/S2 no prueban aplicación ni conformidad F*.

| Familia | Identidad mínima enlazada | Transformación y prueba |
|---|---|---|
| CMP | component_id/key, clase/rol, scope y cardinalidad | Correspondencia inequívoca o composición explícita; cobertura, identidad funcional y duplicación |
| PAR | key, owner, type, state, value/domain, unit, requiredness, default | Conversión tipada; conservar semántica de estado/valor y registrar pérdida/redondeo |
| REF | ref_id, extremos internos/externos, relation_type, direction, role, multiplicity | Mapear ambos extremos y comprobar integridad/dirección/rol/cardinalidad |
| RUL | rule_id, scope, AST, efecto y versión de gramática | Equivalencia declarativa de operadores, operandos, ámbito, efecto y UNKNOWN |
| POL | policy_id/scope/roles/rules, solo si se activa | Preservar política declarada; permisos efectivos/seguridad en E_dst/FP-05 |
| MET | IDs/versiones contractuales, provenance, IAM y oráculo | Identidad/procedencia; hash identifica artefacto, no equivalencia funcional |

### 13.1. Estados de mapping

MAPPED exige correspondencia tipada y evidencia suficiente; UNMAPPED es fallo solo si la pérdida/omisión obligatoria está demostrada; AMBIGUOUS produce ? salvo composición explícita adjudicable; NOT_APPLICABLE requiere IAM pre-Z/B y justificación. Conversión no especificada no se presume válida.

### 13.2. DEFAULT y conversiones

La matriz abstracta usa ABSENT/NULL/DEFAULT/VALUE, mientras M distingue subclases DEFAULT. Propuesta no congelada: DECLARED/INHERITED como metadatos de DEFAULT; ENV_RESOLVED como observación de E_dst. La propuesta no está aprobada; casos semánticamente sensibles quedan ?. Requiere armonizar contrato, catálogo PAR, gramática y predicados FP.

BOOL exige tabla explícita si cambia tipo; INT no admite overflow; DECIMAL declara escala/precisión/redondeo; ENUM mapping completo para valores obligatorios; STRING normalización explícita; REF correspondencia de extremos. Límites concretos abiertos.

### 13.3. M común a F1/F2 y A1/A2

M puede describir submappings por etapa, pero ambas rutas deben satisfacer mismo contrato de entrada/destino, IAM, C0/G/H y F*. F1 PASS no demuestra F2; S2 no es destino aplicado. A1/A2 no es alternativa funcional por alcanzar estado nominal: requiere mismo F* y evidencia de no-afectación por B. FP-01…07 sin compensación; FP-08 gate separado.

**Pendiente:** mappings completos por instancia, reglas many-to-one/one-to-many, conversiones/pérdidas, defaults, C_dst aplicado, IAM y oráculo. No instancias ni fixtures.


## 14. Reconciliación normativa de DEFAULT con DEC-C10-054

La matriz y el perfil de dominios se armonizan con el contrato abstracto mediante una representación discriminada, no mediante colapso:

| Plano | Representación | Ubicación |
|---|---|---|
| Estado de parámetro | ABSENT / NULL / DEFAULT / VALUE | PAR en C_src/C_dst |
| Tipo de default contractual | DECLARED / INHERITED, obligatorio cuando state=DEFAULT | Metadato contractual PAR/default_contract |
| Resolución ambiental | Valor efectivamente resuelto, si existe | Snapshot E_dst; fuera de C_src/C_dst |

\`DEFAULT_DECLARED\` y \`DEFAULT_INHERITED\` son abreviaturas de (state=DEFAULT, default_kind=DECLARED|INHERITED). \`DEFAULT_ENV_RESOLVED\` identifica una observación ambiental y no un tercer default_kind del paquete.

El mapping evalúa por separado origen, regla/ámbito de herencia, valor contractual y valor resuelto en entorno. La resolución ambiental se enlaza a parameter_key y versiones/snapshot; no se incorpora retroactivamente al paquete. Si la fuente no distingue declarado/heredado, el resultado es UNKNOWN salvo evidencia independiente. Snapshot ambiental ausente deja desconocida la resolución, no demuestra que no exista.

Esta lectura implementa DEC-C10-054 y el perfil §3; no añade decisión nueva. La tabla §4 se mantiene, precisando DEFAULT_ENV_RESOLVED como E_dst. La igualdad del valor resuelto no acredita preservación semántica del default.

**Precedencia interna:** La nota de §13.2 que dejaba toda la distinción DEFAULT como propuesta no congelada queda precisada por §14: la distinción conceptual procede de DEC-C10-054 aceptada; permanecen abiertos solo los detalles de instancia, snapshot, mapping y evidencia.


## 15. Mapping candidato para el roster PAR de servicio lógico

| Slot lógico | Tipo fuente/destino | Mapping permitido a explorar | Falsador semántico |
|---|---|---|---|
| PAR-SVC-ENABLED | BOOL→BOOL | Preservación exacta de estado y valor; cualquier conversión exige tabla explícita | true/false invertido, ABSENT/NULL colapsado o default no preservado |
| PAR-SVC-PROFILE | ENUM→ENUM | Tabla total y versionada para todos los símbolos obligatorios; no se presupone igualdad nominal | Dos símbolos funcionalmente distintos fusionados o símbolo sin correspondencia |
| PAR-SVC-RETRY-COUNT | INT→INT | Preservación exacta dentro de dominio finito; INT→DECIMAL solo si se justifica y es exacto | Overflow, truncamiento, signo alterado, cambio de límite o estado |

El roster no fija nombres físicos ni tablas de conversión concretas. Para DECIMAL/STRING/REF condicionales se exige mapping por clave y dominio; no se presume normalización, coerción ni equivalencia por igualdad textual. Cada ruta F1/F2 y A1/A2 usa el mismo contrato semántico y el mismo IAM. Los resultados locales de conversión no sustituyen C_dst_applied ni F*.

## 16. Mapping de reglas RUL entre rutas

El mapping RUL no consiste en copiar el texto/AST ni en conservar identificadores nominales. Debe preservar la semántica de condición, operandos, scope, efecto REQUIRE/FORBID y evaluación trivalente, con correspondencia de cada referencia PAR/CMP y su versión. F1 y A1 producen representaciones intermedias; F2 y A2 aplican la regla en destino bajo el mismo contrato funcional.

Falsadores mínimos: operador o negación alterados; operandos/clave intercambiados; scope ampliado/reducido; dominio ENUM cambiado; regla eliminada/duplicada; REQUIRE↔FORBID; UNKNOWN convertido en TRUE/FALSE; precedencia alterada cuando sea significativa; regla nominalmente preservada pero no aplicada. La equivalencia se adjudica con FP-03 y evidencia del destino aplicado; igualdad textual/AST no basta si mappings cambian significado.

La plantilla ENABLED→PROFILE aún carece de D_profile_enabled y fuente funcional, por lo que no hay mapping instanciable ni resultado esperado por ruta. No crear tabla concreta hasta cerrar esas entradas.

## 16. Mapping de reglas RUL entre rutas

El mapping RUL no consiste en copiar el texto/AST ni en conservar identificadores nominales. Debe preservar la semántica de condición, operandos, scope, efecto REQUIRE/FORBID y evaluación trivalente, con correspondencia de cada referencia PAR/CMP y su versión. F1 y A1 producen representaciones intermedias; F2 y A2 aplican la regla en destino bajo el mismo contrato funcional.

Falsadores mínimos: operador o negación alterados; operandos/clave intercambiados; scope ampliado/reducido; dominio ENUM cambiado; regla eliminada/duplicada; REQUIRE↔FORBID; UNKNOWN convertido en TRUE/FALSE; precedencia alterada cuando sea significativa; regla nominalmente preservada pero no aplicada. La equivalencia se adjudica con FP-03 y evidencia del destino aplicado; igualdad textual/AST no basta si mappings cambian significado.

La plantilla ENABLED→PROFILE aún carece de D_profile_enabled y fuente funcional, por lo que no hay mapping instanciable ni resultado esperado por ruta. No crear tabla concreta hasta cerrar esas entradas.

## 17. Mapping candidato del contrato sintético ENABLED/PROFILE/RUL

El mapping debe preservar la semántica de ENABLED y los tres símbolos de PROFILE, así como RUL-SVC-ENABLE-PROFILE-01, su owner/scope, versión y efecto REQUIRE. Las etiquetas físicas pueden diferir entre fuente/destino únicamente con tabla de correspondencia explícita hacia los mismos IDs semánticos. Deben probarse los dos perfiles permitidos y el violador DISABLED cuando ENABLED=true. Una conversión que cambie el conjunto permitido o la condición falla FP-03; una regla correcta no aplicada falla FP-06; falta de evidencia deja ?. No se fija aún ninguna tabla de mapping concreta.