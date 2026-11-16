# C10-S — Gate 149: crosswalk normativo de V_cont y función efectiva B1

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** HISTORICAL_CROSSWALK_COMPLETE / SEMANTIC_DIRECTION_COMPATIBLE_WITH_CLARIFICATION / A_B1_INTERVAL_PREDICATE_NOT_FULLY_SPECIFIED / COMPLEMENTARY_DECISION_PROPOSED_NOT_ACCEPTED / NO_DEC_AMENDMENT / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Objeto y alcance

Determinar cómo reconciliar R148-A con DEC-C10-068/099/100/101/102/104, Gate 127 y Gate 134 sin reescribir decisiones aceptadas ni confundir regla declarativa, estado runtime, capacidad efectiva, truth, observación y evaluación.

La operación es documental. No cambia DEC existentes, el DGP, el harness, el schema, §51, parámetros temporales ni autorizaciones.

## 2. Autoridad recuperada y precedencia

### 2.1 DEC-C10-068 — contrato declarativo y frontera P0/P1

DEC-C10-068 acepta:
- PAR-SVC-ENABLED y PAR-SVC-PROFILE;
- RUL-SVC-ENABLE-PROFILE-01: ENABLED=true implica PROFILE∈{STANDARD, READ_ONLY};
- la implicación no es reversible; ENABLED=false no restringe PROFILE mediante esa RUL;
- P0 es el paquete declarativo; runtime, binarios, infraestructura, permisos efectivos, recursos y estado ambiental permanecen fuera de P0.

El contrato funcional de trabajo aclara que la instancia lógica admite solicitudes cuando está habilitada y expone PROFILE. La RUL declarativa no codifica por sí sola disponibilidad runtime, recursos, ejecución ni éxito de procesamiento.

**Consecuencia:** no es admisible reinterpretar RUL-SVC-ENABLE-PROFILE-01 como predicado de uptime o disponibilidad. La validez declarativa D_valid y el comportamiento de servicio son objetos distintos.

### 2.2 DEC-C10-099 — constructo V_cont

Selecciona V_cont como dimensión mínima provisional de Value y la describe como continuidad temporal de la capacidad efectiva del servicio que B1 pretende mantener disponible conforme al objetivo basal y al contrato funcional versionado (admitir conforme a ENABLED y exponer PROFILE). Excluye el flag ENABLED aislado, la admisión/respuesta de una oportunidad única, O-CONF/F* y accesibilidad/Reach/trayectoria.

**Consecuencia:** el constructo seleccionado ya es más amplio que la mera validez declarativa de RUL; su referente es la capacidad funcional efectiva del servicio, interpretada conforme al contrato.

### 2.3 DEC-C10-100 — truth por intervalo y agregación

Fija A_B1(i,k)∈{1,0,?}, media no ponderada de K intervalos iguales y bounds si existe truth UNKNOWN. La definición vincula A_B1 al cumplimiento funcional B1 conforme al contrato versionado y ENABLED/PROFILE. No determina por sí sola la lista exhaustiva de predicados funcionales ni el detalle de estados runtime.

### 2.4 DEC-C10-101 — ventana

Fija t0 inmediatamente después de Z, incluyendo provisión e instalación. Ningún evento de petición, instalación, verificación, C_dep, accesibilidad, Reach, selección o ejecución condiciona el inicio.

### 2.5 DEC-C10-102 — continuidad estricta

Fija el operador temporal sin periodo de gracia:
- 1 solo si la regla funcional ENABLED/PROFILE se cumple durante todo el intervalo;
- 0 ante al menos un incumplimiento funcional confirmado en cualquier instante;
- ? solo por indeterminación de truth propia del Generator.

No fija duración mínima de fallo, tolerancia, promediado intraintervalo ni parámetros físicos. La regla de continuidad estricta se conserva íntegra.

**Límite textual:** la formulación se refiere a ENABLED/PROFILE y no enumera expresamente O/A runtime. Leída aisladamente como mera evaluación de RUL-SVC-ENABLE-PROFILE-01, no detectaría la interrupción runtime con configuración intacta.

### 2.6 DEC-C10-104 — fronteras y UNKNOWN

Confirma que no modifica la definición V_cont, t0, continuidad estricta ni separación truth/observación. Fija asignación semiabierta de fronteras y prohíbe functional ? por omisiones de modelo/harness, missingness S3 o defectos de integridad. La truth completa y determinada debe resultar 1 o 0.

### 2.7 Gate 127 — consecuencia focal

Gate 127 identifica como consecuencia focal la disponibilidad temporal de la capacidad de admisión que B1 necesita mantener. Distingue esa consecuencia de procesamiento/respuesta, éxito de negocio, O-CONF y Value contextual general. Advierte que la equivalencia con V_cont requiere estipulación explícita en el DGP y que no debe derivarse solo del nombre.

### 2.8 Gate 134 — benchmark y conformidad

Gate 134 afirma que la semántica temporal de V_cont ya está decidida y que el harness actual no acredita continuidad estricta porque no conserva secuencia temporal completa de eventos/estados. Mantiene el benchmark binario como baseline metodológico parcial, no como implementación confirmatoria completa. Su lectura de DEC-C10-102 está centrada en ENABLED/PROFILE y no resuelve la inclusión normativa de mecanismos runtime aceptada después en Gates 147–148.

### 2.9 Gates 147–148 — ampliación semántica aceptada

R147-A/B y R148-A aceptan que:
- EventHistory contiene truth funcional, no un registro indiscriminado de proceso/evidencia;
- D_valid, D_enabled, O y A son predicados distintos;
- los mecanismos runtime solo alteran truth cuando afectan realmente la función B1;
- V_cont/A_B1 debe representar la continuidad de la función efectiva B1, incluyendo interrupciones runtime que impidan realmente la admisión;
- no se modifican por inferencia DEC-C10-068 ni DEC-C10-099…104;
- la articulación normativa con DEC-C10-102 queda expresamente abierta.

## 3. Dictamen de compatibilidad

**No existe incompatibilidad entre el constructo V_cont de DEC-C10-099 y la dirección semántica de R148-A.** DEC-C10-099 ya apunta a capacidad efectiva del servicio, no al flag ni a la validez declarativa aislada.

**Sí existe una insuficiencia de articulación entre la definición del predicado por intervalo A_B1 y la formulación abreviada de DEC-C10-102.** Si A_B1 se operacionaliza como evaluación exclusiva de RUL-SVC-ENABLE-PROFILE-01, la caída runtime con ENABLED/PROFILE intactos nunca haría A_B1=0, contradiciendo R148-A y la función efectiva aceptada. Si, en cambio, “regla funcional ENABLED/PROFILE” se interpreta como abreviatura del contrato funcional completo del servicio, la inclusión runtime es compatible, pero esa lectura no está explicitada ni suficientemente delimitada en DEC-C10-102.

La resolución más conservadora no consiste en alterar el operador temporal de DEC-C10-102, sino en aclarar el **contenido funcional de A_B1** y conservar DEC-C10-102 como regla de adjudicación temporal estricta aplicada a ese contenido.

## 4. Crosswalk de predicados y consecuencia

| Objeto | Pregunta que responde | Papel en A_B1/V_cont |
|---|---|---|
| D_valid | ¿La configuración cumple RUL-SVC-ENABLE-PROFILE-01? | Condición declarativa; no prueba disponibilidad |
| D_enabled | ¿El servicio está declarado habilitado? | Determina si debe admitir solicitudes |
| O | ¿Están disponibles los mecanismos runtime constitutivos pertinentes? | Condición operativa, solo relevante según la función requerida |
| A | ¿Puede el servicio realizar efectivamente el comportamiento de admisión requerido por la configuración? | Resultado funcional central |
| A_B1(i,k) | ¿Se mantuvo durante todo el intervalo la función B1 estipulada? | Truth por intervalo 1/0/? |
| V_cont_truth | ¿Qué fracción temporal de intervalos cumple A_B1? | Agregación de DEC-C10-100 |

La relación no debe codificarse como equivalencia universal `A_B1 = D_valid ∧ D_enabled ∧ O`. Esa fórmula sería errónea al menos porque:
- D_valid es una implicación sobre PROFILE, no la habilitación misma;
- cuando D_enabled=false, la función declarada es no admitir, que puede ser comportamiento correcto, no necesariamente fallo;
- la disponibilidad runtime solo afecta la verdad si impide el comportamiento que el contrato exige en ese estado;
- capacidad, dependencias y mecanismos constitutivos deben evaluarse según su efecto funcional, no por señales técnicas aisladas.

## 5. Precisión necesaria: qué cuenta como fallo runtime

La regla coherente con las decisiones es:

> Un mecanismo runtime/ambiental afecta A_B1 únicamente cuando, en el estado declarativo vigente y bajo el contrato funcional de servicio aplicable, su condición impide que la instancia realice el comportamiento que B1 requiere mantener disponible durante ese intervalo.

Consecuencias:
1. ENABLED=true y un fallo confirmado de proceso/listener/dependencia/capacidad que impide admitir solicitudes: incumplimiento funcional del intervalo.
2. ENABLED=true y runtime técnicamente disponible: no basta para truth=1 si la capacidad efectiva de admisión sigue impedida por otra condición constitutiva.
3. ENABLED=false: el comportamiento requerido por ENABLED es no admitir. No se debe clasificar automáticamente como fallo de admisión la ausencia de admisión cuando está declarada deshabilitación.
4. Si ENABLED=false y el runtime está caído, no se puede adjudicar automáticamente el efecto sobre A_B1 sin especificar qué comportamiento adicional exige el contrato en estado deshabilitado (por ejemplo, exposición de PROFILE). Ese detalle no está resuelto en DEC-C10-068.
5. Una petición aislada, un rechazo, un log, un reinicio o una señal S3 no determinan por sí solos una transición general. Se requiere truth generada del efecto funcional.
6. La interrupción confirmada que impide la función requerida cuenta en cada intervalo intersectado conforme a DEC-C10-102/104; no hay grace period ni tolerancia intraintervalo.

## 6. Propuesta de resolución documental — complemento, no enmienda temporal

Se recomienda una decisión complementaria (candidata DEC-C10-105; ID provisional, no asignado ni creado) que:
- explicite que A_B1(i,k) representa cumplimiento temporal de la función efectiva del servicio B1 conforme al contrato versionado, y no solo la validez aislada de RUL-SVC-ENABLE-PROFILE-01;
- identifique la conformidad declarativa ENABLED/PROFILE como componente necesario del comportamiento requerido, sin convertir D_valid en disponibilidad;
- incluya mecanismos runtime/recursos únicamente cuando impidan el comportamiento funcional requerido por el estado declarativo vigente;
- conserve el tratamiento correcto de ENABLED=false: no admitir puede ser el comportamiento esperado, por lo que no se etiqueta automáticamente como fallo;
- mantenga intactos el operador de continuidad estricta de DEC-C10-102, la ventana t0 de DEC-C10-101, la agregación/bounds de DEC-C10-100 y la frontera/UNKNOWN de DEC-C10-104;
- mantenga separados truth_dgp, observed_evidence S3/proceso y evaluación posterior;
- establezca que las omisiones del Generator/harness no son functional ? y deben corregirse como defectos de especificación/implementación.

No se propone cambiar el texto histórico de DEC-C10-102 ni reinterpretar la RUL como uptime. El complemento aclararía el referente de A_B1 al que se aplica el operador temporal ya aceptado.

## 7. Cuestiones que permanecen abiertas

Antes de aceptar un complemento, se requiere resolver documentalmente:
- comportamiento funcional exigido cuando ENABLED=false más allá de “no admitir” (especialmente PROFILE exposure);
- qué componentes/dependencias/recursos son constitutivos en el microdominio, según §§49–50, sin introducir redundancia, SLA, protocolos o políticas no aprobados;
- qué condición de capacidad basta para afirmar que la admisión es funcionalmente posible, sin elegir carga/umbral numérico;
- cómo el Generator representa transiciones verdaderas y potenciales sin mezclar PROCESS_EVENT con EventHistory;
- cómo se asigna una interrupción que cruza intervalos conforme DEC-C10-104;
- cómo se conserva la identidad/versión del contrato funcional a lo largo de la historia.

No se fijan reloj, rejilla, T*, Δ, K, resolución, duración mínima, carga, umbral, calibración S3, schema ni algoritmo.

## 8. Dictamen final y siguiente gate

- Constructo V_cont efectivo de DEC-C10-099: COMPATIBLE con R148-A.
- Operador temporal estricto de DEC-C10-102: se conserva sin cambio.
- Definición exacta de A_B1 por intervalo: requiere aclaración complementaria para incluir runtime sin convertir RUL en uptime.
- DEC-C10-104: permanece íntegra y aplicable a fallos funcionales confirmados que afecten intervalos.
- Gate 134: sigue siendo válido respecto a la no conformidad del harness binario; no se eleva ese baseline a confirmación de V_cont completo.
- No se modifica ninguna DEC existente ni se crea DEC-C10-105 en este Gate.

**Gate 150 propuesto:** completar el contrato lógico de A_B1 en los estados ENABLED=true y ENABLED=false, precisar la frontera funcional de O/A sin introducir semántica ajena al DGP y redactar, si procede, el complemento decisional para aceptación expresa.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
