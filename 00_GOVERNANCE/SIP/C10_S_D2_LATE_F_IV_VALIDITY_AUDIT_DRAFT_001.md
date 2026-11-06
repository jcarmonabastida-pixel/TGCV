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
