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
