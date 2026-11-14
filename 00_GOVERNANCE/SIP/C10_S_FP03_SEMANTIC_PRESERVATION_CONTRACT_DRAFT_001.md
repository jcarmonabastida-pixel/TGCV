# C10-S — Contrato candidato de preservación semántica FP-03

**ID:** C10-S-FP03-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta documental de operacionalización; NO aprobada como contrato confirmatorio, NO congelada, NO implementada, NO validada, NO ejecutada.  
**Base de decisión:** DEC-C10-051 selecciona Opción A (migración de configuración entre dos entornos software) y adopta F* como contrato funcional de trabajo candidato.  
**Dependencia:** `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md`, FP-03.

## 1. Pregunta de FP-03

¿La configuración aplicada en el entorno destino conserva las propiedades funcionales y restricciones semánticas que el contrato de migración declara obligatorias para la configuración fuente, dentro del dominio y las excepciones preespecificadas?

FP-03 no pregunta si el artefacto destino es sintácticamente válido, si el proceso terminó sin error, si los identificadores o hashes coinciden, ni si Outcome/Value mejoraron. Pregunta si el significado operativo declarado se preserva.

La equivalencia es relativa a un contrato explícito, una clase de entradas, un contexto C0, granularidad G y horizonte H. No se afirma equivalencia universal entre entornos.

## 2. Principio: equivalencia semántica observable y acotada

Se propone evaluar preservación mediante propiedades observables preespecificadas sobre la configuración fuente y el estado aplicado en destino. Para cada propiedad se declara:
- qué significa en el dominio;
- en qué objeto/relación/alcance aplica;
- cómo se observa en origen y destino;
- qué mapping relaciona ambos;
- qué variaciones son semánticamente neutras;
- qué diferencias son permitidas y bajo qué condición;
- qué diferencias constituyen pérdida, alteración o incumplimiento;
- qué evidencia y cobertura bastan para adjudicar 1/0/?/NA.

No se requiere igualdad textual, de serialización, nombre, orden físico ni hash, salvo que alguno de esos atributos tenga significado contractual explícito. Tampoco se introduce una capa semántica persistida adicional: el mapping y las reglas comparativas son parte del contrato de evaluación, no un nuevo objeto operativo del sistema.

## 3. Catálogo candidato de dimensiones semánticas

Las dimensiones son un catálogo de inspección, no una afirmación de que todas estén presentes en cada configuración. La aplicabilidad de cada una debe declararse ex ante y justificarse.

| ID | Dimensión | Pregunta de preservación | Ejemplos abstractos de pérdida/alteración |
|---|---|---|---|
| SM-01 | Identidad y significado de entidades | ¿Cada entidad obligatoria del origen conserva su identidad funcional en destino o tiene correspondencia explícita? | Entidad omitida, duplicada, fusionada sin autorización o reasignada a otro significado |
| SM-02 | Valores, tipos y dominios | ¿Los valores conservan su significado, dominio, unidad, precisión y restricciones? | Cambio de unidad, truncamiento, redondeo no autorizado, enum reinterpretado |
| SM-03 | Relaciones y referencias | ¿Las relaciones funcionalmente relevantes se conservan y apuntan a los equivalentes correctos? | Referencia rota, relación invertida, dependencia omitida o asociación alterada |
| SM-04 | Ausencia, nulos y valores por defecto | ¿Ausencia, null, vacío y default mantienen distinciones que el contrato considere significativas? | Null convertido en default, campo ausente convertido en valor, default aplicado de forma distinta |
| SM-05 | Cardinalidad y multiplicidad | ¿Se conserva la multiplicidad permitida y sus restricciones? | Colección colapsada, elemento repetido, cardinalidad limitada o expandida sin regla |
| SM-06 | Orden y precedencia | ¿El orden tiene significado en el dominio y, si lo tiene, se conserva la precedencia? | Secuencia reordenada cuando el orden cambia la función |
| SM-07 | Condiciones y reglas operativas | ¿Las condiciones, expresiones, restricciones o reglas que gobiernan el comportamiento mantienen su semántica? | Condición invertida, operador cambiado, regla omitida o precedencia alterada |
| SM-08 | Tiempo y vigencia | ¿Los intervalos, zonas/convenciones temporales, activación y caducidad conservan el significado contractual? | Desplazamiento temporal, duración alterada, vigencia aplicada en instante distinto |
| SM-09 | Permisos y semántica de control | ¿La interpretación funcional de roles, permisos y restricciones se conserva? | Privilegio ampliado/reducido, rol reasignado o regla de acceso reinterpretada |
| SM-10 | Extensiones y propiedades desconocidas | ¿Los elementos no comprendidos por el mapping se preservan, rechazan o aíslan conforme a una regla explícita? | Extensión descartada silenciosamente, atributo desconocido convertido o ignorado con efecto funcional |

La separación con FP-05 (seguridad) debe mantenerse: SM-09 comprueba preservación semántica de las reglas de control como parte de la configuración; FP-05 determina además si el resultado cumple la política de seguridad obligatoria. Un resultado puede preservar fielmente una política insegura y, aun así, fallar FP-05.

## 4. Reglas para el mapping

Cada mapping origen→destino debe clasificarse y justificarse:

- **1:1:** correspondencia directa de significado.
- **1:N:** una entidad/propiedad de origen se representa mediante varios elementos destino; debe probarse que la composición conserva el significado.
- **N:1:** varios elementos origen se consolidan; requiere demostrar que no se pierde una distinción funcional obligatoria.
- **N:M:** mapping compuesto; necesita reglas completas y cobertura de todos los casos admisibles.
- **Sin correspondencia:** solo aceptable si el elemento es explícitamente no obligatorio/no aplicable o existe una regla aprobada de descarte; de lo contrario, evidencia de pérdida.

El mapping no se acepta solo porque el conversor lo haya producido. Debe existir un contrato de correspondencia revisable, versionado y separado del generador. Las correspondencias ambiguas o parciales permanecen ?; la pérdida obligatoria confirmada produce 0.

No se exige crear ni persistir un grafo/ontología/capa semántica paralela. El mapping puede documentarse como tabla contractual y evidencias asociadas dentro del expediente C10-S.

## 5. Clases de variación

| Clase | Tratamiento propuesto |
|---|---|
| Diferencia puramente representacional | Permitida si se demuestra que no altera ninguna propiedad semántica contractual |
| Normalización reversible | Permitida si regla, alcance y reversibilidad están definidos y comprobados |
| Transformación con pérdida | Solo admisible si la propiedad afectada fue declarada no obligatoria o existe excepción ex ante justificada; no puede declararse equivalencia plena sin ello |
| Pérdida de propiedad obligatoria | FP-03=0 |
| Cambio de significado o de regla | FP-03=0, salvo transformación semántica explícita prevista en el contrato de destino |
| Diferencia no adjudicable | FP-03=? |
| Elemento fuera del dominio declarado | NA solo con justificación y regla previa; de otro modo, ? o error de alcance |

Una transformación que cambia deliberadamente el significado no es preservación, aunque el resultado sea más conveniente o produzca mejor Outcome/Value. Si se desea una migración transformativa y no preservativa, deberá definirse otra F* o una propiedad de transformación autorizada; no debe ocultarse dentro de FP-03.

## 6. Evaluación comparativa origen/destino

Para cada propiedad semántica atómica (p_k):
1. fijar el contrato de origen y el dominio de entrada;
2. observar el valor/relación/condición relevante en el snapshot fuente;
3. aplicar el mapping declarado sin consultar Outcome/Value;
4. observar el estado realmente aplicado en destino;
5. evaluar el predicado de equivalencia definido para (p_k);
6. registrar evidencia, cobertura, versión, excepción y adjudicación.

La comparación no puede depender de valores de salida elegidos después de observar el resultado. Los casos de prueba, invariantes y excepciones deben fijarse antes de la evaluación confirmatoria.

Cuando la equivalencia depende del comportamiento y no solo de estructura, el contrato deberá especificar una envolvente de observación: entradas/condiciones bajo las cuales se comparan las respuestas o efectos observables del origen y destino. No se fijan todavía casos concretos, números de probes ni tolerancias; dependen del dominio de configuración que se cierre.

## 7. Regla de adjudicación FP-03

FP-03 se descompone en predicados semánticos atómicos aplicables:

- **FP-03=1:** todas las propiedades semánticas obligatorias aplicables tienen correspondencia válida y cumplen el criterio de preservación; excepciones permitidas están justificadas y preespecificadas.
- **FP-03=0:** al menos una propiedad obligatoria presenta pérdida, alteración o incumplimiento confirmado.
- **FP-03=?:** no hay pérdida confirmada, pero una o más propiedades obligatorias no pueden adjudicarse por evidencia incompleta, mapping ambiguo, cobertura insuficiente o contradicción.
- **FP-03=NA:** solo si el contrato preespecifica que no existe ninguna propiedad semántica de esa familia aplicable a la instancia; no basta con que el dato no esté disponible.

Si se confirma pérdida de una sola propiedad obligatoria, no se compensa con preservación de las demás. El resultado se informa junto con el perfil por propiedad, no solo con el agregado.

## 8. Requisitos de evidencia y cegamiento

La evidencia debe permitir reconstruir la comparación:
- snapshots origen/destino y sus identidades/versiones;
- contrato de origen y destino;
- mapping versionado y reglas de variación;
- predicados atómicos y su aplicabilidad;
- método de observación y cobertura;
- salidas brutas, diferencias y excepciones;
- identidad/versionado del evaluador;
- registro de cegamiento respecto de Z/B y ausencia de acceso a Outcome/Value;
- desacuerdos y adjudicación.

El oráculo debe evaluar las mismas propiedades y reglas en todas las rutas y brazos. No debe conocer qué ruta fue habilitada por B cuando ello pueda sesgar la clasificación. La evaluación de fiabilidad, falsos positivos/negativos y adjudicación independiente permanece pendiente.

## 9. Relación con F1/F2/A1/A2 y cautela histórica

La selección de Opción A no determina por sí sola el mecanismo concreto de las cuatro transformaciones. La propuesta vigente de fichas describe F1 como conversión focal, F2 como aplicación/verificación, A1 como exportación neutral y A2 como importación/aplicación nativa; estas semánticas deben tratarse como **roles candidatos de diseño**, no como identidades TID ni mecanismos técnicos aprobados, hasta que se reconcilien explícitamente con el expediente histórico y se adopten como contratos.

FP-03 evalúa la ruta completa respecto del mismo F*. No presupone que:
- F1 y A1 operen sobre las mismas representaciones;
- F2 y A2 usen mecanismos equivalentes;
- un formato neutral preserve necesariamente el significado;
- la ruta alternativa exista realmente o sea funcionalmente substituible;
- B afecte exclusivamente a F1;
- llegar al estado nominal SF equivalga a conformidad F*.

Si la semántica concreta de F1/F2/A1/A2 no puede derivarse de una decisión explícita y de los contratos de dominio, debe permanecer abierta y elevarse como decisión de diseño, no rellenarse por inferencia.

## 10. Casos de falsación que el futuro DGP debe poder representar

Sin asignar todavía probabilidades ni truth:
1. Estructura válida, pero valor convertido con unidad distinta: FP-01 podría pasar y FP-03 fallar.
2. Entidad conservada, relación funcional omitida: FP-02/FP-03 fallan según contrato.
3. Null y default colapsados cuando son semánticamente distintos: FP-03 falla.
4. Conversión many-to-one que fusiona categorías obligatorias: FP-03 falla.
5. Orden alterado en una colección cuyo orden es irrelevante: no debe penalizarse; si es relevante, sí.
6. Regla temporal interpretada en zona/convención distinta: FP-03 falla si cambia vigencia.
7. Extensión desconocida descartada sin regla: ? si no se conoce su efecto; 0 si es obligatoria y se confirma pérdida.
8. Equivalencia estructural, pero divergencia de comportamiento dentro de la envolvente declarada: FP-03 falla.
9. Mapping parcial con cobertura no exhaustiva: ? y no PASS.
10. Preservación semántica correcta pero política insegura preservada fielmente: FP-03 puede pasar y FP-05 debe fallar.

Estos casos son especificaciones de falsación, no fixtures ejecutados ni resultados observados.

## 11. Decisiones que siguen abiertas

1. Delimitar clases de configuración y dominio de entrada admisible.
2. Decidir qué dimensiones SM-01…SM-10 aplican y cuáles son obligatorias/condicionales.
3. Definir invariantes semánticas atómicas para el microdominio seleccionado.
4. Fijar contratos de origen/destino y mapping permitido.
5. Decidir si la equivalencia se adjudica por invariantes, envolvente de comportamiento o ambas.
6. Especificar diferencias permitidas, pérdidas admisibles y reglas de excepción.
7. Definir tolerancias solo donde la semántica admita variación cuantitativa, con justificación.
8. Resolver semánticas concretas y TID/SID/RID de F1/F2/A1/A2 mediante decisión explícita.
9. Especificar cobertura, método de observación y evaluación de error del oráculo.
10. Alinear FP-03 con FP-01/02/04/05/07 sin duplicar ni dejar huecos.

## 12. Dictamen

FP-03 queda desarrollado a nivel de dimensiones semánticas, clases de mapping, variaciones, regla de adjudicación y requisitos de evidencia. No queda operacionalmente cerrado: faltan dominio concreto, predicados atómicos, mappings, invariantes, envolvente de observación, excepciones, tolerancias y oráculo validado.

**Estado:** DEFINED AT SEMANTIC-DIMENSION/LOGIC LEVEL; ATOMIC CONTRACT OPEN; MAPPING NOT SPECIFIED; ORACLE NOT VALIDATED; NO EMPIRICAL EVIDENCE; NO EXECUTION AUTHORIZATION.


## 13. Delimitación del objeto de configuración — propuesta pendiente

La propuesta `C10_S_CONFIGURATION_OBJECT_SCOPE_AND_MINIMUM_CONTRACT_PROPOSAL_DRAFT_001.md` compara tres clases de objeto y recomienda un paquete de configuración de servicio software con componentes, parámetros tipados, referencias, reglas/restricciones, políticas asociadas y metadatos contractuales. Es una propuesta para decisión, no una selección aprobada.

Si se acepta, permitirá convertir SM-01…SM-10 en predicados atómicos y separar el contenido migrado de recursos, permisos efectivos, ventanas y estado del entorno. No se crea una capa semántica persistida adicional.


## 14. Objeto seleccionado tras DEC-C10-052

La clase de objeto deja de ser una alternativa pendiente: se selecciona un **paquete de configuración de un servicio software**. Su estructura conceptual inicial comprende componente, parámetros tipados, referencias, reglas/restricciones, políticas asociadas y metadatos contractuales. La selección está registrada en DEC-C10-052 y desarrollada en `C10_S_CONFIGURATION_OBJECT_SCOPE_AND_MINIMUM_CONTRACT_PROPOSAL_DRAFT_001.md`.

SM-01…SM-10 deberán especializarse sobre estos elementos, sin asumir que todas las dimensiones aplican u obligan en cada instancia. La obligatoriedad se fijará ex ante en el contrato del dominio. Recursos/capacidad, permisos efectivos, dependencias instaladas y estado del entorno permanecen como condiciones del entorno, no como contenido del paquete.

**Estado:** objeto seleccionado para diseño; predicados atómicos, obligatoriedad, mappings, contratos fuente/destino y oráculo siguen abiertos. No hay validación técnica, revisión independiente, evidencia empírica ni ejecución.


## 15. Catálogo candidato de propiedades atómicas

La primera atomización del objeto seleccionado se registra en `C10_S_CONFIGURATION_OBJECT_ATOMIC_PROPERTY_CATALOG_DRAFT_001.md`. Propone CMP-01…03, PAR-01…06, REF-01…05, RUL-01…05, POL-01…05 y MET-01…04, con correspondencia a SM-01…SM-10 y límites entre FP-01…FP-08.

La atomización no cierra obligatoriedad ni aplicabilidad. Las propiedades candidatas centrales no son automáticamente obligatorias; las propiedades condicionales requieren que el contrato de la instancia declare la dimensión pertinente. Dominio, contratos fuente/destino, mappings, tolerancias y oráculo siguen abiertos.


## 16. Reconciliación de dimensiones y familias

La matriz de SM-01…SM-10 debe leerse junto con `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`. La reconciliación separa estructura, integridad, semántica, compatibilidad, seguridad, aplicación, observación post-aplicación y procedencia. Las dimensiones condicionales no se convierten en obligatorias por aparecer en el catálogo. Se conserva la regla de adjudicación trivalente y no compensatoria.
