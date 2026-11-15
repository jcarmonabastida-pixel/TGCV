# C10-S — Gate 120: expediente de resolución de decisiones P0

**ID:** C10-S-GATE-120-P0-DECISION-RESOLUTION-DOCKET-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** ALL_FIVE_RECOMMENDATIONS_EXPLICITLY_ACCEPTED / DEC-C10-103_RECORDED / HISTORICAL_ACCEPTANCES_RECONCILED / CONDITIONAL_MATERIAL_AND_IDENTIFICATION_GATES_OPEN / NOT_DESIGN_FROZEN / NO_IMPLEMENTATION / NO_EXECUTION.

---

## 1. Propósito y límite

Gate 120 convierte las cinco recomendaciones de Gate 119 en un expediente de resolución explícita. El responsable científico aprobó expresamente las cinco recomendaciones en respuesta afirmativa del 2026-11-15. La resolución queda registrada en DEC-C10-103 y propagada al Decision Log, maestro y plan. La aprobación no demuestra las condiciones materiales/estadísticas ni autoriza ejecución.

## 2. Reconciliación histórica que no debe reabrirse

| Fuente | Estado vigente | Consecuencia para Gate 120 |
|---|---|---|
| DEC-C10-066 | ACEPTADA, alcance limitado | D2 es escenario primario candidato; D1 secundario. No volver a votar D1/D2. |
| DEC-C10-067 | ACEPTADA, alcance conceptual/documental | Políticas materiales D2 y secuencia Z→programación→intento→recepción→instalación→C_dep*→A_f* ya tienen definición conceptual. No implica éxito, accesibilidad, ni aislamiento. |
| DEC-C10-095 | ACEPTADA — arquitectura A/B | A sigue referencia sin cambios; B es extensión sintética separada/versionada para permitir estudiar Value. No volver a decidir si A y B se fusionan. |
| DEC-C10-096 | ACEPTADA — censo de validación B1/Need_preZ | Define el censo de UE del roster B1/Need aplicable y la evaluación E1/E2. **No define por sí sola la población causal P*τ2, ni decide roster causal A/B conjunto/separado, ni convierte Need en filtro causal.** |
| DEC-C10-099…102 | ACEPTADAS en alcance provisional/operacional | V_cont es dimensión mínima provisional de B; agregación temporal igualitaria; ventana desde t0; continuidad estricta por intervalo. K, T*, Δ, S3/calibración y validez siguen abiertos. |
| C10-S §§16.185, 16.199–16.200 y 280–289 | Contratos de integración vigentes | D2, P*τ2 candidata, P*_F secundaria, potenciales separados, ΔT_acc* completo, g_A, q_X* y vías colaterales se mantienen; mapping D2→g_A, soporte y funciones siguen abiertos. |
| Gate 118–119 | Comparaciones/recomendaciones documentales | No son decisiones aceptadas ni Design Freeze. |

## 3. Cinco resoluciones propuestas

### R120-1 — Población causal y relación A/B

**Ya aceptado:** A y B son variantes DGP separadas; B es la variante donde se estipula Value.  
**Pendiente real:** arquitectura de roster causal y posibilidad de matching/spine basal entre variantes.

**Recomendación:** rosters separados por defecto. Solo establecer crosswalk/matching A↔B si se acredita identidad basal equivalente, elegibilidad pre-Z y comparabilidad de variables/contratos. No combinar los rosters ni tratar A como brazo control de B. El roster de validación Need_preZ de DEC-C10-096 es un censo de tarea de adjudicación, no sustituye P*τ2.

**Resolución solicitada:** aceptar esta recomendación / rechazarla y especificar alternativa / mantener OPEN.

### R120-2 — Unidad de asignación e interferencia

**Ya aceptado:** D2 como paquete/política candidata y su secuencia material. No está aceptado que la asignación sea UE=UA ni que exista aislamiento.

**Recomendación:** asignación individual por UE solo como arquitectura confirmatoria condicional, después de demostrar aislamiento material. Deben inventariarse pools, dependencias mutables, agentes, canales, estado compartido, side effects y carryover. Si no se demuestra aislamiento, no se mantiene por defecto el análisis individual: se debe especificar asignación por cluster o mapa de exposición con probabilidades/soporte; si la interferencia no se mapea, abstención/bounds.

**Resolución solicitada:** aceptar A individual condicionada a evidencia / elegir B cluster / elegir C exposición mapeada / mantener OPEN hasta inventario material.

### R120-3 — Unidad y ponderación del estimando

**Recomendación:** bajo asignación individual aislada, target primario promedio por UE de la población causal B pre-Z elegible. Rutas, eventos, intervalos V_cont e instancias no sustituyen el número de UE independientes. Si se elige cluster, reabrir expresamente la ponderación: promedio por UE y promedio por cluster son distintos cuando los tamaños difieren.

**Resolución solicitada:** aceptar promedio por UE condicionado a R120-2A / elegir promedio por cluster / mantener OPEN.

### R120-4 — Alcance confirmatorio de estimandos

**Base ya fijada:** D2 ITT es efecto total de asignación del paquete; g_A1/g_A0 intervienen sobre distribuciones factibles del ΔT_acc* completo bajo q_X* y r_common; no son intercambiables. C4 es mediación interventional longitudinal, no una resta del ITT. V_cont es solo la dimensión mínima provisional de Value en B, su medición/identificación permanece abierta.

**Recomendación:**
1. **Focal de atribución:** \\(\\theta_A(q_X^*,r_{common};V_{cont})\\), intervención sobre el vector completo \\(\\Delta T_{acc}^*\\), solo si g_A1/g_A0 son intervenciones bien definidas, factibles y con soporte.
2. **ITT-D2:** contraste de política separado, estimado como efecto total del paquete sobre V_cont y los demás outcomes preespecificados; no se interpreta como efecto puro de accesibilidad.
3. **C4:** secundario/exploratorio condicionado al cierre de historia longitudinal, confusión post-Z, soporte secuencial y medición.
4. **Efecto directo/no mediado:** fuera del núcleo confirmatorio hasta definición de estimando propio y supuestos. Prohibido calcularlo como ITT menos efecto mediado o menos θ_A.

La etiqueta “focal” no equivale a “identificado”: si falla soporte, medición, interferencia o identificación, el resultado es bounds/NOT_IDENTIFIED/abstención conforme al contrato.

**Resolución solicitada:** aceptar esta jerarquía / proponer otra jerarquía explícita / mantener OPEN.

### R120-5 — Identidad y continuidad UE

**Recomendación:** identidad UE inmutable dentro del roster/package versionado. Replay conserva identidad; una nueva réplica/realización recibe identidad propia según contrato. Matching entre A/B solo mediante crosswalk explícito y versionado, nunca por reutilización implícita de clave. No imponer continuidad global entre variantes o versiones sin necesidad científica demostrada.

El campo `ue_id` propuesto en contratos Draft no queda aprobado/materializado por este gate. UE→U_G root permanece UNKNOWN y no debe forzarse si el estimando/contrato no lo necesita.

**Resolución solicitada:** aceptar identidad local al roster con crosswalk opcional / exigir continuidad compartida A/B con regla explícita / mantener OPEN.

## 4. Orden lógico de resolución

R120-1 define la población y el roster de referencia. R120-2 determina la unidad de asignación y el régimen de interferencia. R120-3 depende de R120-2. R120-4 requiere población, unidad, régimen de exposición y soporte. R120-5 debe cerrarse antes de materializar roster/bindings, pero no sustituye la definición causal.

Una aprobación parcial es válida. Si una decisión depende de otra no resuelta, permanece CONDITIONAL/OPEN. No se fuerza un cierre simultáneo de los cinco puntos.

## 5. Condiciones posteriores a la aprobación

Una vez recibidas respuestas explícitas:
1. crear o actualizar solo las DEC necesarias, con alcance exacto y alternativas;
2. reconciliar el Decision Log, el maestro C10-S, el plan y contratos afectados en el mismo ciclo;
3. preservar decisiones y artefactos históricos; no modificar main ni cambiar la base de PR #116;
4. no materializar roster, schema, fixtures, clusters, mapas de exposición o parámetros salvo autorización separada y contrato aceptado;
5. evaluar identificación, positividad/soporte, medición, vías colaterales, missingness, sensibilidad y potencia;
6. solo después evaluar Design Freeze y contrato de implementación.

## 6. Estado y autorización

`OWNER_APPROVAL_PENDING`; ninguna de R120-1…R120-5 se registra como ACCEPTED por este expediente. Gate 120 es un docket de decisión, no una DEC.

No se modifica C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni `main`. No se modifica código ni se ejecutan validadores, tests, workflows, simulaciones, estimaciones, calibraciones o experimentos. PR #116 permanece Draft.

`scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** incorporar las respuestas explícitas del responsable científico, resolver dependencias y propagar únicamente las decisiones aceptadas a sus contratos existentes.
