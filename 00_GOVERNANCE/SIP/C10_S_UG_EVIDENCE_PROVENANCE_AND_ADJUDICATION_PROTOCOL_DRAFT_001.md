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

`(contract_id, contract_version, instance_id, instance_version, snapshot_id, snapshot_object_record_id, stage_key, route_id, object_class)`.

Los valores deben ser explícitos, no inferidos de nombres libres, hashes, timestamps ni proximidad de filas. `route_id` puede ser un identificador reservado explícito para el scope global de una etapa solo si el contrato de universo lo define como tal; NULL, vacío o comodín no significan global. `object_class` usa el vocabulario controlado CMP/PAR/REF/RUL/MET. `dimension` identifica la dimensión del scope en COVERAGE_REGISTER, pero no forma parte de la tupla de identidad aceptada por DEC-C10-070. La versión de contrato e instancia forma parte de la identidad: no se permite herencia silenciosa desde la versión más reciente.

Cada fila de objeto que referencia el scope debe ser compatible con los nueve componentes de la tupla. La dimensión se comprueba separadamente contra COVERAGE_REGISTER.dimension y la regla de elegibilidad versionada; no se incorpora a la tupla. Si alguna correspondencia no puede recuperarse de los campos versionados o de una declaración inequívoca del universo, el resultado no puede ser PASS.

### 19.2. Invariantes obligatorios

| ID | Invariante | Criterio |
|---|---|---|
| C0-I01 | Identidad de scope | `coverage_scope_id` identifica una sola fila canónica COVERAGE_REGISTER en el conjunto cerrado examinado. |
| C0-I02 | Binding total | Los nueve elementos de la tupla están declarados, versionados y no ambiguos; no se aceptan comodines implícitos. |
| C0-I03 | Snapshot exacto | `snapshot_id` y `snapshot_object_record_id` identifican la misma revisión exacta, no solo la misma entidad semántica. |
| C0-I04 | Consistencia de consumidores | Todos los registros que referencian el scope coinciden con la tupla completa. |
| C0-I05 | Separación de universos | No se mezclan contratos, versiones de instancia, snapshots, etapas, rutas o clases distintas bajo un scope; la dimensión del scope debe concordar con su regla de universo y no se fusionan dimensiones incompatibles. |
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

## 20. Reconciliación de la tupla C0 con el esquema U_G vigente

**Resultado de inspección documental:** la tupla C0 aceptada no está íntegramente representada mediante columnas tipadas en las tablas actuales. Por tanto, §19 define el contrato semántico, pero todavía no existe mapping físico suficiente para declarar PASS de consumidores. No se propone añadir columnas en esta operación.

| Elemento C0 | Representación documentada actualmente | Evaluación de correspondencia |
|---|---|---|
| contract_id / contract_version | Declaración en `universe_definition/version`; no son columnas propias de COVERAGE_REGISTER ni de las tablas de objeto | DOCUMENTAL; requiere identidad/versionado inequívoco del contrato |
| instance_id / instance_version | Declaración en `universe_definition/version`; no son columnas comunes de las tablas de objeto | DOCUMENTAL; requiere vínculo verificable con la identidad de instancia |
| snapshot_id | Columna en SNAPSHOT y en NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP | REPRESENTADO |
| snapshot_object_record_id | En tablas dependientes fija la revisión exacta; en la fila SNAPSHOT el identificador de esa revisión es `object_record_id` | REPRESENTADO por DEC-C10-065/Opción A; requiere comparar el par exacto |
| stage_key | No hay columna canónica stage_key en el esquema descrito. SNAPSHOT.phase contiene baseline/post-B/rollback/route-test y no es sinónimo automático de stage_key | NO MAPEADO; UNKNOWN para comparación de consumidores |
| route_id | Existe en ROUTE y PREDICATE; ROUTE_STEP usa route_record_id; NODE/EDGE no tienen una columna route_id directa común | PARCIAL; la pertenencia derivada exige una regla exhaustiva de recorrido y no puede inferirse de texto libre `routes_affected` |
| object_class (CMP/PAR/REF/RUL/MET) | Clase de origen declarada en el universo; no es columna común de las tablas U_G | Requiere crosswalk explícito a ug_record_type/semantic_role y propiedades; no equivalencia nominal |
| dimension | Columna `dimension` en COVERAGE_REGISTER; no es parte de la tupla C0 ni campo común de consumidores | REPRESENTADO como atributo del scope; elegibilidad de consumidores se fija en universe_definition/version |
| universe_definition/version | Campo de COVERAGE_REGISTER | REPRESENTADO como declaración, pero su gramática, identidad y hash/version canónico no están cerrados |

### 20.1. Consecuencias para el control C0

1. No se equipara `SNAPSHOT.phase` con `stage_key`; hacerlo requeriría una decisión semántica expresa y un mapping total.
2. No se usa `SNAPSHOT.scope` como sustituto: su codificación y compatibilidad siguen OPEN y no están aceptadas.
3. No se deriva `object_class` de semantic_role, predicate_type, relation_type o boundary_class por coincidencia de nombres o intuición. Se necesita un crosswalk explícito por tipo de registro.
4. No se considera que `routes_affected` pruebe pertenencia exacta a una ruta. Para NODE/EDGE, la pertenencia route-specific solo podría derivarse de ROUTE_STEP y sus FKs exactas, si se demuestra que la enumeración del grafo/ruta está cerrada.
5. La información declarada en `universe_definition/version` solo es comprobable si su formato permite recuperar valores inequívocos y versionados. Una cadena libre o hash sin contenido recuperable no basta para verificar la tupla.
6. En consecuencia, el control C0 no puede emitir PASS completo mientras stage_key, object_class y las relaciones route-specific aplicables permanezcan sin mapping. Debe devolver UNKNOWN para esos componentes; cualquier contradicción demostrada en los campos ya representados sigue siendo FAIL.

### 20.2. Trabajo pendiente, sin autorización de cambio físico

- Definir un crosswalk semántico stage_key↔fase/etapa de captura sin colapsar tiempos o roles.
- Definir el crosswalk CMP/PAR/REF/RUL/MET a registros U_G, preservando cardinalidad y tipo; no asumir que las cinco clases equivalen uno-a-uno a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT.
- Definir cómo se demuestra route_id para objetos sin columna directa, y cuándo el scope es global a etapa frente a route-specific.
- Fijar gramática/versionado de universe_definition/version y su regla de hash/provenance.
- Reconciliar todo lo anterior con DDL completo y DEC-C10-065 antes de proponer cualquier extensión de schema.

**Estado:** DOCUMENTALMENTE IDENTIFICADO; MAPPING FÍSICO/SEMÁNTICO OPEN. No se acepta SNAPSHOT.scope, no se equipara phase con stage, no se añaden columnas, no se ejecuta control ni se autoriza implementación.



**Aclaración de conformidad con DEC-C10-070:** la tupla aceptada tiene nueve componentes (contract_id/version, instance_id/version, snapshot_id, snapshot_object_record_id, stage_key, route_id, object_class). `dimension` no se añade como décimo componente de identidad: es atributo del propio `coverage_scope_id` en COVERAGE_REGISTER y se versiona junto con la regla de universo. El control comprueba su consistencia y elegibilidad, pero no altera la tupla aceptada.

### 20.3. Separación de ejes: clase C10, tipo de registro U_G y rol semántico

La inspección histórica de `C10_S_IAM_FIELD_TO_COLUMN_CROSSWALK_PROPOSAL_DRAFT_001.md`, su auditoría FP/EDGE y U_G §§12.7, 15.1–15.4 confirma que no existe una equivalencia uno-a-uno entre `object_class` C10 y una tabla U_G. Deben mantenerse tres ejes:

1. **`source_object_class` C10:** familia constitutiva que se cubre: CMP, PAR, REF, RUL o MET.
2. **`ug_record_type`:** tipo físico/relacional del registro U_G: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT u otro registro probatorio aplicable.
3. **`semantic_role` / `boundary_class`:** clasificación semántica y de frontera de NODE, conforme a DEC-C10-059/060. No codifican la clase C10.

La tupla C0 conserva el campo `object_class` como clase de origen, pero el universo versionado debe definir explícitamente el crosswalk `source_object_class → {ug_record_type, semantic_role, target field/property, inclusion rule}`. El crosswalk puede ser 1:N o N:M y debe conservar el identificador exacto del objeto/campo de origen y el `object_record_id` U_G de destino cuando exista. No se deduce la clase desde NODE/EDGE/PREDICATE por nombre, ni se deduce la tabla desde CMP/PAR/REF/RUL/MET.

### 20.4. Crosswalk temporal: stage_key C10-S, DGP time y SNAPSHOT.phase

La reconstrucción de la plantilla U_G §18.2 recupera siete `stage_key` de captura C10-S ya propuestos:

| stage_key C10-S | Artefacto esperado | Familia de comparación |
|---|---|---|
| `C_SRC` | Snapshot de origen | CMP/PAR/REF/RUL/MET declarados |
| `F1_S2` | Snapshot S2 producido por F1 | Preservación y mapping de CMP/PAR/REF |
| `A1_S1` | Snapshot S1 producido por A1 | Preservación independiente bajo ruta A |
| `F2_DST_DECL` | Destino declarado para F2 | Configuración antes de aplicar |
| `A2_DST_DECL` | Destino declarado para A2 | Configuración antes de aplicar |
| `F2_DST_APPLIED` | Destino observado tras F2 | Estado efectivamente aplicado |
| `A2_DST_APPLIED` | Destino observado tras A2 | Estado efectivamente aplicado |

DEC-C10-071 acepta estos siete valores como vocabulario controlado de stage_key. La aceptación se limita al enum y sus significados; no acepta serialización SNAPSHOT.scope ni crea snapshots. El mapping de cada etapa a snapshots concretos y a rutas/objetos permanece sujeto a los gates siguientes.

Hay tres ejes temporales diferentes:

| Eje | Semántica | Representación | Regla |
|---|---|---|---|
| `stage_key` C10-S | Etapa del proceso de migración/configuración | Nueve-component C0 tuple, declarado en `universe_definition/version` | Usar los siete valores candidatos de §18.2; no codificarlo en SNAPSHOT.phase |
| Reloj DGP | Momento causal/analítico t−1…t9 | Contrato temporal DGP | Mapear una etapa C10-S a uno o varios momentos DGP solo mediante regla explícita; no son el mismo enum |
| `SNAPSHOT.phase` | Contexto/tipo de captura | Columna `SNAPSHOT.phase`: baseline/post-B/rollback/route-test | Conservar dominio propio; no convertirlo en stage_key |
| Tiempo de captura | Instante efectivo | `SNAPSHOT.timestamp` con zona | Auxiliar; no identifica por sí solo la etapa |

**Reconciliación de propuestas:** U_G §18.2 proponía serializar stage/ruta en el campo textual `SNAPSHOT.scope`. Esa codificación sigue expresamente NO ACEPTADA por DEC-C10-070. La tupla C0 aceptada se declara en `COVERAGE_REGISTER.universe_definition/version`; no se debe copiar ni parsear heurísticamente desde SNAPSHOT.scope. El campo SNAPSHOT.scope no se usa como sustituto.

Regla propuesta: cada coverage_scope_id fija un solo stage_key candidato y una revisión exacta de SNAPSHOT en universe_definition/version. El registro U_G queda vinculado mediante `snapshot_id + snapshot_object_record_id`. Múltiples etapas requieren scopes distintos, salvo decisión expresa posterior que defina universo multi-etapa y denominador.

### 20.5. Crosswalk de ruta: familia F/A frente a route_id exacto

Opción A + DEC-C10-065 fija pertenencia y referencias exactas:

- ROUTE tiene `route_id` semántico y `object_record_id` versionado, fijados al snapshot exacto.
- PREDICATE referencia la revisión exacta de ROUTE mediante `route_record_id` y el pinning del snapshot.
- ROUTE_STEP es la fuente canónica del orden y referencia ROUTE/NODE/EDGE mediante record IDs exactos dentro del mismo snapshot.
- NODE y EDGE no tienen columna universal `route_id`; su pertenencia route-specific se demuestra por inclusión exacta en ROUTE_STEP de la revisión concreta de ROUTE.
- `routes_affected` y texto libre no son evidencia de pertenencia.

U_G §18.2 proponía los valores de ruta `NONE/F/A`. Estos son marcadores de familia/alcance, no necesariamente identidades ROUTE.route_id. C0 exige `route_id` exacto. Por ello:

1. Para un scope route-specific, la tupla C0 debe contener el route_id semántico exacto, y el universo debe fijar la revisión route_record_id aplicable dentro del snapshot. NODE/EDGE deben aparecer en ROUTE_STEP de esa revisión; PREDICATE debe resolver su route_record_id a ella; ROUTE debe ser el registro fijado.
2. `F` y `A` pueden conservarse como `route_family`/branch label auxiliar en universe_definition, nunca sustituir route_id.
3. Para C_SRC u otro scope realmente global, se requiere un token reservado explícito y versionado para “sin restricción de ruta”; no puede ser NULL, vacío ni el texto ambiguo NONE sin definición formal. El literal sigue OPEN.
4. Si aún no existe route_id exacto o no puede reconstruirse exhaustivamente la pertenencia desde ROUTE_STEP, resultado UNKNOWN. Una referencia exacta contradictoria produce FAIL.
5. Un objeto presente en varias rutas genera varias pertenencias/scope mappings explícitos; no se duplican objetos ni se fusionan denominadores.

### 20.6. Crosswalk de object_class C10 y dimensión

DEC-C10-070 acepta `object_class ∈ {CMP, PAR, REF, RUL, MET}`. El valor genérico `CONFIG` que aparece en el formato ilustrativo de U_G §18.2 no satisface la granularidad de la tupla C0 y no se adopta para este binding. Se separan:

- `object_class`: familia de origen C10, uno de CMP/PAR/REF/RUL/MET.
- `dimension`: valor propio de COVERAGE_REGISTER, por ejemplo las dimensiones C10S_CONFIG_CMP/PAR/REF/RUL/MET ya enumeradas en §18.6.
- `ug_record_type`: tabla/tipo U_G que materializa o referencia el objeto.
- `semantic_role`/`boundary_class`: clasificación NODE conforme a DEC-C10-059/060.

| object_class | Registros U_G candidatos | Regla/cautela |
|---|---|---|
| CMP | NODE; EDGE solo para relaciones entre componentes | CMP material se representa como NODE con semantic_role apropiado; EDGE no representa el componente |
| PAR | NODE cuando la propiedad/clave requiere identidad propia; o propiedad atómica tipada del owner | Fijar owner, property_key, tipo, dominio, estado y granularidad; no crear NODE por cada valor |
| REF | EDGE y referencias tipadas | Usar catálogo de relaciones aceptado; la referencia declarada no prueba disponibilidad/instalación |
| RUL | PREDICATE para regla evaluable; referencias a operandos/owner | Preservar rule_id, AST, operandos, scope y efecto; AST válido (FP-01) no implica preservación semántica (FP-03) |
| MET | Metadatos tipados transversales; SNAPSHOT para captura; EVIDENCE_REGISTER para procedencia/custodia | No existe una tabla MET única; clasificar cada metadata field por owner, tiempo, ámbito y función |

El crosswalk es explícito y puede ser 1:N/N:M. Debe registrar origen/clave exacta, owner, ug_record_type, destino/propiedad, cardinalidad, regla de inclusión y evidencia. No se deduce por similitud de nombres ni se fuerza equivalencia entre object_class y semantic_role.

### 20.7. Dimensión de cobertura y regla de inclusión

`COVERAGE_REGISTER.dimension` es atributo del scope y queda fuera de la tupla C0 de nueve componentes. `coverage_scope_id` es el vínculo común de los registros U_G. El universo versionado debe definir qué registros/propiedades son elegibles para ese scope.

Cada `universe_definition/version` deberá especificar: (a) dimensión y vocabulario; (b) unidad de denominador; (c) object_class aplicable (CMP/PAR/REF/RUL/MET); (d) ug_record_type admisible; (e) regla de inclusión/exclusión por objeto/propiedad; (f) owner y cardinalidad esperada; (g) stage_key C10-S, route_id exacto o token global reservado y snapshot exacto; (h) mapping auxiliar route_family F/A cuando aplique; (i) correspondencia declarada con el reloj DGP cuando proceda; (j) fuentes para reconstruir la enumeración. Un registro puede pertenecer a scopes distintos solo si cada dimensión/etapa/ruta/clase y regla de inclusión están declaradas; no se fusionan denominadores.

**Dictamen de esta operación:** se reutilizan los contratos y crosswalk históricos. Se propone mantener `stage_key` en el universo versionado, preservar `SNAPSHOT.phase` como eje separado, resolver rutas mediante ROUTE/ROUTE_STEP exactos, y mantener `source_object_class` separado de `ug_record_type` y `semantic_role`. No se selecciona aún el token global de ruta, ni la gramática serializada completa de `universe_definition/version`, ni se autoriza cambio de schema, implementación o ejecución.



## 20.8. Semántica de scope global y route-specific — propuesta para DEC-C10-072

**Estado:** propuesta documental para revisión; no aceptada ni congelada. Reutiliza DEC-C10-064/065/070/071 y §§20.3–20.7. No modifica el schema U_G ni crea scopes.

### 20.8.1. Qué identifica route_id

Para un scope route-specific, `route_id` identifica la identidad semántica estable de una ruta dentro del contrato/instancia. No identifica por sí solo una revisión observada: el universo debe fijar además el `route_record_id` exacto y el par `snapshot_id + snapshot_object_record_id` al que pertenece, conforme a DEC-C10-065. Dos revisiones del mismo `route_id` no se consideran intercambiables por nombre ni por orden temporal.

La tupla C0 mantiene el `route_id` semántico; la revisión exacta se resuelve dentro de `universe_definition/version` y se verifica contra ROUTE/ROUTE_STEP/PREDICATE. `route_family=F/A` es metadato auxiliar y no identidad.

### 20.8.2. Alternativas para scope no restringido a una ruta

| Alternativa | Representación del slot route_id C0 | Ventaja | Riesgo/limitación |
|---|---|---|---|
| G1 — token reservado | Literal reservado versionado, candidato `C10S_SCOPE_GLOBAL` | Mantiene la tupla C0 de nueve componentes y evita NULL/vacío | Requiere reservar namespace, gramática y prohibir colisión con route_id real |
| G2 — NULL/vacío | Sin valor | Simple en serialización | Ambiguo: confunde global, dato ausente y no aplicable; no satisface identidad inequívoca C0 |
| G3 — nuevo campo scope_kind | GLOBAL/ROUTE más route_id nullable | Expresa explícitamente el tipo de scope | Cambia la tupla/estructura aceptada o exige nueva decisión de schema; no procede bajo DEC-C10-070 sin reabrirlo |

**Recomendación provisional: G1.** El candidato `C10S_SCOPE_GLOBAL` significa exclusivamente “el universo de esta etapa/clase no está restringido a una ruta concreta”. No significa que no existan rutas, que el objeto no pertenezca a ninguna ruta, ni que la clase sea NA. El literal queda reservado y no podrá asignarse como route_id semántico real. No se usa `NONE`, NULL ni cadena vacía.

### 20.8.3. Reglas de pertenencia por clase

El scope route-specific requiere crosswalk por objeto y revisión, no solo una etiqueta en el registro:

| source_object_class | Evidencia mínima de pertenencia route-specific | Regla de no inferencia |
|---|---|---|
| CMP | CMP→NODE/propiedad del owner, identidad exacta y NODE incluido en ROUTE_STEP de la revisión ROUTE fijada; si el CMP es raíz/unidad, debe existir una regla explícita de inclusión | Ser owner o nodo raíz no implica automáticamente pertenencia a todos los recorridos |
| PAR | parameter_key y owner CMP exactos; hereda pertenencia solo si la regla versionada declara que las propiedades del owner siguen su NODE en ROUTE_STEP | No convertir cada PAR en NODE ni inferir ruta por nombre de parámetro |
| REF | REF→EDGE exacto; EDGE aparece como paso en ROUTE_STEP de la revisión ROUTE, con extremos y snapshot exactos | La mera existencia de una relación/EDGE no prueba que una ruta la recorra |
| RUL | rule_id/versión y scope/AST tipado; scope GLOBAL usa scope global; scope de componente/ruta requiere resolver operandos/owner y vínculo exacto con la ruta | La validez del AST o el uso de un operando no prueba por sí solo pertenencia a una ruta |
| MET | Campo MET con owner/target y función versionados; route-specific solo si apunta explícitamente a la revisión ROUTE o a un objeto cuya pertenencia se ha probado | Metadatos de instancia/contrato son globales; timestamp/hash no asignan ruta por sí solos |

El crosswalk puede ser 1:N o N:M. Si un objeto pertenece a varias rutas, cada pertenencia route-specific se declara en su scope correspondiente; los denominadores no se suman ni se deduplican entre scopes distintos.

### 20.8.4. Semántica del scope global

Con el token global, el universo enumera todos los objetos elegibles de la clase para la etapa y snapshot indicados, con independencia de su pertenencia a rutas concretas. Cada objeto se cuenta una vez por identidad/versionado dentro de ese scope global. La pertenencia múltiple a rutas no multiplica el denominador global.

Un scope global no es un “scope de objetos sin ruta”. No se puede derivar de que ROUTE/ROUTE_STEP esté vacío, ni sustituye el inventario de rutas. Si la pregunta científica exige comparar una ruta concreta, debe usarse un scope route-specific adicional.

### 20.8.5. Adjudicación 1/0/? de pertenencia

- **1:** route_id semántico y route_record_id exactos resueltos; snapshot exacto fijado; crosswalk de clase/objeto completo; relación de pertenencia demostrada por ROUTE_STEP o por la regla específica de clase de §20.8.3.
- **0:** el universo y el mapping del objeto están completos, la revisión ROUTE y todos sus ROUTE_STEP están exhaustivamente cubiertos, y la regla de pertenencia aplicable demuestra que el objeto no pertenece a esa ruta. Este 0 solo significa “no miembro de esta ruta”; no significa que el objeto esté ausente del snapshot ni que no exista otra ruta.
- **?:** ruta/revisión, mapping de clase, owner, ROUTE_STEP, snapshot o cobertura incompletos/conflictivos; también cuando la clase no tiene una regla de pertenencia resoluble.
- **NA:** solo si la relación de pertenencia no pertenece al dominio de la clase por declaración IAM ex ante; no usar NA para ocultar falta de mapping.

Para un scope global no se adjudica pertenencia a una ruta concreta. Se adjudica inclusión en el universo global por regla de clase y cobertura; los estados de ruta individuales se mantienen separados.

### 20.8.6. Consecuencia para C0 y gate siguiente

El control C0 debe validar que el slot route_id contiene o bien una identidad de ruta real con revisión exacta resuelta, o bien el token global reservado una vez que su literal/gramática hayan sido aceptados. Un valor vacío, NULL, `NONE`, `F` o `A` produce UNKNOWN si no hay contradicción demostrada; una referencia incompatible o colisionada produce FAIL.

La propuesta G1 no queda aprobada por su inclusión en este protocolo. Requiere aceptación explícita del token, namespace y semántica. La gramática completa/versionado de `universe_definition`, el crosswalk físico por propiedad y el control C0 ejecutable permanecen OPEN/CONDITIONAL. No se modifica schema, no se crean snapshots/scopes y no se autoriza implementación ni ejecución científica.


## 20.9. DEC-C10-072 — estado normativo del token global

DEC-C10-072 acepta G1 y reserva el literal exacto `C10S_SCOPE_GLOBAL` para el slot `route_id` de C0. Su significado normativo es “sin restricción a una ruta concreta”. No significa ausencia de rutas, no pertenencia de un objeto ni NA. El literal no puede ser un route_id real; colisión = FAIL. NULL, vacío, NONE, F y A no son sustitutos válidos.

En scope global se enumera el universo elegible de la clase/etapa/snapshot y cada identidad se cuenta una vez, aunque aparezca en varias rutas. Los denominadores route-specific permanecen separados. Para route-specific se mantienen route_id semántico, route_record_id y snapshot exactos.

Esta aceptación no cierra la gramática/versionado completo de universe_definition, el mapping físico ni el control C0 implementado/auditado. Estos gates permanecen OPEN/CONDITIONAL. No schema change, fixtures ni ejecución autorizados.



## 20.10. Gramática versionada de universe_definition — propuesta UDG-01

**Estado:** propuesta documental, no aceptada como contrato final. DEC-C10-070/071/072 prevalecen sobre cualquier redacción histórica anterior de este protocolo.

### 20.10.1. Separación entre identidad C0 y contenido de la definición

La tupla C0 conserva exactamente nueve componentes: `contract_id`, `contract_version`, `instance_id`, `instance_version`, `snapshot_id`, `snapshot_object_record_id`, `stage_key`, `route_id`, `object_class`. `dimension` permanece fuera de la tupla, como atributo independiente de COVERAGE_REGISTER.

`universe_definition/version` porta una definición estructurada y versionada del universo que justifica el denominador de ese scope. No reemplaza ningún componente C0, no es un registro de miembro y no es el resultado del control C0.

### 20.10.2. Envelope candidato

Se propone un objeto JSON UTF-8 con esta estructura lógica (campos ilustrativos normativos solo si la propuesta se acepta):

| Campo | Cardinalidad | Regla propuesta |
|---|---:|---|
| `schema_id` | 1 | Literal `TGCV-C10S-UNIVERSE` |
| `schema_version` | 1 | Versión semántica de la gramática, separada de la versión de instancia/contrato |
| `universe_id` | 1 | Identidad estable del universo definido |
| `universe_revision` | 1 | Entero positivo, inmutable por revisión |
| `scope` | 1 | Los nueve componentes C0, sin campos adicionales en su identidad |
| `membership_mode` | 1 | `EXPLICIT` o `RULE_DEFINED` |
| `member_refs` | 0..N | Referencias tipadas y versionadas, ordenadas canónicamente; obligatorias si EXPLICIT |
| `inclusion_rule_ref` | 0..1 | Referencia exacta a regla/version; obligatoria si RULE_DEFINED |
| `exclusion_rule_refs` | 0..N | Reglas exactas de exclusión, si existen; no pueden contradecir inclusión sin resolución explícita |
| `source_manifest_refs` | 1..N | Fuentes/manifiestos que permiten reconstruir el universo y su cobertura |
| `declared_member_count` | 1 | Entero no negativo; igual a la cardinalidad deduplicada del universo declarado |
| `provenance_ref` | 1 | Identidad/versionado de la procedencia de la definición |

La referencia `scope` replica los nueve componentes aceptados para permitir inspección autocontenida, pero el consumidor debe comprobar igualdad exacta con los campos C0 externos; no crea una segunda identidad independiente.

### 20.10.3. Reglas de route binding

- Si `scope.route_id = C10S_SCOPE_GLOBAL`, no se declara `route_record_id` como ruta focal. El universo es independiente de una ruta concreta.
- En scope route-specific, `route_id` es la identidad semántica y el manifiesto debe resolver un único `route_record_id` exacto para el snapshot fijado.
- El token global no puede colisionar con un route_id real. La colisión es FAIL.
- No se admiten NULL, cadena vacía, NONE, F ni A como sustitutos.

### 20.10.4. Member reference tipado

Cada `member_ref` candidato contiene `object_class`, `object_id`, `object_record_id` y, cuando aplique, `owner_ref` y `source_record_ref`. La clase del miembro debe coincidir con `scope.object_class`. Las referencias deben resolver a registros de la misma instancia y snapshot/etapa, salvo que una regla de mapping aceptada defina explícitamente una proyección entre etapas. No se permite resolver identidad solo por nombre, valor, hash o posición de array.

Para `membership_mode=EXPLICIT`, member_refs es la enumeración del denominador; duplicados exactos son FAIL, referencias no resolubles UNKNOWN y contradicciones de identidad FAIL. Para `RULE_DEFINED`, inclusion_rule_ref y todas sus dependencias deben estar versionadas y el resultado debe ser reproducible; mientras no exista evaluación autorizada, la completitud queda UNKNOWN.

### 20.10.5. Canonicalización y hash — propuesta

Se propone canonicalización JSON determinista: UTF-8, Unicode NFC, claves de objeto ordenadas lexicográficamente, sin whitespace no semántico, arrays de referencias ordenados por (object_class, object_id, object_record_id), números enteros en forma decimal canónica y prohibición de NaN/Infinity. El hash candidato es SHA-256 sobre los bytes canonicalizados. El hash no sustituye identidad ni versión; se almacena como checksum de contenido y debe poder recalcularse.

No se ha fijado aún una dependencia normativa de implementación (por ejemplo, RFC/JCS), ni se acepta todavía esta política de canonicalización/hash.

### 20.10.6. Versionado, compatibilidad y mutabilidad

- `schema_version`: semver de la gramática; cambio incompatible de estructura/semántica requiere major; adición compatible minor; corrección editorial sin cambio semántico patch.
- `universe_revision`: entero monotónico por `universe_id`; una revisión publicada es inmutable. Cambio de miembros, reglas, fuentes, scope o denominador crea revisión nueva.
- `contract_version` e `instance_version` conservan su ciclo independiente aceptado por DEC-C10-069.
- El hash identifica contenido exacto, no equivalencia semántica.
- No se infiere compatibilidad entre versiones; requiere regla explícita y comprobación del mismo scope C0.

### 20.10.7. Invariantes y adjudicación

1. La tupla interna scope debe ser idéntica a la tupla C0 externa.
2. Todas las referencias deben resolver dentro del contrato/instancia y snapshot fijados, o contar con una proyección de etapa explícita.
3. `declared_member_count` debe igualar el conjunto deduplicado de miembros; nunca se corrige automáticamente.
4. EXPLICIT exige lista completa; RULE_DEFINED exige regla y dependencias cerradas.
5. La cobertura de fuentes debe justificar exhaustividad; la lista vacía no prueba universo vacío por sí sola.
6. La versión/hash deben corresponder al contenido recuperado; discrepancia demostrada = FAIL.
7. Dato requerido ausente/no resoluble = UNKNOWN; contradicción demostrada = FAIL; PASS requiere todos los invariantes aplicables y exhaustividad demostrada.
8. Un universo de cardinalidad cero solo puede declararse con fuente y regla de enumeración exhaustivas que demuestren cero miembros.

### 20.10.8. Alternativas de representación

| Alternativa | Descripción | Evaluación provisional |
|---|---|---|
| U1 | Envelope JSON autocontenido dentro de universe_definition, versión/hash registrados por separado | Recomendada; portable y auditable |
| U2 | Cadena compacta con delimitadores | Rechazada provisionalmente: escaping, cardinalidad y tipos ambiguos |
| U3 | Referencia externa a manifiesto versionado | Útil como optimización, pero necesita resolver inmutabilidad/disponibilidad; no basta sola |

Se recomienda U1 con referencias externas permitidas solo como soporte, no como sustituto del envelope autocontenido y su hash. No queda aceptada.

### 20.10.9. Límites del gate

La propuesta no cierra mappings físicos CMP/PAR/REF/RUL/MET, reglas de pertenencia por clase, el control independiente C0, ni la compatibilidad del campo físico U_G. No crea fixtures, parser, validator, snapshots o scopes. No modifica schema, no constituye Design Freeze y no autoriza implementación ni ejecución científica.


## 20.11. DEC-C10-073 — estado vigente de UDG-01

DEC-C10-073 acepta U1 como arquitectura documental: envelope JSON autocontenido y versionado, con los campos/cardinalidades de §20.10. La tupla scope replica exactamente C0 (nueve componentes); dimension sigue fuera. Se aceptan los invariantes de EXPLICIT/RULE_DEFINED, tipado/resolución de referencias, cardinalidad, prueba exhaustiva para universo vacío, route binding y adjudicación PASS/FAIL/UNKNOWN allí definidos.

**No aceptado por DEC-C10-073:** canonicalización UTF-8/NFC/orden determinista como requisito normativo, SHA-256 obligatorio, RFC/JCS, serialización física ejecutable, reglas completas de compatibilidad/incremento semver, mapping físico por clase ni control C0 implementado/auditado. SHA-256 y canonicalización permanecen opciones de diseño abiertas. La aceptación es documental/arquitectónica, no autorización de schema change, parser, validator, fixtures, Design Freeze o ejecución.

Ante conflicto de estatus, este asiento y DEC-C10-073 prevalecen sobre frases históricas de §20.10 que calificaban toda UDG-01 como no aceptada.


## 20.12. Canonicalización e integridad del envelope — propuesta UDG-02

**Estado:** propuesta técnica/documental; no aceptada. Aplica a la arquitectura U1 aceptada por DEC-C10-073 sin modificar sus campos/cardinalidades.

### 20.12.1. Separaciones obligatorias

Se distinguen tres capas:

1. **Bytes de artefacto:** representación física recibida (p. ej. JSON pretty-printed); su hash cambia si cambian whitespace, codificación o finales de línea.
2. **Bytes JSON canónicos:** serialización determinista del envelope validado bajo un perfil de canonicalización identificado; aptos para checksum reproducible.
3. **Equivalencia semántica:** juicio separado que exige comparar identidad, scope, miembros, reglas, fuentes y versión bajo reglas explícitas. Ni igualdad de bytes ni igualdad de hash prueba por sí sola equivalencia semántica, exhaustividad del universo o verdad de las fuentes.

### 20.12.2. Alternativas

| Perfil | Descripción | Evaluación |
|---|---|---|
| C1 — JCS estricto + prevalidación TGCV | RFC 8785 para serialización JSON, con restricciones del schema TGCV antes de canonicalizar | Recomendada provisionalmente; reduce reglas criptográficas ad hoc |
| C2 — Canonicalizador TGCV propio | UTF-8/NFC, claves ordenadas y serialización numérica propia | No recomendado: duplica reglas complejas y puede divergir entre lenguajes |
| C3 — Hash de bytes fuente solamente | SHA-256 del fichero tal como se recibió | Insuficiente para igualdad representacional ante whitespace/orden; útil solo como hash de artefacto fuente |

RFC 8785 (JCS) define serialización determinista sobre I-JSON, ordena recursivamente propiedades de objetos, conserva el orden de arrays y exige que las cadenas Unicode se preserven sin normalización durante canonicalización. Por ello C1 **no** normaliza cadenas a NFC: la prevalidación TGCV rechaza identificadores/cadenas declaradas NFC-required que no estén ya en NFC; nunca las reescribe silenciosamente. JCS es RFC Informational, no Internet Standards Track; la decisión de adoptarlo debe reconocer esa condición.

### 20.12.3. Perfil C1 candidato

A. **Entrada:** UTF-8 válido; JSON parseable; objetos sin nombres de propiedad duplicados; Unicode válido sin lone surrogates; solo tipos JSON admitidos. Rechazar NaN/Infinity y cualquier dato no I-JSON.

B. **Strings:** no alterar durante canonicalización. Para campos identificadores declarados NFC-required, comprobar NFC antes; si no cumple, FAIL de conformidad de entrada, sin autocorrección. Los identificadores son case-sensitive; no recortar whitespace ni aplicar case-folding. Un identificador con whitespace periférico incumple el patrón de su campo y se rechaza, no se transforma.

C. **Properties:** usar exactamente ordenamiento recursivo JCS por unidades UTF-16; no sustituir por orden UTF-8, locale ni orden de inserción.

D. **Arrays:** JCS conserva el orden de arrays. Antes de JCS, los campos cuyo schema declare semántica de conjunto se ordenan por clave de identidad estable: `member_refs` por (object_class, object_id, object_record_id); `exclusion_rule_refs` y `source_manifest_refs` por referencia tipada/versionada. Arrays de secuencia/orden de ejecución mantienen orden declarado. No se ordena ningún array sin clasificación explícita en schema.

E. **Numbers:** para UDG-01 los campos numéricos del envelope son enteros no negativos en rango seguro interoperable (0…2^53−1), en particular declared_member_count y universe_revision; no se admiten floats, -0, NaN o Infinity. Boolean no se acepta como entero. Cualquier entero futuro fuera de rango se representa mediante string tipado definido por schema, no como JSON number.

F. **Null/omisión:** no usar null para representar desconocido, global, vacío ni no aplicable. Campo opcional ausente = no declarado; campo obligatorio ausente = FAIL estructural. Arrays opcionales ausentes se distinguen de arrays presentes vacíos. member_refs es obligatorio en EXPLICIT; [] solo es válido con declared_member_count=0 y evidencia exhaustiva que pruebe universo vacío. En RULE_DEFINED member_refs se omite y inclusion_rule_ref es obligatorio. No aceptar null en ningún campo UDG-01.

G. **Hash:** calcular SHA-256 sobre bytes UTF-8 canónicos del envelope completo, sin incluir el propio hash ni metadatos de integridad externos (evita autorreferencia). Registrar fuera del envelope `canonicalization_profile_id`, `hash_algorithm`, `canonical_content_hash` y, opcionalmente, `source_artifact_hash` calculado sobre bytes originales. No confundir ambos hashes.

H. **Versionado del perfil:** identificar el perfil como candidato `TGCV-C10S-JCS-1`; cualquier cambio en prevalidación, clasificación/orden de arrays, reglas numéricas o tratamiento de campos requiere nueva versión del perfil y evaluación de compatibilidad. No sobrescribir hashes previos.

### 20.12.4. Interpretación de hash y comparaciones

- Mismo perfil + mismo canonical_content_hash: evidencia de igualdad de bytes canónicos, sujeta a la seguridad criptográfica del algoritmo; no prueba verdad, completitud, validez causal ni equivalencia semántica general.
- Distinto source_artifact_hash y mismo canonical_content_hash: representaciones físicas distintas del mismo contenido canónico bajo el perfil.
- Distinto canonical_content_hash: contenidos canónicos distintos; no permite concluir por sí solo que el universo sea semánticamente distinto, pues pueden variar provenance, revisión u otros metadatos.
- Distinto perfil o versión: hashes no comparables directamente; requiere recanonicalización de la fuente preservada bajo un perfil común compatible. Si la fuente no está disponible, UNKNOWN/NOT_COMPARABLE.
- Igualdad de universo requiere comparación semántica explícita; no se define fingerprint semántico en esta propuesta.

### 20.12.5. Fallos y adjudicación

JSON inválido, claves duplicadas, campo desconocido no permitido por schema, null prohibido, tipo/rango incorrecto, identificador NFC-required no conforme, array de conjunto con duplicados, o discrepancia entre hash declarado y recalculado = FAIL. Campo/referencia/fuente requerido no disponible o perfil incompatible sin fuente original = UNKNOWN/NOT_COMPARABLE, no PASS. PASS de integridad solo acredita conformidad estructural y hash reproducible; no adjudica exhaustividad ni pertenencia del universo, que se evalúan por separado conforme UDG-01.

### 20.12.6. Límites

UDG-02 no está aceptada. No modifica DEC-C10-073 ni convierte RFC 8785/SHA-256 en requisitos normativos. No define implementación, parser, validator, fixtures, hash de producción, schema físico, Design Freeze ni autorización de ejecución. La fuente primaria de JCS es RFC 8785: https://www.rfc-editor.org/rfc/rfc8785.html.


## 20.13. DEC-C10-074 — perfil JCS aceptado

DEC-C10-074 acepta C1 (RFC 8785 JCS + prevalidación TGCV) como política documental de canonicalización del envelope U1, bajo las reglas UDG-02 §20.12: entrada UTF-8/JSON/I-JSON válida sin claves duplicadas/lone surrogates/NaN/Infinity; validación NFC previa solo para campos identificadores marcados, sin reescritura; orden de propiedades JCS; orden previo por identidad solo para arrays declarados conjuntos y conservación del orden secuencial; enteros seguros no negativos; null prohibido y omisión distinta de array vacío; SHA-256 de bytes canónicos con hash/metadatos fuera del envelope; separación source_artifact_hash/canonical_content_hash; perfil TGCV-C10S-JCS-1.

La igualdad de canonical_content_hash bajo el mismo perfil acredita igualdad de bytes canónicos, no equivalencia semántica, exhaustividad ni verdad de fuentes. Perfiles distintos requieren recanonicalización desde fuente preservada o UNKNOWN/NOT_COMPARABLE. Esta aceptación no autoriza parser/validator, fixtures, hash de producción, schema change, Design Freeze, implementación ni ejecución científica; mapping físico y C0 independiente siguen abiertos. DEC-C10-074 prevalece sobre §20.12 que calificaba UDG-02 como no aceptada.


## 20.14. Comparación semántica de universos versionados — propuesta UDG-03

**Estado:** propuesta documental; NO ACEPTADA. Se apoya en U1/DEC-C10-073 y JCS/DEC-C10-074. No modifica el envelope, C0 ni el perfil de canonicalización.

### 20.14.1. Principio: no colapsar niveles de igualdad

La comparación produce un vector de resultados por dimensión; no un booleano único. Se distinguen:

1. **Artefacto idéntico:** mismos bytes fuente y mismo source_artifact_hash verificado.
2. **Representación canónica idéntica:** mismo perfil TGCV-C10S-JCS-1 y mismo canonical_content_hash recalculado.
3. **Identidad de universo:** mismo universe_id. La identidad no implica misma revisión ni mismo contenido.
4. **Misma revisión:** mismo universe_id + universe_revision, con artefacto y referencias recuperados y verificados. Si dos artefactos contradictorios reclaman la misma revisión, FAIL de integridad/inmutabilidad.
5. **Igualdad extensional de miembros:** mismo conjunto completo de member identities bajo scope y snapshot comparables, aunque difieran procedencia, representación o modo EXPLICIT/RULE_DEFINED.
6. **Equivalencia de definición:** mismas condiciones de inclusión/exclusión, reglas, dependencias, dominios y semántica de pertenencia; requiere demostrar equivalencia de las definiciones, no solo de los resultados observados.
7. **Compatibilidad de revisiones:** relación dirigida y explícita entre revisiones (p. ej. SAME_MEMBERS, STRICT_SUPERSET, STRICT_SUBSET, REDEFINED, INCOMPARABLE), nunca inferida solo de revision number.

### 20.14.2. Proyección semántica de comparación

La comparación debe construir dos proyecciones separadas:

- **Projection-ID (identidad/revisión):** universe_id, universe_revision, schema_id/version, contract_id/version, instance_id/version, scope C0, stage_key, route_id/route_record_id, snapshot exacto y perfil de canonicalización.
- **Projection-SEM (contenido que define el universo):** membership_mode; conjunto de member_refs normalizados por identidad tipada y sus object_record_id/version; inclusión/exclusión; inclusion_rule_ref y versión/AST/dependencias cuando RULE_DEFINED; manifiestos/fuentes y límites de cobertura; declared_member_count; semántica de proyección entre etapas, si existe.

Provenance, timestamp de captura, source_artifact_hash y canonical_content_hash son evidencia de procedencia/integridad, no miembros del conjunto. Se conservan y auditan, pero su cambio aislado no implica cambio semántico. En cambio, un cambio de snapshot, C0, route_record_id, instancia, versión de objeto o regla puede alterar el universo o impedir compararlo; no se elimina de la comparación como “metadato”.

### 20.14.3. Requisitos previos de comparabilidad

Antes de emitir igualdad/diferencia semántica, comprobar:

- identidad y revisión recuperables e inmutabilidad de cada versión;
- schema/perfil compatibles o recanonicalización reproducible desde las fuentes originales;
- igualdad exacta de la tupla C0 (incluidos scope global o route-specific exacto), stage_key, snapshot y route_record_id cuando aplique;
- misma frontera de contrato/instancia o una proyección/mapping explícito, versionado y validado entre ellas;
- referencias de miembro resueltas a registros inmutables, con clases y versiones exactas;
- exhaustividad demostrada de ambos universos y cobertura suficiente de fuentes/manifiestos;
- reglas, dependencias y AST recuperables si la definición es RULE_DEFINED.

Si difieren scope, etapa, snapshot, ruta o contrato/instancia sin mapping explícito, el resultado es NOT_COMPARABLE (no DIFFERENT). Si falta evidencia requerida, UNKNOWN. Una contradicción demostrada (p. ej. misma revisión con dos contenidos válidos incompatibles, count incorrecto, referencia que contradice la clase) es FAIL.

### 20.14.4. Reglas de igualdad/diferencia

- **Artefacto:** EQUAL solo si bytes fuente completos coinciden; distinto hash verificado = DIFFERENT a nivel artefacto.
- **Canónico:** EQUAL solo con mismo perfil y hash recalculado coincidente; hash diferente = DIFFERENT a nivel de representación canónica.
- **Identidad:** EQUAL si universe_id coincide; DIFFERENT si no coincide. Esto no responde igualdad de contenido.
- **Misma revisión:** EQUAL solo si mismo universe_id/revision y no hay conflicto de contenido; conflicto = FAIL.
- **Extensional:** comparar conjuntos completos de identidades tipadas exactas. EQUAL si conjuntos idénticos y scope/snapshot compatibles. DIFFERENT si ambos completos/comparables y existe al menos una pertenencia distinta. UNKNOWN si cualquiera no es exhaustivo o hay refs sin resolver. NOT_COMPARABLE si scopes/denominadores no coinciden ni existe proyección autorizada.
- **Definicional:** EQUAL requiere equivalencia probada de reglas/AST, dominios, dependencias y condiciones de aplicación. Coincidencia extensional en un snapshot no basta. DIFFERENT requiere contradicción demostrada de semántica/reglas; de otro modo UNKNOWN.
- **Compatibilidad:** clasificar relación dirigida entre revisiones solo después de comparación extensional y, cuando la pregunta lo requiera, definicional. No inferir “superset/subset” de cardinalidades solamente.

### 20.14.5. Resultados controlados

Cada dimensión usa uno de estos resultados:

- `EQUAL`: igualdad demostrada en esa dimensión bajo requisitos cumplidos.
- `DIFFERENT`: diferencia demostrada en esa dimensión con ambos lados comparables y evidencia completa.
- `UNKNOWN`: información/evidencia insuficiente o referencias no resolubles.
- `NOT_COMPARABLE`: objetos válidos pero distintos en scope/contrato/snapshot/perfil no armonizable; no equivale a diferencia.
- `FAIL`: violación de integridad/contrato (p. ej. hash incorrecto, misma revisión mutable, cardinalidad contradictoria); es estado de conformidad, no una clase de igualdad.

El informe registra además reason_code, evidencia utilizada, perfiles/versions, scope comparado y dimensión. No se permite elevar UNKNOWN/NOT_COMPARABLE a PASS ni resumir el vector como “equivalente” si alguna dimensión crítica está abierta.

### 20.14.6. Ejemplos límite

| Caso | Artefacto/canónico | Extensional | Definicional | Dictamen |
|---|---|---|---|---|
| Pretty-print distinto, JCS idéntico | Artefacto DIFFERENT; canónico EQUAL | Puede ser EQUAL | Puede ser EQUAL | No hay cambio de contenido canónico |
| Provenance/timestamp cambia, mismo scope y miembros exhaustivos | Canónico puede DIFFERENT | EQUAL | EQUAL si reglas idénticas | Nueva evidencia de procedencia, no nuevo universo semántico |
| Mismo universe_id, nueva revisión y miembro añadido | DIFFERENT | DIFFERENT | Depende de regla/cambio | Nueva revisión; relación superset solo si ambos exhaustivos |
| Mismo conjunto materializado, EXPLICIT frente a RULE_DEFINED | DIFFERENT | EQUAL | No demostrado por ello | Igualdad extensional, definición aún por comparar |
| Mismo nombre de miembro, distinto object_record_id/version | Puede variar | DIFFERENT o UNKNOWN si mapping no resuelve | UNKNOWN | No inferir identidad por nombre |
| Mismo hash, scope/snapshot distinto en metadatos externos | Hash solo no resuelve | NOT_COMPARABLE | NOT_COMPARABLE | Hash no anula C0 ni snapshot |
| Scope global frente a route-specific | Cualquier | NOT_COMPARABLE por defecto | NOT_COMPARABLE | No mezclar denominadores; proyección explícita requerida |
| Lista vacía sin evidencia exhaustiva | Puede ser canónica | UNKNOWN | UNKNOWN | No prueba universo vacío |

### 20.14.7. Límites

UDG-03 no está aceptada. No crea fingerprint semántico, algoritmo automático de equivalencia, regla de migración, parser/comparator, fixtures, schema change ni autorización de ejecución. No modifica las decisiones DEC-C10-073/074. La equivalencia semántica permanece un juicio sustentado por evidencia, no una propiedad del hash.


## 20.15. DEC-C10-075 — UDG-03 aceptada

DEC-C10-075 acepta UDG-03 como contrato documental de comparación semántica por dimensiones. Se mantienen siete niveles separados: (1) identidad del artefacto, (2) igualdad canónica bajo mismo perfil/hash recalculado, (3) identidad universe_id, (4) identidad de revisión inmutable, (5) igualdad extensional de miembros completos, (6) equivalencia definicional de inclusión/exclusión/reglas/AST/dominios/dependencias y (7) compatibilidad dirigida entre revisiones demostrada, no inferida por revision number/cardinality.

Projection-ID conserva identidad/revisión/schema/contract/instance/C0/stage_key/route/route_record/snapshot/perfil; Projection-SEM conserva modo membership, refs tipadas/versionadas, reglas y fuentes/cobertura. Provenance/timestamp/hash son trazabilidad, no miembros; C0/stage/route/snapshot/contract/instance/object version condicionan comparabilidad. Igualdad extensional requiere dos universos exhaustivos y scopes/snapshots compatibles. Equivalencia definicional requiere evidencia adicional de reglas/domínios/dependencias. EXPLICIT y RULE_DEFINED con mismos miembros en un snapshot no prueban equivalencia definicional.

Resultados: EQUAL, DIFFERENT, UNKNOWN, NOT_COMPARABLE; FAIL para incumplimiento de integridad. Scope/snapshot/contract incompatibles sin mapping explícito = NOT_COMPARABLE; evidencia faltante = UNKNOWN. Registrar dimensión, reason_code, evidencia, perfiles/versiones y scope. No elevar UNKNOWN/NOT_COMPARABLE a PASS ni emitir equivalencia global con dimensión crítica abierta.

Esta aceptación es documental: no crea fingerprint semántico, comparator ejecutable, migración, fixtures, parser/validator ni schema change; no autoriza Design Freeze, implementación o ejecución científica. DEC-C10-075 prevalece sobre §20.14, que describía UDG-03 como no aceptada.


## 20.16. Referencias tipadas, identidad de registro y resolución — propuesta UDG-04

**Estado:** propuesta documental; NO ACEPTADA. Se apoya en DEC-C10-073/074/075 y no modifica U1, JCS ni el contrato de comparación.

### 20.16.1. Identidad en dos niveles

Separar obligatoriamente:

- **Identidad lógica:** `(object_class, object_id)`; identifica el objeto conceptual dentro de su espacio de nombres/clase. No demuestra que exista una versión concreta ni que dos registros sean intercambiables.
- **Identidad de registro:** `(object_class, object_id, object_record_id)`; identifica una materialización/versionado inmutable concreto del objeto. Es la unidad mínima para resolver una referencia histórica reproducible.

El `object_record_id` no se reutiliza para contenido diferente. Si un registro declara además versión semántica, esta se verifica contra el registro recuperado; no sustituye el record_id. No resolver por nombre visible, valor, posición, hash aislado ni similitud textual.

### 20.16.2. Contrato abstracto de referencia

Toda referencia semánticamente relevante debe resolverse como una tupla tipada:

`(ref_role, target_object_class, target_object_id, target_object_record_id)`

- `ref_role` describe la relación desde el origen (p. ej. MEMBER, OWNER, SOURCE, INCLUSION_RULE, EXCLUSION_RULE, DEPENDENCY, PROVENANCE); no altera la identidad del target.
- `target_object_class` restringe el espacio de resolución y evita colisiones entre clases.
- `target_object_id` declara la identidad lógica esperada.
- `target_object_record_id` fija el registro exacto e inmutable.

El conjunto de roles es ilustrativo y requiere validación contra el catálogo REF vigente; no se declara enum cerrado en esta propuesta. Las referencias se clasifican además como REQUIRED/OPTIONAL por contrato del campo. La ausencia de una referencia opcional no es un dangling reference; la ausencia de una requerida es FAIL estructural.

### 20.16.3. Resolución y estados

La resolución se realiza contra un registro/manifiesto versionado y delimitado por el scope declarado; nunca contra “latest” implícito. Para una referencia se comprueba en orden: (1) sintaxis/forma; (2) existencia exacta del record_id; (3) clase e identidad lógica coincidentes; (4) integridad/inmutabilidad del registro; (5) compatibilidad de versión/schema/contract cuando aplique; (6) autorización/alcance de acceso a la fuente; (7) cardinalidad de resolución exactamente uno.

| Situación | Resultado |
|---|---|
| Referencia requerida ausente | FAIL |
| Record_id inexistente tras búsqueda exhaustiva en registry cerrado | FAIL / DANGLING_REFERENCE |
| Registry no disponible o cobertura no exhaustiva | UNKNOWN |
| Más de un registro candidato por clave lógica sin record_id exacto | UNKNOWN; NOT_COMPARABLE si se pretende comparar objetos no fijados |
| Clase u object_id contradicen el registro recuperado | FAIL / IDENTITY_CONFLICT |
| Registro correcto pero versión/schema/contract incompatible sin mapping aprobado | NOT_COMPARABLE |
| Fuente inaccesible o permiso insuficiente | UNKNOWN (no inferir inexistencia) |
| Referencia opcional ausente | NOT_APPLICABLE para esa relación, no FAIL |
| Mismo record_id asociado a contenidos distintos | FAIL / IMMUTABILITY_VIOLATION |

No colapsar NOT_FOUND con INACCESSIBLE ni NOT_FOUND con UNKNOWN. Solo puede afirmarse inexistencia si el registry relevante está cerrado, completo y consultado exhaustivamente.

### 20.16.4. Ciclos y dependencias

Construir grafo dirigido con aristas etiquetadas por ref_role. La detección de ciclos se aplica por tipo de relación:

- MEMBER/OWNER/SOURCE/INCLUSION_RULE/EXCLUSION_RULE no se presumen acíclicas ni cíclicas universalmente; su semántica debe declarar si transitividad o ciclos están permitidos.
- DEPENDENCY requiere política explícita por clase: DAG cuando la ejecución/orden topológico sea requisito; ciclos permitidos solo si el contrato define semántica de grupo/SCC y punto fijo. Sin esa definición, ciclo observado = UNKNOWN para interpretación semántica y FAIL solo si viola una regla acíclica ya declarada.
- PROVENANCE puede formar cadenas históricas; no confundir ciclos de procedencia con dependencia funcional.

Un ciclo no se “rompe” eliminando una arista ni se resuelve escogiendo un nodo arbitrario. Registrar los miembros del ciclo, roles y versiones exactas. La falta de visibilidad del grafo completo produce UNKNOWN sobre aciclicidad.

### 20.16.5. Cardinalidad y propagación

Cada relación declara cardinalidad min/max y si es REQUIRED/OPTIONAL en el contrato de su clase. No asumir cardinalidad universal 1:N por el tipo de referencia. Para una referencia singular, resolución válida exige exactamente un target. Para una colección, comprobar límites, duplicados por identidad de registro y completitud.

La resolución de una referencia no prueba la pertenencia semántica del target al universo: esa pertenencia se adjudica separadamente bajo UDG-01/03 y C0. Resolver un OWNER o SOURCE tampoco prueba que la configuración sea aplicable o que la transformación se haya ejecutado.

Propagación: FAIL de identidad/inmutabilidad invalida la relación afectada y cualquier conclusión que dependa de ella; UNKNOWN en una dependencia requerida propaga UNKNOWN a las conclusiones dependientes; NOT_COMPARABLE no se convierte en DIFFERENT. No propagar un fallo local a objetos no dependientes sin arista causal/dependencia demostrada.

### 20.16.6. Consecuencias para UDG-03

La igualdad extensional compara identidades de registro exactas en scopes/snapshots compatibles. Una misma identidad lógica con record_id distinto no equivale automáticamente al mismo miembro. Puede reconocerse continuidad lógica, pero la comparación de registros/versiones queda DIFFERENT o UNKNOWN según evidencia; para declarar equivalencia semántica se requiere mapping de versión explícito y aprobado. Nombres iguales no bastan.

### 20.16.7. Límites

UDG-04 no está aceptada. No fija schema físico REF, catálogo cerrado de roles, algoritmo de resolución, registro concreto, API, parser, validator, fixtures, comparador, Design Freeze ni ejecución. Tampoco resuelve aún mapping CMP/PAR/RUL entre F1/A1 y F2/A2. La propuesta debe reconciliarse con los contratos y decisiones previas antes de aceptar.


## 20.17. DEC-C10-076 — UDG-04 aceptada

DEC-C10-076 acepta UDG-04 documentalmente. Identidad lógica `(object_class, object_id)`; identidad exacta de registro `(object_class, object_id, object_record_id)`, inmutable. Referencia tipada `(ref_role, target_object_class, target_object_id, target_object_record_id)`. Roles de ejemplo MEMBER/OWNER/SOURCE/INCLUSION_RULE/EXCLUSION_RULE/DEPENDENCY/PROVENANCE deben reconciliarse con catálogo REF; no son enum físico cerrado. REQUIRED/OPTIONAL y cardinalidad se declaran por contrato de clase.

Resolver contra registry/manifiesto versionado y scope explícito; no latest implícito ni fallback por nombre/valor/posición/hash aislado. Comprobar forma, record_id, clase/id, inmutabilidad, compatibilidad, acceso y cardinalidad. Requerida ausente/dangling exhaustivo/conflicto/mutabilidad = FAIL; registry incompleto/inaccesible = UNKNOWN; incompatibilidad sin mapping = NOT_COMPARABLE; opcional ausente = NOT_APPLICABLE. Ciclos por relación; DAG solo cuando contrato DEPENDENCY lo exige. Propagar estados solo por dependencias demostradas.

Resolver ref no prueba membership, aplicabilidad, preservación o ejecución. La aceptación no cierra catálogo/schema/API/registry/resolver/parser/validator/comparator/fixtures ni mapping CMP/PAR/RUL; no autoriza Design Freeze ni ejecución. DEC-C10-076 prevalece sobre §20.16.

## 20.18.

## 20.18. Protocolo de control independiente del binding probatorio PAR — propuesta vinculada a DEC-C10-080

**Estado:** PROPUESTA DOCUMENTAL; pendiente de aceptación expresa.  
**Autoridad de binding:** DEC-C10-080.  
**Dependencias:** DEC-C10-070 (C0), DEC-C10-073 (U1), DEC-C10-076 (identidad/resolución tipada), DEC-C10-079 (identidad y supersession PAR), y §19 (COVERAGE_SCOPE_BINDING_CONTROL).  
**Propósito:** especificar la comprobación lógica de que una afirmación probatoria sobre una fila PAR está vinculada al scope exacto, a la revisión de manifiesto exacta y a evidencia identificable y pertinente, sin ampliar el esquema U_G.

### 20.18.1. Principio de no duplicación y separación de controles

El control PAR no reemplaza ni duplica C0. Reutiliza el control C0 de §19 para comprobar la identidad/binding del COVERAGE_SCOPE. El control PAR añade la resolución del localizador de fila PAR y la consistencia de la relación afirmación–evidencia.

Se emiten resultados separados para:
- **C0_SCOPE:** integridad de COVERAGE_SCOPE, su tupla C0 y consumidores.
- **PAR_ROW_BINDING:** resolución exacta de la fila PAR y correspondencia con el scope.
- **EVIDENCE_LINK_INTEGRITY:** integridad del CLAIM_EVIDENCE_LINK y resolución de EVIDENCE_REGISTER.
- **EVIDENCE_RELEVANCE:** suficiencia de la evidencia para el predicado/estado concreto.
- **COVERAGE_COMPLETENESS:** estado del universo cubierto, evaluado por §19.3 y U_G §18.6; nunca se infiere del mero vínculo.

Un resultado favorable en una capa no compensa ni sustituye una capa no evaluada. No se crea un PASS global si alguna capa obligatoria está UNKNOWN o NOT_COMPARABLE.

### 20.18.2. Entradas mínimas del control

El conjunto de entrada debe estar cerrado, identificado y versionado e incluir, cuando sean aplicables:

1. La versión exacta del contrato/instancia y del IAM/manifest utilizado.
2. La fila PAR exacta, con `manifest_record_id`, `manifest_record_revision`, `supersedes_manifest_record_id` (si aplica), clave lógica y campos de contexto.
3. La fila CLAIM_EVIDENCE_LINK completa: tipo de target, FK poblada, `claim_statement`, `evidence_id`, `support_type`, `relevance_scope` y referencias opcionales a evaluación/adjudicación.
4. La fila COVERAGE_REGISTER exacta y su `coverage_scope_id`, `dimension` y `universe_definition/version`.
5. La identidad exacta del SNAPSHOT y su `snapshot_object_record_id`.
6. El registro exacto del CMP owner cuando el contrato de fila PAR lo requiere.
7. La entrada EVIDENCE_REGISTER y la fuente/artefacto subyacente, con identidad, versión, provenance y alcance temporal.
8. Los mappings versionados necesarios para resolver clases, etapas, rutas y versiones; no se permiten inferencias por nombre o por `latest`.
9. El conjunto cerrado de registros/manifiestos consultados para comprobar unicidad, supersession y ausencia de duplicados.

Si falta una fuente necesaria o no se puede demostrar que el conjunto de resolución está cerrado, el resultado correspondiente es UNKNOWN, no FAIL ni ausencia.

### 20.18.3. Secuencia lógica de comprobación

| Paso | Control | Condición para conformidad | Resultado adverso |
|---|---|---|---|
| P0 | Aplicabilidad | La fila PAR y la afirmación son aplicables al contrato, instancia, snapshot, etapa y scope declarados | NA solo por inaplicabilidad ex ante justificada; ambigüedad = UNKNOWN |
| P1 | Forma y target | `claim_target_type=COVERAGE_SCOPE`; exactamente la FK target correspondiente está poblada; no se usa NODE como sustituto | Contradicción demostrada = FAIL |
| P2 | Resolución C0 | `target_coverage_scope_id` resuelve a una única fila y C0 §19 verifica su binding | Reutilizar el resultado C0; no fabricar PASS |
| P3 | Dimensión y universo | `dimension=C10S_CONFIG_PAR`; el envelope y su versión fijan el contexto exacto de la fila PAR | Contradicción = FAIL; versión incompatible sin mapping = NOT_COMPARABLE; falta de datos = UNKNOWN |
| P4 | Resolución PAR | `manifest_record_id` resuelve globalmente a un único registro inmutable y la revisión indicada coincide exactamente | Colisión/duplicidad/identidad contradictoria = FAIL; registry incompleto = UNKNOWN |
| P5 | Clave lógica y pinning | Contrato/instancia, snapshot/record, stage_key, ruta/scope, owner CMP y parameter_key coinciden exactamente con el registro PAR y con el scope | Mismatch demostrado = FAIL; mapping de versión no aprobado = NOT_COMPARABLE |
| P6 | Supersession | Revisión 1 no tiene predecesor; las posteriores enlazan al inmediato anterior; cadena única, sin ciclos, saltos, bifurcaciones ni cruces de clave | Violación demostrada = FAIL; cadena incompleta/no accesible = UNKNOWN |
| P7 | Evidencia | `evidence_id` resuelve a una única entrada EVIDENCE_REGISTER y su artefacto/version/provenance son recuperables | Dangling tras búsqueda exhaustiva = FAIL; fuente inaccesible = UNKNOWN |
| P8 | Correspondencia afirmación–fila | `claim_statement` identifica sin ambigüedad el predicado/estado y la fila PAR; `relevance_scope` coincide con todo el contexto exigido | Contradicción = FAIL; localizador ambiguo o incompleto = UNKNOWN |
| P9 | Pertinencia sustantiva | La fuente respalda el predicado/estado, la unidad, el momento y el alcance declarados; se registran límites y contradicciones | Evidencia contraria o no pertinente demostrada = FAIL para la afirmación; juicio no resoluble = UNKNOWN |
| P10 | Owner CMP separado | Si existe una afirmación independiente sobre el owner, hay otro vínculo NODE exacto; no se exige ese vínculo cuando no se afirma nada independiente sobre el owner | Mezcla/sustitución de targets = FAIL; referencia requerida no resoluble = UNKNOWN |
| P11 | Cobertura | Se evalúa separadamente el denominador, enumeración, fuentes, excepciones y estado COMPLETE/PARTIAL/NONE conforme a §19.3 y U_G §18.6 | Cobertura insuficiente impide claims de exhaustividad/ausencia; no invalida automáticamente una afirmación positiva local bien sustentada |

### 20.18.4. Clave lógica y reglas de identidad

La clave lógica de observación se evalúa conforme a DEC-C10-079. Incluye como mínimo la identidad exacta del contrato/instancia, snapshot y registro, stage_key, ruta/scope, revisión del CMP owner y la identidad semántica de parameter_key. El universo/version y el IAM se comprueban como contexto de resolución y mapping; un simple cambio de empaquetado IAM no crea automáticamente nueva observación.

- `manifest_record_id` es globalmente único en toda la línea C10-S, independiente de versión IAM.
- `manifest_record_revision` identifica la secuencia de captura/adjudicación de esa clave lógica.
- `supersedes_manifest_record_id` debe apuntar al predecesor inmediato de la misma clave.
- Un registro histórico superseded sigue siendo una identidad histórica válida. No se sustituye silenciosamente por la revisión más reciente.
- La afirmación debe declarar si se refiere a la revisión histórica exacta o al estado vigente en un momento determinado. Una afirmación de estado actual no puede usar una revisión superseded como si fuera la última sin justificación temporal explícita.
- Cambio semántico de parameter_key inicia identidad semántica nueva; no se reinterpreta como corrección de captura.

### 20.18.5. Regla de correspondencia del localizador

El control compara los componentes identificadores presentes en `claim_statement` y `relevance_scope` con la fila PAR, el scope y los registros exactos. Ambos campos deben ser mutuamente coherentes y suficientes para una única resolución. Los componentes requeridos no pueden completarse mediante nombre visible, posición de fila, valor de parámetro, timestamp aproximado, hash aislado ni selección de la versión más reciente.

Esta propuesta no congela todavía una gramática serializada, escaping, orden de campos, vocabulario cerrado de `predicate` ni canonicalización del localizador. Mientras esos elementos no se definan, el control es documental/manual: si la representación concreta no permite resolución inequívoca, UNKNOWN. No se permite parsing heurístico para forzar PASS.

### 20.18.6. Resultados por capa y precedencia

Cada capa emite uno de los siguientes estados, con razón y evidencia:

- **PASS:** entradas completas, identidad exacta resuelta, controles aplicables satisfechos y ninguna contradicción detectada.
- **FAIL:** violación demostrada de identidad, unicidad, inmutabilidad, FK, binding, clave lógica, supersession o contradicción sustantiva de la evidencia con la afirmación.
- **UNKNOWN:** faltan fuentes, cobertura de búsqueda, mapping, contexto o evidencia para decidir; incluye localizador ambiguo.
- **NOT_COMPARABLE:** objetos válidos pero incompatibles en versión/schema/contract/scope sin mapping aprobado. No equivale a FAIL ni a DIFFERENT.
- **NA:** relación no aplicable ex ante según contrato y con justificación explícita. No se usa para ocultar datos ausentes o una comprobación fallida.

Para el dictamen de una capa, FAIL demostrado domina; en ausencia de FAIL, una incompatibilidad demostrada produce NOT_COMPARABLE; en ausencia de ambos, cualquier comprobación necesaria irresuelta produce UNKNOWN; solo la evaluación completa permite PASS. NA se informa por control no aplicable y no se elimina del informe. Se conserva el vector de capas; no se colapsa en una etiqueta global que oculte UNKNOWN/NOT_COMPARABLE.

### 20.18.7. Separación entre integridad, evidencia y cobertura

- PASS de C0 solo acredita el binding del scope bajo el universo declarado.
- PASS de PAR_ROW_BINDING acredita que el localizador identifica una fila PAR exacta.
- PASS de EVIDENCE_LINK_INTEGRITY acredita que el vínculo y la fuente se resuelven correctamente.
- PASS de EVIDENCE_RELEVANCE requiere adjudicación de que la evidencia respalda el predicado/estado específico; no se deriva de FK, hash, metadatos o proximidad.
- COMPLETE de COVERAGE_REGISTER es independiente y relativo al universo operativo declarado.
- Ningún resultado de estas capas prueba por sí solo truth DGP, ejecución, efecto causal, contribución a Value ni cierre científico C10.

Una afirmación de ausencia/estado 0 requiere, además, universo pertinente exhaustivo, fuentes válidas y evidencia negativa suficiente conforme a las reglas del predicado. Falta de vínculo, fila o fuente nunca equivale a 0.

### 20.18.8. Casos adversariales documentales mínimos

| Caso | Perturbación | Resultado esperado |
|---|---|---|
| PAR-BIND-01 | Target COVERAGE_SCOPE exacto, localizador y fila PAR coincidentes, evidencia pertinente | PASS por capas evaluadas |
| PAR-BIND-02 | target_coverage_scope_id resuelve a scope de CMP o REF | FAIL |
| PAR-BIND-03 | claim_statement apunta a manifest_record_id distinto del registro resuelto | FAIL |
| PAR-BIND-04 | manifest_record_id duplicado en dos manifiestos | FAIL |
| PAR-BIND-05 | manifest_record_id no encontrado y registry no exhaustivo/inaccesible | UNKNOWN |
| PAR-BIND-06 | manifest_record_revision no coincide con el registro | FAIL |
| PAR-BIND-07 | supersedes apunta a otra clave lógica o salta una revisión | FAIL |
| PAR-BIND-08 | Se usa revisión histórica superseded para afirmar estado actual sin justificación | FAIL de pertinencia temporal |
| PAR-BIND-09 | Nueva versión IAM reempaqueta la misma observación sin mapping de migración | NOT_COMPARABLE para la resolución entre versiones; no crear observación automáticamente |
| PAR-BIND-10 | CMP owner, snapshot, stage_key o ruta no coincide con el scope | FAIL si mismatch explícito; UNKNOWN si falta mapping |
| PAR-BIND-11 | La evidencia existe pero fuente/versión no es accesible | UNKNOWN |
| PAR-BIND-12 | FK correcta pero evidencia no respalda el predicado | FAIL de EVIDENCE_RELEVANCE |
| PAR-BIND-13 | Afirmación PAR y afirmación independiente del owner mezcladas en un único target NODE | FAIL |
| PAR-BIND-14 | Link válido a scope PARTIAL usado para afirmar ausencia exhaustiva | FAIL de la afirmación de ausencia; binding puede PASS |
| PAR-BIND-15 | Localizador no parseable/ambiguo bajo el perfil documental vigente | UNKNOWN |
| PAR-BIND-16 | Se omite vínculo NODE del owner y no existe afirmación independiente sobre el owner | No es fallo; NODE no aplicable |
| PAR-BIND-17 | Evidencias múltiples representadas como filas independientes para misma afirmación/fila | PASS si cada vínculo se resuelve y se evalúa por separado |
| PAR-BIND-18 | Evidencias múltiples comprimidas en un único campo singular/lista embebida | FAIL de cardinalidad/representación |

Los casos son especificaciones adversariales futuras, no fixtures ni resultados ejecutados.

### 20.18.9. Informe documental requerido

Cada futura ejecución autorizada deberá identificar: control y versión, commit de especificación, IAM/manifest y versiones, contrato/instancia, snapshot/record, stage_key, route/scope, object_class/dimension, coverage_scope_id, manifest_record_id/revision/supersession, CMP owner exacto, claim_evidence_id, evidence_id, fuente/version/hash/provenance, conjunto cerrado consultado, resultado por capa e invariante, reason_code, unknown_reason, excepciones, evaluador/adjudicador y timestamp con zona.

La evidencia de salida debe permitir reconstruir exactamente qué registros se examinaron y cuáles quedaron fuera. No se consulta latest implícito ni se corrigen datos durante el control.

### 20.18.10. Gates y límites

- Esta propuesta reutiliza §19 C0 y DEC-C10-079; no crea un segundo control genérico de COVERAGE_SCOPE.
- Los mappings físicos/semánticos pendientes de §20.1–20.5 siguen condicionando PASS; donde no exista correspondencia inequívoca, UNKNOWN.
- No añade columnas, FK, target_type, tabla, tabla puente ni entidad PAR a U_G.
- No cierra la gramática del localizador, escaping, canonicalización, vocabulario predicate, crosswalk IAM↔U_G ni la suficiencia de evidencia para predicados no definidos.
- No crea datos, scopes, manifiestos, fixtures ni registros observados.
- No autoriza parser, validator, scripts, SQL, implementación, Design Freeze, validación técnica, ejecución del control ni experimento científico.

**Estado:** DOCUMENTAL PROPOSAL / NOT ACCEPTED / NOT IMPLEMENTED / NOT EXECUTED / NOT AUDITED. `scientific_execution=false`; `execution_authorized=false`.

 
### 20.18.11. Registro de aceptación — DEC-C10-081

**Estado:** ACEPTADO — contrato lógico documental conforme a DEC-C10-081 (2026-11-08). La aceptación cubre íntegramente el protocolo de §20.18.1–20.18.10: cinco capas, entradas mínimas, secuencia P0–P11, reglas de identidad/supersession, resultados por capa, separación de pertinencia y cobertura, 18 casos adversariales y requisitos de informe.

Se mantienen sin cerrar los mappings físicos/semánticos, la gramática/escaping/canonicalización del localizador y el vocabulario de predicate. Donde la resolución no sea inequívoca, el resultado será UNKNOWN.

La aceptación no autoriza fixtures, parser, validator, scripts, SQL, implementación, Design Freeze, validación técnica, ejecución del control ni experimento científico. No modifica U_G ni el estado científico TGCV. `scientific_execution=false`; `execution_authorized=false`.


## 21. Auditoría de legitimidad del universo y denominadores C0/UDG (2026-11-09)

**Alcance:** auditoría documental de U_G §§17–18, protocolo §§19–20, decisiones citadas DEC-C10-065/070–076 y roster MAP-05. No se inspeccionaron sistemas ni se crearon snapshots, scopes o registros físicos.

### 21.1. Precedencia normativa recuperada

- **C0 / DEC-C10-070:** binding de nueve componentes: contract_id/version, instance_id/version, snapshot_id, snapshot_object_record_id, stage_key, route_id, object_class. `dimension` queda fuera de la tupla y es atributo del COVERAGE_REGISTER.
- **DEC-C10-071:** vocabulario de siete stage_key aceptado; no se equipara con SNAPSHOT.phase ni con el reloj DGP. La etapa se declara en el envelope versionado, no en SNAPSHOT.scope.
- **DEC-C10-072:** `C10S_SCOPE_GLOBAL` es el único token global aceptado para route_id. NULL, vacío, NONE, F y A no lo sustituyen. F/A pueden ser etiquetas auxiliares route_family.
- **DEC-C10-073:** UDG-01/U1 aceptada documentalmente como envelope JSON autocontenido, con EXPLICIT/RULE_DEFINED, miembros tipados y declared_member_count.
- **DEC-C10-074:** JCS + prevalidación TGCV aceptado para canonicalización/integridad; hash canónico no demuestra equivalencia semántica ni exhaustividad.
- **DEC-C10-075:** UDG-03 aceptada como comparación semántica por dimensiones; exige universos exhaustivos y scopes/snapshots comparables para igualdad extensional.
- **DEC-C10-076:** UDG-04 aceptada para identidad lógica/registro y referencias tipadas; no cierra mappings físicos ni crea una tabla PAR.
- La especificación C0 sigue documental, no implementada ni auditada. Las aceptaciones UDG no son autorización de parser, validator, fixtures, schema change ni ejecución.

### 21.2. Inconsistencia detectada y resolución documental

U_G §17.1/§17.4 asignaba B-M01…15 a `COVERAGE_REGISTER.dimension` y presentaba `COV-D2-BMxx` como coverage_scope_id propuestos. U_G §18.6 y C0/UDG, en cambio, reservan `dimension` para C10S_CONFIG_CMP/PAR/REF/RUL/MET y exigen la tupla C0 exacta. Ambas codificaciones no pueden coexistir como valores del mismo campo sin alterar el esquema/enum.

**Resolución:** B-M01…15 son dominios transversales de auditoría, no dimensiones C0. `COV-D2-BMxx` se mantiene como etiqueta lógica de planificación, no como PK/FK física ni fila COVERAGE_REGISTER. El dominio B-M se registra en las afirmaciones y su relevance_scope; cada afirmación se vincula a los scopes C0 pertinentes mediante CLAIM_EVIDENCE_LINK. `COVERAGE_REGISTER.dimension` conserva C10S_CONFIG_CMP/PAR/REF/RUL/MET. No se amplía el enum ni se añade columna. La corrección se refleja en U_G §27.

### 21.3. Universo y denominador: qué cuenta y qué no

1. La cuadrícula 7×5 de U_G §18.6 es un plan de hasta 35 combinaciones lógicas stage_key×object_class por el conjunto previsto de snapshots. No es un denominador material, no son 35 objetos, no es el número de fuentes y no obliga a crear 35 scopes.
2. Cada scope material requiere una tupla C0 completa y única, con snapshot/record exactos. Sin snapshot material no existe scope instanciable.
3. El denominador cuenta miembros del universo versionado, deduplicados por identidad tipada y registro exacto. No cuenta etiquetas B-M, scopes, claims, CLAIM_EVIDENCE_LINK, documentos ni fuentes.
4. EXPLICIT requiere member_refs completos/resolubles; RULE_DEFINED requiere inclusion_rule_ref y dependencias cerradas, resultado reproducible y declared_member_count reconciliado. Una lista vacía no prueba universo vacío.
5. El denominador por clase exige crosswalk de unidad:
   - CMP: identidad contractual/versionada y NODE anchor exacto por snapshot.
   - PAR: propiedad tipada del CMP owner, parameter_key, versión y manifest_record_id; no se inventa object_record_id ni FK PAR.
   - REF: relación tipada con extremos y EDGE record exactos.
   - RUL: regla/version/AST/scope y PREDICATE/operandos resueltos.
   - MET: campo/metadata tipado con owner/target, tiempo y alcance; no se asume una tabla MET única.
6. C0 exige route_id exacto o `C10S_SCOPE_GLOBAL`. Para route-specific, route_record_id se fija en el envelope y la pertenencia NODE/EDGE se prueba con ROUTE_STEP; PREDICATE con route_record_id. F/A no son IDs de ruta.
7. stage_key se mantiene separado de SNAPSHOT.phase y del reloj DGP. El mapping a cada snapshot/registro concreto debe ser explícito y versionado.
8. La dimensión C10S_CONFIG_* es distinta del dominio de auditoría B-M. Un dominio B-M puede requerir evidencia de varios scopes/clases; no se suman sus denominadores ni se crea un scope agregado sin regla de universo aceptada.

### 21.4. Estado de mappings y bloqueos

| Elemento | Estado documental | Qué falta para materializarlo |
|---|---|---|
| Contrato/versión e instancia/versión | IDs candidatos; no instanciados | Identidad contractual aprobada y versión exacta |
| Unidad raíz / CMP anchor | Concepto N01 aceptado, mapping raíz↔CMP OPEN | Mapping exacto y roster contractual |
| Snapshot/record | Pinning Opción A aceptado | Snapshots reales, autorizados, íntegros |
| stage_key | Enum de siete valores aceptado | Asociación por snapshot/registro, sin colapsar phase/tiempo |
| route_id global | Token C10S_SCOPE_GLOBAL aceptado | Aplicación por scope concreto y no colisión |
| route_id route-specific | Semántica aceptada | route_id + route_record_id + ROUTE_STEP exactos |
| object_class | CMP/PAR/REF/RUL/MET aceptado | Crosswalk físico y unidad de denominador por clase |
| dimension | C10S_CONFIG_CMP/PAR/REF/RUL/MET | Regla de elegibilidad por universo; B-M queda como etiqueta de auditoría |
| UDG envelope | U1/JCS aceptados documentalmente | Artefacto versionado real, referencias y provenance |
| C0 | Especificación de control documental | Mapping físico completo, conjunto cerrado de filas y control autorizado |
| Cobertura | NONE / UNKNOWN | Universo/denominador finito, fuentes examinadas/válidas y adjudicación |

### 21.5. Dictamen y gate siguiente

**Resultado:** `DOCUMENTARY_RECONCILIATION_PARTIAL / NO_C0_INSTANCE / NO_SNAPSHOT / DENOMINATOR_UNKNOWN / COVERAGE_NONE`.

Se resolvió la contradicción documental B-Mxx↔dimension sin alterar schema: los B-Mxx son dominios de auditoría; las dimensiones C0 siguen siendo C10S_CONFIG_*; los COV-D2-BMxx son etiquetas lógicas de planificación, no scopes físicos. La legitimidad de denominadores materiales no puede cerrarse hasta resolver contract/instance, unidad raíz↔CMP, snapshots, route-specific IDs y crosswalk por clase.

**Gate siguiente:** cerrar el crosswalk de identidad y unidad de denominador CMP/PAR/REF/RUL/MET —reutilizando U_G §18 y el contrato de identidad PAR— y reconciliarlo con N01/anchor CMP y N16/oráculo. No volver a diseñar UDG-01…04; no crear scopes; no capturar datos ni ejecutar C0. Sin schema change, implementación, Design Freeze o ejecución científica.



## 22. Criterios de adjudicación del crosswalk de identidad y denominador por clase (2026-11-09)

Este protocolo aplica U_G §28 y no crea una equivalencia automática entre clase C10 y registro U_G.

| Clase | PASS de mapping | FAIL de mapping | UNKNOWN / NOT_COMPARABLE |
|---|---|---|---|
| CMP | Identidad/versión/owner y NODE record exactos dentro del snapshot; regla de inclusión satisfecha | Identidad duplicada contradictoria, owner/record incompatible o mapping que viola frontera | Root anchor o record no disponible; versiones sin mapping |
| PAR | manifest_record_id y revisión resuelven; owner CMP y parameter_key/versión coinciden; scope PAR y localizador DEC-C10-080 exactos | Colisión ID, cadena supersession inválida, owner/clave/snapshot/scope contradictorios | Manifiesto/fuente no disponible, localizador ambiguo, mapping de versión ausente |
| REF | Identidad de relación, tipo, cardinalidad y extremos exactos; mapping M versionado y compatible | Extremo/relación contradicho, cardinalidad o identidad incompatible | Endpoints, M, registry o enumeración no exhaustivos |
| RUL | rule_id/version/scope/AST/operandos recuperables y semántica evaluable; PREDICATE exacto cuando aplique | AST/operandos/efecto contradicen identidad o predicate adjudicado | Regla opaca, scope/owner no resuelto, AST inaccesible o mapping no evaluable |
| MET | metadata_key/tipo/owner/target/tiempo y elegibilidad fijados; destino tipado exacto | Owner/tiempo/tipo incompatibles o duplicidad contradictoria | Metadata sin owner/target, ámbito temporal desconocido o elegibilidad sin regla |

PASS solo acredita el mapping tipado de la unidad declarada, no la exhaustividad del universo ni la validez sustantiva de la afirmación. COMPLETE exige además UDG-01 EXPLICIT exhaustivo o RULE_DEFINED reproducible, fuentes válidas, denominador finito, excepciones resueltas y binding C0 correcto. Una discrepancia de contenido debe separarse de una discrepancia de identidad.

La evaluación de pertenencia 1/0/? se realiza por miembro y scope. 0 requiere identidad del objeto y universo de pertenencia cerrados, además de enumeración suficiente para descartar inclusión; no se deriva de no encontrar una fila. NOT_COMPARABLE se reserva para versiones/contratos sin mapping semántico aprobado; no se sustituye por UNKNOWN cuando la incompatibilidad está demostrada.

**PAR específico:** DEC-C10-079/080 prevalecen: target COVERAGE_SCOPE, localizador exacto, manifest_record_id global y revisión append-only. No crear target PAR ni FK directa. El control independiente verifica la fila contra el manifiesto; integridad del binding y verdad de la afirmación siguen siendo capas distintas.



## 23. Adjudicación del mapping NODE raíz ↔ CMP anchor (DEC-C10-082/089)

Este control aplica U_G §28.5 y no reabre las decisiones aceptadas. El objeto de adjudicación es la relación entre dos identidades de dominio, no una comparación de etiquetas.

**Evidencia mínima:** contrato y versión; definición de unidad lógica; roster de componentes y component_id/version; owner/parent; frontera; relación de lifecycle/contención; snapshot exacto; mapping CMP↔NODE; y resolución de la FK SNAPSHOT→NODE raíz.

**Regla:** SAME_ENTITY requiere definición contractual 1:1 y mapping exacto por snapshot. DISTINCT_ENTITIES requiere definiciones e identidades separadas y mappings a NODE distintos; cualquier relación se representa solo con EDGE sustentada. Si falta una fuente crítica o no existe snapshot comparable, UNKNOWN. Si las versiones no tienen mapping semántico aprobado, NOT_COMPARABLE. Contradicciones demostradas producen FAIL. La ausencia de un CMP adicional en un roster no exhaustivo no permite declarar cardinalidad 1 ni inexistencia.

La evaluación de identidad es independiente de la cobertura del roster: PASS de mapping no acredita que todos los CMP estén enumerados. El roster permanece UNKNOWN/PARTIAL hasta que el universo contractual completo y su regla de enumeración estén disponibles. No se declara CMP=1 ni CMP>1 por la sola existencia del root NODE.

No hay inspección técnica ni evidencia contractual aportada en este bloque. No se asignan estados observados 1/0 a objetos, no se crean registros, snapshots o scopes y no se ejecuta C0. El resultado actual es UNKNOWN / OPEN, no un rechazo de identidad.

