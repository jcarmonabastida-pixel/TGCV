# C10-S — Gramática mínima de reglas y dominio de tipos/parámetros: propuesta

**ID:** C10-S-RULE-TYPE-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta documental derivada de DEC-C10-053; NO aprobada, NO congelada, NO implementada, NO validada.

## 1. Restricciones de diseño

La gramática debe ser declarativa, finita, determinista, interpretable sin ejecutar código arbitrario, suficientemente expresiva para producir cambios semánticos falsables e independiente de parser/serialización concretos. No debe convertirse en un lenguaje de programación general. La notación es metalenguaje de especificación, no sintaxis implementada.

## 2. Dominio abstracto de tipos

| Tipo | Dominio candidato | Restricciones |
|---|---|---|
| BOOL | {true,false} | Sin coerción implícita |
| INT | Enteros en dominio finito declarado | Límites por contrato |
| DECIMAL | Racional/decimal con escala declarada | Precisión, redondeo y tolerancia ex ante |
| ENUM | Conjunto finito de símbolos | Correspondencia explícita |
| STRING | Cadenas de longitud/dominio acotado | Normalización solo si está definida |
| REF | Identificador de componente/recurso declarado | Resolución contra universo cerrado |

No se proponen inicialmente ARRAY, MAP arbitrario, BINARY, fecha/hora ni tipos definidos por usuario como tipos primitivos del núcleo. Las colecciones podrán modelarse en las relaciones del paquete. Su inclusión requiere justificación.

Cada parámetro tendrá como mínimo: key, type, required, value_state y, cuando value_state=VALUE, value. value_state distingue ABSENT, NULL, DEFAULT y VALUE; no se colapsan salvo equivalencia semántica declarada. DEFAULT deberá distinguir valor explícito, heredado o resuelto por el entorno; este último estado no se incorpora al objeto migrado.

## 3. Gramática declarativa candidata

### 3.1 Expresiones atómicas

- EQ, NEQ.
- LT, LE, GT, GE, solo para INT/DECIMAL o tipos ordenables declarados.
- IN, NOT_IN, sobre ENUM o conjunto finito declarado.
- IS_ABSENT, IS_NULL, IS_DEFAULT, IS_VALUE.
- REFERS_TO, REF_EXISTS, sobre REF y universo cerrado.

No se permite comparación entre tipos incompatibles ni coerción implícita. La igualdad de STRING/ENUM/REF depende de reglas de identidad contractual explícitas.

### 3.2 Composición lógica

Se propone AND, OR, NOT, precedencia fija NOT > AND > OR y paréntesis explícitos. La profundidad máxima y el número máximo de átomos deberán fijarse en el contrato del DGP antes de observar resultados.

### 3.3 Restricciones de efecto

Una regla contiene identificador estable, ámbito (componente/parámetro/referencia), condición declarativa y efecto de clase finita (por ejemplo REQUIRE, FORBID, SELECT_ENUM_VALUE). Prioridad solo cuando el contrato declare precedencia semántica.

Se excluyen bucles, recursión, llamadas externas, funciones definidas por usuario, I/O, mutación arbitraria, scripts y evaluación dependiente del reloj real.

## 4. Semántica trivalente

La evaluación de una expresión puede ser TRUE, FALSE o UNKNOWN cuando falten valores, la referencia no esté resuelta o la evidencia sea insuficiente. UNKNOWN no equivale a FALSE. Propagación candidata:
- NOT UNKNOWN = UNKNOWN.
- AND: FALSE si algún operando es FALSE; TRUE si todos son TRUE; UNKNOWN en otro caso.
- OR: TRUE si algún operando es TRUE; FALSE si todos son FALSE; UNKNOWN en otro caso.

El contrato deberá especificar si UNKNOWN bloquea, deja indeterminado o activa tratamiento explícito. No se convierte silenciosamente en TRUE/FALSE. Esta semántica no sustituye la adjudicación trivalente de evidencia 1/0/?; el oráculo deberá conectarlas explícitamente.

## 5. Reglas de parámetros y conversiones

- BOOL no se convierte desde STRING/INT sin mapping explícito.
- INT→DECIMAL puede ser exacto; DECIMAL→INT requiere regla de redondeo y tolerancia explícitas.
- ENUM requiere tabla de correspondencia completa para valores obligatorios.
- STRING no se normaliza (mayúsculas, espacios, Unicode) salvo regla declarada y comprobable.
- REF requiere mapping de extremos; no basta conservar el identificador textual.
- ABSENT/NULL/DEFAULT/VALUE se preservan como estados distintos cuando el contrato fuente los distingue.
- Un default resuelto por el entorno no se confunde con el default declarado en el paquete.

## 6. Candidatos a falsación

La gramática debe permitir detectar: operador cambiado; operandos permutados cuando no sean conmutativos; ámbito alterado; precedencia distinta; conversión con pérdida; enum no mapeado; referencia a entidad no correspondiente; colapso de ABSENT/NULL/DEFAULT; UNKNOWN convertido en resultado concluyente.

No se crean fixtures ni se asigna frecuencia/truth a estos casos.

## 7. Parámetros aún no fijados

1. Dominio finito concreto de INT/DECIMAL/STRING/ENUM.
2. Límites de longitud, escala, precisión y redondeo.
3. Profundidad y tamaño máximo de expresión.
4. Universo de componentes y referencias.
5. Tipos de efecto permitidos y semántica exacta.
6. Política de UNKNOWN por clase de regla.
7. Necesidad de precedencia entre reglas.
8. Tipos y operadores del DGP confirmatorio frente a sensibilidad.
9. Validación independiente del evaluador/oráculo.
10. Vínculo con FP-01/FP-02/FP-03 sin doble conteo.

## 8. Dictamen

La propuesta ofrece un núcleo pequeño, finito y sin ejecución arbitraria. Todavía no constituye una gramática cerrada ni un dominio operacional: los límites concretos, la semántica de UNKNOWN y el contrato de conversión siguen abiertos.

**Estado:** BASE PARTITION APPROVED (DEC-C10-053); TYPE SET PROPOSED; RULE GRAMMAR PROPOSED; FINITE DOMAIN PARAMETERS OPEN; UNKNOWN POLICY OPEN; ORACLE NOT VALIDATED; NO TECHNICAL VALIDATION; NO INDEPENDENT REVIEW; NO EMPIRICAL EVIDENCE; NO EXECUTION AUTHORIZATION.


## 9. Reconciliación decisional posterior — DEC-C10-054

La propuesta de gramática se interpreta ahora junto con el perfil estructural aprobado por DEC-C10-054: AST acíclico declarativo; profundidad máxima 4; 16 átomos por regla; 16 reglas por paquete; efectos del núcleo REQUIRE/FORBID; SELECT_ENUM_VALUE fuera del núcleo; dominios finitos por clave; UNKNOWN no se convierte silenciosamente en TRUE/FALSE. Los dominios numéricos/catálogos concretos por clave, reglas de conflicto, mapping y oráculo permanecen abiertos. La aprobación del perfil no equivale a implementación o validación de esta gramática.


## 10. Aplicación candidata del dominio de tipos al roster PAR

Para mantener el DGP base parsimonioso, el roster de trabajo propone instanciar BOOL (activación lógica), ENUM (perfil funcional finito) e INT (contador opcional acotado). Esto no reduce el conjunto abstracto admitido por el contrato: DECIMAL, STRING y REF siguen disponibles bajo condiciones justificadas, pero no es necesario instanciarlos todos en el caso base.

Los dominios son simbólicos: BOOL={false,true}; ENUM=D_profile finito con al menos dos símbolos sin orden implícito; INT=D_retry={n∈Z:0≤n≤N_retry_max}, con máximo finito pendiente. No se asignan valores ni límites numéricos. DECIMAL requiere escala/precisión/unidad/redondeo por clave; STRING requiere longitud/dominio y normalización explícita; REF requiere universo cerrado y mapping de extremos.

Las reglas REQUIRE/FORBID del núcleo deben usar únicamente claves y dominios declarados. Una regla candidata podría restringir los perfiles permitidos cuando el servicio esté habilitado, pero su semántica y dominio deben cerrarse en el contrato RUL; no se crea una regla confirmatoria por esta nota. Se mantienen AST 4/16/16, acíclico, y UNKNOWN no convertido silenciosamente.

## 11. Contrato mínimo de RUL para la unidad lógica de servicio

**Estado:** instancia RUL-SVC-ENABLE-PROFILE-01 aceptada conceptualmente por DEC-C10-068; semántica ejecutable, parser, mapping y oráculo no validados.

DEC-C10-056 exige RUL≥1 y DEC-C10-054 limita el núcleo a AST declarativo acíclico 4/16/16, operadores atómicos declarados, composición AND/OR/NOT y efectos REQUIRE/FORBID. Se excluye SELECT_ENUM_VALUE del núcleo. La evaluación conserva TRUE/FALSE/UNKNOWN; UNKNOWN no se fuerza a un resultado binario.

La instancia aceptada es una restricción constitutiva P0, comprobable y no tautológica, referida a PAR-SVC-ENABLED y PAR-SVC-PROFILE. Su fuente funcional es el contrato del mundo sintético estipulado ex ante, no una norma externa. La aceptación no amplía el conjunto de operadores ni demuestra que el parser/oráculo la ejecute correctamente. La expresión concreta y sus contrastes están en §12 y en el contrato funcional de referencia.
## 12. Instancia sintética aceptada para comprobar expresividad RUL

DEC-C10-068 acepta BOOL ENABLED y ENUM PROFILE={STANDARD,READ_ONLY,DISABLED}; RUL-SVC-ENABLE-PROFILE-01 se expresa como OR(NEQ(ENABLED,true),IN(PROFILE,{STANDARD,READ_ONLY})) bajo REQUIRE. Esta instancia tiene un estado violador conocido (ENABLED=true/PROFILE=DISABLED) y dos estados permitidos cuando ENABLED=true. ENABLED=false no queda restringido por esta implicación.

La aceptación demuestra una especificación lógica no tautológica dentro del mundo sintético estipulado; no valida parser, semántica ejecutable, mapping ni dominio de servicios reales. Un valor ausente/conflictivo produce UNKNOWN conforme a la regla trivalente. Se mantiene el presupuesto AST 4/16/16 y no se introducen operadores o tipos nuevos.