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

E_i=I(C_auth,0=1 ∧ C_resource,0=1 ∧ C_capacity,0=1 ∧ C_info,0=1 ∧ C_domain,0=1 ∧ C_other,0=1).

Esta expresión no se considera cerrada hasta que cada condición tenga ficha operacional, umbral, fuente, ventana basal, procedimiento, evaluador/cegamiento, versión y criterio de suficiencia. C_other no puede funcionar como comodín; debe descomponerse en predicados identificados o justificarse como residuo acotado.

C_auth, recursos, capacidad, información técnica no focal y dominio se tratan como condiciones basales invariantes en la Candidata A de intervención B. Si B cambia alguna, debe registrarse como cointervención/mediador y reconsiderarse la atribución causal.

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

### 6.2 Precedencia histórica y propuesta posterior

Hay dos recomendaciones registradas:
- Fuente histórica 165–168: D1 principal condicionado a justificar el régimen ordinario; D2 contraste.
- DEC-C10-026 / DGP §25: D2 candidato mecanístico provisional mientras no se justifique D1; D1 secundario incremental.

No se trata de una contradicción matemática: los escenarios responden a comparadores y preguntas diferentes. Sí existe una tensión de precedencia entre recomendaciones. Ninguna está aceptada. La selección primaria permanece ABIERTA.

### 6.3 Regla de decisión

- Elegir D1 si la pregunta primaria es incremental frente a provisión ordinaria real y la frecuencia/estado final están respaldados por fuente independiente, población, periodo y contexto.
- Elegir D2 si la pregunta primaria es apertura focal frente a ausencia de intento y puede verificarse ausencia de provisión focal de fondo.
- No llamar contaminación a la provisión ordinaria que forma parte de B_g0^D1.
- Mantener ITT_D1 e ITT_D2 separados; no agrupar primeras etapas ni Wald/LATE.
- Calcular por separado primeras etapas de C_dep, A_f,1*, D_f* y ΔT_acc.
- No transportar automáticamente LATE/complier population entre D1 y D2.
- No fijar escenario primario sin una decisión explícita que conecte la pregunta científica, población y estimando.

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
| POP-06 | D1 histórico condicionado vs D2 mecanístico provisional | CONFLICTO DE PRECEDENCIA DOCUMENTADO; decisión primaria abierta |
| POP-07 | UE=UA y no interferencia | ESTIPULACIÓN CANDIDATA; auditoría de frontera pendiente |

## 9. Criterios de cierre del Bloque 2

El bloque requiere:
1. aprobación de P*_τ2 y P*_F y de su relación;
2. fichas operacionales y umbrales de cada condición constitutiva;
3. decisión de notación y migración de D_f,0 a C_dep,0;
4. F* completo con S0, objetivo, restricciones, tolerancias, H/G/C0 y evidencia;
5. universo/cobertura de rutas alternativas y adjudicación;
6. decisión primaria D1/D2 y escenario secundario justificados;
7. consistencia de C_dep,0, A_f,0*, A_f,1* y D_f*;
8. unidad, interferencia y población de inferencia aprobadas;
9. revisión causal/transformacional independiente.

Hasta satisfacer estos criterios, el bloque es avance documental y no cierra OPEN-C10-001/003/005/007 ni autoriza freeze o ejecución.
