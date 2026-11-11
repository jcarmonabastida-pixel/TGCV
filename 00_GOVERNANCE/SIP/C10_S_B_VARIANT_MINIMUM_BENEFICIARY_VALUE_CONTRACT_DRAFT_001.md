# C10-S — Contrato mínimo de beneficiario y Value para la variante B

**ID:** C10S-B-VALUE-MIN-001  
**Versión:** Draft 001  
**Estado:** DRAFT / PROPUESTA DOCUMENTAL / NO ACEPTADA / NO CONGELADA  
**Fecha:** 2026-11-11  
**Rama:** research/c10-s-consolidation-draft · **PR:** #116  
**Precedencia:** DEC-C10-095; P179/P182/P183; C-Value §224; contrato temporal/roles del DGP.  
**Ámbito:** extensión sintética B exclusivamente. No modifica la variante A, DEC-C10-068, el roster Opción A ni TGCV Core.

## 1. Propósito

Especificar las condiciones semánticas mínimas para que la variante B pueda contener Value contextual sin inferir beneficiarios desde el roster de A, sin introducir preferencias o dimensiones arbitrarias como si fueran hechos del dominio y sin incorporar la conclusión causal en la definición del resultado.

Este documento propone un contrato de admisibilidad y separación. No selecciona una identidad de beneficiario, tipo de entidad, relación concreta con el servicio, demanda, dimensión V_j, escala, regla de valoración ni parámetro del DGP. Esas elecciones permanecen OPEN y requieren aceptación posterior.

## 2. Principio rector

B puede estipular una **entidad sintética en rol de beneficiario**. "Sintética" significa que su existencia y propiedades forman parte de la verdad declarada del DGP; no significa que represente a usuarios reales ni que su perfil sea empíricamente validado.

No es necesario decidir ahora si la entidad es persona, organización, sistema software u otra unidad. Sí es necesario que la instancia de B, cuando se especifique, determine de forma inequívoca:
- qué entidad/unidad recibe la consecuencia relevante;
- qué relación basal la vincula al servicio lógico;
- qué demanda, necesidad u objetivo existe antes de la asignación;
- qué consecuencia puede experimentar;
- desde qué perspectiva se valora esa consecuencia;
- qué regla fija transforma la consecuencia medida en uno o más resultados V_j.

La mera etiqueta "beneficiario" no satisface estos requisitos.

## 3. Separación de unidades y roles

Deben conservarse, al menos, las siguientes identidades lógicas, aunque una especificación futura pueda justificar relaciones 1:1 o 1:N:

| Objeto/rol | Función | No implica |
|---|---|---|
| Unidad experimental/asignación | Recibe Z conforme al diseño | Ser beneficiaria o usuaria |
| Unidad lógica de servicio | Instancia C10S-SVC-REQUEST-PROCESSOR | Ser propietaria, consumidora o beneficiaria |
| Beneficiario sintético | Entidad cuya situación/consecuencia se valora | Instalar, operar o ejecutar la transformación |
| Actor ejecutor/operador | Realiza un evento del proceso si el DGP lo estipula | Ser beneficiario o valorador |
| Evaluador independiente | Adjudica medición y compara salida con truth | Ser actor del servicio o beneficiario |

La relación entre unidad experimental, unidad lógica de servicio y beneficiario debe declararse explícitamente. No se hereda de CMP.owner, CMP-SERVICE-LOGIC-001, LOGICAL_SERVICE_UNIT ni del campo temporal actor.

## 4. Contrato mínimo de beneficiario (B-BEN)

Una instancia de B no será admisible para análisis confirmatorio de Value hasta que registre ex ante:

| Campo mínimo | Requisito | Estado actual |
|---|---|---|
| beneficiary_id / versión | Identidad sintética estable y versionada | OPEN |
| beneficiary_type | Clase de entidad, sin presuponer persona/organización/sistema | OPEN |
| service_relation | Relación explícita con la unidad lógica de servicio | OPEN |
| experimental_unit_relation | Relación con unidad experimental y asignación | OPEN |
| eligibility_preZ | Regla basal de inclusión, determinada antes de Z | OPEN |
| demand_preZ | Demanda/necesidad/objetivo basal definido antes de Z, incluida su ausencia | OPEN |
| consequence_domain | Tipo de consecuencia que podría experimentar | OPEN |
| valuation_perspective | Desde quién/qué perspectiva se juzga la consecuencia | OPEN |
| valuation_authority | Regla o mandato que legitima esa perspectiva en el mundo sintético | OPEN |
| population_and_horizon | Población objetivo y horizonte temporal | OPEN |
| multiplicity | Cardinalidad beneficiario↔unidad de servicio↔unidad experimental | OPEN |
| provenance | Fuente de estipulación, versión y hash del contrato | OPEN |

Los campos son requisitos de una futura instancia, no entidades ni variables materializadas en la instancia actual.

### 4.1 Demanda pre-Z

La demanda debe ser basal y anterior a Z. Debe distinguirse, según proceda, entre:
- existencia de necesidad/demanda;
- intensidad o prioridad;
- elegibilidad para recibir el servicio;
- conocimiento o consideración de una posibilidad;
- selección e inicio posteriores.

Demanda no equivale a selección, ejecución, éxito técnico ni valoración. No se define retrospectivamente por haber utilizado el servicio. La demanda no atendida debe seguir siendo representable; no puede desaparecer del denominador por no ejecución.

No se fija una distribución, escala ni mecanismo de generación de demanda en este documento.

### 4.2 Beneficiario no equivale a evaluador

La perspectiva de valoración puede ser estipulada por el propio DGP como regla del mundo sintético y aplicada por un evaluador separado. El evaluador no se convierte por ello en beneficiario. Si existen varias perspectivas o beneficiarios, sus resultados no se agregan sin una regla explícita y justificada.

## 5. Contrato mínimo de Value (B-VAL)

Para cada dimensión futura V_j, la instancia B deberá definir una ficha independiente conforme a §224:

1. constructo y significado contextual;
2. beneficiario/perspectiva a la que corresponde;
3. consecuencia valorada y su relación con la demanda basal;
4. criterio de valoración y dirección favorable/desfavorable;
5. evidencia y fuente de datos;
6. unidad, escala, cálculo y baseline;
7. horizonte/ventana temporal;
8. regla de adjudicación y tratamiento de casos limítrofes;
9. validez, fiabilidad, error y acuerdo interevaluador (P182);
10. ausencia, no aplicabilidad, censura, disputa y desconocimiento (P183);
11. cegamiento, independencia y provenance;
12. trade-offs con otras dimensiones.

La estructura vectorial P179 se conserva durante identificación. No se selecciona ninguna de las cinco dimensiones históricas por defecto; no se exige que las cinco sean instanciadas. Tampoco se reduce a V1 por conveniencia. No se define escalar, ponderación ni regla compensatoria en esta propuesta.

## 6. Independencia causal y prohibición de circularidad

La definición de V_j no puede contener como argumento directo la variable cuya contribución causal se pretende estimar de forma que el resultado sea verdadero por construcción.

En particular:
- V_j no puede definirse como función de ΔT_acc, Reach, número de transformaciones accesibles, selección o ejecución, salvo que una de esas cantidades sea explícitamente el constructo de valoración y la afirmación causal se reformule en consecuencia;
- V_j no puede ser una recodificación de O-CONF ni de otro Outcome técnico;
- V_j no puede definirse por "haber completado con éxito" sin una consecuencia para el beneficiario diferenciada del criterio técnico;
- la demanda/eligibilidad no puede depender de Z ni de estados postratamiento;
- el evaluador debe aplicar la misma regla de valoración en ambos brazos y no conocer la asignación cuando sea viable.

La separación no exige independencia estadística entre A, O y V. Exige distinción conceptual, temporal, de medición y de adjudicación.

## 7. DAG causal candidato y vías alternativas

Cadena mediada candidata:

Z → B/provisión → W_attempt → S_install/C_dep → A_f* / ΔT_acc → Reach_H / posibilidades → selección/ejecución → consecuencia para beneficiario → V_j

La demanda basal y la relación beneficiario-servicio se representan antes de Z y pueden modificar elegibilidad, exposición, selección o efecto; no son consecuencias de Z.

Deben existir escenarios adversariales separados para:
- vía directa de la política/paquete a V_j (p. ej. coste, riesgo, demora o calidad no mediada por A_f);
- efecto de B sobre consecuencia/Value a través de un componente distinto de accesibilidad;
- ausencia de demanda basal;
- demanda existente pero posibilidad no conocida/no considerada/no seleccionada;
- selección o ejecución postratamiento;
- consecuencias discordantes entre dimensiones V_j;
- medición imperfecta, ausencia/censura y pérdida diferencial.

Si existe una vía directa B→V_j o B→consecuencia no mediada por A_f, el ITT de Z sigue siendo un efecto de política/paquete, pero no identifica automáticamente el efecto focal de accesibilidad. Se mantiene el firewall Generator/Analyzer/Evaluator: la verdad y los potenciales solo son accesibles al Generator/Evaluator.

Este DAG es candidato semántico; no se declara reconciliado ni aprobado.

## 8. Estimandos: separación obligatoria

La especificación futura debe adjudicar por separado:
- ITT de Z sobre cada V_j;
- efecto de política/paquete sobre cada V_j;
- efecto focal de accesibilidad sobre cada V_j, solo si se justifican exclusión, consistencia/versiones, soporte, medición e interferencia;
- efectos mediados por accesibilidad, con supuestos adicionales explícitos;
- LATE por dimensión, solo bajo los supuestos IV aplicables y para su población local;
- efecto agregado, solo si existe regla de agregación aceptada.

No se hereda identificación de ITT sobre Outcome a Value, ni de una dimensión V_j a otra. El resultado puede ser NO IDENTIFIED / INDETERMINATE.

## 9. Invariantes de admisibilidad propuestos

| ID | Invariante | Criterio de aceptación futuro |
|---|---|---|
| BVAL-01 | Beneficiario explícito | Identidad sintética, tipo, versión y relación con servicio/unidad declarados |
| BVAL-02 | Basalidad | Elegibilidad y demanda definidas antes de Z |
| BVAL-03 | Demanda no es uso | Demanda se conserva aunque no haya selección/ejecución |
| BVAL-04 | Perspectiva | Perspectiva y autoridad de valoración estipuladas ex ante |
| BVAL-05 | Consecuencia distinta | Consecuencia para beneficiario no es sinónimo de A, Reach, ejecución u Outcome técnico |
| BVAL-06 | Regla estable | Mismo criterio de valoración entre brazos y versiones comparables |
| BVAL-07 | No circularidad | V_j no incorpora mecánicamente ΔT_acc ni la hipótesis causal |
| BVAL-08 | Dimensionalidad | Vector y trade-offs preservados; no se fuerzan dimensiones ni pesos |
| BVAL-09 | Tiempo | Baseline, ventana y horizonte fijados antes de observar resultados |
| BVAL-10 | Ausencia | No observado/no aplicable/censurado/desconocido/disputado no se codifica como cero |
| BVAL-11 | Vías alternativas | DAG distingue efecto focal de efecto de paquete |
| BVAL-12 | Información | Generator/Analyzer/Evaluator separados; truth oculta al Analyzer |
| BVAL-13 | Medición | Ficha §224 completa; controles P182/P183 aplicables |
| BVAL-14 | Provenance | Regla, fuente, versión, datos y adjudicación trazables |

## 10. Consecuencias para paquetes C/D/E

### C — C-Value
C debe cerrar semánticamente el rol de beneficiario, relación basal, demanda, perspectiva, consecuencia y criterio antes de seleccionar dimensiones/indicadores. No debe convertir este contrato de requisitos en una identidad concreta por defecto. Las fichas V_j §224 se completan solo después de decisiones contextuales explícitas.

### D — Contrato computacional
D recibe un contrato versionado con cardinalidades, temporalidad, relaciones y estados de ausencia explícitos. Debe representar por separado verdad del DGP, observaciones entregadas al Analyzer y adjudicación del Evaluator. No crear aún nombres de columnas, tablas, tipos físicos, fixtures ni parámetros; el contrato semántico debe cerrarse primero.

### E — Aceptación integrada
E debe verificar invariantes BVAL-01…14, P179/P182/P183, estimandos por dimensión y escenarios adversariales. Debe aceptar la abstención/no identificación correcta, no premiar una estimación positiva forzada. No puede declarar validez externa a partir de B.

## 11. Preguntas abiertas que requieren decisión explícita

1. ¿Qué clase de entidad sintética se estipulará como beneficiaria (persona, organización, sistema u otra)?
2. ¿Cuál será su relación cardinal con la unidad experimental y con la unidad lógica de servicio?
3. ¿Qué demanda/objetivo basal tendrá y cómo se medirá o estipulará sin depender de Z?
4. ¿Qué consecuencia independiente de A/O técnico puede experimentar?
5. ¿Qué perspectiva y autoridad de valoración regirán en el mundo sintético?
6. ¿Qué dimensión o dimensiones V_j están justificadas por esa consecuencia?
7. ¿Qué horizonte, regla de adjudicación y mecanismo de ausencia se usarán?
8. ¿Qué vías alternativas se incluirán para discriminar efecto focal de efecto de paquete?

Ninguna pregunta se resuelve por analogía con el microdominio A. Ninguna opción se presume aceptada.

## 12. Dictamen

**CONTRATO MÍNIMO DE ADMISIBILIDAD PROPUESTO — SEMÁNTICA PARCIALMENTE CERRADA, INSTANCIA B NO ESPECIFICADA.**

Se fija qué debe existir para que Value contextual sea admisible, sin inventar quién es el beneficiario ni qué valora. La siguiente decisión no es elegir un número o una función de utilidad; es seleccionar y justificar el tipo de entidad y su relación con el servicio y la unidad experimental. Solo después se podrá formular demanda, consecuencia y perspectiva sin circularidad.

**Estado:** A/B architecture accepted (DEC-C10-095); B-BEN/B-VAL contract DRAFT; beneficiary instance OPEN; dimensions/indicators OPEN; DGP parameters OPEN; MED-02/MED-03 OPEN; no Design Freeze, implementation, fixtures, simulation or scientific execution.  
scientific_execution=false  
execution_authorized=false

## 13. B1 — Entidad solicitante sintética aceptada como tipo candidato (2026-11-11)

Se acepta B1 como tipo candidato para desarrollo, no como instancia B cerrada. La entidad solicitante-beneficiaria es una entidad lógica sintética con necesidad/objetivo pre-Z, relación explícita con C10S-SVC-REQUEST-PROCESSOR, posibilidad de originar solicitud y consecuencia posterior valorable desde perspectiva ex ante. Solicitante y beneficiario pueden coincidir por estipulación explícita en B1, nunca por inferencia sobre A. Se distinguen necesidad/demanda, solicitud, procesamiento técnico y consecuencia para entidad. Procesamiento correcto/O-CONF no equivale a Value; solicitud enviada no demuestra satisfacción; no solicitud/no ejecución no implica demanda ausente ni Value=0. Se mantienen OPEN instancia, cardinalidad, demanda, consecuencia operacional, perspectiva, dimensiones, medición, DAG y estimandos. Véase C10S-B1-REQUESTER-CANDIDATE-001.
