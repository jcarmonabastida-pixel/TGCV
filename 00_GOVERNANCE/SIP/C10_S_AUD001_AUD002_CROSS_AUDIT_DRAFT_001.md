# C10-S — Auditoría cruzada de la resolución AUD-001/AUD-002
**Informe de revisión — borrador 001**

**Estado:** DRAFT / REVISIÓN DOCUMENTAL — NO APROBADA  
**Objeto:** `C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md`  
**Hallazgos de origen:** AUD-C10S-001 y AUD-C10S-002  
**Alcance:** coherencia causal, transformacional, operacional y editorial.  
**No realizado:** ejecución, simulación, estimación estadística ni auditoría de código.

**Aviso de precedencia vigente (2026-11-09):** esta auditoría revisa la propuesta histórica AUD-001/002 de intervención focal sobre autorización. Sus hallazgos siguen siendo útiles para comprender ese escenario alternativo, pero no deben reabrir la política primaria D2 ni tratar `C_auth,base=1`/`AUTH_f*` como obsoletos. DEC-C10-066/067 rigen D2: provisión técnica focal con autorización basal común e invariante. No usar esta auditoría como contrato operativo de D2 ni como fuente para generar código D2.

---

## 1. Dictamen

La propuesta mejora sustancialmente la arquitectura conceptual: separa accesibilidad focal, espacio accesible y delta transformacional; conecta los módulos mediante una unidad sintética común; mantiene separadas candidatas, selección, ejecución, Outcome y Value; y conserva la exclusividad de `τ2` como cuestión sometida a prueba.

No obstante, **AUD-001 y AUD-002 no pueden cerrarse todavía**. Se identifica una inconsistencia crítica en la definición conjunta de `q), `g_1/g_0) y `C_auth), además de cuestiones mayores sobre la intervención causal, el significado de accesibilidad, la relación entre asignación y manipulación, y la ejecución estandarizada.

**Dictamen: revisión mayor; la propuesta no está lista para armonización como contrato aceptado ni para implementación.**

## 2. Hallazgo crítico

### XAUD-001 — Posible contradicción entre el régimen q y las políticas g

**Severidad:** CRÍTICA  
**Estado:** ABIERTO

La propuesta define:
- `C_auth` como condición que habilita la realizabilidad de `τ2`;
- `A_f^*` como accesibilidad focal derivada;
- `q` como régimen común de condiciones/historias;
- `g_1,g_0` como políticas que modifican la probabilidad de acceso a `τ2`.

Pero no especifica si `C_auth` forma parte de las variables controladas por `q). Si q fija o determina `C_auth), mientras g intenta modificar el acceso mediante esa misma autorización, el contraste puede ser contradictorio: q neutralizaría la intervención de g o dejaría sin definir qué régimen se está comparando.

**Corrección requerida:**

1. Separar las condiciones/historias reguladas por q de la condición manipulada por la política focal.
2. Definir explícitamente si g interviene sobre `C_auth` y `A_f^*) es una consecuencia estructural de esa intervención, o si existe una intervención directa sobre accesibilidad que sea físicamente realizable sin fijar una condición constitutiva incompatible.
3. No describir g como una política abstracta que “cambia A”. Especificar su acción sobre un mecanismo/condición manipulable, su probabilidad, elegibilidad, cumplimiento y soporte.
4. Definir q como régimen común de las demás condiciones e historias pertinentes, excluyendo la variable que g debe manipular; o definir un régimen conjunto coherente `(q,g)` en el que no haya asignaciones incompatibles.
5. Precisar el estimando como efecto de una política de habilitación/autorización que induce un cambio en accesibilidad focal, si ese es el objeto físicamente implementable. No llamarlo efecto puro de A_f si la intervención tiene otras consecuencias.

**Criterio de cierre:** para cada unidad e historia admisible, las políticas comparadas deben poder coexistir con q, respetar condiciones constitutivas y generar contrafactuales bien definidos. La especificación debe mostrar qué se interviene, qué se mantiene común y qué variable resulta afectada.

## 3. Hallazgos mayores

### XAUD-002 — La intervención sobre A_f no está definida como intervención causal autónoma

**Severidad:** ALTA  
**Estado:** ABIERTO

La propuesta alterna entre una política de autorización `Z_A → C_auth → A_f^*) y un estimando presentado como efecto de accesibilidad `θ_{A_f}(q)). Si no existe intervención físicamente coherente sobre A_f separada de C_auth, el efecto identificable puede ser el efecto de la política de habilitación, no un efecto autónomo del mediador A_f.

**Corrección requerida:** definir dos objetos distintos:
- ITT de la asignación/política de habilitación `Z_A);
- efecto de una intervención estocástica sobre accesibilidad solo si se especifica una política realizable y supuestos de identificación suficientes.

La diferencia entre ambos no debe resolverse por cambio de nombre. Si la intervención afecta expectativas, información, incentivos o trato, el ITT incluye esas vías. La atribución exclusiva a A_f requiere diseño adicional o supuestos explícitos y defendibles.

### XAUD-003 — Accesibilidad focal, realizabilidad y aplicabilidad necesitan predicados separados

**Severidad:** ALTA  
**Estado:** ABIERTO

La propuesta define `A_f^*) como “realizable y accesible”, pero INT-03 admite que `τ2` sea accesible y no aplicable desde `S0). Esta distinción es conceptualmente correcta, pero la definición formal no la refleja con claridad.

**Corrección requerida:** distinguir al menos:
- `Acc_f(s,h)`: la transformación pertenece al espacio accesible bajo el sistema/contexto/historia definidos;
- `App_f(s,h)`: sus precondiciones se satisfacen en el estado actual;
- `Exec_f`: la transformación se ejecutó efectivamente.

La relación entre accesibilidad y aplicabilidad debe quedar definida. No inferir `App_f=1) de `Acc_f=1), ni `Exec_f=1) de cualquiera de ellas.

### XAUD-004 — Asignación aleatoria, manipulación perfecta y no cumplimiento

**Severidad:** ALTA  
**Estado:** ABIERTO

La igualdad `A_f^*=Z_A) es aceptable como escenario ideal sintético, pero debe evitarse que se convierta en la estructura general de todos los escenarios. La asignación, condición habilitadora, accesibilidad verdadera y clasificación observada son variables diferentes.

**Corrección requerida:** el DGP debe distinguir:
- asignación `Z_A);
- condición efectivamente recibida `C_auth);
- accesibilidad verdadera `A_f^*);
- clasificación/medición `A_f^{obs});
- aplicabilidad `App_f);
- ejecución `Exec_f).

Definir explícitamente escenarios de cumplimiento perfecto, incumplimiento, error de medición y estados indeterminados. No usar la asignación como sustituto de accesibilidad en el análisis.

### XAUD-005 — Régimen E1 puede cambiar el objeto causal si fuerza una ejecución

**Severidad:** ALTA  
**Estado:** ABIERTO

E1 se describe como ejecución estandarizada “forzada”. Si fuerza `τ2) incluso cuando no es accesible, no aplicable o sus condiciones no se cumplen, contradice el generador transformacional. Si solo fuerza la selección entre trayectorias válidas, debe decirse así.

**Corrección requerida:** especificar E1 como política estandarizada de selección/ejecución condicionada a la existencia de una trayectoria válida y ejecutable. En el brazo sin esa trayectoria, registrar no ejecución o fallo por falta de ruta; nunca saltarse precondiciones. Si se manipula artificialmente la ejecución, etiquetar ese experimento como intervención distinta, no como prueba de accesibilidad.

### XAUD-006 — Cadena generativa requiere orden temporal y reglas de actualización explícitas

**Severidad:** ALTA  
**Estado:** ABIERTO

La cadena `X,S0 → Z_A → C_auth → A_f^* → T_acc → (Reach, Π_H) → selección → ejecución → M → O → V` es útil como mapa, pero no especifica snapshots ni reevaluaciones. T_acc, aplicabilidad y relaciones pueden cambiar en estados hipotéticos sucesivos.

**Corrección requerida:** definir:
- snapshot basal previo a asignación;
- snapshot posterior a la condición habilitadora;
- evaluación de accesibilidad por rama/estado hipotético;
- evaluación de aplicabilidad antes de cada transformación;
- snapshot post-ejecución separado;
- reglas de versionado y tiempo de cada variable.

No reconstruir el snapshot basal a partir del estado postintervención.

## 4. Hallazgo editorial y de formalización

### XAUD-007 — La propuesta contiene errores de notación y delimitación

**Severidad:** MEDIA  
**Estado:** ABIERTO

La versión recuperada contiene delimitadores desbalanceados en varios símbolos (`T_acc))`, `ΔT_acc))`, `A_f^*)`, `q)`, `τ2)`, etc.), paréntesis espurios en la tabla de acceso y expresiones que pueden dificultar su interpretación.

**Corrección requerida:** normalizar notación y revisar automáticamente delimitadores Markdown/LaTeX antes de incorporar el texto al documento maestro. Mantener una sola forma canónica para cada variable.

## 5. Recomendación de resolución

Orden recomendado:

1. Resolver XAUD-001: decidir formalmente qué controla q y qué manipula g.
2. Resolver XAUD-002: separar ITT de la política habilitadora y el efecto atribuible a accesibilidad.
3. Resolver XAUD-003/004: diccionario de estados de accesibilidad, aplicabilidad, asignación, medición y ejecución.
4. Resolver XAUD-005/006: definir E1 sin violar precondiciones y fijar snapshots/temporalidad.
5. Corregir notación y después armonizar los documentos.
6. Solo entonces convertir INT-01 a INT-08 en fichas de prueba ejecutables.

No conviene redactar todavía ecuaciones definitivas para `θ_{A_f}(q)) hasta resolver XAUD-001 y XAUD-002. Una notación aparentemente formal no debe ocultar que la intervención aún no está especificada.

## 6. Estado y límites

- AUD-001: permanece abierto.
- AUD-002: permanece abierto.
- No se ha aceptado la propuesta de resolución.
- No se ha ejecutado código ni simulación.
- No se ha validado potencia, cobertura o identificación con datos.
- No se modifica Core, RMA, Evidence→Claim Matrix, STATUS ni claims.
- Este informe es una revisión documental, no evidencia empírica sobre C10.

**Conclusión:** la integración propuesta es una dirección adecuada, pero antes de cerrar los bloqueos P0 hay que definir una intervención físicamente coherente y separar con rigor el efecto de la política de habilitación del efecto causal atribuible al cambio de accesibilidad.


---
## 7. Delimitación de alcance tras DEC-C10-066/067 (2026-11-09)

Los hallazgos, recomendaciones y siguientes pasos de §§1–6 se refieren a la propuesta histórica AUD-001/002 de intervención focal sobre autorización. No constituyen una recomendación pendiente para seleccionar o construir la política primaria D2.

Para D2 rigen DEC-C10-066/067: provisión técnica focal, con C_auth,base=1 común e invariante; C_auth_base se corresponde con AUTH_f*. La intervención focal sobre autorización solo puede recuperarse como escenario alternativo/adversarial, con política, estimando y vías causales propios.

Por tanto, la frase de §6 sobre definir una intervención físicamente coherente antes de cerrar los bloqueos P0 se limita a la eventual reutilización de AUD-001/002 como escenario alternativo. No reabre D2 ni convierte este informe en contrato operativo. La correspondencia general B→g^Af, exclusión, vías colaterales y revisión independiente continúan abiertos en sus artefactos rectores. No se autoriza freeze, implementación, simulación ni ejecución.

