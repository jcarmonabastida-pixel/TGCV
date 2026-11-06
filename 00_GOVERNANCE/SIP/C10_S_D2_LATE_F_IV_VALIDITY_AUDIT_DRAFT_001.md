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
