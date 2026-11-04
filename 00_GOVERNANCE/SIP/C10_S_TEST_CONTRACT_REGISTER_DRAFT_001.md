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


## 14. Contrato candidato D1/D2 y primera etapa focal

| Elemento | D1 principal condicionado | D2 contraste |
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
