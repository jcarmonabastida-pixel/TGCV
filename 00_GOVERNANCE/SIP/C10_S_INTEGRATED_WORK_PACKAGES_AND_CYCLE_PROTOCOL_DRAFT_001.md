# C10-S — Paquetes integrados de cierre y protocolo de ciclos de trabajo

**ID:** C10-S-WORK-PACKAGES-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-11  
**Estado:** ACCEPTED AS WORKING PROCESS / NOT SCIENTIFIC DESIGN FREEZE / NOT IMPLEMENTATION AUTHORIZATION  
**Ámbito:** PR #116, rama `research/c10-s-consolidation-draft`.

## 1. Propósito

Reducir la fragmentación del cierre C10-S. El trabajo se organizará en cinco paquetes integrados. Cada paquete se resolverá, como unidad de trabajo, en una sola iteración o conversación: reconstrucción histórica y reconciliación de fuentes, síntesis, dictamen, decisiones necesarias y persistencia/verificación. No se dividirá deliberadamente en micro-preguntas o micro-gates conversacionales.

Una conversación puede contener análisis extenso y varias operaciones documentales, pero debe producir un resultado integrado y autocontenido del paquete. El usuario no tendrá que aprobar sucesivamente cada subapartado. Solo se solicitará intervención cuando exista una decisión científica real que no pueda derivarse de decisiones aceptadas o de evidencia/documentación disponible.

## 2. Los cinco paquetes

### PA — Contrato causal C1, población, Outcome y Value

Resolver conjuntamente:
- población objetivo y precedencia ya aceptada de P*_{τ2} y P*_F;
- composición y regla de elegibilidad E_i, E_scope, App*(τ2,S0), frontera respecto de A_f y tratamiento de unknowns pre-Z;
- unidad experimental, asignación D2, estimando ITT C1, comparador, consistencia, interferencia y soporte;
- horizonte temporal y relación con H/profundidad, sin equipararlos;
- Outcome técnico, consecuencia para B1/beneficiario y Value como constructos distintos;
- medición, agregación, perspectiva, autoridad de valoración y datos incompletos relevantes para C1.

Salida: contrato C1 integrado, o dictamen explícito de qué partes quedan limitadas/bloqueadas por ausencia de material (p. ej. IAM, snapshots, asignación o reglas de valoración). No inventar unidades, indicadores, pesos, horizonte ni asignación.

### PB — Material D2, servicio B1 y primera etapa C2

Resolver conjuntamente:
- instancia B1 por UE y servicio asociado/versionado;
- arquitectura de provisión, instalación, dependencias y condiciones no focales;
- ausencia de provisión focal de fondo en control y vías colaterales;
- ciclo de petición estandarizada, oportunidad primaria y relación request_id↔trajectory_id;
- mediciones independientes de C_dep*, A_f*, D_f*, ΔT_acc*, Reach y snapshots;
- recursos compartidos/asignados, interferencia, aislamiento y provenance.

Salida: contrato material D2/C2, inventario de hechos y predicados, y límites de factibilidad. La recepción o respuesta técnica no equivale a accesibilidad, Outcome ni Value.

### PC — Atribución de accesibilidad C3 y mediación C4

Resolver conjuntamente:
- correspondencia entre asignación D2 y distribuciones inducidas de accesibilidad;
- estimando focal/general y régimen común q, población, soporte y positividad;
- DAG integrado, vías paralelas, interacciones y efectos de paquete;
- confusión inducida por tratamiento/mediador y variables postasignación;
- separación de efecto total, efecto atribuible a accesibilidad, mediación interventional y residuo;
- supuestos de identificación, sensibilidad, cotas y criterios de no-identificación.

Salida: contrato de estimandos e identificación, indicando qué puede identificarse, bajo qué supuestos, y qué debe declararse no identificado. No equiparar ITT con efecto de accesibilidad ni llamar “directo” al residuo sin definición.

### PD — DGP, mecanismos C5 y evaluación adversarial

Resolver conjuntamente:
- verdad generativa de ΔT_acc, Reach, trayectorias y consecuencias;
- intervenciones contrafactuales por etapa del ciclo de petición y clases de contribución;
- causas concurrentes, interacciones, rutas alternativas y colaterales;
- separación computacional de truth_dgp, observed_evidence y evaluación;
- contratos P177/P178/P179/P182/P183 y demás fichas aplicables;
- medición, fiabilidad/invariancia, missingness, censura, selección, sensibilidad, potencia y error Monte Carlo;
- criterios de recuperación, falsos positivos/negativos, límites y falsadores.

Salida: especificación DGP/evaluación coherente y auditable, o matriz de limitaciones que impida afirmar recuperación/identificación donde no esté demostrada.

### PE — Especificación técnica integrada e implementación

Resolver conjuntamente, solo después del cierre científico necesario:
- schemas y contratos de datos;
- interfaces Generator–Analyzer–Evaluator y separación de roles/verdad;
- IDs, eventos, snapshots, versiones, timestamps y provenance;
- fixtures confirmatorios/adversariales, oráculos, validators y tests;
- manifests, hashes, reproducibilidad, reporting y criterios de aceptación;
- trazabilidad semántica desde cada elemento ejecutable a decisiones y contratos.

Salida: contrato técnico implementable, listo para autorización. La preparación documental de interfaces puede adelantarse sin congelar semántica; código ejecutable, fixtures confirmatorios, simulación y ejecución científica requieren gates cerrados y autorización explícita.

## 3. Ciclo único de resolución por paquete

Cada paquete seguirá el mismo ciclo completo, en una conversación/iteración:

1. **Reconstrucción canónica e histórica:** leer README/bootstrap/estado canónico en main y la fuente vigente de la rama de trabajo; localizar fuentes primarias, decisiones aceptadas, contratos, auditorías y trabajo histórico. Reutilizar lo compatible.
2. **Reconciliación integral:** cruzar todas las dimensiones del paquete y sus dependencias con los demás paquetes. Detectar contradicciones, duplicaciones, definiciones obsoletas, huecos de evidencia y supuestos implícitos.
3. **Síntesis única:** redactar una propuesta coherente y autocontenida, no una sucesión de propuestas parciales.
4. **Clasificación explícita:** cada punto queda como (a) ya resuelto por decisión aceptada; (b) propuesta derivable; (c) decisión científica requerida al usuario; (d) bloqueado/no verificable por ausencia de evidencia/material; o (e) límite/falsador que debe conservarse.
5. **Decisiones mínimas:** presentar al usuario únicamente las decisiones genuinamente no derivables, agrupadas en un único bloque. No reabrir decisiones aceptadas ni pedir confirmaciones redundantes.
6. **Persistencia integrada:** actualizar en el mismo ciclo el maestro C10-S, el registro de decisiones, el plan y la Closure Control Matrix, además de contratos especializados realmente afectados. Evitar crear documentos nuevos si una sección/addendum en el artefacto rector es suficiente.
7. **Verificación:** releer cada archivo modificado desde el commit resultante; comprobar SHA, coherencia cruzada, rama, PR y ausencia de cambios en main. No declarar persistido lo que no se ha verificado.
8. **Dictamen de paquete:** estado de cierre documental y lista corta de bloqueos residuales, dependencias y criterio objetivo de salida.

## 4. Regla de integridad: una iteración no obliga a fingir cierre

“Resolver en una sola iteración” significa completar la reconciliación y producir el mejor dictamen integrado posible, no garantizar que todos los componentes puedan cerrarse. Si faltan IAM, snapshots, asignación, material de servicio, Outcome/Value, soporte o evidencia, el paquete se resuelve registrando el bloqueo concreto, su impacto y el mínimo artefacto/dato necesario para levantarlo. No se sustituye la ausencia por supuestos inventados ni se convierte una propuesta en decisión aceptada.

Las preguntas al usuario se reservan para decisiones de diseño con alternativas científicamente distintas. La falta de evidencia no se convierte en pregunta de preferencia: se registra como límite verificable.

## 5. Dependencias y orden de trabajo

Orden operativo:
1. PA — C1 causal/población/Outcome/Value.
2. PB — D2 material y C2 primera etapa.
3. PC — C3 atribución y C4 mediación.
4. PD — DGP, C5 y evaluación.
5. PE — especificación técnica integrada e implementación autorizable.

Se permite descubrir dependencias cruzadas y corregir un paquete previo si un paquete posterior revela una contradicción material. No se exige terminar microtareas intermedias para avanzar dentro de un paquete. La dependencia entre paquetes no autoriza a reabrir decisiones aceptadas.

## 6. Criterios globales de salida

El cierre de los cinco paquetes debe dejar:
- estimandos, poblaciones, unidades, tratamientos/comparadores, outcomes, Value y horizontes definidos o limitados explícitamente;
- primera etapa y mediciones independientes de accesibilidad definidas;
- identificación, vías alternativas, mediación y no-identificación tratadas;
- DGP con verdad conocida y evidencia observada segregadas;
- contratos de evaluación y pruebas adversariales completos;
- especificación técnica trazable, reproducible y autorizable.

No equivale a ejecución, auditoría independiente ni evidencia empírica. Mantener `scientific_execution=false` y `execution_authorized=false` hasta autorización expresa conforme a gobernanza.

## 7. Estado inicial de aplicación

Este protocolo queda adoptado como método de trabajo para el cierre documental C10-S. El paquete activo siguiente es **PA**. La precedencia poblacional P*_{τ2}/P*_F ya está aceptada y no se vuelve a preguntar. El crosswalk IAM/C_SRC disponible informa ausencia de IAM y snapshots materiales; debe integrarse como bloqueo, no reiniciarse ni reconstruirse ficticiamente.



## 8. Estado tras el ciclo PA (2026-11-11)

PA ha completado su ciclo integral: `PA_RECONCILED_DOCUMENTALLY / C1_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN`. El resultado y los bloqueos están registrados en la reconciliación C1 §15, el plan §16.155 y la Closure Control Matrix. El siguiente paquete activo es **PB**. PA no se repite; solo se reabre para integrar material nuevo que levante bloqueos.
