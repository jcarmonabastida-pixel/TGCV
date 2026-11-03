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
