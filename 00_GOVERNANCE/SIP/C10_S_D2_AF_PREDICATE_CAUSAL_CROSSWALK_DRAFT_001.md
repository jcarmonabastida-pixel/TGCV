# C10-S — Crosswalk causal de predicados de accesibilidad focal A_f*
**ID:** C10-S-AF-XWALK-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-06
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT · propuesta de reconciliación documental, no aprobación ni freeze.
**Rama:** `research/c10-s-consolidation-draft`

## 0. Regla de lectura anti-regresión

Este crosswalk es la referencia correctiva para la correspondencia entre predicados históricos y la fórmula candidata de accesibilidad focal. Debe leerse junto con el control vinculante §0.5 y §213 del maestro C10-S y con DEC-C10-066/067.

**Corrección que no puede revertirse por recuperación de texto antiguo:**
- `C_auth,base=1` permanece como condición basal común, satisfecha antes de Z e invariante frente a B en el DGP aislado D2.
- `C_auth_base` es la denominación usada en las fichas y se corresponde con `AUTH_f*`; no son dos factores independientes.
- La fórmula candidata de referencia es la de maestro §67.3, no la fórmula histórica de §30.1.
- AUD-001/002 proponía una intervención focal sobre autorización. Esa intervención antigua no es la política primaria D2 y no invalida ni elimina la autorización basal. Solo puede recuperarse como escenario alternativo/adversarial de política de autorización, con interpretación causal propia.
- D2 es primario candidato y D1 secundario; ello no identifica automáticamente el efecto causal de accesibilidad.

Si una fuente dependiente contradice estos puntos, se registra discrepancia y se detiene la inferencia hasta reconciliarla. No se elige la formulación más antigua, más detallada o encontrada primero.

## 1. Alcance y precedencia

Este crosswalk reconcilia la fórmula candidata depurada del maestro §67.3 con DGP §§26, 39–41, 59.1–59.3, 67.3–67.7; Path Predicate Temporal Evidence Matrix §§13.1–13.5; matriz de cobertura U_G §§4–9; contrato de snapshots/delta; y auditoría de medición MEAS-001.

**Corrección expresa:** MEAS-001 describió inicialmente la fórmula histórica de §30.1/§3.x como si fuera la composición vigente. Esa lectura es incorrecta por no respetar la precedencia interna. La ecuación intermedia de maestro §59.3 también queda ahora identificada como antecedente supersedido, no como fuente operativa. La composición candidata vigente de referencia está en maestro §67.3 y en este crosswalk. Las fórmulas de §§30.1 y 59.3 se conservan solo para trazabilidad histórica. Esta corrección no convierte §67.3 en definición universal ni en freeze.

Fórmula de referencia del maestro §67.3:

`A_f^* = I(ID_f^* AND REL_f^* AND COND_f^* AND AUTH_f^* AND RES_f^* AND DEP_f^* AND NOT BLOCK_f^*)`

## 2. Crosswalk exhaustivo de términos recuperados

| Término/familia histórica o actual | Correspondencia en fórmula §67.3 | Clase causal/epistémica | Dictamen de inclusión / no duplicidad | Estado |
|---|---|---|---|---|
| `ID_f*`, ID_τ2, identidad/tipo/versión | `ID_f*) | Constitutivo de identidad del objeto focal | Integrar identidad semántica τ2, tipo, versión y correspondencia con contrato. Hash es evidencia/procedencia; un hash distinto no demuestra por sí solo identidad semántica distinta. | Definición conceptual; contrato de matching/versión abierto |
| `REL_f*`, relaciones/interfaces requeridas | `REL_f*) | Constitutivo relacional | Relaciones, interfaces y dependencias relacionales necesarias para invocar/componer τ2. No absorber sin justificación en identidad ni duplicar las dependencias técnicas de una ruta; explicitar frontera entre relación requerida y ruta completa. | Definido conceptualmente; inventario material NONE |
| `COND_f*), condiciones constitutivas de realizabilidad | `COND_f*) | Constitutivo estructural | Solo condiciones necesarias de realizabilidad independientes de precondiciones particulares de S0. No incluir automáticamente App_f ni estados intermedios. | Definición conceptual; catálogo por τ2 abierto |
| `C_auth_base`, autorización funcional | `AUTH_f*) | Constitutivo de acceso/autorización | Permiso normativo funcional vigente para unidad/actor/objeto/ventana. En D2 se postula común, satisfecho antes de Z e invariante frente a B. ACL/credenciales/endpoint de provisión son permisos técnicos distintos y pueden formar parte de B/C_dep; no ampliar autorización funcional. | Ficha propuesta; fuente normativa, titular, alcance y vigencia abiertos |
| `C_resource`, disponibilidad basal no focal | `RES_f*), solo a través de `R_access*) | Constitutivo si es disponibilidad ex ante necesaria; colateral/interferencia si B desplaza recursos | No crear un multiplicador autónomo paralelo. Incluir solo disponibilidad asignada, suficiente, persistente y no duplicada, por unidad y ventana. Recursos consumidos por B se registran aparte; consumo de ejecución y carga concreta no se retrotraen a acceso. | Crosswalk conceptual desarrollado; inventario y suficiencia material abiertos |
| `C_capacity`, capacidad instalada/disponible/reservada | `RES_f*) vía `R_access*) solo cuando habilita oferta ex ante y no está duplicada; en otro caso fuera de A_f* | Constitutivo condicional / aplicabilidad / ejecución / colateral | Capacidad focal que B provisiona queda en C_dep*. Capacidad no focal disponible para ofrecer τ2 puede integrar RES/R_access si es necesaria y distinta. Carga S0, concurrencia puntual, consumo y margen de una ejecución pertenecen a App/ejecución/rendimiento. No crear C_capacity como factor independiente adicional. | Crosswalk conceptual; dimensión, umbral, unidad, ventana y pools abiertos |
| `C_info`, información técnica del sistema | No es predicado autónomo. Solo podría mapearse a `COND_f*), `REL_f*), `DEP_f*) o `RES_f*) si la función material concreta pertenece inequívocamente a uno de ellos y no duplica contenido | Constitutivo condicional si es imprescindible; de otro modo no accesibilidad | Información técnica integrada imprescindible puede estar ya en configuración/dependencia; manuales, avisos y formación → K/consideración (mediador/colateral); observabilidad del evaluador → E_T (epistémico). Nunca crear C_info autónomo por etiqueta. | Clasificación conceptual desarrollada; inventario de datos técnicos imprescindibles abierto |
| `C_domain`, compatibilidad de dominio/tipo de objeto | `COND_f*` o identidad/tipo `ID_f*`, según el objeto exacto; la fórmula intermedia histórica de §59.3 lo denominaba `D_support*` | Constitutivo de soporte del dominio/tipo | Compatibilidad del tipo de objeto/dominio con τ2 puede ser condición estructural; precondiciones del estado S0 son `App_f*`. No mantener `D_support*` como factor adicional separado si ya está dentro de COND/ID; preservar trazabilidad del nombre histórico. | Candidata; mapping final entre D_support, COND e ID requiere fijación semántica |
| `C_dep*), conjunción técnica | `DEP_f*) en DGP primario de ruta única; generalizado como existencia de ≥1 ruta válida | Constitutivo de ruta/dependencia técnica | `C_dep*=C_install∧C_integrity∧C_compat∧C_oper`. En ruta única postulada, DEP=C_dep. En contrato general, C_dep=0 no implica A_f=0 si existe ruta alternativa válida para la misma τ2. No sustituye REL, AUTH, RES, COND o ausencia de BLOCK. | Fórmula técnica definida; distribución conjunta, rutas y verdad material abiertos |
| `C_install`, `C_integrity`, `C_compat`, `C_oper) | Componentes de `C_dep*) dentro de `DEP_f*) | Constitutivos técnicos de la ruta focal | Mantener los cuatro componentes separados para medición y fallos parciales; no tratarlos como cuatro factores paralelos a DEP en A_f*. Intento/instalación declarada/operación de τ2 no son equivalentes. | Definidos en contrato; valores y distribución conjunta no validados |
| `C_other) | Ninguna | Residual inadmisible | Retirado como comodín; descomponer en predicados nombrados y mapear a una sola función primaria. No añadirlo a fórmula depurada. | Exclusión documental explícita |
| `BLOCK_f*), bloqueo efectivo | `NOT BLOCK_f*) | Constitutivo inhibidor | Requiere bloqueo real y efectivo bajo el contrato; distinguir bloqueo de la ruta focal de bloqueo de todas las rutas admisibles. Evidencia incompleta no prueba bloqueo. | Definición conceptual; catálogo/inventario abierto |
| `VALID_f), cobertura, calidad, E_T, observabilidad | Fuera de la fórmula de truth; afecta clasificación observada `A_f^{obs}) | Epistémico/medición | No hacer que la falta de evidencia cambie la verdad estructural. Cobertura por unidad/snapshot/ruta/predicado/fuente/versión; evidencia de ausencia distinta de ausencia de evidencia. | Principio definido; validación y medición abiertas |
| `App_f*), precondiciones de S0, estado intermedio | Fuera de A_f* | Aplicabilidad | Determina si τ2 puede aplicarse desde un estado concreto una vez disponible. No incluir en accesibilidad estructural por defecto. | Separación conceptual definida; catálogo por estado abierto |
| `K), conocimiento/consideración, formación, avisos | Fuera de A_f* | Mediador/colateral posterior | Medir después de congelar accesibilidad. B→K→consideración/selección/ejecución es una posible vía de política, no accesibilidad. | Separación conceptual definida; invariancia de comunicación por verificar |
| Selección, inicio, ejecución, Outcome, Value | Fuera de A_f* | Eventos/resultados downstream | No usar para reconstruir retrospectivamente accesibilidad ni elegibilidad basal. | Separación definida; medición y causalidad downstream abiertas |
| Alternativas A1/A2/F2, rutas compartidas/externas/desconocidas | Afectan `DEP_f*) general, `REL_f*), `RES_f*) o `BLOCK_f*) según estructura real; no son nuevos factores por nombre | Constitutivo si ruta válida; colateral/interferencia si B las degrada | Deben inventariarse rutas equivalentes para τ2 y dependencias/consumidores compartidos. No declarar ruta única o ausencia de alternativas sin cobertura exhaustiva. | Inventario real NONE; Runknown permanece ? |
| `B-M01…15) | No son predicados de A_f*; son dominios/componentes de intervención/inspección | Provisión o superficies de vías colaterales/medición | Mapear cada componente real a los predicados ya definidos y a rutas U_G; no crear nodos/aristas ni afirmar existencia por crosswalk. B-M13 oráculo y B-M14 alternativas son superficies de inspección, no modificaciones funcionales permitidas. B-M15 reversibilidad es evento/proceso. | Manifiesto/crosswalk documental; componentes materiales no inventariados |

## 3. Resolución del problema de duplicidad

1. La fórmula candidata de referencia sigue siendo §67.3. No se sustituye por la lista histórica de §30.1 ni por la formulación de §26.
2. `C_dep*` se representa una sola vez, dentro de `DEP_f*) cuando la ruta única del DGP primario esté estipulada. Si se mantiene el contrato general de rutas, DEP representa al menos una ruta admisible válida.
3. `C_auth_base` se corresponde con `AUTH_f*); no añadir ambos como factores independientes.
4. `C_resource` y `C_capacity` son descriptores que pueden alimentar `RES_f*) / `R_access*) solo si prueban disponibilidad ex ante necesaria, en el nivel/ventana correctos y sin duplicidad con C_dep. No se agregan por separado.
5. `C_info` no se añade como factor. Se clasifica por contenido material: técnica imprescindible integrada en una condición ya existente; K/comunicaciones como vía posterior; E_T como medición.
6. `C_domain)/`D_support*) debe asignarse a ID/tipo o COND según su semántica, sin crear un octavo factor adicional.
7. `C_other) no tiene correspondencia admisible.
8. `VALID_f)/cobertura nunca se añade a truth de A_f*.
9. App_f, K, selección, ejecución, Outcome y Value quedan fuera de A_f*.
10. REL y DEP permanecen distintos: relaciones/interfaces requeridas no equivalen automáticamente a la existencia de una ruta técnica completa.

## 4. Consecuencia para la auditoría MEAS-001

El hallazgo MEAS-01 original se **corrige**:
- Incorrecto: afirmar que la composición vigente incluye C_info, C_resource, C_capacity, C_domain y C_other como factores autónomos.
- Correcto: la fórmula candidata depurada ya está expresada en §67.3; C_info autónomo está excluido; C_resource/C_capacity se canalizan condicionalmente a RES_f*/R_access*; C_domain/D_support se reconcilia con ID/tipo o COND; C_other es residual inadmisible.
- Lo que permanece abierto no es la existencia de una fórmula depurada, sino la operacionalización sin duplicidad de RES, el mapping semántico D_support↔ID/COND, la especificación material de REL/COND/BLOCK y la correspondencia de la ruta única frente al inventario de alternativas.

Por tanto, MEAS-G1 pasa de “composición sin reconciliar” a **PARTIAL — fórmula candidata identificada; mappings y operacionalización sin duplicidad pendientes**. No se declara cerrado.

## 5. Límite de este crosswalk

Este documento no aprueba ni congela la fórmula; no convierte las fichas DRAFT en decisiones; no afirma invariancia empírica; no inventaría componentes B-M ni rutas U_G; no cierra UG-SCH-10, PROV-05/06/09, MD-C1/MD-C4, XSYNC ni gates IV. La verdad estructural, la clasificación observada y la evidencia siguen separadas. `LATE_f) continúa bloqueado.

## 6. Siguiente paso

Reconciliar la regla trivalente de agregación para:
- conjunción de predicados constitutivos (ID/REL/COND/AUTH/RES/DEP/¬BLOCK);
- existencia de al menos una ruta válida dentro de DEP, con rutas alternativas/compartidas/externas/unknown;
- conflictos de evidencia, cobertura parcial, snapshots no comparables y matching unresolved;
- derivación basal→post de `D_f^{obs}) sin convertir ? en 0;
- diferencia entre truth DGP y salida del analizador.

La regla deberá conservar los casos ya especificados en DGP §§67.5–67.6 y matriz de cobertura; no se autoriza algoritmo/implementación/ejecución.


## 7. Regla trivalente integrada — A_f*, DEP_f* y D_f*

Esta sección operacionaliza lógicamente la agenda del §6; no aprueba ni congela la fórmula candidata.

### 7.1. Conjunción de predicados de A_f*

Para ID/REL/COND/AUTH/RES/DEP/¬BLOCK con estados {1,0,?}: A_f*=1 solo si todos son 1; A_f*=0 si al menos uno es 0 adjudicado; A_f*=? si ninguno es 0 concluyente y al menos uno permanece ?. Evidencia ausente, cobertura parcial, conflicto no resuelto o matching ambiguo no equivalen a 0. Truth_DGP y estado observado se mantienen separados.

### 7.2. Existencia de ruta en DEP_f*

Cada ruta se evalúa con la misma lógica conjuntiva. DEP_f*=1 si al menos una ruta admisible es 1. DEP_f*=0 solo si el inventario relevante es exhaustivo y todas las rutas son 0. DEP_f*=? si no hay ruta válida demostrada y persiste incertidumbre sobre rutas, cobertura o requisitos. Una ruta desconocida no invalida una ruta ya demostrada válida; tampoco la ausencia de rutas observadas demuestra ausencia estructural. Las rutas compartidas/externas/alternativas no reciben estado por su etiqueta, sino por sus predicados.

### 7.3. Apertura focal basal→post

Se conserva D_f*=I(A_f,base*=0 ∧ A_f,post*=1), con regla derivada: D_f*=1 si basal=0 y post=1; D_f*=0 si basal=1 o post=0; D_f*=? en los restantes casos no concluyentes. Se exige matching comparable de unidad, τ2, frontera, versión y snapshots. D_f* no se infiere de asignación, provisión, intento o instalación.

### 7.4. Límite de ΔT_acc* y ΔE_T

ΔT_acc*=Diff(S_T*(t0),S_T*(t1))=(ΔU*,ΔR*,ΔC*,ΔX*) solo para snapshots estructurales comparables. Los campos no comparables, ambiguos o mixtos sin descomposición quedan UNKNOWN/? y no se imputan como cero. ΔX* no se asigna automáticamente a ΔC* o ΔR*. ΔE_T es cambio epistémico separado; variaciones de cobertura, logs o evidencia no constituyen por sí mismas cambios en ΔT_acc*. D_f*=1 no implica que el resto del espacio accesible permanezca constante ni que se haya capturado todo ΔT_acc*.

**Límite:** reglas lógicas de adjudicación en estado DRAFT; no resuelven inventarios, mappings físicos, fuentes, calibración, error de medición ni validación del oráculo. No crean nuevos IDs de test ni autorizan implementación/ejecución.


## 8. Regla de separación REL_f* / DEP_f* / BLOCK_f* y clasificación C_domain (2026-11-12)

Esta regla desarrolla sin ampliar la fórmula de §1 y sin aprobar mappings físicos:

1. **ID_f***: identidad semántica, tipo/clase y versión contractual de τ₂. Hash/build/record ID son identidad técnica o evidencia, no prueba autónoma de identidad semántica.
2. **REL_f***: relaciones/interfaces tipadas necesarias para invocar o componer τ₂ (extremos, dirección, tipo/rol y scope). Una relación declarada no demuestra que exista una ruta técnica completa.
3. **COND_f***: condiciones constitutivas de realizabilidad independientes de precondiciones particulares de S0. `C_domain`/`D_support*` se asigna a ID cuando define el tipo/dominio del objeto focal y a COND cuando es compatibilidad externa necesaria para realizarlo. `D_support*` no es factor adicional.
4. **DEP_f***: existencia de al menos una ruta técnica completa admisible que realice las relaciones necesarias. REL expresa el requisito relacional; DEP comprueba su realización en la ruta. La misma arista/condición/fallo no se cuenta dos veces.
5. **BLOCK_f***: bloqueo efectivo con alcance y ventana explícitos. Un bloqueo local invalida la ruta afectada; `BLOCK_f*=1` a nivel de τ₂ solo si el bloqueo es universal o alcanza todas las rutas admisibles. Si existe otra ruta válida, el bloqueo de una ruta no hace `A_f*=0` por sí solo.
6. **App_f***: las precondiciones particulares de S0 permanecen fuera de A_f* y se evalúan desde el estado de entrada de cada paso.

Regla de clasificación: asignar cada campo por su referente y función primaria; descomponer campos mixtos; si la función no es adjudicable, conservar UNKNOWN/? sin asignación múltiple. `C_other` sigue excluido como comodín; `C_info` no es autónomo; cobertura/VALID/E_T no entra en truth.

**Límite:** se cierra la regla conceptual de separación y no duplicidad, no el catálogo material por τ₂, la exhaustividad de rutas, el inventario, las evidencias ni la validación. No autoriza implementación ni ejecución.

## 9. Mapping de clases P0/P1 frente a A_f* — frontera de no equivalencia (2026-11-12)

Este mapping se deriva de la fórmula §67.3 y de las decisiones de roster/instancia aceptadas; no amplía A_f* ni adjudica observaciones:

| Elemento | Uso correcto | No equivale a |
|---|---|---|
| CMP `contract/instance/component_id` | Identidad del paquete/instancia/componente de configuración | `ID_f*` de la transformación τ₂ |
| PAR ENABLED/PROFILE | Propiedades P0 del objeto configuracional | Predicados de accesibilidad por sí solas |
| RUL AST y operand bindings | Regla declarativa y enlaces AST→PAR | `REL_f*`, REF funcional o ruta `DEP_f*` |
| REF | Relación de configuración con identidad/extremos tipados | EDGE/FK U_G, relación TGCV R*, dependencia ambiental o `DEP_f*` automáticamente |
| POL | Ausente del núcleo mínimo | `AUTH_f*` o permiso efectivo |
| MET/E_T | Identidad, versión, procedencia, observación y matching | Truth estructural A_f* o ΔT_acc* |
| P1 `C_dep*` | Éxito técnico de la dependencia provisionada; candidato de ruta única para DEP | A_f* completa o exhaustividad de rutas |
| `C_auth,base` | Autorización normativa basal común | ACL/credenciales/endpoints técnicos de provisión |
| Recursos/capacidad | Disponibilidad ex ante en RES solo si necesaria y no duplicada | Consumo, carga o capacidad provisionada sin distinción |

En consecuencia, `ID_f*` requiere identidad/versión propias de τ₂; `REL_f*` requiere inventario de relaciones/interfaces necesarias; `COND_f*` condiciones constitutivas independientes de S0; `DEP_f*` rutas técnicas completas y alternativas; `BLOCK_f*` bloqueos efectivos globales o por ruta con scope. Los registros P0 actuales no sustituyen esos inventarios.

El roster mínimo aceptado no declara REF L3; no obstante, REF=0 exige cobertura exhaustiva pre-Z/B por snapshot×etapa×ruta×scope. Hasta entonces REF permanece UNKNOWN. Los operand bindings de RUL no generan REF. P1 ambiental/técnico no se fuerza al paquete P0.

**Estado:** mapping conceptual de clases RESOLVED; mapping físico y roster de fuentes de τ₂/P1 OPEN; no se declara cobertura, REF=0, IAM sellado ni autorización de ejecución.