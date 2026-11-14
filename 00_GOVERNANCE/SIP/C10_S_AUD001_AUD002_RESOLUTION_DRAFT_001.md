# C10-S — Resolución de AUD-001 y AUD-002: variable focal y DGP integrado
**Propuesta documental — borrador 001**

**Estado:** DRAFT / PROPUESTA PARA REVISIÓN — NO APROBADA  
**Vinculación:** PR #116; auditoría `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md`  
**Hallazgos abordados:** AUD-C10S-001 y AUD-C10S-002.  
**Naturaleza:** especificación conceptual y matemática preliminar; no es código, ejecución, preregistro ni evidencia científica.

**Aviso de precedencia vigente (2026-11-09):** este documento conserva una propuesta histórica NO ACEPTADA que intervenía focalmente sobre autorización. No es el contrato operativo del D2 primario candidato. DEC-C10-066/067 establecen D2 primario candidato/D1 secundario y políticas materiales D2 de provisión técnica focal, con `C_auth,base=1` común e invariante. La autorización basal y `AUTH_f*` permanecen vigentes; lo no primario es la intervención focal sobre autorización. Este documento solo puede reutilizarse como antecedente o escenario alternativo/adversarial, con estimando de política propio.

---

## 1. Decisión de diseño propuesta

Separar formalmente:

1. accesibilidad de una transformación focal (`A_f`);
2. representación del espacio completo accesible (`T_acc));
3. cambio estructurado de ese espacio (`ΔT_acc)).

La transformación focal del sistema sintético es `τ2 = Reconfigure`. El contraste experimental manipula la condición de autorización que habilita su realizabilidad, manteniendo invariantes los recursos, capacidad, información técnica, necesidad, motivación e incentivos, salvo que un escenario declare explícitamente otra vía.

Esta es una propuesta de diseño para C10-S. No afirma que la exclusividad de `τ2` esté demostrada en sistemas reales.

## 2. Definiciones formales

### 2.1. Accesibilidad focal

Sea `τ_f = τ2`. Para unidad `i), estado `s), contexto basal `x` e historia pertinente `h):

- `A_f^*(i,s,h)=1`: la transformación focal está respaldada como realizable y accesible.
- `A_f^*(i,s,h)=0`: está respaldado que no es realizable/accesible bajo las condiciones definidas.
- `A_f^*(i,s,h)` no se asigna a 0 por mera ausencia de evidencia.

El asterisco indica estado generador/verdadero del DGP, no una observación infalible disponible al analizador.

El analizador TGCV recibe `A_f^{obs}` o los datos/evidencias a partir de los que debe clasificarla, con estados:
- respaldada accesible;
- respaldada inaccesible;
- indeterminada.

La clasificación observada no debe confundirse con la verdad oculta del generador.

### 2.2. Espacio transformacional accesible

Representación de trabajo:

`T_acc(i,s,h) = (U_acc, R_acc, C_acc)`

donde:
- `U_acc`: identidades/versiones de transformaciones accesibles;
- `R_acc`: relaciones/dependencias activas y respaldadas;
- `C_acc`: condiciones, restricciones y configuraciones relevantes para su realizabilidad y composición.

El catálogo de referencia `U*` no equivale a `U_acc`. Una transformación puede pertenecer al catálogo y no ser accesible en una unidad/estado/historia concretos.

### 2.3. Cambio estructurado

Entre baseline `t=0` y postintervención `t=1`:

- `ΔU = (U_1 \ U_0, U_0 \ U_1)`
- `ΔR = (R_1 \ R_0, R_0 \ R_1)`
- `ΔC = (C_1 \ C_0, C_0 \ C_1)`

Por tanto:

`ΔT_acc = (ΔU, ΔR, ΔC)`

Las diferencias se calculan sobre identidades/versiones y definiciones canónicas comparables. Un cambio en la verdad o valor de una condición se registra como cambio de configuración/estado de condición; no se declara automáticamente una transformación nueva. Un cambio de relación tampoco se convierte automáticamente en una nueva identidad transformacional.

Para el experimento focal ideal:
- `τ2` permanece en el catálogo `U*` en ambos grupos;
- la autorización cambia de forma asignada;
- `τ2` cambia de inaccesible a accesible en la comparación focal;
- los demás componentes de `U_acc`, `R_acc` y `C_acc` solo cambian si el modelo de condiciones y dependencias implica ese cambio y este queda registrado.

La variación de `A_f^*` es así un contraste focal dentro de `ΔT_acc), no una definición exhaustiva de `ΔT_acc).

## 3. Intervención y estimandos

### 3.1. Asignación y accesibilidad

Propuesta de notación:

- `Z_A`: asignación aleatoria de política de autorización/acceso focal.
- `C_auth`: estado de autorización pertinente.
- `A_f^*`: accesibilidad verdadera de `τ2).
- `A_f^{obs}`: clasificación/medición de accesibilidad que recibe el analizador.

En el escenario ideal de manipulación perfecta:

`Z_A → C_auth → A_f^*`

y, bajo las restantes condiciones focales invariantes, `A_f^*=Z_A`. Esta igualdad es una propiedad de un escenario sintético ideal, no una suposición universal ni una equivalencia conceptual.

Si existen incumplimiento, errores o estados indeterminados, deben modelarse explícitamente; no reemplazar la accesibilidad verdadera por la asignación.

### 3.2. Estimando focal

Cuando el objeto causal es el acceso a `τ2`, el contraste de política debe nombrarse como efecto de accesibilidad focal:

`θ_{A_f}(q) = E[V^{q,g_1}] - E[V^{q,g_0}]`

- `q`: régimen común y explícito para condiciones/historias pertinentes.
- `g_1,g_0`: políticas implementables que modifican la probabilidad de acceso a `τ2), condicionadas a covariables basales e historia permitida.
- La población, horizonte, Value, soporte y régimen deben quedar definidos antes de analizar resultados.

Este estimando no equivale automáticamente al efecto de todo `ΔT_acc), ni a un efecto indirecto natural, ni a una fracción del TE.

El efecto de asignación `Z_A` (ITT) debe informarse separadamente. Si `Z_A` cambia expectativas, información, incentivos u otras condiciones además de `A_f`, el ITT no identifica por sí solo el efecto focal de accesibilidad.

### 3.3. Contraste de política y positividad

No utilizar `g_1,g_0` como etiquetas abstractas. Cada política debe:
- ser implementable en la unidad y contexto objetivo;
- especificar probabilidades y reglas condicionales;
- respetar las condiciones constitutivas;
- tener soporte suficiente bajo `q);
- registrar incumplimiento y desviaciones.

Si una política hace imposible una transformación por definición constitutiva, el contraste no identifica el efecto focal original en esa población. Se restringe el objetivo o se formula un efecto conjunto sobre condición y accesibilidad, etiquetándolo como tal.

## 4. DGP transformacional integrado

### 4.1. Unidad experimental común

Una misma unidad sintética `unit_id` atraviesa todos los módulos. No se generan datasets desconectados para el generador TGCV y el modelo causal.

Cada unidad conserva:
- contexto y estado basal;
- asignación y probabilidades;
- condiciones y evidencias;
- snapshots `T_acc,0` y `T_acc,1`;
- `A_f^*` y medición observada;
- Reach y trayectorias candidatas;
- selección y ejecución;
- mecanismos, Outcome y Value;
- verdad generadora y permisos de acceso por rol.

### 4.2. Cadena generativa propuesta

`X,S_0 → Z_A → C_auth → A_f^* → T_acc → (Reach, Π_H) → selección → ejecución → M → O → V`

La cadena es un contrato de producción de datos sintéticos. No implica que todos los efectos estén identificados solo por su orden.

### 4.3. Catálogo y ramas G0/G1

Se conserva el catálogo focal:

- `τ1 Diagnose`
- `τ2 Reconfigure` (transformación focal)
- `τ3 Verify` (solo después de una reconfiguración técnica)
- `τ4 Escalate` (transferencia de responsabilidad, no reconfiguración técnica)

Relaciones activas:
- `r12`: Diagnose habilita Reconfigure, sujeto a sus condiciones.
- `r23`: Reconfigure habilita Verify.
- `r14`: Diagnose habilita Escalate.
- `r43`: inactiva/excluida; Escalate no habilita Verify en el catálogo actual.

Contraste:
- G0: `τ1 → τ4`; la rama termina en incidencia transferida.
- G1: `τ1 → τ2 → τ3`; la rama termina en configuración reconfigurada y verificada.
- `H=3) aplicaciones efectivas.
- No atribuir a G0 una verificación técnica ni introducir una transformación sustitutiva implícita.

La exclusividad de `τ2` para la función focal sigue siendo una hipótesis del universo sintético cerrado que debe pasar pruebas EX. Si se descubre una ruta alternativa compatible, se incorpora al catálogo y se revisa el contraste; no se oculta para preservar el efecto esperado.

### 4.4. Condición manipulada y condiciones invariantes

El DGP ideal modifica `C_auth` y mantiene constantes:
- recursos disponibles;
- capacidad técnica;
- información diagnóstica;
- necesidad/estado inicial;
- tiempo y horizonte;
- incentivos y expectativas;
- reglas de medición;
- criterios de Outcome y Value.

Cualquier variación adicional se registra como vía alternativa o condición posterior `L`; no se absorbe en `A_f).

## 5. Integración con selección, ejecución, Outcome y Value

### 5.1. Candidatas no son ejecuciones

El generador TGCV produce `Π_H` y Reach sin recibir `O) ni `V). Un módulo separado:
1. recibe las trayectorias candidatas y la regla de selección;
2. selecciona una trayectoria bajo el régimen experimental especificado;
3. ejecuta o simula su ejecución;
4. registra paso por paso qué transformaciones fueron efectivamente ejecutadas.

La selección y ejecución no modifican retroactivamente el inventario de candidatas.

### 5.2. Dos regímenes que no deben mezclarse

**Régimen E1 — ejecución estandarizada:** fuerza una política de selección/ejecución previamente definida para aislar la validez de la manipulación y la cadena de mecanismos. No representa necesariamente elección libre del sistema.

**Régimen E2 — selección libre o política de selección:** permite que una regla de decisión seleccione entre candidatas. La regla, información, preferencias e incentivos deben ser iguales entre brazos o medirse como vías potencialmente afectadas por la intervención.

Los resultados E1 y E2 responden preguntas diferentes y no se combinan como si fueran el mismo estimando.

### 5.3. Outcome

`O` se genera a partir de eventos de ejecución y mecanismos definidos para cada transformación/ruta. Deben especificarse:
- evento de ejecución de `τ2` y `τ3`;
- resultado técnico y temporal;
- fallos, no cumplimiento y ejecución parcial;
- efectos de `τ4` propios de transferencia, sin atribuirle reconfiguración técnica.

No se permite generar `O) directamente desde `Z_A) en el escenario focal puro, salvo que el escenario declare una vía alternativa.

### 5.4. Value

`V) se calcula mediante regla independiente preespecificada sobre Outcome y dimensiones admisibles (beneficiario, calidad, tiempo, coste, horizonte y trade-offs). No recibe `T_acc), cardinalidad ni longitud de trayectoria como bonificación automática.

`V_{real}) se deriva de resultados realizados. `V_{potential}), si se conserva, es un análisis complementario distinto y no sustituye evidencia empírica de valor realizado.

## 6. Escenarios integrados mínimos propuestos

Los escenarios S0–S10 de identificación causal permanecen como pruebas unitarias. Se añaden escenarios integrados de extremo a extremo:

| ID | Manipulación/verdad | Resultado esperado |
|---|---|---|
| INT-01 | `Z_A` cambia solo autorización; `A_f^*) cambia; `τ2` habilita ruta G1 | Reconstruir cambio focal, Reach/trayectorias, ejecución, O y V sin filtración |
| INT-02 | Accesibilidad de `τ2` cambia, pero política de ejecución no selecciona `τ2` | Detectar ΔT_acc y candidatas; no inferir ejecución ni cambio de V |
| INT-03 | `τ2` accesible pero condición de aplicabilidad no satisfecha en S0 | A_f puede ser accesible; ruta no aplicable/alcanzable en el estado/horizonte; no confundir niveles |
| INT-04 | La autorización afecta también expectativa/información | Identificar vía alternativa; no atribuir ITT exclusivamente a A_f |
| INT-05 | Existe ruta externa sustitutiva para función focal | Fallar exclusividad de τ2 y revisar el contraste transformacional |
| INT-06 | Error de clasificación en A_f observado | Recuperar incertidumbre/medición; no equiparar A_f observado con verdad |
| INT-07 | Mismo T_acc, distinta regla de selección | Separar generación de candidatas de selección/ejecución y explicar diferencias de O |
| INT-08 | Mismo Outcome, regla Value independiente y misma | V no cambia por cardinalidad/longitud de T_acc |

Para cada INT se requiere ficha de prueba completa antes de implementación: fixture/versiones, entradas por rol, verdad oculta, salida esperada, aserciones, tolerancias, códigos de fallo y artefactos.

## 7. Matriz de acceso y no filtración

| Dato | Generador | Analizador TGCV | Analizador causal | Evaluador |
|---|---:|---:|---:|---:|
| Parámetros verdaderos DGP | Sí | No | No | Sí |
| `A_f^*` | Sí | No, salvo validación diseñada | No, salvo validación diseñada | Sí |
| Evidencias observables de accesibilidad | Sí | Sí | Según estimando/diseño | Sí |
| `A_f^{obs}` | Produce | Sí | Sí | Sí |
| `T_acc` observable/codificado | Produce | Reconstruye/audita | Resumen predefinido si necesario | Sí |
| `Π_H), Reach | Produce verdad de referencia | Reconstruye | Solo variables necesarias | Sí |
| Selección/ejecución | Produce DGP | No se usa para reconstruir candidatas | Según análisis | Sí |
| `O,V) | Produce | Ciego durante evaluación de T_acc | Sí, cuando proceda | Sí |
| Etiqueta de escenario/verdad | Sí | No | No | Sí |

La tabla es provisional: antes de congelar el protocolo se debe decidir qué datos recibe el analizador causal para cada estimando y evitar ajustar por variables postratamiento inapropiadas.

## 8. Criterios de aceptación de la resolución P0

AUD-001 y AUD-002 solo podrán cerrarse cuando:

1. `A_f^*`, `A_f^{obs}), `T_acc) y `ΔT_acc) estén definidos sin ambigüedad en todo el documento y diccionario.
2. Cada escenario especifique si interviene `Z_A), `A_f), una condición o un régimen secuencial.
3. La misma unidad sintética atraviese todos los módulos.
4. El generador de candidatas no use Outcome, Value, selección ni ejecución.
5. La selección/ejecución esté separada y produzca eventos observables.
6. Outcome derive de mecanismos/eventos definidos y Value de regla independiente.
7. Existan INT-01 a INT-08 con contratos de prueba normalizados.
8. S5-C, S5-F, S4-O y S4-R sigan diferenciados y sus estimandos no se mezclen.
9. La exclusividad de τ2 se mantenga como resultado de auditoría, no como premisa.
10. Una revisión cruzada confirme que la notación y las ecuaciones son consistentes en documento, diccionario y protocolos.

## 9. Cuestiones abiertas que no se resuelven por estipulación

- ¿La intervención realista que habilita `τ2` puede cambiar solo autorización, sin cambiar expectativas, información, incentivos o trato?
- ¿Qué evento observable prueba que `τ2` fue ejecutada y que la configuración cambió técnicamente?
- ¿Qué regla de selección corresponde a E1 y cuál a E2?
- ¿Qué mecanismo transforma ejecución en Outcome y con qué incertidumbre?
- ¿Qué regla Value y horizonte resultan adecuados para el piloto real?
- ¿Qué alternativas funcionales externas deben incluirse para evaluar exclusividad?
- ¿Qué población/régimen permite positividad para `g_0,g_1`?

No resolver estas preguntas por conveniencia matemática. Si el piloto real no permite aislar el efecto de accesibilidad, se debe reportar el efecto conjunto identificable o la limitación de identificación.

## 10. Estado

- AUD-C10S-001: **propuesta de resolución elaborada; pendiente de revisión y armonización con el documento consolidado**.
- AUD-C10S-002: **propuesta de arquitectura integrada elaborada; pendiente de contratos de prueba y revisión**.
- No se ha implementado código.
- No se ha ejecutado simulación.
- No se ha realizado validación estadística ni auditoría independiente.
- No se ha seleccionado ni intervenido un caso real.
- No se modifica ninguna afirmación científica ni estado de TGCV.

**Siguiente operación documental:** armonizar esta propuesta con el documento consolidado C10-S y convertir INT-01 a INT-08 en fichas de prueba completas, una vez revisadas las decisiones conceptuales anteriores.


---
## 11. Supersesión de la siguiente operación histórica para D2 (2026-11-09)

La «siguiente operación documental» descrita al final de §10 —armonizar esta propuesta como contrato operativo y convertir INT-01…08 en fichas— queda **supersedida para el D2 primario candidato** por DEC-C10-066/067 y por el aviso de precedencia de §0. Este documento no debe armonizarse como intervención primaria D2 ni alimentar código o fixtures de D2.

INT-01…08 y la arquitectura de intervención sobre autorización solo podrán reutilizarse si se decide desarrollar un escenario alternativo/adversarial explícito, con estimando de política propio y revisión de sus vías causales. Esta nota no cierra AUD-001/002 ni convierte la propuesta en decisión aceptada.

