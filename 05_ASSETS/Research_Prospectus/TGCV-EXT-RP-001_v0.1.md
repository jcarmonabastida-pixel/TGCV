# TGCV-EXT-RP-001 — Research Prospectus v0.1

**Programa:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos  
**Clase:** Prospecto de investigación científico  
**Estado:** WORKING / CURRENT-SITUATION DRAFT  
**RMA ID:** TGCV-EXT-RP-001  
**Fecha:** 2026-09-08  
**Base:** TGCV Core actual + SLR-1 + TR-131 + RUST-DYN-1 + RUST-DYN-2 + D-OPS-21/22/23

## 1. Problema de investigación

¿Puede establecerse una capa analítica transversal que permita representar cómo las condiciones de un sistema determinan qué transformaciones son accesibles, cómo cambia ese espacio de transformaciones a lo largo del tiempo y cómo dichas modificaciones pueden relacionarse, bajo condiciones explícitas, con Reach, Trajectory, Outcome y Value?

La pregunta no presupone que exista una teoría transversal ya establecida. Tampoco presupone que toda modificación de accesibilidad produzca causalmente un efecto positivo o genere valor.

## 2. Objeto científico

El programa estudia la estructura y evolución del espacio de transformaciones accesibles de un sistema.

La arquitectura conceptual actual distingue:

- `S`: sistema y su estado relevante;
- `C`: contexto/condiciones relevantes;
- `L`: restricciones, recursos y condiciones de legalidad/admisibilidad;
- `Uτ`: universo candidato de transformaciones;
- `τ`: transformación canónica;
- `Pτ(S,C,L)`: predicado de accesibilidad;
- `T_acc = {τ ∈ Uτ | Pτ(S,C,L)=1}`;
- `ΔT_acc`: cambio en la pertenencia del conjunto accesible entre estados;
- `Reach`: estados o configuraciones alcanzables bajo una semántica declarada;
- `Trajectory`: secuencia o estructura temporal de estados/alcances bajo una semántica declarada;
- `Outcome`: resultado observado;
- `Value`: consecuencia valorativa dependiente del contexto y de una definición explícita.

La ontología mínima actual mantiene `S` como Core. `T_acc` es un constructo analítico indispensable para comparar transformaciones accesibles, pero no un primitivo ontológico independiente de `S`. La interacción `I` permanece como mecanismo explicativo posible, no como primitivo del Core.

## 3. Relación dinámica

La relación de trabajo es:

`(S_t,C_t) → (S_{t+1},C_{t+1}) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

La cadena representa una arquitectura de análisis y no una afirmación causal completa. Cada flecha requiere una semántica y evidencia propias.

En particular, `ΔT_acc`, `ΔReach` y `ΔTrajectory` no son equivalentes: el programa debe preservar estas distinciones en toda operacionalización y traducción entre dominios.

## 4. Estado de la evidencia

La evidencia empírica actual es acotada al dominio Rust y a la operacionalización congelada correspondiente.

RUST-DYN-1 mostró, sobre 516.061 pares temporales adyacentes, cambios persistencia/expansión/contracción/reconfiguración del espacio accesible, con 438.203 pares no persistentes (~84,91%).

RUST-DYN-2 estableció, bajo la misma población temporal y una semántica de Reach potencial de profundidad 1, distinciones empíricas entre cambio de `T_acc` y cambio de Reach. Los resultados incluyen ND-1=159.921, ND-2=278.282 y ND-4=266.201.

Estos resultados constituyen evidencia E1 dentro de la operacionalización Rust congelada. No demuestran causalidad, predicción de valor, generalización transversal, superioridad explicativa, originalidad plena ni runtime Cargo reachability.

## 5. Consecuencia de TR-131

TR-131 estableció que `T_acc` no debe tratarse como un objeto ontológico independiente de `S`, pero sí es analíticamente indispensable para representar y comparar explícitamente modificaciones del espacio transformacional.

Esta consecuencia limita la arquitectura del programa: la contribución no puede basarse en presentar `T_acc` como una entidad ontológica independiente del sistema.

## 6. Frontera de contribución actual

La revisión comparativa D-OPS-21 detectó alta redundancia local y antecedentes cercanos, incluido trabajo sobre adaptation spaces y su drift. D-OPS-22 no demostró superioridad, pero identificó un posible residuo de no-redundancia en la traducción transversal.

D-OPS-23 congeló un protocolo mínimo de traducción que exige preservar, entre otros, las distinciones entre estado, universo candidato, accesibilidad, Reach, Trajectory, Outcome y Value.

Por tanto, la contribución candidata actual se formula de manera prudente como una **arquitectura analítica de traducción transversal** para comparar cómo dominios heterogéneos representan, modifican y relacionan espacios de transformaciones accesibles con estructuras downstream.

Esta formulación es una hipótesis de contribución, no una afirmación de originalidad o superioridad.

## 7. Preguntas de investigación

### RQ1 — Estructura mínima
¿Qué representación mínima permite distinguir sistema, universo de transformaciones, accesibilidad y cambio de accesibilidad sin introducir redundancia conceptual injustificada?

### RQ2 — Dinámica
¿Bajo qué condiciones puede identificarse `ΔT_acc` de manera independiente de los resultados observados y distinguirse de cambios de estado, Reach o Trajectory?

### RQ3 — Traducción transversal
¿Puede el protocolo TGCV traducir constructos de dominios heterogéneos conservando sus diferencias semánticas sin reducirlos a simples renombramientos?

### RQ4 — Trayectorias
¿En qué condiciones un cambio de accesibilidad se relaciona con diferencias en Reach o Trajectory, y qué información adicional requiere una afirmación de este tipo?

### RQ5 — Valor
¿Bajo qué condiciones, si alguna, pueden relacionarse cambios en espacios de transformaciones accesibles con Outcomes y Value sin introducir circularidad ni confundir valor con accesibilidad?

### RQ6 — Límites
¿En qué dominios o condiciones falla la identificabilidad, la no-redundancia o la traducción propuesta?

## 8. Programa metodológico

El programa seguirá una secuencia gobernada por evidencia:

`Problema → Preguntas → Evidencia → Síntesis → Modelo → Operacionalización → Validación → Traducción → Arquitectura/Transferencia → Aprendizaje`

Cada prueba deberá definir previamente sus unidades de análisis, universo de transformaciones, predicado de accesibilidad, reglas temporales, controles y límites de inferencia.

La ejecución de una transformación y su accesibilidad serán tratadas como dimensiones distintas. Los Outcomes y Value se mantendrán downstream de la definición de accesibilidad.

## 9. Próximos tests

El siguiente control científico previsto es **D-OPS-24 — Controlled Translation Trace Conformance Test**, que deberá reconstruir su propio estado histórico y especificar su protocolo antes de cualquier ejecución.

El programa mantiene abiertas la replicación independiente, la generalización cross-domain, la suficiencia de trayectoria, la identificación causal y el vínculo con Value.

## 10. Falsabilidad

TGCV permanece explícitamente falsable. Son resultados científicamente admisibles:

- que una operacionalización no sea identificable;
- que el constructo sea redundante con una representación existente;
- que `ΔT_acc` no aporte información analíticamente útil en un dominio;
- que no se observe relación suficiente con Reach o Trajectory;
- que el vínculo con Outcome o Value no pueda establecerse sin supuestos adicionales;
- que la arquitectura transversal quede absorbida por antecedentes existentes.

Ningún resultado negativo debe reinterpretarse retrospectivamente como un defecto de implementación sin evidencia independiente.

## 11. Alcance y no-claims

Este prospecto no afirma:

- que TGCV sea universalmente válida;
- que los cambios de accesibilidad sean causalmente eficaces;
- que produzcan o predigan Value;
- que la arquitectura sea superior a alternativas existentes;
- que la contribución sea plenamente original;
- que RUST-DYN-2 observe ejecución runtime de Cargo;
- que exista actualmente un segundo dominio empírico listo para replicación;
- que exista suficiencia demostrada para trayectorias de profundidad superior a 1.

## 12. Resultado esperado

El objetivo del programa es determinar, mediante pruebas independientes y falsables, si la arquitectura mínima y su protocolo de traducción preservan información científicamente útil a través de dominios heterogéneos y si esa información permite establecer relaciones defendibles entre accesibilidad, Reach, Trajectory, Outcome y Value.

El resultado final puede ser una teoría consolidada, una arquitectura parcial, una delimitación de condiciones de aplicabilidad o un resultado negativo. El prospecto no presupone cuál de estos resultados será obtenido.
