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

Si B amplía el permiso funcional para ejecutar `τ2`, aparece la vía `B→C_auth→A_f*`; el contraste deja de aislar únicamente la provisión técnica. La ficha es compatible conceptualmente con B-M05/PROV-06. **Precedencia reconciliada:** DEC-C10-067 fija conceptualmente `C_auth,base=1` como condición basal común no modificada por B; el maestro §67.3 y el crosswalk D2 la corresponden con `AUTH_f*`, no como factor independiente ni duplicado en `C_dep*`. Por tanto, la correspondencia conceptual está RESOLVED_BY_PRECEDENCE. **Permanece abierto materialmente:** fuente normativa, titular competente, objeto/alcance, vigencia, regla de adjudicación, registros y evidencia independiente. La ficha no está verificada ni la invariancia material demostrada.

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

#### 13.3.1. Crosswalk causal individual de D2-CAP-01

**Estado:** trazabilidad documental especializada; ficha DRAFT, no aprobada/no congelada. La capacidad no se ha operacionalizado ni medido en un sistema material.

| Eslabón | Correspondencia | Lectura causal y estado |
|---|---|---|
| Definición y descomposición | Capacidad instalada; disponible en ventana; reservada por unidad/ruta; consumida durante operación; margen operativo | Cinco objetos distintos. El margen es un derivado de capacidad disponible menos compromisos/demanda, no un primitivo autónomo. No sumar dimensiones incompatibles. |
| DGP y elegibilidad | Maestro §§46–47, 59.2–59.4 y 64.5; capacidad no focal basal común y suficiente antes de Z | El DGP S4-R aislado postula invariancia de capacidad no focal. Es supuesto del diseño, no evidencia. Capacidad focal que B instala/provisiona pertenece a C_dep*, no a C_capacity basal. |
| Predicado estructural | C_capacity,i,w = I(K_available(i,w) ≥ K_required(τ2,w)), plantilla existente no operacionalizada; posible inclusión de disponibilidad ex ante en R_access* | No convertir la plantilla en nuevo factor independiente de A_f*. Solo la capacidad/slots necesarios para ofrecer τ2, medidos por unidad y ventana y no duplicados por C_dep*, pueden integrar R_access*. |
| Límite con aplicabilidad/ejecución | App_f*(i,t) = I[Pre_τ2(S0_i,t,historia_i,t)=1]; carga concurrente, saturación puntual y consumo de una instancia | Capacidad requerida por estado S0, demanda concurrente o ejecución concreta no se retrotrae a A_f*. Va a App_f*, ejecución/rendimiento o resultado según su función causal. |
| Dominio de provisión | B-M07 Recursos; B-M02 Runtime/B-M03 Host/B-M12 Rendimiento relacionados si comparten pools, host, servicios o colas; B-M14 Alternativas si la capacidad sirve A1/A2/F2 | B-M07 rector. Las relaciones son candidatas hasta inventariar recursos, capacidad, consumidores y dependencias reales. |
| Contratos | PROV-05 (no reducción de disponibilidad A1/A2/F2), PROV-09 (no modificación de librerías/APIs/servicios críticos compartidos), PROV-03/04 (snapshots y grafo transitivo) | Protección indirecta de capacidad compartida y consumidores; ninguno constituye una prueba específica de capacidad ni PASS material. FCM-D2-06/07 añaden invariancia y registro de colaterales. |
| U_G candidato | N18, N05, N13, N15, N20; E16, E17, E19; etiquetas ya existentes RES-τ2, ALT-DEP, Rshared, Rτ2, RA12 | Mapping B-M07 de matriz de cobertura §9. No crear CAP-τ2 ni E-ID nuevo: el crosswalk no autoriza nuevos símbolos/relaciones. Instanciar solo con objetos, extremos, unidad, frontera, versión, ventana y evidencia observados. |
| Evidencia y falsadores | Configuración/versión; capacidad máxima y utilizable; cuotas/reservas/compromisos; K_required preespecificada; demanda concurrente; colas/contención; consumo B; snapshots pre-B/post-B/rollback | Falsadores: capacidad basal insuficiente; capacidad nominal ya comprometida; reserva que reduce otra ruta; degradación inducida por B; umbral retrospectivo; diferencia de medición/configuración; consumidores no inventariados. Cobertura insuficiente → ?. |
| Mecanismos | (i) condición constitutiva si capacidad/slots necesarios para ofrecer τ2 cambian; (ii) vía colateral a A1/A2/F2, Reach, ejecución, latencia, Outcome/Value por saturación o desplazamiento; (iii) interferencia si unidades comparten pool/cola/host | Puede coexistir más de un mecanismo. Capacidad nominal instalada no prueba capacidad disponible, y capacidad disponible no prueba ausencia de contención en la ventana. |
| Estimandos | ITT de la política material D2; atribución a ΔT_acc*; posible interferencia por capacidad compartida | Si B consume o degrada capacidad no focal, ITT sigue siendo efecto de la política/paquete. No atribuir exclusivamente a accesibilidad. La asignación individual no resuelve interferencia por pools/colas compartidos; exposición, unidad y diseño quedan abiertos. |
| Control | FCM-D2-06/07/08 | FCM-D2-06: invariancia no focal postulada, no demostrada. FCM-D2-07: registrar toda alteración colateral. FCM-D2-08: descartar provisión de fondo/rutas equivalentes en control. |

**Regla de clasificación:** capacidad instalada/slots disponibles para ofrecer τ2 pueden ser condición de acceso si cumplen necesidad, temporalidad, asignación y no duplicidad; capacidad focal introducida por B queda dentro de C_dep*; capacidad disponible/reservada para una ruta concreta debe modelarse según unidad/ventana; margen operativo bajo carga o precondiciones de S0 pertenecen a aplicabilidad/ejecución cuando dependen del estado o de la instancia. No añadir C_capacity a A_f* como factor separado mientras no se demuestre que representa una condición distinta de R_access* y C_dep*.

**Dictamen:** el crosswalk conceptual de D2-CAP-01 queda desarrollado. Permanecen abiertos la dimensión de capacidad pertinente, unidad y ventana, K_required, regla de reservas, inventario de pools/consumidores, separación de capacidad focal/no focal, interferencia, evidencia de invariancia y reconciliación material con App_f*. No se cierra PROV-05/09 ni MD-C1/MD-C4; no se aprueba ni congela la ficha y no se autoriza implementación/ejecución.
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


#### 13.4.1. Crosswalk causal individual de D2-C_INFO

**Estado:** clasificación y trazabilidad documental especializada; propuesta DRAFT. No se crea un predicado autónomo C_info, no se incorpora a A_f* y no se declara que B haya alterado materialmente información, conocimiento u observabilidad.

| Objeto | Correspondencia causal | Evidencia/contrato y falsador | Dictamen |
|---|---|---|---|
| Información técnica del sistema | Si el dato/metadato/parámetro es imprescindible para invocar o realizar τ2, debe localizarse en un término existente de la fórmula §67.3: normalmente DEP_f* si forma parte del adaptador/configuración focal; o COND_f*/REL_f*/RES_f* solo si su función material es distinta, ex ante y no duplicada | Especificación/versionado, frontera, diff de configuración, prueba de necesidad/ausencia y fuente independiente; PROV-03/04/12. Falsador de autonomía: el elemento ya está representado en DEP_f*, AUTH_f*, RES_f* o ID/COND | No añadir C_info a A_f*. La etiqueta histórica C_info de §30.1 se conserva como antecedente, no como factor depurado vigente |
| Conocimiento del agente (K) | Mecanismo posterior: B → manuales/formación/avisos → K → consideración/selección/inicio → Execution. Puede mediar una parte del efecto de política sin cambiar accesibilidad estructural | Inventario de mensajes, destinatarios, contenido, tiempos y exposición; B-M10, N22/E22 y B-M06 solo si cambia información/datos funcionales del sistema; PROV-03/04. I-INFO-01/03. Falsador de aislamiento: comunicación diferencial inducida por B | Vía informativa/mediadora o co-intervención; no confundir K con A_f* ni ajustar automáticamente por K postratamiento |
| Observabilidad y evidencia del evaluador | E_T separado: esquema, cobertura, validez, permisos, retención y adjudicación de logs/métricas. B puede cambiar A_f_obs/ΔT_acc_obs sin cambiar A_f*/T_acc* | B-M10; E_T como plano de medición separado, sin nodo/arista U_G explícitos. N16/E15 representa evaluación funcional/oráculo; N23/E23 representa endpoints de resultados, no el evaluador. PROV-02 protege el oráculo; PROV-03 snapshots; PROV-11 propagación de unknown. I-INFO-04/06. Falsador: cobertura/medición diferencial por brazo, cambio de regla/oráculo o missingness no comparable | Cambio epistémico/medición, no condición causal del sistema. Si no se puede reconstruir verdad del DGP o estado real, mantener ? |
| Información técnica imprescindible no verificable | Estado de presencia/ausencia desconocido | Evidencia independiente de configuración/versión y fuente; I-INFO-06; PROV-11 propaga cobertura incompleta | ?; nunca convertir falta de registro en ausencia ni asumir presencia |

**Contratos adversariales I-INFO-01…06:**

| ID | Caso | Resultado de clasificación requerido |
|---|---|---|
| I-INFO-01 | Sistema dispone de información técnica; agente desconoce τ2 | La accesibilidad no se hace 0 por desconocimiento del agente |
| I-INFO-02 | Agente conoce τ2; sistema carece de dato técnico imprescindible | El conocimiento no convierte la transformación en accesible |
| I-INFO-03 | B mejora manuales/formación sin modificar el sistema | Registrar vía B→K→consideración/selección/ejecución; posible mediación/colateral |
| I-INFO-04 | B mejora documentación del evaluador sin cambiar el sistema | Registrar ΔE_T; no inferir ΔT_acc* |
| I-INFO-05 | Información técnica duplicada por condición incluida en C_dep* | Una sola representación causal; no duplicar predicados |
| I-INFO-06 | Información necesaria cuya presencia no puede verificarse | Mantener ? y propagar cobertura incompleta |

**Reconciliación histórica obligatoria:** §30.1 conserva la conjunción histórica con `C_info`; la fórmula intermedia de §59.3 (ID/versión, `C_dep*`, `C_auth_base`, `R_access*`, `D_support*`) también es un antecedente supersedido como representación operativa. Prevalece la fórmula candidata depurada del maestro §67.3 y del crosswalk D2: `A_f*=I(ID_f* ∧ REL_f* ∧ COND_f* ∧ AUTH_f* ∧ RES_f* ∧ DEP_f* ∧ ¬BLOCK_f*)`. La información técnica imprescindible solo se asigna al término existente cuya función material corresponda, sin factor `C_info` autónomo ni duplicidad; `C_auth,base` se corresponde con `AUTH_f*`; `C_dep*` queda dentro de `DEP_f*`; recursos/capacidad ex ante pueden contribuir a `RES_f*`; `D_support*` se mapea a ID/tipo o COND según semántica. Se conserva el historial sin presentar las fórmulas intermedias como operativas. Los mappings materiales y pruebas de necesidad/no duplicidad siguen abiertos.

**Regla de medición:** distinguir el estado del sistema (truth/estado estructural), el conocimiento del agente (mecanismo) y el proceso de observación del evaluador (E_T). Si B cambia el acceso a telemetría, cobertura o adjudicación, modelar error/missingness diferencial. No condicionar análisis primario en variables postratamiento de conocimiento/observabilidad como si fueran covariables basales; la mediación/efecto de política exige estimando y supuestos propios.

**Dictamen:** el crosswalk de D2-C_INFO queda desarrollado conceptualmente. No hay inventario de información técnica imprescindible, prueba de ausencia/presencia, prueba de invariancia de comunicaciones, validación de E_T ni evidencia de medición comparable. No se aprueba C_info como predicado, no se cierra D2, PROV-02/03/04/11 ni los contratos I-INFO, y no se autoriza implementación, simulación o ejecución.


### 13.5. Regla transversal de clasificación y trazabilidad

Las fichas deben mapearse a las clases I/S/T/R/D/E ya definidas en esta matriz, sin reemplazar la clasificación por una etiqueta universal. Separar: (1) invariancia postulada en el DGP; (2) invariancia definida contractualmente; y (3) no-afectación demostrada empíricamente. Ninguna implica las otras. Para cada condición, conservar unidad, transformación, paso, rama, ventana, verdad del DGP, estado observado, fuente, cobertura, versión, adjudicador y razón de `?`, reutilizando la clave y reglas de propagación ya definidas en §§2–10.

Estas fichas son especializaciones D2 para revisión; no son evidencia empírica, no cierran elegibilidad, no demuestran invariancia y no autorizan implementación, simulación ni ejecución.


## 14. Integración temporal de adjudicaciones de configuración y transición C10-S

**Estado:** ACCEPTED — DOCUMENTAL por DEC-C10-088. La integración reutiliza las etapas y predicados vigentes; no crea un sistema paralelo.

### 14.1. Dos ejes distintos: stage_key y tiempo DGP

La secuencia de siete valores `stage_key` (DEC-C10-071) identifica etapas de configuración/representación:

`C_SRC → F1_S2 / A1_S1 → F2_DST_DECL / A2_DST_DECL → F2_DST_APPLIED / A2_DST_APPLIED`.

No equivale a los tiempos DGP `t0…t9`, a `SNAPSHOT.phase`, ni al paso hipotético `k=1…H`. La matriz temporal (§2) mantiene su reloj causal. El registro de cada observación debe enlazar explícitamente stage_key con snapshot/registro y con el instante DGP de generación/observación, sin inferir correspondencia por orden, timestamp o nombre. La ruta F/A es un eje separado y exige `route_id/route_record_id` exactos.

### 14.2. Crosswalk de etapas y adjudicación

| Etapa de configuración | Unidad de comparación | Predicados/familias primarios | Qué se puede concluir | Qué no se concluye |
|---|---|---|---|---|
| `C_SRC` | Artefacto fuente exacto, contrato/instancia, CMP owner y snapshot | Identidad/aplicabilidad/obligatoriedad IAM; cobertura y binding C0 | Baseline fuente identificable y aplicable | No prueba preservación ni accesibilidad causal |
| `F1_S2` | `C_SRC→F1_S2`, ruta F exacta | §15.3: estado PAR, tipo/dominio/valor, RUL, binding y evidencia; SM/FP primarios según DEC-C10-055 | Conformidad observada de la salida intermedia F | No cubre A1 ni destino/aplicación |
| `A1_S1` | `C_SRC→A1_S1`, ruta A exacta | Los mismos predicados, adjudicados independientemente | Conformidad observada de la salida intermedia A | No cubre F1 ni destino/aplicación |
| `F2_DST_DECL` | `F1_S2→F2_DST_DECL`, ruta F exacta | `P-DECL` semántico; `P-TRANS` lineage probatorio; SM/FP primarios sin duplicidad | Conformidad del destino declarado y, por separado, evidencia de que la transición lo produjo | No prueba instalación, activación ni estado runtime |
| `A2_DST_DECL` | `A1_S1→A2_DST_DECL`, ruta A exacta | Igual que F, adjudicación independiente | Conformidad del destino A declarado y lineage correspondiente | No prueba aplicación efectiva |
| `F2_DST_APPLIED` | `F2_DST_DECL→F2_DST_APPLIED`, destino y snapshot exactos | FP-06 aplicación; FP-07 post-check mediante FP-01…05 aplicables; FP-08 procedencia/identidad | Evento de aplicación y estado observado post-aplicación, cada uno por separado | FP-06 PASS no implica FP-07 PASS; FP-07 no reconstruye FP-06/08 |
| `A2_DST_APPLIED` | `A2_DST_DECL→A2_DST_APPLIED`, destino y snapshot exactos | Igual que F, adjudicación independiente | Aplicación y estado observado de A | No hereda evidencia de F |

### 14.3. Vector de adjudicación por ruta

Para cada ruta `r∈{F,A}`, unidad, parámetro/regla y versión, conservar un vector no compensable:

- **Intermedia:** predicados de §15.3/DEC-C10-085 para `C_SRC→F1_S2` o `C_SRC→A1_S1`.
- **Destino declarado:** `P-DECL` y `P-TRANS` de §15.5/DEC-C10-086, con la asignación primaria SM/FP vigente.
- **Aplicación y post-check:** FP-06, FP-07 y FP-08 de §15.7/DEC-C10-087; FP-07 se descompone por FP-01…05 aplicables.

No se construye un score ni un booleano agregado que compense predicados, rutas o dimensiones. Los resúmenes de etapa y ruta conservan todos los estados; un FAIL obligatorio permanece visible; si no hay FAIL, cualquier UNKNOWN impide PASS global. NOT_COMPARABLE se mantiene explícito y NA solo se permite por inaplicabilidad ex ante justificada, no para los PAR/RUL/FP obligatorios del contrato base.

### 14.4. Regla de lineage y no transferencia de evidencia

La evidencia debe referenciar el objeto exacto y la afirmación concreta. Una observación C_SRC no acredita F1/A1; evidencia F no acredita A; una salida intermedia no acredita el destino declarado; la equivalencia declarada no acredita que el proceso la produjo; el artefacto declarado no acredita aplicación; un evento FP-06 no acredita por sí solo el estado FP-07. FP-08 soporta procedencia/identidad, pero no reemplaza observación ni evento.

Se permite reutilizar una misma pieza de evidencia en más de un vínculo solo cuando su contenido soporte realmente cada afirmación; cada uso conserva predicado primario y alcance. Un mismo defecto causal no se cuenta dos veces en el agregado confirmatorio, de acuerdo con la reconciliación SM/FP.

### 14.5. Estados y cobertura

Se preservan los estados de DEC-C10-075/076 y DEC-C10-085…087:
- `PASS`: predicado satisfecho con identidad, mapping, observación, cobertura y evidencia suficientes.
- `FAIL`: contradicción demostrada con universo/cobertura suficientes; para no aplicación, evidencia autoritativa/exhaustiva o contradicción positiva.
- `UNKNOWN`: falta de observación, cobertura, identidad, mapping, lineage, evento, destino, snapshot u oráculo suficiente. La falta de registro nunca se convierte automáticamente en ABSENT o no aplicación.
- `NOT_COMPARABLE`: incompatibilidad de versiones/namespaces sin mapping aprobado.
- `NA`: inaplicabilidad ex ante justificada, no ausencia de datos.

COV/E_T sigue siendo epistémico: informa qué puede adjudicarse, no cambia por sí mismo la verdad del DGP, la accesibilidad o Reach. La mejora de cobertura puede revelar estado preexistente; no se registra como cambio estructural salvo regla DGP independiente.

### 14.6. Interfaz con la matriz temporal de rutas

Los predicados de configuración alimentan únicamente los componentes que su significado permite. La conformidad de PAR/RUL no equivale automáticamente a ACC, APP, REL, AUTH, RES, DEP, BLOCK o WIN. En particular:
- La presencia/configuración de una dependencia no demuestra su instalación/disponibilidad efectiva; debe resolverse en la frontera C_dep*/DEP y con evidencia pertinente.
- FP-04 compatibilidad ambiental y FP-05 seguridad permanecen diferenciadas de la equivalencia semántica de configuración.
- La aplicación de paquete (FP-06) y el post-check (FP-07) no se retrotraen para redefinir `T_acc(t3)` ni los estados previos.
- Outcome/Value en t8/t9 no se utiliza para adjudicar configuración, aplicación, Reach o cobertura.

Cualquier relación entre estado aplicado y accesibilidad/Reach requiere predicado causal explícito del DGP, unidad/transformación/ventana y evidencia; no se infiere por el solo hecho de FP-07 PASS.

### 14.7. Límites y cuestiones de cierre

Esta integración es un crosswalk documental, no una especificación ejecutable. Permanecen abiertos los mappings físicos CMP/PAR/REF/RUL/MET↔U_G, route_id y ROUTE_STEP exhaustivos, universe_definition/version y C0, gramática del localizador PAR, mapping M concreto, oráculo/observación, IAM completo, cobertura y evidencias materiales. No sella IAM ni autoriza fixtures, parser, validator, implementación, Design Freeze o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.

## 14. Crosswalk semántico AB-04 para las cards sintéticas (2026-11-10)

La definición de field_id y su asignación por card está en §12.8–12.9 de `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md`. Esta matriz conserva su autoridad para la clave temporal y la lógica de adjudicación: unidad×escenario×branch_id×step_k×TID/SID/RID cuando exista×input_state×snapshot exacto×predicate_id×t_eval×fuente/versión; truth_DGP y observed_state separados.

Reglas no alteradas:
- ID/REL/COND/AUTH/RES/DEP/¬BLOCK determinan accesibilidad estructural; APP se evalúa desde el estado de entrada de cada paso y no se incorpora automáticamente a A_f*.
- Una conjunción es 0 si algún requisito necesario es 0; 1 si todos son 1; ? si no hay 0 y queda algún desconocido.
- Una ruta completa es 1 solo si todos sus pasos y relaciones necesarias son 1; es 0 si algún requisito necesario es 0; en otro caso ?.
- Reach es 1 si existe una ruta completa 1; es 0 solo si todas las rutas del universo declarado son 0 y la cobertura es exhaustiva; en otro caso ?.
- Para observed_state se exige evidencia/cobertura suficiente; ausencia de evidencia no es 0. No filtrar hidden_truth al Analyzer.

Los field_id semánticos no son columnas físicas ni crean automáticamente NODE/EDGE/PREDICATE/ROUTE. La implementación futura deberá reconciliarlos con U_G y el crosswalk IAM sin duplicar matrices. No se asignan valores por unidad ni escenario y no se crean fixtures.


## DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 — contrato semántico de enlace (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como arquitectura candidata que la relación entre `request_id` y `trajectory_id` sea explícita, tipada y versionada, sin imponer una cardinalidad funcional 1:1. Se distinguen tres tipos no intercambiables:

1. `TEMPORAL_ASSOCIATION`: coexistencia temporal u orden compatible entre petición y trayectoria; no demuestra trazabilidad ni contribución causal.
2. `TRACEABILITY_LINK`: referencia técnica/documental verificable entre registros; no demuestra que la petición haya causado o modificado la trayectoria.
3. `CAUSAL_CONTRIBUTION`: relación causal definida por el DGP generador; debe distinguirse la verdad conocida por el generador de la evidencia observable y disponible para el analizador.

El modelo debe poder representar petición sin trayectoria atribuible, trayectoria sin petición atribuible, una petición que contribuya a varias trayectorias y, en escenarios con múltiples peticiones, varias peticiones que contribuyan a una trayectoria. La configuración primaria mantiene una oportunidad estandarizada por UE; por tanto, no genera múltiples request_id estandarizados dentro de esa UE, pero no impone que solo pueda existir una trayectoria ni que toda trayectoria tenga origen en esa petición. Las relaciones de escenarios secundarios con peticiones repetidas quedan anidadas en UE y no crean unidades experimentales independientes.

La existencia de cualquier enlace temporal o de trazabilidad no puede promoverse automáticamente a contribución causal. Las contribuciones causales se establecen por la verdad del DGP y se contrastan mediante los mecanismos/contrafactuales pertinentes; no se adjudican por proximidad temporal, coincidencia de IDs, respuesta del servicio o éxito técnico. Los registros observados no deben revelar al analizador la etiqueta de verdad del DGP salvo que ese conocimiento forme parte explícita del diseño de medición.

El enlace no define elegibilidad, inclusión poblacional, ITT, Outcome ni Value, y no puede usarse para excluir UE por eventos post-Z. No equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9; tampoco amplía el reloj t−1/t0…t9 ni la profundidad H. Los eventos de petición y sus enlaces se mantienen en subledger con timestamps, identidad/versionado y procedencia.

**OPEN:** reglas de generación de contribuciones, mecanismo de adjudicación, unidad temporal de atribución, tratamiento de contribuciones concurrentes y colaterales, evidencia observable para el analizador, cardinalidad de enlaces por tipo en cada DGP, y relación exacta con los estimandos ITT/mediación. No se congela schema físico ni protocolo técnico.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. D2 continúa como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren; main no se modifica.

## DEC-C10S-B1-CAUSAL-ADJUDICATION-001 — contrato de contribución causal petición–trayectoria (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como contrato causal candidato que una relación \`CAUSAL_CONTRIBUTION\` entre una petición y una trayectoria requiere un contraste contrafactual definido por el DGP: la presencia/intervención en una etapa concreta del ciclo de petición modifica una propiedad preespecificada de la trayectoria respecto del escenario contrafactual correspondiente, manteniendo explícitas las demás condiciones relevantes. La precedencia temporal, recepción, admisión, procesamiento, respuesta técnica, coincidencia de identificadores o éxito técnico no bastan por sí solos para adjudicar contribución causal.

Se distinguen, como clases potencialmente concurrentes y no necesariamente excluyentes:
- \`NECESSARY_CONTRIBUTION\`: sin la intervención/etapa considerada, la trayectoria definida no existiría bajo el contraste contrafactual especificado.
- \`ENABLING_CONTRIBUTION\`: la intervención hace factible la trayectoria o elimina una barrera relevante, sin implicar que sea causa única o suficiente.
- \`MODIFYING_CONTRIBUTION\`: la trayectoria también existiría, pero cambiaría una propiedad relevante bajo el contrafactual sin esa intervención.

Una contribución puede ser parcial, concurrente o colateral. Estas clases no implican signo positivo de Outcome ni creación de Value. La propiedad afectada debe identificarse en el DGP; no se presume que cualquier cambio de secuencia, factibilidad o atributo sea sustantivo sin regla de relevancia preespecificada.

La adjudicación debe referirse a una etapa concreta del ciclo —\`Request_opportunity\`, \`Request_attempt\`, \`Request_received\`, \`Request_admitted/rejected\`, \`Request_processing\` o \`Request_response\`— sin colapsar sus mecanismos. La oportunidad estandarizada común es una asignación/probe del harness; no se considera automáticamente una intervención realizada por el servicio ni una contribución causal. Cuando no se produce una etapa posterior, el DGP debe representar el mecanismo de no transición sin imputar una contribución de esa etapa.

Se mantiene segregación entre:
1. **Verdad del generador (\`truth_dgp\`)**: intervención/etapa, propiedad de trayectoria, contraste contrafactual, clase de contribución y procedencia de la etiqueta verdadera.
2. **Evidencia observada (\`observed_evidence\`)**: registros y mediciones permitidos al analizador, sin revelar etiquetas o potenciales contrafactuales reservados al generador.
3. **Adjudicación/evaluación**: comparación de inferencia del analizador con verdad segregada, reportando falsos positivos, falsos negativos y errores de clasificación; no convertir trazabilidad en prueba causal.

El registro conceptual de contribución deberá poder identificar etapa de petición, propiedad de trayectoria, contraste contrafactual, clase(s) de contribución, verdad DGP y evidencia observable, además de identidad/versionado/procedencia. Esto no congela un schema físico.

Esta adjudicación es mecanística y no modifica elegibilidad, población, unidad experimental, asignación ni estimando ITT; no se condiciona la inclusión a eventos post-Z. Tampoco define por sí sola Outcome o Value, ni equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9. No amplía el reloj t−1/t0…t9 ni H. D2 sigue como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren.

**OPEN:** especificación de los contrastes concretos de D2; propiedades de trayectoria causalmente relevantes; control de causas concurrentes/colaterales e interacciones; definición de intervención por etapa; positividad/soporte y versiones de tratamiento; evidencia observable y medición; reglas de atribución para contribuciones múltiples; sensibilidad a contrafactuales alternativos; relación con estimandos total, directo e indirecto y mediación.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen \`scientific_execution=false\` y \`execution_authorized=false\`; \`main\` no se modifica.

## 14. Integración PD: adjudicación causal y separación de verdad/evidencia (2026-11-11)

Véase C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md. La ficha por paso/branch conserva truth_dgp y observed_state separados; el Analyzer recibe solo observed_evidence y el Evaluator compara con truth después de sellar su salida. COV/E_T sigue siendo epistémico y no altera truth estructural.

La contribución petición–trayectoria se adjudica por etapa concreta (opportunity, attempt, received, admitted/rejected, processing, response) mediante contraste contrafactual y propiedad de trayectoria preespecificada. Se conservan las clases NECESSARY_CONTRIBUTION, ENABLING_CONTRIBUTION y MODIFYING_CONTRIBUTION, que pueden coexistir. TEMPORAL_ASSOCIATION, TRACEABILITY_LINK y CAUSAL_CONTRIBUTION permanecen distintos. La matriz no asigna valores 1/0/? a escenarios por conveniencia ni crea fixtures. Las vías concurrentes/colaterales, soporte, interacciones y mecanismos de no transición deben quedar explícitos en truth y evaluarse con cobertura observada.