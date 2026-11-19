# C10-S — Gate 110: estimandos de asignación y exposición bajo interferencia

**Estado:** ESTIMAND TAXONOMY SPECIFIED / DESIGN ALTERNATIVES KEPT OPEN / IDENTIFICATION CONDITIONS EXPLICIT / POPULATION, SUPPORT AND RANDOMIZATION OPEN / NO NEW TEST IDS / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO DESIGN FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** plan maestro §§16.185, 16.187–16.200 y 16.259; DGP/PE contracts; DEC-C10-066/067/100/101/102; Gate 108 y Gate 109; contratos D2, g_A, C4, O-CONF y V_cont.  
**Tipo:** especificación metodológica documental derivada; no constituye decisión de diseño, estimación, calibración ni validación empírica.

---

## 1. Pregunta y dictamen ejecutivo

¿Qué estimandos de asignación y exposición son recuperables bajo las cuatro arquitecturas que Gate 109 dejó abiertas, y qué debe hacer el Analyzer cuando la interferencia, el mapping o el soporte no permiten identificación?

**Dictamen:** los cuatro escenarios requieren estimandos y condiciones de identificación distintos. El ITT-D2 puede representar el efecto total del paquete asignado si el mecanismo de asignación, la población, la consistencia, el seguimiento y la estructura de interferencia están suficientemente especificados. Con interferencia, el ITT individual convencional no queda justificado por defecto. La asignación por clúster puede identificar un efecto total de política de clúster bajo aleatorización válida y ausencia de interferencia entre clústeres (o una exposición entre clústeres explícitamente modelada); no elimina la interferencia intraclúster. La asignación individual con mapa de exposición puede identificar efectos directos/indirectos o contrastes de exposición solo con mapa correcto, probabilidades positivas y soporte suficiente. Si la interferencia relevante no está mapeada, el Analyzer no debe devolver una atribución individual puntual como si SUTVA se cumpliera.

Gate 110 no selecciona ninguna arquitectura, no fija población, ponderación, N, ratio, estratos, clústeres, función de exposición, probabilidades ni parámetros.

**Resultado:** GATE_110_ESTIMAND_TAXONOMY_SPECIFIED / FOUR_ASSIGNMENT_ARCHITECTURES_DISTINGUISHED / EXPOSURE_IDENTIFICATION_CONDITIONS_EXPLICIT / D2_ITT_SEPARATE_FROM_G_A_AND_C4 / POPULATION_SUPPORT_RANDOMIZATION_OPEN / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.

## 2. Reconciliación histórica y precedencia

1. **Gate 109** distingue UE, UA, cluster, UO, U_G, revisión U_G, instancia CMP/EID, snapshot y route_id. No demuestra equivalencias ni cardinalidades materiales. Sus gaps G109-01…14 permanecen abiertos.
2. **Plan §16.199.3**: UE=UA solo sería admisible con aislamiento completo por construcción. Si hay recursos/dependencias/pools/agentes/canales compartidos, se requiere asignación por clúster o mapa de exposición (G_i(Z_{-i})); sin mapa y soporte no se declara SUTVA ni ITT individual identificado.
3. **Plan §16.199.4–.7**: (g_{A1}) y (g_{A0}) son políticas estocásticas factibles sobre el vector completo (Delta T_{acc}^{*}=(Delta U^{*},Delta R^{*},Delta C^{*},Delta X^{*})), bajo la misma (q_X^*) y (r_{common}). Las vías directas (D_i(z)), colaterales (C_i(z)), interacciones e interferencia se preservan; no se asume su ausencia.
4. **Plan §16.185**: D2/Z_B genera potenciales por etapas; ITT es efecto total del paquete por resultado. El mapping D2→(g_A) no está demostrado. C4 es mediación interventional distinta.
5. **Plan §16.188.5**: salida por estimando: IDENTIFIED, CONDITIONALLY_IDENTIFIED, BOUNDS_ONLY, NOT_IDENTIFIED, NOT_INSTANTIATED o INDETERMINATE_MEASUREMENT.
6. **DEC-C10-100/101/102**: (V_{cont}) es truth temporal por UE y K intervalos iguales; UNKNOWN se propaga a bounds. No determina por sí mismo el mecanismo de asignación ni la inferencia.

No se reabren decisiones ni se crean tests: Gate 110 formaliza consecuencias analíticas de los contratos existentes.

## 3. Notación y objetos que no se deben colapsar

- (i): unidad experimental UE; (c): unidad/clúster de asignación cuando exista.
- (Z_i) o (Z_c): asignación efectiva según el mecanismo aprobado; no equivale a programación, intento, recepción, instalación o accesibilidad.
- (A_i): unidad de asignación UA a la que pertenece UE (i); su identidad material sigue OPEN.
- (G_i): mapa de exposición a asignaciones de otras unidades; no está especificado.
- (E_i=G_i(mathbf Z_{-i})): exposición inducida por las asignaciones ajenas; no equivale a una etiqueta cluster.
- (Y_i): resultado potencialmente observado por UE, por resultado y ventana, con truth y observación separados.
- (q_X^*): distribución conjunta basal objetivo anterior a Z; no es la propensión (pi_h).
- (g_{A1},g_{A0}): intervenciones estocásticas sobre la distribución completa y factible de (Delta T_{acc}^{*}).
- (r_{common}): régimen explícito común para vías no focales; no es un residuo ni una hipótesis tácita.
- (C4): estimando de mediación interventional longitudinal, distinto de ITT y (g_A).

La unidad de potenciales/resultados, la unidad de aleatorización, la unidad de observación, la unidad lógica U_G y la instancia técnica pueden diferir. Ningún identificador técnico sustituye la unidad causal sin mapping documentado.

## 4. Escenario A — asignación individual con aislamiento completo

### 4.1 Potenciales y estimando

Si cada UE recibe asignación individual (Z_i) y el aislamiento completo elimina vías de interferencia entre UE, puede utilizarse:

[
Y_i(z_i)
]

El ITT por resultado (Y), en población objetivo (P^*), es:

[
	au_{ITT}^{D2}(Y)=E_{isim P^*}[Y_i(1)-Y_i(0)]
]

El contraste se refiere a la asignación D2 como paquete. Se estima por separado para cada resultado definido (p. ej. O-CONF por unidad de adjudicación válida y V_cont por UE); no se intercambian resultados ni unidades.

### 4.2 Condiciones mínimas

- UE=UA demostrada materialmente para el mecanismo individual.
- Asignación aleatoria reproducible, con probabilidades conocidas y positivas en la población objetivo/estratos pertinentes.
- Aislamiento de recursos, dependencias, pools, agentes, canales y otras vías de spillover demostrado por construcción y evidencia apropiada al alcance del diseño.
- Consistencia: versiones/políticas asignadas y recibidas quedan distinguidas; el tratamiento definido corresponde al paquete realmente asignado.
- Población y seguimiento definidos sin selección por variables post-Z; missingness/censura tratados según sus contratos.
- Unidad de análisis e inferencia coincidente con el mecanismo independiente de asignación.

### 4.3 Qué no se sigue

La ausencia de interferencia no demuestra exclusión de vías directas/colaterales de D2 hacia Value. Por ello, aun con ITT identificado, no se atribuye automáticamente a (Delta T_{acc}^{*}). La identificación de (g_A) o C4 necesita sus propias condiciones.

**Estado si no se demuestra aislamiento:** no utilizar esta arquitectura como justificación de ITT individual convencional; evaluar B/C/D.

## 5. Escenario B — asignación por clúster

### 5.1 Potenciales y estimandos

Si todas las UE de un clúster (c) reciben una asignación (Z_c), los resultados pueden depender de la asignación del clúster y de la exposición intraclúster:

[
Y_{ic}(z_c,mathbf z_{-c})
]

Si no existe interferencia entre clústeres, la notación puede reducirse a (Y_{ic}(z_c)), permitiendo que la interferencia dentro del clúster forme parte del efecto de la política de clúster.

Dos promedios posibles, no intercambiables:

**Promedio por UE (estimando individual medio):**
[
	au_{UE} = E_{c}left[rac{1}{N_c}sum_{i=1}^{N_c}
{Y_{ic}(1)-Y_{ic}(0)}ight]
]

**Promedio por clúster (cada clúster con igual peso):**
[
	au_C = E_cleft[ar Y_c(1)-ar Y_c(0)ight]
]

La primera expresión requiere declarar la población objetivo y ponderación por UE; la segunda define una población de clústeres. Con tamaños (N_c) desiguales no son equivalentes. Las fórmulas ilustran objetivos posibles, no fijan cuál debe usarse.

### 5.2 Condiciones mínimas

- UA=cluster demostrada en el mecanismo real.
- Número y roster de clústeres definidos; asignación aleatoria en ese nivel y probabilidades positivas.
- Consistencia de la política dentro de cada clúster y versiones documentadas.
- Interferencia entre clústeres ausente por construcción o modelada mediante exposición interclúster.
- Estimando, ponderación, población objetivo y nivel de inferencia preespecificados.
- Inferencia que respete el nivel de aleatorización y la dependencia intraclúster; el número bruto de UE no sustituye el número de clústeres independientes.

### 5.3 Límite fundamental

La asignación por clúster no elimina automáticamente spillovers entre UE del mismo clúster. Si estos spillovers forman parte del régimen de política, el ITT es efecto total de asignar el clúster bajo ese régimen. Si se pretende un efecto directo individual separado de efectos de pares, se necesita un estimando adicional y un mapa/contraste con soporte. Si existen spillovers entre clústeres no controlados, el contraste simple por cluster puede dejar de identificar el efecto pretendido.

## 6. Escenario C — asignación individual con mapa de exposición

### 6.1 Potenciales y estimandos

Si (Z_i) se asigna individualmente pero las asignaciones ajenas afectan a (Y_i), un mapa correcto (E_i=G_i(mathbf Z_{-i})) permite representar:

[
Y_i(z_i,e_i)
]

No hay un único ITT individual universal: los contrastes dependen de la distribución de exposición inducida por el diseño.

Posibles contrastes, sujetos a definición y soporte:

**Efecto directo a exposición fija (e):**
[
DE(e)=E[Y_i(1,e)-Y_i(0,e)]
]

**Efecto de spillover a asignación propia fija (z):**
[
SE(z;e_1,e_0)=E[Y_i(z,e_1)-Y_i(z,e_0)]
]

**Efecto marginal de política de asignación:** contraste entre distribuciones de asignaciones/exposiciones completas inducidas por dos mecanismos (mathcal{P}_1,mathcal{P}_0). Debe especificarse como efecto de política de red/diseño, no etiquetarse como efecto directo.

El efecto directo y el spillover son distintos. El mapa (G_i) debe reducir la exposición a una representación suficiente para el resultado potencial dentro del dominio del DGP; la suficiencia no se presume por conveniencia.

### 6.2 Condiciones mínimas

- Asignación individual con mecanismo conocido y vector Z trazable.
- Definición previa y versionada de la red/relaciones relevantes y del mapa (G_i), incluidas dependencias/pools/canales compartidos relevantes.
- Consistencia y no ambigüedad de versiones/exposiciones.
- Positividad de las probabilidades de las combinaciones ((z,e)) que integran el contraste.
- Soporte común entre exposiciones comparadas y población objetivo.
- Probabilidades de exposición derivables del mecanismo de aleatorización; no inferidas de una etiqueta de cluster.
- Inferencia que respete dependencia de red/exposición.
- Sensibilidad a misspecification del mapa y a spillovers omitidos.

### 6.3 Límites

Si el mapa es correcto solo para una parte de recursos/canales, el estimando se limita a esa cobertura y no se generaliza a toda la interferencia. Si las categorías de exposición no tienen soporte, el contraste correspondiente es NOT_IDENTIFIED o BOUNDS_ONLY. No se extrapola silenciosamente.

## 7. Escenario D — interferencia relevante no mapeada

Si se sabe o es plausible que (Z_j) afecta a (Y_i), pero no existe un mapa válido ni soporte para describir las exposiciones relevantes, el potencial (Y_i(z_i)) no representa adecuadamente la dependencia.

Consecuencias:

- No declarar ITT individual convencional identificado bajo SUTVA.
- No usar cluster como proxy de exposición sin evidencia.
- No construir (G_i), (mathcal G), cluster_id o relaciones artificiales para salvar el análisis.
- No ajustar por variables post-Z o proxies observados de exposición como sustituto automático de identificación.
- No interpretar el contraste bruto como efecto directo o focal.
- Mantener el resultado como NOT_IDENTIFIED; BOUNDS_ONLY solo si existen restricciones defendibles que permitan cotas válidas.
- Puede reportarse una descripción del contraste observado/aleatorizado con su alcance exacto, pero no renombrarlo como estimando causal individual identificado.

La no identificación es una salida correcta del Analyzer, no un fallo del diseño de validación sintética cuando el DGP exige abstención.

## 8. Matriz comparativa de identificación

| Dimensión | A. Individual aislada | B. Clúster | C. Individual + mapa | D. Interferencia no mapeada |
|---|---|---|---|---|
| Unidad de asignación | UE, si UE=UA demostrado | Cluster | UE | No adjudicable de forma suficiente |
| Potenciales | (Y_i(z_i)) | (Y_{ic}(z_c)) si no hay spillover intercluster; de otro modo (Y_{ic}(z_c,mathbf z_{-c})) | (Y_i(z_i,e_i)) | Mapa de potenciales incompleto |
| ITT D2 | Identificable bajo aleatorización/consistencia/soporte | Efecto total de política de cluster; nivel de promedio explícito | Efecto de política/exposición inducida, si distribución de exposición identificable | ITT individual convencional no identificado |
| Efecto directo | No requiere separar spillovers si aislamiento válido | No se separa del efecto intraclúster sin diseño adicional | (DE(e)), si hay soporte | No identificado |
| Spillover | Por construcción ausente dentro del alcance | Intraclúster puede formar parte del paquete; intercluster debe tratarse | (SE(z;e_1,e_0)), si hay soporte | No identificado; cotas solo con restricciones |
| Unidad de inferencia | UE independiente | Cluster | Según diseño/red y mecanismo | No fijable para estimando individual |
| Ponderación | Población UE declarada | Por UE o por cluster, decisión explícita | Población y distribución de exposición explícitas | No procede punto estimado causal sin supuestos |
| Requisito central | Aislamiento demostrado | Asignación cluster + control de intercluster | Mapa correcto + probabilidades/soporte | Abstención o bounds |
| Estado actual TGCV | No demostrado | No seleccionado | No especificado | Fallback metodológico si gaps no se resuelven |

## 9. Separación de estimandos: D2 ITT, g_A y C4

### 9.1 ITT-D2

Para cada resultado (Y), ITT-D2 es el efecto total de asignar el paquete D2, bajo la unidad y arquitectura de interferencia válidas:

[
	au_{ITT}^{D2}(Y)=E[Y(mathcal P_1)-Y(mathcal P_0)]
]

La notación (mathcal P_z) debe instanciarse según escenario A/B/C (política individual, de clúster o de asignación/exposición). No significa que el tratamiento recibido sea igual a Z. El ITT no condiciona por intento, recepción, instalación, accesibilidad, selección, ejecución ni disponibilidad de Value post-Z.

El ITT se informa por resultado y escala, preservando:
- O-CONF por instancia×ruta, con mapping/agregación a población UE solo si existe regla explícita.
- V_cont truth por UE×K intervalos iguales, con UNKNOWN propagado a bounds.
- Observed evidence y measurement error por separado de truth.

### 9.2 Intervención estocástica de accesibilidad (g_A)

El estimando de accesibilidad permanece:

[
	heta_A(q_X^*;Y)=
E_{Xsim q_X^*,Delta Tsim g_{A1},Rsim r_{common}}[Y(Delta T,R)]
-
E_{Xsim q_X^*,Delta Tsim g_{A0},Rsim r_{common}}[Y(Delta T,R)]
]

(g_{A1}) y (g_{A0}) actúan sobre la distribución factible del vector completo (Delta T_{acc}^{*}), no sobre Z ni sobre A_f* aislada. La interferencia que afecta a la generación/realización de (Delta T_{acc}^{*}) o al resultado debe quedar incluida en el régimen de exposición o restringida explícitamente; el mapa de asignación de D2 no sustituye el régimen causal de (g_A).

Requisitos adicionales: (q_X^*) común, políticas factibles, soporte común, consistencia/versiones, (r_{common}) explícito, vías directas/colaterales declaradas y una unidad/población compatibles con la intervención. El ITT-D2 no identifica (	heta_A) salvo que exista un mapping causal adicional, demostrado y con condiciones propias; ese mapping hoy no está demostrado.

### 9.3 C4 — mediación interventional

C4 pregunta por contribución mediada bajo una intervención longitudinal y exige controlar la confusión mediador–resultado, incluidos confusores post-Z inducidos por Z, con orden temporal, positividad secuencial y régimen de intervención definidos. Con interferencia, la historia y los potenciales relevantes deben incluir la exposición de red/pares en las etapas pertinentes.

C4 no es (	au_{ITT}^{D2}-	heta_A), no es una descomposición automática del ITT y no hereda la identificación de (g_A). Si la historia longitudinal, exposición o soporte no se pueden especificar, C4 permanece BOUNDS_ONLY o NOT_IDENTIFIED conforme al contrato existente.

## 10. Reglas de identificación y salida del Analyzer

| Estado | Regla de uso en Gate 110 |
|---|---|
| IDENTIFIED | Estimando definido; unidad/población, asignación/exposición, consistencia, soporte y medición permiten identificación bajo los supuestos declarados |
| CONDITIONALLY_IDENTIFIED | Identificación válida solo bajo supuestos explícitos no demostrados plenamente; mostrar análisis de sensibilidad y límites |
| BOUNDS_ONLY | Punto no identificado, pero restricciones defendibles permiten cotas identificadas; declarar qué restricciones producen las cotas |
| NOT_IDENTIFIED | Mapa, soporte, aleatorización, consistencia o control de confusión insuficientes para el estimando |
| NOT_INSTANTIATED | Estimando conceptual definido, pero el DGP/contrato aún no fija sus componentes o no existe una versión evaluable |
| INDETERMINATE_MEASUREMENT | El estimando podría estar identificado causalmente, pero la observación/medición no discrimina suficientemente el resultado |
| EFFECT_OF_PACKAGE_ONLY | Etiqueta interpretativa: ITT de D2 recuperable, pero no atribución focal a (Delta T_{acc}^{*}) |

La etiqueta EFFECT_OF_PACKAGE_ONLY no sustituye el estado de identificación; se informa junto con IDENTIFIED/CONDITIONALLY_IDENTIFIED y la razón de no atribución focal.

### 10.1 Orden obligatorio de adjudicación

1. Definir el estimando, resultado, población y unidad.
2. Recuperar el mecanismo de asignación y su unidad efectiva.
3. Adjudicar aislamiento, clúster o mapa de exposición; no presumir ninguno.
4. Verificar soporte/positividad para las asignaciones y exposiciones requeridas.
5. Verificar consistencia, versiones y tratamiento de desviaciones.
6. Verificar pérdida/censura, medición y separación truth/observed.
7. Solo después adjudicar identificación y estimación.
8. Evaluar por separado si el resultado es efecto total del paquete, contribución (g_A) o C4.

No se condiciona el ITT a variables post-Z para mejorar artificialmente la precisión o “controlar” interferencia.

## 11. Sensibilidad y falsadores que deben conservarse

No se crean nuevos test IDs. Los contratos existentes S4R, MEAS, MISS, TRJ, INT, POL, P177–P183 y XSYNC se reutilizan y su cobertura se deberá crosswalkear al completar la matriz de pruebas existente.

Dimensiones de sensibilidad documental/metodológica necesarias:
- Omisión de pools, dependencias, agentes o canales compartidos en (G_i).
- Variación de la definición de clúster y de la frontera de interferencia.
- Interferencia residual entre clústeres.
- Exposición mal clasificada y error en el vector Z.
- Probabilidades de exposición pequeñas/cero y pérdida de soporte.
- Heterogeneidad por tamaño de clúster y diferencia entre ponderación UE/cluster.
- Crossover, contaminación, versiones asignada/recibida/aplicada divergentes.
- Medición S3 diferencial por asignación, exposición, unidad o ventana.
- Vías directas/colaterales D2→O/V e interacciones.
- Misspecification de (q_X^*), (g_A), (r_{common}) y confusores longitudinales C4.

El DGP deberá incluir escenarios donde el estimando es conocido e identificable y escenarios donde no lo es. El Analyzer debe recuperar ambos tipos correctamente: estimación cuando corresponde y abstención/bounds cuando no. Este gate no instanciará parámetros, fixtures, N, R ni tolerancias.

## 12. Crosswalk de gaps y decisiones no tomadas

| ID | Cuestión | Dictamen |
|---|---|---|
| G110-01 | Arquitectura de asignación real | No seleccionada |
| G110-02 | UE/UA/cluster físicos y cardinalidad | OPEN; Gate 109 |
| G110-03 | Aislamiento completo individual | No demostrado |
| G110-04 | Mapa (G_i) y relaciones compartidas | No especificado |
| G110-05 | Probabilidades de asignación/exposición | OPEN; no se inventan |
| G110-06 | Soporte/positividad por estrato y exposición | OPEN |
| G110-07 | Población objetivo y roster | OPEN |
| G110-08 | Ponderación UE vs cluster | No elegida |
| G110-09 | Unidad de inferencia y varianza | Depende de mecanismo; OPEN |
| G110-10 | Consistencia/versiones/crossover | Contratos parciales; mapping material OPEN |
| G110-11 | D2 ITT por O-CONF/V_cont | Separación conceptual definida; mapping/agregación OPEN |
| G110-12 | D2→(g_A) | No demostrado |
| G110-13 | Identificación C4 bajo exposición/interferencia | OPEN; no se hereda de ITT |
| G110-14 | Sensibilidad a interferencia residual | Requisito definido; parámetros OPEN |
| G110-15 | Bounds defendibles | No definidos; no inventar restricciones |
| G110-16 | Reutilización de tests existentes | Crosswalk de cobertura pendiente; no nuevos IDs |

## 13. Disposiciones de gobernanza

- No se selecciona A/B/C/D ni se recomienda un diseño como si estuviera aprobado.
- No se declara SUTVA, no interferencia, aislamiento, cluster o mapa (G_i) por conveniencia.
- No se crean `cluster_id`, `assignment_id`, claves puente, tablas, schemas o FKs.
- No se modifican DEC-C10-059/065/066/067/069/100/101/102, C0, Gate 98 ni Gate 109.
- No se modifican contratos de D2, (g_A), C4, O-CONF o V_cont.
- No se crean nuevos test IDs ni se convierten matrices documentales en fixtures ejecutables.
- No se ejecutan validadores, workflows, código, simulaciones, generación, estimación ni calibración.
- No se promueve research a main ni se altera el estado Draft del PR.
- `scientific_execution=false`; `execution_authorized=false`.

**Dictamen final:** GATE_110_ESTIMAND_TAXONOMY_SPECIFIED / D2_ITT_NOT_EQUIVALENT_TO_ACCESSIBILITY_EFFECT / G_A_AND_C4_SEPARATE / INDIVIDUAL_ISOLATION_NOT_DEMONSTRATED / CLUSTER_DESIGN_NOT_SELECTED / EXPOSURE_MAP_NOT_SPECIFIED / UNMAPPED_INTERFERENCE_REQUIRES_ABSTENTION_OR_DEFENSIBLE_BOUNDS / POPULATION_SUPPORT_RANDOMIZATION_OPEN / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_DESIGN_FREEZE.
