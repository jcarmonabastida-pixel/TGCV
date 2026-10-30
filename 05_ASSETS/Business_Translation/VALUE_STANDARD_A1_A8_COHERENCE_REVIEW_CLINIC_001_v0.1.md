# VALUE — Revisión de coherencia del estándar A1–A8 a partir de CLINIC-001

**Identificador:** VALUE-STANDARD-COHERENCE-CLINIC-001  
**Versión:** 0.1  
**Fecha:** 2026-10-30  
**Estado:** REVISIÓN DOCUMENTAL REALIZADA — aclaración aprobada e incorporada al documento maestro v0.3  
**PR:** #114  
**Caso contrastado:** CLINIC-001 v1.1

## 1. Objetivo y alcance

Comprobar si las lecciones de las revisiones A3→A5 y A6→A8 están ya representadas en:
- `VALUE_METHODOLOGY_LIFECYCLE_001.md` (arquitectura maestra v0.2);
- `VALUE_ARTIFACT_MASTER_SPECS_v0.1.md` (fichas A1–A8 v0.1);
- el caso ficticio CLINIC-001 v1.1.

Esta revisión es documental. No valida empíricamente VALUE/TGCV, no convierte las fichas en estándar aprobado y no modifica el protocolo de usabilidad.

## 2. Resultado por artefacto

| Artefacto | Lo que ya recoge el estándar/ficha | Contraste con CLINIC-001 | Resultado |
|---|---|---|---|
| A1 — Value Intent | Propósito, personas afectadas, criterios, restricciones y autoridad de decisión | El caso mantiene criterios y salvaguardas sin convertirlos en umbrales inventados | Cubierto |
| A2 — Opportunity Brief | Contexto, señales, fuentes, preguntas y supuestos | La oportunidad se separa de la solución y de la causa raíz no demostrada | Cubierto |
| A3 — Value System Model | Alcance, elementos y relaciones con IDs estables, estado epistemológico, fuentes, límites y vistas | CLINIC-001 incorpora E01–E07 y R01–R07, dejando explícito que son propuestas conceptuales | Cubierto |
| A4 — Hypothesis & Options | Cambio, mecanismo, personas/capacidades, supuestos, evidencia favorable/contraria, riesgos, pruebas y descarte | Las opciones O0–O4 se enlazan con A3; H-V1 tiene cadena de razonamiento y criterios de revisión | Cubierto |
| A5 — Evidence Record | Fuente, método, contexto, calidad, sesgo, contradicción, verificación y afirmación apoyada | La matriz distingue datos pertinentes, datos que no miden el mecanismo y brechas de evidencia | Cubierto |
| A6 — Decision Record | Autoridad, criterios, evidencia, trade-offs, decisión, condiciones y autorización explícita para el siguiente paso | El caso diferencia selección de O1 de autorización formal no concedida | Parcial: la ficha lo permite, pero la arquitectura maestra no explicita con suficiente nitidez la diferencia entre autorizar diseño y autorizar ejecución |
| A7 — Blueprint & Delivery Plan | Referencia a decisión autorizante, diseño, plan, responsables, recursos, estados, aceptación, parada/reversión | El caso separa propuesta no autorizada, secuencia contrafactual y ausencia de ejecución | Cubierto en ficha; requiere que A6 identifique con precisión el alcance autorizado |
| A8 — Learning Record | Resultados observados, periodo, comparación, efectos, límites de atribución y cambios entre plan y ejecución | El caso identifica valores fabricados y ausencia de resultados observados o aprendizaje empírico | Cubierto; conviene mantener la distinción entre reconstrucción documental y aprendizaje basado en resultados observados |

## 3. Hallazgo principal

Las fichas A1–A8 ya contienen la mayoría de las salvaguardas que han resultado necesarias durante la revisión del caso. No procede duplicar sus campos ni añadir controles adicionales a cada ficha.

La única aclaración arquitectónica que merece consideración está en la transición DECIDE→ACT:

**No toda decisión de avanzar autoriza la ejecución.** Deben distinguirse al menos:
1. autorización para continuar el diseño o preparar una propuesta;
2. autorización formal para ejecutar, con alcance, autoridad, recursos, condiciones y límites explícitos.

Una decisión puede autorizar únicamente el primer nivel, mantener el segundo pendiente o decidir no continuar. A7 no puede inferir autorización de ejecución a partir de la selección de una opción.

La ficha A6 ya solicita «responsable y autorización para el siguiente paso» y exige alcance explícito de la autorización; la ficha A7 exige referencia a la decisión que autoriza el trabajo. Por tanto, la brecha es de claridad en la arquitectura maestra, no ausencia completa de control en las fichas.

## 4. Ajuste mínimo propuesto al documento maestro

Añadir en la definición de DECIDE / transición a ACT una regla breve:

> La decisión de seleccionar una alternativa o autorizar el desarrollo de su diseño no equivale a autorizar su ejecución. La autorización para ejecutar debe ser explícita, emitida por la autoridad competente y especificar alcance, recursos, condiciones, salvaguardas y límites. Si no existe, A7 permanece en estado de propuesta y ACT no se inicia.

Y precisar en A8:

> A8 puede registrar revisiones documentales o aprendizaje de proceso aunque no exista ejecución, pero debe identificar su naturaleza. Las afirmaciones sobre resultados de intervención o valor realizado requieren resultados observados y evidencia trazable; los datos simulados o contrafactuales no se presentan como aprendizaje empírico.

La segunda frase podría ser redundante con las fichas y el principio general de evidencia. Se recomienda incorporar únicamente la primera regla al maestro; mantener la segunda como interpretación operativa ya cubierta por A5/A8 y demostrada en CLINIC-001.

## 5. Cambios que no se recomiendan

- No crear artefactos A9 ni nuevas fases.
- No ampliar A3 con protocolos operativos o escenarios adicionales.
- No repetir en el maestro los campos detallados de las fichas A1–A8.
- No añadir umbrales, puntuaciones o fórmulas universales.
- No modificar el protocolo de usabilidad antes de cerrar la autoevaluación y revisar su estado real.
- No declarar el estándar validado ni cambiar su estado de borrador por el mero hecho de completar esta revisión.

## 6. Dictamen y decisión

**Dictamen:** las fichas maestras A1–A8 son coherentes, en lo sustancial, con las lecciones del caso. El documento maestro necesita una aclaración breve en DECIDE→ACT para evitar que una selección o autorización de diseño se interprete como permiso de ejecución.

**Decisión del usuario:** aprobó la regla mínima propuesta el 2026-10-30. Se incorporó en `VALUE_METHODOLOGY_LIFECYCLE_001.md`, versión 0.3, sección 4.5. Las fichas maestras A1–A8 permanecen sin cambios porque ya contemplaban el alcance explícito de la autorización. La incorporación no constituye aprobación definitiva ni validación empírica del estándar.

## 7. Referencias

- `VALUE_METHODOLOGY_LIFECYCLE_001.md`, v0.2.
- `VALUE_ARTIFACT_MASTER_SPECS_v0.1.md`, v0.1.
- `VALUE_FICTIONAL_CASE_CLINIC_001_v1.1.md`, versión 1.1.
- `VALUE_A3_A4_A5_COHERENCE_REVIEW_CLINIC_001_v0.1.md`.
- `VALUE_A6_A7_A8_DECISION_EXECUTION_LEARNING_REVIEW_CLINIC_001_v0.1.md`.

**Límite:** revisión de coherencia documental; no constituye validación empírica de usabilidad, eficacia, causalidad ni validez de VALUE/TGCV.
