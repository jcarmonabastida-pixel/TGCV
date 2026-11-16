# C10-S — Gate 148: aceptación R148-A y alcance funcional efectivo de V_cont

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** R148-A_ACCEPTED / EFFECTIVE_SERVICE_FUNCTION_SCOPE_ACCEPTED / DEC_C10_102_SCOPE_RECONCILIATION_REQUIRED / NO_DEC_AMENDMENT / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Acto de aceptación

Se registra la aceptación expresa del usuario de R148-A y de la orientación de que `V_cont` debe adjudicar la continuidad de la **función efectiva del servicio B1**, incluyendo las interrupciones runtime que impidan realmente la admisión, y no limitarse a comprobar la validez declarativa de RUL-SVC-ENABLE-PROFILE-01.

La aceptación es semántica y lógica para el DGP sintético. No crea una DEC-C10, no modifica DEC-C10-068 ni DEC-C10-099…104, no altera el DGP original ni promueve contenido a `main`.

## 2. Reglas R148-A aceptadas

1. **Predicados distintos:** `D_valid`, `D_enabled`, `O` y `A` son predicados diferentes y no se sustituyen entre sí.
2. **Validez declarativa:** `D_valid` se evalúa exclusivamente mediante RUL-SVC-ENABLE-PROFILE-01 y conserva su implicación unidireccional `ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}`. No se añade la implicación inversa ni semántica diferenciada a STANDARD/READ_ONLY.
3. **Deshabilitación:** `D_enabled=false` significa que la función declarada es no admitir, aunque el runtime esté disponible.
4. **Habilitación insuficiente:** `D_enabled=true` no demuestra por sí solo disponibilidad ni capacidad de admisión. `O` y la capacidad efectiva pertinente deben permitir la admisión. Estas son condiciones necesarias dentro del contrato, no una conjunción declarada universalmente suficiente.
5. **Truth y observación:** `O` y `A` no se infieren de una petición individual ni de S3 sin verdad generada. S3 sigue siendo evidencia imperfecta, no definición de truth.
6. **Mecanismos runtime:** los mecanismos runtime y recursos pueden afectar `O` y/o `A`; se conserva la provenance de sus antecedentes sin duplicar transiciones truth. Solo cuenta el cambio funcional efectivo.
7. **Alcance de V_cont:** la verdad de `A_B1(i,k)` y, por agregación, `V_cont`, debe representar la continuidad de la función efectiva B1: capacidad de admitir solicitudes conforme a la configuración declarativa y a las condiciones operativas/recursos que realmente hagan posible esa admisión. No se reduce a la validez de la configuración ni al valor aislado de ENABLED/PROFILE.

## 3. Reconciliación con decisiones vigentes: límite de la aceptación

DEC-C10-068 sigue siendo la fuente constitutiva de la regla declarativa y de los parámetros ENABLED/PROFILE. DEC-C10-099 selecciona V_cont como dimensión provisional; DEC-C10-100 define agregación temporal tri-valuada; DEC-C10-101 fija el origen t0; DEC-C10-102 acepta continuidad estricta por intervalo y formula su truth en términos de cumplimiento ENABLED/PROFILE; DEC-C10-104 conserva esa regla, sus fronteras y el límite conservador de UNKNOWN.

La orientación ahora aceptada amplía la interpretación funcional que debe representar A_B1/V_cont para incluir la disponibilidad efectiva. **No se modifica ni se reescribe DEC-C10-102 por inferencia.** Persiste una cuestión formal de precedencia/alcance: cómo articular la referencia de DEC-C10-102 a ENABLED/PROFILE con la función efectiva ampliada, manteniendo intactos:
- continuidad estricta: cualquier fallo funcional confirmado que afecte la función B1 hace que el intervalo afectado sea 0;
- truth `{1,0,?}` y bounds de DEC-C10-100;
- inicio de ventana t0 y fronteras de DEC-C10-101/104;
- separación truth / observed_evidence / evaluation;
- prohibición de convertir missingness S3 o defectos del harness en UNKNOWN funcional.

Por tanto, la **dirección semántica está aceptada**, pero la reconciliación normativa exacta de DEC-C10-102 permanece pendiente. Antes de materializar A_B1/V_cont se deberá decidir documentalmente si basta una interpretación compatible y explícita o si se necesita una decisión complementaria/sucesora. Ninguna opción se presume en este Gate.

## 4. Lectura funcional resultante

- Configuración declarativa válida no demuestra que el servicio esté operativo.
- ENABLED=true no demuestra que el servicio pueda admitir solicitudes.
- Runtime disponible no autoriza a admitir cuando ENABLED=false.
- La caída de proceso/módulo, listener/superficie de ingreso, dependencia constitutiva o capacidad/recurso solo afecta A_B1 cuando realmente impide la función de admisión según el contrato sintético.
- Un evento técnico, una señal S3 o un intento/rechazo individual no constituye automáticamente una transición truth de disponibilidad general.
- La ausencia de solicitudes no es fallo.
- Procesamiento, respuesta, ejecución transformacional, Outcome y Value global siguen siendo objetos distintos de A_B1/V_cont.

No se afirma que las condiciones necesarias enumeradas sean universalmente suficientes; protocolo, carga, umbrales, tolerancias, granularidad y parámetros temporales permanecen abiertos.

## 5. Estado y límites

| Elemento | Estado |
|---|---|
| R148-A, reglas 1–6 | ACCEPTED — lógico |
| V_cont como continuidad de función efectiva B1 | ACCEPTED — dirección semántica |
| Inclusión de interrupciones runtime con efecto real en admisión | ACCEPTED — dirección semántica |
| Relación formal D_valid/D_enabled/O/A | Delimitada parcialmente |
| Articulación normativa con DEC-C10-102 | OPEN — requiere crosswalk |
| DEC-C10-068/099…104 | Vigentes, no modificadas |
| §51, reloj, rejilla, T*, Δ, K y calibración S3 | OPEN |
| Schema, implementación, pruebas, generación, simulación, estimación y ejecución | No autorizadas |

## 6. Siguiente operación — Gate 149

Realizar un crosswalk documental de DEC-C10-102 y DEC-C10-104 frente a R148-A, DEC-C10-068, DEC-C10-099/100 y Gates 127, 134 y 147-B. Determinar si:
1. la función efectiva B1 puede quedar incluida mediante interpretación compatible de “cumplimiento funcional” sin contradecir el texto aceptado;
2. la formulación de DEC-C10-102 debe aclararse mediante decisión complementaria o sucesora, sin reescribir el registro histórico;
3. cómo se representa la transición de disponibilidad runtime y la continuidad estricta por intervalo sin duplicar ENABLED/PROFILE ni convertir evidencia en truth.

Gate 149 será documental y lógico. No cambiará DEC, schema, código, tests, fixtures, DGP numérico, reloj, §51 ni autorización.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
