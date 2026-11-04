# C10-S ↔ C10-D1 — Reconciliación de estimandos y resolución propuesta para S4-R
**Documento de decisión metodológica — borrador 001**

**Estado:** DRAFT / PROPUESTA PARA REVISIÓN — NO APROBADO / NO CONGELADO  
**Corte:** 2026-11-04  
**Repositorio canónico:** `jcarmonabastida-pixel/TGCV`  
**Rama:** `research/c10-s-consolidation-draft`  
**Dependencia:** PR #116 (Draft); C10-D1 permanece en PR #115 (Draft).

---

## 1. Dictamen ejecutivo

La lectura cruzada de los textos canónicos confirma una tensión de jerarquía, no una contradicción matemática inevitable:

- C10-D1 define como pregunta científica de atribución el contraste de dos políticas factibles de accesibilidad bajo un régimen común, `θ_A(q)`. Distingue expresamente este objeto del efecto total de la intervención `TE`, del efecto conjunto `θ_{L,A}` y de la interacción.
- C10-S §51 propone como objetivo causal primario de S4-R el ITT de la política aleatorizada de provisión en `P*_τ2`, y como objetivo secundario un LATE focal de accesibilidad mediante IV, si se sostienen los supuestos.
- El propio C10-D1 establece que aleatorizar componentes implementables identifica el efecto de asignación (ITT), pero no identifica automáticamente `θ_A(q)`; si no se separan las vías alternativas, la conclusión debe ser efecto de paquete/conjunto o no identificación.
- C10-S §43.4–43.7 reconoce que ITT, primera etapa, LATE focal, `θ_Af(q*)` poblacional y el efecto general de accesibilidad TGCV son objetos distintos, y deja abiertos la población, el régimen, la identificación poblacional y Value.

**Conclusión:** no debe sustituirse la pregunta científica de C10-D1 por el ITT de S4-R. La arquitectura coherente tiene tres niveles de objeto causal y dos estimadores en S4-R:
1. **Pregunta científica general C10:** `θ_A(q)` para políticas factibles sobre cambios del espacio transformacional accesible, cuando sea identificable.
2. **Contraste focal de política S4-R:** `θ_Af(q*)` entre las dos políticas factibles B_g1/B_g0 que inducen distribuciones de apertura de `τ2`. Si Z aleatoriza esas políticas, el ITT_Z estima el contraste de asignación a las políticas. Solo puede interpretarse como `θ_Af(q*)` si B_g1/B_g0 implementan g1/g0, q* es común, las versiones son consistentes y no hay vías diferenciales hacia Value fuera de la accesibilidad focal.
3. **Efecto local de apertura S4-R:** `LATE_f` entre compliers, estimado por Wald solo bajo supuestos IV. Es distinto del contraste poblacional de políticas `θ_Af(q*)`.
4. **Límite de alcance:** S4-R focaliza `τ2`; no identifica por sí solo el efecto general de `θ_A(q)` sobre el espacio completo `ΔT_acc`.

Esta reconciliación se propone para revisión y no se considera decisión aprobada. No cambia el estimando de C10-D1 ni cierra XSYNC.

## 2. Fuentes canónicas inspeccionadas

| Fuente | Referencia | Contenido utilizado |
|---|---|---|
| C10-D1 | `00_GOVERNANCE/SIP/C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`, blob `bf25f6ec8965166e5fa52ff18e6d07613bad0eb3` | §§5, 17.5–17.9, 24.2, 25.3–25.6, 26.1–26.3, 30, 32–34 |
| C10-S | `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, blob `2b7834c23ff690c8dc5379b02486a0693b32a632` | §§43–51; especialmente §§43.3–43.7 y 51.1–51.8 |
| Auditoría integrada | `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md` | AUD-001…012 |
| Propuesta AUD | `C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md` | `A_f`, `T_acc`, `ΔT_acc`, DGP integrado propuesto |
| Auditoría cruzada | `C10_S_AUD001_AUD002_CROSS_AUDIT_DRAFT_001.md` | XAUD-001…007 |

Los SHA anteriores identifican los blobs inspeccionados. La referencia normativa sigue siendo el contenido actual de GitHub en las ramas correspondientes; cualquier modificación posterior exige actualizar esta trazabilidad.

## 3. Jerarquía de estimandos propuesta

### 3.1 Pregunta científica C10-D1

[
\theta_A(q)=E[V^{q,g_1}]-E[V^{q,g_0}]
]

- `q`: régimen común, explícito, causalmente interpretable y factible de condiciones/historias no constitutivas.
- `g_1,g_0`: políticas implementables que inducen cambios de accesibilidad bajo cada historia y respetan el conjunto factible.
- La respuesta posterior de Reach, Trayectoria, selección, ejecución, Outcome y Value evoluciona bajo cada política.
- El estimando se refiere a población, horizonte, regla de Value y versiones de política concretas.
- No es un efecto indirecto natural, una fracción del efecto total ni una intervención abstracta sobre un índice.
- Si la intervención que induce accesibilidad tiene vías propias hacia Value que no pueden separarse, no se atribuye el efecto a accesibilidad.

### 3.2 Efecto de asignación de S4-R

[
ITT_Z=E[V\mid Z=1]-E[V\mid Z=0]
]

Es el efecto de asignar la política de provisión concreta en `P*_τ2`, bajo el diseño aleatorizado y los supuestos de consistencia, interferencia y observación de Value. Es el estimador de la diferencia entre las políticas asignadas. Si el diseño demuestra que esas políticas solo difieren en la distribución de accesibilidad focal bajo q*, el contraste puede interpretarse como `θ_Af(q*)`; si existen vías directas/colaterales, sigue siendo el efecto de la política/paquete (`ψ_policy`/`TE_Z`) y no `θ_Af`. No es el efecto de recibir la provisión ni el efecto de todo `ΔT_acc`.


### 3.2.1 Condición de atribución del ITT a la política de accesibilidad focal

La igualdad interpretativa que debe probarse es:

`ITT_Z = ψ_policy(B_g1,B_g0)`; y solo bajo exclusión/aislamiento, equivalencia de versiones, régimen común y mapeo válido `B_g → A_f*`, se puede interpretar `ψ_policy = θ_Af(q*)`.

No es una identidad algebraica automática. El analizador debe comprobar en la verdad oculta del DGP:
- las políticas asignadas corresponden a g1/g0 y difieren solo en el componente de provisión focal;
- las condiciones constitutivas y q* tienen distribuciones coherentes y soporte;
- no hay vías B/C_dep→Value ajenas a la apertura de τ2;
- costes, calidad, seguridad, latencia, información y demás efectos no focales son invariantes;
- la medición de A_f* y Value es independiente y temporalmente correcta.

Si una condición falla, reportar ITT_Z como efecto de política/paquete y no como θ_Af(q*). La exclusión no se demuestra solo por aleatorización ni por un control negativo; se justifica por diseño y se somete a escenarios adversariales.


### 3.3 Primera etapa y efecto local focal

[
ITT_{D_f}=E[D_f\mid Z=1]-E[D_f\mid Z=0]
]

[
LATE_f=\frac{ITT_Z}{ITT_{D_f}}
]

La razón Wald solo admite interpretación como efecto causal local de la apertura focal entre compliers bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia y medición adecuada. La inferencia debe ser robusta a instrumento débil. Si la primera etapa es nula, no calcular ni interpretar Wald; si es débil, no usar inferencia convencional como si fuera fuerte.

`LATE_f` no es `ATE`, no es `θ_A(q)` poblacional y no representa el efecto de todo `ΔT_acc`. Si se utiliza `A_f*` en lugar de `D_f`, debe quedar explícito que la población elegible tiene `A_f,base*=0`, de modo que la apertura basal→post sea equivalente al tratamiento focal. Si hay accesibilidad basal, el tratamiento y la primera etapa deben redefinirse, no asumir esa equivalencia.

### 3.4 Efecto de paquete y efecto conjunto

Cuando la provisión `B` cambia accesibilidad y otras condiciones con vías propias hacia Value:
- `ITT_Z` puede seguir identificando el efecto total de asignación al paquete.
- La exclusión IV focal no se sostiene si una vía adicional afecta Value y no forma parte de la definición del tratamiento focal.
- El resultado debe etiquetarse como efecto de política/paquete o, si procede, contraste conjunto `θ_{L,A}`; no como contribución específica de accesibilidad.
- `TE-θ_A(q)` no se presenta como efecto directo ni residual puro.

## 4. Consecuencia para la arquitectura del experimento sintético

Se propone mantener dos preguntas de evaluación separadas en el protocolo C10-S:

**Pregunta de funcionamiento del diseño:** ¿el analizador recupera correctamente el ITT de la política asignada y clasifica los escenarios de provisión, no cumplimiento, pérdida y alternativas?

**Pregunta de atribución focal:** ¿el analizador identifica cuándo la variación de asignación puede usarse como instrumento para apertura de `τ2`, cuándo los supuestos son vulnerados y cuándo la conclusión debe ser LATE local, efecto de paquete o no identificación?

Un resultado PASS en ambas preguntas solo valida la discriminación del protocolo frente al DGP sintético especificado. No demuestra causalidad empírica real ni generaliza de `τ2` a todo `T_acc`.

Para evaluar directamente `θ_A(q)` en el sentido de C10-D1, se necesitaría un diseño sintético adicional con políticas `g_1/g_0` implementables sobre accesibilidad bajo un régimen común factible, soporte de las políticas, versiones y vías alternativas separadas. S4-R no debe afirmar que ya lo identifica.

## 5. Resolución propuesta de la ambigüedad temporal p0=.20 / C_dep,base=0

La revisión de C10-S §§30.2, 30.4–30.5, 31.4 y 32.4–32.5 precisa una distinción importante: **no existe contradicción matemática necesaria** entre `C_dep,base=0` y `p0=.20` si `p0` representa la probabilidad post-asignación de instalación/accesibilidad inducida por la política de provisión de control `B_g0`. El contrato §30.2 define expresamente dos políticas técnicas: `B_g0` con probabilidad objetivo .20 y `B_g1` con .80. Ambas son políticas de provisión, no una comparación entre provisión y ausencia total de provisión.

El problema real es de precisión temporal y de mecanismo:
- `C_dep,base=0`: estado técnico basal antes de asignar Z.
- `W_attempt`: intento de instalación posterior a la asignación.
- `S_install`: éxito del procedimiento de instalación.
- `C_dep,post`: estado final verificado de la dependencia.
- `A_f,base*` y `A_f,post*`: accesibilidad focal antes y después.
- `p_z`: probabilidad final post-asignación inducida por la política `B_gz`, no probabilidad basal ni necesariamente probabilidad de intento.

**DGP-S4R aislado (propuesta principal):**
- Mantener `p0=.20` y `p1=.80` como probabilidades finales objetivo verificadas en la población elegible, bajo `B_g0` y `B_g1`.
- `C_dep,base=0` y `A_f,base*=0` se verifican antes de Z para la población de apertura.
- Ambas ramas reciben una política técnica definida; `B_g0` es la provisión de menor intensidad/probabilidad, no ausencia de provisión.
- El generador separa `W_attempt`, `S_install` y `C_dep,post`; calibra el mecanismo para que las probabilidades finales, no solo los intentos, sean .20/.80.
- La regla de accesibilidad se aplica después de verificar `C_dep,post` y todas las demás condiciones necesarias.
- Se conserva el escenario aislado solo si las dos políticas difieren exclusivamente en la probabilidad de apertura focal y no inducen vías directas diferenciales hacia Value.

**DGP adversarial de contaminación/efectos colaterales:**
- Añade una ruta de cruce/contaminación, una vía alternativa o un efecto lateral (coste, demora, calidad, seguridad, información, etc.) explícitamente modelado.
- El analizador debe conservar ITT de asignación al paquete y rechazar LATE focal cuando la exclusión o consistencia se vulneren.
- No se debe confundir la probabilidad basal con la tasa de apertura en control bajo la política `B_g0`.

Una variante con `p0=0` puede definirse como un diseño distinto de provisión frente a no provisión, pero **no sustituye el DGP principal descrito en §30** ni debe introducirse como corrección automática. Requeriría una versión de control distinta y una nueva verdad analítica.

La verdad ilustrativa `θ_A(q*)=3.6` solo se mantiene si .20/.80 son probabilidades finales de accesibilidad focal, todas las demás condiciones permanecen satisfechas, el efecto de accesibilidad sobre los mecanismos y Value es el especificado y no existen vías directas diferenciales. Si esos valores son probabilidades de intento o de instalación antes de fallos, la verdad debe recalcularse desde el DGP completo.

## 6. Poblaciones y apertura focal

Se propone distinguir:

- `P*_τ2`: población definida antes de asignar `Z), elegible para evaluar la apertura de `τ2`; para el estimando de apertura, requiere `A_f,base*=0` y condiciones basales observables/suficientes. No excluye automáticamente alternativas funcionales distintas.
- `P*_F`: subconjunto basal sin alternativa funcional substituible para la función `F*), definido por una auditoría independiente y ciega a `Z), selección, ejecución, Outcome y Value.
- `P*_τ2\setminus P*_F`: unidades con alternativa funcional basal; permanecen en el ITT focal de `τ2` si cumplen elegibilidad, pero permiten estudiar heterogeneidad y sustitución funcional.

La elegibilidad no puede depender de variables post-asignación. Si no se puede verificar `A_f,base*=0` sin error importante, conservar estados indeterminados y definir análisis de sensibilidad; no forzar su clasificación como cero.

La definición final de `F*`, equivalencia funcional, horizonte y criterio de substituibilidad continúa abierta y debe quedar fijada antes de usar el subgrupo como confirmatorio.

## 7. Condiciones de interpretación IV y reglas de salida

| Condición | Resultado del analizador |
|---|---|
| Primera etapa claramente positiva + supuestos IV defendibles en el DGP + medición adecuada | LATE focal, con población de compliers y límites explícitos |
| Primera etapa nula | No Wald; no identificación focal por ese instrumento |
| Primera etapa débil | Inferencia robusta a instrumento débil; si la precisión no permite conclusión, INDETERMINATE |
| Exclusión violada por vía alternativa B→Value | Rechazar LATE focal; mantener ITT del paquete |
| Monotonicidad violada | Rechazar interpretación LATE estándar; informar incumplimiento del supuesto |
| Versiones incompatibles/consistencia fallida | No agrupar como un único tratamiento; efecto de política/versión o no identificación |
| Interferencia relevante no modelada | No usar estimandos individuales convencionales; rediseñar unidad/exposición |
| Error de medición diferencial no corregido | No interpretar primera etapa/Wald como efecto de acceso verdadero |
| Pérdida/selección no tratada | No sustituir población asignada por casos completos; usar límites/sensibilidad o no identificación |
| Alternativa funcional afectada por B | Tratar como paquete o diseñar separación factorial; no atribuir a `τ2` por IV simple |

La exclusión no es verificable de forma concluyente solo con los datos observados. En C10-S se puede probar si el analizador detecta violaciones introducidas en la verdad oculta del DGP. En un estudio real se requiere justificación sustantiva, diseño y sensibilidad; un control negativo no demuestra exclusión.

## 8. Decisiones que se proponen para armonización

| ID | Propuesta | Motivo | Estado |
|---|---|---|---|
| REC-EST-01 | Mantener `θ_A(q)` como pregunta científica C10-D1; no reemplazarla por ITT | Preserva el objeto causal de C10 | Propuesta |
| REC-EST-02 | Mantener ITT_Z como objetivo primario del diseño aleatorizado S4-R | Es el efecto identificado directamente por asignación | Propuesta |
| REC-EST-03 | Mantener LATE_f como objetivo secundario de atribución local, condicionado a IV | Evita convertir ITT en efecto de accesibilidad | Propuesta |
| REC-EST-04 | Declarar explícitamente que S4-R no identifica el `θ_A(q)` general ni el efecto de todo `ΔT_acc` | Alcance del tratamiento focal `τ2` | Propuesta |
| REC-EST-05 | Separar DGP aislado principal (`p0=.20`, `p1=.80` finales) de DGP-CONTAMINATION (`p0>0)) | Elimina contradicción temporal y hace observable el mecanismo de contaminación | Propuesta |
| REC-EST-06 | Definir `P*_τ2` con elegibilidad basal preasignación y `A_f,base*=0` para el contraste de apertura | Hace coherentes D_f y A_f,post* | Propuesta |
| REC-EST-07 | Mantener `P*_F` como subpoblación funcional basal, no como filtro automático de `P*_τ2` | Distingue apertura focal y exclusividad funcional | Propuesta |
| REC-EST-08 | Exigir contrato independiente de `F*`, Value y horizonte | Evita circularidad y clasificación retrospectiva | Abierta |
| REC-EST-09 | Diseñar un módulo posterior específico para `θ_A(q)` si el objetivo es probar la pregunta C10-D1 en el DGP sintético | S4-R no cubre el estimando general | Propuesta; no añadir hasta cerrar S4-R |

## 9. Bloqueos que permanecen abiertos

Esta reconciliación no resuelve:
- la definición física y versionado completo de `B`;
- la factibilidad y soporte de las políticas comparadas;
- la exclusión IV en el DGP limpio y su contraste adversarial;
- `F*`, `q_X*`, horizonte, escala y regla independiente de Value;
- definición y validación de `A_f*`, `T_acc*` y `ΔT_acc` completo;
- interferencia y unidad de asignación;
- pérdidas, censura y error de medición;
- parámetros, réplicas, precisión, `δ` y `ε`;
- contratos ejecutables y revisión independiente XSYNC.

No se declara cerrado AUD-001/002, XAUD-001/002, S4-R ni XSYNC por la creación de este documento. Cada propuesta requiere revisión cruzada y decisión explícita.

## 10. Próximas operaciones documentales

1. Revisar esta jerarquía contra C10-D1 §§25–26 y 30–34 y contra C10-S §§43 y 51.
2. Si se acepta, incorporar las definiciones armonizadas en un addendum versionado a C10-S; no reescribir la historia ni borrar la propuesta previa.
3. Convertir DGP-CLEAN y DGP-CONTAMINATION en fichas de escenario con parámetros, verdad oculta, entradas/salidas y aserciones.
4. Formalizar `P*_τ2`, `P*_F`, `F*`, `q_X*` y Value.
5. Ejecutar revisión independiente documental/matemática; ejecución sintética solo tras autorización explícita y gate de diseño.
6. Actualizar la matriz maestra y decision log con los estados aceptado/rechazado/pendiente y la referencia exacta.

## 11. Límites y estado

**Estado global de este documento: PROPUESTA DE RECONCILIACIÓN, NO APROBADA.**

No se han cambiado los estimandos de C10-D1 ni se ha promovido una propuesta a decisión aceptada. No se ha ejecutado código, simulación, estimación o experimento. No se autoriza implementación, preregistro, selección de caso real, adquisición/procesamiento de datos ni cambio de Core, RMA, Evidence→Claim Matrix, STATUS o claims.

El resultado útil de esta revisión es haber separado la pregunta científica C10, el ITT del diseño S4-R y el efecto local focal, y haber identificado una forma explícita de resolver la ambigüedad `p0=.20` / `C_dep,base=0` sin ocultar contaminación ni cambiar retrospectivamente el DGP.


## 12. Resultado de auditoría integral: precedencia y propuesta armonizada

La auditoría integral se registra en `C10_S_INTEGRATED_RECONCILIATION_AUDIT_DRAFT_001.md` y el punto de integración se incorpora en el capítulo 53 del documento maestro.

La jerarquía candidata es: `theta_A(q)` pregunta general C10-D1; `ITT_Z` estimando primario de asignación S4-R; `LATE_f` atribución local secundaria condicionada a IV; `theta_Af(q*)` contraste poblacional focal solo bajo aislamiento y régimen común; `psi_policy` efecto de paquete cuando existen vías colaterales. S4-R no identifica por sí solo el efecto general de todo `Delta T_acc`.

La fuente 165–183 recomienda D1 como principal condicionado (p0=.20, p1=.80 postasignación, C_dep,base=0) y D2 como contraste (p0=0, p1=.80). Esta propuesta sustituye, para la especificación candidata, la recomendación anterior de usar exclusivamente p0=0 como DGP limpio y relegar p0>0 a contaminación. La formulación anterior se conserva como antecedente histórico, no se elimina.

Poblaciones, q*/g, mecanismo de provisión, exclusión, unidad/interferencia, F*, Value, parámetros estadísticos, fixtures y revisión independiente siguen pendientes. No se acepta automáticamente ninguna DEC ni se cierra AUD/XAUD/XSYNC.


## 13. Política B: mecanismo candidato recuperado y calibración

La fuente integrada §52.2 recupera los siguientes valores de intento/provisión: D1 (w_0=.25,w_1=1); D2 (w_0=0,w_1=1). Las probabilidades finales de acceso son respectivamente .20/.80 y 0/.80.

Una factorización candidata que satisface ambas tablas es (P(C_{dep}=1\mid W_{attempt}=1)=.80), común a los brazos, con (C_{dep}=0) cuando no hay intento. Así, (P(C_{dep}=1\mid Z=z)=P(W_{attempt}=1\mid Z=z)\times.80). Este cálculo supone que el éxito conjunto verificado condicional al intento es .80; no implica independencia de los componentes técnicos. El valor .80 es derivado para reconciliar intento y estado final, no un parámetro textual recuperado ni una observación.

La propuesta de política B, sus cuatro versiones D1/D2, invariantes, registros de asignación/recepción/cumplimiento y decisiones pendientes se desarrolla en el capítulo 54 del documento maestro. OPEN-C10-001 continúa abierta hasta decisión científica sobre el comparador D1 y aprobación de actor, recepción, versiones y verificación.


## 14. q_X* y soporte: operacionalización candidata

La propuesta armonizada con el maestro §55 es (q_X^*=P^*(X,H_0,C_c\mid E=1,C_{dep,0}=0,A_{f,0}^*=0)). Es una distribución objetivo basal, no un régimen que manipula covariables. (C_c) define elegibilidad constitutiva; (C_{dep,0}=0) y (A_{f,0}^*=0) definen cierre basal de la transformación focal. La evaluación se completa antes de Z y no utiliza cumplimiento, selección, ejecución, O o V.

El soporte exige que ambas políticas B_g0/B_g1 sean implementables en cada historia con masa positiva bajo qX y que el diseño asigne probabilidad positiva a ambos brazos. No exige que cada unidad pueda alcanzar ambos valores de D_f; esa es una cuestión de cumplimiento/compliers. Si una política no es factible, se restringe ex ante la población y se redefine el estimando, o se declara no identificación.

El S4-R primario utiliza qX*. qL* solo se requiere si una variable post-asignación L_m es indispensable y se interviene mediante una regla secuencial común. Ajustar marginalmente por L_m no lo sustituye. La distribución P*, composición completa de X/H0/Cc, unidad/interferencia, estratos, pesos y Value siguen abiertos; DEC-C10-012 permanece propuesta.
