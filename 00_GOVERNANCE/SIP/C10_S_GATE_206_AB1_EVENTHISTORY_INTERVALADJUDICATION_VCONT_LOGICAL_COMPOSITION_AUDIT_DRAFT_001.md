# C10-S — Gate 206: composición lógica A_B1 → EventHistory → IntervalAdjudication → V_cont

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** DOCUMENTARY_LOGICAL_RECONCILIATION / GATE_154_SCOPE_APPLIED / GATE_139_PARTIALLY_SUPERSEDED_IN_SCOPE / LOGICAL_CONTRACT_PARTIALLY_CLOSED / TEMPORAL_MATERIALIZATION_OPEN / §51_OPEN / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Objeto, identidad y no-colisión

Gate 206 continúa la línea científica de Gates 145–154. El identificador 155 no se reutiliza: ya corresponde a la implementación técnica de outer Monte Carlo replication, y Gate 156 a su contrato de cobertura de matriz. Gate 206 no altera, renumera ni sustituye Gates 155–205.

Objeto: reconciliar documentalmente la composición lógica de A_B1 → EventHistory → IntervalAdjudication → V_cont bajo el alcance aceptado en Gate 154, comprobando su compatibilidad con R144-A, R146-A…D, R147-A/B, R148-A, R150-A, R151-A8, R152-A1…A6 y DEC-C10-100/101/102/104.

## 2. Fuentes y límites de reconstrucción

Se recuperaron de GitHub:
- Operativa `00_GOVERNANCE/README.md` en `main`.
- Gates 139, 145 (contrato y addendum del plan), 150, 152, 153 y 154 en `research/c10-s-consolidation-draft`.
- Gates 155 y 156 para verificar la ocupación de numeración y su alcance técnico distinto.
- El documento de Gate 205 para verificar que las operaciones recientes de infraestructura no reemplazan la línea lógica aquí auditada.

No se ejecutaron los validadores locales del bootstrap. Este registro no declara un PASS integral de bootstrap ni certifica el estado local. La auditoría es documental y no sustituye una revisión línea por línea de todos los artefactos DEC/DGP fuente; se limita a las reglas y contratos explícitamente recuperados en los documentos citados.

## 3. Precedencia de alcance: Gate 154 frente a la formulación anterior de Gate 139

Gate 139 sigue siendo la especificación de referencia para la separación EventHistory / TruthBundle / Analyzer / Evaluator, relojes, frontera truth/observación, reglas de UNKNOWN y requisitos lógicos de adjudicación.

Sin embargo, Gate 139 §3.1 y §3.3 describían transiciones ENABLED y PROFILE y exigían ENABLED y PROFILE conformes durante todo intervalo. Esa formulación antecede a R151-A8 y a la aceptación expresa de la Opción A en Gate 154.

Por tanto, **para el alcance temporal actual de A_B1/V_cont, Gate 154 delimita y sustituye la lectura de Gate 139 que incluía PROFILE exposure en el predicado temporal adjudicado**. No se elimina ni se reescribe el documento Gate 139. Se conserva todo lo compatible:
- PROFILE sigue siendo configuración declarada y obligación contractual de B1.
- No existe en el DGP vigente una trayectoria truth independiente de PROFILE exposure.
- La continuidad de admisión no demuestra PROFILE exposure.
- PROFILE exposure no se convierte en UNKNOWN ni se declara cumplida.
- El predicado temporal adjudicado por V_cont se limita a la función efectiva de admisión/no-admisión requerida por ENABLED, incluyendo la disponibilidad operativa y los mecanismos runtime cuando impiden efectivamente ese comportamiento.

Esta precedencia evita que un texto anterior vuelva a ampliar silenciosamente el estimando después de Gate 154.

## 4. Contrato lógico compuesto

### 4.1 Predicado funcional temporal A_B1

A efectos de la adjudicación temporal vigente, A_B1 representa el comportamiento funcional abstracto de admisión conforme al estado ENABLED:

- ENABLED=true: el servicio debe admitir.
- ENABLED=false: el servicio no debe admitir.
- La no-admisión con ENABLED=false es comportamiento correcto, no incumplimiento.
- La admisión efectiva con ENABLED=false es incumplimiento.
- La incapacidad funcional confirmada de admitir con ENABLED=true es incumplimiento.
- Las condiciones runtime y de disponibilidad entran en el predicado solo cuando alteran efectivamente el comportamiento requerido.

La validez declarativa de la RUL aplicable se conserva como condición de configuración; no se convierte en uptime ni sustituye la comprobación del comportamiento de admisión.

PROFILE exposure queda fuera del predicado temporal adjudicado por Gate 154, sin perder su condición de obligación contractual.

### 4.2 EventHistory

EventHistory es la historia funcional truth generada, no PROCESS_EVENT ni evidencia S3. Debe permitir reconstruir, para cada unidad, mundo/instancia y régimen potencial pertinente:
- estado funcional basal post-Z;
- transiciones funcionales efectivas que alteren el predicado temporal A_B1;
- estado anterior y posterior;
- identidad propia y versión de transición;
- familia causal y provenance reservada;
- event_time en un orden temporal común;
- estado final o persistencia hasta el cierre del soporte.

No se registra un evento truth por cada antecedente técnico. Provisión, instalación, verificación, rollback, reinicio, solicitudes o registros operativos solo son antecedentes; entran en EventHistory cuando producen un cambio funcional efectivo relevante para A_B1. No se duplica una única transición por múltiples antecedentes.

Las transiciones declarativas ENABLED que cambian el comportamiento requerido y las transiciones runtime que cambian la capacidad efectiva de cumplirlo deben quedar representadas cuando alteran A_B1. No se añade una transición independiente de PROFILE exposure.

### 4.3 IntervalAdjudication

Para cada unidad i e intervalo k, IntervalAdjudication aplica el operador temporal estricto ya aceptado al predicado A_B1 delimitado en §4.1:

- `1`: el comportamiento de admisión/no-admisión requerido se cumple durante todo el soporte del intervalo.
- `0`: existe al menos un incumplimiento funcional confirmado en cualquier instante del soporte.
- `?`: únicamente si una estipulación futura, explícita y aceptada del DGP establece indeterminación funcional intrínseca. No se genera por falta de campo, defecto de historia/harness, evento omitido, ausencia o fallo S3, timestamp no materializado, límite de resolución no definido o incapacidad del Analyzer.

En historias sintéticas completas y determinadas del DGP vigente, la adjudicación debe ser 1 o 0; no se ha aprobado una causa intrínseca de ?.

Se preservan las fronteras y convenciones de DEC-C10-104: intervalos internos semiabiertos, último intervalo cerrado en T*, asignación de evento en frontera interna al intervalo que comienza allí y propagación de episodios a todos los intervalos que intersectan. Esta referencia lógica no fija reloj físico, unidad, rejilla, T*, Δ, K ni resolución.

### 4.4 V_cont

V_cont se deriva de las adjudicaciones A_B1 por intervalo conforme a DEC-C10-100 y al horizonte/convenciones aceptados, sin crear una fórmula alternativa ni almacenar bounds contradictorios con los contadores.

Su alcance actual es **continuidad temporal de la función efectiva de admisión B1**. No es:
- cumplimiento íntegro de todas las obligaciones contractuales B1;
- evidencia de continuidad de PROFILE exposure;
- uptime del flag ENABLED aislado;
- medida general de Value contextual TGCV.

La fórmula/soporte numérico definitivo y los parámetros temporales permanecen sujetos a §51 y a las decisiones temporales aún abiertas.

## 5. Identidad, versionado y completitud

Se preservan R146-A…D:

1. Cada transición truth tiene identidad propia, única dentro de EventHistory y separada de TID/EID/identificadores observacionales.
2. Las versiones de DGP, EventHistory y reglas de adjudicación son identidades distintas.
3. La corrección/regeneración es inmutable: produce nueva versión de historia y conserva la anterior.
4. La completitud se evalúa respecto al ámbito generativo declarado, la cobertura del soporte y la integridad de representación; una historia sin transiciones puede ser completa.

Criterio lógico de completitud: para una unidad, instancia/versión, régimen potencial y soporte declarados, la historia debe incluir el estado basal post-Z, todas y solo las transiciones funcionales generadas que alteren A_B1 dentro del soporte, su orden/simultaneidad/suborden conforme a R144-A, y la persistencia resultante hasta el siguiente cambio o el final del soporte. Debe ser posible reconstruir determinísticamente el estado de A_B1 en todo punto del soporte y verificar el estado terminal/censurado.

Este criterio es **lógico, no todavía un algoritmo verificable materializado**. La identidad física, los hashes concretos, el esquema de versiones y el procedimiento de comparación con el universo generativo permanecen sin definir.

## 6. Simultaneidad, persistencia y orden

Se preserva R144-A:
- estado inicial post-Z;
- persistencia por tramos entre transiciones funcionales explícitas;
- transiciones simultáneas atómicas;
- suborden explícito solo cuando el DGP define estados intermedios funcionalmente relevantes;
- los defectos de historia/harness no se convierten en UNKNOWN funcional.

La historia debe distinguir el orden causal/funcional requerido del orden de captura/ingestión. `event_time`, rejilla de adjudicación, `observation/capture_time` e `ingestion_time` son relojes/conceptos distintos. La captura S3 no crea, elimina ni reordena truth.

## 7. Frontera entre verdad, evidencia y evaluación

- **Generator/EventHistory:** verdad funcional sintética reservada.
- **EvidenceCandidate/SealedEvidence/PROCESS_EVENT:** observaciones, ocurrencias operativas, revisiones, bindings y adjudicaciones probatorias según sus contratos; no sustituyen EventHistory.
- **Analyzer:** recibe evidencia permitida y AnalysisContract; no recibe EventHistory, TruthBundle ni truth reservada.
- **Evaluator:** solo accede a TruthBundle después del sellado y de que Analyzer haya terminado; verifica identidad, versión, correspondencia del target y resultado.

Una ausencia o defecto de evidencia puede producir límites de identificación o abstención analítica si el método correspondiente está especificado; no reescribe A_B1 ni EventHistory. Las garantías de Analyzer bounds y la evaluación estadística de cobertura siguen abiertas según Gate 139.

## 8. Tabla de cierre lógico y pendientes

| Componente | Estado Gate 206 | Qué queda pendiente |
|---|---|---|
| Alcance temporal A_B1 | Delimitado por Gate 154 | Formalización final en contrato DGP/DEC según gobernanza |
| PROFILE exposure | Obligación contractual, fuera de adjudicación temporal | Cualquier ampliación requiere nueva decisión y DGP |
| Familias de transición EventHistory | Principio definido por R147-A/B y Gate 206 | Auditoría exhaustiva de cobertura §§49–50 |
| Identidad/versionado | Reglas lógicas aceptadas R146-A…D | Identificadores, hashes y algoritmo materializados |
| Estado inicial/persistencia | Semántica R144-A aceptada | Mapping al soporte temporal §51 |
| Simultaneidad/suborden | Semántica R144-A aceptada | Representación ejecutable y resolución temporal |
| Completitud | Criterio lógico definido aquí sobre R146-D | Prueba/algoritmo verificable contra el universo generativo |
| IntervalAdjudication {1,0,?} | Operador y separación de UNKNOWN preservados | Mapping temporal y materialización tras §51 |
| V_cont | Alcance de afirmación delimitado | Parámetros y agregación numérica definitiva |
| TruthBundle / Analyzer / Evaluator | Fronteras lógicas preservadas | Analyzer bounds, evaluación y conformidad del harness |

## 9. Dictamen

Gate 206 cierra **la composición lógica de alcance** A_B1 → EventHistory → IntervalAdjudication → V_cont para el DGP sintético vigente, bajo la delimitación de Gate 154. No cierra la totalidad del contrato EventHistory ni su materialización.

Se clasifican los estados así:
- **CERRADO LÓGICAMENTE:** alcance temporal A_B1; exclusión de PROFILE exposure del predicado temporal actual; separación EventHistory/PROCESS_EVENT/evidencia; aplicación del operador estricto {1,0,?}; persistencia/simultaneidad/suborden R144-A; identidad/versionado/completitud como requisitos lógicos R146-A…D.
- **ABIERTO TEMPORALMENTE:** reloj físico, soporte, rejilla, mapping event_time→fronteras, T*, Δ, K y dependencias §51/R144-B.
- **ABIERTO PARA MATERIALIZACIÓN:** schema, IDs físicos, hashes, algoritmo de completitud, serialización, harness, tests y validadores.
- **ABIERTO CIENTÍFICAMENTE:** Analyzer bounds, identificación/cobertura bajo evidencia imperfecta y suficiencia estadística; no se establece ninguna afirmación causal de ΔT_acc→Value.

## 10. No-autorizaciones

Este Gate no:
- modifica DEC-C10-100/101/102/104 ni ninguna otra DEC;
- modifica el DGP original o declara §§48–55 aprobados/frozen;
- altera Gates 139 o 145; su alcance anterior queda reconciliado aquí sin reescritura histórica;
- fija §51, reloj, soporte, rejilla, T*, Δ, K, calibración S3 o parámetros;
- crea schema, ledger, código, harness, tests, fixtures ni workflows;
- ejecuta validadores, pruebas, generación, simulación, calibración, estimación, Monte Carlo o experimento;
- autoriza implementación, ejecución científica ni promoción a `main`.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`

## 11. Siguiente operación

Gate 207: auditoría de cobertura exhaustiva del universo de mecanismos de §§49–50 frente al predicado temporal A_B1 ya delimitado: identificar qué mecanismos pueden alterar admisión, cuáles son solo antecedentes, cuáles son duplicados causales del mismo cambio funcional y qué rutas podrían quedar fuera de EventHistory. No introducir nuevas familias ni seleccionar parámetros temporales; distinguir huecos reales del DGP de huecos de observación/harness.
