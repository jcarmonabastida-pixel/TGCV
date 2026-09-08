# TGCV-EXT-TCP-001 — Testable Concept Paper (TCP) v0.3

**Programa:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos  
**Clase:** Externo científico/técnico  
**Estado:** CURRENT-SITUATION DRAFT / CONTROLLED  
**RMA ID:** TGCV-EXT-TCP-001  
**Fecha:** 2026-09-08

## 1. Propósito

El TCP define la arquitectura mínima y el programa de prueba de TGCV. Su función es mantener una referencia científica común para los demás activos externos sin convertir hipótesis, resultados acotados u originalidad pendiente en afirmaciones demostradas.

El objeto central es la **estructura y evolución de las transformaciones accesibles de un sistema** y, específicamente, la posibilidad de representar y comparar cambios en ese espacio.

## 2. Arquitectura mínima

La ontología mínima actual es:

`Core_ontological = S`

El espacio de transformaciones accesibles es un constructo analítico dependiente de las condiciones relevantes:

`T_acc,t = {τ ∈ Uτ | Pτ(S_t,C_t,L)=1}`

con:

- `S`: sistema/estado relevante;
- `C`: contexto o condiciones relevantes;
- `L`: restricciones, recursos y condiciones de admisibilidad;
- `Uτ`: universo candidato de transformaciones;
- `τ`: transformación canónica;
- `Pτ`: predicado de accesibilidad.

TR-131 estableció que `T_acc` no debe tratarse como un primitivo ontológico independiente de `S`, aunque sí resulta analíticamente indispensable para representar explícitamente su modificación.

La interacción `I` no forma parte del Core. Puede utilizarse como mecanismo explicativo cuando un diseño concreto lo justifique.

## 3. Fenómeno central

El fenómeno estudiado es el cambio de pertenencia del espacio de transformaciones accesibles:

`ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`

El cambio puede manifestarse como expansión, contracción, persistencia o reconfiguración. La clasificación depende de la semántica operacional concreta.

`ΔT_acc` no equivale a cambio de estado, ejecución de una transformación, Reach, Trajectory, Outcome o Value.

## 4. Arquitectura dinámica

La cadena analítica de trabajo es:

`mecanismo → (S_t,C_t) → (S_{t+1},C_{t+1}) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Esta cadena no constituye por sí misma una afirmación causal. Cada relación requiere definición y evidencia independientes.

## 5. Evidencia empírica actual

La evidencia disponible procede de la operacionalización congelada del ecosistema Rust.

RUST-DYN-1 analizó 516.061 pares temporales adyacentes y observó 438.203 pares no persistentes del espacio accesible (~84,91%), además de casos de expansión, contracción y reconfiguración.

RUST-DYN-2, bajo una semántica de Reach potencial de profundidad 1, estableció casos en los que `ΔT_acc` y `ΔReach` se separan o co-varían. Los principales testigos fueron:

- ND-1: 159.921;
- ND-2: 278.282;
- ND-4: 266.201.

Estos resultados constituyen evidencia E1 acotada a la operacionalización Rust. No constituyen prueba de causalidad, predicción, creación de valor, universalidad, superioridad, originalidad plena ni runtime Cargo reachability.

## 6. Programa de investigación

El programa debe responder progresivamente a:

1. **Identificabilidad:** ¿puede definirse `Uτ` y `Pτ` sin circularidad ni información futura ilegítima?
2. **No-redundancia:** ¿la representación conserva información que no sea una simple recodificación de una representación existente?
3. **Dinámica:** ¿puede identificarse `ΔT_acc` independientemente de los resultados observados?
4. **Reach y Trajectory:** ¿bajo qué condiciones los cambios de accesibilidad se relacionan con diferencias de alcance o trayectoria?
5. **Outcome y Value:** ¿puede establecerse una relación defendible sin confundir accesibilidad con resultado o valor?
6. **Traducción transversal:** ¿pueden preservarse estas distinciones al trasladar constructos entre dominios heterogéneos?

## 7. Frontera de contribución

La revisión comparativa D-OPS-21 mostró que la idea de espacios de adaptación/cambio y su drift tiene antecedentes cercanos. Por tanto, TGCV no declara como novedad aislada la existencia de un espacio de transformaciones accesibles ni su modificación temporal.

D-OPS-22 identificó un posible residuo de no-redundancia en una arquitectura de traducción transversal, sin demostrar superioridad.

D-OPS-23 congeló un protocolo mínimo que preserva explícitamente las distinciones entre estado, universo candidato, accesibilidad, `T_acc`, `ΔT_acc`, Reach, Trajectory, Outcome y Value.

La contribución candidata actual es, por tanto, una **arquitectura analítica de traducción transversal** cuya validez, no-redundancia, utilidad y eventual superioridad permanecen sujetas a prueba.

## 8. Testabilidad y falsabilidad

TGCV debe poder fallar. Son resultados posibles:

- que `T_acc` no sea identificable de forma no circular;
- que la representación resulte redundante;
- que `ΔT_acc` no aporte información analítica útil;
- que no exista relación suficiente con Reach o Trajectory;
- que el vínculo con Outcome o Value requiera supuestos no defendibles;
- que el protocolo transversal sea absorbido por arquitecturas existentes;
- que la traducción entre dominios no preserve las distinciones requeridas.

Un resultado negativo no debe corregirse retrospectivamente alterando definiciones o criterios después de observarlo.

## 9. Prior art y originalidad

La originalidad de TGCV permanece abierta y debe tratarse como cuestión comparativa, no como hecho establecido. La SLR y los controles D-OPS-21/22/23 delimitan la frontera actual, pero no equivalen a una prueba exhaustiva de ausencia de antecedentes.

## 10. Valor

El valor se mantiene downstream:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

El TCP no afirma que un cambio de accesibilidad produzca valor ni que pueda predecirlo. La eventual relación con Value constituye una pregunta de investigación independiente.

## 11. Próximo control

El siguiente control metodológico es **D-OPS-24 — Controlled Translation Trace Conformance Test**. Su ejecución requiere reconstrucción histórica, diseño, preflight y autorización propios.

Este TCP no autoriza ninguna ejecución experimental.

## 12. No-claims actuales

Este documento no afirma que:

- TGCV sea universal;
- `T_acc` sea un primitivo ontológico independiente de `S`;
- los cambios de accesibilidad sean causalmente eficaces;
- TGCV prediga o genere Value;
- TGCV sea superior a representaciones alternativas;
- TGCV sea plenamente original;
- RUST-DYN-2 mida ejecución runtime de Cargo;
- H>1 trajectory sufficiency esté demostrada;
- exista actualmente un segundo dominio empírico listo para replicación.

## 13. Estado

**CURRENT-SITUATION DRAFT / CONTROLLED.**

Esta versión supersede únicamente el papel del TCP como activo externo actual. `TGCV-EXT-TCP-001_v0.2.md` permanece preservado como artefacto histórico.
