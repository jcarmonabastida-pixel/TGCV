# C10-S — B1: adjudicación pre-Z de Need_preZ y reconciliación de consecuencias

**ID:** C10-S-B1-PREZ-ADJUDICATION-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-11  
**Estado:** FUNCTIONAL_WORKING_CONTRACT_ACCEPTED / PREZ_RULES_DEFINED_DOCUMENTALLY / UNIT_TRUTH_AND_EVIDENCE_MATERIAL_OPEN / CONSEQUENCE_STRUCTURE_RECONCILED / NO_VJ_SELECTED / NOT_DESIGN_FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Autoridad y precedencia:** DEC-C10-095/096/097; DEC-C10-068/069; aceptación del propósito basal B1; aceptación de la especialización funcional mínima (§14 de `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`); contratos B1/UE, oportunidad estandarizada, DGP temporal/roles, B2–B3, PC, P179/P182/P183 y §224.

## 1. Objeto y alcance

Este paquete integra en una sola especificación documental la definición de trabajo de `Need_preZ`, su adjudicación 1/0/? y la estructura de consecuencias potenciales para B1, después de la aceptación de la especialización funcional mínima del servicio.

No reabre decisiones aceptadas de B1/UE, servicio lógico por UE, oportunidad estandarizada, D2, población primaria candidata `P*_{τ2}`, separación ITT/primeras etapas/LATE ni DEC-C10-068. No elige dimensiones V_j, indicadores, escalas, instrumentos, pesos, autoridad de valoración, horizonte, parámetros ni reglas estadísticas. No crea roster material ni verdad por unidad.

## 2. Función de servicio de referencia aceptada como contrato de trabajo

La instancia lógica de servicio recibe solicitudes dirigidas a ella. Su función mínima de trabajo es comprobar el estado declarativo de habilitación en destino y admitir solicitudes cuando `PAR-SVC-ENABLED=true`; cuando no está habilitado, no las admite. Expone el perfil declarado por `PAR-SVC-PROFILE`.

Límites:
- STANDARD y READ_ONLY son perfiles compatibles con ENABLED=true según RUL-SVC-ENABLE-PROFILE-01. No se asigna semántica de negocio diferenciada entre ellos.
- La exposición del perfil no implica capacidades, permisos efectivos ni resultado de procesamiento.
- La admisión/no admisión es un evento distinto de procesamiento, respuesta, ejecución, conformidad F*/O-CONF, consecuencia B1 y Value.
- El contrato no especifica el contenido de la solicitud ni el procesamiento posterior.
- Esta aceptación especializa el contrato de DEC-C10-068 como contrato de trabajo; no crea una regla constitutiva nueva ni prueba implementación.

## 3. Definición funcional de trabajo de Need_preZ

> Antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

`Need_preZ` representa la existencia de ese objetivo para B1 antes de la asignación experimental. Se refiere al propósito basal de B1, no al éxito técnico ni a que una solicitud haya ocurrido.

La formulación:
- puede estructurar el constructo y su truth pre-Z;
- no convierte automáticamente a toda UE en `Need_preZ=1`;
- no implica que el objetivo sea exclusivo, urgente o prioritario frente a otros objetivos;
- no define el contenido de las solicitudes ni la operación posterior a la admisión;
- no convierte la oportunidad estandarizada en demanda natural;
- no es un criterio de inclusión ITT ni un filtro postratamiento.

La verdad de Need debe vincularse a B1 y a la instancia/versionado del servicio pertinente, con ancla temporal anterior a Z. La unidad B1/UE conserva cardinalidad aceptada de una B1 por UE.

## 4. Regla de verdad y adjudicación 1/0/?

Se mantienen dos objetos que nunca se sustituyen entre sí:

- **`truth_dgp(Need_preZ)`:** estado estipulado por la definición del DGP para la unidad B1/UE antes de Z.
- **`observed_evidence(Need_preZ)`:** evidencia accesible al procedimiento de adjudicación, con provenance y cobertura, sin acceso indebido a la truth oculta.

### 4.1 Truth del DGP

| Estado | Regla |
|---|---|
| `1` | La especificación basal versionada del DGP establece que B1 tiene el objetivo funcional definido en §3 antes de Z. |
| `0` | La especificación basal versionada establece afirmativamente que B1 no tiene ese objetivo en el universo cerrado del DGP. |
| `?` | La truth no está determinada, el DGP no permite resolverla o la especificación basal contiene indeterminación explícita. |

La ausencia de registro, la ausencia de solicitud, la no admisión, la falta de procesamiento, la ausencia de respuesta o la falta de evidencia observada no constituyen por sí mismas truth=0.

### 4.2 Adjudicación de evidencia observada

El adjudicador asigna:
- **Observed 1:** existe evidencia afirmativa admisible, temporalmente pre-Z y vinculada sin ambigüedad a B1/UE y a la versión de servicio/configuración relevante, que respalda el objetivo basal.
- **Observed 0:** existe evidencia afirmativa admisible y suficiente de que el objetivo no forma parte de la especificación basal de esa unidad, dentro de un universo documental/declarativo cerrado y con cobertura demostrada.
- **Observed ?:** evidencia ausente, incompleta, contradictoria, no versionada, temporalmente ambigua, de alcance incierto o insuficiente para decidir.

No basta una búsqueda sin resultados para adjudicar 0: antes debe demostrarse que el universo de fuentes consultado es cerrado, completo y pertinente para esa unidad y periodo. Si no se demuestra cobertura, corresponde ?. Una contradicción no resuelta también produce ? y se conserva el conflicto.

### 4.3 Admisibilidad mínima de evidencia

Toda evidencia usada para adjudicar debe permitir comprobar, según corresponda:
1. identidad y relación B1–UE–servicio;
2. fecha/orden temporal inequívocamente anterior a Z;
3. versión del objetivo/contrato y de la instancia lógica relevante;
4. fuente, autoría/rol, integridad y provenance;
5. alcance de la afirmación y cobertura de las fuentes;
6. correspondencia semántica con el objetivo definido en §3;
7. ausencia de contaminación por eventos o información post-Z.

Esta lista define criterios documentales de admisibilidad, no un schema físico ni un inventario de fuentes ya disponible. No hay actualmente roster por UE ni evidencia IAM/snapshot material suficiente para efectuar la adjudicación de unidades.

## 5. No circularidad, elegibilidad y población ITT

La verdad y adjudicación de Need se fijan antes de Z. Está prohibido inferir o recodificar Need a partir de:
- asignación, política D2, programación, provisión, instalación o rollback;
- C_dep*, A_f*, D_f*, ΔT_acc*, Reach o existencia de ruta;
- oportunidad estandarizada post-snapshot;
- Request_attempt, received, admitted, processing o response;
- F*, O-CONF, selección, ejecución o consecuencia observada.

`E_req_preZ`, elegibilidad experimental, demanda de recursos, Need_preZ y Request_event son constructos distintos. Need_preZ no sustituye la composición de `E_i`, `App*(τ2,S0)`, `C_dep,0` o `A_f,0*`.

La población ITT primaria candidata `P*_{τ2}` no se condiciona a Need=1 ni a solicitud/admisión/procesamiento post-Z. La regla poblacional final de Value, si difiere, deberá justificarse ex ante y por resultado; no se establece aquí. Los estados 0 y ? se conservan para controles negativos, análisis de heterogeneidad, límites o sensibilidad cuando el diseño lo justifique. No se excluyen automáticamente.

## 6. Consecuencias potenciales para B1

El objeto inmediato de consecuencia es el cambio posterior en la situación de B1 respecto de su objetivo basal: si puede contar con la función de servicio que pretende mantener disponible. La consecuencia no se define por un evento técnico aislado.

La estructura analítica deberá permitir, sin seleccionar variables ni dimensiones, al menos:
1. **Disponibilidad funcional:** la capacidad de admisión está disponible o no en el entorno de destino.
2. **Continuidad:** la función se mantiene, se interrumpe o se degrada.
3. **Demora/oportunidad:** la función está disponible tarde o se pierde una oportunidad de uso.
4. **Recuperación:** se requiere o no intervención adicional para restablecer la disponibilidad funcional.
5. **Riesgo/reversibilidad:** exposición a interrupción/fallo y posibilidad de recuperar el estado funcional previo.

Estas clases son una envolvente de consecuencias, no un roster exhaustivo, una escala, un outcome compuesto ni V_j. Su especificación empírica requiere todavía ancla temporal, horizonte, fuentes, adjudicación y relación con la oportunidad estandarizada.

### 6.1 Diferencia entre Need y consecuencia

- Need=1 no implica que la función esté interrumpida: puede existir el objetivo y estar satisfecha basalmente.
- Need=0 no autoriza inferir beneficio por admisión o éxito técnico; pueden existir efectos adversos o consecuencias colaterales para B1.
- Need=? mantiene indeterminada la referencia basal; la consecuencia/valoración no debe forzarse a una categoría que presuponga Need=1 o 0.

La existencia del objetivo es pre-Z; el estado de la función y sus consecuencias se observan o estipulan post-Z. No se define retrospectivamente Need por el resultado observado.

## 7. Separación de eventos y constructos

| Objeto | Qué representa | No demuestra por sí solo |
|---|---|---|
| Configuración declarativa ENABLED/PROFILE | Estado lógico declarado en destino | Admisión efectiva ni función mantenida |
| Request_attempt/received | Intento o recepción de solicitud | Need, admisión ni beneficio |
| Request_admitted | Decisión/evento de admisión | Procesamiento completado o respuesta |
| Processing | Proceso posterior de la solicitud | Resultado correcto ni consecuencia B1 |
| Response | Respuesta del servicio | Satisfacción del objetivo basal |
| F*/O-CONF | Conformidad técnica según contrato y adjudicación | Consecuencia B1 o Value |
| Beneficiary_consequence | Cambio en la situación de B1 respecto del objetivo basal | Valoración normativa completa |
| V_j | Valoración de una consecuencia con regla ex ante | No se define todavía ninguna V_j |

La oportunidad estandarizada es un probe común para comparar el servicio. No es demanda natural ni evidencia suficiente de que B1 necesitara una solicitud concreta. La falta de petición natural no cambia Need_preZ.

## 8. Consecuencias causales y pruebas de no circularidad

El DGP debe permitir que la política D2 afecte la consecuencia B1 por más de una vía: accesibilidad/Reach, disponibilidad/admisión del servicio, rutas alternativas y efectos colaterales. Por tanto:
- ITT sobre consecuencia/Value, cuando sea admisible, conserva interpretación de efecto total de política/paquete;
- no identifica automáticamente el efecto de ΔT_acc*;
- el éxito técnico puede coexistir con consecuencia nula o adversa;
- una ruta alternativa puede preservar la función sin abrir la ruta focal;
- ΔT_acc* puede cambiar sin modificar admisión ni consecuencia;
- la admisión puede ocurrir sin procesamiento satisfactorio ni beneficio para B1.

Estas son condiciones de diseño/adversariales; no son resultados empíricos ni pruebas ejecutadas. PC y P183 deberán determinar qué estimandos por consecuencia son identificables y bajo qué supuestos.

## 9. Qué queda resuelto y qué permanece abierto

| Elemento | Dictamen |
|---|---|
| Propósito basal B1 | Aceptado |
| Especialización mínima del servicio (admitir según ENABLED y exponer PROFILE) | Aceptada como contrato funcional de trabajo |
| Need_preZ semántico | Definido a nivel funcional de trabajo |
| Regla conceptual truth 1/0/? | Definida |
| Regla documental observed 1/0/? | Definida |
| Requisitos de evidencia/provenance/cobertura pre-Z | Definidos documentalmente |
| Truth por UE / roster | OPEN — sin materialización |
| Evidencia observada por UE y cobertura | OPEN — IAM/snapshots/artefactos no disponibles |
| Semántica diferenciada STANDARD/READ_ONLY | OPEN |
| Contenido y procesamiento posterior de solicitudes | OPEN |
| Consecuencia B1 | Estructura reconciliada; instancia y medida OPEN |
| Autoridad normativa de valoración | OPEN |
| Horizonte, ventana y ancla temporal | OPEN |
| Dimensiones V_j, escalas, instrumentos, pesos | NO SELECCIONAN |
| C1–C4 por Value | No identificados/evaluables en el estado material actual |

## 10. Dictamen y siguiente dependencia

**Dictamen:** `B1_PREZ_RULES_DEFINED_DOCUMENTALLY / UNIT_LEVEL_TRUTH_AND_OBSERVED_ADJUDICATION_MATERIAL_BLOCKED / CONSEQUENCE_STRUCTURE_RECONCILED / VALUE_NOT_OPERATIONALIZED`.

Se ha cerrado la arquitectura documental de Need_preZ y la estructura de adjudicación, no la clasificación material de unidades ni una instancia confirmatoria completa. El siguiente paso útil, sin reabrir el contrato funcional, es un crosswalk de fuentes pre-Z disponibles por B1/UE que permita determinar si hay evidencia admisible y cobertura cerrada. Si no existe material autorizado, el resultado debe seguir siendo ?/BLOCKED; no se fabrican filas ni snapshots. En paralelo, puede detallarse la semántica de perfiles o procesamiento solo si se demuestra que es necesaria para definir el objetivo basal, no para adornar el DGP.

No se seleccionan dimensiones de Value ni se establece horizonte. No se autoriza roster material, schema físico, fixtures, captura/materialización, implementación, generación de datos, simulación, estimación, Design Freeze o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## 11. Resultado de la auditoría material de fuentes pre-Z (2026-11-11)

El inventario y dictamen de cobertura se documentan en `C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md`. Ese artefacto distingue documentos de diseño, truth del DGP, evidencia observada pre-Z y evidencia técnica del servicio/configuración.

La revisión confirma que los documentos existentes respaldan el contrato conceptual y las reglas de adjudicación, pero no constituyen evidencia observada por unidad. No se localizó roster material B1/UE, declaración basal individual, vínculo material B1–UE–service_instance, snapshot IAM/configuración pre-Z, expediente de evidencia poblado ni evaluación E1/E2. La plantilla U_G y el registro de cobertura permanecen vacíos; la cobertura efectiva de estas dimensiones es NONE.

Por tanto, no se adjudica ninguna unidad ni se genera roster. Con el material revisado, observed Need_preZ=1 y 0 no son sostenibles; el resultado procedimental sería ?/BLOCKED. Truth DGP permanece NOT MATERIALIZED. Este resultado no implica que no existan fuentes fuera del conjunto C10-S revisado.

La auditoría no altera la definición funcional aceptada, no selecciona dimensiones de Value y no autoriza materialización, captura, implementación o ejecución.
