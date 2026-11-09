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
3. Las DEC-C10 aceptadas prevalecen sobre propuestas/recomendaciones anteriores dentro de su alcance exacto; el maestro C10-S integra la especificación vigente y debe reflejar esas decisiones. Las secciones históricas supersedidas no son fuente operativa.
4. Los contratos especializados, Decision Log, matrices y auditorías complementan al maestro. Si discrepan, la divergencia se registra y se corrige contra el maestro y las decisiones aceptadas; no se elige por intuición.
5. Este plan es derivado y no crea decisiones científicas.
6. Una propuesta, recomendación, fixture ilustrativo o ecuación candidata no se convierte en decisión aceptada por estar persistida.
7. Toda nueva decisión debe actualizar en el mismo ciclo el maestro, Decision Log y artefactos afectados; verificar cada escritura mediante fetch y SHA.
8. No modificar main ni cambiar la base de PR #116 sin instrucción expresa.
9. scientific_execution=false y execution_authorized=false hasta autorización expresa y gates previos.
10. La generación/modificación de código ejecutable C10-S se rige por maestro §0.6 y Closure Control Matrix §100: bloqueada hasta contrato de implementación aceptado y autorización explícita; todo código futuro debe tener trazabilidad semántica a fuentes versionadas.

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

### 4.3 Condiciones de acceso y fórmula candidata — precedencia del crosswalk D2

La composición de referencia para la accesibilidad focal es la fórmula candidata depurada del maestro §67.3 y del crosswalk D2; la ecuación intermedia de §59.3 queda supersedida: 

`A_f^*=I(ID_f^* ∧ REL_f^* ∧ COND_f^* ∧ AUTH_f^* ∧ RES_f^* ∧ DEP_f^* ∧ ¬BLOCK_f^*)`.

La fórmula anterior de esta sección, que expresaba la conjunción mediante `C_dep^*`, `C_auth_base`, `R_access^*` y `D_support^*`, queda supersedida como representación operativa por el crosswalk. Se conserva la correspondencia funcional, no una duplicación de factores:

- `C_auth,base=1` es la condición basal común e invariante D2 por DEC-C10-067; `C_auth_base` se corresponde con `AUTH_f^*`, no es un factor independiente.
- `C_dep^*` y sus cuatro componentes técnicos se representan dentro de `DEP_f^*` para la ruta focal; no sustituyen el resto de predicados.
- Disponibilidad ex ante necesaria de recursos/capacidad puede contribuir a `RES_f^*` solo si se distingue del consumo de ejecución y no duplica dependencias.
- `D_support^*` debe mapearse a identidad/tipo o `COND_f^*` según su función material; el mapping final sigue abierto.
- `C_info` no es un factor autónomo; `C_other` queda excluido como comodín.
- Validez/cobertura de evidencia y `E_T` son epistémicos, no términos de truth estructural. `App_f^*` se evalúa separadamente desde S0.

La fórmula es candidata, no universal ni congelada. Siguen abiertas la operacionalización material de `RES_f^*`, el mapping `D_support^*`, los catálogos REL/COND/BLOCK, el inventario de rutas y su evidencia. `C_dep^*`, `A_f^*`, `D_f^*` y `ΔT_acc^*` deben medirse y analizarse por separado.

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

La inspección confirma que §§46–47 del maestro contienen una formulación histórica/preliminar de elegibilidad con `C_auth,base`, `C_resource`, `C_capacity`, `C_info`, `C_domain`, `C_other,j`, `C_dep,0` y `A_f,0*`. Se conserva como antecedente para reconstruir condiciones y pruebas ELIG-01…12, no como fórmula operativa vigente de `A_f*` ni como contrato cerrado de elegibilidad. La precedencia de la composición focal corresponde al maestro §67.3 y al crosswalk D2: `C_auth,base`→`AUTH_f*`; recursos/capacidad→`RES_f*` solo si son disponibilidad ex ante necesaria/no duplicada; `C_info` no es factor autónomo; `C_other` no es admisible como comodín. La elegibilidad poblacional sigue requiriendo un contrato propio.

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

1. Arquitectura: reconciliar condiciones, relaciones, bloqueos y solapamientos entre `RES_f*`, `ID_f*`, `COND_f*`, `DEP_f*` y predicados; conservar `R_access*`/`D_support*` solo como nombres históricos de mappings intermedios.
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
- Maestro §59.2 conserva la distinción conceptual entre stock/disponibilidad ex ante y demanda/consumo de ejecución. La asignación histórica de esa disponibilidad a `R_access*` en §59.3 queda supersedida; conforme a §67.3/crosswalk D2, solo la disponibilidad ex ante necesaria y no duplicada puede contribuir a `RES_f*`. El consumo durante ejecución permanece downstream.
- El maestro §46.2 incluye `C_resource=1` y `C_capacity=1` en una regla histórica/ilustrativa de elegibilidad. No se interpreta como autorización para añadir factores autónomos a `A_f*`. Conforme a §67.3, cada dimensión debe asignarse una sola vez a `RES_f*` (disponibilidad ex ante necesaria/no duplicada), `DEP_f*` (capacidad/dependencia técnica focal), o aplicabilidad/ejecución.
- C_capacity mantiene ficha separada §13.3; su capacidad focal introducida por B pertenece a C_dep*, mientras que capacidad no focal compartida debe evaluarse como condición común y posible vía de interferencia.

#### 16.7.2. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Definición → DGP | Disponibilidad suficiente basal, unidad×recurso×ventana, antes de Z; maestro §§46–47, 59.2–59.4 y 64.5 | Invariancia postulada/contractual en DGP aislado; no demostrada |
| Predicado | `RES_f*(i,t;τ2)`; `C_resource` como descriptor de disponibilidad ex ante; consumo de ejecución separado | No crear multiplicadores redundantes. Stock/disponibilidad ≠ demanda/consumo |
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

**Dictamen:** el crosswalk conceptual de D2-RES-01 está completado y persistido. Permanecen abiertos la operacionalización de suficiencia, la conciliación material de §46.2 con la fórmula candidata §67.3, inventario y consumidores, PROV-05/09, MD-C1/MD-C4, interferencia/unidad y la atribución específica a accesibilidad. La asignación antigua a `R_access*` de §59.3 es histórica/supersedida; la referencia actual es `RES_f*`. No se modifica DEC-C10-066/067, no se aprueba D2-RES-01 y no se autoriza implementación ni ejecución.

**Siguiente ficha:** D2-CAP-01. El trabajo deberá resolver primero el límite entre capacidad necesaria para ofrecer τ2 (posible contribución a `RES_f*`), capacidad focal ya contenida en `DEP_f*` a través de `C_dep*`, y capacidad/margen dependiente de carga o estado (aplicabilidad/ejecución), sin duplicar `RES_f*` ni `C_resource`.

### 16.8. Crosswalk causal ficha D2-CAP-01 — capacidad no focal (2026-11-06)

**Estado:** trazabilidad documental individual realizada; ficha DRAFT, no aprobada ni congelada. La capacidad no ha sido operacionalizada ni medida en una implementación real.

#### 16.8.1. Reconstrucción y precedencia semántica

- Ficha temporal §13.3; fuentes: Path Predicate Temporal Evidence Matrix §8, manifiesto §5/§12, maestro §§46–47 y 59.2–59.4/64.5, matriz de cierre §§20/26/29/31 y matriz de cobertura §9.
- Maestro §59.2 diferencia capacidad instalada/slots disponibles para ofrecer τ2 (posible condición de acceso) de margen operativo requerido por S0 o carga concurrente concreta (aplicabilidad).
- §67.3 y el crosswalk D2 son la precedencia semántica candidata: capacidad no focal solo puede contribuir a `RES_f*` si es disponibilidad ex ante necesaria y no duplica `DEP_f*`; capacidad focal introducida por B forma parte de `DEP_f*`. Información técnica no crea un predicado autónomo y se asigna al término estructural correspondiente según su función. La plantilla `C_capacity,i,w` de §13.3 no añade por sí sola un factor nuevo a `A_f*`. La asignación antigua a `R_access*/D_support*` de §59.3 es histórica/supersedida.
- Capacidad focal introducida por B pertenece a `DEP_f*` (a través de `C_dep*`). Capacidad no focal común puede contribuir a `RES_f*` solo si se demuestra que es necesaria para poner τ2 a disposición, existe antes de Z, está asignada a unidad/ventana y no está ya contenida en `DEP_f*`.
- La demanda, saturación, cola, consumo o margen de una ejecución concreta no se confunden con la disponibilidad estructural. Se clasifican en App_f*, ejecución/rendimiento o resultado según el mecanismo.

#### 16.8.2. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Definición → DGP | Capacidad instalada, disponible, reservada, consumida y margen; S4-R postula capacidad no focal común/suficiente | Supuesto de diseño, no invariancia demostrada |
| Predicado | Plantilla existente `C_capacity,i,w = I(K_available ≥ K_required)`; posible disponibilidad en `RES_f*` solo si es no focal, ex ante y necesaria | No convertir en factor autónomo ni en CAP-τ2. Requiere dimensión, unidad, configuración, ventana, demanda y umbral preespecificados |
| Frontera A_f*/App_f* | Capacidad/slots para ofrecer τ2 vs precondiciones de S0/carga/ejecución | La primera puede contribuir a `RES_f*` si es no focal, necesaria y no duplicada; la segunda pertenece a `App_f*`/ejecución |
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
- La ecuación intermedia de §59.3 que asignaba información a `R_access*/D_support*` queda supersedida como representación operativa por §67.3/crosswalk D2. §59.5 conserva una distinción útil entre información técnica y conocimiento del agente, pero la información no constituye un factor autónomo `C_info`; debe asignarse al término de §67.3 que corresponda a su función material, con prueba de necesidad y no duplicidad.
- Si un dato técnico imprescindible forma parte del adaptador/configuración focal, su ubicación primaria es `DEP_f*` (a través de `C_dep*`). Solo puede contribuir a `RES_f*`, `COND_f*` o `ID_f*` si es una condición distinta, ex ante y necesaria, con mapping explícito y sin duplicidad. No crear un factor adicional ni un predicado `C_info` independiente.

#### 16.9.2. Cuatro planos que deben permanecer separados

1. **Información técnica del sistema:** dato/metadato/parámetro necesario para invocar/realizar τ2. Puede ser constitutivo, pero debe localizarse en un predicado ya existente y superar necesidad, independencia de conocimiento del agente y no duplicidad.
2. **Conocimiento del agente (K):** mecanismo posterior B→manuales/formación/avisos→K→consideración/selección/inicio→Execution. Puede ser mediador o co-intervención; no redefine accesibilidad estructural.
3. **Información comunicada por B:** mensajes, manuales, formación, asistencia o avisos. Se inspecciona en B-M10 y, cuando implique datos/configuración funcional del sistema, B-M06. No inferir que existió sin inventario.
4. **Observabilidad del evaluador (E_T):** esquema, fuentes, cobertura, permisos, retención, validez y adjudicación. Separa estado verdadero del sistema de A_f_obs/ΔT_acc_obs. Un cambio E_T puede generar error o missingness diferencial sin cambiar el sistema.

#### 16.9.3. Crosswalk de extremo a extremo

| Eslabón | Correspondencia | Lectura y estado |
|---|---|---|
| Predicado | `C_info` histórico §30.1; fórmula candidata §67.3: `DEP_f*`, `RES_f*`, `COND_f*` o `ID_f*` según función material | No mantener `C_info` autónomo. Información técnica se asigna una sola vez, si necesaria/no duplicada |
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

**Dictamen:** crosswalk conceptual D2-C_INFO completado. Quedan abiertos inventario de información técnica imprescindible, mapping final a `DEP_f*`/`RES_f*`/`COND_f*`/`ID_f*`, evidencia de invariancia de comunicaciones, validación de `E_T`, medición comparable y adjudicación de I-INFO-01…06. No se aprueba C_info, no se cierra D2 ni se modifica DEC-C10-066/067; no se autoriza implementación, simulación o ejecución.

**Siguiente operación:** consolidar el crosswalk de las fichas D2-INV-AUTH-01, D2-RES-01, D2-CAP-01 y D2-C_INFO y realizar una auditoría de no duplicidad entre sus condiciones, dominios B-M, U_G, PROV y FCM antes de pasar a estimandos/población/medición. No repetir la construcción de fichas; buscar contradicciones entre ellas y el maestro §67.3/crosswalk D2 y los contratos vigentes.


### 16.10. Auditoría transversal de no duplicidad y coherencia de las cuatro fichas D2 (2026-11-06)

**Estado:** auditoría documental transversal realizada sobre las fichas §13.1–13.4, el maestro C10-S §§46–47, 59.1–59.6 y 64.2–64.3, el manifiesto B-M01…15/PROV-01…12, la matriz U_G §9, la matriz de cierre §31 y DEC-C10-066/067. Resultado: coherencia conceptual parcial con una corrección de mapping aplicada; no es freeze, validación material ni revisión independiente.

#### 16.10.1. Resultado de no duplicidad

| Frontera | Regla reconciliada | Estado y pendiente |
|---|---|---|
| Autorización funcional vs permiso técnico | C_auth,base es autorización normativa funcional basal. ACL, token, credencial y acceso al endpoint son permisos técnicos de provisión B. El canal/interfaz de invocación tampoco equivale a autorización normativa. | Distinción conceptual consistente con B-M04/B-M05, PROV-06 y FCM-D2-06/07. Fuente normativa, titular, alcance, vigencia y evidencia de C_auth siguen abiertos. |
| Recursos vs capacidad | `C_resource` describe recursos materiales/económicos y su disponibilidad/asignación ex ante. `C_capacity` describe capacidad de servicio/slots bajo configuración y ventana. No son sinónimos, pero pueden referirse al mismo pool físico y por tanto solaparse. | No se admiten dos factores independientes ni doble contabilización. La referencia actual es §67.3: disponibilidad ex ante necesaria/no duplicada puede contribuir a `RES_f*`; capacidad técnica focal queda en `DEP_f*`. Falta descomposición por dimensión, unidad, pool, compromiso, ventana y regla de derivación de capacidad. |
| Capacidad focal vs no focal | La capacidad/recursos que B añade para instalar/operar el adaptador forman parte de C_dep* o del proceso de provisión según el objeto; no son capacidad basal no focal. | Regla coherente entre D2-RES-01 y D2-CAP-01. Falta evidencia de separación material y no desplazamiento de A1/A2/F2. |
| Información técnica vs dependencia | Un parámetro/configuración imprescindible integrado en el adaptador puede estar ya representado en `DEP_f*` a través de `C_dep*`. Solo si es una condición distinta, ex ante y necesaria puede asignarse a `RES_f*`, `COND_f*` o `ID_f*` según función material. | `C_info` autónomo no se incorpora a `A_f*`. Inventario de información imprescindible y prueba de necesidad/no duplicidad siguen abiertos. |
| Conocimiento del agente vs accesibilidad | K, avisos, formación y consideración son mecanismos posteriores; no se usan para redefinir A_f*. | B-M10/N22/E22. Posible mediación/cointervención; no ajustar automáticamente por K postratamiento. |
| Aplicabilidad/ejecución vs accesibilidad | Precondiciones de S0 y demanda de una ejecución concreta pertenecen a `App_f*`/ejecución/rendimiento, no a `A_f*`. | Coherente con §67.3 y §64.2–64.3. Umbrales y medición material siguen pendientes. |
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

1. La auditoría solo cubre las cuatro fichas solicitadas; no cierra todos los elementos de A_f*. `C_domain/D_support*`, identidad/versión, bloqueos y mappings a `ID_f*`/`COND_f*` requieren reconciliación material propia; `C_other` histórico queda excluido como comodín por §67.3.
2. La matriz de elegibilidad histórica §46.2 y §47.3 contiene `C_resource/C_capacity/C_info/C_domain/C_other`. La fórmula intermedia §59.3 está supersedida; la composición candidata actual es la de §67.3: `ID_f*`, `REL_f*`, `COND_f*`, `AUTH_f*`, `RES_f*`, `DEP_f*`, `¬BLOCK_f*`. La precedencia de la fórmula no autoriza borrar la historia ni declarar cerrada la población.
3. Las invariancias de DGP, obligaciones contractuales y no-afectación empírica son estados distintos. Ninguna de las fichas demuestra invariancia material.
4. DEC-C10-066 mantiene D2 como escenario primario candidato y D1 como secundario; DEC-C10-067 acepta el contrato material conceptual D2. Ninguna decisión se amplía por esta auditoría.
5. El ITT sigue siendo efecto de asignación de la política material D2. Si cambian vías colaterales, recursos compartidos, conocimiento o medición, no se atribuye automáticamente el resultado a ΔT_acc*. Unidad/interferencia, Value, población/soporte, estimandos y supuestos siguen abiertos.
6. No se modifica C10-D1, TGCV Core, RMA, Evidence→Claim Matrix, STATUS ni DEC-C10-066/067. No se autoriza freeze, implementación, simulación o ejecución científica.

**Dictamen:** las cuatro fichas son conceptualmente compatibles con la fórmula candidata de §67.3 si se mantienen las reglas de no duplicidad anteriores. La representación de `E_T` en U_G queda expresamente incompleta y corregida como tal. La auditoría no convierte la arquitectura candidata en diseño aprobado ni operacionalizado.

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
1. **Hallazgo histórico ya reconciliado conceptualmente:** la conjunción antigua de DGP §3.3 incluía `C_info` y condiciones de recursos/capacidad sin desduplicación suficiente. No es la composición operativa vigente; prevalece §67.3/crosswalk D2. El inventario y mapping material de cada condición siguen abiertos, pero `C_info` no es factor autónomo y los recursos/capacidad solo contribuyen a `RES_f*` si son necesarios ex ante y no duplicados.
2. Matching de τ2, frontera, unidad/contexto, granularidad, catálogo y mapping son requisitos de comparabilidad; unresolved implica `D_f^{obs}=?`.
3. DEC-C10-065 acepta pinning exacto, pero UG-SCH-10 permanece abierto; no hay validación técnica de pertenencia/FKs/constraints.
4. La cobertura de rutas alternativas/compartidas/externas/desconocidas es NONE en la plantilla; ausencia de evidencia no equivale a inaccesibilidad.
5. Cegamiento, doble adjudicación y evaluación con truth oculta son propuestas, no procedimientos ejecutados.
6. Error diferencial y missingness por brazo/tiempo/versión/ruta no están cuantificados.
7. La secuencia temporal t0–t9 está propuesta; ventanas, simultaneidad y vigencia siguen abiertas.

No sustituir `D_f^*) por `D_f^{obs}` en primera etapa/Wald sin modelo de error defendible. `LATE_f` sigue bloqueado. No se altera DEC-C10-065, ni se cierra UG-SCH-10/XSYNC/gates IV.

**Siguiente operación:** crosswalk exhaustivo de predicados de `A_f^*` (constitutivo/invariante/vía colateral/epistémico/duplicado), sin alterar fórmula; luego regla trivalente de agregación.


### 16.15. Crosswalk causal de predicados A_f*

**Registro:** `C10_S_D2_AF_PREDICATE_CAUSAL_CROSSWALK_DRAFT_001.md`.

La auditoría de medición §16.14 queda corregida: la fórmula candidata depurada de referencia está en maestro §67.3/crosswalk D2; la ecuación intermedia de §59.3 está supersedida. MEAS-G1 pasa a **PARTIAL**, no OPEN por ausencia de fórmula. `C_auth_base`→`AUTH_f*`; `C_resource/C_capacity` solo disponibilidad ex ante necesaria/no duplicada→`RES_f*`; `C_info` no es factor autónomo; `C_domain/D_support`→`ID_f*`/`COND_f*`; `C_dep`→`DEP_f*`; `C_other` inadmisible; VALID/cobertura/`E_T` epistémicos; `App_f*`/K/selección/ejecución downstream. El crosswalk especializado conserva mappings y operacionalización material como abiertos.

No se cambia DEC ni se congela la fórmula. Próximo: consolidar regla trivalente de conjunción y rutas.


---

### 16.16. Regla trivalente A_f / DEP / D_f observados

**Fuente:** `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md §10`.  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.

- A_f observado: 0 si algún término necesario tiene 0 válido y suficiente; 1 solo si todos los términos son 1 con comparabilidad/cobertura; resto ?.
- DEP observado: disyunción de rutas; una ruta 1 basta; 0 exige universo operativo COMPLETE y todas las rutas 0, con Runknown/alternativas resueltas; resto ?.
- D_f observado: baseline 0/post 1 → 1; baseline 1 o post 0 → 0; resto ?. No comparabilidad → NOT_COMPARABLE/?.
- Evidencia, cobertura, adjudicación, observed_state y truth DGP permanecen separados. MISSING/NONE/PARTIAL no son 0.
- C_dep=0 no implica DEP=0 cuando existe alternativa admisible. D_f observado no reemplaza al verdadero en IV sin modelo de error defendible.

No se aprueba ni congela la fórmula, no se cierran MEAS-G2…G8 ni IV, y no se autoriza implementación/ejecución.


### 16.17. Reconciliación de casos adversariales y cobertura lógica trivalente


**Fuentes:** auditoría de medición focal §11 (`C10-S-TRI-ADVERSARIAL-CROSSWALK-001`) y registro de pruebas §57. Los subcasos TRI son extensiones de MEAS-01…24; se reutilizan ID/SNAP sin duplicarlos.

Se evita duplicar catálogos existentes. Se reutilizan ID-01…15, SNAP-01…15, DGP §§26–28/32–35, U_G §§4–8 y matriz de fixtures §30. La suite TRI propuesta cubre la agregación A_f/DEP/D_f que esos contratos no articulaban conjuntamente: ceros necesarios con unknown/conflicto, ruta válida con Runknown, DEP=0 con universo COMPLETE frente a PARTIAL, ruta alternativa y bloqueo focal, combinaciones basal/post, no comparabilidad global, redescubrimiento de ruta basal, ausencia de logs, separación truth/observed y error diferencial.

La tabla D_f incluye las nueve combinaciones de estados observados, pero solo es aplicable tras validar matching, identidad, frontera, granularidad, mapping y snapshots. La no comparabilidad global fuerza ?/NOT_COMPARABLE. La elegibilidad verdadera pre-Z no se acredita solo por A_f^{obs}=0.

Los IDs TRI-AF-01…05, TRI-DEP-01…05, TRI-DF-01…06 y TRI-OBS-01…03 son casos lógicos propuestos, sin fixtures serializados ni ejecución. Materialización futura reutilizará el esquema existente de test_case y mantendrá hidden_truth segregada del analizador.

**Estado:** mejora de cobertura documental, no cierre de MEAS-G4/G6/G7/G8. Pendientes la plantilla U_G completa, matching/UG-SCH-10, adjudicación independiente, error diferencial/missingness, fixtures/oráculos y revisión independiente. No autoriza implementación ni ejecución.



## 16.18. Cierre de validez IV D2 — propagación de C10-S-IV-AUD-001 (2026-11-06)

**Estado:** dictamen documental incorporado; supuestos y gates abiertos. No es cierre de identificación.

La auditoría `C10_S_D2_LATE_F_IV_VALIDITY_AUDIT_DRAFT_001.md` establece que `LATE_f` no está identificado ni listo para Wald. Se mantiene como estimando secundario condicional. La asignación aleatoria candidata puede identificar `ITT_Z` como efecto de política asignada, bajo el diseño realmente implementado y sus condiciones; no atribuye automáticamente el resultado a `D_f^*`.

Se incorporan como gates obligatorios IV-G1…IV-G8: (1) tratamiento/población/unidad/versiones; (2) primeras etapas separadas e instrumento débil; (3) independencia/interferencia/carryover; (4) exclusión y vías colaterales; (5) monotonicidad/defiers; (6) consistencia y medición; (7) Outcome y Value separados, horizonte y missingness; (8) recuperación sintética adversarial de identificación/no identificación.

Amenazas materiales: recursos/capacidad y desplazamiento, permisos, coste, latencia/calidad/seguridad, información/conocimiento, alternativas, dependencias compartidas, rollback/carryover y observación diferencial. Si no se defiende exclusión, el estimando reportable será el efecto de política/paquete (`ITT_Z` u objeto de política que corresponda) o no identificación; no Wald etiquetado como `LATE_f`.

Las primeras etapas de `C_dep^*`, `A_f,post^*`, `D_f^*` y `ΔT_acc^*` no son intercambiables. `s=0.80` no es parámetro validado. Un LATE para Outcome no identifica el LATE para Value. No se transportan resultados entre D2/D1 ni hacia `θ_A(q)` sin condiciones adicionales.

**Dependencia de cierre:** la auditoría observacional trivalente de `A_f^*/D_f^*` y el cierre de rutas/cobertura deben alimentar IV-G1/G4/G6; no se habilita Wald por completar únicamente una primera etapa técnica. No se autoriza freeze, implementación, simulación ni ejecución. La siguiente operación documental es cruzar IV-G1/G4/G6 con el contrato de snapshots, identidad/versionado, cobertura U_G y error diferencial, sin reabrir DEC-C10-066/067.



## 16.19. Dependencias cruzadas de identificación y medición — IV-G1/G4/G6 (2026-11-06)

Se fija el crosswalk operativo entre la auditoría IV D2 y la auditoría de medición, sin crear un sistema paralelo de IDs:

- **IV-G1** reutiliza MEAS-G1…G5/G8, TRI-AF-01…05, TRI-DF-01…06, ID-01…15 y SNAP-01…15 para identidad, elegibilidad basal, predicados, matching, snapshots y clasificación D_f*/D_f_obs.
- **IV-G4** reutiliza MEAS-G4, U_G y B-M01…15 para rutas alternativas/compartidas/externas/desconocidas, cobertura negativa y examen de vías colaterales. La invariancia postulada por el DGP no es prueba de exclusión.
- **IV-G6** reutiliza MEAS-G2…G8 y TRI-OBS-01…03 para pinning, cegamiento, adjudicación, error diferencial, missingness y separación truth/observación.

La regla trivalente impide convertir unknown, MISSING, NONE, PARTIAL o conflicto en cero; DEP_f_obs=0 exige universo declarado exhaustivamente cubierto; no comparabilidad temporal/semántica conserva ?. La verdad oculta no se expone al analizador. Esta especificación no demuestra que los contratos estén implementados ni que los datos permitan identificación.

**Resultado:** dependencia documental reconciliada; IV-G1/G4/G6 siguen abiertos, exclusión continúa amenazada materialmente y LATE_f no está identificado. La siguiente operación científica/documental es revisar, por cada vía B-M01…15 y ficha de invariante, qué evidencia permitiría refutar o acotar la exclusión en el DGP Opción A, sin presuponer invariancia ni crear parámetros. No se autoriza implementación ni ejecución.



## 16.20. Exclusión IV: auditoría de las quince superficies B-M01…15

Se incorpora el crosswalk adversarial C10-S-IV-AUD-001 §11 como dependencia de cierre de IV-G4. No se presume que las superficies cambien materialmente. El dossier debe distinguir modificación focal capturada por D_f*, colateral directa a Outcome/Value, mediación por conocimiento/selección/ejecución, cambio epistémico, integridad del oráculo y residuos/interferencia.

**Prioridad de prueba:** B-M06 datos/estado/App/F*; B-M07 recursos/capacidad/contención; B-M09 seguridad/riesgo/coste; B-M11 estado residual; B-M12 rendimiento/latencia; B-M14 alternativas A1/A2. Además, B-M10 conocimiento/observabilidad y B-M13 oráculo exigen controles de medición; B-M05 debe mantener C_auth,base invariante. B-M02/B-M03/B-M08 y B-M15 requieren grafo transitivo y análisis de spillover/carryover.

La evidencia de invariancia exige snapshots/diffs con cobertura suficiente, inventario de consumidores y rutas, medición independiente por unidad/versión/ventana, adjudicación ciega y falsadores explícitos. Falta de evidencia no prueba ausencia. El DGP adversarial deberá incluir al menos las ocho familias de escenarios de §11.5, sin asignar parámetros no justificados.

**Estado:** exclusión NO DEMOSTRADA; IV-G4 ABIERTO; LATE_f bloqueado. No freeze, implementación ni ejecución.

## 16.21. DGP adversarial Opción A — contrato de escenarios antes de parametrizar

La auditoría IV §12 es la especificación cualitativa de referencia para el DGP Opción A. La secuencia de trabajo queda fijada: (i) aceptar/rechazar la semántica funcional S0/S2/SF, F1=τ2, F2, A1/A2 y F*; (ii) mapear cada escenario a variables y tiempos del DGP; (iii) decidir qué mecanismos se manipulan y cuáles permanecen invariantes; (iv) definir potenciales separados para D_f*, Reach/Π/Exec, O*/O_obs y V*/V_obs; (v) solo después justificar parámetros, distribuciones, soporte y sensibilidad; (vi) materializar fixtures y oráculos únicamente tras cierre documental y autorización.

R0/EXC-F0 es control positivo focal; R1 es alternativa basal estable; R2 es alternativa afectada por B; R3 es provisión fallida. Se añaden como contrastes cualitativos separados vía directa a Outcome, vía directa a Value, conocimiento diferencial, medición diferencial, oráculo modificado, recursos compartidos y carryover. No combinar varias violaciones en un mismo fixture si impide identificar qué gate causa el dictamen.

No confundir: (a) exclusión estructural; (b) relevancia de primera etapa focal; (c) independencia/aleatorización; (d) monotonicidad; (e) consistencia/versionado; (f) interferencia; (g) validez de medición. Un escenario puede violar varios, pero debe haber controles que aíslen cada fallo. ITT_Z y LATE_f se informan por separado y Outcome/Value por separado.

**Pendiente antes de parametrizar:** ratificar semántica Opción A y definiciones F*/equivalencia alternativa; completar la tabla variable×tiempo×rol para las manipulaciones; cerrar unidad/soporte/interferencia y regla de Value; luego justificar parámetros y sensibilidad. No implementación ni ejecución.



## 16.22. Crosswalk temporal y de roles — prerrequisito de parametrización

Se incorpora DGP §28 / auditoría IV §13 como contrato común para los escenarios adversariales. DEC-C10-051 ya seleccionó Opción A como microdominio de trabajo y F* como contrato funcional candidato; esa selección no cierra las fichas operacionales versionadas de F1/τ2, adaptador, F2, A1/A2 ni el oráculo. No basta la tabla de familias: cada escenario debe materializar las variables en el reloj t−1/t0–t9/t+1…, mantener truth/observed y roles separados, y demostrar los invariantes declarados dentro del propio DGP.

**Orden obligatorio antes de parametrizar:** (1) resolver precedencia y semántica funcional de F1=τ2, F2, A1/A2 y adaptador con identidad/versiones; (2) fijar O*/O_obs y V*/V_obs, regla de Value, beneficiario y horizonte; (3) fijar unidad experimental/asignación, unidad de interferencia, pool y mapa de exposición; (4) fijar snapshots y regla temporal de rollback/washout; (5) completar variable×tiempo×rol y gates por escenario; (6) justificar soporte, distribuciones, parámetros y sensibilidad por estimando; (7) solo después serializar fixtures/oráculos con hidden_truth segregada y autorización correspondiente.

No se permite tratar el reloj temporal como ejecución real, fijar invariancia por declaración sin contraste de control, ni confundir F* técnico con oráculo de Outcome o regla de Value. La falta de observación mantiene ?; no es ausencia verdadera.

**Estado:** prerequisito documental abierto; no parametrización, implementación ni ejecución.



## 16.23. Reconciliación funcional de Opción A y criterios de salida documental (2026-11-06)

Se reutilizan las fichas F1/τ2, F2, A1/A2, matriz F*, contrato abstracto C_src/C_dst/M, matriz IAM y manifiesto B. La semántica de alto nivel queda documentada: B provisiona; C_dep* acredita estado técnico; A_f*(τ2) adjudica accesibilidad; F1 convierte S0→S2; F2 aplica S2→SF; A1/A2 componen S0→S1→SF; F* evalúa la ruta completa. No se crea una segunda especificación.

**Criterio de salida:** coherencia semántica de objetos y etapas, no aprobación de detalles ausentes. Sigue pendiente instanciación reproducible con identidad/versiones, C_src/C_dst/M, IAM, predicados FP, C0/G/H, recursos/permisos, oráculo y evidencia.

**Bloqueos:** (1) mappings y dominios de parámetros; (2) IAM pre-Z/B con obligatoriedad/NA/cobertura; (3) predicados/tolerancias y equivalencia funcional; (4) oráculo independiente, fiabilidad y cegamiento; (5) manifiesto B-M01…15 y grafo transitivo; (6) no-afectación A1/A2/F2 bajo B; (7) unidad/recursos compartidos e interferencia; (8) rollback/residuos/carryover. La ausencia de evidencia mantiene ?.

No cierra OPEN-C10-003, MD-C1/MD-C4, IV-G4, IV-G6, IV-INT ni Value; no selecciona formatos, productos, parámetros o umbrales. No Design Freeze, implementación, fixtures, validación ni ejecución.



## 16.24. Crosswalk del objeto y criterio de salida

Se reconcilia C_src/C_dst/M con CMP/PAR/REF/RUL/POL/MET, F1/F2/A1/A2, IAM y F*. Se reutilizan DEC-C10-053 (partición), DEC-C10-054 (perfil gramatical), DEC-C10-055 (reconciliación SM/FP) y DEC-C10-056 (cardinalidad), solo dentro de su alcance.

**Salida documental:** trazada la correspondencia por familia, las etapas de transformación, separación E_dst/objeto, IAM común por ruta y gate FP-08. No cierra el contrato confirmatorio.

**Bloqueos:** (1) DEFAULT vs DEFAULT_DECLARED/INHERITED/ENV_RESOLVED; (2) claves/dominios PAR; (3) universo/cardinalidad/clases CMP y multiplicidad REF; (4) M por clase, many-to-one/one-to-many y conversiones/pérdidas; (5) UNKNOWN/conflictos RUL; (6) IAM/cobertura/NA; (7) snapshot/evidencia independiente C_dst aplicado; (8) oráculo, cegamiento, concordancia/error; (9) no-afectación A1/A2/F2 por B, recursos/interferencia/carryover.

No parámetros, fixtures, parser/oráculo validado, freeze ni autorización de implementación.


## 16.25. Resolución de la discrepancia DEFAULT

La reconstrucción de DEC-C10-054 y del perfil de dominios demuestra que la distinción tripartita ya estaba aceptada. No procede abrir una nueva decisión ni reducirla a propuesta. Se armoniza la representación: estado PAR ABSENT/NULL/DEFAULT/VALUE; default_kind=DECLARED|INHERITED cuando DEFAULT; DEFAULT_ENV_RESOLVED como observación de E_dst, externa al paquete.

**Criterios aún abiertos:** contrato de herencia y scope por clave; estructura/procedencia del snapshot ambiental; mapping y tolerancias; comportamiento cuando la fuente no distingue; FP primario y oráculo; error de medición. La resolución conceptual elimina la contradicción de nivel, pero no cierra el contrato de instancia ni autoriza implementación.

## 16.26. Especialización candidata de claves PAR

El roster histórico de tres slots queda supersedido por DEC-C10-068: el núcleo aceptado contiene ENABLED BOOL y PROFILE ENUM; RETRY-COUNT queda excluido. No es esquema físico ni amplía la decisión a otros parámetros. DECIMAL/STRING quedan como extensiones condicionales; REF se modela normalmente en la clase REF.

**Cierre necesario:** verificar pertinencia P0 de cada slot; definir D_profile, N_retry_max y dominios por clave; estados admisibles/defaults; mapping por ruta; obligatoriedad IAM; regla RUL constitutiva y oráculo. No fijar valores de escenario antes de cerrar contrato. Sin freeze ni autorización de implementación.

## 16.27. Cierre sustantivo de RUL

La cardinalidad RUL≥1 ya está aceptada por DEC-C10-056. El cierre sustantivo requiere una regla constitutiva P0, no tautológica, con fuente funcional estipulada ex ante dentro del DGP, owner CMP, scope, claves/dominios, AST 4/16/16, efecto REQUIRE/FORBID y semántica TRUE/FALSE/UNKNOWN. La regla ENABLED→PROFILE se especializa en §16.28 y fue aceptada conceptualmente por DEC-C10-068 como regla del mundo sintético; no necesita una norma externa. Su contrato debe versionarse y congelarse antes de generar/analizar resultados. Después se requiere preservar semántica en F1/A1, aplicar en F2/A2, FP-03/06/07 y oráculo independiente. No freeze ni implementación.

## 16.28. Especialización funcional sintética del servicio lógico y RUL

DEC-C10-068 acepta conceptualmente el servicio lógico sintético de procesamiento de solicitudes con ENABLED BOOL, PROFILE ENUM={STANDARD,READ_ONLY,DISABLED} y RUL-SVC-ENABLE-PROFILE-01: ENABLED=true implica PROFILE∈{STANDARD,READ_ONLY}, REQUIRE. La especificación estipulada ex ante es la fuente constitutiva interna del DGP, no norma externa ni evidencia empírica. RETRY-COUNT queda excluido. La identidad CMP/versión se trata en §16.30; IAM detallado, mapping físico, FP-03/06/07, oráculo y propagación F1/F2/A1/A2 siguen abiertos. No freeze, fixtures ni implementación.

## 16.29. Efecto de DEC-C10-068 sobre el cierre de RUL

DEC-C10-068 cierra la aceptación conceptual del servicio lógico sintético, los parámetros ENABLED/PROFILE y RUL-SVC-ENABLE-PROFILE-01. La fuente funcional es el contrato constitutivo interno del DGP, no una norma externa. Por tanto, RUL-SUB-01/02 pasan de OPEN a ACCEPTED CONCEPTUALLY para esta instancia. Siguen abiertos owner CMP concreto/versionado, serialización, IAM de escenario, mapping físico, FP-03/06/07/08, oráculo, tolerancias y evidencia de preservación/aplicación. El paso siguiente es cerrar la identidad/versionado y el contrato de mapping sin elegir plataforma real ni inventar etiquetas físicas. No Design Freeze ni autorización de implementación/ejecución.

## 16.30. Identidad y versionado de la instancia CMP del servicio sintético

La siguiente tarea documental reutiliza el contrato abstracto de instancia y el contrato de matching de snapshots, sin crear otra ontología. La propuesta `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md` separa contrato, instancia, CMP, rol, versión, revisión, mapping, IAM, oráculo y hash.

**Candidatos sometidos a decisión:** contract_id=C10S-SVC-REQUEST-PROCESSOR / contract_version=1.0.0; instance_id=C10S-SVC-REQUEST-PROCESSOR-001 / instance_version=1; component_id=CMP-SERVICE-LOGIC-001 / component_class=SERVICE_LOGIC. CMP-SERVICE-LOGIC permanece como rol/owner lógico, no ID de instancia. La regla RUL y las dos claves PAR aceptadas por DEC-C10-068 conservan sus IDs.

**Reglas:** contrato semver para cambios semánticos; revisión entera inmutable para cambios de paquete; hash solo identifica serialización exacta después de congelar formato; IDs sin brazo/tiempo/resultado/plataforma; matching explícito para comparar snapshots. Versiones de C_src/C_dst, M, IAM y oráculo independientes.

**Gate:** aceptar o revisar los IDs candidatos y la política de versionado; luego instanciar MET/IAM documentalmente y cerrar tabla de mapping semántico. No fijar valores de escenario ni REF=0 sin cobertura exhaustiva. No serialización ejecutable, fixtures, parser, pruebas, Design Freeze ni autorización de implementación/ejecución.


## 16.31. Efecto de DEC-C10-069 — identidad/versionado CMP

DEC-C10-069 acepta contract_id=C10S-SVC-REQUEST-PROCESSOR / 1.0.0, instance_id=C10S-SVC-REQUEST-PROCESSOR-001 / instance_version=1, component_id=CMP-SERVICE-LOGIC-001 / SERVICE_LOGIC y la política de versionado semver + revisión entera inmutable. CMP-SERVICE-LOGIC se conserva como rol/owner lógico. La propuesta §16.30 pasa de pendiente de aceptación a aceptada en IDs y política; MET físico, serialización canónica, IAM, mapping, cobertura, oráculo y evidencia siguen abiertos. Próximo gate: mapping semántico de CMP/PAR/RUL para F1/A1 y F2/A2, con preservación, aplicación y estados UNKNOWN explícitos. No freeze, fixtures, implementación ni ejecución autorizadas.

## 16.32. Especialización CMP/PAR/RUL del mapping — propuesta documental

Se incorpora en la matriz existente C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md §20 una especialización del mapping para el servicio sintético aceptado por DEC-C10-068/069. Define identidad CMP lógica y cardinalidad de referencia; correspondencias BOOL/ENUM de los dos PAR aceptados; distinción de estados/defaults; identidad, scope, AST tipado y efecto REQUIRE de RUL-SVC-ENABLE-PROFILE-01; y separación F1/A1 (preservación), F2/A2 (aplicación), FP-06 y FP-07.

Se reconcilian explícitamente las referencias históricas: RETRY-COUNT de §15 queda fuera del núcleo por DEC-C10-068 y la aceptación de IDs pendiente de §18 queda supersedida por DEC-C10-069. No se infiere equivalencia por nombres/IDs ni se declara REF=0.

**Estado:** propuesta documental persistida; no aceptada/congelada. IAM, valores/defaults concretos, mapping físico, serialización/MET, oráculo, cobertura y evidencia siguen OPEN. Siguiente gate: reconciliar esta propuesta con IAM y contrato de oráculo, sin crear fixtures ni ejecutar. No Design Freeze, implementación o ejecución autorizadas.

## 16.33. Reconciliación IAM/Oráculo tras DEC-C10-069

La matriz IAM §17 reconcilia las notas históricas de §16 con DEC-C10-069: contract_id/version, instance_id/version y component_id/class están aceptados. La identidad del CMP focal no determina cardinalidad global CMP ni inventario físico P1. Mapping_id, IAM_id, oracle_id y hash de artefacto permanecen pendientes de sus contratos/versiones.

Se define como requisito documental que IAM instancie O/C/NA/? por ruta, etapa, objeto, propiedad, snapshot y cobertura; distinga C_src, S1/S2, C_dst declarado, C_dst aplicado y E_dst/runtime; y mantenga separados truth del DGP, salidas cegadas del Analizador y adjudicación posterior del Evaluador. El oráculo compara truth esperada con estado efectivamente observado; no convierte truth en evidencia ni C_dst declarado en C_dst aplicado.

**Estado:** requisitos IAM/oráculo documentados, no aceptados ni congelados. Roster completo, valores/defaults por escenario, mapping/AST, política UNKNOWN/conflicto, evidencia admisible, cegamiento, suficiencia de cobertura y serialización siguen OPEN. No fixtures, schema ejecutable, parser, implementación ni ejecución científica.

## 16.34. Roster mínimo y cierre IAM pre-Z/B

La matriz IAM §18 reconcilia el roster funcional mínimo aceptado: CMP-SERVICE-LOGIC-001; PAR-SVC-ENABLED BOOL; PAR-SVC-PROFILE ENUM; RUL-SVC-ENABLE-PROFILE-01 REQUIRE; MET obligatorio; POL ausente por diseño en el núcleo. REF=0 requiere inventario/cobertura exhaustivos pre-Z/B. La fila histórica PAR-SVC-RETRY-COUNT de §13 queda supersedida para el núcleo por DEC-C10-068.

No hay DEFAULT contractual declarado para los dos PAR; no se inventan defaults ni valores de escenario. VALUE tipado es candidato confirmatorio; ABSENT/NULL no son admisibles para REQUIRED; DEFAULT requiere declaración contractual trazable. El roster no es todavía inventario exhaustivo ni permite declarar ausencias.

**Gate siguiente:** completar el inventario por C_src, S1/S2, C_dst declarado y C_dst aplicado; fijar cobertura; después instanciar O/C/NA/? por ruta/etapa/propiedad y sellar IAM antes de Z/B. No Design Freeze, implementación o ejecución autorizadas.

## 16.35. Inventario de configuración por snapshot y cobertura

La matriz IAM §19 y la plantilla U_G §18 establecen el overlay de captura para C_src, F1→S2, A1→S1, C_dst declarado y C_dst aplicado en F2/A2. Reutilizan los registros U_G y DEC-C10-065; no crean tablas físicas ni fuerzan PAR/RUL a NODE/PREDICATE. Un manifiesto documental por objeto/propiedad enlaza snapshot exacto, etapa/ruta, mapping, evidencia y coverage_scope.

Los scopes de cobertura se separan por snapshot×etapa×ruta×clase CMP/PAR/REF/RUL/MET. COMPLETE requiere universo/denominador trazables. REF=0 exige cobertura exhaustiva; NONE/PARTIAL/UNKNOWN mantienen ?. Contrato/catálogo no equivalen a evidencia de snapshot ni de aplicación.

El contrato abstracto §16 y catálogo atómico §15 reconcilian el slot histórico RETRY-COUNT como supersedido por DEC-C10-068; ENABLED/PROFILE no tienen DEFAULT aceptado.

**Gate siguiente:** aceptar o revisar la convención textual propuesta para SNAPSHOT.scope en matriz IAM §19.3 y plantilla U_G §18.2; después verificar compatibilidad/parseo antes de instanciar snapshots sintéticos. La propuesta fija phase=route-test y stage/ruta en scope, sin codificar Z/B. No capturar datos ficticios, no declarar COMPLETE, no Design Freeze, implementación o ejecución autorizadas.
## 16.36. Scopes de cobertura por snapshot, etapa, ruta y clase

La matriz IAM §19.7 y U_G §18.6 definen un scope lógico independiente por snapshot exacto × etapa × ruta × clase CMP/PAR/REF/RUL/MET, con hasta 35 scopes para las siete etapas y cinco clases. Se reutiliza COVERAGE_REGISTER §12.3 sin ampliar columnas. coverage_scope_id es PK opaca; dimension distingue la clase; universe_definition/version debe fijar snapshot_id y snapshot_object_record_id, etapa/ruta, regla de enumeración y versión del universo.

Se fijan denominadores por clase y criterios NONE/PARTIAL/COMPLETE. Ausencia/REF=0 exige cobertura completa y evidencia de enumeración exhaustiva; no se infiere 0 por falta de filas. Los dos PAR REQUIRED ausentes bajo cobertura COMPLETE constituyen incumplimiento.

**Limitación a resolver antes de schema freeze:** COVERAGE_REGISTER no contiene FK directa al snapshot exacto; el pinning en universe_definition/version no permite constraint relacional inversa. Mantener U_G-SCH-10 OPEN y no añadir columnas sin decisión de schema. La codificación de SNAPSHOT.scope continúa pendiente de aceptación/compatibilidad. No crear scopes ficticios ni ejecutar.

## 16.37. Cierre de integridad de scopes de cobertura

Separar este gate de U_G-SCH-10: la pertenencia del grafo a snapshot está aceptada semánticamente por DEC-C10-065/Opción A; la validación física del grafo conserva su propio estado. Para COVERAGE_REGISTER, los objetos enlazan coverage_scope_id y fijan snapshot exacto, pero la fila de cobertura no contiene snapshot_id/snapshot_object_record_id; no hay enforcement compuesto de coincidencia.

C0 fue aceptada mediante DEC-C10-070 como contrato documental (esquema actual + tupla exacta en universe_definition/version). El control independiente sigue OPEN y CONDITIONAL hasta su especificación, autorización, ejecución y auditoría. C1 (columnas de snapshot + FK compuestas) necesita decisión de schema, análisis de ciclo con SNAPSHOT.coverage_scope_id y compatibilidad/legacy. C2 (tabla puente) no se recomienda salvo inviabilidad de C1.

Antes de freeze: comparar alternativas contra DDL completo, cardinalidad scopes×snapshot, filas históricas y motor. No alterar schema ni declarar integridad relacional plena.

## 16.38. C0 aceptada y gate del control independiente

DEC-C10-070 acepta C0 como contrato documental condicionado: mantener el schema y fijar por coverage_scope_id la tupla exacta en universe_definition/version. Todo objeto que referencia el scope debe coincidir. El control futuro debe comprobar binding exacto, unicidad, cardinalidad, huérfanos/no usados y conflictos.

Gate previo a Design Freeze: especificación del control y sus casos adversariales; autorización específica antes de implementarlo/ejecutarlo; evidencia de resultado; auditoría independiente/adjudicación. Hasta entonces CONDITIONAL; no afirmar FK ni integridad relacional garantizada. C1/C2 no aceptadas. No hay autorización actual de implementación ni ejecución científica.


## 16.39. Especificación del control C0 y gates de cierre

La especificación documental está en el protocolo de evidencia/adjudicación §19. Incluye tupla completa, invariantes C0-I01…I11, precedencia de resultados PASS/FAIL/UNKNOWN y casos ADV-C0-01…15.

Pendiente antes de implementación: recuperar y reconciliar DDL completo; demostrar mapping de campos y cardinalidad; definir exportación cerrada del universo; revisar casos adversariales y falsos PASS/FAIL/UNKNOWN. La implementación y ejecución requieren autorización técnica específica, distinta de la autorización científica. Antes de Design Freeze: ejecutar y auditar todas las pruebas, preservar inputs/outputs/hash y adjudicar discrepancias.

Estado actual: especificación documental completada; NOT IMPLEMENTED / NOT EXECUTED / NOT AUDITED; C0 CONDITIONAL. Un PASS del control no equivale a COMPLETE ni REF=0.

## 16.40. Crosswalk de la tupla C0 al esquema — gate abierto

El protocolo §20 identifica huecos de representación: stage_key no tiene columna propia; SNAPSHOT.phase no equivale a stage_key y SNAPSHOT.scope sigue sin aceptación; route_id no está directamente en NODE/EDGE; object_class CMP/PAR/REF/RUL/MET carece de campo común tipado. contract/instance versions y dimension dependen de declaraciones versionadas recuperables. snapshot_id + snapshot_object_record_id sí están cubiertos por DEC-C10-065/Opción A.

Antes de implementar C0 se requiere crosswalk semántico por campo/tabla, con regla para rutas globales y route-specific, clases y etapas, y gramática/hash de universe_definition/version. Hasta entonces UNKNOWN para correspondencias no demostradas; no PASS por inferencia. No schema change ni implementación autorizada.


## 16.41. Cierre del crosswalk semántico C0↔U_G

Reutilizar el crosswalk IAM histórico y sus auditorías; no recrear el mapping. Mantener separados object_class C10, ug_record_type y NODE.semantic_role/boundary_class.

DEC-C10-071 acepta los siete valores de stage_key C10-S de U_G §18.2: C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED y A2_DST_APPLIED. No son el reloj DGP t−1…t9 ni SNAPSHOT.phase (baseline/post-B/rollback/route-test); SNAPSHOT.timestamp es el instante de captura. Cualquier correspondencia al reloj DGP requiere regla explícita en universe_definition/version.

La aceptación del vocabulario no acepta la serialización de etapa/ruta en SNAPSHOT.scope. La antigua ruta NONE/F/A es familia/branch label, no route_id exacto; CONFIG no es object_class aceptado por C0. C0 requiere CMP/PAR/REF/RUL/MET y route_id exacto o token global reservado. NODE/EDGE route membership se demuestra por ROUTE_STEP; PREDICATE por route_record_id; ROUTE por su propia revisión.

Gate pendiente: definir token global y route_id exacto, gramática versionada de universe_definition/version y mappings por propiedad/owner; después reconciliar contra DDL. Hasta entonces UNKNOWN donde no pueda demostrarse correspondencia. No schema change, scopes/snapshots, implementación ni ejecución autorizada.


## 16.42. Semántica route_id y scope global — propuesta pendiente de aceptación

El protocolo de evidencia §20.8 compara G1 token reservado, G2 NULL/vacío y G3 scope_kind. Recomendación provisional G1 con literal candidato C10S_SCOPE_GLOBAL para “sin restricción a ruta concreta”; no significa ausencia de rutas ni no pertenencia. En route-specific, route_id semántico debe resolver route_record_id y snapshot exactos. CMP/PAR/REF/RUL/MET tienen reglas de pertenencia diferenciadas; ROUTE_STEP/record IDs exactos son evidencia para NODE/EDGE y no se sustituye por routes_affected.

Scopes globales cuentan cada objeto una vez; scopes route-specific conservan denominadores separados. Pertenencia 1 requiere crosswalk exacto; 0 requiere cobertura exhaustiva y significa únicamente no pertenencia a esa ruta; ? ante mapping/cobertura incompletos; NA solo por IAM ex ante. El token no está aceptado y la gramática universe_definition/version sigue OPEN. No schema change ni autorización de implementación/ejecución.


## 16.43. DEC-C10-072 — token global aceptado; gates restantes

El literal reservado `C10S_SCOPE_GLOBAL` queda aceptado en el slot route_id C0 para “sin restricción a una ruta concreta”; no denota ausencia de rutas/no pertenencia/NA y no puede ser route_id semántico real. Colisión = FAIL. NULL/vacío/NONE/F/A no son sustitutos. Scope global cuenta cada identidad elegible una vez; route-specific mantiene denominadores independientes y requiere route_id + route_record_id + snapshot exactos.

Cerrado: elección G1 y literal/semántica. Abiertos: gramática y versionado completos de universe_definition, mapping físico por clase/propiedad, controles C0 implementados y auditados, fixtures y cualquier Design Freeze. No se autoriza implementación ni ejecución científica.



## 16.44. UDG-01 — gramática versionada de universe_definition (propuesta)

El protocolo de evidencia §20.10 especifica UDG-01: envelope JSON autocontenido con scope C0 exacto de nueve componentes, membership_mode EXPLICIT/RULE_DEFINED, referencias tipadas o regla versionada, fuentes/manifiestos, cardinalidad declarada y provenance. Dimension permanece fuera de la tupla. Cero miembros exige evidencia exhaustiva; lista vacía no basta. Canonicalización UTF-8/NFC, orden determinista y SHA-256 son propuestas, no contrato aprobado. schema_version semver y universe_revision monotónica/inmutable son candidatos.

Estado: DOCUMENTED PROPOSAL; U1 recomendada provisionalmente; no schema change, parser, validator, fixture, implementación ni ejecución. Pendientes: aceptación de envelope/gramática, canonicalización/hash, mapping físico por clase/propiedad y control C0 independiente auditado.


## 16.45. DEC-C10-073 — arquitectura U1 aceptada

U1 queda ACCEPTED como arquitectura documental de universe_definition: envelope JSON autocontenido/versionado, estructura y cardinalidades UDG-01, scope C0 exacto de nueve componentes, modos EXPLICIT/RULE_DEFINED, referencias tipadas, cardinalidad y procedencia. Universo vacío exige evidencia exhaustiva. La separación conceptual schema_version/universe_revision se acepta; reglas completas de incremento/compatibilidad permanecen por especificar.

Gates abiertos: canonicalización concreta, hash normativo, autoridad RFC/JCS, serialización física, mapping CMP/PAR/REF/RUL/MET y control C0 independiente implementado/auditado. No schema change, parser, validator, fixtures, Design Freeze ni ejecución.


## 16.46. UDG-02 — canonicalización/hash (propuesta)

El protocolo §20.12 compara C1 RFC 8785 JCS + prevalidación TGCV, C2 canonicalizador propio y C3 hash de bytes fuente; recomienda provisionalmente C1. Reglas candidatas: strings preservadas por JCS y NFC validada previamente en campos señalados; arrays de conjunto ordenados por identidad antes de canonicalizar, secuencias preservadas; enteros seguros no negativos; null prohibido; hash canónico separado del hash de bytes fuente y registrado fuera del contenido hasheado.

No se acepta aún C1, SHA-256, el perfil TGCV-C10S-JCS-1 ni sus restricciones. La igualdad de hash no demuestra equivalencia semántica/exhaustividad. Pendiente decisión explícita; no parser, validator, fixtures, schema change ni ejecución.


## 16.47. DEC-C10-074 — canonicalización JCS aceptada

C1 RFC 8785 JCS con prevalidación TGCV queda ACCEPTED como política documental para envelope U1, perfil TGCV-C10S-JCS-1. Reglas completas en DEC-C10-074/protocolo §20.13: validación NFC previa en campos marcados; arrays conjuntos ordenados por identidad; arrays secuenciales preservados; enteros seguros no negativos; null prohibido; hashes de artefacto y contenido canónico separados; SHA-256 del contenido canónico.

No autoriza hash de producción, parser/validator, fixtures, schema físico, Design Freeze ni ejecución. Pendientes: mapping físico CMP/PAR/REF/RUL/MET y control C0 independiente implementado/auditado.


## 16.48. UDG-03 — comparación semántica (propuesta)

Antes de Design Freeze debe existir contrato de comparación que separe identidad/revisión, artefacto/canónico, igualdad extensional y equivalencia definicional. Requisitos: scope C0/stage/route/snapshot compatibles; versiones exactas de miembros; exhaustividad de ambos universos; reglas/AST/dependencias y fuentes recuperables; mapping explícito entre contratos/instancias cuando difieran. Resultados por dimensión EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE; FAIL para integridad. Hash/ID/revision/cardinality no demuestran equivalencia. Propuesta UDG-03 en protocolo §20.14, no aceptada; comparator/fingerprint/fixtures/schema change/ejecución no autorizados.


## 16.49. DEC-C10-075 — contrato documental de comparación aceptado

UDG-03 queda ACCEPTED documentalmente: siete niveles de comparación, Projection-ID/Projection-SEM, precondiciones de scope/snapshot/miembros versionados/exhaustividad y resultados EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE; FAIL reservado a integridad. Igualdad extensional no implica equivalencia definicional; mismo hash/ID/nombre/cardinality no la demuestra. Incompatibilidad de scope sin mapping = NOT_COMPARABLE; evidencia faltante = UNKNOWN.

No comparator/fingerprint semántico, migración, fixtures, parser/validator, schema change, Design Freeze ni ejecución autorizados. Registro DEC-C10-075; prevalece sobre §16.48.


## 16.50. UDG-04 — contrato de referencias tipadas (propuesta)

Antes de cerrar mapping REF/CMP/PAR/RUL, resolver identidad lógica vs record identity, roles de referencia, resolución exacta contra registry versionado, cardinalidad, referencias opcionales/requeridas, acceso/incompletitud y ciclos por relación. Se propone que UNKNOWN distinga registry no disponible de inexistencia exhaustiva; NOT_COMPARABLE cubra incompatibilidad sin mapping; FAIL se reserve a ausencia requerida/dangling exhaustivo/conflicto/inmutabilidad. Resolver no equivale a pertenencia ni aplicabilidad.

Propuesta en protocolo §20.16, plantilla U_G §18.21, mapping §20.18 y maestro §195. UDG-04 NO ACEPTADA; schema REF/API/resolver/parser/validator/fixtures/implementación/ejecución no autorizados.


## 16.51. DEC-C10-076 — contrato documental de referencias aceptado

UDG-04 queda ACCEPTED documentalmente: identidad lógica vs record identity inmutable; referencia tipada por rol y target exacto; resolución exacta contra registry versionado/scope explícito; estados FAIL/UNKNOWN/NOT_COMPARABLE/NOT_APPLICABLE separados; ciclos y cardinalidad declarados por relación. Resolver no implica membership/aplicabilidad/preservación/ejecución.

Pendientes: reconciliar catálogo REF; cerrar roles/cardinalidad por clase; schema físico, API/registry/resolver y mapping CMP/PAR/RUL. No autorizados parser/validator/comparator/fixtures/implementación/Design Freeze/ejecución. DEC-C10-076 prevalece sobre §16.50.

## 16.52. Gate de reconciliación del catálogo REF con UDG-04

**Estado:** propuesta documental; no aceptada ni congelada.

Antes de fijar schema físico REF se deben resolver: distinción REF/UDG-reference/FK U_G; modelo de extremos internos/externos; identidad lógica y record_id exactos; dominio de relation_type/direction/role; multiplicidad y cardinalidad; mapping REF↔EDGE y reglas split/merge/n-arias; aplicabilidad por stage_key/scope; evidencia y adjudicación. Los roles de DEC-C10-076 siguen ilustrativos, no enum cerrado.

Criterio de salida documental: matriz IAM por clase×rol×extremo×ruta×etapa; cardinalidades justificadas ex ante; crosswalk REF→EDGE con mapping versionado; casos ADV para endpoint intercambiado, revisión equivocada, snapshot cruzado, duplicación, dangling, endpoint externo no resoluble y dependencia declarada confundida con instalada. El gate no requiere implementar ni ejecutar; schema físico, resolver y pruebas siguen sujetos a autorización separada.

## 16.53. DEC-C10-077 — gate conceptual REF aceptado; IAM pendiente

La base conceptual de REF↔UDG-04 queda ACCEPTED: REF es objeto del dominio con identidad propia/extremos tipados; referencias envelope y FK U_G son capas distintas; REF→EDGE solo por M versionado, sin 1:1 presumido y con parent/group identity para split/merge/n-aria. Permanecen como gates OPEN el catálogo final de roles, dominios de extremos, cardinalidad/obligatoriedad por clase×rol×extremo×stage_key×scope, reglas de ciclos, endpoints externos, IAM y evidencia. No hay autorización de schema físico, resolver ni ejecución.


## 16.54. DEC-C10-078 — contrato lógico IAM aceptado; valores de aplicación abiertos

DEC-C10-078 acepta documentalmente las cuatro capas IAM (L1 membership del universo; L2 referencias del envelope UDG; L3 extremos funcionales REF; L4 FK/vínculos estructurales U_G) y el contrato lógico contextual de fila: `iam_rule_id`, `layer`, `source_class`, `source_identity_rule`, `role_namespace`, `role_key`, `endpoint_position`, `target_domain`, `min_cardinality`, `max_cardinality`, `requiredness`, `applicability_trigger`, `stage_key`, `scope_mode`, `route_binding`, `version_snapshot_binding`, `integrity_rule`, `mapping_rule`, `evidence_rule`, `adjudication` y `rationale/provenance`.

La aceptación cierra la estructura documental del contrato de filas, no los valores de sus campos ni la aplicabilidad por instancia. Se reutilizan DEC-C10-071/072 sin reabrir sus vocabularios.

**Siguiente gate documental:** proponer y contrastar vocabularios candidatos por capa, separando expresamente (a) roles de referencias del envelope UDG en L2 y (b) roles/extremos funcionales de objetos REF en L3. Mantener L1 y L4 como membership/FK estructural, no convertirlos en roles REF. Después, justificar dominios/cardinalidades/requiredness por clase×rol×extremo×stage_key×scope, y reconciliar mapping M sin fijar aún un mapping concreto.

**OPEN:** vocabularios finales, dominios internos/externos, cardinalidades numéricas, requiredness, integridad concreta, evidencia/adjudicación concreta y mapping M. No schema físico, roster exhaustivo, IAM poblado, fixtures, parser/validator, implementación, Design Freeze ni ejecución autorizados.


## 16.55. Propuesta de vocabularios IAM L2/L3 — gate documental siguiente

Se incorpora como propuesta no aceptada la separación de namespaces `UDG_ENVELOPE_ROLE` (L2) y `REF_FUNCTIONAL_ROLE` (L3). L2 reutiliza como candidatos ilustrativos MEMBER, OWNER, SOURCE, INCLUSION_RULE, EXCLUSION_RULE, DEPENDENCY y PROVENANCE, con dominios destino y límites documentados en la matriz IAM §19.13. L3 mantiene `role_key` y `relation_type` abiertos; SOURCE/TARGET es solo posición de extremo binario. `DEPENDS_ON` puede examinarse como candidato funcional únicamente si aparece en REF necesario para el DGP, sin aceptarlo como enum.

**Siguiente tarea:** resolver la semántica de DEPENDENCY en L2 (target REF frente a target directo); extraer el conjunto mínimo de relaciones REF realmente exigido por el DGP; modelar sus extremos binarios/n-arios; y luego derivar dominios/cardinalidades/requiredness por clase×rol×extremo×stage_key×scope. No instanciar filas ni sellar IAM todavía. Esta propuesta no cambia el estado de los bloques 3–8 del §10 ni autoriza implementación/ejecución.

## 16.56. DEPENDENCY L2 — propuesta de resolución semántica no aceptada

Para una dependencia entendida como relación del dominio de configuración, la referencia L2 debe apuntar al REF exacto que representa esa relación; los extremos funcionales pertenecen al REF/L3. No apuntar directamente al objeto dependiente, porque se perdería la identidad propia de la relación y se colapsarían L2/L3.

Se separan dos casos que no deben reutilizar ese significado: (a) dependencias técnicas/ambientales (C_dep/E_dst, runtime, recursos, permisos, instalación), que no crean REF por sí mismas; y (b) dependencias usadas para resolver/evaluar un universo RULE_DEFINED, que se registran como referencias tipadas/versionadas de la regla/envelope, no como REF funcional salvo declaración independiente.

Para el DGP base actual, el roster mínimo CMP/PAR/RUL aceptado no declara una relación REF concreta. REF=0 sigue posible solo tras inventario/cobertura exhaustivos pre-Z/B; no se inventa una dependencia ni se sella REF=0 ahora. Propuesta no aceptada; no cambia DEC-C10-078 ni autoriza implementación/ejecución.

## 16.57. Auditoría del conjunto mínimo REF L3 — resultado provisional

El contrato sintético aceptado CMP-SERVICE-LOGIC-001 + PAR-SVC-ENABLED/PROFILE + RUL-SVC-ENABLE-PROFILE-01 no exige actualmente una relación REF funcional concreta. Los operandos de la RUL, las relaciones R_acc/R* del espacio transformacional, las dependencias técnicas C_dep/E_dst y las referencias de evaluación RULE_DEFINED no se convierten en REF por defecto.

El roster mínimo no es un inventario exhaustivo: no autoriza declarar REF=0. El valor cero solo podrá adjudicarse por snapshot×etapa×ruta×scope con enumeración exhaustiva y cobertura COMPLETE pre-Z/B. Todo REF añadido debe justificar identidad propia de la relación, extremos exactos, semántica, dirección/tipo/rol, multiplicidad, versión/snapshot y distinción frente a FK/condición externa/referencia de regla.

Estado: auditoría documental propuesta; sin filas observadas ni IAM sellado. El siguiente gate es contrastar esta lista negativa con inventarios exhaustivos de C_src/C_dst y con los scopes por stage_key, antes de asignar cardinalidad/requiredness.

## 16.58. Auditoría REF por snapshot y etapa — protocolo propuesto

El siguiente gate IAM es una auditoría de relaciones REF por cada combinación exacta de contrato/instancia, snapshot, stage_key, ruta, scope y universo versionado. Reutiliza el inventario U_G y sus registros de evidencia/cobertura; no crea un segundo inventario. La matriz IAM §19.16 especifica inspección diferenciada de C_SRC, F1_S2, A1_S1, F2/A2_DST_DECL y F2/A2_DST_APPLIED.

Una relación solo se clasifica REF si tiene identidad propia, semántica de dominio, extremos exactos, dirección/tipo/multiplicidad, pertenencia al paquete y procedencia. EDGE/FK/ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos RUL, R_acc/R*, dependencias técnicas C_dep/E_dst y refs de evaluación RULE_DEFINED no se elevan por defecto a REF. Cualquier doble representación U_G↔REF requiere mapping M explícito/versionado.

PRESENT requiere evidencia suficiente; ABSENT/REF=0 exige universo y fuentes exhaustivos y COVERAGE_REGISTER COMPLETE para el scope exacto; UNKNOWN permanece si hay cualquier laguna/conflicto; NA exige no aplicabilidad ex ante. Los snapshots declarados no prueban el estado aplicado. Sin snapshots reales, el resultado sigue siendo protocolo documental, no inventario ni adjudicación.

**Gate:** obtener fuentes/snapshots exactos, poblar U_G y coverage por etapa×ruta×clase, adjudicar candidatos REF y solo entonces derivar cardinalidad/requiredness IAM. Propuesta no aceptada; sin ejecución ni implementación autorizada.

## 16.59 — Inspección cruzada de clases por etapa

**Estado:** PROPUESTA DOCUMENTAL DE INSPECCIÓN; no aceptada como cierre IAM, no implementada y sin observaciones reales. Deriva de DEC-C10-053/056/059/061/062/065/069/070/071/072/073/074/075/076/077 y de los contratos U_G y de instancia existentes. No altera cardinalidades, vocabularios ni obligatoriedad aprobados.

### Unidad de inspección
Cada observación se ancla a la tupla exacta de identidad de contrato/instancia y versión, snapshot y registro, `stage_key`, ruta o `NONE` justificado, scope y universo/versionado. Se reutilizan NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER de U_G. No se crea un inventario paralelo ni se generan registros ficticios.

### Matriz de búsqueda por clase × etapa

| Clase | C_SRC | F1_S2 | A1_S1 | F2_DST_DECL | A2_DST_DECL | F2_DST_APPLIED | A2_DST_APPLIED |
|---|---|---|---|---|---|---|---|
| CMP | Inventario e identidad fuente | CMP afectado y mapping F1 | CMP exportado y preservación | CMP destino declarado | CMP que A2 declara importar/aplicar | CMP producido/materializado por F2 | CMP realmente presente/aplicado |
| PAR | key, owner, tipo, state y value | Conversión, defaults, pérdidas y cambios | Estados/valores exportados | PAR destino declarado y conversión | PAR que A2 declara importar | PAR materializado por F2 | Estado/valor efectivamente aplicado |
| RUL | rule_id, AST, scope, efecto | Reglas transformadas/preservadas/omitidas | Reglas exportadas | Reglas destino y mapping | Reglas que A2 declara importar | Reglas materializadas | Reglas efectivas tras aplicación |
| REF | Inventario, identidad propia, endpoints | Transformación/correspondencia de relación | Referencias exportadas e integridad | REF destino declarada y mapping | REF que A2 declara importar/resolver | REF materializada | Resolución e integridad efectiva de extremos |
| MET | Identidad/versiones contrato, instancia, fuente, snapshot y provenance | Versiones de transformación y artefactos | Identidad de export, formato y lineage | Identidad/versiones destino y mapping | Identidad de import declarado | Artefacto producido, hash y lineage | Registro de aplicación, snapshot y evidencia posterior |

La matriz es un **mapa de inspección**, no una declaración de presencia. F1/A1/F2/A2 no crean automáticamente objetos semánticos. La presencia en cada etapa requiere evidencia específica. `C_DST_DECLARED` no prueba `C_DST_APPLIED`; una diferencia de hash/nombre no prueba equivalencia funcional.

### Evidencia mínima y adjudicación
- **CMP:** identidad semántica y registro exacto, clase/rol, boundary_class cuando proceda, scope y pertenencia al snapshot; mapping explícito para correspondencias entre etapas.
- **PAR:** parameter_key, owner, tipo, estado ABSENT/NULL/DEFAULT/VALUE, valor cuando corresponda, requiredness y dominio/unidad activados; no colapsar estados.
- **RUL:** rule_id, AST tipado, scope explícito (incluido GLOBAL), efecto REQUIRE/FORBID y precedencia/temporalidad solo cuando aplique.
- **REF:** ref_id/registro propio, extremos tipados SOURCE/TARGET, dirección, tipo/rol, multiplicidad si procede, pertenencia al paquete y provenance. No elevar EDGE, FK, ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos RUL, R_acc/R*, C_dep/E_dst ni refs RULE_DEFINED a REF funcional automáticamente.
- **MET:** identidades/versiones exactas, IAM_id/version/hash, mapping_id/version, oráculo/versión, timestamps y provenance de artefactos/evidencias. El hash es control de artefacto, no prueba semántica.

Estados por predicado y unidad de cobertura:
- `1`: presencia/condición acreditada por evidencia suficiente y coherente.
- `0`: ausencia/incumplimiento solo con búsqueda exhaustiva y cobertura COMPLETE del universo, etapa, ruta/scope y versión pertinentes.
- `?`: evidencia, resolución, mapping o cobertura insuficiente/contradictoria.
- `NA`: no aplicabilidad declarada ex ante en IAM, con fundamento de dominio; nunca por falta de evidencia.
- `NOT_COMPARABLE`: versiones/identidades sin mapping aprobado; no sustituir por 0.
- `NOT_APPLICABLE` solo cuando lo autorice el contrato aplicable, distinto de desconocido.

Para REF=0 se requiere inventario exhaustivo del límite funcional y cobertura exacta. La cardinalidad base permanece CMP≥1, PAR≥1, RUL≥1, REF≥0 y MET obligatorio; no se cambia por esta matriz. La aplicabilidad de una clase/propiedad en una etapa se decide con el contrato y el stage_key, no por extrapolación desde otra etapa.

### Exclusiones y salvaguardas
La inspección de CMP/PAR/RUL/REF se refiere al paquete P0. Entorno destino, runtime, recursos, permisos efectivos, C_dep y estados técnicos P1 se registran en sus objetos/mediciones correspondientes; no se incorporan al paquete ni se convierten automáticamente en REF. Las relaciones estructurales U_G (FK) siguen siendo distintas de REF. REF→EDGE requiere mapping M explícito/versionado; EDGE→REF no se infiere. Split/merge/n-aria exige identidad/grupo y regla de conservación explícitos.

### Estado actual
No se han inspeccionado snapshots reales ni se han asignado valores a ninguna celda. No se declara REF=0, cobertura COMPLETE, IAM sellado, cardinalidades adicionales, implementación, validación, fixtures, simulación o ejecución. La siguiente operación tras aceptación será completar el protocolo de extracción/registro de observaciones usando los snapshots existentes; si no hay snapshots, primero habrá que resolver esa ausencia sin fabricar datos.

## 16.60 — Disponibilidad de snapshots y crosswalk de extracción

**Estado:** HALLAZGO DOCUMENTAL / PROPUESTA DE GATE; sin datos observados ni decisión de implementación.

### Resultado de inspección
La plantilla canónica `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md` declara expresamente `DRAFT / PLANTILLA VACÍA / NO INVENTARIADA / NO EJECUTADA`. Sus filas ilustrativas son marcadores de esquema, no registros. El registro de snapshots contiene una fila de plantilla con `No capturado`; la matriz de cobertura está en `NONE` para sus dimensiones. Por tanto, en los artefactos revisados no hay snapshots C10-S reales utilizables ni evidencia de cobertura que permita iniciar extracción de observaciones. Esto no demuestra que no existan fuentes externas; significa que no están incorporadas ni referenciadas como observaciones U_G en esta rama.

### Hallazgo de proyección de clases
U_G dispone de diez registros canónicos: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. No hay tablas físicas independientes CMP, PAR, RUL, REF o MET. No se permite asumir equivalencias nominales:
- CMP: candidatos de representación en NODE según `semantic_role` y frontera, pero NODE no equivale automáticamente a CMP.
- PAR: no existe tabla PAR dedicada; la representación/serialización de propiedades debe quedar mapeada explícitamente a campos/artefactos y a su identidad de owner.
- RUL: PREDICATE registra predicados observados/analíticos; no equivale automáticamente a una regla declarativa RUL con AST, scope y efecto.
- REF: DEC-C10-077 distingue el objeto REF de EDGE y de FK estructural U_G. EDGE no es REF; REF→EDGE requiere mapping M explícito y versionado.
- MET: identidad, versión, snapshot y provenance se distribuyen entre campos de objetos, SNAPSHOT y EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK; MET no es una tabla ni un objeto homogéneo por defecto.

### Protocolo de extracción — cuando existan fuentes
1. Localizar la fuente original y registrar custodio, método, timestamp, versión/hash, alcance y limitaciones en EVIDENCE_REGISTER; no copiar secretos.
2. Verificar que corresponde al contrato/instancia exactos y al snapshot/fase temporal declarados. No emparejar por nombre, hash aislado ni `latest`.
3. Resolver el mapping clase conceptual→representación U_G mediante contrato explícito/versionado. Si no existe o no conserva semántica, adjudicar `UNKNOWN` o `NOT_COMPARABLE`, no forzar una fila.
4. Crear/actualizar registros U_G solo mediante el procedimiento autorizado; fijar snapshot y record IDs exactos, `stage_key`, ruta/scope y universo.
5. Registrar cada afirmación con CLAIM_EVIDENCE_LINK y EVIDENCE_REGISTER; cobertura con COVERAGE_REGISTER; evaluación/adjudicación separadas.
6. Mantener por separado declarado, producido y aplicado. Una fuente C_DST_DECLARED nunca acredita A2_DST_APPLIED.
7. Adjudicar 0 solo con búsqueda exhaustiva y COVERAGE_REGISTER COMPLETE para el universo, versión, etapa y scope exactos; ? ante falta de fuente/mapping/cobertura; NA solo por regla ex ante IAM.

### Gate previo a cualquier extracción
- Identificar fuente(s) real(es) y snapshots existentes; si no existen, definir por separado cómo se obtendrán y autorizar su captura.
- Resolver el crosswalk CMP/PAR/RUL/REF/MET↔U_G sin colapsar REF/EDGE ni RUL/PREDICATE.
- Confirmar identidad/versionado, stage_key, route/scope y snapshot pinning.
- Definir cobertura, evidencia y adjudicación por clase/etapa.
- Solo entonces completar observaciones. La plantilla no se rellena con ejemplos sintéticos ni valores inferidos.

**Conclusión:** no procede todavía extraer ni adjudicar observaciones. El siguiente trabajo documental es cerrar el crosswalk semántico de representación y especificar qué fuentes/snapshots alimentarán cada etapa. No se declara ausencia de objetos, REF=0, IAM sellado, cobertura COMPLETE ni disponibilidad de datos externos. `scientific_execution=false`; `execution_authorized=false`.

## 16.61 — Cierre documental de representación PAR

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión nueva, no implementada, sin instancias ni observaciones reales. Reutiliza DEC-C10-053/054/056/068/069/070/073/074/075/076 y el contrato abstracto de instancia, la matriz de mapping PAR y el overlay U_G existente. No sustituye ni amplía el schema físico U_G.

### 1. Decisión de diseño propuesta
Representar PAR como **propiedad atómica tipada del CMP propietario**, no como NODE independiente y no como EDGE/REF. La identidad semántica de cada parámetro es `parameter_key` dentro del contrato/versión y el ámbito de `owner_component_id`; la instancia observada se distingue por la tupla exacta de contrato/instancia, snapshot/record, stage_key, ruta/scope y versión del CMP owner. Esta opción evita inventar un `semantic_role=PARAMETER` (no existe en el vocabulario aceptado de NODE), evita tratar una propiedad escalar como componente y preserva el ownership ya definido.

La representación es una **fila lógica de manifiesto IAM/inspección**, usando la estructura de referencia ya descrita en U_G §18.3 (manifest_record_id, contract/instance, snapshot exacto, stage_key, route, object_class=PAR, semantic_id/version, owner_component_id, property_key/type/state/value, mapping, declared_or_applied, evidence, claim-evidence, coverage y adjudicación). No se crea una tabla física PAR ni una nueva capa semántica persistida. La fila de manifiesto no recibe por ahora un object_record_id U_G ni una FK nueva: el contrato de identidad de esa fila sigue OPEN.

### 2. Campos semánticos por PAR
Cada entrada lógica debe resolver, sin inferencia:
- `parameter_key` estable y no reutilizable para otro significado;
- `owner_component_id` exacto y su CMP NODE/record/version en el mismo snapshot;
- `type`, dominio/escala/unidad cuando proceda;
- `requiredness` y disparador condicional, si lo hubiera;
- `allowed_states` y estado observado, diferenciando ABSENT, NULL, DEFAULT y VALUE;
- `value` solo si el estado lo permite y procede de la fuente observada;
- `default_contract` (kind, origen, scope, precedencia y versión) solo cuando exista declaración;
- mapping_id/version, estado MAPPED/UNMAPPED/AMBIGUOUS/NOT_APPLICABLE y regla de conversión;
- evidencia, cobertura, adjudicación y procedencia exactas.

No colapsar ausencia, null, default declarado/heredado y valor explícito. `DEFAULT_ENV_RESOLVED` es resolución de E_dst/P1, enlazada al parámetro y snapshot ambiental, no un estado adicional del paquete P0 ni una reescritura de DEFAULT.

### 3. Especialización ya aceptada para el servicio sintético
El roster nuclear se limita a:
- `PAR-SVC-ENABLED`: BOOL, dominio `{false,true}`, REQUIRED.
- `PAR-SVC-PROFILE`: ENUM, dominio `{STANDARD, READ_ONLY, DISABLED}`, REQUIRED.

`PAR-SVC-RETRY-COUNT` queda fuera del núcleo confirmatorio por DEC-C10-068. No debe incorporarse al universo base ni usarse como proxy de capacidad P1. Para ENABLED y PROFILE, ABSENT/NULL no son admisibles; DEFAULT no queda declarado por DEC-C10-068 y solo podría usarse tras declaración contractual explícita, versionada y previa al IAM. No se asignan valores de escenario en este contrato de representación.

### 4. Proyección y enlaces con U_G
- El CMP propietario se resuelve a NODE exacto mediante `component_id/node_id + object_record_id + snapshot_id`; no se resuelve por nombre, rol lógico ni hash.
- La fila lógica PAR referencia ese owner y conserva `parameter_key` como identidad de propiedad. No crea un NODE adicional ni una arista EDGE.
- `COVERAGE_REGISTER` conserva scopes independientes `C10S_CONFIG_PAR` por snapshot×stage_key×ruta/scope, con universo/denominador explícitos. No combinar cobertura PAR con CMP.
- Como CLAIM_EVIDENCE_LINK no admite target_type=PAR, la propuesta es vincular la afirmación a la revisión exacta del NODE owner y/o al COVERAGE_SCOPE correspondiente; `claim_statement` y `relevance_scope` deben identificar inequívocamente `parameter_key`, propiedad, estado y etapa. No se añade un nuevo FK ni se finge que la evidencia apunta a una tabla PAR.
- EVIDENCE_REGISTER conserva fuente, versión, método, integridad y límites; no copiar valores sensibles ni credenciales.
- M mantiene la correspondencia `parameter_key_src → parameter_key_dst`, owner, tipo, dominio, unidad, estado, valor/default y conversión. M es artefacto evaluativo versionado, no EDGE ni una capa semántica adicional.

### 5. Evaluación independiente y etapas
La comparación se realiza por parámetro y etapa, preservando la separación:
- C_SRC: contrato/propiedad fuente observada.
- F1_S2 y A1_S1: representación intermedia producida por cada ruta.
- F2_DST_DECL y A2_DST_DECL: propiedad destino declarada, no aplicada.
- F2_DST_APPLIED y A2_DST_APPLIED: propiedad efectivamente observada tras aplicación.

La evidencia de una etapa no se traslada a otra. El mismo `parameter_key` lógico no prueba por sí solo correspondencia; M debe resolver el owner y la transformación tipada. La equivalencia de valor no compensa una diferencia de tipo, dominio, unidad, estado o default. El analizador no accede a truth oculta ni a etiquetas del oráculo.

### 6. Adjudicación y límites
`1` exige predicado satisfecho con evidencia/cobertura suficiente; `0` exige incumplimiento confirmado o ausencia exhaustiva según el predicado; `?` ante falta de fuente, owner, mapping, snapshot o cobertura; `NA` solo por no aplicabilidad ex ante IAM. `NOT_COMPARABLE` cuando versiones/identidades no tengan mapping aprobado. Una propiedad ausente en el artefacto no equivale a ausencia de observación ni autoriza imputar valor/default.

La propuesta no fija cardinalidades adicionales, no asigna REQUIRED/OPTIONAL nuevos, no cambia DEC-C10-068, no aprueba el roster fuera del núcleo ya aceptado, no añade semantic_role, tabla PAR, FK, EDGE ni REF, no sella IAM, no define serialización ni hash, y no autoriza parser, validator, fixtures, implementación, Design Freeze o ejecución.

### 7. Cuestiones aún abiertas
1. Identidad/versionado de la fila lógica de manifiesto PAR y su relación exacta con el registro IAM sellado.
2. Regla formal para claim_statement/relevance_scope que haga inequívoca la referencia a parameter_key sin crear FK PAR.
3. Mapping concreto de owner y property_key entre representaciones fuente/destino e intermedias.
4. Evidencia disponible por etapa y cobertura real.
5. Defaults y sus reglas por clave, si alguna vez se incorporan; no se presuponen.

## 16.62 — Identidad de registro lógico PAR

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión, no implementada y sin filas/observaciones reales. Resuelve la laguna de identidad detectada en §§19.2/19.19 y §17, sin extender DEC-C10-062 ni modificar el schema U_G.

### 1. Separación de identidades
La fila lógica PAR del manifiesto no es una entidad U_G de las tablas NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. Por tanto:
- `parameter_key` identifica la propiedad semántica en el ámbito de contrato/versión y owner CMP; no identifica una observación.
- `manifest_record_id` identifica una fila concreta e inmutable del manifiesto; es opaco, no vacío y único dentro del manifiesto/versionado IAM que la contiene. No reutilizar `object_record_id`, `node_id`, `component_id` ni IDs TID/SID/RID/EID.
- La clave lógica de captura PAR queda propuesta como la tupla exacta: contract_id/version + instance_id/version + snapshot_id/snapshot_object_record_id + stage_key + route_id/route_record_id o ausencia justificada + scope/universe revision + owner_component_id y revisión exacta del CMP + parameter_key/semantic_version. Esta clave delimita qué observación se está representando; no sustituye a manifest_record_id.
- `coverage_scope_id` sigue siendo identidad del scope de cobertura, independiente de la fila PAR.

### 2. Revisión y corrección
Se propone que cada fila sea inmutable. Una corrección de captura, adjudicación o metadato de la fila no sobrescribe el registro previo: crea un nuevo `manifest_record_id`, incrementa `manifest_record_revision` en uno para la misma clave lógica y señala el registro inmediatamente anterior mediante `supersedes_manifest_record_id`. La primera revisión es 1 y no tiene predecesor. Solo puede existir una cadena lineal por clave lógica; no se admiten bifurcaciones, ciclos, saltos, referencias cruzadas entre claves o snapshots ni reutilización de IDs. El historial se conserva.

Una nueva observación en otro snapshot, etapa, ruta/scope, versión de owner o versión contractual no es una revisión de la misma fila: constituye una nueva clave lógica y comienza revisión 1. Un cambio semántico de parameter_key o de significado exige nueva identidad de parámetro conforme al contrato, no supersession de captura.

Los campos `manifest_record_revision` y `supersedes_manifest_record_id` son nombres propuestos de contrato lógico, no columnas físicas aprobadas. La propuesta no fuerza un `object_version` ni `supersedes_record_id` U_G.

### 3. Límite de DEC-C10-062
DEC-C10-062 se aplica expresamente solo a NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT; las demás tablas mantienen sus propias claves y contratos. No puede extenderse por analogía a filas de manifiesto. La mención histórica en §19.2 de que manifest_record_id sería versionado “conforme a DEC-C10-062 si se adopta” queda aclarada por esta propuesta: el manifiesto necesita contrato propio y no hereda object_version/supersedes_record_id de U_G. Esta aclaración no altera la decisión aceptada ni la reescribe; precisa el límite de su ámbito.

### 4. Unicidad y control
Para una misma clave lógica y revisión debe existir exactamente un manifest_record_id; un manifest_record_id no puede identificar dos claves/revisiones. Toda referencia a una fila debe resolver por ID exacto dentro de la versión de manifiesto/IAM fijada, nunca por latest, posición, nombre o hash aislado. La verificación documental deberá comprobar:
- no duplicidad de manifest_record_id;
- unicidad de clave lógica + manifest_record_revision;
- revisión inicial 1 sin predecesor;
- sucesión inmediata y misma clave lógica para revisiones posteriores;
- ausencia de ciclos, bifurcaciones, huérfanos y referencias futuras;
- pinning exacto del snapshot y del CMP owner;
- coherencia de coverage_scope_id con la misma tupla de etapa/ruta/clase/universo;
- preservación de múltiples evidencias como vínculos separados, no serializadas en la fila.

No se impone unicidad global entre distintas versiones de manifiesto/IAM; el namespace exacto y su versión forman parte de la resolución.

### 5. Estados de propiedad y ausencia
Una fila PAR representa una propiedad esperada/inspeccionada, no presupone que la propiedad esté presente en el artefacto. `state=ABSENT` puede registrarse solo con evidencia/cobertura según el predicado; no se elimina la fila por ausencia. `NULL`, `DEFAULT` y `VALUE` permanecen distintos. El registro de una revisión no convierte por sí mismo ? en 0 ni acredita COMPLETE.

### 6. Límites
No se crea tabla PAR, no se añaden columnas U_G, no se aprueba DDL/serialización/API/parser/validator/fixtures, no se asignan valores de escenario ni se instancia el manifiesto. La aceptación de esta propuesta, si se produce, será documental y no autorizará implementación ni ejecución. IAM permanece sin sellar; `scientific_execution=false`; `execution_authorized=false`.

### 7. Pendientes para aceptación
- Confirmar namespace de unicidad: por versión de manifiesto/IAM (propuesta) frente a global en toda la línea C10-S.
- Confirmar si la revisión de captura es necesaria o si bastaría append-only con IDs nuevos y relación de supersession.
- Confirmar nombre final de los campos de revisión y predecesor.

## 16.63 — Recomendación de adjudicación de identidad PAR

**Estado:** RECOMENDACIÓN PARA ACEPTACIÓN DEL USUARIO; no es DEC aceptada ni contrato congelado. Se propone resolver conjuntamente las tres cuestiones abiertas de §17.1/§19.20/§20/§16.62/§80/§207/§86.

### Recomendación única
1. **Unicidad de `manifest_record_id`: global en toda la línea C10-S**, independiente de versión IAM/manifest. El ID es opaco, inmutable y nunca se reutiliza. La versión IAM sigue formando parte de la resolución contextual de la fila, pero no limita la unicidad del identificador. Se recomienda unicidad global porque simplifica referencias, auditoría y detección de colisiones entre versiones; no implica que el registro sea una entidad U_G.
2. **Modelo append-only con revisión explícita.** Cada corrección/adjudicación posterior genera nuevo `manifest_record_id`; no se sobrescribe ni elimina la fila anterior. Para una misma clave lógica de observación, `manifest_record_revision` empieza en 1 y aumenta exactamente en uno. Las revisiones posteriores incluyen `supersedes_manifest_record_id` apuntando a la revisión inmediatamente anterior. Una sola cadena lineal por clave lógica; sin bifurcaciones, ciclos, saltos ni huérfanos. La revisión es metadato de secuencia de captura, no versión semántica del parámetro.
3. **Nombres recomendados:** `manifest_record_revision` y `supersedes_manifest_record_id`, exactamente así. `manifest_record_id` se mantiene como identificador del registro, distinto de `parameter_key`, CMP owner, `object_record_id` U_G y `coverage_scope_id`.

### Reglas para evitar revisiones falsas
- Nueva etapa, snapshot, ruta/scope, contrato/instancia o revisión del CMP owner = nueva clave lógica y revisión 1, no supersession.
- Cambio de significado de `parameter_key` = nueva identidad semántica; no se corrige como revisión de captura.
- Corrección de transcripción, evidencia, estado, mapping o adjudicación de la misma captura lógica = nueva revisión, conservando la anterior.
- Varias evidencias para una misma fila son vínculos independientes; no crean revisiones por sí solas.
- Un cambio de versión IAM que solo reempaqueta la misma fila no genera automáticamente una nueva observación. Si la identidad lógica de captura permanece idéntica, la política de migración/referencia deberá conservar el ID; si cambia una dimensión de la clave lógica, comienza una nueva cadena. La migración entre versiones IAM requiere mapping explícito y no se presume.

### Condición de aceptación
La aceptación confirmaría solo este contrato lógico documental de identidad/supersession. No crea columnas, tabla PAR, DDL, serialización, generador de IDs, API, parser, validator, fixtures ni registros reales; tampoco sella IAM, cierra el crosswalk PAR↔U_G, autoriza implementación o cambia `scientific_execution=false` / `execution_authorized=false`.

**Pendiente de aceptación expresa:** unicidad global; append-only + revisión explícita; nombres exactos indicados.

## 16.64 — Propagación de DEC-C10-079

**Estado:** ACEPTADO — DEC-C10-079. Esta sección propaga el contrato lógico aprobado; prevalece sobre cualquier recomendación previa que mantuviera abiertas estas cuestiones.

- `manifest_record_id`: globalmente único en toda la línea C10-S, opaco, inmutable y nunca reutilizado, independiente de la versión IAM.
- Append-only: ninguna fila se sobrescribe ni elimina. Toda corrección de la misma captura lógica crea un nuevo ID y conserva el anterior.
- `manifest_record_revision`: revisión secuencial por clave lógica, desde 1, sin saltos.
- `supersedes_manifest_record_id`: en revisiones posteriores, referencia a la revisión inmediatamente anterior de la misma clave lógica. Cadena lineal única, sin bifurcaciones, ciclos, huérfanos ni referencias cruzadas.
- Cambio de snapshot, etapa, ruta/scope, contrato/instancia o revisión del CMP owner inicia una nueva clave lógica y revisión 1. Cambio semántico de `parameter_key` exige nueva identidad semántica.
- Múltiples evidencias no crean revisiones por sí solas. Reempaquetar en nueva versión IAM no crea automáticamente nueva observación; migración exige mapping explícito.

**Límites:** decisión documental lógica. No crea tabla/columnas PAR o U_G, DDL, serialización, generador, API, parser, validator, fixtures ni registros reales; no sella IAM, no cierra PAR↔U_G, no autoriza Design Freeze, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 16.65 — Cierre del binding probatorio PAR

**Estado:** PROPUESTA DOCUMENTAL; no aceptada como nueva DEC, no implementada, sin registros observados. Reutiliza DEC-C10-079 y el esquema U_G §12.2–12.3/§18.3–18.8. No amplía los dominios ni las FK de U_G.

### 1. Principio
CLAIM_EVIDENCE_LINK no tiene target_type PAR ni FK a manifest_record_id. No se simula una FK inexistente. La trazabilidad se compone de:
(a) FK real a COVERAGE_SCOPE (y, cuando la afirmación se refiere al owner CMP como objeto por derecho propio, un vínculo separado al NODE owner);
(b) localizador lógico exacto de la fila PAR en claim_statement/relevance_scope;
(c) control independiente que resuelve ese localizador contra el manifiesto IAM versionado y verifica su integridad.

### 2. Perfil normativo propuesto para una afirmación sobre una fila PAR
Una fila CLAIM_EVIDENCE_LINK por cada evidencia × afirmación × fila PAR:
- `claim_target_type=COVERAGE_SCOPE`;
- `target_coverage_scope_id` = scope PAR exacto, cuyo `dimension=C10S_CONFIG_PAR` y cuyo universe_definition/version fija contrato/instancia, snapshot+record, stage_key, route/scope, clase PAR y universo;
- todos los campos target_* no aplicables quedan vacíos; no se rellenan FK de NODE como sustituto de PAR;
- `claim_statement` identifica explícitamente el predicado y la fila: `PAR_ROW|manifest_record_id=<ID>|manifest_record_revision=<N>|parameter_key=<KEY>|owner_component_id=<CMP_ID>|predicate=<PREDICATE>`;
- `relevance_scope` identifica el contexto completo: `contract_id/version;instance_id/version;snapshot_id/snapshot_object_record_id;stage_key;route_id/route_record_id-or-justified-NONE;coverage_scope_id;owner_component_id/owner-record/version;parameter_key;manifest_record_id;manifest_record_revision`.
Los literales anteriores describen un perfil documental de campos textuales existentes, no una gramática física ni un parser aprobado. No se deben usar separadores/valores ambiguos; si algún identificador contiene delimitadores, la serialización futura tendrá que definir escaping/versionado antes de automatizar.

### 3. Resolución y controles independientes
El control debe resolver manifest_record_id globalmente (DEC-C10-079), verificar revision y supersession, y comprobar igualdad exacta entre la fila del manifiesto, su clave lógica, owner CMP, snapshot, stage_key, route/scope y coverage_scope_id. También verifica:
- dimension C10S_CONFIG_PAR y universe_definition/version compatibles;
- que el scope corresponde a la misma tupla y no está compartido entre snapshots/etapas/rutas/clases;
- que el CMP owner resuelve al NODE/object_record_id/snapshot exactos;
- que parameter_key y manifest_record_revision coinciden con el manifiesto;
- que la evidencia está en EVIDENCE_REGISTER y que la relación 1:N se conserva sin listas serializadas;
- que la evidencia realmente respalda el predicado y estado citados; un enlace FK correcto no prueba el contenido.
Un fallo de resolución, contradicción o colisión es FAIL; falta de manifiesto, snapshot, scope o fuente es UNKNOWN/?; incompatibilidad de versiones sin mapping es NOT_COMPARABLE; NA solo por inaplicabilidad ex ante. No inferir 0 desde falta de vínculo.

### 4. Owner CMP y cobertura
Si una misma evidencia respalda también una afirmación distinta sobre identidad/estado del CMP owner, se crea otro CLAIM_EVIDENCE_LINK con target NODE y su FK exacta. No se duplica ni se mezcla esa afirmación con la afirmación PAR. La afirmación PAR conserva COVERAGE_SCOPE como target FK y el localizador PAR en campos textuales.
COVERAGE_REGISTER permanece por clase PAR y por snapshot×stage_key×ruta/scope; COMPLETE exige denominador, fuentes, enumeración y excepciones conforme a §18.6. El link a un scope no convierte automáticamente el scope en COMPLETE.

### 5. Límites y decisiones abiertas
No se añade target_type PAR, FK, tabla PAR, columna U_G, tabla puente ni relación física nueva. No se crea CLAIM_EVIDENCE_LINK directo a manifest_record_id; su resolución es un control independiente contra el manifiesto. No se define todavía escaping/canonicalización del localizador, vocabulario de predicate ni automatización. No se sella IAM, no se declara cobertura, no se crean registros y no se autoriza parser, validator, fixtures, implementación o ejecución.
Pendiente de aceptación: perfil COVERAGE_SCOPE + localizador en claim_statement/relevance_scope; vínculo NODE separado solo para afirmaciones propias del CMP; control independiente de resolución.

## 16.66 — Propagación de DEC-C10-080

**Estado:** ACEPTADO — DEC-C10-080. Sustituye el estado pendiente de aceptación de §17.4/§19.23/§23/§16.65/§83/§210/§89.

- Afirmación sobre fila PAR: CLAIM_EVIDENCE_LINK usa `claim_target_type=COVERAGE_SCOPE` y FK `target_coverage_scope_id` al scope exacto `dimension=C10S_CONFIG_PAR`.
- `claim_statement` y `relevance_scope` contienen localizador lógico suficiente para resolver `manifest_record_id`, `manifest_record_revision`, `parameter_key`, owner CMP, snapshot/record, `stage_key`, ruta/scope y universo/version.
- Una fila CLAIM_EVIDENCE_LINK por evidencia×afirmación×fila PAR. Las evidencias múltiples se conservan como filas separadas, nunca como listas embebidas.
- Control independiente resuelve ID global y verifica revisión/supersession y coincidencia exacta de clave lógica, owner, snapshot, etapa, ruta/scope, coverage scope, universo, predicado y evidencia.
- Una afirmación separada sobre el CMP owner usa otro CLAIM_EVIDENCE_LINK con target NODE y FK exacta. No sustituye el target COVERAGE_SCOPE de la afirmación PAR.
- El enlace al scope no implica COVERAGE COMPLETE; se aplican U_G §12.3/§18.6.

**Restricciones:** no se añade target_type PAR, FK, tabla o puente. No se aprueban gramática, escaping, canonicalización, serialización, parser ni automatización. Los campos singulares `evidence_id`/`claim_evidence_id` del manifiesto no sustituyen el registro 1:N de CLAIM_EVIDENCE_LINK. No se crean observaciones, no se sella IAM, no se declara cobertura ni se autoriza implementación/ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 16.67 — Control independiente PAR propuesto

**Estado:** PROPUESTA DOCUMENTAL; pendiente de aceptación. Desarrolla DEC-C10-080 reutilizando el C0 ya especificado en el protocolo de evidencia §19; no crea un segundo control genérico.

Se separan cinco capas: C0_SCOPE; PAR_ROW_BINDING; EVIDENCE_LINK_INTEGRITY; EVIDENCE_RELEVANCE; COVERAGE_COMPLETENESS. Se define una secuencia P0–P11 para aplicabilidad, target, resolución C0, dimensión/universo, identidad PAR global, clave lógica/pinning, supersession DEC-C10-079, evidencia, correspondencia de afirmación, pertinencia sustantiva, vínculo NODE separado solo si hay afirmación propia del owner y cobertura.

El control conserva resultados PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA por capa, sin colapsarlos. Un registro histórico superseded conserva validez histórica, pero no acredita estado actual sin justificación temporal. Una FK correcta no prueba pertinencia; un scope COMPLETE tampoco se infiere del vínculo.

Se añaden 18 casos adversariales documentales y requisitos de informe. Se reconocen expresamente las limitaciones ya detectadas en §20.1–20.5: mappings stage_key, clase y ruta aún abiertos producen UNKNOWN donde impiden resolución inequívoca.

No se amplía U_G ni se cierra gramática/escaping/canonicalización/predicate. No crea fixtures, parser, validator ni registros. No autoriza implementación, Design Freeze, validación técnica ni ejecución. `scientific_execution=false`; `execution_authorized=false`.

 
## 16.68 — Aceptación del protocolo de control independiente PAR (DEC-C10-081)

**Estado:** ACEPTADO — contrato lógico documental.

Queda aceptado el §20.18 del protocolo de evidencia como control independiente del binding PAR, con reutilización de C0, cinco capas, entradas mínimas, secuencia P0–P11, identidad/supersession DEC-C10-079, estados por capa y 18 casos adversariales. Integridad, pertinencia sustantiva y cobertura permanecen como evaluaciones distintas.

No se cierran los mappings físicos/semánticos stage_key, clase y ruta ni la gramática del localizador. UNKNOWN es obligatorio cuando falte resolución inequívoca. Esta decisión no autoriza automatización, implementación, Design Freeze ni ejecución del control o del experimento. `scientific_execution=false`; `execution_authorized=false`.


## 16.69 — Reconciliación del plan de cierre con DEC-C10-082…088

**Corte:** 2026-11-08. **Estado:** actualización documental del plan; no es Design Freeze ni autorización de implementación.

La cadena de adjudicación temporal F/A queda documentalmente definida por DEC-C10-085, DEC-C10-086, DEC-C10-087 e integrada por DEC-C10-088. El trabajo pendiente ya no es decidir la estructura conceptual de esos tres tramos, sino especificar mappings, poblar/validar el manifiesto con evidencia y construir el control técnico autorizado.

### Secuencia de cierre revisada

1. **Sincronización documental:** mantener Closure Control Matrix, plan, matriz abstracta, matriz temporal, crosswalk y Decision Log alineados con DEC-C10-088. La discrepancia documental queda identificada para reconciliación; no debe presentarse como bloqueo científico nuevo.
2. **Cierre de especificación IAM/U_G:** resolver roster CMP, clases y rutas; mappings exactos/versionados; cardinalidades y requiredness por rol/etapa/scope; REF endpoints y mapping M; localizador PAR (gramática/escaping/canonicalización); relación con COVERAGE_REGISTER y evidencia 1:N.
3. **Cierre de invariantes y vías colaterales D2:** completar auditoría adversarial de rutas alternativas y de IV-G4; no convertir una lista de controles definidos en evidencia de exclusión. Registrar fuente, método, resultado y sensibilidad por vía.
4. **Cierre de estimandos e identificación:** especificar población/unidad, elegibilidad, soporte, versiones, interferencia, ITT primario y condiciones para LATE secundario; separar efecto total, mediado por accesibilidad y residual. Resolver medición independiente de T_acc, Reach, trayectoria, Outcome y Value, y los requisitos P177/P178/P179/P182/P183.
5. **Contrato de implementación:** solo después de los cierres anteriores, definir artefactos, interfaces, oráculo, generador, analizador, evaluador, fixtures, hashes y auditoría técnica. La especificación debe preservar separación Generator/Analyzer/Evaluator y no exponer truth/potentials al Analyzer.
6. **Autorización y ejecución:** fase separada, requiere autorización explícita, preflight y workflow técnico completo. No está habilitada por esta actualización.

### Gates y estado

- DEC-C10-088: **cerrada documentalmente** en el alcance de integración temporal F/A.
- IAM/U_G: **definido parcialmente; especificación y mappings pendientes**.
- Cobertura/observaciones: **pendiente de evidencia**; no hay sello IAM ni adjudicación de cobertura.
- Exclusión causal D2/IV-G4: **pendiente de evidencia y análisis**.
- Identificación/medición/potencia/sensibilidad: **pendiente de especificación y evidencia**.
- Implementación D2: **bloqueada** hasta cerrar especificaciones mínimas y aprobar el contrato de implementación.
- Ejecución científica: **no autorizada**; scientific_execution=false; execution_authorized=false.

La clasificación detallada y trazable por requisito reside en la Closure Control Matrix §87; este plan no crea una segunda matriz. No se declara Design Freeze ni se rebajan los criterios de identificación causal.


## 16.70 — Especificación lógica CMP↔NODE e inventario de identidad

El crosswalk §10.20 propone el primer contrato lógico de mapping CMP↔NODE reutilizando DEC-C10-069, DEC-C10-082 y los diez registros U_G existentes.

Orden de cierre:
1. aceptar o corregir el contrato lógico propuesto;
2. completar el roster CMP desde el universo contractual completo, sin inferir cardinalidad total desde el único CMP de referencia;
3. especificar mapping de CMP adicionales y P1, si aplican, por snapshot exacto;
4. resolver el soporte físico ya existente para mapping/MET sin añadir columnas por conveniencia;
5. definir controles de unicidad, cobertura y evidencia; mantenerlos como especificación hasta autorización técnica.

**Estado:** propuesta documental; no IAM poblado, no mappings observados, no implementación ni ejecución. La aceptación de esta especificación lógica, si se produce, no implicará aprobación de schema físico ni cierre de evidencia.


## 16.71 — Reconciliación de roster CMP con U_G y frontera

El crosswalk §10.21 es la propuesta vigente para clasificar los 23 roles U_G frente a las clases IAM. No debe derivarse el roster CMP de la lista de nodos ni de boundary_class.

Siguiente secuencia:
1. aceptar/corregir la clasificación funcional de N01–N23;
2. recuperar el universo contractual completo de la instancia y enumerar component_id/component_class/version sin inventar instancias;
3. resolver cada objeto condicional N01, N07, N14, N17, N18, N20 y N21 por identidad, granularidad, clase IAM y boundary_class;
4. mapear solo los CMP confirmados a NODE anchor exacto por snapshot, reutilizando DEC-C10-082;
5. especificar los mappings REF/PAR/RUL/MET sin colapsar sus clases;
6. mantener roster completeness UNKNOWN/PARTIAL hasta enumeración y cobertura suficientes.

**Gate:** la propuesta de clasificación no acredita existencia, ausencia, roster exhaustivo ni cobertura. No se crean registros ni se captura información técnica. La aceptación conceptual no autoriza implementación o ejecución.

## 16.72 — Resolver N01: unidad lógica frente a host y S0

La propuesta crosswalk §10.22 desambigua N01 en tres objetos: NODE raíz LOGICAL_SERVICE_UNIT; host/entorno P1 descompuesto solo según el criterio de granularidad; y S0 como SNAPSHOT basal con pinning exacto.

Siguiente secuencia:
1. aceptar/corregir esta separación conceptual;
2. mantener sin IDs ni registros cualquier host/runtime no observado;
3. resolver si CMP-SERVICE-LOGIC-001 y NODE raíz son la misma entidad de dominio o requieren mapping explícito, sin inferirlo de sus etiquetas;
4. solo tras autorización específica, capturar snapshots y evidencias por universo/scope; hasta entonces cobertura NONE/UNKNOWN;
5. continuar con el siguiente rol condicional únicamente después de resolver N01.

No se autoriza acceso a sistemas, captura de snapshots, población IAM, implementación, Design Freeze o ejecución.
## 16.73 — DEC-C10-089: cierre conceptual N01 y mapping pendiente

DEC-C10-089 acepta NODE raíz `LOGICAL_SERVICE_UNIT` como representación de la unidad lógica de servicio; host/entorno se mantiene separado como contexto P1 sujeto a granularidad; S0 se representa como SNAPSHOT basal con pinning exacto.

La relación del NODE raíz con CMP-SERVICE-LOGIC-001 queda OPEN hasta mapping explícito, versionado y sustentado. No se debe crear ni inferir un segundo NODE ni reutilizar automáticamente la raíz como CMP anchor.

**Siguiente paso:** mantener esta distinción y continuar con el siguiente rol condicional del roster, N07, separando endpoint/interfaz (REF) de componente/servicio (CMP) según identidad contractual, lifecycle y granularidad. No capturar ni inspeccionar sistemas sin autorización específica. Sin IAM sellado, implementación, Design Freeze ni ejecución.
## 16.74 — Reconciliación del NODE raíz y el anchor CMP

Conforme DEC-C10-089 y la reconciliación crosswalk §10.24, mantener separados los conceptos:
- NODE raíz LOGICAL_SERVICE_UNIT = unidad lógica de servicio;
- NODE anchor CMP = correspondencia 1:1 del CMP contractual por snapshot conforme DEC-C10-082.

Ambos pueden ser el mismo registro solo si un mapping explícito lo demuestra; si son distintos, se conservan dos registros relacionados. No se infiere ninguna de las dos alternativas. Esta precisión corrige la lectura ambigua de «NODE raíz para el CMP» en §10.6 sin reabrir ni modificar DEC-C10-082.

Siguiente trabajo: resolver N07 como interfaz/REF frente a CMP de servicio independiente, sin inventar endpoints ni IDs; la decisión será documental hasta contar con identidad contractual y evidencia.
## 16.75 — Resolver N07 endpoint/interfaz/servicio

Crosswalk §10.25 propone separar endpoint técnico, contrato/interfaz y servicio proveedor. Tras aceptación conceptual, resolver identidad/clase de cada uno sin inferencia nominal; determinar REF solo para objeto de dominio con identidad y extremos propios; CMP solo para servicio contractual autónomo; endpoint como atributo o recurso P1 según granularidad.

No realizar inspección técnica ni pruebas de red sin autorización específica. No asignar IDs ni poblar IAM.
## 16.76 — DEC-C10-090: cierre conceptual N07 y pendientes de adjudicación

DEC-C10-090 acepta la separación endpoint/interfaz/servicio y sus criterios conceptuales de clasificación. Se continúa con N14 (formato/artefacto de intercambio), manteniendo la misma disciplina: contrato/formato versionado, artefacto concreto y componente que lo produce/consume son objetos distintos salvo identidad contractual demostrada.

Los objetos técnicos N07 siguen sin observarse ni adjudicarse. No inspeccionar sistemas, probar conectividad ni asignar IDs sin autorización específica. Sin IAM sellado, implementación, Design Freeze o ejecución.
## 16.77 — Resolver N14: formato, payload y transferencia

Crosswalk §10.27 refina el N14 ya existente y plantilla U_G §25. Antes de aceptar o implementar, verificar que la propuesta preserva N14, E12/E13 y B-M14 sin duplicar objetos ni convertir relaciones candidatas en observadas.

Tras aceptación conceptual, el siguiente gate será N15 (importador A2): separar capacidad/implementación/ejecución; entrada declarada frente a payload realmente recibido; parseo, validación, mapping M y aplicación efectiva; errores, tolerancias y evidencia por etapa. Reutilizar DEC-C10-088 para la adjudicación temporal F/A donde corresponda. No inferir aplicación desde recepción ni duplicar el oráculo N16.

No fijar aún formato concreto, IDs, columnas, parser, serialización de payload ni mapping físico. Sin captura, implementación, Design Freeze o ejecución.
## 16.78 — DEC-C10-091: cierre conceptual N14 y siguiente gate N15

DEC-C10-091 acepta la separación de formato/contrato, payload y eventos de transferencia. Se conserva N14 existente, E12/E13 candidatas, N07 para canal/endpoint y M para mapping. Permanecen pendientes la adjudicación de objetos y eventos reales, compatibilidad y evidencia.

**Siguiente gate: N15 — importador A2.** Separar capacidad/contrato del importador, entrada declarada, payload realmente recibido, parseo, validación, resolución/aplicación de M, estado efectivamente aplicado y evidencia por etapa. Diferenciar errores de transporte, formato, semántica, mapping y aplicación. Reutilizar DEC-C10-088 para adjudicación temporal F/A cuando corresponda; no duplicar el oráculo N16 ni inferir aplicación desde recepción.

El siguiente trabajo será documental. No fijar parser, formato físico, IDs, columnas ni mapping físico. Sin captura, implementación, Design Freeze o ejecución.
## 16.79 — Resolver N15: importador A2

Crosswalk §10.29 propone descomponer N15 en capacidad/contrato, implementación y ejecución, sin asumir CMP autónomo. La cadena de inspección documental separa A2_DST_DECL, recepción, parseo, validación estructural/semántica, resolución M, aplicación FP-06, post-check FP-07 y provenance FP-08. Se reutilizan DEC-C10-086/087/088 y los siete stage_key; los hitos internos no crean etapas ni predicados nuevos.

Tras aceptación conceptual, el siguiente gate debe ser N16 — oráculo F*: delimitar criterio funcional, implementación del oráculo y adjudicación/evaluator; fijar F* común para F/A y ruta alternativa, con cegamiento del Analyzer y evaluación posterior independiente. Antes de ello, reconciliar si el contrato F* ya está definido en artefactos históricos y qué partes siguen abiertas. No duplicar el criterio, no asumir oráculo implementado ni usar logs A2 como veredicto funcional.

No inspeccionar ni probar importadores. Sin parser, validator, implementación, Design Freeze o ejecución.

## 16.80 — DEC-C10-092: aceptación conceptual N15 y gate N16

Se acepta documentalmente la descomposición N15 propuesta en crosswalk §10.29: capacidad/contrato A2, implementación y ejecución separados; hitos de recepción, parseo, validación, resolución M, aplicación FP-06, post-check FP-07 y provenance FP-08 diferenciados. Se reutilizan DEC-C10-071/086/087/088, los siete stage_key y FP-01…08. No se crean nuevos predicados ni se presume CMP autónomo.

**Siguiente gate: N16 — reconciliación del oráculo F*.** Antes de proponer especificación nueva, recuperar los contratos históricos de F*, matriz FP-01…08, regla no compensatoria, reglas de aplicabilidad/NA/UNKNOWN, C0/G/H, equivalencia F/A y adjudicación Generator/Analyzer/Evaluator. El resultado debe separar: (1) criterio funcional común F* para ambas rutas; (2) implementación/versionado del oráculo independiente; (3) adjudicación y evidencia, con Analyzer ciego a truth/potenciales y Evaluator actuando después de congelar sus outputs.

No asumir que la regla candidata es decisión aceptada ni que existe oráculo implementado/validado. No usar logs A2 como veredicto funcional. El siguiente trabajo es documental; sin fixtures, parser, validator, pruebas, simulaciones, implementación, Design Freeze o ejecución.


## 16.81 — Gate de conformidad semántica para generación de código y reconciliación de estimandos

**Estado:** control documental integrado; no autoriza implementación, Design Freeze, validación técnica ni ejecución.

### 16.81.1. Contrato de estimandos actualizado

El documento `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md` ha retirado del cuerpo operativo las formulaciones anteriores que presentaban D1 como principal condicionado o D2 como contraste. Se mantienen sus definiciones de escenario y trazabilidad en el historial Git, no como instrucción vigente.

La lectura actual queda:
- C10-D1: θ_A(q) sigue siendo la pregunta científica general.
- C10-S: D2 primario candidato / D1 secundario por DEC-C10-066.
- Políticas materiales D2 por DEC-C10-067: B_g0^D2 no programa/inicia intento focal; B_g1^D2 programa intento estandarizado de provisión técnica focal.
- ITT_Z^D2 es efecto de asignación a las políticas; no se iguala a efecto de accesibilidad ni a política recibida.
- LATE_f^D2 permanece secundario y no identificado/no listo para Wald por los gates abiertos de §132.
- θ_Af(q_X*) permanece no identificado mientras no se demuestre la correspondencia B→g^Af y los supuestos correspondientes.
- s=.80 no está validado; primeras etapas C_dep/A_f/D_f/ΔT_acc separadas.

La precedencia de escenario/políticas está aceptada dentro del alcance DEC-C10-066/067. La jerarquía confirmatoria completa y la identificación causal siguen abiertas.

### 16.81.2. Código ejecutable

No generar ni modificar código ejecutable que materialice DGP, estimandos, políticas, oráculo, Analyzer o Evaluator C10-S hasta contrato de implementación aceptado y autorización explícita. Cualquier pseudocódigo o ejemplo no ejecutable debe rotularse como ilustrativo.

Antes de generar código en el futuro, aplicar el gate del maestro §0.6 y Closure Control Matrix §100: recuperar fuentes/commit exactos, resolver precedencia, trazar cada componente a requisito y fuente versionada, preservar las distinciones causales, separar Generator/Analyzer/Evaluator, ocultar truth al Analyzer y revisar semántica con pruebas adversariales. Una revisión asistida no es independiente.

### 16.81.3. Retirada selectiva de texto histórico

Se retiran de los documentos operativos las formulaciones que inducían regresión cuando ya existe una decisión posterior y explícita. La retirada se limita al texto contradictorio: se conservan valores candidatos, mecanismos D1/D2, escenarios adversariales y referencias útiles. El historial Git mantiene la trazabilidad del contenido anterior. No se borra una sección histórica útil sin comprobar referencias dependientes.

**Límites:** este gate no implica que se haya generado, inspeccionado o validado código. No se ejecutaron validadores, fixtures, parsers, simulaciones ni experimentos. `scientific_execution=false`; `execution_authorized=false`.

## 16.82. Auditoría transversal de precedencia semántica y no-regresión (2026-11-09)

**Estado:** auditoría documental asistida / autoauditoría / no independiente. **Alcance:** los 100 archivos modificados por PR #116 fueron recuperados y revisados para detectar formulaciones históricas o supersedidas que pudieran actuar como especificaciones operativas; además, se contrastaron las secciones causales de referencia §§17/24–30 del protocolo C10-D1 en `research/c10-d1-protocol-draft`.

Se aplicó el criterio de retirada selectiva: eliminar o sustituir texto operativo contradictorio cuando la precedencia está resuelta; conservar IDs, anclas y registros históricos útiles; no borrar definiciones técnicas vigentes ni decisiones aceptadas; no convertir propuestas en decisiones.

**Correcciones realizadas:**
- Auditoría integrada: retirada de la recomendación D1-principal y corrección de `ΔT_acc*`/`ΔE_T`.
- Reconciliación causal: D2 material y autorización basal separados de la intervención histórica AUD-001/002.
- Auditoría de medición: MEAS-01 actualizado a fórmula conceptualmente reconciliada con mappings aún abiertos.
- Reconciliación de población: fórmula histórica de elegibilidad y selección D1/D2 abiertas retiradas como reglas operativas.
- Propuestas AUD-001/002 y auditoría integrada de consistencia: avisos explícitos de no operatividad para D2.
- Este plan §4.3: fórmula focal alineada con maestro §67.3 y crosswalk D2; elegibilidad histórica separada.
- Maestro §59.3: ecuación intermedia anterior sustituida por registro histórico no operativo; §59.4–59.6 alineadas con la autorización basal D2.
- Matriz temporal de predicados §13.4: fórmula intermedia §59.3 declarada supersedida y correspondencia de información técnica alineada con §67.3.
- Crosswalk causal D2: referencias a §59.3 corregidas; la ecuación intermedia queda histórica. La propuesta snapshot/delta queda subordinada al maestro §58.6 y no constituye decisión aceptada.
- Se revisaron también las fichas D2-RES/CAP/C_INFO y MEAS-G1 de §§16.8–16.14: los mappings `R_access*/D_support*` se tratan como históricos y la clasificación actual sigue §67.3 (`RES_f*`, `DEP_f*`, `ID_f*`/`COND_f*`); no se conserva `C_info` autónomo.
- Maestro: §30.1 fórmula antigua de A_f* marcada histórica; §§16.2/16.4 alineadas con DEC-C10-066/067; §§53.5, 58.4/58.6 y 63.7 separan `ΔT_acc*` de `ΔE_T`; §§68.7/69.5 mantienen resuelta la precedencia D2/D1. XSYNC-138-01 queda parcialmente resuelto para D2 y abierto en el mapping general B→g^Af/exclusión; el XSYNC Closure Tracker y S4R-18 reflejan ese alcance.
- Test Contract Register MEAS-03: validez/cobertura epistémica separada de truth estructural.

**Fuentes históricas conservadas:** Draft 001–003 del plan, MRA 001–002, registro de recuperación 165–183, formulaciones históricas de DGP, matriz temporal §30.1 y demás registros con supersesión explícita. No se borró el historial Git ni se modificó `main`.

**Precedencia protegida:** DEC-C10-066/067; `C_auth,base=1` vigente; `C_auth_base` se corresponde con `AUTH_f*`; D2 es provisión técnica focal, no intervención focal de autorización; fórmula candidata `A_f*` según §67.3; `ΔT_acc*` separado de `ΔE_T`; estimandos ITT/LATE/θ_Af/θ_A no intercambiables.

**Límites y siguiente gate:** la revisión cubre los 100 archivos del PR #116, no todo el repositorio. Antes de cualquier generación futura de código debe verificarse la precedencia de todos los documentos y fuentes fuera de ese conjunto y aplicarse maestro §0.6 / Closure Control Matrix §100. No se ejecutaron validadores, generadores, parsers, fixtures, simulaciones ni experimentos. `scientific_execution=false`; `execution_authorized=false`. No Design Freeze.


## 16.83. Cierre de referencias históricas residuales y consistencia de lectura (2026-11-09)

**Estado:** corrección documental persistida en la rama de investigación; autoauditoría asistida, no independiente.

La comprobación focal de referencias cruzadas detectó tres puntos en los que el contenido histórico seguía siendo correcto como registro, pero podía inducir una lectura operativa desactualizada si se consultaba de forma aislada:

1. **Closure Control Matrix §33:** su tabla conservaba «Composición de predicados — OPEN / MATERIAL» del corte anterior. El estado posterior MEAS-G1 **PARTIAL** y la reconciliación conceptual ya estaban en §§34–35; se añadió §101 para fijar expresamente la precedencia y los mappings aún abiertos.
2. **Auditoría cruzada AUD-001/002:** aunque tenía aviso de precedencia, sus conclusiones y siguientes pasos podían leerse como requisito para D2. Se añadió §7 para limitar su alcance a la intervención histórica sobre autorización y al eventual escenario alternativo/adversarial.
3. **Resolución AUD-001/002:** su §10 conservaba una «siguiente operación» de armonización que ya no corresponde a D2. Se añadió §11 para declarar su supersesión limitada y preservar INT-01…08 solo como material reutilizable en un escenario alternativo explícito.

Se preservan los textos originales, las propuestas y la trazabilidad; no se reescriben DEC aceptadas ni se altera el alcance de D2. La fórmula A_f* continúa candidata, MEAS-G1 parcial y el mapping general B→g^Af/exclusión abiertos. No se modifica main, C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS ni claims. No se ejecutan validadores, código, fixtures, parsers, simulaciones o experimentos. scientific_execution=false; execution_authorized=false; sin Design Freeze.



## 16.84. Mapping D2→g de accesibilidad y gate de exclusión (2026-11-09)

**Estado:** análisis documental incorporado; NOT_IDENTIFIED / MAPPING OPEN. No modifica DEC-C10-066/067 ni autoriza implementación.

Se añade como siguiente bloque causal la distinción entre las políticas materiales B_g0^D2/B_g1^D2 y las políticas estocásticas g_j sobre cambios de accesibilidad definidas en C10-D1 §26. Las primeras son reglas implementables de provisión técnica; las segundas son distribuciones objetivo sobre ΔT_acc* condicionadas por historia/contexto y restringidas a transformaciones factibles. La correspondencia debe reconstruirse como distribución inducida por cada B, no suponerse por notación ni por la primera etapa de C_dep*.

El nuevo §14 de C10_S_D2_LATE_F_IV_VALIDITY_AUDIT_DRAFT_001.md especifica la cadena B→W→C_dep*→A_f*/D_f*→ΔT_acc*, los requisitos de historia/soporte/consistencia/versiones, la diferencia entre exclusión focal para D_f* y atribución sobre ΔT_acc* completo, y los siete gates MAP-01…07.

**Consecuencia:** ITT_Z^D2/ψ_policy^D2, LATE_f^D2, θ_Af(q_X*) y θ_A(q) siguen siendo objetos distintos. El mapping no está identificado; las vías colaterales y exclusión no están demostradas. No convertir B_g1/B_g0 en g_1/g_0 ni renombrar el ITT como efecto de accesibilidad.

Siguiente operación documental: completar MAP-01/02 como contrato de correspondencia de intervención y medición, reutilizando DEC-C10-067, D2POL, manifiesto B-M01…15, fichas de invariantes y los predicados vigentes del maestro §67.3. La inspección de evidencias materiales, el cierre de MAP-03…06 y la validación de MAP-07 quedan sujetos a sus propios datos, supuestos y gates. No ejecutar ni implementar; scientific_execution=false; execution_authorized=false.



## 16.85. Contratos MAP-01/MAP-02: intervención material y secuencia de medición (2026-11-09)

**Estado:** contratos de campos y reglas documentales definidos; valores materiales, ventanas y evidencias siguen abiertos. No se modifica DEC-C10-067 ni se declara identificación.

Se desarrollan MAP-01 y MAP-02 en §§14.6–14.7 de la auditoría IV D2:
- MAP-01 separa identidad/versionado de B, actor/rol, artefacto/hash, runtime/canal, programación, intento, recepción, reintentos, fallos, rollback, desviaciones y detección de provisión de fondo. Los valores concretos permanecen NOT SPECIFIED / NOT INVENTORIED.
- MAP-02 define anclas basales pre-Z, eventos de provisión, medición técnica C_dep*, adjudicación independiente de predicados A_f*, contraste D_f*/ΔT_acc* y resultados downstream separados. Se preservan estados 1/0/? y verdad/observación distintas; no se retrodata ni se imputa accesibilidad desde instalación.

La secuencia es un orden causal y de medición propuesto, no un calendario confirmado. Se requieren ventanas, fuentes, instrumentos, sincronización, observadores y tolerancias antes de completar los mappings. La regla candidata de §67.3 no queda aprobada ni congelada.

**Siguiente bloque tras MAP-01/02:** resolver MAP-05 por dominios B-M01…15 y PROV-01…12, con foco en dependencias compartidas, recursos, seguridad, rendimiento, alternativas, oráculo, información y residuos. La cobertura técnica real no existe aún: NO INVENTARIADO no equivale a ausencia. MAP-03/04/06 y la identificación siguen abiertas. No ejecutar, implementar ni parametrizar.



## 16.86. Resultado de auditoría MAP-05: superficies B-M y contratos PROV (2026-11-09)

Se incorpora en el manifiesto de provisión §14 una adjudicación dominio por dominio de B-M01…15 y una tabla de alcance/limitación de PROV-01…12. La clasificación distingue mecanismos focales condicionados, cambios constitutivos, vías colaterales, epistémicas, de medición/oráculo e interferencia/residuo; las clases pueden coexistir.

**Hallazgo principal:** las superficies de mayor prioridad causal son B-M06 (datos/estado), B-M07 (recursos/capacidad), B-M09 (seguridad/riesgo/coste), B-M11 (estado residual), B-M12 (rendimiento), B-M14 (rutas alternativas), además de B-M10/B-M13 por conocimiento y medición. B-M05 requiere mantener separadas credenciales/permisos técnicos y autorización funcional basal. B-M02/B-M03/B-M08/B-M15 exigen grafo transitivo y evaluación de spillover/carryover.

**Resultado:** CLASSIFICATION_DEFINED / MATERIAL_EVIDENCE_NOT_AVAILABLE. La auditoría clasifica amenazas y evidencia falsadora, pero no hay inventario real, snapshots, mediciones ni pruebas funcionales para adjudicar estados 1/0. PROV-01…12 no son PASS por estar definidos. MD-C1/MD-C4 e IV-G4 permanecen OPEN; exclusión no demostrada. El ITT, si resulta identificable, conserva interpretación de efecto de política; no se atribuye exclusivamente a ΔT_acc*.

Siguiente gate: roster de evidencia y grafo por frontera/nodo/arista/consumidor/unidad/versión/ventana, distinguiendo universo conocido y desconocido. No implementar, parametrizar ni ejecutar.



## 16.87. Roster probatorio MAP-05 y reglas de captura (2026-11-09)

Se desarrolla el roster dentro de la plantilla U_G §26, reutilizando los COV-D2-BM01…15 propuestos en §17.4 y los contratos de EVIDENCE_REGISTER / CLAIM_EVIDENCE_LINK / COVERAGE_REGISTER. No se crea una matriz paralela ni se alteran las identidades Nxx/Exx.

El roster separa para cada dominio: afirmaciones a comprobar, destinos U_G cuando el objeto exista, clases de fuentes S1–S8, consecuencia de cobertura insuficiente y reglas de parada. Distingue además identidad/versionado, cambio inducido, dependencias compartidas, alternativas, permisos/autorización, K frente a E_T, recursos/rendimiento, residuos/interferencia e integridad del oráculo.

**Estado:** DOCUMENTARY_READY / NO_SOURCE_INVENTORY / COVERAGE_NONE. Los COV-D2-BMxx siguen siendo IDs lógicos propuestos con denominador UNKNOWN; no se crean scopes ni filas. No se inventan evidence_id, NODE, EDGE, ROUTE, PREDICATE o SNAPSHOT. No hay fuente técnica examinada ni unidad cubierta. MD-C1/MD-C4 e IV-G4 permanecen OPEN; Reach=?, F_alt,0=?, A_f*=?; LATE_f^D2 y θ_Af(q_X*) no identificados.

**Siguiente gate:** revisar la legitimidad del universo y su denominador por frontera P0/P1/P2, unidad, versión, etapa, ruta y clase, resolviendo los mappings C0/UDG aún abiertos antes de solicitar o capturar evidencia. No implementación ni ejecución.



## 16.88. Auditoría de legitimidad del universo y denominadores C0/UDG (2026-11-09)

Se auditó la precedencia entre U_G §§17–18, el protocolo de evidencia §§19–20 y los contratos C0/UDG aceptados documentalmente (DEC-C10-070…076). Se detectó una contradicción interna: §17.1/§17.4 trataba B-M01…15 como valores de COVERAGE_REGISTER.dimension y COV-D2-BMxx como coverage_scope_id; §18.6/C0 limita dimension a C10S_CONFIG_CMP/PAR/REF/RUL/MET y exige la tupla C0 de nueve componentes.

**Corrección persistida en U_G §27:** B-M01…15 son dominios de auditoría transversales; COV-D2-BMxx son etiquetas lógicas de planificación, no scopes físicos ni FK. Se conserva dimension=C10S_CONFIG_*; el dominio B-M se registra en claim_statement/relevance_scope y enlaza a scopes C0 exactos mediante CLAIM_EVIDENCE_LINK. No se amplía enum ni se añade columna.

La auditoría también separa la cuadrícula 7×5 (hasta 35 combinaciones lógicas, no denominador ni obligación de crear filas), los universos UDG EXPLICIT/RULE_DEFINED y los denominadores materiales deduplicados por identidad tipada/registro. Se confirman las precedencias: stage_key ≠ SNAPSHOT.phase ≠ reloj DGP; route_id exacto o C10S_SCOPE_GLOBAL; F/A son familias auxiliares; object_class C10 separado de ug_record_type/semantic_role; PAR es propiedad tipada del CMP owner con parameter_key/manifest_record_id, sin object_record_id U_G propio.

**Bloqueos materiales:** no hay contrato/instancia/snapshot C10-S materializados; mapping NODE raíz↔CMP anchor OPEN; route-specific route_id/route_record_id no fijados; crosswalk físico y unidad de denominador por clase incompletos; C0 no implementado/auditado. El UDG-01/JCS/03/04 está aceptado documentalmente (DEC-C10-073…076), pero no implementado. Estado: DOCUMENTARY_RECONCILIATION_PARTIAL / NO_C0_INSTANCE / NO_SNAPSHOT / DENOMINATOR_UNKNOWN / COVERAGE_NONE.

**Siguiente gate:** cerrar crosswalk de identidad y unidad de denominador CMP/PAR/REF/RUL/MET, reutilizando U_G §18 y el contrato PAR, en coherencia con N01/anchor CMP y N16/oráculo. No repetir diseño UDG ni crear scopes. No captura, C0, schema change, implementación, Design Freeze ni ejecución.



## 16.89. Crosswalk de identidad y unidad de denominador CMP/PAR/REF/RUL/MET (2026-11-09)

Se ha consolidado en U_G §28 la matriz tipada de identidad, proyección U_G, unidad candidata de denominador, condición de inclusión y bloqueo por clase. Se reutilizan U_G §§18–24 y las decisiones vigentes; no se vuelve a diseñar UDG-01…04 ni se reabre PAR.

**Resultado por clase:**
- CMP: unidad candidata = componente contractual distinto elegible por snapshot; CMP→NODE requiere identidad/versión/owner y record exactos. Root LOGICAL_SERVICE_UNIT↔CMP anchor sigue OPEN.
- PAR: propiedad atómica del CMP owner, unidad owner×parameter_key×versión semántica×clave lógica de captura; identidad/supersession DEC-C10-079 y binding DEC-C10-080 aceptados. Sin tabla PAR ni NODE por parámetro.
- REF: unidad candidata = relación tipada, no extremos ni apariciones en rutas; DEC-C10-077 acepta mapping conceptual, pero IDs, endpoints, cardinalidad y mapping M concreto siguen OPEN.
- RUL: unidad candidata = regla/version/scope; PREDICATE solo si es evaluable y operandos/efecto están resueltos. Mapping final OPEN.
- MET: unidad candidata = metadata field tipado por owner/target/tiempo/alcance, solo si es configuración elegible; sin tabla MET única ni taxonomía cerrada.

Se añadieron criterios PASS/FAIL/UNKNOWN/NOT_COMPARABLE por clase en el protocolo §22. El PASS de mapping no equivale a cobertura COMPLETE. Los denominadores continúan UNKNOWN y no se crean scopes/member_refs. Estado: CROSSWALK_TYPED / PAR_IDENTITY_ACCEPTED / CMP_REF_RUL_MET_MAPPING_PARTIAL / NO_INSTANCE / DENOMINATOR_UNKNOWN / COVERAGE_NONE.

**Siguiente gate:** decisión documental focal sobre el mapping del CMP raíz y la cardinalidad de sus componentes, sin inferir identidad por nombre; después, mapping REF/RUL/MET con sus fuentes de contrato. No implementación, captura ni ejecución.



## 16.90. Cierre del gate conceptual NODE raíz ↔ CMP anchor (2026-11-09)

Se ha reconciliado DEC-C10-089 (root NODE LOGICAL_SERVICE_UNIT) con DEC-C10-082 (mapping del CMP contractual a NODE por snapshot) en U_G §28.5 y protocolo §23.

La resolución correcta no es decidir por inferencia si ambos son el mismo objeto. Se fijan criterios documentales diferenciados:
- SAME_ENTITY exige contrato/versión, identidad CMP, definición explícita de unidad lógica, correspondencia 1:1 y mapping exacto al NODE del snapshot.
- DISTINCT_ENTITIES exige identidades/definiciones separadas y NODE distintos; una relación se registra como EDGE solo si está definida y sustentada.
- UNKNOWN se mantiene ante falta de contrato, roster, snapshot o mapping; NOT_COMPARABLE ante versiones sin mapping semántico; FAIL ante contradicción demostrada.

**Resultado reconciliado:** root NODE `LOGICAL_SERVICE_UNIT` conceptualmente aceptado por DEC-C10-089; la identidad contractual `CMP-SERVICE-LOGIC-001`, su clase `SERVICE_LOGIC`, y el `contract_id`/`instance_id` de referencia están aceptados por DEC-C10-069. Lo que permanece UNKNOWN es la relación/mapping material entre ese CMP y el NODE raíz, así como el roster CMP exhaustivo, cardinalidad global, denominador y cobertura. `CMP-SERVICE-LOGIC-001` no es una mera etiqueta candidata: su identidad contractual está aceptada; no está observado su anchor U_G por snapshot.

Este bloque cierra el criterio conceptual, no la adjudicación material. La identidad y versionado de referencia ya constan en `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md` y DEC-C10-069; no hay que inventar otro contrato ni reabrir la decisión. Sigue haciendo falta enumerar el universo contractual completo y resolver el mapping exacto CMP↔NODE por snapshot. No se crean IDs adicionales ni se presume que el roster mínimo sea el roster exhaustivo. No se capturan snapshots, no se inspeccionan sistemas, no se modifica schema ni se implementa IAM. scientific_execution=false; execution_authorized=false.

**Siguiente gate:** localizar y revisar el contrato/artefacto de Opción A y el roster completo de componentes; después resolver N07/REF y las demás clases contra ese universo, preservando las decisiones N07/N14/N15 ya aceptadas. No reabrirlas.



## 16.91. N16 — reconciliación histórica del criterio funcional F*, oráculo y adjudicación (2026-11-09)

### Fuentes existentes y precedencia

N16 se resuelve reutilizando, sin duplicarlos, los siguientes artefactos de esta rama:

- DEC-C10-051: Opción A seleccionada como microdominio de trabajo y F* adoptado como contrato funcional candidato.
- DEC-C10-055: arquitectura de familias FP aceptada; no equivale a aplicabilidad cerrada por instancia.
- DEC-C10-056: cardinalidad base CMP≥1, PAR≥1, RUL≥1; REF=0 solo con IAM ex ante y cobertura exhaustiva; POL ausente por diseño del núcleo mínimo; MET obligatorio.
- DEC-C10-068: contrato funcional sintético de servicio aceptado.
- `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md`: criterio funcional común, ruta completa, C0/G/H y equivalencia funcional.
- `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md`: familias FP-01…FP-08, adjudicación trivalente y no compensatoria.
- `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`: crosswalk propuesto de propiedades atómicas con familias FP; no aprobado como catálogo confirmatorio.
- `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`: aplicabilidad O/C/NA/? y etapas; PAR-SVC-ENABLED/PROFILE y su aplicabilidad por siete stage_key están aceptados documentalmente por DEC-C10-083.
- `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md`: contratos lógicos adversariales, separación de roles y aserciones de no filtración; no son fixtures ni pruebas ejecutadas.

### Tres capas que no deben colapsarse

1. **Criterio funcional F***: contrato común para las rutas focal F1→F2 y alternativa A1→A2, evaluado de extremo a extremo desde una fuente admisible hasta configuración aplicada y verificada en destino. FP-01…FP-07 son dimensiones funcionales no compensatorias; Outcome y Value quedan fuera del criterio.
2. **Oráculo**: implementación independiente, inmutable y versionada del criterio y de sus predicados/mappings/tolerancias. La matriz F* describe la arquitectura del criterio, pero no acredita que exista tal implementación ni que esté validada.
3. **Adjudicación**: evaluación de una instancia/ruta/snapshot exactos contra el oráculo versionado y evidencia asociada. El Generator conserva la truth del DGP; el Analyzer recibe solo sus entradas permitidas y no recibe truth, potenciales ni parámetros generadores; el Evaluator accede a truth y compara después de congelar las salidas del Analyzer. FP-08 es gate de procedencia/reproducibilidad separado, no compensación funcional.

### Estado por elemento

| Elemento | Estado N16 |
|---|---|
| Opción A y F* como contrato de trabajo | ACCEPTED por DEC-C10-051 |
| Familias FP-01…FP-08 | ACCEPTED como arquitectura de familias por DEC-C10-055 |
| Regla no compensatoria | Definida documentalmente en matriz F*; sin predicados/umbrales atómicos cerrados |
| F* común para F1→F2 y A1→A2 | Definido a nivel funcional; equivalencia exige mismo contrato, entrada, destino, C0/G/H e IAM |
| Aplicabilidad O/C/NA/? | Esquema documental; aplicabilidad por instancia aún no sellada en IAM |
| PAR obligatorios y siete stage_key | Aceptación documental DEC-C10-083; sin observaciones materiales |
| C0, G, H | OPEN; deben fijarse ex ante |
| Predicados atómicos y mappings M | OPEN / PARTIAL; reconciliación SM↔FP sigue propuesta |
| Tolerancias, excepciones y reglas de rechazo | OPEN; no inventar umbrales |
| Oráculo independiente y versión/hash | NOT IMPLEMENTED / NOT VALIDATED |
| Adjudicación por unidad/ruta/snapshot | NOT MATERIALIZED; evidencia y cobertura NONE |
| Cegamiento Generator/Analyzer/Evaluator | Requisito documental especificado; no probado |
| FP-08 / procedencia | Gate separado; no validado |
| Outcome / Value | Fuera del oráculo F* |

### Reglas de adjudicación preservadas

- Un FAIL obligatorio confirmado en cualquiera de FP-01…FP-07 no puede compensarse con PASS en otra dimensión.
- UNKNOWN no se convierte en FAIL, FALSE, ABSENT ni NA por falta de observación o cobertura.
- NA exige inaplicabilidad predeclarada y justificada en IAM ex ante; no equivale a dato ausente.
- FP-08 se informa separadamente: una falla probatoria no se oculta como conformidad funcional ni redefine la verdad funcional.
- F* se evalúa por ruta completa. PASS local de F1/F2/A1/A2 no acredita F*.
- No usar Outcome, Value, selección, ejecución ni el brazo Z/B para definir o adjudicar F*.
- La equivalencia F/A no exige mismo mecanismo, pero sí el mismo criterio, universo de entrada y contexto comparable.

### Dictamen y siguiente gate

N16 queda **RECONCILED_DOCUMENTARILY / PARTIAL**: no hace falta crear otro contrato funcional ni otra matriz de propiedades. Sí falta cerrar la atomización confirmatoria, aplicabilidad IAM por instancia, C0/G/H, mappings/tolerancias y el diseño técnico del oráculo; después se requerirá validación adversarial independiente del Analyzer y del Evaluator.

El siguiente gate documental es cruzar el catálogo atómico SM-01…SM-10 con FP-01…FP-07 y el IAM vigente, resolver duplicidades/huecos y fijar requiredness/NA/? por propiedad y etapa sin elevar la propuesta a decisión. Solo entonces podrá definirse un contrato de implementación del oráculo. No generar código, fixtures ni validadores; no ejecutar pruebas, simulaciones ni experimentos. `scientific_execution=false`; `execution_authorized=false`.
