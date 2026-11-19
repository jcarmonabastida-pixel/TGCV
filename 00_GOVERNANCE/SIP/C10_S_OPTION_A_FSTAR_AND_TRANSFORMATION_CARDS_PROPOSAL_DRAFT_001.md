# C10-S — Propuesta de F* y fichas transformacionales para Opción A

**ID:** C10-S-OPTION-A-CARDS-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** Opción A seleccionada para el diseño C10-S; F* adoptado como contrato funcional de trabajo candidato. Documento Draft, no congelado ni ejecutable.  
**Ámbito:** migración de configuración entre dos entornos software.  
**Fuentes:** C10_S_TRANSFORMATION_CARDS_HISTORICAL_RECONCILIATION_DRAFT_001.md; C10_S_SYNTHETIC_MICRODOMAIN_OPTIONS_AND_SELECTION_RECOMMENDATION_DRAFT_001.md; maestro C10-S §§48–57, 74–76, 91–94; contrato de provisión B; contrato DGP temporal/roles; matriz U_G.

## 1. Propósito y límites

Este documento avanza desde aliases topológicos a una propuesta funcional concreta, sin convertir una recomendación histórica en decisión aprobada. Opción A es el microdominio preferente recomendado en el análisis comparativo, pero el repositorio aún la marca como no seleccionada/no aprobada. Por ello las fichas siguientes son una propuesta para decisión explícita.

No se definen formatos concretos, productos, versiones, comandos, umbrales numéricos, recursos, permisos ni tiempos. Tampoco se asignan estados generadores 1/0/? ni se afirma que exista una ruta técnica real. Esos elementos requieren decisión de diseño y, después, evidencia/validación.

## 2. Contrato funcional común F*

**F* (candidata):** dada una configuración fuente admisible y un contrato de configuración destino preespecificado, producir y dejar aplicada en el entorno destino una configuración que satisfaga las propiedades obligatorias de esquema, integridad, compatibilidad y seguridad definidas por ese contrato, preservando las propiedades funcionales declaradas como invariantes.

F* se evalúa sobre la ruta completa, no sobre F1, F2, A1 o A2 aisladamente. No incluye Outcome ni Value, productividad, satisfacción, coste económico ni el mero hecho de alcanzar el marcador formal SF.

### 2.1 Predicados observables candidatos

| Dimensión | Criterio a fijar ex ante | No basta |
|---|---|---|
| Esquema | Campos obligatorios, tipos, cardinalidades, restricciones y versión de contrato conformes | Parseo sintáctico |
| Integridad | Referencias, relaciones y consistencia interna preservadas | Archivo generado |
| Compatibilidad | Configuración admisible para versión/capacidades del destino | Importación sin error |
| Preservación | Propiedades funcionales obligatorias mantienen semántica según mapping declarado | Igualdad textual o de hash |
| Seguridad | No se introducen permisos, secretos o configuraciones prohibidas; controles requeridos se mantienen | Aplicación técnica exitosa |
| Aplicación | El destino acepta/aplica la configuración y el estado resultante puede verificarse | Artefacto convertido pero no aplicado |

Los conjuntos exactos de propiedades, mappings, excepciones, tolerancias y criterios de rechazo quedan OPEN. No se asignan umbrales arbitrarios.

### 2.2 Entrada, salida y contexto

- Entrada común: configuración fuente versionada, su contrato/esquema, estado inicial del entorno destino y contexto basal C0.
- Salida: configuración aplicada en destino más evidencia de conformidad con F*.
- C0: versiones, capacidades, permisos, recursos, ventana de mantenimiento y restricciones del entorno, todos fijados ex ante.
- H: ventana máxima desde inicio de la ruta hasta aplicación y verificación; valor pendiente.
- G: granularidad de transformación y propiedades de configuración; valor pendiente.
- Oráculo: validador independiente, versionado e inmutable, ciego a Z/B y separado del generador. No puede usar Outcome/Value para decidir conformidad.

### 2.3 Regla de equivalencia funcional

Una ruta focal F1→F2 y una alternativa A1→A2 son funcionalmente substituibles solo si ambas, desde la misma clase de entradas admisibles y bajo C0, H y G comunes, satisfacen las mismas propiedades obligatorias de F*, restricciones de seguridad e integridad y tolerancias preespecificadas. No se exige identidad de mecanismo. No se presume igualdad de coste, latencia, fiabilidad o riesgo: se registran separadamente.

## 3. Fichas transformacionales candidatas

### 3.1 F1 / τ2 — conversión focal

- **Rol:** transformación focal cuya accesibilidad puede verse afectada por B.
- **Transición abstracta:** S0 → S2.
- **Función candidata:** convertir la configuración fuente admisible a una representación/configuración objetivo que pueda ser consumida por la continuación F2.
- **Entrada:** configuración fuente y contrato de origen; metadatos/versiones necesarios.
- **Salida:** artefacto convertido en S2, aún no aplicado en destino.
- **Precondiciones de aplicabilidad:** fuente dentro del dominio admitido; mapping disponible; formato/versión reconocidos; restricciones de conversión satisfechas.
- **Accesibilidad:** A_f*(τ2) se evalúa separadamente mediante ID, REL, COND, AUTH, RES, DEP y ausencia de BLOCK. La provisión de B, C_dep=1 o presencia del adaptador no bastan por sí solos.
- **Ejecución:** Exec(F1) solo tras selección/inicio. B no ejecuta F1.
- **Fallo observable:** identidad/mapping no resuelto, fuente no admitida, dependencia incompatible, recurso insuficiente, autorización inválida o conversión no conforme.
- **Pendiente:** TID/SID/RID, contrato exacto de conversión, mapping, tolerancias, recursos, ventana y evidencia E1–E4.

### 3.2 F2 — aplicación y verificación focal

- **Rol:** continuación necesaria de la ruta focal; no se presume accesible por abrir F1.
- **Transición abstracta:** S2 → SF.
- **Función candidata:** aplicar la configuración convertida en el entorno destino y verificar que el estado aplicado satisface las propiedades destino de F*.
- **Entrada:** artefacto S2 validado estructuralmente; entorno destino y snapshot de referencia.
- **Salida:** configuración aplicada más resultado de verificación, o fallo reversible/registrado.
- **Precondiciones de aplicabilidad:** destino compatible; ventana habilitada; permiso de escritura/aplicación; estado destino no bloqueante; validaciones previas satisfechas.
- **Accesibilidad:** predicados propios de identidad, canal, autorización, recursos, dependencias y bloqueos; se evalúa separadamente de F1.
- **Ejecución:** aplicación efectiva posterior a selección/inicio; no forma parte de B.
- **Fallo observable:** rechazo del destino, incompatibilidad, conflicto con estado actual, permiso/ventana ausente, aplicación parcial o verificación F* fallida.
- **Pendiente:** contrato de aplicación, estrategia transaccional/rollback, criterios de verificación, residuos, tolerancias, duración y recursos.

### 3.3 A1 — exportación alternativa

- **Rol:** primer paso de una ruta alternativa basal, no provisionada por B.
- **Transición abstracta:** S0 → S1.
- **Función candidata:** exportar la configuración fuente mediante un mecanismo de exportación disponible en baseline a un artefacto de intercambio neutral.
- **Entrada:** misma configuración fuente y contrato de origen admisible.
- **Salida:** artefacto neutral S1 con esquema, versión y metadatos de procedencia.
- **Precondiciones:** exportador baseline presente y funcional; permiso de lectura; formato de intercambio admitido; recursos y ventana disponibles.
- **Accesibilidad:** propia de A1; no se infiere de la disponibilidad de F1 ni del adaptador.
- **Fallo observable:** exportador ausente/incompatible, cobertura incompleta, pérdida de propiedades, permisos o recursos insuficientes.
- **Pendiente:** mecanismo/exportador concreto, formato neutral, mapping, TID/SID/RID, dependencias transitivas y evidencia.

### 3.4 A2 — importación/aplicación alternativa

- **Rol:** cierre de la ruta alternativa A1→A2.
- **Transición abstracta:** S1 → SF.
- **Función candidata:** importar/aplicar el artefacto neutral mediante un mecanismo nativo del entorno destino y verificar el mismo contrato F*.
- **Entrada:** artefacto S1 producido por A1; destino y contexto comparables a F2.
- **Salida:** configuración aplicada y verificada contra F* o fallo registrado.
- **Precondiciones:** importador nativo baseline; permiso de escritura; compatibilidad del artefacto; ventana, recursos y estado destino admisibles.
- **Accesibilidad:** propia de A2; se evalúa separadamente de A1.
- **Fallo observable:** formato no admitido, mapping insuficiente, incompatibilidad, aplicación parcial o fallo del mismo oráculo F*.
- **Pendiente:** mecanismo/importador concreto, mapping, TID/SID/RID, recursos, dependencias y evidencia.

## 4. Separaciones causales obligatorias

1. B provisiona/configura la dependencia focal; no convierte, aplica ni valida.
2. C_dep describe estado técnico de la dependencia; no equivale a A_f*.
3. A_f* describe accesibilidad de τ2; no equivale a App(F1,S0), ejecución ni éxito.
4. App se evalúa desde el estado de entrada de cada transformación.
5. F1 y F2 son transformaciones distintas; la accesibilidad de F1 no implica accesibilidad/alcanzabilidad de SF.
6. A1/A2 deben ser una ruta mecanísticamente genuina y basal. Si B altera sus dependencias, recursos, permisos o rendimiento, se registra R2/vía colateral y no se sostiene exclusión IV focal.
7. La existencia de A1→A2 no prueba substituibilidad: debe satisfacer el mismo F* con evidencia y cobertura.
8. Reach(SF) puede permanecer 1 antes y después de abrir τ2 si la alternativa ya es funcional. ΔT_acc no implica necesariamente ΔReach.
9. Outcome y Value se miden después y no forman parte del oráculo F*.

## 5. Matriz de pendientes por ficha

| Elemento | Ya definido documentalmente | Abierto antes de DGP cerrado |
|---|---|---|
| F* | Dominio funcional técnico, independiente de O/V; propiedades candidatas | Lista cerrada de propiedades, mappings, tolerancias, rechazo y oráculo |
| F1/τ2 | Rol focal, conversión, S0→S2, separación B/ejecución | Contrato, identidad, versión, precondiciones y recursos |
| F2 | Aplicación destino y verificación, S2→SF | Contrato, atomicidad, rollback, recursos y precondiciones |
| A1 | Exportación neutral, S0→S1 | Formato y mecanismo baseline, mapping, dependencias |
| A2 | Importación/aplicación nativa, S1→SF | Mecanismo, mapping, rollback, recursos y precondiciones |
| Rutas | Composiciones F1→F2 y A1→A2 | Universo cerrado, alternativas adicionales, H/G/C0 y cobertura |
| B | Provisión técnica sin ejecutar rutas | Arquitectura y manifiesto reales; no-afectación y recursos |
| Oráculo | Independiente de O/V y ciego a Z/B como requisito | Especificación, validación, error, fiabilidad y cegamiento |

## 6. Riesgos y pruebas de falsación que debe preservar el DGP

- La ruta alternativa puede ser funcional en baseline y mantener Reach(SF)=1.
- F1 puede abrirse mientras F2 sigue inaccesible o no aplicable.
- Ambas rutas pueden fallar F* por razones distintas.
- La conversión puede preservar esquema pero alterar semántica; por eso parseo no basta.
- B puede consumir recursos o modificar dependencias compartidas y afectar F2/A1/A2.
- Un artefacto neutral puede ser válido pero no importable en el destino.
- La ruta puede alcanzar SF nominal y aun así incumplir F*.
- Un cambio en accesibilidad puede no cambiar selección, ejecución, Outcome o Value.
- Las observaciones del analizador pueden ser ? aun cuando la verdad del DGP sea 0/1; no filtrar truth al analizador.

## 7. Decisiones y datos que siguen sin fijarse

La selección de Opción A y la adopción de F* como contrato de trabajo se registran en DEC-C10-051 (2026-11-05). No deben reabrirse como decisiones pendientes salvo que nueva evidencia o contradicción justifique reconsideración.

1. Cerrar la definición operacional final de F* y su catálogo de propiedades.
3. Definir catálogo de propiedades, mappings, tolerancias y casos fronterizos.
4. Definir formatos/versiones de origen, destino e intercambio.
5. Ratificar contratos de entrada/salida y TID/SID/RID de F1/F2/A1/A2.
6. Fijar C0, G, H, recursos, permisos, ventanas y rollback.
7. Determinar independencia real de A1/A2 respecto de B y componentes compartidos.
8. Especificar oráculo, cegamiento, error y validación E1–E4.
9. Solo después, instanciar R0–R3 y completar ecuaciones/valores del DGP.

## 8. Dictamen

Esta propuesta hace explícita la interpretación funcional adoptada como base de trabajo para las cuatro transformaciones y F*. La selección del microdominio y la adopción del contrato de trabajo quedan decididas por DEC-C10-051; no se consideran cerrados el contrato operacional final, OPEN-C10-003 ni los hallazgos de accesibilidad, cobertura, medición o identificación. No hay inventario técnico, validación empírica, generación, simulación, implementación ni ejecución.


## 9. Registro de decisión DEC-C10-051

El 2026-11-05 el usuario selecciona Opción A —migración de configuración entre dos entornos software— como microdominio de diseño C10-S y adopta F* como contrato funcional de trabajo candidato. La selección habilita completar fichas y DGP documental; no autoriza ejecución ni cierra los parámetros, propiedades, mappings, tolerancias, oráculo, D1/D2 o identificación causal.


## 10. Matriz operacional de propiedades y adjudicación

La matriz complementaria `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md` desarrolla las familias FP-01…FP-08, la regla trivalente no compensatoria de conformidad, las evaluaciones por etapa, los requisitos del oráculo y las condiciones de substituibilidad. Debe leerse conjuntamente con estas fichas.

La matriz no fija todavía predicados atómicos, mappings, tolerancias, H/G/C0, catálogo de entrada, contratos de formato/versiones ni oráculo concreto. Por tanto, F* permanece definido a nivel de familias/arquitectura lógica, no cerrado operacionalmente.



## 11. Reconciliación funcional integrada B/adaptador/F1–F2/A1–A2/F* (2026-11-06)

**Estado:** RECONCILIACIÓN DOCUMENTAL / PROPUESTA OPERACIONAL; NO CONGELADA, NO IMPLEMENTADA, NO VALIDADA. No modifica DEC-C10-051 ni decisiones posteriores.

### 11.1. Precedencia y objetos no colapsables

Se reutilizan estas fichas, la matriz F* (C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md), el manifiesto B (C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md), el contrato abstracto de instancia y la matriz IAM. No se crea una segunda definición de F1/F2/A1/A2.

| Objeto | Función | Acredita | No acredita |
|---|---|---|---|
| B/adaptador | Provisionar dependencia focal, runtime/canal y verificar estado técnico | Política y provisión documentada | Ejecutar F1/F2, aplicación, accesibilidad completa o F*=1 |
| C_dep* | Estado técnico de instalación, integridad, compatibilidad y operación | Dependencia técnica | A_f*, rutas completas, aplicabilidad ni éxito funcional |
| F1/τ2 | Conversión focal S0→S2 | Resultado local y artefacto intermedio | Aplicación, F2 ni F* completo |
| F2 | Aplicar S2→SF y verificar destino | Aplicación/verificación local | Accesibilidad de F1 ni substituibilidad |
| A1→A2 | Ruta alternativa basal S0→S1→SF | Capacidad alternativa si satisface el mismo F* | Independencia respecto de B sin evidencia |
| F* | Evaluación de ruta completa desde fuente admisible a configuración aplicada/verificada | Conformidad funcional bajo IAM/C0/G/H | Accesibilidad TGCV, ausencia de vías colaterales, Outcome o Value |

### 11.2. Secuencia causal/funcional

1. Antes de Z/B se sellan fuente, destino, versiones, mapping, unidad/frontera, IAM, C0, alternativas y condiciones basales.
2. B provisiona y registra el estado técnico; no ejecuta F1/F2/A1/A2 ni modifica fuente, destino, F*, oráculo o alternativa.
3. A_f*(τ2) se adjudica con predicados completos; adaptador presente o C_dep*=1 no bastan.
4. F1 se ejecuta solo tras selección/inicio y produce S2; S2 no equivale a C_dst aplicado.
5. F2 aplica S2 y verifica destino, con precondiciones y fallos propios.
6. A1/A2 se ejecutan por su ruta basal y se evalúan bajo entrada/contexto comparables.
7. F* se adjudica sobre la ruta completa. FP-01…FP-07 son dimensiones funcionales no compensatorias; FP-08 es gate probatorio separado. Outcome/Value quedan fuera del oráculo.

### 11.3. Alternativa genuina y R1/R2

A1→A2 debe existir dentro de la frontera/universo declarado, estar identificada/versionada, ser mecanísticamente distinta, partir de la misma clase de entradas y contexto C0, alcanzar el mismo destino y satisfacer el mismo F*, IAM, H y G. Su independencia requiere evidencia de no-afectación por B sobre dependencias transitivas, permisos, recursos, configuración, red, rendimiento y calidad, con márgenes preespecificados y cobertura suficiente. Un hash o nombre distinto no demuestra independencia; un estado nominal SF no demuestra F*.

R1 (alternativa basal funcional y estable) es distinto de R2 (alternativa modificada/degradada por B). La mera existencia de A1→A2 no viola exclusión; su modificación por B puede abrir una vía colateral. Sin cobertura completa, F_alt queda ?.

### 11.4. Definido frente a abierto

| Dominio | Definido documentalmente | Abierto |
|---|---|---|
| B/adaptador | No ejecuta transformaciones; clases M01–15; snapshots; aislamiento recomendado para evaluar | Implementación/hash/versiones reales, grafo transitivo, permisos efectivos, cuotas, red, residuos y no-afectación |
| F1/τ2 | Rol focal, S0→S2, separación provisión/ejecución | TID/SID/RID, formato, mapping, aplicabilidad, recursos, ventana, tolerancias y evidencia |
| F2 | S2→SF, aplicación y verificación separadas | Contrato, atomicidad, permisos, compatibilidad, rollback y criterios de verificación |
| A1/A2 | Ruta S0→S1→SF | Mecanismos/formatos, mapping, cobertura, dependencias y no-afectación por B |
| F* | Ruta completa, familias FP, adjudicación no compensatoria | IAM de instancia, predicados, obligatoriedad, mappings, tolerancias, C0/G/H, oráculo, cegamiento y error |

### 11.5. Dictamen

La semántica de alto nivel de las transformaciones está definida suficientemente para orientar el DGP; no está cerrada para generar instancias confirmatorias. El siguiente trabajo es reconciliar C_src/C_dst/M con F1/F2/A1/A2, IAM, FP-01…FP-08 y manifiesto B, resolviendo discrepancias de cardinalidad, mapping, frontera y evidencia. No asignar parámetros ni generar fixtures todavía. Sin freeze, implementación, validación, simulación ni ejecución autorizada.



## 12. Corrección de cabecera y reconciliación decisional (2026-11-06)

La cabecera de §1 conserva texto histórico que describía Opción A como no seleccionada/no aprobada. Esa formulación quedó supersedida por la selección de Opción A registrada en DEC-C10-051 y reiterada en la consolidación vigente. Interpretación correcta: **Opción A seleccionada como microdominio de trabajo; F* contrato funcional candidato; fichas Draft, no congeladas ni ejecutables.** La selección no aprueba formatos, productos, versiones, parámetros, umbrales, recursos, permisos o implementación. Esta nota resuelve la precedencia sin borrar el historial.


## 12. Encaje de RUL en F1/F2/A1/A2 y F*

RUL forma parte del paquete P0 migrado. F1/A1 preservan significado, referencias, dominio, scope, versión y efecto en la representación intermedia; F2/A2 aplican la configuración y la regla en destino bajo el mismo contrato funcional. Para RUL-SVC-ENABLE-PROFILE-01 deben preservarse los perfiles permitidos STANDARD/READ_ONLY y el contraste violador DISABLED cuando ENABLED=true. FP-03 evalúa preservación semántica; FP-06 aplicación efectiva; FP-07 verificación post-aplicación; FP-08 trazabilidad probatoria.

Una regla que sobrevive textualmente pero pierde un operando, cambia scope/efecto, queda sin aplicar o resuelve UNKNOWN como booleano puede hacer F*=0 o ?, según suficiencia y cobertura. La verdad funcional del DGP procede del contrato sintético fijado ex ante; no se infiere de resultados de ruta. La misma versión contractual se aplica a ruta focal y alternativa. Esta especificación no congela F*, mapping, tolerancias ni oráculo.

## 13. Roster documental de instancia y superficies para el crosswalk X/C

El maestro §232 consolida el roster parcial. La identidad contractual de referencia sigue DEC-C10-069; ENABLED/PROFILE son PAR nucleares; RETRY-COUNT es slot candidato, no confirmatorio; REF no se presume vacío hasta IAM/cobertura. Las superficies B-M01…15 se tipan por subcampo y función: runtime/host/estado persistente pueden aportar X*; reglas, ACL, cuotas y bloqueos son C*; topología/interfaz es R*; transformaciones A/F son U*; logs, hashes, cobertura y oráculo son E_T.

No se fijan valores ni variables reales de contexto. El roster es documental parcial; el inventario por unidad/versión y el matching de snapshots permanecen OPEN. No se aprueban fixtures ni ejecución.

## 12. Paquete integrado AB-03/04 — cuatro cards sintéticas y crosswalk de campos (2026-11-10)

**Estado:** instancia de diseño sintética autorizada por la aceptación AB-03-SYN; esta sección define semántica funcional abstracta del DGP, no mecanismo técnico real, producto, formato, implementación ni evidencia observada. No modifica las decisiones canónicas de F*, IAM, identidad de servicio ni C10-D1.

### 12.1. Convención de identidad sintética

Se instancian cuatro TID propios del microdominio sintético, usando el esquema de identidad TID/SID ya propuesto. Las identidades son semánticas del DGP; no afirman que exista una realización técnica:

| Alias | TID sintética | SID sintética | Revisión de card | RID/EID |
|---|---|---|---|---|
| F1 / τ2 | `tr:tgcv-c10s-syn:0001` | `sp:tgcv-c10s-syn:0001:1.0.0` | 1 | No asignados: no hay implementación ni ejecución |
| F2 | `tr:tgcv-c10s-syn:0002` | `sp:tgcv-c10s-syn:0002:1.0.0` | 1 | No asignados |
| A1 | `tr:tgcv-c10s-syn:0003` | `sp:tgcv-c10s-syn:0003:1.0.0` | 1 | No asignados |
| A2 | `tr:tgcv-c10s-syn:0004` | `sp:tgcv-c10s-syn:0004:1.0.0` | 1 | No asignados |

Los TID identifican operaciones funcionales distintas. SID versiona el contrato abstracto. RID solo podrá asignarse a una realización concreta si en una fase posterior se elige y documenta; EID solo a un intento/ejecución identificable. No codificar brazo, tiempo, unidad, resultado, Outcome o Value en los IDs.

La decisión histórica de que F2/A1/A2 carecían de semántica queda preservada como diagnóstico del estado anterior. La aceptación expresa de AB-03-SYN habilita ahora esta **instanciación sintética abstracta**; no autoriza rellenar mecanismos físicos ni trasladar estas identidades al mundo real.

### 12.2. Contrato común de las cuatro cards

- **Objeto común:** instancia lógica de configuración `C10S-SVC-REQUEST-PROCESSOR`, contrato `1.0.0`, instancia `C10S-SVC-REQUEST-PROCESSOR-001`, revisión `1`; CMP `CMP-SERVICE-LOGIC-001`; PAR `PAR-SVC-ENABLED` (BOOL) y `PAR-SVC-PROFILE` (ENUM); RUL `RUL-SVC-ENABLE-PROFILE-01`. RETRY-COUNT queda fuera del núcleo.
- **Dominio de entrada:** configuración fuente S0 admisible bajo su contrato y C0 pre-Z declarado. No se fijan valores de parámetros, formato físico, plataforma ni versión de software.
- **Destino común:** contrato de destino declarado y snapshot basal del entorno destino. C_src, C_dst declarado y C_dst aplicado permanecen objetos distintos.
- **Criterio común:** F* de ruta completa, con FP-01…FP-07 no compensatorios y FP-08 como gate probatorio separado. La regla RUL y los dos PAR deben preservarse semánticamente según mapping M; la conformidad local de una card no implica F*=1.
- **Reloj:** estados S0/S1/S2/SF son estados lógicos del DGP. H_path es profundidad de ruta; H_time, ancla, valor y unidad siguen OPEN. No se asignan duraciones ni tolerancias.
- **Ceguera:** truth, mappings generadores y potenciales permanecen en Generator; Analyzer recibe solo campos observables y evidencia permitida; Evaluator compara después de congelar la salida del Analyzer.

### 12.3. Card F1 / τ2 — conversión focal (S0 → S2)

| Campo | Especificación sintética |
|---|---|
| Propósito/operación | Transformar la representación declarativa de la instancia fuente S0 en una representación intermedia S2 consumible por F2, conforme al mapping M versionado |
| Entrada | S0; contrato/versión de origen; identidad/versión de instancia; mapping M; snapshot C0 |
| Salida | S2; referencia a S0 y M; registro de conversión y cobertura de propiedades transformadas |
| Precondiciones de aplicabilidad | S0 dentro del dominio declarado; CMP/PAR/RUL requeridos resolubles; mapping definido para todos los campos obligatorios aplicables; ausencia de contradicción contractual no adjudicada |
| Postcondiciones locales | S2 queda estructuralmente representado; los dos PAR y la RUL conservan sus tipos, dominios y bindings semánticos; pérdidas/transformaciones quedan declaradas; ningún estado de aplicación en destino se infiere |
| Accesibilidad | A_f*(F1) se evalúa por ID, REL, COND, AUTH, RES, DEP y ¬BLOCK. B/C_dep no ejecutan F1 ni equivalen a A_f*=1 |
| Evento | F1_ATTEMPT y resultado local SUCCESS/FAIL/UNKNOWN, separados de provisión, instalación y aplicación |
| Fallos | S0 fuera de dominio; mapping incompleto/ambiguo; binding AST→PAR no resoluble; integridad de entrada no demostrada; bloqueo o recurso/autorización insuficiente; salida no conforme |
| Límite | S2 no equivale a C_dst aplicado, F2 accesible ni F*=1 |

### 12.4. Card F2 — aplicación y verificación focal (S2 → SF)

| Campo | Especificación sintética |
|---|---|
| Propósito/operación | Aplicar en el entorno destino la representación S2 producida por F1 y verificar el estado aplicado contra el contrato destino y F* |
| Entrada | S2 validado; contrato destino; snapshot del destino; C0; mapping M |
| Salida | C_dst aplicado (si la aplicación tiene éxito) y resultado de verificación independiente; o estado de fallo/rollback registrado |
| Precondiciones de aplicabilidad | S2 satisface su contrato de entrada; destino pertenece al dominio declarado; permiso de aplicación, ventana y condiciones de estado requeridas están satisfechas; no hay bloqueo impeditivo |
| Postcondiciones locales | Estado aplicado se registra separadamente del destino declarado; verificación evalúa propiedades obligatorias aplicables, incluyendo semántica de CMP/PAR/RUL, integridad, compatibilidad, seguridad, aplicación y post-check |
| Accesibilidad | A_f*(F2) se evalúa independientemente de F1; no se deduce de A_f*(F1), C_dep ni de la producción de S2 |
| Evento | F2_ATTEMPT, APPLY_RESULT y VERIFY_RESULT, con orden temporal y procedencia |
| Fallos | Destino incompatible; permiso/ventana ausente; conflicto con estado destino; aplicación parcial; rollback/residuo; verificación fallida o desconocida |
| Límite | Un PASS local de F2 no acredita substituibilidad de la ruta A ni ausencia de vías colaterales de B |

### 12.5. Card A1 — exportación alternativa basal (S0 → S1)

| Campo | Especificación sintética |
|---|---|
| Propósito/operación | Producir desde S0 una representación de intercambio S1 mediante la capacidad alternativa declarada como disponible en baseline, sin utilizar la provisión focal B |
| Entrada | El mismo S0, contrato/versión de origen, instancia lógica y C0 que la ruta focal |
| Salida | S1 con referencia a la fuente, contrato de intercambio abstracto, mapping M_A y procedencia |
| Precondiciones de aplicabilidad | Capacidad de exportación alternativa presente en el escenario; permiso de lectura; dominio y mapping de exportación declarados; recursos/ventana requeridos disponibles |
| Postcondiciones locales | S1 cubre los campos obligatorios declarados para el intercambio; los campos omitidos, transformados o no representables se registran explícitamente; no se presume que A2 pueda importarlo |
| Accesibilidad | A_f*(A1) independiente; baseline en R1 se estipula solo en la verdad del DGP, no se acredita como evidencia material |
| Evento | A1_ATTEMPT y resultado local SUCCESS/FAIL/UNKNOWN |
| Fallos | Exportación no disponible; permiso ausente; cobertura incompleta; mapping ambiguo; pérdida semántica o salida no verificable |
| Límite | S1 no acredita aplicación, compatibilidad final, F* ni independencia material frente a B |

### 12.6. Card A2 — importación, aplicación y verificación alternativa (S1 → SF)

| Campo | Especificación sintética |
|---|---|
| Propósito/operación | Consumir S1 mediante la capacidad alternativa declarada en baseline, aplicar la configuración en el mismo destino y verificar el mismo F* |
| Entrada | S1 producido por A1; contrato destino; snapshot del destino; C0; mapping M_A→dst |
| Salida | C_dst aplicado y resultado de verificación, o fallo/rollback registrado |
| Precondiciones de aplicabilidad | S1 íntegro y dentro del dominio de importación; capacidad alternativa de importación/aplicación; permiso, ventana, compatibilidad y recursos declarados |
| Postcondiciones locales | Aplicación y verificación se registran por separado; el resultado se adjudica con las mismas propiedades obligatorias, reglas de seguridad, tolerancias y oráculo que F2 |
| Accesibilidad | A_f*(A2) independiente de A1 y de F2; no se presume que la ruta alternativa sea funcional por su mera topología |
| Evento | A2_ATTEMPT, APPLY_RESULT y VERIFY_RESULT |
| Fallos | S1 no admisible; mapping incompleto; capacidad/importación no disponible; permiso/ventana ausente; aplicación parcial; rollback/residuo; verificación fallida/desconocida |
| Límite | Alcanzar SF nominal no acredita substituibilidad; solo la evaluación común de F* permite clasificarla |

### 12.7. Relaciones, rutas y límites causales

- Rutas candidatas: πF=(F1,F2) y πA=(A1,A2), ambas de dos pasos; no se añade un paso artificial para consumir H_path.
- Relaciones composicionales sintéticas: REL(F1,F2) y REL(A1,A2). Las relaciones técnicas/dependencias internas se añaden solo si el inventario sintético las declara; no se inventan REF.
- Ambas rutas usan misma clase de S0, instancia contractual, destino, IAM, C0, G, F*, oráculo y regla de adjudicación. H_time permanece sin fijar.
- R0: la no-afectación de A1/A2 por B es verdad estipulada del DGP aislado. R2: incluir al menos una modificación colateral de la alternativa/dependencia compartida. Ninguna estipulación equivale a evidencia observada.
- B provisiona dependencia focal para F1; no ejecuta F1/F2 ni A1/A2. La distribución de C_dep y sus cuatro componentes sigue pendiente de parametrización.
- La existencia sintética de πA no prueba que sea alternativa funcional: esa condición requiere truth F* y, para un sistema real, cobertura/evidencia material.

### 12.8. Crosswalk field-level para las cuatro cards

Los siguientes son **field_id semánticos del DGP**, no nombres de columnas ni un schema físico. Cada registro se indexará por unidad, escenario, branch_id, step_k, TID/SID, snapshot exacto, tiempo de evaluación y fuente/versión. Truth_DGP y observed_state se almacenan en canales separados.

| field_id semántico | Contenido | Clase U*/R*/C*/X*/E_T | Predicado/uso | Límite |
|---|---|---|---|---|
| SYN-U-TID | Identidad semántica de F1/F2/A1/A2 | U* | ID | No confundir con RID/hash |
| SYN-U-SID | Revisión contractual de la transformación | U*/MET | ID, comparabilidad | No implica implementación |
| SYN-U-RID | Realización técnica, si llegara a existir | E_T/MET | Provenance | Actualmente NOT_ASSIGNED |
| SYN-R-COMPOSES | Arista ordenada F1→F2 o A1→A2 | R* | REL | No crea rutas cruzadas |
| SYN-R-DEPENDS | Dependencia/interface necesaria, solo si declarada | R* | DEP/REL | Vacío solo con roster/cobertura exhaustivos; de otro modo ? |
| SYN-C-COND | Condición constitutiva de realizabilidad | C* | COND | No absorber App ni Outcome |
| SYN-C-AUTH | Autorización funcional basal por actor/objeto/ventana | C* | AUTH_f* | Separada de ACL técnica de B |
| SYN-C-RES | Oferta/capacidad ex ante reservable | C* | RES_f* | No confundir con consumo de ejecución |
| SYN-C-DEP | Estado técnico conjunto de dependencia | C* | DEP_f*/C_dep* | Mantener install/integrity/compat/oper separados |
| SYN-C-BLOCK | Bloqueo efectivo | C* | BLOCK_f* | Falta de evidencia no equivale a bloqueo |
| SYN-C-APP | Precondición desde estado de entrada | C* solo si constitutiva; si state-specific, registro APP separado | APP | No entra automáticamente en A_f* |
| SYN-X-CONTEXT | Estado efectivo runtime/host/contexto que altera accesibilidad | X* | Revisión de A_f* | Solo con regla causal/semántica; no usar como cubo residual |
| SYN-STATE-IN | Estado lógico de entrada S0/S1/S2 | Snapshot/step | APP | No es Outcome |
| SYN-STATE-OUT | Estado lógico de salida S1/S2/SF | Snapshot/step | Postcondición | SF nominal no equivale a F* |
| SYN-M-MAPPING | Mapping contractual de propiedades CMP/PAR/RUL | MET/contrato; sus relaciones se tipan según contenido | FP-03, integridad | No asumir mapping total ni tolerancias |
| SYN-E-SNAPSHOT | Snapshot exacto y versión de objeto | E_T | Matching temporal | No inferir diff sin comparabilidad |
| SYN-E-EVIDENCE | Fuente, procedencia, método, timestamp y resultado observado | E_T | Observación/adjudicación | Nunca contiene hidden_truth para Analyzer |
| SYN-E-COVERAGE | Universo, alcance, límites y cobertura | E_T | 1/0/? observado | Cobertura incompleta propaga ? |
| SYN-E-ADJUDICATION | Evaluador, desacuerdo, regla y decisión | E_T | FP-08 | No sustituye evidencia primaria |

### 12.9. Crosswalk por etapa y predicado

| Card | ID | REL | COND | AUTH | RES | DEP | ¬BLOCK | APP desde entrada | E_T mínimo |
|---|---|---|---|---|---|---|---|---|---|
| F1 | TID/SID F1 y continuidad | Composición posterior F1→F2 | Dominio y condiciones de conversión | AUTH_f* focal | Oferta ex ante necesaria | C_dep focal y relaciones requeridas | Bloqueo de F1 | App(F1,S0) | snapshot S0/S2, mapping, cobertura, intento |
| F2 | TID/SID F2 | Entrada S2 desde F1 | Compatibilidad/estado destino | Autorización de aplicación | Recursos/ventana | Dependencias propias de F2 | Bloqueo de F2 | App(F2,S2) | snapshot destino pre/post, apply y verify |
| A1 | TID/SID A1 | Composición posterior A1→A2 | Dominio/condiciones de exportación | Permiso de lectura | Recursos/ventana | Dependencias baseline | Bloqueo de A1 | App(A1,S0) | snapshot S0/S1, mapping/cobertura, intento |
| A2 | TID/SID A2 | Entrada S1 desde A1 | Compatibilidad/estado destino | Permiso de aplicación | Recursos/ventana | Dependencias baseline de A2 | Bloqueo de A2 | App(A2,S1) | snapshot destino pre/post, apply y verify |

**Regla de adjudicación:** cada predicado conserva truth_DGP y observed_state separados. Para truth, conjunción constitutiva 0 si algún requisito necesario es 0, 1 si todos son 1, ? si no hay 0 y alguno es ?. Para observado, se requiere cobertura suficiente; ausencia de evidencia no es 0. Para Reach, 1 si existe ruta completa 1; 0 solo si todas las rutas del universo declarado son 0 y la cobertura es exhaustiva; en otro caso ?. Se reutilizan PM-01…18, no se crea una segunda lógica.

### 12.10. Pendientes explícitos tras completar la definición abstracta

Quedan abiertos, y no se rellenan en este bloque: encoding/schema físico; mapping M y M_A concretos; catálogo de propiedades atómicas obligatorias FP-01…07; tolerancias; valores de PAR; REF y dependencias internas; C0 detallado; recursos/demanda/regla de reserva; valores conjuntos C_dep; H_time; universo exhaustivo de alternativas; truth tables por escenario; evidencia MD-C1/MD-C4; oráculo, fiabilidad, cegamiento y validación. No se asignan estados por unidad ni se generan fixtures.

**Dictamen:** AB-03 queda DESIGN SPECIFIED AT ABSTRACT SYNTHETIC LEVEL; AB-04 queda FIELD-LEVEL CROSSWALK SPECIFIED AT SEMANTIC LEVEL. Ambos siguen OPEN para schema físico, instanciación de verdad/observación, evidencia, validación y cierre AB. Sin Design Freeze, implementación, fixtures, simulación ni ejecución científica.
