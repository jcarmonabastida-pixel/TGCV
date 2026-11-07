# C10-S — Protocolo de fuentes, procedencia y adjudicación de evidencia U_G

**ID:** C10-S-UG-EVIDENCE-ADJUDICATION-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** DRAFT / PROPUESTA DOCUMENTAL / NO APROBADO / NO EJECUTADO.  
**Ámbito:** C10-S; U_G §81; contrato de frontera §82; plantilla y crosswalk §§83–84.

## 1. Propósito y límites

Establecer cómo seleccionar, registrar, valorar, triangular y adjudicar fuentes para inventariar nodos, aristas, predicados y rutas, y declarar cobertura sin confundir ausencia de evidencia con evidencia de ausencia.

Este protocolo es documental. No acredita fuentes concretas, no fija microdominio/F*, no completa el inventario y no autoriza inspección de sistemas reales, instalación, captura de snapshots, análisis runtime, pruebas funcionales, simulación ni experimento. Toda aplicación técnica requiere alcance, acceso, seguridad y autorización explícitos.

El universo inspeccionable es el universo operativo declarado y versionado, no la totalidad ontológica de posibles componentes. U_G es catálogo de inspección; Runknown permanece como categoría abierta.

## 2. Principios de evidencia

1. **Afirmación acotada:** cada evidencia respalda una afirmación concreta para identidad, versión, unidad, tiempo, entorno y alcance determinados.
2. **Procedencia reproducible:** conservar origen, custodio, método, fecha/hora, versión, hash/integridad, consulta/procedimiento y limitaciones.
3. **Separación de estados:** observed_state (1/0/?) no es evidence_status (AVAILABLE/MISSING/CONFLICTING) ni coverage_status (NONE/PARTIAL/COMPLETE).
4. **No inferencia por silencio:** búsqueda sin hallazgo no justifica 0 salvo que se demuestre que fuente y método cubren el universo relevante.
5. **Triangulación:** ninguna fuente aislada se considera universalmente exhaustiva. Para afirmaciones críticas se requiere corroboración independiente de fuentes o métodos distintos.
6. **Temporalidad y versión:** evidencia de una versión/ventana no se extrapola a otra sin regla de continuidad justificada.
7. **Cegamiento:** clasificación de accesibilidad, alternativas y cobertura sin Outcome/Value y, cuando sea viable, sin conocimiento de asignación.
8. **Truth separada:** truth_dgp_restricted pertenece al generador/evaluador autorizado; no se expone al analizador.
9. **No circularidad:** F*, criterios de ruta y oráculo se definen independientemente del Outcome/Value que se pretende explicar.
10. **Conservación del desacuerdo:** no promediar estados categóricos ni resolver conflictos por mayoría automática.

## 3. Clases de fuentes y jerarquía contextual

La jerarquía depende de la afirmación: una fuente primaria para una dimensión puede ser incompleta para otra.

| Clase | Ejemplos posibles | Respalda principalmente | Limitación típica |
|---|---|---|---|
| S1. Identidad/paquete declarativo | SBOM, lockfile, manifiesto, inventario, digest firmado | Identidad declarada, versiones, dependencias declaradas | No acredita carga/uso efectivo ni dependencias dinámicas |
| S2. Configuración y control | Configuración efectiva, ACL/IAM, políticas, cuotas, red, deployment manifests | Estado configurado, permisos y recursos declarados | Puede diferir de runtime o permiso efectivo |
| S3. Observación runtime | Procesos, módulos cargados, llamadas, trazas, sockets, logs, métricas | Carga/uso/relaciones observadas en ventana | Muestreo, rutas no activadas y eventos raros |
| S4. Snapshots e integridad | Snapshots inmutables, hashes, diffs, pre/post/rollback | Cambio/versionado/estado entre tiempos | Puede omitir superficies fuera de alcance |
| S5. Contratos/interfaz | API/schema, documentación, contratos existentes, proveedor | Semántica de interfaz, entradas/salidas, compatibilidad contractual | Contrato declarado no prueba comportamiento real |
| S6. Evidencia funcional independiente | Conformidad, pruebas autorizadas, oráculo cegado | Capacidad funcional y cumplimiento de F* | Éxito aislado no prueba cobertura ni independencia causal |
| S7. Documentación/entrevista | Manuales, tickets, diagramas, entrevistas con custodios | Descubrimiento, contexto, hipótesis y rutas potenciales | Secundaria, obsolescencia y omisiones |
| S8. Inferencia analítica | Análisis estático, resolución imports, cierre transitivo, correlación trazas | Relaciones inferidas y cierre del grafo | Requiere supuestos, método y límites de error |

No asignar calidad por el nombre del artefacto. Evaluar ajuste fuente-afirmación, integridad, actualidad, independencia, granularidad, cobertura y reproducibilidad.

## 4. Contrato de registro de procedencia

Cada evidencia tendrá evidence_id persistente y estos campos mínimos:

| Campo | Regla |
|---|---|
| evidence_id | ID único, estable y no semánticamente sobrecargado |
| claim_target | Nodo/arista/predicado/ruta/cobertura y afirmación exacta |
| source_class / source_type | S1–S8 y tipo concreto |
| source_provenance | Sistema/documento/origen, ubicación, custodio y autoridad |
| collection_method | Método, herramienta/consulta y versión; observación directa o inferencia |
| scope | Unidad, frontera, entorno, versión, rutas, tiempo/ventana y población cubierta |
| timestamp | Tiempo de captura y zona horaria; para intervalos, inicio/fin |
| integrity | Hash/digest, firma o control de integridad y resultado |
| version_identity | TID/SID/RID/EID cuando aplique, build, configuración y dependencias |
| access_lineage | Quién obtuvo, transformó, filtró y revisó el artefacto |
| completeness_limitations | Muestreo, filtros, exclusiones, no observables, retención y errores |
| confidentiality | Clasificación, permisos y ubicación segura |
| evidence_status | AVAILABLE / MISSING / CONFLICTING |
| reviewer | Evaluador, independencia, cegamiento y fecha |
| reproducibility | Procedimiento de recuperación/reproducción sin credenciales |

No almacenar credenciales, tokens, datos personales innecesarios ni secretos operativos en GitHub. Registrar referencias seguras y hashes cuando las fuentes primarias deban permanecer protegidas.

## 5. Evidencia mínima por tipo de objeto

### 5.1 Nodos

- **1 (presente):** evidencia primaria de identidad/versión en alcance y tiempo, más corroboración de configuración o runtime cuando la afirmación implique despliegue/uso. Una entrada SBOM acredita componente declarado, no necesariamente instalado/cargado.
- **0 (ausente):** enumeración completa y validada de superficies donde podría residir, control de alias/renombres/paquetes embebidos/carga dinámica y prueba de integridad/alcance. Si una superficie plausible queda opaca, ?.
- **?:** identidad ambigua, fuentes contradictorias, versión no resuelta, superficie no observada o cobertura insuficiente.

Separar componente declarado, instalado, desplegado, cargado, invocado y ejecutado.

### 5.2 Aristas y dependencias

- **1:** evidencia directa de relación dirigida/condicionada por configuración efectiva, importación/enlace, llamada/traza, permiso, flujo de datos o consumo de recurso. Indicar si es declarada, observada o inferida.
- **0:** cobertura de todas las superficies plausibles de relación para nodos/versiones/ventana; análisis estático y dinámico pertinente, alias/carga tardía y prueba de detección de la clase buscada. Falta de traza sin activar ruta no prueba ausencia.
- **?:** cierre transitivo incompleto, resolución dinámica, servicio opaco, telemetría incompleta o conflicto.

Calcular cierre transitivo solo sobre nodos/aristas con identidad y versión compatibles. Registrar ciclos, aristas condicionales, dependencias opcionales, fallbacks y nodos desconocidos. Una relación inferida no se etiqueta como observada directamente.

### 5.3 Predicados

Cada predicado requiere código exacto, ruta/paso/tiempo, definición operacional, fuente admisible, regla de clasificación y efecto sobre A_f*, App, Reach, F_alt o IV.

- **1:** todos los elementos necesarios están respaldados para unidad/versión/tiempo.
- **0:** evidencia válida de incumplimiento de una condición necesaria, o ausencia acreditada con cobertura suficiente cuando la definición lo requiera.
- **?:** evidencia parcial, conflicto, condición no observable o universo/cobertura insuficientes.

Para AUTH, verificar política y permiso efectivo del principal/contexto; RES separa capacidad instalada, disponibilidad temporal, reserva y consumo; DEP distingue C_dep de A_f*; BLOCK no convierte ausencia de logs en ausencia de bloqueo; APP se evalúa desde S0/estado hipotético; ALT-F* usa criterio común independiente; ORACLE versiona F*, implementación, tolerancias y cegamiento; EXT registra opacidad y frontera.

### 5.4 Rutas y substituibilidad

- **Ruta=1:** secuencia ordenada, identidades/versiones, condiciones y dependencias respaldadas; una ruta completa confirmada basta para Reach=1.
- **Ruta=0:** al menos un predicado necesario confirmado 0 dentro de alcance temporal/versionado.
- **Ruta=?:** ningún predicado necesario es 0, pero uno o más siguen ?; también si secuencia, identidad o dependencia no están resueltas.
- **Substituibilidad=1:** misma F*, entrada admisible común, C0, G, H, restricciones, tolerancias y oráculo independiente equivalente.
- **Substituibilidad=0:** evidencia suficiente descarta F* bajo el universo declarado.
- **Substituibilidad=?:** falta comparabilidad, cobertura, oráculo, dependencia o evaluación funcional.

Un éxito aislado no demuestra cobertura de entradas. Una ruta manual, externa, fallback o recovery puede ser substituible si satisface el mismo contrato; la etiqueta no decide el resultado.

## 6. Evidencia negativa y declaración de ausencia

Una afirmación de ausencia (nodo, arista, bloqueo, ruta o alternativa) requiere un argumento de cobertura negativa con:

1. universo operativo declarado, versión, unidad, contexto, tiempo y frontera;
2. listado de superficies/fuentes pertinentes y autoridad;
3. método de enumeración y capacidad de detección para esa clase de objeto;
4. evidencia de integridad, completitud y ausencia de filtros/exclusiones no resueltos;
5. tratamiento de alias, dependencias dinámicas, cargas tardías, servicios externos, fallback y rutas manuales;
6. cobertura por dimensión, omisiones y opacidades;
7. revisión independiente y regla de parada.

Si falta un elemento crítico, no se declara 0: se conserva ?. COMPLETE es local al universo declarado, no exhaustividad ontológica.

## 7. Cobertura: dimensiones, denominadores y estados

Informar cobertura por dimensión y fuente, no mediante porcentaje agregado. Cada fila especifica coverage_scope_id, universo/versionado, dimensión y denominador, fuentes requeridas/examinadas/válidas/no disponibles, unidades cubiertas/excluidas/opacas/no resueltas, regla de cálculo, justificación, revisor y fecha.

- **NONE:** no hay inspección sistemática válida para esa dimensión.
- **PARTIAL:** hay inspección, pero quedan unidades, versiones, ventanas, rutas o superficies materiales sin cubrir.
- **COMPLETE:** todas las unidades del universo operativo declarado están cubiertas por fuentes/métodos adecuados y las excepciones materiales se resolvieron o excluyeron justificadamente.

No promediar dimensiones para declarar cobertura global. Una dimensión crítica NONE/PARTIAL impide conclusiones que dependan de ella. Porcentaje de componentes conocidos no sustituye cobertura de dependencias transitivas o rutas.

## 8. Adjudicación independiente y discrepancias

1. Dos evaluadores clasifican independientemente con el mismo paquete de evidencia y reglas versionadas.
2. Ambos permanecen cegados a Outcome/Value y, cuando sea viable, a Z/B y a la hipótesis de brazo.
3. Cada evaluación conserva estado, evidencia citada, regla aplicada, limitación y razón para ?.
4. Se calcula acuerdo descriptivo por tipo; no se impone umbral estadístico sin diseño/volumen suficiente.
5. Toda discrepancia 1 vs 0, 1 vs ?, 0 vs ?, identidad/versionado, frontera, substituibilidad o cobertura crítica pasa a tercer revisor independiente.
6. El adjudicador no resuelve por mayoría simple: cita regla, compara fuentes, registra supuestos y explica por qué una evidencia es más adecuada.
7. Si persiste conflicto o falta cobertura, resultado final ?. Se conserva opinión minoritaria e historial.
8. Cambios de definición, fuente, versión, cobertura o regla generan nueva versión; no se sobrescribe clasificación anterior.

La independencia exige que evaluadores no compartan una inferencia no verificada como única fuente. Con una sola fuente, registrar limitación; no presentarla como corroboración independiente.

## 9. Reglas de decisión y propagación

- evidence_status=MISSING no implica observed_state=0.
- evidence_status=CONFLICTING fuerza observed_state=? hasta adjudicación.
- coverage_status=NONE implica ? para afirmaciones que dependan de inspección de ausencia.
- observed_state=0 exige evidencia válida y cobertura suficiente para el predicado concreto.
- Una ruta con predicado necesario 0 puede ser 0 en el alcance cubierto; con ? y ningún 0, ruta=?.
- Una ruta confirmada 1 basta para Reach=1; ausencia de rutas solo permite Reach=0 si universo/horizonte cubierto y Runknown resuelto.
- F_alt,0=0 requiere descartar todas las rutas substituibles en el universo F*, C0, G, H declarado; alternativa material desconocida mantiene ?.
- Independencia A1/A2 respecto de B exige cobertura de dependencias transitivas, permisos, recursos, datos, interfaces, servicios y cambios pre/post; unknowns críticos mantienen independencia=?.
- No derivar A_f* desde C_dep sin satisfacer el resto de predicados constitutivos.
- No derivar Value, Outcome, accesibilidad o substituibilidad desde etiqueta de ruta ni selección/ejecución observada.

## 10. Paquete de adjudicación y control de cambios

Cada ciclo futuro entrega: (a) manifiesto de alcance; (b) índice de fuentes; (c) registro de evidencia/procedencia; (d) tablas de nodos/aristas/rutas/predicados; (e) matriz de cobertura; (f) doble evaluación; (g) discrepancias/adjudicación; (h) informe de unknowns/vías colaterales; (i) hashes y versión del paquete.

La revisión verifica consistencia de IDs U_G, plantilla y crosswalk; ningún estado 1/0 sin vínculo válido CLAIM_EVIDENCE_LINK; todo estado ? sin vínculo debe justificar unknown_reason, MISSING y límites de búsqueda/cobertura; ningún 0 sin argumento de cobertura negativa; ningún COMPLETE sin denominador/alcance; ningún cambio de versión sin snapshot; ninguna truth DGP expuesta al analizador. `evidence_ref` es una referencia de navegación opcional, no un requisito de soporte.

## 11. Condiciones de parada

Mantener ? y detener la inferencia si: fuente primaria inaccesible; integridad fallida; alcance no declarado; versiones incompatibles; dependencia transitiva/dinámica desconocida material; servicio externo opaco relevante; ruta manual/fallback no examinada; cobertura crítica NONE/PARTIAL; desacuerdo no adjudicado; cegamiento roto sin control; F*/oráculo no independiente; o evidencia de ausencia insuficiente.

## 12. Estado y cuestiones abiertas

Protocolo candidato, no aprobación. Requieren revisión antes de freeze: correspondencia exacta entre campos y columnas de la plantilla; denominadores y criterios COMPLETE por dimensión en el microdominio seleccionado; evidencia específica por operación/servicio y límites de acceso/seguridad; número de evaluadores y adjudicación; tolerancias/fiabilidad del oráculo/error; plan de cegamiento y ruptura; delimitación del universo, horizonte y versiones.

No se han consultado fuentes técnicas de sistema real ni generado inventario. Cobertura efectiva NONE; A_f*, F_alt,0 y Reach_H siguen ?. No se cierran MD-C1…6, GC-01…12, UGI-01…07, UGC-01…06, AUD-005/007/010/011 ni OPEN-C10-001/003/005/007. No se aprueba microdominio, D1/D2, DGP ni freeze; no se autoriza implementación, simulación o ejecución.


## 13. Reconciliación con el esquema físico de captura

La auditoría campo-a-campo detectó que las reglas de este protocolo no tenían representación suficiente en las tablas abreviadas iniciales de la plantilla. La plantilla se amplía en §§12–13 con EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER con denominadores, EVALUATOR_ASSESSMENT, ADJUDICATION_REGISTER, esquema común de objetos y reglas de integridad referencial.

La cadena normativa de soporte es:
`typed target FK (NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE) → CLAIM_EVIDENCE_LINK → EVIDENCE_REGISTER.evidence_id`.
`object_record.evidence_ref` es únicamente un atajo de navegación opcional hacia un `claim_evidence_id`; su ausencia no elimina los vínculos normalizados. Los identificadores de evidencia y de afirmación no se confunden. Cada evidencia respalda una afirmación específica, con alcance compatible.

Se elimina la columna truth_dgp de la tabla de predicados analítica. La truth DGP queda segregada en el entorno del generador/evaluador autorizado, fuera de los artefactos accesibles al analizador. Esta separación es una condición de arquitectura y seguridad de información, no una mera etiqueta de columna.

La cobertura se normaliza con denominador, definición/versionado del universo, fuentes esperadas/examinadas/válidas, unidades cubiertas/excluidas/opacas, regla de finalización y excepciones. E1 y E2 conservan evaluaciones independientes; el tercer adjudicador registra su decisión y la posición minoritaria. El estado ? se conserva cuando el desacuerdo o la evidencia insuficiente no se resuelven.

La ruta utiliza parent_route_class con las cinco clases U_G y route_subtype separado. Los campos comunes de objetos, versiones, alcance, evidence_status, observed_state, adjudicación y supersession quedan definidos en la plantilla.

**Resultado de auditoría:** brechas FCM-01…09 identificadas y tratadas documentalmente. El esquema normalizado todavía no está validado por un parser, tipos/constraints ejecutables ni revisión independiente. No se ha aplicado a fuentes reales. No implica inventario ni cobertura; estados técnicos siguen ? y cobertura NONE. No se autoriza ejecución.


## 14. Reconciliación de tipos, cardinalidad e integridad de captura

La plantilla §§12.9–12.10 concreta tipos y dominios candidatos, cardinalidad de relaciones, claves lógicas y obligatoriedad por tabla. CLAIM_EVIDENCE_LINK es la relación 1:N canónica entre destinos identificados por FK tipada (incluido COVERAGE_SCOPE) y evidence_id; las referencias de navegación de las tablas no sustituyen ese conjunto. COVERAGE_REGISTER es el registro normativo; la tabla de §7 es solo vista resumen. E1/E2 se guardan en filas independientes; evaluator_record_ids no serializa múltiples evaluadores en una celda.

Los estados se mantienen ortogonales: observed_state {1,0,?,NA}; evidence_status {AVAILABLE,MISSING,CONFLICTING}; coverage_status {NONE,PARTIAL,COMPLETE}; review_adjudication_status usa el dominio definido en plantilla. Tiempos ISO 8601 con offset, hashes con algoritmo explícito y conteos enteros no negativos. COMPLETE exige denominador trazable.

Esta reconciliación es documental. No hay parser, constraints, base de datos ni validación de seguridad ejecutados. La plantilla y protocolo siguen Draft; revisión independiente y validación ejecutable quedan pendientes.


## 15. Referencias normalizadas por evaluador y adjudicación

La plantilla separa la clave `evaluator_record_id` (una fila por E1/E2) de la vista `evaluator_record_ids` en los objetos. `CLAIM_EVIDENCE_LINK` puede asociar cada vínculo a un `evaluator_record_id` o `adjudication_id`, de forma que la evidencia efectivamente revisada por cada rol se reconstruye por relaciones y no por listas serializadas. `EVALUATOR_ASSESSMENT` y `ADJUDICATION_REGISTER` utilizan seis FKs tipadas exclusivas (NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE); la adjudicación referencia las dos evaluaciones originales y conserva la posición minoritaria.

La comprobación estática de encabezados/separadores/filas de esquema muestra alineación de columnas en las diez tablas revisadas. No acredita integridad referencial de instancias, unicidad, dominios ni comportamiento de parser. Sigue siendo necesaria revisión independiente y validación ejecutable autorizada.


## 16. Cardinalidad de referencia de navegación — FCM-20

Se confirma que `evidence_ref` en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT es cero o un vínculo de navegación opcional. No representa la relación completa de evidencias. Todas las relaciones 0..n entre objetos/afirmaciones y evidencias, incluidas las revisadas por E1/E2/adjudicador, se conservan en CLAIM_EVIDENCE_LINK. El registro completo se recupera por la FK destino tipada y, cuando proceda, evaluator_record_id/adjudication_id. La corrección armoniza la plantilla §§12.7/12.9 y el protocolo §§13–15.

FCM-20 es corrección documental; no valida cardinalidad de instancias ni FK en motor.


## 17. Regla adoptada de obligatoriedad — UG-SR-A01

La frase histórica de §10 «ningún estado sin evidence_ref» se considera imprecisa y queda sustituida por la siguiente regla adoptada:

1. `evidence_ref` es opcional (0..1), solo de navegación. Si está poblado, debe resolver a un `claim_evidence_id` válido.
2. Todo registro real con `observed_state=1` o `0` requiere al menos un vínculo CLAIM_EVIDENCE_LINK válido y de alcance compatible. Para `0`, además, se exige cobertura negativa suficiente.
3. Un registro con `observed_state=?` puede carecer de vínculo únicamente si documenta `unknown_reason`, `evidence_status=MISSING` y las limitaciones de búsqueda/cobertura; si hay evidencia pertinente sobre la incertidumbre, debe vincularse.
4. `NA` exige justificación de no aplicabilidad y no requiere vínculo por defecto.
5. CLAIM_EVIDENCE_LINK mantiene la relación canónica 0..n; EVIDENCE_REGISTER conserva las fuentes/artefactos y sus versiones.

Esta reconciliación resuelve documentalmente la contradicción entre §§10, 13, 14, 16 y la plantilla §§11, 12.8–12.9. **Aceptada documentalmente por decisión explícita del usuario (2026-11-05).** SR-03 permanece CONDITIONAL hasta validación técnica de instancias, cardinalidad y FK; esta aceptación no implica freeze ni revisión independiente.


## 18. Referencias tipadas y procedencia canónica — DEC-C10-061

El usuario acepta la arquitectura de referencias tipadas. CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER admiten seis destinos tipados (NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE); exactamente una FK debe estar poblada y concordar con el enum de tipo. `object_record_id` es UNIQUE dentro de cada tabla de objetos; `coverage_scope_id` es PK/UNIQUE. `source_provenance` se conserva canónicamente en EVIDENCE_REGISTER y no se duplica en tablas de objetos.

La plantilla U_G refleja esta decisión. La especificación de CHECK/FK es documental: no hay parser, motor relacional, constraints ni pruebas negativas ejecutadas. DEC-C10-061 no implica freeze, inventario real ni ejecución científica.

## 19. Especificación documental del control independiente C0 — COVERAGE_SCOPE_BINDING_CONTROL (Draft 001)

**Autoridad:** DEC-C10-070. **Estado:** especificación documental propuesta; no implementada, no ejecutada, no auditada.  
**Propósito limitado:** comprobar que cada `coverage_scope_id` usado por un registro C10-S identifica un único universo de cobertura, anclado a un snapshot/registro exacto, y que ningún registro consume ese scope desde otra etapa, ruta, clase o versión.

### 19.1. Unidad de control y binding canónico

La unidad primaria es una fila de `COVERAGE_REGISTER` identificada por `coverage_scope_id`. Su binding C0 debe declarar, en `universe_definition/version`, una única tupla:

`(contract_id, contract_version, instance_id, instance_version, snapshot_id, snapshot_object_record_id, stage_key, route_id, object_class, dimension)`.

Los valores deben ser explícitos, no inferidos de nombres libres, hashes, timestamps ni proximidad de filas. `route_id` puede ser un identificador reservado explícito para el scope global de una etapa solo si el contrato de universo lo define como tal; NULL, vacío o comodín no significan global. `object_class` usa el vocabulario controlado CMP/PAR/REF/RUL/MET. `dimension` identifica la dimensión concreta de cobertura del registro. La versión de contrato e instancia forma parte de la identidad: no se permite herencia silenciosa desde la versión más reciente.

Cada fila de objeto que referencia el scope debe aportar una identidad compatible y resolver al mismo `snapshot_id + snapshot_object_record_id`, `stage_key`, `route_id`, `object_class`, `dimension`, contrato e instancia. Si alguna de estas correspondencias no puede recuperarse de los campos versionados o de una declaración inequívoca del universo, el resultado no puede ser PASS.

### 19.2. Invariantes obligatorios

| ID | Invariante | Criterio |
|---|---|---|
| C0-I01 | Identidad de scope | `coverage_scope_id` identifica una sola fila canónica COVERAGE_REGISTER en el conjunto cerrado examinado. |
| C0-I02 | Binding total | Los diez elementos de la tupla están declarados, versionados y no ambiguos; no se aceptan comodines implícitos. |
| C0-I03 | Snapshot exacto | `snapshot_id` y `snapshot_object_record_id` identifican la misma revisión exacta, no solo la misma entidad semántica. |
| C0-I04 | Consistencia de consumidores | Todos los registros que referencian el scope coinciden con la tupla completa. |
| C0-I05 | Separación de universos | No se mezclan contratos, versiones de instancia, snapshots, etapas, rutas, clases ni dimensiones distintas bajo un scope. |
| C0-I06 | Referencias resolubles | Toda FK `coverage_scope_id` resuelve a una fila COVERAGE_REGISTER; no hay referencias huérfanas. |
| C0-I07 | Cardinalidad declarada | El conjunto observado de consumidores concuerda con el universo/denominador y con la regla de enumeración versionada. |
| C0-I08 | Uso/no uso justificado | Todo scope declarado como requerido tiene consumidores según su cardinalidad; un scope sin consumidores solo es admisible si el universo declara explícitamente cero consumidores y la enumeración es exhaustiva. |
| C0-I09 | Integridad del denominador | Denominador, unidad, fuentes esperadas/examinadas/válidas, cubiertas, excluidas y opacas/desconocidas son coherentes y trazables. |
| C0-I10 | No inferencia de ausencia | NONE/PARTIAL/UNKNOWN o falta de fila no se convierten en ausencia. REF=0 requiere denominador cero y enumeración exhaustiva, conforme al contrato de cobertura vigente. |
| C0-I11 | Inmutabilidad/provenance | La entrada de control identifica versiones, hashes, timestamp, herramienta/control versionado y conjunto exacto de filas examinadas; no sobrescribe registros. |

### 19.3. Reglas de evaluación del contenido de cobertura

1. `denominator_unit_and_count` debe declarar unidad y entero no negativo; la definición y versión del universo deben permitir reconstruir cómo se enumeró.
2. `covered_units/count`, `excluded_units/reason` y `opaque_or_unknown_units/count` deben ser disjuntos o disponer de una regla explícita de solapamiento; no sumar porcentajes incompatibles.
3. `covered + excluded + opaque/unknown` debe reconciliarse con el denominador según la regla de enumeración. Toda diferencia sin explicación es FAIL si se demuestra inconsistencia; UNKNOWN si faltan datos para decidir.
4. `expected_sources`, `examined_sources` y `valid_sources` deben respetar la relación declarada por la regla de universo. Una fuente esperada no examinada no puede contarse como válida.
5. `COMPLETE` solo puede aceptarse si el denominador es finito y trazable, la enumeración es exhaustiva, las fuentes esperadas han sido examinadas y son válidas, las excepciones están resueltas/justificadas y no quedan unidades opacas/desconocidas materiales. COMPLETE es relativo al universo operativo declarado, no a exhaustividad ontológica.
6. `PARTIAL` expresa cobertura incompleta del universo declarado; `NONE` expresa que no se ha cubierto ninguna unidad, no que no existan unidades; `UNKNOWN` se conserva cuando no se puede fijar denominador, enumeración o correspondencia.
7. Un universo con denominador cero puede pasar la integridad C0 únicamente si la regla de enumeración y las fuentes demuestran exhaustividad del cero. Ese PASS estructural no autoriza por sí solo una afirmación REF=0; deben cumplirse además todas las condiciones de evidencia negativa y adjudicación aplicables.
8. La ausencia de un registro de objeto no equivale a ausencia del objeto. No se emite REF=0 a partir de una consulta vacía sin demostrar cierre del universo.

### 19.4. Resultado trivalente y precedencia

El control devuelve exactamente uno de estos resultados por scope y uno agregado:

- **PASS:** todos los invariantes aplicables fueron evaluados con entradas completas y versionadas; no se detectaron violaciones; universo y cardinalidad están reconciliados.
- **FAIL:** existe al menos una violación demostrada (binding contradictorio, duplicidad, FK huérfana, versión/snapshot/ruta/clase incorrectos, cardinalidad incompatible o contradicción aritmética).
- **UNKNOWN:** no hay violación demostrada, pero una o más comprobaciones necesarias no pueden evaluarse por campos ausentes, universo no exhaustivo, versión/hash no recuperable, fuente no examinada o ambigüedad.

**Precedencia:** cualquier FAIL demostrado domina a UNKNOWN; si no hay FAIL pero queda al menos una comprobación necesaria sin resolver, resultado UNKNOWN; solo el cierre completo sin violaciones permite PASS. No existe PASS parcial. Los controles no aplicables deben registrar motivo y regla, no desaparecer del informe.

### 19.5. Casos adversariales mínimos y resultados esperados

| Caso | Perturbación deliberada | Resultado esperado | Razón |
|---|---|---|---|
| ADV-C0-01 | Tupla completa y todos los consumidores coinciden | PASS | Binding íntegro |
| ADV-C0-02 | Un objeto apunta a otro `snapshot_id` | FAIL | Cruce de snapshot |
| ADV-C0-03 | Mismo `snapshot_id`, distinto `snapshot_object_record_id` | FAIL | Revisión exacta distinta |
| ADV-C0-04 | Mismo nombre de instancia, distinta `instance_version` | FAIL | Versiones no equivalentes |
| ADV-C0-05 | Consumidor con `route_id` diferente | FAIL | Scope de ruta cruzado |
| ADV-C0-06 | Consumidor CMP bajo scope PAR, o dimensión distinta | FAIL | Clase/dimensión contaminada |
| ADV-C0-07 | Dos definiciones/filas canónicas para el mismo `coverage_scope_id` | FAIL | Identidad no unívoca |
| ADV-C0-08 | Registro consumidor referencia un scope inexistente | FAIL | FK lógica huérfana |
| ADV-C0-09 | Scope requerido sin consumidores aunque universo declara cardinalidad positiva | FAIL | Cardinalidad/uso contradictorios |
| ADV-C0-10 | Scope sin consumidores y sin declaración exhaustiva de universo vacío | UNKNOWN | No se puede distinguir cero real de omisión |
| ADV-C0-11 | Denominador, versión de universo o regla de enumeración ausente | UNKNOWN | Cobertura no evaluable |
| ADV-C0-12 | Fuente esperada no examinada o unidades opacas sin resolver | UNKNOWN para COMPLETE | No hay cobertura exhaustiva demostrada |
| ADV-C0-13 | Denominador cero con enumeración exhaustiva y fuentes cerradas | PASS estructural C0; REF=0 sujeto a gate de evidencia negativa | Cero demostrado, no inferido |
| ADV-C0-14 | `covered + excluded + opaque` contradice el denominador | FAIL si la contradicción es demostrable; UNKNOWN si faltan conteos | Reconciliación cuantitativa |
| ADV-C0-15 | Hash/versión del snapshot o del universo no recuperable | UNKNOWN | No se puede fijar identidad/provenance |

Los casos son especificaciones de pruebas futuras, no resultados ejecutados.

### 19.6. Registro de ejecución y evidencia exigida

Cada futuro informe de control deberá registrar, como mínimo: `control_id`, `control_version`, `run_id`, fecha/hora y zona, versión/hash de herramienta, commit de la especificación, identidad/hash del universo, contract/instance y versiones, snapshot y snapshot_object_record_id, coverage_scope_id, lista cerrada de object_record_id examinados, invariantes evaluados, resultado por invariante, resultado agregado, excepciones, unknown_reason, evidencia de entrada/salida, responsable y adjudicación/revisión.

El informe debe permitir reproducir qué filas se incluyeron y cuáles quedaron fuera. No se admite que el control consulte silenciosamente el estado más reciente o que complete versiones por heurística. El output del control es evidencia de integridad de binding; no demuestra por sí solo que las fuentes sean verdaderas, que el inventario sea ontológicamente completo o que una afirmación causal de TGCV sea válida.

### 19.7. Gates y límites

- **Ahora:** especificación documental únicamente. No parser, SQL, script, fixtures poblados, ejecución de casos adversariales ni validación física.
- **Antes de implementar:** revisión del DDL completo, correspondencia real de campos que componen la tupla, regla exacta de cardinalidad/denominador, contrato de exportación y decisión/ autorización técnica específica.
- **Antes de ejecutar:** autorización explícita del control y conjunto de datos congelado/versionado; separar prueba del control de ejecución científica.
- **Antes de Design Freeze:** todos los casos adversariales ejecutados con resultados auditables, revisión de falsos PASS/FAIL/UNKNOWN, integridad de provenance y adjudicación.
- Un PASS del control C0 no convierte automáticamente `coverage_status=COMPLETE`, `observed_state=0`, `REF=0` ni una afirmación causal en PASS. Son capas de evidencia distintas.

**Estado:** DOCUMENTED SPECIFICATION / NOT IMPLEMENTED / NOT EXECUTED / NOT AUDITED. `scientific_execution=false`; `execution_authorized=false`.
