# C10-S — Auditoría integral de reconciliación causal-transformacional

**Versión:** borrador 001  
**Fecha:** 2026-11-04  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116  
**Estado:** AUDITORÍA DOCUMENTAL / PROPUESTA DE ARMONIZACIÓN — NO APROBADA, NO IMPLEMENTADA, NO EJECUTADA.  
**Fuente canónica:** GitHub. Se han contrastado README.md y 00_GOVERNANCE/README.md en main, C10-D1, documento maestro C10-S, contrato DGP temporal/roles, reconciliación de estimandos, Decision Log, matriz de cierre, registro de pruebas y registro de recuperación 165–183.

## 1. Dictamen

El diseño previo tenía una arquitectura reconocible, pero no una especificación única plenamente reconciliada. La causa no era ausencia de bloques: eran formulaciones de distinta fecha y nivel de formalización que coexistían sin una regla explícita de precedencia. Esta auditoría propone una especificación de referencia común y registra qué puede armonizarse documentalmente y qué exige decisión científica o revisión independiente.

**Resultado:** se puede establecer una arquitectura candidata internamente coherente para C10-S/S4-R sin borrar las formulaciones históricas. No procede declarar el diseño aprobado, congelado ni listo para ejecución. La coherencia documental propuesta no sustituye la aceptación científica de las decisiones abiertas.

## 2. Regla de precedencia y alcance

1. C10-D1 gobierna la pregunta causal general, la interpretación de `θ_A(q)`, los requisitos de identificación y los límites de atribución.
2. C10-S define el experimento sintético, sus mecanismos generadores, escenarios y contratos de aceptación.
3. El contrato DGP temporal/roles es la formulación operativa candidata de la cadena generativa; no puede redefinir el estimando C10-D1.
4. El documento de reconciliación fija la correspondencia propuesta entre C10-D1 y S4-R.
5. La sección 53 del documento maestro será el punto integrado de lectura de esta auditoría. Las secciones históricas anteriores permanecen para trazabilidad; cuando una formulación preliminar difiera, se identifica como antecedente sustituido para la especificación candidata, no se elimina.
6. Ninguna propuesta de esta auditoría se convierte en decisión aceptada por el hecho de persistirla.

## 3. Especificación candidata reconciliada

### 3.1 Pregunta general y experimento focal

- Pregunta científica general: `θ_A(q)=E[V^{q,g1}]-E[V^{q,g0}]`, bajo una población, horizonte, regla de Value, versiones de política y régimen común factible explícitos.
- S4-R no identifica por sí solo ese estimando general: focaliza la apertura de `τ2` mediante una dependencia técnica concreta.
- S4-R tiene como estimando primario de asignación `ITT_Z`, efecto de asignar las políticas de provisión concretas en la población elegible.
- La atribución focal secundaria es `LATE_f`, solo si los supuestos IV se sostienen. No equivale a ATE, ATT, `θ_A(q)` general ni efecto de todo `ΔT_acc`.
- Si la política tiene vías directas/colaterales, `ITT_Z` sigue siendo efecto de política/paquete; no se etiqueta como efecto aislado de accesibilidad.

### 3.2 Población y apertura

- `P*_{τ2}`: elegibilidad definida exclusivamente con información basal/preasignación y condiciones constitutivas compatibles con ambas políticas.
- Para el estimando de apertura basal→post, exigir `A_{f,base}*=0` antes de Z. La población de apertura no se define usando cumplimiento, accesibilidad post, selección, ejecución, Outcome o Value.
- `P*_F`: subpoblación basal sin alternativa funcional substituible según una regla `F*` explícita. Es análisis de alcance/heterogeneidad y no filtro automático de `P*_{τ2}`.
- Los casos basales indeterminados no se convierten en elegibles ni inelegibles por defecto: se conserva estado indeterminado y se define análisis de sensibilidad.

### 3.3 Registro histórico de la recomendación D1/D2 — NO OPERATIVO

**Estado:** HISTÓRICO / SUPERSEDED EN PRECEDENCIA POR DEC-C10-066/067. Esta sección conserva el contenido de la recuperación 165–183 y la calibración exploratoria de D1/D2; no es una instrucción vigente para seleccionar ni parametrizar el escenario primario.

La fuente recuperada recomendaba D1 como escenario principal condicionado a justificar la provisión ordinaria del control, y D2 como contraste sin provisión ordinaria. Los valores exploratorios asociados eran: D1, C_dep,base=0, p_dep,0=.20, p_dep,1=.80 y primera etapa objetivo .60; D2, C_dep,base=0, p_dep,0=0, p_dep,1=.80 y primera etapa objetivo .80. Son objetivos históricos de DGP, no resultados ni parámetros confirmatorios validados.

**Precedencia vigente:** DEC-C10-066 establece D2 como escenario primario candidato y D1 como secundario. DEC-C10-067 define las políticas materiales D2: B_g0^D2 no programa/inicia intento focal; B_g1^D2 programa un intento estandarizado de provisión técnica focal. C_auth,base=1 permanece común, satisfecha antes de Z e invariante frente a B. La antigua recomendación D1-principal queda supersedida solo en la precedencia; D1 y su mecanismo incremental se conservan como escenario secundario.

La selección de D2 no valida p=.80, no demuestra ausencia de provisión de fondo, no cierra la correspondencia B→g^Af ni identifica por sí sola accesibilidad, LATE o θ_A(q).### 3.4 Mecanismo generativo único

La cadena canónica candidata es:

`Z → B_g → W_attempt → S_install → (C_install,C_integrity,C_compat,C_oper) → C_dep,post → A_f,post* → ΔT_acc → Reach_H → Π_candidate → K/Consider → Sel → Start → Exec → O → V`

Con:
- `Z`: asignación aleatoria.
- `B_g`: política/version de provisión asignada y recibida, registradas por separado.
- `W_attempt`: intento; no es éxito.
- `S_install`: éxito técnico condicional; no es todavía verificación completa.
- `C_dep,post=C_install∧C_integrity∧C_compat∧C_oper`: estado técnico compuesto, cada componente con estado epistémico, fuente y timestamp.
- `A_f,post*`: accesibilidad focal verdadera, derivada de `C_dep,post` y del resto de condiciones focales.
- `D_f=I(A_f,base*=0 ∧ A_f,post*=1)`: apertura basal→post usada para la primera etapa IV en la población de apertura.
- `ΔT_acc^*=(ΔU^*,ΔR^*,ΔC^*,ΔX^*)`: cambio estructural completo del espacio accesible; `ΔE_T` registra en paralelo el cambio de evidencia/observabilidad y no forma parte de `ΔT_acc^*`. `A_f^*` es una proyección focal, no un sustituto del vector.
- Aplicabilidad, Reach, conocimiento, selección, inicio, ejecución parcial/completa, Outcome y Value permanecen como estados/constructos separados.

El generador puede parametrizar intentos y éxitos con `ω_z` y `s_z(·)`, pero debe calibrar las probabilidades finales verificadas. Para el escenario limpio con las demás condiciones focales satisfechas, `P(A_f,post*=1|Z=z,P*_{τ2})=p^dep_z`. Si las condiciones restantes varían, las probabilidades de `C_dep` y de `A_f` no se igualan: se calcula la segunda a partir de todos los predicados. No se asume independencia entre latentes sin especificación. Una variable latente común puede implementar monotonicidad, pero la accesibilidad nunca se asigna directamente a partir de Z.

### 3.5 Régimen común q y políticas g

- `q*` define una distribución/regla común, preespecificada y factible sobre las condiciones e historias no manipuladas por la política, incluyendo las variables basales y temporales pertinentes.
- Las condiciones constitutivas `C_c` no se tratan como variables libremente aleatorizadas: delimitan factibilidad y elegibilidad. Deben ser compatibles con ambas políticas en la población primaria.
- `B_g0/B_g1` son políticas implementables que difieren en la provisión focal según D1 o D2. El componente manipulado por g no se fija simultáneamente como parte de q.
- El soporte/positividad se comprueba por estrato e historia. Si una política no es factible, no se fuerza su asignación; se restringe ex ante la población con justificación o se declara no identificación del contraste definido.
- `q*` no es la regla de Value. Beneficiario, criterio, escala, dimensiones y horizonte de Value se fijan independientemente y son comunes entre brazos.

### 3.6 Estimandos y reglas de salida

1. `ITT_Z=E[V|Z=1]-E[V|Z=0]`: efecto de asignación, reportado por dimensión de Value y para cada Outcome preespecificado. Mantiene la población aleatorizada; no se condiciona a cumplimiento o variables postratamiento.
2. `ITT_{D_f}=E[D_f|Z=1]-E[D_f|Z=0]`: primera etapa de apertura focal.
3. `LATE_f=ITT_Z/ITT_{D_f}`: solo bajo relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, ausencia de interferencia y medición válida; inferencia robusta a instrumento débil. Primera etapa nula: no calcular Wald. Primera etapa débil: método robusto o INDETERMINATE.
4. `θ_{Af}(q*)`: contraste poblacional focal de políticas de accesibilidad. `ITT_Z` solo puede interpretarse como tal si las políticas difieren únicamente en la distribución de accesibilidad focal bajo q común, con versiones y vías alternativas controladas por diseño.
5. `θ_A(q)`: pregunta general C10-D1 sobre cambios del espacio transformacional; S4-R no la identifica por sí solo.
6. Si existen vías colaterales (coste, latencia, calidad, seguridad, información, expectativas, rutas alternativas u otras), reportar efecto de política/paquete `ψ_policy`. No atribuirlo exclusivamente a `A_f`.
7. No usar `TE-θ_A(q)` como efecto directo/residual automáticamente. La mediación requiere identificación y supuestos propios.

### 3.7 DGP aislado y adversarial

- DGP aislado: solo cambia la realizabilidad estructural focal; resto de condiciones, calidad condicional de ejecución, recursos, información, costes no inherentes, latencia, seguridad y regla Value invariantes. Exclusión es una estipulación del mundo sintético, no evidencia real.
- DGP adversarial: introduce δ, γ y/o rutas directas, cambios de alternativas, versiones, no cumplimiento, medición imperfecta, primera etapa débil/nula, interferencia y missingness. El analizador debe clasificar efecto de paquete/no identificación cuando corresponda.
- D1 y D2 son variantes de política de control dentro de la arquitectura; escenarios adversariales no se confunden con el DGP aislado ni se usan para alterar retrospectivamente el estimando.

### 3.8 Value, Outcome y medición

- Outcome operativo y Value son distintos.
- Value se conserva inicialmente como vector multidimensional; no se agrega en índice escalar sin justificar escalas, pesos, compensabilidad, beneficiario y sensibilidad.
- Medición de accesibilidad verdadera del generador, accesibilidad observada del analizador, Outcome y Value se separa por fuente, instrumento, ventana y rol.
- La verdad latente del DGP no se filtra al analizador. El evaluador independiente recibe la verdad solo para comparar el resultado.
- Ausencia, desconocido, censura, fallo técnico y cero observado son estados distintos; dictámenes de identificación separados por estimando/dimensión.

## 4. Inconsistencias reconciliadas documentalmente

| ID | Inconsistencia previa | Armonización candidata |
|---|---|---|
| R-01 | §30.2 equiparaba intento y probabilidad final | §31.4 y contrato DGP prevalecen: separar intento, éxito y verificación |
| R-02 | p0=.20 parecía incompatible con C_dep,base=0 | D1 interpreta p0 como provisión final postasignación; D2 p0=0 |
| R-03 | Reconciliación previa recomendaba p0=0 como limpio y matriz proponía D1 .20 | D1 principal condicionado + D2 contraste, según fuente 165–183; decisión de comparador pendiente |
| R-04 | Se confundían ITT_Z, θ_A(q), θ_Af(q*) y LATE_f | Jerarquía de §3.6 |
| R-05 | A_f podía leerse como todo ΔT_acc | A_f es proyección focal; ΔT_acc completo permanece vectorial |
| R-06 | q y g podían solaparse | q común sobre condiciones/historias no manipuladas; g implementa la política focal |
| R-07 | P*_F podía confundirse con población primaria | P*_τ2 primaria; P*_F subgrupo funcional basal |
| R-08 | Outcome y Value podían agregarse | Separación de constructos y Value vectorial provisional |
| R-09 | Intento/instalación/accesibilidad/aplicabilidad/ejecución colapsados | Cadena temporal y predicados distintos |
| R-10 | Fuente recuperada vs integración confundidas | DOCX y transcripción literal íntegra aún no persistidos; capítulos 52–53 son integración normalizada |

## 5. Matriz de estado residual

| Bloque | Estado tras auditoría | Qué falta para cierre |
|---|---|---|
| Pregunta C10-D1 vs S4-R | ARMONIZADO COMO PROPUESTA | Aprobación científica de jerarquía y alcance |
| D1/D2 y p0/p1 | ARMONIZADO COMO PROPUESTA | Justificar control ordinario D1 y aceptar escenario principal |
| Cadena generativa | FORMALIZADA COMO PROPUESTA | Distribución conjunta/parametrización y fixtures |
| q*/g y factibilidad | PARCIAL | Definición de población/historias, soporte por estrato y política física |
| P*_τ2/P*_F/F* | PARCIAL | Reglas operativas, equivalencia funcional, indeterminados |
| ΔT_acc/Reach/trayectorias | PARCIAL | AUD-004/005; identidad, relaciones, validez, composición y estados posibles |
| IV/exclusión/δ/γ | PARCIAL | Rangos, supuestos, escenarios y reglas de decisión |
| Value/O/medición | PARCIAL | Beneficiario, escalas, horizonte, fuentes y regla evaluativa |
| Unidad/interferencia | ABIERTO | Unidad de asignación, unidad experimental, clústeres y spillovers |
| Missingness/censura | DEFINIDO A NIVEL DE CRITERIOS | Mecanismos, cotas, fixtures y dictámenes por estimando |
| Contratos | INCOMPLETOS | Fixtures, oráculos, tolerancias, códigos y artefactos |
| XSYNC/revisión independiente | ABIERTO | Auditoría externa documentada |
| N/réplicas/precisión | ABIERTO | Dimensionamiento y justificación cuantitativa |
| Fuente 165–183 | RECUPERADA Y EXAMINADA | Persistir DOCX íntegro y transcripción literal en GitHub |
| Aprobación/freeze/ejecución | NO ALCANZADO | Decisiones y gates formales; autorización separada |

## 6. Criterios de aceptación para la siguiente revisión

1. No existe ninguna ecuación que equipare `W_attempt` con `C_dep` o `A_f*`.
2. `C_dep,base=0` se mide antes de Z; D1 p0=.20 es postasignación y D2 p0=0.
3. La probabilidad final de `A_f*` se deriva de todas las condiciones, no se copia automáticamente de `C_dep`.
4. La primera etapa se calcula sobre `D_f` en la población de apertura definida basalmente.
5. ITT, `θ_A(q)`, `θ_Af(q*)`, LATE y efecto de paquete nunca comparten etiqueta.
6. q y g tienen dominios no solapados, y ambas políticas son factibles bajo q en la población objetivo.
7. `P*_τ2` y `P*_F` usan solo información basal.
8. `A_f` no sustituye `ΔT_acc`; Reach y trayectorias no se derivan de ejecuciones observadas.
9. Outcome y Value no son circulares; ausencia no es cero.
10. El analizador no recibe verdad latente ni parámetros generadores.
11. Todos los escenarios tienen truth, expected outputs y reglas PASS/FAIL/INDETERMINATE.
12. Auditoría independiente acepta o registra límites residuales.

## 7. Conclusión y autorización

Esta auditoría resuelve las contradicciones editoriales y de precedencia identificables y ofrece una especificación candidata integrada. No resuelve por decreto las decisiones científicas pendientes. El diseño sigue **DRAFT / NO APROBADO / NO IMPLEMENTADO / NO EJECUTADO**. No se ha ejecutado simulación, código, estimación ni experimento. No se modifican main, TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims ni C09. La ejecución requiere autorización expresa separada.

**Dictamen:** arquitectura candidata reconciliada documentalmente; operacionalización, decisión científica, contratos completos y revisión independiente pendientes.


## 11. Reconciliación de precedencia del protocolo autocontenido (2026-11-05)

Las referencias de §§3.8, 5 y 7 a revisión independiente externa como condición para aceptar o cerrar el diseño quedan supersedidas para la continuidad científica actual. Prevalecen el maestro C10-S §130, Closure Control Matrix §12 y Test Contract Register §§54–55: AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT; R1/R2 no son condición de avance ni de ejecución sintética autorizada.

El evaluador independiente de la arquitectura es un rol computacional separado del analizador, con acceso a truth solo tras congelar su salida. No se afirma revisión humana independiente. La arquitectura causal y las decisiones abiertas de esta auditoría no cambian por este addendum.

## 12. Supersesión de precedencia por DEC-C10-066 (2026-11-06)

La recomendación histórica de §3.3 y las filas R-03/estado residual que dejaban D1 como principal condicionado, D2 como contraste o la selección primaria abierta quedan supersedidas únicamente en la precedencia del comparador. El estado operativo vigente es: **D2 primario candidato; D1 secundario**, conforme a DEC-C10-066.

Se mantienen las definiciones, probabilidades candidatas, distinción de intento/éxito/estado final y requisitos de legitimidad. D2 exige comprobar ausencia basal y ausencia de provisión focal de fondo; D1 requiere justificación independiente del régimen ordinario para interpretar su contraste incremental. No se validan s=.80, p0/p1 ni las primeras etapas. ITT, primeras etapas y LATE siguen siendo específicos de cada escenario.

La decisión no cierra estimandos, q*, población, soporte, vías colaterales, exclusión, medición ni identificación. No autoriza freeze, implementación, simulación ni ejecución.


## 13. Reconciliación de políticas materiales D2 — DEC-C10-067 (2026-11-06)

Se incorpora la aceptación conceptual de las políticas materiales D2 conforme a DEC-C10-067 (00_GOVERNANCE/SIP/DEC-C10-067_D2_MATERIAL_POLICY_CONTRACT_ACCEPTANCE.md, blob 2c3e1dbff4c83ded910a1fd8ca0a47a602df2213). Esta reconciliación es documental y no modifica los parámetros ni el estado de autorización.

| Dimensión | Control B_g0^D2 | Tratamiento B_g1^D2 | Estado |
|---|---|---|---|
| Política de provisión | Mantener configuración basal; no programar ni iniciar intento focal para τ2 | Programar intento estandarizado de despliegue/configuración de dependencia focal para τ2 | Definición conceptual aceptada |
| Autorización | Mantener autorización normativa basal | No modificar autorización normativa basal | Invariante candidata; verificación pendiente |
| Eventos | Registrar cualquier provisión focal de fondo/crossover; no inferir ausencia efectiva desde no-programación | Registrar actor, inicio, recepción, finalización, versión recibida y desviaciones | Contrato temporal pendiente de operacionalizar |
| Estado técnico | Medir por separado cualquier provisión efectiva | Verificar instalación, integridad, compatibilidad y operatividad | C_dep* no se infiere del intento |
| Accesibilidad/apertura | Determinar predicados basales y post por separado | Determinar A_f*, D_f* y ΔT_acc* mediante condiciones completas | No se transfieren probabilidades técnicas a accesibilidad |

La cadena de eventos que debe preservar el DGP es:

Z_i → B_gZ_i^D2 → W_programmed,i → W_attempt,i → S_install,i → C_dep,i* → A_f,i* → D_f,i*.

La programación, el intento efectivo, la recepción, el éxito de cada componente técnico y la apertura de accesibilidad son variables/eventos distintos. El control solo representa ausencia de intento focal programado por política; la ausencia efectiva de provisión focal de fondo y de rutas técnicas equivalentes debe verificarse mediante cobertura/evidencia independiente.

Las condiciones comunes candidatas incluyen C_auth,base=1, elegibilidad y versionado de τ2, recursos no focales, capacidad, información técnica basal y protocolo común de medición/adjudicación. La invariancia efectiva aún no está demostrada. Cambios inducidos por la provisión en recursos, permisos, costes, latencia, calidad, seguridad, información, incentivos o alternativas deben registrarse como vías colaterales/cointervenciones; no pueden absorberse dentro de C_dep*. En presencia de tales vías, el ITT identifica el efecto de la política/paquete bajo supuestos de diseño, no automáticamente un efecto puro de accesibilidad.

El registro contractual auxiliar es Test Contract Register §56 (D2POL-01…10). Sus condiciones son criterios documentales; evidencias, fixtures, oráculos y validación ejecutable siguen pendientes. Se mantienen abiertos actor/rol, artefacto y versión/hash, recepción, ventanas temporales, reintentos/fallos parciales/rollback, detección de provisión de fondo, evidencia independiente de componentes y cobertura de rutas alternativas.

DEC-C10-067 no valida s=0.80, probabilidades conjuntas, cumplimiento, parámetros de Value, potencia o tamaño muestral; tampoco cierra estimandos, población/soporte, unidad/interferencia, correspondencia B↔g, exclusión ni identificación. D2 continúa como primario candidato y D1 como secundario por DEC-C10-066. **No autoriza freeze, implementación, simulación ni ejecución científica.**
