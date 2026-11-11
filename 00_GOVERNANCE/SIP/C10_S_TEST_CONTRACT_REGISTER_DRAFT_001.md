# C10-S — Registro normalizado de contratos de prueba
**Contratos de aceptación propuestos — borrador 001**

**Estado:** DRAFT / ESPECIFICACIÓN — NO IMPLEMENTADO / NO EJECUTADO  
**Fuente:** C10-S consolidated draft 004, §§27–28, 30–32, 38–41, 43 y 51.  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116.

---

## 1. Propósito

Este registro convierte los IDs de pruebas ya documentados en contratos verificables para el futuro generador y analizador. No afirma que las pruebas estén implementadas ni ejecutadas. Tampoco fija todavía parámetros estadísticos, tamaño muestral, tolerancias, δ o ε cuando requieren justificación adicional.

El objetivo de aceptación no es que el analizador produzca siempre un efecto positivo. Debe recuperar la verdad oculta del DGP cuando el estimando esté identificado y emitir **NO IDENTIFICADO**, **INDETERMINATE** o **EFECTO DE PAQUETE** cuando las condiciones lo exijan.

## 2. Contrato común obligatorio

Cada prueba deberá tener una ficha con estos campos:

| Campo | Requisito |
|---|---|
| test_id / version | Identificador único, versión inmutable y relación con la familia |
| objective | Pregunta de discriminación que prueba |
| fixture_id / fixture_hash | Datos/escenario de entrada y hash reproducible |
| unit_id / assignment_unit | Unidad experimental y unidad de asignación, explícitas |
| initial_state | Estado basal, condiciones, T_acc y alternativas antes de Z |
| intervention | Z, B, versión, política, intensidad, tiempo y cumplimiento |
| inputs_by_role | Datos entregados a generador, analizador y evaluador independiente |
| hidden_truth | Potenciales, parámetros y verdad DGP, solo para generador/evaluador |
| expected_output | Estimando, estado, dictamen y campos que debe devolver el analizador |
| assertions | Invariantes positivas y negativas que deben cumplirse |
| tolerance | Tolerancia fijada antes de ejecución y justificada por precisión/error Monte Carlo |
| failure_codes | Códigos de fallo tipados y no ambiguos |
| evidence_artifacts | Logs, snapshots, reporte, hashes y trazas |
| reproducibility | Semilla, versiones, configuración y hash del entorno |

**Separación de roles:** el analizador no recibe `A_f*`, `D_f` verdadero, estados potenciales, parámetros generadores ni Value potencial. La verdad oculta solo se utiliza para evaluar después el resultado del analizador. La medición de referencia se entrega únicamente conforme al diseño de validación preespecificado.

Estados de salida por prueba: **PASS**, **FAIL** o **INDETERMINATE**. No usar PASS si el escenario no discrimina la hipótesis, si faltan entradas esenciales o si el resultado esperado depende de una tolerancia no fijada.

## 3. Precondiciones globales del DGP S4-R

1. `P*_τ2` se define antes de Z; para un contraste de apertura basal→post, `A_f,base*=0` debe verificarse antes de asignación.
2. `P*_F` es subpoblación basal sin alternativa funcional substituible; no es filtro automático de `P*_τ2`.
3. `B_g0` y `B_g1` son políticas de provisión. En el DGP aislado principal, `p0=.20` y `p1=.80` son probabilidades finales post-asignación objetivo, no probabilidades basales.
4. El generador separa `W_attempt`, `S_install`, `C_dep,post`, `A_f,base*` y `A_f,post*`.
5. Si .20/.80 son probabilidades de intento y hay fallos posteriores, la verdad analítica debe calcularse a partir de la probabilidad final verificada; no asumir que se conservan .20/.80.
6. `A_f*` es focal; `ΔT_acc=(ΔU,ΔR,ΔC,...)` conserva el cambio transformacional completo.
7. Accesibilidad, aplicabilidad, conocimiento/consideración, selección, inicio, ejecución parcial/completa, interrupción y finalización son estados separados y fechados.
8. El Value y su regla evaluativa se fijan independientemente de q y se mantienen constantes entre brazos, salvo que el cambio de regla sea objeto explícito del escenario.
9. El DGP aislado estipula ausencia de vías directas diferenciales B→Value; los escenarios adversariales introducen deliberadamente dichas vías.
10. No se condiciona el ITT a cumplimiento, accesibilidad postratamiento, selección, ejecución o disponibilidad de Value.

## 4. Contratos S4R-01…18

| ID | Fixture / perturbación | Truth oculta / oráculo | Salida y aserciones exigidas | Fallo si… |
|---|---|---|---|---|
| S4R-01 | Sin alternativa basal; apertura focal τ2 bajo universo sintético cerrado | F_alt,0=0; A_f,base*=0; apertura post según B_g | Detecta P*_F y P*_τ2; declara exclusividad solo dentro del universo/horizonte declarado | Generaliza exclusividad fuera del catálogo o usa Value para clasificar |
| S4R-02 | Alternativa funcional basal estable entre brazos | F_alt,0=1; B no cambia sus propiedades funcionales | Mantiene unidad en P*_τ2, la excluye de P*_F; alternativa no se marca como violación de exclusión por mera existencia | Excluye unidad del ITT por alternativa o declara violación IV sin vía directa |
| S4R-03 | Alternativa substituye F* pero conserva identidad distinta de τ2 | Identidad de alternativa ≠ τ2; satisface F* bajo criterio fijado | Distingue equivalencia funcional de identidad transformacional | Fusiona identidades o concluye que τ2 era basalmente accesible |
| S4R-04 | Heterogeneidad por alternativa basal sin cambiar la alternativa | Efecto puede variar por F_alt,0; ninguna vía B→alternativa | Informa heterogeneidad preespecificada; mantiene elegibilidad y exclusión | Trata heterogeneidad como prueba automática de violación de exclusión |
| S4R-05 | B modifica una alternativa funcional | Vía B→F_alt→O/V en truth | Conserva ITT_Z del paquete; rechaza LATE focal bajo exclusión violada | Presenta Wald como efecto puro de A_f* |
| S4R-06 | Dependencia compartida cambia una alternativa sin cambiar su identidad nominal | Estado funcional/coste/latencia cambia por dependencia compartida | Detecta vía alternativa aunque el ID del catálogo permanezca igual | Considera invariante la alternativa por conservar su nombre |
| S4R-07 | Intento asignado, instalación fallida | W_attempt=1; S_install=0; C_dep,post=0; A_f,post*=0 | ITT por Z conserva asignación; primera etapa usa estado final verificado | Usa intento como acceso o recodifica fallo como acceso |
| S4R-08 | Primera etapa focal nula | P(A_f,post*=1|Z=1)=P(A_f,post*=1|Z=0) | ITT_D=0; no calcula ni interpreta Wald/LATE | Divide por cero o presenta estimación IV |
| S4R-09 | Primera etapa débil | ITT_D pequeño, no nulo; verdad LATE conocida | Activa inferencia robusta a instrumentos débiles; devuelve INDETERMINATE si precisión insuficiente | Usa Wald/SE convencionales como prueba concluyente |
| S4R-10 | τ2 accesible pero no aplicable desde estado inicial | Acc_f=1; App_f=0 por precondición de estado | Mantiene Acc_f y App_f separados; no hay ejecución válida | Declara inaccesible por no ser aplicable |
| S4R-11 | τ2 accesible y aplicable, pero no seleccionada | Acc_f=1; App_f=1; Sel=0 | Conserva posibilidad y no selección como estados distintos | Infiera ausencia de accesibilidad a partir de no ejecución |
| S4R-12 | Alternativa seleccionada/ejecutada en lugar de τ2 | F_alt ejecutada; τ2 permanece accesible si corresponde | Registra ruta alternativa y ejecución sin borrar τ2 del espacio accesible | Reconstruye T_acc desde la trayectoria ejecutada |
| S4R-13 | B altera coste, calidad o seguridad de alternativa | Vía directa/colateral conocida en truth | Dictamen efecto de paquete o no identificación focal; ITT_Z sigue reportable | Interpreta todo ITT como LATE focal |
| S4R-14 | Evaluador usa Outcome/Value para clasificar F_alt | F_alt_obs depende de O/V aunque truth no | Marca fuga/circularidad y falla la evaluación de exclusividad | Acepta la clasificación como basal independiente |
| S4R-15 | Clasificación de alternativa basal usa datos posteriores a Z | Registro basal adulterado con información postasignación | Detecta violación temporal; no permite inclusión confirmatoria | Acepta selección de población postratamiento |
| S4R-16 | p0/p1 incompatibles con mecanismo final verificado | Intento, éxito y C_dep,post generan probabilidades distintas de las declaradas | Falla contrato de calibración o recalcula truth; no conserva 3.6 por estipulación | Usa p_attempt como P(A_f,post*) |
| S4R-17 | Analizador reduce ΔT_acc a A_f* | Truth incluye otros ΔU/ΔR/ΔC o cambios no focales | Detecta pérdida de dimensión; A_f*=h_f(ΔT_acc) solo como proyección | Informa A_f* como cambio completo del espacio |
| S4R-18 | Wald etiquetado como ATE | Heterogeneidad y compliers definidos | Corrige etiqueta a LATE_f local y reporta población de compliers/supuestos | Informa ATE o efecto universal |

## 5. Contratos de medición MEAS-01…14

| ID | Alteración / fixture | Resultado esperado |
|---|---|---|
| MEAS-01 | Se=Sp=1 | Primera etapa observada coincide con la verdadera |
| MEAS-02 | Error no diferencial moderado | Primera etapa observada atenuada; Wald ingenuo distorsionado |
| MEAS-03 | Se+Sp=1 | Medición no discriminante; primera etapa observada nula |
| MEAS-04 | Se/Sp diferentes por brazo | Detecta posible primera etapa espuria/invertida; no aplica corrección simple |
| MEAS-05 | Error dependiente de versión técnica | Reporta error heterogéneo; no agrupa sin modelo |
| MEAS-06 | Evaluador conoce Outcome/ejecución | Falla independencia/cegamiento; invalida medición para atribución |
| MEAS-07 | Submuestra aleatoria de validación con referencia | Recupera Se/Sp con incertidumbre y diseño de muestreo |
| MEAS-08 | Validación no aleatoria sin probabilidades conocidas | Declara sesgo/no identificación de corrección |
| MEAS-09 | Referencia de validación también imperfecta | No la denomina gold standard; propaga incertidumbre/sensibilidad |
| MEAS-10 | Error en R/C, no en τ2 focal | Separa medición focal de validez de ΔT_acc completo |
| MEAS-11 | Indeterminado recodificado como 0 | Detecta clasificación forzada; falla |
| MEAS-12 | Snapshot posterior a ejecución | Detecta contaminación temporal; no usa para medir estado preejecución |
| MEAS-13 | Pérdida diferencial en submuestra de validación | Modela selección/pondera si identificable; sensibilidad si no |
| MEAS-14 | Medición binaria focal correcta pero catálogo incompleto | Permite IV focal si demás supuestos; prohíbe inferencia general sobre T_acc |

## 6. Contratos de datos faltantes MISS-01…15

| ID | Alteración / fixture | Resultado esperado |
|---|---|---|
| MISS-01 | MCAR bajo | Recuperación calibrada dentro de tolerancias predefinidas |
| MISS-02 | MAR por covariables basales observadas | Recuperación bajo modelo correcto y positividad |
| MISS-03 | MAR por historia postasignación observada | Método longitudinal que respeta orden temporal |
| MISS-04 | MNAR dependiente de Value no observado | Sensibilidad/límites; no afirma identificación puntual automática |
| MISS-05 | Pérdida diferencial por brazo | Reporta efecto de Z sobre retención y sesgo potencial |
| MISS-06 | Pérdida ligada a accesibilidad | No condiciona ingenuamente en observación; modela selección |
| MISS-07 | Value falta más con Outcome desfavorable | Sensibilidad MNAR/tipping point |
| MISS-08 | Snapshot T_acc intermedio ausente | Temporalidad y Reach indeterminados donde corresponda |
| MISS-09 | Solo se observan ejecutores de τ2 | Rechaza análisis causal restringido a ejecutores |
| MISS-10 | Validación seleccionada por A_obs sin diseño conocido | Error de medición no identificado por validación |
| MISS-11 | Abandono tras evento adverso | No asume MAR sin medir evento; sensibilidad |
| MISS-12 | Value no definido vs Value no medido | Separa ausencia ontológica y falta de observación |
| MISS-13 | Pérdida por clúster/unidad organizativa | Ajusta unidad y dependencia; no usa independencia falsa |
| MISS-14 | Retención casi nula en un estrato | Detecta positividad fallida; restringe objetivo o no identifica |
| MISS-15 | Documentación diferencial de U/R/C | Audita sesgo de reconstrucción por dimensión |

## 7. Contratos de versiones y trayectorias VER/TRJ

### VER-01…06

| ID | Alteración | Aserción |
|---|---|---|
| VER-01 | Mismo ΔT_acc, distinto coste | No declara equivalencia causal |
| VER-02 | Mismo ΔT_acc, distinta demora | Conserva versiones separadas |
| VER-03 | Mismo ΔT_acc, distinto riesgo/calidad | No agrupa como un tratamiento único |
| VER-04 | Versión asignada ≠ versión recibida | Registra ambas por separado |
| VER-05 | Incumplimiento | ITT sigue definido por Z, no por recepción |
| VER-06 | Efecto paquete con vías adicionales | No etiqueta como θ_A(q) |

### TRJ-01…07

| ID | Alteración | Aserción |
|---|---|---|
| TRJ-01 | Factible pero desconocida | No equivale a inaccesible |
| TRJ-02 | Conocida pero no considerada | Conserva estado distinto |
| TRJ-03 | Seleccionada pero no iniciada | No equivale a ejecutada |
| TRJ-04 | Ejecución parcial e interrupción | Conserva ambos eventos y marcas temporales |
| TRJ-05 | Finalización sin criterio terminal | No acepta estado completado |
| TRJ-06 | Ejecución usada para reconstruir T_acc | Detecta circularidad temporal |
| TRJ-07 | Estimador ajusta por selección/ejecución postratamiento | Falla si cambia el estimando o induce sesgo no previsto |

## 8. Contratos de interacción y factibilidad INT

| ID | Fixture | Resultado esperado |
|---|---|---|
| INT-01 | Cuatro combinaciones de q/g factibles e identificables | Calcula interacción en escala y contraste preespecificados |
| INT-02 | Una combinación imposible o sin soporte | Devuelve no identificación/restricción explícita; nunca extrapola silenciosamente |

Además, XSYNC-138-04 exige un test de soporte por estrato e historia para cada política; XSYNC-138-02 exige que la regla Value no forme parte de q; XSYNC-138-08 exige que los dictámenes metodológicos C10-S y las conclusiones científicas C10-D1 se emitan en campos separados.


## 9. Contratos de atribución de política y cobertura XSYNC

| ID | Fixture / perturbación | Oráculo y salida exigida | Falla si… |
|---|---|---|---|
| POL-01 | DGP aislado: Z aleatoriza B_g0/B_g1; ambas políticas difieren solo en la probabilidad final verificada de apertura focal; q* común; no vías directas | ITT_Z recupera el contraste entre políticas y puede etiquetarse como θ_Af(q*) solo si se satisfacen las condiciones de atribución | El analizador llama θ_Af al ITT sin verificar mapeo, exclusión, versiones, q* y Value |
| POL-02 | DGP con vía directa B→Value o B→coste/calidad/seguridad | ITT_Z permanece como efecto de política/paquete; θ_Af no identificado por ese contraste | El analizador mantiene atribución focal pese a la vía directa |
| POL-03 | Dos versiones con mismo A_f*/ΔT_acc, pero distinto coste/latencia/calidad | Mantiene equivalencia de accesibilidad separada de equivalencia causal y versión | Agrupa versiones por igualdad de ΔT_acc |
| POL-04 | p0/p1 aplicados a intentos, con fallo de instalación posterior | Recalcula probabilidades finales C_dep,post/A_f,post* y verdad de Value | Conserva θ=3.6 cuando el mecanismo final ya no produce .20/.80 |
| POL-05 | Regla de Value incluida erróneamente dentro de q_X | Detecta mezcla entre régimen de condiciones e instrumento evaluativo | Acepta que q cambie la definición de Value entre brazos |
| POL-06 | g1/g0 no factibles en una historia/estrato | Restringe población ex ante o emite no-identificación del contraste original | Extrapola a configuración imposible o sin soporte |
| POL-07 | θ_A^dyn usado sin historia/políticas/horizonte formalizados | Marca estimando como no disponible/no evaluable | Lo estima como si estuviera definido |
| POL-08 | Dictamen metodológico C10-S PASS sin evidencia empírica C10 | Emite por separado estado del test sintético y conclusión científica C10 | Convierte PASS sintético en confirmación/refutación empírica |
| POL-09 | Resultado impreciso cuyo intervalo cruza cero y ±δ/±ε | Emite INDETERMINATE o evidencia insuficiente según regla preespecificada | Declara equivalencia por p>0.05 |
| POL-10 | Enumerador correcto, pero estados de conocimiento/consideración/selección/ejecución incompletos | Limita el dictamen al módulo efectivamente probado | Afirma validación end-to-end de selección y ejecución sin pruebas |

Estos contratos convierten los hallazgos XSYNC-138-01…10 en aserciones verificables. La correspondencia no es uno-a-uno: varios hallazgos comparten pruebas, y la aceptación exige que cada hallazgo tenga al menos un test discriminante y una revisión documental global.


## 10. Familias GEN y requisitos aún no convertidos a fixtures

Los invariantes S4R-GEN-01…12 de C10-S §30.8 deben convertirse en pruebas con verdad oculta y aserciones equivalentes. Los hallazgos AUD-004…008 requieren contratos específicos para ΔT_acc, Reach_possible, S5-F, S5-C y no circularidad de Value. No se declara que los catálogos existentes cubran estas familias de forma ejecutable.

## 11. Reglas de interpretación del resultado

- PASS significa que el analizador discrimina correctamente el escenario sintético y recupera lo que el DGP hace identificable dentro de tolerancias justificadas.
- FAIL significa que viola una aserción, confunde constructos/estimandos o emite una conclusión no permitida.
- INDETERMINATE significa que la evidencia, soporte, precisión o identificación no permiten una decisión.
- **No identificación** es una conclusión metodológica correcta en ciertos fixtures, no un fallo del analizador.
- No usar ausencia de significación como equivalencia.
- No calcular Wald con primera etapa nula.
- No atribuir ITT_Z a accesibilidad cuando exclusión no está defendida.
- No convertir un resultado sintético PASS en evidencia empírica de C10.

## 12. Pendientes antes de convertirlo en contrato ejecutable

1. Confirmar diccionario y temporalidad de cada variable.
2. Fijar versiones del fixture y mecanismo exacto B_g0/B_g1, intento, éxito y verificación.
3. Resolver población, F*, q*, horizonte y regla Value.
4. Especificar verdad oculta, parámetros y salidas exactas por prueba.
5. Justificar tolerancias, N, réplicas, precisión, δ y ε.
6. Definir códigos de error y artefactos reproducibles.
7. Auditar no filtración entre generador, analizador y evaluador.
8. Obtener revisión independiente.
9. Autorizar por separado implementación y ejecución.

**Dictamen:** este registro normaliza el inventario de pruebas conocido y explicita las aserciones mínimas. No constituye implementación, ejecución ni PASS. El cierre de AUD-003 y XSYNC-01…10 depende de completar los fixtures, verificar cobertura y realizar la auditoría independiente.


## 13. Contratos recuperados de las secciones 182 y 183 (fuente DOCX, 2026-11-04)

Las fichas siguientes se transcriben de las tablas de aceptación de la fuente conversacional recuperada. Se incorporan como **contratos propuestos**, no como tests implementados ni ejecutados.

### P182-01…12 — Validez de constructo y sensibilidad de medidas

| ID | Prueba | Criterio de aceptación |
|---|---|---|
| P182-01 | Cobertura de A | Todas las condiciones constitutivas están documentadas |
| P182-02 | Circularidad de A | A no depende de O ni de V |
| P182-03 | Especificación de O | Cada indicador tiene unidad, fuente y ventana |
| P182-04 | Separación O/V | Ningún indicador usa automáticamente la valoración como resultado operativo |
| P182-05 | Reproducibilidad | Los valores pueden reconstruirse desde los registros |
| P182-06 | Acuerdo interevaluador | Se informa acuerdo y discrepancias |
| P182-07 | Error en A | Se evalúan falsos positivos y falsos negativos |
| P182-08 | Error en O/V | Se comparan escenarios de error de medición |
| P182-09 | Invariancia | Se detectan cambios de criterio entre D1 y D2 |
| P182-10 | Sensibilidad de Value | Se informa si las conclusiones cambian bajo reglas alternativas |
| P182-11 | Separación de datos | El analizador no recibe variables latentes del generador |
| P182-12 | Trazabilidad | Cada resultado conserva versión de indicador y regla aplicada |

### P183-01…13 — Datos ausentes, censura e identificación

| ID | Prueba | Criterio de aceptación |
|---|---|---|
| P183-01 | Taxonomía | Cada ausencia tiene categoría documentada |
| P183-02 | Mecanismo | Se evalúan MCAR, MAR y MNAR |
| P183-03 | Separación A | Desconocido no equivale a inaccesible |
| P183-04 | Separación O | No observado no equivale a resultado cero |
| P183-05 | Separación V | Ausencia dimensional no implica valoración nula |
| P183-06 | ITT | Se conserva la población aleatorizada |
| P183-07 | Selección | Se auditan mecanismos postasignación |
| P183-08 | Mediación | Se evalúa el efecto de la ausencia de A sobre la identificación |
| P183-09 | Censura | Se distingue censura administrativa e informativa |
| P183-10 | Sensibilidad | Se incluyen escenarios MAR y MNAR |
| P183-11 | Cotas | Se calculan cuando no procede una estimación puntual |
| P183-12 | Dictamen | Cada estimando recibe su propio estado de identificación |
| P183-13 | Trazabilidad | Se conservan reglas, versiones y decisiones |

La fuente especifica que las pruebas son propuestas, no ejecutadas. La sección 183 exige dictámenes separados para ITT sobre O, ITT por dimensión de V, efecto mediado por A, LATE sobre V, efecto residual e índice agregado si se utiliza; no debe emitirse un único dictamen global que oculte diferencias de identificación.


## 14. Contrato D2 primario candidato / D1 secundario y primera etapa focal

**Precedencia vigente por DEC-C10-066:** D2 es el escenario primario candidato; D1 es el escenario secundario. Esta precedencia no aprueba todavía el comparador, sus parámetros ni la identificación causal. Los valores de la tabla son objetivos candidatos del DGP, no resultados validados.

| Elemento | D1 secundario | D2 primario candidato |
|---|---:|---:|
| C_dep,base | 0 | 0 |
| P(C_dep,post=1 dado Z=0) | .20 | 0 |
| P(C_dep,post=1 dado Z=1) | .80 | .80 |
| Primera etapa objetivo | .60 | .80 |

Aserciones: (1) población P*_tau2 basal con A_f,base*=0; (2) intento, éxito, verificación, A_f,post* y D_f se almacenan por separado; (3) p_z corresponde al estado final verificado, no al intento; (4) A_f,post* coincide probabilísticamente con C_dep,post solo si el resto de condiciones focales está satisfecho; (5) el generador no asigna directamente A desde Z; (6) D1 exige justificar provisión ordinaria en control; (7) .20/.80 son objetivos del DGP, no resultados.

Estado: contrato candidato definido documentalmente; fixtures, oráculos, tolerancias y pruebas no implementados ni ejecutados.


## 15. Pruebas de aceptación documental de B y calibración D1/D2

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| B-01 | Asignación | Z y versión B asignada se registran antes de cualquier intento |
| B-02 | Oferta/recepción | B asignada, ofrecida y recibida son campos distintos |
| B-03 | Intento | W_attempt coincide con la regla D1/D2 (.25/1 o 0/1) en el DGP |
| B-04 | Éxito conjunto | P(C_dep=1 dado W_attempt=1)=.80 en la factorización candidata |
| B-05 | Componentes | Instalación, integridad, compatibilidad y operatividad se conservan por separado |
| B-06 | Calibración final | C_dep final reproduce .20/.80 en D1 y 0/.80 en D2 |
| B-07 | Baseline | C_dep,base=0 y A_f,base*=0 antes de Z en la población de apertura |
| B-08 | No filtración | Analizador no recibe latentes ni parámetros generadores |
| B-09 | Crossover | Provisión fuera de la versión asignada se identifica como crossover, no se reclasifica el brazo |
| B-10 | Vías colaterales | DGP aislado mantiene invariantes; adversarial introduce y detecta vías |
| B-11 | Accesibilidad | A_f* se deriva de C_dep y demás predicados; no se copia de Z/W |
| B-12 | Primera etapa | Diferencia de C_dep y de D_f se reporta por separado; no se asumen idénticas |
| B-13 | D2 | Control sin intento focal; no se confunde D2 con D1 |
| B-14 | Versionado | Módulo, protocolo, umbrales, actor y fecha quedan identificados |

**Estado:** contrato de pruebas propuesto; no implementado ni ejecutado. La prueba B-04 valida la factorización propuesta, no prueba que sea la única o científicamente correcta.


## 16. Pruebas de aceptación documental de q_X* y soporte

| ID | Prueba | Criterio propuesto |
|---|---|---|
| QX-01 | Temporalidad | X, H0, Cc, E, C_dep,0 y A_f,0* quedan medidos antes de Z |
| QX-02 | Población | qX condiciona solo por criterios basales preespecificados |
| QX-03 | Cuatro estados | Cumplida/incumplida/indeterminada/no aplicable no se colapsan |
| QX-04 | Separación | Cc constitutiva no se confunde con C_dep focal |
| QX-05 | Factibilidad | B_g0 y B_g1 son implementables por cada historia con masa positiva |
| QX-06 | Asignación | Probabilidad de ambos brazos positiva por estrato/historia objetivo |
| QX-07 | No extrapolación | Historias sin factibilidad se restringen ex ante o se declaran no identificadas |
| QX-08 | No postratamiento | No se filtra población usando cumplimiento, A_post, selección, ejecución, O o V |
| QX-09 | qL | Si L_m post-Z es indispensable, existe regla secuencial, historia, momento, soporte e identificación |
| QX-10 | Estimando | ITT_Z, psi_B, theta_Af, LATE_f y theta_A no se intercambian |

Estado: contrato documental candidato; no calculado, implementado ni ejecutado. No se declara positividad empírica sin datos o DGP cuantificado.


## 17. Pruebas de unidad, aleatorización e interferencia

| ID | Prueba | Criterio de aceptación |
|---|---|---|
| UNIT-01 | Identidad de unidades | UE, UA y UO están identificadas; observaciones repetidas no se cuentan como UE independientes |
| UNIT-02 | Independencia primaria | No hay recursos, agentes, información, infraestructura ni canales compartidos relevantes entre UE |
| UNIT-03 | Correlación basal | Distingue correlación por clúster sin spillover de interferencia causada por Z |
| UNIT-04 | Spillover de recurso | Cambiar Z de una unidad altera disponibilidad/resultado de otra; detecta y rechaza ITT individual simple |
| UNIT-05 | Spillover informacional | Provisión/instrucción se transmite entre unidades; requiere mapa de exposición |
| UNIT-06 | Aleatorización por clúster | La UA pasa a ser clúster; N e inferencia se basan en clústeres y probabilidades correctas |
| UNIT-07 | Exposición parcial | Potenciales y estimandos incorporan G_i(Z_-i); separa efecto directo/indirecto/total |
| UNIT-08 | Exposición desconocida | Devuelve INDETERMINATE/NO IDENTIFIED, no fuerza supuesto SUTVA |
| UNIT-09 | Positividad | Comprueba probabilidad positiva en unidad realmente aleatorizada y soporte de exposición |
| UNIT-10 | LATE bajo interferencia | Rechaza Wald individual como LATE_f si no interferencia no se sostiene |
| UNIT-11 | Integridad de asignación | Registra semilla, algoritmo, bloque/estrato, versión B, probabilidades y desviaciones |
| UNIT-12 | Tamaño efectivo | Distingue N de UE, N de UA/clústeres y observaciones longitudinales |
| UNIT-13 | No clúster retrospectivo | Prohíbe definir agrupación después de observar Outcome/Value para ajustar errores |
| UNIT-14 | Cambio de unidad | Si cambia UE/UA, exige recalcular población, estimando, qX, soporte, N y protocolo |

Estado: contratos propuestos, no implementados ni ejecutados.


## 18. Pruebas F* y clasificación de rutas alternativas

| ID | Prueba | Criterio de aceptación |
|---|---|---|
| FSTAR-01 | Independencia de F* | F* se define sin Outcome/Value y antes de Z |
| FSTAR-02 | Ficha completa | Objetivo, entrada/S0, salida, restricciones, tolerancias, H, G, C0 y evidencia |
| FSTAR-03 | Identidad vs función | Ruta distinta de τ2 puede cumplir F* sin fusionar identidades |
| FSTAR-04 | Accesibilidad vs aplicabilidad | No inferir una de otra |
| FSTAR-05 | Substituibilidad | Cumple F* con recursos/precondiciones y dentro de H |
| FSTAR-06 | Composición | Detecta rutas compuestas y distribuidas del universo declarado |
| FSTAR-07 | Recursos | Rechaza ruta que requiere recursos no disponibles; conserva límite contextual |
| FSTAR-08 | Tres estados | F_alt,0=0/1/? sin convertir indeterminado en ausente |
| FSTAR-09 | Cobertura | “No encontrado” sin cobertura suficiente devuelve indeterminado |
| FSTAR-10 | Cegamiento | Clasificación ciega a Z, B, selección, ejecución, O y V |
| FSTAR-11 | Poblaciones | Alternativa presente: permanece en P*_τ2 y sale de P*_F |
| FSTAR-12 | Alternativa indeterminada | Puede permanecer en P*_τ2; P*_F no confirmada |
| FSTAR-13 | Efecto B en alternativa | Detecta vía B→alternativa y rechaza LATE focal bajo exclusión vulnerada |
| FSTAR-14 | Activación post-Z | Clasifica mecanismo postratamiento; prohíbe ajuste ingenuo |
| FSTAR-15 | Sensibilidad | Reporta sensibilidad a error de clasificación, cobertura, G/H/tolerancias |
| FSTAR-16 | Reporte poblacional | Separa P*_τ2, P*_F, diferencia, indeterminados y excluidos |
| FSTAR-17 | q y pesos | Exige distribución objetivo/soporte/pesos propios si se estima efecto en P*_F |
| FSTAR-18 | Límite de exclusividad | PASS solo dentro de universo, granularidad, contexto y horizonte auditados |

Estado: pruebas contractuales documentales; no implementadas ni ejecutadas.


## 19. Contratos de medición focal y cambio transformacional

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| AFT-01 | Truth no filtrada | Analizador no recibe A_f*, C_dep*, D_f*, T_acc* ni ΔT_acc* |
| AFT-02 | Asignación separada | Cambiar Z sin cambiar condiciones verificadas no cambia automáticamente A_f* |
| AFT-03 | C_dep compuesto | C_dep se deriva de componentes verificados; intento no equivale a éxito |
| AFT-04 | Predicados adicionales | C_dep=1 no basta si falta otro predicado de acceso requerido |
| AFT-05 | Aplicabilidad separada | A_f=1 y App_f=0 es representable sin contradicción |
| AFT-06 | Ejecución no definitoria | No ejecutar τ2 no implica A_f=0; ejecutar no reemplaza medición independiente |
| AFT-07 | Tres estados observados | A_f_obs=1/0/?; indeterminado nunca se recodifica como 0 |
| AFT-08 | Elegibilidad basal | P*_τ2 verdadera y elegibilidad observada se reportan separadas; no se equiparan con error |
| AFT-09 | D_f basal→post | D_f* requiere A_f*,base=0 y A_f*,post=1; no se confunde con A_f*,post |
| AFT-10 | Primera etapa medida | Reporta ITT_Df* y ITT_Df_obs por separado cuando existe error |
| AFT-11 | Error diferencial | Detecta Se/Sp distintos por Z, versión o tiempo; no aplica corrección ingenua |
| AFT-12 | Validación sesgada | Validación no aleatoria sin probabilidades conocidas no identifica Se/Sp puntuales |
| AFT-13 | Referencia imperfecta | Propaga error de referencia; no etiqueta gold standard sin fundamento |
| DTA-01 | Identidad/versionado | Distingue identidad canónica, versión y cambio de definición |
| DTA-02 | Relaciones | Detecta relaciones añadidas, retiradas y reconfiguradas sin crear identidades ficticias |
| DTA-03 | Condiciones | Registra cambio de valor/estado de condición sin declararlo transformación nueva |
| DTA-04 | Validez/cobertura | Cambios de evidencia, validez y cobertura quedan explícitos |
| DTA-05 | Snapshots comparables | Incompatibilidad de catálogo/granularidad/reglas devuelve indeterminado o exige correspondencia |
| DTA-06 | Diferencia estructurada | ΔT_acc conserva ΔU, ΔR, ΔC, ΔValidity y ΔState; no se reduce a escalar |
| DTA-07 | Indeterminación | No transforma elementos indeterminados en altas/bajas ciertas |
| DTA-08 | No circularidad | Outcome, Value, selección y ejecución no definen T_acc ni ΔT_acc |

Estado: contratos de aceptación documentales; no implementados ni ejecutados. Las tolerancias y fixtures se fijarán antes de cualquier implementación.


## 20. Contratos de clasificación causal de condiciones de τ2

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| CLS-01 | C_dep compuesto | Cada componente C_install/integrity/compat/oper tiene definición, evidencia y tiempo |
| CLS-02 | Autorización basal | C_auth_base se distingue de Z y de autorización manipulada por política |
| CLS-03 | Recurso | Disponibilidad ex ante se distingue de consumo/insumo de ejecución |
| CLS-04 | Capacidad | Capacidad instalada se distingue de saturación y precondiciones de S0 |
| CLS-05 | Información | Información técnica integrada se distingue de conocimiento/formación/mensajes |
| CLS-06 | Dominio | Compatibilidad del objeto/dominio se distingue de precondiciones del estado |
| CLS-07 | Aplicabilidad | A_f=1, App_f=0 es representable |
| CLS-08 | C_other | Ninguna variable heterogénea permanece bajo un comodín sin definición |
| CLS-09 | No intervención colateral | Cambio de C_auth/recursos/capacidad/información/conocimiento identifica paquete, no efecto aislado |
| CLS-10 | Factibilidad q/g | Ninguna condición manipulada por g se fija simultáneamente como componente incompatible de q* |
| CLS-11 | Cegamiento temporal | Clasificación y elegibilidad no usan selección, ejecución, Outcome ni Value |
| CLS-12 | Escenario adversarial | Cambios colaterales activan dictamen de paquete o no identificación |

Estado: contratos documentales; no implementados ni ejecutados. Los fixtures, tolerancias y adjudicación permanecen pendientes.


## 21. Contratos de frontera, nivel y recursos

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| SYS-01 | Capacidad vs acceso | Una transformación puede pertenecer a T_cap y no a T_acc(i) |
| SYS-02 | Cambio de asignación | ΔT_acc(i) puede ser distinto de cero con ΔT_cap=0 |
| SYS-03 | Cambio estructural | ΔT_cap puede ser distinto de cero sin cambiar T_acc(i) |
| SYS-04 | Recursos compartidos | La saturación/concurrencia se refleja en disponibilidad por unidad/ventana |
| SYS-05 | Consumo | No inferir falta de acceso desde ausencia de consumo |
| SYS-06 | Aplicabilidad | T_acc(i)=1 y App_f(i)=0 es representable |
| SYS-07 | Conocimiento | Conocimiento no convierte una transformación no accesible en accesible |
| SYS-08 | No conocimiento | No conocer/no ejecutar no elimina accesibilidad respaldada |
| SYS-09 | Interferencia | Reasignación a j puede afectar T_acc(i) si el recurso es rival |
| SYS-10 | Frontera externa | Dependencia externa no declarada impide dictamen de cobertura completo |
| SYS-11 | Nivel de asignación | Desajuste entre unidad de Z y unidad de A_f exige modelo multinivel |
| SYS-12 | Agregación | No se agrega por unión/promedio sin estimando y regla predefinidos |

Estado: contratos documentales, no implementados ni ejecutados.


## 22. Contratos de unidad, frontera e intervención primaria

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| BND-01 | Frontera completa | Cada dependencia necesaria de τ2 está dentro de B_sys o declarada externa con versión/contrato |
| BND-02 | Unidad primaria | UE=UA=i; UO son medidas repetidas, no unidades nuevas |
| BND-03 | Niveles | T_cap=T_acc solo si no hay subunidades con acceso diferenciado y la frontera lo justifica |
| BND-04 | Asignación | Z asigna B; Z no se interpreta como provisión, accesibilidad ni ejecución |
| BND-05 | Política material | B tiene acción técnica focal, versión, actor, destinatario, tiempo y mecanismo verificables |
| BND-06 | Vías colaterales | Cambio de autorización/recursos/capacidad/conocimiento/coste/calidad activa dictamen de paquete |
| BND-07 | q_X* | q_X* define historia basal; no fuerza condiciones post-Z ni fija una variable manipulada por B |
| BND-08 | Soporte | Ambas políticas factibles y con probabilidad positiva en cada historia basal objetivo |
| BND-09 | Población | P*_τ2 y P*_F se determinan pre-Z; no se filtra por cumplimiento o resultados |
| BND-10 | No interferencia | No hay recursos, agentes, información ni canales compartidos entre instancias primarias |
| BND-11 | Adversarial | Spillovers fuerzan clúster/exposición y estimando compatible; no ITT individual ingenuo |
| BND-12 | Dependencias externas | Dependencia no inventariada impide declarar frontera/cobertura completa |

Estado: contratos documentales; no implementados ni ejecutados.


## 23. Contratos de intervención material B

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| BACT-01 | Definición de brazos | B0 mantiene configuración basal; B1 aplica protocolo focal versionado |
| BACT-02 | Actor y destinatario | Rol, instancia, objeto τ2, versión y tiempos identificables |
| BACT-03 | Separación Z/B | Z solo asigna; provisión recibida e intento se registran aparte |
| BACT-04 | Instalación | Declaración/intent no basta; identidad y configuración verificadas |
| BACT-05 | Integridad | Hash/configuración corresponden a artefacto autorizado |
| BACT-06 | Compatibilidad | Dependencias e interfaces cumplen contrato versionado |
| BACT-07 | Operación | Canal técnico disponible sin exigir ejecutar τ2 |
| BACT-08 | Primera etapa | C_dep* y A_f* derivan de componentes/predicados verificados |
| BACT-09 | No ejecución forzada | B1 no obliga a seleccionar ni ejecutar τ2 |
| BACT-10 | Vías colaterales | Cambio de condición no focal fuerza reclasificación como paquete |
| BACT-11 | Incumplimiento | Fallo/parcialidad/rollback conserva asignación ITT |
| BACT-12 | Contaminación | Provisión focal en B0 se registra sin reasignar Z |
| BACT-13 | Indeterminación | Evidencia insuficiente conserva estado ? |
| BACT-14 | Exclusión | Efecto directo B→Outcome/Value se representa como adversarial; no se presume ausencia |
| BACT-15 | q y poblaciones | B0/B1 factibles en historias q_X* y elegibilidad pre-Z |
| BACT-16 | Consistencia | Una versión definida de B corresponde a cada brazo; desviaciones versionadas |
| BACT-17 | No interferencia | Provisión y artefactos no se transmiten entre instancias del primario |
| BACT-18 | Revisión independiente | Compatibilidad con C10-D1/S4-R y auditoría de invariantes revisadas antes de freeze |

Estado: contratos documentales, no implementados ni ejecutados.


## 24. Contratos de medición focal y ΔT_acc

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| MEAS-01 | C_dep no suficiente | C_dep*=1 con AUTH/RES/REL/COND/BLOCK fallido no produce A_f*=1 |
| MEAS-02 | Ruta alternativa de acceso | C_dep*=0 no fuerza A_f*=0 si otra ruta válida invoca la misma τ2 |
| MEAS-03 | Predicado focal | A_f* requiere ID/REL/COND/AUTH/RES/DEP y ausencia de BLOCK; validez/cobertura de evidencia se registra en E_T y no se incorpora a truth estructural |
| MEAS-04 | Acceso vs aplicabilidad | A_f*=1 y App_f=0 es representable |
| MEAS-05 | Acceso vs ejecución | No ejecución no implica A_f*=0; ejecución no sustituye medición |
| MEAS-06 | Canal de verdad | Analizador no recibe A_f*, C_dep*, D_f*, T_acc* ni ΔT_acc* |
| MEAS-07 | Cegamiento | Clasificación ciega a Z/B, selección, ejecución, Outcome y Value |
| MEAS-08 | Tres estados | A_f,obs conserva 1/0/?; indeterminado no es ausencia |
| MEAS-09 | Apertura focal | D_f*=1 si y solo si A_f,base*=0 y A_f,post*=1 |
| MEAS-10 | Elegibilidad basal | Baseline indeterminado no se clasifica como elegible confirmada |
| MEAS-11 | Primera etapa | ITT_Df* separado de ITT_Df,obs y de tasa C_dep* |
| MEAS-12 | Validación | Sensibilidad/especificidad puntual solo con validación adecuada; de otro modo límites/sensibilidad |
| MEAS-13 | Error diferencial | Detecta Se/Sp por Z, versión y tiempo; propaga incertidumbre |
| MEAS-14 | Snapshot | U/R/C/Validity/State versionados y trazables |
| MEAS-15 | Compatibilidad | Snapshots no comparables producen indeterminado o correspondencia explícita |
| MEAS-16 | Diff estructurado | ΔU/ΔR/ΔC/ΔValidity/ΔState no se reduce a D_f* |
| MEAS-17 | Proyección focal | h_f(ΔT_acc*)=D_f* solo bajo contrato focal y snapshots compatibles |
| MEAS-18 | No circularidad | Outcome/Value/selección/ejecución no definen accesibilidad |
| MEAS-19 | Alternativas | Substituibilidad F* no equivale a accesibilidad de τ2 |
| MEAS-20 | Vías colaterales | Cambio de AUTH/RES/capacidad/conocimiento/alternativas activa paquete/efecto conjunto |
| MEAS-21 | Dependencias externas | Dependencias no inventariadas impiden PASS de validez/cobertura |
| MEAS-22 | Verdad vs observado | Error del analizador se evalúa contra canal de verdad aislado, sin filtración |
| MEAS-23 | Estados indeterminados | Conflicto/cobertura insuficiente se propaga como ? |
| MEAS-24 | Evidencia temporal | Cada predicado y cambio conserva timestamp, ventana y procedencia |

Estado: contratos documentales; no implementados ni ejecutados.


## 25. Contratos de clasificación temporal-causal

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| TEMP-01 | Indexación | Cada condición tiene componente, unidad, nivel, tiempo, versión y rol |
| TEMP-02 | Baseline sellado | Elegibilidad y A_f,base* usan solo información pre-Z |
| TEMP-03 | No reconstrucción | Baseline nunca se reconstruye desde post-Z |
| TEMP-04 | Constitutiva/temporal | Predicado constitutivo puede ser basal o post; rol causal indexado por tiempo |
| TEMP-05 | C_dep | Componentes pre/post separados y versionados |
| TEMP-06 | Autorización | C_auth basal separada de intervención posterior sobre autorización |
| TEMP-07 | Recursos | Stock, disponibilidad, asignación, demanda y consumo separados |
| TEMP-08 | Capacidad | Instalada, slots, disponibilidad temporal y saturación separados |
| TEMP-09 | Información | Configuración técnica separada de mensajes, formación y conocimiento |
| TEMP-10 | Dominio/estado | Compatibilidad de objeto separada de precondiciones S0/App_f |
| TEMP-11 | Alternativas | F_alt basal pre-Z; cambios post-Z registrados como vías potenciales |
| TEMP-12 | Mediadores | C_dep/A_f/Reach/K/Select/Exec post-Z no tratados como basales |
| TEMP-13 | No ajuste post | ITT no ajustado por mediadores post-Z para inferir efecto directo |
| TEMP-14 | Confusión temporal | Confusores afectados por tratamiento requieren método longitudinal |
| TEMP-15 | Co-intervención | Cambio no focal detectado y etiquetado como paquete/vía alternativa |
| TEMP-16 | Medición | VALID/cobertura no se confunde con condición causal del sistema |
| TEMP-17 | Missingness diferencial | Cambio de observabilidad por B se modela |
| TEMP-18 | Orden temporal | t−1, t0…t9 y eventos t+1 respetan orden/snapshots inmutables |
| TEMP-19 | Política B | Detecta incompatibilidad entre §62 y probabilidades .20/.80 |
| TEMP-20 | Autorización alternativa | C_auth no se mezcla con provisión primaria sin decisión explícita |

Estado: contratos documentales; no implementados ni ejecutados.


## 26. Contratos de política B y calibración D1/D2

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| BPOL-01 | Separación de escenarios | D1 y D2 están identificados como contrastes distintos, no mezclados |
| BPOL-02 | Programación, intento y estado final | W_programmed, W_attempt efectivo y C_dep verificado no se confunden |
| BPOL-03 | D1 control | P(W_programmed=1|Z=0)=.25; W_attempt efectivo y C_dep se registran/derivan aparte |
| BPOL-04 | D1 tratamiento | P(W_programmed=1|Z=1)=1; no se presume W_attempt efectivo=1 |
| BPOL-05 | D2 control | P(W_programmed=1|Z=0)=0; intento de fondo y C_dep=1 se investigan y registran, no se presuponen ausentes |
| BPOL-06 | D2 tratamiento | P(W_programmed=1|Z=1)=1; W_attempt efectivo, recepción y C_dep se observan/derivan aparte |
| BPOL-07 | Éxito condicional | .80 es candidato condicional a W_attempt efectivo elegible; no dato empírico ni tasa de cumplimiento |
| BPOL-15 | Cumplimiento | P(W_attempt=1|W_programmed=1) se registra/modela; no se fija en 1 sin autorización y evidencia |
| BPOL-16 | Provisión de fondo | P(W_attempt=1|W_programmed=0) se mide; D2 control no se declara limpio solo por q_programmed=0 |
| BPOL-17 | C_dep derivado | C_dep se deriva de W_attempt, éxito conjunto y fondo; .20/.80 o 0/.80 solo bajo supuestos explícitos de cumplimiento perfecto y una oportunidad |
| BPOL-08 | Componentes conjuntos | No se presume independencia entre instalación, integridad, compatibilidad y operatividad |
| BPOL-09 | Primera etapa focal | C_dep no sustituye a A_f*/D_f*; accesibilidad se deriva de todos los predicados |
| BPOL-10 | Control D1 legítimo | La justificación del comparador ordinario se documenta antes de aprobar D1 |
| BPOL-11 | Semántica §21/§62 | B0 sin provisión se limita al escenario D2 |
| BPOL-12 | Integridad ITT | Z conserva asignación; crossover, fallo e intento no redefinen el brazo |
| BPOL-13 | Vías colaterales | Se detectan cambios no focales y efecto de paquete |
| BPOL-14 | No ejecución anticipada | Sin aprobación explícita no hay freeze, implementación ni simulación |

Estado: contratos documentales; no implementados ni ejecutados.


## 27. Contratos de selección y legitimidad del comparador D1/D2

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| CMP-01 | Correspondencia objetivo-D1 | D1 se interpreta como provisión programada frente a régimen ordinario incremental |
| CMP-02 | Evidencia del régimen D1 | .25/.20 están respaldados por fuente independiente y población/contexto definidos |
| CMP-03 | No contaminación semántica D1 | Provisión prevista en B_g0^D1 no se etiqueta como crossover |
| CMP-04 | Correspondencia objetivo-D2 | D2 se interpreta como provisión programada frente a ausencia de intento focal |
| CMP-05 | Ausencia basal D2 | C_dep,base=0 y A_f,base*=0 se verifican antes de Z |
| CMP-06 | Ausencia de fondo D2 | No existe provisión focal no registrada ni ruta equivalente omitida |
| CMP-07 | Estimandos separados | ITT_D1 e ITT_D2 no se agrupan ni se presentan como el mismo contraste |
| CMP-08 | Primera etapa por variable | C_dep, A_f,post*, D_f y ΔT_acc se calculan separadamente por escenario |
| CMP-09 | LATE por escenario | No se asume identidad/transportabilidad de estratos de cumplidores |
| CMP-10 | Invariantes de política | Módulo, hash, protocolo, actor, recursos por intento y verificación son comparables según escenario |
| CMP-11 | Crossover | Recepción fuera de política/version se distingue de provisión ordinaria asignada |
| CMP-12 | Efecto de paquete | Vías colaterales impiden atribución exclusiva a accesibilidad |
| CMP-13 | Precedencia y legitimidad | D2 ya está aceptado como primario candidato por DEC-C10-066; su legitimidad exige verificar el objetivo ausencia-vs-provisión y la ausencia de provisión focal de fondo. D1 queda secundario y requiere justificar el régimen ordinario si se conserva como comparador interpretable |
| CMP-14 | No ejecución anticipada | Sin aceptación y gates no hay freeze, implementación, simulación ni ejecución |

Estado: contratos documentales; no implementados ni ejecutados.


## 28. Contratos de primera etapa técnica y accesibilidad

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| ACC-01 | Conjunción C_dep | C_dep=1 solo si C_install, C_integrity, C_compat y C_oper son todos 1 |
| ACC-02 | Fallo parcial | Cualquier componente respaldado como 0 produce C_dep,obs=0; no se compensa por otros componentes |
| ACC-03 | Indeterminación técnica | Sin fallo respaldado y con uno o más componentes desconocidos, C_dep,obs=? |
| ACC-04 | Intento separado | W_attempt=0 no se codifica como fallo de componente ni como éxito |
| ACC-05 | Operación ≠ ejecución | C_oper=1 no requiere ni implica selección/ejecución de τ2 |
| ACC-06 | Sin independencia implícita | El DGP no multiplica marginales ni presume independencia de los cuatro componentes |
| ACC-07 | Significado de .80 | .80 se interpreta como probabilidad conjunta condicional de C_dep tras intento elegible |
| ACC-08 | Sensibilidad de .80 | Escenarios alternativos de s y dependencia se preespecifican antes de freeze |
| ACC-09 | Accesibilidad completa | A_f* deriva de ID/REL/COND/AUTH/RES/DEP/¬BLOCK |
| ACC-10 | VALID epistémico | VALID/cobertura no altera truth estructural; afecta clasificación observada |
| ACC-11 | Ruta única | C_dep=DEP_f solo en fixture de ruta única inventariada |
| ACC-12 | Ruta alternativa | C_dep=0 con otra ruta válida no fuerza A_f*=0 |
| ACC-13 | Aplicabilidad separada | A_f*=1 y App_f=0 sigue siendo representable |
| ACC-14 | Primera etapa por variable | FS_Cdep, FS_Af y FS_Df se informan separadamente por D1/D2 |
| ACC-15 | Equivalencia condicional | .60/.80 solo se transfieren a A_f/D_f si elegibilidad basal y demás predicados están satisfechos e invariantes |
| ACC-16 | Snapshot incompatible | No se deriva D_f de snapshots/versiones no comparables |
| ACC-17 | No filtración | Truth de componentes, C_dep*, A_f* y D_f* permanece oculta al analizador |
| ACC-18 | Error diferencial | Se evalúa error por componente, brazo, escenario y tiempo; si no identificado, límites/sensibilidad |
| ACC-19 | Fallo/rollback/crossover | Se conserva evento, asignación Z y versión recibida sin reclasificar ITT |
| ACC-20 | No circularidad | Outcome/Value/selección/ejecución no definen A_f* ni predicados técnicos |

Estado: contratos propuestos; fixtures no implementados ni ejecutados.


## 29. Contratos de distribución conjunta y sensibilidad

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| JNT-01 | Soporte 16 patrones | La distribución contiene exactamente 16 celdas no negativas y suma 1 |
| JNT-02 | Éxito conjunto | s coincide con p1111, no con un producto implícito de marginales |
| JNT-03 | No identificación | Dos tablas distintas con mismo s y fallos parciales distintos son aceptadas como DGP distintos |
| JNT-04 | Fréchet | Marginales y s respetan límites de Fréchet |
| JNT-05 | Independencia explícita | Producto de marginales solo se utiliza en fixture que declara independencia |
| JNT-06 | Choque común | Fixture de dependencia positiva extrema reproduce el patrón declarado |
| JNT-07 | Fallo parcial | Fixtures con uno/dos/tres componentes fallidos conservan sus patrones |
| JNT-08 | Bottleneck | La sensibilidad puede variar el componente limitante |
| JNT-09 | Heterogeneidad | Estratos basales tienen distribuciones explícitas y no usan mediadores post-Z para definir asignación |
| JNT-10 | Deriva/versiones | Distribuciones de versiones/periodos no equivalentes no se agrupan implícitamente |
| JNT-11 | Sensibilidad s | La malla exploratoria se distingue de primeras etapas por brazo |
| JNT-12 | Reporte D1/D2 | Tablas, marginales y fallos se informan por escenario |
| JNT-13 | No filtración | Tabla, parámetros y truth no llegan al analizador |
| JNT-14 | Reintentos | Dependencia entre intentos/orden/rollback se registra explícitamente |
| JNT-15 | Reproducibilidad | Semilla, versión, parámetros y tabla permiten reconstruir cada réplica |

Estado: contratos propuestos; fixtures no implementados ni ejecutados.


## 30. Contratos de fixtures explícitos y propagación analítica

| ID | Prueba | Criterio de aceptación propuesto |
|---|---|---|
| FIX-01 | Tabla choque común | p1111=s, p0000=1−s, suma 1 |
| FIX-02 | Tabla fallos simples | Cuatro patrones simples con masa (1−s)/4; suma 1 |
| FIX-03 | Bottleneck | Un patrón de fallo con masa 1−s; marginales coherentes |
| FIX-04 | Fallos emparejados | Dos patrones con masa (1−s)/2; suma 1 |
| FIX-05 | Marginales | Coinciden con las derivadas de cada tabla |
| FIX-06 | Escalado s | Para s=.60/.70/.80/.90 cada tabla conserva no negatividad y suma 1 |
| FIX-07 | D1 first stage | q0=.25/q1=1 implica FS=.75s |
| FIX-08 | D2 first stage | q0=0/q1=1 implica FS=s |
| FIX-09 | D1 baseline | P0=.20 únicamente cuando s=.80 bajo q0=.25 |
| FIX-10 | No transferencia | FS_Cdep no se iguala a FS_Af/FS_Df sin supuestos |
| FIX-11 | Intentos múltiples | No usar fórmula de independencia sin contrato de dependencia |
| FIX-12 | Sin simulación | Fixtures analíticos no se presentan como resultados de réplicas |

Estado: contratos documentales propuestos; no implementados ni ejecutados.


## 31. Contratos del Bloque 1 — régimen q, intervención B y atribución causal

| ID | Fixture/verdad DGP | Aserción del analizador | Fallo que debe detectar |
|---|---|---|---|
| CAUS-01 | Z aleatoriza B; B cambia A_f* y no altera otras vías | Informa ITT_Z/ψ_B; solo etiqueta θ_Af(q*) si el contrato de aislamiento, q y versiones está satisfecho | Etiqueta cualquier ITT como efecto puro de accesibilidad |
| CAUS-02 | B altera C_auth además de provisión técnica | Informa efecto de paquete/conjunto o no identificación focal | Oculta C_auth dentro de A_f* y atribuye el paquete a accesibilidad |
| CAUS-03 | q_X* común con soporte insuficiente en un estrato para g1 o g0 | Marca θ_A(q) no identificable/no evaluable en ese soporte o restringe población con nuevo estimando explícito | Extrapola fuera del soporte o elimina unidades postratamiento |
| CAUS-04 | q_L* post-Z es mediador inducido por B | Conserva el efecto ITT total y no ajusta mecánicamente por el mediador | Condiciona por mediador y lo presenta como efecto directo |
| CAUS-05 | B modifica costes, calidad, seguridad, latencia, información o alternativas | Conserva ITT de política; retira atribución focal salvo estrategia válida | Presenta Wald/ITT como θ_A pese a vía directa |
| CAUS-06 | C_auth=0 basal y B no la modifica | Clasifica unidad fuera de la población focal elegible, según contrato aprobado | Atribuye a B una apertura imposible por condición constitutiva |
| CAUS-07 | C_auth=0 basal y B sí la modifica | Clasifica intervención como conjunta/autorización+provisión | La llama intervención pura de provisión técnica |
| CAUS-08 | D1 y D2 inducen first stages/compliers distintos | Reporta ITT, FS y LATE por escenario | Agrupa o transporta automáticamente Wald/LATE entre escenarios |
| CAUS-09 | Exclusión falla con verdad DGP conocida | Reporta ITT de política y no identifica LATE_f puro | No detecta vía directa |
| CAUS-10 | A_f* cambia sin que se ejecute τ2 | Reconoce apertura de accesibilidad sin ejecución | Define accesibilidad por ejecución observada |

Estos son contratos especificados documentalmente; no se han generado fixtures ni ejecutado pruebas. Requieren verdad oculta, versiones, entradas/salidas, tolerancias y revisión para cerrar AUD-003.


## 32. Contratos del Bloque 2 — población, elegibilidad, F* y comparadores

| ID | Fixture/verdad DGP | Aserción del analizador | Fallo que debe detectar |
|---|---|---|---|
| POP-11 | E=1, C_dep,0=0, A_f,0*=0, F_alt,0=0 | Unidad pertenece a P*_τ2 y P*_F | Excluir por error o confundir objetivos |
| POP-12 | E=1, C_dep,0=0, A_f,0*=0, F_alt,0=1 | Unidad pertenece a P*_τ2, no a P*_F | Excluirla de P*_τ2 por alternativa basal |
| POP-13 | E=1, C_dep,0=0, A_f,0*=0, F_alt,0=? | P*_τ2 confirmable; P*_F no confirmable | Tratar indeterminación como ausencia |
| POP-14 | Alguna condición constitutiva incumplida | Fuera de población focal confirmatoria antes de Z | Mantenerla como elegible |
| POP-15 | Condición constitutiva indeterminada | Elegibilidad no confirmada; registrar flujo y sensibilidad | Recodificarla como cumplida/incumplida sin regla |
| POP-16 | Accesibilidad basal A_f,0*=1 | Fuera de población de apertura τ2; cohorte distinta si procede | Mezclar mantenimiento con apertura |
| POP-17 | Dependencia basal C_dep,0=0 pero A_f,0*=1 por ruta alternativa | Detecta discordancia y exige auditoría de ruta/medición | Inferir A_f,0*=0 desde C_dep,0 |
| POP-18 | D_f,0 y D_f* aparecen con roles distintos | Aplica crosswalk C_dep,0 / A_f,0* / A_f,1* / D_f* | Confunde disponibilidad basal con apertura |
| FSTAR-01 | Ruta cumple F* con identidad distinta a τ2 | Mantiene identidad distinta y substituibilidad funcional | Colapsar F* y τ2 |
| FSTAR-02 | Ruta alternativa sin cobertura de búsqueda suficiente | F_alt,0=? | Declarar ausencia por “no encontrado” |
| FSTAR-03 | Ruta documental E1 sin prueba mecanística/técnica | No inferir realizabilidad | Aceptar descripción como ruta accesible |
| FSTAR-04 | Ruta accesible pero no aplicable desde S0 | Juicios separados de accesibilidad y aplicabilidad | Inferir aplicabilidad desde accesibilidad |
| FSTAR-05 | Ruta supera H o viola restricción de seguridad | No substituible dentro de F*/H/C0 definidos | Afirmar imposibilidad universal |
| FSTAR-06 | Evaluador conoce O/V o Z | Clasificación inválida por falta de cegamiento | Usar resultados para definir F* o alternativas |
| CMP-15 | D1 justificado por fuente independiente .25/.20 | D1 puede considerarse un comparador secundario incremental legítimo; no desplaza la precedencia D2 de DEC-C10-066 | Aceptar D1 como primario o tratar .25/.20 como realidad sin fuente |
| CMP-16 | D1 sin justificación externa | D1 permanece no validado como comparador ordinario | Tratar .25/.20 como realidad del dominio |
| CMP-17 | D2 con ausencia de provisión focal de fondo verificada | Satisface un requisito de legitimidad del comparador D2 primario candidato; no equivale a validar parámetros ni identificación | Asumir ausencia por diseño sin verificar fondo |
| CMP-18 | D1/D2 con diferentes first stages/compliers | Reporte y dictamen separados | Agrupar o transportar LATE |

Estos contratos son especificaciones documentales; no se han generado fixtures ni ejecutado pruebas. Para cerrar AUD-003 deben añadirse entradas, salidas, verdad oculta, versiones, tolerancias, oráculos y revisión independiente.


## 33. Contratos del Bloque 3 — snapshots estructurales, ΔT_acc y evidencia

| ID | Fixture/verdad DGP | Aserción del analizador | Fallo que debe detectar |
|---|---|---|---|
| SNAP-01 | Cobertura aumenta; sistema inalterado | ΔE_T≠0 y ΔT_acc*=0 | Fechar como creación una ruta preexistente |
| SNAP-02 | Fuente desaparece; sistema inalterado | ΔE_T≠0; truth ΔT_acc*=0; observación puede ser ? | Inferir pérdida de acceso por pérdida documental |
| SNAP-03 | Se añade relación necesaria para τ2 | ΔR* registra alta y A_f* se recalcula | No registrar cambio relacional |
| SNAP-04 | Se elimina dependencia necesaria | ΔR*/ΔC* registra baja; A_f* puede pasar 1→0 | Mantener accesibilidad sin ruta |
| SNAP-05 | Cambia hash, semántica/ID estable | Conserva ID si corresponde y audita integridad/compatibilidad | Crear nueva identidad por hash solamente |
| SNAP-06 | Cambia semántica de transformación | Registra baja/alta de identidad | Tratar cambio semántico como versión menor |
| SNAP-07 | Mapping entre versiones incierto | Match=?; diff indeterminado | Forzar equivalencia |
| SNAP-08 | Cambios no focales sin cambio de τ2 | ΔT_acc*≠0; D_f*=0 | Colapsar diff completo a indicador focal |
| SNAP-09 | Apertura de τ2 sin otros cambios | D_f*=1; diff contiene cambio focal | No detectar apertura |
| SNAP-10 | Cambia Outcome/Value, estructura constante | ΔT_acc*=0 por ese hecho | Definir acceso mediante valoración |
| SNAP-11 | Truth cambia, evidencia no detecta cambio | Analizador produce ?/error; truth no se filtra | Filtrar variable generadora |
| SNAP-12 | Evidencia post descubre ruta basal | Adjudica baseline; no fecha alta en t1 sin evidencia temporal | Confundir descubrimiento con creación |
| SNAP-13 | Frontera/G no comparable | Rechaza diff o exige mapping M explícito | Comparar snapshots incompatibles |
| SNAP-14 | B cambia autorización/recursos | ΔC* refleja cambio y se declara vía colateral | Ocultar cointervención |
| SNAP-15 | App_f cambia, accesibilidad estable | ΔT_acc*=0 si no cambió espacio accesible | Confundir aplicabilidad con accesibilidad |

Estos contratos son especificaciones documentales. No se han creado fixtures ejecutables ni se han ejecutado pruebas. El cierre requiere entradas/salidas, truth oculta, mapping versionado, oráculos, tolerancias, cegamiento y revisión independiente.


## 34. Contratos del Bloque 3 — identidad, versiones y matching

| ID | Fixture/verdad DGP | Aserción exigida | Fallo que debe detectar |
|---|---|---|---|
| ID-01 | TID igual; hash/commit cambia | TID se conserva provisionalmente; nueva provenance/versión | Nueva identidad por hash |
| ID-02 | Mismo nombre; operación nuclear distinta | TID distinta o unresolved | Match por nombre |
| ID-03 | IDs distintos; contrato equivalente | Candidato requiere adjudicación, no fusión automática | Auto-merge por similitud |
| ID-04 | Cambia precondición esencial | Nueva TID o unresolved según contrato | Continuidad sin evaluación |
| ID-05 | Plataforma cambia; contrato estable | RID/SID cambia; TID puede continuar | Confundir implementación con semántica |
| ID-06 | Macrotransformación se divide | SPLIT con mapping y G explícitos | Equivalencia 1:1 ficticia |
| ID-07 | Transformaciones se fusionan | MERGE; preservar identidades históricas | Fusionar IDs retroactivamente |
| ID-08 | Cobertura basal incompleta | UNKNOWN; no ADD ni NO_MATCH | Ausencia inferida por falta de registro |
| ID-09 | Frontera cambia | DIFF_NOT_COMPARABLE o mapping validado | Comparar fronteras distintas |
| ID-10 | Granularidad cambia | Mapping explícito a G común | Conteos no comparables |
| ID-11 | Recurso/condición cambia, TID estable | MODIFY_STRUCTURAL y reevaluar A_f* | Nueva TID automática |
| ID-12 | Solo cambia E_T | ΔE_T, sin evento estructural | Cambio epistémico como ADD/REMOVE |
| ID-13 | τ2 no corresponde entre tiempos | D_f* no calculable como misma identidad | Apertura falsa de focal |
| ID-14 | Mapping 1:N no validado | MATCH_UNRESOLVED | Sumar/colapsar sin contrato |
| ID-15 | Riesgo/calidad cambian, propósito estable | TID puede continuar; no inferir equivalencia causal | Confundir semántica y equivalencia de política/valor |

Contratos documentales. No hay fixtures ejecutables, oráculos implementados ni pruebas ejecutadas.


## 35. Contratos adversariales de Reach y trayectorias

| ID | Fixture / verdad DGP | Aserción exigida | Fallo que debe detectar |
|---|---|---|---|
| REACH-01 | Ruta completa confirmada | Reach=1 | No reconocer ruta válida |
| REACH-02 | Ruta potencial con predicado ? | Reach=? | Convertir desconocido en 0/1 |
| REACH-03 | Catálogo incompleto y sin ruta confirmada | Reach=? | Falso negativo por cobertura |
| REACH-04 | Todas las rutas refutadas, universo exhaustivo | Reach=0 | Falso positivo |
| REACH-05 | Accesible pero no aplicable desde S0 | No alcanza por esa ruta | Confundir T_acc y App |
| REACH-06 | Ruta válida no seleccionada | Reach=1 | Usar selección como filtro |
| REACH-07 | Ruta válida no ejecutada | Reach=1 | Usar ejecución como prueba necesaria |
| REACH-08 | Ejecución sin baseline | No inferir accesibilidad basal | Sesgo retrospectivo |
| REACH-09 | Paso necesario 0 y otro ? | Ruta=0 | Propagación incorrecta |
| REACH-10 | Recurso necesario ? | Ruta=? | Ignorar recursos |
| REACH-11 | Dos rutas; una confirmada | Reach=1 | Exigir todas las rutas confirmadas |
| REACH-12 | Búsqueda truncada | No declarar Reach=0 | Truncamiento confundido con imposibilidad |
| REACH-13 | Descubrimiento post de ruta basal | ΔE_T, no ADD estructural | Fecha de creación falsa |
| REACH-14 | Cambio RID/SID sin compatibilidad probada | Ruta=? | Continuidad asumida |
| REACH-15 | Mapping 1:N no validado | ?/NOT_COMPARABLE | Composición inventada |
| REACH-16 | Ciclo sin terminación | Enumeración incompleta | No alcanzabilidad falsa |
| REACH-17 | Recurso compartido incompatible | Rutas no simultáneamente factibles | Doble asignación |
| REACH-18 | Outcome/Value favorable | Reach inalterado | Circularidad |
| REACH-19 | Cambio de TID focal | D_f* no comparable | Falsa continuidad focal |
| REACH-20 | ΔT_acc fuera de rutas a s | Reach(s) puede no cambiar | Igualar espacio y alcanzabilidad |

Contratos documentales; sin fixtures implementados ni pruebas ejecutadas.


## 36. Contratos documentales del inventario finito y cobertura

| ID | Fixture / verdad DGP | Aserción exigida | Fallo que debe detectar |
|---|---|---|---|
| INV-01 | F1 abierta; F2 accesible/aplicable/componible | Reach(SF)=1 solo si se cumple toda la secuencia | Inferir Reach por apertura focal |
| INV-02 | F1 abierta; F2=0 | Ruta focal bloqueada; Reach depende de alternativas | Omitir continuación |
| INV-03 | F1=0; A1→A2=1 | Reach(SF)=1; apertura funcional no exclusiva | Confundir τ2 y función |
| INV-04 | F1→F2=1; A1→A2=? | Reach=1, alternativa sigue indeterminada | Exigir conocer todas las rutas para afirmar existencia |
| INV-05 | No hay ruta confirmada; catálogo alternativo incompleto | Reach=? | Declarar Reach=0 por ausencia de hallazgo |
| INV-06 | Universo, ocho coberturas completos; todas rutas=0 | Reach=0 | No reconocer refutación exhaustiva |
| INV-07 | B altera A1/A2 en R2 | Etiquetar vía colateral/efecto paquete; no asumir exclusión | Interpretación como IV focal exclusiva |
| INV-08 | B intenta provisión; F1 no se abre en R3 | D_f*=0; conservar ITT de asignación | Imputar accesibilidad desde Z/W_attempt |
| INV-09 | H=3 búsqueda termina por límite computacional antes de cubrir H | Reach=? / truncado | Truncamiento como imposibilidad |
| INV-10 | A1→A2 consume recurso compartido no duplicable con otra ruta | No declarar simultaneidad incompatible | Doble asignación de recurso |
| INV-11 | Snapshot cambia dentro de H | Evaluar por tramos con snapshots inmutables | Sobrescritura temporal |
| INV-12 | F* se evalúa sin O/V y con adjudicación ciega | GOAL_F independiente de Outcome/Value | Circularidad |
| INV-13 | R0 sin A1/A2, cobertura funcional incompleta | Alternativa=?; no pertenencia confirmada a P*_F | Ausencia inferida por no encontrar |
| INV-14 | Identidad/mapping de τ2=? | D_f* no comparable/indeterminado | Apertura focal espuria |
| INV-15 | Cambia solo evidencia de una ruta basal | ΔE_T, no ADD estructural | Descubrimiento como transformación nueva |

Estos contratos son documentales. No se han creado fixtures ejecutables ni se han ejecutado pruebas. Requieren oráculos, entradas/salidas, cobertura, truth oculta y revisión independiente.


## 37. Contratos documentales de integración temporal

| ID | Caso | Aserción exigida |
|---|---|---|
| TEMP-01 | H=3, ruta de 2 transformaciones | No añadir paso ficticio; longitud y duración separadas |
| TEMP-02 | Reach calculado en t4 | No usar selección/ejecución/Outcome/Value |
| TEMP-03 | Paso τ_k accesible pero App(τ_k,s)=0 | Ruta no admisible |
| TEMP-04 | Todos los pasos accesibles, relación=0 | Ruta no admisible |
| TEMP-05 | Snapshot de rama cambia | Nuevo snapshot hipotético inmutable; no sobrescribir t3 |
| TEMP-06 | Sin regla de actualización dinámica | No inventar cambios de estado |
| TEMP-07 | R2/S4R-C, B cambia alternativa | Marcar vía colateral y no asumir exclusión |
| TEMP-08 | R3/S4R-D, intento fallido | Z/intento no implica C_dep/A_f/D_f |
| TEMP-09 | R0/S4R-A sin cobertura funcional completa | Alternativa=?; no clasificar como exclusiva |

Contratos documentales; no ejecutados.


## 38. Contratos de predicados por paso y rama

| ID | Caso | Aserción requerida |
|---|---|---|
| PM-01 | F1 accesible, F2 inaccesible | Ruta focal=0 |
| PM-02 | F1=1, APP(F2,S2)=? | Ruta=? salvo otro necesario=0 |
| PM-03 | REL(F1,F2)=0 | Ruta focal=0 |
| PM-04 | APP(F2,S2)=0 | Ruta focal=0 |
| PM-05 | Truth estructural=1, cobertura epistémica incompleta | Truth no cambia; Reach_obs puede ser ? |
| PM-06 | Ruta A confirmada, F desconocida | Reach=1 por A confirmada |
| PM-07 | Alternativa no hallada, cobertura incompleta | Alternativa=? |
| PM-08 | Mejora de cobertura descubre ruta preexistente | ΔE_T, no ADD estructural |
| PM-09 | Recursos compartidos no modelados | No asumir no interferencia |
| PM-10 | Ramas F/A contrafactuales | No sumar consumos simultáneos |
| PM-11 | Autorización caduca | Aplicar regla explícita o ? |
| PM-12 | Condición state-dependent | Reevaluar por estado de entrada |
| PM-13 | T_acc cambia sin regla | No inventar transición |
| PM-14 | B modifica alternativa en R2 | Registrar vía colateral |
| PM-15 | Intento con dependencia fallida | No inferir accesibilidad |
| PM-16 | Sin política de reserva | RES=? |
| PM-17 | Outcome/Value filtra adjudicación | No usarlos para Reach |
| PM-18 | Enumeración truncada | No declarar cobertura semántica exhaustiva |

Contratos documentales; no ejecutados.


## 39. Contratos de identidad semántica de fichas transformacionales

| ID | Caso | Aserción requerida |
|---|---|---|
| TC-01 | F1/τ2 | No confundir provisión B/C_dep con A_f*, App, ejecución o resultado |
| TC-02 | F2 sin función definida | No adjudicar accesibilidad/aplicabilidad por su posición en la ruta |
| TC-03 | A1/A2 solo topológicos | No afirmar ruta funcional alternativa ni Sub(π,F*,G,H,C0) |
| TC-04 | SF como estado formal | No usar GOAL_F(SF)=1 por definición como validación empírica de F* |
| TC-05 | Evidencia F1 transferida a F2 | No transferir fuerza probatoria entre identidades distintas sin mapping/evidencia |
| TC-06 | R0 sin cobertura exhaustiva | No afirmar exclusividad funcional |
| TC-07 | R1 con A1→A2 topológica | No afirmar Reach funcional confirmado hasta definir F* y factibilidad |
| TC-08 | F2/A1/A2 reciben semántica no aprobada | Rechazar como cambio de diseño no trazado |

Contratos documentales; no ejecutados.


## 40. Contratos de discriminación del microdominio

| ID | Caso | Aserción requerida |
|---|---|---|
| MD-01 | B provisiona adaptador focal | No ejecuta conversión ni aplica configuración |
| MD-02 | F1 convierte, F2 aplica/valida | Funciones y estados distintos, contratos de salida/entrada compatibles |
| MD-03 | A1 exporta, A2 importa por canal nativo | Mecanismo alternativo no reutiliza el adaptador focal |
| MD-04 | F1 disponible, precondición de S0 no satisfecha | ACC(F1)=1 no implica APP(F1,S0)=1 |
| MD-05 | F1/F2 disponibles, F2 no compatible con destino | Reach focal no se declara 1 |
| MD-06 | A1/A2 satisfacen F* | Ruta alternativa puede mantener Reach(SF)=1 antes/después de B |
| MD-07 | B afecta exportador/importador baseline | Clasificar R2/vía colateral; revisar exclusión |
| MD-08 | Formato o versión cambia semántica | Nuevo SID/TID o mapping explícito; no inferir continuidad por nombre |
| MD-09 | Conversión válida sintácticamente pero pierde propiedad F* | F* no se considera satisfecha |
| MD-10 | F* evaluada con Outcome/Value posterior | Rechazar circularidad/filtración |

Contratos de diseño; no ejecutados.


## 41. Contratos de compatibilidad causal del microdominio

| ID | Caso | Aserción requerida |
|---|---|---|
| MDC-01 | B provisiona adaptador | No ejecuta conversión F1, aplicación F2 ni validación F* |
| MDC-02 | B modifica C_dep | No inferir automáticamente A_f*, D_f* ni ΔT_acc |
| MDC-03 | B cambia permisos/configuración/recursos | Registrar vía colateral; no atribuir ITT exclusivamente a A_f* |
| MDC-04 | F1 definido como habilitar y convertir | Rechazar mezcla; provisión B y conversión F1 separadas |
| MDC-05 | A1/A2 comparten dependencia focal | No afirmar independencia funcional ni exclusión focal sin análisis |
| MDC-06 | B no afecta A1/A2 en R0/R1 | Mantener Reach alternativo; permitir ΔT_acc sin cambio Reach |
| MDC-07 | B afecta A1/A2 en R2 | Clasificar como vía colateral/efecto de paquete |
| MDC-08 | Primer estadio C_dep positivo | No inferir first stage A_f*/D_f*/ΔT_acc |
| MDC-09 | F* evaluada por oráculo común | Compartición de medición admisible si no genera/ejecuta la ruta y es ciego |
| MDC-10 | Se elige Opción A | No inferir elección D1/D2 ni identificación de θ_A(q) |

Contratos documentales; no ejecutados.


## 42. Contratos de provisión y dependencias PROV-01…12

| ID | Escenario | Aserción esperada |
|---|---|---|
| PROV-01 | Provisionar adaptador | B no ejecuta F1/F2/A1/A2 |
| PROV-02 | Cambios en artefactos | B no modifica F*, dataset ni oráculo |
| PROV-03 | Snapshots | PreB/postB/rollback cubren host, datos, permisos, red y componentes |
| PROV-04 | Dependencias | Nodos, aristas transitivas y consumidores inventariados |
| PROV-05 | Recursos | B no reduce recursos A1/A2/F2 en R0/R1 |
| PROV-06 | Permisos | ACL mínima; C_auth funcional no cambia |
| PROV-07 | Estado | Fuente/destino no alterados por B |
| PROV-08 | Ruta alternativa | A1/A2 conservan F* pre/post B dentro de margen justificado |
| PROV-09 | Dependencia compartida | B no modifica librerías/APIs/servicios críticos comunes |
| PROV-10 | Rollback | No quedan residuos funcionales relevantes |
| PROV-11 | Cobertura | Nodo/arista desconocido mantiene estado indeterminado |
| PROV-12 | Primera etapa | C_dep no se interpreta como A_f* sin predicados restantes |

Contratos documentales; no implementados ni ejecutados. El detalle de evidencias y estados está en el manifiesto B.


## 43. Contratos de cobertura de grafo GC-01…GC-12

| ID | Escenario | Aserción esperada |
|---|---|---|
| GC-01 | Nodo sin inventario | Estado ?; no inferir ausencia |
| GC-02 | Arista sin evidencia | Estado ? y cobertura NONE/PARTIAL |
| GC-03 | Inventario parcial | No permite Reach=0 ni F_alt,0=0 |
| GC-04 | Ruta con predicado necesario 0 válido | Ruta=0 dentro de universo cubierto |
| GC-05 | Ruta con cualquier predicado necesario ? y ningún 0 | Ruta=? |
| GC-06 | Todos predicados de ruta confirmados 1 | Ruta=1 si orden/identidad temporal también verificados |
| GC-07 | Una ruta confirmada 1 | Reach=1 aunque otras rutas sean ? |
| GC-08 | Todas rutas enumeradas 0 pero Runknown sin cobertura | Reach=? |
| GC-09 | Todas rutas relevantes 0 y cobertura exhaustiva | Reach=0 dentro del universo/horizonte declarado |
| GC-10 | Ruta alternativa satisface F* | F_alt=1 |
| GC-11 | No se encuentra alternativa, cobertura incompleta | F_alt=? |
| GC-12 | Dependencia externa no observable | Mantener frontera abierta y Reach=? cuando sea necesaria |

Contratos documentales; no implementados ni ejecutados.


## 44. Contratos de plantilla U_G — UGI-01…07

| ID | Escenario | Aserción esperada |
|---|---|---|
| UGI-01 | Nodo no observado | La fila permanece NO INVENTARIADO / ?; no inferir ausencia |
| UGI-02 | Dependencia directa sin fuente | Estado ?; cobertura NONE/PARTIAL |
| UGI-03 | Dependencia transitiva o dinámica no resuelta | Registrar nodo desconocido; no declarar independencia de rutas |
| UGI-04 | Ruta externa/opaca | Mantener EXT_UNKNOWN/Runknown y propagar ? cuando sea relevante |
| UGI-05 | Ruta alternativa sin evidencia F* común | Substituibilidad ?; no declarar F_alt,0=0 |
| UGI-06 | Truth DGP en plantilla | No exponer truth_dgp al analizador; separar clasificación observada |
| UGI-07 | Cobertura COMPLETE | Limitarla al universo operativo declarado/versionado; no reclamar exhaustividad ontológica |

Contratos documentales para revisar la futura instancia de la plantilla; no implementados ni ejecutados. La plantilla no contiene fixtures ni observaciones reales.


## 45. Contratos de revisión del crosswalk U_G — UGC-01…06

| ID | Caso documental | Resultado esperado |
|---|---|---|
| UGC-01 | Cada N01–N23 tiene correspondencia | 23 IDs mapeados; ninguna fila implica existencia técnica. |
| UGC-02 | Aristas mult destino E17–E23 | Una fila por par; conservar parent_edge_id y atomic_edge_id. |
| UGC-03 | E07 | Se registra como regla lógica, no como edge técnico binario. |
| UGC-04 | E22 | No inventar destinos; mantener pendiente definición de eventos/variables de selección y ejecución. |
| UGC-05 | Predicados y rutas | 14 códigos exactos y cinco clases primarias; subtipos separados. |
| UGC-06 | Roles compuestos N16/N23 | Separar criterio F*, oráculo y adjudicación; ejecución, Outcome y Value según identidad/tiempo. |

Contratos de revisión documental. No son tests de software ni se han ejecutado.


## 46. Contratos de revisión del protocolo U_G — UGE-01…08

| ID | Caso documental | Resultado esperado |
|---|---|---|
| UGE-01 | Fuente declarativa sin runtime | No inferir componente cargado/ejecutado |
| UGE-02 | Búsqueda sin hallazgo y cobertura incompleta | observed_state=?; no asignar 0 |
| UGE-03 | Fuentes contradictorias | evidence_status=CONFLICTING y estado ? hasta adjudicación |
| UGE-04 | Dependencia dinámica no observada | Cierre transitivo incompleto; independencia=? |
| UGE-05 | Ruta externa/opaca relevante | Mantener Rexternal/Runknown y propagar ? |
| UGE-06 | Declaración de ausencia | Exigir universo, método de detección, integridad, cobertura negativa y revisión |
| UGE-07 | COMPLETE sin denominador | Rechazar COMPLETE; exigir scope, universo, fuentes y excepciones |
| UGE-08 | Desacuerdo 1 vs 0 | Tercer adjudicador; conservar opiniones y, si no se resuelve, ? |

Contratos documentales de revisión; no implementados ni ejecutados.


## 47. Contratos de revisión del esquema normalizado — FCM-01…09

| ID | Caso de revisión | Resultado esperado |
|---|---|---|
| FCM-01 | evidence_ref huérfano | Rechazar registro sin cadena claim-evidence-evidence válida |
| FCM-02 | evidencia de otra unidad/versión/tiempo | No aceptar como soporte sin justificación de transportabilidad |
| FCM-03 | COMPLETE sin denominador | Rechazar estado COMPLETE |
| FCM-04 | E1/E2 comparten clasificación antes de registrar | Detectar pérdida de independencia; conservar evaluaciones separadas |
| FCM-05 | Desacuerdo 1 vs 0 | Requerir adjudicador y preservar opinión minoritaria |
| FCM-06 | truth DGP accesible al analizador | Rechazar paquete; truth segregada fuera de superficie analítica |
| FCM-07 | route_subtype usado como clase U_G | Rechazar; exigir parent_route_class |
| FCM-08 | Tabla de objeto sin campos comunes | Rechazar instancia incompleta |
| FCM-09 | Revisión sobrescribe versión previa | Rechazar; exigir supersedes_record_id y conservar historial |

Contratos documentales de revisión. No son validadores implementados ni pruebas ejecutadas.


## 48. Contratos de revisión de consistencia del esquema — FCM-10…16

| ID | Caso | Resultado esperado |
|---|---|---|
| FCM-10 | Tabla de objeto sin campos comunes | Rechazar |
| FCM-11 | SNAPSHOT usa ? cuando observed_state no aplica | Exigir NA justificado; no inferir ausencia |
| FCM-12 | E1/E2 en una sola celda | Rechazar; una fila por evaluación |
| FCM-13 | Evidence refs serializados como lista en celda | Exigir CLAIM_EVIDENCE_LINK 1:N |
| FCM-14 | COMPLETE en vista resumen sin denominator | Rechazar; resolver COVERAGE_REGISTER |
| FCM-15 | Estado fuera de dominio o timestamp sin offset | Rechazar |
| FCM-16 | claim_target_id no resuelve a object_record_id | Rechazar referencia huérfana |

Contratos documentales, no validador implementado ni pruebas ejecutadas.


## 49. Contratos de revisión de referencias relacionales — FCM-17…19

| ID | Caso | Resultado esperado |
|---|---|---|
| FCM-17 | Dos evaluadores almacenados en un único registro | Rechazar; una fila y PK evaluator_record_id por evaluación |
| FCM-18 | Evidencia revisada sin vínculo a evaluador/adjudicación | Rechazar o marcar incompleto; exigir CLAIM_EVIDENCE_LINK |
| FCM-19 | Evaluación/adjudicación apunta a ID semántico no versionado | Rechazar; exigir object_record_id existente |

Contratos documentales; no implementados ni ejecutados.


## 50. Controles de revisión independiente del esquema — SR-01…20

Los criterios y evidencia exigible SR-01…20 están especificados en C10_S_UG_SCHEMA_INDEPENDENT_REVIEW_CHECKLIST_DRAFT_001.md. En la fase actual de investigador único, la autoauditoría se registra como AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT y cada control recibe PASS_STATIC/CONDITIONAL/FAIL/NOT_ASSESSED, con versión/hash, fundamento, alcance y acción pendiente. Un revisor identificado y una declaración de independencia solo se exigen cuando se active una revisión externa futura. R1/R2 no son gate inmediato ni bloquean continuidad documental. Los controles críticos no pueden quedar FAIL para aceptar freeze técnico; la apertura web germen as is es un gate separado y no requiere freeze ni revisión por pares global.

Este registro no acredita ejecución ni revisión. No se han designado revisores ni emitido dictamen.


## 51. Revisión de cardinalidad de evidencia — FCM-20

| Caso | Resultado esperado |
|---|---|
| evidence_ref contiene varios IDs serializados | Rechazar; el campo admite 0..1 referencia de navegación |
| CLAIM_EVIDENCE_LINK omite parte de la relación de evidencias | Registrar vínculo faltante; la relación completa es 0..n |
| EVALUATOR_ASSESSMENT usa evaluator_record_ids como PK | Rechazar; PK singular evaluator_record_id por fila |
| Objeto omite evaluator_record_ids de resumen | Permitido si las filas EVALUATOR_ASSESSMENT están enlazadas correctamente |

Contrato documental; no ejecutado.


## 52. Casos de control de obligatoriedad y cardinalidad de evidencia — UG-SR-A01

| ID | Caso | Resultado esperado |
|---|---|---|
| UG-SR-A01-T01 | Objeto con estado 1/0/? sin fila correspondiente en CLAIM_EVIDENCE_LINK | Rechazar o marcar incompleto conforme a la regla que se confirme; no inferir soporte por silencio |
| UG-SR-A01-T02 | Objeto con CLAIM_EVIDENCE_LINK válido y `evidence_ref` vacío | Aceptar si `evidence_ref` se confirma como atajo opcional |
| UG-SR-A01-T03 | `evidence_ref` apunta a vínculo inexistente | Rechazar referencia huérfana |
| UG-SR-A01-T04 | CLAIM_EVIDENCE_LINK apunta a evidence_id inexistente o a object_record_id incompatible | Rechazar FK/alcance |
| UG-SR-A01-T05 | Varios vínculos válidos para un mismo objeto | Aceptar filas múltiples normalizadas; no serializar listas en `evidence_ref` |

Estos contratos documentan la regla UG-SR-A01 aceptada documentalmente el 2026-11-05. No están implementados ni ejecutados. T01 queda definido para los estados observados 1/0; los estados ? y NA se rigen por las condiciones explícitas de la regla.


## 53. Casos ampliados para propuesta UG-SR-A01 — estados y vínculos

| ID | Caso | Resultado esperado propuesto |
|---|---|---|
| UG-SR-A01-T06 | observed_state=1 sin vínculo CLAIM_EVIDENCE_LINK | Rechazar como registro observado sin soporte |
| UG-SR-A01-T07 | observed_state=0 sin vínculo, aunque evidence_ref vacío | Rechazar; además exigir cobertura negativa suficiente |
| UG-SR-A01-T08 | observed_state=? sin vínculo, unknown_reason vacío | Rechazar/incompleto |
| UG-SR-A01-T09 | observed_state=? sin vínculo, unknown_reason presente, evidence_status=MISSING y límites documentados | Aceptar como indeterminado, nunca como 0 |
| UG-SR-A01-T10 | observed_state=NA sin vínculo y con justificación de no aplicabilidad | Aceptar si NA está permitido para esa entidad |
| UG-SR-A01-T11 | observed_state=1/0 con vínculo válido y evidence_ref vacío | Aceptar; evidence_ref es opcional |
| UG-SR-A01-T12 | evidence_ref poblado pero CLAIM_EVIDENCE_LINK inexistente | Rechazar referencia huérfana |

Los resultados son contratos documentales aceptados para UG-SR-A01; no están implementados ni ejecutados. La validación de cardinalidad, FK y comportamiento sigue pendiente.


## 54. Protocolo científico autocontenido y auditable C10-S

La ausencia de revisores externos no bloquea la continuidad del diseño C10-S. Los dictámenes asistidos conservan AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT y la escala PASS_STATIC/CONDITIONAL/FAIL/NOT_ASSESSED. Un revisor identificado solo será exigible si se decide activar una revisión externa; no es requisito para especificar, preanalizar o preparar un experimento falsable.

La suficiencia interna exige que el experimento pueda reconstruirse desde artefactos y registros: DGP y truth versionados; analizador sin acceso a truth; evaluador separado; estimandos y criterios preespecificados; semillas y versiones; salidas brutas; auditoría de integridad; y replay cuando esté autorizado.

La simulación puede probar si el método recupera la verdad causal estipulada y detecta no-identificación dentro del DGP. No constituye por sí sola demostración empírica de la hipótesis general C10 en sistemas reales.


## 55. Reconciliación de estadística, Value y continuidad sin revisión externa (2026-11-05)

Este addendum propaga la arquitectura estadística y de medición de la fuente 165–183. No declara contratos ejecutados ni sustituye la especificación completa del DGP.

### 55.1 P177-01…12 — estimación y evaluación

| ID | Control | Criterio de aceptación |
|---|---|---|
| P177-01 | ITT-A/O/V | Diferencias por asignación correctas y reportadas por resultado |
| P177-02 | Primera etapa | Estimación, error estándar e intervalo correctos para accesibilidad |
| P177-03 | Wald | Cociente correcto; etiqueta LATE solo si los supuestos están defendidos |
| P177-04 | Instrumento débil | Inferencia robusta y dictamen adecuado; no depender solo de aproximación normal |
| P177-05 | O/V | Estimaciones independientes; no inferencia automática entre Outcome y Value |
| P177-06 | Ajuste basal | Ajuste preespecificado; no incorporar mediadores postasignación |
| P177-07 | ATE/ATT | No confundir con ITT ni LATE; no extrapolar automáticamente |
| P177-08 | Heterogeneidad | Ponderación y composición de compliers explícitas |
| P177-09 | Multiplicidad | Jerarquía confirmatoria/exploratoria respetada |
| P177-10 | Recuperación sintética | Sesgo, RMSE y cobertura frente a truth del generador |
| P177-11 | Equivalencia | No significación no se interpreta como equivalencia |
| P177-12 | Dictamen causal | Efecto de política separado de atribución a accesibilidad |

### 55.2 P178-SIM-01…10 — protocolo cuantitativo derivado

Los siguientes controles formalizan el procedimiento de §178 de la fuente; son IDs de organización del registro, no IDs originales de la fuente:

| ID | Control | Criterio de aceptación |
|---|---|---|
| P178-SIM-01 | Potencia separada | Potencia ITT, primera etapa, LATE y clasificación adversarial reportadas por separado |
| P178-SIM-02 | Búsqueda de N | Cuadrícula de N; seleccionar el menor que satisfaga potencia y precisión predefinidas |
| P178-SIM-03 | Clústeres | ICC, efecto de diseño y número de clústeres incluidos si UA es clúster |
| P178-SIM-04 | Réplicas R | R justificado por error Monte Carlo deseado para cobertura, sesgo y clasificación |
| P178-SIM-05 | Error Monte Carlo | SE_MC de métricas y su incertidumbre reportados |
| P178-SIM-06 | Semillas | Jerarquía determinista maestra/escenario/configuración/réplica |
| P178-SIM-07 | Reproducibilidad | Hashes de DGP, analizador, parámetros, reglas y artefactos de salida |
| P178-SIM-08 | Pérdidas | MCAR/MAR/MNAR, censura y selección postasignación por escenario |
| P178-SIM-09 | Métricas | Sesgo, RMSE, cobertura, error tipo I, potencia, convergencia y réplicas inválidas |
| P178-SIM-10 | Parámetros ex ante | MDE, relevancia práctica, equivalencia, δ/ε y tolerancias fijados antes de resultados |

N=2.000 y R=1.000 permanecen como valores históricos ilustrativos, no como parámetros confirmatorios aceptados.

### 55.3 P179-01…08 — valoración de Value

| ID | Control | Criterio de aceptación |
|---|---|---|
| P179-01 | Separación A/O/V | Constructos definidos y medidos independientemente |
| P179-02 | Vector Value | Resultados por dimensión disponibles |
| P179-03 | Independencia de medición | Outcome no se reutiliza como Value sin justificación |
| P179-04 | Contexto de valoración | Observador/beneficiario, contexto y criterio registrados |
| P179-05 | Medición basal | Medidas iniciales diferenciadas y disponibles |
| P179-06 | Efectos discordantes | Deterioros y trade-offs no se ocultan mediante agregación |
| P179-07 | Estimación causal | ITT/LATE por dimensión cuando sean identificables |
| P179-08 | Agregación | Índice solo con ponderaciones y regla justificadas |

Las dimensiones candidatas (eficiencia, calidad, acceso de destinatarios, robustez y sostenibilidad) siguen provisionales; el vector es la opción metodológica recomendada durante identificación.

### 55.4 Relación con P182/P183

P182-01…12 y P183-01…13 ya están registrados en §13. Deben leerse conjuntamente con P177/P178/P179: validez de constructo, error/invariancia, ausencia, censura, selección y cotas se evalúan por estimando y dimensión, no mediante un dictamen global único.

### 55.5 Revisión externa no es gate de continuidad

El punto 8 de §12 («obtener revisión independiente») queda SUPERSEDED como requisito general de conversión a contrato ejecutable y avance científico. Prevalecen el protocolo autocontenido de §54 y el gate científico de la Closure Control Matrix §12: la continuidad se realiza mediante AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT; R1/R2 no son condición de avance. La separación generador/analizador/evaluador es computacional y no equivale a revisión humana externa.

La trazabilidad histórica se conserva; no se simula independencia ni se declara una revisión externa inexistente. La ejecución científica sigue requiriendo autorización expresa separada.

**Estado:** P177/P178/P179 incorporados como contratos de diseño; P182/P183 ya persistidos. Ninguno de estos controles se declara implementado o ejecutado.


## 56. Contrato de aceptación documental de políticas materiales D2 — DEC-C10-067

| ID | Condición de aceptación | Evidencia exigida | Fallo que debe detectar |
|---|---|---|---|
| D2POL-01 | Control D2 no programa ni inicia intento focal por la política asignada | Política/versionado y registro temporal | Tratar el control como provisión ordinaria D1 o inferir ausencia efectiva sin medir fondo |
| D2POL-02 | Tratamiento D2 programa provisión focal estandarizada | Protocolo, actor, artefacto y versión | Confundir programación con intento efectivo o éxito |
| D2POL-03 | Asignación, W_programmed, W_attempt efectivo, recepción y éxito son variables separadas | Registro por unidad y tiempos | Sustituir ITT por recepción/cumplimiento |
| D2POL-04 | Componentes técnicos se verifican separadamente | Evidencia de instalación, integridad, compatibilidad y operatividad | Inferir (C_{dep}^{*}) desde intento o instalación declarada |
| D2POL-05 | (C_{dep}^{*}), (A_f^{*}) y (D_f^{*}) se determinan por separado | Predicados completos y snapshots basal/post | Transferir la primera etapa técnica automáticamente a accesibilidad/apertura |
| D2POL-06 | (C_{auth,base}=1) y condiciones no focales comunes en DGP aislado | Contrato de elegibilidad y auditoría de invariantes | Introducir cambio de autorización o recursos no declarado |
| D2POL-07 | Vías colaterales de provisión quedan registradas | Manifiesto de cambios y grafo de dependencias | Etiquetar ITT de paquete como efecto puro de accesibilidad |
| D2POL-08 | Ausencia de provisión focal de fondo en control D2 se verifica, no se presupone | Inventario/cobertura y evidencia independiente | Declarar control limpio por el mero hecho de no programar intento |
| D2POL-09 | (s=0.80) se mantiene como hipótesis no validada | Configuración del DGP y análisis de sensibilidad futuro | Presentar el parámetro candidato como dato empírico o aprobado |
| D2POL-10 | Provisión no ejecuta F1/F2/A1/A2 | Separación de eventos/protocolos | Mezclar provisión técnica con ejecución transformacional |

**Estado:** contrato documental aceptado; evidencias, implementación y ejecución permanecen pendientes. No implica aprobación del DGP ni autorización científica.



---

## 57. Subcasos agregados trivalentes de medición — crosswalk MEAS / ID / SNAP / U_G

**Estado:** contratos documentales suplementarios; no implementados ni ejecutados.  
**Fuente de reglas:** auditoría focal §10 y crosswalk adversarial §11.  
**Precedencia:** estos subcasos concretan la aplicación agregada de los contratos MEAS-01…24; no los sustituyen, no duplican los catálogos ID-01…15/SNAP-01…15 y no modifican contratos o decisiones aceptados.

| Subcaso | Contrato padre existente | Criterio de aceptación suplementario |
|---|---|---|
| TRI-AF-01 | MEAS-03 / MEAS-08 | Todos los predicados constitutivos 1 y comparabilidad/cobertura adecuadas producen A_f^{obs}=1; no aceptar subconjuntos |
| TRI-AF-02 | MEAS-01 / MEAS-23 | Un predicado necesario 0 válido/suficiente produce A_f^{obs}=0 aunque otro término sea ?; conservar unknown |
| TRI-AF-03 | MEAS-08 / MEAS-23 | Sin cero suficiente y con un término ? producir A_f^{obs}=? |
| TRI-AF-04 | MEAS-23 | Conflicto local se conserva; un cero independiente válido puede producir A_f^{obs}=0; no mayoría automática |
| TRI-AF-05 | MEAS-15 / ID-09/10/13/14 | Incompatibilidad global de identidad/frontera/G/mapping impide agregar; A_f^{obs}=? |
| TRI-DEP-01 | MEAS-02 / GC-06/07 / DGP §32 | Una ruta admisible 1 junto a Runknown=? produce DEP_f^{obs}=1 sin declarar exhaustividad |
| TRI-DEP-02 | MEAS-21 / GC-06/07 / U_G §6 | DEP_f^{obs}=0 solo si todas las rutas del universo declarado están refutadas y coverage COMPLETE, con Runknown resuelto |
| TRI-DEP-03 | MEAS-21 / GC-06/07 | Rutas conocidas 0 con Runknown o cobertura PARTIAL mantienen DEP_f^{obs}=? |
| TRI-DEP-04 | MEAS-02 / ACC-11 | C_dep=0 y alternativa equivalente válida 1 producen DEP_f^{obs}=1 |
| TRI-DEP-05 | MEAS-02 / MEAS-20 / PROV | Bloqueo de una ruta no refuta rutas alternativas; evaluar bloqueo al nivel de la transformación/universo |
| TRI-DF-01 | MEAS-09 | Tabla de nueve combinaciones basal/post; solo (0,1) produce D_f^{obs}=1 |
| TRI-DF-02 | MEAS-09 / MEAS-10 | Baseline=? y post=0, con comparación válida, produce D_f^{obs}=0 |
| TRI-DF-03 | MEAS-09 | Baseline=1 produce D_f^{obs}=0 para post 0, 1 o ? |
| TRI-DF-04 | MEAS-09 / MEAS-10 | Baseline=? y post=1 produce D_f^{obs}=? |
| TRI-DF-05 | MEAS-15 / ID-13 / SNAP-07/13 | No comparabilidad global produce ?/NOT_COMPARABLE, con precedencia sobre estados locales |
| TRI-DF-06 | MEAS-24 / SNAP-12 | Descubrimiento post de una ruta preexistente obliga a revisar baseline; no fechar ADD en post sin evidencia temporal |
| TRI-OBS-01 | MEAS-08 / MEAS-23 | MISSING/NONE/PARTIAL/no logs sin refutación suficiente producen ?, nunca 0 |
| TRI-OBS-02 | MEAS-06/07/22 | Truth/Z/B/Outcome/Value no permitidos en el analizador provocan FAIL de separación/cegamiento |
| TRI-OBS-03 | MEAS-12/13 / P183 | Error y missingness se informan por brazo×tiempo×versión×ruta×cobertura; no aplicar corrección puntual sin identificación |

La materialización futura seguirá el contrato común de §2: test_id, fixture_id/hash, entradas por rol, hidden_truth segregada, expected_output, assertions, failure_codes y artefactos. Los subcasos no tienen fixtures serializados, oráculos implementados, tolerancias calibradas ni hashes de ejecución. Sus resultados futuros serán PASS/FAIL/INDETERMINATE; no ejecutar hasta autorización aplicable.

**Dictamen:** registro de pruebas ampliado documentalmente. MEAS-G8 sigue OPEN; MEAS-G4/G6/G7 permanecen abiertos o parciales según los contratos fuente. No se autoriza implementación, validación ejecutable, simulación ni experimento.



## 58. Contratos de discriminación de validez IV (derivados de C10-S-IV-AUD-001)

Se amplía el catálogo de aceptación para que el analizador no convierta un cociente Wald computable en un LATE interpretado cuando la verdad DGP viola supuestos. Estos contratos son propuestas; no hay fixtures serializados ni pruebas ejecutadas.

| Familia | Escenario mínimo | Salida esperada del analizador |
|---|---|---|
| IV-REL | Primera etapa nula, débil y fuerte, por separado para `C_dep^*`, `A_f,post^*`, `D_f^*`, `ΔT_acc^*` | Distinguir no relevancia/instrumento débil de relevancia focal; no sustituir un constructo por otro |
| IV-EXC | Exclusión satisfecha y violada por cada familia de vías colaterales B-M01…15 | `LATE_f` solo bajo condición satisfecha; efecto de política/paquete o no identificación si se viola |
| IV-MON | Monotonicidad satisfecha y violada con defiers/crowding-out | Abstenerse de declarar LATE estándar cuando hay defiers |
| IV-CROSS | Provisión focal de fondo/crossover en controles y versiones múltiples | Clasificar exposición y consistencia; no inferir tipo individual desde observación incompleta |
| IV-INT | Interferencia, recursos/dependencias compartidos y carryover | Rechazar IV individual estándar o exigir régimen de exposición/clúster definido |
| IV-MEAS | Error diferencial de `D_f^{obs}`, Outcome y Value; missingness/censura por brazo | Separar truth/observación; producir sensibilidad/cotas o no identificación |
| IV-OUT | LATE para Outcome frente a LATE para Value con reglas/horizontes distintos | No transportar identificación de un resultado al otro |

Cada fixture deberá usar el contrato común de §§1–2: `hidden_truth` accesible solo al generador/evaluador, nunca al analizador; entradas/roles separados; expected_output y assertions fijados antes de ejecutar; hash reproducible. La especificación de parámetros, tolerancias, potencia y serialización queda abierta. No se autoriza implementación ni ejecución.



## 59. Crosswalk de contratos trivalentes con gates IV

Los contratos de §§57–58 se reutilizan para IV-G1/G4/G6; no se crean fixtures duplicados ni se asigna PASS sin ejecución autorizada y evidencia.

| Familia existente | Gate IV soportado | Afirmación que puede comprobar | Lo que no demuestra por sí sola |
|---|---|---|---|
| TRI-AF-01…05 | IV-G1, IV-G6 | Agregación trivalente de predicados focales, conflicto, comparabilidad y unknown | Elegibilidad verdadera sin error ni identificación IV |
| TRI-DEP-01…05 | IV-G1, IV-G4 | Disyunción de rutas, alternativas, cobertura completa y Runknown | Exclusión causal ni ausencia real de vías colaterales |
| TRI-DF-01…06 | IV-G1, IV-G6 | Comparación basal/post de la misma τ2 y derivación observada de apertura | Que D_f_obs=D_f* en datos reales |
| TRI-OBS-01…03 | IV-G6 | Separación de estado, evidencia, cobertura y truth; abstención ante conflicto/falta de cobertura | Cegamiento operativo, fiabilidad real ni error diferencial identificado |
| IV-REL/EXC/MON/CROSS/INT/MEAS/OUT (§58) | IV-G2…G8 | Abstención correcta bajo escenarios DGP conocidos, débiles o violados | Validez de supuestos en un sistema real fuera de DGP |

La suite debe probar conjuntamente las dependencias, manteniendo hidden_truth inaccesible al analizador. La cobertura de un contrato no implica cierre de los demás. No hay fixtures serializados, oráculos ejecutables ni resultados de pruebas.



## 60. Contratos adversariales de exclusión por superficies B-M01…15

Los contratos deben separar las quince superficies, aunque algunos escenarios puedan combinarse. La salida del analizador se compara con hidden_truth solo por el evaluador independiente.

| Familia | Manipulación/escenario DGP | Resultado que el analizador debe distinguir |
|---|---|---|
| EXC-F0 | B solo modifica componente focal necesario y capturado por D_f*; no altera otras rutas, Outcome/Value ni medición | LATE_f potencialmente identificable solo si IV-G1…G8 y demás supuestos se satisfacen |
| EXC-B01…04/08/09 | Función extra, runtime/host, interfaz, red o seguridad altera otra ruta, permiso, riesgo, coste o resultado | No atribuir automáticamente a D_f*; clasificar paquete/no identificación según vía y estimando |
| EXC-B05 | C_auth,base diferencial frente a ACL técnica de provisión | Violación del aislamiento de autorización; no LATE_f focal sin estrategia adicional |
| EXC-B06 | Datos/estado/App/F* cambian con B fuera de D_f* | Vía directa a ejecución/Outcome; no exclusión focal |
| EXC-B07 | B consume/desplaza recursos o capacidad de rutas alternativas; pool compartido | Efecto de paquete y/o interferencia; no IV individual estándar |
| EXC-B10 | Formación/avisos cambian K o observabilidad/missingness por brazo | Vía mediadora/colateral o error diferencial; no ajustar mecánicamente por K postratamiento |
| EXC-B11 | Caché/índice/estado residual sobrevive a B o rollback | Inconsistencia, carryover o spillover; abstenerse de Wald estándar |
| EXC-B12 | Latencia/throughput/calidad/coste cambian fuera de τ2 | Vía directa a Outcome/Value o interferencia |
| EXC-B13 | Oráculo/dataset/regla de Outcome cambia | Resultado no comparable; invalidar interpretación causal común |
| EXC-B14 | A1/A2 se habilita, degrada o elimina | Vía directa por alternativa a Reach/Exec/Outcome; exclusión focal violada |
| EXC-B15 | Rollback incompleto/residuos entre unidades o periodos | Carryover/interferencia y consistencia comprometida |

No se serializan fixtures ni se ejecuta esta suite en esta operación. Los escenarios no asignan tasas ni parámetros. La cobertura de una familia no prueba invariancia de las restantes.

## 61. Contratos de escenario DGP Opción A para discriminación causal

Estos contratos concretan §60 y C10-S-IV-AUD-001 §12. No duplican EXC-B01…15 ni sustituyen IV-REL/EXC/MON/CROSS/INT/MEAS/OUT de §58. Cada fixture futuro tendrá un contraste principal aislado, con controles invariantes explícitos y hidden_truth inaccesible al analizador.

| ID | Escenario base | Manipulación única principal | Invariantes/control | Expected output mínimo |
|---|---|---|---|---|
| DGP-EXC-01 / R0 | Opción A, F1=τ2 focal | B abre F1 y solo F1; no cambia F2, A1/A2, datos, F*, recursos, K, coste/riesgo ni medición | Asignación, monotonicidad, consistencia, no interferencia y medición se prueban en fixtures separados | LATE_f solo candidato condicional; ITT_O e ITT_V separados |
| DGP-EXC-02 / R1 | A1→A2 factible antes de Z | Ninguna; alternativa basal estable | B no altera A1/A2 ni sus recursos | No marcar exclusión violada por alternativa basal; Reach puede permanecer constante; permitir efecto nulo/heterogéneo |
| DGP-EXC-03 / R2 | A1→A2 basal presente | B altera una propiedad funcional de A1/A2 | Mantener demás superficies invariantes | Efecto de paquete/vía colateral; no LATE_f focal |
| DGP-EXC-04 / R3 | Adaptador focal candidato | W_attempt sin C_dep* ni D_f* | Separar subcasos sin y con consumo/residuo | Primera etapa focal nula/débil; si hay coste/residuo, efecto de paquete adicional |
| DGP-EXC-05 | R0 | B cambia S0/datos/mapping/App/F* con D_f* fijo | Outcome oracle invariante | Exclusión violada por vía directa a O; no LATE_f |
| DGP-EXC-06 | R0 | B cambia coste/riesgo/recursos que entran en V*, manteniendo O* constante | Medición y regla V invariantes | Vía directa B→V; ITT_V de política posible, LATE_f no |
| DGP-EXC-07 | R0 | B cambia K mediante mensajes/formación y con ello selección/ejecución | Observabilidad constante para aislar conocimiento | Vía no focal a O/V; no ajustar mecánicamente por K post-Z |
| DGP-EXC-08a | R0 | B cambia logs/cobertura/missingness, no estado O*/V* | Truth fija; oráculo semántico invariante | No atribuir diferencia observada a efecto verdadero; IV-G6/medición no cerrado |
| DGP-EXC-08b | R0 | B cambia oráculo/F*/regla/dataset de Outcome | No cambiar mecanismo de estado subyacente | Resultado no comparable; invalidar interpretación causal común |
| DGP-EXC-09 | R0 | B consume recurso compartido o deja residuo entre unidades/periodos | Declarar exposición, UA/UE/clúster y reloj | Interferencia/carryover; rechazar Wald individual estándar sin modelo de exposición |

**Regla de aislamiento:** si un escenario combina varias manipulaciones, debe descomponerse en fixtures separados más un escenario compuesto de estrés. El escenario compuesto no sustituye los controles de una sola vía. Los expected outputs son estados cualitativos, no estimaciones numéricas ni garantías de identificación fuera del DGP.

**Estado:** contratos documentales; no hay fixtures serializados, parámetros, distribuciones, tolerancias, potencia, oráculos ni pruebas ejecutadas. No se autoriza implementación o ejecución.



## 62. Contratos de captura temporal y segregación de roles para DGP-EXC-01…09

Estos contratos concretan §§58–61 y DGP §28. Cada fixture futuro deberá capturar al menos:

- unit_id, cluster_id/pool_id cuando proceda, scenario_id, assignment_id, timepoint, event_timestamp, object_id, semantic_version, implementation_version, snapshot_hash y provenance_ref;
- variable_id, causal_role, truth_value en almacén restringido, observed_value, evidence_status, coverage_status, missingness_reason, evaluator_id y adjudication_status;
- inputs_by_role, hidden_truth_ref, expected_output, assertions, failure_codes, evidence_artifacts y reproducibility_hash según el contrato común vigente.

El esquema es una propuesta de crosswalk, no un schema implementado. Los campos de truth/potenciales/mecanismos se segregan físicamente o mediante control de acceso efectivo: el analizador no debe poder leerlos por API, logs, metadatos, nombres de fixture ni orden de ejecución. El evaluador independiente accede solo después de congelar la salida analítica.

Cada familia requiere por lo menos un control negativo que compruebe los invariantes del contraste, y el escenario de estrés compuesto no sustituye escenarios de una sola vía. Para interferencia/carryover, fixture incluye mapa de exposición y snapshots longitudinales; no usar una sola fila individual como sustituto.

**Estado:** contrato documental; no schema, fixtures, control de acceso, oráculos ni pruebas implementados. No se autoriza ejecución.



## 63. Contratos de discriminación funcional de Opción A — extensión documental

La futura suite debe distinguir sin colapsar: (a) adaptador no provisionado/provisión fallida; (b) adaptador provisionado con C_dep* positivo pero A_f*(τ2)=0 o ?; (c) A_f* positiva con F1 no aplicable o no ejecutada; (d) F1 PASS local con F2 inaccesible/fallida; (e) F1→F2 con F*=0/? pese a éxito local; (f) A1/A2 alternativa funcional estable (R1); (g) A1/A2 alterada por B (R2); (h) ambas rutas alcanzan destino nominal pero no satisfacen el mismo F*; (i) ruta conforme funcionalmente con FP-08 probatorio insuficiente.

Cada caso futuro debe fijar identidad/versiones, C_src/C_dst/M, IAM, C0/G/H, recursos/permisos, snapshots y oráculo; mantener hidden_truth segregada del analizador; registrar cobertura y estados 1/0/?; y declarar qué dimensión FP falla sin doble conteo. Los casos simples de una sola diferencia no serán sustituidos por un escenario compuesto.

Estos son contratos lógicos de discriminación, no IDs de fixture ni fixtures serializados. No se alteran MEAS/TRI existentes ni se afirma que las pruebas estén implementadas. La correspondencia final con MEAS, PROV, ID, SNAP y FP debe cerrarse antes de materialización.


## 64. Contratos de discriminación del mapping y estado aplicado

La suite futura debe distinguir: (a) correspondencia CMP/PAR inequívoca vs ambigua; (b) pérdida obligatoria vs falta de evidencia; (c) ABSENT vs NULL; (d) DEFAULT declarado vs heredado; (e) default resuelto por entorno en E_dst vs estado del paquete; (f) REF vacío con cobertura completa vs inventario incompleto; (g) REF externo vs dependencia instalada; (h) AST preservado vs estructuralmente válido pero semánticamente alterado; (i) artefacto intermedio F1/A1 conforme vs C_dst aplicado divergente; (j) estado aplicado correcto con FP-08 insuficiente; (k) alternativa A1/A2 alterada por B; (l) UNKNOWN/conflicto RUL vs NA legítimo.

Cada caso fijará C_src/C_dst, M, IAM, versiones, C0/G/H, cobertura, snapshot E_dst, oráculo y rol de cada dato. Declarará predicado FP primario, evitará doble conteo y mantendrá hidden_truth fuera del analizador. Son contratos lógicos, no fixtures ni pruebas ejecutadas.


## 65. Contratos de discriminación DEFAULT

La suite debe separar: (1) DEFAULT declarado frente a heredado; (2) mismo valor resuelto con distinto origen contractual; (3) regla/ámbito de herencia distinto; (4) ENV_RESOLVED observado en E_dst frente a no observado; (5) valor ambiental distinto con contrato idéntico; (6) fuente incapaz de distinguir DECLARED/INHERITED; (7) valor resuelto no atribuible a versión/instancia; (8) ausencia real de default acreditada frente a snapshot/evidencia ausente.

Cada caso separará hidden_truth, entrada del analizador, PAR contractual, mapping M y snapshot E_dst; declarará FP primario y resultado esperado 1/0/?. Son contratos lógicos, no fixtures ni pruebas ejecutadas.

## 66. Contratos de discriminación del roster PAR candidato

La futura suite deberá discriminar, sin asumir resultados: (1) BOOL preservado frente a inversión true/false; (2) ENUM con mapping total frente a símbolo obligatorio sin mapping; (3) fusión many-to-one de símbolos funcionalmente distintos; (4) INT dentro del dominio frente a overflow/truncamiento/signo alterado; (5) OPTIONAL ABSENT preservado frente a default introducido; (6) DEFAULT declarado frente a heredado y resolución ambiental separada; (7) NULL introducido en clave no nullable; (8) slot RETRY-COUNT que pertenece a P0 frente a recurso/capacidad P1 indebidamente incorporado; (9) STRING descriptivo en MET frente a STRING funcional contractual; (10) PAR tipo REF duplicando indebidamente una relación REF.

Cada contrato fijará fuente/versión, owner CMP, tipo, dominio, requiredness, estados, default, mapping M, IAM, C_dst_applied, oráculo FP primario y entradas permitidas al analizador. hidden_truth seguirá fuera del analizador. Son contratos lógicos, no fixtures ni pruebas ejecutadas.

## 67. Contratos adversariales de RUL

La suite futura debe discriminar, para la regla finalmente instanciada: (1) AST y semántica preservados; (2) operador EQ/NEQ/IN/NOT_IN alterado; (3) clave/operando intercambiado; (4) scope alterado; (5) REQUIRE/FORBID invertido; (6) dominio finito incompleto o ampliado; (7) regla eliminada/duplicada; (8) UNKNOWN convertido a TRUE/FALSE; (9) regla preservada en F1/A1 pero no aplicada en F2/A2; (10) igualdad textual con mapping semántico divergente; (11) regla tautológica sin capacidad de discriminar; (12) regla sin fuente funcional o fuera de P0.

Cada contrato separará hidden_truth, AST/entrada del analizador, resultado de mapping, estado aplicado, evidencia y oráculo FP-03/06/07. Las salidas admiten 1/0/? según cobertura y evidencia. No hay fixtures serializados ni pruebas ejecutadas.

## 68. Contratos de verdad conocida para el servicio sintético y RUL

Sobre C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md, la futura suite discriminará: (a) ENABLED=true con STANDARD/READ_ONLY (satisface); (b) ENABLED=true con DISABLED (viola); (c) ENABLED=false con cada perfil (no restringido por esta implicación); (d) mutación de operador/dominio; (e) cambio de scope/owner/efecto; (f) regla no aplicada en destino; (g) UNKNOWN por ausencia/conflicto/cobertura; (h) etiquetas físicas distintas con mapping semánticamente equivalente; (i) etiquetas iguales con mapping semánticamente divergente. Separar hidden_truth, entrada del analizador, evidencia y oráculo. Son contratos conceptuales, no fixtures serializados ni pruebas ejecutadas.


## 69. Crosswalk integrado de contratos para el paquete C (2026-11-09)

Este apartado organiza contratos existentes; no crea pruebas nuevas ni declara su ejecución.

| Familia | Contratos reutilizados | Papel en C | Estado |
|---|---|---|---|
| Estimación/identificación | P177-01…12 | ITT, primeras etapas, IV/LATE, heterogeneidad, multiplicidad, recuperación y dictamen | DEFINED / NOT EXECUTED |
| Diseño cuantitativo | P178-SIM-01…10 | N, potencia/precisión, réplicas, error Monte Carlo, pérdidas y reproducibilidad | DEFINED / PARAMETERS OPEN |
| Value | P179-01…08 | Vector, independencia A/O/V, contexto, trade-offs y agregación | DEFINED / OPERATIONALIZATION OPEN |
| Validez de constructo | P182-01…12 | Circularidad, cobertura, error, acuerdo, invariancia, firewall | DEFINED / EVIDENCE OPEN |
| Ausencia/censura | P183-01…13 | MCAR/MAR/MNAR, selección, ITT, cotas y dictamen por estimando | DEFINED / PARAMETERS OPEN |
| Interfaz | Maestro §221 | Entradas AB, salidas C y no sustitución de estimandos | CONTRACT DEFINED |

### 69.1 Reglas de evaluación adicionales como interpretación de los contratos existentes

1. La recuperación se evalúa por estimando, dimensión de Value y escenario; no solo con métricas agregadas.
2. Una abstención correcta ante no-identificación es acierto del Analyzer, no fallo de recuperación.
3. La recuperación de truth sintética no es evidencia empírica externa de ΔT_acc→Value.
4. ITT sobre Outcome no se usa como sustituto de ITT sobre Value.
5. El LATE de Outcome no se transporta a Value ni a otra dimensión sin justificación.
6. Los efectos mediados por ΔT_acc* requieren una intervención mediadora y tratamiento explícito de confusión postratamiento.
7. Los umbrales de aceptación, MDE, potencia, precisión, N y R se fijan ex ante; no se importan valores ilustrativos históricos.

**Estado:** crosswalk documental; sin fixtures, implementación, simulación o ejecución.


## 70. Crosswalk de C-01…C-07 con contratos existentes (2026-11-09)

| Resolución propuesta | Contratos fuente | Verificación exigida |
|---|---|---|
| C-01 Jerarquía científica/diseño | P177-12; C10-D1/S4-R §18 | No sustitución de θ_A(q) por ITT/paquete/LATE |
| C-02 Value vectorial y Outcome separado | P179-01…08; P182-03/04 | Fichas e indicadores independientes por dimensión |
| C-03 Sin dimensiones/pesos por default | P179-04/06/08; P178-SIM-10 | Justificación contextual y sensibilidad |
| C-04 Registro de estimando | P177-01…12; P182-12; P183-13 | Campos obligatorios y provenance |
| C-05 ITT/missingness | P177-01/06; P183-01…10 | Población asignada, ausencia/selección y no ajuste post-Z |
| C-06 Dictamen/abstención | P177-10/12; P183-11/12 | Recuperación y clasificación correcta |
| C-07 Firewall | P182-11; contrato Generator/Analyzer/Evaluator | Pruebas negativas de leakage |

Este crosswalk no crea nuevos contratos ni declara pruebas ejecutadas. Las propuestas C-01…C-07 no cambian el estado de P177/P178/P179/P182/P183.

## 71. Crosswalk del contrato operativo O/V con pruebas existentes (2026-11-09)

| Elemento §224 | Contratos existentes | Criterio de verificación |
|---|---|---|
| Ficha Outcome | P182-03/05/08/12; P183-01…10 | Unidad, fuente, cálculo, ventana, validez y ausencia reconstruibles |
| Ficha Value | P179-01…08; P182-04/06/08/09/10/12 | Dimensión contextual, vector, acuerdo, error, invariancia y sensibilidad |
| Adjudicación A/ΔT_acc | P182-01/02/06/07; contratos A/ΔT_acc | Independencia respecto de O/V y verdad del DGP |
| Firewall | P182-11; contratos Generator/Analyzer/Evaluator | Prueba negativa de acceso a truth y etiquetas ocultas |
| Estados de observación | P183-01…05/09/10/11 | No colapsar desconocido, ausencia, censura o no aplicable |
| Preespecificación | P177-09/10; P178-SIM-10; P179-08 | Dimensiones, multiplicidad y umbrales fijados ex ante |

No se crean pruebas ejecutadas ni se seleccionan indicadores/valores. §224 define fichas y criterios; los gates materiales siguen abiertos.


## 72. Crosswalk de identificación y evaluación estadística del paquete C (2026-11-09)

| Elemento §225 | Contratos / fuentes existentes | Verificación exigida |
|---|---|---|
| Jerarquía e identificación por estimando | P177-01…12; C10-D1/S4-R §§18,20,22; auditoría D2 IV §§1–8 | Dictamen separado por estimando, resultado, población y horizonte; no sustitución de θ_A(q) |
| Primera etapa y tratamiento | P177-03/04; AB event log; contratos C_dep*/A_f*/D_f* | FS_Cdep, FS_Af, FS_Df independientes; truth y observed separados |
| Mediación y confusión postratamiento | P177-05…08; P182-01/02/06/07; §225.3 | DAG temporal, confusores inducidos, estimando interventional y no ajuste post-Z |
| Población/soporte/interferencia | P177-01/02/06; P183-01…10; AB population/unit contracts | Elegibilidad pre-Z, q_X*, overlap, unidad y mapa de exposición |
| Missingness/censura | P183-01…10; §224.5 | Estados de observación, mecanismo, sensibilidad y bounds |
| IV/LATE | Auditoría C10-S D2 LATE/IV §§3–8; C10-D1/S4-R §18.4 | Gates IV-G1…G8; no Wald causal antes de cierre |
| Sensibilidad/bounds | P178-SIM-10; P179-06/08; P183-09/10 | Escenarios adversariales, rangos justificados, cobertura y tipping points |
| Evaluación Analyzer | P177-10/12; P182-11; P183-11/12 | Truth oculta, clasificación de identificación, falsa identificación y abstención |
| Potencia/N/Monte Carlo | P178-SIM-10; P179-08; §225.8 | N/replicates derivados de precisión/potencia/error Monte Carlo, no arbitrarios |
| Criterios de aceptación/falsación | P177-10/12; P178-SIM-10; §225.9 | Tolerancias ex ante y clasificación por estimando×resultado×DGP |

Este crosswalk reutiliza contratos existentes y añade criterios de evaluación, no nuevas pruebas ejecutadas. Los IDs citados deberán comprobarse contra la versión contractual vigente antes del implementation contract; este registro no altera P177/P178/P179/P182/P183.


## 73. Corrección auditada del crosswalk P177–P183 para mediación (2026-11-10)

La fila de mediación/confusión postratamiento de §72 no debe citar P177-05…08 como contratos de mediación. La tabla fuente §55.1 define esos IDs como O/V, ajuste basal, ATE/ATT y heterogeneidad. Se mantiene el historial de §72, pero esta corrección gobierna su interpretación.

| Elemento | Referencia correcta | Alcance real |
|---|---|---|
| ITT sin ajuste post-Z | P177-06 | Ajuste basal preespecificado; no incorporar mediadores postasignación |
| Política frente a atribución focal | P177-12 | Separación del efecto de política y atribución a accesibilidad |
| Validez/adjudicación de A | P182-01/02/06/07 | Cobertura, circularidad, acuerdo y error; no identificación causal de mediación |
| Ausencia de A | P183-08 | Efecto de ausencia de A sobre identificación; no contrato mediacional completo |
| O/V independiente | P177-05; P179-01…03 | Separación de resultados y valoración |
| Mediación propiamente dicha | Maestro §225.3 | Propuesta de DAG, temporalidad, confusión inducida e intervención/método g; aún sin contrato de aceptación completo |

**Resultado:** crosswalk corregido; cobertura C-MED = PARCIAL / OPEN. No modificar definiciones de P177/P178/P179/P182/P183 ni declarar pruebas ejecutadas. No crear un test nuevo por duplicación; antes debe determinarse si la extensión cabe en P177-12 o requiere una especialización versionada y trazable.


## 74. Corrección ampliada del crosswalk estadístico P177–P183 (2026-11-10)

La revisión directa de §55 del propio registro confirma las correspondencias siguientes. Esta tabla gobierna la interpretación del crosswalk previo de §72, sin reescribir el historial ni modificar los contratos fuente.

| Criterio | Contrato correcto | Precisión de alcance |
|---|---|---|
| Primera etapa | P177-02 | Estimación, SE e intervalo de accesibilidad/etapa definida |
| Wald/LATE | P177-03 | Cociente y etiqueta LATE solo si supuestos sostenidos |
| Instrumento débil | P177-04 | Inferencia robusta; no solo aproximación normal |
| O/V independiente | P177-05 | No inferencia automática entre Outcome y Value |
| Ajuste basal/no post-Z | P177-06 | Ajuste preespecificado; no mediadores postasignación |
| ATE/ATT y heterogeneidad | P177-07/08 | No confundir con ITT/LATE; composición/ponderación explícita |
| Potencia/N/clúster/R/SE_MC | P178-SIM-01…05 | SIM-01 potencia; 02 N; 03 clúster; 04 réplicas; 05 error Monte Carlo |
| Métricas y parámetros ex ante | P178-SIM-09/10 | Métricas; MDE/relevancia/equivalencia/δ/ε/tolerancias |
| Trade-offs/agregación Value | P179-06/08 | No son contratos generales de bounds ni potencia |
| Censura/sensibilidad/bounds/dictamen | P183-09/10/11/12 | Mantener cada función diferenciada |
| Recuperación y firewall | P177-10; P182-11 | No cubren por sí solos falsa identificación ni abstención correcta |
| Política frente a atribución | P177-12 | No identifica mediación ni θ_A(q) por sí solo |

**Gates de cobertura parcial:** C-MED: §225.3 no tiene aún contrato de aceptación mediacional completo. C-ANALYZER: falta formalizar adjudicación y tolerancias de falsa identificación, falsa atribución focal y abstención. Ambos permanecen OPEN; no crear pruebas duplicadas hasta decidir si una especialización versionada de contratos existentes es suficiente.

No se declaran pruebas ejecutadas, parámetros fijados, potencia demostrada ni identificación causal.


## 75. Especialización candidata de P177/P182/P183 para C-MED y C-ANALYZER (2026-11-10)

Esta sección no crea IDs de prueba nuevos ni declara pruebas ejecutadas. Organiza los criterios de §228 como extensiones propuestas de contratos existentes.

| Contrato existente | Extensión candidata | Límite actual |
|---|---|---|
| P177-06 | Comprobar ajuste basal y prohibición de ajuste post-Z para ITT | No identifica mediación |
| P177-10 | Recuperación y error del Analyzer solo donde truth permite identificación | Métricas de falsa identificación/abstención requieren extensión explícita |
| P177-12 | Distinguir efecto de política de atribución a accesibilidad | No especifica por sí solo estimando interventional |
| P182-01/02/06/07 | Validez, circularidad, acuerdo y error de medición de A | No cubre confusión mediador–resultado |
| P182-11 | Separación de Generator/Analyzer y control de leakage | Requiere prueba de acceso/artefactos y adjudicación |
| P183-08/10/11/12 | Ausencia de A, sensibilidad, bounds y dictamen por estimando | No cubre por sí solo el régimen de mediación |

**C-MED:** requiere DAG/orden temporal, estimando e intervención mediadora, confusores inducidos, soporte secuencial, rutas colaterales, método y sensibilidad. **C-ANALYZER:** requiere denominadores, verdad de identificación por DGP, falsa identificación/atribución, abstención correcta/falsa abstención y tolerancias ex ante. Ambos gates OPEN.



## 76. Especialización propuesta de contratos para C-MED/C-ANALYZER (2026-11-10)

Esta sección especializa contratos existentes sin crear IDs nuevos ni declarar pruebas ejecutadas.

| Contrato fuente | Uso en la especialización | Límite |
|---|---|---|
| P177-06 | Ajuste basal preespecificado y prohibición de ajustar ITT por variables post-Z | No identifica mediación |
| P177-10 | Recuperación puntual donde la truth permite identificación | Debe complementarse para falsos positivos y abstención |
| P177-12 | Efecto de política frente a atribución a accesibilidad | No define por sí solo θ_A(q) ni el efecto interventional |
| P182-01/02/06/07 | Validez, circularidad, acuerdo y error de medición de A | No resuelve confusión mediador–Value |
| P182-11 | Firewall Generator/Analyzer y leakage | Requiere evidencia de aislamiento y provenance |
| P183-08/10/11/12 | Ausencia, sensibilidad, bounds y dictamen por estimando | No sustituye DAG/método mediacional |

**Criterio de evaluación:** estado de identificación adjudicado por estimando×dimensión×DGP×soporte; recuperación solo en identificación puntual; bounds en parcial; falsa identificación/atribución y abstención adjudicadas con denominadores explícitos. Tolerancias y umbrales siguen OPEN.

No se amplían P177/P182/P183 en esta sección; cualquier especialización contractual futura debe justificar que no duplica criterios existentes y conservar versionado/provenance.


## 77. Precedencia corregida del crosswalk ΔT_acc (2026-11-10)

La referencia correcta del DGP es §30: ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*) y ΔValidity_e pertenece a ΔE_T. La expresión anterior de §3.3 (que incluía ΔValidity y ΔState) queda supersedida. Para el cruce con C10-D1 §27.1: ΔU→A⁺/A⁻/A^reconf; ΔR→ΔR; ΔC→ΔC; ΔX queda OPEN para clasificación semántica; ΔE_T permanece separado. No se declara cierre MED-02.


## 78. Contrato de crosswalk semántico para ΔX*

No se crea un nuevo test ID ni fixture. Esta especialización operacionaliza el registro de MED-02:

- El campo debe clasificarse por su función semántica U/R/C/X/E, no por su nombre.
- X* es contexto/estado efectivo constitutivo; no se agrega como coordenada adicional a la representación analítica C10-D1.
- Se exige no doble conteo entre el contexto ΔX*, sus cambios en condiciones ΔC* y los diffs de transformaciones/relaciones.
- Cada campo tendrá field_id, definición, unidad/frontera, tiempo, tipo, regla basal/post, condición constitutiva, mapping, event_id, overlap, truth/observed, adjudicación y estado 1/0/?.
- UNKNOWN/? es salida válida y bloquea la atribución que dependa de ese campo.

**Adversariales a cubrir en la especificación (sin fixtures):** cambio de versión efectiva con regla de compatibilidad constante; regla de compatibilidad que cambia sin cambiar el entorno; cambio de modo de despliegue que abre/cierra una ruta; evidencia/logs que cambian sin cambio estructural; cambio post-t3; un mismo campo documental que mezcla valor y regla.

El roster y la adjudicación de estos casos siguen OPEN. No se amplían contratos P177/P182/P183 ni se afirma ejecución.


## 79. Roster de campos y regla de clasificación para MED-02c

La evaluación debe consumir el roster del maestro §232, no crear un roster alternativo. No se crean fixtures ni valores. Por cada campo real se exigirá identidad/versionado, unidad/frontera, vigencia, tipo semántico U/R/C/X/E_T, valor basal/post o diff, efecto estructural, mapping, event_id, truth y observación, evidencia/cobertura y adjudicación.

Los adversariales de B-M01…15 se mantienen como dominios de inspección, no como hechos observados. No inventariar = UNKNOWN/?, no 0. Campos mixtos se descomponen o quedan UNKNOWN. E_T nunca entra en ΔT_acc*. Las rutas F y A conservan evidencia y adjudicación separadas.


## 80. Contratos de aceptación del DAG Opción A/D2

- **DAG-01 (temporalidad):** validar reloj t−1…t9, orden causal, snapshots inmutables y eventos posteriores.
- **DAG-02 (separación de estados):** probar que Z/B/W_programmed/W_attempt/S_install/C_dep*/A_f*/D_f*/ΔT_acc*/Reach/K/Sel/Exec/O/V no se colapsan ni imputan entre sí.
- **DAG-03 (crosswalk):** exigir tipado U*/R*/C*/X*/E_T por subcampo, no por superficie B-M; X* no se suma como coordenada independiente ni se duplica con C*/R*/U*.
- **DAG-04 (rutas colaterales):** inspeccionar recursos/capacidad, permisos/seguridad, dependencias compartidas y A1/A2, coste/latencia/calidad, información/incentivos, medición y spillovers.
- **DAG-05 (invariancia D2):** verificar las condiciones comunes de DEC-C10-067; si fallan, clasificar efecto de paquete o diseñar identificación adicional.
- **DAG-06 (mediación):** intervención sobre distribución conjunta factible de ΔT_acc*; A_f* como predicado/proyección y D_f* como indicador derivado, no mediadores seriales.
- **DAG-07 (estimandos):** ITT_Z(D2), primeras etapas, LATE_f y θ_A(q) reportados por separado; no transferir entre escenarios ni derivar uno por resta.
- **DAG-08 (observación):** E_T y A_f/O/V observados separados de truth; falta de cobertura propaga ?.

**Estado:** contratos definidos a nivel de criterio; tolerancias, adjudicación, denominadores y pruebas concretas pendientes. No se han creado fixtures ni ejecutado pruebas.


## 81. Contrato de aceptación AB-01/02 — mapping lógico CMP/PAR/RUL entre etapas (2026-11-10)

Esta sección especializa criterios existentes; no crea test IDs, fixtures ni declara pruebas ejecutadas. Reutiliza DEC-C10-054/065/071/079/080/082/083 y los contratos de preservación FP-01…FP-08.

| Criterio de aceptación | Comprobación documental/técnica futura | Resultado que no debe inferirse |
|---|---|---|
| ABM-01 — AST bindings | Exactamente dos bindings tipados AST→PAR; claves, tipos y snapshot owner concordantes | No REF/EDGE por operand binding |
| ABM-02 — regla RUL | Identidad, owner, scope, AST, OR/NEQ/IN, constantes, conjunto ENUM, REQUIRE y UNKNOWN preservados | No basta igualdad textual ni éxito de parser |
| ABM-03 — parámetros | Aplicar DEC-C10-083 por siete stage_key; identidad/tipo/dominio/estado/valor preservados en F1/A1; estado aplicado observado en F2/A2 | No inferir aplicación desde DST_DECL |
| ABM-04 — CMP anchor | Un NODE anchor exacto por CMP y snapshot; pinning exacto; continuidad por component_id contractual | No exigir igualdad de object_record_id entre snapshots |
| ABM-05 — PAR evidence binding | Manifiesto append-only y COVERAGE_SCOPE exacto; control DEC-C10-081 | No FK PAR inexistente ni cobertura COMPLETE por mera vinculación |
| ABM-06 — REF | Inventario y cobertura exhaustivos antes de declarar REF=0; cada REF real conserva extremos/tipo/dirección | No inferir vacío desde ausencia de filas |
| ABM-07 — mapping de ruta | M_F1/M_F2 y M_A1/M_A2 versionados, composiciones separadas, cobertura y estados MAPPED/UNMAPPED/AMBIGUOUS/NOT_APPLICABLE | No inferir independencia A respecto de B |
| ABM-08 — representación U_G | Reutilizar NODE, PREDICATE, manifiesto/COVERAGE_SCOPE y registros de evidencia existentes | No crear tablas/columnas ni extrapolar JCS UDG-01 |

**Gate:** hasta que existan mappings versionados, snapshots exactos, roster/cobertura, evidencia y validación independiente, AB-01/02 permanecen diseño semántico reconciliado, no schema implementable. UNKNOWN/? es resultado válido; no se imputa como fallo ni como éxito sin regla/evidencia suficiente. Sin fixtures, parser, validator, implementación ni ejecución científica.


## 81. Reconciliación PC — cobertura contractual C3/C4 (2026-11-11)

La reconciliación PC se registra en el maestro C10-S §268. Esta sección no crea IDs de test ni modifica P177/P178/P179/P182/P183, CAUS-01…10 o DAG-01…08.

**Cobertura reutilizada y límite:**
- CAUS-01/03/04/05/08/09 y QX-05…10 cubren atribución focal, régimen común, soporte, mediadores post-Z, vías colaterales, escenarios y separación de estimandos.
- DAG-01…08 cubren temporalidad, separación de estados, crosswalk, vías colaterales, invariancia D2, intervención mediadora conjunta, jerarquía y observación.
- P177-06/12, P182-01/02/06/07/11 y P183-08/10/11/12 cubren partes de la evaluación, pero ninguno por sí solo especifica el estimando interventional ni resuelve confusión mediador–resultado inducida por Z.
- P177-10 y P178-SIM-09/10 requieren especialización posterior para falsa identificación, falsa atribución focal, falsa abstención/abstención correcta y tolerancias por estimando×resultado×DGP.

**C-MED permanece PARCIAL / OPEN.** Antes del contrato técnico deben concretarse: bloque mediador e intervención estocástica/secuencial; orden temporal y régimen; confusores post-Z y estrategia de identificación; soporte secuencial; distinción entre mediación conjunta y path-specific; criterios de descomposición y residual; resultados O_k/V_j; missingness/censura/error; y aserciones/tolerancias de recuperación y abstención. Si el DAG no permite aislar la ruta o falta soporte, la verdad esperada será NO IDENTIFIED/BOUNDS, no un efecto puntual.

No se crean fixtures, no se fijan parámetros y no se ejecutan pruebas.


## 58. Crosswalk de aceptación del paquete PD (2026-11-11)

El contrato integrado y sus bloqueos se especifican en C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md. Este crosswalk no duplica IDs ni declara pruebas ejecutadas.

| Familia existente | Función dentro de PD | Estado documental | Pendiente para aceptación |
|---|---|---|---|
| S4R-01…18 / POL-01…10 | D2, primera etapa, alternativas, vías de paquete y atribución | Registrados | Fixtures/oráculos, mapping, soporte y tolerancias |
| MEAS-01…14 / P182-01…12 | Validez, error, invariancia, fiabilidad y cegamiento | Registrados | Parámetros de error, referencias de validación y reglas cuantitativas |
| MISS-01…15 / P183-01…13 | MCAR/MAR/MNAR, selección, censura, cotas | Registrados | Mecanismos generativos, sensibilidad/tipping points y soporte |
| P177-01…12 | ITT, primeras etapas, IV/LATE, recuperación y dictamen | Registrados | Estimandos finales, weak-IV, precisión, multiplicidad y tolerancias |
| P178-SIM-01…10 | Potencia, N/R, SE_MC, reproducibilidad | IDs organizativos derivados | Objetivos cuantitativos y búsqueda en cuadrícula ex ante |
| P179-01…08 | Value contextual y dimensiones | Registrados | Bloqueados hasta instancia PA de Value |
| VER/TRJ/INT/GEN/PM/SNAP/REACH/PROV/GC/U_G | Versiones, trayectorias, interacciones, invariantes y evidencia | Cobertura parcial/documental | Crosswalk por escenario, truth/observed/evaluation y fixtures discriminantes |

Los dictámenes deben ser por estimando y dimensión. PASS sintético solo acredita recuperación dentro del DGP y tolerancias especificados; no establece causalidad empírica real ni claim TGCV. La no-identificación correctamente detectada es resultado válido del Analyzer.

## 59. Crosswalk PE — validación técnica y gates de implementación (2026-11-11)

La especificación integrada se encuentra en C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md. Esta sección no crea familias de pruebas ni declara tests ejecutados.

| Capa PE | Contratos/fuentes reutilizados | Estado | Aceptación futura requerida |
|---|---|---|---|
| V0 Consistencia estática | DEC-C10-071/074–088, U_G, vocabularios y crosswalks | Documental parcial | Informe estático versionado y sin contradicciones |
| V1 Schema/serialización | U_G §§12.9–12.10; DEC-C10-074 solo UDG-01/U1 | No implementado | Parser/validator, tipos, dominios y canonicalización por objeto |
| V2 Integridad referencial | DEC-C10-061/062/065/076/079–082; contratos U_G | Documental | Constraints/FKs exactas, supersession y ausencia de huérfanos/ciclos |
| V3 Temporalidad | t−1/t0…t9, DEC-C10-071, SNAP/DELTA, subledger B1 | Documental parcial | Casos de orden parcial, simultaneidad, snapshots y no retrocausalidad |
| V4 Firewall/seguridad | DGP roles §§6/45–47; U_G SR-12/13/19 | Condicional/no evaluado | Threat model, ACL, logs, prueba de no fuga y custodia |
| V5 Reconstrucción semántica | S4R, MEAS, POL, VER/TRJ/INT/GEN/PM/SNAP/REACH/PROV/GC/U_G | Documental | Fixtures/oráculos y aserciones discriminantes |
| V6 Recuperación causal | P177/P179/P182/P183 | Documental parcial | Estimandos, supuestos, tolerancias y escenarios identificados/no identificados |
| V7 Reproducibilidad | test_id/version, fixture_id/hash, semillas, manifiestos y workflow de ejecución | Especificado conceptualmente | Entorno/inputs/comandos/hashes fijados y replay autorizado |
| V8 Operabilidad | U_G SR-20 | NOT_ASSESSED | Prueba ciclo completo de captura, consulta, reconstrucción y auditoría |

**Regla de alcance:** JCS DEC-C10-074 solo se aplica a UDG-01/U1. No se generaliza a todos los registros. PASS_STATIC no equivale a validación ejecutable; test registrado no equivale a test implementado/ejecutado. La salida correcta del Analyzer puede ser abstención, efecto de paquete o no-identificación.


## 60. Crosswalk B2–B3 — medición independiente Outcome/Value y evaluación causal (2026-11-11)

Se reutilizan P179-01…08, P182-01…12, P183-01…13 y §224; no se crean IDs duplicados. El artefacto integrador es `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md`.

| Familia | Aplicación en B2–B3 | Estado |
|---|---|---|
| P179 | Vector V_j, perspectiva/criterio contextual, trade-offs y no agregación prematura | Regla metodológica conservada; dimensiones no seleccionadas |
| P182 | Validez, fiabilidad, reproducibilidad, error, acuerdo interevaluador, invariancia, sensibilidad y firewall | Contrato definido; fichas y evidencia no ejecutadas |
| P183 | Ausencia, selección, MCAR/MAR/MNAR, censura, cotas, sensibilidad y dictamen por estimando/dimensión | Contrato definido; mecanismos/valores abiertos |
| §224 Outcome | Ficha por O_k: constructo, criterio, fuente, unidad, baseline, horizonte, adjudicación, error y provenance | O-CONF candidato; no operacionalizado |
| §224 Value | Ficha por V_j: B1/perspectiva, consecuencia, criterio, escala, baseline, horizonte, trade-offs y provenance | Ninguna V_j instanciada |

Outcome técnico y Value contextual son constructos separados. No se asume que Outcome sea la única causa de la consecuencia valorada. ITT sobre O_k y V_j se adjudican separadamente; no se transfiere identificación. La abstención/no-identificación del Analyzer sigue siendo resultado correcto. Ninguna prueba se declara implementada o ejecutada.

## 61. Crosswalk de operacionalización Outcome/Value (2026-11-11)

Se reutilizan contratos existentes; no se crean IDs duplicados ni se declaran pruebas ejecutadas. Artefacto rector: `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md`, maestro §276.

| Familia | Cobertura relevante | Estado |
|---|---|---|
| P179-01…03 | Separación A/O/V, vector, independencia de medición | Regla reconciliada; fichas materiales OPEN |
| P179-04/05 | Perspectiva/contexto y baseline | B1/Need_preZ base; autoridad/criterio y medición basal OPEN |
| P179-06/07/08 | Trade-offs, estimación por dimensión y agregación | Vector preservado; reglas/dimensiones no seleccionadas |
| P182-01…12 | Validez, circularidad, reproducibilidad, acuerdo, error, invariancia, sensibilidad, firewall | Contratos existentes; oráculo/fuentes/evidencia y parámetros OPEN |
| P183-01…13 | Ausencia, selección, MCAR/MAR/MNAR, censura, sensibilidad, cotas y dictamen | Contratos existentes; mecanismos y parámetros OPEN |
| §224.2 | Ficha Outcome | O-CONF candidato; ficha incompleta |
| §224.3 | Ficha por dimensión Value | Ninguna V_j instanciada |
| §224.4 / PE | Adjudicación y canales Generator/Analyzer/Evaluator | Arquitectura definida; separación computacional no validada |
| MEAS-01…14 / MISS-01…15 | Casos adversariales de error/ausencia | Reutilizables; no fixtures ni ejecuciones |

F* se mantiene como criterio funcional y O-CONF como resultado adjudicado, no como dos endpoints independientes. FP-08 es probatorio. No se promueve ningún contrato a IMPLEMENTED/EXECUTED/PASS.
