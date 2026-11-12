# C10-S — Reconciliación integrada de factibilidad confirmatoria y condiciones de Design Freeze

**ID:** C10-S-FEASIBILITY-DF-001  
**Fecha:** 2026-11-11  
**Estado:** INTEGRATED_RECONCILIATION_COMPLETED / CONFIRMATORY_FEASIBILITY_NOT_ESTABLISHED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED  
**Rama:** research/c10-s-consolidation-draft · **PR:** #116 (Draft)  
**Precedencia:** gobernanza canónica main; decisiones aceptadas dentro de su alcance; C10-D1; contratos PA–PE, PB-MAT y B2–B3 recuperables.  
**Naturaleza:** síntesis documental derivada; no crea decisiones científicas, no sustituye contratos fuente y no autoriza captura ni ejecución.

## 1. Dictamen ejecutivo

Se completa en una sola reconciliación la evaluación conjunta de factibilidad confirmatoria que quedó activa tras PA–PE, PB-MAT y B2–B3.

**Dictamen global: NO EXISTE AÚN UN DISEÑO CONFIRMATORIO MATERIALMENTE IDENTIFICADO NI LISTO PARA DESIGN FREEZE.** La arquitectura conceptual y varios contratos lógicos están suficientemente desarrollados para especificar qué habría que identificar y probar, pero faltan datos de diseño y evidencia material indispensables: mecanismo de asignación D2, roster/IAM y snapshots por UE, aislamiento e interferencia, materialización de la provisión, medición completa de Outcome y Value, soporte y parámetros conjuntos del DGP.

No se convierte ninguna ausencia en supuesto favorable. Los resultados correctos son, según el estimando, OPEN, NOT IDENTIFIED, NOT EVALUABLE o CONDITIONAL; no PASS.

Esta conclusión no invalida los cierres documentales anteriores ni reabre decisiones aceptadas. D2 sigue siendo el escenario primario candidato y D1 el secundario; P*τ2 sigue siendo la población primaria candidata y P*_F la subpoblación secundaria; una B1 y una oportunidad estandarizada por UE siguen aceptadas dentro de su alcance. Ninguna de esas decisiones demuestra que el diseño material exista o sea identificable.

## 2. Fuentes históricas reutilizadas y límites de esta reconciliación

Se reutilizan sin recreación:
- PA / C1 ITT D2, crosswalk de elegibilidad basal, precedencia P*τ2/P*_F y regla trivalente pre-Z.
- PB / PB-MAT: DEC-C10-066/067, DEC-C10-095, identidad B1 por UE, instancia lógica de servicio por UE, IAM/U_G, B-M01…15, PROV-01…12, snapshots y alternativas A1/A2.
- PC: separación ITT de política, efecto de accesibilidad θ_A(q), efecto focal θ_Af(q_X*) y mediación interventional C4.
- PD: DGP temporal, mecanismos C5, contrafactuales por etapa, escenarios adversariales, P177/P178/P179/P182/P183.
- PE: arquitectura de responsabilidades, truth/evidence/evaluation, identidades, provenance, snapshots y gates G-SCI/G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO/G-AUTH.
- B2–B3: B1/Need_preZ, Outcome técnico, consecuencia y Value contextual; P179 vectorial y fichas §224.

**Nota histórica corregida por §13:** la lectura Contents devolvía contenido vacío, pero el blob Git original (SHA 61d3079213558f6f74c14b60600ae3ca04c0a395) se recuperó íntegramente. Se inspeccionaron §§266–273 y se incorporó §274. La reconciliación de esta síntesis se contrastó con el maestro recuperado; no se realizó validación local ni CI. La incidencia de recuperación está resuelta y no es gate pendiente.

## 3. Asignación D2, probabilidades y soporte

### 3.1 Qué está decidido y qué no

- D2 es el escenario primario candidato; D1 permanece como contraste incremental secundario.
- En D2, los objetivos candidatos de política son P(W_attempt=1|Z=0)=0 y P(W_attempt=1|Z=1)=1; el éxito técnico conjunto condicional a intento se ha propuesto como 0.80, produciendo C_dep,post candidato 0/0.80.
- En D1, los objetivos históricos candidatos son 0.25/1 para intento y 0.20/0.80 para C_dep,post.
- Estos números son parámetros candidatos del DGP, no probabilidades empíricas observadas ni una especificación confirmatoria validada. El 0.80 es éxito conjunto condicional, no cuatro probabilidades independientes.
- La asignación aleatoria Z está prevista conceptualmente, pero no se ha recuperado un contrato material que fije ratio/probabilidades de asignación, estratos/bloques, nivel de asignación, algoritmo, semilla/hash, versionado, reproducibilidad y gestión de desviaciones.

No se presume asignación 1:1 ni se confunde la probabilidad de recibir/probar B con la probabilidad de asignación Z.

### 3.2 Soporte

q_X*, q_L*, positividad y soporte por historia/estrato no están materializados. La factibilidad de ambas políticas para cada historia y la existencia de unidades que puedan recibir los dos regímenes no se han verificado. El soporte debe comprobarse por política, población, resultado, dimensión e historia relevante; no basta con que cada brazo tenga observaciones agregadas.

**Dictamen:** asignación y probabilidades D2 = arquitectura aceptada, mecanismo no especificado; parámetros de entrega = candidatos; soporte = OPEN/NOT ASSESSED. No se puede calcular una primera etapa ni un efecto causal confirmatorio con la información actual.

## 4. Unidad experimental, asignación e interferencia

La UE es la instancia sintética completa. UA es la unidad a la que se asigna Z; UO son observaciones repetidas/anidadas y no incrementan el número de unidades independientes. La igualdad UE=UA es condicional a aislamiento efectivo.

Se reutilizan las decisiones de una B1 por UE, una instancia lógica de servicio única/versionada por UE y una oportunidad estandarizada por UE. Son decisiones de identidad y arquitectura, no evidencia de independencia.

No hay roster material final, IDs por UE, IAM/ACL efectiva, inventario de recursos compartidos, dependencias transitivas, agentes/canales compartidos ni pruebas de interferencia. Por ello:
- SUTVA/no interferencia no puede darse por satisfecha.
- No se puede declarar que UE=UA sea válido.
- Si existen dependencias compartidas, la unidad de asignación/análisis puede necesitar ser un clúster o un estimando de exposición/interferencia.
- No debe tratarse cada oportunidad, petición, trayectoria o medición repetida como una unidad independiente.

**Dictamen:** unidad lógica definida; unidad efectiva de asignación e inferencia CONDITIONAL; aislamiento y ausencia de interferencia NOT DEMONSTRATED.

## 5. IAM, snapshots, provisión y materialización D2

PB-MAT identifica una carencia material, no una laguna que pueda resolverse por estipulación:

| Dominio | Estado recuperado | Consecuencia |
|---|---|---|
| Roster e IDs de UE/B1/servicio | No materializados | No hay población/identidad material adjudicable |
| C_SRC e IAM pre-Z | NONE | No se puede cerrar E_i ni demostrar condiciones basales |
| Snapshots exactos pre-Z, post-provisión, post-instalación y rollback | No capturados | No se adjudican C_dep*, A_f*, D_f* ni comparabilidad |
| Artefacto/runtime/version/hash de B | No inventariado | Tratamiento material no fijado |
| Actor, recepción, ventana, reintentos, fallos y rollback | OPEN | Exposición y cumplimiento no observables bajo contrato cerrado |
| Grafo transitivo y consumidores | No materializado | No se conoce la frontera de dependencia ni las vías colaterales |
| ACL, recursos, cuotas y estado compartido | No medidos | Aislamiento y no-afectación no probados |
| A1/A2 y F2 | No-afectación no demostrada | No se puede sostener ausencia de rutas colaterales |
| Cobertura de alternativas | No adjudicada | F_alt=0 y exclusividad funcional no demostrables |

B-M01…M12/M15 permanecen NO INVENTARIADO cuando falta evidencia; B-M13 (F*/oráculo) y B-M14 (A1/A2) son superficies que B no debe modificar. ARCH-B1 sidecar sigue siendo recomendación para evaluar, no arquitectura aprobada ni instalada. UNKNOWN/NO INVENTARIADO no equivale a 0 ni a invariancia.

Los estados de la cadena Z→B→W_attempt/recepción→S_install→C_install/C_integrity/C_compat/C_oper→C_dep*→A_f*→D_f*→ΔT_acc* deben observarse y adjudicarse separadamente. C_dep* no sustituye A_f*; intento, recepción e instalación no sustituyen C_dep*; D_f* no sustituye ΔT_acc* completo.

**Dictamen:** G-MAT BLOCKED. No existe evidencia para afirmar primera etapa focal, tratamiento recibido limpio, ausencia de contaminación/crossover, invariancia de alternativas o aislamiento.

## 6. Factibilidad de Outcome y Value

### 6.1 Outcome técnico

O-CONF es el candidato con mejor anclaje conceptual en F*/FP-01…08. No está operacionalizado: faltan predicados, mapping, tolerancias justificadas, oráculo independiente/cego, snapshots, cobertura, unidad, ventana, baseline, regla terminal y adjudicación. O-MIG, O-SVC, O-REC y O-BUR tampoco tienen fichas §224 completas.

No se debe congelar O-CONF como Outcome primario solo por ser el candidato más desarrollado. La selección exige criterio técnico y ficha completa ex ante, y debe mantener Outcome separado de F*, accesibilidad, ejecución y Value.

### 6.2 Value contextual

B1 es el referente sintético solicitante-beneficiario; Need_preZ antecede a Z y no se infiere de la solicitud. La identidad lógica por UE y la oportunidad única están aceptadas, pero contenido/medición de Need_preZ, instancia/provenance material B1, consecuencia, perspectiva y autoridad de valoración siguen OPEN.

P179 recomienda preservar Value como vector durante identificación y los trade-offs entre dimensiones. Las cinco dimensiones históricas no son lista aprobada ni exhaustiva; no se eligen dimensiones, indicadores, escalas, pesos o agregación por defecto. Cada V_j requiere ficha §224 propia, con fuente, unidad, escala, baseline, horizonte, criterio, validez, fiabilidad, error, adjudicación, ausencia/censura y provenance.

### 6.3 Relación Outcome–Value

Outcome y Value son constructos distintos. No se impone Outcome→Value exclusivo ni V_j=f(Outcome). La consecuencia valorada puede depender de Outcome y de otras circunstancias o vías directas/colaterales de la política. La estructura causal concreta debe estar en el DGP y ser evaluada, no codificada en la definición de Value.

Por tanto, un ITT sobre Outcome no identifica un ITT sobre Value; la identificación de una dimensión V_j no se transfiere a otra; y una mejora técnica no implica automáticamente valor positivo para B1.

**Dictamen:** Outcome = constructo separado, no operacionalizado; Value = no instanciado; no existe actualmente ningún Y_j confirmatorio completo para C1.

## 7. Matriz de identificación por estimando y resultado

| Estimando/objeto | Qué requeriría | Dictamen con el estado actual |
|---|---|---|
| ITT_Z^D2(C_dep*) | Asignación D2 verificable, población, medida técnica y seguimiento | No estimable: asignación material e IAM/snapshots ausentes |
| ITT_Z^D2(A_f*, D_f*, ΔT_acc*) | Lo anterior + predicados, evidencia independiente y snapshots comparables | No identificado/evaluable en el D2 material actual |
| ITT_Z^D2(Reach/Π) | Universo de rutas, reglas, cobertura, medición y horizonte | No evaluable materialmente; contratos lógicos no sustituyen datos |
| ITT_Z^D2(O_k) | Asignación, población, horizonte y ficha §224 completa de O_k | No estimando confirmatorio completo: ninguna ficha O está completa |
| ITT_Z^D2(V_j) | Lo anterior + B1, Need_preZ, perspectiva/autoridad y ficha §224 de V_j | No estimando confirmatorio completo: Value no instanciado |
| Efecto de política/paquete ψ_policy | Asignación válida y resultado medido; incluye todas las vías inducidas por Z | Conceptualmente es la interpretación primaria del ITT, pero no estimable ahora por ausencia de asignación y resultado medido |
| θ_A(q;Y) — efecto total de accesibilidad | Intervención/regímenes de accesibilidad definidos, mapping D2→g, régimen q común, soporte/positividad, consistencia, medición y control/identificación de vías alternativas | NOT IDENTIFIED |
| θ_Af(q_X*;Y) — efecto focal | Mapping de política a apertura focal D_f*, medida válida, soporte común, ausencia/identificación de colaterales y supuestos de atribución | NOT IDENTIFIED |
| LATE_f por Wald | IV relevante y válido: asignación, primera etapa focal, independencia, exclusión, monotonicidad, consistencia, no interferencia y medida sin error no modelado | NOT IDENTIFIED; no usar C_dep* ni s=.80 como primera etapa focal |
| IIE C4 sobre ΔT_acc* | DAG longitudinal, intervención mediadora bien definida, confusión mediador–resultado tratada, soporte secuencial, medidas y sensibilidad | NOT IDENTIFIED / NOT EVALUABLE |
| Efecto directo/residual | Descomposición causal compatible con estimandos y supuestos, no resta ad hoc | No definido ni identificado |
| Efectos por dimensión y heterogeneidad | Fichas por dimensión, soporte por estrato, composición de compliers y precisión | No evaluables actualmente |

### 7.1 Efecto total, mediado y residual: no confundir

1. El ITT de Z, cuando llegue a ser identificable, será el efecto total de asignación a la política D2 sobre el resultado declarado. Si B activa otras vías, la interpretación es efecto de paquete.
2. El efecto de accesibilidad requiere un contraste de intervenciones/regímenes de accesibilidad y condiciones de atribución propias; no es sinónimo del ITT de Z.
3. El efecto indirecto interventional C4 requiere una intervención sobre la distribución del mediador y supuestos longitudinales explícitos. No se identifica por ajustar una regresión convencional por el mediador.
4. El residual/directo no se obtiene restando un efecto mediado de un ITT salvo que ambos pertenezcan a una descomposición formal compatible y se sostengan sus supuestos.
5. Los resultados y dimensiones se dictaminan separadamente. No hay transferencia automática entre Outcome y Value ni entre dimensiones V_j.

## 8. Qué puede identificarse, acotarse o debe quedar no identificado

### 8.1 Identificado ahora

- Decisiones y contratos lógicos dentro de su alcance explícito: D2 primario candidato/D1 secundario; precedencia P*τ2/P*_F; una B1 por UE; una oportunidad por UE; identidad lógica de servicio por UE; separación conceptual Outcome/Value; arquitectura de estimandos y estados trivalentes.
- Reconciliación documental de PA–PE, PB-MAT y B2–B3 en el alcance de los artefactos recuperados.

Esto es identificación documental/semántica, no identificación causal ni material.

### 8.2 Potencialmente identificable en un diseño futuro, sujeto a gates

- ITT de asignación por resultado/dimensión si se fija la aleatorización, población, unidad/interferencia, horizonte y medición válida.
- Primeras etapas de C_dep*, A_f*, D_f* y ΔT_acc* si se capturan snapshots y evidencia independiente por etapa.
- LATE_f solo si los supuestos IV se justifican y las amenazas de exclusión, monotonicidad, contaminación e interferencia se resuelven o modelan.
- θ_A/θ_Af y C4 solo si las intervenciones, mappings, soporte, confusión y vías colaterales se hacen identificables.

### 8.3 Cotable o parcialmente identificable

En principio, cotas/sensibilidad pueden ser útiles para:
- elegibilidad basal con estados ?;
- clasificación errónea de accesibilidad;
- missingness/censura MNAR en O/V;
- interferencia/exposición parcial;
- contaminación/crossover y vías directas;
- violaciones acotadas de exclusión/monotonicidad;
- falta de soporte en subpoblaciones.

Pero hoy no hay parámetros, cobertura, tasas, restricciones ni instrumentos materiales suficientes para calcular cotas informativas. **No se reportan cotas numéricas ni límites artificiales.** Se deja preparado el dictamen como BOUNDS_ONLY cuando se definan supuestos y evidencia que los sostengan.

### 8.4 No identificado / no evaluable ahora

- ITT confirmatorio de cualquier Outcome o Value.
- Primera etapa focal D_f* y efecto de accesibilidad.
- LATE_f.
- θ_A(q), θ_Af(q_X*) y efecto atribuible exclusivamente a accesibilidad.
- IIE C4, efecto directo/residual y descomposición de mediación.
- Efectos por dimensión Value, trade-offs y agregación.
- Soporte, potencia, precisión y generalización material.

La no-identificación actual deriva de múltiples carencias estructurales, no de un resultado nulo. No debe describirse como evidencia de ausencia de efecto.

## 9. DGP, estadística, potencia y criterios de recuperación

La arquitectura de DGP y los escenarios adversariales están documentados, pero faltan distribuciones conjuntas, parámetros, reglas de transición y contrafactuales D2 cuantificados. No se fijan valores por analogía ni se reutilizan N=2.000/R=1.000 como parámetros confirmatorios.

Antes de implementar se requiere:
- parametrización conjunta y versionada de DGP, con verdad conocida por etapa;
- asignación y soporte por historia/estrato;
- escenarios focales, nulos, adversos, fallo parcial, vías directas/colaterales, interacción, heterogeneidad, alternativas, interferencia, medición errónea, missingness y censura;
- estimandos por resultado y dimensión con escala, población y horizonte;
- criterios ex ante de sesgo, cobertura, error tipo I, potencia, precisión, recuperación de signo/magnitud, abstención y detección de no-identificación;
- búsqueda en cuadrícula de N y elección de R según error Monte Carlo, coste y precisión; reportar SE_MC;
- sensibilidad y cotas calibradas con parámetros justificados;
- separación computacional Generator/Analyzer/Evaluator y sellado de truth.

Un PASS sintético futuro solo demostraría recuperación metodológica dentro de los DGP y condiciones ensayados; no confirmaría causalidad empírica general ni C10 por sí mismo.

## 10. Condiciones exactas para reconsiderar Design Freeze

Design Freeze solo podrá proponerse cuando se cumplan conjuntamente los siguientes gates:

| Gate | Condición de salida verificable | Estado |
|---|---|---|
| G-SCI | Constructos, estimandos, resultados/dimensiones, horizonte, DAG, mecanismos y dictámenes de identificación reconciliados; lo no identificable queda formalmente acotado/excluido del alcance confirmatorio | BLOCKED |
| G-MAT | Roster UE/B1/servicio, IAM/C_SRC, snapshots exactos, inventario B, grafo transitivo, ACL/recursos, alternativas, provisión/crossover, unidad/interferencia y soporte con provenance | BLOCKED |
| G-SCHEMA | Maestro íntegro recuperado; modelo físico, formatos, cardinalidades, constraints, canonicalización por objeto y migraciones especificados y aceptados | BLOCKED |
| G-ROLE | Threat model, custodia de truth, ACL/canales, secretos, sealer y firewall Generator/Analyzer/Evaluator verificados | BLOCKED |
| G-TEST | P177/P178/P179/P182/P183 cruzados a estimandos, DGP, observables, fixtures previstos, oráculos, tolerancias, missingness, cotas y reglas de abstención | BLOCKED |
| G-REPRO | N/R, semillas, versiones, entorno, dependencias, inputs, comandos, hashes y manifiestos justificados y fijados | BLOCKED |
| G-AUTH | Autorización expresa para freeze/implementación y alcance concreto, separada de la autorización científica posterior | NOT GRANTED |

La secuencia no se invierte: primero se cierra especificación científica/material; después schema y contratos técnicos; luego se evalúa Design Freeze; a continuación se solicita autorización explícita de implementación. La ejecución científica requiere autorización separada y workflow canónico.

## 11. Próxima secuencia óptima

No abrir nuevos paquetes conceptuales ni repetir PA–PE. El trabajo siguiente es resolver fuentes materiales y especificación confirmatoria dentro de los bloqueos identificados:

1. **Recuperación del maestro íntegro y reconciliación de fuente:** resolver el archivo vacío y comprobar las referencias cruzadas sin reconstrucción inferida.
2. **Contrato material de asignación y roster:** probabilidades/ratio, estratos, algoritmo/semilla, UE/UA, IDs y evidencia pre-Z.
3. **Materialización IAM/snapshots/provisión:** solo tras autorización específica de captura; inventario B, dependencias, ACL, alternativas y evidencia de no interferencia.
4. **Outcome y Value:** seleccionar y completar fichas §224 por resultado/dimensión con perspectiva, consecuencia, horizonte y adjudicación; no seleccionar dimensiones por defecto.
5. **Soporte y causalidad:** completar q_X*/q_L*, positividad, mapping D2→g^Af, colaterales, DAG longitudinal e identificación C3/C4; dictaminar cotas solo si hay supuestos/evidencia suficientes.
6. **DGP/estadística:** cuantificar mecanismos, N/R, potencia, precisión, SE_MC, tolerancias y sensibilidad.
7. **Reevaluar gates y Design Freeze:** solo con evidencia verificable y autorización correspondiente.

El orden de captura material y cualquier ejecución queda sujeto a gobernanza y autorización. Esta secuencia es una hoja de ruta de dependencias, no permiso para empezar a capturar o ejecutar.

## 12. No-claims, no-regression y autorización

Esta reconciliación:
- no cambia TGCV Core, C09, C10 en main, RMA v3.38, Matrix v1.47, STATUS ni claims;
- no modifica D1/D2, DEC-C10-066/067/095, P*τ2/P*_F ni decisiones B1;
- no selecciona dimensiones V_j, Outcome primario, escala, ponderación, horizonte, parámetro, N o R;
- no declara identificado el ITT, la accesibilidad, LATE, mediación, efecto residual ni Value;
- no autoriza captura de IAM/snapshots, schema físico, fixtures confirmatorios, código, generación de datos, simulación, estimación o ejecución.

**Estado final:** INTEGRATED_RECONCILIATION_COMPLETED / CONFIRMATORY_FEASIBILITY_NOT_ESTABLISHED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.  
**scientific_execution=false; execution_authorized=false.**


## 13. Corrección de recuperación del maestro C10-S (2026-11-11)

La lectura inicial mediante Contents devolvía contenido vacío, pero el blob Git asociado al SHA `61d3079213558f6f74c14b60600ae3ca04c0a395` se recuperó íntegramente mediante fetch_blob: 1,134,655 caracteres / 12,136 líneas. Se inspeccionaron los §§266–273 y se confirmó la incorporación de PA, PB, PC, PD, PE, identidad B1 por UE, PB-MAT y B2-B3. Por tanto, **la incidencia de recuperación está RESUELTA**; no existía evidencia de pérdida del maestro. Se ha añadido §274 a ese mismo maestro con el dictamen integrado de factibilidad. La limitación de concordancia línea por línea indicada en §2 queda superada para el contenido recuperado, aunque no equivale a validación local de repositorio ni de CI.


## 14. Auditoría de consistencia cruzada y trazabilidad del maestro (2026-11-11)

### 14.1 Identidad de la versión recuperada

- Blob histórico recuperado antes de §274: `61d3079213558f6f74c14b60600ae3ca04c0a395` (1,134,655 caracteres; 12,136 líneas), que contiene §§266–273.
- Blob vigente tras §274 y §274.1: `51dcd3b2c84d33c437292ce5883f5b70e3d9491c` (1,137,928 caracteres; 12,156 líneas). Recuperado y verificado mediante fetch_blob; incluye §§266–274 y la aclaración §274.1.
- fetch_file/Contents continúa devolviendo longitud 0 para el maestro pese al blob vigente; no utilizar esa respuesta vacía como evidencia de pérdida. No existe validación local ni CI en esta sesión.

### 14.2 Crosswalk de consistencia

Se contrastaron §§266–274 con PA/C1, PB/PB-MAT, PC/C3-C4, PD/DGP, PE, identidad B1 por UE, B2–B3, auditoría focal A_f*/D_f*, auditoría IV, matriz mínima Outcome/Value, plan, secuencia, protocolo de paquetes y Closure Control Matrix.

**Resultado: consistencia sustantiva confirmada en los siguientes invariantes:**
1. D2 primario candidato / D1 secundario; no se presume asignación 1:1 ni se trata 0.80 como tasa observada o primera etapa focal.
2. P*_{τ2} primaria y P*_F secundaria; eventos post-Z no redefinen elegibilidad ITT; estados 1/0/? y NA justificado se mantienen.
3. UE/UA/UO diferenciadas; UE=UA condicionado a aislamiento. Una B1 y una oportunidad por UE no prueban no interferencia.
4. B, W_attempt/recepción, instalación, C_dep*, A_f*, D_f* y ΔT_acc* no son proxies intercambiables. A_f* y D_f* siguen medidas candidatas con mapping/evidencia material abiertos.
5. C1 ITT de política/paquete, θ_A general, θ_Af focal, LATE_f y C4 interventional siguen siendo estimandos distintos; no hay transferencia de identificación ni residual por resta ad hoc.
6. Outcome técnico y Value contextual son constructos separados; Outcome no es causa exclusiva por definición ni V_j=f(Outcome). Ningún O_k/V_j está operacionalizado; P179 conserva vector y trade-offs.
7. truth_dgp, observed_evidence y evaluation/adjudication siguen segregados; DGP cuantitativo, N/R, potencia y tolerancias permanecen abiertos.
8. G-SCI/G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO permanecen BLOCKED y G-AUTH NOT GRANTED. No implementación ni ejecución autorizadas.

### 14.3 Discrepancias documentales corregidas

- Se corrigió la referencia de recuperación: el SHA 61d307… identifica el blob histórico pre-§274, no la versión vigente; la precisión quedó registrada en §274.1.
- Se sustituyeron en plan, secuencia, protocolo y Closure Control Matrix los estados activos obsoletos de “maestro inaccesible/RECOVERY BLOCKER” por notas históricas supersedidas y estado recuperado.
- Se preservaron las notas históricas donde aportan trazabilidad, pero ya no operan como gates vigentes.

**Límite del dictamen:** esta es una auditoría de consistencia documental y semántica. No demuestra validez causal, suficiencia de medición, aislamiento, potencia, corrección de código, schema físico, seguridad implementada ni CI. No crea decisiones científicas ni autoriza implementación, captura o ejecución.


## 15. Resultado del ciclo D2 — asignación, población y soporte (2026-11-11)

La reconciliación complementaria está desarrollada en C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md y propagada al maestro §275.

Precisión clave: las probabilidades D2 de programación de intento (0 en control, 1 en tratamiento) son reglas de política condicionales a Z; no especifican la probabilidad experimental P(Z=1 | estrato,UA), ratio ni mecanismo de aleatorización. Tampoco deben confundirse con cumplimiento/recepción c, intento de fondo b o éxito técnico candidato s=0.80.

El contrato lógico de q_X* y positividad queda aclarado, pero distribución, pesos, soporte y factibilidad por historia no están materializados. q_L* solo se incorpora si se requiere historia secuencial post-Z con confusión inducida y estrategia longitudinal. E_i/App, UNKNOWN, IAM/C_SRC, roster, snapshots y aislamiento siguen OPEN/BLOCKED. No cambia el dictamen de no Design Freeze ni las autorizaciones.


## 16. Reconciliación de operacionalización confirmatoria Outcome/Value (2026-11-11)

Artefacto rector: `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md`, maestro §276.

El dictamen de factibilidad se mantiene. Se aclara que F* es el criterio funcional de ruta completa y O-CONF el resultado adjudicado de conformidad del destino; no se contabilizan como dos endpoints independientes. O-CONF sigue candidato prioritario, sin predicados atómicos, mapping/IAM, C0/G/H, snapshots, evento terminal ni oráculo independiente validado. FP-08 es gate probatorio separado.

Value conserva vector P179; B1/Need_preZ y perspectiva B1 son la base, pero autoridad/criterio, consecuencia, dimensiones V_j/k, instrumentos, escalas, baseline y horizonte siguen abiertos. No hay ningún Y_j confirmatorio completo. ITT por O/V separados; C3/C4 siguen no identificados en diseño material actual. G-SCI/G-MAT/G-TEST permanecen bloqueados; no cambia la autorización.

## 17. Caso B1: reconciliación semántica y bloqueo material (2026-11-11)

El caso de valoración se documenta en `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`. B1 por UE, servicio versionado por UE y una oportunidad estandarizada por UE se reutilizan. La oportunidad es un probe, no demanda natural ni Value. Need_preZ se formula como objetivo operativo focal relacionado con sostener una operación de servicio predeclarada en destino, pero la operación concreta sigue OPEN. La consecuencia B1 no se infiere de procesamiento, respuesta, F* ni O-CONF. No se seleccionan dimensiones V_j ni instrumentos. Esto no levanta el bloqueo PB-MAT: roster, IAM/C_SRC, snapshots, provisión, grafo, aislamiento, asignación y soporte siguen no demostrados. G-SCI/G-MAT/G-TEST siguen bloqueados.


## 18. Actualización del gate Outcome/Value tras DEC-C10-099 y §16.182 (2026-11-12)

La selección provisional de V_cont para la extensión sintética B está formalizada por DEC-C10-099; por ello, el estado histórico «no se seleccionan dimensiones V_j» de §16 debe leerse como anterior a esa decisión y no como estado vigente de selección. No se elimina el registro histórico ni se altera P179/DEC-C10-095.

El plan integrado §16.182 especifica truth temporal latente B1 y un canal S3 pasivo de indicadores imperfectos, separando truth, observación y evaluación. La especificación permite ensayar recuperación con canal calibrado por diseño y exige abstención/bounds con canal no calibrado. No es validación empírica de telemetría ni prueba de validez externa.

El gate Value no pasa a PASS: permanecen abiertos agregación normativa, K/frecuencia/baseline/ventana, parámetros del canal, relevancia/MDE y calibración. O-CONF sigue sin ficha §224 completa y su discriminación frente a V_cont es NOT_VERIFIABLE/CONDITIONAL. Se mantienen G-SCI/G-MAT/G-TEST bloqueados, Design Freeze no alcanzado y autorización de ejecución no concedida.


## 19. Actualización de B1 funcional y discriminación Outcome/Value (2026-11-12)

El contrato B1 §2 ya define la función del servicio (admitir solicitudes según ENABLED y exponer PROFILE); los textos previos que la describían como operación concreta abierta se superan solo en ese aspecto. El contenido de negocio de solicitudes/perfiles, roster y materialización siguen abiertos. V_cont representa cumplimiento temporal de esa función; F*/O-CONF representan conformidad terminal de la ruta/estado aplicado.

El plan §16.183 documenta contrastes discriminantes lógicos, pero la validación final no es verificable hasta completar F* (predicados/mapping/C0/G/H) y O-CONF (evento terminal/oráculo/ficha §224). No se altera el estado de G-MAT, G-SCI, G-TEST, G-SCHEMA, G-ROLE, G-REPRO ni G-AUTH. No Design Freeze, implementación o ejecución.



## 20. E+F — actualización integrada de medición, calibración y contrato PE (2026-11-12)

La reconciliación E+F se desarrolla en el plan §16.186 y no modifica decisiones científicas aceptadas.

1. V_cont truth se define como secuencia latente por intervalos de cumplimiento de la función B1; S3 es canal pasivo vectorial imperfecto. Agregación no ponderada, K, rejilla, ventana, baseline y calibración del canal siguen abiertos. La selección provisional de V_cont no cierra su escala.
2. O-CONF permanece ficha parcial y no confirmatoria; F*/IAM/oráculo/snapshot/evento/medición y discriminación frente a V_cont no están validados.
3. P178 tiene clean replay computacional PASS en el benchmark metodológico acotado; no proporciona N/R/ratio ni calibración para el DGP confirmatorio integrado. No se repite.
4. El procedimiento de calibración conjunta está especificado; los criterios normativos de relevancia/error y los parámetros DGP no se deducen de los contratos ni del benchmark.
5. PE tiene contrato lógico de roles e interfaces; la tecnología física sigue abierta. ACL/custodia/sealer/firewall, esquema/serialización y reproducibilidad requieren pruebas técnicas efectivas.

**Gates:** G-SCI, G-MAT, G-SCHEMA, G-ROLE, G-TEST y G-REPRO permanecen BLOCKED; G-AUTH NOT GRANTED. No Design Freeze. El alcance de un experimento sintético metodológico no requiere afirmar materialización D2; cualquier afirmación sobre D2 real, validez externa o identificación material sí exige sus gates materiales. No captura, implementación, generación, simulación ni ejecución científica autorizada.



## 21. Frontera de alcance — núcleo sintético frente a materialización D2 (2026-11-12)

El objetivo vigente de C10-S es un experimento causal sintético que compruebe si el diseño y el Analyzer recuperan, refutan o reconocen como no identificable una contribución conocida de ΔT_acc* a Value bajo DGPs versionados. No requiere una migración informática real ni materializar D2 en infraestructura operativa.

Por tanto, el gate de materialización real G-MAT (roster/IAM/C_SRC/instalación/ACL/recursos reales) queda OUT_OF_SCOPE_FOR_SYNTHETIC_CORE, no como bloqueo que fuerce a construir el entorno real. El núcleo sintético sí debe cerrar una cohorte finita generada/versionada, unidad/UA/UO, asignación reproducible, distribución basal/soporte, interferencia estipulada o aislamiento por construcción, verdad por etapa, parámetros y potenciales. Los escenarios de provisión, dependencias o fallos materiales pueden ser estipulados adversarialmente, sin presentarlos como observaciones reales.

No se harán claims sobre provisión real, validez externa o identificación material. Los gates G-SCI, G-SCHEMA, G-ROLE, G-TEST y G-REPRO siguen sujetos a sus condiciones; G-AUTH sigue NOT GRANTED. Esta precisión no autoriza generación, simulación, implementación ni ejecución.



## 22. DEC-C10-100 — escala V_cont aceptada y estado de factibilidad (2026-11-12)

La escala inicial de V_cont queda aceptada provisionalmente como fracción temporal de cumplimiento funcional B1: media no ponderada de A_B1(i,k) sobre intervalos de igual duración en ventana/rejilla post-Z común ex ante. UNKNOWN produce bounds, no cero ni exclusión del denominador. El baseline no se resta automáticamente. DEC-C10-100 cierra agregación de truth, no K, ventana, frecuencia, MDE, canal S3, parámetros ni criterios de error.

La calibración confirmatoria se organizará como superficie de recuperación a lo largo de magnitudes verdaderas [0,1], con escenarios nulos, positivos, negativos, heterogéneos, directos/colaterales y de medición degradada. No se inventa un MDE: curvas de recuperación/abstención y frontera Pareto N–asignación–R–SE_MC se obtendrán cuando soporte, distribuciones conjuntas y criterios de operación estén justificados. No se transfieren cifras P178.

**Estado:** VCONT_AGGREGATION_ACCEPTED_PROVISIONALLY / MEASUREMENT_VALIDITY_CONDITIONAL / OCONF_DISCRIMINATION_NOT_VERIFIED / QUANTITATIVE_OPERATING_POINT_OPEN / G-SCI/G-SCHEMA/G-ROLE/G-TEST/G-REPRO BLOCKED / G-AUTH NOT GRANTED. No ejecución.
