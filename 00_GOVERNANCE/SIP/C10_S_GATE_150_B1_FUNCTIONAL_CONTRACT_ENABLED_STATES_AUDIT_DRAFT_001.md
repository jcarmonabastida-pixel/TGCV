# C10-S — Gate 150: contrato funcional B1 en ENABLED=true/false y auditoría de exposición de PROFILE

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** HISTORICAL_RECONSTRUCTION_COMPLETE / ENABLED_STATE_CONTRACT_RECONCILED / PROFILE_EXPOSURE_REQUIREMENT_CONFIRMED / RUNTIME_COVERAGE_FOR_PROFILE_EXPOSURE_OPEN / PROPOSAL_R150_A_PENDING_ACCEPTANCE / NO_DEC / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Objeto y fuentes

Completar el contrato lógico B1 en ambos estados de ENABLED y comprobar si la exposición de PROFILE ya está estipulada. Reconstrucción documental de:
- DEC-C10-068 y `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`, §§2–5 y §12;
- DEC-C10-099;
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, §§49–50;
- DEC-C10-102/104;
- Gates 147-B, 148 y 149.

No se modifican decisiones aceptadas ni el DGP. No se introduce protocolo, endpoint, payload, respuesta, SLA, carga, umbral, política de errores ni nueva familia técnica.

## 2. Hallazgo histórico que resuelve ENABLED=false

La cuestión planteada en Gate 149 —si el contrato definía qué ocurre con PROFILE cuando ENABLED=false— ya está resuelta por el texto vigente y no requiere una regla nueva:

- El contrato funcional de DEC-C10-068 (§2) establece que la unidad acepta solicitudes cuando está habilitada y expone un perfil operativo declarado.
- DEC-C10-068 y la sección 4 del contrato lógico estipulan que RUL-SVC-ENABLE-PROFILE-01 solo restringe PROFILE cuando ENABLED=true. Con ENABLED=false, cualquier valor declarado del dominio queda fuera de la restricción de esa implicación.
- El contrato lógico §12 separa esta función abstracta del protocolo de petición, que permanece sin especificar.
- §§49–50 del contrato DGP dicen expresamente: admitir cuando ENABLED=true, no admitir cuando ENABLED=false y exponer PROFILE declarado. STANDARD/READ_ONLY no reciben semántica adicional.

Por tanto, no es correcto dejar PROFILE exposure como una cuestión enteramente ausente en ENABLED=false. La obligación abstracta de exponer el perfil declarado se aplica en ambos estados. No se deriva que PROFILE deba ser DISABLED cuando ENABLED=false ni que STANDARD/READ_ONLY tengan semánticas distintas.

## 3. Contrato funcional por estado

La función B1 es una función abstracta de servicio, no un protocolo físico:

### 3.1 ENABLED=true

Comportamiento requerido:
1. la configuración debe satisfacer RUL-SVC-ENABLE-PROFILE-01; por tanto PROFILE pertenece a {STANDARD, READ_ONLY};
2. el servicio debe admitir solicitudes;
3. debe exponer el PROFILE declarado.

Una violación declarativa de RUL, la incapacidad funcional confirmada de admitir o la incapacidad confirmada de exponer el perfil incumplen la función B1. La disponibilidad de proceso/listener o una señal S3 positiva no basta por sí sola para truth=1.

### 3.2 ENABLED=false

Comportamiento requerido:
1. el servicio no debe admitir solicitudes;
2. debe exponer el PROFILE declarado;
3. RUL-SVC-ENABLE-PROFILE-01 no impone restricción adicional sobre el valor de PROFILE en este estado.

Por consiguiente:
- la ausencia de admisión es comportamiento correcto, no fallo;
- una admisión efectiva cuando ENABLED=false contradice el comportamiento estipulado;
- no poder exponer el PROFILE declarado incumple la función abstracta, aunque la no-admisión sea correcta;
- cualquier PROFILE del dominio declarado sigue siendo admisible bajo la RUL; no se añade ENABLED=false ⇒ PROFILE=DISABLED.

La capacidad técnica de admitir mientras ENABLED=false no es, por sí sola, incumplimiento: lo relevante es el comportamiento funcional estipulado, que exige no admitir. No se especifica cómo se expresa una no-admisión en un protocolo.

## 4. Regla lógica candidata para A_B1

Sea el estado declarativo vigente en el instante t: E(t)=ENABLED(t), P(t)=PROFILE(t). Sea Admit(t) el predicado funcional abstracto de admisión y ExposeProfile(t) el predicado abstracto de exposición del valor PROFILE declarado.

La función instantánea requerida puede expresarse, como notación lógica y no como schema:

`F_B1(t) = ExposeProfile(t) AND ((E(t)=true AND RUL_OK(t) AND Admit(t)) OR (E(t)=false AND NOT Admit(t)))`

donde `RUL_OK(t)` representa únicamente el cumplimiento de `ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}`. No convierte la RUL en regla de uptime.

El contrato temporal estricto ya aceptado se aplica a esta función:
- A_B1(i,k)=1 si F_B1(t) se cumple durante todo el intervalo;
- A_B1(i,k)=0 si existe incumplimiento funcional confirmado en cualquier instante del intervalo;
- A_B1(i,k)=? solo por indeterminación propia de truth generada, no por falta de observación S3, omisión de harness o defecto de integridad.

Esta expresión no fija reloj, duración, rejilla, protocolo ni método de observación. Tampoco afirma que la verdad del Generator se derive de una petición aislada.

## 5. Matriz de estados lógicos

| ENABLED | PROFILE | Comportamiento de admisión requerido | Exposición de PROFILE | Lectura funcional |
|---|---|---|---|---|
| true | STANDARD | Admitir | Exponer STANDARD | Conforme si ambos comportamientos se cumplen |
| true | READ_ONLY | Admitir | Exponer READ_ONLY | Conforme si ambos comportamientos se cumplen; sin semántica adicional |
| true | DISABLED | La configuración viola RUL | Exponer valor declarado si el estado existe | Incumplimiento declarativo; no se legitima por runtime |
| false | STANDARD | No admitir | Exponer STANDARD | Puede ser conforme; RUL no lo restringe |
| false | READ_ONLY | No admitir | Exponer READ_ONLY | Puede ser conforme; RUL no lo restringe |
| false | DISABLED | No admitir | Exponer DISABLED | Puede ser conforme; no se deriva obligación adicional |

La tabla define comportamiento requerido, no estados de protocolo ni respuestas a solicitudes.

## 6. Límite detectado: cobertura de mecanismos runtime para PROFILE exposure

El contrato ya estipula la exposición de PROFILE, pero el catálogo §50 clasifica dependencias y capacidad/recursos como transiciones relevantes únicamente cuando cambian la capacidad funcional de admisión. §49 también define el runtime y los mecanismos principalmente en relación con la admisión. DEC-C10-099, por su parte, incluye exponer PROFILE en el referente de V_cont.

Se detecta una laguna de articulación, no una autorización para ampliar el catálogo:
- La imposibilidad funcional de exponer PROFILE es un incumplimiento del comportamiento B1 estipulado.
- No está completamente determinado qué mecanismos runtime, aparte de los que ya impidan la función global del servicio, pueden causar una pérdida de exposición sin afectar admisión.
- No se debe inventar un endpoint, canal de consulta, API, listener adicional ni dependencia específica.
- No se debe afirmar que toda caída de cualquier componente produce pérdida de exposición.
- Tampoco se puede ignorar la obligación de exposición porque el catálogo runtime se haya redactado alrededor de admisión.

**L150-01:** falta especificar, a nivel lógico del microdominio, si PROFILE exposure es una propiedad funcional continuamente disponible de la instancia y qué mecanismo constitutivo existente puede impedirla, sin definir todavía interfaz física. La obligación abstracta sí está confirmada; su realización causal/temporal y cobertura en EventHistory requieren cierre.

## 7. Propuesta R150-A para decisión

Aceptar:
1. La función B1 contiene dos obligaciones: comportamiento de admisión condicionado por ENABLED y exposición del PROFILE declarado.
2. ENABLED=true requiere admitir y exponer PROFILE; además, RUL exige PROFILE∈{STANDARD, READ_ONLY}.
3. ENABLED=false requiere no admitir y exponer PROFILE; la RUL no restringe el valor declarado.
4. STANDARD y READ_ONLY no reciben semántica diferenciada adicional.
5. La no-admisión esperada con ENABLED=false no es fallo; admitir efectivamente en ese estado sí contradice la función estipulada.
6. El incumplimiento confirmado de cualquiera de las obligaciones funcionales aplicables hace A_B1=0 en los intervalos afectados, bajo continuidad estricta; ? no es estado de conveniencia para evidencia faltante.
7. La exposición se mantiene abstracta: no se define endpoint, protocolo, payload ni mecanismo físico.

Mantener OPEN:
- si PROFILE exposure debe modelarse como propiedad continua del estado de servicio o como condición funcional evaluable en los eventos/estados ya estipulados;
- qué mecanismo constitutivo existente podría impedirla de forma independiente de la admisión;
- cómo se refleja esa pérdida en las transiciones funcionales de EventHistory sin crear un evento de proceso ni ampliar §§49–50 por inferencia.

## 8. Estado y siguiente operación

- Contrato lógico ENABLED=true: delimitado.
- Contrato lógico ENABLED=false: delimitado.
- PROFILE exposure en ambos estados: obligación ya presente, confirmada.
- Semántica adicional STANDARD/READ_ONLY: no añadida.
- RUL declarativa: preservada como implicación unidireccional.
- Función instantánea F_B1: propuesta para aceptación, no DEC ni schema.
- Runtime causal de pérdida de PROFILE exposure: OPEN (L150-01).
- DEC-C10-068/099/100/101/102/104: no modificadas.
- §51, reloj, T*, Δ, K, S3/calibración: OPEN.
- Implementación, pruebas, generación y ejecución: no autorizadas.

**Gate 151 propuesto:** resolver L150-01 estrictamente dentro del microdominio ya estipulado: determinar si la exposición de PROFILE comparte los mecanismos de disponibilidad ya catalogados o si su pérdida independiente está fuera del DGP actual. No introducir interfaz ni componentes nuevos. Después de esa resolución podrá prepararse un complemento decisional para A_B1 sin reescribir DEC-C10-102.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`


## 9. Addendum — aceptación expresa R150-A (2026-11-16)

El usuario acepta expresamente R150-A en los siete términos enumerados en §7. Se registra la aceptación semántica y lógica para el DGP sintético:

1. B1 contiene dos obligaciones funcionales: comportamiento de admisión condicionado por ENABLED y exposición del PROFILE declarado.
2. ENABLED=true requiere admitir y exponer PROFILE, con PROFILE∈{STANDARD, READ_ONLY} por RUL-SVC-ENABLE-PROFILE-01.
3. ENABLED=false requiere no admitir y exponer PROFILE; la RUL no restringe el valor declarado en este estado.
4. STANDARD y READ_ONLY no reciben semántica diferenciada adicional.
5. La no-admisión cuando ENABLED=false es comportamiento correcto; admitir efectivamente en ese estado es incumplimiento.
6. El incumplimiento confirmado de cualquiera de las obligaciones funcionales aplicables hace A_B1=0 en los intervalos afectados, sujeto a la continuidad estricta y las reglas temporales ya aceptadas. UNKNOWN no se usa para suplir evidencia observacional ausente, fallos del harness ni defectos de integridad.
7. La exposición de PROFILE permanece abstracta: no se define endpoint, protocolo, payload ni mecanismo físico.

**La aceptación no resuelve L150-01.** Continúan abiertos el carácter continuo de la exposición de PROFILE, los mecanismos constitutivos ya catalogados que podrían impedirla independientemente de la admisión y su representación como verdad funcional en EventHistory. No se amplían §§49–50 por inferencia.

No se crea ni modifica DEC-C10, schema, DGP numérico, reloj, rejilla, código, tests, fixtures ni harness. No se autoriza generación, simulación, estimación, calibración ni ejecución científica.

Estado: `R150_A_ACCEPTED_FOR_SYNTHETIC_DGP_LOGICAL_SEMANTICS / L150_01_OPEN / NO_DEC / NO_IMPLEMENTATION`.
