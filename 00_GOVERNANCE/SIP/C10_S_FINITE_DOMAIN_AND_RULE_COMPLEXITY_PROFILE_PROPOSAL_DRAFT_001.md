# C10-S — Perfil de dominios finitos y límites de complejidad de reglas

**Estado:** PERFIL ESTRUCTURAL APROBADO — DEC-C10-054; dominios concretos por clave y mapping aún abiertos.

**ID:** C10-S-FINITE-DOMAIN-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA DOCUMENTAL — NO APROBADA / NO CONGELADA / NO IMPLEMENTADA / NO VALIDADA.  
**Dependencia:** DEC-C10-053; `C10_S_MINIMAL_RULE_GRAMMAR_AND_PARAMETER_TYPE_DOMAIN_PROPOSAL_DRAFT_001.md`.

## 1. Propósito y reconstrucción

Este documento concreta cómo hacer finitos los dominios y acotada la gramática sin elegir una tecnología, inventar valores observados ni convertir los parámetros del DGP en supuestos empíricos.

La revisión del Decision Log y de los contratos DGP/FP-01/02/03 no identifica límites numéricos, cardinalidades o presupuesto de complejidad previamente aceptados para este objeto. Por tanto, los límites que siguen son candidatos de diseño, no recuperación de decisiones históricas ni calibración.

## 2. Principio: dominio finito por parámetro, no rango universal

No se recomienda imponer un único intervalo global a todos los parámetros INT/DECIMAL. Cada clave de parámetro tendrá una declaración ex ante en el contrato abstracto:

- clave estable y ámbito;
- tipo y estado permitido;
- unidad/dimensión cuando proceda;
- conjunto finito o intervalo acotado con paso;
- obligatoriedad y default declarado;
- reglas de conversión admitidas;
- versión del contrato.

Para INT, el dominio será un conjunto finito explícito o un intervalo entero cerrado [min,max]. Para DECIMAL, se representará como entero escalado con escala fija por clave (ticks), límites cerrados y regla explícita de redondeo; se prohíbe precisión binaria flotante implícita. No habrá conversión DECIMAL→INT sin regla contractual específica.

ENUM tendrá un catálogo finito versionado por clave. BOOL es exactamente {false,true}. REF se resolverá dentro del universo cerrado de componentes declarados y su mapping, no por igualdad textual aislada.

STRING no será texto libre ilimitado: el contrato fijará longitud máxima, repertorio de caracteres y normalización. La normalización será identidad por defecto; cualquier normalización Unicode/case/espacios requerirá regla explícita, simétrica y versionada. Los identificadores de componente y las cadenas funcionales no compartirán necesariamente el mismo dominio.

## 3. Estados de valor

ABSENT, NULL, DEFAULT y VALUE son estados distintos. DEFAULT se desdobla en:
- DEFAULT_DECLARED: valor por defecto declarado en el paquete/contrato;
- DEFAULT_INHERITED: valor heredado por regla explícita del propio contrato;
- DEFAULT_ENV_RESOLVED: valor resuelto por el entorno.

DEFAULT_ENV_RESOLVED queda fuera del objeto migrado y se registra como condición del entorno/snapshot; no se transforma retrospectivamente en DEFAULT_DECLARED. Si el origen no permite distinguir los estados, la preservación se clasifica UNKNOWN, salvo evidencia independiente que resuelva la distinción.

La equivalencia entre ABSENT, NULL y DEFAULT nunca se presume. Debe declararse por clave, justificarse funcionalmente y someterse a sensibilidad.

## 4. Gramática y presupuesto de complejidad candidatos

Para el DGP confirmatorio mínimo se propone:

- AST declarativo acíclico; sin bucles, recursión, macros, funciones definidas por usuario, llamadas externas, I/O, reloj real ni efectos laterales.
- Operadores atómicos: EQ, NEQ, LT, LE, GT, GE, IN, NOT_IN, IS_ABSENT, IS_NULL, IS_DEFAULT, IS_VALUE, REFERS_TO y REF_EXISTS, sujetos a compatibilidad de tipos.
- Composición: NOT, AND y OR; precedencia NOT > AND > OR y paréntesis explícitos.
- Profundidad máxima candidata: 4 niveles de composición.
- Máximo candidato: 16 átomos por regla y 16 reglas por paquete.
- Efectos del núcleo: REQUIRE y FORBID como restricciones declarativas. SELECT_ENUM_VALUE se excluye del núcleo inicial porque introduce selección/mutación y puede confundir preservación con transformación; podrá evaluarse en extensión separada.
- Sin prioridad implícita entre reglas. Si dos reglas incompatibles se activan, el resultado es conflicto explícito, no resolución por orden de serialización.

Los límites 4/16/16 son un presupuesto inicial de complejidad para deliberación, no valores científicamente calibrados. Antes de congelarlos se deberá demostrar que permiten representar los casos semánticos necesarios y que no excluyen artificialmente la clase de configuraciones objetivo. Una prueba de sensibilidad podrá ampliar un límite cada vez, sin mezclar el cambio con el escenario confirmatorio.

## 5. Semántica de UNKNOWN y propagación a F*

La evaluación de regla devuelve TRUE, FALSE o UNKNOWN. UNKNOWN puede originarse por valor no observado, referencia sin resolver, mapping incompleto, tipo incompatible no adjudicado o cobertura insuficiente.

Reglas:
1. UNKNOWN nunca se convierte silenciosamente en FALSE ni TRUE.
2. Una violación obligatoria confirmada permite F*=0 aunque otra propiedad sea UNKNOWN.
3. Si no hay violación confirmada y alguna propiedad obligatoria queda UNKNOWN, F*=?.
4. F*=1 requiere que todas las propiedades obligatorias aplicables estén confirmadas.
5. UNKNOWN en una restricción REQUIRE/FORBID impide afirmar conformidad; no ejecuta ni aplica cambios.
6. Un conflicto entre reglas se clasifica como fallo contractual si está demostrado; si falta información para resolverlo, UNKNOWN.

Esta semántica es lógica de evaluación del contrato. No sustituye el estado epistémico 1/0/? del registro de evidencia ni determina por sí sola cobertura suficiente.

## 6. Conversiones y mapping

El mapping M será explícito, versionado y completo para todas las propiedades obligatorias:
- identidad de clave y componente;
- correspondencia de tipos;
- conversión de valores;
- correspondencia de estados ABSENT/NULL/DEFAULT/VALUE;
- referencias y extremos;
- reglas, ámbito, operador, operandos y efecto;
- diferencias representacionales permitidas.

Un mapping parcial no se considera conforme por defecto. Para una propiedad obligatoria sin mapping, el dictamen es UNKNOWN si no hay pérdida demostrada; es 0 si se demuestra una pérdida/alteración funcional. No se permite que el mapping redefina F*, el oráculo o la regla de Value.

## 7. Separación FP-01 / FP-02 / FP-03

- FP-01: validez del esquema, tipos, cardinalidades y restricciones estructurales.
- FP-02: integridad de referencias, extremos, unicidad y consistencia relacional.
- FP-03: preservación del significado de parámetros, estados, reglas y relaciones.

Una misma observación puede ser evidencia para más de una familia, pero el dictamen debe indicar el predicado primario para evitar doble conteo. La conformidad estructural no prueba preservación semántica; la preservación semántica no prueba compatibilidad del entorno ni seguridad FP-05.

## 8. Elementos aprobados y pendientes

**Aprobados por DEC-C10-054:** dominios finitos por clave; familias y restricciones de tipos; distinción de estados/defaults; AST acíclico y operadores declarativos; presupuesto 4/16/16; efectos REQUIRE/FORBID; exclusión de SELECT_ENUM_VALUE del núcleo; prohibición de conversión silenciosa de UNKNOWN.

**Pendientes:** límites, escalas y catálogos concretos por parámetro una vez definidas las claves; repertorios/longitudes STRING por clase de campo; reglas detalladas para conflictos; correspondencia SM-01…SM-10 y predicados FP-01/02/03; evidencia, cobertura, cegamiento y oráculo independiente.

## 9. Dictamen y límites

La propuesta convierte dominios potencialmente abiertos en contratos finitos por clave y limita la complejidad expresiva. No selecciona aún valores de configuración concretos, sistema software, formato, parser ni implementación.

**Estado:** DEC-C10-053 y DEC-C10-054 aprobadas; perfil estructural APROBADO; valores concretos por clave y mapping ABIERTOS; gramática documental delimitada, NO IMPLEMENTADA/VALIDADA; oráculo NO VALIDADO; revisión independiente NO REALIZADA; evidencia empírica NINGUNA; ejecución NO AUTORIZADA.

No se generan truth, fixtures, datos ni escenarios; no se ejecutan parser, validadores, pruebas, simulaciones o experimentos.
