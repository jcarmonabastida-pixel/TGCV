# C10-S — Reconciliación de población, elegibilidad, F* y comparadores D1/D2
**ID:** C10-S-POP-CMP-001 · **Versión:** Draft 001 · **Corte:** 2026-11-04  
**Estado:** PROPUESTA DE RECONCILIACIÓN / NO APROBADA / NO CONGELADA.  
**Ámbito:** Bloque 2 del plan C10-S.  
**No autoriza:** selección primaria D1/D2, freeze, implementación, simulación ni ejecución.

## 1. Fuentes y reconstrucción

Se reutilizan las fuentes ya presentes en PR #116:
- Maestro C10-S §§45–51 y §§66–69 (blob inspeccionado be1ad4de022ad1635b507fce632f765d39cdb93c).
- Fuente recuperada 165–183 y registro C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md (blob 0c2e018dbe3aa593dd4c744bbb5c178f9487e031).
- DGP temporal/roles §§2–3, 24–28 (blob 9bc646f64157f08c5bcf406293fbf6b9b3ce72f7).
- Decision Log DEC-C10-017, DEC-C10-026 y DEC-C10-030 (este último propuesta).
- Reconciliación C10-D1/S4-R y contratos CMP/POP/ACC.
- Regla de reconstrucción histórica aceptada en main.

La reconstrucción confirma que existen definiciones sustanciales; la operación no recrea F*, P* ni D1/D2 desde cero. El trabajo consiste en resolver precedencias, corregir sobrecargas de notación y hacer explícitos los límites pendientes.

## 2. Dos objetivos y dos poblaciones

### 2.1 P*_τ2 — apertura de identidad transformacional

Población preasignación de unidades que:
1. satisfacen todas las condiciones constitutivas basales definidas ex ante para que τ2 pueda ser realizable;
2. tienen la dependencia focal basal ausente y verificada (C_dep,0=0);
3. presentan inaccesibilidad basal respaldada de la transformación identificada τ2 (A_f,0*=0);
4. tienen clasificación suficiente de elegibilidad antes de Z.

Formalización candidata:

P*_{τ2}={i: E_i=1, C_dep,i0=0, A_f,i0*=0}.

La existencia de una alternativa funcional no excluye automáticamente de P*_τ2. Se registra como característica basal, posible modificador del efecto y determinante del alcance de interpretación.

### 2.2 P*_F — apertura exclusiva de función

Población que añade a las condiciones anteriores ausencia respaldada de una ruta alternativa funcionalmente substituible:

P*_F={i∈P*_{τ2}: F_alt,i0=0}.

Por construcción P*_F ⊆ P*_{τ2}.

La ausencia de alternativas es requisito de la afirmación de apertura funcional exclusiva, no requisito general de apertura de la identidad τ2. No convertir P*_F en población primaria por defecto.

## 3. Elegibilidad basal y flujo de clasificación

### 3.1 Condiciones constitutivas

La elegibilidad candidata es conjuntiva:

**Retirada de la fórmula histórica como regla operativa:** la conjunción `E_i` con `C_auth`, `C_resource`, `C_capacity`, `C_info`, `C_domain` y `C_other` pertenece a una propuesta temprana y no debe reutilizarse como definición vigente de elegibilidad ni de `A_f*`. `C_other` no es un predicado residual admisible.

Para D2, `C_auth,base=1` es condición basal común, satisfecha antes de Z e invariante frente a B, conforme a DEC-C10-067. La accesibilidad focal se determina por separado mediante la fórmula candidata del maestro §67.3 y el crosswalk D2: `A_f*=I(ID_f* ∧ REL_f* ∧ COND_f* ∧ AUTH_f* ∧ RES_f* ∧ DEP_f* ∧ ¬BLOCK_f*)`. `C_auth_base` se corresponde con `AUTH_f*`; no son factores independientes. Los recursos/capacidad, información y dominio solo se asignan a los predicados actuales según su función material y sin duplicidad.

La composición de elegibilidad de `P*_τ2` sigue siendo una especificación pendiente: debe derivarse de las condiciones basales constitutivas efectivamente definidas y respaldadas, sin copiar esta fórmula histórica ni confundir elegibilidad con accesibilidad focal.

### 3.2 Estados

Cada condición se clasifica como:
- cumplida;
- incumplida;
- indeterminada;
- no aplicable (solo con regla previa y justificación).

La accesibilidad basal y F_alt,0 usan estados respaldado positivo, respaldado negativo e indeterminado. La ausencia de evidencia no equivale a ausencia estructural. Un caso persistentemente indeterminado no se convierte automáticamente en elegible o inelegible: se aplica regla de exclusión del estimando confirmatorio pre-Z y se informa en el diagrama de flujo y sensibilidad.

### 3.3 Flujo antes de aleatorizar

1. Definir unidad, frontera, catálogo/versiones de τ2, granularidad G y horizonte H.
2. Evaluar condiciones constitutivas y su evidencia.
3. Verificar C_dep,0 por protocolo técnico común.
4. Evaluar A_f,0* independientemente, incluyendo rutas alternativas de la misma identidad τ2.
5. Evaluar F_alt,0 para el subobjetivo funcional, con universo de búsqueda y cobertura declarados.
6. Adjudicar indeterminaciones antes de Z; congelar registro basal inmutable.
7. Confirmar P*_τ2 y P*_F por separado.
8. Aleatorizar solo tras sellar elegibilidad y estratos basales.

No excluir después de Z por incumplimiento, recepción, accesibilidad postratamiento, selección, ejecución, O o V.

## 4. Corrección de notación: C_dep,0, A_f,0* y D_f*

Se detecta una sobrecarga histórica que debe corregirse explícitamente sin borrar el texto de origen:

- En §48.2, D_f,0 se usa como disponibilidad basal de la dependencia focal.
- En DGP §26 y decisiones posteriores, D_f* se usa para la transición de apertura basal→post.
- En otros pasajes, C_dep,0 ya representa disponibilidad de la dependencia basal.

Estas tres cosas no son intercambiables. Para el contrato canónico se propone:

| Símbolo | Significado canónico |
|---|---|
| C_dep,0 | Dependencia técnica focal basal, conjunción de componentes técnicos en t−1. |
| A_f,0* | Accesibilidad verdadera basal de τ2, derivada del snapshot y todos los predicados estructurales. |
| A_f,1* | Accesibilidad verdadera post-provisión, antes de conocimiento/selección/ejecución. |
| D_f* | Apertura focal: I(A_f,0*=0 ∧ A_f,1*=1). |
| C_dep,obs, A_f,obs | Clasificaciones observadas con estados 1/0/?; no sustituyen truth. |

**Regla propuesta:** retirar D_f,0 como nombre de disponibilidad basal en nuevas especificaciones. Usar C_dep,0. Mantener el histórico con nota de supersesión explícita cuando se actualice el maestro. No interpretar D_f* como sinónimo de C_dep ni de A_f,1*.

La primera etapa sobre C_dep, A_f,1* y D_f* se calcula por separado. La condición C_dep,0=0 no basta para inferir A_f,0*=0 si existen otras dependencias o rutas.

## 5. F*: función focal y substituibilidad

### 5.1 Definición disponible

La fuente define provisionalmente F* como la función técnica de modificar la configuración del sistema diagnosticado para obtener una configuración objetivo especificada, bajo restricciones de seguridad, integridad y compatibilidad.

F* es función/capacidad funcional, no transformación, identidad τ2 ni resultado de Value.

### 5.2 Contrato requerido

Antes de evaluar rutas o unidades, F* debe fijarse ex ante mediante:
1. objetivo técnico observable y estado inicial S0;
2. configuración/estado objetivo y criterio de aceptación;
3. entradas y salidas requeridas;
4. restricciones de seguridad, integridad y compatibilidad;
5. tolerancias de calidad, coste, latencia y consumo de recursos;
6. horizonte H;
7. granularidad transformacional G;
8. contexto basal C0 y frontera del sistema;
9. recursos y dependencias admisibles;
10. evidencia E1–E4 y regla de adjudicación/cegamiento.

Los criterios no pueden derivarse de Outcome o Value observado. La regla de Value se mantiene separada.

### 5.3 Substituibilidad

Sub(π,F*,G,H,C0) evalúa si una ruta π cumple F* dentro de la granularidad, horizonte, contexto y restricciones definidos. No implica identidad con τ2, equivalencia causal ni equivalencia de Value.

Cada ruta recibe tres juicios separados:
- accesibilidad de la ruta para la unidad/contexto;
- aplicabilidad desde el estado o rama correspondiente;
- substituibilidad funcional respecto de F*.

### 5.4 Cobertura y estados de alternativas

F_alt,0=0 solo puede declararse con ausencia respaldada dentro de universo, fuentes, granularidad, horizonte, contexto y procedimiento de búsqueda documentados. “No encontrado” sin cobertura es indeterminado.

| Estado | Criterio | Consecuencia |
|---|---|---|
| 0 respaldado | Búsqueda y cobertura suficientes; no existe ruta substituible en el ámbito | Puede incluir en P*_F |
| 1 respaldado | Existe al menos una ruta substituible | Permanece en P*_τ2; excluye de P*_F |
| ? | Cobertura/evidencia insuficiente o contradictoria | No confirmar P*_F; P*_τ2 puede seguir confirmado si las otras condiciones lo están |

E1 documental, E2 mecanística, E3 técnica y E4 reproducible describen fuerza y alcance de evidencia, no una escala universal automática. Un E4 fuera del contexto de la unidad no demuestra realizabilidad para esa unidad. La exclusividad solo se afirma dentro del universo sintético cerrado declarado; en sistemas reales se limita por cobertura.

## 6. D1 y D2: precedencia y legitimidad

### 6.1 Contrastes definidos

| Elemento | D1 | D2 |
|---|---|---|
| Pregunta | Provisión programada frente a provisión ordinaria de baja frecuencia | Provisión programada frente a ausencia de intento focal |
| P(W_attempt=1 \| Z=0) | 0.25 | 0 |
| P(W_attempt=1 \| Z=1) | 1 | 1 |
| P(C_dep=1 \| Z=0) | 0.20 | 0 |
| P(C_dep=1 \| Z=1) | 0.80 | 0.80 |
| Primera etapa C_dep | 0.60 | 0.80 |
| Legitimidad | Requiere fuente independiente que justifique régimen ordinario .25/.20 | Requiere que el objetivo sea realmente ausencia-vs-provisión y ausencia de provisión focal de fondo |

Los parámetros son candidatos analíticos del DGP. El .80 es éxito técnico conjunto condicional tras intento elegible, no dato empírico ni probabilidad marginal por componente. .20 en D1 es estado final post-asignación inducido por .25×.80 bajo la factorización candidata; no es accesibilidad basal. En ambos escenarios se puede tener C_dep,0=0.

### 6.2 Registro histórico de comparadores — NO OPERATIVO

La fuente 165–168 recomendaba D1 como escenario principal condicionado y D2 como contraste; DEC-C10-026/DGP §25 registraban después D2 como candidato mecanístico provisional. Ambas formulaciones son antecedentes de la evolución documental, no instrucciones actuales de selección.

**Precedencia vigente:** DEC-C10-066 establece D2 como escenario primario candidato y D1 como escenario secundario. DEC-C10-067 define las políticas materiales D2: `B_g0^D2` no programa/inicia intento focal y `B_g1^D2` programa un intento estandarizado de provisión técnica focal, con `C_auth,base=1` común e invariante. No se reabre la selección primaria.

La tabla de §6.1 conserva parámetros exploratorios históricos (incluidos .25/.20/.80) y no debe usarse como contrato material confirmado de las políticas D2 ni como valores validados. `s=.80` continúa sin validar. La legitimidad del comparador D2 requiere verificar ausencia basal y ausencia de provisión focal de fondo; D1 requiere justificar el régimen ordinario como comparador secundario.

### 6.3 Condiciones de interpretación por escenario

- D2 es el escenario primario candidato; verificar `C_dep,0=0`, `A_f,0*=0` y ausencia real de provisión focal de fondo/rutas equivalentes antes de Z.
- D1 se conserva como contraste incremental secundario; justificar el régimen ordinario .25/.20 con fuente independiente, población, periodo y contexto.
- Mantener `ITT_D1` e `ITT_D2` separados; no agrupar primeras etapas ni Wald/LATE.
- Calcular por separado primeras etapas de `C_dep`, `A_f`, `D_f*` y `ΔT_acc*`.
- No transportar automáticamente LATE/complier population entre D1 y D2.

## 7. Unidad experimental y población de inferencia

La propuesta UE=UA=instancia sintética autónoma es una estipulación candidata para el DGP primario, no un hecho. Debe demostrarse aislamiento de dependencias, recursos, agentes, información y canales. Si hay spillovers, pasar a clúster/exposición/estimando compatible.

UO puede ser longitudinal/anidada, pero no aumenta N experimental por sí misma. N=2000 y 1000 réplicas siguen provisionales y no se justifican en este bloque.

## 8. Matriz de decisiones y estado

| ID | Decisión | Estado |
|---|---|---|
| POP-01 | P*_τ2 incluye alternativas basales; objetivo de apertura de τ2 | PROPUESTA COHERENTE; aprobación pendiente |
| POP-02 | P*_F es subconjunto con F_alt,0=0 respaldado | PROPUESTA COHERENTE; aprobación pendiente |
| POP-03 | Elegibilidad es pre-Z, conjuntiva, versionada y ciega | PARCIAL; umbrales/evidencias pendientes |
| POP-04 | D_f,0 se sustituye en notación nueva por C_dep,0 | CORRECCIÓN PROPUESTA; propagación global pendiente |
| POP-05 | F* y Sub(π,F*,G,H,C0) | DEFINICIÓN PARCIAL; operacionalización abierta |
| POP-06 | Precedencia D2 primario candidato / D1 secundario | RESUELTA POR DEC-C10-066; legitimidad de cada comparador sigue condicionada |
| POP-07 | UE=UA y no interferencia | ESTIPULACIÓN CANDIDATA; auditoría de frontera pendiente |

## 9. Criterios de cierre del Bloque 2

El bloque requiere:
1. aprobación de P*_τ2 y P*_F y de su relación;
2. fichas operacionales y umbrales de cada condición constitutiva;
3. decisión de notación y migración de D_f,0 a C_dep,0;
4. F* completo con S0, objetivo, restricciones, tolerancias, H/G/C0 y evidencia;
5. universo/cobertura de rutas alternativas y adjudicación;
6. legitimidad del D2 primario candidato y del D1 secundario justificadas por separado;
7. consistencia de C_dep,0, A_f,0*, A_f,1* y D_f*;
8. unidad, interferencia y población de inferencia aprobadas;
9. revisión causal/transformacional independiente.

Hasta satisfacer estos criterios, el bloque es avance documental y no cierra OPEN-C10-001/003/005/007 ni autoriza freeze o ejecución.

## 7. Supersesión de precedencia por DEC-C10-066 (2026-11-06)

La reserva de selección primaria D1/D2 incluida en el encabezado y en las formulaciones históricas de este documento queda supersedida por DEC-C10-066: **D2 es el escenario primario candidato y D1 el escenario secundario**. No se reabre la elección del comparador primario.

Los requisitos de población y legitimidad no quedan cerrados por esa elección. D2 exige verificar C_dep,0=0, A_f,0*=0 y ausencia real de provisión focal de fondo/rutas equivalentes. La población P*_τ2 y el subobjetivo P*_F conservan sus definiciones y límites; soporte y factibilidad deben justificarse. D1 solo se conserva como contraste incremental secundario y requiere justificar el régimen ordinario .25/.20 con fuente independiente. Los estimandos y primeras etapas no se agrupan ni se transportan automáticamente.

No se autoriza freeze, implementación, simulación ni ejecución.


## 10. Reconciliación B1: necesidad del solicitante vs elegibilidad experimental P* (2026-11-11)

La aceptación de B1 como tipo candidato introduce un rol de entidad solicitante-beneficiaria, pero no redefine las poblaciones técnicas ya reconstruidas en §§2–4.

1. P*_{τ2} sigue siendo la población pre-Z de unidades que satisfacen condiciones constitutivas basales, tienen C_dep,0=0, A_f,0*=0 respaldada y elegibilidad experimental suficiente. Su composición constitutiva detallada permanece OPEN.
2. P*_F sigue siendo el subconjunto funcional con F_alt,0=0 respaldada. No es población primaria automática.
3. Need_preZ describe una necesidad/objetivo basal de la entidad solicitante B1. No es condición constitutiva de A_f*, ni componente de C_dep, ni sinónimo de E_i.
4. E_req_preZ sería una regla separada de admisibilidad de la petición según el contrato del servicio, todavía no definido. No debe confundirse con elegibilidad experimental E_i.
5. No se ha aprobado que la entidad solicitante sea la unidad experimental ni que exista cardinalidad 1:1. La relación y cualquier población conjunta P*×B1 quedan abiertas.
6. No se filtra la población confirmatoria por Request_event post-Z, recepción, procesamiento, selección, ejecución, Outcome o Value. La población/estimando de Value debe definirse ex ante y preservarse bajo ITT.
7. La ausencia de solicitud no prueba ausencia de necesidad; ausencia de evidencia de necesidad no prueba Need_preZ=0. Los estados 1/0/? y los mecanismos de ausencia deben permanecer diferenciados.
8. La demanda de recursos/capacidad que ya aparece en el contrato DGP es una magnitud operativa del servicio, no demanda/objetivo del beneficiario.

Esta reconciliación es documental y no aprueba composición de P*, instancia B1, regla de elegibilidad de solicitudes, instrumento, estimando ni parámetros. DEC-C10-066/067 y D2 primario candidato/D1 secundario permanecen sin modificación.


## B1 — unidad solicitante y no interferencia (2026-11-11)

**Decisión:** `DEC-C10S-B1-UNIT-001` — **ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN**.

Se acepta provisionalmente una entidad B1 por unidad experimental (UE), vinculada de forma explícita, unívoca, versionada y trazable a una instancia lógica de servicio aislada. La UE sigue siendo la instancia sintética completa a la que se asigna Z y para la que se generan estados transformacionales, trayectorias, Outcome y Value. La entidad B1 es el referente sintético de necesidad/objetivo pre-Z y de la consecuencia potencialmente valorable; no se confunde con la UE, el servicio ni el actor ejecutor.

La instancia de servicio deberá ser aislada respecto de otras UE en recursos, agentes, información, infraestructura, estado y canales de transmisión. La condición de aislamiento es una hipótesis de diseño que deberá justificarse y auditarse, no una propiedad presumida por nombrar instancias distintas. Si no puede sostenerse, se deberá definir clúster/unidad de asignación, mapa de exposición e inferencia compatible con interferencia antes de confirmar el diseño.

El número de oportunidades estandarizadas por UE queda **OPEN**. Cuando se fije, deberá ser constante entre brazos, establecido ex ante y administrado por un harness externo común; no podrá depender de recepción, admisión, procesamiento, selección, ejecución ni variables post-Z. La ausencia de envío/recepción/admisión seguirá siendo un estado observable y no se codificará automáticamente como ausencia de necesidad o Value=0.

La decisión no fija aún la identidad concreta/versionado final de B1 o del servicio, el número de oportunidades, la ventana/calendario, el payload, las reglas del protocolo, la cardinalidad request↔trajectory, los outcomes técnicos, la consecuencia B1, la perspectiva/autoridad de valoración ni los estimandos. No altera la separación entre el ciclo de petición y el reloj t−1/t0…t9; tampoco convierte solicitud, respuesta o procesamiento en selección, ejecución, Outcome o Value.

**Alcance:** decisión arquitectónica para continuar la especificación; no selecciona beneficiarios empíricos ni valida preferencias reales. No modifica DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación entre main y PR #116.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## 10. Reconciliación de decisiones posteriores sobre UE/B1 y oportunidad (2026-11-11)

Las secciones anteriores reflejan el estado documental de su fecha de corte. Su mención de UE=UA como configuración candidata y de cardinalidad de oportunidades OPEN queda actualizada por decisiones posteriores:

- DEC-C10S-B1-UNIT-001 acepta una entidad B1 por UE, con relación explícita/versionada a una instancia lógica de servicio; la UE sigue siendo la unidad sintética completa y la unidad de asignación no se considera cerrada hasta verificar aislamiento.
- DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 acepta N_opportunities=1 por UE como configuración primaria candidata, con oportunidad ex ante y harness común posterior al snapshot t3/t4.
- La aceptación de esas decisiones no prueba no interferencia, no fija la identidad/versionado material final de B1/servicio, ni cierra la población P*_τ2, la composición E_i, la distribución q_X*, el soporte o el horizonte.
- P*_τ2 y P*_F conservan sus definiciones y límites; P*_F no se convierte en población primaria por defecto.

Este addendum corrige la lectura del estado vigente sin reescribir el historial. C1 continúa OPEN; véase `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`.


## 11. Precedencia poblacional aceptada para C1 (DEC-C10S-C1-POPULATION-PRECEDENCE-001, 2026-11-11)

Se acepta `P*_{τ2}` como población objetivo primaria candidata de C1 ITT D2 y `P*_F` como subpoblación secundaria para apertura funcional exclusiva. La alternativa funcional basal no excluye de P*_{τ2}; solo excluye de P*_F cuando está respaldada. La aceptación fija precedencia, no operacionaliza ni congela P*.

La composición de `E_i`, evidencia y estados de indeterminación, `τ2)/frontera/mapping/snapshots, error de clasificación, cobertura de F_alt, soporte `q_X*`, interferencia, aleatorización, horizonte y Outcome/Value permanecen OPEN. Se mantiene la distinción entre `E_i`, `Need_preZ` y `E_req_preZ`, así como entre truth `A_f,0*` y clasificación observada. No se excluye por eventos post-Z.

La decisión completa y sus límites constan en `DEC-C10S-C1-POPULATION-PRECEDENCE-001.md`. Los estados históricos de §§8–9 no se reescriben: su propuesta de aprobación pendiente queda resuelta únicamente en la precedencia P*τ2/P*F; los restantes criterios siguen abiertos.


## 12. Precisión sobre E_i tras C1.3 (2026-11-11)

El crosswalk `C10_S_C1_BASELINE_ELIGIBILITY_CROSSWALK_DRAFT_001.md` propone como hipótesis de composición mínima `E_i=E_scope,i∧App*(τ2,S0_i)`. No es una definición aceptada ni congelada. La definición de E_scope debe derivarse del IAM pre-Z del snapshot fuente y del contrato constitutivo por unidad; App debe tener su predicado y evidencia propios. La cardinalidad abstracta CMP/PAR/RUL y el roster mínimo del servicio no bastan para declarar pertenencia P*.

Esta precisión no altera la definición de P*τ2/P*F ni las condiciones separadas C_dep,0=0 y A_f,0*=0. Próximo trabajo: crosswalk de registros IAM C_SRC y sus mappings con App/C_dep/A_f; no recuperar la fórmula histórica con C_other.


## 13. Integración del ciclo D2 asignación/población/soporte (2026-11-11)

La precedencia P*τ2/P*_F se conserva. El nuevo contrato C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md precisa que E_i=E_scope∧App sigue propuesta no aceptada; C_dep,0=0 y A_f,0*=0 son condiciones separadas; F_alt,0 solo afecta P*_F. UNKNOWN pre-Z no puede excluirse silenciosamente ni convertirse en 0.

Las probabilidades de programación D2 (0/1 condicionales a Z) no son probabilidades de asignación experimental. La aleatorización Z, q_X*, positividad y soporte siguen no especificados/no materializados. UE=UA permanece condicionado a aislamiento. No se reabre la precedencia aceptada ni se declara población materializada.
