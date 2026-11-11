# C10-S — Especificación candidata B1: entidad solicitante sintética

**ID:** C10S-B1-REQUESTER-CANDIDATE-001  
**Versión:** Draft 001  
**Estado:** DRAFT / CANDIDATO ACEPTADO PARA DESARROLLO / NO INSTANCIA CERRADA  
**Fecha:** 2026-11-11  
**Rama:** research/c10-s-consolidation-draft · **PR:** #116  
**Autoridad:** DEC-C10-095; C10S-B-VALUE-MIN-001; P179/P182/P183; §224.  
**Ámbito:** variante B exclusivamente.

## 1. Decisión de alcance

Se acepta **B1 — entidad solicitante sintética del servicio** como tipo candidato de beneficiario para continuar el diseño de B. La aceptación no identifica una persona real, organización, sistema concreto ni instancia empírica; tampoco cierra todavía la instancia B, la cardinalidad, la demanda, el criterio de valoración o las dimensiones de Value.

A permanece intacta. No se modifica DEC-C10-068 ni el roster de Opción A.

## 2. Definición candidata

Una entidad solicitante sintética es una entidad lógica estipulada en el DGP de B que:
1. tiene una necesidad, objetivo o propósito relacionado con una solicitud antes de la asignación Z;
2. mantiene una relación explícita y versionada con una unidad lógica de servicio;
3. puede originar o estar representada por una solicitud dirigida al servicio;
4. puede experimentar una consecuencia atribuible al procesamiento, no procesamiento o resultado de esa solicitud;
5. puede ser el referente de una perspectiva de valoración fijada ex ante.

La entidad es sintética: su existencia y propiedades pertenecen a la verdad del DGP. No se afirma que represente a un usuario real ni que sus preferencias estén validadas empíricamente.

## 3. Separaciones semánticas obligatorias

| Concepto | Definición en B1 | No debe confundirse con |
|---|---|---|
| Entidad solicitante-beneficiaria | Entidad cuya necesidad/objetivo basal da lugar a la solicitud y cuya consecuencia se valora | Operador, evaluador, propietario técnico |
| Demanda basal | Necesidad/objetivo existente antes de Z | Solicitud emitida, selección, ejecución |
| Solicitud | Expresión/registro de una petición al servicio | Totalidad de la demanda o prueba de valor |
| Unidad lógica de servicio | C10S-SVC-REQUEST-PROCESSOR, bajo versión declarada | Beneficiario |
| Unidad experimental | Unidad a la que se asigna Z | Entidad solicitante, salvo relación explícita |
| Actor ejecutor | Actor/entidad que realiza operaciones si el DGP lo estipula | Solicitante o beneficiario por defecto |
| Evaluador | Rol que adjudica mediciones frente a truth | Beneficiario o solicitante |

La entidad solicitante y la entidad beneficiaria pueden ser la misma entidad lógica **por estipulación explícita de B1**. Esta identidad de rol es una característica candidata de B1, no una inferencia sobre Opción A. Si el DGP futuro distingue solicitante y beneficiario, deberá justificarlo y registrar la relación.

## 4. Relación temporal mínima

La secuencia semántica que debe poder representar B1 es:

- **Pre-Z:** entidad, relación con el servicio, elegibilidad y necesidad/objetivo basal.
- **Z:** asignación de la política experimental.
- **Post-Z:** provisión/intento/instalación/dependencias y estados de accesibilidad conforme al contrato causal.
- **Posteriormente:** oportunidad de formular/considerar/enviar solicitud, procesamiento y consecuencia.
- **Horizonte de valoración:** observación/adjudicación de la consecuencia para la entidad.

La secuencia no presupone que toda demanda genere una solicitud ni que toda solicitud sea procesada, seleccionada o ejecutada. La demanda no atendida debe permanecer en la población elegible y en el denominador pertinente.

## 5. Consecuencia para la entidad: delimitación sin operacionalizar

La consecuencia candidata debe referirse a la situación de la entidad solicitante respecto de su necesidad u objetivo basal. Puede consistir en progreso, cumplimiento, resolución o no resolución del propósito que motivó la solicitud. Esta delimitación es semántica y no elige aún un constructo operacional.

No se aprueba ninguna de las siguientes equivalencias:
- procesamiento técnico correcto = Value;
- conformidad técnica O-CONF = Value;
- solicitud enviada = necesidad satisfecha;
- solicitud procesada = objetivo alcanzado;
- transformación accesible = beneficio recibido;
- ausencia de solicitud = ausencia de demanda;
- no ejecución = Value cero.

El resultado técnico del servicio y la consecuencia para el solicitante deben medirse separadamente. La segunda no puede ser una recodificación del primero.

## 6. No circularidad y vías alternativas

La entidad, su elegibilidad y su demanda basal se estipulan antes de Z y no se redefinen en función de A_f*, ΔT_acc, Reach, selección, ejecución o resultado observado.

La regla de valoración se fija antes de observar los brazos y se aplica simétricamente. No se define Value como una función mecánica de accesibilidad ni como "haber completado" la transformación. Si existen vías de Z/paquete a la consecuencia que no pasan por accesibilidad (coste, demora, riesgo, calidad u otras), el ITT_Z sobre Value es efecto de política/paquete y no identifica por sí solo el efecto focal de accesibilidad.

## 7. Contrato de instancia pendiente

Antes de admitir B1 como instancia confirmatoria, la especificación debe cerrar:
1. identidad lógica y tipo de entidad solicitante, versión y provenance;
2. relación cardinal con unidad experimental y unidad de servicio;
3. elegibilidad y demanda/objetivo pre-Z, incluidos los estados de ausencia;
4. relación entre demanda y solicitud emitida;
5. consecuencia candidata y horizonte, sin equipararla a Outcome técnico;
6. perspectiva y autoridad de valoración;
7. dimensión o dimensiones V_j justificadas por esa consecuencia;
8. unidad, escala, baseline, regla de adjudicación, error y ausencia conforme a §224/P182/P183;
9. DAG de vías mediadas y alternativas;
10. estimandos y supuestos de identificación por dimensión.

No se asignan valores, preferencias, distribuciones, pesos, escalas, umbrales, tiempos, tasas ni parámetros en este documento.

## 8. Consecuencias para C/D/E

- **C / C-Value:** B1 reduce la elección del tipo de entidad; C todavía debe justificar demanda, consecuencia, perspectiva y dimensiones. Las fichas §224 siguen pendientes.
- **D:** deberá representar por separado entidad, demanda pre-Z, solicitud, servicio, unidad experimental, consecuencia y medición; no se aprueba todavía ningún schema físico ni fixture.
- **E:** deberá comprobar que demanda no desaparece por no uso, que Outcome técnico y Value son distintos, que la regla es estable, y que el Analyzer puede abstenerse ante ausencia/no identificación.

## 9. Dictamen

**B1 ACEPTADO COMO TIPO CANDIDATO PARA DESARROLLO; NO COMO INSTANCIA B CERRADA.**

La entidad solicitante-beneficiaria es una simplificación semántica parsimoniosa para el microdominio, siempre que se mantenga explícita la diferencia entre necesidad basal, solicitud, procesamiento y consecuencia valorada.

Permanecen OPEN: instancia y cardinalidad, demanda, consecuencia operacional, perspectiva/autoridad, dimensiones V_j, medición, DAG definitivo, estimandos y parámetros.

No Design Freeze, implementación, fixtures, simulación ni ejecución científica.  
scientific_execution=false  
execution_authorized=false
