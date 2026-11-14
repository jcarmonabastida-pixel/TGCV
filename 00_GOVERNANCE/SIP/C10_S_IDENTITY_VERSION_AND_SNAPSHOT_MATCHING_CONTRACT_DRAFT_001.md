# C10-S — Contrato de identidad, versionado y correspondencia de snapshots
**ID:** C10-S-ID-MATCH-001 · **Versión:** Draft 001 · **Corte:** 2026-11-04  
**Estado:** PROPUESTA OPERACIONAL / NO APROBADA / NO CONGELADA.  
**Ámbito:** Bloque 3 — identidad semántica, versiones, granularidad, matching y diff de snapshots.  
**No autoriza:** implementación, simulación, ejecución ni freeze.

## 1. Reconstrucción histórica y alcance de la intervención

Se aplicó la regla de reconstrucción histórica de GitHub antes de crear el contrato. Se revisaron README.md y 00_GOVERNANCE/README.md en main; la regla HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1; maestro C10-S §§43, 47–48, 57–58, 63–64 y 70–71; y el contrato de snapshots C10-S-SNAP-DELTA-001.

Lo ya definido y reutilizable:
- el objeto transformacional se registra con identidad canónica y versión;
- U_acc contiene identidades/versiones; R_acc contiene relaciones tipadas/dirigidas; C_acc contiene condiciones/configuraciones;
- snapshots solo se comparan con frontera, granularidad, catálogo y reglas compatibles;
- un hash distinto no prueba por sí solo identidad semántica nueva;
- identidad semántica distinta requiere alta/baja; mapping no resuelto produce ?;
- el histórico no debe sobrescribirse y la observación no debe recibir truth del DGP.

Brecha real: no existía un contrato completo que determinara cómo asignar IDs, separar definición semántica de versión de implementación/configuración, evaluar continuidad, resolver correspondencias 1:1/1:N/N:1, alinear granularidad y emitir eventos diff sin forzar equivalencias.

Este documento concreta esa brecha. No crea una ontología general TGCV ni modifica el Core.

## 2. Niveles de identidad que no deben colapsarse

Se proponen cuatro niveles:

| Nivel | Símbolo | Qué identifica | Ejemplo abstracto |
|---|---|---|---|
| Tipo/definición semántica de transformación | TID | Qué transformación es, por su contrato semántico | reconfigurar un sistema de S0 a S1 bajo condiciones declaradas |
| Especificación contractual | SID | Una definición formal versionada del contrato de TID | pre/postcondiciones, restricciones y tolerancias de una revisión |
| Realización técnica | RID | Implementación, módulo o dependencia que realiza la especificación | artefacto/software/configuración concreta |
| Instancia/evento de transformación | EID | Una aplicación o intento concreto sobre una unidad y tiempo | invocación de τ2 en unidad i durante t |

La misma TID puede tener varias SID/RID y muchos EID. Un cambio de RID no implica automáticamente nueva TID. Una nueva EID no crea nueva identidad semántica. Si cambia la función/contrato esencial, debe evaluarse una nueva TID o una relación explícita de sucesión.

Para el espacio transformacional:
- U_acc referencia TID y registra SID/RID aplicables, estado y condiciones de acceso.
- R_acc identifica relaciones entre TID (dependencia, composición, habilitación, incompatibilidad, precedencia, interfaz, alternativa, etc.).
- C_acc identifica condiciones/configuraciones asociadas al uso realizable.
- E_T conserva evidencia, provenance y referencias a artefactos; no se usa como verdad estructural.

## 3. Esquema de identificadores

Se propone que los IDs sean opacos, persistentes y no codifiquen atributos mutables:

- `tr:<namespace>:<opaque-id>` para TID;
- `sp:<namespace>:<opaque-id>` para SID;
- `impl:<namespace>:<opaque-id>` para RID;
- `rel:<namespace>:<opaque-id>` para identidad de relación;
- `cond:<namespace>:<opaque-id>` para condición;
- `evt:<namespace>:<opaque-id>` para evento EID.

Los prefijos son ilustrativos del tipo de objeto; el identificador interno no codifica nombre, versión, estado, brazo, resultado ni fecha. No se reutilizan IDs retirados. Un alias nunca sustituye ni borra el ID canónico.

Cada registro mínimo contiene:
1. ID y tipo;
2. estado de ciclo de vida (propuesto, activo, retirado, reemplazado, disputado);
3. definición/contrato legible y hash de su contenido;
4. versión de especificación, implementación y configuración, por separado;
5. dominio, frontera, granularidad y unidad/contexto de aplicabilidad;
6. entradas, salidas, precondiciones, postcondiciones, restricciones y tolerancias;
7. relaciones/dependencias relevantes;
8. vigencia temporal (valid-time) y registro de cuándo se incorporó al repositorio (record-time);
9. provenance, fuente y decisión/adjudicación que autorizó el alta o cambio;
10. enlaces a snapshots y evidencia sin incrustar truth del DGP en el canal del analizador.

El hash detecta integridad del contenido exacto; no determina identidad semántica.

## 4. Firma semántica y regla de continuidad

Para evaluar si una nueva revisión conserva TID, se compara una firma semántica preespecificada:

`Sig(T) = (Purpose, InputDomain, OutputDomain, CoreOperation, Preconditions, Postconditions, Invariants, Constraints, FailureSemantics)`.

No todos los campos tienen que ser idénticos palabra por palabra, pero todo cambio debe clasificarse y justificarse. Se proponen tres dictámenes:

### 4.1 Continuidad semántica (mismo TID)

Se conserva TID cuando:
- el propósito y la operación nuclear permanecen;
- entradas/salidas mantienen equivalencia contractual dentro de tolerancias preestablecidas;
- las pre/postcondiciones esenciales y los invariantes no cambian de modo que altere qué transformación se está definiendo;
- el cambio es de implementación, optimización, corrección interna o parametrización dentro del contrato;
- el mapping de versiones queda respaldado por evidencia y adjudicación.

Puede cambiar la accesibilidad por nueva compatibilidad, recursos, autorización, dependencias, latencia u operación aunque TID se conserve. La continuidad semántica no implica equivalencia de accesibilidad, calidad, coste, riesgo ni resultados.

### 4.2 Nueva identidad (nuevo TID)

Se crea nueva TID cuando cambia materialmente:
- el propósito/función;
- el tipo de entradas o salidas de forma no equivalente;
- la operación nuclear o mecanismo que define la transformación;
- precondiciones/postcondiciones esenciales;
- invariantes, restricciones de seguridad o semántica de fallo que alteran la clase de transformación.

La identidad anterior no se borra: se registra retirada o vigencia final y relación tipada con la nueva (sucede_a, deriva_de, reemplaza, alternativa_de), según evidencia.

### 4.3 Indeterminado / disputado

Se asigna `IdentityMatch=?` cuando la evidencia o especificación no permite decidir continuidad. No se elige la opción más conveniente para producir un diff. Se preservan ambas versiones, la hipótesis de mapping y el desacuerdo para adjudicación independiente.

La firma semántica y las tolerancias deben fijarse antes de observar Outcome/Value y, en el experimento, sin acceso a Z/B/selección/ejecución.

## 5. Cambios que no crean identidad semántica automáticamente

| Cambio observado | Tratamiento por defecto | Comprobación adicional |
|---|---|---|
| Hash/commit distinto | Nueva versión/provenance; conservar TID provisionalmente | Integridad, compatibilidad y diff contractual |
| Lenguaje, plataforma o infraestructura distintos | RID/SID nuevo potencial; TID puede conservarse | Verificar contrato funcional y pre/postcondiciones |
| Parámetro dentro de tolerancia preespecificada | Nueva configuración; TID se conserva | Comprobar invariantes y accesibilidad |
| Parámetro fuera de tolerancia o altera semántica | Candidato a SID/TID nuevo | Adjudicar cambio de contrato |
| Interfaz/canal cambiado | Cambio de RID/relación/condición; no TID automático | Verificar si altera operación/entradas/salidas |
| Recurso, autorización o compatibilidad cambia | Cambio en C_acc/R_acc y posible A_f* | No confundir con identidad semántica |
| Corrección de bug | No automático | Si corrige desviación respecto al contrato, puede conservar TID; si redefine contrato, nueva identidad |
| Nombre/etiqueta cambia | Alias o metadato | No crear identidad nueva solo por renombrado |

## 6. Correspondencia entre snapshots

El matching se realiza en orden jerárquico y con trazabilidad:

1. **ID exacto:** mismo ID canónico y tipo; candidato a correspondencia directa, sujeto a validar contrato/versiones.
2. **Alias/renombre registrado:** mapping explícito, con fuente, vigencia y decisión.
3. **Mapping de versión:** misma TID con SID/RID diferentes; evaluar continuidad según §4.
4. **Candidato semántico:** comparación de firmas para IDs distintos; solo propone candidatos, no los fusiona automáticamente.
5. **Adjudicación:** dos evaluadores independientes, ciegos a brazo y resultados, resuelven casos materiales; desacuerdo no resuelto queda ?.

No usar similitud textual, nombre coincidente, hash ni proximidad temporal como criterio suficiente. El matching debe registrar método, versión de regla, candidatos rechazados, evaluadores, evidencia y motivo.

Estados por objeto:
- `MATCH_EXACT`
- `MATCH_ALIAS`
- `MATCH_VERSION_CONTINUITY`
- `MATCH_SUCCESSION` (identidades distintas relacionadas)
- `MATCH_SPLIT` (una identidad anterior corresponde a varias nuevas)
- `MATCH_MERGE` (varias identidades anteriores corresponden a una nueva)
- `MATCH_UNRESOLVED` (?)
- `NO_MATCH` (ausencia confirmada dentro de cobertura y universo declarados).

`NO_MATCH` no se asigna solo porque no se encuentre un registro: requiere cobertura suficiente del catálogo/universo. Si la cobertura es incompleta, usar MATCH_UNRESOLVED.

## 7. Correspondencias 1:N y N:1

Una transformación puede dividirse en varias transformaciones más pequeñas o varias pueden integrarse en una macrotransformación. No se debe representar esto como continuidad 1:1.

- **Split 1:N:** registrar retirada/vigencia final del objeto agregado si deja de existir como tal, alta de identidades componentes y relación `decomposed_into`. El diff depende de granularidad común; si no hay mapping composicional validado, no se computa equivalencia.
- **Merge N:1:** registrar las identidades previas y nueva identidad agregada con `composed_from` o `merged_into`. No atribuir equivalencia automática.
- **Refactor interno:** si el contrato semántico permanece, puede conservar TID aunque RID/SID y relaciones internas cambien.
- **Descomposición/recomposición funcional:** comparar a nivel de una granularidad común G y verificar composición, orden, condiciones y restricciones; la equivalencia de salida final no basta si costes, riesgos o estados intermedios son parte del contrato.

Los mappings composicionales tienen cardinalidad, dominio, contexto, versión, condiciones y evidencia explícitos. Si una composición no está definida o validada, el resultado es ?.

## 8. Contrato de granularidad y frontera

Cada snapshot lleva:
- frontera `b` y versión;
- unidad/instancia `i`;
- contexto `c`;
- tiempo `t`;
- granularidad `G`;
- catálogo `K` y versión;
- vocabulario/tipos de transformación y relaciones;
- regla de composición y mapping `M`.

Dos snapshots son directamente comparables solo si comparten frontera, unidad de análisis compatible, contexto definido, G, catálogo y reglas compatibles. Si no:
1. aplicar mapping explícito M a granularidad común;
2. conservar transformaciones no mapeadas;
3. documentar pérdida de información y cobertura;
4. no calcular componente afectado si M no es válido;
5. emitir diff parcial con incertidumbre explícita o `DIFF_NOT_COMPARABLE`.

No se debe convertir una macrotransformación en pasos atómicos solo para incrementar el conteo de T_acc, ni agregar pasos solo para forzar equivalencia. G se fija antes de la asignación y se mantiene en el horizonte primario, salvo cambio de diseño preespecificado.

## 9. Eventos canónicos de diff

Una vez resuelto matching y comparabilidad, emitir eventos tipados:

| Evento | Significado |
|---|---|
| ADD | Nueva identidad/relación/condición observada post, con ausencia basal respaldada |
| REMOVE | Identidad/relación/condición basal que deja de existir/ser válida post, con evidencia suficiente |
| MODIFY_STRUCTURAL | Misma identidad; cambian condiciones, relaciones, estado o configuración estructural relevante |
| VERSION_CHANGE | Cambia SID/RID/configuración manteniendo TID, con mapping respaldado |
| SPLIT / MERGE | Cambio de cardinalidad de correspondencia explícitamente validado |
| REWIRE | Cambia relación/extremo/dependencia sin cambio de identidad de los nodos |
| STATE_CHANGE | Cambia estado estructural de accesibilidad sin cambiar identidad |
| UNKNOWN | Evidencia o mapping insuficiente |
| OUT_OF_SCOPE | Cambio fuera de frontera/universo declarado; se registra pero no entra en ΔT_acc del estimando |

Cada evento incluye objeto(s), snapshot basal/post, ID(s), versiones, tipo de diff, fecha de vigencia, fuente, regla M/G, estado 1/0/?, adjudicación y efecto sobre U*/R*/C*/X*. ADD/REMOVE no se infieren por aparición/desaparición documental sin cobertura de ambos tiempos.

## 10. Relación con A_f*, D_f* y ΔT_acc*

- El matching de τ2 es necesario para afirmar que se observa la misma transformación focal entre t0 y t1.
- Si τ2 cambia de identidad, no se calcula `D_f*=I(A_f,0*=0 ∧ A_f,1*=1)` como si fuera el mismo objeto. Se requiere redefinir el objeto focal y el estimando antes de asignar, o declarar el contraste no comparable.
- `D_f*` es la proyección focal de cambios en snapshots comparables; no resume cambios no focales.
- El diff completo puede contener ADD/REMOVE/REWIRE/MODIFY/VERSION_CHANGE de otras transformaciones aunque D_f*=0.
- Un cambio de RID/SID puede modificar C_dep o accesibilidad sin cambiar TID.
- Un cambio en E_T o su cobertura no crea ADD/REMOVE estructural.
- Una relación o condición que cambia puede alterar accesibilidad sin cambiar identidad de los nodos.
- La equivalencia semántica de TID no prueba equivalencia causal de políticas, versiones o efectos sobre Value.

## 11. No filtración, cegamiento y adjudicación

El generador conserva TID/SID/RID verdaderos, mapping real y diff verdadero en el canal oculto. El analizador recibe IDs, snapshots observables y E_T, pero no truth, Z/B ni Outcome/Value. El evaluador independiente compara la salida congelada con truth después de cerrada la clasificación.

Los adjudicadores de continuidad semántica reciben los contratos y evidencias técnicas necesarios, pero no resultados del experimento ni brazo. Se conserva el desacuerdo inicial; la adjudicación no borra la primera clasificación.

La medición de fiabilidad debe separar:
- exactitud del matching;
- falsos matches y matches omitidos;
- error de clasificación de eventos ADD/REMOVE/MODIFY;
- porcentaje de unresolved;
- acuerdo entre evaluadores y tasa de adjudicación;
- sensibilidad a granularidad y mapping.

## 12. Contratos adversariales de diseño

| ID | Escenario | Salida exigida |
|---|---|---|
| ID-01 | Mismo TID, hash nuevo | Continuidad semántica provisional; auditar contrato/RID |
| ID-02 | Mismo nombre, distinta función nuclear | Nuevo TID o unresolved; nunca match por nombre |
| ID-03 | ID distinto, firma equivalente con evidencia | Candidato a alias/continuidad; adjudicación antes de match |
| ID-04 | Cambio de precondición esencial | Nueva identidad o unresolved según contrato; no continuidad automática |
| ID-05 | Cambio de plataforma, contrato estable | RID/SID nuevo posible; TID puede continuar |
| ID-06 | Split de una macrotransformación | SPLIT; diff no equivalente sin mapping G |
| ID-07 | Merge de dos transformaciones | MERGE; no fusionar identidades retroactivamente |
| ID-08 | Cobertura basal incompleta | UNKNOWN, no ADD post ni NO_MATCH |
| ID-09 | Frontera distinta | DIFF_NOT_COMPARABLE o mapping validado |
| ID-10 | Granularidad distinta | Mapping explícito a G común o diff indeterminado |
| ID-11 | Cambio de condición/recurso, TID estable | MODIFY_STRUCTURAL en C*/R*; reevaluar A_f* |
| ID-12 | Cambio de E_T sin cambio del sistema | ΔE_T, no evento estructural |
| ID-13 | τ2 no corresponde entre t0/t1 | D_f* no calculable como transición de misma identidad |
| ID-14 | Mapping 1:N con composición no validada | MATCH_UNRESOLVED; no sumar/colapsar transformaciones |
| ID-15 | Versión nueva altera riesgo/calidad pero no propósito | Mantener TID si contrato lo permite; registrar diferencias y no presumir equivalencia causal |

Son contratos de diseño. No se han creado fixtures ejecutables ni se han ejecutado pruebas.

## 13. Pendientes y criterios de cierre

Antes de aceptar este contrato:
1. acordar la taxonomía mínima TID/SID/RID/EID con el catálogo C10-S y el Core;
2. fijar campos obligatorios y esquema de serialización;
3. definir clases de transformación/relación y firma semántica por clase;
4. fijar tolerancias de equivalencia, reglas de pre/postcondición y versionado;
5. decidir política de IDs para el DGP y τ2 focal;
6. definir granularidad G y frontera para cada fixture;
7. especificar algoritmo de matching y adjudicación sin fuzzy auto-merge;
8. crear fixtures y oráculos para ID-01…15;
9. validar errores por brazo/tiempo/clase y sensibilidad;
10. revisión independiente y decisión formal.

No se cierra AUD-004 ni XSYNC-138-03/06. El artefacto es una propuesta de contrato, no un estándar ontológico TGCV. No hay freeze, implementación, simulación ni ejecución.


## 14. Crosswalk semántico de estado/contexto X*

El matching de snapshots debe distinguir el valor/contexto efectivo (X*) de las reglas/predicados (C*) que determinan la realizabilidad. Por ejemplo, la versión efectiva de un entorno puede ser X* mientras que la regla de compatibilidad con una versión objetivo pertenece a C*; una dependencia tipada es R* y la operación migratoria es U*. Estos ejemplos no sustituyen la ficha real del microdominio.

El cambio de X* debe registrarse con tiempo de vigencia, unidad, frontera, versión y event_id. No se interpreta automáticamente como ADD/REMOVE de transformación. Solo se registra su efecto sobre A⁺/A⁻/A^reconf/ΔR/ΔC cuando la regla de accesibilidad y el matching de snapshots lo sostienen. Un cambio de X* sin efecto estructural en accesibilidad queda como contexto; un cambio de evidencia pertenece a E_T.

Los campos mixtos deben descomponerse o quedar UNKNOWN/?. No se permite fuzzy matching ni equivalencia por nombre. La identidad semántica y la comparabilidad de snapshots siguen sujetas a los gates de §§8–13. El roster real y sus fixtures siguen pendientes; no se autoriza implementación ni ejecución.
