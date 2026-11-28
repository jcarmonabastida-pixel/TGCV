# DEC-C10-102 — Aceptación de continuidad estricta por intervalo para V_cont

**Fecha:** 2026-11-12  
**Estado:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Rama de trabajo:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Complementa:** DEC-C10-068 (contrato funcional B1), DEC-C10-099 (selección de V_cont), DEC-C10-100 (agregación temporal igualitaria) y DEC-C10-101 (inicio de ventana en t0).

## 1. Decisión aceptada

El usuario acepta evaluar la continuidad funcional B1 estrictamente dentro de cada intervalo, sin periodo de gracia ni tolerancia implícita para interrupciones funcionales confirmadas.

Para cada unidad experimental i e intervalo k:
- **Truth=1:** la regla funcional ENABLED/PROFILE se cumple durante todo el intervalo.
- **Truth=0:** ocurre al menos un incumplimiento funcional confirmado en cualquier instante del intervalo.
- **Truth=?:** únicamente cuando la truth funcional del intervalo no queda determinada por el Generator.

No se introduce duración mínima de fallo, cuota tolerada de interrupciones ni promedio intraintervalo. Un fallo breve pero confirmado cuenta como incumplimiento del intervalo.

## 2. Separación truth/observación

La falta, pérdida, lag o cobertura insuficiente de S3 pertenece al canal de observación y no convierte la truth en 0, 1 o ?. S3 sigue siendo pasivo, vectorial e imperfecto. Si no puede detectar los eventos que el DGP estipula como relevantes, Analyzer debe producir bounds o abstenerse; no puede afirmar continuidad por ausencia de señal.

Los eventos exactamente en frontera se asignarán de forma determinista, única y versionada a un intervalo antes de materializar.

## 3. Consecuencia temporal

Se mantiene el inicio t0 aceptado por DEC-C10-101. Se recomienda un reloj explícito de tiempo transcurrido, con unidad normalizada declarada, eventos fechados y rejilla regular. El orden t0…t9 no proporciona duración física; H=3 es profundidad transformacional y no determina ventana, frecuencia ni K.

T* deberá cubrir provisión/instalación y seguimiento hasta el último evento causal que pueda modificar el cumplimiento B1 dentro del estimando. K=(T*−t0)/Δ con Δ constante y divisibilidad exacta preespecificada; no se admiten intervalos residuales de duración distinta. Unidad, eventos relevantes, duración mínima representable, T*, Δ, K, regla de cierre y calibración/cobertura S3 siguen OPEN.

## 4. Límites

Esta decisión no autoriza implementación, materialización, generación, simulación, estimación, calibración ni Design Freeze. No fija parámetros numéricos ni demuestra validez del canal S3.

**Estado:** STRICT_INTERVAL_CONTINUITY_ACCEPTED / NO_GRACE_PERIOD / EVENT_CLOCK_AND_GRID_RECOMMENDED / TSTAR_DELTA_K_OPEN / NOT_DESIGN_FROZEN.

**Trazabilidad:** aceptación expresa del usuario en la conversación del 2026-11-12: “Sí”. Plan integrado §16.192; reconciliación temporal B1/Need_preZ §11; auditoría temporal/S4R §9; Decision Log C10-S.

scientific_execution=false  
execution_authorized=false
