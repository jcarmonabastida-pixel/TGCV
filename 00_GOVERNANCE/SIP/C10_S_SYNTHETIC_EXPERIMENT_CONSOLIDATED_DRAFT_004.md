# C10-S — Experimento sintético de validación transformacional y causal
**Consolidación documental integral — borrador 004 (notación revisada)**

**Estado:** DRAFT / PROPUESTA METODOLÓGICA — NO APROBADA / NO IMPLEMENTADA / NO EJECUTADA  
**Ámbito:** C10 — contribución causal de los cambios en transformaciones accesibles a Value  
**Relación:** Documento complementario a `C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`  
**Naturaleza:** consolidación normalizada de las decisiones, especificaciones, escenarios, contratos, pruebas y auditorías desarrollados conversacionalmente en C10-S hasta la sección 129. No es una transcripción literal.  
**Efecto sobre el estado científico:** ninguno. No modifica TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres experimentales.  
**Restricciones:** no autoriza implementación, ejecución, simulación, selección definitiva de caso real, adquisición/procesamiento de datos, preregistro ni contacto con autores o instituciones.

---

## 0. Control documental y reglas de interpretación

### 0.1. Propósito

C10-S especifica un experimento sintético para comprobar si una arquitectura operacional y analítica puede:

1. representar de forma independiente cambios en el espacio de transformaciones accesibles;
2. generar correctamente composiciones transformacionales, Reach y trayectorias candidatas;
3. distinguir accesibilidad, aplicabilidad, alcanzabilidad, selección y ejecución;
4. recuperar efectos causales conocidos en escenarios simulados;
5. reconocer escenarios nulos, negativos, heterogéneos, confundidos, no identificados y con vías alternativas;
6. mantener Outcome y Value separados de la medición de accesibilidad y de la generación de trayectorias.

C10-S es una prueba de la metodología y de los procedimientos de análisis. **No es evidencia empírica de que la hipótesis C10 sea verdadera en sistemas reales.**

### 0.2. Estados documentales

En este documento:

- **DEFINIDO:** especificación conceptual suficientemente explícita para revisión.
- **PENDIENTE:** decisión o parámetro que requiere justificación o revisión.
- **IMPLEMENTADO:** existe código que materializa la especificación.
- **EJECUTADO:** existe una ejecución identificada y reproducible.
- **AUDITADO:** existe auditoría documentada de la implementación o ejecución.
- **ACEPTADO:** existe decisión explícita de aceptación.
- **NO IDENTIFICADO:** el diseño/datos no permiten identificar el estimando definido.
- **INDETERMINADO:** la evidencia disponible no permite una clasificación afirmativa o negativa.

La inclusión de una prueba o contrato en este documento significa que está **definida**, no que haya sido implementada, ejecutada o superada.

### 0.3. Relación con C10-D1

C10-D1 establece el marco de atribución causal: estimandos, DAG, condiciones post-tratamiento, régimen común, requisitos de identificación, medición de Value y criterios de falsación.

C10-S comprueba, en un universo sintético controlado, si los componentes transformacionales y causales pueden reconstruir escenarios cuyo mecanismo generador es conocido.

C10-S no sustituye C10-D1 ni resuelve por simulación los problemas de identificación de un sistema real.

### 0.4. Regla de no propagación

Ningún resultado futuro de C10-S modificará automáticamente Core, RMA, Evidence→Claim Matrix, STATUS o claims. Cualquier propuesta de cambio científico requerirá una evaluación independiente y el procedimiento de gobernanza aplicable.

---

## 1. Pregunta, hipótesis y alcance

### 1.1. Pregunta de investigación

¿Puede un diseño sintético controlado manipular y medir un cambio en transformaciones accesibles, reconstruir sus consecuencias transformacionales y distinguir su contribución causal a Value de otras vías, recuperando correctamente escenarios en los que la verdad causal es conocida?

### 1.2. Hipótesis condicional C10

En determinados sistemas generativos y bajo condiciones contextuales y evaluativas especificables, los cambios en el espacio de transformaciones accesibles contribuyen causalmente a cambios de valor a través de los mecanismos y trayectorias que esos cambios hacen posibles. Magnitud, dirección y distribución dependen de la composición del espacio transformacional, de las condiciones del sistema y de la regla de construcción de Value.

Es una hipótesis de trabajo falsable, no una afirmación universal ni una modificación del Core.

### 1.3. Tres resultados científicos legítimos

1. Atribución causal identificada dentro de un ámbito delimitado.
2. Evidencia adversa que limite o refute una predicción en el ámbito preespecificado.
3. Identificación insuficiente; no confirma ni refuta.

### 1.4. Qué puede y qué no puede validar C10-S

Puede validar:
- consistencia de la operacionalización sintética;
- integridad de catálogos y relaciones dentro de universos cerrados;
- generación de trayectorias y Reach;
- separación de constructos;
- recuperación de efectos conocidos;
- capacidad de detectar no-identificación y errores de medición;
- reproducibilidad del procedimiento.

No puede validar:
- la completitud de un catálogo real abierto;
- la validez externa a dominios empíricos;
- la existencia de una contribución causal en un sistema real;
- la regla de Value adecuada para todos los contextos;
- la generalización de un resultado sintético a la TGCV en general.

---

## 2. Arquitectura causal y transformacional

### 2.1. Variables

| Símbolo | Definición |
|---|---|
| (X) | Contexto y características basales |
| (Z) | Asignación/intervención aleatorizada o mecanismo de asignación especificado |
| (C_c) | Condiciones constitutivas/habilitadoras de realizabilidad |
| (L) | Otras condiciones temporales, clasificadas por su historia causal |
| (A) | Cambio focal de accesibilidad, operacionalizado mediante ΔT_acc |
| (M) | Mecanismos posteriores, incluidos Reach y trayectorias |
| (O) | Outcome observable |
| (V) | Value, medido mediante regla independiente |
| (N) | Vía alternativa separada, cuando el escenario la incorpora |

### 2.2. Cadena de separación

`estado/contexto/condiciones → catálogo de transformaciones → T_acc → Reach y trayectorias candidatas → selección → ejecución → Outcome → Value`

La cadena no implica que cada flecha sea causalmente identificada. Es una arquitectura de medición y análisis que evita reconstruir constructos anteriores a partir de resultados posteriores.

### 2.3. Reglas fundamentales

- (T_{acc}) no es una lista de acciones observadas, outcomes, take-up o intenciones.
- Accesibilidad requiere realizabilidad respaldada, condiciones, recursos, admisibilidad y dependencias; no exige ejecución.
- Reach deriva de composiciones admisibles de transformaciones, no solo de estados observados.
- Trayectorias candidatas y trayectorias ejecutadas son objetos diferentes.
- Outcome no es Value.
- Value no debe premiar mecánicamente el número de transformaciones, longitud de trayectoria o cardinalidad de (T_{acc}).
- La evaluación de (T_{acc}) debe ser independiente y, cuando sea posible, ciega a (O) y (V).

### 2.4. DAG de trabajo

Estructura orientativa:

- (X) puede afectar (A,L,M,O,V) y, en diseños no aleatorizados, también (Z).
- (Z) puede afectar condiciones habilitadoras, (L,A,M,O,V).
- (A ightarrow M ightarrow O ightarrow V) representa una vía focal de trabajo.
- Pueden existir vías alternativas (Z ightarrow O/V), (A ightarrow V), mediadores adicionales, interacciones y confusión inducida por tratamiento.

La aleatorización de (Z) no aleatoriza automáticamente (A) ni (M), no garantiza exclusión y no identifica por sí sola la mediación específica por accesibilidad.

---

## 3. Operacionalización de transformaciones, accesibilidad y composición

### 3.1. Identidad de una transformación

Unidad candidata:

`τ=(S_o,S_d,M,P_τ,K,E)`

donde:
- (S_o): estado/configuración de origen;
- (S_d): estado/configuración de destino;
- (M): mecanismo;
- (P_τ): predicado de admisibilidad;
- (K): condiciones, recursos, dependencias y restricciones;
- (E): evidencia de identidad y realizabilidad.

### 3.2. Identidad y sustituibilidad

Distinguir:
- **Equivalencia de identidad ≡I:** relación de equivalencia reflexiva, simétrica y transitiva que identifica la misma transformación bajo una granularidad y versionado fijados.
- **Sustituibilidad funcional (Sub(π,τ^*,G,H,C)):** juicio relativo a función objetivo, grupo/contexto, horizonte y condiciones. No tiene por qué ser simétrico ni transitivo y no debe denominarse equivalencia de identidad.

Mismo destino, Outcome o Value no bastan para declarar identidad. Transformaciones con mecanismos distintos pueden seguir siendo transformaciones distintas.

Las composiciones descomponibles se representan como secuencias derivadas; un compuesto solo se trata como unidad atómica si es irreducible en la granularidad preespecificada. Mantener trazabilidad con sus componentes.

### 3.3. Cambio de accesibilidad

Con universo común:

- `A⁺ = T_acc,1 ∖ T_acc,0`
- `A⁻ = T_acc,0 ∖ T_acc,1`
- `ΔT_acc = (A⁺, A⁻)`

No reducir el cambio a cardinalidad neta. Registrar por separado cambios en identidades/unidades, relaciones y configuraciones cuando la representación lo requiera. Una relación nueva no implica por sí misma una transformación nueva.

Estados epistémicos:
- accesible respaldada;
- inaccesible respaldada;
- indeterminada.

Separar estado estimado de calidad/confianza de evidencia.

### 3.4. Representación relacional provisional

`T_acc=(U_acc,R_acc,C_acc)`

donde (U_{acc}) son transformaciones accesibles, (R_{acc}) relaciones/dependencias activas y (C_{acc}) condiciones/configuraciones pertinentes.

Esta representación es operacional para C10-S, no una modificación del Core.

### 3.5. Reach y horizonte

`Reach_H(S_0,T_acc) = { S' : S_0 ⇝_{≤H}^{T_acc} S' }`

- (H) es el máximo de aplicaciones efectivas de transformaciones.
- En el contrato sintético actual, (H=3).
- Las evaluaciones de condiciones/accesibilidad no consumen horizonte.
- Los ciclos cuentan cada aplicación efectiva.
- (T_{acc}) se reevalúa en cada estado hipotético intermedio.
- Cada rama mantiene estado, condiciones y snapshots de accesibilidad independientes.

No se presupone:
- Si `ΔT_acc ≠ 0`, no se sigue necesariamente que `ΔReach ≠ 0`.
- Si `ΔReach = 0`, puede ocurrir que `ΔΠ_H ≠ 0`.
- Un mismo Reach no implica que existan las mismas trayectorias.

### 3.6. Accesible, aplicable, alcanzable y ejecutada

Distinguir obligatoriamente:
1. transformación incluida en catálogo;
2. transformación realizable/accesible bajo condiciones;
3. transformación aplicable desde un estado concreto;
4. transformación incluida en una trayectoria candidata;
5. transformación seleccionada;
6. transformación efectivamente ejecutada con evidencia.

No inferir un nivel a partir de otro.

---

## 4. Sistema sintético de referencia C10-S

### 4.1. Catálogo focal

| ID | Nombre | Origen → destino | Mecanismo |
|---|---|---|---|
| τ1 | Diagnose | Incidencia no identificada → incidencia diagnosticada | Identificación de causa |
| τ2 | Reconfigure | Configuración problemática → configuración técnicamente modificada | Modificación técnica |
| τ3 | Verify | Configuración modificada → configuración verificada | Prueba técnica |
| τ4 | Escalate | Incidencia diagnosticada → responsabilidad transferida | Transferencia a otra unidad |

### 4.2. Condiciones

- τ1: incidencia/datos disponibles, capacidad diagnóstica e información suficiente.
- τ2: diagnóstico completado, autorización vigente, recursos y capacidad de reconfiguración.
- τ3: configuración técnicamente modificada, acceso a pruebas, capacidad de verificación y sistema disponible.
- τ4: diagnóstico completado, unidad receptora disponible, capacidad de transferencia y aceptación receptora.

### 4.3. Relaciones activas

`R_acc={r12,r23,r14}`

- (r_{12}): diagnóstico habilita reconfiguración.
- (r_{23}): reconfiguración habilita verificación técnica.
- (r_{14}): diagnóstico habilita escalado/transferencia.

La relación (r_{43}) queda **inactiva y excluida** de la composición actual. τ3 verifica una configuración técnicamente modificada; τ4 transfiere responsabilidad y no produce por sí misma la reconfiguración requerida.

### 4.4. Contraste G0/G1

- G0: τ2 está en el catálogo de referencia, pero no es realizable/accesible bajo las condiciones G0 por ausencia de autorización constitutiva.
- G1: la autorización hace realizable/accesible τ2; recursos, capacidad, información diagnóstica y motivación se mantienen constantes.
- La intervención manipula la condición que habilita τ2; no asigna abstractamente (T_{acc}).

Trayectorias esperadas:
- G0: τ1 → τ4; termina en estado de incidencia transferida. No se atribuye reconfiguración ni verificación técnica.
- G1: τ1 → τ2 → τ3; alcanza configuración modificada y verificada.

τ3 no es aplicable inmediatamente tras τ1. Solo lo es después de τ2.

### 4.5. Exclusividad aún no demostrada

El contraste solo identifica la apertura focal de τ2 si G0 no dispone de otra transformación o composición que realice la misma función técnica. Deben auditarse alternativas directas, composiciones, transformaciones distribuidas, rutas indirectas y rutas externas al catálogo.

No introducir τ5 en el catálogo actual. Una futura transformación de confirmación de recepción podría estudiarse por separado, pero no debe confundirse con verificación técnica de reconfiguración.

---

## 5. Contrato formal del generador de trayectorias

### 5.1. Entradas

| Entrada | Definición |
|---|---|
| (S_0) | Estado inicial |
| (U^*) | Catálogo inmutable y versionado de transformaciones |
| (U_{acc}(s,c,l)) | Subconjunto accesible en estado/contexto/historia de cada rama |
| (R^*) | Relaciones y dependencias tipificadas |
| (C) | Condiciones, recursos, restricciones y autorizaciones |
| (H) | Horizonte máximo, inicialmente 3 aplicaciones |
| Reglas | Identidad, granularidad, equivalencia de estado, aplicabilidad y composición |
| Evidencias | Procedencia, calidad y estado epistémico de cada condición/clasificación |

(U^*) y (U_{acc}) no son intercambiables. El catálogo es la referencia; la accesibilidad es contextual y puede cambiar por rama.

### 5.2. Salidas

1. Trayectorias candidatas (Pi_H), cada una con validez, estados, dependencias y procedencia.
2. (Reach_{definite}): estados alcanzables mediante composiciones respaldadas.
3. (Reach_{possible}): estados cuya alcanzabilidad depende de condiciones/evidencias indeterminadas; no se mezclan con Reach confirmado.
4. Registro de secuencias rechazadas, con código y motivo.
5. Metadatos reproducibles: versión catálogo/reglas, parámetros, seed cuando aplique, hashes y configuración.

Cada trayectoria conserva identificadores/versiones, estados por paso, snapshots de accesibilidad, condiciones, dependencias, evidencia y dictamen.

### 5.3. Estados de evaluación

| Dimensión | Estados |
|---|---|
| Accesibilidad | Respaldada / no respaldada / indeterminada |
| Aplicabilidad | Sí / no / desconocida |
| Composición | Válida / inválida / indeterminada |
| Alcanzabilidad | Confirmada / descartada / posible |

La incertidumbre relevante impide clasificar como confirmada una trayectoria. No declarar exclusividad con rutas alternativas no resueltas.

### 5.4. Independencia

El generador no recibe Outcome, Value, puntuaciones de preferencia, recomendaciones del selector ni resultados de ejecución. Genera candidatos a partir de transformaciones, relaciones, condiciones, estados hipotéticos y reglas de composición.

Selección, ejecución, Outcome y Value quedan fuera del generador.

### 5.5. Terminación y determinismo

- (H=3) limita aplicaciones efectivas.
- Comprobaciones de condiciones no consumen horizonte.
- Cada rama conserva estado y condiciones propios.
- Catálogo y reglas son inmutables durante una ejecución.
- El orden de expansión no cambia el conjunto final.
- Deduplicación de secuencias por IDs/versiones ordenados.
- Diferentes rutas hacia un mismo estado se conservan.
- Equivalencia de estado final no elimina rutas distintas.
- Ciclos quedan acotados por (H); repetición solo si hay cambio de estado efectivo válido.
- Completitud computacional se refiere al universo declarado, no a todo el sistema real.

### 5.6. Invariantes GEN

| Código | Invariante |
|---|---|
| GEN-01 | No aplicar transformación no accesible |
| GEN-02 | No aplicar sin precondiciones satisfechas |
| GEN-03 | No componer relaciones inexistentes/inactivas |
| GEN-04 | Reevaluar accesibilidad después de cada aplicación |
| GEN-05 | Independencia de ramas hipotéticas |
| GEN-06 | Respetar (H=3) |
| GEN-07 | No confundir candidata con ejecutada |
| GEN-08 | No utilizar Outcome/Value en generación |
| GEN-09 | Conservar rutas distintas al mismo estado |
| GEN-10 | Reproducibilidad con mismos datos/reglas |
| GEN-11 | No confirmar Reach con evidencia indeterminada |
| GEN-12 | No declarar exclusividad con catálogo incompleto |

---

## 6. Contrato de Value y ejecución

### 6.1. Value

`V=f(O;B,R_V,H_V)`

donde:
- (B): beneficiario/entidad evaluada;
- (R_V): regla de construcción de Value;
- (H_V): horizonte evaluativo.

Fijar antes de resultados:
- criterios y pesos, cuando la agregación sea defendible;
- dirección y unidad;
- costes, beneficios y trade-offs;
- beneficiario y horizonte;
- incertidumbre y datos ausentes.

No asumir que todo Value es escalar o agregable. No asignar valor por el mero aumento de cardinalidad de (T_{acc}), número de trayectorias o longitud de una ruta.

### 6.2. Value realizado y potencial

- (V_{real}): Value derivado de resultados de una trayectoria efectivamente ejecutada.
- (V_{potential}): conjunto de valores posibles bajo trayectorias factibles, aún no ejecutadas.

Representación exploratoria:

`F_V(T_acc,q)={V(π,q):π∈Π(T_acc,q)}`

El máximo de una frontera potencial puede aumentar tautológicamente al ampliar el conjunto de opciones. Por ello no es evidencia empírica independiente de creación de valor. (V_{real}) será la medida primaria en C10-P; (V_{potential}) queda como complemento conceptual pendiente de formalización.

### 6.3. Dos regímenes de ejecución

- **Experimento A — ejecución controlada:** prueba manipulación y cadena técnica, pero no identifica por sí sola el efecto causal de accesibilidad sobre Value si expectativas, información o incentivos quedan alterados.
- **Experimento B — selección libre:** permite observar selección entre trayectorias candidatas, con riesgos adicionales de selección, confusión y heterogeneidad.

No confundir ambos objetivos.

---

## 7. Modelo causal sintético y escenarios

### 7.1. Modelo base

Variables continuas con errores independientes normales estándar, salvo que un escenario especifique otra distribución:

`M=1+α_A A+α_AX(A·X)+ε_M`
`O=2M+ε_O`
`V=3O+ε_V`

Con la escala indicada:

`θ_A(X)=6(α_A+α_AX·X)`

Modelo lineal básico sin interacciones: (A=Z), (M=1+alpha_A A+epsilon_M), (O=2M+epsilon_O), (V=3O+epsilon_V). El efecto mediado estructural de A es (6alpha_A).

El generador de escenarios conoce los parámetros verdaderos. El analizador no recibe coeficientes ni etiquetas de verdad; recibe solo variables observables, diseño, diccionario y reglas. Un evaluador independiente compara la conclusión con la verdad generadora.

### 7.2. Parámetros computacionales preliminares

- (N=2000) unidades sintéticas por réplica.
- Asignación 1:1 cuando proceda.
- 1000 réplicas Monte Carlo.
- (alpha=0.05), intervalos del 95%.
- Seed fija y registrada.

Son parámetros de diseño preliminares, **no cálculo de potencia final**. δ (efecto mínimo relevante) y ε (margen de equivalencia) siguen pendientes de justificación. No fijarlos por conveniencia después de observar resultados.

### 7.3. Matriz de escenarios

| Escenario | Mecanismo verdadero | Resultado que debe recuperar el analizador |
|---|---|---|
| S0 — Cambio sin efecto | (A=Z), pero (alpha_A=0); Value no cambia por A | Detectar cambio en T_acc y no inferir efecto en Value |
| S1 — Positivo | (alpha_A=+1), vía M→O→V | Efecto de A en Value (+6) |
| S2 — Negativo | (alpha_A=-1) | Efecto de A en Value (-6) |
| S3 — Heterogéneo | (X∼Bernoulli(.5)), (alpha_A(X)=1-1.5X) | Estrato X=0: +6; X=1: −3; promedio: +1.5 |
| S4-O — Confusión post-tratamiento | Z afecta L; L afecta A y V; M/O/V también dependen de A | TE identificable por aleatorización de Z; θ_A no automáticamente identificable por ajuste convencional |
| S4-R — Régimen común | Intervención secuencial fija (q^*(L=1|X)=.5); políticas (g_1(A=1|X,L)=.8), (g_0=.2) | θ_A(q*)=+3.6 si soporte, consistencia e intervención secuencial se cumplen |
| S5-C — Vía alternativa colineal | A=Z; V recibe efecto A (+6) y vía directa Z (+5) | TE=+11; no separar efecto de A de vía alternativa porque A=Z |
| S5-F — Vía alternativa factorial | (Z_A) aleatoriza A; (Z_D) activa vía alternativa N independiente; contribuciones +6 y +5 | Separar efectos de A y N bajo diseño factorial; informar interacción si se incorpora |
| S6-N — Error de medición no validado | A_true generado; A_obs con sensibilidad/especificidad .8; analizador no observa A_true | No corregir automáticamente; sensibilidad .7/.8/.9/.95 como supuestos |
| S6-V — Validación de medición | Submuestra aleatoria con referencia gold-standard independiente y ciega | Estimar error de clasificación y propagar incertidumbre |
| S7 — Composición, misma cardinalidad | U0={τ1,τ2,τ3}; U1={τ1,τ4,τ3}; Value independiente | Detectar altas/bajas de identidad aunque cardinalidad no cambie |
| S8 — Accesibilidad sin Reach | U1=U0∪{τ4}; τ4 accesible pero no aplicable desde S0 dentro de H | ΔT_acc≠0, ΔReach=0; no inferir ruta alcanzable |
| S9 — Value sin accesibilidad | A=0 en ambos grupos; N=Z; V=V0+5N+ε | TE=+5, θ_A=0, ΔT_acc=0 |
| S10a — Positividad parcial | Ambos A factibles estructuralmente, pero soporte observado incompleto por X | Efecto identificable en estratos con soporte; no extrapolar a población completa |
| S10b — Condición constitutiva | En X=1, A=1 es inevitable; política g0(A=0) imposible | Restringir población a X=0 o definir intervención conjunta L+A; no presentar como θ_A original |

S4-O y S4-R son variantes distintas: la segunda incorpora una intervención secuencial real sobre L y políticas de accesibilidad, no una mera estandarización estadística. S5-C y S5-F también son distintos: en el primero la atribución no está identificada; en el segundo el diseño separa las vías.

### 7.4. S4-O — especificación estructural

- (L|Z=0∼Bernoulli(.25))
- (L|Z=1∼Bernoulli(.75))
- (P(A=1|Z,L)=logit^{-1}(-.5+1.5Z+1.2L))
- (M=1+A+.5X+epsilon_M)
- (O=2M+epsilon_O)
- (V=3O+4L+epsilon_V)

El analizador recibe Z,L,A,M,O,V y variables basales, pero no los coeficientes generadores. No se le permite asumir que el componente estructural de A es identificable por observar asociaciones condicionadas en L.

### 7.5. S4-R — intervención secuencial

Se interviene sobre la distribución de L con (q^*(L=1|X)=.5), y después sobre A mediante políticas factibles (g_1=.8), (g_0=.2). Bajo el modelo de efecto +6 por unidad de A, el contraste es (6(.8-.2)=3.6). El protocolo debe registrar la historia y probabilidades de asignación. No confundir intervención sobre L con estandarización retrospectiva.

### 7.6. S5-F — vía alternativa separada

(Z_A) y (Z_D) son asignaciones independientes. (Z_A) manipula accesibilidad focal A; (Z_D) activa mecanismo alternativo N que afecta Value. La contribución sintética es +6 para A y +5 para N, con TE conjunto +11 en ausencia de interacción. Si se incorpora interacción, debe estimarse e informarse, no absorberse en un efecto principal.

### 7.7. S6 — error de medición

En S6-N, las tasas de sensibilidad/especificidad se conocen solo como escenarios de sensibilidad, no como verdad disponible al analizador. En S6-V existe submuestra aleatoria de validación, medida independientemente y a ciegas. Deben propagarse incertidumbres de clasificación a la estimación causal.

---

## 8. Variables, unidades y arquitectura de evaluación

### 8.1. Unidad experimental

Unidad primaria: instancia independiente de sistema sintético. La asignación, medición y análisis deben corresponder a esa unidad o justificar agrupación/interferencia.

### 8.2. Diccionario mínimo

- scenario_id
- unit_id
- replicate_id
- X y condiciones basales
- Z y probabilidades/historial de asignación
- U_acc, R_acc, C_acc
- A_true (solo generador/evaluador)
- A_observed (analizador)
- Reach
- Pi_candidate
- Pi_selected
- Pi_executed
- M
- O
- V y dimensiones/regla de Value
- missingness
- measurement_status
- evidence_quality
- snapshots de estado y condiciones por rama
- versiones de catálogo y reglas

El analizador no recibe variables de verdad ocultas al diseño real. El evaluador independiente conserva la verdad del generador.

### 8.3. Arquitectura de roles

1. **Generador sintético:** produce unidades, escenarios, tratamientos, transformaciones y outcomes conforme al DGP.
2. **Analizador TGCV ciego:** reconstruye accesibilidad, relaciones, Reach y trayectorias a partir de entradas permitidas.
3. **Analizador causal ciego:** evalúa estimandos, identificación, soporte, confusión y sensibilidad.
4. **Evaluador independiente:** compara salidas con la verdad generadora y aplica criterios preespecificados.

Evitar filtraciones de parámetros, etiquetas de escenario, resultados y reglas de evaluación.

### 8.4. Tres evaluaciones independientes

No producir una puntuación global compensatoria:

- **TGCV reconstruction:** identidad, accesibilidad, relaciones, Reach y trayectorias.
- **Causal identification:** estimabilidad, sesgo, cobertura, falsos positivos/negativos y detección de no-identificación.
- **Value construction:** independencia, consistencia, regla y correcta interpretación de Value.

---

## 9. Protocolos de pruebas transformacionales y causales

### 9.1. Pruebas de identidad EQ

- EQ-01: mismo mecanismo con etiquetas diferentes.
- EQ-02: mismo destino con mecanismos distintos.
- EQ-03: misma transformación bajo diferentes recursos/contextos.
- EQ-04: nueva relación sin nueva transformación.
- EQ-05: secuencia compuesta descomponible.
- EQ-06: compuesto irreducible a granularidad fijada.
- EQ-07: precondición esencial distinta.
- EQ-08: rutas distintas al mismo destino.
- EQ-09: duplicado de catálogo.
- EQ-10: cambio meramente representacional.

La equivalencia de identidad no debe confundirse con sustituibilidad funcional.

### 9.2. Pruebas de exclusividad EX

- EX-01: buscar transformación alternativa directa.
- EX-02: buscar composiciones alternativas.
- EX-03: comparar sustituibilidad funcional respecto de (F^*).
- EX-04: verificar igualdad de recursos/condiciones no focales.
- EX-05: auditar rutas externas al catálogo.
- EX-06: auditoría independiente ciega.
- EX-07: robustez ante granularidad y descomposición.
- EX-08: evidencia de realizabilidad, sin inferir inaccesibilidad de la falta de ejecución.

### 9.3. Pruebas del generador TG

- TG-01: generación de todas las trayectorias válidas del universo cerrado.
- TG-02: rechazo de transformación inaccesible.
- TG-03: rechazo por precondición incumplida.
- TG-04: respeto de dependencias.
- TG-05: reevaluación dinámica de accesibilidad.
- TG-06: control de ciclos.
- TG-07: conservación de rutas distintas al mismo estado.
- TG-08: transformación nueva sin cambio de Reach.
- TG-09: mismo Reach con diferentes trayectorias.
- TG-10: independencia de Outcome y Value.
- TG-11: tratamiento explícito de condiciones indeterminadas.
- TG-12: reproducibilidad.

### 9.4. Pruebas de regresión semántica SR

- SR-01: τ4 (Escalate) no habilita τ3 ni realiza verificación técnica.
- SR-02: τ3 (Verify) no es aplicable tras τ1; solo lo es después de τ2 (Reconfigure).
- SR-03: τ4 puede seguir a τ1 en G0.
- SR-04: G0 termina tras transferencia; no se etiqueta como configuración verificada.
- SR-05: G1 admite τ1→τ2→τ3.
- SR-06: H=3 limita aplicaciones efectivas.
- SR-07: cada rama conserva estado y condiciones independientes.
- SR-08: Value no modifica la generación TGCV.
- SR-09: cualquier ruta externa que realice F* bloquea exclusividad.
- SR-10: no se infiere ejecución a partir de trayectoria candidata.

### 9.5. Pruebas de validación cruzada CV

- CV-01: S0, cambio de accesibilidad sin efecto Value.
- CV-02: S1, efecto positivo.
- CV-03: S2, efecto negativo.
- CV-04: S3, heterogeneidad.
- CV-05: S4-O, confusión post-tratamiento.
- CV-06: S4-R, régimen común intervenido.
- CV-07: S5-C, vía alternativa no separable.
- CV-08: S5-F, vías separables.
- CV-09: S6-N/S6-V, error de medición y validación.
- CV-10: S7, composición con cardinalidad constante.
- CV-11: S8, accesibilidad sin Reach.
- CV-12: S9/S10, Value sin accesibilidad y límites de soporte/constitutivos.

### 9.6. Pruebas de Value V

- V-01: independencia de regla Value respecto de T_acc y Outcome.
- V-02: no premiar automáticamente cardinalidad, longitud o número de transformaciones; conservar dimensiones/trade-offs y reglas preespecificadas.

### 9.7. Puertas de validación

- **P1 — Manipulación:** G0/G1 producen el cambio focal previsto en accesibilidad.
- **P2 — Medición:** analizador recupera identidades, condiciones y clasificación de T_acc sin leakage.
- **P3 — Transformación:** Reach y trayectorias se generan correctamente.
- **P4 — Atribución:** analizador recupera nulo, positivo, negativo, heterogéneo, confusión, alternativa y no-identificación.
- **P5 — Value:** Value se construye independientemente y se interpreta sin circularidad.

P1–P5 son puertas metodológicas; superar una no implica superar las siguientes.

---

## 10. Auditoría de completitud y exclusividad

### 10.1. Tres niveles de completitud

1. **Computacional:** enumeración completa respecto del universo (U^*), reglas y horizonte declarados.
2. **Representacional:** catálogo incluye las transformaciones relevantes conocidas para el dominio y granularidad.
3. **Empírica:** evidencia suficiente para sostener que no se han omitido rutas alternativas relevantes en el sistema real.

C10-S puede validar el nivel computacional en universo cerrado y someter el nivel representacional a pruebas controladas. No puede acreditar por sí solo completitud empírica en un sistema real.

### 10.2. Función focal

`F* = modificar técnicamente la configuración problemática`

La función debe definirse antes de examinar alternativas y sin usar Outcome o Value como criterio retrospectivo.

### 10.3. Familias de alternativas

1. Transformaciones directas.
2. Composiciones.
3. Transformaciones distribuidas entre unidades/agentes.
4. Transformaciones indirectas que cambian condiciones para producir F*.
5. Rutas externas al catálogo.

### 10.4. Criterios de dictamen

- **PASS:** universo y límites explícitos, alternativas sistemáticamente examinadas, ninguna ruta sustitutiva respaldada dentro del alcance.
- **FAIL:** existe una transformación/composición alternativa realizable que satisface F* en G0.
- **INDETERMINATE:** alternativas no evaluadas, evidencia insuficiente, condiciones desconocidas o cobertura incompleta.

PASS no significa irreemplazabilidad universal; solo exclusividad respaldada en dominio, granularidad, horizonte y universo auditados. FAIL no implica irrelevancia de τ2; obliga a rediseñar el contraste o estudiar el efecto conjunto de una familia transformacional.

### 10.5. Registro de alternativas

Cada alternativa tendrá:
- ID y función;
- mecanismo;
- realizabilidad y condiciones;
- recursos y dependencias;
- compatibilidad G0/G1;
- horizonte;
- relación con F*;
- evidencias/calidad;
- dictamen y evaluador.

Conservar alternativas descartadas y razones.

### 10.6. Contaminación causal

Comprobar que G0/G1 mantienen constantes recursos, capacidad técnica, información diagnóstica, motivación, incentivos y expectativas, salvo el componente constitutivo deliberadamente intervenido. Si la autorización focal también altera expectativas, prioridades o incentivos, medir esas vías y revisar identificación. No etiquetar automáticamente como “constante” una variable afectada por la intervención.

### 10.7. Dictamen EXC

- PASS: exclusividad respaldada en el ámbito declarado.
- FAIL: alternativa funcional realizable identificada.
- INDETERMINATE: cobertura/evidencia insuficiente.

Una exclusividad indeterminada bloquea la interpretación causal exclusiva de τ2.

---

## 11. Reglas de falsación y evaluación causal

### 11.1. Estimandos a mantener separados

- (TE=E[V(1)-V(0)]): efecto total de asignación/intervención.
- (	heta_A(q)): efecto de políticas específicas de accesibilidad bajo régimen común factible q.
- (	heta_{L,A}): efecto conjunto de condiciones y accesibilidad; no atribución exclusiva a A.
- Residual (TE-	heta_A): solo si escalas, población y descomposición son compatibles; no denominar efecto directo puro.

No asumir aditividad automática ni (TE=	heta_A+	heta_{L,A}). Las interacciones pueden impedir descomposición y el orden de intervenciones puede importar.

### 11.2. S4-O y S4-R

La aleatorización de Z identifica TE bajo supuestos del diseño, no necesariamente θ_A(q). L inducido por Z puede confundir A–V. El analizador debe reconocer el problema.

En S4-R, q* debe corresponder a una intervención real sobre L, seguida de políticas factibles sobre A. No usar (P(L|Z)) observado como régimen común por defecto ni confundir estandarización estadística con intervención.

### 11.3. Umbrales y precisión

- δ: efecto mínimo relevante.
- ε: margen de equivalencia.

Ambos requieren justificación independiente basada en regla Value, beneficiario y contexto; están pendientes. No usar porcentajes si TE≈0, hay signos opuestos o la escala no lo permite.

IC ancho que incluye cero no demuestra ausencia. Solo evidencia precisa dentro del margen preespecificado puede apoyar equivalencia/ausencia de efecto relevante en el ámbito estudiado.

### 11.4. Falsadores/limitadores

- No hay cambio de accesibilidad: manipulación no probada.
- θ_A(q) cercano a cero con precisión y equivalencia justificadas: evidencia contra contribución relevante en el ámbito.
- Signo contrario a predicción direccional preespecificada: evidencia adversa.
- No existe vía mediadora predicha: limita/rechaza el mecanismo.
- Confusión/falta de robustez: atribución insuficiente.
- Heterogeneidad no explicada: limita alcance.
- No-identificación/medición deficiente: no confirma ni refuta.

### 11.5. Tres niveles de inferencia

- A — Existencial: contribución en un ámbito delimitado.
- B — Condicional: condiciones que delimitan aparición, desaparición o dirección.
- C — Generalización: replicación entre dominios y explicación de heterogeneidad.

El objetivo prioritario es B, sin presuponer universalidad.

---

## 12. Criterios de paso de C10-S a C10-P

C10-S solo podrá recomendar pasar al diseño de un piloto real si:

1. recupera correctamente los escenarios nulo, positivo, negativo y heterogéneo;
2. detecta confusión post-tratamiento y no declara identificado S4-O sin estrategia válida;
3. identifica S4-R solo bajo régimen secuencial y soporte definidos;
4. distingue S5-C no identificado de S5-F separable;
5. detecta error de medición S6-N y usa validación en S6-V;
6. recupera cambios de composición S7 sin depender de cardinalidad;
7. reconoce accesibilidad sin Reach en S8;
8. reconoce Value sin accesibilidad en S9;
9. reconoce positividad parcial y condiciones constitutivas en S10;
10. supera pruebas de identidad, composición, generación, independencia y reproducibilidad;
11. la auditoría de exclusividad obtiene PASS dentro del universo sintético cerrado;
12. una auditoría independiente reproduce los dictámenes.

El paso a C10-P no queda autorizado automáticamente por superar C10-S. Requiere selección y auditoría documental del caso, mediciones independientes, estrategia causal, Value, autorización y gobernanza propios.

---

## 13. Riesgos, limitaciones y decisiones pendientes

### 13.1. Pendientes de definición

- relación de identidad ≡I y granularidad definitiva de transformaciones;
- demostración de que no existe ruta alternativa G0 para F*;
- cobertura del universo sintético declarado;
- justificación de factibilidad y manipulación focal de autorización;
- δ y ε;
- cálculo de potencia y precisión Monte Carlo;
- tratamiento de missingness, interferencia y no cumplimiento;
- formalización adicional de Value potencial;
- definición exacta de la unidad de estado y equivalencia de estados;
- criterio de parada/expansión si el catálogo revela alternativas no previstas.

### 13.2. Riesgos metodológicos

- fuga de verdad generadora al analizador;
- circularidad entre T_acc, Outcome y Value;
- confundir accesibilidad con uso/ejecución;
- inferir Reach desde estados observados;
- contar dos veces compuestos y componentes;
- usar el mismo destino como equivalencia;
- omitir rutas alternativas;
- ajustar incorrectamente por L post-tratamiento;
- extrapolar fuera de soporte;
- confundir un ITT de paquete con efecto de A;
- inferir ausencia a partir de falta de significación;
- premiar mecánicamente mayor número de transformaciones;
- generalizar desde un universo sintético cerrado.

### 13.3. Decisiones consolidadas que deben preservarse

1. C10-S es metodología sintética, no evidencia empírica.
2. El generador deriva trayectorias de transformaciones accesibles, relaciones y condiciones, no de secuencias observadas de estados.
3. τ3 mantiene su significado de verificación técnica; no se redefine para validar una transferencia.
4. (r_{43}) queda excluida/inactiva.
5. G0 termina tras τ4; G1 puede ejecutar τ1→τ2→τ3.
6. H=3 aplicaciones efectivas.
7. Cada rama hipotética mantiene estado y condiciones propios.
8. La generación no recibe Outcome ni Value.
9. Accesibilidad, aplicabilidad, alcanzabilidad, selección y ejecución son estados distintos.
10. Identidad y sustituibilidad funcional son juicios distintos.
11. Completitud computacional, representacional y empírica son niveles distintos.
12. No declarar exclusividad si el catálogo o las rutas alternativas son indeterminados.
13. TE, θ_A(q) y efecto conjunto L+A no se intercambian.
14. S4-O no identifica automáticamente θ_A; S4-R exige intervención secuencial.
15. S5-C no permite separar vías colineales; S5-F sí está diseñado para separarlas.
16. Value realizado es primario; Value potencial complementario y pendiente.
17. Tres evaluaciones independientes, sin score global.
18. No pasar a C10-P por el mero hecho de que el código sintético funcione.

---

## 14. Historial de consolidación y trazabilidad conversacional

Este documento normaliza los desarrollos conversacionales C10-S hasta la sección 129. El mapa de correspondencia es:

| Bloque conversacional | Contenido consolidado |
|---|---|
| 44–60 aprox. | C10-A0, cadena sintética, fases, variables y manipulación |
| 61–80 aprox. | Escenarios causales, estimandos, condiciones post-tratamiento y vías alternativas |
| 81–102 aprox. | S0–S10, medición, evaluación ciega, arquitectura y gates |
| 103–110 | Contrato de datos, escenarios y matrices de validación |
| 111–117 | Identidad, equivalencia, sustituibilidad y exclusividad |
| 118–122 | Generador, Reach, pruebas TG y validación cruzada |
| 123–125 | Corrección semántica de τ3, horizonte H=3, ramas independientes y regresión |
| 126 | Contrato formal consolidado del generador |
| 127 | Suficiencia y niveles de completitud |
| 128 | Auditoría de completitud y exclusividad |
| 129 | Consecuencias para identificación causal |

La numeración aproximada de los primeros bloques sirve como trazabilidad de la conversación, no como numeración canónica de secciones del presente documento. Las definiciones y decisiones explícitas de este documento prevalecen sobre formulaciones preliminares corregidas posteriormente.

### 14.1. Correcciones explícitas incorporadas

- Se elimina (r_{43}) como relación activa porque contradice la precondición de τ3.
- Se mantiene τ3 como verificación de configuración técnicamente modificada.
- Se elimina cualquier trayectoria G0 que pretenda terminar en verificación técnica tras τ4.
- Se distingue accesibilidad del catálogo de aplicabilidad en el estado.
- Se separa equivalencia de identidad de sustituibilidad funcional.
- Se separa completitud computacional de completitud empírica.
- Se aclara que el generador produce candidatas, no trayectorias ejecutadas.
- Se aclara que S4-R representa intervención secuencial, no ajuste estadístico.
- Se mantienen S5-C y S5-F como escenarios diferentes.
- Se mantiene Value potencial fuera de la evidencia primaria.

### 14.2. Límites de esta consolidación

La consolidación es una normalización estructurada del material disponible en el historial de trabajo y de las decisiones recuperadas. No afirma ser una transcripción literal de cada intercambio ni sustituye una futura revisión línea por línea del historial si se requiere auditoría textual exhaustiva.

---

## 15. Estado actual y siguiente operación

**Estado documental:** consolidación propuesta, pendiente de revisión y aceptación.  
**Estado científico:** sin cambios.  
**Implementación:** no realizada.  
**Simulación/ejecución:** no realizada.  
**Auditoría de código:** no realizada.  
**Auditoría de resultados:** no realizada.  
**Evidencia empírica C10:** ninguna nueva.  
**Autorización de C10-P:** no concedida por este documento.

Siguiente operación recomendada:
1. revisión científica integral de esta consolidación frente a C10-D1 y las decisiones previas;
2. resolver inconsistencias editoriales y decisiones pendientes;
3. congelar una versión revisada solo tras aceptación explícita;
4. derivar contratos ejecutables y pruebas técnicas desde la versión aceptada;
5. no implementar ni ejecutar hasta autorización expresa.

**Regla de continuidad:** todo nuevo desarrollo C10-S debe actualizar este documento mediante una nueva revisión/versionado o un registro de decisión trazable. No se considerará canónico un desarrollo que permanezca únicamente en memoria de conversación.


---

## 16. Resolución conceptual de auditoría cruzada XAUD-001 / XAUD-002 (sección conversacional 130)

### 16.1. Hallazgos
- **XAUD-001 (crítico):** posible incompatibilidad entre el régimen común q y las políticas g1/g0 si q fija la autorización focal y las políticas g también la modifican.
- **XAUD-002 (alto):** insuficiente separación entre efecto de política y efecto atribuible a accesibilidad.
- Hallazgos asociados: separar accesibilidad verdadera/observada, aplicabilidad y ejecución; no forzar transformaciones que incumplan precondiciones; conservar temporalidad y snapshots de T_acc.

### 16.2. Resolución de q/g
Se distingue el contexto basal común del componente de intervención focal:
- q_X controla una distribución común de contexto e historia preintervención: estado inicial, recursos, capacidad, información basal, necesidad, horizonte y regla Value.
- q_X no fija la autorización focal ni consecuencias posteriores que forman parte del mecanismo.
- g1 y g0 son políticas implementables sobre autorización focal, condicionadas por X e historia basal pertinente.
- A_f* es accesibilidad verdadera derivada de las condiciones efectivas de realizabilidad de τ_f; A_f^obs es su medición.
- La autorización C_auth es condición habilitadora, no una asignación abstracta de A_f*.

DAG focal: Z_A → C_auth → A_f* → T_acc → Π_H → Exec → O → V.

### 16.3. Estimandos separados
**Efecto de política:** ψ_policy(q_X)=E[V^(q_X,g1)]−E[V^(q_X,g0)]. Incluye todas las vías que la política active, incluidas expectativas, incentivos o prioridades si cambian.

**Efecto atribuible a accesibilidad:** θ_Af(q_X), objetivo específico que requiere un diseño capaz de variar accesibilidad sin vías alternativas no separadas, o un diseño adicional que las identifique. No se declara identificado por estimar ψ_policy.

S4-R debe describir q_X y g como componentes implementables y compatibles. No utilizar automáticamente P(L|Z) observado como régimen común ni sustituir intervención por estandarización retrospectiva.

### 16.4. Modalidades y cumplimiento
- Modalidad A — manipulación técnica aislada: preferida para C10-S; cambia la condición técnica focal sin alterar información, incentivos, expectativas, trato o recursos no focales.
- Modalidad B — política de autorización: puede activar otras vías; requiere diseño factorial u otra estrategia de separación e interacciones explícitas.

Registrar separadamente Z, C_auth, A_f*, A_f^obs, App_f y Exec_f. Una trayectoria experimental estandarizada no puede forzar una transformación inaccesible. La ejecución debe respetar precondiciones; selección libre es un régimen distinto.

### 16.5. Dictamen
- XAUD-001: resuelto conceptualmente, pendiente de cierre formal por auditoría.
- XAUD-002: parcialmente resuelto; estimandos separados, pero identificación específica de θ_Af depende del diseño implementado.
No se modifica el estado científico ni se declara resuelta la identificación empírica de C10.

---

## 17. Matriz de identificación de vías causales y controles negativos (sección 131)

### 17.1. DAG ampliado
Se conserva Z_A → C_auth → A_f* → T_acc → Π_H → Exec → O → V y se explicitan:
- Z_A → L_d → V: variables posteriores que afectan directamente Value.
- Z_A → L_m → A_f* → V: condiciones inducidas que afectan accesibilidad y Value.
- X → (A_f*, Π_H, O, V): contexto basal.
- T_acc → Π_H → Exec: selección y ejecución.

L_d y L_m se clasifican por historia temporal y función causal. No ajustar indiscriminadamente por variables posteriores al tratamiento.

### 17.2. Escenarios C131
| ID | Accesibilidad focal | Vía alternativa | Value | Interpretación |
|---|---|---|---|---|
| C131-01 | Cambia | Ausente | Positivo | Atribución recuperable si el diseño identifica |
| C131-02 | Cambia | Ausente | Nulo | Accesibilidad cambia sin contribución Value detectable |
| C131-03 | Cambia | Ausente | Negativo | Efecto adverso atribuible si se identifica |
| C131-04 | No cambia | Presente | Positivo | No atribuir a accesibilidad |
| C131-05 | Cambia | Presente | Positivo | Separar contribuciones solo si el diseño lo permite |
| C131-06 | Cambia | Presente | Total nulo | No inferir ausencia; puede haber compensación |
| C131-07 | Cambia | Variable por X | Heterogéneo | Recuperar heterogeneidad contextual |
| C131-08 | No cambia | Ausente | Nulo | Control negativo completo |
| C131-09 | Cambia | Ausente | No identificable | Declarar límite de identificación |
| C131-10 | No cambia | Presente | Negativo | Reconocer efecto adverso alternativo |

### 17.3. Controles negativos
- NC-A: ΔT_acc ≠ 0 y ΔReach ≠ 0, pero θ_Af = 0. Expansión no garantiza Value.
- NC-B: ΔT_acc = 0 y ΔV ≠ 0. Value puede cambiar por vía alternativa.
- NC-C: ΔT_acc ≠ 0 y ΔReach ≠ 0, pero Exec_f = 0. No inferir ejecución.

Un TE nulo puede ocultar efectos contrapuestos; por ejemplo θ_Af=+6 y θ_alt=−6. Sin diseño que separe vías no se declaran identificadas ambas contribuciones.

### 17.4. Ecuaciones y arquitectura ciega
Modelo simplificado: M=α_A A_f+α_X X+ε_M; O=β_M M+β_X X+ε_O; V=γ_O O+γ_L L+ε_V. Sin interacciones, contribución estructural θ_Af=α_A β_M γ_O. Con interacciones no se presupone aditividad.

El analizador recibe asignación/historial, probabilidades, autorización, accesibilidad observada y calidad, catálogo/relaciones, Reach/trayectorias, selección/ejecución, Outcome, Value y regla evaluativa. No recibe coeficientes verdaderos, A_true oculto ni etiquetas de escenario. El evaluador conserva el DGP. Tres dictámenes independientes: reconstrucción TGCV, identificación causal y Value; sin puntuación global.

---

## 18. Identificación causal frente a recuperación estadística (sección 132)

### 18.1. Dos preguntas
**Identificabilidad:** diseño y supuestos permiten determinar el estimando a partir de datos observables. **Recuperación:** dado un estimando identificado, el procedimiento lo estima con sesgo, incertidumbre y cobertura aceptables.

La aleatorización de Z puede identificar ITT: TE_Z=E[V|Z=1]−E[V|Z=0], pero no identifica automáticamente θ_Af. Precisión no demuestra identificación.

### 18.2. Matriz
| Identificación | Recuperación | Dictamen |
|---|---|---|
| Sí | Sí | Resultado causal recuperado dentro del modelo |
| Sí | No | Diseño válido; estimación defectuosa/insuficiente |
| No | Sí aparente | Precisión engañosa; no atribuir causalidad |
| No | No | No concluyente por ambas vías |

### 18.3. Identificabilidad esperada por escenario
| Escenario | Identificación esperada | Condición/límite |
|---|---|---|
| S0 | Nulo identificable en DGP | Variación válida y sin vía alternativa |
| S1 | Positivo | Asignación focal aislada |
| S2 | Negativo | No imponer signo positivo |
| S3 | Heterogeneidad | Medir X e interacción A×X; estratos y promedio |
| S4-O | TE de Z | θ_Af no automáticamente identificado; L postratamiento |
| S4-R | θ_A(q*) | Intervención secuencial, soporte y políticas factibles |
| S5-C | TE de Z | A y alternativa colineales; contribuciones no separables |
| S5-F | Efectos de asignaciones independientes | Separación bajo supuestos |
| S6-N | A verdadero no identificado en general | Error sin validación; sensibilidad no es corrección |
| S6-V | Potencialmente identificable | Submuestra de validación adecuada e independiente |
| S7 | Cambio de composición | No implica efecto sobre Value |
| S8 | Accesibilidad sin Reach | No atribuir mediación por Reach si no cambia |
| S9 | Efecto alternativo | A no cambia; efecto de accesibilidad nulo |
| S10a | Efecto en estrato con soporte | Población completa no identificada sin datos/supuestos |
| S10b | Efecto donde ambas políticas son factibles | Contraste original imposible en estrato constitutivo |

S7/S8 son controles de reconstrucción TGCV, no pruebas de atribución causal a Value.

### 18.4. Familias de estimadores
| Diseño/estimando | Familia | Límite |
|---|---|---|
| Asignación aleatoria Z | Diferencia de medias/regresión ajustada preespecificada | ITT, no θ_Af automáticamente |
| Políticas secuenciales q,g1,g0 | G-computation, ponderación inversa o TMLE | Supuestos/soporte; no efectos naturales automáticamente |
| Heterogeneidad por X | Estratificación/interacción | No extrapolar sin soporte |
| A con error | Validación/sensibilidad | No corregir con tasas supuestas como si fueran verdad |
| Instrumento para A | Métodos instrumentales | Relevancia, independencia, exclusión, monotonicidad; alcance local |
| Vías alternativas independientes | Diseño factorial/efectos conjuntos | Estimar interacción; no asumir aditividad |

Mantener ψ_policy y θ_Af separados.

### 18.5. Diagnósticos y Monte Carlo
Antes de estimar: positividad, consistencia, temporalidad, confusión basal/postratamiento, vías alternativas, medición, interferencia y datos ausentes. No corregir automáticamente un diagnóstico negativo; ajustar por variables posteriores puede introducir sesgo.

Métricas de recuperación: sesgo, RMSE, cobertura IC, error tipo I, potencia, calibración, convergencia y error Monte Carlo. Solo aplicarlas como recuperación de un estimando identificado. En escenarios no identificados evaluar si el analizador reconoce correctamente la no-identificación.

N=2.000 por réplica, R=1.000, asignación 1:1, α=.05 e IC95% siguen siendo provisionales; no constituyen cálculo de potencia. δ, ε y tolerancias pendientes.

### 18.6. Estados
Identificación: ID-01 identificado; ID-02 condicional; ID-03 parcial; ID-04 no identificado; ID-05 no factible; ID-06 indeterminado.

Recuperación: REC-01 satisfactoria; REC-02 sesgada; REC-03 mal calibrada; REC-04 inestable; REC-05 no evaluable por falta de identificación; REC-06 inconclusa por precisión insuficiente.

ID-04 ≠ ID-05. REC-05 no es fallo estadístico. Un IC ancho que incluye cero no prueba ausencia.

---

## 19. Contrato de resultados y reglas de interpretación (sección 133)

### 19.1. Niveles e identificadores
L1 unidad sintética; L2 réplica; L3 escenario; L4 experimento. Registrar experiment_id, scenario_id, replicate_id, unit_id, design_version, transform_catalog_version, causal_model_version, value_rule_version, analysis_version y random_seed.

### 19.2. Contrato por unidad
Registrar:
1. Diseño: X, Z/probabilidades, condiciones basales/posteriores, q, g e historial.
2. Transformacional: catálogo, accesibilidad/inaccesibilidad/indeterminación, relaciones, dependencias, A_f*, A_f^obs, T_acc, Reach, trayectorias candidatas/seleccionadas/ejecutadas.
3. Evolución: mecanismos, ejecución, Outcome, dimensiones Value, Value agregado si procede, incertidumbre y missingness.
4. Calidad: fuente, medición, calidad, versiones, incidencias y exclusiones.

No reconstruir T_acc retrospectivamente desde Outcome o Value.

### 19.3. Contrato por estimando
Cada resultado registra estimand_id, definición, población, contraste, resultado, regla Value, horizonte, identificación, supuestos, estimador, estimación, error estándar, IC, N efectivo, diagnósticos, recuperación e interpretación. Separar TE_Z, ψ_policy(q_X), θ_Af(q_X), efectos de mecanismos/alternativas y heterogeneidad. No usar una columna genérica causal_effect.

### 19.4. Dictámenes
- ID-01 identificado; ID-02 condicional; ID-03 parcial; ID-04 no identificado; ID-05 no factible; ID-06 indeterminado.
- REC-01 satisfactoria; REC-02 sesgada; REC-03 incertidumbre mal calibrada; REC-04 inestable; REC-05 no evaluable; REC-06 inconclusa.

Interpretación conjunta: ID-01+REC-01 permite recuperación dentro del DGP; ID-01+REC-02/03/04 exige revisar estimador/modelo; ID-04+REC-05 obliga a declarar no-identificación; ID-02 exige supuestos y sensibilidad; ID-03 exige conjunto identificado; ID-05 impide presentar el contrafactual original como estimado; ID-06 no autoriza conclusión afirmativa/negativa.

### 19.5. Dictamen transformacional
TGCV-01 reconstrucción satisfactoria; TGCV-02 error identidad/equivalencia; TGCV-03 error accesibilidad/admisibilidad; TGCV-04 error composición/dependencia; TGCV-05 error Reach/trayectoria; TGCV-06 contaminación Outcome/Value; TGCV-07 indeterminado.

### 19.6. Value e informe
Registrar beneficiario, objetivo, criterios, regla/pesos, dirección, horizonte, costes/beneficios, trade-offs, incertidumbre y Value realizado. Value potencial es complementario y no sustituye Value realizado ni demuestra causalidad por expansión de opciones.

Informe por escenario: DGP/diseño; manipulación; T_acc/Reach/trayectorias; ejecución/Outcome; Value; identificación; recuperación; diagnósticos/sensibilidad; dictámenes separados; limitaciones. No declarar C10-S validado si alguna dimensión falla o es indeterminada.

---

## 20. Agregación y dictamen global de C10-S (sección 134)

### 20.1. Principios
No compensación; dimensiones separadas; trazabilidad; reproducibilidad; incertidumbre explícita; fallo cerrado ante evidencia ausente. No promediar escenarios con DGP/estimandos distintos.

### 20.2. Grupos
- Fundamentales: S0–S3 (nulo, positivo, negativo, heterogeneidad).
- Identificación/vías alternativas: S4-O/R, S5-C/F, S9, S10a/b.
- Integridad transformacional/medición: S6-N/V, S7, S8.

Controles críticos no compensables: S0, S2, S3, S4-O, S4-R, S5-C, S5-F, S9, S10a y S10b.

### 20.3. Cuatro controles por escenario
A. Fidelidad del generador. B. Reconstrucción transformacional. C. Identificación causal. D. Recuperación estadística cuando proceda.

Estados: PASS, FAIL, INDETERMINATE, NOT_APPLICABLE. NOT_APPLICABLE no equivale a PASS.

### 20.4. Agregación Monte Carlo
Para R réplicas y valor verdadero θ:
- Bias = promedio de (θ̂_r−θ).
- RMSE = raíz del promedio de (θ̂_r−θ)^2.
- Coverage = proporción de IC_r que contienen θ.

Informar distribución, convergencia, amplitud de intervalos, error Monte Carlo, sensibilidad y estratos. En escenarios no identificados evaluar reconocimiento correcto de no-identificación, no sesgo respecto de coeficiente oculto. Umbrales pendientes y preespecificados antes de ejecución.

### 20.5. Dictámenes independientes
TGCV: reconstrucción del espacio transformacional. Causal: identificación y recuperación de contribución causal. Value: construcción/estimación independiente y coherente. Efecto de política identificado no implica efecto de accesibilidad identificado.

### 20.6. Dictamen global
- C10S-01: superado metodológicamente; controles críticos y auditoría satisfechos; permite preparar C10-P.
- C10S-02: superado con límites; piloto restringido al ámbito demostrado.
- C10S-03: superación parcial; rediseño concreto.
- C10S-04: fallido; requisitos esenciales incumplidos.
- C10S-05: indeterminado; evidencia insuficiente.

C10-S superado no demuestra C10; demuestra solo que el protocolo puede investigar la hipótesis distinguiendo accesibilidad, ejecución, Outcome y Value.

### 20.7. Rediseño
Rediseñar ante filtración de verdad, reconstrucción retrospectiva de T_acc, confusión política/accesibilidad, falsa atribución en escenarios no identificados, vías alternativas omitidas, dependencia no controlada de orden/seed/configuración, Value que premie expansión mecánicamente o agregación que oculte fallos.

Estado: arquitectura de decisión definida; umbrales pendientes; no implementado ni ejecutado.

---

## 21. Preespecificación cuantitativa y control de decisiones posteriores (sección 135)

### 21.1. Objetivo
Evitar modificar umbrales, márgenes, escenarios o reglas tras observar resultados para conseguir un dictamen favorable. Separar parámetros del DGP, diseño, evaluación estadística y decisión científica.

### 21.2. Cuatro capas
| Capa | Contenido | Regla |
|---|---|---|
| DGP | Ecuaciones, coeficientes verdaderos, distribuciones, interacciones, mecanismos | Congelar antes de generar |
| Diseño | Unidad, asignación, tamaño, réplicas, horizonte, seeds, missingness, interferencia | Congelar antes de ejecutar |
| Evaluación | Estimandos, estimadores, tolerancias, cobertura, sesgo, potencia, error tipo I | Justificar antes de analizar |
| Decisión científica | δ, ε, dirección esperada, falsadores, límites, gates | Derivar de Value/alcance antes de resultados |

No cambiar una capa silenciosamente para corregir resultados desfavorables en otra.

### 21.3. Registro de parámetros
Cada parámetro registra parameter_id, definición/unidad, capa, valor/rango, justificación, fuente/derivación, sensibilidad, estado (provisional/propuesto/preespecificado/congelado), versión/fecha y responsable.

### 21.4. Pendientes prioritarios
1. δ: efecto mínimo relevante, vinculado a regla Value, beneficiario, escala y horizonte.
2. ε: margen de equivalencia justificado independientemente de resultados.
3. Tolerancias de sesgo y RMSE por estimando.
4. Cobertura y precisión Monte Carlo admisibles.
5. Convergencia y proporción máxima de réplicas inválidas.
6. Potencia y tamaños muestrales justificados.
7. Missingness, interferencia y no cumplimiento.
8. Sensibilidad ante error de medición y especificación.

N=2.000 por réplica y R=1.000 son propuestas iniciales, no decisiones congeladas ni cálculo de potencia.

### 21.5. Prohibición de adaptación post-resultados
Tras la primera ejecución no cambiar silenciosamente DGP/coeficientes, identidad/granularidad, H, población/estimandos, regla Value, estimador primario, δ/ε/tolerancias, escenarios críticos o PASS/FAIL.

Toda modificación posterior requiere nueva versión, motivación, impacto esperado, análisis afectados y preservación íntegra de resultados anteriores.

### 21.6. Confirmatorio, exploratorio y sensibilidad
- Confirmatorio: criterios congelados antes de generar/analizar resultados.
- Exploratorio: análisis adicional rotulado; no sustituye confirmatorio.
- Sensibilidad: variaciones preespecificadas; no seleccionar retrospectivamente el modelo más favorable.

### 21.7. Registro de desviaciones
Registrar deviation_id, versión, fecha, motivo, autorización, momento respecto a resultados, variables/estimandos afectados y análisis original/revisado. No eliminar historial.

### 21.8. Gate previo a simulación confirmatoria
No comenzar hasta versionar DGP/escenarios; definir estimandos/población; fijar Value; justificar δ/ε o declarar inferencias no disponibles; definir criterios de recuperación/precisión; justificar N y réplicas; congelar analizador/evaluador y datos permitidos; registrar seeds/configuración/agregación; activar registro de desviaciones; y superar auditoría independiente previa.

Si falta un requisito, el resultado será exploratorio o la ejecución quedará bloqueada según la naturaleza del requisito.

### 21.9. Estado
Definidos conceptualmente: capas de preespecificación, registro, separación confirmatoria/exploratoria y control de desviaciones. Pendientes: valores, justificaciones, tolerancias y auditoría previa. No realizado: implementación, simulación, ejecución y análisis. No autorizado: ejecución confirmatoria o transición automática a C10-P.

---

## 22. Historial incremental de consolidación

| Secciones conversacionales | Incorporación |
|---|---|
| 130 | Resolución XAUD-001/002 y compatibilidad q/g |
| 131 | Vías causales, controles negativos y efectos contrapuestos |
| 132 | Identificación frente a recuperación estadística |
| 133 | Contrato de resultados y estados de interpretación |
| 134 | Agregación, escenarios críticos y dictamen global |
| 135 | Preespecificación cuantitativa y control de decisiones posteriores |

Las secciones 16–22 amplían incrementalmente el borrador 004. No convierten definiciones en implementación, ejecución, auditoría o aceptación. La numeración conversacional y documental quedan vinculadas en esta tabla; las decisiones explícitas prevalecen sobre formulaciones preliminares corregidas.


---

## 23. Método de justificación de umbrales y dimensionamiento (sección conversacional 136)

### 23.1. Objetivo y separación de decisiones

Esta sección establece cómo justificar los parámetros pendientes de la sección 21 sin introducir valores arbitrarios ni seleccionarlos después de observar resultados. Se distinguen cuatro decisiones que no deben confundirse:

1. **Relevancia sustantiva:** qué cambio en Value importa para el beneficiario y la decisión evaluada.
2. **Calidad estadística:** qué error de estimación es tolerable para el uso previsto.
3. **Capacidad de diseño:** qué tamaño y número de réplicas permiten evaluar los criterios con precisión suficiente.
4. **Regla científica:** qué patrón de resultados respalda, limita o contradice la hipótesis dentro del ámbito especificado.

Los umbrales estadísticos no deben definir por sí mismos qué es Value relevante. La relevancia sustantiva tampoco puede justificar un estimador estadísticamente defectuoso.

### 23.2. Justificación de δ: efecto mínimo relevante

δ debe derivarse de la regla de Value y de la decisión concreta que el sistema evaluado pretende apoyar. Su expediente de justificación debe identificar:

- beneficiario o entidad evaluada;
- decisión que cambiaría ante un efecto de ese tamaño;
- escala, unidad y dirección de Value;
- horizonte temporal;
- costes, riesgos y trade-offs relevantes;
- heterogeneidad que pueda hacer variar la relevancia;
- fuente externa, criterio operativo o procedimiento deliberativo que justifique el umbral;
- incertidumbre de la propia valoración del umbral.

δ no se elegirá para coincidir con el efecto esperado del DGP ni para producir una potencia conveniente. Si Value es multidimensional o no agregable, no se impondrá un δ escalar artificial: se definirán criterios por dimensión o una regla de decisión explícita y justificada.

### 23.3. Justificación de ε: margen de equivalencia

ε responde a una pregunta distinta: qué diferencias pueden considerarse suficientemente pequeñas como para descartar un efecto de relevancia práctica dentro del ámbito especificado.

Debe:
- derivarse de la escala y regla de Value;
- justificarse independientemente de los resultados observados;
- especificar si el margen es simétrico o asimétrico;
- ser compatible con δ, sin solapamientos que hagan incoherentes las categorías;
- reflejar incertidumbre, costes de error y consecuencias de declarar equivalencia.

No se concluirá equivalencia porque un IC incluya cero. Se requerirá que el procedimiento de inferencia y el intervalo correspondiente queden dentro del margen preespecificado. Si no existe justificación defendible de ε, C10-S podrá evaluar estimación y calibración, pero no podrá emitir un dictamen de equivalencia sustantiva.

### 23.4. Tolerancias de recuperación estadística

Las tolerancias se definirán por estimando y escala, no como un único umbral global. El expediente incluirá:

- sesgo absoluto admisible;
- RMSE admisible;
- cobertura objetivo y desviación Monte Carlo tolerable;
- tasa de error tipo I;
- potencia mínima para efectos relevantes;
- proporción máxima de no convergencia o réplicas inválidas;
- precisión mínima de las métricas Monte Carlo.

Cuando sea útil, sesgo y RMSE podrán expresarse en relación con δ, pero esa normalización no sustituye la justificación sustantiva ni se utilizará si δ no está definido o si la escala cruza cero de forma problemática.

Los criterios deberán ser coherentes con el uso del estimador y la severidad de los errores: un falso positivo de atribución causal, una falsa declaración de equivalencia y una no detección no tienen necesariamente el mismo coste.

### 23.5. Dimensionamiento de N y R

Separar dos tamaños:

- **N:** unidades sintéticas por réplica; determina la información disponible en cada dataset generado.
- **R:** número de réplicas Monte Carlo; determina la precisión con que se estiman las propiedades del procedimiento estadístico.

N se elegirá mediante análisis de potencia/precisión sobre una cuadrícula preespecificada de efectos, heterogeneidad, prevalencias, error de medición, missingness y mecanismos alternativos. La cuadrícula debe incluir escenarios adversos plausibles, no solo el DGP favorable.

R se elegirá para que el error Monte Carlo de cobertura, potencia, sesgo y tasa de falsos positivos sea suficientemente pequeño respecto de las tolerancias de evaluación. Aumentar R no compensa un N insuficiente; aumentar N no corrige una identificación fallida.

La elección se documentará por escenario y estimando. Un N común puede ser operativo, pero no se supondrá adecuado para todos los contrastes sin demostrarlo.

### 23.6. Dos ejecuciones Monte Carlo con funciones diferentes

**MC-CAL — calibración de diseño:** explora rangos plausibles para justificar N, R, precisión y sensibilidad del diseño. Sus resultados sirven para elegir el diseño y no se presentan como prueba confirmatoria de que el analizador supera los escenarios.

**MC-EVAL — evaluación confirmatoria metodológica:** utiliza la versión congelada del DGP, estimadores, criterios, N, R, seeds y agregación. Evalúa la recuperación y la detección de no-identificación.

MC-CAL y MC-EVAL deben diferenciarse por versión, configuración y semillas. No se reutilizarán los mismos resultados de calibración como evidencia confirmatoria. Las decisiones derivadas de MC-CAL deben registrarse antes de iniciar MC-EVAL.

### 23.7. Cuadrícula de sensibilidad obligatoria

La calibración debe explorar, cuando sean pertinentes:
- efectos nulos, positivos, negativos y cercanos a δ;
- heterogeneidad por X y cambios de signo;
- vías alternativas que refuercen o contrarresten la vía focal;
- solapamiento y pérdida de positividad;
- incumplimiento y contaminación de la intervención;
- error de medición de accesibilidad;
- missingness diferencial;
- interferencia entre unidades;
- errores de especificación y alternativas de estimador.

Los rangos se justifican antes de la evaluación confirmatoria. No se escogerá como escenario principal el que produzca mejores métricas.

### 23.8. Regla para escenarios no identificados

S5-C, S10a y S10b conservan su función de controles de identificación. No se incrementará N indefinidamente para forzar un estimando que el diseño no identifica.

- Si el problema es falta de soporte, informar el estrato identificable y el alcance poblacional.
- Si la intervención es contrafactualmente imposible, redefinir la población o el estimando de manera explícita; no simular factibilidad.
- Si dos vías están perfectamente colineales, introducir una asignación independiente o aceptar la no-identificación.
- Si falta medición de A verdadera, diseñar validación o limitar la conclusión a A observada bajo supuestos explícitos.

### 23.9. Expediente de justificación y aprobación

Antes de MC-EVAL debe existir una tabla de control con:
- parámetro y estimando al que aplica;
- valor propuesto y unidad;
- justificación sustantiva/estadística;
- análisis de calibración que lo informa;
- sensibilidad y escenarios adversos;
- autoridad/registro de aprobación;
- versión congelada y hash;
- fecha y relación con el protocolo.

No se inventarán aprobaciones ni se inferirá aceptación a partir de que el valor aparezca en un documento.

### 23.10. Gate de dimensionamiento

El dimensionamiento queda satisfecho solo cuando:
1. δ y ε tienen justificación independiente o se declara formalmente qué conclusiones quedan fuera de alcance;
2. tolerancias estadísticas están vinculadas a los estimandos y costes de error;
3. N y R se justifican mediante MC-CAL;
4. la cuadrícula cubre escenarios adversos y no solo favorables;
5. MC-CAL y MC-EVAL están separados;
6. escenarios no identificados no se tratan como problemas de potencia;
7. la versión final queda congelada y auditada antes de MC-EVAL.

### 23.11. Estado

**Definido:** procedimiento para justificar δ/ε, tolerancias, N/R, cuadrícula de sensibilidad y separación MC-CAL/MC-EVAL.  
**Pendiente:** contexto de Value y beneficiario del futuro C10-P, escalas, costes de error, valores numéricos y auditoría de dimensionamiento.  
**No realizado:** cálculo de potencia, simulación de calibración, simulación confirmatoria, implementación o ejecución.  
**Regla:** no asignar valores numéricos a δ, ε, N o R como si estuvieran justificados hasta completar el expediente correspondiente.


---

## 24. Auditoría independiente previa a implementación y ejecución (sección conversacional 137)

### 24.1. Propósito y frontera

La auditoría previa debe comprobar que el protocolo, sus contratos y sus decisiones son internamente coherentes y suficientemente determinados antes de traducirlos a código o ejecutar MC-CAL/MC-EVAL.

La auditoría no implementa, no simula, no ejecuta C10-S y no demuestra C10. Su resultado es una decisión sobre la aptitud metodológica del paquete para pasar a la siguiente fase técnica.

### 24.2. Independencia y separación de funciones

Distinguir:
1. **Autoría del protocolo:** propone definiciones, escenarios y criterios.
2. **Auditoría transformacional:** revisa identidad, accesibilidad, condiciones, relaciones, composición, Reach y trayectorias.
3. **Auditoría causal/estadística:** revisa DAG, estimandos, identificación, soporte, estimadores, calibración, potencia y reglas de interpretación.
4. **Auditoría de Value:** revisa beneficiario, regla, dimensiones, escalas, horizonte, trade-offs y ausencia de circularidad.
5. **Auditoría de reproducibilidad y cegamiento:** revisa separación generador/analizador/evaluador, control de filtraciones, versionado y reproducibilidad.
6. **Autoridad de aceptación:** emite la decisión formal de aceptar, devolver o bloquear.

Cuando no sea posible disponer de auditores distintos para cada área, se registrarán conflictos de rol y medidas compensatorias. El autor del protocolo no puede ser el único evaluador de su propia aceptación.

### 24.3. Paquete de auditoría

El paquete debe incluir:
- borrador C10-S versionado y su hash;
- C10-D1 vigente y su hash;
- matriz de correspondencia entre ambos documentos;
- DAG y diccionario de variables;
- estimandos y supuestos de identificación;
- catálogo transformacional, condiciones, relaciones y equivalencias;
- escenarios y DGP con parámetros verdaderos separados del material del analizador;
- contratos del generador, analizador y evaluador;
- matriz de pruebas EQ, EX, GEN, TG, SR, CV y Value;
- reglas de resultados, agregación y dictamen;
- expediente de δ, ε, tolerancias y dimensionamiento, o lista explícita de conclusiones fuera de alcance;
- política de seeds, versiones, hashes y desviaciones;
- registro de decisiones abiertas y hallazgos anteriores.

No incluir secretos de verdad generadora en el paquete que recibirá el analizador ciego. La auditoría puede verificar el canal protegido de verdad sin exponerlo al componente evaluado.

### 24.4. Matriz de auditoría

| Dominio | Pregunta de auditoría | Evidencia mínima |
|---|---|---|
| Coherencia documental | ¿C10-S es compatible con C10-D1 y no altera silenciosamente estimandos? | Matriz de correspondencia y hashes |
| Identidad transformacional | ¿Identidad y granularidad son operativas y consistentes? | Reglas EQ y ejemplos límite |
| Accesibilidad | ¿Se separan realizabilidad, accesibilidad, aplicabilidad y ejecución? | Predicados, evidencia y pruebas |
| Composición/Reach | ¿El generador deriva rutas de T_acc y reevalúa condiciones por rama? | Contrato y pruebas TG/GEN |
| Exclusividad | ¿Se han examinado alternativas en G0 dentro del alcance declarado? | Expediente EXC y límites de completitud |
| Identificación causal | ¿Cada estimando tiene intervención, población, supuestos y soporte definidos? | DAG, contratos y escenarios |
| Medición | ¿A_true, A_obs y error se mantienen separados? | Plan de medición/validación |
| Value | ¿La regla es independiente y no recompensa mecánicamente expansión? | Especificación Value y pruebas V |
| Estadística | ¿Estimadores y métricas corresponden al estimando y al diseño? | Plan analítico y MC-CAL |
| Preespecificación | ¿Criterios y desviaciones se congelan antes de MC-EVAL? | Registro versionado |
| Cegamiento | ¿El analizador no recibe verdad generadora ni etiquetas reveladoras? | Mapa de datos y prueba de leakage |
| Reproducibilidad | ¿Cada resultado puede vincularse a versión, seed y configuración? | Contrato de artefactos |
| Gobernanza | ¿Está claro qué queda autorizado y qué permanece bloqueado? | Decisión formal y registro de permisos |

### 24.5. Severidad de hallazgos

- **P0 — bloqueante:** amenaza identificación, validez del constructo, integridad del cegamiento o interpretación central. Impide pasar a implementación/ejecución.
- **P1 — mayor:** puede alterar resultados, estimandos, completitud o reproducibilidad. Requiere resolución antes de la fase afectada.
- **P2 — menor:** defecto editorial, trazabilidad o claridad que no cambia el significado, pero debe corregirse antes de congelar.
- **OBS — observación:** mejora recomendada o limitación explícita que no bloquea el gate.

No cerrar hallazgos por reformulación textual si la contradicción subyacente permanece. Toda resolución debe apuntar a evidencia y versión concreta.

### 24.6. Estados del gate de auditoría

- **AUDIT-PASS:** no quedan P0/P1 abiertos; los P2 están corregidos o tienen disposición documentada; los límites están explícitos.
- **AUDIT-CONDITIONAL:** no quedan P0, pero existen condiciones delimitadas que bloquean únicamente fases posteriores concretas.
- **AUDIT-FAIL:** persiste al menos un P0 o una incoherencia que impide interpretar el diseño.
- **AUDIT-INDETERMINATE:** falta material o evidencia para emitir dictamen.

Un AUDIT-PASS documental autoriza únicamente a proponer la traducción técnica. No autoriza por sí solo ejecución científica, simulación confirmatoria, selección de caso real ni C10-P.

### 24.7. Cierre de hallazgos y trazabilidad

Cada hallazgo conserva:
- audit_id y finding_id;
- severidad;
- documento/sección/versión afectados;
- descripción y fundamento;
- consecuencia metodológica;
- resolución propuesta;
- evidencia de resolución;
- revisor y fecha;
- estado (open, resolved, accepted-risk, superseded);
- versión en que se resolvió.

Los hallazgos aceptados como riesgo deben tener justificación, alcance y consecuencia explícitos. No se eliminan hallazgos cerrados ni se sobrescriben auditorías anteriores.

### 24.8. Gate de transición

La transición documental a implementación requiere AUDIT-PASS o AUDIT-CONDITIONAL con condiciones compatibles con esa implementación, más aceptación formal de la versión.

La implementación técnica requiere además contrato ejecutable, pruebas y autorización específica. MC-CAL y MC-EVAL requieren gates y autorizaciones separados. La ejecución confirmatoria y C10-P siguen bloqueadas hasta sus propios controles.

### 24.9. Estado

**Definido:** independencia de funciones, paquete de auditoría, matriz, severidad, estados y gates.  
**Pendiente:** asignación real de auditores, revisión integral C10-S frente a C10-D1, resolución de hallazgos y aceptación formal.  
**No realizado:** auditoría independiente, implementación, simulación o ejecución.  
**No autorizado por esta sección:** ejecución científica o avance automático a C10-P.


---

## 25. Auditoría cruzada C10-S ↔ C10-D1: coherencia de estimandos, intervenciones y constructos (sección conversacional 138)

**Fuentes contrastadas:**
- C10-S consolidado, borrador 004, rama research/c10-s-consolidation-draft.
- C10-D1, C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md, rama research/c10-d1-protocol-draft, blob SHA bf25f6ec8965166e5fa52ff18e6d07613bad0eb3.

**Estado:** auditoría documental de coherencia; no es aceptación ni auditoría de implementación. No modifica C10-D1, Core, RMA, Matrix, STATUS ni claims.

### 25.1 Regla de precedencia

C10-D1 contiene precisiones posteriores sobre condiciones constitutivas, factibilidad de políticas, versiones de intervención, dinámica longitudinal, selección/ejecución y notación. C10-S debe ser compatible con ellas. En caso de diferencia:
1. las definiciones de C10-D1, especialmente sus apartados 17, 24, 25, 26–30, son la referencia causal vigente de trabajo;
2. C10-S describe cómo probar metodológicamente esas definiciones en un entorno sintético;
3. una simplificación de C10-S no puede convertir una intervención implementable en una asignación abstracta de accesibilidad ni cambiar el significado del estimando;
4. toda adaptación sintética debe identificarse como tal y preservar las restricciones de factibilidad.

### 25.2 Hallazgos de auditoría

| ID | Severidad provisional | Hallazgo | Consecuencia | Disposición requerida |
|---|---|---|---|---|
| XSYNC-138-01 | P0 — bloqueante para congelación causal | C10-S §16.3 define g1/g0 como políticas sobre autorización focal; C10-D1 §§17.5, 17.7 y 26 define g1/g0 como políticas implementables sobre cambios de accesibilidad, inducidos por componentes B/Z y respetando el conjunto factible. | Puede confundirse efecto de política de autorización con θ_A(q), o tratar autorización como si fuera accesibilidad. | Reformular el mapeo B/Z → condiciones/intervención → A=ΔT_acc; mantener ψ_policy como efecto de política y θ_A(q) como contraste entre políticas factibles de accesibilidad. |
| XSYNC-138-02 | P1 | C10-S §16.2 incluye la regla de Value dentro de los elementos controlados por q_X. C10-D1 define q como régimen común de condiciones/historias; la regla de Value es una regla evaluativa fijada para el contraste, no una condición aleatoria de q. | Mezcla régimen causal con definición del resultado y puede introducir diferencias evaluativas entre regímenes. | Separar q_X de la regla Value; fijar beneficiario, criterio, escala y horizonte como parte del resultado/estimando, constantes en el contraste salvo que la pregunta estudie explícitamente un cambio evaluativo. |
| XSYNC-138-03 | P1 | C10-S utiliza A_f* como indicador focal binario y en algunos pasajes aproxima A a ΔT_acc. C10-D1 §27 define ΔT_acc como objeto estructurado que puede incluir A+, A−, reconfiguración, cambios relacionales y configuracionales. | El indicador focal puede confundirse con el cambio completo del espacio transformacional. | Declarar A_f* como componente/indicador de accesibilidad de una transformación focal τ_f; preservar ΔT_acc estructurado como constructo TGCV más amplio. Definir la proyección focal y sus límites. |
| XSYNC-138-04 | P1 | S4-R usa q*(L=1|X)=0.5 y políticas g1=.8/g0=.2 bajo la premisa de factibilidad en todos los estratos, pero no separa explícitamente L_c de L_m ni demuestra que las cuatro asignaciones sean realizables. | Puede generar contrafactuales imposibles o falta de positividad. | Especificar que el L de S4-R representa condiciones no constitutivas compatibles con el contraste; si incluye L_c, definir conjuntos factibles por historia. Verificar soporte de ambas políticas en cada estrato y declarar no identificación si falla. |
| XSYNC-138-05 | P1 | C10-D1 §24.3 mantiene θ_A^dyn como marcador pendiente de formalización. C10-S no debe sugerir que existe ya un estimando dinámico listo para estimación. | Riesgo de tratar una etiqueta como estimando definido. | Mantener θ_A^dyn fuera del conjunto de estimandos evaluables hasta fijar historia, políticas dinámicas, factibilidad, población, Value, horizonte y supuestos. |
| XSYNC-138-06 | P1 | C10-D1 §§17.6 y 26 advierten que dos intervenciones que producen el mismo ΔT_acc no son automáticamente equivalentes causalmente; pueden tener vías directas distintas hacia Value. | La igualdad de accesibilidad podría usarse indebidamente para agrupar versiones de tratamiento. | Incorporar equivalencia de accesibilidad, equivalencia de vías relevantes para Value y equivalencia de versión de tratamiento como juicios separados. |
| XSYNC-138-07 | P1 | C10-D1 §§29–30 distingue trayectoria factible, conocida/considerada, seleccionada, iniciada, ejecutada, completada, no seleccionada, interrumpida o fallida. C10-S conserva solo parte de esos estados. | Pérdida de información sobre selección y ejecución; riesgo de sesgo post-tratamiento. | Ampliar diccionario y contrato de resultados para conservar estados y marcas temporales separados, sin ajustar mecánicamente por mediadores posteriores. |
| XSYNC-138-08 | P1 | C10-S §20 denomina dictamen global del experimento y C10-D1 §21 clasifica resultados científicos C10. Son decisiones de niveles diferentes. | Riesgo de confundir superación metodológica de C10-S con conclusión científica sobre C10. | Mantener C10S-01…05 como dictámenes metodológicos del experimento sintético; conservar por separado las categorías científicas de C10-D1 (contribución identificada, equivalencia/adversidad delimitada, paquete identificado sin atribución, imprecisión o no-identificación). |
| XSYNC-138-09 | P2 | C10-D1 §21.3 explicita la interpretación de intervalos respecto de δ y ε; C10-S §§21–23 define justificación, pero aún no incorpora la regla de clasificación completa como contrato de salida. | Puede haber ambigüedad al convertir estimaciones en conclusiones de relevancia/equivalencia. | Incorporar regla preespecificada para efecto relevante, equivalencia, efecto adverso e inconclusión; no usar p no significativo como equivalencia. |
| XSYNC-138-10 | P2 | C10-D1 §§27–30 precisa enumeración de trayectorias, actualización dinámica, selección y no ejecución. C10-S cubre ramas y estados principales, pero no toda la secuencia de conocimiento/consideración/inicio/interrupción. | La evaluación sintética podría validar el enumerador sin probar el proceso posterior de selección/ejecución. | Ampliar el contrato de ejecución y declarar explícitamente qué parte queda fuera del alcance de C10-S si no se modela. |

### 25.3 Distinción causal que debe regir la revisión

La arquitectura que debe conservarse es:

`B/Z` (intervención o componente implementable)
→ condiciones y respuesta estructural
→ `A=ΔT_acc` (medición independiente, estructurada)
→ Reach y trayectorias factibles
→ conocimiento/consideración y selección
→ ejecución (parcial, completa, interrumpida o ausente)
→ Outcome
→ Value.

Esta cadena no afirma mediación exclusiva. Deben mantenerse registradas las vías alternativas desde B/Z hacia Value y las condiciones que afectan simultáneamente accesibilidad, selección, ejecución y resultados.

Los estimandos siguen separados:
- TE_Z: efecto total de asignación/intervención.
- ψ_policy: efecto de la política implementable concreta (por ejemplo, autorización), incluyendo sus vías.
- θ_A(q): contraste entre políticas factibles sobre cambios de accesibilidad bajo un régimen común q, solo cuando el mapeo intervención→A y la identificación específica son defendibles.
- θ_{L,A}: efecto de un régimen conjunto de condiciones y accesibilidad, no atribución exclusiva a A.
- θ_A^dyn: marcador no disponible para estimación hasta formalización completa.

### 25.4 Estado de los hallazgos

- XSYNC-138-01: **abierto; bloquea congelación de la especificación causal C10-S y cualquier interpretación de g como política de accesibilidad**.
- XSYNC-138-02 a 138-08: **abiertos; requieren corrección documental antes de aceptación integral**.
- XSYNC-138-09 y 138-10: **abiertos; requieren incorporación o delimitación explícita del alcance**.

No se declara cerrado ningún hallazgo por esta auditoría. No se modifica C10-D1 ni se altera el contenido histórico de sus addenda. Las correcciones deberán incorporarse como nueva revisión del documento C10-S, conservando la trazabilidad de la versión anterior.

### 25.5 Decisión operativa

La consolidación C10-S puede seguir en estado de borrador para revisión, pero **no debe congelarse, implementarse ni utilizarse para ejecución confirmatoria** hasta resolver XSYNC-138-01 y los hallazgos P1 pertinentes. El siguiente trabajo es una revisión correctiva de C10-S frente a C10-D1, no una ampliación de escenarios ni un salto a código.

**Estado de la auditoría:** documental ejecutada sobre las versiones identificadas; hallazgos registrados; sin aceptación ni cierre formal.


---


---


## 26. Revisión correctiva de la arquitectura de intervención y accesibilidad — XSYNC-138-01 (sección conversacional 139)

**Objeto:** resolver documentalmente el hallazgo bloqueante XSYNC-138-01 sin alterar el estimando causal definido en C10-D1. Esta sección corrige y sustituye, en los puntos incompatibles, las formulaciones simplificadas de §§16.2–16.3 y §25.3. No borra su historial.

### 26.1. Cuatro objetos que no deben colapsarse

1. **Asignación Z:** asignación aleatoria o mecanismo de asignación observado. En un experimento puede asignar una política; no es por sí misma accesibilidad.
2. **Intervención implementable B:** acción, regla o componente que el sistema puede aplicar realmente (por ejemplo, una regla de autorización). Su versión, contenido y momento deben especificarse.
3. **Respuesta transformacional A = ΔT_acc:** cambio estructurado del espacio de transformaciones accesibles producido bajo B, medido independientemente de Outcome y Value.
4. **Ejecución:** selección, inicio y realización de transformaciones accesibles. No se deduce de A ni de Reach.

Relación causal general:
Z -> B -> C -> A = ΔT_acc -> (Reach, Π_feasible) -> conocimiento/consideración -> selección -> ejecución -> Outcome -> Value.

La cadena es una estructura de referencia, no una afirmación de mediación exclusiva. Se deben registrar vías alternativas B -> L -> Value, B -> L -> A y otras que el dominio permita.

### 26.2. Accesibilidad estructurada y componente focal

El objeto TGCV general es A = ΔT_acc = (A+, A−, ΔR, ΔC, ...), donde se conservan las transformaciones incorporadas/eliminadas y los cambios relacionales/configuracionales pertinentes según la representación y granularidad declaradas.

Para un experimento focal puede definirse A_f = h_f(ΔT_acc), donde h_f es una proyección preespecificada que identifica el cambio de accesibilidad de la transformación o familia focal τ_f. Esta proyección:
- no sustituye al objeto completo ΔT_acc;
- no convierte una variable binaria en definición universal de accesibilidad;
- conserva dirección (apertura/cierre), versión, condiciones y evidencia;
- distingue valor verdadero/estructural de su medición A_f_obs;
- no incorpora selección, ejecución, Outcome ni Value.

Si la intervención modifica otras transformaciones o relaciones, el analizador debe recibir el cambio estructurado completo. No se puede presentar el efecto de una reconfiguración amplia como efecto exclusivo de τ_f.

### 26.3. Políticas g1/g0: objeto y factibilidad

En el estimando de accesibilidad de C10-D1, g1 y g0 son políticas implementables que inducen distribuciones distintas de cambios de accesibilidad, condicionadas por contexto basal e historia pertinente. No son, por definición, políticas de autorización ni asignaciones abstractas que fuerzan A.

Mecanismo de implementación: B_g -> C_g -> A_g = ΔT_acc.
Políticas inducidas: g_j(a | X,H0), j ∈ {0,1}.
Conjunto factible: F(X,H0).

Debe cumplirse supp(g_j(. | X,H0)) ⊆ F(X,H0) para cada política y estrato de la población objetivo. La notación no autoriza a intervenir sobre una transformación imposible, a ignorar sus precondiciones ni a asignar accesibilidad sin un mecanismo realizable.

Cuando g_j solo pueda materializarse mediante una política B_gj, se documentan el mecanismo, la versión y las vías adicionales de esa política. Para interpretar el contraste como efecto atribuible a accesibilidad, las versiones deben diferir en el cambio de accesibilidad focal sin introducir diferencias no separadas en información, incentivos, expectativas, recursos, trato u otras vías hacia Value. Si esto no puede garantizarse, el contraste es un efecto de política o de paquete, no θ_A(q) aislado.

### 26.4. Régimen común q y regla de Value

El régimen q fija una distribución común y explícita de condiciones/historias pertinentes para ambos brazos del contraste. Puede incluir contexto basal, estado inicial, recursos y capacidades comunes, información basal, necesidad y condiciones constitutivas no manipuladas, siempre que su papel temporal y causal esté especificado.

La regla de Value no es una variable que q deba asignar. Se fija como parte de la definición del resultado/estimando: beneficiario, dimensión, regla evaluativa, escala, dirección y horizonte. Debe ser idéntica entre los regímenes comparados, salvo que la pregunta científica sea explícitamente el efecto de cambiar el criterio evaluativo, que no es el estimando focal C10.

Las condiciones constitutivas L_c que hacen imposible una transformación no se estandarizan para crear artificialmente soporte. Las condiciones posteriores L_m se clasifican por su posición temporal y papel causal; no se ajustan mecánicamente como covariables ordinarias.

### 26.5. Estimandos no intercambiables

**Efecto total de asignación:**
TE_Z = E[V | do(Z=1)] - E[V | do(Z=0)].

En un diseño aleatorizado, el contraste por asignación identifica el ITT de la asignación, bajo consistencia, ausencia de interferencia relevante y manejo adecuado de pérdidas. No identifica automáticamente el efecto de accesibilidad.

**Efecto de política implementable:**
ψ_policy(q) = E[V^(q,B1)] - E[V^(q,B0)].

Incluye todas las vías causales de las versiones de política comparadas. Si B es una regla de autorización, este es el efecto de esa política, no una etiqueta alternativa para θ_A(q).

**Efecto de políticas de accesibilidad:**
θ_A(q) = E[V^(q,g1)] - E[V^(q,g0)].

Compara políticas factibles que inducen cambios distintos de accesibilidad bajo un régimen común. Su interpretación como contribución atribuible a accesibilidad exige que la intervención esté bien definida y que las vías no atribuibles a ese cambio estén controladas, excluidas por diseño o separadamente identificadas. No se identifica solo porque Z esté aleatorizado ni porque A_f_obs difiera entre brazos.

**Efecto conjunto de condiciones y accesibilidad:** cuando la accesibilidad solo puede cambiar junto con condiciones constitutivas, se define un contraste conjunto sobre esas condiciones y A. Se etiqueta como efecto conjunto (por ejemplo, θ_(L,A)); no se renombra como efecto exclusivo de accesibilidad.

θ_A_dyn continúa fuera del conjunto de estimandos operativos hasta que se definan políticas dinámicas, historia, población, factibilidad, horizonte, regla Value y supuestos.

### 26.6. Papel de la autorización

La autorización es una posible condición o componente de implementación C_auth, no una medida de accesibilidad. La secuencia posible es:
B_auth -> C_auth -> A_f* -> ΔT_acc.

Si la autorización también cambia expectativas, incentivos, prioridades, información o trato, esas vías se miden y el contraste primario se interpreta como ψ_policy. No se atribuye su ITT íntegro a accesibilidad.

La modalidad sintética preferida para probar atribución es una intervención técnica aislada que altere la condición de realizabilidad focal sin cambiar las demás condiciones relevantes. La modalidad de autorización puede conservarse como escenario de efecto de política y como caso adversarial de vías múltiples.

### 26.7. Revisión requerida de S4-R

S4-R queda especificado como escenario de políticas sobre accesibilidad, no como asignación de autorización:
- q* establece una distribución común sobre condiciones no constitutivas pertinentes, condicionada en X,H0.
- Se identifica explícitamente si la variable L representa condición constitutiva L_c, condición inducida L_m o ambas; no se permite la etiqueta indiferenciada.
- g1 y g0 inducen distribuciones diferentes de A_f solo dentro del conjunto factible de cada historia.
- Los valores previos .8/.2 y q*(L=1 | X)=.5 permanecen como parámetros ilustrativos provisionales, no como política aprobada ni prueba de soporte.
- El generador debe comprobar factibilidad/positividad en cada estrato. Si una política exige una transformación imposible o tiene probabilidad positiva fuera de F(X,H0), el contraste poblacional original no es identificable/implementable. No se fuerza la asignación.
- Si la condición es constitutiva y hace g0 imposible, se informa el estrato factible o se formula un estimando conjunto distinto, preservando la diferencia.

### 26.8. Matriz de correspondencia correctiva

| Formulación anterior | Regla corregida | Efecto |
|---|---|---|
| g como política de autorización | g como política factible sobre cambios de accesibilidad; autorización es posible mecanismo B | Corrige XSYNC-138-01 |
| q_X incluye regla Value | q fija condiciones/historias; Value se fija en el estimando | Corrige XSYNC-138-02 |
| A_f* representa todo ΔT_acc | A_f = h_f(ΔT_acc), proyección focal | Corrige XSYNC-138-03 |
| S4-R asume soporte uniforme | Factibilidad por historia y separación L_c/L_m | Corrige XSYNC-138-04 |
| Efecto de autorización se interpreta como accesibilidad | ψ_policy separado de θ_A(q) | Corrige XSYNC-138-01/06 |

### 26.9. Reglas de decisión del analizador

El analizador debe emitir por separado:
1. ¿La asignación Z está definida y fue respetada?
2. ¿Qué intervención implementable B se aplicó y qué versión?
3. ¿Qué condiciones y vías produjo?
4. ¿Qué cambio estructurado ΔT_acc ocurrió y qué evidencia lo respalda?
5. ¿Qué componente focal A_f se deriva mediante h_f?
6. ¿Las políticas g1/g0 son implementables y tienen soporte en la población objetivo?
7. ¿El contraste identifica TE_Z, ψ_policy, θ_A(q), un efecto conjunto o ninguno?
8. ¿Se han confundido accesibilidad, aplicabilidad, selección, inicio, ejecución y finalización?

Debe declarar no-identificación cuando el mapeo B -> A sea ambiguo, existan vías alternativas no separadas, falte soporte, la política no sea factible o la medición no permita recuperar el constructo requerido.

### 26.10. Dictamen de XSYNC-138-01

La presente sección resuelve la contradicción documental a nivel de especificación propuesta: B/Z, A=ΔT_acc, A_f, autorización, g1/g0, q y Value quedan diferenciados y relacionados.

El hallazgo no se declara formalmente cerrado todavía. Requiere:
- revisión de consistencia con los apartados exactos de C10-D1;
- actualización de los escenarios S4-O/S4-R y del diccionario/contrato de datos;
- revisión independiente que confirme que no se ha cambiado el estimando de C10-D1;
- evidencia documental de resolución y aceptación.

**Estado:** resolución correctiva propuesta y registrada; no implementada, no simulada, no ejecutada y no aceptada. Los restantes XSYNC-138-02…10 siguen abiertos salvo cierre explícito posterior.


---

## 27. Reespecificación de S4-O y S4-R tras XSYNC-138-01 (sección conversacional 140)

**Propósito:** separar el escenario de efecto de una política implementable con vías potencialmente múltiples (S4-O) del escenario diseñado para identificar un contraste entre políticas factibles de accesibilidad bajo un régimen común (S4-R). Esta sección prevalece sobre las formulaciones anteriores de S4-O/S4-R cuando exista incompatibilidad. No declara identificabilidad empírica fuera del DGP sintético.

### 27.1. S4-O: efecto total de una política de autorización

**Pregunta:** ¿cuál es el efecto total de asignar una política de autorización, cuando esa política puede cambiar accesibilidad y también otras condiciones relevantes?

- Z_B: asignación aleatoria de la política.
- B_auth: política de autorización aplicada según asignación.
- C_auth: autorización efectiva recibida.
- A_f*: accesibilidad estructural verdadera de la transformación focal, derivada de condiciones de realizabilidad.
- A_f_obs: medición de A_f*.
- L: variable posterior inducida por la política que afecta tanto accesibilidad como Value.
- M, O, V: mecanismo, Outcome y Value.

DGP conceptual:
- L | Z_B=0 ~ Bernoulli(0.25); L | Z_B=1 ~ Bernoulli(0.75).
- A_f* se deriva de C_auth, L y las condiciones técnicas efectivas; no se asigna directamente.
- M = 1 + A_f* + 0.5X + ε_M.
- O = 2M + ε_O.
- V = 3O + 4L + ε_V.

La política puede además modificar expectativas, incentivos o prioridades. Si se incluyen, deben quedar en el DGP y en el diccionario como vías explícitas; no se absorben en A_f*.

**Estimando primario:** TE_ZB o ψ_policy para la política de autorización, según el contraste de asignación o de versiones de política que se haya definido. El contraste identifica el efecto total de la política bajo la aleatorización y supuestos pertinentes. No se etiqueta como θ_A(q).

**Objetivo analítico:** que el analizador reconozca que L es postratamiento, que Z_B aleatorizado no elimina confusión mediador–resultado y que no se puede atribuir todo el ITT a accesibilidad. El efecto estructural de A_f* conocido por el generador se mantiene oculto al analizador. La recuperación de una contribución específica de accesibilidad no es requisito de éxito en S4-O; el reconocimiento de sus límites sí lo es.

### 27.2. S4-R: contraste de políticas de accesibilidad bajo régimen común

**Pregunta:** ¿puede recuperarse el contraste entre dos políticas factibles de cambio de accesibilidad cuando las condiciones/historias pertinentes se mantienen bajo un régimen común explícito?

Se define un régimen común q* y dos políticas de accesibilidad g1/g0. El DGP debe implementarlas mediante condiciones y mecanismos realizables, no mediante asignación directa del indicador A_f*.

- L_m: condición no constitutiva cuya distribución se fija mediante el régimen común q*.
- C_c: conjunto de condiciones constitutivas de realizabilidad.
- Población objetivo primaria: unidades con C_c compatible con ambas políticas, de modo que g1 y g0 sean factibles.
- q*: intervención común y factible sobre L_m, por ejemplo P(L_m=1 | X,H0)=0.5, idéntica bajo ambas políticas.
- g1/g0: políticas que inducen probabilidades distintas de apertura de la condición técnica focal; valores .8 y .2 son ilustrativos y provisionales.
- A_f*: resultado estructural derivado de la condición técnica y de C_c; A_f_obs es su medición.

El soporte exigido es:
supp(g_j(. | X,H0,L_m)) ⊆ F(X,H0,L_m,C_c), j ∈ {0,1}.
La población primaria y el conjunto de condiciones deben permitir ambas políticas. No se extrapola a estratos constitutivos en los que una política sea imposible.

**DGP de resultado ilustrativo:**
- M = 1 + A_f* + 0.5X + ε_M.
- O = 2M + ε_O.
- V = 3O + 4L_m + ε_V.
- ε_M, ε_O y ε_V se generan con distribuciones y semillas preespecificadas.

Bajo este DGP lineal, sin interacciones y con errores de media cero, el contraste estructural esperado inducido por g1=.8 frente a g0=.2 es 6×(.8−.2)=3.6 unidades de Value, condicionado al régimen q* y a la población donde ambas políticas son factibles. Este valor es una verdad del DGP ilustrativo, no un umbral de relevancia, estimación empírica ni prueba de C10.

La contribución de L_m a Value queda estandarizada por q* y no cambia entre políticas. Si q* no puede implementarse o si L_m conserva una vía diferencial entre brazos, el contraste deja de representar el estimando previsto y se informa como no identificado o como efecto conjunto.

### 27.3. Separación entre L_m y C_c

- L_m representa condiciones que pueden ser intervenidas bajo un régimen común factible sin hacer imposible la transformación focal.
- C_c representa condiciones constitutivas que determinan si la transformación es realizable. No se fuerza su valor para crear positividad.
- Si C_c impide g0 o g1 en una parte de la población, esa parte queda fuera del estimando primario de S4-R o requiere un estimando conjunto distinto, predefinido.
- S10b mantiene el papel de control de no factibilidad constitutiva. No se resuelve aumentando N ni ajustando estadísticamente una imposibilidad estructural.

### 27.4. Implementación sintética sin asignación abstracta de accesibilidad

El generador debe ejecutar la siguiente secuencia:
1. generar X, H0 y condiciones basales;
2. determinar C_c y el conjunto factible F;
3. aplicar q* a L_m en S4-R, o asignar Z_B/B_auth en S4-O;
4. ejecutar el mecanismo implementable que altera la condición técnica focal;
5. evaluar realizabilidad y calcular A_f* desde las condiciones efectivas;
6. generar A_f_obs según el modelo de medición;
7. derivar el ΔT_acc estructurado completo, no solo el indicador focal;
8. generar Reach y trayectorias factibles;
9. registrar conocimiento/consideración, selección e inicio;
10. ejecutar o no ejecutar según las reglas del escenario;
11. generar Outcome y Value sin que Value influya retrospectivamente en A, Reach o trayectorias.

El generador conserva la verdad completa; el analizador recibe únicamente variables observables permitidas, metadatos del diseño y reglas de medición. El evaluador compara los dictámenes con el DGP protegido.

### 27.5. Contrato de variables adicional para S4-O/S4-R

| Variable | Rol | Momento | Observabilidad analizador |
|---|---|---|---|
| Z_B | Asignación de política | Basal | Sí |
| B_auth / B_g | Versión de política implementable | Intervención | Sí |
| C_auth | Autorización efectiva | Posterior | Sí, con calidad |
| L_m | Condición bajo régimen común | Según q* | Sí, con historial |
| C_c | Condición constitutiva | Basal/estado | Sí, con evidencia |
| F | Conjunto de políticas factibles | Por historia | Derivable si reglas conocidas |
| A_f* | Accesibilidad focal verdadera | Posterior a mecanismo | No directamente si hay cegamiento/medición imperfecta |
| A_f_obs | Medición de accesibilidad | Posterior | Sí |
| ΔT_acc | Cambio estructurado completo | Por estado/tiempo | Sí, con evidencia y calidad |
| M | Mecanismo | Posterior | Sí si está medido |
| Reach / Π_feasible | Alcance y trayectorias factibles | Dinámico | Reconstrucción ciega |
| Knowledge/Consideration | Conocimiento/consideración | Antes de selección | Sí si se mide |
| Selection / Initiation | Selección/inicio | Posterior | Sí |
| Execution_status | Parcial/completa/interrumpida/ausente | Posterior | Sí |
| O | Outcome | Posterior | Sí |
| V | Value y dimensiones | Según horizonte | Sí, con regla fija |

La verdad A_f* se reserva al generador/evaluador salvo en una submuestra de validación preespecificada. El analizador no recibe coeficientes estructurales ni etiquetas de escenario.

### 27.6. Estimandos y dictámenes por escenario

| Escenario | Estimando primario | Lo que puede concluirse | Lo que no debe concluirse |
|---|---|---|---|
| S4-O | TE_ZB / ψ_policy | Efecto total de política de autorización | θ_A(q) por mera aleatorización |
| S4-R | θ_A(q*) en población con soporte | Contraste de políticas factibles de accesibilidad bajo q* | Efecto universal fuera del soporte |
| S10b | Efecto conjunto o efecto en estrato factible, si se define | Límite de factibilidad constitutiva | Contrafactual imposible de la población completa |

S4-O y S4-R no son réplicas del mismo diseño ni deben agregarse como si estimaran el mismo parámetro.

### 27.7. Pruebas específicas

- S4O-01: recuperación del ITT de política cuando la asignación es aleatoria.
- S4O-02: no atribuir automáticamente el ITT a A_f*.
- S4O-03: reconocer L postratamiento y evitar ajuste mecánico que induzca sesgo.
- S4O-04: identificar vías alternativas explícitas y declarar límites de separación.
- S4R-01: verificar que q* sea común, implementable y aplicado antes/durante la política según protocolo.
- S4R-02: verificar soporte de g1/g0 por estrato e historia.
- S4R-03: comprobar que g1/g0 se implementan mediante condiciones técnicas reales.
- S4R-04: derivar A_f* desde condiciones efectivas, nunca asignarlo como etiqueta.
- S4R-05: recuperar el contraste conocido del DGP dentro de tolerancias preespecificadas.
- S4R-06: detectar no-identificación si se viola soporte o aparece una vía alternativa diferencial.
- S4R-07: conservar ΔT_acc estructurado y no solo el indicador focal.
- S4R-08: comprobar que selección/ejecución no se confunden con accesibilidad.

### 27.8. Estado y relación con XSYNC

- XSYNC-138-01: corrección aplicada en §§26–27; pendiente de revisión independiente antes de cierre formal.
- XSYNC-138-02: corrección propuesta; q y regla Value separados.
- XSYNC-138-03: corrección propuesta; A_f se declara proyección de ΔT_acc.
- XSYNC-138-04: corrección propuesta; S4-R separa L_m/C_c y exige soporte.
- XSYNC-138-06: parcialmente tratado mediante distinción de versiones de política; falta auditoría de equivalencia causal de versiones.
- XSYNC-138-07: contrato ampliado con estados de conocimiento, selección e inicio; falta comprobar exhaustividad frente a C10-D1.
- XSYNC-138-08: permanece abierto hasta separar explícitamente dictamen metodológico C10-S y conclusión científica C10.
- XSYNC-138-05, 09 y 10: permanecen abiertos salvo la delimitación parcial de alcance descrita aquí.

**Estado general:** reespecificación documental propuesta; no implementada, no simulada, no ejecutada ni aceptada. Los valores numéricos siguen siendo ilustrativos. La auditoría cruzada debe verificar que S4-R conserva el estimando de C10-D1 y que q* y las políticas tienen implementación coherente.


---

## 28. Versiones de intervención, equivalencia causal y estados longitudinales de trayectoria (sección conversacional 141)

**Base de coherencia:** C10-D1 §§17.5–17.7, 26–30. Esta sección completa las correcciones iniciadas en §§26–27. No modifica el significado del estimando de C10-D1.

### 28.1. Identidad de la intervención y versiones

Cada intervención/política B debe tener una ficha de versión que incluya:
- mecanismo/componente implementado;
- transformación, unidad o elemento del sistema afectado;
- intensidad, alcance y duración;
- momento de inicio y calendario;
- población/unidad destinataria;
- condiciones y recursos de implementación;
- información, expectativas, incentivos, trato y prioridades que puedan cambiar;
- costes, tiempos, riesgos, calidad y distribución de beneficios;
- versión del procedimiento y evidencia de cumplimiento.

La asignación Z identifica qué versión se ofrece/asigna; el registro de recepción y cumplimiento identifica qué versión se implementó efectivamente. No se colapsan asignación, recepción, intervención implementada y respuesta estructural A=ΔT_acc.

### 28.2. Tres equivalencias independientes

| Tipo | Pregunta | Consecuencia |
|---|---|---|
| Equivalencia transformacional | ¿Las versiones producen el mismo cambio estructurado ΔT_acc bajo la regla de identidad/granularidad fijada? | Compara el constructo de accesibilidad |
| Equivalencia de intervención | ¿Las versiones son iguales en mecanismo, unidad, intensidad, tiempo, recursos y condiciones de implementación relevantes? | Compara tratamientos implementados |
| Equivalencia causal respecto a Value | ¿Las versiones generan los mismos resultados potenciales de Value en la población/horizonte especificados? | Compara sus consecuencias evaluativas |

Ninguna equivalencia implica automáticamente las otras. En particular, igualdad de ΔT_acc no permite agrupar versiones si difieren en costes, demoras, calidad, riesgo, trato o distribución de beneficios. La equivalencia causal respecto a Value requiere evidencia/diseño apropiados y no se deduce de similitud descriptiva.

### 28.3. Regla de atribución cuando las versiones difieren

- Si las versiones difieren únicamente en la distribución inducida de accesibilidad y las restantes vías están controladas por diseño o identificadas separadamente, el contraste puede ser candidato a θ_A(q).
- Si difieren en accesibilidad y en otras vías no separadas, el contraste estima un efecto de política/paquete (ψ_policy) o queda parcialmente identificado.
- Si producen el mismo ΔT_acc pero difieren en costes/tiempos/calidad/riesgos, el contraste es un efecto entre versiones de intervención, no un efecto de accesibilidad.
- Si no puede establecerse qué versión se implementó, se informa contaminación/no cumplimiento y se mantiene el ITT por asignación como estimando distinto del efecto de recepción.

No se utilizará el residual TE−θ_A como efecto directo puro. Solo se informará si ambos estimandos son compatibles en población, escala y horizonte; incluso entonces puede contener vías alternativas e interacciones.

### 28.4. Interacción entre condiciones y accesibilidad

Se conserva el estimando conjunto θ_(L,A) para contrastes coordinados de condiciones y accesibilidad. Cuando el diseño haga factibles e identificables las cuatro combinaciones, puede definirse una interacción aditiva I_(A,L) como diferencia entre el efecto de accesibilidad bajo dos regímenes de condiciones:

I_(A,L) = [V(q1,g1) − V(q1,g0)] − [V(q0,g1) − V(q0,g0)].

Esta interacción:
- requiere que q0/q1 y g0/g1 estén definidos como políticas factibles;
- requiere soporte para las cuatro combinaciones en la población objetivo;
- no se interpreta como componente universal de C10;
- no se presume nula ni se usa para forzar una descomposición aditiva;
- si alguna combinación es imposible, se informa no-identificación de esa interacción o se define un estimando restringido distinto.

### 28.5. Contrato longitudinal de trayectorias

Para cada trayectoria candidata, conservar un historial de eventos y marcas temporales, no una única variable binaria de ejecución. Estados mínimos:
1. factible respaldada;
2. conocida/identificada por los agentes pertinentes;
3. considerada;
4. seleccionada;
5. inicio/intento;
6. ejecución parcial;
7. ejecución completa;
8. completada según criterio terminal;
9. no seleccionada;
10. no iniciada;
11. interrumpida/abandonada;
12. fallida.

Las categorías pueden coexistir secuencialmente: una trayectoria puede ser seleccionada, iniciada, parcialmente ejecutada y después interrumpida. Registrar quién decide, momento, información disponible, regla de selección, motivo conocido y transformaciones realizadas.

La factibilidad es propiedad del sistema bajo condiciones e historia definidas. Conocimiento/consideración/selección son propiedades del proceso de decisión de agentes. La falta de conocimiento o selección no convierte automáticamente una transformación en inaccesible. Si información o permiso son condiciones constitutivas de realizabilidad, se modelan como tales dentro de T_acc y se aporta evidencia.

### 28.6. No ajustar mecánicamente por selección o ejecución

Para θ_A(q), selección y ejecución son respuestas posteriores a las políticas g_j. Su evolución bajo cada política forma parte del resultado potencial V^(q,g_j). No condicionar por selección, inicio o ejecución observada como si fueran covariables basales para estimar el efecto total de la política.

Si se desea estudiar efectos entre quienes ejecutan, se necesita un estimando distinto y una estrategia de identificación específica; no se interpreta la comparación observada entre ejecutores como causal por defecto.

### 28.7. Extensión del diccionario y contrato de datos

Añadir por intervención:
- intervention_id, intervention_version, assignment_id, receipt_status, implementation_fidelity;
- component, target_unit, intensity, scope, start_time, duration, implementation_conditions;
- resources, information_change, incentive_change, expectation_change, priority_change, treatment_other_paths;
- costs, delay, quality, risk, benefit_distribution.

Añadir por trayectoria/evento:
- trajectory_id, event_id, event_time, agent/decision_unit;
- feasibility_status, knowledge_status, consideration_status, selection_status;
- initiation_status, execution_status, completion_status, interruption/failure_reason;
- information_at_decision, selection_rule, transformations_attempted/completed;
- T_acc_snapshot_id y evidencia temporal asociada.

Los registros deben permitir reconstruir qué era accesible, qué conocían los agentes, qué eligieron y qué ejecutaron en cada momento. No inferir estados anteriores desde Outcome o Value.

### 28.8. Pruebas de consistencia adicionales

- VER-01: dos versiones con mismo ΔT_acc y distinto coste no se declaran equivalentes causalmente.
- VER-02: dos versiones con mismo ΔT_acc y distinta demora conservan identidad de versión.
- VER-03: dos versiones con mismo ΔT_acc y distinto riesgo/calidad no se agrupan como un único tratamiento.
- VER-04: versión asignada y versión recibida se registran separadamente.
- VER-05: incumplimiento no altera el ITT por asignación.
- VER-06: el efecto de paquete no se etiqueta θ_A(q) si existen vías adicionales no separadas.
- TRJ-01: factible pero desconocida no equivale a inaccesible.
- TRJ-02: conocida pero no considerada se conserva como estado distinto.
- TRJ-03: seleccionada pero no iniciada no equivale a ejecutada.
- TRJ-04: parcial seguida de interrupción conserva ambos eventos.
- TRJ-05: finalización exige criterio terminal preespecificado.
- TRJ-06: ejecución observada no se usa para reconstruir retrospectivamente T_acc.
- TRJ-07: el estimador de efecto total no ajusta mecánicamente por selección/ejecución posteriores.
- INT-01: interacción I_(A,L) se calcula solo si las cuatro combinaciones son factibles e identificables.
- INT-02: combinación imposible produce no-identificación/restricción explícita, nunca extrapolación silenciosa.

### 28.9. Relación con hallazgos XSYNC-138

- XSYNC-138-06: respuesta documental ampliada; pendiente de auditoría de ejemplos y prueba de equivalencia de versiones.
- XSYNC-138-07: respuesta documental ampliada; pendiente de verificación de exhaustividad respecto al contrato longitudinal C10-D1.
- XSYNC-138-10: el alcance sintético ahora distingue enumeración, conocimiento/consideración, selección e historial de ejecución; queda pendiente demostrar que las pruebas cubren cada estado.
- XSYNC-138-08: sigue abierto; el dictamen metodológico C10-S y la conclusión científica C10 deben quedar en contratos separados.
- XSYNC-138-01: §§26–28 ofrecen una corrección coherente propuesta; no se cierra sin revisión independiente y aceptación.

**Estado:** contrato documental ampliado; no implementado, simulado, ejecutado ni auditado mediante pruebas. Los hallazgos siguen abiertos hasta revisión y cierre explícito.


---

## 29. Auditoría de consistencia de §§26–28 frente a C10-D1 (sección conversacional 142)

**Fuentes de contraste:** C10-D1 §§17.1–17.9, 26.1–26.3 y 27–31; especialmente la definición de políticas factibles, la distinción intervención/respuesta estructural/ejecución, la equivalencia de versiones, la notación de θ_A(q), el contrato de trayectorias y la regla de atribución.

**Alcance:** auditoría documental. No es auditoría de código, simulación, ejecución estadística ni validación empírica. No cierra por sí sola los hallazgos XSYNC.

### 29.1. Matriz de consistencia

| Elemento C10-S | Regla C10-D1 de referencia | Dictamen documental |
|---|---|---|
| §26.1: Z, B, A=ΔT_acc y ejecución | D1 §17.5 y §26.1: intervención implementable, respuesta estructural y ejecución separadas | **Conforme en concepto** |
| §26.2: A_f como proyección de ΔT_acc | D1 §§27.1 y 30.3: medir el cambio estructurado completo y documentar el componente focal sin sustituirlo | **Conforme, condicionado** a que el diccionario conserve ΔT_acc completo y la proyección h_f |
| §26.3: g1/g0 factibles | D1 §§17.2, 17.7 y 31.1: políticas estocásticas implementables, condicionadas por historia y restringidas al conjunto factible | **Conforme en definición; falta operacionalización** |
| §26.4: q y Value | D1 §§17.7 y 31.1: q es régimen común factible; la regla Value define el resultado y debe permanecer coherente entre contrastes | **Conforme** |
| §26.5: TE, ψ_policy y θ_A(q) | D1 §§17.7, 26.1–26.2 y 30: estimandos distintos, no aditivos automáticamente | **Conforme en separación; requiere precisión en S4-O** |
| §26.6: autorización como mecanismo, no accesibilidad | D1 §§17.5 y 26.1: B implementable puede inducir A y otras vías | **Conforme** |
| §27: S4-O frente a S4-R | D1 §§17.7, 26 y 30: efecto de política distinto de contraste de accesibilidad | **Conforme en propósito; S4-O tiene ambigüedad de estimando** |
| §27: q* y soporte S4-R | D1 §§17.1–17.2 y 31.1: separar condiciones constitutivas y otras condiciones; soporte factible por historia | **Conforme como objetivo; falta completar régimen y mecanismo** |
| §28.1: ficha de versiones | D1 §17.5: versiones especificadas por componente, unidad, intensidad, temporalidad, población y condiciones | **Conforme y ampliado** |
| §28.2: equivalencias | D1 §17.6: equivalencia de accesibilidad, equivalencia de vías relevantes para Value y equivalencia de versión de tratamiento | **Requiere corrección terminológica** |
| §28.3: atribución según vías | D1 §§17.6, 26.2 y 30.3 | **Conforme** |
| §28.4: interacción | D1 §§17.3, 17.7 y 26.3: cuatro combinaciones factibles e identificables; no confundir interacciones | **Conforme, condicionado** |
| §§28.5–28.7: estados longitudinales y no ajuste mecánico | D1 §§27–30: posibilidad, selección, ejecución y temporalidad separadas | **Conforme; verificar exhaustividad del diccionario** |

### 29.2. Corrección 1 — S4-O: asignación e implementación recibida

La formulación anterior «TE_ZB o ψ_policy, según el contraste» es demasiado ambigua. Se sustituye por esta regla:

- **ITT de asignación:**  
  TE_ZB = E[V | do(Z_B=1)] − E[V | do(Z_B=0)].  
  Contrasta la asignación aleatoria a las versiones/políticas ofrecidas. Se conserva aunque exista incumplimiento, recepción incompleta o contaminación, bajo los supuestos del diseño y tratamiento adecuado de pérdidas/interferencia.

- **Efecto de política implementada:**  
  ψ_policy = E[V^(B_1)] − E[V^(B_0)].  
  Contrasta los regímenes de política efectivamente definidos e implementados. No se identifica automáticamente por el ITT cuando la recepción o fidelidad difiere de la asignación.

- **Relación entre ambos:** solo coinciden bajo condiciones de consistencia y correspondencia entre asignación y versión recibida —por ejemplo, implementación completa y ausencia de versiones cruzadas relevantes— que deben declararse, no presumirse.

En S4-O, el estimando primario de recuperación del diseño aleatorizado será **TE_ZB**. ψ_policy será un estimando distinto y secundario, únicamente si el generador define recepción/fidelidad y el diseño permite identificarlo. Ninguno se etiqueta como θ_A(q).

El analizador debe informar por separado asignación, política ofrecida, recepción, fidelidad y vías alternativas. La aleatorización de Z_B no elimina la confusión entre A_f* y Value inducida por L ni convierte el ITT en atribución específica de accesibilidad.

### 29.3. Corrección 2 — Taxonomía de equivalencia alineada con C10-D1

La tabla de §28.2 debe leerse y corregirse conforme a las tres categorías exactas de D1 §17.6:

1. **Equivalencia de accesibilidad:** mismo cambio estructural ΔT_acc bajo universo, representación, regla ≡T, contexto y horizonte comunes.
2. **Equivalencia de vías relevantes para Value:** las diferencias entre políticas no introducen vías alternativas relevantes hacia Value, o esas vías quedan separadas mediante un diseño/estimando defendible.
3. **Equivalencia de versión de tratamiento:** las versiones agrupadas bajo una misma política satisfacen una definición de intervención y consistencia previamente justificada.

La expresión «equivalencia causal respecto a Value» utilizada en §28.2 no debe figurar como cuarta equivalencia ni sustituir la segunda categoría. La igualdad de resultados potenciales de Value puede ser una afirmación causal que requiera evidencia, pero no es el criterio operativo de equivalencia de vías formulado en D1.

Regla: la equivalencia de accesibilidad no implica equivalencia de vías; ninguna de las dos implica por sí sola equivalencia de versión. Si las vías relevantes no pueden separarse, informar el efecto de la política concreta o del paquete, no θ_A(q).

### 29.4. Corrección 3 — Mecanismo implementable de S4-R

S4-R no puede limitarse a asignar directamente probabilidades .8 y .2 al indicador A_f*. Debe incorporar una cadena de generación verificable:

B_g → C_g → A_f* → ΔT_acc.

Para el entorno sintético se propone, pendiente de congelación del contrato:

- B_g: asignación de una política a un **módulo técnico de activación de dependencia** focal, con versión e intensidad registradas.
- C_g: estado efectivo del módulo/dependencia técnica después de su implementación.
- A_f*: accesibilidad verdadera derivada de las condiciones técnicas, las precondiciones y C_c; no asignada por el generador como etiqueta independiente.
- g1/g0: versiones del mecanismo que inducen distribuciones distintas de C_g y, a través de él, de A_f*. Los valores .8/.2 solo pueden conservarse si se definen como probabilidades inducidas por ese mecanismo y se verifica su soporte por historia.
- q*: régimen común completo sobre X, H0 y L_m, manteniendo la misma distribución bajo ambas políticas. El valor ilustrativo P(L_m=1|X,H0)=.5 es solo una parte de q*, no su definición completa.
- C_c: condiciones constitutivas verificadas antes de aplicar g; el conjunto factible se calcula para cada unidad/historia y ambas políticas deben ser posibles en la población primaria.

El DGP sintético puede estipular que el módulo técnico solo altera la dependencia que habilita la transformación focal y no modifica información, expectativas, incentivos, recursos, trato, costes, calidad o riesgos por otras vías. Esa exclusión es una propiedad estipulada del mundo sintético y debe probarse como invariante del generador; no puede trasladarse automáticamente a un sistema real.

Si el módulo afecta otras vías, S4-R deja de ser un contraste aislado de accesibilidad y pasa a ser un efecto de paquete. Si una política asigna masa fuera del conjunto factible, el escenario debe producir un dictamen de no factibilidad/no identificación, no forzar A_f*.

### 29.5. Auditoría de temporalidad y trayectoria

La comparación confirma que §§28.5–28.7 preservan la distinción de D1 §§27–30 entre:
- factibilidad estructural;
- conocimiento/consideración por agentes;
- selección;
- inicio/intento;
- ejecución parcial o completa;
- interrupción/fallo;
- Outcome y Value.

Se añade una cautela: el estado de accesibilidad debe llevar un T_acc_snapshot_id y tiempo de validez. Cada decisión/ejecución debe enlazarse con el snapshot vigente en ese momento. Una ejecución puede modificar estado, condiciones y accesibilidad futura; por ello, el historial debe permitir reconstruir la secuencia sin atribuir retrospectivamente al estado inicial posibilidades que solo aparecieron después.

No se ajustará por selección/ejecución observadas para estimar el efecto total de las políticas de accesibilidad. Si se interviene sobre ellas, se define un estimando distinto, tal como exige D1 §§29–30.

### 29.6. Dictamen de auditoría

**Conforme documentalmente, sin cierre formal:**
- separación Z/B/A/ejecución;
- A_f como proyección, sin sustituir ΔT_acc;
- distinción q frente a regla Value;
- factibilidad como restricción de g1/g0;
- versiones de intervención y vías alternativas;
- separación de trayectorias factibles y realizadas;
- tratamiento de selección/ejecución como variables posteriores;
- prohibición de descomposición automática TE−θ_A.

**Correcciones necesarias incorporadas en esta sección:**
- S4-O separa ITT de asignación y efecto de política implementada;
- equivalencias se alinean con las tres categorías de C10-D1;
- S4-R requiere un mecanismo técnico implementable que genere accesibilidad, no asignación directa de A_f*;
- se refuerza la vinculación temporal entre T_acc snapshots y eventos de trayectoria.

**Pendiente antes de cerrar XSYNC-138-01 y los hallazgos relacionados:**
1. convertir la propuesta del módulo técnico S4-R en contrato de datos y reglas del generador;
2. comprobar que q* y g1/g0 son factibles en cada estrato de la población primaria;
3. revisar el DAG de S4-O y S4-R con sus variables temporales y vías alternativas;
4. verificar que el diccionario implementa todos los estados y snapshots;
5. realizar revisión independiente de consistencia con C10-D1;
6. ejecutar, cuando exista autorización y código, las pruebas correspondientes; la auditoría documental no sustituye esos resultados.

**Estado:** auditoría documental realizada; correcciones propuestas y registradas. No implementado, no simulado, no ejecutado, no aceptado y no cerrado formalmente. No modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres previos. No autoriza implementación ni ejecución científica.


---

## 30. Contrato operativo propuesto del mecanismo técnico S4-R (sección conversacional 143)

**Objetivo:** convertir la propuesta de §29.4 en un mecanismo sintético explícito, implementable en principio y auditable, que genere cambios de accesibilidad a través de condiciones técnicas reales. La especificación no autoriza programación ni ejecución. Los parámetros son valores de diseño provisionales, no resultados.

### 30.1. Transformación focal y condición técnica

Se conserva el catálogo sintético:
- τ1: diagnosticar incidencia;
- τ2: reconfigurar técnicamente el sistema (**transformación focal**);
- τ3: verificar técnicamente la reconfiguración;
- τ4: escalar/transferir responsabilidad.

La condición técnica focal será C_dep: disponibilidad efectiva de un componente de dependencia software que habilita la operación de reconfiguración sobre el objeto de sistema designado.

C_dep=1 significa que el componente está instalado, íntegro, compatible con la versión del sistema y operativo en el momento relevante. No significa que τ2 ya se haya ejecutado, que haya sido seleccionada ni que su resultado sea exitoso.

La accesibilidad estructural de τ2 se deriva de:
A_f* = I(C_dep=1 ∧ C_auth_base=1 ∧ C_resource=1 ∧ C_capacity=1 ∧ C_info=1 ∧ C_domain=1 ∧ C_other=1),
donde cada condición distinta de C_dep permanece constante y satisfecha en la población primaria S4-R. La expresión es una regla de este juguete sintético, no una definición universal de T_acc.

Si una de las condiciones restantes no se satisface, A_f*=0 o indeterminado según la evidencia; el generador no debe corregirla ni forzarla. La transformación τ2 solo será applicable después de τ1 y de cumplirse sus precondiciones de estado. Accesible no equivale a aplicable.

### 30.2. Política implementable y mecanismo de generación

Se definen dos versiones de política técnica:
- B_g0: procedimiento de provisión del componente con probabilidad objetivo de instalación operativa p0=0.20;
- B_g1: mismo procedimiento y recursos, con probabilidad objetivo p1=0.80.

Para cada unidad, el sistema de provisión genera un intento técnico W_g ~ Bernoulli(p_g). Si W_g=1, instala/activa el componente según protocolo; si W_g=0, conserva la configuración base. El estado resultante se verifica mediante una prueba técnica independiente y ciega al Outcome/Value, que produce C_dep.

La secuencia es:
Z_g → B_g → W_g → C_dep → A_f* → ΔT_acc.

- Z_g asigna aleatoriamente la versión de política; es el instrumento de asignación del experimento sintético.
- B_g especifica el procedimiento de provisión; no es idéntico a su recepción.
- W_g es el resultado aleatorio del intento de provisión.
- C_dep es el estado técnico verificado, no el resultado de una encuesta o intención.
- A_f* se calcula a partir de todas las condiciones reales de τ2.
- A_f_obs es la medición que recibe el analizador; puede coincidir con A_f* en el escenario de medición perfecta o tener error en S6-N/S6-V.

Las probabilidades .20/.80 son parámetros del generador. Antes de congelar S4-R se debe comprobar que la política las induce efectivamente y que el mecanismo de verificación no introduce clasificación diferencial.

### 30.3. Qué se mantiene constante

En S4-R primario, B_g0 y B_g1 deben ser idénticos salvo por la probabilidad de provisión técnica del componente focal. Se fijan y registran:
- hardware, capacidad de cómputo y disponibilidad del sistema;
- recursos humanos y materiales;
- información de diagnóstico y conocimiento de agentes;
- interfaz, mensajes, formación, expectativas e incentivos;
- prioridades, reglas de selección y tratamiento;
- autorización basal distinta de C_dep;
- costes de operación y mantenimiento, latencia y tiempos no inherentes al cambio focal;
- calidad, seguridad, riesgo y distribución de beneficios no afectados por el componente;
- horizonte, catálogo, reglas de identidad, condiciones de τ1/τ3/τ4 y criterio de Value.

La instalación de C_dep no debe añadir personal, presupuesto, información, prioridad, formación o trato. Si el componente introduce costes, latencia, seguridad u otra consecuencia que varía entre brazos y afecta Value, se registra como vía adicional; el contraste deja de ser un efecto aislado de accesibilidad y se etiqueta como efecto de paquete, salvo diseño factorial que separe esa vía.

No se debe afirmar que estos invariantes se cumplen en un sistema real: son restricciones deliberadas del DGP sintético y deben verificarse en el generador.

### 30.4. Régimen común q* y población objetivo

Para el S4-R primario:
- X y H0 se generan antes de la asignación.
- L_m se fija bajo una distribución común q* idéntica en ambos brazos; para el escenario ilustrativo puede usarse P(L_m=1|X,H0)=0.5.
- C_c contiene condiciones constitutivas de τ2. La población primaria se restringe, antes de asignar Z_g, a unidades en las que ambas políticas B_g0/B_g1 son implementables y las restantes precondiciones basales están satisfechas.
- La pertenencia a la población primaria no puede depender de resultados posteriores, C_dep, A_f*, selección, ejecución, Outcome o Value.
- Se registra el soporte de ambas políticas por estrato de X,H0,L_m y C_c.

q* es la distribución común completa de condiciones/historias declaradas, no solo la distribución marginal de L_m. Si la asignación de q* no puede mantenerse común o el soporte de alguna política falla, el escenario debe emitir no-identificación para el contraste poblacional propuesto.

### 30.5. Estimando y verdad del DGP

El estimando sintético primario es el contraste entre las dos políticas factibles de accesibilidad:
θ_A(q*) = E[V^(q*,g1)] − E[V^(q*,g0)].

Con p1=.80, p0=.20, condiciones restantes satisfechas y medición estructural perfecta:
E[A_f*|g1]−E[A_f*|g0]=.60.

Si el DGP mantiene:
- M = 1 + A_f* + 0.5X + ε_M;
- O = 2M + ε_O;
- V = 3O + 4L_m + ε_V;
- errores de media cero, misma distribución bajo ambas políticas y sin interacciones ni vías directas de B_g/C_dep hacia M, O o V;

entonces el efecto medio inducido en Value es θ_A(q*) = 6 × .60 = 3.6.

Esta igualdad es verdad analítica del DGP propuesto, condicionada a todos los supuestos listados. No es un valor empírico, umbral de relevancia ni evidencia a favor de TGCV. El generador debe conservar el valor verdadero y el analizador no debe recibirlo.

### 30.6. Medición, snapshots y temporalidad

Por unidad se registran:
- assignment_id, Z_g, B_g_version, W_g, installation_status;
- C_dep_status, verification_time, verification_evidence, measurement_quality;
- C_c y condiciones restantes con estado, fuente, instante de validez;
- A_f* solo en el generador/evaluador y A_f_obs para el analizador;
- T_acc_snapshot_id, valid_from, valid_to, U_acc, R_acc, C_acc, ΔT_acc;
- estado de τ1–τ4, Reach_H, trayectorias candidatas y sus dependencias;
- conocimiento/consideración, selección, inicio, ejecución parcial/completa, interrupción/fallo;
- Outcome, dimensiones de Value, regla y horizonte.

El snapshot de accesibilidad se crea después de verificar C_dep y las restantes condiciones, y antes de selección/ejecución. Si una transformación ejecutada altera condiciones o el estado del sistema, se crea un snapshot posterior; nunca se reescribe el snapshot basal. Los eventos se enlazan al snapshot vigente al momento del evento.

### 30.7. Controles negativos y escenarios de falsación interna

Añadir variantes sintéticas:
- S4R-NC1: el módulo se asigna/provisiona, pero C_dep no cambia; ΔT_acc no cambia. El analizador no debe atribuir efecto a accesibilidad.
- S4R-NC2: C_dep y A_f* cambian, pero el coeficiente causal A_f*→M es cero; accesibilidad cambia sin cambio de Value por esa vía.
- S4R-NC3: C_dep/A_f* no cambian, pero una vía alternativa directa B_g→V se activa deliberadamente; el analizador debe identificar efecto de paquete/vía alternativa, no θ_A.
- S4R-NC4: política asignada tiene soporte insuficiente en un estrato constitutivo; no se extrapola el efecto a toda la población.
- S4R-NC5: medición A_f_obs diferencial entre brazos; el analizador debe detectar amenaza de medición y no equiparar A_f_obs con A_f*.

Estas variantes no se agregan a la matriz principal hasta reconciliar su numeración con S0–S10 y C131. Se consideran extensiones de estrés propuestas.

### 30.8. Invariantes y pruebas de aceptación para el generador futuro

- S4R-GEN-01: A_f* se deriva de C_dep y condiciones; nunca se asigna directamente.
- S4R-GEN-02: B_g0/B_g1 difieren únicamente en p_g dentro del escenario aislado.
- S4R-GEN-03: C_dep refleja instalación operativa verificada, no solo intento W_g.
- S4R-GEN-04: las condiciones restantes y q* tienen la misma distribución por brazo.
- S4R-GEN-05: no existen rutas directas B_g/C_dep→Value en el escenario aislado.
- S4R-GEN-06: los costes, tiempos, riesgos y calidad no focales son invariantes.
- S4R-GEN-07: la población objetivo se define antes de Z_g y ambas políticas son factibles en ella.
- S4R-GEN-08: las probabilidades inducidas de A_f* se recuperan dentro de tolerancias que se preespecificarán.
- S4R-GEN-09: el snapshot T_acc precede a selección/ejecución y conserva su historial.
- S4R-GEN-10: el generador/evaluador conoce la verdad; el analizador no recibe A_f* ni coeficientes.
- S4R-GEN-11: los controles negativos producen los dictámenes previstos.
- S4R-GEN-12: semilla, versiones, reglas y resultados permiten reproducibilidad.

No se fijan tolerancias estadísticas ni tamaño muestral definitivo en esta sección; requieren justificación y preespecificación posterior.

### 30.9. Límites de interpretación

Aunque S4-R recupere θ_A(q*) en este mundo sintético:
- solo demuestra que el diseño, la medición y el analizador pueden recuperar una verdad conocida bajo supuestos programados;
- no demuestra que un módulo técnico real carezca de vías alternativas;
- no demuestra que la representación de T_acc sea exhaustiva en sistemas reales;
- no demuestra generalización a otros dominios, poblaciones, horizontes o reglas de Value;
- no valida por sí solo C10 ni cierra XSYNC-138.

**Estado:** contrato operativo sintético propuesto; no congelado, implementado, simulado, ejecutado, auditado mediante pruebas ni aceptado. S4-R permanece en diseño. XSYNC-138-01 y hallazgos relacionados permanecen abiertos hasta revisión independiente, comprobación de factibilidad y pruebas autorizadas. No se modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres previos.


---

## 31. Auditoría adversarial del mecanismo técnico S4-R (sección conversacional 144)

**Objetivo:** evaluar si la dependencia técnica C_dep puede considerarse una manipulación aislada de realizabilidad de τ2 o si introduce vías adicionales hacia Outcome/Value. Revisar además la coherencia del mecanismo probabilístico, la definición de accesibilidad y la separación entre acceso, aplicabilidad y ejecución.

**Alcance:** auditoría conceptual/documental adversarial del contrato de §30. No es revisión independiente, auditoría de código, simulación, ejecución estadística ni validación empírica. No cierra XSYNC-138-01 ni autoriza implementación o ejecución.

### 31.1. Hallazgo principal: C_dep no implica exclusión causal

La definición actual de C_dep como componente software instalado, íntegro, compatible y operativo permite describir una condición técnica de realizabilidad, pero no demuestra que el componente solo afecte a la accesibilidad de τ2.

Una dependencia software real puede modificar:
- costes de instalación, licencia, mantenimiento o consumo de recursos;
- tiempos, latencia, disponibilidad y recuperación;
- calidad, estabilidad, compatibilidad y tasa de errores;
- seguridad, vulnerabilidades, fallos y exposición operacional;
- información, diagnósticos, alertas y visibilidad para los agentes;
- expectativas, confianza, conocimiento, prioridades y decisiones de selección;
- otras transformaciones, al habilitar o bloquear operaciones distintas de τ2.

Si alguna de estas consecuencias varía entre políticas y afecta a Value, existe una vía adicional. El contraste no identifica exclusivamente la contribución de accesibilidad.

### 31.2. Tres variantes que deben distinguirse

| Variante | Cambio inducido | Interpretación admisible |
|---|---|---|
| A. Apertura técnica aislada | Solo cambia la realizabilidad de τ2 | Candidata a identificar θ_A(q*) bajo los restantes supuestos |
| B. Apertura más efectos secundarios | Cambia τ2 y también costes, tiempos, calidad, riesgos, información u otras variables | Efecto de política/paquete; no atribución exclusiva a accesibilidad sin diseño adicional |
| C. Intento sin apertura efectiva | Se intenta instalar/activar, pero C_dep no cambia o las condiciones de τ2 siguen incumplidas | No hay primera etapa transformacional para esa unidad; no atribuir efecto a ΔT_acc |

La variante A es una estipulación posible en un mundo sintético controlado. No es una propiedad que pueda presumirse de una instalación software real.

### 31.3. Descomposición de la condición técnica

La definición binaria de C_dep oculta posibles causas de fallo. Se propone registrar por separado:
- C_install: instalación presente;
- C_integrity: integridad verificada;
- C_compat: compatibilidad con la versión y el objeto de sistema objetivo;
- C_oper: funcionamiento operativo comprobado.

La condición compuesta se deriva como:

C_dep = C_install ∧ C_integrity ∧ C_compat ∧ C_oper.

Cada componente debe conservar estado epistémico, fuente de evidencia, instante de verificación y validez temporal. Un estado desconocido no se convierte automáticamente en falso ni en verdadero.

Esta descomposición no altera la regla focal de accesibilidad: A_f* se deriva de C_dep y de las demás condiciones necesarias de τ2. Tampoco convierte C_dep en una medida universal de accesibilidad.

### 31.4. Corrección de la cadena probabilística

La especificación de §30.2 denomina W_g al intento técnico, pero asocia p_g a la probabilidad de instalación operativa. Si existen fallos, intento y éxito no son equivalentes.

Se propone separar:
- W_attempt: intento de instalación/activación;
- S_install: éxito técnico del procedimiento;
- C_dep: estado final verificado de la dependencia;
- C_dep,0: estado basal previo a la intervención.

Cadena:

Z_g → B_g → W_attempt → S_install → C_dep → A_f* → ΔT_acc.

Los parámetros p0=.20 y p1=.80 deben representar las probabilidades finales inducidas y verificadas:

P(C_dep=1 | g0)=.20;
P(C_dep=1 | g1)=.80,

en la población primaria definida, no meramente la probabilidad de iniciar un intento. Si la tasa de fallo de instalación es distinta de cero, el generador debe parametrizar el mecanismo para que las probabilidades finales correspondan a esos valores, o recalcular la verdad analítica de θ_A(q*).

La población primaria debe especificar el estado basal C_dep,0. Si C_dep,0=0 para todas las unidades, el contraste representa una apertura desde ausencia basal. Si no, debe modelarse la dependencia ya presente y evitar atribuir una nueva apertura a las unidades que ya tenían τ2 accesible.

### 31.5. Separación entre acceso y calidad de ejecución

La existencia de C_dep puede habilitar τ2, pero una implementación concreta también podría modificar la forma en que τ2 se ejecuta: velocidad, precisión, fiabilidad, seguridad o probabilidad de éxito.

Para preservar el escenario aislado:
- C_dep modifica únicamente la realizabilidad estructural de τ2;
- la regla de ejecución y la calidad condicional de τ2 son idénticas entre brazos;
- los recursos, tiempos no inherentes a la apertura, información, incentivos y riesgos no focales permanecen invariantes;
- el generador no permite que C_dep modifique directamente M, O o V fuera de la vía de accesibilidad y sus transformaciones posteriores.

Si el componente modifica la calidad o las consecuencias de τ2, se trata de una versión de intervención distinta o de una vía adicional. No debe interpretarse el contraste como θ_A(q*) aislado.

### 31.6. Arquitectura recomendada: escenario aislado y escenario adversarial

Se recomienda separar dos DGP:

**S4-R aislado — escenario principal de identificación sintética**
- C_dep se representa como una capacidad técnica controlada en un entorno sandbox.
- La capacidad solo cambia la realizabilidad de τ2.
- No modifica recursos, información, expectativas, incentivos, costes, latencia, calidad, seguridad ni condiciones de ejecución.
- La regla y calidad condicional de ejecución de τ2 son comunes entre brazos.
- La asignación aleatoria modifica la probabilidad de activar la capacidad; A_f* se deriva de condiciones verificadas.
- La exclusión de vías alternativas es una estipulación explícita del mundo sintético y un invariante que deberá comprobarse en el generador.

**S4-R ampliado — escenario adversarial de efectos colaterales**
- Se introduce deliberadamente una o varias consecuencias adicionales de la dependencia: coste, demora, riesgo, información, calidad o cambio de decisiones.
- El analizador debe reconocer el efecto de política/paquete y no atribuir el ITT completo a accesibilidad.
- Solo podrá recuperar θ_A(q*) si el diseño separa e identifica las vías adicionales bajo supuestos explícitos.
- Si no se pueden separar, el dictamen correcto será efecto de paquete o no-identificación.

Los dos escenarios no se fusionan en un único DGP ni se presentan como réplicas del mismo estimando.

### 31.7. Pruebas adversariales propuestas

| ID | Perturbación | Dictamen exigido |
|---|---|---|
| ADV-01 | Coste de instalación diferencial | No atribuir el efecto completo a accesibilidad |
| ADV-02 | Latencia o demora diferencial | Detectar vía alternativa |
| ADV-03 | Cambio de calidad o seguridad | Distinguir accesibilidad de calidad de ejecución |
| ADV-04 | Cambio de información o conocimiento | No confundir accesibilidad con consideración/selección |
| ADV-05 | Cambio de expectativas o incentivos | Identificar efecto de política o paquete |
| ADV-06 | Fallo de instalación | Usar C_dep verificado, no el intento |
| ADV-07 | Dependencia ya presente en el estado basal | No atribuir una apertura que no ocurrió |
| ADV-08 | Componente instalado pero incompatible | No clasificar τ2 como accesible |
| ADV-09 | Dependencia operativa, pero τ2 no aplicable tras τ1 | Mantener separadas accesibilidad y aplicabilidad |
| ADV-10 | Mismo ΔT_acc, distinta calidad de ejecución de τ2 | No atribuir la diferencia de Value a accesibilidad |

Estas pruebas se proponen como extensión adversarial de S4-R. No se incorporan todavía como escenarios ejecutables ni se agregan a la matriz principal S0–S10/C131 hasta reconciliar numeración, diccionario y cobertura.

### 31.8. Consecuencias para el estimando y la interpretación

La aleatorización de Z_g identifica el efecto por asignación a las políticas ofrecidas, bajo los supuestos del diseño. No basta por sí sola para identificar el efecto de accesibilidad.

El contraste θ_A(q*) requiere:
- políticas implementables y factibles por historia;
- cambio estructural de accesibilidad derivado de condiciones verificadas;
- equivalencia de versiones en los aspectos no focales relevantes;
- ausencia de vías alternativas diferenciales o identificación separada de estas;
- medición independiente de ΔT_acc;
- régimen q* común y soporte suficiente;
- regla Value, población y horizonte coherentes.

Si B_g/C_dep modifica otras vías hacia Value, el estimando identificado por la asignación será el efecto de política/paquete. No se renombra como θ_A(q*) ni se descompone por residuo sin un diseño identificador.

### 31.9. Dictamen adversarial

**Hallazgos conceptuales:**
1. El mecanismo de §30 es coherente como mundo sintético aislado solo si la exclusión de vías alternativas se estipula y se verifica como invariante del DGP.
2. La interpretación de p0/p1 necesita distinguir intento, éxito y estado técnico final, además de declarar el estado basal de C_dep.
3. La condición C_dep debe conservar sus componentes y evidencia, evitando ocultar incompatibilidad o fallo bajo una etiqueta binaria.
4. La calidad de ejecución de τ2 debe mantenerse constante en S4-R aislado; si cambia, aparece una vía adicional o una versión de intervención distinta.
5. S4-R ampliado debe funcionar como prueba de detección de efectos de paquete, no como estimación del mismo θ_A(q*) bajo supuestos violados.

**Decisión recomendada:** mantener S4-R aislado como escenario sintético principal, reformulando C_dep como capacidad técnica sandbox verificable; conservar S4-R ampliado como escenario adversarial separado. No congelar todavía el contrato de S4-R hasta incorporar estas precisiones y someterlas a revisión independiente.

**Pendientes:** formalizar el estado basal C_dep,0; precisar el mecanismo de intento/éxito/provisión; completar el diccionario; definir las invariantes de exclusión; reconciliar ADV-01…10 con las matrices de escenarios y pruebas; verificar q* y soporte por historia; revisión independiente frente a C10-D1.

**Estado:** auditoría adversarial conceptual/documental propuesta y registrada; no implementada, no simulada, no ejecutada, no auditada mediante pruebas, no aceptada y no congelada. XSYNC-138-01 permanece abierto. No modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres previos. No autoriza implementación ni ejecución científica.


---

## 32. Auditoría cruzada del contrato S4-R frente a C10-D1 (sección conversacional 145)

**Fuentes contrastadas:**
- C10-S, `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, rama `research/c10-s-consolidation-draft`, versión consultada antes de esta adición.
- C10-D1, `C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`, rama `research/c10-d1-protocol-draft`, blob SHA `bf25f6ec8965166e5fa52ff18e6d07613bad0eb3`.

**Naturaleza:** auditoría cruzada documental interna de consistencia entre contratos. No es revisión independiente por especialistas externos, auditoría de código, simulación, ejecución estadística ni validación empírica. La autoría compartida de las propuestas no sustituye la independencia requerida por el gate de aceptación de C10-S.

**Alcance:** §§26–31 de C10-S, con atención a S4-R, contrastadas con C10-D1 §§17.5–17.9, 19–21 y 24–32. No modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres previos.

### 32.1. Matriz de hallazgos

| ID | Severidad provisional | Hallazgo | Consecuencia | Resolución requerida |
|---|---|---|---|---|
| C145-01 | P0 | S4-R usa A_f* como accesibilidad de τ2 focal, mientras C10-D1 define A=ΔT_acc como cambio estructurado completo. | Riesgo de sustituir el constructo completo por un indicador focal y cambiar silenciosamente el estimando. | Mantener ΔT_acc completo y declarar A_f* como proyección focal. Nombrar el estimando focal θ_Af(q*) hasta justificar su relación con θ_A(q). |
| C145-02 | P0 | Las políticas g de S4-R se implementan mediante políticas de provisión B_g que inducen C_dep y A_f*. | El efecto de B_g no es automáticamente un efecto de accesibilidad; puede incluir vías alternativas. | Especificar el mapeo g^B→C_dep→A_f*→ΔT_acc y la exclusión de otras vías en el DGP aislado. Si la exclusión falla, informar efecto de política/paquete o no-identificación. |
| C145-03 | P1 | No está definido C_dep,0 ni la accesibilidad focal basal. | No se distingue apertura nueva de persistencia de accesibilidad previa. | Incorporar C_dep,0, A_f,0*, A_f,1* y ΔA_f; declarar la población basal elegible antes de asignación. |
| C145-04 | P1 | Intento, éxito de instalación, estado operativo y verificación no quedan plenamente separados. | p0/p1 pueden representar intentos y no la primera etapa transformacional efectiva. | Distinguir W_attempt, S_install y C_dep,1 verificado; p0/p1 deben corresponder al estado final inducido o recalibrarse. |
| C145-05 | P1 | La equivalencia de versiones y la calidad condicional de τ2 necesitan regla explícita. | Igual ΔT_acc podría ocultar diferencias de ejecución con consecuencias propias para Value. | Mantener constante la calidad de ejecución en S4-R aislado; si cambia, tratarlo como vía adicional/versión distinta. |
| C145-06 | P1 | q* y el soporte se expresan de forma resumida. | Una probabilidad marginal común no demuestra soporte por historia ni factibilidad conjunta. | Especificar q* completo, separar C_c de L_m y comprobar factibilidad de ambas políticas en cada historia objetivo. |

La severidad es una clasificación provisional de auditoría interna; no constituye un registro externo ni una aceptación de riesgos.

### 32.2. Hallazgo C145-01 — accesibilidad focal frente a ΔT_acc completo

C10-D1 define A como el cambio estructurado del espacio de transformaciones accesibles, operacionalizado como ΔT_acc. S4-R manipula la accesibilidad de una transformación focal τ2 mediante A_f*.

Se establecen dos niveles distintos:
- **ΔT_acc:** cambio completo, conservando altas, bajas y modificaciones de identidades, relaciones y configuraciones transformacionales según la representación y equivalencia fijadas.
- **A_f*:** proyección focal que indica si τ2 pasa a ser realizable bajo las condiciones pertinentes.

La relación que debe preservarse es:

ΔT_acc → A_f* → Reach/trayectorias → ejecución → Outcome → Value.

A_f* no sustituye ΔT_acc ni demuestra el efecto de cualquier cambio del espacio transformacional. Hasta justificar la relación entre el estimando focal y el estimando general, el contraste de S4-R se denominará provisionalmente:

θ_Af(q*) = E[V^(q*,g1^B)] − E[V^(q*,g0^B)].

Esta notación expresa el contraste inducido por dos políticas de provisión focal bajo q*, sujeto a las condiciones de identificación de §32.3. No se identificará automáticamente con θ_A(q) de C10-D1. La etiqueta provisional no altera el estimando general ni establece una nueva definición del Core.

### 32.3. Hallazgo C145-02 — correspondencia entre políticas de provisión y accesibilidad

C10-D1 exige que g1/g0 sean políticas factibles que inducen cambios de accesibilidad mediante componentes/intervenciones implementables. En S4-R, las políticas se materializan mediante provisión técnica B_g.

La correspondencia debe expresarse como:

g0^B, g1^B → B_g → mecanismo de instalación → C_dep → A_f* → ΔT_acc.

g^B no asigna A_f* directamente; es una política implementable que modifica la probabilidad de obtener la condición técnica focal y, a través de ella, la accesibilidad.

Para interpretar θ_Af(q*) como contribución específica de accesibilidad en el DGP aislado se requiere estipular y comprobar:
1. las políticas difieren solo en la provisión de la capacidad focal;
2. la diferencia afecta Value únicamente mediante el cambio de accesibilidad y sus consecuencias transformacionales posteriores;
3. no existen vías directas o alternativas desde B_g/C_dep hacia Value;
4. las versiones de intervención son equivalentes en los aspectos no focales relevantes;
5. las políticas son factibles y tienen soporte en la población/historias objetivo.

La exclusión de vías alternativas es una propiedad estipulada del mundo sintético, no una conclusión empírica. El generador podrá comprobar que respeta la estipulación; ello no demuestra que una instalación real carezca de efectos colaterales.

Si la exclusión falla, el efecto por asignación identifica el efecto de la política de provisión o del paquete bajo los supuestos del diseño, no θ_A ni θ_Af específico. Si las vías no pueden separarse, informar efecto de paquete o no-identificación.

### 32.4. Hallazgo C145-03 — estado basal y primera etapa transformacional

La especificación debe distinguir:
- C_dep,0: estado técnico basal;
- W_attempt: intento de instalación/activación;
- S_install: éxito del procedimiento de instalación;
- C_dep,1: estado final verificado;
- A_f,0* y A_f,1*: accesibilidad focal antes y después.

El cambio focal se registra como ΔA_f=A_f,1*−A_f,0*. No basta con C_dep,1=1 para afirmar una nueva apertura: debe comprobarse que τ2 no era ya accesible en el estado basal, o documentar que la política no produjo una apertura para esa unidad.

La población primaria y sus criterios de elegibilidad deben definirse antes de Z_g. No se excluirán retrospectivamente unidades en función de C_dep,1, A_f, selección, ejecución, Outcome o Value. Si el estado basal no permite una comparación coherente, restringir la población antes de asignar o redefinir el estimando.

### 32.5. Hallazgo C145-04 — probabilidades de provisión y estado final

La cadena probabilística debe separar intento, éxito y estado técnico verificado:

Z_g → B_g → W_attempt → S_install → C_dep,1 → A_f,1* → ΔT_acc.

Los valores p0=.20 y p1=.80 solo pueden interpretarse como probabilidades finales de accesibilidad focal si:
- las condiciones restantes necesarias están satisfechas;
- el estado basal es explícito;
- el procedimiento de verificación es independiente y no diferencial;
- la instalación y compatibilidad se comprueban;
- la probabilidad se refiere a la población e historias objetivo.

Si p0/p1 son probabilidades de intento o de éxito de instalación, no equivalen automáticamente a P(A_f,1*=1|g). La verdad analítica de θ_Af(q*) deberá derivarse del DGP completo, incluyendo accesibilidad basal, fallos, condiciones restantes y régimen q*.

### 32.6. Hallazgo C145-05 — equivalencia de versiones y calidad de ejecución

Se conservan las tres categorías de C10-D1 §17.6:
1. equivalencia de accesibilidad;
2. equivalencia de vías relevantes para Value;
3. equivalencia de versión de tratamiento.

Igualdad de ΔT_acc no implica equivalencia de vías ni de versión. En S4-R aislado, la regla y calidad condicional de ejecución de τ2 deben ser idénticas entre brazos; C_dep modifica únicamente su realizabilidad. Si la dependencia cambia velocidad, precisión, seguridad, fiabilidad, costes o calidad, existe una vía adicional o una versión de intervención distinta. No atribuir esa diferencia exclusivamente a accesibilidad.

Accesibilidad, aplicabilidad, conocimiento/consideración, selección, inicio, ejecución parcial/completa, interrupción y finalización siguen siendo estados distintos y fechados. No ajustar mecánicamente por selección o ejecución posteriores al régimen cuando se pretende el efecto total de la política.

### 32.7. Hallazgo C145-06 — q*, condiciones constitutivas y soporte

q* no se reduce a una probabilidad marginal ilustrativa P(L_m=1)=.5. Debe definirse como régimen conjunto, explícito y factible sobre condiciones/historias no constitutivas pertinentes, condicionado por X y por la historia previa cuando corresponda.

- C_c conserva configuraciones compatibles con τ2; no se fija independientemente en valores que hagan imposible la transformación.
- L_m se clasifica por papel causal y temporal; solo se incluye en q* aquello que el diseño puede intervenir o estandarizar coherentemente.
- Ambas políticas deben ser factibles en cada historia de la población objetivo.
- La población objetivo se define antes de la asignación.
- Se documenta el soporte de ambas políticas por estrato/historia.
- Si alguna historia carece de soporte, no se extrapola: se restringe ex ante la población o se informa no-identificación del contraste propuesto.

La compatibilidad de q* con C10-D1 es conceptual; la factibilidad por historia aún no está demostrada por implementación ni por datos.

### 32.8. Correspondencia resumida con C10-D1

| Requisito C10-D1 | Contrato S4-R | Dictamen |
|---|---|---|
| B implementable induce A=ΔT_acc (§§17.5, 31–32) | B_g induce C_dep y A_f* | Coherente como diseño focal, pero debe distinguir θ_Af de θ_A general |
| g factibles y condicionadas por historia (§§17.7, 31.1) | g^B de provisión con p0/p1 | Mapeo y soporte incompletos |
| Separar vías alternativas (§§30.3, 32.1) | Exclusión estipulada en S4-R aislado; adversarial en S4-R ampliado | Condicional; no transferible a sistemas reales |
| Condiciones constitutivas compatibles (§§17.2, 25.2, 31.1) | C_c y q* | Definición conceptual conforme; falta contrato por historia |
| Medición independiente de T_acc (§§18–19, 27) | A_f* ciega y snapshots | Parcial; debe preservar ΔT_acc completo y estado basal |
| Versiones de intervención (§17.6, §28) | B_g0/B_g1 | Pendiente de demostrar equivalencia no focal |
| Selección/ejecución posterior (§§29–30) | Estados separados y snapshots | Conforme en arquitectura; falta verificación de diccionario/generador |
| Outcome y Value independientes (§§4, 9, 17, 21) | Ecuación sintética de V y regla fija | Requiere mantener trazabilidad de regla, entidad, dimensiones y horizonte en el contrato de datos |

### 32.9. Dictamen y decisiones pendientes

**Conforme en arquitectura:**
- separación de intervención, accesibilidad, aplicabilidad, selección y ejecución;
- uso de una condición técnica verificable para inducir accesibilidad;
- distinción entre escenario aislado y escenario adversarial;
- separación de Outcome y Value;
- uso de snapshots temporales y actualización de T_acc.

**No conforme todavía para congelación causal:**
- sustitución potencial de ΔT_acc por A_f*;
- identificación del contraste de políticas de provisión con θ_A(q);
- ausencia de C_dep,0 y accesibilidad focal basal;
- ambigüedad entre intento, éxito y probabilidad final de accesibilidad;
- soporte de g0/g1 por historia;
- equivalencia de versiones y calidad condicional de τ2.

**Decisión:** S4-R no se congela todavía. Se mantiene como diseño focal sintético en borrador. La siguiente corrección debe preservar el objeto completo ΔT_acc y definir explícitamente θ_Af(q*) como estimando focal, además de completar la cadena basal/provisión/verificación. Solo después procede una revisión independiente externa del paquete.

**Estado:** auditoría cruzada documental interna realizada; hallazgos C145-01…06 registrados como provisionales; no aceptados ni cerrados. No es revisión independiente por especialistas externos. No implementado, no simulado, no ejecutado ni validado empíricamente. XSYNC-138-01 permanece abierto. No modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres previos. No autoriza implementación ni ejecución científica.


---

## 33. Propuesta de corrección del estimando focal S4-R (sección conversacional 146)

**Estado:** propuesta metodológica derivada de C145-01…06; pendiente de revisión independiente y aceptación. No congela S4-R, no cierra XSYNC-138-01 y no modifica C10-D1.

### 33.1. Regla de conservación del constructo completo

Se conserva como objeto transformacional de referencia el cambio estructurado completo:

ΔT_acc = (A⁺, A⁻, ΔR, ΔC),

con las precisiones de identidad, equivalencia, granularidad y evidencia que correspondan al contrato TGCV. La notación es esquemática: los componentes se registran según la representación versionada y no se reducen a cardinalidad.

La transformación focal de S4-R es τ2. Su accesibilidad focal se registra en cada momento:
- A_f,0*: accesibilidad verdadera de τ2 en la configuración basal;
- A_f,1*: accesibilidad verdadera de τ2 después del mecanismo de provisión y verificación;
- ΔA_f: cambio focal derivado de ambas evaluaciones.

La proyección focal se representa como:

ΔA_f = h_f(ΔT_acc; τ2, X, H0, C_c),

donde h_f extrae únicamente el cambio relativo a τ2, bajo la identidad, condiciones y horizonte especificados. No sustituye ni agota ΔT_acc.

El analizador debe recibir la representación completa de ΔT_acc y la medición focal permitida; el evaluador conserva la verdad generadora. La clasificación de A_f no puede reconstruirse a partir de Outcome, Value, selección o ejecución.

### 33.2. Estimando focal restringido

Se propone distinguir:

- **θ_A(q):** estimando general de C10-D1, definido sobre políticas factibles de cambios estructurados de accesibilidad A=ΔT_acc bajo un régimen común q.
- **θ_Af(q*):** estimando focal de S4-R, restringido a políticas que inducen cambios en la accesibilidad de τ2 bajo q* y mantienen constantes las restantes dimensiones relevantes de ΔT_acc, salvo que el diseño declare y modele otra modificación.

La forma de trabajo para S4-R es:

θ_Af(q*) = E[V^(q*,g^Af_1)] − E[V^(q*,g^Af_0)].

g^Af_1 y g^Af_0 son políticas objetivo factibles sobre la modificación focal ΔA_f. No asignan A_f* como etiqueta abstracta: representan distribuciones de cambio focal inducidas por mecanismos implementables. El estimando solo queda definido para la población, horizonte, régimen, reglas de Value y soporte que se especifiquen.

La correspondencia de implementación es:

g^B_0, g^B_1
→ B_g
→ W_attempt
→ S_install
→ C_dep,1
→ A_f,1*
→ ΔA_f
→ ΔT_acc
→ Reach/Π
→ selección/ejecución
→ Outcome
→ Value.

Las políticas de provisión g^B son mecanismos de implementación de las políticas focales g^Af; no son idénticas a ellas. La igualdad de sus contrastes solo puede sostenerse bajo consistencia de versiones, mapeo verificable, exclusión de vías alternativas y supuestos de identificación explícitos.

### 33.3. Condiciones para interpretar θ_Af como contribución de accesibilidad

La interpretación focal requiere:
1. población primaria definida antes de la asignación, con A_f,0*=0 y condiciones basales compatibles, o una formulación explícita que modele accesibilidad basal;
2. g^B_0/g^B_1 implementables y factibles en cada historia de la población objetivo;
3. diferencia inducida verificable en ΔA_f, no solo en intento de provisión;
4. medición de ΔT_acc completo, demostrando qué componentes cambian y cuáles permanecen invariantes;
5. ausencia de cambios diferenciales en otras vías hacia Value o identificación separada de esas vías;
6. calidad condicional de ejecución de τ2 y versiones de intervención comparables en el escenario aislado;
7. q* común, completo, explícito y compatible con condiciones constitutivas;
8. medición independiente de Outcome y Value, con regla, entidad/beneficiario, dimensiones y horizonte fijados;
9. temporalidad, interferencia, pérdidas, error de medición y soporte tratados conforme al diseño.

Si B_g cambia otras condiciones o mecanismos con vías propias hacia Value, el contraste de asignación identifica el efecto de la política de provisión/paquete, no θ_Af(q*). Si el mapeo entre política de provisión y accesibilidad focal no es identificable, declarar no-identificación de la atribución focal.

### 33.4. Corrección de la verdad analítica ilustrativa

La igualdad previa:

θ_A(q*) = 6(0.80−0.20)=3.6

se debe releer, mientras no se resuelva la auditoría, como una verdad analítica candidata del DGP focal, no como el estimando general de C10-D1.

Bajo la población primaria con A_f,0*=0, condiciones restantes satisfechas, políticas que inducen:

P(A_f,1*=1 | g^Af_1)=.80;
P(A_f,1*=1 | g^Af_0)=.20,

y el DGP:

M = 1 + ΔA_f + 0.5X + ε_M;
O = 2M + ε_O;
V = 3O + 4L_m + ε_V,

con errores de media cero, distribución común entre políticas, sin interacciones ni vías alternativas desde B_g/C_dep hacia M, O o V, se obtiene:

E[ΔA_f|g^Af_1]−E[ΔA_f|g^Af_0]=.60;
θ_Af(q*)=6×.60=3.6.

Esta derivación es válida solo bajo las condiciones enumeradas. Si A_f,0* no es cero para toda la población, la diferencia entre probabilidades de acceso final no equivale automáticamente a la diferencia en ΔA_f; el DGP y el valor verdadero deben recalcularse.

El valor 3.6 no es evidencia empírica, umbral de relevancia ni confirmación de C10. Tampoco demuestra el efecto de cambios no focales de ΔT_acc.

### 33.5. Consecuencias para escenarios y controles

- S4-R aislado estima, si se cumplen las condiciones, el contraste focal θ_Af(q*) bajo exclusión estipulada.
- S4-R ampliado introduce vías adicionales y debe producir un dictamen de efecto de política/paquete o no-identificación cuando no sea posible separar la contribución focal.
- S7 y otros escenarios que modifican composición, relaciones o configuraciones conservan su función de comprobar que el analizador no reduce ΔT_acc a A_f* ni a cardinalidad.
- S8 conserva la distinción entre cambio de accesibilidad y cambio de Reach.
- S9 conserva la posibilidad de cambio de Value sin cambio de accesibilidad.
- Los escenarios de medición mantienen separados A_true, A_obs, ΔA_f y ΔT_acc completo.

No se cambia la matriz S0–S10 ni se agregan pruebas ejecutables en esta sección. La correspondencia y cobertura deberán revisarse antes de congelar el contrato.

### 33.6. Decisión propuesta y pendientes

**Propuesta:** mantener S4-R como experimento sintético focal sobre τ2, nombrar provisionalmente su estimando θ_Af(q*), conservar ΔT_acc completo como constructo TGCV y no afirmar equivalencia con θ_A(q) general.

**Pendientes antes de congelación:**
1. confirmar definición de h_f y su relación con la representación completa ΔT_acc;
2. definir C_dep,0, A_f,0*, W_attempt, S_install y C_dep,1;
3. recalibrar p0/p1 como probabilidades de accesibilidad focal final en la población primaria;
4. completar q* y el soporte por historia;
5. formalizar las condiciones de exclusión y equivalencia de versiones;
6. comprobar que la regla sintética de Value y sus dimensiones están trazadas en el diccionario;
7. reconciliar el contrato con C10-D1 §§17, 30–32;
8. someter la revisión a especialistas independientes antes de aceptar el contrato.

**Estado:** propuesta correctiva documental; no aceptada, no congelada, no implementada, no simulada ni ejecutada. C145-01…06 permanecen abiertos hasta resolución y revisión independiente. XSYNC-138-01 permanece abierto. No modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 ni cierres previos. No autoriza implementación ni ejecución científica.


---

## 34. Contrato formal provisional de variables y ecuaciones de S4-R (sección conversacional 147)

**Estado:** especificación formal de trabajo derivada de §§30–33; propuesta, no aceptada ni congelada. No implementada, simulada, ejecutada ni auditada mediante pruebas. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 34.1. Unidad, población y tiempos

- Unidad experimental: sistema sintético independiente (i).
- Población objetivo primaria: unidades definidas antes de asignación, con estado basal verificable y ambas políticas de provisión factibles bajo las historias incluidas.
- (t_0): evaluación basal previa a la asignación.
- (t_1): asignación de política.
- (t_2): provisión e intento de instalación.
- (t_3): verificación técnica de la dependencia.
- (t_4): evaluación ciega de accesibilidad y snapshot completo de (T_{acc}), antes de selección/ejecución.
- (t_5): generación de Reach y trayectorias candidatas.
- (t_6): selección y ejecución.
- (t_7): medición de Outcome.
- (t_8): construcción de Value según regla preespecificada.

Los tiempos son orden causal, no duraciones fijadas. Cada snapshot tiene identificador, timestamp lógico, versión del catálogo/reglas, unidad, historia, fuente y calidad de evidencia. Una modificación posterior crea un snapshot nuevo; nunca sobrescribe el anterior.

### 34.2. Variables basales y régimen común

| Variable | Definición | Momento / uso |
|---|---|---|
| (i) | Identificador de unidad sintética | Todos los tiempos |
| (X_i) | Covariables basales preespecificadas | (t_0); heterogeneidad/estratificación |
| (H_{0i}) | Historia previa relevante | (t_0); soporte y políticas |
| (S_{0i}) | Estado inicial del sistema | (t_0); generación transformacional |
| (C_{c,i}) | Condiciones constitutivas/habilitantes de τ2 | (t_0) y snapshots; no se fijan en valores incompatibles |
| (L_{m,i}) | Variables de historia/mecanismo que el diseño incluye en el régimen común | Según secuencia; no agrupar automáticamente todo post-tratamiento |
| (q^*) | Régimen común, explícito y factible sobre (X,H_0,L_m) según la historia | Preespecificado antes de resultados |

(q^*) no es una distribución marginal ilustrativa aislada. Debe declarar para cada componente: definición, tiempo, quién/qué puede intervenirlo, dependencia de la historia, soporte y mecanismo de asignación. Si un componente no es manipulable ni estandarizable coherentemente, no se presenta como intervención de (q^*); se trata conforme a su papel causal en el diseño. Las condiciones constitutivas (C_c) se conservan compatibles con τ2 y no se fuerzan mediante una distribución común que haga imposible la transformación.

### 34.3. Asignación y mecanismo de provisión

| Variable | Definición | Regla |
|---|---|---|
| (Z_{g,i}) | Asignación aleatoria a política (g_0^B) o (g_1^B) | Asignación, no accesibilidad |
| (B_{g,i}) | Versión/procedimiento de provisión técnica asignado | Debe tener especificación y versión |
| (W_{attempt,i}) | Intento efectivo de instalación/activación | No equivale a éxito |
| (S_{install,i}) | Éxito técnico del procedimiento | Resultado del intento |
| (C_{dep,0,i}) | Estado basal de dependencia antes de asignación | Medido en (t_0) |
| (C_{dep,1,i}) | Estado final verificado de dependencia | Medido en (t_3) |
| (E_{verify,i}) | Evidencia de verificación de instalación, integridad, compatibilidad y operación | Ciega a Outcome/Value |

Descomposición de la dependencia:
- (C_{install}): componente presente/instalado;
- (C_{integrity}): integridad verificada;
- (C_{compat}): compatibilidad con el sistema y versión objetivo;
- (C_{oper}): funcionamiento operativo comprobado.

(C_{dep,1}=1) solo si las cuatro condiciones están respaldadas por evidencia suficiente. Los estados posibles de cada componente son verdadero respaldado, falso respaldado o indeterminado. La ausencia de evidencia no se recodifica automáticamente como fallo ni como éxito.

Cadena de implementación:

[
Z_g ightarrow B_g ightarrow W_{attempt}
ightarrow S_{install} ightarrow C_{dep,1}.
]

La asignación (Z_g) se conserva para ITT. No se condiciona el análisis principal a instalación exitosa, porque (S_{install}) es post-asignación.

### 34.4. Accesibilidad focal y espacio transformacional completo

- (A^*_{f,0,i}): accesibilidad verdadera de τ2 en (t_0).
- (A^*_{f,1,i}): accesibilidad verdadera de τ2 tras verificación en (t_3/t_4).
- (Delta A_{f,i}=A^*_{f,1,i}-A^*_{f,0,i}), con valores (-1,0,+1).
- (A^{obs}_{f,1,i}): medición del analizador; puede diferir de la verdad generadora.
- (T_{acc,0,i}), (T_{acc,1,i}): representación completa versionada del espacio de transformaciones accesibles.
- (Delta T_{acc,i}): cambio completo entre snapshots, incluyendo transformaciones añadidas/eliminadas y cambios relevantes en relaciones/condiciones, sin reducirlo a cardinalidad.
- (h_f): proyección versionada que extrae el cambio focal de τ2 desde la representación completa bajo condiciones, identidad y horizonte definidos.

[
Delta A_{f,i}=h_f(Delta T_{acc,i};	au_2,X_i,H_{0i},C_{c,i}).
]

La regla estructural de accesibilidad de τ2 se propone como:

[
A^*_{f,1,i}=1
iff
C_{dep,1,i}=1
land C_{auth,i}=1
land C_{resource,i}=1
land C_{capacity,i}=1
land C_{info,i}=1
land C_{domain,i}=1
land C_{other,i}=1.
]

La expresión es válida solo si el catálogo de condiciones necesarias está completo para el entorno sintético. Cada condición debe tener evidencia, instante y estado epistémico. La accesibilidad no implica aplicabilidad inmediata, selección ni ejecución. La regla de accesibilidad no se infiere de Outcome ni de Value.

La población primaria más simple para la ilustración analítica puede restringirse ex ante a (A^*_{f,0}=0), con condiciones restantes compatibles. Esta restricción debe aplicarse antes de asignar (Z_g), nunca retrospectivamente según (C_{dep,1}), ejecución o resultados. Si no se restringe, el DGP debe modelar explícitamente la accesibilidad basal y la distribución de (Delta A_f).

### 34.5. Transformaciones, Reach, trayectorias y ejecución

| Variable | Definición |
|---|---|
| (Pi_{H,i}) | Trayectorias candidatas generadas desde (S_0,T_{acc},R_{acc},C_{acc}), con horizonte (H) |
| (Reach_{H,i}) | Estados alcanzables mediante transformaciones accesibles y aplicables hasta (H) |
| (App_{	au_2,i}) | Aplicabilidad de τ2 en el estado/historia actual |
| (Sel_i) | Trayectoria seleccionada |
| (Exec_i) | Registro de ejecución efectiva, parcial, completa o interrumpida |

Se mantiene (H=3) como horizonte provisional del juguete colectivo, según el contrato previo. Accesibilidad y aplicabilidad se reevalúan por estado y snapshot. Las trayectorias candidatas no se reconstruyen retrospectivamente a partir de estados observados. Los estados observados sirven para contrastar ejecución y resultados, no para definir por sí solos el espacio previo de transformaciones.

### 34.6. Outcome y Value

- (O_i): resultado observado de la ejecución bajo definición independiente.
- (V_i): valor construido con regla preespecificada (R_V), beneficiario/entidad (B_V), dimensiones, horizonte y tratamiento de costes, beneficios, compensaciones e incertidumbre.
- La regla (R_V) no puede premiar automáticamente más transformaciones, mayor longitud de trayectoria ni la propia clasificación de accesibilidad.
- El evaluador conserva la verdad del DGP; el analizador recibe solo los datos y reglas que tendría un analista legítimo.

La forma lineal de juguete (V=3O+4L_m+epsilon_V) se conserva únicamente como escenario analítico provisional. Antes de congelar debe documentarse qué representa cada componente de Value, su unidad/escala, beneficiario y horizonte. Si (L_m) es parte del régimen común (q^*), su distribución se define y aplica de forma coherente en ambos brazos; no se ajusta mecánicamente por variables post-tratamiento.

### 34.7. Políticas, estimandos y límites de identificación

Se distinguen tres cantidades:

1. **Efecto por asignación (ITT):**
[
TE_Z=E[Vmid do(Z_g=1)]-E[Vmid do(Z_g=0)].
]
Es el efecto causal de asignar las políticas de provisión, bajo aleatorización, consistencia, ausencia de interferencia relevante y manejo válido de pérdidas.

2. **Contraste de política de provisión bajo régimen común:**
[
psi_B(q^*)=E[V^{q^*,g_1^B}]-E[V^{q^*,g_0^B}].
]
Compara las políticas implementables de provisión. No es automáticamente un efecto de accesibilidad.

3. **Contribución focal de accesibilidad:**
[
	heta_{Af}(q^*)=
E[V^{q^*,g_1^{Af}}]-E[V^{q^*,g_0^{Af}}].
]
Compara políticas objetivo que inducen distribuciones diferentes de (Delta A_f), bajo el mismo régimen (q^*). Requiere definirlas como intervenciones factibles y demostrar que el mapeo desde (g^B) preserva consistencia de versiones, soporte y exclusión de vías alternativas.

La equivalencia (psi_B(q^*)=	heta_{Af}(q^*)) no se presume. Solo podría sostenerse en el DGP aislado si las políticas difieren únicamente en la accesibilidad focal inducida y todas las demás vías relevantes permanecen invariantes. Si la provisión modifica costes, tiempos, información, expectativas, calidad, seguridad, selección u otras variables con vías propias hacia Value, el resultado es efecto de política/paquete o exige diseño adicional. No se obtiene (	heta_{Af}) restando efectos ni ajustando automáticamente por variables post-tratamiento.

Tampoco se identifica (	heta_{Af}) por el mero hecho de aleatorizar (Z_g). La aleatorización identifica ITT; la atribución a accesibilidad necesita supuestos/diseño adicionales sobre el mediador focal, medición, confusión mediador–resultado, versiones y vías alternativas.

### 34.8. DGP focal ilustrativo y condición para el valor 3.6

Para una ilustración deliberadamente simple, se puede estipular:
- (A^*_{f,0}=0) para toda unidad de la población primaria;
- condiciones restantes satisfechas y comunes;
- (P(A^*_{f,1}=1mid g_1^{Af})=.80);
- (P(A^*_{f,1}=1mid g_0^{Af})=.20);
- (Delta A_f=A^*_{f,1});
- (M=1+Delta A_f+0.5X+epsilon_M);
- (O=2M+epsilon_O);
- (V=3O+4L_m+epsilon_V);
- errores de media cero y distribución común, sin interacciones ni vías alternativas desde la provisión/dependencia hacia (M,O,V);
- distribución de (X,L_m) y régimen (q^*) comunes en los dos brazos.

Entonces:

[
E[Delta A_fmid g_1^{Af}]-E[Delta A_fmid g_0^{Af}]=0.80-0.20=0.60,
]

y, dado que el efecto de (Delta A_f) sobre (M) es 1, de (M) sobre (O) es 2 y de (O) sobre (V) es 3:

[
	heta_{Af}(q^*)=0.60	imes1	imes2	imes3=3.6.
]

Esta es una verdad matemática condicional del DGP focal, no evidencia empírica ni validación de C10. Si el estado basal no es cero, las condiciones restantes varían, existe fallo diferencial, hay interacción o aparece una vía alternativa, el valor debe derivarse de nuevo y puede no ser 3.6.

### 34.9. Diccionario mínimo y trazabilidad de datos

Cada registro debe incluir como mínimo:
- IDs: scenario_id, unit_id, replicate_id, snapshot_id, intervention_version;
- tiempos/orden: t0…t8, timestamp lógico y evento;
- basales: X, H0, S0, C_c, C_dep,0, A_f,0*;
- intervención: Z_g, B_g, W_attempt, S_install, C_dep,1, evidencia de verificación;
- transformacional: catálogo/versiones, U_acc, R_acc, C_acc, T_acc, ΔT_acc, A_f,1*, ΔA_f, A_f,obs;
- mecanismos: Reach, Π_H, App, selección, ejecución y estado de ejecución;
- resultados: O, V, regla R_V, beneficiario, dimensiones, horizonte y componentes;
- calidad: estado epistémico, fuente, confianza/calidad de evidencia, missingness y motivo;
- reproducibilidad: DGP/versiones, semilla, configuración, hashes y orden de generación.

La verdad del generador (por ejemplo A_f* y coeficientes verdaderos) se conserva en un artefacto separado y no se entrega al analizador. El analizador no recibe etiquetas de escenario, coeficientes causales verdaderos ni resultados de evaluación. La separación de roles debe poder auditarse.

### 34.10. Invariantes y puertas pendientes

Invariantes del DGP aislado:
1. Z_g se asigna antes de provisión.
2. W_attempt no se confunde con S_install ni con C_dep,1.
3. A_f* se deriva de condiciones verificadas; nunca se asigna directamente.
4. ΔT_acc completo se conserva y A_f* es solo su proyección focal.
5. accesibilidad, aplicabilidad, selección y ejecución son estados distintos.
6. no hay vías directas/alternativas desde B_g/C_dep hacia O/V fuera de la cadena transformacional focal.
7. calidad condicional de τ2 y demás versiones no focales son comunes.
8. q* y la población objetivo se preespecifican; ambas políticas tienen soporte por historia.
9. Value no se construye desde ΔT_acc, longitud de trayectoria ni selección.
10. snapshots no se sobrescriben y la evaluación de accesibilidad es ciega a O/V.
11. la asignación aleatoria identifica ITT, no automáticamente θ_Af.
12. cualquier violación de invariantes se registra y clasifica como escenario adversarial, efecto de paquete o no-identificación.

Puertas aún abiertas:
- definición completa y factibilidad de q*;
- contrato de política (g^{Af}) y mapeo verificable desde (g^B);
- especificación de población basal y C_dep,0;
- justificación de exclusión y equivalencia de versiones;
- definición completa de Value;
- precisión Monte Carlo, δ/ε y tamaño final;
- reconciliación con C10-D1 y revisión verdaderamente independiente;
- cobertura del diccionario y de las matrices de escenarios/pruebas.

**Dictamen:** el contrato de variables y ecuaciones queda especificado como propuesta provisional y mejora la consistencia entre §§30–33. No se considera cerrado ni congelable. Los parámetros .20/.80 y 3.6 siguen siendo ilustrativos. No se ha implementado, simulado, ejecutado ni validado. XSYNC-138-01 permanece abierto. No autoriza implementación ni ejecución científica.


---

## 35. Auditoría matemática y de identificación de S4-R (sección conversacional 148)

**Alcance:** revisión analítica del contrato de §34 y su compatibilidad con C10-D1. No es simulación, ejecución de estimadores, auditoría de código ni revisión independiente externa. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 35.1. Dictamen general

El contrato distingue correctamente ITT de asignación, efecto de política de provisión y estimando focal. Sin embargo, el estimando focal todavía no está plenamente identificado por una intervención implementable. La notación (g^{Af}) describe políticas objetivo sobre cambios de accesibilidad, pero el contrato no define todavía un mecanismo concreto que las implemente sin asignar directamente (A_f^*), ni demuestra que las políticas de provisión (g^B) sean versiones equivalentes de esas políticas focales.

Por tanto:
- (TE_Z) es identificable por aleatorización de (Z_g), sujeto a consistencia, interferencia, pérdidas y cumplimiento del protocolo.
- (psi_B) es un efecto de política de provisión; si (q^*) se aplica realmente y está bien definido, puede ser el estimando de la intervención conjunta.
- (	heta_{Af}) es un objetivo causal focal conceptualmente formulado, pero su identificación a partir de (Z_g) no está demostrada.
- El valor 3.6 es una derivación algebraica del DGP focal bajo supuestos fuertes, no una cantidad ya identificada por el diseño de provisión.

### 35.2. Hallazgo MATH-148-01 — (g^{Af}) carece de implementación independiente

La definición de §34.7 requiere políticas (g_1^{Af},g_0^{Af}) que induzcan distribuciones de (Delta A_f). Pero §34.3 solo proporciona una intervención concreta sobre provisión (B_g). No existe aún un procedimiento distinto y ejecutable para asignar o inducir (g^{Af}).

No debe resolverse asignando directamente (A_f^*), porque eso repetiría la abstracción que el diseño pretende evitar. Hay dos opciones coherentes:

1. **Estimando de política implementada:** mantener (g^B) como intervención concreta y estimar (psi_B(q^*)). Solo denominar su efecto contribución focal de accesibilidad si se estipula y verifica la exclusión de otras vías y la equivalencia de versiones en el DGP.
2. **Diseño de intervención focal adicional:** especificar un mecanismo implementable que cambie la condición necesaria de τ2, con asignación propia y manipulación verificable, sin asignar directamente el estado de accesibilidad. Debe demostrar que no modifica otras causas de Value y que induce la variación focal requerida.

Hasta elegir y formalizar una de estas opciones, (	heta_{Af}) debe mantenerse como estimando objetivo no identificado, no como efecto recuperable garantizado por la aleatorización de (Z_g).

### 35.3. Hallazgo MATH-148-02 — las tres cantidades no son intercambiables

Se conserva la separación:

[
TE_Z=E[Vmid do(Z_g=1)]-E[Vmid do(Z_g=0)]
]

[
psi_B(q^*)=E[V^{q^*,g_1^B}]-E[V^{q^*,g_0^B}]
]

[
	heta_{Af}(q^*)=E[V^{q^*,g_1^{Af}}]-E[V^{q^*,g_0^{Af}}].
]

El primer contraste corresponde a asignar las políticas tal como se implementan en el ensayo. El segundo corresponde a políticas de provisión bajo el régimen común declarado. El tercero corresponde a políticas focales de accesibilidad que todavía requieren implementación y definición propias.

La igualdad (TE_Z=psi_B(q^*)) requiere que el régimen (q^*) coincida con el régimen efectivamente aplicado por diseño, además de consistencia y ausencia de contaminación entre versiones. Si (q^*) es una intervención hipotética distinta de lo aplicado, no es el ITT observado.

La igualdad (psi_B(q^*)=	heta_{Af}(q^*)) requiere que la provisión no tenga vías relevantes hacia Value distintas del cambio focal de accesibilidad y sus consecuencias transformacionales, y que las versiones sean equivalentes en todo lo demás. Esta igualdad es una restricción del DGP aislado, no una consecuencia de aleatorizar (Z_g).

### 35.4. Hallazgo MATH-148-03 — covariables basales no son automáticamente parte de (q^*)

En §34.2 se describe (q^*) como régimen sobre (X,H_0,L_m). Esa expresión puede inducir a tratar covariables basales como variables intervenidas.

Corrección:
- (X,H_0,S_0) definen población, historia, estratificación, condicionamiento y heterogeneidad; no son intervenciones por defecto.
- (q^*) debe designar únicamente un régimen común sobre variables que el diseño pueda intervenir o estandarizar mediante una operación causal explícita.
- Si se desea estandarizar respecto a la distribución basal, se debe declarar una población objetivo/distribución de referencia (P^*(X,H_0)), no describirla como una intervención sobre (X,H_0).
- (C_c) son condiciones constitutivas compatibles; no deben asignarse a valores que hagan imposible τ2.
- Cada componente de (L_m) requiere clasificación temporal y causal antes de incorporarse a (q^*).

La notación debe distinguir (P^*(X,H_0)), régimen (q^*(L)) y políticas (g). No se deben mezclar distribución poblacional, intervención y condicionamiento en una sola letra.

### 35.5. Hallazgo MATH-148-04 — (L_m) y el riesgo de fijar mediadores post-tratamiento

La expresión (V=3O+4L_m+epsilon_V) puede ser coherente como DGP, pero la interpretación depende de cuándo y cómo se genera (L_m).

Se requieren tres casos distintos:

1. **(L_0) basal:** antecede a (Z_g); puede formar parte de (X/H_0), estratificar o condicionar, pero no es post-tratamiento.
2. **(L_1) post-asignación y previo a accesibilidad:** si (Z_g/B_g) puede afectarlo y también afecta (A_f) o Value, es variable inducida por tratamiento y posible confusor mediador–resultado. No se debe ajustar ingenuamente ni fijar como común sin definir una intervención secuencial.
3. **(L_2) posterior a accesibilidad o mecanismo transformacional:** puede ser mediador o consecuencia de la vía focal. Fijarlo en (q^*) podría bloquear parte del efecto que se pretende atribuir a accesibilidad.

Por ello, la fórmula actual debe tratar (L_m) como variable ilustrativa no causalmente clasificada hasta definir su momento y mecanismo. Para el DGP lineal más simple, la opción más limpia es eliminar el término (4L_m) de la ecuación principal de Value, o redefinirlo como covariable basal (L_0) con distribución común por aleatorización/estandarización. Si se mantiene un (L) post-tratamiento, debe introducirse en el DAG y en el régimen longitudinal correspondiente, y recalcularse el estimando.

### 35.6. Hallazgo MATH-148-05 — derivación de 3.6 y condiciones exactas

Bajo el DGP simplificado:
[
M=1+Delta A_f+0.5X+epsilon_M,quad
O=2M+epsilon_O,quad
V=3O+epsilon_V,
]
con (A_{f,0}^*=0), (E[epsilon_M]=E[epsilon_O]=E[epsilon_V]=0), distribuciones de errores invariantes, ausencia de interacciones y de vías alternativas, y la misma distribución de (X) bajo ambas políticas, se obtiene:

[
E[Vmid g_1^{Af}]-E[Vmid g_0^{Af}]
=3cdot2cdot1{E[Delta A_fmid g_1^{Af}]-E[Delta A_fmid g_0^{Af}]}.
]

Si las probabilidades de accesibilidad final son .80 y .20 y la población basal cumple (A_{f,0}^*=0), entonces la diferencia de medias de (Delta A_f) es .60 y el contraste es 3.6.

Si se mantiene (+4L_m), el término se cancela solo si su distribución esperada es igual bajo ambas políticas; esa igualdad debe derivarse del diseño/DGP, no asumirse por el nombre (q^*). Con interacción, heterogeneidad, accesibilidad basal distinta de cero, efectos de provisión directos o errores diferenciales, el producto (6	imes.60) deja de ser la verdad general.

La ecuación de 3.6 es, por tanto, una prueba algebraica condicional y debe etiquetarse como tal.

### 35.7. Hallazgo MATH-148-06 — ITT y notación de identificación

La expresión (E[Vmid do(Z_g=z)]) es notación contrafactual/intervencional. No es literalmente una media observada condicionada en (Z_g=z). Bajo aleatorización, consistencia, positividad de asignación y pérdidas manejadas válidamente, se identifica por la media observada correspondiente:
[
E[V(z)]=E[Vmid Z_g=z].
]
La estimación concreta será diferencia de medias o un estimador compatible con la asignación/estratificación. No debe confundir la definición del estimando con su fórmula de identificación estadística.

Además, la aleatorización de (Z_g) no aleatoriza (A_f), no garantiza exclusión y no elimina confusión mediador–Outcome/Value inducida tras la asignación. Un análisis por instalación exitosa o por accesibilidad observada no sustituye al ITT y puede introducir sesgo de selección.

### 35.8. Matriz de dictamen

| Elemento | Dictamen | Acción |
|---|---|---|
| (TE_Z) | Identificable por asignación bajo supuestos de ensayo | Mantener como efecto primario de política asignada |
| (psi_B(q^*)) | Definible si q* es implementado y documentado | Precisar si coincide con el régimen real del ensayo |
| (	heta_{Af}(q^*)) | Objetivo focal, aún no identificado por el diseño descrito | Definir intervención implementable o limitar interpretación |
| (P^*(X,H_0)) | Distribución de población, no intervención | Separar de q* |
| (L_m) | Ambiguo por temporalidad/rol causal | Clasificar L0/L1/L2 y revisar ecuación |
| Valor 3.6 | Algebraicamente correcto bajo DGP focal simplificado | Mantener como ilustración condicional, no evidencia |
| Equivalencia provisión-accesibilidad | Supuesto fuerte, no demostrado por aleatorización | Auditar vías y versiones |

### 35.9. Correcciones propuestas antes de congelar

1. Decidir si S4-R se presenta primariamente como ensayo de política de provisión con ITT (psi_B), o si se añade una intervención focal implementable para identificar (	heta_{Af}).
2. Separar distribución basal de referencia (P^*(X,H_0)) del régimen intervenido (q^*).
3. Clasificar (L_m) por temporalidad y rol causal; simplificar el DGP principal si no se necesita un confusor post-tratamiento.
4. Especificar el mapeo entre políticas, primera etapa de accesibilidad y estimando, sin igualar probabilidades de instalación con probabilidades de (Delta A_f) salvo derivación.
5. Mantener ITT como resultado identificado por aleatorización y reportar no-identificación de (	heta_{Af}) cuando falten supuestos/diseño.
6. Recalcular la verdad analítica del DGP solo después de resolver los puntos anteriores.

**Conclusión:** el contrato de §34 es matemáticamente coherente como arquitectura de variables, pero no demuestra todavía la identificación del estimando focal. La fórmula 3.6 es correcta únicamente bajo la versión simplificada y explícita del DGP. La siguiente versión debe resolver el estatus de (g^{Af}), (q^*), (L_m) y la relación entre ITT, política de provisión y accesibilidad focal. No se autoriza simulación ni ejecución por esta auditoría.


---

## 36. Propuesta de identificación instrumental focal de S4-R (sección conversacional 149)

**Estado:** propuesta metodológica para resolver MATH-148-01…06. No aceptada ni congelada; requiere revisión independiente y escenarios adversariales. No se ha implementado, simulado ni ejecutado. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 36.1. Decisión de diseño

Se propone no añadir por ahora una segunda intervención que asigne directamente la condición focal. S4-R se mantiene como ensayo sintético de políticas de provisión con asignación aleatoria (Z_g), y se distinguen:

- **Estimando primario:** efecto ITT de la política de provisión, (psi_B), bajo el protocolo efectivamente asignado.
- **Estimando secundario de mecanismo:** efecto causal local de la accesibilidad focal inducida por la política, identificable mediante variable instrumental solo bajo supuestos explícitos.
- **Estimando general C10:** contribución de cambios estructurados de (T_{acc}) a Value en la población/contextos objetivo. No queda identificado automáticamente por este instrumento focal.

Esta estrategia evita asignar directamente (A_f^*), pero limita la interpretación a las unidades cuyo estado de accesibilidad focal responde a la política, salvo supuestos adicionales de homogeneidad o identificación de efectos en otros estratos.

### 36.2. Variables para el diseño instrumental

Se definen:
- (Z_gin{0,1}): asignación aleatoria a política de provisión baja/alta.
- (A_f=Delta A_fin{0,1}): cambio focal de accesibilidad de τ2, en la población primaria con (A_{f,0}^*=0).
- (V): Value final, construido con regla independiente.
- (X,H_0): variables basales de estratificación/heterogeneidad y definición de población.
- (P^*(X,H_0)): distribución basal de referencia para la población objetivo, distinta de un régimen de intervención.
- (C_{dep,0},C_{dep,1}): dependencia técnica antes y después de la provisión; son mecanismo de primera etapa, no sustitutos de (A_f).
- (W_{attempt},S_{install}): intento y éxito de instalación, variables intermedias observadas.

En el DGP focal más simple, las condiciones restantes para τ2 se fijan como satisfechas y estables, (C_{dep,0}=0), y (A_f=C_{dep,1}). En variantes más realistas, la accesibilidad se deriva de todas las condiciones necesarias; la primera etapa debe medirse sobre (A_f), no inferirse únicamente de la instalación.

### 36.3. Estimandos identificables

El efecto de asignación es:

[
ITT_V=E[Vmid Z_g=1]-E[Vmid Z_g=0].
]

La primera etapa es:

[
ITT_A=E[A_fmid Z_g=1]-E[A_fmid Z_g=0].
]

Si (ITT_A
e0), el estimador instrumental de Wald es:

[
	heta_{IV}=rac{ITT_V}{ITT_A}.
]

Con instrumento binario, accesibilidad focal binaria, asignación aleatoria, consistencia, ausencia de interferencia, exclusión, monotonicidad y relevancia, (	heta_{IV}) identifica el **efecto causal medio local (LATE)** de la accesibilidad focal sobre Value entre las unidades cumplidoras (compliers), es decir, aquellas para las que la política cambia (A_f) de 0 a 1.

No identifica por sí solo:
- el efecto medio de accesibilidad en toda la población (ATE);
- el efecto en unidades siempre accesibles o nunca accesibles;
- el efecto de todos los cambios posibles de (T_{acc});
- el efecto de una política distinta de las dos versiones estudiadas;
- una contribución universal de accesibilidad a Value.

Si los efectos de accesibilidad son homogéneos en todos los estratos relevantes, LATE puede coincidir con ATE; esta homogeneidad es un supuesto adicional, no una consecuencia del instrumento.

### 36.4. Supuestos de identificación y condiciones de refutación

1. **Independencia:** (Z_g) es aleatorio respecto de los resultados potenciales y estados potenciales de accesibilidad, según el diseño y estratos de asignación.
2. **Relevancia:** la asignación cambia la probabilidad de (A_f=1); la primera etapa se estima y reporta con incertidumbre.
3. **Exclusión:** (Z_g) afecta Value únicamente mediante (A_f) y las consecuencias causales que se siguen de esa accesibilidad en el sistema TGCV. No puede existir vía directa de provisión, instalación o asignación hacia Value fuera de la vía focal.
4. **Monotonicidad:** ninguna unidad se vuelve menos accesible a τ2 por recibir la política de provisión alta, frente a la baja. Si existen defiers, el Wald estándar no tiene la interpretación LATE habitual.
5. **Consistencia y versiones:** cada política y cada estado focal tienen versiones suficientemente especificadas; no se mezclan tratamientos distintos bajo una misma etiqueta.
6. **No interferencia relevante:** la asignación de una unidad no modifica la accesibilidad o Value de otras unidades, salvo que el diseño modele explícitamente interferencia.
7. **Medición válida:** (A_f) se evalúa con criterios independientes de Outcome y Value; el error de clasificación se valida o se incorpora a análisis de sensibilidad.
8. **Población y soporte:** ambas políticas son factibles y la asignación tiene probabilidad positiva en cada estrato de la población objetivo.

La exclusión es el supuesto más exigente. La asignación de (Z_g) puede alterar expectativas, prioridad, información, entrenamiento, tiempo, costes, seguridad, mantenimiento, calidad o decisiones. Si cualquiera de estas vías alcanza Value sin pasar por la accesibilidad focal, el instrumento no identifica el LATE propuesto. Un test de balance o un resultado no significativo en controles negativos no demuestra por sí solo exclusión.

### 36.5. Ejemplo algebraico y reinterpretación del 3.6

En el DGP focal simplificado:
- (P(A_f=1mid Z_g=1)=.80);
- (P(A_f=1mid Z_g=0)=.20);
- (A_f) es binaria y la población cumple (A_{f,0}^*=0);
- el efecto estructural de (A_f) sobre (M) es 1, de (M) sobre (O) es 2 y de (O) sobre (V) es 3;
- no hay vías alternativas desde (Z_g/B_g/C_{dep}) hacia Value;
- no hay interacciones ni heterogeneidad del efecto focal en esta versión ilustrativa.

Entonces:

[
ITT_A=.80-.20=.60.
]

[
ITT_V=6	imes.60=3.6.
]

[
	heta_{IV}=ITT_V/ITT_A=3.6/.60=6.
]

Interpretación:
- **3.6** es el efecto medio de asignar la política alta en lugar de la baja en este DGP.
- **6** es el efecto causal por unidad de cambio de accesibilidad en la versión homogénea del DGP; bajo los supuestos IV, con heterogeneidad sería el LATE de los compliers.
- Ninguno de los dos números constituye evidencia empírica ni prueba de C10.

Si se mantiene un término (L_m) en la ecuación de Value, debe ser basal o tener distribución esperada igual por el diseño y no abrir una vía directa desde (Z_g). La versión primaria de S4-R debería eliminar (L_m) post-tratamiento del DGP principal. Los confusores inducidos y vías alternativas se reservan para variantes adversariales explícitas.

### 36.6. Qué hacer con (q^*)

Para la versión primaria simple:
- sustituir la notación ambigua de intervención común sobre (X,H_0) por una población/distribución de referencia (P^*(X,H_0));
- definir (X,H_0) antes de la asignación;
- aleatorizar (Z_g) dentro de estratos basales si procede;
- no introducir un régimen post-tratamiento (q^*) si no existe una variable longitudinal concreta que deba intervenirse.

Si una variante requiere controlar una historia post-asignación, debe definirse un régimen secuencial explícito, con orden temporal, intervención factible, probabilidades por historia y soporte. No se llamará (q^*) a una estandarización estadística que no corresponda a una intervención coherente.

### 36.7. Escenarios sintéticos que debe incluir la auditoría instrumental

| Variante | DGP | Dictamen esperado del analizador |
|---|---|---|
| IV-01 | Relevancia, exclusión y monotonicidad verdaderas; efecto homogéneo | Recuperar ITT, primera etapa y efecto focal 6 |
| IV-02 | Supuestos IV válidos; efecto heterogéneo | Recuperar LATE, no etiquetarlo ATE |
| IV-03 | Instrumento débil o primera etapa nula | No estimar atribución focal estable; reportar falta de relevancia |
| IV-04 | Vía directa (Z_g/B_g	o V) | Rechazar interpretación IV focal; conservar ITT de política |
| IV-05 | Defiers/no monotonicidad | No atribuir Wald a LATE estándar |
| IV-06 | Error de clasificación en (A_f^{obs}) | Cuantificar sesgo/sensibilidad; no usar A observada como verdad |
| IV-07 | Cambio de coste/tiempo/calidad por provisión | Efecto de paquete o instrumento inválido para accesibilidad |
| IV-08 | Accesibilidad basal heterogénea | Separar always-takers, never-takers y compliers; definir población objetivo |
| IV-09 | Interferencia entre unidades | Declarar estimando de exposición/interferencia o no-identificación |
| IV-10 | Violación de consistencia/versiones | No combinar versiones; redefinir intervención o limitar alcance |

Los escenarios deben generarse con verdad conocida y analizarse a ciegas. La evaluación separará: recuperación de ITT, primera etapa, diagnóstico de supuestos, recuperación LATE y construcción de Value. No se agregará un score único.

### 36.8. Relación con C10-D1 y alcance TGCV

El diseño instrumental focaliza una sola dimensión de (Delta T_{acc}), concretamente el cambio de accesibilidad de τ2. El instrumento no identifica la contribución causal de todas las transformaciones, relaciones y condiciones de (T_{acc}). La representación completa sigue siendo obligatoria para la evaluación TGCV.

Si la pregunta científica es el efecto de la accesibilidad focal, el LATE es un objetivo legítimo y acotado. Si la pregunta es el efecto general de cambios de (T_{acc}) sobre Value, harán falta variaciones y diseños que cubran composición, relaciones, condiciones y contextos, además de τ2. No se generalizará desde este juguete a ese estimando general.

### 36.9. Decisión propuesta

1. Mantener S4-R como ensayo aleatorizado de política de provisión.
2. Definir ITT de Value como estimando primario identificable por asignación.
3. Añadir el análisis instrumental como estimando secundario de mecanismo, condicionado a los supuestos IV.
4. Denominar el resultado secundario LATE de accesibilidad focal, no ATE ni efecto general de (Delta T_{acc}).
5. Mantener la versión homogénea con verdad analítica 6 como caso de calibración; conservar 3.6 como ITT de política.
6. Añadir IV-01…IV-10 a la matriz de escenarios, pendiente de reconciliación y aceptación.
7. Mantener explícitamente variantes donde la exclusión, relevancia, monotonicidad o medición fallen.
8. No simular, ejecutar ni congelar hasta revisar independientemente este contrato y reconciliarlo con C10-D1.

**Dictamen:** la vía instrumental ofrece una estrategia de identificación focal más concreta sin asignar directamente (A_f^*), pero depende críticamente de exclusión, monotonicidad y validez de la primera etapa. La identificación resultante sería local a los compliers, no una atribución poblacional general. Propuesta documental pendiente de revisión; XSYNC-138-01 permanece abierto.


---

## 37. Auditoría adversarial de la restricción de exclusión instrumental (sección conversacional 150)

**Estado:** auditoría conceptual interna de la propuesta IV de §36. No es prueba empírica de exclusión, auditoría independiente externa, simulación ni ejecución. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 37.1. Pregunta de auditoría

¿La asignación aleatoria a la política de provisión (Z_g) puede afectar Value por alguna vía distinta del cambio focal de accesibilidad (A_f) de τ2 y sus consecuencias transformacionales?

La vía focal pretendida es:

[
Z_gightarrow B_gightarrow C_{dep,1}ightarrow A_f
ightarrow T_{acc}ightarrow Pi_Hightarrow Sel
ightarrow Execightarrow Oightarrow V.
]

Se consideran parte de la vía focal los cambios posteriores que solo ocurren porque τ2 se vuelve accesible y puede ser aplicable, seleccionada y ejecutada. No son vías alternativas el mero hecho de que existan mediadores entre accesibilidad y Value: son el mecanismo causal que se desea estudiar.

La exclusión instrumental se viola si existe una ruta causal desde (Z_g), (B_g) o (C_{dep,1}) hasta Value que no dependa de (A_f) y de sus consecuencias transformacionales. La ruta puede ser directa o pasar por variables intermedias.

### 37.2. Distinción crítica: dependencia habilitadora frente a efecto propio del componente

(C_{dep}) puede desempeñar dos papeles distintos:

1. **Condición habilitadora:** la dependencia instalada solo permite que τ2 sea realizable. No cambia por sí misma el estado operativo, rendimiento, seguridad, costes, tiempos, información ni decisiones. En el DGP aislado, su único efecto causal es cambiar (A_f).
2. **Componente con efectos propios:** además de habilitar τ2, la dependencia modifica rendimiento, latencia, fiabilidad, mantenimiento, seguridad, coste, información, formación, atención o conducta. Cualquier efecto sobre Value que no requiera que τ2 sea accesible constituye una vía que amenaza exclusión.

No basta con llamar a (C_{dep}) «condición de accesibilidad» para garantizar el primer papel. El generador debe declarar qué propiedades cambian y qué propiedades permanecen invariantes. Si el software está activo y altera el sistema incluso cuando τ2 no se ejecuta o no es aplicable, la exclusión puede fallar.

### 37.3. Mapa de vías y clasificación

| Ruta o mecanismo | Clasificación IV | Motivo |
|---|---|---|
| (Z_g	o B_g	o C_{dep}	o A_f	o T_{acc}	oPi_H	o Exec	o O	o V) | Vía focal permitida | La provisión afecta Value a través de la accesibilidad y su desarrollo transformacional |
| (B_g	o) menor coste operativo (	o V), sin depender de (A_f) | Violación | Efecto propio de la provisión |
| (C_{dep}	o) mayor velocidad/latencia (	o O/V), sin τ2 | Violación | Efecto funcional del componente independiente de la transformación focal |
| (C_{dep}	o) mayor seguridad o fiabilidad basal (	o V) | Violación | Mejora directa del sistema no mediada por accesibilidad |
| (B_g	o) formación/atención del personal (	o Sel/Exec/V) sin pasar por (A_f) | Violación | Efecto de acompañamiento o expectativa |
| (Z_g	o) prioridad/incentivos/expectativas (	o Sel/Exec/V) | Violación | Efecto conductual de la asignación |
| (A_f	o) nueva trayectoria posible (	o) selección/ejecución (	o V) | Vía focal permitida | Consecuencia de la nueva posibilidad transformacional |
| (A_f	o) más opciones percibidas (	o) selección (	o V) | Vía focal permitida si la percepción surge únicamente de la accesibilidad real | Si la política comunica información adicional por sí misma, aparece una vía alternativa |
| (C_{dep}	o) calidad de ejecución de τ2, condicionada a que τ2 sea accesible y ejecutada | Ambigua; requiere definición de versión | Puede ser parte del mecanismo de τ2 o una versión distinta; no debe quedar sin especificar |
| (Z_g	o) medición diferencial de (A_f) o (V) | Amenaza de medición | Puede sesgar primera etapa, ITT o Wald |

La ruta focal puede incluir selección, ejecución y mediadores. No exige que todas las unidades ejecuten τ2: el estimando IV refleja el efecto de inducir accesibilidad en la población de cumplidores, incluyendo las consecuencias reales de que esa opción esté disponible.

### 37.4. Por qué la exclusión no es verificable solo con los datos observados

La independencia de (Z_g) puede estar respaldada por el procedimiento de aleatorización; la relevancia puede examinarse mediante la primera etapa; consistencia, interferencia y medición admiten auditorías parciales. Pero la exclusión es una restricción contrafactual sobre rutas que no se observan simultáneamente.

No existe un test estadístico general que demuestre que (Z_g) no tiene ninguna vía alternativa hacia (V). En particular:
- balance basal no prueba exclusión;
- ausencia de diferencias significativas en variables auxiliares no prueba exclusión;
- controles negativos sin efecto no descartan todas las vías alternativas;
- ajustar por variables post-tratamiento puede bloquear parte del efecto focal o inducir sesgo;
- que el Wald recupere el valor esperado en un DGP donde la exclusión fue programada no valida exclusión en un sistema real.

Por tanto, la exclusión debe tratarse como supuesto de diseño y conocimiento mecanístico, sometido a análisis adversarial y sensibilidad; nunca como resultado demostrado por un p-valor.

### 37.5. Condiciones del DGP aislado para que IV-01 sea un control válido

El escenario de calibración IV-01 solo debe declarar exclusión verdadera si el generador impone explícitamente:

1. Los dos brazos usan el mismo procedimiento, interfaz, instrucciones, contacto, formación, prioridad, atención, hardware, recursos, calendario y criterios de soporte.
2. La asignación solo altera la probabilidad de que la dependencia habilitadora quede instalada, íntegra, compatible y operativa.
3. (C_{dep}) no altera el funcionamiento del sistema fuera de hacer realizable τ2.
4. No hay reducción de costes, latencia, riesgo o carga de trabajo independiente de τ2.
5. No se informa al personal de la asignación de forma que cambie expectativas, esfuerzo, selección o conducta.
6. No existe acceso alternativo a τ2 en el brazo de menor provisión ni una ruta sustituta equivalente no catalogada.
7. La accesibilidad se evalúa antes de selección/ejecución, mediante el mismo procedimiento ciego en ambos brazos.
8. La regla de Value y su medición son idénticas y ciegas a la asignación.
9. No hay interferencia ni spillovers entre unidades.
10. Las versiones de τ2, sus precondiciones y la calidad de su ejecución son invariantes; cualquier diferencia se declara como versión/tratamiento adicional.

Si la implementación requiere que el brazo alto reciba más visitas, formación, tiempo de técnicos o prioridad, el DGP ya no es un instrumento puro salvo que esas diferencias se demuestre que no abren vías hacia Value fuera de (A_f). La igualdad de recursos nominales no basta si la experiencia efectiva difiere.

### 37.6. Ambigüedad de las probabilidades .20/.80

Las probabilidades .20 y .80 deben definirse como probabilidades de accesibilidad focal inducida por la asignación, no como meras probabilidades de intento ni de instalación sin demostrar el mapeo.

Se requiere registrar por separado:
- (P(W_{attempt}=1mid Z_g));
- (P(S_{install}=1mid W_{attempt},Z_g));
- (P(C_{dep,1}=1mid Z_g));
- (P(A_f=1mid Z_g)).

En el DGP más simple, con (A_{f,0}=0), todas las demás condiciones satisfechas y (A_f=C_{dep,1}), se puede programar (P(A_f=1mid Z=0)=.20) y (P(A_f=1mid Z=1)=.80). En una variante con fallos de compatibilidad, condiciones basales o medición imperfecta, estas probabilidades no coinciden necesariamente. La primera etapa debe calcularse sobre (A_f) verdadero para el evaluador y sobre (A_f^{obs}) para el analizador.

### 37.7. Pruebas adversariales de exclusión

Se amplía la matriz IV con los siguientes casos:

| ID | Alteración del DGP | Verdad | Dictamen esperado |
|---|---|---|---|
| EXCL-01 | Componente solo habilita τ2; resto idéntico | Exclusión válida por construcción | IV puede recuperar LATE |
| EXCL-02 | Componente mejora latencia aunque τ2 no se use | Vía alternativa | ITT válido; IV focal no válido |
| EXCL-03 | Provisión reduce costes de operación independientemente de τ2 | Vía alternativa | Efecto de paquete; no atribuir a accesibilidad |
| EXCL-04 | Formación/atención adicional modifica selección | Vía alternativa | IV inválido salvo diseño que aisle esa vía |
| EXCL-05 | Personal conoce asignación y cambia esfuerzo | Vía alternativa potencial | Exclusión no establecida |
| EXCL-06 | Componente mejora calidad/seguridad sin τ2 | Vía alternativa | IV focal inválido |
| EXCL-07 | Calidad de τ2 cambia entre versiones de instalación | Consistencia/versión amenazada | Redefinir tratamiento o separar versiones |
| EXCL-08 | Medición de accesibilidad depende del brazo | Medición diferencial | Primera etapa sesgada; auditoría de medición |
| EXCL-09 | Acceso alternativo a τ2 en G0 | Contraste contaminado | Revisar exclusividad y primera etapa |
| EXCL-10 | Efecto de provisión sobre Value solo aparece cuando τ2 se vuelve accesible y sigue su mecanismo | Compatible con vía focal | IV admisible si los demás supuestos se sostienen |
| EXCL-11 | Spillover de instalación entre unidades | Interferencia | Wald individual estándar no identificado |
| EXCL-12 | Efecto directo pequeño, conocido y no nulo desde (Z_g) a (V) | Exclusión falsa | Cuantificar sesgo; no presentar Wald como LATE |

Para EXCL-12, el generador puede usar:
[
V=eta A_f+delta Z_g+epsilon,
qquad
	heta_{Wald}=eta+rac{delta}{ITT_A}.
]
Así se muestra que una vía directa pequeña puede amplificarse cuando la primera etapa es débil. Esta ecuación es un diagnóstico analítico del sesgo, no una corrección automática.

### 37.8. Sensibilidad a violaciones de exclusión

Se propone que el evaluador sintético calcule la sensibilidad del Wald ante un efecto directo hipotético (delta):

[
	heta(delta)=rac{ITT_V-delta}{ITT_A}.
]

El analizador no conoce el (delta) verdadero en escenarios ciegos; puede reportar una curva o intervalo de sensibilidad para valores plausibles justificados externamente. No debe elegir (delta) para obtener el resultado deseado ni presentarlo como estimación empírica del efecto directo.

Con (ITT_A=.60), cada unidad de efecto directo (delta) desplaza el cociente en (delta/.60). Si la primera etapa disminuye, la sensibilidad se amplifica. El informe debe presentar:
- primera etapa e incertidumbre;
- ITT de Value e incertidumbre;
- Wald y su incertidumbre bajo los supuestos;
- sensibilidad a (delta);
- justificación de rangos plausibles de (delta);
- dictamen de identificación: compatible, amenazada o no defendible.

No se fija todavía un rango numérico de (delta); requiere escala de Value, relevancia sustantiva y justificación preespecificada.

### 37.9. Límites de los controles negativos y de la auditoría de mecanismos

Los controles negativos pueden revelar algunas violaciones:
- medir latencia, coste, calidad, seguridad, esfuerzo, formación y expectativas incluso en unidades donde τ2 no llega a ser accesible;
- comprobar si (Z_g) cambia esos resultados auxiliares;
- incluir resultados que no deberían depender de τ2;
- usar escenarios sintéticos con vías alternativas conocidas.

Pero estos controles no prueban exclusión: pueden tener poca potencia, medir imperfectamente o no cubrir todas las vías. Un resultado nulo solo limita las alternativas medidas bajo la precisión del estudio.

El DGP debe separar:
- variables que son consecuencias legítimas de la nueva accesibilidad y su uso;
- variables que cambian por la política/provisión independientemente de la accesibilidad;
- variables cuya clasificación es incierta y exige sensibilidad.

No ajustar automáticamente por ninguna de ellas. La función de los controles es diagnosticar y acotar, no reparar sin supuestos el instrumento.

### 37.10. Dictamen y decisiones propuestas

1. Mantener IV-01 como control sintético de exclusión verdadera, con invariantes explícitos.
2. Añadir EXCL-01…EXCL-12 como matriz adversarial, sin confundirla con pruebas empíricas de exclusión.
3. Distinguir dependencia puramente habilitadora de componente con efectos propios.
4. Definir .20/.80 como probabilidades de accesibilidad focal solo en el DGP simple; separar intento, instalación, dependencia y accesibilidad en variantes generales.
5. Añadir sensibilidad a efecto directo (delta), sin fijar rango hasta definir escala y relevancia de Value.
6. Mantener ITT como estimando primario de política; no atribuir el Wald a accesibilidad si exclusión no es defendible.
7. Si exclusión no puede sostenerse en un caso real, reportar ITT/efecto de paquete y clasificar la atribución focal como no identificada, sin presentar el IV como confirmatorio.
8. Someter el contrato a revisión independiente antes de implementación o simulación.

**Dictamen:** la estrategia IV es coherente como diseño sintético condicionado, pero la exclusión es un supuesto fuerte y no verificable directamente. El DGP aislado puede validar que el analizador recupera el LATE cuando el supuesto es verdadero y rechaza la interpretación focal cuando se introduce una vía alternativa conocida. No puede demostrar que la exclusión se cumpla en un sistema real. XSYNC-138-01 permanece abierto; no se ha implementado, simulado, ejecutado ni aceptado el diseño.


---

## 38. Auditoría de monotonicidad, cumplimiento y versiones del tratamiento (sección conversacional 151)

**Estado:** auditoría conceptual interna de los supuestos IV de §36–37. No es validación empírica, revisión independiente externa, simulación ni ejecución. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 38.1. Dictamen central

El hecho de que la política alta produzca una primera etapa media mayor que la política baja:

[
E[A_fmid Z_g=1]>E[A_fmid Z_g=0]
]

no demuestra monotonicidad individual:

[
A_f(1)ge A_f(0)quad	ext{para cada unidad}.
]

La primera expresión es una diferencia de medias observable bajo aleatorización. La segunda es una restricción sobre dos estados potenciales de la misma unidad, de los cuales como máximo uno se observa. No se puede verificar directamente con los datos del ensayo.

En políticas estocásticas de provisión, elevar la probabilidad media de instalación no excluye que algunas unidades pierdan accesibilidad bajo la política alta por incompatibilidad, sustitución de componentes, interrupción de servicio, errores de despliegue, conflictos de versiones o desplazamiento de recursos.

### 38.2. Definición de estados potenciales y estratos de cumplimiento

Para instrumento binario (Z_g) y accesibilidad focal binaria (A_f), se definen (A_f(0)) y (A_f(1)), accesibilidad que tendría la unidad bajo cada asignación.

Los estratos principales son:

| Estrato | (A_f(0)) | (A_f(1)) | Interpretación |
|---|---:|---:|---|
| Always-taker | 1 | 1 | Accesible con ambas políticas |
| Never-taker | 0 | 0 | Inaccesible con ambas |
| Complier | 0 | 1 | La política alta induce accesibilidad |
| Defier | 1 | 0 | La política alta elimina accesibilidad |

Monotonicidad excluye defiers. En un sistema real, los estratos son contrafactuales y no pueden clasificarse individualmente sin supuestos o diseños adicionales. La asignación aleatoria identifica proporciones marginales y la primera etapa, no la pertenencia individual a cada estrato.

Para el estimando focal de cambio (Delta A_f), la población primaria debe tener (A_{f,0}=0) antes de asignación. Si se incluyen unidades ya accesibles, el resultado binario post-asignación mezcla siempre-accesibles con unidades cuya accesibilidad cambia; debe definirse si el tratamiento es (A_{f,1}) o el cambio (Delta A_f), sin intercambiar ambos.

### 38.3. Qué puede y qué no puede demostrar la primera etapa

Con (P(A_f=1mid Z=1)=.80) y (P(A_f=1mid Z=0)=.20), la primera etapa es .60. Esto acredita relevancia media en el DGP si se calcula con (A_f) verdadero. No acredita monotonicidad.

Una política alta puede generar una media mayor y, al mismo tiempo, crear defiers en una fracción de unidades, compensados por más compliers. En ese caso el Wald no tiene la interpretación LATE estándar de compliers.

La auditoría debe informar:
- diferencia de medias de (A_f) y su intervalo;
- distribución de instalación, compatibilidad, integridad y operatividad;
- fallos y pérdidas de accesibilidad por brazo;
- sensibilidad a proporciones hipotéticas de defiers;
- distinción entre evidencia observable y supuesto contrafactual.

No se etiquetará monotonicidad como «verificada» a partir de una primera etapa positiva o de ausencia de incidentes observados.

### 38.4. Mecanismo de provisión compatible con monotonicidad

Para un DGP sintético de calibración, una construcción transparente es:

[
U_isim Uniforme(0,1),qquad
A_i(z)=mathbb{1}[U_ile p_z],
qquad p_0=.20, p_1=.80.
]

Con el mismo (U_i) en ambos estados potenciales, se cumple por construcción (A_i(1)ge A_i(0)). Las unidades con (U_ile .20) son always-takers; con (.20<U_ile .80), compliers; con (U_i>.80), never-takers; no hay defiers. La proporción de compliers es .60.

Esta construcción es una **acoplación monotónica del DGP**, no una prueba de que una política real cumpla monotonicidad. Para mantener la interpretación técnica, el generador debe representar (U_i) como susceptibilidad/propensión basal a una instalación exitosa bajo versiones anidadas de la misma provisión, no como asignación directa de accesibilidad por el analizador.

Una alternativa física equivalente en el juguete es que la política alta añada oportunidades de instalación sin retirar ninguna oportunidad disponible bajo la política baja, con el mismo componente y sin desplazar recursos. Si el despliegue alto puede reemplazar, desinstalar o degradar una dependencia existente, la monotonicidad deja de estar garantizada.

### 38.5. Cumplimiento en cada etapa de la cadena

La cadena no debe colapsarse en una única variable de cumplimiento:

[
Z_gightarrow B_gightarrow W_{attempt}
ightarrow S_{install}ightarrow C_{dep}
ightarrow A_f^*ightarrow A_f^{obs}.
]

Se registrarán por separado:

- (Z_g): asignación aleatoria.
- (B_g): versión/procedimiento de provisión asignado y realmente ofrecido.
- (W_{attempt}): intento de instalación.
- (S_{install}): instalación técnicamente completada.
- (C_{dep}): dependencia verificada, íntegra, compatible y operativa.
- (A_f^*): accesibilidad focal verdadera, derivada de todas las condiciones necesarias.
- (A_f^{obs}): medición observada de accesibilidad.
- (App_f): aplicabilidad en el estado actual, condicionada a precondiciones.
- (Exec_f): ejecución efectiva de τ2.

No intentar instalar no equivale a instalación fallida; instalación completada no equivale a dependencia operativa; dependencia operativa no equivale a accesibilidad si falla otra condición constitutiva; accesibilidad no equivale a aplicabilidad ni ejecución.

El IV de §36 usa (Z_g) como instrumento de (A_f^*), no de (W_{attempt}), (S_{install}) o (C_{dep}) aisladamente. Si solo se mide instalación y se infiere accesibilidad, el estimando queda expuesto a error de clasificación y a condiciones no observadas.

### 38.6. Versiones del tratamiento y consistencia

La consistencia requiere que el tratamiento focal (A_f=1) represente una condición suficientemente definida. Sin embargo, la accesibilidad de τ2 puede obtenerse con dependencias, configuraciones, versiones, compatibilidades, latencias, garantías de seguridad o soporte técnico distintos.

Si esas versiones tienen efectos distintos sobre la calidad de τ2 o Value, (A_f) binaria no representa una intervención única. El estimando IV pasa a ser un efecto de una mezcla de versiones inducida por (Z_g), no un efecto bien definido de «accesibilidad» en abstracto.

Se requiere:
1. Identificador y versión de la dependencia.
2. Configuración, compatibilidad, integridad y pruebas de aceptación.
3. Versión del mecanismo τ2 y sus precondiciones.
4. Calidad/seguridad/latencia de la ejecución, diferenciadas de la mera accesibilidad.
5. Procedimiento de instalación, soporte y mantenimiento.
6. Registro de sustituciones, actualizaciones y reversión.
7. Regla de equivalencia de versiones definida antes de analizar Value.

Si las versiones son equivalentes en los atributos causales relevantes, pueden agruparse con justificación. Si no, deberán modelarse como tratamientos/versiones distintos, restringir la población o reconocer que el instrumento cambia tanto accesibilidad como versión. No se resolverá ajustando sin más por la versión post-tratamiento.

### 38.7. Monotonicidad de accesibilidad no implica monotonicidad de Value

La monotonicidad IV se refiere a (A_f(1)ge A_f(0)), no a que Value mejore para todas las unidades. Una transformación accesible puede no aplicarse, no seleccionarse, producir resultados desfavorables o implicar trade-offs. Por tanto, no se impondrá:

[
V_i(1)ge V_i(0).
]

El efecto causal local puede ser negativo, nulo o heterogéneo. Monotonicidad de accesibilidad no es una hipótesis normativa de beneficio ni una garantía de mejora de Value.

### 38.8. Matriz adversarial ampliada

| ID | Escenario | Verdad del DGP | Dictamen esperado |
|---|---|---|---|
| MON-01 | Oportunidades de instalación anidadas, sin retirada | Monotonicidad verdadera | Wald puede identificar LATE si demás supuestos se cumplen |
| MON-02 | Primera etapa positiva, con una fracción de defiers | Monotonicidad falsa | No llamar LATE estándar al Wald |
| MON-03 | Política alta sustituye/desinstala configuración funcional | Defiers posibles | Auditar pérdidas de accesibilidad; monotonicidad no establecida |
| MON-04 | Política alta aumenta instalación pero también incompatibilidad | Media puede subir y algunas unidades perder acceso | Primera etapa no demuestra monotonicidad |
| MON-05 | Unidad ya accesible en baseline | Always-taker posible | Definir población y tratamiento; no contar como cambio inducido |
| MON-06 | Instalación falla pero la dependencia ya existía | Cumplimiento de provisión y accesibilidad divergen | Medir baseline y estado final |
| MON-07 | Instalación exitosa, pero otra condición constitutiva falla | (C_{dep}=1), (A_f=0) | No usar instalación como proxy suficiente |
| MON-08 | Dos versiones de dependencia producen distinta calidad/Value | Tratamiento multiversión | Separar versiones o redefinir intervención |
| MON-09 | Política alta cambia soporte/formación y calidad de ejecución | Exclusión/versiones amenazadas | ITT de paquete; no atribución focal |
| MON-10 | Accesibilidad sube, pero Value cae por riesgo de τ2 | Monotonicidad de A verdadera; efecto V negativo | Mantener resultado negativo; no imponer beneficio |
| MON-11 | (A_f^*) monotónica, pero (A_f^{obs}) tiene error diferencial | Monotonicidad latente no basta para análisis observado | Validar medición y propagar incertidumbre |
| MON-12 | Interferencia o recursos compartidos generan desplazamiento entre unidades | Monotonicidad individual puede fallar | Redefinir unidad/exposición y estimando |

### 38.9. Sensibilidad y límites

No hay una prueba observacional general que certifique ausencia de defiers. Se propone:
- documentar por mecanismo por qué la política alta no puede retirar accesibilidad;
- auditar sustitución, desinstalación, degradación e incompatibilidad;
- presentar escenarios sintéticos con y sin defiers;
- evaluar sensibilidad a proporciones hipotéticas de defiers, sin afirmar que se estiman directamente;
- separar monotonicidad de accesibilidad de efectos sobre Value;
- si la política alta puede degradar acceso de algunas unidades, abandonar la interpretación LATE estándar o redefinir el tratamiento/población.

La sensibilidad a defiers debe ser un análisis del evaluador con verdad conocida en simulación futura; no es una corrección automática del Wald ni un test que pruebe monotonicidad.

### 38.10. Dictamen y decisiones propuestas

1. Mantener la primera etapa .60 como relevancia ilustrativa, no como evidencia de monotonicidad.
2. Definir el DGP de calibración con acoplación monotónica de (A_f(0),A_f(1)), manteniendo el mecanismo de provisión implementable.
3. Añadir MON-01…MON-12 a la matriz de escenarios.
4. Registrar todos los eslabones de cumplimiento, desde asignación hasta accesibilidad verdadera/observada, aplicabilidad y ejecución.
5. Definir baseline (A_{f,0}) y población primaria; si (A_{f,0}=1), no contar automáticamente la unidad como compliers.
6. Congelar versiones técnicas relevantes o modelarlas por separado; no mezclar versiones causalmente distintas bajo (A_f=1).
7. No imponer monotonicidad de Value ni interpretación beneficiosa.
8. Si monotonicidad no es defendible, reportar ITT de política y no presentar Wald como LATE estándar.
9. Someter la especificación revisada a revisión independiente antes de simulación o ejecución.

**Dictamen:** relevancia, monotonicidad, cumplimiento y consistencia son condiciones distintas. La política alta puede tener primera etapa positiva y aun así generar defiers. Una construcción monotónica es útil para calibración sintética, pero no valida el supuesto en sistemas reales. La interpretación LATE requiere además exclusión, consistencia/versiones, independencia y ausencia de interferencia. XSYNC-138-01 permanece abierto; no se ha implementado, simulado, ejecutado ni aceptado el diseño.


---

## 39. Auditoría de identificación estadística e inferencia del estimador Wald (sección conversacional 152)

**Estado:** especificación metodológica propuesta. No es simulación, resultado de potencia, auditoría independiente ni aceptación del diseño. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 39.1. Dos preguntas distintas

La inferencia de S4-R debe separar:

1. **Identificación causal:** bajo aleatorización, relevancia, exclusión, monotonicidad, consistencia/versiones y ausencia de interferencia, el cociente instrumental tiene interpretación LATE para los compliers.
2. **Recuperación estadística:** con el tamaño muestral, variabilidad, tasa de primera etapa, error de medición y estimador elegido, ¿se recupera ese parámetro con sesgo, cobertura y precisión aceptables?

Un estimando identificado puede estimarse con gran incertidumbre. Una estimación precisa no corrige supuestos causales falsos. El DGP sintético debe probar ambas dimensiones por separado.

### 39.2. Definición del estimador

Con instrumento aleatorio (Z_g), accesibilidad focal verdadera binaria (A_f) y Value (V):

[
widehat{ITT}_A=ar A_{Z=1}-ar A_{Z=0},qquad
widehat{ITT}_V=ar V_{Z=1}-ar V_{Z=0}.
]

El estimador de Wald es:

[
widehat{	heta}_{W}=
rac{widehat{ITT}_V}{widehat{ITT}_A}.
]

Bajo los supuestos de §36–38, estima LATE. Sin monotonicidad o exclusión puede seguir siendo un cociente descriptivo de formas reducidas, pero no tiene la interpretación LATE focal propuesta.

El analizador no recibe coeficientes ni estados potenciales verdaderos. Recibe asignación, variables observadas, protocolo de medición y reglas de análisis. El evaluador conserva el DGP, los estados potenciales y el efecto verdadero.

### 39.3. Riesgos de muestra finita y denominador débil

El cociente de dos estimaciones aleatorias no se comporta como una estimación lineal ordinaria:
- si la primera etapa es pequeña, el denominador puede acercarse a cero;
- el cociente puede presentar sesgo de muestra finita y distribución asimétrica;
- errores estándar delta/Wald pueden ser poco fiables con instrumento débil;
- intervalos simétricos pueden excluir valores plausibles o sugerir precisión inexistente;
- una primera etapa positiva en la muestra no garantiza una primera etapa poblacional suficientemente fuerte.

Por ello, no se declarará «instrumento fuerte» usando solo una regla mecánica ni se utilizará el estadístico F como certificado de validez causal. Se informarán tamaño, estimación e intervalo de la primera etapa, además de la incertidumbre del efecto reducido.

### 39.4. Inferencia del cociente y conjuntos de confianza

La especificación primaria debe construir un conjunto de confianza para el cociente mediante inversión de una prueba sobre:

[
ITT_V-	heta,ITT_A=0.
]

El enfoque de Fieller o una inversión equivalente de pruebas robustas a instrumento débil puede producir intervalos muy amplios, no acotados o disjuntos cuando la primera etapa es débil. Eso es un resultado informativo de falta de precisión, no un fallo que deba ocultarse.

El intervalo delta puede presentarse como complemento cuando la primera etapa sea suficientemente precisa y alejada de cero, nunca como único intervalo en escenarios de instrumento débil.

La implementación estadística concreta (Fieller, inversión tipo Anderson–Rubin para el parámetro de razón u otro método adecuado al estimando LATE) queda pendiente de selección y validación. No se asumirá que cualquier procedimiento denominado Anderson–Rubin identifica LATE bajo heterogeneidad; el método deberá justificarse para el parámetro de razón y el diseño exacto.

### 39.5. Aleatorización, estratos y errores estándar

La asignación (Z_g) debe analizarse según el esquema realmente generado:
- respetar bloques/estratos de aleatorización;
- ajustar por variables basales solo según un plan preespecificado;
- utilizar errores estándar compatibles con la unidad de asignación;
- si existe agrupación, asignación por clúster o interferencia dentro de clúster, definir la unidad independiente y la inferencia correspondiente;
- no tratar observaciones repetidas de una unidad como unidades independientes;
- reportar el número de unidades y clústeres, no solo el número de filas.

El análisis primario será por asignación (ITT). El análisis IV será secundario y no condicionará la muestra a haber instalado, cumplido, ejecutado τ2 o completado la trayectoria: hacerlo seleccionaría por variables post-asignación.

### 39.6. Recuperación bajo el DGP ilustrativo

En la versión homogénea y aislada de calibración:
- (P(A_f=1mid Z=0)=.20);
- (P(A_f=1mid Z=1)=.80);
- (ITT_A=.60);
- efecto focal por unidad de accesibilidad (=6);
- (ITT_V=3.60);
- Wald poblacional (=6).

Estas igualdades definen la verdad analítica de esa versión. No proporcionan por sí mismas error estándar, potencia ni garantía de recuperación con (N=2000). La varianza depende de la distribución de (V), errores, heterogeneidad, proporción de compliers, estratos, pérdidas, medición y diseño de asignación.

El tamaño provisional (N=2000) por réplica, 1:1, y 1000 réplicas Monte Carlo se conserva como configuración de diseño no validada. Debe aclararse en el contrato si (N) es total por réplica (1000 por brazo en asignación 1:1); la formulación actual se interpretará así salvo corrección explícita. No equivale a cálculo de potencia ni a tamaño recomendado para un piloto real.

### 39.7. Métricas de recuperación

Para cada escenario y réplica se guardarán:
- sesgo: promedio de (hat	heta-	heta_{true});
- sesgo relativo solo cuando el parámetro verdadero esté suficientemente separado de cero;
- RMSE;
- cobertura empírica del intervalo nominal del 95 %;
- anchura y proporción de intervalos no acotados/disjuntos;
- tasa de convergencia y fallos numéricos;
- frecuencia de primera etapa débil;
- error tipo I bajo nulo y potencia bajo alternativas;
- error Monte Carlo de cada métrica;
- calibración de intervalos y estimación de ITT/primera etapa por separado.

Para efectos nulos o próximos a cero, no se utilizará sesgo relativo ni porcentaje de recuperación como métrica principal. Se evaluarán sesgo absoluto, RMSE, cobertura y control de error tipo I. Los escenarios con efecto negativo y heterogeneidad se informarán por separado, sin ocultarlos en una media global.

### 39.8. Matriz de inferencia adversarial

| ID | DGP | Comportamiento esperado |
|---|---|---|
| INF-01 | Primera etapa .60, efecto homogéneo 6, exclusión y monotonicidad verdaderas | Recuperación calibrada de Wald/LATE con cobertura nominal aproximada |
| INF-02 | Primera etapa moderada, efecto heterogéneo | Recuperar LATE, no ATE |
| INF-03 | Primera etapa débil | Intervalos robustos amplios/no acotados; evitar falsa precisión |
| INF-04 | Primera etapa nula | No estimar efecto IV; informar no identificación por falta de relevancia |
| INF-05 | Efecto verdadero cero | Control de error tipo I y cobertura |
| INF-06 | Efecto negativo | Recuperar signo y magnitud sin imponer beneficio |
| INF-07 | Error de medición de (A_f) | Cuantificar distorsión; usar validación o sensibilidad |
| INF-08 | Pérdida diferencial post-asignación | Diagnosticar sesgo y no asumir datos faltantes al azar |
| INF-09 | Asignación por clúster ignorada en SE | Detectar inferencia anticonservadora |
| INF-10 | Heterogeneidad extrema y pocos compliers | Informar LATE impreciso y alcance limitado |
| INF-11 | Defiers | Rechazar interpretación LATE estándar |
| INF-12 | Exclusión violada por efecto directo (delta) | Wald sesgado; sensibilidad a (delta) y no atribución focal |
| INF-13 | Intervalo delta frente a Fieller/inversión robusta | Mostrar fallo de aproximación delta con denominador débil |
| INF-14 | N insuficiente pese a identificación válida | Concluir imprecisión, no ausencia de efecto |
| INF-15 | Nulo con intervalo estrecho dentro de margen predefinido | Permitir conclusión de equivalencia solo si margen y regla se fijaron antes |

### 39.9. Criterios de aceptación metodológica

La futura prueba sintética de inferencia no se considerará satisfactoria por recuperar el valor 6 en el escenario ideal solamente. Deberá:
1. recuperar ITT y primera etapa;
2. recuperar LATE en escenarios identificados;
3. no etiquetar LATE como ATE;
4. reconocer primera etapa nula/débil;
5. producir intervalos robustos al denominador débil;
6. mantener cobertura y error tipo I calibrados dentro de tolerancias preespecificadas;
7. detectar escenarios donde exclusión, monotonicidad, consistencia o medición fallan;
8. distinguir no-identificación, baja potencia e inexistencia de efecto;
9. cuantificar error Monte Carlo;
10. reproducir resultados con semilla, configuración y versiones registradas.

Las tolerancias numéricas, potencia mínima, δ, margen de equivalencia ε y reglas de aceptación siguen abiertos. No se fijarán retrospectivamente después de ver los resultados.

### 39.10. Dictamen

La auditoría concluye que el diseño necesita una evaluación explícita de inferencia de cociente, no solo una comparación de medias ni un error estándar convencional. El estimador Wald puede ser apropiado para el LATE bajo los supuestos, pero su recuperación depende de la fuerza de la primera etapa, tamaño muestral, variabilidad, heterogeneidad y método de intervalo.

**Decisión propuesta:** mantener ITT como estimando primario; Wald/LATE como análisis secundario condicionado; añadir INF-01…INF-15; conservar (N=2000) total por réplica y 1000 réplicas como valores provisionales; seleccionar y validar un método robusto de intervalo antes de implementar. No calcular ni declarar potencia todavía.

**Estado:** contrato estadístico propuesto, no ejecutado. XSYNC-138-01 y las decisiones abiertas de δ/ε, tolerancias y método de inferencia permanecen pendientes. No se ha realizado simulación, cálculo de potencia, experimento real ni aceptación.


---

## 40. Auditoría del error de medición de la accesibilidad (sección conversacional 153)

**Estado:** especificación metodológica propuesta. No es validación de instrumento de medida, simulación, auditoría independiente ni aceptación del diseño. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 40.1. Dos objetos de medición que no deben confundirse

La estrategia IV focal necesita distinguir:

- A_f*: estado verdadero de accesibilidad de la transformación focal τ2, derivado de todas sus condiciones constitutivas y de realizabilidad.
- A_f_obs: clasificación observada por el procedimiento de medición.
- T_acc*: espacio transformacional verdadero, representado por catálogo/versiones, relaciones y condiciones de accesibilidad.
- T_acc_obs: reconstrucción observada y documentada del espacio transformacional.

A_f* es una variable focal binaria útil para el contraste IV de S4-R; no es una representación suficiente de T_acc ni de ΔT_acc. La medición TGCV debe conservar cambios de composición, altas y bajas de transformaciones, relaciones y condiciones, incluidos cambios que no afecten a τ2.

El estado verdadero no se vuelve observable por definición. Debe existir una referencia operacional independiente, trazable y auditada, con reglas que no utilicen Outcome, ejecución ni Value para inferir retrospectivamente accesibilidad.

### 40.2. Matriz de error de clasificación

Para accesibilidad binaria, definir sensibilidad y especificidad:

- Se = P(A_f_obs = 1 | A_f* = 1).
- Sp = P(A_f_obs = 0 | A_f* = 0).

La tasa de falsos negativos es 1−Se; la tasa de falsos positivos es 1−Sp. Deben estimarse o acotarse por brazo, tiempo, versión técnica, contexto y evaluador cuando haya razones para esperar heterogeneidad.

No se supondrá automáticamente sensibilidad y especificidad perfectas, error no diferencial entre brazos, independencia del error respecto a versión/contexto/estado operativo, infalibilidad del evaluador experto ni independencia de mediciones repetidas.

La matriz de clasificación debe distinguir además estado accesible, inaccesible e indeterminado. No convertir indeterminado en inaccesible ni excluirlo silenciosamente.

### 40.3. Consecuencia analítica de error no diferencial

Si Se y Sp son constantes e iguales entre brazos, y el error se refiere a la clasificación binaria A_f*, entonces:

E[A_f_obs | Z=z] = (Se+Sp−1) P(A_f*=1 | Z=z) + (1−Sp).

Por tanto:

ITT_Aobs = (Se+Sp−1) × ITT_A*.

Si el numerador de Value está medido sin error diferencial y el instrumento satisface los demás supuestos, el Wald que usa accesibilidad observada queda:

Wald_obs = ITT_V / ITT_Aobs = LATE* / (Se+Sp−1).

Esto muestra que el error no diferencial no es inocuo para un mediador/endógeno instrumentado: puede atenuar la primera etapa y magnificar el cociente en valor absoluto cuando 0 < Se+Sp−1 < 1. Si Se+Sp=1, la medición no discrimina mejor que azar y la primera etapa observada se anula. Si el índice de Youden es negativo, la clasificación está invertida y debe corregirse con una regla de codificación validada, no interpretar el signo mecánicamente.

La relación anterior es exacta bajo los supuestos indicados; no es una corrección general aplicable cuando el error es diferencial, hay tres estados, cambios de clasificación a lo largo del tiempo o el estimando usa una exposición distinta de A_f*.

### 40.4. Error diferencial entre brazos y versiones

Si Se_z y Sp_z varían con la asignación:

E[A_f_obs | Z=z] = (Se_z+Sp_z−1)p_z + (1−Sp_z), donde p_z=P(A_f*=1 | Z=z).

La diferencia observada ya no es un múltiplo simple de la primera etapa verdadera. Puede aumentar, reducir, invertir o incluso crear una primera etapa aparente cuando la primera etapa verdadera es cero.

Causas plausibles:
- evaluadores conocen el brazo asignado;
- documentación más completa en el brazo de provisión alta;
- pruebas diagnósticas distintas según versión;
- dependencia parcialmente instalada clasificada como plenamente operativa;
- ventanas temporales distintas;
- evaluador infiere accesibilidad porque observó que τ2 se ejecutó;
- condiciones de acceso se reconstruyen retrospectivamente desde Outcome.

Se requiere medición ciega a asignación, selección, ejecución y Value, usando el mismo protocolo y ventana temporal. Si el cegamiento es imposible, registrar la exposición del evaluador y medir acuerdo/error mediante referencia independiente.

### 40.5. Referencia de validación independiente

Se propone una submuestra de validación seleccionada aleatoriamente, estratificada si es necesario por brazo y contexto, en la que un equipo independiente aplique una evaluación de referencia de A_f* y del snapshot T_acc*.

Requisitos:
1. Selección aleatoria o probabilidades conocidas de inclusión en la validación.
2. Evaluadores de referencia cegados a Z, A_f_obs, Outcome y Value cuando sea factible.
3. Aplicación de criterios de realizabilidad, identidad, precondiciones, recursos, dependencias y admisibilidad.
4. Snapshot temporal anterior a selección y ejecución.
5. Registro de evidencia, fuente, versión, evaluador, fecha y grado de incertidumbre.
6. Doble evaluación independiente en una fracción de la submuestra y adjudicación de discrepancias.
7. Estimación de Se/Sp y sus intervalos; análisis por brazo/versión/contexto si el tamaño lo permite.
8. Ponderación por diseño si la probabilidad de entrar en validación varía.
9. Propagación de incertidumbre de Se/Sp a primera etapa y Wald.
10. No usar Outcome o Value como patrón de oro.

Si la referencia también es imperfecta, no llamarla gold standard. Se necesitará una adjudicación compuesta, múltiples indicadores o análisis de sensibilidad a error residual. La submuestra de validación no convierte automáticamente A_f* en verdad conocida.

### 40.6. Métodos de análisis y límites

Se compararán, según el diseño:
- análisis principal con referencia de validación cuando esté disponible;
- corrección de clasificación usando Se/Sp estimadas, propagando incertidumbre;
- estimación con modelos de error de medición o likelihood conjunto cuando el diseño y datos lo permitan;
- análisis de sensibilidad para rangos plausibles de Se/Sp;
- límites parciales si no existe información suficiente para identificar tasas de error.

No se recomienda sustituir A_f* por la probabilidad posterior de accesibilidad sin definir un estimando y un modelo que justifique ese uso. Tampoco se recomienda corregir dividiendo automáticamente por el índice de Youden si Se/Sp son estimadas con error, varían entre brazos o el modelo no es identificable.

El analizador debe informar por separado:
- ITT de política sobre Value;
- primera etapa con A_f_obs;
- primera etapa corregida/estimada para A_f*, si identificable;
- Wald ingenuo y Wald corregido, claramente etiquetados;
- incertidumbre adicional por validación;
- sensibilidad a error diferencial;
- conclusión de identificación o no-identificación.

### 40.7. Error en la medición del espacio completo T_acc

La medición de A_f no resuelve la medición TGCV. Para T_acc se requiere auditar, como mínimo:
- omisiones de transformaciones accesibles;
- falsas inclusiones de transformaciones no realizables;
- identificación duplicada o incorrecta de transformaciones;
- errores en equivalencia y versiones;
- relaciones y dependencias ausentes o falsas;
- condiciones constitutivas mal clasificadas;
- estado indeterminado tratado como cierto;
- cambios temporales sobrescritos;
- catálogo incompleto y rutas alternativas no detectadas.

Se conservarán snapshots versionados de U_acc, R_acc y C_acc, con procedencia y evidencia. Las discrepancias entre T_acc_obs y referencia deben informarse como errores por dimensión, no reducirse a una sola exactitud binaria.

La reconstrucción de Reach y trayectorias se realizará desde el espacio transformacional observado y sus incertidumbres; el evaluador comparará con el espacio verdadero del DGP. No se inferirá T_acc a partir de transformaciones ejecutadas, estados alcanzados, Outcome o Value.

### 40.8. Escenarios adversariales de medición

| ID | Alteración | Resultado esperado |
|---|---|---|
| MEAS-01 | Se=Sp=1 | Primera etapa observada coincide con verdadera |
| MEAS-02 | Error no diferencial moderado | Primera etapa observada atenuada; Wald ingenuo distorsionado |
| MEAS-03 | Se+Sp=1 | Medición sin discriminación; primera etapa observada nula |
| MEAS-04 | Se/Sp difieren por brazo | Posible primera etapa espuria o invertida |
| MEAS-05 | Medición depende de versión técnica | Error heterogéneo; estimación agrupada cuestionable |
| MEAS-06 | Evaluador conoce Outcome/ejecución | Fuga retrospectiva; medición no independiente |
| MEAS-07 | Validación aleatoria con referencia adecuada | Recuperación de tasas de error y propagación de incertidumbre |
| MEAS-08 | Validación no aleatoria sin probabilidades conocidas | Sesgo de validación; corrección no identificada |
| MEAS-09 | Referencia también imperfecta | No declarar gold standard; sensibilidad/identificación parcial |
| MEAS-10 | Error en relaciones/condiciones pero no en τ2 | A_f puede estar bien medido mientras ΔT_acc está mal reconstruido |
| MEAS-11 | Accesibilidad indeterminada recodificada como 0 | Sesgo por clasificación forzada |
| MEAS-12 | Snapshot posterior a ejecución | Contaminación temporal y posible inferencia retrospectiva |
| MEAS-13 | Diferencial de pérdidas en submuestra de validación | Ponderación/identificación de validación amenazada |
| MEAS-14 | Medición binaria correcta pero catálogo incompleto | IV focal puede ser válido; inferencia TGCV sobre el espacio completo no |

### 40.9. Criterios de aceptación de medición

Antes de simulación confirmatoria o piloto se deberán preespecificar:
1. definición operacional de A_f* y T_acc*;
2. protocolo de referencia, evidencia y snapshot;
3. procedimiento de cegamiento;
4. diseño y tamaño de submuestra de validación;
5. tratamiento de indeterminados y discrepancias;
6. tasas de error admisibles o límites de sensibilidad justificados;
7. método de propagación de incertidumbre;
8. análisis de error diferencial;
9. métricas separadas para U, R y C;
10. reglas para concluir medición suficiente, limitada o no identificada.

No se fija ahora un umbral de Se/Sp ni de concordancia: dependerá de la escala, el impacto de falsos positivos/negativos, la precisión del IV y la finalidad TGCV. No se elegirá tras observar resultados.

### 40.10. Dictamen

El error de medición de accesibilidad puede sesgar directamente la primera etapa y el Wald; si es diferencial, puede incluso producir una primera etapa aparente. La aleatorización del instrumento no corrige ese problema. Se necesita una referencia independiente y una estrategia explícita para propagar incertidumbre.

A su vez, una medición fiable de la transformación focal no garantiza una reconstrucción válida del espacio T_acc. Ambas capas deben auditarse por separado.

**Decisión propuesta:** mantener A_f* como variable causal focal del DGP y A_f_obs como medición del analizador; incorporar MEAS-01…MEAS-14; añadir submuestra de validación independiente y análisis de sensibilidad; mantener la evaluación de T_acc multidimensional y temporal. No ejecutar todavía la simulación ni fijar umbrales.

**Estado:** contrato de medición propuesto, no implementado ni probado. XSYNC-138-01 y las decisiones abiertas de Se/Sp, validación, δ/ε, tolerancias y método de inferencia permanecen pendientes.


---

## 41. Auditoría de datos faltantes, pérdidas de seguimiento y selección post-asignación (sección conversacional 154)

**Estado:** especificación metodológica propuesta. No es simulación, análisis de datos, auditoría independiente ni aceptación. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 41.1. Principio: ausencia de dato no equivale a ausencia de transformación ni a valor cero

En C10-S la ausencia de un registro puede tener significados diferentes:
- el dato existe, pero no se capturó;
- el registro se perdió o quedó ilegible;
- la unidad abandonó el seguimiento;
- una evaluación no pudo realizarse por razones técnicas;
- la condición es genuinamente indeterminada;
- la transformación o el evento no ocurrió;
- la unidad dejó de ser observable por una consecuencia de la intervención.

Estos estados no se pueden codificar todos como cero, inaccesible, no ejecutado o Value nulo. Deben distinguirse ausencia de observación, estado negativo observado, indeterminación ontológica y evento realmente inexistente.

### 41.2. Puntos de pérdida en la cadena causal y transformacional

Se requiere un indicador de observación separado para cada bloque:

- R_Z: asignación y versión de política registradas.
- R_C: provisión, instalación y condiciones técnicas observadas.
- R_A: medición de A_f_obs disponible.
- R_T: snapshot y reconstrucción de T_acc_obs disponibles.
- R_M: mecanismos/condiciones intermedias observados.
- R_Pi: enumeración de trayectorias candidatas disponible.
- R_E: selección y ejecución documentadas.
- R_O: Outcome observado.
- R_V: Value evaluado.
- R_val: referencia independiente de validación disponible.

La pérdida puede ocurrir en un bloque y no en otros. No crear un indicador único de caso completo que oculte qué capa falta. Registrar motivo, fecha, responsable, estado de recuperación y relación temporal con Z, A, ejecución y Outcome.

La ausencia de ejecución no implica ausencia de trayectoria candidata; la ausencia de trayectoria registrada no implica que no existiera una ruta accesible; y la falta de Value evaluado no implica Value igual a cero.

### 41.3. Estimandos y población bajo pérdida

El ITT de política se define para la población asignada. El análisis de casos completos puede cambiar esa población si la observación depende de asignación, accesibilidad, ejecución, Outcome o factores pronósticos.

Se distinguirán:
1. Estimando en población asignada: efecto de política sobre Value definido para todas las unidades asignadas.
2. Estimando en población con Value observado: contraste entre quienes tienen R_V=1, descriptivo salvo que la selección sea ignorable o se ajuste bajo supuestos defendibles.
3. Estimando en población principal observable: efecto entre unidades que serían observables bajo ambas asignaciones; contrafactual y generalmente no identificado sin supuestos adicionales.
4. Estimando de supervivencia/retención: efecto de Z sobre la probabilidad de observación, abandono o disponibilidad del resultado.
5. Estimando parcial: límites o conjunto de efectos compatibles cuando Value falta y no puede identificarse puntualmente.

No sustituir el ITT de población asignada por el contraste de casos completos sin declararlo. Si Value no está definido para una unidad por razones ontológicas, distinguirlo de un Value definido pero no medido; redefinir población/estimando si es necesario.

### 41.4. Mecanismos de ausencia

Clasificar, con cautela, los mecanismos de datos faltantes:

- MCAR: ausencia independiente de variables observadas y no observadas. Supuesto fuerte, no deducible de una prueba no significativa.
- MAR: ausencia independiente del dato no observado condicionado a historia observada suficiente. Permite métodos como ponderación o imputación bajo correcta especificación y positividad.
- MNAR: ausencia aún depende del valor no observado o de factores no observados tras condicionar en la historia disponible. Requiere análisis de sensibilidad, modelos explícitos o límites; no se resuelve con imputación estándar.

Los mecanismos pueden diferir por bloque y tiempo. Por ejemplo, Value puede faltar por deterioro no observado aunque Outcome y ejecución estén registrados. No clasificar todo el dataset con una sola etiqueta MCAR/MAR/MNAR.

### 41.5. Selección post-asignación y sesgo de colisionador

No condicionar el análisis primario a haber instalado, cumplido, mantenido accesibilidad, seleccionado τ2, ejecutado una trayectoria, completado el seguimiento o disponer de una medición de referencia si esos estados pueden depender de Z y de causas de Value.

Ejemplo conceptual: Z → R_V ← U_V → V. Condicionar en R_V=1 puede abrir una asociación no causal entre Z y U_V, aun con Z aleatorizado. Análogamente, restringir a Exec_f=1 puede seleccionar unidades por accesibilidad y factores pronósticos.

La selección a validación también debe modelarse: si R_val depende de A observada, brazo o pronóstico, la submuestra deja de ser una muestra aleatoria simple. Registrar probabilidades de selección y utilizar ponderación por diseño cuando proceda.

### 41.6. Estrategias de análisis, condicionadas al mecanismo

No hay una corrección universal. El plan deberá elegir método tras especificar proceso de ausencia, variables disponibles, estructura temporal y estimando:

- ITT con resultados completos solo como análisis descriptivo o bajo supuesto de observación ignorable explícito.
- Ponderación por probabilidad inversa de observación/retención cuando MAR, positividad y modelos adecuados sean defendibles.
- Imputación múltiple bajo MAR, preservando brazo, interacciones, estructura longitudinal, variables auxiliares y relaciones entre capas; no imputar T_acc como si fuera una puntuación escalar sin estructura.
- G-computation o modelos longitudinales cuando la pérdida depende de historia observada y la secuencia temporal lo permita.
- Modelos de selección o patrones-mixtura para MNAR, con parámetros de sensibilidad explícitos.
- Límites parciales para Value no observado, con rangos defendibles en su escala.
- Ponderación por probabilidad de inclusión para submuestra de validación, si las probabilidades son conocidas y hay positividad.
- Análisis de tipping point para determinar cuánto tendría que diferir el Value no observado para cambiar la conclusión.

No usar last observation carried forward como solución general; no imputar no accesible cuando falta el snapshot; no imputar Value cero por ausencia de evaluación; no eliminar unidades con datos incompletos sin mostrar el efecto sobre la población y el estimando.

### 41.7. Pérdida longitudinal y snapshots temporales

Cada snapshot T_acc,t debe tener identificador, fecha, estado de observación y ventana temporal. Si falta un snapshot intermedio, no reconstruirlo automáticamente a partir del posterior ni asumir que el estado permaneció constante.

Distinguir:
- estado transformacional observado en t;
- estado no observado en t;
- estado conocido por evidencia indirecta;
- estado indeterminado;
- transición real entre snapshots respaldada por evento.

La pérdida de snapshot puede impedir establecer cuándo cambió accesibilidad y si precedió a trayectoria, ejecución u Outcome. En ese caso, la secuencia temporal puede quedar no identificada aunque se observe un resultado final.

Para Reach y trayectorias, ausencia de snapshots intermedios puede producir un conjunto de caminos posibles. El analizador debe devolver rutas confirmadas, rutas descartadas y rutas indeterminadas, sin colapsar incertidumbre en una trayectoria retrospectiva única.

### 41.8. Matriz adversarial de ausencia y selección

| ID | Escenario | Resultado esperado |
|---|---|---|
| MISS-01 | Ausencia MCAR baja | Métodos completos/ponderados calibrados dentro de tolerancias |
| MISS-02 | MAR por covariables basales observadas | Recuperación bajo modelo correcto y positividad |
| MISS-03 | MAR por historia post-asignación observada | Método longitudinal que respete orden temporal |
| MISS-04 | MNAR dependiente de Value no observado | Análisis de sensibilidad/límites; no afirmar identificación puntual automática |
| MISS-05 | Pérdida diferencial por brazo | Informar efecto de Z sobre retención y sesgo potencial |
| MISS-06 | Pérdida ligada a accesibilidad | No condicionar ingenuamente en observación; modelar selección |
| MISS-07 | Value falta más en unidades con Outcome desfavorable | Sensibilidad MNAR y tipping point |
| MISS-08 | Snapshot T_acc intermedio ausente | Temporalidad/Reach indeterminados donde corresponda |
| MISS-09 | Solo se observan ejecutores de τ2 | Rechazar análisis causal restringido a ejecutores |
| MISS-10 | Validación seleccionada por A_obs sin diseño conocido | Error de medición no identificado por validación |
| MISS-11 | Abandono después de evento adverso | No asumir MAR sin variables que capturen el evento |
| MISS-12 | Value no definido frente a Value no medido | Separar definición del constructo y falta de observación |
| MISS-13 | Pérdida por clúster/unidad organizativa | Ajustar unidad de análisis y dependencia |
| MISS-14 | Retención casi nula en algún estrato | Positividad fallida; restringir objetivo o reportar no-identificación |
| MISS-15 | Ausencia diferencial de documentación de U/R/C | Auditar sesgo de reconstrucción TGCV por dimensión |

### 41.9. Requisitos de registro y análisis

El diccionario de datos incorporará para cada bloque:
- valor observado y estado de ausencia;
- motivo y momento de ausencia;
- última fecha de observación;
- fuente y responsable;
- si la ausencia ocurrió antes o después de Z, instalación, selección, ejecución y Outcome;
- probabilidad de retención/validación cuando el diseño la conozca;
- indicadores de recuperabilidad;
- reglas de imputación/ponderación y versiones;
- análisis primario y sensibilidad;
- impacto sobre población objetivo, soporte y estimando.

El informe mostrará flujo de unidades por brazo, pérdidas por etapa y motivo, completitud de cada bloque, diferencias entre observadas/no observadas en variables basales, retención, distribución de pesos y diagnósticos de positividad. Los pesos extremos no se truncarán sin justificarlo y mostrar sensibilidad.

### 41.10. Criterios de aceptación metodológica

La futura prueba sintética debe:
1. recuperar el ITT sin selección en ausencia completa;
2. detectar y reportar pérdidas diferenciales;
3. recuperar efectos bajo escenarios MAR correctamente especificados;
4. no prometer recuperación bajo MNAR sin supuestos/sensibilidad;
5. identificar sesgo de casos completos cuando la selección lo genere;
6. preservar la distinción entre no observado, negativo e indeterminado;
7. no reconstruir retrospectivamente snapshots ausentes;
8. detectar pérdida de positividad;
9. ponderar validación según diseño cuando corresponda;
10. distinguir estimando de población asignada, población observada y población parcialmente identificada;
11. propagar incertidumbre de imputación/ponderación al Wald y a Value;
12. mantener independientes las evaluaciones TGCV, causal y Value.

Las tolerancias, tasas máximas de pérdida, reglas de tipping point, tamaño de muestra y métodos específicos permanecen abiertos. No se fijarán retrospectivamente.

### 41.11. Dictamen

El análisis de casos completos puede destruir la comparabilidad creada por la aleatorización al seleccionar por variables post-asignación. La pérdida de Value, snapshots o validación puede afectar de forma distinta al ITT, al IV y a la reconstrucción TGCV. No basta con informar el porcentaje total de datos faltantes.

**Decisión propuesta:** mantener el ITT en población asignada como objetivo primario; registrar pérdidas por bloque y temporalidad; separar MCAR/MAR/MNAR como supuestos de análisis, no diagnósticos automáticos; añadir MISS-01…MISS-15; utilizar ponderación, imputación, sensibilidad o límites solo cuando sus supuestos sean defendibles; no excluir casos incompletos por defecto.

**Estado:** contrato de ausencia/selección propuesto, no implementado ni probado. XSYNC-138-01 y las decisiones abiertas sobre mecanismos de ausencia, métodos, tolerancias, δ/ε, Se/Sp e inferencia permanecen pendientes.



---

## 42. Auditoría integral de coherencia causal, transformacional y estadística

**Estado:** auditoría documental interna de coherencia. No es revisión externa independiente, implementación, simulación, ejecución ni aceptación. No cierra XSYNC-138-01 ni modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS, claims, C09 o cierres previos.

### 42.1. Objeto y alcance de la auditoría

Se contrasta la coherencia interna entre:
1. DAG, intervención y estimandos;
2. DGP de provisión y accesibilidad;
3. representación de ΔT_acc, Reach y trayectorias;
4. medición verdadera/observada y validación;
5. inferencia IV/Wald y heterogeneidad;
6. ausencia de datos, selección y población objetivo;
7. reglas de Value y criterios de aceptación.

La auditoría distingue coherencia matemática bajo un DGP estipulado, identificación causal bajo supuestos, recuperación estadística y validez de medición TGCV. Ninguna de estas capas sustituye a las demás.

### 42.2. Hallazgo INT-42-01 — estimandos que no deben confundirse

En el escenario homogéneo ilustrativo:
- primera etapa verdadera: ITT_A = 0.80 − 0.20 = 0.60;
- efecto de asignación/política sobre Value: ITT_V = 3.60;
- cociente Wald: ITT_V / ITT_A = 6.00.

El 3.60 es el contraste de Value inducido por las dos políticas en el DGP especificado. El 6.00 es el efecto focal por unidad de accesibilidad bajo los supuestos IV y homogeneidad del ejemplo; con heterogeneidad, el Wald identifica un LATE ponderado de compliers, no automáticamente el ATE ni el efecto medio poblacional.

La notación debe mantener separados:
- ITT_Z: efecto de asignación de la política;
- ψ_B(q*): contraste entre políticas implementables de provisión;
- LATE_f: efecto local de accesibilidad focal entre compliers;
- θ_A(q): estimando general de C10-D1 sobre el cambio de accesibilidad/espacio definido en ese protocolo.

No llamar θ_Af al Wald y a ψ_B indistintamente. La relación entre estos parámetros depende del DGP y de los supuestos de identificación. El efecto focal sobre τ2 no valida el efecto general de ΔT_acc.

### 42.3. Hallazgo INT-42-02 — población, ITT y Value faltante

La población asignada define el objetivo ITT, pero no garantiza identificación puntual cuando Value no se observa. Deben distinguirse:
- definición del estimando en toda la población asignada;
- estimación con Value observado;
- identificación bajo supuestos de ausencia;
- conjunto de valores compatible/límites cuando no hay identificación puntual.

El análisis de casos completos no se convierte en ITT por conservar la etiqueta. Si R_V depende de Z, A, pronóstico o Value no observado, la comparación observada puede estar seleccionada. Ponderación, imputación o g-computation solo proceden bajo sus supuestos específicos y positividad. Para MNAR deben presentarse sensibilidad, modelos explícitos o límites. Si Value no está definido ontológicamente para ciertas unidades, no tratarlo como un dato faltante: redefinir población o estimando.

### 42.4. Hallazgo INT-42-03 — régimen común q* y temporalidad

q* no puede ser una distribución marginal abstracta ni un ajuste estadístico posterior. Debe especificar:
- población objetivo y covariables basales X;
- historia relevante y orden temporal;
- variables constitutivas C_c que no se pueden fijar en estados incompatibles;
- régimen común efectivamente implementable para las variables post-asignación incluidas;
- soporte y factibilidad de ambos brazos en cada historia objetivo;
- regla de Value, beneficiario y horizonte.

Si L_m es posterior a Z, su distribución común debe proceder de una intervención/regla definida en el diseño o de una estrategia de identificación justificada. No asumir que condicionar/estandarizar por L_m reproduce q*. Si L_m es afectada por Z y afecta A_f o V, el ajuste ingenuo puede introducir sesgo o cambiar el estimando.

### 42.5. Hallazgo INT-42-04 — interferencia y unidad de asignación

El contrato debe especificar ausencia de interferencia entre unidades o modelar explícitamente la interferencia. Una dependencia, licencia, servidor, equipo técnico o recurso compartido puede:
- habilitar τ2 para varias unidades;
- desplazar capacidad entre unidades;
- generar contaminación entre brazos;
- producir efectos de red o saturación.

Si existe exposición compartida, la asignación individual puede no representar el tratamiento recibido. Deben definirse unidad de asignación, unidad de análisis, conglomerados, mapa de exposición y estimando bajo interferencia. Si la hipótesis de no interferencia no es plausible, usar asignación por conglomerados o diseño de saturación cuando corresponda; no asumir independencia de unidades por conveniencia computacional.

### 42.6. Hallazgo INT-42-05 — cadena transformacional y temporal

Se mantiene la separación:
- A_f*: accesibilidad verdadera de τ2;
- A_f_obs: medición de la accesibilidad focal;
- App_f: aplicabilidad en estado/historia concretos;
- selección de trayectoria;
- ejecución efectiva;
- Outcome;
- Value.

A_f* no sustituye ΔT_acc completo. Deben preservarse U, R y C, sus versiones y snapshots. Reach y trayectorias candidatas se derivan de T_acc y condiciones en cada estado; no se reconstruyen retrospectivamente desde ejecuciones u Outcomes. La falta de snapshot produce indeterminación temporal, no un estado constante supuesto.

El DGP y el analizador deben compartir definiciones y diccionario, pero no acceso a la verdad oculta: el generador/evaluador conserva A_f* y parámetros verdaderos; el analizador recibe solo asignación, registros observables, probabilidades de diseño y reglas de medición autorizadas.

### 42.7. Hallazgo INT-42-06 — medición e inferencia IV

La relación ITT_Aobs = (Se + Sp − 1) ITT_A* solo se aplica bajo error de clasificación no diferencial entre brazos, sensibilidad/especificidad constantes y condiciones de medición compatibles con el modelo. No es una corrección universal. Si Se/Sp difieren por brazo, versión, historia o tiempo, la primera etapa observada puede atenuarse, invertirse o aparecer espuriamente.

La validación requiere referencia independiente suficientemente fiable, selección conocida y propagación de incertidumbre. Si la referencia también es imperfecta, no denominarla gold standard sin justificación.

Para inferencia IV:
- reportar primera etapa, forma reducida y Wald por separado;
- no usar solo errores estándar delta/convencionales si el instrumento puede ser débil;
- considerar inversión Anderson–Rubin u otro procedimiento robusto a instrumentos débiles;
- permitir conjuntos de confianza no acotados o disjuntos;
- evaluar cobertura y error Monte Carlo en simulación;
- mantener separados error de medición, debilidad instrumental y violación de exclusión.

### 42.8. Matriz integrada de coherencia

| Capa | Condición de coherencia | Estado documental |
|---|---|---|
| DAG/estimandos | ITT, política, LATE y θ_A general separados | Parcial; requiere armonización final de notación |
| DGP/provisión | Z→B→instalación verificada→A_f* | Propuesto; estado basal y éxito operativo aún abiertos |
| Exclusión/monotonicidad | Sin vías directas; monotonicidad explicitada como supuesto | Estipulado en DGP aislado, no validado empíricamente |
| ΔT_acc/Reach | Focal τ2 no sustituye espacio completo | Regla definida; implementación no probada |
| q*/soporte | Régimen común implementable y factible por historia | Abierto |
| Medición | A_f* separado de A_f_obs y T_acc multidimensional | Propuesto; Se/Sp y validación abiertos |
| Inferencia | Wald/LATE local y robustez a instrumento débil | Métodos propuestos; no ejecutados |
| Ausencia/selección | Estimando poblacional separado de estimación observada | Propuesto; mecanismos y métodos pendientes |
| Interferencia | Unidad y exposición compartida especificadas | Brecha contractual por resolver |
| Value | Regla estable, independiente y comparable entre brazos | Requiere verificación final de invariancia y datos faltantes |
| Aceptación | Recuperación sintética + auditoría + límites declarados | Criterios aún no ejecutados |

### 42.9. Decisiones requeridas antes de implementar

1. Congelar un diccionario único de variables, símbolos, tiempos y estimandos.
2. Definir formalmente población objetivo, unidad de asignación/análisis y tratamiento de interferencia.
3. Especificar q* como régimen intervenible, con historia y soporte.
4. Cerrar el estado basal de C_dep y distinguir intento, instalación, operación y verificación.
5. Precisar si la calidad/versiones de τ2 son invariantes en el DGP aislado.
6. Separar ψ_B, ITT_Z, LATE_f y θ_A general en todas las ecuaciones, tablas y reportes.
7. Definir Value para la población objetivo y la estrategia ante Value no observado/no definido.
8. Cerrar protocolo de referencia de medición, submuestra y error diferencial.
9. Preespecificar inferencia robusta a instrumento débil y sensibilidad a exclusión/monotonicidad.
10. Resolver las tolerancias, δ/ε y criterios de aceptación antes de observar resultados.
11. Realizar revisión cruzada independiente de C10-S frente a C10-D1 y revisión externa del contrato.
12. Solo después implementar el generador y ejecutar las pruebas autorizadas.

### 42.10. Dictamen integrado

La arquitectura de C10-S es conceptualmente articulable, pero todavía no constituye un contrato ejecutable sin ambigüedad. Los principales bloqueos no son la falta de más escenarios, sino la armonización de estimandos, la intervención q*, la unidad de interferencia, el estado basal de la dependencia, la definición de Value y la identificación bajo ausencia/medición imperfecta.

La evidencia sintética futura deberá demostrar recuperación de verdades programadas y detección de violaciones; no demostrará que los supuestos IV se cumplen en un sistema real. El resultado admisible podrá ser recuperación, identificación parcial, no-identificación o fallo del procedimiento.

**Decisión:** no congelar S4-R, no iniciar simulación ni declarar cierre de XSYNC-138-01. La sección 42 consolida hallazgos y brechas para una revisión independiente posterior. No se modifica C10-D1 ni ningún artefacto de gobernanza superior.
