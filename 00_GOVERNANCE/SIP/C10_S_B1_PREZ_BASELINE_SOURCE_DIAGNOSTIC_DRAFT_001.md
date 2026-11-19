# C10-S — Diagnóstico de fuentes basales y generador de truth para Need_preZ

**ID:** C10-S-B1-PREZ-BASELINE-SOURCE-DIAGNOSTIC-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_DIAGNOSTIC / PROPOSED / NOT_APPROVED / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Objeto

Determinar si las variables basales y los contratos constitutivos ya presentes en C10-S proporcionan una base semántica válida para generar la truth de `Need_preZ` por B1/UE, sin inventar atributos, parámetros o registros ni reutilizar constructos con otro significado.

Fuentes contrastadas en la rama de investigación:
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, §§2, 23.
- `C10_S_C1_BASELINE_ELIGIBILITY_CROSSWALK_DRAFT_001.md`, §§2–8 y dictamen actualizado.
- `C10_S_BASE_DGP_SCOPE_AND_ABSTRACT_CONFIGURATION_CONTRACT_PROPOSAL_DRAFT_001.md`, partición constitutiva/condicional y estado de cierre.
- `C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md`, catálogo S0–SF y rutas.
- `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`, §§3–5 y 9.
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md`.

## 2. Inventario basal existente y límite semántico

El contrato temporal, §2, coloca en t−1:
`X_i, H_i0, C_c,i0, L_m,i0, C_dep,i0, A_f,i0*, T_acc,i0, F_alt,i0`.

| Variable/objeto | Significado contractual | ¿Puede generar Need directamente? | Motivo |
|---|---|---|---|
| X_i | Características basales | No acreditado | No hay mapping semántico aprobado entre sus componentes y el objetivo B1 |
| H_i0 | Historia basal | No acreditado | No se ha especificado contenido ni regla que determine el objetivo |
| C_c,i0 | Condiciones constitutivas/no focales | No | Condiciones de realizabilidad/accesibilidad, no existencia del objetivo |
| L_m,i0 | Otras condiciones temporales | No acreditado | Papel causal y contenido dependen de su ficha; no existe mapping a Need |
| C_dep,i0 | Dependencia técnica focal basal | No | Estado técnico del sistema; no equivale a objetivo operativo de B1 |
| A_f,i0* | Accesibilidad focal basal | No | Accesibilidad y necesidad/objetivo son constructos distintos |
| T_acc,i0 | Espacio transformacional accesible | No | No determina qué objetivo tiene B1 |
| F_alt,i0 | Alternativas funcionales basales | No | Existencia de alternativas no determina si B1 tiene el objetivo focal |

No se concluye que esas variables nunca puedan asociarse estadísticamente con Need. Se concluye que los contratos disponibles no autorizan usarlas como definición, proxy determinista ni regla generadora de la truth.

## 3. Otros candidatos descartados como generadores automáticos

| Candidato | Razón de descarte |
|---|---|
| Existencia de B1 | Una unidad B1 existe por diseño; eso no implica que todas tengan el objetivo focal |
| Instancia lógica de servicio por UE | Identidad/versionado del servicio no implica objetivo de la B1 |
| CMP/PAR/REF/RUL | Constituyen la configuración funcional del paquete DGP; no representan automáticamente el objetivo de cada B1 |
| ENABLED/PROFILE | Estado declarativo del servicio; no acredita el objetivo basal de B1 |
| Oportunidad estandarizada (`N_opportunities=1`) | Probe común de evaluación, no demanda natural ni generador de Need |
| Request_attempt/received/admitted | Eventos de petición posteriores o distintos; no definen Need |
| Instalación, C_dep, A_f, Reach | Variables técnicas/transformacionales y consecuencias del diseño; su uso sería circular |
| Outcome/Value | Resultados posteriores; prohibido reconstruir Need retrospectivamente |

La partición aprobada por DEC-C10-053 —CMP, PAR, REF y RUL constitutivos; POL condicional; MET para trazabilidad— no contiene una regla aprobada de pertenencia del objetivo operativo a cada B1.

## 4. Resultado del diagnóstico

**No hay una regla generadora basal ya existente que permita producir Need_truth sin añadir una estipulación semántica explícita por B1.**

La definición funcional de trabajo aceptada de Need ya proporciona el contenido del objetivo. Lo que falta es una regla de asignación de ese objetivo entre unidades B1.

La solución conceptual mínima que se propone estudiar es distinguir:

1. **Especificación basal del objetivo de B1:** estipulación sintética, ex ante, por unidad, que declara si el objetivo operativo definido en el contrato funcional pertenece a esa B1.
2. **Need_truth:** estado derivado de esa estipulación mediante una regla versionada.
3. **Fuentes observables:** documentos/declaraciones sintéticas generados por el modelo de observación a partir de la estipulación, sin copiar su etiqueta ni revelar la truth.

La especificación basal del objetivo no debe confundirse con una nueva covariable causal de X, H, C_c o L_m. Es el contenido semántico de la unidad B1 que permite definir la truth objeto de adjudicación. Si se decide representarla como atributo/registro técnico, su ubicación y tipo deben aprobarse antes de implementación; no se propone alterar la partición CMP/PAR/REF/RUL ni DEC-C10-061.

## 5. Requisito de heterogeneidad y soporte

Para que el Analyzer pueda evaluarse en clasificación binaria, el diseño aprobado deberá contener soporte para:
- B1 cuyo objetivo focal existe (truth=1).
- B1 cuyo objetivo focal está afirmativamente excluido (truth=0).

No se fijan prevalencia, proporciones, distribución, estratos, correlaciones con X/H/C_c/L_m ni semilla. No se exige que los dos estados aparezcan en cada brazo, estrato o combinación sin una decisión de diseño y soporte formal.

Truth=? solo podrá existir si la especificación generadora está explícitamente indeterminada. No se usará como sustituto de ausencia de fuentes, cobertura incompleta o fallo del adjudicador.

La regla de asignación debe ser independiente de Z, política D2, provisión, instalación, accesibilidad, Reach, petición, ejecución, Outcome y Value. Cualquier asociación con covariables basales requerirá una justificación de diseño explícita y no podrá inferirse de correlaciones o de la conveniencia de producir heterogeneidad.

## 6. Implicación para el modelo de observación

Solo después de aprobar el mecanismo de especificación basal puede definirse el modelo de observación. Este último generará fuentes que puedan:
- declarar afirmativamente el objetivo;
- declarar afirmativamente su exclusión;
- omitir la declaración;
- presentar información ambigua, conflictiva, incompleta o corrupta.

La ausencia de una declaración no es evidencia de exclusión. El modelo debe permitir que truth=1 y truth=0 produzcan evidencia observada imperfecta, sin que el Analyzer tenga acceso al mecanismo generador ni a la etiqueta.

El modelo de observación puede depender de la especificación oculta como causa generadora, pero no puede copiar el valor de truth como contenido o metadato visible.

## 7. Decisión propuesta y gates

| Cuestión | Dictamen |
|---|---|
| Reutilizar X/H/C_c/L_m como proxy automático | Rechazado por falta de fundamento contractual |
| Derivar Need de C_dep/A_f/T_acc/F_alt | Rechazado por diferencia semántica y riesgo de circularidad |
| Derivar Need de CMP/PAR/REF/RUL o ENABLED/PROFILE | Rechazado como equivalencia automática |
| Estipulación basal explícita por B1 | Candidata mínima; requiere aceptación |
| Soporte truth=1 y truth=0 | Requisito para evaluación binaria; composición aún abierta |
| Prevalencia y asignación de estados | OPEN; no parametrizadas |
| Modelo de observación | OPEN; depende de cerrar la estipulación basal |
| Representación física/permisos | OPEN; no implementados |

## 8. Próximo cierre recomendado

Antes de diseñar fuentes o parámetros, se debe resolver una única cuestión de contrato:

**¿Se acepta que la truth de Need_preZ se genere a partir de una especificación sintética explícita del objetivo operativo de cada B1, separada de las covariables causales basales y de la configuración técnica del servicio?**

Si se acepta, el siguiente artefacto deberá definir exclusivamente:
- unidad semántica de la estipulación;
- regla de pertenencia/exclusión del objetivo;
- condiciones para truth=1/0/?;
- independencia respecto de Z y variables post-Z;
- soporte mínimo de escenarios sin prevalencias arbitrarias;
- referencia y versionado de la definición funcional del objetivo.

No se deben generar unidades ni fuentes hasta cerrar este contrato.

## 9. Dictamen

**NO EXISTING BASELINE VARIABLE AUTHORIZED AS NEED GENERATOR / EXPLICIT B1 OBJECTIVE SPECIFICATION IS THE MINIMAL CANDIDATE / REQUIRES ACCEPTANCE BEFORE OBSERVATION MODEL OR PARAMETERIZATION.**

Este diagnóstico no modifica el maestro, las decisiones aceptadas, la RMA, la Evidence→Claim Matrix, STATUS, la población, los estimandos ni el DGP ejecutable. No materializa truth, roster, fuentes, fixtures o código. No ejecuta validadores, simulaciones ni replay.

`scientific_execution=false`; `execution_authorized=false`.



## 8. Reconciliación específica: covariables basales y condicionamiento del canal S7

La revisión de §2 y del contrato temporal confirma que no hay una covariable basal autorizada para generar Need ni para condicionar la declaración S7. El resultado se especializa ahora para el proceso observacional:

- X, H₀, C_c, L_m no entran en el canal S7 base mientras no exista definición semántica, rol causal y evidencia específica por variable.
- C_dep, A_f*, T_acc, F_alt, instalación, Reach, peticiones, ejecución, Outcome y Value no pueden usarse como sustitutos de Need ni como predictores del canal basal: no acreditan el objetivo y varios son técnicos, posteriores o potencialmente circulares.
- CMP/PAR/REF/RUL y ENABLED/PROFILE describen configuración/estado del servicio; no establecen el objetivo de B1 ni el mandato declarativo.
- La única dependencia constructiva que el canal necesita representar es la relación de medición entre la estipulación Need reservada y el resultado observable, mediante un mecanismo explícito con errores posibles y firewall. La oportunidad y la versión/mandato son condiciones de diseño fijadas ex ante, no covariables estimadas.
- Esto no supone independencia estadística entre Need y las características basales ni entre unidades. Simplemente deja esas relaciones fuera del DGP base por falta de especificación y evidencia.

Cualquier futura inclusión de covariable debe superar los requisitos de §15.4 del contrato de observación. No se crean variables, mappings, parámetros ni escenarios por conveniencia.

**Estado:** X₀=∅ como conjunto de covariables admitidas en el canal base, por insuficiencia de fundamento contractual; no es un hallazgo empírico ni una afirmación de independencia. No materialización/ejecución.
