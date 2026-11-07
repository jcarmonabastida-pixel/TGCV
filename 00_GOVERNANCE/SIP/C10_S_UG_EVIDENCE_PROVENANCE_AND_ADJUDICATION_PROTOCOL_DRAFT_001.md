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

### 20.4. Crosswalk temporal: `stage_key` no es `SNAPSHOT.phase`

El contrato DGP temporal define los momentos `t−1` basal, `t0` asignación, `t1` política/intento, `t2` instalación/verificación, `t3` accesibilidad post, `t4` espacio de posibilidades, `t5` conocimiento/consideración, `t6` selección/inicio, `t7` ejecución, `t8` Outcome y `t9` Value. En cambio, U_G `SNAPSHOT.phase` utiliza `baseline/post-B/rollback/route-test` para describir el tipo/contexto de captura. Son ejes distintos.

| Eje | Semántica | Representación C0/U_G | Regla |
|---|---|---|---|
| `stage_key` | Momento del proceso DGP | Declaración explícita en `universe_definition/version` | Usar el vocabulario temporal DGP versionado; no inferirlo de phase |
| `SNAPSHOT.phase` | Tipo/contexto de captura | Columna `SNAPSHOT.phase` | Conservar su dominio propio; no convertirlo en etapa causal |
| Tiempo de captura | Instante efectivo de captura | `SNAPSHOT.timestamp` con zona | Evidencia temporal auxiliar; por sí solo no identifica el stage |
| Pertenencia a snapshot | Revisión exacta observada | `snapshot_id + snapshot_object_record_id` | Fijar por DEC-C10-065/Opción A |

**Regla propuesta:** cada `coverage_scope_id` C10-S declara un solo `stage_key` y una revisión exacta de SNAPSHOT en `universe_definition/version`. El registro U_G queda vinculado por el par exacto `snapshot_id + snapshot_object_record_id`. Si el diseño requiere cubrir más de una etapa, se crean scopes distintos; no se agrupan varias etapas bajo un único scope salvo que una decisión posterior defina explícitamente un universo multi-etapa y sus denominadores.

No se acepta una transformación automática `stage_key ↔ SNAPSHOT.phase`. La tabla anterior es un crosswalk de ejes, no una equivalencia de valores.

### 20.5. Crosswalk de ruta y alcance global

Opción A + DEC-C10-065 ya fija pertenencia y referencias exactas:

- ROUTE tiene `route_id` semántico y `object_record_id` versionado, fijados al snapshot exacto.
- PREDICATE referencia la revisión exacta de ROUTE mediante `route_record_id` y el pinning del snapshot.
- ROUTE_STEP es la fuente canónica del orden y referencia ROUTE/NODE/EDGE mediante record IDs exactos dentro del mismo snapshot.
- NODE y EDGE no tienen una columna universal `route_id`; su pertenencia a una ruta concreta solo se demuestra por su inclusión exacta en ROUTE_STEP de la revisión concreta de ROUTE.
- `routes_affected` y texto libre no son evidencia de pertenencia.

**Regla propuesta para C0:**

1. Scope route-specific: `route_id` debe resolver a una única revisión de ROUTE dentro del snapshot fijado; para NODE/EDGE, el registro debe aparecer en la secuencia ROUTE_STEP de esa revisión. Para PREDICATE, debe resolver `route_record_id` a esa misma revisión. Para ROUTE, debe ser el propio registro.
2. Scope global a etapa/snapshot: se requiere un token reservado, explícito y versionado para “global/no restringido a una ruta”, distinto de NULL, vacío o comodín. Su literal aún NO está aceptado; no se fija aquí.
3. Si la ruta no puede reconstruirse exhaustivamente desde ROUTE_STEP, la pertenencia route-specific es UNKNOWN. Si una referencia exacta contradice el route_id declarado, es FAIL.
4. La inclusión de un nodo/edge en varias rutas produce varias relaciones de pertenencia, no duplicación ficticia del objeto ni colapso de los scopes.

### 20.6. Crosswalk candidato por familia C10

El siguiente cuadro es una guía de correspondencia semántica para diseñar el `universe_definition`; no establece equivalencias obligatorias ni crea registros.

| source_object_class | Registros U_G candidatos | Correspondencia y cautela |
|---|---|---|
| CMP | NODE; EDGE cuando exista una relación constitutiva entre componentes | CMP material se representa normalmente como NODE con semantic_role apropiado; EDGE representa dependencia/interacción, no el componente. No convertir una relación en CMP. |
| PAR | NODE para propiedad/clave cuando tenga identidad propia y granularidad exigida; propiedades tipadas del NODE/artefacto propietario cuando el contrato admita representación atómica en sus campos | El crosswalk debe fijar clave/owner, tipo, dominio, estado y granularidad. No crear NODE por cada valor ni asumir que todos los PAR son nodos separados. |
| REF | EDGE para referencias/dependencias tipadas; en casos definidos, campos de referencia tipada U_G | Usar el catálogo de relaciones permitido. Una REF declarativa no demuestra por sí sola resolución, instalación o disponibilidad efectiva. |
| RUL | PREDICATE cuando la regla se evalúa como condición/predicado; NODE/EDGE solo para la identidad de su definición u operandos cuando sea necesario | Preservar rule_id, AST, operandos, scope y efecto mediante mapping explícito; no confundir AST bien formado (FP-01) con preservación semántica (FP-03). |
| MET | Metadatos tipados de los registros de objeto; SNAPSHOT para metadatos de captura; EVIDENCE_REGISTER para procedencia/custodia de fuente | MET es transversal y no corresponde a una tabla única. Clasificar cada propiedad por owner, ámbito, tiempo y función; no duplicar source_provenance fuera de EVIDENCE_REGISTER ni confundir record-time con validez/observación. |

La granularidad fuente puede exigir varios registros U_G, y un registro U_G puede contener varias propiedades tipadas. El crosswalk debe declarar cardinalidad, owner, clave de propiedad, regla de inclusión y evidencia de correspondencia; no se permite deducirla por similitud nominal.

### 20.7. Dimensión de cobertura y regla de inclusión

`COVERAGE_REGISTER.dimension` identifica la dimensión del universo cubierto; `coverage_scope_id` es el vínculo común de los registros U_G. La dimensión no necesita replicarse como columna en NODE/EDGE/ROUTE/PREDICATE: se obtiene del scope, pero el universo debe definir qué registros/propiedades son elegibles para ese scope.

Cada `universe_definition/version` deberá especificar: (a) `dimension` y su vocabulario; (b) unidad de denominador; (c) conjunto de clases C10 aplicables; (d) tipos de registro U_G admisibles; (e) regla de inclusión/exclusión por objeto/propiedad; (f) cardinalidad esperada; (g) ruta/etapa y snapshot fijados; (h) fuentes que permiten reconstruir la enumeración. El mismo registro puede pertenecer a scopes distintos solo cuando sus dimensiones/etapas/rutas sean distintas y cada pertenencia esté declarada; no se fusionan denominadores.

**Dictamen de esta operación:** se reutilizan los contratos y crosswalk históricos. Se propone mantener `stage_key` en el universo versionado, preservar `SNAPSHOT.phase` como eje separado, resolver rutas mediante ROUTE/ROUTE_STEP exactos, y mantener `source_object_class` separado de `ug_record_type` y `semantic_role`. No se selecciona aún el token global de ruta, ni la gramática serializada completa de `universe_definition/version`, ni se autoriza cambio de schema, implementación o ejecución.
