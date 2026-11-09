# C10-S — Auditoría integrada de consistencia científica y transformacional
**Informe de auditoría documental — borrador 001**

**Estado:** DRAFT / AUDITORÍA DOCUMENTAL — NO APROBADA  
**Documento auditado:** `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`  
**PR de trabajo:** #116 — C10-S consolidated synthetic experiment specification  
**Alcance:** consistencia conceptual, causal, transformacional y de protocolos de prueba.  
**No realizado:** ejecución de código, simulación, validación estadística, auditoría de implementación o revisión independiente externa.  
**Efecto científico:** ninguno. No modifica Core, RMA, Evidence→Claim Matrix, STATUS, claims ni cierres.

**Aviso de precedencia vigente (2026-11-09):** esta auditoría registra hallazgos históricos AUD-001…012 y no es una especificación operativa autónoma. Para el D2 primario candidato prevalecen DEC-C10-066/067 y el maestro §§0.5, 51, 53, 131–132: D2 primario candidato/D1 secundario; provisión técnica focal; `C_auth,base=1` común e invariante; `C_auth_base` se corresponde con `AUTH_f*`. Las observaciones históricas sobre intervención focal de `C_auth` pertenecen al escenario alternativo AUD-001/002 y no deben reabrir D2. Los hallazgos abiertos que no hayan sido resueltos expresamente por esas decisiones conservan su estado y alcance.

---

## 1. Dictamen ejecutivo

La consolidación representa adecuadamente buena parte de las decisiones conceptuales desarrolladas en C10-S y corrige una inconsistencia importante del catálogo: `τ4 (Escalate)` no habilita `τ3 (Verify)`, y `τ3` conserva la precondición de configuración técnicamente modificada. También diferencia accesibilidad, aplicabilidad, Reach, trayectorias candidatas, selección y ejecución; distingue identidad de sustituibilidad; y mantiene separados TE, `θ_A(q)` y los escenarios de no-identificación.

Sin embargo, la especificación **todavía no está lista para implementación ni para considerarse un protocolo de pruebas ejecutable**. Se identifican dos bloqueos estructurales:

1. La variable causal binaria `A` no está definida con precisión suficiente respecto al objeto transformacional `ΔT_acc`.
2. La arquitectura causal sintética y el generador TGCV están descritos en paralelo, pero no existe todavía un contrato que demuestre que ambos forman una misma cadena generativa integrada desde la manipulación de accesibilidad hasta la ejecución, Outcome y Value.

Además, los catálogos de pruebas están definidos principalmente como inventarios de casos, no como protocolos reproducibles con fixtures, entradas, aserciones, criterios PASS/FAIL/INDETERMINATE y artefactos de evidencia.

**Dictamen global: REVISIÓN MAYOR REQUERIDA / NO LISTO PARA IMPLEMENTACIÓN.**

Esto no invalida C10-S. Significa que la arquitectura conceptual ha avanzado más que su especificación operacional y que conviene cerrar esas brechas antes de programar.

---

## 2. Hallazgos críticos

### AUD-C10S-001 — Definición incompleta de A respecto de ΔT_acc

**Severidad:** CRÍTICA  
**Estado:** ABIERTO

El documento define `A` como “cambio focal de accesibilidad, operacionalizado mediante ΔT_acc”, pero los modelos sintéticos tratan `A` como una variable binaria (por ejemplo, `A=Z`, o políticas `g_1(A=1)` y `g_0(A=1)`). En cambio, `ΔT_acc` es un cambio estructurado de conjuntos/unidades, relaciones y condiciones. No son automáticamente el mismo objeto.

**Riesgo:** el estimando `θ_A(q)` puede parecer un efecto de una política sobre todo el espacio transformacional cuando el DGP solo manipula la disponibilidad de una transformación focal.

**Corrección requerida:**

1. Definir `A_f` como estado binario/ordinal de accesibilidad de la transformación focal `τ_f`, por ejemplo `A_f=1` si `τ_f` está respaldada como accesible bajo las condiciones especificadas.
2. Definir por separado `T_acc,t` y `ΔT_acc=(A^+,A^-;ΔR,ΔC)`, o una representación formal equivalente, con cambios de unidades, relaciones y condiciones claramente diferenciados.
3. Definir la relación entre la manipulación de `A_f` y el cambio observado en el espacio completo: `Z → A_f → ΔT_acc`. En el experimento focal, especificar si `ΔT_acc` solo contiene el cambio de `τ_f` o si también cambian relaciones/condiciones.
4. Reescribir `θ_A(q)` para que las políticas `g_1,g_0` actúen sobre un objeto inequívoco. Si el objetivo es la política de acceso a `τ_f`, nombrarlo como tal; no generalizarlo automáticamente a toda `ΔT_acc`.

**Criterio de cierre:** ningún símbolo `A` en ecuaciones, diccionario o estimandos debe confundirse con el conjunto `ΔT_acc`; la política causal debe tener una intervención bien definida y factible.

### AUD-C10S-002 — Falta de integración entre DGP causal y DGP transformacional

**Severidad:** CRÍTICA  
**Estado:** ABIERTO

El documento define:
- un catálogo de transformaciones `τ1–τ4` y rutas G0/G1;
- un generador de trayectorias y Reach;
- modelos causales abstractos con `A → M → O → V`, donde `M` es una variable continua.

Pero no especifica cómo una unidad sintética generada por el primer sistema produce las variables del segundo. No hay contrato común que conecte inequívocamente:
`Z → condición habilitadora → A_f/T_acc → Π_H/Reach → selección → ejecución → O → V`.

**Riesgo:** podrían superarse por separado pruebas del generador y pruebas de recuperación causal aunque el pipeline conjunto no represente la hipótesis C10 que se quiere evaluar. Se probarían dos componentes correctos pero desconectados.

**Corrección requerida:**

1. Definir una unidad sintética común y un identificador estable que atraviese todos los módulos.
2. Especificar el efecto de `Z` sobre la condición constitutiva de `τ2` y cómo esa condición modifica la clasificación ciega de `A_f`.
3. Conectar las trayectorias candidatas generadas con selección y ejecución. Definir qué evento observable cuenta como ejecución de `τ2` y `τ3`.
4. Definir cómo ejecución y mecanismos generan `O`; y cómo la regla independiente transforma `O` y otras dimensiones admisibles en `V`.
5. Mantener la verdad generadora oculta al analizador y al evaluador de cada módulo, salvo en el rol de evaluación independiente.
6. Conservar escenarios abstractos de identificación causal como pruebas unitarias, pero añadir escenarios integrados de extremo a extremo.

**Criterio de cierre:** debe existir al menos un DGP integrado en el que la misma unidad permita reconstruir, sin filtración de verdad, asignación, accesibilidad, Reach, trayectorias, ejecución, Outcome y Value; y en el que el evaluador pueda comprobar cada eslabón por separado.

### AUD-C10S-003 — Los protocolos de pruebas aún no son contratos ejecutables

**Severidad:** ALTA  
**Estado:** ABIERTO

EQ, EX, TG, SR, CV y V enumeran objetivos de prueba, pero en la mayoría de casos no incluyen:
- fixture/catálogo exacto;
- estado inicial y condiciones;
- entradas observables al módulo;
- salida esperada exacta;
- aserciones;
- tolerancias numéricas cuando proceda;
- criterios PASS/FAIL/INDETERMINATE;
- artefactos y hashes a conservar.

**Riesgo:** distintos implementadores podrían interpretar una misma prueba de manera diferente y obtener resultados no comparables.

**Corrección requerida:** para cada prueba, crear una ficha normalizada:
`test_id, objetivo, fixture_version, inputs, hidden_truth, expected_output, assertions, tolerance, failure_codes, evidence_artifacts`.

La verdad oculta solo estará disponible al generador/evaluador; no al analizador que se somete a prueba.

**Criterio de cierre:** todas las pruebas requeridas para el gate C10-S→C10-P tienen entradas, salidas esperadas y aserciones inequívocas. Las pruebas exploratorias restantes pueden seguir etiquetadas como no ejecutables.

---

## 3. Hallazgos mayores

### AUD-C10S-004 — ΔT_acc relacional no formalizado de extremo a extremo

**Severidad:** ALTA  
**Estado:** ABIERTO

La sección 3.3 define `A⁺` y `A⁻` como diferencias de conjuntos, mientras que 3.4 representa `T_acc=(U_acc,R_acc,C_acc)`. La frase “registrar por separado cambios en identidades/unidades, relaciones y configuraciones” no define formalmente el delta relacional.

**Corrección requerida:** especificar, como mínimo:
- `ΔU=(U_1\U_0,U_0\U_1)`;
- `ΔR=(R_1\R_0,R_0\R_1)`;
- `ΔC=(C_1\C_0,C_0\C_1)`;
- regla de identidad/versionado común;
- cómo se representan relaciones cuya validez cambia por condiciones sin que cambie su identidad;
- cómo se tratan cambios indeterminados.

No asumir que un delta en R o C es una transformación nueva.

### AUD-C10S-005 — Salidas de Reach_possible y trayectorias indeterminadas insuficientemente especificadas

**Severidad:** ALTA  
**Estado:** ABIERTO

El contrato introduce `Reach_definite` y `Reach_possible`, pero no formaliza la propagación de incertidumbre, la deduplicación entre ambas ni el estado de una trayectoria que combina pasos confirmados e indeterminados.

**Corrección requerida:** definir una lógica de tres estados para cada predicado y reglas de composición. Un estado alcanzable solo debe pertenecer a `Reach_definite` si existe al menos una trayectoria íntegramente respaldada. Debe pertenecer a `Reach_possible` si existe una trayectoria compatible cuya validez depende de una o más condiciones indeterminadas y no existe evidencia que la descarte. Documentar cómo se resuelven estados presentes en ambas búsquedas y evitar doble conteo.

### AUD-C10S-006 — Escenario S5-F necesita ecuaciones generadoras completas

**Severidad:** ALTA  
**Estado:** ABIERTO

S5-F declara dos asignaciones independientes y contribuciones +6 y +5, pero no escribe el DGP completo ni el objeto exacto afectado por `N`.

**Corrección requerida:** especificar, por ejemplo, la independencia de `Z_A` y `Z_D`, `A=Z_A`, el mecanismo de `M), `O=2M+ε_O), `N=Z_D) y `V=3O+5N+ε_V), o una alternativa justificada. Declarar explícitamente si hay interacción y cuál es el estimando de cada factor. No dejar que la descripción verbal sustituya a la ecuación.

### AUD-C10S-007 — S5-C debe distinguir verdad estructural de identificabilidad observacional

**Severidad:** ALTA  
**Estado:** ABIERTO

S5-C afirma que el generador conoce una contribución estructural de A (+6), pero que el analizador no puede separarla de la vía directa Z→V porque A=Z. Es coherente como escenario de no-identificación, pero debe quedar explícito que el efecto estructural conocido por el generador no se recupera del soporte observado bajo ese diseño.

**Corrección requerida:** registrar por separado:
- efecto contrafactual estructural definido en el DGP;
- soporte observado;
- estimando objetivo;
- conclusión permitida al analizador: TE estimado y efecto específico de A no identificado bajo los datos/diseño observados.

No presentar el +6 como estimación identificada por el analizador.

### AUD-C10S-008 — Criterio de independencia entre Value y T_acc requiere pruebas de no circularidad más precisas

**Severidad:** ALTA  
**Estado:** ABIERTO

La regla establece que Value no debe premiar automáticamente cardinalidad o longitud de trayectoria, pero V-01/V-02 no incluyen fixtures que detecten dependencia accidental o filtración.

**Corrección requerida:** incluir pruebas metamórficas: mantener O, beneficiario y regla Value constantes mientras cambia T_acc; el Value calculado no debe cambiar salvo que la regla haya preespecificado explícitamente una dimensión de opción/potencial. Inversamente, cambiar O manteniendo T_acc debe cambiar V cuando la regla así lo determine. Separar V_real de V_potential.

---

## 4. Hallazgos de precisión y trazabilidad

### AUD-C10S-009 — Parámetros de simulación aún no justifican potencia ni precisión

**Severidad:** MEDIA  
**Estado:** ABIERTO

N=2000 y 1000 réplicas son valores preliminares. No se ha demostrado potencia, cobertura, sesgo, error Monte Carlo ni precisión de las tasas de clasificación de escenarios.

**Corrección requerida:** antes de congelar parámetros, definir métricas de recuperación y su incertidumbre Monte Carlo; justificar N y número de réplicas por escenario, especialmente para heterogeneidad, error de medición, soporte parcial y falsos positivos de identificación.

### AUD-C10S-010 — Diccionario de datos necesita separación por rol y tiempo

**Severidad:** MEDIA  
**Estado:** ABIERTO

El diccionario lista variables pero no indica de forma exhaustiva quién puede observar cada campo ni cuándo se genera.

**Corrección requerida:** matriz variable × rol (generador, analizador TGCV, analizador causal, evaluador) y momento temporal (basal, post-asignación, post-accesibilidad, post-selección, post-ejecución, Outcome, Value). Marcar explícitamente las columnas de verdad oculta.

### AUD-C10S-011 — Condiciones constitutivas y otras L necesitan clasificación operacional

**Severidad:** MEDIA  
**Estado:** ABIERTO

El documento distingue conceptualmente condiciones constitutivas `C_c) y condiciones post-tratamiento `L), pero falta una regla de clasificación aplicable a cada variable del DGP y al caso real.

**Corrección requerida:** para cada condición registrar su temporalidad, posibilidad de intervención, relación con realizabilidad, si es constitutiva, mediadora, confusora inducida por tratamiento o variable de contexto. No clasificarla por nombre, sino por su papel causal en el DAG y en el régimen de intervención.

### AUD-C10S-012 — La referencia conversacional no sustituye un historial documental versionado

**Severidad:** MEDIA  
**Estado:** ABIERTO

La sección de trazabilidad describe rangos de secciones conversacionales de forma aproximada. Es útil como índice, pero no permite reconstruir literalmente cada decisión ni verificar por sí sola qué formulación fue sustituida.

**Corrección requerida:** mantener un decision log versionado con ID, decisión, alternativas consideradas, justificación, sección afectada, fecha/orden, estado (propuesta/aceptada/sustituida) y referencia al commit o revisión que la incorpora. No declarar transcripción exhaustiva.

---

## 5. Revisión de consistencia del catálogo transformacional

### 5.1. Aspectos coherentes

- `τ3 (Verify)` conserva el requisito de configuración técnicamente modificada.
- `τ4 (Escalate)` cambia responsabilidad/unidad receptora; no modifica por sí misma la configuración técnica.
- `r43` está excluida de las relaciones activas.
- G0: `τ1→τ4`, finalizando en transferencia.
- G1: `τ1→τ2→τ3`, finalizando en configuración reconfigurada y verificada.
- `H=3` permite la trayectoria G1 sin exceder el horizonte.
- La exclusividad de `τ2) sigue abierta y no se declara demostrada.

### 5.2. Aspectos aún no demostrados

- que `τ2) sea la única transformación/composición que satisface la función focal F* en G0/G1;
- que no existan rutas distribuidas o externas;
- que la autorización sea la única condición diferencial relevante;
- que la evaluación de accesibilidad sea independiente de Outcome y Value;
- que las condiciones y relaciones se reevalúen de forma correcta en todos los estados hipotéticos.

### 5.3. Dictamen del catálogo

**CONSISTENCIA SEMÁNTICA INTERNA: PROVISIONALMENTE COHERENTE.**  
**EXCLUSIVIDAD FUNCIONAL: INDETERMINADA.**  
**COMPLETITUD EMPÍRICA: NO EVALUADA.**

---

## 6. Matriz de prioridades de resolución

| Prioridad | Hallazgos | Acción antes de |
|---|---|---|
| P0 — Bloqueante | AUD-001, AUD-002 | Cualquier implementación integrada |
| P1 — Necesaria para protocolo ejecutable | AUD-003 a AUD-008 | Congelar contrato y suite de pruebas |
| P2 — Necesaria para evaluación cuantitativa | AUD-009 | Fijar N, réplicas y criterios de precisión |
| P2 — Necesaria para reproducibilidad | AUD-010 a AUD-012 | Congelar paquete experimental y trazabilidad |

No se recomienda implementar hasta cerrar P0 y P1. Los puntos P2 pueden desarrollarse en paralelo documentalmente, pero deben estar resueltos antes de interpretar resultados o afirmar reproducibilidad completa.

---

## 7. Decisiones y límites

1. Esta auditoría es documental y conceptual; no es auditoría de código ni de resultados.
2. No se ha ejecutado ninguna prueba ni simulación.
3. No se ha calculado potencia.
4. No se ha seleccionado ni validado un caso real.
5. No se ha cambiado el estado de C10-D1 ni de la gobernanza científica.
6. Ningún hallazgo constituye por sí solo evidencia a favor o en contra de la hipótesis C10.
7. Los hallazgos abiertos deben resolverse en el documento C10-S y quedar versionados antes de derivar contratos ejecutables.

---

## 8. Recomendación de continuación

La siguiente unidad de trabajo debe ser documental y secuencial:

1. resolver AUD-001 y AUD-002, definiendo la variable focal y el DGP integrado;
2. formalizar el delta relacional y la propagación de indeterminación;
3. convertir las pruebas de mayor prioridad en fichas ejecutables;
4. completar S5-F y aclarar la lectura de S5-C;
5. definir las matrices de acceso a datos por rol y temporalidad;
6. cerrar parámetros y métricas de precisión solo después de definir los objetivos de recuperación.

**Estado de salida:** C10-S consolidado, pero con revisión mayor abierta. No listo para implementación/ejecución.
