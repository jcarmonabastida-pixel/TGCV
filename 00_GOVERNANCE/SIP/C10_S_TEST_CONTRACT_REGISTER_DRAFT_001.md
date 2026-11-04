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
| MEAS-03 | Predicado focal | A_f* requiere identidad, relaciones, condiciones, autorización, recursos, dependencias, no bloqueo y validez |
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
| BPOL-02 | Intento vs estado final | W_attempt no se confunde con C_dep verificado |
| BPOL-03 | D1 control | P(W_attempt=1|Z=0)=.25 y P(C_dep=1|Z=0)=.20 bajo factorización candidata |
| BPOL-04 | D1 tratamiento | P(W_attempt=1|Z=1)=1 y P(C_dep=1|Z=1)=.80 |
| BPOL-05 | D2 control | P(W_attempt=1|Z=0)=0 y P(C_dep=1|Z=0)=0 |
| BPOL-06 | D2 tratamiento | P(W_attempt=1|Z=1)=1 y P(C_dep=1|Z=1)=.80 |
| BPOL-07 | Éxito condicional | .80 identificado como propuesta algebraica condicional, no dato empírico |
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
| CMP-13 | Selección primaria | D1 requiere justificación de régimen ordinario; D2 requiere justificación del objetivo ausencia-vs-provisión |
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
| CMP-15 | D1 justificado por fuente independiente .25/.20 | D1 puede considerarse para selección primaria tras decisión | Aceptar D1 solo por etiqueta “ordinario” |
| CMP-16 | D1 sin justificación externa | D1 permanece no validado como comparador ordinario | Tratar .25/.20 como realidad del dominio |
| CMP-17 | D2 con ausencia de provisión focal de fondo verificada | D2 puede considerarse para objetivo ausencia-vs-provisión | Asumir ausencia por diseño sin verificar fondo |
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
