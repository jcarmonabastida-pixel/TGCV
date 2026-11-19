# C10-S — Gate 145: auditoría del contrato lógico de EventHistory

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Estado:** HISTORICAL_RECONSTRUCTION_COMPLETE / R144-A_ACCEPTED / EVENTHISTORY_LOGIC_PARTIALLY_CLOSED / MATERIALIZATION_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Objeto y límites

Auditar si la semántica aceptada en R144-A basta para cerrar el contrato lógico de EventHistory, reutilizando Gates 94–98, el contrato DGP temporal §§48–55, Gates 135–144, DEC-C10-100…104 y el crosswalk lógico de Gate 139.

Esta operación es documental y de lectura estática. No crea un schema físico, no modifica el DGP original, no altera PROCESS_EVENT/U_G, no fija §51 ni parámetros temporales, y no autoriza implementación o ejecución.

## 2. Hallazgo histórico decisivo: EventHistory no es PROCESS_EVENT

Gates 94–98 desarrollan un contrato lógico candidato para PROCESS_EVENT, PROCESS_EVENT_RELATION, PROCESS_EVENT_BINDING y PROCESS_EVENT_SNAPSHOT_BINDING. Gate 97 identifica incompatibilidades y Gate 98 corrige el contrato, manteniéndolo no aceptado/no implementado.

Ese registro tiene por objeto **ocurrencias operativas observadas y revisiones de su registro**, con bindings, evidencia, snapshots y adjudicación. No es el universo exhaustivo de transiciones funcionales verdaderas generado para cada potencial sintético.

EventHistory tiene otro papel: representar la secuencia de estados funcionales verdaderos de ENABLED/PROFILE por unidad y régimen potencial, bajo control del Generator, y permitir que el Evaluator reconstruya la verdad después del sellado del Analyzer.

Consecuencias:
- No se debe reutilizar PROCESS_EVENT como contenedor de truth ni hacer que Sealer/Analyzer reciban EventHistory.
- No se debe crear un segundo registro observacional para duplicar PROCESS_EVENT.
- Los eventos de proceso (programación, intento, receipt, instalación, rollback) no son automáticamente transiciones funcionales B1.
- Una ocurrencia de proceso solo cambia A_B1 si el Generator estipula y registra el cambio efectivo de ENABLED/PROFILE.
- La identidad de una transición truth no se equipara a EID, event_id observacional, evidence_id ni adjudication_id.

## 3. Crosswalk de suficiencia lógica

| Requisito | Fuente/precedencia | Resultado Gate 145 |
|---|---|---|
| Contexto por unidad, mundo/DGP y potencial (z,g) | Gate 139; DGP temporal; Gate 143 | Definido conceptualmente; identidad física/versionado pendientes |
| Estado funcional inicial post-Z en t0 | R144-A aceptada; DEC-C10-101 | Aceptado |
| Estado ENABLED/PROFILE previo y posterior | R144-A; §§49–50; Gate 139 | Aceptado como contenido semántico |
| Persistencia por tramos | R144-A aceptada | Aceptada |
| Simultaneidad atómica y suborden explícito | R144-A aceptada | Aceptado; sin inferencia por ID/serialización |
| Familia causal, identidad/versión y provenance | R144-A; §§49–50 | Requisito aceptado; reglas de identidad/versionado aún incompletas |
| Completitud de historia en el soporte pertinente | DEC-C10-104; Gate 139 | Obligación conceptual; certificado/criterio material no especificado |
| Comparación de event_time con fronteras | DEC-C10-104; R144-B | Abierto hasta resolver §51/reloj/rejilla |
| Adjudicación estricta A_B1 | DEC-C10-102/104; Gate 139 | Regla definida; adjudicador no implementado |
| Firewall Generator → Evaluator frente a Analyzer | DGP temporal §§48–55; Gate 139 | Definido como principio; controles técnicos no verificados |

## 4. Contrato lógico mínimo resultante

Sin anticipar nombres físicos ni tipos de datos, una EventHistory válida debe preservar:

1. **Ámbito:** identidad de instancia/mundo DGP, versión del DGP, unidad, réplica/run y régimen potencial al que pertenece la historia. Los potenciales no se mezclan en una única secuencia.
2. **Estado inicial:** vector funcional ENABLED/PROFILE inmediatamente después de Z en t0, antes de las transiciones post-Z ordenadas en ese ancla.
3. **Transiciones truth:** ocurrencias que cambian el estado funcional efectivo, cada una con identidad/versionado, event_time, estado anterior/posterior, componente funcional afectado, familia causal y provenance del Generator.
4. **Orden:** relación temporal común y suborden explícito solo cuando existan varios pasos causalmente ordenados en el mismo instante. Cambios genuinamente simultáneos forman una transición atómica. No se deduce precedencia de IDs ni del orden de serialización.
5. **Persistencia:** el estado posterior de una transición permanece vigente hasta la siguiente transición truth explícita, sin interpolación.
6. **Completitud:** la historia debe declararse completa para su ámbito, régimen y soporte generativo. La ausencia de otra transición solo permite mantener el estado si esa completitud está garantizada por el contrato del Generator. Historia incompleta, colisión irresuelta, timestamp inválido u omisión es defecto DGP/harness, no UNKNOWN funcional.
7. **Trazabilidad:** cada valor adjudicado de ENABLED/PROFILE y cada A_B1 derivada debe poder remontarse a estado inicial, transiciones relevantes, versión de reglas y provenance del mundo sintético.
8. **Separación:** EventHistory y TruthBundle permanecen reservados al Generator/Evaluator. Sealer/Projector reciben únicamente observaciones permitidas; Analyzer no recibe verdad, potenciales, historia reservada, parámetros secretos ni truth bounds.

Este es un contrato lógico de contenido y relaciones. No define todavía un schema, campos obligatorios físicos, codificación de timestamp, algoritmo de ordenación ni estructura de almacenamiento.

## 5. Separación de eventos de proceso y transiciones funcionales

Se mantiene la cadena de proceso ya establecida (programación → intento → receipt → instalación/verificación/rollback) como historia de antecedentes operativos. La cadena no determina por sí misma A_B1.

La relación correcta es:

- Evento de proceso: describe qué acto ocurrió en el mundo sintético.
- Transición truth funcional: describe el cambio efectivo de ENABLED y/o PROFILE causado o no por ese acto.
- Estado funcional: valor que persiste tras la transición.
- A_B1: adjudicación estricta de ambos componentes durante el intervalo completo, cuando exista una rejilla temporal comparable.

Un evento de instalación exitosa no prueba ENABLED=1 ni PROFILE=1. Un rollback no implica por sí mismo fallo B1. Una transición puede tener más de una causa en el DGP; la provenance debe conservar la relación causal declarada sin introducir atribución post hoc.

## 6. Identidad, versión y completitud: lo que aún no está cerrado

R144-A acepta que cada transición tenga identidad/versión y provenance, pero no fija el ciclo de vida exacto de esa identidad. Gate 98 ofrece distinciones útiles para registros observacionales (ocurrencia, revisión, evidencia y adjudicación), pero no autoriza transferir su modelo de revisiones a truth generada.

Quedan pendientes, para una especificación de materialización posterior:
- alcance de unicidad de la identidad de transición dentro de mundo, unidad, potencial y versión;
- significado de versión de transición frente a versión del DGP/historia completa;
- regla para regeneración/corrección de una historia sintética y preservación de hashes/provenance;
- criterio verificable de completitud sobre el soporte de eventos posibles;
- tratamiento de un evento válido pero funcionalmente neutro, sin confundirlo con ausencia de historia.

No se resuelven mediante event_id observacional ni creando nuevas tablas. Deben derivarse del contrato de identidad/provenance del DGP y de los objetos existentes.

## 7. Límite temporal preservado

EventHistory puede definirse lógicamente sin seleccionar unidad física ni valores temporales. Sin embargo, una clave ordinal no basta para decidir si una transición cae dentro de un intervalo o coincide con una frontera.

Continúan abiertos por R144-B y Gate 142:
- aceptación completa de §51 y de la coordenada normalizada como contrato;
- reloj y soporte temporal común materializables;
- W_c, t_c,max, T*, ρ_follow, Δ y K;
- relación exacta entre event_time y fronteras b_k;
- resolución/detectabilidad y mecanismo/calibración S3.

DEC-C10-104 se aplicará sin alteración cuando exista una relación temporal comparable. No se calcula V_cont numérico ni se declara conformidad temporal completa antes de resolver esas dependencias.

## 8. Dictamen

**EventHistory está parcialmente cerrado en semántica, no en contrato materializable.** R144-A resuelve el estado inicial, persistencia, cambios funcionales, simultaneidad y suborden. Gates 139 y 143 ya fijan su papel reservado y su relación lógica con TruthBundle/Evaluator. No hace falta crear otra matriz ni otro ledger.

Los vacíos genuinos son: identidad/versionado de transiciones truth, completitud verificable del ámbito generativo y posterior mapeo de event_time al soporte/rejilla. La separación frente a PROCESS_EVENT observacional es obligatoria para evitar duplicación y leakage.

No se crea DEC nueva. No se cambia DGP original, Decision Log, schemas, U_G, código, tests, workflows, RMA, Evidence→Claim Matrix, STATUS, main ni PR base. No se ejecutaron validadores, pruebas, generación, simulaciones, calibración o experimentos.

**Siguiente operación:** Gate 146 debe reconciliar identidad/versionado y completitud de EventHistory con los contratos DGP de identidad, provenance y generación ya existentes, sin diseñar todavía el reloj físico ni un schema.

scientific_execution=false  
execution_authorized=false
