# VALUE — Registro de versiones y documentos de diseño

**Propósito:** distinguir la fuente integrada anterior a la normalización, el documento maestro de referencia y una alternativa de ciclo todavía no evaluada.

## Estado de cada documento

### 1. DOCUMENTO MAESTRO — vigente como referencia de trabajo

[VALUE — Diseño integrado del estándar metodológico (v0.2)](../VALUE_METHODOLOGY_LIFECYCLE_001.md)

- Es la referencia de trabajo para normalización, decisiones metodológicas y siguientes entregables.
- Mantenerlo como maestro salvo justificación clara y documentada para cambiarlo.
- Su estado es propuesta en revisión; no significa que la metodología esté empíricamente validada.

### 2. ARCHIVO HISTÓRICO — original anterior a la normalización

[ARCHIVE — VALUE Methodology v0.1, original no normalizado](ARCHIVE_ORIGINAL_UNNORMALIZED_VALUE_METHODOLOGY_v0.1.md)

- Copia textual exacta del documento previo a la normalización, recuperada del commit `86936ed02141052fc202d0218e4b74576110b6c4`.
- Solo para trazabilidad histórica y comparación de cambios.
- No usar como referencia metodológica activa ni editar para reflejar decisiones posteriores.

### 3. ALTERNATIVA — ciclo VALUE de cinco etapas, NO EVALUADA

[ALTERNATIVA NO EVALUADA — Visualizar / Align / Learn / Unlock / Execute & Evolve](ALTERNATIVE_UNEVALUATED_VALUE_FIVE_STAGE_CYCLE_v0.1.md)

- Explora el ciclo mnemónico V-A-L-U-E y reasigna los ocho artefactos canónicos a sus cinco etapas.
- No sustituye al maestro ni es el flujo aprobado.
- Requiere comparación explícita antes de adoptar cualquier elemento o reemplazar el ciclo maestro.

## Convención de gobernanza

1. El maestro es la única referencia activa para el trabajo metodológico, salvo decisión documentada.
2. El archivo histórico se conserva sin alteraciones de contenido.
3. Toda propuesta alternativa debe incluir en el título y el cuerpo su estado: propuesta, no evaluada, aceptada o rechazada.
4. La decisión entre ciclos debe basarse en una comparación documentada de comprensión, cobertura, trazabilidad, esfuerzo de aplicación y utilidad en casos reales.
5. No trasladar automáticamente al playground una alternativa no evaluada.
6. Los cambios se versionan en GitHub mediante commits y revisión; no dependen de la memoria de conversación.

## Relación de versiones

| Documento | Versión | Estado | Función |
|---|---|---|---|
| `../VALUE_METHODOLOGY_LIFECYCLE_001.md` | 0.2 | **MAESTRO DE REFERENCIA** | Normalización actual. |
| `ARCHIVE_ORIGINAL_UNNORMALIZED_VALUE_METHODOLOGY_v0.1.md` | 0.1 | **ARCHIVO HISTÓRICO** | Trazabilidad del documento anterior. |
| `ALTERNATIVE_UNEVALUATED_VALUE_FIVE_STAGE_CYCLE_v0.1.md` | 0.1 | **ALTERNATIVA NO EVALUADA** | Explorar el ciclo mnemónico VALUE de cinco etapas. |

