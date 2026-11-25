# TGCV — Evidence Brief: Changes in a Software Ecosystem v0.1

**Identifier:** TGCV-WEB-EVIDENCE-SOFTWARE-001  
**Version:** 0.1  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — NOT APPROVED FOR PUBLICATION  
**Branch:** `strategy/tgcv-web-master`

> This brief translates a bounded structural empirical result into a public-facing account. It does not replace the scientific record, publish the underlying dataset, or authorise release of controlled source material. The scope and caveats below are integral to the finding.

# ESPAÑOL

## Qué se quería investigar

¿Cambian con el tiempo las transformaciones que están al alcance de los componentes de un sistema de software? Y, si cambian, ¿esos cambios son analíticamente distinguibles de los cambios en los estados que podrían alcanzarse mediante esas transformaciones?

Para examinar estas preguntas se estudió un ecosistema real de paquetes de software construidos con Rust. El análisis se centró en las relaciones entre paquetes y sus dependencias declaradas a través de versiones sucesivas.

## Sistema y datos

El estudio utilizó una instantánea histórica de datos del ecosistema Rust que contiene información estructural sobre paquetes, versiones, fechas de publicación y declaraciones de dependencias. La instantánea comprende:

- 91.437 paquetes;
- 607.498 versiones;
- 3.618.523 declaraciones de dependencias.

La unidad temporal comparada fue el par de versiones consecutivas de un mismo paquete focal. Se reconstruyeron 516.061 pares temporales. No se identificaron exclusiones por empates en las marcas temporales dentro de la población analizada.

La fuente de datos es una instantánea histórica, no una descarga actualizada en tiempo real. El archivo completo se conserva fuera del repositorio de código; el registro científico mantiene su identidad, procedencia e integridad mediante metadatos y huellas criptográficas.

## Cómo se definieron las transformaciones accesibles

El análisis construyó una representación operacional de las transformaciones relacionadas con las dependencias que satisfacían una regla de admisibilidad definida previamente. La misma identidad de transformación se siguió entre los dos momentos comparados.

La accesibilidad se reconstruyó a partir de información estructural disponible en el momento correspondiente. El procedimiento no utilizó la aparición posterior de una versión objetivo como criterio para decidir retrospectivamente que una transformación era accesible. Tampoco utilizó ejecución de Cargo, actividad futura, resultados posteriores ni medidas de valor para construir la representación estructural.

El análisis comparó la pertenencia de las transformaciones a los conjuntos accesibles en ambos momentos. De ese modo pudo distinguir persistencia, incorporación, desaparición y reconfiguración de posibilidades.

## Qué se observó

En los 516.061 pares temporales reconstruidos:

| Tipo de cambio | Pares |
|---|---:|
| Persistencia de la estructura accesible | 77.858 |
| Expansión | 8.295 |
| Contracción | 3.786 |
| Reconfiguración | 426.122 |
| **Total** | **516.061** |

En conjunto, 438.203 pares (aproximadamente el 84,91 %) presentaron algún cambio en la pertenencia o composición del conjunto de transformaciones accesibles. La persistencia se observó en los 77.858 pares restantes.

El resultado muestra que, bajo la representación y las reglas fijadas para este estudio, la estructura de transformaciones accesibles no permaneció constante entre versiones consecutivas de muchos paquetes. El cambio más frecuente fue la reconfiguración: la composición de las posibilidades cambió, sin que eso tuviera que significar simplemente que el conjunto aumentara.

## ¿Son esos cambios lo mismo que cambiar los estados alcanzables?

No. La investigación examinó por separado representaciones de sucesores potenciales de un paso. Sin embargo, una revisión metodológica posterior determinó que la construcción utilizada derivaba los sucesores directamente de las transformaciones accesibles. Por tanto, esa representación no era un grafo de estados sucesores construido de manera independiente.

Los análisis anteriores habían producido comparaciones entre conjuntos de transformaciones accesibles y conjuntos de sucesores construidos, incluidos casos con igual cardinalidad y distinta composición. Pero, al depender la construcción de sucesores de T_acc, esas comparaciones no constituyen una prueba empírica independiente de que Reach aporte información distinta de T_acc.

La distinción conceptual sigue siendo relevante, pero su contraste empírico requiere una relación de sucesión independiente, con estados iniciales, transiciones admisibles y sucesores definidos sin proyectar simplemente T_acc. Esa condición no se ha satisfecho todavía para esta operacionalización del ecosistema Rust.

## Qué permite afirmar el estudio

Dentro del ecosistema, los datos, la población temporal y las reglas operacionales examinadas, el estudio aporta evidencia empírica estructural de que:

1. la composición de las transformaciones accesibles puede cambiar entre estados sucesivos de un sistema de software real;
2. esos cambios pueden incluir persistencia, expansión, contracción y reconfiguración;
3. la reconstrucción de transformaciones accesibles puede realizarse a gran escala con controles de integridad y sin utilizar ejecución, resultados futuros ni medidas de valor.

El análisis también permitió identificar una limitación metodológica importante: la construcción de sucesores potenciales utilizada en una fase posterior dependía directamente de T_acc. Por ello, no proporciona una prueba independiente de la distinción empírica entre T_acc y Reach.

## Qué no permite afirmar

El estudio no demuestra:

- que cada dependencia declarada corresponda, en cualquier contexto, a una transformación significativa para todos los propósitos;
- que la representación reconstruya toda la semántica histórica de Rust o de Cargo;
- que todos los sucesores potenciales sean configuraciones que Cargo seleccionaría o que pudieran ejecutarse;
- que los cambios de accesibilidad causen cambios en Reach o en trayectorias posteriores;
- que se produzcan mejores resultados, adopción, éxito o valor;
- que el resultado se generalice a otros ecosistemas o dominios;
- que TGCV sea una teoría universal, superior u ontológicamente irreducible.

El análisis de alcance se limitó a un paso. No establece suficiencia de trayectorias a horizontes mayores ni resultados de ejecución observada.

## Limitaciones y lectura adecuada

La conclusión depende de una definición operacional concreta de transformación y accesibilidad, de una instantánea histórica y de una regla temporal específica. Una parte de las evaluaciones de versiones objetivo quedó fuera del análisis porque no podía interpretarse con seguridad mediante la gramática de versiones fijada. Esas exclusiones son casos no resueltos, no evidencia de inaccesibilidad.

Por ello, el resultado debe leerse como evidencia estructural acotada, no como una demostración completa del comportamiento del ecosistema ni como validación general del programa TGCV.

## Relación con la investigación TGCV

Este estudio contribuye a examinar dos distinciones centrales: que las posibilidades accesibles pueden cambiar con el tiempo y que ese cambio no es idéntico al cambio en los estados potencialmente alcanzables. No resuelve por sí mismo las preguntas posteriores sobre trayectorias, resultados, causalidad o valor.

La siguiente etapa de investigación requiere diseños capaces de examinar esas relaciones sin definir la accesibilidad a partir de los resultados que se pretende explicar.

---

# ENGLISH

## What the study set out to investigate

Do the transformations available to components of a software system change over time? And, when they do, are those changes analytically distinguishable from changes in the states that might be reached through those transformations?

To examine these questions, the study analysed a real ecosystem of software packages built with Rust. It focused on relationships between packages and their declared dependencies across successive versions.

## System and data

The study used a historical snapshot of the Rust ecosystem containing structural information about packages, versions, release dates and dependency declarations. The snapshot covered:

- 91,437 packages;
- 607,498 versions;
- 3,618,523 dependency declarations.

The temporal unit of comparison was a pair of consecutive versions of the same focal package. The analysis reconstructed 516,061 temporal pairs. No timestamp-tie exclusions were identified within the analysed population.

The data source is a historical snapshot, not a live or continuously updated feed. The full archive is retained outside the code repository; the scientific record preserves its identity, provenance and integrity through metadata and cryptographic hashes.

## How accessible transformations were defined

The analysis constructed an operational representation of dependency-related transformations that satisfied a pre-specified admissibility rule. The same transformation identity was followed across the two compared time points.

Accessibility was reconstructed from structural information available at the relevant time. The procedure did not use the later appearance of a target version to decide retrospectively that a transformation had been accessible. Nor did it use Cargo execution, future activity, subsequent outcomes or value measures to construct the structural representation.

The analysis compared membership of transformations in the accessible sets at both time points. This made it possible to distinguish persistence, additions, removals and reconfiguration of possibilities.

## What was observed

Across the 516,061 reconstructed temporal pairs:

| Type of change | Pairs |
|---|---:|
| Persistence of the accessible structure | 77,858 |
| Expansion | 8,295 |
| Contraction | 3,786 |
| Reconfiguration | 426,122 |
| **Total** | **516,061** |

Overall, 438,203 pairs (approximately 84.91%) showed some change in the membership or composition of the accessible-transformation set. Persistence was observed in the remaining 77,858 pairs.

Under the representation and rules fixed for this study, the structure of accessible transformations did not remain constant between successive versions of many packages. Reconfiguration was the most frequent form of change: the composition of possibilities changed, without necessarily meaning that the set simply grew.

## Are these changes the same as changes in reachable states?

No. The research separately examined representations of one-step potential successors. However, a subsequent methodological review determined that the construction used derived successors directly from accessible transformations. The representation was therefore not an independently constructed graph of successor states.

Earlier analyses had compared accessible-transformation sets with constructed successor sets, including cases with equal cardinality but different membership. Because successor construction depended on T_acc, those comparisons do not provide an independent empirical test that Reach contains information distinct from T_acc.

The conceptual distinction remains relevant, but its empirical assessment requires an independent successor relation, with initial states, admissible transitions and successors defined without simply projecting T_acc. That condition has not yet been met for this Rust ecosystem operationalisation.

## What the study supports

Within the ecosystem, data, temporal population and operational rules examined, the study provides structural empirical evidence that:

1. the composition of accessible transformations can change between successive states of a real software system;
2. such changes can include persistence, expansion, contraction and reconfiguration;
3. accessible transformations can be reconstructed at scale with integrity controls and without using execution, future outcomes or value measures.

The analysis also identified an important methodological limitation: the potential-successor construction used in a later phase depended directly on T_acc. It therefore does not provide an independent empirical test of the distinction between T_acc and Reach.

## What the study does not support

The study does not demonstrate:

- that every declared dependency is, in every context, a meaningful transformation for all analytical purposes;
- that the representation reconstructs the complete historical semantics of Rust or Cargo;
- that every potential successor is a configuration Cargo would select or that could be executed;
- that accessibility changes cause changes in Reach or subsequent trajectories;
- that better outcomes, adoption, success or value follow;
- that the result generalises to other ecosystems or domains;
- that TGCV is a universal, superior or ontologically irreducible theory.

The reachability analysis was limited to one step. It does not establish trajectory sufficiency over longer horizons or observed execution outcomes.

## Limitations and appropriate interpretation

The conclusion depends on a specific operational definition of transformation and accessibility, a historical snapshot and a defined temporal rule. Some target-version evaluations were excluded because they could not be interpreted safely under the frozen version grammar. These exclusions are unresolved cases, not evidence of inaccessibility.

The result should therefore be read as bounded structural evidence, not as a complete demonstration of ecosystem behaviour or general validation of the TGCV programme.

## How this contributes to TGCV research

This study helps examine two central distinctions: accessible possibilities can change over time, and such change is not identical to change in potentially reachable states. It does not, by itself, resolve subsequent questions about trajectories, outcomes, causality or value.

Further research requires designs capable of examining those relationships without defining accessibility from the outcomes they are intended to explain.

---

## Editorial and publication checks

Before publication:
1. Verify the numerical summary against the final canonical evidence records and current claim matrix.
2. Confirm that the public description of the historical dataset and its provenance is permitted; do not publish the archive or restricted raw data.
3. Confirm whether the method description can be accompanied by a public protocol or reproducibility package.
4. Add stable links to the public scientific method and evidence records only after release permissions and destinations are confirmed.
5. Keep the limitations and non-claims visible wherever this brief is summarised.
