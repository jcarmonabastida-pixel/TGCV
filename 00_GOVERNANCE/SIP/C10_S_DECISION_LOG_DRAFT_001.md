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
