# C10-S F5/G7 v1.1 — especificación integrada de cierre del gate instrumental

**Registro:** C10S-F5-G7-INTEGRATED-GATE-CLOSURE-SPEC-001  
**Fecha:** 2026-11-25  
**Rama:** `research/c10s-f5-g7-canonical-mle-v1.1-20261122`  
**PR:** #119 (Draft; no integrado)  
**Commit base:** `6d9f5f35503c27abe924611976e8d5e66fe7df0a`  
**Estado:** SPECIFICATION FOR IMPLEMENTATION / NOT G7 AUTHORIZATION  
**Ámbito:** cierre técnico del gate instrumental F5/G7 v1.1. No modifica estimandos, DGP, outcomes, reglas de falsación, bancos de semillas ni integración científica C10-S.

## 1. Propósito y regla de no repetición

Esta especificación consolida RG-01…RG-07 en un único contrato verificable. Sustituye la ejecución por parches aislados: ningún requisito se considerará cerrado por un test que solo compruebe presencia de texto, por un PASS de compilación, o por una simulación que no atraviese la interfaz productiva correspondiente.

La reconciliación previa ya identificó las causas y su relación. Este documento no repite ese diagnóstico; fija qué debe implementarse, cómo se prueba y qué evidencia permite cerrar cada requisito.

**No se inicia G7, holdout, bootstrap confirmatorio, cobertura, replay científico ni adjudicación Tier-A durante la implementación/validación de esta especificación.** Solo se permiten pruebas deterministas de software con fixtures sintéticos y repositorios/artefactos temporales.

## 2. Estado de partida verificado

HEAD auditado: `6d9f5f35503c27abe924611976e8d5e66fe7df0a`.

| RG | Estado en HEAD | Evidencia y límite |
|---|---|---|
| RG-01 nombre/descubrimiento de perfil | PASS determinista | Productor/consumidor alineados; prueba contractual. La prueba no sustituye el recorrido de descarga real. |
| RG-02 integridad ZIP y JSON | Implementado; PASS determinista | Workflow descarga ZIP por API y compara SHA-256 ZIP y JSON con manifest. El test actual inspecciona literales del workflow; aún no ejecuta el paso de descarga contra un artefacto temporal/real. |
| RG-03 identidad compute path / Git | PASS en repositorio temporal real | Test crea commits reales, valida ascendencia y detecta cambio de archivo. No prueba aún el checkout/manifest de autorización de extremo a extremo. |
| RG-04 aprobación humana | NO CERRADO | Validador aún acepta `approved_by=USER_EXPLICIT_APPROVAL`; push + mensaje de commit no son una atestación independiente. |
| RG-05 inventarios de identidad | NO CERRADO | `PROFILE_SOURCE_PATHS` y `SOURCE_HASH_PATHS` son listas manuales distintas, con solapamiento que puede derivar. |
| RG-06 overhead de 300 s | NO JUSTIFICADO | Constante fija por fase; no hay evidencia desglosada que demuestre que cubre setup real. |
| RG-07 extrapolación K=100→K=1.000 | CONDICIONAL | Máximo observado de 100 datasets no es cota de los 1.000. La proyección de scheduling es una cota para tiempos de trabajo estimados, no una garantía física. |

El run `45538151019` terminó 7/7 PASS en la suite determinista del commit anterior. Esto valida esa suite; no equivale a ejecutar el preflight productivo completo.

## 3. Contrato canónico de artefacto (RG-01/RG-02)

### 3.1 Identidad única

El manifest de perfil es la autoridad de identidad y debe declarar, como mínimo:
- schema/version;
- nombre exacto del miembro JSON dentro del ZIP;
- profile run ID y artifact ID;
- nombre completo e ID numérico del repositorio de origen, contrastados con los IDs del objeto artifact/workflow_run de GitHub;
- source commit;
- profile scope, namespace, K y B;
- SHA-256 del ZIP y del JSON;
- roster de celdas y denominadores.

El productor, consumidor, validador y tests deben leer el nombre del miembro del manifest/constante compartida. Se prohíben literales divergentes mantenidos manualmente. El manifest se valida contra un schema estricto; campos desconocidos o ausentes fallan cerrados.

### 3.2 Descarga y verificación

El preflight productivo debe:
1. recuperar run/artifact identificados por el manifest y autorización;
2. verificar que el artifact pertenece al run esperado y al repositorio esperado (no confiar solo en el ID proporcionado);
3. descargar los bytes del ZIP original;
4. calcular SHA-256 del ZIP y compararlo con manifest;
5. extraer de forma segura el único miembro canónico, rechazando rutas absolutas, traversal, duplicados y miembros inesperados si el contrato los excluye;
6. calcular SHA-256 del JSON extraído y compararlo con manifest;
7. validar schema, scope, celdas, K/B, namespace y source commit;
8. solo entonces entregar el perfil al dimensionador.

Cada error debe abortar antes de crear/emitir la matriz. No se permite continuar con perfil alternativo, caché no identificada ni JSON preexistente.

### 3.3 Pruebas RG-01/RG-02

La prueba integrada debe ejecutar una función Python compartida por workflow/test (no limitarse a buscar cadenas YAML) sobre:
- ZIP fixture válido;
- ZIP con un byte alterado;
- JSON interno alterado manteniendo ZIP reempaquetado;
- nombre de miembro ausente o incorrecto;
- ZIP con path traversal o miembros duplicados;
- manifest con run/artifact/repo incoherente.

Criterio PASS: válido aceptado; cada variante adulterada/referencialmente incoherente rechazada antes de invocar dimensionador. Un test del texto del workflow puede permanecer como lint, nunca como prueba principal.

## 4. Aprobación y autorización de ejecución (RG-04)

### 4.1 Separación de estados

Se distinguen cuatro elementos que no deben confundirse:
1. **Autorización humana explícita:** acción consciente del responsable único al despachar manualmente el workflow y seleccionar la confirmación exacta de alcance.
2. **Atestación técnica de GitHub:** identidad del actor, evento, ref/SHA, run ID y attempt, conservados en un artefacto inmutable del run.
3. **Validación técnica:** comprobación del registro de un solo uso, rama, commit padre, ventana, manifests y perfil.
4. **Permiso científico:** sigue requiriendo una autorización explícita, vigente y delimitada; no se deriva de la mera existencia del workflow ni de un test PASS.

El JSON ya no puede autodeclarar consentimiento mediante `approved_by=USER_EXPLICIT_APPROVAL`. Debe declarar `approval_channel=GITHUB_WORKFLOW_DISPATCH`; el workflow comprueba además que el actor sea el propietario del repositorio, que el evento sea `workflow_dispatch`, que la rama sea la rama de autorización dedicada y que el usuario seleccione la confirmación literal del alcance. El mensaje de commit no concede autorización.

### 4.2 Mecanismo para un único responsable

El workflow debe:
- aceptar exclusivamente `workflow_dispatch`, sin rutas `push` ni disparadores automáticos;
- ejecutarse sobre la rama de autorización de un solo uso y el SHA exacto seleccionado;
- exigir actor igual a `github.repository_owner` (no basta con que el actor sea autor del commit);
- exigir la confirmación literal `I_APPROVE_C10S_F5_G7_TIERA_V1_1_ON_THIS_COMMIT`;
- validar que el registro de autorización enlaza el commit de código aprobado como único padre y que no ha caducado;
- generar y conservar `g7-dispatch-attestation.json` con actor, evento, ref, SHA, run ID, attempt, alcance confirmado y la declaración `independent_review=NOT_AVAILABLE_SINGLE_OPERATOR`;
- no depender de GitHub Environment ni de sus reglas de reviewers; el run y el artefacto de atestación de Actions constituyen el registro auditable;
- mantener todos los jobs científicos detrás del job de autorización y fallar cerradamente ante cualquier ausencia o discordancia.

La atestación demuestra quién despachó qué snapshot y qué alcance confirmó; no se presenta como revisión independiente. Al existir un único responsable, la revisión independiente se declara no disponible y no se simula mediante autoaprobación. El workflow no declara `environment:`: así no queda sujeto a una regla administrativa de reviewers que reproduzca el bloqueo que se está eliminando.

### 4.3 Un solo uso y no herencia

Cada autorización se consume en su rama dedicada, no solo mediante una atestación efímera del run:

- Un grupo de concurrencia a nivel de workflow serializa los dispatches sobre la misma ref.
- El gate consulta el historial de workflow_dispatch de esa rama y rechaza cualquier run anterior, incluso si terminó en fallo. La consulta falla cerrada si GitHub no responde.
- El primer intento debe tener github.run_attempt == 1. Preflight, banco primario/replay y adjudicación vuelven a comprobarlo en sus condiciones de ejecución; así, «Re-run failed jobs» no puede reanudar una ejecución cuyo job de autorización ya terminó correctamente.
- Tras validar el registro, el workflow crea mediante GitHub Contents API un marcador 00_GOVERNANCE/authorizations/consumed/<authorization_id>.json en la propia rama. La creación es atómica (no se suministra SHA de archivo existente) y se verifica que el commit del marcador tenga como padre único el commit de autorización y que la ref apunte al nuevo commit.
- Una nueva invocación sobre esa rama queda bloqueada por el historial y, aun si ese historial no estuviera disponible, el marcador hace que la ref ya no sea el commit de autorización válido. El marcador conserva ID, commit de autorización, código aprobado, rama, run y actor.

La combinación de concurrencia, historial, control de intento y marcador persistente impide el segundo dispatch y el reintento ordinario. Como límite de gobernanza, un propietario con capacidad de reescribir forzosamente la rama o alterar/eliminar los registros puede eludir controles del propio repositorio; no se presenta como una garantía criptográfica frente al administrador del repositorio. Tier-B y ejecución causal C10 permanecen excluidos.

### 4.4 Pruebas RG-04

- Tests estáticos: solo `workflow_dispatch`; ausencia de `push`; actor propietario; confirmación literal; artefacto de atestación; todos los jobs científicos dependen del job de autorización.
- Tests negativos: actor distinto del propietario, evento distinto, rama no autorizada, confirmación ausente/incorrecta, SHA distinto, registro ausente/caducado y scope ampliado.
- La configuración administrativa de reviewers no es un requisito porque no existe un segundo revisor independiente. No se usa GitHub Environment como gate ni como requisito administrativo.

## 5. Identidad de código sin inventarios duplicados (RG-05)

### 5.1 Dos conceptos, una fuente generadora

Compute-path identity y execution-source identity son conjuntos conceptualmente distintos:
- **Compute path:** archivos cuyo contenido determina la medición de recursos y por tanto la reutilización del perfil.
- **Execution source:** código, protocolos, workflows, tests, fixtures y dependencias que determinan la ejecución G7 autorizada.

No se deben fusionar ambos conjuntos por conveniencia, ni mantener dos listas manuales independientes.

### 5.2 Generación determinista

Crear un único registro versionado de rutas tipadas (p. ej. `c10s_f5_g7_source_inventory.json`) con clasificación por ruta: `compute_path`, `execution_source` o ambas, y exclusiones justificadas. Un único generador:
- valida que cada ruta exista y esté versionada;
- calcula SHA-256 desde el árbol Git del commit (no del working tree);
- produce dos manifests derivados, con schema/version, commit, paths ordenadas y digests;
- genera un root digest de cada manifest;
- falla ante rutas duplicadas, no clasificadas, ausentes o exclusiones no justificadas.

El validador de perfil consume el digest/manifest compute-path. El validador de autorización consume execution-source manifest y referencia el compute-path manifest por digest. No mantiene su propia lista paralela de rutas.

### 5.3 Pruebas RG-05

- determinismo byte a byte con el mismo tree SHA;
- orden de rutas estable;
- detección de archivo añadido/modificado/eliminado;
- detección de ruta no clasificada/duplicada;
- autorización que referencia digest obsoleto rechazada;
- perfil reutilizado tras cambio en compute path rechazado;
- cambio solo en documento no compute-path no invalida perfil, pero sí cambia execution-source manifest cuando ese documento forma parte del alcance aprobado.

## 6. Presupuesto temporal y extrapolación (RG-06/RG-07)

### 6.1 RG-06: overhead

No se debe mantener 300 s como si fuera una constante empíricamente garantizada. Descomponerlo en:
- checkout/materialización;
- instalación de dependencias;
- inicialización del proceso;
- transferencia/descarga de artefactos;
- overhead de runner y workflow.

Reutilizar los logs y timestamps existentes. Si los datos disponibles no aíslan componentes, documentar explícitamente que 300 s es una reserva de ingeniería elegida, no una medición. Definir sensibilidad con al menos tres escenarios (p. ej. 300/600/900 s por fase) sin ejecutar datasets científicos. El presupuesto por job sigue siendo 9.000 s y timeout 165 min; cualquier escenario que supere el límite invalida esa topología/tamaño.

### 6.2 RG-07: extrapolación

El máximo muestral K=100 no es un límite determinista de latencia futura. La proyección debe etiquetarse como condicional y acompañarse de:
- estadísticos observados (media, P95, P99, máximo);
- agregación conservadora por shard;
- incertidumbre muestral del extremo de cola, si puede estimarse con datos guardados;
- sensibilidad de job size y overhead;
- regla fail-closed ante incertidumbre que impida garantizar el límite de 150 min.

No ejecutar un perfil nuevo solo para resolver la documentación. Si los datos guardados no permiten una cota predictiva defendible, RG-07 queda CONDITIONAL y no se puede describir el plan como temporalmente garantizado. La fórmula de Graham para una lista de jobs sobre pool compartido permanece como cota de scheduling de los tiempos asumidos.

### 6.3 Pruebas RG-06/RG-07

Pruebas deterministas sobre datos de perfil ya persistidos: recomputar escenarios de overhead, confirmar límites por job y proyección global, y comprobar que el informe distingue límite de scheduling de incertidumbre de duración. No simular que datos sintéticos prueban una distribución empírica real.

## 7. Validación integrada y negativa (un único gate)

El cierre requiere un único conjunto de pruebas no científicas que ejecute, en orden:
1. generar manifests desde un tree Git real;
2. empaquetar/recuperar el ZIP de fixture;
3. verificar identidad del run/artifact (fixture local de API en tests; prueba productiva separada);
4. verificar ZIP, extraer miembro canónico y verificar JSON;
5. validar source commit/compute path;
6. validar autorización estructural y deployment approval;
7. derivar la matriz a partir del perfil validado;
8. comprobar que los jobs científicos permanecen bloqueados si cualquier gate anterior falla.

Cada gate debe tener al menos un caso negativo. La prueba principal debe invocar funciones productivas compartidas por workflow y tests. Los tests de YAML son complementarios.

La suite se ejecuta en una sola validación determinista sobre el commit integrado. No se deben crear commits intermedios que disparen workflows G7. Los workflows automáticos de validación de software pueden ejecutarse; los workflows de ejecución científica permanecen inalcanzables.

## 8. Criterios de cierre por requisito

| RG | PASS exigido | Si no puede probarse |
|---|---|---|
| RG-01 | Productor, manifest, consumidor y extractor usan identidad única; negativo de miembro ausente | FAIL |
| RG-02 | ZIP real de fixture validado contra digest; JSON validado; negativos de alteración y traversal | FAIL |
| RG-03 | Repositorio Git real: ascendencia y contenido; negativos de no-ancestro y cambio | FAIL |
| RG-04 | Dispatch manual del propietario, confirmación literal de alcance y atestación actor/ref/SHA/run conservada; sin revisión independiente ficticia | FAIL si actor/evento/alcance no coinciden |
| RG-05 | Inventario tipado único genera ambos manifests deterministas; negativos de drift | FAIL |
| RG-06 | Overhead medido o declarado como reserva; sensibilidad no excede presupuesto | CONDITIONAL si solo reserva |
| RG-07 | Extrapolación defendible o declarada condicional con límite de uso | CONDITIONAL; no afirmar garantía |

**Cierre del gate instrumental para G7:** RG-01…RG-05 deben estar PASS. RG-06/RG-07 deben tener evaluación documentada y la proyección debe satisfacer los límites bajo los escenarios aceptados. RG-04 bloquea toda ejecución si no puede verificarse el actor propietario, el dispatch manual, el alcance literal, la atestación o la identidad del commit. Un PASS determinista no sustituye una autorización explícita para el run concreto.

## 9. Preservación de gobernanza y alcance

- PR #119 permanece Draft.
- No modificar `main`, PR #116 ni Evidence→Claim Matrix/RMA.
- No modificar contratos científicos, DGP, estimandos, thresholds, seed bank ni adjudicador.
- No ejecutar G7, holdout, cobertura, bootstrap confirmatorio, replay científico ni Tier-A.
- No repetir el perfil resource-only existente.
- Cualquier nueva ejecución G7 requiere un dispatch manual explícito del propietario sobre la rama/commit de autorización de un solo uso, confirmación literal del alcance y validación técnica satisfactoria. Este cambio de mecanismo no equivale a emitir ahora esa autorización.


## 10. Adjudicación RG-06/RG-07 con evidencia persistida

Esta actualización utiliza exclusivamente el artefacto resource-only ya existente; no se ha repetido el perfil ni se han ejecutado datasets nuevos.

**Fuente de tiempos:** run 45365559253, artifact 14908914198, source commit 8b62b89a78681cc39bdd4c0cbb76c43ef073c1e9, K=100 por celda, B=1.000, coverage_adjudication=NOT_PERFORMED. El ZIP original y el JSON extraído se verificaron contra sus dos SHA-256 canónicos. El perfil registra 20 shards, 200 datasets y 2.600,725 s de wall time del propio perfil resource-only.

### 10.1 RG-06 — overhead

Los logs de tres shards existentes del mismo entorno Ubuntu 24.04/pinned Python muestran desde el primer registro del runner hasta el inicio del cálculo:

| Job | Inicio del runner | Inicio del cálculo | Setup observado |
|---|---:|---:|---:|
| 138346242310 | 09:28:42.716 | 09:29:02.772 | 20,055 s |
| 138346242252 | 09:28:42.714 | 09:28:59.352 | 16,638 s |
| 138346242265 | 09:28:42.849 | 09:29:04.544 | 21,695 s |

En los jobs de agregación y empaquetado, la descarga del artefacto existente duró 0,591 s (138370192179) y 0,451 s (138370455491). Estas medidas incluyen el flujo de perfilado resource-only, no constituyen una medición directa de todos los pasos del futuro workflow G7.

El setup observado (16,638–21,695 s) pertenece al workflow resource-only v1.1 y cubre runner, checkout, instalación hash-locked y llegada al cálculo. El allowance de **900 s por fase** adoptado por el dimensionador es una reserva de ingeniería —15 minutos, aproximadamente 41,5 veces el mayor setup observado—, no una constante medida del workflow G7 consumidor.

Con el máximo observado de la celda lenta (418,194638 s/dataset) y **8 datasets por shard**, el job pareado primary+replay se proyecta en **8.491,114 s (141,519 min)**, con margen de **508,886 s (8,481 min)** frente al presupuesto de 9.000 s.

| Reserva por fase | Job pareado lento, shard 8 | ¿Dentro de 9.000 s? |
|---:|---:|---|
| 300 s | 7.291,114 s (121,519 min) | Sí, margen 1.708,886 s |
| 600 s | 7.891,114 s (131,519 min) | Sí, margen 1.108,886 s |
| 900 s | 8.491,114 s (141,519 min) | Sí, margen 508,886 s |

El plan derivado para K=1.000 es de **125 shards por celda y 250 jobs de matriz por fase**, con un pool compartido de 20. El coste agregado conservador primary+replay es **361,756 runner-hours**. La cota de list scheduling de Graham es **73.182,699 s (20,329 h)** para primary+replay y **75.783,425 s (21,051 h)** al añadir el perfil resource-only ya ejecutado (2.600,725 s). Son estimaciones condicionadas a la latencia máxima muestral y al allowance de 900 s; no son garantías de duración.

**Estado RG-06: CONDITIONAL — PLAN ROBUSTO BAJO LA RESERVA DECLARADA.** La sensibilidad 300/600/900 s queda dentro del presupuesto con shard 8. La reserva de 900 s sigue siendo una hipótesis de ingeniería y no una medición completa del recorrido G7 consumidor; no se eleva a garantía temporal.

### 10.2 RG-07 — K=100 → K=1.000

Estadísticos guardados del artefacto (segundos por dataset):

| Celda | Media | P95 | P99 | Máximo |
|---|---:|---:|---:|---:|
| F5_beta22_M10_R5 | 0,372553 | 0,413426 | 7,674969 | 7,966772 |
| F5_beta22_M30_R20 | 208,420042 | 285,520522 | 356,961762 | 418,194638 |

El dimensionador utiliza el máximo observado por dataset y el allowance de 900 s/fase. Con shard size 8, K=1.000 por celda, dos celdas, **125 shards por celda (250 jobs por fase)** y max-parallel=20 compartido, el trabajo agregado pareado conservador es **361,756 runner-hours**. La cota de list scheduling de Graham es **73.182,699 s (20,329 h)** para primary+replay; incluyendo el perfil resource-only ya ejecutado, el recorrido estimado suma **75.783,425 s (21,051 h)**. Es una cota de scheduling de tiempos asumidos, no una cota probabilística de la duración real.

Con K=100 observaciones IID, la probabilidad de que el máximo muestral supere el verdadero P99 es 1−0,99^100 = **63,397 %**; para el P95 es 1−0,95^100 = **99,408 %**. Harían falta al menos **299 observaciones IID** para que el máximo muestral exceda el verdadero P99 con un 95 % de confianza. Además, bajo IID continuo/exchangeability, la probabilidad de que el máximo de 1.000 observaciones futuras no supere el máximo de las 100 observaciones del perfil es solo 100/(100+1.000) = **9,091 %**; la probabilidad de que lo supere es **90,909 %**. Por tanto, el máximo K=100 no es una cota predictiva defendible para el máximo K=1.000.

**Estado RG-07: CONDITIONAL — RIESGO DE COLA EXPLÍCITO.** El dimensionamiento shard 8 satisface el presupuesto de 150 minutos bajo el máximo observado y la reserva declarada, pero K=100 no garantiza el máximo ni los percentiles extremos de K=1.000. El workflow debe conservar timeout y fallo cerrado; no se describirá el plan como temporalmente garantizado. No se generará otro perfil para intentar cerrar esta limitación sin autorización expresa.

### 10.3 Límite de uso

RG-06 y RG-07 quedan evaluados con evidencia existente, pero no autorizan ejecución. RG-04 ha superado la validación determinista del mecanismo de dispatch y atestación en el run 45638639205 (8/8 jobs SUCCESS, commit de código `ceda2f765c1c9554e2af2223c731ad77646ce05c`). La actualización de dimensionamiento RG-06/RG-07 se validó en el run `45646262954` (8/8 jobs SUCCESS) sobre el commit `4cf9ca6534648e34d79d970d351e4c403cbf8de2`. El HEAD documental actual `87742dc90261e9a84f2c2f0282224e691fbb3ea1` solo añade dos reconciliaciones documentales posteriores: no altera el dimensionador, workflow, validador ni tests. El estado RG-02 y RG-05 se actualiza en las subsecciones 10.4 y 10.5, a partir de la descarga productiva del artefacto y de la validación integrada posterior a esta adjudicación.

### 10.4 RG-02 — verificación material del artefacto productivo

El artefacto original `c10s-f5-g7-resource-profile-v1-1` (ID `14908914198`, run `45365559253`) se descargó directamente mediante el endpoint de descarga de artefactos de GitHub Actions, sin reconstruir ni reempaquetar el ZIP. Se calculó SHA-256 sobre los bytes descargados y sobre el único miembro JSON extraído:

| Objeto | SHA-256 esperado en manifest | SHA-256 calculado |
|---|---|---|
| ZIP original | `14e317a6f38d9934dc0903b4b038da5ffc580c9bb076d26dbcc6e47cfe568e21` | `14e317a6f38d9934dc0903b4b038da5ffc580c9bb076d26dbcc6e47cfe568e21` |
| JSON extraído | `005ef265fa7dd8812c2572d9187cc7943c365506dc8e1169f1883487c0094d9f` | `005ef265fa7dd8812c2572d9187cc7943c365506dc8e1169f1883487c0094d9f` |

El ZIP contiene exactamente un miembro: `c10s-f5-g7-resource-profile.json`. El manifiesto v003 liga el perfil al repositorio `jcarmonabastida-pixel/TGCV`, ID `1348691577`, al run `45365559253`, al commit fuente `8b62b89a78681cc39bdd4c0cbb76c43ef073c1e9`, namespace `c10s_f5_g7_resource_v1_1`, K=100, C0_B=C5_B=1.000 y scope resource-only con `coverage_adjudication=NOT_PERFORMED`.

La validación integrada del consumidor contra la forma real de metadatos de GitHub y los casos negativos de identidad de repositorio pasó en el run `45550608608`. Ese run terminó SUCCESS con 8/8 jobs en el commit `60c34a17606627a62c7f0db2064855985cf2efe9`.

**Estado RG-02: PASS.** La descarga y la integridad de los bytes del artefacto existente están verificadas; esto no equivale a ejecutar G7 ni autoriza consumir el perfil para una ejecución científica.

### 10.5 RG-05 — inventario único y clausura de fuentes

El inventario tipado único `c10s_f5_g7_source_inventory.json` contiene 55 rutas: 19 clasificadas como `compute_path` y 55 como `execution_source` (con solapamiento tipado). El generador de manifest del perfil queda clasificado solo como `execution_source`: se ejecuta después de terminar y agregar los shards de medición, por lo que no determina los tiempos observados ni forma parte del compute path medido. La revisión de roles eleva el inventario a versión 2 sin cambiar el protocolo ni los datos del perfil K=100 existente. El inventario incluye el código transitivo importado por el ejecutor, tests y workflows, y el fixture ZIP inmutable. El generador produce los manifests derivados y los hashes desde el árbol Git; las pruebas detectan dependencias transitivas ausentes, referencias de workflow/test fuera del inventario y fixtures no identificados.

La suite de validación del run `45550608608`, commit `60c34a17606627a62c7f0db2064855985cf2efe9`, terminó SUCCESS 8/8. El job de compilación y las particiones de autorización, perfil, artefactos, shards, bootstrap y polinomios terminaron todas en SUCCESS.

**Estado RG-05: PASS.** El inventario y su cobertura quedan validados en ese commit. No se ha modificado `main` ni se ha promovido el PR #119.

### 10.6 Estado consolidado del gate

| Requisito | Estado actualizado | Evidencia / límite |
|---|---|---|
| RG-01 | PASS determinista | Contrato de nombre y descubrimiento alineado |
| RG-02 | PASS | ZIP productivo descargado; hashes ZIP/JSON coincidentes; verificación integrada 8/8 |
| RG-03 | PASS determinista | Identidad Git / compute path |
| RG-04 | PASS_STATIC | Dispatch manual del propietario, confirmación literal y atestación validados por CI 8/8; sin dependencia de Environment/reviewers |
| RG-05 | PASS | Inventario tipado único; cobertura integrada 8/8 |
| RG-06 | CONDITIONAL — PLAN ROBUSTO BAJO RESERVA 900 s | Shard 8; margen calculado de 508,886 s frente a 9.000 s incluso en sensibilidad 900 s/fase |
| RG-07 | CONDITIONAL — RIESGO DE COLA EXPLÍCITO | K=100 no garantiza el máximo K=1.000; probabilidad IID de superar el máximo muestral: 90,909 % |

**Decisión:** RG-01…RG-05 están cerrados en los niveles de evidencia indicados. RG-06 y RG-07 quedan CONDITIONAL, pero el plan operativo derivado con shard 8 satisface el presupuesto de 150 minutos bajo la reserva declarada de 900 s/fase y sus sensibilidades 300/600/900 s. Esta aceptación es una envolvente de planificación condicionada, no una garantía de duración ni una autorización de ejecución. G7 permanece sin autorización vigente: requiere un nuevo dispatch manual del propietario sobre un commit de autorización de un solo uso y validación completa. No se inicia G7, Tier-A, holdout, cobertura, replay científico ni ejecución causal C10.

### 10.7 RG-04 — autorización explícita para un único responsable

El diseño previo exigía revisores obligatorios y prevención de autoaprobación en el Environment. Ese requisito suponía la existencia de una segunda persona revisora que no existe en la estructura actual del proyecto. Mantenerlo no aportaba una revisión independiente real: bloqueaba el flujo por una condición organizativa ficticia.

Se sustituye por un control de autorización humana explícita, acotada y auditable:
- evento exclusivamente `workflow_dispatch`;
- actor igual al propietario del repositorio;
- confirmación literal del alcance G7 v1.1;
- rama de autorización dedicada y commit de autorización de un solo uso;
- registro técnico enlazado al commit de código aprobado como único padre;
- artefacto `g7-dispatch-attestation.json` que conserva actor, evento, ref, SHA, run ID, attempt y alcance confirmado;
- jobs científicos dependientes del job de autorización y bloqueados ante cualquier discordancia.

La revisión independiente queda registrada como `NOT_AVAILABLE_SINGLE_OPERATOR`; no se simula mediante autoaprobación. El workflow deja de declarar GitHub Environment; la atestación y los metadatos nativos del run son el registro auditable.

**Estado RG-04: PASS_STATIC — VALIDADO POR CI.** El run `45638639205` terminó SUCCESS con 8/8 jobs, incluida la partición `test_c10s_f5_g7_tiera_authorization`, sobre `ceda2f765c1c9554e2af2223c731ad77646ce05c`. El único cambio posterior hasta el HEAD `87742dc90261e9a84f2c2f0282224e691fbb3ea1` es documental; no altera workflow, validador ni tests. El PASS cubre el contrato y los tests estáticos/deterministas: no demuestra todavía una ejecución real de dispatch, ni una autorización vigente, ni habilita G7. No se ha ejecutado G7 ni se ha modificado `main`.
