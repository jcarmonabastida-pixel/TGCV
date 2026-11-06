# C10-S — Regla trivalente de agregación de A_f* y D_f observado
**ID:** C10-S-AF-DF-TRI-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-06  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT · reconciliación documental candidata; no aprobada ni ejecutada.  
**Rama:** `research/c10-s-consolidation-draft`

## 1. Propósito y precedencia

Formalizar la propagación 1/0/? para la accesibilidad focal observada `A_f^{obs}`, el predicado de rutas `DEP_f^{obs}` y la transición observada `D_f^{obs}`, reutilizando reglas existentes, sin crear una semántica paralela.

Precedencia y fuentes:
- DGP temporal/rol §§26, 30–32: conjunción de componentes técnicos, separación truth/observed y propagación de Reach.
- Matriz U_G de cobertura y evidencia trivalente §5: ruta como conjunción; conjunto de rutas como disyunción; ausencia exige cobertura exhaustiva.
- Protocolo U_G de evidencia/adjudicación §§2, 5–11, 14 y 17–18: estados ortogonales, cobertura negativa, conflictos, cegamiento y conservación de unknown.
- Fórmula candidata depurada del maestro §67.3 y su crosswalk causal C10-S-AF-XWALK-001.

Esta regla concreta la aplicación a `A_f^{obs}` y `D_f^{obs}`; no altera la fórmula de truth ni cierra los contratos fuente.

## 2. Dominios ortogonales

Para cada predicado y ruta conservar por separado:

- `observed_state ∈ {1,0,?}`: clasificación adjudicada de lo observado.
- `evidence_status ∈ {AVAILABLE,MISSING,CONFLICTING}`: estado del paquete de evidencia.
- `coverage_status ∈ {NONE,PARTIAL,COMPLETE}`: cobertura del universo declarado y versionado.
- `review_adjudication_status`: estado de revisión/adjudicación conforme a U_G.
- `truth_dgp ∈ {0,1}`: solo en generador/evaluador restringido; nunca en paquete del analizador.

No hay conversión mecánica entre estos dominios. En particular, MISSING, NONE, PARTIAL, no inventariado, no observado o sin logs no significan observed_state=0. CONFLICTING no se resuelve por mayoría automática.

## 3. Conjunción de predicados constitutivos

La fórmula candidata de referencia se mantiene:

`A_f^*=I(ID_f^*∧REL_f^*∧COND_f^*∧AUTH_f^*∧RES_f^*∧DEP_f^*∧¬BLOCK_f^*)`.

Para su versión observada, cada término debe haberse adjudicado sobre la misma unidad, identidad τ2, frontera, contexto, snapshot/revisión y ventana temporal compatibles.

| Regla de conjunción observada | Resultado |
|---|---|
| Al menos un término necesario está adjudicado 0 con evidencia válida, alcance compatible y cobertura suficiente para ese incumplimiento | `A_f^{obs}=0` |
| Todos los términos necesarios están adjudicados 1, con identidad/matching y comparabilidad válidos y cobertura adecuada para cada afirmación | `A_f^{obs}=1` |
| No hay un 0 suficiente y al menos un término es ?, falta, conflicto no resuelto, identidad no comparable o cobertura insuficiente | `A_f^{obs}=?` |

**Regla de evidencia negativa:** un 0 local puede bastar para refutar una conjunción si el predicado es realmente necesario y la evidencia válida demuestra su incumplimiento en el alcance focal. No se exige completar los demás términos una vez establecido ese 0. En cambio, no encontrar una ruta, permiso, recurso o componente no basta para adjudicar 0 sin la cobertura negativa que exige U_G.

**Regla positiva:** un 1 requiere respaldo de todos los términos constitutivos. No se infiere por declaración contractual, intención de provisión, éxito de un intento ni por un único componente técnico.

**Conflictos:** un conflicto sobre un término impide adjudicar ese término 1 o 0 hasta resolución. Un 0 independiente, válido y suficiente en otro término necesario puede mantener la conjunción agregada en 0; el conflicto no se oculta y queda registrado. Si el conflicto afecta identidad, frontera, unidad o comparabilidad global, no se calcula el agregado y se conserva ?.

## 4. Agregación específica de DEP y rutas

Cada ruta candidata `r` es una conjunción de predicados necesarios propios y de la secuencia/identidad/versiones/orden temporal:

- `route_obs(r)=1` si todos los necesarios están adjudicados 1 y la secuencia, identidad, versiones, condiciones y orden temporal son compatibles.
- `route_obs(r)=0` si al menos un necesario está adjudicado 0 con evidencia válida y suficiente para esa ruta y alcance.
- `route_obs(r)=?` en cualquier otro caso, incluidos unknown, conflicto material, secuencia incompleta o cobertura insuficiente.

`DEP_f` en el contrato general representa existencia de al menos una ruta admisible válida para la misma transformación focal. Por tanto:

| Universo de rutas candidatas | Resultado de `DEP_f^{obs}` |
|---|---|
| Existe al menos una ruta adjudicada 1 | 1 |
| Todas las rutas del universo operativo declarado están adjudicadas 0 y el universo está COMPLETE; Runknown y rutas externas/compartidas/alternativas materiales están resueltas | 0 |
| No hay ruta 1 y queda alguna ruta ?, Runknown, ruta externa/compartida/alternativa material no inventariada o cobertura NONE/PARTIAL | ? |

Una ruta confirmada 1 basta para `DEP_f^{obs}=1`, aunque otras rutas sigan ?. La existencia de una ruta alternativa válida para la misma τ2 impide declarar DEP=0 solo porque la ruta focal técnica `C_dep` sea 0. `C_dep` y `DEP_f` solo coinciden bajo el supuesto explícito de ruta única del DGP aislado; no se traslada ese supuesto al contrato general sin inventario/cobertura.

## 5. Agregación del bloqueo

El término de la fórmula es `¬BLOCK_f^*`. Se conserva esta convención:

- `BLOCK_f^{obs}=1` (bloqueo efectivo demostrado para la accesibilidad focal, no solo para una ruta no necesaria) implica `¬BLOCK_f^{obs}=0` y puede hacer `A_f^{obs}=0`.
- `BLOCK_f^{obs}=0` solo puede sostener `¬BLOCK_f^{obs}=1` con cobertura suficiente del universo de bloqueos relevantes dentro de la frontera/ventana declaradas.
- Si bloqueo o cobertura permanecen ?, el término negado permanece ?.

Un bloqueo de una ruta no implica bloqueo de todas las rutas alternativas. Un conflicto o falta de logs no equivale a ausencia de bloqueo.

## 6. Derivación basal→post de D_f^{obs}

La transición verdadera sigue siendo `D_f^*=I(A_{f,base}^*=0 ∧ A_{f,post}^*=1)`. La transición observada se deriva de los dos estados observados, no de Z, B, intento, C_dep, selección o ejecución.

| `A_{f,base}^{obs}` | `A_{f,post}^{obs}` | `D_f^{obs}` | Interpretación |
|---|---|---|---|
| 0 | 1 | 1 | Apertura observada |
| 0 | 0 | 0 | No apertura: sigue inaccesible |
| 1 | 0 | 0 | Pérdida, no apertura |
| 1 | 1 | 0 | Ya accesible en baseline; no apertura |
| ? | 0 | 0 | Estado post descarta la condición de apertura |
| ? | 1 | ? | Baseline indeterminado |
| 0 | ? | ? | Post indeterminado |
| ? | ? | ? | Ambos indeterminados |

Regla general equivalente: `D_f^{obs}=1` solo si baseline=0 y post=1; `D_f^{obs}=0` si baseline=1 o post=0; en los demás casos `D_f^{obs}=?`.

**No comparabilidad:** si identidad semántica τ2, frontera, unidad/contexto, granularidad, catálogo, mapping o versiones no permiten comparar los snapshots, la transición focal no se calcula como apertura ni como no apertura; se registra `D_f^{obs}=?` con motivo `NOT_COMPARABLE`/unresolved. No se convierte en 0.

La población focal verdadera de apertura exige `A_{f,base}^*=0) pre-Z. Una clasificación observada basal 0 no sustituye automáticamente esa condición de elegibilidad verdadera; el error de clasificación y la selección de elegibles deben tratarse explícitamente.

## 7. Ejemplos de frontera (lógicos, no datos ni escenarios ejecutados)

1. `ID=1, REL=1, COND=1, AUTH=1, RES=1, DEP=?, ¬BLOCK=1` → `A_f^{obs}=?`.
2. Mismos términos, pero `AUTH=0` con evidencia normativa/efectiva válida y focal → `A_f^{obs}=0`, aunque DEP siga ?.
3. Ruta focal=0, ruta alternativa equivalente=1 → `DEP_f^{obs}=1`; no inferir A=0 desde `C_dep=0`.
4. Ninguna ruta confirmada; Runknown permanece ? → `DEP_f^{obs}=?`, nunca 0.
5. Todas las rutas inventariadas=0 pero cobertura PARTIAL → `DEP_f^{obs}=?`.
6. Baseline=0 y post=? → `D_f^{obs}=?`, no 0.
7. Baseline=? y post=1 → `D_f^{obs}=?`, no 1.
8. Snapshot post con τ2 distinta/no comparable → `D_f^{obs}=?`, no apertura ni pérdida.

## 8. Contrato mínimo de trazabilidad

Cada agregado debe ser reproducible mediante vínculos a:
- unidad, frontera, contexto, τ2/TID, versión y snapshot/revisión basal/post;
- predicado/ruta y regla versionada que produce el estado;
- evidencia, fuente, hash, método, tiempo/ventana, observador y cegamiento;
- evidence_status, coverage_status, denominador/scope y limitaciones;
- evaluaciones independientes, conflictos, adjudicación y posición minoritaria;
- composición exacta de términos/rutas utilizada en el agregado;
- razón explícita para 0, 1 o ?; para ? registrar unknown_reason.

El analizador no recibe `truth_dgp`, Z/B ni Outcome/Value cuando el contrato exige cegamiento. El evaluador accede a truth solo después de congelar la salida observada.

## 9. Implicaciones para primera etapa e IV

- La primera etapa causal de interés se define sobre `D_f^*` verdadero en el DGP, no sobre `D_f^{obs}` sin más.
- `D_f^{obs}` sirve para evaluar el proceso de medición y estimar una primera etapa observada; no sustituye a la verdadera si existe error diferencial/desconocido.
- No convertir ? en 0, excluir indeterminados como si fueran aleatorios ni imputar estado sin modelo explícito.
- Reportar por brazo/tiempo/version/ruta la distribución de 1/0/?, missingness, conflictos, cobertura y error contra truth restringida después de congelar.
- Si sensibilidad/especificidad, dependencia de errores o missingness no están identificadas, usar sensibilidad/límites o declarar no identificación; no aplicar corrección puntual ficticia.
- La regla trivalente no resuelve independencia, exclusión, monotonicidad, interferencia, consistencia ni relevancia IV. `LATE_f` permanece bloqueado.

## 10. Estado, límites y cuestiones pendientes

Esta es una reconciliación documental asistida de reglas ya presentes en DGP §26/§32, matriz U_G §5 y protocolo U_G §§5–11/17. No es decisión aceptada ni freeze; no se ha aplicado a registros, fuentes o truth reales/sintéticos; no se ha implementado ni validado con parser/fixtures. Requiere revisión independiente.

Pendientes:
- armonizar formalmente la tabla de `D_f^{obs}` con los dominios de plantilla U_G y el contrato de matching/snapshots;
- revisar con DEC-C10-065 y UG-SCH-10 la identidad exacta de snapshot/revisión y pertenencia de todas las referencias;
- concretar predicados/rutas del microdominio sin declarar rutas reales no inventariadas;
- diseñar fixtures adversariales para conflictos, unknowns, rutas alternativas, cobertura negativa, identidad/versionado y no comparabilidad;
- medir clasificación/error diferencial con truth oculta, bajo autorización futura.

No se cierra MEAS-G2…G8, UG-SCH-10, XSYNC, PROV, MD-C1/MD-C4 ni gates IV. No se modifica DEC-C10-065/066/067, fórmula candidata, DGP, RMA, Matrix, STATUS, Core o claims. No autoriza implementación, validación ejecutable, simulación, experimento o acceso a sistemas reales.
