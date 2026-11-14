# DEC-C10-101 — Aceptación del inicio de la ventana post-Z de V_cont en t0

**Fecha:** 2026-11-12  
**Estado:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Complementa:** DEC-C10-099 (selección de V_cont) y DEC-C10-100 (agregación temporal igualitaria).

## 1. Decisión

El usuario acepta iniciar la ventana de V_cont en **t0, inmediatamente después de la asignación Z**, incluyendo el periodo de provisión e instalación.

La ventana no queda condicionada a que ocurran intento, recepción, instalación, verificación, C_dep, A_f, Reach, selección o ejecución. Así, los efectos de la política sobre la continuidad durante la provisión no quedan excluidos por definición del resultado.

## 2. Regla temporal

La ventana se representa como [t0,T*], donde T* será un horizonte post-Z común, fijo y preespecificado. Esta decisión no fija T*, duración, unidad temporal, K, resolución ni tolerancia para transitorios.

No se identifica T* automáticamente con t9: t0…t9 es el reloj de etapas causales y no una duración física. H=3 sigue siendo profundidad transformacional y no determina el horizonte ni K.

## 3. Agregación y observación

Se mantiene DEC-C10-100: K intervalos de igual duración en una rejilla común ex ante; V_cont_truth es la fracción temporal de intervalos conformes, con UNKNOWN propagado a bounds y sin complete-case ni imputación automática a cero.

S3 sigue siendo un canal runtime pasivo, vectorial e imperfecto. No envía solicitudes, no activa rutas ni muta el sistema. S4 apoya identidad/versión/integridad y S5 aporta el contrato ENABLED/PROFILE; ninguno sustituye S3. No se presume independencia entre señales, tasas constantes ni MCAR/MAR/MNAR. El Analyzer no recibe truth, potenciales, semillas ni parámetros reservados.

## 4. Lo que no queda aprobado

Permanecen OPEN: T*, unidad temporal, K, resolución, duración mínima de interrupción relevante, regla para fallos breves/transitorios/fronteras, indicadores S3 concretos, cobertura, correlación, error, calibración, sensibilidad y discriminación frente a O-CONF.

Esta decisión no aprueba Design Freeze, schema físico, fixtures, código, implementación, generación de datos, simulación, estimación ni ejecución científica.

## 5. Estado y autorización

**WINDOW_START_T0_ACCEPTED / TSTAR_OPEN / K_OPEN / S3_SIGNAL_VALIDITY_OPEN / NOT_DESIGN_FROZEN.**

`scientific_execution=false`  
`execution_authorized=false`

**Trazabilidad:** aceptación expresa del usuario en la conversación del 2026-11-12: “Acepto iniciar la ventana V_cont en t0, incluyendo provisión e instalación.”
