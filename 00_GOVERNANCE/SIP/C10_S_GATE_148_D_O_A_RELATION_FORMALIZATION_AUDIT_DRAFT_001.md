# C10-S — Gate 148: auditoría de formalización de la relación D/O/A

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** DOCUMENTARY_RECONCILIATION / RELATION_PARTIALLY_FORMALIZED / USER_DECISION_PENDING / NO_NEW_DEC / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Objeto y precedencia

Formalizar la relación entre las tres dimensiones aceptadas en R147-B sin modificar DEC-C10-068/101/102, §§49–50 ni añadir semántica al microdominio. Esta auditoría es documental y lógica. No acepta §51, no selecciona parámetros ni autoriza implementación.

Fuentes reconciliadas:
- DEC-C10-068 y `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`;
- `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`;
- DEC-C10-102;
- §§49–50 de `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`;
- Gates 145, 147-A y 147-B.

## 2. Distinción que gobierna la formalización

No son el mismo predicado:

1. **Validez declarativa de configuración (D_valid):** cumplimiento de RUL-SVC-ENABLE-PROFILE-01:
   `ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}`.
   La regla es una implicación, no una equivalencia. Si ENABLED=false, esta RUL no restringe PROFILE. No se añade la implicación inversa ni se atribuye semántica diferenciada a STANDARD/READ_ONLY.
2. **Habilitación declarada (D_enabled):** valor de PAR-SVC-ENABLED, distinto de la validez de la regla. Declara si el servicio debe aceptar solicitudes.
3. **Disponibilidad operativa efectiva (O):** condición funcional runtime derivada de los mecanismos constitutivos enumerados en §50 (proceso/módulo, listener/socket/superficie y dependencias). La evidencia S3 no define O; solo puede informar sobre ella.
4. **Capacidad efectiva de admisión (A):** capacidad del servicio para admitir solicitudes bajo la configuración declarada y las condiciones operativas/recursos pertinentes. No es el resultado de una solicitud aislada ni equivale a procesamiento, respuesta, Outcome o Value.

D_valid no equivale a O ni a A. D_enabled tampoco demuestra O/A. O no autoriza a ignorar D_enabled. Un servicio técnicamente disponible puede estar correctamente no habilitado. Un servicio habilitado puede carecer de disponibilidad o capacidad efectiva.

## 3. Relación lógica mínima derivable sin ampliar el contrato

Se puede establecer una relación de condiciones necesarias, no una equivalencia universal:

- Si `D_enabled=false`, la función declarada es no admitir; la disponibilidad técnica O puede seguir siendo verdadera, pero A_B1 no debe interpretarse como permiso para admitir.
- Si `D_enabled=true` y `O=false`, la admisión efectiva no está disponible.
- Si `D_enabled=true` y `O=true`, todavía puede faltar capacidad efectiva suficiente; por tanto A no se deduce automáticamente.
- Si `D_enabled=true`, `O=true` y la capacidad pertinente es suficiente, la admisión puede ser funcionalmente posible, sujeto al contrato de servicio que siga aplicando.

Por tanto, las condiciones `D_enabled=true`, `O=true` y capacidad suficiente son candidatas a condiciones necesarias para A=1. No se declara que su conjunción sea universalmente suficiente: §§49–50 no fijan umbral de capacidad, carga, política de concurrencia ni protocolo completo de petición. No se inventan esos parámetros.

## 4. Tabla de estados conceptuales

| D_enabled | O | Capacidad pertinente | Interpretación admisible |
|---|---|---|---|
| false | true | suficiente | Runtime disponible; servicio declarado no habilitado; no admitir |
| false | false | insuficiente o no evaluable | Declarado no habilitado; runtime también indisponible; no colapsar causas |
| true | false | irrelevante/no alcanzable | Habilitado declarativamente; indisponibilidad runtime impide admisión |
| true | true | insuficiente | Servicio operativo en sentido runtime, pero capacidad de admisión insuficiente |
| true | true | suficiente | Admisión funcionalmente posible, no prueba por sí sola procesamiento o beneficio |
| true | ? | ? | Truth de O/A no determinada por la especificación; no inferirla de ausencia S3 |

La tabla es lógica y no introduce estados físicos, cargas, umbrales ni escenarios nuevos.

## 5. Solapamiento que debe evitarse

§50 enumera capacidad/recursos como familia de mecanismos runtime cuando alteran la capacidad funcional de admisión. R147-B distingue O de A. Para evitar doble contabilización:

- el recurso/capacidad es un mecanismo o condición causal del entorno;
- O es el estado resumido de disponibilidad runtime;
- A es la capacidad funcional resultante de admisión bajo la configuración y condiciones aplicables.

Un mismo mecanismo puede afectar O y A, pero no crea dos transiciones truth independientes por el mero hecho de aparecer en ambas relaciones. La transición truth se define por el cambio efectivo en la dimensión funcional pertinente; R144-A gobierna simultaneidad y suborden. La provenance conserva el antecedente.

## 6. Separación respecto de V_cont y del contrato RUL

DEC-C10-068 define la regla constitutiva declarativa y sus contrastes. DEC-C10-102 define Truth=1/0/? para el cumplimiento de la regla funcional ENABLED/PROFILE durante el intervalo. §§49–50, a su vez, incluyen mecanismos runtime que pueden impedir/restaurar capacidad funcional de admisión y exigen considerar la función efectiva.

La relación exacta entre:
- cumplimiento de RUL-SVC-ENABLE-PROFILE-01;
- función efectiva de admitir/no admitir conforme a ENABLED;
- disponibilidad operativa O;
- capacidad A;
- adjudicación A_B1/V_cont,

no puede declararse cerrada solo con la frase de DEC-C10-102. Debe mantenerse la distinción entre validez de la configuración declarativa y cumplimiento de la función de servicio en operación. No se debe reinterpretar DEC-C10-102 como si RUL fuese una regla de uptime, ni reducir §§49–50 a la mera validez del paquete declarativo.

**Hallazgo L148-01:** existe una brecha de articulación entre la regla constitutiva declarativa de DEC-C10-068, la definición de trabajo de admisión B1 y la inclusión de mecanismos runtime en §§49–50. La relación conceptual D/O/A puede delimitarse, pero la proyección exacta a A_B1/V_cont necesita una aclaración lógica explícita y compatible con DEC-C10-102.

## 7. Propuesta R148-A para decisión

Aceptar únicamente estas reglas de articulación:

1. D_valid, D_enabled, O y A son predicados distintos; no se sustituyen entre sí.
2. D_valid se evalúa exclusivamente con RUL-SVC-ENABLE-PROFILE-01 y conserva su implicación unidireccional.
3. D_enabled=false implica que la función declarada es no admitir, aunque O sea verdadera.
4. D_enabled=true no basta para concluir admisión: O y la capacidad efectiva pertinente deben permitirla.
5. O y A no se infieren de una petición individual ni de S3 sin truth generada; S3 es evidencia imperfecta.
6. Los mecanismos runtime/recursos pueden afectar O/A; sus antecedentes se conservan sin duplicar transiciones truth.
7. La relación formal de estos predicados con A_B1 y la regla de DEC-C10-102 se mantiene abierta hasta reconciliar expresamente si V_cont adjudica solo la validez declarativa o la función efectiva de servicio definida por §§49–50. No se modifica DEC-C10-102 por inferencia.

## 8. Estado y límites

- Relación conceptual D_valid/D_enabled/O/A: delimitada.
- Condiciones necesarias de admisión: identificadas, sin suficiencia universal afirmada.
- Solapamiento recurso–O–A: identificado.
- Proyección exacta a A_B1/V_cont: OPEN (L148-01).
- Perfil STANDARD/READ_ONLY: sin semántica adicional.
- Protocolo, carga, umbral/capacidad, reloj, rejilla y §51: OPEN.
- Schema/código/tests/generación/simulación/ejecución: no autorizados.
- No se crea DEC-C10 ni se modifica DEC existente.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`


## 9. Addendum — aceptación expresa R148-A (2026-11-16)

El usuario acepta R148-A y la orientación de que V_cont adjudique la continuidad de la función efectiva del servicio B1, incluyendo interrupciones runtime que impidan realmente la admisión. La aceptación se registra íntegramente en `C10_S_GATE_148_R148A_ACCEPTANCE_EFFECTIVE_SERVICE_VCONT_SCOPE_DRAFT_001.md`.

La aceptación resuelve la dirección semántica del punto 7 de R148-A: A_B1/V_cont no se limita a la validez declarativa de RUL-SVC-ENABLE-PROFILE-01. Se mantienen separados D_valid, D_enabled, O y A; ENABLED=false impide admisión aunque O sea verdadera; ENABLED=true no basta para inferir disponibilidad/capacidad; y los mecanismos runtime solo alteran truth cuando afectan realmente la función B1.

**Límite de precedencia:** DEC-C10-102 sigue vigente y no se modifica. Su formulación expresa continuidad estricta de ENABLED/PROFILE, mientras que la orientación aceptada requiere incluir disponibilidad efectiva. La reconciliación normativa exacta queda abierta para Gate 149. No se reescribe la DEC ni se presume que la aceptación conversacional la haya sustituido.

Estado actualizado: `R148-A_ACCEPTED / EFFECTIVE_SERVICE_FUNCTION_SCOPE_ACCEPTED / DEC_C10_102_SCOPE_RECONCILIATION_REQUIRED`. No se crea DEC-C10 ni se autoriza schema, código, tests, fixtures, generación, simulación, estimación, calibración o ejecución.
