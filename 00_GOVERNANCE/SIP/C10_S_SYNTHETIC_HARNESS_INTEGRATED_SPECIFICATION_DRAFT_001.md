# C10-S — Especificación integrada del harness sintético: contrato A–B–C

**ID:** C10-S-SYNTHETIC-HARNESS-SPEC-001  
**Versión:** 001  
**Fecha:** 2026-11-11  
**Estado:** A_B_C_RECONCILED / IMPLEMENTABLE_SPECIFICATION_CANDIDATE / FOCAL_IMPLEMENTATION_SLICE_001_PERSISTED / FULL_HARNESS_INCOMPLETE / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Precedencia:** decisiones aceptadas aplicables; PA–PE; contratos DGP temporal/roles, PD, B2–B3, operacionalización Outcome/Value, D2 assignment/population/support y U_G. Este documento integra interfaces y reglas; no sustituye las fuentes rectoras ni reabre decisiones aceptadas.

## 1. Dictamen y alcance

Esta especificación integra los cierres A (DGP/estimandos), B (observación/resultados/Analyzer/Evaluator) y C (datos/interfaces/control/reproducibilidad) para construir un **harness metodológico sintético**.

El harness debe permitir generar DGP con verdad conocida, producir evidencia observada imperfecta, analizarla sin acceso a la verdad reservada y evaluar después si el Analyzer recupera estimandos identificables, detecta límites de identificación y se abstiene cuando corresponde.

No es una especificación de una instancia confirmatoria material D2. Los bloqueos de roster real, IAM/C_SRC, snapshots materiales, inventario real de dependencias, aislamiento material y soporte empírico permanecen en ese carril separado. El Generator produce equivalentes sintéticos para probar métodos; no simula que sean observaciones reales.

**Resultado de la reconciliación:** los contratos lógicos y las reglas de comportamiento quedan integrados y suficientemente determinados para implementar un motor parametrizado. Las configuraciones numéricas de escenarios, la selección sustantiva de Outcome/Value y las decisiones materiales confirmatorias se suministran como configuración versionada o permanecen explícitamente no identificadas; no se rellenan por defecto.

## 2. Decisiones y contratos que se reutilizan sin reabrir

1. D2 es escenario primario candidato y D1 secundario; se conservan las políticas B_g0^D2/B_g1^D2 según DEC-C10-066/067. La asignación Z no se confunde con las reglas de política.
2. P*_{τ2} conserva precedencia primaria y P*_F es subpoblación secundaria; no se condiciona la población ITT a eventos post-Z.
3. Una UE tiene una B1; la identidad lógica del servicio es única/versionada por UE; una oportunidad estandarizada por UE en el probe primario. La UE=UA solo es admisible en escenarios sintéticos configurados como aislados; si hay recursos/actores/estado/canales compartidos, la asignación y la inferencia se hacen al nivel de clúster o mediante exposición explícita.
4. Need_preZ es basal, anterior a Z, con estados 1/0/?; la clase de propósito B1 aceptada es mantener operativa una función de servicio dependiente de la configuración migrada. La operación concreta sigue abierta; no se asigna Need=1 automáticamente.
5. Se mantienen separados Request_opportunity, Request_attempt, received, admitted/rejected, processing y response; sus relaciones con trajectory son TEMPORAL_ASSOCIATION, TRACEABILITY_LINK o CAUSAL_CONTRIBUTION. Las clases NECESSARY/ENABLING/MODIFYING no se infieren de temporalidad o coincidencia de IDs.
6. T_acc*=(U*,R*,C*,X*) y ΔT_acc* completo se preservan; A_f* es proyección/predicado focal y D_f* apertura basal→post. C_dep* mantiene sus componentes técnicos; intento, instalación, C_dep, A_f*, App_f, Reach, selección y ejecución no se colapsan.
7. F*, G, H, O-CONF y Value no se convierten en constantes confirmatorias por conveniencia. O-CONF es candidato no operacionalizado. Value es vectorial P179; no hay V_j seleccionada, escala, peso, agregación, autoridad o horizonte aprobados.
8. Generator, Proyector/Sealer, Analyzer, Evaluator/Adjudicator, Orquestador y Artifact/Provenance Store mantienen responsabilidades separadas. El Analyzer no recibe truth, potenciales, semillas secretas ni metadatos reveladores; el Evaluator accede a truth solo después del sellado de la salida del Analyzer.
9. DEC-C10-074/JCS se aplica exclusivamente al envelope U1 de UDG-01. No se generaliza a otros registros.
10. Se reutilizan S4R, MEAS, MISS, POL, VER, TRJ, INT, GEN, PM, SNAP, REACH, PROV, GC, U_G y P177/P178/P179/P182/P183. No se crean familias de tests paralelas.

## 3. A — Contrato generativo del DGP

### 3.1 Unidad, población y calendario

- Unidad lógica de generación: UE = instancia sintética completa.
- Unidad de asignación UA: UE en escenarios aislados; clúster en escenarios con recursos/actores/estado compartidos; o UE con mapa de exposición explícito si el escenario define interferencia.
- UO: observaciones repetidas de la UE; no incrementan N independiente.
- Una B1 por UE, una instancia de servicio por UE y una oportunidad estandarizada por UE en el núcleo primario.
- La población objetivo y la elegibilidad se generan exclusivamente con variables pre-Z. P*_{τ2} y P*_F se conservan como poblaciones distintas.
- Reloj principal: t−1 basal; t0 asignación; t1 política/provisión/intento; t2 estado técnico y dependencias; t3/t4 snapshot de accesibilidad/aplicabilidad; subledger de oportunidad y petición después del snapshot t3/t4; t5 consideración; t6 selección/inicio; t7 ejecución; t8 Outcome técnico; t9 consecuencia/Value. El subledger de petición no amplía el reloj ni la profundidad H.

### 3.2 Configuración de escenario obligatoria

Cada escenario DGP debe declarar, sin defaults silenciosos:

| Bloque de configuración | Parámetros obligatorios |
|---|---|
| Identidad | dgp_id/version, scenario_id/version, microdomain/version, contract versions |
| Población | regla pre-Z de elegibilidad, P* objetivo, definición de UA, roster sintético y composición de estratos |
| Asignación | mecanismo, probabilidades por estrato/unidad, algoritmo, semilla restringida, versión, unidad aleatorizada y regla para desviaciones |
| Política | D1/D2, brazo, policy_id/version, reglas de programación y política de control/tratamiento |
| Intento | probabilidades/mecanismos de cumplimiento, recepción, intento de fondo y sus dependencias con X/H/estrato |
| Provisión | distribución conjunta de C_install, C_integrity, C_compat y C_oper; no asumir independencia |
| Accesibilidad | predicados focales vigentes, condiciones basales/post, identidad/versionado τ2, reglas de agregación y NA/? |
| Transformación | estado basal/post, U/R/C/X, referencias/versiones, ΔT_acc, proyección focal A_f* y D_f* |
| Reach/trayectoria | catálogo de rutas, predicados, alternativas, G/H/ventanas, reglas de composición y cobertura |
| Petición B1 | oportunidad común, reglas de intento/recepción/admisión/procesamiento/respuesta, eventos de no transición y enlaces tipados |
| Resultado | constructos Outcome/Value que el escenario realmente instancia, regla generadora, horizonte y potenciales |
| Interferencia | aislamiento, clúster o mapa de exposición; carryover y versiones |
| Observación | cobertura, error, adjudicación, missingness, censura, selección y proceso de medición por variable/tiempo |
| Evaluación | estimandos, método/tolerancias, criterios de identificación/abstención y criterios de recuperación |

La ausencia de un parámetro obligatorio produce error de validación de configuración antes de generar datos. No se sustituye por una cifra ilustrativa.

### 3.3 Reglas generativas y orden causal

El Generator construye para cada UE una historia completa y coherente. La secuencia mínima es:

1. Generar exógenas basales X, H0, condiciones constitutivas y no constitutivas, necesidad/objetivo basal B1 y estado transformacional basal.
2. Determinar pertenencia a población y elegibilidad usando solo información pre-Z; registrar 1/0/? y el motivo.
3. Construir las políticas y comprobar factibilidad y soporte de ambos brazos para la población objetivo. La factibilidad de política no implica cumplimiento ni éxito.
4. Asignar Z mediante el mecanismo declarado. Registrar probabilidad de asignación, estrato, UA y semilla/versión en el ámbito restringido.
5. Generar política asignada/recibida, programación, intento efectivo y cualquier intento de fondo como variables distintas. En D2, las reglas de programación aceptadas distinguen Z=0 sin intento focal programado y Z=1 con provisión programada; el cumplimiento/recepción y el intento efectivo son mecanismos separados.
6. Generar el vector conjunto de resultados técnicos de provisión. C_dep*=C_install*∧C_integrity*∧C_compat*∧C_oper*. El patrón conjunto, no solo su marginal, es parte del truth.
7. Derivar A_f,post* aplicando los predicados focales y las condiciones no focales pertinentes conforme a los contratos vigentes. Derivar D_f*=I(A_f,base*=0 ∧ A_f,post*=1). No derivar A_f* directamente de W_attempt ni de C_dep* por sí solos.
8. Construir T_acc,base*, T_acc,post* y ΔT_acc* completo; registrar ΔValidity_e en E_T, no como componente de ΔT_acc. Calcular la proyección focal A_f* sin sustituir el espacio completo por el predicado.
9. Generar Reach_H y rutas con el catálogo/criterio/cobertura declarados. REACH=0 requiere universo exhaustivo; cobertura insuficiente produce ?.
10. Generar oportunidad y eventos del subledger B1, trayectorias y contribuciones potenciales por etapa. Temporalidad y trazabilidad no determinan contribución causal; esta procede de contraste contrafactual y propiedad preespecificada.
11. Generar conocimiento, consideración, selección, inicio, ejecución parcial/completa, Outcome técnico y consecuencia/Value en sus momentos separados. Se permiten vías directas y colaterales de política a Outcome/Value; no se impone mediación exclusiva.
12. Generar potenciales bajo los regímenes/intervenciones definidos por el escenario, tanto para la unidad asignada como para los contrastes requeridos por el estimando. El valor observado/realizado corresponde al régimen asignado; los potenciales no observados permanecen en truth_dgp.
13. Aplicar el proceso de observación al conjunto de eventos/estados generados, produciendo cobertura, error, missingness y censura sin modificar la verdad estructural.

### 3.4 Parámetros no fijados y prohibición de defaults

- Las cifras históricas D1/D2 de programación y s=.80 se conservan como antecedentes/candidatos dentro de sus límites. No son defaults ejecutables ni tasas empíricas.
- Las probabilidades de cumplimiento, intento de fondo y éxito conjunto de cuatro componentes deben estar explícitas en el escenario. Para la provisión, el vector de 16 patrones de cuatro componentes es la representación general; las restricciones sobre celdas/marginales deben declararse y validarse.
- El mecanismo de asignación, ratio, estratos, semilla, soporte y unidad de aleatorización son parámetros requeridos por escenario; no se inventan.
- F*, G, H, ventanas, rutas y tolerancias son parámetros tipados del escenario; no se importan candidatos históricos como constantes.
- Una configuración sintética puede fijar números para probar una propiedad matemática, siempre que estén etiquetados como fixture/metaparámetros sintéticos y no como valores confirmatorios o evidencia material.

### 3.5 Potenciales y estimandos

El DGP conserva, por unidad/cluster y escenario, potenciales coherentes bajo los regímenes necesarios. Para un resultado Y_j y horizonte h:

- **ITT de asignación:** diferencia de medias potenciales por asignación Z=1 frente a Z=0 en la población pre-Z objetivo. Estima el efecto total de asignar la política/paquete.
- **Primeras etapas:** contrastes separados de W_programmed, W_attempt, recepción, C_dep*, A_f*, D_f* y ΔT_acc*. Ninguna primera etapa sustituye a otra.
- **Efecto de política de accesibilidad θ_Af(q_X*):** solo se estima/atribuye si el escenario define políticas de accesibilidad coherentes, régimen común q_X*, factibilidad/positividad, medición y ausencia de vías colaterales no controladas. Si no, reportar efecto de paquete o NOT_IDENTIFIED.
- **LATE_f:** Wald solo si el DGP/escenario establece relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia y medición adecuada. Primera etapa nula: no calcular. Primera etapa débil: método robusto declarado o INDETERMINATE.
- **Mediación C4:** solo si existe intervención mediadora definida, orden temporal, historia y soporte longitudinal y estrategia para confusión mediador–resultado inducida por Z. No usar ajuste convencional ni calcular residual por resta.
- **θ_A(q) general:** no se identifica por el experimento focal τ2 sin una intervención sobre el espacio transformacional completo y sus relaciones.

La salida se emite por resultado/dimensión/horizonte. No se transfiere identificación entre Outcome y Value, entre dimensiones V_j, entre poblaciones ni entre D1 y D2.

## 4. B — Contrato de observación, Outcome/Value y análisis

### 4.1 Tres planos inmutables

1. `truth_dgp`: exógenas, reglas generativas, asignación verdadera, estados estructurales, potenciales, mecanismos, contribuciones verdaderas, Outcome/Value verdaderos y parámetros de escenario.
2. `observed_evidence`: únicamente registros y mediciones liberados al Analyzer, con fuente, versión, timestamp, cobertura, error, validez, missingness, censura y estado observado.
3. `evaluation_adjudication`: salida Analyzer sellada, truth abierto después del sellado, comparación y métricas de recuperación/error/abstención.

La proyección de truth a evidencia no puede alterar truth. El Analyzer no recibe potenciales, semillas, parámetros generadores, etiquetas de contribución causal ni metadatos que revelen el escenario. La segregación abarca contenido, IDs, nombres, orden, logs, errores, API y canales laterales.

### 4.2 Contrato genérico de resultado

Se define un contenedor de resultado tipado que no selecciona constructos sustantivos:

| Campo lógico | Regla |
|---|---|
| result_id | Identificador estable del resultado |
| construct_class | OUTCOME_TECHNICAL o VALUE_CONTEXTUAL |
| dimension_id | Obligatorio para una dimensión vectorial instanciada; no se inventa ni se rellena por defecto |
| unit_id / cluster_id | Unidad de asignación/análisis pertinente |
| horizon_id | Horizonte explícito del resultado |
| value_type / scale | Tipo y escala declarados por el escenario; no hay escala global implícita |
| truth_value | Solo truth_dgp |
| observed_value | Solo observed_evidence, opcional según observación |
| observation_status | OBSERVED / NOT_RECORDED / SOURCE_UNAVAILABLE / TECHNICAL_FAILURE / INVALID / CENSORED / STRUCTURALLY_UNDEFINED / NOT_INSTANTIATED |
| provenance_ref | Referencia tipada a fuente/medición/adjudicación |
| measurement_contract_id/version | Contrato que define regla, unidad, baseline y error |
| missingness_model_ref | Mecanismo de observación declarado, si aplica |

La clase OUTCOME_TECHNICAL no se confunde con consecuencia B1. VALUE_CONTEXTUAL requiere dimensión identificada, referente B1/Need_preZ, perspectiva/autoridad, criterio, escala, baseline, horizonte y regla de trade-offs. Si esos campos no existen, Value se marca NOT_INSTANTIATED; no se convierte en cero ni en missing ordinario.

O-CONF permanece candidato prioritario y no operacionalizado. Need_preZ conserva propósito basal aceptado pero la operación concreta y su truth por UE permanecen abiertos. Por tanto, el contrato genérico permite transportar resultados sintéticos tipados, pero no crea un endpoint confirmatorio Outcome/Value ni valida ΔT_acc→Value.

### 4.3 Proceso de observación

Para cada campo medible, el DGP declara:
- si es observado, por qué fuente y en qué momento;
- probabilidad/regla de cobertura y disponibilidad por brazo/escenario;
- mecanismo de error y validez;
- missingness MCAR/MAR/MNAR o mecanismo estructural equivalente, con parámetros explícitos;
- censura y su razón;
- reglas de adjudicación, cegamiento y desacuerdo.

Las categorías de ausencia no son intercambiables. NOT_INSTANTIATED no es missing; NOT_RECORDED no es 0; SOURCE_UNAVAILABLE no demuestra ausencia estructural; STRUCTURALLY_UNDEFINED no es un dato censurado. La falta de cobertura negativa suficiente produce ?.

### 4.4 Salida obligatoria del Analyzer

El Analyzer emite un registro por estimando × resultado/dimensión × población × horizonte:

| Campo | Contenido requerido |
|---|---|
| analysis_id, run_id, analyzer_version | Identidad y versión |
| estimand_id/version | Estimando exacto, sin inferirlo del nombre del resultado |
| result_id/dimension_id, population_id, horizon_id | Objeto y ámbito |
| identification_status | IDENTIFIED / PARTIALLY_IDENTIFIED / NOT_IDENTIFIED / INDETERMINATE |
| estimand_scope | POLICY_PACKAGE / FOCAL_ACCESSIBILITY / LOCAL_COMPLIER / INTERVENTIONAL_MEDIATION / OTHER_DECLARED |
| estimate, standard_error, interval | Solo cuando el estatus y método lo permiten |
| assumptions | Supuestos necesarios y dictamen de cada uno |
| support_diagnostics | Positividad, overlap, factibilidad, clúster/exposición y versiones |
| measurement_diagnostics | Cobertura, error, invariancia, missingness y censura |
| sensitivity | Análisis/cotas solo si sus restricciones están declaradas |
| abstention_reason | Código y explicación cuando no hay estimación admisible |
| input_manifest_ref, output_hash | Trazabilidad y sellado |

Reglas:
- El ITT conserva toda la población aleatorizada; no se filtra por Request, cumplimiento, accesibilidad post-Z, selección, ejecución o disponibilidad observada del resultado.
- Un ITT identificable de política no se etiqueta como efecto focal de accesibilidad si hay vías directas/colaterales.
- No se emite Wald/LATE si falla relevancia, exclusión, monotonicidad, consistencia, no interferencia o medición.
- No se emite mediación C4 sin intervención mediadora y estrategia longitudinal defendible.
- No se calcula efecto directo/residual por resta de estimandos incompatibles.
- Un dictamen correcto de no-identificación/indeterminación cuenta como recuperación correcta, no como fallo del Analyzer.

### 4.5 Evaluator y criterio de recuperación

El Evaluator abre truth solo tras el sellado de la salida Analyzer. Compara por escenario y estimando:
- sesgo/RMSE/cobertura y tolerancia numérica declarada;
- recuperación de signo, orden, interacción o clasificación estructural cuando aplique;
- clasificación correcta IDENTIFIED / PARTIALLY_IDENTIFIED / NOT_IDENTIFIED / INDETERMINATE;
- falsos positivos/negativos y tasas de abstención;
- detección de vías directas/colaterales, interferencia, falta de soporte, observación diferencial y fallos de medición;
- fuga de truth, integridad, reproducibilidad y completitud de provenance.

Los valores de tolerancia, niveles de confianza, MDE, N, R y error Monte Carlo son parámetros del contrato de evaluación versionado; no se fijan por conveniencia ni se heredan de cifras ilustrativas. La configuración debe validarlos antes de la ejecución.

## 5. C — Contrato lógico de datos, interfaces y control

### 5.1 Objetos de intercambio

Los componentes intercambian artefactos versionados e inmutables. Se definen los siguientes tipos lógicos; la implementación puede mapearlos a registros/objetos internos sin alterar campos ni semántica:

1. `RunManifest`: run_id, test_id/version, dgp_id/version, scenario_id/version, commit/component versions, configuration refs, randomization ref, seed commitment/restricted ref, timestamps y provenance.
2. `UnitRoster`: unit_id (UE), assignment_unit_id (UA o cluster_id), beneficiary_id (B1), service contract/instance IDs y versiones, population/eligibility status pre-Z.
3. `AssignmentLedger`: assignment_id, unit/cluster, Z, policy_id/version, assignment probability, stratum, randomization mechanism/version y t0.
4. `EventLedger`: event_id, unit_id, event_type, event_time, causal_time_key, stage_key cuando corresponda, actor/source, object/version refs, observed state y provenance. Request subledger conserva los tipos de evento y enlaces aceptados.
5. `SnapshotBundle`: snapshot_id, snapshot_object_record_id, object_record_id/version, unit, time/phase, exact object references, coverage and evidence refs.
6. `TruthBundle`: potential outcomes/states, DGP parameters, hidden causal labels, randomization internals/seed and provenance. Acceso restringido a Generator y Evaluator bajo secuencia de sellado.
7. `ObservedEvidenceBundle`: registros observables, valores medidos, referencias, cobertura, validez, ausencia, censura y hashes; nunca truth reservado.
8. `AnalyzerResult`: registros por estimando/resultado conforme §4.4, sellados e inmutables antes de evaluación.
9. `EvaluationReport`: truth ref, AnalyzerResult hash, métricas, clasificación de recuperación, fallos de firewall y adjudicación.

Las identidades existentes TID/SID/RID/EID, object_record_id/version, snapshot_id + snapshot_object_record_id, request_id/trajectory_id, evidence_id y referencias U_G se reutilizan. No se sustituyen por aliases ni se colapsan. Los objetos nuevos de intercambio son tipos de bundle, no nuevos IDs científicos ni una nueva ontología de nodos.

### 5.2 Interfaces de componente

| Interfaz | Entrada | Salida | Precondición / error fail-closed |
|---|---|---|---|
| Orchestrator.prepare_run | Test/DGP/scenario contract, autorización y versiones | RunManifest | Rechazar contrato no versionado, configuración incompleta o falta de autorización para la operación |
| Generator.generate | RunManifest + DGP config | TruthBundle + generated event/state source | Rechazar parámetros inválidos, potenciales incoherentes o soporte no declarado |
| Projector.project | Generated source + observation config | ObservedEvidenceBundle candidate | Rechazar mapping desconocido, ausencia de provenance o fuga de campos reservados |
| Sealer.seal | Candidate bundle + firewall/integrity rules | Sealed ObservedEvidenceBundle + manifest/hash | Rechazar fuga, integridad inválida o inputs no reproducibles |
| Analyzer.analyze | Sealed ObservedEvidenceBundle + visible analysis contract | AnalyzerResult | No permitir lectura de TruthBundle; emitir abstención estructurada si no identifica |
| Evaluator.evaluate | TruthBundle + sealed AnalyzerResult + evaluation contract | EvaluationReport | Rechazar AnalyzerResult no sellado, hash discrepante o truth no correspondiente al mismo run |
| Store.persist | Versioned artifact + provenance | Immutable reference | Rechazar sobrescritura, referencias huérfanas o identidad flotante |

### 5.3 Identidad, temporalidad y estados

- Todo artefacto tiene identidad, versión, tipo, provenance y referencias explícitas.
- Snapshots se resuelven por identidad exacta, nunca por “latest”.
- Reloj t−1/t0…t9, stage_key, phase y subledger de petición permanecen distintos.
- Estados 1/0/? y estados de observación/cobertura/adjudicación se almacenan en campos separados. No se colapsa ausencia en cero.
- Referencias tipadas se validan; no se infieren relaciones por nombre o proximidad temporal.
- Las versiones asignadas, recibidas y aplicadas se conservan separadas; crossover no se borra.

### 5.4 Serialización y canonicalización

La semántica de los objetos de intercambio queda fijada en esta especificación; el formato físico y canonicalización se aplican por perfil de objeto. JCS/RFC8785 solo para UDG-01/U1 según DEC-C10-074. Para los demás objetos, el contrato exige serialización determinista definida por el perfil de implementación, versionado del perfil, bytes/codificación declarados y hash sobre bytes exactos. No se generaliza JCS ni se declara hash antes de definir la serialización concreta.

### 5.5 Roles y firewall verificable

- Generator: crea y conserva truth; no puede alterar salida sellada del Analyzer.
- Projector/Sealer: transforma mediciones en evidencia observable; no lee ni publica potenciales/etiquetas reservadas; no adjudica causalidad.
- Analyzer: acceso solo al bundle observado y contratos visibles; no accede a truth, semilla secreta, parámetros ocultos, potenciales o evaluación.
- Evaluator: acceso a truth solo después del sello del Analyzer; no modifica el resultado analítico.
- Orchestrator: controla secuencia y referencias; no actúa como canal de lectura del Analyzer hacia truth.
- Store: aplica separación de namespaces/permisos y registro de accesos.

La aceptación del contrato lógico no prueba seguridad. Antes de una ejecución, G-ROLE requiere threat model, permisos efectivos, separación de almacenamiento, prueba negativa de acceso, pruebas de canales laterales y logs verificables. Los secretos no se almacenan en GitHub ni en el bundle del Analyzer.

### 5.6 Reproducibilidad

Un run se identifica por commit, versiones de componentes, contrato DGP, escenario, configuración, mecanismo/semilla, roster sintético, inputs y manifiestos. Se preservan los artefactos exactos de Generator, ObservedEvidenceBundle sellado, AnalyzerResult sellado y EvaluationReport. La repetición usa las mismas identidades y configuración; cualquier cambio produce nueva versión/run, no sobrescritura.

## 6. Contrato de prueba y aceptación del harness

Se reutilizan IDs existentes; cada test contract debe apuntar a entradas, escenario, truth, salida esperada, aserciones, tolerancias, códigos de fallo y artefactos. La cobertura mínima se organiza en los escenarios adversariales PD: aislado focal, nulo, fallo parcial, adverso, vía directa, colateral, interacción, heterogeneidad, IV nulo/débil/defiers/exclusión violada, interferencia, crossover/versionado, alternativas, observación diferencial, contribuciones múltiples, falta de soporte, MCAR/MAR/MNAR y censura.

Las capas de verificación son:
- contrato/configuración y validación de tipos;
- integridad referencial y temporal;
- derivación C_dep/A_f*/D_f*/ΔT_acc*/Reach;
- no filtración de truth y sellado;
- estimandos e identificación/abstención;
- observación/missingness/censura;
- evaluación contra truth;
- reproducibilidad y replay.

Un test solo se declara PASS después de implementación y ejecución con artefactos verificables. Esta especificación no registra ningún PASS técnico o científico.

## 7. Decisiones irreducibles que siguen fuera del cierre genérico

Estas cuestiones no se rellenan artificialmente. Se mantienen abiertas para una futura **instancia confirmatoria sustantiva**, no para impedir la construcción del motor parametrizado:

1. Operación concreta del servicio B1 y adjudicación material de Need_preZ por UE.
2. Ficha confirmatoria completa de O-CONF u otro O_k: predicados, evento terminal, fuente/oráculo, ventana, validez/error y adjudicación.
3. Perspectiva/autoridad, criterio, dimensiones V_j, escalas, baseline, horizonte y trade-offs de Value.
4. Parámetros materiales D2: asignación real, roster, q_X*, positividad/soporte, IAM/C_SRC, snapshots, grafo de dependencias, aislamiento/cluster, provisión y vías colaterales.
5. Decisiones numéricas por escenario sintético: probabilidades de cumplimiento/intento/fallo, distribuciones conjuntas, efectos/interacciones, observación, tolerancias, N/R y potencia. Son entradas versionadas de escenarios/fixtures, no constantes del motor.
6. Perfil físico concreto de serialización/almacenamiento y tecnología de despliegue. El contrato lógico no selecciona stack; el mapeo físico debe respetar íntegramente los objetos y permisos definidos aquí.

**Regla:** ningún elemento de esta lista se convierte en un bloqueo genérico del harness si puede recibirse como configuración tipada. Si el motor necesita una semántica no definida para ejecutar un estimando concreto, ese estimando devuelve NOT_IDENTIFIED/NOT_INSTANTIATED o queda deshabilitado; no se inventa semántica.

## 8. Relectura final de los gates PE

| Gate | Harness sintético | Confirmación material D2 |
|---|---|---|
| G-SCI | Contrato generativo, potenciales, escenarios y reglas de estimación/abstención de §§3–4 | Constructos/estimandos/medición materialmente defendibles |
| G-MAT | Roster, asignación, dependencias y truth generados y versionados sintéticamente | IAM/C_SRC, snapshots, inventario, aislamiento y soporte reales |
| G-SCHEMA | Tipos lógicos, campos, referencias, cardinalidades y validadores según §5 | Crosswalk físico/material y mappings |
| G-ROLE | Permisos efectivos y pruebas de firewall para el entorno de harness | Custodia/seguridad del entorno material |
| G-TEST | Fixtures, oráculos, tolerancias y abstención definidos por test contract | Validez y cobertura de medición confirmatoria |
| G-REPRO | Versiones, configuración, semilla, manifiestos, hashes y replay del harness | Provenance de inputs materiales |
| G-AUTH | Autorización específica para implementar/ejecutar el harness | Autorización para captura/implementación/ejecución material |

## 9. Criterio de salida y estado

Una persona técnica puede construir el motor parametrizado con los contratos de componentes, artefactos, campos lógicos, orden generativo, separación de roles, reglas de estimación/abstención y evaluación especificados aquí. Los escenarios concretos se suministran como configuraciones versionadas; los resultados no operacionalizados permanecen explícitamente no instanciados.

**Estado de esta iteración:** A–B–C permanece reconciliado documentalmente como especificación del motor/harness parametrizado. Se ha persistido una primera porción de implementación focal para la instancia sintética B1 en `03_EXPERIMENTS/C10-S/harness/`; no equivale al harness completo y sus pruebas aún no se han ejecutado. No se afirma que un escenario confirmatorio D2 esté congelado, que el Value general esté operacionalizado, que los efectos de accesibilidad estén identificados ni que exista validación técnica/científica.

**No autorizado por este documento:** Design Freeze; modificación de main/Core/RMA/Matrix/STATUS/claims; creación/materialización de fixtures o datos; código/parser/validator; simulación, estimación, replay o ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

## 10. Fuentes rectoras integradas

- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`
- `C10_S_BASE_DGP_SCOPE_AND_ABSTRACT_CONFIGURATION_CONTRACT_PROPOSAL_DRAFT_001.md`
- `C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md`
- `C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md`
- `C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md`
- `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`
- `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md`
- `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md`
- `C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md`
- `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`
- `C10_S_IMPLEMENTABILITY_BOUNDARY_AND_MINIMUM_SPEC_RECONCILIATION_DRAFT_001.md`
- `C10_S_CLOSURE_SEQUENCE_AND_C1_ITT_WORKPLAN_001.md`
