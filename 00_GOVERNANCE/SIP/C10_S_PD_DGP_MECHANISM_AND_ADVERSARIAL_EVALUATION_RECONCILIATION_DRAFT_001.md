# C10-S — Reconciliación integrada PD: DGP, mecanismos C5 y evaluación adversarial

**ID:** C10-S-PD-RECON-001 · **Fecha:** 2026-11-11
**Estado:** RECONCILIADO DOCUMENTALMENTE CON BLOQUEOS / DRAFT / NO DESIGN-FROZEN / NO IMPLEMENTADO / NO EJECUTADO
**Ámbito:** PR #116 · research/c10-s-consolidation-draft

## 1. Dictamen

PD queda reconciliado documentalmente en arquitectura, mecanismos y cobertura de evaluación. No queda cerrado como DGP cuantitativo congelable ni como contrato ejecutable. Se reutilizan la matriz temporal de predicados, inventario finito de rutas/Reach, S4R-01…18, MEAS-01…14, MISS-01…15, POL-01…10, P177/P178/P179/P182/P183 y las decisiones B1 del 11-11 sobre enlace y adjudicación causal de petición–trayectoria. No se crean familias paralelas ni se duplican IDs.

Estado: PD_RECONCILED_DOCUMENTALLY / DGP_QUANTITATIVE_SPECIFICATION_OPEN / NOT_DESIGN_FROZEN.

## 2. DGP integrado y separación de planos

El DGP debe generar una historia temporal coherente por unidad y escenario, con identidad/versionado y snapshots exactos: (i) estado basal y elegibilidad pre-Z; (ii) asignación Z y política material B; (iii) programación, intento, recepción, instalación y verificación técnica; (iv) estado estructural postintervención; (v) rutas, Reach y trayectorias potenciales/realizadas; (vi) conocimiento, consideración, selección, inicio, ejecución, Outcome y Value; y (vii) proceso de observación, error, cobertura, missingness, censura y adjudicación.

Se mantienen T_acc*=(U*,R*,C*,X*), ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), A_f* como proyección focal, D_f* como apertura y E_T como plano epistémico separado. La cadena generativa no implica mediación exclusiva; las vías paralelas, directas y colaterales permanecen explícitas.

Se segregan tres planos:
- truth_dgp: estados estructurales, potenciales por régimen, parámetros, causas, interacciones, rutas, contribuciones y resultados potenciales.
- observed_evidence: registros que recibe el Analyzer, con fuentes, cobertura, error, timestamps, versiones y ausencias; nunca etiquetas causales ocultas ni potenciales.
- evaluation/adjudication: comparación posterior entre la salida sellada del Analyzer y truth_dgp, con errores, recuperación, calibración y abstención.

El Analyzer no recibe truth_dgp. El Evaluator accede a la verdad solo después de sellar la salida del Analyzer. Temporalidad, coincidencia de IDs, recepción, respuesta técnica o éxito de instalación no prueban por sí mismos contribución causal. La cobertura epistémica no cambia la verdad estructural.

## 3. Mecanismos C5 y contrafactuales por etapa

La adjudicación se refiere a una etapa concreta del ciclo de petición, sin colapsarlas: Request_opportunity, Request_attempt, Request_received, Request_admitted/rejected, Request_processing y Request_response. La oportunidad estandarizada del harness es un probe/asignación común; no se presume acción del servicio ni contribución causal. Si una etapa posterior no ocurre, el DGP registra el mecanismo de no transición y no imputa contribución de esa etapa.

Para cada etapa, el generador define el contraste contrafactual pertinente: trayectoria/proceso con la intervención o etapa frente al contrafactual correspondiente, haciendo explícitas historia previa, versiones, condiciones y demás causas relevantes. El objeto afectado debe ser una propiedad de trayectoria preespecificada (existencia, factibilidad, ruta, secuencia, duración, integridad u otra definida ex ante). No se adjudica relevancia retrospectivamente a cualquier diferencia.

Se reutilizan las clases aceptadas en DEC-C10S-B1-CAUSAL-ADJUDICATION-001:
- NECESSARY_CONTRIBUTION: sin la intervención/etapa considerada, la trayectoria objetivo no existiría bajo el contraste definido.
- ENABLING_CONTRIBUTION: hace factible la trayectoria o elimina una barrera relevante, sin implicar causa única o suficiente.
- MODIFYING_CONTRIBUTION: la trayectoria existiría, pero cambiaría una propiedad relevante bajo el contrafactual sin esa intervención.

Las clases pueden coexistir; las contribuciones pueden ser parciales, concurrentes o colaterales. No implican signo favorable de Outcome ni creación de Value. Deben representarse contribuciones redundantes, antagonistas, compensatorias e interactivas cuando el DGP las contenga.

Se respeta DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001: TEMPORAL_ASSOCIATION, TRACEABILITY_LINK y CAUSAL_CONTRIBUTION son tipos distintos. Se permiten petición sin trayectoria atribuible, trayectoria sin petición atribuible, una petición con varias trayectorias y múltiples peticiones contribuyendo a una trayectoria en escenarios secundarios. No se impone cardinalidad funcional 1:1 ni se usa información post-Z para redefinir elegibilidad.

## 4. Cobertura mínima de escenarios adversariales

| Familia | Verdad generada | Salida exigida al Analyzer |
|---|---|---|
| Aislado focal | D2 altera solo provisión focal; sin vías colaterales; mapping/soporte estipulados | ITT de política; atribución focal solo si se satisfacen mapping, medición, régimen y supuestos |
| Nulo | Sin cambio verdadero de A_f/ΔT_acc/O/V | No fabricar primera etapa ni efecto |
| Fallo parcial | Intento/recepción/instalación sin C_dep o apertura A_f | Mantener etapas separadas; ITT sigue por Z |
| Adverso | B deteriora dimensión estructural, ruta o consecuencia | Recuperar signo adverso; no imponer monotonicidad positiva |
| Vía directa | B afecta O/V sin pasar por ΔT_acc | Efecto de paquete; no atribución focal exclusiva |
| Colateral | B modifica alternativas, dependencias, recursos, coste, seguridad, calidad, latencia o información | Detectar paquete, atribución condicionada o no-identificación |
| Interacción | Efecto depende de accesibilidad, condiciones, alternativas o recursos | Recuperar interacción en escala preespecificada |
| Heterogeneidad | τ_i y composición de compliers varían por historia; D1/D2 distintos | No extrapolar LATE a ATE/ATT ni transportar entre D1/D2 |
| IV adversarial | Primera etapa nula/débil, defiers o exclusión violada | No Wald cuando no procede; weak-IV o no-identificación |
| Interferencia | Pools, colas, host o recursos compartidos producen exposición cruzada | Modelar unidad/exposición o abstenerse de SUTVA |
| Versionado/crossover | Asignada, recibida y aplicada difieren; mismo ΔT con coste/calidad distintos | Preservar versiones; no agrupar por ΔT solamente |
| Alternativas | Ruta basal substitutiva o modificada por B | Separar P*_τ2 y P*_F; exclusividad solo en universo cubierto |
| Observación diferencial | B cambia telemetría, cobertura, documentación o adjudicación | Separar cambio epistémico de cambio estructural |
| Petición múltiple | Contribuciones necesarias, habilitadoras, modificadoras, concurrentes y colaterales | Adjudicar por etapa y contrafactual; no por temporalidad |
| Soporte fallido | Política/historia imposible o sin positividad | Restringir objetivo ex ante o NO IDENTIFICADO |
| Datos incompletos | MCAR/MAR/MNAR, pérdida diferencial, censura y selección post-Z | Modelo defendible, sensibilidad/cotas o no-identificación |

No se exige factorial completo; la selección final debe justificar cobertura de cada contraste, interacción y falsador. D1 permanece secundario y no se mezcla con D2. No se reabren DEC-C10-066/067. s=.80 sigue como hipótesis no validada; intento, instalación, dependencia y accesibilidad final se generan por separado.

## 5. Contratos de evaluación: reutilización y estado

- P177-01…12: ITT-A/O/V, primeras etapas, Wald/LATE, weak-IV, separación O/V, ajuste basal, heterogeneidad, multiplicidad, recuperación, equivalencia y dictamen causal. Cobertura documental existente; cuantificación, tolerancias y fixtures pendientes.
- P178-SIM-01…10: potencia, búsqueda de N, clústeres, réplicas, error Monte Carlo, semillas, reproducibilidad, pérdidas y métricas. Son IDs organizativos derivados, no IDs originales.
- P179-01…08: Value contextual, vector, separación A/O/V, dimensiones, trade-offs, estimación y agregación. Bloqueado para cierre sustantivo hasta que PA instancie Value.
- P182-01…12: validez, circularidad, especificación O/V, reproducibilidad, acuerdo, error, invariancia, sensibilidad, separación de roles y trazabilidad.
- P183-01…13: taxonomía/mecanismo de ausencia, separación A/O/V, ITT, selección, mediación, censura, sensibilidad, cotas y dictamen por estimando.
- S4R, MEAS, MISS, POL, VER, TRJ, INT, GEN, PM, SNAP, REACH, PROV, GC y U_G se conservan según aplicabilidad.

El registro de un contrato no implica implementación, cobertura completa ni PASS. P177–P183 se evalúan por estimando y dimensión; no se emite un dictamen global que oculte que ITT-O puede ser evaluable mientras ITT-V, mediación o una dimensión no lo son.

## 6. Medición, missingness y censura

A, O y V requieren definiciones y procesos de medición independientes. Para cada variable/tiempo se distinguen truth, observado, validez, cobertura, fiabilidad y adjudicación. Error diferencial por brazo/versión, cambio de criterio, falta de invariancia y validación no aleatoria son escenarios adversariales.

La taxonomía distingue no registrado, fuente inaccesible, fallo técnico, abandono, censura administrativa, censura informativa, indefinición estructural, medición inválida y Value no instanciado. Ninguna ausencia se recodifica automáticamente como cero, inaccesibilidad, no ejecución o Value nulo.

MCAR/MAR solo permiten recuperación puntual bajo sus supuestos/modelos y positividad. MNAR, selección por variables no observadas y censura informativa requieren sensibilidad, tipping points o cotas defendibles; de lo contrario, no-identificación. ITT conserva la población aleatorizada y no se condiciona en cumplimiento, A postratamiento, selección, ejecución o disponibilidad de Value. Value no definido es distinto de Value definido pero no observado.

## 7. Potencia, precisión y error Monte Carlo

El diseño cuantitativo está documentado, pero no hay parámetros confirmatorios aprobados. El cierre posterior deberá fijar estimandos prioritarios, escala, efecto mínimo relevante, MDE y márgenes de equivalencia; buscar N en cuadrícula y elegir el menor que satisfaga potencia y precisión por estimando; calcular potencia separada para ITT-O, primeras etapas, LATE cuando sea válido y clasificación adversarial; incorporar ICC/efecto de diseño/número efectivo de clústeres si corresponde; elegir R según SE_MC tolerable para sesgo, RMSE, cobertura y clasificación; y fijar semillas jerárquicas y hashes reproducibles.

Reportar sesgo, RMSE, cobertura, error tipo I, potencia, calibración, convergencia, réplicas inválidas y clasificación correcta de identificación/no-identificación. N=2.000, asignación 1:1 y R=1.000 son ilustraciones históricas, no parámetros aprobados. Más N/R no repara violaciones de identificación ni invalidez de constructo. No significación no demuestra equivalencia; baja precisión no refuta.

## 8. Bloqueos materiales y límites heredados

1. Value no está instanciado por PA: no inventar beneficiario, dimensiones finales, escalas, pesos, agregación, perspectiva ni horizonte. P179 e ITT-V/mediación sobre Value siguen bloqueados.
2. Outcome técnico sigue candidato, no operacionalización completa; no inventar indicadores ni ventanas.
3. Faltan IAM/snapshots/inventario material para demostrar ausencia basal de provisión, mapping B→g^Af, invariancia de dependencias, soporte y colaterales reales.
4. PC ya dictaminó θ_A(q), θ_Af(q_X*) y mediación interventional no identificados en el D2 material actual. PD solo construye escenarios donde el Analyzer deba recuperar identificación conocida o abstenerse; no convierte el D2 actual en identificado.
5. Distribuciones conjuntas, parámetros, dependencia, interacción, heterogeneidad y mecanismos de transición del DGP no están cerrados.
6. F*, G, H y ventanas conservan estados abiertos; no convertir topología candidata en parámetro confirmatorio.
7. Clases de contribución aceptadas conceptualmente; contrastes D2 concretos, propiedades relevantes, soporte, causas concurrentes y reglas de adjudicación siguen abiertos.
8. UE/UA, clústeres y exposición deben ser coherentes con PA/PB; no asumir independencia.
9. La lectura de C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md en esta rama devolvió contenido vacío con SHA e791578396a9527cb3b72b1b7c2d7ff1bbe0c100. No se sobrescribe un maestro cuyo contenido íntegro no pudo recuperarse. Se requiere recuperar/verificar el blob correcto antes de propagar PD al maestro.

## 9. Criterios de aceptación y siguiente paquete

PD solo podrá pasar a PE cuando truth/potenciales y reglas generativas estén versionados; las contribuciones tengan contrastes contrafactuales por etapa; truth/observed/evaluation estén segregados; escenarios adversariales tengan contrastes y falsadores; P177/P178/P179/P182/P183 estén cruzados a estimandos, escenarios, entradas, salidas y tolerancias; A/O/V, missingness, censura, soporte, interferencia y versiones estén cubiertos; y parámetros/N/R/potencia/precisión/SE_MC estén justificados ex ante. Los bloqueos de Value/Outcome y material D2 deberán resolverse o limitar expresamente el alcance de PE.

**Dictamen:** PD_RECONCILED_DOCUMENTALLY / DGP_QUANTITATIVE_SPECIFICATION_OPEN / NOT_DESIGN_FROZEN. No autorizado código, fixtures confirmatorios, generación de datos, simulación, estimación ni ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false.

**Siguiente:** PE — especificación técnica integrada y contrato de implementación, condicionado a cierres científicos y materiales. Se pueden preparar interfaces conceptuales; no código ejecutable ni fixtures confirmatorios sin gates y autorización expresa.


## 10. Crosswalk C+D integrado — referencia rectora (2026-11-12)

La integración posterior del plan §16.185 es la referencia rectora para relacionar DGP, potenciales, estimandos, población, observación y evaluación. Este addendum no sustituye PD §§1–9 ni convierte el DGP en cuantitativo/frozen.

- Se mantiene la separación truth_dgp / observed_evidence / evaluation-adjudication. O-CONF truth se indexa por instancia×ruta y deriva de F* en el estado terminal aplicado; V_cont truth es temporal por UE/ventana. Son constructos/Outcomes separados, con observación y evaluación independientes.
- D2/Z_B genera la historia potencial de programación, intento, recepción, instalación, C_dep*, T_acc*, A_f*, D_f*, ΔT_acc*, Reach/Π y etapas downstream. ITT_Z^D2 es efecto total de asignación al paquete por resultado; O-CONF_r y V_cont no transfieren identificación entre sí.
- g_A1/g_A0 es una intervención estocástica distinta sobre la distribución conjunta factible del ΔT_acc* completo bajo q común y régimen común de vías no focales. El mapping B_D2→g_Af, q_X*, soporte y régimen común siguen sin demostrar. C4 conserva ΔT_acc* como objeto mediador; no se obtiene por resta del ITT ni por ajuste convencional de confusores post-Z.
- D_i(z) conserva rutas directas/colaterales e interacciones. Si no se separan, ITT se interpreta como efecto de paquete; si falta soporte/identificación, Analyzer informa bounds o abstención.
- P*τ2 primaria candidata, P*_F secundaria; E_i/App, q_X*, asignación π_h, estratos, N, UA, aislamiento y mapa de exposición permanecen abiertos según el contrato D2. Need_preZ no es elegibilidad.
- La tabla de escenarios y crosswalk P177/P178/P179/P182/P183 se especifica en plan §16.185. Se reutilizan los IDs existentes; no se crean pruebas ni parámetros.

**Estado:** PD_CAUSAL_CROSSWALK_INTEGRATED / DGP_QUANTITATIVE_SPECIFICATION_OPEN / SUPPORT_AND_POPULATION_NOT_MATERIALIZED / NOT_DESIGN_FROZEN / NO_EXECUTION_AUTHORIZED.
