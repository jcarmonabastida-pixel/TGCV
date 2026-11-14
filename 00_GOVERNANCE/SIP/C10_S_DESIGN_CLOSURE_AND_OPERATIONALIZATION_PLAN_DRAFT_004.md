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


## 16.92 — Auditoría focalizada de readiness para especificación implementable C10-S (2026-11-09)

**Tipo:** auditoría documental asistida / autoauditoría / no independiente. **Alcance:** gobierno canónico main (README, bootstrap, canonical state, STATUS, RMA/Matrix pointers y workflows); estado C10-S en research/c10-s-consolidation-draft; maestro Draft 004, plan, Closure Control Matrix §§87/100–109 y contratos especializados funcionales, DGP, causalidad, población, medición, IV, IAM/U_G, provisión, Reach/trayectoria y Test Contract Register. No es auditoría de código ni validación técnica.

### Dictamen ejecutivo

**IMPLEMENTATION_READINESS = NOT_READY / SPECIFICATION_INCOMPLETE.** La arquitectura y varias decisiones de alto nivel están suficientemente desarrolladas para dejar de reabrirlas. El bloqueo no es falta de más arquitectura general: es la ausencia de un contrato integrado, concreto y versionado que permita programar un experimento sintético sin que el implementador tenga que decidir semántica científica por su cuenta.

La auditoría no encuentra motivo para volver a seleccionar Opción A, redefinir D2, recrear el contrato funcional del servicio, rehacer la arquitectura de familias FP o reabrir decisiones DEC-C10-068…092 dentro de sus alcances aceptados. Sí encuentra especificaciones candidatas, crosswalks parciales y contratos lógicos que aún no han sido instanciados, atomizados o aceptados como paquete implementable.

### Base ya reutilizable — no reabrir

- Opción A y servicio lógico sintético: DEC-C10-051/068.
- DGP base, tipos/dominios y complejidad: DEC-C10-052…056.
- D2 primario candidato / D1 secundario y políticas materiales D2: DEC-C10-066/067.
- Identidad contractual CMP, C0/UDG, stage_key, IAM lógico y binding PAR: DEC-C10-069…081.
- Aplicabilidad y equivalencia PAR, predicados F1/A1, destino declarado, aplicación/verificación y secuencia temporal F/A: DEC-C10-083…088.
- Unidad lógica raíz y descomposición conceptual N07/N14/N15: DEC-C10-089…092.
- Separación Generator/Analyzer/Evaluator, cegamiento y pruebas adversariales: contratos existentes del DGP y Test Contract Register.
- F* como criterio común de ruta completa y familias FP-01…FP-08: aceptados a nivel conceptual/arquitectura, no como oráculo operativo.

### Bloqueos agrupados para obtener la especificación implementable

| Paquete | Qué falta cerrar en un único trabajo agrupado | Resultado verificable |
|---|---|---|
| A. Instancia funcional y transformación | Instancia sintética concreta; roster CMP/PAR/REF/RUL/MET dentro del alcance elegido; C_src/C_dst declarado/aplicado; M versionado; C0/G/H; F1/F2/A1/A2; crosswalk SM↔FP↔IAM; predicados, requiredness, tolerancias y oráculo F* | Un único contrato funcional versionado con ejemplos/fixtures lógicos y expected adjudication, sin mappings implícitos |
| B. DGP y diseño causal | Unidad/población y elegibilidad; asignación y soporte; versiones/actor/recepción/reintentos/rollback de B_g^D2; reloj/ventanas; secuencia B→W→C_dep*→A_f*→D_f*/ΔT_acc*; rutas alternativas/interferencia; DGP limpio y adversariales; truth y potenciales | Especificación de escenarios con ecuaciones, parámetros, distribuciones, soporte y truth esperado |
| C. Medición y estimandos | Medición independiente A_f*, D_f*, ΔT_acc*, Reach, trayectoria, Outcome y Value; regla/horizonte/dimensiones de Value; separación ITT_Z^D2, efecto de paquete, LATE_f y θ_Af/θ_A; error, missingness, censura, sensibilidad, cotas, potencia y réplicas | Plan estadístico y de medición preespecificado, con condiciones explícitas de identificación y abstención |
| D. Contrato computacional y de evidencia | Interfaces Generator/Analyzer/Evaluator; firewall efectivo de truth/potenciales; serialización y versionado; oráculo independiente; snapshots/evidencias/cobertura; fixtures adversariales y aserciones; hashes/reproducibilidad y estados de salida | Contrato de software trazable a A–C, con entradas/salidas y criterios de aceptación por módulo |
| E. Gate integrado | Reconciliación final con DEC, matriz y maestro; trazabilidad requisito→fuente→componente→test; clasificación de cada requisito y decisiones pendientes resueltas; aceptación explícita del contrato de implementación | Paquete implementable aprobado; autorización de generación de código separada de autorización de ejecución científica |

### Hallazgos transversales que no deben convertirse en vueltas adicionales

1. **No exigir una inspección de sistema real para poder construir el fixture sintético.** El CMP contractual de referencia ya tiene identidad aceptada; su mapping físico por snapshot solo se necesita en el nivel de evidencia que el diseño vaya a ejercitar. La instancia sintética puede definirse como artefacto del DGP con IDs/versiones propios, sin fingir observaciones reales.
2. **No implementar todo U_G como plataforma genérica antes de C10-S.** Debe implementarse el subconjunto de identidad, snapshots, scopes, evidencia y cobertura que sea necesario para comprobar los requisitos científicos. No se alteran los contratos U_G aceptados; se evita sobredimensionar el software.
3. **No crear otro oráculo, otra matriz ni otro registro.** Reutilizar maestro, Closure Control Matrix, F* matrix, IAM, temporal matrix y Test Contract Register; corregirlos solo cuando haya una discrepancia concreta.
4. **No confundir contratos aceptados con implementación:** DEC-C10-088 cierra la secuencia temporal documental F/A, no mappings, IAM sellado, observaciones ni oráculo.
5. **No confundir clasificación de vías con exclusión demostrada:** MAP-05 mantiene MD-C1/MD-C4/IV-G4 abiertos; las superficies B-M01…15 están clasificadas, no observadas.
6. **No usar los valores históricos N=2.000, R=1.000, s=.80 o probabilidades .20/.80 como confirmatorios sin derivación y aprobación.**
7. **No exigir revisión humana externa para continuar especificando:** la autoauditoría se declara asistida/no independiente. La validación computacional y la revisión semántica del contrato se mantienen separadas.

### Riesgo de integración del PR

PR #116 sigue abierto y Draft, con base research/c10-d1-protocol-draft, head research/c10-s-consolidation-draft, 100 archivos modificados y 1.411 commits por delante de su base según comparación GitHub consultada. No debe tratarse como un PR pequeño de implementación ni promocionarse automáticamente a main. Antes de integración habrá que revisar el alcance/base del PR de forma independiente; esta auditoría no cambia su estado.

### Secuencia de trabajo recomendada — agrupada

1. **Paquete A+B en una sola pasada de especialización:** fijar una única instancia sintética y, sobre ella, las rutas F/A, IAM/F*, DGP temporal, unidad, asignación y escenarios limpio/adversariales. Resolver conjuntamente las dependencias, sin microgates documentales separados.
2. **Paquete C sobre la misma instancia y DGP:** cerrar medición, Value, estimandos, supuestos, sensibilidad y potencia. Si un estimando no puede identificarse, especificar la salida correcta de no-identificación en vez de forzar supuestos.
3. **Paquete D:** traducir A–C a interfaces, esquema de datos, oráculo, fixtures y aserciones; reutilizar el Test Contract Register.
4. **Paquete E:** auditoría de consistencia final y aceptación del contrato de implementación. Solo después se solicitará autorización explícita para generar código; ejecución científica requerirá autorización distinta.

**Estado de autorización:** no se genera ni modifica código ejecutable; no se ejecutan validadores, parsers, fixtures, simulaciones ni experimentos. scientific_execution=false; execution_authorized=false. La auditoría recomienda pasar de la reconciliación documental fragmentada a los paquetes A+B, C, D y E, agrupados y trazables.


## 16.93 — Regla operativa vinculante y cuatro paquetes de trabajo (2026-11-09)

Esta sección concreta la secuencia de §16.92 y evita que la planificación dependa de memoria conversacional.

### Los cuatro paquetes sustantivos

La unidad de seguimiento son **cuatro paquetes**, no cinco. A y B son subámbitos que se resuelven juntos como un solo paquete AB:

1. **AB — Instancia funcional + DGP/diseño causal:** una única instancia sintética versionada y un único DGP coherente. Incluye contrato funcional F/A, roster y mappings necesarios, IAM/F*, C0/G/H, unidad/población, asignación D2, secuencia temporal, rutas alternativas, escenarios y truth/potenciales.
2. **C — Medición, Value y estimandos:** mediciones independientes, regla de Value, jerarquía confirmatoria, estimandos, identificación/no-identificación, error, missingness, sensibilidad, potencia y réplicas, todos referidos a la instancia y DGP del paquete AB.
3. **D — Contrato computacional:** interfaces Generator/Analyzer/Evaluator, separación efectiva de truth/potenciales, esquema y serialización, oráculo independiente, evidencia/snapshots, fixtures y aserciones, versionado y reproducibilidad.
4. **E — Gate final de aceptación:** auditoría integrada requisito→fuente/decisión→componente→test; resolución o aceptación explícita de cada OPEN; clasificación de riesgos residuales; aceptación del contrato implementable.

### Regla de trabajo obligatoria para cada paquete

- Trabajar de forma **agrupada y de extremo a extremo**, resolviendo dependencias en la misma pasada; no abrir microgates o documentos auxiliares por cada subtema.
- Usar como fuentes los documentos y registros ya existentes. El maestro consolidado y los instrumentos oficiales siguen siendo la referencia; actualizar sus secciones/crosswalks cuando corresponda. Crear un artefacto nuevo solo si existe una necesidad funcional que no pueda alojarse razonablemente en los instrumentos actuales.
- Antes de editar, recuperar la fuente vigente y las decisiones aplicables; no inferir contenido de títulos, resúmenes conversacionales ni versiones históricas.
- Para cada requisito, registrar en el instrumento existente: identificador, definición operacional, fuente/DEC, estado, decisión pendiente (si la hay), componente afectado y criterio de aceptación/prueba.
- Reutilizar lo ya aceptado; no reabrir decisiones canónicas dentro de su alcance. Distinguir explícitamente ACCEPTED/DEFINED/OPEN/NOT_REQUIRED/BLOCKED. Una clasificación documental no se elevará a evidencia empírica.
- No introducir parámetros, mappings, supuestos causales, exclusiones o umbrales sin justificación y estado explícito. Si no hay identificación, especificar abstención/no-identificación y sus condiciones.
- Cerrar cada paquete con un único resultado integrado, una lista residual acotada y una comprobación de consistencia contra maestro, decisiones y matrices existentes. No declarar cierre si hay contradicciones o requisitos críticos sin criterio de aceptación.
- No ejecutar código, validadores, parsers, fixtures, simulaciones ni experimentos durante la especificación. No modificar código ejecutable. La generación de código requiere autorización explícita posterior; la ejecución científica requiere autorización separada.

### Condición de salida por paquete

Un paquete solo pasa a DONE cuando: (i) todas sus decisiones críticas están aceptadas o justificadamente declaradas NOT_REQUIRED; (ii) las dependencias con otros paquetes están resueltas o tienen interfaz/estado explícito; (iii) cada requisito tiene fuente y criterio de aceptación; (iv) el instrumento canónico afectado ha sido actualizado y releído; y (v) no quedan contradicciones internas conocidas. En otro caso permanece IN_PROGRESS/BLOCKED con causas concretas.

### Estado y orden

Orden: **AB → C → D → E**. El trabajo inmediato es AB. E es el gate final de aceptación de la especificación, no una autorización automática para programar ni ejecutar. El estado global continúa NOT_READY hasta superar E.


## 16.94 — Ejecución documental del paquete AB: integración de instancia y DGP (2026-11-09)

Se incorpora al maestro §216 una especificación integrada de trabajo que reutiliza DEC-C10-051…092 y los contratos funcionales, IAM, F*, causal, población, DGP temporal, provisión B y Reach ya existentes. No crea un artefacto paralelo.

**Resultado:** BASE RECONCILED / AB IN_PROGRESS. Se consolida en una única lectura la instancia aceptada (C10S-SVC-REQUEST-PROCESSOR v1.0.0 / instance C10S-SVC-REQUEST-PROCESSOR-001 rev.1 / CMP-SERVICE-LOGIC-001), núcleo ENABLED/PROFILE/RUL, MET obligatorio, REF=0 solo con cobertura sintética exhaustiva, rutas F1/F2 y A1/A2, provisión B separada de transformación/aplicación, fórmula candidata A_f* §67.3, separación DEP_f*/C_dep*/App_f*/F_alt/Reach, poblaciones P*_τ2/P*_F, q_X* basal, UE/UA propuesta, reloj t−1…t9/t+1, D2 primario candidato/D1 secundario y escenarios R0–R3/adversariales.

**Bloqueos AB-01…AB-09:** roster/cobertura por snapshot; C_src/C_dst/M concretos; cards/identidades de transformaciones y adaptador; mappings materiales ID/REL/COND/AUTH/RES/DEP/BLOCK; F*/C0/G/H/tolerancias; mecanismo operativo D2; distribución conjunta técnica; elegibilidad/q_X*/unidad/soporte/interferencia; universo de alternativas y truth/observed.

**Regla de continuidad:** la siguiente pasada debe especializar conjuntamente AB-01…AB-05 y AB-06…AB-09 sobre la misma instancia, no abrir auditorías separadas ni repetir decisiones aceptadas. No fijar por memoria ni conveniencia valores de s, cumplimiento, fondo/crossover, N, probabilidades ni tolerancias. Los asuntos estadísticos de N/potencia/Value se transfieren a C, conservando en AB las variables generadoras e interfaces necesarias.

No se declara AB DONE, Design Freeze ni readiness de implementación. No se ejecuta código/validator/parser/fixture/simulación ni experimento. scientific_execution=false; execution_authorized=false.


## 16.95 — Paquete AB: propuesta material para instancia, mapping y rutas (2026-11-09)

Se añade al maestro §217 una propuesta única y acotada para especializar la instancia ya aceptada: roster mínimo CMP/PAR/REF/RUL/MET; valores semánticos de referencia y adversariales; contratos sintéticos C_src/C_dst y mapping ENUM; rutas F1/F2 y A1/A2; perfil F* por FP-01…FP-07 con FP-08 separado; frontera candidata B/ARCH-B1.

No se acepta automáticamente: REF como clase separada frente a operand bindings del AST; namespaces/códigos físicos sintéticos; alcance G; perfil FP-05; y parámetros/ventana H. Se presentan como propuesta explícita, no como DEC ni como implementación.

La continuidad será una única decisión de paquete sobre la especialización semántica. Después se cerrarán H, mecanismo probabilístico D2 y elegibilidad/soporte como subbloques coordinados del mismo AB. No abrir otra auditoría general ni volver a discutir decisiones ya aceptadas. No código/fixtures/simulación/ejecución; autorizaciones permanecen false.


## 16.96 — DEC-C10-093: aceptación de la base de especialización AB

Se registra la aceptación expresa del usuario de §217 como base de diseño de trabajo, formalizada en DEC-C10-093. Se conservan sin reabrir las elecciones conceptuales cubiertas y se mantienen OPEN las reservas enumeradas en §3 de la decisión: REF/AST, namespaces/serialización, roster IAM/cobertura, FP-05, G/C0/H, mecanismo/distribución D2, aislamiento, población/soporte/interferencia y oráculo.

La siguiente operación es completar la especificación material integrada AB-01…AB-09 sobre esta base; no repetir auditorías generales ni reabrir el núcleo funcional ya aceptado. AB permanece IN_PROGRESS hasta que cada bloqueo tenga definición, trazabilidad y criterio de aceptación. No Design Freeze ni autorización de implementación/ejecución.


## 16.97 — AB integrado: contratos, criterios y gates residuales

Se incorpora el maestro §219 como especificación integrada propuesta de AB-01…AB-09. La unidad de trabajo es el mismo servicio DEC-C10-069, con inventario CMP/PAR/RUL y dos operand bindings representados una sola vez (REF o AST), namespaces sintéticos versionados, mapping total/injectivo, fichas F1/F2 y A1/A2, F* común no compensatorio, IAM por rol/acción/objeto/etapa, C0 pre-Z, G como unidad lógica completa y H común preespecificado.

La integración fija además el event log D2 (asignación, programación, recepción, cumplimiento, intento, instalación, dependencia conjunta, accesibilidad, aplicación y ΔT_acc); exige distribución conjunta de instalación/integridad/compatibilidad/operatividad sin independencia asumida; separa truth/observed y Generator/Analyzer/Evaluator; define población elegible pre-Z, q_X*, soporte, unidad/interferencia y R0–R3; y especifica las interfaces causales que pasan a C sin equiparar ITT, efecto de paquete, LATE_f, θ_Af o θ_A.

**Resultado documental:** AB-01…AB-09 tienen contratos y criterios de aceptación integrados. **AB no está DONE ni implementable**: faltan elecciones/observaciones no deducibles (REF/AST físico y serialización; valor/ancla de H; manifiesto y evidencia MD-C1/MD-C4; distribución conjunta y parámetros D2; roster/cobertura y población/q_X*/soporte; unidad/interferencia material; validación del oráculo y adjudicación). No se asignan defaults ni tasas inventadas. Estas reservas se mantienen como gates de decisión/evidencia dentro del paquete, no como auditorías conceptuales nuevas.

No se autoriza Design Freeze, código, parser, validator, fixture ejecutable, simulación ni experimento. scientific_execution=false; execution_authorized=false. El paquete C podrá preparar su estructura sin tratar como congelados los inputs AB todavía abiertos.

## 16.98. DEC-C10-094 — resoluciones materiales integradas de AB (2026-11-09)

Se acepta como base de diseño de trabajo el paquete de resoluciones DEC-C10-094: inventario lógico y operand bindings únicos; encoding REF/AST físico pendiente de gramática; namespaces/mapping semántico; IAM exhaustivo por dimensión; FP-05 endurecido; G/C0/H; D2 event log y distribución conjunta de C_dep*; población pre-Z, q_X* y soporte; unidad/interferencia; truth/observed y oráculo independiente. No se reabren las decisiones conceptuales ya aceptadas.

La aceptación cierra elecciones documentales, no evidencia. Permanecen gates materiales: serialización/encoding físico; H* y ancla definitiva; MD-C1/MD-C4; parámetros D2 y sensibilidad; algoritmo/roster/q_X*/soporte; cluster/interferencia real; validación y adjudicación del oráculo. AB sigue IN_PROGRESS, no DONE, no Design Freeze y no implementable. Paquete C puede preparar estimandos y medición, pero no asumir cerrados los inputs AB que condicionan identificación. `scientific_execution=false`; `execution_authorized=false`.


## 16.99 — Interfaz contractual AB→C (2026-11-09)

Se incorpora el maestro §221 como contrato de transferencia. C recibe objetos causales no intercambiables: ITT_Z^D2; primeras etapas FS_Cdep/FS_Af/FS_Df; efecto de paquete/política; ψ_B para versiones recibidas; LATE_f^D2; θ_Af(q_X*); θ_A(q); y estimandos propios de mediación/residual. Se prohíbe sustituir unos por otros, condicionar por mediadores post-Z al estimar ITT o calcular efectos residuales mediante restas de estimandos no armonizados.

AB debe entregar a C entradas versionadas de unidad/población pre-Z, asignación y eventos B, C0/G/H, distribución conjunta C_dep*, predicados y ΔT_acc*, vías colaterales, Outcome/Value, truth/observed y soporte. C debe devolver diagnósticos de asignación/seguimiento/interferencia, ITT por Outcome y Value, primeras etapas separadas, dictamen IV por supuesto, evaluación B→g^Af, recuperación de truth DGP y abstención correcta cuando no hay identificación.

La interfaz permite avanzar documentalmente en diccionario, medición y análisis, pero no declarar identificados LATE_f, θ_Af o θ_A ni cerrar mediación/residual. Se mantienen los gates AB y los requisitos de C sobre Value, población, soporte, interferencia, identificación, sensibilidad, potencia y N. Fuente: maestro §221; jerarquía previa C10-D1/S4-R §18 y auditoría IV mantienen precedencia.

Estado: CONTRACT_DEFINED / MATERIAL INPUTS OPEN / IDENTIFICATION NOT ESTABLISHED. No Design Freeze ni autorización de implementación/ejecución; scientific_execution=false; execution_authorized=false.


## 16.100 — Paquete C: especificación integrada de identificación, Value y atribución (2026-11-09)

Se incorpora el maestro §222 como arquitectura de análisis y medición propuesta, reutilizando los contratos ya existentes P177-01…12, P178-SIM-01…10, P179-01…08, P182-01…12 y P183-01…13. No se crea una batería paralela.

**Decisiones de diseño recomendadas para C:** (i) ITT_Z^D2 como estimando primario de asignación, separado de efecto de política recibida, primeras etapas, LATE_f, θ_Af y θ_A; (ii) Outcome y Value como constructos independientes; (iii) Value vectorial como salida primaria durante identificación, sin seleccionar aún dimensiones/pesos; (iv) medición independiente y temporal de A_f*, ΔT_acc*, Reach, trayectoria, Outcome y Value; (v) análisis por gates, con abstención explícita cuando identificación falle; (vi) evaluación del Analyzer frente a truth oculta por Evaluator separado; (vii) efectos interventional indirect/direct sobre ΔT_acc* como candidato de mediación, no como estimando ya aprobado o identificado.

**Condiciones pendientes:** dimensiones/escala/regla Value; intervención y distribución de referencia del mediador ΔT_acc*; confusión postratamiento y modelo secuencial; población/q_X*/soporte/unidad/interferencia; mapping B→g^Af y exclusión; medición y cegamiento; parámetros de sensibilidad, MDE, potencia, precisión, N y R; umbrales del Analyzer. Los valores históricos N=2.000, R=1.000, s=.80 y .20/.80 no se elevan a parámetros confirmatorios.

**Dictamen:** paquete C DOCUMENTED DESIGN PROPOSAL / NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. La identificación de ΔT_acc→Value sigue abierta. Sin código, simulación ni ejecución; scientific_execution=false; execution_authorized=false.


## 16.101 — Especialización operativa del paquete C (2026-11-09)

El maestro §223 aclara que θ_A(q) mantiene la primacía como pregunta científica C10, mientras que ITT_Z^D2 es el estimando primario de asignación únicamente dentro de S4-R. Así se evita que el estimando identificable del diseño sustituya a la pregunta científica de atribución a accesibilidad.

Se propone un registro versionado por estimando con intervención/contraste, población pre-Z, unidad de asignación/análisis/interferencia, régimen C0/G/H, tratamiento/mediador, resultado específico, horizonte, escala, supuestos, missingness/medición, estimador/inferencia, estado y provenance. Cada dimensión Value tendrá ficha independiente de beneficiario/contexto, constructo, indicador/fuente/unidad, cálculo/escala/dirección, baseline/ventana, validez/error, ausencia y trade-offs. Outcome se registra aparte. No se seleccionan dimensiones, pesos, índice, MDE o parámetros estadísticos sin justificación.

Resoluciones propuestas C-01…C-07: jerarquía científica/diseño; Value vectorial; no selección post hoc de dimensiones/pesos; registro de estimandos; ITT sin ajuste post-Z; dictamen por estimando/dimensión y abstención correcta; firewall Generator/Analyzer/Evaluator. Todas requieren aceptación; ninguna está congelada.

**Estado:** paquete C continúa DOCUMENTED DESIGN PROPOSAL / NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. Gates materiales y estadísticos siguen OPEN; sin ejecución.


## 16.102 — Paquete C: contrato operativo de Outcome y Value (2026-11-09)

El maestro §224 establece fichas versionadas independientes para cada indicador Outcome y cada dimensión Value, separando constructo, evidencia y adjudicación. O describe resultados operativos; V expresa valoración contextual. A_f*, ΔT_acc*, Reach, trayectoria y ejecución permanecen separados. Se fijan campos obligatorios para fuentes, unidades/escalas, cálculo, baseline, ventana/ancla, validez, error, acuerdo, ausencia/censura, cegamiento, trade-offs y provenance.

Se propone firewall Generator/truth → Evaluator y Analyzer/observed sin truth; adjudicación independiente de A/ΔT_acc sin consultar O/V. Los estados OBSERVED_VALID, OBSERVED_INVALID, NOT_OBSERVED, NOT_APPLICABLE, CENSORED, DISPUTED y UNKNOWN no se colapsan en cero ni entre sí.

No se eligen indicadores, dimensiones confirmatorias, escalas, ventanas, ponderaciones, tolerancias ni parámetros estadísticos por defecto. El cierre exige fichas completas y preespecificación de dimensiones/multiplicidad, fuentes, ventanas, validez/error/ausencia y auditoría del firewall.

**Estado:** contrato de medición propuesto; indicadores y dimensiones aún no operacionalizados; paquete C no aprobado, no congelado y no implementable. Sin ejecución.


## 16.103 — Paquete C: identificación, sensibilidad y evaluación estadística (2026-11-09)

El maestro §225 integra la estrategia de identificación por estimando y resultado. ITT_Z^D2 identifica, si se cumplen sus condiciones, el efecto de asignación a la política; no identifica por sí solo recepción, C_dep*, A_f*, D_f*, ΔT_acc* ni Value mediado por accesibilidad. Las primeras etapas FS_Cdep/FS_Af/FS_Df se reportan separadas. ψ_policy conserva vías colaterales; ψ_B requiere estrategia propia ante incumplimiento. LATE_f permanece NO IDENTIFICADO / NO LISTO PARA WALD según auditoría IV. θ_Af(q_X*) requiere mapping B→g^Af y soporte; θ_A(q) sigue siendo la pregunta científica general no identificada por D2 focal.

Se añade contrato de mediación que exige DAG/temporalidad, confusores basales y postratamiento, mediadores multicomponente, rutas colaterales e interacciones. ITT no se ajusta por variables post-Z. Para mediación se requieren estimandos/intervenciones propios y métodos compatibles con confusión inducida por tratamiento; no se usa la resta de estimandos ni efectos naturales por defecto.

Se integran población pre-Z, q_X*, positividad/overlap, soporte/transporte, unidad de asignación/análisis/exposición e interferencia; missingness, censura, selección y error diferencial; análisis de sensibilidad, bounds y tipping points; métricas de recuperación y falsa identificación; potencia, precisión, N y réplicas Monte Carlo determinados mediante justificación y error Monte Carlo. Ningún valor numérico se fija sin entradas materiales y preespecificación.

Estados de salida: IDENTIFIED/RECOVERED, IDENTIFIED/NOT RECOVERED, PARTIALLY_IDENTIFIED, NOT_IDENTIFIED—CORRECTLY RECOGNIZED, FALSE_IDENTIFICATION, INDETERMINATE y NOT_APPLICABLE. Una recuperación sintética valida solo el Analyzer bajo el DGP cubierto; no prueba causalidad empírica ΔT_acc→Value.

**Gates abiertos:** estimandos/resultados concretos; DAG y régimen de mediación; población/soporte/interferencia; missingness; parámetros DGP; fichas O/V; sensibilidad/bounds; métricas/tolerancias; multiplicidad/potencia/N/réplicas; firewall y adjudicación; crosswalk contractual completo.

**Estado:** paquete C DOCUMENTED DESIGN PROPOSAL / NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. No implementación ni ejecución; scientific_execution=false; execution_authorized=false.


## 16.104 — Auditoría de crosswalk: mediación causal y P177–P183 (2026-11-10)

La verificación de los criterios originales en Test Contract Register §55 muestra que la referencia P177-05…08 para mediación/confusión postratamiento no es correcta: esos IDs cubren O/V, ajuste basal, ATE/ATT y heterogeneidad. Se corrige la trazabilidad sin modificar sus definiciones.

La mediación queda vinculada parcialmente a §225.3, P177-06 (no ajuste post-Z), P177-12 (política frente a atribución focal), P182-01/02/06/07 (validez/adjudicación de A) y P183-08 (ausencia de A y efecto sobre identificación). Ninguno de esos contratos, individual o conjuntamente, sustituye una especificación completa de identificación mediacional.

**Gate C-MED — OPEN:** faltan estimando e intervención mediadora versionados; DAG y orden temporal por ola; conjunto de confusores basales e inducidos por tratamiento; soporte/positividad secuencial; tratamiento de múltiples mediadores, interacción y retroalimentación; método principal y alternativa; sensibilidad/bounds; y criterio de recuperación/abstención del Analyzer por DGP. No se elige por defecto un efecto natural ni una descomposición residual.

La corrección no añade pruebas ejecutadas ni cambia el estado de los contratos fuente. Paquete C sigue DOCUMENTED DESIGN PROPOSAL / NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. Sin implementación ni ejecución.


## 16.105 — Auditoría ampliada de trazabilidad P177–P183 (2026-11-10)

Se amplía la corrección del crosswalk: P177-02 es el contrato de primera etapa; P177-03/04 cubren Wald/LATE e instrumento débil. Para dimensionamiento, P178-SIM-02/03/04/05 cubren N, clústeres, réplicas y error Monte Carlo; SIM-01 y SIM-09 cubren potencia/métricas y SIM-10 parámetros/tolerancias ex ante. Para sensibilidad/cotas, P183-09/10/11/12 distinguen censura, sensibilidad, bounds y dictamen; P179-06/08 solo cubren trade-offs y agregación de Value.

P177-10/12, P182-11 y P183-11/12 aportan cobertura parcial a recuperación, firewall y clasificación. Las tasas de falsa identificación/falsa atribución y la evaluación de abstención correcta propuestas en §225.7 todavía requieren criterios explícitos de adjudicación y tolerancias; no se declaran cubiertas por mera proximidad temática.

**Estado:** crosswalk documental corregido; gates de Analyzer y mediación permanecen OPEN. No se alteran contratos fuente ni se declara implementación/ejecución. Paquete C sigue NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE.


## 16.106 — Especialización candidata de mediación y evaluación del Analyzer (2026-11-10)

El maestro §228 propone completar dos gates sin duplicar automáticamente P177/P182/P183:

- **C-MED:** estimandos interventional indirect/direct separados del ITT y del efecto de política; intervención estocástica sobre la distribución conjunta de ΔT_acc*; DAG longitudinal; confusión mediador–resultado inducida por Z/B; soporte secuencial; rutas colaterales; sensibilidad/bounds y regla de no identificación.
- **C-ANALYZER:** recuperación solo en DGP identificables; bounds en identificación parcial; falsas declaraciones de identificación; falsa atribución focal de efectos de paquete; abstención correcta y falsa abstención; firewall Generator/Analyzer/Evaluator y adjudicación por estimando×dimensión×DGP.

Se trata de especialización candidata de P177-06/10/12, P182-01/02/06/07/11 y P183-08/10/11/12. La cobertura actual es parcial; las tolerancias y los denominadores no están fijados. No se selecciona un método mediacional ni un DAG sin microdominio y entradas AB aceptadas.

**Estado:** C-MED OPEN; C-ANALYZER OPEN; paquete C NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. Sin ejecución.


## 16.107 — Reconciliación causal de C-MED y contrato de evaluación del Analyzer (2026-11-10)

El maestro §229 corrige la ambigüedad de §228: θ_A(q) es el contraste científico entre políticas factibles de accesibilidad bajo q común; la mediación del efecto de asignar/proveer B^D2 es una pregunta mecanística secundaria y no se obtiene del ITT ni de restas entre estimandos incompatibles.

Se adopta como referencia de medición de ΔT_acc la representación analítica de C10-D1 §27.1 (A⁺, A⁻, A^reconf, ΔR, ΔC), sin elevarla a nueva ontología del Core. La tupla del contrato DGP requiere crosswalk explícito antes del freeze y separación de ΔE_T.

Se concreta el reloj t−1…t9 y se distingue confusión mediador–Value inducida por B antes de t3 de mecanismos downstream posteriores a ΔT_acc. No ajustar mecánicamente por estos últimos para el efecto total. Para mediación secundaria se requiere estimando interventional y método longitudinal compatibles con el DAG; no efecto natural ni regresión convencional por defecto.

El Analyzer debe evaluarse por estimando×dimensión Value×DGP×soporte, con truth sellada, bounds cuando proceda, falsa identificación/atribución y abstención correcta/falsa. Se especifican denominadores conceptuales, manteniendo thresholds, tolerancias, multiplicidad, N y réplicas OPEN.

**Estado:** propuesta integrada; MED-01…06 y AN-01…04 no están cerrados; paquete C NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. Sin ejecución.


## 16.108 — Corrección de precedencia ΔT_acc DGP/C10-D1

Se corrige la lectura de §229.2: la tupla DGP vigente es (ΔU*, ΔR*, ΔC*, ΔX*) según DGP §30 y la reconciliación de snapshots; ΔValidity_e pertenece a ΔE_T, no a ΔT_acc*. La expresión anterior de DGP §3.3 queda supersedida por §30.

El crosswalk con C10-D1 §27.1 debe mapear ΔU* a altas/bajas/reconfiguraciones, ΔR* a relaciones y ΔC* a condiciones/configuraciones. ΔX* requiere clasificación campo a campo; no se asigna automáticamente a ΔC ni al régimen q. MED-02 permanece OPEN hasta resolverlo. Sin freeze ni ejecución.


## 16.109 — Regla de tipado de ΔX* y crosswalk C10-D1

El maestro §231 fija la clasificación por función semántica U/R/C/X/E. ΔX* representa el contexto efectivo constitutivo que altera accesibilidad, no una transformación ni una regla de admisibilidad. C10-D1 §27.1 no tiene una coordenada autónoma para ΔX: se conserva como contexto causal del DGP y sus consecuencias se reflejan, sin doble conteo, en A⁺/A⁻/A^reconf/ΔR/ΔC. Si el campo es un predicado se reclasifica en C; si es historia no constitutiva puede pertenecer a q bajo factibilidad; si no cambia accesibilidad queda fuera del mediador; si no se puede resolver queda UNKNOWN/?.

Se define un registro de crosswalk campo a campo y gates MED-02a…d. La regla está definida/propuesta, pero el roster concreto del microdominio y la adjudicación de campos siguen OPEN. No se cierra MED-02 ni se autoriza ejecución.


## 16.110 — Roster documental de superficies y campos del microdominio

El maestro §232 consolida el roster parcial derivado de DEC-C10-069, la matriz CMP/PAR/REF/RUL/MET, las fichas F1/F2/A1/A2, B-M01…15, PROV-01…12 y el contrato de snapshots. Distingue U*/R*/C*/X*/E_T por función semántica. No asigna valores ni truth.

La identidad lógica de referencia es C10S-SVC-REQUEST-PROCESSOR v1.0.0 / instancia -001 rev1 / CMP-SERVICE-LOGIC-001 / SERVICE_LOGIC / RUL-SVC-ENABLE-PROFILE-01. ENABLED y PROFILE son PAR nucleares; RETRY-COUNT es candidato no confirmatorio; REF no se presume vacío. Los contextos de runtime/host, recursos, permisos, red, seguridad, estado persistente, rendimiento y alternativas se clasifican campo a campo, sin asumir que toda superficie B-M sea X*.

MED-02c3/c4/d siguen OPEN: faltan valores/campos efectivos por unidad/versión, matching temporal y adjudicación de UNKNOWN. No se declara crosswalk total ni autorización de ejecución.


## 16.111 — DAG causal específico Opción A/D2 y vías colaterales

El maestro §233 integra el DAG temporal con el roster MED-02c y la precedencia DEC-C10-066/067. Se distingue la vía focal Z→B_D2→W_programmed→W_attempt→S_install→C_dep*→predicados de accesibilidad/T_acc→Reach/Π_H→K/consideración/selección→ejecución→Outcome→Value de las vías colaterales B→U/R/C/X, recursos/capacidad, permisos/seguridad, dependencias compartidas/A1-A2, coste/latencia/calidad, información/incentivos, observación y spillovers.

A_f,1* es predicado/proyección focal dentro de la adjudicación de T_acc; D_f* es indicador derivado de apertura basal→post. Ninguno se trata como mediador adicional en serie con ΔT_acc*. El mediador secundario candidato es la distribución conjunta factible de ΔT_acc*. ITT_Z(D2) conserva interpretación de efecto de política/paquete si existen vías colaterales. La identificación de θ_A(q) requiere mapping B→g, régimen común, soporte y exclusión demostrados; no se presume por aleatorización.

El DAG es candidato documental, no congelado. El inventario B-M01…15 sigue sin valores efectivos; MED-02c3/c4/d, unidad/interferencia, población, q*, F*, Value, DGP y estrategia de identificación permanecen abiertos. No se autoriza ejecución.

## 16.112 — Ledger integrado de inputs residuales AB (2026-11-10)

El ledger `C10_S_AB_RESIDUAL_INPUT_CLOSURE_LEDGER_DRAFT_001.md` consolida AB-01…AB-09 tras DEC-C10-093/094. Distingue diseño documental resuelto, input material abierto, gate de evidencia y handoff a C. No crea decisiones ni declara cierre por integración narrativa.

Quedan ordenados 11 inputs: (AB-M01) encoding REF/AST; (M02) schema físico y canonicalización de C_src/C_dst/M; (M03) TID/SID/RID y cards concretas; (M04) roster de predicados y fuentes/captura; (M05) H* común; (M06) evidencia MD-C1/MD-C4; (M07) evento/probabilidades D2 y distribución conjunta C_dep; (M08) elegibilidad, q_X*, soporte y estratos; (M09) unidades y exposición/interferencia; (M10) oráculo/cegamiento/adjudicación; (M11) truth tables R0–R3 y proceso de observación/missingness.

La canonicalización JCS aceptada por DEC-C10-074 se limita al envelope UDG-01; no se extrapola al payload de configuración. Los dos operand bindings se representan una sola vez; no se cuenta como REF de configuración una referencia UDG, FK U_G o EDGE.

**Estado:** AB IN_PROGRESS; ningún gate material se cierra por esta actualización. El próximo trabajo documental se concentra en M01/M02, M03 y M04; los valores H*, D2, q_X* y topología requieren decisión o evidencia explícita. Sin implementación ni ejecución.

## 16.113 — Reconciliación documental AB-M01/M02 (2026-11-10)

La revisión de DEC-C10-054/068/069/074/076/077/078/093/094, el contrato abstracto, catálogo, matriz M, gramática y plantilla U_G concluye:

- AB-01: roster lógico y dos operand bindings semánticos DESIGN RESOLVED; encoding físico REF/AST, IAM instanciado y cobertura OPEN. UDG refs/FKs/EDGE no son objetos REF de configuración por defecto.
- AB-02: BOOL/ENUM y mapping semántico aceptados; namespaces, schema/payload físico, serialización y canonicalización de C_src/C_dst/M OPEN. JCS solo cubre envelope UDG-01; no se extrapola. DEFAULT no forma parte del baseline confirmatorio ENABLED/PROFILE.

No se cambia ninguna decisión aceptada ni se declara cierre material. Véase ledger AB §8. La siguiente pasada documental puede abordar AB-M03/M04; los datos/valores de H*, D2, q_X* y topología no se rellenan por inferencia.

## 16.114 — Reconciliación AB-M03/M04 y AB-TIME-01 (2026-11-10)

Las cards existentes no deben recrearse: F1/τ2 tiene una función candidata de conversión; F2 es aplicación/verificación; A1 exportación; A2 importación/aplicación, con descomposición conceptual posterior. Sin embargo, F2/A1/A2 no tienen mecanismo material definido y ninguna de las cuatro tiene TID/SID/RID completos. DEC-C10-090/091/092 no prueban implementación ni identidad transformacional.

El crosswalk A_f* y la regla trivalente resuelven parte de la semántica AB-04, pero B-M01…15 no están pobladas y U_G no contiene snapshots C10-S reales. La captura por campo, cobertura y adjudicación sigue OPEN/NONE.

Se detecta discrepancia de índices: DGP temporal usa baseline t−1, Z t0, política t1; Path Predicate Matrix usa baseline t0 y asignación/oferta t1. Se conserva el orden por nombre de evento, pero no se equiparan índices hasta reconciliación explícita.

Véase ledger AB §§9.1–9.4. No se inventan identidades, mecanismos, estados ni timestamps.

## 16.115 — AB-M05…M11 y discrepancia H_path/H_time (2026-11-10)

La reconciliación final de inputs AB confirma: C0/G/F* tienen estructura aceptada, pero H* temporal exige ancla, valor y unidad todavía OPEN. La Path Predicate Matrix contiene H=3 como profundidad máxima candidata del grafo, no como horizonte temporal; se registra AB-TIME-02 y se prohíbe reutilizar ese 3 como duración/ventana.

La programación D2 está definida por política; intento efectivo, recepción/cumplimiento, provisión de fondo, joint C_dep, fallos y rollback no. P*_τ2/P*_F están diferenciadas; elegibilidad, q_X*, soporte, pesos/estratos y cluster/interferencia no están materializados. Oráculo, cegamiento, adjudicación, R0–R3 truth tables y observación/missingness permanecen sin validación/evidencia.

Véase ledger AB §10. Ningún valor se inventa ni se transfiere a C como si estuviera cerrado.

## 16.116 — Propuesta integrada de cierre AB para aceptación (2026-11-10)

Se incorpora como referencia el ledger AB §11. No se abren nueve microgates: la resolución se realizará como una única instancia sintética y DGP autocontenidos.

Recomendación: resolver REF/AST y payload schema contra los contratos; completar cards sintéticas F1/F2/A1/A2; reutilizar crosswalk A_f*/matriz temporal/trivalencia; separar H_path/H_time y aplazar H_time hasta Outcome/Value; mantener eventos D2 separados; parametrizar C_dep como distribución conjunta con sensibilidad justificada; definir población/q_X* desde C0 pre-Z y soporte explícito; reutilizar R0–R3 y añadir adversariales de interferencia, vías colaterales y medición.

Las decisiones que requieren aceptación del usuario son AB-03-SYN, AB-05-H, AB-08-POP, AB-09-INT y AB-06/07-PARAM. No se acepta unilateralmente ningún valor, población, topología ni parámetro. R0 puede contener invariancias estipuladas para el DGP, nunca presentadas como evidencia observada. MD-C1/MD-C4 y cobertura real permanecen probatorios.

AB sigue IN_PROGRESS / NOT DESIGN FROZEN / NOT IMPLEMENTABLE. Véase ledger AB §11 para definición, límites y criterio de salida.

## 16.117 — Aceptación de la propuesta integrada AB (2026-11-10)

El usuario acepta el ledger AB §11 como base de trabajo, con valores numéricos y horizonte temporal no justificado expresamente abiertos. Quedan aceptadas como reglas de diseño las cuatro cards sintéticas F1/F2/A1/A2 sin mecanismo real; separación H_path/H_time (H_time sigue OPEN); elegibilidad C0 pre-Z, P*_τ2/P*_F separados y q_X* sujeto a soporte; no interferencia solo estipulada en R0 con adversariales interferentes; y parametrización D2/C_dep por justificación y sensibilidad sin aprobar valores.

REF/AST y schema/canonicalización se resuelven técnicamente contra contratos. MD-C1/MD-C4, cobertura y evidencia material permanecen OPEN. No hay Design Freeze, implementación ni ejecución. AB sigue IN_PROGRESS.

## 16.118 — AB-M01: binding AST tipado a PAR (2026-11-10)

Queda resuelta la alternativa semántica REF vs AST: los dos operandos ENABLED y PROFILE son bindings tipados de hojas/posiciones del AST RUL a PAR-SVC-ENABLED/BOOL y PAR-SVC-PROFILE/ENUM. No generan objetos REF de configuración. Se prohíbe el doble registro AST+REF del mismo binding. Un REF solo existiría para una relación/dependencia constitutiva independiente.

AB-M01 pasa a DESIGN RESOLVED en semántica; encoding/schema/serialización física, namespace/versionado y constraints permanecen OPEN. No extrapolar JCS UDG-01. Véase ledger AB §13.

## 16.119 — AB-03/04: cards sintéticas y crosswalk field-level (2026-11-10)

Se completa la especificación funcional abstracta de F1/F2/A1/A2 con TID/SID sintéticos versionados y sin RID/EID. F1 convierte S0→S2; F2 aplica/verifica S2→SF; A1 exporta S0→S1; A2 importa/aplica/verifica S1→SF. Se vinculan a la instancia de servicio y a CMP/PAR/RUL aceptados, sin fijar valores, producto, formato ni mecanismo.

El crosswalk semántico define field_id por identidad, composición, dependencia, condiciones, autorización, recursos, bloqueo, contexto X*, estados, mapping, snapshots, evidencia, cobertura y adjudicación; clasifica cada campo en U*/R*/C*/X*/E_T y lo enlaza con predicados y etapas. No es schema físico. Se mantiene la separación truth/observed y la regla 1/0/? de la matriz temporal.

AB-03 y AB-04 pasan a DESIGN SPECIFIED AT ABSTRACT/SEMANTIC LEVEL, no DONE. Permanecen abiertos mapping concreto, requiredness FP, tolerancias, C0, recursos, C_dep, H_time, universo alternativo, cobertura material, MD-C1/MD-C4 y validación del oráculo. No hay implementación ni ejecución.


## 16.120 — AB-01/02: crosswalk semántico CMP/PAR/RUL/MET (2026-11-10)

Se reutilizan DEC-C10-054/068/069/071/079/080/082/083. El mapping semántico de la instancia queda reconciliado: CMP→NODE anchor por snapshot; PAR→propiedad tipada del CMP owner + manifiesto/COVERAGE_SCOPE; RUL→PREDICATE con AST y bindings tipados a ENABLED/PROFILE; REF→EDGE solo si existe relación inventariada; MET→metadatos/evidencia existentes. No se crean tablas/columnas ni NODE por PAR.

Los dos PAR siguen DEC-C10-083 en siete etapas; la RUL conserva expresión, owner, scope, operadores, operandos, bindings y REQUIRE. Se distinguen mappings semánticos de etapa y composición para rutas F y A; la igualdad semántica no acredita independencia técnica de A respecto de B.

AB-01 semántico DESIGN RESOLVED; encoding/schema/escaping/canonicalización OPEN. AB-02 SEMANTIC CROSSWALK RECONCILED; mapping_id/version, roster REF, snapshots, cobertura y evidencia OPEN. No hay IAM sellado ni autorización de implementación/ejecución.


## 16.121 — Reconciliación AB-09: escenarios, truth/observed y firewall (2026-11-10)

Se integra el contrato del ledger AB §15 y del maestro §247. R0–R3 quedan diferenciados sin crear IDs nuevos: R0 estipula aislamiento focal dentro de universo cerrado; R1 conserva alternativa basal estable; R2 incorpora vía colateral de B y obliga a interpretar ITT como efecto de política/paquete; R3 contiene intento efectivo sin C_dep* completo y prohíbe inferir accesibilidad desde intento/instalación. Se reutilizan FSTAR, EXC/PM/IV, B-M01…15, PROV-01…12 y la matriz temporal.

Se fijan las reglas comunes de verdad binaria del DGP, observación trivalente 1/0/? según evidencia/cobertura, y no equivalencia entre desconocido y ausencia. F_alt=0 y Reach=0 exigen universo cerrado y cobertura exhaustiva. C_dep*, A_f*, D_f*, ΔT_acc*, F*, Outcome y Value conservan sus contratos separados.

Se explicita la frontera de roles: Generator conoce truth/potenciales/semillas; Analyzer recibe solo observables autorizados (incluida Z observada) y no truth, potenciales, asignación oculta ni etiquetas de escenario; Evaluator puntúa solo después de congelar la salida del Analyzer. La separación requiere controles técnicos y pruebas negativas; no se considera demostrada por esta especificación.

**Resultado:** AB-09 DESIGN SPECIFIED / INTEGRATION RECONCILED, no DESIGN COMPLETE ni materialmente cerrado. Permanecen abiertos universo/cobertura, F*/C0/G/H_time, oráculo y cegamiento, observación/missingness, parámetros D2/C_dep, población/soporte/interferencia y criterios cuantitativos de evaluación. No se crean fixtures ni código y no se ejecuta simulación. AB sigue IN_PROGRESS / NOT DESIGN FROZEN / NOT IMPLEMENTABLE; `scientific_execution=false`; `execution_authorized=false`.


## 16.122 — Matriz integrada AB-01…09 y transferencia parcial a C (2026-11-10)

Se incorpora la matriz de dependencias y handoff del ledger AB §16 y maestro §248. La reconciliación distingue gates semánticos/abstractos definidos de inputs materiales aún ausentes; identifica cuatro bloques de bloqueo (medición/identidad, mecanismo/primeras etapas, población/soporte/interferencia y evaluación truth/observed) y establece que la dependencia AB es parcialmente paralela, no estrictamente lineal.

El paquete C §§221–229 puede continuar con contratos semánticos y simbólicos, jerarquía de estimandos, reglas de población pre-Z, roster de 16 estados C_dep*, R0–R3, trivalencia y separación Generator/Analyzer/Evaluator. Debe preservar AB-M01…M11 y cada input OPEN/UNKNOWN con su procedencia. No puede tratar como resueltos schemas físicos, identidades ejecutables, C0/G/H_time, U_G/cobertura, evidencia MD-C1/MD-C4, probabilidades D2/θ, población/q_X*/soporte, interferencia, oráculo, truth por unidad ni missingness.

No se declara AB cerrado ni paquete C aprobado. §§221–229 son contratos/propuestas documentales; C-MED y C-ANALYZER mantienen cobertura parcial y la mediación causal no está identificada. Sin Design Freeze, implementación, simulación ni ejecución; scientific_execution=false; execution_authorized=false.


## 16.123 — C-MED: estimando interventional, confusión inducida y reglas de identificación (2026-11-10)

Se incorpora la especialización del maestro §249 y ledger AB §17. Se separan ITT de Z, efecto del régimen material B, mediación interventional por la distribución conjunta factible de ΔT_acc* y pregunta primaria C10-D1 θ_A(q). Se fija una referencia explícita b1 para el estimando interventional candidato; cualquier término complementario incluye rutas restantes y no se etiqueta como efecto directo puro.

La historia post-B pre-M L puede ser confusor mediador–Value inducido por tratamiento. El análisis requiere DAG longitudinal, historia medida suficiente, método g compatible, positividad secuencial, soporte, intervención mediadora factible, consistencia/versiones, medición válida e interferencia tratada. No se resuelve con regresión convencional ni ajuste por covariables postratamiento como si fueran basales.

MED-03 y MED-05 siguen OPEN; los inputs AB-M03…M11 permanecen abiertos donde corresponda. No se aprueba estimando final, método, parámetros, tolerancias ni potencia; sin Design Freeze, implementación ni ejecución.


## 16.124 — C-MED: registro causal H/L/M y rutas hacia Value (2026-11-10)

Se operacionaliza el DAG preexistente (§233) y la especificación C-MED (§249) en maestro §250 y ledger AB §18. Se reutiliza el roster, sin crear una matriz paralela: H basal; Z/B y eventos de recepción/instalación; L post-B pre-M candidata; M=ΔT_acc*; E_T como proceso de observación; y variables downstream Reach/Π_H, conocimiento/consideración, selección/inicio, ejecución, Outcome y Value.

La clasificación de L es relativa al estimando y dimensión V_j: solo es confusor mediador–Value inducido si B la afecta y causa tanto M como V_j por una ruta pertinente. Los dominios de recursos, permisos, dependencias, runtime, capacidad y C_dep* no se clasifican automáticamente. Las rutas B→L→M→downstream→V, B→L→V, vías A1/A2/colaterales, observación diferencial e interferencia quedan como hipótesis a auditar.

Siguiente gate material: crosswalk campo a campo del roster U*/R*/C*/X*/E_T, con field_id ya existente, unidad/frontera, tiempo, snapshot, rol, fuente, cobertura, truth/observed y relación con cada V_j. No se inventan campos ni se rellenan valores. Outcome/Value (§224), microdominio, fuentes, topología de interferencia y evidencia de rutas permanecen OPEN. Sin Design Freeze, implementación, simulación ni ejecución.


## 16.125 — MED-02c: crosswalk documental de subcampos U*/R*/C*/X*/E_T

Se añade maestro §251 y ledger AB §19, descomponiendo el roster ya existente de §232 sin duplicar matrices ni crear field_id/event_id. Se explicitan los subcampos documentados de transformaciones e identidades, interfaces/dependencias, CMP/PAR/RUL, runtime/host, recursos, autorización/ACL, red, configuración/datos, seguridad, estado persistente, observabilidad/oráculo, rendimiento y alternativas A1/A2. El tipo es primario y condicional por función; las familias mixtas se descomponen, y los campos no inventariados permanecen UNKNOWN.

Se conserva AB-TIME-01: hasta armonización aceptada, usar nombres de eventos y timestamps/snapshots fuente, sin renumerar índices. Se mantiene separación de truth/observed/E_T y regla de no doble conteo. La clasificación de L como confusor inducido exige B→L, L→M y L→V_j por estimando/horizonte.

**Resultado:** avance documental de MED-02c; no cierre material. MED-02c3/c4/d, field_id/event_id efectivos, instancia, fuentes/cobertura, matching, MD-C1/MD-C4, Outcome/Value dimensional y DAG por V_j siguen OPEN. Sin Design Freeze, implementación, fixtures ni ejecución.


## 16.126 — MED-02d: crosswalk E_T y adjudicación sobre U_G

Se incorpora maestro §252 y ledger AB §20. Se reutilizan los cinco registros U_G existentes: EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER; no se crean tablas, FK, target PAR ni taxonomía física nueva. Se separan truth_DGP, observed_state, E_T y ΔT_acc*, y se fijan clases funcionales de fuentes, dimensiones de suficiencia, cobertura por universo exacto, cegamiento y cadena de adjudicación.

**Resultado:** interfaz documental E_T/U_G especificada. MED-02d continúa OPEN materialmente por falta de instancia/fuentes/snapshots, IDs efectivos, denominadores/scopes, AB-TIME-01, oráculo/fiabilidad, evaluadores/cegamiento y modelo de missingness/error diferencial. No registros, fixtures, implementación ni ejecución.


## 16.127 — AB-TIME-01: crosswalk temporal de event_key

Se añade maestro §253 y ledger AB §21. Se distinguen los tres relojes históricos, se corrige la referencia documental errónea a DGP §2 (el reloj comprimido está en §34.1), y se define la secuencia semántica BASELINE_PRE_Z…POST_HORIZON_RESIDUAL. Se identifica el colapso de ASSIGNMENT_Z y POLICY_PROVISION en Path Matrix t1 y la compresión de selección/ejecución en DGP §34.1.

**Resultado:** orden semántico reconciliado; alias numéricos trazados; AB-TIME-01 PARTIALLY RESOLVED. La adopción formal del reloj posterior t−1…t9/t+1 y el tratamiento normativo del reloj §34.1 siguen OPEN. stage_key, SNAPSHOT.phase/timestamp, ruta y step_k permanecen ejes separados. Sin cambios a registros U_G, sin event_id ni timestamps inventados, sin implementación o ejecución.


## 16.128 — MED-02c4: contrato de correspondencia temporal y snapshots

Se incorpora maestro §254 y ledger AB §22. Se reutilizan DEC-C10-065/070/071/072, C0, stage_key, SNAPSHOT, COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK y evaluadores/adjudicación. Se distingue event_key semántico, source-native event ID y EID de transformación; no se crea campo/tabla de eventos.

**Resultado:** MED-02c4 DOCUMENTED / MATERIAL OPEN. Quedan definidas precedencia de las siete etapas, binding C0 de nueve componentes, separación de SNAPSHOT.phase y reloj causal, trazabilidad de evento→snapshot→evidencia, matching/deduplicación y contratos C4-01…15. Faltan instancias, snapshots, event IDs, tiempos válidos/sincronizados, rutas exactas, scopes/denominadores y control C0 ejecutado bajo autorización. AB-TIME-01 continúa parcialmente resuelto por su adopción formal pendiente. Sin schema change, fixtures, implementación ni ejecución.


## 16.129 — AB-09: truth tables R0–R3 y separación Generator/Analyzer/Evaluator

Se incorpora maestro §255 y ledger AB §23, desarrollando el contrato ya existente en §247 y el inventario finito. Se especifican invariantes lógicos por escenario, el cruce R3 con fondo R0/R1, derivaciones de C_dep*/F_alt/A_f*/D_f*/ΔT_acc*/Reach, truth binaria y observed_state trivalente, firewall de escenarios y 12 contratos adversariales.

**Resultado:** AB-09 LOGICALLY SPECIFIED / DOCUMENTARY CROSSWALK COMPLETE / MATERIAL DGP AND OBSERVATION OPEN. No se repiten escenarios ni se asignan valores/probabilidades. Permanecen abiertos los parámetros y truth por unidad, alternativas y cobertura, F*/G/H, medición/missingness/oráculo, q_X*/soporte/interferencia, Outcome/Value dimensional, firewall ejecutado y métricas de recuperación. Sin fixtures, implementación, simulación ni ejecución.


## 16.130 — C-ANALYZER: adjudicación y denominadores de recuperación/errores

Se incorpora maestro §256 y ledger AB §24, reutilizando §§225.7/225.9 y 229.5–229.7, sin duplicar contratos P177/P178/P179/P182/P183. Se fijan clases truth/salida, falsas declaraciones de identificación, falsa atribución focal, sustitución de estimando, bounds incorrectos, abstención correcta/falsa, fallos técnicos, denominadores por clase y solapamiento de errores, ficha de tolerancias ex ante y orden de cegamiento/adjudicación.

**Resultado:** AN-03 DOCUMENTED / DENOMINATOR LOGIC SPECIFIED; AN-04 PARTIALLY SPECIFIED / NUMERIC THRESHOLDS OPEN; C-ANALYZER OPEN. No se asignan umbrales, multiplicidad, N ni réplicas; permanecen pendientes la calibración, potencia/precisión y validación técnica del firewall. Sin fixtures, código, simulación ni ejecución.


## 16.131 — C-MED / MAP-01–02: frontera D2→g y separación de estimandos

Se incorpora maestro §257 y ledger AB §25. La reconstrucción confirma que MAP-01/02 ya existían en la auditoría IV §14.6–14.7; se reutilizan sin duplicarlos. MAP-01 tiene campos contractuales definidos pero valores materiales abiertos. MAP-02 tiene secuencia/medición temporal definidas documentalmente, pero ventanas, fuentes, snapshots y evidencia abiertos.

La reconciliación mantiene separados:
1. θ_A(q): pregunta científica general sobre políticas factibles que inducen el ΔT_acc* completo bajo régimen común q;
2. ITT_Z^D2: efecto de asignar B_g0/B_g1, interpretable como política/paquete si no se excluyen o identifican rutas colaterales;
3. IIE_M candidato: componente interventional secundario a través de la distribución conjunta factible de M=ΔT_acc*, con H/L pre-M y método longitudinal pendiente.

D2 no equivale por definición a g^Af ni a las políticas generales g1/g0. La interpretación focal exige versiones, mapping B→g^Af, q*, población/soporte, medición independiente y control de vías colaterales. A_f*/D_f* no sustituyen el mediador estructural completo; ΔE_T permanece separado y ΔX* requiere crosswalk semántico por campo. Se mantienen abiertos MED-03/05 y MAP-03…07.

**Resultado:** reconciliación conceptual/documental; no identificación ni cierre material. Sin aprobación de estimando/método, Design Freeze, implementación, fixtures, simulación o ejecución. scientific_execution=false; execution_authorized=false.


## 16.132 — MAP-03/04 y MED-03: soporte, equivalencia de versiones y clasificación longitudinal

Se incorpora maestro §258 y ledger AB §26. MAP-03 formaliza la distribución inducida conjunta de M=ΔT_acc* bajo política/versiones y régimen común; distingue soporte estructural, asignación/recepción, secuencial, mediador y resultado. L postratamiento solo entra como historia pre-M en un método longitudinal explícito; no se ajusta mecánicamente como basal. MAP-04 impide agrupar versiones por etiqueta o igualdad observada de M si persisten diferencias directas/colaterales hacia V_j.

MED-03 reutiliza el roster §§232/250 y crosswalk §§251–254. La clasificación campo×tiempo×V_j exige evaluar B→L, L→M y L→V_j. Solo la conjunción de las tres relaciones hace de L_k un confusor mediador–Value inducido. Se distinguen antecedente técnico, vía colateral, causa compartida, downstream y evidencia E_T. Las flechas desconocidas permanecen UNKNOWN/UNRESOLVED.

**Resultado:** contratos documentales integrados; MAP-03/04 y MED-03 permanecen OPEN en lo material/identificativo. No se elige método, umbral de positividad, población, q, parámetros o potencia. Sin Design Freeze, implementación ni ejecución. scientific_execution=false; execution_authorized=false.

## 16.133 — MAP-05/06: rutas alternativas, vías colaterales y exclusión por resultado

Se incorpora maestro §259 y ledger AB §27. Se reutilizan auditoría IV §§12.2–12.4 y 14.5–14.7, R0–R3 y superficies B-M existentes. MAP-05 exige cobertura del universo de rutas F/A y alternativas, dependencias compartidas, recursos, permisos, red, seguridad, rendimiento/costes, datos, conocimiento y residuos. R1 alternativa basal estable no es por sí sola violación de exclusión; R2 alternativa modificada por B sí introduce ruta no focal. La ausencia requiere universo exhaustivo y cobertura.

MAP-06 emite dictámenes separados EXCLUSION_O y EXCLUSION_Vj (SUPPORTED/CONTRADICTED/UNKNOWN). Una ruta directa a Value puede existir con Outcome constante. Se separan exclusión estructural, medición diferencial/oráculo e interferencia/carryover. ITT_Z^D2 puede seguir siendo efecto de asignación si diseño, consistencia, unidad/interferencia y medición son válidos; LATE_f/Wald no se interpreta causalmente si falla cualquier supuesto IV. Estos gates no identifican θ_A(q) ni la mediación por sí mismos.

**Estado:** especificación contractual/documental integrada; MAP-05/06 MATERIAL OPEN. No hay dictamen empírico de exclusión para una instancia no materializada. AB-M06/M09/M10 siguen OPEN. Sin Design Freeze, implementación ni ejecución.

## 16.134 — MAP-07: matriz de adjudicación y regla de no transferencia entre estimandos

Se incorpora maestro §260 y ledger AB §28, especializando auditoría IV §14.5, C-MED §257 y C-ANALYZER §256. Se documenta la adjudicación por estimando × resultado/dimensión × población/unidad × horizonte × versión para ITT_Z^D2, LATE_f^D2, θ_Af(q_X*), θ_A(q) e IIE_M. Se fijan condiciones mínimas, límites de interpretación y reglas para no transferir evidencia entre objetos causales.

Se añaden reglas de lectura de combinaciones (p. ej. ITT identificado con exclusión focal UNKNOWN; LATE local sin θ_A; mediación IIE_M sin identificación general), dictámenes independientes para Outcome y cada V_j y abstención del Analyzer ante target mismatch, supuestos UNKNOWN, evidencia no comparable o rutas no discriminadas. Se reutilizan §256 y P177/P178/P179/P182/P183; no se inventan umbrales ni denominadores.

**Estado:** MAP-07 DOCUMENTED / MATERIAL OPEN. Contrato de adjudicación integrado; no existe validación empírica de los estimandos. MAP-01…06, MED-02…06, C-Value y AN-04 siguen pendientes. Sin Design Freeze, implementación, fixtures, simulación ni ejecución; scientific_execution=false; execution_authorized=false.

## 16.135 — MED-04: contrato candidato de políticas factibles g0/g1 y régimen común q

Se incorpora maestro §261 y ledger AB §29, reutilizando C-MED §§249/257 y auditoría IV §§14.1–14.5. Se define g0/g1 como políticas estocásticas factibles sobre el mediador estructural conjunto ΔT_acc*; se preserva la dependencia entre ΔU*/ΔR*/ΔC*/ΔX* y se impide confundirlas con B_g0/B_g1^D2, instalación o D_f* aislado. La expresión θ_A,j(q)=E_q[V_j^{g1}−V_j^{g0}] es notación candidata, no fórmula aprobada.

Se especifica el contenido mínimo de q y una regla crítica para L post-B: no se ajusta como basal; debe permanecer invariante bajo la comparación, definirse una distribución de referencia común factible o reformularse el contraste como régimen longitudinal conjunto. Se documentan requisitos de factibilidad, soporte, versiones, interferencia, medición y separación truth/observed.

**Estado:** MED-04 DOCUMENTED / PARTIALLY SPECIFIED. Definición sustantiva de g0/g1, q material, conjunto admisible M, población/H, Value/horizonte, soporte y tratamiento de L permanecen OPEN. No se aprueba fórmula final, método ni identificación. Sin Design Freeze, implementación, fixtures, simulación o ejecución; scientific_execution=false; execution_authorized=false.

## 16.136 — MED-05: contrato de identificación del efecto interventional conjunto

Se incorpora maestro §262 y ledger AB §30, especializando el IIE_M candidato de §249 sin crear otro estimando. Se fijan nueve gates de identificación para consistencia/versiones, historia basal, intercambiabilidad de B y M, positividad secuencial, factibilidad de M, medición, interferencia y especificación. Se detalla el tratamiento de L inducida por B bajo referencia b1 y el soporte condicional cruzado requerido para evaluar G_M^b0 en historias L relevantes bajo b1.

Se delimitan g-computation longitudinal, ponderación/densidades y TMLE longitudinal como familias candidatas, sin seleccionar método. Se integra la evolución downstream hasta V_j para el contraste total y se prohíbe el ajuste convencional de L como basal o la transferencia del IIE a θ_A(q), ITT, LATE o V_j distintos. Se incorporan estados IDENTIFIED/PARTIALLY_IDENTIFIED/NOT_IDENTIFIED/INDETERMINATE y reglas de abstención.

**Estado:** MED-05 DOCUMENTED / CANDIDATE; sin validación empírica. MED-03/04/06, §224, inputs AB/MAP y AN-04 siguen OPEN. Sin Design Freeze, implementación, fixtures, simulación o ejecución; scientific_execution=false; execution_authorized=false.

## 16.137 — MED-06: sensibilidad, identificación parcial y bounds para C-MED

Se incorpora maestro §263 y ledger AB §31, reutilizando §225.6–225.9, §§249.5–249.7, §262 y §256. Se especializa la sensibilidad para IIE_M con mediador conjunto ΔT_acc*, por tupla de estimando×V_j/Outcome×población/unidad×horizonte×versión/soporte. Se mantiene la no transferencia a θ_A(q), ITT/paquete D2, LATE_f o θ_Af.

Se definen amenazas y parámetros a justificar para confusión B–resultado y M–V, L incompleta, error conjunto de M, error Outcome/Value, soporte cruzado, missingness/selección, interferencia/carryover, versiones/provisión de fondo y especificación/interacciones. Se exige análisis de tipping points y escenarios conjuntos cuando proceda. Se delimitan familias candidatas de bounds, incluidas cotas worst-case para resultados acotados, selección (Lee solo bajo monotonicidad defendible), confusión no medida bajo restricciones explícitas, error acotado, soporte limitado y spillovers. Se establece que un bound solo es informativo si reduce el rango trivial y que incertidumbre muestral e identificación parcial se reportan por separado.

**Estado:** MED-06 DOCUMENTED / PARTIALLY SPECIFIED. Rangos/valores, escalas, soporte, historia L, error, missingness, interferencia, método concreto de bounds y umbrales AN-04 siguen OPEN. Sin Design Freeze, implementación, fixtures, simulación o ejecución; scientific_execution=false; execution_authorized=false.

## 16.138 — C-Value: crosswalk candidato Outcome/Value para Opción A

Se incorpora maestro §264 y ledger AB §32, especializando §224 para la migración de configuración entre entornos. Se diferencia F* como criterio técnico, Outcome como estado/consecuencia operativa y Value como valoración contextual para beneficiarios identificados. Se proponen, sin seleccionar, familias O-MIG, O-CONF, O-SVC, O-REC y O-BUR, y roles/dimensiones candidatas para propietario del servicio, operador, mantenedor, usuarios (si existen) y responsable de riesgo (si procede).

Se preserva Value como vector y se prohíbe circularidad con ΔT_acc*, A_f*, D_f*, Reach, trayectoria o ejecución. Telemetría no equivale a valoración; portabilidad futura no se infiere de disponibilidad técnica actual; seguridad/compliance puede ser restricción no compensatoria. La selección confirmatoria exige fichas completas §224 y decisión pre-resultados.

**Estado:** C-Value CANDIDATE CROSSWALK DOCUMENTED / MATERIAL OPEN. Beneficiarios, indicadores, fuentes, escalas, ventanas, trade-offs, instrumentos, error, missingness, cegamiento y multiplicidad siguen OPEN. No se identifica ΔT_acc→Value ni se aprueba implementación/ejecución; scientific_execution=false; execution_authorized=false.

## 16.139 — C-Value ↔ roster: crosswalk de Outcomes/Value contra §232/§233

Se incorpora maestro §265 y ledger AB §33. Se especializa la instancia C10S-SVC-REQUEST-PROCESSOR v1.0.0 / instancia -001 rev1 / CMP-SERVICE-LOGIC-001. Se reutilizan el roster §232, DAG §233, F*/FP-01…08, B-M01…15 y E_T/U_G; no se crean campos ni IDs.

Se mapean los cinco Outcomes candidatos: O-MIG sin campo terminal; O-CONF con anclaje conceptual parcial en F*/FP-01…08; O-SVC con superficies de observación pero sin medida de continuidad; O-REC con superficies de rollback/estado pero sin medida de recuperación; O-BUR con superficies de recursos/rendimiento pero sin coste/tiempo aprobados. Ningún O tiene ficha §224 completa. W_attempt, S_install, C_dep*, transformaciones, accesibilidad, Reach y ejecución no sustituyen Outcome.

No hay beneficiarios/roles Value confirmados; CMP.owner no equivale a beneficiario. No hay instrumentos ni registros de valoración poblados. L_m y la ecuación lineal ilustrativa V=3O+4L_m+epsilon_V no se heredan como Value aceptado. No se crean field_id/event_id, snapshots, registros E_T ni fixtures.

**Estado:** C-VALUE↔ROSTER CROSSWALK DOCUMENTED / MATERIAL OPEN. MED-02/03 continúan OPEN; no se identifica ΔT_acc→Value. Sin Design Freeze, implementación ni ejecución; scientific_execution=false; execution_authorized=false.

 
## 16.140 — C-Value: auditoría de roles y beneficiarios del dominio sintético (2026-11-11)

Se incorpora al expediente C-Value la auditoría de los roles candidatos de §264 contra DEC-C10-068/069/089, el contrato funcional de referencia, el DGP temporal/roles y el crosswalk §265.

La instancia `C10S-SVC-REQUEST-PROCESSOR v1.0.0` define una unidad lógica sintética que acepta solicitudes cuando está habilitada y expone un perfil operativo declarado. No identifica solicitante, consumidor, usuario, cliente, propietario organizativo del servicio ni beneficiario. La referencia genérica a consumidor/sistema en la definición de servicio lógico no materializa una entidad ni una población.

Se preservan estas distinciones:
- `CMP-SERVICE-LOGIC-001` es el CMP lógico de referencia; `CMP-SERVICE-LOGIC` es owner/rol lógico provisional de la RUL, no propietario organizativo ni beneficiario.
- El campo `actor` en t6 y el rol ejecutor sintético registran quién inicia/ejecuta el intento; no demuestran que sea operador del servicio, consumidor o beneficiario.
- `LOGICAL_SERVICE_UNIT` es NODE raíz aceptado; DEC-C10-089 deja sin adjudicar su identidad/relación con CMP-SERVICE-LOGIC-001.
- El evaluador independiente es un rol metodológico de adjudicación, no un beneficiario.

| Rol candidato §264 | Resultado del cotejo | Estado |
|---|---|---|
| Propietario del servicio | Owner lógico de componente/regla no acredita propiedad organizativa del servicio | NOT_GROUNDED |
| Operador | Actor ejecutor previsto, sin identidad/responsabilidad operativa materializada | NOT_GROUNDED |
| Mantenedor | No existe función de mantenimiento instanciada | NOT_GROUNDED |
| Usuario/destinatario | Servicio acepta solicitudes, pero no hay solicitante, población ni relación de consumo instanciados | NOT_GROUNDED |
| Responsable de riesgo | Seguridad/compliance son restricciones candidatas, sin actor ni mandato de valoración | NOT_GROUNDED |

El DGP incluye beneficiario, regla/version y horizonte en t9 y DGP-13 exige beneficiario, criterio, escala y horizonte fijados ex ante. Son requisitos todavía no satisfechos, no prueba de que los roles existan. F*/FP-01…08 puede sostener Outcome técnico de conformidad cuando se complete su ficha §224; no demuestra valoración contextual ni beneficiario.

**Conclusión:** Opción A puede seguir desarrollándose para accesibilidad, conformidad y Outcomes técnicos. El dominio aceptado no permite actualmente instanciar Value contextual. No se concluye que sea imposible: introducir un consumidor/beneficiario sintético sería una extensión sustantiva del DGP que requiere propuesta, decisión explícita y revisión de sus consecuencias causales, temporales, de medición e interferencia. No se infiere desde el nombre del servicio, CMP.owner, actor ejecutor ni telemetría.

**Estado:** ROLE/BENEFICIARY AUDIT DOCUMENTED / NO BENEFICIARY GROUNDED / VALUE MATERIAL OPEN. No se crean entidades, IDs, campos, eventos, snapshots, instrumentos ni fixtures. MED-02/03 siguen OPEN; no Design Freeze, implementación ni ejecución; scientific_execution=false; execution_authorized=false.

 
## 16.141 — Comparación de alcance Value A/B y recomendación de variante DGP (2026-11-11)

Se incorpora a C-Value la comparación de dos alcances, sin alterar DEC-C10-068 ni el contrato funcional aceptado de Opción A.

- **A — base sin extensión:** conserva el microdominio aceptado. Puede validar accesibilidad/ΔT_acc, Reach, trayectoria y Outcomes técnicos una vez operacionalizados. Value contextual permanece no instanciado; por tanto, A no permite probar la atribución causal ΔT_acc→Value.
- **B — extensión sintética explícita:** añade un rol consumidor/beneficiario y una relación con el servicio, demanda pre-Z y criterio de valoración ex ante. Puede probar si el Analyzer recupera la contribución causal a Value dentro del DGP estipulado; no aporta validez externa sobre usuarios reales.

**Recomendación propuesta:** mantener A intacta como variante base y desarrollar B como variante DGP separada/versionada. Esta opción preserva la trazabilidad del dominio aceptado, permite comparar resultados con y sin capa de beneficiario y evita presentar una ampliación como si ya perteneciera al roster de Opción A. La recomendación no está aceptada y no crea roles ni variables.

B no podrá aprobarse hasta especificar: rol/relación beneficiario-servicio-unidad; demanda y población pre-Z; perspectiva y criterio; separación O/V; vector Value y trade-offs sin agregación por defecto (P179); DAG con vías directas y mediadas; temporalidad; medición independiente §224/P182/P183; unidad/interferencia; y DGPs adversariales que distingan efecto focal, vías directas, Outcome constante/Value cambiante y trade-offs. El Analyzer no recibe truth ni potenciales; el Evaluator conserva el DGP verdadero.

**Límite:** un PASS solo acredita recuperación de la relación estipulada dentro del DGP sintético. No valida preferencias ni Value de usuarios reales ni acredita la hipótesis empírica general de TGCV.

**Estado:** A/B COMPARISON DOCUMENTED / B RECOMMENDED AS SEPARATE DGP VARIANT / USER ACCEPTANCE OPEN. No Design Freeze, implementación, fixtures, simulación ni ejecución. scientific_execution=false; execution_authorized=false.


## 16.142 — Aceptación de arquitectura A/B para C-Value (2026-11-11; DEC-C10-095)

El usuario acepta conservar A como variante DGP base inalterada y desarrollar B como extensión sintética independiente y versionada.

**Consecuencias para C:** A conserva el dominio y contrato aceptados; podrá operacionalizar accesibilidad/ΔT_acc, Reach, trayectoria y Outcomes técnicos. Value contextual permanece no instanciado y no se atribuirá ΔT_acc→Value en A. B se especificará como extensión separada; todavía no se seleccionan rol beneficiario, relación con unidad/servicio, demanda pre-Z, perspectiva, criterio, dimensiones, indicadores, escalas, pesos, horizonte ni parámetros. P179 exige preservar el vector y trade-offs; P182/P183 gobiernan medición y ausencia/identificación.

**Consecuencias para D:** deberá consumir contratos A/B versionados y distinguir datos observados, truth del DGP y outputs del Analyzer; ninguna verdad generadora se filtra al Analyzer. No se deriva schema físico de esta decisión.

**Consecuencias para E:** integración confirmatoria solo tras cierre semántico de A/B, estimandos, contratos de medición, adjudicación y provenance. Los resultados de A y B no se agrupan ni intercambian.

**Gates:** B permanece en especificación documental; MED-02/03 OPEN; no Design Freeze, implementación, fixtures, simulación o ejecución. scientific_execution=false; execution_authorized=false. Véase DEC-C10-095.


## 16.143 — Contrato mínimo de beneficiario y Value para B (2026-11-11)

Se crea C10S-B-VALUE-MIN-001 como contrato de admisibilidad documental para la variante B. Establece requisitos, no una instancia: identidad/tipo de beneficiario, relación con servicio y unidad experimental, elegibilidad y demanda pre-Z, consecuencia, perspectiva/autoridad de valoración, población/horizonte, cardinalidad y provenance. Distingue unidad experimental, unidad lógica de servicio, beneficiario, actor ejecutor y evaluador. Prohíbe inferir beneficiario desde CMP.owner/actor/LOGICAL_SERVICE_UNIT; demanda no equivale a uso/selección/ejecución; V_j no puede recodificar ΔT_acc, Reach u Outcome técnico ni contener circularmente la hipótesis. Mantiene vector P179 y trade-offs, P182/P183, §224, estimandos por dimensión y vías alternativas. No selecciona tipo de beneficiario, demanda, consecuencia, dimensión, escala, regla, horizonte ni parámetros. C: resolver semántica antes de fichas; D: representar relaciones/temporalidad/truth-observed sin schema físico; E: probar invariantes y abstención/no identificación. B-BEN/B-VAL DRAFT; instancia B OPEN; MED-02/03 OPEN; sin freeze/implementación/ejecución. Véase C10S-B-VALUE-MIN-001.


## 16.144 — B1 entidad solicitante sintética como tipo candidato (2026-11-11)

El usuario acepta B1 —entidad solicitante sintética del servicio— como tipo candidato de beneficiario para desarrollar B. No es una instancia real ni un perfil empírico. La definición candidata vincula necesidad/objetivo pre-Z, relación versionada con la unidad lógica de servicio, posible solicitud y consecuencia para la entidad. Se distinguen demanda basal, solicitud, procesamiento técnico y consecuencia valorada. El procesamiento correcto/O-CONF no equivale a Value; solicitud enviada no equivale a necesidad satisfecha; no solicitud/no ejecución no implica ausencia de demanda ni V=0. Solicitante y beneficiario pueden ser la misma entidad lógica solo por estipulación explícita B1. C debe cerrar demanda/consecuencia/perspectiva/dimensiones; D separar entidad-demanda-solicitud-servicio-unidad-consecuencia sin schema físico todavía; E probar separación Outcome/Value, conservación de demanda no atendida y abstención. Instancia, cardinalidad, demanda concreta, consecuencia operacional, perspectiva, dimensiones, medición, DAG/estimandos y parámetros siguen OPEN. Véase C10S-B1-REQUESTER-CANDIDATE-001.


## 16.145 — Reconciliación de demanda basal B1 y demanda operativa (2026-11-11)

Se reconcilia B1 con C10-S-POP-CMP-001 y el contrato temporal DGP. Need_preZ es la necesidad/objetivo focal de la entidad solicitante en truth antes de Z; E_req_preZ es elegibilidad de petición aún no definida; Request_event es la petición formulada/registrada con ventana y ubicación temporal OPEN; D_resource es demanda operativa de recursos/capacidad, distinta de la necesidad del beneficiario. No confundir E_req_preZ con E_i/P*_tau2/P*_F. No condicionar población/ITT a Request_event ni a variables post-Z. La verdad Need_preZ=1/0/? se separa de evidencia observada; Request_event=0 no demuestra ausencia de necesidad y Request_event=1 no prueba admisibilidad/procesamiento/satisfacción. No asignar Request_event a t5/t6/t7 sin reconciliación. No cambiar el reloj t−1/t0…t9 ni DEC-C10-066/067. OPEN: contenido/medida de necesidad, elegibilidad de petición, cardinalidad, relación con unidad experimental, ventana de solicitud, observabilidad, población y estimando de Value. Véanse C10S-B1-REQUESTER-CANDIDATE-001 §10, C10-S-POP-CMP-001 §10 y DGP temporal §14. Sin implementación ni ejecución.


## 16.146 — Ciclo de vida de solicitud B1 separado de la trayectoria transformacional (2026-11-11)

La reconciliación B1 §11 propone distinguir Request_opportunity, Request_attempt, Request_received, Request_admitted/rejected, Request_processing, Request_response y Beneficiary_consequence. No equivalen respectivamente a necesidad basal, t5 conocimiento/consideración, t6 selección/inicio, t7 ejecución, t8 Outcome ni t9 Value. El enlace petición↔trayectoria es OPEN (0:1/1:1/1:N); los eventos se registran en subledger con timestamps, sin añadir tiempos al reloj t−1/t0…t9 ni a H. El contrato funcional ENABLED/PROFILE/RUL no define protocolo completo, payload, colas, errores, SLA ni reintentos. Recomendación aún no aceptada: usar en la comparación sintética confirmatoria una carga de oportunidades/peticiones estandarizada ex ante y presentada mediante harness idéntico entre brazos, con registro del intento aunque no haya recepción; esto es probe de carga, no demanda natural ni preferencia real. La rama de envío endógeno sería secundaria/adversarial. No filtrar ITT por eventos post-Z. OPEN: calendario, payload, cardinalidad, relación con selección/ejecución, protocolo, consecuencia y horizonte. Véanse B1 spec §11, causal architecture §14, DGP temporal §15 y service contract §12.


## 16.147 — Aceptación de modalidad primaria estandarizada y modalidad secundaria endógena (2026-11-11)

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.


## C10-S — incorporación de decisión B1-UNIT-001 (2026-11-11)

**Decisión:** `DEC-C10S-B1-UNIT-001` — **ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN**.

Se acepta provisionalmente una entidad B1 por unidad experimental (UE), vinculada de forma explícita, unívoca, versionada y trazable a una instancia lógica de servicio aislada. La UE sigue siendo la instancia sintética completa a la que se asigna Z y para la que se generan estados transformacionales, trayectorias, Outcome y Value. La entidad B1 es el referente sintético de necesidad/objetivo pre-Z y de la consecuencia potencialmente valorable; no se confunde con la UE, el servicio ni el actor ejecutor.

La instancia de servicio deberá ser aislada respecto de otras UE en recursos, agentes, información, infraestructura, estado y canales de transmisión. La condición de aislamiento es una hipótesis de diseño que deberá justificarse y auditarse, no una propiedad presumida por nombrar instancias distintas. Si no puede sostenerse, se deberá definir clúster/unidad de asignación, mapa de exposición e inferencia compatible con interferencia antes de confirmar el diseño.

El número de oportunidades estandarizadas por UE queda **OPEN**. Cuando se fije, deberá ser constante entre brazos, establecido ex ante y administrado por un harness externo común; no podrá depender de recepción, admisión, procesamiento, selección, ejecución ni variables post-Z. La ausencia de envío/recepción/admisión seguirá siendo un estado observable y no se codificará automáticamente como ausencia de necesidad o Value=0.

La decisión no fija aún la identidad concreta/versionado final de B1 o del servicio, el número de oportunidades, la ventana/calendario, el payload, las reglas del protocolo, la cardinalidad request↔trajectory, los outcomes técnicos, la consecuencia B1, la perspectiva/autoridad de valoración ni los estimandos. No altera la separación entre el ciclo de petición y el reloj t−1/t0…t9; tampoco convierte solicitud, respuesta o procesamiento en selección, ejecución, Outcome o Value.

**Alcance:** decisión arquitectónica para continuar la especificación; no selecciona beneficiarios empíricos ni valida preferencias reales. No modifica DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación entre main y PR #116.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 — una oportunidad estandarizada por UE (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta **N_opportunities = 1 por unidad experimental (UE)** como configuración primaria candidata del probe estandarizado de servicio en el núcleo confirmatorio mínimo de C10-S. La oportunidad se define ex ante antes de Z y se presenta después del snapshot de accesibilidad t3/t4 mediante el mismo harness externo y bajo las mismas reglas en ambos brazos. El harness registra Request_attempt aunque no exista recepción por el servicio.

La identidad y el contenido de la oportunidad deberán ser comunes, trazables y versionados entre brazos. No recepción, rechazo, error o estado pendiente permanecen como estados observables; no se recodifican automáticamente como ausencia de necesidad, fallo transformacional, Outcome negativo ni Value=0. La población ITT no se condiciona a intento, recepción, admisión, procesamiento o respuesta post-Z.

Las oportunidades repetidas o cargas de mayor intensidad quedan reservadas a escenarios secundarios/adversariales; si se estudian, sus observaciones se anidan en la UE y no incrementan el número de unidades experimentales independientes. Esta configuración de una oportunidad no demuestra capacidad bajo carga sostenida ni demanda natural, preferencia revelada o Value del beneficiario.

Se mantienen abiertos: ventana/calendario exacto; definición final del payload y protocolo; identidad/versionado de B1 y servicio; cardinalidad request_id↔trajectory_id; tratamiento técnico de timeout, errores y pendientes; outcome técnico de respuesta; consecuencia independiente de B1 y horizonte; perspectiva/autoridad de valoración; población/soporte e integración exacta con ITT y mediación. No se equiparan eventos de petición con t5/t6/t7, ejecución transformacional, Outcome o Value, ni se amplía el reloj t−1/t0…t9.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación main/PR #116.

## DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 — contrato semántico de enlace (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como arquitectura candidata que la relación entre `request_id` y `trajectory_id` sea explícita, tipada y versionada, sin imponer una cardinalidad funcional 1:1. Se distinguen tres tipos no intercambiables:

1. `TEMPORAL_ASSOCIATION`: coexistencia temporal u orden compatible entre petición y trayectoria; no demuestra trazabilidad ni contribución causal.
2. `TRACEABILITY_LINK`: referencia técnica/documental verificable entre registros; no demuestra que la petición haya causado o modificado la trayectoria.
3. `CAUSAL_CONTRIBUTION`: relación causal definida por el DGP generador; debe distinguirse la verdad conocida por el generador de la evidencia observable y disponible para el analizador.

El modelo debe poder representar petición sin trayectoria atribuible, trayectoria sin petición atribuible, una petición que contribuya a varias trayectorias y, en escenarios con múltiples peticiones, varias peticiones que contribuyan a una trayectoria. La configuración primaria mantiene una oportunidad estandarizada por UE; por tanto, no genera múltiples request_id estandarizados dentro de esa UE, pero no impone que solo pueda existir una trayectoria ni que toda trayectoria tenga origen en esa petición. Las relaciones de escenarios secundarios con peticiones repetidas quedan anidadas en UE y no crean unidades experimentales independientes.

La existencia de cualquier enlace temporal o de trazabilidad no puede promoverse automáticamente a contribución causal. Las contribuciones causales se establecen por la verdad del DGP y se contrastan mediante los mecanismos/contrafactuales pertinentes; no se adjudican por proximidad temporal, coincidencia de IDs, respuesta del servicio o éxito técnico. Los registros observados no deben revelar al analizador la etiqueta de verdad del DGP salvo que ese conocimiento forme parte explícita del diseño de medición.

El enlace no define elegibilidad, inclusión poblacional, ITT, Outcome ni Value, y no puede usarse para excluir UE por eventos post-Z. No equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9; tampoco amplía el reloj t−1/t0…t9 ni la profundidad H. Los eventos de petición y sus enlaces se mantienen en subledger con timestamps, identidad/versionado y procedencia.

**OPEN:** reglas de generación de contribuciones, mecanismo de adjudicación, unidad temporal de atribución, tratamiento de contribuciones concurrentes y colaterales, evidencia observable para el analizador, cardinalidad de enlaces por tipo en cada DGP, y relación exacta con los estimandos ITT/mediación. No se congela schema físico ni protocolo técnico.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. D2 continúa como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren; main no se modifica.

## DEC-C10S-B1-CAUSAL-ADJUDICATION-001 — contrato de contribución causal petición–trayectoria (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como contrato causal candidato que una relación \`CAUSAL_CONTRIBUTION\` entre una petición y una trayectoria requiere un contraste contrafactual definido por el DGP: la presencia/intervención en una etapa concreta del ciclo de petición modifica una propiedad preespecificada de la trayectoria respecto del escenario contrafactual correspondiente, manteniendo explícitas las demás condiciones relevantes. La precedencia temporal, recepción, admisión, procesamiento, respuesta técnica, coincidencia de identificadores o éxito técnico no bastan por sí solos para adjudicar contribución causal.

Se distinguen, como clases potencialmente concurrentes y no necesariamente excluyentes:
- \`NECESSARY_CONTRIBUTION\`: sin la intervención/etapa considerada, la trayectoria definida no existiría bajo el contraste contrafactual especificado.
- \`ENABLING_CONTRIBUTION\`: la intervención hace factible la trayectoria o elimina una barrera relevante, sin implicar que sea causa única o suficiente.
- \`MODIFYING_CONTRIBUTION\`: la trayectoria también existiría, pero cambiaría una propiedad relevante bajo el contrafactual sin esa intervención.

Una contribución puede ser parcial, concurrente o colateral. Estas clases no implican signo positivo de Outcome ni creación de Value. La propiedad afectada debe identificarse en el DGP; no se presume que cualquier cambio de secuencia, factibilidad o atributo sea sustantivo sin regla de relevancia preespecificada.

La adjudicación debe referirse a una etapa concreta del ciclo —\`Request_opportunity\`, \`Request_attempt\`, \`Request_received\`, \`Request_admitted/rejected\`, \`Request_processing\` o \`Request_response\`— sin colapsar sus mecanismos. La oportunidad estandarizada común es una asignación/probe del harness; no se considera automáticamente una intervención realizada por el servicio ni una contribución causal. Cuando no se produce una etapa posterior, el DGP debe representar el mecanismo de no transición sin imputar una contribución de esa etapa.

Se mantiene segregación entre:
1. **Verdad del generador (\`truth_dgp\`)**: intervención/etapa, propiedad de trayectoria, contraste contrafactual, clase de contribución y procedencia de la etiqueta verdadera.
2. **Evidencia observada (\`observed_evidence\`)**: registros y mediciones permitidos al analizador, sin revelar etiquetas o potenciales contrafactuales reservados al generador.
3. **Adjudicación/evaluación**: comparación de inferencia del analizador con verdad segregada, reportando falsos positivos, falsos negativos y errores de clasificación; no convertir trazabilidad en prueba causal.

El registro conceptual de contribución deberá poder identificar etapa de petición, propiedad de trayectoria, contraste contrafactual, clase(s) de contribución, verdad DGP y evidencia observable, además de identidad/versionado/procedencia. Esto no congela un schema físico.

Esta adjudicación es mecanística y no modifica elegibilidad, población, unidad experimental, asignación ni estimando ITT; no se condiciona la inclusión a eventos post-Z. Tampoco define por sí sola Outcome o Value, ni equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9. No amplía el reloj t−1/t0…t9 ni H. D2 sigue como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren.

**OPEN:** especificación de los contrastes concretos de D2; propiedades de trayectoria causalmente relevantes; control de causas concurrentes/colaterales e interacciones; definición de intervención por etapa; positividad/soporte y versiones de tratamiento; evidencia observable y medición; reglas de atribución para contribuciones múltiples; sensibilidad a contrafactuales alternativos; relación con estimandos total, directo e indirecto y mediación.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen \`scientific_execution=false\` y \`execution_authorized=false\`; \`main\` no se modifica.

## DEC-C10S-D2-ESTIMAND-SEPARATION-001 — propagación al plan (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

El plan adopta cinco carriles de trabajo separados para D2: **C1** efecto total de asignación/ITT; **C2** primeras etapas separadas para `C_dep*`, `A_f*`, `D_f*`, `ΔT_acc*`; **C3** efecto focal de accesibilidad bajo mapping B→g y régimen común; **C4** mediación interventional vía `ΔT_acc*`, tratando Reach/trayectoria secuencialmente o como bloque conjunto explícito; **C5** contribución mecanística petición–trayectoria por contrastes contrafactuales específicos de etapa y propiedades de trayectoria predefinidas.

Reglas: no derivar residual por resta automática; no llamar efecto puro de accesibilidad al ITT si B abre vías colaterales; no sustituir primeras etapas entre eslabones; no reducir mediador estructural completo a `A_f*`; no filtrar ITT por eventos post-Z; no convertir contribución a trayectoria en Outcome/Value; mantener reloj t−1/t0…t9 y H sin cambios. P179 mantiene Value vectorial/trade-offs y P182/P183 permanecen como contratos transversales, no cerrados por esta decisión.

**Dependencias OPEN para cierre de los carriles:** población, unidad/interferencia, horizonte, Outcome y Value; versiones y cumplimiento de políticas; mapping B→g, q y soporte; vías colaterales, confusión mediador–resultado e interacciones; medición independiente y error de accesibilidad/Reach/trayectoria/Outcome/Value; identificación, sensibilidad, precisión y abstención; propiedades de trayectoria y contrastes DGP de las etapas de petición. No se selecciona método estadístico definitivo ni se declara ningún efecto identificado.

La decisión no autoriza Design Freeze, implementación, fixtures, simulación o ejecución científica. `scientific_execution=false`; `execution_authorized=false`. Registro: `DEC-C10S-D2-ESTIMAND-SEPARATION-001.md`.


## 16.148 — Secuencia estable de cierre y activación de C1 (2026-11-11)

Se adopta como control operativo la secuencia de ocho paquetes: (1) C1 ITT D2; (2) Outcome/Value; (3) C2 primeras etapas; (4) C3 efecto de accesibilidad; (5) C4 mediación; (6) C5 + DGP; (7) estadística/Analyzer; (8) contrato integrado de implementación. Cada paquete debe reutilizar decisiones y contratos existentes, producir un entregable verificable y distinguir cierre documental de identificación empírica. No se reabren decisiones aceptadas salvo contradicción o dependencia material demostrada. No se congelan schemas ni fixtures antes de cerrar dependencias científicas.

Se activa **C1.1 — reconciliación de población, UE/interferencia, brazos D2 y resultados Outcome/Value**. C1 es ITT por asignación a B_g0^D2 frente a B_g1^D2, no por provisión recibida, instalación, accesibilidad, petición, selección o ejecución. El ITT incluye las vías que active la política y se interpreta como efecto de paquete si existen vías colaterales no separadas. No se define residual por resta automática.

La aceptación A/B de DEC-C10-095 impide tratar Value como ya instanciado en A: A puede sostener Outcome(s) técnicos cuando se completen sus fichas; B es extensión separada para Value contextual y B1 sigue siendo tipo candidato, no instancia completa. Por ello C1 deberá dictaminar por separado resultados técnicos de A y dimensiones V_j de B cuando sean admisibles; no inventar dimensiones, indicadores, escalas, pesos ni escalar.

La secuencia, los criterios y el alcance de C1 se desarrollan en `C10_S_CLOSURE_SEQUENCE_AND_C1_ITT_WORKPLAN_001.md`. Este registro no modifica decisiones anteriores, no declara cerrado C1 ni autoriza Design Freeze, schemas físicos, fixtures, implementación, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`.


## 16.149 — C1.1: reconciliación del ITT D2 (2026-11-11)

Se documenta en `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md` la reconciliación de población, UE/interferencia, políticas D2, Outcome/Value y horizonte. Dictamen: C1 permanece OPEN. D2 y su contraste de asignación se reutilizan de DEC-C10-066/067; no se sustituye Z por recepción/cumplimiento ni se excluye por eventos post-Z. `P*_{τ2}` es candidato histórico, no población aprobada; `P*_F` es subpoblación de apertura funcional exclusiva. UE=UA requiere demostrar aislamiento o definir clúster/exposición. A permite Outcomes técnicos aún no operacionalizados; B es extensión independiente y Value sigue sin instanciar. H=3 es profundidad, no duración temporal.

Siguiente: **C1.2**, composición de `E_i`, predicados constitutivos y evidencia/indeterminación pre-Z, junto con recuperación del contrato de aleatorización D2. No se reabre ninguna decisión aceptada ni se autoriza freeze/implementación/ejecución.


## 16.150 — C1.2: elegibilidad basal y mecanismo de asignación (2026-11-11)

La auditoría §12 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md` confirma que la fórmula histórica de `E_i` con `C_other` no debe reutilizarse; `C_auth,base=1` es condición D2 común/invariante; `C_dep,0=0` no implica por sí sola `A_f,0*=0`; `E_req_preZ` es distinta de elegibilidad experimental. El contrato material de aleatorización (probabilidades/ratio, estratos, algoritmo/semilla y desviaciones) no se ha encontrado en los contratos revisados.

Recomendación: mantener `P*_{τ2}` como población objetivo primaria candidata C1 y `P*_F` como subpoblación secundaria, sin declarar cerrada la composición de `E_i`. Pendiente confirmación de esa precedencia poblacional. C1 permanece OPEN; no freeze ni ejecución.


## 16.151 — Decisión aceptada de precedencia poblacional C1 (2026-11-11)

`DEC-C10S-C1-POPULATION-PRECEDENCE-001` acepta `P*_{τ2}` como población objetivo primaria candidata del ITT C1-D2 y `P*_F` como subpoblación secundaria de apertura funcional exclusiva. La alternativa funcional basal no excluye de P*τ2; solo excluye de P*F cuando está respaldada. Esta decisión resuelve la confirmación de precedencia y no vuelve a abrirse sin contradicción material.

Composición de `E_i`, predicados/evidencia/indeterminación, soporte, truth/medición, interferencia, aleatorización, horizonte y resultados permanecen OPEN. Siguiente: **C1.3**, reconstruir E_i desde DGP/IAM y predicados constitutivos vigentes, distinguiendo validez de instancia, aplicabilidad de τ2, A_f basal, Need_preZ y E_req_preZ. No inventar una lista ni recuperar `C_other`; si la especificación material no permite cierre, declarar límite.


## 16.152 — C1.3: composición candidata de E_i y C1.4

El crosswalk `C10_S_C1_BASELINE_ELIGIBILITY_CROSSWALK_DRAFT_001.md` separa admisibilidad de instancia basal (`E_scope`) y aplicabilidad semántica de `τ2` desde `S0` (`App*(τ2,S0)`), sin confundirlas con `C_dep,0=0` ni `A_f,0*=0`. La propuesta `E_i=E_scope∧App*(τ2,S0)` queda como candidata NO aceptada. Las cardinalidades de clases CMP/PAR/RUL y el roster mínimo de servicio no bastan para definir pertenencia P* por UE. IAM y evidencia material no están sellados.

Siguiente: **C1.4**, crosswalk de predicados/filas IAM pre-Z en `C_SRC` contra App, C_dep y A_f, con boundary P0/P1/DUAL, obligatoriedad, estados y evidencia. Sin IAM ficticio, freeze ni ejecución.


## 16.153 — C1.4: crosswalk IAM/C_SRC y bloqueo material (2026-11-11)

`C10_S_C1_PREZ_IAM_CROSSWALK_C10S_001.md` establece el crosswalk lógico por CMP/PAR/REF/RUL/MET y separa E_scope, App, C_dep, A_f, F_alt, Need_preZ y E_req_preZ. No existen snapshots C10-S observados ni filas IAM/coverage materiales; las etiquetas 7×5 son planificación, no registros. Dictamen **PARTIAL / MATERIAL BLOCKED BY ABSENT IAM AND SNAPSHOTS**. No se puede clasificar población ni declarar REF=0.

`E_i=E_scope∧App*(τ2,S0)` continúa como propuesta no aceptada. Siguiente: **C1.5**, cerrar App y su frontera con A_f, rol de E_scope, regla pre-Z para unknowns, asignación D2 y soporte. Sin freeze ni ejecución.


## 16.154 — Protocolo de cinco paquetes integrados y resolución en ciclo único (2026-11-11)

Se adopta como método operativo `C10_S_INTEGRATED_WORK_PACKAGES_AND_CYCLE_PROTOCOL_DRAFT_001.md`. El cierre se organiza en cinco paquetes: **PA** contrato causal C1/población/Outcome/Value; **PB** material D2/servicio B1/primera etapa C2; **PC** atribución de accesibilidad C3/mediación C4; **PD** DGP/mecanismos C5/evaluación adversarial; **PE** especificación técnica integrada e implementación autorizable.

Cada paquete debe resolverse integralmente en una única iteración o conversación, con reconstrucción histórica, reconciliación de todas sus dimensiones, síntesis única, clasificación de decisiones y bloqueos, persistencia cruzada y relectura/verificación de todos los artefactos modificados. No se fragmentará en micro-preguntas. Solo se consultarán decisiones científicas genuinamente no derivables; la falta de evidencia se registrará como bloqueo, no como preferencia ni supuesto.

Orden: PA → PB → PC → PD → PE. El paquete activo es PA. La precedencia P*_{τ2}/P*_F está aceptada y no se reabre. El crosswalk IAM/C_SRC ya documenta ausencia de IAM y snapshots materiales; debe reutilizarse como bloqueo vigente. Esta organización no implica freeze ni autoriza código, fixtures, simulación o ejecución: `scientific_execution=false`, `execution_authorized=false`.


## 16.155 — PA: reconciliación integral de C1 (2026-11-11)

El paquete PA se resolvió en una única iteración y queda desarrollado en §15 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`. Dictamen: **PA_RECONCILED_DOCUMENTALLY / C1_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN**.

Se consolidan como contrato de trabajo: D2 sigue siendo el contraste de asignación aceptado; C1 es efecto total de política/paquete y familia de ITT por variante × población × resultado/dimensión × horizonte; P*_{τ2} es población objetivo primaria candidata y P*_F subpoblación secundaria ya aceptadas; eventos post-Z no redefinen inclusión; Outcome técnico A y Value contextual B permanecen separados; Value conserva vector P179 sin escalar/pesos arbitrarios; H=3 es profundidad, no duración; truth DGP y clasificación observada permanecen segregadas.

La fórmula `E_i=E_scope∧App*(τ2,S0)` no se acepta. Se registra como recomendación de trabajo distinguir E_scope como gate de alcance del universo DGP y App como aplicabilidad semántica focal, manteniendo C_dep,0=0 y A_f,0*=0 como condiciones separadas de P*τ2. Sin IAM/C_SRC y snapshots materiales no se adjudica E_i ni se estima la población/soporte. UNKNOWN pre-Z no se recodifica como cero ni se excluye silenciosamente; debe resolverse antes de Z o conservarse en un marco observable con estimando/cotas explícitos.

Bloqueos materiales: asignación D2 (ratio/probabilidades, estratos, algoritmo/semilla/provenance); aislamiento UE/UA y no interferencia; q_X*/positividad/soporte; horizonte y ventanas; ficha operacional de O-CONF u Outcome alternativo; instancia B1, consecuencia y fichas V_j; medición/missingness/censura y precisión. No se han inventado valores ni se solicita decisión de preferencia al usuario en este ciclo.

**Estado:** PA reconciliado documentalmente, no cierre científico de C1. Próximo paquete operativo: **PB — D2 material, servicio B1 y primera etapa C2**. PA se reabrirá solo para integrar material nuevo que levante los bloqueos, no para repetir la reconciliación. Sin freeze, implementación ni ejecución.


## 16.156 — PB: material D2, servicio B1 y primera etapa C2 (2026-11-11)

PB se resolvió en una única iteración integral. Dictamen: **PB_RECONCILED_DOCUMENTALLY / D2_C2_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN**. Registro completo: maestro C10-S §267.

Se reutilizan sin reabrir DEC-C10-066/067 (D2 primario, D1 secundario; política material y límites de B), DEC-C10-068/069 (servicio lógico, CMP/PAR/RUL, identidad y versionado), DEC-C10-095 (A/B), y decisiones B1 de modalidad de petición, una B1/UE, una oportunidad estandarizada/UE, enlaces request↔trajectory y adjudicación causal. La provisión D2 se delimita a P1, manteniendo P0, F*, oráculo, autorización normativa basal y rutas no focales invariantes por diseño. La frontera P0/P1/P2, el crosswalk de A_f* y la secuencia de medidas C2 quedan integrados en §267.

C2 no se declara cuantitativamente establecida: W_programmed, W_attempt, S_install, C_dep*, A_f*, D_f*, ΔT_acc*, E_T/ΔE_T y Reach/Π permanecen separados. s=0.80 no está validado; D_f_obs no sustituye D_f*; Wald/LATE bloqueado. No existe inventario B-M01…15, instalación, IAM/snapshots completos, prueba de aislamiento, no-afectación A1/A2/F2 ni validación observacional.

**Decisión única pendiente para armonizar identidades:** mantener contract_id/version y CMP de referencia comunes, interpretar C10S-SVC-REQUEST-PROCESSOR-001 como instancia ejemplar y asignar instance_id único/versionado por UE, con component_id local a la instancia y clave compuesta. Recomendación: sí, para respetar el aislamiento por UE ya aceptado. No se ha aplicado ni congelado hasta aceptación expresa.

Siguiente paquete: **PC — atribución de accesibilidad C3 y mediación C4**. PB no se repite; se reabre solo si se acepta la decisión de identidad o aparece evidencia material nueva. Sin implementación/fixtures/simulación/ejecución; scientific_execution=false; execution_authorized=false.


## 16.157 — PC: atribución C3 y mediación C4 (2026-11-11)

PC completó una reconciliación integral en una iteración. Dictamen: **PC_RECONCILED_DOCUMENTALLY / C3_C4_NOT_IDENTIFIED_IN_CURRENT_D2_MATERIAL / NOT_DESIGN_FROZEN**. Registro rector: maestro C10-S §268.

Se conserva la jerarquía no intercambiable C1 ITT_Z^D2/efecto de política, C3 general θ_A(q), C3 focal θ_Af(q_X*), LATE_f^D2 y C4 mediación interventional. D2 no equivale a g^Af: B asigna una política material de provisión, no ΔT_acc*. El mapping B_D2→g^Af, q_X*, soporte/positividad por historia, ausencia/separación de vías colaterales, aislamiento y medición siguen sin demostración. El ITT permanece efecto de política/paquete si hay vías paralelas.

El mediador C4 es ΔT_acc* completo; Reach_H/Π_H son mediadores secuenciales posteriores o bloque conjunto solo con intervención y orden definidos. A_f* es proyección/predicado dentro de T_acc y D_f* indicador derivado, no mediadores seriales. Si Z induce confusores postratamiento del vínculo mediador–Value, el ajuste convencional no identifica mediación; se requiere estrategia longitudinal/interventional o dictamen de no-identificación. No se define residual por resta automática.

No hay Value contextual instanciado: ninguna dimensión V_j ni beneficiario/perspectiva/regla de valoración está materialmente definida; O-CONF sigue candidato no operacionalizado. Los dictámenes C3/C4 para Value son NOT IDENTIFIED/NOT EVALUABLE en el estado actual. P177/P178/P179/P182/P183 y DAG/CAUS existentes se reutilizan; C-MED permanece PARCIAL/OPEN, sin crear IDs duplicados.

Siguiente paquete: **PD — DGP, mecanismos C5 y evaluación adversarial**. No reabrir PC salvo evidencia nueva o contradicción material. Sin Design Freeze, fixtures, código, simulación ni ejecución; scientific_execution=false; execution_authorized=false.


## 16.158. Reconciliación integrada PD — DGP, mecanismos C5 y evaluación adversarial (2026-11-11)

**Estado:** PD_RECONCILED_DOCUMENTALLY / DGP_QUANTITATIVE_SPECIFICATION_OPEN / NOT_DESIGN_FROZEN. Referencia rectora del paquete: C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md.

La reconciliación reutiliza la matriz temporal de predicados, inventario finito de DGP/Reach, contratos S4R, MEAS, MISS, POL, VER, TRJ, INT, GEN, PM, SNAP, REACH, PROV, GC y U_G, y P177/P178/P179/P182/P183. No crea familias duplicadas. Integra tres planos computacionales: truth_dgp (potenciales, estados, mecanismos y contribuciones verdaderas, ocultos al Analyzer), observed_evidence (registros/cobertura/error/missingness disponibles al Analyzer) y evaluation/adjudication (comparación posterior con truth tras sellar la salida). La cobertura epistémica no altera la verdad estructural.

C5 se adjudica por etapa concreta del ciclo de petición —opportunity, attempt, received, admitted/rejected, processing, response— mediante contraste contrafactual explícito y propiedad de trayectoria preespecificada. Se preservan NECESSARY_CONTRIBUTION, ENABLING_CONTRIBUTION y MODIFYING_CONTRIBUTION conforme a DEC-C10S-B1-CAUSAL-ADJUDICATION-001; pueden coexistir y no implican Outcome favorable ni Value. TEMPORAL_ASSOCIATION, TRACEABILITY_LINK y CAUSAL_CONTRIBUTION permanecen distintos conforme a DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001.

La cobertura adversarial mínima incluye efectos focales positivos/nulos/adversos, fallos parciales, vías directas y colaterales, interacciones, heterogeneidad, weak/null IV, defiers, interferencia, alternativas, crossover/versiones, observación diferencial, peticiones/contribuciones múltiples, falta de soporte, missingness MCAR/MAR/MNAR, censura y selección post-Z. P177–P183 se evalúan por estimando y dimensión; N/R, potencia, precisión y SE_MC requieren especificación ex ante. N=2.000, 1:1 y R=1.000 son ilustrativos, no aprobados.

**Bloqueos:** Value no instanciado por PA; Outcome no operacionalizado; falta IAM/snapshots/inventario material D2; θ_A(q), θ_Af(q_X*) y mediación siguen no identificados en D2 actual según PC; parámetros conjuntos, contrastes contrafactuales concretos, soporte, interferencia, F*/G/H/ventanas y estadística cuantitativa siguen abiertos. Nota histórica supersedida (2026-11-11): la lectura Contents devolvía contenido vacío, pero el blob Git se recuperó íntegramente. El maestro fue actualizado en §274; véase la corrección de recuperación y el artefacto rector de factibilidad. La incidencia ya no es un bloqueo.

No se autoriza código, fixtures confirmatorios, generación de datos, simulación, estimación ni ejecución científica. Siguiente paquete PE; preparación conceptual de interfaces solamente, hasta cerrar los requisitos científicos y recibir autorización expresa.

## 16.159. Reconciliación integrada PE — especificación técnica y contrato de implementación (2026-11-11)

**Estado:** PE_RECONCILED_DOCUMENTALLY / TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY / NOT_IMPLEMENTED / NOT_EXECUTED. Artefacto rector: C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md; maestro §270.

PE reutiliza DGP temporal/roles, U_G, plantilla/protocolo de evidencia, identidad/versionado/snapshot matching, snapshot/delta, manifiesto B, Decision Log y Test Contract Register. Define seis responsabilidades lógicas (Orquestador, Generator, Proyector/Sealer, Analyzer, Evaluator/Adjudicator y Artifact/Provenance Store), contratos de intercambio y firewall truth_dgp/observed_evidence/evaluation. No crea un segundo modelo de datos ni nuevos IDs de prueba. Preserva identidades TID/SID/RID/EID, object_record_id/version, snapshot exacto, request_id/trajectory_id, estados trivalentes y los ejes temporales diferenciados.

DEC-C10-074/JCS solo rige el envelope U1 de UDG-01; no se generaliza a todos los registros. El esquema físico, serialización de bundles/eventos, motor, cardinalidades, almacenamiento, permisos, secretos, retención y contrato final del Analyzer siguen OPEN. U_G SR-01…20 conserva 8 PASS_STATIC, 10 CONDITIONAL y 2 NOT_ASSESSED; SR-13 sigue CONDITIONAL y SR-19/20 NOT_ASSESSED.

Gates para implementación: G-SCI, G-MAT, G-SCHEMA, G-ROLE, G-TEST, G-REPRO y G-AUTH. PA–PD mantienen bloqueos de Value/Outcome, IAM/snapshots/material D2, mapping B→g^Af, colaterales, soporte/interferencia, parámetros DGP, contrastes, fixtures, N/R, potencia y tolerancias. PC no identifica θ_A(q), θ_Af(q_X*) ni mediación en el D2 material actual.

**Resultado:** PE reconciliado documentalmente; contrato técnico parcial; implementación no lista, no implementada ni ejecutada. No se crea decisión científica nueva ni se autoriza código/fixtures/simulación/ejecución. scientific_execution=false; execution_authorized=false.


## 16.160. Decisión aceptada de identidad de instancia B1 por UE (2026-11-11)

Se acepta `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001`. El contrato funcional `C10S-SVC-REQUEST-PROCESSOR` v`1.0.0` y la plantilla CMP/PAR/RUL son comunes; cada UE tendrá `instance_id` único y `instance_version` independiente. `component_id` es local a la instancia y su clave inequívoca es `(instance_id, component_id)`. El ID `C10S-SVC-REQUEST-PROCESSOR-001` queda como instancia ejemplar de referencia DEC-C10-069.

Queda resuelta la identidad lógica/documental, no el aislamiento material. Siguen abiertos el roster final y asignación de IDs por UE, IAM/ACL, recursos/estado compartido, evidencia de no interferencia, MET/schema físico y pruebas. No se altera A ni DEC-C10-069 en su alcance original. No se autoriza implementación ni ejecución.


## 16.161. Reconciliación material PB — identidad B1 por UE y aislamiento D2 (2026-11-11)

**Artefacto rector:** `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md`. **Estado:** PB_MATERIAL_CONTRACT_RECONCILED_DOCUMENTALLY / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / NOT_DESIGN_FROZEN.

Se integra DEC-C10-067 con la decisión aceptada de identidad B1 por UE, el overlay IAM/U_G, B-M01…15, PROV-01…12, snapshots exactos y rutas A1/A2. Se cierra la armonización lógica entre contrato/plantilla CMP común e instancia única/versionada por UE. El adaptador/dependencia focal P1 se mantiene distinto del servicio lógico CMP. D2 opera en P1; P0, F*, oráculo, mapping semántico, autorización normativa basal y alternativas deben permanecer invariantes por diseño, sujetas a evidencia.

**No materializado:** roster e IDs por UE; IAM/C_SRC; snapshots; inventario de dependencias/consumidores; artefacto/runtime/version/hash; actor y recepción; ventanas/reintentos/rollback; ACL y recursos; no-afectación A1/A2; evidencia C_dep*/A_f*/D_f*/ΔT_acc*; soporte/interferencia. B-M13/F* y B-M14/A1-A2 permanecen prohibidos como superficies modificadas por B. NO INVENTARIADO/UNKNOWN no equivale a ausencia.

**Dictamen:** reconciliación documental del contrato material completada; PB material y G-MAT siguen bloqueados. No se declara D2 aislado, primera etapa focal ni IV válido. No se autoriza captura, implementación, fixtures, simulación, estimación o ejecución.

## 16.162. B2–B3 — reconciliación de B1, Outcome técnico y Value contextual (2026-11-11)

**Artefacto rector:** `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md`. **Estado:** B2_B3_WORKING_BASIS_ACCEPTED / SEMANTIC_RECONCILIATION_DOCUMENTED / OUTCOME_NOT_OPERATIONALIZED / VALUE_NOT_INSTANTIATED / NOT_DESIGN_FROZEN.

Se acepta como base de trabajo que B1 es la entidad sintética cuyo Need_preZ antecede a Z; Outcome mide un resultado técnico del servicio/proceso; Value valora la consecuencia para B1 respecto de Need_preZ desde perspectiva/autoridad ex ante. La consecuencia puede depender de Outcome y de otras vías; no se impone Outcome→Value exclusivo ni V_j=f(Outcome). Se mantienen separados Need_preZ, Request_event, D_resource, procesamiento, Outcome, consecuencia y Value.

Se reutilizan DEC-C10-095, B1 por UE, oportunidad estandarizada por UE, identidad/versionado de servicio y contratos §224/P179/P182/P183. O-CONF es el candidato técnico mejor anclado, no operacionalizado. P179 mantiene vector y trade-offs; no se eligen dimensiones históricas ni pesos por defecto. Cada O_k/V_j requiere ficha §224 independiente; no hay transferencia de identificación Outcome→Value ni entre dimensiones.

**OPEN:** instancia/provenance material B1; contenido/medición Need_preZ; perspectiva/autoridad; consecuencia e horizonte; selección justificada de O_k/V_j; fuentes, escalas, baseline, adjudicación, error, missingness/censura; vías causales y soporte. C3/C4 permanecen no identificados en D2 material actual. No se modifica A, D2, P*τ2/P*_F, Core, RMA, Matrix, STATUS o claims. Sin Design Freeze, implementación, fixtures, simulación, estimación o ejecución.


## 16.163. Reconciliación integrada de factibilidad confirmatoria y Design Freeze (2026-11-11)

**Artefacto rector:** C10_S_INTEGRATED_CONFIRMATORY_FEASIBILITY_AND_DESIGN_FREEZE_RECONCILIATION_DRAFT_001.md. **Estado:** INTEGRATED_RECONCILIATION_COMPLETED / CONFIRMATORY_FEASIBILITY_NOT_ESTABLISHED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

Se integran en una sola evaluación los resultados PA/C1, PB/PB-MAT, PC/C3-C4, PD/DGP, PE, identidad B1 y B2–B3. No se reinician paquetes ni se reabren decisiones aceptadas. D2 permanece escenario primario candidato y D1 secundario; P*τ2 es población primaria candidata y P*_F subpoblación secundaria; B1 y oportunidad única por UE conservan su alcance aceptado.

**Dictamen conjunto:** no existe todavía un diseño confirmatorio materialmente identificado ni listo para Design Freeze. El mecanismo material de asignación D2 (ratio/probabilidades, estratos, algoritmo/semilla y desviaciones) no está especificado; q_X*/q_L*, positividad y soporte no están materializados. La unidad UE=UA depende de aislamiento que no está demostrado; si existen recursos/agentes/estado/canales compartidos debe considerarse clúster/exposición. IAM/C_SRC, roster, snapshots, inventario B, grafo transitivo, ACL/recursos, provisión/crossover y no-afectación A1/A2 siguen ausentes. Outcome carece de ficha §224 completa y Value no está instanciado; no hay Y_j confirmatorio completo.

ITT de política/paquete, primeras etapas técnicas/focales, θ_A/θ_Af, LATE_f, IIE C4 y efecto directo/residual se mantienen como estimandos separados. Ninguno está identificado/evaluable con el estado material actual. No se calculan cotas numéricas porque faltan cobertura, parámetros y restricciones justificadas; cotas/sensibilidad quedan como opción futura, no como resultado actual. Outcome y Value permanecen distintos y no se impone V_j=f(Outcome) ni una vía causal exclusiva Outcome→Value.

**Gates:** G-SCI, G-MAT, G-SCHEMA, G-ROLE, G-TEST y G-REPRO BLOCKED; G-AUTH NOT GRANTED. El maestro C10-S Nota histórica supersedida por recuperación del blob Git: el contenido completo de §§266–273 fue inspeccionado y §274 añadido al mismo maestro. La reconciliación queda contrastada con el maestro recuperado; no se realizó validación local ni CI.

No se modifica main/Core/RMA/Matrix/STATUS/claims ni decisiones aceptadas. No Design Freeze, captura material, schema físico, fixtures, implementación, simulación, estimación o ejecución. scientific_execution=false; execution_authorized=false.

## Corrección de recuperación del maestro C10-S — 2026-11-11

La lectura inicial del maestro mediante Contents devolvía contenido vacío, pero el blob Git fue recuperado íntegramente (1,134,655 caracteres / 12,136 líneas) e inspeccionados sus §§266–273. La incidencia está **RESUELTA**; el documento no estaba perdido. Se ha añadido §274 al maestro con la reconciliación integrada de factibilidad y Design Freeze. No queda pendiente recuperar el maestro; permanecen los bloqueos científicos/materiales y los gates indicados en el artefacto rector. La limitación de concordancia línea por línea por inaccesibilidad del maestro queda superada para el contenido recuperado; no equivale a validación local ni CI.


## 16.164. Reconciliación integrada D2 — asignación, población y soporte (2026-11-11)

**Artefacto rector:** C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md.

Se cierra la reconciliación documental de las distinciones del contrato D2: P(Z=1 | estrato,UA) es asignación experimental y permanece sin mecanismo/ratio/estratos/algoritmo/semilla; las reglas W_programmed D2 condicionales a Z (0/1) son política aceptada y no asignación. Cumplimiento/recepción, provisión de fondo y s=0.80 siguen abiertos/no aprobados.

Se preservan P*τ2/P*_F y los límites de E_i/App, C_dep,0/A_f,0*, estados UNKNOWN pre-Z, q_X* como distribución basal objetivo, q_L* solo si se requiere régimen secuencial, y UE=UA condicionado a aislamiento. No se calculan población, positividad ni soporte sin IAM/C_SRC/snapshots/roster y truth/evidence por UE.

**Estado:** DESIGN_CONTRACT_RECONCILED_PARTIALLY / RANDOMIZATION_NOT_SPECIFIED / SUPPORT_NOT_ESTABLISHED / NOT_DESIGN_FROZEN. No nuevas decisiones ni autorización. scientific_execution=false; execution_authorized=false.


## 16.165. Reconciliación de operacionalización confirmatoria Outcome/Value (2026-11-11)

**Artefacto rector:** `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md`; maestro §276.

F* se conserva como criterio funcional de ruta completa; O-CONF como resultado adjudicado del estado de conformidad del destino, sin duplicar F* como segundo endpoint. O-CONF es candidato prioritario, no confirmado/operacionalizado: predicados atómicos, mapping/IAM, C0/G/H, snapshots, evento terminal y oráculo independiente validado siguen OPEN. FP-08 permanece gate probatorio separado.

Value se mantiene vectorial P179. B1/Need_preZ y perspectiva B1 son base semántica; autoridad/criterio y consecuencia, dimensiones k/V_j, fuentes, escalas, baseline y horizonte siguen OPEN. No se seleccionan dimensiones históricas, pesos ni agregación por defecto. P179/P182/P183, §224 y MEAS/MISS se reutilizan sin nuevos IDs.

**Estado:** MEASUREMENT_ARCHITECTURE_RECONCILED / NO_CONFIRMATORY_Y / NOT_DESIGN_FROZEN. ITT por O/V separados; C3/C4 no identificados. Sin captura, schema, fixtures, implementación, simulación o ejecución.



## 16.166. P178 Analyzer Monte Carlo — cierre de replay limpio (2026-11-12)

**Artefacto rector:** `03_EXPERIMENTS/C10-S/harness/P178_CLEAN_REPLAY_CLOSURE_AUDIT_001.md`. **Estado:** COMPUTATIONAL_REPRODUCIBILITY_CLOSED / PASS / NON_CONFIRMATORY.

El replay limpio `43120303588` completó las 27 celdas × 10.000 réplicas (270.000 invocaciones), usando el commit fuente primario exacto `689c8f0164e0625ca536a20b1805e555cd63d5fd`, Python 3.12.16, NumPy 2.3.5 y SciPy 1.17.0. Las 17 pruebas de contrato pasaron; las 27 celdas reprodujeron la referencia; no hubo réplicas inválidas, errores de clasificación ni abstenciones focales inesperadas.

El CSV y el manifiesto del replay son byte-identical a los del primario: SHA-256 CSV `e73a204b6ffc3ff4666c37d9a3e2d5ff4612a3d0602a25349cbb8bc12287914f`; SHA-256 manifiesto `72aed4c8bbe30a20cdb20e3b1c2d27f38e046687b100349f94b99aaed9f04294`. El workflow emitió `CLEAN_REPLAY_BYTE_IDENTICAL=PASS`; duración del job 23 min 25 s. Artefacto replay ID `13901876197`, SHA-256 ZIP `a72922ca51dc5afb713edcb35932dc1598d535f77abe9af6aaa8f3ed1b83e4de`.

**Consecuencia:** se cierra la reproducibilidad computacional del benchmark P178 acotado. No se amplía su dominio de validez: siguen fuera weak-signal, vías directas, fallo de positividad, medición degradada, interferencia y abstención bajo no-identificación. No se valida la afirmación causal/value general ni la factibilidad confirmatoria C10-S. No se modifica el Analyzer; el probe de caché exacta permanece NO-GO. No se modifica `main`, RMA, Matrix, STATUS, Core ni claims; no se concede autorización adicional de ejecución.

**Siguiente continuidad científica:** reanudar el cierre documental de Need_preZ sin recrear artefactos ya existentes. El protocolo U_G §3–7 ya define S1–S8, provenance, cobertura por dimensión/denominador y reglas 1/0/?; el inventario Need_preZ ya contiene el crosswalk de fuentes candidatas y el dictamen COVERAGE_NONE / observed ? / BLOCKED. Por tanto, no procede duplicar un catálogo genérico. La brecha residual es material: roster B1/UE/instancia, objetivo basal individual pre-Z, fuentes admisibles versionadas y cobertura por unidad. Su captura/materialización requiere un alcance y autorización específicos; no se infiere de este cierre P178.


## 16.167. Contrato mínimo de materialización DGP de Need_preZ (2026-11-12)

**Artefacto rector:** `C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md`.

Se especifica la separación por unidad entre (i) truth Need_preZ reservada al generador, (ii) fuentes/evidencia pre-Z accesibles al adjudicador y (iii) clasificación observada 1/0/?. Se fija el binding lógico UE↔B1↔service instance versionado, sin asignar IDs ni crear roster. Se establecen requisitos de ancla temporal pre-Z, fuente semánticamente pertinente al objetivo B1, manifiesto de fuentes/cobertura, provenance, E1/E2 y evaluación truth-vs-observed solo después de sellar la salida observada.

Se prohíbe inferir Need desde configuración técnica, ausencia de documento/solicitud, oportunidad estandarizada, Request_event, C_dep, A_f, Reach, Outcome o Value. En particular, observed=0 requiere evidencia afirmativa y cobertura negativa suficiente; un universo de documentos sin declaración no prueba por sí solo ausencia del objetivo. No se asigna Need=1 por defecto. Truth=?, missingness y observed=? permanecen diferenciados.

**Estado:** DOCUMENTARY_SPECIFICATION / NOT_APPROVED / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED. Prevalencia, mecanismo generador de truth, modelo de observación/error/missingness, fuentes concretas, roster, denominador y cobertura siguen OPEN/NONE. Se reutilizan EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_REGISTER y ADJUDICATION_REGISTER; no se crea tabla U_G ni clase de objeto. No se implementa ni ejecuta DGP; no se autoriza fixture, captura, simulación o Design Freeze. `scientific_execution=false`; `execution_authorized=false`.


## 16.168. Auditoría de compatibilidad Need_preZ ↔ DGP temporal/U_G (2026-11-12)

**Artefacto rector:** `C10_S_B1_PREZ_DGP_U_G_COMPATIBILITY_AUDIT_DRAFT_001.md`.

La separación conceptual truth/evidencia/adjudicación, la procedencia EVIDENCE_REGISTER, el almacenamiento segregado DGP_TRUTH_SECURE y la regla trivalente son compatibles en principio. Se identifica un bloqueo de representación: CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER solo admiten targets NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE. Need_preZ es una afirmación basal sobre B1/UE y no debe forzarse a PREDICATE (predicado de ruta) ni a COVERAGE_SCOPE (universo/denominador). Los scopes C10S_CONFIG_* cubren configuración técnica, no el objetivo B1.

El reloj t−1→t0 aporta precedencia temporal, pero Need no figura expresamente en el diccionario variable×tiempo×rol. El contrato Need deberá vincularse a t−1 y separar Need_truth reservada, Need_evidence y Need_observed. El target de claim/evaluator/adjudication y la cobertura específica del objetivo B1 requieren decisión de representación antes de schema o fixtures.

**Estado:** PARTIAL_COMPATIBILITY / U_G_TARGET_TYPE_GAP_OPEN / NO_SCHEMA_CHANGE / NOT_IMPLEMENTED / NOT_EXECUTED. Se prohíbe añadir enums/tablas/FK o asignar IDs sin decisión; no se selecciona todavía entre claim extension, registro B1 separado o artefacto analítico externo. La siguiente dependencia es inspeccionar el contrato canónico de claims y las decisiones U_G de tipos de target.


## 16.169. DEC-C10-061 y destino de adjudicación Need_preZ (2026-11-12)

La revisión de `C10_S_UG_TYPED_TARGET_REFERENTIAL_INTEGRITY_CONTRACT_PROPOSAL_DRAFT_001.md` y DEC-C10-061 confirma que los seis destinos U_G son un enum cerrado aceptado documentalmente. CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER no admiten B1/UE/Need; EVIDENCE_REGISTER es fuente de soporte, no target. Reutilizar PREDICATE o COVERAGE_SCOPE sería semánticamente incorrecto; ampliar targets reabriría DEC-C10-061.

**Orientación provisional:** estudiar un paquete analítico B1/Need separado de U_G, versionado, con procedencia/cobertura y separación truth/observed propias, sin añadir clase de grafo ni cambiar enums. Antes de fijar su representación se debe comprobar el contrato canónico de claims y si requiere vínculo de matriz adicional. No se aprueba todavía la opción ni se crea schema/fixture. El contrato temporal sigue Draft y Need no está aún incorporado expresamente al diccionario variable×tiempo×rol.

**Estado:** U_G_TARGET_ENUM_CLOSED / NEED_TARGET_NOT_SUPPORTED / SEPARATE_ANALYTIC_PACKAGE_PREFERRED_FOR_REVIEW / NO_SCHEMA_CHANGE / NOT_IMPLEMENTED / NOT_EXECUTED.


## 16.170. Need_preZ: límite de Evidence→Claim Matrix y representación analítica local (2026-11-12)

La revisión de `EVIDENCE_TO_CLAIM_MATRIX_v1.47.md` confirma que la matriz registra claims científicos C01–C16, no adjudicaciones de variables por unidad; `Need_preZ` no figura como claim. Need es constructo basal del diseño C10-S, no una nueva afirmación teórica TGCV. No se crea C17 ni se modifica la Matrix por este trabajo, ni se propaga evidencia a C10.

Combinado con DEC-C10-061 (targets U_G cerrados), el camino de menor impacto es mantener truth/evidencia/adjudicación Need como paquete analítico local del DGP, fuera de U_G y de la Matrix global, versionado y con IDs/hashes/provenance propios. No se implementa ni se materializa todavía; su contrato de campos debe someterse a revisión antes de fixtures. Solo una evidencia futura que afecte una afirmación científica existente activará el proceso de impacto habitual.

**Estado:** NEED_LOCAL_DGP_CONSTRUCT / NO_GLOBAL_CLAIM / U_G_TARGET_CLOSED / SIDE-PACKAGE_ROUTE_PREFERRED / NOT_APPROVED / NOT_IMPLEMENTED / NOT_EXECUTED.


## 16.171. Continuidad de C10-S y aplazamiento del playground (2026-11-12)

**Origen:** conversación de continuidad del 2026-11-12; orientación explícita del usuario: guardar esta aclaración en GitHub y centrar ahora el trabajo en el experimento causal sintético.

**Aclaración de alcance:**
- C10-S conserva su naturaleza de experimento causal sintético. No se ampliará para convertirlo en una simulación exhaustiva o realista de una migración informática.
- El caso de migración de configuración entre entornos sigue siendo un microdominio instrumental del DGP; su detalle operativo solo se añadirá cuando sea necesario para definir una intervención, mecanismo causal, medición, amenaza a identificación o criterio falsable.
- El playground TGCV, cuando se retome, probablemente requerirá un escenario operativo más desarrollado y una simulación interactiva que permita explorar estados, transformaciones, restricciones, rutas, trayectorias, resultados y valor contextual. Ese nivel de detalle pertenece a la línea de playground, no al núcleo confirmatorio de C10-S.
- No se presupone que el motor experimental C10-S sea por sí solo el motor operativo completo del playground. Se evaluará la reutilización de componentes compatibles (p. ej., representación de estados/transformaciones, trazabilidad, ejecución de escenarios y registro de resultados) y, si procede, se construirá una capa operativa diferenciada. La arquitectura compartida se decidirá por compatibilidad real, no por anticipación.
- No se iniciarán ahora diseño detallado, implementación ni simulación del playground. La línea queda aparcada para retomarla expresamente más adelante.

**Regla de contención para C10-S:** no incorporar complejidad contextual por realismo narrativo. Un componente solo se añade si es necesario para la verdad del DGP, intervención, estimando, observación/medición o evaluación; resuelve una amenaza causal/metrológica concreta; y tiene consecuencia falsable o criterio explícito de bloqueo. Las extensiones que no superen ese filtro quedan fuera del núcleo mínimo o se reservan como sensibilidad/extensión justificada.

**Continuidad inmediata:** reanudar la auditoría integrada de suficiencia del diseño causal mínimo C10-S sobre los contratos existentes, reutilizando el trabajo histórico y sin recrear artefactos. Revisar D2 primario/D1 secundario, asignación e intervención, población/unidad/soporte/interferencia, separación T_acc–Reach–trayectoria–ejecución–Outcome–Value, ITT y atribución focal/mediación, vías directas/alternativas, DGP truth frente a evidencia observada, estimadores/oráculos, sensibilidad y condiciones de no-identificación. B1/Need_preZ/S7 se mantendrán solo en la medida en que resuelvan una necesidad real del diseño o de su medición; no se expandirán por realismo del microdominio.

**Límites y estado:** esta entrada registra una orientación de continuidad, no una nueva decisión causal aceptada, no congela el diseño ni cambia estimandos, parámetros, DGP, contratos normativos, claims, Core, RMA, Matrix o STATUS. No autoriza implementación, simulación, validadores ni ejecución científica. scientific_execution=false; execution_authorized=false.



## 16.172. Secuencia integrada de cierre confirmatorio y reducción de iteraciones (2026-11-12)

**Origen:** instrucción explícita del usuario de registrar en este plan la secuencia de cierre propuesta para C10-S y abordarla en el mínimo número de interacciones posible.

### 16.172.1. Regla de trabajo

La prioridad deja de ser ampliar/reconciliar repetidamente componentes aislados y pasa a convertir el diseño existente en una especificación experimental cuantitativa, identificable y evaluable. Se reutilizan los contratos, decisiones, matrices y pruebas existentes. No se recrean cuestiones ya cerradas ni se reabren por falta de contexto conversacional.

La auditoría debe ser histórica e integrada antes de proponer cambios: cada requisito se clasifica como **CERRADO/REUTILIZABLE**, **ABIERTO CON DEPENDENCIA MATERIAL**, **BLOQUEADO POR EVIDENCIA/AUTORIZACIÓN** o **NO NECESARIO PARA EL NÚCLEO CONFIRMATORIO**. Una distinción conceptual ya aceptada no se presenta como trabajo pendiente; solo puede quedar abierta su materialización, mapping, parametrización o prueba, identificando exactamente cuál.

No se solicitará al usuario que vuelva a definir entidades, funciones, objetivos, distinciones o decisiones ya registradas. Las cuestiones resueltas se citarán desde su contrato rector. No se abrirán nuevos documentos, catálogos, test IDs o familias de pruebas cuando los artefactos existentes admitan una actualización trazable.

### 16.172.2. Orden de cierre y dependencias

El cierre se organiza en seis bloques dependientes, en este orden:

1. **A — Outcome y Value confirmatorios.** Reutilizar los contratos B1/B2–B3, Outcome/Value y P179. Completar, sin duplicar constructos, el resultado técnico adjudicable (O-CONF/F* sin doble conteo) y el resultado de valor contextual independiente: perspectiva/autoridad de valoración, consecuencia, horizonte, dimensiones V_j estrictamente justificadas, indicadores, escalas, baseline y regla de adjudicación. No seleccionar dimensiones, pesos, agregaciones ni escalas por conveniencia. Si el mínimo no puede justificarse sin circularidad o arbitrariedad, registrar el bloqueo concreto y su consecuencia para el alcance confirmatorio.
2. **B — Intervenciones y estimandos.** Reutilizar C1, C3, C4, D2/D1 y las reconciliaciones causales vigentes. Cerrar por separado: ITT de asignación D2 como efecto de paquete; primeras etapas; efecto focal/general de accesibilidad; mediación interventional; efectos directos/residuales y vías alternativas. Especificar qué intervención identifica cada estimando, población, horizonte, supuestos, soporte y criterio de identificación/no-identificación. No transferir identificación desde ITT D2 a accesibilidad ni derivar residuales por resta ad hoc. Si el mapping D2→g^Af no queda demostrado, mantener separados el efecto de paquete y la atribución a accesibilidad.
3. **C — DGP causal cuantitativo.** A partir de A y B, cerrar ecuaciones/reglas estructurales, orden temporal, variables y relaciones generadoras, contrafactuales, truth por etapa, distribuciones y parámetros justificables. Incluir solo escenarios necesarios para evaluar recuperación y falsación: contribución positiva, nula y adversa de accesibilidad; vías directas/colaterales; interacción/heterogeneidad; confusión inducida; errores de medición/missingness/censura; interferencia o soporte insuficiente; y condiciones de no-identificación. Cada escenario debe tener verdad conocida, mecanismo explícito y dictamen esperado. No convertir el microdominio en una simulación de migración realista.
4. **D — Población, unidad y asignación material.** Cerrar roster sintético y elegibilidad basal, unidad de asignación/análisis, relación UE/UA/UO, mecanismo aleatorio, probabilidades por estrato, ratio derivado, algoritmo/semillas, soporte/positividad, interferencia, contaminación/crossover y horizonte. Distinguir reglas de política condicionales a Z de la probabilidad experimental P(Z=1|estrato, unidad), y distinguir asignación de cumplimiento/recepción/éxito. No presumir 1:1, tasas, prevalencias ni tamaños muestrales. Los datos materiales de IAM/snapshots/provisión solo se capturarán si existe autorización específica; no se infiere autorización de esta secuencia.
5. **E — Medición, observación y evaluación.** Cerrar mappings observables independientes para T_acc, Reach, trayectoria, ejecución, Outcome y cada V_j; modelo de medición, cobertura, error, missingness/censura y procedencia. Definir la frontera Generator–sealer–Analyzer–Evaluator: truth reservada, evidencia visible y outputs adjudicados separados. Reutilizar P177/P178/P179/P182/P183 y los contratos B1 ya existentes. Fijar métricas y tolerancias ex ante (sesgo, cobertura, error tipo I, potencia/precisión, recuperación de signo/magnitud, falsa atribución/mediación y abstención), con justificación y reglas para IDENTIFIED / BOUNDS_ONLY / NOT_IDENTIFIED / BLOCKED. No tratar el PASS computacional de P178 como validación causal de C10.
6. **F — Contrato ejecutable y gates.** Integrar las especificaciones cerradas en interfaces/versiones de Generator, Analyzer y Evaluator, schema/modelo físico, manifests, provenance, hashes, entorno y comandos. Reconciliar G-SCI, G-MAT, G-SCHEMA, G-ROLE, G-TEST y G-REPRO; solo después valorar Design Freeze. G-AUTH sigue siendo un gate separado: esta entrada no autoriza implementación, captura, fixtures confirmatorios, simulación ni ejecución científica.

### 16.172.3. Modo de trabajo para minimizar interacciones

Los seis bloques se trabajarán en **tres pasadas integradas**, sin pedir confirmación al usuario entre subapartados que ya estén gobernados:

- **Pasada 1: A+B.** Outcome/Value y estimandos/intervenciones se revisan conjuntamente para evitar definir el resultado sin saber qué efecto debe identificar, o viceversa. Entrega: crosswalk de decisiones ya cerradas, gaps estrictamente materiales y propuesta completa de cierre.
- **Pasada 2: C+D.** DGP cuantitativo, población, unidad, asignación, soporte e interferencia se cierran conjuntamente, manteniendo sus dependencias explícitas. Entrega: especificación causal estructural y diseño de generación/asignación, con parámetros no justificables señalados como bloqueos y no inventados.
- **Pasada 3: E+F.** Medición, observación, oráculos, criterios de recuperación y contrato ejecutable se integran en una sola reconciliación. Entrega: matriz de aceptación por estimando/escenario y estado de gates.

Cada pasada debe consultar de forma exhaustiva los artefactos rectores y auxiliares pertinentes antes de formular conclusiones. El usuario recibirá una síntesis consolidada por pasada, no una sucesión de preguntas de detalle. Solo se interrumpirá para solicitar una decisión cuando exista una elección científica/normativa genuinamente no delegable, con alternativas, consecuencias y recomendación explícitas; las cuestiones técnicas derivables de contratos o evidencias se resolverán directamente y se documentarán. Si no hay decisión del usuario imprescindible, se continúa sin detener el flujo.

### 16.172.4. Regla de no-regresión y salida

- No reabrir la función operativa B1, el objetivo basal, la separación truth/evidence/adjudication, las definiciones de Reach, la distinción Outcome/Value, ni la jerarquía de estimandos cuando los contratos vigentes ya las fijan. Revisar solo inconsistencias demostradas o mappings/materializaciones aún abiertos.
- No ampliar B1/Need_preZ/S7, el microdominio, la taxonomía de errores ni la narrativa de migración salvo que una amenaza identificada a estimación, medición o evaluación lo exija.
- No crear un documento paralelo: esta sección del plan es el registro de la secuencia. Las modificaciones sustantivas posteriores se propagarán al contrato rector existente correspondiente, conservando trazabilidad.
- No fijar arbitrariamente Outcome/V_j, escalas, pesos, N/R, prevalencias, probabilidades, tasas de error, parámetros, semillas ni tolerancias. Toda elección cuantitativa deberá derivarse de estimando, soporte, análisis de potencia/precisión, sensibilidad y criterios de aceptación.
- Los estados de diseño, implementación, ejecución, auditoría y aceptación se mantendrán separados. No declarar Design Freeze ni PASS científico por completar esta secuencia documental.

**Estado al registrar:** secuencia y método de trabajo aceptados como orientación operativa para el cierre documental; A–F no se declaran cerrados por esta entrada. No cambia ningún estimando, decisión causal, claim, Core, RMA, Evidence→Claim Matrix o STATUS. No se autoriza implementación, captura, validadores locales, generación de datos, simulación, estimación ni ejecución. `scientific_execution=false`; `execution_authorized=false`.


## 16.173. Pasada 1 A+B — auditoría integrada Outcome/Value e intervención/estimandos (2026-11-12)

**Artefactos rectores inspeccionados:** `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md` §§2–10 y 12/14; `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md` §§5–9 y 14–15; `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md` §§2, 7–11; `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md` §§2–8; `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md` §§3–12; `C10_S_VALUE_MINIMUM_CORE_RECONCILIATION_MATRIX_DRAFT_001.md` §§497–529; `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md` §§18–32; `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md` §§15–17; `C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md` §§2–9. Se reutilizan P179, P182, P183, §224, P177/P178, C-MED y C-ANALYZER.

### 16.173.1. Requisitos ya cerrados — no reabrir

- B1 por UE, identidad lógica y relación con servicio por UE, una oportunidad estandarizada por UE y distinción Need_preZ / Request_event / admisión / procesamiento / respuesta / consecuencia / Value: contratos y decisiones existentes.
- Objetivo basal de B1 y función mínima de servicio: mantener disponible en destino un servicio capaz de admitir solicitudes según ENABLED y exponer PROFILE. La truth de Need_preZ se estipula explícitamente por unidad y se mantiene separada de la configuración técnica, covariables, evidencia observada y eventos post-Z.
- Outcome técnico, consecuencia de B1 y Value son tres objetos distintos. F* es criterio funcional; O-CONF es resultado adjudicado de conformidad del destino y no un segundo endpoint duplicado de F*; Value es valoración contextual de consecuencias para B1.
- Value conserva P179 como vector y no se impone índice escalar, peso, agregación ni las cinco dimensiones históricas. La perspectiva primaria B1 está aceptada como base; autoridad/regla valorativa debe ser estipulada ex ante en el mundo sintético.
- ITT de asignación D2, primeras etapas, efecto de paquete, LATE focal, contraste poblacional de accesibilidad y mediación interventional son estimandos distintos. D2 asigna políticas materiales, no accesibilidad. No se transfiere identificación entre Outcome y Value, ni desde ITT a C3/C4.
- C4 utiliza como objeto mediador la distribución conjunta factible de ΔT_acc*; no se reduce a A_f* o D_f*, ni se obtiene por ajuste convencional post-Z o resta de estimandos.
- D2→g^Af permanece no demostrado; vías colaterales no están excluidas. Por tanto, el ITT D2 conserva interpretación de efecto de política/paquete y no puede atribuirse automáticamente a accesibilidad.

### 16.173.2. Gaps materiales reales de A — Outcome/Value

**A1. O-CONF:** sigue siendo candidato prioritario, no endpoint confirmatorio cerrado. Faltan mapping/predicados atómicos completos, snapshots y estado terminal común, evento/horizonte, oráculo/fuente independiente y validación de error/cobertura/cegamiento. F* y O-CONF no deben contarse como dos Outcomes. O-CONF puede conservarse como medida técnica secundaria/diagnóstica mientras no se cierre su ficha; no debe bloquear la especificación del endpoint de Value si este puede definirse y medirse independientemente.

**A2. Value:** el bloqueo central no es volver a definir B1 ni inventar una operación de negocio. La clase funcional basal está suficientemente especificada para formular un candidato mínimo de consecuencia: continuidad temporal de la disponibilidad de la capacidad que B1 declara como objetivo (servicio habilitado para admitir solicitudes y exponer el perfil declarado). Sin embargo, ninguna dimensión V_j está aprobada/instanciada y siguen pendientes la regla normativa de valoración, su unidad/escala, baseline, horizonte, indicador/fuente y adjudicación. No se puede declarar un Value confirmatorio solo con la definición funcional.

**A3. Propuesta mínima de cierre, pendiente de aceptación científica:** estudiar un único componente confirmatorio `V_cont` —continuidad de la disponibilidad efectiva de la capacidad de servicio que constituye el objetivo basal de B1 durante una ventana común— como vector unitario `V=(V_cont)`, sin índice compuesto ni pesos. Debe medir la consecuencia para B1 a lo largo del horizonte, no la configuración terminal ni la mera admisión de una única solicitud. La regla valorativa sería una estipulación ex ante de truth_dgp desde la perspectiva B1. La medición deberá ser independiente de ΔT_acc*/Reach/trayectoria y no podrá definirse como su recodificación. La observación repetida de disponibilidad, su unidad/escala, baseline y ventana no se fijan en esta propuesta; deberán derivarse en C/D/E, no inventarse aquí.

Esta propuesta explota la semántica ya aceptada de “mantener disponible” y minimiza dimensiones sin ampliar el caso operativo. La separación que deberá respetarse es:
- F*/O-CONF: conformidad funcional del estado de destino en el punto terminal adjudicado;
- `V_cont`: continuidad efectiva, en el tiempo, de la capacidad de servicio que B1 pretende mantener;
- ΔT_acc*/Reach/trayectoria: mecanismo/estados transformacionales, no medidas de Value.

Si la continuidad no puede medirse sin circularidad, o no representa una consecuencia valorable distinta de O-CONF, no se fuerza: el dictamen será que el Value confirmatorio sigue bloqueado y habrá que reducir/replantear el alcance antes de C/D. No se selecciona una segunda dimensión por completitud.

### 16.173.3. Resultado B — intervención y estimandos

La jerarquía causal documental está suficientemente reconciliada; no requiere otra ronda conceptual. La materialización/identificación permanece abierta:

| Estimando | Objeto | Dictamen vigente y regla de cierre |
|---|---|---|
| `ITT_Z^D2(V_cont)` | Efecto de asignar las políticas materiales D2 sobre Value | Candidato primario de asignación; requiere roster/población, mecanismo Z, unidad/interferencia, horizonte y medida V_cont válidos. Es efecto de paquete, no efecto puro de accesibilidad. |
| `FS_{Cdep}, FS_{Af}, FS_{Df}, FS_{ΔTacc}` | Primeras etapas separadas | Deben medirse por separado; ninguna sustituye a otra. |
| `LATE_f^D2` | Efecto local sobre apertura focal D_f* | Secundario; no identificado/no listo para Wald hasta resolver todos los supuestos IV y error de medida. |
| `θ_{Af}(q_X^*;V_cont)` | Contraste poblacional focal de accesibilidad | No identificado: mapping D2→g^Af, régimen común, soporte y vías colaterales siguen sin demostrarse. No inferirlo desde ITT ni LATE. |
| `θ_A(q;V_cont)` | Pregunta general C10-D1 entre políticas factibles de accesibilidad bajo q común | Pregunta científica general; requiere intervención g0/g1 propia, distribución factible de ΔT_acc*, soporte y medida V_cont. D2 no la identifica por sí solo. |
| `IIE_{ΔTacc^*}(V_cont)` | Mediación interventional por distribución conjunta de ΔT_acc* | No identificado; exige intervención mediadora factible, orden temporal, soporte secuencial y estrategia para confusión mediador–resultado inducida por Z. |
| Efecto directo/residual | Rutas no mediadas | Solo si se define una descomposición compatible e identificada; nunca por resta entre ITT y θ_A/IIE no armonizados. |

La salida de Analyzer por estimando/escenario será IDENTIFIED, BOUNDS_ONLY (solo con restricciones justificadas), NOT_IDENTIFIED o BLOCKED/INDETERMINATE_MEASUREMENT. El DGP debe contener escenarios identificables y deliberadamente no identificables para probar tanto recuperación como abstención. La verdad del DGP evalúa al Analyzer; no constituye evidencia empírica de la teoría.

### 16.173.4. Decisión única pendiente para completar A+B

La arquitectura y jerarquía de estimandos no requieren más decisiones del usuario. La única decisión científica no delegable para cerrar el endpoint mínimo es aceptar o rechazar la propuesta de `V_cont` como única dimensión confirmatoria inicial.

**Recomendación:** aceptar provisionalmente `V_cont` como vector unitario confirmatorio, sujeto a que la pasada C/D/E demuestre distinción de constructo, medición independiente y factibilidad de identificación. O-CONF queda como Outcome técnico secundario/diagnóstico, no como sustituto de Value. Si `V_cont` no supera esos gates, no se declara Value confirmatorio ni se fuerza otra dimensión.

No se pide al usuario que vuelva a definir B1, Need_preZ, la función del servicio, la oportunidad estandarizada o la jerarquía de estimandos; todo ello está ya documentado. La decisión pendiente se limita a la dimensión valorativa propuesta.

### 16.173.5. Estado y límites

**Pasada 1 A+B:** DOCUMENTARY_RECONCILIATION_COMPLETE / VALUE_ENDPOINT_PROPOSAL_PENDING_USER_ACCEPTANCE / D2_TO_ACCESSIBILITY_MAPPING_NOT_DEMONSTRATED / CAUSAL_IDENTIFICATION_NOT_CLOSED / NOT_DESIGN_FROZEN.

Esta entrada registra auditoría y propuesta, no acepta por sí misma `V_cont`, no cambia P179 ni selecciona una dimensión confirmatoria. No cambia D1/D2, población P*τ2/P*_F, decisiones B1, estimandos vigentes, DAG, Core, claims, RMA, Evidence→Claim Matrix o STATUS. No autoriza schema físico, roster/captura, fixtures, implementación, generación de datos, simulación, estimación ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## 16.174. Aceptación de V_cont y aclaración de precedencia documental (2026-11-12)

El usuario acepta la propuesta de utilizar `V_cont` como dimensión única mínima de Value para el núcleo confirmatorio inicial, con carácter **provisional y sujeto a los gates de medición e identificación** de las pasadas C/D/E. Se registra la aceptación para evitar volver a solicitarla.

### 16.174.1. Reconciliación con el trabajo previo

La auditoría histórica confirma que varios elementos sustantivos ya estaban cerrados y no debieron presentarse como si fueran nuevos:
- clase de propósito basal B1 y relación con configuración destino/función de servicio;
- especialización funcional mínima del servicio: admitir solicitudes conforme a ENABLED y exponer PROFILE;
- separación entre admisión, procesamiento, respuesta, consecuencia B1, Outcome técnico y Value;
- envolvente de consecuencias potenciales que ya incluía continuidad/interrupción/degradación;
- perspectiva B1 como referente y Value vectorial P179 sin índice ni pesos;
- arquitectura y jerarquía de estimandos C1–C4.

La precisión documental es que los artefactos rectores anteriores registraban explícitamente `NO_VJ_SELECTED` / `VALUE_NOT_INSTANTIATED`: la continuidad estaba contemplada como clase de consecuencia, pero no constaba formalmente seleccionada como dimensión confirmatoria V_j. Por tanto, no se reabre el caso ni se afirma que la selección formal ya estuviera registrada: se documenta ahora la aceptación expresa de `V_cont`, apoyada en el trabajo previo.

### 16.174.2. Alcance exacto de la aceptación

- Se acepta `V_cont` como única dimensión inicial propuesta: continuidad temporal de la capacidad efectiva del servicio que B1 pretende mantener disponible conforme al contrato funcional basal.
- Se conserva `V=(V_cont)) como vector unitario, sin escalar compuesto, pesos ni compensación con otras dimensiones.
- `V_cont` no es el valor del flag ENABLED, una configuración terminal, una admisión puntual, una respuesta técnica, O-CONF/F*, ni una recodificación de `T_acc`, Reach o trayectoria.
- Debe expresar una consecuencia temporal para B1 durante un horizonte común, con baseline y regla de valoración sintética ex ante.
- La medición debe ser independiente de las medidas de accesibilidad/Reach/trayectoria y del Outcome técnico; la disponibilidad técnica puede ser evidencia o mecanismo, pero no sustituye automáticamente la valoración contextual.
- La perspectiva B1 queda como referente aceptado; la autoridad/regla normativa del DGP, indicador/fuente, unidad/escala, baseline, horizonte, adjudicación, error y validez se completarán en C/D/E.
- La aceptación no presupone que el constructo sea finalmente identificable/medible. Si no supera la prueba de discriminación frente a O-CONF y la prueba de independencia de medición, el dictamen será BLOCKED/NOT_CONFIRMATORY; no se sustituirá silenciosamente por otra dimensión.

### 16.174.3. No-regresión y estado

No se reabren B1, Need_preZ, ENABLED/PROFILE, cardinalidad de una oportunidad estandarizada, la envolvente de consecuencias ni la jerarquía de estimandos. No se solicita al usuario otra decisión sobre `V_cont`.

**Estado:** `V_CONT_ACCEPTED_PROVISIONALLY / SINGLE_DIMENSION_CONFIRMATORY_CANDIDATE / MEASUREMENT_AND_IDENTIFICATION_GATES_OPEN / NOT_DESIGN_FROZEN`.

Esta aceptación no altera P179, no crea un índice escalar, no modifica decisiones previas ni claims, y no autoriza roster/materialización, schema físico, implementación, generación de datos, simulación, estimación o ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## 16.175. Pasada 2 C+D — especificación estructural del DGP y diseño de población/asignación sintéticos (2026-11-12)

**Artefactos rectores inspeccionados:** §§3–8 del presente plan; §16.158 y el artefacto C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md §§1–9; C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md §§1–9; C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md §§15–17; C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md §§1–13; C10_S_INTEGRATED_CONFIRMATORY_FEASIBILITY_AND_DESIGN_FREEZE_RECONCILIATION_DRAFT_001.md; C-MED/MAP-01…07/MED-02…06; S4R, SNAP, REACH, PROV, MEAS, MISS, POL, VER, TRJ, INT, GEN, PM y P177/P178/P179/P182/P183.

### 16.175.1. Requisitos ya definidos — no reabrir

- Microdominio Opción A, frontera P0/P1/P2, F1/F2/A1/A2, D2 primario candidato y D1 secundario: se reutilizan dentro de su alcance. No se amplía el caso por realismo.
- Cadena temporal Z → política B → intento/recepción/instalación/verificación → C_dep* → A_f* → D_f* → ΔT_acc* → Reach/Π → selección/ejecución → Outcome/Value. Los estados no se imputan unos desde otros.
- Snapshot estructural S_T*=(U*,R*,C*,X*), ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*) completo y plano epistémico E_T separado. ΔX* no se cuenta dos veces ni se sustituye por validez/cobertura de evidencia.
- Predicado focal A_f* según la conjunción ID/REL/COND/AUTH/RES/DEP/¬BLOCK; C_dep* es solo parte de DEP y no basta para declarar accesibilidad. App_f*, D_f* y ΔT_acc* conservan sus distinciones.
- Reglas D2: W_programmed=0 bajo Z=0 y W_programmed=1 bajo Z=1. Son reglas de política, no probabilidades de asignación. W_attempt, recepción, instalación, C_dep*, A_f*, D_f* y ΔT_acc* siguen separados. s=0.80 no está aprobado.
- P*τ2 es la población primaria candidata; P*_F es secundaria y no se impone como filtro de P*τ2. E_scope, aplicabilidad, C_dep,0 y A_f,0* no se infieren unos de otros. Need_preZ no es elegibilidad.
- UE/UA/UO y la condición UE=UA solo bajo aislamiento; UO repetidas no aumentan N. Truth_dgp, observed_evidence y evaluation/adjudication se segregan. El Analyzer no recibe truth.
- Familias adversariales ya inventariadas en PD y sus contratos P177/P178/P179/P182/P183 se reutilizan. No se crean escenarios, pruebas ni IDs redundantes.

### 16.175.2. C — modelo estructural causal mínimo recomendado

Se propone un DGP finito y versionado, definido por reglas estructurales y tablas de potenciales sobre estados factibles, no por una simulación narrativa de migración ni por una regresión lineal impuesta a priori.

**Marco basal.** El Generator construye una cohorte sintética finita desde una distribución conjunta versionada q_X* de historias/condiciones basales. Para el núcleo limpio, el marco generador se restringe por construcción a instancias dentro del alcance y con τ2 aplicable; C_dep,0=0 y A_f,0*=0 se estipulan como verdad basal por unidad. Así, la cohorte generada representa P*τ2 dentro de ese universo sintético. Esto no acepta la fórmula pendiente de E_i para un universo externo más amplio ni permite generalizar fuera del marco estipulado. F_alt,0 puede variar como modificador basal y define P*_F solo para análisis secundario; no excluye unidades de P*τ2.

**Política D2 y estados técnicos.** Para cada unidad i, Z_i asigna la política D2 y W_programmed,i=Z_i. El intento efectivo, recepción, instalación y cada predicado técnico se generan separadamente mediante reglas estructurales versionadas y parámetros de cumplimiento/fallo. El control puede incluir un escenario explícito de contaminación/provisión de fondo, sin alterar la regla normativa W_programmed=0. C_dep* se adjudica por sus componentes; A_f* se deriva de todos los predicados aplicables; D_f* compara verdad basal y post; ΔT_acc* se obtiene del diff completo de snapshots. No se asigna Z directamente a accesibilidad ni se fija s=.80.

**Resultado de valor.** Para cada unidad y régimen se genera una trayectoria temporal de disponibilidad de la capacidad que B1 pretende mantener. La verdad candidata de V_cont es la fracción de la ventana común de valoración en la que esa capacidad está efectivamente disponible conforme al objetivo basal B1; formalmente, una medida temporal normalizada de disponibilidad, no el flag ENABLED, una petición aislada, el snapshot terminal O-CONF ni una recodificación de ΔT_acc*. El horizonte y la observación se fijan ex ante en la pasada E; la independencia de medición y la discriminación frente a O-CONF se someten al gate E. El estimando compara potenciales V_cont entre regímenes; no requiere definir ΔV como diferencia mecánica respecto de una configuración terminal.

**Estructura de potenciales y rutas.** El DGP conserva una función estructural versionada:
V_cont,i(z,g)=f_V(X_i, ΔT_acc,i(g), L_i(z), D_i(z), ε_i; θ_V),
donde L_i representa condiciones post-Z que puedan afectar mediador y resultado; D_i representa rutas directas/colaterales; y ε_i causas residuales explícitas del mundo sintético. La forma concreta de f_V se implementa como regla/tabla finita sobre estados y transiciones factibles, sin imponer linealidad, aditividad ni monotonicidad. Los parámetros θ_V y las tablas de verdad se fijan antes de generar resultados y quedan reservados al Evaluator.

### 16.175.3. Separación necesaria de las dos intervenciones

Se formalizan dos experimentos contrafactuales dentro del mismo marco sintético, sin confundirlos:

1. **Intervención D2, Z_B:** asigna la política material de provisión. Su ITT sobre V_cont es el efecto total del paquete, incluyendo toda vía activada por la política. No demuestra por sí mismo que ΔT_acc* causó el cambio.
2. **Intervención de accesibilidad, g_A:** compara dos políticas estocásticas factibles g_A1 y g_A0 sobre la distribución conjunta completa de ΔT_acc*, condicionadas por la misma historia basal q_X*. No fija A_f*=1/0 ni asigna Z a accesibilidad. Es una intervención causal distinta, necesaria para evaluar θ_A(q;V_cont), y debe respetar estados factibles, consistencia y soporte común.

El estimando de accesibilidad se expresa como contraste de medias potenciales bajo g_A1 frente a g_A0, estandarizado a la misma q_X* y a un régimen común explícito para las demás vías. El ITT_Z^D2(V_cont) se estima separadamente. La mediación interventional C4 conserva su propio estimando y exige tratamiento longitudinal de L si Z induce confusión mediador–resultado. No se calcula efecto directo/residual por resta de ITT y efecto de accesibilidad. Si no hay soporte, régimen común o control/identificación de vías alternativas, el Analyzer debe emitir BOUNDS_ONLY o NOT_IDENTIFIED según supuestos disponibles.

Esta separación no cambia la precedencia documental D2/D1 ni afirma que D2 identifique g_A. Permite que el experimento sintético pruebe directamente la recuperación de la contribución de accesibilidad, a la vez que prueba la correcta interpretación del efecto de paquete D2.

### 16.175.4. D — población, unidad y asignación del experimento sintético

**Población.** La cohorte finita es generada por el DGP dentro del marco sintético P*τ2 descrito en §16.175.2. El Generator conserva el roster y la elegibilidad verdaderos; el Analyzer recibe solo los campos observables sellados. En el escenario base, la evidencia pre-Z de elegibilidad es suficiente para que la asignación sea auditable. Los escenarios de error, ausencia o UNKNOWN pre-Z se mantienen como estrés de medición y selección; no se recodifican como inelegibilidad ni se excluyen silenciosamente. P*_F se conserva como análisis secundario condicionado a F_alt,0 respaldado.

**Unidad e interferencia.** En el núcleo limpio, cada UE constituye su propia UA y sus recursos, servicio, estado, agentes y canales son aislados por construcción del DGP. UO son medidas repetidas anidadas. Esta estipulación es verdad del escenario sintético, no evidencia de aislamiento en una instalación real. Un escenario adversarial introduce recursos/pools/canales compartidos; el Analyzer debe reconocer clúster/exposición o abstenerse de interpretar un ITT individual bajo SUTVA.

**Asignación.** Z_B se asigna mediante aleatorización reproducible dentro de estratos basales preespecificados, con probabilidad π_h conocida y estrictamente entre 0 y 1 en cada estrato elegible. El algoritmo, la semilla y el hash quedan fijados en el manifiesto del experimento antes de generación. No se presume 1:1: la asignación, N y los tamaños por estrato se seleccionarán conjuntamente en E mediante búsqueda de potencia/precisión para los estimandos confirmatorios, sujeto a positividad y coste. Las reglas W_programmed=D2 condicionales a Z no sustituyen a π_h.

**Soporte.** q_X* es una distribución conjunta basal común, explícita y versionada; ambas intervenciones comparadas deben ser factibles en su soporte para el estimando correspondiente. El escenario base garantiza soporte por construcción y lo documenta; escenarios adversariales retiran soporte en historias identificables y exigen restricción explícita del estimando o NOT_IDENTIFIED. q_L* no forma parte del núcleo base: se activa solo en el escenario longitudinal con confusión post-Z inducida, si existe una intervención secuencial implementable y soporte; de lo contrario, se exige abstención para C4.

### 16.175.5. Suite mínima de escenarios: selección de existentes, no expansión

La batería no será factorial completo. Se seleccionan de las familias ya definidas en PD los contrastes mínimos siguientes:

- **Recuperación identificable:** contribución de accesibilidad positiva, nula y adversa, con verdad conocida.
- **Separación de rutas:** efecto directo/colateral de D2 sobre V_cont sin cambio de ΔT_acc*; y escenario mixto con accesibilidad más vía paralela/interacción.
- **Mecanismo D2:** fallo parcial/contaminación y primera etapa focal débil o nula; distinguir W_attempt, C_dep*, A_f*, D_f* y ΔT_acc*.
- **Identificación:** soporte/positividad insuficiente y confusión mediador–resultado inducida por Z; comprobar bounds o abstención correcta.
- **Robustez de diseño:** error/ausencia diferencial de medición y un escenario de interferencia por recursos compartidos.

Los contrastes de heterogeneidad, alternativas, defiers, crossover, MNAR y censura se conservan como extensiones/sensibilidad cuando afecten a un supuesto concreto; no se convierten todos en factores cruzados del núcleo confirmatorio. Cada escenario debe declarar truth, mecanismo alterado, estimando afectado y salida esperada. Se reutilizan los IDs de PD/P177–P183; no se crean pruebas nuevas.

### 16.175.6. Parámetros y elecciones que se derivan, no se inventan

No se fijan en esta pasada N, R, π_h numérico, semilla concreta, pesos/prevalencias de q_X*, tasas de cumplimiento/éxito, parámetros de transición, magnitudes de efecto, varianzas, ventanas temporales ni tolerancias. No se adoptan los ilustrativos 1:1, N=2.000, R=1.000 o s=.80.

En la pasada E se derivarán en una única optimización conjunta:
- magnitudes positivas/nulas/adversas y efectos directos/interacciones a partir de la escala de V_cont, el efecto mínimo relevante y la precisión objetivo;
- q_X* y estratos a partir del soporte requerido y de los contrastes que deben recuperarse;
- π_h, N y asignación por estrato mediante búsqueda de potencia y precisión, sin perder positividad;
- R y semillas jerárquicas según el error Monte Carlo admisible y la reproducibilidad;
- horizontes, observación, error y missingness de acuerdo con la definición de V_cont y los escenarios que deben discriminarse.

Si la elección requiere una preferencia científica no derivable de estos criterios, se presentará una única recomendación con alternativas y consecuencias; no se solicitarán decisiones parciales sucesivas.

### 16.175.7. Separación entre experimento sintético y materialización operativa real

El experimento de recuperación metodológica no necesita capturar IAM, snapshots, artefactos, runtime ni telemetría de una migración informática real. El propio Generator puede crear cohortes, identidades/versiones, estados, snapshots, evidencia y errores sintéticos con provenance y verdad conocida, conforme a los contratos existentes. Esto no equivale a declarar G-MAT satisfecho para una futura prueba de material D2 real, ni demuestra que el mecanismo D2 sea implementable o aislado en infraestructura real.

La ausencia de material externo real deja de bloquear el experimento sintético si el alcance se declara como recuperación bajo DGPs estipulados. Sí bloquea cualquier afirmación sobre factibilidad/efecto de una implementación real de D2 y cualquier transferencia empírica fuera del marco sintético.

### 16.175.8. Dictamen y salida de la pasada

**Estado:** C_STRUCTURAL_DGP_SPECIFIED_PROVISIONALLY / D_SYNTHETIC_POPULATION_AND_ASSIGNMENT_SPECIFIED_PROVISIONALLY / NUMERICAL_CALIBRATION_DEFERRED_TO_E / REAL_D2_MATERIALIZATION_OUT_OF_SYNTHETIC_SCOPE / NOT_DESIGN_FROZEN.

La pasada C+D queda cerrada a nivel de arquitectura estructural y contrato de población/asignación sintéticos, sujeto a la calibración ex ante de E. No se declara identificado ningún efecto empírico ni se afirma que D2→g_A esté demostrado en el mundo real. Los parámetros y criterios numéricos se resolverán junto con la evaluación, no mediante elecciones arbitrarias.

No se reabren las decisiones existentes ni se modifican D1/D2, P*τ2/P*_F, DEC-C10-066/067, P179, estimandos C1–C4, DAG, claims, Core, RMA, Evidence→Claim Matrix o STATUS. No se crea documento, test ID o fixture nuevo. No se autoriza implementación, generación de datos, simulación, estimación, validadores ni ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false.


## 16.176. Pasada 3 E+F — auditoría final de suficiencia, medición, calibración y contrato técnico (2026-11-12)

**Fuentes reconstruidas:** gobernanza main (README, bootstrap, regla de reconstrucción histórica); plan §§7–12 y 16.173–16.175; C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md §§1–15; C10_S_INTEGRATED_CONFIRMATORY_FEASIBILITY_AND_DESIGN_FREEZE_RECONCILIATION_DRAFT_001.md §§6–12 y 16–17; C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md §§1–9; matriz Value mínimo §§9–10; contratos B1/Need y modelo de observación S7. No se ha ejecutado validador, DGP, Analyzer, simulación ni prueba técnica.

### 16.176.1. Lo que ya está definido y no debe volver a diseñarse

- Separación de roles Generator → Proyector/Sealer → Analyzer → Evaluator/Adjudicator y almacén de procedencia; Analyzer sin truth/potenciales/semillas secretas; Evaluator solo después del sellado.
- Separación de `truth_dgp`, `observed_evidence` y `evaluation/adjudication`; separación de identidad/versiones, relojes, snapshots, estados trivalentes y ausencias.
- Arquitectura lógica de los seis artefactos B1 ya aceptados; no se crea un séptimo ni un segundo modelo universal.
- Reglas B1/Need_preZ, S7, adjudicación E1/E2, cobertura, ausencia≠0, comparación observada-vs-polaridad y observada-vs-truth en sus alcances documentados.
- Contrato de salida del Analyzer por estimando/constructo y dimensión, con estimación/incertidumbre cuando proceda y abstención correcta cuando no exista identificación.
- Familias de métricas y controles P177/P178/P179/P182/P183: sesgo, RMSE, cobertura, error tipo I, potencia, calibración, convergencia, réplicas inválidas, clasificación de identificación/no-identificación, missingness/censura, weak-IV, sensibilidad y error Monte Carlo.
- La arquitectura estadística existe; no se debe volver a describir como ausente. Lo que falta es su instanciación cuantitativa coherente con los estimandos y el DGP.
- El contrato PE existe como arquitectura lógica e interfaces; no se debe recrear. Su propio dictamen es `TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY`.

### 16.176.2. E — medición de V_cont: aceptación de constructo no equivale a operacionalización validada

La aceptación de §16.174 selecciona provisionalmente `V_cont` como única dimensión inicial candidata. §16.175.2 propuso como verdad candidata una fracción temporal normalizada de la ventana común durante la que está disponible la capacidad de servicio. Esa propuesta es una hipótesis de operacionalización, no un indicador ya validado ni un contrato congelado.

Siguen abiertos y deben resolverse juntos, no mediante nuevas preguntas parciales:

1. **Objeto valorado y regla normativa:** qué estado observable cuenta como capacidad efectivamente disponible para el objetivo basal B1, qué estados no cuentan y cómo se valora su continuidad desde la perspectiva B1. No inferir valor desde ENABLED, una respuesta aislada o la mera existencia de un endpoint.
2. **Discriminación de constructo:** demostrar que `V_cont` no es O-CONF/F*, ni un duplicado del Outcome técnico, ni una recodificación de `A_f^*`, `ΔT_acc^*`, Reach o trayectoria. La disponibilidad técnica puede ser parte del mecanismo o evidencia, pero no acredita por sí sola una consecuencia valorada distinta.
3. **Medición independiente:** fuente/observador, regla de captura, resolución temporal, cobertura, error, fiabilidad y adjudicación. El Generator conserva truth temporal; el Analyzer solo recibe la proyección observada permitida.
4. **Baseline y horizonte:** definir baseline, inicio/fin y tratamiento de estados transitorios, interrupciones, degradación, censura y ausencia. No se elige una ventana por conveniencia ni después de ver efectos.
5. **Escala y estimando:** decidir si el valor normalizado de continuidad es una proporción temporal, una secuencia o una representación vectorial temporal; especificar el contraste causal sin colapsar incertidumbre de medición y variabilidad entre unidades.

La recomendación de parsimonia sigue vigente: una sola dimensión, sin pesos, índice compuesto ni sustitución silenciosa. Si no se supera la discriminación frente a O-CONF, `V_cont` no pasa a endpoint confirmatorio y no se fuerza otra dimensión. O-CONF sigue siendo Outcome técnico candidato no operacionalizado; no se declara resuelto por este plan.

### 16.176.3. E — calibración estadística conjunta pendiente

La documentación existente fija el procedimiento, no los valores. No se han aprobado:
- magnitud mínima científicamente relevante y MDE, margen de equivalencia y tolerancias por estimando;
- forma funcional/tablas estructurales definitivas y parámetros de los mecanismos, potenciales, heterogeneidad, dependencia e interacciones;
- distribución conjunta `q_X^*`, estratos, soporte común de las intervenciones y restricciones de población;
- probabilidades de asignación por estrato `π_h`, ratio, N, algoritmo y semillas;
- número de réplicas R y límite de error Monte Carlo (SE_MC);
- multiplicidad/jerarquía inferencial y reglas de decisión/inconclusión;
- rangos de sensibilidad `δ/γ`, error diferencial, missingness y censura, ni tolerancias de recuperación del Analyzer.

Estos elementos se derivarán en un único procedimiento de calibración, no por elección independiente. La función objetivo debe equilibrar potencia y precisión de ITT, primeras etapas y estimandos de accesibilidad que sean identificables por construcción; control de error y recuperación de escenarios nulos/adversos; clasificación correcta de no-identificación; y SE_MC para métricas de evaluación. No se dimensionará un estimando que carezca de definición/soporte. No se adoptarán N=2.000, 1:1, R=1.000 ni s=.80 como parámetros aprobados.

### 16.176.4. F — suficiencia del contrato técnico

PE ya define arquitectura de seis roles, interfaces conceptuales, dominios de datos, trazabilidad, manifiestos, capas V0–V8 y formato lógico de salida. No falta otra arquitectura conceptual.

Bloqueos concretos de implementación confirmatoria que PE declara abiertos:
- perfil físico de serialización/canonicalización para registros y bundles fuera del alcance JCS/U1 ya aceptado;
- schema físico o estructura equivalente, cardinalidades, restricciones, referencias, migraciones y validación ejecutable;
- formato de eventos, timestamps y orden parcial material;
- almacenamiento, separación de dominios, custodia de truth/semillas, permisos ACL efectivos, threat model, logs y controles de acceso;
- sealer/firewall probado, incluida evidencia de que Analyzer no puede recuperar truth ni metadatos reveladores;
- crosswalk final de P177/P178/P179/P182/P183 a estimandos, escenarios, entradas/salidas, oráculos, tolerancias y abstenciones;
- identidad/versionado/hash de Generator, Analyzer, Evaluator, reglas, configuración, inputs, entorno y artefactos;
- preflight de integridad y reproducibilidad, pruebas estáticas/técnicas y evidencia de aceptación.

No se debe imponer DDL/U_G si una implementación equivalente preserva todos los contratos de identidad, snapshots, observación y procedencia; tampoco se puede omitir esa infraestructura si es necesaria para reconstruirlos. La elección física debe derivarse del crosswalk, no precederlo.

### 16.176.5. Bloqueos heredados que no desaparecen con el DGP sintético

La pasada C+D define un marco sintético provisional y puede evaluar recuperación bajo verdades estipuladas. No resuelve:
- la factibilidad material de D2 en un entorno real (IAM, roster, snapshots, provisión basal, dependencias, ACL, alternativas, aislamiento e interferencia);
- que D2 material identifique `g_A`, `θ_A(q)`, `θ_{Af}(q_X^*)` o C4;
- la validez empírica de las reglas estructurales del DGP fuera de los escenarios estipulados;
- la validez de constructo/medición de `V_cont` hasta completar §16.176.2.

La falta de D2 material no invalida el alcance metodológico sintético, siempre que las conclusiones se limiten a recuperación bajo DGPs versionados. Sí impide claims de implementación real, validez externa o identificación empírica de D2.

### 16.176.6. Estado real de gates y corrección de la secuencia

La reconciliación integrada de factibilidad mantiene `G-SCI`, `G-MAT`, `G-SCHEMA`, `G-ROLE`, `G-TEST` y `G-REPRO` en `BLOCKED`, y `G-AUTH` en `NOT GRANTED`. Por tanto, no hay Design Freeze ni implementación autorizada.

La aceptación provisional de `V_cont` registrada en §16.174 prevalece como decisión de trabajo posterior a los documentos PA/PD que aún dicen `VALUE_NOT_INSTANTIATED`; esos estados históricos no se borran, pero deben quedar marcados como anteriores a la selección provisional. No equivalen a que PA/PD, P179 o el maestro completo hayan sido propagados y reconciliados. La presente auditoría no modifica directamente esos artefactos ni los declara actualizados.

También se limita la fuerza de §16.175: sus expresiones sobre cohorte sintética, aislamiento, baseline, función de potenciales e intervención `g_A` son **propuestas estructurales del DGP**, no hechos materiales verificados ni parámetros cerrados. `V_cont` como fracción temporal sigue siendo propuesta operacional que debe superar los gates de §16.176.2. La designación C+D como “especificada provisionalmente” no equivale a DGP cuantitativo cerrado ni a diseño confirmatorio congelado.

### 16.176.7. Paquete único mínimo para completar cierre documental antes de pedir autorización

Para reducir iteraciones, el trabajo pendiente se agrupa en un solo paquete integrado, con dependencias internas explícitas:

1. **Reconciliación de precedencia:** propagar la aceptación provisional de `V_cont` y los límites C+D al maestro C10-S y a PA/PD/PE/estimandos/P179, manteniendo trazabilidad de los estados históricos.
2. **Ficha mínima V_cont:** decidir y justificar objeto valorado, regla B1, baseline, horizonte, indicador, fuente independiente, error/cobertura/adjudicación y discriminación frente a O-CONF. Si no supera el test de constructo, dejar Value fuera del núcleo confirmatorio y no sustituirlo automáticamente.
3. **DGP confirmatorio versionado:** convertir las propuestas estructurales C+D en reglas/funciones o tablas de potenciales concretas, fijar intervenciones factibles D2 y `g_A`, historias, vías colaterales, escenarios y verdad reservada; distinguir explícitamente escenarios identificables y no identificables.
4. **Calibración cuantitativa conjunta:** derivar q_X*, soporte, estratos, π_h, N, efectos, δ/γ, tolerancias, multiplicidad, R, SE_MC y semillas conforme a criterios aprobados, sin valores ilustrativos.
5. **Crosswalk final de aceptación:** P177/P178/P179/P182/P183 y pruebas ya existentes ↔ estimandos ↔ escenarios ↔ datos observables ↔ oráculos ↔ métricas/tolerancias ↔ salida esperada/abstención.
6. **Contrato técnico final:** cerrar estructura física o equivalente, serialización, manifests/hashes, aislamiento de roles, almacenamiento/custodia, permisos, interfaces y validadores requeridos; emitir matriz de preparación por gate con evidencia verificable.
7. **Autoauditoría documental de no-regresión:** comprobar maestro, decisiones, test register, closure matrix, U_G, RMA/Evidence y ramas; clasificar PASS_STATIC / CONDITIONAL / NOT_VERIFIABLE y registrar riesgos residuales. No presentar esta autoauditoría como revisión independiente.

La salida del paquete será una de dos: (a) especificación científica y técnica completa para someter a Design Freeze y solicitar autorización de implementación; o (b) un conjunto mínimo de bloqueos restantes con la razón objetiva y la consecuencia de cada uno. No se abrirán subpaquetes ni consultas intermedias salvo una decisión científica no derivable o una autorización explícita que solo el usuario pueda otorgar.

### 16.176.8. Dictamen final de la pasada E+F

**Estado:** `E_F_ARCHITECTURE_RECONCILED / V_CONT_MEASUREMENT_NOT_CLOSED / QUANTITATIVE_CALIBRATION_OPEN / PE_TECHNICAL_CONTRACT_PARTIAL / G_SCI_G_MAT_G_SCHEMA_G_ROLE_G_TEST_G_REPRO_BLOCKED / G_AUTH_NOT_GRANTED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTATION_READY`.

La pasada E+F se cierra como auditoría de suficiencia y localización de bloqueos, no como cierre de diseño confirmatorio. No se declara completo el experimento causal sintético, no se autoriza implementación ni ejecución y no se modifica `main`, Core, claims, RMA, Evidence→Claim Matrix o STATUS. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## 16.177. Ruta óptima vinculante y paquete integrado único de cierre (2026-11-12)

**Solicitud del usuario:** persistir la ruta óptima y el paquete integrado de cierre y completarlo con el mínimo número de interacciones.

### 16.177.1. Regla de ejecución documental

Esta sección convierte §16.176.7 en el plan operativo vigente. No abre un nuevo ciclo PA–PE ni una nueva arquitectura. Se trabaja por reconciliación de precedencia, reutilización de contratos y cierre integrado. No se preguntarán al usuario decisiones que ya estén aceptadas ni se fragmentará el trabajo en aprobaciones de cada campo.

La salida buscada es una especificación científica y técnica sintética coherente, versionada y trazable, lista para una evaluación formal de Design Freeze **o** un dictamen cerrado de bloqueos objetivos. No implica autorización para implementar, generar datos, simular, estimar ni ejecutar.

### 16.177.2. Orden único de trabajo y dependencias

| Orden | Trabajo integrado | Fuentes rectoras que se reutilizan | Salida necesaria |
|---|---|---|---|
| 1 | Precedencia y no-regresión | Maestro C10-S, plan §16.174–176, B2–B3, PA–PE, P179 | Crosswalk de estados vigentes; decisiones posteriores prevalecen sin borrar estados históricos |
| 2 | Ficha confirmatoria mínima V_cont | B1 Need_preZ, contrato funcional B1, B2–B3, §224, P179/P182/P183, Outcome/Value operationalization | Definición, criterio B1, perspectiva/autoridad sintética, truth temporal, observación independiente, baseline/horizonte, estados ausentes, discriminación O-CONF y dictamen |
| 3 | DGP contrafactual completo | PD, D2 assignment/population/support, C1, C-MED/MAP-01…07, B1/S7, P177–P183 | Funciones/tablas estructurales versionadas por escenario; potenciales de D2 y g_A; rutas directas/colaterales; truth y observación separadas |
| 4 | Identificación y evaluación | C1–C4, C-MED, P177/P178/P179/P182/P183 y tests existentes | Estimando por resultado/dimensión; supuestos; soporte; métricas; abstenciones; falsadores; crosswalk completo sin IDs nuevos |
| 5 | Calibración conjunta | PD §7, contratos P178 y DGP cerrado | Algoritmo de búsqueda para q_X*, estratos, π_h, N, parámetros de efectos, sensibilidad, R, SE_MC y semillas; valores solo si se derivan de criterios trazables |
| 6 | Contrato técnico final | PE §§3–15, U_G, U1/JCS, manifests, roles y provenance | Estructura física o equivalente, interfaces, serialización, custodia, ACL, sealer/firewall, hashes, preflight y aceptación |
| 7 | Propagación y autoauditoría | Maestro C10-S, PA/PD/PE, estimandos, P179, matrices y test register en rama research | Referencias cruzadas reconciliadas, estados PASS_STATIC / CONDITIONAL / NOT_VERIFIABLE, riesgos residuales y dictamen de gates |

Dependencias no invertibles: la ficha V_cont precede a su calibración; el DGP precede a potencia/N/R; el crosswalk precede a la elección física de schemas; la verificación de firewall precede a cualquier implementación confirmatoria. El trabajo 1–7 se integra en un solo ciclo documental y no se solicitarán microaceptaciones.

### 16.177.3. Criterios para aceptar V_cont sin circularidad

La dimensión se conserva solo si expresa una consecuencia valorada para B1 respecto de su objetivo basal, y no una recodificación de estado transformacional, predicado A_f*, Reach, trayectoria, ejecución ni O-CONF. La propuesta de fracción temporal de disponibilidad es candidata y deberá separar:
- verdad funcional de la capacidad del servicio a lo largo de una ventana común;
- observación independiente de esa capacidad, con resolución temporal y estados de ausencia;
- regla de valoración ex ante atribuible a B1;
- O-CONF como adjudicación terminal de conformidad del destino frente a F*, sin reutilizarla como medida de continuidad.

La observación de continuidad no podrá depender de la única oportunidad estandarizada por UE ni aumentar la cardinalidad N_opportunities=1: se distinguirá un canal de observación no-mutante del ciclo de petición. Si no es posible demostrar discriminación y medición independiente con las fuentes ya previstas, V_cont queda fuera del endpoint confirmatorio; no se inventa otra dimensión ni se fuerza la aceptación.

### 16.177.4. Regla de calibración y no invención

No se insertarán cifras convencionales (N, R, ratio, MDE, potencia, tolerancias, horizonte, frecuencia, tasas o parámetros) por parecer razonables. Cada valor numérico deberá:
1. tener definición y unidad;
2. estar ligado a un estimando, escenario y criterio de aceptación;
3. derivarse de una regla de diseño reproducible o de una estipulación explícita del DGP;
4. superar una comprobación de sensibilidad;
5. quedar registrado antes de observar resultados del Analyzer.

Si un parámetro no puede derivarse sin una preferencia científica, se agrupa en una sola decisión residual, con recomendación única y consecuencias. No se abrirá una conversación por parámetro.

### 16.177.5. Alcance de materialización

El objetivo es el experimento causal **sintético** de recuperación metodológica. La identidad/instancia, estados, snapshots, eventos, fuentes, canales y errores pueden ser generados con verdad conocida y provenance. No se requiere una migración informática real para ese objetivo. Los bloqueos de D2 material y validez externa se mantienen como límites de claims, no como prerequisitos del DGP sintético.

La especificación técnica puede definirse documentalmente; no se ejecutarán validadores, código, generación de datos, simulación, estimación, replay ni pruebas de seguridad hasta autorización expresa conforme a la gobernanza.

### 16.177.6. Control de avance y salida única

Cada bloque se clasificará como:
- **REUSED/CLOSED:** contrato existente suficiente, sin modificación;
- **RECONCILED:** conflicto de precedencia corregido en el documento rector;
- **SPECIFIED:** regla concreta versionada, aún no ejecutada;
- **CONDITIONAL:** depende de supuesto o validación posterior;
- **BLOCKED:** falta dato/decisión/autoridad no derivable;
- **NOT_IN_SCOPE:** materialización real o validación empírica externa al experimento sintético.

El paquete solo se declarará completo documentalmente cuando no existan contradicciones entre el plan, maestro y contratos rectores, y cada estimando tenga salida identificable/condicional/bounds/no-identificado. Si queda una decisión humana inevitable, se presentará una única pregunta consolidada. No se cambia main ni se promueve PR #116; no se crean IDs o tests nuevos; se mantienen `scientific_execution=false` y `execution_authorized=false`.

## 16.178. Desarrollo integrado del paquete — ficha V_cont y especificación DGP no numérica (2026-11-12)

Esta sección ejecuta los pasos 1–4 de §16.177 a nivel documental. Distingue decisiones ya aceptadas, operacionalización recomendada aún no aceptada y parámetros que no pueden fijarse sin criterio científico explícito. No constituye Design Freeze.

### 16.178.1. Precedencia y no-regresión

Se aplican las siguientes precedencias:
- B1/Need_preZ se rige por el contrato funcional basal y sus decisiones posteriores: objetivo de mantener disponible en destino un servicio capaz de admitir solicitudes conforme a ENABLED y exponer PROFILE; truth explícita pre-Z por B1/UE; separación Need, Request_event, admisión, procesamiento, consecuencia y Value.
- Una B1 por UE, una instancia lógica de servicio versionada por UE y una oportunidad estandarizada por UE son decisiones aceptadas. La observación longitudinal de V_cont no crea oportunidades adicionales ni peticiones de servicio.
- D2 sigue siendo política de provisión asignada; W_programmed=Z no sustituye la asignación aleatoria ni asigna accesibilidad. D1 sigue secundario.
- P*τ2 es la población primaria candidata de trabajo de C1 según precedencia aceptada; P*_F es secundaria. No se afirma que la elegibilidad material o el soporte estén demostrados.
- Value se conserva como vector P179; para este experimento se acepta provisionalmente una única dimensión candidata V_cont, sin pesos ni agregación. Esta selección no se propaga retroactivamente como si los documentos anteriores ya la hubieran congelado. Los estados históricos VALUE_NOT_INSTANTIATED permanecen como registro temporal y quedan superados solo en cuanto a selección provisional, no en cuanto a operacionalización.

### 16.178.2. Ficha de constructo recomendada para V_cont

**Nombre:** V_cont — continuidad de la disponibilidad operativa del servicio para el objetivo basal B1.

**Constructo:** grado temporal en que la instancia de servicio vinculada a B1 mantiene la capacidad de responder conforme a su contrato funcional basal: cuando ENABLED=true, admitir la solicitud de prueba común; cuando ENABLED=false, no admitirla; en ambos casos, exponer el PROFILE declarado. No se atribuye semántica adicional a STANDARD/READ_ONLY ni se equipara admisión con procesamiento o respuesta de negocio.

**Perspectiva y autoridad:** perspectiva B1, ya aceptada como base. La autoridad valorativa es una regla normativa interna y explícita del DGP que representa el objetivo basal de B1; se versiona antes de generar resultados y se aplica simétricamente entre brazos. No se presenta como preferencia humana observada ni como validación externa. El Evaluator aplica la regla, pero no es el beneficiario.

**Unidad:** B1/UE vinculada a una instancia lógica de servicio única y versionada. La unidad estadística continúa siendo UE; las observaciones temporales son repetidas y anidadas.

**Indicador de verdad propuesto:** secuencia temporal binaria/trivalente de disponibilidad conforme al contrato B1 en una rejilla de observación preespecificada dentro de una ventana común post-Z:
- 1: evidencia generada por el DGP de que la instancia cumple la condición operativa aplicable a ENABLED y expone el PROFILE declarado;
- 0: evidencia positiva de incumplimiento de esa condición;
- ?: la verdad de ese intervalo no puede determinarse conforme a la regla del DGP.

La verdad agregada candidata es la proporción de intervalos programados en los que la condición se cumple:
V_cont,i = K^(-1) × Σ(k=1…K) A^B1_ik,
donde K y la rejilla se fijan ex ante, A^B1 es el estado de cumplimiento de la función basal en el intervalo y el vector temporal completo se conserva para evaluación. Es una única dimensión con escala normalizada [0,1], no un índice compuesto ni una suma de Outcome, accesibilidad o trayectorias. La proporción no autoriza ponderaciones temporales diferenciales.

**Observación independiente:** un monitor sintético no-mutante, separado del harness de la única oportunidad estandarizada y del ciclo Request_event, registra en los instantes programados la capacidad de la instancia para comportarse conforme a ENABLED/PROFILE. No envía solicitudes de negocio ni modifica estado. Su fuente, versión, cobertura, timestamps, error y provenance se proyectan al Analyzer sin truth, potenciales ni metadatos reservados. El Generator conserva la secuencia verdadera; el Evaluator compara después del sellado. La existencia de este monitor es una regla de medición del DGP, no una nueva clase U_G, actor cognitivo ni séptimo artefacto B1.

**Ausencia y cobertura:** la ausencia de lectura, pérdida, fallo del monitor, fuente inválida, censura o intervalo no evaluable no equivale a 0. Se registra como no observado/invalid/censored/unknown según el contrato existente. El Analyzer debe informar cobertura y mecanismo; estimación puntual requiere supuestos de observación defendibles, de lo contrario sensibilidad/bounds o NOT_IDENTIFIED. No se calcula una proporción de casos completos como estimación confirmatoria por defecto.

**Baseline y horizonte:** se requiere una medición basal pre-Z con la misma definición y fuente para describir el estado inicial y, si procede, ajuste preespecificado. El endpoint confirmatorio es el nivel temporal post-Z en una ventana común iniciada en el ancla de asignación/intervención definida por el DGP; no se sustituye por una diferencia post-baseline no aceptada. La longitud K, frecuencia de observación y fin de ventana no están fijados: deben cubrir la transición y un tramo de persistencia que haga que “continuidad” sea distinguible de una lectura terminal. Se fijan antes de generación y no a partir de resultados.

**Discriminación frente a O-CONF/F*:** O-CONF es una adjudicación de conformidad funcional del estado terminal del destino frente a F*, con lógica 1/0/? no compensatoria. V_cont es una trayectoria temporal de disponibilidad operativa durante una ventana, bajo el objetivo basal B1. Pueden correlacionar causalmente, pero no son equivalentes: O-CONF no mide continuidad temporal y V_cont no adjudica conformidad terminal completa del destino. El DGP incluirá los casos de separación ya contemplados por PD: configuración terminal conforme con interrupciones durante la ventana; y configuración terminal no conforme con disponibilidad temporal parcial según el contrato operacional. Si el modelo funcional no permite esos estados sin contradicción, o si la medida solo replica O-CONF, la discriminación falla y V_cont no será endpoint confirmatorio.

**No circularidad:** V_cont no se calcula desde A_f*, D_f*, ΔT_acc*, Reach, Π, trayectoria, selección, ejecución, F* ni O-CONF. Esos constructos pueden causar, explicar o correlacionarse con la secuencia de disponibilidad, pero la medida se obtiene del monitor independiente y de la regla B1. No se presume que la accesibilidad sea la única vía hacia V_cont.

**Estado:** V_CONT_CONSTRUCT_SELECTED_PROVISIONALLY / OPERATIONAL_RULE_RECOMMENDED_NOT_YET_ACCEPTED / TEMPORAL_MEASURE_AND_DISCRIMINATION_GATE_OPEN.

### 16.178.3. DGP causal integrado: reglas estructurales y potenciales

El DGP confirmatorio se define como un sistema finito de transiciones versionadas sobre UE y sus instancias, con truth conocida por el Evaluator. No se impone regresión lineal, normalidad, monotonicidad ni efecto positivo.

Para cada UE i:
1. Se genera una historia basal X_i desde q_X* versionada, junto con B1, servicio, objetivo Need_preZ y snapshots basales. La verdad de inclusión/exclusión/unknown se genera explícitamente conforme al contrato Need_preZ; no se infiere desde variables técnicas.
2. Se asigna Z_i mediante aleatorización reproducible dentro de estratos basales pre-Z, con π_h conocido y 0<π_h<1. La política D2 programa W_programmed=Z_i; intento, recepción, instalación, dependencia, predicados de accesibilidad, snapshots y ΔT_acc* son transiciones distintas.
3. Se conserva el vector completo ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), su estado de observación E_T y la proyección A_f*/D_f* según los contratos existentes. No se asigna Z ni g_A directamente a A_f*=1/0.
4. Se genera Reach/Π y trayectoria a partir del estado transformacional y las condiciones de la historia; selección/ejecución se mantienen como etapas posteriores y separadas.
5. Se genera O-CONF verdadero por la regla F* cuando esa rama de escenario se incluya. Se genera por separado la secuencia A^B1_i(t_k) de disponibilidad operativa y V_cont,i conforme a §16.178.2. Las rutas desde Z, ΔT_acc*, Reach/trayectoria, Outcome y condiciones colaterales hacia V_cont se especifican explícitamente por escenario.
6. Se genera observed_evidence mediante los canales de observación versionados; se permite error, pérdida, ausencia, opacidad y medición diferencial conforme a familias ya registradas. Truth y potenciales no se filtran.
7. El Analyzer recibe solo la proyección sellada. El Evaluator conserva potenciales y compara salidas después del sellado.

**Potenciales de política D2:** para cada i se generan estados y resultados potenciales bajo z∈{0,1}, incluyendo V_cont,i(z), ΔT_acc,i(z), O-CONF_i(z) y etapas intermedias. El ITT primario por resultado se define como contraste medio de potenciales bajo asignación Z=1 frente a Z=0 en la población sintética objetivo; para V_cont:
ITT_Z^D2(V_cont)=E_{P*τ2}[V_cont(1)-V_cont(0)].
La aleatorización identifica este efecto de asignación dentro del DGP si la asignación, consistencia, interferencia, observación y población cumplen sus condiciones; las vías directas/colaterales permanecen incluidas.

**Potenciales bajo intervención de accesibilidad:** para θ_A(q;V_cont), el DGP genera resultados potenciales bajo políticas estocásticas g_A1 y g_A0 que intervienen sobre la distribución conjunta factible del cambio completo ΔT_acc*, condicionadas por una misma q_X* y un régimen común explícito para las demás vías. La intervención no fija A_f*, D_f* ni Z. El estimando es el contraste de medias potenciales bajo g_A1 frente a g_A0. Solo es identificable si las políticas son consistentes y factibles, existe soporte común por historia, el régimen común está definido y las rutas alternativas/confusores están controlados por el diseño estructural o por una estrategia de identificación válida. De lo contrario, el oráculo exige BOUNDS_ONLY con restricciones justificadas o NOT_IDENTIFIED.

**C4:** el efecto mediado interventional permanece distinto de θ_A. Si Z induce L postratamiento que confunde mediador–V_cont, el DGP incluye L y la identificación usa una estrategia longitudinal/interventional con soporte secuencial; el ajuste convencional no se acepta. Si el contrato existente no permite una intervención secuencial factible, C4 se declara NOT_IDENTIFIED en ese escenario.

**Efecto residual/directo:** se obtiene solo bajo un estimando propio con intervención/régimen explícitos. Nunca se calcula restando ITT y θ_A ni combinando estimandos con poblaciones, escalas u horizontes distintos.

### 16.178.4. Escenarios mínimos de recuperación y falsación

Se seleccionan de PD y de los contratos existentes, sin crear IDs:
- focal positivo, focal nulo y focal adverso sobre ΔT_acc*/V_cont;
- efecto de paquete D2 sobre V_cont por vía directa/colateral sin cambio de ΔT_acc*;
- combinación de vía de accesibilidad y vía paralela/interacción;
- fallo de provisión por etapas y primera etapa focal nula/débil;
- falta de soporte/positividad para g_A, con salida NOT_IDENTIFIED;
- confusión mediador–resultado inducida por Z para C4, con recuperación solo si el diseño longitudinal la identifica;
- interferencia por recurso/pool compartido, con unidad/exposición compatible o abstención;
- observación diferencial, pérdida/censura y error de monitor, separando error de canal de error del Analyzer.

Cada escenario debe fijar truth, potenciales, mecanismo alterado, estimando, supuestos, observables y salida oráculo antes de cualquier ejecución. No se exige factorial completo; no se añaden pruebas ni IDs.

### 16.178.5. Calibración estadística: algoritmo de cierre, sin cifras inventadas

La calibración se realizará después de aceptar la ficha V_cont y de versionar las reglas estructurales. Para cada escenario:
- elegir primero el estimando evaluable y la población/soporte;
- definir escala de efecto y una rejilla de efectos DGP positivos/nulos/adversos; los niveles no representan evidencia empírica, sino desafíos de recuperación conocidos;
- derivar la magnitud mínima de recuperación (MDE) a partir de la resolución del indicador, la relevancia de la consecuencia para el objetivo B1 y el criterio de error de decisión del experimento;
- seleccionar N y π_h mediante búsqueda reproducible que satisfaga simultáneamente potencia, precisión y positividad para el estimando; el ratio no se presupone 1:1;
- seleccionar R para que el error Monte Carlo de sesgo, RMSE, cobertura, error tipo I, potencia y clasificación de identificación sea inferior a la tolerancia fijada;
- seleccionar K y la frecuencia temporal para distinguir continuidad de estado terminal sin convertir la observación en nuevas oportunidades de servicio;
- seleccionar parámetros de error, missingness, censura, sensibilidad δ/γ y tolerancias de recuperación conforme a falsadores de los contratos MEAS/MISS/P177–P183;
- fijar semillas jerárquicas y hashes del DGP, asignación, observación y Analyzer antes de generar resultados.

No se adoptan cifras ilustrativas de N, R, asignación, tasas, efectos, tolerancias o ventanas. Si la magnitud mínima relevante y el riesgo de error aceptable no pueden derivarse del contrato B1 ni de criterios científicos existentes, constituyen una sola decisión metodológica consolidada, no múltiples consultas.

### 16.178.6. Crosswalk de aceptación y salida del Analyzer

Para cada combinación estimando × escenario × resultado, el Evaluator debe comparar la salida del Analyzer con el oráculo oculto en:
- signo y orden de magnitud del efecto;
- sesgo/RMSE y cobertura de intervalos cuando haya estimación puntual identificada;
- error tipo I/potencia y equivalencia en escenarios nulos, solo con margen preespecificado;
- clasificación correcta de IDENTIFIED / CONDITIONAL / BOUNDS_ONLY / NOT_IDENTIFIED / INDETERMINATE_MEASUREMENT;
- recuperación de primera etapa y distinción entre ITT de paquete y atribución a accesibilidad;
- detección de vía directa/colateral e interacción;
- abstención correcta ante falta de soporte, IV débil/inválido, confusión longitudinal no resuelta, interferencia incompatible y medición no evaluable;
- cobertura, missingness, censura, error diferencial y calibración de incertidumbre;
- no filtración de truth, potenciales, semillas o metadata reservada.

Se reutilizan P177/P178/P179/P182/P183 y MEAS/MISS/PROV/SNAP/REACH/U_G. Los IDs no se reinterpretan como PASS: cada prueba mantiene su scope y requiere fixture/oráculo/criterio de aceptación existente. La matriz final debe indicar para cada fila el test existente que la cubre; cualquier hueco real se informa como gap, sin crear automáticamente otro test.

### 16.178.7. Contrato técnico: límite de lo que puede cerrarse sin implementación

Se reutiliza PE: Orquestador, Generator, Proyector/Sealer, Analyzer, Evaluator/Adjudicator y Artifact/Provenance Store; seis artefactos lógicos B1; interfaces, manifiestos, capas V0–V8, identidad/versionado, snapshots, timestamps y estados trivalentes. No se crea otro rol ni otro ledger.

Antes de implementación se requiere un perfil físico/equivalente que detalle:
- serialización de registros y bundles sin extender automáticamente JCS/U1 a objetos fuera de su alcance;
- claves, cardinalidades, referencias, restricciones y validación;
- representación de eventos y orden temporal;
- almacenamiento separado de truth, observed y evaluation;
- ACL, secretos, custodia, logs, threat model y firewall/sealer;
- hashes/versiones de DGP, Generator, Analyzer, Evaluator, dependencias, entorno, configuración y entradas;
- preflight de integridad, reproducibilidad y aceptación técnica.

La selección de lenguaje, base de datos, serialización y despliegue no está fijada por las fuentes inspeccionadas. No se elige una tecnología por conveniencia del chat. Puede cerrarse documentalmente un perfil neutral de interfaces y requisitos; la elección física se deriva de la implementación autorizada y debe preservar los contratos PE/U_G. G-SCHEMA y G-ROLE siguen BLOCKED hasta que exista evidencia verificable de diseño y controles efectivos.

### 16.178.8. Dictamen del paquete integrado en este corte

**Cerrado documentalmente en este corte:** ruta óptima §16.177; precedencia de decisiones aceptadas; recomendación operacional de V_cont; estructura de potenciales D2 y g_A; separación ITT/θ_A/C4/residual; escenarios mínimos reutilizados; algoritmo de calibración; criterios de salida del Analyzer; requisitos técnicos derivados de PE.

**No cerrado / bloqueos genuinos:** aceptación de la regla operacional concreta de V_cont; definición numérica de horizonte K/frecuencia y baseline; MDE y riesgo de error aceptable; calibración de N/π_h/R/SE_MC y parámetros; soporte cuantificado; identidad/roster y elegibilidad material; estructura física/equivalente, ACL/firewall y validación técnica. Estos no se convierten en falsos PASS por describir sus requisitos.

**Estado:** CLOSURE_ROUTE_PERSISTED / V_CONT_OPERATIONALIZATION_RECOMMENDED / DGP_STRUCTURAL_RULES_SPECIFIED_NONNUMERICALLY / ESTIMAND_ORACLES_SPECIFIED / CALIBRATION_RULE_DEFINED_BUT_NOT_RUN / PE_PHYSICAL_CONTRACT_PARTIAL / DESIGN_FREEZE_NOT_READY / EXECUTION_NOT_AUTHORIZED.

No se crean Decision Records, tests, IDs, fixtures ni schemas físicos. No se actualizan main, RMA, Evidence→Claim Matrix, Core, claims o STATUS. Se mantienen scientific_execution=false y execution_authorized=false.

## 16.179. Auditoría de consistencia y precisión operacional de V_cont (2026-11-12)

**Propósito:** reconciliar la aceptación registrada en §16.174 con el desarrollo posterior §16.178 y resolver ambigüedades de medición antes de calibrar. Esta sección prevalece sobre cualquier estado pendiente de aceptación de la dimensión V_cont que permanezca por arrastre en §§16.173/16.178. No convierte en aceptada la regla operacional concreta propuesta en §16.178.2.

### 16.179.1. Estado de decisión y precedencia

- **V_cont como dimensión única provisional:** ACCEPTED, según §16.174. No volver a solicitar esta decisión.
- **Perspectiva B1 y semántica basal ENABLED/PROFILE:** reutilizadas de los contratos aceptados; no se reabren.
- **Regla temporal de agregación propuesta en §16.178.2:** PROPOSED / NOT YET ACCEPTED. La aceptación de la dimensión no implica aceptación automática de su indicador, rejilla, horizonte ni regla de agregación.
- **Distinción frente a O-CONF/F*:** requisito de validez obligatorio; no se declara superado hasta que los escenarios de separación se puedan generar sin contradicción con el contrato funcional.
- **Medición independiente y validez del monitor:** OPEN; la descripción de un monitor no-mutante no demuestra por sí sola que mida capacidad operativa.

Por tanto, las frases de §16.178.8 que presentan como pendiente la aceptación de V_cont quedan corregidas: lo pendiente es la operacionalización de medida, no la selección provisional de la dimensión.

### 16.179.2. Separación obligatoria entre estado verdadero y observación

La ficha de §16.178.2 mezcla parcialmente el estado verdadero del DGP con el estado de observación trivalente. Para preservar el firewall Generator/Analyzer/Evaluator y la regla de que ausencia no equivale a cero, se establece esta distinción para la siguiente versión integrada:

1. **Estado verdadero por intervalo:** el Generator debe estipular para cada intervalo programado el estado de capacidad operativa B1 conforme al contrato funcional aplicable. En escenarios plenamente especificados será binario (cumple/no cumple). Un estado desconocido en truth solo será admisible si el propio DGP deja genuinamente indefinido el estado; ese intervalo no podrá tratarse como un 0 ni producir una verdad puntual completa de V_cont.
2. **Observación del monitor:** el canal observado puede emitir 1, 0 o desconocido (incluyendo no observado, inválido o censurado, según los contratos existentes). Este estado epistémico/observacional nunca se copia como truth.
3. **Agregación de truth:** la fórmula de media sobre K intervalos solo tiene verdad puntual si los K estados verdaderos están definidos y la regla de ponderación igual por intervalo se acepta ex ante. Si hay estados verdaderos genuinamente indefinidos, se informa indeterminación o bounds justificados; no se fuerza una media puntual.
4. **Estimación desde observaciones:** no se usa por defecto la media de casos completos ni se sustituye ausencia por cero. Error del monitor, cobertura, censura y missingness se tratan con P182/P183 y MEAS/MISS existentes; sin supuestos defendibles, la salida es bounds o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT.

Esta separación es una corrección metodológica de consistencia; no añade ledger, rol, clase U_G, test ID ni artefacto lógico.

### 16.179.3. Alcance y límite del monitor no-mutante

El monitor no-mutante no envía solicitudes de negocio, no crea Request_attempt y no incrementa la cardinalidad de una oportunidad estandarizada por UE. Su objeto no puede ser el mero valor declarativo ENABLED/PROFILE: leer un flag no demuestra que la capacidad funcional exista.

Para ser admisible, el DGP debe definir el estado latente por intervalo como la capacidad efectiva de la instancia para admitir una solicitud conforme al estado ENABLED y exponer el PROFILE aplicable, y debe especificar qué evidencia sintética independiente permite al monitor observar esa capacidad sin ejecutar la oportunidad de servicio. El canal puede tener error y pérdida, y el Analyzer recibe solo la evidencia proyectada, no el estado latente ni la truth.

La fuente concreta, su semántica observacional y su error no están todavía demostrados por los contratos recuperados. Si no puede especificarse una observación no-mutante que discrimine capacidad efectiva del mero estado declarativo, V_cont no supera el gate de medición y no será endpoint confirmatorio. No se inventa una API, telemetría real, protocolo de health-check ni nueva fuente por conveniencia.

### 16.179.4. Regla de valoración y discriminación

La media no ponderada de intervalos implica que cada intervalo programado tiene el mismo peso en la valoración sintética de B1. Esto debe declararse como regla normativa interna del DGP, no como preferencia observada ni como propiedad universal. K, frecuencia, ancla y horizonte siguen sin fijarse y deben ser comunes, ex ante y compatibles con el reloj temporal C10-S.

O-CONF/F* permanece como adjudicación técnica del estado terminal; V_cont pretende representar continuidad temporal de la capacidad funcional. Los casos de separación de §16.178.2 son controles de discriminación, no evidencia de que la separación ya haya sido demostrada. Si el contrato F* y el modelo de servicio impiden producir alguno de esos casos sin contradicción, debe revisarse la validez discriminante antes de aceptar V_cont como endpoint confirmatorio; no se altera F* ni el contrato funcional para fabricar contraste.

### 16.179.5. Ruta inmediata sin nueva ronda conceptual

La siguiente operación integrada será:
1. cruzar la fuente/semántica del monitor con PE, U_G, snapshots y contratos de observación ya existentes;
2. cerrar el contrato de estado verdadero por intervalo y el mapping observado sin añadir una fuente o interfaz no justificada;
3. verificar que la regla de agregación temporal y la discriminación O-CONF/V_cont son coherentes con B1, F* y el reloj t−1/t0…t9;
4. derivar K, frecuencia, baseline, ventana y criterio de relevancia solo después de fijar la semántica de observación;
5. integrar esa ficha con los estimandos C1–C4 y después continuar la calibración conjunta N, asignación, réplicas y tolerancias.

No se solicita de nuevo aceptar V_cont como dimensión. No se declara aceptada la regla de agregación ni superados los gates de medición/discriminación. No se crean tests, IDs, fixtures, schemas físicos ni nuevos roles; no se ejecuta código, validadores, generación, simulación o estimación. Se mantienen scientific_execution=false y execution_authorized=false.

**Estado actualizado:** V_CONT_CONSTRUCT_ACCEPTED_PROVISIONALLY / TEMPORAL_AGGREGATION_PROPOSAL_OPEN / MONITOR_VALIDITY_OPEN / DISCRIMINANT_VALIDITY_OPEN / CALIBRATION_NOT_RUN / DESIGN_FREEZE_NOT_READY / EXECUTION_NOT_AUTHORIZED.

## 16.180. Crosswalk de fuentes U_G/PE para la observación de V_cont (2026-11-12)

**Objeto:** determinar si las fuentes ya admitidas por U_G/PE pueden sustentar la observación temporal de la capacidad operativa B1 sin crear una fuente, interfaz o rol nuevo.

### 16.180.1. Reutilización de clases existentes

El protocolo U_G ya distingue, entre otras, estas familias relevantes:
- **S3 — observación runtime:** procesos, módulos cargados, llamadas, trazas, sockets, logs y métricas. Puede aportar evidencia temporal de actividad/estado operativo, pero su cobertura está limitada por muestreo, rutas no activadas y eventos raros.
- **S4 — snapshots e integridad:** snapshots inmutables, hashes, diffs y estados pre/post/rollback. Acredita identidad y estado capturado, pero no demuestra por sí solo capacidad operativa durante intervalos.
- **S5 — contratos/interfaz:** API, schema, documentación y contratos existentes. Acredita semántica declarada, pero el contrato declarado no prueba comportamiento runtime.
- **EVIDENCE_REGISTER / CLAIM_EVIDENCE_LINK / COVERAGE_REGISTER:** conservan procedencia, vínculo a afirmaciones y universo/cobertura exactos; no son fuentes de capacidad por sí mismos.

### 16.180.2. Dictamen del crosswalk

1. S4 puede fijar identidad, versión y estado estructural de la instancia en el ancla temporal; no sustituye una observación temporal de disponibilidad.
2. S5 fija el comportamiento esperado ENABLED/PROFILE; no demuestra que la instancia pueda realizarlo.
3. S3 es la única familia existente con alcance temporal runtime compatible como **candidato** para la observación no-mutante de V_cont. No obstante, su inclusión en U_G no acredita automáticamente que un conjunto concreto de procesos/métricas/logs mida capacidad efectiva de admisión.
4. No se ha encontrado en los contratos recuperados un mapping aprobado de señales S3 a la capacidad latente de admitir una solicitud conforme al estado ENABLED y exponer PROFILE, ni un instrumento validado, una cobertura temporal o un modelo de error específico para V_cont.
5. Por tanto, el monitor no-mutante puede representarse como una regla de observación sintética sobre S3 dentro del DGP, pero su semántica y sus indicadores concretos siguen CONDITIONAL/OPEN. No se crea una nueva clase de fuente, actor, tabla, ledger, rol o interfaz.

### 16.180.3. Condiciones para cerrar la medición

La ficha podrá cerrarse documentalmente solo cuando el contrato identifique, sin inventar campos físicos:
- qué estado operativo latente define la capacidad B1 por intervalo;
- qué evidencia S3 observable sería compatible con ese estado y qué no puede inferirse de ella;
- cómo se generan sensibilidad, especificidad/errores, cobertura, pérdida y censura sin asumir tasas no justificadas;
- cómo el Analyzer recibe evidencia S3 versionada y sellada sin truth, potenciales ni metadatos reveladores;
- cómo se demuestra discriminación frente a O-CONF terminal y frente al mero valor declarativo ENABLED/PROFILE;
- qué dictamen se emite cuando S3 no cubre una ventana o no permite inferir capacidad.

No se fijan nombres de métricas, endpoints, payloads, intervalos, tasas, campos, API ni tecnologías. No se ejecutan capturas ni se inspeccionan sistemas reales.

**Estado:** S3_RUNTIME_OBSERVATION_REUSED_AS_CANDIDATE / S4_S5_LIMITS_RECONCILED / V_CONT_SIGNAL_MAPPING_NOT_ESTABLISHED / MONITOR_VALIDITY_CONDITIONAL / NO_NEW_SOURCE_OR_ROLE / EXECUTION_NOT_AUTHORIZED.


## 16.181. Crosswalk semántico S3 y límites de inferencia para V_cont (2026-11-12)

### 16.181.1. Qué autoriza realmente S3

El protocolo U_G §3 define S3 como observación runtime mediante procesos, módulos cargados, llamadas, trazas, sockets, logs y métricas; su alcance es carga/uso/relaciones observadas en una ventana. Declara expresamente como límites el muestreo, las rutas no activadas y los eventos raros. Por tanto, S3 aporta una familia temporal de evidencia potencial, no una medida ya validada de disponibilidad/capacidad del servicio.

### 16.181.2. Mapping conceptual candidato (sin campos físicos)

Para el contrato funcional B1 —admitir solicitudes conforme a ENABLED y exponer PROFILE— el mapping conceptual que puede evaluarse dentro de un DGP sintético es:

| Dimensión latente por intervalo | Familia S3 candidata | Qué podría apoyar | Qué no demuestra por sí sola |
|---|---|---|---|
| Proceso/instancia activa | Estado de proceso y módulo cargado | Que el componente está vivo/cargado en la ventana | Que admita una solicitud o exponga el PROFILE correcto |
| Superficie de admisión disponible | Socket/listener y trazas de estado del endpoint | Que la superficie de recepción esté activa | Que la ruta completa acepte/adjudique solicitudes válidas |
| Dependencias runtime necesarias | Estado/llamadas/trazas de dependencias relevantes | Que dependencias requeridas estén presentes/activas | Que el conjunto satisfaga el contrato funcional de extremo a extremo |
| Capacidad disponible | Métricas de cola, capacidad o recursos, si el DGP las define | Que no se observe una saturación/barrera cuantificada según regla ex ante | Que la capacidad sea suficiente sin umbral, unidad y relación causal justificados |
| Perfil servido | Módulo/estado/traza runtime que identifique el perfil activo | Que existe evidencia de exposición del perfil esperado | Que el contenido/semántica sea correcto sin contrastarlo con S5 y el contrato versionado |

Este mapping es una hipótesis de medición para someter a diseño adversarial, no un mapping aceptado ni un catálogo de campos. S5 aporta el contrato semántico de ENABLED/PROFILE; S4 fija identidad/versión/snapshot; S3 aporta observación runtime. Ninguna familia aislada sustituye las otras.

### 16.181.3. Regla de adjudicación y límite de inferencia

La verdad del Generator debe fijar por intervalo la capacidad efectiva latente de la instancia, bajo el contrato funcional y versión aplicables. El canal S3 genera observaciones con error/cobertura/censura conforme a un modelo explícito, manteniendo la truth segregada. El Analyzer recibe solo la evidencia observable y su provenance/cobertura. El Evaluator compara después de sellar la salida con la truth reservada.

La conjunción de señales de proceso, listener, dependencias, capacidad y perfil puede ser un indicador de readiness operacional, pero no equivale automáticamente a éxito funcional extremo a extremo. No se enviará una segunda solicitud de negocio para medirlo: se preserva N_opportunities=1 por UE. Tampoco se inventa health endpoint, API, payload, protocolo de prueba, campo físico, telemetría concreta o tecnología. Si el DGP no puede definir señales observables que discriminen capacidad efectiva de mera configuración declarada, la medición queda NOT_IDENTIFIED y V_cont no pasa a endpoint confirmatorio.

### 16.181.4. Discriminación respecto de O-CONF

V_cont sería una propiedad temporal por intervalos; O-CONF/F* es una adjudicación técnica terminal del destino. La diferencia conceptual no basta para probar validez discriminante. El DGP debe poder producir escenarios temporalmente distintos con estado terminal equivalente y escenarios terminalmente distintos con trayectorias temporales compatibles, sin violar el contrato funcional ni redefinir F*. O-CONF continúa sin ficha §224 completa; por ello, el gate de discriminación sigue CONDITIONAL/NOT_VERIFIABLE, no PASS.

### 16.181.5. Dictamen de cierre de esta operación

- S3 queda identificado como familia observacional temporal reutilizable, con mapping conceptual candidato y límites explícitos.
- No existe mapping de señales concreto aprobado ni evidencia de validez del monitor; no se declara cerrado el instrumento.
- No se fija K, frecuencia, baseline, ventana, umbral de capacidad, error, cobertura, MDE o N; se derivarán solo tras cerrar el contrato de medida.
- No se crean clases U_G, fuentes, roles, tests, IDs, fixtures, schemas físicos ni interfaces nuevas.
- Estado: `S3_CANDIDATE_MAPPING_DOCUMENTED / SIGNAL_VALIDITY_OPEN / O_CONF_DISCRIMINATION_NOT_VERIFIED / V_CONT_SELECTION_ACCEPTED_PROVISIONALLY / MEASUREMENT_NOT_OPERATIONALIZED / NO_EXECUTION_AUTHORIZED`.


### 16.181.6. Precedencia y propagación de la selección de V_cont

La selección provisional de la dimensión ya no depende solo del plan derivado §16.174: queda formalizada en **DEC-C10-099**, incorporada al Decision Log C10-S y propagada al maestro consolidado §277 y al addendum de Outcome/Value. Esta decisión complementa DEC-C10-095 para la extensión B, sin alterar A ni P179. Los estados históricos `NO_VJ_SELECTED / VALUE_NOT_INSTANTIATED` se interpretan ahora como anteriores a DEC-C10-099; siguen siendo correctos respecto de la falta de instancia material/operacionalización, pero no respecto de la selección del constructo. La selección de V_cont no cierra el indicador, el canal S3, la medición ni la identificación.


## 16.182. Contrato semántico de medición sintética de V_cont y límites de identificación (2026-11-12)

**Objeto:** cerrar documentalmente qué representa la truth temporal, qué puede observar el canal S3 no-mutante y qué inferencias quedan permitidas. Esta sección especifica el modelo de medición sintético; no afirma validez empírica de telemetría real ni supera por sí sola el gate O-CONF.

### 16.182.1. Referente funcional y estado verdadero

Se conserva el contrato basal B1: mantener disponible en destino una instancia de servicio capaz de comportarse conforme al estado declarativo versionado ENABLED/PROFILE. La condición funcional se interpreta de forma condicional al modo:
- ENABLED=true: la instancia debe mantener capacidad operativa de admisión conforme al contrato y exponer el PROFILE aplicable.
- ENABLED=false: la instancia debe respetar la no-admisión prevista por el contrato y exponer el PROFILE aplicable.

Para cada UE i e intervalo k de la rejilla DGP, el Generator estipula una truth binaria (A^{B1}_{ik}): 1 si la instancia satisface la condición funcional aplicable durante el intervalo; 0 si existe incumplimiento funcional positivo estipulado. La truth no se deriva de señales S3, de una petición, de la etiqueta ENABLED aislada ni de O-CONF. En el núcleo plenamente especificado no se usa ? como valor ordinario de truth: si el DGP no determina el estado, el intervalo queda fuera de una verdad puntual y se informa como indefinido/bounds, nunca como 0.

La secuencia completa (A^{B1}_{i1},...,A^{B1}_{iK}) es la truth temporal. La dimensión de Value se mantiene como continuidad temporal conforme al objetivo B1; la selección provisional de V_cont no determina aún que la media no ponderada sea la regla normativa final.

### 16.182.2. Canal de observación S3 no-mutante

El canal S3 es pasivo: observa estado runtime y no envía solicitudes, no activa rutas de negocio, no muta configuración/estado y no añade oportunidades. Por intervalo puede producir un vector de evidencia, sin imponer nombres de campos físicos:

| Componente conceptual S3 | Evidencia candidata | Límite inferencial |
|---|---|---|
| Proceso/módulo | proceso y módulo runtime presentes | no prueba admisión ni perfil correcto |
| Superficie de recepción | listener/socket y estado runtime asociado | no prueba ruta completa ni aceptación de una solicitud válida |
| Dependencias | procesos/llamadas/trazas de dependencias necesarias | presencia observada no prueba suficiencia funcional conjunta |
| Capacidad | estado de cola/recursos/capacidad cuando el DGP lo haya definido | no hay umbral suficiente sin unidad, regla y relación estructural explícitas |
| Perfil runtime | módulo/estado runtime asociado al PROFILE versionado | no prueba semántica correcta sin correspondencia contractual |

Cada componente observado puede tomar 1/0/?; ? incluye no capturado, inválido, censurado, contradictorio o fuera de cobertura, según los contratos U_G/P182/P183. Un 0 observado requiere evidencia afirmativa válida de incumplimiento de ese componente; silencio o ausencia de traza no lo demuestra.

El vector S3 no se reduce por una regla AND/OR, puntuación ponderada o umbral arbitrario. Es un conjunto de indicadores imperfectos del estado latente (A^{B1}_{ik}). El DGP debe especificar la distribución conjunta del canal (P(O^{S3}_{ik}mid A^{B1}_{ik},M_{ik})), donde (M) representa solo los mecanismos de captura/error/missingness que se definan explícitamente. No se presupone independencia condicional entre señales, ni sensibilidad/especificidad constantes, ni missingness MCAR/MAR/MNAR. La dependencia, error diferencial y pérdida se estipulan por escenario y se evalúan con P182/P183/MEAS/MISS existentes.

### 16.182.3. Separación de funciones y de fuentes

- **S3:** canal longitudinal candidato para la medición observacional de V_cont; proxy imperfecto, no prueba funcional directa.
- **S4:** identidad, versión e integridad de snapshots; no mide continuidad.
- **S5:** contrato semántico ENABLED/PROFILE; define lo esperado, no demuestra runtime.
- **S6:** evidencia funcional independiente autorizada puede respaldar F*/O-CONF o la oportunidad estandarizada existente; no se convierte en monitor temporal ni se añade una segunda petición. La oportunidad única por UE conserva su cardinalidad y su estimando propio.
- **S7/S8:** contexto o inferencia; no sustituyen evidencia runtime directa ni se convierten en señal de Need/Value por disponibilidad.

No se crea una nueva clase U_G, actor, interfaz, ledger, rol o artefacto lógico. La observación temporal no se confunde con la oportunidad estandarizada ni con la evaluación de Need_preZ.

### 16.182.4. Identificación de V_cont desde evidencia observada

La truth de la dimensión y la estimación desde observaciones son objetos distintos:

[
V^{truth}_{cont,i}=K^{-1}sum_{k=1}^{K}A^{B1}_{ik}
]

La expresión es una definición candidata de agregación, válida solo si: (a) K intervalos están definidos; (b) la rejilla y ventana son comunes y fijadas ex ante; y (c) se acepta normativamente igual peso por intervalo desde la perspectiva B1. Si cualquiera falla, se conserva la secuencia o se informan bounds; no se fuerza un escalar.

El Analyzer no observa (A^{B1}_{ik}), V_truth, potenciales ni parámetros reservados. Recibe solo el vector S3 observado, cobertura, tiempos, identidad/versionado y el protocolo público de medición permitido. No puede usar la media de señales S3 ni la proporción de intervalos observados como sustituto automático de V_cont.

La recuperación de un estimando puntual requiere que el modelo de medición sea identificable con información disponible al Analyzer: por ejemplo, parámetros de canal calibrados de forma independiente y accesibles bajo el protocolo, o una estrategia de identificación justificada en el diseño. En ausencia de calibración/identificación, el resultado correcto es bounds bajo restricciones defendibles o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT. El hecho de que el Evaluator conozca la truth del DGP no habilita al Analyzer ni valida externamente el instrumento.

Se distinguen explícitamente dos condiciones de evaluación sintética:
1. **Canal calibrado por diseño:** parámetros del canal se estipulan antes de generación y su disponibilidad al Analyzer queda fijada en el protocolo. Permite evaluar recuperación bajo medición calibrada, sin afirmar que los parámetros procedan de evidencia empírica.
2. **Canal no calibrado/ambiguo:** el Analyzer no recibe información suficiente para identificar la relación truth–señal. Debe abstenerse o producir bounds; una estimación puntual se considera falsa recuperación.

Estas condiciones reutilizan los escenarios de error, observación diferencial, pérdida/censura y abstención ya previstos; no crean tests ni IDs.

### 16.182.5. Regla de baseline, ventana y agregación

El baseline pre-Z utiliza la misma definición conceptual y el mismo protocolo de observación para describir el estado inicial y permitir ajuste solo si está preespecificado. El estimando principal continúa siendo el nivel post-Z en una ventana común anclada al reloj causal DGP; no se transforma en diferencia respecto de baseline sin decisión previa.

K, frecuencia, inicio/fin y tratamiento de transitorios siguen sin fijarse. Deben ser comunes, ex ante y suficientemente densos para distinguir continuidad temporal de una lectura terminal, sin aumentar N_opportunities. La agregación igual por intervalo sigue propuesta y no se declara aceptada en esta sección. No se asignan cifras sin calibración.

### 16.182.6. Discriminación frente a O-CONF/F*

La distinción conceptual se mantiene:
- V_cont: secuencia temporal de cumplimiento operativo del objetivo B1 durante la ventana.
- O-CONF: adjudicación terminal de conformidad del destino frente a F*.

El DGP puede especificar casos de separación solo cuando F* y la regla terminal O-CONF permitan estipularlos sin contradicción: (a) destino terminal conforme con una o más interrupciones durante la ventana; (b) destino terminal no conforme, pero con cumplimiento operativo parcial durante intervalos previos. Estos casos prueban discriminación dentro del DGP, no validez empírica del instrumento. O-CONF sigue sin ficha §224 completa; por tanto, el gate de discriminación permanece CONDITIONAL/NOT_VERIFIABLE hasta cerrar F*, el evento terminal, el oráculo y su observación. No se redefine F* para fabricar contraste.

### 16.182.7. Dictamen de cierre

- **SPECIFIED:** truth temporal latente, canal S3 pasivo como vector de indicadores imperfectos, separación truth/observed/evaluation, límites de inferencia y regla de abstención.
- **CONDITIONAL:** relación de medición S3–capacidad B1, calibración del canal, validez del proxy y recuperación puntual.
- **NOT_VERIFIABLE:** validez empírica de señales S3 concretas y discriminación final frente a O-CONF mientras §224/F* sigan incompletos.
- **OPEN:** aceptación de la regla de agregación no ponderada; K/frecuencia/baseline/ventana; parámetros del canal; MDE y calibración conjunta.
- **NO AUTHORIZATION:** no se crean fuentes/interfaces/campos físicos ni tests/IDs; no hay captura, implementación, generación, simulación o ejecución.

**Estado:** `V_CONT_TRUTH_SEMANTICS_SPECIFIED / S3_OBSERVATION_MODEL_SPECIFIED_CONDITIONALLY / MEASUREMENT_IDENTIFICATION_CONDITIONAL / AGGREGATION_RULE_OPEN / O_CONF_DISCRIMINATION_NOT_VERIFIABLE / CALIBRATION_NOT_RUN / DESIGN_FREEZE_NOT_READY / EXECUTION_NOT_AUTHORIZED`.


## 16.183. Auditoría de frontera B1–F*–O-CONF–V_cont y discriminación lógica (2026-11-12)

### 16.183.1. Reconciliación del referente B1

La definición funcional aceptada y versionada en el contrato B1 §2 es:

> Antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

Por tanto, la función de servicio no permanece genéricamente abierta. Lo que puede seguir abstracto en el DGP es el contenido de negocio de las solicitudes o del PROFILE, siempre que se conserve un contrato sintético común y versionado. No se vuelve a pedir al usuario que nombre una operación adicional. Las formulaciones históricas de B2–B3 y del caso de valoración que decían que la operación concreta seguía OPEN se entienden superadas en cuanto a la función de servicio; no se consideran cerrados el roster material, el contenido de cada perfil, el instrumento ni la valoración.

La truth temporal de V_cont debe seguir esa función: cumplimiento del modo ENABLED (admisión cuando está habilitado; no admisión cuando está deshabilitado) y exposición del PROFILE aplicable. La truth mide cumplimiento funcional por intervalo, no la pertenencia de Need_preZ ni el hecho de que una solicitud se haya producido.

### 16.183.2. Frontera de F* y O-CONF

La matriz F* define conformidad de la ruta completa y del estado destino aplicado/verificado. FP-01…FP-07 cubren propiedades estructurales, semánticas, compatibilidad, seguridad, aplicación y verificación post-aplicación; FP-08 es validez probatoria/provenance y no propiedad funcional. F* no contiene actualmente una regla de continuidad temporal ni una rejilla runtime común a la ventana de V_cont.

O-CONF es la adjudicación terminal 1/0/? frente a F*, no un resumen de la trayectoria runtime. La separación temporal/terminal es conceptualmente coherente con los contratos disponibles, pero no está todavía demostrada en un instrumento ejecutable: faltan predicados atómicos, mapping, C0/G/H, snapshot/evento terminal, fuente/oráculo independiente y cierre de §224.

### 16.183.3. Contrastes discriminantes admisibles como candidatos

El DGP debe intentar generar, sin alterar F* ni V_cont, al menos estos contrastes lógicos:

1. **O-CONF=1 y V_cont<1:** el destino satisface F* en el estado terminal, pero la instancia sufrió una interrupción o degradación en uno o más intervalos anteriores y se recuperó antes de la adjudicación terminal.
2. **O-CONF=0 y V_cont>0:** el servicio cumple la función B1 durante parte de la ventana, pero el estado terminal incumple una propiedad F* distinta de la continuidad de servicio (por ejemplo, una propiedad estructural, semántica o de seguridad que no impida necesariamente la operación observada). Este contraste solo es admisible si el predicado concreto y su independencia funcional quedan justificados por el F* versionado.

Estos son candidatos de separación, no fixtures ni pruebas ejecutadas. Si el cierre posterior de F* muestra que la conformidad terminal incorpora necesariamente continuidad de servicio durante toda la ventana, el primer contraste dejaría de ser admisible y V_cont podría quedar subsumida por O-CONF. Si no existe una propiedad terminal independiente que permita el segundo contraste, no se fuerza ese caso: se informa la limitación y se evalúa si queda suficiente discriminación para el alcance confirmatorio.

### 16.183.4. Dictamen

- **PASS_STATIC:** frontera conceptual B1 (función de servicio) / F* (conformidad completa terminal) / O-CONF (adjudicación terminal) / V_cont (cumplimiento temporal) diferenciada en los contratos documentales recuperados.
- **CONDITIONAL:** existencia de los contrastes O-CONF/V_cont, dependiente del cierre de predicados F*, evento terminal y regla de O-CONF.
- **NOT_VERIFIABLE:** validez discriminante final, porque O-CONF y su oráculo no están operacionalizados ni validados.
- **OPEN:** contenido sintético de perfiles/solicitudes cuando sea necesario, regla normativa de agregación V_cont, rejilla/ventana y parámetros de medición.
- **No se añaden:** nuevos tests, IDs, fuentes, roles, oportunidades, schemas físicos ni interfaces. No se ejecuta nada.

**Estado:** `B1_SERVICE_FUNCTION_RECONCILED / FSTAR_TERMINAL_SCOPE_RECONCILED / V_CONT_TEMPORAL_SCOPE_DISTINCT_CONDITIONALLY / O_CONF_DISCRIMINATION_NOT_VERIFIED / NO_NEW_TESTS / EXECUTION_NOT_AUTHORIZED`.


## 16.184. N16 — cierre documental integrado de F* y ficha §224 de O-CONF (2026-11-12)

**Tipo:** reconciliación histórica y operacionalización documental; autoauditoría asistida, no independiente.  
**Alcance:** F* común a F1→F2 y A1→A2; oráculo; adjudicación terminal O-CONF; relación discriminante con V_cont.  
**No alcance:** aceptar el IAM material, inventar parámetros/predicados, implementar/validar oráculo, generar fixtures, ejecutar pruebas o autorizar Design Freeze.

### 16.184.1. Precedencia histórica — reutilizar, no recrear

Se recuperaron y cotejaron: DEC-C10-051/055/056/068–071/078/082–088; las fichas Opción A; matriz F* §§1–21; reconciliación SM-01…SM-10↔FP; IAM; decisiones de adjudicación PAR/RUL por etapa; PE Generator–Analyzer–Evaluator; C-Value §224 y su crosswalk actualizado en la matriz de Value. No se encontró una decisión posterior que sustituya el contrato común F* ni un oráculo implementado/validado.

Quedan como precedencia:
- Opción A y F* son el microdominio y criterio funcional de trabajo seleccionados; no reabrir esa elección.
- FP-01…FP-08 son familias aceptadas como arquitectura. FP-01…FP-07 son dimensiones funcionales no compensatorias; FP-08 es validez probatoria/provenance separada.
- Cardinalidad de clase base: CMP≥1, PAR≥1, RUL≥1; REF=0 solo con IAM pre-Z/B y cobertura exhaustiva; POL ausente por diseño en el núcleo mínimo; MET obligatorio para identidad/versionado/procedencia.
- C0 está aceptado como binding lógico de cobertura a snapshot, no como integridad física ni como valores del contexto ambiental. Los siete stage_key son vocabulario cerrado y no equivalen al reloj DGP ni a SNAPSHOT.phase.
- PAR-SVC-ENABLED y PAR-SVC-PROFILE, sus estados/valores y mappings semánticos, y RUL-SVC-ENABLE-PROFILE-01 están aceptados documentalmente dentro de su alcance. Las adjudicaciones F1/A1, destino declarado, aplicación efectiva y post-check se rigen por DEC-C10-085…088.
- F* y O-CONF no son dos Outcomes técnicos distintos: F* es el criterio; O-CONF es el estado adjudicado al aplicar ese criterio a una ruta/instancia terminal exacta. No sumar ni duplicar ambos como endpoints.
- La regla de adjudicación no compensatoria y los estados 1/0/?/NA se reutilizan sin cambio.

### 16.184.2. Unidad, ruta y ancla terminal

La unidad lógica de adjudicación O-CONF es una **instancia de configuración × ruta completa**. Se emite un resultado independiente para F1→F2 y para A1→A2; no se promedian ni se transfieren estados entre rutas. El binding a UE/B1/servicio se conserva cuando la instancia B lo requiera, sin colapsar UE, servicio lógico, CMP, snapshot y ruta.

El ancla terminal documental disponible es:
- ruta F: `F2_DST_APPLIED`;
- ruta A: `A2_DST_APPLIED`.

Ambas son etapas aceptadas por DEC-C10-071. DEC-C10-087 exige evidencia del evento de aplicación y snapshot/registro post-aplicación exacto, con FP-06, FP-07 y FP-08 diferenciados. La adjudicación terminal se realiza sobre el estado aplicado observado en el post-check, no sobre `*_DST_DECL`, un artefacto preparado, un exit code o un log aislado.

No se inventa un stage ni se interpreta stage_key como instante. Permanecen por fijar el snapshot_id/object_record_id real, route_id/route_record_id, el evento terminal y timestamp, su mapping al reloj DGP y la relación exacta con H. La ventana máxima H no está cuantificada ni aprobada.

### 16.184.3. Regla integrada de O-CONF

Para cada ruta e instancia, el oráculo aplica el IAM sellado ex ante y adjudica cada predicado obligatorio aplicable de FP-01…FP-07:

- **O-CONF=1:** todos los predicados obligatorios aplicables de FP-01…FP-07 están en 1 y el conjunto no está vacío.
- **O-CONF=0:** al menos un predicado obligatorio aplicable está en 0 con evidencia/cobertura suficiente.
- **O-CONF=?:** no hay fallo obligatorio confirmado, pero al menos un predicado obligatorio aplicable es desconocido, no observable, no comparable o insuficientemente cubierto, según la regla específica.
- **SCOPE_ERROR / NOT_EVALUABLE:** el conjunto obligatorio aplicable queda vacío o se incumple la cardinalidad constitutiva; no se fuerza PASS ni NA para salvar la instancia.

NA solo procede por no aplicabilidad declarada y justificada en IAM antes de Z/B. La falta de observación no demuestra 0 ni NA. Un FAIL obligatorio no se compensa con PASS de otra familia. El vector por predicado/familia se conserva junto al resultado agregado.

**FP-08 se informa separadamente.** Su fallo no convierte la verdad funcional en O-CONF=0. Si impide acreditar identidad, cobertura, integridad o procedencia de la adjudicación, el resultado observado queda no válido/no evaluable (normalmente `O_CONF_obs=?`), mientras la truth funcional del DGP permanece separada. FP-06 acredita aplicación; FP-07 verifica el estado efectivamente aplicado mediante FP-01…05; FP-08 acredita la cadena probatoria. No se duplican fallos de FP-01…05 por volver a observarlos en FP-07.

### 16.184.4. Crosswalk atómico disponible — alcance y límites

| Elemento | Familia primaria / función | Estado de aceptación |
|---|---|---|
| PAR-SVC-ENABLED BOOL | FP-01 para tipo/estado formal; FP-03 para equivalencia semántica exacta | Contrato aceptado; observaciones y mappings físicos no materializados |
| PAR-SVC-PROFILE ENUM | FP-01 para validez formal; FP-03 para biyección semántica total/versionada | Contrato aceptado; observaciones y mappings físicos no materializados |
| RUL-SVC-ENABLE-PROFILE-01 | FP-03 para preservación de lógica, scope, operandos y efecto REQUIRE; FP-01 para forma AST | Semántica aceptada; mapping/registro físico y evaluación material abiertos |
| CMP / identidad de componente | FP-01 cobertura/forma y FP-03 identidad/significado; anclaje NODE por snapshot bajo DEC-C10-082 | Contrato de identidad aceptado; roster/snapshots y evidencia material abiertos |
| REF / integridad y significado de relaciones | FP-02 integridad; FP-03 semántica; FP-04 disponibilidad de dependencias cuando aplique | Catálogo/mapping propuesto; universo y cobertura material abiertos |
| FP-04 compatibilidad destino | Admisibilidad con capacidades/versión/interfaz del entorno | Familia aceptada; predicados, C0 material y evidencia abiertos |
| FP-05 seguridad efectiva | Requisitos de seguridad declarados independientemente de POL | Familia aceptada; perfil/amenazas/controles/evidencia abiertos |
| FP-06 / FP-07 | Aplicación efectiva / verificación post-aplicación | Contrato lógico aceptado por DEC-C10-087; eventos y snapshots no observados |
| FP-08 | Identidad, provenance, cobertura y reproducibilidad probatoria | Gate separado; enforcement/validez material no demostrados |

La reconciliación SM-01…SM-10↔FP-01…FP-07 sigue propuesta como catálogo global; no se eleva a aceptación confirmatoria por analogía con las decisiones PAR/RUL. No se inventa obligatoriedad de CMP/REF/MET atómicos, propiedades de seguridad, tolerancias ni mapping M. La instancia IAM completa debe resolver O/C/NA/? por objeto, predicado, etapa, ruta y snapshot.

### 16.184.5. Ficha §224 de O-CONF — lo que puede fijarse ahora

| Campo de ficha | Especificación documental alcanzable | Estado |
|---|---|---|
| Identidad/constructo | O-CONF = adjudicación terminal de conformidad de la ruta completa frente al criterio F* versionado | DEFINED |
| Relación con F* | F* es criterio; O-CONF es su salida terminal. No son dos Outcomes | DEFINED |
| Unidad | Instancia de configuración × ruta exacta; vínculo a UE/B1 cuando proceda | DEFINED AT LOGICAL LEVEL |
| Escala | 1/0/?; SCOPE_ERROR/NOT_EVALUABLE separado; FP-08 como gate probatorio | DEFINED AT LOGICAL LEVEL |
| Regla de cálculo | Agregación no compensatoria de predicados obligatorios FP-01…07 bajo IAM | DEFINED AT LOGICAL LEVEL; IAM NOT MATERIALIZED |
| Ancla/evento | Post-aplicación y post-check en F2_DST_APPLIED o A2_DST_APPLIED | PARTIAL; snapshot/evento/timestamp exactos OPEN |
| Fuente | Oráculo independiente/versionado que aplica criterios públicos a evidencia de fuente, destino, mapping, aplicación y snapshot | ARCHITECTURE DEFINED; IMPLEMENTATION NOT EXISTENT/NOT VALIDATED |
| Baseline/contexto | C_src y estado basal del destino identificados bajo C0 | PARTIAL; snapshots y C0 material OPEN |
| Horizonte/ventana | Ruta completa hasta aplicación/verificación dentro de H | H OPEN; no fijar duración |
| Cobertura/ausencia | Evidencia suficiente por predicado; ausencia y falta de cobertura → ? salvo regla positiva exhaustiva | LOGIC DEFINED; coverage NONE/MATERIAL OPEN |
| Error/fiabilidad/acuerdo | Evaluación de falsos positivos/negativos, error, repetibilidad y desacuerdo conforme a P182 | OPEN; no hay estimaciones |
| Cegamiento/provenance | Generator conserva truth; Analyzer no recibe truth/potenciales; salida Analyzer sellada antes de Evaluator; oráculo no se modifica por Z/B ni Outcome/Value | REQUIRED DOCUMENTALLY; firewall/material enforcement NOT VERIFIED |
| P183 | Ausencia, selección, censura y sensibilidad se informan por estimando; no convertir missing en cero | CONTRACT REUSED; mechanisms/parameters OPEN |

La ficha queda **PARTIAL / NOT_OPERATIONALIZED**: cumple parte de la estructura conceptual de §224, pero no la ficha confirmatoria completa. No se inventa fuente concreta, escala distinta, ventana, tolerancia, fiabilidad, acuerdo ni error.

### 16.184.6. Separación Generator–oráculo–Analyzer–Evaluator

1. Generator estipula `O_CONF_truth` y la verdad de cada predicado, con potenciales/parámetros reservados.
2. El canal de evidencia genera observaciones separadas; el oráculo independiente adjudica `O_CONF_obs` a partir de evidencia permitida, criterios e IAM versionados, sin leer truth ni usar Z/B, Outcome o Value para cambiar reglas.
3. Analyzer recibe solo el bundle observable y, si el contrato analítico lo requiere, la adjudicación observada `O_CONF_obs` con identidad/versionado/provenance. Nunca recibe `O_CONF_truth`, potenciales, semilla ni parámetros reveladores.
4. Analyzer sella su salida inmutable antes de abrir truth.
5. Evaluator accede a truth y parámetros después del sellado, compara por ruta/instancia/escenario y clasifica recuperación, error, sesgo, cobertura y abstención.

La independencia del oráculo y el firewall son requisitos documentales, no hechos técnicos probados. La implementación del oráculo, ACL/custodia, threat model y pruebas de no filtración permanecen sin cerrar.

### 16.184.7. Discriminación respecto de V_cont

Se mantiene la distinción de constructos:
- O-CONF: estado terminal de conformidad técnica de la ruta aplicada frente a F*.
- V_cont: continuidad temporal del cumplimiento de la función basal B1 durante una ventana.

Los dos contrastes ya propuestos en §16.183 siguen siendo **candidatos lógicos**, no casos admisibles ya demostrados:
1. O-CONF=1 con V_cont<1, si existe interrupción temporal recuperada antes del snapshot terminal y F* no exige continuidad durante toda la ventana.
2. O-CONF=0 con V_cont>0, si falla una propiedad terminal F* independiente que no impide el servicio durante intervalos anteriores.

No se redefinirá F* ni se debilitará V_cont para fabricar esos contrastes. Si el cierre de predicados/alcance F* impide ambos contrastes o muestra que los constructos se subsumen en el DGP elegido, la discriminación no pasa y V_cont no se declarará confirmatoria por separado.

### 16.184.8. Dictamen de N16 y siguiente cierre

- **PASS_STATIC:** precedencia histórica; criterio común F*; familias FP; regla no compensatoria; estados trivalentes; frontera F*/O-CONF; etapas terminales disponibles; responsabilidades lógicas Generator/Analyzer/Evaluator.
- **CONDITIONAL:** crosswalk atómico global; aplicabilidad IAM; C0/G/H; mapping/tolerancias; fuente/oráculo; cobertura, error, acuerdo y cegamiento; existencia de contrastes discriminantes.
- **NOT_VERIFIABLE:** implementación/independencia/validación del oráculo; adjudicación material por ruta; validez de O-CONF como Outcome confirmatorio; discriminación empírica/sintética ejecutada frente a V_cont.
- **OPEN:** completar instancia IAM y C_src/C_dst/M; predicados FP-04/05 y restantes atomics; snapshot/evento terminal; H; calibración/validación P182/P183; controles técnicos de custodia/firewall.
- **No-regresión:** no se reabren Opción A, contrato B1, PAR/RUL aceptados, stage_key ni familias FP; no se crean tests, IDs, clases, fuentes, interfaces, fixtures o schema físico.

**Resultado:** `N16_RECONCILED_DOCUMENTARILY / FSTAR_CRITERION_DEFINED_AT_FAMILY_LEVEL / OCONF_FICHE_224_PARTIAL / ORACLE_NOT_IMPLEMENTED_NOT_VALIDATED / DISCRIMINATION_CONDITIONAL / DESIGN_FREEZE_NOT_READY / EXECUTION_NOT_AUTHORIZED`.

No se autoriza implementación, validación ejecutable, generación de datos, simulación, estimación ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


### 16.184.9. Siguiente operación vinculante — integración C+D sin reabrir N16

El siguiente trabajo es retomar la pasada C+D ya documentada en §16.175, no abrir otra auditoría de F*. Debe integrar:
1. la truth de O-CONF por predicado/ruta definida en §16.184 y la truth temporal B1 de V_cont definida en §§16.182/179;
2. las funciones estructurales y tablas de potenciales para D2 y g_A, manteniendo ITT de paquete, efecto de accesibilidad y mediación C4 separados;
3. las rutas directas/colaterales y escenarios adversariales existentes, sin añadir escenarios/IDs por duplicado;
4. población, soporte, unidad/interferencia y asignación reproducible, dejando sin cifras los parámetros que dependan de criterios aún abiertos;
5. los contratos P177–P183 para identificación, recuperación, error, missingness, abstención, sensibilidad y precisión por resultado.

La salida será un único crosswalk de variables/potenciales/observación/estimandos y una lista mínima de parámetros derivables frente a decisiones no deducibles. No se calcularán N, probabilidades, réplicas, MDE o tolerancias hasta que estén cerradas las funciones de medida y los criterios de aceptación. No se vuelve a pedir aprobación de Opción A, F*, familias FP, contrato B1, PAR/RUL, V_cont como dimensión ni secuencia de cierre. Sin implementación ni ejecución.




## 16.185. Pasada C+D — crosswalk causal único de DGP, potenciales, observación, estimandos y población (2026-11-12)

**Tipo:** integración y depuración de contratos existentes; no nueva decisión científica ni Design Freeze.  
**Precedencia:** §§16.175–16.176 y 16.184; DEC-C10-066/067 y DEC-C10S-D2-ESTIMAND-SEPARATION-001; maestro §268; PC §32; C1 §16; contratos D2 población/asignación/soporte, PD, matriz A_f*, medición V_cont y ficha O-CONF §224.  
**Propósito:** un único mapa de objetos, potenciales, estimandos, observaciones y salidas del Analyzer. No duplicar tests, IDs, clases, schemas ni arquitectura PE.

### 16.185.1. Contrato de precedencia y alcance

Se mantienen sin reabrir:
- D2 como escenario primario candidato y D1 secundario; políticas materiales D2 según DEC-C10-066/067.
- P*_{τ2} como población primaria candidata y P*_F secundaria, sin filtrar la primera por la segunda.
- Fórmula candidata de A_f* del crosswalk vigente; A_f* es proyección focal de T_acc*, D_f* compara estado basal/post y C_dep* es solo un componente de DEP.
- Cadena temporal t−1 basal; t0 Z; t1 política/intento; t2 recepción/instalación/dependencias; t3 snapshots/T_acc/A_f/ΔT_acc; t4 Reach/Π; t5 consideración; t6 selección/inicio; t7 ejecución; t8 Outcome; t9 Value. Los subeventos B1/Request permanecen separados y no redefinen elegibilidad.
- Separación de truth_dgp, observed_evidence y evaluation/adjudication; Generator retiene truth y potenciales, Analyzer recibe evidencia permitida, Evaluator compara después del sellado.
- O-CONF = adjudicación terminal de F* por instancia×ruta, no un Outcome adicional a F*. V_cont = medida temporal candidata de continuidad de la capacidad de servicio B1; no se deriva de O-CONF, A_f*, Reach, trayectoria ni de un flag ENABLED/PROFILE.

El presente crosswalk es un contrato de estructura causal y medición lógica. No convierte en aceptados los elementos marcados como candidatos en DEC-C10-066/067, PC, PA/PB/PD, ni completa IAM, DGP numérico o la factibilidad material.

### 16.185.2. Diccionario causal integrado y plano de verdad

| Objeto | Papel en el DGP | Relación/derivación permitida | No equivale a |
|---|---|---|---|
| X_i, H0_i, Cc_i | Historia basal conjunta de la UE | Muestreo conjunto q_X* dentro del marco objetivo | Z, propensión de asignación o q_L* |
| E_i, App_i, C_dep,i0, A_f,i0* | Elegibilidad/aplicabilidad/condiciones basales distintas | P*_{τ2} candidata exige los criterios aceptados; E_i/App siguen con límites de operacionalización documentados | Need_preZ, evidencia observada o variables post-Z |
| Z_i | Asignación experimental a la política D2 | Aleatorización por UA/clúster según diseño futuro | W_programmed, recepción, instalación, A_f o ΔT_acc |
| W_programmed,i | Estado prescrito por la política | D2: 0 si Z=0 y 1 si Z=1 | Probabilidad de aleatorización |
| W_attempt, receipt, S_install, C_dep* | Etapas de cumplimiento y provisión técnica | Funciones estructurales condicionales a Z e historia; separadas entre sí | Accesibilidad final |
| T_acc,i,t=(U*,R*,C*,X*) | Estado estructural del espacio accesible | Snapshot versionado por tiempo/ruta | Evidencia E_T o estado de observabilidad |
| A_f,i,t* | Predicado focal de accesibilidad | Conjunción depurada ID/REL/COND/AUTH/RES/DEP/¬BLOCK y regla trivalente | C_dep*, D_f* o ΔT_acc completo |
| D_f,i* | Indicador derivado de apertura focal desde basal | I(A_f,i0*=0 y A_f,i1*=1), bajo matching y predicados comparables | Asignación, cumplimiento o mediador serial adicional |
| ΔT_acc,i* | Cambio estructural completo (ΔU*, ΔR*, ΔC*, ΔX*) | Diferencia entre snapshots comparables; mediador focal de C4 | Solo A_f*, Reach o evidencia de cambio |
| Reach_i / Π_H,i | Factibilidad de ruta y conjunto/trayectoria alcanzable posterior | Se conserva orden posterior a T_acc; intervención conjunta solo si se define explícitamente | Accesibilidad estructural ni ejecución |
| K, Request, Consider, Selection, Start, Exec | Procesos/etapas downstream y contribuciones por etapa | Contrastes contrafactuales por etapa conforme a DEC-C10S-B1-CAUSAL-ADJUDICATION-001 | Elegibilidad, accesibilidad o Value |
| O-CONF_i,r | Outcome técnico terminal por ruta r | Oráculo aplica F* al estado post-aplicación/post-check de esa ruta; truth y observación separadas | F* como endpoint duplicado, V_cont o Value |
| V_cont,i | Dimensión de Value candidata para B1 | Truth temporal de disponibilidad efectiva durante ventana común; medición independiente y discriminación pendientes | ENABLED/PROFILE, O-CONF, A_f, ΔT_acc o una petición aislada |
| E_T / observed_evidence | Canal epistémico | Proceso observacional con error, cobertura, autoridad, versiones, pérdida y censura | Truth estructural o resultado causal |
| evaluation/adjudication | Comparación posterior | Evaluator compara salida sellada con truth por unidad, ruta, escenario y estimando | Insumo del Analyzer o mecanismo causal |

La unidad experimental UE, unidad de asignación UA y unidad de observación UO siguen distintas. UO repetidas no incrementan N. UE=UA solo bajo aislamiento íntegro por construcción; si hay recursos, agentes, estado, información, infraestructura o canales compartidos, se requiere clúster o mapa de exposición y potenciales compatibles.

### 16.185.3. Estructura de potenciales: dos intervenciones, resultados separados

**A. Política material D2 (Z_B).** Para cada UE i se conserva una historia estructural potencial bajo z:
`S_i(z) = (W_programmed_i(z), W_attempt_i(z), receipt_i(z), S_install_i(z), C_dep_i(z), T_acc_i(z), A_f_i(z), D_f_i(z), ΔT_acc_i(z), Reach_i(z), Π_i(z), K_i(z), Request_i(z), Selection_i(z), Exec_i(z))`.
La notación es un vector de estados potenciales, no una afirmación de que todos los elementos estén medidos o identificados. La verdad de O-CONF y V_cont se genera separadamente a partir de los estados/funciones correspondientes:
- O_CONF_truth_i,r(z): conformidad terminal de la ruta r bajo F* versionado, con ancla F2_DST_APPLIED o A2_DST_APPLIED.
- V_cont_truth_i(z): continuidad temporal de la capacidad que B1 pretende mantener, conforme a la regla y ventana comunes que se cierren en E.

El ITT_Z^D2 se define por resultado y horizonte. En particular, ITT_Z^D2(O-CONF_r) y ITT_Z^D2(V_cont) son contrastes distintos; ninguno transfiere identificación ni validez de medida al otro. ITT sobre V_cont solo pasa a confirmatorio si la medición y discriminación de V_cont superan sus gates. Con vías directas/colaterales, ITT sigue siendo efecto total de asignación al paquete D2.

**B. Intervenciones de accesibilidad g_A.** Para θ_A(q) / θ_Af(q_X*) se comparan dos políticas estocásticas factibles g_A1 y g_A0 que inducen distribuciones del vector completo ΔT_acc* condicionado a una historia basal común. No se asigna Z a A_f/D_f ni se fija accesibilidad a 1/0. El contraste formal conserva la estructura:
`θ_A(q;Y) = E_{X~q, ΔT~g_A1, R~r_common}[Y(ΔT,R)] − E_{X~q, ΔT~g_A0, R~r_common}[Y(ΔT,R)]`,
donde Y debe ser un resultado ya definido (para esta extensión, V_cont es candidato); r_common representa un régimen explícito y común para las vías no focales. Esta expresión es un esqueleto de estimando, no su identificación ni una especificación ejecutable: q, g_A1/g_A0, r_common, consistencia, soporte y Y deben estar cerrados. Para el objetivo focal τ2 se exige además el mapping B_D2→g_Af; actualmente no demostrado.

**C. Mediación C4.** El objeto mediador es ΔT_acc* completo. Reach/Π_H y trayectoria pueden ser posteriores secuenciales o un bloque conjunto solo si se define intervención/estimando propio. Confusores mediador–resultado inducidos por Z exigen una estrategia longitudinal/interventional con historia, soporte y régimen definidos. No se introduce ajuste convencional post-Z como solución automática. No se obtiene C4 restando θ_A del ITT ni restando estimandos de población/escala/horizonte diferentes.

**D. Directo/colateral/residual.** Se conservan rutas D_i(z) para efectos de B sobre resultado sin pasar por ΔT_acc*, incluidas alternativas, recursos, dependencias, coste, seguridad, calidad, latencia, información y cambios del canal de observación. Se preservan efectos concurrentes, redundantes, antagonistas, compensatorios e interacciones. El residual/directo solo puede calcularse bajo una descomposición interventional formal, compatible e identificada; nunca como diferencia aritmética automática. Si no se pueden separar vías, la conclusión correcta es efecto de paquete o no identificación.

### 16.185.4. Matriz de estimandos y salidas del Analyzer

| Bloque existente | Pregunta/contraste | Resultado(s) | Condiciones de interpretación | Salida si falla |
|---|---|---|---|---|
| C1 | ITT_Z^D2 por asignación a política material | O-CONF_r; V_cont solo tras gate; cualquier V_j aprobado | Z aleatorizado; población/UA/interferencia; consistencia/versiones; medición/seguimiento; missingness/censura tratados | BOUNDS_ONLY o NOT_IDENTIFIED; no condicionar post-Z |
| C2 | Primeras etapas separadas de Z | W_programmed, W_attempt, receipt, S_install, C_dep*, A_f*, D_f*, ΔT_acc* | Matching/medición/tiempo válidos; cada etapa mantiene su propia escala | No transferir primera etapa técnica a accesibilidad |
| C3 focal / θ_Af(q_X*) | Efecto de políticas de accesibilidad focales en τ2 | ΔT_acc* y V_cont candidato | Mapping B_D2→g_Af; q_X* común; soporte; versiones; régimen común; rutas colaterales separadas | BOUNDS_ONLY / NOT_IDENTIFIED |
| C3 general / θ_A(q) | Efecto de g_A1 vs g_A0 en distribución completa ΔT_acc* | Resultado Y definido, aquí V_cont candidato | Intervenciones factibles, q común, soporte, consistencia, régimen de otras vías | No transportar resultado focal a general |
| LATE_f^D2 | Efecto local de D_f* inducido por Z | Outcome/Value definidos | IV: relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, interferencia, error de medida y robustez weak-IV | No Wald causal; weak-IV / NOT_IDENTIFIED |
| C4 | Mediación interventional por ΔT_acc* | V_cont o V_j aprobado; Reach/Π/trajectory según estimando | Intervención mediadora, orden temporal, confusión inducida por Z, soporte longitudinal y régimen | BOUNDS_ONLY / NOT_IDENTIFIED |
| C5 | Contribución por etapa de Request a trayectoria | Propiedad de trayectoria preespecificada | Contrafactual por etapa, historia/versiones y causas concurrentes; clases NECESSARY/ENABLING/MODIFYING | No atribuir por temporalidad/trazabilidad |

La jerarquía aceptada por DEC-C10S-D2-ESTIMAND-SEPARATION-001 y PC §32 se mantiene. θ_A(q), θ_Af(q_X*), ITT_Z^D2, LATE_f y C4 no se agrupan. La inferencia sobre O-CONF no prueba Value; la inferencia sobre V_cont no valida automáticamente O-CONF.

### 16.185.5. Población, asignación, soporte e interferencia

1. **Marco:** P*_{τ2} sigue como población primaria candidata, generada como cohorte finita desde q_X* versionada; P*_F es análisis secundario. La regla E_i = E_scope ∧ App*(τ2,S0) sigue NO ACEPTADA/no operacionalizada. El núcleo sintético limpio descrito en §16.175 estipula C_dep,0=0 y A_f,0*=0 por unidad dentro del marco; esto no resuelve la elegibilidad externa ni sustituye el crosswalk basal.
2. **Need_preZ:** no es elegibilidad ni filtro de asignación. La cohorte se fija sin examinar truth Need, evidencia, Z ni resultados; los seis artefactos B1 conservan su separación.
3. **Asignación:** Z se aleatoriza en la unidad realmente asignada, con probabilidad positiva en cada estrato elegible. π_h, algoritmo, ratio, semilla, hash, estratos y N siguen abiertos. W_programmed=D2 condicional a Z no es π_h. c/b (cumplimiento e intento de fondo) y éxito técnico s permanecen sin fijar; s=.80 no aprobado.
4. **q_X* y soporte:** q_X* es distribución basal objetivo, no propensión Z. No está materializada. Ambas políticas comparadas deben ser factibles y tener soporte común en las historias con masa para el estimando. Si no, restricción ex ante de población/estimando con justificación o NOT_IDENTIFIED; no extrapolación.
5. **q_L*:** no se introduce como ajuste marginal automático. Solo se especifica si se necesita intervención secuencial sobre historia post-Z/confusores mediador–resultado inducidos, con soporte e identificación longitudinal. Si no puede definirse, C4 queda no identificado.
6. **Interferencia:** UE=UA solo bajo aislamiento total por construcción. Con pools, recursos, agentes, estado, información o canales compartidos se asigna por clúster o se modela G_i(Z_-i) y Y_i(z_i,g_i). Si el mapa de exposición no es conocido, no ITT individual/SUTVA ni Wald individual.
7. **UNKNOWN pre-Z:** no es 0 ni exclusión silenciosa. La ruta para resolverlo/restringir marco observable/usar cotas debe preespecificarse antes de Z. El Analyzer no recibe truth.

### 16.185.6. Truth, observación y evaluación: crosswalk por resultado

| Constructo | Truth reservada del Generator | Observación admisible del Analyzer | Evaluación posterior |
|---|---|---|---|
| A_f*/D_f*/ΔT_acc* | Predicados estructurales, snapshots y diff verdaderos por tiempo/ruta | Evidencia MEAS/SNAP/PROV con matching, cobertura y error | MEAS/MISS/PM/P177–P183 según aplicabilidad; error de clasificación y recuperación |
| Reach/Π/trajectory | Grafo/estados/rutas potenciales y realizadas | Registros de ruta/estado permitidos, sin potenciales | REACH/TRJ/GEN y contratos causales existentes |
| O-CONF | Predicados F* por ruta, aplicabilidad IAM, verdad terminal | Evidencia post-aplicación y post-check; oráculo observado versionado, sin truth | Comparación O_CONF_obs vs O_CONF_truth después del sellado; P182/P183 y familias F*/SNAP/PROV |
| V_cont | Serie temporal verdadera de disponibilidad efectiva por intervalos de la ventana común | Monitor sintético no-mutante independiente; intervalos observados, no observados, inválidos y timestamps diferenciados | Comparación de medida observada con verdad temporal; error/cobertura/fiabilidad/sensibilidad; discriminación frente a O-CONF |
| Need_preZ | Estipulación explícita basal B1/UE en TRUTH_LEDGER | Evidencia S7 visible, separada de truth, adjudicaciones E1/E2 | Evaluación posterior B1; no Analyzer PE ni elegibilidad |
| Outcome/Value adicionales | Potenciales y reglas versionados por DGP | Solo medidas independientes definidas y autorizadas | P177/P179/P182/P183 por resultado/dimensión, no traslado de identificación |

La truth O-CONF se indexa por instancia×ruta; V_cont por UE y ventana temporal. Los intervalos UO repetidos no son unidades independientes para asignación. El canal observacional puede depender de Z, estado o resultado; su dependencia debe representarse y someterse a sensibilidad, no asumirse MCAR/MAR/MNAR ni independencia de fuentes. Ausencia, pérdida, no emisión, opacidad o cobertura incompleta no se imputan a cero.

### 16.185.7. Suite mínima de escenarios reutilizados

Se seleccionan de PD §§3–6 y contratos existentes solo las familias necesarias para probar recuperación/refutación/no-identificación; no se crea una batería factorial nueva:

| Contraste DGP | Verdad conocida que debe variar | Dictamen exigido |
|---|---|---|
| Recuperación focal positiva / nula / adversa | ΔT_acc* y V_cont con signo/ausencia de contribución estipulados | Recuperar signo/magnitud dentro de tolerancia futura o abstenerse |
| Ruta directa/colateral | Z/B cambia O-CONF o V_cont sin cambiar ΔT_acc* | Informar ITT de paquete; no atribuir a accesibilidad |
| Mixto/interacción | ΔT_acc* y vía paralela actúan conjuntamente | Recuperar interacción preespecificada; no asumir aditividad |
| Primera etapa débil/nula/fallo parcial | Z→intento/recepción/instalación/C_dep/A_f/D_f/ΔT_acc se desacopla | Mantener etapas; no fabricar mecanismo ni LATE |
| Soporte/positividad fallidos | g_A o régimen no factible en parte de q_X* | Restringir estimando ex ante o BOUNDS_ONLY/NOT_IDENTIFIED |
| Confusión mediador–resultado inducida por Z | L post-Z común a mediador y resultado | C4 solo con estrategia longitudinal válida; si no, abstención |
| Interferencia | Pools/recursos/agentes/canales compartidos | Clúster/exposición o no interpretar efecto individual |
| Error/ausencia diferencial | Z modifica emisión/captura/retención/medición | Separar cambio estructural de epistémico; P183/sensibilidad/cotas |
| Versionado/crossover/alternativas | Asignado, recibido y aplicado difieren; rutas alternativas o compartidas | Preservar versiones/rutas; no colapsar por ΔT |
| Discriminación O-CONF/V_cont | Estado terminal conforme con interrupciones recuperadas y/o continuidad parcial con fallo terminal independiente | Solo declarar dimensiones diferenciadas si predicados y contrastes son admisibles sin redefinir F* ni V_cont |

Los escenarios de heterogeneidad, defiers, MNAR, censura, crossover y múltiples peticiones se conservan como sensibilidades/escenarios ya inventariados cuando afecten a supuestos concretos. Se reutilizan los IDs y oráculos existentes; no se crean tests nuevos. Los contrastes de discriminación O-CONF/V_cont siguen siendo candidatos lógicos hasta cerrar F*, ventana y predicados de disponibilidad; no se declaran superados por esta tabla.

### 16.185.8. Mapa de contratos P177–P183 y familias existentes

| Contrato | Uso en el crosswalk | Cierre pendiente |
|---|---|---|
| P177 | Definición/recuperación de ITT, primeras etapas, IV/LATE, separación O/V, ajuste basal, heterogeneidad, multiplicidad, equivalencia y dictamen causal | Estimandos Outcome/Value, fixtures/oráculos y tolerancias |
| P178 | Potencia, N, clústeres, réplicas, SE_MC, semillas, reproducibilidad y pérdidas | Función objetivo, parámetros y criterios de precisión |
| P179 | Value contextual/vectorial, dimensiones, trade-offs y agregación | Regla/beneficiario/perspectiva de V_cont y cualquier V_j; no pesos/índice arbitrario |
| P182 | Validez, circularidad, especificación O/V, reproducibilidad, acuerdo, error, invariancia, sensibilidad, roles y trazabilidad | IAM/oráculos/medición/criterios materiales |
| P183 | Ausencia, selección, ITT, mediación, censura, sensibilidad, cotas y dictamen por estimando | Mecanismos y parámetros de ausencia; análisis por estimando |
| S4R/MEAS/MISS/POL/VER/TRJ/INT/GEN/PM/SNAP/REACH/PROV/GC/U_G | Generación, predicados, estados, rutas, observación, cobertura, identidad y procedencia según alcance | Mapping concreto a fixtures, evidencia, oráculos y tolerancias |

El contrato B1 de seis artefactos se reutiliza sin séptimo artefacto. Los IDs P178-SIM organizativos no se presentan como tests originales. El crosswalk no declara PASS por la mera existencia documental de un contrato.

### 16.185.9. Parámetros derivables, no derivables y gates

**Derivable por regla una vez cerradas las medidas:** fórmulas de contraste ITT por brazo y resultado; separación de primeras etapas; regla de agregación temporal de V_cont una vez aprobada la ventana/resolución/criterio de disponibilidad; métricas de recuperación P177/P182/P183; algoritmo de búsqueda de N/π_h/R/SE_MC conforme a potencia/precisión y coste; estimación del error Monte Carlo; tamaños efectivos según clústeres; límites por positividad/soporte.

**No deducible del material actual sin una decisión o evidencia nueva:**
- función estructural concreta/tablas de potenciales y distribución conjunta q_X*;
- parámetros de cumplimiento, recepción, intento de fondo, instalación, transiciones, heterogeneidad, interacción, efectos directos/colaterales y ruido;
- mapping material B_D2→g_Af, definiciones operativas de g_A1/g_A0 y régimen común r;
- roster/IAM/C_SRC/snapshots, composición material E_i, estratos, mecanismo π_h, unidad real de asignación e interferencia;
- regla final de disponibilidad efectiva B1, ventana/horizonte, resolución, baseline, monitor/canal, cobertura/error y prueba discriminante O-CONF/V_cont;
- magnitud mínima científicamente relevante, MDE, márgenes de equivalencia, α/potencia/precisión, tolerancias por estimando, multiplicidad, δ/γ, R y límite SE_MC;
- formato físico/equivalente, almacenamiento, ACL, sealer/firewall, custodia, threat model, logs, hashes de artefactos y validación técnica.

**Regla de calibración conjunta:** no dimensionar N/R ni seleccionar π_h hasta que existan (i) resultado y escala definidos, (ii) estimando y población/soporte identificables, (iii) magnitud mínima relevante/margen y tolerancias aprobadas, (iv) escenarios nulos/adversos y función de pérdida/objetivo de precisión. Después buscar conjuntamente N, asignación, estratos y R para satisfacer potencia, precisión y SE_MC por estimando; informar cuando no exista solución factible. Más N/R no corrige falta de identificación, constructo inválido o soporte.

### 16.185.10. Dictamen integrado C+D

- **PASS_STATIC:** precedencia D2/D1, jerarquía C1–C5, cadena temporal, distinción Z/política/cumplimiento/accesibilidad, roles truth/observed/evaluation, unidad lógica y reglas de no transferencia; arquitectura de población/soporte/interferencia como contrato condicional.
- **CONDITIONAL:** estructura potencial D2/g_A; V_cont como resultado candidato; O-CONF por ruta; escenarios mínimos; crosswalk P177–P183; reglas de estimación y calibración.
- **NOT_VERIFIABLE:** verdad material de D2, mapping B→g_Af, q_X*/soporte, aislamiento real, oráculo/monitor, independencia de medición, discriminación O-CONF/V_cont, identificación C3/C4 y firewall técnico.
- **OPEN/BLOCKED:** parámetros y tablas del DGP; materialización de población/asignación; resultados y horizonte confirmatorios; calibración cuantitativa; contratos físicos y gates técnicos.

**Resultado:** `C_DGP_CAUSAL_SKELETON_RECONCILED / D2_ITT_SEPARATE_FROM_ACCESSIBILITY / g_A_NOT_MAPPED_TO_D2 / C4_NOT_IDENTIFIED / OCONF_AND_VCONT_TRUTH_SEPARATED / POPULATION_SUPPORT_NOT_MATERIALIZED / QUANTITATIVE_CALIBRATION_BLOCKED / NOT_DESIGN_FROZEN`.

No se modifica main/Core/RMA/Evidence→Claim/STATUS/claims ni decisiones aceptadas. No se crean tests/IDs ni schema físico. No implementación, generación de datos, simulación, estimación, validación ejecutable ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.



## 16.186. Pasada E+F — cierre integrado de medición, calibración y contrato técnico (2026-11-12)

**Tipo:** reconciliación documental derivada; no aceptación normativa de la agregación V_cont, no Design Freeze, no autorización.  
**Fuentes:** §§16.176–16.185; contrato V_cont §16.182; ficha O-CONF §16.184/§224; Outcome/Value §§16–19; factibilidad §§18–19; PE §§1–15; P178 clean replay closure audit 001 y artefactos primarios; contratos P177/P178/P179/P182/P183.  
**Objetivo:** cerrar lo deducible, reutilizar evidencia existente y aislar la decisión normativa que no se puede inferir del material.

### 16.186.1. Corrección de precedencia — medición V_cont

La fuente rectora es §16.182, no la simplificación conversacional de §16.178 ni la descripción abreviada de §16.185. Se ratifican estas distinciones:

1. La truth reservada es la secuencia latente A_B1(i,k): para cada UE e intervalo, 1 si la instancia satisface la condición funcional B1 aplicable al modo ENABLED/PROFILE; 0 solo ante incumplimiento funcional positivamente estipulado. Un intervalo no determinado por el DGP queda indefinido/bounds, nunca se imputa como 0.
2. S3 es un canal pasivo no-mutante y vectorial de indicadores imperfectos (proceso/módulo, superficie de recepción, dependencias, capacidad definida y perfil runtime). Ninguna señal aislada ni su conjunción no validada demuestra admisión/perfil correctos. No se añade petición, actor, clase U_G, ledger ni oportunidad.
3. S5 declara semántica esperada; S3 observa runtime; S4 fija identidad/versionado/snapshot; S6 y la oportunidad única no se reutilizan como monitor longitudinal.
4. Analyzer no recibe A_B1, V_cont_truth, potenciales ni parámetros reservados. Solo recibe observación S3, cobertura, tiempos, identidad y protocolo público permitido. Media de señales, complete cases o proporción de intervalos observados no sustituyen a V_cont.
5. Estimación puntual requiere modelo de medición identificable con información permitida (p. ej. calibración independiente y disponible al Analyzer). Si no, bounds justificadas o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT.
6. O-CONF sigue siendo adjudicación terminal por instancia×ruta frente a F*. Los contrastes de discriminación no se declaran validados hasta completar F*/IAM/oráculo/snapshot/evento y el canal S3.

**Única decisión normativa pendiente de este subbloque:** si se acepta como escala inicial de V_cont la media no ponderada de A_B1(i,k), con intervalos de igual duración en una rejilla común ex ante, V_cont_truth(i)=K^-1 sum_k A_B1(i,k). En ese caso equivale a la fracción temporal de la ventana en estado funcional. Si no se acepta, se preserva la secuencia temporal como resultado vectorial y no se fabrica un escalar. K, frecuencia, inicio/fin, baseline y transitorios no se fijan aquí. Recomendación: aceptar la media solo bajo intervalos de igual duración y una ventana común preespecificada; no usar ponderaciones no justificadas.

### 16.186.2. Reutilización P178 — cierre computacional previo, no calibración confirmatoria

El artefacto 03_EXPERIMENTS/C10-S/harness/P178_CLEAN_REPLAY_CLOSURE_AUDIT_001.md acredita:
- run primario 43083651875 y replay limpio 43120303588;
- 27 celdas, K={2,10,50}, π0={0.2,0.5,0.8}, null/positive/negative; N=700 equilibrado 350/350, R=10.000/celda; 270.000 invocaciones;
- 17/17 tests de contrato PASS; los 27 contrastes de referencia concordaron; los CSV y manifest primario/replay fueron byte-idénticos;
- cierre COMPUTATIONAL REPRODUCIBILITY PASS / NON-CONFIRMATORY METHODOLOGICAL CALIBRATION.

La auditoría de clean replay posterior prevalece sobre el diagnóstico de replay incompleto anterior; no se repite el replay. Límite expreso: benchmark de estimador acotado, no Analyzer TGCV completo ni DGP confirmatorio C10-S; no cubre canales adversariales, falta de identificación, rutas directas, soporte fallido, medición degradada o interferencia. Por ello N=700, 1:1, R=10.000, K/π0, efectos y escenarios del benchmark no se transfieren al DGP integrado. Tampoco se abre otra ejecución P178.

### 16.186.3. Calibración conjunta — procedimiento cerrado, valores no deducibles

La calibración confirmatoria se realizará en una única búsqueda conjunta, después de aprobar la escala de V_cont, Outcome(s), estimandos, población, soporte y escenarios. Orden vinculante:

1. **Congelar target por estimando:** población/estrato, unidad de asignación, horizonte, resultado/escala, contraste, versión y dictamen admisible.
2. **Parametrizar DGP:** distribuciones conjuntas y ecuaciones/funciones de transición por etapa; efectos focales positivos/nulos/adversos; vías directas/colaterales e interacciones; heterogeneidad; error/cobertura diferencial S3; missingness/censura; interferencia/clúster cuando aplique. Cada parámetro debe tener origen (decisión normativa, restricción lógica, evidencia previa o rango de sensibilidad); no rellenar vacíos por conveniencia.
3. **Fijar criterios ex ante:** α/error tipo I, potencia mínima, precisión/anchura máxima, cobertura, magnitud mínima relevante/MDE, margen de equivalencia, tolerancias de sesgo/RMSE/recuperación, error de clasificación y coste de falsa atribución/no-identificación. La escala y el objetivo de B1 justifican relevancia; P177–P183 justifican métricas, pero no suministran automáticamente valores.
4. **Buscar conjuntamente diseño:** N, π_h/ratio/estratos, unidad/clúster, réplicas R y semillas deterministas. Minimizar N/coste sujeto a todas las restricciones por estimando y escenario prioritario, sin sacrificar clasificación de no-identificación ni falsadores adversariales.
5. **Calibrar R aparte de N:** aumentar R hasta que SE_MC de sesgo, RMSE, cobertura, error tipo I, potencia y tasas de clasificación quede por debajo de tolerancias aprobadas. Reportar incertidumbre Monte Carlo y réplicas inválidas.
6. **Evaluar sensibilidad:** δ/γ, error de medida, pérdida/censura, soporte e interferencia dentro de rangos justificados. Si no hay parámetros defendibles, mostrar frontera de sensibilidad y dejar no identificado; no inventar cotas.
7. **Elegir solución o declarar inviabilidad:** seleccionar el menor diseño factible que cumpla todos los criterios. Si no existe, reducir ex ante el alcance confirmatorio o mantener BOUNDS_ONLY/NOT_IDENTIFIED/INDETERMINATE; no relajar tolerancias después de ver resultados.

No se aprueban valores α, potencia, MDE, márgenes, tolerancias, δ/γ, N, π_h, R, SE_MC, parámetros del canal ni semillas en este addendum. N=700/R=10.000/1:1 pertenecen al benchmark P178 citado, no a esta calibración.

### 16.186.4. Contrato técnico PE — perfil agnóstico a tecnología

Se conserva PE como arquitectura lógica; no se crea una segunda arquitectura ni un esquema físico. El contrato mínimo que cualquier implementación o equivalente debe demostrar:

| Frontera | Invariante obligatorio | Evidencia técnica de aceptación futura |
|---|---|---|
| Generator | Truth, potenciales, parámetros y semillas reservados; proyección observacional derivada sin copiado de etiquetas | manifiesto/hash separado; tests de no filtración |
| Proyector/Sealer | única vía autorizada de liberación; validación de identidad, versión, cobertura, timestamps, integridad y campos permitidos; bundle inmutable | allowlist/denylist versionada; hash; tests de manipulación/replay |
| Analyzer | acceso solo a bundle liberado y contratos públicos; sin credenciales, rutas, logs o metadatos que permitan resolver truth | matriz efectiva de permisos; pruebas negativas de acceso/exfiltración; logs |
| Evaluator | truth solo después del sello de salida Analyzer; no modifica salida ni evidencia | orden de estados y hashes verificables; prueba de apertura posterior |
| Artifact/provenance store | separación de dominios, referencias exactas, versionado append-only según contrato, retención y reconstrucción | manifiestos, lineage, integridad referencial, backup/restore y audit trail |
| Orquestador | autorización y versiones fijadas antes de ejecutar; no canal de truth; run envelope reproducible | verificación de autorización, versiones y hashes |

**No se elige tecnología.** El diseño físico/equivalente debe decidir y documentar: serialización/canonicalización por objeto (JCS solo donde ya se aceptó); modelo lógico/físico y cardinalidades; timestamps/orden parcial; almacenes y fronteras de confianza; identidad/autenticación/autorización; custodia de secretos/semillas; ACL de mínimo privilegio y denegación por defecto; sealer; logs/retención/backups; amenaza de fuga por contenido, nombres, tamaños, tiempos, orden, errores, hashes o metadatos. No colocar truth/secretos en GitHub ni exponerlos al Analyzer.

El gate G-ROLE requiere pruebas de permisos efectivos y ataques negativos, no solo módulos separados. G-SCHEMA requiere validación de estructura/serialización/referencias sobre fixtures no confirmatorios. G-REPRO requiere replay y hashes bajo versiones/inputs/entorno fijados. Ninguna de esas pruebas se ejecuta aquí.

### 16.186.5. Matriz de salida E+F y Design Freeze

| Gate | Salida documental actual | Estado |
|---|---|---|
| G-SCI | D2/g_A/C4 y resultados separados reconciliados; V_cont escala normativa y medición aún incompletas; O-CONF ficha/oráculo incompletos | BLOCKED |
| G-MAT | materialización D2 real no requerida por el alcance sintético; cohorte/soporte sintéticos siguen dentro de G-SCI/G-REPRO | OUT_OF_SCOPE_FOR_SYNTHETIC_CORE |
| G-SCHEMA | contrato lógico PE suficiente como frontera; perfil físico/equivalente, estructura y validadores no elegidos/probados | BLOCKED |
| G-ROLE | segregación conceptual definida; ACL/custodia/sealer/firewall efectivo no probado | BLOCKED |
| G-TEST | P177–P183 y familias existentes mapeados; O/V, oráculos, fixtures y tolerancias incompletos | BLOCKED |
| G-REPRO | P178 benchmark acotado reproducido; reproducción del DGP integrado y manifests de todos los roles no definidos | BLOCKED |
| G-AUTH | autorización de Design Freeze/implementación/ejecución ausente | NOT GRANTED |

**Decisiones no deducibles antes del freeze:** (i) regla normativa de agregación de V_cont; (ii) selección/alcance de Outcome confirmatorio — O-CONF no se convierte en primario por estar más desarrollado; (iii) relevancia/MDE y riesgo de error de decisión; (iv) horizonte/rejilla/criterio de disponibilidad. El alcance de este trabajo es el experimento causal sintético de recuperación, no la materialización de una migración/D2 real; esa frontera ya está decidida y no se vuelve a consultar. G-MAT material real queda fuera del gate del experimento sintético, aunque sus condiciones puedan inspirar escenarios adversariales estipulados. No se harán claims de provisión real, validez externa ni identificación material.

**Dictamen E+F:** MEASUREMENT_CONTRACT_RECONCILED_CONDITIONALLY / VCONT_AGGREGATION_DECISION_OPEN / OCONF_NOT_OPERATIONALIZED / P178_BOUNDED_REPLAY_CLOSED / CONFIRMATORY_CALIBRATION_NOT_DERIVED / PE_TECHNICAL_BOUNDARIES_SPECIFIED_NOT_IMPLEMENTED / G_SCI_SCHEMA_ROLE_TEST_REPRO_BLOCKED / G_MAT_OUT_OF_SCOPE_FOR_SYNTHETIC_CORE / NO_AUTHORIZATION.

No ejecución de código, pruebas, validadores, generación, simulación, estimación, captura material ni implementación. scientific_execution=false; execution_authorized=false.


### 16.186.6. Corrección de alcance del gate material

El alcance científico vigente es el experimento causal sintético. La materialización real de D2, IAM/roster operativo, instalación real o migración informática no es prerequisito ni entregable de este experimento. En consecuencia:
- G-MAT material se marca OUT_OF_SCOPE_FOR_SYNTHETIC_CORE, no como bloqueo que obligue a construir un entorno real.
- Sí son obligatorios en el núcleo sintético: cohorte finita generada y versionada; unidad/UA/UO; asignación reproducible; distribución basal y soporte; interferencia estipulada o aislamiento por construcción; verdad por etapa; parámetros y potenciales versionados.
- Las condiciones de materialización real solo pueden aparecer como escenarios sintéticos adversariales claramente estipulados, nunca como evidencia material observada.
- No se derivarán claims de validez externa, factibilidad operativa o efecto de D2 real.

Esta corrección no relaja G-SCI/G-SCHEMA/G-ROLE/G-TEST/G-REPRO ni autoriza ejecución.




## 16.187. DEC-C10-100 — escala temporal V_cont aceptada y calibración conjunta consolidada (2026-11-12)

**Tipo:** decisión expresa del usuario + derivación metodológica integrada.  
**Registro autónomo:** `00_GOVERNANCE/decisions/DEC-C10-100_V_CONT_EQUAL_INTERVAL_TEMPORAL_AGGREGATION_ACCEPTANCE.md`.  
**Complementa:** DEC-C10-099; §§16.182, 16.186; P179/P182/P183 y MEAS/MISS existentes.

### 16.187.1. Decisión aceptada

Se acepta provisionalmente como escala inicial de la verdad sintética de V_cont la fracción temporal de cumplimiento funcional B1 en una ventana post-Z común:

`V_cont_truth(i) = (1/K) Σ A_B1(i,k)`

Los K intervalos tienen igual duración y pertenecen a una rejilla común definida ex ante. A_B1(i,k)=1/0 solo por estipulación funcional positiva del DGP; ? permanece desconocido. Si existen intervalos ?, Evaluator conserva bounds [n1/K, (n1+n?)/K]; no elimina intervalos del denominador, no imputa cero y no usa complete cases para fabricar punto. El baseline describe el estado inicial; el estimando primario es el nivel post-Z en la ventana común, no un cambio pre/post.

Esta decisión cierra la regla de agregación de la truth, no K, duración, frecuencia, inicio/fin, transitorios, MDE ni el canal de observación. DEC-C10-099 sigue siendo la selección de la dimensión; DEC-C10-100 acepta su escala temporal inicial.

### 16.187.2. Consecuencias de escala para la calibración

1. V_cont truth pertenece a [0,1]; diferencias y efectos en esta escala también son acotados por construcción. Los bounds de intervalos ? se propagan al resultado y a los contrastes, sin colapsarlos.
2. La resolución K debe ser suficiente para representar interrupciones de duración relevante, pero no se elige por conveniencia estadística: se deriva de la semántica de continuidad, de los transitorios que deban distinguirse y del coste/precisión de observación. Ventana y K se fijan antes de observar resultados.
3. La rejilla temporal común no aumenta N_opportunities ni sustituye la oportunidad estandarizada única S6. S3 sigue siendo vector de señales imperfectas; no se promedia ni se interpreta directamente como A_B1.
4. La calibración del canal debe separar como mínimo: sensibilidad a estado 1, especificidad a estado 0, dependencia temporal de errores, cobertura/loss por intervalo, error diferencial por Z/versión y observación no ignorable. No se asignan tasas ni se presupone independencia.
5. Si el Analyzer no recibe información de calibración suficiente para identificar A_B1/V_cont, su salida correcta es bounds o abstención. La capacidad del Evaluator de calcular truth no autoriza revelar el modelo generador al Analyzer.

### 16.187.3. Diseño de calibración — superficie de recuperación, no MDE inventado

Para evitar fijar un único MDE sin criterio sustantivo, la calibración sintética debe evaluar una superficie de recuperación por estimando y por magnitud de contribución conocida:

- Incluir efecto focal nulo, positivo, negativo y heterogéneo; vías directas/colaterales e interacciones se varían separadamente de la contribución mediada por ΔT_acc*.
- Barrer una malla de magnitudes verdaderas de V_cont dentro del rango admisible [0,1], restringida por las distribuciones basales y los potenciales válidos. La malla y su resolución se derivan después de fijar K y el soporte; no se confunde con un MDE normativo.
- Para cada celda, reportar sesgo, RMSE, cobertura, error tipo I, potencia/curvas de detección, clasificación de signo, recuperación de magnitud, bounds coverage y tasas de abstención/no-identificación. Informar resultados por ITT_Z^D2, θ_A/θ_Af y C4 por separado, solo donde el estimando sea identificable.
- Incluir escenarios de medición calibrada por diseño y no calibrada/ambigua; S3 diferencial, pérdida/censura, UNKNOWN, soporte fallido, interferencia, vías colaterales, efecto directo, nulo y adversarial. Los escenarios deben conservar el truth conocido en el Generator y la información realmente permitida al Analyzer.
- Elegir N/π_h/estratos/unidad/clúster y R conjuntamente contra las restricciones aprobadas. La búsqueda produce curvas y una frontera Pareto de coste–precisión–recuperación; no se declara un único N confirmatorio mientras no exista un punto de operación con α, potencia, precisión y coste aceptados.
- R se incrementa hasta controlar SE_MC de las métricas de evaluación; no se confunde número de réplicas DGP con número de unidades experimentales N.

Esta estrategia permite evaluar falsabilidad y capacidad de recuperación en un rango completo sin inventar MDE. Para una afirmación confirmatoria puntual todavía habrá que escoger, ex ante, un punto de operación y sus criterios de error.

### 16.187.4. Parámetros: derivables frente a decisiones no deducibles

**Derivables por lógica/contrato:** rango [0,1] de V_cont; fórmula de igual peso por intervalo; propagación de UNKNOWN a bounds; separación de truth/observed; necesidad de estimandos por resultado; clasificación de escenarios nulo/positivo/negativo/colateral/medición degradada; uso de curvas de recuperación y SE_MC; exclusión de P178 como fuente de N/R confirmatorios.

**No derivables sin criterio científico explícito o especificación de soporte:** ventana y K; duración mínima de interrupción relevante; baseline/transitorios; MDE sustantivo; α, potencia y precisión exigidas; márgenes de equivalencia; rangos/probabilidades de parámetros DGP; dependencia temporal/correlación de señales; prevalencia de escenarios; N/ratio/estratos/clúster; R/tolerancia SE_MC; coste aceptable. No se rellenan con valores convencionales por defecto ni se importan cifras de P178.

### 16.187.5. Próxima consolidación mínima y gates

La próxima pasada no abrirá subpaquetes. Integrará en una sola ficha de calibración:
1. ventana/K derivadas del contrato funcional y de la escala temporal;
2. soporte y distribuciones conjuntas del DGP por etapa;
3. escenarios y rangos paramétricos con procedencia explícita;
4. curvas de recuperación/abstención por estimando;
5. frontera N–asignación–R–SE_MC;
6. punto de operación confirmatorio, si puede justificarse, o declaración de benchmark de recuperación sin claim confirmatorio puntual.

**Estado:** VCONT_SCALE_RULE_ACCEPTED_PROVISIONALLY / VCONT_MEASUREMENT_VALIDITY_CONDITIONAL / OCONF_DISCRIMINATION_NOT_VERIFIED / CALIBRATION_SURFACE_SPECIFIED_NOT_RUN / QUANTITATIVE_OPERATING_POINT_OPEN / DESIGN_FREEZE_NOT_READY / NO_EXECUTION_AUTHORIZED.

No se ejecuta código, validador, generación, simulación, estimación ni calibración computacional. `scientific_execution=false`; `execution_authorized=false`.

## 16.188. Cierre estructural del DGP y ledger integrado de parámetros (2026-11-12)

**Tipo:** reconciliación derivada de contratos existentes; no crea decisiones científicas ni parámetros numéricos.  
**Fuentes:** §§16.185–16.187; DEC-C10-053, 066, 067, 095–100; contratos DGP base, D2 población/soporte, causal architecture, PD, inventario finito, temporal B1, Outcome/Value y PE; S4R, MEAS, MISS, P177/P178/P179/P182/P183.

### 16.188.1. Precedencia y bloqueos heredados

1. §16.187 y DEC-C10-100 superseden las frases de §16.186 que presentaban abierta la decisión de agregación de V_cont. La escala está aceptada provisionalmente; validez de medición, ventana y K continúan abiertas.
2. El reloj del estudio t−1/t0…t9, la profundidad transformacional H y la duración/ventana de factibilidad son magnitudes distintas. H=3 permanece como profundidad máxima candidata, no como duración ni como fuente para fijar K.
3. La oportunidad estandarizada única por UE no es un intervalo de monitorización ni determina la rejilla V_cont.
4. El contrato B1 aún no especifica la operación funcional concreta que depende de ENABLED/PROFILE ni su criterio temporal de cumplimiento. No es lícito derivar duración de interrupción relevante, inicio/fin de ventana, frecuencia ni K. Este bloqueo afecta a la parametrización temporal sustantiva de V_cont, no al cierre del resto de la estructura generativa.
5. O-CONF/F* conserva su oráculo parcial y no se selecciona automáticamente como Outcome confirmatorio. Value general y sus dimensiones tampoco se completan por inferencia desde V_cont.

### 16.188.2. Esqueleto estructural único del DGP

Para cada unidad i, régimen z y etapa t, Generator construye una historia potencial versionada:

- **Basal pre-Z:** X_i, elegibilidad E_i, unidad de asignación UA_i/cluster_i, condiciones constitutivas C_i, frontera y versiones. Need_preZ y su evidencia permanecen en sus contratos y no son elegibilidad automática.
- **Asignación/política:** Z_i (o Z_cluster), probabilidad π_i/π_h y política D2 versionada. D2 es el contraste primario candidato; D1 es secundario y separado.
- **Provisión:** B_i(z) → W_attempt_i(z) → W_received_i(z) → S_install_i(z) → C_dep_i(z), conservando programación, intento, recepción, instalación, integridad, compatibilidad y operatividad como estados distintos. Ninguna etapa se copia automáticamente desde Z.
- **Estado transformacional:** T_cap, T_acc_i(z,t) y snapshots S_T,i(z,t). A_f_i(z,t) deriva de los predicados aplicables ID/REL/COND/AUTH/RES/DEP/¬BLOCK; App_f se evalúa desde el estado de entrada; D_f y ΔT_acc=(ΔU,ΔR,ΔC,ΔX) son objetos separados.
- **Grafo/rutas:** F1→F2 y A1→A2 son rutas candidatas del fixture finito, con R0–R3/S4R-A…D como escenarios de referencia. Cada paso requiere accesibilidad, aplicabilidad, composición, recursos, autorización, ventanas y bloqueos. Reach_H y Π_H se derivan del snapshot y universo cubierto, antes de selección/ejecución. H no es reloj.
- **Etapas posteriores:** conocimiento/consideración, selección, inicio y ejecución se generan por separado y después de Reach/Π; no se infieren desde accesibilidad ni redefinen población ITT.
- **Resultados:** O-CONF truth se adjudica por instancia×ruta en el estado terminal aplicado conforme F*. V_cont truth es la fracción temporal post-Z de A_B1 en rejilla común, con UNKNOWN propagado a bounds. Ningún resultado define otro.
- **Observación/evaluación:** observaciones, validez, cobertura, error, missingness, censura y adjudicación son procesos distintos de truth. Analyzer recibe solo la proyección sellada permitida; Evaluator abre truth tras sellar la salida.

Esto define orden y dependencias, no distribuciones paramétricas. Los potenciales por régimen reutilizan condiciones basales/versiones y reglas estructurales; solo cambian variables que la política puede afectar. Las dependencias comunes, directas, colaterales e interacciones se declaran expresamente, nunca se suponen ausentes por omisión.

### 16.188.3. Ledger de parámetros: fuente, estado y regla de cierre

| Bloque | Parámetros/objetos del contrato versionado | Estado y regla |
|---|---|---|
| Población basal | N, roster sintético, q_X, E_i, composición por estrato, UE/UA/cluster | OPEN. Soporte y unidad preceden al dimensionamiento; Need_preZ no filtra ITT. |
| Aleatorización | π_h, ratio, estratos, algoritmo, semilla, desviaciones | OPEN; no asumir 1:1. |
| Política D2/D1 | policy_id/version, reglas por Z, régimen control/tratamiento | Precedencia D2/D1 ACCEPTED; valores históricos .25/.80 no son tasas confirmatorias. |
| Provisión | reglas/probabilidades de intento, recepción, instalación, integridad, compatibilidad, operatividad | OPEN. Transiciones separadas; sin independencia ni tasas por defecto. |
| Dependencias/accesibilidad | C_dep componentes, predicados A_f, App, D_f, T_acc y sus cuatro deltas | Estructura parcial; dominios, soporte y dependencias paramétricas OPEN. |
| Rutas/Reach | catálogo cubierto, relaciones, G, H, recursos, ventanas, bloqueos, alternativas | F1/F2/A1/A2 y R0–R3 son fixture candidato; H=3 solo profundidad candidata; F*/G/ventanas y exhaustividad OPEN. |
| Outcome O | predicados FP, IAM/mapping, snapshots, evento terminal, oráculo y error | O-CONF parcial; no endpoint confirmatorio congelado. |
| V_cont | operación B1, A_B1, ventana, K, duración mínima relevante, baseline/transitorios | Escala DEC-C10-100 ACCEPTED; operación y reloj funcional incompletos; ventana/K OPEN. |
| Canal S3 | vector de señales, sensibilidad/especificidad, error temporal, correlación, cobertura/loss, diferencialidad por Z/versión | Estructura pasiva aceptada; tasas y modelo OPEN; sin independencia asumida. |
| Observación general | MCAR/MAR/MNAR, pérdida, censura, selección, validez/invariancia | Taxonomía existente; parámetros/escenarios OPEN. |
| Interferencia | exposición, recursos/pools compartidos, cluster, spillovers | OPEN; aislamiento por construcción o modelo de exposición explícito. |
| Causalidad | efectos focales, directos, colaterales, interacciones, heterogeneidad, defiers y monotonicidad | Variar como escenarios conocidos; rangos/distribuciones OPEN. |
| Calibración | α, potencia, precisión, MDE/relevancia, equivalencia, tolerancias, N, R, SE_MC y coste | Normativo/operativo OPEN; ningún valor importado de P178. |

Cada parámetro debe tener ID, definición, unidad/escala, dominio, nivel (unidad/cluster/etapa/intervalo), momento, papel causal, distribución/regla estructural, dependencias, potenciales afectados, procedencia, estado de aprobación, rango de sensibilidad, versión y restricciones de soporte. Un parámetro sin procedencia o dominio explícito invalida la configuración; no recibe default silencioso.

### 16.188.4. Matriz finita mínima de escenarios sin factorial completo

La selección se organiza por falsador/contraste y no por el producto cartesiano de todos los factores. Perfiles mínimos:

1. **Focal aislado:** D2 cambia provisión focal; sin vía directa/colateral, con soporte y medición estipulados. Evalúa ITT-paquete y, solo bajo mapping/régimen identificados, atribución focal.
2. **Nulo/primera etapa nula:** Z no cambia cadena focal; impide fabricar efecto o primera etapa.
3. **Fallo por etapas:** intento/recepción/instalación ocurren, pero C_dep o A_f no se abren.
4. **Focal adverso:** la política deteriora una dimensión de ΔT_acc, Reach o V_cont; no imponer monotonicidad positiva.
5. **Vía directa:** B afecta O/V sin pasar por ΔT_acc; clasificar efecto de paquete/no atribución focal.
6. **Vía colateral/alternativa:** B altera A1/A2, dependencias, recursos, seguridad, latencia, información o coste; exclusión focal no se presume.
7. **Interacción/heterogeneidad:** efecto dependiente de condiciones basales, alternativa, recursos o unidad; no transportar LATE entre D1/D2.
8. **IV adversarial:** instrumento nulo/débil, defiers, exclusión o monotonicidad violadas; no usar Wald cuando no procede.
9. **Medición adversarial:** S3 diferencial, temporalmente correlacionado, con cobertura incompleta o no ignorable; bounds/abstención cuando corresponda.
10. **Soporte/interferencia/versionado:** positividad fallida, historia imposible, spillover/cluster, crossover o versiones asignada/recibida/aplicada divergentes.
11. **O/V no discriminables:** interrupción temporal y conformidad terminal no separables con observación/oráculo disponible; abstenerse de afirmar discriminación.

No se requiere cruzar todos los perfiles con todos los parámetros. Cada contraste causal, interacción crítica y falsador debe tener escenario positivo y control negativo apropiado; las combinaciones omitidas requieren justificación. Métricas por estimando, resultado y escenario, nunca un promedio global que oculte fallos.

### 16.188.5. Estimandos y reglas de salida del Analyzer

- **ITT-D2 por resultado:** contraste de resultados potenciales bajo asignación D2 en población/unidad declaradas. Interpreta efecto total del paquete; requiere asignación, población, consistencia, soporte e interferencia especificados.
- **Primeras etapas:** estimandos separados para intento, recepción, instalación, C_dep, A_f, D_f y ΔT_acc.
- **Accesibilidad g_A:** intervención estocástica sobre distribuciones factibles del ΔT_acc completo bajo q basal común y régimen no focal común. No se identifica por el ITT-D2; requiere mapping, soporte y régimen común.
- **C4 interventional:** contribución mediada por el cambio estructural completo; requiere intervención longitudinal, control de confusión post-Z y positividad secuencial. Nunca se calcula por resta ITT−θ_A.
- **LATE:** solo con relevancia, independencia, exclusión, monotonicidad, consistencia/versiones y no interferencia; si no, weak-IV, bounds o NOT_IDENTIFIED.
- **O-CONF y V_cont:** estimandos separados con medición/error propios. Identificación de ITT-O no valida ITT-V ni viceversa.
- **Salida obligatoria:** por estimando, IDENTIFIED, CONDITIONALLY_IDENTIFIED, BOUNDS_ONLY, NOT_IDENTIFIED, NOT_INSTANTIATED o INDETERMINATE_MEASUREMENT, con razones/supuestos visibles. No convertir no significación en equivalencia ni ausencia de evidencia en cero.

### 16.188.6. Orden de cierre cuantitativo y regla de parada

Secuencia única: (A) cerrar semántica funcional B1 y reloj/ventana; (B) cerrar soporte basal, unidad de asignación/interferencia y distribuciones estructurales; (C) cerrar funciones de transición/potenciales y parámetros de observación; (D) congelar matriz finita de escenarios y contrastes; (E) aprobar criterios normativos de error/relevancia/precisión; (F) buscar conjuntamente N, asignación, clúster y R y derivar frontera coste–precisión–recuperación.

La calibración numérica no comienza mientras A–E estén abiertos. Si B1 no permite derivar una duración funcionalmente relevante, V_cont se conserva como resultado temporal vectorial/bounds y no se inventa K. Si C3/C4 no satisfacen identificación/soporte, el benchmark evalúa abstención/recuperación de no-identificación; no se les asigna potencia como si fueran estimandos identificados.

**Estado:** DGP_STRUCTURAL_SKELETON_RECONCILED / PARAMETER_LEDGER_DEFINED_BUT_UNPOPULATED / ADVERSARIAL_SCENARIO_SET_SPECIFIED_NOT_INSTANTIATED / VCONT_WINDOW_K_BLOCKED_BY_B1_OPERATIONAL_SEMANTICS / SUPPORT_AND_RANDOMIZATION_OPEN / CALIBRATION_NOT_RUN / DESIGN_FREEZE_NOT_READY / NO_EXECUTION_AUTHORIZED.

No se ha creado código, schema físico, fixture, truth, roster, dato ni resultado. No se han ejecutado validadores, generación, simulación, estimación o calibración computacional. scientific_execution=false; execution_authorized=false.


## 16.189. Precedencia funcional B1 y especificación temporal de V_cont (2026-11-12)

**Reconciliación correctiva de §16.188.1 y §16.188.3.** La frase que declara no especificada la operación funcional B1 queda supersedida: la función de referencia ya está definida como contrato funcional de trabajo en `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md` §2, `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md` §13 y DEC-C10-068. No se reabre ni amplía.

### 16.189.1. Función B1 vigente

Para cada intervalo post-Z, el constructo latente `A_B1(i,k)` representa conformidad con la función mínima del servicio lógico vinculado a B1:

1. **Regla de admisión:** cuando PAR-SVC-ENABLED=true, el servicio tiene capacidad funcional de admitir solicitudes dirigidas a él; cuando es false, no las admite. La ausencia de solicitudes durante un intervalo no equivale a incumplimiento ni a cumplimiento observado.
2. **Exposición de perfil:** el servicio expone el PAR-SVC-PROFILE declarado para la instancia/versión aplicable. STANDARD y READ_ONLY siguen siendo perfiles diferenciados por etiqueta, sin atribuirles capacidades de negocio adicionales.
3. **Conformidad conjunta:** el estado funcional del intervalo es 1 cuando ambos requisitos aplicables se cumplen; 0 ante incumplimiento funcional estipulado y suficientemente determinado; ? cuando la truth del intervalo no puede determinarse. La falta de señal S3 es un problema de observación, no una conversión automática de truth a ?.

La definición es de capacidad/regla funcional latente, no de conteo de peticiones, tasa de respuestas, éxito de procesamiento, ejecución F*, Outcome o Value. Una petición observada puede aportar evidencia de admisión, pero no sustituye el estado funcional del intervalo. No se añade payload, SLA, timeout, retry, carga, concurrencia ni semántica de negocio.

### 16.189.2. Separaciones temporales obligatorias

- `t−1/t0…t9` es el reloj de etapas causales del estudio, no una rejilla de intervalos de igual duración.
- `k=1…K` indexa intervalos iguales de la ventana de V_cont; K no se deduce del número de etapas t ni de H=3.
- H=3 es profundidad transformacional candidata, no horizonte temporal.
- La oportunidad lógica S7 única por UE (DEC-C10-098) pertenece al canal declarativo pre-Z de Need_preZ; no es una repetición de probes ni determina K.
- La oportunidad estandarizada post-snapshot pertenece a su contrato propio; no se multiplica ni reutiliza como observación repetida de continuidad.
- S3 sigue siendo observación pasiva imperfecta; no se convierte en verificador directo ni en verdad.

### 16.189.3. Ventana: recomendación y decisión pendiente

Para que V_cont represente continuidad y no solo estado terminal, la recomendación de diseño es que la ventana post-Z comience en t0 (asignación), de modo que no se excluya por definición una posible interrupción durante provisión/instalación. Su extremo final debe ser un horizonte de seguimiento fijo, común y preespecificado, expresado en tiempo de estudio y no en número de etapas causales.

Esta elección es una recomendación derivada del constructo, no una decisión aceptada. Permanecen sin fijar: duración del horizonte, unidad temporal, resolución mínima defendible, K y regla para eventos/transitorios en fronteras de intervalo. No se usarán t9, H=3 ni la cardinalidad S7 como sustitutos de esos parámetros. Si se decide otra ancla inicial, deberá justificarse por qué la continuidad durante la provisión queda fuera del resultado.

### 16.189.4. Agregación ya aceptada

DEC-C10-100 permanece vigente: con K intervalos iguales, V_cont_truth es la fracción temporal de intervalos conformes. UNKNOWN se propaga a cotas; no se imputa cero ni se elimina del denominador. Esta sección no altera la escala, no fija K y no valida S3.

### 16.189.5. Estado y siguiente operación

**FUNCTIONAL_REFERENCE_SPECIFIED / INTERVAL_TRUTH_CONTRACT_RECONCILED / WINDOW_START_T0_RECOMMENDED_NOT_APPROVED / HORIZON_RESOLUTION_K_OPEN / S3_CALIBRATION_OPEN / NO_DESIGN_FREEZE.**

La siguiente operación es cerrar la ventana y resolución temporal con el reloj causal y el objetivo de continuidad, después especificar el canal S3 por intervalo. No se materializan intervalos, señales, truth, roster, fixtures ni datos. No se ejecuta código, calibración ni simulación. `scientific_execution=false`; `execution_authorized=false`.

## 16.190. Aceptación del inicio t0 y cierre del contrato temporal observable de V_cont (2026-11-12)

**Tipo:** aceptación expresa del usuario para el ancla inicial + reconciliación metodológica derivada; no fija horizonte ni resolución por inferencia.  
**Precedencia:** DEC-C10-068 (función B1), DEC-C10-099 (selección V_cont), DEC-C10-100 (agregación igualitaria), §§16.180–16.183, §16.187, §16.189, auditoría temporal/S4R y contratos U_G/PE, P182/P183/MEAS/MISS.

### 16.190.1. Decisión temporal aceptada

Se acepta iniciar la ventana de V_cont en **t0, inmediatamente después de la asignación Z**, incluyendo provisión, intento, recepción, instalación, verificación y el resto de la trayectoria causal posterior que quede dentro del horizonte de seguimiento. La ventana inicial no se condiciona a recepción, instalación, C_dep, A_f, Reach, selección o ejecución. Así se evita excluir del resultado precisamente las interrupciones que la política asignada pudiera producir durante la provisión.

La regla se aplica simétricamente a los brazos D2 y a la población/versión declaradas. El estimando continúa siendo el nivel post-Z en la ventana común, no un cambio pre/post. El baseline pre-Z conserva función descriptiva y solo podrá utilizarse como ajuste si queda preespecificado.

### 16.190.2. Ventana y relojes

La ventana queda representada como W_V=[t0,T*], donde T* es un horizonte final post-Z común, fijo y preespecificado. La aceptación de t0 **no** determina la duración ni autoriza identificar T* con t9: t0…t9 es un orden de etapas causales, no un reloj físico de duración conocida. Tampoco se deriva T* de H=3, de la oportunidad S6/S7 ni de la cardinalidad de solicitudes.

Se mantienen tres ejes:
- reloj causal del estudio t−1,t0…t9;
- rejilla de continuidad k=1…K, con intervalos de igual duración sobre [t0,T*];
- profundidad transformacional h=0…H y ventanas de factibilidad por paso.

T*, unidad temporal, K, duración de intervalo, tolerancia de alineación de timestamps y regla de adjudicación de eventos que cruzan fronteras siguen OPEN. La elección de T* deberá cubrir el periodo causal cuya continuidad se pretende valorar y permitir observar recuperación/persistencia sin seleccionar el horizonte tras ver los resultados.

### 16.190.3. Regla temporal de truth y eventos

Se conserva A_B1(i,k) como truth funcional latente del intervalo, determinada por Generator conforme al contrato ENABLED/PROFILE versionado. No se convierte en una variable derivada de telemetría. Los intervalos tienen igual duración y denominador K fijo. Si el DGP no determina el estado de un intervalo, se conserva como desconocido y el Evaluator calcula bounds conforme DEC-C10-100.

No se ha aprobado aún si un fallo breve dentro de un intervalo hace que todo el intervalo sea 0, ni una duración mínima de interrupción relevante, regla de continuidad en fronteras o tratamiento de transitorios. Estos elementos deben derivarse conjuntamente de la semántica temporal del objetivo y de la resolución de observación. No se asigna una tolerancia de gracia ni se ignoran eventos por conveniencia.

### 16.190.4. S3: contrato de observación por intervalo reutilizando U_G

Se reutiliza exclusivamente S3 como familia temporal runtime candidata, con el apoyo contextual de S4 (identidad/versión/integridad) y S5 (contrato ENABLED/PROFILE). S4 y S5 no sustituyen observación runtime. No se crea clase de fuente, actor, interfaz, ledger, artefacto, endpoint ni oportunidad adicional.

El vector conceptual S3 por UE×intervalo conserva, cuando estén en alcance y sean observables, cinco familias no colapsadas:
1. proceso/módulo runtime;
2. superficie de recepción (listener/socket y estado asociado);
3. dependencias runtime necesarias;
4. capacidad/recursos/cola, solo si el DGP define su significado y unidad;
5. perfil runtime asociado al PROFILE versionado.

Cada componente puede ser 1/0/? conforme a evidencia afirmativa válida, silencio/captura ausente, invalidez, contradicción, censura o falta de cobertura. Un 0 de componente requiere evidencia positiva de incumplimiento de ese componente; ausencia de traza no es 0. Ningún componente individual ni su conjunción automática, score o media se declara equivalente a A_B1. No se envían solicitudes de negocio ni se activa una ruta para observar; S3 permanece pasivo y no mutante.

El Generator define la truth latente y genera separadamente el proceso observacional conjunto P(O_S3(i,k) | A_B1(i,k), M(i,k)). M solo contendrá mecanismos explícitos de emisión, captura/retención/pérdida, cobertura, validez, temporalidad, error semántico, censura y dependencias entre señales. No se presume independencia condicional, sensibilidad/especificidad constantes, MCAR/MAR/MNAR ni invariancia entre brazos/versiones. Los mecanismos que por diseño deban ser pre-Z/invariantes no pueden depender de Z, D2 ni variables downstream; los mecanismos de monitorización post-Z se especifican como proceso de medición del resultado, con diferencialidad explícita si la política puede afectarlos.

El Analyzer recibe únicamente S3 observado, identidad/versionado, timestamps, cobertura/provenance y la información de calibración permitida y preespecificada. No recibe A_B1, V_cont_truth, potenciales, semillas ni parámetros reservados. El Evaluator accede a truth solo después del sellado. Sin modelo identificable y calibración accesible: bounds justificados o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT, nunca una media bruta de señales ni complete-case.

### 16.190.5. Cobertura y alineación temporal

La cobertura se informa por UE×intervalo×componente S3 y para la ventana completa, manteniendo separados: oportunidad de observación prevista, emisión, captura, validez, disponibilidad, pérdida, censura y evidencia admisible. No se declara cobertura completa por haber encontrado todas las señales disponibles. Los timestamps se vinculan a la identidad y versión de la instancia; desalineación, lag, muestreo, rutas no activadas y eventos raros se mantienen como mecanismos explícitos. No se interpola un estado 1/0 a través de huecos sin regla validada.

S3 no aumenta el número de unidades experimentales ni las oportunidades de petición. Las observaciones repetidas se anidan en UE; la inferencia causal respeta UE/UA/clúster y posible dependencia intr unidad.

### 16.190.6. Dictamen y siguiente cierre

**ACCEPTED:** inicio de ventana en t0, inclusión de provisión/instalación, horizonte común por brazo, rejilla de igual duración y agregación DEC-C10-100.  
**SPECIFIED_DOCUMENTALLY:** separación de relojes; estructura vectorial S3; proceso conjunto de medición; estados de cobertura/error; firewall y reglas de abstención.  
**OPEN:** T*, unidad temporal, K, duración mínima relevante, semántica de fallo breve/transitorios/fronteras, indicadores S3 concretos, dependencia/correlación, error, cobertura, calibración, sensibilidad y discriminación O-CONF.

Siguiente cierre integrado: (i) decidir si el constructo exige continuidad estricta o tolera interrupciones de duración acotada; (ii) derivar unidad y resolución de intervalo desde esa regla y las capacidades de observación S3; (iii) elegir T* en relación con la última consecuencia causal incluida, sin equipararlo automáticamente a t9; (iv) poblar rangos/sensibilidades del canal solo con procedencia explícita. No se crean parámetros, fixtures, roster, truth, señales, schema físico o código. No se ejecutan validadores, generación, simulación, estimación ni calibración. scientific_execution=false; execution_authorized=false.


## 16.191. Criterio candidato de continuidad estricta dentro de cada intervalo (2026-11-12)

**Estado:** DERIVACIÓN SEMÁNTICA RECOMENDADA / NO ACEPTADA COMO DECISIÓN NORMATIVA.

El contrato B1 habla de mantener disponible la capacidad funcional, no de alcanzar una tasa media de disponibilidad ni de tolerar una cuota de interrupciones. La interpretación más fiel para la truth binaria por intervalo ya aceptada es:

- A_B1(i,k)=1 si la regla ENABLED/PROFILE se cumple durante todo el intervalo k.
- A_B1(i,k)=0 si existe al menos un incumplimiento funcional positivo y suficientemente determinado dentro del intervalo.
- A_B1(i,k)=? solo si el Generator no puede determinar la truth funcional del intervalo; la falta de S3 es incertidumbre observacional y no modifica la truth reservada.

Esta lectura implica continuidad estricta dentro del intervalo: no se introduce un periodo de gracia ni una duración mínima de fallo que el contrato B1 no haya definido. Un fallo breve confirmado cuenta como incumplimiento del intervalo. La resolución temporal y la sensibilidad del canal S3 deben ser capaces de detectar los eventos que el DGP estipule; si no, el Analyzer deberá abstenerse o producir bounds, no reinterpretar el silencio como continuidad.

La regla es una derivación semántica candidata, no una decisión aceptada. La alternativa —permitir transitorios de hasta una duración δ— exigiría una regla normativa nueva, definir δ y justificarla desde el objetivo de B1; no se inventará.

**Consecuencia para K:** K no se elige para diluir interrupciones ni por conveniencia estadística. Debe ser compatible con la escala temporal de eventos que el DGP pretende representar y con la capacidad de observación S3. Mientras no se apruebe la semántica de transitorios y no se determine el alcance temporal de eventos detectables, K permanece OPEN.

**Siguiente gate:** aceptación o rechazo expreso de la continuidad estricta por intervalo. No se solicita aún una cifra de δ, frecuencia, K o T*.


## 16.192. Aceptación de continuidad estricta por intervalo para V_cont (2026-11-12)

**Decisión:** DEC-C10-102 · **Estado:** ACCEPTED WORKING DESIGN DECISION · NOT DESIGN FREEZE.
**Precedencia:** DEC-C10-068, DEC-C10-099, DEC-C10-100, DEC-C10-101; contrato B1 ENABLED/PROFILE; §§16.190–16.191.

El usuario acepta la interpretación estricta de continuidad dentro de cada intervalo, sin periodo de gracia para interrupciones funcionales confirmadas.

Para cada UE i e intervalo k:
- A_B1(i,k)=1 si la regla funcional ENABLED/PROFILE se cumple durante todo el intervalo.
- A_B1(i,k)=0 si se produce al menos un incumplimiento funcional confirmado en cualquier instante del intervalo.
- A_B1(i,k)=? solo cuando la truth funcional del intervalo no queda determinada por el Generator. UNKNOWN de truth no se usa para representar falta de S3, pérdida, lag o cobertura observacional: esos son estados del canal observado.

No se introduce duración mínima de fallo, periodo de gracia, cuota tolerada de interrupciones ni promedio intraintervalo. Un fallo breve pero confirmado cuenta como incumplimiento del intervalo. La frontera temporal se adjudica por el intervalo al que pertenece el instante del evento según la rejilla común; el tratamiento de timestamps exactamente en frontera deberá ser determinista, único y versionado antes de materializar.

### 16.192.1. Consecuencias para la medición y el diseño

La truth la estipula el Generator con resolución suficiente para determinar los eventos del DGP; S3 es un canal de observación imperfecto y no define truth. El Analyzer no puede declarar continuidad por ausencia de señal ni inferir que la falta de detección equivale a ausencia de interrupción. Si la resolución/cobertura del canal no soporta la clasificación puntual, se producen bounds o abstención y se informa la limitación.

La decisión no fija por sí sola una frecuencia física de S3, duración del intervalo, K o T*. La resolución deberá permitir representar los eventos más breves que el DGP incluya como funcionalmente relevantes; si no existe un límite mínimo justificable para esos eventos, no se podrá alegar detección exhaustiva de cualquier interrupción arbitrariamente breve. Esta limitación se reflejará en el dominio de validez del estimando de medición.

### 16.192.2. Derivación del horizonte y rejilla: dictamen

El horizonte V_cont empieza en t0 (DEC-C10-101) y termina en un T* post-Z común que debe cubrir el periodo de provisión/instalación y el seguimiento funcional hasta el último evento causal que pueda modificar el cumplimiento B1 dentro del estimando. El mapa t0…t9 es un orden de etapas; no proporciona duraciones ni permite asignar automáticamente intervalos iguales a etapas. Por ello, T* no se fija como t9 sin un contrato de reloj/event_time y una regla de cierre.

La opción metodológicamente preferida para el DGP sintético es un reloj explícito de tiempo transcurrido (unidad normalizada declarada) con eventos fechados, ventana común [t0,T*] y rejilla regular. Los eventos causales se insertan en ese reloj mediante offsets/duraciones generados por reglas versionadas; no se asigna una duración igual por etapa ni se usa el número de etapas como K. La duración/unidad del tick y el horizonte deberán derivarse de las duraciones funcionales que el escenario pretende representar y de la resolución alcanzable por S3.

K se deriva de K=(T*−t0)/Δ, con Δ constante y una regla de divisibilidad preespecificada; si la duración no es múltiplo exacto de Δ, se ajusta el horizonte antes de generar, no se crea un intervalo residual de distinta duración. Δ debe ser suficientemente fino para el mínimo evento funcional incluido y observable; no se elige para diluir fallos ni se infiere de H, t0…t9 o S6/S7.

Permanecen OPEN: unidad normalizada y su anclaje semántico, conjunto de eventos funcionalmente relevantes y su mínima duración representada, T*, Δ, K, timestamps exactos, regla de cierre/fin de seguimiento, distribución de duraciones, resolución de captura S3, cobertura y calibración. La recomendación de reloj transcurrido y rejilla regular queda SPECIFIED AS DESIGN ROUTE, no como parámetros numéricos aceptados.

### 16.192.3. Próxima operación vinculante

Reconciliar el reloj transcurrido con el contrato B1 y los eventos existentes, sin crear un segundo reloj ni una nueva clase de fuente: (i) inventariar eventos/estados que pueden cambiar A_B1 durante provisión, instalación y seguimiento; (ii) determinar cuáles son funcionalmente relevantes y qué duración mínima puede justificarse; (iii) definir la relación de sus event_time con S3 y S4/S5; (iv) derivar conjuntamente Δ, T* y K; (v) actualizar el modelo de observación, los potenciales V_cont y el crosswalk PE. Solo entonces parametrizar el canal y calibrar.

No se asignan números arbitrarios, no se materializan eventos/intervalos/truth/señales, y no se ejecutan validadores, generación, simulación, estimación o calibración. scientific_execution=false; execution_authorized=false.

## 16.193. Inventario de eventos B1 y reconciliación de la escala temporal V_cont (2026-11-12)

**Alcance:** derivación documental de DEC-C10-068/100/101/102; no crea una nueva decisión normativa ni autoriza ejecución.

### 16.193.1. Inventario funcional y causal

Se reutiliza el contrato B1 §2 y la reconciliación temporal §8–10. La conformidad funcional exige: (a) admitir solicitudes cuando el estado efectivo ENABLED=true; (b) no admitirlas cuando ENABLED=false; y (c) exponer el PROFILE declarado. STANDARD y READ_ONLY no reciben semántica adicional.

| Clase | Eventos/estados que deben representarse | Papel respecto de A_B1 |
|---|---|---|
| Provisión | programación, intento, recepción/disponibilidad de componentes | Antecedentes causales; no son por sí mismos conformidad ni fallo |
| Instalación | aplicación, verificación, integridad, compatibilidad, operabilidad, rollback | Pueden modificar el estado efectivo; se adjudica el resultado funcional, no la etiqueta de instalación |
| Configuración funcional | cambio efectivo ENABLED; cambio efectivo PROFILE; versión/identidad de instancia y configuración | Determinantes directos o de binding de la regla B1 |
| Operación runtime | proceso/módulo disponible o detenido; listener/socket/superficie de recepción; pérdida/recuperación de dependencia; capacidad/recursos cuando sean constitutivos de la admisión; reinicio, caída y recuperación | Estados/eventos que pueden impedir o restituir la capacidad funcional; la señal observada no sustituye a truth |
| Solicitud | oportunidad, intento, recepción, admisión/rechazo, procesamiento y respuesta | Interacción discreta. Una oportunidad estandarizada no es monitor continuo; la ausencia de solicitud no es fallo y la respuesta no define por sí sola continuidad |
| Transformación/valor | Reach, selección, inicio, ejecución, F*, O-CONF, Outcome y Value | No son indicadores constitutivos de A_B1 ni sustitutos de S3 |

La verdad del Generator debe registrar el estado funcional efectivo y sus transiciones con event_time suficiente para determinar si hubo algún incumplimiento dentro de cada intervalo. Provisión, instalación, reinicio o dependencia son antecedentes/eventos explicativos: solo afectan A_B1 cuando el estado funcional resultante incumple la regla. S4 conserva identidad/versionado/snapshot; S5 fija la semántica declarativa ENABLED/PROFILE; S3 observa pasivamente proceso/módulo, listener/socket/superficie, dependencias, capacidad/recursos si están definidos y perfil runtime.

### 16.193.2. Reconciliación de reloj, rejilla y observación

Se distingue formalmente:
- **Reloj de truth:** event_time de cambios del estado funcional efectivo estipulados por Generator.
- **Rejilla de agregación:** partición común de [t0,T*] en K intervalos iguales, sobre la que se aplica la regla estricta DEC-C10-102.
- **Reloj de observación S3:** timestamps de emisión/captura, cobertura, lag y pérdida del canal pasivo. Su frecuencia/resolución no se iguala por definición a Δ.

Por tanto, Δ no es automáticamente la frecuencia de polling S3. El Generator puede determinar truth a partir de su historial de eventos; S3 solo permite recuperarla si su modelo de observación y cobertura lo identifican. Un canal basado únicamente en snapshots espaciados no garantiza detectar interrupciones breves entre snapshots. No se añaden probes ni solicitudes activas para resolverlo.

### 16.193.3. Consecuencia matemática que debe corregirse en la interpretación de V_cont

La combinación aceptada DEC-C10-100 + DEC-C10-102 implica V_cont_truth(i)=(1/K)Σ_k A_B1(i,k), donde A_B1 vale 1 solo si todo el intervalo cumple y 0 si existe cualquier incumplimiento confirmado.

Esta cantidad es la **proporción de intervalos completamente conformes**, no la fracción exacta del tiempo transcurrido en conformidad. Una interrupción breve confirmada convierte en 0 el intervalo completo; por ello, el resultado depende de Δ y de la alineación de la rejilla. No se debe describir como integral temporal ni como porcentaje exacto de uptime. Se preservan la fórmula y las decisiones aceptadas; se corrige únicamente la interpretación semántica derivada. Si el objetivo científico fuese medir la fracción exacta de tiempo disponible, requeriría otra operacionalización y una decisión explícita, que no se introduce aquí.

### 16.193.4. Fronteras y cierre

Para una rejilla futura con b_k=t0+kΔ, la convención determinista recomendada es [b_k,b_{k+1}) para intervalos internos: un evento exactamente en una frontera interna pertenece al intervalo que comienza en esa frontera. El último intervalo incluye T* como extremo terminal. Un episodio que se extienda a través de una frontera afecta a cada intervalo cuyo interior intersecte el periodo de incumplimiento. La convención deberá versionarse antes de materializar.

T* no se equipara a t9. Para no censurar la duración de un evento terminal, el contrato de cierre deberá identificar el último evento causal del DGP capaz de modificar A_B1 y un seguimiento común posterior suficiente para observar persistencia/recuperación. Puede expresarse como T*=t_last+τ_follow, con τ_follow fijado ex ante; tanto el evento terminal como τ_follow siguen OPEN hasta definir el catálogo de escenarios y su escala temporal.

### 16.193.5. Dictamen y siguiente operación

**EVENT_INVENTORY_RECONCILED / TRUTH_CLOCK_SEPARATED_FROM_S3_CADENCE / STRICT_BLOCK_SCORE_NOT_ELAPSED_TIME_FRACTION / BOUNDARY_RULE_RECOMMENDED / TSTAR_DELTA_K_OPEN.**

La siguiente operación debe cerrar el catálogo finito de transiciones que el DGP permite, el mínimo episodio funcional que el escenario pretende representar, la capacidad realista de S3 para capturarlo y el seguimiento terminal. Después se derivan conjuntamente unidad normalizada, τ_follow, T*, Δ y K. No se fijan cifras por analogía ni por conveniencia estadística.

No se generan eventos, intervalos, truth, señales ni fixtures. No se ejecuta código, simulación, estimación, calibración ni validación. scientific_execution=false; execution_authorized=false.

## 16.194. Catálogo funcional finito y separación entre verdad de fallo y detectabilidad S3 (2026-11-12)

**Alcance:** derivación documental de DEC-C10-068/100/101/102 y del contrato de trabajo B1 §2; no añade una tolerancia ni una nueva decisión normativa.

### 16.194.1. Estado funcional que adjudica V_cont

Se reutiliza el contrato de trabajo B1: cuando ENABLED=true, el servicio debe admitir solicitudes; cuando ENABLED=false, no debe admitirlas; debe exponer el PROFILE declarado. STANDARD y READ_ONLY no reciben semántica de negocio diferenciada. La regla RUL de DEC-C10-068 sigue siendo una implicación declarativa y no se amplía a una equivalencia.

La truth A_B1 se determina por el cumplimiento conjunto de esa función durante el intervalo. El catálogo causal se limita a cinco familias finitas de transición:
1. **Configuración efectiva:** cambios de ENABLED o PROFILE, incluida una configuración declarativa incompatible con RUL.
2. **Proceso/módulo:** pérdida y recuperación de la capacidad runtime necesaria para admitir.
3. **Frontera de ingreso:** listener/socket/superficie de recepción que deja de estar disponible o se recupera.
4. **Dependencias:** pérdida/recuperación de una dependencia solo cuando impide/restaura la admisión funcional.
5. **Capacidad/recursos:** insuficiencia/restauración solo cuando impide/restaura la admisión funcional.

Provisión, recepción de componentes, instalación, verificación, rollback y reinicio son eventos antecedentes o de transición entre estados; no se etiquetan automáticamente como fallo. Solo cambian A_B1 si el estado funcional efectivo resultante incumple o vuelve a cumplir la regla. No se agregan causas técnicas nuevas por separado.

### 16.194.2. Separación de estados y eventos

Para cada transición el Generator conserva unidad/instancia, versión, event_time, estado funcional efectivo anterior y posterior, familia causal y referencia de provenance. El registro de transición no sustituye la verdad adjudicada del intervalo.

- **Incumplimiento funcional:** ENABLED=true sin capacidad de admisión; ENABLED=false con admisión; PROFILE declarado no expuesto conforme al contrato; o estado declarativo incompatible con la regla constitutiva aceptada.
- **Restitución:** transición que devuelve el servicio a conformidad; no borra el incumplimiento anterior del intervalo.
- **No-evento:** ausencia de una solicitud o de una señal no prueba conformidad ni incumplimiento.
- **Solicitud:** la oportunidad estandarizada única por UE y sus eventos attempt/received/admitted/rejected/processing/response permanecen como eventos discretos; no se convierten en monitor repetido ni sustituyen S3.

La función de servicio, no el nombre de la causa técnica, determina A_B1. STANDARD/READ_ONLY siguen sin semántica diferenciada.

### 16.194.3. Duración funcional y límite de observación

DEC-C10-102 no establece duración mínima funcional ni periodo de gracia: cualquier incumplimiento confirmado, por breve que sea, hace A_B1=0 en cada intervalo afectado. Esto no exige afirmar que S3 detecta cualquier episodio arbitrariamente breve.

Se introduce una distinción de diseño, no una nueva tolerancia:
- δ_event: duración efectiva del episodio estipulado por Generator; puede ser positiva y breve, sin cambiar la regla truth.
- δ_det: dominio mínimo de duración para el que el canal S3 pueda demostrar una capacidad de detección bajo un modelo de captura/cobertura calibrado. Es una frontera de validez de medición, no un filtro de truth ni un periodo de gracia.

Para episodios inferiores a δ_det, truth conserva su valor (incluido A_B1=0 si hubo incumplimiento), pero Analyzer no puede afirmar recuperación puntual salvo que otro componente pasivo autorizado lo identifique. Debe producir bounds o abstención. No se fija δ_det ni se presupone que S3 sea event-driven, periódico, continuo, independiente o completo. La función de detección, lag, pérdida, cobertura, dependencia entre señales y sensibilidad quedan para especificación/calibración.

### 16.194.4. Relación de escalas y cierre terminal

Δ define la anchura de los bloques de adjudicación; no es la cadencia S3 ni δ_det. La elección futura debe satisfacer conjuntamente: (i) representar los episodios que el DGP declara en su dominio; (ii) permitir adjudicar cada bloque sin ocultar incumplimientos entre capturas; y (iii) conservar K=(T*−t0)/Δ entero, con bloques iguales. Si no se demuestra la condición de observabilidad, el resultado se acota o no se identifica; no se relaja DEC-C10-102.

t_last se define como el tiempo de la última transición causal del DGP que pueda cambiar A_B1, incluida la recuperación final si ocurre. τ_follow es el seguimiento común posterior a esa transición para observar persistencia y cerrar el registro. T*=t_last+τ_follow. Un episodio aún activo al final del horizonte no se codifica como recuperado: debe quedar como estado terminal/censura explícita según contrato, sin imputación.

### 16.194.5. Dictamen

**FINITE_CAUSAL_FAMILIES_BOUNDED / NO_MINIMUM_FUNCTIONAL_FAILURE_DURATION / DETECTION_DOMAIN_SEPARATE_FROM_TRUTH / S3_DETECTABILITY_UNCALIBRATED / TSTAR_DELTA_K_OPEN.**

Siguiente derivación única: definir unidad normalizada y escala de episodios mediante el catálogo de escenarios ya aceptado; caracterizar el canal S3 que realmente puede implementarse pasivamente; y derivar δ_det, Δ, τ_follow, T* y K en una sola tabla de calibración. No se eligen valores sin anclaje semántico ni evidencia de recuperación.

No se generan transiciones, truth, señales ni fixtures; no se ejecuta código, simulación, calibración ni validación. scientific_execution=false; execution_authorized=false.


## 16.195. Reloj normalizado, dominio de episodios y frontera de detectabilidad S3 (2026-11-12)

**Tipo:** derivación de escala y diseño de calibración; no introduce duraciones físicas, tolerancias funcionales ni parámetros numéricos aceptados. Reutiliza §§16.180–16.194, el catálogo finito de cinco familias, DEC-C10-068/099/100/101/102, S3/U_G, S4/S5 y los contratos P182/P183/MEAS/MISS.

### 16.195.1. Normalización sin fingir una unidad física

Se adopta como representación de trabajo un reloj adimensional de tiempo transcurrido. Sea W_c=t_c,max−t0, donde t_c,max es el límite superior común y preespecificado del soporte temporal de cualquier transición causal del DGP que pueda cambiar A_B1, considerando todos los brazos y escenarios. Se define x=(t−t0)/W_c, por lo que t0=0 y t_c,max=1 en coordenadas normalizadas.

Esta transformación fija únicamente una unidad de coordenada: **no afirma que W_c equivalga a segundos, horas, días ni a una duración operativa real**. Las distribuciones y decisiones temporales se expresarán mediante razones adimensionales; cualquier conversión a tiempo físico requeriría una fuente externa y una decisión separada. No se identifica W_c con t9, H, una fase de provisión ni un intervalo de rejilla.

La cola común se expresa ρ_follow=τ_follow/W_c, todavía OPEN. El horizonte común resulta T*=1+ρ_follow en coordenadas normalizadas. t_c,max es el último instante posible de transición causal dentro del soporte del DGP, no el último evento observado retrospectivamente en cada unidad. Esto permite mantener T* común y preespecificado. Un episodio que siga activo en T* queda terminal/censurado.

### 16.195.2. Dominio de episodios sin periodo de gracia

Cada episodio funcional tiene inicio, fin, familia causal, unidad/versión y estados efectivos antes/después. Su duración se expresa d_e=δ_event/W_c. Se conservan cinco familias (§16.194); provisión/instalación son antecedentes salvo que el estado B1 efectivo incumpla.

No existe mínimo funcional ni gracia: cualquier incumplimiento confirmado afecta a todos los intervalos que intersecte, conforme DEC-C10-102. El límite inferior que eventualmente se use para una matriz finita de escenarios será exclusivamente el **límite de soporte del benchmark sintético** (d_min,DGP), no una tolerancia del servicio ni una regla que convierta episodios menores en conformes. El informe deberá declarar explícitamente que no generaliza la detectabilidad fuera del soporte temporal ensayado. Los escenarios deben incluir episodios situados a ambos lados de la frontera de captura S3 y variación de fase respecto de la captura.

### 16.195.3. Canal S3 pasivo compatible con U_G

Se conserva un único canal lógico S3, vectorial y no-mutante, sin añadir fuente, actor, probe, endpoint o solicitud. Sus componentes conceptuales siguen siendo: proceso/módulo; listener/socket/superficie de ingreso; dependencias necesarias; capacidad/recursos cuando estén definidos; perfil runtime. S4 aporta identidad/versión/snapshot y S5 el contrato ENABLED/PROFILE, sin sustituir S3.

El modelo de observación debe poder representar, como mecanismos alternativos o combinados dentro de S3 ya existente:
- captura por snapshots/métricas en ventanas;
- registros pasivos de logs/trazas/eventos runtime;
- canal híbrido con ambos mecanismos.

No se declara que el sistema real disponga de captura event-driven, muestreo periódico, cobertura completa ni independencia. Cada componente conserva observación 1/0/?; ausencia, pérdida, lag, invalidez o falta de cobertura no equivalen a 0 funcional. La dependencia entre componentes y entre capturas puede ser arbitraria dentro de los escenarios declarados; no se impone independencia condicional.

Para una captura periódica ideal, instantánea y sin pérdida, con fase uniforme, P(detección|d_e,c)=min(1,d_e/c), donde c es el periodo de captura. Esta expresión es solo un límite de referencia geométrico para ese mecanismo ideal; no es tasa asumida ni se extrapola a logs/trazas, canales híbridos, capturas perdidas o señales dependientes. La calibración debe estimar/recuperar la curva conjunta P_det_joint(d_e|θ_S3,familia,versión,fase), incluyendo lag, pérdida, cobertura, falsos positivos/negativos y dependencia.

### 16.195.4. δ_det como curva, no como cifra arbitraria

Hasta que exista un umbral normativo de detección p*, no se fija un único δ_det. Se conserva primero la curva de detectabilidad. Condicionalmente a un umbral aprobado, podrá definirse:
δ_det(p*;θ_S3)=inf{d_e:P_det_joint(d_e|θ_S3)≥p*}.
p*, θ_S3, los dominios por familia/componente y los criterios de error permanecen OPEN. Si no existe un tramo de soporte en el que se alcance el criterio, el canal no identifica la truth puntual en ese dominio y el Analyzer debe emitir bounds/abstención. δ_det nunca altera A_B1 ni la regla estricta.

### 16.195.5. Derivación conjunta de Δ, K, τ_follow y T*

Se distinguen cuatro razones/objetos:
- d_e: duración de episodio funcional relativa a W_c;
- c_j/W_c: periodo/resolución de cada mecanismo de captura S3;
- Δ/W_c: anchura de los intervalos de adjudicación;
- ρ_follow: cola común posterior al último evento causal posible.

La rejilla se define sobre [0,1+ρ_follow], con K entero y Δ=(1+ρ_follow)/K. Δ no se iguala a la cadencia S3 ni a δ_det. La selección de K/Δ se obtiene mediante una frontera de recuperación y aliasing: variar K y las fases de evento/captura, comprobar la adjudicación estricta de todos los episodios del soporte y medir la recuperación de V_cont_truth. No se acepta un K que diluya episodios o cuya recuperación dependa de alineación favorable.

ρ_follow se somete a sensibilidad sobre la persistencia/recuperación posterior a la última transición posible. Se fija solo cuando el soporte de retrasos de recuperación de los escenarios queda declarado y el seguimiento permite distinguir recuperación, persistencia y censura. Entonces T*=1+ρ_follow; si no hay cota defendible de recuperación, se conserva el estado terminal/censurado y no se afirma recuperación completa.

### 16.195.6. Tabla única de parámetros y criterios de cierre

| Parámetro | Definición/escala | Regla de cierre | Estado |
|---|---|---|---|
| W_c | escala de coordenada hasta última transición causal posible | normalización W_c=1; sin unidad física | COORDINATE_ONLY |
| d_e / d_min,DGP | duración de episodio / límite inferior del soporte sintético | dominio de escenarios y sensibilidad, no tolerancia | OPEN |
| c_j/W_c | resolución/cadencia por componente S3 | mecanismo de captura especificado y curva de recuperación | OPEN |
| P_det_joint | detectabilidad conjunta por duración, fase, familia y versión | P182/P183/MEAS/MISS; dependencia y errores explícitos | OPEN |
| p*, δ_det | criterio de detección y duración que lo alcanza | requiere aprobación normativa de p*; primero curva | OPEN |
| Δ/W_c, K | anchura de intervalo y número entero de bloques | búsqueda de recuperación/aliasing con divisibilidad exacta | OPEN |
| ρ_follow, T* | cola común y horizonte final | soporte de recuperación/persistencia; T* común ex ante | OPEN |
| frontera temporal | pertenencia de evento exactamente en frontera | conservar regla recomendada [b_k,b_{k+1}); versionar antes de materializar | PENDING_PREMATERIALIZATION |
| criterio de error/coverage | falsos positivos/negativos, cobertura, bounds y abstención | criterios normativos y curvas por escenario/estimando | OPEN |

### 16.195.7. Secuencia mínima restante

No se abre otra ronda conceptual. La siguiente pasada integrada debe: (1) poblar el dominio/rangos adimensionales de episodios a partir de los escenarios adversariales ya inventariados en §16.188.4; (2) instanciar los tres mecanismos S3 (snapshot, log/trace, híbrido) con parámetros simbólicos y dependencia explícita; (3) definir la matriz de recuperación por duración/fase/componente; (4) obtener curvas condicionales de δ_det y la frontera K–Δ–ρ_follow; (5) identificar los umbrales normativos que requieren aprobación expresa; y (6) pasar a la parametrización estructural conjunta del DGP. No se repiten P178 ni los cierres semánticos previos.

**Dictamen:** NORMALIZED_CLOCK_COORDINATE_DEFINED / NO_PHYSICAL_TIME_INFERENCE / STRICT_TRUTH_PRESERVED / S3_CAPTURE_MODES_BOUNDED_TO_EXISTING_SOURCE / DETECTABILITY_CURVE_BEFORE_THRESHOLD / TEMPORAL_PARAMETERS_NOT_NUMERICALLY_CALIBRATED.

No se materializan escenarios, intervalos, truth, señales ni fixtures. No se ejecuta código, simulación, estimación, calibración ni validación. scientific_execution=false; execution_authorized=false.


## 16.195.8. Precedencia del último evento y horizonte común

Para reconciliar la notación anterior: t_last,i es la última transición efectiva de la unidad i; t_last^max=t_c,max es el límite superior común del soporte de transiciones posibles sobre todas las unidades, brazos y escenarios. El horizonte confirmatorio no se fija retrospectivamente como t_last,i+τ_follow para cada unidad, porque produciría ventanas distintas y potencialmente dependientes del resultado. Se fija ex ante como T*=t_last^max+τ_follow, equivalente a 1+ρ_follow en coordenadas normalizadas. Para cada unidad, el tramo desde su última transición efectiva hasta T* forma parte del seguimiento común; si el estado sigue incumpliendo al cierre, se conserva como terminal/censurado. Si el soporte de transiciones no puede acotarse ex ante, T* permanece OPEN y no se afirma cierre completo.


## 16.196. Crosswalk de escenarios temporales y contratos de medición existentes (2026-11-12)

**Objeto:** poblar la matriz temporal usando únicamente los perfiles DGP ya definidos en §16.188.4 y los contratos P182/P183, MEAS/MISS y PE. No se crean IDs de escenarios ni pruebas nuevas.

### 16.196.1. Mecanismos S3 a contrastar

| Variante dentro de S3 | Parámetros simbólicos | Riesgo que debe poder revelar |
|---|---|---|
| Snapshots/métricas | periodo c_j, fase φ_j, cobertura, lag, pérdida, validez | episodios entre capturas, aliasing, falsos negativos |
| Logs/trazas/eventos runtime | probabilidad de emisión/captura, retardo, duplicación, orden, pérdida | eventos no emitidos/perdidos, retraso, registros espurios |
| Híbrido | parámetros de ambos y distribución conjunta | dependencia entre fuentes, falsa sensación de cobertura por redundancia |

Las tres son configuraciones del canal S3 ya existente. No se convierten en tres fuentes independientes, no se asume independencia condicional y no se suman señales por una regla AND/OR no validada.

### 16.196.2. Reutilización de perfiles DGP ya aceptados

| Perfil existente §16.188.4 | Instanciación temporal/observacional reutilizada | Dictamen que debe recuperar Analyzer |
|---|---|---|
| Focal aislado | continuidad sin fallo y episodios funcionales bajo soporte declarado | recuperar V_cont cuando el canal identifica; separar ITT-paquete de atribución focal |
| Nulo/primera etapa nula | truth sin cambio funcional bajo Z | no fabricar cambio de V_cont |
| Fallo por etapas | retraso/fallo de provisión o instalación; solo cuenta si cambia A_B1 efectivo | no etiquetar antecedente técnico como fallo funcional |
| Focal adverso | interrupción B1 causada por cualquiera de las cinco familias | recuperar signo adverso o abstenerse si la medida no lo identifica |
| Vía directa/colateral | cambio de señal/captura por Z sin cambio de truth, y viceversa | no confundir cambio de observabilidad con cambio funcional |
| Interacción/heterogeneidad | fase, duración, cobertura o error distintos por estrato/versión | informar heterogeneidad; no promediar ocultando celdas fallidas |
| Medición adversarial | episodios breves/largos, fase de captura, pérdida, lag, errores correlacionados/diferenciales y cobertura incompleta | estimación, bounds o abstención según identificación |
| Soporte/interferencia/versionado | canal/host compartido, spillover, versión distinta, timestamps inconsistentes | no asumir independencia/unidad aislada; declarar soporte/versión inválidos |
| O/V no discriminables | misma conformidad terminal con secuencias V_cont distintas y secuencias compatibles con O-CONF distinto | no declarar validez discriminante sin recuperación de ambos sentidos |

Los perfiles temporales son subcasos de los escenarios existentes, no una batería factorial nueva. La matriz debe cubrir controles negativos de truth estable y de señal espuria, cambios de fase, episodios que cruzan fronteras, recurrencia, captura diferencial por brazo/versión y episodios activos al cierre.

### 16.196.3. Crosswalk con contratos existentes

| Riesgo/afirmación | Contrato reutilizado | Salida/criterio |
|---|---|---|
| error de medida temporal, falsos positivos/negativos | P182-07/08 | tasas y curvas por familia/duración/fase; no score agregado único |
| independencia del Analyzer respecto de truth | P182-11 + PROV-02/03/11 | firewall y sellado; cualquier fuga invalida la evaluación |
| versión y reconstrucción | P182-05/12 | trazabilidad por canal, señal, regla y resultado |
| taxonomía y mecanismo de ausencia | P183-01/02 + MEAS/MISS existentes | distinguir no emitido, no capturado, perdido, inválido, censurado y fuera de cobertura |
| no observado ≠ cero | P183-04 | desconocido observacional no se recodifica como fallo funcional ni continuidad |
| pérdida diferencial/selección | P183-07/10 + MEAS-13/MISS-10/13/15 | sensibilidad MAR/MNAR y dictamen por estimando |
| censura y seguimiento terminal | P183-09/11 | distinguir censura administrativa/informativa; bounds cuando proceda |
| discriminación Outcome/Value | P182-04/10 + contrato O-CONF/V_cont | mantener O-CONF terminal y V_cont temporal; no inferir uno del otro |

No se abren nuevos IDs. Si un contrato existente no cubre una aserción concreta, se registra el gap antes de proponer cualquier extensión. La cobertura de un contrato no equivale a implementación, ejecución o PASS.

### 16.196.4. Salidas mínimas del canal y regla de parada

El canal S3 debe conservar por componente y ventana: estado 1/0/?; mecanismo de captura; timestamp/intervalo de captura; cobertura; lag; pérdida; validez; versión; unidad/instancia; provenance y relación de dependencia declarada. Son requisitos semánticos, no nombres de columnas físicas.

El Analyzer recibe únicamente la proyección permitida y debe emitir, por intervalo y para V_cont: estimación puntual solo si la curva de observación identifica; bounds si el conjunto identificado es no trivial; abstención/NOT_IDENTIFIED cuando la pérdida, fase, dependencia o soporte impidan recuperar. La ausencia de evidencia nunca se interpreta como continuidad. El Evaluator compara con truth únicamente después del sellado.

**Dictamen:** EXISTING_DGP_PROFILES_REUSED / P182_P183_MEAS_MISS_CROSSWALKED / NO_NEW_TEST_IDS / TEMPORAL_OBSERVATION_MATRIX_SPECIFIED_NOT_INSTANTIATED / NO_EXECUTION.


## 16.197. Matriz adimensional de cobertura temporal y regla de selección de K (2026-11-12)

Esta sección convierte §§16.195–16.196 en una matriz finita de cobertura, sin fijar valores ni abrir escenarios/tests nuevos. Los cortes 1 son relaciones geométricas entre magnitudes ya definidas, no umbrales empíricos o normativos.

### 16.197.1. Ejes adimensionales

Para cada episodio funcional:
- r_c=d_e/c_j: duración del episodio frente al periodo/resolución del componente S3.
- r_Δ=d_e/Δ: duración frente a la anchura del intervalo V_cont.
- φ_j: fase del episodio respecto a la captura snapshot; para logs/trazas se sustituye por retardo/orden del evento.
- r_f=τ_follow/τ_recovery,max: seguimiento frente al máximo retraso de recuperación declarado en el soporte del DGP, cuando dicho máximo exista.

La matriz cubre r_c<1, r_c=1 y r_c>1; r_Δ<1, r_Δ=1 y r_Δ>1; y fases alineada, desfavorable (episodio entre capturas) y aleatoria para snapshots. Para logs/trazas se cubren evento capturado, evento no emitido/perdido y evento retrasado/desordenado. El canal híbrido conserva dependencia conjunta, no independencia supuesta. Estos son estratos de cobertura; no implican ejecutar el producto cartesiano completo.

### 16.197.2. Cobertura dirigida, no factorial completa

La matriz mínima debe incluir:
1. truth estable + señal estable (control negativo de error);
2. truth estable + señal espuria (falso positivo);
3. episodio truth breve con r_c<1 y fase desfavorable (riesgo de falso negativo/aliasing);
4. episodio con r_c=1 (frontera de captura);
5. episodio con r_c>1 (captura potencial repetida);
6. episodio breve con r_Δ<1 (un fallo puede poner a cero el bloque completo);
7. episodio que cruza una frontera de rejilla y afecta ambos intervalos;
8. pérdida/lag/captura diferencial por brazo, versión o componente;
9. canal híbrido con errores correlacionados y sin redundancia efectiva;
10. episodio recuperado antes de T* y episodio aún activo/censurado en T*;
11. mismo O-CONF terminal con secuencias V_cont distintas y contraste inverso para el gate discriminante.

Cada celda se vincula a los perfiles existentes §16.188.4 y a P182/P183/MEAS/MISS conforme §16.196. No se asignan nuevos IDs ni se cruzan indiscriminadamente todos los ejes. Se documenta qué combinaciones no se cubren y por qué.

### 16.197.3. Regla de horizonte y seguimiento

Sea τ_recovery,max el límite superior del soporte de retrasos de recuperación tras la última transición causal posible. Si existe y está justificado, se requiere τ_follow≥τ_recovery,max para observar el soporte completo; si se elige una cola menor, la fracción no cubierta queda explícitamente censurada. Si no existe un límite superior defendible, no se afirma recuperación completa y se mantienen bounds/censura. La cola es común a brazos y escenarios.

### 16.197.4. Regla de selección de Δ y K

K no se selecciona para minimizar el número de intervalos ni para maximizar artificialmente V_cont. Para cada candidato K entero, Δ=(1+ρ_follow)/K y se evalúa:
- recuperación de la secuencia A_B1 por intervalo y de V_cont_truth;
- sensibilidad a fase de eventos/capturas y a eventos que cruzan fronteras;
- falsos positivos/negativos, bounds, abstención y cobertura;
- estabilidad de la estimación al refinar K;
- error Monte Carlo y coste solo después de fijar criterios de aceptación.

Se conserva la regla de intervalo semiabierto [b_k,b_{k+1}) con evento en frontera asignado al intervalo que comienza allí; T* pertenece al extremo terminal del último bloque. La regla debe versionarse antes de materializar.

**Dictamen:** DIMENSIONLESS_COVERAGE_GRID_DEFINED / TARGETED_NOT_FULL_FACTORIAL / K_SELECTION_BY_RECOVERY_AND_ALIASING / FOLLOWUP_BY_RECOVERY_SUPPORT / NUMERIC_PARAMETERS_AND_ACCEPTANCE_THRESHOLDS_OPEN / NO_EXECUTION.


## 16.198. Registro paramétrico temporal integrado y dependencias (2026-11-12)

**Objeto:** convertir §§16.188.3 y 16.193–16.197 en un registro paramétrico único para la siguiente calibración. Es una especificación de familias, dominios y dependencias; no asigna valores, distribuciones numéricas, umbrales ni priors. Reutiliza el catálogo de cinco familias y los perfiles de §16.188.4; no crea escenarios, variables científicas, fuentes ni IDs de prueba.

### 16.198.1. Corrección semántica obligatoria de V_cont

La combinación DEC-C10-100 + DEC-C10-102 define V_cont_truth como la **proporción de intervalos completamente conformes**, no como la fracción exacta de tiempo en servicio ni como uptime integral. Un incumplimiento funcional confirmado en cualquier instante hace A_B1(i,k)=0 para cada intervalo que intersecte; no hay gracia ni duración mínima funcional. Por tanto, el valor depende de Δ y de la alineación de la rejilla. Las curvas y resultados deben denominarlo proporción de intervalos completamente conformes; queda prohibido describirlo como porcentaje exacto de tiempo disponible. Esta corrección no altera las decisiones aceptadas ni su fórmula.

### 16.198.2. Registro de parámetros de tiempo y episodios

| Familia | Parámetros simbólicos y dominio | Restricciones/dependencias obligatorias | Estado |
|---|---|---|---|
| Reloj | W_c; x=(t−t0)/W_c; t0=0; t_c,max=1 | W_c es escala de coordenada, no unidad física; soporte común a brazos/escenarios | Coordinate-only |
| Inicio/causa | x_on,e∈[0,1]; family_e∈{configuración, proceso, ingreso, dependencia, capacidad}; unit/version | El cambio de A_B1 depende del estado funcional resultante, no de la etiqueta técnica | Estructura definida; leyes OPEN |
| Duración | d_e=δ_event/W_c; soporte sintético [d_min,DGP,d_max,DGP]⊂(0,∞) | d_min,DGP es límite del benchmark, nunca tolerancia funcional; episodios pueden cruzar rejilla y capturas | Soporte OPEN |
| Recurrencia | número/orden de episodios, separación entre episodios y solapamiento por unidad | No independencia por defecto; solapamiento resuelto por estado funcional efectivo | OPEN |
| Recuperación | τ_recovery/W_c y estado funcional tras cada transición | Distribución condicional a familia, estado, versión y escenario; límite superior solo si defendible | OPEN |
| Horizonte | ρ_follow=τ_follow/W_c; T*=1+ρ_follow | Cola común tras t_c,max; si soporte de recuperación no acotado, conservar censura | Regla definida; valor OPEN |
| Rejilla | K∈ℕ+, Δ=(1+ρ_follow)/K | K y Δ comunes; divisibilidad exacta; intervalos iguales; no derivar de t0…t9 ni H | OPEN |
| Fronteras | convención semiabierta [b_k,b_{k+1}) | Evento en frontera se asigna al intervalo que comienza allí; regla versionada antes de materializar | Pendiente de versionado |
| Detección | δ_det(p*;θ_S3), P_det_joint(d_e|θ_S3,familia,versión,fase) | Primero curva; p* requiere aprobación normativa; δ_det no modifica truth | OPEN |

### 16.198.3. Registro del canal S3 y modelo conjunto

**Snapshots/métricas:** para cada componente j, c_j/W_c, fase φ_j, cobertura temporal/espacial, probabilidad o regla de captura, lag, pérdida, invalidez y errores de clasificación. La fase se trata como parámetro o estrato explícito; no se asume uniforme salvo que un escenario lo estipule.

**Logs/trazas/eventos pasivos:** probabilidad/regla de emisión, captura condicionada a emisión, retardo/lag, pérdida, duplicación, desorden, validez y errores semánticos. Emisión y captura son procesos distintos; ausencia de registro no se convierte en evento negativo.

**Híbrido:** distribución conjunta de todos los componentes y sus dependencias condicionales a familia, unidad, versión, brazo, tiempo y estado. No se multiplican sensibilidades/especificidades de fuentes como si fueran independientes ni se aplica una regla AND/OR no validada.

En las tres configuraciones se conservan por componente y ventana: cobertura, estado observado 1/0/?, timestamp, lag, validez, pérdida, versión, unidad, provenance y dependencia. El vector S3 no se reduce a una señal promedio.

### 16.198.4. Modelo generativo de eventos y dependencias

El Generator produce primero, en truth reservada, una historia de estados funcionales efectivos y transiciones. La secuencia mínima por episodio es (estado previo, evento/causa, event_time, estado posterior, versión, provenance); A_B1 se deriva después sobre cada intervalo mediante DEC-C10-102. La provisión/instalación puede anteceder a una transición, pero no determina A_B1 por sí misma.

La familia causal, el estado basal, la política Z, la etapa de provisión/instalación, versión, disponibilidad de dependencias/recursos y episodios previos pueden condicionar inicio, duración y recuperación. Se deben especificar las dependencias y potenciales afectados por escenario; no se factoriza la distribución conjunta ni se presume independencia temporal, entre componentes S3, entre unidades o entre brazos. Si hay recursos/canales compartidos, se usa unidad de asignación por clúster o mapa de exposición; de otro modo, aislamiento explícito por construcción.

S3 se genera después como mecanismo de observación de esa historia, pudiendo depender de Z, versión, estado, familia y tiempo. Este orden permite escenarios con cambio de truth sin cambio de señal y cambio de señal sin cambio de truth. Analyzer recibe solo evidencia observada sellada; Evaluator abre truth después.

### 16.198.5. Matriz de recuperación derivable, sin números ni factorial completo

La matriz dirigida combina los perfiles ya aceptados con los estratos temporales de §16.197:
- control estable sin episodio y control estable con señal espuria;
- episodios de cada familia causal, con duración por debajo, en y por encima de las fronteras d_e/c_j y d_e/Δ;
- fases favorables/desfavorables y variación de fase;
- episodio aislado, recurrente y solapado;
- captura correcta, no emisión, pérdida, lag, duplicación y desorden;
- S3 diferencial por Z/versión y errores correlacionados en híbrido;
- recuperación antes de T* y persistencia/censura en T*;
- truth cambiante con señal estable y truth estable con señal cambiante;
- O-CONF terminal equivalente con secuencias V_cont distintas y contraste inverso.

No es un producto cartesiano. Cada escenario debe declarar qué dimensiones activa, qué contraste falsifica, qué control negativo lo acompaña y qué soporte deja fuera. Las curvas P_det_joint se informan por familia/duración/fase/versión/configuración S3; falsos positivos, falsos negativos, cobertura, bounds y abstención no se agregan en un score global.

### 16.198.6. Qué se puede derivar y qué requiere decisión/soporte

**Derivable por construcción:** identidades de normalización; relación T*=1+ρ_follow; K=(1+ρ_follow)/Δ cuando la divisibilidad es exacta; asignación de eventos a intervalos; generación de truth por estado funcional; fórmulas de detección condicionadas al mecanismo; métricas de recuperación, error, cobertura, bounds y abstención; error Monte Carlo tras fijar estimando y tolerancia.

**No deducible sin soporte/decisión:** d_min,DGP/d_max,DGP; leyes de inicio/duración/recurrencia/recuperación; dependencia entre familias, unidades y brazos; configuración material pasiva S3; fase y cadencia reales; distribución conjunta de pérdida/lag/error; p*; δ_det; K/Δ/ρ_follow numéricos; relevancia científica, α, potencia mínima, precisión, equivalencia, MDE y tolerancias; N, π_h, clústeres y R.

Los candidatos numéricos históricos (.25/.80, N=2.000, 1:1, R=1.000, y parámetros de P178) no se importan como confirmatorios. Un valor solo entra al ledger con procedencia, justificación, dominio, estado de aprobación y análisis de sensibilidad. Ningún default silencioso.

### 16.198.7. Gate de parada y siguiente integración

La calibración temporal numérica sigue BLOCKED hasta disponer de (i) soporte de episodios/recuperación y distribuciones justificadas; (ii) especificación factible del mecanismo S3 pasivo; (iii) criterio normativo p* y criterios de error/coverage; y (iv) mantener la escala ya aceptada por DEC-C10-100/102 como proporción de intervalos completos, reconociendo su dependencia de Δ. Solo si se pretende recuperar la fracción exacta de tiempo disponible —constructo distinto— deberá abrirse una decisión explícita; no se presume ni se sustituye la escala vigente. No se selecciona K por conveniencia ni se simulan cifras ilustrativas como si fueran evidencia.

La siguiente integración no es otra ronda de decisiones aisladas: reconciliar este registro con el ledger global §16.188.3, los potenciales de D2, soporte/interferencia y los estimandos P177–P183; después identificar qué parámetros quedan estructuralmente identificados por diseño, cuáles son escenarios de sensibilidad y cuáles exigen aprobación. Solo entonces podrá prepararse una calibración autorizable.

**Dictamen:** TEMPORAL_PARAMETER_FAMILIES_AND_DEPENDENCIES_SPECIFIED / V_CONT_SEMANTIC_INTERPRETATION_CORRECTED / NO_NUMERIC_VALUES_INVENTED / NO_NEW_TEST_IDS / CALIBRATION_BLOCKED_BY_SUPPORT_AND_NORMATIVE_CRITERIA / NO_EXECUTION.


## 16.199. Crosswalk estructural único: D2, accesibilidad g_A, vías no focales y soporte (2026-11-12)

**Tipo:** integración de contratos y ledger estructural; no nueva decisión científica, no parametrización numérica, no Design Freeze.  
**Precedencia:** §§16.175–16.185, 16.188.3–16.188.6, 16.198; contrato DGP temporal/roles §§3, 30–31; PD y contratos D2/PC/C1; DEC-C10-066/067 y DEC-C10S-D2-ESTIMAND-SEPARATION-001.  
**Objeto:** una sola representación estructural que conecte la política D2, sus etapas de provisión, el cambio completo ΔT_acc*, las intervenciones g_A, los caminos directos/colaterales y los resultados O-CONF/V_cont, sin equiparar etapas ni estimandos.

### 16.199.1. Orden estructural y potenciales bajo D2

Para cada unidad experimental i y asignación z∈{0,1}, el Generator conserva la historia potencial versionada:

`S_i(z)=[W_programmed_i(z),W_attempt_i(z),receipt_i(z),S_install_i(z),C_dep_i(z),A_f_i(z),D_f_i(z),T_acc_i(z),ΔT_acc_i(z),Reach_i(z),Π_i(z),K_i(z),Request_i(z),Selection_i(z),Start_i(z),Exec_i(z),O-CONF_i(z),V_cont_i(z)]`.

La secuencia causal de referencia es:

`Z → W_programmed → W_attempt → receipt → S_install → C_dep* → A_f* → D_f*/T_acc* → ΔT_acc* → Reach/Π → consideración/selección/inicio/ejecución → O-CONF/V_cont`.

Es un orden de dependencias posibles, no una cadena determinista ni una mediación serial obligatoria. Se permiten antecedentes basales, causas comunes, rutas paralelas, retroalimentación temporal legítima y fallos en cada etapa, siempre que se fechen y se declaren por escenario. No se infiere que una etapa posterior ocurra por el mero éxito de la anterior.

- **W_programmed:** estado prescrito por la política; para D2, 0 bajo Z=0 y 1 bajo Z=1, conforme a la regla de política ya aceptada. No es π_h ni cumplimiento.
- **W_attempt:** intento efectivo, condicionado por programación, historia y mecanismo de cumplimiento; se registra por separado cualquier intento de fondo bajo W_programmed=0. No equivale a recepción.
- **receipt:** recepción/disponibilidad efectiva del paquete o componentes previstos. No equivale a instalación.
- **S_install:** aplicación/instalación y sus estados separados de integridad, compatibilidad, operabilidad y verificación. No equivale a C_dep* ni a accesibilidad.
- **C_dep*:** estado derivado del intento/recepción/instalación y del éxito técnico conjunto de las dependencias constitutivas vigentes. No se asigna como marginal independiente ni se fuerza a 1 cuando W_programmed=1.
- **A_f*:** predicado focal de accesibilidad estructural, con la conjunción y lógica trivalente de su contrato vigente. Se conserva como candidato la dependencia de C_dep* y de las condiciones constitutivas AUTH/RES/CAP/INFO/DOMAIN/OTHER; la atomización y el estatus basal independiente de C_auth,base siguen sujetos a sus invariantes abiertos. No se colapsan C_auth,base y C_dep* ni se los trata como equivalentes.
- **D_f*:** apertura basal→post, derivada solo cuando snapshots/predicados comparables permiten establecer A_f,0*=0 y A_f,1*=1. No sustituye A_f,1* ni representa asignación.
- **T_acc* y ΔT_acc*:** snapshots estructurales verdaderos y su diferencia comparable; no se sustituyen por A_f* ni por C_dep*.

Cada etapa mantiene su propio potencial bajo z. Las funciones estructurales pueden depender de historia basal, versión, estado previo, política, etapa precedente, recursos y causas compartidas justificadas. No se fijan probabilidades, independencia, monotonicidad ni éxito técnico por defecto. Los valores históricos .25/.80, s=.80 y cualquier idealización de cumplimiento perfecto no se elevan a parámetros confirmatorios.

### 16.199.2. Crosswalk del cambio estructural completo

Los snapshots verdaderos son S_T*(t)=(U_t*,R_t*,C_t*,X_t*) y:

`ΔT_acc*=Diff_{G,M}(S_T*(t_pre),S_T*(t_post))=(ΔU*,ΔR*,ΔC*,ΔX*)`.

| Componente | Significado vigente | Papel causal y regla de modelado |
|---|---|---|
| ΔU* | Cambios en identidades/estados de transformaciones accesibles | Altas, bajas, reconfiguraciones y cambios de estado, con identidad/versionado comparable |
| ΔR* | Cambios en relaciones tipadas, dependencias y composición | Aristas añadidas, eliminadas o modificadas; preservar dirección, tipo y dependencia transitiva |
| ΔC* | Cambios en condiciones, predicados, restricciones y configuraciones de realizabilidad | Cambios constitutivos que habilitan/restringen transformaciones o relaciones; no mezclar evidencia epistémica |
| ΔX* | Cambios del contexto/estado efectivo constitutivo que condiciona accesibilidad | Clasificar campo a campo; no convertirlo automáticamente en C*, U*, covariable basal q_X ni sexta coordenada |

ΔValidity_e, cobertura, procedencia, timestamp y calidad de observación pertenecen a ΔE_T, no a ΔT_acc*. Un cambio de evidencia sin cambio estructural no produce ΔT_acc*. Un diff no comparable por identidad, frontera, granularidad o mapping de versiones se conserva como ?; no se fuerza a cero.

ΔX* requiere mapping semántico por campo. Si el campo es realmente un predicado/regla se clasifica en C*; si es contexto basal no intervenido y no constitutivo del cambio, puede pertenecer a q_X*; si es contexto post-Z constitutivo, permanece en ΔX*; si no afecta accesibilidad queda fuera del mediador; si no se resuelve, UNKNOWN/?. No hay equivalencia automática ΔX*↔q_X*.

### 16.199.3. q_X*, q_L* y soporte

q_X* es la distribución conjunta basal objetivo, definida antes de Z sobre la historia pertinente (incluidos X, H0, Cc y demás campos basales que el crosswalk acepte). No es la propensión de asignación π_h, no es una distribución post-Z y no se estima a partir de resultados. El roster se fija sin usar Need_preZ, S7, Z ni outcomes como filtro; Need_preZ no es elegibilidad.

La misma q_X* debe estandarizar las dos políticas g_A y los contrastes que pretendan compararse. Deben declararse dominio, soporte, masas, restricciones de factibilidad, versiones y reglas de truncamiento. Si una política no es factible para una historia con masa en q_X*, se restringe la población/estimando ex ante con justificación o se declara falta de identificación; no se extrapola silenciosamente.

q_L* no se añade como ajuste basal ni como covariable automática. Solo procede si la identificación de C4 requiere una intervención longitudinal sobre historia/confusores mediador–resultado post-Z inducidos por Z. En tal caso debe especificarse como distribución/regla secuencial, con orden temporal, soporte y régimen común. Si no se puede definir/identificar, C4 permanece BOUNDS_ONLY o NOT_IDENTIFIED.

La unidad UE, UA y UO permanece diferenciada. UE=UA requiere aislamiento completo por construcción. Si hay recursos, dependencias, pools, agentes o canales compartidos, se asigna por clúster o se declara un mapa de exposición G_i(Z_-i); sin mapa/soporte no se declara SUTVA ni ITT individual identificados.

### 16.199.4. Intervenciones g_A y régimen no focal

g_A1 y g_A0 son políticas estocásticas factibles sobre la distribución conjunta del vector completo ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), condicionadas por la misma q_X*. No asignan Z a accesibilidad, no fijan A_f* a 1/0 y no intervienen en una sola coordenada aislada salvo que el estimando se redefina expresamente.

Para cada régimen deben declararse: mecanismo generador de la distribución de ΔT_acc*, versiones/estados admisibles, probabilidades o reglas de asignación, restricciones de factibilidad, soporte común, consistencia y tratamiento de desconocidos. El contraste conserva la forma ya aceptada:

`θ_A(q_X*;Y)=E_{X~q_X*,ΔT~g_A1,R~r_common}[Y(ΔT,R)]−E_{X~q_X*,ΔT~g_A0,R~r_common}[Y(ΔT,R)]`.

r_common fija explícitamente las vías no focales que se mantienen comunes; no es una etiqueta residual ni una suposición tácita de ausencia de efectos. El resultado Y se declara por separado; V_cont es el candidato vigente, pero su uso confirmatorio depende de la medición S3, soporte y discriminación frente a O-CONF.

El mapping D2→g_A no está demostrado. El ITT_Z^D2 identifica, bajo sus condiciones, el efecto total de asignar el paquete D2; no identifica θ_A ni permite atribuir el ITT a ΔT_acc*. La recuperación de θ_A debe probarse directamente bajo g_A en el DGP sintético. C4 es mediación interventional distinta y no se calcula como ITT−θ_A.

### 16.199.5. Vías directas, colaterales e interacciones

Se conserva un bloque explícito D_i(z) para las vías que pueden afectar Y sin pasar por ΔT_acc*, y un bloque C_i(z) para cambios colaterales que pueden alterar otras rutas, recursos o condiciones. No son residuos calculados por resta: son mecanismos generativos declarados.

| Vía | Ejemplos ya presentes en contratos | Regla |
|---|---|---|
| Directa a O/V | efecto de política sobre outcome/value sin mediación por ΔT_acc* | Debe activarse en perfiles adversariales; ITT sigue siendo efecto de paquete |
| Colateral de recursos/dependencias | RES_f*, capacidad no focal, dependencias críticas compartidas, consumo/desplazamiento | Preservar PROV-05/09 y contratos D2-RES/CAP; no asumir ausencia ni doble contabilizar C_dep* |
| Alternativas/otras rutas | A1/A2/F2, Reach/Π, seguridad, latencia, coste, información y calidad | Mantener resultados y rutas propios; no absorber automáticamente en ΔT_acc* |
| Medición/observación | S3 diferencial por Z, versión, familia, estado o tiempo | No tratarlo como vía funcional ni ajustar mecánicamente por observación post-Z |
| Interacción/heterogeneidad | política×ΔT_acc*, estado basal×política, recursos×versión, unidad×exposición | Declarar potenciales y escenarios; no imponer aditividad ni monotonicidad |
| Interferencia | recursos/pools/canales compartidos entre UE | Clúster/mapa de exposición; si no se conoce, límites de identificación |

La distribución conjunta puede factorizarse solo cuando el diseño o el escenario lo justifique. La ausencia de una arista en el diagrama no prueba independencia ni exclusión. Los efectos directos, colaterales, redundantes, antagonistas y compensatorios pueden coexistir. Si no se separan con soporte/identificación, el dictamen es efecto de paquete o BOUNDS_ONLY/NOT_IDENTIFIED, no atribución focal.

### 16.199.6. Ledger global de parámetros: familias, dependencias y estado

| Bloque | Parámetros/reglas a registrar | Dependencias/potenciales afectados | Estado de cierre |
|---|---|---|---|
| Baseline/población | q_X*, roster, estratos, E/App, versiones y soporte | Historia basal conjunta; todos los potenciales posteriores | Estructura conocida; distribución/soporte OPEN |
| Asignación D2 | π_h, UA/clúster, ratio, algoritmo, semilla, exposición | Z y todos los potenciales bajo z | Política D2 definida; diseño de asignación OPEN |
| Programación/intento | W_programmed, regla de intento, cumplimiento, intentos de fondo | Z, historia, versión → W_attempt | Regla de programación D2 definida; mecanismo de cumplimiento OPEN |
| Recepción | receipt, disponibilidad, integridad de recepción | W_attempt, logística/versión → receipt | Función OPEN |
| Instalación | S_install, aplicación, integridad, compatibilidad, operabilidad, verificación, rollback | receipt, estado previo, versión, entorno → S_install | Estados definidos; leyes/soporte OPEN |
| Dependencias | componentes de C_dep*, éxito técnico conjunto, fallback/alternativas admisibles | intento/recepción/instalación, dependencias transitivas → C_dep* | Derivación estructural; parámetros OPEN |
| Accesibilidad focal | C_auth,base, RES_f*, C_capacity, C_info, C_domain, C_other, predicados ID/REL/COND/AUTH/RES/DEP/¬BLOCK | C_dep*, historia, snapshots → A_f* | Crosswalk parcial; atomización/invariantes abiertos |
| Cambio estructural | ΔU*, ΔR*, ΔC*, ΔX*, matching y Diff_{G,M} | T_acc basal/post, identidad/versionado → ΔT_acc* | Tipado definido; mapping/catálogos/soporte OPEN |
| Reach/Trayectoria | grafo G, horizonte H, ventanas, recursos, bloqueos, rutas alternativas | T_acc*, reglas de composición → Reach/Π y etapas posteriores | Estructura parcial; dominio/exhaustividad OPEN |
| Outcome/Value | F*/O-CONF por ruta; A_B1/V_cont por intervalos | estados post-aplicación y trayectoria temporal; observación separada | reglas semánticas definidas; oráculos/canal y validez OPEN |
| Observación | S3, E_T, errores, pérdida, lag, cobertura, dependencia, missingness/censura | truth → observed_evidence; potencialmente diferencial por Z/estado/versión | mecanismo estructural; distribución conjunta OPEN |
| Vías no focales | D_i(z), C_i(z), r_common, interacciones y heterogeneidad | Z, ΔT_acc*, recursos/alternativas → Y | Deben declararse por escenario; magnitudes OPEN |
| Interferencia | UA/cluster, pools, G_i(Z_-i), exposición | potenciales de otras unidades → resultados propios | Aislamiento o mapa OPEN |
| g_A | g_A1/g_A0, soporte, consistencia, versiones y régimen común | q_X*, ΔT_acc*, r_common → Y | Estimando definido; políticas/soporte OPEN |
| C4/q_L | historia longitudinal, confusores inducidos, intervención mediadora | Z → L → ΔT_acc*/Y | Necesidad y estrategia OPEN; no ajustar automáticamente |
| Calibración | distribuciones, parámetros, α, potencia, precisión, relevancia, equivalencia, N, π_h, R, error MC | recuperación por estimando/escenario | Bloqueada hasta soporte y criterios |

Cada entrada numérica futura debe incluir definición, unidad/escala, dominio, nivel (UE/UA/clúster/etapa/intervalo), tiempo, potenciales afectados, función/distribución, dependencias, procedencia, estado de aprobación, rango de sensibilidad, versión y restricción de soporte. Sin ello, no se materializa.

### 16.199.7. Clasificación de parámetros y decisiones pendientes

**Derivable sin aprobación adicional:** orden de estados/potenciales ya aceptado; identidades de programación D2; fórmulas de primeras etapas una vez definidos sus eventos; composición de A_f*/D_f* conforme a contratos vigentes; Diff estructural de cuatro componentes; estandarización formal a q_X* común; separación ITT/g_A/C4; métricas de recuperación y reglas de abstención.

**Requiere soporte empírico/sintético justificado:** distribuciones de cumplimiento, recepción, instalación y éxito técnico; dependencias transitivas; q_X* y soporte; leyes de cambio de U/R/C/X; distribución de g_A; vías directas/colaterales e interacciones; distribución de S3; interferencia/exposición; horizonte, rejilla y error de medición.

**Requiere decisión normativa explícita:** población/soporte confirmatorios; criterio de factibilidad de g_A; régimen r_common; relevancia científica/MDE; α, potencia, precisión y equivalencia; tolerancias de medición; reglas de exclusión/restricción de soporte; unidad/clúster cuando el aislamiento no sea demostrable.

No se importan N=700, R=10.000, asignación 1:1 ni parámetros del replay P178 como confirmatorios. Tampoco se elevan .25/.80 o s=.80 históricos a tasas aprobadas.

### 16.199.8. Gate y siguiente paso

La matriz estructural integrada queda especificada, pero no poblada numéricamente. Antes de calibrar se debe producir una tabla finita de funciones estructurales por etapa y potencial afectado, junto con un inventario de campos basales para q_X* y un mapping adjudicable de ΔX*. Después se puede declarar, parámetro por parámetro, si se fija por construcción, se varía como sensibilidad o exige decisión normativa. Los escenarios existentes §16.188.4 son el marco de cobertura; no se crea factorial completo ni nuevos IDs.

**Dictamen:** D2_STAGE_CROSSWALK_SPECIFIED / FULL_ΔT_ACC_COORDINATES_PRESERVED / q_X_AND_SUPPORT_OPEN / g_A_SEPARATE_FROM_D2_ITT / DIRECT_COLLATERAL_PATHS_EXPLICIT / NO_NEW_TEST_IDS / NO_NUMERIC_PARAMETERS_INVENTED / CALIBRATION_BLOCKED / NO_EXECUTION.


## 16.200. Tabla de funciones estructurales, inventario basal q_X* y mapping de ΔX* (2026-11-12)

**Tipo:** especificación de funciones y clasificación de campos derivada de contratos existentes; no asigna parámetros numéricos ni acepta variables basales aún discutidas.  
**Precedencia:** §§16.175.2/4, 16.185, 16.188.3–.6, 16.199; DGP §§3.1–3.4, 30–31; contratos de snapshots, C_dep*, A_f* y población.  
**Propósito:** convertir el crosswalk en una tabla adjudicable de funciones/potenciales, separando lo fijado por definición, lo que requiere función estructural y lo que permanece sin mapping.

### 16.200.1. Tabla mínima de funciones estructurales por etapa

La notación (f_j) representa una función estructural versionada; no presupone linealidad, independencia, distribución paramétrica ni ruido aditivo. Los argumentos listados son dependencias permitidas por los contratos, no una afirmación de que todas deban estar activas en el escenario base.

| Etapa/objeto | Función estructural mínima | Potenciales/objetos afectados | Qué queda abierto |
|---|---|---|---|
| Asignación | (Z_isim Assign(UA_i,strata_i,pi_h,seed)) | Z y toda la historia potencial posterior | UA/cluster, estratos, π_h, algoritmo, semilla, N |
| Programación D2 | (W_{prog,i}(z)=z) | W_programmed_i(z) | Versión/payload del paquete y elegibilidad material |
| Intento efectivo | (W_{att,i}(z)=f_{att}(W_{prog},z,X_i,H0_i,version,epsilon_{att})) | W_attempt_i(z) | Cumplimiento (c_{z,D}(X,H)), intento de fondo (b_{z,D}(X,H)), oportunidad y dependencias |
| Recepción | (Rec_i(z)=f_{rec}(W_{att},policy,version,logistics,environment,epsilon_{rec})) | receipt_i(z) | Disponibilidad, pérdida, compatibilidad y tiempos de recepción |
| Instalación/verificación | (S_{inst,i}(z)=f_{inst}(Rec,version,environment,integrity,compatibility,operability,epsilon_{inst})) | aplicación, integridad, compatibilidad, operabilidad, verificación y rollback | Funciones conjuntas, orden, fallos parciales y recuperación |
| Dependencias técnicas | (C_{dep,i1}^*=f_{dep}(W_{att},Rec,S_{inst},C_{install},C_{integrity},C_{compat},C_{oper},dependency_graph)) | C_dep* y potenciales de dependencias | Catálogo transitivo, condiciones constitutivas y soporte; no marginal independiente |
| Accesibilidad focal | (A_{f,i1}^*=h_f(C_{dep},C_{auth,base},C_{resource},C_{capacity},C_{info},C_{domain},C_{other})) | A_f,post* | Atomización/mappings y estatus separado de C_auth,base; lógica 1/0/? |
| Apertura focal | (D_{f,i}=I(A_{f,i0}^*=0land A_{f,i1}^*=1)) | D_f* | Matching basal/post, predicados comparables; no se calcula si hay ? o identidad no comparable |
| Snapshot estructural | (S_{T,i}^*(t)=f_T(history_i(t),identity,version,boundary)) | U*, R*, C*, X* por tiempo | Catálogo, identidad, granularidad, frontera y mapping |
| Cambio completo | (Delta T_{acc,i}^*=Diff_{G,M}(S_T^*(t_{pre}),S_T^*(t_{post}))) | ΔU*, ΔR*, ΔC*, ΔX* | Matching y mapping; UNKNOWN si diff no comparable |
| Reach/posibilidades | (Reach_i,Pi_i=f_{reach}(T_{acc}^*,G,H,preconditions,resources,windows,blocks)) | Reach*, Π_H* | G, H, exhaustividad, ventanas, reglas y recursos |
| Trayectoria downstream | (K,Consider,Selection,Start,Exec=f_{path}(Reach,Pi,knowledge,actors,history)) | Potenciales por etapa de trayectoria | Funciones por etapa; no se reconstruye acceso desde ejecución |
| Continuidad B1 | (A_{B1,i}(t)=f_{B1}(ENABLED_{eff},PROFILE_{eff},admission_capacity)); (V_{cont,i}^{truth}=K^{-1}sum_k A_{B1}(i,k)) | Serie funcional y V_cont_truth | Parámetros temporales y S3; truth estricta por intervalo conforme DEC-C10-102 |
| Conformidad terminal | (O_{CONF,i,r}^{truth}=F^*(state_{postapply,postcheck,r})) | O-CONF por ruta | IAM, predicados, oráculo y validación de §224 |

Para D2, (W_{prog}(z)=z) expresa únicamente la regla de programación ya definida. No autoriza sustituir (W_{att}), receipt, (S_{inst}), (C_{dep}^*) o (A_f^*) por Z. La conjunción técnica de (C_{dep}^*) conserva la fórmula vigente del DGP; no se presume independencia entre sus componentes. La función (h_f) conserva el contrato focal vigente, sin resolver por esta tabla la disputa/invariante abierta sobre C_auth,base.

### 16.200.2. Inventario basal para q_X*: admisión, exclusión y estado

q_X* debe contener solo historia/condiciones medidas o estipuladas antes de Z que sean necesarias para definir la población objetivo, factibilidad y heterogeneidad de las intervenciones. La tabla no convierte todos los campos candidatos en covariables ni los declara independientes.

| Campo basal candidato | Papel documentado | Tratamiento para q_X* |
|---|---|---|
| X, H0 | Historia/contexto basal conjunto de la UE | Núcleo de q_X*, pendiente de schema, dominio y distribución conjunta |
| C_c | Condiciones constitutivas para factibilidad de τ2 | Incluir solo componentes con mapping semántico y soporte; no confundir con outcomes |
| F_alt,0 | Alternativa funcional basal | Modificador basal; define P*_F para análisis secundario, no excluye automáticamente de P*_τ2 |
| E_i / App_i | Alcance y aplicabilidad de la unidad a τ2 | Condiciones de marco/selección; regla externa E_i pendiente. En núcleo sintético τ2 aplicable por construcción |
| C_dep,i0* / A_f,i0* | Estado estructural basal | En núcleo limpio, C_dep,0=0 y A_f,0*=0 por construcción; en estrés, estados/UNKNOWN se declaran explícitamente. No convertirlos en filtros post-Z |
| L_m,0 | Condiciones temporales basales | Solo si se demuestra papel basal y mapping; no confundir con q_L* post-Z ni ajustar mecánicamente por mediadores |
| T_acc,i0* | Snapshot basal de accesibilidad | Puede ser parte de historia basal solo con identidad, frontera y catálogo; no duplicar sus campos en X/H0/C_c |
| C_auth,base | Autorización funcional basal | Mapping y condición de independencia respecto de C_dep* siguen abiertos; no fijar inclusión en q_X* ni colapsarlo |
| Need_preZ / S7 / truth B1 | Constructo objetivo y canal declarativo pre-Z | No usar como covariable predictora, filtro de elegibilidad ni variable para generar q_X*; mantener reserva y reglas DEC-C10-095/097/098 |
| Z, W_attempt, receipt, S_install, C_dep,post, A_f,post, ΔT_acc, Reach, trayectoria, O, V | Variables post-Z | Excluidas de q_X*; no usar para construir baseline ni selección basal |

**Regla de construcción:** primero fijar el marco sintético P*τ2 y el roster por condiciones de diseño; después generar conjuntamente los campos basales admisibles desde q_X*. El núcleo limpio estipula aplicabilidad τ2 y los estados basales C_dep,0=0/A_f,0*=0 por construcción, sin afirmar que esta sea una distribución externa representativa. F_alt,0 modifica el análisis secundario P*_F, no la cohorte primaria. Need_preZ nunca determina la composición de la cohorte.

### 16.200.3. Mapping adjudicable de X* y ΔX*

El mapping se hace por campo y por función semántica, no por nombre de columna:

| Clase | Regla de clasificación | Ejemplos de función (no mapping aprobado de campos concretos) |
|---|---|---|
| U* | Identidad/estado de una transformación | Transformación añadida, retirada, reconfigurada o con estado efectivo distinto |
| R* | Relación tipada/dirigida entre objetos/transformaciones | Dependencia, interfaz, composición, conexión o arista modificada |
| C* | Regla, predicado, restricción o configuración de realizabilidad | Autorización, precondición, cuota/recurso como restricción, bloqueo, condición de invocación |
| X* | Estado/contexto efectivo constitutivo que condiciona accesibilidad y no es U/R/C | Contexto material de ejecución/entorno que cambia y altera factibilidad, una vez excluidas reglas y relaciones |
| E_T / ΔE_T | Evidencia y conocimiento sobre la estructura | Fuentes, cobertura, validez epistémica, provenance, hashes, logs, timestamps y adjudicación |

**Procedimiento de adjudicación por campo:** (1) identificar referente y unidad; (2) fijar momento basal/post y versión; (3) preguntar si el campo es una transformación, relación o regla/condición; si sí, clasificar U/R/C; (4) si no, determinar si es estado/contexto efectivo constitutivo de accesibilidad; solo entonces X; (5) si solo describe qué se conoce, clasificar E_T; (6) si mezcla funciones, descomponer; (7) si no se puede decidir sin inferencia, UNKNOWN/? y no entra al diff puntuable.

No se aprueba todavía un listado físico de campos ΔX*. El contrato de snapshots exige clasificación campo a campo; el mapping con C10-D1 §27.1 tampoco permite asignar ΔX* automáticamente a A⁺/A⁻/A^reconf, ΔR o ΔC. Sus consecuencias pueden reflejarse en esas clases solo tras adjudicación semántica y sin doble conteo.

### 16.200.4. Parámetros estructurales: clasificación por estado epistemológico

1. **Fijados por contrato/decisión:** regla D2 de programación (W_{prog}=Z); separación de etapas; conjunción de C_dep* según sus componentes vigentes; cuatro coordenadas ΔT_acc*; función A_f*/D_f* en su alcance; B1/ENABLED/PROFILE; inicio t0, intervalos iguales y continuidad estricta de DEC-C10-100/101/102; F* y anclas terminales de O-CONF.
2. **Funciones estructurales por especificar, sin valores:** intento/cumplimiento, recepción, instalación, éxito conjunto, predicados de A_f, snapshots/diff, Reach/Π y etapas downstream. Deben definirse por estado/versión y potencial afectado.
3. **Distribuciones/soporte por justificar:** q_X*, heterogeneidad basal, dependencias transitivas, fallos/recuperación, políticas g_A, r_common, caminos directos/colaterales, interferencia y observación S3.
4. **Decisiones normativas pendientes:** población/soporte confirmatorios, admisibilidad de historias, mapping C_auth,base, relevancia/MDE, α, potencia, precisión, equivalencia y tolerancias de medición.

Una fórmula simbólica no equivale a una función implementable: cada (f_j) necesita dominio/codominio, estados 1/0/?, versión, soporte, orden temporal, parámetros y procedencia. No se asignan valores por defecto.

### 16.200.5. Regla de salida y siguiente integración

El ledger queda preparado para una adjudicación por filas: cada función se clasificará como (a) identidad fijada por contrato, (b) función estructural pendiente de especificación, (c) distribución/soporte pendiente de justificación o (d) decisión normativa. La siguiente pasada debe resolver en conjunto las funciones de intento→recepción→instalación→C_dep*, la atomización de A_f*/C_auth,base y el inventario de campos ΔX* que pueda adjudicarse sin materialización. Lo que no tenga mapping defendible queda UNKNOWN/?; no se fuerza una decisión para acelerar la simulación.

**Dictamen:** STRUCTURAL_FUNCTION_TABLE_DRAFTED / q_X_BASELINE_INVENTORY_CLASSIFIED / ΔX_FIELD_MAPPING_RULE_DEFINED_NOT_MATERIALIZED / NO_NUMERIC_PARAMETERS / NO_NEW_TEST_IDS / CALIBRATION_BLOCKED / NO_EXECUTION.


### 16.201. Adjudicación trivalente integrada de A_f*, D_f* y ΔT_acc*

**Estado:** especificación documental propuesta; no aprobada, no congelada, no implementada ni ejecutada. Se reconcilia con la fórmula candidata del maestro §67.3, el crosswalk D2 y los contratos de snapshots/evidencia. No crea una nueva definición sustantiva de accesibilidad.

#### 16.201.1. Lógica de conjunción para A_f*

Cada predicado constitutivo aplicable (ID, REL, COND, AUTH, RES, DEP y ¬BLOCK) conserva truth en {1,0,?}:

- A_f*=1 únicamente si todos los predicados requeridos son 1.
- A_f*=0 si al menos un predicado requerido es 0 con truth adjudicada.
- A_f*=? si no existe un 0 concluyente y al menos un predicado requerido permanece ? o no adjudicable.

La falta de evidencia, cobertura insuficiente, conflicto no resuelto, matching ambiguo o snapshot no comparable no se convierten en 0. La verdad del DGP y el estado observado del Analyzer se almacenan por separado; la regla anterior se aplica primero a truth y luego, con evidencia permitida, a la clasificación observada.

#### 16.201.2. Agregación de rutas dentro de DEP_f*

Cada ruta candidata se adjudica por separado, conservando identidad, versión, unidad, frontera y ventana:

- Ruta=1 si todos sus requisitos constitutivos son 1.
- Ruta=0 si al menos un requisito necesario es 0.
- Ruta=? en los demás casos no resueltos.

DEP_f*=1 si existe al menos una ruta admisible con estado 1, aunque otras rutas sean desconocidas. DEP_f*=0 solo si el universo de rutas admisibles relevante está declarado exhaustivo y todas las rutas son 0. DEP_f*=? si no se ha demostrado una ruta válida y permanece alguna ruta potencial o cobertura/inventario desconocido. Una ruta compartida, externa o alternativa no se presume válida ni inválida por su etiqueta topológica: se evalúa con el mismo contrato. La ausencia de inventario exhaustivo impide adjudicar 0 por mera ausencia de rutas observadas.

#### 16.201.3. Derivación de D_f* basal→post

Se conserva la definición:

D_f*=I(A_f,base*=0 ∧ A_f,post*=1).

Su regla trivalente derivada es:

- D_f*=1 si A_f,base*=0 y A_f,post*=1.
- D_f*=0 si A_f,base*=1 o A_f,post*=0.
- D_f*=? en cualquier otro caso, incluidos los casos en que un estado necesario sea ? y no exista ya una condición concluyente para 0.

La apertura exige snapshots basales y post comparables en unidad, transformación, frontera, versión y regla de adjudicación. No se infiere D_f*=1 desde Z, B, W_attempt, receipt, S_install o C_dep*. D_f* no sustituye A_f*(t), ni representa todos los cambios de T_acc*.

#### 16.201.4. ΔT_acc* y separación epistémica

ΔT_acc* se deriva exclusivamente de la comparación de snapshots estructurales truth comparables:

ΔT_acc*=Diff(S_T*(t0),S_T*(t1))=(ΔU*,ΔR*,ΔC*,ΔX*).

Cada campo requiere identidad/matching, tipo, versión, unidad, frontera y mapping semántico adjudicables. Si alguno no puede compararse o clasificarse, su estado permanece ?/UNKNOWN y se excluye de cualquier suma o puntuación que requiera valor determinado; no se imputa cero. Un campo mixto se descompone antes del diff; si no puede descomponerse, queda UNKNOWN. No se asigna ΔX* automáticamente a ΔC*, ΔR* ni a contexto basal.

ΔE_T registra cambios de fuentes, cobertura, validez, procedencia, versión, timestamp y adjudicación. ΔE_T no es componente de ΔT_acc* y una mejora de observabilidad no prueba cambio estructural. La apertura focal D_f*=1 puede coexistir con cambios adicionales, ausencia de otros cambios o incertidumbre en otras coordenadas; por tanto no equivale a ΔT_acc* completo.

#### 16.201.5. Límites de uso

Esta adjudicación fija reglas lógicas de propagación, no inventario exhaustivo, evidencia, probabilidades, parámetros, mappings físicos, tolerancias ni distribución de q_X*. No cierra RES/REL/COND/BLOCK, el universo de rutas, el contrato de snapshots, la medición observada ni la validez del oráculo. Tampoco autoriza implementación o ejecución. Los casos de conflicto, cobertura parcial y no comparabilidad deben conservarse en los escenarios adversariales existentes, sin crear nuevos IDs de prueba por esta integración.

**Dictamen:** TRI-STATE_LOGIC_SPECIFIED_AS_DRAFT / ROUTE_EXISTENCE_RULE_SPECIFIED_AS_DRAFT / D_F_BASELINE_POST_RULE_SPECIFIED_AS_DRAFT / ΔT_ACC_SNAPSHOT_DIFF_BOUNDARY_SPECIFIED_AS_DRAFT / NO_NUMERIC_PARAMETERS / NO_EXECUTION.


## 16.202. Reconciliación AUTH_f* y contrato de snapshots (2026-11-12)

Esta sección cierra la divergencia documental entre el maestro, DEC-C10-067, la ficha D2-INV-AUTH-01 y los contratos de identidad/snapshot. No crea una decisión nueva ni convierte las propuestas operacionales en contratos aprobados.

### A. Correspondencia de autorización

1. **Regla conceptual fijada por precedencia:** DEC-C10-067 exige que la autorización normativa funcional basal para τ₂ sea común (C_auth,base=1) y que B_g0^D2/B_g1^D2 no la modifiquen. El maestro §67.3 y el crosswalk D2 establecen que C_auth,base se corresponde con el predicado AUTH_f*; no se añade como factor independiente ni se duplica dentro de C_dep*.
2. **Distinción de dominios:** autorización normativa funcional para realizar τ₂ = AUTH_f*; ACL/credenciales/tokens/endpoints técnicos necesarios para provisionar = superficie técnica de B y/o relaciones/dependencias según su función; conocimiento/consideración del agente = mecanismo downstream. No son intercambiables.
3. **Vía de desviación:** si B cambia la autorización normativa funcional, se materializa la vía B → AUTH_f* → A_f*. Debe registrarse como desviación/cointervención y el ITT conserva interpretación de efecto del paquete; no se atribuye automáticamente a accesibilidad técnica aislada.
4. **Qué queda abierto:** identificar titular competente, fuente normativa, objeto y alcance autorizado, versión, vigencia, regla de adjudicación, registros basales y post, cobertura y evidencia independiente. Sin ello, el valor observado/analizado no se presume 1: la truth del DGP se estipula según el diseño y el Analyzer conserva ? cuando la evidencia no identifica.
5. **Estado:** correspondencia conceptual RESOLVED_BY_PRECEDENCE; materialización, evidencia y prueba de invariancia NOT_VERIFIABLE / OPEN. D2 sigue sin acreditación material de aislamiento.

### B. Contrato de snapshots reutilizado, sin duplicación

1. El objeto estructural sigue siendo S_T*(i,b,c,t)=(U_t*,R_t*,C_t*,X_t*); el paquete epistémico E_T permanece separado. ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*); ΔE_T recoge cambios de fuentes, cobertura, validez de evidencia, procedencia, versión y adjudicación.
2. La comparación basal/post exige misma unidad lógica, frontera y versión de frontera, contexto declarado, granularidad G, catálogo/vocabulario y reglas de composición/mapping compatibles. Si no hay comparabilidad directa, solo se aplica mapping explícito y trazable a granularidad común; en caso contrario, diff afectado = UNKNOWN/? o DIFF_NOT_COMPARABLE, sin imputar cero.
3. Se conserva la jerarquía de identidad/matching del contrato C10-S-ID-MATCH-001: ID canónico exacto; alias registrado; continuidad de versión con firma semántica; candidato semántico sujeto a adjudicación; split/merge explícitos; no-match solo con cobertura suficiente. Hash, nombre, similitud textual o proximidad temporal no bastan para identidad.
4. DEC-C10-065 obliga a fijar (snapshot_id, snapshot_object_record_id) con FK compuesta exacta en NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP. No se resuelve por timestamp, última versión, orden de inserción ni fallback. La aceptación arquitectónica no equivale a validación técnica de esquema/constraints.
5. Cada diff debe conservar valores basal/post, IDs y versiones, regla de matching, frontera/unidad/G, vigencia/evento, evidencia/cobertura y adjudicación. Los cambios de X* no se convierten automáticamente en ADD/REMOVE; campos mixtos se descomponen o quedan ?.

### C. Dependencias de cierre integradas

No abrir otro contrato. Completar en los artefactos ya existentes: (i) roster material de autorización y de objetos U/R/C/X; (ii) mapping de cada campo de X* y de condiciones REL/COND/RES/DEP/BLOCK sin doble contabilización; (iii) snapshots y cobertura pre-B/post-B/rollback con pinning exacto; (iv) adjudicación ciega y separación Generator/Analyzer/Evaluator; (v) pruebas de invariancia/no-afectación y registro de colaterales. Los inventarios marcados NO INVENTARIADO no equivalen a ausencia.

**Límite:** esta reconciliación documental no cierra los predicados materiales, no valida el oráculo ni la medición, no fija distribuciones/parametría, no alcanza Design Freeze y no autoriza implementación, simulación, estimación, calibración ni ejecución. scientific_execution=false; execution_authorized=false.


## 16.203. Regla de separación y no duplicidad para ID_f*, REL_f*, COND_f*, DEP_f* y BLOCK_f* (2026-11-12)

**Tipo:** adjudicación semántica derivada de la fórmula candidata §67.3 y de los contratos de frontera, grafo, provisión, instancia y snapshots. No constituye decisión normativa nueva, no asigna valores ni cierra inventarios.

### 16.203.1. Asignación primaria por función material

1. **ID_f*** responde a qué transformación focal es: identidad semántica, clase/tipo y versión contractual de τ₂. El hash/build y el identificador de registro son evidencia/identidad técnica versionada, no sustitutos automáticos de identidad semántica.
2. **REL_f*** responde qué relaciones/interfaces tipadas son constitutivamente necesarias para invocar o componer τ₂: extremos, dirección, tipo/rol, alcance y condiciones de relación. Su existencia declarada no demuestra que haya una ruta técnica completa operativa.
3. **COND_f*** recoge condiciones constitutivas de realizabilidad que no son identidad del objeto ni relaciones ni dependencias de una ruta y que son independientes de las precondiciones particulares del estado de entrada S0. La compatibilidad del dominio/tipo se asigna a ID_f* cuando define el tipo admisible de τ₂; se asigna a COND_f* cuando es una condición externa de realizabilidad. `D_support*` queda como descriptor histórico, no como factor adicional.
4. **DEP_f*** responde si existe al menos una ruta técnica completa admisible que realiza las relaciones necesarias y satisface sus requisitos. Se evalúa por rutas y con la regla OR/trivalente ya fijada en §16.201. REL especifica requisitos relacionales; DEP evalúa su realización en una ruta concreta. No se duplican la misma arista/condición ni el mismo fallo en ambos términos.
5. **BLOCK_f*** representa una prohibición/bloqueo efectivo, vigente y aplicable a τ₂, con alcance y ventana explícitos. Un bloqueo de una ruta concreta invalida esa ruta; solo un bloqueo universal o que cubra todas las rutas admisibles puede hacer `BLOCK_f*=1` para la transformación en conjunto. La mera ausencia de evidencia, una ruta no inventariada o un bloqueo focal con alternativa válida no prueban bloqueo global.
6. **App_f*** permanece separado: precondiciones dependientes del estado concreto S0 se evalúan al aplicar τ₂ desde ese estado; no se introducen como COND_f* por conveniencia.

### 16.203.2. Regla de precedencia para clasificar cada campo

Para cada campo/condición material, identificar primero su referente y scope; después aplicar en orden: (a) identidad/tipo del objeto → ID; (b) relación tipada entre objetos → REL; (c) dependencia/ruta técnica de realización → DEP; (d) condición constitutiva externa e independiente de S0 → COND; (e) prohibición efectiva → BLOCK; (f) precondición del estado de entrada → App; (g) dato sobre conocimiento/observabilidad → mecanismo downstream o E_T. Si un campo mezcla funciones, descomponerlo; si no puede descomponerse o clasificarse, conservar UNKNOWN/? y no duplicarlo en dos términos.

### 16.203.3. Consecuencias para la agregación

- La fórmula A_f* de §67.3 se conserva sin añadir `C_domain`, `D_support*`, `C_other`, `App_f*` ni `C_info` como factores adicionales.
- `DEP_f*` se adjudica por existencia de ruta válida; por tanto, `BLOCK_f*` debe referirse a bloqueo de la transformación en conjunto, no al fallo de una única ruta si otra admisible permanece válida.
- La clasificación conceptual queda fijada; permanecen abiertos el roster material de campos/condiciones, las rutas y dependencias reales, las fuentes, cobertura, versiones, umbrales y adjudicación independiente. `NO INVENTARIADO`/`?` no se recodifica como 0.

**Dictamen:** SEMANTIC_BOUNDARIES_RESOLVED_BY_PRECEDENCE / FIELD_LEVEL_MAPPING_AND_INVENTORY_OPEN / NO_NUMERIC_PARAMETERS / NO_DESIGN_FREEZE / NO_EXECUTION.

## 16.204. Mapping negativo/positivo entre roster P0 y predicados de accesibilidad (2026-11-12)

**Objetivo:** resolver qué elementos del DGP de configuración actual pueden alimentar los predicados de A_f* y cuáles no, sin equiparar el objeto configuracional con el espacio transformacional. Se reutilizan DEC-C10-053/056/068/069/077/082/083, la matriz IAM §§18–20, el contrato abstracto y el manifiesto P1.

### A. Resultado de mapping por clase

| Clase/elemento aceptado | Función e identidad ya fijadas | Mapping admisible a A_f* | Dictamen |
|---|---|---|---|
| `contract_id/version`, `instance_id/version`, `component_id/class` (CMP) | Identidad contractual/instancia/componente del paquete de servicio | Evidencia del objeto/contexto configuracional; no es identidad semántica de τ₂ (`ID_f*`) | No equivalencia; ID_f* requiere contrato/versión propios de τ₂ |
| `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` | Propiedades P0 REQUIRED del CMP; BOOL/ENUM, dominios aceptados por DEC-C10-068/083 | Pueden integrar el objeto/configuración sobre el que opera τ₂; no prueban por sí mismas `ID`, `REL`, `COND`, `DEP`, `AUTH`, `RES` ni ausencia de `BLOCK` | Fuera de los predicados de acceso salvo regla explícita del contrato de τ₂; no usar como proxy |
| `RUL-SVC-ENABLE-PROFILE-01` y AST→PAR bindings | Regla constitutiva P0 REQUIRE con operandos tipados | Sus bindings son referencias sintácticas de AST a PAR; no son relaciones de dominio `REL_f*`, REF funcional ni rutas técnicas `DEP_f*` | Excluir de REL/DEP por mera existencia del AST |
| `REF` declarativo | Clase de relación de configuración con identidad propia, extremos tipados y mapping explícito a EDGE si procede | Solo podría contribuir a `REL_f*` si el contrato de τ₂ declara que esa relación concreta es necesaria para invocarlo/componerlo. No prueba la ruta técnica completa (`DEP_f*`) | Roster mínimo no exige REF; REF=0 no adjudicado; mantener `?` hasta inventario COMPLETE por snapshot/etapa/ruta/scope |
| `POL` | Ausente por diseño del núcleo confirmatorio mínimo | No aporta `AUTH_f*`; la autorización normativa basal y ACL/credenciales técnicas pertenecen a contratos/superficies diferentes | No crear POL ni inferir AUTH desde su ausencia |
| `MET` / snapshots / E_T | Identidad, versión, procedencia y evidencia | Habilita matching y clasificación observada; no es componente de truth A_f* ni de ΔT_acc* | Epistémico; separar `E_T`/`ΔE_T` |
| P1: `C_install`, `C_integrity`, `C_compat`, `C_oper`, `C_dep*` | Éxito técnico de la dependencia provisionada | Puede operacionalizar una ruta focal dentro de `DEP_f*` solo bajo la ruta única estipulada; no sustituye A_f* completa ni otras rutas | Mantener componentes y alternativas separados |
| P1: `C_auth,base` / `AUTH_f*` | Autorización normativa funcional basal común, no modificada por B según DEC-C10-067 | Correspondencia conceptual directa con `AUTH_f*` | Materialización, fuente, titular, vigencia y evidencia siguen OPEN |
| P1: recursos/capacidad | Disponibilidad ex ante necesaria y no duplicada; separar capacidad provisionada y consumo | Solo la disponibilidad no focal que habilita oferta puede integrar `RES_f*`; consumo/contención inducida por B es vía colateral/interferencia | Mapping condicional; inventario/umbral/cobertura OPEN |
| P1: interfaces, servicios externos y relaciones técnicas | Grafo técnico versionado y cierre transitivo de rutas | Interfaz/relación requerida puede alimentar REL; ruta técnica completa y sus dependencias alimentan DEP; condiciones ambientales independientes de S0 alimentan COND; bloqueos efectivos alimentan BLOCK | Clasificación campo a campo; fuentes reales no inventariadas |

### B. Campos de A_f* que no están representados aún por el roster P0

1. `ID_f*`: identificador semántico estable de τ₂, tipo, contrato y versión; no derivarlo de `component_id` CMP ni del hash del paquete.
2. `REL_f*`: inventario de interfaces/relaciones funcionalmente necesarias para τ₂; no derivarlo de AST operand bindings ni de FK/EDGE por nombre.
3. `COND_f*`: condiciones constitutivas externas a la identidad, relaciones y rutas, independientes de S0; cada candidato debe probar su necesidad y scope.
4. `DEP_f*`: inventario de rutas completas, directas, transitivas, alternativas, compartidas, externas y dinámicas; `C_dep*` solo cubre la ruta provisionada estipulada, no el universo por defecto.
5. `BLOCK_f*`: registro de prohibiciones/bloqueos efectivos con alcance y ventana; no se obtiene por ausencia de ruta observada ni por cobertura parcial.

### C. Consecuencia y gate

El mapping semántico de clase queda RESOLVED: no existe equivalencia automática P0↔predicados A_f*. Se resuelve también la ubicación funcional de los elementos conocidos (AUTH, C_dep, recursos, E_T). El mapping material de cada interfaz, condición, ruta y bloqueo permanece OPEN. REF permanece UNKNOWN, no 0. No se crean filas IAM, snapshots, IDs físicos, fixtures ni valores de DGP. Antes de especificar distribuciones conjuntas debe existir roster de τ₂ y de superficies P1 por unidad/versión, con cobertura y fuentes identificadas.

**Dictamen:** CLASS_BOUNDARY_RESOLVED / PREDICATE_SOURCE_ROSTER_OPEN / REF_NOT_ADJUDICATED / NO_DESIGN_FREEZE / NO_EXECUTION.

## 16.205. Roster de fuentes de verdad para A_f* y superficies P1 — contrato de captura sin inventario ficticio (2026-11-12)

**Base:** U_G y predicados de `C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md` §§2–7; B-M01…15 y PROV-01…12 del manifiesto; crosswalk de clases §16.204; identidad/versionado y snapshots DEC-C10-062/065/069/079/082/089. Esta sección operacionaliza el roster en el artefacto existente; no crea IDs ni declara fuentes presentes.

### 16.205.1. Campos obligatorios de cada registro de fuente

Cada fuente material que se incorpore al roster debe registrar: `source_record_id` (ID exacto de origen; no inventar), `source_class` (contract/API/schema/SBOM/package_manifest/runtime_config/ACL_policy/resource_quota/network_policy/security_policy/state_snapshot/external_service/functional_test/oracle/evidence_log), `source_owner`, `source_locator`, `unit_id` + `unit_object_record_id`, `snapshot_id` + `snapshot_object_record_id` cuando aplique, `object_id` + `object_record_id`, `semantic_role`, `version`, `hash` o razón de no aplicabilidad, `valid_from/to`, `capture_time`, `observer`, `blinding/access_class`, `coverage_scope`, `method`, `error/limitations`, `predicate_mapping`, `U_G node/edge mapping`, `truth_dgp` (solo Generator/Evaluator), `observed_evidence_status` (Analyzer), y `adjudication_status`. No se registra ningún secreto; ACL/tokens se representan mediante alcance/identificadores y evidencia redactada.

### 16.205.2. Roster por predicado y fuentes mínimas que deben localizarse

| Predicado | Fuentes primarias a recuperar/crear solo cuando existan | Nodos/aristas U_G candidatos | Límite de adjudicación |
|---|---|---|---|
| `ID_f*` | Contrato funcional de τ₂/F1; TID/SID/RID; clase/tipo, versión contractual y mapping de identidad del artefacto/runtime focal | N04, N10; E02–E04 | CMP ID, hash/build o nombre no sustituyen identidad semántica de τ₂; sin contrato/versionado → `?` |
| `REL_f*` | API/schema; endpoints; interfaces tipadas, extremos, dirección, roles, scope; ACL de canal separada de autorización funcional | N07, N17, N20–N21; E05, E18–E20 | Endpoint aislado no prueba todas las relaciones necesarias ni su disponibilidad; REF declarativo no equivale a canal técnico |
| `COND_f*` | Contrato de realizabilidad F1; restricciones ambientales externas a S0; requisitos de compatibilidad y condiciones constitutivas con scope/ventana | N01, N19–N21; E19–E21 | Precondiciones dependientes de S0 son `App_f*`; no duplicarlas como COND |
| `AUTH_f*` | Fuente normativa/titular de autorización basal; roles/alcance/vigencia; diffs pre/post B; ACL/credenciales técnicas por separado | N17; E18; B-M05/B-M08 | DEC-C10-067 fija invariancia conceptual, no demuestra estado material ni invariancia observada; sin fuente/titular/evidencia → `?` |
| `RES_f*` | Capacidad utilizable ex ante, cuotas/reservas, demanda concurrente, consumidores, colas y medición por unidad/ventana | N18, N05, N13, N15; E16–E17 | Separar capacidad instalada, reserva, disponibilidad y consumo; contención es vía colateral/interferencia, no RES basal automáticamente |
| `DEP_f*` | SBOM/manifiesto de artefactos; runtime/imagen; librerías transitivas; servicios/API; relaciones calls/loads/reads/writes/authenticates/shares_resource; versiones y consumidores | N04–N07, N20–N21, N13–N15; E02–E06, E11–E14, E19–E20 | `C_dep*` solo caracteriza la dependencia provisionada; incluir rutas directas, transitivas, alternativas, compartidas, externas y dinámicas; cobertura incompleta → `?` |
| `BLOCK_f*` | Políticas de seguridad, firewall/red, certificados, permisos, restricciones de runtime, bloqueos de servicio y vigencia/alcance | N07, N17–N21; E18–E21; B-M08/B-M09 | Bloqueo local invalida una ruta; bloqueo de transformación solo con universalidad/cobertura de todas las rutas; ausencia de logs no prueba ausencia |

### 16.205.3. Roster de superficies P1 y control de colaterales

El manifiesto B-M01…15 se usa como índice de superficies, no como fuente observada. Para cada unidad y versión se enlazan B-M01 artefacto/SBOM; B-M02 runtime; B-M03 host; B-M04 interfaz; B-M05 permisos; B-M06 datos/estado; B-M07 recursos; B-M08 red; B-M09 seguridad; B-M10 observabilidad; B-M11 estado persistente; B-M12 rendimiento; B-M13 oráculo (prohibido modificar); B-M14 alternativa A1/A2 (prohibido modificar); B-M15 rollback/residuos. Cada fila exige evidencia pre-B/post-B/rollback, consumidores, ventana y cobertura; la prohibición de modificación no prueba cumplimiento.

Snapshots requeridos se mantienen en el contrato existente: `S_preB`, `S_postB`, `S_rollback` y `S_routeA`, con pinning exacto DEC-C10-065. No se crea un snapshot nuevo ni se presume que exista. La cobertura debe ser explícita por unidad×snapshot×componente/relación×ruta×ventana×versión; si una dimensión no está inspeccionada, la cobertura global no puede marcarse COMPLETE.

### 16.205.4. Estado de cierre del roster

El roster queda **especificado como contrato de captura**, pero **no materializado**: no hay fuentes reales recuperadas, SBOM, runtime, APIs, ACL, recursos medidos, grafo transitivo ni snapshots observados. Los N01–N23/E01–E23 siguen roles/aristas candidatos con existencia `?` y cobertura `NONE`; B-M01…12/B-M15 permanecen `NO INVENTARIADO`; B-M13/B-M14 son superficies contractualmente prohibidas, cuyo cumplimiento material sigue `?`. `REF=UNKNOWN`; `Reach=?`; `A_f*=?`; `D_f*` no adjudicable.

**Gate para el siguiente bloque:** no especificar distribuciones conjuntas de `ID/REL/COND/AUTH/RES/DEP/BLOCK` como si fueran empíricas hasta (a) declarar el universo finito de fuentes/unidades/versiones por construcción del DGP, (b) asignar verdad sintética en Generator a partir de reglas explícitas, (c) definir observación imperfecta separada para Analyzer y (d) fijar cobertura/adjudicación en Evaluator. El DGP puede estipular mundos sintéticos; no puede presentarlos como inventario real del microdominio.

**Dictamen:** SOURCE_ROSTER_SCHEMA_SPECIFIED / SOURCE_INVENTORY_NOT_MATERIALIZED / U_G_COVERAGE_NONE / NO_NUMERIC_PARAMETERS / NO_DESIGN_FREEZE / NO_EXECUTION.

## 16.206. Corrección de alcance: DGP abstracto, no caso real de migración (2026-11-12)

**Precedencia interpretativa:** se preservan DEC-C10-051/052 y la selección del microdominio lógico de configuración/migración como andamiaje semántico del benchmark. La aclaración expresa del usuario es que C10-S **no es un caso real de migración** ni pretende representar, reconstruir o validar una migración de producción. El microdominio es una gramática de juguete controlada para generar mundos sintéticos; no un objeto de estudio empírico ni una especificación de despliegue real.

### 16.206.1. Consecuencias obligatorias

1. No buscar ni recopilar SBOM, runtimes, APIs, ACL, hosts, servicios externos, cuotas, logs, snapshots o infraestructura reales. No exigir acceso a plataformas, software, entornos, proveedores ni expertos de migración.
2. Los términos CMP/PAR/REF/RUL/MET, P0/P1/P2, F1/F2/A1/A2, B-M01…15, N/E y S_preB/S_postB/S_rollback/S_routeA designan clases, roles y registros **sintéticos** dentro del DGP, salvo que un artefacto se identifique explícitamente como metadato del propio experimento. No presuponen que exista un sistema real correspondiente.
3. El roster §16.205 se reinterpreta como **esquema de entidades y fuentes sintéticas que Generator instancia** y como contrato de evidencia sintética que Analyzer recibe; no como inventario de fuentes reales pendientes de recuperar. `source_locator`, `owner`, `capture_time` y `hash` se sustituyen/representan con identificadores y procedencia sintéticos reproducibles cuando no exista una fuente externa real.
4. Las superficies P1 son variables abstractas del entorno causal (dependencias, autorización, recursos, interfaces, bloqueos, observabilidad, etc.). Solo se incluyen cuando sirven para representar una vía causal, alternativa, colateral, interacción o mecanismo de observación que el experimento deba probar.
5. La complejidad no se añade para ganar realismo operativo. Cada entidad, relación, condición o dimensión debe justificar qué hipótesis, estimando, mecanismo, falsador o fallo de identificación permite probar. El núcleo mínimo debe mantenerse finito y parsimonioso.
6. El Generator asigna la truth estructural y potencial por reglas explícitas; produce después evidencia observada con cobertura/error/missingness controlados. Analyzer no ve truth ni parámetros causales ocultos. Evaluator abre truth tras sellar la salida del Analyzer.
7. El benchmark debe contener mundos de control donde el método deba recuperar efectos conocidos y mundos adversariales donde deba detectar nulos, signos adversos, vías directas/colaterales, alternativas, interacciones, heterogeneidad, interferencia, weak/null IV, falta de soporte, error y no-identificación. La migración no es el resultado a medir: lo es la capacidad metodológica de reconstrucción e inferencia causal-transformacional.

### 16.206.2. Relectura del estado del roster

Se retira la interpretación de §16.205.4 como necesidad de recuperar fuentes reales. El roster está **definido como contrato de modelado**, pero falta instanciar el universo sintético finito y sus reglas de generación. `NONE`/`?` describen ausencia de una instancia/verdad/evidencia definida en el borrador actual, no una deficiencia de recopilación de datos reales. B-M13 (oráculo) y B-M14 (alternativa) son roles sintéticos protegidos contra contaminación del Analyzer/Generator según el contrato de roles; su separación se verifica en el diseño, no inspeccionando sistemas externos.

**Gate correcto:** especificar la ontología finita del mundo sintético, los mecanismos generadores y los canales de observación/adjudicación. No abrir una fase de trabajo de campo ni exigir fuentes reales. No fijar todavía cardinalidades o parámetros numéricos no justificados.

**Dictamen:** ABSTRACT_SYNTHETIC_BENCHMARK_SCOPE_CLARIFIED / REAL_MIGRATION_CASE_NOT_IN_SCOPE / SYNTHETIC_ROSTER_INSTANTIATION_OPEN / NO_EXECUTION.

## 16.207. Especificación del universo sintético finito y arquitectura de escenarios (2026-11-12)

**Precedencia:** esta sección operacionaliza §§16.188–16.206 y los contratos DGP/PD/inventario. No crea una nueva familia de escenarios ni aprueba cardinalidades, parámetros, H, estimandos o Design Freeze.

### 16.207.1. Unidad lógica de mundo y ontología mínima candidata

Un mundo sintético `w` es una instancia finita y versionada de un mecanismo causal-transformacional, con una o más unidades `i`, historia basal `X_i/H_i0`, asignación `Z_i`, régimen/política `B`, estados estructurales, catálogo finito de transformaciones, relaciones de composición, condiciones de aplicabilidad, rutas, trayectorias potenciales y procesos separados de observación/evaluación. La unidad de asignación puede coincidir con UE solo bajo aislamiento; si hay exposición compartida, el mundo debe definir clúster/mapa de exposición antes de invocar SUTVA.

Como **esqueleto candidato reutilizado**, no como cardinalidad confirmatoria: estados `S0/S1/S2/SF`; transformaciones `F1/F2/A1/A2`; ruta focal `F1→F2`; ruta alternativa `A1→A2`; horizonte `H` y granularidad `G` parametrizables. `H=3`, las cuatro transformaciones y las dos rutas permanecen candidatos del inventario, no decisiones ratificadas. No añadir TID, estados o rutas adicionales salvo que discriminen una hipótesis/falsador no cubierto.

### 16.207.2. Arquitectura de escenarios sin factorial completo

R0–R3 del inventario son **perfiles de topología/alternativas y provisión**, no cuatro DGP completos ni cuatro resultados. Se reutilizan como base:

- R0: focal exclusiva solo dentro del universo sintético exhaustivamente estipulado.
- R1: alternativa basal estable; apertura focal no equivale a apertura funcional exclusiva.
- R2: alternativa afectada; vía colateral que impide interpretar automáticamente D2 como instrumento focal.
- R3: fallo de provisión por etapas; no imputar `C_dep*`, `A_f*` o `D_f*` desde Z o intento.

Sobre estos perfiles se instancian selectivamente los mecanismos adversariales ya enumerados en PD §4 y el ledger §16.188.4: focal aislado, nulo, fallo parcial, adverso, vía directa, colateral, interacción/heterogeneidad, IV débil/nulo/defiers/exclusión, interferencia, versionado/crossover, observación diferencial, soporte fallido y datos incompletos/censura. No se exige producto cartesiano ni se crean IDs nuevos. Cada mundo seleccionado debe cubrir un contraste o falsador concreto y declarar qué perfiles/mecanismos combina.

### 16.207.3. Funciones generadoras y coherencia contrafactual

Para cada mundo se definen funciones estructurales versionadas y un vector de exógenas comunes `U_i` (o `U_c` si la asignación/exposición es por clúster). Los potenciales bajo cada régimen se derivan de las mismas funciones y exógenas compartidas; no se generan como tablas independientes incompatibles. La dependencia entre programación, intento, recepción, instalación, `C_dep*`, predicados `A_f*`, `D_f*`, `ΔT_acc*`, Reach/Π, trayectorias y resultados se estipula explícitamente, sin asumir independencia, monotonicidad, exclusión, positividad o mediación serial.

Se preservan las etapas: `Z → W_programmed → W_attempt → receipt → S_install → C_dep* → A_f*/D_f* → ΔT_acc* → Reach/Π → K/Consider → Sel/Start → Exec → O/V`. Es una lista de variables con dependencias posibles, no una cadena determinista. Se añaden ramas directas y colaterales en la propia función generadora cuando el mundo deba probarlas.

### 16.207.4. Condición de suficiencia científica

El conjunto de mundos es suficiente solo si permite: (a) recuperar una contribución conocida de `ΔT_acc*` cuando el diseño y los supuestos la hacen identificable; (b) recuperar nulo o signo adverso cuando esa sea la truth; (c) distinguir efecto total D2/paquete de efecto atribuible a accesibilidad; (d) detectar alternativas, vías directas/colaterales e interacciones; y (e) producir bounds/abstención/no-identificación cuando falte soporte, medición o identificación. La exactitud del analizador reconstructivo no sustituye la prueba de atribución causal.

O-CONF, `V_cont` y Value siguen siendo variables/constructos distintos. `O-CONF_truth` se deriva del criterio terminal F*; `V_cont_truth` de B1 por intervalos; Value requiere la regla PA aprobada. Mientras Value no esté instanciado, el bloque de estimandos/resultados sobre Value permanece explícitamente bloqueado: no sustituirlo por O-CONF ni por `V_cont`.

### 16.207.5. Evidencia sintética y cierre de roles

Las clases de fuente del roster §16.205 son tipos abstractos de registros generados, no fuentes físicas requeridas. El Generator produce truth estructural, potenciales y metadatos sintéticos; genera después `observed_evidence` mediante un canal con cobertura, error, pérdida, lag y sesgo estipulados. Analyzer recibe solo evidencia permitida y sellada. Evaluator conserva truth independiente y compara después del sellado. El oráculo/verdad de evaluación no se expone al Analyzer; la alternativa A1/A2 solo se modifica cuando el mecanismo R2 lo estipula, no por accidente de generación.

**Siguiente gate:** formalizar las funciones generadoras por bloque causal y la matriz selectiva `perfil R0–R3 × mecanismo PD × contraste/estimando × salida esperada`, sin asignar probabilidades ni ejecutar. La identificación y el soporte se evalúan antes de dimensionar/calibrar.

**Dictamen:** FINITE_SYNTHETIC_WORLD_ARCHITECTURE_SPECIFIED_CANDIDATE / R0_R3_REUSED_NOT_FROZEN / MECHANISM_OVERLAYS_SELECTIVE / VALUE_OPERATIONALIZATION_BLOCKED_BY_PA / NO_NUMERIC_PARAMETERS / NO_EXECUTION.


## 16.208. Paquete integrado del universo finito, mecanismos generadores y verdad causal (2026-11-12)

**Estado:** especificación integrada candidata derivada de §§16.188–16.207 y contratos finitos, DGP temporal/roles y PD. DRAFT / NO APROBADA / NO CONGELADA. No crea nuevas familias de tests ni parámetros numéricos. Hace operativa documentalmente la arquitectura ya definida, evitando abrir otro inventario paralelo.

### 16.208.1. Significado y límite del universo finito

El universo confirmatorio candidato no es el producto cartesiano de todos los factores. Es un roster finito y dirigido de clases de mundos. Cada mundo es una instancia sintética finita, versionada y reproducible de un mecanismo; cada clase activa solo los ejes necesarios para un contraste o falsador. Los perfiles R0–R3 describen topología, alternativas y provisión; los mecanismos PD describen la verdad causal adversarial. Ninguno de los dos, aislado, constituye un mundo completo.

La ontología mínima reutiliza, sin ratificar aún sus cardinalidades: unidad(es) UE y unidad(es) de asignación UA; historia basal; política D2; estados S0/S1/S2/SF; transformaciones F1/F2/A1/A2; relaciones F1→F2 y A1→A2; predicados ID/REL/COND/AUTH/RES/DEP/BLOCK; snapshots y versiones; rutas y trayectorias potenciales; resultados O-CONF y V_cont separados; y procesos de evidencia. H=3, cuatro transformaciones y dos rutas siguen siendo candidatos. Cada mundo declara frontera, G, H, estructura de unidades, asignación, alternativas incluidas y criterio de exhaustividad. No se admite «ausencia de alternativa» sin roster exhaustivo.

### 16.208.2. Roster mínimo dirigido de clases de mundo

La tabla materializa la matriz §16.188.4 + PD §4 sobre R0–R3. Los nombres son etiquetas descriptivas, no nuevos IDs de test. No se exige cruzar cada clase con todos los perfiles.

| Clase de mundo | Perfil/topología base | Mecanismo generador activado | Verdad causal estipulada | Salida exigida al Analyzer |
|---|---|---|---|---|
| Focal limpio | R0 | D2 modifica provisión focal; resto invariante; sin vía directa/colateral; soporte y mapping estipulados | Contribución focal conocida solo en el contraste y régimen que realmente la identifican | ITT-D2 por resultado; atribución focal solo si mapping, soporte, medición y supuestos se satisfacen |
| Nulo | R0 o R3 | Z no modifica la cadena focal relevante, o una transición posterior neutraliza la primera etapa | Efecto nulo para el resultado/estimando designado; no se fuerza nulo para otros resultados | Recuperar nulo dentro de precisión; no fabricar primera etapa ni causalidad |
| Fallo por etapas | R3 | Fallos separados en intento, recepción, instalación, integridad, compatibilidad, operatividad o dependencia | Cada etapa conserva su potencial; el éxito anterior no determina el posterior | ITT por Z; primeras etapas separadas; no imputar C_dep*, A_f* o D_f* |
| Focal adverso | R0 | La intervención deteriora una coordenada ΔU/ΔR/ΔC/ΔX, Reach o resultado | Signo adverso conocido; sin monotonicidad positiva impuesta | Recuperar dirección o declarar límites/no identificación |
| Alternativa basal | R1 | A1→A2 disponible y estable mientras puede abrirse F1→F2 | Apertura focal no implica incremento de Reach ni exclusividad funcional | Distinguir D_f* de Reach; no atribuir resultado a τ2 por mera apertura |
| Alternativa afectada/colateral | R2 | B modifica A1/A2, dependencias, recursos u otra ruta | Existe vía no focal; exclusión focal falla salvo prueba contraria | Efecto de paquete; no interpretar automáticamente D2 como instrumento focal |
| Vía directa | R0–R3 según soporte | B afecta O-CONF o V_cont por camino que no atraviesa ΔT_acc* | Efecto directo/paquete conocido, sin mediación focal exclusiva | Identificar ITT de paquete; atribución a ΔT_acc* solo si separable |
| Interacción/heterogeneidad | R0–R2 | Funciones dependen de historia basal, alternativa, recursos, versión o unidad | Efectos condicionales y composición de respuesta conocidos por construcción | Recuperar interacción/heterogeneidad; no transportar LATE ni mezclar D1/D2 |
| IV adversarial | R0–R3 | Primera etapa nula/débil, defiers, exclusión o monotonicidad violadas | Supuesto IV violado de forma conocida | No aplicar Wald inválido; weak-IV, bounds o NOT_IDENTIFIED |
| Interferencia | Perfil con exposición compartida | Recursos, pool, canal o clúster conectan unidades | Potenciales dependen de asignación/exposición de otras unidades | Definir UA y mapa de exposición; si no, abstenerse de SUTVA |
| Observación adversarial | Cualquier perfil compatible | Error, pérdida, lag, cobertura o sesgo diferencial; dependencia entre señales | Truth estructural no cambia por cambiar la evidencia | Recuperar si identificable; si no, bounds/abstención; no convertir falta en cero |
| Soporte/ausencia/censura | Cualquier perfil compatible | Historia imposible, positividad fallida, missingness MCAR/MAR/MNAR o censura | Estimando identificado, acotado o no identificado según mecanismo | Dictamen por estimando con supuestos; no extrapolar fuera de soporte |

La cobertura mínima exige un control negativo apropiado, un mundo con contribución conocida recuperable bajo supuestos explícitos y mundos que obliguen a distinguir efecto de paquete, vía focal, alternativa y no-identificación. La selección final debe demostrar qué fila cubre cada contraste/falsador de §16.188.4; las filas no cubiertas quedan como brecha explícita, no se declaran superadas por analogía.

### 16.208.3. Contrato generador común: funciones, potenciales y dependencia

Para cada mundo w, unidad i y régimen z, Generator define una única colección versionada de funciones estructurales y exógenas comunes U_i (o U_c cuando asignación/exposición sea por clúster). Los potenciales de todos los regímenes se derivan de esas mismas funciones y exógenas; queda prohibido generar por separado tablas potenciales incompatibles o asignar independientemente etapas cuya dependencia esté definida.

La forma funcional mínima, sin imponer distribuciones ni independencia, es:

1. **Basal:** X_i, H_i0, C_i, F_alt,i0 y snapshots basales admisibles se generan conjuntamente desde q_X*. E/App definen marco/aplicabilidad según su contrato. En núcleo limpio se estipula C_dep,0*=0 y A_f,0*=0; en estrés, cualquier desviación o UNKNOWN se declara antes de generar resultados.
2. **Asignación:** Z_i o Z_c se genera conforme al mecanismo que finalmente se especifique. En D2, W_programmed_i(z)=z por definición de política; ello no fija W_attempt ni cumplimiento.
3. **Provisión:** W_attempt=f_att(W_programmed,Z,X,H0,version,U_att); receipt=f_rec(W_attempt,policy,version,logistics,environment,U_rec); S_install=f_inst(receipt,version,integrity,compatibility,operability,U_inst); C_dep*=f_dep(W_attempt,receipt,S_install,componentes,grafo,U_dep). Las funciones mantienen fallos parciales y dependencias conjuntas.
4. **Acceso/transformación:** cada predicado ID/REL/COND/AUTH/RES/DEP/¬BLOCK se genera por su mecanismo y momento; A_f* aplica la lógica trivalente vigente; D_f*=I(A_f,base*=0 ∧ A_f,post*=1) cuando snapshots sean comparables. T_acc* se representa por snapshots completos y ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*); ΔE_T queda fuera. No se infiere ΔT_acc* desde D_f*.
5. **Reach/trayectoria:** Reach y Π se derivan del catálogo finito, relaciones, aplicabilidad, predicados de ruta, recursos, versiones y horizonte declarados; no desde ejecución observada. K/Consider, Sel, Start y Exec se generan como etapas distintas, con no-transiciones explícitas.
6. **Resultados:** O-CONF_truth se deriva del oráculo F* terminal conforme a su contrato; V_cont_truth se deriva de A_B1 por intervalos conforme DEC-C10-100/102 y ventana común t0…T*. No son sustitutos entre sí. Value general no se genera ni estima hasta que PA lo instancie; queda NOT_INSTANTIATED.
7. **Vías no focales:** cada mundo declara si B/Z tiene efectos directos sobre O/V, efectos sobre rutas alternativas, recursos, costes u otros mediadores, y las interacciones. La ausencia de esas vías solo puede estipularse en el mundo focal limpio con invariantes explícitos; no se presume globalmente.

Los argumentos U_* pueden compartir componentes o depender entre sí. Toda independencia, monotonicidad, exclusión, mediación serial, positividad y ausencia de interferencia es una propiedad del mundo que debe declararse y probarse, nunca un default del generador. La especificación final debe indicar para cada función dominio/codominio, orden temporal, estados 1/0/?, versión, argumentos activos, soporte y procedencia.

### 16.208.4. Verdad causal que conserva cada mundo

Cada mundo contiene potenciales coherentes para todas las etapas bajo las asignaciones/régimen pertinentes y una ficha de verdad que declara: (1) población/unidad y unidad de asignación; (2) intervención concreta y versiones; (3) historia basal y soporte factible; (4) potenciales por etapa, no solo resultado terminal; (5) cambios verdaderos en A_f*, D_f*, ΔT_acc*, Reach y trayectoria; (6) contribuciones necesarias, habilitadoras o modificadoras, incluidas redundancia, antagonismo y compensación cuando proceda; (7) efectos directos, colaterales e interacciones; (8) O-CONF_truth y V_cont_truth separados, Value solo si PA lo define; (9) estimandos identificados por construcción, los que requieren supuestos y los no identificables; y (10) causa de cualquier bounds, censura o abstención esperada.

La ficha no entrega esos potenciales al Analyzer. Evaluator conserva la verdad y calcula los contrastes verdaderos únicamente después del sellado del análisis.

### 16.208.5. Canal de observación y separación de roles

La observación es una segunda función, condicionada a truth pero no idéntica a ella. Para cada bloque j, Generator produce E_j mediante un mecanismo M_j(T_j*,version,arm,time,U_obs,j), con parámetros y dependencias declarados. El contrato registra sensibilidad/falsos negativos, especificidad/falsos positivos, cobertura, pérdida, lag, error de clasificación, validez, invariancia y missingness según el tipo de variable. No se supone que señales S3 sean independientes ni que el canal sea igual entre brazos/versiones.

- **Generator:** crea mundo, funciones, potenciales, truth, evidencia observada y metadatos reproducibles; separa internamente truth_dgp de observed_evidence.
- **Analyzer:** recibe solo asignación y observed_evidence permitidas; no recibe U_i, parámetros ocultos, potenciales, etiquetas de escenario que revelen la verdad, oráculo F* ni claves de desenmascaramiento. Produce estimandos, supuestos, diagnósticos, bounds y estados de identificación por resultado.
- **Evaluator:** tras sellado inmutable de Analyzer, abre truth_dgp, calcula estimandos verdaderos, compara recuperación y clasifica errores/abstenciones. No modifica la salida del Analyzer ni retroalimenta truth antes del sellado.

Si el Analyzer necesita un dato que el canal no identifica, su salida correcta es bounds/abstención/NOT_IDENTIFIED, no reconstrucción por intuición. La evaluación separa error de reconstrucción, error de estimación, error de clasificación de identificación y filtración de truth.

### 16.208.6. Correspondencia mundo–estimando–criterio

- **ITT-D2:** efecto total de asignación al paquete por cada resultado definido; no equivale a efecto focal.
- **Primeras etapas:** contrastes separados de W_attempt, receipt, S_install, C_dep*, A_f*, D_f* y ΔT_acc*.
- **g_A:** contraste entre intervenciones estocásticas sobre distribuciones factibles del ΔT_acc* completo bajo q_X* y régimen no focal común; no se deriva del ITT-D2 y requiere mapping/soporte.
- **C4:** efecto indirecto interventional sobre cambio estructural completo; requiere identificación longitudinal y control de confusión post-Z; nunca ITT menos efecto mediado.
- **LATE:** solo si se sostienen relevancia, independencia, exclusión, monotonicidad, consistencia/versiones y no interferencia; si no, no Wald.
- **O-CONF y V_cont:** evaluados por separado. La selección de V_cont no completa su validez de medición ni la discriminación frente a O-CONF.
- **Value general:** bloqueado por PA; no reemplazar por O-CONF ni V_cont.

El criterio de éxito metodológico no es que Analyzer siempre produzca un número. Es que recupere el estimando cuando la identificación está construida y las condiciones se cumplen, y que clasifique correctamente bounds, debilidad, no-identificación o no-instanciación cuando no se cumplen. Métricas y tolerancias cuantitativas permanecen abiertas a la fase normativa posterior.

### 16.208.7. Trazabilidad y brechas de cierre

| Elemento | Fuente rectora existente | Estado tras esta integración documental |
|---|---|---|
| Topología S0/S1/S2/SF; F1/F2/A1/A2; R0–R3 | Inventario finito §2–8; plan §§16.207.1–.2 | CANDIDATE_REUSED; frontera/G/H y exhaustividad abiertas |
| Clases de mecanismos adversariales | PD §4; plan §16.188.4 | ROSTER_INTEGRATED; combinaciones finales y cobertura demostrada abiertas |
| Funciones/potenciales y exógenas comunes | DGP temporal/roles §§2–4; plan §§16.199–.200 | CONTRACT_RECONCILED; funciones concretas, dependencias y soporte abiertos |
| Truth/observed/evaluation | PD §2; DGP temporal/roles §6; plan §16.207.5 | ROLE_SEPARATION_DEFINED; firewall efectivo y schemas abiertos |
| A_f*/D_f*/ΔT_acc* | Plan §16.201; crosswalk D2; inventario finito §6–9 | LOGIC_DEFINED_CANDIDATE; atomización/mapping material abiertos |
| Reach y alternativas | Inventario finito §3–8; contrato Reach | TOPOLOGY_CANDIDATE; F*, catálogo completo y cobertura semántica abiertos |
| O-CONF | Plan §16.184; matriz F* §22; DEC-C10-083…088 | PARTIAL / NOT_VERIFIABLE |
| V_cont | DEC-C10-099…102; plan §§16.182, 16.189–.198 | AGGREGATION_RULE_DEFINED; K, ventana numérica, S3 calibration y discriminación abiertos |
| Value general | PA / DEC-C10-095, 099 | NOT_INSTANTIATED; bloqueado |
| Unidad, clúster, q_X*, soporte e interferencia | D2 population/support; plan §16.200 | OPEN |
| Parámetros, distribuciones, dependencias, sensibilidad | PD; P177–P183; plan §§16.198–.200 | OPEN; no valores ni calibración |
| Criterios normativos MDE/α/potencia/precisión/error | P177/P178/P182/P183 | OPEN; no dimensionamiento |

La pregunta «¿está definido el universo finito y sus mecanismos generadores?» recibe dos respuestas: **sí**, existe una arquitectura finita candidata y queda integrada como roster de clases de mundo y contrato generador; **no**, no existe todavía un universo confirmatorio cerrado ni un DGP cuantitativo implementable. No se puede declarar completado el gate B de §16.188.6 mientras unidad/asignación, q_X*, soporte, funciones, dependencias e interferencia sigan abiertos.

### 16.208.8. Secuencia restante única

1. Adjudicar el núcleo basal y la unidad: UE/UA/clúster, q_X*, C_c, C_auth,base y soporte; distinguir estipulaciones del núcleo limpio de mundos de estrés.
2. Completar mapping finito: frontera, G/H, catálogo F*/alternativas, rutas y snapshots; resolver qué combinaciones R0–R3 son exhaustivas y comparables.
3. Cerrar funciones estructurales: intento→recepción→instalación→C_dep*; predicados A_f*; diff ΔT_acc*; Reach/Π; trayectorias y resultados, con potenciales coherentes y exógenas compartidas.
4. Cerrar observación y evaluación: mecanismo por bloque, errores/dependencias/cobertura/ausencia, firewall Generator–Analyzer–Evaluator y métricas/tolerancias normativas.
5. Congelar el roster dirigido: verificar cobertura de cada contraste/falsador de §16.188.4 y PD §4 sin factorial completo; registrar exclusiones justificadas.
6. Solo después: diseño cuantitativo, parámetros, N/R, calibración y gates de implementación/ejecución conforme §16.188.6.

No se reabre D2 primario candidato/D1 secundario ni DEC-C10-066/067, 099–102. No se generan mundos/datos, no se programa ni ejecuta, no se ejecutan validadores, no se calcula potencia ni se declara Design Freeze. scientific_execution=false; execution_authorized=false.

**Dictamen:** FINITE_WORLD_ROSTER_AND_GENERATOR_CONTRACT_INTEGRATED_CANDIDATE / QUANTITATIVE_DGP_NOT_CLOSED / DESIGN_FREEZE_NOT_READY / NO_IMPLEMENTATION / NO_EXECUTION.


## 16.209. Adjudicación integrada del núcleo basal, unidad experimental y soporte D2 (2026-11-12)

**Estado:** reconciliación de arquitectura y contrato candidato; no aprobación de parámetros, no materialización, no Design Freeze. Precedencia: DEC-C10-066/067, DEC-C10S-C1-POPULATION-PRECEDENCE-001, crosswalk C1.3 §§6–10, reconciliación D2 asignación/población/soporte §§3–10, contrato DGP §§26, 57 y 59, y reconciliación PB material/isolation. Este apartado consolida decisiones ya existentes y precisa el diseño sintético; no crea otra secuencia C1 ni otro inventario.

### 16.209.1. Núcleo basal: lo fijado y lo que no debe reabrirse

| Elemento | Adjudicación para el DGP C10-S | Estado |
|---|---|---|
| Población objetivo C1 | P*_{τ2} primaria candidata; P*_F secundaria para apertura funcional exclusiva | PRECEDENCIA ACCEPTED; composición OPEN |
| Autorización normativa basal | C_auth,base=1 común, pre-Z e invariante bajo D2; corresponde a AUTH_f* y no es un segundo factor | ACCEPTED DESIGN CONDITION; no reabrir |
| Dependencia técnica basal | C_dep,0=0 como condición separada de P*_{τ2}; no implica por sí sola A_f,0*=0 | REQUIREMENT DEFINED; truth por unidad OPEN |
| Accesibilidad focal basal | A_f,0*=0, adjudicada con la conjunción completa ID/REL/COND/AUTH/RES/DEP/¬BLOCK | REQUIREMENT DEFINED; truth/mapping por unidad OPEN |
| Aplicabilidad | App*(τ2,S0) es distinta de accesibilidad y de ruta realizable | CANDIDATE COMPONENT OF E_i; NOT ACCEPTED |
| E_scope | Gate de alcance/validez del universo DGP; no filtro adicional dentro del universo si todas las unidades se generan dentro de alcance | INTERPRETATION RECONCILED; roster/IAM OPEN |
| Alternativas basales | F_alt,0 solo determina pertenencia a P*_F; no excluye de P*_{τ2} | ACCEPTED PRECEDENCE |
| Need_preZ / E_req_preZ | Necesidad B1 y admisión de petición, respectivamente; no son elegibilidad experimental | SEPARATION REQUIRED |
| C_other | No se recupera ni se introduce como comodín | SUPERSEDED / EXCLUDED |

La composición E_i=E_scope,i ∧ App*(τ2,S0_i) continúa siendo propuesta no aceptada. En mundos sintéticos cuya frontera se define íntegramente dentro del dominio, E_scope=1 puede fijarse por construcción como condición del marco, pero esto no ratifica la composición universal de E_i ni autoriza a clasificar unidades reales. App debe permanecer explícita y separada de A_f*. La población objetivo sigue siendo la definición aceptada P*_{τ2}={i:E_i=1,C_dep,i0=0,A_f,i0*=0} hasta que se resuelva formalmente E_i.

**Regla basal que evita una falsa equivalencia:** en cada mundo se debe declarar qué predicado o mecanismo hace verdadera la inaccesibilidad focal basal. No se deduce A_f,0*=0 de C_dep,0=0; tampoco se deduce desde ausencia de evidencia, Need_preZ, fallo de instalación o ausencia de ruta observada. En el mundo focal limpio puede estipularse ruta técnica única y predicados no técnicos invariantes, de modo que DEP_f,0*=0 explique la inaccesibilidad; esa estipulación no se transporta a R1/R2 ni a los mundos adversariales.

### 16.209.2. q_X*: definición funcional sin inventar distribución

Se conserva q_X* como distribución conjunta objetivo de la historia basal pre-Z dentro de P*_{τ2}, no como probabilidad de asignación ni como intervención mediadora:

q_X* = Law(X,H0,C_c | i ∈ P*_{τ2}).

- X,H0 son el núcleo candidato de historia basal.
- C_c es el vector de condiciones basales no focales que el DGP necesita para definir factibilidad, heterogeneidad, soporte y potenciales. Cada campo se incorpora una sola vez, con ID, tiempo, versión y papel causal/medición declarado; no se agregan comodines ni duplicidades.
- C_auth,base=1 se trata como condición de diseño común fijada, no como variable aleatoria que se muestrea en q_X*. AUTH_f* sigue siendo término de A_f* y toma el valor común estipulado en el DGP aislado. Si un mundo adversarial cambia autorización, debe identificarse expresamente como intervención/violación de invariancia, no como variación inadvertida de q_X*.
- Recursos, capacidad, información, dominio y otras condiciones pueden aparecer en la historia basal si son necesarias; su representación en q_X* no crea predicados adicionales ni permite doble contabilización entre E_i, C_dep, A_f*, C_c y vías colaterales.
- F_alt,0 se conserva para definir P*_F y heterogeneidad; no condiciona q_X* de la población primaria P*_{τ2}, salvo que un estimando secundario se defina expresamente en P*_F.
- Variables post-Z, incluida L_m inducida por Z, no entran en q_X*. q_L* solo se introduce para C4 si la estrategia longitudinal lo exige.

La expresión anterior define el objeto estadístico, no su distribución empírica/sintética material. Siguen OPEN su soporte, masa, dependencias, pesos, estratos y cobertura. No se asignan valores ni distribuciones paramétricas en este paso.

### 16.209.3. Unidad y asignación: regla para mundos limpios y adversariales

Se fija la siguiente arquitectura de unidades, compatible con UE/UA/UO:

1. **UE:** instancia sintética completa, con identidad y versión propias.
2. **UA:** entidad a la que el mecanismo asigna Z; se declara por mundo, no se infiere de B1.
3. **UO:** observaciones repetidas de una UE a través de t−1…t9; no son unidades independientes ni incrementan N.
4. **Mundo focal limpio/aislado:** candidato de diseño UA=UE, asignación individual a nivel de instancia, con no-interferencia estipulada por construcción: sin recursos, agentes, estado, información, infraestructura, canales compartidos ni carryover entre UE. Esta estipulación pertenece a la verdad del mundo sintético y debe ser comprobable por Generator/Evaluator; no se presenta como evidencia de aislamiento material PB.
5. **Mundos de interferencia:** UA será el clúster o se declarará un mapa de exposición G_i(Z_{-i}) y potenciales Y_i(z_i,g_i). El Analyzer no recibirá supuestos SUTVA por defecto. Si no se especifica clúster/mapa suficiente, el estimando individual será NOT_IDENTIFIED/INDETERMINATE.
6. **Asignación:** el Generator implementará una regla de asignación coherente con UA y estratos pre-Z. Para el contraste ITT-D2, ambos brazos deben tener probabilidad positiva en cada estrato/historia incluida (0 < p_i < 1, o el análogo por clúster). La aleatorización, cuando se use, será independiente de los potenciales según el diseño declarado. Ratio, p_i concretos, algoritmo, semilla, bloques, N y provenance quedan abiertos hasta cerrar roster y soporte.

Esta arquitectura permite probar por separado recuperación bajo aislamiento y abstención/robustez bajo interferencia, sin convertir la unidad observacional en unidad experimental ni imponer factorial completo.

### 16.209.4. Soporte y factibilidad de D2

Para cada historia con masa positiva bajo q_X*, ambas políticas B_g0^D2 y B_g1^D2 deben ser materialmente factibles y el mecanismo de asignación debe permitir ambos brazos en la UA correspondiente. La regla de política ya aceptada es W_programmed(z)=z; no fija W_attempt, recepción, instalación, C_dep*, A_f*, D_f* ni éxito técnico.

Si una historia no admite una de las políticas, no se fuerza una asignación imposible: se restringe ex ante la población/soporte con nuevo estimando justificado o se declara el contraste no identificado para esa región. No se extrapola fuera del soporte común. El cumplimiento, intento de fondo y éxito técnico se mantienen como mecanismos separados; no se introducen tasas históricas ni parámetros P178.

### 16.209.5. Puerta de cierre material y estado de los subproblemas

| Subproblema | Dictamen |
|---|---|
| Precedencia P*_{τ2}/P*_F | CLOSED AT ARCHITECTURE LEVEL; no reabrir |
| C_auth,base / AUTH_f* | CLOSED AS COMMON D2 DESIGN INVARIANT; no reabrir |
| Separación E_i / App / C_dep,0 / A_f,0* / F_alt,0 / Need_preZ | CLOSED SEMANTICALLY; E_i composition remains NOT ACCEPTED |
| q_X* object and role | DEFINED SYMBOLICALLY; distribution/support NOT MATERIALIZED |
| UE/UA/UO semantics | RECONCILED |
| UA=UE in isolated synthetic world | DESIGN CANDIDATE BY CONSTRUCTION; not material PB evidence |
| Cluster/exposure in adversarial worlds | REQUIRED WHEN INTERFERENCE IS PRESENT; concrete map OPEN |
| Randomization and positivity | REQUIREMENTS DEFINED; probabilities/algorithm/seed/strata/N OPEN |
| Baseline truth/evidence and IAM snapshots | NOT MATERIALIZED; no unit-level adjudication |
| D2 common support/factibility | OPEN; no identification claim |

La única operación siguiente dentro de este núcleo no es volver a discutir C_auth, la precedencia poblacional ni la semántica UE/UA/UO. Es completar el crosswalk lógico de E_i/App/C_dep,0/A_f,0* con el IAM/C_SRC sintético por unidad y después declarar el soporte de q_X* por mundo. Si el roster/IAM no existe todavía, el resultado válido es una matriz de campos y estados pendientes, no datos ficticios ni un supuesto de cobertura.

No se captura ni sella IAM real, no se crean schemas físicos ni fixtures, no se generan mundos/datos, no se programa, simula, estima ni ejecuta. No se eligen N, ratio, α, potencia, R, pesos, probabilidades o parámetros. scientific_execution=false; execution_authorized=false.

**Dictamen:** BASELINE_AND_UNIT_ARCHITECTURE_RECONCILED / C_AUTH_INVARIANT_REUSED / Q_X_SYMBOLIC_ONLY / UE_UA_CONDITIONAL_DESIGN_SPECIFIED / SUPPORT_AND_E_I_MATERIALIZATION_OPEN / NOT_DESIGN_FROZEN / NO_IMPLEMENTATION / NO_EXECUTION.

## 16.210. Crosswalk basal sintético por UE y soporte simbólico por mundo (2026-11-12)

**Precedencia:** §16.206 (DGP abstracto), §16.207–16.209, contratos DGP temporal/roles, D2 assignment/population/support, PB-MAT y U_G. Esta sección ejecuta la siguiente operación ya prescrita en §16.209.5; no abre otro paquete ni crea un inventario paralelo.

### 16.210.1. Frontera del crosswalk

El crosswalk es un contrato lógico para que Generator instancie verdad basal y evidencia sintética por UE. **No es IAM/C_SRC real, no representa una migración real y no requiere fuentes, sistemas, ACL, snapshots ni infraestructura externos.** Se reutilizan los tipos lógicos NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y las referencias/provenance sintéticas ya definidas en U_G y PE. No se crean familias nuevas de objetos.

Cada registro sintético se vincula, como mínimo, a world_id/version, UE_id/version, predicate_id o transformation_id, timepoint, boundary/version y source_class sintética. La verdad generada y la evidencia observada tienen identidades y almacenes separados; el Analyzer solo recibe la segunda y los campos de asignación permitidos. El Evaluator conserva la primera y adjudica después del sellado.

### 16.210.2. Crosswalk basal

| Elemento | Truth que genera Generator por UE | Representación/evidencia sintética admisible | Regla de adjudicación y límite |
|---|---|---|---|
| E_i | Estado pre-Z de pertenencia al marco/población del mundo, con regla versionada propia del escenario | Registro PREDICATE/CLAIM sintético, con cobertura, provenance y tiempo pre-Z | No se deriva universalmente de E_scope∧App. Esa composición continúa NO ACEPTADA. En el mundo limpio puede fijarse E_i=1 por construcción; esto es una estipulación local del mundo, no una definición universal |
| E_scope | Pertenencia al dominio abstracto estipulado para ese mundo | Metadato de configuración del mundo, no una fuente material | Puede fijarse 1 por construcción cuando Generator solo crea unidades dentro de la frontera. No añade un filtro individual ni ratifica la fórmula de E_i |
| App*(τ2,S0) | Aplicabilidad de τ2 desde S0, independiente de accesibilidad y de E_i | PREDICATE sintético enlazado a S0, τ2 y versión | Se genera explícitamente como 1/0/?; no se infiere de C_dep, A_f, Reach ni de la asignación |
| C_dep,0* | Estado técnico basal de la dependencia focal, con componentes y regla conjunta versionados | NODE/EDGE/ROUTE y SNAPSHOT sintéticos pre-Z; evidencia por componente y cobertura | Se adjudica por su contrato propio. C_dep,0*=0 no implica A_f,0*=0 ni DEP_f,0*=0 |
| ID_f,0 / REL_f,0 / COND_f,0 | Verdad basal de identidad, relaciones necesarias y condiciones constitutivas | PREDICATE y EDGE sintéticos con referencias exactas a objeto, relación, condición y versión | Cada predicado se adjudica por separado en 1/0/?; REL y DEP no se fusionan |
| AUTH_f,0 | Autorización normativa basal | PREDICATE sintético con scope/holder/validity estipulados en el mundo | En el núcleo D2 limpio vale 1 por DEC-C10-067; no se introduce como factor aleatorio ni se confunde con ACL técnica |
| RES_f,0 / DEP_f,0 / BLOCK_f,0 | Disponibilidad ex ante de recursos, existencia de ruta técnica completa y bloqueo efectivo | NODE/EDGE/ROUTE/PREDICATE y snapshots sintéticos | RES no es consumo/capacidad provisionada; DEP=1 si existe al menos una ruta válida; DEP=0 exige inventario exhaustivo; BLOCK=1 requiere bloqueo efectivo de todas las rutas admisibles |
| A_f,0* | Resultado de la conjunción completa ID∧REL∧COND∧AUTH∧RES∧DEP∧¬BLOCK | Salida derivada del Generator, no una etiqueta observada autónoma | 1 solo si todos los términos son 1; 0 si algún término requerido es 0; ? si no hay 0 concluyente y queda algún ? |
| P*_{τ2} | Pertenencia según la definición de población vigente: E_i=1, C_dep,0*=0 y A_f,0*=0 | Cohorte truth reservada y su proyección observada, si el mundo incluye error de clasificación | No condicionar por variables post-Z. Los casos ? no se recodifican como 0 ni se excluyen silenciosamente; el mundo debe declarar cómo trata la indeterminación pre-Z |
| F_alt,0* | Disponibilidad basal de alternativa | ROUTE/EDGE/PREDICATE sintéticos para A1→A2 u otras alternativas declaradas | Define la subpoblación secundaria P*_F cuando corresponda; no excluye por sí sola de P*_{τ2} |

### 16.210.3. Estipulaciones del mundo limpio y mundos adversariales

Para el mundo focal limpio aislado, el Generator puede estipular explícitamente, por construcción y antes de Z: E_scope=1, E_i=1, App*(τ2,S0)=1, C_dep,0*=0 y A_f,0*=0. La última condición debe resultar de la conjunción completa; por ejemplo, DEP_f,0*=0 con el resto de predicados constitutivos en 1. C_dep,0*=0 y DEP_f,0*=0 se registran como verdades separadas, aunque el mundo pueda hacerlas coincidir. No se permite inferir una de la otra.

En los mundos R1/R2/R3 y PD adversariales, E_i, App, C_dep,0*, predicados de A_f,0* y F_alt,0* se generan conforme al mecanismo específico que el mundo pretende probar. No se transportan las estipulaciones del mundo limpio. La truth de elegibilidad y la evidencia observada de elegibilidad se conservan separadas; un mundo con error de clasificación debe permitir que difieran sin alterar retrospectivamente la asignación.

### 16.210.4. q_X* y soporte común por mundo

Para cada mundo w se declara un conjunto finito simbólico de historias basales admisibles H_w dentro de P*_{τ2,w}, con q_{X,w}*(h)>0 para cada historia que se incluya en su soporte. Cada h conserva X, H0 y los componentes pertinentes de C_c, sin duplicidad y con tiempo/versión/papel causal declarados. Esta definición fija el objeto y la regla de soporte; **no asigna valores, pesos, probabilidades ni una distribución paramétrica**.

Por cada h del soporte declarado, el contrato del mundo debe indicar separadamente:

- factibilidad de B_g0^D2 y B_g1^D2;
- positividad del mecanismo de asignación en la UA correspondiente para ambos brazos;
- unidad UA (UE en el mundo aislado; clúster/mapa de exposición en mundos con interferencia);
- invariantes y vías no focales activas;
- estimandos habilitados y supuestos que los identifican.

Si una política no es factible, la historia no se fuerza dentro del contraste común: se restringe ex ante con estimando explícito o se informa falta de soporte/no-identificación. Si la unidad/exposición no está definida, no se invoca SUTVA ni se calcula un ITT individual como si las unidades fueran independientes. Las masas, pesos, probabilidades de asignación, algoritmo, semilla, estratos y N quedan como configuración pendiente de la fase cuantitativa; no se importan cifras de P178.

### 16.210.5. Reglas de observación, asignación y evaluación

1. Generator conoce y conserva E_i, App, C_dep,0*, predicados basales, pertenencia truth a P*_{τ2}, H_w y potenciales.
2. El mecanismo de asignación del mundo se aplica a la UA declarada y se registra con su probabilidad y provenance. La elegibilidad usada para formar la población experimental se fija pre-Z conforme al mecanismo explícito del mundo; no se reconstruye desde variables post-Z.
3. Analyzer recibe Z y la evidencia sintética permitida, incluida su cobertura/error/missingness. No recibe truth, potenciales, parámetros ocultos, semillas secretas ni etiquetas que revelen la clase causal.
4. Evaluator abre truth tras el sellado del Analyzer y compara por separado clasificación basal, ITT de paquete, primeras etapas, atribución focal, soporte y abstención.
5. UNKNOWN, evidencia ausente, cobertura parcial o mapping ambiguo permanecen ?. No se transforman en 0, no se imputan por conveniencia y no se ocultan en el denominador.

### 16.210.6. Estado de cierre del gate

| Componente | Estado tras este crosswalk |
|---|---|
| Separación E_i / E_scope / App | CLOSED AT LOGICAL CONTRACT LEVEL; fórmula universal E_i=E_scope∧App NOT ACCEPTED |
| C_dep,0* frente a DEP_f,0* y A_f,0* | CLOSED AS DISTINCT CONSTRUCTS; truth por mundo se estipula explícitamente |
| Predicados basales y conjunción A_f,0* | LOGIC CLOSED; mapping sintético tipado definido; escenarios aún no instanciados |
| Cohorte truth P*_{τ2} | DEFINITION REUSED; pertenencia generada por mundo, no materializada como datos |
| q_X* | FINITE SUPPORT CONTRACT DEFINED SYMBOLICALLY; masses/weights OPEN |
| Soporte D2 | CONDITIONS DEFINED; factibilidad/positividad por historia aún requieren configuración por mundo |
| Asignación UE/UA/interferencia | RULE RECONCILED; probabilidades/algoritmo/semillas y mapas concretos OPEN |
| Evidencia/roles | LOGICAL FIREWALL CONTRACT REUSED; seguridad técnica efectiva y schemas físicos OPEN |

**Gate result:** BASELINE_SYNTHETIC_CROSSWALK_LOGICALLY_CLOSED / Q_X_SUPPORT_CONTRACT_DEFINED_SYMBOLICALLY / WORLD_CONFIGURATION_AND_FINITE_MAPPING_OPEN / NO_REAL_MIGRATION / NO_DATA_GENERATED / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.

La operación siguiente se limita a completar el mapping finito ya previsto en §16.208.8: frontera, G/H, catálogo F*/alternativas, rutas y snapshots por clase de mundo, demostrando qué contraste/falsador cubre cada clase. No se amplía el factorial, no se generan unidades/datos, no se eligen parámetros numéricos y no se ejecutan pruebas científicas.

## 16.211. Mapping finito de frontera, rutas, snapshots y falsadores por mundo (2026-11-12)

**Precedencia:** §16.206–16.210; inventario finito §2–14; cuatro cards sintéticas AB-03/04 §12; contratos de frontera/granularidad, identidad/versionado, snapshots/diff, Reach y U_G. Este mapping integra lo ya definido; no ratifica propuestas abiertas ni crea escenarios, IDs de test o familias de artefactos nuevas.

### 16.211.1. Frontera y granularidad del universo

| Dimensión | Mapping reutilizado | Estado y límite |
|---|---|---|
| Unidad lógica | Una instancia sintética de servicio B1 por UE; UE/UA/UO según §16.209.3 | Semántica reconciliada; UA=UE solo en mundos aislados por construcción |
| Perímetro | P0_CONFIG, P1_ENVIRONMENT, DUAL_P0_P1 y NA según DEC-C10-059; P2 es frontera causal transversal | Taxonomía aceptada; objetos exactos por mundo son abstractos y se declaran en su configuración |
| Microdominio | Gramática sintética de configuración declarativa, entorno, adaptador/dependencia y rutas | No es caso real de migración; no hay adquisición de fuentes externas |
| G | Una transformación TID/card como unidad atómica candidata; relaciones de composición se registran aparte | Granularidad lógica propuesta; no congelada globalmente |
| Catálogo | F1/τ2, F2, A1 y A2 con TID/SID sintéticas ya asignadas en las cards AB-03/04 | Identidades semánticas abstractas definidas; RID/EID no asignados ni necesarios en esta fase |
| Rutas | πF=(F1,F2), πA=(A1,A2), ambas de dos pasos y con mismo S0, destino, C0, F* y oráculo | Topología candidata definida; no se añaden pasos artificiales |
| H_path | Profundidad de las dos rutas definidas: 2 transformaciones | Descripción de estas rutas, no freeze del horizonte global |
| H=3 | Candidato histórico del inventario finito | No ratificado; no se impone a las cards ni justifica añadir un tercer paso |
| H_time | Duración, ventanas, caducidad, concurrencia y anclaje temporal | OPEN; no se deduce de t0–t9 ni de H_path |
| Ciclos | Excluidos del fixture base; adversariales solo con regla de visita/terminación | Candidato de diseño; exhaustividad no demostrada |

La frontera causal P2 debe incluir únicamente los elementos sintéticos que representen intervención, condición, dependencia, alternativa, recurso compartido, interacción, interferencia o canal de observación pertinente al mundo. No se crea un inventario productivo ni se presupone que cada clase abstracta tenga equivalente real.

### 16.211.2. Mapping de cards, estados y snapshots

| Etapa lógica | Ruta focal | Ruta alternativa | Snapshot/estado que debe conservarse | Límite |
|---|---|---|---|---|
| Basal pre-Z | S0 común | S0 común | Snapshot estructural basal exacto, versión de instancia/contrato, frontera, G y catálogo | Debe permitir adjudicar E_i, App, C_dep,0*, A_f,0* y F_alt,0* sin usar información post-Z |
| Política/provisión | B intenta provisionar la dependencia focal; no ejecuta F1/F2 | Mismo contexto y destino; B no ejecuta A1/A2 | Snapshot post-política/provisión, separado del basal y previo a la transformación | No inferir accesibilidad desde intento, instalación o C_dep |
| Primer paso | F1: S0→S2 | A1: S0→S1 | Snapshot de salida de F1 o A1 con TID/SID, mapping, campos cubiertos y estado 1/0/? | Éxito local no demuestra F* ni Reach(SF) |
| Segundo paso | F2: S2→SF | A2: S1→SF | Snapshot terminal aplicado/verificado, con versión y correspondencia al mismo criterio F* | No equiparar SF nominal con conformidad funcional |
| Evaluación | F* común por ruta | F* común por ruta | Registro de adjudicación O-CONF por instancia/ruta, independiente de V_cont y Value | F* y oráculo completos siguen abiertos; O-CONF no está validado |

Los nombres S0/S1/S2/SF son estados lógicos, no tiempos t0/t1/t2. El reloj causal t−1/t0…t9 se conserva separado. Los snapshots estructurales S_T* son verdad del DGP; E_T/observed_evidence es un canal distinto. Cada comparación requiere matching exacto de identidad/versiones y compatibilidad de frontera, G, catálogo y mapping; en otro caso el diff afectado es UNKNOWN/DIFF_NOT_COMPARABLE.

### 16.211.3. Matriz finita mundo–mecanismo–contraste–salida

Se reutiliza el roster dirigido de §16.208.2 y los perfiles R0–R3 del inventario. La matriz no es factorial: cada mundo activa solo el mecanismo necesario para el contraste/falsador.

| Clase de mundo | Perfil y rutas relevantes | Contraste/verdad que debe preservar | Salida exigida al Analyzer | Cobertura actual |
|---|---|---|---|---|
| Focal limpio | R0; πF abierta por D2; πA ausente solo si exhaustividad se estipula | Contribución focal conocida bajo régimen común, soporte, mapping y ausencia de vías no focales | ITT-D2; atribución focal solo si todos sus gates se cumplen | Arquitectura candidata; F* y parámetros no cerrados |
| Nulo | R0/R3; primera etapa nula o efecto terminal nulo según el mundo | Nulo específico por estimando, sin forzar nulos en otras etapas/resultados | Recuperar nulo o declarar precisión insuficiente | Mecanismo mapeado; verdad numérica no configurada |
| Fallo por etapas | R3; πF no se abre o falla en una etapa declarada | W_attempt, receipt, S_install y componentes C_dep* con potenciales separados | ITT y primeras etapas separadas; no imputar accesibilidad | Etapas mapeadas; funciones conjuntas abiertas |
| Focal adverso | R0; deterioro de coordenada U/R/C/X, Reach o resultado | Signo adverso conocido por construcción | Recuperar dirección o declarar límites/no-identificación | Clase mapeada; coordenada/función concreta abierta |
| Alternativa basal | R1; πA disponible y estable junto a πF | Apertura focal no implica aumento de Reach ni exclusividad | Distinguir D_f*, Reach y resultado; no inferir exclusividad | Cards y perfil definidos; equivalencia F* no adjudicada |
| Alternativa afectada/colateral | R2; B modifica A1/A2 o dependencia compartida | Vía no focal que invalida exclusión focal salvo separación | Efecto de paquete; abstenerse de atribución focal automática | Mecanismo mapeado; función colateral concreta abierta |
| Vía directa | R0–R3 según soporte; B/Z afecta Outcome/Value fuera de ΔT_acc* | Efecto directo/paquete conocido | ITT de paquete separado de efecto focal/mediación | Clase mapeada; Value general no instanciado |
| Interacción/heterogeneidad | R0–R2; funciones dependen de X/H0/C_c, versión o exposición | Efectos condicionales y composición por historia | Estimandos condicionales; no transportar LATE sin supuestos | Clase mapeada; soporte y funciones abiertas |
| IV adversarial | R0–R3; primera etapa nula/débil, defiers o exclusión/monotonicidad violadas | Supuesto IV deliberadamente incumplido | No usar Wald inválido; bounds/weak-IV/NOT_IDENTIFIED | Falsadores definidos en PD; parámetros y pruebas abiertos |
| Interferencia | Perfil con recursos/estado/canales compartidos | Potenciales dependen de clúster o exposición | UA/clúster o mapa de exposición; si falta, NOT_IDENTIFIED | Regla de unidad definida; mapa por mundo abierto |
| Observación adversarial | Cualquier perfil; error, pérdida, lag, cobertura o sesgo diferencial | Truth invariante bajo degradación del canal | Recuperar si identificable; en otro caso bounds/abstención | Canal lógico definido; calibración y dependencias abiertas |
| Soporte/ausencia/censura | Cualquier perfil; positividad fallida, historia imposible, missingness o censura | Identificación/acotación/no-identificación según soporte y canal | No extrapolar; dictamen por estimando | Reglas definidas; soporte/configuración por mundo abierta |

### 16.211.4. Gate F* / Reach: qué está y qué no está cerrado

1. Las cuatro cards abstractas y las dos composiciones πF/πA están definidas documentalmente; el mismo F* debe aplicarse a ambas rutas desde la misma entrada y contexto.
2. FP-01…FP-07 se plantean como criterios no compensatorios de conformidad de ruta; FP-08 es un gate probatorio/provenance separado. No se han cerrado todavía los predicados atómicos obligatorios, mapping M/M_A, tolerancias, reglas de equivalencia, oráculo ni cobertura funcional.
3. SF es un marcador de estado objetivo, no una prueba de F*. Una ruta alcanza funcionalmente SF solo si todos los pasos son admisibles y el criterio común F* queda adjudicado.
4. O-CONF es el resultado terminal adjudicado por instancia/ruta; V_cont mide continuidad funcional B1 por intervalos. No son duplicados ni sustitutos. La ficha/oráculo O-CONF y su discriminación validada frente a V_cont siguen pendientes.
5. Reach_H*=1 requiere al menos una ruta completa verdadera; Reach_H*=0 requiere universo exhaustivo y todas las rutas refutadas; en otro caso ?. La existencia de πA o su ausencia no se infiere de los perfiles R0/R1 sin estipulación y cobertura del universo del mundo.
6. La verdad de Generator, la evidencia observada de Analyzer y la adjudicación de Evaluator se mantienen separadas en todos los pasos/snapshots.

### 16.211.5. Resultado y límite del mapping

**Cerrado a nivel de mapping lógico:** correspondencia de frontera/clases, G candidato, cuatro cards sintéticas, rutas focal/alternativa, estados, roles de snapshots y roster dirigido de mecanismos frente a contrastes y salidas esperadas.

**No cerrado:** frontera exacta por mundo, ratificación de G/H, H_time, exhaustividad semántica de alternativas, F*, mapping M/M_A, tolerancias, oráculo O-CONF, snapshots/fixtures materializados, cobertura efectiva del canal y parámetros/soporte. Por tanto, el mapping no demuestra todavía que todos los falsadores estén cubiertos ni habilita un DGP cuantitativo ejecutable.

**Dictamen:** FINITE_WORLD_TOPOLOGY_AND_FALSIFIER_MAPPING_RECONCILED_CANDIDATE / F_STAR_AND_REACH_ORACLE_OPEN / H_TIME_OPEN / COVERAGE_NOT_VERIFIED / NOT_DESIGN_FROZEN / NO_DATA / NO_IMPLEMENTATION / NO_EXECUTION.

La siguiente operación del mismo cierre integrado es reconciliar las funciones generadoras por bloque causal y sus dependencias contrafactuales con este mapping, sin asignar distribuciones ni parámetros numéricos. Debe quedar explícito qué función genera cada variable, qué exógenas comparte, qué invariantes preserva y qué ramas directas/colaterales/interferentes activa cada clase de mundo.

## 16.212. Reconciliación de funciones generadoras y dependencias contrafactuales por bloque causal (2026-11-12)

**Tipo:** cierre documental de la siguiente operación de §58, sobre §16.199–16.211 y los contratos DGP A–B–C. No es una nueva familia de mundos ni una parametrización. No genera datos, no estima potenciales y no habilita implementación o ejecución.
**Objetivo:** hacer explícitos, para cada bloque del universo finito, la función generadora, sus entradas y salidas, las exógenas que deben conservarse entre contrafactuales, las invariantes del mundo y las ramas no focales que pueden activarse.

### 16.212.1. Convención contrafactual común

1. Para cada UE (o UA/clúster cuando corresponda) el Generator define una historia basal y un vector de exógenas latentes versionado, U_i. U_i puede descomponerse en componentes por mecanismo (asignación, cumplimiento, recepción, instalación, transformación, trayectoria, resultado y observación), pero su distribución conjunta y sus dependencias no se presuponen independientes.
2. Los potenciales bajo asignaciones, políticas o intervenciones distintas se obtienen aplicando las funciones estructurales declaradas a la misma historia basal y al mismo vector de tipo/exógenas de la unidad, salvo que el escenario declare una intervención sobre el propio mecanismo exógeno. No se vuelve a sortear una unidad latente distinta para cada brazo contrafactual. Esta convención conserva la identidad de la unidad y hace comparables sus potenciales; no identifica por sí sola la cópula ni la distribución de U_i.
3. Las exógenas específicas de un evento pueden ser compartidas entre regímenes o tener componentes régimen-específicos solo si la regla se declara en la configuración. La correlación entre componentes, la independencia y la monotonicidad quedan sin imponer. Una asignación aleatoria usa una exógena U_Z separada e independiente de los potenciales solo cuando el diseño del mundo estipula esa aleatorización; no se presume en mundos observacionales o adversariales.
4. Las funciones son tipadas, versionadas y temporales. Cada salida conserva estado {1,0,?} cuando el contrato es trivalente, identidad/unidad, versión, tiempo y provenance. Un argumento desconocido no se sustituye por cero. Las funciones deterministas por definición (p. ej., W_programmed(z)=z) no se convierten en distribuciones.
5. Se distingue entre (a) potenciales bajo asignación D2, (b) potenciales bajo políticas factibles g_A0/g_A1 para ΔT_acc*, y (c) intervenciones mediadoras longitudinales C4 si el escenario las declara. No se identifica una familia de potenciales con otra ni se obtiene C4 por resta.

### 16.212.2. Tabla integrada de funciones, exógenas, invariantes y potenciales

| Bloque | Función generadora y entradas permitidas | Exógenas/dependencias contrafactuales | Invariantes y salidas |
|---|---|---|---|
| Basal y población | X_i,H0_i,C_c,i,E_i,App_i,C_dep,i0*, predicados A_f,i0*,F_alt,i0* = f_base(U_base,i; regla del mundo) | U_base,i compartida en todos los regímenes de la misma UE; no incorpora variables post-Z. Las dependencias entre campos basales se declaran conjuntamente, no se presumen independientes | P*_{τ2} se determina pre-Z según definición vigente; C_auth,base=1 común en D2 y corresponde a AUTH_f, no es un factor aleatorio adicional. C_dep,0*=0 no implica A_f,0*=0. Need_preZ no filtra la cohorte |
| Asignación | Z_i = f_Z(UA_i,strata_i,π_h,U_Z,i) | U_Z independiente de U potencial solo en los mundos aleatorizados que así lo estipulen; U_Z compartida entre el registro de asignación y su provenance, no se vuelve a sortear por resultado | UA=UE solo en mundo aislado; si hay interferencia, UA/clúster o mapa de exposición. Probabilidades/ratio/semilla permanecen como configuración, no como valores fijados |
| Política/programación | W_prog,i(z)=z para D2; policy_i(z)=f_policy(z,version,history) | U_policy,i puede compartirse con cumplimiento si el mecanismo causal así lo declara; no se infiere cumplimiento de programación | La regla de programación D2 es invariante; D1 y g_A no se sustituyen por D2 |
| Intento/recepción | W_att,i(z)=f_att(W_prog,z,X,H0,version,U_att); Rec_i(z)=f_rec(W_att,policy,version,logistics,environment,U_rec) | U_att/U_rec pueden depender de historia y compartir causas latentes; la dependencia conjunta se declara. Intento de fondo tiene mecanismo explícito | W_att, receipt y programación son variables distintas; potenciales por z preservados. Sin parámetros, tasas ni independencia inventados |
| Instalación y C_dep | S_inst,i(z)=f_inst(Rec,version,environment,U_inst); C_dep,i(z)=I(C_install∧C_integrity∧C_compat∧C_oper) según contratos | U_inst puede compartir causas con recepción y dependencias; vector de cuatro componentes se genera conjuntamente, no por marginales independientes salvo justificación | Instalación no equivale a C_dep; C_dep no equivale a A_f ni ΔT_acc. Fallos parciales y rollback permanecen distintos |
| A_f y D_f | A_f,i(t)=h_f(ID,REL,COND,AUTH,RES,DEP,¬BLOCK; estado/snapshot); D_f,i=I(A_f,i0=0 ∧ A_f,i1=1) | U_access puede compartir causas con provisión, recursos, entorno y dependencias; cualquier vía Z/B→AUTH, RES, capacidad, información o dominio se declara como colateral | Se aplica la lógica trivalente y la conjunción completa. C_auth,base=1 es invariante común en D2 limpio por DEC-C10-067; su cambio en mundo adversarial es desviación explícita, no ruido inadvertido |
| T_acc y ΔT_acc | S_T,i*(t)=f_T(historia, identidad, versión, frontera, U_T); ΔT_acc=Diff_G,M(S_pre,S_post) | U_T puede compartir causas con U_access y recursos; el mismo vector exógeno de unidad se conserva entre potenciales. La función puede generar ΔU,ΔR,ΔC,ΔX correlacionados | Se conservan las cuatro coordenadas; ΔE_T queda fuera. Matching no comparable produce UNKNOWN, no diff cero. A_f/D_f son proyecciones focales, no sustitutos del vector |
| Reach y rutas | (Reach_i,Π_i)=f_reach(T_acc,G,H,preconditions,resources,windows,blocks,alternatives,U_reach) | U_reach puede compartir causas con accesibilidad, alternativas y recursos; rutas focal y alternativa se evalúan bajo la misma historia/contexto, sin transferir estados entre rutas | Reach=0 exige universo exhaustivo; Reach=1 al menos una ruta completa verdadera; resto ?. πF y πA conservan sus dos pasos candidatos; G/H global y H_time no congelados |
| Trayectoria downstream | (K,Consider,Selection,Start,Exec)=f_path(Reach,Π,knowledge,actors,history,U_path) | U_knowledge/U_path pueden compartir causas con X,H0, oportunidad y outcomes; selección puede ser post-Z y no se usa para filtrar ITT | Etapas separadas y potenciales coherentes; ejecución no reconstruye retrospectivamente accesibilidad ni Reach |
| Outcome técnico | O_i(z,g)=f_O(ΔT_acc,Reach,Π,trajectory,D_i,C_i,history,U_O; regla de resultado del escenario) | U_O puede compartir causas con U_path y U_value. D_i/C_i son mecanismos explícitos, no residuales. Las ramas directas/colaterales pueden activarse por mundo | Outcome no es O-CONF ni Value automáticamente. Se declara unidad, dimensión, escala y horizonte; no se infiere causalidad focal por temporalidad |
| Value contextual | V_i(z,g)=f_V(B1,Need_preZ,consecuencia,autoridad/perspectiva,ΔT_acc,Reach,trajectory,O,D_i,C_i,history,U_V; contrato V1 del mundo) | U_V puede compartir causas con U_O y U_path; la dependencia debe declararse. La función y sus argumentos pueden omitir mediadores o añadir vías independientes si el mundo lo define | V1 se especifica como consecuencia contextual no circular, independiente de una definición automática por accesibilidad/éxito técnico. Sin contrato completo, VALUE=NOT_INSTANTIATED; no se inventa escala ni pesos |
| Interferencia | Exposure_i=f_G(Z_-i,shared_resources,network,U_G); Y_i=f_Y(...,Exposure_i) | Exógenas compartidas y asignaciones de vecinos/clúster determinan potenciales; mapa G_i(Z_-i) o unidad cluster debe ser explícito | No SUTVA/ITT individual por defecto. Sin mapa o clúster suficiente, salida NOT_IDENTIFIED/INDETERMINATE |
| Observación | E_i,obs = f_obs(truth_i,coverage,error,lag,missingness,censoring,U_obs) | U_obs puede depender de brazo, estado, versión, resultado o unidad; no se presume MCAR/MAR ni independencia del truth. Su mecanismo no altera truth | Analyzer recibe solo evidencia permitida y Z; Generator/Evaluator conservan truth. Missing/UNKNOWN no se convierte en cero; Evaluator abre truth tras sellado |

Esta tabla concreta y amplía el ledger de §16.200 y el crosswalk de §16.199; no cambia sus objetos ni ratifica las propuestas que permanecen abiertas. La correspondencia basal de C_auth,base se interpreta conforme a DEC-C10-067 y §16.202/16.210, que prevalecen sobre la mención histórica de §16.200.1 que la describía como disputa abierta.

### 16.212.3. Contrafactuales que deben coexistir sin confundirse

| Familia | Intervención/contraste | Potenciales que conserva | Interpretación admisible |
|---|---|---|---|
| D2 paquete | Z=1 frente a Z=0, con W_prog(z)=z | S_i(z), incluyendo todas las etapas y ramas activadas por el paquete | ITT total de asignación a D2; no atribución focal automática |
| Accesibilidad focal/general | g_A1 frente a g_A0 bajo q_X* común y régimen no focal r_common declarado | Y_i(g_A1,r_common) y Y_i(g_A0,r_common), con ΔT_acc completo y soporte factible | θ_A(q_X*;Y) solo para el resultado/versión/población/horizonte definidos y si los gates de soporte/consistencia/medición se cumplen |
| Mediación interventional | intervención secuencial sobre mediador/historia L bajo C4 | Potenciales longitudinales con orden temporal y confusores inducidos por Z explícitos | Efecto interventional solo con estrategia de identificación longitudinal; nunca ITT−θ_A |
| Interferencia | asignación de UA/clúster o exposición G_i(Z_-i) | Y_i(z_i,g_i) o potenciales de clúster declarados | Efecto bajo régimen de exposición definido; sin mapa suficiente, no identificado |
| Observación | mismo truth bajo canales observacionales distintos | Truth invariante y E_obs potencial por canal/brazo/estado | Robustez de medición/Analyzer; no confundir cambio de evidencia con ΔT_acc |

Los potenciales de una misma UE deben respetar consistencia: el valor realizado coincide con el potencial correspondiente al régimen efectivamente asignado/aplicado; los potenciales no observados permanecen en truth_dgp. Los cruces entre familias solo se realizan si el DGP declara una intervención conjunta coherente y sus restricciones de soporte. No se reconstruye un contrafactual mezclando etapas observadas de brazos incompatibles.

### 16.212.4. Matriz de ramas por clase de mundo ya inventariada

| Clase de mundo de §16.211 | Bloques que varían/activan | Invariantes que deben conservarse | Contraste y salida de control |
|---|---|---|---|
| Focal limpio | g_A/ΔT_acc cambia; ramas directas, colaterales e interferencia desactivadas por construcción | q_X común, r_common fijo, C_auth,base=1, unidad aislada, soporte y medición declarados | Recuperar θ_A para V1 si está instanciado; D2 ITT se reporta aparte |
| Nulo | Primera etapa nula o respuesta V1 nula, según la definición exacta del nulo | No alterar otros bloques sin declararlo; distinguir nulo de accesibilidad y nulo de resultado | Analyzer no fabrica efecto; resultado por estimando, con precisión/abstención apropiada |
| Fallo por etapas | Mecanismo de intento, recepción, instalación o componente de C_dep falla | Mantener separados W_prog, W_att, receipt, S_inst, C_dep y A_f | ITT/primeras etapas separadas; nunca imputar ΔT_acc desde el éxito previo |
| Focal adverso | g_A induce cambio adverso en coordenada(s) declarada(s) de ΔT_acc, Reach o V1 | Misma historia basal y potenciales coherentes; no imponer monotonicidad positiva | Recuperar signo o informar límites/no identificación |
| Alternativa basal (R1) | πA está disponible y estable; πF puede abrirse | Misma entrada, destino/contexto y F* común por ruta; alternativas no se excluyen de población primaria | Distinguir apertura focal de Reach/resultado; no inferir exclusividad |
| Alternativa afectada/colateral (R2) | B/Z modifica A1/A2, dependencias, recursos o rutas compartidas | Registrar cambio no focal separado de ΔT_acc focal; mantener verdad de cada ruta | ITT paquete; abstenerse de atribución focal si no se separa |
| Vía directa | D_i(z) afecta Outcome/Value sin pasar por ΔT_acc | Mantener explícito el bloque focal y r_common; no absorber D_i como error | ITT de paquete frente a θ_A; no atribución focal espuria |
| Interacción/heterogeneidad | Funciones dependen de X,H0,C_c, versión, recurso o exposición | Exógenas basales compartidas entre potenciales; soporte condicional explícito | Efectos condicionales/estandarización solo con soporte; no transportar LATE |
| IV adversarial | Primera etapa nula/débil, defiers o exclusión/monotonicidad violadas | La verdad del mundo conserva la violación; no se repara desde el Analyzer | Rechazar Wald inválido; bounds/NOT_IDENTIFIED/INDETERMINATE |
| Interferencia | U_G y exposición/recursos compartidos activos | Identidad de clúster/mapa y potenciales de exposición completos | Inferencia por UA/clúster; sin mapa, abstención |
| Observación adversarial | Error, pérdida, lag, cobertura o sesgo diferencial por Z/estado/versión | Truth estructural idéntica al canal de referencia; canal separado | Recuperación solo si canal identifica; si no, bounds/abstención |
| Soporte/ausencia/censura | Positividad fallida, historia imposible, ausencia estructural o censura | No modificar ex post la cohorte ni imputar masas/valores | Restringir estimando ex ante con justificación o declarar falta de soporte/no identificación |

Esta matriz es un cruce de las clases existentes, no un factorial. Una clase puede combinarse con otra únicamente cuando el roster dirigido ya contempla la combinación y el mecanismo conjunto se declara; no se crean nuevos IDs ni nuevas familias de mundos.

### 16.212.5. Separación de ITT, atribución focal y Value

1. El ITT-D2 es el efecto total de Z sobre cada resultado efectivamente instanciado. Incluye las rutas de política que el mundo active: provisión, accesibilidad, vía directa, colateral, interacción e interferencia según corresponda.
2. θ_A(q_X*;V1) contrasta políticas factibles g_A1/g_A0 sobre ΔT_acc* completo bajo historia basal común y régimen no focal r_common explícito. No se identifica sustituyendo g_A por Z ni interpretando el ITT como mediación.
3. La atribución focal requiere que la intervención sobre accesibilidad esté definida, tenga soporte/consistencia/versiones, medición suficiente y que las vías no focales estén fijadas, separadas o identificadas. Si no, la salida admisible es efecto de paquete, bounds o NOT_IDENTIFIED.
4. Value no se define como función automática de ΔT_acc, Reach, trayectoria, ejecución u Outcome. El DGP debe declarar una consecuencia contextual V1 y su regla antes de generar datos; la función puede contener vías adicionales o interacción si la clase de mundo lo requiere. Si falta perspectiva/autoridad, regla, unidad/escala, baseline u horizonte, el estado es NOT_INSTANTIATED y no se calibra θ_A sobre Value.
5. P178 permanece como benchmark focal ideal no confirmatorio. Su replay no valida estas funciones, la separación causal ni la recuperación de las clases adversariales de §16.211.

### 16.212.6. Gate de suficiencia y decisiones todavía abiertas

| Requisito del contrato | Estado tras esta reconciliación | Qué falta sin bloquear la definición lógica |
|---|---|---|
| Bloques/orden causal y función mínima por variable | RECONCILED SYMBOLICALLY sobre §16.199–16.200 y A–B–C | Dominio/codominio y parámetros concretos de cada configuración de escenario |
| Exógenas compartidas y coherencia contrafactual | RECONCILED AS DESIGN RULE; distribución/cópula no asumida | Elegir acoplamiento/distribución por escenario y justificarlo antes de calibración |
| Invariantes basales D2 | C_auth,base=1 común y AUTH_f correspondiente; W_prog(z)=z; separación de etapas | Desviaciones adversariales deben etiquetarse y versionarse por mundo |
| Ramas directas/colaterales/interacción | ROSTER MAPPED; magnitudes y funciones por escenario OPEN | Especificar activación y función exacta en cada configuración |
| Alternativas/Reach/interferencia | RUTAS Y CLASES MAPEADAS; G/H/F*/O-CONF y mapas concretos OPEN | Exhaustividad, oráculo, horizonte y exposición donde aplique |
| Outcome/Value | CONTRATO GENÉRICO REUTILIZADO; V1 NO INSTANTIATED | Selección explícita de consecuencia, perspectiva/autoridad, regla, unidad/escala, baseline y horizonte |
| Observación y firewall | SEPARACIÓN LÓGICA REUTILIZADA | Modelo de canal, parámetros, calibración y seguridad técnica del firewall |
| Estimandos y abstención | ITT/g_A/C4 separados; salidas de no-identificación preservadas | Factibilidad, soporte, métodos, sensibilidad, precisión y criterios ex ante |

**Resultado del gate:** CAUSAL_GENERATING_FUNCTIONS_AND_COUNTERFACTUAL_DEPENDENCIES_RECONCILED_SYMBOLICALLY / FINITE_WORLD_ROSTER_REUSED / NUMERIC_DISTRIBUTIONS_NOT_ASSIGNED / VALUE_V1_NOT_INSTANTIATED / F_STAR_REACH_ORACLE_AND_H_TIME_OPEN / NO_DATA / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate del paquete integrado:** adjudicar el contrato mínimo de la instancia sintética V1 (consecuencia B1, perspectiva/autoridad, regla no circular, unidad/escala, baseline y horizonte) y verificar que el DGP puede producir efecto positivo, nulo y negativo sin definir Value por accesibilidad. En paralelo, cerrar únicamente las decisiones lógicas imprescindibles de factibilidad/soporte de g_A y r_common; no pasar aún a distribuciones numéricas, potencia ni calibración. La selección V1 no se presume aprobada por esta sección.

## 16.213. Precedencia del resultado sintético B1: V_cont provisional, O-CONF terminal y contrafactuales (2026-11-12)

**Tipo:** corrección de continuidad y reconciliación de precedencia; reutiliza decisiones y contratos existentes. No crea dimensión, indicador, regla de valoración, test ni escenario nuevo.
**Precedencia:** DEC-C10-099/100/101/102; DEC-C10-068; B1 pre-Z §2 y §17; B2–B3 §§5–6 y 16–18; operacionalización Outcome/Value §§3–5 y 16–18; plan §§16.182–16.198 y 16.199–16.212.

### 16.213.1. Corrección obligatoria del siguiente gate

La propuesta de §16.212 de adjudicar una instancia genérica V1 no es el siguiente paso vigente y queda supersedida en ese punto por la precedencia posterior ya aceptada. DEC-C10-099 seleccionó provisionalmente V_cont como dimensión mínima de Value para la extensión sintética B. La selección no equivale a Value materialmente instanciado ni a endpoint confirmado, pero sí impide reabrir la selección como si no existiera. La operación pendiente es cerrar la especificación sintética de V_cont y su integración con el universo finito, no inventar una V1 paralela ni solicitar una nueva elección de dimensión.

### 16.213.2. Contrato de resultado vigente y fronteras

| Objeto | Definición vigente | No equivale a |
|---|---|---|
| B1 / Need_preZ | Beneficiario sintético por UE; objetivo basal pre-Z, adjudicado 1/0/? sin inferencia desde eventos post-Z | UE, servicio, solicitud, admisión o resultado |
| A_B1(i,k) | Truth funcional latente del intervalo: capacidad de admitir solicitudes cuando ENABLED=true (no admitir cuando false) y exponer el PROFILE declarado | Conteo de peticiones, procesamiento, respuesta, éxito técnico o telemetría S3 |
| V_cont_truth | Proporción de intervalos completamente conformes en la ventana común iniciada en t0, con intervalos iguales y regla DEC-C10-102 | Fracción exacta de tiempo en uptime, score de señales S3 o V1 genérica |
| F* / O-CONF | F* es criterio funcional técnico versionado; O-CONF adjudica conformidad terminal de cada ruta tras aplicación/check | Continuidad durante toda la ventana ni Value contextual |
| Outcome / consecuencia B1 | Resultado técnico y cambio de situación del beneficiario, separados de la valoración | V_cont automáticamente, accesibilidad o Value |
| Value | V_cont es la única dimensión mínima provisional seleccionada para esta extensión B; P179 vectorial sigue vigente en el marco general | Valor material validado, preferencia real o índice escalar global |

DEC-C10-100/102 fijan la agregación como proporción de intervalos completamente conformes: cualquier incumplimiento funcional confirmado hace que el intervalo intersectado sea 0; el intervalo solo vale 1 si cumple durante todo él; UNKNOWN se propaga a cotas y no se imputa cero ni se elimina del denominador. No describir V_cont como porcentaje exacto del tiempo disponible. La regla es estricta, sin gracia ni duración mínima de fallo. DEC-C10-101 fija el inicio en t0 e incluye provisión e instalación.

### 16.213.3. Función generadora de V_cont y potenciales

Para cada UE i, régimen z/política g y mundo m, el Generator genera la historia latente de estado funcional efectivo ENABLED_eff(i,z,m,t), PROFILE_eff(i,z,m,t), capacidad de admisión y sus transiciones versionadas. La verdad por intervalo se deriva de esa historia según la regla B1/DEC-C10-102; después se agrega sobre la rejilla común [t0,T*]. La misma historia basal y exógenas compartidas de §16.212 se conservan entre potenciales compatibles. No se vuelve a sortear la unidad por brazo.

El contrato no autoriza a inferir A_B1 desde W_programmed, W_attempt, receipt, S_install, C_dep*, A_f*, ΔT_acc*, Reach, ejecución o una señal individual S3. Estos pueden ser causas, antecedentes o evidencia imperfecta; el estado funcional efectivo es el que determina truth. La ausencia de peticiones no es fallo funcional. Los cambios de ENABLED/PROFILE y las interrupciones de capacidad se fechan en truth; la provisión/instalación entra en la ventana por comenzar en t0.

Los potenciales V_cont_i(z) y V_cont_i(g_A) se conservan separados. ITT-D2 compara V_cont bajo asignación z y contiene todas las vías del paquete. θ_A compara políticas g_A1/g_A0 sobre ΔT_acc* completo bajo q_X* común y r_common explícito; solo es interpretable si la intervención, soporte, medición y régimen están definidos. La verdad de V_cont puede cambiar por vía directa/colateral sin cambio de ΔT_acc*, o permanecer constante pese a cambio estructural. C4 sigue siendo mediación interventional distinta. No se calcula efecto directo por ITT−θ_A.

### 16.213.4. Canal S3, O-CONF y límites de identificación

S3 permanece canal pasivo imperfecto separado de truth; conserva emisión, captura, cobertura, lag, pérdida, validez, error, dependencia y censura por UE×intervalo×componente. No se adopta AND/OR/score ni independencia de señales por defecto. Analyzer recibe solo observación permitida y parámetros de calibración accesibles; truth, potenciales y exógenas reservadas quedan en Generator/Evaluator hasta sellado. Si S3 no identifica la secuencia o agregado, salida bounds o NOT_IDENTIFIED/INDETERMINATE_MEASUREMENT.

O-CONF se adjudica terminalmente por ruta frente a F*, con su propio snapshot, evento y oráculo. La discriminación V_cont/O-CONF exige contrastes cruzados: mismo O-CONF con secuencias V_cont distintas y mismo V_cont con O-CONF distinto, siempre que la definición y el soporte de los mundos lo permitan. La arquitectura de contraste está definida, pero F*, oracle, evento terminal, H, snapshots y validez siguen abiertos; por ello la discriminación continúa CONDITIONAL/NOT_VERIFIABLE. No se fusionan endpoints para cerrar esa brecha.

### 16.213.5. Decisiones temporales abiertas y gate real

Ya están aceptados: inicio t0; inclusión de provisión/instalación; intervalos de igual duración; continuidad estricta dentro de cada intervalo; agregación por proporción de intervalos completamente conformes; unknown→bounds; regla semántica ENABLED/PROFILE; y separación del canal S3. No reabrir ni volver a solicitar estas decisiones.

Siguen abiertos y requieren justificación documental antes de cualquier parametrización: T* y cola de seguimiento según soporte de recuperación; unidad temporal de coordenada; K/Δ y convención de fronteras versionada; soporte de episodios/recuperación; familias y dependencia del proceso de estado funcional; configuración/cadencia/cobertura y modelo conjunto S3; criterio normativo de error/precisión; oráculo y horizonte terminal O-CONF; factibilidad/soporte de g_A y definición de r_common; distribución q_X*. Los valores no se derivan de t0…t9, H, S7, P178 ni de conveniencia.

**Siguiente operación integrada:** completar el ledger finito de estados/eventos funcionales B1 y sus dependencias temporales por mundo (qué puede cambiar ENABLED_eff, PROFILE_eff y capacidad de admisión, cuándo, con qué persistencia/recuperación y qué potenciales afecta), enlazándolo con los perfiles R0–R3 y mecanismos adversariales existentes. En la misma pasada, marcar los parámetros temporales como identidad de contrato, dominio derivable, sensibilidad que requiere soporte o decisión normativa. No abrir otra dimensión Value, no generar episodios/datos, no fijar números ni ejecutar calibración.

**Dictamen:** V_CONT_PROVISIONAL_SELECTION_REUSED / B1_TEMPORAL_TRUTH_AND_AGGREGATION_RECONCILED / O_CONF_TERMINAL_SEPARATE / S3_IMPERFECT_OBSERVATION_FIREWALL_PRESERVED / T_STAR_K_S3_SUPPORT_AND_G_A_OPEN / NO_NUMERIC_PARAMETERS / NO_DATA / NO_IMPLEMENTATION / NO_EXECUTION / NOT_DESIGN_FROZEN.


## 16.214. Cierre documental del universo finito funcional B1 y crosswalk temporal R0–R3 (2026-11-12)

Se completa el siguiente gate ordenado en §16.213.5 mediante la sección 14 de `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md`, persistida en esta misma rama.

**Cierre documental alcanzado:**
- Estado funcional finito por UE×B1×versión×intervalo: ENABLED efectivo; PROFILE efectivo frente al declarado; proceso/módulo; superficie de ingreso; dependencias requeridas; capacidad/recursos funcionalmente suficientes. Estados no adjudicables permanecen `?`; componentes no requeridos no se convierten en requisitos.
- Regla A_B1 completa: admitir cuando ENABLED=true, no admitir cuando ENABLED=false y exponer PROFILE declarado. `ENABLED=false` no es fallo por sí mismo. Cualquier incumplimiento funcional confirmado produce A_B1=0 en los intervalos intersectados; ausencia de solicitud no es fallo.
- Cinco familias exhaustivas de transición al nivel funcional B1: CFG, PROC, INGRESS, DEP y CAP. Provisión, instalación, rollback, reinicio, peticiones y señales S3 quedan clasificados como antecedentes, interacciones discretas u observación, no como truth automática.
- Dependencias temporales: transiciones fechadas y versionadas, recurrencia/recuperación permitidas, truth/event_time separado de rejilla V_cont y reloj S3; episodio activo en T* queda censurado, no recuperado.
- Correspondencia explícita con R0–R3: R1 alternativa basal no modifica B1 por sí sola; R2 solo altera B1 si existe componente funcional compartido y cambia efectivamente; R3 fallo de etapa no equivale automáticamente a fallo funcional; R0 no fuerza efecto.

**Clasificación de lo no cerrado:**
- Reglas aceptadas: t0/inclusión provisión-instalación; intervalos iguales; agregación no ponderada; continuidad estricta sin gracia.
- Derivación estructural cerrada: universo finito de estados/eventos funcionales y cinco familias causales.
- Sensibilidad pendiente: persistencia, recurrencia, duración/fase de episodios y recuperación.
- Decisiones temporales pendientes: t_c,max, τ_follow, T*, unidad, Δ, K y convención exacta de frontera versionada.
- Medición pendiente: mecanismo S3, cadencia, cobertura, lag, pérdida, error, dependencia, δ_det y umbral p*.

**Dictamen:** `B1_FINITE_FUNCTIONAL_STATE_EVENT_UNIVERSE_CLOSED_DOCUMENTARILY / R0_R3_TEMPORAL_CROSSWALK_CLOSED / TEMPORAL_PARAMETER_AND_S3_CALIBRATION_GATES_OPEN`.

Este cierre no declara cerrada la temporalización cuantitativa ni la identificación causal. No crea escenarios, IDs, fixtures, parámetros ni datos; no autoriza implementación, generación, simulación, calibración, estimación o ejecución. `scientific_execution=false`; `execution_authorized=false`; `NOT_DESIGN_FROZEN`; PR #116 permanece Draft; no se modifica main.

## 16.215. Contrato de soporte temporal finito y construcción del horizonte común (2026-11-12)

Se desarrolla el gate temporal siguiente a §16.214 mediante la sección 15 de `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md`.

**Cierre estructural:** cada configuración R0–R3 y modificador adversarial aplicable debe declarar soporte superior finito para inicio tardío, número de recurrencias, duración, recuperación y toda transición causal B1; el soporte de truth se separa del lag/captura S3. `t_c,max(m,z)` es la cota de la última transición causal permitida, incluida recuperación; `t_c,max` global es el máximo sobre brazos y mundos del estimando. `T*=t_c,max+τ_follow`, con cola suficiente para capturar el estado terminal según el modelo S3. Se prohíbe truncar silenciosamente episodios, inferir recuperación desde silencio o usar horizontes distintos por brazo.

**Regla de admisión:** una configuración sin soporte acotado, recurrencia finita declarada o comparabilidad temporal no entra en un contraste puntual finito; se trata como sensibilidad/horizonte distinto, censura/bounds o abstención. La rejilla se elige después del soporte y de la cota de captura: Δ debe representar los eventos admitidos; K=(T*−t0)/Δ debe ser entero y común. Δ no altera truth ni tolera transitorios.

**No cerrado numéricamente:** cotas por familia/mundo, máximo de recurrencias, duración/recuperación, lag/captura S3, τ_follow, unidad, Δ y K. No se derivan de t0…t9, H, S3 cadence ni conveniencia.

**Dictamen:** `FINITE_TEMPORAL_SUPPORT_RULE_CLOSED / COMMON_HORIZON_CONSTRUCTION_DEFINED / NUMERIC_SUPPORT_AND_S3_CALIBRATION_OPEN / DELTA_K_OPEN / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN`.

El siguiente paso es resolver la sensibilidad temporal que el DGP debe cubrir y el dominio de detectabilidad S3 en conjunto; después seleccionar Δ/K. No se asignan cifras ni se ejecuta calibración.

## 16.216. Cierre estructural del contrato de detectabilidad temporal S3 (2026-11-12)

Se completa el gate metodológico de detectabilidad mediante §17 de `C10_S_TEMPORAL_HORIZON_AND_S4R_INTEGRATION_AUDIT_DRAFT_001.md`.

**Cierre:** Generator conserva truth temporal exacta; S3 produce evidencia pasiva imperfecta; Analyzer recibe solo evidencia sellada; Evaluator abre truth después. Los tres modos `SNAPSHOT_METRIC`, `LOG_TRACE_EVENT` y `HYBRID_PASSIVE` quedan definidos como configuraciones comparables, sin seleccionar uno como ganador. Se fijan métricas separadas de sensibilidad de episodio, falsos positivos, localización/lag, cobertura/pérdida, detección de recuperación y error de clasificación por intervalo; estratificación por familia, duración relativa, fase, modo y versión; no se presupone independencia.

`δ_det` queda definido como resumen condicional de la curva de detección, no como mínimo funcional. Solo puede derivarse tras aprobar `p*`, criterio de falsos positivos, cobertura y tolerancia temporal; antes se reportan curvas y bounds. La ausencia de señal no prueba funcionamiento ni recuperación. La verdad estricta DEC-C10-102 no se relaja por limitaciones S3.

Se fija la convención `[b_k,b_{k+1})`: frontera interna asignada al intervalo que comienza allí; T* incluido en el último intervalo. La cadencia S3 y Δ permanecen distintos.

**Abierto:** modo confirmatorio, parámetros y soporte de cada modo, p*, nivel de confianza, falso positivo tolerable, tolerancia temporal, cobertura mínima, soporte de lag, τ_follow, unidad, Δ y K. No hay calibración ni valores aprobados.

**Dictamen:** `S3_DETECTABILITY_EVALUATION_CONTRACT_CLOSED_STRUCTURALLY / CURVE_FIRST / NUMERIC_CALIBRATION_OPEN / DELTA_K_OPEN / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN`.

## 16.217. Comparación emparejada de modos S3 y criterio de recuperación causal (2026-11-12)

Se desarrolla §16.216 mediante §18 de `C10_S_TEMPORAL_HORIZON_AND_S4R_INTEGRATION_AUDIT_DRAFT_001.md`.

**Decisión estructural:** no se selecciona snapshots, logs ni híbrido como ganador a priori. Los tres modos existentes se proyectan como observaciones alternativas sobre las mismas historias truth B1, unidades, mundos, brazos, ventanas y rejillas. Se comparan emparejadamente; no se presume independencia entre modos ni entre componentes híbridos. El Analyzer no recibe etiquetas de truth, mundo, parámetros reservados ni semillas.

**Separación de objetivos:** S3 es exclusivamente medición runtime post-Z de V_cont; no se usa para Need_preZ, cuya observación basal conserva el canal S7 y DEC-C10-097/098.

**Evaluación en tres niveles:** (1) detección/lag/cobertura/error de episodios e intervalos; (2) recuperación/bounds de V_cont frente a truth; (3) recuperación causal por estimando frente a potenciales DGP, incluyendo falsa atribución en nulos/vías directas/colaterales y abstención correcta/incorrecta. No se admite un score agregado que oculte falsas atribuciones; no significación no equivale a equivalencia.

**Regla de calibración:** se cruzan los tres modos con canal calibrado por diseño (parámetros accesibles al Analyzer) y no calibrado/ambiguo (bounds/abstención). El Evaluator conserva truth y parámetros reservados. Cualquier selección/calibración de método debe separarse de la evaluación que pretende validar recuperación.

**Abierto:** p*, nivel de confianza, tolerancias de precisión/error, cobertura inferencial, tasas admisibles de falsa recuperación y abstención excesiva, parámetros/soporte por modo y selección posterior de un modo confirmatorio si fuese necesaria. Hasta entonces solo curvas/distribuciones; no PASS/FAIL confirmatorio.

**Dictamen:** `S3_PAIRED_MODE_COMPARISON_DEFINED / CAUSAL_RECOVERY_AND_ABSTENTION_CRITERIA_DEFINED / NO_A_PRIORI_WINNER / NUMERIC_ACCEPTANCE_THRESHOLDS_OPEN / NO_CALIBRATION / NO_EXECUTION / NOT_DESIGN_FROZEN`.

## 16.218. Regla integrada de suficiencia para recuperación causal y abstención (2026-11-12)

**Objeto:** desarrollar el gate siguiente a §16.217. Define cuándo el harness sintético recupera correctamente una contribución causal conocida, cuándo incurre en falsa atribución y cuándo debe abstenerse. No aprueba todavía umbrales numéricos ni autoriza calibración o ejecución.

### 16.218.1. Unidad de adjudicación y oráculo

La unidad de evaluación no es un único score del experimento. Es cada combinación:

estimando × resultado/dimensión × población × horizonte × escenario/mundo × régimen de observación/calibración.

El Generator conserva los potenciales y la verdad exacta de cada combinación. El Analyzer declara primero el estado de identificación y después, solo si procede, la estimación o los bounds. El Evaluator compara la salida sellada con el oráculo sin retroalimentar truth ni parámetros reservados al Analyzer.

La clasificación de identificación del oráculo se determina por las condiciones del estimando y la información observable autorizada al Analyzer, no por el hecho de que el Generator conozca el efecto verdadero.

### 16.218.2. Separación obligatoria por estimando

| Objeto | Qué debe recuperar | Qué no puede sustituirlo |
|---|---|---|
| ITT_Z^D2 sobre V_cont | Efecto total de asignación D2, incluyendo vías directas, colaterales e interacciones | Efecto focal de accesibilidad, LATE o mediación |
| θ_A(q_X*, r_common; V_cont) | Contraste de políticas factibles g_A sobre el vector completo ΔT_acc*, bajo historia basal y régimen no focal común | ITT_Z^D2, C_dep*, A_f*, D_f* aislados o una coordenada de ΔT_acc* |
| C4 interventional | Efecto mediado bajo intervención longitudinal definida y condiciones de identificación secuencial | ITT−θ_A, ajuste convencional del mediador o residual algebraico |
| LATE_f^D2 | Efecto local solo si relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición son defendibles | Wald automático por existir una primera etapa |
| Primeras etapas C2 | Contrastes separados de asignación sobre C_dep*, A_f*, D_f* y cada coordenada ΔT_acc* | Outcome causal ni prueba suficiente de mediación |

La evaluación se realiza por separado para cada objeto. No se transfiere identificación, precisión, signo ni cobertura entre estimandos, resultados o poblaciones.

### 16.218.3. Regla conjuntiva de recuperación válida

Una salida cuenta como **recuperación válida** únicamente cuando se cumplen conjuntamente:

1. **Identificación correcta:** el estado declarado por Analyzer coincide con el oráculo (IDENTIFIED, PARTIALLY_IDENTIFIED, NOT_IDENTIFIED o INDETERMINATE).
2. **Objeto correcto:** el estimador corresponde al estimando, resultado, población, horizonte y régimen declarados; no cambia de etiqueta ni de escala.
3. **Inferencia calibrada:** cuando el punto está identificado, el intervalo/procedimiento tiene cobertura y error tipo I compatibles con los criterios aprobados, y la precisión/potencia alcanza el objetivo ex ante aplicable.
4. **Magnitud y dirección:** signo, sesgo, RMSE y error se evalúan frente al valor exacto del oráculo en la escala de V_cont; no basta acertar el signo ni que un intervalo contenga el truth por azar en una réplica.
5. **Observación admisible:** la medición S3, cobertura, pérdida, censura, dependencia y calibración permiten el dictamen emitido. El Analyzer no puede usar parámetros reservados ni completar datos por conveniencia.
6. **No falsa atribución:** ITT, efecto focal, LATE y mediación permanecen separados; las vías directas/colaterales no se etiquetan como efecto de accesibilidad.

La recuperación estadística se juzga sobre réplicas independientes y métricas de operación, no por una sola ejecución ni por la coincidencia puntual de una estimación con el oráculo.

### 16.218.4. Falsa recuperación, abstención correcta y abstención excesiva

- **Falsa recuperación:** Analyzer emite una estimación puntual o atribución focal cuando el oráculo es NOT_IDENTIFIED/INDETERMINATE; confunde ITT con θ_A/LATE/C4; ignora falta de soporte, vía directa/colateral no separada, interferencia o error de medición; o presenta como recuperado un efecto cuya precisión/error incumple el criterio aprobado.
- **Abstención correcta:** Analyzer devuelve NOT_IDENTIFIED cuando no hay identificación; INDETERMINATE cuando la evidencia/medición no permite decidir; o PARTIALLY_IDENTIFIED con bounds cuando las restricciones disponibles solo sostienen identificación parcial. Los bounds deben cubrir la verdad DGP bajo el procedimiento y supuestos declarados.
- **Abstención excesiva:** Analyzer no recupera un estimando que el oráculo considera identificado y para el que el canal entrega información/calibración suficiente. Se mide separadamente en el núcleo limpio y en cada escenario identificable.
- **Fallo de clasificación:** una salida puede tener un valor numérico cercano al truth y aun así fallar si su estado de identificación o etiqueta causal es incorrecto.

Cualquier falsa atribución focal en un mundo no identificado se informa como fallo crítico independiente. No puede compensarse con menor RMSE, buena detección S3, potencia o cobertura en otros mundos.

### 16.218.5. Nulo, adversariales y significado de refutar

El roster existente debe contener, sin expansión factorial innecesaria, al menos las clases ya definidas: efecto focal positivo, nulo general, nulo condicionado, adverso/negativo, señal débil, primera etapa nula/débil, vía directa, vía colateral/alternativa, interacción/heterogeneidad, soporte fallido, medición diferencial/degradada, pérdida/censura e interferencia.

- En el nulo, se evalúa control del error tipo I; no rechazar H0 no demuestra equivalencia ni efecto exactamente cero.
- Una afirmación de equivalencia requiere margen de equivalencia justificado y aprobado ex ante; no se inventa.
- En el efecto negativo/adverso, la recuperación debe preservar signo y estimando, no forzar positividad.
- En los mundos directos/colaterales o sin soporte, la salida debe distinguir el ITT de paquete de la atribución focal; cuando esta última no está identificada, no se acepta estimación puntual.
- El experimento puede demostrar que el método recupera una contribución conocida dentro de las condiciones estipuladas, o refutar su suficiencia mostrando falsa atribución, mala cobertura, sesgo, falta de potencia o abstención excesiva. No demuestra por sí mismo el efecto en una migración real ni una afirmación TGCV universal.

### 16.218.6. Métricas no compensatorias y separación calibración/evaluación

El informe conservará, por estimando y celda, al menos: error de identificación; falsa recuperación; abstención correcta/excesiva; sesgo; RMSE; cobertura y anchura de intervalos; error tipo I; potencia/curva de recuperación; cobertura de bounds; error de signo; error de medición y cobertura S3; MCSE de cada métrica.

No se permite un score agregado que oculte falsas atribuciones o abstenciones incorrectas. Se informan curvas y distribuciones por escenario/modo y también el peor comportamiento entre falsadores prioritarios.

Los datos/configuraciones usados para seleccionar o calibrar Analyzer, método, canal o parámetros se separan de las réplicas/configuraciones de evaluación final. La evaluación no puede retroalimentar el ajuste y volver a computarse como PASS sobre los mismos casos.

### 16.218.7. Reutilización de criterios cuantitativos existentes y límites

Los criterios de §39 (α bilateral 0.05, potencia objetivo ≥0.80, cobertura nominal 95% y MCSE objetivo ≤0.005 para tasas) permanecen **propuestas previas**, no decisiones aprobadas en este gate. Su ámbito original es el benchmark focal θ_A de P178; no se transfieren automáticamente a ITT_Z^D2, C4, LATE_f ni al harness integrado. El replay P178 ya cerrado no se repite ni se presenta como validación del Analyzer integrado.

No existe todavía margen de precisión/anchura, MDE/relevancia, equivalencia, tasa admisible de falsa recuperación ni abstención excesiva aprobado para el experimento integrado. La escala V_cont∈[0,1] permite reportar errores y anchuras en escala original, pero no determina por sí sola qué error es científicamente aceptable.

Por tanto, se cierra la **regla lógica y estadística de adjudicación**, no los umbrales numéricos. No se emite PASS/FAIL confirmatorio hasta que los criterios aplicables estén aprobados y calibrados.

### 16.218.8. Auditoría de suficiencia del módulo integrado actual

La revisión estática de vcont_integrated_harness.py confirma que el módulo todavía no implementa este contrato completo:
- su tipo de identificación no incluye PARTIALLY_IDENTIFIED ni una salida de bounds;
- el Evaluator compara errores puntuales y una regla limitada de abstención, pero no evalúa cobertura de bounds, error tipo I, potencia, sesgo/RMSE Monte Carlo ni tasas de falsa recuperación/abstención excesiva por estimando;
- la salida focal y el ITT de paquete están separados, pero el módulo no implementa C4 ni un contrato completo de LATE_f;
- el módulo no es aún el DGP integrado completo de D2, Reach/trayectoria, O-CONF y Value general; V_cont es la instancia escalar seleccionada provisionalmente.

Estas son brechas de implementación contra el contrato, no resultados de una ejecución. La suite de contratos previa no las cierra por el mero hecho de pasar.

### 16.218.9. Dictamen y siguiente operación

**CERRADO DOCUMENTALMENTE:** regla conjuntiva de recuperación; clasificación de falsa recuperación/abstención; evaluación separada por estimando; tratamiento de nulos y adversariales; métricas no compensatorias; separación calibración/evaluación.

**ABIERTO:** aprobación de umbrales cuantitativos de operación; criterios de precisión/MDE/equivalencia y coste de error; extensión del harness a PARTIALLY_IDENTIFIED/bounds y métricas Monte Carlo; implementación y validación integrada.

**Dictamen:** CAUSAL_RECOVERY_SUFFICIENCY_RULE_CLOSED_STRUCTURALLY / NUMERIC_ACCEPTANCE_THRESHOLDS_OPEN / INTEGRATED_HARNESS_GAP_CONFIRMED_STATICALLY / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** consolidar en una sola decisión los criterios cuantitativos para el benchmark integrado, separando lo reutilizable de P178 de lo que requiere justificación adicional. La recomendación deberá proponer un punto de partida para α/cobertura/MCSE y una regla de selección de precisión/potencia sin inventar MDE, además de un límite explícito de falsa atribución y abstención. No iniciar calibración hasta autorización expresa.


## 16.219. Decisión cuantitativa de partida para el benchmark integrado (2026-11-12)

**Estado de decisión:** ACEPTADA por el usuario como propuesta cuantitativa de partida. Esta aceptación fija objetivos de diseño para su operacionalización; no constituye calibración, ejecución, Design Freeze ni evidencia de que el harness actual los satisfaga.

### 16.219.1. Parámetros estadísticos de partida

Se adoptan para el benchmark integrado, sujetos a verificación de adecuación por estimando y procedimiento:

| Parámetro | Decisión de partida | Aplicación |
|---|---:|---|
| Error tipo I | α bilateral = 0,05 | Por estimando confirmatorio y contraste preespecificado; se deberá controlar multiplicidad en la familia confirmatoria |
| Cobertura de intervalos | 95 % nominal | Procedimientos de intervalo para estimandos identificados |
| Potencia | ≥ 0,80 | En cada estimando/escenario identificable para el efecto mínimo relevante que se declare antes de dimensionar |
| Precisión Monte Carlo de tasas | MCSE ≤ 0,005 | Para tasas de error tipo I, cobertura, potencia, falsa recuperación y abstención; justificar el número de réplicas |
| Falsa atribución | ≤ 0,05 | Tasa en cada familia de mundos no identificados/adversariales, con límite superior unilateral de incertidumbre Monte Carlo ≤ 0,05 |
| Abstención excesiva | ≤ 0,05 | Tasa en cada familia de mundos identificables y con observación suficiente, con límite superior unilateral de incertidumbre Monte Carlo ≤ 0,05 |

Los dos últimos límites son umbrales de aceptación de diseño, no tolerancias que permitan ocultar errores críticos: cada falsa atribución focal se registra y audita como evento crítico, se informa por separado y no se compensa con resultados favorables de otras celdas. La regla del límite superior evita aprobar una tasa solo porque su estimación puntual sea inferior al 5% con incertidumbre amplia.

### 16.219.2. Aplicación por estimando y multiplicidad

Los objetivos no se agregan en una única métrica. Se reportan separadamente para ITT-D2, θ_A de accesibilidad y cualquier estimando C4 o LATE_f que llegue a quedar formalmente especificado e identificado. Las primeras etapas C2 se tratan como diagnósticos de mecanismo, no como efectos sobre V_cont.

α=0,05 se aplica a cada contraste confirmatorio conforme a un plan de multiplicidad preespecificado. Antes de calibrar debe fijarse la familia confirmatoria, la jerarquía de hipótesis y el procedimiento de control familiar (por ejemplo, gatekeeping jerárquico o Holm); no se elegirá retrospectivamente el procedimiento que produzca el resultado más favorable. Si no se aprueba una familia, no se presenta una afirmación confirmatoria conjunta.

La cobertura nominal del 95% se evalúa empíricamente sobre réplicas, por estimando y celda identificable, junto con anchura, sesgo y error. La potencia ≥0,80 no se interpreta como permiso para elegir a posteriori el efecto mínimo que el diseño puede detectar.

### 16.219.3. Regla de precisión, relevancia y dimensionamiento sin MDE inventado

No se asigna ahora un MDE numérico. Antes de dimensionar N y R, el protocolo deberá declarar para cada estimando:

1. **δ_min,e:** menor efecto en escala V_cont que tendría relevancia científica para ese estimando, justificado sustantivamente y sin derivarlo de la potencia observada.
2. **w_max,e:** máxima anchura admisible del intervalo (o precisión equivalente) para permitir la decisión prevista, justificada por la resolución científica requerida.
3. **Familia de escenarios:** condiciones identificables y adversariales en las que se exige recuperación, con distribución/ponderación explícita y análisis separado de peores casos.
4. **Pérdida de información:** medición, calibración, censura, falta de soporte, heterogeneidad e interferencia que forman parte del objetivo de evaluación.

Después, seleccionar N y R mediante búsqueda de diseño sobre la cuadrícula preespecificada, eligiendo la menor combinación que cumpla simultáneamente potencia ≥0,80 para δ_min,e, anchura ≤w_max,e, cobertura nominal, MCSE y límites de falsa atribución/abstención en todas las celdas obligatorias. Si no existe combinación factible dentro de recursos declarados, el resultado es INFEASIBLE/REDESIGN, no relajación post hoc de los umbrales.

Para estimandos parcialmente identificados, no se fuerza un punto ni se aplica la regla de anchura de intervalos puntuales: se evalúan cobertura y anchura de bounds frente a la verdad y a la resolución decisional que se apruebe para ellos. Para estimandos no identificados, el criterio es clasificación/abstención correcta, no potencia.

### 16.219.4. Alcance y salvaguardas

- Los parámetros α, cobertura, potencia y MCSE proceden de la propuesta previa P178, pero esta decisión los adopta como objetivos de partida del benchmark integrado; no convierte el replay P178 en validación del harness integrado.
- Los límites de 5% para falsa atribución y abstención excesiva se aceptan como criterios de diseño por familia de escenarios, no como permiso para una tasa de errores críticos no auditada.
- No se aprueba margen de equivalencia, δ_min,e, w_max,e, familia confirmatoria/multiplicidad, distribución de escenarios, N ni R. Deben justificarse y aprobarse antes de calibración.
- Las tasas y su MCSE deben reportarse por estimando y familia; el agregado global nunca puede ocultar una familia que incumple.
- El objetivo de 95% de cobertura se aplica a procedimientos identificados y a bounds con cobertura declarada; no convierte una salida no identificada en identificada.

### 16.219.5. Dictamen y siguiente gate

**DECISIÓN CERRADA COMO BASE DE DISEÑO:** α bilateral 0,05; cobertura nominal 95%; potencia mínima 0,80; MCSE de tasas ≤0,005; falsa atribución ≤0,05 por familia no identificada/adversarial con límite superior unilateral ≤0,05; abstención excesiva ≤0,05 por familia identificable con límite superior unilateral ≤0,05.

**ABIERTO ANTES DE CALIBRACIÓN:** δ_min,e; w_max,e; familia confirmatoria y multiplicidad; definición/ponderación de familias de escenarios; tamaño N y réplicas R; presupuesto computacional; procedimiento exacto de incertidumbre Monte Carlo para límites de tasas; implementación de bounds y métricas en Analyzer/Evaluator.

**Dictamen:** QUANTITATIVE_STARTING_CRITERIA_ACCEPTED / PRECISION_AND_RELEVANCE_MARGINS_OPEN / MULTIPLICITY_PLAN_OPEN / HARNESS_IMPLEMENTATION_GAP_OPEN / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** fijar δ_min,e y w_max,e por estimando, a partir de justificación científica y resolución de decisión, y cerrar la familia confirmatoria/multiplicidad. No dimensionar N/R ni calibrar antes de ello y de la autorización de ejecución correspondiente.


## 16.220. Paquete C — auditoría integrada de justificabilidad de relevancia y precisión por estimando (2026-11-12)

**Objeto:** ejecutar el siguiente tramo del paquete C bajo la regla agrupada de §16.93. Se contrasta la decisión cuantitativa §16.219 con la instancia, el endpoint y la identificación que constan realmente en el expediente. No se asignan δ_min,e ni w_max,e por conveniencia.

### 16.220.1. Resultado de la auditoría de fundamento

La evidencia documental disponible no sostiene todavía un margen sustantivo numérico para ningún estimando del benchmark integrado:

- **V_cont:** DEC-C10-099…102 lo selecciona provisionalmente como dimensión operativa mínima de Value y define una fracción de intervalos conformes B1 en una rejilla común. No están cerrados la rejilla/cadencia, K, duración efectiva de intervalo, calibración basal, ni el punto operativo que permitiría interpretar qué cambio de esa fracción sería material. La escala [0,1] fija límites matemáticos, no relevancia científica.
- **Value contextual:** el crosswalk C-Value y la auditoría de roles §16.140 no encuentran beneficiario, población de valoración, instrumento ni dimensión de Outcome/Value materializados. CMP owner, actor ejecutor y evaluador metodológico no son beneficiarios. Por tanto V_cont no puede presentarse como una medida general ya validada de Value.
- **ITT_Z^D2:** es el efecto total de asignación al paquete D2 sobre V_cont, si diseño, consistencia, interferencia y observación lo permiten. Puede tener un δ_min propio solo después de justificar la consecuencia operativa de cambiar V_cont; no representa por sí mismo el efecto causal de accesibilidad.
- **θ_A / θ_Af:** la correspondencia B_g^D2→g^Af no está demostrada; θ_Af(q_X*) sigue no identificado y θ_A(q) general no queda resuelto por D2. No es metodológicamente admisible fijar un δ_min confirmatorio para una intervención focal cuya versión, población/régimen y estado de identificación aún no están cerrados.
- **C4/IIE_M y LATE_f:** permanecen condicionados a contratos y supuestos de identificación longitudinal/IV. No se fijan márgenes confirmatorios mientras no estén especificados e identificados por resultado.

### 16.220.2. Contrato de definición de márgenes — sin cifras inventadas

Cuando las dependencias anteriores estén resueltas, cada estimando e deberá tener una ficha de margen con:

1. **Objeto y escala:** estimando exacto, resultado/dimensión, población/unidad, horizonte, versiones y régimen común; unidad de medida y rango.
2. **Ancla sustantiva:** consecuencia operacional/contextual que cambiaría una decisión real del dominio sintético, quién recibe el beneficio/coste y qué regla de decisión se altera. Para V_cont, la justificación debe volver a duración y significado de los intervalos B1, no solo a una diferencia abstracta de proporciones.
3. **δ_min,e:** menor diferencia que cambia la decisión sustantiva, argumentada antes de observar resultados y separada del efecto que el diseño tenga potencia para detectar. No se deriva de N, potencia observada, coeficientes diagnósticos P178 ni de maximizar recuperación.
4. **w_max,e:** máxima anchura admisible del intervalo/bounds para la decisión concreta. Se deriva de cuánto error de localización tolera esa decisión; no se fija automáticamente como múltiplo de δ_min,e.
5. **Zona de inconclusión:** resultados cuya incertidumbre no permite ni afirmar efecto relevante ni descartarlo; se especifica antes del análisis. Equivalencia solo con margen propio justificado y procedimiento adecuado.
6. **Vínculo con identificación:** si el estimando es PARTIALLY_IDENTIFIED, se define una resolución para bounds y no un MDE de estimación puntual; si NOT_IDENTIFIED, el gate es abstención correcta y no se define potencia de efecto.

Las fichas se aprueban por separado para ITT_Z^D2 y θ_A/θ_Af aunque compartan V_cont. No se transfiere un δ entre estimandos por compartir escala.

### 16.220.3. Jerarquía confirmatoria y multiplicidad — estado

No se declara todavía una familia confirmatoria cerrada. La arquitectura estadística debe preservar como objetos separados ITT_Z^D2 y θ_A; C4/IIE_M y LATE_f quedan condicionales/secundarios mientras sus contratos no se completen. Antes de cualquier calibración se deberá resolver:

- si ITT_Z^D2 sobre V_cont se formula como objetivo confirmatorio de efecto de paquete, sin atribución a accesibilidad;
- si θ_A/θ_Af llega a satisfacer correspondencia de políticas, soporte e identificación suficientes para entrar en la familia confirmatoria;
- cuál es la familia exacta de contrastes, resultados y poblaciones que controla α, y si se usa gatekeeping jerárquico, Holm u otro procedimiento justificado;
- cómo se conserva el carácter separado de los dictámenes cuando un estimando es identificable y otro no.

No se permite que la selección del estimando confirmatorio dependa de qué resultado sea significativo o más favorable. Tampoco se excluye silenciosamente θ_A del informe principal por no ser identificable: su no-identificación es un resultado central del experimento.

### 16.220.4. Consecuencia para dimensionamiento y estado del paquete C

No es posible elegir N/R de forma defendible a partir de los umbrales §16.219 sin δ_min,e, w_max,e, familia de escenarios y endpoint calibrado. N=700 de P178 es solo candidato del benchmark focal bajo DGP y observación ideales; no es trasladable a D2, V_cont runtime, S3, adversariales, ITT ni al Analyzer integrado. Tampoco se reutilizan automáticamente los tamaños históricos N=2.000/R=1.000.

**Resultado:** el procedimiento de justificación de márgenes queda definido; su contenido sustantivo permanece BLOCKED por falta de endpoint/beneficiario/regla operativa y por falta de correspondencia/identificación del estimando focal. La jerarquía confirmatoria/multiplicidad queda OPEN.

**Dictamen:** MARGIN_JUSTIFICATION_CONTRACT_DEFINED / NUMERIC_MARGINS_NOT_JUSTIFIABLE_FROM_CURRENT_SPECIFICATION / VALUE_ENDPOINT_MATERIALIZATION_OPEN / THETA_A_MAPPING_AND_IDENTIFICATION_OPEN / CONFIRMATORY_FAMILY_OPEN / NO_N_R_SELECTION / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente operación agrupada del paquete C:** completar sobre la misma instancia B1 la materialización mínima de V_cont/Outcome/Value y la ficha de identificación de ITT-D2 y θ_A, incluyendo las decisiones que permitan o impidan que cada uno entre en la familia confirmatoria. Después se fijan δ_min,e, w_max,e y multiplicidad en una sola pasada. No abrir nuevos documentos ni iniciar calibración.


## 16.221. Corrección de precedencia histórica de Value/V_cont y rectificación del Gate 66 (2026-11-12)

**Motivo:** la auditoría §16.220 reabrió indebidamente asuntos ya resueltos y describió como ausente la instancia sintética B1. Esta sección reconstruye la precedencia del propio expediente y supersede expresamente las afirmaciones incompatibles de §16.220. No borra el registro histórico del error.

### 16.221.1. Decisiones y contratos ya aceptados — no reabrir

La reconstrucción de §§16.141–16.147, 16.160–16.165, 16.173–16.174 y 16.182–16.217 establece:

1. **Variante B:** DEC-C10-095 acepta A como variante base y B como extensión sintética independiente/versionada para estudiar la relación causal con Value. No se está usando la variante A sin beneficiario.
2. **Beneficiario:** B1 es la entidad solicitante/beneficiaria sintética vinculada por UE al servicio lógico y a su Need_preZ basal. B1 por UE y la oportunidad estandarizada única por UE tienen decisiones/contratos previos. No es una persona real ni una muestra de usuarios reales.
3. **Perspectiva y objetivo:** la perspectiva de valoración es B1; el objetivo basal es mantener disponible la capacidad funcional del servicio, definida mediante ENABLED/PROFILE. Need_preZ es basal y se observa por S7; no se infiere de logs post-Z.
4. **Outcome/Value:** F* es criterio técnico; O-CONF es adjudicación terminal de conformidad y sigue como Outcome técnico candidato con partes materiales abiertas; consecuencia B1 y Value son objetos distintos. La instancia B selecciona V_cont como dimensión mínima unitaria provisional de Value, sin índice, pesos ni compensación, conforme a DEC-C10-099…102 y aceptación §16.174.
5. **Truth de V_cont:** por UE e intervalo, A_B1 vale 1 si se cumple durante todo el intervalo la regla funcional aplicable (admisión/no-admisión según ENABLED efectivo y exposición del PROFILE declarado), 0 ante incumplimiento funcional confirmado y ? si la verdad no queda determinada. V_cont_truth es la proporción no ponderada de intervalos completamente conformes en la rejilla común. UNKNOWN se propaga a bounds; no se imputa como cero ni se elimina del denominador. No es porcentaje exacto de uptime.
6. **Ventana:** comienza en t0 e incluye provisión e instalación; intervalos de igual duración; continuidad estricta sin gracia. La truth se genera desde estados funcionales efectivos, no desde ENABLED declarativo aislado, W_attempt, S_install, C_dep, A_f, ΔT_acc, Reach, trayectoria, petición ni señal individual S3.
7. **Observación:** S3 es canal pasivo runtime post-Z, imperfecto y separado de truth. Snapshot, log y modo híbrido se comparan emparejadamente sobre las mismas historias sintéticas. S7 conserva Need_preZ basal. No se mezclan.
8. **Discriminación:** V_cont no es O-CONF/F*, ni una recodificación de accesibilidad/Reach/trayectoria. La arquitectura de contrastes cruzados V_cont/O-CONF está definida; su comprobación sigue CONDITIONAL/NOT_VERIFIABLE mientras F*, oráculo, evento terminal, snapshots y soporte no permitan demostrar los contrastes.

Estas decisiones no convierten V_cont en medida general/universal de Value, ni en evidencia de preferencias reales. Sí constituyen una instancia sintética B1 definida por estipulación normativa ex ante, suficiente como objeto de prueba metodológica si los gates pendientes de horizonte, observación e identificación se satisfacen.

### 16.221.2. Rectificación explícita de §16.220

Quedan **RETIRADAS/SUPERSEDIDAS** las siguientes afirmaciones de §16.220:
- que no existe beneficiario/población valorativa para la instancia: B1 por UE, Need_preZ, perspectiva B1 y modalidad de oportunidad estandarizada están definidos/aceptados para la variante B;
- que Value sigue sin instanciarse en esta variante: V_cont está seleccionado y su regla semántica/funcional y agregación están especificadas documentalmente;
- que es necesario volver a materializar V_cont/Outcome/Value como si el paquete A+B no se hubiera completado;
- que la ausencia de una decisión de relevancia de una aplicación real impide evaluar el benchmark sintético.

La auditoría §16.140 sobre roles de la variante A conserva su validez dentro de su alcance; no puede utilizarse para invalidar B1 de la variante B. La secuencia correcta es A (sin beneficiario materializado) frente a B (extensión B1 explícita). La decisión §16.142/DEC-C10-095 y la aceptación posterior de B1/V_cont prevalecen para el experimento actual.

### 16.221.3. Qué permanece realmente abierto

No se reabre la semántica de Value ni la selección de V_cont. Los bloqueos remanentes son de especificación/calibración y de identificación:

- **Tiempo y soporte:** t_c,max, τ_follow, T*, unidad temporal, Δ, K y soporte finito de recurrencia/duración/recuperación, dentro de las reglas ya fijadas en §§16.214–16.215.
- **S3:** parámetros/cadencia, cobertura, lag, pérdida, error, dependencia, calibración y criterios de detectabilidad/recuperación; comparación emparejada de modos sigue vigente.
- **Discriminación V_cont/O-CONF:** sigue CONDITIONAL/NOT_VERIFIABLE hasta completar el oráculo/evento terminal F* y los contrastes cruzados factibles. No bloquea reabrir la semántica de V_cont; sí limita el estatus confirmatorio si no se demuestra validez discriminante.
- **D2 y estimandos:** ITT-D2(V_cont) es efecto de asignación al paquete, condicionado a unidad/asignación, soporte, interferencia y observación. No es efecto puro de accesibilidad. θ_Af/θ_A requieren correspondencia de políticas, régimen común, soporte y separación de vías colaterales; siguen sin identificación demostrada. C4 y LATE_f permanecen condicionales a sus contratos propios.
- **Analyzer/Evaluator:** la brecha de implementación identificada en §16.218.8 (bounds/identificación parcial, métricas por estimando, tasas de falsa recuperación/abstención, Monte Carlo, C4/LATE) permanece real y no queda resuelta por los cierres semánticos de Value.

### 16.221.4. Relectura correcta de δ_min,e y w_max,e para un experimento sintético

El objetivo C10-S actual es un **benchmark metodológico sintético de verdad conocida**, no una evaluación de la importancia de una variación de Value para usuarios reales ni una decisión empresarial real. Por ello:

- No se exige inventar un MDE sustantivo de una aplicación real para probar la recuperación causal del Analyzer.
- La magnitud verdadera del efecto se conoce por construcción en cada DGP. La evaluación debe recorrer una cuadrícula preespecificada de efectos focales positivos, nulos y adversos, junto con vías directas/colaterales y escenarios no identificados.
- El análogo pertinente de δ_min,e es el menor efecto de la cuadrícula de benchmark para el que se exige una operación/potencia determinada; es un punto de prueba del método, no un umbral de Value universal ni una afirmación de relevancia humana. La cuadrícula debe justificarse por rango factible del DGP y resolución de recuperación, no elegirse después de ver resultados.
- w_max,e es una meta de resolución inferencial del benchmark, justificada por la separación que se quiere discriminar entre valores de la cuadrícula y por la cobertura requerida; no un margen de decisión real. Se reportarán además curvas potencia/precisión, sesgo, RMSE y cobertura a lo largo de la cuadrícula.
- Si se decide incluir una afirmación de relevancia sustantiva, deberá quedar explícitamente fuera del alcance de este benchmark y requerirá otra instancia/perspectiva; no se importará a posteriori.

Por tanto, la sección §16.219 se conserva como base cuantitativa ya aceptada, pero su lectura se especializa: potencia y precisión se evalúan frente a efectos de prueba conocidos del DGP; no se bloquea el experimento por ausencia de un MDE de usuario real. La selección exacta de cuadrícula, resolución y N/R pertenece a calibración posterior y no se ejecuta en este gate.

### 16.221.5. Dictamen corregido

**CERRADO / REUTILIZAR:** instancia sintética B1; perspectiva/objetivo basal; separación Need_preZ-S7 y runtime V_cont-S3; selección provisional V_cont; regla funcional A_B1 y agregación por intervalos; truth/observed/evaluation; comienzo t0 e inclusión de provisión/instalación; igualdad de intervalos; unknown→bounds; separación conceptual O-CONF/V_cont; arquitectura de estimandos C1–C4.

**ABIERTO:** soporte temporal numérico, Δ/K/T*, parámetros/calibración S3, validez discriminante material V_cont/O-CONF, identificación específica de ITT-D2/θ_A/C4/LATE y extensión técnica Analyzer/Evaluator; cuadrícula de efectos y precisión/N/R, sin MDE sustantivo real.

**Dictamen:** GATE66_CORRECTED_HISTORICAL_PRECEDENCE / B1_BENEFICIARY_AND_VCONT_RULE_REUSED / VALUE_SEMANTICS_NOT_REOPENED / TEMPORAL_S3_AND_CAUSAL_IDENTIFICATION_GAPS_RETAINED / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** cerrar de forma conjunta la definición de la cuadrícula de efectos del DGP y el contrato de identificación/soporte de ITT-D2 y θ_A, reutilizando las fichas C1/C-MED/MAP ya existentes. No reabrir Value, B1 ni la fórmula de V_cont. No crear una nueva matriz o subpaquete.


## 16.222. Gate 68 — contrato estructural de identificación/soporte y cuadrícula de efectos (2026-11-12)

**Precedencia:** §§16.199–16.212, 16.218–16.221; C1 §§15–18; D2 assignment/population/support §§3–10; C10-D1/S4R §§18–20 y 23–27; P177–P183. Esta sección cierra la arquitectura de los contrastes sintéticos y la lógica de su cuadrícula. No cierra todavía sus parámetros numéricos ni la identificación material de una instancia no generada.

### 16.222.1. Regla de no reapertura y alcance

Se reutilizan B1/variante B y V_cont conforme a DEC-C10-095/099–102, §16.174 y corrección §16.221. No se reabre Value, su perspectiva B1, la semántica de V_cont, la regla por intervalos ni la separación S3/S7/O-CONF. La auditoría A de falta de beneficiario no invalida la variante B.

El objeto de este gate es el benchmark sintético de verdad conocida. La pertenencia a la población, las historias basales, la asignación y los mecanismos se estipulan dentro de cada mundo versionado. Esa estipulación local no ratifica una fórmula universal de E_i, no crea evidencia IAM real y no autoriza transportar los parámetros a una población empírica.

### 16.222.2. Contraste C1: ITT total de asignación D2 sobre V_cont

Para cada mundo w, se define antes de generar resultados una cohorte finita P_w cuya pertenencia verdadera se establece en el Generator mediante los predicados basales del mundo. En el mundo limpio, las unidades incluidas satisfacen por construcción las condiciones de la población objetivo candidata P*_{τ2} (incluidos C_dep,0*=0 y A_f,0*=0); E_scope y App*(τ2,S0) se declaran separadamente, sin elevar E_i=E_scope∧App a regla universal aceptada. Los mundos con pertenencia ambigua conservan ? y no se reclasifican como excluidos.

El contraste es:
\[
ITT^{D2}_{V_{cont}}(P_w,T^*) =
E_{i\in P_w}[V_{cont,i}(Z=1;D2,T^*)-V_{cont,i}(Z=0;D2,T^*)].
\]

Contrato de identificación para que el oráculo clasifique el contraste como IDENTIFIED:
- Z se asigna aleatoriamente en la unidad UA conforme a probabilidades de diseño versionadas; en cada estrato/historia con masa objetivo, 0<π_h<1. No se presupone ratio 1:1, algoritmo, semilla ni tamaño.
- La aleatorización es independiente de los potenciales bajo el diseño declarado; las desviaciones, crossover y versiones se registran y no se sustituyen por recepción/cumplimiento.
- UA=UE solo en mundos aislados por construcción. Si hay exposición compartida, el mundo define clúster/UA o G_i(Z_{-i}) y potenciales compatibles. Sin ese mapa, el ITT individual no es IDENTIFIED.
- La cohorte y su regla basal se fijan antes de Z. El Analyzer recibe evidencia pre-Z suficiente para la pertenencia en las celdas identificables; si la evidencia de elegibilidad es incompleta/diferencial, el oráculo exige bounds o INDETERMINATE/NOT_IDENTIFIED según el mecanismo. El Generator no filtra a posteriori por variables post-Z.
- La distribución basal finita tiene soporte explícito. El estimando se refiere a P_w y al horizonte común T*; no se transporta a otra población/horizonte.
- V_cont tiene truth por unidad y ventana conforme a DEC-C10-100/102. La salida observada procede de S3. Si el canal, pérdida/censura o missingness no permite identificar el resultado bajo los supuestos declarados, no se aprueba un punto por el mero hecho de que Generator conozca la truth.

Con estas condiciones, el objeto recuperable es el efecto total del paquete D2 sobre V_cont, incluidas todas las vías activadas por D2. Nunca se renombra como efecto focal de accesibilidad. El estimador debe respetar probabilidades de asignación/estratos y la unidad realmente aleatorizada; el estimador concreto se fija junto al mecanismo de asignación antes de calibración.

### 16.222.3. Contraste focal C3: θ_A bajo intervención directa g_A

\[
\theta_A(q_X^*,r_{common};V_{cont}) =
E_{X\sim q_X^*,\,\Delta T\sim g_{A1},\,R\sim r_{common}}[V_{cont}]
-
E_{X\sim q_X^*,\,\Delta T\sim g_{A0},\,R\sim r_{common}}[V_{cont}].
\]

- q_X* es una distribución basal finita y versionada, con masas q_j>0 sobre sus historias x_j; excluye Z, Need_preZ como filtro y variables post-Z. Las mismas historias, masas y pesos se usan para g_A1 y g_A0.
- g_A1 y g_A0 son intervenciones estocásticas factibles sobre el vector completo ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), no sobre D_f* ni una coordenada aislada. Para cada historia con masa positiva, ambas políticas deben tener soporte/positividad y versiones admisibles. Si no, el contraste sobre esa q_X* no está identificado; solo cabe restringir la población ex ante y redefinir el estimando, o informar bounds/no identificación.
- r_common fija por contrato los mecanismos no focales compartidos entre ambos regímenes. No significa que las vías directas/colaterales sean inexistentes. Si una vía afecta diferencialmente a V_cont y no puede mantenerse común, separarse o identificarse, el efecto focal puntual no está identificado.
- Los potenciales bajo g_A1/g_A0 comparten la misma historia basal y exógenas de unidad según §16.212; no se generan como muestras independientes de unidades distintas.
- La comparación se prueba directamente en el DGP bajo g_A; no se infiere desde Z, W_programmed, provisión, C_dep*, A_f*, D_f* ni desde ITT_Z^D2.

El mapping B_g^D2→g_A permanece NOT_DEMONSTRATED. Solo un mundo específico que lo estipule y demuestre distribución inducida equivalente, versiones, régimen común, soporte y ausencia/separación de vías diferenciales podrá probar una correspondencia. La existencia de ese mundo no autoriza generalizar la equivalencia a R1/R2 ni a todo D2.

### 16.222.4. Matriz de identificación por clase de mundo

| Clase ya existente | ITT-D2(V_cont) | θ_A(V_cont) | Dictamen/uso |
|---|---|---|---|
| Focal limpio, asignación D2 aleatoria, aislamiento, medición suficiente | Identificado como efecto total de paquete | Identificado solo en su contraste g_A directo; no por D2 sin mapping probado | Control positivo por estimando |
| Nulo general/condicionado | Identificado si conserva asignación/soporte/canal | Identificado si ambas g_A son factibles y el canal lo permite | Debe recuperar cero dentro del criterio; no confundir no-rechazo con equivalencia |
| Vía directa o colateral D2→V_cont | ITT identificado si se mantienen las condiciones C1 | No identificado como focal si no se mantiene/separa la vía mediante r_common | Control de falsa atribución focal |
| Alternativa basal R1 | ITT identificado bajo diseño | θ_A solo sobre q_X* común y factibilidad de ambas políticas | No confundir apertura focal con incremento de Reach |
| Alternativa afectada R2 / interacción | ITT total puede identificarse por diseño; heterogeneidad exige soporte por estrato | Identificación depende de soporte condicional y régimen común | Sin soporte, bounds/abstención |
| Primera etapa nula/débil o IV adversarial | ITT no queda invalidado por ello | No habilita atribución IV; LATE_f no se presume | No Wald automático |
| Falta de positividad o historia fuera de soporte | No identificado para la población/historia sin soporte; posible estimando restringido solo ex ante | No identificado en la masa sin soporte | No extrapolar |
| Interferencia | Identificado solo para UA/clúster/exposición definido | Requiere política/exposición y soporte compatibles | Sin mapa, no efecto individual |
| S3 diferencial, pérdida/censura o medición degradada | Según modelo de observación: identificado, bounds o indeterminado | Igual, con identificación focal adicional | Truth no sustituye observación |

C4/IIE_M y LATE_f no se declaran cerrados en este gate: conservan sus contratos y supuestos propios. Las primeras etapas C2 siguen siendo diagnósticos de mecanismo, no sustitutos de C1 o C3.

### 16.222.5. Cuadrícula de efectos: estructura cerrada, valores numéricos abiertos

Se fijan dos cuadrículas separadas: G_ITT para el contraste verdadero ITT^{D2}_{V_cont} y G_A para θ_A. Ningún valor de una se transfiere a la otra. En cada mundo y estimando, el Evaluator calcula la truth exacta (o conjunto de truth si el oráculo es parcial) después del sellado del Analyzer.

Como V_cont∈[0,1], la cuadrícula se construye desde la media de referencia μ_0 y el rango factible, no desde valores arbitrarios:
- efecto nulo: δ=0;
- efectos positivos: δ^+_e(κ)=κ(1−μ_{0,e});
- efectos negativos: δ^-_e(κ)=−κ μ_{0,e};
- κ toma niveles ordenados desde señal débil hasta efecto amplio, predeclarados y comunes dentro de cada familia comparable. Sus valores concretos quedan pendientes de justificación por resolución del benchmark.
- Para exigir ambos signos sin degeneración de techo/suelo, las celdas bidireccionales usan una condición basal interior 0<μ_{0,e}<1. Si la media está en frontera, solo se incluye la dirección factible y se registra la limitación; no se fabrica un efecto imposible.
- Los efectos heterogéneos pueden combinar signos opuestos por estrato y producir media marginal nula; estas celdas comprueban que el Analyzer no confunda nulo marginal con ausencia de efectos condicionales.
- Las familias directas/colaterales cruzan el efecto total ITT con un efecto focal nulo, débil o de signo distinto; no se imponen relaciones algebraicas entre ITT y θ_A.
- Los mundos de no-identificación, soporte fallido, interferencia no mapeada y observación insuficiente no reciben un efecto puntual exigible: se evalúa clasificación, bounds y abstención.

La cuadrícula se genera dentro del roster dirigido de §§16.208/16.211; no es factorial completo. Cada celda declara estimando, población, horizonte, mundo, signo, nivel κ, mecanismo focal/no focal, estado de identificación del oráculo y régimen de observación. Las configuraciones de calibración y evaluación final permanecen separadas conforme §16.218.6.

δ_min,e se interpretará como el primer nivel no nulo de la cuadrícula para el que se exige potencia objetivo; w_max,e como la resolución inferencial requerida para distinguir los niveles pertinentes, siempre en la escala V_cont y por estimando. Los valores de κ, δ_min,e, w_max,e, masas q_j, pesos de familias, parámetros y N/R siguen abiertos; no se seleccionan retrospectivamente ni se derivan de P178.

### 16.222.6. Criterios de aceptación y salidas del Analyzer

Se reutilizan sin modificación los objetivos aceptados en §16.219: α bilateral 0,05, cobertura nominal 95%, potencia ≥0,80 en celdas identificables al efecto mínimo predeclarado, MCSE≤0,005 y límites de falsa atribución/abstención por familia con su incertidumbre Monte Carlo. No se ejecutan ni se extienden automáticamente a C4/LATE.

- IDENTIFIED: estimación e intervalo según el diseño/contraste y cobertura aplicables.
- PARTIALLY_IDENTIFIED: bounds que cubren el conjunto de verdad bajo las restricciones declaradas; no punto forzado.
- NOT_IDENTIFIED: falta de identificación estructural (p. ej. no soporte, vía no separada, interferencia no mapeada).
- INDETERMINATE: la evidencia/canal no permite decidir entre estados/valores.
- Cualquier punto focal emitido en un mundo cuyo oráculo sea NOT_IDENTIFIED/INDETERMINATE es falsa atribución crítica, incluso si numéricamente parece próximo a la truth.

No se usa significación aislada como criterio de recuperación, ni se agrega el rendimiento de estimandos/familias para compensar fallos.

### 16.222.7. Estado y siguiente dependencia

**CERRADO ESTRUCTURALMENTE:** definición separada de C1 y C3 en el benchmark; condiciones de identificación y soporte por estimando; separación D2/g_A; construcción factible de cuadrículas distintas; relación entre cuadrícula, δ_min y w_max; roster dirigido de controles positivos, nulos y adversariales.

**ABIERTO:** valores de κ, composición/masas numéricas de q_X*, probabilidades/estratos de asignación, parámetros de las funciones generadoras, régimen r_common por escenario, mapping D2→g_A si se quiere probar, parámetros S3, δ_min,e, w_max,e, pesos/orden de familias, multiplicidad, N/R y capacidad técnica del Analyzer para bounds y métricas. La identificación efectiva de cualquier instancia depende de que esas condiciones se materialicen y se verifiquen.

**Dictamen:** ITT_AND_THETA_A_IDENTIFICATION_SUPPORT_CONTRACT_CLOSED_STRUCTURALLY / SEPARATE_EFFECT_GRIDS_DEFINED / NUMERIC_GRID_AND_SUPPORT_OPEN / D2_TO_GA_MAPPING_NOT_DEMONSTRATED / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** completar el ledger paramétrico mínimo de cada celda de la cuadrícula (masas q_X*, asignación/UA, κ y funciones activas) y el r_common por clase, todavía sin asignar valores numéricos. Después se podrá preparar la decisión cuantitativa de parametrización, sin ejecutar calibración.


## 16.223. Gate 69 — ledger paramétrico mínimo y régimen común por mundo (2026-11-12)

**Precedencia:** §§16.208–16.218 y 16.221–16.222; crosswalk basal §16.210; mapping finito §16.211; funciones generadoras/contrafactuales §16.212; contratos D2 y C1. Este gate no reabre Value, B1, V_cont, S3/S7 ni el roster. Traduce los contratos existentes a un esquema único de configuración por celda.

### 16.223.1. Separación de objetos

Cada celda distingue obligatoriamente: (a) P_w, cohorte finita pre-Z del ITT-D2; (b) q_X*, distribución de historias basales para C3; (c) Z y pi_h, mecanismo de asignación en UA para C1; (d) g_A0/g_A1, intervenciones directas sobre el vector completo DeltaT_acc* para C3. No se identifica ninguno de estos objetos con otro. W_programmed(z)=z es regla de política, no aleatorización. La truth contrafactual calculada por Generator bajo g_A tampoco implica que Analyzer tenga una fuente de identificación disponible.

### 16.223.2. Ledger obligatorio por celda del roster existente

| Campo | Registro requerido | Regla de admisión |
|---|---|---|
| world_id/version | Clase y modificador ya existente en §16.211 | Identidad estable; no multiplicar clases por combinatoria |
| estimand_id | C1, C2, C3, C4 o LATE_f | Estado de identificación independiente por estimando |
| population_id | P_w o q_X* y regla basal | Cohorte/soporte pre-Z; UNKNOWN no se convierte en exclusión |
| assignment_id | UA, estratos y pi_h, si aplica | pi_h positiva para ambos brazos por estrato con masa; no asumir ratio |
| intervention_id | Política D2 o g_A0/g_A1, versión y factibilidad | D2 no equivale a g_A sin mapping demostrado |
| effect_cell | Estimando, signo, κ, media basal y truth/conjunto truth | G_ITT y G_A separados; efecto factible en la escala de V_cont ya fijada |
| active_functions | Funciones generadoras que cambian en la celda | Variar solo mecanismos necesarios para el falsador |
| held_fixed | Historia, exógenas pareadas, versiones y funciones no focales | Declaración explícita; no inferir invariancia por omisión |
| r_common_status | COMMON_FIXED / DIFFERENTIAL_IDENTIFIED / DIFFERENTIAL_UNRESOLVED / NOT_APPLICABLE | Solo COMMON_FIXED sustenta el contraste focal controlado sin ajuste adicional |
| support_status | Soporte de Z y, por separado, de ambas g_A en cada historia con masa | Fallo: restringir ex ante con nuevo estimando, bounds o no identificación; nunca extrapolar |
| interference_status | Aislamiento UA=UE, clúster o mapa de exposición | Sin estructura compatible, no ITT individual |
| observation_profile | Modo S3 y propiedades de cobertura/error/lag/pérdida | Truth constante al comparar canales; S7 sigue siendo basal |
| oracle_identification | IDENTIFIED / PARTIALLY_IDENTIFIED / NOT_IDENTIFIED / INDETERMINATE | Lo adjudica Evaluator con truth completa |
| analyzer_information | Campos y parámetros visibles realmente | No exponer potenciales, truth ni secretos del Generator |
| acceptance_target | Criterio aplicable por estimando/familia | Reutilizar §16.219; no extender a C4/LATE sin contrato propio |

q_X* es una distribución finita de historias con masas positivas en el soporte declarado y suma unitaria. pi_h son probabilidades de asignación, no masas basales. Los pesos de familias del benchmark son un tercer objeto distinto. No se fijan número de historias, masas ni probabilidades en este gate.

### 16.223.3. Matriz de mecanismos activos y r_common por clases existentes

| Clase existente | Mecanismo activo o variado | r_common / invariantes | Uso y salida esperada |
|---|---|---|---|
| Focal limpio R0 | g_A altera DeltaT_acc*; outcome focal responde según G_A | Misma historia, exógenas pareadas, q_X*, versiones y mecanismos no focales; sin interferencia por construcción | Control positivo C3 si Analyzer tiene identificación; C1 solo con Z/UA/pi_h propios |
| Nulo focal | DeltaT_acc* puede variar, pero el mecanismo de outcome no responde a su componente focal | Todo lo no focal permanece idéntico entre g_A0/g_A1 | Truth focal cero; medir error tipo I y falsa recuperación |
| Nulo de primera etapa D2 | Z no induce el cambio de accesibilidad definido | No alterar por ello la definición de ITT ni confundir first-stage con outcome | C2 nulo; ITT puede tener otras vías; no habilita LATE |
| Fallo de etapa R3 | Se activa solo la función de intento/recepción/instalación/C_dep que corresponda | Mantener separados programación, intento, receipt, instalación, C_dep*, A_f*, D_f* y DeltaT_acc* | No propagar automáticamente un fallo upstream a V_cont o accesibilidad |
| Focal adverso | g_A cambia DeltaT_acc* en dirección adversa | Misma historia, exógenas, q_X*, r_common y canal | Recuperar signo adverso o bounds/abstención |
| Alternativa basal R1 | Se activa ruta alternativa basal pi_A | Alternativa y outcome permanecen iguales bajo g_A salvo interacción declarada | No equiparar apertura focal a incremento de Reach ni exclusividad |
| Alternativa afectada/colateral R2 | Cambia A1/A2 o dependencia/recurso compartido | Si la rama es igual bajo ambos g_A, es común aunque esté activa; si difiere, marcar diferencial | ITT puede incluirla; theta_A puntual solo si se separa/identifica |
| Vía directa D2→outcome | Z/paquete afecta V_cont sin pasar por DeltaT_acc* | No es parte de r_common si varía entre brazos D2; para C3 debe mantenerse fija o identificarse aparte | ITT total incluye la vía; atribuirla a accesibilidad es falso positivo focal |
| Interacción/heterogeneidad | Outcome depende de X/H0/C_c, versión o exposición | Misma q_X* y exógenas pareadas; declarar r_common condicional a historia | Informar efecto marginal y heterogeneidad con soporte; no extrapolar |
| IV adversarial | Se viola la condición IV designada (exclusión, monotonicidad o relevancia) | Mantener invariantes las demás funciones salvo interacción prevista | ITT sigue separado; no Wald/LATE automático |
| Interferencia | Se activa recurso/agente/estado/canal compartido | Mapa G_i o clúster forma parte del régimen; no fingir invariancia individual | Estimando de clúster/exposición o NOT_IDENTIFIED |
| Observación adversarial | Cambia solo S3: modo, error, cobertura, lag, pérdida o censura | Misma truth, potenciales, asignación y funciones | Comparar detección, V_cont y efecto causal; bounds/abstención si el canal no identifica |
| Soporte/ausencia/censura | Se retira positividad, factibilidad, historia o seguimiento | No sustituir historias ni cambiar población a posteriori | NOT_IDENTIFIED o bounds; población restringida solo como estimando nuevo predeclarado |

La matriz es un mapping de mecanismos, no una expansión factorial. Una rama no focal puede estar activa y ser COMMON_FIXED si función, versión y exógenas se mantienen iguales entre los regímenes comparados. Si cambia diferencialmente y su contribución no se identifica, r_common_status=Differential_Unresolved y no procede atribución puntual focal.

### 16.223.4. Acoplamiento contrafactual

Los potenciales g_A0/g_A1 se construyen sobre la misma historia basal y las mismas exógenas de UE, conservando sus dependencias conjuntas. No se resortea una unidad por régimen ni se presume independencia entre componentes. Las funciones no focales, recursos, alternativas, entorno, capacidad, información, interferencia y proceso de outcome se fijan explícitamente; solo cambia lo que define el régimen o el falsador. Las comparaciones emparejadas de canales S3 cambian el canal y mantienen truth constante. Ninguna variable post-intervención se ajusta como si fuera basal cuando forma parte del mecanismo causal.

### 16.223.5. Estado del ledger y criterios de coherencia

El esquema y la matriz de activación quedan cerrados estructuralmente. La materialización celda a celda, masas q_X*, pi_h/UA, kernels g_A, κ, medias basales, funciones/exógenas, mapas de interferencia, parámetros S3 y dimensionamiento permanecen abiertos. Se conservan los criterios cuantitativos aceptados en §16.219; no se recalibran ni se trasladan a C4/LATE. La coherencia del ledger debe verificar que pi_h no se use como q_j; q_X* no sea peso de escenarios; κ no sea probabilidad; r_common no se deduzca de nombres iguales; y NOT_APPLICABLE no se convierta en efecto nulo.

**Dictamen:** PARAMETER_LEDGER_SCHEMA_AND_R_COMMON_RULES_CLOSED_STRUCTURALLY / EXISTING_WORLD_ROSTER_REUSED / CELL_LEVEL_MATERIALIZATION_OPEN / NUMERIC_PARAMETERS_OPEN / D2_TO_GA_MAPPING_NOT_DEMONSTRATED / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** auditar la cobertura mínima del roster existente por estimando C1 y C3: controles positivos identificables, nulos identificables, falsadores de falsa atribución, escenarios que exigen bounds/abstención y huecos de representación. Reutilizar §16.211; no ampliar el roster por defecto.


## 16.224. Gate 70 — auditoría de cobertura mínima del roster por estimando C1/C3 (2026-11-12)

**Precedencia:** §§16.208–16.223, en particular mapping finito §16.211, funciones generadoras §16.212, B1/V_cont §§16.213–16.221 y contratos C1/C3 y ledger §§16.222–16.223. Esta auditoría no reabre Value, B1, V_cont, S3/S7, semántica temporal ni roster. Comprueba qué cubre realmente el roster documental y qué no puede afirmarse todavía.

### 16.224.1. Regla de lectura de cobertura

Se distinguen cuatro estados: **MAPPED** (clase/mecanismo y salida previstos); **IDENTIFICATION-CONDITIONED** (control positivo solo si se materializan las condiciones del estimando y la información del Analyzer); **ABSTENTION-ONLY** (prueba bounds/abstención/no-identificación, no recuperación puntual); **NOT-MATERIALIZED** (mecanismo mencionado, pero sin celda versionada con truth, soporte, asignación/intervención y observación).

Una clase MAPPED no equivale a cobertura ejecutable ni a test implementado. No se cuentan menciones documentales como celdas. La base es exclusivamente el roster §16.211.3 y el mapping §16.211.4.

### 16.224.2. Matriz de cobertura por estimando

| Clase existente §16.211 | C1: ITT-D2 sobre V_cont | C3: θ_A sobre ΔT_acc* | Cobertura y limitación |
|---|---|---|---|
| Focal limpio R0 | IDENTIFICATION-CONDITIONED | IDENTIFICATION-CONDITIONED | Único candidato positivo principal. C1 necesita Z/UA/π_h materializados; C3 necesita g_A directo factible, q_X*, r_common y fuente de identificación visible al Analyzer. La truth del Generator no basta |
| Nulo | MAPPED, NOT-MATERIALIZED | MAPPED, NOT-MATERIALIZED | Deben existir nulos separados ITT=0 y θ_A=0; nulo de outcome no implica primera etapa nula |
| Fallo por etapas R3 | IDENTIFICATION-CONDITIONED | No positivo; puede ser ABSTENTION-ONLY | Separa programación/intento/recepción/instalación/C_dep; no implica por sí mismo fallo B1 ni efecto focal |
| Focal adverso | IDENTIFICATION-CONDITIONED | IDENTIFICATION-CONDITIONED | Candidato negativo; función, contraste y soporte aún no materializados |
| Alternativa basal R1 | IDENTIFICATION-CONDITIONED para ITT total | IDENTIFICATION-CONDITIONED o ABSTENTION-ONLY según r_common | No equivale a exclusividad ni a efecto focal; punto focal solo si la alternativa permanece común o se identifica |
| Alternativa afectada/colateral R2 | IDENTIFICATION-CONDITIONED para ITT total | ABSTENTION-ONLY si diferencial no identificada; identificable si se separa | Falsador crítico; función colateral no parametrizada |
| Vía directa D2→resultado | IDENTIFICATION-CONDITIONED para ITT total | ABSTENTION-ONLY si no se separa | ITT recoge la vía; no se rebautiza como θ_A |
| Interacción/heterogeneidad | IDENTIFICATION-CONDITIONED | IDENTIFICATION-CONDITIONED solo con soporte condicional | Cobertura conceptual; faltan masas, estratos, funciones y celdas condicionales |
| IV adversarial | ITT puede seguir IDENTIFICABLE por asignación | No identifica θ_A; ABSTENTION-ONLY para LATE inválido | Controla el rechazo de Wald/LATE automático |
| Interferencia | ABSTENTION-ONLY hasta definir UA/clúster/mapa | ABSTENTION-ONLY hasta definir exposición/política | Sin mapa concreto no se admite ITT individual por defecto |
| Observación adversarial S3 | IDENTIFICATION-CONDITIONED o ABSTENTION-ONLY según canal | Igual, con gate focal adicional | Truth emparejada; calibración, error, pérdida y dependencia abiertos |
| Soporte/ausencia/censura | ABSTENTION-ONLY o bounds salvo región identificable predeclarada | ABSTENTION-ONLY o bounds si falta soporte de alguna g_A | Prohibida la extrapolación y el cambio post hoc de población |

### 16.224.3. Cobertura conceptual existente

El roster contiene clases para: control focal limpio; nulo; primera etapa nula/débil; fallo por etapas; efecto adverso; alternativa basal y alternativa afectada/colateral; vía directa; interacción/heterogeneidad; IV adversarial; interferencia; observación degradada/diferencial; falta de soporte, ausencia y censura. Esta cobertura dirigida es suficiente conceptualmente para los falsadores principales C1/C3. No se justifica añadir nuevas clases por ahora.

### 16.224.4. Huecos efectivos

1. No hay controles positivos identificables materializados para C1 ni C3. R0 es candidato: faltan asignación Z/UA/π_h para C1; fuente de identificación de g_A, kernels y soporte para C3.
2. El nulo no está desdoblado por estimando: faltan celdas independientes ITT-D2=0, θ_A=0 y primera etapa ΔT_acc*=0, incluyendo desacoplamientos (primera etapa nula con vía directa ITT no nula).
3. No se ha verificado celda a celda el cruce signo×estimando: positivos, negativos y niveles débiles de G_ITT y G_A siguen estructurales, no materializados. No se presupone coincidencia de signos.
4. Vía directa/colateral existe como clase, no como verdad de celdas: faltan pares ITT no nulo con θ_A nulo/no identificado y casos donde ambos difieran en signo o magnitud.
5. R1/R2 no prueban cobertura de Reach/F*: F*, M/M_A, exhaustividad de alternativas y O-CONF siguen abiertos; no sustituyen C1/C3.
6. Heterogeneidad está solo mapeada: faltan masas por historia, soporte condicional y celdas de signos opuestos con media marginal potencialmente nula.
7. Interferencia, observación adversarial y censura son controles de bounds/abstención mientras no se materialicen mapas/modelos y condiciones de identificación.
8. La capacidad del Analyzer para PARTIALLY_IDENTIFIED/bounds, cobertura de bounds y métricas por familia sigue siendo una brecha de implementación ya registrada en §16.218.8.

### 16.224.5. Dictamen y siguiente dependencia

El roster es **suficiente como roster conceptual dirigido** para los falsadores principales de C1/C3; su cobertura efectiva es **NOT_VERIFIED**. No se amplía el roster. La clasificación anterior es contrato de cobertura, no evidencia de ejecución. No se crean nuevas clases por cada combinación signo×modo S3×familia; esas combinaciones serán atributos de celdas cuando la parametrización las justifique. C4/LATE conservan sus contratos separados.

**Dictamen:** EXISTING_ROSTER_CONCEPTUALLY_SUFFICIENT_FOR_C1_C3 / EFFECTIVE_CELL_COVERAGE_NOT_VERIFIED / POSITIVE_CONTROLS_NOT_MATERIALIZED / ESTIMAND_SPECIFIC_NULL_AND_SIGN_CELLS_OPEN / DIRECT_COLLATERAL_DECOUPLING_CELLS_OPEN / BOUNDS_ANALYZER_IMPLEMENTATION_GAP_RETAINED / NO_ROSTER_EXPANSION / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** especificar las celdas mínimas obligatorias —sin cifras— para C1 y C3: control positivo, nulo por estimando, efecto negativo, vía directa/colateral desacoplada, heterogeneidad con signos opuestos y control de no-identificación/abstención. Reutilizar §§16.211–16.223 sin duplicar sus mecanismos/campos.


## 16.225. Gate 71 — especificación de celdas mínimas obligatorias C1/C3 (2026-11-12)

**Precedencia:** §§16.208–16.224, especialmente roster §16.211.3, identificación/soporte y cuadrículas §16.222, ledger/r_common §16.223 y auditoría de cobertura §16.224. Este gate define roles de celda y contrastes mínimos; no crea nuevas clases de mundo, no asigna cifras, no materializa parámetros ni modifica código. No reabre Value, B1, V_cont, S3/S7, la ventana temporal ni C4/LATE.

### 16.225.1. Regla de construcción

Las celdas son **roles de contraste del ledger**, no nuevos mundos ni nuevas familias. Cada celda referencia una clase/mecanismo del roster §16.211.3 y hereda del ledger §16.223 sus campos de población, asignación, intervención, soporte, r_common, interferencia, observación, verdad y firewall. Una misma configuración puede cubrir dos roles solo si las verdades y condiciones de identificación requeridas son simultáneamente compatibles y quedan registradas por separado; no se permite contar una celda dos veces por su etiqueta.

La matriz es mínima en cobertura lógica, no un factorial. Los signos, magnitudes, historias, perfiles S3 y parámetros se fijarán después dentro de la cuadrícula ya prevista; no se crean valores de efecto ni márgenes numéricos en este gate.

### 16.225.2. Celdas obligatorias C1 — ITT-D2

| Rol de celda | Clase existente | Verdad DGP exigida | Condición de identificación/salida exigida |
|---|---|---|---|
| C1-POS | Focal limpio R0 | ITT-D2 no nulo positivo | Z aleatorizado en UA, positividad por estrato, consistencia/versiones, interferencia resuelta y observación compatible; Analyzer recupera ITT total con incertidumbre |
| C1-NULL | Nulo | ITT-D2 exactamente nulo, aunque las primeras etapas o θ_A puedan ser no nulas | No imponer nulos a C2/C3; Analyzer no debe fabricar efecto y debe distinguir estimación compatible con cero de falta de precisión |
| C1-NEG | Focal adverso o vía directa/colateral con signo adverso | ITT-D2 no nulo negativo | Mismas condiciones de identificación que C1-POS; recuperar dirección y magnitud con incertidumbre |
| C1-DECOUPLED | Vía directa D2→resultado y/o R2 colateral | ITT-D2 no nulo mientras θ_A sea nulo o no identificable, según verdad separada | El ITT conserva el efecto total del paquete; queda prohibido presentarlo como efecto focal. Si la rama colateral viola r_common, C3 debe abstenerse/bounds |
| C1-HET | Interacción/heterogeneidad | Efectos condicionales de ITT con signos opuestos en historias con masa positiva; registrar también el ITT marginal, que puede ser nulo o de signo distinto | q_X*/P_w y soporte condicional predeclarados; informar marginal y condicionales sin transportar fuera del soporte |
| C1-ABSTAIN | Interferencia, soporte/ausencia/censura u observación adversarial | Al menos una condición necesaria de identificación de C1 ausente o no verificable | Analyzer no emite ITT puntual identificado; salida NOT_IDENTIFIED/INDETERMINATE o bounds solo si el contrato de bounds está disponible |

### 16.225.3. Celdas obligatorias C3 — efecto focal sobre ΔT_acc*

| Rol de celda | Clase existente | Verdad DGP exigida | Condición de identificación/salida exigida |
|---|---|---|---|
| C3-POS | Focal limpio R0 | θ_A no nulo positivo bajo g_A1/g_A0 sobre el vector completo ΔT_acc* | Ambas políticas factibles y con soporte en cada historia con masa; q_X* común; r_common acreditado; fuente de asignación/intervención visible al Analyzer; estimación focal con incertidumbre |
| C3-NULL | Nulo focal | θ_A exactamente nulo, sin imponer ITT-D2=0 ni primera etapa nula | Analyzer distingue cero verdadero de imprecisión y no usa ITT como sustituto |
| C3-NEG | Focal adverso | θ_A no nulo negativo | Mismas condiciones de soporte, régimen común y observabilidad que C3-POS |
| C3-DECOUPLED | Vía directa D2→resultado y R2 colateral | Contrastes separados: (a) ITT no nulo con θ_A nulo; (b) rama no focal diferencial bajo g_A con θ_A no identificable. No colapsarlos | En (a), recuperar/abstenerse según fuente focal realmente disponible; en (b), abstención o bounds. Nunca atribuir a ΔT_acc* la vía directa/colateral |
| C3-HET | Interacción/heterogeneidad | Efectos focales condicionales de signos opuestos sobre historias con masa positiva; conservar el efecto marginal y su relación con la composición de q_X* | Soporte de ambas g_A en cada estrato/historia relevante; informar heterogeneidad y marginal sin extrapolación |
| C3-ABSTAIN | Soporte/factibilidad fallida, r_common diferencial no separado, interferencia o canal no identificante | θ_A no identificable o parcialmente identificable por construcción | No emitir estimación puntual identificada. PARTIALLY_IDENTIFIED/bounds solo cuando exista contrato y Analyzer implementado; de lo contrario, abstención explícita |

### 16.225.4. Separaciones cruzadas que no se pueden omitir

1. **Nulo de outcome ≠ nulo de primera etapa.** C1-NULL, C3-NULL y primera etapa nula son verdades separadas. Debe existir al menos un desacoplamiento con primera etapa ΔT_acc* nula y ITT-D2 no nulo por vía directa, si se mantiene dentro del rango factible del DGP.
2. **ITT-D2 ≠ θ_A.** C1-DECOUPLED debe contener una verdad donde el paquete tenga efecto y el efecto focal sea nulo o no identificable. El Evaluator adjudica ambos por separado.
3. **Asignación G ≠ intervención focal identificada por definición.** La diferencia observada por G solo representa θ_A cuando G implementa el contraste sobre el vector completo ΔT_acc* y no abre vías directas/colaterales diferenciales; de otro modo es un contraste de asignación/manipulación y no acredita el efecto focal. La truth de θ_A debe definirse por el régimen g_A, no copiarse automáticamente del contraste empírico G.
4. **Heterogeneidad ≠ promedio.** Las verdades condicionales, sus masas q_X* y el efecto marginal se conservan; un promedio nulo no demuestra ausencia de efectos condicionales.
5. **Abstención ≠ error de recuperación.** La abstención es correcta si falta identificación; es excesiva si se produce en un control positivo identificable con canal y soporte suficientes. La auditoría debe puntuar ambos por estimando.
6. **C4 y LATE_f no se aprueban con estas celdas.** Sus celdas y condiciones permanecen sujetas a contratos independientes.

### 16.225.5. Compatibilidad con el harness existente y límite de implementación

La inspección estática del artefacto existente 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py (blob SHA 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4) muestra que ya contiene asignaciones separadas Z/G, potenciales cruzados [unidad][z][g], cuatro coordenadas observadas de ΔT_acc*, perfiles R0–R3 y escenarios candidatos de positivo, nulo, adverso, vía directa, alternativa, colateral, fallo de provisión, medición, interferencia, soporte y heterogeneidad. Esto es **cobertura de código candidato**, no cierre de las celdas ni autorización de ejecución.

Se detecta una precisión semántica obligatoria antes de cualquier futura implementación/aceptación: el campo actual theta_access_truth se calcula como contraste potencial de G sobre V_cont bajo Z=0. Ese contraste solo coincide con θ_A si G manipula el vector ΔT_acc* y no tiene vía directa/colateral diferencial. El escenario focal_direct_effect demuestra por qué no puede tratarse automáticamente como verdad de θ_A. La futura truth del Evaluator debe conservar por separado (i) contraste ITT de Z, (ii) contraste de asignación G y (iii) θ_A definido por el régimen g_A sobre ΔT_acc*. No se modifica el código en este gate.

La misma inspección confirma que el Analyzer actual solo emite IDENTIFIED/NOT_IDENTIFIED/INDETERMINATE, no implementa PARTIALLY_IDENTIFIED/bounds y no calcula métricas de cobertura/calibración por familia; §16.218.8 sigue vigente. La lista benchmark_scenarios es candidata y no acredita por sí sola que todos los roles C1/C3 estén cubiertos: en particular, el desacoplamiento de primera etapa nula con ITT no nulo y la heterogeneidad con signos condicionales opuestos no están demostrados por el inventario nominal de escenarios.

### 16.225.6. Dictamen

Queda cerrada la **especificación lógica de roles mínimos C1/C3**, reutilizando las clases existentes y sin expansión del roster. Quedan abiertos: materialización de cada rol en el ledger; parámetros/masas y soporte; separación formal de truth ITT, contraste G y θ_A; verificación de compatibilidad de las celdas; implementación de bounds/abstención y métricas; y cualquier calibración/dimensionamiento posterior.

**Dictamen:** MINIMUM_C1_C3_CELL_ROLES_SPECIFIED / EXISTING_WORLD_ROSTER_REUSED / CELL_LEVEL_CONFIGURATION_OPEN / ITT_G_ASSIGNMENT_AND_THETA_A_TRUTH_SEPARATION_REQUIRED / BOUNDS_ANALYZER_GAP_OPEN / NO_CODE_CHANGE / NO_CALIBRATION / NO_DATA / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** auditar la coherencia del contrato de verdad del Generator/Evaluator con los tres objetos ITT-D2, contraste G y θ_A(g_A), y definir su representación sin fugas al Analyzer. Reutilizar TruthBundle/AnalyzerResult/Evaluator existentes como artefactos a revisar; no implementar código todavía.


---

## 16.226. Gate 73 — contrato formal de los tres objetos de verdad y de la intervención focal g_A (2026-11-12)

**Precedencia:** §§16.211, 16.223, 16.225 y contrato DGP temporal/roles §§3–6. Reutiliza roster, clases de mundo, ledger y objetos de intercambio existentes. No crea mundos, no redefine Outcome/Value/V_cont, no modifica estimandos generales C10-D1 y no implementa código.

### 16.226.1. Decisión central

Se distinguen tres objetos causales, que no pueden compartir un único campo de truth ni ser intercambiados:

1. **ITT-D2 / ITT-Z:** efecto total de asignar la política D2.
2. **Contraste de asignación G bajo Z=0:** efecto de asignar G dentro del régimen Z=0. Se denomina **ITT_G|Z=0**; no se denomina efecto de accesibilidad.
3. **Efecto focal θ_A(g_A):** contraste entre dos intervenciones explícitas g_A1 y g_A0 sobre el vector completo ΔT_acc*, bajo una misma población objetivo y un mismo régimen no focal q*.

El Generator produce las tres verdades desde el mismo DGP y exógenos coherentes. El Evaluator las conserva y adjudica por separado. El Analyzer no recibe ninguna.

### 16.226.2. Definiciones contrafactuales

Sea Y_i el resultado del estimando correspondiente.

**A. Efecto total de asignación Z**

ITT_Z = E[Y_i(Z=1)] − E[Y_i(Z=0)].

Es el contraste marginal de asignación a las políticas D2, promediado sobre la distribución de G que defina el diseño factorial o sobre el régimen de G expresamente fijado. La elección debe constar en el contrato; no queda implícita. Conserva las vías causales que formen parte del paquete asignado.

**B. Contraste de asignación G dentro de Z=0**

ITT_G|Z=0 = E[Y_i(Z=0,G=1)] − E[Y_i(Z=0,G=0)].

Es un efecto de asignación/manipulación G bajo Z=0. Incluye todas las consecuencias de G: cambios efectivos en el vector, fallos de provisión, cambios en otras variables y cualquier vía directa o colateral permitida por el DGP. Su identificación por aleatorización de G requiere positividad, consistencia, ausencia de interferencia (o estimando de exposición compatible), medición y asignación válidas dentro de Z=0.

**C. Efecto focal de la intervención sobre el vector completo**

Sea A_i = ΔT_acc,i* el vector focal completo, sin reducirlo a una coordenada, a un indicador de éxito ni a la asignación G. Sean g_A1(a|h) y g_A0(a|h) dos intervenciones explícitas sobre ese vector, condicionadas por la historia basal admisible h. Sea q* la distribución objetivo común de esas historias y sea r_common el régimen no focal común que fija las condiciones no focales pertinentes.

θ_A(g_A;q*,r_common) = E_{H~q*}[ E{Y_i^{g_A1,r_common} | H} − E{Y_i^{g_A0,r_common} | H} ].

Las dos intervenciones deben especificarse como reglas sobre el vector completo, incluida su distribución conjunta, factibilidad y soporte. r_common debe ser idéntico en ambos brazos contrafactuales; no puede ocultar cambios colaterales inducidos diferencialmente. El resultado incluye los mecanismos downstream que el DGP defina como consecuencia de la accesibilidad intervenida, pero no vías ajenas al vector focal que se atribuyan indebidamente a él.

La ecuación define un estimando; no afirma que esté identificado por el diseño actual. q*, g_A1, g_A0 y r_common deben recibir identidades/versiones y definición de soporte antes de materializar una celda confirmatoria.

### 16.226.3. Relación entre ITT_G y θ_A: criterio de equivalencia

ITT_G|Z=0 = θ_A(g_A;q*,r_common) solo puede sostenerse si se acreditan conjuntamente:

- G implementa exactamente la comparación g_A1 frente a g_A0 sobre el vector completo ΔT_acc*, o existe una identificación válida que transporte del mecanismo G a esas intervenciones;
- no hay vía directa G→Y que no opere a través del vector focal intervenido;
- G no altera diferencialmente condiciones no focales ni abre vías colaterales fuera de r_common;
- el régimen no focal y la distribución objetivo son comunes y coherentes;
- existe soporte/factibilidad de ambas intervenciones en toda historia con masa positiva bajo q*;
- consistencia, versiones, medición, asignación e interferencia están resueltas.

Si cualquiera de estas condiciones falla o no puede verificarse, el contraste G conserva su identidad como ITT_G|Z=0, pero no se renombra ni se utiliza como θ_A. La salida focal será NOT_IDENTIFIED/INDETERMINATE, o PARTIALLY_IDENTIFIED únicamente cuando exista un contrato de bounds implementado y validado.

No se calcula θ_A mediante una división automática por la primera etapa de G. Un estimando local tipo Wald requeriría un contrato IV distinto, con unidad de cumplimiento, tratamiento focal, monotonicidad, exclusión, relevancia, independencia, interferencia y población local explícitos. C3/θ_A no se convierte por defecto en LATE_f.

### 16.226.4. Auditoría del Generator existente

La inspección estática de 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py (blob SHA 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4) confirma:

- potential_v está indexado como [unit][z][g];
- potential_delta_t_acc conserva cuatro coordenadas por unidad y régimen [z][g];
- itt_package_truth se calcula como contraste Z promediado sobre G;
- theta_access_truth se calcula como contraste G bajo Z=0;
- cada coordenada de delta_vector depende de g, provision_ok y umbrales exógenos; G no fuerza necesariamente un vector completo fijo;
- focal_direct_effect permite una vía directa G→resultado; R2 puede introducir una alternativa cuyo mecanismo depende de Z.

Consecuencia: el objeto actualmente denominado theta_access_truth es semánticamente ITT_G|Z=0. El nombre induce una equivalencia que el DGP no garantiza. El contraste de G puede ser válido como efecto de asignación, pero no es por ello la verdad de θ_A.

El arreglo futuro no consiste en renombrar solamente el campo. El Generator debe construir, usando el mismo DGP y exógenos comunes, la verdad contrafactual bajo g_A1 y g_A0 con r_common, además del contraste G. El mecanismo de intervención debe actuar sobre el vector completo y recomputar sus consecuencias downstream conforme a las ecuaciones del DGP. No se inventa una familia de mundos nueva: se evalúan intervenciones contrafactuales dentro de las clases existentes.

### 16.226.5. Representación lógica de los artefactos (sin implementación)

**TruthBundle** debe conservar campos semánticamente separados:

- itt_z_truth + definición del régimen G marginal/condicional y población;
- itt_g_z0_truth + definición de la asignación G y régimen Z=0;
- theta_a_truth + IDs/versiones de g_A1, g_A0, q*, r_common, vector focal, horizonte y población;
- potenciales o referencias reproducibles suficientes para auditar cada contraste, incluyendo resultados bajo las intervenciones focales;
- provenance, DGP/config/version y vínculo con el mismo run_id.

Los nombres actuales itt_package_truth y theta_access_truth no se aceptan como contrato final sin esta desambiguación. La migración/aliasado será explícita y versionada; no se sobrescriben silenciosamente significados históricos.

**AnalyzerResult** debe separar, por estimando:

- itt_z_estimate/status/uncertainty;
- itt_g_z0_estimate/status/uncertainty;
- theta_a_estimate/status/uncertainty, solo si evidencia y contrato permiten identificarlo;
- razones de abstención y soporte por estimando, sin derivar el estado de uno a partir de otro.

El Analyzer no recibe TruthBundle, potenciales, parámetros ocultos, semillas ni etiquetas de celda. Que el contrato visible describa g_A no le revela la verdad del DGP.

**Evaluator** abre truth únicamente después del sellado del AnalyzerResult y compara cada salida con su propia verdad, sin sustituir una por otra. Debe detectar la atribución falsa ITT_G|Z=0 → θ_A, la estimación puntual focal sin identificación y la abstención indebida en controles positivos identificables.

### 16.226.6. Consecuencias para las celdas Gate 71

No se añaden celdas ni clases. Se precisan las verdades que deben figurar en las celdas ya definidas:

- C1-POS/NULL/NEG/HET/ABSTAIN se adjudican contra itt_z_truth.
- C3-POS/NULL/NEG/HET/ABSTAIN se adjudican contra theta_a_truth, nunca contra itt_g_z0_truth por defecto.
- C1-DECOUPLED debe mantener itt_z_truth no nulo y theta_a_truth nulo o no identificable, con itt_g_z0_truth registrado aparte.
- Debe conservarse al menos un contraste en que la primera etapa de G sobre el vector focal sea nula y el ITT-Z no nulo por una vía de paquete no focal, si la clase existente y sus rangos admitidos lo permiten.
- Una vía directa de G o una modificación diferencial de la rama no focal debe producir desacoplamiento/no-identificación focal, no una θ_A espuria.
- La heterogeneidad se conserva por historia/estrato y como efecto marginal bajo q*; no se valida solo por el promedio.

### 16.226.7. Dictamen y límites

**Cerrado en este gate:** contrato semántico de los tres objetos de verdad; definición contrafactual de θ_A sobre el vector completo; criterio de equivalencia entre ITT_G y θ_A; diagnóstico del campo mal denominado en el harness; representación lógica mínima y reglas de firewall.

**Sigue abierto:** elección/versionado de g_A1/g_A0, q* y r_common; materialización de potenciales focales en TruthBundle; definición de estimadores y condiciones observables de identificación; bounds/identificación parcial; soporte por historia; mapping de celdas a parámetros; pruebas de Analyzer/Evaluator. No se declara identificación ni diseño congelado.

**Dictamen:** THREE_TRUTH_OBJECTS_SEMANTICALLY_SEPARATED / THETA_A_DEFINED_AS_FULL_VECTOR_INTERVENTION / CURRENT_G_CONTRAST_NOT_EQUIVALENT_BY_DEFAULT / GENERATOR_EVALUATOR_REPRESENTATION_SPECIFIED / CELL_PARAMETERIZATION_OPEN / BOUNDS_OPEN / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 74 — traducir estas definiciones a un contrato de potenciales y estimadores verificable por escenario: especificar qué observaciones/variación identifican cada uno de ITT-Z, ITT-G|Z=0 y θ_A; qué condiciones se verifican con evidencia observable; y cuándo la salida obligatoria es abstención. No implementar todavía el estimador ni ampliar el roster.


---

## 16.227. Gate 74 — contrato de identificación observable, supuestos y abstención por estimando (2026-11-12)

**Precedencia:** §§16.211, 16.218, 16.223, 16.225–16.226; contrato DGP temporal/roles §§2, 6–8; reconciliación D2 de población/asignación/soporte. Reutiliza clases, ledger, Generator, Projector, Sealer, Analyzer y Evaluator existentes. No añade mundos, no reabre Value/V_cont, no implementa estimadores/bounds y no autoriza ejecución.

### 16.227.1. Regla epistemológica

Una condición de identificación declarada en AnalysisContract no constituye evidencia de que se haya cumplido. El Analyzer solo puede utilizar evidencia observada/proyectada y sellada, un contrato público versionado y certificados/registros de diseño verificables incluidos en el canal permitido. No puede recibir truth del Generator, parámetros estructurales ocultos, potenciales, semilla del Generator ni etiquetas de celda.

El Evaluator puede contrastar después los supuestos verdaderos del DGP con los certificados/evidencia que vio el Analyzer, puntuando falsa identificación, abstención correcta y abstención excesiva.

Cada condición se clasifica como:
- **OBSERVABLE/VERIFICABLE:** comprobable con el registro disponible, dentro de su alcance.
- **DECLARADA, NO VERIFICADA:** aparece en el contrato sin certificado/evidencia suficiente.
- **SUPUESTO NO TESTABLE DESDE LOS DATOS:** requiere garantía del diseño/DGP o sensibilidad.
- **FALLIDA:** evidencia válida contradice la condición.
- **DESCONOCIDA:** no existe evidencia suficiente para decidir.

DESCONOCIDA nunca se convierte en cumplida. Un hash acredita integridad del artefacto sellado, no aleatorización, ausencia de interferencia ni validez causal.

### 16.227.2. ITT-Z — efecto total de asignación D2

**Objeto:** ITT_Z de §16.226.2.A, con régimen de G marginal/condicional expresamente versionado.

**Identificación puntual requiere:** asignación Z válida en la UA declarada; positividad de Z por estrato/historia de la población objetivo; consistencia de política/versiones; interferencia ausente o estimando de exposición compatible; Outcome y seguimiento medidos en el horizonte; mecanismo de ausencia identificado si hay missingness; población, UA, pesos y distribución de G fijados ex ante.

**Verificable por Analyzer:** presencia/dominio de Z; conteos por brazo y estrato; probabilidades registradas; bloques cuando el protocolo los exige; versiones/desviaciones; cobertura de Outcome/seguimiento; clusters y mapa de exposición si se suministran; integridad del sello.

**No demostrado por los datos por sí solos:** balance basal no prueba aleatorización; probabilidades registradas no prueban ejecución correcta del algoritmo; no detectar spillovers no prueba ausencia de interferencia; completitud observada no prueba que la ausencia sea ignorable.

**Estimador candidato:** diferencia de medias por Z para aleatorización individual simple; estimador ponderado conforme al mecanismo en diseños estratificados/bloqueados; inferencia al nivel de UA si la asignación es por cluster. El régimen G marginal debe coincidir con el objetivo declarado; no se supone 50/50 salvo contrato explícito.

**Abstención:** NOT_IDENTIFIED si el diseño/evidencia contradice una condición necesaria (p. ej., positividad estructural fallida o asignación no aleatoria para el estimando causal propuesto); INDETERMINATE si aleatorización, interferencia, Outcome, seguimiento o ausencia quedan declarados pero no verificables, o la información es insuficiente. No etiquetar como ITT identificado una mera diferencia de medias.

### 16.227.3. ITT-G|Z=0 — efecto de asignación G bajo Z=0

**Objeto:** ITT_G|Z=0 de §16.226.2.B; no es θ_A.

**Identificación puntual requiere:** asignación G aleatoria/condicionalmente aleatoria dentro de Z=0 conforme al protocolo; positividad de G por historia objetivo dentro de Z=0; consistencia/versiones de G; interferencia ausente o exposición compatible; Outcome/seguimiento medidos; población y estandarización declaradas.

**Verificable por Analyzer:** G observado y válido; conteos G=0/1 dentro de Z=0 y por estrato; probabilidades/protocolo registrados; celdas vacías; versiones, cumplimiento y contaminación documentados; Outcome y ausencia por brazo.

**No demostrado:** diferencias del vector focal no prueban aleatorización G; primera etapa no prueba exclusión; balance basal no prueba ausencia de confusión; no observar vía directa no prueba que no exista.

**Estimador candidato:** contraste de Outcome entre G=1 y G=0 restringido a Z=0, respetando estratos/bloques y población objetivo. Si G se asigna por cluster o hay interferencia, se requiere estimando e inferencia compatibles. La primera etapa se informa por separado para cada coordenada y para el vector completo; no se sustituye por W_attempt o C_dep*.

**Abstención:** NOT_IDENTIFIED ante asignación G no aleatoria para el contraste causal, positividad estructural fallida o versiones incompatibles; INDETERMINATE ante protocolo no verificable, interferencia no resuelta, Outcome/missingness no identificado o soporte muestral insuficiente. El contraste descriptivo puede informarse como tal, sin etiqueta causal.

### 16.227.4. θ_A — intervención sobre el vector completo ΔT_acc*

**Objeto:** θ_A(g_A;q*,r_common) de §16.226.2.C. Su identificación no se hereda de ITT-Z ni de ITT-G.

**Rutas admisibles, a elegir y especificar antes de analizar:**

- **A — intervención focal aleatorizada directamente:** asignación que implementa g_A1/g_A0 sobre el vector completo, con versiones/consistencia, soporte por historia, q* y r_common comunes, Outcome medido y ausencia/interferencia resueltas. La intervención manipula el vector definido; no es solo ofrecer una provisión que puede fallar.
- **B — G como instrumento/encouragement:** requiere contrato IV separado: tratamiento focal, primera etapa pertinente, independencia, exclusión, monotonicidad cuando proceda, consistencia, interferencia y población estimanda local. No identifica automáticamente el ATE poblacional θ_A; podría identificar otro efecto local.
- **C — identificación observacional/secuencial:** requiere historia suficiente, intercambiabilidad condicional secuencial, medición de confusores mediador–Outcome, positividad y método longitudinal preespecificado. No está disponible por defecto.

**Verificable por Analyzer:** existencia de asignación/intervención focal observada; distribución y soporte empírico del vector por historia; positividad muestral; versiones; medición de coordenadas/cobertura; q* y r_common públicos/versionados; balance según diseño; primera etapa vectorial estimable; ruta declarada y certificados disponibles.

**No verificable solo con datos observados:** exclusión de vías directas G→Outcome; ausencia de rutas colaterales ocultas; ausencia de confusión no medida; equivalencia causal G=g_A; régimen no focal realmente común en contrafactuales; ausencia de interferencia no medida. Requieren garantía del diseño/DGP, auditoría del mecanismo o sensibilidad. No se satisfacen por flags booleanos.

**Estado del harness actual:** G cambia probabilísticamente las coordenadas de ΔT_acc* mediante provisión/umbrales; no garantiza asignación directa del vector completo. El Analyzer estima un contraste G bajo Z=0 y lo etiqueta focal mediante flags de exclusión/régimen común. Según Gate 73, eso es ITT_G|Z=0, no θ_A por defecto. No hay ruta implementada de intervención directa g_A ni contrato IV completo. El Analyzer actual no puede emitir IDENTIFIED para θ_A con la evidencia/contrato presentes; debe abstenerse de la atribución focal e informar ITT_G como estimando separado cuando sus condiciones propias estén acreditadas.

### 16.227.5. Soporte, positividad y población objetivo

La positividad se evalúa respecto de la intervención y unidad correctas:
- ITT-Z: probabilidad positiva de ambos brazos Z en cada estrato/historia con masa positiva.
- ITT-G|Z=0: probabilidad positiva de ambos brazos G dentro de Z=0 y cada estrato relevante.
- θ_A: factibilidad/soporte de g_A1 y g_A0 sobre el vector completo para cada historia con masa positiva bajo q*.

Distinguir:
1. **Fallo estructural:** brazo/intervención imposible en una historia; falla identificación del estimando original.
2. **Soporte observado vacío/escaso:** puede ser insuficiencia muestral o señal de violación; no se declara fallo estructural sin conocer el mecanismo, pero no se extrapola.
3. **Soporte desconocido:** abstención o bounds solo si están formalizados.

No se restringe silenciosamente q* a la intersección observada. Una población de solapamiento define otro estimando y debe declararse ex ante.

### 16.227.6. Ausencia, medición e inferencia

- Missingness de Outcome/covariables: registrar completitud, censura, motivo y brazo; nunca recodificar como cero. MAR/MCAR u otro mecanismo requiere declaración y justificación; los datos no prueban el supuesto por sí solos.
- Error de medida de ΔT_acc*: requiere matriz de error/calibración identificada o medición ideal respaldada por protocolo. Sin ello, no sustituir vector verdadero por proxy observado ni declarar θ_A identificado.
- Incertidumbre: estimación puntual no equivale a recuperación. Reportar error estándar/intervalo compatible con diseño; inferencia por cluster si UA es cluster y varianza que respete estratos/bloques. Cobertura/calibración se evalúan sobre repeticiones del benchmark, no en un único run.
- N pequeño, celdas vacías o grados de libertad insuficientes producen INDETERMINATE, no intervalos artificialmente precisos.

### 16.227.7. Taxonomía obligatoria de salida

Por estimando:
- **IDENTIFIED:** ruta preespecificada y evidencia/protocolo suficiente; estimación e incertidumbre compatibles con diseño.
- **PARTIALLY_IDENTIFIED:** solo con conjunto identificado/bounds, supuestos, fórmula, cobertura y algoritmo implementados y validados. No disponible en el harness integrado actual.
- **NOT_IDENTIFIED:** evidencia/diseño contradice una condición necesaria o demuestra violación estructural.
- **INDETERMINATE:** no puede decidirse si las condiciones se cumplen; soporte, medición, seguimiento o certificados insuficientes.
- **DESCRIPTIVE_ONLY:** contraste calculable sin garantías causales; etiqueta descriptiva, nunca efecto identificado.

Puntuación separada:
- abstención correcta cuando falta identificación;
- falsa identificación cuando se emite IDENTIFIED y falla la ruta causal;
- abstención excesiva en control positivo identificable;
- falsa atribución focal al etiquetar ITT-G como θ_A;
- bounds improcedentes sin conjunto identificado formal y validación.

### 16.227.8. Diagnóstico del código existente y brechas

La inspección estática de vcont_integrated_harness.py (blob 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4) muestra:
- AnalysisContract transporta booleanos (randomized_z/g, positivity, no_interference, measurement_identified, version_consistency, focal_direct_path_absent, common_nonfocal_regime) que el Analyzer trata como condiciones satisfechas sin verificar procedencia/certificado.
- Los registros observados incluyen Z/G, estrato, cluster, S3, vector focal observado y versión; no incluyen protocolo completo de asignación, probabilidades individuales, bloques/semillas de asignación, certificados de consistencia ni mapa completo de exposición.
- El Analyzer calcula ITT-Z por diferencia de medias por Z y contraste G dentro de Z=0; el segundo se etiqueta focal si pasan los flags.
- positivity es global; no se comprueba por historia/estrato ni para el vector completo.
- Se usan errores estándar de medias independientes; no se adapta inferencia a clusters/estratos. Interferencia no resuelta causa abstención, pero no existe estimador cluster/exposición.
- El Outcome S3 es un proxy sintético del harness; estas reglas no acreditan Outcome/Value general TGCV.
- Truth conserva potenciales Z×G, pero no potenciales separados bajo g_A1/g_A0. Evaluator compara el resultado focal con theta_access_truth, que Gate 73 identifica como ITT_G|Z=0.

**Brecha:** el contrato de entrada confunde declaración con verificación y no separa condiciones observables, certificadas, asumidas y desconocidas. No se corrige en este gate.

### 16.227.9. Dictamen y dependencias

**Cerrado:** reglas de identificación por estimando; separación entre verificaciones observables, garantías de diseño y supuestos no testables; soporte por población/intervención; taxonomía de abstención; diagnóstico de insuficiencia del AnalysisContract actual.

**Abierto antes de implementar:** (a) protocolo/certificados de asignación y unidad/estratos/interferencia; (b) observación/sellado de Outcome, vector focal, ausencia y versiones; (c) ruta de identificación de θ_A —intervención directa g_A o contrato IV/longitudinal independiente—; (d) q*, r_common y soporte por historia; (e) estimadores/varianzas por UA/estrato; (f) bounds antes de habilitar PARTIALLY_IDENTIFIED; (g) mapping de roles Gate 71 a condiciones/salidas sin ampliar roster.

**Dictamen:** ESTIMAND_SPECIFIC_IDENTIFICATION_RULES_DEFINED / CONTRACT_FLAGS_NOT_EVIDENCE / ITT_Z_AND_ITT_G_REQUIRE_DESIGN_CERTIFICATION / THETA_A_NOT_IDENTIFIED_BY_CURRENT_G / SUPPORT_AND_INTERFERENCE_CHECKS_INCOMPLETE / BOUNDS_NOT_IMPLEMENTED / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 75 — reconciliar el ledger de celdas C1/C3 con las condiciones de identificación y las salidas de Gate 74: para cada rol existente, asignar ruta identificante, condiciones observables/certificadas/no testables, verdad separada y comportamiento Analyzer/Evaluator exigido. No crear escenarios ni parámetros; no implementar ni ejecutar.


---

## 16.228. Gate 75 — reconciliación operativa del ledger de celdas C1/C3 (2026-11-13)

**Precedencia:** §§16.211–16.225 y, en particular, ledger estructural §16.223, roles mínimos §16.225, contrato de tres verdades §16.226 y reglas de identificación/abstención §16.227. Este gate no crea mundos, mecanismos, estimandos ni parámetros. Convierte los doce roles existentes en requisitos de ledger y adjudicación. No reabre Value/V_cont, C2, C4 ni LATE_f.

### 16.228.1. Resultado de reconciliación

Los doce roles quedan vinculados a tres verdades separadas:
- **C1:** itt_z_truth (efecto total de asignación D2/Z).
- **Registro auxiliar común:** itt_g_z0_truth (contraste de asignación G bajo Z=0); se registra cuando el diseño contiene G, pero nunca sustituye la verdad C1 o C3.
- **C3:** theta_a_truth (intervención explícita g_A1 frente a g_A0 sobre el vector completo ΔT_acc*, bajo q* y r_common).

Cada celda conserva los campos del ledger §16.223.2. Este mapping añade únicamente la relación entre cell_role, estimand_id, verdad adjudicadora, ruta de identificación, evidencia permitida, condición no testable, salida Analyzer y aserción Evaluator. No se duplican population_id, assignment_id, intervention_id, support_status, interference_status, observation_profile ni firewall: se referencian sus valores en el ledger primario.

### 16.228.2. Matriz mínima de adjudicación de las doce celdas

| Cell role | Estimand / truth adjudicadora | Reutilización de clase existente y contraste requerido | Ruta y condiciones de identificación | Analyzer exigido | Evaluator exigido |
|---|---|---|---|---|---|
| C1-POS | C1 / itt_z_truth > 0 | Focal limpio R0; D2/Z frente a control bajo régimen G marginal/condicional fijado | Ruta ITT-Z de §16.227.2; UA, protocolo/certificado Z, positividad por estrato, consistencia/versiones, Outcome y seguimiento; interferencia resuelta | IDENTIFIED solo con evidencia/protocolo suficiente; estimación e incertidumbre conforme a UA/estratos | Puntuar signo, error y cobertura frente a itt_z_truth; detectar abstención excesiva |
| C1-NULL | C1 / itt_z_truth = 0 | Clase Nulo; efecto total Z cero, sin imponer theta_a_truth=0 ni primera etapa nula | Misma ruta ITT-Z identificante que C1-POS; control nulo no significa falta de precisión ni ausencia de asignación | Estimar ITT-Z; no fabricar señal. Estado de identificación depende del diseño, no del valor verdadero; no declarar “demostrado nulo” solo porque el intervalo incluya cero | Evaluar sesgo/error tipo I y compatibilidad con truth cero sobre repeticiones; separar falta de potencia de error de identificación |
| C1-NEG | C1 / itt_z_truth < 0 | Focal adverso o mecanismo directo/colateral ya presente en roster; efecto total D2/Z negativo | Misma ruta ITT-Z identificante que C1-POS; no condicionar por cumplimiento ni mediadores post-Z | IDENTIFIED con signo negativo si canal y diseño lo permiten; incertidumbre válida | Puntuar signo, magnitud y cobertura contra itt_z_truth |
| C1-DECOUPLED | C1 / itt_z_truth distinto de cero; registrar aparte theta_a_truth nulo o no identificado según submecanismo | Vía directa D2→Outcome y/o clase R2 colateral existente; conservar también itt_g_z0_truth | ITT-Z puede seguir identificado por su propia aleatorización; ruta focal exige g_A/r_common. Si rama no focal diferencial no separable, C3 no identificado | Recuperar ITT-Z total sin rebautizarlo como focal; no emitir inferencia de theta_A derivada de ITT-Z o G | Detectar falsa atribución focal; confirmar que ITT incluye la vía de paquete; adjudicar C3 con theta_a_truth y su estado propio |
| C1-HET | C1 / itt_z_truth(h) con signos opuestos; registrar itt_z_truth marginal bajo q* o población ITT predefinida | Clase Interacción/heterogeneidad; historias/estratos ya previstos con masa positiva | Ruta ITT-Z con asignación y soporte dentro de cada estrato; q*/pesos y escala de interacción predeclarados; no extrapolar | Informar efectos condicionales y marginal; no reducir a promedio ni inferir signos fuera del soporte | Comparar efectos condicionales y marginal con truth y masas; detectar inversión/ocultación por agregación |
| C1-ABSTAIN | C1 / truth DGP conservada, identificación NOT_IDENTIFIED o INDETERMINATE | Clase existente de interferencia, soporte, ausencia/censura u observación adversarial; activar condición ya contemplada | Ruta ITT-Z falla estructuralmente o queda no verificable según §16.227.2; distinguir positividad estructural fallida de soporte muestral insuficiente | Abstenerse del ITT causal puntual: NOT_IDENTIFIED si violación demostrada; INDETERMINATE si desconocida. DESCRIPTIVE_ONLY opcional | Puntuar abstención correcta, falsa identificación y descripción correctamente etiquetada; no premiar abstención si el escenario resulta identificable |
| C3-POS | C3 / theta_a_truth > 0 | Focal limpio R0; intervención directa g_A1 vs g_A0 sobre vector completo, sin usar G como sustituto | Ruta A de §16.227.4: intervención focal representada en el diseño DGP, q* común, ambas políticas factibles/con soporte por historia, r_common acreditado, Outcome/medición e interferencia resueltos | IDENTIFIED solo si ruta A y evidencia permitida están representadas. El harness actual no satisface esta precondición y debe abstenerse, no usar itt_g_z0 | Comparar θ_A estimado con theta_a_truth; verificar vector completo, régimen y soporte; puntuar abstención excesiva solo cuando ruta A esté disponible |
| C3-NULL | C3 / theta_a_truth = 0; itt_z_truth y primera etapa pueden ser no nulos | Nulo focal; mecanismo de Outcome no responde a la intervención focal, manteniendo las demás funciones comunes | Misma ruta A identificante que C3-POS; nulidad de θ_A no exime de identificación, soporte ni medición | Estimar bajo ruta focal; no usar ITT-Z/ITT-G como proxy. Distinguir estimación imprecisa de identificación fallida | Puntuar error tipo I/calibración frente a theta_a_truth=0; comprobar que no se fuerza itt_z_truth=0 ni first-stage=0 |
| C3-NEG | C3 / theta_a_truth < 0 | Focal adverso existente; intervención sobre vector completo con efecto focal negativo | Misma ruta A identificante que C3-POS; q*, r_common, soporte y medición compatibles | Recuperar signo negativo solo si vector e intervención son identificables; de lo contrario abstenerse | Puntuar signo, error y cobertura contra theta_a_truth |
| C3-DECOUPLED | C3 / dos verdades: (a) theta_A=0 con ITT-Z no nulo; (b) theta_A no identificable por vía no focal diferencial | Vía directa D2→Outcome y R2 colateral existentes. Son dos subcasos de adjudicación del mismo rol, no nuevas clases | (a) ruta A focal identificable con r_common y theta_A nulo; (b) r_common_status=DIFFERENTIAL_UNRESOLVED o exclusión fallida: no identificación puntual focal | En (a), estimar theta_A=0 por ruta A y no atribuirle ITT; en (b), abstenerse o bounds solo si implementados. Nunca absorber vía directa/colateral | Verificar por separado nulo focal y no identificación; detectar contaminación de theta_A por ITT/G y falsos bounds |
| C3-HET | C3 / theta_a_truth(h) con signos opuestos y verdad marginal bajo q* | Interacción/heterogeneidad existente; historias con masa positiva y respuesta focal distinta | Ruta A y soporte de ambas g_A en cada historia; q* predeclarado y r_common común condicional a historia | Informar condicionales y marginal, con incertidumbre y sin extrapolación; no inferir heterogeneidad desde promedio solo | Puntuar signo/estimación por historia y promedio ponderado; detectar ocultación por cancelación |
| C3-ABSTAIN | C3 / theta_A no identificable o, en futuro, conjunto parcialmente identificado formal | Clases existentes de soporte/factibilidad, r_common diferencial, interferencia, medición o canal no identificante | Ruta A ausente/fallida/no verificable, o IV/secuencial solo si contrato distinto se aprueba. Bounds no disponibles hasta contrato y validación | Ahora: NOT_IDENTIFIED si fallo estructural demostrado o INDETERMINATE si condición desconocida. No emitir PARTIALLY_IDENTIFIED sin algoritmo/bounds implementados y validados | Comprobar razón de abstención; penalizar falsa identificación y bounds inventados; evaluar cobertura de bounds solo tras habilitación formal |

### 16.228.3. Reglas transversales del ledger

1. **Una fila por rol y versión de celda.** Las doce filas son roles mínimos, no doce nuevos mundos. world_id/version referencia §16.211; los subcasos (a)/(b) de C3-DECOUPLED quedan como variantes de adjudicación dentro de la clase existente, no como familias nuevas.
2. **Truth no es información del Analyzer.** itt_z_truth, itt_g_z0_truth, theta_a_truth, potenciales, parámetros generadores y etiquetas de celda permanecen en Generator/Evaluator. El Analyzer recibe solo observaciones selladas, contrato público y certificados permitidos.
3. **Tres verdades en toda celda donde procedan.** Registrar las tres aunque alguna sea NOT_APPLICABLE, explicando por qué. NOT_APPLICABLE no significa cero. Nunca inferir una verdad desde otra.
4. **Cero exacto y recuperación estadística son distintos.** El DGP puede estipular verdad exactamente cero; el Analyzer no “demuestra” un cero por un p-valor no significativo o un intervalo que contiene cero. La aceptación se evalúa con error, incertidumbre, calibración y repeticiones según criterios preexistentes §16.219; no se fijan tolerancias nuevas aquí.
5. **Signo y heterogeneidad tienen escala y población.** El signo se refiere a Outcome ya fijado y al contraste/población declarados. C1 usa población ITT pre-Z; C3 usa q*. No intercambiar masas q*, probabilidades pi_h ni pesos del benchmark.
6. **Primera etapa separada.** Registrar primera etapa de G sobre cada coordenada y sobre el vector completo; no confundirla con theta_A, ITT-Z ni el efecto de Outcome.
7. **Soporte y r_common se heredan, no se presumen.** Cada celda debe rellenar support_status, r_common_status, interference_status, assignment_id, intervention_id y analyzer_information conforme a §16.223. La omisión no equivale a COMMON_FIXED ni IDENTIFIED.
8. **C1 y C3 se adjudican por separado.** La misma configuración puede producir ITT-Z identificado y θ_A no identificado; es un resultado válido y necesario para probar que Analyzer no colapsa estimandos.

### 16.228.4. Brechas de representación y materialización detectadas

La reconciliación documental cierra el mapping lógico, pero no la cobertura efectiva. Permanecen brechas concretas:
- El ledger §16.223 define los campos, pero no contiene todavía doce registros de celda versionados con población, UA, probabilidades, g_A, masas q*, soporte, r_common, perfil de observación y truth.
- El roster R0/R1/R2/R3 y los mecanismos existentes son candidatos, no acreditación de que cada signo/nulo/heterogeneidad sea factible dentro de los rangos admitidos.
- No está demostrado un control C3-POS/C3-NULL/C3-NEG identificable: falta ruta A materializada de intervención directa sobre el vector completo.
- C1-HET y C3-HET requieren al menos dos historias con masas positivas, signos condicionales opuestos y estimación/soporte por historia; la etiqueta nominal “heterogeneity” no basta.
- El desacoplamiento de primera etapa vectorial nula con ITT-Z no nulo debe verificarse en el DGP existente antes de afirmar cobertura; no se crea clase adicional.
- PARTIALLY_IDENTIFIED continúa deshabilitado como salida válida hasta formalizar e implementar bounds y validar su cobertura.
- AnalysisContract como flags booleanos no satisface el canal de certificados/evidencia de §16.227; no se sustituye por flags con nombres nuevos.

### 16.228.5. Criterio de cierre y dictamen

Gate 75 queda cerrado como reconciliación documental cuando las doce filas, sus verdades y reglas Analyzer/Evaluator quedan especificadas en este apartado. No se declara que las celdas estén materializadas, sean factibles, identificadas por el harness actual o hayan sido ejecutadas.

**Cerrado:** mapping unívoco de C1/C3 a itt_z_truth/theta_a_truth; registro auxiliar itt_g_z0_truth; condiciones de identificación por rol; conducta Analyzer/Evaluator; reglas transversales del ledger y brechas concretas.

**Abierto:** creación de los doce registros versionados dentro del ledger existente; factibilidad de signos/nulos/masas dentro del roster; ruta A para θ_A; certificados de asignación; soporte por historia; parámetros y perfiles de observación; bounds; pruebas de Analyzer/Evaluator.

**Dictamen:** C1_C3_TWELVE_ROLE_LEDGER_MAPPING_CLOSED / THREE_TRUTH_ADJUDICATION_PRESERVED / EXISTING_ROSTER_ONLY / CELL_RECORDS_NOT_MATERIALIZED / THETA_A_DIRECT_IDENTIFICATION_ROUTE_MISSING / HETEROGENEITY_AND_DECOUPLING_FEASIBILITY_UNVERIFIED / BOUNDS_NOT_ENABLED / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 76 — comprobar la factibilidad lógica de las doce celdas contra las funciones generadoras y rangos admitidos del roster §§16.211–16.212, usando la cuadrícula y los mecanismos ya existentes. Resolver contradicciones e imposibilidades; no asignar cifras ni crear clases nuevas. No implementar ni ejecutar.


---

## 16.229. Gate 76 — auditoría de factibilidad lógica de las doce celdas frente al Generator existente (2026-11-13)

**Precedencia:** §§16.211–16.212, 16.223–16.228 y código 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py, blob 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4. Este gate es una auditoría estática de representabilidad algebraica/estructural. No ejecuta el Generator, no asigna parámetros, no crea clases ni escenarios, no modifica código y no autoriza simulación. No reabre Value/V_cont ni C4/LATE_f.

### 16.229.1. Criterio de factibilidad

Se distinguen cuatro resultados que no deben colapsarse:

- **REPRESENTABLE:** las variables y la intervención requeridas existen en el modelo generador y la estructura permite construir la verdad solicitada.
- **REPRESENTABLE_CONDITIONALLY:** la estructura contiene una ruta candidata, pero su signo, soporte, no saturación, masas o compatibilidad requieren una configuración admisible aún no especificada.
- **NOT_REPRESENTABLE:** falta una variable/intervención/potencial indispensable o la función generadora actual impone una restricción incompatible.
- **NOT_DEMONSTRATED:** la función permite una hipótesis plausible, pero no se ha demostrado que alcance el patrón requerido dentro de los dominios y restricciones vigentes.

REPRESENTABLE no significa materializada, identificada por Analyzer, estadísticamente recuperable ni ejecutada. La inspección no usa simulación ni selecciona cifras.

### 16.229.2. Hallazgos estructurales del código

La inspección estática confirma:

1. ScenarioConfig contiene randomized_z, randomized_g, positivity, no_interference, perfiles R0–R3 y coeficientes para efecto focal, directo de paquete, directo de G, colateral, heterogeneidad y provisión.
2. El Generator construye z_assign y g_assign balanceados; randomized_z/randomized_g se validan como booleanos requeridos, pero no contienen por sí mismos un protocolo/certificado de asignación ni probabilidades por estrato.
3. Los potenciales de Outcome están indexados exclusivamente [unit][z][g]. Las cuatro coordenadas de potential_delta_t_acc también se indexan por (z,g).
4. delta_vector se activa mediante G y provision_ok; no existe una función de asignación directa g_A1/g_A0 sobre el vector completo ni potenciales separados Y(g_A1,r_common) / Y(g_A0,r_common).
5. theta_access_truth se calcula como media de V(z=0,g=1)-V(z=0,g=0). Es ITT_G|Z=0, no θ_A. El nombre del campo no cambia el estimando.
6. itt_package_truth promedia para cada Z los potenciales G=0 y G=1 con peso 1/2. El régimen marginal G=50/50 queda así implícito en el código de verdad, sin un g_regime_id/peso versionado explícito en ScenarioConfig/manifest. No se debe generalizar ese ITT a otro régimen G sin corregir y versionar el contrato.
7. focal_access_effect opera sobre trajectory; package_direct_effect sobre Z; focal_direct_effect sobre G; collateral_effect sobre Z × alternative; heterogeneity modula el efecto de trajectory según x. El resultado profile_match_p se trunca a [0,1], restricción que puede saturar y alterar los signos/magnitudes efectivos.
8. En R3, la provisión cambia con Z mediante una regla fija de reducción; R2 cambia la probabilidad de alternativa con Z; R1 fija la alternativa. La asignación de peers entra cuando se activa interferencia.
9. La validación exige randomized_g=True para todo benchmark, aunque C1/ITT-Z no requiere por definición que G sea aleatorizado si el régimen marginal de G está fijado de otra forma. El harness actual no representa esa flexibilidad; su requisito no debe confundirse con una necesidad causal universal de C1.

### 16.229.3. Matriz de factibilidad por celda

| Celda | Verdad requerida | Dictamen frente al Generator actual | Motivo y límite |
|---|---|---|---|
| C1-POS | ITT-Z positivo | **REPRESENTABLE_CONDITIONALLY** | package_direct_effect, R3/provisión o R2/colateral pueden abrir rutas Z→V_cont. Falta fijar una configuración admisible no saturada, el régimen G explícito y verificar signo/soporte. |
| C1-NULL | ITT-Z exactamente cero, sin imponer θ_A ni primera etapa nulos | **REPRESENTABLE_CONDITIONALLY** | R0 con ramas Z no focales inactivas permite ausencia estructural de efecto Z sobre V_cont mientras G/ΔT_acc puede variar. La igualdad exacta de la verdad poblacional debe comprobarse algebraicamente/configurarse; una muestra con diferencia cero no basta. |
| C1-NEG | ITT-Z negativo | **REPRESENTABLE_CONDITIONALLY** | La función admite coeficientes directos de paquete con signo adverso y rutas R2/R3. El signo efectivo depende de la suma de vías y del truncamiento [0,1]; no está demostrado con los dominios configurados. |
| C1-DECOUPLED | ITT-Z no nulo y θ_A nulo o no identificado | **REPRESENTABLE_CONDITIONALLY para el desacoplamiento de paquete; NO REPRESENTABLE como verdad θ_A completa** | La vía directa Z→V_cont puede separarse de la ruta G/ΔT. Pero el Generator no dispone de potenciales θ_A; solo puede registrar ITT_G|Z=0. No puede adjudicar que θ_A sea cero. |
| C1-HET | Efectos ITT-Z condicionales de signos opuestos por historia | **NOT_DEMONSTRATED** | heterogeneity modula trajectory, pero no introduce directamente una interacción Z×H. R3 puede hacer que Z cambie provisión/trajectory y activar una diferencia condicional por x; la inversión de signos requiere demostrarse dentro de los límites y sin saturación. No contar el parámetro nominal como cobertura. |
| C1-ABSTAIN | Condición ITT-Z necesaria ausente/no verificable | **REPRESENTABLE_CONDITIONALLY** | Interferencia activa y medición incompleta permiten escenarios de abstención/indeterminación. La positividad implementada afecta G, no acredita fallo estructural de positividad Z. La razón exacta de abstención debe corresponder a la condición efectivamente activada. |
| C3-POS | θ_A positivo bajo g_A1/g_A0 sobre vector completo | **NOT_REPRESENTABLE** | No existen asignaciones/intervenciones g_A ni potenciales separados. El contraste G positivo no satisface el requisito. |
| C3-NULL | θ_A exactamente cero, sin imponer ITT-Z/primera etapa nulos | **NOT_REPRESENTABLE** | Se puede anular el contraste G o el efecto de trayectoria, pero no establecer la verdad del estimando θ_A definido por intervención directa. |
| C3-NEG | θ_A negativo bajo g_A1/g_A0 | **NOT_REPRESENTABLE** | Un focal_access_effect negativo cambia el resultado vía trayectoria bajo G; no crea el contraste contrafactual g_A. |
| C3-DECOUPLED | ITT-Z no nulo con θ_A nulo, o θ_A no identificable por vía diferencial | **NOT_REPRESENTABLE como verdad C3** | El componente directo Z y los canales G/colaterales permiten desacoplar ITT-Z de ITT_G|Z=0. No permiten declarar el valor/estado de θ_A sin potenciales g_A. |
| C3-HET | θ_A condicional con signos opuestos y promedio bajo q* | **NOT_REPRESENTABLE** | El término heterogeneity puede modular el contraste G por x, pero no existen g_A potenciales, q* ni r_common materializados. No es una celda C3 aunque produzca heterogeneidad de ITT_G. |
| C3-ABSTAIN | θ_A no identificado/indeterminado por falta de ruta/soporte/evidencia | **REPRESENTABLE como prueba de abstención requerida; comportamiento actual NO ACREDITADO** | El contrato Gate 74 exige abstención focal porque G no acredita θ_A. Los flags actuales del Analyzer pueden tratar declaraciones como condiciones satisfechas; la abstención correcta requiere corrección y prueba posterior, no se da por implementada. |

### 16.229.4. Contradicciones y correcciones de contrato que quedan fijadas

**A. Tres verdades no equivalentes.** El campo histórico theta_access_truth del harness contiene ITT_G|Z=0. Debe considerarse nombre/semántica legacy incorrecta respecto de C3; no se copia a theta_a_truth. En una futura revisión de código se mantendrán campos independientes itt_z_truth, itt_g_z0_truth y theta_a_truth, este último solo cuando se implementen los potenciales g_A.

**B. Régimen marginal de G en ITT-Z.** El truth ITT actual usa peso fijo 1/2 sobre G=0/1. Es una definición implícita de ITT-Z bajo régimen G 50/50, no un ITT marginal genérico. Antes de materializar C1 se debe declarar/versionar ese régimen o sustituirlo por el régimen G objetivo del ledger. No se elige ahora un régimen distinto ni se inventan probabilidades.

**C. Asignación versus intervención.** La asignación aleatoria G no equivale a la intervención sobre ΔT_acc*. La primera etapa vectorial inducida por G, incluso si es positiva, no demuestra que G implemente g_A ni que no existan vías directas/colaterales.

**D. Heterogeneidad.** La presencia del coeficiente heterogeneity no prueba heterogeneidad del estimando de interés. C1-HET exige heterogeneidad de ITT-Z; C3-HET exige heterogeneidad de θ_A. Deben comprobarse efectos condicionales y masas sobre la población correspondiente, no solo variación de profile_match_p.

**E. Interferencia y positividad.** El modo de interferencia actual utiliza asignaciones observadas de peers para construir potenciales; sin mapa de exposición/estimando de cluster completo no acredita ITT individual. La opción positivity=False retira G=1 en estrato alto; no prueba falta de positividad Z ni positividad de g_A.

**F. Truncamiento.** El clipping de profile_match_p a [0,1] hace que los coeficientes configurados no sean iguales a los efectos causales realizados. Los signos y contrastes deben adjudicarse desde potenciales generados, nunca desde el signo nominal de un coeficiente.

### 16.229.5. Dictamen y alcance de cierre

**Cerrado:** auditoría estática de las doce celdas; separación de representabilidad algebraica y cobertura científica; detección de la ausencia de g_A; identificación del régimen G 50/50 implícito; delimitación de lo que el parámetro heterogeneity y el indicador positivity realmente representan; reutilización del roster existente.

**Abierto y no bloqueable por documentación:** (1) ruta de intervención directa g_A y potenciales propios; (2) régimen G explícito para ITT-Z; (3) configuración factible de C1 con signos/nulo y ausencia de saturación; (4) demostración de signos condicionales opuestos para C1-HET; (5) certificados/diseño y verificación del Analyzer; (6) estimación/varianza compatible con unidad/estratos/interferencia; (7) materialización de registros del ledger. Ninguna de estas brechas se resuelve asignando nombres o flags.

**Dictamen:** TWELVE_CELL_LOGICAL_FEASIBILITY_AUDITED / C1_PARTIALLY_REPRESENTABLE_NOT_MATERIALIZED / C1_HETEROGENEITY_NOT_DEMONSTRATED / C3_POINT_TRUTH_NOT_REPRESENTABLE_WITH_CURRENT_ZG_POTENTIALS / LEGACY_THETA_ACCESS_TRUTH_EQUALS_ITT_G_Z0 / ITT_Z_IMPLICIT_G_50_50_REGIME / NO_ROSTER_EXPANSION / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 77 — resolver, dentro del contrato ya aprobado, la mínima representación contrafactual de g_A sobre el vector completo y el régimen G explícito de ITT-Z, sin crear nuevas clases ni cambiar estimandos. La decisión debe especificar qué se mantiene fijo, qué cambia bajo g_A, cómo se conserva el acoplamiento de exógenas y qué truth queda en Generator/Evaluator; el Analyzer seguirá ciego a esa truth. No asignar parámetros numéricos ni ejecutar.


---

## 16.230. Gate 77 — contrato mínimo de intervención g_A y régimen G de ITT-Z (2026-11-13)

**Precedencia:** §§16.226–16.229, en especial definición contrafactual §16.226.2, equivalencia §16.226.3, ruta A/B/C §16.227.4 y matriz de celdas §16.228.2. Reutiliza el vector ΔT_acc* de cuatro coordenadas, las historias/exógenas, los mecanismos downstream y el roster actual. No crea mundos ni estimandos, no reabre Value/V_cont, no implementa código ni ejecuta.

### 16.230.1. Corrección de precisión al Gate 76

La inspección de código confirma que el harness ya incluye una **asignación G aleatorizada que modifica las cuatro coordenadas** de delta_vector, y el encabezado del módulo la describe como intervención sintética focal. Por ello, no es correcto afirmar que el código carece de toda operación sobre el vector o que G solo modifica una coordenada.

La limitación es más precisa y coincide con §§16.226–16.227: G no fuerza directamente un vector completo bajo dos políticas focales especificadas. En el código, cada coordenada depende de G, provision_ok y su umbral exógeno; la provisión puede fallar y la distribución conjunta resultante del vector no está definida como dos kernels g_A1(a|h) y g_A0(a|h) con soporte/versiones propios. G sigue siendo una asignación cuyo efecto incluye fallos de provisión y cualquier vía directa/colateral permitida. El encabezado descriptivo no prevalece sobre el estimando formal.

Por tanto:
- Existe ITT_G|Z=0 y su potencial contrafactual [Z=0,G=0/1].
- Existe una primera etapa vectorial de G sobre las cuatro coordenadas.
- No existe todavía una ruta A materializada que intervenga directamente sobre el vector completo según el contrato de §16.226.2.C.
- La afirmación de Gate 76 “no existe función de asignación sobre el vector” se corrige por la formulación anterior. Su conclusión sustantiva —el contraste G no es θ_A por defecto— permanece válida.

### 16.230.2. Definición mínima de las políticas focales

Se fija el objeto estructural de intervención, sin asignar parámetros probabilísticos ni alterar el DGP:

- A_i = ΔT_acc,i* = (A_i1,A_i2,A_i3,A_i4), con las cuatro coordenadas preservadas y en el orden canónico del contrato.
- g_A0: intervención directa que fija el vector completo en el estado focal de referencia sin cambios, a0 = (0,0,0,0).
- g_A1: intervención directa que fija el vector completo en el estado focal de cambio en las cuatro coordenadas, a1 = (1,1,1,1).

Son dos políticas deterministas sobre el vector conjunto, no cuatro intervenciones independientes ni una intervención sobre un indicador agregado. El contraste no se define como G=1 frente a G=0. La factibilidad de ambos vectores en las historias de q* debe acreditarse; si alguno no es factible en una historia con masa positiva, no se extrapola y la celda C3 correspondiente no obtiene identificación puntual para el q* completo.

Esta elección define un contraste sintético extremo y reproducible para probar recuperación causal de accesibilidad completa. No afirma que sea el único contraste sustantivamente relevante ni que describa toda intervención realista. Si la especificación maestra ya contiene un par de políticas g_A con identidad y versión aprobadas, ese par prevalece; esta definición no lo sustituye ni lo duplica.

### 16.230.3. Construcción contrafactual y acoplamiento

Para cada unidad/historia H_i, el Generator debe construir las dos ramas Y_i^(g_A0,r_common) y Y_i^(g_A1,r_common) con:

1. La misma historia basal H_i, la misma pertenencia a q* y la misma versión de Outcome/horizonte.
2. El vector completo fijado por cada política; no se vuelve a pasar por provision_ok, u_access, u_relation, u_context o u_mapping para decidir si la intervención focal “se instaló”. Esas variables describen el mecanismo natural/de asignación G y permanecen en la rama ITT-G; no pueden convertir la intervención directa g_A en un encouragement.
3. Los mismos valores exógenos acoplados para todos los mecanismos downstream y no focales que deban permanecer comunes: trayectoria, ENABLED, PROFILE y cualquier ruido de Outcome/medición, según el DGP vigente. El acoplamiento no cambia las distribuciones marginales de cada rama; permite comparar potenciales bajo las mismas condiciones exógenas.
4. El mismo r_common en ambos brazos: alternativas/ramas colaterales, régimen de paquete, contexto, versiones y demás condiciones no focales se fijan según la definición aprobada. No se permite que Z, G, provisión u otra rama cambie diferencialmente entre los dos potenciales focales.
5. El recálculo completo de los descendientes causales de A: Reach, trayectoria y Outcome se derivan otra vez desde el vector intervenido y los mecanismos downstream ya existentes. No se reemplaza Outcome por una fórmula lineal paralela ni se copia el resultado de las ramas Z/G.
6. La verdad focal por unidad es Y_i^(g_A1,r_common) − Y_i^(g_A0,r_common); theta_a_truth es su promedio sobre la distribución q* predeclarada. Se conservan además ambos potenciales, el vector aplicado, q*, r_common, soporte y provenance para auditoría del Evaluator.

El Generator puede conservar potential_v[unit][z][g] para las asignaciones Z/G y añadir una familia contrafactual separada para las dos políticas g_A. No se sobrescribe ni reinterpreta ningún potencial histórico. La representación es una dimensión contrafactual del mismo DGP y de las mismas unidades/exógenas, no un roster nuevo.

### 16.230.4. Régimen explícito de G para ITT-Z

El cálculo vigente de itt_package_truth promedia los potenciales G=0 y G=1 con pesos iguales bajo cada Z. Para no alterar retrospectivamente el estimando ni dejar el régimen implícito, se fija como identidad de régimen legacy:

G_REGIME_MARGINAL_50_50_V1

Definición: distribución marginal objetivo de asignación G con pesos P(G=0)=P(G=1)=1/2, aplicada de igual forma a ambos brazos Z para el ITT-Z. La verdad se expresa como:

ITT_Z^(G 1/2) = 1/2 E[Y(1,0)+Y(1,1)] − 1/2 E[Y(0,0)+Y(0,1)].

El régimen se declara/versiona en el contrato y manifest; el Analyzer debe conocerlo como parte del estimando, no inferirlo de un promedio interno oculto. Esta decisión conserva exactamente la convención de verdad que ya usa el Generator; no declara que 50/50 sea óptimo ni universal. Cualquier otro régimen sería otro estimando/versionado y requeriría decisión expresa, no un cambio silencioso.

### 16.230.5. Tres objetos y firewall resultantes

El contrato mínimo mantiene separados:

| Objeto | Definición / potenciales | Uso |
|---|---|---|
| itt_z_truth | ITT-Z bajo G_REGIME_MARGINAL_50_50_V1 | Verdad C1 |
| itt_g_z0_truth | E[Y(0,1)-Y(0,0)] bajo asignación G | Verdad auxiliar de asignación; nunca proxy automático de C3 |
| theta_a_truth | E_{H~q*}[Y^(g_A1,r_common)-Y^(g_A0,r_common)] | Verdad C3 |

El Generator/Evaluator conserva las tres verdades, potenciales y metadatos. El Analyzer recibe observaciones selladas, asignaciones/protocolos y el contrato público de estimandos/régimen. No recibe los vectores contrafactuales no observados, semillas, parámetros, etiquetas de celda ni TruthBundle.

La ruta A solo puede declararse identificante si el diseño/protocolo realmente implementa la intervención directa del vector o si la evidencia permite verificar su aplicación, con soporte/factibilidad en q*, Outcome medido, consistencia, r_common y ausencia/interferencia resueltas. La asignación G actual no se convierte retroactivamente en esa ruta por cambiar el nombre de un campo.

### 16.230.6. Consecuencias para las doce celdas y límites

- C1 mantiene sus seis roles y se adjudica bajo el régimen G 50/50 explícito, salvo que una celda preexistente defina legítimamente una población/régimen distinto y lo identifique como estimando separado.
- C3-POS/NULL/NEG se construyen variando únicamente la función downstream focal ya existente y se adjudican frente a theta_a_truth, una vez demostrada la factibilidad de ambos vectores bajo q*. No se asignan ahora coeficientes ni signos nominales.
- C3-DECOUPLED conserva el subcaso de theta_A nulo con ITT-Z no nulo mediante una vía de paquete no focal ya existente, y el subcaso de ruta focal no identificable por condiciones no focales diferenciales. El segundo no se etiqueta como theta_A puntual identificado.
- C1-HET y C3-HET siguen sin estar acreditadas: el acoplamiento por unidad no crea por sí solo historias con signos condicionales opuestos ni masas q* positivas. Deben demostrarse dentro de las clases y rangos existentes.
- C3-ABSTAIN debe seguir absteniéndose en el harness actual cuando solo disponga de G como encouragement y no exista ruta A acreditada.
- PARTIALLY_IDENTIFIED continúa deshabilitado hasta contrato, algoritmo y validación de bounds.
- No se añade clase de mundo, mecanismo causal, estimando, Outcome, coordenada focal ni parámetro numérico.

### 16.230.7. Criterio de cierre y dictamen

**Cerrado:** distinción exacta entre asignación G y política directa g_A; definición mínima conjunta de g_A0/g_A1; reglas de acoplamiento exógeno y propagación downstream; r_common y q* como condiciones compartidas; régimen G 50/50 explicitado sin cambiar el ITT-Z legacy; separación de las tres verdades y firewall; corrección de precisión del Gate 76.

**Abierto:** identidad/versionado definitivo de q* y r_common desde el ledger; verificación de factibilidad/soporte de los vectores extremos en cada historia; construcción de potenciales g_A en TruthBundle; certificados de implementación de la intervención para Analyzer; factibilidad de signos/nulos/heterogeneidad en el roster; estimadores/varianzas y pruebas Analyzer/Evaluator. No se declara cobertura ni identificación implementada.

**Dictamen:** GATE_77_CONTRAST_AND_REGIME_CONTRACT_DEFINED / G_ASSIGNMENT_NOT_EQUIVALENT_TO_DIRECT_VECTOR_INTERVENTION / G_A0_AND_G_A1_FULL_VECTOR_POLICIES_SPECIFIED / SHARED_EXOGENOUS_COUPLING_REQUIRED / ITT_Z_G_50_50_REGIME_EXPLICIT / THREE_TRUTHS_PRESERVED / GATE_76_WORDING_CORRECTED / NO_NEW_WORLDS_OR_ESTIMANDS / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 78 — reconciliar estas políticas deterministas con las restricciones de factibilidad y soporte del roster y del ledger existente. Comprobar, sin simulación ni parámetros nuevos, si los cuatro componentes de a0 y a1 son admisibles en las historias con masa q* y qué clases existentes permiten una comparación focal limpia con r_common. Si los extremos no son factibles, no suavizarlos ni reemplazarlos en silencio: registrar la limitación y volver a la especificación maestra para resolver la política admisible. No implementar ni ejecutar.


---

## 16.231. Gate 78 — auditoría de factibilidad y soporte de g_A frente al roster y al contrato maestro (2026-11-13)

**Precedencia:** §§16.208.2–16.208.6, 16.211.1–16.211.5, 16.212.1–16.212.3, 16.223.1–16.223.3, 16.226.2.C–16.226.6 y 16.230. Este gate audita soporte lógico/documental; no genera historias, no asigna masas/probabilidades/parámetros, no ejecuta y no cambia el roster. No reabre Value/V_cont.

### 16.231.1. Regla maestra de admisibilidad

La definición rectora es §16.226.2.C: g_A0 y g_A1 son intervenciones explícitas sobre la distribución conjunta del vector completo ΔT_acc*, condicionadas por historia basal admisible h; q_X* es la distribución objetivo común y r_common fija las condiciones no focales pertinentes. Las intervenciones deben tener identidad/versión, distribución conjunta, factibilidad y soporte. §16.208.6 confirma que el contraste se formula sobre distribuciones factibles del vector completo.

Por consiguiente, los vectores deterministas (0,0,0,0) y (1,1,1,1) introducidos como candidatos en §16.230.2 no quedan aprobados por este gate. Son un caso particular posible solo si la semántica de cada coordenada, el dominio, las restricciones conjuntas y el soporte por historia permiten ambas asignaciones. El hecho de que el harness represente actualmente cada coordenada como entero binario no demuestra que esos extremos sean las políticas maestras ni que sean factibles en q_X*.

### 16.231.2. Auditoría de semántica y representación

1. La especificación de §16.212 define ΔT_acc* como diferencia entre snapshots estructurales completos, con cuatro coordenadas ΔU/ΔR/ΔC/ΔX potencialmente correlacionadas; ΔE_T queda fuera. No presupone que cada coordenada sea un tratamiento binario independiente ni que cualquier combinación cartesiana sea admisible.
2. El roster §16.208.2 es un conjunto de clases/mecanismos, no una tabla de historias basales con soporte enumerado. Las clases Focal limpio, Nulo, Focal adverso, Alternativa basal, Alternativa afectada/colateral, Vía directa, Heterogeneidad, Interferencia, Observación adversarial y Soporte/ausencia/censura no proporcionan por sí solas el dominio conjunto de ΔT_acc* ni las masas de q_X*.
3. El ledger §16.223.2 exige population_id/q_X*, intervention_id, active_functions, held_fixed, r_common_status y support_status por celda. El propio contrato indica que no se fijan número de historias ni masas en esa especificación. No hay base para adjudicar soporte puntual por historia a partir del nombre del perfil.
4. El harness actual usa un vector de cuatro indicadores binarios en el que cada componente depende de G, provision_ok y su exógena/umbral; la provisión puede fallar y las coordenadas pueden no alcanzar conjuntamente el vector completo. Esto acredita una primera etapa vectorial bajo asignación G, no la factibilidad de intervenciones directas deterministas ni el soporte de sus políticas en q_X*.
5. El comentario de cabecera del harness que denomina G una intervención sintética sobre el cambio focal no prevalece sobre el contrato formal de §§16.226.2.C–16.226.3: la semántica se adjudica por potenciales, mecanismo y equivalencia, no por etiqueta del código.

### 16.231.3. Matriz de soporte que puede acreditarse sin inventar datos

| Clase existente | Condición para un contraste C3 limpio | Estado de factibilidad/soporte hoy |
|---|---|---|
| Focal limpio (R0) | q_X* definido; ambas políticas g_A factibles en cada historia con masa; mismo r_common; sin vías directas/colaterales diferenciales; mapping/medición/versiones válidos | **CANDIDATO ESTRUCTURAL; SOPORTE NO ACREDITADO.** Es la única clase del roster orientada expresamente a control positivo focal limpio, pero §16.211 advierte que πA ausente solo puede estipularse con exhaustividad. |
| Nulo (R0/R3) | La política puede modificar ΔT_acc*, mientras la función de Outcome focal es nula, o una etapa posterior neutraliza el resultado según el rol | **CONDICIONAL; NO MATERIALIZADO.** El roster permite la distinción conceptual, pero no contiene historias, masas ni función concreta de Outcome adjudicadas. |
| Focal adverso (R0) | Ambas políticas factibles y una función existente deteriora una coordenada/resultado con dirección adversa conocida | **CONDICIONAL; NO MATERIALIZADO.** No se puede inferir signo efectivo de la etiqueta ni de un coeficiente nominal. |
| Alternativa basal (R1) | La misma ruta alternativa permanece bajo ambos brazos y r_common; la interpretación distingue apertura focal de Reach | **NO ACREDITA EXCLUSIVIDAD FOCAL.** Puede servir como falsador de Reach/exclusividad, no como control positivo limpio sin una definición adicional del resultado y contraste. |
| Alternativa afectada/colateral (R2) | La política no focal que altera A1/A2/dependencias se mantiene común o se identifica explícitamente como diferencial | **NO COMMON_FIXED POR DEFECTO.** Si la alternativa cambia diferencialmente, el contraste focal limpio falla; la salida es efecto de paquete/no identificación según contrato. |
| Fallo por etapas / provisión (R3) | g_A debe fijar directamente el vector sin volver a pasar por provisión natural; los fallos de provisión permanecen en ITT-G/Z | **NO ES PRUEBA DE SOPORTE g_A.** R3 es útil para separar intento/recepción/instalación/provisión de accesibilidad intervenida. |
| Vía directa | Las vías directas deben mantenerse comunes o separarse mediante un contrato identificante | **NO COMMON_FIXED SI ES DIFERENCIAL.** No atribuir a θ_A el efecto total del paquete. |
| Heterogeneidad | q_X* incluye estratos/historias con masa positiva y ambas políticas tienen soporte en cada estrato relevante | **NO DEMOSTRADA.** No hay distribución de historias ni masas/soporte condicionales cerrados. |
| Interferencia | UA/clúster o mapa de exposición definido y compatible con ambas políticas | **NO ACREDITADA.** La estructura de peers del harness no sustituye el mapa/estimando de exposición del contrato maestro. |
| Observación adversarial / soporte, ausencia o censura | La verdad estructural y soporte se distinguen del canal observado; missingness/censura no se recodifican como vector cero | **NO ACREDITA SOPORTE.** Puede forzar bounds/abstención, pero no crear factibilidad estructural. |

### 16.231.4. Dictamen sobre los extremos propuestos en Gate 77

- a0=(0,0,0,0) y a1=(1,1,1,1) permanecen como **candidatos deterministas no validados**, no como políticas confirmatorias congeladas.
- No se puede concluir que sean imposibles: el contrato no aporta una restricción que los refute universalmente.
- Tampoco se puede concluir que sean factibles: faltan dominio semántico por coordenada, historias de q_X*, restricciones conjuntas, soporte y compatibilidad con snapshots/versiones.
- No se sustituyen por políticas estocásticas inventadas ni se suavizan sus extremos para forzar positividad.
- Si el soporte no cubre ambas políticas en toda historia de q_X* con masa positiva, no se extrapola. Cualquier restricción a subpoblación, nuevo q_X* o bounds exige estimando/decisión explícitos y no se hace en este gate.
- r_common_status=COMMON_FIXED debe demostrarse por cada celda; no se deduce del perfil R0–R3 ni de que el Generator reutilice la misma semilla. Acoplar exógenas no elimina una vía estructural diferencial.
- La factibilidad de política y la identificación por Analyzer son preguntas distintas: un potencial puede existir en Generator sin que el diseño/evidencia permita identificarlo.

### 16.231.5. Corrección y reconciliación de Gate 77

Se conserva la definición de §16.230.1 que separa asignación G de intervención directa g_A y la exigencia de acoplamiento/descendencia causal. Se limita §16.230.2: los dos vectores binarios son una propuesta de política determinista para someter a soporte, no una decisión aprobada por la especificación maestra. La forma general de las políticas sigue siendo la de §16.226.2.C: distribuciones conjuntas explícitas sobre el vector completo, condicionadas por h. El régimen G_REGIME_MARGINAL_50_50_V1 conserva la convención legacy de ITT-Z, pero no aporta evidencia sobre q_X* ni sobre soporte de g_A.

### 16.231.6. Dictamen y siguiente dependencia

**Cerrado:** reconciliación normativa entre el contrato general de g_A y la propuesta extrema de Gate 77; auditoría de qué clases del roster pueden servir como candidatos, falsadores o adversariales; separación de soporte, r_common, primera etapa G e identificación; constatación de que el roster no materializa q_X* ni soporte por historia.

**Bloqueado por especificación/ledger, no por falta de más documentación narrativa:** no es posible emitir una matriz afirmativa de soporte ni seleccionar políticas confirmatorias sin los registros por historia que §16.223 exige. No se añaden mundos, distribuciones, parámetros, masas ni IDs.

**Dictamen:** GATE_78_SUPPORT_AUDIT_COMPLETE / G_A_EXTREME_VECTORS_UNVALIDATED / MASTER_POLICY_FORM_REMAINS_JOINT_HISTORY_CONDITIONAL_DISTRIBUTIONS / FOCAL_CLEAN_R0_IS_CANDIDATE_NOT_CERTIFIED / R1_R2_R3_RETAIN_EXISTING_ROLES / Q_X_SUPPORT_NOT_MATERIALIZED / R_COMMON_NOT_CERTIFIED_PER_CELL / NO_ROSTER_EXPANSION / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 79 — convertir el requisito ya existente de §16.223.2 en el registro mínimo por historia de q_X* y de soporte conjunto de g_A0/g_A1, reutilizando exclusivamente las historias/clases ya contenidas en el universo finito. Resolver qué información ya existe en las cards/ledger y qué campo concreto falta; no inventar historias, masas, políticas ni parámetros. Si el universo actual no permite ese registro, elevar la limitación al contrato maestro en lugar de fabricar soporte. No implementar ni ejecutar.


---

## 16.232. Gate 79 — registro mínimo por historia de q_X* y soporte conjunto de g_A (2026-11-13)

**Precedencia:** §§16.208.3–16.208.8, 16.211–16.212, 16.223.1–16.223.5, 16.226.2.C–16.226.6 y 16.231. Este gate convierte el ledger estructural ya existente en un registro hijo por historia. No crea historias, unidades, clases, masas, políticas, parámetros ni estimandos; no materializa filas sin fuente; no implementa ni ejecuta.

### 16.232.1. Qué existe realmente y qué no

La reconstrucción de los artefactos existentes produce este inventario:

| Fuente existente | Información reutilizable | Lo que no acredita para q_X* / g_A |
|---|---|---|
| Inventario finito §16.208 y C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md | UE/UA candidatas, perfiles R0–R3, topologías, rutas y clases de mecanismos | No enumera historias basales h ni asigna masas q_X*(h); UE=UA es solo candidata bajo aislamiento |
| Mapping finito §16.211 y cards AB-03/AB-04 | Identidades/roles abstractos F1/F2/A1/A2, predicados, snapshots requeridos y condiciones por ruta | Son fichas de transformaciones/predicados, no registros de historia ni distribuciones conjuntas admisibles de ΔT_acc* |
| Contrato DGP temporal y de roles | X, H0, C_c, q_X*, secuencia temporal, variables y separación Generator/Analyzer/Evaluator | Define objetos y dependencias, pero no aporta valores basales por UE, soporte conjunto ni pesos |
| Contrato D2 población/soporte | Define q_X* como distribución objetivo condicionada por elegibilidad basal y distingue P*, q_X*, π_h y pesos del benchmark | Declara roster, q_X*, pesos, soporte común y positividad no materializados |
| Paquete B1/Need y crosswalk de cohorte | Claves que podrán anclar una unidad: ue_id, b1_id, instance_id/version, baseline_record_id; composición Need explícita y reservada | El roster B1/UE sigue no aprobado/no materializado. Need_preZ y su soporte 1/0 no son q_X*, elegibilidad C3 ni soporte de g_A |
| Revisión de composición Need_preZ | Regla de truth 1/0/? y soporte binario mínimo de su cohorte propia | No permite inferir X, H0, C_c, masas q_X* ni soporte causal focal |
| Harness integrado actual (blob 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4) | n_units, seed, asignaciones Z/G y un baseline_x escalar aleatorio por unidad; exógenas comunes para potenciales Z/G | No contiene objeto/versión q_X*, roster de historias, history_id, masas, X/H0/C_c conjuntos, snapshot basal completo ni kernels g_A. baseline_x no es una historia basal y la asignación balanceada Z/G no es una distribución q_X* |

**Resultado:** existe un contrato que exige q_X* y soporte, pero no existe en los artefactos inspeccionados una tabla materializada de historias basales C3 ni una distribución objetivo con masas. No se puede rellenar el ledger por analogía a partir de las cards, perfiles R0–R3, Need_preZ, baseline_x, n_units o la semilla.

### 16.232.2. Registro hijo mínimo, sin duplicar el ledger de celda

Se conserva §16.223.2 como ledger padre por celda. Para cada celda C3 se define un registro hijo por cada historia h que tenga masa positiva en q_X*. No se crea otro ledger paralelo: cada fila hija referencia world_id/version, cell_id, estimand_id=C3, population_id=q_X* e intervention_id del registro padre.

| Campo del registro hijo | Contenido mínimo exigido |
|---|---|
| history_ref | Referencia compuesta y estable a la UE/instancia y baseline existentes: ue_id, instance_id/version, baseline_record_id y snapshot basal/version. No inventar un ID de historia separado si esas identidades ya resuelven la unidad/historia |
| q_X_version / q_X_mass | Versión de la distribución y masa basal positiva de esa historia; las masas de todas las historias del q_X* declarado deben sumar 1 |
| baseline_history_ref | Referencias versionadas a X, H0 y C_c, elegibilidad basal y predicados necesarios (incluidos C_dep,0* y A_f,0*) que definen la historia admisible; UNKNOWN conserva su estado y no se recodifica |
| delta_t_acc_schema_ref | Orden, semántica, dominio y versión de las cuatro coordenadas ΔU*/ΔR*/ΔC*/ΔX*, derivadas de snapshots estructurales completos; no tratarlas como cuatro tratamientos independientes |
| g_A0_ref | Identidad/versión de la regla conjunta g_A0(ΔT_acc*|h), su distribución sobre vectores completos y la referencia a la política/soporte declarados |
| g_A1_ref | Identidad/versión de la regla conjunta g_A1(ΔT_acc*|h), su distribución sobre vectores completos y la referencia a la política/soporte declarados |
| g_A0_support / g_A1_support | Dictamen separado por política y por historia: factibilidad estructural del vector/conjunto de vectores, evaluación contrafactual posible bajo el DGP y soporte observacional necesario para la ruta de identificación del Analyzer |
| joint_support_status | Resultado de soporte conjunto de la distribución vectorial completa bajo cada g_Ak; no se deriva multiplicando cuatro soportes marginales ni suponiendo independencia entre coordenadas |
| r_common_ref/status | Referencias a las versiones/valores no focales y exógenas que se mantienen comunes, con COMMON_FIXED, DIFFERENTIAL_IDENTIFIED, DIFFERENTIAL_UNRESOLVED o NOT_APPLICABLE; COMMON_FIXED requiere evidencia/referencia, no mera igualdad de nombres o semillas |
| support_evidence_ref | Evidencia o regla generadora que permite adjudicar factibilidad, soporte, cobertura y cualquier UNKNOWN, con provenance y versión |

Los campos history_ref, q_X_mass, g_A0/1_support, joint_support_status y r_common_ref son la desagregación mínima de population_id, intervention_id, support_status, held_fixed y r_common_status ya exigidos por §16.223.2; no crean estimandos ni requisitos poblacionales distintos.

### 16.232.3. Tres estados de soporte que no deben colapsarse

Para evitar que Generator y Analyzer parezcan acreditar lo mismo, el support_status del ledger se informa con tres componentes distintos:

1. **Factibilidad estructural:** la política conjunta g_Ak es admisible para esa historia según dominio, restricciones entre coordenadas, snapshots, identidad/versionado y condiciones basales. Si no puede decidirse, UNKNOWN; no se interpreta como vector cero.
2. **Evaluabilidad contrafactual del Generator:** las funciones estructurales del DGP permiten calcular Y bajo g_Ak, con las dependencias y exógenas compartidas requeridas. Que Generator pueda calcular un potencial no prueba soporte observacional ni identificación.
3. **Soporte de identificación del Analyzer:** el diseño y la evidencia observada ofrecen la variación/positividad necesaria para identificar el contraste definido, en esa historia y población, bajo los supuestos declarados. La ausencia de soporte no se repara extrapolando desde otras historias.

La intervención g_A es una regla conjunta sobre ΔT_acc* completo, condicionada por h. La positividad/soporte relevante debe evaluarse para el vector conjunto que la política asigna, no solo para cada coordenada por separado. No se declara ahora que g_A0/g_A1 sean deterministas ni se valida el par extremo propuesto en §16.230.2; sigue prevaleciendo la forma general de §16.226.2.C y el dictamen de §16.231.4.

### 16.232.4. Reglas de materialización y controles de integridad

- El conjunto de filas hijas debe ser exactamente el soporte finito declarado de q_X*, sin historias añadidas por conveniencia ni omisiones silenciosas.
- Cada masa q_X*(h) debe ser positiva y la suma de masas debe ser 1. No se fijan cardinalidad ni valores de masa en este gate.
- q_X* no se sustituye por π_h, pesos de escenarios/benchmark, asignaciones balanceadas Z/G, prevalencia Need_preZ ni frecuencia accidental de valores en una muestra simulada.
- X, H0 y C_c se anclan en baseline pre-Z y en sus versiones. Variables post-Z, instalación, observación o Outcome no pueden definir retrospectivamente h.
- Los cuatro componentes de ΔT_acc* se conservan como vector estructural conjunto derivado de snapshots; la proyección focal A_f* o el indicador all(delta_vector) no sustituye al vector.
- Para cada historia se registra el soporte de ambas políticas. Una política no factible en una historia de masa positiva bloquea el contraste puntual sobre el q_X* completo; no se recorta la población ni se cambia q_X* en este gate.
- r_common se acredita mediante referencias a funciones, parámetros, versiones, alternativas, recursos, entorno y exógenas fijadas. Si una vía cambia diferencialmente, se registra como diferencial y se adjudica según §16.226.3; el acoplamiento exógeno por sí solo no la neutraliza.
- Los registros de Generator/Evaluator con truth y potenciales permanecen separados de la información efectivamente disponible al Analyzer, conforme al firewall de §16.208.5 y §16.226.5.

### 16.232.5. Dictamen: qué se cierra y qué bloquea

**Cerrado por Gate 79:** fuentes históricas reutilizables identificadas; distinción entre cards de transformación, historias basales, composición Need y población q_X*; registro hijo mínimo definido dentro del ledger de §16.223; separación de factibilidad estructural, evaluabilidad contrafactual y soporte de identificación; controles de masa, soporte vectorial conjunto y r_common especificados.

**No materializable todavía:** no hay roster DGP/B1 aprobado con UE/instancias/baselines enumerados; no hay filas de historias X/H0/C_c versionadas; no hay q_X* con masas; no hay dominio/soporte conjunto por historia para g_A0/g_A1; no hay evidencia por historia de r_common. No se rellena ninguna fila ni se declara soporte.

**Dictamen:** GATE_79_HISTORY_LEVEL_LEDGER_SCHEMA_CLOSED / EXISTING_ARTIFACTS_RECONCILED / Q_X_HISTORY_ROWS_NOT_MATERIALIZED / Q_X_MASSES_NOT_DEFINED / JOINT_G_A_SUPPORT_NOT_ESTABLISHED / STRUCTURAL_FEASIBILITY_SEPARATED_FROM_ANALYZER_IDENTIFICATION / NEED_PREZ_NOT_A_Q_X_PROXY / NO_NEW_HISTORIES_OR_WORLDS / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 80 — comprobar si el roster B1/UE cuya aprobación ya está prevista puede proporcionar, sin ampliar sus unidades, el universo basal requerido por q_X*. Reconciliar sus identidades y snapshots con history_ref, y determinar si las historias X/H0/C_c y sus masas pueden derivarse de los registros ya definidos o si requieren una decisión de diseño explícita. No usar la cohorte Need_preZ como sustituto de q_X*, no crear unidades para conseguir soporte y no asignar masas. Si el roster sigue sin aprobarse/materializarse, dejar la dependencia bloqueada y pasar al siguiente componente de cierre que no dependa de ella; no abrir otra ronda de documentación narrativa. No implementar ni ejecutar.


---

## 16.233. Gate 80 — capacidad del roster B1/UE para materializar el universo basal de q_X* (2026-11-13)

**Precedencia:** §§16.208–16.212, 16.223, 16.226–16.232; DEC-C10S-B1-UNIT-001, DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001, DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001, DEC-C10-095 y DEC-C10-096; crosswalk B1/Need, contrato de materialización B1 y reconciliación D2. Este gate comprueba capacidad documental y estado de aprobación. No aprueba el roster, no materializa unidades ni snapshots, no asigna masas, no modifica la precedencia P* ni ejecuta.

### 16.233.1. Dictamen sobre el alcance ya decidido

DEC-C10-096 ya resolvió la cuestión de alcance de la cohorte de validación Need: será el censo de todas las UE del roster DGP/paquete B1 aprobado al que aplique el paquete. DEC-C10-095 fija la composición truth Need 1/0/? y sus controles. Por tanto, no queda pendiente elegir entre censo y subcohorte para Need.

Lo que sigue pendiente es anterior: **no existe todavía una versión de roster B1/UE aprobada y materializada a la que aplicar ese censo**. El crosswalk de población y el documento de denominadores declaran expresamente ROSTER_NOT_APPROVED / NOT_MATERIALIZED; el contrato mínimo de materialización especifica qué claves deberá contener cada unidad, pero no asigna IDs concretos ni aporta filas. La decisión de censo no crea por sí misma el censo.

### 16.233.2. Qué puede proporcionar el paquete B1 y qué no

| Artefacto/decisión existente | Capacidad acreditada | Límite para q_X* |
|---|---|---|
| DEC-C10S-B1-UNIT-001 y decisiones de cardinalidad | Una B1 vinculada unívocamente a cada UE del paquete; cardinalidad lógica definida | No identifica ninguna UE concreta ni define el marco total de historias |
| DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | Cada UE tendrá una instancia lógica de servicio propia, única y versionada | No proporciona instance_id/version ni snapshot real/materializado por unidad |
| Contrato mínimo B1/Need | Define ue_id, b1_id, contract_id/version, instance_id/version, baseline_record_id y z_event_id, y separa truth, evidencia y adjudicación | Declara que los IDs se generan solo desde un roster cerrado/versionado; no contiene valores ni registros |
| DEC-C10-095 / DEC-C10-096 y crosswalk de cohorte | Regla de truth Need y censo de la cohorte B1 aplicable, sin selección por Need, Z u observabilidad | La cohorte es de validación de Need; no es P*_{τ2}, P*_F, q_X* ni denominador ITT |
| Contrato DGP temporal/roles y D2 | Define simbólicamente X, H0, C_c, elegibilidad pre-Z, q_X* y sus relaciones | No asigna valores basales conjuntos, versiones por unidad, roster causal ni distribución/masas |
| Harness actual | n_units, seed, Z/G y baseline_x escalar sintético | No implementa roster B1, UE/B1/instancia/baseline IDs, X/H0/C_c conjuntos ni q_X* |

**Resultado:** B1/UE es una arquitectura válida para anclar historias cuando exista el roster, pero no puede suministrar ahora el universo basal. Las claves contractuales son un esquema lógico, no unidades existentes. baseline_x del harness no puede completar las claves ni sustituir X/H0/C_c.

### 16.233.3. Reconciliación de los tres universos

Se mantienen separados:

1. **Roster DGP/paquete B1:** marco censal al que aplicará la validación Need cuando sea aprobado y versionado.
2. **Población causal P*_{τ2} / P*_F:** definida por sus propios criterios basales y de ruta; no se deriva del soporte truth 1/0 de Need.
3. **Población objetivo q_X* de C3:** distribución conjunta sobre historias basales admisibles (X,H0,C_c y campos aceptados), con masas y soporte de g_A; no se deriva automáticamente del censo B1 ni de sus frecuencias.

La eventual reutilización de una misma UE entre estos marcos exige un crosswalk de identidad y una regla explícita de inclusión. La igualdad de rosters, si se decidiera, no implica igualdad de poblaciones ni igualdad de pesos. Un censo de unidades tampoco determina por sí mismo si q_X* será empírica, uniforme, ponderada o una distribución objetivo distinta: esa decisión debe estar especificada, justificada y versionada, no inferida del orden de filas ni de la semilla.

### 16.233.4. Matriz de materialización

| Requisito | Estado actual | Dictamen |
|---|---|---|
| Regla de cardinalidad B1/UE | Decidida | DEFINED |
| Identidad lógica de instancia por UE | Decidida | DEFINED |
| Alcance censal de cohorte Need | DEC-C10-096 aceptado | DEFINED / ROSTER-DEPENDENT |
| Roster UE/B1 aprobado, cerrado y versionado | No existe en los artefactos inspeccionados | BLOCKED |
| Filas ue_id/b1_id/instance_id/version/baseline_record_id | No materializadas | NONE |
| Snapshots y valores conjuntos pre-Z de X/H0/C_c | No materializados por UE | NONE |
| Elegibilidad y predicados basales por unidad | Reglas simbólicas; adjudicación material ausente | NOT MATERIALIZED |
| q_X* y masas por historia | Definición simbólica; sin distribución ni pesos | OPEN / NOT MATERIALIZED |
| Correspondencia roster B1 ↔ P*_{τ2}/q_X* | No establecida | OPEN |
| Soporte conjunto de g_A0/g_A1 y r_common por historia | No evaluable sin las filas basales y las políticas | BLOCKED |

No se crean filas vacías como si fueran historias, ni se inventan IDs de ejemplo para aparentar materialización. Los estados NONE, OPEN y BLOCKED se conservan diferenciados.

### 16.233.5. Decisión operativa y cierre

1. Se reutiliza DEC-C10-096: no se reabre el alcance censal Need ni se propone subcohorte.
2. Se reutiliza el contrato de materialización B1: no se vuelve a diseñar la identidad B1/UE/instancia.
3. No se puede aprobar ni completar el roster con los artefactos disponibles; falta la fuente/decisión autorizada que enumere las UE y sus baselines. La reconciliación D2 indica además que la autorización para capturar/materializar roster, IAM/C_SRC y snapshots no existe en este ciclo.
4. No se asignan masas q_X* a partir de frecuencias del harness, tamaño n_units, orden de unidades o pesos de benchmark.
5. La dependencia de q_X* queda **BLOCKED por ausencia de roster/baselines y de autorización de materialización**, no por falta de otra especificación narrativa.
6. Se pasa al siguiente componente de cierre que no depende de q_X*: auditoría del contrato de asignación ITT-Z y de la evidencia/certificados que el Analyzer necesita para verificarlo. Esto no elimina los bloqueos de población C1 ni habilita estimación; solo permite cerrar de forma independiente qué debe observarse y qué no puede presumirse sobre la asignación.

**Dictamen:** GATE_80_ROSTER_CAPABILITY_AUDIT_CLOSED / B1_UNIT_AND_INSTANCE_KEYS_DEFINED / DEC_C10_096_CENSUS_SCOPE_REUSED / ROSTER_NOT_APPROVED / NO_UNIT_ROWS_OR_BASELINES / X_H0_CC_NOT_MATERIALIZED / Q_X_MASSES_NOT_DERIVABLE / NEED_COHORT_NOT_CAUSAL_POPULATION / MATERIALIZATION_AUTHORIZATION_ABSENT / Q_X_DEPENDENCY_BLOCKED / NO_NEW_UNITS_OR_WORLDS / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

**Siguiente gate:** Gate 81 — auditoría de suficiencia del contrato de asignación ITT-Z: distinguir flags internos del harness de un protocolo de aleatorización verificable; identificar qué datos/certificados puede recibir el Analyzer, qué truth queda reservada al Generator/Evaluator y qué estados deben conducir a identificación, descripción o abstención. Reutilizar §§16.226–16.227, el contrato DGP y el código actual; no fijar probabilidades, estratos, semillas, UA/clúster ni tamaño muestral, no modificar el estimando C1, no ejecutar ni implementar.


---

## 16.233. Gate 80 — capacidad del roster B1/UE para materializar historias basales de q_X* (2026-11-13)

**Precedencia:** §§16.208, 16.211–16.212, 16.223, 16.226, 16.232; C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md; contratos B1/Need de materialización, paquete analítico y crosswalk de cohorte; contrato DGP temporal/roles. Gate de auditoría documental y de dependencias. No crea unidades/historias, no aprueba roster, no asigna truth o masas, no implementa ni ejecuta.

### 16.233.1. Pregunta y evidencia revisada

Pregunta: ¿puede el roster B1/UE ya previsto proporcionar, sin ampliarlo, las historias basales h que requiere q_X* y los anclajes de history_ref definidos en §16.232?

Se inspeccionan:
- C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md;
- C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md;
- C10_S_B1_PREZ_COHORT_SCOPE_AND_EVALUATION_DENOMINATORS_RECONCILIATION_DRAFT_001.md;
- C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md;
- C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md;
- C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md;
- C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md;
- harness integrado vcont_integrated_harness.py (blob 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4).

### 16.233.2. Hallazgo: universo de clases no equivale a roster de unidades

El inventario finito sí contiene una gramática de mundos candidata: estados S0/S1/S2/SF; aliases F1/F2/A1/A2 y relaciones permitidas; perfiles R0–R3 (focal exclusiva, alternativa basal, alternativa afectada y fallo de provisión); y una matriz de ruta/predicado/tiempo/evidencia/cobertura. Pero el propio inventario declara no aprobados catálogo canónico, F*, G, H, recursos, comparador, escenario primario y cobertura de alternativas. Sus aliases y perfiles son clases/mecanismos del fixture, no identidades UE ni historias basales enumeradas.

Los contratos B1 fijan la cardinalidad de una B1 por UE y una instancia lógica de servicio propia/versionada por UE. El paquete define claves ue_id, b1_id, instance_id/version, baseline_record_id y z_event_id, pero declara que no se asignan valores hasta disponer de un roster cerrado y versionado. El contrato mínimo de materialización figura NOT_APPROVED / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED; el crosswalk de cohorte acepta el censo del roster B1 aprobado, pero dice expresamente que esa decisión no aprueba ni materializa el roster.

El contrato temporal define X, H0 y C_c como objetos basales y q_X* como distribución objetivo candidata, pero deja abiertos su distribución concreta, población, pesos, unidad/interferencia, inventario y soporte. No contiene valores X/H0/C_c por UE ni snapshots basales enlazados. La relación UE=UA sigue condicionada a aislamiento no demostrado.

El harness actual genera n_units, asignaciones Z/G y un baseline_x escalar aleatorio por unidad. No contiene ue_id/b1_id/instance_id, baseline_record_id, snapshots completos X/H0/C_c, versión de q_X*, masa por historia ni registro de soporte conjunto g_A. baseline_x y la semilla no se convierten en historias basales ni en q_X*.

### 16.233.3. Matriz de capacidad de materialización

| Requisito de §16.232 | Fuente reutilizable | Dictamen |
|---|---|---|
| Universo de clases/mecanismos | Inventario finito R0–R3 y F1/F2/A1/A2 | EXISTE COMO PROPUESTA; NO ES ROSTER |
| Censo de UE/B1 | Crosswalk DEC-C10-096 y cardinalidad B1/UE | REGLA ACEPTADA; ROSTER NO APROBADO NI MATERIALIZADO |
| Identidad de instancia/versiones | Contratos B1 y servicio | CAMPOS DEFINIDOS; VALORES AUSENTES |
| Baseline inmutable por UE | Contratos B1/paquete | CAMPO DEFINIDO; REGISTROS AUSENTES |
| X, H0, C_c y elegibilidad basal | Contrato temporal y D2 | SEMÁNTICA CANDIDATA; VALORES/VERDAD POR UE AUSENTES |
| q_X* y masas | Contrato temporal/D2 | DEFINICIÓN CANDIDATA; DISTRIBUCIÓN Y MASAS AUSENTES |
| Vector basal/post y schema ΔT_acc* por historia | Contrato de snapshots y harness | REPRESENTACIÓN PARCIAL EN CÓDIGO; SNAPSHOTS/HISTORIAS NO MATERIALIZADOS |
| Soporte conjunto g_A0/g_A1 y r_common | §§16.226, 16.232 | REQUISITOS DEFINIDOS; NO HAY REGISTROS POR HISTORIA |

### 16.233.4. Dictamen y consecuencia operativa

**Gate 80 cerrado:** el roster B1/UE, en su estado documental actual, no puede materializar q_X* ni las historias basales requeridas. No existe fuente aprobada de la que derivar identidades UE, snapshots X/H0/C_c, elegibilidad basal, masas o soporte conjunto. No se asignan valores, no se generan IDs y no se promueve el inventario de clases a roster. Need_preZ conserva su cohorte propia y no se reutiliza como población causal.

La dependencia q_X*/history-level ledger queda BLOCKED_ON_ROSTER_APPROVAL_AND_BASELINE_MATERIALIZATION, sin bloquear todo el cierre de C10-S. No se repite la petición de materializar el roster en gates narrativos sucesivos.

**Dictamen:** GATE_80_ROSTER_CAPABILITY_AUDIT_CLOSED / FINITE_CLASS_GRAMMAR_EXISTS_AS_DRAFT / B1_UE_ROSTER_NOT_APPROVED / UNIT_IDENTITIES_NOT_MATERIALIZED / BASELINE_X_H0_CC_NOT_MATERIALIZED / Q_X_MASSES_ABSENT / NO_SYNTHETIC_UNIT_CREATION / NO_MASS_ASSIGNMENT / Q_X_DEPENDENCY_BLOCKED / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

### 16.233.5. Siguiente gate independiente

**Gate 81 — auditoría de correspondencia entre las clases/mecanismos R0–R3 y los potenciales del harness integrado.** Sin depender del roster B1 ni de q_X*, determinar qué roles científicos de las celdas obligatorias C1/C3 están realmente representados por las funciones y parámetros ya implementados, cuáles son solo etiquetas/perillas disponibles y cuáles no pueden producirse o distinguirse con el DGP actual. Revisar en particular el contraste G frente a la intervención focal g_A, los potenciales por (Z,G), las vías directas/colaterales, signos, nulos, heterogeneidad, interferencia y abstención. No crear escenarios, no fijar valores de parámetros, no cambiar código ni ejecutar. El resultado debe ser una matriz de cobertura implementada/parametrizable/ausente y los bloqueos exactos, no otra propuesta de roster.


---

## 16.234. Gate 81 — correspondencia entre clases R0–R3, potenciales y cobertura científica del harness (2026-11-13)

**Precedencia:** §§16.223, 16.226, 16.231–16.233; harness 03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py, blob auditado 2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4. Auditoría estática del contrato y del código existente. No se ejecuta el harness, no se modifican funciones ni parámetros y no se crean escenarios.

### 16.234.1. Contrato efectivo del Generator

El Generator materializa potenciales V_i(z,g) indexados por unidad y por los cuatro regímenes (Z,G). Reutiliza las mismas exógenas de unidad entre regímenes, incluidas u_access, u_relation, u_context, u_mapping, u_provision, u_alt, u_trajectory y las secuencias temporales. G=0 produce el vector focal nulo; G=1 intenta habilitar conjuntamente las cuatro coordenadas, condicionado por provisión y por umbrales exógenos. El predicado focal es conjuntivo (all(delta_vector)), y Reach admite además la vía alternativa.

El resultado B1/V_cont se genera como conjunción temporal de ENABLED y PROFILE. La asignación Z modifica el resultado mediante mecanismos que ya existen en el código: package_direct_effect, reducción de provisión en R3 y modificación de la probabilidad de alternativa en R2; collateral_effect añade una vía Z × alternative. G puede afectar el resultado por el mecanismo focal de accesibilidad y, separadamente, por focal_direct_effect.

El Generator sí calcula los cuatro potenciales bajo (Z,G), pero el diseño de G no es una parametrización general de cualquier par de políticas conjuntas g_A0/g_A1: actualmente es una única regla binaria concreta, con vector cero para G=0 y una regla estocástica compartida de provisión/umbrales para G=1. No se declara soporte general para otras distribuciones vectoriales.

### 16.234.2. Hallazgo crítico: la verdad focal está definida como efecto de G, no separada de G

El código define:

- itt_package_truth como el promedio unitario de la diferencia Z=1 frente a Z=0, promediando los dos valores de G;
- theta_access_truth como el promedio de V_i(0,1) − V_i(0,0).

El segundo objeto es, por construcción, el efecto total de la asignación G bajo Z=0. Sin embargo, el mecanismo de resultado incluye focal_direct_effect × G. Cuando ese parámetro es distinto de cero, theta_access_truth incorpora una vía G→Outcome que no está mediada por ΔT_acc*. El contrato del Analyzer detecta la violación y se abstiene, pero el Evaluator sigue comparando cualquier resultado focal con una verdad que contiene esa vía directa.

Por ello, el actual theta_access_truth no es una verdad independiente del estimando focal causal θ_A. El problema no se resuelve renombrando la variable ni excluyendo del Analyzer las configuraciones directas: el Generator/Evaluator deben poder distinguir siempre el contraste de asignación G de la intervención causal sobre el vector ΔT_acc*.

La reparación conceptual requerida, sin decidir todavía su implementación, es conservar por separado:
1. theta_G_truth: contraste total de la asignación G bajo Z=0, incluidas sus vías directas;
2. theta_A_truth: contraste de las políticas conjuntas declaradas sobre el vector ΔT_acc*, con las vías directas de G excluidas del estimando y con las condiciones no focales fijadas según el contrato;
3. itt_package_truth: efecto total de Z bajo la política/distribución de G que defina el estimando ITT.

theta_A_truth debe derivarse mediante una intervención estructural sobre ΔT_acc* completo, no mediante la etiqueta G ni por el mero hecho de que G sea aleatorio. El par de políticas y su soporte siguen sujetos al contrato general de §§16.226 y 16.232; este gate no declara que el actual mecanismo G satisfaga por sí solo todas sus condiciones.

### 16.234.3. Matriz de cobertura de las celdas C1/C3

Estados: **I** = implementado como mecanismo/contraste; **P** = parametrizable en Generator, pero no cubierto/acreditado como celda del benchmark o del Analyzer; **A** = ausente como capacidad analítica o de verdad independiente.

| Rol obligatorio | Evidencia en código | Estado y límite |
|---|---|---|
| C1 ITT positivo | package_direct_effect; R2/R3 también pueden alterar Z→Outcome por vías alternativas/provisión | **I/P**: el mecanismo existe y el benchmark incluye R0_DIRECT_Z; falta una batería explícita que acredite la celda ITT positiva como verdad y recuperación |
| C1 ITT nulo propio | Configuración sin efecto Z; el benchmark contiene mundos sin efecto de paquete | **P**: el cero puede resultar por configuración o cancelación; no hay celda propia de nulo ITT identificada y protegida frente a cancelaciones accidentales |
| C1 ITT negativo | Efecto Z negativo parametrizable; R3 reduce provisión y R2 puede reducir alternativa | **P**: no hay una celda negativa explícita en benchmark_scenarios ni acreditación de su signo |
| C1 desacoplamiento ITT/focal | Efectos Z y G separados; R0 focal sin efecto Z y R2/R3 con vías Z diferenciadas | **I/P**: la estructura permite desacoplar; no está acreditado un par de contrastes de signos/valores preespecificados y recuperados |
| C1 heterogeneidad con signos opuestos | heterogeneity × (baseline_x−0.5) × trajectory | **P/A**: un coeficiente suficientemente grande puede generar signos condicionales opuestos, pero el benchmark actual (0.20 con efecto focal 0.20) no los genera; TruthBundle no publica el truth por estrato y Analyzer solo estima el efecto agregado |
| C1 no-identificación/abstención | Controles de interferencia, medición, versiones y asignación | **I/P**: hay abstención por condiciones declaradas; la cobertura depende de flags del contrato y no de diagnóstico completo de los datos |
| C3 focal positivo | focal_access_effect positivo y política G sobre las cuatro coordenadas | **I/P**: mecanismo presente; la verdad focal actual es el contraste G y no está separada de θ_A |
| C3 nulo propio | focal_access_effect=0 o vía alternativa que hace redundante la ruta focal (R1) | **P**: generable, pero no se distingue aún un nulo causal propio de un nulo por saturación/alternativa sin una descomposición de verdad |
| C3 negativo | focal_access_effect negativo | **I/P**: parámetro y candidato R0_FOCAL_ADVERSE presentes; recuperación frente a θ_A independiente no acreditada |
| C3 vía directa/colateral impeditiva | focal_direct_effect, package_direct_effect, collateral_effect, perfiles R1/R2/R3 | **I**: mecanismos presentes; el rechazo focal por vía directa G está codificado, pero la verdad del Evaluator queda contaminada como se documenta en §16.234.2 |
| C3 heterogeneidad focal con signos opuestos | Modificador por baseline_x en la ecuación de PROFILE | **P/A**: generable solo con valores adecuados; no hay truth ni estimación focal estratificados ni evaluación de recuperación por estrato |
| C3 no-identificación/abstención | Positividad, aleatorización G, exclusión focal, régimen común, medición e interferencia | **I/P**: abstención puntual implementada; no existen bounds ni identificación parcial |

### 16.234.4. Límites del Analyzer y del Evaluator

- El Analyzer estima ITT mediante diferencias de V_cont observado por Z y estima el contraste G mediante diferencias de V_cont entre G=1 y G=0 restringidas a Z=0. No estima una intervención general sobre ΔT_acc* ni una función de respuesta por vector.
- Las cuatro coordenadas delta_t_acc_observed se publican sin error ni missingness en el registro, aunque S3 sí puede tener error/missingness. El Analyzer usa esas coordenadas para un first stage descriptivo, pero no las usa para reconstruir o estimar θ_A. Por tanto, el first stage no convierte el contraste G en efecto causal del vector.
- contract_for deriva focal_direct_path_absent de que focal_direct_effect == 0, pero fija common_nonfocal_regime=True de forma constante. La condición común no se audita a partir de un registro explícito de políticas, versiones y vías mantenidas fijas.
- La positividad y otras condiciones llegan al Analyzer como declaraciones del contrato. El Analyzer no reconstruye por sí mismo el soporte conjunto de los vectores ni valida la verdad de las declaraciones contra el Generator.
- Para falta de medición, interferencia o problemas de identificación, el Analyzer se abstiene; no calcula bounds, conjuntos identificados, sensibilidad ni efectos parciales.
- La interferencia está incorporada como exposición de los otros miembros del clúster condicionada a sus asignaciones Z realizadas. El Analyzer rechaza la estimación individual bajo no_interference=False, pero no estima un contraste de exposición por clúster.
- La verdad ITT se calcula con ponderación 50/50 de G; la estimación observada compara los brazos Z con la mezcla G realizada. Con asignaciones marginalmente balanceadas pero sin balance factorial exacto garantizado, el estimador no es algebraicamente el mismo contraste estandarizado en cada muestra; su interpretación requiere el diseño aleatorio y la incertidumbre correspondientes.

### 16.234.5. Dictamen

**Gate 81 cerrado como auditoría estática de cobertura, no como validación de recuperación.**

Queda acreditado que el harness existente contiene potenciales (Z,G), cuatro coordenadas de ΔT_acc*, mecanismos focales, directos, alternativos, de provisión e interferencia, y un firewall Generator/Analyzer/Evaluator. También queda acreditado que varios roles son parametrizables. No queda acreditado que las doce celdas C1/C3 estén configuradas y recuperadas por el Analyzer.

Bloqueo principal: theta_access_truth representa actualmente el efecto total de G bajo Z=0, no una verdad causal θ_A separada de las vías directas de G. Bloqueos adicionales: ausencia de estimación/evaluación por estratos para heterogeneidad de signos opuestos; ausencia de bounds/identificación parcial; soporte conjunto y régimen común no validados desde registros de política; y cobertura de celdas positivas/nulas/negativas ITT no materializada como batería confirmatoria.

**Dictamen:** GATE_81_STATIC_HARNESS_COVERAGE_AUDIT_CLOSED / ZG_POTENTIALS_IMPLEMENTED / FOUR_COORDINATE_DELTA_TACC_IMPLEMENTED / DIRECT_ALTERNATIVE_PROVISION_INTERFERENCE_MECHANISMS_PRESENT / THETA_G_AND_THETA_A_TRUTH_CONFLATED / ITT_AND_FOCAL_ROLE_COVERAGE_PARTIAL / SIGN_OPPOSED_HETEROGENEITY_NOT_ANALYZED / PARTIAL_IDENTIFICATION_BOUNDS_ABSENT / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

### 16.234.6. Siguiente gate

**Gate 82 — contrato de verdad causal independiente del Generator/Evaluator.** Resolver, reutilizando los potenciales existentes y sin modificar todavía código, las definiciones operativas separadas de ITT_D2, theta_G y theta_A; especificar la intervención conjunta sobre ΔT_acc* completo, la exclusión de vías directas de G, las condiciones no focales mantenidas, la relación entre el par g_A0/g_A1 y el mecanismo actual G, y qué debe comparar exactamente el Evaluator en mundos limpios, directos, colaterales y no identificados. El gate debe terminar con ecuaciones de verdad y criterios de adjudicación que puedan traducirse después al harness sin cambiar el estimando por conveniencia. No volver a diseñar Value/V_cont, no crear mundos ni parámetros, no implementar ni ejecutar.


---

## 16.235. Gate 85 — matriz integrada de reconciliación e implementación C10-S (2026-11-13)

**Precedencia:** §§16.223–16.234; contrato DGP temporal/roles; inventario finito R0–R3; harness integrado `03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py` (blob `2dafb9cdc4a6e0b5b6d686acc74bdecc71dbead4`); tests `test_vcont_integrated_harness.py` (blob `791530c34f154bc11a4360a676af54db8fd4c8ce`); P178 clean replay closure audit 001 (blob `f8b52ed0be4e7d74a8a5bfc226f7cd32d4d138d4`); P178 replay performance diagnostic 001 (blob `a8b29379339a3ddcb6374530742e1b9d5b9684d8`). Gate de reconciliación estática y secuenciación de implementación. No modifica código, estimandos congelados, roster, parámetros, mundos, tamaños muestrales ni protocolo de ejecución.

### 16.235.1. Reconciliación canónica y reconstrucción histórica

La lectura de `00_GOVERNANCE/README.md`, `CHATGPT_BOOTSTRAP.md`, `CANONICAL_STATE.json`, `STATUS.md`, punteros RMA/matriz y traceability en `main` confirma una cadena consistente: RMA v3.38, Evidence→Claim Matrix v1.47, RMA traceability v3.38 y Governance Operating Principles v0.1. La discrepancia RMA 3.37/3.38 comunicada en una revisión conversacional anterior no está presente en los artefactos actuales consultados; se considera resuelta por el estado canónico actual, no por inferencia ni edición local. No se modifica `main`.

La rama `research/c10-s-consolidation-draft` contiene el plan integrado en `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md`. Se conserva su historial y se añade esta reconciliación sin reescribir gates previos. El encabezado/siguiente operación histórico del documento todavía apunta a Gate 81; ese texto queda reconocido como routing histórico obsoleto frente a las secciones de gates ya añadidas. No se reescribe en este gate para evitar una edición amplia y no necesaria; la continuidad posterior debe seguir el último gate secuencial registrado.

### 16.235.2. Evidencia histórica que se reutiliza — P178

P178 no es un experimento causal integrado de Generator/Projector/Analyzer/Evaluator. Es un benchmark Monte Carlo metodológico del Analyzer y se reutiliza únicamente para lo que acredita.

La auditoría `P178_CLEAN_REPLAY_CLOSURE_AUDIT_001.md` registra:
- 27 celdas (K=2,10,50 × π0=0.2,0.5,0.8 × nulo/positivo/negativo);
- N=700 por celda, R=10.000, 270.000 invocaciones;
- 17 pruebas de contrato PASS;
- replay limpio completo, 27/27 comparaciones `reference_match=True`;
- CSV y manifiesto byte-idénticos;
- cierre: COMPUTATIONAL REPRODUCIBILITY PASS / NON-CONFIRMATORY METHODOLOGICAL CALIBRATION.

El diagnóstico de rendimiento conserva la historia de intentos de replay incompletos anteriores; su cierre posterior documenta el replay completo y byte-idéntico. No se interpreta el diagnóstico de rendimiento como sustituto ni como revocación de la auditoría final. P178 no cubre las verdades θ_Z/θ_G/θ_A del DGP integrado, vías directas/colaterales, soporte conjunto de intervenciones focales, heterogeneidad focal por estratos, interferencia ni identificación parcial. No se repite P178 ni se usa su PASS como evidencia causal C10-S.

### 16.235.3. Matriz única de implementación integrada

Estados: **EXISTE** = función/campo/camino implementado en el harness; **PARCIAL** = mecanismo parametrizable o representación presente, sin contrato/cobertura suficiente; **AUSENTE** = capacidad necesaria no implementada; **REUTILIZAR** = evidencia previa válida dentro de su alcance, sin duplicarla.

| Bloque | Estado actual verificado | Brecha exacta | Acción mínima de implementación posterior | Aceptación exigida |
|---|---|---|---|---|
| Generator: potenciales (Z,G) | EXISTE: V_i(z,g), cuatro regímenes, exógenos compartidos | G se documenta como intervención sobre g_A, pero no existe una familia de potenciales que intervenga separadamente sobre el vector A bajo r_common y permita adjudicar θ_A sin el término directo de G | Añadir la evaluación estructural focal requerida por el contrato congelado, reutilizando mecanismos y exógenos existentes; no crear perfiles nuevos | Identidad de potenciales y consistencia; contraste focal invariante a la vía directa de G; tests de acoplamiento |
| Generator: θ_Z | EXISTE: `itt_package_truth`, promedio 50/50 sobre G | El estimando depende del régimen G marginal definido; estimador por asignación observada y verdad estandarizada no son algebraicamente idénticos en cada muestra | Mantener la definición ITT vigente y documentar el régimen/estimador compatible; no redefinir C1 por conveniencia | Verdad y estimador comparan el mismo target; incertidumbre/calibración conforme al diseño |
| Generator: θ_G | PARCIAL: contraste V(0,1)-V(0,0) computable desde potenciales | No hay campo/identidad separado en TruthBundle; actualmente se etiqueta como `theta_access_truth` | Exponer `theta_g_truth` como verdad total de asignación G, incluidas vías directas | En R0 limpio, θ_G coincide con el contraste focal solo bajo condiciones de equivalencia; con vía directa difiere |
| Generator: θ_A | AUSENTE como verdad independiente | No existe potencial focal bajo intervención conjunta A/r_common; θ actual hereda el efecto total G | Incorporar potenciales/verdad focales independientes conforme a §16.234 y al contrato de políticas factibles; no fijar aquí valores ni extremos nuevos | El Evaluator recupera θ_A independiente; activar efecto directo de G no altera θ_A cuando A y r_common se mantienen |
| TruthBundle | PARCIAL: guarda potenciales (Z,G), intervalos, enabled/profile, ΔT_acc, ITT y theta_access | No publica θ_G y θ_A separados, políticas/versión, r_common, soporte o verdades estratificadas | Extender el bundle con identidades de estimando/política, verdades separadas, soporte y descomposición por estrato necesaria | Esquema versionado, completo, reproducible y sin fuga al Analyzer |
| Projector | EXISTE: evidencia observada S3, Z/G, coordenadas observadas, unidad/clúster, estrato | Publica las cuatro coordenadas sin error/missingness; el first stage descriptivo no estima la respuesta causal a A; no acredita por sí mismo r_common/soporte | Mantener la frontera de información; publicar solo variables autorizadas por el contrato y estados reales de observación/medición | Pruebas negativas de ausencia de truth, potenciales, parámetros DGP y flags privados |
| Sealer | EXISTE: whitelist de campos, hash e integridad | Whitelist y schema actual no llevan contrato auditable de política/soporte común | Versionar schema y sellar metadatos observables de diseño necesarios, sin incorporar truth | Tampering detectado; schema exacto; procedencia/versiones preservadas |
| Analyzer: ITT | EXISTE: diferencia observada V_cont por Z y SE | El target observado debe alinearse explícitamente con la verdad estandarizada sobre G | Conservar estimador o justificar ajuste compatible con el estimando ya congelado; no cambiar estimando | Recuperación/calibración para positivos, nulos y negativos ITT, con incertidumbre |
| Analyzer: efecto G | EXISTE: contraste G en Z=0 | No está presentado como θ_G separado de θ_A en salida/contrato | Identificarlo explícitamente como efecto de asignación G y no como estimador focal por defecto | Recupera θ_G cuando sus supuestos de asignación/medición/soporte se cumplen |
| Analyzer: θ_A | AUSENTE | No estima intervención general/conjunta sobre A ni respuesta focal independiente; usa contraste G condicionado a flags | Implementar estimador focal solo tras fijar identificación, soporte, política, régimen común y evidencia admisible | Recuperación focal independiente; abstención cuando supuestos no identificados; no confundir first stage con efecto |
| Analyzer: heterogeneidad | AUSENTE como inferencia focal por estrato | Solo existe modificador DGP por baseline_x; no publica truth/estimación focal condicional | Añadir estimación/diagnóstico por estratos predefinidos en contrato existente, sin escoger cortes post hoc | Recuperación de efectos condicionales y detección de signos opuestos; agregado compatible con verdad |
| Analyzer: bounds | AUSENTE | Abstención puntual, sin conjunto identificado ni bounds | Diseñar bounds solo para fuentes de no-identificación donde el contrato y evidencia los permitan; si no, abstención explícita | Cobertura/validez de bounds y abstención correcta; no reportar punto identificado |
| Evaluator | PARCIAL: compara package/focal con TruthBundle y verifica abstención | Focal se compara con verdad G contaminada; no adjudica tres verdades ni estratos, falsos positivos ni bounds | Comparar separadamente θ_Z, θ_G y θ_A; adjudicar falsos positivos de atribución, heterogeneidad y estados no identificados | Adjudicación independiente y exhaustiva por rol de celda; no leer truth antes del sellado |
| Ledger C1/C3 | PARCIAL: benchmark_scenarios tiene 12 configuraciones candidatas R0–R3 | No coincide con las doce celdas obligatorias del Gate 71: son escenarios/mecanismos, no ledger de roles con criterios de aceptación | Mapear clases existentes a los seis roles C1 y seis C3; una clase puede cumplir varios roles si cada verdad/mecanismo se demuestra; no crear mundos por correspondencia nominal | Cada celda tiene scenario_ref existente, truth target, evidencia, criterio, resultado y estado |
| Tests adversariales | PARCIAL: tests de positivo, directo, alternativa, R2/R3, soporte, missingness, interferencia, integridad | Faltan tests independientes de θ_G/θ_A, desacoplamiento de signos, nulo propio, heterogeneidad focal de signos opuestos y adjudicación de bounds | Añadir únicamente pruebas faltantes sobre las funciones existentes | Cinco contrastes adversariales y doce roles C1/C3 superados; negativos de firewall |
| P178 | REUTILIZAR | No es cobertura causal del harness integrado | No modificar ni repetir; citarlo como calibración/reproducibilidad metodológica del Analyzer | Preservar su alcance no confirmatorio y sus límites |

### 16.235.4. Mapeo de las doce celdas C1/C3 a clases existentes

El roster finito de escenarios del harness contiene R0_FOCAL_POSITIVE, R0_FOCAL_NULL, R0_FOCAL_ADVERSE, R0_DIRECT_G, R0_DIRECT_Z, R1_ALTERNATIVE_BASELINE, R2_ALTERNATIVE_AFFECTED, R3_PROVISION_FAILURE, R0_MEASUREMENT_ADVERSE, R0_INTERFERENCE, R0_SUPPORT_FAILURE y R0_HETEROGENEITY. Este inventario se reutiliza; no se crea ningún mundo adicional.

| Celda | Clase/escenario existente candidato | Estado actual | Condición de acreditación |
|---|---|---|---|
| C1-1 ITT positivo | R0_DIRECT_Z / R2 / R3, según truth efectiva | PARCIAL | θ_Z>0 y recuperación ITT |
| C1-2 ITT nulo propio | R0_FOCAL_POSITIVE u otra configuración existente con Z sin vía causal | PARCIAL | θ_Z=0 por mecanismo nulo propio, no cancelación accidental; recuperación/IC compatible |
| C1-3 ITT negativo | R3_PROVISION_FAILURE o R0_DIRECT_Z con mecanismo existente | PARCIAL | θ_Z<0 en verdad DGP y recuperación ITT |
| C1-4 Desacoplamiento ITT/focal | R0_DIRECT_Z / R2 / R3 | PARCIAL | θ_Z y θ_A con relación/signos adversariales preespecificados y ambos targets recuperados |
| C1-5 Heterogeneidad de signos opuestos | R0_HETEROGENEITY | AUSENTE analíticamente | θ_A(x) con signos opuestos, estimación por estrato y agregado adjudicados |
| C1-6 No-identificación/abstención | R0_SUPPORT_FAILURE / R0_MEASUREMENT_ADVERSE / R0_INTERFERENCE | PARCIAL | Analyzer se abstiene por diagnóstico respaldado en evidencia; no solo flag no verificado |
| C3-1 Focal positivo | R0_FOCAL_POSITIVE | PARCIAL | θ_A independiente >0 y recuperación |
| C3-2 Focal nulo propio | R0_FOCAL_NULL | PARCIAL | θ_A=0 estructuralmente, distinguido de saturación R1 y cancelación |
| C3-3 Focal negativo | R0_FOCAL_ADVERSE | PARCIAL | θ_A independiente <0 y recuperación |
| C3-4 Vía directa/colateral impeditiva | R0_DIRECT_G / R2_ALTERNATIVE_AFFECTED / R3_PROVISION_FAILURE | PARCIAL | θ_G≠θ_A cuando corresponde; no atribución falsa; abstención o estimando alternativo válido |
| C3-5 Heterogeneidad focal de signos opuestos | R0_HETEROGENEITY | AUSENTE analíticamente | Efectos focales condicionales de signos opuestos, estimados y adjudicados |
| C3-6 No-identificación/abstención | R0_SUPPORT_FAILURE / R0_MEASUREMENT_ADVERSE / R0_INTERFERENCE | PARCIAL | Estado correcto IDENTIFIED/NOT_IDENTIFIED/INDETERMINATE; bounds solo si válidos |

Las etiquetas de escenario no constituyen por sí mismas la verdad ni acreditan la celda. Los signos y ceros se comprobarán sobre las verdades generadas, no se inferirán de los nombres ni del signo aislado de un parámetro.

### 16.235.5. Orden mínimo de implementación posterior

La implementación debe realizarse como una única reconciliación integrada, manteniendo la separación Generator → Projector → Sealer → Analyzer → Evaluator:

1. **Congelar el contrato de estimandos/políticas** usando §§16.226, 16.231 y 16.234: θ_Z, θ_G, θ_A; relación G↔A; régimen no focal común; soporte/factibilidad y población aplicable. No se codifica una elección no resuelta como si estuviera aprobada.
2. **Extender Generator/TruthBundle** para producir verdades independientes y descomposición por estrato, reutilizando los mecanismos R0–R3 y exógenos existentes.
3. **Ajustar Projector/Sealer** solo para transportar evidencia observable y metadatos de política/diseño necesarios; mantener truth y parámetros privados fuera del Analyzer.
4. **Implementar Analyzer** en este orden: ITT target-compatible; contraste θ_G identificado como tal; estimación θ_A solo bajo condiciones verificables; análisis por estrato; bounds donde procedan y abstención en lo demás.
5. **Rehacer Evaluator** para tres verdades independientes, recuperación, falsos positivos de atribución, heterogeneidad y abstención/bounds.
6. **Materializar el ledger** de doce roles mediante referencias a escenarios existentes y criterios explícitos; no añadir mundos para rellenar celdas.
7. **Añadir tests adversariales faltantes** y ejecutar primero pruebas unitarias/software autorizadas por el workflow, separadas de cualquier ejecución científica. P178 no se repite.
8. **Preflight y autorización científica independiente** antes de cualquier benchmark confirmatorio o ejecución del experimento.

No se debe implementar el estimador θ_A antes de resolver el par de políticas factibles y su régimen común. La ausencia del roster B1/UE y q_X* sigue siendo una dependencia separada: no se rellena con el baseline_x aleatorio del harness. Esta dependencia bloquea la materialización de la población causal por historia, pero no justifica inventar unidades ni impide completar tareas de software que sean válidas sin reclamar evidencia poblacional.

### 16.235.6. Dictamen del Gate 85

**Gate 85 cerrado como matriz integrada de reconciliación y secuencia de implementación; no es Design Freeze ni autorización de código/ejecución.**

Se ha identificado una ruta de implementación única y reutilizable. P178 queda preservado dentro de su alcance real. Los bloqueos de θ_A, estimación por estratos, validación de soporte/régimen común, bounds y materialización de q_X* permanecen explícitos. No se crean escenarios, parámetros, unidades, masas, estimandos ni valores de resultado. No se reabre Value ni V_cont.

**Dictamen:** GATE_85_INTEGRATED_IMPLEMENTATION_MATRIX_CLOSED / CANONICAL_BOOTSTRAP_CONSISTENT / P178_REPLAY_REPRODUCIBILITY_REUSED_WITH_BOUNDED_SCOPE / GENERATOR_TRUTH_SEPARATION_REQUIRED / THETA_A_ESTIMATOR_ABSENT / STRATIFIED_HETEROGENEITY_ANALYSIS_ABSENT / PARTIAL_IDENTIFICATION_BOUNDS_ABSENT / C1_C3_LEDGER_NOT_YET_MATERIALIZED / NO_NEW_WORLDS / NO_CODE_CHANGE / NO_EXECUTION / DESIGN_FREEZE_NOT_GRANTED.

### 16.235.7. Siguiente gate — 86

**Gate 86 — resolver el contrato de intervención focal G↔A y el estimando θ_A a partir de las decisiones congeladas existentes.** Antes de implementar el Generator/TruthBundle, inspeccionar §§16.208, 16.211–16.212, 16.226, 16.231 y los Decision Records D2; establecer si el mecanismo G actual puede reutilizarse como política estocástica focal o si el contrato exige políticas distintas, qué significa mantener r_common y cómo se acredita factibilidad/soporte sin inventar extremos ni depender de q_X* no materializado. El resultado debe ser una decisión operativa derivada de los contratos existentes o una lista cerrada de dependencias bloqueantes. No modificar código, no crear políticas/valores nuevos, no ejecutar.


---

## 16.236. Gate 86 — adjudicación del contrato G↔g_A, q_X* y r_common (2026-11-13)

**Precedencia:** §§16.208.3–16.208.8, 16.209–16.212, 16.223, 16.226.2–16.226.6, 16.230–16.233 y matriz integrada §16.235. Este gate adjudica únicamente lo que puede resolverse desde decisiones y contratos existentes. No crea políticas, historias, masas, mundos, parámetros ni estimandos; no modifica código ni ejecuta.

### 16.236.1. Decisión sobre reutilización de G

**G no puede reutilizarse como g_A ni su contraste como θ_A.** Esta decisión se desprende de §16.226.3 y queda confirmada por la auditoría de implementación de §16.231:

- G es una asignación/encouragement aleatorizado con potenciales V(z,g); sus efectos incluyen fallo de provisión y cualquier vía directa o colateral que el DGP permita.
- El vector ΔT_acc* observado bajo G es una primera etapa vectorial aleatoria y potencialmente incompleta: cada coordenada depende de G, provisión y exógenas. No es la aplicación de una regla de intervención focal conjunta especificada.
- Por tanto, ITT_G|Z=0 conserva su identidad de efecto de asignación. No es θ_A y no se usa como sustituto, ni se convierte en θ_A por renombrado, ajuste por primera etapa o acoplamiento exógeno.
- La igualdad ITT_G|Z=0=θ_A solo sería admisible si se demostraran todas las condiciones de equivalencia de §16.226.3. El harness y el ledger actuales no las acreditan.

Se mantiene el contrato de tres verdades: ITT_Z bajo G_REGIME_MARGINAL_50_50_V1; ITT_G|Z=0 como efecto de asignación auxiliar; θ_A como efecto de intervención focal sobre el vector completo.

### 16.236.2. Decisión sobre la forma de g_A0/g_A1

Prevalece la forma general congelada en §16.226.2.C y precisada en §16.231.1:

- dos reglas explícitas/versionadas sobre la **distribución conjunta** del vector completo ΔT_acc*;
- condicionadas por historia basal h;
- definidas sobre una misma población q_X*;
- factibles y con soporte conjunto en las historias con masa positiva;
- evaluadas bajo el mismo r_common.

No se ratifican como políticas confirmatorias los extremos deterministas (0,0,0,0) y (1,1,1,1) propuestos en §16.230.2: §16.231.4 los deja como candidatos no validados. Tampoco se sustituyen por kernels estocásticos alternativos, distribuciones suavizadas ni políticas elegidas para producir positividad. No existe en las decisiones congeladas otro par versionado de políticas que pueda reemplazarlos.

**Resultado:** la forma del estimando está definida; la identidad operativa de g_A0/g_A1 no puede seleccionarse con el expediente actual. Queda bloqueada por ausencia de dominio semántico conjunto, historias q_X*, masas y soporte por historia, no por una necesidad de crear más alternativas teóricas.

### 16.236.3. q_X*: qué está fijado y qué falta

Se conserva la definición funcional de §16.209.2:

q_X* = Law(X, H0, C_c | i ∈ P*_{τ2}).

La población primaria candidata y sus criterios basales mantienen la precedencia ya adjudicada. q_X* es una distribución objetivo conjunta de historias pre-Z; no es la asignación Z/G, la frecuencia de baseline_x, el roster de clases R0–R3, la cohorte Need_preZ ni el número de unidades del harness.

Los contratos §§16.232–16.233 establecen que:
- el registro hijo por historia y sus campos están definidos;
- no existe roster B1/UE aprobado/materializado;
- no hay filas versionadas X/H0/C_c ni snapshots basales por unidad;
- no hay masas q_X* ni soporte conjunto de las dos políticas;
- no hay autorización de materialización en este ciclo.

Por tanto, q_X* está definido simbólicamente, pero no materializado. No se derivan pesos de frecuencias sintéticas, ni se restringe la población para acomodar políticas no soportadas.

### 16.236.4. r_common: significado operativo y límite de acreditación

r_common significa mantener idénticos, en ambos potenciales focales, el régimen y las condiciones no focales relevantes: política/paquete Z y G según el régimen declarado, alternativas y rutas colaterales, recursos, contexto, versiones, horizonte y mecanismos/exógenas no focales. Solo se recalculan los descendientes causales de la intervención sobre ΔT_acc*.

El mismo identificador de semilla o el acoplamiento de exógenas no basta para declarar COMMON_FIXED: debe acreditarse que las funciones estructurales no focales y sus versiones son invariantes entre ambos brazos contrafactuales y que ninguna vía colateral cambia diferencialmente. Si una vía cambia, se registra como DIFFERENTIAL_IDENTIFIED o DIFFERENTIAL_UNRESOLVED; no se atribuye a θ_A.

Puede congelarse esta regla semántica ahora, pero no emitir certificados COMMON_FIXED por historia/celda porque no existen las filas q_X* ni el soporte materializado. En mundos R1/R2/R3 la invariancia se evalúa según el mecanismo concreto; no se presume por perfil.

### 16.236.5. Dictamen y dependencias bloqueantes

| Cuestión | Dictamen |
|---|---|
| ¿G equivale a g_A? | NO; asignación/primera etapa distinta de intervención focal |
| ¿ITT_G|Z=0 es θ_A? | NO, salvo equivalencia completa demostrada; hoy no acreditada |
| Forma de g_A | Reglas conjuntas condicionadas por historia sobre ΔT_acc* completo |
| Par de políticas operativo | BLOCKED; extremos de §16.230 no validados y no hay alternativa congelada |
| q_X* | Definido simbólicamente; roster, historias, masas y soporte no materializados |
| r_common | Regla semántica definida; invariancia estructural y certificados por historia no acreditados |
| Nuevas políticas/mundos/parámetros | PROHIBIDOS en este gate |

**Gate 86 cerrado como adjudicación de dependencias, no como selección de políticas ni identificación de θ_A.** No queda una decisión documental adicional que pueda resolver la ausencia de roster, historias, masas y soporte. No se abre otro inventario narrativo ni se solicita repetir el mismo trabajo.

**Dictamen:** GATE_86_G_NOT_EQ_G_A / ITT_G_Z0_NOT_THETA_A / JOINT_HISTORY_CONDITIONAL_POLICY_FORM_RETAINED / EXTREME_POLICIES_UNVALIDATED / Q_X_MATERIALIZATION_BLOCKED / R_COMMON_SEMANTIC_RULE_CLOSED_BUT_PER_HISTORY_CERTIFICATION_BLOCKED / NO_NEW_POLICIES_OR_WORLDS / NO_CODE_CHANGE / NO_EXECUTION / NOT_DESIGN_FROZEN.

### 16.236.6. Siguiente operación — Gate 87

**Gate 87 — separar e implementar únicamente el contrato de verdades ya identificable en el harness, sin fingir que θ_A está resuelto.** Antes de modificar código, preparar una intervención técnica acotada y reversible sobre Generator/TruthBundle/Evaluator para:
1. conservar itt_package_truth bajo el régimen G_REGIME_MARGINAL_50_50_V1 como ITT_Z;
2. exponer el contraste actual V(0,1)-V(0,0) como itt_g_z0_truth, con migración/alias explícitos y sin llamarlo θ_A;
3. dejar θ_A explícitamente NOT_MATERIALIZED/no disponible, sin estimador ni truth ficticia;
4. añadir pruebas de no-equivalencia cuando la vía directa de G esté activa y de equivalencia únicamente bajo condiciones de control positivo que el DGP existente permita demostrar;
5. preservar el firewall: ninguna verdad, potencial contrafactual o parámetro oculto pasa al Analyzer.

La intervención no debe tocar el estimador θ_A, q_X*, políticas g_A, roster B1/UE, masas, bounds, R0–R3 ni resultados P178. Primero se comprobarán permisos/workflow y el alcance exacto de la edición; solo se modificará código si la autorización aplicable lo permite. No ejecutar benchmark ni simulación científica. scientific_execution=false; execution_authorized=false.


---

## 16.237. Gate 87 — separación implementada de ITT-Z, ITT-G|Z=0 y θ_A no materializado (2026-11-13)

**Precedencia:** §16.235 (matriz integrada), §16.236 (G no equivale a g_A), §§16.226.3–16.226.5 y §16.234 (auditoría del Generator). Alcance: corrección acotada de semántica en Generator/TruthBundle/AnalyzerResult/Evaluator y tests de contrato. No modifica el DGP, mecanismos R0–R3, asignaciones, exógenas, estimandos congelados, roster, políticas g_A, q_X*, masas, bounds, Projector, Sealer ni P178. No ejecuta pruebas ni benchmark.

### 16.237.1. Corrección del contrato de verdad

Se elimina el campo ambiguo `theta_access_truth`. TruthBundle distingue ahora:

- `itt_z_truth`: contraste Z promediado sobre G según el régimen marginal 50/50 ya implementado;
- `itt_g_z0_truth`: contraste total V(0,1)−V(0,0), incluidas las vías directas/colaterales que el DGP haga operar bajo G;
- `theta_a_truth`: `None` / NOT_MATERIALIZED. No se calcula ni se aproxima mediante G.

Se conserva `itt_package_truth` únicamente como propiedad alias de compatibilidad explícita hacia `itt_z_truth`; no existe alias equivalente de `theta_access_truth`, porque perpetuaría la falsa identidad semántica.

### 16.237.2. Corrección del contrato de salida y evaluación

AnalyzerResult deja de etiquetar el contraste estimado de G como `focal_effect`; sus campos son `g_assignment_status`, `g_assignment_effect` y `g_assignment_se`. El Analyzer sigue recibiendo exclusivamente SealedEvidence y AnalysisContract: no recibe TruthBundle, potenciales, parámetros del Generator ni `theta_a_truth`.

El contraste G es un efecto de asignación aleatorizada. Una vía directa G→Outcome no invalida su interpretación como ITT-G|Z=0; sí impide identificarlo con θ_A. En consecuencia, el Analyzer ya no se abstiene del contraste de asignación G únicamente por la presencia de una vía directa G ni por el requisito de régimen no focal común que pertenece a la atribución de θ_A. Mantiene las condiciones de aleatorización G, soporte, medición, versión e interferencia que sí afectan a la estimación del contraste G bajo el contrato implementado.

Evaluator compara:
- `package_itt` con `itt_z_truth`;
- `g_assignment_effect` con `itt_g_z0_truth`;
- nunca compara una estimación G con θ_A.

Los campos del informe pasan a `g_assignment_abs_error` y `g_assignment_recovered`. La evaluación de θ_A queda expresamente fuera de alcance hasta que existan políticas conjuntas factibles, q_X* y r_common certificables.

### 16.237.3. Pruebas añadidas/actualizadas

La suite de contrato contiene 15 tests declarados. Se añade una prueba que verifica:
- `theta_a_truth is None` tanto en R0 focal limpio como en R0 con vía directa G;
- `itt_g_z0_truth` se conserva en ambos casos;
- manteniendo el mismo seed/exógenas, la vía directa G modifica el contraste total G, demostrando que este incorpora dicha vía y no debe etiquetarse como θ_A.

Los tests previos se migran a los nombres semánticos ITT-Z y asignación G. El test de vía directa comprueba que el Analyzer puede estimar el ITT-G cuando las condiciones de identificación de esa asignación se cumplen; el test de fallo de soporte mantiene la abstención. Los tests no se han ejecutado en este gate.

### 16.237.4. Verificación estática y procedencia

Cambios en la rama `research/c10-s-consolidation-draft`:

| Artefacto | Blob final |
|---|---|
| `vcont_integrated_harness.py` | `74e530028721b6f91312c852931fea425e8b3493` |
| `test_vcont_integrated_harness.py` | `83e47323ddd50437cc436ab0a341479ea6ec9ac4` |

Comprobaciones estáticas tras recuperar los blobs finales:
- no quedan referencias a `theta_access_truth`;
- no quedan campos `focal_status/focal_effect/focal_se` en el contrato de salida;
- `theta_a_truth` está declarado como opcional y se materializa como `None`;
- Evaluator compara la salida G exclusivamente con `itt_g_z0_truth`;
- 15 funciones de test presentes y nombres sintácticamente válidos;
- Projector, Sealer y su whitelist no se han modificado.

Estas comprobaciones no equivalen a compilación, ejecución de tests ni validación estadística.

### 16.237.5. Dictamen y límites

**Gate 87 cerrado como corrección semántica implementada y estáticamente verificada; aceptación de software pendiente de ejecución autorizada.**

Se ha eliminado la contaminación de verdad del Evaluator: el contraste G ya no se presenta como θ_A. Se ha corregido también la salida del Analyzer para identificar el estimando que efectivamente estima. La presencia de una vía directa G cambia el ITT-G, pero no lo convierte en efecto focal de accesibilidad.

No se ha implementado la intervención estructural conjunta g_A0/g_A1, ni θ_A, ni sus potenciales, ni el soporte por historia, ni bounds. No se afirma recuperación causal de ΔT_acc*. La corrección no añade mundos, parámetros, unidades, distribuciones ni valores DGP. No se ha ejecutado ningún test, simulación o benchmark.

**Dictamen:** GATE_87_TRUTH_SEPARATION_IMPLEMENTED / ITT_Z_AND_ITT_G_Z0_DISTINCT / THETA_A_NOT_MATERIALIZED / ANALYZER_FIREWALL_PRESERVED_BY_STATIC_CONTRACT / EVALUATOR_NO_LONGER_ADJUDICATES_G_AS_THETA_A / STATIC_CHECKS_PASS / TESTS_NOT_RUN / NO_SCIENTIFIC_EXECUTION / NO_DESIGN_FREEZE.

### 16.237.6. Siguiente gate — 88

**Gate 88 — auditoría estática de integridad de la migración y del contrato Analyzer/Evaluator.** Comprobar consumidores, serialización/hash del AnalyzerResult, informes, contratos y tests para detectar referencias obsoletas o incompatibilidades; confirmar que el contraste G se identifica solo como ITT-G|Z=0 y que θ_A no puede aparecer como identificado por ningún alias, campo o reporte. Corregir únicamente residuos de esta migración. No implementar θ_A, no modificar el DGP ni ejecutar tests. La ejecución de la suite queda sujeta a autorización técnica explícita separada y no es ejecución científica.


---

## 16.238. Gate 88 — auditoría de integridad de migración y condiciones de identificación separadas (2026-11-13)

**Precedencia:** §§16.236–16.237 y Technical Execution Workflow v0.1. Alcance: auditoría estática de la migración ITT-Z / ITT-G|Z=0 / θ_A en el harness integrado, consumidores del PR, sellado del resultado y separación del harness P178 histórico. No implementar θ_A ni modificar DGP, P178, políticas g_A, q_X*, roster, masas o bounds.

### 16.238.1. Auditoría del contrato AnalyzerResult / hash / Evaluator

La recuperación completa de `vcont_integrated_harness.py` confirma que el payload sellado por Analyzer y el payload reconstruido por Evaluator utilizan el mismo contrato de salida:
- `package_status`, `g_assignment_status`;
- `package_itt`, `g_assignment_effect`;
- `first_stage_delta_t_acc`;
- `package_se`, `g_assignment_se`;
- `reasons`, `input_sha256`.

El digest de salida se calcula sobre ese payload y Evaluator reconstruye los mismos campos antes de comparar con las verdades respectivas. No se encontró un campo de θ_A en AnalyzerResult ni una ruta por la que Evaluator compare `g_assignment_effect` con `theta_a_truth`.

La migración integrada no conserva referencias a `theta_access_truth`, `focal_status` o `focal_effect` en el contrato de salida. El alias `itt_package_truth` solo apunta a `itt_z_truth`; no existe alias focal equivalente.

### 16.238.2. Incidencia corregida: dependencia indebida de Z para estimar G

La auditoría encontró que el Analyzer condicionaba la construcción de `observed_v` a que no existieran motivos de abstención de ITT-Z. Eso acoplaba indebidamente el contraste de G dentro de Z=0 a la aleatorización de Z.

Se corrigió separando:
- requisitos compartidos de evidencia/resultado (no interferencia, medición, versión, completitud y cobertura);
- requisitos propios de ITT-Z (aleatorización Z);
- requisitos propios de ITT-G|Z=0 (aleatorización G y soporte).

El resultado observado se construye cuando se satisfacen los requisitos compartidos. Después, cada estimando se adjudica contra sus condiciones propias. Una falta de aleatorización Z deja ITT-Z como `NOT_IDENTIFIED`, pero no bloquea por sí sola ITT-G|Z=0 si G está aleatorizado y el soporte dentro de Z=0 es suficiente.

Se añadió el test `test_g_assignment_does_not_require_z_randomization`, que también comprueba que Evaluator registra correctamente la abstención de ITT-Z y conserva la recuperación del contraste G.

### 16.238.3. Separación del harness integrado y el harness histórico P178

La revisión de los 175 ficheros del PR #116 y de los consumidores relevantes confirma dos implementaciones distintas:
- `vcont_integrated_harness.py` / `test_vcont_integrated_harness.py`: harness integrado al que se aplica Gate 87–88.
- `focal_harness.py`, sus tests y los puentes P178: harness anterior e independiente. Sus campos históricos `theta_access_truth` y `focal_*` no se han migrado ni se deben reinterpretar como el θ_A conjunto de la especificación integrada.

Se actualizó `03_EXPERIMENTS/C10-S/harness/README.md` para dejar explícita esta frontera. P178 y sus artefactos permanecen intactos. La búsqueda de referencias en la rama de investigación debe entenderse dentro de esta separación; no se declara que todo el repositorio haya eliminado vocabulario focal histórico.

### 16.238.4. Ejecución CI automática no prevista y resultado observado

El push documental que actualizó el README coincidió con el filtro `paths: 03_EXPERIMENTS/C10-S/harness/**` del workflow `.github/workflows/c10-s-focal-harness-tests.yml`. GitHub Actions lanzó automáticamente el workflow, sin que se hubiera solicitado una ejecución manual ni se pretendiera autorizarla mediante este gate.

Registro observado:
- Workflow run: `43411488324`.
- Commit probado: `dd886afd1bc68de231f5675e5364602914088453`.
- Evento: `push`.
- Job: `131838734939`.
- Resultado: `FAILURE`.
- Suite: 33 tests; 32 PASS y 1 FAIL.
- Compilación declarada por el workflow: PASS.
- Replay: SKIPPED al fallar la ejecución primaria.

El único fallo fue `test_structural_support_failure_removes_high_stratum_g1` (línea 123 en el blob probado), que espera `g_assignment_status == IDENTIFIED`. El test `test_support_failure_blocks_g_assignment_but_not_package` espera para el mismo escenario `NOT_IDENTIFIED`. La configuración de escenario declara fallo de positividad/soporte; por tanto, la segunda expectativa es la coherente con el contrato y la primera es una expectativa obsoleta contradictoria.

El test añadido de independencia respecto a la aleatorización Z pasó en ese run, así como los tests de separación de verdades, hash/seal, y los tests del harness P178 histórico. No se ejecutó replay. El run automático no equivale a una ejecución confirmatoria ni al benchmark científico C10-S; sí es una ejecución técnica real de la suite y queda registrada como no prevista. No se debe describir Gate 88 como “tests no ejecutados”.

No se ha solicitado ni iniciado un rerun. La ejecución primaria automática no estaba expresamente autorizada; queda registrada como desviación operativa, sin ocultarla ni atribuirle autorización retroactiva.

### 16.238.5. Estado de los artefactos y dictamen

Blobs recuperados en la rama `research/c10-s-consolidation-draft`:
| Artefacto | Blob |
|---|---|
| `vcont_integrated_harness.py` | `ba0b588051cad1b7f5cf91af19200fdfaaa77f20` |
| `test_vcont_integrated_harness.py` | `e48009753df7fe498213564bb9cf1e701e22a8fb` |
| `README.md` del harness | `aa4480e4133aec46c9bf725f7d285485699e6979` |

Comprobaciones estáticas recuperadas después de los cambios:
- ausencia de alias focal obsoleto dentro del harness integrado;
- nombres de salida y payload de hash alineados;
- ITT-Z, ITT-G y θ_A no materializado permanecen separados;
- condiciones de aleatorización Z/G separadas;
- 16 tests declarados, incluido el nuevo test de independencia;
- README distingue el harness integrado del P178 histórico.

**Dictamen:** GATE_88_STATIC_MIGRATION_AUDIT_PASS / G_ASSIGNMENT_NO_LONGER_DEPENDS_ON_Z_RANDOMIZATION / ANALYZER_RESULT_SEAL_FIELDS_ALIGNED / LEGACY_P178_SCOPE_PRESERVED / AUTO_CI_UNAUTHORIZED_RUN_RECORDED / CI_PRIMARY_FAIL_32_OF_33 / REPLAY_SKIPPED / SOFTWARE_ACCEPTANCE_BLOCKED / NO_SCIENTIFIC_BENCHMARK / NO_DESIGN_FREEZE.

El gate queda cerrado como auditoría y corrección estática, pero la aceptación técnica de la migración permanece bloqueada por el test contradictorio y el run CI fallido.

### 16.238.6. Siguiente gate — 89

**Gate 89 — reconciliar el contrato de positividad de R0_SUPPORT_FAILURE y corregir la expectativa obsoleta sin cambiar el DGP.** No ampliar el universo de escenarios ni relajar el criterio de soporte. La corrección esperada es alinear el test `test_structural_support_failure_removes_high_stratum_g1` con el dictamen `NOT_IDENTIFIED`, y verificar que no haya otro test que contradiga el mismo contrato.

La actualización de código/tests volvería a activar el workflow por su filtro de paths. Por tanto, antes de cualquier nuevo push que pueda disparar CI, se requiere autorización explícita del usuario para ejecutar la suite técnica. No se debe lanzar benchmark P178 ni experimento científico. `scientific_execution=false`; la suite técnica requiere autorización expresa.


---

## 16.239. Gate 89 — reconciliación de positividad y suite técnica primaria + replay PASS (2026-11-13)

**Precedencia:** §§16.237–16.238 y Technical Execution Workflow v0.1. Alcance: corregir la expectativa obsoleta del escenario sintético `R0_SUPPORT_FAILURE` y ejecutar la suite técnica automatizada autorizada por el usuario. No modificar el DGP, roster, políticas, estimandos, Generator, Analyzer, Evaluator, harness P178 ni criterios de soporte. No ejecutar benchmark Monte Carlo ni experimento científico confirmatorio.

### 16.239.1. Corrección mínima del contrato de test

En `03_EXPERIMENTS/C10-S/harness/test_vcont_integrated_harness.py`, el test `test_structural_support_failure_removes_high_stratum_g1` verificaba correctamente que no existía asignación G=1 en el estrato HIGH, pero esperaba erróneamente `g_assignment_status == IDENTIFIED`.

Se cambia únicamente esa expectativa a `NOT_IDENTIFIED`, alineándola con:
- el contrato de positividad/soporte común;
- la abstención del Analyzer cuando `contract.positivity == False`;
- el test complementario `test_support_failure_blocks_g_assignment_but_not_package`, que conserva ITT-Z identificado y bloquea ITT-G.

No se altera el escenario ni se elimina ninguna observación para hacer pasar la suite. El cambio es una reconciliación de una expectativa contradictoria, no un ajuste del mecanismo generador.

### 16.239.2. Autorización y ejecución técnica

El usuario autorizó explícitamente la corrección y la ejecución automática de la suite técnica. El push en la rama de investigación activó el workflow existente `.github/workflows/c10-s-focal-harness-tests.yml`.

Registro:
- Workflow: `c10-s-focal-harness-tests`.
- Run ID: `43412059150`.
- Job ID: `131840643599`.
- Commit probado: `244896092e6414ccd92bd31a19776dcf71266c15`.
- Evento: `push`.
- Resultado del run: `SUCCESS`.

Secuencia observada:
1. Checkout del commit exacto: PASS.
2. Python 3.12 setup: PASS.
3. Instalación de dependencias fijadas `numpy==2.3.5`, `scipy==1.17.0`: PASS.
4. Compilación de harness y tests: PASS.
5. Suite primaria: PASS, 33 tests en 0.630 s.
6. Replay desde clean source archive, después del PASS primario: PASS, 33 tests en 0.637 s.
7. Manifiesto de ejecución y subida de capturas: PASS.

No se registraron fallos de tests en la ejecución primaria ni en el replay. Los tests integrados relevantes pasaron, incluidos:
- `test_structural_support_failure_removes_high_stratum_g1`;
- `test_support_failure_blocks_g_assignment_but_not_package`;
- `test_g_assignment_does_not_require_z_randomization`;
- `test_direct_g_path_does_not_contaminate_g_assignment_truth`;
- `test_truth_bundle_separates_g_assignment_from_unmaterialized_theta_a`.

La suite completa incluye también los contratos del harness focal histórico P178. Su PASS acredita los tests técnicos cubiertos por esta suite, no una migración semántica del harness P178 ni validación de θ_A integrado.

### 16.239.3. Artefacto y procedencia

- Artefacto CI: `c10s-focal-harness-244896092e6414ccd92bd31a19776dcf71266c15-43412059150-1`.
- Artifact ID: `14029179772`.
- SHA-256 del ZIP de artefactos: `1ab1879cc39787bb43f252b83fc3482a8c352052c86e6cc95a494a6053685fd3`.
- URL: `https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43412059150/artifacts/14029179772`.
- Run: `https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/43412059150`.

El artefacto contiene capturas stdout/stderr de ejecución primaria y replay, y manifiesto con commit, run, intento, evento y ref. Retención declarada por workflow: 30 días.

Blob final del test corregido:
`b4fd8ea192ab145d990bee3e1087ebc12b665502`.

### 16.239.4. Dictamen y límites

**Gate 89 cerrado.** La contradicción de positividad está resuelta mediante una modificación mínima; compilación, suite primaria y replay han pasado en el commit exacto.

Dictamen:
`GATE_89_SUPPORT_CONTRACT_RECONCILED / STRUCTURAL_POSITIVITY_FAILURE_ABSTENTION_CORRECT / PACKAGE_ITT_REMAINS_IDENTIFIED / G_ASSIGNMENT_NOT_IDENTIFIED_WITHOUT_COMMON_SUPPORT / COMPILE_PASS / PRIMARY_33_OF_33_PASS / REPLAY_33_OF_33_PASS / CI_SUCCESS / EXECUTION_ARTIFACT_PRESERVED / TECHNICAL_SUITE_AUTHORIZED_AND_COMPLETED / NO_MONTE_CARLO_BENCHMARK / NO_SCIENTIFIC_CONFIRMATORY_EXECUTION / NO_THETA_A_VALIDATION / NO_DESIGN_FREEZE`.

La suite técnica no demuestra recuperación causal de θ_A ni atribución del efecto de ΔT_acc*. θ_A sigue sin materializarse. El PASS no convierte ITT-G en efecto focal, no resuelve identificación parcial/bounds, no acredita todas las celdas C1/C3 del Gate 71 y no cierra C10-S globalmente.

### 16.239.5. Siguiente gate — 90

**Gate 90 — cerrar el inventario de cobertura científica C1/C3 contra el roster finito existente, sin crear mundos nuevos.** Cruzar las clases y configuraciones ya presentes con los seis roles de C1 y los seis roles de C3 definidos en Gate 71; distinguir cobertura implementada, cobertura ejecutada por tests, y cobertura todavía no representada. Para cada celda no cubierta, identificar si falta un escenario, una verdad de referencia, un estimador, una regla de abstención o un test. No inferir cobertura científica a partir del PASS de la suite de 33 tests. No ampliar el roster salvo que la auditoría demuestre una ausencia irreducible y se justifique antes como discrepancia científica. No ejecutar benchmark ni experimento confirmatorio sin autorización separada.
