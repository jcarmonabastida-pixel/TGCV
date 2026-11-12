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


## 44. Cardinalidad de evidence_ref y evaluación independiente — DEC-C10-050

Se decide como convención documental candidata: evidence_ref en objetos admite cero o un vínculo de navegación opcional; CLAIM_EVIDENCE_LINK conserva la relación completa 0..n, también por evaluador/adjudicador. EVALUATOR_ASSESSMENT conserva evaluator_record_id singular por fila; evaluator_record_ids plural en objetos es solo una vista/resumen opcional. Se corrige FCM-12 y se registra FCM-20.

DEC-C10-050 es reconciliación documental, no aprobación/freeze del esquema ni validación ejecutable.


## 45. Selección del microdominio y contrato funcional de trabajo — DEC-C10-051 (2026-11-05)

**Decisión:** se selecciona Opción A, migración de configuración entre dos entornos software, como microdominio de diseño y operacionalización de C10-S. Se adopta F* como contrato funcional de trabajo candidato: la ruta completa produce y aplica en el destino una configuración conforme a propiedades obligatorias preespecificadas de esquema, integridad, compatibilidad, preservación funcional y seguridad.

**Alcance:** esta decisión resuelve la selección entre opciones de microdominio para el diseño documental. Opción B/C quedan como alternativas históricas. La adopción de F* no cierra todavía su lista de propiedades, mappings, tolerancias, casos frontera ni oráculo.

**No implica:** aprobación de ejecución; selección de D1/D2; cierre de R0–R3; identificación causal; inventario real de componentes; parámetros de versiones/recursos/ventanas; validación técnica; revisión independiente; freeze o cambio de main.

**Siguiente trabajo:** cerrar el contrato operacional F*, fichas F1/F2/A1/A2, mappings, condiciones y oráculo; después completar DGP y análisis de identificación.


## 46. Selección del objeto de configuración — DEC-C10-052 (2026-11-05)

**Decisión:** se selecciona la clase A, paquete de configuración de un servicio software, como objeto concreto de trabajo dentro del microdominio Opción A ya adoptado por DEC-C10-051. Se adoptan como estructura conceptual inicial los seis elementos: componente; parámetros tipados; referencias; reglas/restricciones; políticas asociadas; metadatos contractuales.

**Alcance:** selección para diseño documental y especialización de FP-03. Los seis elementos son estructura inicial, no esquema final ni afirmación de obligatoriedad universal. Se mantiene separada la configuración declarada de recursos, permisos efectivos, dependencias instaladas y estado del entorno, provisión B, transformación/ejecución y Outcome/Value.

**No implica:** contratos fuente/destino cerrados; propiedades atómicas obligatorias; mappings o tolerancias aprobados; semántica concreta de F1/F2/A1/A2; TID/SID/RID; oráculo validado; implementación; inventario real; validación técnica; revisión independiente; evidencia empírica; freeze o autorización de ejecución. `scientific_execution=false`; `execution_authorized=false`.

**Siguiente trabajo:** especializar SM-01…SM-10, determinar obligatoriedad/aplicabilidad, definir invariantes y mappings atómicos y reconciliar las fichas de transformación con el historial.


## 47. Aprobación de la partición del DGP base — DEC-C10-053 (2026-11-05)

**Decisión explícita:** se aprueba el alcance mínimo propuesto para el DGP base:
- constitutivos: componentes, parámetros tipados, referencias y reglas/restricciones con gramática mínima;
- políticas asociadas (POL): módulo/escenario condicional secundario, fuera del núcleo confirmatorio mínimo;
- metadatos contractuales: soporte obligatorio para identidad, versionado y procedencia; extensiones desconocidas condicionales.

La decisión no modifica la estructura conceptual de seis elementos de DEC-C10-052: POL sigue perteneciendo al objeto conceptual, aunque no sea constitutivo del escenario base. La ausencia de políticas migrables deberá declararse ex ante, nunca inferirse después de observar resultados.

**No cierra:** gramática, dominios de tipos/parámetros, cardinalidad/direccionalidad, semántica ausencia/null/default, mappings, tolerancias, oráculo ni DGP completo. No hay truth, fixtures, validación técnica, revisión independiente, evidencia empírica ni autorización de ejecución.


## 48. Perfil finito de dominios y complejidad de reglas — DEC-C10-054 (2026-11-05)

**Decisión explícita:** el usuario aprueba el perfil estructural de dominios finitos por clave y el presupuesto de complejidad del DGP base propuesto en `C10_S_FINITE_DOMAIN_AND_RULE_COMPLEXITY_PROFILE_PROPOSAL_DRAFT_001.md`:
- dominios finitos declarados por clave/parámetro, sin imponer rangos universales arbitrarios;
- BOOL binario; INT finito o intervalo entero cerrado; DECIMAL escalado con precisión/redondeo explícitos; ENUM y REF cerrados/versionados; STRING acotado y normalización explícita;
- distinción ABSENT/NULL/DEFAULT/VALUE y separación de DEFAULT_DECLARED, DEFAULT_INHERITED y DEFAULT_ENV_RESOLVED;
- AST declarativo acíclico, sin bucles, recursión, macros, llamadas externas, I/O, reloj real ni efectos laterales;
- operadores tipados EQ/NEQ/LT/LE/GT/GE/IN/NOT_IN, predicados de estado y referencia; composición NOT/AND/OR con precedencia declarada;
- límites de complejidad: profundidad máxima 4, 16 átomos por regla y 16 reglas por paquete;
- efectos del núcleo limitados a REQUIRE/FORBID; SELECT_ENUM_VALUE queda fuera del núcleo confirmatorio y reservado a extensión separada;
- UNKNOWN no se convierte silenciosamente en TRUE/FALSE; propagación a F* conforme al perfil aprobado.

**Alcance y reservas:** se aprueba el perfil estructural y los límites 4/16/16 como presupuesto inicial, no su calibración empírica. No se aprueban todavía límites numéricos, escalas, catálogos, longitudes o valores concretos por clave: deberán derivarse del contrato abstracto y quedar declarados ex ante. Tampoco se cierra la política de conflictos entre reglas, mapping completo, tolerancias ni oráculo.

**No implica:** gramática implementada; parser validado; contrato fuente/destino cerrado; FP-01/02/03 cerrados; truth, fixtures o datos generados; revisión independiente; evidencia empírica; ejecución autorizada; freeze del DGP o cambio de main. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

**Siguiente trabajo:** construir el contrato abstracto de parámetros por clave y la matriz de correspondencias C_src→C_dst/M, vinculando cada predicado con FP-01 (estructura/tipos), FP-02 (integridad relacional) y FP-03 (preservación semántica), con regla de predicado primario para evitar doble conteo.


## DEC-C10-055 — aceptación de reconciliación SM/FP (2026-11-05)

**Decisión explícita del usuario:** se acepta la propuesta de reconciliación de SM-01…SM-10, catálogo atómico CMP/PAR/REF/RUL/POL/MET y familias FP-01…FP-08 contenida en `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`.

**Alcance aceptado:** separar estructura formal FP-01, integridad relacional FP-02, preservación semántica FP-03, compatibilidad FP-04, seguridad FP-05, aplicación FP-06, verificación post-aplicación FP-07 y procedencia/reproducibilidad FP-08; descomponer predicados compuestos; fijar un predicado primario y evitar doble conteo; preservar la distinción entre paquete declarado, estado aplicado y entorno; mantener POL condicional y no inferir seguridad por preservación de política.

**Límite:** la aceptación valida la arquitectura de reconciliación, no convierte todos los predicados candidatos en confirmatorios ni resuelve obligatoriedad/NA por instancia. Se mantienen las decisiones DEC-C10-052/053/054 y sus alcances.

**Siguiente operación:** elaborar la matriz ex ante de obligatoriedad y aplicabilidad por propiedad, con IAM previo a Z/B, condiciones verificables para NA, cardinalidades explícitas, separación F* funcional/gates técnicos/FP-08 probatorio y controles contra decisiones post hoc.

No implica implementación, validación, truth, fixtures, revisión independiente, evidencia empírica, freeze ni ejecución. `scientific_execution=false`; `execution_authorized=false`.


## DEC-C10-056 — cardinalidad de clases del DGP base (2026-11-05)

**Decisión explícita del usuario:** acepta la política de cardinalidad propuesta para el paquete de configuración del microdominio Opción A.

- CMP ≥ 1: al menos un componente; CMP=0 es SCOPE_ERROR.
- PAR ≥ 1: al menos un parámetro; PAR=0 es SCOPE_ERROR.
- REF ≥ 0: puede estar vacío solo si IAM lo declara ex ante y la cobertura del inventario es exhaustiva; incertidumbre de cobertura se mantiene como ?.
- RUL ≥ 1: al menos una regla/restricción; RUL=0 es SCOPE_ERROR en el DGP base confirmatorio.
- POL ≥ 0: ausente por diseño en el núcleo confirmatorio mínimo; si se incorpora, debe declararse como módulo condicional antes de Z/B.
- MET obligatorio: identidad, versionado, procedencia y trazabilidad/IAM.

**Alcance:** fija cardinalidades de clase, no máximos, clases concretas, claves/valores, reglas sustantivas, topología del servicio ni mapping final. Un cambio del contrato de unidad para permitir CMP/PAR/RUL vacíos requeriría rediseño y aprobación antes de generar/asignar instancias; no puede decidirse post hoc.

**Artefacto derivado:** `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`, propuesta documental que formaliza estructura e invariantes sin constituir schema ejecutable.

No implica implementación, truth, fixtures, validación técnica, revisión independiente, evidencia empírica, freeze ni ejecución. `scientific_execution=false`; `execution_authorized=false`.


## Propuesta de frontera P0/P1/P2 — pendiente de decisión del usuario (2026-11-05)

Se crea `C10_S_SOFTWARE_SERVICE_CONFIGURATION_BOUNDARY_PROFILE_PROPOSAL_DRAFT_001.md`. Propone tres perímetros: P0 paquete declarativo migrable C (CMP/PAR/REF/RUL/POL?/MET); P1 envolvente técnica E_src/E_dst (software/runtime, recursos, permisos efectivos, servicios, estado y mecanismos de aplicación); P2 sistema causal de la unidad (P0+P1, B, alternativas, dependencias compartidas, agentes, medición, ejecución y Outcomes/Value pertinentes).

La propuesta distingue declaración REF de disponibilidad real del recurso, POL de permisos efectivos, C_dst_decl de C_dst_applied y mapping M del contenido fuente. Incluye reglas para secretos, endpoints, deployment manifests, datos persistentes, sidecar B, alternativas A1/A2 y oráculo. La unidad experimental permanece candidata y no se redefine.

**Estado:** propuesta documental no aceptada ni congelada; no se crea DEC-C10-057 hasta decisión explícita. Sin inventario real, snapshots, IAM instanciado, truth, fixtures, validación, instalación ni ejecución.


## DEC-C10-057 — arquitectura de frontera P0/P1/P2 (2026-11-05)

**Decisión explícita del usuario:** acepta la arquitectura de tres perímetros y la regla de clasificación semántica, no basada en formato/ubicación.

- **P0:** paquete declarativo de configuración migrable del servicio (CMP/PAR/REF/RUL/POL?/MET).
- **P1:** envolvente técnica/estado de los entornos fuente y destino (runtime, software, recursos, permisos efectivos, servicios, estado y aplicación).
- **P2:** frontera analítica causal que integra los elementos P0/P1 pertinentes y además B, alternativas, dependencias compartidas, agentes, medición, ejecución y resultados.

P0/P1 son clases de objeto/contexto; P2 es una frontera analítica transversal, no una tercera clase mutuamente excluyente. Se distinguen declaración de referencia y disponibilidad real, POL declarada y permisos efectivos, configuración declarada y aplicada, y mapping M del paquete fuente.

La aceptación valida la arquitectura y la regla general, no clasifica automáticamente cada deployment manifest, variable, secreto, dato persistente o servicio externo. Esas aplicaciones requieren el contrato de clasificación por elemento y registro IAM ex ante.

**Estado:** DEC-C10-057 ACCEPTED; perfil de frontera aceptado a nivel arquitectónico, no inventariado ni congelado como schema. Sin truth, fixtures, validación, acceso a sistemas, instalación ni ejecución; scientific_execution=false; execution_authorized=false.


## DEC-C10-058 — unidad de servicio lógico y clasificación semántica de frontera (2026-11-05)

**Decisión explícita del usuario:** acepta la definición operativa de unidad de servicio lógico y las reglas de clasificación P0/P1/P2 desarrolladas en `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md`.

### Decisión

1. **Objeto/unidad de migración:** una instancia lógica de un servicio software, identificada por un contrato funcional distinguible y un contrato de configuración versionado, migrada entre un entorno fuente y uno destino. No equivale necesariamente a microservicio, proceso, binario o unidad de despliegue.
2. **P0:** configuración declarativa propia del servicio y versionada; incluye parámetros, referencias declaradas, reglas, manifiestos/variables solo en sus campos contractuales, esquema/descriptor y metadatos.
3. **P1:** realización técnica y estado ambiental; incluye runtime, binarios, infraestructura, permisos efectivos, secretos reales, datos persistentes, servicios externos efectivos y mecanismos de aplicación.
4. **P2:** frontera causal transversal; conserva elementos/relaciones que puedan afectar B, accesibilidad, aplicabilidad, Reach, rutas alternativas, selección, ejecución, Outcome, Value o medición. No es clase mutuamente excluyente.
5. **Clasificación semántica:** manifiestos y variables se descomponen campo a campo/clave a clave, sin clasificar por extensión o ubicación.
6. **Secretos:** solo referencia/identificador/requisito en P0; material secreto real en P1, nunca copiado a documentación o fixtures.
7. **Datos persistentes:** fuera de P0 por defecto; en P1 si condicionan la migración y en P2 cuando constituyan vía causal/interferencia. Migraciones de esquema de datos son proceso/artefacto separado, fuera de F* base de configuración, y se registran como cointervención cuando la ruta/B las active.
8. **Servicios externos opacos:** no se excluyen por opacidad; se registran en P2 con dependencia P1, límites de observabilidad y estado ? donde no haya evidencia suficiente.
9. **Unidad de aleatorización/analítica:** no queda decidida por DEC-C10-058. Se determinará tras resolver recursos/entornos compartidos e interferencia; podrá requerir clúster/mapa de exposición sin ampliar P0.

### Alcance y límites

La decisión acepta la arquitectura operativa y las reglas generales, no crea inventario real, no clasifica elementos concretos de un sistema no observado, no congela cardinalidades/schema ejecutable y no decide unidad de aleatorización. La identidad concreta del servicio y los contratos CMP/PAR/REF/RUL deberán fijarse ex ante en IAM/registro de inventario.

**Estado:** DEC-C10-058 ACCEPTED. Documental only; no truth, fixtures, validación, acceso a sistemas, instalación, simulación ni ejecución. `scientific_execution=false`; `execution_authorized=false`.


## DEC-C10-058 — unidad de servicio lógico y clasificación semántica de frontera (2026-11-05)

**Decisión explícita del usuario:** acepta la definición operativa de unidad de servicio lógico y las reglas de clasificación P0/P1/P2 desarrolladas en `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md`.

1. **Objeto/unidad de migración:** una instancia lógica de un servicio software, identificada por un contrato funcional distinguible y un contrato de configuración versionado, migrada entre un entorno fuente y uno destino. No equivale necesariamente a microservicio, proceso, binario o unidad de despliegue.
2. **P0:** configuración declarativa propia del servicio y versionada; incluye parámetros, referencias declaradas, reglas, manifiestos/variables solo en sus campos contractuales, esquema/descriptor y metadatos.
3. **P1:** realización técnica y estado ambiental; incluye runtime, binarios, infraestructura, permisos efectivos, secretos reales, datos persistentes, servicios externos efectivos y mecanismos de aplicación.
4. **P2:** frontera causal transversal; conserva elementos/relaciones que puedan afectar B, accesibilidad, aplicabilidad, Reach, rutas alternativas, selección, ejecución, Outcome, Value o medición. No es clase mutuamente excluyente.
5. **Clasificación semántica:** manifiestos y variables se descomponen campo a campo/clave a clave, sin clasificar por extensión o ubicación.
6. **Secretos:** solo referencia/identificador/requisito en P0; material secreto real en P1, nunca copiado a documentación o fixtures.
7. **Datos persistentes:** fuera de P0 por defecto; en P1 si condicionan la migración y en P2 cuando constituyan vía causal/interferencia. Migraciones de esquema de datos son proceso/artefacto separado, fuera de F* base de configuración, y se registran como cointervención cuando la ruta/B las active.
8. **Servicios externos opacos:** no se excluyen por opacidad; se registran en P2 con dependencia P1, límites de observabilidad y estado ? donde no haya evidencia suficiente.
9. **Unidad de aleatorización/analítica:** no queda decidida por DEC-C10-058. Se determinará tras resolver recursos/entornos compartidos e interferencia; podrá requerir clúster/mapa de exposición sin ampliar P0.

**Alcance:** aceptación conceptual; no crea inventario real, no clasifica elementos concretos de sistemas no observados, no congela cardinalidades/schema ejecutable ni decide unidad de aleatorización.

**Estado:** DEC-C10-058 ACCEPTED. Documental only; no truth, fixtures, validación, acceso a sistemas, instalación, simulación ni ejecución. `scientific_execution=false`; `execution_authorized=false`.

## Operacionalización documental posterior a DEC-C10-058 — IAM overlay (2026-11-05)

Se recuperaron y reconciliaron la plantilla U_G de diez registros, el protocolo de evidencia/adjudicación, la matriz trivalente, el contrato de frontera/granularidad, el manifiesto B y los contratos de identidad/snapshots. Se determina que la brecha pendiente no justifica recrear una plantilla: se crea `C10_S_IAM_SERVICE_BOUNDARY_OVERLAY_AND_CROSSWALK_DRAFT_001.md` como overlay sobre los diez registros U_G existentes.

El overlay propone campos semánticos P0/P1 y relaciones P2, crosswalk a los diez registros canónicos y correspondencia funcional provisional FP-01…08. No crea registros ni estados técnicos, no amplía el catálogo EDGE y no modifica los contratos trivalentes. Sigue pendiente de revisión/decisión y reconciliación detallada de FP y cardinalidades.


## DEC-C10-059 — incorporación de NODE.boundary_class y FK versionada SNAPSHOT→NODE (2026-11-05)

**Decisión explícita del usuario:** acepta la columna `NODE.boundary_class` con el dominio sustantivo `{P0_CONFIG, P1_ENVIRONMENT, DUAL_P0_P1}` y las restricciones del crosswalk IAM.

1. Se incorpora `NA` únicamente como marcador de no aplicabilidad justificada; no es una cuarta clase sustantiva. No se admite null/omisión como sustituto de NA. Si la clase aplicable es desconocida, no se usa NA.
2. `boundary_class` es obligatorio en NODE, no sustituye `class` ni `semantic_role`, no codifica P2 y no implica existencia, truth, accesibilidad ni cobertura.
3. Se resuelve la referencia SNAPSHOT→NODE usando la clave compuesta: `SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`. `unit_id` conserva identidad semántica estable; `unit_object_record_id` identifica la versión de fila del nodo raíz, cuyo `semantic_role=LOGICAL_SERVICE_UNIT`.
4. La referencia compuesta evita que una FK simple a node_id apunte ambiguamente a varias revisiones versionadas.
5. La plantilla se actualiza documentalmente; parser, constraints físicos y validador siguen pendientes.

**Alcance:** decisión conceptual/documental; no freeze ejecutable, no captura, no inventario real, no truth, fixtures, simulación ni experimento. `scientific_execution=false`; `execution_authorized=false`.

**Estado:** DEC-C10-059 ACCEPTED.

## DEC-C10-060 — vocabulario semantic_role y nodo raíz lógico U_G (2026-11-05)

**Decisión explícita del usuario:** acepta el contrato propuesto `C10_S_UG_SEMANTIC_ROLE_AND_LOGICAL_ROOT_CONTRACT_DRAFT_001.md`, incluido el vocabulario controlado de 16 roles, el crosswalk no uno-a-uno N01–N23 y las reglas del nodo raíz lógico.

1. Se distinguen tres dimensiones independientes: `parent_catalog_id` (linaje N01–N23), `semantic_role` (tipo semántico del objeto NODE) y `boundary_class` (P0/P1/DUAL/NA conforme a DEC-C10-059).
2. Los NODE utilizan exactamente un `semantic_role` del vocabulario controlado versionado de 16 valores. Si un objeto no encaja, no se fuerza su clasificación: se documenta la indeterminación y se propone revisión del vocabulario antes de instanciarlo.
3. N01–N23 son roles/elementos del catálogo U_G, no una taxonomía de NODE; su correspondencia con semantic_role puede ser muchos-a-muchos y no crea nodos/aristas.
4. Se confirma la regla DEC-C10-059: `SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`; el NODE destino debe tener `semantic_role=LOGICAL_SERVICE_UNIT`.
5. Para cada combinación `(unit_id, snapshot_id, scope)` debe resolver exactamente un nodo raíz lógico. Los snapshots preservan la revisión exacta del nodo raíz; no se reescribe historia.
6. El nodo raíz es ancla de identidad analítica, no necesariamente un objeto P0/P1. `boundary_class=NA` solo con justificación si no es por sí mismo un objeto/artefacto P0/P1; no asignar DUAL por representar la unidad lógica.
7. Esta decisión es conceptual/documental. Enums, FK compuesta, exclusividad/cardinalidad y restricciones físicas quedan pendientes del gate técnico autorizado.

**Estado:** DEC-C10-060 ACCEPTED. No se crean instancias, inventario real, truth, fixtures ni evidencia. `scientific_execution=false`; `execution_authorized=false`.


## Registro complementario — reconciliación de plantilla U_G (2026-11-05)

Tras DEC-C10-060, se actualiza el encabezado SNAPSHOT para declarar la FK compuesta `(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`. Se aclara que los NA de las filas ilustrativas NODE/SNAPSHOT son marcadores de plantilla y no observaciones reales. Estas son reconciliaciones documentales de DEC-C10-059, no nuevas decisiones sustantivas ni validaciones físicas.


## DEC-C10-061 — referencias tipadas e integridad referencial U_G (2026-11-05)

**Decisión explícita del usuario:** acepta la propuesta de contrato `C10_S_UG_TYPED_TARGET_REFERENTIAL_INTEGRITY_CONTRACT_PROPOSAL_DRAFT_001.md`.

1. CLAIM_EVIDENCE_LINK utiliza seis referencias FK tipadas: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE. Exactamente una debe estar poblada y debe coincidir con `claim_target_type`.
2. EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER utilizan el mismo patrón con `object_type`; E1/E2 mantienen FKs directas a EVALUATOR_ASSESSMENT.
3. `object_record_id` es UNIQUE dentro de cada una de NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT, como clave candidata de las FKs tipadas, preservando claves semánticas compuestas y versionado.
4. `COVERAGE_REGISTER.coverage_scope_id` es PK/UNIQUE.
5. `source_provenance` se normaliza en EVIDENCE_REGISTER y no se duplica como campo común en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT.
6. `evidence_ref` continúa siendo navegación opcional 0..1; CLAIM_EVIDENCE_LINK conserva cardinalidad 0..n.
7. Las FKs, CHECK de exclusividad/tipo, dominios y reglas de unicidad son requisitos de diseño; su implementación y validación física quedan pendientes del gate técnico autorizado.

**Estado:** DEC-C10-061 ACCEPTED DOCUMENTALLY. No hay freeze, parser, constraints, fixtures, inventario real, truth, simulación ni experimento. `scientific_execution=false`; `execution_authorized=false`.


## DEC-C10-062 — identidad de registro, versionado y supersession U_G (2026-11-05)

**Decisión explícita del usuario:** acepta la propuesta `C10_S_UG_RECORD_ID_VERSION_AND_SUPERSESSION_CONTRACT_PROPOSAL_DRAFT_001.md`.

1. `object_record_id` es identificador opaco, persistente, no vacío y UNIQUE dentro de cada tabla de objetos NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT; no se exige unicidad global entre tablas porque las referencias externas son tipadas.
2. Los IDs semánticos (`node_id`, `edge_id`, `route_id`, `predicate_id`, `snapshot_id`) permanecen separados de la identidad de registro. La clave de versión es UNIQUE por (ID semántico, `object_version`) dentro de cada tabla.
3. `object_version` es entero positivo, inicia en 1 y aumenta secuencialmente de uno en uno para revisiones de la misma identidad semántica. No admite duplicados, saltos, decrementos ni reutilización.
4. La versión 1 tiene `supersedes_record_id=NULL`. Cada versión posterior referencia el registro inmediatamente anterior de la misma tabla y misma identidad semántica. La referencia debe resolver, y la versión predecesora debe ser la actual menos uno.
5. La cadena es lineal: cada registro puede tener como máximo un sucesor inmediato; no se permiten autorreferencias, referencias futuras, bifurcaciones, ciclos ni huérfanos. Se exige una única raíz v1 y un único extremo vigente por cadena.
6. Los registros históricos son inmutables; correcciones generan nuevas filas. Supersession no implica equivalencia funcional, causal ni de valor.
7. Cambios semánticos materiales, split/merge, derivación, alternativa o nueva captura SNAPSHOT no se representan como supersession. Requieren identidad/relación propia; continuidad incierta permanece `MATCH_UNRESOLVED / ?`.
8. `created_at` es record-time y no equivale al tiempo de observación o validez. SNAPSHOT conserva la FK compuesta a la versión exacta del NODE raíz.
9. Estas reglas se aplican solo a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. Las demás tablas mantienen claves y contratos propios.

**Estado:** DEC-C10-062 ACCEPTED DOCUMENTALLY. Se aplica a la plantilla y documentos relacionados. Constraints físicos, parser, validador de cadena, protección de inmutabilidad y pruebas negativas quedan pendientes del gate técnico autorizado. No implica freeze, inventario real ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## DEC-C10-065 — Pinning exacto de revisión SNAPSHOT (2026-11-05)

**Estado:** ACCEPTED — decisión expresa del usuario.

Se aprueba `snapshot_object_record_id` obligatorio en NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP, junto con `snapshot_id`. La pareja forma FK compuesta hacia SNAPSHOT(`snapshot_id`, `object_record_id`). La decisión conserva el versionado de SNAPSHOT de DEC-C10-062 y prohíbe resolución por timestamp, última versión o fallback.

La plantilla U_G actualiza encabezados y filas de esquema. §15.2/§15.6 especifican claves candidatas y FKs compuestas en orden explícito, incluyendo EDGE→NODE, PREDICATE→ROUTE, ROUTE_STEP→ROUTE/NODE/EDGE y SNAPSHOT→NODE raíz. Las referencias deben conservar exactamente el mismo snapshot_id + snapshot_object_record_id. La circularidad SNAPSHOT↔NODE raíz queda sujeta a FK diferibles o mecanismo transaccional equivalente probado.

OAS-02: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING. OAS-03: matriz compuesta especificada documentalmente; validación de completitud/implementabilidad pendiente. UG-SCH-10 sigue OPEN; no schema freeze, revisión independiente, DDL, parser, fixtures ni ejecución científica.


## 46. Reconciliación de registro — DEC-C10-063 y DEC-C10-064 (2026-11-05)

Esta entrada completa la indexación documental de decisiones ya aceptadas y registradas en el maestro; no constituye una nueva decisión ni altera su fecha, alcance o contenido.

### DEC-C10-063 — Opción A para UG-SCH-10

El usuario aceptó Opción A como arquitectura de referencia para pertenencia de NODE/EDGE/ROUTE/PREDICATE a snapshots, referencias versionadas exactas y ROUTE_STEP normalizado. El registro autónomo queda en DEC-C10-063_UG_OPTION_A_ARCHITECTURE_ACCEPTANCE.md. Su aceptación no implica schema freeze ni validación técnica. El maestro la registra en §118.

### DEC-C10-064 — resolución estructural de Opción A

El usuario aprobó documentalmente el contrato de versionado observacional, SNAPSHOT↔NODE raíz con integridad referencial diferible/transacción atómica, referencias exactas EDGE→NODE y PREDICATE→ROUTE, ROUTE_STEP normalizado y separación de cambios de observación, estructura, evidencia y accesibilidad. El registro autónomo es DEC-C10-064_OPTION_A_STRUCTURAL_RESOLUTION_ACCEPTANCE.md. Su alcance y condiciones técnicas permanecen como constan en ese registro y en el maestro §119.

DEC-C10-065 completa el pinning exacto de revisión SNAPSHOT y permanece en su registro autónomo. Esta reconciliación solo cierra la laguna de indexación del Decision Log; UG-SCH-10 sigue OPEN y no hay schema freeze, validación física ni ejecución científica.


## 47. DEC-C10-066 — aceptación de D2 como escenario primario candidato (2026-11-06)

Se acepta D2 como escenario primario candidato de C10-S para el contraste mecanístico de provisión técnica focal frente a ausencia de intento focal en control. D1 se conserva como escenario secundario para el contraste incremental frente a provisión ordinaria de baja frecuencia.

El registro autónomo es `DEC-C10-066_D2_PRIMARY_CANDIDATE_ACCEPTANCE.md`. Esta decisión resuelve la selección primaria candidata que DEC-C10-026, DEC-C10-031 y la reconciliación causal mantenían abierta. Las recomendaciones históricas de D1 como principal condicionado quedan supersedidas únicamente para esta selección; D1 no se elimina ni se reescribe su historial.

La decisión no valida (s=0.80), parámetros ni DGP; no cierra (B_{g0}/B_{g1}), (g_0/g_1), estimandos, (q_X^*), poblaciones, Value, horizonte ni identificación; tampoco autoriza freeze, implementación, simulación o ejecución científica. ITT, primeras etapas y LATE/Wald de D1 y D2 permanecen específicos por comparador y no se agrupan ni transportan automáticamente.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.


## 48. DEC-C10-067 — aceptación del contrato material de políticas D2 (2026-11-06)

El usuario acepta las definiciones materiales conceptuales de (B_{g0}^{D2}) y (B_{g1}^{D2}): control sin intento focal programado, frente a tratamiento con provisión técnica focal programada y protocolo de verificación separado. La asignación, intento programado/efectivo, recepción, instalación, componentes técnicos, (C_{dep}^{*}), (A_f^{*}) y (D_f^{*}) permanecen distintos.

El registro autónomo es `DEC-C10-067_D2_MATERIAL_POLICY_CONTRACT_ACCEPTANCE.md`. La autorización basal (C_{auth,base}=1) y las condiciones no focales declaradas se mantienen comunes en el DGP aislado. Cualquier cambio diferencial en recursos, permisos, costes, latencia, calidad, seguridad, información, incentivos o alternativas se registra como vía colateral/cointervención; el ITT no se etiqueta automáticamente como efecto puro de accesibilidad.

La aceptación es conceptual/documental. (s=0.80) sigue siendo candidato no validado; no se aprueban parámetros, distribuciones conjuntas, actor, artefacto/hash, recepción, ventanas, reintentos, evidencia, inventario de rutas, estimandos, población/soporte ni identificación. D2 continúa primario candidato y D1 secundario por DEC-C10-066. No se autoriza freeze, implementación, validación ejecutable, simulación ni ejecución científica.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.


## 49. Reconciliación de representación DEFAULT (2026-11-06)

DEC-C10-054 ya acepta distinguir DEFAULT_DECLARED / DEFAULT_INHERITED / DEFAULT_ENV_RESOLVED. La discrepancia posterior era de representación entre el enum PAR y la matriz de mapping, no una cuestión que requiera reabrir la decisión.

Interpretación armonizada: PAR conserva state ∈ {ABSENT,NULL,DEFAULT,VALUE}; cuando DEFAULT, default_kind ∈ {DECLARED,INHERITED}. DEFAULT_ENV_RESOLVED es observación del entorno E_dst/snapshot, no estado del paquete. Si no se puede distinguir origen declarado/heredado, UNKNOWN salvo evidencia independiente. Igualdad del valor ambiental resuelto no demuestra equivalencia del contrato.

Esta entrada registra reconciliación de alcance de decisión existente, no una nueva DEC aceptada, no modifica DEC-C10-054 y no autoriza implementación/ejecución. Campos por clave, herencia, snapshot, evidencia y oráculo siguen abiertos.

## 50. Contrato RUL: cardinalidad aceptada y semántica de instancia (2026-11-06)

DEC-C10-056 acepta RUL≥1 y DEC-C10-054 fija el presupuesto y semántica general del núcleo. Esta entrada no aprueba una regla de instancia. La propuesta posterior de §51 especializa el mundo sintético del DGP mediante un contrato estipulado ex ante; su fuente es interna al DGP y no una norma externa. §51 prevalece para describir esa propuesta, sin cambiar su estado pendiente de aceptación.
## 51. Propuesta de especialización funcional sintética del servicio lógico (2026-11-06)

Se propuso especializar la unidad aceptada por DEC-C10-051/052/057/058 como servicio lógico sintético de procesamiento de solicitudes, con PAR-SVC-ENABLED BOOL, PAR-SVC-PROFILE ENUM={STANDARD,READ_ONLY,DISABLED} y RUL-SVC-ENABLE-PROFILE-01: ENABLED=true implica PROFILE∈{STANDARD,READ_ONLY}, efecto REQUIRE. Esta propuesta fue aceptada conceptualmente por DEC-C10-068; la fuente es el contrato estipulado ex ante del mundo sintético, no una norma externa ni afirmación sobre servicios reales. RETRY-COUNT queda excluido.

**Estado actualizado por DEC-C10-068: ACEPTADA CONCEPTUALMENTE como contrato funcional sintético de referencia.** No modifica DEC-C10-056 ni convierte RUL-01/02/03 (propiedades de preservación) en identificador de esta regla. RETRY-COUNT queda fuera del núcleo. Owner CMP de instancia/versionado, IAM detallado, mapping físico, oráculo, estimandos y unidad de asignación siguen abiertos. No crea fixtures ni autoriza implementación/ejecución.

## 52. DEC-C10-068 — aceptación del contrato funcional sintético del servicio de referencia (2026-11-07)

El usuario acepta el servicio lógico sintético de procesamiento de solicitudes, PAR-SVC-ENABLED BOOL, PAR-SVC-PROFILE ENUM={STANDARD,READ_ONLY,DISABLED} y RUL-SVC-ENABLE-PROFILE-01: ENABLED=true implica PROFILE∈{STANDARD,READ_ONLY}, efecto REQUIRE. El contrato es constitutivo del mundo sintético y fija la verdad del DGP ex ante; no es norma externa ni afirmación empírica sobre servicios reales. ENABLED=false no queda restringido por esta implicación. PAR-SVC-RETRY-COUNT permanece fuera del núcleo.

El registro autónomo es `00_GOVERNANCE/decisions/DEC-C10-068_SYNTHETIC_SERVICE_FUNCTIONAL_CONTRACT_ACCEPTANCE.md`. CMP-SERVICE-LOGIC es owner lógico provisional; identidad/versionado de instancia, serialización, IAM detallado, mapping físico, tolerancias y oráculo permanecen abiertos. La aceptación no constituye Design Freeze ni autoriza fixtures, implementación, validación ejecutable, simulación o ejecución científica.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.

## 53. Propuesta de identidad/versionado CMP para el servicio sintético (2026-11-07)

Se documenta `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md` como especialización pendiente del contrato abstracto de instancia y de MET. Se separan contract_id/version, instance_id/version, component_id/class, owner, mapping, IAM, oráculo y hash de artefacto. TID/SID/RID/EID del espacio transformacional no se reutilizan como IDs CMP.

Candidatos: contract_id=C10S-SVC-REQUEST-PROCESSOR, contract_version=1.0.0, instance_id=C10S-SVC-REQUEST-PROCESSOR-001, instance_version=1, component_id=CMP-SERVICE-LOGIC-001, component_class=SERVICE_LOGIC. Son candidatos y no valores canónicos hasta aceptación. CMP-SERVICE-LOGIC de DEC-C10-068 es rol/owner lógico, no identidad única. RETRY-COUNT sigue excluido.

La propuesta separa versión del contrato, revisión inmutable del paquete y hash de serialización. No se fija hash antes de formato canónico; versiones de C_src/C_dst, M, IAM y oráculo son independientes. Matching no se infiere por nombre/hash.

**Estado:** propuesta documental; aceptación de IDs/política pendiente. No crea fixture, IAM sellado, serialización, prueba ni autorización de implementación/ejecución.


## 54. DEC-C10-069 — aceptación de identidad y versionado CMP (2026-11-07)

El usuario acepta los identificadores y la política de versionado propuestos para la instancia de servicio sintético: contract_id=C10S-SVC-REQUEST-PROCESSOR, contract_version=1.0.0, instance_id=C10S-SVC-REQUEST-PROCESSOR-001, instance_version=1, component_id=CMP-SERVICE-LOGIC-001, component_class=SERVICE_LOGIC. CMP-SERVICE-LOGIC de DEC-C10-068 permanece como owner/rol lógico, no ID único. Se acepta contract_version MAJOR.MINOR.PATCH; instance_version entero positivo, monotónico e inmutable; hash solo de serialización canónica definida; versionado independiente de C_src/C_dst, M, IAM y oráculo; matching explícito sin equivalencia inferida por nombre/hash.

Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-069_SERVICE_CMP_IDENTITY_AND_VERSIONING_ACCEPTANCE.md`. DEC-C10-069 especializa DEC-C10-068. Serialización, MET físico, IAM sellado, mapping, valores por escenario, oráculo y evidencia siguen OPEN. No Design Freeze ni autorización de implementación/ejecución.

## 55. Especialización documental del mapping CMP/PAR/RUL (2026-11-07)

Se incorpora la especialización propuesta en C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md §20, reutilizando el crosswalk previo. El mapping referencia los IDs aceptados por DEC-C10-069 y el contrato funcional DEC-C10-068. Define CMP lógico, los dos PAR aceptados y RUL-SVC-ENABLE-PROFILE-01, con separación por etapa F1/A1 frente a F2/A2, FP-06/07 y adjudicación 1/0/?/NA.

No constituye una nueva decisión del usuario ni acepta/congela la propuesta. RETRY-COUNT queda excluido por DEC-C10-068; la nota de aceptación pendiente de §18 de la matriz queda supersedida por DEC-C10-069. IAM, defaults/valores concretos, mapping físico, serialización/MET, oráculo y evidencia siguen OPEN. Sin fixtures, implementación, validación ejecutable o ejecución científica.

## 56. Reconciliación documental IAM/Oráculo tras DEC-C10-069 (2026-11-07)

La matriz IAM §17 corrige el estado histórico de §16: los IDs contract/instance/CMP ya fueron aceptados por DEC-C10-069; mapping_id, IAM_id, oracle_id y serialización/hash siguen OPEN. Se especifica como requisito la instanciación IAM por ruta/etapa/objeto/propiedad/snapshot, la distinción C_dst declarado/aplicado y E_dst, y la separación de truth del DGP, salidas del Analizador y adjudicación del Evaluador.

La especificación es documental y no constituye nueva decisión del usuario ni contrato de oráculo aceptado/congelado. Roster global, valores/defaults por escenario, AST/mapping, cobertura, evidencia, cegamiento y reglas operativas de UNKNOWN/conflicto permanecen OPEN. Sin fixtures, implementación o ejecución científica.

## 57. Reconciliación documental del roster funcional mínimo (2026-11-07)

Se documenta en la matriz IAM §18 la reconciliación de DEC-C10-056/068/069: CMP focal aceptado, dos PAR y una RUL funcional aceptados, MET obligatorio, POL fuera del núcleo y REF=0 condicionado a inventario/cobertura exhaustivos pre-Z/B. RETRY-COUNT queda excluido del núcleo por DEC-C10-068. No se declara cerrado el inventario exhaustivo ni se sella IAM.

Los PAR aceptados no tienen DEFAULT contractual declarado; no se asignan valores por escenario. La especificación no constituye una nueva decisión del usuario, no acepta el mapping §20 ni autoriza implementación/ejecución.

## 58. Protocolo documental de inventario por snapshot (2026-11-07)

Se especializa la plantilla U_G existente §18 y la matriz IAM §19 para el inventario de configuración C10-S por snapshot, ruta y etapa. Se reutilizan NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y los registros de evidencia/cobertura; no se alteran schema/FKs ni se crean tablas físicas. PAR/RUL permanecen en el catálogo/manifiesto de configuración, sin forzarlos a NODE/PREDICATE. C_src, F1→S2, A1→S1, C_dst declarado y aplicado por F2/A2 se mantienen separados.

Se reconcilian contrato abstracto §16 y catálogo atómico §15: RETRY-COUNT histórico queda supersedido para el núcleo por DEC-C10-068; no hay DEFAULT aceptado para ENABLED/PROFILE. El protocolo no crea snapshots ni evidencia y no es decisión aceptada de schema/manifiesto físico. La codificación de etapa/ruta en scope y el inventario exhaustivo siguen OPEN. No autoriza ejecución.
## 59. Contrato documental propuesto para scopes de cobertura C10-S (2026-11-07)

Se documenta en IAM §19.7 y plantilla U_G §18.6 la especialización de COVERAGE_REGISTER §12.3: scope lógico único por snapshot exacto×etapa×ruta×clase CMP/PAR/REF/RUL/MET; coverage_scope_id opaco/único; dimension C10S_CONFIG_*; universe_definition/version con tupla exacta y regla de enumeración. Hasta 35 scopes lógicos para siete etapas×cinco clases, sin instanciarlos como observaciones.

Se explicitan denominadores y criterios de cobertura NONE/PARTIAL/COMPLETE; ausencia/REF=0 requiere cobertura exhaustiva y evidencia. Se identifica que COVERAGE_REGISTER carece de FK directa a SNAPSHOT: el pinning textual no equivale a integridad relacional. No se modifica schema. Esta limitación no reabre U_G-SCH-10: la pertenencia versionada del grafo a SNAPSHOT ya fue aceptada por DEC-C10-065 (Opción A), con validación física pendiente en su propio gate. El vínculo de COVERAGE_REGISTER a snapshot es un gate separado y continúa OPEN. Este registro es avance documental/propuesta, no una nueva aceptación del usuario ni autorización de ejecución.

## 60. Aclaración de integridad de scopes y snapshots (2026-11-07)

Se corrige el registro anterior: U_G-SCH-10 no es el gate de COVERAGE_REGISTER. La pertenencia versionada del grafo a SNAPSHOT fue aceptada semánticamente mediante DEC-C10-065/Opción A; su validación física sigue separada. Los registros de objeto enlazan coverage_scope_id y snapshot exacto, pero COVERAGE_REGISTER no contiene el par snapshot_id/snapshot_object_record_id, por lo que el motor no puede imponer su coincidencia mediante FK compuesta.

Se documentan alternativas C0 (esquema actual + pinning en universe_definition/version + control independiente, provisional/conditional), C1 (extensión de COVERAGE_REGISTER y FK compuesta, no aceptada) y C2 (tabla puente, no recomendada salvo necesidad). No se modifica schema ni se declara integridad relacional plena. La convención SNAPSHOT.scope permanece pendiente.

## 61. DEC-C10-070 — aceptación condicionada de C0 (2026-11-07)

El usuario acepta C0 para el binding COVERAGE_REGISTER↔SNAPSHOT: conservar el schema y fijar en universe_definition/version una tupla exacta por coverage_scope_id (contrato/instancia/snapshot/registro/etapa/ruta/clase). Todo registro que referencia el scope debe coincidir. Se requiere control independiente de igualdad, unicidad, cardinalidad, huérfanos/no usados y conflictos.

C0 es una decisión documental aceptada, pero su enforcement queda CONDITIONAL hasta que el control esté especificado, implementado bajo autorización, ejecutado y auditado antes de Design Freeze. No equivale a FK compuesta. C1/C2 no aceptadas ni autorizadas. No se modifica schema, no se reabre DEC-C10-065, no se acepta SNAPSHOT.scope ni se autoriza implementación/ejecución.


## 62. Especificación documental del control C0 (2026-11-07)

Se registra que el protocolo de evidencia/adjudicación §19 contiene la especificación documental del control independiente C0: binding canónico, invariantes, reconciliación de cobertura/denominador, resultados PASS/FAIL/UNKNOWN, casos adversariales y requisitos de provenance. No se registra como nueva aceptación del usuario ni autorización de implementación/ejecución.

Estado: DOCUMENTED SPECIFICATION; DDL mapping OPEN; NOT IMPLEMENTED; NOT EXECUTED; NOT AUDITED. DEC-C10-070 sigue siendo la decisión que acepta C0 como contrato documental. No Design Freeze ni ejecución científica.

## 63. Limitación de mapping C0↔U_G (2026-11-07)

La inspección documental del esquema vigente (protocolo §20) identifica que stage_key no tiene columna propia; SNAPSHOT.phase no equivale y SNAPSHOT.scope sigue OPEN. route_id solo está directo en ROUTE/PREDICATE/ROUTE_STEP, no en NODE/EDGE. object_class CMP/PAR/REF/RUL/MET carece de campo común tipado. contract/instance versions y dimension requieren binding documental recuperable. snapshot_id + snapshot_object_record_id sí están cubiertos por DEC-C10-065/Opción A.

Esto no revoca DEC-C10-070 ni la aceptación de C0; delimita su evaluabilidad. No habrá PASS completo hasta un crosswalk explícito y verificable. Correspondencia no demostrada → UNKNOWN; contradicción demostrada → FAIL. No se añade schema ni se autoriza implementación/ejecución.

## 64. Reconciliación del crosswalk C0↔U_G (2026-11-07)

Se registra como propuesta documental la reutilización del crosswalk IAM histórico y la separación de object_class C10, ug_record_type y semantic_role/boundary_class de NODE. U_G §18.2 aporta siete stage_key candidatos (C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED, A2_DST_APPLIED); no equivalen al reloj DGP t−1…t9 ni a SNAPSHOT.phase. La propuesta de SNAPSHOT.scope no fue aceptada por DEC-C10-070.

Las etiquetas NONE/F/A son familia de ruta, no route_id exacto; CONFIG no satisface el object_class C0, que permanece CMP/PAR/REF/RUL/MET. Route membership requiere ROUTE_STEP/record IDs exactos. dimension permanece en COVERAGE_REGISTER, fuera de la tupla C0 de nueve componentes.

No constituye aceptación nueva del usuario. Vocabulario final de stage_key, token global, gramática universe_definition/version y mapping por propiedad permanecen OPEN. No se modifica schema ni se autoriza implementación/ejecución.


## 65. DEC-C10-071 — aceptación del vocabulario controlado stage_key (2026-11-07)

El usuario acepta como vocabulario cerrado de stage_key C10-S los siete valores de U_G §18.2: C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED y A2_DST_APPLIED. La decisión se registra en `00_GOVERNANCE/decisions/DEC-C10-071_C10S_STAGE_KEY_VOCABULARY_ACCEPTANCE.md`.

La aceptación se limita a los valores y sus significados. stage_key se mantiene separado del reloj DGP t−1…t9, SNAPSHOT.phase y SNAPSHOT.timestamp. No se acepta la serialización en SNAPSHOT.scope ni los campos route=NONE/F/A u object_class=CONFIG de la propuesta histórica. El binding C0 permanece en COVERAGE_REGISTER.universe_definition/version; route_id exacto/token global y mappings físicos siguen OPEN. C0 mantiene object_class CMP/PAR/REF/RUL/MET y dimension fuera de la tupla.

DEC-C10-071 no modifica schema, no crea scopes/snapshots ni autoriza implementación, validación ejecutable o ejecución científica. No Design Freeze.


## 66. Propuesta de route_id y scope global (2026-11-07) — no es decisión aceptada

Se documenta en protocolo de evidencia §20.8 una comparación de tres alternativas para el slot route_id de C0. G1 usa un token reservado, candidato `C10S_SCOPE_GLOBAL`, recomendado provisionalmente; G2 NULL/vacío se considera ambiguo; G3 scope_kind separado requeriría reabrir estructura/tupla. El candidato G1 significa “sin restricción a ruta concreta”, no ausencia de rutas ni no pertenencia de objetos. No queda aceptado por este asiento.

Se especifican reglas de pertenencia CMP/PAR/REF/RUL/MET, denominadores independientes para scopes route-specific y conteo único por objeto en scope global, además de adjudicación 1/0/?/NA. El 0 de pertenencia solo significa no miembro de una ruta concreta y requiere inventario/mapping/ROUTE_STEP exhaustivos.

Referencias: protocolo de evidencia §20.8; matriz mapping §20.10; plantilla U_G §18.13; maestro §187; plan §16.42; matriz de control §60. La aceptación del literal/namespace y la gramática versionada universe_definition/version siguen pendientes. No schema change, implementación ni ejecución autorizada.


## 67. DEC-C10-072 — aceptación del token de scope global (2026-11-07)

**Estado: ACEPTADA.** Se acepta G1 y el literal reservado `C10S_SCOPE_GLOBAL` en el slot route_id de C0, con significado exclusivo “sin restricción a una ruta concreta”. No significa ausencia de rutas, no pertenencia de objetos ni NA. Se prohíbe como route_id semántico real; colisión = FAIL. NULL/vacío/NONE/F/A no son sustitutos.

Scope global cuenta cada identidad elegible una sola vez por clase/etapa/snapshot; scopes route-specific mantienen denominadores independientes y exigen route_id semántico, route_record_id y snapshot exactos. G2 queda descartada por ambigüedad; G3 no se adopta.

DEC-C10-072 cierra solo literal y semántica. Gramática/versionado universe_definition, mapping físico, control C0 implementado/auditado y Design Freeze permanecen abiertos. No implementación ni ejecución autorizadas. Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-072_GLOBAL_ROUTE_SCOPE_TOKEN_ACCEPTANCE.md`.



## 68. UDG-01 — propuesta de gramática universe_definition (2026-11-07)

Se registra propuesta documental UDG-01 en protocolo de evidencia §20.10, plantilla U_G §18.15, matriz de mapping §20.12, maestro §189, plan §16.44 y matriz de control §62. Recomienda envelope JSON autocontenido con scope C0 exacto de nueve componentes, membership EXPLICIT/RULE_DEFINED, referencias tipadas/reglas versionadas, fuentes, cardinalidad y provenance; propone canonicalización determinista y SHA-256, semver de schema y revisión inmutable de universo.

Estado: NO ACEPTADA. No crea schema ni contrato ejecutable; no parser, validator, fixtures, Design Freeze ni autorización de implementación/ejecución. La gramática final, canonicalización/hash y mapping físico permanecen OPEN.

**Reconciliación de estado DEC-C10-072:** los asientos históricos §§64 y 66 y las redacciones previas de §§20.8.6/18.13 reflejan el estado anterior a la aceptación. No se reescriben por inmutabilidad histórica. Desde DEC-C10-072 (asiento §67 y registro autónomo), G1 y el literal C10S_SCOPE_GLOBAL están ACEPTADOS. Toda lectura vigente debe aplicar DEC-C10-072; solo permanecen abiertos la gramática completa, mappings físicos y control C0.


## 69. DEC-C10-073 — aceptación de arquitectura U1 para universe_definition (2026-11-07)

**Estado: ACEPTADA.** U1 se adopta como arquitectura documental: envelope JSON autocontenido y versionado con campos/cardinalidades UDG-01, scope C0 exacto de nueve componentes, EXPLICIT/RULE_DEFINED, referencias tipadas, cardinalidad declarada, fuentes y provenance. Universo vacío exige evidencia exhaustiva. La separación conceptual schema_version/universe_revision queda aceptada.

**No aceptado/cerrado:** canonicalización UTF-8/NFC/orden determinista como obligación, SHA-256 normativo, RFC/JCS, serialización física ejecutable, reglas completas de compatibilidad semver, mapping físico CMP/PAR/REF/RUL/MET y control C0 implementado/auditado. No schema change, parser, validator, fixtures, Design Freeze ni ejecución autorizados.

Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-073_UNIVERSE_DEFINITION_ENVELOPE_ACCEPTANCE.md`. Este asiento prevalece sobre §68, que registraba UDG-01 como propuesta no aceptada antes de la aceptación explícita.


## 70. UDG-02 — propuesta de canonicalización e integridad (2026-11-07)

Se registra propuesta UDG-02 en protocolo §20.12, plantilla U_G §18.17, matriz de mapping §20.14, maestro §191, plan §16.46 y matriz de control §64. Se comparan C1 RFC 8785 JCS con prevalidación TGCV, C2 canonicalizador propio y C3 hash de bytes fuente; C1 se recomienda provisionalmente. La propuesta distingue hash de artefacto fuente y hash del contenido canónico, define restricciones Unicode/números/null/arrays y prohíbe inferir equivalencia semántica a partir del hash.

**Estado: NO ACEPTADA.** No se convierte SHA-256/JCS en requisito, no hay perfil de producción, parser, validator, fixtures, schema change ni ejecución autorizados. Fuente normativa consultada: RFC 8785 (Informational, no Internet Standards Track): https://www.rfc-editor.org/rfc/rfc8785.html.


## 71. DEC-C10-074 — aceptación del perfil JCS (2026-11-07)

**Estado: ACEPTADA.** C1 RFC 8785 JCS + prevalidación TGCV se adopta como política documental de canonicalización del envelope U1, con perfil TGCV-C10S-JCS-1 y las reglas de DEC-C10-074. Se distinguen source_artifact_hash y canonical_content_hash; igualdad de hash/perfil no acredita equivalencia semántica ni exhaustividad.

No autoriza hash de producción, parser/validator, fixtures, schema change, Design Freeze, implementación o ejecución científica. Mapping físico CMP/PAR/REF/RUL/MET y control C0 independiente permanecen abiertos. Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-074_CANONICALIZATION_PROFILE_JCS_ACCEPTANCE.md`. Este asiento prevalece sobre §70, propuesta anterior no aceptada.


## 72. UDG-03 — propuesta de comparación semántica de universos (2026-11-07)

Se registra UDG-03 en protocolo §20.14, plantilla U_G §18.19, matriz de mapping §20.16, maestro §193, plan §16.48 y matriz de control §66. Propone un vector de comparación por dimensión: artefacto, canónico, identidad, revisión, extensional, definicional y compatibilidad. Establece precondiciones de scope/snapshot, miembros versionados y exhaustividad; separa igualdad extensional de equivalencia definicional; fija EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE y FAIL de integridad.

**Estado: NO ACEPTADA.** No crea fingerprint semántico ni comparator ni autoriza fixtures, schema change o ejecución. La propuesta no modifica DEC-C10-073/074.


## 73. DEC-C10-075 — aceptación de comparación semántica UDG-03 (2026-11-07)

**Estado: ACEPTADA.** Se acepta UDG-03 como contrato documental de comparación vectorial por siete niveles: artefacto, canónico, identidad universe_id, revisión, extensional, definicional y compatibilidad dirigida entre revisiones. Se separan Projection-ID y Projection-SEM; igualdad extensional exige universos completos/exhaustivos y scope/snapshot compatibles; equivalencia definicional requiere reglas/AST/domínios/dependencias equivalentes. Resultados EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE y FAIL de integridad.

No se infiere equivalencia por hash/ID/nombre/cardinality. Aceptación no crea fingerprint ni comparator ejecutable y no autoriza fixtures, parser/validator, schema change, Design Freeze, implementación o ejecución científica. Registro: `00_GOVERNANCE/decisions/DEC-C10-075_SEMANTIC_UNIVERSE_COMPARISON_ACCEPTANCE.md`. Este asiento prevalece sobre §72, propuesta previa no aceptada.


## 74. UDG-04 — propuesta de referencias tipadas y resolución (2026-11-07)

Se registra UDG-04 en protocolo §20.16, plantilla U_G §18.21, matriz de mapping §20.18, maestro §195, plan §16.50 y matriz de control §68. Distingue identidad lógica de identidad de registro inmutable, define referencia tipada por rol y target exacto, resolución en registry versionado, estados de ausencia/conflicto/inaccesibilidad/incompatibilidad, y tratamiento de ciclos/cardinalidad por relación. Resolver no prueba pertenencia, aplicabilidad ni ejecución.

**Estado: NO ACEPTADA.** Requiere reconciliación con catálogo REF y contratos vigentes; no fija schema físico ni autoriza resolver/API/parser/validator/fixtures/implementación/ejecución.


## 75. DEC-C10-076 — aceptación UDG-04 (2026-11-07)

**Estado: ACEPTADA.** Se acepta la separación de identidad lógica y de registro inmutable; referencia tipada por rol/target exacto; resolución en registry/manifiesto versionado con scope explícito; estados FAIL/UNKNOWN/NOT_COMPARABLE/NOT_APPLICABLE; ciclos y cardinalidad por relación. Resolver no demuestra pertenencia, aplicabilidad, preservación ni ejecución.

La aceptación no cierra catálogo REF/schema/API/registry/resolver ni mapping CMP/PAR/RUL; no autoriza parser/validator/comparator/fixtures/implementación/Design Freeze/ejecución. Registro: `00_GOVERNANCE/decisions/DEC-C10-076_TYPED_REFERENCE_IDENTITY_AND_RESOLUTION_ACCEPTANCE.md`. Prevalece sobre §74, propuesta previa no aceptada.

## 76. Reconciliación REF↔UDG-04 (2026-11-07) — propuesta, no decisión aceptada

Se propone separar REF de configuración, referencias tipadas del envelope UDG y FK/vínculos estructurales U_G. REF conserva identidad propia y extremos tipados; REF→EDGE solo por M versionado y con cardinalidad/split/merge explícitos. EDGE no es automáticamente REF. Los roles ilustrativos de DEC-C10-076 no se convierten en enum físico. IAM, cardinalidades, endpoints externos, schema físico y mapping siguen OPEN. La propuesta no modifica DEC-C10-076 ni autoriza implementación/ejecución.

## 77. DEC-C10-077 — aceptación conceptual de reconciliación REF↔UDG-04 (2026-11-07)

**Estado: ACEPTADA.** Se acepta separar REF de configuración, referencia envelope UDG y FK estructural U_G; REF posee identidad y extremos tipados; REF→EDGE requiere M explícito/versionado, sin equivalencia automática ni 1:1 asumida; split/merge/n-aria requiere parent/group identity. Los roles UDG siguen ilustrativos. No se fijan roles finales, dominios, cardinalidades, obligatoriedad, IAM ni schema físico. Registro: 00_GOVERNANCE/decisions/DEC-C10-077_REF_UDG04_CONCEPTUAL_RECONCILIATION_ACCEPTANCE.md. No autoriza implementación/Design Freeze/ejecución.


## 78. DEC-C10-078 — aceptación del contrato lógico de filas IAM (2026-11-07)

**Estado: ACEPTADA.** Se acepta la estructura de cuatro capas L1 membership del universo; L2 referencias del envelope UDG; L3 extremos funcionales de REF; L4 FK/vínculos estructurales U_G, y el contrato lógico de fila IAM: `iam_rule_id`, `layer`, `source_class`, `source_identity_rule`, `role_namespace`, `role_key`, `endpoint_position`, `target_domain`, `min_cardinality`, `max_cardinality`, `requiredness`, `applicability_trigger`, `stage_key`, `scope_mode`, `route_binding`, `version_snapshot_binding`, `integrity_rule`, `mapping_rule`, `evidence_rule`, `adjudication` y `rationale/provenance`.

La estructura es lógica y contextual; no todos los campos aplican a todas las capas. No se fijan vocabularios cerrados, cardinalidades numéricas, valores REQUIRED/OPTIONAL/CONDITIONAL, endpoints externos, enum relation_type, mapping M concreto ni schema físico. Se reutilizan los siete stage_key de DEC-C10-071 y C10S_SCOPE_GLOBAL de DEC-C10-072. Los roles UDG siguen ilustrativos y no crean objetos REF automáticamente. El siguiente trabajo puede proponer vocabularios candidatos por capa, manteniendo separados roles UDG y roles funcionales REF.

No modifica DEC-C10-077 ni autoriza roster exhaustivo, IAM poblado, DDL/API/registry/resolver, parser/validator, fixtures, Design Freeze, implementación, simulación, experimento o ejecución científica. Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-078_IAM_LOGICAL_ROW_CONTRACT_ACCEPTANCE.md`.


## 79. Propuesta de vocabularios IAM L2/L3 (2026-11-07) — no aceptada

Se registra como propuesta documental, no como decisión: separar namespace L2 `UDG_ENVELOPE_ROLE` de namespace L3 `REF_FUNCTIONAL_ROLE`. L2 reutiliza los ejemplos ilustrativos MEMBER, OWNER, SOURCE, INCLUSION_RULE, EXCLUSION_RULE, DEPENDENCY y PROVENANCE con dominios destino candidatos y límites en matriz IAM §19.13. L3 conserva role_key y relation_type abiertos; SOURCE/TARGET es endpoint_position binario. `DEPENDS_ON` solo se estudiará como candidato si una relación de dependencia REF resulta necesaria para el DGP.

OPEN: semántica de DEPENDENCY en L2; conjunto mínimo de REF funcionales requeridos por DGP; binario/n-ario; dominios de extremos; cardinalidad/requiredness por clase×rol×extremo×stage_key×scope. No se fijan enums, cardinalidades, requiredness, endpoints externos ni mapping M. No se modifica DEC-C10-078 ni se autoriza implementación/Design Freeze/ejecución.

## 80. Propuesta de resolución semántica de DEPENDENCY L2 (2026-11-07) — no aceptada

Para una dependencia como relación del dominio de configuración, se propone que L2 DEPENDENCY apunte al REF exacto que representa la relación, mientras REF/L3 conserva sus extremos tipados. Las dependencias técnicas/ambientales C_dep/E_dst no crean REF automáticamente. Las dependencias usadas para resolver/evaluar universos RULE_DEFINED permanecen como referencias tipadas/versionadas de regla/envelope, no como REF funcional por defecto. Se evita doble contabilización entre L2, REF y endpoints.

El roster mínimo CMP/PAR/RUL aceptado no declara por sí mismo una relación REF. REF=0 solo será adjudicable tras inventario/cobertura exhaustivos pre-Z/B; no se inventa relación ni se declara REF=0 ahora.

**Estado:** propuesta no aceptada; vocabulario, cardinalidad y requiredness abiertos. No modifica DEC-C10-076/077/078 ni autoriza implementación, Design Freeze o ejecución.

## 81. Auditoría propuesta del conjunto mínimo REF L3 (2026-11-07) — no aceptada

El contrato sintético aceptado CMP-SERVICE-LOGIC-001, PAR-SVC-ENABLED, PAR-SVC-PROFILE y RUL-SVC-ENABLE-PROFILE-01 no exige actualmente una relación REF funcional concreta. Operandos de RUL, R_acc/R* transformacionales, C_dep/E_dst técnicos/ambientales y dependencias de evaluación RULE_DEFINED no se convierten en REF por defecto.

El roster mínimo no es exhaustivo; REF=0 solo podrá declararse con inventario/cobertura COMPLETE por snapshot×etapa×ruta×scope pre-Z/B. La auditoría no crea filas de instancia ni sella IAM.

**Estado:** propuesta de auditoría documental no aceptada; no modifica DEC-C10-078 ni autoriza implementación/ejecución.

## 82. Propuesta de protocolo de auditoría REF por snapshot/etapa (2026-11-07) — no aceptada

Se propone adjudicar REF por contrato/instancia, snapshot exacto, stage_key, ruta, scope y universo versionado, reutilizando U_G/COVERAGE_REGISTER. La inspección separa C_SRC, F1_S2, A1_S1, F2/A2_DST_DECL y F2/A2_DST_APPLIED. Una relación exige identidad propia, semántica de dominio, extremos exactos, dirección/tipo/multiplicidad y procedencia; EDGE/FK/ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos RUL, R_acc/R*, C_dep/E_dst y referencias RULE_DEFINED no son REF por defecto.

ABSENT/REF=0 requiere enumeración exhaustiva y cobertura COMPLETE para el scope exacto; UNKNOWN ante cualquier laguna; NA solo por no aplicabilidad ex ante. Los estados no se extrapolan entre snapshots/rutas y C_DST_DECLARED no prueba C_DST_APPLIED.

**Estado:** propuesta no aceptada; sin observaciones, REF=0 ni IAM sellado. No modifica DEC-C10-078 ni autoriza implementación/ejecución.

## 83 — Registro de propuesta de inspección CMP/PAR/RUL/REF/MET

**Estado:** PROPUESTA DOCUMENTAL DE INSPECCIÓN; no aceptada como cierre IAM, no implementada y sin observaciones reales. Deriva de DEC-C10-053/056/059/061/062/065/069/070/071/072/073/074/075/076/077 y de los contratos U_G y de instancia existentes. No altera cardinalidades, vocabularios ni obligatoriedad aprobados.

### Unidad de inspección
Cada observación se ancla a la tupla exacta de identidad de contrato/instancia y versión, snapshot y registro, `stage_key`, ruta o `NONE` justificado, scope y universo/versionado. Se reutilizan NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER de U_G. No se crea un inventario paralelo ni se generan registros ficticios.

### Matriz de búsqueda por clase × etapa

| Clase | C_SRC | F1_S2 | A1_S1 | F2_DST_DECL | A2_DST_DECL | F2_DST_APPLIED | A2_DST_APPLIED |
|---|---|---|---|---|---|---|---|
| CMP | Inventario e identidad fuente | CMP afectado y mapping F1 | CMP exportado y preservación | CMP destino declarado | CMP que A2 declara importar/aplicar | CMP producido/materializado por F2 | CMP realmente presente/aplicado |
| PAR | key, owner, tipo, state y value | Conversión, defaults, pérdidas y cambios | Estados/valores exportados | PAR destino declarado y conversión | PAR que A2 declara importar | PAR materializado por F2 | Estado/valor efectivamente aplicado |
| RUL | rule_id, AST, scope, efecto | Reglas transformadas/preservadas/omitidas | Reglas exportadas | Reglas destino y mapping | Reglas que A2 declara importar | Reglas materializadas | Reglas efectivas tras aplicación |
| REF | Inventario, identidad propia, endpoints | Transformación/correspondencia de relación | Referencias exportadas e integridad | REF destino declarada y mapping | REF que A2 declara importar/resolver | REF materializada | Resolución e integridad efectiva de extremos |
| MET | Identidad/versiones contrato, instancia, fuente, snapshot y provenance | Versiones de transformación y artefactos | Identidad de export, formato y lineage | Identidad/versiones destino y mapping | Identidad de import declarado | Artefacto producido, hash y lineage | Registro de aplicación, snapshot y evidencia posterior |

La matriz es un **mapa de inspección**, no una declaración de presencia. F1/A1/F2/A2 no crean automáticamente objetos semánticos. La presencia en cada etapa requiere evidencia específica. `C_DST_DECLARED` no prueba `C_DST_APPLIED`; una diferencia de hash/nombre no prueba equivalencia funcional.

### Evidencia mínima y adjudicación
- **CMP:** identidad semántica y registro exacto, clase/rol, boundary_class cuando proceda, scope y pertenencia al snapshot; mapping explícito para correspondencias entre etapas.
- **PAR:** parameter_key, owner, tipo, estado ABSENT/NULL/DEFAULT/VALUE, valor cuando corresponda, requiredness y dominio/unidad activados; no colapsar estados.
- **RUL:** rule_id, AST tipado, scope explícito (incluido GLOBAL), efecto REQUIRE/FORBID y precedencia/temporalidad solo cuando aplique.
- **REF:** ref_id/registro propio, extremos tipados SOURCE/TARGET, dirección, tipo/rol, multiplicidad si procede, pertenencia al paquete y provenance. No elevar EDGE, FK, ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos RUL, R_acc/R*, C_dep/E_dst ni refs RULE_DEFINED a REF funcional automáticamente.
- **MET:** identidades/versiones exactas, IAM_id/version/hash, mapping_id/version, oráculo/versión, timestamps y provenance de artefactos/evidencias. El hash es control de artefacto, no prueba semántica.

Estados por predicado y unidad de cobertura:
- `1`: presencia/condición acreditada por evidencia suficiente y coherente.
- `0`: ausencia/incumplimiento solo con búsqueda exhaustiva y cobertura COMPLETE del universo, etapa, ruta/scope y versión pertinentes.
- `?`: evidencia, resolución, mapping o cobertura insuficiente/contradictoria.
- `NA`: no aplicabilidad declarada ex ante en IAM, con fundamento de dominio; nunca por falta de evidencia.
- `NOT_COMPARABLE`: versiones/identidades sin mapping aprobado; no sustituir por 0.
- `NOT_APPLICABLE` solo cuando lo autorice el contrato aplicable, distinto de desconocido.

Para REF=0 se requiere inventario exhaustivo del límite funcional y cobertura exacta. La cardinalidad base permanece CMP≥1, PAR≥1, RUL≥1, REF≥0 y MET obligatorio; no se cambia por esta matriz. La aplicabilidad de una clase/propiedad en una etapa se decide con el contrato y el stage_key, no por extrapolación desde otra etapa.

### Exclusiones y salvaguardas
La inspección de CMP/PAR/RUL/REF se refiere al paquete P0. Entorno destino, runtime, recursos, permisos efectivos, C_dep y estados técnicos P1 se registran en sus objetos/mediciones correspondientes; no se incorporan al paquete ni se convierten automáticamente en REF. Las relaciones estructurales U_G (FK) siguen siendo distintas de REF. REF→EDGE requiere mapping M explícito/versionado; EDGE→REF no se infiere. Split/merge/n-aria exige identidad/grupo y regla de conservación explícitos.

### Estado actual
No se han inspeccionado snapshots reales ni se han asignado valores a ninguna celda. No se declara REF=0, cobertura COMPLETE, IAM sellado, cardinalidades adicionales, implementación, validación, fixtures, simulación o ejecución. La siguiente operación tras aceptación será completar el protocolo de extracción/registro de observaciones usando los snapshots existentes; si no hay snapshots, primero habrá que resolver esa ausencia sin fabricar datos.

## 84 — Hallazgo documental: plantilla U_G sin snapshots reales

**Estado:** HALLAZGO DOCUMENTAL / PROPUESTA DE GATE; sin datos observados ni decisión de implementación.

### Resultado de inspección
La plantilla canónica `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md` declara expresamente `DRAFT / PLANTILLA VACÍA / NO INVENTARIADA / NO EJECUTADA`. Sus filas ilustrativas son marcadores de esquema, no registros. El registro de snapshots contiene una fila de plantilla con `No capturado`; la matriz de cobertura está en `NONE` para sus dimensiones. Por tanto, en los artefactos revisados no hay snapshots C10-S reales utilizables ni evidencia de cobertura que permita iniciar extracción de observaciones. Esto no demuestra que no existan fuentes externas; significa que no están incorporadas ni referenciadas como observaciones U_G en esta rama.

### Hallazgo de proyección de clases
U_G dispone de diez registros canónicos: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. No hay tablas físicas independientes CMP, PAR, RUL, REF o MET. No se permite asumir equivalencias nominales:
- CMP: candidatos de representación en NODE según `semantic_role` y frontera, pero NODE no equivale automáticamente a CMP.
- PAR: no existe tabla PAR dedicada; la representación/serialización de propiedades debe quedar mapeada explícitamente a campos/artefactos y a su identidad de owner.
- RUL: PREDICATE registra predicados observados/analíticos; no equivale automáticamente a una regla declarativa RUL con AST, scope y efecto.
- REF: DEC-C10-077 distingue el objeto REF de EDGE y de FK estructural U_G. EDGE no es REF; REF→EDGE requiere mapping M explícito y versionado.
- MET: identidad, versión, snapshot y provenance se distribuyen entre campos de objetos, SNAPSHOT y EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK; MET no es una tabla ni un objeto homogéneo por defecto.

### Protocolo de extracción — cuando existan fuentes
1. Localizar la fuente original y registrar custodio, método, timestamp, versión/hash, alcance y limitaciones en EVIDENCE_REGISTER; no copiar secretos.
2. Verificar que corresponde al contrato/instancia exactos y al snapshot/fase temporal declarados. No emparejar por nombre, hash aislado ni `latest`.
3. Resolver el mapping clase conceptual→representación U_G mediante contrato explícito/versionado. Si no existe o no conserva semántica, adjudicar `UNKNOWN` o `NOT_COMPARABLE`, no forzar una fila.
4. Crear/actualizar registros U_G solo mediante el procedimiento autorizado; fijar snapshot y record IDs exactos, `stage_key`, ruta/scope y universo.
5. Registrar cada afirmación con CLAIM_EVIDENCE_LINK y EVIDENCE_REGISTER; cobertura con COVERAGE_REGISTER; evaluación/adjudicación separadas.
6. Mantener por separado declarado, producido y aplicado. Una fuente C_DST_DECLARED nunca acredita A2_DST_APPLIED.
7. Adjudicar 0 solo con búsqueda exhaustiva y COVERAGE_REGISTER COMPLETE para el universo, versión, etapa y scope exactos; ? ante falta de fuente/mapping/cobertura; NA solo por regla ex ante IAM.

### Gate previo a cualquier extracción
- Identificar fuente(s) real(es) y snapshots existentes; si no existen, definir por separado cómo se obtendrán y autorizar su captura.
- Resolver el crosswalk CMP/PAR/RUL/REF/MET↔U_G sin colapsar REF/EDGE ni RUL/PREDICATE.
- Confirmar identidad/versionado, stage_key, route/scope y snapshot pinning.
- Definir cobertura, evidencia y adjudicación por clase/etapa.
- Solo entonces completar observaciones. La plantilla no se rellena con ejemplos sintéticos ni valores inferidos.

**Conclusión:** no procede todavía extraer ni adjudicar observaciones. El siguiente trabajo documental es cerrar el crosswalk semántico de representación y especificar qué fuentes/snapshots alimentarán cada etapa. No se declara ausencia de objetos, REF=0, IAM sellado, cobertura COMPLETE ni disponibilidad de datos externos. `scientific_execution=false`; `execution_authorized=false`.

## 85 — Propuesta documental de proyección PAR en U_G

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión nueva, no implementada, sin instancias ni observaciones reales. Reutiliza DEC-C10-053/054/056/068/069/070/073/074/075/076 y el contrato abstracto de instancia, la matriz de mapping PAR y el overlay U_G existente. No sustituye ni amplía el schema físico U_G.

### 1. Decisión de diseño propuesta
Representar PAR como **propiedad atómica tipada del CMP propietario**, no como NODE independiente y no como EDGE/REF. La identidad semántica de cada parámetro es `parameter_key` dentro del contrato/versión y el ámbito de `owner_component_id`; la instancia observada se distingue por la tupla exacta de contrato/instancia, snapshot/record, stage_key, ruta/scope y versión del CMP owner. Esta opción evita inventar un `semantic_role=PARAMETER` (no existe en el vocabulario aceptado de NODE), evita tratar una propiedad escalar como componente y preserva el ownership ya definido.

La representación es una **fila lógica de manifiesto IAM/inspección**, usando la estructura de referencia ya descrita en U_G §18.3 (manifest_record_id, contract/instance, snapshot exacto, stage_key, route, object_class=PAR, semantic_id/version, owner_component_id, property_key/type/state/value, mapping, declared_or_applied, evidence, claim-evidence, coverage y adjudicación). No se crea una tabla física PAR ni una nueva capa semántica persistida. La fila de manifiesto no recibe por ahora un object_record_id U_G ni una FK nueva: el contrato de identidad de esa fila sigue OPEN.

### 2. Campos semánticos por PAR
Cada entrada lógica debe resolver, sin inferencia:
- `parameter_key` estable y no reutilizable para otro significado;
- `owner_component_id` exacto y su CMP NODE/record/version en el mismo snapshot;
- `type`, dominio/escala/unidad cuando proceda;
- `requiredness` y disparador condicional, si lo hubiera;
- `allowed_states` y estado observado, diferenciando ABSENT, NULL, DEFAULT y VALUE;
- `value` solo si el estado lo permite y procede de la fuente observada;
- `default_contract` (kind, origen, scope, precedencia y versión) solo cuando exista declaración;
- mapping_id/version, estado MAPPED/UNMAPPED/AMBIGUOUS/NOT_APPLICABLE y regla de conversión;
- evidencia, cobertura, adjudicación y procedencia exactas.

No colapsar ausencia, null, default declarado/heredado y valor explícito. `DEFAULT_ENV_RESOLVED` es resolución de E_dst/P1, enlazada al parámetro y snapshot ambiental, no un estado adicional del paquete P0 ni una reescritura de DEFAULT.

### 3. Especialización ya aceptada para el servicio sintético
El roster nuclear se limita a:
- `PAR-SVC-ENABLED`: BOOL, dominio `{false,true}`, REQUIRED.
- `PAR-SVC-PROFILE`: ENUM, dominio `{STANDARD, READ_ONLY, DISABLED}`, REQUIRED.

`PAR-SVC-RETRY-COUNT` queda fuera del núcleo confirmatorio por DEC-C10-068. No debe incorporarse al universo base ni usarse como proxy de capacidad P1. Para ENABLED y PROFILE, ABSENT/NULL no son admisibles; DEFAULT no queda declarado por DEC-C10-068 y solo podría usarse tras declaración contractual explícita, versionada y previa al IAM. No se asignan valores de escenario en este contrato de representación.

### 4. Proyección y enlaces con U_G
- El CMP propietario se resuelve a NODE exacto mediante `component_id/node_id + object_record_id + snapshot_id`; no se resuelve por nombre, rol lógico ni hash.
- La fila lógica PAR referencia ese owner y conserva `parameter_key` como identidad de propiedad. No crea un NODE adicional ni una arista EDGE.
- `COVERAGE_REGISTER` conserva scopes independientes `C10S_CONFIG_PAR` por snapshot×stage_key×ruta/scope, con universo/denominador explícitos. No combinar cobertura PAR con CMP.
- Como CLAIM_EVIDENCE_LINK no admite target_type=PAR, la propuesta es vincular la afirmación a la revisión exacta del NODE owner y/o al COVERAGE_SCOPE correspondiente; `claim_statement` y `relevance_scope` deben identificar inequívocamente `parameter_key`, propiedad, estado y etapa. No se añade un nuevo FK ni se finge que la evidencia apunta a una tabla PAR.
- EVIDENCE_REGISTER conserva fuente, versión, método, integridad y límites; no copiar valores sensibles ni credenciales.
- M mantiene la correspondencia `parameter_key_src → parameter_key_dst`, owner, tipo, dominio, unidad, estado, valor/default y conversión. M es artefacto evaluativo versionado, no EDGE ni una capa semántica adicional.

### 5. Evaluación independiente y etapas
La comparación se realiza por parámetro y etapa, preservando la separación:
- C_SRC: contrato/propiedad fuente observada.
- F1_S2 y A1_S1: representación intermedia producida por cada ruta.
- F2_DST_DECL y A2_DST_DECL: propiedad destino declarada, no aplicada.
- F2_DST_APPLIED y A2_DST_APPLIED: propiedad efectivamente observada tras aplicación.

La evidencia de una etapa no se traslada a otra. El mismo `parameter_key` lógico no prueba por sí solo correspondencia; M debe resolver el owner y la transformación tipada. La equivalencia de valor no compensa una diferencia de tipo, dominio, unidad, estado o default. El analizador no accede a truth oculta ni a etiquetas del oráculo.

### 6. Adjudicación y límites
`1` exige predicado satisfecho con evidencia/cobertura suficiente; `0` exige incumplimiento confirmado o ausencia exhaustiva según el predicado; `?` ante falta de fuente, owner, mapping, snapshot o cobertura; `NA` solo por no aplicabilidad ex ante IAM. `NOT_COMPARABLE` cuando versiones/identidades no tengan mapping aprobado. Una propiedad ausente en el artefacto no equivale a ausencia de observación ni autoriza imputar valor/default.

La propuesta no fija cardinalidades adicionales, no asigna REQUIRED/OPTIONAL nuevos, no cambia DEC-C10-068, no aprueba el roster fuera del núcleo ya aceptado, no añade semantic_role, tabla PAR, FK, EDGE ni REF, no sella IAM, no define serialización ni hash, y no autoriza parser, validator, fixtures, implementación, Design Freeze o ejecución.

### 7. Cuestiones aún abiertas
1. Identidad/versionado de la fila lógica de manifiesto PAR y su relación exacta con el registro IAM sellado.
2. Regla formal para claim_statement/relevance_scope que haga inequívoca la referencia a parameter_key sin crear FK PAR.
3. Mapping concreto de owner y property_key entre representaciones fuente/destino e intermedias.
4. Evidencia disponible por etapa y cobertura real.
5. Defaults y sus reglas por clave, si alguna vez se incorporan; no se presuponen.

## 86 — Propuesta de identidad de fila lógica PAR

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión, no implementada y sin filas/observaciones reales. Resuelve la laguna de identidad detectada en §§19.2/19.19 y §17, sin extender DEC-C10-062 ni modificar el schema U_G.

### 1. Separación de identidades
La fila lógica PAR del manifiesto no es una entidad U_G de las tablas NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. Por tanto:
- `parameter_key` identifica la propiedad semántica en el ámbito de contrato/versión y owner CMP; no identifica una observación.
- `manifest_record_id` identifica una fila concreta e inmutable del manifiesto; es opaco, no vacío y único dentro del manifiesto/versionado IAM que la contiene. No reutilizar `object_record_id`, `node_id`, `component_id` ni IDs TID/SID/RID/EID.
- La clave lógica de captura PAR queda propuesta como la tupla exacta: contract_id/version + instance_id/version + snapshot_id/snapshot_object_record_id + stage_key + route_id/route_record_id o ausencia justificada + scope/universe revision + owner_component_id y revisión exacta del CMP + parameter_key/semantic_version. Esta clave delimita qué observación se está representando; no sustituye a manifest_record_id.
- `coverage_scope_id` sigue siendo identidad del scope de cobertura, independiente de la fila PAR.

### 2. Revisión y corrección
Se propone que cada fila sea inmutable. Una corrección de captura, adjudicación o metadato de la fila no sobrescribe el registro previo: crea un nuevo `manifest_record_id`, incrementa `manifest_record_revision` en uno para la misma clave lógica y señala el registro inmediatamente anterior mediante `supersedes_manifest_record_id`. La primera revisión es 1 y no tiene predecesor. Solo puede existir una cadena lineal por clave lógica; no se admiten bifurcaciones, ciclos, saltos, referencias cruzadas entre claves o snapshots ni reutilización de IDs. El historial se conserva.

Una nueva observación en otro snapshot, etapa, ruta/scope, versión de owner o versión contractual no es una revisión de la misma fila: constituye una nueva clave lógica y comienza revisión 1. Un cambio semántico de parameter_key o de significado exige nueva identidad de parámetro conforme al contrato, no supersession de captura.

Los campos `manifest_record_revision` y `supersedes_manifest_record_id` son nombres propuestos de contrato lógico, no columnas físicas aprobadas. La propuesta no fuerza un `object_version` ni `supersedes_record_id` U_G.

### 3. Límite de DEC-C10-062
DEC-C10-062 se aplica expresamente solo a NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT; las demás tablas mantienen sus propias claves y contratos. No puede extenderse por analogía a filas de manifiesto. La mención histórica en §19.2 de que manifest_record_id sería versionado “conforme a DEC-C10-062 si se adopta” queda aclarada por esta propuesta: el manifiesto necesita contrato propio y no hereda object_version/supersedes_record_id de U_G. Esta aclaración no altera la decisión aceptada ni la reescribe; precisa el límite de su ámbito.

### 4. Unicidad y control
Para una misma clave lógica y revisión debe existir exactamente un manifest_record_id; un manifest_record_id no puede identificar dos claves/revisiones. Toda referencia a una fila debe resolver por ID exacto dentro de la versión de manifiesto/IAM fijada, nunca por latest, posición, nombre o hash aislado. La verificación documental deberá comprobar:
- no duplicidad de manifest_record_id;
- unicidad de clave lógica + manifest_record_revision;
- revisión inicial 1 sin predecesor;
- sucesión inmediata y misma clave lógica para revisiones posteriores;
- ausencia de ciclos, bifurcaciones, huérfanos y referencias futuras;
- pinning exacto del snapshot y del CMP owner;
- coherencia de coverage_scope_id con la misma tupla de etapa/ruta/clase/universo;
- preservación de múltiples evidencias como vínculos separados, no serializadas en la fila.

No se impone unicidad global entre distintas versiones de manifiesto/IAM; el namespace exacto y su versión forman parte de la resolución.

### 5. Estados de propiedad y ausencia
Una fila PAR representa una propiedad esperada/inspeccionada, no presupone que la propiedad esté presente en el artefacto. `state=ABSENT` puede registrarse solo con evidencia/cobertura según el predicado; no se elimina la fila por ausencia. `NULL`, `DEFAULT` y `VALUE` permanecen distintos. El registro de una revisión no convierte por sí mismo ? en 0 ni acredita COMPLETE.

### 6. Límites
No se crea tabla PAR, no se añaden columnas U_G, no se aprueba DDL/serialización/API/parser/validator/fixtures, no se asignan valores de escenario ni se instancia el manifiesto. La aceptación de esta propuesta, si se produce, será documental y no autorizará implementación ni ejecución. IAM permanece sin sellar; `scientific_execution=false`; `execution_authorized=false`.

### 7. Pendientes para aceptación
- Confirmar namespace de unicidad: por versión de manifiesto/IAM (propuesta) frente a global en toda la línea C10-S.
- Confirmar si la revisión de captura es necesaria o si bastaría append-only con IDs nuevos y relación de supersession.
- Confirmar nombre final de los campos de revisión y predecesor.

## 87 — Recomendación de adjudicación pendiente PAR

**Estado:** RECOMENDACIÓN PARA ACEPTACIÓN DEL USUARIO; no es DEC aceptada ni contrato congelado. Se propone resolver conjuntamente las tres cuestiones abiertas de §17.1/§19.20/§20/§16.62/§80/§207/§86.

### Recomendación única
1. **Unicidad de `manifest_record_id`: global en toda la línea C10-S**, independiente de versión IAM/manifest. El ID es opaco, inmutable y nunca se reutiliza. La versión IAM sigue formando parte de la resolución contextual de la fila, pero no limita la unicidad del identificador. Se recomienda unicidad global porque simplifica referencias, auditoría y detección de colisiones entre versiones; no implica que el registro sea una entidad U_G.
2. **Modelo append-only con revisión explícita.** Cada corrección/adjudicación posterior genera nuevo `manifest_record_id`; no se sobrescribe ni elimina la fila anterior. Para una misma clave lógica de observación, `manifest_record_revision` empieza en 1 y aumenta exactamente en uno. Las revisiones posteriores incluyen `supersedes_manifest_record_id` apuntando a la revisión inmediatamente anterior. Una sola cadena lineal por clave lógica; sin bifurcaciones, ciclos, saltos ni huérfanos. La revisión es metadato de secuencia de captura, no versión semántica del parámetro.
3. **Nombres recomendados:** `manifest_record_revision` y `supersedes_manifest_record_id`, exactamente así. `manifest_record_id` se mantiene como identificador del registro, distinto de `parameter_key`, CMP owner, `object_record_id` U_G y `coverage_scope_id`.

### Reglas para evitar revisiones falsas
- Nueva etapa, snapshot, ruta/scope, contrato/instancia o revisión del CMP owner = nueva clave lógica y revisión 1, no supersession.
- Cambio de significado de `parameter_key` = nueva identidad semántica; no se corrige como revisión de captura.
- Corrección de transcripción, evidencia, estado, mapping o adjudicación de la misma captura lógica = nueva revisión, conservando la anterior.
- Varias evidencias para una misma fila son vínculos independientes; no crean revisiones por sí solas.
- Un cambio de versión IAM que solo reempaqueta la misma fila no genera automáticamente una nueva observación. Si la identidad lógica de captura permanece idéntica, la política de migración/referencia deberá conservar el ID; si cambia una dimensión de la clave lógica, comienza una nueva cadena. La migración entre versiones IAM requiere mapping explícito y no se presume.

### Condición de aceptación
La aceptación confirmaría solo este contrato lógico documental de identidad/supersession. No crea columnas, tabla PAR, DDL, serialización, generador de IDs, API, parser, validator, fixtures ni registros reales; tampoco sella IAM, cierra el crosswalk PAR↔U_G, autoriza implementación o cambia `scientific_execution=false` / `execution_authorized=false`.

**Pendiente de aceptación expresa:** unicidad global; append-only + revisión explícita; nombres exactos indicados.

## 88 — DEC-C10-079: aceptación de identidad global y supersession PAR

**Estado:** ACEPTADO — DEC-C10-079. Esta sección propaga el contrato lógico aprobado; prevalece sobre cualquier recomendación previa que mantuviera abiertas estas cuestiones.

- `manifest_record_id`: globalmente único en toda la línea C10-S, opaco, inmutable y nunca reutilizado, independiente de la versión IAM.
- Append-only: ninguna fila se sobrescribe ni elimina. Toda corrección de la misma captura lógica crea un nuevo ID y conserva el anterior.
- `manifest_record_revision`: revisión secuencial por clave lógica, desde 1, sin saltos.
- `supersedes_manifest_record_id`: en revisiones posteriores, referencia a la revisión inmediatamente anterior de la misma clave lógica. Cadena lineal única, sin bifurcaciones, ciclos, huérfanos ni referencias cruzadas.
- Cambio de snapshot, etapa, ruta/scope, contrato/instancia o revisión del CMP owner inicia una nueva clave lógica y revisión 1. Cambio semántico de `parameter_key` exige nueva identidad semántica.
- Múltiples evidencias no crean revisiones por sí solas. Reempaquetar en nueva versión IAM no crea automáticamente nueva observación; migración exige mapping explícito.

**Límites:** decisión documental lógica. No crea tabla/columnas PAR o U_G, DDL, serialización, generador, API, parser, validator, fixtures ni registros reales; no sella IAM, no cierra PAR↔U_G, no autoriza Design Freeze, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 89 — Propuesta de binding probatorio PAR

**Estado:** PROPUESTA DOCUMENTAL; no aceptada como nueva DEC, no implementada, sin registros observados. Reutiliza DEC-C10-079 y el esquema U_G §12.2–12.3/§18.3–18.8. No amplía los dominios ni las FK de U_G.

### 1. Principio
CLAIM_EVIDENCE_LINK no tiene target_type PAR ni FK a manifest_record_id. No se simula una FK inexistente. La trazabilidad se compone de:
(a) FK real a COVERAGE_SCOPE (y, cuando la afirmación se refiere al owner CMP como objeto por derecho propio, un vínculo separado al NODE owner);
(b) localizador lógico exacto de la fila PAR en claim_statement/relevance_scope;
(c) control independiente que resuelve ese localizador contra el manifiesto IAM versionado y verifica su integridad.

### 2. Perfil normativo propuesto para una afirmación sobre una fila PAR
Una fila CLAIM_EVIDENCE_LINK por cada evidencia × afirmación × fila PAR:
- `claim_target_type=COVERAGE_SCOPE`;
- `target_coverage_scope_id` = scope PAR exacto, cuyo `dimension=C10S_CONFIG_PAR` y cuyo universe_definition/version fija contrato/instancia, snapshot+record, stage_key, route/scope, clase PAR y universo;
- todos los campos target_* no aplicables quedan vacíos; no se rellenan FK de NODE como sustituto de PAR;
- `claim_statement` identifica explícitamente el predicado y la fila: `PAR_ROW|manifest_record_id=<ID>|manifest_record_revision=<N>|parameter_key=<KEY>|owner_component_id=<CMP_ID>|predicate=<PREDICATE>`;
- `relevance_scope` identifica el contexto completo: `contract_id/version;instance_id/version;snapshot_id/snapshot_object_record_id;stage_key;route_id/route_record_id-or-justified-NONE;coverage_scope_id;owner_component_id/owner-record/version;parameter_key;manifest_record_id;manifest_record_revision`.
Los literales anteriores describen un perfil documental de campos textuales existentes, no una gramática física ni un parser aprobado. No se deben usar separadores/valores ambiguos; si algún identificador contiene delimitadores, la serialización futura tendrá que definir escaping/versionado antes de automatizar.

### 3. Resolución y controles independientes
El control debe resolver manifest_record_id globalmente (DEC-C10-079), verificar revision y supersession, y comprobar igualdad exacta entre la fila del manifiesto, su clave lógica, owner CMP, snapshot, stage_key, route/scope y coverage_scope_id. También verifica:
- dimension C10S_CONFIG_PAR y universe_definition/version compatibles;
- que el scope corresponde a la misma tupla y no está compartido entre snapshots/etapas/rutas/clases;
- que el CMP owner resuelve al NODE/object_record_id/snapshot exactos;
- que parameter_key y manifest_record_revision coinciden con el manifiesto;
- que la evidencia está en EVIDENCE_REGISTER y que la relación 1:N se conserva sin listas serializadas;
- que la evidencia realmente respalda el predicado y estado citados; un enlace FK correcto no prueba el contenido.
Un fallo de resolución, contradicción o colisión es FAIL; falta de manifiesto, snapshot, scope o fuente es UNKNOWN/?; incompatibilidad de versiones sin mapping es NOT_COMPARABLE; NA solo por inaplicabilidad ex ante. No inferir 0 desde falta de vínculo.

### 4. Owner CMP y cobertura
Si una misma evidencia respalda también una afirmación distinta sobre identidad/estado del CMP owner, se crea otro CLAIM_EVIDENCE_LINK con target NODE y su FK exacta. No se duplica ni se mezcla esa afirmación con la afirmación PAR. La afirmación PAR conserva COVERAGE_SCOPE como target FK y el localizador PAR en campos textuales.
COVERAGE_REGISTER permanece por clase PAR y por snapshot×stage_key×ruta/scope; COMPLETE exige denominador, fuentes, enumeración y excepciones conforme a §18.6. El link a un scope no convierte automáticamente el scope en COMPLETE.

### 5. Límites y decisiones abiertas
No se añade target_type PAR, FK, tabla PAR, columna U_G, tabla puente ni relación física nueva. No se crea CLAIM_EVIDENCE_LINK directo a manifest_record_id; su resolución es un control independiente contra el manifiesto. No se define todavía escaping/canonicalización del localizador, vocabulario de predicate ni automatización. No se sella IAM, no se declara cobertura, no se crean registros y no se autoriza parser, validator, fixtures, implementación o ejecución.
Pendiente de aceptación: perfil COVERAGE_SCOPE + localizador en claim_statement/relevance_scope; vínculo NODE separado solo para afirmaciones propias del CMP; control independiente de resolución.

## 90 — DEC-C10-080: binding probatorio PAR

**Estado:** ACEPTADO — DEC-C10-080. Sustituye el estado pendiente de aceptación de §17.4/§19.23/§23/§16.65/§83/§210/§89.

- Afirmación sobre fila PAR: CLAIM_EVIDENCE_LINK usa `claim_target_type=COVERAGE_SCOPE` y FK `target_coverage_scope_id` al scope exacto `dimension=C10S_CONFIG_PAR`.
- `claim_statement` y `relevance_scope` contienen localizador lógico suficiente para resolver `manifest_record_id`, `manifest_record_revision`, `parameter_key`, owner CMP, snapshot/record, `stage_key`, ruta/scope y universo/version.
- Una fila CLAIM_EVIDENCE_LINK por evidencia×afirmación×fila PAR. Las evidencias múltiples se conservan como filas separadas, nunca como listas embebidas.
- Control independiente resuelve ID global y verifica revisión/supersession y coincidencia exacta de clave lógica, owner, snapshot, etapa, ruta/scope, coverage scope, universo, predicado y evidencia.
- Una afirmación separada sobre el CMP owner usa otro CLAIM_EVIDENCE_LINK con target NODE y FK exacta. No sustituye el target COVERAGE_SCOPE de la afirmación PAR.
- El enlace al scope no implica COVERAGE COMPLETE; se aplican U_G §12.3/§18.6.

**Restricciones:** no se añade target_type PAR, FK, tabla o puente. No se aprueban gramática, escaping, canonicalización, serialización, parser ni automatización. Los campos singulares `evidence_id`/`claim_evidence_id` del manifiesto no sustituyen el registro 1:N de CLAIM_EVIDENCE_LINK. No se crean observaciones, no se sella IAM, no se declara cobertura ni se autoriza implementación/ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 91 — Propuesta de control independiente PAR

**Estado:** PROPUESTA DOCUMENTAL; pendiente de aceptación. Desarrolla DEC-C10-080 reutilizando el C0 ya especificado en el protocolo de evidencia §19; no crea un segundo control genérico.

Se separan cinco capas: C0_SCOPE; PAR_ROW_BINDING; EVIDENCE_LINK_INTEGRITY; EVIDENCE_RELEVANCE; COVERAGE_COMPLETENESS. Se define una secuencia P0–P11 para aplicabilidad, target, resolución C0, dimensión/universo, identidad PAR global, clave lógica/pinning, supersession DEC-C10-079, evidencia, correspondencia de afirmación, pertinencia sustantiva, vínculo NODE separado solo si hay afirmación propia del owner y cobertura.

El control conserva resultados PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA por capa, sin colapsarlos. Un registro histórico superseded conserva validez histórica, pero no acredita estado actual sin justificación temporal. Una FK correcta no prueba pertinencia; un scope COMPLETE tampoco se infiere del vínculo.

Se añaden 18 casos adversariales documentales y requisitos de informe. Se reconocen expresamente las limitaciones ya detectadas en §20.1–20.5: mappings stage_key, clase y ruta aún abiertos producen UNKNOWN donde impiden resolución inequívoca.

No se amplía U_G ni se cierra gramática/escaping/canonicalización/predicate. No crea fixtures, parser, validator ni registros. No autoriza implementación, Design Freeze, validación técnica ni ejecución. `scientific_execution=false`; `execution_authorized=false`.

 
## 92 — DEC-C10-081: aceptación del protocolo de control independiente PAR

**Estado:** ACEPTADA — DEC-C10-081 (2026-11-08).

Se acepta §20.18 del protocolo de evidencia como contrato lógico documental del control independiente PAR. Comprende reutilización de C0 §19; cinco capas separadas; entradas mínimas; secuencia P0–P11; identidad y supersession conforme a DEC-C10-079; resultados por capa PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA; separación entre integridad, pertinencia y cobertura; 18 casos adversariales y requisitos de informe.

**Límites:** no amplía U_G, no cierra mappings stage_key/clase/ruta ni gramática/escaping/canonicalización/predicate, y no crea registros o fixtures. No autoriza parser, validator, scripts, SQL, implementación, Design Freeze, validación técnica ni ejecución. `scientific_execution=false`; `execution_authorized=false`.


## 93 — DEC-C10-082: aceptación del anclaje CMP↔NODE 1:1 por snapshot

**Estado:** ACEPTADA — DEC-C10-082 (2026-11-08).

Se acepta el contrato lógico del crosswalk §10.7: cardinalidad 1:1 del anclaje por CMP y snapshot exacto, unicidad en ambos sentidos, NODE subordinados no considerados CMP sin identidad propia, continuidad entre snapshots mediante `component_id` contractual y mappings separados. `stage_key`/ruta califican cobertura y no multiplican la identidad NODE.

La adjudicación conserva PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA según las condiciones documentadas. PASS de correspondencia no demuestra verdad PAR, preservación, pertenencia a ruta ni completitud.

**Límites:** no completa roster CMP, mappings P1/PAR ni IAM; no crea registros ni cambia U_G; no autoriza poblar IAM, parser, validator, implementación, Design Freeze o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 94 — DEC-C10-083: aceptación de aplicabilidad PAR por stage_key

**Estado:** ACEPTADA — DEC-C10-083 (2026-11-08).

Se aceptan para `PAR-SVC-ENABLED` y `PAR-SVC-PROFILE` las obligaciones por las siete etapas DEC-C10-071: P0 REQUIRED; VALUE tipado en posiciones declarativas; preservación semántica independiente en F1/A1; evidencia del estado efectivamente aplicado en F2/A2. No hay DEFAULT contractual; ABSENT/NULL no son admisibles si la ausencia está demostrada con cobertura suficiente. Falta de evidencia/cobertura → UNKNOWN; runtime no es `stage_key`.

La aceptación no adjudica observaciones ni asigna valores por escenario, no sella IAM y no autoriza mappings físicos, implementación ni ejecución científica. Véase DEC-C10-083.

## 95 — DEC-C10-084: aceptación del contrato de equivalencia semántica PAR

**Estado:** ACEPTADA — DEC-C10-084 (2026-11-08).

Se acepta matriz abstracta §15.1–15.2: identidad BOOL exacta; biyección total, inyectiva y versionada ENUM entre STANDARD/READ_ONLY/DISABLED; separación de estado y valor; preservación independiente de `RUL-SVC-ENABLE-PROFILE-01); evaluación independiente F1/A1; y separación entre configuración destino declarada y aplicación efectiva F2/A2.

La composición requiere mappings explícitos/versionados, sin inferir transitividad ni comparar literales físicos de namespaces distintos. La aceptación no fija codificaciones ni mappings físicos, no adjudica observaciones, no sella IAM y no autoriza implementación, Design Freeze ni ejecución científica. Véase DEC-C10-084.


## DEC-C10-085 — Aceptación de predicados de adjudicación PAR en F1/A1

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta el contrato de §15.3 de la matriz abstracta para C_SRC→F1_S2 y C_SRC→A1_S1, con reconciliación obligatoria de las cinco familias organizadoras con SM/FP aceptado (DEC-C10-055), sin predicados confirmatorios duplicados ni doble contabilización. F1 y A1 se adjudican independientemente; el resultado conserva el vector de estados por predicado.

Se mantienen BOOL exacto, biyección ENUM total/versionada, preservación semántica RUL, binding exacto CMP/snapshot/etapa/ruta/scope/mapping y suficiencia probatoria. PASS exige evidencia y cobertura suficientes; FAIL exige contradicción demostrada con cobertura suficiente; UNKNOWN refleja insuficiencia; NOT_COMPARABLE incompatibilidad sin mapping aprobado; NA solo inaplicabilidad ex ante (no admisible para estos elementos en el contrato base).

No se definen mappings físicos ni observaciones; no se sella IAM ni se autoriza implementación, Design Freeze o ejecución científica. Véase `00_GOVERNANCE/decisions/DEC-C10-085_PAR_F1_A1_ADJUDICATION_PREDICATES_ACCEPTANCE.md`.

## DEC-C10-086 — Aceptación de conformidad del destino declarado y de la transición F1/A1→F2/A2

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta la matriz abstracta §15.5 y el crosswalk §10.15. Se separan dos dimensiones no compensables: P-DECL, equivalencia semántica del destino declarado frente a F1/A1; y P-TRANS, evidencia íntegra y trazable de que la transición identificada produjo el artefacto declarado exacto. F y A se adjudican independientemente, conservando vectores por parámetro/regla/predicado y reconciliación SM/FP sin duplicidad.

Se aplican BOOL exacto, biyección ENUM total/versionada y preservación semántica RUL. PASS exige demostración suficiente; FAIL contradicción demostrada con cobertura suficiente; UNKNOWN insuficiencia; NOT_COMPARABLE incompatibilidad sin mapping aprobado; NA solo inaplicabilidad ex ante (no admisible para los PAR/RUL del contrato base). La equivalencia de artefactos no demuestra lineage. F2/A2 declaradas no prueban aplicación efectiva, que permanece en FP-06/FP-07 y etapas applied.

No se definen mappings físicos ni se sella IAM; no se autoriza parser, validator, implementación, Design Freeze o ejecución científica. Véase el Decision Record DEC-C10-086.

## DEC-C10-087 — Aceptación de aplicación efectiva y verificación post-aplicación F/A

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta §15.7 y §10.17 para F2_DST_DECL→F2_DST_APPLIED y A2_DST_DECL→A2_DST_APPLIED. Se reutilizan FP-06 (aplicación efectiva), FP-07 (observación post-aplicación) y FP-08 (procedencia/identidad/reproducibilidad), sin crear predicados confirmatorios paralelos. FP-06 requiere evidencia trazable del evento y destino; FP-07 observación del estado aplicado exacto y evaluación mediante FP-01…05; FP-08 soporta la procedencia sin sustituir los otros dos.

F y A se adjudican independientemente. La falta de registro no demuestra no aplicación; UNKNOWN salvo evidencia autoritativa/exhaustiva o contradicción positiva. FP-06 PASS no implica FP-07 PASS. Se reportan por separado aplicación, post-check, procedencia y vector FP-01…05, sin doble contabilización.

No se define herramienta, observación, oráculo, tolerancias o mapping físico; no se sella IAM ni se autoriza implementación, Design Freeze o ejecución científica. Véase el Decision Record DEC-C10-087.

## DEC-C10-088 — Aceptación de integración temporal de adjudicaciones F/A

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta la integración de la matriz temporal §14, matriz abstracta §15.9 y crosswalk IAM §10.19. Consolida por ruta F/A tres tramos: C_SRC→F1/A1 (DEC-C10-085); F1/A1→F2/A2 declaradas con P-DECL/P-TRANS (DEC-C10-086); y F2/A2 declaradas→aplicadas con FP-06/07/08 (DEC-C10-087). `stage_key`, reloj DGP, SNAPSHOT.phase y step_k son ejes distintos; la evidencia no se transfiere automáticamente entre etapas/rutas/afirmaciones. Se mantienen PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA, no compensación, cobertura epistémica y ausencia de inferencia causal automática hacia ACC/Reach/ΔT_acc→Value.

Aceptación documental únicamente. No sella IAM, no declara Design Freeze y no autoriza parser, validator, implementación ni ejecución científica. Véase DEC-C10-088.

## DEC-C10-089 — Identidad de unidad lógica raíz y relación con CMP

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta NODE raíz `LOGICAL_SERVICE_UNIT` como representación de la unidad lógica de servicio, separada conceptualmente del host/entorno y de S0, que se representa como SNAPSHOT basal con pinning exacto. La relación entre NODE raíz y CMP-SERVICE-LOGIC-001 queda OPEN: no se presume identidad ni separación; requiere mapping explícito, versionado y sustentado, compatible con DEC-C10-082.

No se asignan IDs ni se crean registros; no se sella IAM, no se declara roster exhaustivo ni cobertura y no se autoriza acceso técnico, captura, implementación, Design Freeze o ejecución científica. Véase DEC-C10-089.
## DEC-C10-090 — Descomposición semántica de N07: endpoint, interfaz y servicio

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta separar N07 en endpoint técnico, contrato/interfaz y servicio proveedor. Endpoint no implica CMP/REF; interfaz solo es REF con identidad propia y extremos tipados; servicio solo es CMP con identidad contractual, lifecycle y frontera autónomos. Los servicios externos no ingresan al roster CMP interno por mero consumo; EDGE y REF no se infieren entre sí.

Instancias, identidades, mappings, rutas, snapshots, cobertura y evidencia permanecen OPEN/UNKNOWN. No se crean registros ni se autoriza inspección, implementación, Design Freeze o ejecución. Véase DEC-C10-090.
## DEC-C10-091 — Descomposición semántica de N14: formato, payload y transferencia

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta refinar N14 existente separando formato/contrato versionado, payload concreto y eventos temporales de transferencia/recepción/parseo/validación/aplicación. Formato y payload tienen identidad/versionado separados; N13/A1 produce, N15/A2 consume, N07 conserva canal y M mapping. E12/E13 siguen candidatas. Hash no demuestra equivalencia semántica; JCS de DEC-C10-074 no se extiende al payload. Recepción no implica validación ni aplicación.

Permanecen OPEN formato y objetos/eventos reales, mapping, compatibilidad, aplicación, evidencia y cobertura. No se crean IDs ni se autoriza captura, implementación, Design Freeze o ejecución. Véase DEC-C10-091.

## DEC-C10-092 — Aceptación conceptual de N15: importador A2

**Estado:** ACCEPTED — DOCUMENTAL. **Fecha:** 2026-11-08.

Se acepta la descomposición conceptual N15 propuesta en el crosswalk IAM↔U_G §10.29: capacidad/contrato A2, implementación concreta y ejecución temporal son planos distintos; recepción efectiva, parseo, validación estructural/semántica, resolución M, aplicación FP-06, verificación FP-07 y procedencia FP-08 son hitos distintos. N15 no se presume CMP autónomo; requiere identidad contractual, lifecycle y frontera autónomos para serlo.

Se reutilizan DEC-C10-071/086/087/088, los siete stage_key y FP-01…08. No se crean nuevos predicados confirmatorios. F/A se adjudican independientemente; evidencia no heredable entre etapas/rutas; ausencia de registro no demuestra ausencia de evento.

La aceptación cierra solo la descomposición conceptual. Permanecen abiertos protocolo/implementación A2, formato/parser, validación, mapping físico, destino, eventos reales, snapshots, cobertura y evidencia. No crea IDs, registros ni columnas, no sella IAM y no autoriza captura, pruebas, implementación, Design Freeze o ejecución.

**Propagación:** crosswalk IAM↔U_G §10.30; Closure Control Matrix §98; Plan de cierre §16.80.

## DEC-C10-095 — Arquitectura A/B para el alcance de Value en C10-S (2026-11-11)

**Estado:** ACCEPTED — DESIGN-ARCHITECTURE ONLY. La aceptación explícita del usuario establece A como DGP base inalterado y autoriza diseñar B como extensión sintética independiente y versionada. B no altera DEC-C10-068 ni el roster de A. No se infieren beneficiarios, preferencias, indicadores, dimensiones, escalas, pesos, horizontes, DAG ni parámetros. A puede estudiar accesibilidad, Reach, trayectorias y Outcomes técnicos cuando se operacionalicen; no puede probar ΔT_acc→Value mientras Value no esté instanciado. B podrá probar únicamente la recuperación de la relación estipulada en su DGP, sin validez externa. P179 conserva Value vectorial y trade-offs; P182/P183 siguen como contratos transversales. Consecuencias: C separa Outcomes A y Value B; D consume contratos versionados sin filtrar truth al Analyzer; E integra solo tras cierre semántico y de medición. MED-02/03 OPEN; no Design Freeze, implementación, fixtures, simulación ni ejecución. scientific_execution=false; execution_authorized=false. Véase DEC-C10-095.


## Nota de seguimiento — C10S-B-VALUE-MIN-001 (2026-11-11)

Se registra como propuesta documental derivada de DEC-C10-095, no como decisión sustantiva aceptada. C10S-B-VALUE-MIN-001 define condiciones mínimas de admisibilidad del beneficiario sintético y Value en B; deja OPEN tipo/identidad, relación, cardinalidad, demanda pre-Z, consecuencia, perspectiva/autoridad, dimensiones, regla, escala, horizonte y parámetros. Mantiene separados unidad experimental, unidad de servicio, beneficiario, actor ejecutor y evaluador; impide inferir beneficiario desde CMP.owner/actor. Demanda no es uso; V_j no recodifica A/Reach/O técnico ni introduce circularidad. C/D/E reciben consecuencias documentales, sin schema físico ni implementación. No se acepta todavía ninguna instancia B ni se seleccionan dimensiones o reglas. Véase el contrato en C10S-B-VALUE-MIN-001.


## Nota de seguimiento — aceptación de B1 como tipo candidato (2026-11-11)

El usuario acepta B1 —entidad solicitante sintética del servicio— como tipo candidato para desarrollar la variante B. No es aceptación de instancia cerrada ni de dimensiones/reglas/medidas. Necesidad/objetivo pre-Z, solicitud, procesamiento técnico y consecuencia valorada permanecen separados. Solicitante y beneficiario coinciden solo por estipulación explícita en B1. No solicitud/no ejecución no implica ausencia de demanda ni Value cero; procesamiento correcto/O-CONF no equivale a Value. Véase C10S-B1-REQUESTER-CANDIDATE-001.


## Nota de seguimiento — reconciliación de demanda basal B1 (2026-11-11)

Se registra una distinción semántica propuesta, no una instancia confirmatoria ni un cambio de estimando. Need_preZ es la necesidad/objetivo focal de la entidad solicitante-beneficiaria en truth antes de Z; E_req_preZ es elegibilidad de petición aún OPEN; Request_event es la petición registrada con ventana temporal OPEN; D_resource es demanda operativa de recursos/capacidad ya existente en DGP y no representa necesidad del beneficiario. Need_preZ no equivale a E_i/P*_tau2/P*_F; no solicitud no implica ausencia de necesidad; truth 1/0/? y evidencia observada permanecen separadas. No filtrar ITT por Request_event y no asignarlo a t5/t6/t7 sin reconciliar reloj/DAG. P*_tau2/P*_F, D2 primario candidato/D1 secundario y DEC-C10-066/067 permanecen intactos. Véanse B1 spec §10, POP-CMP §10, DGP temporal §14 y matriz C-Value §16.


## Nota de seguimiento — ciclo de vida de solicitud B1 (2026-11-11)

Se registra como propuesta documental la separación entre Request_opportunity, Request_attempt, Request_received, Request_admitted/rejected, Request_processing, Request_response y Beneficiary_consequence. No son equivalentes a t5/t6/t7 ni a Outcome/Value. La cardinalidad request↔trajectory y el protocolo de servicio siguen OPEN. Se recomienda, sin aceptación aún, una carga de oportunidades/peticiones estandarizada ex ante mediante harness idéntico entre brazos; esto es probe de carga, no demanda natural. La rama de envío endógeno queda como adversarial/secundaria. No filtrar ITT por eventos post-Z. No cambia D2 primario candidato/D1 secundario, DEC-C10-066/067, reloj ni autorización. Véanse B1 spec §11 y documentos crosswalk relacionados.


## DEC-C10S-B1-REQUEST-MODE-001 — decisión aceptada

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.


## DEC-C10S-B1-UNIT-001 — entidad B1 por UE (2026-11-11)

**Decisión:** `DEC-C10S-B1-UNIT-001` — **ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN**.

Se acepta provisionalmente una entidad B1 por unidad experimental (UE), vinculada de forma explícita, unívoca, versionada y trazable a una instancia lógica de servicio aislada. La UE sigue siendo la instancia sintética completa a la que se asigna Z y para la que se generan estados transformacionales, trayectorias, Outcome y Value. La entidad B1 es el referente sintético de necesidad/objetivo pre-Z y de la consecuencia potencialmente valorable; no se confunde con la UE, el servicio ni el actor ejecutor.

La instancia de servicio deberá ser aislada respecto de otras UE en recursos, agentes, información, infraestructura, estado y canales de transmisión. La condición de aislamiento es una hipótesis de diseño que deberá justificarse y auditarse, no una propiedad presumida por nombrar instancias distintas. Si no puede sostenerse, se deberá definir clúster/unidad de asignación, mapa de exposición e inferencia compatible con interferencia antes de confirmar el diseño.

El número de oportunidades estandarizadas por UE queda **OPEN**. Cuando se fije, deberá ser constante entre brazos, establecido ex ante y administrado por un harness externo común; no podrá depender de recepción, admisión, procesamiento, selección, ejecución ni variables post-Z. La ausencia de envío/recepción/admisión seguirá siendo un estado observable y no se codificará automáticamente como ausencia de necesidad o Value=0.

La decisión no fija aún la identidad concreta/versionado final de B1 o del servicio, el número de oportunidades, la ventana/calendario, el payload, las reglas del protocolo, la cardinalidad request↔trajectory, los outcomes técnicos, la consecuencia B1, la perspectiva/autoridad de valoración ni los estimandos. No altera la separación entre el ciclo de petición y el reloj t−1/t0…t9; tampoco convierte solicitud, respuesta o procesamiento en selección, ejecución, Outcome o Value.

**Alcance:** decisión arquitectónica para continuar la especificación; no selecciona beneficiarios empíricos ni valida preferencias reales. No modifica DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación entre main y PR #116.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 — una oportunidad estandarizada por UE (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta **N_opportunities = 1 por unidad experimental (UE)** como configuración primaria candidata del probe estandarizado de servicio en el núcleo confirmatorio mínimo de C10-S. La oportunidad se define ex ante antes de Z y se presenta después del snapshot de accesibilidad t3/t4 mediante el mismo harness externo y bajo las mismas reglas en ambos brazos. El harness registra Request_attempt aunque no exista recepción por el servicio.

La identidad y el contenido de la oportunidad deberán ser comunes, trazables y versionados entre brazos. No recepción, rechazo, error o estado pendiente permanecen como estados observables; no se recodifican automáticamente como ausencia de necesidad, fallo transformacional, Outcome negativo ni Value=0. La población ITT no se condiciona a intento, recepción, admisión, procesamiento o respuesta post-Z.

Las oportunidades repetidas o cargas de mayor intensidad quedan reservadas a escenarios secundarios/adversariales; si se estudian, sus observaciones se anidan en la UE y no incrementan el número de unidades experimentales independientes. Esta configuración de una oportunidad no demuestra capacidad bajo carga sostenida ni demanda natural, preferencia revelada o Value del beneficiario.

Se mantienen abiertos: ventana/calendario exacto; definición final del payload y protocolo; identidad/versionado de B1 y servicio; cardinalidad request_id↔trajectory_id; tratamiento técnico de timeout, errores y pendientes; outcome técnico de respuesta; consecuencia independiente de B1 y horizonte; perspectiva/autoridad de valoración; población/soporte e integración exacta con ITT y mediación. No se equiparan eventos de petición con t5/t6/t7, ejecución transformacional, Outcome o Value, ni se amplía el reloj t−1/t0…t9.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación main/PR #116.

## DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 — contrato semántico de enlace (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como arquitectura candidata que la relación entre `request_id` y `trajectory_id` sea explícita, tipada y versionada, sin imponer una cardinalidad funcional 1:1. Se distinguen tres tipos no intercambiables:

1. `TEMPORAL_ASSOCIATION`: coexistencia temporal u orden compatible entre petición y trayectoria; no demuestra trazabilidad ni contribución causal.
2. `TRACEABILITY_LINK`: referencia técnica/documental verificable entre registros; no demuestra que la petición haya causado o modificado la trayectoria.
3. `CAUSAL_CONTRIBUTION`: relación causal definida por el DGP generador; debe distinguirse la verdad conocida por el generador de la evidencia observable y disponible para el analizador.

El modelo debe poder representar petición sin trayectoria atribuible, trayectoria sin petición atribuible, una petición que contribuya a varias trayectorias y, en escenarios con múltiples peticiones, varias peticiones que contribuyan a una trayectoria. La configuración primaria mantiene una oportunidad estandarizada por UE; por tanto, no genera múltiples request_id estandarizados dentro de esa UE, pero no impone que solo pueda existir una trayectoria ni que toda trayectoria tenga origen en esa petición. Las relaciones de escenarios secundarios con peticiones repetidas quedan anidadas en UE y no crean unidades experimentales independientes.

La existencia de cualquier enlace temporal o de trazabilidad no puede promoverse automáticamente a contribución causal. Las contribuciones causales se establecen por la verdad del DGP y se contrastan mediante los mecanismos/contrafactuales pertinentes; no se adjudican por proximidad temporal, coincidencia de IDs, respuesta del servicio o éxito técnico. Los registros observados no deben revelar al analizador la etiqueta de verdad del DGP salvo que ese conocimiento forme parte explícita del diseño de medición.

El enlace no define elegibilidad, inclusión poblacional, ITT, Outcome ni Value, y no puede usarse para excluir UE por eventos post-Z. No equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9; tampoco amplía el reloj t−1/t0…t9 ni la profundidad H. Los eventos de petición y sus enlaces se mantienen en subledger con timestamps, identidad/versionado y procedencia.

**OPEN:** reglas de generación de contribuciones, mecanismo de adjudicación, unidad temporal de atribución, tratamiento de contribuciones concurrentes y colaterales, evidencia observable para el analizador, cardinalidad de enlaces por tipo en cada DGP, y relación exacta con los estimandos ITT/mediación. No se congela schema físico ni protocolo técnico.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. D2 continúa como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren; main no se modifica.

## DEC-C10S-B1-CAUSAL-ADJUDICATION-001 — contrato de contribución causal petición–trayectoria (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como contrato causal candidato que una relación \`CAUSAL_CONTRIBUTION\` entre una petición y una trayectoria requiere un contraste contrafactual definido por el DGP: la presencia/intervención en una etapa concreta del ciclo de petición modifica una propiedad preespecificada de la trayectoria respecto del escenario contrafactual correspondiente, manteniendo explícitas las demás condiciones relevantes. La precedencia temporal, recepción, admisión, procesamiento, respuesta técnica, coincidencia de identificadores o éxito técnico no bastan por sí solos para adjudicar contribución causal.

Se distinguen, como clases potencialmente concurrentes y no necesariamente excluyentes:
- \`NECESSARY_CONTRIBUTION\`: sin la intervención/etapa considerada, la trayectoria definida no existiría bajo el contraste contrafactual especificado.
- \`ENABLING_CONTRIBUTION\`: la intervención hace factible la trayectoria o elimina una barrera relevante, sin implicar que sea causa única o suficiente.
- \`MODIFYING_CONTRIBUTION\`: la trayectoria también existiría, pero cambiaría una propiedad relevante bajo el contrafactual sin esa intervención.

Una contribución puede ser parcial, concurrente o colateral. Estas clases no implican signo positivo de Outcome ni creación de Value. La propiedad afectada debe identificarse en el DGP; no se presume que cualquier cambio de secuencia, factibilidad o atributo sea sustantivo sin regla de relevancia preespecificada.

La adjudicación debe referirse a una etapa concreta del ciclo —\`Request_opportunity\`, \`Request_attempt\`, \`Request_received\`, \`Request_admitted/rejected\`, \`Request_processing\` o \`Request_response\`— sin colapsar sus mecanismos. La oportunidad estandarizada común es una asignación/probe del harness; no se considera automáticamente una intervención realizada por el servicio ni una contribución causal. Cuando no se produce una etapa posterior, el DGP debe representar el mecanismo de no transición sin imputar una contribución de esa etapa.

Se mantiene segregación entre:
1. **Verdad del generador (\`truth_dgp\`)**: intervención/etapa, propiedad de trayectoria, contraste contrafactual, clase de contribución y procedencia de la etiqueta verdadera.
2. **Evidencia observada (\`observed_evidence\`)**: registros y mediciones permitidos al analizador, sin revelar etiquetas o potenciales contrafactuales reservados al generador.
3. **Adjudicación/evaluación**: comparación de inferencia del analizador con verdad segregada, reportando falsos positivos, falsos negativos y errores de clasificación; no convertir trazabilidad en prueba causal.

El registro conceptual de contribución deberá poder identificar etapa de petición, propiedad de trayectoria, contraste contrafactual, clase(s) de contribución, verdad DGP y evidencia observable, además de identidad/versionado/procedencia. Esto no congela un schema físico.

Esta adjudicación es mecanística y no modifica elegibilidad, población, unidad experimental, asignación ni estimando ITT; no se condiciona la inclusión a eventos post-Z. Tampoco define por sí sola Outcome o Value, ni equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9. No amplía el reloj t−1/t0…t9 ni H. D2 sigue como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren.

**OPEN:** especificación de los contrastes concretos de D2; propiedades de trayectoria causalmente relevantes; control de causas concurrentes/colaterales e interacciones; definición de intervención por etapa; positividad/soporte y versiones de tratamiento; evidencia observable y medición; reglas de atribución para contribuciones múltiples; sensibilidad a contrafactuales alternativos; relación con estimandos total, directo e indirecto y mediación.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen \`scientific_execution=false\` y \`execution_authorized=false\`; \`main\` no se modifica.

## DEC-C10S-D2-ESTIMAND-SEPARATION-001 — separación de estimandos y contrastes mecanísticos (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta organizar D2 en cinco bloques no intercambiables: **C1** efecto total de asignación/ITT de las políticas D2; **C2** primeras etapas separadas sobre `C_dep*`, `A_f*`, `D_f*` y `ΔT_acc*`; **C3** efecto focal de accesibilidad `θ_A(q)`/`θ_Af(q_X*)`, sujeto a mapping B→g, régimen común, soporte y separación/identificación de vías colaterales; **C4** mediación interventional vía `ΔT_acc*`, con Reach/trayectoria como mediadores secuenciales o bloque conjunto solo si se define explícitamente; **C5** contribución mecanística petición–trayectoria, contrastada contra truth segregada del DGP y no equiparada a Outcome/Value.

No se define residual/directo por resta automática entre estimandos incompatibles. El ITT incluye todas las vías activadas por la política y conserva interpretación de efecto de paquete si existen vías colaterales no separadas. `C_dep*`, `A_f*`, `D_f*` y `ΔT_acc*` permanecen diferenciados; el mediador no se reduce a `A_f*` sin justificación. No condicionar ITT a eventos post-Z. No mapear ciclo de petición a t5/t6/t7 ni a Outcome t8/Value t9; reloj t−1/t0…t9 y H inalterados. P179 conserva Value vectorial y trade-offs; P182/P183 siguen transversales y no se reescriben ni cierran.

**OPEN:** población/UE/interferencia; horizonte y Outcome/Value; versiones y cumplimiento; mapping B→g y q; vías colaterales/confusión/interacciones; medición A/Reach/trayectoria/O/V; identificación, precisión y reglas de abstención; contrastes concretos de etapas y propiedades de trayectoria. La decisión organiza el trabajo; no identifica efectos ni cierra jerarquía confirmatoria.

No modifica DEC-C10-066/067, C10-D1, Core, main, RMA, Matrix ni claims. No autoriza Design Freeze, implementación, fixtures, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`. Registro autónomo: `DEC-C10S-D2-ESTIMAND-SEPARATION-001.md`.


## DEC-C10S-C1-POPULATION-PRECEDENCE-001 — Precedencia poblacional C1 (2026-11-11)

**Estado:** ACCEPTED AS DESIGN-ARCHITECTURE DECISION / NOT DESIGN-FROZEN.

Se acepta `P*_{τ2}` como población objetivo primaria candidata del ITT C1-D2 y `P*_F` como subpoblación secundaria de apertura funcional exclusiva. La alternativa funcional basal no excluye de P*τ2; excluye de P*F cuando su existencia está respaldada. No se reabre la selección D2/D1 ni se altera DEC-C10-066/067.

La decisión no cierra composición de `E_i`, predicados/evidencia/indeterminación, clasificación observada frente a truth, soporte `q_X*`, unidad/interferencia, aleatorización, horizonte ni resultados. `Need_preZ` y `E_req_preZ` son distintos de `E_i`. No se excluye por eventos post-Z. Registro completo: `DEC-C10S-C1-POPULATION-PRECEDENCE-001.md`.


## PB — reconciliación integral D2/B1/C2 (2026-11-11)

**Registro rector:** maestro C10-S §267. **Estado:** PB_RECONCILED_DOCUMENTALLY / D2_C2_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN.

No se crean nuevas decisiones aceptadas ni se reabren las existentes. Se consolidan por reutilización DEC-C10-066/067, DEC-C10-068/069, DEC-C10-095 y las decisiones B1 de modalidad de petición, unidad, cardinalidad de oportunidad, enlace petición–trayectoria y adjudicación causal.

**Dictamen:** frontera P0/P1/P2 reconciliada conceptualmente; provisión D2 se limita a P1 y no modifica P0, F*, oráculo, autorización normativa basal ni rutas A1/A2. C_dep*, A_f*, D_f*, ΔT_acc*, E_T/ΔE_T y Reach/Π se mantienen separados. C2 cuantitativa no establecida; s=0.80 no validado; no inventario B-M01…15, instalación, IAM/snapshots, pruebas de aislamiento o no-afectación. D_f_obs no sustituye D_f*; Wald/LATE bloqueado.

**Única decisión nueva requerida:** armonización DEC-C10-069 con aislamiento por UE: mantener contrato/plantilla CMP común, tratar C10S-SVC-REQUEST-PROCESSOR-001 como instancia ejemplar y asignar instance_id único/versionado por UE (component_id local, clave compuesta). Recomendación favorable; pendiente de aceptación expresa. No se modifica DEC-C10-069 hasta entonces.

Siguiente paquete: PC — C3 atribución de accesibilidad y C4 mediación. Sin Design Freeze, implementación ni ejecución.


## PC — reconciliación integral de C3/C4 (2026-11-11)

**Registro rector:** maestro C10-S §268. **Estado:** PC_RECONCILED_DOCUMENTALLY / C3_C4_NOT_IDENTIFIED_IN_CURRENT_D2_MATERIAL / NOT_DESIGN_FROZEN.

No se crea una nueva decisión aceptada ni se reabre DEC-C10-066/067 o DEC-C10S-D2-ESTIMAND-SEPARATION-001. Se conserva la jerarquía C1 ITT_Z^D2/efecto de política, C3 θ_A(q), C3 focal θ_Af(q_X*), LATE_f^D2 y C4 mediación interventional.

Dictamen: D2 no equivale a políticas g1/g0 sobre ΔT_acc*. El mapping B_D2→g^Af, q_X*, soporte, vías colaterales, unidad/interferencia y medición no están demostrados. C4 requiere intervención mediadora explícita y estrategia longitudinal ante confusores mediador–resultado inducidos por Z; no ajuste convencional post-Z. El mediador es ΔT_acc* completo; Reach/Π_H son secuenciales o bloque explícito. No se obtiene residual por resta automática.

Value permanece vectorial y no instanciado: no hay V_j, beneficiario, perspectiva ni regla de valoración completos; O-CONF sigue candidato no operacionalizado. C3/C4 sobre Value no identificados/no evaluables en el material actual. P177/P178/P179/P182/P183 y DAG/CAUS existentes se reutilizan; C-MED PARCIAL/OPEN, sin nuevos IDs duplicados.

Siguiente paquete: **PD — DGP, mecanismos C5 y evaluación adversarial**. Sin Design Freeze, implementación ni ejecución.


## PE — registro de decisiones reutilizadas (2026-11-11)

PE no crea una nueva decisión científica ni reabre decisiones aceptadas. Reutiliza, dentro de su alcance, DEC-C10-061/062/065/068/069/070/071/074–088, DEC-C10-095 y las decisiones B1 de modalidad de solicitud, oportunidad estandarizada, enlace request–trajectory y adjudicación causal. Las reglas UDG/JCS/PAR son locales a sus contratos; no constituyen aceptación global del schema físico C10-S.

La arquitectura de seis responsabilidades, los bundles de rol, el pipeline V0–V8 y los gates G-SCI/G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO/G-AUTH son una síntesis técnica propuesta en PE, no decisiones aprobadas ni autorizaciones. Los formatos físicos, motor, APIs, seguridad/custodia, serialización general, esquema de eventos y salida final del Analyzer permanecen OPEN y requieren revisión/decisión antes de implementarse. `scientific_execution=false`; `execution_authorized=false`.


## DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 — 2026-11-11

| Campo | Registro |
|---|---|
| Decisión | Armonizar la identidad del servicio B1 por UE con DEC-C10-069 |
| Estado | **ACEPTADA** por aprobación expresa del responsable científico |
| Contrato | `C10S-SVC-REQUEST-PROCESSOR`, versión común `1.0.0` |
| Plantilla | Definición CMP/PAR/RUL común y versionada por contrato |
| Instancia | `instance_id` único por UE; `instance_version` monotónica e independiente |
| Componente | `component_id` local; clave compuesta `(instance_id, component_id)` |
| Referencia | `C10S-SVC-REQUEST-PROCESSOR-001` permanece como instancia ejemplar DEC-C10-069 |
| Justificación | Evitar colapsar instancias aisladas por UE sin duplicar el contrato funcional |
| Dependencias abiertas | Roster e IDs concretos, IAM/ACL, evidencia de aislamiento, MET/schema físico |
| Alcance | C10-S / PB / B1; no altera A, Core, RMA, Matrix, STATUS ni claims |
| Autorización | No autoriza implementación, fixtures, simulación, estimación ni ejecución |

Fuente normativa: `00_GOVERNANCE/SIP/DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001.md`. DEC-C10-069 se conserva dentro de su alcance original; la presente decisión añade la regla de instanciación por UE.


## PB-MAT — reconciliación documental sin nueva decisión científica (2026-11-11)

Se registra `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md` como reconciliación del contrato material, no como nueva decisión científica. Reutiliza DEC-C10-066/067, DEC-C10-068/069, DEC-C10-065/076, DEC-C10-079…083, DEC-C10S-B1-UNIT-001 y DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001. No reabre ni amplía su alcance.

**Dictamen:** contrato/plantilla funcional común e instancia lógica única por UE armonizados; adaptador/dependencia P1 separado; P0, F*/oráculo, mapping, autorización basal y A1/A2 invariantes por requisito. El requisito no demuestra invariancia. Roster/IDs, IAM/C_SRC, snapshots, grafo, artefacto/runtime, ACL/recursos, actor/recepción/ventanas/reintentos, soporte/interferencia y pruebas permanecen OPEN/BLOCKED. B-M13/M14 no pueden ser modificados por B.

No se aprueba ningún parámetro operativo nuevo, schema físico, fixture, valor DGP ni estimando. No se autoriza captura, implementación, simulación, estimación o ejecución.

## B2–B3 — aceptación de base de trabajo, sin nueva decisión científica (2026-11-11)

El usuario acepta como base de trabajo que B1 es la entidad sintética con Need_preZ basal; Outcome mide resultado técnico; Value valora la consecuencia para B1 respecto de su objetivo basal desde perspectiva/autoridad ex ante.

La reconciliación añade una precisión causal: Outcome y Value son constructos distintos, pero no se presupone que Outcome sea la causa exclusiva de Value ni que V_j=f(Outcome). La consecuencia puede depender de Outcome y de vías directas/colaterales de la política. Se mantienen P179 vectorial, fichas independientes §224 y controles P182/P183. No se eligen dimensiones, escalas, pesos, horizontes o parámetros.

Este registro documenta la aceptación de una base de trabajo; **no crea una DEC nueva ni cambia una decisión científica**. Artefacto integrador: `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md`; maestro §273. Outcome no operacionalizado; Value no instanciado; no Design Freeze ni ejecución autorizada.


## DEC-C10-099 — Selección provisional de V_cont como dimensión mínima de Value (2026-11-12)

**Estado:** ACCEPTED — PROVISIONAL DESIGN DECISION; MEASUREMENT/IDENTIFICATION GATES OPEN.

Se formaliza la aceptación expresa ya registrada en el plan §16.174: para la extensión sintética B, V_cont se selecciona provisionalmente como única dimensión mínima de Value del núcleo confirmatorio candidato; V=(V_cont), vector unitario sin índice ni pesos. La selección no aprueba todavía indicador, fórmula, ventana, resolución, baseline, horizonte, fuente, escala o agregación. La medición debe ser independiente de ΔT_acc*/Reach/trayectoria y Outcome técnico; debe superar los gates P182/P183/MEAS/MISS, validez discriminante frente a O-CONF/F* e identificación. Si no los supera, no será endpoint confirmatorio y no se sustituirá silenciosamente. DEC-C10-095 permanece vigente para A/B en su alcance, con esta decisión posterior específica para B. No Design Freeze ni autorización de implementación/ejecución. Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-099_V_CONT_PROVISIONAL_SELECTION_ACCEPTANCE.md`.



## DEC-C10-100 — Aceptación provisional de agregación temporal igualitaria de V_cont (2026-11-12)

**Estado:** ACCEPTED — PROVISIONAL OPERATIONALIZATION DECISION; MEASUREMENT/IDENTIFICATION/DISCRIMINATION GATES OPEN.

Se acepta V_cont_truth(i)=(1/K)Σ A_B1(i,k), con intervalos de igual duración en rejilla/ventana post-Z común preespecificada. UNKNOWN se conserva y produce bounds [n1/K,(n1+n?)/K]; no se imputa cero ni se elimina del denominador. El estimando es nivel post-Z, no cambio pre/post. S3 sigue siendo un canal pasivo vectorial imperfecto, no truth ni verificador directo. K, frecuencia, duración, ventana, baseline/transitorios, MDE, parámetros del canal y criterios cuantitativos siguen abiertos. La validez de medida, discriminación frente a O-CONF/F* y recuperación puntual requieren gates P182/P183/MEAS/MISS existentes. DEC-C10-099 selecciona V_cont; DEC-C10-100 acepta su regla de escala inicial. Registro autónomo: 00_GOVERNANCE/decisions/DEC-C10-100_V_CONT_EQUAL_INTERVAL_TEMPORAL_AGGREGATION_ACCEPTANCE.md. No Design Freeze ni autorización de implementación/ejecución.


## DEC-C10-101 — Aceptación del inicio de la ventana post-Z de V_cont en t0 (2026-11-12)

**Estado:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE.

Se acepta iniciar la ventana de V_cont inmediatamente después de la asignación Z en t0, incluyendo provisión e instalación. La ventana no queda condicionada a intento, recepción, instalación, verificación, C_dep, A_f, Reach, selección o ejecución. Se aplica simétricamente a los brazos comparados.

La ventana se representa [t0,T*], donde T* será un horizonte post-Z común, fijo y preespecificado. La decisión no fija duración, unidad temporal, K, resolución, duración mínima de interrupción ni regla para transitorios/fronteras. No se identifica T* automáticamente con t9, pues t0…t9 es un reloj de etapas causales y no una duración física; H=3 tampoco es horizonte temporal.

Se mantiene DEC-C10-100: K intervalos de igual duración y agregación no ponderada, con UNKNOWN propagado a bounds. S3 continúa como canal runtime pasivo, vectorial e imperfecto; no añade peticiones ni muta el sistema. La separación truth/observed/evaluation y el firewall PE permanecen obligatorios.

Registro autónomo: `00_GOVERNANCE/decisions/DEC-C10-101_V_CONT_POST_Z_WINDOW_START_T0_ACCEPTANCE.md`. Plan integrado §16.190; reconciliación B1/Need_preZ temporal §9; auditoría temporal/S4R §8. No Design Freeze ni autorización de implementación/ejecución.


## DEC-C10-102 — Aceptación de continuidad estricta por intervalo para V_cont (2026-11-12)

**Estado:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE.

El usuario acepta que la truth funcional B1 se evalúe estrictamente dentro de cada intervalo, sin periodo de gracia ni tolerancia implícita para interrupciones confirmadas:
- truth=1 solo si ENABLED/PROFILE se cumple durante todo el intervalo;
- truth=0 si ocurre al menos un incumplimiento funcional confirmado en cualquier instante;
- truth=? solo si la truth funcional no queda determinada por el Generator.

La ausencia, pérdida, lag o cobertura insuficiente de S3 es incertidumbre del canal de observación, no UNKNOWN ni cumplimiento/incumplimiento de truth. No se promedian señales ni se diluyen fallos. Eventos exactamente en frontera requieren asignación determinista y versionada a un único intervalo. Si S3 no puede detectar el mínimo evento relevante del DGP, Analyzer debe abstenerse o producir bounds.

La ventana empieza en t0 conforme DEC-C10-101. Se recomienda un reloj explícito de tiempo transcurrido, unidad normalizada declarada, eventos fechados y rejilla regular. t0…t9 es orden causal y no duración física; H=3 es profundidad transformacional. T* debe cubrir provisión/instalación y el seguimiento hasta el último evento causal que pueda modificar el cumplimiento B1 dentro del estimando. K=(T*−t0)/Δ con Δ constante y divisibilidad exacta; no se admiten intervalos residuales desiguales.

Unidad, eventos relevantes, duración mínima representable, T*, Δ, K, regla de cierre y calibración S3 siguen OPEN. Esta decisión no autoriza implementación, materialización, generación, simulación, estimación, calibración ni Design Freeze.

Registro autónomo: 00_GOVERNANCE/decisions/DEC-C10-102_V_CONT_STRICT_INTERVAL_CONTINUITY_ACCEPTANCE.md. Plan integrado §16.192; reconciliación B1/Need_preZ temporal §11; auditoría temporal/S4R §9. scientific_execution=false; execution_authorized=false.
