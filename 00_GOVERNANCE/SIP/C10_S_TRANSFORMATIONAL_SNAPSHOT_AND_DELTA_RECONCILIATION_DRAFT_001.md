# C10-S — Contrato de snapshots transformacionales y separación de ΔT_acc / evidencia
**ID:** C10-S-SNAP-DELTA-001 · **Versión:** Draft 001 · **Corte:** 2026-11-04  
**Estado:** RECONCILIACIÓN PROPUESTA / NO APROBADA / NO CONGELADA.  
**Ámbito:** Bloque 3, subbloque de snapshots, correspondencia, ΔT_acc y validez epistémica.  
**No autoriza:** implementación, simulación, ejecución ni freeze.

**Aviso de precedencia vigente (2026-11-09):** este documento conserva la propuesta histórica de reconciliación de snapshots/delta y no es una especificación operativa autónoma. La formulación anterior de §63.7 que incluía `ΔValidity` en `ΔT_acc*` queda supersedida. Para la lectura actual prevalece el maestro §58.6: `S_T*=(U_t*,R_t*,C_t*,X_t*)`, `E_T` separado y `ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*)`; `ΔE_T` contiene cambios de evidencia/observabilidad. La propuesta aquí documentada no se convierte por este aviso en decisión aceptada ni en freeze.

## 1. Hallazgo de auditoría: conflación entre cambio estructural y cambio epistémico

La lectura conjunta de maestro §§43.1, 58.1–58.2, 63.5–63.9, 67.3–67.6, DGP §§26–29 y contratos ACC/JNT/FIX revela una inconsistencia de clasificación:

- §63.7 define el snapshot con U_acc, R_acc, C_acc, Validity y State/context y expresa ΔT_acc*=(ΔU, ΔR, ΔC, ΔValidity, ΔState).
- §67.3 y §67.6 establecen que VALID_f, cobertura y calidad de evidencia no pertenecen a la verdad estructural causal de A_f*; son requisitos epistémicos para clasificar A_f,obs.
- §64.2 y DEC-C10-023 también tratan VALID/cobertura como proceso de medición, no como condición causal del sistema.

No se puede mantener simultáneamente que la calidad/cobertura de evidencia es epistémica y que cualquier cambio en esa calidad es, sin cualificación, un componente del cambio real del espacio accesible. Un aumento de cobertura puede revelar transformaciones que ya eran accesibles; no necesariamente las crea. Del mismo modo, perder registros no necesariamente elimina una transformación del sistema.

**Resolución propuesta:** separar el snapshot estructural verdadero y su diferencia de los metadatos/evidencia de observación. Preservar el historial de §63.7, pero declarar que la inclusión de ΔValidity allí queda supersedida para la definición causal de ΔT_acc*. La validez semántica/operativa de una transformación sí pertenece a sus condiciones estructurales; la validez de la evidencia usada para conocerla no.

## 2. Dos capas de snapshot

Para unidad i, frontera b, contexto c y tiempo t, se proponen dos objetos sincronizados pero no confundibles.

### 2.1 Snapshot estructural verdadero

S_T*(i,b,c,t) = (U_t*, R_t*, C_t*, X_t*)

- U_t*: identidades canónicas de transformaciones y su estado estructural de accesibilidad en el sistema-unidad-contexto.
- R_t*: relaciones tipadas/dirigidas entre transformaciones, dependencias, interfaces, composición y condiciones de conexión.
- C_t*: condiciones y configuraciones estructurales de realizabilidad: precondiciones de invocación, restricciones, autorización, recursos, dependencias y bloqueos, con alcance temporal.
- X_t*: estado/contexto del sistema que sea constitutivo de la relación de accesibilidad en el tiempo; excluye Outcome y Value como criterios definitorios.

El asterisco denota verdad estructural del DGP, no conocimiento del analizador. En un sistema real esa verdad no es directamente observable.

### 2.2 Paquete de evidencia y observación

E_T(i,b,c,t) = (Sources, Coverage, Validity_e, Provenance, Version, Timestamp, Adjudication)

Incluye fuentes, cobertura del universo y de rutas, validez/fiabilidad de evidencia, procedencia, hashes, versión del protocolo, timestamps y adjudicación. Este paquete permite al evaluador emitir T_acc,obs o estados 1/0/?; no redefine por sí mismo el estado verdadero del sistema.

**Distinción crítica:** Validity_struct (p. ej., una ruta deja de ser compatible/operativa conforme al contrato) pertenece a C_t* o R_t*; Validity_e (p. ej., un registro pierde fiabilidad o caduca como evidencia) pertenece a E_T. No usar una sola etiqueta Validity para ambos.

## 3. Definición de ΔT_acc estructural

Dados dos snapshots comparables, basal t0 y post t1:

ΔT_acc*(i; t0,t1) = Diff_G,M(S_T*(i,b,c,t0), S_T*(i,b,c,t1))

y su representación canónica se propone como:

ΔT_acc* = (ΔU*, ΔR*, ΔC*, ΔX*).

- ΔU*: transformaciones añadidas, retiradas o cuyo estado estructural de accesibilidad cambió.
- ΔR*: relaciones añadidas, retiradas o reconfiguradas, incluidas dependencias, interfaces y reglas de composición.
- ΔC*: condiciones/configuraciones estructurales cambiadas, incluidos cambios reales de autorización, recursos disponibles, dependencias, compatibilidad y bloqueos.
- ΔX*: cambios de estado/contexto que alteran realmente la relación de accesibilidad, no meros resultados posteriores.

La evidencia/cobertura no se incorpora a esta tupla causal. Su diferencia se informa en paralelo:

ΔE_T = Diff_E(E_T(t0), E_T(t1))

ΔE_T = (ΔSources, ΔCoverage, ΔValidity_e, ΔProvenance, ΔVersion, ΔAdjudication).

Un cambio en ΔE_T puede modificar la confianza o clasificación observada sin que cambie ΔT_acc*. A la inversa, puede existir cambio estructural real sin evidencia suficiente para clasificarlo; el analizador emitirá ?.

## 4. Identidad, versiones y correspondencia entre snapshots

No se calcula un diff antes de fijar la correspondencia.

Cada objeto/relación requiere:
1. ID canónico persistente;
2. tipo/semántica de transformación;
3. versión de especificación y versión de implementación/configuración;
4. frontera y unidad/contexto;
5. regla de equivalencia/correspondencia entre versiones;
6. fecha de vigencia y procedencia.

Se distinguen tres casos:

| Caso | Regla |
|---|---|
| Misma identidad semántica, nueva versión de implementación | Mantener ID si el contrato funcional y las condiciones de identidad permanecen; registrar versión y cambios estructurales/operativos pertinentes. |
| Nueva identidad semántica o cambio de función | Registrar baja de identidad previa y alta de nueva identidad; no tratarlo como simple actualización. |
| Correspondencia no decidible | Match=?; el diff correspondiente queda indeterminado y no se fuerza equivalencia. |

Diff_G,M solo se admite si frontera, granularidad G, catálogo y mapeo M están preespecificados y son compatibles. Si cambia la granularidad o frontera sin transformación explícita a una representación común, no se calcula ΔT_acc como si ambos snapshots fueran comparables.

Un cambio de hash aislado no demuestra por sí solo cambio de identidad semántica; sí exige registrar versión/procedencia y verificar si afecta compatibilidad, integridad o condiciones estructurales.

## 5. Relación exacta entre C_dep, A_f*, D_f* y ΔT_acc*

Se preservan cuatro niveles:

1. C_dep*: éxito de la conjunción técnica de una ruta focal inventariada.
2. A_f*(i,t): juicio verdadero sobre accesibilidad de la identidad τ2 en el sistema-unidad-contexto-tiempo, derivado de todos los predicados estructurales del §67.3.
3. D_f*(i)=I(A_f*(i,t0)=0 AND A_f*(i,t1)=1): indicador de apertura focal basal→post.
4. ΔT_acc*: diferencia estructural completa del espacio de transformaciones accesibles.

Consecuencias:
- C_dep*=1 no implica A_f*=1 si falla otro predicado o bloqueo.
- C_dep*=0 no implica A_f*=0 si existe otra ruta válida para la misma τ2.
- D_f*=1 implica un cambio focal de estado de τ2 bajo snapshots comparables, pero no resume cambios no focales.
- ΔT_acc*≠0 puede ocurrir con D_f*=0 por cambios en otras transformaciones, relaciones o condiciones.
- D_f*=0 no implica ΔT_acc*=0.
- ΔE_T≠0 no implica ΔT_acc*≠0.
- ΔT_acc*≠0 puede coexistir con ΔE_T=0, aunque la clasificación observada sea incierta.

La proyección focal h_f(ΔT_acc*)=D_f* es una función derivada bajo identidad, granularidad, contexto y correspondencia establecidos; no es una igualdad de objetos ni una sustitución del espacio completo por un indicador binario.

## 6. Estados de verdad, observación e indeterminación

La verdad del DGP para cada predicado estructural se conserva como 0/1. El analizador produce estados observados 1/0/? según regla versionada y evidencia disponible.

| Situación | ΔT_acc* (truth) | ΔE_T | ΔT_acc,obs | Dictamen |
|---|---|---|---|---|
| Se añade realmente una relación accesible; evidencia adecuada | Cambio | Puede cambiar | Cambio clasificado | Cambio estructural identificado |
| La cobertura mejora y descubre una ruta preexistente | Sin cambio | Cambio | Puede aparentar aumento si no se controla baseline | Cambio epistémico; no atribuir creación |
| Se pierde una fuente, sistema intacto | Sin cambio | Cambio | ? o cobertura reducida | No inferir pérdida de accesibilidad |
| Se elimina realmente una dependencia requerida | Cambio estructural | Puede no cambiar inicialmente | 0 o ? según evidencia | Posible pérdida de accesibilidad |
| Cambia versión y no existe correspondencia fiable | No adjudicable bajo diff actual | Cambio de versión/procedencia | ? | No comparar hasta resolver mapping |
| Cambia solo la valoración de Outcome/Value | Sin cambio definicional por ese hecho | Puede no cambiar | Sin cambio estructural esperado | No circularidad |

La observación de un cambio requiere evidencia de los snapshots antes y después, no solo un aumento del número de registros disponibles.

## 7. Contrato de medición y no filtración

- El generador mantiene S_T*, ΔT_acc*, A_f*, D_f* y sus potenciales ocultos.
- El analizador recibe snapshots observables y E_T, nunca truth ni parámetros del DGP.
- El analizador devuelve A_f,obs, T_acc,obs, ΔT_acc,obs, correspondencias y estados 1/0/?.
- El evaluador independiente compara resultados del analizador con truth después de congelar su salida.
- Los errores se estiman por objeto, relación, componente, brazo, tiempo, versión y escenario; si no se identifican, se informan límites/sensibilidad.
- La cobertura de rutas alternativas se registra por separado de la ausencia estructural de rutas.
- Ninguna etiqueta de Outcome, Value, selección o ejecución se usa para definir snapshots o ΔT_acc.

## 8. Crosswalk y supersesión documental

| Fuente histórica | Formulación | Reconciliación propuesta |
|---|---|---|
| Maestro §43.1 | Cadena A_f* → ΔT_acc | Se mantiene como relación focal→cambio completo, sin equivalencia automática. |
| Maestro §58.1 | T_acc como snapshot y ΔT_acc como diferencia estructurada | Se mantiene; se precisan dos capas estructural/evidencia. |
| Maestro §63.7 | ΔT_acc*=(ΔU,ΔR,ΔC,ΔValidity,ΔState) | ΔValidity_e se mueve a ΔE_T; el cambio de validez estructural permanece en ΔC*/ΔR*. |
| Maestro §67.3/67.6 | VALID epistémico, no parte de truth | Se adopta como regla de precedencia conceptual. |
| Maestro §70 | C_dep, A_f, D_f separados | Se conserva y complementa. |

Esta reconciliación no borra el texto histórico de §63.7. La expresión anterior queda **supersedida para la definición causal**; la nueva especificación es ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), con ΔE_T como registro epistémico paralelo.

## 9. Matriz de contratos propuestos

| ID | Caso adversarial | Resultado exigido |
|---|---|---|
| SNAP-01 | Mejora cobertura, sistema inalterado | ΔE_T≠0; ΔT_acc*=0; no atribuir creación |
| SNAP-02 | Pérdida de evidencia, sistema inalterado | ΔE_T≠0; ΔT_acc*=0; observación puede ser ? |
| SNAP-03 | Se añade relación requerida | ΔR*≠0; recalcular A_f* y accesibilidad afectada |
| SNAP-04 | Se elimina dependencia requerida | ΔR*/ΔC* reflejan pérdida; A_f* puede pasar 1→0 |
| SNAP-05 | Cambia hash, identidad semántica igual | No crear identidad nueva automáticamente; auditar integridad/compatibilidad |
| SNAP-06 | Cambia función/semántica | Registrar baja y alta de identidad |
| SNAP-07 | Mapping entre versiones no resuelto | Match=?; diff no adjudicable |
| SNAP-08 | Cambia T_acc no focal y τ2 no cambia | ΔT_acc*≠0; D_f*=0 |
| SNAP-09 | Se abre τ2 sin otras transformaciones | D_f*=1; ΔT_acc* contiene el cambio focal |
| SNAP-10 | Cambia Value/Outcome sin cambio estructural | ΔT_acc*=0 por ese hecho; impedir circularidad |
| SNAP-11 | A_f* verdadero cambia, pero evidencia no lo detecta | Truth cambia; ΔT_acc,obs=?/error, no filtrar truth |
| SNAP-12 | Evidencia revela ruta que ya existía en baseline | Corregir clasificación observada basal mediante adjudicación; no fechar la creación en t1 |
| SNAP-13 | Granularidad/frontera no comparable | Rechazar diff o exigir transformación M documentada |
| SNAP-14 | Cambio de autorización/recursos inducido por B | Registrar en ΔC* y como vía colateral/mediador potencial |
| SNAP-15 | App_f cambia por S0, sin cambio de accesibilidad | No codificar como ΔT_acc* si el espacio accesible no cambia |

Estos son contratos de diseño; aún no hay fixtures ejecutables ni pruebas realizadas.

## 10. Decisiones y pendientes

Se propone:
1. separar snapshot estructural y paquete de evidencia;
2. retirar ΔValidity_e de la tupla causal ΔT_acc* y mantenerlo en ΔE_T;
3. mantener cambios de validez estructural en ΔC*/ΔR*;
4. usar correspondencia explícita de identidad/versiones antes de diff;
5. separar ΔT_acc verdadero, observado y cambio de evidencia;
6. conservar la función focal h_f como proyección, no identidad.

Pendientes para cierre:
- aprobar formalmente esta separación y propagarla globalmente;
- fijar catálogo, G, frontera y esquema de IDs/versiones;
- definir reglas de diff y mapping por clase de transformación;
- completar verdad oculta/observación por U/R/C/X;
- diseñar fixtures ejecutables, oráculos y tolerancias;
- validar error diferencial y cobertura;
- auditar relación con Reach_possible, S5-F/S5-C, Value y q;
- revisión independiente y decisión formal.

No se cierra AUD-001/004/005/007, XAUD-003/004/006 ni XSYNC-138-03/06. No hay freeze, implementación, simulación ni ejecución.


## 6. Roster de campos del microdominio y regla X/C/E_T

El roster documental consolidado está en el maestro C10-S §232. Para el diff de snapshots, cada subcampo de U_t*/R_t*/C_t*/X_t* se registra con ID canónico, versión, unidad/frontera, vigencia, regla de matching, valor basal/post, event_id y efecto estructural. La fuente de observación/cobertura/validez/provenance/adjudicación se registra separadamente en E_T.

X_t* solo contiene estado/contexto efectivo constitutivo de accesibilidad; reglas, ACL, cuotas, restricciones y bloqueos pertenecen a C_t*; endpoints/dependencias a R_t*; transformaciones a U_t*; logs/hash/cobertura a E_T. Los campos mixtos se descomponen o quedan UNKNOWN. El roster real y su comparabilidad siguen OPEN.
