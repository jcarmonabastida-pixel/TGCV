

## 277. DEC-C10-099 — V_cont: selección provisional y límites (2026-11-12)

Se incorpora la decisión aceptada DEC-C10-099. Para la extensión sintética B, V_cont es la única dimensión mínima provisional de Value; V=(V_cont), sin índice ni pesos. La selección del constructo no operacionaliza su medición. Indicador, regla temporal, baseline, horizonte, resolución, fuente, escala, agregación, error, cobertura y adjudicación permanecen OPEN. Se exige separación truth_dgp/observed_evidence/evaluation, independencia respecto de ΔT_acc*/Reach/trayectoria y Outcome técnico, y gates de discriminación frente a O-CONF/F* y de identificación. Si fallan, V_cont queda NOT_CONFIRMATORY/NOT_IDENTIFIED; no se sustituye por otra dimensión. DEC-C10-095 sigue rigiendo A/B en su alcance, complementada por esta decisión específica posterior para B. No se autoriza implementación ni ejecución.


## 278. Contrato de medición sintética V_cont — referencia integrada (2026-11-12)

La especificación rectora se encuentra en el plan C10-S §16.182. V_cont tiene selección provisional por DEC-C10-099; truth temporal B1 y canal S3 pasivo se mantienen separados. S3 es un vector de indicadores runtime imperfectos, no evidencia funcional concluyente. La recuperación puntual requiere un canal identificable/calibrado y acceso permitido al protocolo; sin ello, bounds o NOT_IDENTIFIED. La regla de agregación, K, ventana, frecuencia, baseline y parámetros siguen abiertos. O-CONF/F* y la discriminación terminal/temporal siguen CONDITIONAL/NOT_VERIFIABLE. No se autoriza implementación ni ejecución.



## 279. N16 — F* y ficha §224 de O-CONF (2026-11-12)

La especificación rectora está en el plan §16.184 y la matriz F* §22. F* es criterio de ruta completa; O-CONF es su adjudicación terminal, no un Outcome duplicado. La unidad es instancia × ruta, anclada en F2_DST_APPLIED o A2_DST_APPLIED; la regla lógica 1/0/? es no compensatoria sobre FP-01…07, con FP-08 separado. PAR/RUL y las etapas de aplicación/post-check reutilizan DEC-C10-083…088. La ficha §224 queda PARTIAL, no operacionalizada: IAM, atomización/mappings globales, C0/G/H materiales, snapshots/evento, tolerancias, oráculo, validación, error/cobertura/acuerdo y firewall efectivo siguen abiertos. V_cont conserva su dimensión temporal y la discriminación frente a O-CONF no está verificada. No Design Freeze ni autorización de ejecución.
