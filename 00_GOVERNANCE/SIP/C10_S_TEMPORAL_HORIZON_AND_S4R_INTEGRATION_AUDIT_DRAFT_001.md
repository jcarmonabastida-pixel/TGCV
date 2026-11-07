# C10-S — Auditoría de integración temporal, horizonte H y escenarios S4-R

**ID:** C10-S-TEMP-INT-001 · **Draft 001** · 2026-11-04
**Estado:** propuesta documental no aprobada. No autoriza ejecución.

## 1. Dictamen

Se detecta una ambigüedad: el inventario finito describe H=3 como tres pasos, cada uno ocupando una unidad discreta de tiempo; el contrato DGP sitúa Reach_H en t4, tras el snapshot t3 y antes de conocimiento, selección y ejecución. Deben separarse el reloj del estudio t0–t9, la profundidad de ruta k=0…H y el tiempo/ventanas internas de factibilidad.

## 2. Reconciliación propuesta

H=3 se conserva solo como profundidad máxima candidata (máximo tres transformaciones atómicas), no como tres unidades temporales ni como intervalo t4–t7. Las rutas del fixture F1→F2 y A1→A2 tienen longitud 2; no se añade un paso ficticio para llenar H. Duración, ventanas, caducidad de permisos/recursos y precedencias son variables separadas que requieren especificación. Por ello H=3 no está confirmado como horizonte temporal científico.

## 3. Evaluación temporal

- t0: asignación Z.
- t1: política B, recepción e intento.
- t2: verificación técnica y condiciones.
- t3: snapshot estructural postintervención; A_f, T_acc, ΔT_acc y App desde S0.
- t4: cálculo estructural de Reach_H y trayectorias candidatas sobre el snapshot t3.
- t5: conocimiento/consideración.
- t6: selección/inicio.
- t7: ejecución real.
- t8: Outcome.
- t9: Value.

Reach en t4 no se construye a partir de ejecuciones observadas. Cada paso potencial se evalúa desde su estado hipotético de entrada: accesibilidad, aplicabilidad, relación de composición, autorización, recursos, ventanas y bloqueos. Si se modelan actualizaciones dinámicas, cada rama requiere snapshots hipotéticos inmutables; nunca se sobrescribe el snapshot observado t3. Sin reglas de transición explícitas, no se inventan actualizaciones.

## 4. Correspondencia de escenarios

| Inventario | S4-R | Interpretación |
|---|---|---|
| R0: alternativa funcional ausente | S4R-A | Solo con cobertura exhaustiva del universo funcional. |
| R1: alternativa basal estable | S4R-B | B no modifica la alternativa; Reach puede no cambiar al abrir τ2. |
| R2: B modifica alternativa | S4R-C | Vía colateral; no asumir exclusión IV focal. |
| R3: provisión fallida | S4R-D | Asignación/intento no implica C_dep, A_f ni D_f. |

R0 no implica automáticamente pertenencia a P*_F: F*, frontera, granularidad, horizonte y ausencia respaldada deben definirse ex ante. El crosswalk no selecciona D1/D2.

## 5. Separaciones que debe preservar el DGP

A_f* es accesibilidad focal; T_acc* es el espacio completo; App*(τ,s) es aplicabilidad desde un estado; Rel* es composición; Feas*(π) es factibilidad conjunta de recursos, autorización, ventanas y bloqueos; Reach_H* es existencia de una ruta completa admisible. Selección, inicio y ejecución son posteriores.

## 6. Cobertura y pendientes

Se añaden dos dimensiones a las ocho ya propuestas: (9) semántica de horizonte —profundidad frente a duración, unidad, origen, límites y sensibilidad—; (10) factibilidad por rama —App, recursos, ventanas, caducidades y snapshots hipotéticos por prefijo—. Sin ambas no puede declararse exhaustividad.

Pendiente: ratificar H como profundidad o definir duración científica; fijar ventanas y reglas de recursos; formalizar actualizaciones de ramas; definir F* y objetivo; validar cobertura de alternativas; elegir D1/D2; construir oráculos y revisar independientemente. AUD-005 y AUD-007 siguen abiertos; tampoco se cierran AUD-004 ni OPEN-C10-001/003/005/007.

**Dictamen:** se propone separar reloj del estudio, profundidad y tiempo de factibilidad. No hay fixtures ejecutables, generación de datos, simulación ni ejecución.