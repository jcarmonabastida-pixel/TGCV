# TGCV-EXT-RP-001 — Research Prospectus v0.2

**Programa:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos  
**Clase:** Prospecto de investigación científico  
**Estado:** CURRENT / CONTROLLED  
**RMA ID:** TGCV-EXT-RP-001  
**Fecha:** 2026-09-11  
**Predecesor:** v0.1  
**Base canónica:** RMA v3.32 + Evidence→Claim Matrix v1.1 + TR-131 + TCP v0.4 + Vision Paper v0.3

## 1. Propósito y problema de investigación

El programa investiga si puede establecerse una capa analítica transversal que permita representar cómo las condiciones de un sistema determinan qué transformaciones son accesibles, cómo cambia esa estructura a lo largo del tiempo y bajo qué condiciones explícitas esas modificaciones pueden relacionarse con Reach, Trajectory, Outcome y Value.

La pregunta no presupone una teoría transversal ya establecida. TGCV se mantiene como programa de investigación integrador propuesto y falsable. Tampoco presupone que una modificación de accesibilidad produzca causalmente un efecto positivo, genere valor o sea superior a alternativas existentes.

## 2. Objeto científico y arquitectura mínima

El objeto de estudio es la estructura y evolución de las transformaciones accesibles de un sistema.

La arquitectura actual distingue:

- `S`: sistema/estado relevante;
- `C`: contexto y condiciones relevantes;
- `L`: restricciones, recursos y condiciones de legalidad/admisibilidad;
- `Uτ`: universo candidato de transformaciones;
- `τ`: transformación canónica;
- `Pτ(S,C,L)`: predicado de accesibilidad;
- `T_acc = {τ ∈ Uτ | Pτ(S,C,L)=1}`;
- `ΔT_acc`: cambio de la estructura accesible entre estados;
- `Reach`: estados/configuraciones alcanzables bajo una semántica declarada;
- `Trajectory`: secuencia o estructura temporal de estados/alcances bajo una semántica declarada;
- `Outcome`: resultado observado;
- `Value`: consecuencia valorativa dependiente del contexto y de una definición explícita.

La ontología mínima mantiene `S` como Core. `T_acc` es un objeto analítico indispensable para representar y comparar cambios de accesibilidad, pero no un primitivo ontológico independiente de `S`. `I` permanece como mecanismo explicativo posible, no como primitivo del Core.

## 3. Dinámica y separación de capas

La arquitectura de trabajo es:

`mecanismo → (S_t,C_t) → (S_{t+1},C_{t+1}) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Esta cadena es una arquitectura analítica y no una afirmación causal completa. Cada relación requiere definición, operacionalización y evidencia propias.

El programa debe preservar las distinciones entre accesibilidad, Reach, Trajectory, Outcome y Value. En particular, la ejecución u observación de una transformación no debe utilizarse retrospectivamente para definir su accesibilidad.

## 4. Consecuencia metodológica actual

La enumeración completa ex ante de toda `T_acc(S_t)` **no es un requisito universal**. La operacionalización debe concentrarse, según el caso, en:

1. una transformación o conjunto candidato concreto;
2. el estado/contexto relevante `(S_t,C_t)`;
3. una regla de accesibilidad/admisibilidad independiente del resultado;
4. condiciones congeladas en el momento de decisión;
5. una transición de estado reconstruible.

El conocimiento parcial de alternativas no constituye por sí mismo un criterio de rechazo. La accesibilidad debe permanecer separada de la observación del Outcome. El cierre operativo de accesibilidad es dependiente del caso.

## 5. Estado actual de la evidencia

La evidencia científica permanece acotada y gobernada. RUST-DYN-1 analizó 516.061 pares temporales adyacentes y observó 438.203 pares no persistentes del espacio accesible (~84,91%), con casos de expansión, contracción, persistencia y reconfiguración. RUST-DYN-2 mostró, bajo una semántica de Reach potencial de profundidad 1, casos que distinguen cambios de `T_acc` y Reach, incluidos ND-1=159.921, ND-2=278.282 y ND-4=266.201.

La evidencia adicional incluye: IUT-A-01 U2 FULL_PILOT, clasificado `U2-NULL` tras M1 PASS y M2 FAIL; IT-NOSD-010 G0/G1/G2 como evidencia metodológica acotada de reconstrucción y separación downstream; EXT-UPD-4.8 O3 como evidencia de frontera de cierre de accesibilidad (`INDETERMINATE / H-B / HS-AC01`); y evidencia fixture-level Class-II AWS.

Estos resultados no demuestran causalidad, valor, superioridad, universalidad, originalidad plena, utilidad industrial ni validación transversal completa. Tampoco convierten RUST-DYN-2 en evidencia de runtime Cargo reachability.

## 6. Frontera de contribución

D-OPS-21 identificó antecedentes cercanos y alta redundancia local. D-OPS-22 dejó abierta una posible no-redundancia residual en la traducción transversal sin demostrar superioridad. D-OPS-23 congeló invariantes mínimos para preservar las distinciones entre estado, universo candidato, accesibilidad, `T_acc`, `ΔT_acc`, Reach, Trajectory, Outcome y Value.

La contribución candidata se formula por tanto de manera prudente como una **arquitectura analítica de traducción transversal** que permita comparar cómo dominios heterogéneos representan y modifican estructuras de transformaciones accesibles y cómo, bajo condiciones explícitas, esas modificaciones pueden conectarse con estructuras downstream.

Esta formulación sigue siendo una hipótesis de contribución y no una afirmación de originalidad o superioridad.

## 7. Preguntas de investigación

### RQ1 — Estructura mínima
¿Qué representación mínima permite distinguir sistema, transformaciones candidatas, accesibilidad y cambio de accesibilidad sin redundancia conceptual injustificada?

### RQ2 — Dinámica
¿Bajo qué condiciones puede identificarse `ΔT_acc` independientemente del Outcome y distinguirse de cambios de estado, Reach o Trajectory?

### RQ3 — Traducción transversal
¿Puede TGCV traducir constructos de dominios heterogéneos conservando sus diferencias semánticas sin reducirlos a simples renombramientos?

### RQ4 — Reach y Trajectory
¿En qué condiciones un cambio de accesibilidad se relaciona con diferencias en Reach o Trajectory, y qué evidencia adicional exige esa relación?

### RQ5 — Outcome y Value
¿Bajo qué condiciones, si alguna, pueden relacionarse cambios de accesibilidad con Outcome y Value sin circularidad ni confusión entre accesibilidad y valor?

### RQ6 — Límites
¿En qué dominios o condiciones fallan la identificabilidad, la no-redundancia, la traducción o la separación de capas?

## 8. Programa metodológico y falsabilidad

El programa sigue una secuencia gobernada por evidencia:

`Problema → Preguntas → Evidencia → Síntesis → Modelo → Operacionalización → Validación → Traducción → Arquitectura/Transferencia → Aprendizaje`

Cada prueba debe congelar previamente unidades de análisis, transformaciones candidatas, regla de accesibilidad, condiciones de decisión, reglas temporales, controles y límites de inferencia.

TGCV permanece falsable. Son resultados admisibles: falta de identificabilidad; redundancia con representaciones existentes; ausencia de información útil en `ΔT_acc`; falta de relación defendible con Reach o Trajectory; imposibilidad de vincular Outcome/Value sin supuestos adicionales; o absorción de la arquitectura por antecedentes existentes.

## 9. Estado de operaciones metodológicas

D-OPS-24 y EXT-UPD-4.8 están **cerrados dentro de sus respectivos alcances autorizados**. No se presentan como operaciones pendientes ni este prospecto autoriza su reapertura.

Toda futura operación metodológica o experimental requiere su propio diseño, preflight y autorización. La existencia del Research Prospectus no constituye autorización de ejecución industrial ni científica.

## 10. Orientación de investigación y transferencia

El programa puede alimentar rutas académicas, doctorales, de investigación industrial, demostradores controlados y futuras hipótesis de aplicación. La transferencia no se considera evidencia científica ni validación industrial.

Las oportunidades industriales actuales permanecen en el nivel definido por el MOI v0.1 y el RII v0.1: hipótesis y rutas de descubrimiento sujetas a evidencia adicional. El prospecto no atribuye beneficios a organizaciones concretas ni establece utilidad, superioridad, causalidad o valor financiero.

## 11. No-claims

Este prospecto no afirma:

- validez universal de TGCV;
- que `T_acc` sea un primitivo ontológico independiente;
- eficacia causal de cambios de accesibilidad;
- generación o predicción de Value;
- superioridad explicativa o de rendimiento;
- originalidad plena;
- validación transversal completa;
- suficiencia demostrada de trayectorias de profundidad superior a 1;
- utilidad industrial, producción o beneficio financiero demostrado;
- validación por una organización, socio o dominio externo;
- autorización para ejecución industrial.

## 12. Resultado esperado

El programa busca determinar, mediante pruebas independientes y falsables, si la arquitectura mínima y su protocolo de traducción preservan información científicamente útil entre dominios heterogéneos y si permiten establecer relaciones defendibles entre accesibilidad, Reach, Trajectory, Outcome y Value.

El resultado final puede ser una teoría consolidada, una arquitectura parcial, una delimitación de aplicabilidad o un resultado negativo. El prospecto no presupone cuál de estos resultados será obtenido.

## 13. Estado

**CURRENT / CONTROLLED.**

La v0.1 permanece preservada como histórico/inmutable. Las adaptaciones específicas de programa o candidatura no sustituyen el prospecto canónico y deben mantener su propia frontera de alcance.