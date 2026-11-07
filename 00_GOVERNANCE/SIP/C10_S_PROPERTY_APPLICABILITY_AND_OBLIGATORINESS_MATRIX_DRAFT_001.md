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
