# C10 — Registro versionado de decisiones metodológicas
**Decision log de C10-D1 / C10-S — borrador 001**

**Estado:** DRAFT / REGISTRO INICIAL — NO APROBADO  
**Corte:** 2026-11-04  
**Repositorio canónico:** `jcarmonabastida-pixel/TGCV`  
**Rama:** `research/c10-s-consolidation-draft`  
**Uso:** registrar decisiones aceptadas, propuestas, abiertas, rechazadas o sustituidas sin borrar su historia.

---

## 1. Reglas de gobernanza del registro

1. Una propuesta no es una decisión aceptada.
2. Ninguna decisión se considera aceptada sin fuente, justificación, alcance, alternativas consideradas, criterio de aceptación y acto explícito de aprobación.
3. Las decisiones científicas deben identificar si modifican C10-D1, C10-S, ambos o ninguno.
4. Una modificación de protocolo no se propaga a TGCV Core, RMA, Evidence→Claim Matrix, STATUS o claims sin proceso separado y autorización.
5. Los cambios posteriores crean una nueva entrada que sustituye o restringe la anterior; no se sobrescribe el historial.
6. Los parámetros del DGP son especificaciones sintéticas, no observaciones ni evidencia empírica.
7. No se ejecuta simulación ni experimento sin autorización expresa y gate metodológico completo.

Estados:
- **PROPUESTA:** recomendación documentada, pendiente de aprobación.
- **ABIERTA:** falta definición, evidencia o decisión.
- **ACEPTADA:** aprobada explícitamente por el responsable científico y trazable a una versión/commit.
- **RECHAZADA:** descartada con justificación.
- **SUSTITUIDA:** reemplazada por una decisión posterior, conservando el enlace histórico.
- **CONDICIONAL:** aceptada solo dentro de condiciones especificadas.
- **NO APLICABLE:** excluida justificadamente del diseño.

## 2. Registro de decisiones

| ID | Fecha | Decisión/objeto | Estado | Fuente y justificación | Dependencias / criterio de aceptación | Alcance |
|---|---|---|---|---|---|---|
| DEC-C10-001 | 2026-11-04 | Mantener `θ_A(q)` como pregunta científica de atribución C10; no sustituirla por ITT_Z | PROPUESTA | C10-D1 §§5, 17.7, 25.3–25.6, 26.2 y 30; la aleatorización de Z identifica ITT de Z, no automáticamente el efecto de accesibilidad | Aprobación explícita; política g implementable; q factible; soporte; versiones; vías alternativas; medición e identificación | C10-D1 / alcance científico |
| DEC-C10-002 | 2026-11-04 | Mantener ITT_Z como objetivo primario del diseño aleatorizado S4-R | PROPUESTA | C10-S §51.1 y C10-D1 §§25.5–25.6; ITT mide efecto de asignación de la política concreta | Definir B y versiones, población, Value, horizonte, interferencia y ausencia | C10-S / S4-R |
| DEC-C10-003 | 2026-11-04 | Mantener LATE_f como objetivo secundario de atribución local de apertura de τ2, condicionado a IV | PROPUESTA | C10-S §§43.4 y 51.5; IV identifica efecto local entre compliers bajo supuestos, no ATE | Relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia, medición y robustez a instrumento débil | C10-S / S4-R |
| DEC-C10-004 | 2026-11-04 | Declarar que S4-R no identifica por sí solo θ_A(q) poblacional ni el efecto general sobre ΔT_acc | PROPUESTA | S4-R focaliza τ2; C10-S §43.4 distingue LATE_f, θ_Af(q*) y accesibilidad TGCV general | Revisar cobertura de constructos y estimandos; no ampliar alcance sin diseño adicional | C10-S / límite de interpretación |
| DEC-C10-005 | 2026-11-04 | Mantener p0=.20 y p1=.80 como probabilidades finales post-asignación bajo B_g0/B_g1; distinguirlas de C_dep,base=0 y separar intento/éxito/estado verificado | PROPUESTA CORREGIDA | C10-S §§30.2, 31.4 y 32.4–32.5: B_g0 también es política de provisión; no hay contradicción si p0 es post-asignación | Definir si .20/.80 son probabilidades finales calibradas, mecanismo de fallos, A_f,base*, y vías colaterales; escenario adversarial separado | C10-S / DGP |
| DEC-C10-006 | 2026-11-04 | Definir P*_τ2 preasignación con A_f,base*=0 para contraste de apertura basal→post; P*_F como subgrupo funcional basal | PROPUESTA | C10-S §§43.3, 43.7 y 51.4; evita confundir apertura con nivel post y evita selección postratamiento | Definir regla de medición basal, indeterminados, F*, equivalencia funcional y adjudicación ciega | C10-S / población |
| DEC-C10-007 | 2026-11-04 | No tratar la exclusión IV como demostrada por aleatorización ni por controles negativos | CONDICIONAL / REGLA METODOLÓGICA | C10-D1 §§25.6, 26.2, 30.3 y S4-R §51.3; exclusión requiere justificación sustantiva y diseño | Escenarios adversariales con vías directas ocultas; rechazo de LATE cuando DGP viole exclusión | C10-D1 / C10-S |
| DEC-C10-008 | 2026-11-04 | No calcular Wald con primera etapa nula; ante primera etapa débil usar inferencia robusta o concluir indeterminado | PROPUESTA | C10-S §§39 y 51.7–51.8; regla inferencial necesaria | Definir estadístico/umbral, método robusto, cobertura y criterio de suficiencia antes de ejecución | C10-S / inferencia |
| DEC-C10-009 | 2026-11-04 | No declarar recuperadas las secciones 165–183 ni XSYNC sin fuente original íntegra | ACEPTADA COMO REGLA DE TRAZABILIDAD | Informe de recuperación y búsquedas GitHub documentadas; evita reconstrucción presentada como original | Mantener fuente, hash, fecha y correspondencia de cada decisión recuperada | C10-S / gobernanza documental |
| DEC-C10-010 | 2026-11-04 | No autorizar ejecución, simulación, implementación o selección de caso real por el mero avance documental | ACEPTADA COMO REGLA DE GOBERNANZA | README y gobernanza canónica; estado de autorización vigente no concede ejecución | Autorización explícita separada y gates documentales/científicos previos | Todo C10 |

## 3. Decisiones no tomadas

| ID | Objeto | Estado | Qué falta para decidir |
|---|---|---|---|
| OPEN-C10-001 | Política B y versiones del brazo control/tratamiento | ABIERTA | Acción implementable, dosis, unidad, tiempo, control, contaminación, cumplimiento y efectos colaterales |
| OPEN-C10-002 | q_X* / q_L* y soporte | ABIERTA | Población objetivo, distribución de historia, condiciones constitutivas vs variables, positividad y coherencia |
| OPEN-C10-003 | F* y equivalencia funcional | ABIERTA | Criterio de función, horizonte, sustitución, recursos, coste, calidad, latencia y seguridad |
| OPEN-C10-004 | Regla de Value | ABIERTA | Beneficiario, objetivos, escala, dimensiones, pesos, costes/beneficios, distribución, horizonte e incertidumbre |
| OPEN-C10-005 | Unidad de asignación e interferencia | ABIERTA | UE/UA, clústeres, recursos compartidos, spillovers y exposición a políticas |
| OPEN-C10-006 | Exclusión IV en el DGP principal | ABIERTA | Justificación de ausencia de vías directas; escenarios que falsen al analizador si hay vías |
| OPEN-C10-007 | Definición final de A_f* y relación con C_dep | ABIERTA | Predicados, condiciones constitutivas, estados indeterminados, versiones y validación independiente |
| OPEN-C10-008 | Contrato de ΔT_acc completo | ABIERTA | ΔU, ΔR, ΔC, identidad, equivalencia, composición, validez y snapshots |
| OPEN-C10-009 | Parámetros, N, réplicas, δ, ε y tolerancias | ABIERTA | Dimensionamiento basado en precisión, error Monte Carlo, cobertura y relevancia |
| OPEN-C10-010 | P182-01…12 y P183-01…13 | ABIERTA / FUENTE NO RECUPERADA | Fuentes originales y contratos íntegros |
| OPEN-C10-011 | XSYNC-138-01…10 | ABIERTA / FUENTE PARCIAL | Texto completo de hallazgos, revisión independiente y resolución |
| OPEN-C10-012 | Aprobación de reconciliación C10-D1 ↔ S4-R | ABIERTA | Revisión de este registro y del documento de reconciliación por responsable científico |

## 4. Alternativas descartadas o no admisibles

| ID | Alternativa | Estado | Razón |
|---|---|---|---|
| ALT-C10-001 | Reetiquetar ITT_Z como efecto de accesibilidad | NO ADMISIBLE | Confunde efecto de asignación con mediador/constructo inducido |
| ALT-C10-002 | Interpretar LATE_f como ATE o θ_A(q) poblacional | NO ADMISIBLE | Cambia población y estimando sin supuestos adicionales |
| ALT-C10-003 | Tratar D_f, A_f*, ΔT_acc y ejecución como una variable | NO ADMISIBLE | Colapsa constructos, medición y temporalidad |
| ALT-C10-004 | Tratar p0=.20 como accesibilidad basal o como probabilidad final sin distinguir intento/éxito/verificación | NO ADMISIBLE | Confunde tiempos y etapas; p0=.20 sí puede ser probabilidad final post-asignación bajo B_g0 si el mecanismo está especificado |
| ALT-C10-005 | Considerar que control negativo demuestra exclusión IV | NO ADMISIBLE | Ausencia de señal en un control no prueba ausencia de toda vía directa |
| ALT-C10-006 | Tratar PASS sintético como prueba empírica de C10 | NO ADMISIBLE | Solo valida discriminación del DGP y analizador definidos |

## 5. Protocolo para añadir una decisión

Cada nueva entrada deberá incluir:
- ID único;
- fecha y versión;
- formulación precisa de la decisión;
- alternativas consideradas;
- evidencia/fuente exacta (path, sección, blob/commit);
- justificación;
- supuestos y dependencias;
- consecuencias sobre otros artefactos;
- estado y responsable de aprobación;
- criterio de revisión o revocación.

No usar expresiones como “queda decidido”, “cerrado” o “validado” si el estado no es ACEPTADA/CONDICIONAL con aprobación trazable.

## 6. Estado

Este registro inicial formaliza propuestas y reglas de trazabilidad. Las DEC-C10-001…008 permanecen propuestas; DEC-C10-009/010 son reglas documentales y de gobernanza derivadas de las restricciones operativas existentes. No se han cerrado las auditorías AUD/XAUD, S4-R o XSYNC. No se ha ejecutado código, simulación, experimento ni análisis de datos.


## 7. Addendum de reconciliación (2026-11-04)

DEC-C10-005 se aclara: D1 mantiene p0=.20 y p1=.80 como probabilidades finales postasignación con C_dep,base=0; D2 es contraste p0=0 y p1=.80. D1 es principal solo si se justifica que la provisión ordinaria en control pertenece al comparador. Intento, éxito, verificación y accesibilidad son variables separadas.

| ID | Objeto | Estado | Criterio/pendiente |
|---|---|---|---|
| DEC-C10-011 | D1 principal condicionado; D2 contraste | PROPUESTA | Justificar comparador, política B y calibración final |
| DEC-C10-012 | q* común sobre condiciones/historias no manipuladas por g | PROPUESTA | Dominios, factibilidad y soporte |
| DEC-C10-013 | ITT_Z primario S4-R; LATE_f secundario; theta_A(q) pregunta general | PROPUESTA | Aprobación científica y cierre de supuestos |

OPEN-C10-010 se actualiza: fuente P182/P183 recuperada y criterios incorporados; fixtures/oráculos/tolerancias siguen abiertos. OPEN-C10-011: contenido XSYNC-138-01…10 localizado en el documento maestro histórico; revisión independiente y resolución siguen abiertas. OPEN-C10-012 continúa pendiente de aprobación explícita. DEC-C10-011…013 no son decisiones aceptadas.


## 8. Propuesta de operacionalización de B (2026-11-04)

Se añade DEC-C10-014 como propuesta, no como decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-014 | Operacionalización candidata de B en D1/D2 | PROPUESTA | Mismo módulo/protocolo/recursos; D1 intento .25/1; D2 intento 0/1; éxito técnico conjunto condicional a intento .80; estados finales C_dep .20/.80 y 0/.80 | Aceptar comparador D1, actor, recepción, versiones, criterios de verificación, crossover, factibilidad y exclusión |

La factorización .80 es derivada matemáticamente de las probabilidades de intento recuperadas y los estados finales objetivo; no se presenta como dato original ni como resultado. OPEN-C10-001 continúa ABIERTA. La propuesta no autoriza implementación o ejecución.


## 9. Propuesta de operacionalización de q_X* (2026-11-04)

Se añade DEC-C10-015 como propuesta, no como decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-015 | q_X* basal y soporte por historia | PROPUESTA | (P^*(X,H_0,C_c\mid E=1,C_{dep,0}=0,A_{f,0}^*=0)); ambas políticas factibles y asignación positiva por historia; L_m fuera del DGP aislado | Fijar P*, variables/estratos/pesos, inventario C_c, unidad/interferencia, probabilidades de asignación, ventanas y Value |

q_X* es una distribución objetivo, no una intervención sobre covariables. q_L* solo se requiere para variables post-asignación indispensables bajo una política secuencial explícita. No se excluye por variables postratamiento. Si una política no es factible en una historia, se restringe la población ex ante con nuevo estimando o se declara no identificación. DEC-C10-015 no cierra OPEN-C10-002 ni autoriza ejecución.


## 10. Propuesta de unidad experimental y de asignación (2026-11-04)

Se añade DEC-C10-016 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-016 | Unidad e interferencia S4-R | PROPUESTA | UE=UA=instancia sintética independiente; UO repetida T0–T9; si hay recursos/canales compartidos, definir clúster, asignación por clúster o exposición explícita; no usar ITT/Wald individual convencional con spillover no modelado | Auditar recursos, agentes, información, infraestructura, red de exposición, marco/probabilidades de aleatorización y unidad efectiva |

La propuesta no convierte no interferencia en hecho. OPEN-C10-005 sigue ABIERTA hasta auditoría de recursos y aprobación.


## 11. Propuesta de contrato F* y reconciliación de poblaciones (2026-11-04)

Se añade DEC-C10-017 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-017 | F*, substituibilidad y P*_τ2/P*_F | PROPUESTA | F* preespecificada y evaluada sin O/V; distinguir identidad, accesibilidad, aplicabilidad y substituibilidad; P*_τ2 conserva alternativas basales; P*_F exige ausencia respaldada de rutas substituibles; exclusión IV solo se compromete por vías alternativas afectadas por Z/B u otras vías directas | Criterio/tolerancias, H/G/C0, universo/cobertura, recursos, adjudicación, errores/sensibilidad, q_X,F*, pesos y revisión independiente |

DEC-C10-017 no cierra OPEN-C10-003, OPEN-C10-006 ni la exclusión IV del DGP primario.


## 12. Propuesta de contrato de medición A_f*, C_dep y ΔT_acc (2026-11-04)

Se añade DEC-C10-018 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-018 | Medición separada de accesibilidad focal y cambio transformacional | PROPUESTA | Separar truth DGP de observación; C_dep de A_f*; A_f* de App_f; D_f* de A_f*,post; T_acc/ΔT_acc estructurado de la proyección focal; clasificación observada 1/0/?; validación y cegamiento independientes | Clasificación de predicados; definición/versionado de τ2; estándares E1–E4; adjudicación/concordancia; submuestra de validación; error diferencial; cobertura y correspondencia de snapshots |

DEC-C10-018 no cierra AUD-004, XAUD-003/004 ni OPEN-C10-004. No declara validez de constructo, no aprueba el diseño y no autoriza implementación, simulación o ejecución.


## 13. Propuesta de clasificación causal de condiciones de τ2 (2026-11-04)

Se registra DEC-C10-019 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-019 | Clasificación de condiciones de accesibilidad y aplicabilidad focal | PROPUESTA | Separar componentes técnicos C_dep; autorización basal; disponibilidad de recursos/capacidad; información técnica vs conocimiento; dominio vs precondiciones S0; retirar C_other como comodín; mantener K/selección/ejecución posteriores | Revisión de cada predicado, inventario C_other, definición/versionado, ventanas temporales, evidencia, q/g y escenarios adversariales |

DEC-C10-019 no aprueba la ecuación depurada, no cierra AUD-011, XAUD-003/004, AUD-001/002 ni OPEN-C10-004 y no autoriza implementación, simulación o ejecución.


## 14. Propuesta sobre frontera del sistema y accesibilidad relacional (2026-11-04)

Se registra DEC-C10-020 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-020 | Nivel de sistema, unidad y recursos en T_acc | PROPUESTA | Tratar accesibilidad como propiedad relacional del sistema-en-relación-con-la-unidad; distinguir auxiliarmente T_cap estructural de T_acc efectivo; indexar por frontera, unidad, tiempo, recursos y contexto; mantener Core=(S,T_acc) | Frontera, unidad, niveles de asignación/medición, recursos compartidos/asignados, interferencia, proveedores externos, agregación y estimando |

DEC-C10-020 no altera el Core, no aprueba la ecuación depurada de §59, no cierra AUD-010/011, XAUD-001…004 ni OPEN-C10-004 y no autoriza implementación, simulación o ejecución.


## 15. Propuesta de unidad, frontera e intervención para C10-S (2026-11-04)

Se registra DEC-C10-021 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-021 | Configuración primaria UE/UA/frontera/Z-B | PROPUESTA | UE=UA=instancia sintética completa e independiente; UO longitudinal; B_sys contiene componentes/recursos necesarios; Z asigna política B de provisión técnica focal; q_X* define historias basales; interferencia se excluye por construcción en primario y se trata en escenarios adversariales | Inventario de frontera, acción material B, soporte q_X*, elegibilidad basal, no interferencia, vías colaterales y revisión independiente |

DEC-C10-021 no cierra OPEN-C10-005, AUD-010/011, XAUD-001/002; no cambia C10-D1/Core ni autoriza implementación, simulación o ejecución.


## 16. Propuesta de intervención material B0/B1 para C10-S (2026-11-04)

Se registra DEC-C10-022 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-022 | Política material B de provisión técnica focal | PROPUESTA | B0 mantiene configuración basal; B1 despliega/configura la dependencia técnica focal τ2, habilita su interfaz y verifica instalación/integridad/compatibilidad/operación. Z asigna la política; intento, recepción, C_dep*, A_f*, medición observada, apertura, aplicabilidad y ejecución permanecen separados. | Identidad/versiones τ2, artefacto B1, tiempos, evidencia, invariantes, fallos/contaminación, soporte q_X*, exclusión y revisión independiente |

DEC-C10-022 no cierra OPEN-C10-005, XAUD-001/002 ni los supuestos de atribución. El ITT sigue siendo efecto de asignación de política, no efecto mediado de A_f*. No autoriza freeze, implementación, simulación o ejecución.


## 17. Propuesta de contrato de medición focal y ΔT_acc (2026-11-04)

Se registra DEC-C10-023 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-023 | Medición de accesibilidad focal y cambio estructurado | PROPUESTA | C_dep* acredita provisión técnica pero no basta para A_f*. A_f* se deriva de snapshots completos y predicados ID/REL/COND/AUTH/RES/DEP/BLOCK/VALID. A_f,obs permanece separada y ciega a verdad/Z/B/O/V/selección/ejecución. D_f* es transición basal-post. ΔT_acc* conserva diff U/R/C/Validity/State; h_f es proyección focal, no sustituto del objeto completo. | Contrato τ2, cobertura, frontera, G/H, catálogo/versionado, evidencia/adjudicación, validación, error diferencial, predicados por clase y revisión independiente |

DEC-C10-023 armoniza documentalmente §§26.2, 43.3 y 58.6, pero no cierra XSYNC-138-03, AUD-001/004/005/007 ni OPEN-C10-005. No congela ni autoriza implementación, simulación o ejecución.


## 18. Propuesta de clasificación temporal-causal de condiciones (2026-11-04)

Se registra DEC-C10-024 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-024 | Clasificación temporal-causal de condiciones de accesibilidad | PROPUESTA | Clasificar cada componente por unidad/nivel/tiempo/versión y rol. Condiciones constitutivas pueden ser basales o post-Z; si cambian por B son mediadores/co-intervenciones potenciales. Elegibilidad solo pre-Z. No ajustar ITT por mediadores. Separar C_dep, C_auth, recursos, capacidad, información técnica, dominio, App_f, conocimiento, selección, ejecución y proceso de medición. | §§59, 62–64; DGP §§2–23; AUD-011; XAUD-003/004/006; OPEN-C10-004/005 |

**Advertencias registradas:** (i) §62 describe B0/B1 como ausencia frente a provisión, mientras DGP §3.1 mantiene probabilidades objetivo .20/.80; contratos no armonizados. (ii) la propuesta histórica de intervención sobre C_auth no equivale al diseño primario de provisión técnica con C_auth basal/invariante. DEC-C10-024 no decide estas discrepancias ni cierra AUD-011/XAUD-003/004/006.


## 19. Propuesta de reconciliación de política B y escenarios D1/D2 (2026-11-04)

Se registra DEC-C10-025 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-025 | Semántica de B, distinción D1/D2 y factorización de provisión | PROPUESTA | D1 es control ordinario de baja frecuencia frente a provisión programada; D2 es control sin provisión frente a provisión programada. W_attempt: D1 .25/1; D2 0/1. S_success condicional .80 es propuesta algebraica. C_dep final: D1 .20/.80; D2 0/.80. D1 principal solo si se justifica el comparador; C_dep no sustituye A_f*/D_f*. | Maestro §§53–54, 62–65; DGP §§3.1–3.2, 21–24; S4-R §§16–17; OPEN-C10-001/005 |

DEC-C10-025 aclara la semántica documental, pero no aprueba D1, D2 ni el .80 condicional, no cierra OPEN-C10-001/005 y no autoriza freeze, implementación, simulación o ejecución.


## 20. Propuesta de adjudicación del comparador D1/D2 (2026-11-04)

Se registra DEC-C10-026 como recomendación de diseño, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-026 | Legitimidad del comparador y selección primaria D1/D2 | PROPUESTA | El expediente no acredita que .25 intentos/.20 estado final representen el régimen ordinario de la población objetivo. D1 se conserva como contraste incremental secundario hasta justificarlo. D2 se recomienda provisionalmente como candidato preferente para el objetivo mecanístico sintético de provisión focal frente a ausencia de intento. ITT y LATE se mantienen específicos por escenario; no se agrupan. La selección primaria sigue abierta. | Maestro §§52–54, 65–66; DGP §§24–25; S4-R §§17–18; OPEN-C10-001/005 |

DEC-C10-026 no aprueba D2 ni D1, no valida .80, no cierra OPEN-C10-001/005 y no autoriza freeze, implementación, simulación o ejecución.


## 21. Propuesta de calibración de la primera etapa y accesibilidad (2026-11-04)

Se registra DEC-C10-027 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-027 | Conjunción técnica, éxito condicional y derivación de accesibilidad | PROPUESTA | C_dep*=C_install*∧C_integrity*∧C_compat*∧C_oper*. El .80 es probabilidad conjunta condicional de éxito de esa ruta tras intento elegible, no tasa marginal por componente ni dato empírico. A_f* requiere ID/REL/COND/AUTH/RES/DEP/¬BLOCK; VALID es epistémico y App_f separado. C_dep equivale a DEP_f solo bajo ruta única estipulada. Las primeras etapas C_dep/A_f/D_f se calculan separadamente; .60 (D1) y .80 (D2) solo coinciden bajo elegibilidad basal y predicados restantes satisfechos e invariantes. | Distribución conjunta de componentes, sensibilidad de .80, protocolo/actor/versiones, rutas alternativas/cobertura, evidencia/adjudicación, errores diferenciales, q_X*/soporte y revisión independiente |

DEC-C10-027 formaliza una propuesta de medición y mecanismo, no valida la tasa .80 ni selecciona D2. No cierra OPEN-C10-001/007/008, AUD-001/004/005/007/010/011 ni XSYNC-138-03/04/06. No autoriza freeze, implementación, simulación o ejecución.


## 22. Propuesta de distribución conjunta y sensibilidad (2026-11-04)

Se registra DEC-C10-028 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-028 | Distribución de cuatro componentes | PROPUESTA | Definir tabla de 16 patrones (p_{abcd}), con s=p1111. s=.80 no identifica marginales ni fallos parciales. Incluir sensibilidad de dependencia (choque común, fallos parciales, bottleneck, mixta), heterogeneidad y deriva de versiones. Malla exploratoria s={.60,.70,.80,.90}, sin privilegiar .80. | Protocolo/denominador de intentos, marginales y fallos parciales, dependencia, heterogeneidad, versiones, revisión independiente |

DEC-C10-028 demuestra la insuficiencia de s para determinar el mecanismo completo; no selecciona una distribución, no valida parámetros, no aprueba D1/D2 como primario ni autoriza ejecución.


## 23. Propuesta de fixtures y propagación de s (2026-11-04)

Se registra DEC-C10-029 como propuesta, no decisión aceptada:

- Cuatro fixtures con s=.80: choque común, fallos simples dispersos, bottleneck instalación y fallos emparejados.
- Se conservan las 16 celdas por tabla; los cuatro fixtures comparten s pero producen marginales y patrones de fallo diferentes.
- Para la malla s=.60/.70/.80/.90 se escala la masa residual 1−s según cada estructura; esta familia cambia marginales y no mantiene marginales fijas.
- Bajo una oportunidad de intento y las políticas candidatas D1 q0=.25/q1=1 y D2 q0=0/q1=1, con éxito condicional común s: FS_Cdep,D1=.75s y FS_Cdep,D2=s.
- El estado D1 control=.20 se deriva de .25×.80; no debe tratarse como constante independiente al variar s.
- Las igualdades con FS_Af/FS_Df siguen condicionadas a §67.4.

DEC-C10-029 no selecciona distribución confirmatoria, escenario primario ni s, y no autoriza freeze/implementación/simulación/ejecución.


## 24. Propuesta de reconciliación de arquitectura causal y estimandos (2026-11-04)

Se registra **DEC-C10-030** como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-030 | Arquitectura causal C10-D1/S4-R, régimen q, intervención B y C_auth | PROPUESTA | Preservar θ_A(q) como pregunta científica C10-D1; distinguir TE_Z/ITT_Z de efecto de política ψ_B y LATE_f local. q_X* es candidato como distribución basal común; q_L* solo si se requiere régimen secuencial explícito. Se recomienda para revisión una intervención material de provisión técnica B con C_auth basal, elegible e invariante; si B cambia autorización u otras vías hacia O/V, reportar efecto de paquete salvo identificación adicional. La selección D1/D2 permanece abierta. | Aprobación de jerarquía de estimandos; q_X*/soporte; población, horizonte y Value; definición final B/g0/g1; resolución C_auth; comparador; unidad/interferencia; vías directas; revisión independiente. |

DEC-C10-030 documenta una reconciliación candidata y no acepta ni congela la Candidata A. No cierra OPEN-C10-001/002/005/006, AUD-001/002/011, XAUD-001/002/003/004/006 ni XSYNC-138. No autoriza implementación, simulación o ejecución.


## 25. Propuesta de reconciliación de población, F* y notación basal (2026-11-04)

Se registra **DEC-C10-031** como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-031 | P*_τ2/P*_F, F*, D_f,0 y D1/D2 | PROPUESTA | P*_τ2 requiere elegibilidad constitutiva pre-Z, C_dep,0=0 y A_f,0*=0; P*_F añade F_alt,0=0 respaldado. F* se define ex ante sin O/V y con S0, objetivo, restricciones, tolerancias, H/G/C0 y evidencia. En notación nueva, C_dep,0 es dependencia basal y D_f* es transición I(A_f,0*=0∧A_f,1*=1); no usar D_f,0 para disponibilidad basal. D1 histórico principal condicionado y D2 mecanístico provisional se conservan como recomendaciones en conflicto de precedencia; selección primaria abierta. | Fichas y umbrales constitutivos; universo/cobertura de alternativas; operacionalización F*; revisión de notación global; evidencia externa D1 o justificación del objetivo D2; población/unidad/interferencia; revisión independiente. |

DEC-C10-031 no acepta la población, no cierra OPEN-C10-001/003/005/007, no selecciona D1/D2 y no autoriza freeze, implementación, simulación o ejecución.


## 26. Propuesta de separación de ΔT_acc estructural y ΔE_T epistémico (2026-11-04)

Se registra **DEC-C10-032** como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-032 | Snapshots, ΔT_acc y validez de evidencia | PROPUESTA | Definir S_T*=(U*,R*,C*,X*) como snapshot estructural; E_T como paquete de evidencia/cobertura/validez epistémica; ΔT_acc*=Diff(S_T*(t0),S_T*(t1))=(ΔU*,ΔR*,ΔC*,ΔX*); ΔE_T registra cambios epistémicos. ΔValidity_e se retira de la tupla causal; validez estructural real permanece en C*/R*. Correspondencia ID/versiones/frontera/G es requisito previo al diff. | Aprobación formal; propagación global; catálogo/IDs/G/frontera; mapping por versión; verdad oculta/observación; fixtures/oráculos; validación de error diferencial; revisión independiente. |

DEC-C10-032 propone superseder, no borrar, la formulación de §63.7. No cierra AUD-001/004/005/007, XAUD-003/004/006 ni XSYNC-138-03/06; no autoriza freeze, implementación, simulación o ejecución.


## 27. Propuesta de contrato de identidad y matching de snapshots (2026-11-04)

Se registra **DEC-C10-033** como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-033 | Identidad semántica, versiones y matching | PROPUESTA | Separar TID/SID/RID/EID; IDs opacos persistentes; continuidad por firma contractual; split/merge explícito; matching jerárquico sin auto-merge fuzzy; diff solo con frontera/G/catálogo/mapping compatibles; D_f* requiere correspondencia de τ2. | Taxonomía mínima aprobada; catálogo y serialización; firma/tolerancias por clase; G/frontera DGP; fixtures/oráculos ID-01…15; revisión independiente. |

No cierra AUD-004 ni XSYNC-138-03/06. No autoriza freeze, implementación, simulación o ejecución.


## 28. Propuesta de contrato de alcanzabilidad y trayectorias (2026-11-04)

Se registra DEC-C10-034 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-034 | Reach_H y propagación de trayectorias | PROPUESTA | Separar Reach_H* y Reach_H,obs; usar lógica 1/0/? por ruta y disyunción entre alternativas; una ruta confirmada basta para Reach=1; Reach=0 requiere cobertura exhaustiva; truncamiento/cobertura incompleta/mapping ? producen indeterminación; selección/ejecución/Outcome/Value no definen Reach. | Catálogo/estados/objetivos DGP; G/H; reglas composicionales; recursos/ciclos; snapshots dinámicos; fixtures/oráculos REACH-01…20; revisión independiente. |

No cierra AUD-005 ni AUD-007. No autoriza freeze, implementación, simulación o ejecución.


## 29. Propuesta de inventario finito del DGP y mapa de cobertura (2026-11-04)

Se registra DEC-C10-035 como propuesta, no decisión aceptada:

| ID | Objeto | Estado | Formulación | Dependencias |
|---|---|---|---|---|
| DEC-C10-035 | Universo finito candidato para Reach | PROPUESTA | Fixture abstracto S0/S1/S2/SF; rutas focal F1→F2 y alternativa A1→A2; escenarios R0 exclusivo, R1 alternativa basal, R2 alternativa afectada y R3 fallo; G atómica y H=3 candidatos. La apertura focal no implica Reach(SF), y la ruta alternativa puede mantenerlo alcanzable. La no alcanzabilidad/ausencia de alternativa exige cobertura exhaustiva en ocho dimensiones. | Aprobación de frontera/G/H; F* y criterio GOAL_F; identidad τ2; recursos/condiciones; escenario y comparador primario; evidencia E1–E4, cobertura, oráculos y revisión independiente. |

DEC-C10-035 es una topología de fixture para revisión. No canoniza TID, no selecciona D1/D2, no valida F*, no cierra AUD-005/007 y no autoriza freeze, implementación, simulación o ejecución.


## 30. Reconciliación propuesta de horizonte y escenarios (2026-11-04)

Se registra DEC-C10-036 como propuesta, no decisión aceptada: distinguir reloj del estudio t0–t9, profundidad de ruta k=0…H y tiempo/ventanas de factibilidad. H=3 se interpreta provisionalmente como profundidad máxima candidata, no duración temporal. Reach se calcula en t4 sobre snapshot t3, antes de K/Sel/Exec; dinámica por rama requiere snapshots inmutables y reglas explícitas. Crosswalk R0/R1/R2/R3 ↔ S4R-A/B/C/D. Dependencias: ratificación de H, duración/ventanas, actualización de estados hipotéticos, recursos, F*, cobertura, D1/D2 y oráculos.

DEC-C10-036 no cierra AUD-005/007, no selecciona parámetros ni autoriza freeze, implementación, simulación o ejecución.


## 31. Matriz operacional de predicados (2026-11-05)

Se registra DEC-C10-037 como propuesta de operacionalización: evaluar por paso y rama ID, ACC, APP, REL, COND, AUTH, RES, DEP, BLOCK, WIN y COV; fijar T_acc/snapshot estructural en t3 para fixture base; evaluar APP por estado hipotético de entrada; y no permitir cambios intrarrama sin regla DGP versionada y snapshot inmutable. Las ramas focal y alternativa se consideran potenciales contrafactuales separadas, no consumos simultáneos. Se incorpora taxonomía I/S/T/R/D/E y contratos PM-01…18.

No se asignan valores por escenario ni se ratifican F*, G/H, recursos, ventanas, D1/D2 o cobertura. DEC-C10-037 no cierra AUD-004/005/007/010/011 ni autoriza implementación, simulación o ejecución.


## 32. Reconciliación de fichas transformacionales (2026-11-05)

Se registra DEC-C10-038 como propuesta de control semántico. Se reutilizan las definiciones existentes de §§47–51 y 57–69. F1=τ2 focal está parcialmente especificada; F2/A1/A2 solo son aliases con transiciones topológicas S2→SF, S0→S1 y S1→SF. SF no constituye una definición operacional de F*. No asignar operaciones, precondiciones o recursos ficticios a los aliases. El hueco se resolverá con una propuesta explícita de microdominio sintético que permita una F* común y rutas focal/alternativa genuinas.

DEC-C10-038 no aprueba el microdominio, no completa las fichas sustantivas, no cierra AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007, y no autoriza freeze, implementación, simulación o ejecución.


## 33. Recomendación comparativa de microdominio (2026-11-05)

Se registra DEC-C10-039 como recomendación, no decisión aceptada. Se comparan tres opciones: migración de configuración software, integración de datos y flujo organizativo. Se recomienda Opción A para revisión: F1 conversión mediante adaptador focal provisionado por B; F2 aplicación y validación en destino; A1 exportación a formato neutral baseline; A2 importación/aplicación por mecanismo nativo; F* conformidad técnica de esquema/integridad/compatibilidad. Ventajas: separación provisión/ejecución, precondiciones diferenciables, alternativa genuina, control de recursos/ventanas e interferencia menor.

La selección sigue abierta. Deben aprobarse F*, propiedades de preservación, independencia A1/A2, identidades/versiones, recursos, autorizaciones, ventanas, R0–R3 y evidencia. DEC-C10-039 no selecciona D1/D2, no fija parámetros ni autoriza freeze/implementación/simulación/ejecución.


## 34. Auditoría causal de Opción A — DEC-C10-040 (recomendación condicionada)

DEC-C10-040 registra que Opción A es potencialmente compatible pero no demuestra intervención autónoma sobre A_f* ni identifica θ_A(q). Se requiere separar B/provisión, C_dep, A_f*, F1 como conversión ejecutada, App, F2, F* y ejecución. Se rechaza la formulación ambigua de F1 como “habilitar y utilizar” adaptador: habilitar pertenece a B; convertir pertenece a F1.

La política B puede abrir vías colaterales por permisos, recursos, estado/configuración, seguridad, coste, latencia, información, librerías o dependencias compartidas. Se requiere manifiesto de cambios y grafo de dependencias. A1/A2 deben ser no afectadas por B en R0/R1; si son afectadas, R2/vía colateral y efecto de paquete. D1/D2 permanece abierto. Se mantiene Opción A como recomendación condicionada, no seleccionada ni aprobada. DEC-C10-040 no autoriza freeze, implementación, simulación ni ejecución.


## 35. Manifiesto B y arquitectura aislada — DEC-C10-041 (recomendación condicionada)

Se registra la recomendación de evaluar ARCH-B1: provisionar el adaptador focal como sidecar/runtime separado, aditivo, con versiones fijadas, permisos mínimos, cuotas y canal explícito. No es una decisión de instalación ni de implementación. B no debe ejecutar F1/F2/A1/A2 ni cambiar F*, oráculo, datos fuente/destino, C_auth funcional o ruta alternativa.

Se crea C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md con catálogo B-M01…15, clases de dependencia, snapshots, criterios de reversibilidad y no-afectación, y contratos PROV-01…12. Todas las superficies técnicas permanecen NO INVENTARIADO hasta aportar evidencia; no significa que no cambien. MD-C1/MD-C4 abiertos. DEC-C10-041 no selecciona definitivamente microdominio, no decide D1/D2 y no autoriza instalar, implementar, simular o ejecutar.


## 36. Universo candidato y cobertura trivalente — DEC-C10-042

Se registra U_G como catálogo finito candidato de inspección (23 roles de nodo, 23 aristas, predicados y cinco clases de ruta), no como universo técnico real/exhaustivo. Todos los estados técnicos permanecen indeterminados y la cobertura efectiva es NONE hasta disponer de inventario real, SBOM, runtime, snapshots y grafo de dependencias transitivas.

Se adopta como regla documental que MISSING/PARTIAL no equivalen a 0; ruta=0 exige evidencia válida y cobertura suficiente; Reach=0 exige descarte exhaustivo de rutas; F_alt,0=0 exige descarte exhaustivo de alternativas funcionalmente substituibles. Runknown permanece como clase abierta. Reach_H=?, F_alt,0=?, A_f*=?; R0/R1 no clasificables, R2 posible pero no observado. No se aprueba DGP, microdominio, comparador ni ejecución.


## 37. Plantilla de inventario U_G — DEC-C10-043 (propuesta documental)

Se crea C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md como esquema vacío para registrar nodos, aristas/dependencias, rutas, predicados, snapshots/fuentes y cobertura. Se exige procedencia, identidad/versionado, estado observado 1/0/?, cobertura, evaluador/cegamiento y motivo de indeterminación. La truth del DGP queda restringida al generador/evaluador independiente.

DEC-C10-043 es una propuesta de instrumento documental, no una decisión de inventario ni una aprobación del DGP. No se completan componentes, rutas, dependencias, versiones o valores de truth; cobertura NONE y A_f*, F_alt,0 y Reach_H permanecen ?. No cierra auditorías ni OPEN-C10; no autoriza inspección técnica, implementación, simulación o ejecución.


## 38. Reconciliación U_G/plantilla — DEC-C10-044 (hallazgo documental)

Se registra el crosswalk 23/23 nodos, 23/23 IDs padre de arista, 14/14 predicados y 5/5 clases de ruta entre §81 y la plantilla. Se determina que E07 debe ser regla lógica y no arista técnica; las relaciones mult destino se normalizan a 39 filas binarias candidatas. E22 carece de destinos identificados como nodos/eventos. N16 y N23 son roles compuestos que requieren desagregación analítica.

DEC-C10-044 es un hallazgo/recomendación documental, no decisión sobre topología real, DGP o microdominio. Se amplía la plantilla con campos de procedencia/evidencia/cobertura/adjudicación. Esquema no cerrado; todos los estados técnicos ? y cobertura NONE. No autoriza inventario real, implementación, simulación ni ejecución.


## 39. Protocolo de evidencia U_G — DEC-C10-045 (propuesta documental)

Se registra la creación de C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md. Define S1–S8, procedencia, evidencia mínima por objeto, argumentos de cobertura negativa, denominadores, doble evaluación cegada, adjudicación independiente y propagación trivalente.

DEC-C10-045 es propuesta documental, no aprobación de fuentes, microdominio, procedimiento de inspección ni ejecución. No hay evidencia observada ni inventario; cobertura NONE, A_f*, F_alt,0 y Reach_H siguen ?. Requiere auditoría campo-a-campo de la plantilla y definición contextual de denominadores, evaluadores, seguridad, oráculo y tolerancias. No autoriza inspección real, implementación, simulación o experimento.


## 40. Auditoría de esquema U_G — DEC-C10-046 (hallazgo y corrección documental)

Se identifican nueve brechas FCM-01…09 entre el protocolo de procedencia y las tablas de la plantilla: ausencia de registro separado de evidencia y vínculo claim-evidence, cobertura sin denominador, falta de doble evaluación y adjudicación estructuradas, exposición de truth DGP en la tabla analítica, mezcla de clases de ruta/subtipos y ausencia de campos comunes/integridad referencial.

Se incorporan registros normalizados y segregación de truth en la plantilla §§12–13 y se actualiza el protocolo §13. DEC-C10-046 registra la corrección documental y la necesidad de revisión independiente/validación de tipos y constraints; no aprueba el esquema para uso, no acredita seguridad efectiva y no autoriza inspección, implementación, simulación o ejecución.


## 41. Segunda pasada de consistencia del esquema U_G — DEC-C10-047

Se registran FCM-10…16: campos comunes no materializados en las tablas, NA en snapshots, referencia singular de evaluador, cardinalidad de evidencia, cobertura resumen vs registro normativo, dominios/tipos y destino de claim_target_id. La plantilla se actualiza con campos físicos, diccionario candidato y matriz de obligatoriedad; CLAIM_EVIDENCE_LINK queda como relación 1:N y E1/E2 como filas separadas.

DEC-C10-047 es hallazgo/corrección documental. No declara esquema cerrado, no aprueba implementación ni acredita validación técnica, seguridad o cegamiento. No autoriza inventario real, parser, simulación o ejecución.


## 42. Normalización relacional de evaluación/evidencia — DEC-C10-048

Se corrigen FCM-17…19: EVALUATOR_ASSESSMENT usa evaluator_record_id singular; ADJUDICATION_REGISTER apunta a object_record_id y conserva referencias E1/E2; CLAIM_EVIDENCE_LINK asocia evidencias a evaluadores/adjudicaciones sin listas serializadas. Se registra comprobación estática de alineación de columnas de diez tablas.

DEC-C10-048 es una corrección documental, no validación ejecutable ni aprobación de esquema. No acredita integridad referencial, seguridad, cegamiento o inventario técnico.


## 43. Preparación de revisión independiente U_G — DEC-C10-049

Se crea C10_S_UG_SCHEMA_INDEPENDENT_REVIEW_CHECKLIST_DRAFT_001.md, que define SR-01…20, perfiles R1/R2, independencia, cegamiento, procedimiento y dictamen. La revisión está preparada pero NO INICIADA. No se designan revisores ni se declara aceptabilidad del esquema. FCM-01…19 y XSYNC-138-01 permanecen abiertos; el freeze y la selección del microdominio quedan condicionados a revisión y validación pertinentes.

DEC-C10-049 es registro de preparación documental; no autoriza parser, validación ejecutable, inspección, simulación o experimento.
