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

## 9. Familias GEN y requisitos aún no convertidos a fixtures

Los invariantes S4R-GEN-01…12 de C10-S §30.8 deben convertirse en pruebas con verdad oculta y aserciones equivalentes. Los hallazgos AUD-004…008 requieren contratos específicos para ΔT_acc, Reach_possible, S5-F, S5-C y no circularidad de Value. No se declara que los catálogos existentes cubran estas familias de forma ejecutable.

## 10. Reglas de interpretación del resultado

- PASS significa que el analizador discrimina correctamente el escenario sintético y recupera lo que el DGP hace identificable dentro de tolerancias justificadas.
- FAIL significa que viola una aserción, confunde constructos/estimandos o emite una conclusión no permitida.
- INDETERMINATE significa que la evidencia, soporte, precisión o identificación no permiten una decisión.
- **No identificación** es una conclusión metodológica correcta en ciertos fixtures, no un fallo del analizador.
- No usar ausencia de significación como equivalencia.
- No calcular Wald con primera etapa nula.
- No atribuir ITT_Z a accesibilidad cuando exclusión no está defendida.
- No convertir un resultado sintético PASS en evidencia empírica de C10.

## 11. Pendientes antes de convertirlo en contrato ejecutable

1. Confirmar diccionario y temporalidad de cada variable.
2. Fijar versiones del fixture y mecanismo exacto B_g0/B_g1, intento, éxito y verificación.
3. Resolver población, F*, q*, horizonte y regla Value.
4. Especificar verdad oculta, parámetros y salidas exactas por prueba.
5. Justificar tolerancias, N, réplicas, precisión, δ y ε.
6. Definir códigos de error y artefactos reproducibles.
7. Auditar no filtración entre generador, analizador y evaluador.
8. Obtener revisión independiente.
9. Autorizar por separado implementación y ejecución.

**Dictamen:** este registro normaliza el inventario de pruebas conocido y explicita las aserciones mínimas. No constituye implementación, ejecución ni PASS. El cierre de AUD-003 y XSYNC-06/07/09/10 depende de completar los fixtures, verificar cobertura y realizar la auditoría independiente.
