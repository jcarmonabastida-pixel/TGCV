# C10-S — Alcance semántico y criterio de exclusión basal para Need_preZ

**ID:** C10-S-B1-PREZ-EXCLUSION-SCOPE-CONTRACT-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** CONTRACT_PROPOSAL / USER_ACCEPTED_PARENT_PRINCIPLE / NOT_APPROVED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Objeto y anclajes

Este contrato propone el alcance mínimo que permite estipular `Need_preZ=0` sin equiparar ausencia de declaración con ausencia de objetivo. Se subordina a la definición funcional de Need_preZ del contrato de adjudicación B1, la especificación candidata de entidad solicitante B1, la decisión de una B1 por UE vinculada a una instancia lógica de servicio aislada, y las reglas vigentes de truth y adjudicación.

La definición funcional focal permanece: antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

## 2. Alcance semántico focal propuesto

Para decidir pertenencia del objetivo focal no es necesario enumerar todos los propósitos posibles de B1. El universo pertinente se limita a **la especificación basal, en t−1, de los objetivos de B1 relativos a mantener disponible la función del servicio lógico vinculado a esa B1/UE, conforme a la definición funcional versionada de Need_preZ**.

El alcance se identifica por:
1. entidad B1 y UE vinculadas unívocamente conforme a la decisión de cardinalidad;
2. instancia lógica de servicio asignada y su versión;
3. relación B1–servicio declarada para esa unidad;
4. definición funcional/versionado exacto del objetivo focal.

No abarca todos los objetivos de B1, todas sus necesidades posibles ni toda la demanda del servicio. Tampoco se reduce a una petición concreta o a la oportunidad estandarizada del harness.

"Universo cerrado" significa aquí el alcance de la especificación basal de objetivos de B1 respecto de esa relación B1–servicio; no una ontología exhaustiva de todos los objetivos posibles de una entidad.

## 3. Vías admisibles para estipular truth=0

### 3.1 Exclusión focal explícita — vía mínima

La especificación basal reservada afirma expresamente que el objetivo funcional focal no pertenece a los objetivos basales de B1 respecto de la instancia lógica de servicio vinculada, en t−1. La afirmación debe estar vinculada a B1/UE/servicio/versiones y formar parte de la truth reservada del DGP.

### 3.2 Enumeración exhaustiva del alcance B1–servicio — vía opcional

La especificación basal declara que el conjunto de objetivos de B1 respecto de la relación con ese servicio está completo para t−1, enumera su contenido y no incluye el objetivo focal. La exhaustividad debe ser una propiedad explícita de la estipulación generadora; nunca se infiere de un registro aparentemente completo, un campo vacío o la ausencia de una mención.

Ambas vías representan exclusión positiva en la truth. La segunda no es inferencia por silencio: incluye una afirmación explícita de completitud y una enumeración cerrada. La decisión de admitir ambas o mantener solo la vía focal queda abierta.

## 4. Lo que no permite truth=0

No son exclusión:
- ausencia de declaración o documento observable;
- campo omitido, vacío, nulo o no materializado;
- ausencia de solicitudes, intentos, recepción, admisión u oportunidad estandarizada;
- falta de instalación, habilitación, disponibilidad, capacidad o accesibilidad;
- ausencia de déficit o interrupción: el objetivo puede estar satisfecho;
- no inclusión en un registro cuya exhaustividad no esté afirmada;
- ausencia o fallo de la instancia de servicio o relación B1–servicio;
- defecto técnico del generador o del paquete.

Si la identidad, versión, alcance o integridad de la estipulación falla, la unidad queda bloqueada como defecto de integridad, no se fuerza a truth=0 ni truth=?. Si la estipulación es válida pero genuinamente no determina pertenencia/exclusión, corresponde truth=?.

## 5. Truth=0 no equivale a observed=0

**Truth=0** es una estipulación reservada del generador: exclusión focal explícita o enumeración exhaustiva declarada que excluye el objetivo. No requiere que el adjudicador disponga de una fuente.

**Observed=0** exige evidencia afirmativa admisible, pre-Z, con identidad, versión, autoridad, alcance y cobertura demostrados, suficiente para respaldar que el objetivo no forma parte de la especificación basal. Una declaración negativa focal o una declaración observable de alcance exhaustivo podrían servir si el contrato de fuentes las admite.

La estipulación reservada, la etiqueta truth, la marca interna de exhaustividad y metadatos que revelen la etiqueta no se entregan a E1/E2. La falta de evidencia o la imposibilidad de demostrar cobertura produce observed=?, nunca observed=0. El modelo de observación deberá representar las fuentes sin copiar truth ni filtrar metadatos reservados; queda fuera de este contrato.

## 6. Casos abstractos de prueba (no son unidades ni registros)

| Caso | Truth / observado | Regla |
|---|---|---|
| Estipulación reservada incluye el objetivo | Truth=1 | Inclusión explícita |
| Estipulación reservada excluye el objetivo | Truth=0 | Exclusión focal explícita |
| Enumeración declarada completa no contiene el objetivo | Truth=0 | Exhaustividad afirmada |
| Campo ausente o vacío | No asigna truth=0 | Omisión no es exclusión |
| Expediente observable sin mención y cobertura desconocida | Observed=? | Ausencia de evidencia |
| Truth=1 pero no hay fuente observable suficiente | Truth=1; Observed=? | Error/ausencia de observación |
| Truth=0 pero adjudicador no recibe evidencia negativa suficiente | Truth=0; Observed=? | No filtrar truth |
| Estipulación válida declara indeterminación | Truth=? | Indeterminación generadora |

## 7. Gates pendientes

Antes de congelar el contrato:
1. aceptar el alcance focal B1–servicio de §2;
2. aceptar la exclusión focal explícita como vía mínima de truth=0;
3. decidir si se admite también enumeración exhaustiva;
4. cerrar requisitos de identidad, versión y completitud.

Después se reconciliará la representación técnica con el paquete analítico reservado y el maestro DGP. Solo entonces se definirá la composición de estados en el roster, sin prevalencias arbitrarias; posteriormente se diseñará el modelo de observación.

## 8. Dictamen

**FOCAL B1–SERVICE SCOPE PROPOSED / EXPLICIT NEGATIVE ATTESTATION SUFFICIENT FOR TRUTH=0 / EXHAUSTIVE ENUMERATION OPTIONAL AND OPEN / OBSERVED NEGATIVE EVIDENCE REMAINS SEPARATE AND COVERAGE-DEPENDENT.**

Este documento no modifica decisiones aceptadas, RMA, Evidence→Claim Matrix, STATUS, población, estimandos, contratos congelados ni DGP ejecutable. No crea roster, IDs, truth, fuentes, snapshots, cobertura, fixtures o código. No ejecuta validadores, DGP, simulación ni replay.

`scientific_execution=false`; `execution_authorized=false`.
