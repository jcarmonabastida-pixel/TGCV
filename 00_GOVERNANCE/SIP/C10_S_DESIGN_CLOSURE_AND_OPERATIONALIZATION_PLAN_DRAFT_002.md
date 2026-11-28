> **HISTÓRICO / SUPERSEDIDO COMO GUÍA OPERATIVA (2026-11-05).** Draft 002 se conserva para trazabilidad y no debe dirigir nuevas decisiones. La guía vigente es `C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_003.md`, alineada con el maestro C10-S §§1–130 y con la integración conversacional 130–183 en §§16–52. El Draft 002 incorporó una hipótesis errónea de laguna histórica y una arquitectura simplificada; no usarlo como referencia normativa.

---

# C10-S — Plan integral de cierre científico y operacionalización

**ID:** C10-S-PLAN-001 · **Versión:** Draft 002 · **Fecha:** 2026-11-05  
**Estado:** DRAFT / NO APROBADO / NO CONGELADO / NO EJECUTADO  
**Sustituye como guía operativa a:** `C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_001.md` (se conserva como histórico; no utilizar sus secuencias antiguas sin reconciliación).  
**Maestro:** `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, incluida la auditoría §§131–132.  
**Auditoría de referencia:** `C10_S_MASTER_RECONCILIATION_AUDIT_DRAFT_001.md`.

---

## 1. Mandato y alcance

C10-S es un experimento sintético diseñado para evaluar si una arquitectura de intervención, medición e inferencia puede recuperar, distinguir y falsar la contribución causal de la accesibilidad transformacional a Value bajo DGP conocidos. Su finalidad no es producir una demostración empírica general de TGCV: los resultados sintéticos solo autorizan conclusiones dentro de los DGP, poblaciones, políticas, horizontes, reglas de Value y supuestos que se definan y ejecuten.

El único ámbito de este plan es la línea científica C10-S. Web, playground, difusión y productización quedan fuera de alcance y no son gates ni dependencias del experimento.

El diseño debe poder producir: (i) atribución focal identificada bajo supuestos defendibles; (ii) efecto de política/paquete sin atribución focal; (iii) evidencia de ausencia o equivalencia dentro de márgenes justificados; (iv) efecto adverso; o (v) no identificación/precisión insuficiente. No se diseñará para garantizar un resultado favorable a TGCV.

## 2. Reglas de autoridad y persistencia

1. `00_GOVERNANCE/README.md` en `main` y los documentos de bootstrap/estado canónico gobiernan el proceso, permisos y límites; no sustituyen el contenido científico de C10-S.
2. Las decisiones científicas aceptadas se identifican por DEC-C10 y deben constar en Decision Log y maestro. Las propuestas, auditorías, ejemplos numéricos y fuentes recuperadas nunca se convierten automáticamente en decisiones.
3. El maestro C10-S es la integración normativa de diseño. Los contratos especializados deben mantener crosswalk explícito hacia él. El plan es derivado y no puede contradecirlo.
4. No se utilizará memoria conversacional como fuente de verdad. Toda recuperación histórica debe citar artefacto, commit/blob, sección y estado.
5. Toda actualización documental debe verificarse mediante fetch posterior y SHA. No modificar `main`; mantener PR #116 Draft y su base actual salvo decisión expresa.
6. La modalidad de control es `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`. No se requiere revisión externa para continuar el trabajo científico interno; nunca se describirá autoauditoría como independiente.
7. `scientific_execution=false` y `execution_authorized=false` hasta autorización expresa. Diseño documental no autoriza DDL, parser, validadores, fixtures, simulación o experimento.

## 3. Arquitectura de referencia vigente

Esta sección define el mapa de constructos que debe preservar el diseño; no declara que todas las relaciones estén identificadas ni que todas las variables estén operacionalizadas definitivamente.

### 3.1 Microdominio y frontera

- Opción A: migración de configuración entre entornos software (DEC-C10-051).
- Objeto: paquete/contrato de configuración versionado de una instancia lógica de servicio (DEC-C10-052 y DEC-C10-058).
- DGP base, gramática finita, dominio de tipos, matrices SM/FP y cardinalidades conforme DEC-C10-053…056.
- Frontera P0/P1/P2 conforme DEC-C10-057/058: P0 configuración declarativa migrable; P1 envolvente técnica y estado de entornos; P2 frontera causal transversal.
- F* es criterio funcional de referencia; no equivale a Value ni convierte por sí solo una ruta en equivalente. Las reglas, predicados, mapping y adjudicación siguen sujetos a sus contratos y estados.

### 3.2 Intervención y mecanismo técnico

La intervención no es una manipulación abstracta directa de `A_f*`. La arquitectura material de trabajo distingue asignación y política de provisión:

`Z → B0/B1 → B_received / W_attempt → (C_install, C_integrity, C_compat, C_oper) → C_dep* → A_f*(t) → D_f*`

- `Z`: asignación a política; `B0/B1`: versiones materiales de política de provisión.
- `B_received` y `W_attempt`: recepción y realización del intento, no equivalentes a éxito.
- `C_install`, `C_integrity`, `C_compat`, `C_oper`: componentes técnicos que deben modelarse conjuntamente.
- `C_dep*`: estado de dependencia técnica efectiva, derivado de los componentes y condiciones pertinentes.
- `A_f*(t)`: accesibilidad estructural verdadera de la transformación focal a lo largo del tiempo.
- `D_f*`: apertura focal definida respecto de la condición basal elegible y la ventana temporal acordada.

La cadena es una arquitectura generadora candidata, no una identidad determinista. La provisión no garantiza intento; el intento no garantiza dependencia; la dependencia no garantiza accesibilidad si faltan predicados estructurales; accesibilidad no garantiza apertura en toda definición de población; apertura no equivale al cambio completo `ΔT_acc*`.

### 3.3 Espacio transformacional, rutas y resultados

- Snapshots estructurales versionados, identidad/matching y eventos diff permiten reconstruir `ΔT_acc*`. Cambio de captura/versionado no equivale a cambio estructural; cambio de evidencia `ΔE_T` no equivale a `ΔT_acc*`.
- Reach y trayectorias `Π_H` se derivan de rutas admisibles, predicados temporales y horizonte H; mantener propagación trivalente 1/0/? y no resolver indeterminación como falso.
- F1/F2: transformaciones/rutas focales; A1/A2: alternativas candidatas. Su disponibilidad, afectación por B, equivalencia funcional y rol causal deben generarse y medirse, no suponerse.
- Separar aplicabilidad `App`, selección, ejecución `Exec`, Outcome `O` y Value `V`. Accesibilidad no se define por ejecución; Outcome no es valoración; Value no se deriva mecánicamente de A u O.

### 3.4 Evidencia y U_G

U_G es sistema de registro de observaciones, snapshots, cobertura, procedencia, evaluaciones y adjudicación; no genera la verdad causal. DEC-C10-059…065 y OAS-01…11 especifican contratos documentales, pero U_G sigue sin schema freeze ni validación física. Mantener segregación de truth del DGP, datos observados, analizador y evaluador.

## 4. Jerarquía causal y estadística

Los siguientes objetos no son intercambiables:

1. `ITT_Z`: efecto de asignación a la política B en la población y horizonte definidos.
2. `ψ_policy` / efecto de paquete: interpretación correcta de ITT cuando B modifica accesibilidad y otras vías.
3. `ITT_Df`: primera etapa de asignación sobre apertura focal.
4. `LATE_f`: efecto local entre compliers bajo supuestos IV; secundario y condicionado, nunca etiquetado como ATE ni como efecto general de `ΔT_acc*`.
5. `θ_Af(q*)`: contraste focal de políticas bajo régimen común y condiciones de atribución demostradas en el DGP.
6. `θ_A(q)`: pregunta científica general C10-D1 sobre accesibilidad y Value; no se sustituye por el ITT/LATE focal de S4-R.
7. `θ_{L,A}`: interpretación conjunta cuando no se pueda aislar la contribución focal.

La aleatorización identifica el efecto de asignación bajo el diseño; no demuestra por sí sola exclusión, mediación o atribución exclusiva a accesibilidad. Si hay vías directas/colaterales, informar efecto de política/paquete o efecto conjunto. No presentar `TE − θ_A(q)` como efecto directo/residual puro.

## 5. D1/D2, q y población: asuntos abiertos

- D1 (provisión ordinaria postasignación en control) y D2 (sin provisión ordinaria en control) son escenarios candidatos con objetivos y primeras etapas diferentes. La fuente recuperada recomienda D1 como principal condicionado a justificar el régimen ordinario; otras reconciliaciones mantienen gates para D1/D2 según objetivo. No hay selección primaria aprobada.
- D1 ilustrativo: intento control 0.25, tratamiento 1; éxito técnico conjunto candidato 0.80; p0=0.20, p1=0.80 y primera etapa 0.60 bajo los supuestos especificados.
- D2 ilustrativo: intento control 0, tratamiento 1; p0=0, p1=0.80 y primera etapa 0.80.
- `q_X*` es candidato a distribución común basal de condiciones para S4-R aislado; `q_L*` se reserva como candidato para intervenciones secuenciales si L_m postasignación es indispensable. Ninguno está aprobado.
- `P*_τ2` (apertura de transformación focal) y `P*_F` (apertura funcional exclusiva) son poblaciones distintas. No usar exclusividad funcional como restricción automática de elegibilidad.
- Unidad experimental, unidad de asignación, recursos compartidos, interferencia, elegibilidad, accesibilidad basal, soporte y composición de compliers siguen abiertos.

Los valores p0/p1, s=.80, efectos ilustrativos y probabilidades de componentes no son tasas empíricas ni parámetros confirmatorios. La distribución conjunta de los cuatro componentes debe explicitarse (16 patrones); independencia es un escenario, no supuesto por defecto. La sensibilidad debe cubrir shocks comunes, fallos dispersos, cuellos de botella, dependencia mixta y heterogeneidad basal/temporal.

## 6. Medición y validez de constructo

Integrar los contratos de medición en una sola arquitectura coherente:

- A: accesibilidad estructural y apertura focal, medida con fuentes/predicados independientes del éxito de ejecución.
- O: Outcome funcional, medido separadamente de la valoración.
- V: Value contextual y multidimensional como recomendación de trabajo recuperada, no decisión final sobre vector/índice, dimensiones, escalas, ponderaciones o compensación.
- F*: criterio funcional para juzgar rutas; mapping, tolerancias, preservación semántica y adjudicación deben quedar explícitos.
- Temporalidad: estados basales, provisión, dependencia, accesibilidad, selección/ejecución y medición posterior, con ventanas y snapshots definidos.
- Calidad: validez de constructo, fiabilidad, error de clasificación/medición, invariancia, sensibilidad, acuerdo y trazabilidad.
- Cegamiento: generador conserva verdad latente; analizador recibe solo observables permitidos; evaluador compara predicciones con truth sin filtración.
- Ausencia: diferenciar falta de registro, fallo técnico, abandono, censura, indefinición y medición inválida; analizar MCAR/MAR/MNAR, selección postasignación, cotas y sensibilidad. No imputar automáticamente 0 ni confundir ausencia de dato con inaccesibilidad.

P181/P182/P183 son familias de contratos propuestos recuperados; deben reconciliarse con Test Contract Register y DGP. No se consideran pruebas ejecutadas.

## 7. Identificación, falsación y adversarialidad

El DGP confirmatorio debe incluir, al menos:

- efecto focal positivo, nulo y adverso;
- política sin primera etapa, primera etapa débil y fuerte;
- incumplimiento, fallos parciales y versiones múltiples;
- vías directas/colaterales de B a O/V;
- alternativas basales no afectadas y alternativas afectadas por B;
- heterogeneidad de efectos y composición de compliers distinta en D1/D2;
- violaciones de exclusión, monotonicidad, independencia y consistencia;
- interferencia/recursos compartidos;
- error de medición, clasificación diferencial, missingness y censura;
- escenarios de no identificación y soporte insuficiente.

Las pruebas adversariales deben permitir que el analizador falle, clasifique como paquete, o declare no identificación. No se aceptará que el generador establezca directamente `A_f*=Z` o codifique la conclusión deseada.

## 8. Diseño estadístico — bloque obligatorio, aún no cerrado

El dimensionamiento se abordará después de cerrar estimandos, población, DGP, medición y reglas de decisión. Debe justificar:

- familia de estimandos y jerarquía confirmatoria/secundaria;
- tamaño muestral por unidad/cluster y asignación, considerando interferencia;
- potencia y precisión para ITT, primera etapa, LATE/IV y objetivos de recuperación;
- cobertura de intervalos y control de error tipo I/falsos positivos;
- métodos robustos a instrumento débil;
- heterogeneidad, multiplicidad, covariables basales y estimación por perfiles;
- error Monte Carlo y número de réplicas requerido;
- missingness, censura y sensibilidad conjunta;
- márgenes `δ` y `ε`, relevancia práctica, equivalencia y reglas de inconclusión.

`N=2000` total por réplica, asignación 1:1 y 1000 réplicas Monte Carlo son candidatos históricos provisionales sin justificación final. No deben aparecer como parámetros confirmatorios hasta que el cálculo/estudio de precisión los sostenga. Ninguna decisión estadística se tomará después de observar resultados.

## 9. Secuencia de cierre revisada

| Orden | Bloque | Trabajo y condición de salida | Estado |
|---|---|---|---|
| 0 | Integridad documental | Recuperar §§131–163; reconciliar §§164–183; cruzar maestro/Decision Log/DGP/matriz/tests/plan; registrar estados y SHA | ABIERTO — BLOQUEA nuevas decisiones |
| 1 | Arquitectura de intervención | Cerrar B0/B1, Z, recepción, intento, componentes técnicos, C_dep*, mecanismo y versiones | PARCIAL |
| 2 | Población/unidad/régimen | Resolver P*_τ2/P*_F, elegibilidad, D1/D2, q_X*/q_L*, unidad, interferencia y soporte | ABIERTO |
| 3 | Accesibilidad y espacio | Definir A_f*(t), D_f*, snapshots, ΔT_acc*, Reach, Π_H, F1/F2/A1/A2 y predicados temporales | PARCIAL |
| 4 | Estimandos e identificación | Formalizar ITT, efecto paquete, primera etapa, IV/LATE, θ_Af(q*) y θ_A(q); supuestos y salidas | ABIERTO |
| 5 | DGP y escenarios | Especificación generativa completa, distribuciones conjuntas, truth oculta, escenarios positivos/nulos/adversariales | PARCIAL |
| 6 | Medición/Value | A/O/V, F*, instrumentos, validez, fiabilidad, error, invariancia, temporalidad, ausencia/censura | PARCIAL |
| 7 | Estadística | Potencia, precisión, cobertura, weak-IV, Monte Carlo, N, réplicas, δ/ε, multiplicidad | ABIERTO |
| 8 | Evidencia U_G y contratos | Cerrar semántica documental, integridad, crosswalks y test contracts; luego gate técnico separado | DOCUMENTAL PARCIAL; TÉCNICO NO VALIDADO |
| 9 | Auditoría interna de no-regresión | Verificar coherencia de todos los artefactos; clasificar como self-review asistida no independiente | PENDIENTE |
| 10 | Congelación de diseño | Solo con todos los bloques aprobados, decisiones registradas y riesgos residuales explícitos | NO ALCANZADO |
| 11 | Implementación/validación | DDL/parser/fixtures/validadores y pruebas técnicas con autorización separada | NO AUTORIZADO |
| 12 | Simulación/experimento | Ejecución reproducible, análisis ciego, evaluación y reporte con autorización expresa | NO AUTORIZADO |

## 10. Criterios de salida científica

- **Atribución focal recuperada:** el método identifica correctamente el efecto focal solo en escenarios donde los supuestos/condiciones se cumplen y recupera incertidumbre apropiada.
- **Efecto de paquete:** identifica ITT de política, pero detecta que vías colaterales impiden atribución focal.
- **Ausencia/equivalencia:** solo con intervalos suficientemente precisos y márgenes preespecificados justificados; no inferir equivalencia de un p no significativo.
- **Efecto adverso:** el método recupera signo y magnitud dentro de tolerancias predefinidas.
- **No identificación:** reconoce violaciones, soporte insuficiente, instrumento débil, ausencia/censura no identificable o medición inválida; no fuerza estimación causal.
- **Recuperación estadística insuficiente:** se informa como limitación del método/diseño, no como refutación automática de la hipótesis sustantiva.

## 11. Control de cambios y no-regresión

- Mantener las decisiones aceptadas DEC-C10-051…065 según su alcance; no ampliar su significado. DEC-C10-059…065 son contratos U_G, no decisiones sobre estimandos ni identificación causal.
- No reintroducir `q/g0/g1/C_auth` como arquitectura material primaria sin reconciliación expresa con B0/B1 y los constructos posteriores.
- No colapsar provisión, intento, dependencia, accesibilidad, apertura, ΔT_acc, Reach, trayectoria, ejecución, Outcome y Value.
- No convertir D1/D2, q_X*/q_L*, F*, Value vectorial, parámetros técnicos o estadísticos en decisiones sin aceptación trazable.
- Mantener históricos y propuestas para trazabilidad, marcando explícitamente SUPERSEDED/PROPOSAL/OPEN cuando corresponda; no borrar evidencia de por qué se cambió.
- Cualquier nueva decisión debe actualizar en el mismo cambio: maestro, Decision Log, contrato afectado, matriz de cierre, Test Contract Register y plan/crosswalk según aplicabilidad.

## 12. Estado actual y siguiente acción

El maestro incorpora §§131–132 para registrar la brecha de sincronización y el gate de recuperación. La auditoría MRA-001 identifica la falta de recuperación primaria de §§131–163 y la integración incompleta de §§165–183. Por ello, el Bloque 0 es prioritario y bloquea nuevas decisiones de diseño. El plan Draft 002 sustituye al plan 001 como guía, pero no se considera aprobado ni resuelve por sí solo la brecha histórica.

**Siguiente operación:** completar recuperación desde fuentes GitHub/PR/commits de §§131–163; normalizar la fuente recuperada §§164–183 (incluida copia íntegra/transcripción o referencia persistida); reconciliar cada afirmación con el maestro y Decision Log; propagar P181/P182/P183 a DGP y Test Contract Register; actualizar descripción PR #116; y ejecutar auditoría de no-regresión. Solo entonces se reanuda el diseño causal específico.

**Estado de autorización:** `scientific_execution=false`; `execution_authorized=false`. No se ha implementado ni ejecutado el experimento.
