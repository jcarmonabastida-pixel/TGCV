# TGCV-EXT-TCP-001 — Testable Concept Paper (TCP) v0.2

**Programa:** TGCV — Teoría General de la Construcción de Valor  
**Clase:** Externo científico/técnico  
**Estado epistemológico:** WORKING / CONDITIONAL  
**Revision status:** Internal critical review completed; v0.2 incorporates integrity corrections and clarification of the test boundary.  
**Versión TGCV de referencia:** arquitectura estabilizada post-TR-140; operationalization later superseded by the explicitly frozen TGCV-EMP-1.1 state.  
**RMA ID:** TGCV-EXT-TCP-001  
**Fecha:** 2026-08-27

## 1. Propósito

El TCP establece la arquitectura mínima que debe conservarse al pasar de la formulación conceptual de TGCV a una investigación empírica falsable. Su función es servir de referencia estructural para el Vision Paper, Research Prospectus, ARM y RII, evitando que cada activo introduzca una teoría distinta.

El objeto de prueba no es si TGCV explica el valor en términos generales. La cuestión inmediata es si la representación operacionalizada de la **estructura de transformaciones accesibles** contiene información empírica relevante que no queda capturada por representaciones convencionales suficientemente fuertes. El TCP separa `T_acc` como constructo, `R` como representación operacional y el desempeño empírico de `R`.

## 2. Estado conceptual de partida

- Ontología mínima: `S`.
- Estructura analítica: `T_acc = F(S,C,L)`.
- Dinámica: `(S_t,C_t) --τ--> (S_{t+1},C_{t+1})`.
- Fenómeno central: `T_acc,t ≄ T_acc,t+1`.
- Consecuencia: `ΔT_acc -> ΔReach -> ΔTrajectory`.
- Extensión de valor: `Trajectory -> Outcome -> Value`.
- Interacción `I`: mecanismo explicativo, no primitivo del Core.

## 3. Fenómeno

TGCV estudia la **modificación de la estructura de transformaciones accesibles de un sistema**.

`T_acc,t ≄ T_acc,t+1`

La modificación es neutral respecto de su signo y puede adoptar expansión, contracción, reconfiguración o sustitución. No debe confundirse con un simple cambio de estado, una interacción, una mera expansión de posibilidades, un conjunto de acciones o una capacidad de cambio.

## 4. Mecanismo y dinámica

Un mecanismo puede producir `(S,C) -> (S',C')`, que a su vez puede modificar `T_acc`. La interacción es sólo una posible instancia de mecanismo.

`mecanismo -> (S_t,C_t) -> (S_{t+1},C_{t+1}) -> ΔT_acc -> ΔReach -> ΔTrajectory -> Outcome -> Value`

## 5. Hipótesis empírica mínima

La hipótesis de trabajo es que una representación operacional `R` de la estructura transformacional puede contener información predictiva incremental sobre un outcome futuro `Y` más allá de una representación convencional `B`, bajo un protocolo sin información futura y con controles contra ventajas espurias.

La formulación histórica `P(Y | S,B,R) != P(Y | S,B)` fue posteriormente corregida por el programa TGCV-EMP-1.1 porque `R=F(S,C,L)` no puede aportar información incremental condicionada a un `S` completamente observado. La formulación empírica válida es de nivel representacional: `P(Y|B,R) != P(Y|B)`.

## 6. Hipótesis nula

`H0: P(Y|B,R) = P(Y|B)`.

No rechazarla implica que la ventaja empírica específica de la representación TGCV no queda demostrada bajo el diseño establecido.

## 7. Qué debe falsarse

1. Identificabilidad: `R` puede operacionalizarse sin circularidad ni información futura ilegítima.
2. No redundancia: `R` no es una simple recodificación del baseline.
3. Información incremental: `R` aporta señal predictiva adicional.
4. Robustez: la señal no desaparece bajo controles razonables.

## 8. Arquitectura comparativa

- M0 — Null.
- M1 — Conventional.
- M2 — Conventional + R.

La comparación principal es `M2` frente a `M1`, con mismo algoritmo y controles sobre complejidad, dimensionalidad, tuning, regularización, codificación accidental, leakage y disponibilidad temporal.

## 9. Decisión

La decisión distingue PASS, FAIL e INCONCLUSIVE y no permite reparar retrospectivamente un FAIL modificando teoría o criterios después de observar resultados.

Los criterios cuantitativos concretos pertenecen al protocolo experimental congelado correspondiente.

## 10. Valor

`ΔT_acc -> ΔReach -> ΔTrajectory -> Outcome -> Value`

La creación de valor es una capa posterior y no justifica retrospectivamente el Core.

## 11. Novedad y prior art

El TCP no declara demostrada la originalidad de TGCV. La SLR debe distinguir similitud terminológica, equivalencia de constructo, equivalencia estructural y absorción arquitectónica completa.

## 12. Dependencias

Entradas: arquitectura estabilizada; TR-129, TR-130 y TR-135–TR-140; especificación experimental; SLR-1.  
Salidas: Vision Paper, Research Prospectus, ARM, RII y actualización del RMA.

## 13. Integridad

No presentar TGCV como universalmente validada; no introducir `I`, `C`, `R`, `Reach`, `Trajectory` o `Value` como nuevos primitivos del Core sin evidencia/gate; no cambiar criterios retrospectivamente; conservar versiones anteriores.

## 14. Estado histórico

**WORKING / CONDITIONAL.** La revisión interna resultó PASS WITH CLARIFICATIONS. Esta versión debe conservarse como artefacto histórico y no confundirse con el protocolo posterior congelado de `TGCV-EMP-1.1`.
