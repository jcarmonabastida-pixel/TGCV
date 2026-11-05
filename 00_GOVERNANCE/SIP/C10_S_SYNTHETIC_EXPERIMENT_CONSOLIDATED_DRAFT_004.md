# C10-S — Experimento sintético de validación transformacional y causal
**Consolidación documental integral — borrador 004 (notación revisada)**

**Estado:** DRAFT / PROPUESTA METODOLÓGICA — NO APROBADA / NO IMPLEMENTADA / NO EJECUTADA  
**Ámbito:** C10 — contribución causal de los cambios en transformaciones accesibles a Value  
**Relación:** Documento complementario a `C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`  
**Naturaleza:** consolidación normalizada del desarrollo C10-S hasta la sección 164, con recuperación e integración documental de las secciones conversacionales 165–183 en §§52–53. No es una transcripción literal íntegra de las conversaciones ni de la fuente DOCX.  
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

**Nota de precedencia incorporada en la auditoría integral:** la parametrización preliminar `W_g ~ Bernoulli(p_g)` no debe leerse como cadena generativa final. `p_g` se refiere al estado final verificado, no al intento; la cadena separada `W_attempt → S_install → C_dep` de §31.4 y el D1/D2 del capítulo 53 gobiernan la especificación candidata.

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


---

## 43. Diccionario canónico de variables y estimandos para S4-R (sección conversacional 156)

**Estado:** propuesta de armonización interna específica de C10-S/S4-R. No modifica definiciones generales de C10-D1 ni el Core TGCV. No es implementación, simulación, auditoría independiente ni aceptación. No cierra XSYNC-138-01.

### 43.1. Principio de separación

La asignación a una política, su provisión efectiva, la accesibilidad resultante y el cambio completo del espacio transformacional son variables distintas. Cadena propuesta:

`Z → B → W → C_dep → A_f* → ΔT_acc → {Reach_H, Π_H} → selección → Exec → O → V`

La cadena es una hipótesis estructural del DGP, no una afirmación de que todas las flechas estén identificadas.

### 43.2. Diccionario de variables

| Símbolo | Definición operacional en S4-R | Naturaleza / observación |
|---|---|---|
| X | Covariables basales del sistema/unidad | Basales |
| H₀ | Historia basal relevante anterior a Z | Basal, temporalmente ordenada |
| Z | Asignación aleatoria a política de provisión | Instrumento/encouragement asignado |
| B | Política o versión de provisión realmente recibida | Registrar versión y cumplimiento |
| W | Intento de instalación/provisión | Evento posterior a B |
| C_install | Dependencia instalada correctamente | Componente técnico |
| C_integrity | Dependencia íntegra y no alterada | Componente técnico |
| C_compat | Dependencia compatible con sistema/entorno | Componente técnico |
| C_oper | Dependencia operativa en condiciones de uso | Componente técnico |
| C_dep | Conjunción verificada de los cuatro componentes | Estado técnico; no equivale por sí solo a accesibilidad |
| A_f,t* | Indicador verdadero de accesibilidad de τ2 en tiempo t | Estado focal verdadero |
| D_f | Apertura focal: 1 si A_f,post*=1 y A_f,base*=0 | Tratamiento endógeno binario focal para IV |
| A_f,obs | Medición observada de A_f* / D_f | Sujeta a error de clasificación |
| T_acc,t | Espacio accesible en t: U_acc,t, R_acc,t, C_acc,t | Objeto TGCV multidimensional |
| ΔT_acc | Diferencia estructurada entre snapshots: ΔU, ΔR, ΔC | Cambio completo; no se reduce a D_f |
| App_f,t | Aplicabilidad de τ2 en estado e historia t | No equivale a accesibilidad |
| Reach_H | Estados alcanzables dentro de H bajo T_acc y condiciones | Derivado del espacio transformacional |
| Π_H^cand | Trayectorias candidatas válidas | Enumeración TGCV |
| Π_H^sel | Trayectoria seleccionada | Decisión posterior |
| Π_H^exec / Exec | Trayectoria/transformaciones ejecutadas | Evento, no medida de accesibilidad |
| M | Mecanismos intermedios definidos por DGP | Desglosar; no usar como caja negra |
| O | Outcome definido antes del análisis | Resultado con indicador de ausencia |
| V | Value según beneficiario, regla, horizonte y dimensiones preespecificados | Evaluación independiente de O y T_acc |
| R_j | Indicador de observación del bloque j | Un indicador por bloque; sección 41 |

### 43.3. Apertura focal D_f

`D_f = I(A_{f,post}*=1 ∧ A_{f,base}*=0)`

D_f indica que τ2 pasó de no accesible a accesible. Si el DGP impone A_f,base*=0 para todas las unidades, D_f coincide con A_f,post*. Si no, deben conservarse las unidades con accesibilidad basal, estratificar o definir otro contraste antes del análisis.

La proyección h_f(ΔT_acc)=D_f solo representa la apertura focal bajo el diccionario, snapshots y equivalencia fijados. No conserva por sí sola cambios en otras transformaciones, relaciones o condiciones. Por tanto:
- D_f no es ΔT_acc;
- D_f=1 no implica necesariamente ΔReach_H>0;
- ΔT_acc≠0 no implica D_f=1;
- D_f=1 no implica selección ni ejecución de τ2;
- ejecución de τ2 no debe reconstruir D_f retrospectivamente.

### 43.4. Estimandos que deben reportarse por separado

**A. Efecto de asignación (ITT primario)**

`ITT_Z = E[V | Z=1] - E[V | Z=0]`

Bajo asignación aleatoria, consistencia y ausencia de interferencia (o diseño que la modele), es el efecto causal de asignar la política. Con Value faltante, su identificación estadística depende además del mecanismo de ausencia y de la estrategia correspondiente. No es automáticamente el efecto de recibir B ni el efecto de D_f.

**B. Primera etapa focal**

`ITT_D = E[D_f | Z=1] - E[D_f | Z=0]`

Mide cuánto cambia la probabilidad de apertura focal por asignación. Debe acompañarse de incertidumbre, distribución por estratos/historia y diagnóstico de soporte. No basta con reportar que la instalación se intentó.

**C. Efecto instrumental focal**

`LATE_f = ITT_Z / ITT_D`

La razón Wald puede interpretarse como efecto causal local de D_f entre compliers solo bajo instrumento relevante, asignación independiente, exclusión, monotonicidad, consistencia/versiones bien definidas, ausencia de interferencia y tratamiento binario bien especificado. Si ITT_D es débil, el cociente puede ser inestable y requiere inferencia robusta a instrumentos débiles. Con heterogeneidad, no es ATE.

**D. Efecto de política recibida**

Un contraste causal entre versiones de B recibidas no se identifica por el mero hecho de que Z se aleatorice si existe incumplimiento. Debe definirse como estimando propio y justificar el diseño/análisis. No etiquetar ITT_Z como efecto de B cuando Z solo asigna una oferta o encouragement.

**E. Efecto focal poblacional θ_Af(q*)**

Representa el contraste contrafactual de Value bajo políticas de accesibilidad focal definidas dentro de un régimen común q*. No queda identificado automáticamente por el IV: el IV aporta LATE_f bajo sus supuestos, mientras θ_Af poblacional requiere homogeneidad, extrapolación justificada u otro diseño/estimador identificador.

**F. Efecto general de accesibilidad TGCV**

El estimando general sobre cambios en T_acc del protocolo C10-D1 no puede sustituirse por D_f ni por LATE_f. S4-R manipula una transformación focal τ2 y solo puede informar sobre ese mecanismo acotado, salvo que el diseño y la medición cubran el espacio completo y permitan otra identificación.

### 43.5. Separación de información entre generador y analizador

El generador/evaluador conserva valores verdaderos y parámetros del DGP, incluidos A_f*, D_f, T_acc verdadero y estados potenciales. El analizador recibe únicamente:
- asignación Z y probabilidades de asignación;
- versiones y registros observables de B, W y verificación técnica;
- mediciones A_f,obs y snapshots observados con su calidad;
- información de diseño necesaria para los estimandos;
- Reach, trayectorias, ejecución, Outcome y Value solo cuando estén observados;
- indicadores, motivos y tiempos de ausencia.

No recibe A_f*, D_f verdadero, estados potenciales contrafactuales ni parámetros estructurales del generador. La validación de accesibilidad se entrega solo en la submuestra y bajo el mecanismo de selección preespecificado.

### 43.6. Reporte mínimo obligatorio

Cada escenario debe informar por separado:
1. ITT_Z sobre Value y su incertidumbre;
2. ITT_D y fuerza de primera etapa;
3. forma reducida y estimación IV/LATE_f, si procede;
4. supuestos IV evaluados, no evaluables y violados en el DGP;
5. D_f y ΔT_acc como objetos distintos;
6. cambios en Reach_H y Π_H^cand;
7. selección y ejecución, sin condicionar ingenuamente el ITT;
8. pérdidas por bloque y método/limitación de identificación;
9. evaluación independiente de Value;
10. alcance: focal τ2 frente al espacio general TGCV.

### 43.7. Decisiones todavía abiertas

- Si la población primaria impondrá A_f,base*=0 o incluirá unidades con accesibilidad basal.
- Definición final de las versiones de B y del cumplimiento.
- Correspondencia exacta entre C_dep y condiciones constitutivas de realizabilidad de τ2.
- Regla de equivalencia/versiones de τ2.
- q*, soporte por historia y tratamiento de L_m.
- Unidad de asignación y posible interferencia.
- Identificación de θ_Af poblacional más allá del LATE.
- Definición completa de Value y estrategia para ausencia.
- Concordancia final de símbolos con C10-D1 §17.6 y ecuaciones previas del documento.

**Dictamen:** este diccionario separa los objetos que S4-R debe medir y estimar, pero no cierra las decisiones de q*, interferencia ni identificación poblacional. Se propone como base de armonización, no como freeze. No implementar ni simular hasta resolver los puntos abiertos y completar revisión independiente.


---

## 44. Definición operativa del régimen común q* para S4-R (sección conversacional 157)

**Estado:** propuesta metodológica para el S4-R primario. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 44.1. Decisión estructural

Se distinguen dos objetos:
- **q_X***: distribución objetivo común de características e historia basales anteriores a la asignación.
- **q_L***: régimen dinámico común sobre variables posteriores a la asignación, definido mediante una intervención secuencial implementable.

Para el S4-R primario se propone q_X* y retirar L_m post-asignación del DGP aislado si no es indispensable para representar el mecanismo focal. Los escenarios con L_m inducido por Z se mantienen como variantes adversariales, no como parte del DGP primario limpio.

q_X* no es una intervención que fuerce covariables basales. Es la distribución de la población objetivo sobre la que se comparan las políticas. La aleatorización equilibra los brazos en expectativa; explicitar q_X* fija el referente poblacional común.

### 44.2. Definición de q_X*

Sea X el vector basal, H₀ la historia anterior a la asignación y C_c las condiciones constitutivas basales relevantes:

`q_X^* = P^*(X,H_0,C_c)`

P* es la distribución de la población objetivo preespecificada, restringida al soporte donde la comparación es coherente y ambas políticas son factibles. La restricción no puede eliminar unidades después de observar Z, A, ejecución, O o V.

C_c no debe confundirse con C_dep posterior a la provisión. C_c describe el dominio y condiciones basales necesarias para que el contraste tenga sentido; C_dep pertenece a la cadena de provisión que puede cambiar tras Z.

Si se impone A_f,base*=0, esa restricción se define antes de generar resultados como característica de la población objetivo; no se aplica retrospectivamente.

### 44.3. Estimandos bajo q_X*

El contraste de política estandarizado se expresa:

`ψ_B(q_X^*) = E_{(X,H₀,C_c)~q_X^*}[E(V^{B_1}|X,H₀,C_c)-E(V^{B_0}|X,H₀,C_c)]`

Representa versiones implementables de B₁ y B₀ en la misma población objetivo. No es un efecto puro de accesibilidad. Si Z aleatoriza una oferta y existe incumplimiento, ITT_Z sigue siendo el contraste primario por asignación; ψ_B requiere consistencia de versiones y estrategia de identificación propia.

`ITT_Z(q_X^*) = E_{q_X^*}[V(1)-V(0)]`

La igualdad ITT_Z=ψ_B no se presume: requiere implementación completa o condiciones que hagan coincidir asignación y política recibida. Con Value faltante, la definición del ITT no garantiza su identificación estadística puntual.

### 44.4. DGP primario simplificado: retirar L_m

Para aislar la ruta focal, el DGP primario no incluirá una variable post-asignación L_m que afecte simultáneamente accesibilidad y Value, salvo que se justifique su indispensabilidad. Especificación ilustrativa:

`D_f = I(C_dep=1 ∧ C_{auth,base}=1 ∧ C_{resource}=1 ∧ C_{capacity}=1 ∧ C_{info}=1 ∧ C_{domain}=1)`

`M = 1 + D_f + 0.5X + ε_M`

`O = 2M + ε_O`

`V = 3O + ε_V`

Con errores de media cero y distribución común entre brazos, el efecto estructural homogéneo de D_f sobre V es 6. Si P(D_f=1|B₁)=0.80 y P(D_f=1|B₀)=0.20, el contraste esperado de Value entre políticas es 3.60. Son valores analíticos ilustrativos, no evidencia ni estimaciones empíricas.

La simplificación no afirma que sistemas reales carezcan de confusión post-tratamiento; evita introducirla en el escenario primario diseñado para comprobar recuperación bajo una ruta causal aislada conocida.

### 44.5. Cuándo conservar q_L*

Si L_m posterior a Z es indispensable, no se elimina por conveniencia. Se define q_L* como política secuencial:

`q_L^*: P(L_t | X,H₀,ar L_{t-1},ar B_{t-1},ar A_{t-1})`

Debe especificar momento de intervención, historia condicionante, mecanismo operativo común a ambos brazos, soporte/factibilidad por historia, efectos de L_t y estrategia de identificación. Una distribución marginal común de L no basta: puede ocultar historias incompatibles y no equivale a una intervención coherente. Ajustar estadísticamente por L tampoco sustituye q_L*.

### 44.6. Soporte y factibilidad

Antes de aceptar q_X* o q_L* se debe comprobar:
1. probabilidad positiva de ambas políticas en cada estrato/historia objetivo;
2. factibilidad física y técnica de la apertura focal en la población definida;
3. ausencia de selección de estratos mediante variables posteriores a Z;
4. distinción entre condiciones constitutivas y consecuencias de provisión;
5. tratamiento explícito de estratos sin soporte, sin extrapolación silenciosa.

La factibilidad de B₀ y B₁ no implica que ambos estados de D_f sean posibles para cada unidad; esa distinción afecta la interpretación de compliers.

### 44.7. Matriz de decisión

| Elemento | S4-R primario | Variantes adversariales |
|---|---|---|
| q_X* | Distribución basal común | Puede incorporar heterogeneidad |
| L_m post-asignación | Excluida si no es indispensable | Incluida para estudiar confusión inducida |
| q_L* | No requerido | Requerido si se interviene sobre L_m |
| Ajuste por L_m | No aplica | No sustituye intervención |
| Soporte | Verificado antes de generar | Puede manipularse para probar no-identificación |
| Interpretación | Ruta focal aislada bajo DGP estipulado | Efecto conjunto/condicional según régimen |

### 44.8. Decisión propuesta y cuestiones abiertas

**Decisión propuesta:** adoptar q_X* como referente común del S4-R primario y retirar L_m post-asignación de su DGP aislado. Mantener escenarios separados con L_m para probar confusión post-tratamiento y la necesidad de métodos longitudinales.

Continúan abiertas: distribución P* y población objetivo; accesibilidad basal A_f,base*; definición/medición de C_c; soporte por estrato; unidad de asignación e interferencia; regla de Value y pérdidas; y si las variantes con L_m requieren q_L* explícito o se limitan a demostrar no-identificación sin intervención adecuada.

**Dictamen:** q_X* queda definido conceptualmente como distribución basal común; q_L* es un objeto distinto reservado a intervenciones dinámicas. La simplificación mejora la atribución focal bajo el DGP estipulado, pero no demuestra que los supuestos se cumplan en sistemas reales. No congelar S4-R, implementar ni simular hasta cerrar las decisiones abiertas y obtener revisión independiente.


---

## 45. Unidad experimental, unidad de asignación e interferencia en S4-R (sección conversacional 158)

**Estado:** propuesta de especificación de diseño para C10-S/S4-R. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 45.1. Tres unidades diferenciadas

Se definen por separado:

1. **Unidad experimental (UE):** sistema generativo autónomo para el que se definen accesibilidad, trayectorias, Outcome y Value potenciales.
2. **Unidad de asignación (UA):** unidad a la que se asigna Z y, por tanto, la política de provisión.
3. **Unidad de observación (UO):** nivel al que se registran variables, snapshots y resultados; puede incluir medidas anidadas dentro de la UE.

La configuración primaria propuesta es UE=UA, con UO anidadas en UE cuando sea necesario. Esta coincidencia solo es admisible si la provisión, dependencia, recursos y resultados de una unidad no afectan a otras unidades del experimento. No se presume por definición.

### 45.2. Fuentes potenciales de interferencia

En S4-R, la dependencia técnica puede generar exposición compartida mediante:
- instalación, licencia o paquete reutilizado;
- servidor, entorno de ejecución o infraestructura común;
- equipo técnico, capacidad de instalación o soporte compartido;
- transferencia de configuraciones o conocimiento entre unidades;
- competencia por recursos que altera tiempos o calidad de provisión;
- propagación de fallos, incompatibilidades o actualizaciones.

La interferencia puede ser positiva (una provisión habilita otra unidad) o negativa (una provisión desplaza capacidad o introduce fallos). También puede alterar A_f*, ejecución, Outcome o Value sin cambiar la asignación individual.

### 45.3. Hipótesis primaria de no interferencia

Para el S4-R sintético aislado se propone generar unidades independientes, cada una con:
- dependencia, instalación y entorno técnico propios;
- recursos y capacidad no compartidos;
- ausencia de transferencia entre unidades;
- asignación y provisión sin efectos sobre otras unidades;
- generación independiente de errores, salvo factores basales explícitamente modelados.

Bajo esta estipulación, los resultados potenciales de la unidad i dependen de su propia asignación:

`Y_i(z_i,mathbf z_{-i}) = Y_i(z_i)`

La hipótesis debe verificarse como invariante del generador y someterse a pruebas adversariales; no es evidencia de que sistemas reales carezcan de interferencia. La independencia estadística de los errores tampoco sustituye a la ausencia causal de interferencia.

### 45.4. Cuando UE y UA no coinciden

Si la dependencia o los recursos se comparten, la asignación individual puede contaminarse. Se contemplan tres diseños alternativos:

**A. Aleatorización por conglomerados.** La UA es el conglomerado que comparte dependencia, infraestructura o capacidad. Todas las UE del conglomerado reciben la misma política. El análisis debe reconocer la correlación intraclúster y el número de conglomerados como determinante de la precisión.

**B. Diseño de saturación.** Se asigna aleatoriamente a conglomerados una proporción objetivo de unidades tratadas y después se aleatoriza dentro de conglomerado. Permite estudiar efectos directos e indirectos según exposición, si el mapa de interferencia está bien definido.

**C. Exposición de red o mapa explícito.** Se define para cada unidad una exposición G_i a las asignaciones/provisiones de otras unidades (por ejemplo, proporción de vecinos o unidades conectadas con dependencia instalada). Los resultados potenciales se expresan Y_i(z_i,G_i). El estimando debe especificar contraste propio y exposición; no se aplica el ITT individual sin modificación.

No se elegirá uno de estos diseños para el S4-R primario mientras se mantenga la estipulación de independencia entre unidades. Se conservarán como variantes adversariales y posibles extensiones a C10-P.

### 45.5. Estimandos bajo interferencia

Si hay interferencia, el resultado potencial individual se representa:

`Y_i(z_i,g_i)`

donde g_i es una exposición definida mediante un mapa de interferencia preespecificado. Deben distinguirse:
- efecto directo: cambiar z_i manteniendo fija la exposición g_i;
- efecto indirecto/spillover: cambiar g_i manteniendo z_i;
- efecto total: cambiar conjuntamente asignación propia y exposición;
- efecto de política/conglomerado: contraste entre regímenes de asignación.

Estos contrastes no son intercambiables. La forma de aleatorización debe proporcionar soporte para las exposiciones comparadas. Si el diseño no genera ese soporte, el efecto correspondiente no se identifica.

### 45.6. Invariantes del generador y pruebas adversariales

**Invariantes del S4-R primario:**
1. Cada UE tiene dependencia y entorno aislados.
2. Ninguna instalación cambia C_dep o A_f* de otra UE.
3. No se comparten recursos limitantes entre UE.
4. No hay transferencia de configuraciones, conocimiento ni efectos de red.
5. La asignación de una UE no altera provisión, trayectoria, Outcome o Value de otra.
6. Los identificadores UE, UA y UO quedan registrados y enlazados.
7. La unidad de análisis coincide con la unidad de asignación en el análisis primario si UE=UA.
8. Si existen observaciones repetidas/anidadas, se modela su dependencia y no se cuentan como UE independientes.

**Pruebas adversariales propuestas:**
- INT-01: instalación compartida habilita τ2 en unidad no asignada.
- INT-02: capacidad técnica compartida retrasa o impide instalación de otra unidad.
- INT-03: una licencia limita el número de unidades habilitadas.
- INT-04: propagación de actualización o fallo entre unidades.
- INT-05: transferencia de conocimiento cambia la accesibilidad de control.
- INT-06: exposición de red modifica selección o ejecución.
- INT-07: asignación individual aleatoria con contaminación entre brazos.
- INT-08: conglomerados con correlación intraclúster y número reducido de conglomerados.
- INT-09: mapa de exposición mal especificado.
- INT-10: unidad de observación confundida con unidad experimental, produciendo pseudorreplicación.

Cada prueba debe tener un resultado esperado de detección, clasificación de estimando y limitación de identificación. No se asignará PASS hasta implementar y ejecutar pruebas.

### 45.7. Consecuencias para tamaño muestral e inferencia

La cifra provisional N=2000 no puede interpretarse como 2000 unidades independientes si la asignación se hace por conglomerados o existen medidas anidadas. En diseños agrupados la precisión depende, entre otros factores, del número de conglomerados, tamaños, variación de tamaños y correlación intraclúster. Debe recalcularse mediante análisis de potencia o precisión coherente con el diseño finalmente elegido.

Para el S4-R aislado, N=2000 por réplica y 1000 réplicas Monte Carlo siguen siendo parámetros provisionales del plan previo, no una decisión de tamaño muestral. No se ejecuta ni se declara potencia.

### 45.8. Decisión propuesta

**S4-R primario:** estipular UE=UA y ausencia de interferencia mediante aislamiento de dependencias, recursos y entornos. La unidad de observación puede ser anidada, pero no se cuenta como unidad experimental independiente.

**Variantes adversariales:** incluir interferencia positiva, negativa, de red y por conglomerado para comprobar que el analizador no interpreta como efecto individual lo que es efecto indirecto o de política agrupada.

**C10-P:** la unidad de asignación deberá elegirse tras mapear dependencias y recursos compartidos en el sistema real; no se heredará automáticamente UE=UA.

### 45.9. Cuestiones pendientes y dictamen

Quedan pendientes:
- verificar si la unidad autónoma del modelo representa adecuadamente el sistema generativo de interés;
- decidir la granularidad de UE y UO;
- establecer cómo se mapearán recursos y dependencias compartidas en C10-P;
- definir exposición y estimandos si se detecta interferencia;
- ajustar inferencia y tamaño muestral si la asignación es agrupada;
- revisar la coherencia de esta estipulación con el contrato de C_dep y con q_X*.

**Dictamen:** la ausencia de interferencia se propone como estipulación explícita del DGP primario sintético, no como supuesto general de TGCV ni como afirmación empírica. El diseño alternativo ante interferencia queda delimitado, pero no seleccionado. No congelar S4-R, implementar ni simular hasta completar las decisiones abiertas y revisión independiente.


---

## 46. Delimitación de la población objetivo y elegibilidad basal de S4-R (sección conversacional 159)

**Estado:** propuesta de definición de población para el experimento sintético S4-R. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 46.1. Principio de delimitación

La población primaria no debe definirse únicamente por la inaccesibilidad basal de τ2. Debe incluir sistemas donde τ2 sea técnicamente realizable si se habilita la dependencia focal, pero donde esa dependencia esté ausente al inicio.

Se proponen dos condiciones simultáneas:
1. **Elegibilidad constitutiva:** se cumplen las condiciones basales no manipuladas necesarias para que τ2 pueda ser realizable.
2. **Cierre focal basal:** τ2 no es accesible en el momento basal debido a la ausencia de la condición técnica focal C_dep,0.

Así se evita incluir sistemas donde τ2 sea imposible por falta de capacidad, recursos, información, compatibilidad de dominio u otras condiciones que la intervención no modifica.

### 46.2. Regla de elegibilidad

Para cada unidad i, antes de asignar Z:

`E_i = I(C_{auth,base}=1 ∧ C_{resource}=1 ∧ C_{capacity}=1 ∧ C_{info}=1 ∧ C_{domain}=1 ∧ C_{other}=1)`

La regla es ilustrativa y debe armonizarse con el contrato completo de τ2. Cada condición tendrá definición observable, fuente, momento de medida y criterio de suficiencia preespecificado. No se admiten juicios retrospectivos basados en Outcome o Value.

La población primaria propuesta satisface:

`P^* = {i: E_i=1,; C_{dep,0}=0,; A_{f,0}^*=0}`

La ausencia basal de C_dep debe verificarse mediante el mismo protocolo técnico en todos los brazos. La accesibilidad A_f,0* se determina con evaluación independiente y ciega a asignación y resultados posteriores.

Si el DGP garantiza que C_dep,0=0 y que ninguna ruta equivalente existe, A_f,0*=0 puede derivarse del contrato. Aun así, se conserva la prueba de accesibilidad basal para detectar errores de especificación o rutas alternativas.

### 46.3. Qué se manipula y qué no

| Elemento | Rol en S4-R | Tratamiento |
|---|---|---|
| C_dep,0 | Dependencia técnica basal | Debe estar ausente en la población primaria |
| C_install / C_integrity / C_compat / C_oper | Componentes de dependencia posterior | Se verifican tras provisión |
| C_auth,base | Autorización basal no focal | Se mantiene constante y se documenta |
| C_resource | Recursos disponibles | Se mantiene constante |
| C_capacity | Capacidad técnica/operativa | Se mantiene constante |
| C_info | Información necesaria | Se mantiene constante |
| C_domain | Condición de dominio/compatibilidad del problema | Se mantiene constante |
| C_other | Otras precondiciones esenciales | Se definen antes de asignación |
| Z / B | Asignación y política de provisión | Única variación asignada del diseño primario |
| A_f* / D_f | Accesibilidad y apertura focal | Se derivan de condiciones verificadas, no se asignan directamente |

Si la autorización es realmente parte de la condición focal que se pretende modificar, no puede figurar simultáneamente como condición basal constante: deberá redefinirse el tratamiento y revisarse el estimando. El contrato actual de S4-R trata la dependencia como condición focal y mantiene la autorización como condición constitutiva basal.

### 46.4. Unidades con τ2 accesible al inicio

Las unidades con A_f,0*=1 no pertenecen a la población primaria cuyo estimando es la apertura de τ2. Se deben:
- identificar antes de aleatorizar;
- excluir del estimando primario mediante la regla basal preespecificada;
- conservar en un registro separado si se quiere estudiar mantenimiento, robustez o efectos de provisión sobre unidades ya habilitadas.

No deben mezclarse con las unidades elegibles de τ2 inicialmente inaccesible ni eliminarse después de conocer Z, cumplimiento, ejecución, Outcome o Value.

### 46.5. Casos indeterminados y errores de clasificación

La accesibilidad basal puede quedar como accesible, inaccesible o indeterminada. Los casos indeterminados no se reclasifican automáticamente como inaccesibles.

Antes de asignación:
- repetir o complementar la evaluación conforme a un protocolo ciego preestablecido;
- documentar la causa de indeterminación y calidad de evidencia;
- si persiste, excluir del estimando primario por regla previa y contabilizar su frecuencia;
- evaluar en sensibilidad cómo cambiaría la población y el estimando bajo clasificaciones alternativas.

La proporción de indeterminados es un resultado de calidad de medición, no un motivo para ocultar unidades.

### 46.6. Relación con q_X* y estimandos

La distribución objetivo pasa a ser condicional a elegibilidad basal:

`q_X^* = P^*(X,H_0,C_c mid E=1,; C_{dep,0}=0,; A_{f,0}^*=0)`

Esta definición fija el alcance del efecto: sistemas constitutivamente elegibles para τ2, inicialmente sin acceso a τ2 por ausencia de la dependencia focal.

El ITT_Z y la primera etapa ITT_D se estiman en esta población preasignación. El LATE_f, si se identifican sus supuestos, se refiere a compliers dentro de esta población, no a todos los sistemas generativos. La generalización a sistemas con otras condiciones basales requiere evidencia y un estimando de transporte explícito.

### 46.7. Pruebas de elegibilidad y robustez

Se proponen:
- POP-01: sistema elegible con C_dep,0=0 y τ2 inaccesible.
- POP-02: falta de recursos; debe quedar fuera del objetivo primario.
- POP-03: capacidad insuficiente; debe quedar fuera.
- POP-04: información insuficiente; debe quedar fuera o indeterminado según regla.
- POP-05: C_dep,0=1 y τ2 accesible; cohorte separada.
- POP-06: ruta alternativa equivalente a τ2; no clasificar como cierre focal sin revisar el contraste.
- POP-07: accesibilidad basal indeterminada; no recodificar automáticamente.
- POP-08: clasificación de elegibilidad basada en Outcome/Value; debe detectarse como violación.
- POP-09: exclusión posterior a Z por incumplimiento o resultado; debe detectarse como selección inválida.
- POP-10: diferencias de medición de elegibilidad entre brazos; debe detectarse como riesgo de sesgo.

### 46.8. Límites y decisión propuesta

**Decisión propuesta:** población primaria S4-R = sistemas que cumplen todas las condiciones constitutivas basales preespecificadas, tienen C_dep,0=0 y presentan τ2 inaccesible en una evaluación independiente anterior a la asignación.

Esta decisión acota la inferencia. No representa sistemas donde τ2 ya sea accesible, sistemas donde sea imposible por otras restricciones ni sistemas con accesibilidad basal indeterminada no resuelta.

Queda pendiente:
- definición observable y umbrales de cada condición constitutiva;
- confirmación de que la ausencia de C_dep es la única diferencia focal relevante;
- equivalencia y búsqueda de rutas alternativas;
- protocolo y fiabilidad de la evaluación basal;
- tratamiento de elegibilidad indeterminada;
- población P* concreta y su distribución;
- revisión de la coherencia con C10-D1, q_X* y el contrato de τ2.

**Dictamen:** la población queda delimitada conceptualmente y la regla evita seleccionar según variables post-asignación. La elegibilidad constitutiva y el cierre focal basal deben verificarse de forma independiente antes de randomizar. No congelar S4-R, implementar ni simular hasta cerrar las decisiones abiertas y obtener revisión independiente.


---

## 47. Contrato operativo de las condiciones constitutivas y elegibilidad (sección conversacional 160)

**Estado:** propuesta de especificación para la clasificación basal de elegibilidad S4-R. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 47.1. Estados de clasificación

Cada condición basal se clasifica en uno de cuatro estados:

| Estado | Criterio | Consecuencia |
|---|---|---|
| Cumplida | Evidencia suficiente conforme al criterio preespecificado | Puede contribuir a la elegibilidad |
| Incumplida | Evidencia suficiente de que no se satisface | La unidad no pertenece a la población primaria |
| Indeterminada | Evidencia insuficiente, contradictoria o no verificable | No se presume cumplida ni incumplida |
| No aplicable | La condición no corresponde al dominio definido | Requiere regla previa y justificación; no equivale a cumplida |

La ausencia de evidencia no prueba que la condición esté incumplida; tampoco autoriza a tratarla como cumplida. La categoría no aplicable no puede asignarse para evitar una restricción de elegibilidad.

### 47.2. Ficha mínima de cada condición

Cada condición constitutiva C_j debe disponer de una ficha versionada con:

1. **Identificador y definición operacional:** qué propiedad del sistema se evalúa, con límites explícitos.
2. **Criterio de suficiencia:** umbral, regla lógica o evidencia cualitativa admisible, definido antes de asignar Z.
3. **Fuente de evidencia:** registro, prueba técnica, inventario, inspección o medición; procedencia y fecha.
4. **Procedimiento:** pasos reproducibles, instrumentos y condiciones de evaluación.
5. **Temporalidad:** instante o ventana basal; debe preceder a Z y a cualquier provisión experimental.
6. **Evaluador y cegamiento:** rol responsable y confirmación de que desconoce asignación y resultados posteriores.
7. **Estado y justificación:** cumplida, incumplida, indeterminada o no aplicable, con razón codificada.
8. **Calidad de evidencia:** completitud, fiabilidad, actualidad y limitaciones, separadas del estado de la condición.
9. **Versión y trazabilidad:** identificador de ficha, versión del criterio, evidencia asociada y registro de cualquier reevaluación.

El estado de una condición y la calidad de la evidencia son dimensiones diferentes. Una condición puede estar clasificada como cumplida con evidencia de calidad limitada; esa limitación debe conservarse y entrar en análisis de sensibilidad.

### 47.3. Matriz inicial de condiciones de S4-R

| Condición | Definición operacional que debe concretarse | Evidencia admisible propuesta | Riesgo de clasificación |
|---|---|---|---|
| C_auth,base | Autorización basal vigente para efectuar la reconfiguración focal una vez disponible la dependencia | Registro de autorización y vigencia | Confundir autorización basal con autorización creada por B |
| C_resource | Recursos materiales y económicos necesarios, excluyendo la dependencia focal | Inventario y disponibilidad documentada | Contar como disponible un recurso comprometido o compartido |
| C_capacity | Capacidad técnica/operativa suficiente para realizar τ2 | Prueba de capacidad o acreditación verificable | Confundir capacidad nominal con capacidad efectiva |
| C_info | Información mínima necesaria para diagnosticar y ejecutar τ2 | Registros, entradas y comprobación de integridad | Información generada después de Z o por la propia provisión |
| C_domain | El sistema y problema pertenecen al dominio donde τ2 está definida | Criterios de dominio y diagnóstico basal | Definir dominio a partir del Outcome observado |
| C_other,j | Cualquier otra precondición esencial no focal | Ficha específica por condición | Incorporación retrospectiva de nuevas condiciones para explicar resultados |
| C_dep,0 | Dependencia técnica focal ausente al inicio | Inventario/versiones y prueba de entorno | Confundir ausencia de paquete con ausencia de capacidad equivalente |
| A_f,0* | τ2 no es accesible por el cierre focal basal, sin ruta equivalente | Evaluación TGCV independiente del catálogo, condiciones y alternativas | Inferir inaccesibilidad solo por no haber ejecutado τ2 |

Esta tabla no fija todavía umbrales ni acredita que las fuentes propuestas sean suficientes. Cada fila requiere una ficha operacional completa antes de congelar el protocolo.

### 47.4. Regla de agregación de elegibilidad

La regla provisional es conjuntiva:

`E_i = I( C_{auth,base}=1 land C_{resource}=1 land C_{capacity}=1 land C_{info}=1 land C_{domain}=1 land igwedge_j C_{other,j}=1 )`

La unidad se considera elegible solo si todas las condiciones constitutivas requeridas están **cumplidas**. Una condición requerida incumplida implica E_i=0. Una condición requerida indeterminada impide confirmar E_i; no se convierte automáticamente en E_i=0 ni en E_i=1. Una condición no aplicable solo se excluye de la conjunción si la regla de aplicabilidad estaba definida antes de evaluar la unidad y su justificación es auditable.

La población primaria sigue requiriendo, además, C_dep,0=0 y A_f,0*=0. La clasificación de elegibilidad y la evaluación de accesibilidad basal son procesos distintos, aunque ambos preceden a Z.

### 47.5. Protocolo de evaluación y adjudicación

1. Congelar versiones de fichas, criterios y catálogo antes de generar o asignar unidades.
2. Evaluar todas las condiciones con el mismo protocolo y ventana temporal.
3. Mantener a los evaluadores ciegos a Z, provisión, ejecución, Outcome y Value.
4. Registrar evidencia original, estado, justificación y calidad; no sobrescribir registros.
5. En discrepancias, aplicar adjudicación independiente según regla preestablecida; conservar las clasificaciones originales.
6. En indeterminación, aplicar solo las pruebas complementarias predefinidas. Si persiste, registrar como indeterminada.
7. Resolver la elegibilidad y la pertenencia a P* antes de aleatorizar.
8. Publicar el diagrama de unidades evaluadas, elegibles, no elegibles e indeterminadas, con motivos.
9. Repetir la clasificación solo ante nueva evidencia basal válida y bajo procedimiento documentado, nunca por conocer resultados posteriores.

### 47.6. Cegamiento, fiabilidad y desacuerdo

Se propone doble evaluación independiente para condiciones con juicio técnico o cualitativo. Para cada condición se informará:
- acuerdo bruto;
- matriz de desacuerdos entre categorías;
- medida de concordancia apropiada al tipo de escala y prevalencia;
- porcentaje de indeterminados;
- frecuencia y motivos de adjudicación.

No se impondrá automáticamente kappa como único indicador: su interpretación depende de prevalencia y distribución marginal. En condiciones técnicas objetivas se priorizará reproducibilidad de medición, calibración y concordancia con la prueba de referencia.

El acuerdo entre evaluadores no demuestra validez de constructo; solo informa reproducibilidad de la clasificación.

### 47.7. Pruebas adversariales

Se proponen:
- ELIG-01: todas las condiciones requeridas cumplidas; unidad elegible si también satisface cierre focal.
- ELIG-02: una condición constitutiva incumplida; unidad no elegible.
- ELIG-03: una condición requerida indeterminada; elegibilidad no confirmada.
- ELIG-04: condición no aplicable sin regla previa; clasificación rechazada.
- ELIG-05: evidencia caducada o fuera de ventana basal; estado indeterminado.
- ELIG-06: evaluador conoce Z o resultados; riesgo de cegamiento detectado.
- ELIG-07: criterio cambia entre unidades; inconsistencia de versión detectada.
- ELIG-08: autorización basal confundida con provisión experimental; contaminación de tratamiento detectada.
- ELIG-09: recursos nominales compartidos y no disponibles; C_resource no se declara cumplida.
- ELIG-10: capacidad acreditada documentalmente pero falla prueba operativa; discrepancia adjudicada.
- ELIG-11: ausencia de dependencia focal pero existe ruta técnica equivalente; A_f,0* no se declara inaccesible.
- ELIG-12: exclusión posterior a Z por incumplimiento, ejecución u Outcome; violación de población preasignación detectada.

### 47.8. Relación con errores de medición y estimando

La clasificación de elegibilidad también puede contener error. Debe distinguirse:
- error en medición de condiciones constitutivas;
- error en presencia/ausencia de C_dep,0;
- error en evaluación de accesibilidad basal A_f,0*;
- indeterminación genuina por evidencia incompleta.

La validación debe usar una referencia independiente, ciega y, cuando sea posible, una submuestra seleccionada sin sesgo. Si la selección para validación depende de características observadas, se documentará y corregirá mediante diseño o ponderación apropiada; si depende de estado no observado, se requerirá sensibilidad.

La incertidumbre de clasificación puede alterar quién pertenece a P* y, por tanto, cambiar el estimando objetivo. No basta con corregir el error de A_f observado si E_i también está mal clasificado. Deben analizarse errores conjuntos y la sensibilidad de la composición de P*.

### 47.9. Decisión propuesta y pendientes

**Decisión propuesta:** adoptar una regla conjuntiva de elegibilidad preasignación, basada en fichas operacionales versionadas, evidencia trazable, evaluación ciega y clasificación de cuatro estados. Solo las unidades con todas las condiciones constitutivas requeridas cumplidas, C_dep,0=0 y A_f,0*=0 integran la población primaria confirmada.

Continúan abiertos:
- umbrales concretos y pruebas de cada condición;
- definición final de C_other,j y su control de proliferación;
- fiabilidad y validez de las fuentes de evidencia;
- protocolo de adjudicación y tamaño de muestra de validación;
- tratamiento analítico de elegibilidad indeterminada;
- error conjunto en E_i, C_dep,0 y A_f,0*;
- verificación de ausencia de rutas equivalentes;
- distribución y composición concreta de P*.

**Dictamen:** el contrato hace reproducible la lógica de clasificación, pero todavía no permite clasificar unidades reales sin completar umbrales, instrumentos y evidencias. La matriz no debe utilizarse como lista de comprobación informal ni para reclasificar unidades a posteriori. No congelar S4-R, implementar ni simular hasta completar esas especificaciones y obtener revisión independiente.


---

## 48. Operacionalización de accesibilidad basal de τ2 y exclusividad funcional (sección conversacional 161)

**Estado:** propuesta de protocolo de medición basal y análisis de rutas alternativas para S4-R. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 48.1. Dos objetos distintos

Se separan:

- **Disponibilidad de la dependencia focal:** C_dep,0 indica si la dependencia técnica específica está instalada, íntegra, compatible y operativa en el estado basal.
- **Accesibilidad de la transformación focal:** A_f,0* indica si la transformación τ2, con identidad, mecanismo y condiciones definidos en el catálogo, es realizable desde el estado basal.

C_dep,0=0 no implica por sí solo A_f,0*=0. Puede haber una instalación alternativa de la misma dependencia, una dependencia distinta o una composición de transformaciones que permita una reconfiguración equivalente.

También se separa la accesibilidad de la identidad τ2 de la posibilidad de cumplir su función objetivo por otra vía. Una transformación alternativa no se convierte automáticamente en τ2: se registra como ruta alternativa y se evalúa su substituibilidad funcional por separado.

### 48.2. Definiciones operacionales

Se proponen tres variables:

1. **D_f,0:** disponibilidad basal de la dependencia focal, derivada de C_install, C_integrity, C_compat y C_oper.
2. **A_f,0*:** accesibilidad basal de τ2 como transformación identificada en el catálogo TGCV.
3. **F_alt,0:** existencia de una ruta alternativa realizable que cumple la función focal predefinida de reconfiguración técnica dentro del horizonte H y bajo las condiciones basales.

D_f,0=1 requiere que todos los componentes de la dependencia estén verificados. Si alguno está indeterminado, D_f,0 no se fuerza a cero.

A_f,0* requiere evidencia de identidad, mecanismo, precondiciones, recursos, compatibilidad, admisibilidad y dependencia. La ausencia de ejecución no es evidencia de inaccesibilidad.

F_alt,0 no se define por igualdad de estado final ni por igualdad de Outcome o Value. Se evalúa por la función técnica objetivo y por criterios de substituibilidad preespecificados, preservando la identidad y el mecanismo de cada ruta.

### 48.3. Función focal y criterio de substituibilidad

Antes de inspeccionar las unidades se define la función focal F* de τ2: modificar técnicamente la configuración del sistema diagnosticado para obtener una configuración objetivo especificada, bajo restricciones de seguridad, integridad y compatibilidad.

Para cada ruta alternativa π se evalúa:

`Sub(π, F^*, G, H, C_0)`

donde G es la granularidad transformacional fijada, H el horizonte y C₀ las condiciones basales. La relación significa que π puede cumplir la función focal bajo esas condiciones. No es una equivalencia de identidad entre π y τ2, ni tiene por qué ser simétrica o transitiva.

Criterios de substituibilidad funcional propuestos:
- mismo objetivo técnico previamente especificado;
- modificación real de la configuración, no mera transferencia de responsabilidad o diagnóstico;
- cumplimiento de las restricciones de seguridad e integridad;
- factibilidad dentro de H;
- disponibilidad de recursos y precondiciones;
- evidencia de mecanismo realizable, no mera posibilidad lógica o intención.

Los umbrales técnicos concretos y la tolerancia a diferencias de calidad deben fijarse antes de evaluar unidades. No se permite definir F* a partir de Outcome o Value observado.

### 48.4. Protocolo basal de doble evaluación

**A. Auditoría de dependencia**
1. Registrar versión, origen, instalación y configuración de la dependencia.
2. Verificar instalación efectiva, integridad, compatibilidad y operación en el entorno de la unidad.
3. Comprobar licencias, permisos y restricciones técnicas que formen parte de la disponibilidad.
4. Registrar evidencia, herramienta, fecha, evaluador, resultado y estado de incertidumbre.
5. No confundir documentación de instalación con prueba de operación.

**B. Auditoría transformacional**
1. Congelar catálogo, granularidad, identidad de τ2, condiciones, relaciones y horizonte H.
2. Enumerar transformaciones accesibles respaldadas y sus precondiciones en el estado basal.
3. Enumerar composiciones y rutas factibles, incluidas vías distribuidas o mecanismos alternativos.
4. Evaluar accesibilidad y aplicabilidad por separado, reevaluando condiciones a lo largo de cada rama.
5. Comparar rutas con F* usando criterios funcionales independientes.
6. Registrar ruta, mecanismo, dependencias, evidencia, incertidumbres y decisión de substituibilidad.
7. Mantener evaluación ciega a Z, provisión, ejecución, Outcome y Value.

El análisis de rutas es completo solo respecto al universo y granularidad declarados. La inspección de un catálogo incompleto no prueba ausencia universal de alternativas.

### 48.5. Clasificación conjunta

| C_dep,0 | A_f,0* | F_alt,0 | Interpretación para S4-R |
|---|---|---|---|
| 0 | 0 | 0 | Caso basal objetivo, si elegibilidad constitutiva está cumplida y cobertura de rutas es suficiente |
| 0 | 0 | 1 | τ2 focal inaccesible, pero la función puede lograrse por otra vía; el contraste de apertura funcional no es exclusivo |
| 0 | 1 | 0/1 | Inconsistencia aparente o ruta de τ2 independiente de la dependencia declarada; investigar contrato/medición |
| 1 | 1 | 0/1 | Dependencia y τ2 ya accesibles; fuera de la población primaria de apertura |
| Indeterminado | Cualquiera | Cualquiera | No confirmar el cierre basal |
| Cualquiera | Indeterminado | Cualquiera | No confirmar inaccesibilidad |
| Cualquiera | Cualquiera | Indeterminado | No confirmar exclusividad funcional |

Una ruta alternativa funcional no significa necesariamente que τ2 esté accesible como identidad transformacional. Sí significa que la intervención puede no ser la única vía para cumplir la función focal, lo que afecta la interpretación causal y el contraste de exclusividad.

### 48.6. Regla de inclusión y consecuencias

La población primaria de apertura de τ2 requiere:
- elegibilidad constitutiva confirmada;
- D_f,0=0;
- A_f,0*=0;
- ausencia respaldada de ruta funcional alternativa F_alt,0=0, dentro del universo, granularidad, condiciones y horizonte auditados.

Si existe ruta alternativa, no se debe excluir automáticamente la unidad sin analizar el estimando. Hay dos posibilidades:
1. **Estimando de apertura de τ2 como identidad:** la unidad podría seguir siendo elegible si τ2 es realmente inaccesible, pero la alternativa se registra como mecanismo competidor y puede afectar exclusión/atribución.
2. **Estimando de apertura de la función F*:** la unidad no tiene cierre funcional basal y no pertenece a una población donde la intervención sea la única apertura de esa función.

S4-R pretende estudiar el efecto focal de τ2 y su contribución transformacional. Por ello, la ausencia de rutas funcionalmente substituibles se propone como requisito del escenario sintético aislado. En sistemas reales, si no puede demostrarse, la conclusión deberá limitarse al cambio de accesibilidad de τ2, no a la apertura exclusiva de la función.

### 48.7. Estados de evidencia y pruebas adversariales

Para D_f,0, A_f,0* y F_alt,0 se conservarán estados respaldado presente, respaldado ausente e indeterminado, además de calidad/confianza por separado. “No encontrado” solo puede clasificarse como ausencia respaldada si la cobertura del universo de búsqueda está documentada.

Pruebas propuestas:
- ACC-01: dependencia focal ausente y τ2 sin ruta; inaccesibilidad respaldada.
- ACC-02: dependencia ausente pero τ2 disponible mediante instalación equivalente; A_f,0* debe ser accesible.
- ACC-03: τ2 inaccesible pero existe ruta alternativa funcional; separar identidad de función.
- ACC-04: ruta alternativa solo alcanza mismo estado final por mecanismo distinto; no inferir equivalencia automática.
- ACC-05: ruta alternativa requiere recursos no disponibles; no clasificar como realizable.
- ACC-06: ruta requiere más pasos que H; no es funcionalmente substituible dentro del horizonte definido.
- ACC-07: ruta compuesta válida no enumerada en catálogo; fallo de cobertura.
- ACC-08: condición indeterminada en una ruta; exclusividad indeterminada.
- ACC-09: evaluación basada en no ejecución observada; inferencia inválida detectada.
- ACC-10: evaluador conoce Outcome/Value; violación de cegamiento.
- ACC-11: cambio de granularidad altera identidad/substituibilidad; sensibilidad documentada.
- ACC-12: evidencia de ausencia incompleta; no confirmar F_alt,0=0.

### 48.8. Registro y trazabilidad

El registro basal debe contener como mínimo:
- unidad y momento basal;
- versiones del catálogo, reglas de identidad y granularidad;
- D_f,0 y evidencia de cada componente;
- A_f,0* y justificación de identidad, mecanismo y condiciones;
- rutas alternativas candidatas, aceptadas, rechazadas o indeterminadas;
- función F*, H y restricciones utilizadas;
- cobertura del universo auditado y límites conocidos;
- evaluadores, cegamiento, desacuerdos y adjudicación;
- clasificación final y regla de elegibilidad aplicada.

Los snapshots son inmutables. Una reevaluación válida genera una nueva versión enlazada, sin sobrescribir el estado basal original.

### 48.9. Dictamen y decisiones abiertas

**Decisión propuesta:** mantener separadas la disponibilidad de dependencia, accesibilidad de τ2 como identidad transformacional y substituibilidad funcional. Para el S4-R sintético aislado se exige cierre basal de τ2 y ausencia de ruta funcional alternativa dentro del universo declarado. Para aplicaciones reales, la conclusión se limita por la cobertura empírica de ese universo.

Pendientes:
- fijar función focal F* y tolerancias técnicas;
- cerrar identidad/granularidad de τ2;
- determinar H y reglas de factibilidad;
- especificar cobertura y exhaustividad del catálogo/rutas;
- validar las pruebas de dependencia y accesibilidad;
- definir tratamiento de rutas alternativas y estados indeterminados;
- revisar consistencia con C10-D1, exclusión IV y población P*.

**Dictamen:** el protocolo evita inferir inaccesibilidad a partir de la mera ausencia de una dependencia o de la no ejecución. La exclusividad solo puede afirmarse respecto al universo, granularidad, condiciones y horizonte auditados; no se demuestra universalmente por una búsqueda finita. No congelar S4-R, implementar ni simular hasta completar criterios técnicos, cobertura y revisión independiente.


---

## 49. Contrato de evidencia para rutas alternativas y evaluación de exclusividad (sección conversacional 162)

**Estado:** propuesta de contrato de evidencia para evaluar rutas alternativas a τ2 en S4-R. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 49.1. Principio: realizabilidad no equivale a ejecución histórica

La accesibilidad TGCV no exige que una transformación se haya ejecutado previamente. Exige que sea realizable bajo condiciones, recursos, mecanismos y restricciones definidos. Por tanto:
- la ausencia de ejecuciones históricas no demuestra inaccesibilidad;
- una descripción documental no demuestra realizabilidad;
- una ruta imaginable o lógicamente concebible no constituye una ruta accesible;
- la prueba técnica puede respaldar realizabilidad prospectiva sin convertir la ejecución previa en requisito ontológico;
- la ejecución observada puede validar mecanismos y resultados, pero no es el único tipo de evidencia admisible de accesibilidad.

La evaluación debe referirse al sistema, estado/contexto, historia, granularidad y horizonte concretos.

### 49.2. Niveles de evidencia

Los niveles describen fuerza y tipo de respaldo, no estados ontológicos ni una escala universal automática:

| Nivel | Evidencia | Inferencia permitida | Inferencia no permitida |
|---|---|---|---|
| E1 Documental | Descripción, diseño, manual, especificación o referencia | La ruta está documentada/propuesta | Que sea realizable |
| E2 Mecanística | Mecanismos, dependencias, precondiciones, recursos y restricciones identificados | Existe una explicación concreta y contrastable de cómo podría realizarse | Que el mecanismo funcione en el entorno de la unidad |
| E3 Técnica | Prueba independiente de componentes y compatibilidad en entorno representativo; evidencia de que se satisfacen condiciones | Realizabilidad técnica respaldada bajo las condiciones probadas | Generalización a otras versiones, contextos o condiciones |
| E4 Reproducible | Repetición trazable, control de versiones/condiciones y reproducción independiente | Respaldo robusto de realizabilidad dentro del ámbito verificado | Ausencia universal de alternativas o validez fuera del ámbito probado |

Un nivel superior no compensa una incompatibilidad de contexto: una prueba E4 en un entorno distinto no demuestra realizabilidad para la unidad objetivo. Se conservarán los artefactos y condiciones que delimitan cada inferencia.

### 49.3. Ficha de evidencia por ruta

Cada ruta candidata π debe registrarse con:
- route_id, versión e identidad de sus transformaciones;
- función objetivo F* y criterio de substituibilidad aplicado;
- sistema/unidad, estado basal, contexto e historia;
- granularidad y horizonte H;
- secuencia ordenada de transformaciones, relaciones y dependencias;
- precondiciones, recursos, restricciones y condiciones de seguridad;
- evidencia E1–E4 disponible, con fuente, fecha, versión y responsable;
- método de verificación, entorno y representatividad;
- estado de accesibilidad, aplicabilidad y substituibilidad;
- incertidumbres, limitaciones y condiciones no verificadas;
- hashes/IDs de artefactos y registro de evaluación/adjudicación.

La ficha debe permitir a un tercero reconstruir por qué la ruta se considera viable, inviable o indeterminada sin conocer Outcome ni Value.

### 49.4. Tres juicios separados por ruta

Para evitar que la evidencia de una propiedad se utilice como prueba de otra, cada ruta recibe tres juicios:

1. **Accesibilidad:** ¿la secuencia es realizable para el sistema y contexto considerados?
2. **Aplicabilidad:** ¿se satisfacen las precondiciones para iniciar cada paso desde el estado/ramificación correspondiente?
3. **Substituibilidad funcional:** ¿la ruta cumple F* dentro de H y las restricciones especificadas?

Una ruta puede estar accesible pero no ser aplicable desde el estado inicial; puede ser aplicable pero no cumplir la función focal; o puede cumplir F* sin ser la misma identidad que τ2. Las tres evaluaciones se documentan separadamente.

### 49.5. Estados de conclusión

Cada juicio se clasifica como:
- **Respaldado positivo:** evidencia suficiente y contextualizada de que se cumple.
- **Respaldado negativo:** evidencia suficiente de que no se cumple bajo el ámbito definido.
- **Indeterminado:** evidencia insuficiente, contradictoria o no representativa.
- **Fuera de ámbito:** el contexto/versión no corresponde a la población o condiciones objetivo; no se interpreta como positivo ni negativo.

“Ruta no encontrada” solo puede convertirse en ausencia respaldada si se documentan el universo de búsqueda, fuentes, granularidad, reglas de identidad, horizonte, cobertura y procedimiento de búsqueda. De lo contrario, el resultado es indeterminado.

### 49.6. Evidencia para descartar una ruta

No encontrar una ruta en el catálogo no basta para descartarla. El descarte requiere demostrar al menos una condición bloqueante bajo la definición y ámbito fijados, por ejemplo:
- mecanismo necesario físicamente/operativamente imposible en el sistema;
- precondición esencial incumplida y no modificable dentro del régimen/horizonte;
- recurso imprescindible ausente y no obtenible dentro del horizonte;
- incompatibilidad técnica verificada;
- dependencia imposible de satisfacer;
- secuencia que excede H;
- violación inevitable de restricciones de seguridad/integridad;
- imposibilidad de alcanzar F* según el criterio técnico preespecificado.

La conclusión negativa se limita a la versión, contexto, estado, historia, horizonte y granularidad examinados. Si el supuesto bloqueo es incierto o puede cambiar mediante otra transformación, la ruta permanece indeterminada o debe ampliarse la búsqueda.

### 49.7. Prueba técnica independiente sin exigir ejecución histórica

Una prueba técnica E3 puede respaldar realizabilidad prospectiva mediante:
- verificación de componentes y dependencias;
- pruebas de compatibilidad e interfaces;
- comprobación de precondiciones y recursos;
- validación de mecanismo en entorno aislado/sandbox representativo;
- inspección de restricciones y fallos previsibles;
- prueba de la secuencia completa cuando la composición sea esencial.

La prueba debe evitar modificar las condiciones que definen el estimando, o documentar que lo hace. Si la ruta solo funciona tras una intervención adicional, esa intervención forma parte de la ruta y debe incluirse en la comparación.

Cuando el sandbox no representa adecuadamente el entorno objetivo, la evidencia no supera E2/E3 para ese contexto. La calificación de nivel depende de la correspondencia demostrada, no de la sofisticación del instrumento.

### 49.8. Independencia, cegamiento y adjudicación

- Los evaluadores de rutas desconocen asignación, provisión, selección, ejecución, Outcome y Value.
- La definición de F*, granularidad, H y restricciones se congela antes de evaluar alternativas.
- Cuando la clasificación implica juicio, se utilizan dos evaluadores independientes y adjudicación documentada.
- Se conservan desacuerdos, evidencia original y versiones; la adjudicación no sobrescribe juicios previos.
- El evaluador de exclusividad no utiliza como evidencia que una ruta produjo peor Value o no fue seleccionada.
- El generador conserva la verdad de las rutas del DGP; el analizador recibe evidencia y debe inferir estados. El evaluador independiente compara clasificación con verdad generadora.

El cegamiento reduce sesgos de evaluación, pero no corrige un universo de búsqueda incompleto ni demuestra validez del criterio F*.

### 49.9. Regla de exclusividad funcional

Para afirmar que τ2 es la única vía que cumple F* en el escenario sintético, se requiere:
1. universo de transformaciones y mecanismos declarado como cerrado;
2. granularidad e identidad congeladas;
3. enumeración completa de rutas hasta H;
4. evaluación de condiciones y aplicabilidad por rama;
5. examen de rutas directas, compuestas, distribuidas e indirectas incluidas en el universo;
6. evidencia suficiente para descartar rutas candidatas no viables;
7. ausencia de rutas alternativas con substituibilidad funcional respaldada;
8. ausencia de rutas relevantes indeterminadas.

Si alguna ruta potencialmente substituible permanece indeterminada, la exclusividad no recibe PASS. El resultado será INDETERMINATE, no FAIL por defecto. Si una ruta alternativa sí cumple F*, la exclusividad funcional falla para ese escenario, aunque τ2 siga siendo una transformación distinta y relevante.

En un DGP sintético cerrado, la completitud puede demostrarse respecto al universo generado mediante enumeración exhaustiva y pruebas del generador. Esto no demuestra completitud empírica en sistemas reales.

### 49.10. Pruebas adversariales

Se proponen:
- EVID-01: ruta documentada E1 sin mecanismo; no clasificar accesible.
- EVID-02: mecanismo plausible E2 sin compatibilidad contextual; no elevar a realizable.
- EVID-03: prueba E3 en entorno no representativo; marcar fuera de ámbito.
- EVID-04: prueba E3 reproducida independientemente; evaluar E4 dentro del ámbito.
- EVID-05: ruta no encontrada sin cobertura documentada; exclusividad indeterminada.
- EVID-06: bloqueo técnico verificado y esencial; descarte limitado al ámbito probado.
- EVID-07: ruta requiere recurso adicional no contemplado; ampliar ruta y revisar estimando.
- EVID-08: ruta accesible pero no aplicable desde S0; conservar distinción.
- EVID-09: ruta cumple F* mediante mecanismo distinto; τ2 no equivalente por identidad, pero funcionalmente substituible.
- EVID-10: ruta con precondición indeterminada; no confirmar exclusividad.
- EVID-11: secuencia excede H; no substituible dentro del horizonte, sin afirmar imposibilidad general.
- EVID-12: evaluador conoce Outcome/Value; invalidar evaluación por cegamiento.
- EVID-13: universo sintético declarado cerrado pero generador omite una composición; falla completitud computacional.
- EVID-14: ruta externa fuera del universo declarado; documentar límite, no inferir ausencia universal.
- EVID-15: dos evaluadores discrepan; conservar ambas clasificaciones y adjudicar según protocolo.

### 49.11. Dictamen y decisiones pendientes

**Decisión propuesta:** utilizar los niveles E1–E4 y los tres juicios separados (accesibilidad, aplicabilidad y substituibilidad) para documentar rutas alternativas. La ausencia de rutas solo se considera respaldada cuando el procedimiento de búsqueda y la cobertura del universo están especificados. La exclusividad recibe PASS únicamente dentro del universo, granularidad, contexto y horizonte declarados, sin alternativas indeterminadas.

Pendientes:
- fijar F* y criterios técnicos/umbrales;
- definir qué entornos se consideran representativos;
- cerrar granularidad, identidad y H;
- especificar el universo cerrado del DGP sintético;
- definir estándares de evidencia E3/E4 por tipo de transformación;
- establecer la regla de adjudicación y reproducibilidad;
- armonizar el contrato con C10-D1, XSYNC-138 y el protocolo de accesibilidad basal.

**Dictamen:** el contrato evita confundir documentación, plausibilidad, realizabilidad, ejecución y ausencia de búsqueda. La exclusividad puede probarse computacionalmente solo en un universo sintético cerrado; en aplicaciones reales queda limitada por cobertura y evidencia. No congelar S4-R, implementar ni simular hasta completar criterios, universo y revisión independiente.


---

## 50. Auditoría integrada de consistencia de elegibilidad, accesibilidad y exclusividad (sección conversacional 163)

**Estado:** auditoría conceptual cruzada de las secciones 46–49. Propone separar poblaciones objetivo según el objeto causal. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 50.1. Hallazgo principal: dos preguntas causales distintas

Las secciones 46–49 aproximaban dos objetivos que deben mantenerse separados:

**Objetivo I — Apertura de τ2 como transformación identificada.** Pregunta si hacer accesible la transformación focal τ2 cambia los mecanismos, trayectorias, Outcome o Value, aunque existan otras rutas que puedan cumplir una función parecida.

**Objetivo F — Apertura exclusiva de la función técnica F*.** Pregunta si la intervención abre una capacidad funcional que no podía realizarse previamente por ninguna ruta alternativa admisible dentro del universo, granularidad, condiciones y horizonte definidos.

La ausencia de alternativas funcionales es constitutiva del segundo objetivo, pero no necesariamente del primero. Convertirla en requisito de toda la población primaria seleccionaría unidades por una propiedad funcional adicional y cambiaría el alcance del estimando de apertura de τ2.

### 50.2. Dos poblaciones objetivo explícitas

Se proponen dos poblaciones, que no deben confundirse:

**P*_τ2 — Población de apertura de la identidad transformacional**

Incluye unidades que:
- cumplen las condiciones constitutivas basales;
- tienen la dependencia focal ausente y verificada (D_f,0=0);
- presentan inaccesibilidad basal respaldada de τ2 (A_f,0*=0);
- disponen de información suficiente para clasificar estas propiedades antes de Z.

La existencia de rutas funcionales alternativas no excluye automáticamente la unidad. Se registra como característica basal, posible modificador del efecto y límite de interpretación. Si su presencia cambia el régimen de intervención o abre vías afectadas por B, se revisa la identificación.

**P*_F — Población de apertura exclusiva de la función**

Incluye unidades de P*_τ2 que, además, presentan ausencia respaldada de rutas alternativas funcionalmente substituibles (F_alt,0=0) en el universo, granularidad, condiciones y horizonte congelados.

P*_F es, por construcción, un subconjunto de P*_τ2. La diferencia entre ambas poblaciones debe quedar visible en el diagrama de selección y en los resultados.

### 50.3. Tabla de decisión de elegibilidad

| Condiciones constitutivas | D_f,0 | A_f,0* | F_alt,0 | Clasificación |
|---|---|---|---|---|
| No cumplidas | Cualquiera | Cualquiera | Cualquiera | Fuera de ambas poblaciones |
| Indeterminadas | Cualquiera | Cualquiera | Cualquiera | Elegibilidad no confirmada |
| Cumplidas | 0 | 0 | 0 respaldado | P*_τ2 y P*_F |
| Cumplidas | 0 | 0 | 1 respaldado | P*_τ2; no P*_F |
| Cumplidas | 0 | 0 | Indeterminado | P*_τ2 si las demás condiciones están confirmadas; exclusividad funcional indeterminada |
| Cumplidas | 1 | 1 | Cualquiera | Fuera de la población de apertura basal |
| Cumplidas | Indeterminado | Cualquiera | Cualquiera | No confirmar pertenencia a P*_τ2 |
| Cumplidas | Cualquiera | Indeterminado | Cualquiera | No confirmar pertenencia a P*_τ2 |

La tabla presupone que la ausencia de D_f,0 y la inaccesibilidad de τ2 se han medido mediante protocolos independientes. Una discordancia —por ejemplo, dependencia focal ausente pero τ2 accesible— exige auditoría de mecanismos, catálogo y medición, no una clasificación automática.

### 50.4. Estimandos y alcance de interpretación

La población objetivo debe formar parte explícita de cada estimando:

- θ_τ2(P*_τ2,q*): contraste causal de la política que abre la accesibilidad focal de τ2, bajo el régimen común q*, en P*_τ2.
- θ_F(P*_F,q*): contraste correspondiente en la población donde la función F* carecía de ruta funcional alternativa basal.

Estos símbolos identifican objetivos conceptuales, no estimandos ya identificados. Antes de formalizarlos deben fijarse la versión de intervención, régimen q*, horizonte, Value, tratamiento de no cumplimiento y supuestos de identificación.

No se puede interpretar θ_τ2 como efecto de abrir una capacidad funcional exclusiva cuando F_alt,0=1 o indeterminado. Tampoco se puede generalizar θ_F a unidades de P*_τ2 excluidas de P*_F sin hipótesis adicionales.

La presencia de una alternativa basal no invalida por sí misma el efecto causal de hacer accesible τ2. Sí puede:
- reducir la necesidad de ejecutar τ2;
- modificar selección y ejecución;
- cambiar Reach y el conjunto de trayectorias;
- generar heterogeneidad;
- hacer que el efecto observado sea distinto del efecto de abrir una función antes imposible.

### 50.5. Implicaciones para el DAG y la exclusión IV

La ruta focal sigue siendo:

Z → B → W → C_dep → A_f* → ΔT_acc → Reach/Π → selección/ejecución → O → V.

Las rutas alternativas basales se representan como característica F_alt,0 del sistema, que puede modificar la relación entre accesibilidad, ejecución y Value. No se deben eliminar estadísticamente por defecto ni confundir con una vía directa de Z.

Se requiere distinguir tres situaciones:

1. **Alternativa basal no afectada por Z/B:** puede modificar el efecto de abrir τ2 y generar heterogeneidad, sin violar automáticamente la exclusión IV.
2. **La provisión B altera también la alternativa:** aparece una vía adicional desde Z/B; la interpretación como efecto instrumental exclusivo de A_f* queda comprometida.
3. **La alternativa se activa como respuesta a Z/B:** es un mecanismo post-asignación. No debe ajustarse ingenuamente; requiere modelización temporal y un estimando compatible.

La exclusión IV exige que Z afecte V únicamente a través del tratamiento focal instrumentado, bajo la definición de tratamiento y versiones elegida. La existencia de rutas alternativas no demuestra ni refuta por sí sola esa exclusión: importa si la asignación las modifica o si la versión de tratamiento incluye sus cambios.

### 50.6. Error de clasificación y selección de población

La clasificación errónea de F_alt,0 afecta principalmente a la separación P*_τ2/P*_F. La clasificación errónea de condiciones constitutivas, D_f,0 o A_f,0* afecta a la composición de P*_τ2 y puede sesgar ambos estimandos.

Reglas propuestas:
- realizar todas las clasificaciones antes de Z;
- mantener indeterminación explícita;
- no reclasificar con Outcome, ejecución o Value;
- conservar las unidades indeterminadas en el diagrama de flujo;
- no excluirlas silenciosamente del denominador;
- analizar sensibilidad a errores de clasificación y a diferentes reglas de pertenencia;
- si se estima efecto en P*_F, informar el procedimiento de selección y la incertidumbre de F_alt,0.

La clasificación de P*_F puede ser más exigente y menos precisa por depender de una afirmación de ausencia de alternativas. No debe ocultarse esa menor cobertura detrás de una etiqueta binaria.

### 50.7. Armonización de las secciones 46–49

Se propone la siguiente reconciliación:

- **Sección 46:** define el marco de población basal constitutivamente elegible y requiere inaccesibilidad de τ2 para el estudio de apertura focal. La ausencia de alternativas se reserva para el subobjetivo funcional.
- **Sección 47:** mantiene fichas versionadas, cuatro estados y evaluación ciega de condiciones constitutivas; no decide por sí sola la exclusividad funcional.
- **Sección 48:** conserva por separado D_f,0, A_f,0* y F_alt,0; su regla de inclusión se interpreta según P*_τ2 o P*_F.
- **Sección 49:** mantiene niveles E1–E4 y juicios separados. La regla PASS de exclusividad se aplica a P*_F, no como filtro general de P*_τ2.

Esta reconciliación corrige el alcance de la regla de inclusión propuesta en las secciones 46 y 48, sin borrar su contenido ni reescribir la trazabilidad previa.

### 50.8. Pruebas de coherencia cruzada

Se proponen:
- INT-01: alternativa funcional ausente; unidad clasificada en P*_τ2 y P*_F.
- INT-02: alternativa funcional respaldada presente; unidad permanece en P*_τ2, sale de P*_F.
- INT-03: alternativa indeterminada; P*_τ2 confirmada si sus condiciones se cumplen, P*_F no confirmada.
- INT-04: τ2 accesible basalmente; exclusión de ambas poblaciones de apertura.
- INT-05: dependencia ausente pero τ2 accesible por otra vía; activar auditoría de contrato.
- INT-06: alternativa basal no afectada por Z; permitir análisis de heterogeneidad sin declarar violación automática de exclusión.
- INT-07: B altera alternativa funcional; marcar posible violación de exclusión/versión.
- INT-08: alternativa aparece tras Z; clasificar como mecanismo post-asignación y no ajustar ingenuamente.
- INT-09: clasificación de alternativa utiliza Outcome/Value; invalidar evaluación por contaminación.
- INT-10: clasificación de P*_F cambia tras conocer asignación; violación de temporalidad.
- INT-11: error en A_f,0* cambia P*_τ2; propagar incertidumbre de población.
- INT-12: reporte combina ambos estimandos sin distinguir poblaciones; fallo de interpretación.

### 50.9. Dictamen y decisiones pendientes

**Dictamen conceptual:** las secciones 46–49 pueden reconciliarse si se distinguen dos objetivos y dos poblaciones. La ausencia de alternativas es necesaria para la afirmación de apertura funcional exclusiva, pero no debe imponerse automáticamente como criterio de elegibilidad del estudio de apertura de τ2.

Continúan pendientes:
- definición formal y operacional de θ_τ2 y θ_F;
- decisión de cuál será el objetivo primario de C10-S y su transición a C10-P;
- definición de q* y población de referencia para cada objetivo;
- protocolo de interacción/heterogeneidad por F_alt,0;
- análisis de sensibilidad a error de clasificación y selección;
- especificación de efectos de B sobre rutas alternativas;
- armonización formal con C10-D1 y revisión independiente de XSYNC.

No se declara cerrada la auditoría completa ni se congela S4-R. No se implementa ni simula. La propuesta resuelve una contradicción de alcance, pero aún debe comprobarse contra los contratos causales y el DGP antes de aceptar el diseño.


---

## 51. Contraste de objetivos causales y matriz de escenarios S4-R (sección conversacional 164)

**Estado:** propuesta de matriz DGP para contrastar apertura de τ2, apertura funcional y no cumplimiento. No modifica C10-D1 ni el Core TGCV. No es freeze, implementación, simulación, ejecución, auditoría independiente ni aceptación.

### 51.1. Objetivo primario propuesto

Se propone que C10-S tenga como objetivo causal primario el efecto de la política aleatorizada de provisión sobre Value en la población P*_τ2, y como objetivo de identificación secundario el efecto local de la accesibilidad focal de τ2 entre las unidades cuyo acceso cambia por la política, si los supuestos IV se sostienen.

La elección no debe confundirse con afirmar que el efecto de accesibilidad está ya identificado:
- **Primario de diseño:** ITT de asignación a la política de provisión (TE_Z), estimable por la aleatorización si Value se observa o su ausencia se trata con supuestos/límites explícitos.
- **Secundario causal:** efecto de accesibilidad focal (A_f*) inducido por la política; el cociente de Wald solo identifica un LATE entre compliers bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones y ausencia de interferencia, además de medición válida.
- **Subobjetivo funcional:** efecto en P*_F, donde no existen alternativas basales substituibles; análisis de alcance/heterogeneidad, no filtro automático de la población primaria.
- **No objetivo de S4-R:** estimar el efecto universal de todo ΔT_acc. El instrumento focaliza τ2 y no representa todos los cambios posibles en U_acc, R_acc y C_acc.

Esta jerarquía es una propuesta de diseño para C10-S, pendiente de armonización con C10-D1 y decisión formal.

### 51.2. Variables y secuencia común del DGP

Se conserva la separación:
- Z: asignación aleatoria a política de provisión.
- B: política/provisión efectivamente ofrecida y su versión.
- W: intento de instalación/provisión.
- C_dep: estado verificado de la dependencia focal.
- A_f*: accesibilidad verdadera de τ2 derivada de C_dep y las demás condiciones.
- ΔT_acc: cambio completo del espacio transformacional, no solo el indicador focal.
- F_alt,0: existencia basal de ruta funcional alternativa.
- F_alt,1: estado posterior de las rutas alternativas.
- Reach, Π_candidate, Π_selected, Π_executed: alcance y etapas de trayectoria, separadas.
- O, V: Outcome y Value, respectivamente.

Secuencia estructural:

Z → B → W → C_dep → A_f* → ΔT_acc → Reach/Π_candidate → Π_selected → Π_executed → O → V.

La ruta alternativa puede existir antes de la asignación (F_alt,0) y mantenerse inalterada, o cambiar tras la asignación (F_alt,1). No debe confundirse su disponibilidad con la identidad de τ2.

### 51.3. Cuatro escenarios mínimos

| Escenario | Alternativa basal | Efecto de B sobre alternativa | Apertura focal | Interpretación principal |
|---|---|---|---|---|
| S4R-A | Ausente | No aplica | Sí, con cumplimiento imperfecto permitido | Apertura de τ2 y, dentro del universo cerrado, de F* |
| S4R-B | Presente y funcional | Ninguno | Sí | Apertura de τ2 con sustitución funcional basal |
| S4R-C | Ausente o presente | B la modifica | Puede abrirse τ2 | Intervención compuesta; exclusión IV focal comprometida |
| S4R-D | Cualquiera | Ninguno | No se produce en algunas unidades | No cumplimiento/fallo de provisión; separar ITT y primera etapa |

**S4R-A — Sin alternativa basal.** La unidad pertenece a P*_F y P*_τ2. G0 carece de ruta funcional F* y G1 hace accesible τ2. La afirmación de exclusividad queda limitada al universo sintético, granularidad, condiciones y H declarados. Si todas las unidades cumplen, el efecto de política y el de accesibilidad pueden coincidir bajo consistencia; no se debe asumirlo antes de comprobar implementación.

**S4R-B — Alternativa basal no afectada.** La unidad pertenece a P*_τ2, pero no a P*_F. La alternativa está disponible en ambos brazos y no es modificada por B. El efecto de abrir τ2 puede ser menor, nulo o heterogéneo porque el sistema ya puede realizar F* por otra vía. No es por sí mismo una violación de exclusión IV. Deben conservarse por separado rutas, selección y ejecución: la existencia de alternativa no significa que τ2 se ejecute ni que ambas rutas sean equivalentes por identidad.

**S4R-C — Provisión que modifica alternativas.** B altera la accesibilidad, calidad, coste, latencia o disponibilidad de una ruta alternativa. Si Z afecta V por esa ruta además de A_f*, la exclusión del instrumento para el efecto focal queda violada. El ITT de la política continúa siendo un estimando de la asignación aleatoria, pero ya representa el paquete de cambios inducido por B. No se presentará el cociente de Wald como efecto causal exclusivo de A_f* sin una redefinición justificada del tratamiento y un diseño que identifique los componentes.

**S4R-D — No cumplimiento o fallo de provisión.** Z asigna la política, pero W puede no iniciarse, la instalación puede fallar, C_dep puede no quedar operativo o alguna condición constitutiva puede impedir A_f*. Se registra cada etapa; no se fuerza A_f*=Z. Si existe primera etapa positiva, se puede estudiar IV bajo sus supuestos. Si la primera etapa es nula, el efecto IV focal no está identificado por ese instrumento; un ITT distinto de cero puede revelar vías alternativas o errores de especificación, no un efecto de accesibilidad.

### 51.4. Construcción coherente del no cumplimiento

La generación no asigna directamente A_f*. Para cada unidad se genera un estado basal de dependencia y un mecanismo de provisión:

1. C_dep,0 se mide antes de Z; la población de apertura exige C_dep,0=0.
2. Z asigna una versión concreta de B.
3. W registra intento, inicio y finalización de instalación.
4. Se generan C_install, C_integrity, C_compat y C_oper.
5. C_dep,1 = C_install ∧ C_integrity ∧ C_compat ∧ C_oper.
6. A_f* se deriva de C_dep,1 y del resto de condiciones focales: autorización basal, recursos, capacidad, información, dominio y restricciones.
7. ΔT_acc se recalcula con el catálogo completo y se registra snapshot versionado.

Para el ejemplo monotónico previo puede utilizarse una variable latente común U y probabilidades finales de acceso p0=.20, p1=.80, de modo que A_f*(z)=I(U≤p_z). Esta construcción solo es admisible si se implementa a través de los pasos de provisión y verificación anteriores: U representa propensión a completar la provisión/instalación, no una asignación directa de accesibilidad. La interpretación de p0 debe aclarar si representa acceso por instalación basal residual, contaminación o provisión de control; no puede contradecir C_dep,0=0 sin explicar la vía que genera ese acceso.

### 51.5. Consecuencias para los estimandos

En cada escenario se informarán, como mínimo:
- TE_Z = E[V|Z=1] − E[V|Z=0], ITT de asignación;
- ITT_A = E[A_f*|Z=1] − E[A_f*|Z=0], primera etapa en accesibilidad verdadera;
- Wald = TE_Z / ITT_A, solo si la primera etapa es distinta de cero y los supuestos IV son defendibles;
- estimandos por F_alt,0, para detectar modificación del efecto y diferenciar P*_τ2 de P*_F;
- contraste de accesibilidad observada frente a verdadera, cuando haya error de medición.

El cociente Wald no es θ_τ2(P*_τ2) en general: bajo las condiciones IV usuales identifica un efecto local ponderado entre compliers. Con heterogeneidad, no equivale al ATE en P*_τ2 ni al efecto en P*_F. Si hay múltiples versiones de instalación o de accesibilidad, se debe demostrar consistencia de versiones o definir el tratamiento como una política/versionado más amplio.

En S4R-C, reportar TE_Z como efecto de asignación al paquete. Si la provisión altera varias rutas, no atribuir el efecto a τ2 mediante el IV simple. En S4R-D con primera etapa cero, no calcular ni interpretar Wald; reportar ITT, primera etapa y fallo de identificación.

### 51.6. Contrato de rutas alternativas por brazo

El registro de F_alt incluirá:
- identidad y versión de cada ruta alternativa;
- accesibilidad basal y posterior;
- relaciones, precondiciones, recursos y dependencias;
- evidencia de que B no la modifica o descripción del cambio;
- función F* que satisface y horizonte;
- si se seleccionó/ejecutó, en campos separados de accesibilidad;
- coste, latencia, calidad, seguridad y otros efectos colaterales.

No se inferirá que B no afecta una alternativa solo porque no cambie su etiqueta de catálogo. Deben verificarse condiciones y rendimiento funcional. Si B cambia una dependencia compartida, la alternativa puede cambiar aunque su identidad transformacional permanezca igual.

### 51.7. Pruebas de aceptación propuestas

- S4R-01: en A, G0 sin alternativa y G1 con τ2; exclusividad solo respecto al universo declarado.
- S4R-02: en B, alternativa basal permanece idéntica entre brazos y τ2 se abre; P*_τ2 incluye, P*_F excluye.
- S4R-03: alternativa basal sustituye F* pero conserva identidad distinta de τ2.
- S4R-04: alternativa basal modifica la magnitud del efecto sin violar automáticamente exclusión.
- S4R-05: B modifica alternativa y el analizador rechaza interpretación IV focal.
- S4R-06: cambio de dependencia compartida modifica alternativa sin cambiar identidad; detectar vía adicional.
- S4R-07: fallo en instalación deja C_dep,1=0 y A_f*=0 pese a Z=1.
- S4R-08: primera etapa nula; Wald no calculado/interpretado.
- S4R-09: primera etapa débil; activar inferencia robusta a instrumento débil.
- S4R-10: acceso focal se abre, pero τ2 no se aplica desde S0; no confundir accesibilidad con aplicabilidad.
- S4R-11: τ2 accesible y aplicable, pero no seleccionada; no inferir ausencia de acceso.
- S4R-12: ruta alternativa se ejecuta en lugar de τ2; mantener ambas trayectorias y mecanismo.
- S4R-13: B altera coste/calidad/seguridad de la alternativa; marcar paquete y revisar exclusión.
- S4R-14: clasificación F_alt utiliza Outcome o Value; invalidar evaluación.
- S4R-15: clasificación basal cambia tras asignación; fallo de temporalidad.
- S4R-16: p0=.20/p1=.80 contradice C_dep,0=0 o el proceso de instalación; fallo de consistencia DGP.
- S4R-17: ΔT_acc se reduce a A_f*; fallo de representación del cambio transformacional completo.
- S4R-18: estimación Wald se presenta como ATE; fallo de interpretación.

### 51.8. Dictamen y decisiones pendientes

**Dictamen:** los cuatro escenarios mínimos permiten separar apertura de τ2, substitución funcional basal, intervención compuesta y no cumplimiento. La matriz debe integrarse en el DGP antes de implementar el generador.

Se propone mantener como objetivo primario de diseño el ITT de la política aleatorizada en P*_τ2; como objetivo de atribución focal, el efecto IV/LATE solo cuando sus supuestos sean defendibles; y como análisis secundario, P*_F y la heterogeneidad por alternativas basales.

Pendientes antes de congelar:
- definir la política B y sus versiones, incluidos control y contaminación;
- reconciliar p0=.20 con la condición C_dep,0=0;
- decidir si S4R-C es un escenario de fallo de exclusión o un diseño factorial alternativo;
- formalizar estimandos y población en C10-D1;
- fijar F*, q_X*, horizonte y Value;
- especificar medición de F_alt, costes/efectos colaterales y validación;
- fijar reglas para primera etapa nula/débil y estimación robusta;
- completar revisión independiente XSYNC y resolver hallazgos abiertos.

No se congela S4-R, no se implementa ni simula. Los valores y escenarios son especificaciones analíticas propuestas, no resultados experimentales.


---

# 52. Integración en el documento maestro de la recuperación conversacional 165–183

**Fecha de integración:** 2026-11-04  
**Fuente primaria examinada:** `Notes_261104_163033.docx`, recibida como archivo adjunto de conversación.  
**Cobertura:** secciones 165–183 inclusive; la sección 184 queda fuera.  
**Estado:** integración documental en borrador; decisiones científicas no aprobadas por el mero hecho de incorporarse; no hay ejecución experimental.

Esta sección incorpora al documento maestro los desarrollos recuperados de 165–183. El registro de recuperación conserva la procedencia y las alertas de cotejo; el registro de contratos conserva el catálogo normalizado de pruebas. Esta sección es el punto integrado de lectura dentro del documento principal y no sustituye la fuente primaria original.

## 52.1. Sección 165 — problema de coherencia de la primera etapa

La cuestión recuperada es cómo representar una primera etapa con acceso final en control (p_0=.20) y en tratamiento (p_1=.80), manteniendo a la vez una condición de dependencia basal (C_{dep,0}=0) para la población de apertura focal.

La distinción temporal esencial es entre dependencia basal antes de la asignación y dependencia/provisión final después de la asignación. (C_{dep,0}=0) no impide que el régimen de control tenga una provisión ordinaria posterior a la asignación; pero esa vía debe estar descrita en el DGP. No se puede introducir (p_0=.20) como probabilidad final sin identificar el mecanismo que lo genera.

## 52.2. Secciones 166–168 — mecanismos D1 y D2

Se mantienen dos construcciones candidatas, no decisiones aceptadas:

| Parámetro | D1: provisión ordinaria en control | D2: sin provisión ordinaria en control |
|---|---:|---:|
| Intento/provisión en control (w_0) | .25 | 0 |
| Intento/provisión en tratamiento (w_1) | 1 | 1 |
| Probabilidad final de acceso (p_0) | .20 | 0 |
| Probabilidad final de acceso (p_1) | .80 | .80 |
| Primera etapa (p_1-p_0) | .60 | .80 |

La cadena generativa que debe quedar explícita es:

[
Z ightarrow B ightarrow W ightarrow
(C_{install},C_{integrity},C_{compat},C_{oper})
ightarrow C_{dep,1}ightarrow A_f^*
]

con:

[
C_{dep,1}=C_{install}land C_{integrity}land C_{compat}land C_{oper}.
]

(A_f^*) se deriva de (C_{dep,1}) y de las demás condiciones focales (autorización basal, recursos, capacidad, información, dominio y restricciones); no se asigna directamente a partir de (Z). La variable latente común (U) puede representar propensión a completar la provisión/instalación y generar (A_f^*(z)=I(Ule p_z)), pero solo si el mecanismo de instalación y verificación implementa esa probabilidad. La independencia entre latentes es una elección del DGP, no una condición lógica de monotonicidad.

La recomendación recuperada es D1 como escenario principal **condicionado** a justificar que la provisión en control pertenece al régimen comparador ordinario; D2 como contraste. En D1 no debe llamarse contaminación a una provisión que forma parte del comparador preespecificado. Sí debe registrarse crossover/contaminación si el control recibe componentes reservados al tratamiento. Instalación, integridad, compatibilidad y operatividad permanecen como componentes observables separados.

## 52.3. Sección 169 — supuestos IV

La interpretación IV/LATE exige auditar por separado:

1. Independencia del instrumento/asignación respecto de los potenciales pertinentes.
2. Relevancia: primera etapa distinta de cero y suficientemente informativa.
3. Monotonicidad individual, sin defiers bajo la codificación adoptada.
4. Exclusión para el resultado y tratamiento focales.
5. Consistencia y versiones del tratamiento suficientemente definidas.
6. Ausencia de interferencia o tratamiento explícito de interferencia.
7. Medición válida de accesibilidad verdadera y resultado/Value.

Ningún supuesto se considera demostrado por estar escrito en el DGP. La primera etapa positiva no prueba exclusión. La asignación aleatoria puede identificar el ITT de la política aunque no identifique el efecto focal de accesibilidad.

## 52.4. Secciones 170–171 — exclusión, efectos directos y sensibilidad

La fuente introduce potenciales (V_i(a,z)), con efecto directo (delta), interacción (gamma) y vías alternativas desde la asignación/provisión hacia Value. El diseño debe distinguir:

- efecto de accesibilidad focal;
- efecto directo de la asignación/provisión;
- interacción entre accesibilidad y asignación;
- vías por coste, calidad, seguridad, latencia u otras rutas;
- efecto total de la política asignada.

Con (delta
e0) o vías directas no bloqueadas, el cociente de Wald no debe atribuirse exclusivamente a accesibilidad. Con interacción (gamma), el efecto focal puede depender del régimen. Las expresiones de sesgo Wald recuperadas pertenecen a un modelo simplificado y deben verificarse bajo el DGP final, en particular si hay heterogeneidad.

Se propone una batería adversarial E1–E6 y análisis de sensibilidad sobre (delta) y (gamma), sesgo IV, umbrales de cambio de signo, cotas y clasificación de resultados como robustos, condicionados o insuficientes. Los rangos plausibles, tolerancias y precisión deben fijarse antes de la ejecución; los ejemplos de la fuente no son resultados.

## 52.5. Secciones 172–174 — heterogeneidad, LATE y poblaciones objetivo

Con heterogeneidad, el IV identifica un efecto local ponderado entre compliers inducidos por la política/instrumento estudiados. No autoriza inferencia automática al ATE ni al ATT. D1 y D2 pueden producir distintas proporciones y composiciones de compliers, y por tanto distintos LATE.

Deben mantenerse diferenciadas las poblaciones:
- (P^*_{	au2}): población con posibilidad estructural/focal de apertura de (	au2) según las condiciones basales especificadas.
- (P^*_F): población para la que la función objetivo (F^*) carece de alternativa funcional basal, según la definición preasignación.

La alternativa basal, los perfiles (X_i), la positividad/soporte y los pesos de agregación deben fijarse ex ante. La existencia de una alternativa puede modificar el efecto de abrir (	au2) sin constituir por sí sola una violación de exclusión. No debe confundirse sustitución funcional con identidad transformacional.

## 52.6. Secciones 175–176 — potenciales y DGP adversariales

La arquitectura de verdad del generador debe mantener separados, por unidad e historia:

- (A_i(z)): accesibilidad verdadera;
- (O_i(a,z)): Outcome;
- (F_{alt,i}(z)): rutas alternativas y sus cambios;
- (V_i(a,z)): Value;
- estados basales y postasignación, con tiempos y versiones;
- verdad latente del DGP y variables observadas disponibles al analizador.

El generador puede conocer estratos y potenciales que el analizador no recibe. Las pruebas deben comprobar no filtración, temporalidad, asignación, versiones, alternativas, vías directas y casos de no identificación. Los escenarios adversariales no deben construirse de forma que hagan imposible la condición de transformación o fuercen ejecuciones incompatibles.

## 52.7. Sección 177 — arquitectura de estimación

El protocolo recuperado contempla, como mínimo, ITT de asignación sobre Outcome y sobre cada dimensión de Value, primera etapa en accesibilidad verdadera/observada, IV/Wald/LATE cuando los supuestos se sostengan, covariables basales preespecificadas, heterogeneidad por perfiles y alternativas, intervalos de incertidumbre, errores estándar y reglas de multiplicidad/recuperación.

Los estimandos deben etiquetarse y dictaminarse por separado. ITT de política no equivale a efecto mediado por accesibilidad. El análisis de mediación requiere supuestos adicionales y tratamiento explícito de confusión postratamiento. ATE/ATT no se obtienen automáticamente del LATE. Los parámetros, población, horizonte, precisión, tolerancias y reglas inferenciales permanecen pendientes de fijación.

## 52.8. Sección 178 — protocolo sintético y reproducibilidad

Antes de ejecutar se debe preespecificar tamaño muestral (N), número de réplicas Monte Carlo, semillas, escenarios, parámetros, pérdidas/censura, potencia o precisión objetivo, intervalos, tolerancias, reglas de aceptación, artefactos de salida y condiciones de parada. Debe justificarse el diseño respecto de los estimandos y escenarios adversariales; no se fija aquí un (N) ni un número de réplicas por ausencia de justificación final en la fuente.

La ejecución requiere autorización separada. La existencia del protocolo o de fixtures no autoriza simulación.

## 52.9. Secciones 179–180 — definición y medición de Value

La recomendación recuperada es mantener inicialmente Value como vector multidimensional y no imponer un índice escalar hasta justificar dimensiones, escalas, ponderaciones, compensabilidad y sensibilidad. Outcome y Value no son intercambiables. Value requiere observador, contexto, criterio y regla explícitos; su valoración debe conservar momentos antes/después y trazabilidad.

La fuente considera dimensiones candidatas de calidad, seguridad, acceso, coste/eficiencia y otros componentes contextuales. La selección final y sus escalas requieren aceptación. Debe distinguirse accesibilidad de una transformación de acceso de los destinatarios a un resultado. No se permite que la definición/regla de Value se incorpore al régimen (q) de forma que cambie entre brazos.

## 52.10. Sección 181 — protocolo de medición independiente

A, O y V se miden con fuentes e instrumentos independientes, ventanas temporales explícitas, cegamiento cuando proceda y trazabilidad de versiones. No se define A mediante éxito de ejecución, O mediante valoración ni V mecánicamente a partir de A/O. La accesibilidad verdadera del generador se conserva separada de la medición observada del analizador.

La temporalidad T0–T6 debe fijar baseline, asignación, provisión, medición de accesibilidad, aplicabilidad/selección/ejecución, Outcome y valoración. Las pruebas P181-01…12 cubren independencia de medición, circularidad, fuentes, cegamiento, temporalidad, ausencias, invariancia, reproducibilidad, no filtración y contaminación. Siguen propuestas y no ejecutadas.

## 52.11. Sección 182 — validez de constructo

Se incorporan al registro maestro de pruebas los criterios recuperados:

| ID | Prueba | Criterio |
|---|---|---|
| P182-01 | Cobertura de A | Todas las condiciones constitutivas documentadas |
| P182-02 | Circularidad de A | A no depende de O ni de V |
| P182-03 | Especificación de O | Cada indicador tiene unidad, fuente y ventana |
| P182-04 | Separación O/V | La valoración no sustituye automáticamente al resultado operativo |
| P182-05 | Reproducibilidad | Valores reconstruibles desde registros |
| P182-06 | Acuerdo interevaluador | Acuerdo y discrepancias informados |
| P182-07 | Error en A | Falsos positivos y negativos evaluados |
| P182-08 | Error en O/V | Escenarios de error de medición comparados |
| P182-09 | Invariancia | Cambios de criterio entre D1/D2 detectados |
| P182-10 | Sensibilidad de Value | Efecto de reglas alternativas informado |
| P182-11 | Separación de datos | El analizador no recibe latentes del generador |
| P182-12 | Trazabilidad | Versión de indicador y regla conservadas |

La validez de constructo no se demuestra por completar la tabla: deben existir operacionalizaciones, instrumentos, fixtures, oráculos y evidencia de ejecución/revisión.

## 52.12. Sección 183 — datos ausentes, censura e identificación

Se incorporan los criterios recuperados:

| ID | Prueba | Criterio |
|---|---|---|
| P183-01 | Taxonomía | Cada ausencia tiene categoría documentada |
| P183-02 | Mecanismo | MCAR, MAR y MNAR evaluados |
| P183-03 | Separación A | Desconocido no equivale a inaccesible |
| P183-04 | Separación O | No observado no equivale a cero |
| P183-05 | Separación V | Ausencia dimensional no implica Value nulo |
| P183-06 | ITT | Se conserva la población aleatorizada |
| P183-07 | Selección | Mecanismos postasignación auditados |
| P183-08 | Mediación | Efecto de ausencia de A sobre identificación evaluado |
| P183-09 | Censura | Censura administrativa e informativa diferenciadas |
| P183-10 | Sensibilidad | Escenarios MAR/MNAR incluidos |
| P183-11 | Cotas | Calculadas cuando no procede estimación puntual |
| P183-12 | Dictamen | Estado de identificación separado por estimando |
| P183-13 | Trazabilidad | Reglas, versiones y decisiones conservadas |

Los dictámenes se emiten separadamente para ITT sobre O, ITT por dimensión de V, efecto mediado por A, LATE sobre V, efecto residual e índice agregado si se utiliza. No se convierte la ausencia de datos en cero ni se excluye automáticamente a unidades postratamiento. Si la mediación no es identificable, eso no implica necesariamente que el ITT total deje de serlo. Deben distinguirse ausencia de registro, fallo técnico, abandono, censura temporal, indefinición estructural y medición inválida; aplicar cotas/sensibilidad cuando sean defendibles y declarar no identificación cuando no lo sean.

## 52.13. Integración con S4-R, C10-D1 y el resto de C10-S

La recuperación refuerza y precisa la matriz S4-R de la sección 51:

- S4R-A: sin alternativa funcional basal; la exclusividad queda limitada al universo sintético declarado.
- S4R-B: alternativa basal presente y no modificada; puede reducir/modificar el efecto sin violar automáticamente exclusión.
- S4R-C: la política modifica alternativas/coste/calidad/latencia/seguridad; el ITT sigue siendo efecto de política/paquete, pero el IV focal queda comprometido.
- S4R-D: no cumplimiento/fallo de provisión; se separan asignación, provisión, dependencia operativa, accesibilidad y ejecución.

La matriz S4-R y esta recuperación deben armonizarse con C10-D1 en población, intervención, régimen (q), políticas (g), tratamiento focal, Outcome/Value, horizonte y estimandos. El ITT de la política es el estimando primario de asignación propuesto; el IV/LATE focal es condicional a supuestos; el ITT no demuestra por sí mismo la contribución causal específica de accesibilidad. Esta integración no resuelve por sí sola AUD-001/002 ni XAUD-001/002.

## 52.14. Decisiones, cuestiones abiertas y criterio de aceptación

Se conservan como propuestas recuperadas, no como decisiones congeladas:

1. D1 como principal condicionado y D2 como contraste.
2. Primera etapa generada por mecanismo de provisión verificable, no asignación directa de (A_f^*).
3. ITT de política separado de atribución focal IV/LATE.
4. LATE no extrapolado automáticamente a ATE/ATT.
5. Value multidimensional provisional, sin índice agregado no justificado.
6. Medición independiente de A/O/V, con generador y analizador separados.
7. Tratamiento explícito de missingness/censura y dictámenes por estimando.
8. Revisión de heterogeneidad, perfiles, soporte, alternativas y vías directas.

Quedan abiertos: reconciliación formal de (p_0=.20) con (C_{dep,0}=0) bajo el mecanismo D1; versión final de (B), (q), (g) y población; definición de (F^*), (q_X^*), horizonte y Value; ecuaciones de sesgo IV bajo el DGP heterogéneo; rangos (delta/gamma); tamaño muestral, réplicas y precisión; escalas y pesos de Value; contratos ejecutables y oráculos P181/P182/P183; cobertura GEN y AUD-004…008; revisión independiente y autorización de ejecución.

**Criterio de estado:** recuperación e integración documental ≠ aceptación científica ≠ test implementado ≠ test ejecutado ≠ evidencia empírica ≠ freeze. Ninguna de estas transiciones se presume.

## 52.15. Trazabilidad de artefactos de apoyo

- `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`: inventario de procedencia, cobertura, decisiones y alertas.
- `C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md`: actualización del estado de recuperación y límites de persistencia.
- `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md`: contratos normalizados, incluidos P182-01…12 y P183-01…13.
- `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`: puertas de cierre y reconciliación de hallazgos.

La copia íntegra DOCX original no está todavía persistida en el repositorio. Este capítulo es la integración en el documento maestro, no una reproducción literal íntegra de la fuente primaria. La sección 184 no se incorpora ni desarrolla aquí.


---

# 53. Auditoría integral de reconciliación y especificación candidata única

**Referencia:** `C10_S_INTEGRATED_RECONCILIATION_AUDIT_DRAFT_001.md`  
**Estado:** integración de auditoría documental / propuesta de armonización; NO APROBADA, NO IMPLEMENTADA, NO EJECUTADA.  
**Fecha:** 2026-11-04.

Esta sección establece el punto integrado de lectura para el diseño C10-S después de contrastar el documento maestro, C10-D1, la recuperación 165–183, el contrato DGP temporal/roles, la reconciliación de estimandos, el Decision Log, la matriz de cierre y los contratos de prueba. Las secciones históricas previas no se borran. Cuando una formulación temprana difiere de esta especificación candidata, se conserva como antecedente y se aplica la regla de precedencia aquí declarada; no se convierte una propuesta en decisión aceptada.

## 53.1. Precedencia

1. C10-D1 gobierna la pregunta causal general `θ_A(q)`, su interpretación y requisitos de identificación.
2. C10-S operacionaliza un experimento sintético focal y sus pruebas; no redefine C10-D1.
3. El contrato DGP temporal/roles contiene la formulación generativa candidata que debe armonizarse con este capítulo.
4. S4-R focaliza `τ2`; no identifica por sí solo el efecto general de todo `ΔT_acc`.
5. La matriz de cierre y el Decision Log registran estado y pendientes; no sustituyen las definiciones matemáticas.
6. Las fuentes 165–183 respaldan las propuestas recuperadas, pero su incorporación no implica aprobación científica.

## 53.2. Pregunta científica, objetivo del experimento y estimandos

Se mantienen distintos:

- **Pregunta C10-D1:** `θ_A(q)=E[V^{q,g1}]-E[V^{q,g0}]`, definida para población, horizonte, regla Value, versiones de política y régimen común factible. Es el objeto científico general.
- **Objetivo primario de S4-R:** `ITT_Z=E[V|Z=1]-E[V|Z=0]`, efecto de asignación aleatoria a las políticas de provisión concretas. Se informa por dimensión de Value y para los Outcomes preespecificados, sin condicionar a cumplimiento ni a variables postratamiento.
- **Primera etapa focal:** `ITT_{D_f}=E[D_f|Z=1]-E[D_f|Z=0]`, donde `D_f=I(A_{f,base}*=0 ∧ A_{f,post}*=1)`.
- **Atribución local secundaria:** `LATE_f=ITT_Z/ITT_{D_f}`, únicamente bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición válida; con inferencia robusta a instrumento débil.
- **Contraste poblacional focal:** `θ_{Af}(q*)`, solo cuando las políticas difieren únicamente en la distribución de accesibilidad focal bajo régimen común y factible, sin vías colaterales hacia Value.
- **Efecto de paquete:** `ψ_policy`, cuando la política cambia otras vías además de accesibilidad.

No intercambiar ITT, `θ_A(q)`, `θ_{Af}(q*)`, LATE, ATE, ATT ni efecto de paquete. Un ITT identificado no demuestra por sí mismo contribución causal específica de accesibilidad. La mediación y cualquier residual requieren identificación adicional; no usar `TE-θ_A(q)` como residual automático.

## 53.3. Poblaciones

- `P*_{τ2}` se define antes de Z con elegibilidad y condiciones basales; para el contraste de apertura basal→post requiere `A_{f,base}*=0`.
- `P*_F` es un subgrupo basal sin alternativa funcional substituible bajo `F*`; no es filtro automático de la población primaria.
- Alternativas, equivalencia funcional, soporte y estados indeterminados deben evaluarse solo con información basal para la clasificación primaria.
- No se excluyen unidades por cumplimiento, accesibilidad postratamiento, selección, ejecución, Outcome o Value.

## 53.4. D1 y D2: resolución de p0=.20 y C_dep,base=0

La recuperación de las secciones 165–183 propone D1 como escenario principal condicionado a justificar la provisión ordinaria en el control y D2 como contraste.

| Parámetro | D1 principal condicionado | D2 contraste |
|---|---:|---:|
| `C_dep,base` | 0 | 0 |
| `P(C_dep,post=1|Z=0)` | .20 | 0 |
| `P(C_dep,post=1|Z=1)` | .80 | .80 |
| Primera etapa objetivo | .60 | .80 |

Así, `p0=.20` en D1 es probabilidad de provisión/estado técnico final postasignación bajo la política de control, no accesibilidad basal. No contradice `C_dep,base=0`. D2 representa ausencia de provisión ordinaria en control. Si no se justifica que la provisión de control D1 pertenece al comparador legítimo, no se mantiene D1 como principal sin decisión explícita.

## 53.5. Cadena generativa y condiciones

La cadena de referencia es:

`Z → B_g → W_attempt → S_install → C_install/C_integrity/C_compat/C_oper → C_dep,post → A_f,post* → ΔT_acc → Reach_H → Π_candidate → K/Consider → Sel → Start → Exec → O → V`.

- Intento, éxito de instalación, estado técnico verificado y accesibilidad verdadera son variables distintas.
- `C_dep,post=C_install∧C_integrity∧C_compat∧C_oper`; cada componente conserva valor, estado epistémico, evidencia y tiempo de verificación.
- `A_f,post*` se deriva de `C_dep,post` y del resto de condiciones focales. Si estas últimas no están todas satisfechas, no se copia automáticamente la probabilidad de C_dep a A_f.
- La probabilidad .20/.80 se calibra en el estado final verificado. Si se usan `ω_z` y `s_z` para intento y éxito, la distribución conjunta debe producir las probabilidades finales objetivo; no se presume independencia.
- `A_f` es una proyección focal. `ΔT_acc=(ΔU,ΔR,ΔC,ΔValidity,ΔState)` conserva el cambio transformacional completo.
- Accesibilidad, aplicabilidad, Reach, conocimiento/consideración, selección, inicio, ejecución parcial/completa, Outcome y Value son predicados/eventos separados y fechados.

## 53.6. q*, g y factibilidad

`q*` es el régimen común, preespecificado y factible sobre condiciones/historias no manipuladas por la política. `g_0/g_1` implementan las políticas de provisión focal. No se fija simultáneamente el componente manipulado por g como si fuera una condición común de q.

Las condiciones constitutivas `C_c` delimitan la factibilidad y la elegibilidad; no se tratan como variables libremente intervenibles. Las políticas deben ser factibles bajo q* en la población/historias incluidas y tener soporte por estrato. Si no lo son, se restringe ex ante la población con justificación o se declara no identificación. q* no es la regla de Value.

## 53.7. DGP aislado y escenarios adversariales

El DGP aislado estipula que la política solo modifica la realizabilidad estructural de τ2; calidad condicional de ejecución, recursos, información, costes no inherentes, latencia, seguridad, expectativas y regla Value permanecen invariantes. La exclusión es una propiedad estipulada del mundo sintético que debe comprobarse en el generador.

Los DGP adversariales introducen δ, γ, vías directas, cambios de alternativas, versiones, no cumplimiento, errores de medición, primera etapa débil/nula, interferencia y missingness. El analizador debe clasificar correctamente efecto de paquete o no identificación. No se fusionan los DGP ni se redefine el estimando después de observar sus resultados.

## 53.8. Outcome, Value, medición y roles

Outcome y Value son constructos distintos. Value permanece vectorial de forma provisional; no se agrega sin justificar dimensiones, escalas, pesos, compensabilidad, beneficiario y horizonte. A, Outcome y Value se miden con fuentes, instrumentos y ventanas independientes. El analizador no recibe estados potenciales, latentes ni parámetros generadores. Ausencia, desconocido, censura, fallo técnico y cero observado no son equivalentes. Los dictámenes de identificación se emiten por estimando y dimensión.

## 53.9. Pendientes que permanecen abiertos

La armonización no cierra: definición física/versionado de B; aceptación de D1 como comparador principal; q* y soporte; F* y equivalencia funcional; unidad de asignación/interferencia; especificación completa de ΔT_acc, Reach y lógica de indeterminación; exclusión IV y rangos δ/γ; Value operacional; N, réplicas, precisión, tolerancias; fixtures y oráculos de todas las familias; cotejo literal y persistencia del DOCX; revisión independiente XSYNC; aprobación científica y gates de freeze.

## 53.10. Criterio de interpretación

La persistencia de este capítulo significa **especificación candidata reconciliada documentalmente**, no decisión aceptada, test PASS, implementación, ejecución, evidencia causal ni freeze. El estado de cada bloque debe mantenerse según la matriz de cierre y el Decision Log.



---

# 54. Diseño candidato de la política técnica B y calibración D1/D2

**Estado:** propuesta de operacionalización; OPEN-C10-001 no se declara cerrado.  
**Fuente de partida:** documento maestro §§30.2, 31.4, 52.2; contrato DGP §§3.1–3.2; recuperación de secciones 166–168.  
**Objetivo:** concretar la política B lo suficiente para que sus versiones y probabilidades puedan someterse a revisión, sin confundir asignación, intento, instalación ni accesibilidad.

## 54.1. Unidad técnica y acción de la política

La intervención focal candidata es la provisión/activación de un módulo de dependencia software en un sandbox sintético. El módulo habilita técnicamente la operación focal de reconfiguración τ₂ sobre un objeto de sistema predefinido. No ejecuta τ₂, no la selecciona y no determina su resultado.

La acción asignada es una política de provisión que determina la probabilidad de que el procedimiento técnico de activación sea iniciado. El procedimiento, módulo, versión, instrucciones, recursos, verificación y soporte técnico son comunes entre brazos. La diferencia focal entre versiones es la frecuencia/probabilidad de intento de provisión.

## 54.2. Versiones candidatas de B

| Versión | Escenario | Política de provisión | Probabilidad de intento |
|---|---|---|---:|
| B_g0^D1 | D1 control ordinario | Provisión ordinaria de baja frecuencia del mismo módulo | 0,25 |
| B_g1^D1 | D1 tratamiento | Provisión programada del mismo módulo a todas las unidades elegibles | 1,00 |
| B_g0^D2 | D2 control sin provisión | No se inicia provisión focal | 0 |
| B_g1^D2 | D2 tratamiento | Provisión programada del mismo módulo a todas las unidades elegibles | 1,00 |

Los valores 0,25/1,00 y 0/1,00 proceden de la tabla recuperada para D1/D2 en §52.2. No son tasas observadas ni una decisión aceptada. Debe precisarse quién/qué dispara el intento, la regla de elegibilidad técnica y el registro de recepción.

## 54.3. Mecanismo de intento a estado técnico verificado

Sea (W_i) el intento de provisión y (S_i) el éxito técnico conjunto de instalación/verificación condicionado a que se haya intentado:

[
P(W_i=1mid Z_i=z,D1)=
egin{cases}
0.25 & z=0\
1.00 & z=1
end{cases}
qquad
P(W_i=1mid Z_i=z,D2)=
egin{cases}
0 & z=0\
1.00 & z=1
end{cases}
]

[
P(S_i=1mid W_i=1,Z_i=z,D)=0.80
]

El 0,80 es la calibración algebraicamente necesaria para reconciliar las probabilidades de intento recuperadas con los estados finales objetivo .20/.80 en D1 y 0/.80 en D2. No es un parámetro original recuperado de forma literal ni un dato empírico: es una propuesta de factorización que deberá aceptarse o reemplazarse.

La condición técnica sigue siendo:

[
C_{dep,i1}=C_{install,i1}land C_{integrity,i1}
land C_{compat,i1}land C_{oper,i1}
]

El contrato debe definir la distribución conjunta de esos componentes de modo que:

[
P(C_{dep,i1}=1mid W_i=1,D)=0.80
]

No se presupone independencia entre instalación, integridad, compatibilidad y operatividad. Tampoco se permite que un fallo de verificación se convierta en éxito por imputación.

Bajo esta factorización:

| Escenario | (P(W=1mid Z=0)) | (P(W=1mid Z=1)) | (P(C_{dep}=1mid Z=0)) | (P(C_{dep}=1mid Z=1)) |
|---|---:|---:|---:|---:|
| D1 | .25 | 1.00 | .20 | .80 |
| D2 | 0 | 1.00 | 0 | .80 |

La primera etapa de (C_{dep}) es .60 en D1 y .80 en D2. Para que también sea la primera etapa de accesibilidad focal (D_f), todas las demás condiciones de τ₂ deben estar satisfechas en la población de apertura, o se debe calcular (A_f^*) desde todos sus predicados y reportar la diferencia real.

## 54.4. Separación de política, asignación, recepción y cumplimiento

Registrar por unidad y versión:

- (Z): brazo asignado aleatoriamente.
- (B_{assigned}): versión de política asignada.
- (B_{offered}): política efectivamente ofrecida.
- (B_{received}): provisión recibida/activada.
- (W): intento técnico, con actor/sistema, instante y motivo.
- (S): éxito de instalación y verificación.
- (C_{install},C_{integrity},C_{compat},C_{oper}): resultados separados y evidencia.
- (C_{dep}): conjunción técnica final.
- (A_f^*): accesibilidad verdadera derivada de C_dep y demás condiciones.
- (A_{f,obs}): medición disponible al analizador.
- (D_f): apertura basal→post.

Una asignación a B_g1 no garantiza que el intento o instalación hayan tenido éxito. Un fallo de intento, un fallo técnico, un crossover y una versión incorrecta son estados diferentes. El ITT conserva la asignación original. La recepción/fidelidad no sustituye Z ni permite redefinir retrospectivamente el brazo.

## 54.5. Invariantes del DGP aislado

Entre versiones deben permanecer idénticos: módulo y hash/versionado; protocolo técnico; criterios de elegibilidad; recursos por intento; soporte; instrumentos y umbrales de verificación; personal/actor o automatización; hardware/software no focal; información, formación, expectativas e incentivos; costes y latencias no inherentes; calidad, seguridad y riesgo; reglas de selección y ejecución; horizonte y regla de Value.

La única diferencia intencionada es la política de frecuencia de intento. Si la provisión ordinaria D1 produce vías adicionales o cambia otros recursos/expectativas, se registra como paquete y no se atribuye el ITT exclusivamente a accesibilidad. D2 es un contraste de diseño distinto, no una corrección silenciosa de D1.

## 54.6. Reglas de aceptación documental propuestas

1. Las probabilidades de intento son las de la tabla D1/D2; las probabilidades finales verificadas son .20/.80 o 0/.80.
2. El éxito técnico conjunto condicional a intento es .80 en la factorización candidata, con componentes separados y sin independencia supuesta.
3. (C_{dep,base}=0) y (A_{f,base}^*=0) se fijan antes de Z en la población de apertura.
4. Ningún registro confunde W, S, C_dep, A_f*, D_f, aplicabilidad o ejecución.
5. La verdad del DGP se calcula desde la cadena generativa, no desde una asignación directa de A_f*.
6. Crossover, no intento, fallo técnico, verificación desconocida y versión incorrecta tienen códigos distintos.
7. Se comprueba que las versiones no alteran vías no focales en el DGP aislado; el escenario adversarial las modifica deliberadamente.
8. La población, soporte y condiciones comunes permiten ambas políticas donde el contraste lo requiere.

## 54.7. Decisión que queda por tomar

La propuesta concreta el mecanismo B y muestra una factorización coherente con la fuente recuperada. No resuelve aún: (i) si la política D1 representa realmente el comparador científico deseado; (ii) quién/qué ejecuta el intento; (iii) qué constituye la recepción de B; (iv) qué componentes y tolerancias definen el éxito técnico; (v) cómo se codifica crossover; (vi) si se acepta .80 como tasa conjunta de éxito condicional; (vii) si el estimando focal es sobre C_dep o sobre D_f; y (viii) revisión independiente de exclusión y versiones.

**Dictamen:** B queda especificada como propuesta operativa candidata, no como decisión aceptada. OPEN-C10-001 continúa ABIERTA hasta aprobación explícita de la política, sus versiones y su comparador. No hay implementación, simulación ni ejecución.


---

# 55. Especificación candidata de q_X*, población objetivo y soporte por historia

**Estado:** operacionalización documental candidata; DEC-C10-012 y OPEN-C10-002 continúan abiertas.  
**Base fuente:** §44 (q_X*/q_L*), §§46–47 (población y elegibilidad basal), §53.6 y contrato DGP §3.4.  
**Alcance:** S4-R primario sintético. No modifica C10-D1 general, no redefine TGCV Core y no constituye aprobación ni ejecución.

## 55.1. Elección del régimen común para el DGP primario

Se adopta como propuesta de especificación primaria (q_X^*), no (q_L^*):

[
q_X^* = P^*(X,H_0,C_c mid E=1, C_{dep,0}=0, A_{f,0}^*=0)
]

(X) recoge características basales; (H_0), la historia completa relevante anterior a la asignación; (C_c), las condiciones constitutivas basales. (E=1) exige que todas las condiciones requeridas estén confirmadas como cumplidas. La ausencia basal de la dependencia focal y la inaccesibilidad basal de τ₂ se evalúan antes de Z mediante protocolo independiente y ciego.

(q_X^*) es una distribución objetivo sobre la población primaria preespecificada, no una intervención que fuerce valores de covariables. La distribución concreta, sus estratos, pesos y tamaño de soporte no están todavía fijados; no se asignan valores numéricos por conveniencia.

## 55.2. Condiciones que pertenecen a (C_c)

Las condiciones constitutivas son precondiciones de realizabilidad y elegibilidad, no componentes que la política B pueda manipular en el DGP primario. La matriz mínima candidata conserva:

- autorización basal no focal ((C_{auth,base}));
- recursos y disponibilidad ((C_{resource}));
- capacidad técnica/operativa ((C_{capacity}));
- información necesaria ((C_{info}));
- compatibilidad de dominio ((C_{domain}));
- otras precondiciones esenciales, identificadas y justificadas antes de Z ((C_{other})).

Cada (C_j) tiene ficha versionada según §47: definición, umbral, evidencia, procedimiento, tiempo basal, evaluador ciego, estado, calidad y trazabilidad. Los cuatro estados —cumplida, incumplida, indeterminada y no aplicable— se preservan. Solo las unidades con todas las condiciones requeridas cumplidas integran la población primaria confirmada. Indeterminada no equivale a incumplida ni a cumplida; no aplicable requiere regla de dominio previa.

(C_{dep,0}=0) no se incorpora a (C_c): es la ausencia basal de la dependencia focal que B pretende proveer. (A_{f,0}^*=0) es la comprobación independiente del cierre basal de la transformación focal. Esta separación evita definir elegibilidad usando el propio resultado postratamiento.

## 55.3. Historia y orden temporal

El contrato temporal mínimo es:

1. fijar dominio, unidad y versión del sistema;
2. observar (X,H_0,C_c) y documentar evidencia de elegibilidad;
3. verificar (C_{dep,0}=0) y (A_{f,0}^*=0), incluyendo búsqueda de rutas equivalentes;
4. cerrar la población objetivo y (q_X^*);
5. aleatorizar (Z) y registrar (B_{assigned});
6. aplicar la política asignada, registrando oferta/recepción, intento, instalación y verificación;
7. medir (C_{dep,post}), (A_{f,post}^*), (D_f), trayectorias, Outcome y Value en sus ventanas predefinidas.

Ninguna unidad se añade o elimina de (P^*_{	au2}) por variables observadas después de Z. Las reevaluaciones de baseline deben preceder a la asignación y conservar la trazabilidad.

## 55.4. Factibilidad y soporte por historia

Sea (mathcal H^*) el soporte de historias basales con masa positiva bajo (q_X^*). Para cada estrato/historia (hinmathcal H^*) se requiere:

- ambas políticas (B_{g0}) y (B_{g1}) tienen versiones definidas y son física/técnicamente implementables;
- el procedimiento no viola ninguna condición constitutiva ni exige cambiarla;
- la probabilidad de asignación a cada brazo es positiva en el diseño;
- la oferta/recepción y los fallos se registran sin redefinir retrospectivamente el brazo;
- la elegibilidad del estrato se determina antes de Z.

La factibilidad de ambas políticas no significa que cada unidad pueda alcanzar ambos estados de (D_f), ni garantiza cumplimiento. Esa diferencia determina quién puede ser complier y se conserva para la interpretación IV. No se excluyen estratos porque después se observe que no cumplen o no abren τ₂.

Si una política no es factible en una historia, hay solo dos salidas admisibles: (a) redefinir antes de Z la población objetivo y el estimando, justificando el alcance de la restricción; o (b) mantener la población y declarar que el contraste de políticas no está identificado para ese soporte. No se extrapola silenciosamente ni se reemplaza una política por otra.

## 55.5. Lugar de las variables post-asignación (L_m)

El DGP primario aislado no incorpora (L_m) post-asignación como confusor común de accesibilidad y Value, de acuerdo con §44.4. Esto es una estipulación del experimento sintético, no una afirmación sobre sistemas reales.

Si una variable post-asignación es indispensable y afecta tanto accesibilidad como Value, no puede incorporarse a (q_X^*) como si fuera basal ni resolverse mediante ajuste marginal. Debe definirse un régimen secuencial (q_L^*), con momento de intervención, historia condicionante, mecanismo implementable común, soporte por historia y estrategia de identificación longitudinal. Si no se puede definir ese régimen, el escenario correspondiente se clasifica como adversarial/no identificado para el contraste focal, no como DGP primario aislado.

## 55.6. Estimandos y alcance

Bajo (q_X^*), (ITT_Z) es el contraste primario de asignación en (P^*_{	au2}). (psi_B(q_X^*)) es el contraste estandarizado entre versiones implementables de las políticas. Solo si la asignación implementa las políticas previstas, hay consistencia de versiones y no existen vías diferenciales ajenas a accesibilidad podrá interpretarse el contraste como (	heta_{Af}(q_X^*)). Con incumplimiento, el ITT sigue referido a asignación; (LATE_f) requiere sus supuestos IV y se limita a compliers. Ninguno de estos objetos identifica automáticamente (	heta_A(q)) general de C10-D1.

## 55.7. Elementos todavía no fijados

No se inventan ni se cierran: distribución empírica/paramétrica (P^*); variables y categorías completas de (X,H_0); inventario definitivo y umbrales de (C_c); unidad de asignación e interferencia; probabilidades de asignación; tamaño y pesos de estratos; evaluación de rutas equivalentes; ventanas temporales; protocolo de Value; reglas para indeterminación persistente; y necesidad de (q_L^*) en cada escenario adversarial.

**Dictamen:** (q_X^*) queda especificado como referente común basal condicionado a elegibilidad constitutiva, dependencia focal ausente e inaccesibilidad basal. El soporte se define por historia y factibilidad de ambas políticas, sin condicionar por resultados postratamiento. Es una propuesta operacional coherente con §§44, 46 y 47; no cierra DEC-C10-012 ni autoriza ejecución.


---

# 56. Unidad experimental, unidad de asignación e interferencia: contrato candidato

**Estado:** propuesta de diseño para el DGP sintético primario; OPEN-C10-005 permanece ABIERTA hasta aprobación.  
**Base fuente:** §51.2 y §51.5 (unidad i, no interferencia como supuesto IV); contrato DGP §2; matriz S4R-15.  
**Objetivo:** hacer explícita la unidad sobre la que se define el tratamiento y los resultados potenciales, y especificar qué hacer si hay recursos compartidos o spillovers.

## 56.1. Tres unidades que no deben confundirse

- **Unidad experimental (UE):** instancia sintética del sistema cuyo estado basal, espacio de transformaciones, trayectoria, Outcome y Value se generan y evalúan.
- **Unidad de asignación (UA):** entidad a la que se asigna aleatoriamente una versión de B.
- **Unidad de observación (UO):** entidad sobre la que se registran las medidas y snapshots. Puede haber varias observaciones temporales por UE, pero no crean nuevas unidades independientes.

**Propuesta primaria:** UE = UA = una instancia sintética completa e independiente. La UO es la misma instancia repetida en tiempos T0–T9. Cada instancia recibe una sola asignación Z y una versión B durante el horizonte primario. La asignación no se realiza por transformación, trayectoria, resultado ni medición temporal.

Esta propuesta es adecuada para el DGP primario aislado si y solo si las instancias no comparten recursos, agentes, información, estado, políticas adaptativas ni canales de transmisión que permitan que la asignación de una instancia afecte los resultados de otra.

## 56.2. Clúster y dependencia

Si varias UE comparten un recurso, agente, entorno, organización, infraestructura, presupuesto, cola de servicio, información o regla de decisión, se define un clúster (c). La independencia entre esas UE no puede suponerse por conveniencia.

Hay dos diseños admisibles, que no se mezclan:

1. **Asignación individual dentro de clúster:** solo si se puede justificar ausencia de interferencia entre UE del mismo clúster o modelar explícitamente la exposición cruzada. La inferencia debe respetar la dependencia residual.
2. **Asignación por clúster:** todas las UE del clúster reciben la misma política asignada (Z_c). La UA es el clúster y el estimando primario es un contraste de política a nivel de clúster o un contraste individual ponderado con inferencia que respete la aleatorización por clúster. El tamaño efectivo depende del número de clústeres, no del número bruto de UE.

La decisión entre ambos diseños requiere conocer el mecanismo concreto de B y el mapa de recursos/relaciones. No se declara que la asignación por clúster sea necesaria sin evidencia de agrupación; tampoco se declara que la asignación individual sea válida antes de auditarla.

## 56.3. Resultados potenciales con interferencia

Bajo no interferencia:

[
V_i(z_i),quad D_{f,i}(z_i)
]

y el ITT individual es (E[V_i(1)-V_i(0)mid P^*_{	au2}]).

Si puede existir interferencia, se introduce un mapa de exposición preespecificado (G_i(mathbf Z_{-i})), basado en relaciones de recursos, agentes, comunicación o vecindad pertinentes:

[
V_i(z_i,g_i),quad D_{f,i}(z_i,g_i)
]

El mapa (G_i) debe fijarse antes de generar resultados y debe corresponder al mecanismo real de spillover. Se distinguen al menos: exposición cero, exposición a unidades tratadas, exposición a unidades control, recurso compartido saturado y exposición indeterminada. No se infiere (G_i) desde Outcome o Value.

Si la exposición es parcial, se define el estimando compatible: efecto directo a exposición fija, efecto indirecto/spillover, efecto total de política o contraste de saturación. El ITT individual convencional no se conserva como si no hubiera interferencia.

## 56.4. Contrato de aleatorización y positividad

El diseño debe registrar, antes de asignar:

- identificador UE, UA, UO y, cuando aplique, clúster;
- marco de aleatorización, estratos/bloques y probabilidad conocida de cada asignación;
- versión de B asignada y regla de asignación;
- semilla/algoritmo, orden, fecha y hash del manifiesto;
- relaciones de recursos compartidos y mapa de exposición;
- desviaciones, reasignaciones y unidades no asignadas, sin borrado.

La probabilidad de asignación positiva requerida por (q_X^*) se evalúa en la UA real. Si se aleatoriza por clúster, no basta con que cada UE tenga probabilidad marginal positiva: debe existir soporte de asignación de clúster compatible con el estimando y con los estratos definidos.

## 56.5. Escenarios de interferencia y reglas de interpretación

| Escenario | Mecanismo | Resultado exigido |
|---|---|---|
| INT-U0 | UE independientes; sin recursos ni canales compartidos | ITT individual válido bajo aleatorización y demás supuestos |
| INT-U1 | Correlación basal por clúster, sin spillover de tratamiento | Errores/inferencia respetan clúster; no confundir correlación con interferencia |
| INT-U2 | Recurso compartido cuya disponibilidad cambia con Z ajeno | Detectar interferencia; ITT individual simple no se etiqueta causal |
| INT-U3 | Información/decisión/actor transmite provisión entre unidades | Modelar exposición; si no es medible, no identificación del efecto individual focal |
| INT-U4 | Asignación aleatoria por clúster | Estimar efecto de política según unidad y esquema de aleatorización por clúster |
| INT-U5 | Mapa de exposición incompleto o desconocido | INDETERMINATE / NO IDENTIFICADO para efectos que requieren exposición |
| INT-U6 | B modifica recursos compartidos y afecta más de una UE | Efecto de política de clúster/paquete; no LATE individual focal sin rediseño |

## 56.6. Implicaciones para ITT, IV/LATE y C10-D1

- El ITT de S4-R sigue siendo efecto de asignación, pero su unidad es la UA realmente aleatorizada. Con UA individual y no interferencia puede expresarse como contraste individual; con UA clúster, debe respetar el clúster.
- El LATE_f exige no interferencia en la versión individual convencional. Si hay interferencia, se requiere un estimando IV de exposición/cluster explícito; no se reutiliza el Wald individual.
- La primera etapa (ITT_{D_f}) también debe estimarse en la unidad y exposición definidas.
- El estimando general (	heta_A(q)) de C10-D1 no se sustituye por un efecto de clúster ni por ITT_Z. Si la política opera sobre recursos compartidos, la intervención causal debe redefinirse como política sobre el clúster/sistema relevante.

## 56.7. Regla de decisión y datos faltantes

No se acepta UE=UA por definición universal. Se acepta como configuración primaria candidata únicamente si el inventario del entorno confirma independencia entre instancias. Si aparece cualquier recurso/canal compartido relevante, se pausa la asignación individual y se decide entre clúster, diseño de saturación o declaración de no identificación.

La unidad, el clúster, la exposición y las probabilidades de asignación se fijan antes de generar los resultados potenciales y antes de observar Outcome/Value. No se crean clústeres retrospectivos para obtener errores estándar convenientes.

**Dictamen:** UE=UA=instancia sintética independiente es la propuesta más parsimoniosa para el DGP aislado; no es todavía una decisión aprobada ni un hecho verificado. El mapa de interferencia y la auditoría de recursos compartidos son condiciones de aceptación. OPEN-C10-005 sigue ABIERTA. No hay implementación, simulación ni ejecución.


---



---

# 57. F*, equivalencia funcional y rutas alternativas: contrato armonizado

**Estado:** operacionalización candidata y reconciliación interpretativa de §§48–50; DEC-C10-017 y OPEN-C10-003 permanecen ABIERTAS.  
**Fuentes internas:** §§48.3–48.8, 49.11, 50.1–50.9, 51.1–51.5; contrato DGP §14; matriz S4R-02…06, S4R-11…15; INT-01…12; ACC-01…12 y EVID-01…15.

## 57.1. Dos objetivos y dos poblaciones

- **P*_tau2:** unidades constitutivamente elegibles, con D_f,0=0 y A_f,0*=0 respaldados antes de Z. Estudia la apertura de la identidad transformacional focal tau2.
- **P*_F:** subconjunto de P*_tau2 en el que la ausencia de rutas alternativas funcionalmente substituibles para F* está respaldada dentro del universo, granularidad, condiciones y horizonte declarados. Estudia la apertura funcional exclusiva.

**Reconciliación de §48.6:** su frase que incluía F_alt,0=0 como requisito general de la población primaria se interpreta, a la luz de §50.7 y §51.1, como requisito de P*_F, no como filtro automático de P*_tau2. Se conserva la formulación histórica y su trazabilidad; esta sección explicita la interpretación armonizada candidata, pendiente de revisión y aceptación.

El objetivo primario propuesto de S4-R sigue siendo el ITT de la política en P*_tau2. P*_F es subobjetivo funcional/heterogeneidad, no población primaria por defecto.

## 57.2. Ficha operacional de F*

F* es una especificación técnica de capacidad/función evaluable sin Outcome ni Value. Antes de clasificar unidades debe fijar:

1. Objetivo funcional observable y criterio técnico de éxito.
2. Entrada, estado inicial S0, información y precondiciones.
3. Salida/efecto técnico y propiedades verificables; no basta una etiqueta o estado final nominal.
4. Restricciones constitutivas: seguridad, integridad, compatibilidad, permisos y recursos.
5. Tolerancias admisibles de calidad, precisión, fiabilidad, capacidad y degradación. No se inventan umbrales numéricos.
6. Horizonte H: tiempo/pasos máximos y ventanas.
7. Granularidad G: nivel de identidad de transformaciones, composiciones, operaciones y rutas.
8. Contexto C0: condiciones basales y recursos disponibles.
9. Evidencia, estándar E1–E4 aplicable, evaluadores, cegamiento, desacuerdos y reproducibilidad.

La ficha debe contener ejemplos positivos, negativos y fronterizos. No puede ajustarse después de conocer Z, B, selección, ejecución, Outcome o Value.

## 57.3. Substituibilidad no equivale a identidad ni a equivalencia causal

Se conserva la relación propuesta: Sub(pi, F*, G, H, C0).

Una ruta pi es funcionalmente substituible si, desde el contexto basal especificado, satisface F*, sus restricciones y tolerancias dentro de H, con recursos y precondiciones disponibles y evidencia suficiente de mecanismo realizable.

Esto no significa que pi sea tau2, ni que ambas tengan igual coste, latencia, calidad, riesgo, fiabilidad o efectos sobre Value. Tampoco implica equivalencia causal, simetría o transitividad. Identidad transformacional y equivalencia funcional se registran separadamente.

Una posibilidad lógica, promesa o documentación no acredita realizabilidad. Tampoco la acredita una ruta que requiera recursos no disponibles. Se incluyen composiciones y mecanismos distribuidos cuando pertenezcan al universo declarado.

## 57.4. Juicios separados y estados de evidencia

Para cada ruta candidata se registran por separado:

- Acc(pi): accesibilidad de sus transformaciones constituyentes.
- App(pi,S0): aplicabilidad desde el estado y precondiciones basales.
- Sub(pi,F*,G,H,C0): cumplimiento funcional dentro del horizonte y restricciones.
- Identidad, versión, composición y mecanismo.
- Recursos, coste, latencia, calidad, seguridad y fiabilidad.
- Nivel de evidencia E1–E4, cobertura y evaluador.

F_alt,0 conserva tres estados:

- **Respaldado ausente (0):** cobertura suficiente del universo declarado y ninguna ruta substituible.
- **Respaldado presente (1):** al menos una ruta alternativa satisface el criterio con evidencia suficiente.
- **Indeterminado (?):** cobertura/evidencia insuficiente, recursos o precondiciones no resueltos, discrepancia no adjudicada o ruta candidata pendiente.

“No encontrado” no equivale a ausencia respaldada. Una ruta no aplicable, fuera de horizonte o carente de recursos se rechaza solo dentro de las condiciones auditadas; no se infiere imposibilidad universal.

## 57.5. Universo de búsqueda y procedimiento reproducible

Antes de clasificar F_alt,0 se versionan catálogo y versiones, reglas de identidad, granularidad, composiciones, universo de mecanismos permitido, S0, C0, recursos, H, F*, restricciones y tolerancias.

El procedimiento enumera rutas simples y compuestas; verifica precondiciones y recursos a lo largo de cada rama; evalúa accesibilidad y aplicabilidad sin inferirlas de ejecución; aplica el criterio funcional independiente; conserva rutas rechazadas e indeterminadas con sus razones; mide cobertura y límites; y versiona inputs, reglas, evaluadores, evidencia y resultados. La evaluación es ciega a Z, B, selección, ejecución, Outcome y Value.

La exclusividad solo recibe PASS dentro del universo, granularidad, contexto y horizonte declarados, con cobertura suficiente y sin rutas indeterminadas relevantes. No prueba ausencia universal fuera de ese ámbito.

## 57.6. Poblaciones, régimen común y estimandos

F_alt,0 no redefine por sí mismo la elegibilidad de P*_tau2:

- P*_tau2 conserva la definición basal de §50.2 y el régimen común candidato q_X* de §55.
- P*_F se informa como subconjunto separado, con su procedimiento de clasificación e incertidumbre.
- Si se estima un efecto estandarizado en P*_F, debe especificarse su distribución objetivo/restricción de q_X* (o un q_X,F* explícito), población de referencia, pesos y soporte. No se reutilizan automáticamente los pesos de P*_tau2.
- Las unidades con F_alt,0=1 permanecen en P*_tau2 si cumplen los demás criterios; las unidades con F_alt,0=? también pueden permanecer en P*_tau2, pero no se confirma su pertenencia a P*_F.
- P*_F no se generaliza a P*_tau2 sin supuestos de transporte/heterogeneidad defendibles.

Una alternativa basal puede modificar selección, ejecución, Reach, trayectorias y heterogeneidad sin invalidar automáticamente el efecto de abrir tau2.

## 57.7. Exclusión IV y vías de B

Una alternativa basal estable y no afectada por Z/B puede ser modificadora del efecto; su mera existencia no demuestra violación de exclusión.

Si B modifica disponibilidad, coste, calidad, seguridad, latencia o activación de una ruta alternativa, aparece una vía adicional que compromete la interpretación del instrumento como apertura exclusiva de A_f*. Si la alternativa emerge después de Z, se registra como mecanismo postasignación y no se ajusta ingenuamente.

En esos casos se conserva ITT_Z como efecto de política/paquete; no se etiqueta el Wald como LATE_f focal bajo exclusión vulnerada. Se requiere separación factorial, intervención adicional o estimando de paquete/exposición para atribuir componentes. Un control negativo no demuestra exclusión.

## 57.8. Error de clasificación, sensibilidad y reporte

La clasificación de F_alt,0 debe ser pre-Z, independiente y ciega. Se conservan los indeterminados; no se recodifican como ausentes. Se preespecifican análisis de sensibilidad a falsos positivos/negativos, cobertura incompleta, desacuerdo entre evaluadores y cambios razonables de granularidad, horizonte y tolerancias.

El informe presenta por separado P*_tau2, P*_F, P*_tau2\P*_F, indeterminados y excluidos; cobertura del universo; evidencia por ruta; y estimandos por población. No se combinan ambas poblaciones bajo una sola etiqueta de exclusividad.

## 57.9. Pruebas de aceptación

FSTAR-01…FSTAR-18 comprueban independencia de F* respecto de O/V; fijación previa de G/H/C0; separación identidad/accesibilidad/aplicabilidad/substituibilidad; rutas compuestas; recursos y precondiciones; estados 0/1/?; cobertura incompleta; cegamiento; P*_tau2 frente a P*_F; pesos/soporte específicos; efectos de B sobre alternativas; activación post-Z; errores de clasificación y sensibilidad; y límites de generalización.

## 57.10. Decisiones abiertas

No se fijan valores numéricos de F*, tolerancias, H, G, universo sintético cerrado, cobertura, recursos permitidos, estándar E1–E4 por clase, regla de adjudicación, tasas de error, distribución q_X,F*, pesos ni protocolo confirmatorio de heterogeneidad. Requieren decisión explícita y revisión independiente.

**Dictamen:** la reconciliación de §§48–50 es conceptualmente coherente si P*_tau2 y P*_F permanecen separadas y la exclusividad se limita a P*_F. El contrato ofrece una estructura operacional, pero no cierra la definición empírica de F*, la cobertura del universo ni la exclusión IV. DEC-C10-017 queda como propuesta. No hay freeze, implementación, simulación ni ejecución.


---

# 58. Contrato integrado de medición de A_f*, C_dep y ΔT_acc

**Estado:** propuesta operacional de medición y validación; no aprobada, no congelada, no implementada y no ejecutada.  
**Dependencias:** §§30, 38–43, 47–51, 53–57; contrato DGP §§2–8 y 16; resolución AUD-001/002 §§2–4; contratos ACC-01…12, EVID-01…15 y MEAS-01…14.  
**Propósito:** evitar que asignación, provisión, estado técnico, accesibilidad focal, aplicabilidad, medición observada y cambio completo del espacio transformacional se traten como una misma variable.

## 58.1. Objetos que deben permanecer separados

| Objeto | Significado | No equivale a |
|---|---|---|
| Z | Asignación aleatoria | Oferta, recepción, intento o acceso |
| B_assigned / offered / received | Política/versiones asignadas, ofrecidas y recibidas | Cumplimiento o éxito |
| W_attempt | Intento de provisión/instalación | Instalación verificada |
| S_install | Resultado del proceso de instalación | Dependencia técnica completa |
| C_dep | Conjunción de componentes técnicos de la dependencia focal | Accesibilidad completa de τ2 |
| A_f* | Verdad generadora sobre accesibilidad de la identidad focal τ2 | Z, C_dep por sí solo, aplicabilidad o ejecución |
| A_f_obs | Clasificación observada de accesibilidad, con incertidumbre | Verdad generadora infalible |
| App_f | Aplicabilidad de τ2 desde el estado inicial S0 y sus precondiciones | Accesibilidad estructural |
| T_acc | Snapshot del espacio completo de transformaciones accesibles | Catálogo de referencia o conjunto de ejecuciones |
| ΔT_acc | Diferencia estructurada entre snapshots comparables | A_f* ni una puntuación escalar |
| D_f | Apertura basal→post de τ2 en unidades inicialmente inaccesibles | A_f,post* ni ITT de Z |

La clasificación de cada condición concreta como constitutiva de accesibilidad, aplicabilidad desde S0, provisión técnica, contexto o mecanismo postratamiento sigue requiriendo justificación. No se resuelve por el nombre de la variable.

## 58.2. Verdad generadora y clasificación observada

Para el DGP, A_f*(i,t) ∈ {0,1} es el estado verdadero oculto de accesibilidad de τ2 en la unidad y snapshot especificados. El analizador no recibe este campo. Recibe A_f_obs(i,t) ∈ {1,0,?} y la evidencia observable permitida:

- 1: accesibilidad respaldada por evidencia suficiente dentro del ámbito definido;
- 0: inaccesibilidad respaldada por evidencia suficiente y condiciones de evaluación cubiertas;
- ?: evidencia ausente, contradictoria, incompleta o insuficiente.

? no se imputa a cero ni a uno. La verdad binaria del DGP permite evaluar el error del clasificador después de congelar la salida del analizador; no autoriza a filtrar la verdad al analizador.

La elegibilidad verdadera de P*_τ2 se conserva en el generador. La elegibilidad observada pre-Z se registra separadamente. Si la clasificación basal observada es indeterminada o discordante, no se incorpora silenciosamente como inaccesible confirmada: se informa como indeterminada y se evalúa el impacto de la selección/misclasificación sobre el estimando. Cualquier análisis restringido a elegibilidad observada confirmada debe etiquetarse como tal y no presentarse automáticamente como el estimando sobre P*_τ2 verdadero.

## 58.3. Contrato de C_dep

Se conserva la conjunción técnica candidata:

C_dep* = C_install* ∧ C_integrity* ∧ C_compat* ∧ C_oper*.

Cada componente debe tener definición operacional, identidad/versión, criterio de verificación, fuente, instante, responsable, resultado y evidencia. Los cuatro componentes no se presumen independientes. C_dep* es la verdad técnica del DGP; el analizador recibe los resultados/evidencias verificables y sus estados observados, no una etiqueta derivada sin trazabilidad.

Para cada componente se distinguen: satisfecho, incumplido e indeterminado en la capa observacional; no aplicable solo cuando una regla de dominio pre-Z lo justifique. Un fallo de verificación no se convierte en éxito por imputación. La tasa final P(C_dep*=1|Z=z) no se iguala a la probabilidad de intento P(W_attempt=1|Z=z).

C_dep no basta por sí solo para establecer A_f*. La relación entre dependencia técnica y accesibilidad debe especificar los demás predicados necesarios, y demostrar que son condiciones de acceso y no condiciones de aplicabilidad, ejecución o resultado.

## 58.4. Definición generadora de A_f* y App_f*

La propuesta de definición para cada snapshot es:

A_f*(i,t) = I[ID_τ2 válido en versión declarada ∧ C_dep*(i,t)=1 ∧ todos los predicados adicionales de acceso focal preespecificados satisfechos].

El inventario de predicados adicionales debe ser explícito y clasificado antes de construir los fixtures. No se presume que C_auth, recursos, capacidad, información, compatibilidad de dominio u otros campos pertenezcan todos a la misma clase: cada uno debe clasificarse como condición de acceso, precondición de aplicabilidad, condición constitutiva, mecanismo de provisión o variable postratamiento. La fórmula solo podrá cerrarse cuando esta clasificación esté aprobada.

App_f*(i,t) = I[las precondiciones de τ2 para el estado S0_i,t se satisfacen] se evalúa por separado. Es posible que A_f*=1 y App_f*=0: la transformación está accesible en el sistema, pero no es aplicable desde el estado actual. También es posible que la evidencia para uno de los juicios sea indeterminada mientras el otro está respaldado.

La ejecución observada no define retrospectivamente A_f* ni App_f*. Una transformación no ejecutada puede estar accesible; una ejecución observada puede ser evidencia auxiliar, pero no sustituye el protocolo independiente de medición ni permite inferir accesibilidad desde una muestra seleccionada de ejecutores.

## 58.5. Apertura focal D_f y primera etapa

Para la verdad del DGP:

D_f* = I(A_f*,base=0 ∧ A_f*,post=1).

D_f* se distingue del estado posterior A_f*,post. Para el analizador se construye D_f_obs únicamente con las clasificaciones observadas basales y post, preservando estados indeterminados y error de clasificación. La primera etapa causal primaria de referencia se calcula con la verdad del DGP por el evaluador; el analizador estima/reportará la primera etapa observada. La comparación entre ambas cuantifica sesgo de medición.

No se sustituye ITT_Df* por ITT_Df_obs sin advertirlo. Si hay error, se reportan sensibilidad/especificidad y su incertidumbre cuando la validación lo permita, o límites/análisis de sensibilidad cuando no. La corrección requiere una submuestra de validación con selección conocida; una referencia imperfecta no se denomina gold standard y debe aportar su propia incertidumbre.

## 58.6. Contrato de T_acc y ΔT_acc

Cada snapshot T_acc(i,t) debe incluir, al menos:

1. U_acc: identidades canónicas de transformaciones y versiones accesibles, con estados respaldados/indeterminados.
2. R_acc: relaciones tipadas, dirigidas cuando corresponda, con origen/destino, versión, condiciones, estado activo/inactivo/indeterminado y evidencia.
3. C_acc: condiciones/configuraciones relevantes para realizabilidad y composición, con valor/estado, ámbito, temporalidad y procedencia.
4. Validity: validez de identidad, versión, evidencia y cobertura del snapshot.
5. State: estado del sistema e historia necesarios para interpretar el snapshot, sin incorporar Outcome o Value como criterio de accesibilidad.

La comparación exige snapshots con unidad, dominio, horizonte de observación, granularidad, catálogo de referencia y reglas de identidad/versionado compatibles. Si no son comparables, ΔT_acc es indeterminado o requiere una transformación explícita de correspondencia; no se fuerza una diferencia por nombres parecidos.

Se conserva la descomposición:

- ΔU = (altas, bajas, cambios de versión/definición);
- ΔR = (relaciones añadidas, retiradas, reconfiguradas);
- ΔC = (condiciones/configuraciones añadidas, retiradas o modificadas);
- ΔValidity = (cambios de validez, evidencia, cobertura o estado epistémico);
- ΔState = (cambios relevantes del estado/contexto entre snapshots).

Cada evento de diferencia mantiene referencia al objeto antes/después, tipo de cambio, momento, fuente, regla de comparación y evidencia. Cambio de versión no implica automáticamente nueva identidad; cambio de condición o relación no implica automáticamente nueva transformación. Las indeterminaciones se propagan y no se convierten en altas/bajas ciertas.

ΔT_acc = (ΔU, ΔR, ΔC, ΔValidity, ΔState) es un objeto estructurado multidimensional, no una magnitud escalar ni una suma ponderada. A_f* es una proyección focal de τ2 dentro de este objeto, no su definición completa. Reach y trayectorias candidatas se derivan posteriormente conforme a reglas separadas; no forman parte del snapshot ni se infieren de ejecuciones.

## 58.7. Protocolo de medición y cegamiento

- Baseline: cerrar y sellar snapshots, identidad/versionado, condiciones, C_dep, A_f_obs, App_f, T_acc y cobertura antes de Z.
- Postprovisión: verificar instalación/componentes técnicos y C_dep después de la provisión, con instante y evidencia.
- Postaccesibilidad: capturar A_f_obs y T_acc después de verificación y antes de conocimiento/consideración, selección, inicio o ejecución.
- Fuentes: usar registros de autorización, configuración, inventario de recursos, pruebas de compatibilidad/operatividad y evidencia técnica reproducible. La mera documentación declarativa o la ausencia de ejecución no basta.
- Evaluación: dos evaluaciones independientes cuando el protocolo lo requiera; conservar desacuerdos y adjudicación trazable. El cegamiento cubre Z/B cuando sea factible y siempre selección, ejecución, Outcome y Value.
- Validación: una submuestra de referencia con mecanismo de selección conocido permite estimar error de clasificación. Si la referencia es imperfecta, modelar su error; si la selección de validación es desconocida o diferencial no corregible, declarar límites/no identificación.
- Cobertura: reportar universo, catálogo, reglas, componentes observados, fuentes ausentes, rutas no evaluables y alcance de la afirmación.

No se fijan aún estándares E1–E4 por clase, número de evaluadores, umbrales de concordancia, tamaño de validación, sensibilidad/especificidad mínimas ni tolerancias. Requieren decisión y justificación; no se inventan.

## 58.8. Roles y permisos de datos

| Campo | Generador | Analizador | Evaluador independiente |
|---|---|---|---|
| A_f*, C_dep*, D_f*, T_acc*, ΔT_acc* verdaderos | Sí | No | Sí, después de congelar salida |
| Asignación, B, intento y eventos técnicos observables | Sí | Sí | Sí |
| Evidencia y clasificación A_f_obs, App_f_obs, T_acc_obs | Sí | Sí | Sí |
| Parámetros de error, estados potenciales y truth del DGP | Sí | No | Sí |
| Selección, ejecución, Outcome y Value observados | Sí | Sí | Sí |
| Truth de vías alternativas y omisiones deliberadas | Sí | No | Sí |

El evaluador independiente compara el resultado ya congelado del analizador con la verdad oculta; no puede corregirlo ni revelar parámetros antes del análisis.

## 58.9. Salidas mínimas y criterios de fallo

El informe debe mostrar por separado: verdad DGP y clasificación observada; C_dep por componente; A_f_obs y App_f_obs; D_f* y D_f_obs; snapshots y cobertura de T_acc; cada componente de ΔT_acc; indeterminados; error de medición y sensibilidad; población verdadera y población observada elegible; y cualquier cambio no explicado por la política focal.

Falla del contrato si: se copia Z o B a A_f; se copia C_dep directamente a A_f sin predicados restantes; se deduce accesibilidad de ejecución; se colapsa App_f en A_f; se usa Outcome/Value para definir o validar A_f; se omiten versiones/relaciones/condiciones del ΔT_acc; se mezclan cambios ciertos e indeterminados; se compara snapshots no equivalentes; o el analizador accede a truth oculta.

## 58.10. Pendientes explícitos

Permanecen abiertos: clasificación causal/ontológica de cada condición del DGP; definición completa de identidad y versión de τ2; ficha técnica de C_dep y de cada predicado adicional; definición y medición de App_f; estándares de evidencia E1–E4; reglas de adjudicación y concordancia; diseño/tamaño de validación; error diferencial por brazo/versión; cobertura del universo sintético; catálogo y relaciones completos; reglas de correspondencia entre snapshots; umbrales/tolerancias; y revisión independiente.

**Dictamen:** el contrato separa las capas y fija invariantes de medición suficientes para evitar sustituciones conceptuales, pero todavía no cierra la operacionalización empírica ni la validez de constructo. AUD-004, XAUD-003/004 y OPEN-C10-004 continúan abiertas. No hay freeze, implementación, simulación ni ejecución.


---

# 59. Matriz de clasificación causal y operacional de condiciones de τ2

**Estado:** propuesta de clasificación para auditoría; no aprobada, no congelada, no implementada ni ejecutada.  
**Dependencias:** §§30.1–30.4, 31.3–31.8, 53, 58; contrato DGP §§2–8 y 17; XAUD-003/004; AUD-011.  
**Objetivo:** sustituir el término residual C_other y clasificar cada condición por función causal y momento, sin inferir su papel por el nombre.

## 59.1. Regla de clasificación

Una condición pertenece a la accesibilidad focal si, en el nivel de análisis declarado, su ausencia impide que τ2 esté disponible/realizable para la unidad bajo el sistema, configuración, recursos y política vigentes, con independencia de que la transformación sea aplicable desde el estado actual o finalmente ejecutada.

Una condición pertenece a la aplicabilidad si determina si τ2 puede ejecutarse desde un estado S0 concreto una vez que τ2 está disponible. Una condición de ejecución/calidad determina cómo se realiza o qué resultado produce después de iniciar una trayectoria válida. Una condición de provisión describe el proceso por el que se intenta modificar el sistema; no es por sí misma el estado de accesibilidad resultante.

La clasificación es relacional y dependiente del nivel: una misma variable nominal puede tener componentes distintos. Debe especificarse unidad, objeto, horizonte, versión, momento y contrafactual. No se permite usar una etiqueta única para ocultar esta heterogeneidad.

## 59.2. Matriz candidata

| Predicado/variable | Clasificación candidata | Regla operacional de inclusión/exclusión | Papel en S4-R aislado |
|---|---|---|---|
| C_install | Componente de dependencia/provisión técnica; constitutivo de C_dep una vez verificado | Instalación presente en la unidad/objeto/versión focal. Intento o registro de instalación no bastan | Parte de C_dep; puede variar por política |
| C_integrity | Componente técnico constitutivo de C_dep | Integridad del componente y artefactos verificada frente a criterio/versionado declarado | Parte de C_dep; puede variar por política |
| C_compat | Componente técnico constitutivo de C_dep | Compatibilidad con versión, interfaces y objeto designado; incompatibilidad impide realizabilidad focal | Parte de C_dep; puede variar por política |
| C_oper | Componente técnico constitutivo de C_dep | Prueba operativa mínima de disponibilidad del mecanismo; no mide éxito/calidad de una ejecución de τ2 | Parte de C_dep; puede variar por política |
| C_auth_base | Condición constitutiva basal de acceso/autorización | Permiso vigente para que la unidad pueda invocar τ2. No equivale a conocimiento ni a selección | Fijada y satisfecha antes de Z; no manipulada por B_g |
| C_resource | Condición de acceso si denota disponibilidad asignada y persistente de recursos necesarios para poner τ2 a disposición; condición de aplicabilidad/ejecución si denota insumo consumido por una instancia concreta | Descomponer stock/disponibilidad ex ante de recurso de la demanda/consumo requerido por ejecución. Registrar quién controla, cuándo y para qué unidad | Disponibilidad basal suficiente, constante y satisfecha. Consumo/calidad de ejecución se mide aparte |
| C_capacity | Condición de acceso si denota capacidad instalada/slots disponibles para ofrecer τ2; aplicabilidad si denota margen operativo requerido por S0 o carga concurrente concreta | Separar capacidad instalada de disponibilidad efectiva por unidad/tiempo y de precondiciones del estado | Capacidad basal fijada y suficiente; saturación/colas no deben cambiar diferencialmente por B_g |
| C_info | Condición de acceso solo si denota información técnica incorporada al sistema que hace posible invocar/realizar τ2; conocimiento, aviso, formación o conciencia del agente son mecanismos de conocimiento/consideración posteriores | Separar especificación/configuración técnica del conocimiento del usuario/agente y de mensajes/formación inducidos por la política | Especificación técnica fija; información/conocimiento del agente y comunicaciones invariantes, medidos aparte |
| C_domain | Condición constitutiva de acceso si denota que τ2 está definida y soportada para el dominio/tipo de objeto; aplicabilidad si denota que el estado S0 satisface precondiciones particulares | Separar compatibilidad del tipo de sistema/objeto del estado concreto sobre el que se aplicará τ2 | Dominio objetivo fijado; precondiciones de S0 se evalúan como App_f |
| C_other | No admisible como predicado residual | Descomponer en predicados nombrados, verificables, temporales y asignados a una sola función causal primaria; cualquier interacción se documenta explícitamente | Prohibido en fórmula final sin inventario, definición y pruebas |
| Estado S0 / precondiciones de τ1 | Aplicabilidad | Determina si τ2 puede seguir válidamente a la trayectoria/estado actual; no elimina la disponibilidad estructural de τ2 | App_f, no A_f* |
| Conocimiento/consideración K | Mediador o evento posterior de conocimiento/consideración | Requiere que el agente conozca o considere τ2; no constituye accesibilidad estructural salvo que el diseño defina explícitamente acceso informacional como parte del constructo y lo justifique | Medir después de snapshot A_f/T_acc; no incluir en A_f* en el DGP focal actual |
| Selección/inicio/ejecución/fin | Eventos posteriores distintos | Seleccionar, iniciar o ejecutar no prueba por sí solo accesibilidad; ejecución requiere aplicabilidad y trayectoria válida | No incluir en A_f*; conservar como eventos fechados |

Esta tabla no declara que la clasificación nominal sea universal. En especial, C_resource, C_capacity y C_info requieren descomposición semántica antes de asignarles un único indicador.

## 59.3. Ecuación candidata depurada

La fórmula de §30.1 contiene siete condiciones, pero C_other no está definido y varias condiciones pueden mezclar acceso con aplicabilidad. Se propone reemplazar su interpretación —no borrar la formulación histórica— por:

A_f*(i,t;τ2) = I[ID_τ2 y versión válidos ∧ C_dep*(i,t)=1 ∧ C_auth_base(i,t)=1 ∧ R_access*(i,t)=1 ∧ D_support*(i,t)=1],

donde:

- R_access* contiene únicamente disponibilidad ex ante de recursos necesarios para poner τ2 a disposición, no consumo o suficiencia de recursos de una ejecución concreta;
- D_support* representa compatibilidad del dominio/tipo de objeto con la definición de τ2, no precondiciones particulares del estado S0;
- capacidad instalada, información técnica y demás predicados solo entran en R_access*/D_support* si su definición satisface el criterio de §59.1 y no duplican C_dep;
- cada predicado debe tener definición, fuente, versión, ámbito, ventana temporal, estado verdadero y clasificación observada.

La ecuación es una propuesta para el DGP S4-R, no una definición universal de accesibilidad TGCV. Si R_access* o D_support* no añaden condiciones distintas y justificadas, se eliminan en vez de mantener factores redundantes. C_other queda retirado como comodín en la especificación futura, sujeto a auditoría de sus usos históricos.

La aplicabilidad se define aparte:

App_f*(i,t) = I[Pre_τ2(S0_i,t, historia_i,t)=1].

No se presupone que App_f* sea consecuencia de A_f*. La ejecución válida requiere además trayectoria habilitada, selección/inicio según régimen y cumplimiento de las reglas de ejecución; no se incorpora a ninguna de las dos definiciones.

## 59.4. Consecuencia para la intervención y los estimandos

En la modalidad preferida A de §16.4 y S4-R aislado, la política B_g modifica solo el proceso técnico que puede cambiar C_dep. C_auth_base, recursos, capacidad, información, dominio, interfaz, incentivos, conocimiento y calidad condicional de ejecución permanecen invariantes y satisfechos en la población primaria, salvo que se abra un escenario adversarial específico.

Si Z/B modifica C_auth, recursos, capacidad, mensajes/conocimiento, prioridades, trato, coste, latencia, seguridad o calidad de ejecución, la intervención deja de ser la manipulación técnica aislada descrita. El ITT sigue siendo efecto de la política/paquete. La atribución a A_f* requiere factorialización, control experimental independiente o supuestos identificadores defendibles; no se obtiene por ajustar estadísticamente variables postratamiento.

Las condiciones constitutivas basales delimitan factibilidad y elegibilidad; no se intervienen simultáneamente mediante q* y g. La condición manipulada por g queda fuera del régimen común q*. Cualquier unidad sin soporte para las políticas comparadas se excluye ex ante con regla explícita o se declara fuera del dominio de identificación.

## 59.5. Invariantes y pruebas de clasificación

- Accesible y no aplicable: A_f*=1, App_f*=0 es un estado permitido.
- Aplicable pero inaccesible: App_f*=1 no convierte A_f* en 1; la ejecución válida no puede proceder.
- Instalado pero incompatible: C_install=1 y C_compat=0 implican C_dep=0.
- Autorización ausente: si C_auth es constitutiva y no satisfecha, A_f*=0 aunque C_dep=1.
- Recurso basal suficiente vs recurso consumido: no colapsar disponibilidad ex ante y uso durante ejecución.
- Capacidad instalada vs saturación puntual: no colapsar stock de capacidad con disponibilidad bajo carga concreta.
- Información técnica vs conocimiento del agente: el segundo no se usa para redefinir A_f* en el DGP actual.
- Dominio compatible vs precondición de S0: C_domain puede ser 1 mientras App_f*=0.
- C_other no puede quedar sin definición ni recibir variables heterogéneas para cerrar artificialmente la conjunción.

## 59.6. Pendientes que impiden el cierre

Siguen abiertos: inventario exacto de componentes de C_resource, C_capacity y C_info; definición y fuente de C_auth_base; semántica de C_domain; inventario que sustituye C_other; si capacidad/recursos forman parte de la definición del sistema o de la unidad de análisis; ventanas de vigencia y reglas de actualización; interacción entre condiciones; evidencia y adjudicación; y reconciliación de toda fórmula histórica que use C_auth como condición basal frente a las modalidades de intervención sobre autorización.

**Dictamen:** se dispone de una matriz de clasificación provisional y una ecuación depurada candidata para S4-R. No se cierra AUD-011, XAUD-003/004, AUD-001/002 ni OPEN-C10-004. DEC-C10-019 queda como propuesta. No hay freeze, implementación, simulación ni ejecución.


---

# 60. Nivel de sistema y accesibilidad relacional: frontera, unidad y recursos

**Estado:** propuesta de arquitectura de medición; no aprobada, no congelada, no implementada ni ejecutada.  
**Dependencias:** §§2–3, 30–31, 58–59; contrato DGP §§2–8 y 17–18; XAUD-001…004; AUD-010/011.  
**Pregunta:** ¿la accesibilidad es propiedad del sistema o del sistema en relación con una unidad y sus recursos?

## 60.1. Dictamen conceptual provisional

La accesibilidad no debe definirse como propiedad intrínseca y descontextualizada de un sistema, ni como atributo psicológico o conductual del usuario. Es una **propiedad relacional y situada de realizabilidad**: una transformación pertenece al espacio accesible respecto de una frontera de sistema, una configuración temporal, un contexto y un conjunto de recursos/disposiciones efectivamente disponibles para la unidad de análisis.

La estructura del sistema delimita qué transformaciones puede soportar. La relación de esa estructura con una unidad, sus interfaces, asignaciones de recursos y condiciones de acceso determina cuáles de ellas están efectivamente disponibles para esa unidad. El conocimiento, la consideración, la selección y la ejecución son eventos posteriores y no constituyen accesibilidad en el contrato focal actual.

Por tanto, no se trata de elegir entre “propiedad del sistema” o “propiedad del usuario”. La formulación más precisa es: **propiedad del sistema-en-relación-con-la-unidad, bajo una frontera y un contexto explícitos**. La unidad no tiene que ser una persona; puede ser una organización, equipo, subsistema, agente o entidad experimental.

## 60.2. Dos niveles que no deben colapsarse

Se propone distinguir:

1. **Espacio de capacidad estructural del sistema**, T_cap(sys,t | B_sys, C_sys): transformaciones que la arquitectura/configuración del sistema puede soportar bajo la frontera B_sys y contexto estructural C_sys, sin asignarlas todavía a una unidad concreta.
2. **Espacio de accesibilidad efectiva de la unidad**, T_acc(i,t | sys, B_i, R_i, C_i): transformaciones de esa capacidad que están disponibles y son realizables para la unidad i en el momento t, dadas su interfaz, autorización, recursos asignados/disponibles y condiciones contextuales pertinentes.

Relación candidata: T_acc(i,t) ⊆ T_cap(sys,t).

La inclusión solo se sostiene cuando ambos conjuntos usan la misma identidad/versionado, granularidad, horizonte y reglas de realizabilidad. Si una unidad puede acceder a una transformación mediante un proveedor o sistema externo, ese proveedor debe incluirse dentro de la frontera de sistema o registrarse como dependencia externa explícita; no se permite que la inclusión falle silenciosamente por una frontera ambigua.

T_cap no sustituye al T_acc del Core TGCV ni se propone como cambio del Core. Es una descomposición auxiliar para evitar confundir capacidad arquitectónica con acceso efectivo de la unidad. Si el sistema se define desde el principio incluyendo la unidad y sus recursos asignados, los dos niveles pueden coincidir; esa coincidencia debe declararse, no presumirse.

## 60.3. Frontera del sistema y unidad de análisis

Antes de medir accesibilidad se debe fijar:

- B_sys: frontera funcional y organizativa del sistema; componentes internos, servicios externos, interfaces y dependencias.
- i: unidad de análisis y entidad a la que se atribuye la disponibilidad.
- B_i: relación de pertenencia/acceso de la unidad al sistema (interfaz, canal, credenciales, derechos, ubicación o conexión pertinente).
- R_pool: recursos compartidos dentro de la frontera del sistema.
- R_i: recursos asignados o efectivamente disponibles para la unidad, con reglas de reserva, competencia, prioridad y concurrencia.
- C_sys y C_i: condiciones estructurales y condiciones específicas de la unidad, respectivamente.
- t: instante/snapshot y ventana de vigencia.
- G, H: granularidad y horizonte de evaluación.
- V: versiones de sistema, transformación, dependencias y política.

La elección de unidad no es una cuestión editorial: cambia la variable medida, la población, la estructura de dependencia y el estimando. Si Z se asigna a organizaciones pero A_f se mide por persona, la estructura jerárquica y la interferencia deben declararse. No se permite mezclar niveles sin una regla de agregación y un estimando multinivel explícitos.

## 60.4. Tratamiento de recursos y capacidad

Los recursos no son automáticamente “del sistema” ni automáticamente “de la unidad”. Se clasifican según su mecanismo:

| Recurso/condición | Nivel candidato | Tratamiento |
|---|---|---|
| Infraestructura instalada, licencias globales, capacidad nominal | Sistema | Delimita T_cap; no demuestra disponibilidad individual |
| Pool compartido y capacidad libre en una ventana | Sistema/tiempo | Registrar inventario, concurrencia, reglas de cola/prioridad y disponibilidad temporal |
| Recurso reservado/asignado a i | Relación sistema-unidad | Puede ser constitutivo de T_acc(i) si es necesario para disponer de τ2 |
| Recurso aportado por i y requerido para τ2 | Unidad/relación | Puede ser constitutivo de acceso efectivo; distinguir existencia de consumo |
| Recurso consumido por una ejecución | Ejecución | No usar retrospectivamente para definir accesibilidad basal |
| Capacidad requerida por el estado S0 o carga de una instancia | Aplicabilidad/ejecución | Evaluar por separado; no colapsar con capacidad instalada |
| Recurso externo/proveedor | Dependencia de frontera | Incluirlo en B_sys o documentar dependencia externa, disponibilidad, versión y contrato |

Una capacidad nominal instalada no basta si el recurso compartido está saturado y no existe asignación o disponibilidad para la unidad durante H. A la inversa, el hecho de que una unidad no haya consumido un recurso no prueba que careciera de acceso a él.

Si la disponibilidad depende de competencia entre unidades, T_acc(i) puede variar por la asignación a otras unidades. Se debe modelar interferencia/versión de exposición y no asumir SUTVA por conveniencia. Si el pool es no rival y suficiente, la disponibilidad puede ser común.

## 60.5. Notación y relación con el Core

Notación candidata:

T_acc,i,t = T_acc(i,t | B_sys, B_i, S_sys,t, R_pool,t, R_i,t, C_sys,t, C_i,t, V_t, G, H).

T_cap,sys,t = T_cap(sys,t | B_sys, S_sys,t, C_sys,t, V_t, G, H).

La lista de argumentos es un contrato de indexación, no una afirmación de que todos sean predictores independientes ni una ecuación causal. Algunos pueden ser partes del estado S del Core, otros relaciones de asignación o condiciones externas. Su clasificación debe evitar doble conteo.

El Core sigue siendo Core=(S,T_acc). Esta propuesta aclara que S y la frontera deben contener o referenciar la configuración relevante, mientras que T_acc se indexa por unidad y tiempo cuando la unidad no coincide con el sistema completo. No se introduce un tercer componente del Core.

## 60.6. Consecuencias para ΔT_acc y el experimento C10-S

ΔT_acc,i debe comparar snapshots de la misma unidad o de unidades comparables, con frontera, catálogo, granularidad, horizonte y reglas de recursos declarados. La descomposición de cambio debe distinguir:

- cambios de capacidad estructural ΔT_cap;
- cambios en interfaz/relación de acceso ΔB_i;
- cambios en asignación o disponibilidad de recursos ΔR_i;
- cambios en condiciones contextuales ΔC_i;
- cambios de identidad/versión, relaciones y evidencia ya definidos en §58.

Una variación de T_acc,i puede ocurrir sin cambio de T_cap (p. ej., se asigna una licencia o se habilita una interfaz). Una variación de T_cap no implica que todas las unidades reciban acceso efectivo. Si la política cambia a la vez capacidad del sistema y asignación por unidad, ambos mecanismos deben registrarse; no atribuir toda la diferencia a una sola causa.

El estimando C10 debe declarar si la intervención pretende:
(a) cambiar capacidad estructural del sistema;
(b) cambiar la relación de acceso de unidades a capacidad ya existente;
(c) cambiar ambos componentes como paquete.
El escenario S4-R de habilitación técnica aislada solo puede etiquetarse así después de fijar esta elección y demostrar que los otros componentes permanecen invariantes.

## 60.7. No agregación automática

No se define T_acc(sys)=⋃_i T_acc(i) como medida universal. La unión solo describe si alguna unidad dispone de cada transformación y puede ocultar desigualdad, saturación y distribución del acceso. Tampoco se usa promedio de cardinalidades como sustituto del espacio transformacional.

Si el outcome se mide a nivel de sistema, debe fijarse una función de agregación explícita (cobertura, distribución, mínimo, proporción de unidades elegibles, acceso ponderado u otra) y justificarla con el estimando. La agregación no forma parte de la definición básica de accesibilidad.

## 60.8. Pruebas conceptuales adversariales

1. Capacidad estructural presente, unidad sin credenciales: τ∈T_cap, pero τ∉T_acc(i).
2. Capacidad estructural presente, recurso compartido saturado y sin reserva: acceso efectivo puede ser 0 o indeterminado según ventana y regla.
3. Recurso asignado, transformación no aplicable desde S0: τ∈T_acc(i) y App_f(i)=0.
4. Unidad conoce una transformación no accesible: conocimiento no la incorpora a T_acc(i).
5. Transformación accesible no conocida ni ejecutada: sigue perteneciendo a T_acc(i) si la evidencia de realizabilidad es suficiente.
6. Cambio de asignación sin cambio de arquitectura: ΔT_cap=0, ΔT_acc(i)≠0.
7. Cambio de arquitectura sin asignación a la unidad: ΔT_cap≠0, pero ΔT_acc(i) puede ser 0.
8. Pool rival: la asignación a j puede modificar T_acc(i); evaluar interferencia.
9. Unidad agregada distinta de la unidad de asignación: declarar estructura jerárquica y no mezclar denominadores.
10. Servicio externo: si no se declara en la frontera ni como dependencia, el juicio de accesibilidad queda incompleto.

## 60.9. Decisiones que permanecen abiertas

Se requiere decidir para el experimento: frontera B_sys; unidad de asignación y unidad de análisis; si la unidad está dentro de la frontera o es una entidad relacionada; inventario de recursos compartidos y asignados; rivalidad/concurrencia; reglas de reserva y prioridad; dependencias externas; nivel al que se manipula Z/B; nivel de medición de Outcome/Value; estructura de interferencia; y regla de agregación si procede.

**Dictamen:** la accesibilidad se conceptualiza provisionalmente como propiedad relacional del sistema-en-relación-con-una-unidad, bajo frontera y contexto definidos. T_cap es un auxiliar de descomposición, no reemplaza T_acc ni altera el Core. La propuesta no cierra AUD-010/011, XAUD-001…004 ni OPEN-C10-004. No hay freeze, implementación, simulación ni ejecución.


---

# 61. Contrato de unidad y frontera para el DGP primario C10-S

**Estado:** propuesta de resolución de diseño; no aprobada ni congelada. No autoriza implementación, simulación ni ejecución.  
**Dependencias:** §§56, 59–60; DGP §§2, 14–15, 19; OPEN-C10-005; AUD-010/011; XAUD-001…004.  
**Objetivo:** elegir una configuración primaria parsimoniosa y falsable para que frontera, unidad, intervención y población sean coherentes.

## 61.1. Regla de diseño propuesta

Para el DGP sintético primario aislado se propone definir cada unidad experimental como **una instancia completa e independiente del sistema generativo**, incluyendo dentro de su frontera todos los componentes técnicos, interfaces, autorizaciones, recursos y dependencias que sean necesarios para evaluar la transformación focal τ2.

En esta configuración:

- UE = UA = unidad de análisis causal i.
- UO = la misma instancia observada repetidamente en T0–T9.
- Cada instancia recibe una sola asignación Z_i y una versión de política B_i durante el horizonte.
- No se aleatorizan por separado transformaciones, trayectorias, eventos, mediciones o resultados.
- Las observaciones longitudinales no incrementan el número de unidades independientes.

Esta es una **decisión candidata para el DGP aislado**, no una regla universal sobre sistemas TGCV ni una afirmación de que toda unidad real sea independiente.

## 61.2. Frontera operativa B_sys

La frontera de cada instancia incluye, cuando resulten pertinentes para τ2:

1. arquitectura y configuración del sistema;
2. módulo/dependencia focal y sus versiones;
3. interfaces y canales de invocación;
4. permisos y autorización basal;
5. recursos propios o asignados a la instancia;
6. capacidad disponible durante el horizonte;
7. información técnica integrada necesaria para realizar la transformación;
8. mecanismos internos de provisión, integridad, compatibilidad y operación.

Toda dependencia externa necesaria debe quedar en uno de dos estados: incorporada explícitamente a B_sys como componente/servicio gestionado, o declarada como dependencia externa con proveedor, versión, disponibilidad, contrato y posible interferencia. Una dependencia no inventariada impide clasificar la instancia como completamente evaluable; no se asume silenciosamente que está satisfecha.

## 61.3. Relación con T_cap y T_acc

Al tomar la instancia completa como unidad y contener dentro de su frontera los recursos y condiciones pertinentes, la distinción T_cap/T_acc puede colapsar operacionalmente en el escenario primario aislado, siempre que no haya asignaciones internas diferenciadas ni recursos compartidos entre subunidades.

En ese caso se registra T_acc(i,t) para la instancia. T_cap(sys,t) puede coincidir con T_acc(i,t) por construcción, pero no se elimina la distinción conceptual del capítulo 60 ni se generaliza esa igualdad a otros diseños.

Si se introducen usuarios, equipos o subsistemas con diferentes permisos, interfaces o asignaciones, la unidad vuelve a ser multinivel y T_cap/T_acc(i) deben medirse por separado. No se permite cambiar de nivel después de observar Outcome o Value.

## 61.4. Unidad de intervención y papel de Z/B

La asignación Z_i se realiza a nivel de instancia completa. B_i es la política de provisión técnica asignada a esa instancia; se registran por separado política asignada, ofrecida, recibida, intento, éxito técnico y estado final verificado.

Para el contraste aislado propuesto, B debe actuar sobre la provisión técnica focal necesaria para modificar C_dep y, por esa vía, A_f*. No debe cambiar simultáneamente autorización basal, reglas de asignación de recursos, capacidad compartida, información/conocimiento del agente, incentivos, prioridad, coste, latencia, calidad o seguridad de ejecución. Si alguna de estas condiciones cambia, se registra como vía colateral y el contraste pasa a interpretarse como efecto de paquete, salvo diseño factorial u otra estrategia de identificación previamente especificada.

Z no es la intervención material ni una medida de accesibilidad: asigna la política B. W_attempt, S_install, C_dep, A_f*, A_f_obs y D_f siguen siendo variables distintas.

## 61.5. Papel de q_X* y poblaciones

q_X* se interpreta como distribución objetivo de historias basales y condiciones constitutivas dentro de la población elegible; no como una intervención que modifica recursos, autorización u otras condiciones. Para evitar incompatibilidad, las condiciones constitutivas necesarias se fijan y verifican antes de Z. La política B no puede manipular una condición que simultáneamente se haya fijado como invariante basal en q_X*.

P*_τ2 contiene instancias con condiciones constitutivas basales confirmadas, D_f,0=0 y A_f,0*=0, conforme al contrato de §§50–57. P*_F sigue siendo el subconjunto con ausencia respaldada de rutas alternativas funcionalmente substituibles. La unidad, frontera y elegibilidad se fijan antes de determinar q_X* y aleatorizar.

La factibilidad de ambas políticas B_g0/B_g1 debe evaluarse para cada historia basal con masa positiva bajo q_X*. La falta de factibilidad exige restricción ex ante con nuevo estimando o dictamen de no identificación; no se corrige condicionando por cumplimiento postratamiento.

## 61.6. Interferencia y escenario primario

El DGP primario aislado se construye sin recursos, agentes, información, estado, políticas adaptativas ni canales de transmisión compartidos entre instancias. La no interferencia es, por tanto, una propiedad del generador que debe verificarse, no una presunción verbal.

Se conserva un escenario adversarial separado para recursos compartidos, spillovers informacionales, actores comunes o decisiones coordinadas. En ese escenario se debe definir el clúster, la UA clúster o un mapa de exposición G_i(Z_-i), y reformular estimandos, positividad, N efectivo e inferencia. No se mezcla el escenario adversarial con el primario aislado ni se lo usa para afirmar que el ITT individual es válido.

## 61.7. Condiciones para aceptar esta configuración

La propuesta solo podrá aceptarse cuando una revisión del DGP y de los contratos demuestre:

- frontera cerrada y dependencias inventariadas;
- UE=UA=i y UO longitudinal correctamente implementadas en la especificación;
- ausencia de recursos/canales compartidos entre instancias en el escenario primario;
- acción material de B descrita y diferenciada de Z/W/C_dep/A_f;
- invariancia de vías colaterales o reclasificación explícita como paquete;
- q_X* compatible con la intervención y soporte de ambas políticas;
- poblaciones P*_τ2 y P*_F clasificadas exclusivamente con información basal;
- escenario adversarial de interferencia separado y con regla de no identificación cuando corresponda.

**Dictamen:** se propone UE=UA=instancia sintética completa e independiente para el DGP primario aislado; la frontera contiene los componentes y recursos necesarios; Z asigna B, que manipula la provisión técnica focal. La propuesta no cierra OPEN-C10-005, AUD-010/011 ni XAUD-001/002. No modifica el Core, los estimandos de C10-D1 ni autoriza ejecución.


---

# 62. Contrato de intervención material B: provisión técnica focal de τ2

**Estado:** especificación candidata del tratamiento para el DGP sintético; no aprobada, no congelada, no implementada ni ejecutada.  
**Dependencias:** §§17–20, 56, 59–61; DGP §§14–20; C10-D1/S4-R; XSYNC-138-01/04; XAUD-001/002; OPEN-C10-005.  
**Pregunta:** ¿qué acción concreta asigna Z y por qué mecanismo se espera que cambie la accesibilidad focal?

## 62.1. Decisión de diseño propuesta

Para el DGP primario aislado se propone que B sea una **política protocolizada de provisión técnica de la dependencia focal τ2** a una instancia sintética completa. La acción material no es “hacer accesible” como etiqueta, ni asignar Z, ni ordenar una ejecución de τ2. Consiste en desplegar/configurar la dependencia técnica identificada, habilitar su interfaz de invocación dentro de la frontera y verificar su integridad, compatibilidad y disponibilidad operativa.

Esta definición concreta la clase de acción, pero no inventa un producto, módulo, tecnología real, duración, coste o umbral numérico. La identidad/versiones y los parámetros del artefacto sintético deberán quedar fijados en la ficha del DGP antes de cualquier implementación.

## 62.2. Contraste de políticas

| Elemento | B0 — control | B1 — provisión focal |
|---|---|---|
| Acción | Mantener la configuración basal; no desplegar ni habilitar la dependencia focal durante H | Aplicar el protocolo versionado de despliegue/configuración de la dependencia τ2 |
| Interfaz | Mantener interfaz basal | Habilitar el canal técnico específico de invocación de τ2 |
| Verificación | Verificar el estado basal con el mismo esquema de medición | Verificar instalación, integridad, compatibilidad y operación |
| τ2 | Permanece no provista/no accesible basalmente si se cumplen criterios de elegibilidad | Puede quedar técnicamente disponible si todos los predicados focales se satisfacen |
| Ejecución de τ2 | No se ordena | Tampoco se ordena como parte de B1 |
| Momento | Procedimiento de control en la ventana asignada; sin provisión focal hasta terminar H | Una intervención protocolizada dentro de la ventana asignada, con tiempos registrados |

B0 no debe retirar una capacidad basal existente ni empeorar deliberadamente la condición de control. B1 no garantiza éxito: una provisión fallida o parcial es non-compliance/fracaso de provisión, no motivo para reclasificar la asignación. El ITT conserva Z como asignación original.

## 62.3. Actor, destinatario, objeto y versión

Cada instancia recibe un registro de intervención con, como mínimo:

- actor/rol ejecutor del protocolo (agente de provisión sintético);
- destinatario (ID de instancia i);
- objeto focal (ID canónico de τ2 y dependencia técnica asociada);
- versión de protocolo B, artefacto, configuración e interfaz;
- fecha/orden de asignación, inicio, pasos, finalización y verificación;
- estado de cada paso: no iniciado, intentado, completado, fallido o indeterminado;
- desviaciones, reintentos, rollback y contaminación entre brazos;
- evidencia técnica independiente, snapshot pre y post y hash de configuración.

El actor es un rol del DGP, no una persona ni proveedor real. El protocolo no se adapta a Outcome, Value, trayectoria, selección ni respuesta observada.

## 62.4. Cadena causal y estados que no deben confundirse

La secuencia de implementación queda: Z_i → política B_i asignada → provisión recibida/intentada → estado técnico de dependencia C_dep*. C_dep* es evidencia de mecanismo/provisión, no definición suficiente de accesibilidad. A_f* se determina mediante el contrato estructural independiente de snapshots y predicados de accesibilidad del capítulo 63; después se deriva D_f* comparando baseline y post. La secuencia no autoriza inferir A_f* directamente desde C_dep*.

Se conservan separadas estas variables:

- Z_i: asignación aleatoria.
- B_i: política asignada (B0/B1).
- B_received: protocolo efectivamente recibido.
- W_attempt: intento de provisión.
- S_install: estado de instalación/configuración.
- C_dep*: verdad del contrato técnico compuesto.
- A_f*: verdad de accesibilidad focal.
- A_f_obs: medición observada de accesibilidad.
- D_f*: transición basal-post de inaccesible a accesible.
- App_f: aplicabilidad desde S0.
- Exec_f: ejecución efectiva de τ2.

B1 puede asignarse y no recibirse; recibirse y no completarse; completarse parcialmente; o completarse sin satisfacer todos los predicados de acceso. Ninguna de estas situaciones se reetiqueta como cambio de Z.

## 62.5. Contenido técnico de C_dep*

Para la dependencia focal, se mantiene la composición candidata:

C_dep* = C_install* ∧ C_integrity* ∧ C_compat* ∧ C_oper*.

- C_install*: componente/versión focal desplegado y registrado dentro de B_sys.
- C_integrity*: artefacto/configuración corresponde a la identidad y hash autorizados, sin alteración no permitida.
- C_compat*: interfaces, dependencias y contrato de τ2 son compatibles con la instancia y versión objetivo.
- C_oper*: canal de invocación está disponible y responde conforme al contrato técnico en la ventana definida, sin exigir que se ejecute τ2 sobre un caso funcional.

Cada componente requiere evidencia, tiempo y regla de adjudicación propios. **C_dep*=1 no implica por sí solo A_f*=1**: aún deben verificarse identidad transformacional, relaciones y dependencias activas, precondiciones/contexto, recursos y autorización aplicables, ausencia de bloqueos y validez/cobertura del snapshot. La accesibilidad se deriva del estado estructural completo, no del éxito de instalación aislado. La simple declaración de instalación, el intento, un test de salud superficial o la ejecución exitosa de τ2 no sustituyen el conjunto de verificaciones. Umbrales, fixtures y estándares de evidencia siguen abiertos.

## 62.6. Aislamiento de vías colaterales

Para interpretar B1 como provisión focal y no como paquete, el DGP debe mantener invariantes, entre otras, las siguientes dimensiones:

- autorización basal no focal y reglas de permisos;
- recursos no focales, presupuesto, capacidad compartida y prioridades;
- información/conocimiento/formación del agente o unidad;
- incentivos, selección, instrucciones de uso y atención diferencial;
- coste, latencia, calidad, seguridad y fiabilidad de rutas no focales;
- estado inicial, demanda, composición de la unidad y condiciones constitutivas;
- medición, adjudicación y observación de Outcome/Value.

Si el despliegue cambia necesariamente una de estas dimensiones, se documenta el cambio y el tratamiento se denomina **paquete de provisión**, no manipulación aislada de accesibilidad. El ITT de Z sigue siendo interpretable como efecto de asignar ese paquete, sujeto a aleatorización, consistencia y no interferencia; no identifica por sí mismo el efecto mediado por A_f*.

No se puede imponer por definición que no existan efectos directos B→Outcome/Value. Deben representarse en el DGP adversarial y tratarse como amenaza a exclusión/atribución.

## 62.7. Fracaso, desviación y contaminación

- B1 asignado pero no iniciado: incumplimiento de provisión; conservar en B1 por ITT.
- Intentado pero fallido: registrar el componente fallido; no inferir C_dep*=1.
- Parcial: evaluar cada componente; C_dep* solo vale 1 si se cumplen todos los predicados necesarios.
- B0 contaminado con provisión focal: registrar cruce; mantener asignación original y evaluar consistencia/contaminación.
- Rollback: registrar estado temporal y snapshot; no borrar que existió provisión.
- Evidencia indeterminada: C_dep_obs y A_f_obs conservan “?”; no recodificar como 0.
- Desviación del protocolo: versión y motivo; no redefinir B retrospectivamente.

## 62.8. Qué identifica y qué no identifica esta intervención

Con asignación aleatoria válida y ausencia de interferencia, el contraste primario identifica el ITT de asignar B1 frente a B0 en la población preespecificada. El primer estadio sobre D_f* mide si la política abre efectivamente τ2.

No basta con observar un ITT sobre Outcome/Value y una primera etapa positiva para afirmar mediación causal o efecto causal específico de accesibilidad. Esa atribución requiere los supuestos y análisis de mediación/IV ya abiertos en C10-D1/S4-R, incluida exclusión, versiones, monotonicidad, relevancia y ausencia de vías alternativas.

El estimando de política no debe rebautizarse como efecto de A_f*. Si B modifica otras condiciones, la conclusión se limita al paquete asignado.

## 62.9. Condiciones de aceptación antes de congelar B

La ficha de intervención debe completar y auditar, antes de congelar el DGP:

1. identidad canónica y versión sintética de τ2/dependencia;
2. artefacto y configuración exactos de B1 y estado basal exacto de B0;
3. actor/rol, destinatario, pasos y ventana temporal;
4. evidencia y criterio técnico para cada componente C_dep*;
5. prueba de que B0 no retira capacidad basal ni recibe contaminación focal;
6. inventario de variables invariantes y vías colaterales plausibles;
7. reglas para fallo, parcialidad, rollback, desviación y datos indeterminados;
8. correspondencia de B con q_X*, P*_τ2, P*_F y la unidad del §61;
9. escenario adversarial con vía directa B→Outcome/Value o B→alternativa funcional;
10. revisión independiente de la especificación y de su compatibilidad con C10-D1/S4-R.

**Dictamen:** B se concreta provisionalmente como política protocolizada de provisión técnica focal de τ2, comparada con mantenimiento de configuración basal. Es una especificación de tratamiento para el DGP sintético, no una intervención física ya implementada ni evidencia de que la accesibilidad haya cambiado. OPEN-C10-005, XAUD-001/002, AUD-001/002/011 y los supuestos de atribución permanecen abiertos. No hay freeze, implementación, simulación ni ejecución.


---

# 63. Contrato de medición de accesibilidad focal y cambio estructurado ΔT_acc

**Estado:** propuesta de especificación de medición y reconciliación; no aprobada ni congelada. No autoriza implementación, simulación o ejecución.  
**Dependencias:** §§26.2, 43.3–43.4, 58.5–58.6, 60–62; C10-D1 §27; XSYNC-138-03; AUD-001/004/005/007; OPEN-C10-005.  
**Objetivo:** impedir que el éxito técnico de B1, la aplicabilidad, la ejecución o una medición observada se confundan con la accesibilidad verdadera o con el cambio transformacional completo.

## 63.1. Distinciones normativas

Se mantienen cinco objetos diferentes:

1. **C_dep***: estado verdadero de los componentes técnicos de provisión de la dependencia focal. Es evidencia de mecanismo, no constructo completo de accesibilidad.
2. **A_f***: estado verdadero de accesibilidad de la transformación focal τ2, derivado de la representación estructural completa y de las condiciones de realizabilidad.
3. **A_f,obs**: clasificación observada/estimada por el analizador a partir de evidencia disponible; puede contener error o indeterminación.
4. **D_f***: apertura focal basal-post, definida por transición verdadera de inaccesible a accesible.
5. **ΔT_acc***: diferencia estructurada entre snapshots completos de accesibilidad; no se reduce a A_f* ni D_f*.

La notación estrella indica verdad del DGP/evaluador en el experimento sintético, no una variable que el analizador pueda observar directamente. En un estudio empírico, la verdad puede no ser identificable y debe informarse como tal.

## 63.2. Predicado estructural de accesibilidad focal

Para unidad i, transformación canónica τ2 y snapshot t, se propone:

A_f^*(i,t)=1 si y solo si todos los predicados siguientes están respaldados en el snapshot y bajo la frontera, granularidad, horizonte y reglas versionadas:

- **ID**: identidad canónica y versión de τ2 inequívocas y compatibles con el catálogo.
- **REL**: relaciones, dependencias y canales requeridos para invocar τ2 existen, están activos y conectan los componentes pertinentes.
- **COND**: condiciones/precondiciones de realizabilidad aplicables se satisfacen en el estado/contexto t.
- **AUTH**: autorización/credenciales pertinentes están vigentes y permiten el acceso focal.
- **RES**: recursos requeridos están disponibles o asignados a i en la ventana definida, sin asumir disponibilidad desde capacidad nominal.
- **DEP**: dependencias necesarias, incluidas externas, están dentro de la frontera o inventariadas y verificadas.
- **BLOCK**: no existe bloqueo, incompatibilidad o restricción activa que impida el acceso focal.
- **VALID**: evidencia, cobertura, temporalidad, identidad y versión del snapshot son suficientes para emitir un juicio.

A_f^*=0 solo cuando al menos un predicado necesario está respaldadamente incumplido y la cobertura permite descartar que otra ruta de invocación válida satisfaga la definición focal adoptada. Si no puede decidirse por falta de cobertura, conflicto de fuentes o granularidad incompatible, el estado verdadero se conserva como indeterminado en el DGP de referencia; el analizador reporta A_f,obs=?.

La definición es focal a τ2 y al contrato de acceso/invocación. No exige que exista una demanda concreta, que τ2 sea aplicable al estado S0, que alguien la conozca, seleccione o ejecute, ni que produzca Outcome/Value favorable.

## 63.3. Relación entre C_dep* y A_f*

C_dep* = C_install* ∧ C_integrity* ∧ C_compat* ∧ C_oper* sigue siendo el contrato de provisión técnica introducido en §62.

- C_dep*=0 implica que el mecanismo de provisión focal no ha satisfecho su contrato; no basta por sí solo para clasificar A_f*=0 si existe otra ruta válida de acceso a la misma τ2 dentro de la frontera.
- C_dep*=1 no implica A_f*=1: pueden fallar AUTH, RES, REL, COND, DEP, BLOCK o VALID.
- A_f*=1 puede existir sin que B1 haya sido recibido si otra provisión basal/alternativa hace τ2 accesible; esas unidades se tratan según elegibilidad basal y no se convierten retrospectivamente en aperturas.
- La atribución de un cambio A_f* a B requiere comparar potenciales bajo B0/B1 y separar vías alternativas; no se deduce de la coincidencia temporal.

Así se resuelve la posible lectura excesiva de la cadena de §62: C_dep* es un mediador técnico/proxy de mecanismo, nunca un sustituto definitorio de A_f*.

## 63.4. Aplicabilidad, ejecución y estados de acceso

Se mantienen separadas:

- **A_f***: τ2 está disponible y realizable como transformación accesible bajo el contrato focal.
- **App_f**: τ2 es aplicable al estado inicial S0 y a la demanda/objetivo concreto.
- **Know_f / Consider_f**: el agente conoce o considera τ2.
- **Select_f**: τ2 es seleccionada.
- **Exec_f**: τ2 se inicia o ejecuta.
- **Outcome/Value**: consecuencias observadas y valoración contextual.

Por tanto, son estados coherentes A_f*=1 con App_f=0, con Know_f=0, con Select_f=0 o con Exec_f=0. La no ejecución no prueba inaccesibilidad. Una ejecución observada no se usa para reconstruir retrospectivamente A_f*.

## 63.5. Medición observada y validación

El analizador recibe evidencia y snapshots; no recibe los campos de verdad del generador (A_f*, C_dep*, D_f*, T_acc* ni ΔT_acc*). Debe producir A_f,obs∈{1,0,?}, con:

- regla de clasificación versionada y ciega a Z/B, selección, ejecución, Outcome y Value;
- fuentes, timestamps, cobertura, identidad/versión, procedencia y hashes;
- matriz de desacuerdos y adjudicación independiente;
- sensibilidad/especificidad por brazo/versión/tiempo solo cuando una submuestra de validación con selección conocida permita estimarlas;
- si la validación es imperfecta, probabilidades desconocidas o no representativa, límites/análisis de sensibilidad, no estimaciones puntuales ficticias;
- propagación de incertidumbre de referencia y del propio analizador.

El evaluador conserva la verdad del DGP en un canal separado para calcular error de medición y sesgo. Nunca se filtra al analizador durante la clasificación.

## 63.6. Apertura focal D_f* y primera etapa

Se conserva la definición:

D_f^*(i)=I(A_{f,base}^*(i)=0 ∧ A_{f,post}^*(i)=1).

La elegibilidad primaria requiere A_f,base*=0 respaldado antes de Z. Si el estado basal es indeterminado, la unidad no se reclasifica como elegible confirmada; se informa en una categoría de incertidumbre conforme al protocolo de selección. Si A_f,base*=1, no existe apertura basal-post, aunque pueda existir accesibilidad focal.

Reportar separadamente:

- ITT_Df* = E[D_f*|Z=1]−E[D_f*|Z=0], calculable por el evaluador en simulación con verdad conocida;
- ITT_Df,obs, el contraste sobre la medición observada, con incertidumbre y corrección/límites según validación;
- tasa de C_dep*, para evaluar mecanismo de provisión;
- matriz de clasificación basal/post y errores diferenciales.

No sustituir ITT_Df* por ITT_Df,obs sin declarar el error. Una primera etapa sobre C_dep* no es primera etapa de accesibilidad.

## 63.7. ΔT_acc*: snapshots y diferencia estructurada

Para cada unidad i y tiempo t, el snapshot contiene al menos:

- U_acc: identidades canónicas/versiones de transformaciones y estado accesible/inaccesible/indeterminado;
- R_acc: relaciones tipadas/dirigidas, extremos, condiciones, estado y evidencia;
- C_acc: condiciones/configuraciones de realizabilidad, ámbito, temporalidad y procedencia;
- Validity: identidad, versión, evidencia, cobertura y estado epistémico;
- State/context: estado e historia necesarios para interpretar realizabilidad, sin usar Outcome/Value como criterio.

La diferencia basal-post se registra como:

ΔT_acc^*(i)=(ΔU, ΔR, ΔC, ΔValidity, ΔState).

Cada componente identifica altas, bajas, cambios de versión/definición, relaciones añadidas/retiradas/reconfiguradas, condiciones/configuraciones modificadas, cambios de validez/cobertura y variaciones relevantes del estado/contexto. Cada evento conserva objeto antes/después, momento, fuente, regla de comparación y evidencia.

Los snapshots solo se comparan si coinciden o se transforman explícitamente a una identidad/versionado, frontera, granularidad G, catálogo y reglas compatibles. De lo contrario, la diferencia es indeterminada o requiere una correspondencia versionada; no se fuerza un diff.

La proyección focal h_f(ΔT_acc*)=D_f* se permite únicamente bajo el contrato focal y snapshots comparables. No conserva cambios no focales. En consecuencia:

- D_f*=1 no implica ΔReach>0, selección, ejecución ni Value positivo.
- ΔT_acc*≠0 no implica D_f*=1.
- D_f*=0 no implica ΔT_acc*=0.
- La ausencia de cambio focal no autoriza a descartar cambios relacionales/configuracionales no focales.

## 63.8. Auditoría de atribución y vías alternativas

Para cada unidad se registran por separado los cambios en autorización, recursos, capacidad, información/conocimiento, dominio/precondiciones, dependencias, alternativas y bloqueos. Si B cambia una de estas vías además de la provisión focal, el tratamiento se reevalúa como paquete o efecto conjunto.

Una alternativa funcional puede mantener F* realizable sin τ2; esto no hace τ2 accesible ni inaccesible por sí solo. La accesibilidad de τ2 y la substituibilidad funcional de F* se adjudican como constructos separados. La ruta alternativa debe registrarse en el snapshot y en el universo/granularidad/horizonte declarados.

## 63.9. Criterios de aceptación y límites

Antes de congelar medición deben resolverse: definición exacta del contrato de invocación de τ2; predicados constitutivos por clase de transformación; frontera y cobertura; regla de ausencia respaldada frente a indeterminación; granularidad/catálogo/versionado; ventanas temporales; fuentes y estándares E1–E4; adjudicación; selección de validación; error diferencial; reglas para dependencias externas y alternativas; fixtures y pruebas adversariales.

**Dictamen:** se propone que A_f* sea un juicio estructural focal derivado de snapshots completos y predicados de realizabilidad; C_dep* es evidencia del mecanismo de provisión, no proxy suficiente. ΔT_acc* permanece estructurado y más amplio que D_f*. Esta especificación armoniza §§26.2, 43.3 y 58.6 sin cerrar XSYNC-138-03 ni AUD-001/004/005/007. OPEN-C10-005 y las decisiones de umbral/adjudicación permanecen abiertas. No hay freeze, implementación, simulación ni ejecución.


---

# 64. Clasificación temporal y causal de las condiciones de accesibilidad

**Estado:** propuesta de reconciliación; no aprobada ni congelada. No autoriza implementación, simulación o ejecución.  
**Dependencias:** §§30–31, 43, 53, 58–63; DGP §§2–22; AUD-010/011; XAUD-003/004/006; OPEN-C10-004/005.

## 64.1. Regla de clasificación

No se clasifica una variable nominal completa si agrupa componentes distintos. Cada registro debe identificar: constructo/componente, unidad, objeto τ2, nivel, tiempo, versión, estado, rol causal, fuente y política que puede modificarlo.

Hay que responder por separado:
1. ¿Es constitutiva de la accesibilidad focal?
2. ¿Cuándo se mide: antes de Z, después de Z o tras eventos posteriores?
3. ¿Qué rol causal desempeña en ese momento: basal, tratamiento recibido, mediador, co-intervención, confusor temporal, resultado o proceso de medición?
4. ¿Se utiliza para elegibilidad, definir A_f*, medir A_f,obs, explicar cumplimiento o estimar un efecto?

Una condición puede ser constitutiva de A_f* en sentido definicional y, a la vez, basal antes de Z o mediadora si cambia después de Z. El papel causal se indexa temporalmente.

## 64.2. Matriz temporal-causal candidata

| Componente | Antes de Z (t−1) | Después de Z (t1–t3) | Papel y cautela |
|---|---|---|---|
| Identidad/versión de τ2, dominio y frontera | Fijar identidad, tipo de objeto y frontera | Cambio exige nuevo snapshot y versionado | Un cambio inducido por B puede cambiar el objeto tratado; no mezclar versiones |
| C_install, C_integrity, C_compat, C_oper | Estado basal de provisión y elegibilidad | Estado post de provisión | Constitutivos de C_dep; C_dep post es mecanismo/mediador, no sustituto de A_f* |
| C_auth | C_auth,0 respaldada y satisfecha en población primaria | Medir C_auth,1; si B la cambia, es mediador/co-intervención | Constitutiva de acceso; en la provisión técnica focal debe permanecer invariante |
| Recursos | Separar stock, disponibilidad/asignación por unidad, demanda y consumo | Registrar disponibilidad/asignación post y consumo aparte | Disponibilidad puede ser constitutiva; consumo de ejecución no define acceso |
| Capacidad | Separar capacidad instalada, slots, disponibilidad temporal y carga | Registrar cada dimensión por tiempo | Capacidad instalada puede ser constitutiva; margen requerido por S0 es aplicabilidad; saturación puede generar interferencia |
| Información técnica | Configuración técnica integrada basal | Cambios de configuración inducidos por B | Puede ser constitutiva si habilita invocación; no confundir con formación o conocimiento del agente |
| Conocimiento, avisos, formación | Baseline descriptivo, nunca requisito de A_f* | Puede ser afectado por Z/B | Mediador de conocimiento/consideración, no covariable basal |
| Dominio/objeto | Compatibilidad del tipo de objeto fijada antes de Z | Cambio de objeto requiere nuevo contrato | Constitutiva si τ2 soporta el tipo; distinta de precondiciones de S0 |
| Precondiciones S0/demanda | Baseline de aplicabilidad | Reevaluar antes de cada transformación y rama | App_f, no A_f* |
| Relaciones, dependencias y bloqueos | Snapshot basal completo | Snapshot post-provisión y posteriores por evento | Parte de A_f*/T_acc; registrar cambios focales y no focales |
| Alternativas F* | Clasificar antes de Z en universo, granularidad y horizonte fijados | Registrar si B las activa o modifica | Substituibilidad funcional separada de acceso a τ2 |
| Selección, inicio y ejecución | No usar para elegibilidad | Eventos downstream | No constituyen accesibilidad; cambios posteriores generan snapshots nuevos |
| Outcome y Value | Regla, beneficiario y horizonte fijados ex ante | Medición posterior | Nunca definen A_f* ni sus predicados |
| Evidencia, cobertura y medición | Protocolo, fuentes, cegamiento fijados | Evidencia por tiempo; cambios de cobertura registrados | VALID es requisito epistémico del juicio, no condición causal del sistema; error diferencial puede sesgar A_f,obs |

## 64.3. Contrato temporal

Se conserva el reloj DGP:
- **t−1:** sellar frontera, versión τ2, población, q_X*, P*_τ2/P*_F, alternativas, condiciones basales, A_f,base*, T_acc,base*, reglas de medición y elegibilidad.
- **t0:** asignar Z y registrar probabilidad.
- **t1:** registrar B asignada/recibida, versión, actor, intento y desviaciones.
- **t2:** verificar instalación, integridad, compatibilidad y operación; registrar aparte C_auth, recursos, capacidad, información y co-intervenciones.
- **t3:** generar snapshot post; calcular A_f,post* en canal de verdad y A_f,obs en canal independiente; evaluar App_f por separado, antes de conocimiento, selección, inicio y ejecución.
- **t4:** derivar Reach_H y trayectorias candidatas desde T_acc y reglas de composición.
- **t5:** medir conocimiento y consideración.
- **t6:** medir selección e inicio.
- **t7:** registrar ejecución parcial/completa, interrupción, fallo y razón.
- **t8:** medir Outcome.
- **t9:** evaluar Value bajo regla independiente.
- **t+1…:** eventos que cambien el sistema crean snapshots nuevos e inmutables; nunca sobrescribir t3.

El orden temporal es un contrato de medición, no prueba de identificación causal. Registrar timestamps/eventos reales cuando varias condiciones cambien dentro de una ventana.

## 64.4. Elegibilidad y no ajuste postratamiento

1. P*_τ2 requiere A_f,base*=0 respaldada antes de Z y soporte/factibilidad de ambas políticas.
2. Baseline indeterminado no se convierte en 0 ni en elegibilidad confirmada.
3. Una condición constitutiva que cambia después de Z pasa a ser mediador/co-intervención potencial; no covariable basal.
4. No ajustar el ITT por C_dep, C_auth, recursos, capacidad, información, A_f, D_f, conocimiento, Reach, selección o ejecución medidos después de Z para reclamar un efecto directo.
5. Ese ajuste puede bloquear mediación o abrir sesgo por collider/confusión inducida por tratamiento.
6. Si existen confusores temporales afectados por tratamiento que influyen en mediador y resultado, la descomposición exige estimandos y métodos longitudinales explícitos; una regresión convencional no basta.
7. Si B cambia condiciones adicionales, conservar el ITT como efecto de política/paquete y separar atribución mediante factorialización, intervención adicional o identificación defendible.
8. VALID/cobertura pertenece al proceso de medición. Si B afecta la observabilidad, modelar missingness/error diferencial.

## 64.5. Reconciliación de §§59, 62 y 63

§59 aporta la matriz de clasificación; §63 define el juicio estructural de A_f*; §62 define B como provisión técnica focal. Para el escenario primario candidato:
- C_dep puede cambiar por B.
- C_auth, recursos, capacidad no focal, información no focal y dominio deben estar fijados/satisfechos antes de Z y mantenerse invariantes, salvo decisión explícita.
- Si cambian post-Z, registrar el cambio como mediador/co-intervención; no ocultarlo dentro de C_dep ni ajustar automáticamente por él.
- A_f,post* se deriva de los predicados del §63, no de la fórmula histórica con C_other.
- App_f y precondiciones S0 quedan fuera de la definición de accesibilidad.
- VALID determina si puede emitirse un juicio; no es una condición causal del sistema.

**Inconsistencia B aún abierta:** §62 describe B0 como ausencia de provisión y B1 como aplicación del protocolo; DGP §3.1 conserva B_g0/B_g1 como políticas probabilísticas con probabilidades objetivo ilustrativas .20/.80, y §3.2 separa intento de éxito. No asumir que son equivalentes. Antes de congelar B hay que decidir si son políticas estocásticas de distinta intensidad o brazos deterministas con incumplimiento estocástico, y alinear asignación, recepción, intento, éxito, C_dep, q_X* y estimandos. No recalibrar .20/.80 por intuición.

**Inconsistencia de autorización:** la propuesta histórica de resolución AUD-001/002 contiene una modalidad de intervención sobre C_auth; el escenario actual trata C_auth como basal/invariante y manipula provisión técnica. Son diseños distintos. La modalidad de autorización se conserva como alternativa histórica/adversarial y no se mezcla con el primario sin decisión explícita.

## 64.6. Dictamen

La clasificación temporal-causal queda organizada como propuesta coherente con §§59, 62 y 63. No se considera cerrada AUD-011 ni XAUD-003/004/006. La semántica de B y la alternativa histórica de autorización siguen sin reconciliar. OPEN-C10-004/005 permanecen abiertos. No hay freeze, implementación, simulación ni ejecución.


---

# 65. Reconciliación semántica y generativa de la política B: D1 principal condicionado y D2 contraste

**Estado:** propuesta de reconciliación documental basada en §§53.4–53.5 y 54.1–54.7; no aprobada ni congelada. No autoriza implementación, simulación o ejecución.  
**Dependencias:** §§21, 23, 30–31, 53–54, 62–64; DGP §§3.1–3.2, 21–24; DEC-C10-022/024; OPEN-C10-001/005.

## 65.1. Hallazgo y regla de precedencia

La auditoría confirma que la aparente contradicción no debe resolverse eligiendo entre «política estocástica» y «brazo determinista con incumplimiento» como si fueran las únicas opciones. El diseño ya contiene dos escenarios distintos:

- **D1:** comparador ordinario con provisión focal de baja frecuencia frente a provisión programada; escenario principal condicionado.
- **D2:** control sin provisión focal frente a provisión programada; contraste de diseño.

La precedencia operativa candidata es: §53.4 fija el estatus de D1/D2; §54 concreta la factorización de intentos y éxito; §62 y DGP §21 describen la variante sin provisión en control y deben leerse como D2, no como definición universal de B0/B1. DGP §3.1 debe leerse como objetivo de estado técnico final verificado C_dep, no como probabilidad de intento.

Se conserva el texto histórico; esta sección aclara su alcance y no lo borra.

## 65.2. Parámetros separados por nivel

| Cantidad | D1 principal condicionado | D2 contraste | Interpretación |
|---|---:|---:|---|
| C_dep,base | 0 | 0 | Ausencia basal pre-Z |
| P(W_attempt=1 | Z=0) | .25 | 0 | Probabilidad de intento bajo control |
| P(W_attempt=1 | Z=1) | 1.00 | 1.00 | Intento programado bajo tratamiento |
| P(S_success=1 | W_attempt=1) | .80 | .80 | Éxito técnico conjunto condicional propuesto |
| P(C_dep,post=1 | Z=0) | .20 | 0 | Estado final técnico verificado |
| P(C_dep,post=1 | Z=1) | .80 | .80 | Estado final técnico verificado |
| Primera etapa de C_dep | .60 | .80 | Diferencia entre probabilidades finales |

En la factorización candidata, y si no hay intentos sin registro ni estados finales por otras rutas:

[
P(C_{dep}=1mid Z=z,D)=P(W_{attempt}=1mid Z=z,D)	imes P(S_{success}=1mid W_{attempt}=1,D)
]

No se presupone independencia entre componentes de C_dep. El .80 de éxito condicional es una propuesta algebraica de §54, no un parámetro recuperado literalmente ni un dato empírico; requiere aceptación y especificación técnica.

## 65.3. Definición de las versiones de política

- **D1, control ordinario:** el mismo procedimiento/módulo focal se intenta con probabilidad .25; el éxito conjunto condicional candidato es .80.
- **D1, tratamiento:** el mismo procedimiento se programa para todas las unidades elegibles (intento objetivo 1.00); el éxito conjunto condicional candidato es .80.
- **D2, control sin provisión:** no se inicia el intento focal (0); no se retira ninguna capacidad basal.
- **D2, tratamiento:** provisión programada para todas las unidades elegibles (intento objetivo 1.00); éxito conjunto condicional candidato .80.

Dentro de cada escenario, el módulo, versión, protocolo, recursos por intento, actor/automatización, verificación, soporte y condiciones no focales deben ser comunes. La diferencia asignada es la frecuencia del intento focal. Z asigna la política; W_attempt, S_success, C_dep, A_f* y D_f* son resultados/estados posteriores distintos.

## 65.4. Condición para mantener D1 como primario

D1 permanece como **principal condicionado**, no como elección irrevocable. Antes de aprobarlo se debe justificar que la provisión ordinaria de control (25% de intentos; 20% de estados técnicos finales bajo la factorización propuesta) es parte del comparador científicamente legítimo y no contaminación, co-intervención o política externa al contraste pretendido.

Si esa justificación falla, D2 puede pasar a ser el escenario primario mediante decisión explícita; no se cambia silenciosamente el estimando ni se reetiqueta D1.

D2 conserva utilidad como contraste más limpio de ausencia frente a provisión, pero su primera etapa y población de contraste son distintas.

## 65.5. Qué se identifica y qué no

Las probabilidades .20/.80 se refieren primero a C_dep, estado técnico verificado. No se transfieren automáticamente a A_f* ni D_f*. Para que la primera etapa focal sea .60 en D1 o .80 en D2, las demás condiciones de accesibilidad deben estar satisfechas en la población de apertura y la definición estructural de §63 debe confirmarlo. En caso contrario, se calcula:

[
P(A_{f,post}^*=1mid Z=z,D)
quad	ext{y}quad
ITT_{D_f^*}
]

desde todos los predicados, sin sustituirlos por C_dep.

El ITT por Z estima el efecto de asignación a la política concreta. LATE_f/Wald requiere por separado relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición válida. Si D1 produce vías no focales, su ITT es efecto de política/paquete; no se atribuye automáticamente a accesibilidad.

## 65.6. Reconciliación de textos previos

1. DGP §3.1: p0=.20 y p1=.80 son objetivos de probabilidad final verificada C_dep, no probabilidades de intento.
2. DGP §3.2: ω_z/s_z deben parametrizarse para reproducir la tabla D1/D2; no se asignan automáticamente .20/.80 a W_attempt.
3. DGP §21 y maestro §62: la descripción «B0 sin provisión / B1 provisión programada» corresponde a D2.
4. Maestro §54 y DGP §24 (esta sección) detallan la factorización D1/D2; no sustituyen los estados separados de asignación, oferta, recepción, intento, éxito y verificación.
5. Maestro §64.5 y DGP §23 registraron correctamente la discrepancia en ese momento. Esta sección resuelve la ambigüedad semántica principal, pero no aprueba el comparador D1 ni el .80 condicional.

## 65.7. Pendientes que siguen abiertos

- Justificación científica del control ordinario D1 y decisión de mantener D1 como primario.
- Identidad/hash del módulo, actor/automatización, disparador de intento y evidencia de recepción.
- Especificación conjunta de C_install/C_integrity/C_compat/C_oper y validación del .80 condicional.
- Crossover, contaminación, rollback, intentos parciales, fallos e indeterminación.
- Calibración de A_f* desde todos sus predicados y cálculo de la primera etapa verdadera.
- Revisión independiente de exclusión y compatibilidad con C10-D1/S4-R.
- Aprobación expresa de OPEN-C10-001/005 antes de freeze o ejecución.

**Dictamen:** la semántica D1/D2 y la distinción intento/éxito/estado final quedan reconciliadas documentalmente como propuesta. No se acepta todavía D1 como comparador definitivo, no se cierra OPEN-C10-001/005 y no se autoriza implementación, simulación ni ejecución.


---

# 66. Adjudicación del comparador D1/D2: objetivo del contraste y regla de selección

**Estado:** auditoría de diseño y recomendación condicionada; no constituye decisión aprobada ni freeze.  
**Base:** §§52.2–52.4, 53.4–53.9, 54.1–54.7 y 65; DGP §§3.1–3.4, 21–25; S4-R §§17–18.  
**Pregunta:** qué comparador responde al objetivo científico del experimento sintético C10-S sin confundir efecto de política con efecto atribuible a accesibilidad.

## 66.1. Hallazgo de la auditoría

La recuperación histórica recomienda D1 como principal solo si se justifica que la provisión focal de baja frecuencia en control forma parte del régimen ordinario relevante. La documentación disponible conserva los valores D1 (.25 intentos; .20 estado técnico final) y D2 (0 intentos; 0 estado técnico final), pero no aporta todavía una fuente externa, institucional o empírica que establezca que .25/.20 representa un régimen ordinario objetivo para la población del experimento.

Por tanto, la condición que permitiría elevar D1 a comparador principal no está satisfecha en el expediente actual. La recomendación histórica se conserva como condicional, no como una selección vigente.

## 66.2. Dos objetivos científicos diferentes

| Objetivo del contraste | D1 | D2 |
|---|---|---|
| Efecto incremental frente a una política ordinaria de provisión | Adecuado si el régimen ordinario está justificado ex ante | No representa ese contraste |
| Efecto de introducir provisión focal frente a no iniciarla | Contraste atenuado por provisión basal post-Z | Contraste directo entre provisión programada y ausencia de intento focal |
| Primera etapa objetivo de C_dep | .60 | .80 |
| Interpretación | Cambio de intensidad de una política existente | Apertura de provisión focal frente a no provisión focal |
| Requisito decisivo | Justificar la política ordinaria de control | Justificar que ausencia de provisión es el comparador pertinente |

La diferencia no es simplemente potencia estadística. D1 y D2 definen políticas, contrastes y poblaciones de cumplidores potencialmente distintos.

## 66.3. Recomendación para el experimento sintético mecanístico

Mientras no exista una justificación verificable del régimen ordinario D1, recomiendo:

1. Mantener **D2 como candidato preferente a contraste primario** para el experimento sintético cuyo objetivo es aislar la apertura de la provisión focal frente a ausencia de intento.
2. Mantener **D1 como escenario secundario de política incremental**, útil para evaluar qué ocurre cuando la provisión focal ya existe con baja frecuencia en el control.
3. No denominar «contaminación» a la provisión de control D1 cuando forma parte de la política B_g0^D1 asignada y preespecificada. La contaminación/crossover se reserva para recepción de componentes o versiones fuera de la política asignada.
4. No combinar ni promediar los ITT de D1 y D2 como si fueran el mismo estimando.
5. No asumir que los Wald/LATE de ambos escenarios representan el mismo estrato de cumplidores: cada contraste induce una primera etapa y una población de cumplidores potencialmente distintas.

Esta recomendación es una regla de diseño provisional. D2 no queda seleccionado ni aprobado por esta sección.

## 66.4. Gates para aceptar D1 como primario

D1 solo podrá pasar a primario si, antes de congelar el DGP, se documenta:

- el régimen ordinario concreto que representa la provisión de control;
- la fuente y justificación de la frecuencia de intento .25 y del estado final .20, sin derivarlas circularmente de Outcome o Value;
- la población, periodo y contexto a los que esa política ordinaria es transportable;
- la equivalencia de módulo, versión, protocolo, actor, recursos por intento y verificación entre brazos;
- que la diferencia asignada se limita a la frecuencia de intento y que cualquier vía colateral queda identificada como efecto de paquete;
- la definición de crossover y la evidencia que distinguirá provisión ordinaria asignada de recepción fuera de política.

Si esos gates no se satisfacen, D1 permanece escenario secundario y no puede llamarse comparador ordinario validado.

## 66.5. Gates para aceptar D2 como primario

D2 podrá pasar a primario si se confirma ex ante que:

- el estimando de interés es provisión focal programada frente a ausencia de intento focal bajo control;
- C_dep,base=0 y A_f,base*=0 están verificados antes de Z en la población de apertura;
- no existe provisión focal de fondo omitida ni ruta técnica equivalente que haga falso el control «sin provisión»;
- las condiciones no focales, recursos y reglas de ejecución permanecen comunes;
- no hay interferencia o spillover no modelado;
- se preservan por separado intento, éxito técnico, C_dep, A_f*, D_f*, aplicabilidad y ejecución.

Si el control no puede sostener ausencia de provisión, D2 no es el contraste implementado y deberá declararse desviación o crossover, no recodificarse retrospectivamente.

## 66.6. Estimandos y límites de interpretación

Definir, para cada escenario d en {D1,D2}, el ITT de política:

[
ITT_d = E[V | Z=1, D=d] − E[V | Z=0, D=d]
]

y análogamente para Outcome y cada dimensión de Value preespecificada. El ITT_D1 responde al cambio entre provisión ordinaria y programada; el ITT_D2 responde a provisión programada frente a ausencia de intento focal.

La primera etapa se estima separadamente para C_dep, A_f,post*, D_f y el ΔT_acc completo. No sustituir una por otra. Los Wald/LATE se estiman por escenario y solo bajo sus supuestos; no se transportan ni agrupan automáticamente entre D1 y D2.

La asignación Z identifica el efecto de la política asignada bajo aleatorización y consistencia, pero no prueba por sí sola que el efecto opere exclusivamente a través de accesibilidad. Una vía colateral mantiene la interpretación como efecto de paquete y bloquea la atribución focal que requiera exclusión.

## 66.7. Estado resultante

- Semántica D1/D2: reconciliada documentalmente.
- Legitimidad empírica del régimen ordinario D1: no acreditada en el expediente actual.
- Recomendación provisional: D2 preferente para el contraste mecanístico; D1 como escenario incremental secundario.
- Selección del escenario primario: ABIERTA, pendiente de aceptación científica explícita.
- .80 de éxito condicional: sigue siendo hipótesis de factorización, no parámetro validado.
- OPEN-C10-001/005: permanecen ABIERTAS.
- No freeze, implementación, simulación ni ejecución.


---


---

# 67. Calibración de la primera etapa técnica y derivación estructural de accesibilidad focal

**Estado:** propuesta de diseño y reconciliación matemática; NO aprobada, NO congelada.  
**Dependencias:** §§58–66; DGP §§17–25; AUD-001/004/005/007/010/011; XAUD-003/004/006; OPEN-C10-001/007/008.

## 67.1. Cuatro componentes técnicos y definición de C_dep

Para cada intento focal se registran cuatro predicados verdaderos del DGP, binarios y versionados:

- `C_install*`: instalación efectiva del artefacto/dependencia correspondiente a la identidad y versión autorizadas de τ2.
- `C_integrity*`: integridad verificada del artefacto y configuración; identidad, hash y configuración corresponden a lo autorizado.
- `C_compat*`: compatibilidad de interfaces, dependencias y versiones con el contrato del sistema y dominio.
- `C_oper*`: disponibilidad operativa del canal técnico requerido para invocar la dependencia, sin exigir que τ2 sea seleccionada ni ejecutada.

La dependencia técnica focal queda verificada si y solo si:

`C_dep* = C_install* AND C_integrity* AND C_compat* AND C_oper*`.

Los cuatro predicados son conjuntamente necesarios para esta ruta técnica. No se presupone independencia estadística, igualdad de tasas marginales ni que el estado de un componente determine los demás.

La verdad del DGP conserva estados 0/1. La observación de cada componente conserva 1/0/?:
- `C_dep,obs=1`: los cuatro componentes están respaldados como 1.
- `C_dep,obs=0`: al menos uno está respaldado como 0.
- `C_dep,obs=?`: no hay componente respaldado como 0, pero al menos uno es desconocido, no observado o contradictorio.

No se clasifica la conjunción como 1 por promedio, mayoría, éxito parcial, intento, instalación declarada o ausencia de registro de fallo. Un componente desconocido no se recodifica como fallo verdadero.

## 67.2. Éxito condicional 0,80: significado y límite

La cifra candidata se define como:

`s = P(C_dep*=1 | W_attempt=1, E=1, D=d, H)`,

donde E identifica población/historias elegibles y H fija contexto, versión, protocolo, actor, recursos por intento y ventana de verificación.

El 0,80 significa **probabilidad conjunta de que los cuatro componentes técnicos resulten satisfechos tras un intento elegible**. No significa que cada componente tenga probabilidad 0,80 ni que la probabilidad conjunta sea el producto de cuatro probabilidades marginales.

La cifra se eligió hasta ahora para reproducir algebraicamente los estados finales documentados (.20/.80 en D1 y 0/.80 en D2). No procede de medición empírica, fuente externa, fiabilidad de ingeniería ni calibración de datos. Por tanto:
- se conserva como **parámetro sintético candidato**, no como tasa validada;
- no puede presentarse como evidencia de que un procedimiento real alcanza 80 %;
- un DGP reproducible debe especificar una distribución conjunta de los cuatro componentes o un mecanismo generador equivalente, con sus dependencias;
- una calibración empírica futura necesitaría intentos elegibles observados, denominador definido, ventana de verificación, protocolos/versiones comparables y adjudicación independiente de cada componente.

No se impone 0,80 a cada componente ni se ajusta retrospectivamente para producir el efecto deseado. La sensibilidad debe explorar valores alternativos de s y estructuras de dependencia antes de cualquier congelación.

## 67.3. De C_dep a accesibilidad: predicados estructurales completos

La accesibilidad focal verdadera no se define por C_dep aisladamente. Para τ2 y la unidad/historia/tiempo especificados se propone:

`A_f* = I(ID_f* AND REL_f* AND COND_f* AND AUTH_f* AND RES_f* AND DEP_f* AND NOT BLOCK_f*)`.

Donde:
- `ID_f*`: identidad, tipo y versión de τ2 están determinados y corresponden al objeto del contrato.
- `REL_f*`: existen las relaciones, interfaces y dependencias requeridas para invocar/componer τ2.
- `COND_f*`: se satisfacen las condiciones constitutivas de realizabilidad de τ2, sin incorporar por defecto las precondiciones del estado actual S0.
- `AUTH_f*`: existe autorización válida para la unidad, actor, objeto y ventana definidos.
- `RES_f*`: los recursos necesarios están disponibles/asignados ex ante en el nivel pertinente; el consumo posterior de ejecución no define acceso.
- `DEP_f*`: existe al menos una ruta técnica/dependencia completa y válida que soporta τ2.
- `BLOCK_f*`: existe un bloqueo efectivo que impide la invocación bajo el contrato.

**Distinción de ruta:** en el DGP primario aislado se postula una única ruta focal inventariada, por lo que `DEP_f*=C_dep*`. En el contrato general, `DEP_f*` representa la existencia de al menos una ruta válida entre las rutas admisibles. Por ello, `C_dep*=0` no implica universalmente `A_f*=0`: podría existir otra ruta válida que invoque la misma τ2. Esta posibilidad se mantiene como control adversarial MEAS-02 y debe quedar excluida por inventario/cobertura, no por suposición verbal, si se quiere interpretar D2 como ausencia de provisión focal.

`VALID_f`, cobertura y calidad de evidencia **no forman parte de la verdad estructural causal** de `A_f*`. Son requisitos epistémicos para clasificar `A_f,obs`. Así se evita que falta de evidencia cambie retroactivamente el estado verdadero del sistema.

Tampoco se incorpora `App_f`: accesibilidad no implica que las precondiciones del estado S0 permitan aplicar τ2 en ese momento. Aplicabilidad, conocimiento, consideración, selección, inicio y ejecución siguen siendo estados separados.

## 67.4. Primeras etapas de C_dep, A_f y D_f

Para cada escenario d en {D1,D2}, reportar separadamente:

- `FS_Cdep,d = P(C_dep,post*=1 | Z=1,d,E) - P(C_dep,post*=1 | Z=0,d,E)`.
- `FS_Af,d = P(A_f,post*=1 | Z=1,d,E) - P(A_f,post*=1 | Z=0,d,E)`.
- `FS_Df,d = P(D_f*=1 | Z=1,d,E) - P(D_f*=1 | Z=0,d,E)`.

Conservar además la diferencia entre brazos en cada componente técnico y en el cambio estructurado completo ΔT_acc; no reducir ΔT_acc a un indicador binario.

Si la población elegible tiene `A_f,base*=0`, la ruta técnica focal es única y completa, y todos los predicados no técnicos de accesibilidad permanecen satisfechos e invariantes, entonces `A_f,post*=C_dep,post*` y `D_f*=C_dep,post*`. **Solo bajo esas estipulaciones** las primeras etapas coinciden:
- D1: `FS_Cdep=FS_Af=FS_Df=.80-.20=.60`.
- D2: `FS_Cdep=FS_Af=FS_Df=.80-0=.80`.

Si los predicados no técnicos varían, hay rutas alternativas, bloqueos, snapshots incompatibles o elegibilidad basal incierta, no se transfieren esas cifras a A_f* o D_f*. En general, para la ruta única:

`P(A_f,post*=1 | Z=z,d,E) = P(C_dep,post*=1 AND G_f*=1 | Z=z,d,E)`,

donde G_f* es la conjunción de los demás predicados estructurales y ausencia de bloqueo. La probabilidad conjunta debe calcularse; no puede reemplazarse por el producto de marginales sin una hipótesis de independencia justificada.

`D_f*=I(A_f,base*=0 AND A_f,post*=1)`. Por tanto, la primera etapa de A_f,post* y la de D_f* solo coinciden en la población con inaccesibilidad basal verdadera confirmada. Si se mezclan unidades con accesibilidad basal, se informan ambas sin intercambiarlas.

## 67.5. Fallos, parcialidad, indeterminación y verificación desconocida

| Situación | Estado técnico verdadero | Clasificación observada | Consecuencia analítica |
|---|---|---|---|
| Intento no iniciado | W=0 | intento no realizado, no fallo de componente | Mantener Z; C_dep no se presume 1 |
| Intento iniciado y un componente falla | C_dep*=0 | 0 si el fallo está respaldado | No hay éxito de la ruta técnica focal |
| Uno o más componentes desconocidos, ninguno fallido | Truth DGP oculta; observación incompleta | C_dep,obs=? | No recodificar como 0 ni 1; sensibilidad/límites |
| Cuatro componentes respaldados | C_dep*=1 | C_dep,obs=1 | Solo acredita dependencia técnica |
| C_dep*=1 pero AUTH/RES/REL/COND/BLOCK no satisfacen acceso | A_f*=0 | A_f,obs=0 si hay evidencia suficiente; si no, ? | No declarar apertura de τ2 |
| C_dep*=0 y existe otra ruta válida | DEP_f*=1 puede mantenerse | Depende de cobertura de rutas | A_f* puede ser 1; no inferir inaccesibilidad desde C_dep |
| Snapshots/versiones no comparables | ΔT_acc* no adjudicable bajo diff actual | ? o correspondencia versionada | No calcular D_f por comparación forzada |
| Evidencia insuficiente o contradictoria | Truth permanece separada | A_f,obs=? | INDETERMINATE; no elegibilidad confirmada |

Los fallos, reintentos, rollback, crossover y tiempos se conservan como eventos. La asignación Z no cambia por cumplimiento. El ITT se calcula por asignación; el análisis de accesibilidad verdadera y el de accesibilidad observada se mantienen separados.

## 67.6. Contrato de observación y protección contra filtración

El generador conserva los valores verdaderos de cada componente, C_dep*, A_f*, D_f*, rutas, bloqueos y ΔT_acc*. El analizador recibe evidencia observable, snapshots y estados 1/0/?; no recibe truth ni parámetros generadores. El evaluador independiente compara la salida congelada del analizador con truth después del análisis.

La cobertura/validez se evalúa por predicado, ruta, unidad, tiempo y versión. Una ausencia de evidencia se distingue de evidencia de ausencia. Los errores de clasificación deben estimarse o acotarse por brazo, componente y escenario; si la validación no identifica sensibilidad/especificidad, se reportan límites/sensibilidad y no una corrección puntual ficticia.

## 67.7. Dictamen y pendientes

Queda formalizada la lógica de la conjunción técnica y su relación no suficiente con accesibilidad. No queda validado el 0,80, ni la distribución conjunta de componentes, ni la exclusividad de la ruta focal en un sistema real. D2 sigue siendo candidato preferente recomendado, no escenario primario seleccionado. D1 conserva su papel incremental secundario hasta justificar el régimen ordinario.

Permanecen abiertos: protocolo/actor/versiones de intento; distribución conjunta y sensibilidad de los cuatro componentes; inventario de rutas alternativas y cobertura; adjudicación E1–E4; clasificación de predicados por tipo de τ2; error diferencial; snapshots comparables; q_X*/soporte; política B y escenario primario; Value y exclusión. No se cierra OPEN-C10-001/007/008, AUD-001/004/005/007/010/011 ni XSYNC-138-03/04/06. No hay freeze, implementación, simulación, ejecución ni autorización empírica.


---

# 68. Distribución conjunta de componentes técnicos y sensibilidad del éxito condicional

**Estado:** propuesta de especificación probabilística del DGP; no aprobada ni congelada.  
**Dependencias:** §67; DGP §26; DEC-C10-027; ACC-01…20.  
**Pregunta:** ¿qué estructura probabilística completa genera los estados de los cuatro componentes, y qué puede inferirse del parámetro conjunto s?

## 68.1. Objeto probabilístico completo

Orden fijo de componentes: (C=(C_{install},C_{integrity},C_{compat},C_{oper})). Para cada intento elegible, el DGP debe definir un vector binario conjunto y sus 16 patrones posibles:

[
p_{abcd}=P(C_{install}=a,C_{integrity}=b,C_{compat}=c,C_{oper}=dmid W_{attempt}=1,E,D,H),
quad a,b,c,din{0,1}.
]

Restricciones:
- (p_{abcd}geq0) para los 16 patrones;
- (sum_{a,b,c,d}p_{abcd}=1);
- (s=p_{1111});
- la distribución es específica del régimen D, protocolo, versión, actor, recursos y ventana H, salvo que se imponga y justifique invariancia;
- los cuatro componentes se generan una sola vez por intento, con trazabilidad de reintentos y dependencia temporal explícita si hay más de uno.

El parámetro s fija una sola celda de la distribución. No identifica las otras 15 celdas, las cuatro tasas marginales, las dependencias por pares ni el patrón de fallos parciales. Por tanto, s=.80 no constituye por sí solo un DGP completo.

## 68.2. Demostración de no identificación de fallos parciales

Dos distribuciones ilustrativas pueden compartir (s=.80) y producir diagnósticos radicalmente distintos:

| Patrón | Distribución A | Distribución B |
|---|---:|---:|
| 1111 (todos correctos) | .80 | .80 |
| 0111 (falla instalación) | 0 | .05 |
| 1011 (falla integridad) | 0 | .05 |
| 1101 (falla compatibilidad) | 0 | .05 |
| 1110 (falla operación) | 0 | .05 |
| 0000 (todos fallan) | .20 | 0 |
| Otros 10 patrones | 0 | 0 |

Ambas tienen la misma probabilidad conjunta de éxito técnico. Sin embargo, A representa un choque común que hace que todos los componentes funcionen o fallen conjuntamente; B representa cuatro fallos parciales mutuamente excluyentes, con cada componente marginalmente correcto en .95. No son equivalentes en diagnóstico, reparación, observabilidad ni transportabilidad.

Esto demuestra que fijar s no permite inferir qué componente causa el fracaso ni la frecuencia de fallos parciales. Los patrones de fallo deben ser generados y reportados, no ocultados bajo un único indicador C_dep.

## 68.3. Límites marginales y dependencia

Si se conocen o se proponen marginales (m_i=P(C_i=1mid W=1,E,D,H)), la probabilidad conjunta satisface los límites de Fréchet:

[
max(0,sum_{i=1}^{4}m_i-3)leq sleqmin_i m_i.
]

Por ejemplo, (m_i=.95) para los cuatro componentes permite (s=.80) en el límite inferior; la distribución B de §68.2 es compatible. En cambio, si cada marginal fuese .80, s=.80 también sería un extremo superior y exigiría una estructura de dependencia muy fuerte. Bajo independencia con cuatro marginales .80, (s=.80^4=.4096), no .80.

Estos ejemplos son demostraciones matemáticas, no parámetros seleccionados para el DGP. No se debe imponer independencia, ni deducir marginales desde s, ni usar Fréchet como si identificara la distribución.

## 68.4. Familias de sensibilidad que debe cubrir el diseño

Antes de elegir una distribución confirmatoria, el protocolo de sensibilidad debe incluir, como mínimo:

1. **Choque común / dependencia positiva extrema:** los componentes tienden a tener el mismo estado; permite separar fallos sistémicos de fallos aislados.
2. **Fallos parciales dispersos:** masa en patrones con uno o dos componentes fallidos; evalúa capacidad de diagnóstico y medición.
3. **Bottleneck:** un componente concentra la mayor parte de fallos, variando cuál es el limitante.
4. **Dependencia mixta:** coocurrencia de algunos fallos y fallos idiosincráticos; especificar mediante tabla 16-celdas o modelo generador identificable.
5. **Heterogeneidad entre intentos/unidades:** probabilidades distintas por estrato basal o clase de unidad, sin condicionar en variables post-asignación que formen parte del efecto.
6. **Deriva temporal/versiones:** cambios en la distribución conjunta entre versiones o periodos; no agrupar versiones no equivalentes sin modelo explícito.

Para cada familia se debe fijar la tabla de 16 celdas, o parámetros suficientes para reconstruirla, antes de generar resultados. Deben informarse s, cuatro marginales, fallos parciales por patrón, asociaciones y probabilidad de cero/dos/tres componentes fallidos. No basta reportar C_dep.

## 68.5. Sensibilidad del valor s y separación de regímenes

La cuadrícula (sin{.60,.70,.80,.90}) se propone únicamente como malla exploratoria inicial. Debe ampliarse o reemplazarse según la pregunta científica y no convierte .80 en valor central validado.

Para cada s y familia conjunta:
- recalcular la distribución de patrones respetando no negatividad y suma uno;
- conservar constantes solo los parámetros que el diseño declare invariantes;
- volver a calcular (FS_{Cdep}), (FS_{Af}), (FS_{Df}) y los cambios por componente para D1 y D2 por separado;
- registrar si el cambio de s afecta solo éxito tras intento o también la probabilidad/intensidad de intento, recursos, autorización, rutas alternativas o vías colaterales;
- no comparar Wald/LATE entre distribuciones como si conservaran la misma población de cumplidores.

La malla .60/.70/.80/.90 no debe confundirse con la primera etapa .60/.80 previamente derivada para D1/D2. Una es sensibilidad del éxito condicional por intento; la otra es una diferencia entre brazos en una variable post bajo supuestos concretos.

## 68.6. Contrato de generación y reporte

Cada ejecución futura autorizada tendría que registrar, por escenario y réplica:
- semilla y versión del generador;
- vector de parámetros y tabla completa (p_{abcd});
- denominador de intentos elegibles y no intentos;
- conteo de los 16 patrones y tasa de C_dep;
- marginales y asociaciones de componentes;
- reintentos, orden, tiempo, rollback y versión;
- heterogeneidad por estrato preespecificado;
- truth separada de evidencia observada para evitar filtración.

El analizador no recibe (p_{abcd}), s, truth de componentes ni estado verdadero C_dep/A_f/D_f. El evaluador independiente los utiliza después de cerrar la salida del analizador.

## 68.7. Dictamen y decisiones no tomadas

Queda demostrado que s=.80 no identifica la distribución de fallos parciales. El DGP necesita una tabla conjunta de 16 patrones o un generador equivalente explícito. Las familias y la cuadrícula de sensibilidad son propuestas para diseñar pruebas, no decisiones confirmatorias.

No se selecciona una distribución, no se fija s, no se aprueba independencia ni una estructura de dependencia, no se selecciona D1/D2 como primario y no se valida empíricamente el mecanismo. Siguen abiertas la calibración con datos, la heterogeneidad, el protocolo de intentos, la observación de fallos, las rutas alternativas y la revisión independiente. No hay freeze, implementación, simulación ni ejecución.


---

# 69. Fixtures conjuntos explícitos y propagación de sensibilidad a las primeras etapas

**Estado:** propuesta matemática de fixtures del DGP; no aprobada ni congelada.  
**Dependencias:** §§67–68; DGP §§26–27; DEC-C10-028.  
**Propósito:** pasar de familias cualitativas a tablas de probabilidad válidas y comprobar cómo la variación de s afecta a las primeras etapas bajo políticas de intento distintas.

## 69.1. Cuatro fixtures explícitos con s=.80

Orden de bits: C_install, C_integrity, C_compat, C_oper. Cada fila es uno de los 16 patrones; las probabilidades omitidas en una presentación abreviada serían cero, pero aquí se muestran todos para evitar ambigüedad.

| Patrón | Choque común | Fallo simple disperso | Bottleneck instalación | Fallo emparejado |
|---|---:|---:|---:|---:|
| 0000 | .20 | .00 | .00 | .00 |
| 0001 | .00 | .00 | .00 | .00 |
| 0010 | .00 | .00 | .00 | .00 |
| 0011 | .00 | .00 | .00 | .10 |
| 0100 | .00 | .00 | .00 | .00 |
| 0101 | .00 | .00 | .00 | .00 |
| 0110 | .00 | .00 | .00 | .00 |
| 0111 | .00 | .05 | .20 | .00 |
| 1000 | .00 | .00 | .00 | .00 |
| 1001 | .00 | .00 | .00 | .00 |
| 1010 | .00 | .00 | .00 | .00 |
| 1011 | .00 | .05 | .00 | .00 |
| 1100 | .00 | .00 | .00 | .10 |
| 1101 | .00 | .05 | .00 | .00 |
| 1110 | .00 | .05 | .00 | .00 |
| 1111 | .80 | .80 | .80 | .80 |
| **Suma** | **1.00** | **1.00** | **1.00** | **1.00** |

Los cuatro fixtures comparten s=.80, pero sus marginales son diferentes:

| Fixture | m_install | m_integrity | m_compat | m_oper |
|---|---:|---:|---:|---:|
| Choque común | .80 | .80 | .80 | .80 |
| Fallo simple disperso | .95 | .95 | .95 | .95 |
| Bottleneck instalación | .80 | 1.00 | 1.00 | 1.00 |
| Fallo emparejado | .90 | .90 | .90 | .90 |

En el fixture de fallo emparejado, 0011 concentra el fallo de instalación e integridad; 1100 concentra el fallo de compatibilidad y operación. Es un fixture de estructura, no una hipótesis sobre mecanismos reales.

## 69.2. Generalización a la cuadrícula s

Para cada fixture se conserva la estructura relativa de la masa residual y se sustituye la celda 1111 por s y la masa de fallo total por (1−s):

- Choque común: p1111=s; p0000=1−s.
- Fallo simple disperso: p1111=s; p0111=p1011=p1101=p1110=(1−s)/4.
- Bottleneck instalación: p1111=s; p0111=1−s.
- Fallo emparejado: p1111=s; p0011=p1100=(1−s)/2.

Las restantes celdas son cero en estos fixtures concretos. Para s∈{.60,.70,.80,.90}, cada tabla suma uno y respeta no negatividad. Esta construcción varía deliberadamente los marginales junto con s; no aísla una variación de s manteniendo fijas las marginales. Una sensibilidad con marginales fijas exige otra familia de tablas y solo es posible para valores de s dentro de los límites de Fréchet.

## 69.3. Propagación a C_dep bajo las políticas de intento D1/D2

Se fija únicamente para este cálculo ilustrativo:
- una oportunidad de intento por unidad;
- tasa de intento D1: q0=.25 en control y q1=1 en tratamiento;
- tasa de intento D2: q0=0 en control y q1=1 en tratamiento;
- éxito condicional por intento s, igual entre brazos dentro de cada escenario;
- ausencia basal de C_dep, sin rutas alternativas, reintentos, interferencia ni cambios de otros predicados.

Entonces:
- D1: P(C_dep,post*=1|Z=0)=.25s; P(C_dep,post*=1|Z=1)=s; FS_Cdep,D1=.75s.
- D2: P(C_dep,post*=1|Z=0)=0; P(C_dep,post*=1|Z=1)=s; FS_Cdep,D2=s.

| s | D1 control (.25s) | D1 tratamiento (s) | FS D1 (.75s) | D2 control | D2 tratamiento (s) | FS D2 |
|---:|---:|---:|---:|---:|---:|---:|
| .60 | .15 | .60 | .45 | .00 | .60 | .60 |
| .70 | .175 | .70 | .525 | .00 | .70 | .70 |
| .80 | .20 | .80 | .60 | .00 | .80 | .80 |
| .90 | .225 | .90 | .675 | .00 | .90 | .90 |

Esto precisa la relación entre el parámetro candidato y los estados finales anteriores: D1 control=.20 solo cuando q0=.25 y s=.80. Si s cambia, el estado de control cambia proporcionalmente; no debe mantenerse .20 fijo mientras se varía s salvo que se esté modificando otro mecanismo. D2 control permanece cero bajo la política de no intento focal y las estipulaciones indicadas.

## 69.4. Alcance y límites de la propagación

Las fórmulas anteriores generan primeras etapas de C_dep, no automáticamente de A_f* ni D_f*. La igualdad requiere las condiciones de §67.4: inaccesibilidad basal confirmada, ruta única, predicados no técnicos satisfechos/invariantes y medición sin error diferencial relevante.

Si la probabilidad de intento depende del brazo y el éxito condicional también depende del brazo, la fórmula general es:
`P(C_dep,post*=1|Z=z,D=d,E)=q_{zd}s_{zd}`
bajo una oportunidad y ausencia basal de dependencia. Si hay múltiples intentos, la probabilidad de al menos un éxito requiere modelar el proceso secuencial y la dependencia entre intentos; no es automáticamente (1-(1-s)^n).

La tabla de sensibilidad cambia s y por tanto los estados esperados de C_dep. No simula muestras, no evalúa potencia, no elige tamaño muestral ni estima incertidumbre de muestreo.

## 69.5. Dictamen

Quedan construidos cuatro fixtures explícitos y una propagación analítica de la cuadrícula s hacia FS_Cdep para D1 y D2. Se identifica una dependencia que debe conservarse: el .20 de control D1 es consecuencia de q0=.25 y s=.80, no un parámetro independiente si s está en sensibilidad.

No se selecciona fixture confirmatorio, no se justifica empíricamente ninguna tabla, no se infiere accesibilidad desde C_dep sin condiciones y no se elige D1/D2 como primario. Las familias mixtas más generales, las marginales fijas, la heterogeneidad y la calibración observacional siguen abiertas. No hay freeze, implementación, simulación ni ejecución.


---

## 70. Reconciliación de población, elegibilidad, F* y comparadores (2026-11-04)

**Estado:** propuesta documental; no aprobada, no congelada. Complementa §§46–51 y 66–69. Artefacto desarrollado: `C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md`.

### 70.1 Dos objetivos y dos poblaciones

- `P*_{τ2}`: unidades con condiciones constitutivas basales cumplidas, `C_dep,0=0` y accesibilidad basal de τ2 respaldadamente nula (`A_f,0*=0`), todo determinado antes de Z.
- `P*_F ⊆ P*_{τ2}`: añade ausencia respaldada de ruta funcional substituible (`F_alt,0=0`) en universo, granularidad, contexto y horizonte declarados.
- Las alternativas basales no excluyen automáticamente de P*_{τ2}; son modificadores potenciales y limitan la interpretación de apertura funcional exclusiva.
- La regla de Value no define F* ni substituibilidad.

### 70.2 Corrección de sobrecarga notacional

Se identifica que §48.2 usa `D_f,0` para disponibilidad basal de dependencia, mientras el DGP posterior utiliza `D_f*` para apertura basal→post. En especificaciones nuevas:
- `C_dep,0`: disponibilidad de dependencia técnica focal basal;
- `A_f,0*` y `A_f,1*`: accesibilidad verdadera basal y post;
- `D_f*=I(A_f,0*=0 ∧ A_f,1*=1)`: transición de apertura focal.
No usar `D_f,0` para disponibilidad basal; preservar el histórico con nota de supersesión, sin reescritura silenciosa. Calcular las primeras etapas de C_dep, A_f,1* y D_f* por separado.

### 70.3 F* y alternativas

F* continúa parcialmente definido como función técnica de reconfigurar el sistema diagnosticado hacia una configuración objetivo bajo restricciones de seguridad, integridad y compatibilidad. Faltan S0, objetivo/criterio de aceptación, entradas/salidas, tolerancias, recursos, H, G, C0 y umbrales. Cada ruta debe recibir juicios separados de accesibilidad, aplicabilidad y substituibilidad. F_alt,0=0 requiere cobertura documentada; “no encontrado” sin cobertura es indeterminado. E1–E4 delimitan fuerza de evidencia, no garantizan ausencia universal.

### 70.4 D1/D2

D1: provisión ordinaria de baja frecuencia en control frente a provisión programada; W_attempt .25/1, C_dep final .20/.80, FS_Cdep .60 bajo factorización candidata. D2: ausencia de intento focal frente a provisión programada; 0/1, C_dep final 0/.80, FS_Cdep .80. El .80 es candidato de éxito conjunto condicional, no dato empírico. El .20 de D1 es postasignación, no basal; ambos escenarios pueden tener C_dep,0=0.

La fuente 165–168 recomienda D1 principal condicionado; DEC-C10-026 y DGP §25 recomiendan D2 provisionalmente como contraste mecanístico mientras no se justifique D1. Ninguna recomendación está aceptada. La selección primaria sigue ABIERTA. ITT y Wald/LATE se mantienen específicos por escenario.

### 70.5 Estado

Propuesta de reconciliación documentada. No cierra OPEN-C10-001/003/005/007, AUD-001/004/005/011, ni los contratos CMP/POP. No selecciona D1/D2, no fija F*, no congela y no autoriza implementación, simulación o ejecución.


---

## 71. Reconciliación de snapshots estructurales, evidencia y ΔT_acc (2026-11-04)

**Estado:** propuesta de armonización; no aprobada ni congelada. Artefacto: `C10_S_TRANSFORMATIONAL_SNAPSHOT_AND_DELTA_RECONCILIATION_DRAFT_001.md`.

### 71.1. Hallazgo y precedencia

Se detecta una tensión entre §63.7, que incluía ΔValidity en ΔT_acc*, y §§64.2/67.3/67.6 y DEC-C10-023/027, que sitúan VALID/cobertura en el plano epistémico, fuera de la verdad estructural de A_f*. Una mejora de cobertura puede descubrir una ruta preexistente sin crearla; perder evidencia no destruye por sí mismo una ruta.

Se propone mantener la verdad estructural separada del paquete de evidencia. La validez semántica/operativa real de una ruta permanece en las condiciones estructurales; la validez/fiabilidad de la evidencia permanece en la medición. La formulación de §63.7 se conserva como histórico, pero su ΔValidity queda supersedida para la definición causal.

### 71.2. Dos objetos

Snapshot estructural verdadero:
`S_T^*(i,b,c,t)=(U_t^*,R_t^*,C_t^*,X_t^*)`.

Paquete epistémico de evidencia:
`E_T(i,b,c,t)=(Sources,Coverage,Validity_e,Provenance,Version,Timestamp,Adjudication)`.

### 71.3. Diferencias

`ΔT_acc^*=Diff_{G,M}(S_T^*(t0),S_T^*(t1))=(ΔU^*,ΔR^*,ΔC^*,ΔX^*)`.

`ΔE_T=Diff_E(E_T(t0),E_T(t1))=(ΔSources,ΔCoverage,ΔValidity_e,ΔProvenance,ΔVersion,ΔAdjudication)`.

La evidencia/cobertura no forma parte de la tupla causal. Un cambio de ΔE_T puede modificar la clasificación observada sin cambio estructural. La verdad puede cambiar aunque el analizador emita ? por falta de evidencia.

### 71.4. Correspondencia e identidad

No calcular diff antes de fijar ID canónico, semántica, versiones de especificación/implementación, frontera, granularidad G y mapping M. Misma identidad semántica con nueva versión puede conservar ID y registrar cambios; cambio semántico requiere baja/alta; mapping incierto produce Match=? y diff indeterminado. Un hash distinto no implica automáticamente identidad distinta.

### 71.5. Relación con variables focales

Se mantienen separados C_dep*, A_f*(t), D_f*=I(A_f*(t0)=0 ∧ A_f*(t1)=1) y ΔT_acc*. h_f(ΔT_acc*)=D_f* es proyección focal bajo snapshots comparables, no equivalencia de objetos. ΔT_acc* puede cambiar sin D_f*; D_f*=0 no implica ΔT_acc*=0; ΔE_T≠0 no implica ΔT_acc*≠0.

### 71.6. Contratos

Se registran SNAP-01…15 en el registro de pruebas: cambios de cobertura sin cambio de sistema, pérdida de evidencia, altas/bajas de relaciones, versiones, mapping incierto, cambios no focales, apertura focal, Outcome/Value sin cambio estructural, evidencia tardía, frontera no comparable, vías de B y cambio de aplicabilidad.

### 71.7. Estado

La reconciliación se propone y requiere propagación global. No cierra AUD-001/004/005/007, XAUD-003/004/006 ni XSYNC-138-03/06. No fija G, catálogo, IDs/versiones, reglas de mapping, validación ni oráculos. No hay freeze, implementación, simulación ni ejecución.


---

## 72. Contrato de identidad, versionado y correspondencia de snapshots (2026-11-04)

**Estado:** propuesta operacional; no aprobada ni congelada. Artefacto: `C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md`.

### 72.1. Brecha histórica concreta

Se reutilizan §§43, 47–48, 57–58, 63–64 y 70–71: identidad canónica/versiones, U/R/C, comparabilidad por frontera/G/catálogo, no equivalencia por hash y estado ? ante mapping no resuelto. La brecha restante era un contrato de identidad multinivel, continuidad semántica, split/merge, granularidad y eventos diff.

### 72.2. Niveles separados

Se propone distinguir:
- TID: identidad semántica de la transformación;
- SID: versión de especificación/contrato;
- RID: realización técnica/implementación;
- EID: instancia o evento concreto.

Una TID puede tener varias SID/RID y muchos EID. Cambiar RID no crea automáticamente una TID nueva. Cambiar la función/contrato esencial puede exigir nueva TID y relación de sucesión.

### 72.3. Identidad y continuidad

Los IDs son persistentes, opacos y no codifican versión, fecha, estado, brazo o resultado. Se propone firma semántica `Sig(T)=(Purpose,InputDomain,OutputDomain,CoreOperation,Preconditions,Postconditions,Invariants,Constraints,FailureSemantics)`. La continuidad requiere equivalencia contractual adjudicada; un cambio material de propósito/operación/pre-postcondiciones/invariantes exige nueva identidad; la evidencia insuficiente produce `IdentityMatch=?`.

Hash, nombre, plataforma o cambio de implementación no bastan por sí solos para crear o fusionar identidad.

### 72.4. Matching y granularidad

Se establece jerarquía de ID exacto, alias registrado, continuidad de versión, candidato semántico y adjudicación ciega. Se prohíbe fuzzy auto-merge. Se contemplan mappings 1:N/N:1 (SPLIT/MERGE) sin equivalencia automática. Snapshots incompatibles en frontera/G/catálogo solo se comparan mediante mapping explícito a granularidad común; si no, diff parcial o `DIFF_NOT_COMPARABLE`.

### 72.5. Eventos diff y relación focal

Se proponen ADD, REMOVE, MODIFY_STRUCTURAL, VERSION_CHANGE, SPLIT, MERGE, REWIRE, STATE_CHANGE, UNKNOWN y OUT_OF_SCOPE. La aparición/desaparición documental no prueba alta/baja estructural sin cobertura basal/post.

El matching de τ2 es requisito para D_f* basal→post. Si la identidad focal cambia, D_f* no se calcula como transición de la misma transformación sin redefinir ex ante el objeto/estimando. Cambios RID/SID pueden afectar C_dep/A_f* sin cambio de TID.

### 72.6. Contratos de diseño

Se registran ID-01…15 para hash, nombre, precondiciones, plataforma, split/merge, cobertura, frontera/G, recursos, ΔE_T, continuidad focal y mappings no validados. No hay fixtures ejecutables ni pruebas realizadas.

### 72.7. Dictamen

La propuesta completa el contrato documental de matching, pero no fija aún catálogo, serialización, clases de transformación, tolerancias, G/frontera del DGP, algoritmo confirmatorio ni oráculos. No cierra AUD-004 ni XSYNC-138-03/06. No hay freeze, implementación, simulación ni ejecución.


---

# 73. Alcanzabilidad y propagación de indeterminación en trayectorias (2026-11-04)

**Estado:** propuesta metodológica; no aprobada ni congelada. Artefacto: C10_S_REACHABILITY_AND_TRAJECTORY_PROPAGATION_CONTRACT_DRAFT_001.md.

### 73.1. Distinción de objetos

Se mantienen T_acc*, aplicabilidad App*, relaciones de composición, Reach_H*, Π_H^cand,obs, Π_H^sel y Π_H^exec. Reach_H* pregunta si existe secuencia estructuralmente admisible que alcanza un estado dentro de H; no exige selección ni ejecución. Se recomienda reservar Reach_H* para verdad del DGP y Reach_H,obs para clasificación observada; Reach_possible no debe usarse sin sufijo truth/obs.

### 73.2. Admisibilidad de una ruta

Una trayectoria requiere identidad/versiones comparables, accesibilidad de cada transformación, aplicabilidad desde el estado intermedio correspondiente, relaciones de composición válidas, recursos/autorización/condiciones sin bloqueos, secuencia temporal factible y frontera/G compatibles. App* es necesaria para recorrer una ruta desde un estado dado, pero no redefine T_acc*.

### 73.3. Lógica de propagación

Se propone lógica trivalente 1/0/?:
- conjunción por ruta: 1 si todos los predicados necesarios son 1; 0 si alguno necesario es 0; ? si no hay 0 y al menos uno es ?;
- disyunción entre rutas: Reach=1 si existe una ruta confirmada; Reach=0 solo si el universo/rutas están exhaustivamente cubiertos y todas refutadas; en otro caso Reach=?.
- una búsqueda truncada, catálogo incompleto o mapping no resuelto no permiten concluir Reach=0.

### 73.4. Límites lógicos

Se introducen Reach_H^- (estados con ruta confirmada) y Reach_H^+ (estados con ruta confirmada o no refutada). Su diferencia contiene alcanzabilidad posible pero no confirmada. No son intervalos probabilísticos.

### 73.5. Horizonte, snapshots y no filtración

H, G, ciclos, duraciones, recursos, concurrencia, ventanas y criterio de terminación deben fijarse ex ante. Los cambios dentro de H generan snapshots nuevos e inmutables. No usar selección, ejecución, Outcome o Value para definir Reach. Descubrir después una ruta preexistente actualiza E_T, no fecha su creación.

### 73.6. Contratos

Se registran REACH-01…20 para rutas confirmadas/indeterminadas, cobertura incompleta, no alcanzabilidad exhaustiva, no aplicabilidad, no selección/no ejecución, truncamiento, descubrimiento basal, identidad/versionado, ciclos, recursos y no circularidad. Son contratos documentales, no fixtures ejecutables.

### 73.7. Dictamen

Se resuelve documentalmente la regla de propagación, pero no se cierra AUD-005 ni AUD-007. Faltan catálogo/estados/objetivos, G/H, reglas por clase, ciclos, recursos, snapshots dinámicos, cobertura, oráculos, validación de error y revisión independiente. No hay freeze, implementación, simulación ni ejecución.


---

# 74. Inventario finito candidato del DGP y mapa de cobertura Reach (2026-11-04)

**Estado:** propuesta de fixture conceptual; no aprobada ni congelada. Artefacto: C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md.

Se propone un universo abstracto mínimo con estados S0 (inicial), S1 (intermedio alternativo), S2 (intermedio focal) y SF (objetivo funcional formal). El catálogo local contiene F1=τ2 focal (S0→S2), F2 (S2→SF), A1 (S0→S1) y A2 (S1→SF); relaciones permitidas F1→F2 y A1→A2. Estos aliases no son TID canónicas aprobadas.

Se distinguen escenarios R0 focal exclusivo, R1 alternativa basal estable, R2 alternativa afectada por B y R3 fallo de provisión. R0 puede representar P*_F solo si F* y la cobertura de alternativas se validan; R1/R2 pertenecen como máximo a P*_τ2 según elegibilidad. R2 introduce vía colateral y no sostiene automáticamente exclusión instrumental.

Se propone G atómica, H=3 pasos y ciclos prohibidos en el fixture base. Son candidatos que requieren ratificación; el historial menciona H=3, pero no cierra duración, ventanas ni sensibilidad. Se especifica matriz ruta×predicados×tiempo×evidencia×cobertura y ocho dimensiones de exhaustividad: catálogo, relaciones, condiciones, alternativas, recursos, tiempo, identidad/versiones y observación.

Hallazgo de coherencia: abrir F1 no basta para alcanzar SF; F2 también debe ser accesible, aplicable y componible. Si A1→A2 permanece disponible, Reach(SF) puede ser 1 antes y después de abrir F1. Por tanto D_f* no equivale a apertura funcional exclusiva ni a cambio de Reach.

No se cierran AUD-005/007, G/H, F*, catálogo, comparador D1/D2, recursos, cobertura ni oráculos. No hay fixtures ejecutables, implementación, simulación o ejecución.


# 75. Reconciliación temporal de H y escenarios S4-R (2026-11-04)

Se propone distinguir reloj de estudio t0–t9, profundidad de trayectoria k=0…H y tiempo/ventanas internas de factibilidad. H=3 se conserva solo como profundidad máxima candidata, no como duración de tres unidades temporales. Reach_H se calcula en t4 sobre snapshot t3; no se construye a partir de ejecución observada. App se evalúa por estado hipotético de entrada; recursos, relaciones, autorización, ventanas y bloqueos por prefijo. Las ramas dinámicas requieren snapshots hipotéticos inmutables y reglas de transición explícitas.

Se propone R0↔S4R-A, R1↔S4R-B, R2↔S4R-C y R3↔S4R-D. R0 solo acredita ausencia alternativa con cobertura exhaustiva; R2 introduce vía colateral; R3 conserva ITT y no imputa accesibilidad por Z/intento. El artefacto de auditoría C10_S_TEMPORAL_HORIZON_AND_S4R_INTEGRATION_AUDIT_DRAFT_001.md documenta la reconciliación.

No se ratifican H, duración, ventanas, F*, recursos, D1/D2 ni cobertura. AUD-005/007 permanecen abiertos. No hay ejecución ni simulación.


# 76. Matriz operacional de predicados por paso, rama y tiempo (2026-11-05)

Se crea C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md. La matriz separa ID, ACC, APP, REL, COND, AUTH, RES, DEP, BLOCK, WIN y COV; distingue verdad DGP de clasificación observada; y especifica evaluación por paso F1(S0→S2), F2(S2→SF), A1(S0→S1), A2(S1→SF). ACC/T_acc queda fijada en snapshot t3 en el fixture base; APP se evalúa desde el estado hipotético de entrada; REL por arista; recursos/ventanas/autorizaciones solo cambian intrarrama con reglas explícitas. Las ramas F y A son alternativas contrafactuales, no ejecuciones concurrentes.

Se proponen clases I (invariante), S (state-dependent), T (temporal), R (recurso-dependiente), D (dinámica explícita) y E (epistémica). Por defecto no se inventan transiciones: sin regla DGP, se mantiene snapshot t3 o se clasifica indeterminado. Se añaden contratos documentales PM-01…18. No se asignan valores por escenario ni se cierran AUD-004/005/007/010/011 u OPEN-C10-001/003/005/007. No hay implementación, fixtures ejecutables, simulación ni ejecución.


# 77. Reconciliación histórica de fichas F1/F2/A1/A2 (2026-11-05)

Se crea C10_S_TRANSFORMATION_CARDS_HISTORICAL_RECONCILIATION_DRAFT_001.md tras recuperar §§47–51 y 57–69. Se evita duplicar las fichas ya existentes de F*, elegibilidad, accesibilidad, C_dep, evidencia E1–E4 y condiciones temporales. Hallazgo: F1 está parcialmente especificada como τ2 focal por §§62–63 y 67; F2, A1 y A2 solo tienen posición topológica y transición abstracta en §74, sin semántica transformacional propia, precondiciones, recursos o evidencia específicos. SF es objetivo formal, no definición operacional de F*.

Se documentan cuatro fichas controladas que separan lo conocido de lo abierto. No se inventan operaciones técnicas ni se asignan valores truth por escenario. R0–R3 tampoco permiten afirmar substituibilidad hasta que la ruta A1→A2 se evalúe contra F* común. El hueco requiere elegir y documentar un microdominio sintético concreto o una descripción técnica neutral concreta antes de fijar DGP.

Las fichas sustantivas no están cerradas. AUD-004/005/007/010/011 y OPEN-C10-001/003/005/007 permanecen abiertos. No hay aprobación, freeze, implementación, datos, simulación ni ejecución.


# 78. Comparación de microdominios sintéticos y recomendación (2026-11-05)

Se crea C10_S_SYNTHETIC_MICRODOMAIN_OPTIONS_AND_SELECTION_RECOMMENDATION_DRAFT_001.md para resolver el hueco semántico de §77 sin inventar silenciosamente definiciones. Se comparan: A) migración de configuración entre entornos software; B) integración de datos; C) reconfiguración de flujo de trabajo organizativo. La Opción A se recomienda como candidata por permitir F* técnico verificable, separación entre provisión B y ejecución, ruta focal F1/F2, alternativa A1/A2, recursos/permisos/ventanas controlables y menor riesgo de interferencia.

Bajo Opción A se propone F1 convertir configuración fuente mediante adaptador focal; F2 aplicar y validar en destino; A1 exportar mediante formato neutral preexistente; A2 importar/aplicar y validar por mecanismo nativo. F* sería conformidad con propiedades preespecificadas de esquema, integridad y compatibilidad. Son fichas ilustrativas, no seleccionadas: formatos, tolerancias, IDs, recursos y reglas permanecen abiertos.

B debe provisionar el adaptador, no ejecutar conversión ni aplicación. A1/A2 deben permanecer mecanísticamente independientes en R0/R1; R2 conserva el caso de vía colateral. No se aprueba microdominio ni se fijan parámetros DGP. No se cierran AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007. Sin datos, fixtures ejecutables, simulación ni ejecución.


# 79. Auditoría de compatibilidad causal del microdominio Opción A (2026-11-05)

Se crea C10_S_MICRODOMAIN_CAUSAL_COMPATIBILITY_AUDIT_DRAFT_001.md. Dictamen: la migración de configuración software es potencialmente compatible, pero la formulación actual no demuestra una intervención autónoma sobre A_f* ni identifica θ_A(q). Una asignación Z a provisión B identifica, bajo supuestos de diseño, el ITT de esa política; no el efecto mediado por accesibilidad. Un primer estadio de C_dep no demuestra primer estadio de A_f*, D_f* ni ΔT_acc.

Hallazgo crítico de separación: B provisiona/configura el adaptador; C_dep registra su estado técnico; A_f* determina accesibilidad de τ2; F1 es la operación de conversión cuando se ejecuta, no la instalación; F2 aplica/valida en destino. La descripción anterior de F1 como “habilitar y utilizar” mezclaba provisión y transformación y debe reformularse. ACC, App, selección, ejecución y F* permanecen separados.

Se identifican posibles vías B→permisos, recursos, configuración fuente/destino, seguridad, latencia, costes, información, librerías/dependencias compartidas y A1/A2. Se requiere manifiesto de cambios y grafo de dependencias. A1/A2 solo son alternativa genuina si no dependen del adaptador focal ni son afectadas por B en R0/R1. Si B las afecta, R2 es vía colateral y el ITT es efecto de paquete. F* debe armonizarse con la definición histórica de §§47–51/POP §5; el oráculo común puede ser compartido si mide sin generar la ruta.

D1/D2 sigue abierto; el microdominio no elige comparador. Se mantienen seis gates MD-C1…MD-C6 para B, A_f*, rutas, F*, estimandos/comparador y medición/cobertura. Opción A permanece recomendación condicionada, NO seleccionada ni aprobada. No se generan datos, implementa, simula ni ejecuta.


# 80. Manifiesto de provisión B y grafo de dependencias (2026-11-05)

Se crea C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md para concretar la frontera de provisión de la Opción A. No existe todavía implementación ni inventario técnico real; por ello las superficies B-M01…15 se marcan NO INVENTARIADO, no como ausentes. La arquitectura de menor riesgo recomendada para evaluar es un adaptador sidecar/runtime aislado, aditivo, con versiones fijadas, permisos mínimos y cuotas propias; no está aprobada ni instalada.

B puede obtener/verificar/instalar el paquete, habilitar canal restringido y registrar C_dep; no puede ejecutar F1/F2/A1/A2, modificar F*, oráculo, datos fuente/destino, permisos funcionales ni ruta alternativa. Se distinguen dependencias focales, alternativas, comunes de medición, infraestructura compartida, críticas compartidas y externas. Se especifican snapshots preB/postB/rollback, catálogo de cambios, grafo nodo-arista, criterios de no-afectación A1/A2 y contratos PROV-01…12.

MD-C1 y MD-C4 permanecen abiertos: no se ha demostrado que B sea aislada, que A1/A2 sean independientes ni que B modifique A_f*. El siguiente bloque es una matriz de cobertura del grafo con evidencia 1/0/? y propagación de Reach/F_alt. No se implementa ni instala nada.


# 81. Matriz de cobertura del grafo y evidencia trivalente (2026-11-05)

Se crea C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md. El universo U_G contiene 23 roles de nodos y 23 aristas candidatas; se identifican 14 predicados de accesibilidad/ruta y cinco clases de ruta (focal, alternativa, compartida, externa y desconocida). Este catálogo es un universo candidato de inspección, no un inventario técnico real ni exhaustivo. Todos los estados técnicos siguen ? y cobertura NONE por falta de manifiesto, SBOM, runtime, snapshots y grafo transitivo.

Se separan status estructural, coverage, evidence_status e intención contractual. Ruta=0 exige predicado necesario refutado con evidencia y cobertura; Reach=0 exige descarte de todas las rutas con cobertura exhaustiva; F_alt,0=0 exige descartar todas las rutas funcionalmente substituibles dentro del universo delimitado. Runknown se conserva para evitar inferencia de exhaustividad. Resultado actual: Reach_H=?, F_alt,0=?, A_f*=?; R0/R1 no clasificables y R2 posible pero no observado. MD-C1/2/4 y AUD-005/007 permanecen abiertos. No se ejecuta ni simula.


# 82. Contrato de frontera, granularidad e inventario de U_G (2026-11-05)

**Fuente:** C10_S_SYSTEM_BOUNDARY_AND_GRAPH_GRANULARITY_CONTRACT_DRAFT_001.md. **Estado:** DRAFT; integración documental, no aprobación científica.

## 82.1. Alcance y precedencia

Esta sección desarrolla U_G de §81 sin convertir el catálogo candidato (23 roles de nodo, 23 aristas, 14 predicados y cinco clases de ruta) en inventario observado ni en prueba de exhaustividad. Se reutilizan los contratos de identidad/snapshot (§72), Reach y propagación trivalente (§73), inventario finito (§74), predicados por tiempo/rama (§76), manifiesto B (§80) y matriz de cobertura (§81). No los sustituye ni redefine sus objetos.

## 82.2. Frontera y granularidad

Un elemento se representa como nodo independiente cuando difiere materialmente en intervención/cambio, identidad o versión, fallo/sustitución, interfaz, permisos, recursos, exposición causal, ruta afectada o fuente de evidencia. No se separa por nombre, archivo, hash o paquete sin diferencia funcional/causal relevante. La agregación solo es admisible si no oculta vías diferenciales, dependencias compartidas ni rutas alternativas; ante duda, separar provisionalmente o marcar ?.

Cada arista debe registrar origen/destino, tipo y dirección, tiempo, condición, brazos afectados, versión, evidencia, cobertura y necesidad para la ruta. Se distinguen dependencias directas, transitivas, compartidas y críticas compartidas. La independencia respecto de B requiere análisis transitivo y evidencia pre/post; separar procesos o runtimes no basta.

## 82.3. Alternativas, externos y recursos

Una ruta solo es funcionalmente substituible respecto de F* si parte de entrada admisible común y satisface el mismo criterio independiente bajo C0, G, H, restricciones y tolerancias equivalentes, con cobertura y evidencia suficientes. Un éxito aislado o etiqueta similar no basta. F_alt,0=0 exige descartar todas las rutas substituibles dentro del universo delimitado.

Los servicios fuera de la frontera de control se registran como externos, con interfaz, versión, permisos, disponibilidad, latencia, cuotas, dependencias, observabilidad y exposición a B. Los servicios opacos se representan como cajas negras/nodos desconocidos; la opacidad no prueba ausencia de vías colaterales.

Se separan capacidad instalada, disponibilidad compartida temporal, reserva/asignación por unidad/ruta y consumo durante ejecución. Los tres primeros niveles pueden ser condiciones de accesibilidad según el reloj causal; el consumo de ejecución no se retrotrae a accesibilidad basal.

## 82.4. Versiones, cobertura y estados

Hash/build distinto no implica TID distinta. Un cambio es material si afecta función, contrato entrada/salida, precondiciones, composición, permisos, recursos, fallos o criterio de resultado relevantes para las rutas/estimandos. La continuidad incierta queda ?.

La cobertura se informa por componentes, dependencias directas y transitivas/carga dinámica, interfaces, datos/estado, permisos, recursos, alternativas, externos, tiempo/versiones, observabilidad y adjudicación. COMPLETE solo significa cobertura suficiente del universo operativo declarado, siempre acotado por frontera, versión, contexto y horizonte; no exhaustividad ontológica absoluta. MISSING/NO INVENTARIADO no equivale a 0; PARTIAL no equivale a COMPLETE.

## 82.5. Protocolo de inventario

1. Declarar frontera, unidad, microdominio/F*, S0, G, C0, H/ventanas, versiones, recursos, permisos y periodo; si no están fijados, el inventario es preliminar.
2. Definir snapshots inmutables baseline/post-B/rollback con fecha, origen, hash y limitaciones.
3. Reunir manifiestos, lockfiles/SBOM, análisis estático, configuración, carga dinámica, llamadas, permisos, trazas y documentación de proveedor; ninguna fuente aislada acredita completitud universal.
4. Normalizar nodos/aristas versionados, calcular cierre transitivo, registrar ciclos, resolución dinámica, fallbacks y dependencias desconocidas.
5. Enumerar rutas focales, alternativas, nativas, manuales, externas, compartidas y de recuperación; evaluarlas contra F* común.
6. Comparar snapshots y comportamiento pre/post-B/rollback, incluidos residuos y efectos sobre alternativas, permisos, recursos y estado.
7. Obtener clasificación independiente de nodos, aristas, rutas y cobertura, ciega a Outcome/Value; conservar discrepancias y adjudicación.
8. Para cada ?, registrar fuente faltante, impacto, posible resolución y condición de parada.

Este protocolo define evidencia requerida; no autoriza inspección de sistemas reales, instalación, ejecución ni captura de snapshots.

## 82.6. Estado y consecuencias

No existe aún inventario técnico real. Dependencias directas/transitivas, endpoints externos, recursos compartidos y cambios materiales siguen sin observarse; la independencia A1/A2 respecto de B no está demostrada. La cobertura efectiva permanece NONE donde no hay fuentes inspeccionadas. A_f*, F_alt,0 y Reach_H siguen ?. No se cierra MD-C1…6, AUD-005/007/010/011 ni OPEN-C10-001/003/005/007; tampoco se decide D1/D2, q*, G/H, Value o dimensionamiento. No hay freeze ni autorización de implementación, simulación o ejecución.


# 83. Plantilla de inventario U_G y registro de evidencia (2026-11-05)

Se crea C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md como esquema vacío para registrar nodos, aristas/dependencias, rutas, predicados por paso/tiempo, snapshots/fuentes y cobertura por dimensión. La plantilla separa identidad/versionado, estado observado 1/0/?, truth DGP restringida, procedencia, cobertura, evaluador/cegamiento y motivo de indeterminación.

Las filas de ejemplo son filas de esquema, no componentes, aristas o rutas reales. No se han completado registros técnicos. La plantilla no acredita existencia ni ausencia, ni exhaustividad del universo. Cobertura NONE; A_f*, F_alt,0 y Reach_H permanecen ?. No se cierran MD-C1…6, AUD-005/007/010/011 ni OPEN-C10-001/003/005/007. No autoriza inspección técnica, instalación, implementación, simulación ni ejecución.


# 84. Reconciliación U_G ↔ plantilla de inventario (2026-11-05)

Se incorpora en la sección 10 de C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md el crosswalk explícito con U_G §81: 23/23 roles de nodo, 23/23 IDs padre de arista, 14/14 predicados y 5/5 clases de ruta tienen correspondencia semántica. Esto no acredita existencia ni cobertura técnica.

Hallazgos de estructura:
- Las aristas mult destino E17–E21 y E22–E23 requieren normalización a filas binarias con parent_edge_id; E07 es una relación lógica/conjuntiva y no debe representarse como arista técnica binaria.
- La normalización propuesta produce 39 filas binarias candidatas y mantiene E07 como regla lógica. Son claves de captura, no relaciones observadas.
- E22 apunta a selección/ejecución sin IDs de nodo explícitos; se deben definir eventos/variables sin inventar componentes.
- N16 agrupa criterio F*, oráculo y adjudicación; N23 agrupa ejecución, Outcome y Value. Ambos requieren desagregación analítica cuando tengan identidad/tiempo propio.
- Los cinco tipos primarios de ruta se mapean a Rτ2/RA12/Rshared/Rexternal/Runknown; native/manual/fallback/recovery quedan como subtipos.
- Se identifican campos complementarios: parent_catalog_id, evidence_status, contract_intent, coverage_scope_id, source_provenance, review/adjudication_status y unknown_reason; además parent_edge_id/atomic_edge_id y route_subtype/parent_route_class.

**Dictamen:** correspondencia semántica completa, pero esquema no cerrado. Requiere normalización y ampliación de campos. Todos los estados técnicos permanecen ?; cobertura NONE; A_f*, F_alt,0 y Reach_H siguen indeterminados. No se completa inventario, no se aprueba microdominio/DGP ni se autoriza ejecución.


# 85. Protocolo de fuentes, procedencia y adjudicación U_G (2026-11-05)

Se crea C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md. Define clases de fuentes S1–S8; procedencia reproducible; evidencia mínima por nodo, arista, predicado y ruta; argumento de cobertura negativa; cobertura por dimensión y denominador; doble evaluación cegada; adjudicación de discrepancias; propagación trivalente y condiciones de parada.

El protocolo establece que ausencia solo puede clasificarse 0 con universo operativo, fuentes pertinentes, método con capacidad de detección, integridad, tratamiento de dependencias dinámicas/alias/externos/fallback, cobertura suficiente y revisión independiente. MISSING no es 0; CONFLICTING fuerza ?; COMPLETE es local al universo declarado. C_dep no implica A_f*. Reach=0 y F_alt,0=0 requieren descarte exhaustivo dentro del universo operativo relevante; Runknown y dependencias críticas no resueltas impiden esa conclusión.

El cross-reference se incorpora a la plantilla §11, DGP §44, plan XXIII, matriz de cierre §23, Decision Log §39 y registro de pruebas §46.

**Dictamen:** protocolo documental desarrollado, no aplicado ni validado sobre sistemas reales. No hay fuentes observadas, inventario ni adjudicación. Cobertura NONE; A_f*, F_alt,0 y Reach_H permanecen ?. La plantilla aún necesita auditoría de correspondencia campo a campo. No se cierran MD-C1…6, GC/UGI/UGC, AUD-005/007/010/011 ni OPEN-C10; no se aprueba microdominio, D1/D2, DGP o freeze, ni se autoriza implementación/simulación/ejecución.


# 86. Auditoría campo-a-campo del esquema de evidencia U_G (2026-11-05)

Se audita la correspondencia del protocolo U_G con las tablas físicas de la plantilla. Se detecta que el protocolo definía requisitos sin tablas/campos suficientes: no había EVIDENCE_REGISTER separado, vínculo claim-evidence, denominadores y fuentes válidas en cobertura, registros independientes E1/E2 ni expediente de adjudicación. Además, truth_dgp aparecía como columna de la tabla analítica y route_class mezclaba clases primarias con subtipos.

Se normaliza la plantilla §§12–13: EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT, ADJUDICATION_REGISTER, segregación DGP_TRUTH_SECURE fuera del dataset analítico, separación parent_route_class/route_subtype, campos comunes y reglas de integridad referencial/versionado. El protocolo §13 se actualiza con el mismo contrato.

**Dictamen:** brechas FCM-01…09 tratadas documentalmente. El esquema aún requiere revisión independiente y validación de tipos/constraints; no está cerrado. No hay inventario ni cobertura real; A_f*, F_alt,0 y Reach_H siguen ?. No se cierra UGI/UGC/UGE, MD-C1…6 ni AUD-005/007/010/011. No se autoriza inspección real, implementación, simulación ni ejecución.


# 87. Auditoría de consistencia interna del esquema U_G (2026-11-05)

La segunda pasada de auditoría detecta FCM-10…16: campos comunes no materializados en §§2–6; estado NA de snapshots; evaluador singular frente a E1/E2; posible serialización de múltiples evidence refs; matriz §7 confundible con cobertura canónica; dominios/tipos no definidos; y destino ambiguo de claim_target_id.

Se actualiza la plantilla con columnas comunes físicas en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, diccionario de tipos/domínios y matriz de obligatoriedad (§§12.9–12.10). CLAIM_EVIDENCE_LINK queda como relación 1:N canónica; evidence_ref es enlace primario opcional. COVERAGE_REGISTER es registro normativo y §7 vista resumen. Los evaluadores se conservan como filas independientes; SNAPSHOT usa NA cuando observed_state no aplica.

**Dictamen:** FCM-01…16 tratados documentalmente. No se ha ejecutado parser, validador, constraint check, prueba de seguridad ni cegamiento. Consistencia estática documental, no cierre técnico. Esquema Draft; revisión independiente pendiente. No hay inventario ni cobertura real; A_f*, F_alt,0 y Reach_H siguen ?. Sin autorización de inspección/implementación/simulación/ejecución.


# 88. Tercera pasada de normalización de referencias U_G (2026-11-05)

Se detectan FCM-17…19: clave singular/plural inconsistente en EVALUATOR_ASSESSMENT, listas serializadas de evidencias en evaluación/adjudicación y uso ambiguo de object_id. Se corrige la plantilla: EVALUATOR_ASSESSMENT usa evaluator_record_id singular y object_record_id; ADJUDICATION_REGISTER usa object_record_id y referencias E1/E2; CLAIM_EVIDENCE_LINK enlaza cada evidencia y puede asociarse a evaluator_record_id/adjudication_id. Los objetos exponen evaluator_record_ids solo como navegación; la evaluación canónica sigue siendo una fila por evaluador.

Se ejecuta comprobación estática de tablas: en NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y EVIDENCE/CLAIM-LINK/COVERAGE/EVALUATOR/ADJUDICATION, los conteos de columnas de encabezado, separador y fila de esquema coinciden (29/29/29; 29/29/29; 29/29/29; 24/24/24; 25/25/25; 18/18/18; 10/10/10; 15/15/15; 13/13/13; 12/12/12). No se detectan referencias de verdad DGP en la tabla analítica de predicados.

**Límite:** es una comprobación estática de Markdown/tablas mediante lectura del artefacto remoto; no es parser de esquema, validador FK, constraint check, prueba de seguridad ni ejecución. FCM-01…19 están tratados documentalmente; revisión independiente y validación ejecutable pendientes.


# 89. Paquete de revisión independiente del esquema U_G (2026-11-05)

Se crea C10_S_UG_SCHEMA_INDEPENDENT_REVIEW_CHECKLIST_DRAFT_001.md con 20 controles SR-01…20, perfil propuesto de revisión de modelo de datos y metodología causal, criterios de independencia/cegamiento, procedimiento, dictámenes y evidencia exigible. El paquete distingue revisión documental de validación ejecutable y de autorización científica.

**Estado:** preparado, no iniciado; no hay revisores designados ni dictamen independiente. La comprobación estática de autoría no se presenta como revisión independiente. XSYNC-138-01 y FCM-01…19 permanecen abiertos hasta revisión y validación pertinentes. No hay inventario ni cobertura técnica; sin autorización de ejecución.


# 90. Cuarta pasada de reconciliación semántica U_G — FCM-20 (2026-11-05)

La auditoría de consistencia cruzada detecta que §12.7 permitía interpretar evidence_ref como uno o varios claim_evidence_id, mientras §§12.9 y 14 lo definían como referencia primaria opcional y CLAIM_EVIDENCE_LINK como relación 0..n canónica. Se armoniza: evidence_ref es cero o un vínculo de navegación opcional; el conjunto completo 0..n reside exclusivamente en CLAIM_EVIDENCE_LINK. Se corrige además la descripción histórica FCM-12: evaluator_record_id singular es la clave de cada evaluación E1/E2; evaluator_record_ids plural es solo una referencia resumida opcional en objetos.

Se registra FCM-20 y se actualiza el protocolo de procedencia §16. La corrección es documental; no valida cardinalidades reales ni FKs ejecutables. FCM-01…20 están tratados documentalmente, pendientes de revisión independiente y validación autorizada. No se crea inventario ni se modifica truth DGP.


# 91. Autoauditoría documental asistida SR-01…20 de U_G (2026-11-05)

Se registra `C10_S_UG_SR01_20_AUTHOR_SELF_AUDIT_DRAFT_001.md`, realizada como `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT` sobre la versión documental de U_G disponible en el head de PR #116.

**Resultado:** 8 PASS_STATIC, 10 CONDITIONAL, 2 NOT_ASSESSED, 0 FAIL. PASS_STATIC acredita únicamente presencia/coherencia documental; no equivale a validación técnica, revisión independiente, freeze ni cierre científico. SR-19 (seguridad/custodia) y SR-20 (aptitud operativa) no son evaluables sin arquitectura/instancias y pruebas. SR-02…05, 09, 11…14 y 18 quedan condicionados a instancias, cobertura, aclaraciones o validación.

**Hallazgo UG-SR-A01:** el protocolo §10 dice “ningún estado sin evidence_ref”, mientras §16 y plantilla §12.9 establecen `evidence_ref` como 0..1 opcional y CLAIM_EVIDENCE_LINK como relación 0..n canónica. Debe aclararse si cada estado exige vínculo de evidencia en CLAIM_EVIDENCE_LINK, sin exigir que el atajo `evidence_ref` esté poblado. SR-03 permanece CONDITIONAL.

No se ejecutaron validadores, parser, constraints, fixtures, pruebas de seguridad/cegamiento, inspección técnica, simulación ni experimento. No hay inventario ni cobertura real; A_f*, F_alt,0 y Reach_H permanecen indeterminados. No se cierra FCM-01…20 ni XSYNC-138-01…10, no se congela U_G y no cambia Core/RMA/Matrix/claims/autorización.


# 92. Propuesta de reconciliación UG-SR-A01 — evidencia y cardinalidad

La revisión ampliada detectó que la ambigüedad no se limita al protocolo §10: también afecta a la cadena de §13 y a la regla por fila de la plantilla §11/§12.8, frente a la opcionalidad de `evidence_ref` en plantilla §12.9 y protocolo §16.

Se propone: (a) `evidence_ref` opcional 0..1 como atajo de navegación; (b) CLAIM_EVIDENCE_LINK como relación canónica 0..n; (c) vínculo válido obligatorio para `observed_state=1/0`; (d) `observed_state=?` sin vínculo solo con `unknown_reason`, `evidence_status=MISSING` y límites de búsqueda/cobertura; (e) `NA` con justificación de no aplicabilidad. La propuesta está desarrollada en plantilla §12.11, protocolo §17 y Test Contract Register §§52–53.

**Estado:** propuesta documental pendiente de aceptación; SR-03 permanece CONDITIONAL. No se ha ejecutado parser, FK, constraints ni pruebas. No hay instancias U_G. No se declara FCM cerrado ni esquema congelado.


# 93. Decisión documental UG-SR-A01 — aceptación explícita (2026-11-05)

El usuario acepta la regla de evidencia y cardinalidad registrada en plantilla §12.11, protocolo §17 y Test Contract Register §§52–53: `evidence_ref` opcional 0..1 de navegación; CLAIM_EVIDENCE_LINK relación canónica 0..n; vínculo válido obligatorio para observed_state 1/0; estado ? sin vínculo solo con unknown_reason, MISSING y límites de búsqueda/cobertura; NA con justificación. La contradicción documental queda resuelta. SR-03 se mantiene CONDITIONAL hasta validación técnica de instancias, cardinalidad, FK y parser. No se declara freeze, revisión independiente, inventario U_G ni cobertura efectiva.


# 94. F* y fichas transformacionales candidatas para Opción A

Se ha creado `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md`. El documento desarrolla una propuesta funcional para F*, F1/τ2, F2, A1 y A2, basada en la recomendación de migración de configuración entre entornos software y en la reconciliación histórica de fichas.

La propuesta distingue conversión focal, aplicación/verificación destino, exportación neutral e importación/aplicación nativa; define un F* común técnico, independiente de Outcome/Value; y explicita entradas/salidas, precondiciones, accesibilidad, ejecución, fallos y pendientes. No fija formatos, versiones, tolerancias, recursos, ventanas ni estados generadores.

**Estado:** propuesta de operacionalización; Opción A y F* siguen sin aprobación formal en el repositorio. No se cierra OPEN-C10-003 ni la selección de microdominio. No hay inventario real, DGP completo, validación, simulación o ejecución.


# 95. DEC-C10-051 — selección de Opción A y adopción de F* (2026-11-05)

El usuario selecciona Opción A —migración de configuración entre dos entornos software— como microdominio de diseño de C10-S y adopta F* como contrato funcional de trabajo candidato. La ruta completa debe producir y aplicar en el destino una configuración que satisfaga propiedades obligatorias preespecificadas de esquema, integridad, compatibilidad, preservación funcional y seguridad.

La decisión sustituye el estado previo «recomendado, no seleccionado» para el diseño C10-S. Las Opciones B/C permanecen documentadas como alternativas históricas. F* no se considera cerrado: catálogo exacto de propiedades, mappings, tolerancias, casos frontera, oráculo y protocolo de validación permanecen pendientes. Tampoco se han decidido D1/D2, R0–R3 ni parámetros del DGP.

La selección no constituye aprobación de ejecución, validación técnica, evidencia empírica, revisión independiente ni freeze. `scientific_execution=false`; `execution_authorized=false`.


# 96. Matriz operacional de F* y reconciliación de estados previos (2026-11-05)

Se crea `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md`, complementaria a las fichas Opción A. Define familias FP-01…FP-08 (esquema, integridad, preservación semántica, compatibilidad destino, seguridad, aplicación efectiva, verificación post-aplicación y procedencia/reproducibilidad), regla trivalente no compensatoria, evaluación por etapas y requisitos del oráculo independiente.

**Estado de F*:** definido a nivel de familias y lógica de adjudicación; predicados atómicos, mappings, tolerancias, H/G/C0, contratos concretos y oráculo siguen abiertos. No hay implementación, validación ni evidencia empírica.

**Reconciliación de DEC-C10-051:** las menciones previas en §94 que describen Opción A como «no aprobada» son estado histórico anterior a la decisión. Para el estado vigente rige §95 y DEC-C10-051: Opción A está seleccionada para el diseño C10-S y F* adoptado como contrato de trabajo candidato. La selección no equivale a aprobación de ejecución ni cierre operacional. La referencia de §94 se interpreta como descripción de la propuesta original en el momento de su registro, no como estado vigente.


# 97. Contrato candidato FP-03 — preservación semántica (2026-11-05)

Se crea `C10_S_FP03_SEMANTIC_PRESERVATION_CONTRACT_DRAFT_001.md`. Desarrolla FP-03 mediante dimensiones candidatas SM-01…SM-10 (identidad/significado, valores/tipos/dominios, relaciones, null/default/ausencia, cardinalidad, orden, reglas, tiempo, permisos/control y extensiones desconocidas), reglas de mapping, clases de variación, adjudicación trivalente y requisitos de evidencia/cegamiento.

El criterio es equivalencia semántica observable y acotada al contrato, entradas, C0, G y H preespecificados; no igualdad textual ni equivalencia universal. No se introduce una capa semántica persistida paralela. Se distinguen las propiedades semánticas de FP-03 y el cumplimiento de seguridad FP-05.

**Límite histórico importante:** la selección de Opción A y la adopción de F* no determinan por sí solas los mecanismos concretos de F1/F2/A1/A2. Las descripciones de las fichas actuales se mantienen como roles candidatos de diseño, no TID ni contratos técnicos aprobados, hasta reconciliación/decisión explícita.

**Estado:** FP-03 definido a nivel de dimensiones y lógica; predicados atómicos, dominio, mappings, envolvente de observación, excepciones, tolerancias y oráculo siguen OPEN. No hay validación, evidencia empírica ni ejecución.


# 98. DEC-C10-052 — selección del objeto de configuración (2026-11-05)

El usuario confirma la selección de la clase A: **paquete de configuración de un servicio software**, dentro del microdominio ya seleccionado por DEC-C10-051. Se adoptan como estructura conceptual inicial seis elementos: componente; parámetros tipados; referencias; reglas/restricciones; políticas asociadas; metadatos contractuales.

La decisión permite especializar el contrato FP-03 sobre un objeto delimitado y separar explícitamente el contenido migrado de recursos/capacidad, permisos efectivos, dependencias instaladas y estado de los entornos, provisión B, transformación/ejecución y Outcome/Value. No introduce una capa semántica persistida adicional.

**No se cierra:** dominio de entradas, contratos fuente/destino, propiedades atómicas obligatorias, mappings, tolerancias, excepciones, envolvente de observación, F1/F2/A1/A2, oráculo, DGP, D1/D2, estimandos ni identificación causal. No hay implementación, validación técnica, revisión independiente o evidencia empírica. `scientific_execution=false`; `execution_authorized=false`.


# 99. Catálogo candidato de propiedades atómicas del objeto (2026-11-05)

Se crea `C10_S_CONFIGURATION_OBJECT_ATOMIC_PROPERTY_CATALOG_DRAFT_001.md`, derivado de DEC-C10-052. Atomiza la estructura seleccionada en candidatos para componentes (CMP), parámetros (PAR), referencias (REF), reglas (RUL), políticas (POL) y metadatos (MET); relaciona las propiedades con SM-01…SM-10 y FP-01…FP-08.

Se explicitan límites para no duplicar integridad, compatibilidad, seguridad, aplicación y procedencia; se mantiene separada la política declarada del permiso efectivo y la dependencia declarada de la instalada.

**Estado:** catálogo candidato, no contrato confirmatorio. Ninguna propiedad se declara obligatoria por aparecer en el catálogo; aplicabilidad y obligatoriedad requieren decisión ex ante. Contratos fuente/destino, dominio, mappings, tolerancias y oráculo permanecen abiertos. Sin validación técnica, revisión independiente, evidencia empírica ni ejecución.


# 100. Alcance del DGP base y contrato abstracto fuente/destino (2026-11-05)

Se crea `C10_S_BASE_DGP_SCOPE_AND_ABSTRACT_CONFIGURATION_CONTRACT_PROPOSAL_DRAFT_001.md`. La propuesta recomienda cuatro familias constitutivas para el DGP base (componentes, parámetros tipados, referencias y reglas/restricciones con gramática mínima), políticas como módulo condicional y metadatos como soporte obligatorio de trazabilidad; extensiones desconocidas, orden semántico, temporalidad y mappings complejos se reservan para escenarios condicionales/adversariales.

Se definen las obligaciones documentales de C_src, C_dst y M, y predicados candidatos BASE-CMP, BASE-PAR-TYPE/VALUE/STATE, BASE-REF-ENDPOINT/RELATION, BASE-RULE-LOGIC, BASE-MAP-COVERAGE y BASE-APPLIED-STATE. Se preserva la separación entre FP-01…FP-08 y entre objeto, entorno, provisión, accesibilidad, ejecución, Outcome y Value.

**Estado:** propuesta de alcance, no decisión aprobada ni DGP completo. No fija cardinalidades, dominios, gramática, mappings, valores, probabilidades, truth, oráculo o estimandos. Sin validación técnica, revisión independiente, evidencia empírica ni ejecución.


# 101. DEC-C10-053 — aprobación de la partición del DGP base (2026-11-05)

El usuario aprueba la partición del DGP base propuesta en el documento de alcance: componentes, parámetros tipados, referencias y reglas/restricciones con gramática mínima son constitutivos; POL queda como módulo/escenario condicional fuera del núcleo confirmatorio mínimo; metadatos contractuales son soporte obligatorio de identidad, versionado y procedencia, con extensiones desconocidas condicionales.

Se preserva la estructura conceptual de seis elementos de DEC-C10-052. POL no se elimina del objeto: solo queda fuera del núcleo base. La ausencia de políticas en un escenario base deberá declararse ex ante.

La decisión aprueba la partición, no el contrato completo. Gramática, dominios, cardinalidad/direccionalidad, ausencia/null/default, mappings, tolerancias, oráculo y DGP siguen abiertos. Sin truth, fixtures, validación técnica, revisión independiente, evidencia empírica ni ejecución.


# 102. Gramática mínima de reglas y dominio de tipos (2026-11-05)

Se crea `C10_S_MINIMAL_RULE_GRAMMAR_AND_PARAMETER_TYPE_DOMAIN_PROPOSAL_DRAFT_001.md`. Propone BOOL/INT/DECIMAL/ENUM/STRING/REF, distinción ABSENT/NULL/DEFAULT/VALUE, operadores atómicos finitos, composición AND/OR/NOT y efectos declarativos limitados sin scripts ni ejecución arbitraria.

Se distingue el resultado lógico TRUE/FALSE/UNKNOWN de la clasificación de evidencia 1/0/?. La propuesta no fija dominios finitos, límites, semántica final de UNKNOWN, conversiones ni oráculo; no es gramática aprobada ni implementación.


# 103. DEC-C10-054 — aprobación del perfil finito de dominios y complejidad (2026-11-05)

El usuario aprueba el perfil estructural de dominios finitos por clave y el presupuesto 4/16/16: dominios cerrados/declarados por parámetro; representación decimal escalada; ENUM/REF finitos; STRING acotado; estados ABSENT/NULL/DEFAULT/VALUE con distinción de defaults; AST declarativo acíclico; operadores tipados y composición NOT/AND/OR; efectos base REQUIRE/FORBID; SELECT_ENUM_VALUE fuera del núcleo; UNKNOWN no se convierte silenciosamente en TRUE/FALSE.

La aprobación de 4 niveles, 16 átomos por regla y 16 reglas por paquete es un presupuesto inicial de complejidad, no una calibración empírica. Los límites, escalas, catálogos y valores concretos por clave permanecen abiertos hasta definir el contrato abstracto. También siguen abiertos el mapping completo, los conflictos entre reglas, tolerancias y oráculo.

No implica implementación, parser, validación, truth, fixtures, revisión independiente, evidencia empírica, ejecución autorizada ni freeze del DGP. El siguiente bloque es el contrato abstracto de parámetros y la matriz C_src→C_dst/M con trazabilidad FP-01/02/03 y prevención de doble conteo.


# 104. Matriz abstracta de parámetros y mapping fuente/destino (2026-11-05)

Se crea `C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md` como desarrollo documental posterior a DEC-C10-054. Define campos contractuales por clave de parámetro, correspondencias C_src→C_dst/M para CMP/PAR/REF/RUL/POL/MET, tratamiento de estados/defaults, conversiones tipadas, predicados candidatos FP-01/02/03 y distinción entre paquete destino declarado, estado realmente aplicado y entorno destino.

La matriz no selecciona claves ni valores reales, no fija obligatoriedad final ni mappings concretos, y no cierra el oráculo. Sus predicados deben reconciliarse con SM-01…SM-10 y el catálogo atómico para evitar duplicidad/doble conteo. No hay truth, fixtures, validación técnica, revisión independiente, evidencia empírica ni ejecución.


# 105. Reconciliación SM-01…SM-10 y familias FP (2026-11-05)

Se crea `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md` para reconciliar las dimensiones semánticas SM-01…SM-10 con CMP/PAR/REF/RUL/POL/MET y FP-01…FP-08. La reconciliación corrige la matriz inicial separando propiedades compuestas: estructura formal FP-01, integridad relacional FP-02, significado funcional FP-03, compatibilidad FP-04, seguridad FP-05, aplicación FP-06, verificación post-aplicación FP-07 y procedencia FP-08.

No se aprueba aún obligatoriedad/NA ni predicados confirmatorios. Se preserva DEC-C10-053: CMP/PAR/REF/RUL constitutivos; POL condicional; MET de identidad/versión/procedencia obligatorio. No se genera truth ni se ejecuta.


# 106. DEC-C10-055 — aceptación de reconciliación SM/FP y matriz de aplicabilidad (2026-11-05)

El usuario acepta la reconciliación SM-01…SM-10, propiedades CMP/PAR/REF/RUL/POL/MET y familias FP-01…FP-08. Se adopta la separación entre estructura, integridad, semántica, compatibilidad, seguridad, aplicación, verificación post-aplicación y procedencia, con predicado primario y sin doble conteo. La aceptación no hace confirmatorios todos los candidatos ni resuelve obligatoriedad/NA por instancia.

Se crea `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md` para operacionalizar la declaración ex ante mediante IAM sellado antes de Z/B. La matriz propone O/C/NA/? por propiedad, disparadores, cardinalidad explícita, controles contra scope gaming y separación entre F* funcional, gates técnicos FP-04/05/06 y validez probatoria FP-08.

**Estado:** DEC-C10-055 aceptada; matriz de aplicabilidad PROPUESTA, no aprobada/congelada/validada. Persisten decisiones sobre cardinalidad cero de REF/RUL, fronteras F*/gates y detalle del IAM. Sin truth, fixtures, ejecución ni evidencia empírica.


# 107. DEC-C10-056 — cardinalidad de clases y contrato abstracto (2026-11-05)

El usuario aprueba CMP≥1, PAR≥1, RUL≥1; REF≥0 solo con IAM ex ante y cobertura exhaustiva; POL≥0 ausente por diseño en el núcleo confirmatorio; MET obligatorio para identidad/versionado/procedencia. CMP/PAR/RUL vacíos son SCOPE_ERROR; REF vacío no equivale a falta de evidencia. Se crea `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md` con estructura e invariantes abstractos, sin valores concretos ni schema ejecutable.

**Estado:** DEC-C10-056 aceptada. Contrato abstracto Draft; unidad de servicio, frontera del paquete, clases, claves, mapping, oráculo y validación pendientes. Sin ejecución científica.


# 108. Perfil de frontera P0/P1/P2 — propuesta para decisión (2026-11-05)

Se crea `C10_S_SOFTWARE_SERVICE_CONFIGURATION_BOUNDARY_PROFILE_PROPOSAL_DRAFT_001.md`. Propone separar P0 (paquete declarativo migrable C), P1 (envolvente técnica de origen/destino) y P2 (sistema causal: P0+P1, B, alternativas, dependencias compartidas, agentes, medición y resultados). La separación evita que runtime, permisos efectivos o disponibilidad de dependencias se confundan con contenido del paquete, sin excluirlos del análisis causal.

Se incluyen reglas de clasificación de referencias/recursos, secretos, políticas, binarios/runtime, datos persistentes, mapping, sidecar B, alternativas y snapshots. No se afirma que componentes reales hayan sido inventariados.

**Estado:** propuesta no aceptada/congelada. La frontera concreta, unidad de servicio, deployment manifests, secretos, estado persistente, servicios opacos y unidad experimental siguen abiertos. Sin ejecución.


# 109. DEC-C10-057 — aceptación de arquitectura de frontera (2026-11-05)

El usuario acepta la arquitectura P0/P1/P2 y la clasificación semántica. P0: paquete declarativo migrable; P1: envolvente técnica y estado de los entornos; P2: frontera causal transversal que integra dependencias, alternativas, B, medición, ejecución y resultados. P2 no es clase mutuamente excluyente con P0/P1.

Se registra DEC-C10-057 y se actualiza el perfil de frontera. Se crea `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md`, que propone delimitar una instancia lógica de servicio y clasificar por semántica manifests, variables, secretos, datos persistentes, servicios externos y mapping. El nuevo perfil es propuesta pendiente, no decisión aprobada.

**Estado:** arquitectura aceptada; clasificación elemento a elemento, unidad lógica definitiva, IAM, inventario y diseño de interferencia pendientes. Sin ejecución científica.


# 110. DEC-C10-058 — unidad lógica de servicio y clasificación P0/P1 (2026-11-05)

Se acepta la definición de unidad de migración como una instancia lógica de servicio software identificada por contrato funcional y contrato de configuración versionado, sin equipararla a microservicio/proceso/binario/unidad de despliegue. Se aceptan las reglas semánticas de P0 (configuración declarativa), P1 (realización técnica/estado del entorno) y P2 (frontera causal transversal), incluida la clasificación campo a campo de manifests/variables, separación referencia/secretos, tratamiento por defecto de datos persistentes fuera de P0, migraciones de esquema fuera de F* base y registro de servicios externos opacos como dependencias con incertidumbre explícita.

La unidad de aleatorización/analítica no queda decidida: depende de la evaluación de entornos/recursos compartidos e interferencia. La aceptación no implica inventario real ni schema ejecutable.
