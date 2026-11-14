# C10-S — Contrato de alcanzabilidad y propagación de indeterminación en trayectorias
**ID:** C10-S-REACH-001 · **Versión:** Draft 001 · **Corte:** 2026-11-04  
**Estado:** PROPUESTA METODOLÓGICA / NO APROBADA / NO CONGELADA.  
**Ámbito:** Bloque 3 — Reach_possible, composición de rutas, horizonte y trayectorias candidatas.  
**No autoriza:** implementación, simulación, ejecución ni freeze.

## 1. Reconstrucción histórica y brecha

Se revisaron README.md y 00_GOVERNANCE/README.md en main, la regla de reconstrucción histórica, maestro C10-S §§43.2–43.6, 47–49, 58, 63–67 y 71–72, el contrato DGP y los contratos SNAP e ID.

La base ya distingue T_acc, Reach_H, trayectorias candidatas, selección y ejecución; accesibilidad A_f*, aplicabilidad App_f, conocimiento/consideración; snapshot estructural y evidencia E_T; identidad TID/SID/RID/EID; y verdad DGP oculta frente a clasificación observada 1/0/?.

La brecha concreta es cómo propagar esos estados por secuencias compuestas, cuándo afirmar alcanzabilidad/no alcanzabilidad/indeterminación, cómo tratar cobertura incompleta y cómo impedir que la enumeración use selección, ejecución, Outcome o Value para definir accesibilidad o alcanzabilidad.

## 2. Objetos y notación

Para unidad i, estado inicial s0, snapshot estructural S_T*(t), frontera b, contexto c y horizonte H:

- T_acc*(i,t): transformaciones estructuralmente accesibles.
- App*(τ,s,t): aplicabilidad de τ desde estado s.
- Rel*(τj,τj+1,s,t): relación válida de composición/transición.
- Π_H*: conjunto verdadero de secuencias admisibles dentro de H.
- Reach_H*(s0): conjunto de estados alcanzables desde s0 mediante alguna secuencia admisible.
- Π_H^cand,obs: trayectorias que el enumerador observa/clasifica como candidatas.
- Reach_H,obs: alcanzabilidad clasificada por el procedimiento observacional.
- Π_H^sel y Π_H^exec: trayectoria seleccionada y trayectoria/transformaciones ejecutadas; variables downstream.

Reach_possible se reserva para alcanzabilidad estructural posible bajo snapshot, condiciones y horizonte definidos, sin exigir selección o ejecución. Se recomienda usar Reach_H* para la verdad del DGP y Reach_H,obs para la clasificación observada. No usar Reach_possible como etiqueta indiferenciada.

## 3. Definición estructural de trayectoria admisible

Una trayectoria candidata es una secuencia ordenada π=(s0,τ1,s1,…,τk,sk), k≥0. Es admisible dentro de H si se cumplen conjuntamente:

1. Identidad: cada τj tiene TID y SID/RID aplicables determinados o mapping válido durante el tramo.
2. Accesibilidad: τj pertenece a T_acc* para unidad, frontera, contexto y tiempo.
3. Aplicabilidad: App*(τj,sj−1,tj)=1 desde el estado resultante de los pasos previos. Aplicabilidad permite recorrer la ruta, pero no define la accesibilidad global.
4. Composición: relación entre pasos definida y satisfecha; salida de τj compatible con entrada/precondiciones de τj+1.
5. Condiciones/recursos: autorización, recursos, dependencias, restricciones, bloqueos y ventanas temporales compatibles.
6. Temporalidad: orden factible dentro de H, con duraciones, precedencias, caducidad y disponibilidad.
7. Consistencia de estado: cada sj deriva de la postcondición contractual de τj, nunca de Outcome o Value.
8. Frontera y granularidad: objetos dentro del universo/catálogo G declarado o mapping válido.

Una trayectoria de longitud cero conserva s0 como alcanzable solo si se preespecifica reflexividad; no cuenta como transformación ejecutada. No se exige selección, inicio o ejecución.

## 4. Lógica de composición 1/0/?

Se propone lógica trivalente fuerte de Kleene: 1 respaldado, 0 refutado, ? indeterminado. No se asignan probabilidades a ?.

### 4.1 Conjunción dentro de una ruta
Una ruta es 1 si todos sus predicados constitutivos están respaldados como 1; 0 si al menos un predicado necesario está respaldado como 0; ? si ninguno está respaldado como 0 y al menos uno es ?. Un bloqueo confirmado refuta esa ruta específica. Un componente desconocido no se convierte en fallo.

### 4.2 Disyunción entre rutas alternativas
Para un estado objetivo s:
- Reach_H,obs(s)=1 si existe al menos una ruta completa clasificada 1.
- Reach_H,obs(s)=0 solo si todas las rutas posibles dentro del universo, frontera, catálogo, G y H están exhaustivamente enumeradas y refutadas, o se demuestra que no existe ruta.
- Reach_H,obs(s)=? si no hay ruta confirmada y queda alguna ruta indeterminada, o la cobertura no permite descartar rutas omitidas.

Una ruta confirmada basta para establecer alcanzabilidad aunque otras sean ?. Para afirmar no alcanzabilidad se requiere exhaustividad: ausencia de rutas confirmadas no basta.

### 4.3 Propagación secuencial
Si un paso es 0, la ruta queda bloqueada desde ese punto. Si un paso es ?, los estados posteriores dependientes no se promueven a 1; permanecen ? salvo refutación independiente. No se propaga una salida hipotética como estado confirmado.

Registrar primer predicado bloqueante, predicados desconocidos y su posición, dependencias entre pasos, rutas alternativas y motivos de exclusión del universo.

## 5. Conjuntos alcanzables y límites lógicos

Se proponen:
- Reach_H^-: estados con al menos una trayectoria completamente confirmada.
- Reach_H^+: estados con al menos una trayectoria no refutada (confirmada o indeterminada) dentro del universo y reglas declarados.
- Reach_H^? = Reach_H^+ \ Reach_H^-: estados posibles pero no confirmados.

Reach_H^- está contenido en Reach_H^+. Estos límites son lógicos, no intervalos de confianza ni probabilidades. Un estado fuera de Reach_H^+ solo puede declararse no alcanzable si universo y cobertura son exhaustivos. Si la cobertura no es completa, el complemento es indeterminado/fuera de cobertura.

## 6. Horizonte H, recursos y estado dinámico

H se fija antes de Z y antes de observar Outcome/Value. Debe especificar unidad temporal/origen, duración máxima, ventanas por transformación, duraciones/precedencias, concurrencia, caducidad de autorización/recursos/dependencias, ciclos/repeticiones, profundidad máxima, criterio de terminación, granularidad G y eventos que generan snapshots.

No se recorta H ni profundidad después de observar qué rutas producen mejores resultados. Un límite computacional debe distinguir truncamiento de ausencia real de ruta: una búsqueda truncada no autoriza Reach=0.

Los recursos compartidos se asignan temporalmente; no se cuentan simultáneamente rutas incompatibles que consumen el mismo recurso limitante. El nivel y momento de disponibilidad deben declararse. El consumo posterior en ejecución no redefine retrospectivamente accesibilidad basal.

Los ciclos requieren regla explícita de terminación/visita. Sin ella, enumeración finita no puede demostrar no alcanzabilidad.

## 7. Identidad, snapshots y cambios durante H

Cada tramo referencia TID/SID/RID y snapshot vigente. Continuidad de identidad semántica no implica continuidad de accesibilidad o aplicabilidad.

- Cambio RID/SID con TID estable: registrar versión y reevaluar compatibilidad/condiciones.
- Cambio de TID: aplicar contrato ID; no tratarlo como mismo paso sin mapping adjudicado.
- Mapping ?: tramo y trayectorias dependientes quedan ?.
- Cambio estructural dentro de H: snapshot nuevo e inmutable; evaluar por tramos temporales.
- Cambio de E_T no es cambio estructural.
- Descubrir post una ruta preexistente no fecha su creación en ese momento: actualizar la clasificación epistémica basal preservando cuándo se descubrió.

Declarar si el estimando pregunta por alcanzabilidad con snapshot t0 congelado, evolución temporal hasta tH o contrafactual bajo política. Son objetos distintos.

## 8. Distinciones obligatorias

| Objeto | Pregunta | No significa |
|---|---|---|
| T_acc* | Qué transformaciones son estructuralmente accesibles | Que sean aplicables desde S0 o ejecutadas |
| App*(τ,s,t) | Si τ puede aplicarse desde estado/tiempo | Que τ no sea accesible en otros estados |
| Reach_H* | Si existe secuencia admisible que alcanza s en H | Que alguien la conozca, elija o ejecute |
| Π_H^cand,obs | Qué rutas identifica el enumerador | Cobertura completa de rutas verdaderas |
| Π_H^sel | Qué ruta se selecciona | Que sea la única accesible |
| Π_H^exec | Qué se ejecuta realmente | Prueba retrospectiva de accesibilidad basal |
| Outcome/Value | Resultado y valoración | Criterio definitorio de T_acc o Reach |

Reach_H* puede cambiar por ΔT_acc, aplicabilidad, relaciones, recursos, restricciones, identidad, contexto u horizonte. No se asume ΔT_acc≠0 implica ΔReach_H≠0, ni ΔReach_H≠0 implica D_f*=1. Una transformación nueva puede no ser aplicable desde S0 o no conducir a estado nuevo dentro de H.

## 9. Observación, cobertura y no-identificación

E_T declara universo de estados y transformaciones, cobertura de catálogo/relaciones/condiciones/alternativas, cobertura de rutas compuestas/profundidad, cobertura temporal/recursos, versiones de snapshots/matching/enumerador, fuentes y adjudicación, límites/truncamientos y rutas no examinadas.

Códigos de salida:
- REACH_CONFIRMED (1): existe ruta confirmada.
- REACH_REFUTED (0): no existe ruta y búsqueda/universo es exhaustivo.
- REACH_INDETERMINATE (?): no hay confirmación y no se puede descartar ruta.
- REACH_OUT_OF_SCOPE: objetivo fuera de frontera/universo.
- REACH_NOT_COMPARABLE: snapshots, identidad o granularidad incompatibles.

Declarar no-identificación si el catálogo/universo no está cerrado; falta cobertura basal para distinguir ruta nueva de ruta descubierta; mapping de identidades/split/merge no se resuelve; horizonte/profundidad está truncado; predicados críticos son desconocidos/contradictorios; cambio de snapshot no está temporalmente localizado; o no se distingue acceso de aplicabilidad desde estado actual.

No convertir un juicio lógico 1/0/? en probabilidad de Reach sin modelo estadístico, calibración y estimando explícitos.

## 10. Relación con C_dep, A_f*, D_f*, ΔT_acc y Value

1. C_dep es estado de dependencia técnica; no demuestra por sí solo A_f*.
2. A_f* es accesibilidad de τ2; no demuestra App* desde S0.
3. D_f* es apertura focal basal→post bajo identidad/snapshots comparables; no representa ΔT_acc completo.
4. ΔT_acc* describe cambio estructural; no garantiza que nueva ruta alcance estado dentro de H.
5. Reach_H* deriva de accesibilidad, aplicabilidad, relaciones, condiciones, estado inicial y horizonte.
6. Selección/ejecución son downstream; no construyen Reach_H*.
7. Outcome/Value no definen admisibilidad de rutas.

El contrato define medición/propagación; no identifica por sí mismo los efectos causales de accesibilidad, Reach o Value.

## 11. Contratos adversariales propuestos

| ID | Caso | Salida exigida |
|---|---|---|
| REACH-01 | Ruta completa confirmada; otras rutas ? | Reach=1 |
| REACH-02 | Sin ruta confirmada; una ruta potencial tiene predicado ? | Reach=? |
| REACH-03 | Rutas enumeradas fallan, catálogo incompleto | Reach=?, no 0 |
| REACH-04 | Todas las rutas refutadas y cobertura exhaustiva | Reach=0 |
| REACH-05 | Transformación accesible pero no aplicable desde S0 | T_acc=1; esa ruta no alcanza s |
| REACH-06 | Ruta válida no seleccionada | Reach=1; selección=0 no altera Reach |
| REACH-07 | Ruta válida nunca ejecutada | Reach=1; Exec=0 |
| REACH-08 | Ejecución observada sin snapshot basal suficiente | No reconstruir accesibilidad basal |
| REACH-09 | Ruta con paso 0 y otro ? | Ruta=0 por paso necesario refutado |
| REACH-10 | Ruta con recurso ? y resto 1 | Ruta=? |
| REACH-11 | Dos rutas alternativas, una confirmada y otra ? | Reach=1 |
| REACH-12 | Búsqueda truncada | No declarar Reach=0 |
| REACH-13 | Evidencia descubre ruta ya existente en t0 | ΔE_T; no ADD estructural en t1 |
| REACH-14 | RID/SID cambia, TID estable, compatibilidad no probada | Ruta=? |
| REACH-15 | Mapping 1:N sin composición validada | Ruta=? / NOT_COMPARABLE |
| REACH-16 | Ciclo sin regla de terminación | Enumeración incompleta; no declarar no alcanzabilidad |
| REACH-17 | Recurso compartido en rutas incompatibles | No contar rutas simultáneas como factibles |
| REACH-18 | Outcome/Value alto en una ruta | No alterar Reach |
| REACH-19 | τ2 cambia de identidad entre tiempos | D_f* no comparable como misma identidad |
| REACH-20 | ΔT_acc cambia fuera de rutas hacia s | ΔT_acc≠0 puede coexistir con Reach(s) inalterado |

Son contratos de diseño. No hay fixtures ejecutables ni pruebas realizadas.

## 12. Dictamen y pendientes

**Avance:** se formaliza composición, lógica 1/0/? y criterio asimétrico: una ruta confirmada basta para afirmar alcanzabilidad; no alcanzabilidad exige cobertura exhaustiva. Se protege la separación entre accesibilidad, aplicabilidad, alcanzabilidad, candidaturas, selección y ejecución.

**No cerrado:** faltan catálogo finito DGP, estados/objetivos, G, H, duraciones, reglas por clase, ciclos, recursos, snapshots dentro de H, cobertura y oráculos. También falta decidir si el objetivo primario usa snapshot basal congelado o evolución dinámica. AUD-005 y AUD-007 permanecen abiertos.

Criterios de cierre:
1. fijar estado inicial, objetivos y universo;
2. fijar G, H, ciclos y temporalidad;
3. definir relaciones y reglas composicionales;
4. inventariar recursos, autorizaciones, bloqueos y alternativas;
5. decidir snapshot congelado/dinámico;
6. especificar serialización de ruta y estados 1/0/?;
7. construir fixtures/oráculos REACH-01…20;
8. validar errores de cobertura, enumeración y clasificación;
9. revisión independiente;
10. decisión formal.

No hay freeze, implementación, simulación, ejecución ni autorización empírica.
