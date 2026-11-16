# C10-S — Gate 147-B: matriz de cobertura y clasificación del catálogo B1 §§49–50

**Fecha:** 2026-11-16  
**Base documental:** `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, §§49–50; Gate 145; Gates 139 y 144; aceptación R147-A y R147-B.  
**Estado:** DOCUMENTARY_AUDIT / COVERAGE_PARTIAL / FUNCTIONAL_RELATION_OPEN / §51_OPEN / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Resultado ejecutivo

El inventario de §49 y el catálogo finito de §50 cubren las cinco familias explícitas de transición B1, pero no constituyen todavía un contrato completo de la relación entre configuración declarativa, disponibilidad operativa efectiva y capacidad de admisión. La aceptación R147-B permite clasificar los elementos sin confundirlos, pero no resuelve las reglas necesarias/suficientes que derivan capacidad de admisión.

Se conserva el alcance de §50: ENABLED/PROFILE; proceso/módulo; listener/socket/superficie de ingreso; dependencias solo cuando afecten capacidad funcional de admisión; capacidad/recursos solo cuando afecten esa capacidad. No se amplía el DGP mediante la mera enumeración de señales.

## 2. Matriz de cobertura

| Familia / elemento de §§49–50 | Dimensión truth candidata | Papel causal/funcional | Observed evidence posible | Dictamen / laguna |
|---|---|---|---|---|
| ENABLED | Configuración declarativa | Estado declarativo que gobierna admisión | Config snapshots/logs | Incluido explícitamente; conservar regla declarativa sin convertirla en equivalencia con disponibilidad |
| PROFILE | Configuración declarativa | Perfil declarado expuesto por el servicio | Config snapshots/logs | Incluido; STANDARD/READ_ONLY sin semántica adicional según §50 |
| Proceso/módulo | Disponibilidad operativa efectiva | Mecanismo runtime constitutivo cuando su estado altera disponibilidad B1 | Process/module telemetry, logs/traces | Incluido condicionalmente; falta formalizar cuándo un módulo es imprescindible |
| Listener/socket/superficie de ingreso | Disponibilidad operativa efectiva | Mecanismo de recepción/admisión | Socket/listener state, traces, logs | Incluido condicionalmente; falta definir qué superficie es constitutiva y cómo se trata degradación parcial |
| Dependencias | Disponibilidad operativa efectiva | Condición constitutiva solo si altera capacidad funcional de admisión | Dependency telemetry, logs/traces | Incluido condicionalmente; falta catálogo/versionado de dependencias funcionalmente necesarias |
| Capacidad/recursos | Disponibilidad operativa efectiva | Restricción funcional si impide/restaura admisión | Capacity/resource metrics and logs | Incluido condicionalmente; §49 separa stock, disponibilidad/asignación, demanda y consumo en antecedentes; falta regla de suficiencia/carga |
| Provisión/instalación/verificación | No son por sí mismas dimensión truth | Antecedentes causales/proceso que pueden modificar mecanismos o configuración | Deployment/install records, verification results | Cubiertos como antecedentes; no inferir transición por etiqueta o éxito de paso |
| Rollback/reinicio | No son por sí mismos dimensión truth | Acción/evento de proceso con posible efecto posterior | Process logs, deployment records | Cubiertos como antecedentes; solo el cambio efectivo resultante altera truth |
| Request opportunity/attempt | Ciclo discreto de solicitud, no estado continuo | Probe ex ante / intento de envío | Harness record | Ausencia no es fallo; oportunidad e intento distintos |
| Request received | Ciclo discreto | Recepción técnica; evidencia de resultado de canal | Gateway/server receipt | No equivale a admisión ni capacidad general |
| Request admitted/rejected | Resultado discreto de admisión bajo solicitud | Resultado observable/funcional de una petición concreta | Response/status record | No colapsar con ENABLED ni disponibilidad; reglas de protocolo y payload siguen abiertas |
| Request processing/response | Ciclo discreto | Etapas posteriores a recepción/admisión | Processing/response logs | No equivalen a ejecución transformacional, Outcome ni Value |
| Beneficiary consequence | Consecuencia separada | Posible resultado B1/beneficiario | Outcome records | No se deriva de respuesta técnica; regla/horizonte abiertos |
| Reach/selection/execution/F*/O-CONF/Outcome/Value | Fuera de A_B1 | Resultados de trayectoria/valor posteriores | Evaluator/measurement records | §49 los excluye de A_B1; mantener separación |

## 3. Reconciliación de las tres dimensiones

Se establece el siguiente mapa lógico, sin imponer todavía una función matemática:

1. **Configuración declarativa (D):** ENABLED/PROFILE.
2. **Disponibilidad operativa efectiva (O):** estado funcional runtime sintetizado a partir de los mecanismos constitutivos que realmente afectan disponibilidad.
3. **Capacidad efectiva de admisión B1 (A):** capacidad/resultado funcional de admisión conforme a D, O y las reglas de servicio aún por formalizar.

La dimensión A no debe confundirse con el resultado de una única petición. Las oportunidades estandarizadas permiten sondear capacidad bajo carga común; cada petición tiene además sus estados discretos (attempt, received, admitted/rejected, processing, response). La ausencia de intento no es evidencia de incapacidad.

No se afirma todavía que A sea una conjunción booleana simple D∧O, ni que todos los mecanismos runtime sean necesarios, ni que una única señal sea suficiente. Esas reglas requieren el contrato de servicio y el microdominio concreto.

## 4. No duplicación y simultaneidad

Cuando varios mecanismos cambian dentro de una misma transición funcional:
- se conserva provenance y atribución de todos los antecedentes pertinentes;
- se representa el cambio funcional una sola vez por cada transición de estado realmente estipulada;
- se aplica R144-A a simultaneidad atómica y suborden solo si hay estados intermedios funcionalmente relevantes;
- no se crea una transición separada por cada log, retry, reinicio o componente si el estado funcional no cambió entre ellos.

La deduplicación no debe borrar multiplicidad causal ni confundir una transición conjunta con causalidad identificada. El registro de antecedentes no prueba por sí solo qué mecanismo causó el cambio.

## 5. Incompatibilidades y lagunas detectadas

### L147-01 — Estado de admisión vs disponibilidad

§50 conserva la regla declarativa ENABLED=true/false y a la vez reconoce que mecanismos runtime pueden impedir/restaurar capacidad de admisión. R147-B acepta tres dimensiones, pero aún no existe regla formal que relacione D, O y A. Es la laguna principal.

### L147-02 — Perfil y admisión

PROFILE debe exponerse y mantenerse como configuración declarativa; STANDARD/READ_ONLY no reciben semántica adicional. No debe inferirse que PROFILE cambie la admisibilidad sin regla explícita. Su efecto sobre A queda limitado a lo que el contrato vigente estipule.

### L147-03 — Constitutividad runtime

No está completamente especificado cuándo un proceso, módulo, listener, dependencia o recurso es necesario para la disponibilidad B1, ni cómo se tratan degradación parcial, redundancia, failover o disponibilidad por componente. No introducir estos casos como hechos aprobados: son lagunas del catálogo que deben resolverse solo si pertenecen al microdominio estipulado.

### L147-04 — Carga y capacidad

§49 separa stock, disponibilidad/asignación, demanda y consumo. §50 solo incorpora capacidad/recursos cuando cambian la capacidad funcional de admisión. Falta definir qué representa el probe estandarizado, su carga y criterio de capacidad; esos parámetros permanecen abiertos.

### L147-05 — Solicitud y transición truth

El ciclo discreto está correctamente separado. Sin embargo, el contrato aún no fija completamente cómo un resultado de una petición concreta informa sobre la capacidad general de admisión. No usar un rechazo aislado como transición de estado general sin regla causal/funcional explícita.

### L147-06 — Estados intermedios y simultaneidad

R144-A define simultaneidad y suborden lógico, pero la identificación de estados intermedios que son funcionalmente relevantes depende del contrato de D/O/A. No resolverlo mediante timestamps, resolución S3 o serialización.

## 6. Dictamen

- **Cobertura de familias expresamente enumeradas en §50:** presente.
- **Separación truth / observed_evidence / evaluation:** preservada.
- **Separación D/O/A:** aceptada conceptualmente.
- **Relación formal D→O→A o interacción:** abierta.
- **Completitud generativa R146-D:** todavía no demostrada por el mero inventario; requiere catálogo de estados/transiciones y regla de generación cerrados.
- **§51, reloj, soporte, T*, Δ, K y calibración S3:** abiertos.
- **Schema, implementación, pruebas, generación y ejecución científica:** no autorizados.

## 7. Próxima operación

Gate 148 debe resolver, exclusivamente a nivel lógico, el contrato de relación entre D, O y A y los criterios de transición de cada dimensión. Debe empezar por reconciliar la regla declarativa ENABLED/PROFILE de §50 con los fallos runtime ya contemplados, sin introducir semántica adicional para PROFILE, protocolos, SLA, redundancia o degradación que no esté estipulada.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
