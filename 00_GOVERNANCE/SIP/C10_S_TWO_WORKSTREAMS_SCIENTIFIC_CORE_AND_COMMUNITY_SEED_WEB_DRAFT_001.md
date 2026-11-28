# C10-S — Dos líneas de trabajo: cierre científico y web germen comunitaria con playground TGCV

**ID:** C10-S-WORKSTREAMS-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** DRAFT / ORIENTACIÓN DE PLANIFICACIÓN / NO APROBADO COMO CIERRE CIENTÍFICO  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116

## 1. Propósito

Registrar las dos líneas de trabajo planteadas para TGCV, desde la consideración de que el investigador está solo en esta fase hasta la concepción de una web germen que abra TGCV *as is* a la comunidad. Las líneas son complementarias: C10-S produce la especificación y evidencia científica; la web facilita comprensión, crítica, colaboración y posible evolución. El playground será una proyección interactiva de los mismos contratos, no un modelo paralelo.

Este documento registra orientación de planificación. No aprueba hipótesis, estimandos, DGP, intervención, microdominio, implementación, experimento, claims ni lanzamiento público.

## 2. Contexto: investigador único

En esta fase el proyecto está siendo desarrollado por una sola persona. Por ello:
- La falta de revisores externos no debe bloquear la continuación del diseño y la consolidación documental.
- Se realizará una auditoría interna estructurada, crítica y trazable.
- Toda revisión asistida por ChatGPT se declarará **AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT**. No equivale a revisión por pares ni validación externa.
- La revisión independiente se difiere al momento en que aporte valor real: antes de congelar artefactos técnicos que lo requieran y/o antes de publicar afirmaciones de reproducibilidad o validación.
- No se elevará el estado de un artefacto por haber sido autoauditado.

## 3. Línea A — Científica troncal: C10-S

### Propósito y pregunta

Cerrar el diseño del experimento sintético C10-S para evaluar si la contribución causal de los cambios en transformaciones accesibles puede identificarse y separarse de otros efectos de la intervención. Deben distinguirse: (1) efecto total de intervención/política; (2) contribución atribuible al cambio de accesibilidad; y (3) efectos residuales o vías alternativas. El ITT de una política de provisión no demuestra por sí mismo un efecto mediado por A_f* o ΔT_acc.

### Microdominio

El microdominio previsto es la migración de configuración entre dos entornos software. Su selección y operacionalización definitivas siguen sujetas a los gates C10-S. No se inventariarán componentes, dependencias ni parámetros no observados.

### Prioridades

- Resolver la intervención autónoma sobre accesibilidad, relación entre Z, B, políticas, condiciones constitutivas y vías directas/colaterales.
- Cerrar jerarquía de estimandos, comparador, población y horizonte, separando TE, ITT, efectos bajo políticas de accesibilidad y cualquier IV/LATE condicionado a sus supuestos.
- Completar DGP extremo a extremo, ecuaciones, roles, reloj temporal, escenarios adversariales/nulos y protección de la verdad generativa.
- Diferenciar accesibilidad verdadera/observada, ΔT_acc, aplicabilidad, Reach, consideración, selección, inicio, ejecución, Outcome y Value.
- Completar validez de constructo, medición independiente, error de clasificación, cegamiento, no circularidad y adjudicación.
- Resolver frontera, granularidad, cobertura, dependencias y rutas alternativas; ausencia de evidencia no equivale a evidencia de ausencia.
- Formalizar identificación, falsadores, sensibilidad, soporte, heterogeneidad y límites.
- Justificar tamaño muestral, réplicas, potencia/precisión y criterios interpretativos antes de resultados.
- Auditar contratos sin confundir especificaciones documentales con pruebas ejecutadas.

### Revisión interna y externa

Para U_G y otros artefactos, la autoauditoría registrará por control PASS_STATIC, CONDITIONAL, FAIL o NOT_ASSESSED, con fundamento, versión, alcance y acción pendiente. No se marcarán como superados controles que requieran parser, constraints, motor, seguridad, inspección técnica o validación empírica. El paquete SR-01…20 seguirá siendo la especificación de revisión externa, pero su revisión independiente queda diferida. La autoauditoría puede detectar contradicciones; no acredita independencia ni validez empírica.

## 4. Línea B — Web germen TGCV y playground

### Propósito: apertura pública *as is*

La web no será el escaparate de un producto terminado ni la presentación de una teoría ya validada. Será una web germen que muestre TGCV en su estado real de desarrollo para que la comunidad pueda conocerlo, examinarlo, cuestionarlo y decidir si merece la oportunidad de crecer y evolucionar.

### Contenidos públicos propuestos

- **TGCV hoy:** propósito, motivación, alcance, arquitectura conceptual y vocabulario.
- **Estado de desarrollo:** qué está definido, propuesto, implementado, ejecutado, auditado, aceptado o abierto.
- **Hipótesis y programa experimental:** preguntas, estimandos, diseños, predicciones y condiciones de falsación.
- **Evidencias y resultados:** materiales trazables, métodos, versiones, resultados negativos/inconclusos y límites.
- **Cuestiones abiertas:** incertidumbres, supuestos, alternativas, debilidades y decisiones pendientes.
- **Agenda de investigación:** experimentos, replicaciones, extensiones y aplicaciones candidatas.
- **Participación comunitaria:** canales y reglas para objeciones, propuestas, contribuciones y discusión.
- **Gobernanza:** versiones, procedencia, autoría, decisiones e historial.

La comunicación distinguirá arquitectura conceptual, hipótesis, diseño, resultado técnico, evidencia empírica y claim científico. No presentará un diseño como resultado ni una demo como validación causal.

### Playground interactivo: capacidades candidatas

El playground podría ser una de las primeras herramientas de la web. De forma visual e intuitiva permitiría explorar escenarios modelados y recorrer la cadena TGCV. Capacidades candidatas:
- Cargar escenarios de un sistema y sus dos entornos/configuraciones.
- Visualizar estados, componentes, dependencias, restricciones, compatibilidades y condiciones.
- Examinar snapshots y diferencias.
- Visualizar transformaciones accesibles y relaciones, diferenciándolas de estados del sistema.
- Explorar rutas alternativas, bloqueos, dependencias e incertidumbres.
- Recorrer Reach, trayectorias candidatas, selección y ejecución.
- Comparar intervenciones, escenarios y contrafactuales.
- Observar Outcome y valoración contextual de Value, haciendo explícitos observador, contexto, criterio, regla y justificación.
- Mostrar, cuando el diseño lo permita, efecto total, contribución atribuible a accesibilidad y residuo.
- Modificar supuestos y condiciones del escenario y comparar consecuencias modeladas.
- Exponer estados indeterminados y límites, sin ocultarlos.

La lista no es un alcance aprobado. La interacción debe subordinarse a la exactitud semántica y la trazabilidad.

### Coherencia científica

El playground debe respetar los contratos, variables y distinciones semánticas de TGCV/C10-S, pero no se presupone que el motor experimental sintético sea suficiente como motor operativo completo. Podrá reutilizar componentes compatibles del núcleo y requerir una capa operativa diferenciada para escenarios más desarrollados, simulación interactiva y exploración de trayectorias. No debe crear definiciones semánticas contradictorias ni presentar una demo como evidencia causal. Debe mantener las distinciones entre sistema/estado y espacio transformacional; accesibilidad/aplicabilidad/Reach/selección/ejecución; estados 1/0/?; snapshots, identidad, versiones y dependencias; Outcome y Value. Cada elemento visual debe corresponder a una definición y versión identificables.

El playground mostrará consecuencias de escenarios modelados: la visualización no demuestra que el modelo sea verdadero ni acredita causalidad en sistemas reales.

### Desarrollo diferido

La web y el playground no deben retrasar el cierre científico ni convertirse ahora en una línea de implementación. En esta fase se registra la visión y se preservan requisitos de coherencia; no se inicia diseño visual detallado ni desarrollo web. El microdominio software podrá reutilizarse si finalmente es adecuado. La apertura inicial no requiere necesariamente que el playground esté terminado.

## 5. Apertura comunitaria y revisión externa futura

La revisión externa no se concibe como certificación académica previa para legitimar TGCV. Se busca preparar una apertura pública honesta y suficientemente rigurosa para que la comunidad decida si desea examinar, criticar, replicar o desarrollar la propuesta.

### Antes de abrir la web

Revisión de preparación y transparencia, proporcionada a lo que se publique:
1. **Accesibilidad intelectual:** comprensión sin depender de conversaciones privadas.
2. **Coherencia:** terminología, conceptos y documentos consistentes.
3. **Trazabilidad:** procedencia y versión de definiciones, decisiones, hipótesis y evidencias.
4. **Estados explícitos:** definido/propuesto/implementado/ejecutado/auditado/aceptado/abierto.
5. **Falsabilidad:** predicciones y condiciones de refutación identificables.
6. **Criticabilidad:** debilidades, supuestos, alternativas e incertidumbres expuestos.
7. **Honestidad probatoria:** no confundir demo, simulación, ejecución técnica y evidencia empírica.
8. **Seguridad, privacidad, licencias, atribución y protección de datos/secretos.**
9. **Reproducibilidad:** claridad sobre qué puede reproducirse y qué no.

Esta revisión no equivale a revisión por pares de la teoría ni a validación científica global.

### Después de abrir la web

La comunidad podrá aportar crítica científica/metodológica, discutir supuestos y alternativas, replicar experimentos cuando sea posible, proponer escenarios y extensiones, contribuir técnica/documentalmente y registrar objeciones, respuestas y desacuerdos. Las aportaciones se incorporarán mediante gobernanza versionada, preservando procedencia, autoría, revisión y decisiones. Publicar una contribución no significa que esté aceptada.

La revisión externa deberá declarar experiencia, participación previa, conflictos de interés, alcance y acceso a materiales. La independencia se juzgará respecto del objeto revisado. No se exige designar revisores ahora. Antes de abrir se determinará la revisión mínima proporcionada a los materiales y claims que efectivamente se publiquen.

## 6. Secuencia y dependencias

| Fase | Línea científica | Web germen / playground |
|---|---|---|
| Actual | Auditoría interna y cierre causal/documental C10-S | Registrar visión y requisitos; sin implementación |
| Preparación científica | DGP, identificación, medición, sensibilidad y dimensionamiento | Identificar materiales publicables y su estado real |
| Preparación de apertura | Auditar claims, trazabilidad, límites y materiales | Arquitectura de información y mecanismos comunitarios |
| Apertura germen | Mantener C10-S trazable y revisable | Publicar TGCV *as is*, con límites y agenda abierta |
| Evolución | Evaluar nuevas pruebas bajo gobernanza | Recibir crítica, colaboración y contribuciones |
| Playground | Contratos científicos como fuente normativa | Desarrollar visualización interactiva derivada de esos contratos |

La apertura no exige que TGCV esté científicamente cerrado, pero sí que el alcance de las afirmaciones públicas corresponda a la evidencia disponible. El playground puede llegar después.

## 7. Orientaciones registradas

- Dos líneas complementarias: C10-S científico troncal y web germen/playground posterior.
- La falta de revisores externos no bloquea el trabajo documental actual; autoauditoría asistida declarada no independiente.
- La web muestra TGCV *as is*, con límites, incertidumbres y agenda abierta; no lo presenta como teoría validada o producto terminado.
- La comunidad puede criticar, replicar, proponer y contribuir; la aceptación requiere trazabilidad y gobernanza.
- El playground será una proyección interactiva de los mismos contratos y escenarios, no un modelo paralelo ni evidencia causal.
- La revisión externa tendrá una fase de preparación antes de la apertura y otra de crítica/replicación/evolución posterior.
- Prioridad inmediata: C10-S. No se inicia ahora la implementación de web/playground.

Estas orientaciones no modifican TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims científicos, autorización de ejecución ni decisiones experimentales.

## 8. Próximos pasos

1. Continuar auditoría interna estructurada U_G.
2. Reconciliar sus resultados con plantilla, protocolo, maestro, matriz de cierre y plan.
3. Completar DGP y arquitectura causal, incluida la intervención autónoma sobre accesibilidad y separación de vías.
4. Cerrar medición/validez, identificación, falsación, sensibilidad y dimensionamiento.
5. Mantener este documento como referencia para planificar la web germen.
6. Antes de abrir, preparar paquete de publicación *as is* y protocolo comunitario.

## 9. Estado y límites

C10-S sigue Draft, no aprobado, no congelado y no ejecutado. La auditoría interna U_G está pendiente; SR-01…20 no han recibido revisión independiente. No hay inventario técnico real ni cobertura demostrada. D1/D2, arquitectura B, parámetros y DGP final no están aprobados. Web y playground no están implementados; no existe todavía comunidad ni proceso comunitario operativo. No se declara validación científica, causal, empírica, predictiva o externa.

**Principio rector:** cerrar C10-S con rigor sin bloquear el trabajo por la ausencia actual de revisores externos y preparar una apertura pública honesta de TGCV *as is* para que la comunidad pueda decidir si merece desarrollarse, cuestionarse y evolucionar.
