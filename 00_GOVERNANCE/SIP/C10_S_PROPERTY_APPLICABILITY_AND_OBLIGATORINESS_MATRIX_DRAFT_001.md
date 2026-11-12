# C10-S — Matriz de obligatoriedad y aplicabilidad ex ante de propiedades

**ID:** C10-S-APPLICABILITY-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA OPERACIONAL — NO APROBADA / NO CONGELADA / NO IMPLEMENTADA.  
**Decisión precedente:** DEC-C10-055 (aceptación de reconciliación SM/FP).  
**Base:** DEC-C10-052/053/054; catálogo atómico; reconciliación SM/FP; matriz F*; matriz de mapping C_src→C_dst/M.

## 1. Propósito y regla de aplicación

Esta matriz determina cómo declarar ex ante la presencia, obligatoriedad y aplicabilidad de cada propiedad atómica en una instancia del DGP base. No convierte todo elemento conceptual del paquete en una obligación de que cada subpropiedad tenga un valor no vacío. Distingue:

1. **Elemento constitutivo del objeto:** su clase/campo forma parte del contrato del paquete (CMP, PAR, REF, RUL).
2. **Predicado obligatorio:** debe evaluarse para cada objeto/registro al que se aplica.
3. **Predicado condicional:** se activa solo si el disparador contractual existe y queda declarado antes de asignación/Outcome.
4. **NA legítimo:** la propiedad no pertenece al dominio definido de la instancia; exige condición y justificación ex ante.
5. **Desconocido (? ):** la propiedad es pertinente, pero no puede determinarse por falta de evidencia/cobertura; nunca es NA.

La ausencia de una instancia de una clase no prueba por sí sola NA. Se requiere inventario de cobertura y declaración explícita del dominio.

## 2. Contrato de instancia y momento de congelación

Antes de generar/asignar cualquier escenario se sella un **Instance Applicability Manifest (IAM)**, que contendrá:
- ID/versiones de contrato fuente, destino y mapping M;
- universo de componentes, parámetros, referencias y reglas;
- declaración de cardinalidad de cada clase, incluidos conjuntos vacíos;
- propiedad atómica, condición de activación, obligatoriedad y FP primario;
- NA permitido, fundamento de dominio y evidencia de cobertura;
- dominios/tipos/unidades/defaults y reglas de conversión;
- módulos POL y extensibilidad (MET-03) incluidos o excluidos;
- condiciones externas (E_dst, C_dep, recursos, permisos efectivos, runtime);
- identidad del oráculo, versión, reglas de cegamiento y evidencia;
- hash/identidad y timestamp del manifiesto.

El IAM se fija antes de Z/B y antes de Outcome/Value. Cualquier modificación posterior requiere nueva versión, motivo, timestamp, diff y clasificación como cambio preasignación o postasignación. Un cambio postasignación no puede reescribir retroactivamente la elegibilidad ni el denominador; se conserva como desviación/protocolo.

## 3. Matriz por propiedad atómica

Abreviaturas: **O** = obligatoria en los objetos a los que aplica; **C** = condicional al disparador; **NA** = no aplicable solo por regla ex ante; **?** = pertinente pero no adjudicable. La clase/familia constitutiva no se elimina por declarar una propiedad secundaria NA.

| ID | Regla propuesta | Disparador / dominio | FP primario | NA admisible |
|---|---|---|---|---|
| CMP-01 | O por cada componente incluido en el universo contractual | Todo componente fuente/destino inventariado | FP-03 | No para componentes dentro del scope; scope vacío requiere error de alcance |
| CMP-02 | O por cada componente | Toda clase/rol funcional declarada | FP-03 | Solo si el contrato demuestra que clase/rol no tiene semántica diferenciable; preferir simplificar catálogo antes del experimento |
| CMP-03 | C | Si cardinalidad, colección, unicidad o duplicación puede afectar contrato | FP-01/02; FP-03 secundario si impacto funcional | Sí, si el modelo de componente es singleton/no repetible y queda definido ex ante |
| PAR-01 | O por cada parámetro del universo | Cada clave declarada en contrato | FP-03 | No para claves dentro del scope; cero parámetros requiere justificar que el objeto no incluye configuración parametrizada |
| PAR-02 | O por cada parámetro | Todo parámetro tipado | FP-01 para validez formal; FP-03 para significado | No |
| PAR-03 | O por cada parámetro con estado/valor contractual | Todo parámetro; incluye ABSENT/NULL/DEFAULT/VALUE | FP-03 | Solo si se declara un parámetro puramente estructural sin valor/estado funcional, con fundamento |
| PAR-04 | C | Unidad, dimensión, escala, precisión o redondeo tiene significado | FP-03 | Sí si el tipo/dominio es adimensional o discreto sin unidad/escala, declarado ex ante |
| PAR-05 | O como discriminación de estados | Cada parámetro cuyo contrato admita más de un estado entre ABSENT/NULL/DEFAULT/VALUE | FP-03; FP-01 valida estado permitido | Si contrato restringe explícitamente a un único estado posible; la distinción no se presume relevante |
| PAR-06 | O por cada parámetro | Todo parámetro debe declarar REQUIRED/OPTIONAL/CONDITIONAL | FP-01 para esquema; FP-03 para semántica | No; la condición puede ser CONSTANT/NA solo si el dominio contractual no tiene esa dimensión, justificado |
| REF-01 | O por cada referencia declarada | Cada referencia en el universo; ambos extremos identificados | FP-03 | Si el inventario de referencias es genuinamente vacío y se acredita cobertura; no equivale a evidencia ausente |
| REF-02 | O por cada referencia declarada | Toda relación debe declarar tipo, dirección y rol | FP-03 | Solo si el contrato declara una referencia no direccional/no tipada, con semántica formal |
| REF-03 | C | Si el contrato admite multiplicidad >1, colecciones o cardinalidad funcional | FP-02; FP-03 si altera función | Sí para relaciones estrictamente 1:1/singleton fijadas ex ante |
| REF-04 | O por cada referencia declarada | Integridad/resolución de extremos en C_dst^applied | FP-02; FP-07 observa estado aplicado | No para referencias incluidas; inventario vacío se trata como REF-01 |
| REF-05 | O como regla de separación cuando hay dependencias declaradas | Cada dependencia REF; distinguir declaración de disponibilidad/instalación | FP-03 para semántica declarada; FP-04/C_dep para estado técnico | NA solo si no existe ninguna dependencia declarada, acreditado por inventario |
| RUL-01 | O por cada regla/restricción del universo | Cada AST declarado | FP-03; FP-01 valida AST | NA para predicado si se demuestra que no hay regla en el scope; el contrato RUL sigue declarado |
| RUL-02 | O por cada regla | Toda regla tiene ámbito explícito o GLOBAL explícito | FP-03; FP-01 estructura | No; GLOBAL es un valor válido, no NA |
| RUL-03 | O por cada regla | Toda regla tiene efecto declarado dentro de REQUIRE/FORBID | FP-03; FP-01 valida tipo/gramática | No para reglas presentes |
| RUL-04 | C | Dos o más reglas cuya precedencia/orden pueda cambiar resultado | FP-03 | Sí si hay una sola regla o semántica declarada conmutativa |
| RUL-05 | C | Regla con inicio/fin/duración/zona/ventana temporal significativa | FP-03; FP-04 para runtime/reloj | Sí si ninguna regla tiene semántica temporal, acreditado por catálogo |
| POL-01 | C, módulo POL excluido del núcleo mínimo por DEC-C10-053 | Solo si POL se incluye explícitamente en escenario secundario | FP-03 | Sí en núcleo base, declarando POL_ABSENT_BY_DESIGN |
| POL-02 | C | Solo si módulo POL está incluido y existe ámbito de autorización declarado | FP-03 | Sí si POL excluido o la política no contiene ámbito |
| POL-03 | C | Solo si POL está incluido y contiene allow/deny | FP-03 | Sí si POL excluido o no hay semántica allow/deny |
| POL-04 | O como regla de frontera cuando POL esté incluido | Distinguir política declarada de permiso efectivo del entorno | FP-03 como separación; permiso efectivo fuera | NA si POL está excluido |
| POL-05 | C / gate externo | Solo si requisitos de seguridad explícitos forman parte del contrato de aceptación | FP-05 | No inferir NA de POL ausente; seguridad del entorno puede seguir siendo gate independiente |
| MET-01 | O | Versiones de contrato/esquema fuente y destino identificadas | FP-01/FP-04 | No |
| MET-02 | O (validez probatoria) | Procedencia de artefactos, mapping, transformaciones, aplicación y oráculo | FP-08 | No; si falta, resultado probatorio no válido/no evaluable |
| MET-03 | C | Formato/contrato admite extensiones o aparecen campos desconocidos | FP-03; FP-01 reconoce esquema; FP-08 registra | Sí si el formato cerrado prohíbe extensiones y esa restricción está sellada |
| MET-04 | O como regla interpretativa, no como outcome binario | Siempre: hash/nombre/serialización no equivalen a identidad funcional | FP-08 | No; se registra como salvaguarda, no como score |

## 4. Elementos constitutivos y cardinalidad de clase

De DEC-C10-053:
- CMP, PAR, REF y RUL son elementos constitutivos del DGP base.
- POL es módulo condicional fuera del núcleo confirmatorio mínimo; su ausencia se declara ex ante.
- MET-01/MET-02 son obligatorios para identidad/versionado/procedencia.
- Los elementos constitutivos requieren campos/inventarios explícitos en IAM. La cardinalidad concreta de instancias por clase (incluido cero) no se fijará por intuición: debe justificarse por el dominio abstracto seleccionado y por la pregunta F*.
- Para evitar que un paquete vacío pase como conforme, un universo CMP o PAR vacío produce SCOPE_ERROR salvo justificación formal de que la unidad no contiene componentes/parameters. REF/RUL pueden tener cardinalidad cero solo si el contrato de dominio permite esa ausencia y la cobertura demuestra que no se omitieron registros. RUL vacío exige especial cautela dado que reglas/restricciones son constitutivas; no se acepta como default.

## 5. Frontera correcta de F* y gates de validez probatoria

F* representa la **capacidad funcional de la ruta completa**, no solo la preservación interna del paquete. Según el contrato candidato F* ya definido (producir y aplicar en destino una configuración que satisfaga esquema, integridad, compatibilidad, preservación funcional y seguridad), su adjudicación de ruta puede depender de FP-01…FP-07:
- FP-01/02/03: conformidad estructural, integridad y preservación funcional del objeto;
- FP-04: compatibilidad técnica con el entorno destino;
- FP-05: seguridad efectiva conforme a requisitos de seguridad declarados ex ante;
- FP-06: aplicación efectiva en destino;
- FP-07: verificación post-aplicación de los requisitos pertinentes sobre C_dst^applied.

Estas dimensiones se reportan por separado y sin puntuación compensatoria. FP-06 no es un atributo semántico del paquete, pero sí condición de que la ruta completa haya realizado la función F*. FP-07 verifica el estado aplicado y no crea un segundo fallo si ya se registró la causa primaria.

FP-08 (procedencia/reproducibilidad) es un **gate de validez probatoria** separado: su fallo puede hacer que el resultado sea no evaluable/no aceptable como evidencia, pero no convierte por sí solo una configuración funcionalmente correcta en F*=0. Del mismo modo, un F* técnico positivo sin trazabilidad suficiente no autoriza una conclusión probatoria.

La exclusión de POL del núcleo confirmatorio por DEC-C10-053 significa que no se exige preservar un módulo de políticas declaradas ausente por diseño. **No exime de FP-05**: los requisitos de seguridad efectivos que formen parte de F* deben definirse por un contrato de seguridad independiente del contenido POL y evaluarse en el entorno destino. Preservar POL, cuando exista, no demuestra seguridad; ausencia de POL no equivale a ausencia de requisitos de seguridad.

C_dep, E_dst, recursos, permisos efectivos y runtime se registran como condiciones/mediciones técnicas externas; cuando formen parte de compatibilidad o seguridad, informan FP-04/05 sin confundirse con T_acc ni con el objeto migrado. El contrato F* debe declarar antes de Z/B qué requisitos FP-04/05 aplican y qué evidencia los adjudica.

## 6. Regla de estado por propiedad

1. Primero se fija aplicabilidad en IAM: O/C/NA y el disparador.
2. Después se determina observabilidad/cobertura.
3. Si aplica y hay evidencia suficiente: 1 o 0.
4. Si aplica y la evidencia es insuficiente: ?.
5. NA solo se asigna por la regla ex ante del IAM; nunca para resolver una observación difícil.
6. Si un elemento constitutivo está ausente cuando el contrato requiere instancia, se clasifica SCOPE_ERROR o 0 según el predicado y la evidencia, no NA.
7. F*=? si alguna propiedad obligatoria aplicable es ? y no hay fallo confirmado; F*=0 si una obligatoria falla; F*=1 solo si todas las obligatorias aplicables son 1 y el conjunto no está vacío.
8. La imposibilidad de construir IAM antes de Z/B bloquea la instancia confirmatoria.

## 7. Riesgos y controles contra decisiones post hoc

- **Scope gaming:** cambiar universo o declarar NA después de ver resultados. Control: IAM sellado antes de Z/B; cambios posteriores conservan versión original.
- **Empty-class loophole:** omitir una clase difícil. Control: cardinalidad declarada y SCOPE_ERROR para clases constitutivas sin justificación.
- **Outcome leakage:** usar Outcome/Value para decidir relevancia. Control: aplicabilidad basada en contrato/dominio y evaluadores ciegos.
- **Double counting:** contar mismo defecto en FP-01/02/03/07. Control: predicado primario y enlaces diagnósticos.
- **Security conflation:** inferir seguridad de POL preservada. Control: FP-05 separado.
- **Evidence-to-NA conversion:** convertir falta de evidencia en no aplicabilidad. Control: ? conserva incertidumbre.

## 8. Decisiones todavía abiertas

1. Aceptación de esta matriz y de las reglas de cardinalidad de clases.
2. Tipo de servicio abstracto y frontera de la unidad de configuración.
3. Si REF/RUL admiten cardinalidad cero en el escenario confirmatorio y bajo qué prueba.
4. Qué propiedades FP-04/05/06 son gates de F* versus outcomes separados.
5. Criterios de obligatoriedad de CMP-02/PAR-05 en el microdominio elegido.
6. Política de conflictos RUL y semántica exacta de UNKNOWN.
7. Cómo se acredita cobertura completa para inventarios vacíos.
8. Si el DGP base incorpora seguridad explícita o la conserva como módulo/gate separado.
9. Diseño final del IAM, almacenamiento seguro, hash, timestamps y cambios de versión.
10. Cegamiento y oráculo independiente.

## 9. Dictamen

La matriz propone un procedimiento reproducible para declarar obligatoriedad y aplicabilidad por instancia sin convertir la estructura conceptual de seis elementos en una lista plana de requisitos siempre presentes. Distingue propiedad constitutiva, disparador condicional, NA, incertidumbre, gate técnico y validez probatoria.

**Estado:** propuesta documental derivada de DEC-C10-053/054/055; no aprobada ni congelada; sin claves ni valores concretos, sin IAM instanciado, sin truth/fixtures, sin validación técnica, sin revisión independiente, sin evidencia empírica y sin autorización de ejecución.


## 10. Nota de reconciliación F* — frontera funcional y probatoria (2026-11-05)

Se precisa que F* es una función de ruta completa que produce y aplica configuración en destino; por ello FP-01…FP-07 pueden integrar su adjudicación por dimensiones separadas, no compensatorias. FP-08 permanece como gate de validez probatoria separado. La exclusión de POL del núcleo base no excluye requisitos de seguridad de FP-05 cuando formen parte del contrato F*; estos deben especificarse independientemente de POL.


## 11. DEC-C10-056 — cardinalidad de clases aprobada (2026-11-05)

Se registra la decisión explícita: CMP≥1, PAR≥1 y RUL≥1; REF≥0 solo con IAM pre-Z/B y cobertura exhaustiva; POL≥0 ausente por diseño en el núcleo mínimo salvo módulo condicional predeclarado; MET obligatorio para identidad/versionado/procedencia. CMP=0, PAR=0 o RUL=0 implica SCOPE_ERROR, no NA. REF=0 requiere evidencia de cobertura completa; falta de evidencia queda ?. La estructura abstracta se formaliza en `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`.

La matriz de aplicabilidad continúa en Draft: la decisión cierra cardinalidad de clase, no obligatoriedad de cada propiedad atómica, máximos, valores, mappings, instancia IAM ni validación.



## 12. Reconciliación de aplicabilidad con contrato abstracto y Opción A (2026-11-06)

Cardinalidad de clase y obligatoriedad de predicados son niveles distintos:
- CMP≥1, PAR≥1 y RUL≥1 en el paquete base; REF≥0 solo si IAM pre-Z/B acredita inventario/cobertura exhaustivos; POL ausente por diseño salvo módulo secundario; MET obligatorio.
- Esta cardinalidad no convierte automáticamente todas las propiedades atómicas CMP/PAR/REF/RUL en O. La matriz §3 conserva O/C/NA/? por predicado y objeto.
- RUL no puede desaparecer como clase; RUL-04/05 pueden ser NA si los disparadores no existen por contrato y el inventario lo acredita. UNKNOWN/conflicto no equivale a NA.
- REF=0 no equivale a REF desconocido; falta de cobertura deja ?. Referencias externas/dependencias respetan la frontera.
- POL ausente no elimina requisitos FP-05 declarados independientemente.

El IAM se aplica a F1/F2 y A1/A2 por igual. Antes de Z/B sella propiedades O/C/NA/?, C_src/C_dst, versiones, M, C0/G/H, cobertura y oráculos. Ninguna ruta redefine el IAM tras observar resultados.

**Discrepancia preservada:** §4 histórico de esta matriz contiene formulaciones de REF/RUL con cardinalidad cero anteriores a DEC-C10-056. Se consideran supersedidas para cardinalidad de clase; no se reescribe el historial ni se altera la obligatoriedad de predicados individuales más allá de esa decisión.


## 13. IAM candidato por roster PAR de servicio lógico

| Slot | Aplicabilidad | Requiredness del parámetro | Estados candidatos | Predicados atómicos prioritarios | Pendiente |
|---|---|---|---|---|---|
| PAR-SVC-ENABLED / BOOL | Candidato base si es configuración declarada P0 | REQUIRED | VALUE; DEFAULT con contrato; no ABSENT/NULL | PAR-01/02/03/05/06 | Evidencia P0, mapping, default |
| PAR-SVC-PROFILE / ENUM | Candidato base si determina perfil funcional P0 | REQUIRED | VALUE; DEFAULT con contrato; no ABSENT/NULL | PAR-01/02/03/05/06 | D_profile, tabla mapping, default |
| PAR-SVC-RETRY-COUNT / INT | Candidato base solo si el servicio declara reintentos | OPTIONAL | ABSENT/VALUE; DEFAULT con contrato; NULL no salvo declaración | PAR-01/02/03/05/06 | N_retry_max, semántica de ausencia y regla vinculada |

La tabla es un IAM candidato, no un sellado operativo. Ninguna propiedad pasa a O/C/NA confirmatorio hasta que la unidad, fuente contractual, dominio, mapping, cobertura y regla de evidencia estén definidos ex ante. Si un slot no pertenece al P0 de la unidad, se elimina/sustituye antes de Z/B y se registra justificación; no se declara NA post hoc. POL sigue ausente por diseño y MET obligatorio conforme a decisiones existentes.

## 14. IAM conceptual de la RUL mínima aceptada

| Control | Requisito ex ante | Estado |
|---|---|---|
| RUL-BASE-01 | Al menos una regla constitutiva, no tautológica y con fuente funcional | Instancia aceptada conceptualmente por DEC-C10-068 |
| RUL-BASE-02 | Owner CMP, scope, claves/dominios y versión inequívocos | Owner lógico/scope y claves/dominios aceptados; CMP concreto/versionado OPEN |
| RUL-BASE-03 | AST acíclico 4/16/16, operadores/efecto dentro de DEC-C10-054 | Perfil y expresión compatibles documentalmente; ejecución/parser no validados |
| RUL-BASE-04 | TRUE/FALSE/UNKNOWN y tratamiento explícito de UNKNOWN | Regla general documentada; oráculo/adjudicación OPEN |
| RUL-BASE-05 | Mapping de regla y operandos F1/A1, aplicación F2/A2 | Invariantes definidos; mapping concreto y evidencia OPEN |
| RUL-BASE-06 | FP-03 RUL-01/02/03, cobertura, oráculo independiente | Contratos conceptuales; cobertura/oráculo OPEN |

DEC-C10-068 acepta la regla como verdad constitutiva interna al DGP. No asigna todavía O/C/NA confirmatorio por escenario ni acredita preservación/aplicación.
## 15. IAM conceptual aceptado y aplicabilidad de la regla sintética de servicio

| Elemento | Aplicabilidad/obligatoriedad conceptual | Estado |
|---|---|---|
| CMP-SERVICE-LOGIC | Owner lógico de RUL-SVC-ENABLE-PROFILE-01 | Aceptado por DEC-C10-068; identidad/versionado de instancia OPEN |
| PAR-SVC-ENABLED | P0 REQUIRED para la instancia sintética | Aceptado conceptualmente por DEC-C10-068 |
| PAR-SVC-PROFILE | P0 REQUIRED para la instancia sintética | Aceptado conceptualmente por DEC-C10-068 |
| RUL-SVC-ENABLE-PROFILE-01 | P0 REQUIRED; efecto REQUIRE; scope de unidad lógica | Aceptada conceptualmente por DEC-C10-068 |
| PAR-SVC-RETRY-COUNT | Fuera del núcleo mínimo | Excluido hasta justificación P0 |

La aceptación conceptual no asigna todavía O/C/NA por escenario ni sustituye la matriz IAM de evidencia/cobertura. Owner lógico y scope quedan definidos; la identidad CMP concreta, versión de instancia, serialización, mapping, predicados observables y oráculo permanecen OPEN. La regla de servicio no sustituye RUL-01/02/03, que siguen siendo predicados de preservación.

## 16. Identidad/versionado de la instancia CMP: propuesta pendiente

La matriz IAM reutilizará la separación de `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md`: contract_id/version, instance_id/version, component_id/class, owner_component_id, IDs de PAR/RUL, mapping_id/version, IAM_id/version/hash y oráculo. La propuesta de IDs candidatos no está aceptada ni sellada.

CMP-SERVICE-LOGIC es rol/owner lógico provisional, no component_id único. CMP-SERVICE-LOGIC-001 es solo candidato. La matriz deberá registrar IDs y versiones de C_src/C_dst y cobertura por clase antes de Z/B. No declarar REF=0 sin inventario/cobertura exhaustivos; no calcular hash antes de serialización canónica. El IAM operativo permanece OPEN.

## 17. Reconciliación IAM con DEC-C10-069 y gate de adjudicación independiente (2026-11-07)

### 17.1. Corrección de estado de identidad

La §16 histórica queda **supersedida únicamente en su estado de aceptación**, no eliminada: DEC-C10-069 acepta los identificadores candidatos y la separación de versionado. En consecuencia:

| Campo | Valor aceptado | Estado IAM |
|---|---|---|
| contract_id / version | `C10S-SVC-REQUEST-PROCESSOR` / `1.0.0` | Identidad aceptada; snapshot/versionado de contenido por registrar |
| instance_id / version | `C10S-SVC-REQUEST-PROCESSOR-001` / `1` | Identidad/revisión aceptadas; no equivale a serialización |
| component_id / class | `CMP-SERVICE-LOGIC-001` / `SERVICE_LOGIC` | Identidad/clase del CMP focal aceptadas |
| owner lógico | `CMP-SERVICE-LOGIC` | Rol/owner, no ID de componente |
| PAR | `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` | Contrato funcional aceptado por DEC-C10-068 |
| RUL | `RUL-SVC-ENABLE-PROFILE-01` | Contrato funcional aceptado por DEC-C10-068 |
| mapping_id/version | Por asignar | OPEN |
| IAM_id/version | Por asignar | OPEN |
| oracle_id/version | Por asignar | OPEN |
| artifact_hash | No calculable aún | OPEN hasta serialización canónica |

La identidad aceptada no determina por sí sola cardinalidad global CMP, inventario de CMP auxiliares ni correspondencia física P1. CMP focal ≠ universo CMP completo. CMP≥1 se satisface conceptualmente por el focal aceptado; inventario adicional y cobertura permanecen pre-Z/B.

### 17.2. Instanciación IAM pendiente por objeto y etapa

El IAM confirmatorio deberá materializar una fila por combinación de: ruta (F/A), etapa (1/2), objeto fuente/intermedio/destino, clase, propiedad atómica y snapshot/version. Como mínimo:

- C_src: inventario y versión del CMP/PAR/RUL de origen.
- S2 en F1 y S1 en A1: representación intermedia efectivamente producida, con mapping/version y evidencia de preservación.
- C_dst^decl: destino declarado antes de aplicación, no evidencia de estado aplicado.
- C_dst^applied: estado observado tras F2/A2, con snapshot/version, timestamp y evidencia independiente.
- E_dst/runtime: entorno y condiciones de aplicación, entidad separada de la configuración declarada/aplicada.

Cada fila registrará O/C/NA/? y disparador, expected semantic identity/value, observed value/state, source/destination snapshot refs, coverage denominator/numerator, evidence refs, primary predicate (FP-01…07), diagnostic predicates, adjudicator y rationale. NA requiere disparador ex ante y evidencia de pertenencia fuera del dominio; falta de inspección/cobertura siempre deja ?. No se sella ninguna fila después de conocer resultados.

### 17.3. Contrato de roles y oráculo — requisitos de adjudicación, no instancia ejecutable

Se explicita el contrato de separación que debe implementar el futuro oráculo:

| Rol | Acceso permitido | Acceso prohibido / condición |
|---|---|---|
| Generador DGP | Parámetros ex ante, verdad estipulada, potenciales y mecanismo asignado necesarios para generar el mundo | No adjudica el resultado de preservación/aplicación |
| F1/F2 y A1/A2 | Solo entradas, contratos, permisos e interfaces previstos para cada ruta | No reciben truth/potenciales ocultos ni etiquetas del oráculo |
| Analizador | Artefactos observables y evidencia autorizada por el protocolo; produce predicados/estimandos antes de revelar truth | No accede a truth oculta, potenciales, claves privadas del oráculo ni etiquetas de Evaluador |
| Evaluador/oráculo | Truth del DGP, snapshots sellados, IAM pre-Z/B, mapping versionado y evidencia observada, tras cierre/congelación de salidas del Analizador | No altera truth/IAM/criterios tras observar salidas; no repara datos faltantes inventando evidencia |

El Evaluador no convierte la verdad estipulada en evidencia de que una ruta la preservó: compara truth esperada con estado efectivamente observado y documenta cobertura. El oráculo adjudica por predicado y objeto; no reemplaza medición independiente ni infiere C_dst^applied desde C_dst^decl.

### 17.4. Adjudicación trivalente y reglas de evidencia

Para cada predicado aplicable:

- **1:** evidencia observada válida satisface el predicado, con cobertura suficiente del universo declarado.
- **0:** evidencia válida demuestra violación/omisión en el universo cubierto, y el criterio de fallo estaba predeclarado.
- **?:** snapshot ausente, inspección parcial, mapping ambiguo, conflicto de fuentes, identidad/versionado no trazable o cobertura insuficiente.
- **NA:** IAM pre-Z/B demuestra que el predicado no aplica; nunca se deriva de falta de datos.
- **SCOPE_ERROR:** falta una clase constitutiva exigida o el universo de comparación no satisface el contrato; no se recodifica como NA.

Truth esperada, salida del Analizador y adjudicación del Evaluador se conservan como campos distintos. Un mismo defecto tiene un único predicado primario para evitar double counting; FP-07 puede referenciarlo como diagnóstico sin sumar un segundo fallo. FP-08 es gate de validez probatoria, no sustituto de FP-01…07.

### 17.5. Gate de cierre pendiente

No puede congelarse IAM/oráculo hasta que estén definidos y versionados: mapping_id, IAM_id, oracle_id; roster CMP completo y cobertura; valores/defaults concretos por escenario; snapshots y reglas de captura; mapping de AST/operadores y política de UNKNOWN/conflicto; evidencia admisible y criterios de suficiencia; cegamiento, momento de liberación de truth y hash/procedencia de artefactos. No se fijan aquí defaults, tolerancias, fixture, parser, serialización ni schema.

**Estado:** identidad CMP reconciliada con DEC-C10-069; IAM operativo y contrato del oráculo especificados solo a nivel de requisitos. No aceptados ni congelados. No Design Freeze, implementación, validación ejecutable o ejecución científica.

## 18. Roster mínimo de referencia y reconciliación de slots PAR (2026-11-07)

### 18.1. Base normativa y roster funcional aceptado

El roster funcional mínimo conocido se deriva conjuntamente de DEC-C10-056, DEC-C10-068 y DEC-C10-069. No se infiere el universo completo de componentes ni referencias a partir de la identidad del CMP focal.

| Clase | ID lógico | Cardinalidad mínima | Estado de aceptación | Tratamiento IAM |
|---|---|---:|---|---|
| CMP | `CMP-SERVICE-LOGIC-001` | 1 focal | Identidad/clase aceptadas por DEC-C10-069 | REQUIRED; registrar inventario completo CMP y cobertura antes de Z/B |
| PAR | `PAR-SVC-ENABLED` | 1 | Contrato funcional aceptado por DEC-C10-068 | REQUIRED; BOOL {false,true} |
| PAR | `PAR-SVC-PROFILE` | 1 | Contrato funcional aceptado por DEC-C10-068 | REQUIRED; ENUM {STANDARD, READ_ONLY, DISABLED} |
| RUL | `RUL-SVC-ENABLE-PROFILE-01` | 1 | Contrato funcional aceptado por DEC-C10-068 | REQUIRED; REQUIRE, scope y semántica aceptados |
| REF | Sin IDs asignados | 0 o más | No se ha aceptado un inventario vacío ni un roster de referencias | Si REF=0, exige IAM pre-Z/B e inventario/cobertura exhaustivos; si no, ? |
| POL | Ausente por diseño en núcleo mínimo | 0 | Exclusión condicional del núcleo conforme a DEC-C10-053 | NA/ausente por diseño solo bajo declaración ex ante; no elimina FP-05 |
| MET | Identidades/versiones/procedencia | Obligatorio | Obligación estructural aceptada | Registrar vínculos y procedencia; serialización/hash físico OPEN |

Este es el roster **mínimo funcional aceptado**, no un inventario exhaustivo ya observado de C_src, S1/S2 o C_dst. CMP focal=1, PAR aceptados=2 y RUL aceptada=1 son identificables; no se afirma que no existan CMP/PAR/RUL adicionales hasta completar inventario y cobertura. DEC-C10-056 impide que una clase constitutiva exigida se omita o se recodifique como NA.

### 18.2. Supersesión del slot RETRY-COUNT

La fila `PAR-SVC-RETRY-COUNT` de §13 es una propuesta histórica anterior a DEC-C10-068 y queda **supersedida para el núcleo confirmatorio base**. No pertenece al roster aceptado, no tiene requiredness ni dominio confirmatorio, y no debe aparecer en fixtures/IAM como slot base. Una futura ampliación requeriría justificación P0, decisión/versionado explícitos y revisión del contrato/IAM; no se incorpora por defecto.

### 18.3. Estados de los dos PAR aceptados

Para evitar inventar defaults:

- El contrato funcional acepta las claves, tipos y dominios, pero no declara un valor DEFAULT para ninguna.
- El estado confirmatorio candidato es VALUE con valor perteneciente al dominio tipado.
- ABSENT y NULL son estados no admisibles para estos parámetros REQUIRED; si se observan con cobertura válida en el objeto inspeccionado, constituyen incumplimiento del contrato/IAM.
- DEFAULT no puede utilizarse como sustituto de VALUE mientras no exista default contractual explícito con kind, origen, scope, precedencia y versión. Si aparece DEFAULT sin esa declaración, se adjudica ?/CONTRACT_ERROR según el predicado predefinido; nunca se inventa el valor.
- DEFAULT_ENV_RESOLVED es una observación del entorno/runtime y no un estado del paquete declarativo P0.

No se eligen valores por escenario ni se prescribe ENABLED=true/false o PROFILE concreto: la regla aceptada admite los contrastes definidos en DEC-C10-068. La asignación de valores para cada DGP/escenario debe ser predeclarada por el diseño experimental, no inferida del mapping.

### 18.4. Aplicabilidad por etapa y objeto

| Objeto/etapa | CMP focal | PAR-ENABLED | PAR-PROFILE | RUL aceptada | REF |
|---|---|---|---|---|---|
| C_src | Inventario/clase/scope | REQUIRED | REQUIRED | REQUIRED | Inventario y cobertura |
| F1→S2 / A1→S1 | Identidad/clase preservada | Tipo/estado/valor preservados | Tipo/estado/dominio/valor preservados | Identidad/scope/AST/operandos/efecto preservados | Correspondencias/integridad si existen |
| C_dst^decl | Inventario declarado | REQUIRED | REQUIRED | REQUIRED | Declaraciones de referencias |
| F2/A2→C_dst^applied | CMP efectivamente aplicado | Estado/valor efectivos | Estado/valor efectivos | Regla efectiva y evaluable | Integridad observada |
| E_dst/runtime | No confundir con CMP P0 | No sustituye PAR | No sustituye PAR | No sustituye RUL | Dependencias ambientales separadas |

La tabla define qué debe inventariarse/adjudicarse, no afirma que las etapas o artefactos ya existan ni que hayan pasado. Cada ruta se evalúa independientemente. Si un snapshot o universo no se puede inspeccionar, el resultado es ? y no NA.

### 18.5. Gate de cierre de roster/IAM

Antes de sellar IAM pre-Z/B faltan: inventario exhaustivo CMP/PAR/RUL/REF en C_src y destino; criterio y evidencia de cobertura; confirmación de que no hay slots adicionales obligatorios; mapping_id/version; IAM_id/version; valores por escenario y sus reglas de asignación; snapshots S1/S2 y C_dst declarado/aplicado; política de DEFAULT/conflicto/UNKNOWN; y evidencia/oráculo. REF=0 solo se podrá registrar tras cobertura exhaustiva. No se infiere un universo cerrado de la lista funcional mínima.

**Estado:** roster funcional mínimo aceptado reconciliado; roster exhaustivo e IAM operativo OPEN. No se asignan valores de escenario, no se declara REF=0, no se crean fixtures y no se autoriza implementación/ejecución.

## 19. Protocolo de inventario por snapshot — overlay C10-S sobre U_G (2026-11-07)

### 19.1. Precedencia y reutilización de registros existentes

El inventario C10-S debe reutilizar la plantilla U_G C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md y sus registros versionados NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. No se crea un segundo inventario U_G ni se alteran las claves/FKs aprobadas por DEC-C10-064/065.

La configuración lógica se describe mediante el catálogo atómico de CMP/PAR/REF/RUL y esta matriz IAM. **No se fuerzan PAR ni RUL a NODE o PREDICATE**: NODE representa entidades U_G con identidad propia; PREDICATE conserva el catálogo de predicados U_G. CMP focal se enlaza al nodo raíz LOGICAL_SERVICE_UNIT cuando corresponda; componentes adicionales solo generan NODE si son entidades reales identificadas y pertenecen al universo U_G. Los valores de PAR y la definición/estado de RUL se registran en el manifiesto de configuración C10-S descrito abajo, vinculado a snapshot/evidencia, sin crear nodos artificiales.

### 19.2. Manifiesto de configuración C10-S — estructura de captura propuesta

Este manifiesto es una vista documental de captura para poblar/referenciar la matriz IAM; **no es tabla física aprobada, schema ejecutable ni dato observado**. Una fila por objeto/propiedad y snapshot exacto:

| Campo | Semántica / restricción |
|---|---|
| manifest_record_id | Identidad opaca de la fila de captura; versionada conforme a DEC-C10-062 si se adopta |
| contract_id / contract_version | Identidad aceptada por DEC-C10-069 |
| instance_id / instance_version | Identidad/revisión aceptadas por DEC-C10-069 |
| snapshot_id / snapshot_object_record_id | FK exacta al snapshot U_G conforme a DEC-C10-065; nunca latest/timestamp lookup |
| stage | C_src; F1→S2; A1→S1; C_dst_declared_F2; C_dst_declared_A2; C_dst_applied_F2; C_dst_applied_A2 |
| route_id / route_record_id | F o A, según ruta; NULL solo cuando la etapa no pertenece a ruta y se justifica |
| object_class | CMP / PAR / REF / RUL / MET; no amplía NODE/PREDICATE enum |
| semantic_id / semantic_version | ID y versión propios de CMP/PAR/RUL/REF/MET; no reutilizar TID/SID/RID |
| owner_component_id | CMP-SERVICE-LOGIC-001 como referencia al CMP aceptado; owner lógico CMP-SERVICE-LOGIC no es component_id |
| property_key / property_type | Obligatorio para PAR; tipo/domain exactos por contrato |
| state / value | Estados separados ABSENT/NULL/DEFAULT/VALUE; value solo si VALUE; no inferir default |
| rule_id / rule_version / scope / AST_ref / effect | Obligatorio para RUL; contenido/AST versionado, no inferido de un nombre |
| mapping_id / mapping_version / mapping_status | OPEN hasta asignación; status MAPPED/UNMAPPED/AMBIGUOUS/NOT_APPLICABLE, con NA solo justificado |
| declared_or_applied | Distingue paquete/configuración declarada de estado aplicado; no se usa para E_dst/runtime |
| evidence_id / claim_evidence_id | Referencia a EVIDENCE_REGISTER y CLAIM_EVIDENCE_LINK, con procedencia |
| coverage_scope_id | Universo/denominador por clase, snapshot, ruta y etapa |
| observed_state / unknown_reason | 1/0/?/NA con reglas U_G; truth DGP permanece fuera del manifiesto visible al Analizador |
| recorded_at / recorded_by / supersedes | Record-time y linaje; no sustituye timestamp del snapshot |

El manifiesto solo se instancia cuando existan snapshots y evidencia. Antes, sus filas son esquema y no observaciones. No se fijan aquí valores de escenario, serialización, enums físicos ni DDL.

### 19.3. Crosswalk de snapshots y etapas

| Etapa lógica | Snapshot U_G requerido | Universo que se inventaría | Límite |
|---|---|---|---|
| C_src | Snapshot exacto de origen | CMP/PAR/REF/RUL/MET declarados en fuente | No inferir estado destino |
| F1→S2 | Snapshot exacto de representación S2 | Correspondencias y preservación CMP/PAR/REF/RUL | No equivale a aplicación |
| A1→S1 | Snapshot exacto de representación S1 | Mismo universo semántico bajo ruta A | Evidencia independiente; no copiar resultados F |
| C_dst_declared_F2 | Snapshot del destino declarado para ruta F | Declaración pre-aplicación | No prueba instalación ni estado efectivo |
| C_dst_declared_A2 | Snapshot del destino declarado para ruta A | Declaración pre-aplicación | No heredar el snapshot F |
| C_dst_applied_F2 | Snapshot post-aplicación de F2 | CMP/PAR/RUL/REF efectivamente observables | No inferir desde declaración |
| C_dst_applied_A2 | Snapshot post-aplicación de A2 | CMP/PAR/RUL/REF efectivamente observables | No inferir desde declaración |

Los nombres de etapa se almacenan en el campo textual SNAPSHOT.scope, sin ampliar el enum phase ni alterar la tabla. Propuesta de serialización textual determinista (aún no aceptada como contrato de schema): `program=C10-S|contract_id=C10S-SVC-REQUEST-PROCESSOR|contract_version=1.0.0|instance_id=C10S-SVC-REQUEST-PROCESSOR-001|instance_version=1|stage_key=<STAGE>|route=<NONE|F|A>|object_class=CONFIG`. Valores de stage_key: C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED, A2_DST_APPLIED. C_SRC usa route=NONE; las demás etapas fijan F o A. `phase` se asigna independientemente conforme al significado temporal real del snapshot y a su contrato U_G (`baseline`, `post-B`, `rollback` o `route-test`); no se fuerza `route-test` a todas las etapas C10-S. La etapa/ruta de configuración se registra en `scope`, sin inferir con ello asignación Z/B ni momento causal. coverage_scope_id es una FK separada a COVERAGE_REGISTER y nunca sustituye scope. El consumidor debe rechazar campos duplicados, ausentes o no reconocidos; no usar parsing heurístico. La propuesta permite distinguir etapa/ruta con el schema textual existente, pero requiere aceptación y pruebas de compatibilidad antes de captura. Si se decide no aceptar esta codificación, detener y emitir decisión de schema, no introducir otra convención informal.

### 19.4. Cobertura por clase y por etapa

Crear COVERAGE_REGISTER scopes separados para cada combinación de snapshot×etapa×ruta×clase (CMP, PAR, REF, RUL, MET) y para fuentes de evidencia pertinentes. Cada scope fija universe_definition/version, denominator, expected_sources, examined_sources, valid_sources, covered_units, excluded_units y opaque_or_unknown_units. No agregar clases distintas en un único porcentaje.

Reglas:
- CMP: cubrir roster de componentes lógicos, clases, owners, versiones y límites P0/P1. La cardinalidad del CMP focal no demuestra que el roster total esté cerrado.
- PAR: cubrir todas las claves declaradas en el contrato/instancia, estado, tipo, dominio, valor y owner. Para la instancia mínima conocida, ENABLED y PROFILE son obligatorios; RETRY-COUNT queda excluido por DEC-C10-068.
- RUL: cubrir todas las reglas constitutivas del paquete, IDs/versiones, scope, AST, operandos, efecto y referencias PAR. RUL≥1 es exigencia estructural; la regla aceptada es la base funcional, pero no demuestra que no existan reglas adicionales.
- REF: cobertura de extremos, tipo, dirección, multiplicidad, integridad y dependencias; REF=0 solo si universo y fuentes exhaustivos justifican ausencia.
- MET: cubrir IDs/versiones, procedencia, timestamps, relaciones a snapshots/M/IAM/oráculo y hashes solo si serialización canónica existe.

COMPLETE es relativo al universo operativo declarado y versionado; no significa exhaustividad ontológica. NONE/PARTIAL o universo desconocido impiden declarar ausencia (0) o REF=0; se conserva ?.

### 19.5. Cobertura de evidencia y cegamiento

Las fuentes de contrato y catálogos prueban intención/semántica aceptada, no el contenido de un snapshot ni el estado aplicado. Para clasificar una propiedad observada se exige evidencia del artefacto/snapshot exacto y un CLAIM_EVIDENCE_LINK con support_type, scope y limitaciones. C_dst_applied exige evidencia post-aplicación independiente; logs o telemetría diferencial por ruta deben reflejarse en cobertura y E_T.

El manifiesto visible al Analizador contiene observaciones autorizadas, no truth DGP ni potenciales. DGP_TRUTH_SECURE permanece segregado. El Evaluador compara tras congelación de salidas del Analizador, pero no sustituye observación faltante por truth. Dos evaluadores independientes E1/E2 y adjudicación se aplican conforme al registro U_G cuando se habilite esa fase; no se afirma que estén disponibles ahora.

### 19.6. Estado y gate

**Estado:** protocolo de captura por snapshot documentado; sin snapshots, filas observadas ni evidencia técnica aportada. Inventario exhaustivo e IAM operativo siguen OPEN. La plantilla U_G §17.5 ya advierte que la captura técnica no se ha realizado; esta especialización no modifica ese estado. No se declara COMPLETE, REF=0 ni ausencia de objetos. No se crean fixtures, schema físico, parser, implementación, simulación o ejecución científica.
### 19.7. Contrato documental de COVERAGE_REGISTER para C10-S

Se reutiliza sin cambios el encabezado vigente de COVERAGE_REGISTER (§12.3 U_G): coverage_scope_id; dimension; universe_definition/version; denominator_unit_and_count; expected_sources; examined_sources; valid_sources; covered_units/count; excluded_units/reason; opaque_or_unknown_units/count; status; completion_rule; exceptions_and_impact; reviewer_id; timestamp. No se añade una columna física ni se cambia la PK.

**Unidad lógica de cobertura:** una combinación exacta de (contract_id/version, instance_id/version, snapshot_id, snapshot_object_record_id, stage_key, route/route_id, object_class). Cada combinación tiene un coverage_scope_id propio; no se comparte una fila entre snapshots, etapas, rutas o clases. coverage_scope_id es una clave opaca/única, no se parsea para reconstruir la semántica. dimension identifica la familia y clase, por ejemplo C10S_CONFIG_CMP, C10S_CONFIG_PAR, C10S_CONFIG_REF, C10S_CONFIG_RUL o C10S_CONFIG_MET. universe_definition/version debe fijar explícitamente la tupla anterior, la regla de enumeración y la versión del universo; no basta con una etiqueta libre como “complete”.

La matriz de 7 etapas × 5 clases define hasta 35 scopes lógicos por instancia completa de snapshots. Es una plantilla de cobertura, no 35 filas observadas ni obligación de crear scope para un snapshot inexistente. Las fuentes examinadas y válidas se enumeran en cada scope; no se mezclan fuentes de C_src con evidencia post-aplicación ni rutas F/A.

**Denominadores y reglas por clase:**
- CMP: unidades = identidades CMP del universo declarado; cubrir identidad/clase/versión/owner y frontera. El CMP focal aceptado no cierra el denominador total.
- PAR: unidades = claves PAR declaradas por contrato/instancia; cubrir existencia, estado, tipo, dominio, valor y owner. ENABLED y PROFILE son slots requeridos; RETRY-COUNT no pertenece al núcleo.
- REF: unidades = referencias declaradas y extremos/tipos/relaciones que el contrato de enumeración incluya. Denominador 0 solo es válido si fuentes y universo se han enumerado exhaustivamente; de otro modo UNKNOWN.
- RUL: unidades = reglas constitutivas; cubrir ID/versión, AST, scope, operandos, efecto y dependencias PAR. La regla aceptada no prueba que el universo de reglas sea exhaustivo.
- MET: unidades = assertions de identidad, versión, procedencia, snapshot, mapping/IAM/oráculo y hashes solo cuando exista serialización canónica. No convertir metadatos ausentes en NA por defecto.

**Estados de cobertura y clasificación:**
- NONE = ninguna unidad cubierta; no significa ausencia.
- PARTIAL = cobertura incompleta, con omisiones/opacidad explícitas.
- COMPLETE = denominador finito/versionado, regla de enumeración explícita, todas las fuentes esperadas examinadas y válidas, unidades cubiertas o exclusiones justificadas, cero unidades opacas/desconocidas relevantes y revisión registrada. COMPLETE es relativo al universo operativo declarado, no exhaustividad ontológica.
- Un objeto/propiedad no observado con cobertura NONE/PARTIAL conserva ?; no se adjudica 0 por falta de fila.
- Un 0 de ausencia exige scope COMPLETE y evidencia válida para el predicado de ausencia. Para REF=0 se requiere denominator=0 con enumeración exhaustiva demostrada. Para slots PAR REQUIRED, ausencia observada en scope COMPLETE es incumplimiento (0), no NA.
- Si el denominador no puede determinarse, o hay fuentes esperadas no examinadas, artefactos opacos, conflictos no resueltos o límites materiales, status no puede ser COMPLETE.

**Limitación de integridad referencial detectada:** el esquema vigente de COVERAGE_REGISTER tiene coverage_scope_id como PK/UNIQUE, pero no contiene snapshot_id ni snapshot_object_record_id. La tupla exacta se puede documentar en universe_definition/version y el snapshot/objeto apunta al scope mediante su FK coverage_scope_id; sin embargo, el vínculo inverso no es una FK compuesta físicamente verificable. No se oculta esta limitación ni se añaden columnas unilateralmente. La decisión semántica de pertenencia del grafo a snapshot está aceptada mediante DEC-C10-065 (Opción A); su validación física permanece pendiente según el gate U_G correspondiente. La limitación descrita aquí pertenece a un gate distinto: integridad de COVERAGE_REGISTER→snapshot para scopes de cobertura C10-S.

**Estado:** contrato documental de cobertura propuesto; no hay filas COVERAGE_REGISTER C10-S pobladas, snapshots ni evidencia observada. La codificación de SNAPSHOT.scope sigue pendiente de aceptación/compatibilidad. No se declara COMPLETE ni REF=0.

### 19.8. Reconciliación de integridad COVERAGE_REGISTER↔SNAPSHOT (gate independiente)

Corrección de clasificación: U_G-SCH-10 trata pertenencia y referencias del grafo; su solución semántica Opción A fue aceptada por DEC-C10-065. No se reabre por la limitación de cobertura descrita en §19.7.

En el esquema actual, los registros de objeto contienen coverage_scope_id y, para los registros de grafo, snapshot_id + snapshot_object_record_id; COVERAGE_REGISTER tiene coverage_scope_id único pero no almacena el par de snapshot. Existe por tanto un enlace hacia el scope mediante la FK de objeto, pero no existe una clave compuesta que permita al motor demostrar que el scope referenciado corresponde al mismo snapshot exacto que el objeto. universe_definition/version puede documentarlo, pero no crea por sí solo integridad relacional.

Alternativas:
- **C0 — contrato documental + control de integridad independiente (recomendación provisional):** conservar el esquema; cada scope fija en universe_definition/version la tupla exacta (contract/version, instance/version, snapshot_id, snapshot_object_record_id, stage_key, route, object_class). Cada registro que referencia el scope debe coincidir con esa tupla. Un control estático/validador futuro comprueba la igualdad, unicidad, cardinalidad y ausencia de scopes huérfanos. Hasta que ese control exista y sea auditado, estado CONDITIONAL; no se presenta como FK garantizada.
- **C1 — FK compuesta en el esquema:** extender COVERAGE_REGISTER con snapshot_id y snapshot_object_record_id para scopes snapshot-bound, declarar FK compuesta al SNAPSHOT exacto y clave candidata (coverage_scope_id,snapshot_id,snapshot_object_record_id); migrar las referencias de los registros C10-S a FK compuesta (coverage_scope_id,snapshot_id,snapshot_object_record_id). Requiere revisar nullable/legacy, registros SNAPSHOT que ya portan coverage_scope_id, ciclos FK, compatibilidad del motor y todas las diez tablas. No aceptar ni aplicar sin decisión explícita de schema.
- **C2 — tabla puente de binding:** añadir una relación normalizada para scope↔snapshot/etapa/ruta/clase. No recomendada por ahora: añade una tabla y claves/validaciones adicionales cuando C1 puede resolver la integridad básica con menos superficie.

**Estado vigente tras DEC-C10-070:** C0 está ACEPTADA como contrato documental condicionado; no es ya una mera recomendación. Se mantiene el schema actual y se exige el control independiente descrito en §19.9 y desarrollado en la especificación de control C10-S. Su estado de cierre permanece CONDITIONAL hasta especificación, autorización, ejecución y auditoría. C1/C2 no aceptadas. No atribuir a C0 enforcement relacional.

Este gate no cambia Opción A/DEC-C10-065, no modifica el enum SNAPSHOT.phase, ni acepta la codificación SNAPSHOT.scope. Tampoco crea scopes/snapshots, valida DDL, implementa parser o autoriza ejecución.

### 19.9. DEC-C10-070 — aceptación de C0 para binding de scopes

**ACEPTADO POR EL USUARIO — diseño documental condicionado.** Se acepta C0: conservar el esquema actual y fijar en universe_definition/version la tupla exacta contract/version × instance/version × snapshot_id × snapshot_object_record_id × stage_key × route × object_class por coverage_scope_id. Todo registro que apunte al scope debe coincidir con esa tupla.

El control independiente debe comprobar igualdad del binding, unicidad, cardinalidad, scopes huérfanos/no usados y conflictos. Hasta que esté especificado, implementado bajo autorización, ejecutado y auditado, C0 permanece CONDITIONAL y no equivale a FK compuesta ni integridad relacional garantizada.

C1 (FK compuestas) y C2 (tabla puente) no se aceptan ni autorizan. La decisión no modifica el schema, no reabre DEC-C10-065/Opción A, no acepta SNAPSHOT.scope ni cambia SNAPSHOT.phase. No crea registros ni autoriza validación ejecutable, implementación o ejecución científica.

### 19.10. Crosswalk IAM para REF bajo DEC-C10-076 — propuesta

El IAM deberá separar: (i) pertenencia de un objeto REF al universo; (ii) referencias de envelope UDG (member/owner/source/rule/provenance); (iii) extremos funcionales de REF; (iv) FK estructurales U_G. No comparten denominador ni obligatoriedad automáticamente.

Por cada REF incluido, IAM predeclarará: origen/owner permitido; clase y cardinalidad de source/target endpoints; relation_type, direction, role y multiplicity; internal/external namespace; integridad requerida; versión/snapshot; si aplica a ruta global o específica; regla de inclusión/exclusión; mapping permitido a EDGE y política split/merge; evidencia y cobertura exigidas. No se asignan aquí valores ni cardinalidades numéricas.

REF vacío solo podrá declararse con universo REF exhaustivo y evidencia completa. Ausencia de una referencia opcional no implica REF=0. La ausencia de EDGE en ROUTE_STEP solo prueba no pertenencia a esa ruta cuando la cobertura correspondiente es completa; no prueba ausencia de REF ni del objeto en snapshot.

Las seis FK tipadas de CLAIM_EVIDENCE_LINK y las FKs Opción A siguen siendo integridad U_G; no se añaden al roster REF salvo una declaración de dominio independiente. El IAM sigue abierto y no autoriza instancias ni ejecución.

### 19.11. DEC-C10-077 — límites IAM aceptados para REF

Quedan aceptadas las cuatro capas separadas: membership del universo; referencias UDG del envelope; extremos funcionales de REF; FK estructurales U_G. No comparten denominador ni obligatoriedad por defecto. IAM aún debe declarar, ex ante y por clase/rol/extremo/stage_key/scope, dominios, cardinalidades, REQUIRED/OPTIONAL, endpoints internos/externos, integridad, mapping M y evidencia. DEC-C10-077 no asigna esos valores ni cierra applicability.


### 19.12. DEC-C10-078 — contrato lógico de filas IAM aceptado

**ACEPTADO POR EL USUARIO — contrato documental lógico.** Se acepta la estructura de cuatro capas y el contrato lógico de filas IAM, sin convertir esta aceptación en schema físico, roster exhaustivo ni IAM poblado.

**Capas:**

1. **L1 — Membership del universo:** pertenencia de objetos CMP/PAR/REF/RUL/MET al universo declarado, con identidad lógica y referencia exacta al registro/versionado.
2. **L2 — Referencias del envelope UDG:** referencias tipadas usadas para membership, owner, source, reglas de inclusión/exclusión, dependencias y provenance. Los ejemplos `MEMBER`, `OWNER`, `SOURCE`, `INCLUSION_RULE`, `EXCLUSION_RULE`, `DEPENDENCY` y `PROVENANCE` son ilustrativos; `ref_role` no crea por sí mismo un objeto REF.
3. **L3 — Extremos funcionales REF:** REF es objeto con identidad propia y extremos tipados; SOURCE/TARGET es patrón binario, no catálogo cerrado. N-aria requiere representación/grupo explícito.
4. **L4 — FK/vínculos estructurales U_G:** relaciones estructurales de registros/tablas U_G; no se cuentan como REF por defecto salvo declaración de dominio independiente, explícita y justificada.

Las capas no comparten automáticamente universo, denominador, obligatoriedad ni cardinalidad.

**Contrato lógico de fila:** `iam_rule_id`, `layer`, `source_class`, `source_identity_rule`, `role_namespace`, `role_key`, `endpoint_position`, `target_domain`, `min_cardinality`, `max_cardinality`, `requiredness`, `applicability_trigger`, `stage_key`, `scope_mode`, `route_binding`, `version_snapshot_binding`, `integrity_rule`, `mapping_rule`, `evidence_rule`, `adjudication` y `rationale/provenance`. Es un contrato lógico contextual: no exige que todos los campos se apliquen a todas las capas ni les asigna valores por defecto.

Se reutilizan los siete `stage_key` aceptados en DEC-C10-071 y el token de scope global `C10S_SCOPE_GLOBAL` de DEC-C10-072; no se reabren ni amplían aquí.

**No aceptado/no fijado:** vocabulario cerrado de roles/namespaces; cardinalidades numéricas; valores finales REQUIRED/OPTIONAL/CONDITIONAL; endpoints externos; enum `relation_type`; mapping M concreto o split/merge; schema físico/DDL/FKs adicionales/API/registry/resolver; roster exhaustivo o IAM poblado.

El siguiente desarrollo puede proponer vocabularios candidatos por capa, separando roles UDG de roles funcionales REF. Cardinalidades, obligatoriedad y reglas concretas permanecen OPEN. No se modifica DEC-C10-077 ni se autoriza implementación, validator/parser, fixtures, Design Freeze, simulación, experimento o ejecución científica.

Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-078_IAM_LOGICAL_ROW_CONTRACT_ACCEPTANCE.md`.


### 19.13. Vocabularios candidatos separados para L2 y L3 — propuesta no aceptada

**Propósito.** Desarrollar DEC-C10-078 sin colapsar referencias del envelope UDG (L2) con relaciones funcionales REF (L3). Esta sección es una propuesta de trabajo, no una decisión aceptada ni un enum cerrado.

#### A. L2 — referencias del envelope UDG

Namespace candidato: `UDG_ENVELOPE_ROLE`. Los siguientes `role_key` reutilizan exclusivamente los ejemplos ilustrativos ya registrados; su presencia aquí no los convierte en vocabulario aprobado.

| role_key candidato | Función de la referencia del envelope | Dominio destino candidato | Límite / cuestión abierta |
|---|---|---|---|
| `MEMBER` | Identificar un miembro declarado del universo | CMP/PAR/REF/RUL/MET | La referencia apunta al registro exacto; no crea un REF. |
| `OWNER` | Identificar el owner del objeto declarado | CMP como caso ordinario | No sustituir identidad CMP por etiqueta de rol; otros dominios requieren contrato explícito. |
| `SOURCE` | Identificar fuente/origen de la declaración | CMP/PAR/REF/RUL/MET o artefacto externo tipado | El endpoint externo y su namespace siguen OPEN; no forzarlo a MET. |
| `INCLUSION_RULE` | Referenciar regla que determina inclusión | RUL | Resolver la regla no prueba exhaustividad ni pertenencia observada. |
| `EXCLUSION_RULE` | Referenciar regla que determina exclusión | RUL | Mismo límite: debe evaluarse sobre universo/scope/version exactos. |
| `DEPENDENCY` | Declarar/identificar dependencia relacionada con el envelope | OPEN: REF y/o target contractual | No inferir instalación, disponibilidad, consumo ni éxito técnico. No asumir que la referencia misma sea un objeto REF. |
| `PROVENANCE` | Referenciar procedencia de la definición | MET o artefacto/registro de evidencia tipado | Evidencia/procedencia no es automáticamente miembro del universo. |

La matriz no fija obligatoriedad ni cardinalidad para ninguna fila. El universo destino y el record_id deben ser exactos según DEC-C10-076. Un target externo exige contrato de tipo/namespace/versión/resolución antes de poder abandonar UNKNOWN.

#### B. L3 — extremos funcionales de objetos REF

Namespace candidato: `REF_FUNCTIONAL_ROLE`, distinto de `UDG_ENVELOPE_ROLE). L3 aplica a un objeto REF que ya tiene identidad propia; no a cada referencia del envelope.

| Campo | Propuesta de interpretación | Estado |
|---|---|---|
| `role_key` | Semántica funcional de la relación declarada por REF | OPEN; no se propone enum cerrado. `DEPENDS_ON` puede estudiarse como candidato solo para relaciones de dependencia efectivamente declaradas en el DGP. |
| `endpoint_position` | Posición del extremo dentro de la relación | SOURCE/TARGET como patrón binario de DEC-C10-078; no equivale a role_key. |
| `target_domain` | Clase/namespace del objeto al que apunta ese extremo | OPEN por extremo; distinguir dominios internos y externos. |
| `relation_type` | Tipo de relación declarado por el contrato REF | OPEN y separado de role_key y endpoint_position; no se acepta enum. |
| identidad del extremo | object_class + object_id + object_record_id y versión/snapshot compatibles | Reutiliza DEC-C10-076; nunca resolver por nombre, posición o latest implícito. |

Las relaciones n-arias requieren una identidad de grupo/parent explícita y una representación que conserve todos los extremos, dirección, tipo, multiplicidad e integridad. No se convierten automáticamente en pares SOURCE/TARGET ni en una colección de REF binarias sin mapping M explícito.

#### C. Separación de capas y reglas de no-colapso

- L2 referencia objetos/artefactos desde el envelope; L3 describe una relación del dominio cuyo objeto REF tiene identidad propia.
- El mismo texto —por ejemplo DEPENDENCY— podría aparecer como etiqueta ilustrativa en ambos contextos, pero no implica misma identidad, namespace, cardinalidad ni semántica.
- L1 sigue siendo membership de CMP/PAR/REF/RUL/MET; L4 sigue siendo integridad FK/vínculo estructural U_G. Ninguna de las dos capas hereda roles L2/L3.
- No inferir REF=0 por ausencia de MEMBER/DEPENDENCY en un envelope parcial, ni inferir dependencia técnica instalada desde una declaración REF.
- Para ambas capas, requiredness, cardinalidades, triggers, stage_key, scope, binding, integridad, evidencia y adjudicación deben justificarse por regla IAM y evidencia/cobertura. No asignar valores por defecto.

#### D. Siguiente gate propuesto

1. Validar conceptualmente cada fila L2 contra la gramática U1/UDG-04 y los dominios exactos del registry.
2. Determinar si DEPENDENCY en L2 apunta a un objeto REF o directamente a un target tipado, sin doble contabilización.
3. Construir ejemplos mínimos de REF L3 realmente necesarios para el DGP; no inventar relaciones adicionales.
4. Para cada REF, decidir si es binaria o n-aria y separar role_key, relation_type, endpoint_position y target_domain.
5. Solo después proponer cardinalidades/requiredness por clase×rol×extremo×stage_key×scope.

**Estado:** PROPUESTA NO ACEPTADA. No se cierra vocabulario, cardinalidad, obligatoriedad, endpoints externos ni mapping M. No se crean instancias/filas IAM, no se declara REF=0, y no se autoriza schema físico, implementación, parser/validator, fixtures, Design Freeze ni ejecución científica.

### 19.14. Resolución conceptual de DEPENDENCY en L2 — propuesta no aceptada

**Pregunta:** cuando el envelope UDG declara una dependencia, ¿la referencia L2 apunta al objeto dependiente directamente o a un objeto REF que representa la relación?

**Propuesta de resolución, condicionada al significado declarado:**

1. **Dependencia como relación del dominio de configuración:** si se afirma que un objeto de configuración depende de otro, L2 `DEPENDENCY` debe apuntar al registro REF exacto que representa esa relación. El REF conserva identidad propia y contiene sus extremos tipados, dirección, tipo/rol, multiplicidad e integridad. El envelope L2 referencia ese REF; no duplica sus extremos ni sustituye su identidad por la del target.
2. **Dependencia técnica/ambiental:** disponibilidad de servicio externo, runtime, recurso, permiso efectivo, instalación o condición de entorno pertenece a las condiciones técnicas/ambientales (p. ej. C_dep/E_dst) salvo que el DGP declare expresamente una relación de configuración como REF. No se crea un REF solo porque una condición técnica sea necesaria.
3. **Dependencias para evaluar un universo RULE_DEFINED:** las reglas y sus dependencias de resolución/evaluación deben permanecer como referencias tipadas/versionadas de la definición de universo/regla. No deben reutilizarse automáticamente como relación funcional REF ni confundirse con el role_key L2 `DEPENDENCY` de una relación de configuración.
4. **No doble contabilización:** si L2 apunta a REF, el objeto REF es la unidad de relación en L3; el objeto endpoint no se vuelve otra relación REF. Los extremos se resuelven por identidad exacta UDG-04. Una referencia L2 no crea un REF.
5. **Caso externo:** un REF de configuración puede tener un extremo externo solo con namespace, tipo, versión, identidad y política de resolución explícitos. Hasta entonces el extremo permanece UNKNOWN; no se sustituye por un identificador nominal ni se fuerza a MET.
6. **DGP base actual:** el roster mínimo aceptado CMP-SERVICE-LOGIC-001, PAR-SVC-ENABLED, PAR-SVC-PROFILE y RUL-SVC-ENABLE-PROFILE-01 no declara por sí mismo una relación REF. La cardinalidad REF=0 solo podrá adjudicarse después de inventario y cobertura exhaustivos pre-Z/B. No crear una fila DEPENDENCY ni un REF sintético por conveniencia del envelope.

**Consecuencia:** para el significado «relación de dependencia declarada en la configuración», el target de L2 es REF exacto, no el objeto dependiente directamente. El target directo queda reservado a referencias tipadas que expresen explícitamente otro propósito de envelope, no a una dependencia funcional encubierta.

**Estado:** PROPUESTA NO ACEPTADA. No se cierra el enum L2, ni se acepta cardinalidad/requiredness, ni se declara REF presente o ausente en la instancia. No modifica DEC-C10-076/077/078. No autoriza schema, resolver, parser/validator, fixtures, implementación, Design Freeze ni ejecución científica.

### 19.15. Conjunto mínimo de REF L3 exigido por el contrato sintético actual — auditoría propuesta

**Pregunta:** ¿qué objetos REF funcionales L3 exige realmente el contrato aceptado del servicio lógico?

| Elemento observado en el DGP/contrato | Interpretación correcta provisional | ¿Crea REF L3? |
|---|---|---|
| CMP-SERVICE-LOGIC-001 | Identidad del componente lógico | No por sí mismo |
| PAR-SVC-ENABLED / PAR-SVC-PROFILE | Propiedades tipadas del CMP | No; su ownership no crea una relación REF independiente |
| RUL-SVC-ENABLE-PROFILE-01 y sus operandos ENABLED/PROFILE | Regla constitutiva con AST y referencias a operandos PAR | No por sí mismo; los operandos pertenecen a la gramática/contrato RUL, salvo declaración independiente de relación REF |
| R_acc / R* en el generador TGCV | Relaciones/dependencias activas del espacio transformacional y de composición | No automáticamente; no son la clase REF del paquete de configuración |
| C_dep / E_dst, recursos, permisos efectivos, runtime, instalación y condiciones ambientales | Dependencias/condiciones técnicas externas | No automáticamente; permanecen en el plano técnico/ambiental |
| Dependencias de evaluación de universo RULE_DEFINED | Referencias tipadas/versionadas necesarias para evaluar regla y cierre del universo | No automáticamente; no son relaciones funcionales REF |
| Dependencia explícita entre objetos del paquete de configuración | Relación del dominio con identidad propia y extremos tipados | Sí: REF L3, si el contrato la declara expresamente |

**Resultado de la auditoría del roster mínimo:** no se identifica actualmente ningún REF funcional L3 exigido por el contrato mínimo aceptado CMP/PAR/RUL. Esto no prueba REF=0 para los snapshots reales ni para C_src/C_dst: el roster es mínimo, no exhaustivo. REF=0 solo podrá declararse por snapshot×etapa×ruta×scope después de enumeración exhaustiva, fuentes examinadas, denominador trazable y cobertura COMPLETE pre-Z/B.

**Regla de no-colapso:** no convertir operandos de RUL, FK U_G, R_acc/R*, dependencias ambientales o referencias de evaluación UDG en REF por semejanza nominal. Para añadir un REF candidato se debe aportar: identidad de la relación, source/target exactos, semántica de dominio, dirección/tipo/rol, multiplicidad, versión/snapshot y justificación de por qué no es solo una FK, condición externa o referencia de regla.

**Estado:** AUDITORÍA DOCUMENTAL PROPUESTA; no se declara REF=0 ni se sella roster/IAM. No se crea fila de instancia. La clasificación debe revisarse frente al inventario exhaustivo por snapshot antes de cualquier adjudicación. No autoriza implementación ni ejecución.

### 19.16. Protocolo de auditoría REF por snapshot y etapa — propuesta no aceptada

**Objetivo.** Convertir la conclusión negativa provisional de §19.15 en una inspección reproducible, sin crear registros hipotéticos ni declarar REF=0 a partir del roster mínimo.

#### A. Unidad de auditoría

La unidad mínima de adjudicación es la combinación exacta:
(contract_id/version, instance_id/version, snapshot_id, snapshot_object_record_id, stage_key, route_id o NONE justificado, scope, clase REF, universe_definition/version).

Cada combinación requiere un COVERAGE_REGISTER propio, con denominador, fuentes esperadas/examinadas/válidas, unidades cubiertas/excluidas y unidades opacas/desconocidas. Se reutilizan SNAPSHOT, COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER U_G; no se crea un inventario U_G paralelo.

#### B. Inspección por etapa

| stage_key | Ruta | Objeto inspeccionado | Pregunta REF específica | Límite |
|---|---|---|---|---|
| C_SRC | NONE | Paquete fuente exacto | ¿Qué relaciones REF funcionales declara el paquete fuente? | No inferir contenido de destino. |
| F1_S2 | F | Representación intermedia S2 | ¿Qué REF se preservan, transforman, dividen, agregan o pierden respecto de C_SRC bajo M? | S2 no prueba aplicación. |
| A1_S1 | A | Representación intermedia S1 | La misma inspección para la ruta A, con evidencia propia. | No copiar inventario ni resultado de F. |
| F2_DST_DECL | F | Paquete destino declarado antes de aplicar | ¿Qué REF declara la configuración preparada para F2? | No prueba estado aplicado. |
| A2_DST_DECL | A | Paquete destino declarado antes de aplicar | ¿Qué REF declara la configuración preparada para A2? | No heredar la declaración F. |
| F2_DST_APPLIED | F | Configuración efectivamente aplicada | ¿Qué REF existen y resuelven en el estado aplicado F2? | Exige snapshot y evidencia post-aplicación independientes. |
| A2_DST_APPLIED | A | Configuración efectivamente aplicada | La misma inspección para el estado aplicado A2. | Exige snapshot y evidencia post-aplicación independientes. |

#### C. Criterios para clasificar una relación como REF

Una candidata solo se registra como REF funcional si se acredita: (i) identidad propia de la relación; (ii) semántica de dominio declarada; (iii) extremos exactos por identidad lógica y record/version; (iv) dirección, tipo/rol y multiplicidad aplicables; (v) pertenencia al paquete de configuración; y (vi) procedencia y snapshot exactos.

No se elevan automáticamente a REF: EDGE de U_G, FK/ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos o referencias internas de RUL/AST, R_acc/R* transformacionales, dependencias técnicas C_dep/E_dst ni referencias usadas solo para resolver universos RULE_DEFINED. Si una estructura U_G corresponde además a una relación REF, la doble representación exige mapping M explícito/versionado y trazabilidad; no identidad por semejanza nominal.

#### D. Estados de adjudicación

- **1 / PRESENT:** REF identificado y respaldado por evidencia suficiente.
- **0 / ABSENT:** solo tras enumeración exhaustiva del universo y fuentes pertinentes, cobertura COMPLETE para el scope exacto y ausencia confirmada. REF=0 se adjudica por snapshot×stage_key×ruta×scope, nunca por extrapolación entre etapas.
- **? / UNKNOWN:** snapshot ausente, inspección parcial, universo/denominador no cerrado, fuentes no accesibles, mapping ambiguo o evidencia conflictiva/no suficiente.
- **NA:** únicamente si la clase/propiedad está fuera del dominio por regla ex ante explícita; no sustituye a un inventario vacío.

Un estado 0 requiere CLAIM_EVIDENCE_LINK y justificación de cobertura negativa. COMPLETE es relativo al universo operativo declarado/versionado y no implica exhaustividad ontológica. C_DST_DECLARED no permite inferir C_DST_APPLIED.

#### E. Salida mínima de la auditoría

Por cada REF candidato: ref_id/record_id/version, semantic role/relation type (sin enum supuesto), source endpoint y target endpoint exactos, dirección, multiplicidad, snapshot/stage/route/scope, mapping M si aplica, evidence/claim links, coverage_scope_id, adjudicación y rationale. Para una clase sin candidatos, conservar denominador y evidencia de enumeración que sustenten 0 o ?, sin crear una fila REF ficticia.

**Estado:** PROPUESTA NO ACEPTADA. No hay snapshots ni observaciones incorporados por esta sección; no se adjudica REF=0, no se sella IAM y no se autoriza schema físico, parser/validator, fixtures, implementación, Design Freeze ni ejecución científica.

## 19.17 — Matriz de inspección CMP/PAR/RUL/REF/MET por stage_key

**Estado:** PROPUESTA DOCUMENTAL DE INSPECCIÓN; no aceptada como cierre IAM, no implementada y sin observaciones reales. Deriva de DEC-C10-053/056/059/061/062/065/069/070/071/072/073/074/075/076/077 y de los contratos U_G y de instancia existentes. No altera cardinalidades, vocabularios ni obligatoriedad aprobados.

### Unidad de inspección
Cada observación se ancla a la tupla exacta de identidad de contrato/instancia y versión, snapshot y registro, `stage_key`, ruta o `NONE` justificado, scope y universo/versionado. Se reutilizan NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER de U_G. No se crea un inventario paralelo ni se generan registros ficticios.

### Matriz de búsqueda por clase × etapa

| Clase | C_SRC | F1_S2 | A1_S1 | F2_DST_DECL | A2_DST_DECL | F2_DST_APPLIED | A2_DST_APPLIED |
|---|---|---|---|---|---|---|---|
| CMP | Inventario e identidad fuente | CMP afectado y mapping F1 | CMP exportado y preservación | CMP destino declarado | CMP que A2 declara importar/aplicar | CMP producido/materializado por F2 | CMP realmente presente/aplicado |
| PAR | key, owner, tipo, state y value | Conversión, defaults, pérdidas y cambios | Estados/valores exportados | PAR destino declarado y conversión | PAR que A2 declara importar | PAR materializado por F2 | Estado/valor efectivamente aplicado |
| RUL | rule_id, AST, scope, efecto | Reglas transformadas/preservadas/omitidas | Reglas exportadas | Reglas destino y mapping | Reglas que A2 declara importar | Reglas materializadas | Reglas efectivas tras aplicación |
| REF | Inventario, identidad propia, endpoints | Transformación/correspondencia de relación | Referencias exportadas e integridad | REF destino declarada y mapping | REF que A2 declara importar/resolver | REF materializada | Resolución e integridad efectiva de extremos |
| MET | Identidad/versiones contrato, instancia, fuente, snapshot y provenance | Versiones de transformación y artefactos | Identidad de export, formato y lineage | Identidad/versiones destino y mapping | Identidad de import declarado | Artefacto producido, hash y lineage | Registro de aplicación, snapshot y evidencia posterior |

La matriz es un **mapa de inspección**, no una declaración de presencia. F1/A1/F2/A2 no crean automáticamente objetos semánticos. La presencia en cada etapa requiere evidencia específica. `C_DST_DECLARED` no prueba `C_DST_APPLIED`; una diferencia de hash/nombre no prueba equivalencia funcional.

### Evidencia mínima y adjudicación
- **CMP:** identidad semántica y registro exacto, clase/rol, boundary_class cuando proceda, scope y pertenencia al snapshot; mapping explícito para correspondencias entre etapas.
- **PAR:** parameter_key, owner, tipo, estado ABSENT/NULL/DEFAULT/VALUE, valor cuando corresponda, requiredness y dominio/unidad activados; no colapsar estados.
- **RUL:** rule_id, AST tipado, scope explícito (incluido GLOBAL), efecto REQUIRE/FORBID y precedencia/temporalidad solo cuando aplique.
- **REF:** ref_id/registro propio, extremos tipados SOURCE/TARGET, dirección, tipo/rol, multiplicidad si procede, pertenencia al paquete y provenance. No elevar EDGE, FK, ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos RUL, R_acc/R*, C_dep/E_dst ni refs RULE_DEFINED a REF funcional automáticamente.
- **MET:** identidades/versiones exactas, IAM_id/version/hash, mapping_id/version, oráculo/versión, timestamps y provenance de artefactos/evidencias. El hash es control de artefacto, no prueba semántica.

Estados por predicado y unidad de cobertura:
- `1`: presencia/condición acreditada por evidencia suficiente y coherente.
- `0`: ausencia/incumplimiento solo con búsqueda exhaustiva y cobertura COMPLETE del universo, etapa, ruta/scope y versión pertinentes.
- `?`: evidencia, resolución, mapping o cobertura insuficiente/contradictoria.
- `NA`: no aplicabilidad declarada ex ante en IAM, con fundamento de dominio; nunca por falta de evidencia.
- `NOT_COMPARABLE`: versiones/identidades sin mapping aprobado; no sustituir por 0.
- `NOT_APPLICABLE` solo cuando lo autorice el contrato aplicable, distinto de desconocido.

Para REF=0 se requiere inventario exhaustivo del límite funcional y cobertura exacta. La cardinalidad base permanece CMP≥1, PAR≥1, RUL≥1, REF≥0 y MET obligatorio; no se cambia por esta matriz. La aplicabilidad de una clase/propiedad en una etapa se decide con el contrato y el stage_key, no por extrapolación desde otra etapa.

### Exclusiones y salvaguardas
La inspección de CMP/PAR/RUL/REF se refiere al paquete P0. Entorno destino, runtime, recursos, permisos efectivos, C_dep y estados técnicos P1 se registran en sus objetos/mediciones correspondientes; no se incorporan al paquete ni se convierten automáticamente en REF. Las relaciones estructurales U_G (FK) siguen siendo distintas de REF. REF→EDGE requiere mapping M explícito/versionado; EDGE→REF no se infiere. Split/merge/n-aria exige identidad/grupo y regla de conservación explícitos.

### Estado actual
No se han inspeccionado snapshots reales ni se han asignado valores a ninguna celda. No se declara REF=0, cobertura COMPLETE, IAM sellado, cardinalidades adicionales, implementación, validación, fixtures, simulación o ejecución. La siguiente operación tras aceptación será completar el protocolo de extracción/registro de observaciones usando los snapshots existentes; si no hay snapshots, primero habrá que resolver esa ausencia sin fabricar datos.

## 19.18 — Gate de disponibilidad de snapshots y proyección U_G

**Estado:** HALLAZGO DOCUMENTAL / PROPUESTA DE GATE; sin datos observados ni decisión de implementación.

### Resultado de inspección
La plantilla canónica `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md` declara expresamente `DRAFT / PLANTILLA VACÍA / NO INVENTARIADA / NO EJECUTADA`. Sus filas ilustrativas son marcadores de esquema, no registros. El registro de snapshots contiene una fila de plantilla con `No capturado`; la matriz de cobertura está en `NONE` para sus dimensiones. Por tanto, en los artefactos revisados no hay snapshots C10-S reales utilizables ni evidencia de cobertura que permita iniciar extracción de observaciones. Esto no demuestra que no existan fuentes externas; significa que no están incorporadas ni referenciadas como observaciones U_G en esta rama.

### Hallazgo de proyección de clases
U_G dispone de diez registros canónicos: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. No hay tablas físicas independientes CMP, PAR, RUL, REF o MET. No se permite asumir equivalencias nominales:
- CMP: candidatos de representación en NODE según `semantic_role` y frontera, pero NODE no equivale automáticamente a CMP.
- PAR: no existe tabla PAR dedicada; la representación/serialización de propiedades debe quedar mapeada explícitamente a campos/artefactos y a su identidad de owner.
- RUL: PREDICATE registra predicados observados/analíticos; no equivale automáticamente a una regla declarativa RUL con AST, scope y efecto.
- REF: DEC-C10-077 distingue el objeto REF de EDGE y de FK estructural U_G. EDGE no es REF; REF→EDGE requiere mapping M explícito y versionado.
- MET: identidad, versión, snapshot y provenance se distribuyen entre campos de objetos, SNAPSHOT y EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK; MET no es una tabla ni un objeto homogéneo por defecto.

### Protocolo de extracción — cuando existan fuentes
1. Localizar la fuente original y registrar custodio, método, timestamp, versión/hash, alcance y limitaciones en EVIDENCE_REGISTER; no copiar secretos.
2. Verificar que corresponde al contrato/instancia exactos y al snapshot/fase temporal declarados. No emparejar por nombre, hash aislado ni `latest`.
3. Resolver el mapping clase conceptual→representación U_G mediante contrato explícito/versionado. Si no existe o no conserva semántica, adjudicar `UNKNOWN` o `NOT_COMPARABLE`, no forzar una fila.
4. Crear/actualizar registros U_G solo mediante el procedimiento autorizado; fijar snapshot y record IDs exactos, `stage_key`, ruta/scope y universo.
5. Registrar cada afirmación con CLAIM_EVIDENCE_LINK y EVIDENCE_REGISTER; cobertura con COVERAGE_REGISTER; evaluación/adjudicación separadas.
6. Mantener por separado declarado, producido y aplicado. Una fuente C_DST_DECLARED nunca acredita A2_DST_APPLIED.
7. Adjudicar 0 solo con búsqueda exhaustiva y COVERAGE_REGISTER COMPLETE para el universo, versión, etapa y scope exactos; ? ante falta de fuente/mapping/cobertura; NA solo por regla ex ante IAM.

### Gate previo a cualquier extracción
- Identificar fuente(s) real(es) y snapshots existentes; si no existen, definir por separado cómo se obtendrán y autorizar su captura.
- Resolver el crosswalk CMP/PAR/RUL/REF/MET↔U_G sin colapsar REF/EDGE ni RUL/PREDICATE.
- Confirmar identidad/versionado, stage_key, route/scope y snapshot pinning.
- Definir cobertura, evidencia y adjudicación por clase/etapa.
- Solo entonces completar observaciones. La plantilla no se rellena con ejemplos sintéticos ni valores inferidos.

**Conclusión:** no procede todavía extraer ni adjudicar observaciones. El siguiente trabajo documental es cerrar el crosswalk semántico de representación y especificar qué fuentes/snapshots alimentarán cada etapa. No se declara ausencia de objetos, REF=0, IAM sellado, cobertura COMPLETE ni disponibilidad de datos externos. `scientific_execution=false`; `execution_authorized=false`.

## 19.19 — Binding IAM de PAR y evidencia por propiedad

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

## 19.20 — Identidad de registro del manifiesto PAR

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

## 19.21 — Recomendación de cierre del registro PAR

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

## 19.22 — Binding normativo de identidad PAR (DEC-C10-079)

**Estado:** ACEPTADO — DEC-C10-079. Esta sección propaga el contrato lógico aprobado; prevalece sobre cualquier recomendación previa que mantuviera abiertas estas cuestiones.

- `manifest_record_id`: globalmente único en toda la línea C10-S, opaco, inmutable y nunca reutilizado, independiente de la versión IAM.
- Append-only: ninguna fila se sobrescribe ni elimina. Toda corrección de la misma captura lógica crea un nuevo ID y conserva el anterior.
- `manifest_record_revision`: revisión secuencial por clave lógica, desde 1, sin saltos.
- `supersedes_manifest_record_id`: en revisiones posteriores, referencia a la revisión inmediatamente anterior de la misma clave lógica. Cadena lineal única, sin bifurcaciones, ciclos, huérfanos ni referencias cruzadas.
- Cambio de snapshot, etapa, ruta/scope, contrato/instancia o revisión del CMP owner inicia una nueva clave lógica y revisión 1. Cambio semántico de `parameter_key` exige nueva identidad semántica.
- Múltiples evidencias no crean revisiones por sí solas. Reempaquetar en nueva versión IAM no crea automáticamente nueva observación; migración exige mapping explícito.

**Límites:** decisión documental lógica. No crea tabla/columnas PAR o U_G, DDL, serialización, generador, API, parser, validator, fixtures ni registros reales; no sella IAM, no cierra PAR↔U_G, no autoriza Design Freeze, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 19.23 — Regla de trazabilidad PAR sin FK propia

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

## 19.24 — Binding PAR aceptado (DEC-C10-080)

**Estado:** ACEPTADO — DEC-C10-080. Sustituye el estado pendiente de aceptación de §17.4/§19.23/§23/§16.65/§83/§210/§89.

- Afirmación sobre fila PAR: CLAIM_EVIDENCE_LINK usa `claim_target_type=COVERAGE_SCOPE` y FK `target_coverage_scope_id` al scope exacto `dimension=C10S_CONFIG_PAR`.
- `claim_statement` y `relevance_scope` contienen localizador lógico suficiente para resolver `manifest_record_id`, `manifest_record_revision`, `parameter_key`, owner CMP, snapshot/record, `stage_key`, ruta/scope y universo/version.
- Una fila CLAIM_EVIDENCE_LINK por evidencia×afirmación×fila PAR. Las evidencias múltiples se conservan como filas separadas, nunca como listas embebidas.
- Control independiente resuelve ID global y verifica revisión/supersession y coincidencia exacta de clave lógica, owner, snapshot, etapa, ruta/scope, coverage scope, universo, predicado y evidencia.
- Una afirmación separada sobre el CMP owner usa otro CLAIM_EVIDENCE_LINK con target NODE y FK exacta. No sustituye el target COVERAGE_SCOPE de la afirmación PAR.
- El enlace al scope no implica COVERAGE COMPLETE; se aplican U_G §12.3/§18.6.

**Restricciones:** no se añade target_type PAR, FK, tabla o puente. No se aprueban gramática, escaping, canonicalización, serialización, parser ni automatización. Los campos singulares `evidence_id`/`claim_evidence_id` del manifiesto no sustituyen el registro 1:N de CLAIM_EVIDENCE_LINK. No se crean observaciones, no se sella IAM, no se declara cobertura ni se autoriza implementación/ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 19.25 — Control PAR propuesto

**Estado:** PROPUESTA DOCUMENTAL; pendiente de aceptación. Desarrolla DEC-C10-080 reutilizando el C0 ya especificado en el protocolo de evidencia §19; no crea un segundo control genérico.

Se separan cinco capas: C0_SCOPE; PAR_ROW_BINDING; EVIDENCE_LINK_INTEGRITY; EVIDENCE_RELEVANCE; COVERAGE_COMPLETENESS. Se define una secuencia P0–P11 para aplicabilidad, target, resolución C0, dimensión/universo, identidad PAR global, clave lógica/pinning, supersession DEC-C10-079, evidencia, correspondencia de afirmación, pertinencia sustantiva, vínculo NODE separado solo si hay afirmación propia del owner y cobertura.

El control conserva resultados PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA por capa, sin colapsarlos. Un registro histórico superseded conserva validez histórica, pero no acredita estado actual sin justificación temporal. Una FK correcta no prueba pertinencia; un scope COMPLETE tampoco se infiere del vínculo.

Se añaden 18 casos adversariales documentales y requisitos de informe. Se reconocen expresamente las limitaciones ya detectadas en §20.1–20.5: mappings stage_key, clase y ruta aún abiertos producen UNKNOWN donde impiden resolución inequívoca.

No se amplía U_G ni se cierra gramática/escaping/canonicalización/predicate. No crea fixtures, parser, validator ni registros. No autoriza implementación, Design Freeze, validación técnica ni ejecución. `scientific_execution=false`; `execution_authorized=false`.

 
## 19.26 — Aceptación del control independiente PAR (DEC-C10-081)

**Estado:** ACEPTADO — contrato lógico documental.

Se acepta el protocolo §20.18 del protocolo de evidencia como control independiente del binding probatorio PAR, reutilizando C0 §19 y conservando las cinco capas, entradas mínimas, pasos P0–P11, estados por capa y 18 casos adversariales. La integridad del vínculo, la pertinencia sustantiva y la completitud de cobertura se evalúan separadamente.

Los mappings stage_key/clase/ruta y la gramática/escaping/canonicalización del localizador permanecen abiertos; sin resolución inequívoca corresponde UNKNOWN. Esta aceptación no sella IAM ni autoriza implementación, automatización, Design Freeze o ejecución. `scientific_execution=false`; `execution_authorized=false`.


## 19.27. Mapping candidato CMP→NODE por snapshot — dependencia del IAM

**Estado:** propuesta de correspondencia pendiente de aceptación; remite al contrato detallado del crosswalk §10.7. No modifica las decisiones DEC-C10-068/069 ni sella IAM.

Para cada CMP aplicable, el IAM deberá poder resolver exactamente un NODE anchor dentro del snapshot exacto `(snapshot_id, snapshot_object_record_id)`. Un NODE anchor no puede representar dos CMP distintos. NODE subordinados no se convierten automáticamente en CMP; requieren identidad funcional propia declarada ex ante.

La continuidad entre snapshots se prueba mediante `component_id` contractual estable y mappings versionados separados por snapshot. No se exige igualdad de `node_id`/ `object_record_id` entre snapshots. `stage_key` y `route_id/scope` diferencian filas de cobertura, no duplican el NODE.

La adjudicación exige comprobar identidad, snapshot y NODE record exactos, unicidad en ambos sentidos, universe_definition/version, scope C0, mapping/provenance y evidencia. Falta de universo o evidencia suficiente produce UNKNOWN; contradicción o cardinalidad múltiple produce FAIL; incompatibilidad semántica sin mapping aprobado produce NOT_COMPARABLE; NA requiere no aplicabilidad ex ante.

Esta propuesta no fija roster completo de CMP, no resuelve mappings P1, no crea columnas/FKs/tablas ni autoriza poblar IAM, implementar o ejecutar controles. `scientific_execution=false`; `execution_authorized=false`.


## 19.28. Aceptación del anclaje CMP↔NODE por snapshot — DEC-C10-082

**Estado:** ACEPTADO — contrato lógico documental.

Se acepta el anclaje 1:1 por CMP y snapshot: cada CMP aplicable resuelve a un único NODE anchor exacto dentro del snapshot; ningún NODE anchor representa dos CMP. La continuidad entre snapshots se basa en `component_id` contractual y mappings versionados separados, sin exigir igualdad de IDs U_G. `stage_key` y `route_id/scope` califican cobertura, no crean NODE por etapa/ruta.

Se aplican los estados y controles de §10.7 del crosswalk y DEC-C10-082. Un PASS solo demuestra correspondencia de identidad; no demuestra verdad PAR, preservación, pertenencia a ruta ni completitud del universo.

No se completa roster CMP ni mappings P1/PAR, no se sella IAM ni se autoriza implementación, Design Freeze o ejecución. `scientific_execution=false`; `execution_authorized=false`.


### 18.6. Propuesta de adjudicación PAR por los siete stage_key

**Estado:** propuesta documental pendiente de aceptación. Deriva del contrato funcional aceptado en DEC-C10-068, del vocabulario DEC-C10-071, de la identidad CMP DEC-C10-069 y de las reglas de estado de §§18.3–18.4. No sella filas IAM ni afirma que existan snapshots observados.

| stage_key | Objeto/posición | PAR-SVC-ENABLED | PAR-SVC-PROFILE | Qué se puede adjudicar |
|---|---|---|---|---|
| `C_SRC` | Configuración fuente declarada | REQUIRED; estado VALUE y BOOL del dominio | REQUIRED; estado VALUE y ENUM del dominio | Presencia, identidad/owner, tipo, dominio y valor fuente |
| `F1_S2` | Representación intermedia producida por F1 | Preservar estado y valor BOOL de origen mediante mapping versionado | Preservar estado, dominio y valor ENUM de origen mediante mapping versionado | Correspondencia semántica F1; no prueba aplicación en destino |
| `A1_S1` | Representación intermedia producida por A1 | Igual obligación de preservación, evaluada independientemente de F1 | Igual obligación de preservación, evaluada independientemente de F1 | Correspondencia semántica A1; no prueba aplicación en destino |
| `F2_DST_DECL` | Configuración destino declarada para F2 | REQUIRED; VALUE BOOL, sin DEFAULT implícito | REQUIRED; VALUE ENUM, sin DEFAULT implícito | Declaración destino antes de aplicación |
| `A2_DST_DECL` | Configuración destino declarada para A2 | REQUIRED; VALUE BOOL, sin DEFAULT implícito | REQUIRED; VALUE ENUM, sin DEFAULT implícito | Declaración destino antes de aplicación |
| `F2_DST_APPLIED` | Configuración observada tras aplicación F2 | Estado/valor aplicado observado; debe concordar con mapping y contrato | Estado/valor aplicado observado; debe concordar con mapping y contrato | Aplicación efectiva F2, con snapshot y evidencia independientes |
| `A2_DST_APPLIED` | Configuración observada tras aplicación A2 | Estado/valor aplicado observado; debe concordar con mapping y contrato | Estado/valor aplicado observado; debe concordar con mapping y contrato | Aplicación efectiva A2, con snapshot y evidencia independientes |

#### Reglas transversales de interpretación

1. Los dos PAR son P0 REQUIRED para la instancia sintética. Esta obligatoriedad conceptual no significa que cada fila ya esté observada ni adjudicada.
2. En `C_SRC`, `F2_DST_DECL` y `A2_DST_DECL`, la representación declarativa debe contener un valor `VALUE` tipado. No hay DEFAULT contractual aceptado; ABSENT/NULL incumplen el contrato cuando su presencia/ausencia se demuestra con cobertura suficiente.
3. En `F1_S2` y `A1_S1`, la obligación es preservación semántica independiente por ruta. El mapping puede cambiar representación física, pero no tipo/dominio/estado/valor sin regla explícita, total y versionada. La salida intermedia no se confunde con destino aplicado.
4. En `F2_DST_APPLIED` y `A2_DST_APPLIED`, la adjudicación requiere evidencia del estado realmente aplicado. No se infiere desde `*_DST_DECL`, desde el paquete preparado ni desde DEFAULT_ENV_RESOLVED.
5. La falta de snapshot, mapping, inspección o cobertura produce `?`/UNKNOWN; contradicción observada con evidencia suficiente produce `0` para el predicado predeclarado; `NA` requiere no aplicabilidad ex ante y no es admisible para los dos PAR en estas siete etapas del contrato base.
6. Cada fila debe vincular CMP owner exacto, snapshot exacto, `stage_key`, ruta/scope, `coverage_scope_id`, `parameter_key`, mapping/version y evidencia. La identidad NODE anchor sigue DEC-C10-082; no se crea NODE por PAR.
7. `E_dst/runtime` no es un octavo `stage_key` ni sustituye la configuración P0. Los valores resueltos por el entorno se registran como evidencia ambiental separada.

#### Precedencia sobre la tabla histórica de §13

La columna «Estados candidatos» de §13 es preliminar y queda precisada por §§18.3 y 18.6: para el núcleo aceptado no hay DEFAULT contractual; VALUE es el estado declarativo esperado; ABSENT/NULL no son admisibles para los dos PAR REQUIRED. La fila RETRY-COUNT permanece supersedida conforme a §18.2.

#### Límites

La tabla no asigna valores concretos a los escenarios, no fija tablas físicas de conversión, no adjudica predicados de preservación ya ejecutados y no completa la cobertura por snapshot. No sella IAM, no crea fixtures, parser, validator ni mappings físicos y no autoriza Design Freeze, implementación o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.

## 18.7. Aceptación — DEC-C10-083

**Estado:** ACEPTADA — contrato documental de aplicabilidad.

La tabla de §18.6 queda aceptada para `PAR-SVC-ENABLED` y `PAR-SVC-PROFILE` en las siete etapas DEC-C10-071. Se confirma P0 REQUIRED en todas ellas; VALUE tipado en las posiciones declarativas; preservación semántica independiente en F1/A1; y evidencia del estado efectivamente aplicado en F2/A2.

No hay DEFAULT contractual; ABSENT/NULL no son admisibles cuando su ausencia se demuestra con cobertura suficiente. La falta de evidencia o cobertura produce UNKNOWN, no ABSENT ni NA. `E_dst/runtime` permanece fuera de `stage_key`.

Rigen los detalles y límites de DEC-C10-083. La aceptación no adjudica observaciones, no asigna valores por escenario, no sella IAM ni autoriza mappings físicos, implementación o ejecución científica.


## 20. Reconciliación AB-01/02 con DEC-C10-083, U_G y la instancia RUL (2026-11-10)

Esta sección no modifica DEC-C10-083 ni duplica su tabla de siete etapas. La matriz §§18.6–18.7 conserva autoridad para la aplicabilidad y adjudicación de PAR. Se integra con DEC-C10-079/080 (identidad y vínculo PAR), DEC-C10-082 (CMP↔NODE por snapshot) y DEC-C10-054/068 (AST/RUL).

| Clase | Mapping semántico consolidado | Materialización documental existente | Límite abierto |
|---|---|---|---|
| CMP | Identidad contractual estable a través de snapshots | NODE anchor exacto por snapshot, 1:1 según DEC-C10-082 | Roster total, snapshots y evidencia material |
| PAR | ENABLED/PROFILE conservan clave, tipo, dominio, estado y valor según DEC-C10-083 | Manifiesto PAR + COVERAGE_SCOPE; propietario CMP exacto; sin NODE propio | Filas, mapping_id/version, cobertura y evidencia no poblados |
| RUL | Conservación de identidad, owner, scope, AST, operadores, operandos, bindings y REQUIRE | PREDICATE por snapshot exacto; bindings a claves PAR | Mapping/registro concreto y validación independiente |
| REF | Solo relaciones constitutivas inventariadas | EDGE conforme a contrato U_G | Universo REF desconocido; no afirmar REF=0 |
| POL | Ausente por diseño en núcleo confirmatorio | No materializar objeto POL | FP-05 se mantiene independiente |
| MET | Identidad/versionado/procedencia | Metadatos, snapshots y EVIDENCE_REGISTER existentes | Serialización canónica/hash OPEN |

### 20.1. Mappings de etapa y composición

Se distinguen M_F1_sem, M_F2_sem, M_A1_sem, M_A2_sem, con composiciones M_F_sem=M_F2_sem∘M_F1_sem y M_A_sem=M_A2_sem∘M_A1_sem. Ambas rutas conservan la misma semántica contractual; sus mecanismos técnicos no se presumen iguales ni independientes. La no-afectación de A por B se evalúa en escenarios DGP y no queda probada por igualdad de mappings.

### 20.2. Invariantes RUL

La expresión aceptada OR(NEQ(PAR-SVC-ENABLED,true),IN(PAR-SVC-PROFILE,{STANDARD,READ_ONLY})) bajo REQUIRE debe mantener operadores, operandos, dominio, scope, owner, efecto y TRUE/FALSE/UNKNOWN. Los dos operand bindings son AST→PAR, no REF/EDGE. Cualquier encoding físico alternativo debe decodificarse a la misma semántica bajo mapping versionado; no se define parser ni canonicalización.

### 20.3. Estado

AB-01 queda DESIGN RESOLVED en semántica, encoding/schema físico OPEN. AB-02 queda SEMANTIC CROSSWALK RECONCILED con DEC-C10-083; mappings versionados y evidencia material OPEN. No se sella IAM, no se declara REF=0 ni se crea schema freeze, fixture o ejecución.


## 20.4. Mapping P0/P1 a predicados de accesibilidad: resultado de frontera (2026-11-12)

Se incorpora el resultado del crosswalk D2 §9 sin duplicar la matriz IAM ni convertir el catálogo atómico en truth de accesibilidad:

- CMP IDs identifican contrato/instancia/componente del paquete; no identifican τ₂ ni satisfacen `ID_f*`.
- PAR-SVC-ENABLED y PAR-SVC-PROFILE son propiedades P0 REQUIRED; no prueban por sí solas ningún predicado de A_f*.
- RUL-SVC-ENABLE-PROFILE-01 y sus operand bindings son regla/AST→PAR; no crean REF ni `REL_f*`/`DEP_f*`.
- REF puede alimentar `REL_f*` únicamente si una relación declarada concreta es necesaria para τ₂. El roster mínimo no exige REF, pero REF=0 sigue prohibido sin cobertura exhaustiva por snapshot×etapa×ruta×scope; estado actual UNKNOWN.
- POL está ausente por diseño; no inferir autorización desde esa ausencia. `C_auth,base` es un contrato P1 distinto, conceptualmente alineado con `AUTH_f*`.
- `C_dep*` es éxito técnico de la dependencia provisionada y solo coincide con DEP bajo la hipótesis explícita de ruta única; no es A_f* completa.
- Recursos disponibles ex ante pueden alimentar RES si son necesarios y no duplicados. Consumo, carga y contención se separan como ejecución/colateral.
- MET/E_T y snapshots soportan identidad, procedencia y observación, no truth estructural ni ΔT_acc*.

El roster de τ₂, las interfaces, condiciones constitutivas, rutas completas/alternativas y bloqueos efectivos no están materialmente inventariados. No se rellena esa ausencia por inferencia desde el paquete P0. `scientific_execution=false`; `execution_authorized=false`.