# DEC-C10S-C1-POPULATION-PRECEDENCE-001 — Precedencia poblacional para C1 ITT D2

**Fecha:** 2026-11-11  
**Estado:** ACCEPTED AS DESIGN-ARCHITECTURE DECISION / NOT DESIGN-FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Autoridad:** aceptación explícita del usuario en la sesión de continuidad C10-S.  
**Alcance:** precedencia entre las poblaciones candidatas ya definidas en POP-CMP-001; no aprueba todavía la composición operativa de elegibilidad ni identifica el ITT.

## 1. Decisión

Para el carril **C1 — ITT de asignación D2** se adopta la siguiente precedencia de diseño:

1. **P*_{τ2}** se mantiene como población objetivo primaria candidata: unidades definidas pre-Z que satisfacen las condiciones constitutivas basales aplicables, presentan `C_dep,0=0` y tienen `A_f,0*=0` respaldada para la identidad focal `τ2`, con clasificación basal suficiente.
2. **P*_F** se mantiene como subpoblación secundaria de apertura funcional exclusiva: `P*_F={i∈P*_{τ2}:F_alt,i0=0}`, donde la ausencia de ruta funcional alternativa debe estar respaldada con universo y cobertura suficientes.

La existencia de una ruta funcional alternativa no excluye a una unidad de P*_{τ2}; sí impide incluirla en P*_F cuando la alternativa está respaldada. Un estado `F_alt,0=?` no se recodifica como ausencia.

## 2. Interpretación y límites

- Esta decisión fija la precedencia entre candidatos ya documentados; no crea una población nueva ni reabre D2 como comparador primario candidato.
- No declara que P*_{τ2} esté operacionalmente cerrada, que todos sus predicados estén medidos o que el soporte sea suficiente.
- La composición de `E_i` —condiciones constitutivas basales y reglas de clasificación— sigue OPEN y debe derivarse de contratos actuales, sin recuperar la fórmula histórica retirada con `C_other`.
- `C_dep,0=0` y `A_f,0*=0` son requisitos separados. La primera no implica la segunda.
- La truth estructural DGP y la clasificación observada del Analyzer permanecen separadas. `A_f,0^{obs}=0` no sustituye automáticamente `A_f,0*=0`; la elegibilidad observada y el error de clasificación requieren contrato y sensibilidad.
- `Need_preZ` de B1 y `E_req_preZ` de admisión de petición son distintos de `E_i`; no se usan para redefinir P*.
- Toda elegibilidad se determina y sella antes de Z. No se excluye por intento, recepción, admisión, instalación, accesibilidad post-Z, petición, selección, ejecución, Outcome o Value.
- Si hay indeterminación basal, su tratamiento debe fijarse antes de Z, informarse en el flujo de unidades y someterse a análisis de sensibilidad; no se transforma automáticamente en 0 o 1.
- La pertenencia a P*_F es secundaria y no condiciona el denominador primario C1 sobre P*_{τ2}.

## 3. Contratos que permanecen abiertos

1. Composición de `E_i`: predicados constitutivos aplicables a la instancia/unidad, disparadores, evidencia, estados 1/0/?/NA justificado y regla de adjudicación.
2. Identidad semántica y versión de `τ2`, frontera, contexto, granularidad, catálogo, mapping y snapshots comparables.
3. Protocolo independiente para `C_dep,0` y verdad `A_f,0*`; clasificación observada y error diferencial.
4. Cobertura de rutas y evidencia negativa suficiente para `F_alt,0`.
5. Distribución objetivo `q_X*`, soporte, estratos y factibilidad de ambas poblaciones.
6. Unidad de asignación e interferencia: la UE=UA requiere evidencia de aislamiento; si no, clúster/exposición/estimando compatible.
7. Mecanismo de asignación D2, probabilidades, estratos/bloques, algoritmo/semilla, provenance y desviaciones.
8. Horizonte y resultados por variante: Outcome técnico en A; dimensiones Value en B solo cuando B1 y fichas V_j estén instanciadas.

## 4. Consecuencia para C1

C1 se formulará como familia de ITT por resultado/dimensión y horizonte dentro de P*_{τ2}, cuando cada uno esté operacionalizado. P*_F podrá sustentar un análisis secundario de apertura funcional exclusiva/heterogeneidad, con estimando y soporte propios. No se mezclan poblaciones, ni se transporta automáticamente un ITT de Outcome técnico a Value, C3, C4 o LATE.

## 5. Trazabilidad

- `C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md`, §§2–3 y addenda B1.
- `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`, §§4–5 y §12.
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`.
- `C10_S_D2_AF_PREDICATE_CAUSAL_CROSSWALK_DRAFT_001.md`.
- `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md`.
- `DEC-C10-066` y `DEC-C10-067`.

**Estado final:** precedencia poblacional aceptada como decisión de arquitectura; composición de `E_i`, medición, soporte, interferencia, asignación, resultados y horizonte permanecen OPEN. No Design Freeze, implementación, simulación ni ejecución. `scientific_execution=false`; `execution_authorized=false`.
