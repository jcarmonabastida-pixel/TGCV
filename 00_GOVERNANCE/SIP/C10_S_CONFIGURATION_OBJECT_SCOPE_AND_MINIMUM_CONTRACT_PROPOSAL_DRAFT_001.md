# C10-S — Delimitación del objeto de configuración y contrato mínimo: propuesta

**ID:** C10-S-CONFIG-SCOPE-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta para decisión; NO seleccionada como subdominio técnico, NO congelada, NO implementada, NO validada.  
**Decisión marco:** DEC-C10-051 selecciona Opción A (migración de configuración entre dos entornos software); esta propuesta delimita el objeto que se migraría, sin modificar esa decisión.

## 1. Decisión que falta

«Migración de configuración entre dos entornos software» delimita el tipo general de operación, pero aún no define qué clase de configuración contiene el objeto. Sin esa delimitación no pueden cerrarse invariantes semánticas SM-01…SM-10, mappings, predicados atómicos FP-03 ni condiciones de aplicabilidad de F1/F2/A1/A2.

La selección del objeto debe permitir:
- una función F* técnica observable e independiente de Outcome/Value;
- propiedades semánticas no triviales, pero acotadas;
- diferencias representacionales entre entornos sin exigir igualdad byte a byte;
- dependencias, permisos y recursos que puedan separarse del contenido migrado;
- rutas focal y alternativa genuinamente distintas;
- un DGP sintético parsimonioso, sin depender de productos o sistemas reales.

## 2. Clases candidatas

| Candidata | Objeto migrado | Ventaja | Riesgo para C10-S |
|---|---|---|---|
| A. Paquete de configuración de un servicio software | Identidad del componente, parámetros tipados, referencias/dependencias, restricciones/reglas y políticas asociadas | Permite probar tipos, defaults, referencias, reglas, compatibilidad y preservación semántica con un único objeto acotado | Requiere fijar qué reglas y propiedades son funcionalmente significativas |
| B. Perfil de despliegue/infraestructura | Recursos, instancias, dependencias, endpoints, límites y políticas de despliegue | Hace visibles recursos, capacidad y restricciones del entorno | Puede mezclar el objeto migrado con los recursos/capacidad del entorno que deben permanecer como condiciones causales separadas |
| C. Paquete de integración entre servicios | Endpoints, protocolos, mappings de mensajes, credenciales referenciadas y reglas de intercambio | Proporciona relaciones y mappings ricos | Añade complejidad de protocolos, seguridad y comportamiento de integración, elevando el número de vías colaterales |

Escala cualitativa de diseño; no son resultados empíricos ni una evaluación de sistemas reales.

## 3. Recomendación: candidata A

Se recomienda **A. Paquete de configuración de un servicio software**, limitado a una especificación abstracta y sintética. No se elige ningún producto, formato, lenguaje, plataforma ni tecnología.

### 3.1 Contenido lógico mínimo del objeto

| Elemento | Contenido abstracto | Propiedades semánticas que permite evaluar |
|---|---|---|
| Componente | Identificador estable y clase funcional declarada | Identidad y correspondencia |
| Parámetro | Clave, tipo, valor, unidad si aplica, obligatoriedad y default | Tipos, dominios, unidades, null/ausencia/default |
| Referencia | Relación tipada con otro componente o recurso declarado | Integridad referencial, multiplicidad y dependencia |
| Regla/restricción | Condición declarativa, ámbito y efecto esperado | Operadores, precedencia, restricciones y semántica operativa |
| Política asociada | Rol/ámbito/operación autorizada, si aplica | Preservación de control y separación de FP-05 |
| Metadatos contractuales | Versión de esquema, procedencia y compatibilidad declarada | Identidad/versionado y compatibilidad |

El conjunto es un modelo de contenido candidato del objeto fuente/destino; **no** es una capa semántica persistida adicional entre el sistema y TGCV. Las tablas/mappings sirven como contrato de comparación y evidencia, no como tercer sistema operativo.

### 3.2 Lo que queda fuera del objeto

Para no confundir tratamiento, accesibilidad y resultado, quedan fuera del paquete migrado y se modelan como contexto/condiciones independientes cuando proceda:
- capacidad y disponibilidad de CPU, memoria, almacenamiento u otros recursos del entorno;
- permisos efectivos de la unidad/agente que intenta la operación;
- ventanas de mantenimiento y disponibilidad temporal del entorno;
- estado operativo del entorno destino;
- éxito de instalación/provisión del adaptador focal;
- ejecución de conversión, importación o aplicación;
- Outcome y Value.

La presencia de referencias a recursos o permisos dentro del paquete no equivale a que los recursos existan o los permisos estén efectivamente concedidos. Se distinguen configuración declarada y condición efectiva del entorno.

## 4. Contrato funcional mínimo F* propuesto

Dada una configuración fuente admisible (C_s), un contrato fuente, un contrato destino y un contexto C0 preespecificado, la ruta completa debe producir y dejar aplicada una configuración destino (C_d) tal que:

1. todos los componentes y parámetros obligatorios tienen correspondencia semántica definida;
2. tipos, dominios, unidades y valores se preservan o transforman mediante reglas explícitas;
3. referencias y dependencias obligatorias permanecen íntegras y apuntan a los equivalentes correctos;
4. reglas/restricciones obligatorias conservan su lógica y ámbito;
5. defaults, ausencia, null y opcionalidad mantienen las distinciones declaradas como significativas;
6. políticas asociadas no se amplían ni debilitan inadvertidamente; su cumplimiento se evalúa además por FP-05;
7. el entorno destino acepta y aplica la configuración;
8. el estado aplicado satisface el contrato destino y las invariantes anteriores.

No se fijan aún listas de campos, valores, reglas, cantidades, tolerancias ni casos de prueba. La lista de propiedades se debe cerrar ex ante antes del DGP confirmatorio. La conformidad es no compensatoria y trivalente según la matriz F*.

## 5. Implicaciones para FP-03

Si se adopta esta candidata, el catálogo SM-01…SM-10 se especializaría así:
- SM-01: correspondencia de componentes y parámetros.
- SM-02: tipos, valores, unidades y dominios.
- SM-03: referencias y dependencias.
- SM-04: ausencia, null, default y opcionalidad.
- SM-05: cardinalidad de referencias/colecciones.
- SM-06: orden solo si alguna colección tiene semántica de precedencia.
- SM-07: reglas y restricciones declarativas.
- SM-08: solo si el objeto incluye vigencia/activación temporal; no se presupone.
- SM-09: políticas declaradas; cumplimiento efectivo se contrasta también con FP-05.
- SM-10: extensiones desconocidas, con regla explícita de preservar/rechazar/ignorar.

No todas las dimensiones deben declararse obligatorias. La decisión de aplicabilidad y obligatoriedad se fija por el contrato del objeto, no por conveniencia posterior.

## 6. Separación de objeto, entorno y proceso

| Capa | Contenido | No debe confundirse con |
|---|---|---|
| Objeto de configuración | Componentes, parámetros, referencias, reglas y políticas declaradas | Capacidad/estado real del entorno |
| Entorno fuente/destino | Versiones, capacidades, dependencias instaladas, permisos efectivos y recursos | Contenido migrado |
| Provisión B | Disponibilidad/configuración de dependencia técnica focal | Ejecución de transformación |
| Transformación | Conversión/exportación/importación/aplicación según contratos que se decidan | Accesibilidad basal |
| Evaluación F* | Conformidad del estado aplicado frente al contrato | Outcome/Value |

La matriz causal deberá mantener por separado las variables de estas capas. En particular, no se debe incluir dentro de F* una propiedad que haga que B sea exitoso por definición.

## 7. Condiciones para que el objeto sea adecuado

La candidata solo será aceptable si el futuro diseño puede demostrar documentalmente:
1. el dominio de entrada está acotado;
2. las propiedades funcionales obligatorias pueden observarse sin usar Outcome/Value;
3. existen mappings y casos de pérdida semántica que pueden falsar FP-03;
4. la ruta alternativa puede definirse sin reutilizar el mismo mecanismo focal;
5. la provisión B no ejecuta ni valida la migración;
6. recursos, permisos, dependencias y ventanas pueden modelarse fuera del objeto cuando sean condiciones causales;
7. el contrato no depende de un producto concreto ni de un entorno real;
8. el modelo es suficientemente pequeño para un DGP manejable, pero permite distinguir ACC, APP, Reach, ejecución y F*.

## 8. Decisiones aún necesarias

1. Seleccionar A, B o C como clase del objeto de configuración.
2. Si se selecciona A, aprobar o modificar los seis elementos lógicos de §3.1.
3. Determinar qué propiedades de §4 son obligatorias, condicionales o NA.
4. Delimitar la clase de entradas admisibles y los contratos fuente/destino.
5. Decidir qué reglas declarativas tienen semántica operacional y cómo se comparan.
6. Fijar qué elementos del entorno son condiciones basales, mediadores potenciales o efectos colaterales de B.
7. Solo después, cerrar mappings atómicos, tolerancias, envolvente de observación y oráculo.

## 9. Dictamen y límites

La candidata A es la recomendación de menor complejidad para concretar FP-03 sin incorporar un dominio humano ni un producto específico. Separa el contenido migrado de recursos, permisos efectivos, estado del entorno, provisión y ejecución.

**No se adopta automáticamente.** La selección requiere decisión explícita del usuario. DEC-C10-051 permanece intacta: el microdominio general sigue siendo migración de configuración entre entornos software. Esta propuesta solo pretende fijar la clase del objeto y el contrato mínimo.

No hay inventario real, TID/SID/RID, implementación, fixtures, validación técnica, simulación, experimento ni evidencia empírica. `scientific_execution=false`; `execution_authorized=false`.
