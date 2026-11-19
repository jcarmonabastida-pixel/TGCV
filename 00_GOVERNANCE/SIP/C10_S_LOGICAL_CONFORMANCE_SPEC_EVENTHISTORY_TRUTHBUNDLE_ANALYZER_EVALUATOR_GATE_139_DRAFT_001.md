# C10-S — Gate 139: especificación lógica mínima EventHistory → TruthBundle → Analyzer → Evaluator

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** LOGICAL_CONFORMANCE_SPECIFIED / EXISTING_TEMPORAL_CONTRACT_REUSED / CURRENT_HARNESS_NOT_CONFORMANT / ANALYZER_VCONT_BOUNDS_METHOD_OPEN / EVALUATOR_VCONT_SCORING_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Objeto, precedencia y reconstrucción histórica

Gate 139 transforma Gate 138 en una especificación lógica mínima, reutilizando los contratos existentes. No crea otra matriz, ledger, escenario, test ID, reloj ni schema físico.

Fuentes rectoras y antecedentes:
- DEC-C10-100…104 y C10-S Decision Log.
- DGP temporal y de roles §§48–55, en particular §§49–55: estados funcionales, familias de transición, event_time, relojes separados, continuidad estricta, horizonte común, captura S3 y orden de generación.
- Integrated V_cont Analysis Contract §§1–11: estimandos ITT-Z/ITT-G, roles, firewall, validación y evaluación de estimandos de asignación. Su alcance no convierte ITT-G en θ_A ni acredita por sí solo V_cont temporal completo.
- Gates 131–138, especialmente Gate 135 (punto de pérdida de truth), Gate 136 (suficiencia documental temporal), Gate 137/DEC-C10-104 (UNKNOWN y frontera) y Gate 138 (crosswalk de componentes).
- Path Predicate Temporal Evidence Matrix, Test Contract Register P182/P183/MEAS/MISS.
- Lectura estática del harness y de los contratos. No se ejecutó código, tests, validadores, workflows, generación ni simulación.

**Precedencia de estado:** DEC-C10-100…104 aceptadas; el DGP temporal §§48–55 es contrato propuesto/borrador, no debe etiquetarse como aprobado/frozen por este Gate; el harness actual sigue siendo baseline parcial. Esta especificación lógica no promueve automáticamente el contrato DGP a estado aprobado.

## 2. Dictamen ejecutivo

La correspondencia lógica queda especificada sin fijar parámetros ni payload físico:

1. **EventHistory** es la representación reservada de la secuencia funcional efectiva generada, no una secuencia de observaciones S3.
2. **IntervalAdjudication** deriva determinísticamente A_B1(i,k) desde EventHistory, con DEC-C10-101/102/104.
3. **TruthBundle** conserva la adjudicación por unidad, intervalo y régimen potencial, además de identidad, versión y provenance; permanece inaccesible al Analyzer.
4. **Analyzer** trabaja solo con evidencia observacional sellada y el contrato analítico público. Puede emitir punto, bounds observacionales/identificativos o abstención solo si el método correspondiente está especificado y justificado.
5. **Evaluator** abre TruthBundle después de completar Analyzer y verificar identidad/sellos; evalúa recuperación y cobertura respecto al mismo estimando, población, régimen, ventana y versión.

El harness actual no implementa todavía esta cadena completa: su Generator construye arrays binarios por slot sin event history funcional fechado; TruthBundle conserva esos arrays; Analyzer no implementa bounds de V_cont; Evaluator actual puntúa ITT-Z/ITT-G escalares. El baseline ideal sigue siendo reutilizable para sus targets actuales, no como conformidad completa de V_cont.

## 3. Contrato lógico de EventHistory

### 3.1 Contenido semántico mínimo

Para cada unidad, instancia/versión, régimen potencial y ventana pertinente, la historia reservada debe permitir reconstruir:
- estado funcional efectivo basal al inicio de la ventana;
- transiciones efectivas ENABLED y PROFILE y los eventos causales que las producen;
- event_time en un reloj común ordenable;
- estado funcional previo y posterior;
- identidad/versión del objeto o componente afectado;
- familia causal y provenance reservada;
- estado terminal/censurado al cierre, si el episodio sigue activo.

Se reutilizan las familias y el registro paramétrico de DGP §§49–55. No se añade un catálogo causal alternativo. Solicitudes son eventos discretos y no sustituyen monitorización continua. Provisión, instalación, verificación, rollback y reinicio son antecedentes o transiciones; por su etiqueta no determinan A_B1. Solo el efecto funcional efectivo cuenta.

### 3.2 Relojes separados

Deben permanecer diferenciados:
- event_time: cuándo cambia la verdad funcional;
- interval grid: partición común [t0,T*] para agregar V_cont;
- observation/capture_time: cuándo S3 captura una señal;
- ingestion_time: cuándo la observación entra al expediente.

Lag, pérdida, duplicación, desorden, invalidez o ausencia S3 nunca reescriben event_time ni la truth ya generada. Δ no es frecuencia S3.

### 3.3 Continuidad estricta y fronteras

Para cada intervalo I_k, A_B1(i,k)=0 si existe al menos un incumplimiento funcional confirmado en cualquier instante de su soporte. A_B1(i,k)=1 solo si ENABLED y PROFILE se mantienen conformes durante todo el intervalo. La adjudicación usa la convención DEC-C10-104: intervalos internos semiabiertos [b_{k−1},b_k), último intervalo [b_{K−1},b_K]; evento en frontera interna se asigna al intervalo que comienza allí, y T* pertenece al último intervalo. Episodios que cruzan fronteras afectan todos los intervalos intersectados.

No se fija T*, K, Δ, unidad física, resolución, frecuencia de captura, duración mínima de episodio ni tolerancia. La especificación exige que el DGP pueda adjudicar todos los eventos que él mismo estipula; si el propio modelo/harness omite o no representa un evento, eso es defecto de especificación/implementación, no UNKNOWN funcional.

## 4. Regla de UNKNOWN: dos niveles que no deben mezclarse

### 4.1 Truth funcional reservada

Se conserva el dominio de DEC-C10-100 {1,0,?}, pero tras DEC-C10-104:
- en una historia sintética completa y determinada, Generator debe producir 1 o 0;
- ? no se genera por ausencia de campos, eventos no modelados, timestamps ausentes por defecto, incompletitud del harness, límites de resolución no definidos, fallos de captura S3 o incapacidad del Analyzer;
- ? solo podrá aparecer si una futura estipulación DGP explícita y aceptada define una indeterminación funcional intrínseca de A_B1, con condición, alcance y provenance.

No existe en los contratos inspeccionados una causa intrínseca de UNKNOWN ya aprobada. Por tanto, para el DGP confirmatorio actualmente delimitado, n?=0 en historias completas y determinadas. Se preserva compatibilidad lógica con DEC-C10-100 para una futura estipulación; no se inventa ahora esa causa.

### 4.2 Incertidumbre observacional/analítica

S3 missing, delayed, invalid, lost, incomplete o erroneous pertenece a EvidenceCandidate/SealedEvidence. No cambia la truth del Generator. Puede impedir identificación puntual del Analyzer y conducir a bounds observacionales si existe método identificado, o a abstención si no lo hay.

Por tanto, existen dos objetos de bounds distintos:
- **Truth bounds** de DEC-C10-100: [n1/K, (n1+n?)/K], calculados desde A_B1 tri-valuado reservado por unidad/régimen. Con DEC-C10-104 y sin una futura causa DGP de ?, colapsan a punto en historias completas.
- **Analyzer bounds**: conjunto identificado para el target a partir de evidencia sellada y supuestos/calibración aprobados. No se derivan automáticamente de los truth bounds ni de la fórmula [n1/K,(n1+n?)/K]. Su método, garantías y condiciones siguen OPEN.

No imputar S3 missing como funcional ?, cero ni uno. Tampoco equiparar abstención con bounds.

## 5. Contrato lógico de TruthBundle

TruthBundle es el objeto reservado Generator→Evaluator; no es EvidenceCandidate y no entra en Sealer ni Analyzer. Sin definir campos físicos nuevos, debe preservar conceptualmente:
1. identidad de mundo, unidad, instancia/versión y régimen potencial;
2. identidad/versionado del DGP y provenance/hash de la historia;
3. ventana común, fronteras y versión de la convención;
4. EventHistory y estado basal/terminal suficiente para reproducir adjudicación;
5. A_B1 por intervalo y régimen potencial;
6. contadores n1, n0, n? y truth bounds individuales derivados, con K y regla versionada;
7. outcomes/potenciales adicionales que correspondan a los estimandos de asignación ya declarados, sin colapsar targets diferentes.

Los contadores deben reconciliarse con K: n1+n0+n?=K. Los bounds deben derivarse de los contadores, no almacenarse como fuente independiente contradictoria. La verdad por intervalo debe poder reconstruirse desde EventHistory y reglas, y su derivación debe ser determinista. No se permite que S3 alimente o reescriba la truth reservada.

## 6. Contrato lógico de Analyzer

Analyzer recibe exclusivamente:
- SealedEvidence / evidencia observacional permitida;
- AnalysisContract versionado y sus supuestos visibles;
- identidad pública necesaria para verificar run, estimando, régimen y versión.

No recibe TruthBundle, potenciales, event history reservado, parámetros secretos del Generator ni truth bounds. Para V_cont:
- **Punto:** solo si el diseño y canal observacional identifican el target y la cobertura/medición requeridas están justificadas.
- **Bounds:** solo si existe un método de identificación parcial explícito, con target, supuestos, soporte, mecanismo de missingness/error y alcance de garantía declarados.
- **Abstención:** si no hay identificación puntual ni bounds válidos, o falla identidad, soporte, medición, cobertura o provenance.

El contrato integrado actual conserva su ruta puntual bajo S3 perfecto/completo para los targets de asignación que define. No debe reinterpretarse como método general para V_cont bajo S3 imperfecto. Analyzer no puede leer truth para completar intervalos ni corregir missingness.

## 7. Contrato lógico de Evaluator

Evaluator se ejecuta después de Analyzer. Antes de comparar, valida run/world, escenario, DGP, estimando, población, régimen, outcome, ventana/fronteras, versión, hashes de evidencia y resultado. Una incompatibilidad es fallo de contrato/provenance, no error numérico del estimador.

Para cada resultado V_cont:
1. reconstruir o verificar A_B1 por unidad/intervalo/régimen desde TruthBundle;
2. comprobar n1+n0+n?=K y bounds truth derivados;
3. alinear exactamente el target del Analyzer con el target de truth (unidad, población, régimen, ventana y versión);
4. si Analyzer entrega punto y truth puntual, evaluar error/recuperación conforme al criterio preespecificado;
5. si Analyzer entrega bounds, evaluar si contienen el target truth correspondiente y reportar cobertura/anchura según diseño de evaluación aprobado;
6. si Analyzer se abstiene, evaluar si las condiciones de no identificación/insuficiencia realmente lo justificaban;
7. separar fallos del Generator/harness, fallos de sellado/provenance, no identificación y error estadístico.

La cobertura de bounds requiere un diseño de repetición/replicación y criterio de aceptación aprobado; un único intervalo que contiene la truth no demuestra cobertura nominal. No se fija ahora tolerancia, cobertura nominal, N/R, inferencia ni criterio estadístico.

El Evaluator actual de ITT-Z/ITT-G permanece reutilizable para esos estimandos y sus verdades escalares. No es todavía un Evaluator V_cont tri-valuado ni de bounds.

## 8. Qué se reutiliza y qué no

**Reutilizable como base existente:**
- estructura de potenciales y asignación Z/G para ITT-Z/ITT-G en el alcance del benchmark;
- TruthBundle como frontera reservada;
- Projector/Sealer, allowlist, hash y provenance;
- S3 ideal y ruta puntual actual para los targets ya implementados;
- escenarios adversariales de medición y abstención como cobertura existente;
- contratos temporales §§49–55 como fuente de semántica de eventos, relojes, familias y orden de generación;
- P182/P183/MEAS/MISS como criterios existentes, sin declarar que los tests están implementados o ejecutados.

**No acreditado/pendiente:**
- EventHistory materializado y adjudicación temporal estricta en el harness;
- mapping completo de eventos de provisión/instalación al soporte post-Z;
- A_B1 por intervalo derivado de eventos con DEC-C10-104;
- bounds truth en TruthBundle/Evaluator (aunque su fórmula está definida);
- método de Analyzer bounds para S3 imperfecto;
- evaluación estadística de cobertura de bounds;
- θ_A y sus bounds/identificación, que no se derivan de ITT-G.

## 9. Dependencias y orden lógico previo a implementación

1. Resolver estado de aprobación/versionado del DGP temporal §§48–55 y reconciliarlo con DEC-C10-104; no duplicar su contenido.
2. Cerrar mapping temporal post-Z de provisión/instalación y soporte de EventHistory, sin seleccionar aún parámetros numéricos.
3. Definir la derivación determinista EventHistory→A_B1 por intervalo y reconciliarla con TruthBundle actual.
4. Definir por separado el contrato de Analyzer bounds para S3 imperfecto o declarar la abstención como única salida hasta que exista método.
5. Definir el criterio de evaluación de punto/bounds/abstención y su unidad de repetición.
6. Solo después, preparar una propuesta coordinada de implementación y autorización independiente.

Gate 139 no decide que haya que introducir una nueva causa de UNKNOWN. No aprueba un schema físico, no modifica el DGP contract, no fija parámetros, no cierra la identificación causal y no declara Design Freeze.

## 10. Estado y autorización

Auditoría y especificación lógica documental, más lectura estática de fuentes. No se ejecutaron tests, validadores, workflows, imports, generación, simulación, calibración, estimación ni experimento. No se modificaron código, schemas, fixtures, tests, workflows, DEC-C10-100…104, DGP contract, test register, RMA, Evidence→Claim Matrix, STATUS, main ni PR base.

scientific_execution=false  
execution_authorized=false
