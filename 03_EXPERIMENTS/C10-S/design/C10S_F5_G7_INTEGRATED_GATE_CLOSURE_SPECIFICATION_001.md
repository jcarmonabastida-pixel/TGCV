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

Deben distinguirse cuatro estados, sin inferencia entre ellos:
1. consentimiento conversacional para un alcance;
2. aprobación registrada por GitHub para un deployment/run;
3. validación técnica de la autorización y de la identidad del código;
4. permiso científico de ejecución para el alcance exacto.

El JSON no puede autoconceder el estado 2. El campo `approved_by=USER_EXPLICIT_APPROVAL` y un mensaje de commit no constituyen prueba independiente y deben dejar de actuar como gate suficiente.

### 4.2 Mecanismo exigido

El workflow que habilita G7 debe:
- ser iniciado mediante evento manual explícito (`workflow_dispatch`) en el snapshot exacto;
- declarar un GitHub Environment dedicado, p. ej. `c10s-f5-g7-tiera-v1-1`;
- exigir la aprobación de deployment del environment antes de ejecutar el job de holdout;
- comprobar que el environment existe y que su protección de reviewers está configurada; ausencia/no verificabilidad de la protección implica fail-closed;
- ligar el deployment aprobado al workflow run, SHA, protocol/architecture IDs, profile manifest digest, authorization ID, K/B/celdas, primary/replay y Tier-A;
- impedir que un push, un mensaje de commit o el propio workflow creen aprobación implícita.

La configuración de required reviewers es una protección de repositorio/environment administrada en GitHub Settings, fuera de los archivos versionados. El código puede exigir el environment, pero no puede afirmar que la protección está activa sin leer/verificar su configuración. La disponibilidad de un reviewer y la política de autoaprobación deben comprobarse en la configuración real antes de habilitar G7. No se declarará RG-04 cerrado solo por añadir `environment:` al YAML.

### 4.3 Consentimiento de un solo uso

El consentimiento conversacional previo se reconoce como consentimiento explícito al alcance que se presentó entonces; no es una prueba técnica almacenada por GitHub ni debe extenderse a un nuevo SHA, una nueva ventana o un nuevo intento. Para la siguiente ejecución G7, se requerirá aprobación humana registrada en el deployment del commit exacto. Tier-B y ejecución causal C10 permanecen excluidos.

### 4.4 Pruebas RG-04

- Tests estáticos: workflow_dispatch obligatorio; environment declarado; no existe ruta push que salte el environment; jobs científicos dependen del job protegido.
- Tests negativos: falta de environment, approval pendiente/rechazada, SHA distinto, manifest distinto, ventana expirada, scope ampliado.
- Prueba de configuración: consulta verificable de la protección real del environment; si el conector/API no puede leerla, estado NOT_VERIFIABLE y gate cerrado.

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
| RG-04 | Deployment approval de GitHub ligado al SHA/scope y protección real verificable | NOT_VERIFIABLE = gate cerrado |
| RG-05 | Inventario tipado único genera ambos manifests deterministas; negativos de drift | FAIL |
| RG-06 | Overhead medido o declarado como reserva; sensibilidad no excede presupuesto | CONDITIONAL si solo reserva |
| RG-07 | Extrapolación defendible o declarada condicional con límite de uso | CONDITIONAL; no afirmar garantía |

**Cierre del gate instrumental para G7:** RG-01…RG-05 deben estar PASS. RG-06/RG-07 deben tener evaluación documentada y la proyección debe satisfacer los límites bajo los escenarios aceptados. RG-04 NOT_VERIFIABLE bloquea toda ejecución. Un PASS de la suite determinista no reemplaza la verificación de la protección real del environment.

## 9. Preservación de gobernanza y alcance

- PR #119 permanece Draft.
- No modificar `main`, PR #116 ni Evidence→Claim Matrix/RMA.
- No modificar contratos científicos, DGP, estimandos, thresholds, seed bank ni adjudicador.
- No ejecutar G7, holdout, cobertura, bootstrap confirmatorio, replay científico ni Tier-A.
- No repetir el perfil resource-only existente.
- Cualquier nueva ejecución científica requiere aprobación de deployment verificable y confirmación de que el SHA y alcance coinciden exactamente con esta especificación.


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

El allowance de **300 s por fase** es una reserva de ingeniería, no una constante medida. Es aproximadamente 13,8 veces el mayor intervalo runner→cálculo observado en esta muestra. Con shard size 10 y el máximo observado de la celda lenta (418,194638 s/dataset), el job pareado primary+replay se proyecta en **8.963,893 s (149,398 min)**, solo **36,107 s** por debajo del presupuesto de 9.000 s.

| Reserva por fase | Job pareado lento | ¿Dentro de 9.000 s? |
|---:|---:|---|
| 300 s | 8.963,893 s (149,398 min) | Sí, margen 36,107 s |
| 600 s | 9.563,893 s (159,398 min) | No |
| 900 s | 10.163,893 s (169,398 min) | No |

**Estado RG-06: CONDITIONAL.** La reserva de 300 s está respaldada como holgada frente al setup observado, pero el margen final del job es estrecho y no existe una medición completa del workflow G7 consumidor. Los escenarios de 600/900 s invalidan el shard size 10 vigente. No se afirmará garantía temporal hasta medir el overhead del recorrido G7 o fijar y validar otra topología.

### 10.2 RG-07 — K=100 → K=1.000

Estadísticos guardados del artefacto (segundos por dataset):

| Celda | Media | P95 | P99 | Máximo |
|---|---:|---:|---:|---:|
| F5_beta22_M10_R5 | 0,372553 | 0,413426 | 7,674969 | 7,966772 |
| F5_beta22_M30_R20 | 208,420042 | 285,520522 | 356,961762 | 418,194638 |

El dimensionador usa el máximo observado para proyectar cada dataset de un shard size 10. Con dos celdas, 100 shards por celda (200 jobs), max-parallel=20 y un pool compartido, el trabajo agregado pareado conservador es 270,090 runner-hours. La cota de list scheduling de Graham es **57.131,839 s (15,870 h)** para primary+replay, bajo los tiempos asumidos; no es una cota probabilística de la duración real.

Con K=100 observaciones IID, la probabilidad de que el máximo muestral supere el verdadero P99 es 1−0,99^100 = 63,397 %; para el P95 es 1−0,95^100 = 99,408 %. Harían falta al menos **299 observaciones IID** para que el máximo muestral exceda el verdadero P99 con un 95 % de confianza. Aun así, eso acotaría un percentil, no el máximo futuro.

**Estado RG-07: CONDITIONAL.** K=100 no demuestra una cota de cola para K=1.000 ni un máximo futuro. La proyección de 15,870 h es una cota de scheduling condicionada a los tiempos observados y a la reserva de 300 s; no es garantía de duración. No se generará otro perfil para intentar cerrar esta limitación sin autorización expresa.

### 10.3 Límite de uso

RG-06 y RG-07 quedan evaluados con evidencia existente, pero no autorizan ejecución. RG-04 continúa bloqueante mientras la protección efectiva del GitHub Environment no pueda verificarse. El cierre técnico de RG-02/RG-05 queda pendiente del resultado de la suite determinista integrada sobre el HEAD final.