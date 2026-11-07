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

El mapping preserva la semántica de condición, operandos, scope, efecto REQUIRE/FORBID y evaluación trivalente, con correspondencia de cada referencia PAR/CMP y versión. F1/A1 producen representaciones intermedias; F2/A2 aplican la regla en destino bajo el mismo contrato funcional.

Para la instancia sintética aceptada conceptualmente por DEC-C10-068, RUL-SVC-ENABLE-PROFILE-01:
- PAR-SVC-ENABLED conserva BOOL y sus estados; ABSENT/NULL/DEFAULT se mantienen diferenciados conforme al contrato de parámetros.
- PAR-SVC-PROFILE conserva el dominio semántico {STANDARD, READ_ONLY, DISABLED}. La correspondencia física puede renombrar símbolos, pero debe ser total, inyectiva respecto de los tres significados y versionada.
- La regla conserva ENABLED=true implica PROFILE∈{STANDARD, READ_ONLY}, scope de la unidad lógica y efecto REQUIRE.
- ENABLED=true con STANDARD/READ_ONLY sigue satisfaciendo; ENABLED=true con DISABLED sigue violando. ENABLED=false no queda restringido por esta implicación.
- UNKNOWN no puede colapsarse en TRUE/FALSE.

Falsadores: operador/negación alterados; clave/operando intercambiado; scope alterado; dominio ENUM incompleto, fusionado o ampliado; regla eliminada/duplicada; REQUIRE↔FORBID; UNKNOWN convertido en booleano; regla no aplicada en destino; mapping nominalmente igual pero semánticamente divergente.

No se fijan nombres físicos ni tabla concreta porque no se ha elegido formato/plataforma. FP-03 adjudica preservación; FP-06 aplicación; FP-07 verificación; FP-08 trazabilidad. Esta sección especifica invariantes, no mapping implementado ni evidencia de preservación.

## 18. Identidad/versionado de la instancia y metadatos para M

La tabla M deberá consumir, sin colapsarlos, contract_id/version, instance_id/version, component_id/class, owner_component_id, parameter_key, rule_id, source_id/version, destination_id/version, mapping_id/version, IAM_id/version/hash y oráculo/version. La propuesta de valores candidatos está en `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md` y requiere aceptación.

CMP-SERVICE-LOGIC no debe usarse como component_id único: es etiqueta de rol/owner lógico; CMP-SERVICE-LOGIC-001 es candidato. El hash identifica serialización exacta, no equivalencia semántica. C_src, C_dst declarado y C_dst aplicado permanecen separados. No se asignan todavía nombres físicos ni tablas concretas de plataforma.

## 19. Gate siguiente: mapping semántico bajo DEC-C10-069

El mapping M debe usar los IDs aceptados por DEC-C10-069 y mantener versionado independiente. La tabla siguiente a completar será por familia CMP/PAR/RUL: identidad y cardinalidad fuente; identidad y cardinalidad destino; correspondencia/transformación; precondición y postcondición; preservación semántica FP-03; aplicación FP-06/07; evidencia y oráculo; tratamiento de ausencia, conflicto y UNKNOWN; cobertura IAM. Se distinguirán C_dst declarado y C_dst aplicado. No se aceptará equivalencia por igualdad nominal de IDs ni se declarará REF=0 sin cobertura exhaustiva. Mapping concreto y evidencias siguen OPEN; no ejecución autorizada.

## 20. Especialización documental del mapping CMP/PAR/RUL tras DEC-C10-069

**Estado:** PROPUESTA DE ESPECIALIZACIÓN DOCUMENTAL; no aceptada como mapping confirmatorio, no congelada, no implementada ni validada. Reutiliza §§3–8 y 11–19; no crea una matriz paralela. Base conceptual: DEC-C10-068 y DEC-C10-069.

### 20.1. Identidad de referencia y frontera de comparación

La instancia funcional de referencia queda enlazada por:

| Nivel | Identificador | Regla |
|---|---|---|
| Contrato | `C10S-SVC-REQUEST-PROCESSOR` / `1.0.0` | Identidad y versión semántica del contrato |
| Instancia | `C10S-SVC-REQUEST-PROCESSOR-001` / `1` | Identidad lógica y revisión inmutable del paquete |
| Componente | `CMP-SERVICE-LOGIC-001` / `SERVICE_LOGIC` | CMP lógico de referencia |
| Owner lógico | `CMP-SERVICE-LOGIC` | Etiqueta de rol/owner; no sustituye component_id |
| Parámetros | `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` | Claves semánticas aceptadas |
| Regla | `RUL-SVC-ENABLE-PROFILE-01` | Identidad de la regla constitutiva aceptada |

M debe registrar por separado las identidades/versiones de C_src, C_dst, M, IAM y oráculo. Los IDs aceptados identifican el objeto lógico de referencia; no demuestran por sí solos correspondencia entre dos representaciones. La equivalencia exige un registro M explícito, cobertura y evidencia.

### 20.2. Mapping CMP

| Dimensión | C_src | M / transformación | C_dst declarado | C_dst aplicado y adjudicación |
|---|---|---|---|---|
| Identidad | CMP lógico de la instancia, enlazado a `CMP-SERVICE-LOGIC-001` | Correspondencia explícita de identidad funcional; no basta igualdad de nombre/ID | Un CMP destino correspondiente, o composición declarada que represente una sola unidad lógica | Comprobar identidad funcional en el estado aplicado; no inferirla de la configuración preparada |
| Clase | `SERVICE_LOGIC` | Preservación de clase/rol semántico | Clase destino equivalente | Verificar clase funcional efectiva; clase ausente/conflictiva → ? |
| Owner | Owner lógico `CMP-SERVICE-LOGIC`, enlazado al component_id aceptado | Resolver owner_component_id sin confundir etiqueta de rol con identidad | Owner destino explícito y trazable | Verificar que parámetros y regla pertenecen al CMP lógico correspondiente |
| Cardinalidad | Un CMP focal de referencia identificado por DEC-C10-069 | Correspondencia 1:1 para ese CMP lógico; split/merge físico solo si una regla de composición explícita preserva la unidad | Un CMP lógico correspondiente | Duplicación, omisión o composición no declarada que altere la unidad → 0 si demostrada; falta de inventario/cobertura → ? |

La cardinalidad anterior identifica el CMP focal, no afirma que el universo total CMP contenga exactamente un componente. La cardinalidad global y cualquier CMP adicional se declaran en IAM antes de Z/B. No impone una cardinalidad de procesos, contenedores, servicios físicos o componentes de plataforma: esos elementos pertenecen a P1 y requieren clasificación/IAM separado. No se fija REF=0 ni se deduce ausencia de dependencias de la cardinalidad CMP.

### 20.3. Mapping PAR

| Clave | Contrato fuente/destino | Correspondencia semántica exigida | Falsadores observables |
|---|---|---|---|
| `PAR-SVC-ENABLED` | BOOL; dominio `{false,true}`; parámetro obligatorio en el contrato lógico aceptado | Preservar significado booleano y estado; conversión física solo con tabla total explícita y reversible respecto de ambos valores | Inversión true/false; coerción no declarada; pérdida o colapso de estado |
| `PAR-SVC-PROFILE` | ENUM; dominio semántico `{STANDARD, READ_ONLY, DISABLED}`; parámetro obligatorio | Mapping total y semánticamente inyectivo entre los tres significados; los símbolos físicos pueden renombrarse, pero no fusionarse ni ampliarse silenciosamente | Símbolo sin correspondencia; fusión de perfiles; ampliación/restricción del dominio; igualdad nominal con significado distinto |

Reglas de estado y valor:

1. ABSENT y NULL no son equivalentes a VALUE ni entre sí; el contrato funcional aceptado los trata como no admisibles para los dos parámetros obligatorios. La observación de ausencia/null es incumplimiento formal si está acreditada en el objeto cubierto; si no se puede inspeccionar el objeto completo, es ?.
2. DEFAULT solo puede evaluarse cuando exista un default contractual declarado o heredado, con tipo, origen, scope y versión trazables. No se inventa un default para completar el mapping.
3. DEFAULT_ENV_RESOLVED es observación de E_dst/snapshot, no estado PAR del paquete. Su valor no sustituye el default contractual ni demuestra preservación.
4. VALUE se compara tras tipado y decodificación semántica. La igualdad textual no basta; conversiones, normalización y pérdida requieren regla explícita por clave.
5. Los valores concretos de C_src/C_dst por escenario, los defaults y la obligatoriedad/NA atómica más allá de lo aceptado conceptualmente permanecen sujetos al IAM pre-Z/B.

### 20.4. Mapping RUL

Identidad y contrato de regla:

- `rule_id=RUL-SVC-ENABLE-PROFILE-01`.
- Owner lógico: `CMP-SERVICE-LOGIC`; componente enlazado: `CMP-SERVICE-LOGIC-001`.
- Scope: configuración declarativa completa de la unidad lógica del servicio.
- Efecto: REQUIRE.
- Dominio de operandos: ENABLED BOOL y PROFILE ENUM={STANDARD, READ_ONLY, DISABLED}.
- Condición semántica: ENABLED=true implica PROFILE∈{STANDARD, READ_ONLY}.

Representación declarativa de referencia:

`OR(NEQ(PAR-SVC-ENABLED,true), IN(PAR-SVC-PROFILE,{STANDARD,READ_ONLY}))`

M debe conservar, por separado, identidad de regla, scope, referencias a claves PAR, tipos, operadores, operandos, conjunto ENUM, composición/precedencia, efecto y versión de gramática. La equivalencia se juzga por semántica tipada, no por igualdad textual del AST. Un renombrado físico es admisible únicamente con correspondencia explícita de cada referencia y símbolo.

Contrastes semánticos que el mapping debe preservar:
- ENABLED=true / PROFILE=STANDARD → regla satisfecha.
- ENABLED=true / PROFILE=READ_ONLY → regla satisfecha.
- ENABLED=true / PROFILE=DISABLED → regla violada.
- ENABLED=false / cualquier PROFILE declarado → esta implicación no impone restricción.

Falsadores: operador o negación alterados; clave/operando cambiado; conjunto ENUM fusionado/ampliado/restringido; scope/owner alterado; REQUIRE↔FORBID; regla omitida/duplicada; UNKNOWN forzado a booleano. Esta enumeración expresa consecuencias lógicas del contrato aceptado, no fixtures ni resultados ejecutados.

### 20.5. Separación por ruta y etapa

| Ruta/etapa | Objeto producido/observado | Obligación | Familia de evaluación |
|---|---|---|---|
| F1 | Representación intermedia S2 | Preservar CMP/PAR/RUL mediante M; no declarar aplicación | FP-03; FP-01/02 cuando proceda |
| F2 | Aplicación en destino | Aplicar el paquete/regla correspondiente al contrato | FP-06 |
| F2 post-aplicación | Estado destino observado | Verificar CMP/PAR/RUL sobre C_dst^applied, no sobre C_dst^decl | FP-07 y FP-01…05 según predicado |
| A1 | Representación intermedia S1 | Misma obligación semántica, evaluada independientemente de F1 | FP-03; FP-01/02 cuando proceda |
| A2 | Aplicación en destino | Aplicar el paquete/regla correspondiente al mismo contrato funcional | FP-06 |
| A2 post-aplicación | Estado destino observado | Verificar CMP/PAR/RUL sobre C_dst^applied | FP-07 y FP-01…05 según predicado |

F1 PASS no implica F2 PASS; A1 PASS no implica A2 PASS. No se agrupan rutas ni se transfiere evidencia entre ellas. S1/S2 y C_dst^decl no sustituyen C_dst^applied. La comparación de F1/F2 frente a A1/A2 exige mismo contrato funcional, IAM aplicable y criterio F*, pero conserva resultados y evidencia separados por ruta.

### 20.6. Evidencia mínima y adjudicación trivalente

Para cada correspondencia CMP/PAR/RUL y cada ruta/etapa se requiere, documentalmente, enlace a: identidad/versiones de contrato e instancia; snapshots C_src, S1/S2 cuando aplique, C_dst^decl y C_dst^applied; versión de M; IAM y cobertura; observación independiente del estado aplicado; versión/identidad del oráculo; procedencia y timestamps. El hash de artefacto solo se añade cuando exista serialización canónica definida conforme a DEC-C10-069.

- **1:** correspondencia semántica satisfecha, cobertura suficiente y evidencia independiente del objeto/estado pertinente.
- **0:** omisión, mutación o incumplimiento confirmado dentro de un universo cuya cobertura es suficiente.
- **?:** identidad, mapping, cobertura, snapshot aplicado, evidencia o adjudicación incompletos/conflictivos; UNKNOWN nunca se fuerza a 0/1.
- **NA:** solo si el IAM lo predeclara antes de Z/B y demuestra que la propiedad no pertenece al dominio de la instancia. NA no sustituye falta de cobertura.

La verdad estipulada del DGP, la información visible al Analizador y la adjudicación del Evaluador siguen siendo planos distintos. El Evaluador podrá usar verdad oculta/potenciales tras el cegamiento previsto; el Analizador no. Ningún resultado de preservación demuestra por sí solo aplicación, y ningún resultado de aplicación demuestra preservación semántica.

### 20.7. Reconciliaciones necesarias y límites

- La fila histórica PAR-SVC-RETRY-COUNT de §15 queda supersedida para el núcleo por DEC-C10-068; no forma parte del mapping confirmatorio base.
- La nota de §18 que condicionaba la aceptación de los IDs queda supersedida por DEC-C10-069. Los IDs enumerados en §20.1 son aceptados; serialización/MET físico siguen OPEN.
- Esta especialización no completa IAM, cardinalidades globales, referencias REF, defaults concretos, mapping físico, formato, oráculo, tolerancias, cobertura ni reglas de conflicto.
- No convierte FP-03, FP-06, FP-07 o F* en propiedades validadas; no crea fixtures, parser, schema, pruebas, implementación, simulación o ejecución científica.

**Resultado del gate:** la estructura semántica de referencia CMP/PAR/RUL y sus falsadores quedan especificados documentalmente como propuesta trazable. Su aceptación, IAM y evidencia operacional permanecen OPEN. `scientific_execution=false`; `execution_authorized=false`.

### 20.8. Binding de cobertura aceptado

DEC-C10-070 acepta C0 como contrato documental condicionado para los scopes de evidencia usados por este mapping. Cada coverage_scope_id debe quedar ligado en universe_definition/version a un único snapshot exacto, registro, etapa, ruta, clase y versiones de contrato/instancia. La evidencia CMP/PAR/RUL no puede reutilizar un scope de otra etapa/ruta/clase ni inferir equivalencia por compartir nombre o valor.

El control independiente del binding sigue OPEN y es condición previa al Design Freeze. Hasta su auditoría, cobertura y adjudicación que dependan del binding permanecen CONDITIONAL o ? cuando la correspondencia no pueda demostrarse. No se han creado registros ni se autoriza implementación/ejecución.


### 20.9. Reutilización del crosswalk IAM y separación de ejes C0

Se reutiliza el crosswalk histórico `C10_S_IAM_FIELD_TO_COLUMN_CROSSWALK_PROPOSAL_DRAFT_001.md` y la auditoría IAM FP/EDGE. No se crea una taxonomía paralela.

El `object_class` de C0 identifica CMP/PAR/REF/RUL/MET; no identifica directamente NODE/EDGE/ROUTE/PREDICATE ni NODE.semantic_role/boundary_class. El universo versionado debe declarar mapping a ug_record_type, rol/propiedad destino, owner, cardinalidad y regla de inclusión. Mapping candidato: CMP→NODE (EDGE solo relación); PAR→NODE o propiedad atómica del owner; REF→EDGE/referencia tipada; RUL→PREDICATE/operandos; MET→metadatos transversales y SNAPSHOT/EVIDENCE_REGISTER según función.

DEC-C10-071 acepta siete stage_key C10-S: C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED y A2_DST_APPLIED. No equivalen al reloj DGP t−1…t9 ni a SNAPSHOT.phase. La propuesta de codificarlos en SNAPSHOT.scope no fue aceptada; C0 fija la tupla en universe_definition/version.

NONE/F/A son etiquetas de familia de ruta, no route_id exacto; route_id debe identificar la ruta concreta o usar un token global reservado aún OPEN. Para NODE/EDGE, la pertenencia se prueba mediante ROUTE_STEP y record IDs exactos; PREDICATE usa route_record_id; ROUTE su propia revisión. El valor CONFIG de la antigua serialización §18.2 no satisface C0: object_class debe ser CMP/PAR/REF/RUL/MET. dimension C10S_CONFIG_* permanece en COVERAGE_REGISTER, fuera de la tupla de nueve componentes.

El literal del token global, gramática de universe_definition/version y mapping por propiedad permanecen OPEN. Esta sección es propuesta documental, no nueva aceptación ni autorización de cambio de schema/implementación/ejecución.

Esta aceptación es documental. No cambia schema, no crea snapshots/scopes y no autoriza implementación, validación ejecutable, simulación ni ejecución científica; el mapping por propiedad y el enforcement C0 permanecen OPEN/CONDITIONAL.
