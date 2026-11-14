# DEC-C10-079 — Identidad global y supersession append-only de filas del manifiesto PAR

**Fecha:** 2026-11-08  
**Estado:** ACEPTADA — contrato documental lógico  
**Ámbito:** C10-S / Instance Applicability Manifest (IAM) / filas lógicas PAR  
**Rama de registro:** `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta el contrato lógico de identidad y revisión de las filas PAR del manifiesto IAM:

1. **Unicidad global:** `manifest_record_id` es opaco, inmutable, no vacío, nunca reutilizable y globalmente único en toda la línea C10-S, con independencia de la versión del manifiesto/IAM. La versión IAM sigue siendo parte del contexto de resolución, pero no limita el namespace de unicidad.
2. **Append-only:** los registros no se sobrescriben ni eliminan. Toda corrección de captura, evidencia, mapping, estado o adjudicación para la misma clave lógica crea un nuevo `manifest_record_id`; el registro anterior permanece íntegro.
3. **Revisión explícita:** `manifest_record_revision` empieza en 1 para cada clave lógica de observación y aumenta exactamente en uno. Es secuencia de captura/adjudicación, no versión semántica del parámetro.
4. **Supersession:** toda revisión posterior incluye `supersedes_manifest_record_id`, apuntando al registro inmediatamente anterior de la misma clave lógica. Se admite una única cadena lineal, sin bifurcaciones, ciclos, saltos, huérfanos ni referencias cruzadas entre claves.
5. **Nombres normativos exactos:** `manifest_record_revision` y `supersedes_manifest_record_id`.
6. **Nueva observación:** cambio de contrato/instancia, snapshot, etapa, ruta/scope, revisión del CMP owner o cualquier dimensión de la clave lógica inicia una nueva cadena en revisión 1. Cambio semántico de `parameter_key` exige nueva identidad semántica, no supersession.
7. Varias evidencias vinculadas a una fila no crean revisiones por sí solas. El mero reempaquetado por una nueva versión IAM tampoco crea una observación nueva; cualquier migración entre versiones requiere mapping explícito y no se presume.

## 2. Reglas de integridad

- Un `manifest_record_id` identifica exactamente un registro y no puede repetirse en ningún manifiesto C10-S.
- La combinación de clave lógica + revisión identifica exactamente un registro.
- Revisión 1 no tiene predecesor; revisiones posteriores apuntan a la revisión inmediatamente anterior.
- Toda supersession conserva la misma clave lógica y pinning exacto de snapshot y CMP owner.
- Se preservan por separado las evidencias múltiples y la identidad independiente de `coverage_scope_id`.

## 3. Límites explícitos

Esta decisión no crea tabla PAR, columnas U_G, DDL, serialización, generador de IDs, API, parser, validator, fixtures ni registros reales. No cierra el crosswalk PAR↔U_G, no sella IAM, no asigna valores de escenario, no modifica DEC-C10-062 ni convierte `manifest_record_id` en entidad U_G. No autoriza Design Freeze, implementación, validación técnica ni experimento.

`scientific_execution=false`; `execution_authorized=false`.

## 4. Propagación y precedencia

Esta decisión resuelve las tres cuestiones planteadas en las propuestas §17.1/§17.2, §19.20/§19.21, §20/§21, §16.62/§16.63, §80/§81, §207/§208 y §86/§87. En caso de contradicción, DEC-C10-079 prevalece; las propuestas anteriores se conservan como historial y no como estado pendiente.

## 5. Consecuencias

1. La matriz de mapping PAR, la matriz IAM, la plantilla de inventario U_G, el plan de cierre, la Closure Control Matrix, el maestro C10-S y el Decision Log deben reflejar este contrato lógico.
2. La decisión es documental y no constituye cierre del IAM, freeze del schema ni autorización de implementación/ejecución.
