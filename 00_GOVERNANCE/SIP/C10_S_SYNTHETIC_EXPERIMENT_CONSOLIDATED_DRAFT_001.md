# C10-S — Experimento sintético de validación transformacional y causal
**Consolidación documental integral — borrador 001**

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

- (A^+=T_{acc,1}setminus T_{acc,0})
- (A^-=T_{acc,0}setminus T_{acc,1})
- (Delta T_{acc}=(A^+,A^-))

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

[
Reach_H(S_0,T_{acc})={S':S_0\rightsquigarrow_{\leq H}^{T_{acc}}S'}
]

- (H) es el máximo de aplicaciones efectivas de transformaciones.
- En el contrato sintético actual, (H=3).
- Las evaluaciones de condiciones/accesibilidad no consumen horizonte.
- Los ciclos cuentan cada aplicación efectiva.
- (T_{acc}) se reevalúa en cada estado hipotético intermedio.
- Cada rama mantiene estado, condiciones y snapshots de accesibilidad independientes.

No se presupone:
- (Delta T_{acc}
eq0 Rightarrow Delta Reach
eq0);
- (Delta Reach=0 Rightarrow DeltaPi_H=0);
- mismo Reach implica mismas trayectorias.

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

- SR-01: τ3 no habilita τ3 ni verificación técnica.
- SR-02: τ3 no puede preceder a τ3? **No aplica como composición; la regla correcta es que τ3 (Verify) solo se aplica después de τ2 (Reconfigure).**
- SR-03: τ4 puede seguir a τ1 en G0.
- SR-04: G0 termina tras transferencia; no se etiqueta como configuración verificada.
- SR-05: G1 admite τ1→τ2→τ3.
- SR-06: H=3 limita aplicaciones efectivas.
- SR-07: cada rama conserva estado y condiciones independientes.
- SR-08: Value no modifica la generación TGCV.
- SR-09: cualquier ruta externa que realice F* bloquea exclusividad.
- SR-10: no se infiere ejecución a partir de trayectoria candidata.

**Nota de corrección:** SR-02 se formula de manera normativa como “τ3 solo aplicable tras τ2”; no debe conservarse la frase interrogativa/duplicada como una prueba distinta. Esta normalización evita la ambigüedad tipográfica de las notas de trabajo.

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
