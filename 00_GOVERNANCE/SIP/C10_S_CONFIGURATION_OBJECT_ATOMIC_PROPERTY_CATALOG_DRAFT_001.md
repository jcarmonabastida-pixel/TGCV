# C10-S — Catálogo candidato de propiedades atómicas del objeto de configuración

**ID:** C10-S-CONFIG-ATOMIC-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** catálogo candidato derivado de DEC-C10-052; NO aprobado como contrato confirmatorio, NO congelado, NO implementado, NO validado.  
**Base:** DEC-C10-051 (microdominio Opción A) y DEC-C10-052 (paquete de configuración de servicio software; seis elementos iniciales).

## 1. Propósito y límite

Este catálogo traduce la estructura conceptual seleccionada del objeto en propiedades candidatas observables. Su objetivo es preparar la especialización de FP-01…FP-08 y SM-01…SM-10 sin inventar un producto, formato, lenguaje de configuración ni dominio operativo concreto.

Los identificadores y predicados de este documento son **propuestas de operacionalización**. No se asignan todavía obligatoriedad, aplicabilidad universal, tolerancias, valores admisibles, cardinalidades numéricas, dominios de enumeración ni truth del DGP. Cada instancia de configuración deberá declarar ex ante qué propiedades aplican y qué contrato concreto las define.

La estructura del objeto contiene seis elementos: componente; parámetros tipados; referencias; reglas/restricciones; políticas asociadas; metadatos contractuales. Los recursos/capacidad, permisos efectivos, dependencias instaladas y estado operativo de los entornos permanecen fuera del objeto.

## 2. Regla para convertir un candidato en predicado confirmatorio

Cada propiedad seleccionada deberá completarse con:
1. identificador estable y versión del predicado;
2. elemento del objeto y alcance exacto;
3. definición operacional y dominio de valores;
4. condición de aplicabilidad preespecificada;
5. fuente de verdad contractual y snapshot al que aplica;
6. mapping origen→destino permitido;
7. criterio de conformidad y tolerancia, si procede;
8. método de observación independiente del conversor;
9. cobertura requerida y regla de evidencia;
10. regla trivalente 1/0/? y NA justificado;
11. errores de clasificación previsibles y su tratamiento;
12. vínculo con FP-01…FP-08, sin doble contabilizar una misma propiedad.

Una propiedad no está confirmatoriamente definida mientras falte alguno de los elementos necesarios para adjudicarla sin usar Outcome/Value ni conocer el brazo/ruta cuando ello pueda sesgar la evaluación.

## 3. Catálogo de candidatos

### 3.1 Componente

| ID | Propiedad candidata | Predicado conceptual | Familia principal | Estado |
|---|---|---|---|---|
| CMP-01 | Correspondencia de identidad funcional | Cada componente obligatorio de origen se corresponde con exactamente el componente destino declarado por el mapping, o con una composición explícita permitida | FP-03 / SM-01 | Candidato; mapping abierto |
| CMP-02 | Conservación de clase funcional | La clase/rol funcional contractual del componente no cambia, salvo transformación explícitamente autorizada | FP-03 / SM-01 | Candidato; taxonomía abierta |
| CMP-03 | Unicidad/duplicación funcional | No se omite ni duplica un componente cuando ello altera la identidad o el comportamiento contractual | FP-02 + FP-03 | Candidato; cardinalidad abierta |

### 3.2 Parámetros tipados

| ID | Propiedad candidata | Predicado conceptual | Familia principal | Estado |
|---|---|---|---|---|
| PAR-01 | Correspondencia de clave | Cada parámetro obligatorio tiene una correspondencia de destino inequívoca o una regla de mapping compuesta aprobada | FP-03 / SM-01 | Candidato |
| PAR-02 | Preservación de tipo | El tipo destino conserva el significado del tipo origen bajo la regla de conversión declarada | FP-03 / SM-02 | Candidato; sistema de tipos abierto |
| PAR-03 | Preservación de valor y dominio | El valor destino representa el mismo valor funcional dentro del dominio contractual | FP-03 / SM-02 | Candidato; dominios/tolerancias abiertos |
| PAR-04 | Unidad y escala | Unidad, escala, precisión y redondeo se preservan o convierten mediante regla explícita semánticamente válida | FP-03 / SM-02 | Condicional; solo si la propiedad tiene unidad/escala |
| PAR-05 | Distinción ausencia/null/default | Las distinciones declaradas significativas entre propiedad ausente, null, vacío y default se conservan | FP-03 / SM-04 | Candidato; semántica de cada estado abierta |
| PAR-06 | Obligatoriedad y opcionalidad | La condición de requerido/opcional se conserva o se transforma mediante regla contractual explícita | FP-03 / SM-04 | Candidato |

### 3.3 Referencias y dependencias declaradas

| ID | Propiedad candidata | Predicado conceptual | Familia principal | Estado |
|---|---|---|---|---|
| REF-01 | Correspondencia de extremos | Cada referencia obligatoria apunta al componente/recurso destino que corresponde al extremo origen | FP-03 / SM-03 | Candidato; mapping abierto |
| REF-02 | Tipo y dirección de relación | Tipo, dirección y papel funcional de la relación se conservan | FP-03 / SM-03 | Candidato |
| REF-03 | Multiplicidad | Cardinalidad/multiplicidad permitida se conserva dentro del contrato | FP-02 + FP-03 / SM-05 | Candidato; límites abiertos |
| REF-04 | Integridad referencial | No quedan referencias obligatorias rotas o ambiguas tras la aplicación | FP-02 y FP-07; impacto FP-03 si cambia significado | Candidato |
| REF-05 | Dependencia declarada vs instalada | La declaración de dependencia se conserva, sin inferir que la dependencia esté instalada o disponible en destino | FP-03 para declaración; entorno/C_dep por separado | Límite explícito |

### 3.4 Reglas y restricciones declarativas

| ID | Propiedad candidata | Predicado conceptual | Familia principal | Estado |
|---|---|---|---|---|
| RUL-01 | Conservación de condición lógica | La condición mantiene operadores, operandos, cuantificadores y lógica contractual | FP-03 / SM-07 | Candidato; lenguaje/gramática abiertos |
| RUL-02 | Conservación de ámbito | La regla aplica al mismo componente, parámetro, evento o contexto declarado | FP-03 / SM-07 | Candidato |
| RUL-03 | Conservación de efecto | La consecuencia/acción declarada de la regla conserva su significado | FP-03 / SM-07 | Candidato |
| RUL-04 | Precedencia y composición | Orden/precedencia entre reglas se conserva cuando modifica el resultado funcional | FP-03 / SM-06/07 | Condicional; semántica de orden abierta |
| RUL-05 | Vigencia temporal | Inicio, fin, duración o zona temporal se conservan cuando el dominio les atribuye significado | FP-03 / SM-08 | Condicional |

### 3.5 Políticas asociadas

| ID | Propiedad candidata | Predicado conceptual | Familia principal | Estado |
|---|---|---|---|---|
| POL-01 | Correspondencia de sujeto/rol | Los sujetos/roles declarados mantienen su correspondencia funcional | FP-03 / SM-09 | Candidato; identidad de roles abierta |
| POL-02 | Alcance de autorización declarada | El ámbito y recurso al que se aplica la política se conserva | FP-03 / SM-09 | Candidato |
| POL-03 | Semántica allow/deny | El efecto de permitir/denegar y su precedencia se conserva | FP-03 / SM-09 | Candidato |
| POL-04 | Separación entre política declarada y permiso efectivo | La migración conserva el contenido declarado, pero no se infiere que el entorno conceda efectivamente el permiso | FP-03 frente a condición de entorno y FP-05 | Límite explícito |
| POL-05 | Cumplimiento de seguridad destino | La política aplicada satisface los requisitos de seguridad del contrato | FP-05, no duplicar en FP-03 | Requiere política de seguridad explícita |

### 3.6 Metadatos contractuales

| ID | Propiedad candidata | Predicado conceptual | Familia principal | Estado |
|---|---|---|---|---|
| MET-01 | Versión del contrato/esquema | La versión fuente y la versión destino se identifican y se aplica una regla de compatibilidad/mapping declarada | FP-01/FP-04 | Candidato; versiones abiertas |
| MET-02 | Procedencia | Se conserva la trazabilidad de origen, mapping, transformación y aplicación | FP-08 | Candidato; contrato de procedencia abierto |
| MET-03 | Extensiones desconocidas | Los elementos desconocidos se preservan, rechazan o ignoran solo según política explícita; no se descartan silenciosamente | FP-03 / SM-10 | Candidato; política abierta |
| MET-04 | Identidad de artefacto vs identidad funcional | Hash/nombre/serialización se usan como identificadores de artefacto, no como prueba de equivalencia semántica | FP-08 e identidad/versionado | Regla de interpretación |

## 4. Matriz de cobertura de dimensiones semánticas

| Dimensión | Propiedades candidatas relacionadas | Aplicabilidad inicial |
|---|---|---|
| SM-01 Identidad/significado | CMP-01/02, PAR-01 | Candidata central |
| SM-02 Valores/tipos/dominios | PAR-02/03/04 | Candidata central |
| SM-03 Relaciones/referencias | REF-01/02/04 | Candidata central |
| SM-04 Ausencia/null/default | PAR-05/06 | Candidata central |
| SM-05 Cardinalidad | CMP-03, REF-03 | Condicionada a colecciones/relaciones con multiplicidad |
| SM-06 Orden/precedencia | RUL-04 | Condicionada a orden funcional |
| SM-07 Reglas operativas | RUL-01/02/03/04 | Condicionada a presencia de reglas |
| SM-08 Tiempo/vigencia | RUL-05 | Condicionada a semántica temporal |
| SM-09 Permisos/control | POL-01/02/03 | Condicionada a inclusión de políticas en el paquete |
| SM-10 Extensiones desconocidas | MET-03 | Condicionada a extensibilidad del formato/contrato |

La clasificación «candidata central» no significa obligatoriedad confirmatoria ya aprobada. Solo indica que la dimensión parece intrínseca al contenido conceptual seleccionado y deberá resolverse en la especificación del dominio. Ninguna propiedad pasa a obligatoria por aparecer en esta tabla.

## 5. Fronteras entre familias FP

Para evitar duplicación y circularidad:
- **FP-01 (esquema/tipos estructurales):** valida conformidad formal con el contrato de representación. PAR-02 puede alimentar FP-03 solo cuando el tipo tiene semántica funcional, no por simple igualdad de etiquetas.
- **FP-02 (integridad):** valida consistencia estructural y referencias. REF-04 y CMP-03 no se cuentan dos veces; su efecto semántico se registra en FP-03 solo si cambia el significado o función.
- **FP-03 (preservación semántica):** compara significado funcional contractual de origen y destino, con mappings explícitos.
- **FP-04 (compatibilidad):** comprueba compatibilidad del paquete/versión con el entorno destino; no demuestra preservación semántica.
- **FP-05 (seguridad):** evalúa política de seguridad del resultado. Preservar fielmente una política no implica que sea segura.
- **FP-06 (aplicación efectiva):** verifica que el paquete se aplicó; no demuestra que lo aplicado sea semánticamente correcto.
- **FP-07 (verificación post-aplicación):** observa el estado final frente al contrato; reutiliza criterios FP-01…05 sin sustituirlos.
- **FP-08 (procedencia/reproducibilidad):** conserva evidencia y trazabilidad de la evaluación; no es por sí sola una propiedad funcional de la configuración.

## 6. Regla de evaluación propuesta

Para cada propiedad seleccionada y aplicable:
- **1:** criterio contractual satisfecho con evidencia y cobertura suficientes.
- **0:** incumplimiento contractual confirmado.
- **?:** evidencia insuficiente, mapping ambiguo, cobertura incompleta o contradicción no resuelta.
- **NA:** solo cuando la no aplicabilidad fue preespecificada y justificada en el contrato de la instancia.

No se agregan puntuaciones compensatorias. F* solo puede adjudicarse cuando todas las propiedades obligatorias aplicables tienen estado concluyente; cualquier obligatoria 0 implica F*=0; ausencia de 0 pero alguna obligatoria ? implica F*=?.

## 7. Decisiones pendientes para cerrar el catálogo

1. Delimitar el tipo de servicio y la clase de configuración abstracta, sin elegir producto/plataforma.
2. Definir contrato fuente y contrato destino y sus versiones.
3. Resolver semántica de parámetros, tipos, unidades, defaults, ausencia y null.
4. Definir taxonomía mínima de componentes, referencias y reglas.
5. Decidir si políticas asociadas forman parte del objeto mínimo confirmatorio o son un módulo condicional.
6. Decidir qué dimensiones SM-05…SM-10 se incluyen en el DGP base y cuáles quedan en escenarios de sensibilidad/adversariales.
7. Definir mappings permitidos y criterios de pérdida/transformación.
8. Asignar obligatoriedad/NA por propiedad ex ante.
9. Fijar cobertura, tolerancias y método de observación.
10. Reconciliar las propiedades con F1/F2/A1/A2, sin asumir sus mecanismos.
11. Completar el oráculo independiente y su evaluación de error.

## 8. Dictamen

Se ha producido una primera atomización candidata del objeto seleccionado, con propiedades vinculadas a sus seis elementos y límites entre FP-01…FP-08. Es suficiente para guiar la siguiente ronda de especificación, pero no para declarar FP-03 o F* operacionalmente cerrados.

**Estado:** OBJECT CLASS SELECTED; INITIAL SIX-ELEMENT STRUCTURE ADOPTED; ATOMIC PROPERTY CATALOG DRAFTED; OBLIGATORINESS/APPLICABILITY OPEN; SOURCE/DESTINATION CONTRACTS OPEN; MAPPINGS OPEN; ORACLE NOT VALIDATED; NO TECHNICAL VALIDATION; NO INDEPENDENT REVIEW; NO EMPIRICAL EVIDENCE; NO EXECUTION AUTHORIZATION.


## 9. Reconciliación con FP-01…FP-08

La asignación de familia primaria/secundaria y la separación de predicados compuestos se desarrolla en `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`. El catálogo original se conserva como catálogo candidato; la reconciliación no eleva propiedades a obligatorias. En especial, CMP-03/REF-03 separan cardinalidad/integridad de impacto semántico; PAR-02/PAR-06 separan validez formal y significado; REF-04 queda en FP-02; POL-05 queda en FP-05; MET-02/04 quedan en FP-08.


## 10. Estado decisional y matriz de aplicabilidad

La reconciliación de familias fue aceptada mediante DEC-C10-055. La obligatoriedad y aplicabilidad concreta por propiedad no se infiere de esta aceptación; se desarrolla separadamente en `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`. CMP/PAR/REF/RUL siguen siendo elementos constitutivos del DGP base según DEC-C10-053; la cardinalidad de instancias por clase, los predicados condicionales y NA deben declararse ex ante en IAM. POL permanece fuera del núcleo confirmatorio mínimo. MET-01/MET-02 obligatorios para trazabilidad.


## 11. DEC-C10-056 — cardinalidad de clases

La cardinalidad base queda fijada por DEC-C10-056: CMP≥1, PAR≥1, RUL≥1; REF≥0 con declaración IAM ex ante y cobertura exhaustiva; POL≥0 ausente por diseño salvo módulo condicional predeclarado; MET obligatorio. La ausencia de CMP/PAR/RUL es SCOPE_ERROR, no NA. Véase el contrato abstracto `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`. Esta decisión no convierte cada propiedad atómica en obligatoria ni fija máximos/valores.


## 12. Especialización candidata del catálogo PAR: claves lógicas mínimas

**Estado histórico:** propuesta documental original, posteriormente acotada por DEC-C10-068; no es roster vigente completo ni instancia serializada.

Se proponen tres roles de clave para una unidad lógica de servicio, no nombres de campos de un producto ni una serialización:

| ID lógico | Rol semántico | Tipo candidato | Requiredness candidato | Dominio abstracto | Estados admisibles propuestos |
|---|---|---|---|---|---|
| PAR-SVC-ENABLED | Activación lógica del servicio | BOOL | REQUIRED | {false,true} | VALUE; DEFAULT solo si el contrato declara/hereda explícitamente el default; ABSENT/NULL inválidos |
| PAR-SVC-PROFILE | Perfil funcional de operación/configuración | ENUM | REQUIRED | D_profile finito, con al menos dos símbolos abstractos distinguibles; sin orden implícito | VALUE; DEFAULT solo con contrato; ABSENT/NULL inválidos |
| PAR-SVC-RETRY-COUNT | Número configurado de reintentos | INT | OPTIONAL | D_retry={n∈Z: 0≤n≤N_retry_max}; N_retry_max finito y por fijar | ABSENT, VALUE; DEFAULT solo con contrato; NULL no admitido salvo decisión explícita |

Los nombres son etiquetas de trabajo para roles semánticos, no claves literales de configuración. PROFILE no presupone nombres ni significados de perfiles reales. RETRY-COUNT es un parámetro de configuración del servicio, no disponibilidad/capacidad de recursos P1. Si la unidad lógica elegida no posee una semántica contractual de reintentos, este slot debe sustituirse antes de congelar la instancia, no forzarse.

### 12.1 Tipos del núcleo y extensiones

El conjunto de tipos admitidos por el contrato abstracto sigue siendo BOOL, INT, DECIMAL, ENUM, STRING y REF. La propuesta de roster base instancia BOOL, ENUM e INT para mantener el núcleo parsimonioso. No exige que toda instancia use todos los tipos admitidos.

- DECIMAL: slot condicional (p. ej. umbral cuantitativo) solo si una regla constitutiva lo necesita; escala, precisión, unidad y redondeo deben definirse por clave.
- STRING: slot condicional solo si el texto tiene significado funcional contractual; etiquetas descriptivas sin efecto funcional pertenecen a MET, no se añaden para aumentar cobertura de tipos.
- REF: usar la clase REF para relaciones/dependencias ordinarias. Un PAR de tipo REF solo se admite si el contrato demuestra que es un valor escalar configuracional y no duplica la misma relación.
- ARRAY/MAP/BINARY/fecha-hora y tipos definidos por usuario siguen fuera del núcleo primitivo conforme a la propuesta gramatical vigente.

### 12.2 Reglas comunes por clave

Cada registro PAR debe fijar key estable, owner CMP, type, requiredness, dominio, estado, value cuando proceda, default contract, versión y procedencia. Los estados ABSENT/NULL/DEFAULT/VALUE no se colapsan. Si state=DEFAULT, default_kind=DECLARED|INHERITED; la resolución DEFAULT_ENV_RESOLVED se observa en E_dst, fuera de PAR.

Los estados admisibles de la tabla son candidatos por clave, no una relajación del enum global. Un estado no admitido es incumplimiento formal si está observado; si la evidencia no permite decidirlo, queda ?. ABSENT en OPTIONAL significa ausencia explícita del parámetro, no default ambiental. El comportamiento efectivo de E_dst se mide separadamente.

### 12.3 Criterio de parsimonia y condición de reemplazo

Tres slots cubren tres semánticas diferenciables: activación booleana, selección categórica y límite entero opcional. No se afirma que sean universales a todo servicio software. Antes de fijar instancia debe verificarse que los tres pertenecen realmente al contrato P0 de la unidad lógica; si no, se reemplaza el slot manteniendo la misma justificación de tipo/función y sin trasladar recursos, permisos efectivos, runtime o estado externo desde P1.

La propuesta no fija valores, símbolos ENUM, N_retry_max, versión, conversión, mapping, unidades, tolerancias ni truth. Tampoco resuelve todavía la regla RUL constitutiva que debe relacionar o restringir propiedades: RUL≥1 sigue siendo obligatorio por DEC-C10-056 y su contenido sustantivo queda abierto.

## 13. Contrato mínimo de RUL para la instancia sintética aceptada

DEC-C10-056 exige RUL≥1; DEC-C10-054 fija el presupuesto y la semántica general del núcleo. DEC-C10-068 acepta la instancia RUL-SVC-ENABLE-PROFILE-01 como regla constitutiva del servicio lógico sintético: ENABLED=true implica PROFILE∈{STANDARD,READ_ONLY}, efecto REQUIRE, con ENABLED=false no restringido por esta implicación. La regla tiene un estado permitido y un violador conocido dentro del dominio finito estipulado ex ante.

Esta aceptación es conceptual y documental. No demuestra ejecución del AST, preservación en mapping, aplicación en destino ni corrección de un parser/oráculo. Owner lógico y scope están definidos; identidad/versionado CMP de instancia, serialización, IAM por escenario, mapping, cobertura y adjudicación permanecen abiertos.
## 14. RUL constitutiva del servicio sintético: distinción de identificadores

RUL-01/02/03 del catálogo son propiedades de preservación (condición lógica, ámbito y efecto), no la identidad de una regla de instancia. La regla de instancia aceptada conceptualmente por DEC-C10-068 se denomina RUL-SVC-ENABLE-PROFILE-01 y está descrita en `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`. Su condición es ENABLED=true ⇒ PROFILE∈{STANDARD,READ_ONLY}, con PROFILE={STANDARD,READ_ONLY,DISABLED}. El identificador de instancia no debe confundirse con los predicados de preservación. Estado: regla sintética aceptada conceptualmente por DEC-C10-068; owner lógico y scope definidos; identidad/versionado de instancia, mapping y oráculo OPEN.

**Precedencia decisional:** la tabla histórica de §12 queda supersedida en lo relativo a RETRY-COUNT y al estado de ENABLED/PROFILE. DEC-C10-068 acepta solo PAR-SVC-ENABLED BOOL y PAR-SVC-PROFILE ENUM como núcleo; PAR-SVC-RETRY-COUNT queda excluido. La identidad/versionado CMP candidato se documenta por separado en `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md`; no queda aceptado por DEC-C10-068.

## 15. Reconciliación de roster del catálogo atómico tras DEC-C10-068/069

La fila histórica PAR-SVC-RETRY-COUNT de §12 se conserva como antecedente trazable, pero queda **SUPERSEDED FOR THE BASE CONFIRMATORY INSTANCE** por DEC-C10-068. No es slot obligatorio ni opcional del roster funcional base; no debe poblarse ni usarse para satisfacer PAR≥1 en la instancia aceptada. Cualquier futura extensión requeriría decisión/versionado y justificación P0 explícitos.

El roster PAR funcional vigente de la instancia aceptada se limita a PAR-SVC-ENABLED BOOL {false,true} y PAR-SVC-PROFILE ENUM {STANDARD, READ_ONLY, DISABLED}. No existe DEFAULT contractual aceptado para ninguno. La regla RUL-SVC-ENABLE-PROFILE-01 vincula ambos. El catálogo histórico no constituye evidencia de valores presentes en C_src/S1/S2/C_dst.

**Estado:** precedencia documental reconciliada; no se alteran IDs/valores aceptados ni se crean filas observadas.

## 16. Reconciliación del catálogo REF con UDG-04 — propuesta (2026-11-07)

REF-01…REF-05 conservan su alcance candidato. Se precisa que REF es un objeto de relación declarado en el paquete de configuración, con identidad propia y dos extremos (o estructura n-aria expresamente modelada); no es sinónimo de EDGE, FK U_G ni CLAIM_EVIDENCE_LINK.

La especialización propuesta de REF incluye: identidad lógica/record exacto; owner/source endpoint y target endpoint tipados; relation_type; direction; role; multiplicity/cardinality; integrity_rule; versión y provenance. La cardinalidad de extremos y la posibilidad de endpoint externo deben declararse por contrato/IAM; no se presume que todos los destinos pertenezcan a CMP/PAR/REF/RUL/MET.

REF→EDGE es mapping candidato sujeto a M versionado. Una relación binaria puede mapear a una EDGE atómica; split/merge o relación n-aria exige agrupación/parent identity explícita y conservación de extremos, dirección y multiplicidad. EDGE→REF no es inferencia automática.

Los roles MEMBER/OWNER/SOURCE/INCLUSION_RULE/EXCLUSION_RULE/DEPENDENCY/PROVENANCE citados en DEC-C10-076 siguen siendo ilustrativos, no enum aprobado. Se distinguen roles de referencia del envelope UDG y relaciones declaradas dentro de un objeto REF. Obligatoriedad, cardinalidad, dominio de roles y NA requieren IAM ex ante. No se cambia schema, catálogo de clases ni estado de aceptación.

## 17. DEC-C10-077 — aceptación conceptual REF↔UDG-04

Se acepta que REF sea objeto de relación del dominio con identidad propia y extremos tipados, separado de las referencias del envelope UDG y de FK/vínculos estructurales U_G. REF→EDGE requiere M explícito y versionado; no hay equivalencia automática ni 1:1 asumida. Las relaciones n-arias/split/merge requieren agrupación explícita. Los roles ilustrativos no son enum cerrado. La aceptación no fija cardinalidades, obligatoriedad, IAM, endpoints externos ni schema físico. REF-01…REF-05 siguen siendo propiedades candidatas, no PASS empírico ni freeze.
