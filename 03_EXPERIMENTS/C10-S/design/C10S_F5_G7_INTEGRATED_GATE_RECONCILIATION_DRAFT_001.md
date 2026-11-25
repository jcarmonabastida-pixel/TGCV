# C10-S F5/G7 v1.1 — reconciliación integrada del gate instrumental

**Registro:** C10S-F5-G7-INTEGRATED-GATE-RECONCILIATION-001  
**Fecha:** 2026-11-25  
**Rama:** `research/c10s-f5-g7-canonical-mle-v1.1-20261122`  
**PR:** #119 (Draft; no integrado)  
**Commit de referencia auditado:** `5e02168b0073e59916c1a1944b22e35cb6905817`  
**Estado:** DOCUMENTARY RECONCILIATION / CORRECTIVE DESIGN PROPOSAL / NOT IMPLEMENTED / NOT AUTHORIZED FOR G7  
**Ámbito:** integración técnica del preflight F5/G7 v1.1. No reabre ni modifica el diseño causal C10-S, sus estimandos, DGP, outcomes, reglas de falsación o integración científica.

## 1. Dictamen ejecutivo

La secuencia de fallos no debe tratarse como una sucesión de defectos independientes. La inspección conjunta del artefacto de perfil, su workflow productor, el test de integración, el validador de perfil, el validador de autorización y el workflow consumidor identifica discrepancias de contrato entre componentes.

La causa estructural más inmediata del último fallo de `resource_preflight_validation` es una discrepancia de nombre de archivo:

- El workflow productor consolida y publica `c10s-f5-g7-resource-profile.json`.
- El test de perfil lee ese mismo miembro dentro del ZIP.
- El workflow consumidor busca `c10s-f5-g7-resource-parallel-profile.json`.

Por tanto, el consumidor no busca el nombre que realmente produce el productor y que utiliza el test. El test determinista puede pasar sin ejercitar el paso de descubrimiento real del workflow. Esta discrepancia basta para explicar que la validación falle antes de planificar la matriz; no implica que el perfil, el motor MLE o el cálculo de shards sean incorrectos.

La auditoría identifica además dos defectos de diseño de control que deben resolverse antes de cualquier ejecución: (i) el hash del archivo ZIP se comprueba en el test-fixture, pero no contra los bytes del artefacto descargado por el workflow productivo; y (ii) la autorización se representa mediante campos autodeclarados en un JSON y un mensaje de commit, que no prueban por sí mismos una aprobación explícita del usuario.

**Conclusión:** no se debe crear otra autorización ni disparar otro G7. Primero hay que reconciliar y probar el contrato integrado de extremo a extremo.

## 2. Fuentes y evidencia reconstruidas

Fuentes examinadas en el commit de referencia:

| Componente | Ruta |
|---|---|
| Arquitectura de ejecución | `03_EXPERIMENTS/C10-S/design/C10S_F5_G7_EXECUTION_ARCHITECTURE_002.md` |
| Protocolo Tier-A | `03_EXPERIMENTS/C10-S/design/C10S_F5_G7_TIERA_PROSPECTIVE_PROTOCOL_002.md` |
| Workflow productor del perfil | `.github/workflows/c10s-f5-g7-resource-profile.yml` |
| Script productor del perfil | `03_EXPERIMENTS/C10-S/harness/profile_c10s_f5_g7_resource_preflight_parallel.py` |
| Agregador del perfil | `03_EXPERIMENTS/C10-S/harness/aggregate_c10s_f5_g7_resource_shards.py` |
| Manifest del perfil | `03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/manifest.json` |
| Fixture ZIP del perfil | `03_EXPERIMENTS/C10-S/fixtures/g7_resource_profile_v1_1/profile_artifact.zip.b64` |
| Validador del perfil | `03_EXPERIMENTS/C10-S/harness/validate_c10s_f5_g7_resource_profile.py` |
| Tests del perfil | `03_EXPERIMENTS/C10-S/harness/test_c10s_f5_g7_resource_profile.py` |
| Validador de autorización | `03_EXPERIMENTS/C10-S/harness/validate_c10s_f5_g7_tiera_authorization.py` |
| Tests de autorización | `03_EXPERIMENTS/C10-S/harness/test_c10s_f5_g7_tiera_authorization.py` |
| Workflow consumidor G7 | `.github/workflows/c10-s-f5-g7-tiera-calibration.yml` |

Evidencia de ejecución relevante:

- Run `45365559253`: perfil resource-only finalizado; 20 shards y 200 mediciones, K=100 por celda y B=1.000. Artefacto de perfil `14908914198`; SHA-256 del ZIP declarado `14e317a6f38d9934dc0903b4b038da5ffc580c9bb076d26dbcc6e47cfe568e21`; SHA-256 del JSON `005ef265fa7dd8812c2572d9187cc7943c365506dc8e1169f1883487c0094d9f`. El manifest registra como fuente `8b62b89a78681cc39bdd4c0cbb76c43ef073c1e9`.
- El commit de perfil es ancestro del commit auditado `5e02168...` (comparación GitHub: `ahead`, base común igual al commit de perfil). La comparación entre ambos no muestra cambios en los doce archivos de la lista `PROFILE_SOURCE_PATHS`; sí muestra cambios en el validador/dimensionador, workflow y documentación, que no forman parte del compute path medido.
- Run `45479589765`: 7/7 jobs deterministas PASS. Esto acredita esa suite en el commit ejecutado, no el circuito de descarga/descubrimiento/validación real.
- Run `45517753203`: el job de autorización pasó; `resource_preflight_validation` falló; los jobs primario y de adjudicación no se ejecutaron. No se generó evidencia científica G7.

## 3. Matriz de contratos e interfaces

### 3.1 Productor → artefacto → consumidor

| Interfaz | Contrato observado | Dictamen |
|---|---|---|
| Productor → nombre del JSON | `c10s-f5-g7-resource-profile.json` | Definido por el workflow productor |
| ZIP fixture → miembro interno | `c10s-f5-g7-resource-profile.json` | Confirmado por el test |
| Consumidor → búsqueda del JSON | `c10s-f5-g7-resource-parallel-profile.json` | **FAIL: nombre incompatible** |
| Consumidor → manifest | `../fixtures/g7_resource_profile_v1_1/manifest.json` desde el directorio harness | Ruta coherente con el árbol |
| Consumidor → raíz Git | `--root ../../..` desde `03_EXPERIMENTS/C10-S/harness` | Resuelve al root del repositorio |
| Perfil → código fuente medido | Ancestro + comparación byte a byte de `PROFILE_SOURCE_PATHS` | Diseño adecuado; test actual simula Git y no prueba repositorio real |

El nombre del archivo debe tener una sola autoridad. No debe repetirse como literales independientes en productor, fixture, test y consumidor. El contrato de artefacto debe exponerlo desde un manifest/schema único o desde una constante importable que el workflow pueda consumir de forma inequívoca.

### 3.2 Integridad del artefacto

El test `test_shard_plan_uses_immutable_original_v1_1_profile_artifact_and_manifest` decodifica el ZIP fixture, verifica su SHA-256, extrae el JSON y comprueba el digest del JSON contra el manifest.

En producción, el workflow consumidor usa `actions/download-artifact`, que extrae el artefacto, y pasa el JSON extraído al validador. El validador comprueba que `profile_artifact_archive_sha256` tenga formato hexadecimal de 64 caracteres, pero no recibe ni calcula el hash de los bytes del ZIP descargado.

Por tanto:

- el test prueba el ZIP fixture almacenado en el repositorio;
- el workflow productivo prueba el JSON extraído y su digest;
- el log productivo del run `45517753203` acredita que `actions/download-artifact` calculó el digest `14e317a6…fe568e21` y lo comparó con el digest esperado por GitHub, coincidente con `profile_artifact_archive_sha256` del manifest. El workflow no compara explícitamente ese digest descargado con el campo del manifest; por ello RG-02 es una brecha de enlace explícito manifest-descarga, no ausencia total de verificación del ZIP.

Debe elegirse y materializarse una sola política:
1. descargar el archivo ZIP original, verificar su digest y después extraerlo; o
2. retirar el digest de archivo como afirmación de integridad y definir expresamente que la cadena de confianza se apoya en el ID inmutable del artefacto y el digest del JSON extraído.

No se debe mantener un hash de archivo que solo se valida en un test de fixture.

### 3.3 Identidad de fuente y hashes

El validador de perfil comprueba:

1. esquema, scope, namespace, K/B, celdas y denominadores;
2. digest del JSON frente al manifest;
3. que el commit fuente sea ancestro de HEAD;
4. igualdad byte a byte de los archivos declarados en `PROFILE_SOURCE_PATHS`.

Este control es conceptualmente correcto para la reutilización del perfil: una modificación del compute path invalida la medición. Sin embargo, la prueba principal sustituye las operaciones Git por mocks (`subprocess.run` y `subprocess.check_output`). No prueba un repositorio Git temporal real, el checkout de profundidad completa ni los fallos reales de ascendencia/archivo ausente.

El validador de autorización mantiene además un inventario manual `SOURCE_HASH_PATHS` con numerosos hashes en el JSON de autorización. Se solapan parcialmente las funciones de identidad del perfil y de identidad de la ejecución. Debe aclararse la distinción:

- **Compute-path identity:** archivos que determinan el coste/rendimiento medido y cuya igualdad permite reutilizar el perfil.
- **Execution-source identity:** todos los archivos, contratos, workflows, dependencias y fixtures que gobiernan la ejecución autorizada.

Ambos inventarios pueden ser distintos, pero deben derivarse de manifests versionados y no de listas paralelas mantenidas manualmente en distintos componentes.

### 3.4 Autorización y disparo del workflow

El validador exige `status=APPROVED`, `g7_tiera_calibration_authorized=true` y `approved_by=USER_EXPLICIT_APPROVAL`. El workflow se activa por un push al patrón de rama de autorización y comprueba que el mensaje de commit contenga la frase `Approve one-use C10-S F5 G7 TierA calibration`.

Estas condiciones validan el formato del registro y una convención de commit; no demuestran que el usuario haya emitido la aprobación. El valor `USER_EXPLICIT_APPROVAL` es texto autodeclarado por quien crea el JSON. El mensaje de commit también puede ser escrito por el propio operador. No hay una atestación independiente de actor/acción que conecte el consentimiento real con el alcance, el commit y la ventana de autorización.

El usuario había dado previamente una respuesta afirmativa explícita a una pregunta que delimitaba la ejecución G7 v1.1 (K=1.000 por celda, B=1.000, C0/C5, primary/replay y adjudicación Tier-A; Tier-B y ejecución causal C10 excluidas). Por tanto, sí existió consentimiento conversacional para ese alcance. Sin embargo, el workflow no conserva una atestación verificable de esa interacción: `approved_by=USER_EXPLICIT_APPROVAL` y el mensaje de commit no la acreditan por sí solos. Tampoco debe suponerse que cada nueva autorización técnica o reintento hereda automáticamente el consentimiento de un solo uso. El PASS del job de autorización en el run `45517753203` acredita únicamente la validación técnica del documento, no la trazabilidad independiente del consentimiento ni el paso de los demás gates.

La solución no es generar otro JSON con los mismos campos. El gate debe distinguir:
- aprobación humana explícita y registrada para el alcance exacto;
- validación técnica del registro y de la identidad del código;
- autorización de implementación;
- autorización de ejecución científica.

Ninguna de estas categorías debe inferirse de otra. El mecanismo de aprobación debe registrar un actor verificable y una acción explícita de aprobación (por ejemplo, un despacho manual protegido por el control de entorno/actor que el repositorio tenga configurado), y el workflow automático no debe autoconcederse aprobación a partir de un mensaje de commit.

### 3.5 Dimensionamiento y presupuesto temporal

La arquitectura y el validador coinciden en que cada job de matriz ejecuta primary y replay secuencialmente en el mismo runner, con un único pool `max-parallel: 20`. La fórmula implementada para planificación de lista de trabajos es:

`W/m + (1 - 1/m) × p_max`

donde `W` es el cómputo total estimado de todos los pares primary/replay, `m=20` y `p_max` es el mayor tiempo estimado de un par. La fórmula de Graham es una cota de planificación para tiempos de trabajo dados; no convierte por sí sola estimaciones empíricas de duración en límites físicos garantizados.

Dos supuestos necesitan trazabilidad antes de aceptar el plan:
- `JOB_SETUP_OVERHEAD_SECONDS=300` se añade a cada fase, pero no se ha documentado aquí una medición que demuestre que cubre checkout, instalación de dependencias, inicialización y overhead real del runner.
- `max` observado en K=100 por celda es el máximo de la muestra de perfil, no una cota estadística garantizada para los 1.000 datasets de G7.

El cálculo actual puede conservarse como **proyección condicional basada en el perfil observado**, no como garantía de que ningún job excederá el presupuesto. La decisión sobre margen, cuantiles, overhead y fallo seguro debe quedar explícita y preespecificada. No se debe volver a perfilar solo por esta observación: primero se debe comprobar si los registros existentes permiten estimar setup y variabilidad; si no, declarar la limitación y decidir si es material.

### 3.6 Alcance resource-only

La inspección del script `profile_c10s_f5_g7_resource_preflight_parallel.py` muestra que conserva tiempos por dataset, resumen por celda, tiempos de pared/CPU/RSS y la marca `coverage_adjudication=NOT_PERFORMED`. No he encontrado en ese script la variable `global_mle_certificate_status_counts` ni una lectura/retención de estados de certificado, intervalos o resultados de cobertura.

Por tanto, se retira la sospecha anterior de que ese script concreto estuviera reteniendo recuentos de certificados. La revisión de scope debe mantenerse, pero no debe registrarse ese hallazgo como defecto probado. El perfil existente declara `coverage_adjudication=NOT_PERFORMED`; no debe repetirse ni recalcularse por esta sospecha no confirmada.

## 4. Causas raíz agrupadas

| ID | Causa / discrepancia | Evidencia | Estado |
|---|---|---|---|
| RG-01 | Nombre de perfil distinto entre productor, fixture/test y consumidor | Rutas y literales de los workflows/tests | **CONFIRMADO; bloquea preflight** |
| RG-02 | Digest ZIP del manifest no enlazado explícitamente al digest que reporta la descarga productiva | `actions/download-artifact` verificó el digest del artefacto contra GitHub en run 45517753203; el workflow no compara ese valor con el campo del manifest | **CONDITIONAL; transporte verificado, enlace manifest-descarga no explícito** |
| RG-03 | Tests de Git simulan ascendencia y `git show` | Mocks en test de perfil | **CONFIRMADO; falta integración real** |
| RG-04 | Aprobación humana sin atestación independiente en el workflow | Consentimiento explícito conversacional existente; JSON y mensaje de commit no lo acreditan por sí solos | **CONFIRMADO; brecha de trazabilidad, no ausencia de consentimiento** |
| RG-05 | Inventarios de hash manuales y solapados | `SOURCE_HASH_PATHS` y `PROFILE_SOURCE_PATHS` | **CONFIRMADO; riesgo de deriva** |
| RG-06 | Overhead fijo de 300 s sin justificación de medición registrada | Constante del validador/test | **OPEN; supuesto no acreditado** |
| RG-07 | Máximo observado K=100 tratado como base de proyección para K=1.000 | Perfil y fórmula | **CONDICIONAL; límite de extrapolación** |
| RG-08 | Estado de certificados retenido por el perfilador | No aparece en el script inspeccionado | **NO CONFIRMADO; sospecha retirada** |

## 5. Contrato integrado de corrección

La corrección debe realizarse como una unidad coordinada, sin secuencia de parches y sin tocar el diseño causal:

1. **Contrato del artefacto:** un único nombre/ruta canónica, schema, manifest, ID de artefacto, run de origen, commit fuente, scope, digest JSON y, si se conserva, digest ZIP verificable.
2. **Productor/consumidor:** el workflow consumidor descarga exactamente el artefacto identificado, verifica su identidad e integridad y localiza el archivo por el contrato canónico. Si falta un elemento, falla antes de crear la matriz.
3. **Identidad de fuente:** manifests separados y explícitos para compute path y execution source, generados de forma determinista desde el commit; autorización enlazada al digest del manifest, no a una lista duplicada que deba actualizarse manualmente.
4. **Autorización:** separar validación de estructura de aprobación humana. El workflow no puede interpretar un string autodeclarado o un mensaje de commit como prueba suficiente de aprobación.
5. **Dimensionamiento:** conservar la fórmula de pool compartido; documentar el alcance condicional de la proyección y justificar setup/margen con evidencia disponible. No presentar una estimación como límite garantizado.
6. **Pruebas integradas:** usar un repositorio Git temporal real y el ZIP original como fixture. Comprobar productor→ZIP→manifest→descarga/extracción→validador→matriz; incluir casos negativos de nombre incorrecto, ZIP alterado, JSON alterado, artefacto/run no coincidente, commit no ancestro, archivo del compute path modificado, autorización ausente/caducada y aprobación no verificable.
7. **Workflow:** solo después de los gates anteriores, una acción humana explícita y verificable podrá habilitar la ejecución autorizada. Primary/replay y adjudicación permanecen detrás de ese gate.

No se crean nuevos contratos científicos ni nuevos estimandos. Las pruebas anteriores son pruebas de integración de software del gate instrumental; deben mapearse a los contratos existentes y no duplicar el Test Contract Register científico.

## 6. Orden de trabajo y criterios de cierre

### Fase 0 — preservar el estado

- Mantener PR #119 en Draft.
- No modificar `main`, PR #116 ni el diseño causal C10-S.
- No usar las ramas de autorización `...-006` o `...-007` ni sus runs como autorización válida.
- No repetir el perfil resource-only existente.

### Fase 1 — implementación coordinada en una sola revisión

Implementar conjuntamente RG-01…RG-05; resolver RG-06/RG-07 mediante evidencia disponible o registrar explícitamente la limitación. No hacer commits intermedios que disparen el workflow de G7.

### Fase 2 — validación técnica no científica

Ejecutar exclusivamente:
- compilación/importación;
- pruebas unitarias ya existentes;
- pruebas de integración real del repositorio/artefacto;
- pruebas negativas de los contratos;
- validación estática del workflow y de los gates.

No ejecutar K=1.000, bootstrap confirmatorio, cobertura, holdout, adjudicación Tier-A ni ninguna operación que inspeccione resultados científicos.

### Fase 3 — informe único de cierre

El informe deberá emitir por cada RG:
- requisito y fuente de autoridad;
- archivo/commit exacto;
- prueba ejecutada y resultado;
- evidencia persistida;
- limitación residual;
- estado PASS / FAIL / CONDITIONAL / NOT_VERIFIABLE.

El gate instrumental solo podrá declararse técnicamente conforme si todos los controles bloqueantes pasan y las limitaciones condicionales están aceptadas explícitamente. Eso no equivale a Design Freeze ni a autorización científica.

## 7. Estado de autorización y no-claims

`main` mantiene `experiment_authorization=NONE`. La arquitectura G7 v1.1 es un draft para validación determinista de software y declara expresamente que no autoriza holdout. El run `45517753203` no ejecutó primary/replay ni adjudicación.

Esta reconciliación:
- no autoriza G7;
- no autoriza Tier-B, holdout, cobertura o calibración;
- no modifica C10-S científico, D2, ITT-Z, θ_A, DGP, Value ni criterios de falsación;
- no cambia RMA, Evidence→Claim Matrix, STATUS, Core o `main`;
- no convierte los PASS técnicos previos en evidencia causal.

**Siguiente operación permitida:** implementar en una sola unidad la corrección del contrato instrumental y su suite de integración, exclusivamente en la rama de investigación, después de revisar esta reconciliación. La ejecución científica seguirá bloqueada hasta una aprobación explícita separada y vigente.
