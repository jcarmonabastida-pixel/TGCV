# DEC-C10-100 — Aceptación provisional de agregación temporal igualitaria de V_cont

**Fecha:** 2026-11-12  
**Estado:** ACCEPTED — PROVISIONAL OPERATIONALIZATION DECISION; MEASUREMENT/IDENTIFICATION/DISCRIMINATION GATES OPEN.

## Decisión

Se acepta como escala inicial de la verdad sintética de V_cont la fracción temporal de cumplimiento funcional B1 en una ventana post-Z común, calculada como media no ponderada de los estados latentes por intervalos de igual duración:

`V_cont_truth(i) = (1/K) Σ_{k=1}^{K} A_B1(i,k)`

donde `A_B1(i,k) ∈ {1,0,?}` representa, para la UE i y el intervalo k, el cumplimiento de la función basal B1 conforme al contrato funcional versionado y a ENABLED/PROFILE.

- `1`: cumplimiento funcional positivamente estipulado por el DGP.
- `0`: incumplimiento funcional positivamente estipulado por el DGP.
- `?`: verdad no determinada para ese intervalo; nunca se convierte automáticamente en 0.

La rejilla y los intervalos deben ser comunes, de igual duración y definidos ex ante. En intervalos todos determinados, la media es la fracción de tiempo funcional. Si hay intervalos desconocidos, el Evaluator conserva bounds: límite inferior = número de intervalos con 1 dividido por K; límite superior = (intervalos con 1 + intervalos ?) dividido por K. No se usa complete-case ni se reduce el denominador para fabricar una estimación puntual.

## Alcance y condiciones

1. La decisión cierra la regla de agregación de la truth sintética, no K, duración, frecuencia, origen/fin de ventana, baseline, transitorios, magnitud mínima relevante, tolerancias o diseño de muestreo temporal.
2. El estimando de V_cont se refiere al nivel post-Z en una ventana común. No se transforma en cambio respecto al baseline ni se resta baseline salvo decisión separada y justificada.
3. S3 sigue siendo un canal pasivo, no-mutante y vectorial de señales imperfectas. No es verificador directo de A_B1 ni se promedia para sustituir V_cont. La recuperación puntual exige un modelo de medición identificable y la información de calibración permitida al Analyzer; en caso contrario, bounds o abstención.
4. La truth permanece reservada al Generator/Evaluator. Analyzer recibe solo S3 y metadatos de cobertura/tiempo/identidad permitidos, nunca A_B1, V_cont_truth, potenciales, parámetros reservados o semillas.
5. La aceptación no prueba validez de medida, identificación, validez empírica del proxy ni discriminación frente a O-CONF/F*. Esos gates permanecen abiertos y se evaluarán con contratos existentes P182/P183/MEAS/MISS/P179, sin crear nuevas familias.
6. O-CONF continúa como resultado técnico terminal distinto; la separación lógica entre una interrupción temporal y el estado terminal solo constituye prueba de discriminación cuando F*, evento terminal, oráculo, snapshot e instrumentos estén especificados y evaluables.
7. V_cont sigue siendo la dimensión mínima provisional seleccionada por DEC-C10-099. No se agregan otras dimensiones, pesos ni índice compuesto.

## No autorizado

No autoriza fijar parámetros no aprobados, Design Freeze, schema físico, fixtures confirmatorios, código, implementación, generación de datos, simulación, estimación ni ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

**Aceptación expresa:** respuesta afirmativa del usuario de 2026-11-12 a la propuesta de escala temporal igualitaria.  
**Registro rector:** plan C10-S §16.187 y Decision Log C10-S.  
**Decisión complementaria:** DEC-C10-099 selecciona V_cont como dimensión; esta DEC-C10-100 acepta su regla inicial de agregación temporal.
