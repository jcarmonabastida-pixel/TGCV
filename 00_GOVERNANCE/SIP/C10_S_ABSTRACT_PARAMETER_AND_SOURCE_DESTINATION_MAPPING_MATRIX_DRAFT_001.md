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



### 20.10. Semántica de route_id y scope global — propuesta alineada con DEC-C10-070/071

Esta sección especializa §§20.5–20.9 sin aprobar el token global ni alterar el mapping CMP/PAR/REF/RUL/MET.

1. En scope route-specific, route_id es la identidad semántica de ROUTE y el universo versionado fija route_record_id + snapshot_id + snapshot_object_record_id exactos. ROUTE_STEP prueba la secuencia y la pertenencia de NODE/EDGE; PREDICATE resuelve route_record_id; ROUTE queda fijada por su propio object_record_id.
2. El token global candidato `C10S_SCOPE_GLOBAL` ocuparía el slot route_id de C0 y significaría “sin restricción a ruta concreta”, nunca “no existe ruta” ni “objeto no pertenece a ruta”. Es propuesta G1, pendiente de aceptación y reserva formal del namespace.
3. CMP route-specific requiere CMP→NODE/owner exacto y presencia del NODE en ROUTE_STEP, salvo regla de inclusión explícita para unidad raíz. PAR solo hereda ruta mediante owner CMP y regla IAM explícita. REF requiere EDGE exacto presente en ROUTE_STEP. RUL exige scope/AST/owner resolubles. MET exige target explícito; metadata de contrato/instancia es global.
4. Un objeto en varias rutas se incluye en scopes específicos separados; el scope global lo cuenta una vez. No se agregan denominadores de scopes diferentes.
5. Pertenencia=1 exige mapping y ruta/revisión exactos; pertenencia=0 exige universo del objeto y ROUTE_STEP completos y solo significa no pertenencia a esa ruta; ? conserva mapping/cobertura incompletos; NA requiere IAM ex ante.
6. La ausencia de un objeto en ROUTE_STEP no prueba su ausencia del snapshot, ni ausencia de otras rutas. La ausencia de rutas solo podría sostenerse con cobertura exhaustiva de ROUTE y universo operativo, según el protocolo de evidencia.

No se crea route_id real, token canónico, scope, mapping físico ni fixture. La propuesta queda OPEN hasta aceptación explícita; scientific_execution=false y execution_authorized=false.


### 20.11. DEC-C10-072 — token global aceptado

El literal reservado `C10S_SCOPE_GLOBAL` queda aceptado para el slot route_id C0 con semántica exclusiva “sin restricción a una ruta concreta”. No denota ausencia de rutas ni no pertenencia. Está prohibido como route_id semántico real; colisión produce FAIL. NULL/vacío/NONE/F/A no sustituyen el token.

Scope global: universo elegible de clase/etapa/snapshot, conteo único por identidad. Scope route-specific: route_id real + route_record_id + snapshot exactos, denominadores independientes. Las reglas de pertenencia CMP/PAR/REF/RUL/MET de §20.10 siguen siendo propuesta de mapping y no quedan aprobadas por DEC-C10-072. La gramática universe_definition/version y mapping físico permanecen OPEN.



### 20.12. Envelope y tipado de universe_definition — propuesta UDG-01

Se propone un envelope JSON autocontenido en universe_definition/version. Su scope replica los nueve componentes C0 y debe igualar exactamente la tupla externa; dimension permanece fuera. El envelope declara schema_id/schema_version, universe_id/universe_revision, scope, membership_mode (EXPLICIT/RULE_DEFINED), member_refs tipados o inclusion_rule_ref versionado, exclusion_rule_refs, source_manifest_refs, declared_member_count y provenance_ref.

member_ref identifica object_class, object_id y object_record_id; owner_ref/source_record_ref se incluyen cuando sean necesarios para resolver la semántica de CMP/PAR/REF/RUL/MET. La clase del miembro debe coincidir con la clase del scope. La pertenencia a otra etapa solo se permite mediante proyección explícita y versionada. No inferir identidad por nombre/valor/hash/posición.

Se propone canonicalización determinista UTF-8/NFC, claves ordenadas, arrays ordenados por identidad y SHA-256 del contenido; semver para schema_version y revisión entera monotónica e inmutable para universe_revision. Es una propuesta, no un contrato aceptado. Mapping físico por clase/propiedad y control C0 siguen OPEN; no schema change ni implementación/ejecución.


### 20.13. DEC-C10-073 — envelope aceptado; mapping físico abierto

Se acepta U1 como arquitectura documental de universe_definition: envelope JSON autocontenido/versionado con los campos/cardinalidades de §20.12 y scope C0 de nueve componentes. member_ref se tipa mediante object_class/object_id/object_record_id, con owner/source refs cuando aplique; no se infiere identidad por nombre/valor/hash/posición. EXPLICIT y RULE_DEFINED se aceptan con sus requisitos de exhaustividad y referencias versionadas.

No se acepta canonicalización UTF-8/NFC como obligación, SHA-256 normativo, RFC/JCS ni serialización ejecutable. El mapping físico CMP/PAR/REF/RUL/MET sigue OPEN; esta decisión no valida la pertenencia por clase propuesta en §20.10/20.11 ni cierra C0.


### 20.14. Canonicalización e integridad UDG-02 — propuesta no aceptada

Para el envelope U1 se propone C1: RFC 8785 JCS con prevalidación de schema TGCV. No normalizar Unicode durante canonicalización; exigir NFC previamente solo en campos identificadores declarados NFC-required y rechazar, sin autocorregir. Propiedades ordenadas según JCS; arrays de conjunto ordenados por identidad tipada antes de JCS; arrays secuenciales conservan orden. Números UDG-01 restringidos a enteros seguros no negativos; null prohibido y omisión distinta de array vacío.

Separar source_artifact_hash (bytes físicos originales) de canonical_content_hash (SHA-256 sobre envelope canónico; hash y metadatos fuera del contenido hasheado). Igual hash bajo mismo perfil solo acredita igualdad de bytes canónicos; no prueba equivalencia semántica, pertenencia o exhaustividad. Perfiles distintos no comparables directamente. C1/UDG-02 no aceptada; mapping físico y C0 siguen OPEN.


### 20.15. DEC-C10-074 — canonicalización aceptada; semántica separada

Se acepta C1 RFC 8785 JCS + prevalidación TGCV para U1, perfil documental TGCV-C10S-JCS-1, conforme a las restricciones DEC-C10-074. Arrays de conjunto se ordenan por identidad antes de JCS; secuencias conservan orden; NFC se valida previamente solo donde se marque; null prohibido; enteros seguros no negativos; hashes de fuente y contenido canónico separados.

canonical_content_hash igual bajo el mismo perfil demuestra igualdad de bytes canónicos, nunca equivalencia semántica o exhaustividad. La equivalencia del universo requiere evaluación de mapping/miembros/reglas/fuentes por separado. No hash de producción ni parser/validator autorizados; mapping físico CMP/PAR/REF/RUL/MET sigue OPEN.


### 20.16. UDG-03 — comparación semántica de universos (propuesta)

No inferir equivalencia semántica por hash, nombre, universe_id, revision ni cardinalidad. Comparar por separado: identidad/revisión; scope C0, stage_key, route_id/route_record_id y snapshot; conjunto completo de member identities (object_class/object_id/object_record_id/version); reglas/AST/dependencias y fuentes/cobertura. Provenance/timestamp/hash son evidencia, no miembros; cambios en contrato/instancia/snapshot/ruta o versiones de objetos exigen mapping explícito o NOT_COMPARABLE.

Igualdad extensional requiere conjuntos exhaustivos idénticos en scope/snapshot compatibles. Equivalencia definicional requiere además equivalencia probada de inclusión/exclusión/reglas/dependencias. EXPLICIT y RULE_DEFINED pueden producir mismo conjunto en un snapshot sin ser definicionalmente equivalentes. Estados por dimensión EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE; FAIL reservado a violación de integridad. Propuesta no aceptada; no comparator/implementación.


### 20.17. DEC-C10-075 — comparación semántica aceptada

Se acepta comparación vectorial en siete niveles: artefacto, canónico, identidad, revisión, extensional, definicional y compatibilidad entre revisiones. No inferir equivalencia por hash/nombre/ID/cardinalidad. Igualdad extensional exige conjuntos completos de refs tipadas/versionadas idénticos en C0/stage/route/snapshot comparables; equivalencia definicional exige además inclusión/exclusión/reglas/AST/domínios/dependencias equivalentes. Provenance/timestamp/hash son trazabilidad, no miembros. Scope/snapshot/contrato/instancia/versiones condicionan comparabilidad.

Resultados EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE; FAIL para integridad. Scope incompatible sin mapping explícito = NOT_COMPARABLE; falta evidencia = UNKNOWN. No se autoriza comparator/fingerprint/fixtures/schema change/implementación/ejecución. DEC-C10-075 es aceptación documental.


### 20.18. UDG-04 — identidad y resolución de referencias (propuesta)

Identidad lógica: `(object_class, object_id)`; identidad exacta de registro: `(object_class, object_id, object_record_id)`. Referencia: `(ref_role, target_object_class, target_object_id, target_object_record_id)`; el catálogo de roles debe reconciliarse con REF vigente y no se cierra aquí. No resolver por nombre/valor/hash/posición ni por latest implícito.

Comprobar record_id exacto, clase/id, inmutabilidad, compatibilidad de versiones y cardinalidad en registry versionado con scope definido. Requerida ausente, dangling exhaustivo, contradicción de clase/id o record_id mutable = FAIL; registry inaccesible/incompleto = UNKNOWN; incompatibilidad no mapeada = NOT_COMPARABLE; opcional ausente = NOT_APPLICABLE. Ciclos y cardinalidad se declaran por tipo de relación; no asumir DAG universal. La resolución no prueba pertenencia, aplicabilidad ni ejecución. Propuesta no aceptada; mapping físico REF y mapping CMP/PAR/RUL permanecen OPEN.


### 20.19. DEC-C10-076 — identidad y resolución de referencias aceptadas

Identidad lógica `(object_class, object_id)` distinta de identidad inmutable de registro `(object_class, object_id, object_record_id)`. Referencia tipada por rol y target exacto. Resolución contra registry versionado/scope explícito; prohibido latest implícito o fallback por nombre/valor/posición/hash. REQUIRED/OPTIONAL y cardinalidad según contrato de clase. Ausencia requerida/dangling exhaustivo/conflicto/inmutabilidad = FAIL; registry incompleto/inaccesible = UNKNOWN; incompatibilidad no mapeada = NOT_COMPARABLE; opcional ausente = NOT_APPLICABLE. Ciclos por relación, sin DAG universal. Resolver no prueba membership, aplicabilidad, preservación ni ejecución.

Catálogo REF, schema físico/API/registry/resolver/parser/validator/comparator/fixtures y mapping CMP/PAR/RUL siguen abiertos. No Design Freeze ni ejecución. DEC-C10-076.

### 20.20. Reconciliación REF↔UDG-04 y crosswalk de referencias — propuesta documental

**Estado:** propuesta de reconciliación; no acepta un enum físico de roles, no congela el mapping REF ni modifica el esquema U_G. Prevalecen DEC-C10-061/064/065 para relaciones tipadas de evidencia, snapshot pinning y ROUTE_STEP; DEC-C10-076 gobierna identidad/resolución.

#### A. Tres conceptos que no deben colapsarse

1. **REF de configuración:** objeto del dominio con identidad propia `(REF, ref_id, ref_record_id)`, extremos tipados, dirección, papel/tipo de relación, multiplicidad y regla de integridad. Es candidato a mapping hacia EDGE, no una EDGE por definición.
2. **Referencia UDG-04:** vínculo de resolución desde un origen a un target exacto `(object_class, object_id, object_record_id)`. Su `ref_role` califica la relación desde el origen; no es por sí solo una nueva instancia REF.
3. **FK/vínculo estructural U_G:** integridad de registros como ROUTE_STEP→NODE/EDGE/ROUTE, SNAPSHOT→NODE raíz y CLAIM_EVIDENCE_LINK→destino tipado. No se convierte en REF de configuración ni en miembro REF salvo declaración IAM independiente y justificada.

#### B. Reconciliación de roles ilustrativos

| Rol ilustrativo DEC-C10-076 | Destino/clase esperable | Interpretación y límite |
|---|---|---|
| MEMBER | CMP/PAR/REF/RUL/MET | Referencia de envelope a un miembro; no crea un objeto REF adicional |
| OWNER | Normalmente CMP | Owner exacto del objeto; no sustituir component_id por etiqueta de rol |
| SOURCE | CMP/PAR/REF/RUL/MET o artefacto externo tipado | Origen/procedencia; si es fuente externa no inventar clase CMP ni convertirla en MET sin contrato |
| INCLUSION_RULE | RUL | Regla versionada que define inclusión en universo |
| EXCLUSION_RULE | RUL | Regla versionada que define exclusión |
| DEPENDENCY | REF como relación declarada; target según contrato | No implica instalación, disponibilidad, consumo ni éxito de resolución técnica |
| PROVENANCE | MET o referencia a EVIDENCE_REGISTER/artefacto de procedencia | Evidencia/procedencia no es automáticamente miembro del universo |

La tabla es un crosswalk candidato, no un vocabulario cerrado. Los roles deben tener dominio, cardinalidad, obligatoriedad, origen permitido, destino permitido y condiciones por clase definidos en IAM antes de sellar el universo.

#### C. Modelo semántico candidato de REF

Cada REF debe declarar: identidad lógica y record_id exactos; owner/source endpoint; target endpoint; clase/ID/record_id de ambos extremos; relation_type; direction; role; multiplicity/cardinality; integrity_rule; versión y provenance. Los extremos internos deben resolver en el registry/snapshot compatible. Un endpoint externo requiere tipo/namespace/versión y política de resolución explícitos; no se fuerza a CMP/PAR/MET por conveniencia.

El mapping REF→EDGE solo es admisible con una regla M versionada que conserve extremos exactos, dirección, relation_type/role, multiplicidad e integridad. Una REF binaria puede mapear a una EDGE atómica; una relación n-aria o multiplicidad expandida puede requerir varias EDGE con parent/group identity explícita. No asumir 1:1. Una EDGE U_G no se interpreta automáticamente como REF: puede representar relación analítica, causal, de ruta o estructural.

#### D. Cardinalidad y adjudicación

- Referencia REQUIRED ausente o dangling solo produce FAIL tras demostrar registry cerrado y búsqueda exhaustiva en scope/version exactos.
- Registry incompleto/inaccesible, endpoint sin record_id, más de un candidato o snapshot no fijado → UNKNOWN.
- Versión/schema/contract incompatible sin mapping aprobado → NOT_COMPARABLE.
- Referencia OPTIONAL ausente → NOT_APPLICABLE para esa relación; no elimina la clase REF ni demuestra universo vacío.
- Duplicación, omisión, split/merge o multiplicidad solo se juzgan contra cardinalidad IAM/M predeclarada.
- Resolver ambos extremos no demuestra pertenencia al universo, preservación semántica, instalación de dependencia ni ejecución.

#### E. Falsadores y límites

Falsadores: extremo fuente/destino intercambiado; target con misma identidad lógica pero record_id distinto; EDGE de snapshot distinto; route membership inferida sin ROUTE_STEP; dependencia declarada confundida con dependencia instalada; cardinalidad colapsada; REF transformada en FK estructural; evidencia/provenance contada como miembro; resolución por latest/nombre/hash.

**Gate siguiente:** aceptar/corregir este crosswalk semántico; después definir matriz IAM por clase×rol×extremo×stage_key×scope y cardinalidad. Schema físico REF, enum de roles, registry, resolver, fixtures y ejecución permanecen OPEN/no autorizados.

### 20.21. DEC-C10-077 — aceptación de la base conceptual REF↔UDG-04

Se acepta la distinción REF de configuración / referencia tipada UDG / FK estructural U_G; la identidad propia y extremos tipados de REF; y que REF→EDGE solo sea candidato mediante M explícito/versionado, sin presunción 1:1 y con parent/group identity para split/merge/n-aria. Los roles de DEC-C10-076 siguen ilustrativos, no enum cerrado. No quedan aceptados roles finales, dominios de extremos, cardinalidades, REQUIRED/OPTIONAL, IAM ni mapping físico. DEC-C10-077 prevalece sobre la propuesta de §20.20 solo en estos límites conceptuales; gates abiertos permanecen abiertos.

## 17. Proyección semántica PAR sobre U_G — propuesta de reconciliación

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión nueva, no implementada, sin instancias ni observaciones reales. Reutiliza DEC-C10-053/054/056/068/069/070/073/074/075/076 y el contrato abstracto de instancia, la matriz de mapping PAR y el overlay U_G existente. No sustituye ni amplía el schema físico U_G.

### 1. Decisión de diseño propuesta
Representar PAR como **propiedad atómica tipada del CMP propietario**, no como NODE independiente y no como EDGE/REF. La identidad semántica de cada parámetro es `parameter_key` dentro del contrato/versión y el ámbito de `owner_component_id`; la instancia observada se distingue por la tupla exacta de contrato/instancia, snapshot/record, stage_key, ruta/scope y versión del CMP owner. Esta opción evita inventar un `semantic_role=PARAMETER` (no existe en el vocabulario aceptado de NODE), evita tratar una propiedad escalar como componente y preserva el ownership ya definido.

La representación es una **fila lógica de manifiesto IAM/inspección**, usando la estructura de referencia ya descrita en U_G §18.3 (manifest_record_id, contract/instance, snapshot exacto, stage_key, route, object_class=PAR, semantic_id/version, owner_component_id, property_key/type/state/value, mapping, declared_or_applied, evidence, claim-evidence, coverage y adjudicación). No se crea una tabla física PAR ni una nueva capa semántica persistida. La fila de manifiesto no recibe por ahora un object_record_id U_G ni una FK nueva: el contrato de identidad de esa fila sigue OPEN.

### 2. Campos semánticos por PAR
Cada entrada lógica debe resolver, sin inferencia:
- `parameter_key` estable y no reutilizable para otro significado;
- `owner_component_id` exacto y su CMP NODE/record/version en el mismo snapshot;
- `type`, dominio/escala/unidad cuando proceda;
- `requiredness` y disparador condicional, si lo hubiera;
- `allowed_states` y estado observado, diferenciando ABSENT, NULL, DEFAULT y VALUE;
- `value` solo si el estado lo permite y procede de la fuente observada;
- `default_contract` (kind, origen, scope, precedencia y versión) solo cuando exista declaración;
- mapping_id/version, estado MAPPED/UNMAPPED/AMBIGUOUS/NOT_APPLICABLE y regla de conversión;
- evidencia, cobertura, adjudicación y procedencia exactas.

No colapsar ausencia, null, default declarado/heredado y valor explícito. `DEFAULT_ENV_RESOLVED` es resolución de E_dst/P1, enlazada al parámetro y snapshot ambiental, no un estado adicional del paquete P0 ni una reescritura de DEFAULT.

### 3. Especialización ya aceptada para el servicio sintético
El roster nuclear se limita a:
- `PAR-SVC-ENABLED`: BOOL, dominio `{false,true}`, REQUIRED.
- `PAR-SVC-PROFILE`: ENUM, dominio `{STANDARD, READ_ONLY, DISABLED}`, REQUIRED.

`PAR-SVC-RETRY-COUNT` queda fuera del núcleo confirmatorio por DEC-C10-068. No debe incorporarse al universo base ni usarse como proxy de capacidad P1. Para ENABLED y PROFILE, ABSENT/NULL no son admisibles; DEFAULT no queda declarado por DEC-C10-068 y solo podría usarse tras declaración contractual explícita, versionada y previa al IAM. No se asignan valores de escenario en este contrato de representación.

### 4. Proyección y enlaces con U_G
- El CMP propietario se resuelve a NODE exacto mediante `component_id/node_id + object_record_id + snapshot_id`; no se resuelve por nombre, rol lógico ni hash.
- La fila lógica PAR referencia ese owner y conserva `parameter_key` como identidad de propiedad. No crea un NODE adicional ni una arista EDGE.
- `COVERAGE_REGISTER` conserva scopes independientes `C10S_CONFIG_PAR` por snapshot×stage_key×ruta/scope, con universo/denominador explícitos. No combinar cobertura PAR con CMP.
- Como CLAIM_EVIDENCE_LINK no admite target_type=PAR, la propuesta es vincular la afirmación a la revisión exacta del NODE owner y/o al COVERAGE_SCOPE correspondiente; `claim_statement` y `relevance_scope` deben identificar inequívocamente `parameter_key`, propiedad, estado y etapa. No se añade un nuevo FK ni se finge que la evidencia apunta a una tabla PAR.
- EVIDENCE_REGISTER conserva fuente, versión, método, integridad y límites; no copiar valores sensibles ni credenciales.
- M mantiene la correspondencia `parameter_key_src → parameter_key_dst`, owner, tipo, dominio, unidad, estado, valor/default y conversión. M es artefacto evaluativo versionado, no EDGE ni una capa semántica adicional.

### 5. Evaluación independiente y etapas
La comparación se realiza por parámetro y etapa, preservando la separación:
- C_SRC: contrato/propiedad fuente observada.
- F1_S2 y A1_S1: representación intermedia producida por cada ruta.
- F2_DST_DECL y A2_DST_DECL: propiedad destino declarada, no aplicada.
- F2_DST_APPLIED y A2_DST_APPLIED: propiedad efectivamente observada tras aplicación.

La evidencia de una etapa no se traslada a otra. El mismo `parameter_key` lógico no prueba por sí solo correspondencia; M debe resolver el owner y la transformación tipada. La equivalencia de valor no compensa una diferencia de tipo, dominio, unidad, estado o default. El analizador no accede a truth oculta ni a etiquetas del oráculo.

### 6. Adjudicación y límites
`1` exige predicado satisfecho con evidencia/cobertura suficiente; `0` exige incumplimiento confirmado o ausencia exhaustiva según el predicado; `?` ante falta de fuente, owner, mapping, snapshot o cobertura; `NA` solo por no aplicabilidad ex ante IAM. `NOT_COMPARABLE` cuando versiones/identidades no tengan mapping aprobado. Una propiedad ausente en el artefacto no equivale a ausencia de observación ni autoriza imputar valor/default.

La propuesta no fija cardinalidades adicionales, no asigna REQUIRED/OPTIONAL nuevos, no cambia DEC-C10-068, no aprueba el roster fuera del núcleo ya aceptado, no añade semantic_role, tabla PAR, FK, EDGE ni REF, no sella IAM, no define serialización ni hash, y no autoriza parser, validator, fixtures, implementación, Design Freeze o ejecución.

### 7. Cuestiones aún abiertas
1. Identidad/versionado de la fila lógica de manifiesto PAR y su relación exacta con el registro IAM sellado.
2. Regla formal para claim_statement/relevance_scope que haga inequívoca la referencia a parameter_key sin crear FK PAR.
3. Mapping concreto de owner y property_key entre representaciones fuente/destino e intermedias.
4. Evidencia disponible por etapa y cobertura real.
5. Defaults y sus reglas por clave, si alguna vez se incorporan; no se presuponen.

## 17.1 — Identidad y revisión de la fila lógica PAR

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión, no implementada y sin filas/observaciones reales. Resuelve la laguna de identidad detectada en §§19.2/19.19 y §17, sin extender DEC-C10-062 ni modificar el schema U_G.

### 1. Separación de identidades
La fila lógica PAR del manifiesto no es una entidad U_G de las tablas NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. Por tanto:
- `parameter_key` identifica la propiedad semántica en el ámbito de contrato/versión y owner CMP; no identifica una observación.
- `manifest_record_id` identifica una fila concreta e inmutable del manifiesto; es opaco, no vacío y único dentro del manifiesto/versionado IAM que la contiene. No reutilizar `object_record_id`, `node_id`, `component_id` ni IDs TID/SID/RID/EID.
- La clave lógica de captura PAR queda propuesta como la tupla exacta: contract_id/version + instance_id/version + snapshot_id/snapshot_object_record_id + stage_key + route_id/route_record_id o ausencia justificada + scope/universe revision + owner_component_id y revisión exacta del CMP + parameter_key/semantic_version. Esta clave delimita qué observación se está representando; no sustituye a manifest_record_id.
- `coverage_scope_id` sigue siendo identidad del scope de cobertura, independiente de la fila PAR.

### 2. Revisión y corrección
Se propone que cada fila sea inmutable. Una corrección de captura, adjudicación o metadato de la fila no sobrescribe el registro previo: crea un nuevo `manifest_record_id`, incrementa `manifest_record_revision` en uno para la misma clave lógica y señala el registro inmediatamente anterior mediante `supersedes_manifest_record_id`. La primera revisión es 1 y no tiene predecesor. Solo puede existir una cadena lineal por clave lógica; no se admiten bifurcaciones, ciclos, saltos, referencias cruzadas entre claves o snapshots ni reutilización de IDs. El historial se conserva.

Una nueva observación en otro snapshot, etapa, ruta/scope, versión de owner o versión contractual no es una revisión de la misma fila: constituye una nueva clave lógica y comienza revisión 1. Un cambio semántico de parameter_key o de significado exige nueva identidad de parámetro conforme al contrato, no supersession de captura.

Los campos `manifest_record_revision` y `supersedes_manifest_record_id` son nombres propuestos de contrato lógico, no columnas físicas aprobadas. La propuesta no fuerza un `object_version` ni `supersedes_record_id` U_G.

### 3. Límite de DEC-C10-062
DEC-C10-062 se aplica expresamente solo a NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT; las demás tablas mantienen sus propias claves y contratos. No puede extenderse por analogía a filas de manifiesto. La mención histórica en §19.2 de que manifest_record_id sería versionado “conforme a DEC-C10-062 si se adopta” queda aclarada por esta propuesta: el manifiesto necesita contrato propio y no hereda object_version/supersedes_record_id de U_G. Esta aclaración no altera la decisión aceptada ni la reescribe; precisa el límite de su ámbito.

### 4. Unicidad y control
Para una misma clave lógica y revisión debe existir exactamente un manifest_record_id; un manifest_record_id no puede identificar dos claves/revisiones. Toda referencia a una fila debe resolver por ID exacto dentro de la versión de manifiesto/IAM fijada, nunca por latest, posición, nombre o hash aislado. La verificación documental deberá comprobar:
- no duplicidad de manifest_record_id;
- unicidad de clave lógica + manifest_record_revision;
- revisión inicial 1 sin predecesor;
- sucesión inmediata y misma clave lógica para revisiones posteriores;
- ausencia de ciclos, bifurcaciones, huérfanos y referencias futuras;
- pinning exacto del snapshot y del CMP owner;
- coherencia de coverage_scope_id con la misma tupla de etapa/ruta/clase/universo;
- preservación de múltiples evidencias como vínculos separados, no serializadas en la fila.

No se impone unicidad global entre distintas versiones de manifiesto/IAM; el namespace exacto y su versión forman parte de la resolución.

### 5. Estados de propiedad y ausencia
Una fila PAR representa una propiedad esperada/inspeccionada, no presupone que la propiedad esté presente en el artefacto. `state=ABSENT` puede registrarse solo con evidencia/cobertura según el predicado; no se elimina la fila por ausencia. `NULL`, `DEFAULT` y `VALUE` permanecen distintos. El registro de una revisión no convierte por sí mismo ? en 0 ni acredita COMPLETE.

### 6. Límites
No se crea tabla PAR, no se añaden columnas U_G, no se aprueba DDL/serialización/API/parser/validator/fixtures, no se asignan valores de escenario ni se instancia el manifiesto. La aceptación de esta propuesta, si se produce, será documental y no autorizará implementación ni ejecución. IAM permanece sin sellar; `scientific_execution=false`; `execution_authorized=false`.

### 7. Pendientes para aceptación
- Confirmar namespace de unicidad: por versión de manifiesto/IAM (propuesta) frente a global en toda la línea C10-S.
- Confirmar si la revisión de captura es necesaria o si bastaría append-only con IDs nuevos y relación de supersession.
- Confirmar nombre final de los campos de revisión y predecesor.

## 17.2 — Recomendación de cierre de identidad PAR

**Estado:** RECOMENDACIÓN PARA ACEPTACIÓN DEL USUARIO; no es DEC aceptada ni contrato congelado. Se propone resolver conjuntamente las tres cuestiones abiertas de §17.1/§19.20/§20/§16.62/§80/§207/§86.

### Recomendación única
1. **Unicidad de `manifest_record_id`: global en toda la línea C10-S**, independiente de versión IAM/manifest. El ID es opaco, inmutable y nunca se reutiliza. La versión IAM sigue formando parte de la resolución contextual de la fila, pero no limita la unicidad del identificador. Se recomienda unicidad global porque simplifica referencias, auditoría y detección de colisiones entre versiones; no implica que el registro sea una entidad U_G.
2. **Modelo append-only con revisión explícita.** Cada corrección/adjudicación posterior genera nuevo `manifest_record_id`; no se sobrescribe ni elimina la fila anterior. Para una misma clave lógica de observación, `manifest_record_revision` empieza en 1 y aumenta exactamente en uno. Las revisiones posteriores incluyen `supersedes_manifest_record_id` apuntando a la revisión inmediatamente anterior. Una sola cadena lineal por clave lógica; sin bifurcaciones, ciclos, saltos ni huérfanos. La revisión es metadato de secuencia de captura, no versión semántica del parámetro.
3. **Nombres recomendados:** `manifest_record_revision` y `supersedes_manifest_record_id`, exactamente así. `manifest_record_id` se mantiene como identificador del registro, distinto de `parameter_key`, CMP owner, `object_record_id` U_G y `coverage_scope_id`.

### Reglas para evitar revisiones falsas
- Nueva etapa, snapshot, ruta/scope, contrato/instancia o revisión del CMP owner = nueva clave lógica y revisión 1, no supersession.
- Cambio de significado de `parameter_key` = nueva identidad semántica; no se corrige como revisión de captura.
- Corrección de transcripción, evidencia, estado, mapping o adjudicación de la misma captura lógica = nueva revisión, conservando la anterior.
- Varias evidencias para una misma fila son vínculos independientes; no crean revisiones por sí solas.
- Un cambio de versión IAM que solo reempaqueta la misma fila no genera automáticamente una nueva observación. Si la identidad lógica de captura permanece idéntica, la política de migración/referencia deberá conservar el ID; si cambia una dimensión de la clave lógica, comienza una nueva cadena. La migración entre versiones IAM requiere mapping explícito y no se presume.

### Condición de aceptación
La aceptación confirmaría solo este contrato lógico documental de identidad/supersession. No crea columnas, tabla PAR, DDL, serialización, generador de IDs, API, parser, validator, fixtures ni registros reales; tampoco sella IAM, cierra el crosswalk PAR↔U_G, autoriza implementación o cambia `scientific_execution=false` / `execution_authorized=false`.

**Pendiente de aceptación expresa:** unicidad global; append-only + revisión explícita; nombres exactos indicados.

## 17.3 — Aplicación de DEC-C10-079 a la identidad de filas PAR

**Estado:** ACEPTADO — DEC-C10-079. Esta sección propaga el contrato lógico aprobado; prevalece sobre cualquier recomendación previa que mantuviera abiertas estas cuestiones.

- `manifest_record_id`: globalmente único en toda la línea C10-S, opaco, inmutable y nunca reutilizado, independiente de la versión IAM.
- Append-only: ninguna fila se sobrescribe ni elimina. Toda corrección de la misma captura lógica crea un nuevo ID y conserva el anterior.
- `manifest_record_revision`: revisión secuencial por clave lógica, desde 1, sin saltos.
- `supersedes_manifest_record_id`: en revisiones posteriores, referencia a la revisión inmediatamente anterior de la misma clave lógica. Cadena lineal única, sin bifurcaciones, ciclos, huérfanos ni referencias cruzadas.
- Cambio de snapshot, etapa, ruta/scope, contrato/instancia o revisión del CMP owner inicia una nueva clave lógica y revisión 1. Cambio semántico de `parameter_key` exige nueva identidad semántica.
- Múltiples evidencias no crean revisiones por sí solas. Reempaquetar en nueva versión IAM no crea automáticamente nueva observación; migración exige mapping explícito.

**Límites:** decisión documental lógica. No crea tabla/columnas PAR o U_G, DDL, serialización, generador, API, parser, validator, fixtures ni registros reales; no sella IAM, no cierra PAR↔U_G, no autoriza Design Freeze, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 17.4 — Binding probatorio de PAR en CLAIM_EVIDENCE_LINK

**Estado:** PROPUESTA DOCUMENTAL; no aceptada como nueva DEC, no implementada, sin registros observados. Reutiliza DEC-C10-079 y el esquema U_G §12.2–12.3/§18.3–18.8. No amplía los dominios ni las FK de U_G.

### 1. Principio
CLAIM_EVIDENCE_LINK no tiene target_type PAR ni FK a manifest_record_id. No se simula una FK inexistente. La trazabilidad se compone de:
(a) FK real a COVERAGE_SCOPE (y, cuando la afirmación se refiere al owner CMP como objeto por derecho propio, un vínculo separado al NODE owner);
(b) localizador lógico exacto de la fila PAR en claim_statement/relevance_scope;
(c) control independiente que resuelve ese localizador contra el manifiesto IAM versionado y verifica su integridad.

### 2. Perfil normativo propuesto para una afirmación sobre una fila PAR
Una fila CLAIM_EVIDENCE_LINK por cada evidencia × afirmación × fila PAR:
- `claim_target_type=COVERAGE_SCOPE`;
- `target_coverage_scope_id` = scope PAR exacto, cuyo `dimension=C10S_CONFIG_PAR` y cuyo universe_definition/version fija contrato/instancia, snapshot+record, stage_key, route/scope, clase PAR y universo;
- todos los campos target_* no aplicables quedan vacíos; no se rellenan FK de NODE como sustituto de PAR;
- `claim_statement` identifica explícitamente el predicado y la fila: `PAR_ROW|manifest_record_id=<ID>|manifest_record_revision=<N>|parameter_key=<KEY>|owner_component_id=<CMP_ID>|predicate=<PREDICATE>`;
- `relevance_scope` identifica el contexto completo: `contract_id/version;instance_id/version;snapshot_id/snapshot_object_record_id;stage_key;route_id/route_record_id-or-justified-NONE;coverage_scope_id;owner_component_id/owner-record/version;parameter_key;manifest_record_id;manifest_record_revision`.
Los literales anteriores describen un perfil documental de campos textuales existentes, no una gramática física ni un parser aprobado. No se deben usar separadores/valores ambiguos; si algún identificador contiene delimitadores, la serialización futura tendrá que definir escaping/versionado antes de automatizar.

### 3. Resolución y controles independientes
El control debe resolver manifest_record_id globalmente (DEC-C10-079), verificar revision y supersession, y comprobar igualdad exacta entre la fila del manifiesto, su clave lógica, owner CMP, snapshot, stage_key, route/scope y coverage_scope_id. También verifica:
- dimension C10S_CONFIG_PAR y universe_definition/version compatibles;
- que el scope corresponde a la misma tupla y no está compartido entre snapshots/etapas/rutas/clases;
- que el CMP owner resuelve al NODE/object_record_id/snapshot exactos;
- que parameter_key y manifest_record_revision coinciden con el manifiesto;
- que la evidencia está en EVIDENCE_REGISTER y que la relación 1:N se conserva sin listas serializadas;
- que la evidencia realmente respalda el predicado y estado citados; un enlace FK correcto no prueba el contenido.
Un fallo de resolución, contradicción o colisión es FAIL; falta de manifiesto, snapshot, scope o fuente es UNKNOWN/?; incompatibilidad de versiones sin mapping es NOT_COMPARABLE; NA solo por inaplicabilidad ex ante. No inferir 0 desde falta de vínculo.

### 4. Owner CMP y cobertura
Si una misma evidencia respalda también una afirmación distinta sobre identidad/estado del CMP owner, se crea otro CLAIM_EVIDENCE_LINK con target NODE y su FK exacta. No se duplica ni se mezcla esa afirmación con la afirmación PAR. La afirmación PAR conserva COVERAGE_SCOPE como target FK y el localizador PAR en campos textuales.
COVERAGE_REGISTER permanece por clase PAR y por snapshot×stage_key×ruta/scope; COMPLETE exige denominador, fuentes, enumeración y excepciones conforme a §18.6. El link a un scope no convierte automáticamente el scope en COMPLETE.

### 5. Límites y decisiones abiertas
No se añade target_type PAR, FK, tabla PAR, columna U_G, tabla puente ni relación física nueva. No se crea CLAIM_EVIDENCE_LINK directo a manifest_record_id; su resolución es un control independiente contra el manifiesto. No se define todavía escaping/canonicalización del localizador, vocabulario de predicate ni automatización. No se sella IAM, no se declara cobertura, no se crean registros y no se autoriza parser, validator, fixtures, implementación o ejecución.
Pendiente de aceptación: perfil COVERAGE_SCOPE + localizador en claim_statement/relevance_scope; vínculo NODE separado solo para afirmaciones propias del CMP; control independiente de resolución.

## 17.5 — Binding probatorio aceptado (DEC-C10-080)

**Estado:** ACEPTADO — DEC-C10-080. Sustituye el estado pendiente de aceptación de §17.4/§19.23/§23/§16.65/§83/§210/§89.

- Afirmación sobre fila PAR: CLAIM_EVIDENCE_LINK usa `claim_target_type=COVERAGE_SCOPE` y FK `target_coverage_scope_id` al scope exacto `dimension=C10S_CONFIG_PAR`.
- `claim_statement` y `relevance_scope` contienen localizador lógico suficiente para resolver `manifest_record_id`, `manifest_record_revision`, `parameter_key`, owner CMP, snapshot/record, `stage_key`, ruta/scope y universo/version.
- Una fila CLAIM_EVIDENCE_LINK por evidencia×afirmación×fila PAR. Las evidencias múltiples se conservan como filas separadas, nunca como listas embebidas.
- Control independiente resuelve ID global y verifica revisión/supersession y coincidencia exacta de clave lógica, owner, snapshot, etapa, ruta/scope, coverage scope, universo, predicado y evidencia.
- Una afirmación separada sobre el CMP owner usa otro CLAIM_EVIDENCE_LINK con target NODE y FK exacta. No sustituye el target COVERAGE_SCOPE de la afirmación PAR.
- El enlace al scope no implica COVERAGE COMPLETE; se aplican U_G §12.3/§18.6.

**Restricciones:** no se añade target_type PAR, FK, tabla o puente. No se aprueban gramática, escaping, canonicalización, serialización, parser ni automatización. Los campos singulares `evidence_id`/`claim_evidence_id` del manifiesto no sustituyen el registro 1:N de CLAIM_EVIDENCE_LINK. No se crean observaciones, no se sella IAM, no se declara cobertura ni se autoriza implementación/ejecución. `scientific_execution=false`; `execution_authorized=false`.


### 15.1. Contrato candidato de equivalencia semántica para los dos PAR nucleares

**Estado:** propuesta documental pendiente de aceptación. Especializa §§4–5 y 15–16 para el roster aceptado por DEC-C10-068 y las obligaciones de etapa DEC-C10-083. No selecciona representación física ni declara mappings observados.

#### A. Separación de dos niveles

La equivalencia se adjudica en dos niveles no intercambiables:

1. **Equivalencia de estado:** conserva la distinción entre VALUE, ABSENT, NULL y cualquier estado DEFAULT contractual que pudiera aprobarse en el futuro. Para los dos PAR del núcleo, DEC-C10-083 exige VALUE en posiciones declarativas y no hay DEFAULT contractual aceptado. La falta de registro/evidencia no se recodifica como ABSENT.
2. **Equivalencia de valor:** solo se evalúa cuando ambos lados tienen estado VALUE y sus tipos/dominios están resueltos. Un valor igual no compensa estado, tipo, dominio u owner incorrectos.

Cada adjudicación identifica parámetro, owner CMP, snapshot, stage_key, ruta, mapping_id/version y evidencia. Los mappings F1 y A1 se adjudican por separado.

#### B. PAR-SVC-ENABLED — BOOL

El mapping semántico candidato es identidad exacta:
- dominio fuente y destino: `{false,true}`;
- `false → false`, `true → true`;
- sin inversión de polaridad, coerción implícita, codificación ambigua ni valor por defecto;
- cualquier representación física alternativa debe decodificarse mediante regla total, determinista y versionada a exactamente uno de los dos valores lógicos.

Falsadores: inversión true/false; colapso de ambos valores; conversión no determinista; coerción dependiente de entorno; estado no VALUE tratado como booleano.

#### C. PAR-SVC-PROFILE — ENUM

El mapping semántico candidato debe ser una **biyección total versionada** entre los tres significados lógicos:
- `STANDARD ↔ STANDARD` (significado funcional STANDARD);
- `READ_ONLY ↔ READ_ONLY` (significado funcional READ_ONLY);
- `DISABLED ↔ DISABLED` (significado funcional DISABLED).

La notación muestra identidades lógicas; no obliga a que los símbolos físicos de origen/destino tengan esos mismos literales. Si difieren, M debe declarar explícitamente los tres pares físicos→significado lógico→destino. No se admite símbolo sin correspondencia, fusión de dos significados, expansión silenciosa del dominio ni mapping parcial. La bijección preserva los tres significados, no necesariamente la grafía.

Falsadores: STANDARD y READ_ONLY fusionados; DISABLED traducido a un modo habilitado; símbolo obligatorio sin mapping; mapping dependiente de alias no versionado; valor desconocido convertido a uno de los tres símbolos.

#### D. Invariante de la regla constitutiva

Después de decodificar ambos parámetros al dominio lógico común, debe conservarse sin alteración:
`ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}`, efecto `REQUIRE`, scope de la unidad lógica y semántica de evaluación. No se añade la implicación inversa. `ENABLED=false` no restringe PROFILE por esta regla.

La evaluación de la regla es independiente de la comparación de valores PAR: ambos PAR pueden mapearse individualmente y, aun así, la regla podría estar alterada, ausente o no aplicada. FP-03 evalúa preservación; FP-06 aplicación efectiva; FP-07 verificación post-aplicación; FP-08 validez probatoria/procedencia.

#### E. Composición por etapas y rutas

- `C_SRC → F1_S2` y `C_SRC → A1_S1`: dos adjudicaciones independientes; no se permite que el PASS de una ruta cubra la otra.
- `F1_S2 → F2_DST_DECL` y `A1_S1 → A2_DST_DECL`: comparar la declaración destino con el resultado intermedio de su propia ruta y con la semántica lógica fuente.
- `F2_DST_DECL → F2_DST_APPLIED` y `A2_DST_DECL → A2_DST_APPLIED`: comprobar aplicación efectiva por evidencia independiente. La igualdad declarativa no demuestra aplicación.
- Las comparaciones se hacen mediante composición explícita de mappings versionados; no se presume transitividad entre mappings incompatibles ni se comparan literales físicos directamente si sus namespaces difieren.

#### F. Resultados y límites

- `PASS`: estado y valor semántico conformes, owner/snapshot/mapping exactos y evidencia/cobertura suficientes.
- `FAIL`: contradicción semántica demostrada (inversión BOOL, pérdida/fusión ENUM, estado indebido, alteración de regla o valor distinto).
- `UNKNOWN`: evidencia, cobertura, owner, snapshot, mapping o decodificación insuficientes.
- `NOT_COMPARABLE`: identidades/versiones incompatibles sin mapping aprobado.
- `NA`: solo no aplicabilidad declarada ex ante; no se deriva de falta de datos y no se admite para los dos PAR en las siete etapas del contrato base.

La propuesta no fija valores por escenario, nombres físicos, codificación concreta, tablas de conversión, tolerancias, oráculo ni mediciones. No adjudica resultados F1/A1/F2/A2, no sella IAM, no crea fixtures/parser/validator ni autoriza implementación, Design Freeze o ejecución científica.

### 15.2. Aceptación del contrato de equivalencia semántica — DEC-C10-084

**Estado:** ACEPTADO — contrato lógico documental.

La propuesta §15.1 queda aceptada conforme a DEC-C10-084. Para `PAR-SVC-ENABLED` se exige identidad semántica BOOL exacta (`false→false`, `true→true`); para `PAR-SVC-PROFILE`, biyección total, inyectiva y versionada entre los tres significados STANDARD/READ_ONLY/DISABLED, sin exigir igualdad de grafía física. Estado y valor se adjudican separadamente.

Se acepta la preservación independiente de `RUL-SVC-ENABLE-PROFILE-01`, las adjudicaciones independientes F1/A1 y la separación entre destino declarado y aplicación efectiva F2/A2. La composición exige mappings explícitos y versionados; no se presume transitividad ni equivalencia por literales físicos.

Rigen estados y límites de DEC-C10-084. No se aprueban codificaciones ni mappings físicos, no se adjudican resultados observados, no se sella IAM ni se autoriza implementación o ejecución científica.

### 15.3. Predicados candidatos de adjudicación C_SRC→F1_S2 / C_SRC→A1_S1

**Estado:** propuesta documental pendiente de aceptación. Especializa DEC-C10-083/084; no afirma observaciones ni mappings implementados. Se aplica exclusivamente a `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` y `RUL-SVC-ENABLE-PROFILE-01`.

#### A. Unidad de adjudicación

Cada adjudicación es independiente por la tupla:

`contract_id/version + instance_id/version + component_id + source_snapshot_record + target_snapshot_record + stage_key + route_id/route_record_id + coverage_scope_id + parameter_key/rule_id + mapping_id/version`.

La comparación F1 usa `stage_key=F1_S2` y la ruta F exacta; la comparación A1 usa `stage_key=A1_S1` y la ruta A exacta. El snapshot C_SRC de referencia debe estar fijado explícitamente en el envelope del universo y ser el mismo baseline lógico para ambas comparaciones, salvo que el diseño declare y versiona baselines separados ex ante. Ninguna inferencia se realiza desde SNAPSHOT.phase, timestamp, texto libre o familia F/A sin route_id exacto.

#### B. Cinco familias de predicados

| Familia | Predicado lógico | PASS exige | FAIL exige |
|---|---|---|---|
| Estado PAR | `P-STATE(k,r)` | Estado fuente y salida observados y conformes; VALUE preservado en ambos extremos para estos PAR | Contradicción observada y cubierta: estado no VALUE, ABSENT/NULL o pérdida/alteración de estado |
| Valor/tipo/dominio PAR | `P-VALUE(k,r)` | Decodificación total/versionada; tipo y dominio válidos; significado lógico idéntico | Contradicción demostrada: BOOL invertido/colapsado o ENUM fusionado/perdido/alterado |
| Regla RUL | `P-RUL(r)` | Misma identidad/versionado lógico, AST/operandos, efecto REQUIRE, scope y semántica después de normalización aprobada | Regla ausente/alterada o implicación/efecto/scope contradictorios, con cobertura suficiente |
| Identidad y alcance | `P-BIND(r)` | CMP owner, snapshots, etapa, ruta, scope, registros y mapping/version resueltos exactamente | Colisión, contradicción de identidad, scope o referencia demostrada |
| Procedencia probatoria | `P-EVID(r)` | EVIDENCE_REGISTER y CLAIM_EVIDENCE_LINK resuelven fuente, método, custodio, captura, integridad y predicado respaldado | Evidencia contradictoria, inválida o procedencia rota demostrada |

Donde `k∈{PAR-SVC-ENABLED, PAR-SVC-PROFILE}` y `r∈{F1,A1}`. Cada familia se registra por separado; no se suman en una puntuación ni se permite que un PASS compense un FAIL.

#### C. Instanciación por ruta

Para cada ruta se crean, conceptualmente, estas adjudicaciones separadas:

- `P-STATE(PAR-SVC-ENABLED,r)`
- `P-VALUE(PAR-SVC-ENABLED,r)`
- `P-STATE(PAR-SVC-PROFILE,r)`
- `P-VALUE(PAR-SVC-PROFILE,r)`
- `P-RUL(r)`
- `P-BIND(r)`
- `P-EVID(r)`

La matriz de observaciones debe conservar `r=F1` y `r=A1` como unidades distintas. No se crea un predicado agregado F1+A1 que permita compensación o imputación cruzada.

#### D. Reglas específicas

1. **BOOL:** comparar los valores lógicos decodificados; `false→false` y `true→true`. Si la codificación física cambia, M debe cubrir el dominio completo y ser determinista/versionado.
2. **ENUM:** resolver cada símbolo observado al significado lógico STANDARD/READ_ONLY/DISABLED. M debe cubrir el dominio completo, ser biyectivo y versionado; no basta con que el símbolo observado tenga una traducción si el mapping contractual global es parcial.
3. **Estado:** para ambos PAR, VALUE debe estar presente en C_SRC y F1_S2/A1_S1. Ausencia de fila, captura o evidencia no demuestra ABSENT; se mantiene UNKNOWN salvo que el universo y cobertura permitan demostrar ausencia.
4. **RUL:** evaluar la preservación de `ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}`, efecto REQUIRE y scope lógico. La comprobación FP-03 es preservación estructural/semántica; no prueba que el runtime haya aplicado la regla (FP-06/FP-07).
5. **Owner y binding:** la identidad del CMP debe resolver al NODE anchor por snapshot según DEC-C10-082. Los PAR no crean NODE ni se vinculan por similitud nominal.
6. **Evidencia:** el analizador no recibe DGP truth ni valores potenciales. La fuente de referencia y la salida observada se fijan por artefactos/snapshots exactos; el adjudicador no puede inferir equivalencia desde el nombre de clave.

#### E. Resultados y agregación

- `PASS`: todos los requisitos de ese predicado están observados y cubiertos, con identidad y mapping exactos.
- `FAIL`: contradicción sustantiva demostrada con universo/cobertura suficientes. No usar FAIL por ausencia de registro cuando la cobertura es incompleta.
- `UNKNOWN`: snapshot, observación, cobertura, evidencia, mapping o resolución insuficientes.
- `NOT_COMPARABLE`: contratos/versiones/namespaces incompatibles sin mapping aprobado.
- `NA`: no aplicable ex ante; no admisible para estos dos PAR ni la regla en las dos rutas del contrato base.

El resultado de una ruta es un vector de estados por predicado, no un único PASS binario. Si se requiere resumen, se reporta el peor estado sin ocultar componentes: cualquier FAIL permanece FAIL; en ausencia de FAIL, cualquier UNKNOWN impide PASS global; NOT_COMPARABLE se mantiene explícito.

#### F. Límites

Estos predicados definen criterios de adjudicación, no valores concretos, snapshots, fuentes, mappings físicos, resultados ni truth. No definen todavía tolerancias/oráculo técnico ni predicados de compatibilidad FP-04, seguridad FP-05, aplicación FP-06 o verificación post-aplicación FP-07. No completan IAM ni autorizan fixtures, parser, validator, implementación, Design Freeze o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## 15.4. Aceptación DEC-C10-085 — adjudicación PAR C_SRC→F1/A1

**Estado:** ACCEPTED — DOCUMENTAL. Véase `00_GOVERNANCE/decisions/DEC-C10-085_PAR_F1_A1_ADJUDICATION_PREDICATES_ACCEPTANCE.md`.

Se acepta §15.3 con reconciliación obligatoria de sus cinco familias organizadoras con el catálogo SM/FP aceptado por DEC-C10-055. Las familias no crean predicados confirmatorios duplicados ni permiten doble contabilización de una misma discrepancia. Se conserva la primacía FP correspondiente: cobertura estructural no sustituye equivalencia semántica; tipo/esquema y significado se distinguen; FP-06 verifica aplicación y FP-07 observa estado aplicado.

F1 y A1 se adjudican independientemente por parámetro/regla, con identidad exacta de CMP, snapshots, etapa, ruta, scope, registros y mapping versionado. El resultado es un vector de estados por predicado, sin compensación entre rutas.

Se mantienen las reglas BOOL/ENUM, preservación RUL, estados y evidencia de §15.3. PASS requiere observación, cobertura y evidencia suficientes; FAIL requiere contradicción demostrada con cobertura suficiente; falta de información produce UNKNOWN; incompatibilidad sin mapping aprobado produce NOT_COMPARABLE; NA solo procede por inaplicabilidad ex ante y no aplica al contrato base.

Esta aceptación no define mappings físicos, valores observados, tolerancias ni oráculo; no sella IAM ni autoriza fixtures, parser, validator, implementación, Design Freeze o ejecución científica.

## 15.5. Predicados candidatos de comparación F1/A1→destino declarado F2/A2

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Especializa DEC-C10-083/084/085. No adjudica observaciones ni demuestra aplicación efectiva.

### A. Unidad de comparación

Se mantienen dos comparaciones independientes:

- Ruta F: `F1_S2 → F2_DST_DECL`.
- Ruta A: `A1_S1 → A2_DST_DECL`.

Cada comparación fija contrato/versión, instancia/versión, CMP owner y NODE anchor por snapshot, snapshot y registro intermedio, snapshot y registro destino declarado, `stage_key`, `route_id/route_record_id`, `coverage_scope_id`, `parameter_key/rule_id` y `mapping_id/version`. No se infiere identidad por nombre, posición, timestamp ni semejanza de valores.

### B. Dos dimensiones no compensables

**1. Conformidad semántica del destino declarado (`P-DECL`).** Comprueba si la configuración declarada F2/A2 conserva el significado lógico de la salida intermedia correspondiente. Para cada PAR evalúa separadamente estado, tipo/dominio y valor semántico; para RUL evalúa identidad lógica, efecto REQUIRE, operandos, scope y semántica normalizada mediante mapping aprobado. Se aplican DEC-C10-068 y DEC-C10-084: BOOL exacto; ENUM mediante biyección total, inyectiva y versionada sobre STANDARD/READ_ONLY/DISABLED. La conformidad se calcula por parámetro/regla y ruta.

**2. Conformidad probatoria de la transición (`P-TRANS`).** Comprueba que existe evidencia íntegra y trazable del proceso de transformación que vincula la salida F1/A1 exacta con el artefacto declarado F2/A2 exacto, y que el artefacto declarado evaluado es realmente el producto declarado de esa transición. Requiere registros de proceso, entradas/salidas identificadas, mapping/versiones, procedencia, captura e integridad, con cobertura suficiente. La mera equivalencia entre dos artefactos no prueba que el proceso haya producido el destino; un enlace o declaración sin evidencia del proceso no basta.

Ambas dimensiones se reportan por separado. `P-DECL=PASS` no implica `P-TRANS=PASS`; un resultado no compensa al otro. F y A tampoco se compensan.

### C. Predicados por objeto

Para cada ruta `r∈{F,A}`:

- `P-DECL-STATE(k,r)`: estado PAR intermedio/destino declarado.
- `P-DECL-VALUE(k,r)`: tipo, dominio y significado lógico BOOL/ENUM.
- `P-DECL-RUL(r)`: preservación semántica de `RUL-SVC-ENABLE-PROFILE-01`.
- `P-DECL-BIND(r)`: identidad CMP, snapshots, registros, etapa, ruta, scope y mapping exactos.
- `P-TRANS-LINEAGE(r)`: evidencia de que la transición identificada produjo el artefacto declarado.
- `P-TRANS-EVID(r)`: integridad, procedencia, suficiencia y correspondencia de la evidencia con la afirmación.

Estas etiquetas son descomposición operativa de las familias SM/FP existentes, no autorización para crear predicados confirmatorios duplicados ni doble contabilización. La matriz debe conservar la asignación primaria SM/FP vigente.

### D. Resultados

Cada predicado recibe uno de los estados:

- `PASS`: equivalencia semántica o lineage probatorio demostrado, según la dimensión evaluada, con identidad, mapping, observación, cobertura y evidencia suficientes.
- `FAIL`: diferencia semántica o contradicción de lineage demostrada con cobertura suficiente.
- `UNKNOWN`: artefacto, observación, cobertura, mapping, lineage o evidencia insuficientes.
- `NOT_COMPARABLE`: versiones/namespaces incompatibles sin mapping aprobado.
- `NA`: inaplicabilidad ex ante justificada; no admisible para estos PAR/RUL en las rutas del contrato base.

La falta de registro no demuestra ABSENT ni demuestra que la transición no ocurrió. FAIL requiere contradicción o ausencia exhaustivamente demostrada dentro de un universo/cobertura cerrados.

### E. Frontera con aplicación efectiva

`F2_DST_DECL` y `A2_DST_DECL` son configuraciones declaradas. Ningún resultado de §15.5 acredita que se instalaron, activaron o quedaron efectivamente vigentes. La aplicación y observación post-aplicación pertenecen a los predicados FP-06/FP-07 y a las etapas `F2_DST_APPLIED`/`A2_DST_APPLIED`. No se define aquí runtime, tolerancias, oráculo ni criterio de éxito de aplicación.

### F. Límites

Esta propuesta no define codificaciones ni mappings físicos, no crea registros reales, fixtures, columnas o FK, no sella IAM y no autoriza parser, validator, implementación, Design Freeze ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## 15.6. Aceptación DEC-C10-086 — conformidad destino declarado y transición F1/A1→F2/A2

**Estado:** ACCEPTED — DOCUMENTAL. Véase `00_GOVERNANCE/decisions/DEC-C10-086_PAR_DECLARED_DESTINATION_AND_TRANSITION_CONFORMANCE_ACCEPTANCE.md`.

Se acepta §15.5 para las rutas independientes F1_S2→F2_DST_DECL y A1_S1→A2_DST_DECL, con dos dimensiones no compensables:

- `P-DECL`: conformidad semántica del destino declarado respecto de la salida intermedia exacta, por parámetro/regla, estado, tipo/dominio/valor, RUL e identidad/alcance.
- `P-TRANS`: conformidad probatoria de la transición, con lineage íntegro y trazable que vincule entrada, proceso y artefacto destino declarado exacto.

La equivalencia de artefactos no demuestra por sí sola que el proceso produjo el destino. F y A se adjudican independientemente y conservan vectores de resultado por predicado. Se aplican DEC-C10-068/084 y la reconciliación SM/FP, sin duplicidad ni doble contabilización.

PASS requiere demostración suficiente; FAIL, contradicción demostrada con cobertura suficiente; UNKNOWN, información/cobertura/evidencia insuficiente; NOT_COMPARABLE, incompatibilidad sin mapping aprobado; NA, inaplicabilidad ex ante (no admisible para PAR/RUL del contrato base).

F2/A2 declaradas no demuestran aplicación efectiva; FP-06/FP-07 y F2/A2 applied permanecen fuera de este bloque. Esta aceptación no define mappings físicos, no sella IAM ni autoriza parser, validator, implementación, Design Freeze o ejecución científica.

## 15.7. Propuesta de adjudicación de aplicación efectiva y verificación post-aplicación

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Especializa la frontera de §15.5–15.6 y reutiliza FP-06, FP-07 y FP-08 según la reconciliación SM/FP aceptada en DEC-C10-055. No crea familias ni predicados confirmatorios paralelos.

### A. Unidad y rutas independientes

Se evalúan separadamente:

- F: `F2_DST_DECL → F2_DST_APPLIED`.
- A: `A2_DST_DECL → A2_DST_APPLIED`.

Cada evaluación fija contract_id/version, instance_id/version, CMP owner/NODE anchor, artefacto declarado y su registro exacto, evento de aplicación, destino/environment identity, snapshot post-aplicación y registro exacto, `stage_key`, route_id/route_record_id, coverage_scope_id, mapping_id/version y evidencia. No se infiere identidad por nombre, timestamp, ruta familiar F/A ni similitud del contenido.

### B. Separación de funciones FP-06 / FP-07 / FP-08

**1. FP-06 — aplicación efectiva del paquete.** Comprueba que el paquete/configuración declarada exacta fue objeto de una operación de aplicación identificable sobre el destino previsto, y que existe evidencia del resultado de esa operación. Requiere vincular el artefacto declarado, versión/hash/provenance, operación, target/environment identity, alcance y resultado. Un plan, intención, comando preparado, declaración de éxito sin registro trazable o mera existencia del artefacto no demuestra aplicación. Un código de salida aislado tampoco demuestra que el estado resultante satisfaga el contrato.

**2. FP-07 — verificación post-aplicación contra el contrato.** Comprueba mediante una captura/observación post-aplicación identificada que el estado realmente observado en el destino satisface el contrato declarado. La observación debe ser del destino y snapshot exactos, con cobertura suficiente para las propiedades aplicables. Los parámetros se evalúan con FP-01/FP-03 según validez formal y semántica; relaciones con FP-02; compatibilidad con FP-04; seguridad efectiva con FP-05 solo cuando esté activada y sea aplicable. FP-07 no sustituye esas familias ni permite declarar conformidad total si una propiedad obligatoria queda UNKNOWN/FAIL.

**3. FP-08 — procedencia, identidad y reproducibilidad probatoria.** Asegura que el paquete, evento de aplicación, destino, snapshot y evidencia observacional son artefactos identificables, versionados, íntegros y trazables. FP-08 soporta la adjudicación de FP-06/FP-07, pero no reemplaza la evidencia de aplicación ni la observación del estado.

La misma evidencia puede informar más de una familia cuando sea legítimo, pero cada afirmación debe conservar su vínculo probatorio y predicado primario. Un único defecto no se cuenta dos veces en el agregado confirmatorio.

### C. Reglas sustantivas del contrato base

- Los dos PAR nucleares deben observarse en el estado post-aplicación con la aplicabilidad/obligatoriedad ex ante de DEC-C10-083: estado VALUE, BOOL exacto para ENABLED y biyección ENUM total/versionada para PROFILE conforme a DEC-C10-084.
- La regla `RUL-SVC-ENABLE-PROFILE-01` debe estar presente y conservar la semántica REQUIRE/scope/operandos. Su preservación declarativa no demuestra evaluación/aplicación efectiva; la comprobación post-aplicación debe usar el oráculo/observación aprobado cuando exista.
- La conformidad de configuración no implica compatibilidad ambiental FP-04 ni seguridad FP-05. No se incorporan silenciosamente permisos, recursos o runtime al objeto de configuración.
- Una operación FP-06 exitosa no implica FP-07 PASS. FP-07 PASS no reconstruye por sí solo la procedencia del paquete ni demuestra qué operación lo aplicó (FP-06/08).
- F y A no se compensan. Los resultados se conservan por ruta, parámetro/regla y familia.

### D. Adjudicación

Cada familia/predicado recibe:

- `PASS`: aplicación demostrada (FP-06), y/o estado post-aplicación observado y conforme (FP-07), con identidad, mapping, cobertura y evidencia suficientes para la afirmación concreta.
- `FAIL`: no aplicación o aplicación a destino equivocado demostrada con registro/cobertura exhaustivos; o estado post-aplicación que contradice una propiedad obligatoria del contrato.
- `UNKNOWN`: falta evento, destino, snapshot, observación, cobertura, evidencia, mapping u oráculo suficiente.
- `NOT_COMPARABLE`: incompatibilidad de versiones/namespaces sin mapping aprobado.
- `NA`: inaplicabilidad ex ante justificada; no admisible para FP-06/FP-07 ni para los dos PAR y RUL del contrato base en ambas rutas.

La falta de registro no demuestra que la aplicación no ocurrió. FAIL por no aplicación exige un registro autoritativo y exhaustivo del universo de operaciones/target o evidencia positiva de contradicción; de lo contrario UNKNOWN. Un exit code cero o log de herramienta sin captura independiente del estado no basta para FP-07 PASS.

### E. Resultado agregado y no compensación

Se reportan por separado `FP06_APPLY`, `FP07_POSTCHECK` y la validez probatoria FP-08, junto con el vector FP-01…05 aplicable al estado observado. No se fusionan en un booleano único que oculte la causa. Para una ruta, cualquier FAIL obligatorio permanece visible; en ausencia de FAIL, UNKNOWN impide declarar conformidad global PASS. La suficiencia de cobertura se informa aparte del estado semántico.

### F. Límites y no autorizaciones

Esta propuesta no selecciona herramienta/command de aplicación, protocolo de observación, oráculo, tolerancias, método de captura, runtime ni mapping físico. No crea registros observados, fixtures, columnas/FK ni nuevos predicados FP. No sella IAM ni autoriza parser, validator, scripts, implementación, Design Freeze, validación técnica, ejecución del control o experimento científico. `scientific_execution=false`; `execution_authorized=false`.


## 15.8. Aceptación DEC-C10-087 — aplicación efectiva y verificación post-aplicación

**Estado:** ACCEPTED — DOCUMENTAL. Véase `00_GOVERNANCE/decisions/DEC-C10-087_EFFECTIVE_APPLICATION_AND_POST_APPLICATION_VERIFICATION_ACCEPTANCE.md`.

Se acepta §15.7 para F2_DST_DECL→F2_DST_APPLIED y A2_DST_DECL→A2_DST_APPLIED, reutilizando FP-06 (aplicación efectiva), FP-07 (verificación post-aplicación) y FP-08 (procedencia/identidad/reproducibilidad) existentes. No se crean predicados confirmatorios paralelos.

FP-06 requiere evidencia trazable del evento que aplicó el paquete exacto al destino identificado; plan, intención, existencia del paquete o exit code aislado no bastan. FP-07 requiere observación post-aplicación del destino/snapshot exactos y evaluación mediante FP-01…05 aplicables; log o exit code sin observación del estado no bastan. FP-08 soporta identidad/procedencia/integridad, sin sustituir FP-06/07.

F y A se adjudican independientemente. La falta de registro no demuestra no aplicación: UNKNOWN salvo evidencia autoritativa/exhaustiva o contradicción positiva. FAIL exige contradicción o no aplicación demostrada con cobertura suficiente. FP-06 PASS no implica FP-07 PASS. Se reportan FP06_APPLY, FP07_POSTCHECK, FP-08 y vector FP-01…05, sin doble contabilización de un defecto.

La configuración declarada no equivale a aplicada. Esta aceptación no define herramienta, protocolo de observación, oráculo, tolerancias ni mapping físico; no sella IAM ni autoriza parser, validator, implementación, Design Freeze o ejecución científica.

## 15.9. Integración de adjudicación por etapa y ruta

**Estado:** ACCEPTED — DOCUMENTAL por DEC-C10-088. Este apartado integra, sin sustituir, los contratos previos.

El vector por ruta F/A conserva tres tramos no transferibles: (1) `C_SRC→F1_S2/A1_S1`, DEC-C10-085; (2) `F1_S2/A1_S1→F2_DST_DECL/A2_DST_DECL`, DEC-C10-086 con `P-DECL` y `P-TRANS`; (3) `F2_DST_DECL/A2_DST_DECL→F2_DST_APPLIED/A2_DST_APPLIED`, DEC-C10-087 con FP-06/07/08. No se colapsan en una puntuación ni se compensan entre rutas.

`stage_key` identifica la etapa de configuración; no equivale al reloj DGP `t0…t9`, a SNAPSHOT.phase ni a paso hipotético k. Cada registro debe enlazar explícitamente etapa, snapshot/registro, ruta, unidad, instante de generación/observación y mapping versionado. La evidencia no se transfiere entre etapas ni entre F y A.

La conformidad de configuración no prueba por sí sola ACC/APP/REL/DEP/Reach; FP-06 no implica FP-07; FP-07 evalúa estado post-aplicación mediante FP-01…05 aplicables; FP-08 soporta identidad/procedencia sin sustituir evento u observación. La falta de registro produce UNKNOWN salvo contradicción o ausencia exhaustivamente demostrada. Véase §14 de la matriz temporal.

No se crean predicados FP/SM, columnas/FK o mappings físicos. No se sella IAM ni se autoriza implementación o ejecución científica.
