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


## 12. Estado vigente de precedencia y alcance causal (actualizado 2026-11-09)

Este apartado sustituye la recomendación histórica de §§12, 17 y 18. La precedencia operativa no se reconstruye cronológicamente: se rige por DEC-C10-066/067 y por el maestro C10-S §§53, 131–132 y 213, junto con C10-D1 §§17.7 y 26.1–26.3.

- **Pregunta científica general:** `θ_A(q)`, efecto de políticas factibles sobre cambios estructurados del espacio de accesibilidad bajo un régimen común. C10-S focalizado en τ2 no lo sustituye ni lo identifica por sí solo.
- **Escenario primario candidato C10-S:** D2, por DEC-C10-066. D1 queda como escenario secundario incremental; la legitimidad de su régimen ordinario se justifica si se pretende transportar o interpretar ese contraste como política ordinaria.
- **Políticas materiales D2:** DEC-C10-067 acepta `B_g0^D2` (no programar/iniciar intento focal) y `B_g1^D2` (programar un intento estandarizado de provisión técnica focal). No son políticas de accesibilidad abstractas ni manipulan la autorización basal.
- **Estimando primario del diseño:** `ITT_Z^D2`, efecto de asignación a las políticas materiales D2 sobre Value (y Outcomes preespecificados). No equivale automáticamente al efecto de recepción ni a un efecto de accesibilidad.
- **Atribución focal:** `LATE_f^D2` es secundario y condicional a todos los supuestos IV y a medición válida de `D_f*`. `θ_Af(q_X*)` requiere identificación poblacional adicional y correspondencia demostrada entre B_D2 y políticas `g^Af`.
- **Efecto de paquete:** `ψ_policy^D2` conserva las vías activadas por la política cuando no puede atribuirse todo el efecto a accesibilidad. No se obtiene por renombrar el ITT ni por restar estimandos.
- **Correspondencia material→accesibilidad:** sigue CONDICIONAL / NO DEMOSTRADA. `s=0.80` sigue siendo hipótesis de DGP no validada. Las primeras etapas de `C_dep*`, `A_f*`, `D_f*` y `ΔT_acc*` se mantienen separadas.

Este estado no aprueba la jerarquía confirmatoria completa, no identifica `θ_A(q)`, `θ_Af(q_X*)` ni `LATE_f`, y no cierra población, soporte, unidad/interferencia, Value, vías colaterales, sensibilidad o potencia. Los detalles y límites se desarrollan en §§17–19 y en el maestro §131.

La recomendación antigua D1-principal/D2-contraste se retira del cuerpo operativo de este contrato. Su contenido histórico permanece en el historial Git y en la fuente recuperada 165–183, no como especificación vigente.

## 13. Política B: mecanismo candidato recuperado y calibración

La fuente integrada §52.2 recupera los siguientes valores de intento/provisión: D1 (w_0=.25,w_1=1); D2 (w_0=0,w_1=1). Las probabilidades finales de acceso son respectivamente .20/.80 y 0/.80.

Una factorización candidata que satisface ambas tablas es (P(C_{dep}=1\mid W_{attempt}=1)=.80), común a los brazos, con (C_{dep}=0) cuando no hay intento. Así, (P(C_{dep}=1\mid Z=z)=P(W_{attempt}=1\mid Z=z)\times.80). Este cálculo supone que el éxito conjunto verificado condicional al intento es .80; no implica independencia de los componentes técnicos. El valor .80 es derivado para reconciliar intento y estado final, no un parámetro textual recuperado ni una observación.

La propuesta de política B, sus cuatro versiones D1/D2, invariantes, registros de asignación/recepción/cumplimiento y decisiones pendientes se desarrolla en el capítulo 54 del documento maestro. OPEN-C10-001 continúa abierta hasta decisión científica sobre el comparador D1 y aprobación de actor, recepción, versiones y verificación.


## 14. q_X* y soporte: operacionalización candidata

La propuesta armonizada con el maestro §55 es (q_X^*=P^*(X,H_0,C_c\mid E=1,C_{dep,0}=0,A_{f,0}^*=0)). Es una distribución objetivo basal, no un régimen que manipula covariables. (C_c) define elegibilidad constitutiva; (C_{dep,0}=0) y (A_{f,0}^*=0) definen cierre basal de la transformación focal. La evaluación se completa antes de Z y no utiliza cumplimiento, selección, ejecución, O o V.

El soporte exige que ambas políticas B_g0/B_g1 sean implementables en cada historia con masa positiva bajo qX y que el diseño asigne probabilidad positiva a ambos brazos. No exige que cada unidad pueda alcanzar ambos valores de D_f; esa es una cuestión de cumplimiento/compliers. Si una política no es factible, se restringe ex ante la población y se redefine el estimando, o se declara no identificación.

El S4-R primario utiliza qX*. qL* solo se requiere si una variable post-asignación L_m es indispensable y se interviene mediante una regla secuencial común. Ajustar marginalmente por L_m no lo sustituye. La distribución P*, composición completa de X/H0/Cc, unidad/interferencia, estratos, pesos y Value siguen abiertos; DEC-C10-012 permanece propuesta.


## 15. Unidad e interferencia: armonización con el maestro §56

La propuesta primaria es UE=UA=instancia sintética independiente; UO son mediciones repetidas T0–T9. No es un hecho verificado: requiere inventario que descarte recursos, agentes, información, infraestructura y canales compartidos. Si varias UE comparten esos elementos, definir clúster y elegir asignación individual con exposición modelada o asignación por clúster. El N efectivo e inferencia respetan la UA real.

Sin interferencia, potenciales individuales V_i(z_i), D_f,i(z_i). Con interferencia, definir antes de generar resultados el mapa G_i(Z_-i) y potenciales V_i(z_i,g_i), D_f,i(z_i,g_i). Si no se puede especificar/observar la exposición, ITT individual y Wald individual no reciben interpretación causal focal. Correlación basal dentro de clúster no equivale por sí sola a interferencia.

La aleatorización, probabilidades y positividad se documentan en la unidad asignada. LATE individual requiere no interferencia; un diseño con spillovers exige estimando de exposición/clúster explícito. OPEN-C10-005 permanece ABIERTA.


## 16. F*, P*_τ2 y P*_F: reconciliación operativa

Se armoniza con el maestro §57 y la auditoría de §50.7: P*_τ2 incluye unidades basalmente elegibles con D_f,0=0 y A_f,0*=0; la presencia o indeterminación de alternativas no las excluye automáticamente. P*_F es subconjunto con ausencia respaldada de rutas substituibles para F* dentro del universo/G/H/C0 declarado. La regla de §48.6 que parecía exigir F_alt,0=0 a toda la población se restringe interpretativamente a P*_F; la formulación histórica se conserva y no se borra.

F* se especifica ex ante con objetivo técnico observable, entrada/S0, salida, restricciones, tolerancias, H, G, C0 y evidencia/adjudicación independiente de O/V. Para cada ruta se distinguen accesibilidad, aplicabilidad y substituibilidad; identidad no equivale a función. F_alt,0 admite 0/1/indeterminado y ausencia exige cobertura suficiente. Si B altera alternativas, exclusión IV focal se compromete y se conserva ITT del paquete; si alternativa basal permanece estable, su existencia puede producir heterogeneidad sin violar automáticamente exclusión.

La definición cuantitativa de F*, universo, umbrales, cobertura, error de clasificación, sensibilidad, q_X,F*, pesos y estimando confirmatorio P*_F siguen abiertos. DEC-C10-017 es propuesta.


## 17. Contrato vigente de escenarios y políticas materiales D1/D2

**Precedencia:** DEC-C10-066/067 y maestro C10-S §§53.4, 67 y 131–132. Las §§65–66 del maestro son únicamente registros de supersesión histórica, no especificaciones operativas.

| Elemento | D2 — primario candidato | D1 — secundario |
|---|---|---|
| `C_dep,base` | 0 antes de Z | 0 antes de Z |
| `P(W_attempt=1 | Z=0)` | 0 | .25 (política ordinaria candidata) |
| `P(W_attempt=1 | Z=1)` | 1 | 1 |
| `P(S_success=1 | W_attempt=1)` | .80 candidato, no validado | .80 candidato, no validado |
| `P(C_dep,post=1 | Z=0)` | 0, objetivo del DGP candidato | .20, objetivo del DGP candidato |
| `P(C_dep,post=1 | Z=1)` | .80, objetivo del DGP candidato | .80, objetivo del DGP candidato |
| Contraste | Provisión focal programada frente a ausencia de intento focal | Provisión programada frente a provisión ordinaria de baja frecuencia |

La tabla describe políticas/objetivos candidatos, no resultados observados ni parámetros validados. La probabilidad .80 es éxito técnico conjunto condicional al intento elegible; no es la probabilidad de cada componente y no se transfiere automáticamente a `A_f*` o `D_f*`.

En D2:
- `B_g0^D2` mantiene configuración basal y no programa ni inicia un intento focal como parte de la política.
- `B_g1^D2` programa un intento estandarizado de provisión técnica focal para unidades elegibles.
- La política no garantiza recepción, intento efectivo, instalación, integridad, compatibilidad, operatividad ni accesibilidad.
- `C_auth,base=1` permanece común, satisfecha antes de Z e invariante frente a B; la política D2 no interviene sobre autorización basal.
- `C_dep*` no es sinónimo de `A_f*`, `D_f*` ni `ΔT_acc*`. Cada estado y primera etapa se calcula por separado.

D1 conserva utilidad como escenario secundario de política incremental. Su provisión ordinaria de control no es contaminación si forma parte de la versión asignada y preespecificada; la legitimidad/transportabilidad del régimen .25/.20 no está acreditada y debe justificarse si se formula esa interpretación.

La correspondencia entre `B_g^D2` y políticas objetivo `g^Af` sigue CONDICIONAL / NO DEMOSTRADA. Se requiere derivar las distribuciones inducidas de cambios de accesibilidad por historia y verificar predicados, soporte, versiones, rutas alternativas y vías colaterales. Ver maestro §131. No trasladar a D2 la ilustración .20→.80 de D1 ni el valor ilustrativo 3.6.

**Estado:** precedencia D2/D1 aceptada dentro del alcance DEC-C10-066; contenido material D2 aceptado dentro del alcance DEC-C10-067; mecanismo de éxito, recepción/cumplimiento, distribución de accesibilidad y exclusión permanecen abiertos.

## 18. Jerarquía de estimandos y reglas de identificación bajo D2

Este apartado define la jerarquía de trabajo para el diseño sintético, sin convertirla en una decisión confirmatoria aprobada ni modificar el estimando general de C10-D1.

### 18.1. Pregunta científica general

`θ_A(q)=E[V^{q,g1}]-E[V^{q,g0}]` es la pregunta general de C10-D1: contraste entre políticas factibles que inducen cambios estructurados de accesibilidad `ΔT_acc` bajo un régimen común q, para población, horizonte, versiones y regla de Value definidos. S4-R focaliza τ2 y no identifica por sí solo este efecto general.

### 18.2. Estimando primario del diseño D2

`ITT_Z^D2=E[V|Z=1,D2]-E[V|Z=0,D2]` es el efecto de asignación a las políticas materiales D2. Bajo aleatorización válida, consistencia de asignación y tratamiento de interferencia/ausencia conforme al diseño, identifica el efecto de asignar la política, sin condicionar por recepción, cumplimiento, accesibilidad postratamiento, selección o ejecución. Debe reportarse también por Outcome y por cada dimensión de Value preespecificada.

El ITT no es automáticamente el efecto de recibir B, de `C_dep*`, de `A_f*`, de `D_f*` ni de todo `ΔT_acc`. Si hay vías colaterales, sigue siendo efecto de política/paquete.

### 18.3. Primera etapa y tratamiento focal

Reportar separadamente:
- `FS_Cdep^D2`: efecto de Z sobre `C_dep,post*`;
- `FS_Af^D2`: efecto de Z sobre `A_f,post*`;
- `FS_Df^D2`: efecto de Z sobre apertura `D_f*=I(A_f,base*=0 ∧ A_f,post*=1)`;
- cambio completo de `ΔT_acc*` y sus dimensiones/relaciones.

Ninguna primera etapa se sustituye por otra. `C_dep*` solo coincide con `A_f*`/`D_f*` bajo las condiciones explícitas de ruta única, inaccesibilidad basal y predicados no técnicos satisfechos e invariantes; véanse maestro §§67 y 131.

### 18.4. Atribución local IV

`LATE_f^D2` es un estimando secundario local entre compliers inducidos por Z para el tratamiento focal `D_f*`. Solo puede interpretarse causalmente si se sostienen relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia no modelada y medición válida del tratamiento. Se requiere inferencia robusta a instrumento débil. La auditoría del maestro §132 mantiene estos supuestos abiertos y concluye que `LATE_f` no está actualmente identificado ni listo para Wald. No calcular ni presentar Wald como causal mientras persistan esos gates.

Un eventual `LATE_f^D2` es local a los compliers D2; no es ATE, ATT, `θ_Af(q_X*)` poblacional ni `θ_A(q)` general.

### 18.5. Contraste focal poblacional y efecto de política/paquete

`θ_Af(q_X*)` es un contraste poblacional focal bajo políticas de accesibilidad `g^Af` y régimen común `q_X*`. No queda identificado por el ITT ni por LATE automáticamente. Requiere correspondencia demostrada `B_g^D2→g^Af`, población y soporte, versiones consistentes, régimen común completo y ausencia de vías diferenciales hacia Value o una estrategia que las separe. El maestro §131 clasifica esa correspondencia como CONDICIONAL / NO DEMOSTRADA.

`ψ_policy^D2` representa el efecto de la política material/paquete cuando se mantienen todas las vías que activa B, incluidas las no mediadas por accesibilidad focal. `ψ_B(q_X*)` para versiones recibidas no se identifica por el mero hecho de aleatorizar Z si hay incumplimiento; requiere estrategia propia de identificación y consistencia de versiones.

### 18.6. Mediación, residual y límites

No se interpretará `ITT_Z^D2-θ_Af(q_X*)` ni `TE-θ_A(q)` como efecto directo o residual puro. La mediación requiere intervención/estimando propio, población, horizonte y régimen definidos, con tratamiento de confusión postratamiento. Un efecto residual solo se informará bajo una descomposición formal identificada y compatible en población, escala y horizonte.

El diseño D2 focal no identifica por sí solo la contribución causal general de todo `ΔT_acc`. `θ_A_dyn` permanece fuera del conjunto evaluable hasta formalización.

### 18.7. Estado de cierre

- D2 primario candidato / D1 secundario: precedencia aceptada por DEC-C10-066.
- Políticas materiales D2: definidas conceptualmente por DEC-C10-067.
- `ITT_Z^D2`: objeto primario de asignación del diseño; su identificación empírica/sintética depende de aleatorización, consistencia, interferencia y Value.
- `LATE_f^D2`: secundario y no identificado/no listo para Wald en el estado documental actual.
- `θ_Af(q_X*)`: objetivo poblacional focal no identificado; mapeo B→g^Af no demostrado.
- `θ_A(q)`: pregunta científica general, no sustituida por el diseño focal.
- Población/soporte, Value, horizonte, unidad/interferencia, vías colaterales, medición, sensibilidad y potencia siguen abiertos.

La jerarquía anterior es una reconciliación documental de trabajo con decisiones de escenario/política ya aceptadas; no aprueba la identificación ni autoriza implementación, Design Freeze, simulación o ejecución. Mantener `scientific_execution=false` y `execution_authorized=false`.

## 8. Supersesión de precedencia del comparador — DEC-C10-066 (2026-11-06)

La recomendación histórica de §3.3 y las referencias anteriores a D1 como principal condicionado/D2 como contraste quedan **supersedidas exclusivamente en la precedencia del escenario primario candidato**. La decisión aceptada DEC-C10-066 establece D2 como escenario primario candidato de C10-S y D1 como escenario secundario. Se conserva la descripción histórica y la diferencia entre sus políticas; no se reescribe la fuente recuperada ni se mezclan sus estimandos.

La decisión no modifica la jerarquía causal de este documento: θ_A(q) sigue siendo la pregunta científica general C10-D1; ITT_Z es el efecto de asignación de la política D2 en el diseño S4-R; LATE_f es local y condicionado a IV; θ_Af(q*) requiere identificación adicional. La legitimidad de D2, el soporte, las vías colaterales, los parámetros y la identificación permanecen abiertos. D1 requiere justificación del régimen ordinario para interpretar su contraste secundario.

No se autoriza freeze, implementación, simulación ni ejecución.



## 19. Addendum D2: correspondencia de políticas materiales y políticas focales de accesibilidad (2026-11-06)

DEC-C10-066/067 no convierten (B_{g0}^{D2}/B_{g1}^{D2}) en (g_0^{Af}/g_1^{Af}). Las políticas g de C10-D1 son distribuciones objetivo factibles sobre cambios de accesibilidad; las políticas B D2 son mecanismos materiales de provisión. La correspondencia requiere reconstruir la distribución de (ΔA_f) inducida por cada B según historia y verificar consistencia, soporte, población basal, snapshots comparables, medición independiente, ausencia de rutas de fondo no registradas y separación de vías colaterales.

La pareja ilustrativa 0,20→0,80 de §33.4 no describe D2. D2 programa intento focal con probabilidad 0 en control y 1 en tratamiento. Solo bajo s=.80 candidato, cumplimiento perfecto, una oportunidad, ausencia de provisión de fondo, ruta focal única, inaccesibilidad basal y predicados restantes satisfechos/invariantes, la apertura focal (D_f^*) sería algebraicamente 0→0,80. No se valida s, no se identifica la primera etapa de accesibilidad por la de C_dep, y no se traslada el valor 3,6 a D2.

(ψ_B(q_X^*)) es la instancia del contraste de política (ψ_{policy}(q)) para las versiones recibidas B bajo el régimen/población basal (q_X^*), solo si ambos representan el mismo contraste y el régimen común está completo. No equivale a (ITT_Z) con incumplimiento ni a (θ_{Af}(q_X^*)) sin atribución focal. Si q exige (q_L^*), (q_X^*) no lo sustituye.

La auditoría se desarrolla en el maestro C10-S §131 y el plan de cierre §16.12. Estado: correspondencia B→g^Af condicional/no demostrada; (θ_{Af}) no identificado; sin freeze, implementación, simulación o ejecución.


## 20. Interfaz AB→C y salvaguardas de estimandos (2026-11-09)

El maestro C10-S §221 formaliza la transferencia contractual a C sin modificar la jerarquía de §18. C debe conservar separados ITT_Z^D2, FS_Cdep/FS_Af/FS_Df, ψ_policy^D2, ψ_B(q_X*), LATE_f^D2, θ_Af(q_X*), θ_A(q), mediación y residual. Sus poblaciones, regímenes, horizontes, versiones y escalas deben declararse; ningún estimando sustituye a otro.

La transferencia exige entradas versionadas AB: unidad/población pre-Z, Z/B y event log, C0/G/H, distribución conjunta C_dep*, mediciones independientes A_f/D_f/ΔT_acc, vías colaterales, Outcome/Value, truth/observed y soporte. C debe devolver ITT por Outcome/Value, primeras etapas separadas, diagnóstico de interferencia/seguimiento, dictamen IV por supuesto, evaluación del mapping B→g^Af y validación de recuperación del DGP.

Reglas no negociables: no condicionar ITT por recepción/cumplimiento/mediadores post-Z; no inferir A_f o D_f desde C_dep; no presentar Wald como causal mientras los supuestos IV sigan abiertos; no equiparar ITT o efecto de paquete con θ_Af/θ_A; no obtener mediación o residual por resta de estimandos no armonizados. La recuperación de truth sintética evalúa al Analyzer, no demuestra empíricamente ΔT_acc→Value.

Estado: interfaz contractual definida; inputs materiales AB y gates de identificación permanecen abiertos. Este addendum no supersede §18 ni la auditoría IV, no aprueba identificación y no autoriza implementación o ejecución.


## 22. Aclaración de jerarquía para el paquete C (2026-11-09)

La primacía de θ_A(q) como pregunta científica general de C10-D1 se mantiene. ITT_Z^D2 es el estimando primario de asignación dentro del diseño S4-R, no un sustituto de la pregunta científica. LATE_f^D2 y θ_Af(q_X*) siguen siendo objetivos focales secundarios/condicionales y no se transportan automáticamente a θ_A(q).

Si D2 activa vías diferenciales no mediadas por el tratamiento focal, el contraste debe conservarse como efecto de política/paquete. La exclusión no se deduce de la aleatorización. Esta aclaración desarrolla la jerarquía ya contenida en §18 y no la supersede.


## 23. Reconciliación de identificación y evaluación estadística — paquete C (2026-11-09)

El maestro C10-S §225 desarrolla sin sustituir la jerarquía de §18:
- ITT_Z^D2 y ψ_policy^D2 conservan el efecto de asignación/política;
- FS_Cdep, FS_Af y FS_Df son primeras etapas distintas;
- LATE_f^D2 sigue no identificado/no listo para Wald según la auditoría IV;
- ψ_B(q_X*) requiere estrategia propia ante recepción/incumplimiento;
- θ_Af(q_X*) requiere mapping B→g^Af, población/soporte y tratamiento de vías colaterales;
- θ_A(q) permanece la pregunta científica general C10, no identificada por el diseño focal D2.

La mediación requiere estimando e intervención propios y tratamiento explícito de confusión inducida por política; no se obtiene por resta ni por ajuste convencional de variables post-Z. Población pre-Z, q_X*, positividad, soporte, interferencia, missingness, sensibilidad, bounds, potencia y evaluación Monte Carlo quedan sujetos a los gates de §225.

La recuperación de truth sintética mide el desempeño del Analyzer bajo DGPs especificados. No constituye evidencia empírica de identificación de ΔT_acc→Value ni cierra la atribución causal general.

**Estado:** reconciliación documental propuesta; no modifica §18 ni la auditoría IV; no aprueba identificación, Design Freeze, implementación o ejecución. Mantener scientific_execution=false y execution_authorized=false.


## 24. Auditoría de cobertura contractual de mediación (2026-11-10)

Se corrige la correspondencia del Register §72: P177-05…08 no son contratos de mediación; sus definiciones vigentes son O/V, ajuste basal, ATE/ATT y heterogeneidad. Para la interfaz causal se aplican P177-06 (ajuste basal/no post-Z), P177-12 (política frente a atribución focal), P182-01/02/06/07 (validez/adjudicación de A) y P183-08 (ausencia de A y efecto sobre identificación), sin atribuirles alcance mayor.

La identificación mediacional sigue gobernada por la pregunta y los requisitos de C10-D1 §18 y por la propuesta del maestro §225.3. La cobertura contractual es parcial: falta definir el estimando/intervención mediadora, la secuencia y confusores postratamiento, soporte secuencial, método de identificación, sensibilidad y criterio de recuperación/abstención. No se infiere efecto mediado ni residual por resta de estimandos.

**Estado:** corrección documental verificada como necesaria; C-MED OPEN; no modifica la jerarquía θ_A(q)/ITT_Z^D2/LATE_f, no aprueba identificación, no congela diseño ni autoriza implementación/ejecución.


## 25. Auditoría ampliada de cobertura de contratos estadísticos (2026-11-10)

Se corrige el crosswalk de Register §72 conforme a las definiciones exactas de §55: P177-02 es primera etapa; P177-03 Wald/LATE; P177-04 instrumento débil. P178-SIM-02/03/04/05 corresponden a N, clústeres, réplicas y error Monte Carlo, complementados por SIM-01/09/10 para potencia, métricas y parámetros ex ante. P183-09/10/11/12 separan censura, sensibilidad, bounds y dictamen. P179-06/08 se limitan a trade-offs y agregación de Value.

La recuperación del Analyzer y el firewall tienen soporte parcial en P177-10/12 y P182-11, pero falsa identificación, falsa atribución focal y abstención correcta requieren criterios de adjudicación/tolerancias explícitos. La mediación permanece en §225.3 como propuesta, sin contrato completo.

**Estado:** crosswalk ampliado corregido; C-MED y C-ANALYZER OPEN. No modifica jerarquía de estimandos, contratos fuente, autorización ni estado científico. Sin implementación o ejecución.


## 26. Interfaz C10-D1/S4-R con los gates C-MED y C-ANALYZER (2026-11-10)

La jerarquía de §18 y las aclaraciones de §§22–25 se mantienen. §228 propone una especialización para evaluar la mediación de ΔT_acc* sin sustituir θ_A(q) por ITT_Z^D2, ψ_policy^D2 o LATE_f^D2. La intervención mediadora se define sobre la distribución conjunta del objeto transformacional completo o, en un análisis separado, sobre A_f*; no se equiparan ambas.

El mapping material B→g y las rutas colaterales de §14 de la auditoría IV son precondiciones para interpretar el contraste de D2 como intervención de accesibilidad. Cuando no se sostengan, se conserva el efecto de política/paquete y se impide atribución focal automática.

C-ANALYZER evaluará la recuperación solo en DGP identificables, bounds en parciales y clasificación/abstención en escenarios no identificables. Falsa identificación y falsa atribución focal se tratan como errores críticos; sus denominadores y tolerancias permanecen OPEN.

**Estado:** especialización propuesta; C-MED y C-ANALYZER OPEN; no cambia estimandos aceptados, no identifica ΔT_acc→Value y no autoriza implementación/ejecución.


## 27. Corrección de alcance causal y crosswalk C-MED/C-ANALYZER (2026-11-10)

El maestro §229 corrige la ambigüedad: la pregunta C10-D1 θ_A(q) es el contraste entre políticas factibles que inducen cambios de accesibilidad bajo un régimen común; la mediación del efecto material D2 es secundaria y no equivale a esa pregunta. El ITT-Z-D2 identifica, bajo los supuestos de diseño, el efecto de asignar B; no identifica automáticamente accesibilidad ni su contribución a Value.

La intervención g debe operar sobre la distribución conjunta factible de ΔT_acc, no sobre un índice abstracto. C10-D1 §27.1 ofrece la representación analítica (A⁺, A⁻, A^reconf, ΔR, ΔC). La tupla alternativa del DGP queda pendiente de crosswalk explícito, incluida la separación de ΔE_T; no se declara equivalente.

El reloj DGP t−1…t9 distingue confusores mediador–Value inducidos por B antes de t3 de consecuencias posteriores (Reach, trayectorias, K, selección, ejecución y Outcome). No ajustar mecánicamente por estas últimas para el efecto total. La mediación secundaria exige estimando interventional y método longitudinal compatible; sin soporte o separación de vías, bounds/no identificación.

El Analyzer se evalúa por estimando×dimensión×DGP×soporte; Generator conserva truth, Analyzer no la recibe y Evaluator adjudica después del sellado. Los denominadores de falsa identificación, falsa atribución y abstención se explicitan conceptualmente; tolerancias/umbrales permanecen OPEN.

**Estado:** reconciliación metodológica propuesta; C-MED/C-ANALYZER OPEN; no se identifica ΔT_acc→Value, no se altera la jerarquía de estimandos ni se autoriza implementación/ejecución.


## 28. Precedencia corregida de ΔT_acc y MED-02

Se corrige la descripción de §27 conforme al contrato DGP §30 y al documento de snapshots: la verdad estructural usa S_T*=(U*,R*,C*,X*) y ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*). ΔValidity_e es epistémica y pertenece a ΔE_T. La formulación previa de DGP §3.3 queda supersedida.

El mapping propuesto con C10-D1 §27.1 es ΔU→A⁺/A⁻/A^reconf; ΔR→ΔR; ΔC→ΔC. ΔX no se mapea sin más: requiere decidir si su contenido modifica realizabilidad (ΔC), es historia/contexto q o queda fuera del mediador. MED-02 permanece OPEN.


## 29. MED-02 — clasificación de ΔX* y regla de no doble conteo

La definición de snapshot distingue X_t* como estado/contexto efectivo constitutivo de accesibilidad y C_t* como condiciones/configuraciones estructurales de realizabilidad. C10-D1 §27.1 no tiene coordenada autónoma ΔX. Por tanto, ΔX* se conserva como contexto causal del DGP y sus consecuencias estructurales se reflejan en A⁺/A⁻/A^reconf/ΔR/ΔC sin contabilizarlo de nuevo como una contribución adicional.

Los campos se clasifican por función semántica: U transformación, R relación, C condición/predicado, X estado/contexto efectivo, E evidencia. Un supuesto X que sea una regla se reclasifica en C; historia no constitutiva puede pertenecer a q solo si es coherente y soportada; un campo sin efecto en accesibilidad queda fuera del mediador; UNKNOWN/? se conserva como tal. Se exige descomponer campos mixtos y registrar event_id, tiempo, frontera, truth/observed y adjudicación.

**Estado:** regla conceptual propuesta; roster del microdominio y mappings campo a campo OPEN. MED-02 no cerrado.


## 30. Roster documental MED-02c y clasificación por campo

Se consolida el roster parcial del maestro §232: transformaciones F1/F2/A1/A2 (U*); dependencias/interfaces/topología (R*); reglas, permisos, recursos y restricciones (C*); contexto efectivo runtime/host/modo/estado persistente (X* solo cuando sea constitutivo); logs, hashes, cobertura, validez y adjudicación (E_T). CMP/PAR/REF/RUL/MET conservan sus identidades y funciones contractuales; ENABLED/PROFILE son los PAR nucleares y RETRY-COUNT permanece candidato no confirmatorio.

B-M01…15 son superficies de inspección, no variables tipadas automáticamente ni evidencia de cambios. Se exige subcampo, event_id, tiempo de vigencia, frontera, mapping, truth/observed y cobertura. MED-02c3/c4/d OPEN; no declarar roster completo.


## 31. DAG Opción A/D2: reconciliación de vías y objeto mediador (2026-11-10)

El maestro §233 es la especificación candidata vigente del DAG específico y debe leerse junto con DEC-C10-066/067, el roster §232 y los contratos de provisión/snapshots. El DAG histórico de §6 se conserva como antecedente; para Opción A bajo D2 prevalece la especialización de §233.

Se precisa que A_f,1* es el predicado/proyección focal de accesibilidad dentro del snapshot T_acc,1, y D_f* es el indicador derivado de apertura basal→post. No se modelan como mediadores adicionales en serie con ΔT_acc*. El mediador secundario candidato es la distribución conjunta y factible de ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), con ΔX* conservado en el DGP y sin doble conteo analítico.

D2 asigna política B; no asigna A_f*, D_f* ni ΔT_acc*. El ITT_Z(D2) es efecto de política asignada. Solo puede interpretarse como θ_Af(q*) si se demuestra correspondencia B→g^Af, régimen común, soporte, consistencia y ausencia/identificación de vías colaterales hacia Value. Recursos, permisos, seguridad, dependencias compartidas/A1-A2, coste/latencia/calidad, información/selección, observación y spillovers son rutas explícitas a auditar. Confusores mediador–Outcome inducidos por B no se ajustan rutinariamente; requieren estrategia longitudinal o limitación a efecto de paquete.

No se cierra θ_A(q), mediación, LATE, población, q*, unidad/interferencia, Value ni identificación. El DAG queda DRAFT/CANDIDATE.


## 32. PC — dictamen integrado C3/C4 tras PA/PB (2026-11-11)

Prevalece la reconciliación integrada del maestro C10-S §268. Se preserva θ_A(q) como pregunta general C10-D1; θ_Af(q_X*) como contraste focal que requiere correspondencia B_D2→g^Af; ITT_Z^D2 como efecto de asignación/paquete; LATE_f^D2 como local y condicionado a IV; y C4 como mediación interventional separada. Ninguno sustituye a otro.

El estimando θ_A(q) requiere políticas factibles g1/g0 sobre la distribución de ΔT_acc* bajo régimen común q y soporte por historia. D2 no es esa intervención: asigna políticas materiales de provisión. La equivalencia interpretativa ITT_Z^D2=θ_Af(q_X*) solo sería defendible con mapping, consistencia/versiones, régimen común, soporte, medición y exclusión/identificación de todas las vías diferenciales. El inventario PB no permite declarar ausentes las vías colaterales; por tanto, no se atribuye el ITT a accesibilidad.

Para C4, el mediador no se reduce a A_f* o D_f*: es ΔT_acc* completo, con Reach/Π_H como mediadores secuenciales o bloque conjunto explícito. La mediación interventional requiere intervención factible sobre su distribución y estrategia longitudinal para confusores mediador–resultado inducidos por Z. El ajuste convencional post-Z no es válido como sustituto. No se adopta efecto indirecto natural ni se define residual por resta.

Estado: θ_A(q), θ_Af(q_X*) e IIE_T no identificados en el D2 material actual; Value no evaluable por falta de V_j/beneficiario/perspectiva/regla; LATE sigue bloqueado. P177/P178/P179/P182/P183 y DAG-01…08/CAUS-01…10 se reutilizan; C-MED PARCIAL/OPEN. Sin freeze/implementación/ejecución.
