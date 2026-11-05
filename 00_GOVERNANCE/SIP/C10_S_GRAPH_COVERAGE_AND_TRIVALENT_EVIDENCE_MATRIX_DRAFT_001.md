# C10-S — Matriz de cobertura del grafo y evidencia trivalente del microdominio Opción A

**ID:** C10-S-GRAPH-COVERAGE-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** especificación de cobertura y universo candidato; NO aprobada, NO ejecutada, NO evidencia empírica.  
**Dependencias:** contrato Reach; manifiesto de provisión B; auditoría de compatibilidad causal.

## 1. Dictamen

Puede fijarse un universo candidato de componentes y relaciones que el diseño deberá inspeccionar, pero no afirmar que sea el universo real, exhaustivo o cerrado: no hay implementación, manifiesto de paquetes, runtime, interfaz, sistema operativo ni inventario de dependencias. Por ello las afirmaciones técnicas sobre presencia, ausencia, independencia o no-afectación permanecen indeterminadas.

Se distinguen:
- **status:** verdad estructural del objeto dentro del universo de referencia (1/0/?);
- **coverage:** cobertura del universo declarado (COMPLETE/PARTIAL/NONE);
- **evidence_status:** AVAILABLE/MISSING/CONFLICTING;
- **contract_intent:** lo que B debe hacer según especificación, no observación de lo que hace.

No convertir MISSING en 0, PARTIAL en ausencia ni intención contractual en cumplimiento. El resultado actual de Reach y de existencia de alternativa funcional es ?.

## 2. Universo candidato U_G (no exhaustivo)

### 2.1 Nodos

| ID | Componente/función candidata | Clase | Papel | Existencia | Cobertura |
|---|---|---|---|---:|---|
| N01 | Unidad/sistema anfitrión y S0 | Frontera | Estado inicial | ? | NONE |
| N02 | Asignación Z | Diseño | Asigna B | ? | NONE |
| N03 | Política/proceso B | Intervención | Provisiona adaptador | ? | NONE |
| N04 | Paquete adaptador focal | D-Focal | Dependencia τ2 | ? | NONE |
| N05 | Runtime/sidecar focal | D-Focal | Aloja adaptador | ? | NONE |
| N06 | Librerías/dependencias focales | D-Focal | Dependencias transitivas | ? | NONE |
| N07 | Endpoint/canal focal | D-Focal | Invocación | ? | NONE |
| N08 | C_dep | Medición técnica | Estado técnico | ? | NONE |
| N09 | Predicados A_f* | Constructo | Accesibilidad completa τ2 | ? | NONE |
| N10 | Transformación focal τ2/F1 | Transformación | Conversión | ? | NONE |
| N11 | Aplicación F2 | Transformación | Aplicación/validación destino | ? | NONE |
| N12 | Estado destino | Estado | Resultado estructural | ? | NONE |
| N13 | Exportador A1 | D-Alternativa | Ruta alternativa | ? | NONE |
| N14 | Formato/artefacto intercambio | D-Alternativa | Interfaz alternativa | ? | NONE |
| N15 | Importador A2 | D-Alternativa | Ruta alternativa | ? | NONE |
| N16 | Oráculo/criterio F* | Medición | Evaluación funcional | ? | NONE |
| N17 | Autorizaciones C_auth | Condición | Permisos | ? | NONE |
| N18 | Recursos/capacidad compartida | Infraestructura | CPU/RAM/I/O/red/cuotas | ? | NONE |
| N19 | Configuración fuente/destino | Estado/datos | Inputs funcionales | ? | NONE |
| N20 | Dependencias/API/servicios compartidos | D-Compartida | Consumidos por ambas rutas | ? | NONE |
| N21 | Servicios externos | D-Externa | Fuera de frontera | ? | NONE |
| N22 | Información/conocimiento agente | Mecanismo | Consideración/selección | ? | NONE |
| N23 | Ejecución/Outcome/Value | Resultados | Consecuencias posteriores | ? | NONE |

Los nombres son roles del modelo, no afirmaciones de que ya exista un componente con ese nombre.

### 2.2 Aristas candidatas

| ID | Desde → hasta | Relación | Tiempo | Relevancia | Estado | Cobertura |
|---|---|---|---|---|---:|---|
| E01 | Z→B | Asigna política | t0–t1 | Tratamiento | ? | NONE |
| E02 | B→N04 | Provisiona paquete | t1 | Primera etapa | ? | NONE |
| E03 | N04→N05 | Carga en runtime | t1–t2 | Dependencia | ? | NONE |
| E04 | N05→N06 | Carga dependencias | t1–t2 | Transitiva | ? | NONE |
| E05 | N05→N07 | Expone canal | t1–t2 | Relación | ? | NONE |
| E06 | N07→N08 | Verifica estado técnico | t2 | C_dep | ? | NONE |
| E07 | N04–N08→N09 | Satisface predicados focales | t2–t3 | A_f* | ? | NONE |
| E08 | N09→N10 | Permite invocación τ2 | t3–t7 | Accesibilidad/uso | ? | NONE |
| E09 | N10→N11 | Entrega conversión | t7 | Composición | ? | NONE |
| E10 | N11→N12 | Aplica en destino | t7 | Estado | ? | NONE |
| E11 | N01→N13 | Entrada alternativa | t3–t7 | Alternativa | ? | NONE |
| E12 | N13→N14 | Exporta | t7 | Alternativa | ? | NONE |
| E13 | N14→N15 | Importa | t7 | Alternativa | ? | NONE |
| E14 | N15→N12 | Aplica en destino | t7 | Alternativa | ? | NONE |
| E15 | N12→N16 | Evalúa F* | t8 | Medición | ? | NONE |
| E16 | N18→N05 | Asigna recursos | t1–t7 | Recurso | ? | NONE |
| E17 | N18→N13/N15 | Recursos compartidos | t1–t7 | Interferencia | ? | NONE |
| E18 | N17→N07/N10/N11/N13/N15 | Autoriza operaciones | t−1–t7 | Autorización | ? | NONE |
| E19 | N20→N05/N13/N15 | Dependencia compartida | t−1–t7 | Vía colateral | ? | NONE |
| E20 | N21→N04/N05/N07/N13/N15 | Servicio externo | t−1–t7 | Frontera | ? | NONE |
| E21 | N19→N10/N11/N13/N15 | Estado/datos entrada | t−1–t7 | Condición | ? | NONE |
| E22 | N22→selección/ejecución | Información/conocimiento | t4–t7 | Vía no focal | ? | NONE |
| E23 | N10/N11/N15→N23 | Ejecución/Outcome/Value | t7–t9 | Resultado | ? | NONE |

E07 es una relación lógica de composición, no una arista técnica única. Las aristas son hipótesis de inventario; dirección y temporalidad se corregirán según arquitectura observada. Lo desconocido no se considera ausente.

## 3. Matriz de predicados de accesibilidad y trayectoria

Códigos: ID identidad/versión; REL relación/canal; COND precondiciones; AUTH autorización; RES recursos; DEP dependencias; BLOCK ausencia de bloqueos dentro del universo cubierto; APP aplicabilidad desde S0; F* conformidad funcional.

| Predicado | Pregunta operacional | Momento | Evidencia requerida | Estado | Cobertura |
|---|---|---|---|---:|---|
| ID-τ2 | ¿TID/SID/RID y versión de τ2 están fijados? | t−1,t2 | Contrato, versión, hashes, mapping | ? | NONE |
| REL-τ2 | ¿Existe canal focal invocable? | t2–t3 | API/schema, endpoint, ACL, prueba | ? | NONE |
| COND-τ2 | ¿Se satisfacen precondiciones de realización? | t−1,t3 | Contrato F1, S0, restricciones | ? | NONE |
| AUTH-τ2 | ¿Autorización funcional válida e invariante? | t−1,t3 | ACL/roles/política y diffs | ? | NONE |
| RES-τ2 | ¿Recursos disponibles en ventana? | t1–t3 | Cuotas, demanda, contención | ? | NONE |
| DEP-τ2 | ¿Dependencias presentes, íntegras, compatibles y operativas? | t1–t3 | SBOM, hashes, compatibilidad | ? | NONE |
| BLOCK-τ2 | ¿Se han descartado bloqueos relevantes? | t−1–t3 | Catálogo de bloqueos y cobertura | ? | NONE |
| APP-τ2 | ¿τ2 es aplicable al estado S0? | t3 | S0 y precondiciones | ? | NONE |
| ALT-A1 | ¿A1 existe y es funcional? | t−1–t3 | Catálogo, versión, contrato, prueba | ? | NONE |
| ALT-A2 | ¿A2 existe y es funcional? | t−1–t3 | Catálogo, versión, contrato, prueba | ? | NONE |
| ALT-DEP | ¿A1/A2 dependen de B o de componentes compartidos? | t−1–t3 | Grafo transitivo y consumidores | ? | NONE |
| ALT-F* | ¿A1→A2 satisface F*? | t3,t7,t8 | Oráculo ciego, resultado, margen equivalencia | ? | NONE |
| ORACLE | ¿F* y oráculo permanecen invariantes y ciegos? | t−1–t8 | Versión/hash, cegamiento, protocolo | ? | NONE |
| EXT | ¿Frontera externa identificada y cubierta? | t−1–t3 | Inventario servicios y límites | ? | NONE |

Un canal instalado no basta para accesibilidad. C_dep es solo una parte de DEP y no equivale a A_f*. App es distinto de A_f*.

## 4. Matriz ruta × predicados × tiempo × evidencia × cobertura

| Ruta | Secuencia candidata | Predicados necesarios | Ventana | Evidencia mínima | Estado | Cobertura |
|---|---|---|---|---|---:|---|
| Rτ2 | S0→adaptador→τ2/F1→F2→destino | ID, REL, COND, AUTH, RES, DEP, BLOCK; luego APP | t−1…t8 | Snapshots, contratos, permisos, recursos, logs, oráculo | ? | NONE |
| RA12 | S0→A1→artefacto→A2→destino | Identidad A1/A2, REL, COND, AUTH, RES, DEP, BLOCK, F* | t−1…t8 | Catálogo, grafo, snapshots, prueba funcional | ? | NONE |
| Rshared | Rτ2 o RA12 vía dependencia compartida | Predicados ruta + invariancia/estado dependencia | t−1…t8 | Grafo transitivo, diffs, recursos y comportamiento | ? | NONE |
| Rexternal | Ruta que usa servicio externo | Predicados ruta + contrato externo y disponibilidad | t−1…t8 | Inventario, versión, telemetría y límites | ? | NONE |
| Runknown | Cualquier ruta no enumerada en U_G | Cobertura universo y búsqueda exhaustiva | t−1…t8 | Justificación catálogo, enumeración y límites | ? | NONE |

Son rutas candidatas abstractas, no rutas técnicas descubiertas. Runknown se conserva para impedir inferir exhaustividad del catálogo propuesto.

## 5. Reglas de propagación 1/0/?

Para una ruta con predicados necesarios:
- Ruta=0 solo si al menos un predicado necesario es 0 con evidencia válida y cobertura suficiente.
- Ruta=1 solo si todos los predicados necesarios son 1 y la secuencia, identidad y orden temporal están verificados.
- Ruta=? en cualquier otro caso, incluido predicado desconocido, conflicto de evidencia o cobertura insuficiente.

Para el conjunto:
- Reach=1 si existe al menos una ruta 1.
- Reach=0 solo si todas las rutas del universo relevante son 0 y el universo está exhaustivamente cubierto.
- Reach=? si no hay ruta confirmada y queda alguna ruta ?, ruta desconocida o cobertura incompleta.

Para alternativa funcional:
- F_alt=1 si al menos una ruta alternativa confirmada satisface F* con oráculo válido.
- F_alt=0 solo si todas las rutas funcionalmente substituibles del universo definido están descartadas con cobertura exhaustiva.
- F_alt=? si quedan rutas, dependencias o servicios no inventariados o evidencia insuficiente.

Verdad estructural y observación permanecen separadas. Una observación 0 no equivale a verdad 0 si sensibilidad/cobertura no es suficiente.

## 6. Estado de cobertura en este corte

| Objeto | Estado | Motivo |
|---|---|---|
| Universo real de componentes | PARTIAL; cobertura efectiva NONE | Solo roles candidatos, sin inventario |
| Grafo de dependencias | PARTIAL; cobertura efectiva NONE | Sin SBOM, manifiesto, runtime ni relaciones observadas |
| Predicados A_f* | INDETERMINATE | Sin evidencia de identidad, relación, condiciones, autorización, recursos, dependencias y bloqueos |
| Ruta focal Rτ2 | INDETERMINATE | No hay evidencia de ruta completa implementada |
| Ruta alternativa RA12 | INDETERMINATE | No se verificó presencia ni ausencia/funcionalidad |
| Dependencias compartidas | INDETERMINATE | Sin grafo transitivo |
| R0 (sin alternativa) | NO CLASIFICABLE | F_alt,0=?; catálogo no exhaustivo |
| R1 (alternativa estable) | NO CLASIFICABLE | Sin evidencia pre/post de no-afectación |
| R2 (alternativa afectada) | POSIBLE, NO OBSERVADO | Vía plausible; no hay evidencia de ocurrencia |
| Reach_H | ? | No hay ruta confirmada ni universo exhaustivamente descartado |
| F_alt,0 | ? | No se probó presencia ni ausencia funcional |
| MD-C1 / MD-C2 / MD-C4 | OPEN | Manifiesto, primera etapa focal y no-afectación sin evidencia técnica |
| AUD-005 / AUD-007 | OPEN | Cobertura/Reach y verdad estructural vs identificación observacional pendientes |

## 7. Evidencia necesaria para cambiar estados

Cada evidencia futura deberá registrar: evidence_id, source, component/edge/predicate, unit_id, time, version, hash, method, observer, blinding, coverage_scope, error_profile, result (1/0/?) y limitations.

Mínimos:
1. Manifiesto real de instalación y SBOM del adaptador/runtime.
2. Snapshots S_preB/S_postB/S_rollback comparables.
3. Grafo transitivo con consumidores, interfaces y recursos compartidos.
4. ACL/permisos y cambios de autorización.
5. Contratos/precondiciones de τ2/F1/F2, A1/A2 y S0.
6. Oráculo F* versionado, ciego e independiente.
7. Pruebas de comportamiento de rutas y equivalencia pre/post B con margen justificado.
8. Inventario de servicios externos y límites de observabilidad.
9. Evidencia de cobertura del catálogo de rutas, granularidad y horizonte.

No se asignan resultados hipotéticos ni probabilidades a estas evidencias.

## 8. Conclusión y límites

El diseño permite definir un esquema finito de auditoría, pero todavía no un DGP técnico finito y exhaustivo. U_G es una lista de roles y rutas candidatas; los componentes reales, dependencias transitivas y alternativas funcionales no están identificados. No se puede clasificar R0/R1/R2 como escenarios observados, afirmar F_alt,0=0 ni cerrar Reach.

La decisión metodológica correcta es mantener Reach=?, F_alt,0=?, A_f*=? y MD-C1/MD-C2/MD-C4 abiertos. Esto refleja los límites de cobertura disponibles.

**Siguiente bloque:** fijar el contrato de frontera y granularidad de U_G (qué cuenta como componente, dependencia, ruta funcionalmente substituible, servicio externo, versión y recurso compartido), y diseñar el protocolo de evidencia/cobertura para completar el inventario sin confundir búsqueda finita con exhaustividad ontológica.

**Prohibición:** no ejecutar, instalar, simular, generar datos ni marcar contratos PASS en este bloque.
