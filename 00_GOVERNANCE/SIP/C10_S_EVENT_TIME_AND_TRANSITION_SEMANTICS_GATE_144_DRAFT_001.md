# C10-S — Gate 144: semántica mínima de event_time y transiciones para V_cont

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Estado:** HISTORICAL_RECONSTRUCTION_COMPLETE / EVENT_TIME_PARTIALLY_SPECIFIED / TRANSITION_HOLD_AND_SAME_TIME_ORDER_OPEN / R144_PROPOSAL_PENDING_USER_ACCEPTANCE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Objeto

Determinar qué parte del reloj temporal puede cerrarse sin elegir unidad física, soporte, T*, Δ, K ni calibración S3; y si EventHistory puede adjudicar continuidad estricta con el contrato actual.

No se ha ejecutado código, tests, validadores, workflows, generación, simulación ni calibración.

## 2. Reconstrucción y precedencia

Se reutilizaron DEC-C10-100…104, DGP temporal §§48–55, Gates 135–143 y sus addenda. En particular: Gate 139 (EventHistory, relojes separados, adjudicación y firewall); Gate 136 (estructura de evento y vacíos temporales); Gate 137/DEC-C10-104 (frontera semiabierta y regla conservadora de UNKNOWN); Gate 140 (mapping post-Z de provisión/instalación y alcance Analyzer); y el delta Gate 143.

## 3. Hallazgo: qué está definido y qué no

### 3.1 Definido o aceptado

1. DEC-C10-101 fija t0 inmediatamente después de Z e incluye provisión e instalación.
2. DEC-C10-102 fija continuidad estricta: cualquier incumplimiento funcional confirmado en cualquier instante del intervalo hace A_B1=0 en ese intervalo.
3. DEC-C10-104 fija intervalos internos [b_{k−1},b_k), último [b_{K−1},b_K], asignación de frontera y regla de UNKNOWN.
4. §§49–50, aceptados parcialmente por Gate 142 como especificación de trabajo, exigen event_time, identidad/versión, estado funcional previo/posterior, familia causal y provenance; distinguen reloj de truth, rejilla de agregación y reloj S3.
5. Gate 139 requiere un event_time común y ordenable, separado de observation/capture_time e ingestion_time.
6. §51 ya contiene una propuesta de coordenada adimensional x=(t−t0)/W_c, con t0=0 y t_c,max=1, además de la cola ρ_follow y el modelo S3. Pero §51 quedó expresamente fuera de la aceptación R141-A; sigue siendo DRAFT/propuesta, no baseline aceptada.
7. DEC-C10-102 recomienda un reloj explícito normalizado y eventos fechados, pero deja unidad, soporte, resolución, T*, Δ y K abiertos.

### 3.2 Vacío real localizado

No se ha encontrado una regla aceptada que defina explícitamente:
- si el estado funcional permanece constante entre dos transiciones truth;
- cómo se representa un estado inicial inmediatamente después de Z antes de los eventos post-Z;
- cómo se resuelven transiciones simultáneas o varias transiciones con igual event_time;
- cómo se preserva una transición funcional instantánea/intermedia sin inventar duración;
- cómo un event_time abstracto se compara posteriormente con fronteras b_k cuando el reloj y la rejilla aún no están aprobados.

Por tanto, Gate 143 acierta al separar EventHistory de la rejilla, pero la frase «los estados persistentes se mantienen hasta una transición posterior» es todavía una regla de modelado propuesta, no una regla demostrada como aceptada. No debe codificarse silenciosamente.

## 4. Límite de lo que puede hacerse sin §51 ni parámetros

Puede especificarse documentalmente un registro lógico de eventos con identidad, versión, estado previo/posterior, familia, provenance y una clave temporal común ordenable. Eso preserva la historia y su orden sin una unidad física.

Pero el orden ordinal por sí solo **no basta** para calcular A_B1(i,k): no determina si un evento cae dentro de un intervalo, coincide con una frontera, ni cuánto tiempo persiste un estado. La adjudicación estricta requiere una relación temporal común entre eventos y fronteras de la rejilla. Por tanto:
- EventHistory puede diseñarse conceptualmente sin valores de T*, Δ o K.
- No se puede materializar la adjudicación confirmatoria por intervalos ni calcular V_cont numérico hasta que exista un reloj común comparable con la rejilla.
- No se puede sustituir el reloj por número de slot, t0…t9, orden de generación o cadencia S3.
- No se puede interpretar ausencia de eventos como continuidad si no se ha aprobado la semántica de persistencia y completitud del historial.

## 5. Propuesta R144-A — semántica lógica del proceso de transición

Se propone aceptar, como regla de trabajo para el DGP sintético, lo siguiente:

1. **Estado inicial:** el Generator declara el estado funcional B1 inmediatamente después de Z en el ancla t0, antes de aplicar los eventos post-Z ordenados en ese mismo ancla. Se conserva como estado inicial de la ventana.
2. **Persistencia:** entre dos transiciones truth, el último estado funcional adjudicado permanece vigente (proceso de estado por tramos, sin interpolación). Solo una transición truth explícita puede cambiarlo.
3. **Evento:** cada transición registra estado previo y posterior, familia causal, identidad/versión, event_time y provenance reservada. Los eventos de provisión/instalación solo afectan A_B1 mediante el cambio funcional efectivo.
4. **Igual event_time:** cambios genuinamente simultáneos se representan como una única transición atómica vectorial. Si existe una secuencia causal con estados intermedios funcionalmente distintos, cada paso conserva un suborden explícito y determinista; los estados intermedios son adjudicables incluso si no se les asigna duración positiva. No se infiere orden a partir de IDs ni del orden accidental de serialización.
5. **Fronteras:** una vez que existan fronteras comparables, se aplica DEC-C10-104 sin modificación. Eventos en frontera interna pertenecen al intervalo que comienza allí; T* pertenece al último.
6. **Completitud:** una historia completa y determinada permite adjudicar 1/0. Un evento omitido, una colisión no resuelta, un timestamp inválido o un hueco de especificación/implementación es fallo de contrato/harness, no funcional ?. DEC-C10-104 permanece prevalente.

Esta propuesta no fija una unidad física, resolución, W_c numérico, t_c,max, T*, ρ_follow, Δ, K, soporte de episodios, frecuencia S3 ni δ_det. Tampoco aprueba una causa funcional intrínseca para UNKNOWN.

## 6. Propuesta R144-B — mantener §51 fuera de aceptación por ahora

Mantener abierta la aceptación del §51 completo. La coordenada normalizada x=(t−t0)/W_c es una representación candidata ya documentada, pero no debe convertirse en requisito implementable hasta que se aprueben su soporte común y la relación entre el reloj de eventos y la rejilla. El contrato de captura/detección S3, la curva P_det_joint, fases, lag, pérdida, error y calibración siguen abiertos y no deben confundirse con el reloj de truth.

La aceptación de R144-A, si se concede, cerraría solo la semántica lógica de transiciones. No aprobaría §51, EventHistory físico, rejilla, adjudicador, TruthBundle temporal ni implementación.

## 7. Dictamen y siguiente paso

La dependencia temporal no se resuelve eligiendo una escala numérica prematuramente. El vacío mínimo es la semántica de persistencia y simultaneidad de transiciones. Se recomienda que el usuario acepte R144-A y mantenga R144-B como condición de no ampliación: primero cerrar cómo cambia la truth; después resolver cómo se ubica esa truth en la ventana y rejilla.

La propuesta requiere aceptación expresa. Hasta entonces, Gate 143 sigue siendo una especificación preparatoria, no autorizada para código. No se modifica DGP original, DEC, Decision Log, schemas, código, tests, workflows, RMA, Evidence→Claim Matrix, STATUS, main ni PR base.

scientific_execution=false  
execution_authorized=false
