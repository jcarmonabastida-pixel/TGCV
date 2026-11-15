# C10-S — Gate 107: identidad y granularidad de las afirmaciones lifecycle

**Estado:** HISTORICAL RECONSTRUCTION COMPLETED / EXISTING LINK-TO-ADJUDICATION NAVIGATION PATH CONFIRMED / STATE-CLAIM GRANULARITY CONDITIONALLY REPRESENTABLE / CROSS-EVIDENCE CLAIM IDENTITY NOT GUARANTEED / OCCURRENCE IDENTITY NOT REPRESENTABLE AS NORMALIZED EVENT / MINIMUM SEMANTIC CONTRACT PROPOSED / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Precedencia:** Gates 103–106; Gate 98 successor; U_G Inventory Register Template Draft 001 §§2, 5, 12.1–12.10, 15.4–15.6, 17–20; U_G Evidence/Provenance/Adjudication Protocol Draft 001 §§8–10, 13–17; DGP Temporal and Role Contract; DEC-C10-061/065/070/071/083/088. No se modifica ninguna decisión aceptada.

---

## 1. Pregunta y dictamen ejecutivo

Gate 107 resuelve una pregunta más acotada que Gate 106:

> ¿Puede el esquema U_G actual identificar, versionar y adjudicar afirmaciones lifecycle de NODE con granularidad suficiente, o requiere una identidad claim-level nueva?

La respuesta no es binaria para todos los casos.

1. **La capacidad relacional existente es mayor que la descrita inicialmente en Gate 105.** CLAIM_EVIDENCE_LINK dispone de claim_evidence_id y puede referenciar opcionalmente un evaluator_record_id singular y un adjudication_id singular. ADJUDICATION_REGISTER enlaza las dos evaluaciones E1/E2 y conserva decisión y posición minoritaria. La cadena permite navegar desde una fila concreta de claim-evidence hasta una adjudicación y, desde ella, hasta ambas evaluaciones. Es una asociación relacional documental; no garantiza por sí sola que el target de la adjudicación sea una proposición claim-level, porque EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER conservan target tipado de objeto y no una FK a claim_id.
2. **Para una afirmación de estado de NODE con una única evidencia o un paquete de evidencia previamente consolidado**, esa granularidad puede bastar documentalmente si la fila CLAIM_EVIDENCE_LINK se trata como la unidad adjudicable y se impone un contrato semántico explícito: una proposición por fila, dimensión lifecycle explícita en claim_statement/relevance_scope, target NODE exacto y evaluación con scope/regla idénticos. No hace falta afirmar que la estructura sea incapaz de cualquier adjudicación claim-specific.
3. **Para una misma afirmación respaldada por varias filas CLAIM_EVIDENCE_LINK**, el esquema no ofrece una clave común de afirmación. Repetir el texto no crea una FK ni garantiza que las filas sean la misma proposición, la misma revisión semántica, ventana, población o scope. claim_evidence_id identifica cada vínculo, no el claim compartido. Por tanto, la agrupación y la evolución/versionado de una afirmación a través de varias evidencias no están garantizados.
4. **Para ocurrencias individuales INVOKED/EXECUTED**, claim_evidence_id tampoco es un event_id: identifica el vínculo probatorio, no el acto ocurrido. La referencia a NODE solo identifica el componente/objeto, no una invocación concreta. CLAIM_EVIDENCE_LINK puede documentar una afirmación textual sobre una ocurrencia localizable en una fuente, pero no normaliza multiplicidad, correlación, reintentos, orden ni identidad del evento.
5. **No se justifica todavía añadir un claim_id global ni aceptar PROCESS_EVENT.** La mínima convención documental puede cerrar parte del problema de claims de estado; la identidad compartida entre múltiples evidencias sigue abierta. Para ocurrencias, se necesita una identidad de evento si el estimando/análisis requiere consultar episodios individualmente, pero su representación física depende del contrato PROCESS_EVENT y de las decisiones correspondientes.

**Dictamen:** GATE_107_LINK_TO_ADJUDICATION_NAVIGATION_PATH_CONFIRMED / CLAIM_TARGET_EXCLUSIVITY_NOT_CONSTRAINED / STATE_CLAIMS_CONDITIONALLY_DOCUMENTABLE / CROSS_EVIDENCE_CLAIM_IDENTITY_NOT_GUARANTEED / OCCURRENCE_IDENTITY_NOT_NORMALIZED / NO_GLOBAL_CLAIM_ID_APPROVED / NO_PROCESS_EVENT_ACCEPTANCE / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.

## 2. Reconstrucción histórica y correcciones

### 2.1. Gate 103 — suficiencia conceptual, no identidad estable

Gate 103 concluyó que U_G tiene capacidad conceptual para registrar afirmaciones, evidencia, cobertura, evaluaciones y adjudicaciones. No afirmó que la identidad de cada afirmación estuviera normalizada. Su suficiencia era condicional y documental; no probó observabilidad real, validación de FKs ni instancias.

### 2.2. Gate 105 — precisión necesaria

Gate 105 detectó correctamente que:
- claim_statement y relevance_scope son campos descriptivos, no una clave de afirmación;
- claim_evidence_id identifica una relación claim-evidence, no una identidad de claim común a varias evidencias;
- los evaluadores/adjudicadores tienen como target un objeto tipado, no un claim_id autónomo;
- no están definidos un tipo/revisión de claim lifecycle ni un contrato físico por dimensión.

Pero su frase de que las evaluaciones/adjudicaciones no tienen una FK inequívoca a nivel claim debe interpretarse con precisión. La plantilla sí permite que cada fila CLAIM_EVIDENCE_LINK referencie opcionalmente un evaluator_record_id y un adjudication_id. Esa FK da un enlace inverso desde el vínculo probatorio concreto al registro de evaluación/adjudicación. Lo que falta no es toda asociación relacional, sino una identidad común para una proposición que se respalda con varios vínculos, y restricciones de cardinalidad que hagan inequívoca su evaluación conjunta.

### 2.3. Gate 106 — corrección incorporada

Gate 106 ya rectificó la lectura absoluta de Gate 105. Gate 107 la desarrolla: distingue tres granularidades que no deben colapsarse:

- **Objeto:** NODE y su revisión exacta.
- **Afirmación:** proposición lifecycle delimitada por dimensión, estado, tiempo/ventana y alcance.
- **Vínculo probatorio:** relación de esa afirmación con una evidencia concreta y su evaluación/adjudicación asociada.

Una misma afirmación puede tener varias evidencias; una misma evidencia puede respaldar varias afirmaciones. La plantilla permite esta estructura a nivel de vínculos, pero no contiene un identificador común de la afirmación entre varias filas.

### 2.4. Antecedentes de plantilla y protocolo

- U_G Template §12.1: un evidence_id representa un artefacto/fuente y versión exacta; puede respaldar varias afirmaciones.
- §12.2: CLAIM_EVIDENCE_LINK tiene claim_evidence_id, target tipado, claim_statement, evidence_id, support_type, relevance_scope, evaluator_record_id opcional y adjudication_id opcional.
- §12.4: EVALUATOR_ASSESSMENT tiene evaluator_record_id, target tipado, evaluator_id, rol E1/E2, observed_state, rule_version, scope_id, cegamiento, limitaciones y rationale.
- §12.5: ADJUDICATION_REGISTER tiene adjudication_id, target tipado, FKs a evaluaciones E1/E2, decisión, regla/razón, posición minoritaria y limitaciones.
- §15: CLAIM_EVIDENCE_LINK puede asociar el vínculo con los registros de evaluación y adjudicación; la cadena se reconstruye por relaciones, no por listas serializadas.
- §16: evidence_ref de NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT es navegación opcional 0..1; no representa el conjunto de evidencias.
- §17: la obligatoriedad de evidencia para observed_state 1/0 se cumple mediante al menos un CLAIM_EVIDENCE_LINK válido; para ? sin evidencia se documentan unknown_reason, MISSING y límites.
- §18 / DEC-C10-061: los seis destinos tipados se mantienen cerrados; no se añade PROCESS_EVENT.

La plantilla y el protocolo siguen Draft y no validados técnicamente. Sus relaciones documentales no deben describirse como FKs ejecutadas ni como esquema aceptado.

## 3. Tres granularidades y sus claves actuales

| Nivel | Identidad actual | Qué identifica | Qué no identifica |
|---|---|---|---|
| Objeto | object_record_id + node_id + object_version; snapshot exacto cuando aplica | Revisión de NODE | Una afirmación lifecycle concreta |
| Vínculo probatorio | claim_evidence_id | Una relación target–claim_statement–evidence | Una proposición estable común a varias evidencias |
| Evaluación | evaluator_record_id | Una evaluación E1/E2 con regla/scope/target | Automáticamente una afirmación compartida por varias filas |
| Adjudicación | adjudication_id | Resolución de dos evaluaciones sobre target tipado | Una familia de claims agrupada si no hay clave común |
| Fuente | evidence_id | Artefacto/fuente y versión | Un evento ni una afirmación |
| Ocurrencia | No existe clave normalizada aceptada para INVOKED/EXECUTED | — | Identidad individual de un acto runtime |

La FK opcional de CLAIM_EVIDENCE_LINK a evaluator_record_id (singular) y adjudication_id (singular) permite una ruta de navegación **desde el vínculo**. El vínculo directo evaluator_record_id puede apuntar a una evaluación; la referencia a adjudication_id permite alcanzar el par E1/E2 que la adjudicación registra. Pero las tablas de evaluación/adjudicación siguen targeteando el objeto, no la proposición. Por ello, la relación no demuestra que la evaluación sea semánticamente exclusiva de ese claim si el mismo objeto/scope contiene varias proposiciones. Tampoco convierte claim_evidence_id en clave de una afirmación que sobreviva a la sustitución/añadido de fuentes.

## 4. Subcaso A — afirmaciones de estado sobre NODE

### 4.1. Semántica requerida

Para DECLARED, INSTALLED, DEPLOYED y, cuando sea apropiado como estado acotado, LOADED, la unidad de afirmación debe especificar:

1. NODE semántico y object_record_id/object_version exactos.
2. Una sola dimensión lifecycle por afirmación.
3. Proposición verificable y dirección: presencia/estado 1, ausencia/estado 0 o indeterminado ?.
4. Unidad/entorno/instancia y frontera donde se evalúa.
5. Tiempo de validez o ventana observada; no confundir timestamp de evidencia con vigencia del estado.
6. Snapshot exacto si la afirmación requiere estado estructural capturado y DEC-C10-065 resulta aplicable.
7. Scope de cobertura compatible, sin inventar coverage_scope_id ni debilitar C0/DEC-C10-070.
8. Evidencia pertinente, regla versionada, evaluaciones E1/E2 y adjudicación cuando proceda.
9. Separación de observed_state, evidence_status, coverage_status y truth_dgp.

No se admite una afirmación genérica “NODE presente” para inferir las seis dimensiones.

### 4.2. Qué puede hacerse con el esquema actual

La estructura actual puede representar documentalmente un claim de estado por vínculo si se usa una convención de granularidad estricta:
- una fila CLAIM_EVIDENCE_LINK representa una sola proposición lifecycle sobre un NODE exacto y una fuente/versión concreta;
- claim_statement expresa la dimensión y el estado afirmado;
- relevance_scope expresa unidad, entorno, ventana/tiempo, versión y alcance;
- support_type distingue soporte directo, inferido, contradictorio o contextual;
- EVALUATOR_ASSESSMENT se crea para ese target y scope/regla, y su evaluator_record_id se referencia desde la fila de vínculo;
- E1 y E2 permanecen separados; el adjudication_id solo se usa cuando existe adjudicación válida y apunta a los registros originales;
- una fila de objeto no hereda automáticamente la evaluación de otra dimensión o de otro scope.

Esto permite una **ruta documental de asociación a granularidad de vínculo**, condicionada a que target, dimensión, regla y scope de la adjudicación coincidan exactamente con la proposición del vínculo. No equivale a tener un objeto claim independiente ni a una restricción técnica que asegure que la adjudicación no se reutiliza para otra proposición del mismo objeto. Si se pretende que la misma proposición agregue varias evidencias, la convención no puede agruparlas con garantías relacionales.

### 4.3. Varias evidencias para una misma afirmación

Hay tres opciones documentales:

**A1. Una fila de vínculo por evidencia, con texto/scope repetidos.**  
Permite conservar todas las fuentes, pero la igualdad de claim_statement/relevance_scope no es identidad: diferencias de texto, versión, ventana o error tipográfico pueden separar afirmaciones idénticas o unir afirmaciones distintas. No es suficiente como identidad estable.

**A2. Un paquete consolidado de evidencia registrado como un único evidence_id.**  
Puede ser admisible cuando exista realmente un artefacto compuesto, versionado, íntegro y con índice de sus componentes, custodio y método. No es admisible crear un bundle ficticio para ocultar varias fuentes independientes ni perder sus procedencias, timestamps o evaluaciones diferenciadas. Es una opción de empaquetado de evidencia, no un sustituto universal de claim_id.

**A3. Una sola fila CLAIM_EVIDENCE_LINK con una fuente y evaluaciones vinculadas.**  
Es la representación mínima más clara para un claim de estado respaldado por una evidencia/paquete exacto. No resuelve la agregación de varias evidencias independientes ni la persistencia de la identidad del claim a través de ellas.

**Conclusión A:** para claims de estado de una única fuente/paquete, el esquema actual es documentalmente utilizable bajo convención estricta. Para un claim con múltiples evidencias independientes que deban agregarse como una sola proposición adjudicada, la identidad común no está garantizada. claim_id sería una extensión justificable solo si el análisis exige esa agrupación/versionado como unidad independiente; no se aprueba ahora.

## 5. Subcaso B — ocurrencias INVOKED y EXECUTED

### 5.1. Diferencia ontológica

- **INVOKED:** acto de invocar/llamar una operación, con identidad de invocación, actor/proceso, target, contexto, tiempo y resultado de la invocación.
- **EXECUTED:** operación efectivamente iniciada/ejecutada según el criterio técnico declarado; no implica éxito funcional ni resultado correcto.
- **SUCCESS/FAILURE:** resultado de ejecución, dimensión separada; una ejecución con error sigue siendo una ejecución si el criterio de inicio/ejecución se cumple.
- **LOADED:** puede ser estado durante una ventana o una transición de carga individual; el DGP/fuente debe fijar cuál es el objeto de afirmación.

Una invocación no prueba ejecución completada; ejecución no prueba éxito funcional. Ausencia de log no demuestra ausencia de acto salvo cobertura negativa S3 adecuada.

### 5.2. Capacidad del esquema actual

CLAIM_EVIDENCE_LINK a NODE puede respaldar “se observó INVOKED/EXECUTED para el componente X en la ventana Y”, siempre que el localizador de la fuente permita recuperar inequívocamente el episodio. Sin embargo:
- la fila identifica el vínculo de evidencia, no la ocurrencia;
- NODE identifica el componente, no la llamada/ejecución concreta;
- claim_statement/relevance_scope son texto y no proporcionan una clave de evento normalizada;
- no se pueden garantizar cardinalidad, deduplicación, correlación, retries, causal links ni orden de episodios;
- una evaluación sobre NODE no se convierte por ello en evaluación de cada ocurrencia.

Por tanto, el esquema actual puede respaldar un claim textual sobre un episodio, pero no ofrecer una tabla normalizada de eventos para análisis longitudinal/multiplicidad.

### 5.3. Umbral para necesitar event_id

Un event_id/event_record_id normalizado es necesario si el análisis pretende cualquiera de estas operaciones:
- contar ocurrencias distintas;
- deduplicar reintentos/duplicados de captura;
- asociar cada invocación con una ejecución o resultado;
- ordenar episodios usando tiempos comparables;
- reconstruir secuencias, retries, relaciones PRECEDES/CAUSES o correlaciones;
- evaluar por episodio en lugar de por componente/ventana.

Si el análisis solo requiere una afirmación agregada “ocurrió al menos una invocación dentro de la ventana”, puede permanecer como claim de estado/ventana sobre NODE con fuente S3 y limitaciones explícitas, sin fabricar un registro PROCESS_EVENT. El estimando y la medición deben decidir la granularidad requerida; no el deseo de normalizar todos los logs.

**Conclusión B:** claim textual respaldado por evidencia S3 puede registrarse hoy a nivel documental; una ocurrencia consultable/contable requiere identidad de evento. Gate 98 Opción B y DEC-C10-061 permanecen sin modificación.

## 6. Matriz de suficiencia

| Requisito | Esquema actual | Dictamen |
|---|---|---|
| Identidad exacta de NODE | object_record_id + node_id/version | Disponible documentalmente, condicionado a matching |
| Separar seis dimensiones lifecycle | claim_statement/relevance_scope + NODE §12.7 conceptual | Parcial; requiere convención una dimensión por claim |
| Un claim de estado + una evidencia | CLAIM_EVIDENCE_LINK + E1/E2/adjudicación referenciados | Suficiente documentalmente bajo convención |
| Un claim + varias evidencias independientes | Varios CLAIM_EVIDENCE_LINK sin clave común | No garantizado |
| Evaluación por vínculo concreto | FK opcional evaluator_record_id/adjudication_id | Representable documentalmente |
| Evaluación por claim estable agregado | No existe claim_id compartido ni target de evaluación claim-level | No garantizado |
| Versionado de definición del claim | Sin claim_revision/claim_type | No disponible como clave explícita |
| Ventana/scope | relevance_scope y scope_id; texto/contrato | Parcial, exige semántica exacta |
| Ocurrencia individual INVOKED/EXECUTED | CLAIM_EVIDENCE_LINK a NODE y fuente S3 | Evidencia/afirmación textual, no evento normalizado |
| Multiplicidad/correlación/retry | Sin event identity aceptada | No disponible |
| Cobertura negativa | COVERAGE_REGISTER + C0 | Condicionada a scope válido; DEC-C10-070 intacta |
| Truth DGP / observed firewall | Protocolo de segregación | Documental; no validado técnicamente |

## 7. Contrato semántico mínimo provisional (sin DDL)

Se establece como **regla de documentación propuesta**, no como nuevo esquema ni como aceptación del inventario:

### 7.1. Claim de estado

Una fila CLAIM_EVIDENCE_LINK destinada a respaldar un estado NODE debe representar una sola dimensión lifecycle, un NODE/revisión exactos, un alcance temporal/contextual y una fuente/versión exacta. El texto y scope deben ser suficientemente explícitos para distinguir claims distintos sobre el mismo objeto. Cada E1/E2 debe referirse al mismo target exacto, dimensión, regla y scope; el vínculo opcional desde CLAIM_EVIDENCE_LINK a evaluator_record_id/adjudication_id debe usarse para identificar qué evaluación revisó ese vínculo. No inferir que todas las filas del mismo NODE son el mismo claim.

### 7.2. Varias fuentes

Si dos o más fuentes sustentan la misma afirmación:
- conservar cada evidence_id y su provenance;
- conservar los vínculos claim-evidence separados;
- si la identidad compartida es necesaria para agregar/adjudicar las fuentes, marcar CLAIM_GROUP_IDENTITY_OPEN y no fusionar por texto;
- solo usar un evidence bundle si existe como artefacto real, versionado y con componentes recuperables;
- no usar evidence_ref del objeto como sustituto de los vínculos 0..n.

### 7.3. Ocurrencias

Para INVOKED/EXECUTED:
- conservar el artefacto S3, versión, localizador, ventana y límites de captura;
- no fabricar event_id ni filas PROCESS_EVENT;
- cuando el episodio no sea recuperable con identidad inequívoca, mantener la afirmación agregada en ?/OPEN;
- si el análisis necesita multiplicidad/secuencia, elevar la necesidad de evento normalizado a una decisión separada y resolver Opción B Gate 98 y DEC-C10-061 antes de materializar.

### 7.4. No inferencias

No derivar:
- INSTALLED desde DECLARED;
- DEPLOYED desde INSTALLED;
- LOADED desde DEPLOYED;
- INVOKED desde LOADED;
- EXECUTED desde INVOKED;
- SUCCESS desde EXECUTED;
- ausencia desde falta de log;
- equivalencia de claims desde igualdad de texto;
- identidad de claim desde claim_evidence_id;
- evento desde proximidad a SNAPSHOT o timestamp.

## 8. Decisión de diseño y cuestiones abiertas

1. No se añade claim_id, claim_type ni claim_revision en Gate 107.
2. Se reconoce la ruta documental de navegación desde CLAIM_EVIDENCE_LINK hacia EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER mediante las FKs opcionales ya definidas; la exclusividad claim-target no está constreñida.
3. Se limita la suficiencia actual a claims de estado de una dimensión por vínculo, target NODE exacto, scope/ventana y fuente/paquete inequívocos.
4. La agrupación de varias filas de evidencia bajo una afirmación común permanece OPEN; no se resuelve por texto repetido ni por bundle artificial.
5. Las ocurrencias INVOKED/EXECUTED no se normalizan en NODE ni en CLAIM_EVIDENCE_LINK; event identity sigue OPEN y condicionada a necesidad analítica.
6. No se acepta PROCESS_EVENT Opción B ni se amplía DEC-C10-061.
7. DEC-C10-065/070/071/083/088 y C0 permanecen intactas.
8. No se crea una tabla paralela, no se modifica el catálogo PREDICATE y no se alteran los seis destinos tipados.
9. No se realiza DDL, parser, validator, implementación, inventario material ni ejecución.

## 9. Gaps remanentes

| ID | Gap | Estado |
|---|---|---|
| G107-01 | Claim state unitario por link con semántica explícita | DOCUMENTABLE UNDER CONVENTION; no validado |
| G107-02 | Claim identity compartida por varias evidencias | OPEN |
| G107-03 | claim_type/claim_revision explícitos | OPEN; no aprobados |
| G107-04 | Asociar E1/E2/adjudicación al claim agregado | LINK-LEVEL NAVIGATION PATH AVAILABLE; claim-target exclusivity not constrained |
| G107-05 | Seis dimensiones lifecycle como campos tipados de NODE | OPEN; no se requieren seis booleanos |
| G107-06 | INVOKED/EXECUTED event identity | OPEN; necesidad depende de análisis |
| G107-07 | LOAD como estado vs ocurrencia | OPEN; DGP/fuente deben fijar unidad |
| G107-08 | S3 episode locator, deduplication, correlation and retries | OPEN |
| G107-09 | Claim scope/window and snapshot compatibility | DOCUMENTARY RULE DEFINED; mapping por fuente abierto |
| G107-10 | Validación de cardinalidad/FKs/constraints | NOT EXECUTED |

## 10. Siguiente operación

**Gate 108 — decisión de necesidad analítica de identidad claim/event y cierre de la unidad de observación.**

Antes de diseñar campos:
1. recuperar los estimandos, variables observadas y reglas de adjudicación que consumen cada dimensión lifecycle;
2. determinar si el analizador necesita afirmaciones de estado por ventana o episodios individuales;
3. para cada variable, fijar unidad de observación, target, granularidad, temporalidad y multiplicidad;
4. identificar qué operaciones analíticas exigen claim_id compartido o event_id;
5. comparar coste de convención documental, paquete de evidencia real y extensión estructural mínima;
6. emitir una decisión por necesidad, no una extensión global.

No iniciar DDL ni cambios en DEC-C10-061 hasta que el requisito de análisis haga imprescindible una clave nueva. No reabrir la decisión de cobertura C0.

## 11. Límites y control

Auditoría documental asistida, no revisión independiente. Se inspeccionaron contratos y plantillas versionados; no se consultaron sistemas reales, fuentes S3, snapshots poblados, evaluaciones o adjudicaciones ejecutadas. No se generaron claims ni eventos. No se validaron FKs, constraints, cardinalidades, parsers, reglas de reloj ni seguridad del firewall.

scientific_execution=false; execution_authorized=false.

**Dictamen final:** GATE_107_LINK_TO_ADJUDICATION_NAVIGATION_PATH_CONFIRMED / CLAIM_TARGET_EXCLUSIVITY_NOT_CONSTRAINED / STATE_CLAIMS_CONDITIONALLY_DOCUMENTABLE / MULTI_EVIDENCE_CLAIM_IDENTITY_OPEN / OCCURRENCE_IDENTITY_NOT_NORMALIZED / NO_GLOBAL_CLAIM_ID_APPROVED / NO_PROCESS_EVENT_ACCEPTANCE / C0_UNCHANGED / NO_DECISION_AMENDMENT / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_DESIGN_FREEZE.
