# C10-S — Addendum al plan, Gate 135: TruthBundle y adjudicación temporal

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Estado:** DOCUMENTAL / NO IMPLEMENTACIÓN / NO EJECUCIÓN.

Gate 135 localiza la discrepancia DEC-C10-100…102 → DGP → TruthBundle → Evaluator. La binarización principal se produce en Generator al combinar ENABLED y PROFILE con conjunción binaria; no existe truth funcional UNKNOWN ni event log que permita adjudicar incumplimientos intraintervalo. TruthBundle conserva la frontera de verdad reservada, pero el payload actual es binario. Sealer mantiene una allowlist observacional S3 sin truth y debe seguir así. Evaluator verifica el sello y compara ITT-Z/ITT-G puntuales, pero no calcula bounds tri-valuados de V_cont.

La semántica de bounds por unidad/régimen es [n1/K,(n1+n?)/K]. No se deriva de ello un método automático para bounds de contrastes causales: potenciales conjuntos, población, soporte e interferencia requieren contrato. UNKNOWN funcional no equivale a S3 missingness; ausencia/lag son estados del canal observacional.

Se reutilizan TruthBundle como frontera, S3/Sealer/firewall, baseline ideal bajo S3 perfecto/completo y evaluación puntual ITT existente, cada uno con alcance acotado. Quedan pendientes los contratos exactos para origen de UNKNOWN, cronología de eventos, fronteras, t0/provisión/instalación y adjudicación de bounds. No se cambian DEC, código, schemas, tests, workflows ni parámetros.

**Siguiente operación:** Gate 136 — auditoría de suficiencia de los contratos temporales existentes y localización de vacíos estrictamente necesarios, antes de decidir cualquier cambio de diseño.

scientific_execution=false; execution_authorized=false.
