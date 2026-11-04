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
