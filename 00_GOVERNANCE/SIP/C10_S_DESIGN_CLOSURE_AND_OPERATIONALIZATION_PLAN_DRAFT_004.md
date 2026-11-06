# C10-S — Plan integrado de cierre científico y operacionalización
**ID:** C10-S-PLAN-001 · **Versión:** Draft 004 · **Fecha:** 2026-11-05
**Estado:** DRAFT / NO APROBADO / NO CONGELADO / NO IMPLEMENTADO / NO EJECUTADO
**Sustituye como guía operativa:** Draft 001, Draft 002 y Draft 003 (se conservan como históricos).
**Maestro normativo:** C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md, §§1–130.
**Auditoría de alineación:** C10_S_MASTER_RECONCILIATION_AUDIT_DRAFT_003.md.

---

## 1. Propósito, alcance y límites

C10-S es el experimento sintético para evaluar si el diseño causal-transformacional puede: (i) reconstruir correctamente los constructos; (ii) identificar los estimandos que el diseño permite identificar; (iii) recuperar efectos conocidos; y (iv) reconocer efectos de paquete, vías alternativas, heterogeneidad, efectos adversos, ausencia de efecto y no-identificación bajo DGP con verdad conocida.

C10-S evalúa la capacidad metodológica dentro de los DGP, poblaciones, intervenciones, horizontes y reglas de Value efectivamente especificados. Una simulación no demuestra por sí sola causalidad empírica en sistemas reales ni confirma/refuta una regularidad general de TGCV.

Este plan se refiere exclusivamente a la línea científica C10-S. La web germen/playground y su evolución comunitaria son una línea separada, fuera del alcance y de los gates de C10-S.

La continuidad no depende de revisores externos. Las auditorías propias se identifican como AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT. Los roles generador, analizador y evaluador deben estar separados computacionalmente; el evaluador no se presenta como revisor humano independiente.

## 2. Cobertura histórica y precedencia documental

### 2.1 Cobertura ya integrada

| Secciones conversacionales | Integración en el maestro |
|---|---|
| 130 | §16 |
| 131–137 | §§17–24 |
| 138–163 | §§25–50 |
| 164 | §51 |
| 165–183 | síntesis en §52 y desarrollo en contratos especializados |

No procede recuperar ni reconstruir otra vez §§130–163. El contenido 164–183 no se reduce a §52: su desarrollo estadístico, de medición, heterogeneidad y ausencia se conserva también en el registro auxiliar y en los contratos especializados, incluidos P177, P182 y P183. La fuente Notes_261104_163033.docx comienza en la sección 164 y cubre 164–183; el registro auxiliar C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md organiza específicamente el tramo 165–183 y no es transcripción literal completa.

### 2.2 Precedencia

1. La gobernanza de main (README, bootstrap, estado canónico y workflows) determina proceso, permisos y límites.
2. C10-D1 determina la pregunta causal general θ_A(q), sus requisitos y límites.
3. El maestro C10-S integra la especificación del experimento sintético; las decisiones DEC-C10 se interpretan con su alcance.
4. Los contratos especializados, Decision Log, matrices y auditorías complementan al maestro. Si discrepan, la divergencia se registra y se corrige contra el maestro y las decisiones aceptadas; no se elige por intuición.
5. Este plan es derivado y no crea decisiones científicas.
6. Una propuesta, recomendación, fixture ilustrativo o ecuación candidata no se convierte en decisión aceptada por estar persistida.
7. Toda nueva decisión debe actualizar en el mismo ciclo el maestro, Decision Log y artefactos afectados; verificar cada escritura mediante fetch y SHA.
8. No modificar main ni cambiar la base de PR #116 sin instrucción expresa.
9. scientific_execution=false y execution_authorized=false hasta autorización expresa y gates previos.

Los estados DEFINIDO, PROPUESTO, ABIERTO, ACEPTADO, IMPLEMENTADO, EJECUTADO, AUDITADO, NO IDENTIFICADO e INDETERMINADO se mantienen separados.

## 3. Arquitectura del microdominio y del sistema

### 3.1 Opción A y frontera

Opción A es el microdominio seleccionado: migración de configuración de una instancia lógica de servicio software entre entorno fuente y destino. El objeto de trabajo es el paquete de configuración versionado, no el runtime o la unidad de despliegue por sí solos.

Se conserva la frontera aceptada:
- P0: configuración declarativa del servicio.
- P1: realización técnica y estado de los entornos.
- P2: frontera analítica causal transversal que integra elementos P0/P1, B, alternativas, dependencias compartidas, agentes, medición, ejecución, Outcome y Value.

La unidad lógica de servicio y la clasificación semántica P0/P1/P2 fueron aceptadas en DEC-C10-057/058. La unidad de migración no decide automáticamente la unidad experimental, de asignación ni de análisis.

El DGP base finito, gramática, dominios, mapping, matrices SM/FP y cardinalidades se rigen por DEC-C10-052…056. POL queda como módulo condicional secundario; no se infiere su presencia o ausencia después de observar resultados. F* es criterio funcional técnico, no Value.

### 3.2 Fichas transformacionales

La semántica de trabajo de Opción A es:
- F1/τ2: conversión de la configuración fuente mediante el adaptador focal disponible.
- F2: aplicación y validación en destino.
- A1: exportación mediante mecanismo/formato neutral preexistente.
- A2: importación/aplicación mediante mecanismo nativo.

Esta distinción evita confundir provisión B con ejecución de F1/F2. Sin embargo, las fichas F1/F2/A1/A2 no están completamente cerradas: formatos, identidad/versiones TID/SID/RID, precondiciones, recursos, composición, tolerancias, evidencia y oráculo siguen pendientes. No inventar operaciones ni declarar A1/A2 independientes por sus nombres.

F* debe fijar objetivo funcional, S0, entradas/salidas, restricciones, tolerancias, horizonte H, granularidad G, contexto C0, recursos y procedimiento de adjudicación. No incorpora Outcome ni Value.

## 4. Arquitectura relacional de accesibilidad y medición transformacional

### 4.1 Capacidad del sistema y accesibilidad de la unidad

La accesibilidad no se trata como atributo descontextualizado del sistema ni como estado psicológico del usuario. Es una propiedad relacional y situada de realizabilidad.

Distinguir:
- T_cap(sys,t): capacidad estructural del sistema dentro de una frontera/versionado/contexto.
- T_acc(i,t): transformaciones efectivamente disponibles para la unidad i, dadas la relación de acceso, interfaz, recursos asignados/disponibles, condiciones y contexto.

La relación candidata es T_acc(i,t) ⊆ T_cap(sys,t), solo cuando identidad, granularidad, horizonte y reglas de realizabilidad son comparables. Deben declararse B_sys, B_i, R_pool, R_i, C_sys, C_i, versión, tiempo, G y H. Recursos instalados, compartidos, asignados y consumidos no se colapsan. La unidad de análisis y el nivel de Outcome deben ser coherentes; cualquier agregación requiere regla explícita.

### 4.2 Cadena generativa y distinciones

La cadena de referencia del escenario focal es:

Z → B asignada/ofrecida/recibida → W_attempt → S_install → (C_install, C_integrity, C_compat, C_oper) → C_dep* → A_f*(t) → D_f* → ΔT_acc* → Reach_H* → Π_H* → Known/Consider → Sel → Start → Exec → O → V.

Es un orden temporal/generativo, no una afirmación de mediación exclusiva. Las vías B→O/V y las rutas alternativas se mantienen explícitas.

- Z: asignación aleatoria a una política concreta.
- B: política y versión material de provisión.
- W_attempt: intento; no equivale a instalación o éxito.
- S_install: resultado de instalación; no equivale a verificación completa.
- C_dep*: conjunción de instalación, integridad, compatibilidad y operatividad verificadas.
- A_f*: verdad estructural de accesibilidad de τ2, derivada de todos los predicados de acceso aplicables a unidad, frontera y tiempo; no se asigna desde Z/B/W/C_dep.
- App_f*: aplicabilidad desde S0; se mide separadamente.
- D_f*: apertura basal→post, I(A_f,base*=0 ∧ A_f,post*=1).
- ΔT_acc*: cambio completo del espacio accesible; A_f es solo una proyección focal.
- Reach, trayectoria, conocimiento, selección, inicio, ejecución, Outcome y Value son constructos/eventos separados.

### 4.3 Condiciones de acceso y fórmula candidata

La matriz de §§59 y 63–64 clasifica cada condición según función causal, nivel y tiempo. La fórmula focal candidata es:

A_f*(i,t;τ2) = I[ID_τ2 y versión válidos ∧ C_dep*(i,t)=1 ∧ C_auth_base(i,t)=1 ∧ R_access*(i,t)=1 ∧ D_support*(i,t)=1].

App_f*(i,t) = I[Pre_τ2(S0_i,t, historia_i,t)=1].

Esta fórmula es una operacionalización candidata para S4-R, no una definición universal ni una decisión cerrada. C_auth_base, recursos, capacidad, información, dominio y bloqueos deben clasificarse y descomponerse; no se agrupan en C_other. R_access* solo incluye disponibilidad de recursos necesarios para poner τ2 a disposición, no el consumo de una ejecución. D_support* representa soporte del dominio/tipo de objeto, no precondiciones particulares de S0. App_f no redefine A_f.

C_dep* = C_install* ∧ C_integrity* ∧ C_compat* ∧ C_oper*. Los componentes no se presumen independientes. Debe definirse su distribución conjunta de 16 patrones o generador equivalente; el éxito condicional candidato s=.80 no es dato empírico ni calibración aprobada.

### 4.4 Snapshot estructural y evidencia

La verdad estructural y la evidencia observacional son objetos separados:

- S_T*(i,b,c,t) = (U_t*, R_t*, C_t*, X_t*): snapshot estructural verdadero.
- E_T(i,b,c,t) = (Sources, Coverage, Validity_e, Provenance, Version, Timestamp, Adjudication): paquete epistémico de evidencia.
- ΔT_acc* = Diff(S_T*(t0), S_T*(t1)) = (ΔU*, ΔR*, ΔC*, ΔX*).
- ΔE_T = Diff_E(E_T(t0), E_T(t1)).

Una mejora o pérdida de cobertura puede cambiar lo que se conoce sin cambiar el sistema. La validez/cobertura de evidencia no se introduce como componente causal de ΔT_acc*. La formulación histórica que incorporaba ΔValidity queda supersedida para esta definición por §71, conservada solo para trazabilidad.

La identidad, versión, frontera, granularidad, catálogo y mapping deben ser comparables antes del diff. Cambio de captura, cambio estructural, cambio de evidencia y cambio de accesibilidad son distintos.

### 4.5 Reach y trayectorias

Reach_H* (truth) y Reach_H,obs (clasificación del analizador) permanecen separados. La admisibilidad de una ruta exige identidad/versiones, accesibilidad de cada transformación, aplicabilidad en cada estado intermedio, composición válida, recursos/autorización, temporalidad, ventanas y frontera/G compatibles.

Lógica trivalente:
- Ruta=1 solo si todos los predicados necesarios están respaldados.
- Ruta=0 solo si algún predicado necesario está refutado con evidencia/cobertura suficiente.
- Ruta=? en los demás casos.
- Reach=1 si existe ruta confirmada.
- Reach=0 solo si todas las rutas relevantes están descartadas y el universo operativo está cubierto.
- Reach=? si queda ruta desconocida, indeterminada o cobertura incompleta.

Reach_H− y Reach_H+ delimitan estados con ruta confirmada y estados con ruta confirmada/no refutada; no son intervalos probabilísticos. F_alt=0 requiere cobertura suficiente de todas las rutas funcionalmente substituibles del universo delimitado. No encontrado no significa ausente.

El reloj del estudio t0–t9 es distinto de la profundidad de trayectoria k=0…H. H=3 es profundidad máxima candidata, no duración temporal aprobada. Reach se deriva de snapshots y reglas previas a selección/ejecución; nunca se infiere de trayectorias ejecutadas observadas.

## 5. Intervención B, alternativas y comparadores D1/D2

### 5.1 B y vías colaterales

B provisiona/configura la dependencia focal. No ejecuta F1/F2 ni A1/A2, no modifica F*, el oráculo, los datos funcionales, permisos funcionales ni rutas alternativas. El manifiesto B-M01…15 debe cubrir artefacto, runtime, host, interfaz, permisos, datos, recursos, red, seguridad, observabilidad, estado, rendimiento, oráculo, alternativas y reversibilidad.

ARCH-B1 (sidecar/runtime aislado, aditivo, versionado, permisos mínimos y cuotas propias) es una arquitectura recomendada para evaluar, no aprobada ni instalada. El inventario real no existe aún: NO INVENTARIADO no equivale a ausencia. La independencia de A1/A2 respecto de B debe demostrarse mediante grafo transitivo, snapshots preB/postB/rollback y comportamiento funcional. Si B afecta rutas, recursos, permisos, seguridad, latencia, costes, información o dependencias compartidas, hay vía colateral y el ITT es efecto de paquete salvo identificación adicional.

### 5.2 D1 y D2

| Parámetro | D1: provisión ordinaria en control | D2: sin intento focal en control |
|---|---:|---:|
| P(W_attempt=1 | Z=0) | .25 | 0 |
| P(W_attempt=1 | Z=1) | 1 | 1 |
| P(S_success=1 | W_attempt=1) | .80 | .80 |
| P(C_dep,post=1 | Z=0) | .20 | 0 |
| P(C_dep,post=1 | Z=1) | .80 | .80 |
| Primera etapa de C_dep | .60 | .80 |

Estos valores son objetivos candidatos del DGP, no hechos empíricos. El .80 es éxito técnico conjunto condicional; no cuatro probabilidades marginales independientes. El .20 de D1 es estado final postasignación derivado de .25×.80, no accesibilidad basal.

**Precedencia vigente por DEC-C10-066:** D2 es el escenario primario candidato para el contraste mecanístico de provisión focal frente a ausencia de intento focal en control; D1 queda como escenario secundario para el contraste incremental frente a provisión ordinaria de baja frecuencia. La justificación del régimen ordinario D1 es requisito para interpretar ese comparador secundario, no para decidir la precedencia primaria. La legitimidad de D2 sigue condicionada a verificar ausencia basal y ausencia de provisión focal de fondo. ITT, primeras etapas y compliers de D1/D2 no se agrupan ni transportan automáticamente.

### 5.3 Población, régimen y unidad

- P*_τ2: población de apertura focal elegible con A_f,base*=0 respaldada antes de Z.
- P*_F: subpoblación sin alternativa funcional substituible basal bajo F*; no es filtro automático de P*_τ2.
- q_X*: distribución común candidata de condiciones/historias basales y constitutivas; no incluye Value ni variables postratamiento.
- q_L*: alternativa secuencial solo si se requiere intervenir/estandarizar historia postasignación con reglas y soporte identificables.
- C_c: condiciones constitutivas para factibilidad.
- L_m: condiciones temporales según su papel causal; no ajustar mecánicamente por mediadores/confusores postratamiento.
- UE, UA, UO, clúster y mapa de interferencia deben declararse. UE=UA individual solo si la independencia entre unidades se sostiene. Si existen recursos/canales compartidos, considerar asignación por clúster o estimando de exposición. No asumir SUTVA.

## 6. Jerarquía causal y estimandos

Se conservan como objetos distintos:

1. ITT-A: efecto de asignación sobre accesibilidad observada/verdadera según el estimando y medición declarados.
2. ITT-O: efecto de asignación sobre Outcome.
3. ITT-V: efecto de asignación sobre cada dimensión de Value.
4. Primeras etapas separadas sobre C_dep, A_f,post*, D_f* y ΔT_acc*.
5. ψ_policy: efecto de la política/paquete cuando B activa vías adicionales.
6. LATE_f para O o V: efecto local entre compliers inducidos, solo bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia y medición válida.
7. θ_Af(q*): contraste focal de políticas de accesibilidad bajo régimen común factible y vías colaterales separadas.
8. θ_A(q): pregunta general C10-D1 sobre políticas que modifican accesibilidad transformacional; S4-R focalizado en τ2 no la sustituye.
9. Efecto conjunto/θ_L,A cuando condiciones y accesibilidad no pueden separarse.

La aleatorización identifica el ITT de la política, no demuestra exclusión ni mediación. Un instrumento fuerte no garantiza validez. No extrapolar LATE a ATE/ATT ni equiparar LATE D1/D2. No calcular un efecto residual como TE−θ_A(q) sin identificación propia. Si hay vías directas/colaterales, reportar efecto de política/paquete y límites de atribución.

## 7. DGP, escenarios adversariales y medición de Value

### 7.1 Verdad y roles

El generador conserva potenciales, estados estructurales, C_dep, A_f*, D_f*, rutas, alternativas, parámetros y mecanismos ocultos. El analizador recibe solo datos/evidencia observables. El evaluador compara con truth después de congelar la salida del analizador. La verdad no se filtra al analizador.

### 7.2 Escenarios que deben discriminarse

Incluir efectos focales positivos, nulos y adversos; primera etapa nula/débil/fuerte; incumplimiento, intentos fallidos y fallos parciales; efectos directos δ; interacción política×accesibilidad γ; rutas alternativas afectadas; monotonicidad/defiers; heterogeneidad τ_i; interferencia/exposición; errores de medición diferenciales; missingness, censura, selección postasignación y soporte/positividad insuficiente.

La sensibilidad δ/γ debe usar rangos justificados y cotas de efectos compatibles; no confundir intervalos de sensibilidad con intervalos de confianza. La clasificación debe distinguir atribución robusta, atribución condicionada, efecto de paquete, identificación insuficiente e indeterminación. El analizador no tiene que detectar supuestos no identificables solo con datos observados; debe reconocer límites de inferencia.

### 7.3 Heterogeneidad y compliers

El efecto individual τ_i puede variar con condiciones iniciales, recursos, alternativas, complementariedades, contexto y unidad. D1 y D2 pueden inducir estratos de compliers diferentes; sus LATE pueden diferir por composición, no solo por fuerza del instrumento. No asumir que ambos estiman el mismo efecto ni que representan el ATE.

### 7.4 A, O y V

A, O y V se miden independientemente:
- A: accesibilidad estructural; no se define por ejecución exitosa.
- O: ejecución, resultado inmediato y consecuencias operativas se separan; cada indicador tiene unidad, fuente y ventana.
- V: valoración contextual por observador/beneficiario, criterio, regla, dimensiones y horizonte; no se deriva mecánicamente de O.

Las cinco dimensiones candidatas de Value son eficiencia, calidad, acceso de destinatarios, robustez y sostenibilidad. Se mantienen provisionales: el vector multidimensional es la opción metodológica recomendada durante identificación; índice escalar solo secundario, si se justifican escalas, pesos, compensabilidad y sensibilidad. No elegir reglas tras observar resultados.

Validez, fiabilidad interevaluador/temporal, error de clasificación, sensibilidad, invariancia entre D1/D2, brazos, perfiles y escenarios adversariales, y trazabilidad de reglas forman parte del diseño, no de una validación ya realizada.

### 7.5 Ausencia, censura y selección

Distinguir ausencia de registro, fallo técnico, abandono, censura administrativa/informativa, indefinición estructural y medición inválida. Evaluar MCAR/MAR/MNAR, selección postasignación, pérdida de A, O y V, y efecto sobre cada estimando. Mantener población aleatorizada para ITT. No convertir desconocido en cero, inaccesible, no ejecución o Value nulo. Aplicar cotas/sensibilidad si son defendibles; si no, declarar no-identificación por estimando/dimensión.

## 8. Diseño estadístico: arquitectura existente y cierre cuantitativo pendiente

La arquitectura estadística existe en la fuente 165–183 y en los contratos asociados; no debe describirse como inexistente. Lo pendiente es convertirla en especificación cuantitativa preespecificada, coherente con el DGP y el estimando primario que se acepte.

Debe cerrarse:
1. Jerarquía confirmatoria/secundaria y multiplicidad.
2. Estimación separada ITT-A, ITT-O e ITT-V por dimensión; primera etapa; Wald/LATE para O y V cuando proceda.
3. Inferencia robusta a instrumento débil; intervalos/conjuntos adecuados para IV y reglas ante primera etapa nula/débil.
4. Heterogeneidad, pesos de compliers, diferencias D1/D2 y límites de transporte a ATE/ATT.
5. Sensibilidad de exclusión mediante δ, interacción γ y vías alternativas; cotas de efectos compatibles, separadas de incertidumbre muestral.
6. Tamaño muestral por búsqueda en cuadrícula de escenarios, eligiendo el menor N que satisfaga simultáneamente potencia y precisión para los estimandos prioritarios.
7. Potencia/precisión por separado para ITT, primera etapa, LATE y clasificación de escenarios adversariales.
8. Si hay clústeres, incorporar ICC, efecto de diseño y número efectivo de clústeres; no dimensionar por N bruto solamente.
9. Número de réplicas R determinado por error Monte Carlo deseado para sesgo, cobertura y tasas de clasificación; reportar SE_MC.
10. Métricas: sesgo, RMSE, cobertura, error tipo I, potencia, calibración, convergencia, réplicas inválidas y clasificación correcta de identificación/no-identificación.
11. Justificación ex ante de efecto mínimo detectable, efecto mínimo relevante, margen de equivalencia, δ/ε, tolerancias y reglas de inconclusión.
12. Semilla maestra y derivación determinista por escenario, configuración y réplica; hashes de DGP, analizador, reglas, parámetros y salidas.

N=2.000, asignación 1:1 y R=1.000 son valores históricos ilustrativos, no parámetros confirmatorios aprobados. La selección de N/R debe seguir el procedimiento de búsqueda y precisión Monte Carlo; no fijarse por conveniencia ni adaptarse tras ver resultados.

No significación no demuestra equivalencia. Precisión insuficiente no refuta hipótesis. Un tamaño mayor no repara violaciones de identificación, sesgo estructural o validez de constructo.

## 9. U_G y contratos de evidencia

U_G es infraestructura para inventario, observaciones, procedencia, cobertura, evaluación y adjudicación; no es el generador de truth. El catálogo de 23 roles de nodo, 23 aristas candidatas, predicados y clases de ruta es universo de inspección candidato, no inventario real ni prueba de exhaustividad. La cobertura efectiva es NONE donde no existen fuentes observadas; estados técnicos A_f*, Reach_H y F_alt permanecen ?.

DEC-C10-059…065 aceptan documentalmente elementos del esquema U_G, incluida Opción A y pinning exacto de SNAPSHOT. UG-SCH-10 sigue OPEN; no hay schema freeze, motor fijado, DDL, parser, validadores, fixtures ni pruebas físicas. PASS_FORMAT_ONLY de tablas Markdown no es validación técnica.

La relación entre U_G físico y la ruta crítica de C10-S debe evaluarse explícitamente: no se debe imponer DDL/parser como prerequisito científico si el experimento puede preservar el mismo contrato de verdad/observación/procedencia mediante una implementación autorizada equivalente. Tampoco se debe omitir U_G si es necesario para reconstruir los snapshots y evidencias del diseño. Esta decisión de arquitectura de implementación queda abierta hasta cerrar el crosswalk técnico.

## 10. Secuencia de cierre y autorización

| Orden | Bloque | Resultado exigido | Estado |
|---|---|---|---|
| 1 | Alineación maestro-plan | Plan Draft 004 refleja §§53–130 y la integración 130–183 sin regresiones | ESTE PLAN |
| 2 | Crosswalk documental | Maestro ↔ Decision Log ↔ DGP ↔ estimandos ↔ Closure Matrix ↔ Test Register ↔ auxiliares | EN CURSO |
| 3 | Arquitectura causal | B, D1/D2, g0/g1, q, población, estimandos y vías colaterales | ABIERTO |
| 4 | Arquitectura transformacional | T_cap/T_acc(i,t), A_f/App_f/D_f, snapshots, ΔT/ΔE, Reach, rutas y F* | PARCIAL |
| 5 | DGP completo | potenciales, distribución conjunta técnica, heterogeneidad, δ/γ, escenarios y truth oculta | PARCIAL |
| 6 | Medición | A/O/V, validez, fiabilidad, error, invariancia, ausencia/censura | PARCIAL |
| 7 | Diseño estadístico | N, potencia, precisión, R, error Monte Carlo, weak-IV, cotas, multiplicidad y decisión | ABIERTO |
| 8 | Contratos de aceptación | P177/P178/P179, P182/P183, S4R, PM, SNAP, REACH, PROV, GC y U_G | PARCIAL |
| 9 | Autoauditoría de no-regresión | revisión asistida propia, trazabilidad, pruebas estáticas/documentales con alcance declarado | PENDIENTE |
| 10 | Freeze/aprobación documental | estimandos, DGP, medición, estadística, criterios, hashes y riesgos residuales preespecificados | NO ALCANZADO |
| 11 | Implementación/validación técnica | motor, parser, DDL/estructura equivalente, fixtures y validadores bajo autorización específica | NO AUTORIZADO |
| 12 | Simulación/experimento | generación, análisis ciego, evaluación, auditoría, replay y resultados bajo autorización expresa | NO AUTORIZADO |

La revisión externa R1/R2 no es requisito para avanzar ni para ejecutar un experimento sintético autorizado. Toda autoauditoría se etiqueta como no independiente. La independencia requerida entre generador, analizador y evaluador se garantiza mediante separación de datos, permisos, procesos y hashes, no mediante una afirmación de revisión humana externa.

## 11. Criterios de salida científica

C10-S debe poder distinguir sin forzar resultados:
- contribución focal recuperada bajo supuestos satisfechos;
- efecto de política/paquete identificado pero atribución focal no identificada;
- contribución focal positiva, nula o adversa dentro del ámbito preespecificado;
- efecto local/heterogéneo sin extrapolación indebida;
- identificación parcial mediante cotas;
- no-identificación o indeterminación;
- recuperación estadística insuficiente de un estimando identificado;
- fallo de validez de constructo o de la arquitectura sintética.

Un PASS de C10-S acredita solo la capacidad del procedimiento dentro de los DGP, parámetros, poblaciones, políticas, horizontes y reglas de Value evaluados. No demuestra por sí mismo la hipótesis empírica general C10.

## 12. Estado y siguiente operación

La información histórica está integrada; no se abre una nueva recuperación. Draft 004 es la guía operativa. DEC-C10-066 ha resuelto la precedencia del comparador: D2 es primario candidato y D1 secundario. La siguiente operación científica es cerrar la arquitectura causal y los estimandos/políticas factibles: θ_A(q), θ_Af(q*), ITT/LATE/ψ_policy, q_X*, B_g0/B_g1, C_auth y las condiciones de legitimidad/identificación de D2 y D1; no se reabre la selección primaria. La propagación documental de DEC-C10-066 debe mantenerse sincronizada en los contratos auxiliares.

No se cambia main, Core, RMA, Evidence→Claim Matrix, STATUS, claims ni C09. No se implementa, simula ni ejecuta el experimento.

**Autorización:** scientific_execution=false; execution_authorized=false.


## 13. Decisión aceptada sobre el escenario primario candidato (2026-11-06)

DEC-C10-066 acepta **D2 como escenario primario candidato** para el contraste mecanístico de provisión técnica focal frente a ausencia de intento focal en control. **D1 queda como escenario secundario** para el contraste incremental frente a provisión ordinaria de baja frecuencia.

Esta decisión posterior supersede las formulaciones anteriores de §§5.2 y 12 solo en cuanto mantenían abierta la selección del escenario primario candidato o recomendaban D1 como principal condicionado. No borra el historial ni elimina D1. Los parámetros de intento y éxito, incluido (s=0.80), siguen siendo candidatos no validados.

La aceptación no resuelve la correspondencia (B_{g0}/B_{g1}leftrightarrow g_0/g_1), la jerarquía definitiva de estimandos, (q_X^*), poblaciones, horizonte, regla de Value, vías colaterales o identificación. ITT, primeras etapas y LATE/Wald permanecen específicos de cada comparador.

**Estado actualizado del bloque 3:** la selección del escenario primario candidato queda resuelta; la arquitectura causal y los estimandos permanecen **ABIERTO** hasta cerrar políticas materiales, régimen (q), poblaciones, estimandos y vías colaterales.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.


## 14. Precedencia y continuidad tras DEC-C10-067 (2026-11-06)

DEC-C10-067 acepta las definiciones materiales conceptuales de (B_{g0}^{D2}) y (B_{g1}^{D2}). El siguiente bloque debe resolver invariantes verificables y vías colaterales de la provisión, y concretar los campos operativos pendientes (actor, artefacto/hash, recepción, ventanas, reintentos, evidencia de componentes y detección de provisión de fondo). No reabrir la precedencia D2 primario candidato/D1 secundario de DEC-C10-066.

La aceptación no valida (s=0.80), parámetros, estimandos, población/soporte, unidad/interferencia, exclusión ni identificación. No autoriza freeze, implementación, simulación ni ejecución científica.


---

## 15. Control de continuidad, recuperación y persistencia del bloque de invariantes y vías colaterales

**Estado:** addendum de coordinación documental asistida; DRAFT / NO APROBADO / NO CONGELADO.  
**Fecha de corte:** 2026-11-06.  
**No constituye:** decisión científica nueva, cierre de auditoría, validación independiente, autorización de implementación, simulación o ejecución.  
**Precedencia:** conserva DEC-C10-066 (D2 primario candidato; D1 secundario) y DEC-C10-067. No reabre ni amplía su alcance.

### 15.1. Regla de continuidad operativa propuesta

GitHub es la fuente de verdad. La conversación y la memoria solo sirven como ayudas de recuperación y nunca sustituyen un artefacto canónico. Cada unidad de trabajo C10-S debe cerrar un ciclo documental verificable antes de iniciar la siguiente:

1. **Recuperar:** leer desde GitHub `main` el README de gobernanza, bootstrap y estado canónico; leer desde la rama C10-S el plan, maestro, Decision Log, Closure Control Matrix y artefactos especializados directamente afectados.
2. **Reconciliar:** contrastar el trabajo nuevo con decisiones aceptadas, propuestas, artefactos históricos y estado real de la rama/PR. Reutilizar lo compatible; no duplicar ni sustituir semántica silenciosamente.
3. **Resolver:** delimitar el objeto de trabajo, las alternativas, dependencias, contradicciones y estado epistemológico. Una contradicción bloqueante se resuelve antes de avanzar.
4. **Registrar:** incorporar el resultado en el artefacto existente más adecuado de la rama C10-S, o justificar expresamente la creación de uno nuevo. Una conclusión material no debe quedar solo en la conversación.
5. **Verificar:** recuperar de GitHub cada archivo modificado y comprobar contenido, blob SHA, commit, diff y PR. No declarar persistencia antes de esta comprobación.
6. **Comunicar:** informar por separado qué se recuperó, qué se reconstruyó, qué se persistió, qué se verificó y qué permanece abierto.

La reconstrucción desde memoria debe etiquetarse como tal cuando no exista fuente primaria recuperable. Nunca debe presentarse como transcripción literal, ficha original ni auditoría íntegra.

### 15.2. Estado de recuperación de las fichas de invariantes

La inspección de los artefactos actuales confirma que el maestro consolidado, §§46–47, contiene una arquitectura preliminar de condiciones de elegibilidad y clasificación: `C_auth,base`, `C_resource`, `C_capacity`, `C_info`, `C_domain`, `C_other,j`, `C_dep,0` y `A_f,0*`; incluye regla conjuntiva, estados cumplida/incumplida/indeterminada/no aplicable y pruebas ELIG-01…12. También distingue condiciones estructurales de calidad/cobertura de evidencia. Estos contenidos son antecedentes útiles, pero el propio maestro declara que cada condición requiere ficha operacional completa.

La recuperación conversacional disponible aporta solo una **reconstrucción parcial**, no el texto original completo:

| Objeto | Recuperación disponible | Límite que debe conservarse |
|---|---|---|
| `C_auth,base` | Se recuperó el identificador conversacional `D2-INV-AUTH-01`, autorización normativa basal por unidad×ventana, evidencia de titular/alcance/vigencia/objeto/versiones y falsador basado en cambio diferencial inducido por B. | No se recuperó la ficha literal completa, sus campos íntegros ni la totalidad de sus pruebas. |
| `C_resource` | Se recuperó la separación entre disponibilidad basal, capacidad instalada, consumo de ejecución y recursos usados por B; desplazamiento de recursos de rutas alternativas como vía potencial. | No se recuperaron literalmente ID, umbrales, ventanas, fuentes, adjudicación ni batería completa de pruebas. |
| `C_capacity` | Se recuperó la separación entre capacidad instalada, disponible, reservada, consumida y margen; `K_available ≥ K_required` como criterio candidato, no validado. | No se recuperaron literalmente ID, dimensionalidad completa, reglas de agregación ni pruebas completas. |
| `C_info` | Se recuperó la separación entre información técnica constitutiva, conocimiento del agente, comunicación inducida por B y observabilidad/evidencia del evaluador; riesgo de vía `B→K→Selection→Execution`. | Se conocen referencias conversacionales a I-INFO-01…06, pero no su texto literal ni correspondencia completa. No deben reconstruirse como fichas originales. |
| Otras condiciones/invariantes | El maestro aporta `C_domain`, `C_other,j`, `C_dep*`, `A_f*` y elegibilidad. | No se puede afirmar que el conjunto de fichas conversacionales se limite a las cuatro filas anteriores ni que estas agoten el paquete generado. |

**Dictamen de recuperación:** las fichas desarrolladas que se elaboraron en conversación no se han recuperado íntegramente desde los artefactos GitHub inspeccionados ni desde el contexto conversacional disponible. Lo anterior conserva una síntesis parcial verificable y sus límites; no reemplaza ni certifica las fichas originales. Queda pendiente recuperar la versión íntegra o reconstruirla explícitamente, campo por campo, con trazabilidad y sin atribuir literalidad.

### 15.3. Estado de recuperación de la auditoría de vías colaterales

Se han localizado y contrastado los siguientes artefactos que contienen partes sustantivas de la auditoría:

- `C10_S_CAUSAL_ARCHITECTURE_RECONCILIATION_DRAFT_001.md`: jerarquía de estimandos, efecto de política/paquete y condiciones de atribución.
- `C10_S_MICRODOMAIN_CAUSAL_COMPATIBILITY_AUDIT_DRAFT_001.md`: compatibilidad causal de Opción A, riesgos de B, independencia de A1/A2 y separación de objetos.
- `C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md`: superficies B-M01…15, grafo transitivo, snapshots preB/postB/rollback y contratos PROV.
- `C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md`: universo candidato U_G, nodos/aristas, cobertura y cinco clases de ruta: focal, alternativa, compartida, externa y desconocida.
- Maestro consolidado, especialmente §§53–54 y §§61–67, y `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`, especialmente el crosswalk FCM-D2-01…10.

La reconstrucción recuperable de la lógica causal de auditoría distingue: (i) vía focal de provisión hacia dependencia, accesibilidad y transformaciones accesibles; (ii) cambios inducidos en condiciones constitutivas no focales; (iii) cambios en rutas alternativas, recursos o dependencias compartidas con consecuencias para Reach, trayectoria, ejecución, Outcome o Value; (iv) vías de información/conocimiento/selección; y (v) cambios epistémicos de observación, cobertura o adjudicación, que no deben confundirse con cambios estructurales. Esta es una clasificación analítica de mecanismos, no el catálogo de clases de ruta U_G. Por separado, U_G define cinco clases de ruta: focal, alternativa, compartida, externa y desconocida. Ninguna de las dos clasificaciones sustituye el inventario detallado de nodos, aristas, pruebas y evidencias.

La auditoría conceptual disponible requiere, entre otros elementos, manifiesto real de componentes y versiones, grafo transitivo, snapshots comparables preB/postB/rollback, cambios de permisos, recursos, red, seguridad, estado, rendimiento, información y rutas alternativas, además de pruebas de comportamiento e independencia funcional. Los estados `NO INVENTARIADO`, `?` o cobertura `NONE/PARTIAL` no equivalen a ausencia ni a PASS. Si B cambia vías distintas de accesibilidad, el contraste es efecto de paquete salvo estrategia adicional de identificación.

**Dictamen de recuperación:** se han recuperado los artefactos y la arquitectura conceptual de la auditoría, pero no se ha certificado que reproduzcan íntegramente la auditoría conversacional desarrollada ni todas sus fichas de prueba, evidencias y reglas de adjudicación. El texto original completo de esa auditoría permanece **NO RECUPERADO ÍNTEGRAMENTE**. No se declarará independencia de B, ausencia de vías colaterales ni cierre de MD-C1/MD-C4 por esta reconstrucción documental.

### 15.4. Próximo trabajo documental y reglas de no-regresión

El siguiente bloque debe cerrar, en este orden:

1. Localizar en los artefactos de la rama cualquier ficha detallada adicional y cotejarla contra la síntesis de §15.2, evitando duplicados.
2. Recuperar la fuente íntegra de las fichas y de la auditoría conversacional si está disponible; si no, reconstruir cada ficha desde sus campos y fuentes, marcando cada elemento como recuperado, inferido o pendiente.
3. Consolidar una matriz única de invariantes con ID estable, definición operacional, unidad/ventana, papel causal, fuente, procedimiento, temporalidad, evaluador/cegamiento, estados 1/0/?/NA, evidencia, falsadores, pruebas adversariales y trazabilidad.
4. Completar el crosswalk de cada invariante y cada vía colateral hacia B-M01…15, PROV, U_G, predicados, Reach/alternativas, estimandos y filas FCM-D2 correspondientes.
5. Distinguir invariancia postulada en el DGP, invariancia definida contractualmente y no-afectación empíricamente demostrada. Ninguna de ellas se infiere de la otra.
6. Registrar la reconciliación en el maestro y en los artefactos afectados en un mismo ciclo documental, sin alterar DEC-C10-066/067 ni convertir propuestas en decisiones aceptadas.
7. Antes de pasar a implementación o ejecución, exigir revisión explícita de los contratos y autorización separada. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

**Estado de salida de este addendum:** continuidad operativa propuesta y laguna documental identificada; fichas conversacionales completas y auditoría conversacional íntegra aún no recuperadas; no se declara cierre científico ni técnico.


---

## 16. Estado de recuperación y siguiente fase de cierre

**Corte:** 2026-11-06. **Origen:** contenido detallado aportado por el usuario en la conversación de continuidad C10-S. Se conserva su contenido sustantivo, sin atribuirle literalidad histórica. **Estado:** DRAFT / NO APROBADO / NO CONGELADO / NO IMPLEMENTADO / NO EJECUTADO.

### 16.1. Recuperación y persistencia documental

Este apartado actualiza los dictámenes de §15.2–15.3: las fichas D2 y la auditoría causal que antes solo estaban parcialmente recuperadas han sido aportadas en esta conversación y persistidas en los artefactos existentes:

- `C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md`, §13: `D2-INV-AUTH-01`, `D2-RES-01`, `D2-CAP-01`, clasificación `D2-C_INFO` e invariantes adversariales `I-INFO-01…06`.
- `C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md`, §12: auditoría causal D2, B-M01…15, taxonomías de ruta/mecanismo, pruebas de separación, evidencia y consecuencias para estimandos.

Se ha reutilizado la matriz temporal y el manifiesto existentes; no se ha creado una matriz general duplicada ni una auditoría paralela. La persistencia actualiza el estado de recuperación documental de §15, pero no aprueba las fichas ni demuestra invariancia, aislamiento o ausencia de vías colaterales.

### 16.2. Estado científico de las fichas y la auditoría

Las cuatro fichas/clasificaciones siguen siendo propuestas: autorización basal `C_auth,base`; recursos no focales; capacidad no focal; y clasificación de información técnica, conocimiento del agente, comunicaciones de B y evidencia del evaluador. No se añade todavía `C_info` como predicado autónomo de `A_f*`. Los detalles, criterios, falsadores y contratos I-INFO-01…06 están en la matriz §13.

La auditoría del manifiesto §12 distingue la taxonomía topológica U_G (focal, alternativa, compartida, externa, desconocida) de los mecanismos causales (focal, cambio constitutivo, vía colateral a resultados y cambio epistémico/informativo). El ITT sigue siendo efecto de la política asignada; la atribución exclusiva a `ΔT_acc*` requiere excluir o identificar otras vías.

Inventario real, grafo transitivo, snapshots pre-B/post-B/rollback y pruebas materiales de no-afectación siguen pendientes. `NO INVENTARIADO`, `?`, `NONE` o `PARTIAL` no significan ausencia ni PASS. ARCH-B1 es recomendación, no instalación aprobada. MD-C1 y MD-C4 permanecen abiertos.

### 16.3. Crosswalk y siguiente operación documental

El crosswalk causal B-M01…15 → variable/predicado → clase U_G → mecanismo → evidencia/PROV → cadena/estimando → FCM-D2 está incorporado en C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md, §31. Su correspondencia con los IDs existentes N01–N23, E01–E23 y predicados de la matriz de cobertura está registrada en C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md, §9. Se reutilizan el manifiesto §3/§12, U_G y PROV-01…12. Es trazabilidad candidata, no inventario real ni prueba de aislamiento.

La aplicación del mapping a la plantilla está incorporada en C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md, §17. Define la correspondencia B-M01…15 con NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK/COVERAGE_REGISTER, sin convertir dominios de auditoría en objetos U_G ni crear observaciones. Reserva scopes lógicos COV-D2-BM01…15 en estado NONE, con denominador UNKNOWN; son planificación, no filas físicas ni evidencia.

La auditoría cruzada se completó el 2026-11-06; sus resultados, límites y correcciones se registran en §16.5. La siguiente operación es auditar la trazabilidad causal individual de las fichas de invariantes: definición y clase temporal → predicado/condición del DGP → dominio B-M → contrato PROV → objeto/arista/ruta U_G → evidencia/falsador → mecanismo causal y estimando afectado → control FCM-D2. Debe resolver solapamientos sin crear símbolos ni predicados duplicados, y distinguir invariancia postulada, exigencia contractual y no-afectación demostrada. No materializar inventario técnico hasta disponer de una instancia/versión concreta y fuentes accesibles. MD-C1/MD-C2/MD-C4 siguen abiertos.

### 16.4. Cierre científico-operacional previo a implementación

C10-S permanece en fase de cierre de diseño. Los ocho bloques pendientes son:

1. Arquitectura: reconciliar condiciones, relaciones, bloqueos y solapamientos entre `R_access*`, `D_support*`, `C_dep*` y predicados.
2. Contraste causal: formalizar ITT D2, estimando de accesibilidad, régimen común y vías alternativas.
3. Población/unidad/soporte: elegibilidad, asignación/análisis, versiones `τ2`, consistencia, interferencia, cumplimiento y compliers.
4. Medición: `T_acc`, Reach, trayectorias, ejecución, Outcome y Value; fuentes, ventanas, adjudicación y separación verdad DGP/observación.
5. DGP/parámetros: ecuaciones, dependencias, heterogeneidad y probabilidades; justificar o sustituir `s=.80`, aún no validado.
6. Análisis/identificación: P177/P178/P179/P182/P183, efectos directos/indirectos, confusión inducida, mediadores, selección, sensibilidad y falsadores.
7. Validación/potencia: escenarios con verdad conocida, recuperación de efectos, detección de vías colaterales, errores, robustez, N y potencia.
8. Contrato/autorización: especificación ejecutable, entradas/salidas, trazabilidad, reproducibilidad, aceptación, pruebas negativas y autorización separada.

Secuencia: arquitectura → población/unidad/soporte/políticas → estimandos/identificación → mediciones/DGP → análisis/sensibilidad/potencia → validación/especificación → decisión separada de autorización.

El hito previo será un **C10-S Design Freeze Candidate** con arquitectura causal reconciliada; DGP y parámetros justificados; población/unidad/soporte; estimandos/supuestos; contratos de medición/análisis; escenarios de validación/falsación; y criterios de aceptación/no identificación. No basta con nombrar variables: debe saberse qué cambia materialmente, cómo separar accesibilidad de otros efectos, qué miden los instrumentos, qué identifica el diseño y si el analizador recupera la verdad causal.

**Límites:** no se aprueban fichas, no se validan parámetros, no se declara Design Freeze Candidate ni readiness de implementación. Se mantienen `scientific_execution=false` y `execution_authorized=false`. D2 sigue primario candidato y D1 secundario; DEC-C10-066/067 no se reabren.


### 16.5. Resultado de auditoría cruzada de invariantes, provisión y U_G (2026-11-06)

**Estado:** auditoría documental cruzada completada; DRAFT / NO APROBADA / NO CONGELADA. No es auditoría técnica de una implementación ni validación científica.

#### 16.5.1. Artefactos y contenido verificados

| Artefacto | Contenido comprobado | Estado |
|---|---|---|
| `C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md`, §13 | `D2-INV-AUTH-01`, `D2-RES-01`, `D2-CAP-01`, clasificación `D2-C_INFO`, contratos `I-INFO-01…06` | Presente y recuperado |
| `C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md`, §12 | Vía focal, B-M01…15, cinco clases topológicas U_G separadas de cuatro mecanismos causales, pruebas de separación, evidencia y consecuencias para estimandos | Presente y recuperado |
| `C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md`, §9 | Crosswalk de los quince dominios hacia N01–N23, E01–E23, predicados, rutas y PROV | Presente y recuperado |
| `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`, §31 | Crosswalk B-M01…15 → variable/mecanismo/evidencia/estimando/FCM-D2 | Presente y recuperado |
| `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md`, §17 | Correspondencia de B-M01…15 con NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y registros de evidencia/cobertura; scopes COV-D2-BM01…15 | Presente y recuperado |

El registro de continuidad §16.1–16.2 queda confirmado en cuanto a la localización de fichas y auditoría. La recuperación de esos artefactos no implica que las fichas estén aprobadas ni que la auditoría material se haya ejecutado.

#### 16.5.2. Divergencias documentales detectadas y corregidas

1. La tabla de §17.2 de la plantilla omitía o no explicitaba varios roles/aristas candidatos presentes en el crosswalk rector de cobertura §9 (entre otros, B-M04, B-M06, B-M07, B-M08 y B-M14). Se reconciliaron las quince filas B-M01…15 con los candidatos Nxx/Exx y clases de ruta de §9. Las identidades siguen siendo candidatas; no se crean registros observados.
2. La matriz de cobertura §9 y la matriz de cierre §31 conservaban instrucciones históricas que pedían aplicar el mapping o construir la matriz de cobertura, pese a que esos artefactos ya existían. Ambas instrucciones se actualizaron para registrar la aplicación en plantilla §17 y la auditoría cruzada completada.
3. Se preservó la distinción entre cinco clases topológicas de ruta (focal, alternativa, compartida, externa, desconocida) y cuatro mecanismos causales de adjudicación (focal, cambio de condición constitutiva, vía colateral a resultados, cambio epistémico/informativo). No se fusionaron en una taxonomía única.
4. Se comprobó que las quince filas lógicas `COV-D2-BM01…15` se presentan como planificación de cobertura, no como registros físicos: denominador UNKNOWN y estado NONE. Los ceros de captura no se interpretan como ausencia de componentes o efectos.
5. Se comprobó que la ficha de autorización mantiene abierta la fuente normativa/alcance/vigencia de `C_auth,base`; recursos y capacidad siguen separados; la clasificación informativa no introduce un `C_info` autónomo en `A_f*`.

#### 16.5.3. Resultado y límites

- **Consistencia documental del mapping:** reconciliada en los artefactos examinados tras las correcciones indicadas.
- **Cobertura de dominios:** 15/15 dominios B-M01…15 tienen trazabilidad conceptual; esto no equivale a cobertura técnica del sistema.
- **Inventario real:** no disponible en esta fase; nodos, aristas, dependencias, consumidores, versiones y snapshots reales siguen sin inventariar.
- **Evidencia empírica de invariancia/no-afectación:** no disponible; no se declara PASS, ausencia, independencia funcional ni aislamiento de B.
- **Estimandos e identificación:** no resueltos por esta auditoría documental; el ITT conserva interpretación como efecto de la política material asignada. La atribución exclusiva a `ΔT_acc*` sigue requiriendo exclusión defendible o identificación adicional.
- **Gates:** MD-C1, MD-C2, MD-C4, AUD-005 y AUD-007 permanecen abiertos. No se cierra DGP, población/soporte, estimandos, medición, potencia ni Design Freeze Candidate.
- **Decisiones:** no se modifica DEC-C10-066 ni DEC-C10-067; no se actualiza Decision Log porque ninguna decisión aceptada ha cambiado.
- **Ejecución:** no se ha inspeccionado ni modificado ningún sistema técnico real; no se han ejecutado validadores científicos, simulaciones ni experimentos. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

#### 16.5.4. Siguiente gate

Realizar el crosswalk causal **ficha por ficha**: definición/clase temporal → predicado y condición del DGP → dominio B-M → contrato PROV → objeto/arista/ruta U_G → fuente/evidencia/falsador → mecanismo causal y estimando afectado → control FCM-D2. El alcance inicial comprende `D2-INV-AUTH-01`, `D2-RES-01`, `D2-CAP-01` y `D2-C_INFO/I-INFO-01…06`; las condiciones adicionales del maestro (`C_domain`, `C_other,j`, `C_dep*`, `A_f*`) se incorporarán solo donde la correspondencia esté respaldada. No crear predicados/símbolos duplicados ni elevar propuestas a invariantes demostradas.


### 16.6. Crosswalk causal ficha D2-INV-AUTH-01 — autorización normativa basal (2026-11-06)

**Estado:** trazabilidad documental individual realizada; ficha DRAFT, no aprobada ni congelada. La fuente normativa concreta y la verificación material permanecen abiertas.

#### 16.6.1. Semántica y predicado protegido

- Ficha: `D2-INV-AUTH-01`, matriz temporal §13.1.
- Predicado: `C_auth,base`; condición constitutiva basal de autorización funcional de la unidad para la transformación focal `τ2`.
- Clase/tiempo: candidata I (invariante respecto de B en el DGP aislado); satisfecha antes de Z y mantenida común hasta la adjudicación postprovisión.
- No equivale a ACL, token, credencial o permiso técnico de instalación/invocación del adaptador; tampoco equivale a conocimiento/consideración del agente.
- Falsador: cambio diferencial inducido por B en la autorización normativa funcional. En ese caso se activa una condición constitutiva adicional y el contraste deja de representar únicamente provisión técnica focal.

#### 16.6.2. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Definición → DGP | `C_auth,base=1`; maestro §§46–47, 59.2, 59.4 y 64.5 | Elegibilidad basal y régimen común; invariancia postulada/contractual, no demostrada |
| Predicado de evidencia | `AUTH-τ2`; matriz U_G §3 y matriz temporal | Pregunta: autorización funcional válida e invariante en t−1/t3; estado actual `?`, cobertura `NONE` |
| Dominio de provisión | B-M05 Permisos; B-M04 Interfaz y B-M09 Seguridad como dominios relacionados | Separar política normativa/permiso funcional de ACL técnica, canal, roles y controles que puedan afectar otras operaciones |
| Contrato PROV | PROV-06; manifiesto §10 | Permisos de B mínimos y sin ampliar `C_auth` funcional; contrato documental, no ejecutado |
| U_G candidato | N17 y E18, más N07/N10/N11/N13/N15 cuando correspondan a principal/operación/consumidor; E18 representa autorización de operaciones | Roles candidatos, no identidades observadas. La asignación B-M05→N17/N07/N10/N11/N13/N15 y E18 está en matriz de cobertura §9 y plantilla U_G §17 |
| Evidencia y falsador | Fuente normativa, titular competente, objeto/operación `τ2`, alcance, vigencia, unidad, ventana y versiones/diffs pre/post | Fuente/alcance/vigencia no resueltos en maestro §59.6. Un diff funcional inducido por B falsifica invariancia; ausencia de evidencia conserva `?` |
| Mecanismo causal | Vía focal no manipulada por autorización; vía adversarial `B→C_auth→A_f*→ΔT_acc*` si B amplía autorización funcional | La segunda es cambio de condición constitutiva, no parte admisible del mecanismo técnico focal D2 |
| Estimando | ITT de la política material D2; atribución específica a accesibilidad | Con `C_auth,base` común y satisfecha, no es la variable manipulada por D2. Si cambia por B, el ITT sigue siendo efecto de política/paquete; la atribución exclusiva a `ΔT_acc*` requiere identificación adicional |
| Control de cierre | FCM-D2-06 y FCM-D2-07 | FCM-D2-06: invariancia candidata, no demostrada. FCM-D2-07: registrar cambios colaterales; evidencia pendiente |

#### 16.6.3. Resolución de la aparente contradicción histórica

La matriz de cierre §4, REC-CAUS-04, conservaba `Z_A→C_auth→A_f*` como modalidad propuesta y dejaba abierto si la política modificaba autorización o provisión. El maestro §64.5 ya distingue expresamente esa modalidad histórica de autorización del escenario primario actual: son diseños diferentes; la primera queda como alternativa histórica/adversarial y no se mezcla con D2 sin decisión explícita. DEC-C10-067 mantiene `C_auth,base=1` común en el DGP D2 aislado y exige que los permisos técnicos de B no amplíen la autorización funcional.

Se actualizó REC-CAUS-04 en la matriz de cierre para reflejar esa delimitación. **No** se declara cerrada la reconciliación causal general: permanecen abiertos q frente a g, legitimidad del comparador, fuente/alcance/vigencia de `C_auth,base`, cumplimiento material de PROV-06 y la demostración de invariancia. No se cambia DEC-C10-066/067 ni se elimina la modalidad histórica.

#### 16.6.4. Dictamen y condición de cierre

La ficha protege el supuesto de que la política D2 no modifica autorización normativa funcional, evitando que una apertura por autorización se confunda con la provisión técnica de `C_dep*). La arquitectura semántica es coherente para el D2 actual; la invariancia material **no está demostrada**. Para cerrar se requiere identificar la fuente normativa competente y su regla de vigencia, comprobar basalmente `C_auth,base=1` en la población elegible y comparar de forma independiente el alcance funcional pre/post B, separando ACL/credenciales técnicas de permisos funcionales. Si el contraste no puede observar esa separación, la clasificación permanece indeterminada y no se afirma aislamiento.

**Siguiente ficha:** `D2-RES-01`, con idéntica cadena de trazabilidad, distinguiendo disponibilidad basal, recursos usados por B, consumidores compartidos y posibles vías a rutas alternativas/interferencia.


### 16.7. Crosswalk causal ficha D2-RES-01 — recursos no focales (2026-11-06)

**Estado:** trazabilidad documental individual realizada; ficha DRAFT, no aprobada ni congelada. No se ha inspeccionado un sistema material, ni demostrado invariancia, no desplazamiento o ausencia de interferencia.

#### 16.7.1. Semántica y reconciliación de predicados

- Ficha: D2-RES-01, matriz temporal §13.2; dominio rector B-M07.
- La ficha separa disponibilidad basal de recursos no focales, capacidad instalada, consumo de ejecución y recursos reservados/consumidos por B.
- Maestro §59.2 distingue explícitamente stock/disponibilidad ex ante de demanda/consumo de ejecución. §59.3 sitúa en R_access* únicamente la disponibilidad ex ante necesaria para poner τ2 a disposición y no duplicada por C_dep* u otro predicado.
- El maestro §46.2 incluye C_resource=1 y C_capacity=1 en una regla ilustrativa de elegibilidad. No se interpreta como autorización para añadir dos factores autónomos a la fórmula depurada de A_f*. Antes del freeze, cada dimensión concreta debe asignarse a (a) R_access*, (b) C_dep*, o (c) aplicabilidad/ejecución, con una sola función causal primaria.
- C_capacity mantiene ficha separada §13.3; su capacidad focal introducida por B pertenece a C_dep*, mientras que capacidad no focal compartida debe evaluarse como condición común y posible vía de interferencia.

#### 16.7.2. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Definición → DGP | Disponibilidad suficiente basal, unidad×recurso×ventana, antes de Z; maestro §§46–47, 59.2–59.4 y 64.5 | Invariancia postulada/contractual en DGP aislado; no demostrada |
| Predicado | R_access*(i,t;τ2); C_resource como descriptor de disponibilidad; consumo de ejecución separado | No crear multiplicadores redundantes. Stock/disponibilidad ≠ demanda/consumo |
| Dominio de provisión | B-M07; B-M02/B-M03/B-M12 relacionados según dependencias transitivas; B-M14 si afecta consumidores alternativos | Crosswalk candidato; no prueba que los componentes o consumidores existan |
| PROV | PROV-05 (no reducción A1/A2/F2), PROV-09 (no modificación de dependencias críticas compartidas), PROV-03/04 (snapshots y grafo transitivo) | Contratos documentales no implementados ni ejecutados |
| U_G candidato | N18, N05, N13, N15, N20; E16, E17, E19; RES-τ2, ALT-DEP, Rshared, Rτ2, RA12 | IDs de rol/candidatos según matriz de cobertura §9; no registros observados |
| Evidencia/falsador | Inventario, asignación, cuotas, reservas, consumo B, compromisos, consumidores y series por unidad/ventana; snapshots pre-B/post-B/rollback | Insuficiencia/compromiso basal, consumo no registrado, desplazamiento/degradación de A1/A2/F2, dependencias o consumidores no cubiertos; cobertura insuficiente → ? |
| Mecanismo | Cambio constitutivo si cambia disponibilidad estructural; vía colateral si afecta rutas alternativas, rendimiento, ejecución, Outcome/Value; interferencia si cruza unidades | Mecanismos potencialmente simultáneos; no adjudicados sin evidencia |
| Estimandos | ITT de la política material D2; efecto específico de accesibilidad de C10-D1; LATE_f solo bajo supuestos IV | Si B afecta recursos no focales, ITT es efecto de política/paquete. No atribuirlo exclusivamente a ΔT_acc*. La aleatorización individual no elimina interferencia por recursos compartidos; la estructura de conglomerados/exposición queda abierta |
| Control | FCM-D2-06/07 y, si afecta alternativas o fondo, FCM-D2-08 | Invariancia candidata; obligación de registrar cambios; comprobación de alternativas pendiente |

#### 16.7.3. Reconciliación de los cuatro objetos

1. **Disponibilidad basal:** puede ser constitutiva de accesibilidad solo si es necesaria para poner τ2 a disposición, está asignada a la unidad/ventana y no está ya representada por C_dep*.
2. **Capacidad instalada/no focal:** propiedad de configuración; su papel de acceso depende de si habilita la oferta, no de la carga concreta de una ejecución.
3. **Consumo de ejecución:** se mide en aplicabilidad/ejecución/calidad según recurso y nivel; no se retrotrae como accesibilidad.
4. **Recursos usados por B:** forman parte de la provisión y se miden separadamente. Si consumen recursos compartidos, pueden afectar A1/A2/F2, Reach, ejecución, Outcome/Value y otras unidades.

#### 16.7.4. Consecuencias causales y regla de salida

- Si solo cambia la dependencia focal y los recursos no focales permanecen comunes, el mecanismo focal sigue siendo candidato, sujeto a los demás supuestos.
- Si B altera disponibilidad basal o capacidad no focal constitutiva, aparece un cambio adicional en condiciones de accesibilidad; el ITT es efecto del paquete y la atribución exclusiva a ΔT_acc* no queda identificada por aleatorización de B.
- Si B desplaza recursos de rutas alternativas o degrada servicios compartidos, existe una vía paralela a Reach/Outcome/Value y posible interferencia.
- Si no puede determinarse el inventario/consumo/consumidores, el estado es ?; no se declara no-afectación, aislamiento ni ausencia.
- No ajustar mecánicamente por recursos/consumo postratamiento como si fueran covariables basales: pueden ser mediadores o co-intervenciones inducidos por B.

**Dictamen:** el crosswalk conceptual de D2-RES-01 está completado y persistido. Permanecen abiertos la operacionalización de suficiencia, la conciliación final de §46.2 con §59.3, inventario y consumidores, PROV-05/09, MD-C1/MD-C4, interferencia/unidad y la atribución específica a accesibilidad. No se modifica DEC-C10-066/067, no se aprueba D2-RES-01 y no se autoriza implementación ni ejecución.

**Siguiente ficha:** D2-CAP-01. El trabajo deberá resolver primero el límite entre capacidad necesaria para ofrecer τ2 (posible condición de acceso), capacidad focal ya contenida en C_dep*, y capacidad/margen dependiente de carga o estado (aplicabilidad/ejecución), sin duplicar R_access* ni C_resource.

### 16.8. Crosswalk causal ficha D2-CAP-01 — capacidad no focal (2026-11-06)

**Estado:** trazabilidad documental individual realizada; ficha DRAFT, no aprobada ni congelada. La capacidad no ha sido operacionalizada ni medida en una implementación real.

#### 16.8.1. Reconstrucción y precedencia semántica

- Ficha temporal §13.3; fuentes: Path Predicate Temporal Evidence Matrix §8, manifiesto §5/§12, maestro §§46–47 y 59.2–59.4/64.5, matriz de cierre §§20/26/29/31 y matriz de cobertura §9.
- Maestro §59.2 diferencia capacidad instalada/slots disponibles para ofrecer τ2 (posible condición de acceso) de margen operativo requerido por S0 o carga concurrente concreta (aplicabilidad).
- §59.3 es la precedencia semántica candidata: capacidad instalada e información técnica solo se incorporan a R_access*/D_support* si son necesarias y no duplican C_dep*. La plantilla C_capacity,i,w de §13.3 no añade por sí sola un factor nuevo a A_f*.
- Capacidad focal introducida por B pertenece a C_dep*. Capacidad no focal común puede formar parte de R_access* solo si se demuestra que es necesaria para poner τ2 a disposición, existe antes de Z, está asignada a unidad/ventana y no está ya contenida en C_dep*.
- La demanda, saturación, cola, consumo o margen de una ejecución concreta no se confunden con la disponibilidad estructural. Se clasifican en App_f*, ejecución/rendimiento o resultado según el mecanismo.

#### 16.8.2. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Definición → DGP | Capacidad instalada, disponible, reservada, consumida y margen; S4-R postula capacidad no focal común/suficiente | Supuesto de diseño, no invariancia demostrada |
| Predicado | Plantilla existente C_capacity,i,w = I(K_available ≥ K_required); posible disponibilidad en R_access* | No convertir en factor autónomo ni en CAP-τ2. Requiere dimensión, unidad, configuración, ventana, demanda y umbral preespecificados |
| Frontera A_f*/App_f* | Capacidad/slots para ofrecer τ2 vs precondiciones de S0/carga/ejecución | Primera puede integrar R_access* si necesaria/no duplicada; segunda pertenece a App_f*/ejecución |
| Dominio B-M | B-M07 rector; B-M02/B-M03/B-M12 relacionados por runtime/host/servicios/colas; B-M14 por rutas alternativas | Mapping candidato sujeto a inventario y grafo transitivo |
| PROV | PROV-05 no reducción A1/A2/F2; PROV-09 no modificación de servicios críticos compartidos; PROV-03/04 snapshots y dependencias | Salvaguardas documentales indirectas; no demuestran capacidad ni aislamiento |
| U_G | N18, N05, N13, N15, N20; E16, E17, E19; RES-τ2, ALT-DEP, Rshared, Rτ2, RA12 | Roles y aristas candidatos del mapping B-M07; no observados ni ampliables por inferencia |
| Evidencia/falsadores | Capacidad máxima/utilizable, K_required, cuotas/reservas, compromisos, demanda concurrente, colas/contención, consumo B, consumidores, snapshots pre/post/rollback | Capacidad nominal comprometida, insuficiencia, desplazamiento, saturación inducida, medición diferencial o cobertura incompleta (→ ?) |
| Mecanismo | Condición constitutiva; vía colateral a alternativas/Reach/ejecución/Outcome/Value; interferencia entre unidades | Mecanismos no excluyentes; requieren adjudicación empírica |
| Estimandos | ITT D2 de la política material; atribución exclusiva a ΔT_acc*; interferencia | Cambio de capacidad no focal hace ITT efecto de paquete; no ajustar mecánicamente por capacidad post-B; unidad/exposición ante pools compartidos sigue abierta |
| Control | FCM-D2-06/07/08 | Invariancia postulada; cambios colaterales por registrar; ausencia de provisión de fondo/rutas equivalentes no demostrada |

#### 16.8.3. Regla de salida

1. No declarar suficiente capacidad instalada si está comprometida, no disponible en la ventana o no asignada a la unidad/ruta.
2. No inferir independencia porque los componentes tengan nombres o identificadores distintos: comprobar pool, host, runtime, servicio, cola y consumidores transitivos.
3. No sumar CPU, memoria, concurrencia, almacenamiento, red u otras dimensiones inconmensurables; si varias son necesarias, fijar una regla conjuntiva y umbrales ex ante.
4. No crear símbolos/edges nuevos ni rellenar huecos del U_G por analogía; cobertura parcial conserva ?.
5. Si B altera capacidad no focal o el margen de rutas alternativas, el ITT sigue siendo el efecto de la política asignada, pero la atribución exclusiva a accesibilidad exige identificación adicional. Si la capacidad compartida produce interferencia, el estimando y la unidad de asignación/análisis deben revisarse.

**Dictamen:** el crosswalk conceptual D2-CAP-01 está completado y persistido. Siguen abiertos dimensión, K_required, unidad/ventana, reglas de reserva, inventario de pools/consumidores, interferencia, evidencia de invariancia y frontera con App_f*. No se modifica DEC-C10-066/067, no se aprueba ni congela la ficha, y no se autoriza implementación, simulación o ejecución.

**Siguiente operación:** revisar D2-C_INFO (información) y decidir si existe información técnica constitutiva diferenciable de C_dep*, o si manuales/conocimiento/comunicaciones pertenecen a mecanismos posteriores o vías colaterales. Mantener separado el plano epistémico E_T del sistema y no añadir C_info como factor autónomo sin demostrar necesidad y no duplicidad.
### 16.9. Crosswalk causal D2-C_INFO — información, conocimiento y observabilidad (2026-11-06)

**Estado:** clasificación y trazabilidad conceptual completadas; DRAFT, no aprobada ni congelada. No se crea un predicado C_info autónomo ni se añade a A_f*. No se ha demostrado cambio material inducido por B ni comparabilidad de medición.

#### 16.9.1. Reconstrucción histórica y precedencia

- Fuente primaria de clasificación: matriz temporal §13.4 y contratos adversariales I-INFO-01…06. Mapping de provisión: manifiesto §§3/12.3–12.4; matriz de cobertura §9; matriz de cierre §31; maestro §§30.1, 59.3–59.6, 64.5 y 65.
- §30.1 conserva una fórmula histórica del juguete sintético con C_info=1 entre siete condiciones. No debe borrarse ni leerse como especificación depurada actual.
- §59.3 propone para S4-R una ecuación candidata depurada sin C_info autónomo: información técnica solo entra en R_access*/D_support* si es necesaria y no duplica C_dep*. §59.5 separa información técnica del conocimiento del agente. Esta precedencia es propuesta, no freeze; requiere inventario, prueba de necesidad y reconciliación de usos históricos.
- Si un dato técnico imprescindible forma parte del adaptador/configuración focal, su ubicación primaria es C_dep*. Solo podría clasificarse en R_access*/D_support* si es una condición distinta, ex ante, necesaria y no duplicada. No crear un sexto factor ni un predicado C_info independiente.

#### 16.9.2. Cuatro planos que deben permanecer separados

1. **Información técnica del sistema:** dato/metadato/parámetro necesario para invocar/realizar τ2. Puede ser constitutivo, pero debe localizarse en un predicado ya existente y superar necesidad, independencia de conocimiento del agente y no duplicidad.
2. **Conocimiento del agente (K):** mecanismo posterior B→manuales/formación/avisos→K→consideración/selección/inicio→Execution. Puede ser mediador o co-intervención; no redefine accesibilidad estructural.
3. **Información comunicada por B:** mensajes, manuales, formación, asistencia o avisos. Se inspecciona en B-M10 y, cuando implique datos/configuración funcional del sistema, B-M06. No inferir que existió sin inventario.
4. **Observabilidad del evaluador (E_T):** esquema, fuentes, cobertura, permisos, retención, validez y adjudicación. Separa estado verdadero del sistema de A_f_obs/ΔT_acc_obs. Un cambio E_T puede generar error o missingness diferencial sin cambiar el sistema.

#### 16.9.3. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Predicado | C_info histórico §30.1; ecuación depurada §59.3: C_dep*, R_access*, D_support* | No mantener C_info autónomo. Información técnica se asigna una sola vez, si necesaria/no duplicada |
| Mecanismo del agente | K; B→comunicación→consideración/selección/Execution | Vía informativa/mediadora; no equivale a ΔT_acc* |
| Medición | E_T; A_f_obs/ΔT_acc_obs frente a estado real | Cambio epistémico; posible error/missingness diferencial |
| Dominios B-M | B-M10 rector; B-M06 solo si cambia datos/configuración funcional; B-M13 inspección del oráculo | No mezclar comunicación al agente con medición evaluador ni modificar oráculo |
| U_G | B-M10: N16 (oráculo/evaluación funcional), N22 (conocimiento) y N23 (endpoint de resultados); E15, E22 y E23 son relaciones/endpoints relacionados. E_T no tiene nodo/arista U_G explícitos | N22/E22 representa conocimiento; N16/E15 evaluación funcional/oráculo; N23/E23 resultados Outcome/Value, no proceso evaluador. E_T permanece como plano epistémico externo |
| Contratos | PROV-02 (F*/dataset/oráculo inmutables), PROV-03 (snapshots), PROV-04 (dependencias/consumidores), PROV-11 (propagación de unknown); I-INFO-01…06 | Contratos documentales no implementados ni ejecutados; no PASS material |
| Evidencia | Inventario de contenido, destinatarios, exposición, timestamps, permisos, esquema, retención, cobertura, validez, adjudicación y acceso por brazo | Ausencia de inventario → ?; no asumir invariancia o ausencia |
| Estimandos | ITT D2 de política material; mediación por K; error de medición en E_T | Si B comunica/formaliza conocimiento diferencial, ITT es efecto del paquete; mediación exige estrategia/supuestos. No ajustar mecánicamente por K post-B. Si cambia E_T, no confundir cambio observado con cambio estructural |
| Control | FCM-D2-07/10 | Registrar vías colaterales; separar provisión técnica de ejecución y preservar oráculo/medición independiente |

#### 16.9.4. Pruebas adversariales y falsadores

- I-INFO-01: información técnica del sistema presente y agente ignorante → no convertir A_f* en 0 por desconocimiento.
- I-INFO-02: agente informado y dato técnico imprescindible ausente → conocimiento no implica accesibilidad.
- I-INFO-03: manuales/formación B sin cambio del sistema → detectar B→K→selección/ejecución.
- I-INFO-04: mejora de documentación evaluador → cambio E_T, no inferir ΔT_acc*.
- I-INFO-05: dato técnico ya contenido en C_dep* → no doble contabilización.
- I-INFO-06: información imprescindible no verificable → ?.
- Falsadores de aislamiento: mensajes o destinatarios diferenciales, modificación del dataset/oráculo, permisos/cobertura de logs distintos por brazo, timestamps incompletos, cambio de reglas de adjudicación, error/missingness dependiente de B.

#### 16.9.5. Regla de salida y estimandos

- Distinguir verdad del DGP/estado del sistema, conocimiento del agente y proceso de observación. No sustituir uno por otro.
- Si B altera K, el ITT sigue siendo efecto de la política asignada y puede incluir esa vía. No atribuirlo exclusivamente a accesibilidad sin identificación adicional.
- Si B altera E_T, el cambio en A_f_obs/ΔT_acc_obs puede ser artefacto de observación. Exigir medición comparable o modelar explícitamente error/missingness.
- No ajustar automáticamente por K u observabilidad postratamiento; pueden ser mediadores o variables de selección inducidas por B.
- El estado NO INVENTARIADO no equivale a ausencia; cobertura incompleta conserva ?. No crear símbolos/aristas nuevos.

**Dictamen:** crosswalk conceptual D2-C_INFO completado. Quedan abiertos inventario de información técnica imprescindible, mapeo final a C_dep*/R_access*/D_support*, evidencia de invariancia de comunicaciones, validación de E_T, medición comparable y adjudicación de I-INFO-01…06. No se aprueba C_info, no se cierra D2 ni se modifica DEC-C10-066/067; no se autoriza implementación, simulación o ejecución.

**Siguiente operación:** consolidar el crosswalk de las fichas D2-INV-AUTH-01, D2-RES-01, D2-CAP-01 y D2-C_INFO y realizar una auditoría de no duplicidad entre sus condiciones, dominios B-M, U_G, PROV y FCM antes de pasar a estimandos/población/medición. No repetir la construcción de fichas; buscar contradicciones entre ellas y el maestro §§59/64/65.


### 16.10. Auditoría transversal de no duplicidad y coherencia de las cuatro fichas D2 (2026-11-06)

**Estado:** auditoría documental transversal realizada sobre las fichas §13.1–13.4, el maestro C10-S §§46–47, 59.1–59.6 y 64.2–64.3, el manifiesto B-M01…15/PROV-01…12, la matriz U_G §9, la matriz de cierre §31 y DEC-C10-066/067. Resultado: coherencia conceptual parcial con una corrección de mapping aplicada; no es freeze, validación material ni revisión independiente.

#### 16.10.1. Resultado de no duplicidad

| Frontera | Regla reconciliada | Estado y pendiente |
|---|---|---|
| Autorización funcional vs permiso técnico | C_auth,base es autorización normativa funcional basal. ACL, token, credencial y acceso al endpoint son permisos técnicos de provisión B. El canal/interfaz de invocación tampoco equivale a autorización normativa. | Distinción conceptual consistente con B-M04/B-M05, PROV-06 y FCM-D2-06/07. Fuente normativa, titular, alcance, vigencia y evidencia de C_auth siguen abiertos. |
| Recursos vs capacidad | C_resource describe recursos materiales/económicos y su disponibilidad/asignación ex ante. C_capacity describe capacidad de servicio/slots bajo configuración y ventana. No son sinónimos, pero pueden referirse al mismo pool físico y por tanto solaparse. | No se admiten dos factores independientes ni doble contabilización. Maestro §59.3 permite incorporarlos a R_access* solo si son necesarios y distintos de C_dep*. Falta descomposición por dimensión, unidad, pool, compromiso, ventana y regla de derivación de capacidad. |
| Capacidad focal vs no focal | La capacidad/recursos que B añade para instalar/operar el adaptador forman parte de C_dep* o del proceso de provisión según el objeto; no son capacidad basal no focal. | Regla coherente entre D2-RES-01 y D2-CAP-01. Falta evidencia de separación material y no desplazamiento de A1/A2/F2. |
| Información técnica vs dependencia | Un parámetro/configuración imprescindible integrado en el adaptador puede estar ya representado en C_dep*. Solo si es una condición distinta, ex ante y necesaria puede clasificarse en R_access*/D_support*. | C_info autónomo no se incorpora a A_f*. Inventario de información imprescindible y prueba de necesidad/no duplicidad siguen abiertos. |
| Conocimiento del agente vs accesibilidad | K, avisos, formación y consideración son mecanismos posteriores; no se usan para redefinir A_f*. | B-M10/N22/E22. Posible mediación/cointervención; no ajustar automáticamente por K postratamiento. |
| Aplicabilidad/ejecución vs accesibilidad | Precondiciones de S0 y demanda de una ejecución concreta pertenecen a App_f*/ejecución/rendimiento, no a A_f*. | Coherente con §59.3 y §64.2–64.3. Umbrales y medición material siguen pendientes. |
| Evidencia del evaluador E_T vs objeto medido | E_T es el proceso/plano epistémico de observación, cobertura y adjudicación; no es un predicado del sistema ni equivale al oráculo o al resultado observado. | E_T no tiene nodo/arista U_G explícitos. N16/E15 es oráculo/evaluación funcional; N22/E22 es conocimiento; N23/E23 es endpoint de resultados. La ausencia de representación explícita de E_T debe permanecer visible, no rellenarse por analogía. |

#### 16.10.2. Corrección de la inconsistencia U_G / E_T

La versión anterior del crosswalk D2-C_INFO atribuía N23/E23 a observabilidad del evaluador. La definición canónica de U_G los identifica como resultado de ejecución/Outcome/Value (N23) y su relación downstream (E23). Esa atribución era incorrecta.

Se corrigió de forma consistente en:
- Path Predicate Temporal Evidence Matrix §13.4.1.
- Closure Control Matrix, fila B-M10.
- Design Closure and Operationalization Plan §16.9.3.
- Graph Coverage and Trivalent Evidence Matrix §9, fila B-M10 y precaución transversal 3.

La lectura reconciliada es:
- N22/E22: conocimiento del agente y vía a consideración/selección/ejecución.
- N16/E15: oráculo/criterio y evaluación funcional.
- N23/E23: endpoint de resultados de ejecución/Outcome/Value.
- E_T: plano de medición/observabilidad separado, sin nodo/arista U_G específico en el esquema actual.

B-M10 puede afectar a los tres tipos de superficies/endpoint, pero ello no convierte a N16, N22 o N23 en el proceso E_T. PROV-02 protege F*/dataset/oráculo; PROV-03 exige snapshots; PROV-11 propaga desconocidos. Ninguno constituye por sí solo un contrato completo de validez, comparabilidad y adjudicación de E_T. No se inventa un nuevo PROV, FCM, nodo o arista.

FCM-D2-10 se mantiene como separación de provisión técnica y ejecución; aplica a la vía K→selección/ejecución, no como validación del proceso E_T. FCM-D2-07 obliga a registrar cambios colaterales.

#### 16.10.3. Correspondencia cruzada consolidada

| Ficha | Dominio B-M rector | U_G candidato existente | PROV / FCM principal | No duplicidad que debe preservarse |
|---|---|---|---|---|
| D2-INV-AUTH-01 | B-M05; B-M04/B-M09 relacionados | N17/E18; otras superficies solo si el grafo lo demuestra | PROV-06; FCM-D2-06/07 | Autorización funcional basal ≠ ACL/credencial/endpoint técnico |
| D2-RES-01 | B-M07; B-M02/B-M03/B-M12 relacionados; B-M14 si afecta alternativas | N18/N05/N13/N15/N20; E16/E17/E19 | PROV-03/04/05/09; FCM-D2-06/07/08 | Disponibilidad ex ante ≠ consumo; no duplicar capacidad ni C_dep* |
| D2-CAP-01 | B-M07; B-M02/B-M03/B-M12 relacionados; B-M14 si afecta alternativas | N18/N05/N13/N15/N20; E16/E17/E19 | PROV-03/04/05/09; FCM-D2-06/07/08 | Capacidad de servicio/slots ≠ cantidad de recursos; capacidad focal de B ≠ capacidad basal no focal |
| D2-C_INFO | B-M10; B-M06 solo si cambia datos/configuración funcional | N22/E22 (K), N16/E15 (evaluación funcional), N23/E23 (resultados); E_T no mapeado explícitamente | PROV-02/03/11; FCM-D2-07 y FCM-D2-10 solo para separación provisión/ejecución | Información técnica ≠ conocimiento; E_T ≠ oráculo ni Outcome; no crear C_info autónomo |

Los nodos/aristas son roles y relaciones candidatos del grafo; su cobertura material sigue siendo NONE/unknown según el registro. El crosswalk no prueba que existan componentes, dependencias o cambios.

#### 16.10.4. Alcance y límites del dictamen

1. La auditoría solo cubre las cuatro fichas solicitadas; no cierra todos los elementos de A_f*. C_domain/D_support*, identidad/versión, bloqueos, C_other histórico y su retirada requieren reconciliación propia dentro del maestro.
2. La matriz de elegibilidad histórica §46.2 y §47.3 contiene C_resource/C_capacity/C_info/C_domain/C_other. La ecuación candidata §59.3 depura su interpretación hacia C_dep*, C_auth_base, R_access* y D_support*. La precedencia es propuesta; no autoriza borrar la historia ni declarar cerrada la población.
3. Las invariancias de DGP, obligaciones contractuales y no-afectación empírica son estados distintos. Ninguna de las fichas demuestra invariancia material.
4. DEC-C10-066 mantiene D2 como escenario primario candidato y D1 como secundario; DEC-C10-067 acepta el contrato material conceptual D2. Ninguna decisión se amplía por esta auditoría.
5. El ITT sigue siendo efecto de asignación de la política material D2. Si cambian vías colaterales, recursos compartidos, conocimiento o medición, no se atribuye automáticamente el resultado a ΔT_acc*. Unidad/interferencia, Value, población/soporte, estimandos y supuestos siguen abiertos.
6. No se modifica C10-D1, TGCV Core, RMA, Evidence→Claim Matrix, STATUS ni DEC-C10-066/067. No se autoriza freeze, implementación, simulación o ejecución científica.

**Dictamen:** las cuatro fichas son conceptualmente compatibles con la ecuación candidata §59.3 si se mantienen las reglas de no duplicidad anteriores. La representación de E_T en U_G queda expresamente incompleta y corregida como tal. La auditoría no convierte la arquitectura candidata en diseño aprobado ni operacionalizado.

**Siguiente operación:** retomar el Bloque 2 del plan de cierre: reconciliar formalmente la jerarquía de estimandos y la identificación para D2, reutilizando C10-D1 §§5, 17, 25–30, la reconciliación C10-D1/S4-R, P177/P178/P179/P182/P183 y las decisiones DEC-C10-001…067. No crear un nuevo estimando ni empezar por fórmulas sin resolver primero la correspondencia entre políticas materiales B_g, régimen q, política g y estimandos.


### 16.11. Reconciliación histórica de estimandos e identificación para D2 (2026-11-06)

**Estado:** auditoría documental de precedencia y coherencia; reutiliza trabajo existente. No crea estimandos, no aprueba REC-EST-01…09, no cierra identificación ni constituye revisión independiente.

#### 16.11.1. Fuentes recuperadas y regla de precedencia

Se recuperaron desde GitHub en la rama de investigación:
- C10-D1, `C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`, §§5.1–5.3, 17.7–17.9, 24.2, 25.2–25.3 y 26.1–26.3.
- Maestro C10-S, §§43–44, 51, 53–55, 65 y addenda de §§130 y 130 (DEC-C10-067).
- `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`, §§1–18, incluida §12 y addendum de precedencia DEC-C10-066.
- `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`, §§2–5.
- `C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md`.
- `C10_S_DECISION_LOG_DRAFT_001.md`, DEC-C10-066/067 y registros relacionados.
- `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`, REC-CAUS-02/03/07 y SRC-09.

La precedencia aplicable es:
1. C10-D1 gobierna el significado de la pregunta causal general `θ_A(q)` y las condiciones de identificación.
2. C10-S maestro §§43/53 operacionaliza el experimento sintético focal; no redefine C10-D1.
3. DEC-C10-066 fija D2 como escenario primario candidato y D1 como secundario.
4. DEC-C10-067 acepta el contrato material conceptual de las políticas D2.
5. Ninguna de esas dos decisiones acepta la jerarquía completa de estimandos, el mapeo B→g, la población, q*, soporte, exclusión, IV, Value o ejecución.

#### 16.11.2. Objetos causales distintos — no intercambiables

| Objeto | Pregunta que responde | Alcance y condición |
|---|---|---|
| `θ_A(q)` | ¿Cuál es la contribución causal de políticas factibles sobre el cambio estructurado de accesibilidad `ΔT_acc` a Value, bajo un régimen común factible? | Pregunta científica general C10-D1. Requiere g1/g0 implementables, factibilidad por historia, soporte, temporalidad, consistencia/versiones y separación/identificación de vías alternativas. |
| `ITT_Z` / `TE_Z` | ¿Cuál es el efecto de asignar Z a las políticas D2 sobre Value? | Estimando primario de asignación S4-R. La aleatorización puede identificarlo bajo consistencia, interferencia tratada y observación/manejo válido de Value y pérdidas. Incluye incumplimiento/crossover según asignación; no es efecto de recibir B ni de accesibilidad. |
| `ψ_B(q_X^*)` | ¿Cuál es el contraste entre las versiones implementables B1/B0 en la población basal objetivo común? | El maestro §44 lo formula como contraste de políticas recibidas/versiones bajo `q_X^*`. No se identifica automáticamente por `ITT_Z`; requiere correspondencia entre asignación y versión recibida, consistencia y estrategia propia. |
| `ψ_policy` | ¿Cuál es el efecto de la política/paquete incluyendo las vías que activa? | Etiqueta usada en el maestro §53 y en la reconciliación para el efecto de paquete. No debe intercambiarse sin aclaración con `ψ_B(q_X^*)`: el maestro §42/§44 usa `ψ_B`, mientras §53 usa `ψ_policy`. La relación/notación entre ambos sigue pendiente de armonización. |
| `LATE_f` | ¿Cuál es el efecto local de apertura focal entre compliers inducidos por Z? | Wald basado en `ITT_Z/ITT_{D_f}`, solo bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición válida. Es local a D2 y a sus compliers; no es ATE, `θ_A(q)` ni `θ_Af(q_X^*)`. Si se estima para O y V, cada resultado requiere su propio contraste. |
| `θ_Af(q_X^*)` / `θ_Af(q*)` | ¿Cuál es el contraste poblacional de políticas que inducen apertura focal de `τ2` bajo un referente común? | Estimando focal candidato. Requiere demostrar que las políticas B_g^D2 implementan las políticas g^Af pertinentes, que el régimen es común/factible y que no quedan vías diferenciales hacia Value fuera de accesibilidad focal. No equivale automáticamente a ITT ni a LATE. |
| `θ_{L,A}` | ¿Cuál es el efecto conjunto de cambiar coordinadamente condiciones y accesibilidad? | Alternativa de interpretación si ambas dimensiones cambian y no pueden separarse. No atribuye el efecto exclusivamente a accesibilidad. |

No se define un residual `TE_Z-θ_A(q)` como efecto directo puro. La descomposición requiere secuencia de intervenciones y contrastes compatibles, misma población/escala/horizonte y tratamiento explícito de interacciones.

#### 16.11.3. D2 y el mapeo de política a accesibilidad

DEC-C10-066/067 permiten fijar la lectura material siguiente:
- `B_g0^D2`: mantener configuración basal; no programar ni iniciar provisión focal ni desplegar/configurar el adaptador focal.
- `B_g1^D2`: programar provisión técnica focal con artefacto/versionado y eventos que deberán identificarse y registrarse.
- `C_auth,base=1`, elegibilidad, recursos no focales, capacidad, información basal y medición/adjudicación se mantienen comunes en el DGP aislado.
- La política asignada no garantiza recepción, intento efectivo, éxito de instalación, `C_dep*`, `A_f*`, `D_f*`, `ΔT_acc`, selección ni ejecución. Provisión de fondo/crossover debe observarse en ambos brazos.

La secuencia a preservar es:
`Z → B_assigned/offered → B_received/W_programmed → W_attempt → C_dep → A_f* → D_f*/ΔT_acc → Reach/Π_H → K/consideración/selección → Exec → O → V`.

La flecha `B_g^D2 → g^Af` **no está aceptada ni demostrada**. Es una condición de interpretación de `θ_Af(q_X^*)`, no una equivalencia otorgada por DEC-C10-067. Si B cambia recursos, permisos, información, coste, latencia, seguridad, calidad, incentivos, alternativas u otras vías hacia Value, el ITT sigue siendo efecto de asignación al paquete; la atribución focal/IV no se mantiene sin identificación adicional.

#### 16.11.4. Régimen común: q, q_X* y q_L* no son sinónimos

- `q` en C10-D1 es un régimen común, explícito y factible de condiciones/historias no constitutivas bajo las políticas de accesibilidad.
- `q_X^*` en C10-S §44 es la distribución objetivo común de características e historia **basales** (X, H₀, C_c) de la población elegible. No es una intervención que fuerce covariables y no representa automáticamente todo el régimen `q` de C10-D1.
- `q_L^*` es una política secuencial sobre variables postasignación L_m cuando sean indispensables. Una distribución marginal o ajuste estadístico por L_m no la sustituye.
- La regla de Value es parte de la definición del resultado/estimando y debe permanecer fija; no es una variable que se manipule dentro de q.

El uso de `q_X^*` en S4-R es candidato y depende de definir P*, elegibilidad pre-Z, soporte/factibilidad por estrato, unidad/interferencia y regla Value. No convertir q_X* en evidencia de que se ha identificado el q general.

#### 16.11.5. Primera etapa e identificación IV

Calcular y reportar por separado las primeras etapas sobre `C_dep`, `A_f,post^*`, `D_f` y `ΔT_acc`. La primera etapa técnica no sustituye la primera etapa de accesibilidad focal; ninguna demuestra por sí misma exclusión.

`LATE_f` solo se interpreta mediante Wald cuando:
- existe relevancia y la inferencia es robusta a instrumento débil;
- Z es independiente de los potenciales pertinentes en la unidad de asignación;
- se sostiene exclusión de vías Z/B hacia el resultado fuera de D_f;
- se sostiene monotonicidad en el tratamiento focal definido;
- hay consistencia y versiones coherentes;
- no hay interferencia relevante no modelada;
- D_f y Value están medidos con validez y error diferencial controlado.

Una vía colateral B→Value o una modificación de alternativas puede conservar el ITT de asignación y, a la vez, invalidar la interpretación LATE focal. D1 y D2 tienen primeras etapas y poblaciones de compliers distintas; no agrupar ni transportar sus Wald/LATE.

#### 16.11.6. Estado real de decisiones y pendientes

- DEC-C10-066: ACCEPTED, alcance limitado a D2 primario candidato / D1 secundario.
- DEC-C10-067: ACCEPTED, alcance limitado a definiciones materiales conceptuales de B_g0^D2/B_g1^D2.
- REC-EST-01…09: permanecen como propuestas/abiertas en la reconciliación; no se promueven a decisiones aceptadas.
- La reconciliación previa ya contiene la jerarquía; este trabajo no la recrea. Se actualiza su lectura tras DEC-C10-066/067 y se registran las diferencias de notación pendientes.
- Población P*_τ2/P*_F, q_X*, q_L*, soporte, F*, Value, actor/artefacto/recepción, cumplimiento, ausencia de provisión de fondo, primeras etapas, exclusión, monotonicidad, interferencia, medición y pérdidas siguen abiertos.
- Las secciones 177–183 recuperadas son propuestas metodológicas; P177/178 parámetros y precisión pendientes; P179 regla dimensional de Value pendiente; P181–183 pruebas de medición, error y missingness no ejecutadas.
- No se declara XSYNC cerrado, no se acepta el DGP ni se aprueba freeze, implementación, simulación o ejecución.

**Dictamen:** la jerarquía existente es conceptualmente compatible con D2 si se conserva la separación de los objetos y las condiciones anteriores. La principal discrepancia documental nueva es la notación `ψ_B(q_X^*)` (§44) frente a `ψ_policy` (§53); no se resuelve por sustitución automática. La correspondencia B_g^D2→g^Af y la identificación de `θ_Af(q_X^*)` permanecen pendientes.

**Siguiente operación:** auditar específicamente la correspondencia de intervención `B_g^D2 → C_dep → A_f^* → D_f/ΔT_acc` frente a las políticas g de C10-D1, y resolver la relación/notación `ψ_B(q_X^*)` / `ψ_policy` antes de seleccionar una estrategia de identificación. Reutilizar §§26–33, 42–44, 53–55, DEC-C10-066/067 y XSYNC-138; no crear símbolos nuevos.



### 16.12. Correspondencia D2 (B_g\rightarrow g^{Af}) y armonización (ψ_B/ψ_{policy}) (2026-11-06)

**Estado:** auditoría documental completada y persistida en el maestro §131; no aceptación de estimandos ni identificación.

1. **Regla causal:** (g^{Af}) son políticas objetivo sobre distribuciones factibles de cambios focales de accesibilidad; (B_g^{D2}) son mecanismos materiales de provisión. No son idénticos. La correspondencia solo existe si la distribución de (ΔA_f) inducida por cada versión B se reconstruye por historia, con población/soporte, consistencia, medición y vías alternativas resueltas.
2. **Cadena:** (Z→B_{assigned}^{D2}→W_{programmed}→W_{attempt}→C_{dep}^*→A_f^*→D_f^*→ΔT_{acc}^*→Reach/Π_H→Exec→Outcome→Value). (C_{dep}^*) no es suficiente para (A_f^*); (D_f^*) es proyección focal, no (ΔT_{acc}^*).
3. **D2 frente a §33.4:** el contraste ilustrativo 0,20→0,80 no corresponde a D2. Bajo s=.80 candidato, cumplimiento perfecto, una oportunidad, ausencia de provisión de fondo, ruta única y predicados restantes satisfechos/invariantes, D2 implicaría 0→0,80 para (D_f^*). Son condiciones algebraicas no validadas; no se traslada el valor 3,6 ni se calcula otro efecto Value.
4. **Notación:** (ψ_B(q_X^*)) es una instancia específica de (ψ_{policy}(q)) cuando coinciden versiones B, población, resultado, regla Value, horizonte y régimen completo. No es igual a (ITT_Z), que es efecto de asignación, ni a (θ_{Af}), que exige atribución focal adicional. (q_X^*) no reemplaza (q_L^*) si se necesita un régimen secuencial postratamiento.
5. **Estado:** DEC-C10-066/067 conservan alcance. Correspondencia (B_g^{D2}↔g^{Af}): CONDICIONAL/NO DEMOSTRADA. (θ_{Af}(q_X^*)): no identificado. (θ_A(q)): pregunta general C10-D1, no resuelta por D2.

Se actualizan REC-CAUS-02/03/04/07 en la matriz de cierre. No se aprueban REC-EST-01…09 ni se cierran XSYNC-138. No hay freeze, implementación, simulación o ejecución.

**Siguiente operación:** auditar (LATE_f) y la validez de (D_f^*) como tratamiento endógeno IV en D2; no seleccionar Wald hasta revisar exclusión, monotonicidad, versiones, interferencia y error de medición.


### 16.13. Auditoría IV de D2: validez de LATE_f y D_f* (2026-11-06)

**Registro:** `C10_S_D2_LATE_F_IV_VALIDITY_AUDIT_DRAFT_001.md`.  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT. Auditoría documental; no es validación empírica ni autorización.

**Dictamen:** `LATE_f` permanece **NO IDENTIFICADO / NO LISTO PARA WALD**. La aleatorización candidata puede identificar el ITT de la política D2 si se cierra y respeta la asignación, pero no prueba exclusión, monotonicidad, consistencia, ausencia de interferencia ni validez de medición.

Hallazgos:
- **Relevancia:** no demostrada para `D_f^*`. Programación, intento y éxito técnico son estados distintos; `s=0.80` es candidato no validado. Separar primeras etapas de `C_dep^*`, `A_f,post^*`, `D_f^*` y `ΔT_acc^*`.
- **Independencia:** condicional a unidad, elegibilidad pre-Z, aleatorización/bloques y nivel de clúster, aún abiertos.
- **Exclusión:** no demostrada. Las vías B-M01…15 pueden alterar recursos, rendimiento, coste, seguridad, información, alternativas, estado, rollback y medición. Las vías posteriores a `D_f^*` forman parte de su efecto; las vías B→Outcome/Value que no pasan por `D_f^*` invalidan la atribución focal.
- **Monotonicidad:** abierta; crowding-out, desplazamiento de recursos o degradación de alternativas podrían producir defiers. El crossover de control puede producir always-takers y debe medirse.
- **Consistencia/versiones:** faltan identidad/hash y trazabilidad operativa completa.
- **Interferencia:** no resuelta por dependencias y recursos compartidos.
- **Medición:** distinguir `D_f^*` de `D_f^{obs}`; adjudicar `A_f^*` con predicados y snapshots independientes; fijar medición de Value, error diferencial y missingness.

No calcular Wald como efecto causal nominal. Mantener `ITT_Z` como efecto de asignación/política y `LATE_f` como objeto secundario condicional. Si no se sostiene exclusión, informar efecto de paquete o no identificación focal. Un eventual LATE sería local a compliers D2, no `θ_Af(q_X^*)` poblacional ni `θ_A(q)` general.

**Gates IV-G1…IV-G8:** definición y medición del tratamiento/población; primera etapa e inferencia débil; independencia/interferencia; exclusión; monotonicidad; consistencia/versiones; resultado Outcome/Value y missingness; recuperación sintética bajo escenarios adversariales. Su cierre no autoriza ejecución.

No se modifican DEC-C10-066/067 ni el estado de autorización. No hay freeze, implementación, simulación, estimación o ejecución. La siguiente operación es auditar la definición observacional de `D_f^*` y el protocolo de medición de `A_f^*`.


### 16.14. Auditoría de medición focal D_f* / A_f* (2026-11-06)

**Registro:** `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md`.  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.

**Dictamen:** concepto parcialmente estabilizado; medición observacional no cerrada. Se separan `S_T^*`, `E_T`, `A_f^*), `A_f^{obs}`, `D_f^*) y `D_f^{obs}`; `ΔT_acc^*) no se confunde con `ΔE_T).

Hallazgos:
1. La conjunción de DGP §3.3 no está reconciliada con las fichas: `C_info` aparece en la fórmula aunque el crosswalk mantiene su inclusión autónoma pendiente; recursos/capacidad también requieren desduplicación.
2. Matching de τ2, frontera, unidad/contexto, granularidad, catálogo y mapping son requisitos de comparabilidad; unresolved implica `D_f^{obs}=?`.
3. DEC-C10-065 acepta pinning exacto, pero UG-SCH-10 permanece abierto; no hay validación técnica de pertenencia/FKs/constraints.
4. La cobertura de rutas alternativas/compartidas/externas/desconocidas es NONE en la plantilla; ausencia de evidencia no equivale a inaccesibilidad.
5. Cegamiento, doble adjudicación y evaluación con truth oculta son propuestas, no procedimientos ejecutados.
6. Error diferencial y missingness por brazo/tiempo/versión/ruta no están cuantificados.
7. La secuencia temporal t0–t9 está propuesta; ventanas, simultaneidad y vigencia siguen abiertas.

No sustituir `D_f^*) por `D_f^{obs}` en primera etapa/Wald sin modelo de error defendible. `LATE_f` sigue bloqueado. No se altera DEC-C10-065, ni se cierra UG-SCH-10/XSYNC/gates IV.

**Siguiente operación:** crosswalk exhaustivo de predicados de `A_f^*` (constitutivo/invariante/vía colateral/epistémico/duplicado), sin alterar fórmula; luego regla trivalente de agregación.
