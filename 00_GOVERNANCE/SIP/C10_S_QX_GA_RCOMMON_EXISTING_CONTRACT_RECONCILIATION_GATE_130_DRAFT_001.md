# C10-S — Gate 130: reconciliación de q_X*, g_A0/g_A1 y r_common con contratos existentes

**ID:** C10-S-QX-GA-RCOMMON-EXISTING-CONTRACT-RECONCILIATION-130  
**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** CONTRACT_SCHEMAS_ALREADY_DEFINED / q_X_HISTORY_ROWS_AND_MASSES_NOT_MATERIALIZED / g_A_PAIR_NOT_SELECTED_OR_VERSIONED / r_COMMON_SEMANTICS_DEFINED_BUT_NOT_CERTIFIED_PER_HISTORY / MATERIALIZATION_AUTHORIZATION_ABSENT / NO_NEW_CONTRACT_REQUIRED / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** DEC-C10-103; plan §§16.223, 16.226–16.227, 16.230–16.236; Gates 69, 73–86, 80, 125, 129; ledger C10-S-AB residual input and closure; DGP Temporal and Role Contract; B1 minimum DGP materialization contract; Gate 110; Gate 129.

## 1. Pregunta y dictamen ejecutivo

¿Los contratos existentes permiten especificar el mínimo operativo de q_X*, g_A0/g_A1 y r_common, y cuál es el bloqueo exacto que impide materializar theta_a_truth?

**Dictamen:** la forma semántica y el esquema documental ya están definidos. Gate 79 (§16.232) cerró el registro hijo por historia dentro del ledger padre §16.223; Gate 86 (§16.236) cerró la forma conjunta de g_A, la definición simbólica de q_X* y el significado de r_common. Gate 80 (§16.233) ya determinó que no existe roster B1/UE aprobado y materializado, no hay historias basales por unidad ni autorización de materialización en este ciclo. No falta otro contrato narrativo: faltan los objetos sintéticos aprobados/materializados que esos contratos requieren.

La auditoría Gate 130 **no selecciona** políticas g_A0/g_A1, no aprueba roster, no genera historias ni asigna masas. Declara que la dependencia está documentalmente especificada y materialmente bloqueada. Repetir el diseño de esos objetos o crear otro ledger sería duplicación.

**Resultado:** `QX_SCHEMA_CLOSED_BUT_ROWS_MASSES_ABSENT / GA_FORM_CLOSED_BUT_NO_APPROVED_OPERATIONAL_PAIR / RCOMMON_RULE_CLOSED_BUT_NO_PER_HISTORY_CERTIFICATES / ROSTER_AND_MATERIALIZATION_AUTHORIZATION_ABSENT / NO_NEW_CONTRACT_REQUIRED / NO_FREEZE`.

## 2. Fuentes existentes y adjudicación

| Fuente | Qué ya está resuelto | Qué no proporciona |
|---|---|---|
| Ledger padre §16.223.2 (Gate 69) | Campos por celda: población, asignación, intervención, efecto, funciones, held-fixed, r_common, soporte, interferencia, observación, oráculo, información Analyzer y criterio | Filas de celdas con valores y referencias materiales |
| §16.232 (Gate 79) | Registro hijo por historia: history_ref, q_X_version/mass, baseline_history_ref, schema vectorial, g_A0/1 refs y soporte, r_common_ref | Historias, masas, políticas, soporte ni certificados reales del DGP |
| §16.232.4–.5 | Masa positiva y suma 1; baseline pre-Z; vector conjunto; soporte de ambas políticas; invariancia no focal acreditada; separación Generator/Analyzer/Evaluator | Valores, filas y evidencia por historia |
| §16.230.2–.3 (Gate 77) | Candidatos deterministas extremos (0,0,0,0) y (1,1,1,1), con intervención directa y acoplamiento propuesto | Aprobación como políticas confirmatorias |
| §16.231.1–.4 (Gate 78) | Regla maestra: intervenciones conjuntas/versionadas/factibles sobre vector completo, condicionadas por historia y misma q_X*/r_common | No ratifica los extremos ni selecciona un par sustituto |
| §16.236.2–.5 (Gate 86) | Dictamen final sobre forma de g_A, q_X* y r_common; G≠g_A; ausencia de soporte | Identidades operativas de políticas, roster, historias, masas y certificados |
| §16.233 (Gate 80) | Cohorte Need censal cuando exista roster B1 aprobado; claves lógicas B1/UE/instancia; universos B1, P* y q_X* separados | Roster aprobado, filas UE/B1, snapshots X/H0/C_c y autorización |
| Gate 125 | No duplicar ledger ni expandir roster; dependencias estructurales y semánticas reales | No convierte propuestas en inputs materializados |
| Gate 129 | θ_A no materializado; Analyzer actual no lo estima; P178 es benchmark limitado | No cambia la situación de población, intervención o soporte |

## 3. q_X*: contrato definido, distribución no materializada

Se conserva la definición funcional ya vigente:

`q_X* = Law(X, H0, C_c | i ∈ P*_{τ2})`.

q_X* es una distribución objetivo conjunta de historias basales pre-Z. No es:

- la cohorte censal de Need_preZ;
- el roster B1 por sí mismo;
- el número de unidades del harness ni la distribución de `baseline_x`;
- la frecuencia observada en una simulación, el reparto Z/G ni las probabilidades de asignación `π_h`;
- el roster de perfiles R0–R3 ni el peso de una celda del benchmark.

Gate 79 ya define `history_ref` mediante las identidades y snapshots basales existentes, sin inventar una clave de historia paralela. Exige X/H0/C_c versionados, masa positiva por historia y suma de masas igual a uno. Gate 80 concluye que no hay roster B1/UE aprobado ni registros basales por unidad; el contrato B1/Need es NOT_APPROVED / NOT_MATERIALIZED. DEC-C10-096 fija el alcance censal Need cuando exista roster, pero no aprueba ni materializa el roster ni define q_X*.

**Bloqueo exacto:** ausencia de roster causal B1/UE aprobado y versionado, de snapshots/valores conjuntos pre-Z por unidad y de autorización para materializarlos. Por tanto, no existen filas válidas sobre las que definir masas q_X*. No se infieren masas de n_units, semilla, baseline_x, prevalencia Need ni frecuencias sintéticas.

## 4. g_A0/g_A1: forma definida, par operativo no seleccionado

La regla maestra de §§16.226.2.C y 16.231.1 exige dos intervenciones explícitas y versionadas sobre la **distribución conjunta del vector completo** `ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*)`, condicionadas por historia basal h, factibles y con soporte conjunto para todas las historias con masa positiva bajo la misma q_X*.

Adjudicación de antecedentes:

1. §16.230.2 introdujo como candidatos los extremos deterministas (0,0,0,0) y (1,1,1,1).
2. §16.231.1–.4 determinó que no están ratificados: la semántica de coordenadas, restricciones conjuntas, dominio y soporte por historia no acreditan su factibilidad.
3. §16.236.2 confirma que no existe otro par versionado aprobado que pueda sustituirlos y prohíbe crear kernels alternativos, distribuciones suavizadas o políticas elegidas para producir positividad.

Por ello, la forma contractual está cerrada, pero no se puede asignar `intervention_id`, versión o distribución conjunta operativa. El mecanismo G actual no es sustituto: sus cuatro coordenadas dependen de G, provisión y exógenas; representa una asignación/primera etapa, no dos intervenciones directas focales sobre el vector.

**Bloqueo exacto:** falta un par de políticas admisible y versionado; su selección depende del dominio semántico conjunto y de la factibilidad/soporte por historia, que a su vez no pueden evaluarse sin q_X* materializado. No se autoriza resolverlo eligiendo los extremos ni inventando alternativas.

## 5. r_common: regla semántica definida, certificación no disponible

§16.236.4 define r_common como las condiciones no focales idénticas en ambos potenciales: régimen de paquete Z/G según el diseño, rutas alternativas/colaterales, recursos, contexto, versiones, horizonte y mecanismos/exógenas no focales. Solo cambian los descendientes causales de la intervención focal sobre ΔT_acc*.

La regla de acreditación también está definida:

- mismo seed o acoplamiento de exógenas no basta;
- deben ser invariantes las funciones estructurales no focales y sus versiones;
- cualquier vía colateral diferencial se registra como DIFFERENTIAL_IDENTIFIED o DIFFERENTIAL_UNRESOLVED;
- no se atribuye a θ_A una diferencia no focal;
- COMMON_FIXED se certifica por historia/celda, no por etiqueta nominal de escenario.

Sin filas q_X*, políticas y potenciales por historia, no hay certificados por historia/celda. R0–R3 no garantizan invariancia por su etiqueta.

**Bloqueo exacto:** ausencia de las historias/potenciales versionados y de la pareja operativa g_A que permita contrastar invariantes no focales. La regla no requiere otra definición, pero su cumplimiento no puede adjudicarse ahora.

## 6. Tres estados de soporte y separación de roles

Se conserva la separación de §16.232.3:

1. **Factibilidad estructural:** la política conjunta está dentro del dominio y respeta restricciones del vector para una historia.
2. **Evaluabilidad contrafactual del Generator:** el DGP puede calcular el potencial bajo esa intervención con las exógenas/dependencias requeridas.
3. **Soporte de identificación del Analyzer:** la asignación y evidencia sellada contienen variación/positividad suficiente para identificar el contraste en la población objetivo.

Ningún estado implica los otros. Que Generator pueda computar un potencial no demuestra soporte observacional; que el Analyzer vea una asignación aleatoria G no demuestra que haya observado las intervenciones g_A. UNKNOWN no se transforma en PASS, y la falta de soporte no se repara con extrapolación o recorte retrospectivo de q_X*.

## 7. ¿Qué impide materializar theta_a_truth?

El bloqueo es una cadena de dependencias, no una ausencia de código aislada:

`Roster B1/UE aprobado → historias X/H0/C_c y snapshots pre-Z → q_X* y masas → selección/versionado de g_A0/g_A1 → factibilidad y soporte conjunto por historia → r_common acreditable → potenciales focales → theta_a_truth`.

En paralelo, el Analyzer necesitaría una ruta de identificación observacional propia, con asignación/interferencia resueltas y evidencia sellada suficiente. El actual contraste G no completa esa ruta.

La cadena no puede saltarse:
- no calcular theta_a_truth desde G;
- no asignar masas por frecuencias del harness;
- no considerar las etiquetas R0–R3 como historias;
- no certificar r_common solo por seed compartida;
- no declarar identificación por el hecho de que Generator conozca la truth.

## 8. Dictamen y routing

**Gate 130 cierra la reconciliación documental**: no falta otro contrato para describir q_X*, la forma de g_A0/g_A1 o r_common. Los contratos y controles ya existen. Permanecen no materializados el roster/historias/masas, el par operativo de políticas y los certificados de soporte/invariancia. Gate 80 ya declara ausente la autorización de materialización en este ciclo.

No se solicita una decisión de políticas aislada del roster ni se propone materializar unidades, historias, snapshots, parámetros o potenciales sin autorización explícita. Tampoco se vuelve a abrir Gate 79/86 con otra matriz.

**Siguiente operación propuesta — Gate 131:** auditoría de suficiencia del contrato de medición/observación de `V_cont` mediante S3, reutilizando DEC-C10-099…102, el contrato integrado V_cont, P182/P183 y la matriz temporal de evidencia existente. Determinar qué parte de truth temporal, observación, error, lag, pérdida, duplicación, desorden, cobertura y adjudicación está ya especificada, qué falta para el Analyzer y qué permanece no verificable. No fijar `T*`, `Δ`, `K`, tolerancias, tasas de error, parámetros ni calibración por conveniencia. No duplicar matrices ni ejecutar.

No se modifica código, schema, roster, test register, DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o `main`. No se ejecutan validadores, tests, workflows, generación, simulaciones, calibraciones, estimaciones o experimentos.

`scientific_execution=false`  
`execution_authorized=false`
