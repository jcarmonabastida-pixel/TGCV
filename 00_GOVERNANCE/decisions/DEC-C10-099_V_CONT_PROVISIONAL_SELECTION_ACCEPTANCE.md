# DEC-C10-099 — Selección provisional de V_cont como dimensión mínima de Value

**Fecha:** 2026-11-12  
**Estado:** ACCEPTED — PROVISIONAL DESIGN DECISION; MEASUREMENT/IDENTIFICATION GATES OPEN.

## Decisión

Se formaliza la aceptación expresa registrada en el plan C10-S §16.174: para la extensión sintética B, se selecciona provisionalmente `V_cont` como única dimensión mínima de Value del núcleo confirmatorio candidato. `V=(V_cont)` se conserva como vector unitario, sin índice compuesto, pesos ni compensación con otras dimensiones.

`V_cont` representa la continuidad temporal de la capacidad efectiva del servicio que B1 pretende mantener disponible conforme al objetivo basal y al contrato funcional versionado (admitir solicitudes conforme a ENABLED y exponer PROFILE). No es el flag ENABLED, una configuración terminal, la admisión/respuesta de la única oportunidad estandarizada, O-CONF/F*, ni una recodificación de accesibilidad, Reach o trayectoria.

## Alcance y condiciones

1. La aceptación selecciona el constructo/dimensión, no su indicador, fórmula, resolución, ventana, baseline, horizonte, unidad, fuente, escala ni regla de agregación.
2. La perspectiva B1 se conserva como referente; el criterio normativo del DGP, las consecuencias potenciales y el mecanismo de valoración deben estar estipulados ex ante.
3. La medición debe ser independiente de `ΔT_acc*`, Reach/trayectoria y Outcome técnico. La verdad temporal del DGP se mantiene separada de la evidencia observada y del acceso del Analyzer.
4. Deben superarse los gates de validez de medición, cobertura/error/missingness (P182/P183 y MEAS/MISS existentes), discriminación frente a O-CONF/F* y factibilidad de identificación para los estimandos pertinentes.
5. Si no se supera cualquiera de esos gates, `V_cont` no será endpoint confirmatorio identificable en el diseño resultante. No se sustituirá silenciosamente por otra dimensión ni se declarará Value confirmado.
6. Esta decisión posterior y más específica complementa DEC-C10-095: A permanece como DGP base; B es extensión sintética independiente y versionada. No altera P179 (Value vectorial y trade-offs), no selecciona dimensiones adicionales y no modifica claims.

## No autorizado

No autoriza Design Freeze, schema físico, captura, fixtures, código, implementación, generación de datos, simulación, estimación ni ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

**Registro de aceptación original:** C10-S plan §16.174 (2026-11-12).  
**Artefactos rectores a propagar:** Decision Log C10-S, maestro consolidado C10-S y plan integrado de cierre.
