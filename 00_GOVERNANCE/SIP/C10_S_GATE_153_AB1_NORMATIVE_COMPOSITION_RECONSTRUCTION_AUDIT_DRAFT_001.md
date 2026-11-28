# C10-S — Gate 153: reconstrucción normativa de la composición A_B1 y alcance de DEC-C10-102

**Fecha:** 2026-11-16  
**Rama de trabajo:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** HISTORICAL_RECONSTRUCTION_PARTIAL / DEC-C10-099_CONSTRUCT_COMPATIBLE / DEC-C10-102_OPERATOR_PRESERVED / R150_R151A8_COMPOSITION_TENSION_IDENTIFIED / COMPLEMENTARY_DECISION_NOT_READY / NO_DEC / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Objeto y límites

Determinar si la composición de A_B1 aceptada en Gates 150–152 puede leerse de forma compatible con DEC-C10-068/099/100/101/102/104 y el contrato DGP §§49–50, o si requiere una decisión complementaria.

Operación exclusivamente documental. No modifica DEC existentes, DGP, §51, reloj, soporte temporal, rejilla, T*, Δ, K, S3, schema, código, harness ni autorizaciones. No declara cierre de EventHistory ni de A_B1.

## 2. Fuentes reconstruidas

Se recuperaron de GitHub:
- `00_GOVERNANCE/README.md`, `CHATGPT_BOOTSTRAP.md`, `CANONICAL_STATE.json`, `STATUS.md`, RMA v3.38 y Evidence→Claim Matrix v1.47 desde `main`;
- Gates 145, 149, 150, 151, el addendum del plan de cierre de Gate 145, Gate 139, Gate 127 y Gate 128 desde `research/c10-s-consolidation-draft`;
- aceptación Gate 152, registrada en esta rama.

La cadena de bootstrap consultada confirma las versiones declaradas RMA v3.38 / Matrix v1.47 / traceability v3.38. Esta auditoría no ejecutó los validadores locales ni verificó materialmente todos los punteros auxiliares del bootstrap; no se declara un PASS integral de bootstrap.

## 3. Hallazgos normativos

### 3.1 DEC-C10-099 y DEC-C10-102 no son equivalentes

El crosswalk de Gate 149 establece que DEC-C10-099 selecciona V_cont como continuidad temporal de la capacidad efectiva del servicio conforme al propósito B1, y no como uptime del flag ENABLED aislado. No se identifica contradicción entre ese constructo y R148-A.

DEC-C10-102 fija el operador estricto: 1 si la función exigida se cumple durante todo el intervalo; 0 ante incumplimiento funcional confirmado; ? solo por indeterminación propia de truth generada. La formulación abreviada ENABLED/PROFILE no enumera por sí misma las condiciones runtime. La lectura compatible es aplicar el operador estricto al contenido funcional de A_B1, una vez que ese contenido quede definido sin ambigüedad. El operador no necesita cambiar; el predicado al que se aplica requiere delimitación.

### 3.2 R150-A amplió el contrato lógico de B1

R150-A fue aceptada expresamente y establece dos obligaciones funcionales:
- admisión/no admisión conforme a ENABLED;
- exposición del PROFILE declarado en ambos estados.

El texto de Gate 150 también propuso que el incumplimiento confirmado de cualquiera de las obligaciones aplicables haga A_B1=0 en los intervalos afectados. La exposición se mantuvo abstracta, sin interfaz física.

### 3.3 R151-A8 delimitó la adjudicabilidad de PROFILE exposure

La aceptación posterior R151-A8 preserva PROFILE exposure como obligación contractual, pero establece que no existe en el DGP actual una trayectoria temporal independiente para ella; por tanto, su cumplimiento continuo no puede darse por demostrado por EventHistory ni inferirse de la continuidad de admisión.

Esto no elimina la obligación contractual, pero impide incluirla silenciosamente como componente temporal observado/generado de A_B1 bajo el soporte actual.

### 3.4 R152-A dejó abierta precisamente la composición

R152-A1…A6 acepta EventHistory para transiciones declarativas y runtime, conserva PROFILE como configuración/obligación contractual sin trayectoria independiente, incorpora runtime cuando altera admisión, preserva {1,0,?} y continuidad estricta, y deja abierta la composición definitiva de A_B1 antes de afirmar que V_cont mide íntegramente B1.

Por ello, Gate 152 no resolvió la tensión entre la regla de Gate 150 sobre incumplimiento de PROFILE exposure y el límite de adjudicación de R151-A8. No debe interpretarse como resolución implícita.

## 4. Matriz de compatibilidad

| Elemento | Estado tras Gate 153 |
|---|---|
| V_cont como continuidad de capacidad efectiva | Compatible con R148-A |
| Operador estricto DEC-C10-102 | Preservado; no se propone cambiarlo |
| ENABLED y comportamiento de admisión | Temporalmente adjudicables en el DGP, sujetos a EventHistory y §51 |
| PROFILE declarado/versionado | Parte del estado declarativo |
| PROFILE exposure | Obligación contractual confirmada; sin trayectoria temporal independiente adjudicable en DGP actual |
| Runtime que impide admisión requerida | Debe afectar A_B1 cuando el efecto funcional truth esté generado |
| ENABLED=false | No admitir es comportamiento correcto; no debe tratarse como fallo de admisión |
| A_B1 como cumplimiento íntegro de todas las obligaciones B1 | No resuelto; no afirmar equivalencia completa |
| V_cont como Value contextual general | Fuera de alcance; Gate 128 limita VCONT-B1-MIN a dimensión sintética acotada |

## 5. Tensión que impide cerrar el complemento decisional

Hay dos enunciados aceptados que no se pueden combinar sin una regla de alcance:

1. Gate 150/R150-A: el incumplimiento confirmado de cualquiera de las obligaciones funcionales aplicables (incluida PROFILE exposure) hace A_B1=0 en los intervalos afectados.
2. Gate 151/R151-A8: PROFILE exposure no tiene trayectoria temporal independiente adjudicable; su continuidad no se demuestra con EventHistory ni se infiere de la continuidad de admisión.

No es válido resolverlo de ninguna de estas formas:
- convertir PROFILE exposure en UNKNOWN por falta de trayectoria (prohibido por la separación entre indeterminación truth y límite de representación);
- inferir exposición continua a partir de admisión;
- inventar un estado/transición runtime PROFILE_EXPOSURE;
- borrar la obligación contractual de exposición;
- afirmar que A_B1/V_cont adjudica el cumplimiento íntegro de B1 sin limitar el alcance.

## 6. Opciones de resolución para Gate 154

Se identifican dos opciones normativamente distinguibles. Ninguna queda aceptada en este Gate.

**Opción A — A_B1 temporal acotado a la consecuencia representable.**  
Definir A_B1 para DEC-C10-100…102 como predicado temporal de cumplimiento del comportamiento de admisión/no-admisión requerido por ENABLED, incluida la disponibilidad runtime necesaria para realizarlo. PROFILE sigue siendo parte del contrato declarativo y obligación funcional B1, pero fuera del componente temporal adjudicado por V_cont en el DGP actual. La afirmación resultante debe llamarse cumplimiento temporal de la función de admisión B1 / dimensión V_cont seleccionada, no cumplimiento íntegro de todas las obligaciones B1.

Ventaja: compatible con R151-A8 y con la consecuencia focal de Gate 127. Coste: obliga a precisar que V_cont no adjudica PROFILE exposure, pese a que el contrato funcional B1 la mantiene como obligación.

**Opción B — ampliar la representación truth de PROFILE exposure.**  
Reabrir explícitamente R151-A8 y el alcance del DGP para especificar una trayectoria funcional de exposición, su mecanismo generativo y su relación con EventHistory/A_B1. Solo después podría aplicarse continuidad estricta también a esa obligación.

Ventaja: permitiría que A_B1 adjudicara un contrato compuesto más completo. Coste: requiere modificar/ampliar el DGP y resolver causalidad, completitud, observabilidad y no duplicación; no se puede hacer por inferencia ni en el Gate actual.

## 7. Recomendación

Recomendar Opción A como la resolución más conservadora para el DGP vigente, porque:
- respeta la aceptación R151-A8;
- conserva la consecuencia focal de Gate 127 (disponibilidad temporal de la capacidad de admisión);
- no inventa una trayectoria ni un mecanismo para PROFILE exposure;
- mantiene el operador de DEC-C10-102 sin cambios;
- hace explícito el límite de la afirmación de V_cont, evitando atribuirle cumplimiento contractual integral que no puede adjudicar.

La Opción A requiere una aceptación expresa y una redacción cuidadosa: no modifica el contrato lógico completo de B1; delimita el predicado temporal de A_B1/V_cont para el endpoint sintético vigente. Si el objetivo científico requiere que V_cont mida todas las obligaciones B1, la Opción B será necesaria y el DGP actual no bastará.

## 8. Dictamen y siguiente operación

**Dictamen:** DEC-C10-099 es semánticamente compatible con R148-A; DEC-C10-102 conserva íntegramente su operador estricto. La ambigüedad pendiente no está en el operador temporal, sino en el alcance del predicado A_B1 frente a la obligación PROFILE exposure. Gates 150–152 dejan esa composición abierta; por tanto, no procede redactar ni aceptar todavía un complemento decisional como si la composición estuviera resuelta.

**Siguiente operación — Gate 154:** decidir entre A (alcance temporal acotado a admisión efectiva) y B (ampliar la truth del DGP para PROFILE exposure). La decisión deberá declarar expresamente qué afirmación puede sostener V_cont y qué queda fuera.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
