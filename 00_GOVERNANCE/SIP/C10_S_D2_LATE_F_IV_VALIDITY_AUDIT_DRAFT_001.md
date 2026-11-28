# C10-S — Auditoría de validez IV de D2 y del tratamiento focal D_f*
**ID:** C10-S-IV-AUD-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-06
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT
**Rama:** `research/c10-s-consolidation-draft`
**Dependencia:** PR #116 (Draft)
**Alcance:** auditoría documental y causal de los supuestos necesarios para interpretar un Wald como `LATE_f` en D2. No es validación empírica, simulación, ejecución ni aceptación de estimando.

## 1. Dictamen ejecutivo

**`LATE_f` no está actualmente identificado ni listo para estimación Wald en D2.** La aleatorización candidata puede sostener un efecto de asignación de la política material (`ITT_Z`) si se completa y respeta el diseño de asignación, pero no basta para atribuirlo al cambio focal de accesibilidad. Los supuestos IV relevantes siguen abiertos y varios tienen amenazas concretas en la propia arquitectura de provisión.

El obstáculo principal no es la existencia de una fórmula Wald, sino la correspondencia entre el instrumento asignado (`Z`), la política material (`B_{gZ}^{D2}`), el tratamiento focal verdadero (`D_f^*`) y el resultado específico (Outcome o Value). DEC-C10-066 y DEC-C10-067 no aceptan los supuestos IV ni cierran esa correspondencia.

**Disposición:** mantener `LATE_f` como estimando secundario estrictamente condicional; no calcular ni seleccionar Wald como resultado causal interpretable hasta cerrar los gates de §8. No se modifica la jerarquía general de C10-D1 ni se sustituye `θ_A(q)` por un estimando local focal.

## 2. Fuentes y precedencia inspeccionadas

- C10-S maestro Draft 004, en particular §§16.11.5 y 16.12.
- Plan integrado Draft 004, en particular §16.11 y la operación siguiente registrada en §16.12.
- DEC-C10-066: D2 primario candidato / D1 secundario, alcance limitado.
- DEC-C10-067: aceptación conceptual de las políticas materiales D2, sin aprobación de cumplimiento, éxito, accesibilidad o ejecución.
- Reconciliación C10-S ↔ C10-D1 S4-R, que separa `ITT_Z`, `ψ_policy`, `θ_Af(q_X^*)`, `LATE_f` y `θ_A(q)`.
- Manifiesto B-M01…15, matriz de cobertura U_G, fichas de invariantes y contratos de medición/temporalidad recuperados en la rama.

La auditoría reutiliza estos contratos; no recrea la definición de D2, no reabre DEC-C10-066/067 y no declara cerrado XSYNC.

## 3. Tratamiento IV y cadena causal

El tratamiento candidato para el IV focal es la apertura basal→post de la transformación `τ2`, representada por `D_f^*`, dentro de la población elegible definida antes de asignar Z y con inaccesibilidad focal basal. No debe sustituirse por la asignación, el intento programado, el intento efectivo, la recepción, la instalación o `C_dep^*`.

La secuencia que debe preservarse es:

`Z → B_assigned^D2 → W_programmed → W_attempt/receipt → C_dep* → A_f* → D_f* → ΔT_acc* → Reach/Π_H → selección/inicio → Exec → Outcome → Value`.

La primera etapa debe calcularse por separado para `C_dep*`, `A_f,post^*`, `D_f^*` y `ΔT_acc^*`. Un efecto de Z sobre `C_dep*` no demuestra una primera etapa sobre `D_f^*`; tampoco demuestra exclusión. La derivación candidata 0→0.80 depende de supuestos de diseño aún no validados y no es una primera etapa observada.

Debe conservarse además la distinción entre:
- `D_f^*`: estado focal verdadero adjudicado;
- `D_f^{obs}`: registro observado utilizado por el analizador;
- error de clasificación y ausencia de observación de ambos estados.

No se acepta que el analizador reconstruya `D_f^*` a partir de Z, B, W o C_dep. La adjudicación debe derivarse de los predicados completos de `A_f^*` y de snapshots comparables, sin usar Outcome/Value para definir accesibilidad.

## 4. Auditoría por supuesto IV

### 4.1 Relevancia — ABIERTA / NO DEMOSTRADA

La política D2 programa un intento focal en tratamiento y no lo programa en control. Esto define el contraste de política, no garantiza que el intento se inicie, sea recibido, se instale o abra `D_f^*`. DEC-C10-067 separa expresamente esos estados y permite provisión de fondo/crossover en control, que debe registrarse.

El parámetro candidato `s=0.80` y la derivación condicional de `P(C_dep*=1|Z=1)` no son evidencia de una primera etapa sobre `D_f^*`. No existen todavía estimaciones observadas ni parámetros DGP aprobados que permitan certificar relevancia focal.

**Cierre requerido:** especificar y luego evaluar por separado las primeras etapas técnicas y transformacionales, con incertidumbre, soporte, cumplimiento, provisión de fondo y reglas ante primera etapa nula/débil. La relevancia estadística no valida los otros supuestos.

### 4.2 Independencia del instrumento — CONDICIONAL / NO CERRADA

La asignación aleatoria puede proporcionar independencia de Z respecto de los resultados y tratamientos potenciales dentro de la unidad de asignación, conforme al esquema realmente ejecutado. Sin embargo, la unidad de asignación, el posible nivel de clúster, la estratificación/bloques, la población elegible final y la estructura de recursos compartidos no están cerrados en el diseño operativo.

No debe confundirse aleatorización individual hipotética con independencia efectiva cuando dependencias, capacidad, licencias, servidores o equipos son compartidos.

**Cierre requerido:** fijar unidad y mecanismo de asignación, elegibilidad pre-Z, bloques/estratos, registro de semilla y probabilidades, y correspondencia entre unidad de asignación, análisis e inferencia. Si la asignación es por clúster, el análisis debe respetarlo.

### 4.3 Exclusión — AMENAZA MATERIAL / NO DEMOSTRADA

Para interpretar Wald como efecto de `D_f^*`, Z/B no puede afectar el resultado considerado por vías que no pasen por ese tratamiento focal. La aleatorización no demuestra exclusión.

La arquitectura identifica amenazas plausibles:
- recursos, capacidad y desplazamiento de recursos no focales;
- costes, incentivos, permisos o cambios de autorización;
- latencia, rendimiento, disponibilidad y calidad;
- seguridad, riesgo, integridad o fallos residuales;
- información comunicada, conocimiento del agente y observabilidad diferencial;
- habilitación, degradación o eliminación de alternativas A1/A2;
- cambios de dependencias compartidas, estado persistente, rollback y carryover;
- cambios en el oráculo, adjudicación, datos, missingness o medición de Outcome/Value.

DEC-C10-067 exige que estas condiciones sean comunes y que cualquier diferencia se registre como vía colateral/cointervención. Ese requisito conceptual no equivale a evidencia de invariancia.

**Distinción importante:** las consecuencias posteriores de la apertura focal —Reach, trayectorias, selección, ejecución, Outcome y Value— son parte del efecto de `D_f^*` si el tratamiento está definido como esa apertura. En cambio, un efecto de B sobre Value por rendimiento, coste, seguridad, información, recursos o alternativas que no esté contenido en `D_f^*` viola la exclusión focal. También la viola que B modifique otros componentes de `ΔT_acc^*` y afecte Value sin quedar representado por el tratamiento focal `D_f^*`.

**Cierre requerido:** inventario y evidencia por unidad/frontera/versión/ventana de las vías B-M01…15; clasificación de rutas focales, compartidas, alternativas, externas y desconocidas; prueba de invariancia solo donde exista evidencia; escenarios adversariales con vías directas; sensibilidad/cotas para desviaciones de exclusión. Si la exclusión no es defendible, reportar `ITT_Z` como efecto de política/paquete y no etiquetar Wald como `LATE_f`.

### 4.4 Monotonicidad — ABIERTA / PLAUSIBILIDAD NO ESTABLECIDA

La condición requerida es que la asignación al tratamiento no reduzca `D_f^*` para ninguna unidad respecto al control (ausencia de defiers), en la definición y población concretas. Una primera etapa media positiva no demuestra monotonicidad individual.

La política de provisión puede producir desplazamiento de capacidad, degradación de alternativas, incompatibilidades, cambios de dependencias compartidas, residuos o rollback incompleto. Estas vías podrían hacer que la asignación tratada reduzca la apertura focal en algunas unidades, aun cuando el efecto medio sea positivo.

La provisión focal de fondo en controles puede generar always-takers; por sí sola no demuestra violación de monotonicidad. Deben distinguirse compliers, never-takers, always-takers y defiers sin inferir tipos individuales a partir de observaciones incompletas.

**Cierre requerido:** fijar la definición binaria/versionada de `D_f^*`; construir escenarios DGP con y sin defiers y con crossover; verificar que el analizador no declara LATE cuando la verdad oculta viola monotonicidad; y justificar sustantivamente por qué la política no puede cerrar rutas focales para ninguna unidad. La monotonicidad no es plenamente verificable en datos observados y debe conservar análisis de sensibilidad.

### 4.5 Consistencia y versiones — ABIERTA

La política aceptada requiere artefacto y versión identificados antes de asignación, pero los datos operativos pendientes incluyen identidad/hash, recepción, protocolo de aceptación, ventana, reintentos, fallos parciales, rollback y evidencia por componente de `C_dep^*`.

Si unidades asignadas a la misma política reciben versiones o procedimientos materialmente distintos, la exposición puede tener múltiples versiones. No se debe colapsar intento programado, intento recibido y tratamiento focal realizado en una sola variable.

**Cierre requerido:** pin exacto de artefacto/configuración y versión; registro de actor, recepción, intento, instalación, integridad, compatibilidad, operatividad, reintentos y rollback; regla de consistencia entre política asignada, versión recibida y `D_f^*`; tratamiento explícito de desviaciones y crossover.

### 4.6 Interferencia — ABIERTA / RIESGO ESTRUCTURAL

No está demostrada la ausencia de interferencia. Dependencias, licencias, servicios, servidores, capacidad, equipos y alternativas pueden compartirse entre unidades. La provisión a una unidad puede alterar la disponibilidad o el resultado de otra; los residuos y rollback pueden producir exposición entre periodos.

**Cierre requerido:** fijar unidad de asignación y unidad de exposición; inventariar dependencias y recursos compartidos; elegir entre ausencia de interferencia defendible, diseño por clúster o un mapa explícito de exposición/interferencia parcial; especificar ventanas y carryover. Si no puede identificarse el efecto bajo interferencia, no utilizar el Wald individual estándar.

### 4.7 Medición de tratamiento y resultado — ABIERTA / RIESGO DE CLASIFICACIÓN

La medición de `D_f^*` requiere adjudicación independiente de `A_f,base^*` y `A_f,post^*), con predicados completos y snapshots temporales. `C_dep^*` no basta. El registro observado `D_f^{obs}` puede diferir de la verdad por cobertura, oráculo, conocimiento, permisos de observación o error diferencial inducido por B.

Value requiere regla, beneficiario, dimensiones, horizonte y medición fijados e independientes de la definición de accesibilidad. Pérdida/observación selectiva de Value puede cambiar la población observada y sesgar ITT y Wald; no se debe llamar ITT a un análisis de casos completos sin supuestos.

**Cierre requerido:** protocolo ciego de adjudicación, fuentes independientes, error por brazo, sensibilidad a misclasificación, separación de `D_f^*` y `D_f^{obs}`, contrato Outcome/Value y análisis de missingness/censura/selección. Si no hay identificación puntual, presentar límites o declarar no identificación.

## 5. Consecuencias para los estimandos

1. `ITT_Z` conserva como objeto el efecto de asignación de la política D2, sujeto a aleatorización, interferencia, consistencia y observación válida del resultado.
2. El efecto de la política material (`ψ_B` / `ψ_policy`) no es automáticamente un efecto de accesibilidad focal.
3. `LATE_f` solo tendría interpretación local entre compliers de D2 bajo todos los supuestos IV, para un resultado específico y versiones definidas.
4. `LATE_f` sobre Outcome y `LATE_f` sobre Value son resultados distintos; identificar uno no identifica el otro.
5. Aun identificado, `LATE_f` no equivale a `θ_Af(q_X^*)` poblacional ni a `θ_A(q)` general de C10-D1. No se transporta a D1 ni se agrupa con sus compliers.
6. Si falla exclusión, monotonicidad, consistencia, independencia o interferencia, la conclusión apropiada es efecto de política/paquete, análisis de sensibilidad o no identificación; no un Wald causal nominal.

## 6. Qué puede y qué no puede demostrar una auditoría sintética

Los supuestos IV no se validan empíricamente por el mero hecho de que el analizador recupere un parámetro en un DGP ideal. La suite sintética debe incluir verdad oculta con:
- primera etapa nula, débil y fuerte;
- exclusión satisfecha y violada por cada familia de vías colaterales;
- monotonicidad satisfecha y violada por defiers;
- crossover/provisión de fondo;
- versiones múltiples e incumplimiento;
- interferencia y recursos compartidos;
- error de medición diferencial de `D_f` y Value;
- missingness/censura dependiente de brazo y resultado.

El criterio es que el analizador clasifique correctamente identificación, no identificación, estimando de paquete, incertidumbre débil y límites. No basta que calcule un cociente. Esta propuesta no define todavía parámetros ni tolerancias de esos escenarios.

## 7. Estado consolidado de la auditoría

| Supuesto/objeto | Estado documental | Dictamen |
|---|---|---|
| Tratamiento focal `D_f^*` y población | Parcialmente definido | Falta contrato final de verdad/observación y población elegible |
| Relevancia | Abierta | No hay primera etapa focal observada ni parámetros aprobados |
| Independencia | Condicional | Depende de unidad, esquema de asignación y clúster |
| Exclusión | No demostrada; amenazas materiales | No atribuir ITT a accesibilidad ni interpretar Wald |
| Monotonicidad | Abierta | No demostrada; amenazas por desplazamiento/crowding-out |
| Consistencia/versiones | Abierta | Identidad/hash y cumplimiento operativo pendientes |
| Interferencia | Abierta | Recursos y dependencias compartidas sin mapa cerrado |
| Medición `D_f`/Value | Abierta | Error diferencial, adjudicación y missingness no cerrados |
| Wald/`LATE_f` | NO LISTO / NO IDENTIFICADO | No seleccionar ni reportar como efecto causal |

## 8. Gates mínimos antes de seleccionar Wald

- **IV-G1 — Tratamiento/población:** definir `D_f^*`, `D_f^{obs}`, elegibilidad basal, unidad y versiones.
- **IV-G2 — Primera etapa:** estimar las primeras etapas separadas y fijar inferencia robusta a instrumento débil.
- **IV-G3 — Independencia/interferencia:** cerrar asignación, unidad/clúster, exposición y carryover.
- **IV-G4 — Exclusión:** cerrar inventario de rutas y evidencia de no-afectación o abandonar atribución focal.
- **IV-G5 — Monotonicidad:** justificarla y someterla a escenarios con defiers/crowding-out.
- **IV-G6 — Consistencia/medición:** pin de versiones, adjudicación independiente y error diferencial.
- **IV-G7 — Resultado:** fijar por separado Outcome y Value, horizonte, regla, missingness y estimando.
- **IV-G8 — Recuperación sintética:** demostrar que el analizador distingue LATE identificable de paquete/no identificación bajo verdad oculta adversarial.

El cierre de estos gates no autoriza por sí mismo ejecución: siguen siendo necesarios el cierre del diseño global y la autorización explícita.

## 9. Límites y siguiente operación

Esta auditoría no acepta nuevos parámetros, no cierra DEC-C10-066/067, REC-EST-01…09, XSYNC ni el diseño D2; no modifica C10-D1, TGCV Core, RMA, Matrix, STATUS o claims. No autoriza freeze, implementación, simulación, estimación, adquisición de datos ni ejecución científica.

**Siguiente operación documental:** integrar este dictamen en el maestro, plan y matriz de cierre; después, auditar la definición observacional de `D_f^*` y el protocolo de medición de `A_f^*` frente a los contratos de snapshots, predicados, cobertura y error. Mantener Wald bloqueado hasta que los gates IV estén cerrados.



## 10. Crosswalk operativo IV-G1/G4/G6 ↔ medición trivalente y cobertura U_G (2026-11-06)

**Fuentes enlazadas:** C10-S-MEAS-AUD-001 §§8–10; C10-S-AF-XWALK-001 §§1–6; registro de contratos de prueba §57 (familias TRI-AF/DEP/DF/OBS); identidad/versionado y matching; matriz de cobertura U_G y protocolo de procedencia/adjudicación. Esta sección reconcilia dependencias; no declara gates cerrados.

| Gate IV | Contratos de medición/cobertura que lo soportan | Condición de cierre específica para IV | Estado |
|---|---|---|---|
| IV-G1 Tratamiento/población | MEAS-G1…G5; MEAS-G8; TRI-AF-01…05; TRI-DF-01…06; ID-01…15; SNAP-01…15 | Identidad focal τ2, frontera/unidad/contexto y snapshots comparables; elegibilidad basal pre-Z; fórmula candidata y predicados sin duplicidad; D_f* separado de D_f_obs; unknown/no comparabilidad conservados | ABIERTO / PARCIAL |
| IV-G4 Exclusión | MEAS-G4; U_G rutas focales/alternativas/compartidas/externas/desconocidas; B-M01…15; D2-RES-01/D2-CAP-01/D2-C_INFO y fichas de invariantes | Inventario por unidad/frontera/versión/ventana, cobertura negativa suficiente, rutas desconocidas resueltas o explícitamente acotadas y evaluación de cada vía B→Outcome/Value; invariancia postulada no se etiqueta como demostrada | AMENAZA MATERIAL / NO DEMOSTRADA |
| IV-G6 Consistencia/medición | MEAS-G2…G8; TRI-OBS-01…03; TRI-DF-01…06; contratos de snapshots, adjudicación y truth segregada | Versiones y eventos pinned; adjudicación ciega/independiente especificada; error diferencial y missingness cuantificados o acotados; D_f_obs no sustituye a D_f* sin modelo defendible | ABIERTO |

### 10.1 Regla de propagación para la decisión IV

1. A_f_obs=0 o D_f_obs=0 solo puede usarse si la evidencia negativa es válida, suficiente y de alcance compatible; MISSING, NONE, PARTIAL, unknown o conflicto no son cero.
2. DEP_f_obs=0 exige que todas las rutas del universo declarado estén clasificadas 0 y cobertura COMPLETE; una ruta alternativa confirmada 1 basta para DEP=1; una ruta desconocida material conserva ?.
3. No comparabilidad de identidad, frontera, unidad/contexto, granularidad, catálogo, mapping o snapshots fuerza NOT_COMPARABLE/?; no se calcula apertura focal basal→post como si fuera la misma τ2.
4. Truth DGP queda segregada del analizador. La evaluación de error compara la salida congelada con truth después, nunca la usa para construir la clasificación.
5. Incluso una medición trivalente correctamente especificada no demuestra exclusión, monotonicidad, independencia ni ausencia de interferencia. Esos supuestos conservan gates propios.

**Dictamen:** el crosswalk permite reutilizar la especificación trivalente y U_G, sin crear un catálogo paralelo. No hay inventario material completo, fixtures serializados ni validación ejecutada; IV-G1/G4/G6 permanecen abiertos. LATE_f continúa bloqueado.



## 11. Auditoría adversarial de exclusión por superficies B-M01…15 — Opción A (2026-11-06)

**Base documental:** inventario B-M01…15 y reglas de adjudicación de la Closure Control Matrix §§31–31.1; crosswalk A_f*; DGP temporal/roles; contratos PROV; U_G y snapshots. **Estado:** auditoría conceptual asistida, no revisión independiente, sin inventario material ni evidencia empírica. Las superficies son dominios de inspección; no se afirma que B las modifique realmente.

### 11.1 Regla de decisión

Para D2, la exclusión IV exige que Z/B no afecte Outcome/Value por una vía que evite el tratamiento focal definido como apertura estructural D_f* (o el tratamiento focal que se fije finalmente), una vez fijados población, versiones, horizonte y régimen. Una modificación que forme parte de la definición constitutiva de A_f* no es automáticamente una violación; pero si cambia otro predicado, otra transformación, aplicabilidad, conocimiento, ejecución, coste, riesgo, medición o resultado fuera del tratamiento focal, no puede atribuirse a D_f* sin estrategia adicional.

Clasificaciones de esta sección:
- **Focal admisible condicional:** parte del mecanismo que abre τ2 y queda íntegramente capturada por D_f*/A_f*; exige no ampliar el tratamiento después de observar resultados.
- **Colateral amenazante:** posible vía B→otra condición/Reach/selección/ejecución/Outcome/Value no mediada por D_f*.
- **Epistémica/medición:** cambia lo observado, adjudicado o perdido, no necesariamente el estado del sistema; puede sesgar IV/ITT por error o selección.
- **Residual/interferencia:** persiste tras B o afecta otras unidades/periodos.
- **Control de integridad:** superficie que no debe formar parte de B; cualquier cambio invalida comparabilidad del resultado o de la medición.

Una fila en la tabla expresa una posibilidad causal que debe probarse/refutarse, no un efecto constatado. La ausencia de diff en una fuente parcial no acredita invariancia. Se requiere evidencia positiva de cobertura y alcance; unknown material permanece ?.

### 11.2 Crosswalk adversarial de las quince superficies

| Superficie | Vía que debe someterse a prueba | Clasificación para exclusión | Evidencia mínima y falsador relevante |
|---|---|---|---|
| B-M01 Artefacto/versión | B→artefacto/configuración→C_dep*→A_f* (focal); funcionalidad, permisos, seguridad o rutas extra no previstas→Outcome/Value (directa) | Focal admisible solo si artefacto y contenido quedan restringidos al contrato; resto colateral | Manifiesto/SBOM, firma, hashes y diff de contenido/funciones, procedencia, snapshots y consumidores. Falsador: funcionalidad/permiso/ruta adicional o dependencia transitiva no declarada. |
| B-M02 Runtime | B→runtime/aislamiento/cuotas→C_dep*; también recursos, seguridad, latencia o dependencias compartidas→Reach/Exec/Outcome | Mixta: focal + colateral/interferencia posible | Imagen/hash/configuración, cuotas, llamadas, grafo transitivo, consumidores, métricas de carga/seguridad y snapshots. Falsador: cambios en capacidad, latencia, seguridad o servicios fuera de τ2. |
| B-M03 Host | B→paquetes/SO/servicios/variables→compatibilidad o rutas A1/A2, seguridad y Reach | Colateral amenazante, salvo componente estrictamente necesario y declarado en τ2 | Diff completo pre/post, grafo de host y dependencias, consumidores A1/A2, pruebas funcionales y seguridad. Falsador: cambio en alternativa, servicio compartido o condición no focal. |
| B-M04 Interfaz | B→endpoint/API/ACL técnica→relación focal/REL; canal compartido, latencia o ruta adicional→otras transformaciones/resultados | Focal admisible + colateral posible | Contrato API/schema, ACL/puertos, grafo de llamadas y consumidores, pruebas de latencia/errores y cambios de rutas. Falsador: canal compartido alterado, autorización funcional ampliada o nueva ruta no focal. |
| B-M05 Permisos | B→ACL/credenciales técnicas→C_dep*; posible B→C_auth,base→A_f* si cambia autorización normativa funcional | Invariante basal requerida; violación material si cambia C_auth,base | Fuente normativa, titular/alcance/vigencia y diff de ACL, roles, tokens y permisos por unidad/actor/τ2/ventana. Falsador: autorización funcional diferencial; separar credencial técnica de permiso normativo. |
| B-M06 Datos | B→datos/configuración/estado X/F*→App_f/ejecución/Outcome, o altera el objeto que se evalúa | Colateral directo; potencial cambio constitutivo solo si pertenece a la definición fijada antes | Hashes/snapshots de fuente y destino, mapping, metadatos, estado S0, F* y prueba ciega de equivalencia. Falsador: datos de entrada, estado o conformidad cambian por B sin quedar capturados por D_f*. |
| B-M07 Recursos | B→reservas/cuotas/colas/capacidad→R_access* o C_dep*; desplazamiento/saturación de A1/A2/F2→Reach/Exec/Outcome; pool compartido→spillover | Colateral e interferencia; constitutivo solo para disponibilidad ex ante necesaria y no duplicada dentro de A_f* | Capacidad utilizable, K_required, reservas/compromisos, demanda, consumo B, consumidores, ventanas y snapshots. Falsador: reducción o redistribución de recursos no focales, saturación o spillover. |
| B-M08 Red | B→DNS/proxy/firewall/rutas/puertos→REL/DEP focal; cambios topológicos→rutas alternativas, Reach y seguridad | Mixta: focal + colateral/rutas alternativas | Diff topológico y reglas, grafo transitivo, dependencias externas/compartidas, consumidores y pruebas de rutas. Falsador: apertura/cierre de ruta distinta de τ2 o cobertura de red incompleta. |
| B-M09 Seguridad | B→sandbox/certificados/bloqueos→A_f*; riesgo, superficie de ataque, coste o exposición→Outcome/Value | Mixta: constitutiva si bloquea τ2; colateral directa si cambia riesgo/coste/seguridad más allá de τ2 | Configuración y revisión de seguridad pre/post, vulnerabilidades, incidentes, permisos, coste/riesgo y adjudicación independiente. Falsador: riesgo/coste diferencial no incluido en D_f*. |
| B-M10 Observabilidad | B→manuales/formación/avisos→K→consideración/selección/Exec; B→logs/telemetría/permisos→E_T, A_f_obs, Outcome/Value observados | Epistémica y mediación/colateral de conocimiento; no es accesibilidad estructural por sí misma | Contenido/destinatarios/timestamps, exposición por brazo, permisos, esquema, retención, cobertura, missingness y ceguera. Falsador: comunicación diferencial o observación/adjudicación/retención diferencial. No ajustar automáticamente por K post-Z. |
| B-M11 Estado | B→cachés/registros/índices/estado persistente→App, relaciones o rutas alternativas; residuos tras retirada | Colateral residual y amenaza a consistencia/carryover | Inventario de estado, snapshots pre/post/rollback, diffs, consumidores y pruebas de restauración. Falsador: estado residual, caché o ruta modificada que persiste o contamina otra unidad/periodo. |
| B-M12 Rendimiento | B→latencia/throughput/prioridad/contención/disponibilidad→factibilidad temporal, calidad, coste, Exec, Outcome/Value | Colateral directa e interferencia potencial | Medición comparable por unidad/brazo/ventana, perfil de carga, colas, margen, disponibilidad y métricas de A1/A2. Falsador: degradación/mejora diferencial fuera de la apertura focal o contención compartida. |
| B-M13 Oráculo | B→F*/dataset/validador/regla→clasificación o definición de Outcome | Control de integridad; cambio prohibido dentro de B | Hash/version inmutable, separación de roles, ceguera, snapshots y registro de adjudicación. Falsador: oráculo/regla/dataset diferencial; invalida comparabilidad del resultado, no es un mecanismo admisible de accesibilidad. |
| B-M14 Alternativas | B→A1/A2/exportador/importador/formato/dependencias/recursos→F_alt→Reach/Exec/Outcome | Colateral directa crítica para exclusión | Catálogo/grafo completo, pruebas funcionales pre/post, recursos/permisos y margen de equivalencia preespecificado. Falsador: alternativa habilitada, degradada o eliminada por B; un cambio así convierte el contraste en paquete. |
| B-M15 Reversibilidad | B→rollback/residuos/dependencias/permisos/recursos→exposición posterior, carryover e interferencia | Residual/interferencia y amenaza a consistencia | Snapshots S_preB/S_postB/S_rollback/S_routeA, diff, pruebas de restauración, ventanas y unidades afectadas. Falsador: rollback incompleto, residuos o spillover entre periodos/unidades. |

### 11.3 Síntesis por clase causal

1. **Ruta focal potencialmente compatible con exclusión:** B-M01/B-M02/B-M04/B-M08/B-M09 solo en la parte estrictamente necesaria para habilitar τ2 y capturada por la definición preespecificada de D_f*. No basta con etiquetar la modificación como técnica: cualquier función adicional, seguridad, coste, ruta alternativa o recurso compartido abre una vía colateral.
2. **Amenazas directas prioritarias:** B-M06 (datos/estado/aplicabilidad/F*), B-M07 (recursos y desplazamiento), B-M09 (riesgo/coste), B-M11 (estado residual), B-M12 (rendimiento) y B-M14 (alternativas). Pueden afectar Reach, ejecución, Outcome o Value sin pasar por D_f*.
3. **Amenazas de medición/conocimiento:** B-M10 y B-M13. B-M10 puede cambiar selección/ejecución mediante K y puede cambiar la observación; B-M13 no debe ser manipulado por B. Si cambia el proceso de observación o el criterio de Outcome, el contraste medido deja de ser comparable.
4. **Amenazas de consistencia/interferencia:** B-M02/B-M03/B-M07/B-M08/B-M11/B-M12/B-M14/B-M15 requieren identificar recursos, dependencias, consumidores, unidades, periodos y carryover. La aleatorización individual no resuelve spillovers por sí sola.
5. **B-M05:** la autorización normativa funcional basal se mantiene común e invariante por contrato. Permisos técnicos de provisión no son equivalentes a autorización funcional. Si esta última cambia, se viola el aislamiento previsto.

### 11.4 Regla de evidencia para sostener exclusión

Para cada superficie y unidad/versión/ventana, el dossier debe registrar: (a) componente real y frontera; (b) nodos/aristas y consumidores; (c) snapshot pre-B/post-B/rollback; (d) diff y cobertura positiva/negativa; (e) medida independiente de la vía causal y resultado al que podría llegar; (f) exposición de otras unidades/periodos; (g) adjudicación ciega; (h) falsador y estado 1/0/? con procedencia. La etiqueta «no cambia» requiere evidencia con alcance suficiente; ausencia de logs, inventario incompleto o búsqueda sin denominador conserva ?. No basta un contrato declarativo de invariancia.

La auditoría de exclusión debe incluir resultados separados para Outcome y Value. Si una vía llega a Outcome y luego a Value, debe representarse explícitamente; si llega directamente a Value (p. ej., coste/riesgo/recursos), no puede asumirse mediación completa por Outcome. No ajustar mecánicamente por mediadores postratamiento para fabricar exclusión.

### 11.5 Dictamen y consecuencias

**Dictamen actual:** exclusión **NO DEMOSTRADA; amenazas materiales abiertas**. El inventario de B-M01…15 permite localizar amenazas y especificar pruebas, pero no contiene observaciones materiales ni evidencia de no-afectación. No se puede declarar que D2 identifica LATE_f. El ITT_Z sigue siendo el efecto de asignación de la política D2, condicionado a validez de asignación, interferencia, consistencia y observación del resultado; si hay vías no focales, su lectura es de política/paquete. No se reabre DEC-C10-066/067.

**Resultado adversarial que debe poder recuperar el analizador:** (i) solo modificación focal capturada por D_f* y sin vías laterales; (ii) una vía directa a Outcome; (iii) vía directa a Value sin pasar por Outcome; (iv) alternativa A1/A2 modificada; (v) recursos/rendimiento compartidos con spillover; (vi) conocimiento/medición diferencial; (vii) cambio de oráculo; (viii) residuo/rollback/carryover. Salida esperada: LATE_f solo en (i) si los demás supuestos IV se cumplen; efecto de política/paquete o no identificación en los restantes según el estimando y la evidencia. No se fijan parámetros ni tasas.

No hay inventario material, fixtures serializados, pruebas ejecutadas ni revisión independiente. No se cierra IV-G4, no se aprueba exclusión, no se habilita Wald y no se autoriza implementación/ejecución.

## 12. Especificación causal adversarial del DGP Opción A — escenarios cualitativos (2026-11-06)

**Propósito:** convertir el dictamen de §11 en escenarios discriminantes para el DGP Opción A (migración de configuración entre entornos software), reutilizando R0–R3, EXC-F0 y EXC-B01…15. Esta sección especifica estructuras causales y salidas esperadas; no fija parámetros, tasas, distribuciones, umbrales ni fixtures. No declara identificado ningún efecto.

### 12.1 Contrato funcional común del microdominio

- S0: configuración fuente; S2: estado/configuración intermedia tras la transformación focal; SF: configuración objetivo en entorno destino.
- F1 = τ2: conversión de S0 a S2 mediante adaptador focal. B puede provisionar/configurar el adaptador, pero no ejecuta F1.
- F2: aplicación y validación de S2 en SF. B tampoco ejecuta F2.
- A1: exportación de S0 a formato neutral preexistente; A2: importación/aplicación y validación desde formato neutral a SF. A1→A2 es la ruta alternativa candidata, no debe suponerse funcionalmente equivalente sin F* y contrato versionados.
- F*: criterio funcional común de conformidad técnica (esquema, integridad y compatibilidad) fijado antes de Z y separado del oráculo de medición. Las definiciones concretas siguen pendientes.
- D_f*: apertura verdadera basal→post de la accesibilidad focal de F1, no éxito de F1, aplicación F2, Reach(SF), selección ni ejecución. D_f_obs es su clasificación observada y no sustituye a truth.

La apertura de F1 no implica por sí sola Reach(SF): F2 debe ser accesible, aplicable y componible. Una alternativa estable A1→A2 puede mantener Reach(SF)=1 sin que F1 esté abierta. Esta circunstancia no viola por sí sola exclusión: puede generar efecto nulo o heterogéneo de D_f* sobre O/V.

### 12.2 Familias mínimas de escenarios causales

| ID/familia | Modificación estructural de B en el DGP | Ruta causal verdadera | Dictamen que debe emitir el analizador |
|---|---|---|---|
| EXC-F0 / R0 focal exclusiva | B solo provisiona el adaptador necesario para abrir F1; F2, A1/A2, F*, datos, autorización, recursos no focales, coste/riesgo, K y medición permanecen invariantes | Z→B→D_f*→Reach/Π→selección→Exec→O→V; no existe otra ruta Z/B→O/V | LATE_f solo es candidato si relevancia focal, independencia, monotonicidad, consistencia, no interferencia y medición válida también se sostienen. Reportar O y V por separado. |
| R1 alternativa basal estable | F1 puede abrirse por B, pero A1→A2 ya es factible y no cambia por B | Z→D_f*; A1→A2 permanece basal e invariante. El acceso focal puede no alterar Reach(SF), o cambiar opciones/valor solo mediante uso de F1 | No declarar violación de exclusión por la mera existencia de alternativa. Distinguir efecto sobre D_f*, Reach, conjunto de trayectorias y O/V; reportar heterogeneidad y posible efecto nulo. |
| EXC-B06 / vía directa a Outcome | B altera datos fuente/destino, mapping, S0, aplicabilidad o conformidad F* fuera de D_f* | Z→B→datos/App/F*→Exec/O (y eventualmente V), sin pasar por D_f* | Exclusión focal violada; no etiquetar Wald como LATE_f. ITT_Z puede seguir siendo efecto de política si diseño, consistencia, interferencia y medición del resultado son válidos. |
| EXC-B09/B12 / vía directa a Value | B cambia seguridad, exposición, latencia, rendimiento, coste o consumo de recursos que entra en Value aunque O permanezca igual | Z→B→riesgo/coste/recursos→V; posible Z→B→rendimiento→O→V en paralelo | No inferir mediación completa O→V. LATE_f focal no identificado bajo exclusión violada; informar ITT_V como efecto de política si V es comparable y medido válidamente. |
| EXC-B14 / alternativa modificada (R2) | B habilita, degrada o elimina A1/A2, o altera sus dependencias/recursos | Z→B→A1/A2→Reach/Π/Exec→O/V, además o en lugar de D_f* | Efecto de paquete; no atribuir a D_f*. Comparar R2 con R1 y mantener alternativas como ruta separada. |
| EXC-B07/B02/B03/B12 / recursos compartidos | B consume, reserva, desplaza o congestiona recursos/runtime/host/colas que sirven a F2, A1/A2 u otras unidades | Z_i→B_i→R_pool/latencia→Reach/Exec/O/V de i y/o j≠i | Interferencia/carryover potencial. El ITT individual y Wald individual no se interpretan con SUTVA; exigir mapa de exposición o asignación/análisis por clúster. |
| EXC-B10 / conocimiento diferencial | B entrega formación, avisos o instrucciones que cambian K, consideración, selección o inicio independientemente de D_f* | Z→B→K→Consider→Sel→Start→Exec→O/V | Vía no focal que viola exclusión para D_f*. No ajustar mecánicamente por K post-Z; tratar como efecto de política/paquete o diseñar intervención separada. |
| EXC-B10/OBS / medición diferencial | B cambia logs, telemetría, permisos, retención, cobertura o adjudicación sin cambiar necesariamente el estado verdadero | Z→B→E_T/observación/missingness→O_obs/V_obs y D_f_obs | No es por sí sola una vía causal sobre O*/V*, pero invalida o sesga estimación observada si el error es diferencial/no identificado. Separar exclusión estructural de IV-G6/medición. |
| EXC-B13 / oráculo alterado | B cambia F*, dataset, validador o regla de clasificación/resultado | Z→B→regla de medición/definición→O_obs/V_obs; el constructo medido difiere por brazo | Resultado no comparable; invalidar interpretación causal común. No reinterpretar el cambio del oráculo como accesibilidad. |
| EXC-B11/B15 / residuo y carryover | Estado, caché, índice, permiso o dependencia persiste tras rollback o contamina otra unidad/periodo | B_t→estado residual_(t+1)→exposición/Reach/Exec/O/V posteriores | Consistencia temporal e interferencia comprometidas; exigir snapshots y mapa de exposición. No Wald estándar. |
| R3 / intento o provisión fallida | W_attempt ocurre pero C_dep* no se satisface y no hay apertura focal; considerar por separado si el intento consume recursos o deja residuos | Z→B→W_attempt; no llega a C_dep*/D_f*. Si consume recursos/residuos, añadir vía colateral específica | Primera etapa focal nula/débil: no relevancia o instrumento débil, no LATE_f. Si hay coste/residuo, además efecto de paquete/interferencia; no asumir ITT nulo. |

### 12.3 Separación de dictámenes por resultado y mecanismo

El generador debe conservar al menos cuatro objetos distintos: (a) potenciales de D_f*; (b) potenciales de Reach_H/trayectorias/ejecución; (c) O* y su medición O_obs; (d) V* y su medición V_obs. No se permite inferir que una vía a O es también la única vía a V, ni que ausencia de efecto sobre O implica ausencia de efecto sobre V.

La salida analítica distingue: LATE_f identificado condicionalmente; ITT_Z como efecto de asignación de política; efecto de paquete cuando B actúa por múltiples componentes; instrumento irrelevante/débil; interferencia; resultado no comparable; error de medición/missingness no identificado; y NOT_IDENTIFIED. Estas categorías no son mutuamente excluyentes: el reporte debe indicar el estimando y el gate que falla.

### 12.4 Reglas de comparación y no identificación

1. EXC-F0 es un control positivo de atribución focal, no el escenario por defecto ni una demostración de exclusión real.
2. R1 es un control de discriminación: alternativa basal estable no equivale a vía colateral inducida por B. Puede bloquear efecto sobre Reach sin bloquear por ello la identificación del efecto local de D_f* sobre un resultado que sí responda al tratamiento.
3. R2 debe manipular únicamente la alternativa especificada para aislar la violación; otros mecanismos se mantienen invariantes en ese contraste conceptual.
4. La vía directa a Value se prueba con O* constante y V* sensible al coste/riesgo/recursos; la vía a Outcome se prueba separadamente. No se imponen magnitudes.
5. La manipulación epistémica/medición se mantiene separada de la manipulación del estado verdadero; el analizador no recibe hidden_truth.
6. Los escenarios de recursos compartidos y carryover cambian explícitamente el mapa de exposición/unidad; no se etiquetan como simple violación de exclusión individual si el problema adicional es interferencia.
7. Si la evidencia observada no distingue entre F0 y una vía colateral, el resultado correcto es indeterminado/no identificado, no selección del escenario más favorable.

**Estado:** especificación causal cualitativa propuesta; sin parámetros, tasas, distribuciones, fixtures serializados, oráculos ejecutables o pruebas. IV-G4 permanece abierto; relevancia, monotonicidad, independencia, consistencia, interferencia y medición conservan gates propios. No se habilita Wald, freeze, implementación ni ejecución.



## 13. Crosswalk variable×tiempo×rol de escenarios Opción A

Se incorpora el contrato temporal C10-S DGP §28 como mapa de implementación documental. Se conserva el reloj t−1/t0–t9/t+1… y la separación Generador/Analizador/Evaluador. El mapa no añade parámetros ni supone que las manipulaciones estén materialmente observadas.

| Familia | Tiempo focal | Variables principales | Truth oculta al analizador | Observación disponible al analizador | Gate/dictamen |
|---|---|---|---|---|---|
| R0/EXC-F0 | t1–t4; resultados t8/t9 | B/W (t1), C_dep (t2), A_f*/D_f*/ΔT_acc* (t3), Reach/Π (t4), O/V (t8/t9) | D_f*, ausencia de vías colaterales, potenciales O*/V* | Asignación, intento, snapshots/evidencia, A_f,obs, Reach/Π obs, O_obs/V_obs | Control positivo; LATE_f solo condicional |
| R1 | t−1 y t2–t4 | F_alt,base, A1/A2 y dependencias | Factibilidad basal y ausencia de modificación por B | Inventario/snapshots y cobertura trivalente | No violación por alternativa basal; efecto sobre Reach puede ser nulo |
| R2/EXC-B14 | t2–t4, t7–t9 | Cambio A1/A2/dependencias, Reach, ejecución y resultados | Ruta colateral inducida por B | Diffs/snapshots, mapa de rutas, O_obs/V_obs | Exclusión focal violada; paquete/no LATE_f |
| R3 | t1–t3 y t+1 | W_attempt, C_dep, D_f*, consumo/residuo | Fallo de provisión y primera etapa focal verdadera | Intento y verificación; recursos/residuos observables | No relevancia/débil; posible coste/carryover |
| Directa a O | t2/t7/t8 | Datos/S0/mapping/App/F* técnico, Exec, O | Ruta B→O no mediada por D_f* | Diffs, registros de ejecución y O_obs | IV-G4 falla |
| Directa a V | t2/t7/t9 | Coste/riesgo/recursos, O* constante y V* afectado en subcaso aislado | O* constante y V* afectado en subcaso aislado | Costes/riesgos medidos, O_obs/V_obs | IV-G4 falla para V; ITT_V política puede ser estimable |
| K diferencial | t1/t5/t6/t7 | Mensajes, K, Consider, Sel, Start, Exec | Efecto de B sobre K y conducta | Comunicaciones y registros conductuales | Vía epistémica; no ajustar por K post-Z |
| Medición diferencial | t2/t3/t8/t9 | ΔE_T, cobertura, R_A/R_O/R_V | Truth fija; missingness/error inducido por B | Logs, cobertura, adjudicación y ausencia por brazo | IV-G6; sensibilidad/cotas o no identificación |
| Oráculo diferencial | t8/t9 | Versión de regla/dataset/oráculo | Cambio de definición por brazo | Especificación y versión accesible | Resultado no comparable |
| Recursos compartidos | t1/t2/t4/t7–t9 | Pool, reservas, consumo, exposición i←j | Spillover entre unidades | Mapa de exposición y métricas del pool | IV-INT; cluster/exposure model o no identificación |
| Carryover | t+1… | Estado residual, rollback, recursos/exposición futura | Persistencia entre periodos/unidades | Snapshots longitudinales y rollback | Consistencia/interferencia; no Wald individual estándar |

La observabilidad de una variable no la convierte en verdad estructural. O_obs y V_obs no reemplazan O* y V*; el analizador no recibe truth ni parámetros. El contrato es una especificación de entrada/salida, no evidencia de validez de supuestos en un sistema externo.

**Estado:** crosswalk añadido; IV-G4/IV-G6/IV-INT continúan abiertos. No se parametriza ni ejecuta.


---

## 14. Correspondencia entre las políticas materiales D2 y las políticas estocásticas g sobre accesibilidad (2026-11-09)

**Estado:** reconciliación causal documental; mapping no identificado ni aprobado. Esta sección desarrolla XSYNC-138-01 residual y no modifica DEC-C10-066/067, C10-D1 ni la jerarquía de estimandos.

### 14.1. Objetos distintos

Se deben mantener separados:

1. **Asignación:** Z.
2. **Política material D2:** B_g0^D2 o B_g1^D2, definidas por DEC-C10-067. B_g0 no programa/inicia por política un intento focal; B_g1 programa un intento estandarizado de provisión técnica focal. Ninguna política ejecuta F1/F2/A1/A2.
3. **Respuesta de provisión:** W_programmed, W_attempt, recepción, C_dep*, cada uno con su propio estado y tiempo.
4. **Respuesta de accesibilidad:** ΔT_acc* completo y su proyección focal A_f*=h_f(ΔT_acc*); no se sustituyen por C_dep*, D_f* ni por el intento.
5. **Política causal de accesibilidad g_j:** régimen estocástico sobre cambios de accesibilidad, condicionado por historia/contexto y restringido al conjunto factible, según C10-D1 §26. No es el nombre alternativo de B_gj^D2.

### 14.2. Mapping inducido que debe demostrarse

Para cada política material b_j^D2 y cada historia/contexto h compatible con el régimen común q, el objeto a reconstruir es la distribución inducida:

g_j^ind(a | h; q) := P(ΔT_acc*=a | do(B=b_j^D2), H=h, q),

y, para el contraste focal IV, la distribución correspondiente de D_f* o A_f* bajo la definición/versionado basal→post. La expresión es un objetivo de mapping, no una distribución observada ni una afirmación de identificación.

La correspondencia requiere, como mínimo:
- intervención B versionada y físicamente realizable, con actor, artefacto, alcance, tiempo y desviaciones;
- mecanismo completo B→W→C_dep*→A_f*/D_f*→ΔT_acc*, sin colapsar etapas;
- medición independiente de ΔT_acc* completo y de su proyección focal, con verdad y observación separadas;
- compatibilidad con estado, condiciones constitutivas, historia y conjunto de transformaciones factibles;
- soporte/positividad de las políticas inducidas dentro de cada estrato/historia objetivo;
- consistencia y equivalencia de versiones defendibles;
- especificación de recursos compartidos, interferencia, crossover, provisión de fondo y carryover;
- inventario y adjudicación de todas las vías B→Outcome/Value que no pasan por ΔT_acc* o por la proyección focal declarada.

No basta observar P(A_f_obs|Z), una primera etapa en C_dep*, ni una diferencia media de D_f_obs. Tampoco se infiere g_j^ind a partir de tasas de intento/instalación. La medición de accesibilidad no puede definirse mediante selección, ejecución, Outcome o Value.

### 14.3. Condición de equivalencia entre B y g

B_g0^D2/B_g1^D2 podrían inducir dos distribuciones candidatas g_0^ind/g_1^ind, pero eso no establece que el contraste material sea θ_A(q). Para interpretarlo como contraste específico de accesibilidad deben cumplirse simultáneamente:

(a) ambas distribuciones están definidas bajo el mismo régimen q, población, historia, versión de τ y regla Value;

(b) la diferencia relevante entre políticas queda representada por el cambio estructurado ΔT_acc* (o por la proyección focal cuando el estimando sea explícitamente focal);

(c) cualquier efecto de B sobre otras condiciones, conocimiento, selección, ejecución, Outcome, Value, medición o rutas alternativas está ausente, contenido en la definición causal de A, o separado por un diseño/estimando identificable;

(d) las versiones de B que inducen el mismo A son equivalentes para el estimando, o sus diferencias directas se modelan y separan;

(e) la factibilidad y el soporte de ambas políticas se sostienen para la población objetivo.

Si estas condiciones no se sostienen, el contraste identificado por Z es ITT de asignación a B_g^D2 y, bajo consistencia, puede interpretarse como efecto de la política/paquete material. No debe renombrarse como θ_A(q), efecto de ΔT_acc* ni LATE_f.

### 14.4. Exclusión focal frente a atribución sobre ΔT_acc completo

La exclusión de IV-G4 es relativa al tratamiento focal D_f*. No debe confundirse con una prueba suficiente de atribución al constructo completo ΔT_acc*. Incluso si una vía está mediada por otro componente de ΔT_acc* distinto de la proyección focal, puede violar la exclusión para D_f* y, a la vez, ser parte del efecto del objeto transformacional completo si el estimando y la intervención están definidos sobre ese objeto.

A la inversa, una vía B→coste/riesgo/recursos/medición/alternativas→Value que no esté representada en ΔT_acc* no se convierte en efecto de accesibilidad por el mero hecho de que B también cambie A_f*. Debe conservarse la clasificación por resultado: vía a Outcome, vía directa a Value con Outcome constante, vía epistémica/medición y vía de interferencia/carryover.

Por tanto:
- ITT_Z^D2: efecto de asignación a política D2, sujeto a los supuestos de diseño y observación.
- ψ_policy^D2: efecto de la política material implementable, con sus vías.
- LATE_f^D2: efecto local focal solo bajo todos los supuestos IV y gates específicos de D_f*.
- θ_A(q): contraste de políticas estocásticas sobre ΔT_acc* bajo q, según C10-D1; no queda identificado por ITT ni por Wald focal.
- θ_Af(q_X*): contraste focal distinto y pendiente de mapping/identificación; no equivale automáticamente a θ_A(q).

### 14.5. Dictamen y gates de cierre

**Dictamen actual: NOT_IDENTIFIED / MAPPING OPEN.** Las políticas D2 están definidas conceptualmente, pero no existe aún una distribución inducida g_j^ind adjudicada ni evidencia para demostrar equivalencia, soporte o exclusión. El inventario B-M01…15 es un mapa de inspección, no evidencia de invariancia o ausencia de vías.

Gates documentales/empíricos que deben cerrarse antes de interpretar D2 como política de accesibilidad:
- MAP-01: versiones, actor, alcance, tiempos y factibilidad de B_g0/B_g1.
- MAP-02: mapping temporal y medido B→W→C_dep*→A_f*/D_f*→ΔT_acc*.
- MAP-03: distribución inducida por historia/contexto y soporte común de g_0^ind/g_1^ind.
- MAP-04: equivalencia de versiones que inducen el mismo ΔT_acc* y separación de diferencias directas.
- MAP-05: cobertura de rutas alternativas/compartidas, recursos, permisos, rendimiento, seguridad y residuos.
- MAP-06: exclusión por separado para Outcome y Value, además de medición diferencial, interferencia y carryover.
- MAP-07: distinción explícita entre estimando focal D_f*/LATE_f y estimando estructurado θ_A(q).

Hasta superar estos gates, mantener el resultado como efecto de asignación/política cuando sea identificable; si los supuestos de ese efecto tampoco se sostienen, declarar no identificación. No calcular Wald como LATE_f ni presentar θ_A(q) como identificado. No se parametriza, implementa ni ejecuta.



### 14.6. Contrato documental MAP-01: identidad y versión de la intervención material

Este contrato operacionaliza el registro conceptual de DEC-C10-067 sin completar por inferencia los datos que esa decisión dejó pendientes. Su función es impedir que una política nominal se confunda con una intervención material reproducible.

**Elementos invariantes ya aceptados**
- B_g0^D2: mantener la configuración basal asignada; no programar ni iniciar por política el intento focal; no desplegar/configurar el adaptador como parte de la intervención.
- B_g1^D2: programar un intento estandarizado de provisión de la dependencia focal, usando artefacto y versión identificados antes de la asignación; habilitar el canal técnico requerido sin alterar autorización normativa basal.
- Ninguna política ejecuta F1/F2/A1/A2 ni aplica una transformación funcional.
- C_auth,base=1, elegibilidad, τ2, condiciones basales no focales y protocolo/oráculo de medición permanecen comunes conforme a DEC-C10-067.
- La provisión de fondo/crossover en B_g0 se registra como exposición recibida, nunca como cambio retrospectivo de asignación.

**Registro mínimo por unidad y asignación**
Cada registro futuro deberá contener:
1. unit_id, eligibility_record_id, Z, policy_id, policy_version, assignment_time;
2. actor_id, actor_role, authorization_scope, actor_action_time;
3. artifact_id, artifact_version, artifact_hash, signature_or_integrity_evidence, runtime_id/version, endpoint_or_channel_id/version;
4. planned_attempt_id, planned_window_start/end, actual_attempt_id, attempt_start/end;
5. receipt_id, receipt_time, received_artifact_hash, acceptance_protocol_version, acceptance_result;
6. retry_parent_id, retry_number, failure_code, partial_state, rollback_id/time/result, deviation_id;
7. background_provision_detected, detection_method, coverage_window, evidence_ref;
8. resource_profile_id, permission_diff_ref, network_diff_ref, snapshot_preB_ref, snapshot_postB_ref, snapshot_rollback_ref.

Los valores concretos de identidad/rol, artefacto, hash, runtime, endpoint, ventanas, protocolo de recepción, número/regla de reintentos, rollback y detección de provisión de fondo siguen NOT SPECIFIED / NOT INVENTORIED. Este esquema define campos necesarios; no los rellena ni selecciona ARCH-B1/B2/B3.

**Reglas de adjudicación**
- W_programmed se adjudica desde el registro de programación de la política, no desde el intento observado.
- W_attempt exige evidencia de inicio efectivo; la programación no lo prueba.
- Recepción exige evidencia del artefacto recibido y su integridad; no se infiere de intento.
- Reintentos son eventos separados vinculados al intento raíz; no se colapsan en éxito único ni se elige retrospectivamente el mejor.
- Fallo parcial, rollback y desviación conservan sus estados/tiempos y no borran exposición previa.
- En B_g0, cualquier provisión focal detectada es crossover/background provision. Si la cobertura de detección no es suficiente, su ausencia es ? y no 0.
- Las desviaciones se registran por brazo y antes/después de conocer resultados; no se reclasifica el brazo asignado.

**Estado MAP-01:** CONTRACT_FIELDS_DEFINED / MATERIAL VALUES OPEN. El contrato de registro está definido documentalmente; la intervención material reproducible aún no puede congelarse porque faltan datos operativos aceptados y evidencia técnica. No autoriza implementación.

### 14.7. Contrato documental MAP-02: secuencia temporal y medición independiente

La secuencia causal candidata se conserva como orden lógico de estados, no como calendario ya especificado:

baseline/eligibility → Z/B → W_programmed → W_attempt → receipt → S_install → C_dep* → A_f* → D_f* / ΔT_acc*

Cada evento debe registrar unit_id, event_id, event_type, event_time, time_source, window_id, policy_version, artifact_version, observer_or_system_id, evidence_ref, status ∈ {1,0,?}, missingness_reason y deviation_id. Los relojes y ventanas deben sincronizarse y documentarse; cuando solo se conozca un intervalo, se conserva como intervalo, no se inventa un instante.

**Anclas y separación de medición**
- **Basal, antes de Z:** elegibilidad y estado basal de τ2; medición de A_f,0* y de los componentes de ΔT_acc* requeridos para establecer inaccesibilidad focal basal. No se usa información posterior para reconstruir la línea basal.
- **Asignación/provisión:** Z, versión de B, programación, intento, recepción e instalación son exposiciones/eventos separados.
- **Estado técnico postprovisión:** C_dep* se adjudica mediante evidencia separada de instalación, integridad, compatibilidad y operatividad. Cada componente conserva su resultado y evidencia; el compuesto no se completa por imputación de otro componente.
- **Accesibilidad postprovisión, antes de selección/inicio y antes de F1:** adjudicar por separado ID_f*, REL_f*, COND_f*, AUTH_f*, RES_f*, DEP_f* y BLOCK_f*, con evidencia de la unidad y ventana aplicables. La instalación o C_dep* no sustituyen estos predicados. La regla exacta de composición sigue siendo la fórmula candidata §67.3, no aprobada ni congelada.
- **Cambio focal y estructural:** D_f* se adjudica mediante contraste basal→post de la transformación focal bajo su definición/versionado; ΔT_acc* conserva las dimensiones estructurales ΔU*, ΔR*, ΔC*, ΔX*. No introducir ΔE_T como componente estructural: evidencia, cobertura y validez de observación se registran en paralelo.
- **Resultados downstream:** selección, inicio, ejecución, Outcome y Value se registran después y por separado. No se usan para definir A_f*, D_f* ni ΔT_acc*.

**Reglas temporales/epistémicas**
1. Una observación tardía no se retrodata: si la ventana basal/post no permite adjudicación, estado ?.
2. Un estado 0 exige evidencia de ausencia dentro de un universo y ventana con cobertura declarada; la falta de registro es ?.
3. Los predicados se miden con fuentes independientes del asignador/provisionador cuando sea posible; se identifica quién observa y si conoce Z/B.
4. Se conservan verdad DGP y observación como campos distintos; el Analyzer no recibe truth ni potenciales.
5. Medición diferencial, pérdida de seguimiento, censura, contaminación o desalineación temporal se registran como amenazas, no se reparan con inferencia.
6. Si la provisión de fondo en control o el crossover no se puede detectar con cobertura suficiente, MAP-02 no puede sostener ausencia de exposición ni una primera etapa causal limpia.

**Estado MAP-02:** TEMPORAL_SCHEMA_DEFINED / WINDOWS_AND_MEASUREMENT_OPEN. Se ha definido qué eventos y mediciones deben distinguirse; no están fijadas ventanas, fuentes, instrumentos, tolerancias ni evidencias observadas. No se afirma que B→C_dep*→A_f*→D_f* haya ocurrido ni que el mapping esté identificado.

