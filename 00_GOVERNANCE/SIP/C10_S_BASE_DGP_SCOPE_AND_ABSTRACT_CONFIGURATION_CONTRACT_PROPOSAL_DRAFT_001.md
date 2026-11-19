# C10-S — Alcance del DGP base y contrato abstracto de configuración: propuesta

**ID:** C10-S-DGP-BASE-CONTRACT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** partición del DGP base aprobada por decisión explícita del usuario (DEC-C10-053); contrato abstracto y predicados aún candidatos; NO congelado, NO implementado, NO validado.  
**Propósito inmediato:** reducir la indeterminación del objeto y de FP-03 para poder completar el DGP sin asignar truth ni parámetros empíricos prematuramente.

## 1. Decisiones marco que se preservan

- DEC-C10-051: el microdominio es migración de configuración entre dos entornos software.
- DEC-C10-052: el objeto es un paquete de configuración de un servicio software con seis elementos conceptuales: componente, parámetros tipados, referencias, reglas/restricciones, políticas asociadas y metadatos contractuales.
- La configuración declarada se distingue de dependencias instaladas, permisos efectivos, recursos/capacidad, estado del entorno, provisión B, ejecución, Outcome y Value.
- El objeto seleccionado no implica elegir plataforma, producto, formato, lenguaje ni sistema real.
- La propuesta no autoriza ejecución, fixtures, generación de truth ni simulación.

## 2. Recomendación para el DGP base

Se recomienda un paquete finito y cerrado por contrato, con cuatro familias funcionales constitutivas y dos familias condicionales:

| Familia | Tratamiento propuesto en DGP base | Razón |
|---|---|---|
| Componente (CMP) | Constitutiva | Fija identidad funcional y ámbito del paquete |
| Parámetros tipados (PAR) | Constitutiva | Permite evaluar tipos, valores, dominios y distinciones ausencia/null/default |
| Referencias (REF) | Constitutiva | Permite evaluar relaciones, extremos y dependencias declaradas |
| Reglas/restricciones (RUL) | Constitutiva, con gramática mínima | Necesaria para que preservación semántica no se reduzca a copia estructural |
| Políticas asociadas (POL) | Condicional; fuera del núcleo confirmatorio mínimo | Su inclusión añade seguridad/roles como vía adicional; conservarlas como módulo/escenario adversarial separado |
| Metadatos contractuales (MET) | Metadatos obligatorios de evaluación; extensiones desconocidas condicionales | Versionado/procedencia necesarios para trazabilidad, pero no deben contaminar el contenido funcional |

Esta partición no elimina POL del objeto conceptual adoptado. Significa que el paquete base puede declarar explícitamente que no contiene políticas migrables, mientras que escenarios secundarios incorporan políticas para probar preservación y separación FP-03/FP-05. No se permite declarar NA después de observar resultados.

## 3. Alcance semántico mínimo recomendado

### 3.1 Constitutivo

1. **Identidad del componente:** un conjunto finito de componentes declarados, cada uno con identificador de instancia y clase/rol funcional contractual. Los identificadores físicos pueden cambiar si existe mapping funcional explícito.
2. **Parámetros:** conjunto finito de parámetros con clave, tipo, valor, obligatoriedad y semántica explícita de ausencia/null/default. Unidades solo cuando el tipo/contrato las defina.
3. **Referencias:** relaciones tipadas entre componentes del paquete o recursos declarados. Se fija si cada relación es dirigida/no dirigida y su multiplicidad contractual.
4. **Reglas/restricciones:** expresiones declarativas de gramática acotada, con operandos, operadores, ámbito y efecto. No se introduce un lenguaje de programación general ni ejecución arbitraria de código.

### 3.2 Condicional o adversarial

5. **Políticas:** roles, ámbitos y reglas allow/deny. Se incorporan en una capa de escenarios si se quiere estudiar su preservación; el cumplimiento de seguridad destino se adjudica por FP-05, no por FP-03.
6. **Orden/precedencia:** solo si el contrato declara que el orden altera el significado; de lo contrario, las colecciones son no ordenadas.
7. **Tiempo/vigencia:** solo si la clase de configuración elegida necesita semántica temporal.
8. **Extensiones desconocidas:** escenario adversarial de compatibilidad/preservación, con regla ex ante de conservar, rechazar o ignorar.
9. **Many-to-one / one-to-many:** escenarios de mapping adversarial, no requisito de que todas las instancias base contengan esos casos.

## 4. Contrato abstracto de origen y destino

Se propone que ambos contratos describan el mismo dominio funcional abstracto, pero puedan diferir en representación. No se fija aún una serialización.

### 4.1 Contrato fuente C_src

Declara:
- identidad/versionado del contrato fuente;
- conjunto de componentes y clases funcionales;
- parámetros tipados y sus dominios;
- distinción contractual entre ausente, null, valor explícito y default;
- referencias tipadas, extremos y multiplicidades;
- reglas declarativas con gramática, ámbito y efecto;
- política de extensiones y campos desconocidos;
- propiedades obligatorias y opcionales;
- snapshot de origen y procedencia.

### 4.2 Contrato destino C_dst

Declara:
- identidad/versionado del contrato destino;
- representaciones destino admitidas para cada familia;
- restricciones de tipos/dominios y reglas de conversión;
- correspondencias de componentes, parámetros y referencias;
- tratamiento de ausente/null/default;
- representación destino de reglas y restricciones;
- compatibilidad del paquete con el entorno destino;
- política de campos desconocidos;
- propiedades que deben verificarse después de la aplicación;
- snapshot del estado efectivamente aplicado.

### 4.3 Contrato de correspondencia M

M es una especificación de evaluación versionada, no una capa operativa persistida adicional. Para cada entidad/propiedad origen debe declarar:
- correspondencia 1:1, 1:N, N:1 o N:M;
- regla de transformación/conversión;
- preservación de tipo, valor, unidad y dominio;
- transformación de referencias y extremos;
- transformación de reglas;
- variaciones representacionales admitidas;
- condiciones de pérdida y rechazo;
- cobertura del mapping y elementos sin correspondencia.

No se acepta el mapping por el mero hecho de que el conversor lo haya producido. Las correspondencias ambiguas o sin cobertura suficiente permanecen ?.

## 5. Predicados mínimos para el DGP base

Los siguientes son predicados conceptuales candidatos; su formulación final deberá incorporar variables, dominios, cuantificadores y observabilidad:

- **BASE-CMP:** toda entidad funcional obligatoria del origen tiene correspondencia destino única o composición explícita permitida.
- **BASE-PAR-TYPE:** el tipo destino representa el mismo dominio funcional declarado.
- **BASE-PAR-VALUE:** el valor destino conserva el valor funcional bajo la regla de conversión.
- **BASE-PAR-STATE:** ausencia, null, default y valor explícito mantienen las distinciones declaradas significativas.
- **BASE-REF-ENDPOINT:** cada referencia obligatoria apunta al extremo destino correspondiente.
- **BASE-REF-RELATION:** tipo, dirección y multiplicidad contractual se conservan.
- **BASE-RULE-LOGIC:** condición, ámbito y efecto de cada regla obligatoria se preservan.
- **BASE-MAP-COVERAGE:** todos los elementos obligatorios del universo de entrada están cubiertos por una correspondencia definida.
- **BASE-APPLIED-STATE:** la adjudicación se realiza sobre el estado realmente aplicado, no solo sobre un artefacto intermedio (FP-06/07).

La pertenencia a esta lista no establece aún truth, prevalencia ni peso. Los predicados se evalúan con 1/0/? y NA solo por no aplicabilidad preespecificada. F* no es una media: cualquier propiedad obligatoria 0 implica F*=0; sin 0 pero con alguna obligatoria ? implica F*=?.

## 6. Diferencias representacionales admisibles

El contrato debe permitir que fuente y destino representen el mismo significado de forma distinta. Se propone admitir:
- identificadores físicos distintos con correspondencia funcional inequívoca;
- reordenación de campos/colecciones cuando el orden no sea semántico;
- cambio de nombre de clave mediante mapping explícito;
- conversión de tipo/escala únicamente con regla semántica declarada y sin pérdida no autorizada;
- descomposición o agregación de representaciones si la composición conserva todas las propiedades obligatorias.

No se presupone que ninguna de estas diferencias esté presente en el DGP base. Cada una debe quedar especificada antes de construir el escenario confirmatorio.

## 7. Falsadores mínimos que debe poder distinguir el DGP

1. Copia estructural correcta con valor semánticamente alterado.
2. Parámetro ausente convertido en default cuando el contrato distingue ambos.
3. Referencia conservada como texto pero apuntando a entidad funcional equivocada.
4. Regla con operador o ámbito cambiado.
5. Mapping parcial que omite una propiedad obligatoria.
6. Transformación many-to-one que fusiona dos categorías funcionalmente distintas.
7. Estado intermedio correcto pero estado aplicado final incorrecto.
8. Preservación funcional correcta con incompatibilidad del entorno (FP-04), para no confundir FP-03 con compatibilidad.
9. Preservación fiel de política insegura: FP-03 puede pasar y FP-05 fallar, en escenario condicional.
10. Falta de evidencia/cobertura que debe producir ?, no 0 ni 1.

Estos son requisitos de capacidad falsadora del diseño, no fixtures, datos, frecuencias ni resultados ejecutados.

## 8. Separación de roles FP-01…FP-08

- FP-01: conformidad de esquema/tipos de representación.
- FP-02: integridad estructural y referencial.
- FP-03: preservación del significado funcional declarado.
- FP-04: compatibilidad con entorno destino.
- FP-05: seguridad del resultado aplicado.
- FP-06: aplicación efectiva.
- FP-07: verificación del estado post-aplicación.
- FP-08: procedencia y reproducibilidad de la evaluación.

Una propiedad puede aportar evidencia a más de una familia, pero el mismo fallo no debe contarse dos veces como fallos independientes sin justificar la distinción. FP-03 se adjudica por significado; FP-01/02 por representación e integridad; FP-04/05 por condiciones del entorno/seguridad; FP-06/07 por estado de aplicación/verificación; FP-08 por trazabilidad.

## 9. Límites de identificación y protección contra circularidad

- El oráculo de F* no usa Outcome ni Value para adjudicar conformidad.
- El oráculo no recibe truth del generador ni Z/B cuando ello pueda sesgar la clasificación.
- Accesibilidad (A_f*/A_f_obs), aplicabilidad (App_f), Reach, selección, ejecución, F* y Outcome se mantienen como variables separadas.
- El éxito de B o C_dep no define por sí mismo accesibilidad ni F*.
- El estado nominal de destino no demuestra preservación semántica.
- El DGP debe poder producir escenarios en los que la provisión técnica tenga éxito y la preservación falle, y viceversa.
- La identificación de contribución causal de accesibilidad sigue dependiendo de la arquitectura causal global, no de que F* esté bien definido.

## 10. Decisiones aún abiertas

1. La partición constitutivo/condicional del §2 queda aprobada por DEC-C10-053; la formalización detallada sigue abierta.
2. Fijar la gramática mínima de reglas y el dominio de tipos/parámetros.
3. Decidir si el DGP base requiere una o varias entidades y qué clases funcionales se permiten.
4. Definir multiplicidad y direccionalidad de referencias.
5. Cerrar las distinciones ausencia/null/default y sus reglas.
6. Especificar el contrato de correspondencia M y las variaciones admitidas.
7. POL queda fuera del núcleo confirmatorio mínimo y se incorpora como módulo/escenario secundario, conforme a DEC-C10-053.
8. Definir el alcance del oráculo y su independencia/fiabilidad.
9. Reconciliar los predicados con F1/F2/A1/A2 sin asumir sus mecanismos técnicos.
10. Integrar el contrato resultante en DGP/estimandos una vez aprobadas las definiciones.

## 11. Dictamen

La propuesta reduce el objeto a un paquete funcional finito con cuatro familias constitutivas y módulos condicionales, y define las obligaciones mínimas de C_src, C_dst y M. Es suficiente para orientar la siguiente decisión y el trabajo de formalización; no constituye todavía un DGP completo.

**Estado:** OBJECT SELECTED; BASE FAMILY PARTITION APPROVED (DEC-C10-053); POL CONDITIONAL; METADATA TRACEABILITY REQUIRED; SOURCE/DESTINATION CONTRACTS STRUCTURED BUT NOT CLOSED; ATOMIC PREDICATES CANDIDATE; DOMAIN/GRAMMAR/CARDINALITY/NULL-DEFAULT RULES OPEN; MAPPING NOT SPECIFIED; ORACLE NOT VALIDATED; NO TECHNICAL VALIDATION; NO INDEPENDENT REVIEW; NO EMPIRICAL EVIDENCE; NO EXECUTION AUTHORIZATION.


## 12. Registro de decisión — DEC-C10-053 (2026-11-05)

**Decisión explícita del usuario:** se aprueba la partición propuesta para el DGP base:
- constitutivos: componentes, parámetros tipados, referencias y reglas/restricciones con gramática mínima;
- políticas asociadas (POL): fuera del núcleo confirmatorio mínimo, como módulo/escenario condicional secundario;
- metadatos contractuales: soporte obligatorio de identidad, versionado y procedencia; extensiones desconocidas condicionales.

La decisión mantiene intacta la estructura conceptual de seis elementos de DEC-C10-052. Que POL sea condicional no significa que se elimine del objeto; el escenario base deberá declarar ex ante si no hay políticas migrables. La regla de metadatos tampoco convierte las extensiones desconocidas en obligatorias.

**Alcance:** aprobación de la partición del DGP base para continuar la formalización documental. No aprueba aún la gramática de reglas, dominios de tipos/parámetros, número/clases de componentes, cardinalidad/direccionalidad de referencias, semántica ausencia/null/default, mappings, tolerancias, oráculo ni DGP completo.

**Límites:** no genera truth, parámetros empíricos, fixtures ni resultados; no valida FP-03/F*, no constituye revisión independiente ni evidencia empírica. `scientific_execution=false`; `execution_authorized=false`.

**Siguiente paso:** fijar una gramática declarativa mínima y finita para reglas/restricciones, junto con el dominio abstracto de tipos/parámetros, manteniendo los restantes puntos abiertos.
