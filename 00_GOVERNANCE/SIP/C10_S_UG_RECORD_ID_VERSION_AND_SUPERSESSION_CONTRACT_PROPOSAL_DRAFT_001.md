# C10-S — Contrato de identidad de registro, versionado y supersession U_G

**ID:** C10-S-UG-RECORD-VERSION-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** ACCEPTED DOCUMENTALLY — DEC-C10-062 / NO CONGELADA.  
**Hallazgo:** UG-SCH-07.  
**Dependencias:** DEC-C10-059, DEC-C10-060, DEC-C10-061; contrato de identidad/versionado y matching de snapshots.  
**No autoriza:** modificación de datos observados, inventario real, implementación, parser, constraints ejecutables, fixtures, simulación ni experimento.

## 1. Objeto y reconstrucción de lo ya decidido

UG-SCH-07 pide precisar el ámbito de unicidad de `object_record_id` y las reglas de `object_version` y `supersedes_record_id`.

Se preserva, sin reabrir, DEC-C10-061:
- `object_record_id` es UNIQUE dentro de cada una de NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT, y sirve como destino de sus FKs tipadas.
- Las claves semánticas existentes (`node_id`, `edge_id`, `route_id`, `predicate_id`, `snapshot_id`) se mantienen separadas de la identidad de la fila versionada.
- SNAPSHOT→NODE conserva la FK compuesta aceptada por DEC-C10-059.
- COVERAGE_REGISTER usa `coverage_scope_id` como PK/UNIQUE; no se fuerza `object_record_id` a esta tabla.
- La propuesta de identidad TID/SID/RID/EID y de matching semántico sigue gobernada por el contrato C10-S-ID-MATCH-001. Este documento no la sustituye.

La brecha residual es fijar formalmente el alcance y la secuencia de las revisiones de una fila lógica, así como impedir supersession cruzada, ambigua o cíclica.

## 2. Recomendación: tres identidades distintas

No deben colapsarse:

1. **Identidad semántica del objeto:** el ID propio de la tabla (`node_id`, `edge_id`, `route_id`, `predicate_id`, `snapshot_id`). Permanece estable solo mientras persista la identidad definida por el contrato de ese objeto.
2. **Identidad del registro:** `object_record_id`. Identifica una fila concreta e inmutable de una tabla concreta.
3. **Versión del registro:** `object_version`. Ordena las revisiones de una misma identidad semántica dentro de esa tabla. No es versión de software, build, SID/RID, catálogo ni snapshot del sistema.

Un cambio semántico material no se disfraza como revisión: requiere una nueva identidad semántica y, cuando proceda, una relación explícita de sucesión, derivación, split o merge bajo el contrato de matching.

## 3. Ámbito de unicidad

Se propone:

- `object_record_id`: identificador opaco, persistente, no vacío y UNIQUE **dentro de cada tabla de objetos** (NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT). No se exige unicidad global entre tablas, porque todas las referencias externas son tipadas y el tipo de destino forma parte de la clave.
- ID semántico de tabla: puede repetirse entre filas históricas de la misma entidad, pero no puede identificar dos entidades semánticas distintas dentro de su tabla.
- Clave de versión: UNIQUE por pareja (ID semántico, `object_version`) dentro de la tabla correspondiente.
- Se conserva la PK compuesta declarada actualmente en la matriz de esquema; la restricción UNIQUE de `object_record_id` es adicional y necesaria para las FKs tipadas de DEC-C10-061.

No se impone que el texto del ID codifique tipo, versión, fecha, estado, brazo, resultado o contenido. Los IDs retirados no se reutilizan.

## 4. Dominio y secuencia de object_version

Se recomienda tipar `object_version` como entero positivo (`INT >= 1`), no como cadena libre:

- primera fila de una identidad semántica: versión 1;
- cada revisión posterior: versión inmediatamente anterior + 1;
- no se permiten duplicados, saltos, reutilización ni decrementos dentro de la cadena;
- una corrección documental que afecte a la fila genera un nuevo registro; no sobrescribe el anterior;
- la versión de registro no sustituye los campos de versión técnica/contractual específicos del objeto.

La secuencia es local a cada identidad semántica y tabla; no es una secuencia global del inventario.

## 5. Contrato de supersedes_record_id

Para NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT:

1. La primera versión (`object_version=1`) tiene `supersedes_record_id=NULL`.
2. Toda versión posterior debe contener `supersedes_record_id` y apuntar a un `object_record_id` existente **en la misma tabla**.
3. El registro predecesor debe tener el mismo ID semántico y `object_version = versión actual - 1`.
4. `supersedes_record_id` no puede apuntar al propio registro, a una versión futura, a otra identidad semántica ni a otra tabla.
5. Cada registro puede ser supersedido por como máximo un sucesor inmediato. Se recomienda UNIQUE sobre `supersedes_record_id` dentro de cada tabla para impedir bifurcaciones de la cadena canónica.
6. La secuencia estrictamente creciente y la referencia exclusiva al predecesor inmediato impiden ciclos. El validador debe comprobar además que toda cadena tiene una única raíz (versión 1), un único extremo vigente y ninguna fila huérfana.
7. El registro anterior permanece íntegro e inmutable. La nueva fila no borra ni reescribe el historial.

La relación significa «revisión de la misma entidad semántica», no equivalencia funcional, causal ni de valor.

## 6. Casos que NO se representan con supersedes_record_id

No usar `supersedes_record_id` para:

- cambio material de identidad semántica;
- TID nuevo por cambio del contrato funcional;
- split 1:N o merge N:1;
- relación de alternativa, dependencia, composición o derivación;
- cambio de tabla/tipo de objeto;
- nuevo snapshot de captura con contenido o instante de observación distinto.

Estos casos requieren nueva identidad y la relación tipada/mapping que corresponda. Si la continuidad es incierta, se conserva `MATCH_UNRESOLVED / ?`; no se fuerza una cadena de supersession.

**Caso SNAPSHOT:** `snapshot_id` identifica una captura concreta. Una corrección de metadatos/procedencia de esa misma captura puede producir una nueva versión de registro que supersede la anterior. Una captura nueva, contenido observado distinto o nuevo instante de observación requiere nuevo `snapshot_id`; no se trata como revisión de la captura anterior.

## 7. Tiempo, inmutabilidad y snapshots

- `created_at` registra cuándo se incorporó la fila al registro (record-time); no equivale a cuándo el estado descrito fue válido u observado.
- Los campos temporales propios de cada tabla y el snapshot de referencia conservan el tiempo de observación/aplicabilidad conforme a sus contratos. No se infiere validez retroactiva por el mero hecho de crear una versión nueva.
- SNAPSHOT debe seguir apuntando a la versión exacta del NODE raíz mediante la FK compuesta ya aceptada; no se resuelve solo por ID semántico ni por «última versión».
- Una revisión nueva no altera el contenido ni las referencias históricas de snapshots anteriores.
- La corrección de un error en una fila se registra como nueva versión con explicación/procedencia; no se actualiza destructivamente la fila previa.

La propuesta no añade por ahora `valid_from/valid_to` genéricos. Si el dominio exige intervalos de validez distintos de los tiempos de observación ya existentes, deberán añadirse mediante decisión separada y contrato específico, sin reinterpretar `created_at`.

## 8. Tablas fuera del ámbito de esta regla

La cadena `object_record_id/object_version/supersedes_record_id` se aplica solo a las cinco tablas de objetos indicadas. No se extiende automáticamente a COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT o ADJUDICATION_REGISTER. Estas conservan sus claves propias y las FKs tipadas aceptadas. Cualquier versionado de esos registros requiere su propio contrato, no reutilizar implícitamente el de U_G.

## 9. Constraints y validaciones que deberán implementarse en un gate posterior

Por cada tabla de objetos:

- UNIQUE(`object_record_id`);
- UNIQUE(`semantic_id`, `object_version`);
- CHECK(`object_version >= 1`);
- FK autorreferente `supersedes_record_id → object_record_id` de la misma tabla;
- CHECK/trigger diferido que verifique mismo ID semántico y versión predecesora inmediata;
- UNIQUE(`supersedes_record_id`) para sucesor único, con tratamiento explícito del NULL según motor;
- validación de una raíz v1, secuencia contigua, un solo extremo vigente, ausencia de huérfanos y ausencia de ciclos;
- prohibición de UPDATE/DELETE destructivo de registros históricos, salvo mecanismo de corrección gobernado que preserve el original.

Los nombres concretos de constraints y la estrategia SQL/serializada quedan pendientes de elegir motor/formato. Una descripción documental de estas reglas no equivale a integridad física implementada.

## 10. Reconciliación y límites

La propuesta resuelve conceptualmente el ámbito de unicidad y el significado de las tres identidades, pero no cierra:
- la revisión integral de las diez tablas;
- el parser, tipos, constraints ni validaciones físicas;
- la seguridad/custodia de DGP_TRUTH_SECURE;
- el inventario real, la cobertura o la evidencia;
- la revisión independiente.

No cambia el DGP, el estimando, el Core TGCV, RMA, Evidence→Claim Matrix, claim status ni autorización científica.

## 11. Decisión adoptada — DEC-C10-062

Se recomienda aceptar este contrato con:
- unicidad de `object_record_id` por tabla, no global;
- `object_version` entero positivo, secuencial por identidad semántica;
- supersession autorreferente, en misma tabla e identidad, al predecesor inmediato;
- cadena lineal sin bifurcaciones, ciclos ni reescritura histórica;
- separación entre record-time y tiempo de observación;
- snapshots fijados a la versión exacta del registro raíz.

**Estado:** ACEPTED DOCUMENTALLY por DEC-C10-062. La plantilla U_G ha recibido el complemento normativo §12.12. No implica freeze ni validación física.


## 12. Addendum DEC-C10-064 — significado observacional de object_version

Bajo Opción A, object_version sigue siendo entero positivo, secuencial y lineal por identidad semántica, pero representa la revisión del registro observacional. Cada nueva aparición de una entidad semántica en un snapshot nuevo genera nuevo object_record_id y siguiente versión aunque la estructura observada sea idéntica. supersedes_record_id sigue apuntando al predecesor inmediato. Una versión nueva no prueba cambio material, cambio de accesibilidad ni cambio de evidencia. El diff debe comparar atributos/relaciones sustantivos entre snapshots comparables, excluyendo IDs opacos, record IDs, timestamps y números de versión como señales de cambio.


## 13. Addendum DEC-C10-065 — snapshot exacto y referencias de raíz

La revisión exacta de SNAPSHOT se identifica por `(snapshot_id, object_record_id)`. NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP fijan esa revisión mediante `(snapshot_id, snapshot_object_record_id)`. Las referencias interobjeto incorporan ambos componentes en las claves/FKs de origen y destino.

Para SNAPSHOT→NODE raíz, la FK compuesta vigente es:
`SNAPSHOT(snapshot_id, object_record_id, unit_object_record_id, unit_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id)`.
El object_record_id de SNAPSHOT ocupa el componente snapshot_object_record_id de NODE. Se mantiene semantic_role=LOGICAL_SERVICE_UNIT y la resolución de circularidad diferible/transaccional.

Este addendum completa la formulación previa de DEC-C10-062 sobre versión exacta del nodo raíz; no cambia el ámbito de object_record_id, la semántica observacional de object_version ni las reglas de supersession. La compatibilidad física sigue pendiente.
