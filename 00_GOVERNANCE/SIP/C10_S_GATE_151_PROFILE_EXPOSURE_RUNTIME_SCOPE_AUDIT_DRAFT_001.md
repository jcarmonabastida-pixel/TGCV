# C10-S — Gate 151: alcance runtime de PROFILE exposure y cierre de L150-01

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** HISTORICAL_RECONSTRUCTION_COMPLETE / PROFILE_EXPOSURE_CONTRACTUAL_OBLIGATION_CONFIRMED / NO_INDEPENDENT_RUNTIME_MECHANISM_SPECIFIED / DGP_SCOPE_LIMIT_PROPOSED / R151_A_PENDING_ACCEPTANCE / NO_DEC / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Pregunta y criterio

Resolver L150-01 sin introducir interfaz, endpoint, canal, componente, dependencia o transición no contenidos en el DGP vigente. La pregunta no es si PROFILE debe exponerse —R150-A ya lo aceptó—, sino si el DGP especifica un mecanismo runtime por el que esa exposición pueda perderse de forma independiente de la función de admisión.

## 2. Reconstrucción de las fuentes vigentes

### 2.1 Contrato lógico del servicio, §§2–5 y §12

La unidad lógica versionada se define con una función abstracta: aceptar solicitudes cuando está habilitada y exponer el perfil operativo declarado. La identidad funcional no depende de host, proceso, contenedor o ubicación.

El contrato:
- define ENABLED y PROFILE como parámetros declarativos;
- restringe PROFILE a STANDARD/READ_ONLY solo cuando ENABLED=true;
- no define protocolo de petición completo ni interfaz para consultar/exponer PROFILE;
- no asigna mecanismo runtime independiente a la exposición del perfil.

Por tanto, “exponer PROFILE” es una obligación funcional del servicio lógico, no un endpoint ni una operación técnica ya especificada.

### 2.2 DGP temporal y de roles, §§49–50

§49 enumera runtime: proceso/módulo, listener/socket/superficie de recepción, dependencias y capacidad/recursos cuando sean constitutivos de admisión; caída, reinicio y recuperación. Su efecto expresamente catalogado es impedir/restaurar capacidad de admisión. La lista de solicitudes separa intento, recepción, admisión/rechazo, procesamiento y respuesta.

§50 acota las familias de transición a:
1. cambios efectivos ENABLED/PROFILE;
2. pérdida/recuperación de proceso/módulo;
3. pérdida/recuperación de listener/socket/superficie de ingreso;
4. pérdida/recuperación de dependencia solo si cambia la capacidad funcional de admisión;
5. insuficiencia/restauración de capacidad/recursos solo si cambia la capacidad funcional de admisión.

El mismo §50 vuelve a enunciar la función B1 completa —admitir cuando ENABLED=true, no admitir cuando ENABLED=false y exponer PROFILE declarado—, pero no añade una familia de transición runtime para pérdida independiente de exposición.

### 2.3 R150-A

R150-A acepta dos obligaciones funcionales de B1: comportamiento de admisión condicionado por ENABLED y exposición de PROFILE declarado, en ambos estados. La exposición permanece abstracta y no define mecanismo físico. La aceptación no autoriza completar por inferencia el catálogo runtime.

## 3. Dictamen

**El DGP actual no especifica un mecanismo causal/runtime que permita una pérdida de PROFILE exposure independiente de la capacidad de admisión.** No es lícito inventar uno ni deducirlo solo de que exista una obligación abstracta de exposición.

La función de exposición queda como parte del contrato lógico B1, pero su variación temporal independiente no forma parte del espacio de transiciones actualmente especificado.

Esto impone dos límites:

1. No se añade a EventHistory un estado o transición autónoma `PROFILE_EXPOSURE_AVAILABLE`, ni evento equivalente.
2. Una transición de proceso/módulo o listener/superficie solo afecta la exposición si el DGP ya estipula que esa transición hace indisponible la instancia lógica como servicio completo. §§49–50, por sí solos, describen su efecto sobre admisión y no autorizan atribuirle automáticamente pérdida de exposición.

En el DGP vigente, la exposición se conserva como obligación funcional abstracta asociada al estado de la instancia y al PROFILE declarado. La transición ENABLED/PROFILE ya existente conserva la identidad/versionado del perfil. No se presume que una señal técnica, un evento de proceso o un fallo de admisión demuestre por sí mismo una pérdida separada de exposición.

## 4. Propuesta R151-A — delimitación conservadora del espacio causal

Aceptar:
1. PROFILE exposure sigue siendo obligación funcional de B1, confirmada por R150-A.
2. El DGP actual no incluye una vía causal independiente ni una familia de transiciones para perder esa exposición.
3. No se añade un estado dinámico autónomo ni una transición runtime específica de exposición en EventHistory.
4. Las transiciones runtime existentes solo alteran truth de exposición si una estipulación explícita del DGP les atribuye indisponibilidad de la instancia lógica completa; tal atribución no se presume en Gate 151.
5. En ausencia de esa estipulación, los mecanismos runtime de §§49–50 se adjudican por el efecto ya definido sobre admisión; la obligación de exposición permanece parte del contrato lógico, sin variación causal independiente en el DGP.
6. Si una futura ampliación científica quiere estudiar fallos independientes de exposición, requerirá cambio explícito del DGP y nueva decisión; queda fuera de esta especificación confirmatoria.
7. No se transforma la falta de observación en UNKNOWN funcional ni se utiliza S3 para crear truth.

## 5. Implicación para A_B1 y EventHistory

A_B1 conserva el contrato compuesto aceptado en R150-A. Sin embargo, el soporte de transiciones dinámicas generado por el DGP vigente solo varía mediante las familias ya estipuladas en §§49–50. No se crea un eje dinámico de PROFILE exposure.

EventHistory debe conservar:
- estado declarativo ENABLED/PROFILE, identidad de instancia y versión;
- transiciones funcionales efectivas ya estipuladas;
- estado de admisión funcional derivado de ENABLED y de los mecanismos runtime catalogados;
- simultaneidad, suborden y persistencia conforme a R144-A;
- procedencia truth separada de PROCESS_EVENT, S3 y adjudicación.

No debe conservar un evento ficticio de exposición, ni convertir observaciones de proceso/listener en una transición autónoma de PROFILE exposure.

La obligación de exponer PROFILE permanece visible en el contrato funcional y en la definición de A_B1, pero sin inventar una dinámica independiente que el generador no posee.

## 6. Límites y cuestiones que siguen abiertas

R151-A no decide:
- si en una futura versión del DGP se quiere hacer variable la exposición de PROFILE;
- si una caída runtime determinada afecta a la instancia lógica completa además de la admisión;
- qué interfaz física permitiría observar PROFILE;
- reloj, rejilla, T*, Δ, K, duración mínima o calibración S3.

Estas cuestiones no bloquean el cierre lógico del alcance causal actual si se acepta expresamente que la pérdida independiente de exposición queda fuera del DGP vigente.

## 7. Estado y siguiente gate

- Obligación abstracta de exposición PROFILE: ACCEPTED por R150-A.
- Mecanismo runtime independiente de pérdida de exposición: NOT SPECIFIED IN CURRENT DGP.
- Familia dinámica autónoma en EventHistory: NO, salvo futura ampliación aprobada.
- Efecto de runtime sobre admisión: limitado a §§49–50.
- R151-A: propuesta pendiente de aceptación.
- DEC-C10-068/099/100/101/102/104: no modificadas.
- §51, reloj, T*, Δ, K y S3/calibración: OPEN.
- Schema, código, tests, fixtures, generación y ejecución: no autorizados.

**Gate 152 propuesto:** una vez aceptada R151-A, reconciliar el contrato compuesto A_B1 con EventHistory y redactar el complemento decisional candidato para aclarar el referente funcional al que se aplica la continuidad estricta de DEC-C10-102. No crear la DEC hasta aceptación expresa.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
