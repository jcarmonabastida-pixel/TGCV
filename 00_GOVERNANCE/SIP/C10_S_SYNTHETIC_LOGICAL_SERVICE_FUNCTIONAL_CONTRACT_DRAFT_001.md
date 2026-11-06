# C10-S — Contrato funcional del servicio lógico sintético de referencia

**ID:** C10-S-SYNTHETIC-SERVICE-CONTRACT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-06  
**Estado:** ACEPTADO CONCEPTUALMENTE POR DEC-C10-068; contrato funcional de referencia para C10-S. No es aún Design Freeze, mapping físico implementado, inventario real, implementación ni ejecución.

## 1. Propósito y relación con decisiones vigentes

Este documento especializa, sin sustituirlas, las decisiones ya registradas: DEC-C10-051 (microdominio de migración de configuración entre dos entornos software), DEC-C10-052 (clase A: paquete de configuración de servicio software), DEC-C10-057/058 (perímetros P0/P1/P2 y unidad lógica de servicio) y DEC-C10-056 (CMP≥1, PAR≥1, RUL≥1; MET obligatorio).

No se elige producto, proveedor, lenguaje, formato, plataforma ni servicio real. Se define un **servicio lógico sintético de referencia** para que el DGP tenga semántica funcional conocida y falsable. Es una especificación estipulada del mundo sintético, no una afirmación empírica sobre servicios reales ni una generalización a toda configuración software.

## 2. Unidad lógica y función de referencia

Unidad: una instancia lógica versionada de un servicio software de procesamiento de solicitudes. Su función abstracta es aceptar solicitudes cuando está habilitado y exponer un perfil operativo declarado. La identidad funcional no depende de host, proceso, contenedor ni ubicación.

El objeto migrado P0 es el paquete declarativo de configuración de esa unidad. P1 contiene runtime, binarios, infraestructura, permisos efectivos, recursos y estado del entorno. P2 conserva rutas, provisión B, dependencias, alternativas, agentes, observación, ejecución y posibles vías colaterales. Se mantiene la clasificación de DEC-C10-058.

## 3. Parámetros lógicos del núcleo

Se proponen dos parámetros obligatorios para esta instancia sintética:

| Clave lógica | Tipo | Dominio finito | Semántica |
|---|---|---|---|
| PAR-SVC-ENABLED | BOOL | {false,true} | Declara si el servicio debe aceptar solicitudes |
| PAR-SVC-PROFILE | ENUM | {STANDARD, READ_ONLY, DISABLED} | Declara el modo funcional deseado |

Los símbolos ENUM son identificadores semánticos abstractos del DGP, no valores de un producto. STANDARD y READ_ONLY son perfiles operativos habilitados; DISABLED es el perfil que declara inactividad. No se infiere que estos perfiles existan en una plataforma real.

PAR-SVC-RETRY-COUNT queda fuera del núcleo mínimo hasta que se justifique su pertenencia al contrato funcional de esta unidad. No se traslada a P0 una variable de capacidad, cuota o consumo de recursos P1.

## 4. Regla constitutiva candidata

**ID lógico:** RUL-SVC-ENABLE-PROFILE-01  
**Owner:** CMP-SERVICE-LOGIC (identidad lógica provisional; debe asignarse al CMP concreto de la instancia).  
**Scope:** configuración declarativa completa de la unidad lógica de servicio.  
**Efecto:** REQUIRE.  
**Condición:** si PAR-SVC-ENABLED=true, PAR-SVC-PROFILE debe pertenecer a {STANDARD, READ_ONLY}.

Metalenguaje compatible con el núcleo aprobado:

`OR(NEQ(PAR-SVC-ENABLED,true), IN(PAR-SVC-PROFILE,{STANDARD,READ_ONLY}))`

La regla tiene contraste no tautológico dentro del dominio declarado:
- ENABLED=true, PROFILE=STANDARD → satisface.
- ENABLED=true, PROFILE=READ_ONLY → satisface.
- ENABLED=true, PROFILE=DISABLED → viola.
- ENABLED=false, cualquier PROFILE declarado → no queda restringido por esta regla.

La última condición es deliberada: esta RUL impone una implicación, no una equivalencia. No se infiere que ENABLED=false obligue a PROFILE=DISABLED. Si se desea esa segunda dirección, requerirá justificación y regla separada, no se añadirá por simetría.

La regla no codifica Outcome, Value, permisos efectivos, disponibilidad de recursos, ejecución ni éxito de la migración. Su fuente funcional es este contrato sintético, fijado ex ante para el DGP. Por tanto, su validez es interna al mundo sintético definido aquí; no se presenta como norma de ingeniería externa.

## 5. Semántica de evaluación

La evaluación usa TRUE/FALSE/UNKNOWN. Si falta un valor, hay NULL/ABSENT no admisible, conflicto de identidad/versión o cobertura insuficiente, la regla no se fuerza a TRUE/FALSE: resultado UNKNOWN salvo que evidencia suficiente confirme una violación independiente.

Una evaluación FALSE acredita incumplimiento de la regla en el objeto/versión evaluados; no implica por sí sola F*=0 si la agregación contractual y la suficiencia de evidencia no están cerradas. UNKNOWN permanece indeterminado. No se imputan estados ni se confunde verdad DGP con observación del analizador.

## 6. Conservación y aplicación en rutas

F1/A1 deben preservar la identidad semántica de la regla, sus operandos, dominio ENUM, scope, versión y efecto en el mapping intermedio. F2/A2 deben aplicar el paquete/regla en destino bajo el mismo contrato funcional. El mapping puede cambiar etiquetas físicas, pero debe preservar los símbolos semánticos y la condición; su equivalencia requiere tabla de correspondencia explícita y evidencia del estado aplicado.

La adjudicación distingue:
- FP-03: preservación semántica de condición, operandos, scope y efecto;
- FP-06: aplicación efectiva del paquete/regla en destino;
- FP-07: verificación post-aplicación;
- FP-08: trazabilidad y procedencia probatoria.

La igualdad textual del AST no basta si el mapping altera el significado. La preservación del AST tampoco prueba que la regla se haya aplicado.

## 7. Casos adversariales mínimos para el DGP

El generador deberá incluir, al menos conceptualmente, estos contrastes conocidos:
1. regla y parámetros preservados: condición satisfecha;
2. ENABLED=true con PROFILE=DISABLED: violación;
3. inversión de NEQ/IN o ampliación indebida del conjunto permitido: mutación semántica;
4. cambio de scope o de owner: pérdida de aplicabilidad;
5. REQUIRE cambiado a FORBID: inversión del efecto;
6. regla preservada en representación intermedia pero no aplicada en destino;
7. valor ausente/conflictivo o evidencia incompleta: UNKNOWN;
8. cambio de etiqueta física con mapping semántico correcto: equivalencia preservada;
9. igualdad de etiquetas físicas con mapping semántico incorrecto: no equivalencia.

Los casos no son fixtures serializados ni pruebas ejecutadas. Los resultados futuros deberán separar hidden_truth del input accesible al analizador y del oráculo evaluador.

## 8. Límites y gates pendientes

La especialización funcional y RUL descritas quedan aceptadas conceptualmente por DEC-C10-068 como contrato de referencia del DGP sintético. No cierra:
- identidad CMP concreta, versión de instancia, procedencia detallada y serialización final;
- identidad CMP definitiva, versión, procedencia y serialización;
- tabla concreta de mapping fuente/destino;
- obligatoriedad/aplicabilidad IAM de cada predicado;
- contrato completo de F*, oráculo y errores de medición;
- unidad de asignación/interferencia y estimandos;
- fixtures, implementación, validadores, simulación o ejecución.

**Estado final:** contrato funcional sintético aceptado por DEC-C10-068; DEC-C10-056 sigue siendo la fuente de cardinalidad. La aceptación no congela el diseño completo ni autoriza implementación o ejecución.

## 9. Registro de aceptación

DEC-C10-068 acepta el servicio lógico sintético, los parámetros PAR-SVC-ENABLED/PAR-SVC-PROFILE y RUL-SVC-ENABLE-PROFILE-01 con la semántica y contrastes de §§2–4. CMP-SERVICE-LOGIC permanece como owner lógico provisional; identidad/versionado concretos, IAM de instancia, mapping físico, tolerancias y oráculo siguen abiertos. PAR-SVC-RETRY-COUNT continúa excluido del núcleo. No hay fixtures ni ejecución.
