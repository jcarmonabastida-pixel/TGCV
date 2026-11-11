# DEC-C10S-D2-ESTIMAND-SEPARATION-001 — separación de estimandos y contrastes mecanísticos

**Fecha:** 2026-11-11  
**Estado:** ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.  
**Ámbito:** arquitectura causal y de estimandos de C10-S, escenario D2 primario candidato.  
**Ubicación:** rama `research/c10-s-consolidation-draft`, PR #116 Draft.  
**Autoridad:** aceptación expresa del usuario en la conversación de continuidad C10-S.

## 1. Decisión aceptada

Se acepta organizar la arquitectura de estimandos y contrastes de D2 en cinco bloques separados, no intercambiables:

1. **C1 — efecto total de asignación / ITT de D2 (`ITT_Z^D2`).** Contraste entre asignación a las políticas materiales `B_g1^D2` y `B_g0^D2` sobre un resultado definido, en la población ITT y horizonte comunes. Bajo diseño válido estima el efecto de asignación a la política D2; no atribuye automáticamente el efecto a accesibilidad.
2. **C2 — primeras etapas.** Contrastes de asignación sobre `C_dep*`, `A_f*`, `D_f*` y `ΔT_acc*`, manteniendo las mediciones separadas. Una primera etapa en un eslabón no demuestra una primera etapa en los posteriores ni un efecto sobre Value.
3. **C3 — efecto focal de accesibilidad (`θ_A(q)` / `θ_Af(q_X*)`, según el alcance).** Contraste de políticas de accesibilidad bajo régimen común y soporte definido. Requiere mapping implementable entre D2 y las políticas objetivo de accesibilidad, además de ausencia, separación o identificación de vías colaterales. El estimando focal sobre `τ2` no sustituye automáticamente la pregunta general sobre `ΔT_acc*`.
4. **C4 — mediación interventional.** Análisis separado del componente indirecto que opera a través de `ΔT_acc*`; Reach y trayectoria podrán tratarse como mediadores secuenciales posteriores o como bloque mediador conjunto solo mediante definición explícita. Deben especificarse población, régimen, horizonte, escala/regla de Value, intervenciones mediadoras y confusión mediador–resultado, incluida la inducida por Z. No se presume identificación de efectos naturales ni descomposición aditiva.
5. **C5 — contribución mecanística petición–trayectoria.** Contrastes contrafactuales del DGP referidos a etapas concretas del ciclo de petición y propiedades preespecificadas de trayectoria. Se evalúan contra truth segregada del Generator y evidencia observada disponible al Analyzer. No equivalen a ITT, efecto mediado, Outcome ni Value.

## 2. Reglas de interpretación

- No definir un residual/directo como resta automática entre `ITT_Z^D2`, `LATE_f^D2`, `θ_Af(q_X*)` o `θ_A(q)`; sus poblaciones, intervenciones, escalas o supuestos pueden diferir.
- El efecto total de asignación incluye todas las vías activadas por la política D2. Si hay vías colaterales a Outcome/Value, el resultado conserva interpretación de efecto de política/paquete salvo identificación adicional.
- `C_dep*`, `A_f*`, `D_f*` y `ΔT_acc*` no se sustituyen entre sí.
- La medición de `ΔT_acc*` debe representar el cambio estructural completo; no reducir el mediador a `A_f*` sin justificación.
- La población ITT no se condiciona a intento, recepción, admisión, procesamiento, respuesta, accesibilidad post-Z, selección o ejecución.
- El ciclo de petición no se identifica con t5/t6/t7 ni con Outcome t8 o Value t9; no se amplía el reloj t−1/t0…t9 ni H.
- Una contribución mecanística a una trayectoria no implica efecto positivo de Outcome ni creación de Value.
- P179 mantiene Value vectorial y trade-offs; no se fija índice escalar ni ponderaciones. P182/P183 siguen como contratos transversales de medición, error, invariancia, datos ausentes/censura e identificación; esta decisión no los reescribe ni los cierra.
- B1 y la oportunidad estandarizada (una por UE) constituyen un probe común de servicio, no evidencia por sí sola de demanda natural, preferencia revelada o Value.

## 3. Dependencias y cuestiones OPEN

La aceptación no cierra:
- población objetivo, unidad de asignación/UE y posible interferencia;
- horizonte, resultado confirmatorio y regla/instancia de Value;
- versiones completas de políticas, actor/artefacto, recepción, cumplimiento y ventanas;
- mapping de `B_g^D2` a políticas de accesibilidad `g), soporte y régimen común `q);
- vías colaterales, confusores mediador–Outcome, interacciones y sensibilidad;
- operacionalización independiente de `ΔT_acc*`, Reach, trayectorias, Outcome y Value;
- estimandos exactos, identificación estadística, estimación, precisión/potencia y reglas de abstención;
- contrastes DGP concretos por etapa del ciclo de petición, propiedades de trayectoria relevantes y evidencia observable;
- relación entre contribuciones múltiples y mediación.

La jerarquía confirmatoria completa y la identificación causal permanecen abiertas. Esta decisión organiza el trabajo y no declara identificado ningún efecto.

## 4. Trazabilidad y límites

Debe propagarse en el Decision Log, la reconciliación causal, el plan de cierre/operacionalización y la Closure Control Matrix de esta rama. No se afirma propagación al maestro consolidado si su contenido íntegro no está recuperado y verificado.

No modifica `main`, DEC-C10-066/067, C10-D1, Core, RMA, Evidence→Claim Matrix ni claims. No autoriza Design Freeze, implementación, fixtures, validadores modificadores, simulación, estimación o ejecución científica.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.
