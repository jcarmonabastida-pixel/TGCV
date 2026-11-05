> **HISTÓRICO / SUPERSEDIDO COMO GUÍA OPERATIVA (2026-11-05).** Draft 003 omitía desarrollos vigentes de §§59–81 y parte de la arquitectura estadística 165–183. La guía operativa vigente es C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md. Se conserva este archivo para trazabilidad; no dirigir nuevas operaciones desde él.

---

# C10-S — Plan integrado de cierre científico y operacionalización
**ID:** C10-S-PLAN-001 · **Versión:** Draft 003 · **Fecha:** 2026-11-05  
**Estado:** DRAFT / NO APROBADO / NO CONGELADO / NO IMPLEMENTADO / NO EJECUTADO  
**Sustituye como guía operativa:** Draft 001 y Draft 002 (se conservan como históricos).  
**Maestro:** `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md` (secciones 1–130).  
**Auditoría de consistencia de referencia:** `C10_S_MASTER_RECONCILIATION_AUDIT_DRAFT_002.md`.

---

## 1. Propósito, alcance y límites

C10-S es el experimento sintético para comprobar si el diseño causal-transformacional puede reconstruir constructos, identificar los estimandos que el diseño permite identificar, recuperar efectos conocidos y reconocer efectos de paquete, vías alternativas, heterogeneidad, ausencia de efecto, efectos adversos y no-identificación bajo DGP con verdad conocida.

C10-S evalúa la capacidad metodológica del procedimiento dentro de los DGP, poblaciones, intervenciones, horizontes y reglas de Value que se especifiquen. No demuestra por sí solo causalidad empírica en sistemas reales ni confirma/refuta una regularidad general de TGCV.

Este plan se refiere exclusivamente a la línea científica C10-S. La web germen/playground, su arquitectura, publicación y evolución comunitaria son una línea separada, fuera del alcance y de los gates de C10-S.

La autoauditoría interna asistida permite continuar sin depender de revisores externos. Debe etiquetarse siempre `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`; no se presentará como revisión independiente.

## 2. Regla documental: cobertura histórica ya integrada

La revisión del maestro confirma que no existe la laguna histórica que se había diagnosticado erróneamente:

| Sección conversacional | Ubicación integrada en el maestro |
|---|---|
| 130 | §16 |
| 131–137 | §§17–24 |
| 138–163 | §§25–50 |
| 164 | §51 |
| 165–183 | Integración resumida en §52 |

El contenido de §§130–163 no debe recuperarse ni reconstruirse otra vez. El trabajo pendiente es asegurar que el plan y los contratos derivados reflejen las formulaciones vigentes y no reintroduzcan arquitecturas sustituidas.

La fuente `Notes_261104_163033.docx` corresponde al intervalo 165–183. Su contenido está sintetizado en §52 y desarrollado en los artefactos auxiliares de recuperación, especialmente `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`, `C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md` y los contratos DGP/estimación/pruebas. El registro de recuperación no es una transcripción literal íntegra del DOCX; no se necesita una nueva recuperación para dirigir el plan.

El texto XSYNC-138-01…10 está en el maestro §§25–28 y se traza en `C10_S_XSYNC_138_CLOSURE_TRACKER_DRAFT_001.md`. El tracker es auxiliar de cierre, no reemplaza el texto del maestro.

## 3. Precedencia y estados

1. `00_GOVERNANCE/README.md` en `main`, bootstrap y estado canónico gobiernan proceso, permisos y límites.
2. C10-D1 gobierna la pregunta causal general y sus requisitos; C10-S la operacionaliza en el microdominio sintético sin redefinirla.
3. El maestro C10-S es la integración normativa de diseño. Las decisiones aceptadas se leen con su DEC-C10 y alcance explícito.
4. Los contratos especializados, registros, matrices y auditorías complementan el maestro; si discrepan, se corrigen contra la formulación vigente del maestro y las decisiones aceptadas.
5. El plan es derivado: no crea decisiones ni puede prevalecer sobre el maestro.
6. Las propuestas históricas, recomendaciones, fórmulas ilustrativas y fixtures no son decisiones aceptadas por el hecho de aparecer en el maestro o en un artefacto auxiliar.
7. Toda decisión nueva debe actualizar en el mismo ciclo el maestro, Decision Log y los artefactos afectados; cada escritura se verifica mediante fetch/SHA.
8. No modificar `main`; mantener PR #116 Draft y su base actual salvo instrucción expresa.
9. `scientific_execution=false`; `execution_authorized=false` hasta autorización expresa y gates previos.

Estados que deben mantenerse separados: DEFINIDO, PROPUESTO, ABIERTO, ACEPTADO, IMPLEMENTADO, EJECUTADO, AUDITADO, NO IDENTIFICADO e INDETERMINADO. Definir una prueba no significa implementarla, ejecutarla ni superarla.

## 4. Arquitectura vigente del experimento

### 4.1 Microdominio, sistema y objeto

La línea de trabajo vigente es Opción A: migración de configuración entre entornos software. Se adopta como microdominio seleccionado por DEC-C10-051 y se concreta en los contratos posteriores:

- Objeto: configuración versionada de una instancia lógica de servicio (DEC-C10-052 y DEC-C10-058).
- DGP base finito, gramática, dominios, mapping fuente/destino, matrices SM/FP y cardinalidades: DEC-C10-053…056.
- Frontera P0/P1/P2: DEC-C10-057/058.
- F* es el criterio funcional de referencia y adjudicación de equivalencia/substituibilidad; no es Value ni prueba por sí mismo de identidad o equivalencia causal.
- Distinguir frontera del sistema, capacidades disponibles y transformaciones accesibles; recursos, dependencias y condiciones compartidas se modelan en el nivel causal que corresponda.

Las decisiones DEC-C10-051…065 se preservan dentro de su ámbito. Las DEC-C10-059…065 son decisiones/contratos del esquema de evidencia U_G; no resuelven estimandos, comparador, exclusión ni atribución causal.

### 4.2 Intervención material B: provisión, no ejecución de la transformación

La intervención actual se concreta en la provisión técnica del adaptador/dependencia focal. B puede provisionar, configurar, verificar e inventariar el adaptador y sus dependencias; no ejecuta las transformaciones funcionales F1/F2 ni las alternativas A1/A2.

En Opción A:
- B provisiona el adaptador.
- `C_dep*` representa el estado técnico verificado de la dependencia focal.
- F1 es la transformación funcional de conversión; F2 aplica/valida en destino.
- A1/A2 son rutas alternativas candidatas cuya independencia respecto de B debe demostrarse, no presumirse.
- Si B modifica una alternativa, permisos, recursos, seguridad, latencia, costes, información, configuración o dependencias compartidas con efecto en Outcome/Value, existe una vía colateral y el ITT se interpreta como efecto de paquete salvo identificación adicional.

El manifiesto B y el grafo de dependencias son contratos documentales. No hay inventario técnico real ni prueba de aislamiento: estados desconocidos se mantienen como `?`, no como ausencia.

### 4.3 Mecanismo y primera etapa: conservar cada estado

La cadena material de referencia es:

`Z → B asignada/ofrecida/recibida → W_attempt → S_install → (C_install, C_integrity, C_compat, C_oper) → C_dep* → A_f*(t) → D_f* → ΔT_acc* → Reach_H → Π_H → Known/Consider → Sel → Start → Exec → O → V`.

Es un orden generativo y temporal, no una afirmación de mediación exclusiva. Las vías alternativas B→O/V se mantienen explícitas.

- `Z`: asignación aleatoria a la política concreta.
- `B`: política/version material de provisión.
- `W_attempt`: intento efectivo; no equivale a instalación ni éxito.
- `S_install`: instalación completada.
- `C_dep*`: conjunción de instalación, integridad, compatibilidad y operatividad verificadas.
- `A_f*(t)`: accesibilidad estructural verdadera de τ2, derivada de todos los predicados constitutivos del contrato; no se asigna directamente desde Z, B, W o C_dep.
- `D_f*`: apertura focal basal→post, `I(A_f,base*=0 ∧ A_f,post*=1)`; no equivale al estado post ni a la accesibilidad completa.
- `ΔT_acc*`: cambio estructurado completo del espacio transformacional; A_f es una proyección focal, nunca sustituto del constructo completo.
- `App_f`, Reach, conocimiento/consideración, selección, inicio, ejecución parcial/completa/interrumpida, Outcome y Value son estados/constructos distintos.

La primera etapa debe calcularse por separado para W, éxito técnico, C_dep, A_f, D_f y ΔT_acc. Una primera etapa sobre C_dep no demuestra una primera etapa sobre accesibilidad.

### 4.4 Componentes técnicos y distribución conjunta

`C_dep*=C_install* ∧ C_integrity* ∧ C_compat* ∧ C_oper*`.

El parámetro candidato `s=P(C_dep*=1 | W_attempt=1, E=1, D, H)` es una probabilidad conjunta de éxito técnico tras intento, no cuatro probabilidades marginales de 0,80. Una especificación suficiente debe definir la distribución de los 16 patrones conjuntos o un generador equivalente. No asumir independencia. Los fixtures y cuadrículas de sensibilidad de §§68–69 son propuestas ilustrativas, no distribución confirmatoria ni calibración empírica.

### 4.5 D1/D2: comparación y estado

- **D1:** provisión ordinaria de control con `P(W_attempt=1|Z=0)=.25`, tratamiento con intento programado 1; éxito conjunto condicional candidato .80; `P(C_dep,post=1|Z=0)=.20`, `P(C_dep,post=1|Z=1)=.80`; primera etapa técnica objetivo .60.
- **D2:** sin intento/provisión focal en control (0), intento programado 1 en tratamiento; éxito conjunto condicional candidato .80; estados técnicos finales 0/.80; primera etapa técnica objetivo .80.

D1 es un contraste incremental frente a provisión ordinaria y solo puede ser primario si se justifica ex ante que ese régimen es el comparador científicamente pertinente. D2 es el candidato preferente recomendado en §66 para el contraste mecanístico provisión focal frente a ausencia de intento. **La selección del escenario primario sigue ABIERTA**: D2 no está aprobado y D1 no queda descartado. Los ITT, primeras etapas y poblaciones de compliers de D1 y D2 no se agrupan ni se transportan automáticamente.

Los valores .25, .80, .20, .60 y .80 son parámetros candidatos del DGP, no tasas empíricas ni hechos técnicos observados. La igualdad de C_dep y A_f solo se daría si todos los predicados estructurales restantes están satisfechos; no se presume.

### 4.6 Población, q*, condiciones y factibilidad

- `P*_{τ2}`: población de apertura focal elegible, definida antes de Z; para apertura basal→post requiere `A_f,base*=0` respaldada.
- `P*_F`: subpoblación sin alternativa funcional substituible basal bajo F*; no es filtro automático de P*_{τ2}.
- `q_X*`: distribución común candidata de condiciones/historias basales y constitutivas elegibles. No incorpora la regla de Value ni variables postratamiento.
- `C_c`: condiciones constitutivas que deben permanecer compatibles para que las políticas sean factibles.
- `L_m`: condiciones temporales según su función causal; no ajustar mecánicamente por confusores/mediadores postratamiento.
- `q_L*`: alternativa secuencial solo si el diseño requiere intervenir/estandarizar historia postasignación con reglas, tiempos y soporte identificables.
- Ambas políticas deben ser factibles en cada historia con masa positiva del régimen común; si falla positividad, restringir población ex ante con nuevo estimando o declarar no-identificación.
- Unidad experimental (UE), unidad de asignación (UA), unidad de observación (UO), clúster y mapa de interferencia deben quedar explícitos. UE=UA individual es solo candidato cuando no hay recursos, agentes, estado o canales compartidos. Si hay spillovers, definir exposición y estimando a nivel de clúster/exposición.

### 4.7 F*, alternativas y cobertura

F* define objetivo funcional observable, entrada/salida, restricciones, granularidad, contexto, horizonte, tolerancias y adjudicación. Por cada ruta se evalúan separadamente accesibilidad, aplicabilidad, substituibilidad funcional, identidad/versión, coste, latencia, calidad, seguridad y fiabilidad.

La existencia de alternativa basal no elimina por sí sola elegibilidad en P*_{τ2} ni viola exclusión. Si B modifica la alternativa o una dependencia compartida que la afecta, aparece una vía colateral. La ausencia de alternativa solo puede afirmarse dentro del universo operativo delimitado y con cobertura suficiente; falta de inventario, opacidad o ruta desconocida mantienen estado indeterminado.

### 4.8 Snapshots, evidencia y U_G

Los snapshots pre/post/rollback, identidad, versionado, matching y eventos diff sustentan la reconstrucción de `ΔT_acc*`; `ΔE_T` (cambio de evidencia/captura) no se confunde con cambio estructural. Reach y `Π_H` se derivan de predicados temporales y rutas válidas; la propagación de estados 1/0/? debe preservar la indeterminación.

U_G registra observaciones, procedencia, cobertura, evaluación y adjudicación; no es generador de truth. La arquitectura Opción A, versionado y pinning exacto (DEC-C10-064/065) están especificados documentalmente, pero U_G no está técnicamente validado ni congelado. Las verificaciones de tablas Markdown son solo formato, no validez de esquema/FK/motor.

## 5. Arquitectura causal y jerarquía de estimandos

Los siguientes objetos se mantienen separados:

1. `ITT_Z`: efecto total de asignación a la política concreta, sobre Outcomes y cada dimensión de Value, en la población/horizonte predefinidos.
2. `ψ_policy`: efecto de la política/paquete cuando B activa vías adicionales además de accesibilidad.
3. Primera etapa sobre `C_dep`, `A_f,post*`, `D_f*` y `ΔT_acc*`: objetos diferentes.
4. `LATE_f/Wald`: efecto local entre compliers inducidos por el instrumento/política, solo bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición válida; inferencia robusta a instrumento débil.
5. `θ_{Af}(q*)`: contraste focal poblacional bajo régimen común y políticas factibles, solo si el contraste varía accesibilidad focal y no deja vías colaterales sin separar.
6. `θ_A(q)`: pregunta causal general C10-D1 sobre políticas que modifican accesibilidad transformacional; S4-R focalizado en τ2 no la sustituye.
7. `θ_{L,A}`/efecto conjunto: interpretación si condiciones y accesibilidad no pueden separarse.

La aleatorización identifica el ITT de asignación bajo los supuestos de diseño, no demuestra exclusión ni mediación. Un instrumento fuerte no garantiza validez. No se extrapola LATE a ATE/ATT ni se equiparan los LATE de D1/D2. No se usa `TE−θ_A(q)` como efecto residual automático. Si hay vías colaterales, informar efecto de política/paquete y declarar qué atribución no queda identificada.

## 6. Verdad del DGP, medición y roles

El generador conserva truth de potenciales, estados estructurales, componentes técnicos, accesibilidad verdadera, apertura, rutas, alternativas y parámetros. El analizador recibe solo datos observables y evidencias permitidas. El evaluador compara con truth después de congelar la salida del analizador. No filtrar etiquetas de escenario, parámetros generadores, potenciales ni A_f*/D_f* verdaderos.

A, O y V se miden independientemente:
- A: predicados y evidencia estructural; no se define por ejecución.
- O: resultados operativos observables; no se define por valoración.
- V: valoración contextual por observador/beneficiario, criterio, regla, dimensiones y horizonte; no se deriva mecánicamente de A u O.
- El vector multidimensional de Value es recomendación provisional; dimensiones, escalas, pesos, compensación e índice agregado requieren aceptación explícita.
- F* es el criterio funcional; no debe incorporar Outcome/Value para clasificar alternativas.

Temporalidad T0–Tn, fuentes, instrumentos, cegamiento, error de clasificación/medición, fiabilidad, acuerdo, invariancia, sensibilidad y trazabilidad deben quedar definidos. P181/P182/P183 y sus contratos son propuestas, no pruebas ejecutadas.

Datos ausentes: distinguir ausencia de registro, fallo técnico, abandono, censura administrativa/informativa, indefinición estructural y medición inválida. No convertir desconocido en 0, inaccesible, no ejecución o Value nulo. Mantener población aleatorizada para ITT; auditar selección postasignación. Mediación por A puede dejar de identificarse aunque ITT siga identificado. Aplicar cotas/sensibilidad cuando sean defendibles; de lo contrario, no-identificación por estimando.

## 7. Identificación, falsación y escenarios adversariales

El DGP y el analizador deben discriminar al menos:
- efecto focal positivo, nulo y adverso;
- ausencia de primera etapa, primera etapa débil y fuerte;
- incumplimiento, intentos fallidos, fallos parciales y versiones;
- efectos directos B→O/V, interacción B×A y rutas alternativas modificadas;
- alternativas basales presentes/ausentes/indeterminadas;
- heterogeneidad por perfiles y composición distinta de compliers D1/D2;
- violaciones de exclusión, monotonicidad, consistencia y no interferencia;
- errores de medición diferenciales, missingness, censura y selección postasignación;
- soporte/positividad insuficiente, poblaciones parciales y no-identificación.

Los controles negativos y diagnósticos no demuestran por sí solos exclusión. El analizador debe poder clasificar el resultado como efecto de paquete, atribución condicionada, identificación parcial/insuficiente o indeterminado. La verdad del DGP no debe garantizar artificialmente una conclusión favorable a TGCV.

## 8. Diseño estadístico: parcialmente especificado, no cerrado

La arquitectura estadística ya está desarrollada en el maestro §§18–23 y en las secciones 39, 52, 66 y 68–69; por tanto, no debe describirse como inexistente. **Lo pendiente es su cierre cuantitativo y la justificación ex ante de parámetros y criterios.**

Debe cerrarse:
1. Jerarquía confirmatoria/secundaria y multiplicidad de estimandos.
2. Tamaño muestral y asignación a nivel de unidad realmente aleatorizada/clúster.
3. Potencia y precisión separadas para ITT, primera etapa, LATE/IV y objetivos de clasificación/no-identificación.
4. Inferencia robusta a instrumento débil; intervalos/conjuntos de confianza adecuados para cocientes IV.
5. Sesgo, RMSE, cobertura, error tipo I, potencia, calibración, convergencia y tasa de réplicas inválidas.
6. Número de réplicas Monte Carlo y error Monte Carlo de las métricas.
7. Heterogeneidad, estratificación, covariables basales, errores de medición, missingness, censura e interferencia.
8. Justificación de `δ` (efecto mínimo relevante), `ε` (equivalencia), tolerancias de sesgo/RMSE/cobertura y reglas de clasificación.
9. Reglas de inconclusión: no significación no demuestra equivalencia; precisión insuficiente no refuta hipótesis; sesgo/violación de identificación no se arregla aumentando N.

`N=2.000`, asignación 1:1 y `R=1.000` son candidatos históricos, no parámetros confirmatorios justificados. Los rangos ilustrativos de `δ`/`γ` de la sección 171 tampoco son rangos aprobados de sensibilidad. No fijar ni adaptar parámetros tras observar resultados.

## 9. U_G, contratos y estado técnico

U_G y la plantilla/contratos deben permanecer alineados con §§82–129 y DEC-C10-059…065. La secuencia documental de OAS se mantiene como especificación, no como validación física. Pendientes técnicos separados: selección de motor, DDL, constraints/FKs, parser, validadores, fixtures y pruebas negativas. Ninguna prueba técnica se declara superada por una comprobación de Markdown.

Los artefactos auxiliares principales a mantener sincronizados son: Decision Log; DGP temporal/roles; reconciliación C10-D1/S4-R; causal architecture reconciliation; Closure Control Matrix; Test Contract Register; XSYNC tracker; U_G crosswalk/plantilla/auditorías; registro de recuperación 165–183. Ninguno sustituye al maestro.

## 10. Secuencia revisada de cierre

| Orden | Bloque | Resultado exigido | Estado |
|---|---|---|---|
| 1 | Alinear plan con maestro vigente | Plan refleja §§16–130, §§51–52 y DEC-C10; no reintroduce formulaciones tempranas | ESTE PLAN |
| 2 | Crosswalk de consistencia documental | Maestro ↔ Decision Log ↔ DGP ↔ estimandos ↔ matriz de cierre ↔ Test Register ↔ auxiliares | PENDIENTE |
| 3 | Cerrar arquitectura causal y política | B, estados de provisión, D1/D2 primario/secundario, versiones, vías colaterales y estimandos | ABIERTO |
| 4 | Cerrar población/unidad/régimen | P*_{τ2}/P*_F, UE/UA/UO, q_X*/q_L*, C_c/L_m, soporte e interferencia | ABIERTO |
| 5 | Cerrar arquitectura transformacional | F*, alternativas, C_dep/A_f/D_f/ΔT_acc, snapshots, predicados, Reach/Π_H | PARCIAL |
| 6 | Cerrar DGP completo | Distribución conjunta técnica, potenciales, heterogeneidad, escenarios adversariales y truth oculta | PARCIAL |
| 7 | Cerrar medición y ausencia | A/O/V, instrumentos, validez, fiabilidad, error, invariancia, P181–183, missingness/censura | PARCIAL |
| 8 | Cerrar diseño estadístico | N, potencia, precisión, réplicas, MC error, weak-IV, δ/ε, multiplicidad y reglas de decisión | ABIERTO |
| 9 | Autoauditoría interna de no-regresión | Reconciliación completa y pruebas de consistencia documental; declarar alcance no independiente | PENDIENTE |
| 10 | Freeze/aprobación del diseño | Decisiones aceptadas, riesgos residuales, hashes y protocolo preespecificado | NO ALCANZADO |
| 11 | Implementación/validación técnica | DDL/parser/fixtures/validadores bajo autorización específica | NO AUTORIZADO |
| 12 | Simulación/experimento | Ejecución reproducible, análisis ciego, auditoría y replay bajo autorización expresa | NO AUTORIZADO |

## 11. Criterios de salida científica

C10-S debe poder distinguir, sin forzar resultados:
- atribución focal recuperada bajo supuestos satisfechos;
- ITT de política/paquete identificado pero atribución focal no identificada;
- contribución focal positiva, nula o adversa dentro del ámbito preespecificado;
- efecto heterogéneo/local sin extrapolación indebida;
- identificación parcial mediante cotas;
- no-identificación o indeterminación;
- recuperación estadística insuficiente de un estimando identificado.

La conclusión sintética se limita a la arquitectura y DGP efectivamente evaluados. No se transforma automáticamente en claim C10 empírico ni modifica Core/RMA/Matrix/STATUS.

## 12. Estado y siguiente operación

La documentación histórica 130–163 está integrada en el maestro §§16–50; 164 está en §51; 165–183 están resumidas en §52 y trazadas en los artefactos auxiliares. No procede abrir una recuperación histórica adicional.

La siguiente operación es ejecutar el crosswalk de no-regresión entre el plan y las formulaciones más recientes del maestro (§§53–69 y §§70–130), y después propagar las correcciones necesarias a Decision Log, DGP, matriz de cierre, Test Contract Register y descripción PR. La prioridad es cerrar el diseño causal y el DGP sin confundir provisión, dependencia técnica, accesibilidad, apertura focal, ΔT_acc, Outcome y Value.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`. No se ha implementado, simulado ni ejecutado el experimento.
