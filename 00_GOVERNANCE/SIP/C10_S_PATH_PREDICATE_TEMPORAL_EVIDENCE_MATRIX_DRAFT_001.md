# C10-S — Matriz operacional de predicados por paso, rama y tiempo

**ID:** C10-S-PRED-MATRIX-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta operacional documental; no aprobada ni ejecutable.  
**Dependencias:** inventario finito §74, reconciliación temporal §75, contrato DGP §§33–34, contrato Reach §73 y contrato de identidad/versionado.  
**Restricciones:** no implementa ni ejecuta fixtures; no genera datos; no autoriza simulación, experimento, preregistro o freeze.

## 1. Objetivo y dictamen

Se convierte el inventario abstracto S0/S1/S2/SF y F1/F2/A1/A2 en una matriz de evaluación por paso. La matriz distingue: (1) accesibilidad estructural de la transformación; (2) aplicabilidad desde el estado concreto de entrada; (3) composición e identidad/versionado; (4) factibilidad conjunta —autorización, recursos, dependencias, ventanas y bloqueos—; y (5) evidencia observada y cobertura, separadas de la verdad estructural del DGP.

Reach se evalúa en t4 sobre el snapshot postintervención sellado en t3. El inventario base no contiene reglas de transformación que modifiquen el catálogo de accesibilidad durante la ruta. Por ello, en el fixture base propuesto, T_acc y las condiciones estructurales del snapshot t3 se mantienen fijas a lo largo de las ramas hipotéticas. Los estados de entrada cambian según F1/F2/A1/A2, por lo que App debe evaluarse paso a paso. Recursos, ventanas o autorizaciones solo cambian dentro de una rama si el DGP incorpora explícitamente una regla de consumo, caducidad, renovación o modificación; no se presupone ninguna.

## 2. Convención temporal y de rama

- t0: baseline/elegibilidad antes de Z.
- t1: asignación/oferta/recepción B y W_attempt.
- t2: verificación técnica y condiciones.
- t3: snapshot postintervención S_T(i,t3) y clasificación observada.
- t4: cálculo de Reach_H sobre snapshot t3 y reglas de rama declaradas.
- t5–t9: conocimiento, selección, ejecución, Outcome y Value; no alimentan retroactivamente Reach_H.

Índice de paso k=1…H; s0=S0. Ramas candidatas:
- πF=(F1,F2): S0→S2→SF.
- πA=(A1,A2): S0→S1→SF.

H=3 continúa siendo profundidad máxima candidata; ambas rutas enumeradas tienen longitud 2. No se añade un tercer paso artificial.

## 3. Ficha de predicado por paso

Cada evaluación se almacena con clave mínima:
(unit_id, scenario_id, branch_id, step_k, TID_alias, SID, RID, input_state, snapshot_id, predicate_id, t_eval, branch_time, truth_dgp, observed_state, evidence_id, coverage_id, source_version, adjudicator, reason_unknown).

| Código | Predicado | Pregunta operacional | Nivel/tiempo de referencia | ¿Puede variar dentro de la rama? |
|---|---|---|---|---|
| ID | Identidad/continuidad | ¿Es la transformación semánticamente la misma y su versión compatible? | TID/SID/RID; fijado en t3 | No en fixture base; solo con evento/versionado explícito |
| ACC | Accesibilidad | ¿Está la transformación en T_acc de la unidad bajo snapshot t3? | unidad×transformación×t3 | No en fixture base; requiere regla explícita de cambio de T_acc |
| APP | Aplicabilidad | ¿Se satisfacen precondiciones desde el estado de entrada s(k−1)? | transformación×estado hipotético×paso | Sí, porque cambia el estado de entrada |
| REL | Composición | ¿Está permitida la relación entre paso anterior y actual? | arista ordenada×versión | No en fixture base; solo por rewire/regla explícita |
| COND | Condiciones constitutivas | ¿Se cumplen las condiciones necesarias de la transformación en su contexto? | unidad/sistema o paso según ficha | Solo si son state-dependent o temporales y existe regla |
| AUTH | Autorización | ¿La autorización cubre actor, objeto, unidad y ventana del paso? | basal o unidad×paso×ventana | No si autorización basal constante; sí con caducidad/revocación explícita |
| RES | Recursos | ¿Hay recursos reservables para completar el paso y la ruta sin doble asignación? | sistema/unidad/rama×ventana | Sí solo con regla de reserva/consumo/liberación; no inferir consumo real |
| DEP | Dependencia técnica | ¿Se satisfacen instalación, integridad, compatibilidad y operación de la dependencia requerida? | unidad×dependencia×snapshot t3 | No en fixture base; cambio solo por intervención/evento explícito |
| BLOCK | Bloqueo | ¿Existe bloqueo que impide el paso? | transformación×unidad×ventana | Puede variar si causa state-dependent/temporal; exige regla y evidencia |
| WIN | Ventana/duración | ¿El paso y la ruta caben en ventanas, precedencias y caducidades? | paso/ruta×θ | Sí por programación temporal; H no define duración |
| COV | Cobertura/evidencia | ¿El universo, fuente y observación son suficientes para clasificar el predicado? | predicado×ruta×unidad×tiempo | Puede mejorar como conocimiento; no cambia truth estructural |

COV no es una condición causal constitutiva: no entra en la conjunción truth de accesibilidad ni en la verdad de Reach. Sí determina si el observador puede clasificar 1/0/? y si puede afirmar exhaustividad.

## 4. Matriz por ruta y paso

| Rama/paso | Entrada→salida | ACC en t3 | APP | REL | COND/AUTH/RES/DEP/BLOCK/WIN |
|---|---|---|---|---|---|
| F1, k=1 | S0→S2 | ACC(F1,t3) | APP(F1,S0) | Inicio de ruta; no requiere arista previa | Evaluar para F1 y ventana de k=1 |
| F2, k=2 | S2→SF | ACC(F2,t3) | APP(F2,S2) | REL(F1,F2) | Evaluar para F2 y ruta acumulada |
| A1, k=1 | S0→S1 | ACC(A1,t3) | APP(A1,S0) | Inicio de ruta; no requiere arista previa | Evaluar para A1 y ventana de k=1 |
| A2, k=2 | S1→SF | ACC(A2,t3) | APP(A2,S1) | REL(A1,A2) | Evaluar para A2 y ruta acumulada |

La accesibilidad de F2/A2 no se infiere de la de F1/A1. La aplicabilidad se evalúa desde S2/S1, no desde S0. La admisibilidad de ruta es una conjunción de los predicados necesarios de ambos pasos, la relación y las restricciones conjuntas de ruta.

## 5. Invariancia y dinámica: regla de clasificación

Antes de construir un fixture, cada variable debe clasificarse en una clase:

- **I — Invariante de rama:** queda fijada en t3 y no puede cambiar durante el recorrido hipotético (p. ej., identidad/versiones, catálogo, T_acc en el fixture base).
- **S — Dependiente del estado:** se vuelve a evaluar desde s(k−1) (p. ej., APP y cualquier COND expresamente state-dependent).
- **T — Dependiente del tiempo/ventana:** se evalúa para el intervalo asignado al paso (p. ej., WIN y AUTH con caducidad).
- **R — Dependiente de recursos de ruta:** requiere una regla de reserva, concurrencia, consumo/liberación (p. ej., RES).
- **D — Dinámica explícita:** solo cambia por una regla de transición versionada del DGP; crea snapshot hipotético de rama inmutable.
- **E — Epistémica:** evidencia/cobertura/adjudicación; puede cambiar la clasificación observada, nunca por sí sola la verdad estructural.

Regla por defecto: si no existe regla DGP explícita, el predicado se mantiene fijo conforme al snapshot t3 o queda indeterminado; no se inventa una transición. Un predicado no puede clasificarse simultáneamente como invariante y dinámico para la misma versión de fixture.

## 6. Evaluación por escenario

| Escenario | Rama focal F1→F2 | Rama alternativa A1→A2 | Precaución |
|---|---|---|---|
| R0 / S4R-A | F1 puede abrirse tras B; F2 requiere evaluación propia | Ausencia de A1/A2 solo si cobertura funcional exhaustiva | No asumir Reach=0 basal sin descartar ambas rutas; no asumir F* por alias |
| R1 / S4R-B | Evaluación ordinaria de F1 y F2 | Ruta basal estable puede mantener Reach=1 | Apertura focal no implica cambio de Reach |
| R2 / S4R-C | Evaluar efecto de B sobre F1/F2 | Revaluar A1/A2 si B puede modificarlas | Vía colateral; efecto paquete salvo identificación adicional |
| R3 / S4R-D | El intento fallido puede dejar ACC(F1)=0 o ? según evidencia | Según escenario basal subyacente | Z/W_attempt no determinan ACC, DEP o Reach |

No se asignan valores 1/0 a predicados concretos por escenario en este documento: esos valores pertenecen a la especificación del DGP y deben justificarse por mecanismo y evidencia, no rellenarse para obtener un resultado deseado.

## 7. Lógica de composición y propagación

Para una ruta π, los predicados necesarios incluyen por paso ID, ACC, APP, COND, AUTH, RES, DEP, ausencia de BLOCK y WIN, además de REL entre pasos. En verdad DGP:
- ruta=1 si todos los predicados necesarios son 1;
- ruta=0 si al menos uno necesario es 0;
- ruta=? si no hay 0 y al menos uno es ?.

Entre rutas alternativas:
- Reach=1 si alguna ruta completa es 1;
- Reach=0 solo si todas las rutas del universo relevante son 0 y la cobertura es exhaustiva;
- Reach=? en los demás casos.

La evidencia/cobertura no se introduce como una conjunción causal. Para el observador, cada predicado se clasifica 1/0/? según evidencia, y Reach_obs aplica las mismas reglas más la condición de cobertura para declarar 0.

## 8. Reservas, recursos y no interferencia

En el fixture aislado se propone asignar pools no compartidos por unidad. Sin embargo, la factibilidad de una ruta no se puede derivar de “hay recursos” sin especificar: tipo/cantidad de recurso; demanda de cada transformación; simultaneidad o secuencialidad; regla de reserva y liberación; capacidad por ventana; posibilidad de compartir entre ramas contrafactuales.

Las ramas F y A son alternativas potenciales de la misma unidad, no dos ejecuciones concurrentes. No deben consumir simultáneamente un mismo recurso por el mero hecho de enumerarse. La evaluación pregunta si cada ruta, considerada por separado bajo la política de reserva declarada, es factible. Si el diseño introduce competición real entre unidades, se abandona la independencia simple y se modela clúster/interferencia antes de calcular estimandos.

## 9. Evidencia, cobertura y adjudicación

Para cada predicado y ruta registrar evidencia directa/indirecta y fuente; instante de generación y observación; versión del contrato y del sistema; universo/catálogo al que se refiere; cobertura y límites de búsqueda; observador/adjudicador, cegamiento respecto de Z/B/O/V; estado observado 1/0/? y motivo; desacuerdo, contradicción o no comparabilidad.

La ausencia de evidencia no equivale a evidencia de ausencia. Una mejora de cobertura entre t0 y t3 puede descubrir una ruta preexistente: se registra como cambio epistémico, no como ADD estructural. No se usa Outcome/Value para adjudicar F*, alternativa, App, Reach ni cobertura.

## 10. Contratos adversariales documentales

| ID | Caso | Resultado requerido |
|---|---|---|
| PM-01 | F1 ACC=1, F2 ACC=0 | Ruta focal=0 |
| PM-02 | F1 ACC=1, F2 APP(S2)=? | Ruta focal=? salvo otro predicado necesario 0 |
| PM-03 | F1/F2 accesibles y aplicables, REL(F1,F2)=0 | Ruta focal=0 |
| PM-04 | F2 accesible pero APP(F2,S2)=0 | Ruta focal=0 |
| PM-05 | Todos los predicados estructurales 1, cobertura epistémica incompleta | Truth ruta=1; Reach_obs puede ser ? |
| PM-06 | Ruta A confirmada, ruta F desconocida | Reach truth/obs=1 si A observada y validada |
| PM-07 | A1/A2 no halladas, cobertura incompleta | Ruta alternativa=?; no declarar Reach=0 |
| PM-08 | Mejora de cobertura descubre A1 preexistente | ΔE_T≠0; no ADD estructural |
| PM-09 | Recurso compartido entre unidades sin modelo | No asumir no interferencia |
| PM-10 | F y A son ramas contrafactuales alternativas | No sumar sus consumos como simultáneos |
| PM-11 | AUTH caduca entre pasos | Aplicar regla temporal explícita; sin ella, ? |
| PM-12 | COND depende de estado intermedio | Reevaluar desde el estado de entrada de cada paso |
| PM-13 | Cambio de T_acc dentro de la rama sin regla DGP | Rechazar actualización inventada; mantener snapshot o ? |
| PM-14 | B modifica A1/A2 en R2 | Registrar vía colateral y revisar estimando/exclusión |
| PM-15 | W_attempt=1, dependencia técnica fallida | No inferir ACC=1 |
| PM-16 | No existe regla de reserva/consumo | RES=?; no afirmar ruta factible |
| PM-17 | Outcome/Value conocido antes de adjudicación | Cegamiento/independencia comprometidos; no usar para Reach |
| PM-18 | Catálogo truncado por límite computacional | No declarar exhaustividad semántica |

Son contratos de diseño; no se han implementado ni ejecutado.

## 11. Decisiones y dependencias aún abiertas

No se fija todavía: valor verdadero u observado de cada predicado por escenario; definición operacional de F* y criterio GOAL_F; universo funcional de alternativas y cobertura; G y H confirmatorios; duración, ventanas y caducidad; regla de reservas, demanda y recursos por transformación; qué condiciones constitutivas son invariantes o state-dependent en el dominio sustantivo; si existe dinámica dentro de la trayectoria o si el fixture base es estático; elección D1/D2, q_X*, estimandos y unidad/interferencia; fuentes E1–E4, adjudicación y matriz de error.

No se cierran AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007. La matriz es una especificación candidata, no un DGP completo.

## 12. Dictamen

Se dispone ahora de una matriz operacional que identifica qué se evalúa por transformación, estado de entrada, paso, rama y tiempo. El default del fixture base es snapshot estructural fijo en t3, aplicabilidad por estado hipotético, factibilidad por ruta y ausencia de dinámica no declarada. Cualquier cambio intrarrama exige regla DGP explícita y snapshot inmutable.

**Siguiente bloqueo:** definir el catálogo de predicados constitutivos y su ficha sustantiva para F1/F2/A1/A2, incluyendo qué es realmente state-dependent, temporal, recurso-dependiente o invariante. Después podrá fijarse el vector de evidencia y el oráculo de clasificación sin inventar valores.

No se han generado datos, implementado fixtures, simulado ni ejecutado el experimento.


---

## 13. Especialización D2 — condiciones basales, recursos, capacidad e información

**Estado:** fichas de trabajo recuperadas de material conversacional aportado el 2026-11-06 y reconciliadas documentalmente con esta matriz, el maestro C10-S y el manifiesto B. **DRAFT / PROPUESTA / NO APROBADO / NO CONGELADO / NO EJECUTABLE.** Los identificadores indicados como candidatos no adquieren carácter canónico por su inclusión aquí.

**Alcance:** especialización del contraste D2 (B_g0^D2 frente a B_g1^D2), manteniendo D2 como escenario primario candidato y D1 como secundario conforme a DEC-C10-066. No modifica DEC-C10-067 ni afirma que las condiciones sean invariantes demostradas.

### 13.1. Ficha D2-INV-AUTH-01 — autorización normativa basal

| Campo | Especificación candidata |
|---|---|
| Predicado | `C_auth,base` |
| Función | Condición constitutiva basal de autorización funcional para la transformación focal `τ2` |
| Nivel | Unidad × transformación `τ2` |
| Momento basal | Antes de asignación `Z` |
| Estado exigido | `C_auth,base=1` en la población primaria elegible |
| Clase | I — invariante respecto de la política B, como postulado del DGP aislado |
| Ventana | Desde la evaluación basal hasta la adjudicación de accesibilidad postprovisión |
| Tolerancia | Cero cambios inducidos por B en la autorización normativa funcional |
| Evidencia | Registro de autorización, titular, alcance, vigencia, objeto autorizado y versiones pre/post |
| Falsificador | Cualquier cambio diferencial inducido por B en la autorización normativa funcional |

**Distinción semántica obligatoria:**

1. **Autorización normativa funcional:** permiso para realizar `τ2`; debe estar satisfecha basalmente y permanecer común entre políticas.
2. **Permisos técnicos de provisión:** ACL, credenciales, tokens o acceso al endpoint del adaptador; pueden formar parte de B bajo alcance mínimo, sin ampliar la autorización funcional.
3. **Conocimiento o consideración del agente:** mecanismo posterior; no equivale a autorización ni a accesibilidad estructural.

Si B amplía el permiso funcional para ejecutar `τ2`, aparece la vía `B→C_auth→A_f*`; el contraste deja de aislar únicamente la provisión técnica. La ficha es compatible conceptualmente con B-M05/PROV-06. **Abierto:** fuente normativa, titular competente, alcance exacto y regla de vigencia/adjudicación de `C_auth,base` (véase maestro §59.6). No declarar ficha verificada hasta resolverlo.

### 13.2. Ficha D2-RES-01 — recursos no focales

**Estado:** propuesta de especialización; no aprobada. Evitar un indicador único que mezcle disponibilidad estructural y consumo de ejecución.

| Objeto | Qué representa | Función causal | Tratamiento D2 |
|---|---|---|---|
| Disponibilidad basal | Recursos no focales asignados y disponibles para que `τ2` pueda estar a disposición | Condición constitutiva candidata de accesibilidad | Común, suficiente y verificada antes de Z |
| Capacidad instalada | Recursos técnicos que permiten ofrecer `τ2`, separados de la carga de una ejecución concreta | Propiedad de configuración; solo condición de acceso si habilita la oferta | Común, salvo escenario adversarial |
| Consumo de ejecución | CPU, memoria, almacenamiento, tiempo, trabajo humano u otros insumos de una instancia | Aplicabilidad, ejecución o calidad, según recurso y nivel | Medición separada; no incorporarlo automáticamente a `A_f*` |
| Recursos usados por B | Recursos para instalar, mantener y operar el adaptador | Parte de provisión y posible vía colateral | Registrar y comprobar no desplazamiento de rutas alternativas |

**Predicado candidato:** `R_access*(i,t;τ2)=1` cuando, para la unidad y ventana declaradas, existe una asignación verificable y suficiente de recursos no focales requeridos para poner `τ2` a disposición, independientemente de selección o ejecución. La suficiencia exige identificar recurso/unidad, titular o mecanismo de asignación, cantidad disponible y comprometida, unidad/sistema, ventana, dependencias/consumidores compartidos, evidencia y regla preespecificada. La existencia nominal no basta.

**Contraste D2:** el régimen de recursos no focales debe ser el mismo en control y tratamiento; los recursos reservados/consumidos por el adaptador se registran por separado; se mide la disponibilidad de recursos compartidos y consumidores; el consumo de ejecución no se retrotrae como accesibilidad. Si B desplaza recursos de A1/A2 u otras rutas, registrar `B→recursos compartidos→ruta alternativa→Reach/Outcome/Value`.

**Evidencia y falsadores:** inventario/asignación/medición pre-Z; insuficiencia o compromiso del recurso; umbral no satisfecho o retrospectivo; disponibilidad A1/A2 degradada; consumo B no registrado; variación diferencial no modelada. Sin cobertura suficiente, estado `?`, nunca invariancia presumida.

**Reutilización y dependencias:** maestro §§46–47 y 59.2–59.3; manifiesto B-M07; PROV-05 (no reducción de disponibilidad A1/A2/F2) y PROV-09 (no modificación de dependencias críticas compartidas); MD-C1/MD-C4 permanecen abiertos. No introducir nuevos símbolos definitivos para subcomponentes sin mapearlos a `R_access*` y al DGP.

#### 13.2.1. Crosswalk causal individual de D2-RES-01

**Estado:** reconciliación documental especializada; la ficha sigue siendo propuesta no aprobada/no congelada. No existe inventario material ni prueba de invariancia.

| Eslabón | Correspondencia | Lectura causal y estado |
|---|---|---|
| Definición y clase | Disponibilidad basal de recursos no focales asignados y utilizables para poner τ2 a disposición; separar capacidad instalada, consumo de ejecución y recursos usados por B | Condición constitutiva candidata. No usar un indicador agregado que mezcle stock/disponibilidad ex ante con demanda/consumo de una instancia. |
| DGP y elegibilidad | Maestro §§46–47, 59.2–59.4 y 64.5; elegibilidad basal antes de Z | La disponibilidad suficiente se postula común/satisfecha en la población primaria. La notación histórica C_resource/C_capacity de §46.2 requiere reconciliarse con R_access* y C_dep*; no implica tres factores autónomos ni autoriza doble contabilización. |
| Predicado estructural | R_access*(i,t;τ2), maestro §59.3; C_resource solo como descriptor de la disponibilidad de recursos, no como nuevo multiplicador | Incluir en R_access* únicamente disponibilidad ex ante necesaria y no duplicada. Consumo de ejecución, carga S0 y recursos consumidos por B no se retrotraen automáticamente a accesibilidad. |
| Dominio de provisión | B-M07 Recursos; B-M02 Runtime/B-M03 Host/B-M12 Rendimiento relacionados si el grafo transitivo revela recursos o servicios compartidos; B-M14 Alternativas si los consumidores son A1/A2 | B-M07 es el dominio rector; los demás son superficies relacionadas, no vías observadas. |
| Contratos PROV | PROV-05 y PROV-09; PROV-03/04 para snapshots, dependencias y consumidores | PROV-05 exige no reducción de disponibilidad A1/A2/F2; PROV-09 exige no modificar dependencias críticas compartidas. Son contratos documentales pendientes, no PASS ni prueba material. |
| U_G candidato | N18, N05, N13, N15, N20; E16, E17, E19; predicados RES-τ2, ALT-DEP, Rshared, Rτ2 y RA12 | Roles/aristas candidatos según matriz de cobertura §9. Crear registros solo con objetos, extremos, unidad, frontera, versión, ventana y evidencia observados. No inferir consumidores ni relaciones por el crosswalk. |
| Evidencia/falsadores | Inventario y asignación pre-Z; disponibilidad, compromisos, cuotas, consumo B, consumidores compartidos y medición por unidad/ventana; snapshots pre-B/post-B/rollback | Falsadores: recurso basal insuficiente/comprometido; consumo B no registrado; desplazamiento o degradación A1/A2/F2; variación diferencial; consumidores/dependencias no cubiertos. Cobertura insuficiente → ?. |
| Mecanismo causal | (i) cambio constitutivo si B altera R_access* y con ello A_f*; (ii) vía colateral si desplaza recursos/capacidad de rutas alternativas o afecta rendimiento, ejecución, Outcome/Value; (iii) interferencia si el consumo de una unidad afecta a otras | Puede haber varios mecanismos simultáneos. No confundir la ruta topológica compartida/alternativa con la clase de mecanismo causal. |
| Estimandos | ITT de la política material D2; efecto específico de accesibilidad/estimando C10-D1 y LATE_f solo bajo sus supuestos | Si B cambia recursos no focales, el ITT conserva interpretación como efecto de la política/paquete. No atribuirlo exclusivamente a ΔT_acc*. La aleatorización individual no elimina interferencia por recursos compartidos; si existe, se necesita exposición/interferencia definida, diseño por conglomerados u otra estrategia defendible. No se elige aquí una unidad de conglomerado. |
| Control | FCM-D2-06 y FCM-D2-07; FCM-D2-08 cuando afecte alternativas/provisión de fondo | FCM-D2-06: condición común postulada, no demostrada. FCM-D2-07: registrar cambios colaterales. FCM-D2-08: comprobar alternativas y fondo. MD-C1/MD-C4 permanecen abiertos. |

**Regla de no duplicidad que queda abierta para reconciliación:** §46.2 enumera C_resource y C_capacity en la elegibilidad; §59.2–59.3 los descompone y sitúa la disponibilidad ex ante dentro de R_access* solo si es necesaria y no duplicada, mientras que capacidad/consumo dependientes del estado pueden pertenecer a aplicabilidad o ejecución. Antes de congelar A_f* debe decidirse, para cada dimensión concreta, si es (a) disponibilidad estructural dentro de R_access*, (b) componente ya cubierto por C_dep*, o (c) aplicabilidad/ejecución/resultado. No mantener simultáneamente predicados redundantes.

**Dictamen:** la trazabilidad conceptual de D2-RES-01 queda desarrollada. La invariancia de recursos, la independencia de A1/A2/F2, el inventario de consumidores, la suficiencia basal y la ausencia de interferencia no están demostrados. No se aprueba la ficha ni se cierra PROV-05/09, MD-C1/MD-C4 o la identificación causal.

### 13.3. Ficha D2-CAP-01 — capacidad no focal

**Estado:** propuesta de especialización; no aprobada. `C_capacity` no es sinónimo de `C_resource`.

| Objeto | Definición | Papel en el modelo |
|---|---|---|
| Capacidad instalada | Máximo técnico soportable bajo condiciones especificadas | Propiedad del sistema/configuración |
| Capacidad disponible | Parte utilizable en una ventana, descontando compromisos y restricciones | Condición potencial de acceso |
| Capacidad reservada | Fracción asignada a unidad, transformación o ruta | Factibilidad de ruta |
| Capacidad consumida | Capacidad efectivamente utilizada durante operación | Aplicabilidad/ejecución y posible vía colateral |
| Margen operativo | Diferencia entre capacidad disponible y demanda comprometida | Indicador de suficiencia, no primitivo autónomo |

**Predicado candidato (plantilla, no operacionalizada):**

`C_capacity,i,w = I(K_available(i,w) ≥ K_required(τ2,w))`

No aplicar hasta fijar dimensión (concurrencia, tasa, memoria, procesamiento, red, capacidad humana u otra), unidad/método, configuración/versión, ventana, demanda requerida, compromisos/reglas de reserva y umbral preespecificado. Si se requieren varias dimensiones, la suficiencia es conjuntiva; no sumar magnitudes incompatibles.

**Contraste D2:** capacidad no focal basal bajo régimen común; capacidad focal introducida por B pertenece a `C_dep*`, no se vuelve a contabilizar en `C_capacity`; capacidad compartida se registra por compromisos y contención; saturación/degradación inducida por B es posible vía colateral. Si B modifica capacidad disponible de A1/A2, no se absorbe como mejora de accesibilidad focal.

**Falsadores:** capacidad basal inferior al umbral; capacidad nominal comprometida durante la ventana; reserva de una ruta reduce otra; adaptador degrada capacidad no focal; medición/configuración diferencial; interferencia entre unidades. Ausencia de cobertura → `?`.

**Fuentes:** Path Predicate Temporal Evidence Matrix §8 (reserva/concurrencia/factibilidad); manifiesto §5; maestro §§46–47 y 59; Closure Control Matrix §§20, 26 y 29. **Abiertos:** pertenencia de la capacidad necesaria para ofrecer `τ2` a `C_dep*` o a una condición no focal; ventana cuando hay rutas secuenciales/reservas; necesidad de conglomerados/interferencia por capacidad compartida. DGP S4-R aislado postula no modificación de capacidad no focal; es hipótesis verificable, no hecho demostrado.

### 13.4. Ficha de clasificación D2-C_INFO — información

**Estado:** propuesta conceptual de clasificación; no crear por ahora un predicado autónomo `C_info` ni añadirlo a `A_f*`. Primero comprobar duplicidad con `C_dep*`, autorización, recursos y dominio.

| Objeto | Contenido | Clasificación causal provisional |
|---|---|---|
| Información técnica del sistema | Datos, descriptores, metadatos, especificaciones o parámetros incorporados al sistema para invocar/realizar `τ2` | Podría ser constitutiva de accesibilidad |
| Conocimiento del agente | Conocer existencia y modo de uso de `τ2` | Mecanismo posterior de conocimiento/consideración |
| Información comunicada por B | Avisos, instrucciones, formación o asistencia de B | Posible vía colateral de la intervención |
| Información del evaluador | Fuentes, registros, cobertura, validez y observabilidad | Plano epistémico `E_T`, no condición causal de accesibilidad |

La información técnica solo se considera constitutiva si conjuntamente: (a) está incorporada/disponible en frontera y versión declaradas; (b) es necesaria para invocar/realizar `τ2`, no solo conveniente; (c) se verifica independientemente del conocimiento/comportamiento del agente; (d) su ausencia impide la realizabilidad focal con las demás condiciones satisfechas; y (e) no duplica contenido ya representado en `C_dep*`, autorización, recursos o dominio.

**Relación con B:** instalar/configurar información técnica imprescindible exige decidir si pertenece a `C_dep*` o es vía adicional; manuales/formación/avisos al agente son vía informativa distinta; conocimiento puede alterar consideración/selección/ejecución sin cambiar accesibilidad estructural; cambios en registros/cobertura del evaluador modifican `E_T`, no necesariamente el sistema.

**Contratos adversariales recuperados I-INFO-01…06 (propuestos):**

| ID | Caso | Resultado requerido |
|---|---|---|
| I-INFO-01 | Sistema dispone de información técnica, agente desconoce `τ2` | No convertir automáticamente accesibilidad en 0 |
| I-INFO-02 | Agente conoce `τ2`, sistema carece de dato técnico imprescindible | Conocimiento no implica accesibilidad |
| I-INFO-03 | B mejora manuales/formación sin modificar sistema | Detectar vía informativa colateral |
| I-INFO-04 | Mejora documentación del evaluador sin cambiar sistema | Cambio en `E_T`, no necesariamente en `ΔT_acc*` |
| I-INFO-05 | Información técnica duplicada por condición incluida en `C_dep*` | Evitar doble contabilización |
| I-INFO-06 | Información necesaria cuya presencia no puede verificarse | Mantener `?`, no asumir presencia/ausencia |

**Consecuencia arquitectónica:** mantener separados (i) accesibilidad estructural, con información técnica solo si supera los criterios constitutivos; (ii) mecanismo de conocimiento del agente; y (iii) evidencia del evaluador en `E_T`. No ajustar automáticamente por conocimiento postratamiento: la vía `B→K→Selection→Execution` puede ser mediadora/colateral y el ajuste no resuelve por sí solo identificación.

**Abiertos:** inventario concreto de información técnica imprescindible; mapping de cada elemento a `C_dep*` u otra condición sin duplicidad; evidencia para invariancia técnica y ausencia de comunicaciones diferenciales.

### 13.5. Regla transversal de clasificación y trazabilidad

Las fichas deben mapearse a las clases I/S/T/R/D/E ya definidas en esta matriz, sin reemplazar la clasificación por una etiqueta universal. Separar: (1) invariancia postulada en el DGP; (2) invariancia definida contractualmente; y (3) no-afectación demostrada empíricamente. Ninguna implica las otras. Para cada condición, conservar unidad, transformación, paso, rama, ventana, verdad del DGP, estado observado, fuente, cobertura, versión, adjudicador y razón de `?`, reutilizando la clave y reglas de propagación ya definidas en §§2–10.

Estas fichas son especializaciones D2 para revisión; no son evidencia empírica, no cierran elegibilidad, no demuestran invariancia y no autorizan implementación, simulación ni ejecución.
