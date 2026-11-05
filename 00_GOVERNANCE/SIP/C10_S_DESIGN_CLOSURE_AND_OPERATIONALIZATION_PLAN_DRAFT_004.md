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
