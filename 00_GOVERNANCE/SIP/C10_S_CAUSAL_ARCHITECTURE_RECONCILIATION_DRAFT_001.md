# C10-S — Reconciliación de arquitectura causal, estimandos e intervención
**ID:** C10-S-CAUSAL-ARCH-001 · **Versión:** Draft 001 · **Corte:** 2026-11-04  
**Estado:** PROPUESTA DE RECONCILIACIÓN / NO APROBADA / NO CONGELADA.  
**Ámbito:** Bloque 1 del plan C10-S: arquitectura causal y estimandos.  
**Precedencia de comparador:** DEC-C10-066 acepta D2 como escenario primario candidato y D1 como secundario. **No autoriza:** freeze, implementación, simulación, ejecución ni modificación de C10-D1/Core.

## 1. Resultado de la reconstrucción histórica

Se recuperaron y contrastaron las fuentes canónicas siguientes:

| Fuente | Identidad inspeccionada | Aportación / estado |
|---|---|---|
| C10-D1, protocolo causal | blob `bf25f6ec8965166e5fa52ff18e6d07613bad0eb3` | Rector de la pregunta causal general y de las condiciones de atribución; Draft, no aprobado. |
| C10-S, maestro | blob `be1ad4de022ad1635b507fce632f765d39cdb93c` | S4-R, diccionario, q_X*/q_L*, unidades, población, alternativas, escenarios y §§66–69; Draft. |
| DGP temporal/roles | blob `9bc646f64157f08c5bcf406293fbf6b9b3ce72f7` | Cadena Z→B→W→C_dep→A_f*→ΔT_acc→Reach/Π_H→selección→ejecución→O→V; contrato propuesto. |
| Decision Log | blob `34ceee11751d9d41a4504d414c4fa8d903bd75fb` | DEC-C10-015…029 son propuestas; OPEN-C10-001/002/005/006/007/008 permanecen abiertas. |
| Reconciliación C10-D1/S4-R | blob `62b0af9ff8dfc0e67330bf49e7be210ef4566700` | Jerarquía θ_A(q), ITT de política y LATE_f; no aprobada. |
| Auditoría cruzada XAUD | blob `ce53c902fb39820e976eed5cb2a87e5eacace31c` | XAUD-001…007 abiertos; advierte no formalizar θ_Af(q) antes de resolver q/g e intervención. |
| Resolución AUD-001/002 | blob `5a3a2fa061fe146d9df9d4cdfbb803c5ee274d65` | Propuesta antigua que focaliza manipulación de C_auth; no aceptada. |
| Regla de reconstrucción histórica | main, blob `c01b0cc3b2a7d6bcf56893a0665f09fd2c8ddba4` | Obliga a reutilizar el trabajo previo y no sustituir semántica silenciosamente. |

La inspección fue documental. No se ejecutaron tests, validadores, simulaciones ni análisis de datos. No es revisión causal independiente.

## 2. Dictamen de coherencia

La arquitectura es conceptualmente reconciliable, pero aún no está cerrada. La distinción central que debe conservarse es:

1. **Pregunta científica C10:** contribución causal de políticas factibles de accesibilidad bajo un régimen común, expresada por `θ_A(q)` en C10-D1.
2. **Efecto total de intervención/política:** efecto de asignar Z a una política concreta, incluyendo todas las vías que esa política active.
3. **Efecto focal S4-R:** efecto de políticas que inducen apertura de `τ2`, solo atribuible a accesibilidad si la intervención implementable y el DGP excluyen o identifican vías alternativas.
4. **Efecto local IV:** `LATE_f` entre compliers inducidos por el instrumento, bajo supuestos IV. No es ATE, ni `θ_A(q)` poblacional, ni el efecto de todo `ΔT_acc`.

La reconciliación C10-D1/S4-R ya formula esta jerarquía, pero no está aprobada. El ITT de S4-R no sustituye la pregunta causal general.

## 3. Estimandos y reglas de interpretación

| Objeto | Definición / interpretación | Condición |
|---|---|---|
| `TE_Z` | Diferencia de Value bajo asignación de políticas Z=1 vs Z=0 en la población y horizonte definidos. | Aleatorización/consistencia y observación válida identifican el efecto de asignación; no lo atribuyen automáticamente a A. |
| `ITT_Z` | Contraste estimado por intención de tratar entre asignaciones. | Mantener todos los asignados; no condicionar por recepción, accesibilidad post, selección o ejecución. |
| `ψ_B` | Efecto de las versiones concretas de política B_g1 frente a B_g0. | Es efecto de política/paquete si B tiene otras vías a O/V. |
| `θ_A(q)` | `E[V^{q,g1}]-E[V^{q,g0}]`: contraste de dos políticas factibles de accesibilidad bajo un régimen común q. | Requiere q, g1/g0, población, soporte, versiones, horizonte y Value definidos; vías no mediadas por accesibilidad ausentes o separadas/identificadas. |
| `θ_Af(q*)` | Contraste focal de políticas que inducen accesibilidad de τ2 bajo q*. | Es específico de τ2 y población; no representa automáticamente todo ΔT_acc. |
| `LATE_f` | Efecto local de apertura focal entre compliers. | Wald solo si relevance, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición válida. |

No se definirá un “residual” como resta automática TE−θ_A. Los efectos no son necesariamente aditivos ni definidos sobre el mismo régimen/población. La mediación requiere supuestos adicionales y tratamiento de confusión postratamiento.

## 4. q: qué se mantiene común

La propuesta histórica distingue:

- `q_X*`: distribución objetivo común de covariables, estado e historia **basales pre-Z** dentro de la población elegible. No es intervención que fuerce valores basales.
- `q_L*`: régimen dinámico común para variables post-Z, solo si son indispensables y se define una intervención secuencial factible. No significa ajustar/condicionar mecánicamente por mediadores postratamiento.

**Candidato de trabajo:** utilizar `q_X*` como referente común del DGP primario; excluir del DGP aislado las variables post-Z no indispensables. Si una condición post-Z debe variar, declarar su regla causal y tratarla como parte de la política/intervención o de un régimen secuencial explícito, no como covariable de ajuste convencional.

Pendiente: fijar población, componentes de X/H/C_c, pesos, soporte y positividad por estrato. OPEN-C10-002 sigue ABIERTA.

## 5. g1/g0 y la intervención material B

### 5.1 Regla conceptual

`g1` y `g0` no son asignaciones abstractas de A. Deben corresponder a políticas implementables que inducen distribuciones de accesibilidad bajo el mismo régimen q, respetando las condiciones constitutivas, versiones y conjunto factible.

La asignación Z aleatoriza una versión de política B. No asigna directamente `A_f*`.

### 5.2 Reconciliación de las dos propuestas históricas

Se identifican dos propuestas no equivalentes:

- **Propuesta de resolución AUD-001/002:** manipular `C_auth` para habilitar τ2, manteniendo otras condiciones invariantes.
- **Propuesta material DEC-C10-022 / DGP:** B1 despliega/configura la dependencia técnica focal, habilita interfaz/canal técnico y verifica instalación, integridad, compatibilidad y operación; B0 conserva la configuración asignada de control.

DEC-C10-024 ya advierte que intervenir C_auth no equivale al diseño primario de provisión técnica con C_auth basal/invariante. No debe mantenerse una mezcla tácita.

### 5.3 Arquitectura candidata recomendada para el DGP aislado

**Candidata A — provisión técnica focal con autorización basal común:**

1. `C_auth,0=1` es condición de elegibilidad pre-Z y permanece invariante entre brazos.
2. `B_g1` intenta desplegar/configurar la dependencia técnica focal de τ2, habilitando su interfaz técnica y verificando los cuatro componentes técnicos.
3. `B_g0` aplica el régimen de comparación especificado (D1 o D2), sin alterar autorización basal.
4. Recursos, capacidad, información técnica, dominio, necesidad, incentivos, costes y calidad no cambian diferencialmente por B en el DGP aislado.
5. `C_dep*` es resultado técnico intermedio; `A_f*` se deriva además de ID/REL/COND/AUTH/RES/DEP/BLOCK.
6. Z→B→W_attempt→componentes→C_dep*→A_f*→T_acc/ΔT_acc; después Reach/Π_H, conocimiento, selección, ejecución, O y V.

**Frontera crítica:** habilitar un canal técnico de invocación no puede introducir silenciosamente un cambio de autorización normativa. Si B también concede permisos, modifica expectativas, costes, recursos o incentivos, se registra como cointervención/vía directa. El ITT sigue siendo válido como efecto del paquete; la atribución a A_f* no queda identificada por ese contraste sin una estrategia adicional.

La Candidata A es la opción documental más coherente con DEC-C10-022 y el contrato DGP actual. Se recomienda para revisión, pero no se acepta ni congela en este documento.

### 5.4 Alternativa si se mantiene la intervención sobre C_auth

Si la pregunta requiere manipular autorización, la intervención debe llamarse política conjunta de autorización/provisión. Si autorización forma parte constitutiva de A_f*, el efecto de política puede ser efecto conjunto de cambio de condición y accesibilidad; no etiquetarlo automáticamente como efecto puro de accesibilidad. Para preservar `θ_A(q)`, habría que demostrar que el contraste implementa g1/g0 bajo q y separar cualquier vía directa de C_auth hacia Value.

## 6. DAG temporal de trabajo

```text
t−1 BASELINE / ELEGIBILIDAD
X, H0, C_c0, C_auth0, recursos0, capacidad0, información técnica0
C_dep0, A_f0*, T_acc0, alternativas0, Value/O baseline
              │
              ▼
t0 ASIGNACIÓN ALEATORIA
Z ───────────────► B_gz (política/version asignada)
                         │
                         ▼
t1 PROVISIÓN
W_attempt ─► recepción/cumplimiento/versión recibida
                         │
                         ▼
t2 VERIFICACIÓN TÉCNICA
C_install*, C_integrity*, C_compat*, C_oper* ─► C_dep*
                         │
                         ▼
t3 ACCESIBILIDAD / SNAPSHOT
ID*, REL*, COND*, AUTH*, RES*, DEP*, BLOCK* ─► A_f*
                         │                    └─► A_f,obs (medición 1/0/?)
                         ▼
T_acc,1 ; ΔT_acc = T_acc,1 ⊖ T_acc,0
                         │
                         ▼
t4 REACH_H / Π_H CANDIDATAS
                         │
                         ▼
t5 CONOCIMIENTO / CONSIDERACIÓN
                         │
                         ▼
t6 SELECCIÓN / INICIO
                         │
                         ▼
t7 EJECUCIÓN / FALLO / INTERRUPCIÓN
                         │
                         ▼
t8 OUTCOME O
                         │
                         ▼
t9 VALUE V (vector/regla/beneficiario/horizonte por fijar)
```

Vías de exclusión a vigilar: B→C_auth; B→recursos/capacidad; B→información/conocimiento; B→coste/latencia/calidad/seguridad; B→alternativas; B→selección/incentivos; Z→medición. Si alguna existe, no atribuir automáticamente el ITT a A_f*.

## 7. Diccionario mínimo de roles causales

| Variable | Tiempo | Rol | Observación / regla |
|---|---|---|---|
| X, H0, C_c0 | Pre-Z | Basales / régimen objetivo q_X* | Elegibilidad y soporte solo con información preasignación. |
| C_auth,0 | Pre-Z | Condición constitutiva candidata | Candidata A: elegibilidad común, invariante; si B la cambia, cointervención. |
| Z | t0 | Asignación aleatoria | Base del ITT; nunca sustituir por recepción. |
| B_gz / version_B | t0–t1 | Política asignada | Registrar versión asignada y recibida. |
| W_attempt | t1 | Intento de provisión | No equivale a éxito técnico. |
| C_install/integrity/compat/oper | t2 | Componentes técnicos verdaderos y medidos | Verdad DGP separada de evidencia observada; conjunción para C_dep. |
| C_dep* / C_dep,obs | t2 | Dependencia técnica efectiva | 0/1 en truth; 1/0/? en observación. |
| A_f* / A_f,obs | t3 | Accesibilidad focal verdadera/observada | A_f* incluye todos los predicados; A_f,obs ciega y validada. |
| App_f | t3–t4 | Aplicabilidad desde S0 | No equivale a accesibilidad. |
| T_acc, ΔT_acc | t3 | Espacio accesible y cambio estructurado | Snapshot completo; la proyección focal no sustituye el objeto. |
| Reach_H, Π_H | t4 | Posibilidades/trajectorias candidatas | Derivadas sin consultar O/V ni ejecuciones históricas. |
| K, Consider | t5 | Conocimiento/consideración | Mediadores potenciales si B afecta información. |
| Sel, Start | t6 | Selección e inicio | No ajustar ITT por estas variables. |
| Exec | t7 | Ejecución | No define accesibilidad retrospectivamente. |
| O | t8 | Outcome | Indicadores, fuente y ventana independientes. |
| V | t9 | Value | Regla/beneficiario/horizonte fijados; distinto de O. |
| A_f,obs / O_obs / V_obs | Según medición | Proceso de observación | Missingness/error no se convierte en cero ni en verdad. |

## 8. Decisiones y discrepancias que permanecen abiertas

| ID | Punto | Dictamen de este bloque | Estado |
|---|---|---|---|
| CA-01 | C10-D1 θ_A(q) vs S4-R ITT | Jerarquía conceptual reconciliada; aprobación responsable pendiente. | ABIERTO |
| CA-02 | q_X* / q_L* | q_X* basal como candidato primario; q_L* solo si régimen secuencial necesario. | ABIERTO |
| CA-03 | C_auth intervenido vs basal/invariante | Recomendada Candidata A; no aceptada. | ABIERTO |
| CA-04 | B_g0/B_g1 y D1/D2 | Políticas deben definirse materialmente; selección D1/D2 no se resuelve aquí. | ABIERTO |
| CA-05 | Vías directas/colaterales | Invariantes especificadas como requisito del DGP aislado; escenarios adversariales necesarios. | ABIERTO |
| CA-06 | Unidad/interferencia | UE/UA y no interferencia por construir siguen propuestas, no hechos. | ABIERTO |
| CA-07 | Value, horizonte y población | No definidos suficientemente para ecuación final de estimando. | ABIERTO |

### Precedencia D1/D2

La fuente histórica 165–183 recomienda D1 como principal condicionado a justificar el régimen ordinario; DEC-C10-026 y DGP §25 recomiendan provisionalmente D2 como candidato mecanístico mientras no se justifique D1. Son recomendaciones de alcance diferente y ambas no aceptadas. Se conserva la selección primaria ABIERTA. D1 y D2 son estimandos de política distintos; no agrupar ITT ni Wald/LATE.

## 9. Criterios de cierre del Bloque 1

El bloque no se considera cerrado hasta que una decisión científica explícita:
1. acepte o rechace la jerarquía `θ_A(q)` / `TE_Z/ITT_Z` / `LATE_f`;
2. fije población, horizonte, regla de Value y versiones de políticas;
3. acepte q_X* y, si aplica, q_L* con soporte;
4. resuelva si C_auth es basal/invariante o parte de una intervención conjunta;
5. elija una intervención material B y su correspondencia con g0/g1;
6. disponga D1/D2 con justificación del objetivo y comparador;
7. defina y audite vías colaterales, consistencia, positividad e interferencia;
8. registre revisión causal independiente y estado de aprobación.

Hasta entonces, este documento es un contrato candidato de reconciliación y no una especificación congelada.


## 10. Auditoría de compatibilidad con el microdominio Opción A (2026-11-05)

La auditoría C10_S_MICRODOMAIN_CAUSAL_COMPATIBILITY_AUDIT_DRAFT_001.md concluye que la migración de configuración es potencialmente compatible, pero no identifica por sí misma θ_A(q). Z→B identifica ITT de la política de provisión bajo supuestos de diseño; la atribución a A_f* requiere políticas g1/g0 bajo q común y ausencia/separación de vías directas. C_dep first stage no equivale a A_f*, D_f* o ΔT_acc first stage.

Se corrige una ambigüedad de fichas: B provisiona/configura el adaptador; C_dep mide el estado técnico; A_f* mide accesibilidad de τ2; F1 es la conversión ejecutada mediante el adaptador disponible, no su instalación; F2 aplica/valida en destino. No usar “habilitar y utilizar” como una sola definición de F1. App, ejecución y F* se mantienen separados.

La instalación puede afectar configuración, permisos, recursos, seguridad, costes, latencia, información, librerías o dependencias compartidas. Se requiere manifiesto de cambios y grafo de dependencias. A1/A2 deben ser no afectadas por B en R0/R1 para sostener interpretación focal; si B las modifica, R2/vía colateral y efecto de paquete. D1/D2 permanece abierto. Recomendación condicionada, no aprobada.

## 11. Precedencia de continuidad y revisión asistida (2026-11-05)

Las referencias de §9 a revisión causal independiente como condición de cierre quedan supersedidas para la continuidad actual de C10-S. Prevalece el protocolo autocontenido del maestro §130, Closure Control Matrix §12 y Test Contract Register §54: AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT. No se exige R1/R2 para seguir especificando, preanalizar, preparar o ejecutar una simulación una vez autorizada.

La independencia de generador, analizador y evaluador es una separación computacional de truth, datos, permisos y momento de acceso; no equivale a revisión humana independiente. La arquitectura causal y las decisiones abiertas de este documento no cambian por este addendum.


## 12. Precedencia posterior: DEC-C10-066 (2026-11-06)

La selección del escenario primario candidato queda resuelta por aceptación expresa: **D2 es el escenario primario candidato** de C10-S para el contraste mecanístico de provisión focal frente a ausencia de intento focal en control; **D1 se conserva como escenario secundario** para el contraste incremental frente a provisión ordinaria de baja frecuencia.

Esta decisión supersede la apertura de selección registrada en §§5.5 y 9, así como las recomendaciones previas de D1 como principal condicionado, exclusivamente en lo relativo a qué comparador ocupa la posición primaria candidata. No modifica la pregunta general (\theta_A(q)), no convierte (B_{g0}/B_{g1}) en equivalentes automáticos de (g_0/g_1), y no cierra la jerarquía de estimandos ni los supuestos de atribución.

Los ITT, primeras etapas y LATE/Wald se mantienen específicos por escenario. La legitimidad de la atribución a accesibilidad sigue dependiendo de las vías colaterales, exclusión, medición y supuestos de identificación; si B afecta directamente otros determinantes de Outcome o Value, el resultado se interpreta como efecto de política/paquete salvo identificación adicional.

El registro autónomo es `DEC-C10-066_D2_PRIMARY_CANDIDATE_ACCEPTANCE.md`. Parámetros, incluido (s=0.80), DGP, políticas materiales, (q_X^*), poblaciones, Value, horizonte y ejecución permanecen abiertos/no aprobados.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.

## 12. Supersesión de precedencia por DEC-C10-066 (2026-11-06)

La decisión aceptada DEC-C10-066 supersede la cláusula de §5 que reservaba la selección primaria D1/D2 y cualquier formulación anterior de este documento que mantuviera abierta esa precedencia: **D2 es el escenario primario candidato; D1 es el escenario secundario**. Las recomendaciones anteriores se conservan como historial, no como estado operativo vigente.

Esta decisión no cierra la arquitectura causal: no equipara B_g0/B_g1 con g0/g1, no identifica θ_A(q), θ_Af(q*) ni el efecto mediado, y no valida exclusión, población, soporte, parámetros o vías colaterales. La legitimidad del comparador D2 sigue requiriendo ausencia basal y ausencia de provisión focal de fondo verificadas. D1 conserva su uso secundario condicionado a justificar el régimen ordinario.

No se autoriza freeze, implementación, simulación ni ejecución.


## 13. Aceptación del contrato material de políticas D2 — DEC-C10-067 (2026-11-06)

Se aceptan documentalmente las definiciones materiales de (B_{g0}^{D2}) y (B_{g1}^{D2}) del registro DEC-C10-067: control sin intento focal programado y tratamiento con intento de provisión técnica focal programado, usando artefacto/versionado identificados y verificación separada de instalación, integridad, compatibilidad y operatividad. Ninguna política garantiza éxito técnico, (C_{dep}^{*}), (A_f^{*}), (D_f^{*}) ni ejecución de F1/F2/A1/A2.

(C_{auth,base}=1), elegibilidad, recursos no focales, capacidad, información basal y protocolo de medición/adjudicación se mantienen comunes en el DGP aislado. Los cambios diferenciales en permisos, recursos, costes, latencia, calidad, seguridad, información, incentivos o alternativas constituyen vías colaterales que deben registrarse. El ITT mantiene interpretación de efecto de política/paquete si existen esas vías; no equivale automáticamente a efecto puro de accesibilidad.

El registro no cierra actor, artefacto/hash, recepción, ventanas, reintentos, rollback, evidencia de componentes ni ausencia de provisión de fondo. (s=0.80) sigue siendo hipótesis no validada y no se transfiere automáticamente a (A_f^{*}) o (D_f^{*}). No se autoriza freeze, implementación ni ejecución.


## 14. Precedencia posterior: autorización basal D2 y descarte de la intervención focal como primaria (DEC-C10-067; 2026-11-09)

Esta sección corrige la lectura que pudiera derivarse de CA-03 y de §9. **La cuestión «C_auth basal/invariante o intervención focal sobre autorización» ya no está abierta para el D2 primario candidato.** DEC-C10-067 establece que `C_auth,base=1`, elegibilidad, recursos no focales, capacidad, información basal y protocolo de medición/adjudicación permanecen comunes en el DGP aislado.

Por tanto:

1. En D2, `C_auth,base=1` es una condición basal común, satisfecha antes de Z e invariante frente a B.
2. La política D2 modifica la provisión técnica focal conforme a DEC-C10-067; no manipula la autorización basal.
3. La antigua propuesta AUD-001/002 de intervenir focalmente sobre `C_auth` no es la intervención primaria D2. Puede conservarse como escenario alternativo/adversarial de política de autorización, con su propio efecto de política/paquete y vías causales.
4. La autorización basal no se elimina de la arquitectura: el crosswalk D2 de predicados la corresponde con `AUTH_f*`; `C_auth_base` y `AUTH_f*` no se cuentan como factores independientes duplicados.
5. Esta resolución no cierra la jerarquía de estimandos, la equivalencia entre B y g, las vías colaterales, exclusión, población, soporte ni identificación de la contribución causal específica de accesibilidad.

**Supersesión limitada:** esta sección supersede exclusivamente el estado ABIERTO de CA-03 en la medida en que se refería a la elección para D2 entre autorización basal y autorización intervenida, y la pregunta equivalente de §9. No borra la propuesta AUD-001/002 ni cierra la posibilidad de estudiarla como escenario distinto. Los restantes asuntos CA-01, CA-02 y CA-04…CA-07 conservan sus estados y alcances, salvo resolución posterior expresa.

**Control de lectura:** no interpretar «AUD-001/002 es antiguo/no primario» como «C_auth basal es obsoleto» ni como «AUTH_f* debe retirarse». La intervención focal sobre autorización y el predicado basal de autorización son objetos distintos.

**Estado:** reconciliación documental basada en DEC-C10-067 y en el crosswalk de predicados; no es una nueva DEC ni una aprobación de la arquitectura causal completa. No autoriza freeze, implementación, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`.
