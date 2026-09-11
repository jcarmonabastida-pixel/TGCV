# TGCV-EXT-TCP-001 — Testable Concept Paper (TCP) v0.4

**Programa:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos  
**Clase:** Externo científico/técnico  
**Estado:** CURRENT / CONTROLLED  
**RMA ID:** TGCV-EXT-TCP-001  
**Fecha:** 2026-09-11  
**Predecesor:** v0.3

## 1. Propósito

El TCP define la arquitectura mínima y el programa de prueba de TGCV. Mantiene una referencia científica común para los demás activos externos sin convertir hipótesis, resultados acotados u originalidad pendiente en afirmaciones demostradas.

El objeto central es la **estructura y evolución de las transformaciones accesibles de un sistema** y la posibilidad de representar y comparar cambios en esa estructura.

## 2. Arquitectura mínima actual

La ontología mínima actual es:

`Core_ontological = S`

La estructura de transformaciones accesibles es una representación analítica dependiente de las condiciones relevantes:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

con `S` como sistema/estado relevante, `C` como contexto, `L` como restricciones, recursos y condiciones de admisibilidad, `Uτ` como universo candidato, `τ` como transformación canónica y `Pτ` como predicado de accesibilidad.

TR-131 estableció que `T_acc` no es un primitivo ontológico independiente de `S`, aunque es analíticamente indispensable para representar explícitamente su modificación. La interacción `I` permanece fuera del Core y puede utilizarse como mecanismo explicativo cuando un diseño concreto lo justifique.

## 3. Fenómeno central y dinámica

El fenómeno estudiado es el cambio de la estructura de transformaciones accesibles:

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

La modificación puede manifestarse como expansión, contracción, persistencia o reconfiguración, según la semántica operacional declarada.

La cadena analítica de trabajo es:

`mecanismo → (S_t,C_t) → (S_{t+1},C_{t+1}) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Esta cadena es una arquitectura de análisis, no una afirmación causal. Cada relación requiere definición y evidencia independientes.

## 4. Consecuencia metodológica actual

La operacionalización experimental no exige como requisito universal la enumeración exhaustiva ex ante de toda la estructura `T_acc(S_t)`.

El screening y la reconstrucción deben centrarse, según el caso, en:

- una transformación concreta o conjunto candidato explícito;
- el estado/contexto relevante `(S_t,C_t)`;
- una regla de accesibilidad o admisibilidad independiente del outcome;
- condiciones de decisión temporalmente congeladas;
- una transición de estado reconstruible.

La información parcial o desconocida sobre transformaciones alternativas no constituye por sí misma criterio de rechazo. La clausura operacional de accesibilidad es dependiente del caso y debe permanecer separada de la observación del resultado.

Esta frontera metodológica es coherente con TR-131 y TR-132-MOD-1 y ha sido incorporada en ARM v0.2 y en la gobernanza industrial vigente.

## 5. Estado de la evidencia

La evidencia estructural principal continúa siendo la operacionalización congelada del ecosistema Rust. RUST-DYN-1 analizó 516.061 pares temporales adyacentes y observó 438.203 pares no persistentes del espacio accesible (~84,91%), además de casos de expansión, contracción y reconfiguración.

RUST-DYN-2, bajo una semántica de Reach potencial de profundidad 1, estableció casos en los que `ΔT_acc` y `ΔReach` se separan o co-varían. Los principales testigos fueron ND-1=159.921, ND-2=278.282 y ND-4=266.201.

La evidencia adicional gobernada incluye IUT-A-01 U2 (`U2-NULL`), IT-NOSD-010 como reconstrucción acotada y separación downstream, EXT-UPD-4.8 como evidencia de frontera de accesibilidad y la evidencia fixture Class-II AWS. Estos registros no establecen causalidad, predicción de valor, superioridad, universalidad, originalidad plena, runtime Cargo reachability ni status industrial Class-I.

## 6. Frontera de contribución

La revisión comparativa D-OPS-21 mostró antecedentes cercanos y redundancia local. D-OPS-22 identificó un posible residuo de no-redundancia en la traducción transversal sin demostrar superioridad. D-OPS-23 congeló un protocolo mínimo para preservar las distinciones entre estado, universo candidato, accesibilidad, `T_acc`, `ΔT_acc`, Reach, Trajectory, Outcome y Value.

La contribución candidata se formula prudentemente como una **arquitectura analítica de traducción transversal** cuya validez, no-redundancia, utilidad y eventual superioridad permanecen sujetas a prueba.

## 7. Programa de investigación

El programa debe responder progresivamente a:

1. **Identificabilidad:** definición de `Uτ` y `Pτ` sin circularidad ni información futura ilegítima.
2. **No-redundancia:** información no reducible a una simple recodificación de representaciones existentes.
3. **Dinámica:** identificación de `ΔT_acc` independientemente del resultado observado.
4. **Reach y Trajectory:** condiciones bajo las que cambios de accesibilidad se relacionan con alcance o trayectoria.
5. **Outcome y Value:** relación defendible sin confundir accesibilidad con resultado o valor.
6. **Traducción transversal:** preservación de las distinciones en dominios heterogéneos.
7. **Límites:** identificación explícita de dominios y condiciones en los que la operacionalización falla.

## 8. Testabilidad y falsabilidad

TGCV debe poder fallar. Son resultados admisibles que `T_acc` no sea identificable de forma no circular, que la representación resulte redundante, que `ΔT_acc` no aporte información analítica útil, que no exista relación suficiente con Reach o Trajectory, que el vínculo con Outcome o Value requiera supuestos no defendibles o que la arquitectura transversal quede absorbida por antecedentes existentes.

Los criterios no deben modificarse retrospectivamente para convertir un resultado negativo en positivo.

## 9. Prior art y originalidad

La originalidad permanece abierta y debe tratarse como cuestión comparativa. La SLR y los controles D-OPS-21/22/23 delimitan la frontera conocida, pero no equivalen a una prueba exhaustiva de ausencia de antecedentes.

## 10. Valor

El valor permanece downstream:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

El TCP no afirma que un cambio de accesibilidad produzca o prediga Value. La eventual relación con Value constituye una cuestión independiente.

## 11. Estado de operaciones metodológicas

D-OPS-24 y EXT-UPD-4.8 ya están **cerrados en sus ámbitos autorizados**. Por tanto, este TCP no presenta D-OPS-24 como un control pendiente ni autoriza su reapertura. Cualquier futura operación metodológica deberá disponer de su propio diseño, preflight y autorización.

Este TCP no autoriza ninguna ejecución experimental o industrial.

## 12. No-claims actuales

Este documento no afirma que:

- TGCV sea universal;
- `T_acc` sea un primitivo ontológico independiente de `S`;
- los cambios de accesibilidad sean causalmente eficaces;
- TGCV prediga o genere Value;
- TGCV sea superior a representaciones alternativas;
- TGCV sea plenamente original;
- RUST-DYN-2 mida ejecución runtime de Cargo;
- exista una validación transversal completa;
- exista actualmente un resultado industrial de utilidad, superioridad o valor demostrado.

## 13. Estado

**CURRENT / CONTROLLED.**

Esta versión supersede el papel del TCP como activo externo actual. `v0.2` y `v0.3` permanecen preservadas como artefactos históricos e inmutables.