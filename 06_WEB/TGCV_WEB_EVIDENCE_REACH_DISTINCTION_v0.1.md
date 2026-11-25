# TGCV — Evidence Brief: Distinguishing Accessible Transformations from Reach v0.1

**Identifier:** TGCV-WEB-EVIDENCE-REACH-001  
**Version:** 0.1  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — NOT APPROVED FOR PUBLICATION  
**Branch:** `strategy/tgcv-web-master`

# ESPAÑOL

## La pregunta

¿Un cambio en las transformaciones que están al alcance de un sistema implica necesariamente un cambio en los estados que ese sistema podría alcanzar?

La pregunta importa porque ambas cosas describen aspectos diferentes. Una transformación accesible es una posibilidad de cambio disponible bajo unas condiciones y restricciones determinadas. Reach, en cambio, se refiere al conjunto de estados que podrían obtenerse mediante transiciones admisibles. Que cambien las opciones disponibles no significa automáticamente que cambie el conjunto de estados alcanzables.

## Qué se ha investigado

En el ecosistema de paquetes de software Rust se realizaron análisis estructurales que compararon transformaciones accesibles y configuraciones sucesoras potenciales en versiones sucesivas de paquetes.

Un análisis inicial encontró patrones compatibles con una distinción informativa: había cambios en las transformaciones accesibles que no se correspondían de forma simple con cambios en la representación de sucesores, y también pares temporales con igual número de elementos pero distinta composición.

Sin embargo, una revisión metodológica posterior identificó una limitación decisiva en la construcción utilizada: los sucesores se derivaban directamente de las transformaciones accesibles. Por tanto, esa representación no constituía un grafo de estados sucesores construido de forma independiente. En esas condiciones, el análisis no permite establecer de manera válida que Reach sea empíricamente independiente de T_acc.

## Qué podemos afirmar hoy

La investigación ha definido una distinción conceptual y ha especificado qué tendría que demostrar una prueba empírica rigurosa:

- las transformaciones accesibles y los estados alcanzables deben construirse mediante procedimientos conceptualmente independientes;
- la pertenencia a Reach no puede definirse simplemente proyectando las transformaciones accesibles;
- las transiciones y los estados sucesores deben tener una semántica explícita y reproducible;
- la reconstrucción no puede depender de ejecuciones observadas, resultados futuros ni medidas de valor si el objeto investigado es la posibilidad estructural;
- los casos no reconstruibles deben permanecer como indeterminados, no convertirse silenciosamente en casos positivos o negativos.

La evidencia estructural anterior es útil para identificar problemas de representación y orientar el diseño. Pero, debido a la dependencia entre la construcción de sucesores y T_acc, no debe presentarse como demostración empírica independiente de la distinción entre T_acc y Reach.

## Qué sigue sin resolverse

Con los datos y la semántica estructural actualmente disponibles para este caso, todavía no se ha establecido una representación de estados sucesores que sea independiente de la construcción de T_acc y que permita probar la diferencia empírica entre ambos objetos.

Por ello, no se puede afirmar todavía que los cambios en las transformaciones accesibles causen cambios en Reach, ni que Reach añada información empírica independiente en esta operacionalización. Tampoco se han demostrado trayectorias realizadas, resultados, creación de valor ni una relación causal entre estos niveles.

## Qué permitiría avanzar

La siguiente investigación tendría que identificar una relación estructural de sucesión que pueda reconstruirse de manera independiente a partir de los datos disponibles, o concluir que el conjunto de datos no permite esa prueba sin cambiar el objeto empírico. Cualquier cambio de semántica requiere justificación explícita y revisión metodológica antes de una nueva ejecución.

Esta limitación no demuestra que la distinción conceptual sea falsa o redundante. Indica que la operacionalización empírica examinada hasta ahora no basta para resolverla.

## Interpretación

El resultado más importante de esta línea no es una confirmación de que T_acc y Reach sean empíricamente distintos en el ecosistema estudiado. Es una delimitación metodológica: para evaluar esa diferencia, Reach debe reconstruirse de manera independiente. La investigación mantiene abierta esa cuestión en lugar de presentar como evidencia concluyente un cálculo que no satisface ese requisito.

---

# ENGLISH

## The question

Does a change in the transformations available to a system necessarily imply a change in the states that the system could reach?

The question matters because these describe different aspects. An accessible transformation is an available possibility for change under specified conditions and constraints. Reach, by contrast, concerns the set of states that could be obtained through admissible transitions. Changes in available options do not automatically mean that the set of reachable states changes.

## What has been investigated

Structural analyses of the Rust software-package ecosystem compared accessible transformations and potential successor configurations across successive package versions.

An initial analysis found patterns compatible with an informational distinction: changes in accessible transformations did not map simply onto changes in the successor representation, and some temporal pairs had equal numbers of elements but different membership.

A subsequent methodological review, however, identified a decisive limitation in the construction used: successors were derived directly from accessible transformations. The representation therefore did not constitute an independently constructed graph of successor states. Under these conditions, the analysis cannot validly establish that Reach is empirically independent of T_acc.

## What can currently be said

The research has defined a conceptual distinction and specified what a rigorous empirical test would need to demonstrate:

- accessible transformations and reachable states must be constructed through conceptually independent procedures;
- Reach membership cannot simply be defined by projecting accessible transformations;
- transitions and successor states need explicit, reproducible semantics;
- reconstruction must not depend on observed executions, future outcomes or value measures when the object under study is structural possibility;
- cases that cannot be reconstructed must remain indeterminate rather than being silently recoded as positive or negative.

The earlier structural evidence is useful for identifying representation problems and informing design. However, because successor construction depended on T_acc, it should not be presented as independent empirical demonstration of the distinction between T_acc and Reach.

## What remains unresolved

With the structural data and semantics currently available for this case, an independently constructed representation of successor states has not yet been established in a form that can empirically test the difference between the two objects.

It is therefore not yet possible to claim that changes in accessible transformations cause changes in Reach, or that Reach adds independent empirical information under this operationalisation. Realised trajectories, outcomes, value creation and causal relationships across these levels have not been demonstrated either.

## What would allow progress

Further research would need to identify a successor relation that can be independently reconstructed from the available data, or conclude that this dataset cannot support the test without changing the empirical object. Any change in semantics requires explicit justification and methodological review before a new execution.

This limitation does not show that the conceptual distinction is false or redundant. It shows that the empirical operationalisation examined so far is insufficient to resolve it.

## Interpretation

The most important result of this line of work is not confirmation that T_acc and Reach are empirically distinct in the ecosystem studied. It is a methodological boundary: to evaluate that distinction, Reach must be reconstructed independently. The research keeps the question open rather than presenting a calculation that does not meet this requirement as conclusive evidence.

---

## Editorial and publication checks

Before publication:
1. Verify this summary against the current canonical semantic and methodological decisions.
2. Confirm that public references can be linked without exposing internal governance identifiers or controlled records.
3. Keep the unresolved status and the independence requirement visible wherever this brief is summarised.
4. Do not describe the earlier successor counts or non-redundancy figures as independent Reach evidence.
