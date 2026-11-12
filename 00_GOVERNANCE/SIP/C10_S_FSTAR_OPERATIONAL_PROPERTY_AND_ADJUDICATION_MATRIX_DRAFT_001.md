# C10-S — Matriz operacional de propiedades y adjudicación de F*

**ID:** C10-S-FSTAR-OP-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** diseño documental derivado de DEC-C10-051; NO congelado, NO implementado, NO validado, NO ejecutado.  
**Microdominio:** migración de configuración entre dos entornos software (Opción A, seleccionada).  
**Contrato relacionado:** `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md`.

## 1. Propósito

Convertir F* de una definición funcional de trabajo en una estructura de evaluación observable, no circular y adjudicable. Esta matriz no elige productos, formatos, herramientas, umbrales ni componentes técnicos. Define qué clases de propiedad deben especificarse y cómo se decide conformidad una vez fijadas.

F* se evalúa sobre la **ruta completa** desde la configuración fuente admisible hasta la configuración aplicada y verificada en el destino. F1, F2, A1 y A2 se evalúan también por separado como transformaciones; su éxito local no equivale por sí solo a cumplir F*.

## 2. Unidad de evaluación y contrato de entrada

Una instancia de evaluación F* debe quedar identificada por:
- configuración fuente y snapshot/versionado de origen;
- contrato/esquema fuente aplicable;
- identidad y snapshot basal del entorno destino;
- contrato/esquema objetivo y versión destino;
- mapping declarado entre origen, representación intermedia y destino;
- contexto basal C0;
- granularidad G de objetos, propiedades y relaciones evaluadas;
- horizonte H para completar aplicación y verificación;
- conjunto de propiedades obligatorias, condicionales y no aplicables fijado ex ante;
- identidad/versionado del procedimiento de evaluación y de sus oráculos.

C0, G, H y las versiones concretas siguen OPEN. No deben inferirse después de observar el resultado ni adaptarse por brazo Z/B.

## 3. Matriz de familias de propiedades

Las familias siguientes constituyen el catálogo mínimo de inspección. Cada propiedad atómica debe transformarse en un predicado verificable con dominio, tolerancia si procede, fuente de evidencia, regla de fallo y responsable de adjudicación.

| ID | Familia | Propiedad observable requerida | Regla candidata de conformidad | Riesgo si se omite |
|---|---|---|---|---|
| FP-01 | Esquema y tipos | Campos/objetos obligatorios, tipos, cardinalidades, restricciones y versión contractual | Todo requisito obligatorio del contrato objetivo se satisface; ningún requisito prohibido se introduce | Parseo sintáctico confundido con conformidad |
| FP-02 | Integridad estructural | Referencias, relaciones, claves, unicidad, dependencias internas y consistencia entre objetos | No hay referencias rotas, duplicidades prohibidas ni invariantes estructurales violadas | Configuración aparentemente válida pero incoherente |
| FP-03 | Preservación semántica | Correspondencia de significado entre propiedades fuente y destino según mapping explícito | Todas las invariantes funcionales declaradas se preservan dentro de tolerancias predefinidas | Igualdad de nombres/hash confundida con equivalencia |
| FP-04 | Compatibilidad destino | Admisibilidad respecto de capacidades, versión, restricciones e interfaces del destino | El destino acepta la configuración conforme al contrato y sin incompatibilidad bloqueante | Artefacto convertible pero no utilizable |
| FP-05 | Seguridad y control | Permisos, secretos, exposición, restricciones de acceso y políticas obligatorias | Ninguna violación de seguridad; controles obligatorios preservados o reforzados según política | Migración técnicamente exitosa pero insegura |
| FP-06 | Aplicación efectiva | Estado destino posterior a la aplicación, no solo artefacto preparado | La configuración objetivo queda efectivamente aplicada dentro de H | Confundir exportación/conversión con migración completa |
| FP-07 | Verificación post-aplicación | Comprobación del estado resultante frente al contrato y las invariantes | Evidencia posterior confirma FP-01…FP-05 en el estado realmente aplicado | Validar solo el artefacto previo |
| FP-08 | Procedencia y reproducibilidad | Identidad de entradas, mappings, versiones, transformaciones, oráculo y salida | Cadena de procedencia completa y repetible conforme al protocolo que se cierre | Resultado no auditable o no atribuible |

**Distinción:** FP-01…FP-07 son propiedades funcionales/técnicas de conformidad. FP-08 es una condición de validez probatoria y reproducibilidad de la evaluación; se reporta separadamente y no debe ocultar un fallo funcional. Puede ser requisito de aceptación del paquete experimental sin convertirse en propiedad semántica de la configuración.

## 4. Obligatorio, condicional y NA

- **Obligatoria:** propiedad necesaria para que la instancia satisfaga F*. Su incumplimiento implica no conformidad.
- **Condicional:** propiedad aplicable solo cuando se cumple una condición de alcance declarada ex ante. La condición y su fuente deben registrarse; no se decide después de ver el resultado.
- **No aplicable (NA):** solo cuando la propiedad no pertenece al dominio de esa instancia según regla preespecificada y justificación verificable. NA no equivale a dato ausente.
- **Desconocida (?):** la propiedad sí es pertinente, pero la evidencia no permite decidirla. No se transforma en NA ni en PASS.

El catálogo definitivo debe especificar por propiedad: obligatoriedad, condición de aplicabilidad, dominio, unidad/granularidad, regla de aceptación, tolerancia, excepción permitida, evidencia requerida y regla de adjudicación. Ninguno de esos valores se fija por intuición en esta versión.

## 5. Regla de adjudicación no compensatoria

Para una instancia (j), sea (M_j) el conjunto de propiedades obligatorias aplicables, excluyendo solo NA legítimos. Cada propiedad toma estado trivalente 1/0/? con la siguiente interpretación:

- **1:** evidencia suficiente confirma que satisface el criterio preespecificado.
- **0:** evidencia suficiente confirma una violación.
- **?:** evidencia insuficiente, contradictoria o no concluyente.

Regla candidata para la conformidad funcional:
- (F^*_j=1) si todas las propiedades de (M_j) son 1.
- (F^*_j=0) si al menos una propiedad obligatoria de (M_j) es 0.
- (F^*_j=?) en los demás casos (ninguna violación confirmada, pero al menos una propiedad obligatoria desconocida).

No se permite compensación por suma, promedio o puntuación: un buen resultado de esquema no compensa una violación de seguridad o de preservación semántica. Un fallo bloqueante confirmado basta para F*=0. La regla no autoriza umbrales ad hoc; los umbrales cuantitativos que resulten necesarios deben preespecificarse por propiedad.

Si (M_j) queda vacío por NA, la instancia no se considera automáticamente conforme: se marca como **NO EVALUABLE / SCOPE ERROR** y requiere revisar la definición de dominio del contrato.

## 6. Aplicación por etapas y transformaciones

| Elemento | Evaluación local | Lo que NO permite concluir |
|---|---|---|
| F1 / τ2 | Conversión y conformidad del artefacto intermedio S2 con su contrato | No prueba aplicación, compatibilidad final ni F*=1 |
| F2 | Aplicación del artefacto y verificación en destino | No prueba por sí sola equivalencia de la ruta alternativa |
| A1 | Exportación y completitud del artefacto neutral S1 | No prueba que A2 pueda importarlo ni que la ruta satisfaga F* |
| A2 | Importación/aplicación y verificación en destino | No prueba substituibilidad sin mismo F*, entradas y C0 |
| Ruta F1→F2 | F* completo sobre estado final | No atribuye causalidad a accesibilidad |
| Ruta A1→A2 | El mismo F* completo, con igual universo de entrada y contexto comparable | No es control funcional válido si solo alcanza SF nominal |

Una transformación intermedia puede tener PASS local y la ruta completa fallar F*. También puede darse un fallo técnico en una transformación con estado de evidencia ? si no se ha podido observar su condición real. Aplicabilidad, accesibilidad, selección, ejecución, resultado y conformidad siguen siendo variables distintas.

## 7. Oráculo de conformidad: arquitectura lógica requerida

Se requiere un procedimiento de evaluación independiente de la intervención y de los resultados downstream. Como mínimo, debe cubrir:
1. validación contractual de esquema y tipos;
2. comprobación de integridad estructural;
3. evaluación del mapping y de invariantes semánticas;
4. comprobación de compatibilidad del destino;
5. evaluación de políticas de seguridad;
6. verificación del estado efectivamente aplicado;
7. captura de procedencia, versiones, resultados y limitaciones.

Requisitos del oráculo:
- ciego a Z y B en la medida necesaria para impedir adjudicación diferencial;
- no usa Outcome ni Value para decidir F*;
- separado del mecanismo que genera/aplica la configuración, para evitar auto-certificación;
- versionado e inmutable durante una comparación;
- reglas deterministas cuando la propiedad lo permita; reglas de adjudicación explícitas cuando requiera juicio;
- conserva salidas brutas, errores, excepciones y evidencia contradictoria;
- somete sus falsos positivos/negativos y fiabilidad a evaluación independiente antes de usarlo como medida confirmatoria.

No se ha seleccionado ni implementado ningún validador concreto. La independencia efectiva del oráculo sigue sin demostrarse.

## 8. Equivalencia funcional y substituibilidad de rutas

A1→A2 será alternativa funcional substituible a F1→F2 únicamente si:
- opera sobre la misma clase de configuraciones fuente admisibles;
- se evalúa contra el mismo contrato F*, propiedades, mappings/tolerancias de salida y oráculo;
- utiliza C0, G y H comparables fijados ex ante;
- produce un estado destino aplicado que satisface F*;
- no omite propiedades por ser incómodas para una ruta;
- las condiciones de seguridad y restricciones obligatorias son equivalentes.

La equivalencia funcional no implica igualdad de mecanismo, coste, latencia, fiabilidad, riesgo o consumo de recursos. Estas dimensiones deben registrarse separadamente si forman parte de Outcomes o de vías causales de B. La mera presencia de A1/A2, un artefacto neutral o un marcador SF no demuestra substituibilidad.

## 9. Evidencia y adjudicación

Cada predicado atómico debe vincularse a evidencia con:
- ID y procedencia de la fuente;
- instante/snapshot y ámbito cubierto;
- método de obtención y versión;
- integridad/autenticidad;
- limitaciones, datos ausentes y cobertura;
- regla aplicada y resultado 1/0/?/NA;
- evaluador, cegamiento y posibles conflictos;
- adjudicación y desacuerdo preservado.

La ausencia de observación no equivale a 0. La ausencia de hallazgo no prueba cobertura exhaustiva. Un 0 requiere evidencia positiva de violación o cobertura negativa suficiente según el predicado; un 1 requiere cobertura suficiente de todos los requisitos aplicables. Los casos ambiguos permanecen ?.

## 10. Decisiones abiertas antes de cerrar F*

1. Inventario de clases de configuración y delimitación del dominio de entrada.
2. Catálogo atómico de invariantes funcionales que deben preservarse.
3. Contratos de origen, intercambio y destino, con versiones.
4. Reglas de mapping, transformaciones permitidas, pérdida admisible y excepciones.
5. Lista de requisitos de seguridad y tratamiento de secretos/permisos.
6. Definición de H, G, C0 y límites de recursos/ventanas.
7. Clasificación de propiedades obligatorias/condicionales y reglas NA.
8. Umbrales/tolerancias específicos y justificación de cada uno.
9. Oráculo independiente, versionado, cegamiento y evaluación de error.
10. Cobertura del universo de rutas y alternativas funcionales.
11. Identidad TID/SID/RID para F1/F2/A1/A2.
12. Procedimiento de adjudicación de desacuerdos y control de cambios.

## 11. Relación con el DGP y la inferencia causal

Esta matriz define el criterio funcional contra el que se clasifican resultados de las rutas. No define la intervención B, no convierte C_dep en accesibilidad, no define A_f*, no determina Reach, y no establece exclusión IV. El DGP debe mantener separados:
- verdad generadora de cada propiedad;
- observación/clasificación del analizador;
- accesibilidad de cada transformación;
- aplicabilidad desde el estado de entrada;
- selección e inicio;
- ejecución;
- Outcome;
- Value.

Un F*=1 no implica Outcome favorable ni Value positivo. Un cambio en F* no demuestra por sí mismo que ΔT_acc haya causado el cambio. La atribución causal sigue dependiendo de los estimandos y supuestos C10-S separados.

## 12. Dictamen

La matriz establece una arquitectura operacional de propiedades y una regla candidata de adjudicación no compensatoria, suficientemente explícita para orientar el cierre posterior de contratos y oráculos. No es aún una definición confirmatoria completa porque los predicados atómicos, mappings, tolerancias, H/G/C0 y evidencia no están fijados.

**Estado:** DEFINED AT FAMILY/LOGIC LEVEL; ATOMIC OPERATIONALIZATION OPEN; ORACLE NOT IMPLEMENTED/NOT VALIDATED; NO EMPIRICAL EVIDENCE; NO EXECUTION AUTHORIZATION.


## 13. Desarrollo específico de FP-03

La operacionalización específica de preservación semántica se desarrolla en `C10_S_FP03_SEMANTIC_PRESERVATION_CONTRACT_DRAFT_001.md`. Este documento define dimensiones SM-01…SM-10, mappings 1:1/1:N/N:1/N:M, clases de variación, adjudicación trivalente y requisitos de evidencia.

La ampliación no cierra FP-03: el dominio de configuración, invariantes atómicas, mappings, envolvente de observación, excepciones, tolerancias y oráculo siguen abiertos. Las dimensiones son un catálogo de inspección, no la afirmación de que todas estén presentes o sean obligatorias en cada instancia.


## 14. Reconciliación con el catálogo atómico

La correspondencia de F* con CMP/PAR/REF/RUL/POL/MET y FP-01…FP-08 se desarrolla en `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`. Los predicados estructurales y semánticos se separan; FP-06/07 no duplican FP-03, y POL preservada no implica seguridad FP-05. La reconciliación sigue siendo propuesta y no cierra obligatoriedad, NA ni oráculo.


## 17. Aplicabilidad ex ante y DEC-C10-055

La arquitectura de familias FP queda aceptada por DEC-C10-055, pero la selección de propiedades obligatorias por instancia no se cierra por esa aceptación. Se propone el IAM en `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`, con declaración previa de O/C/NA/? y cardinalidad/cobertura. La frontera entre F* funcional y gates técnicos FP-04/05/06, y el tratamiento separado de FP-08 como validez probatoria, permanece abierta a decisión antes del freeze.


## 18. Frontera F* / FP-08 precisada

F* es capacidad funcional de ruta completa (producción y aplicación en destino) y puede requerir FP-01…FP-07 en dimensiones separadas, incluida compatibilidad FP-04, seguridad efectiva FP-05, aplicación FP-06 y verificación FP-07. FP-08 es gate probatorio independiente, no atributo funcional ni compensación. La exclusión de POL en el núcleo mínimo no elimina los requisitos de seguridad F*; estos se declaran independientemente del módulo POL. Véase la precisión en la matriz IAM.


## 19. DEC-C10-056 — cardinalidad del objeto F*

La instancia funcional de F* se restringe al DGP base con CMP≥1, PAR≥1, RUL≥1; REF puede ser cero únicamente con IAM ex ante y cobertura exhaustiva; POL ausente por diseño en el núcleo mínimo; MET obligatorio. Esta cardinalidad delimita la unidad/objeto candidato y no reemplaza los gates FP-01…FP-07 ni el gate probatorio FP-08. El contrato abstracto es `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`.



## 20. Reconciliación con las fichas funcionales de Opción A (2026-11-06)

La lectura conjunta con la propuesta de fichas §11 fija la interpretación sin ampliar DEC-C10-051: F1/τ2 es conversión S0→S2; F2 aplica S2→SF; A1/A2 componen la ruta alternativa S0→S1→SF; F* se adjudica sobre la ruta completa. El adaptador es provisión técnica de B y no ejecuta transformaciones.

La conformidad local de F1/F2/A1/A2 no sustituye la adjudicación F* de ruta completa. Las rutas comparadas usan la misma instancia contractual, clase de entrada, destino, IAM, C0, G, H, familias FP aplicables y oráculo versionado. La substituibilidad exige satisfacer el mismo F*, no identidad de mecanismo ni igualdad presumida de coste/riesgo/latencia; estos últimos se registran separadamente.

FP-01…FP-07 conservan adjudicación funcional por dimensiones no compensatorias y FP-08 es gate probatorio separado. Outcome/Value quedan fuera del oráculo. La declaración O/C/NA/? se sella en IAM pre-Z/B; unknown y falta de cobertura no se convierten en NA.

**Estado:** reconciliación documental; no cierra propiedades atómicas, IAM, mappings, tolerancias, C0/G/H, oráculo, MD-C1/MD-C4 ni exclusión IV. No implementación ni ejecución.


## 21. N16 — síntesis de precedencia del criterio y del oráculo (2026-11-09)

Esta matriz es el instrumento vigente para las familias funcionales F*. Se mantiene la siguiente precedencia:

- DEC-C10-051 acepta Opción A y F* como contrato funcional de trabajo candidato.
- DEC-C10-055 acepta la arquitectura de familias FP-01…FP-08, no la selección de obligatoriedad por instancia.
- DEC-C10-056 fija la cardinalidad del objeto base, sin sustituir IAM ni cobertura.
- DEC-C10-083 acepta la aplicabilidad de los dos PAR del servicio sintético en los siete stage_key, sin adjudicar observaciones materiales.

La separación de capas es obligatoria:
1. Criterio funcional común F* de ruta completa.
2. Oráculo independiente, versionado e inmutable que implementa criterios, mappings y tolerancias aprobados.
3. Adjudicación por instancia, ruta, versión y snapshot, con evidencia vinculada.

El Generator conserva hidden_truth y potenciales. El Analyzer no recibe hidden_truth, parámetros generadores, potenciales ni Value potencial. El Evaluator compara la salida del Analyzer con truth y criterios de referencia después de congelar esa salida. No se permite que el Analyzer use Outcome/Value, Z/B o la ejecución para definir F*.

FP-01…FP-07 son dimensiones funcionales no compensatorias; FP-08 es un gate probatorio separado. UNKNOWN por falta de evidencia/cobertura no se convierte en 0 ni NA; NA requiere inaplicabilidad ex ante en IAM. Un PASS de una etapa local no equivale a F*=1 de ruta completa.

**Estado:** arquitectura del criterio definida y familias aceptadas; reconciliación atómica, requiredness por instancia, C0/G/H, mappings, tolerancias, oráculo, validación y evidencia siguen OPEN. Esta matriz no afirma implementación, validación ni ejecución.



## 22. N16 — integración terminal F*/O-CONF y ficha §224 (2026-11-12)

La reconciliación vigente del plan C10-S §16.184 precisa la aplicación de esta matriz sin sustituirla ni convertirla en oráculo implementado.

### 22.1. Criterio, resultado y evidencia

F* es el criterio común de ruta completa; O-CONF es el resultado terminal de adjudicar una instancia/ruta exacta contra ese criterio. No se cuentan como dos Outcomes. FP-01…FP-07 son dimensiones funcionales no compensatorias. FP-08 es gate de validez probatoria separado: su fallo no cambia la truth funcional, pero puede dejar la adjudicación observada no válida/no evaluable.

### 22.2. Unidad y ancla terminal

La unidad lógica es instancia de configuración × ruta. La ruta F se ancla en F2_DST_APPLIED; la ruta A, en A2_DST_APPLIED, usando el snapshot post-aplicación/post-check exigido por DEC-C10-087. No se infiere aplicación desde *_DST_DECL, artefacto preparado, exit code o log aislado. Snapshot, evento terminal, timestamp, route_id y mapping al reloj DGP siguen abiertos.

### 22.3. Regla de O-CONF

- 1: todos los predicados obligatorios aplicables FP-01…07 son 1 y el conjunto no está vacío.
- 0: al menos un predicado obligatorio aplicable es 0, demostrado con evidencia/cobertura suficiente.
- ?: sin fallo obligatorio confirmado, al menos un predicado obligatorio aplicable es desconocido/no comparable/insuficientemente cubierto.
- SCOPE_ERROR/NOT_EVALUABLE: conjunto obligatorio vacío o cardinalidad constitutiva incumplida.

NA requiere IAM pre-Z/B justificado. La falta de observación no demuestra 0 ni NA. FP-08 se reporta aparte; cuando impide validar evidencia, la salida observada es no válida/no evaluable sin recodificar la truth como 0. Se preservan vectores por predicado y la regla anti-doble-conteo FP-01…05/FP-07.

### 22.4. Alcance aceptado frente a pendiente

PAR-SVC-ENABLED/PROFILE y RUL-SVC-ENABLE-PROFILE-01 tienen contratos semánticos aceptados dentro de su alcance (DEC-C10-083…086); FP-06/07/08 y las etapas aplicadas se rigen por DEC-C10-087/088. La reconciliación SM-01…SM-10↔FP global sigue propuesta; no se extrapola la aceptación PAR/RUL a todo CMP/REF/MET ni a FP-04/05. C0 aceptado es binding lógico de cobertura, no C0 ambiental material. G/H, IAM poblado, mappings, tolerancias, oráculo, snapshots, error y cobertura siguen OPEN.

### 22.5. Oráculo y PE

El oráculo debe ser independiente, versionado/inmutable y aplicar criterios públicos a evidencia permitida; no lee truth ni potenciales y no cambia por Z/B/Outcome/Value. Generator mantiene truth; Analyzer recibe observaciones y, si el contrato lo requiere, O-CONF observado; Evaluator compara después del sellado. No existe implementación ni validación del oráculo; el firewall lógico no acredita ACL/custodia material.

**Estado:** N16_RECONCILED_DOCUMENTARILY / OCONF_RULE_DEFINED_LOGICALLY / ORACLE_NOT_IMPLEMENTED_NOT_VALIDATED / IAM_AND_ATOMICS_PARTIAL / NO_EXECUTION_AUTHORIZED.
