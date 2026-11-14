# C10-S — Manifiesto de provisión B y grafo de dependencias del microdominio Opción A

**ID:** C10-S-MD-PROVISION-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta de arquitectura y contrato de auditoría; NO aprobada, NO implementada, NO ejecutada.  
**Dependencia:** C10_S_MICRODOMAIN_CAUSAL_COMPATIBILITY_AUDIT_DRAFT_001.md.

## 1. Dictamen ejecutivo

No puede declararse todavía que B sea una intervención aislada sobre accesibilidad: no hay implementación concreta, inventario real de dependencias ni evidencia de instalación. La arquitectura candidata de menor riesgo es una provisión aislada y aditiva: adaptador focal en componente/runtime separado, versiones fijadas, permisos mínimos, recursos reservados y comunicación explícita con el sistema anfitrión. La ruta alternativa permanece en componentes baseline separados y no consume el adaptador ni sus dependencias.

Esta arquitectura reduce vías colaterales plausibles, pero no las elimina por definición. El aislamiento debe verificarse en el manifiesto real, snapshots pre/post y pruebas de no-afectación. Si el runtime aislado no es viable, modificar el entorno anfitrión se tratará como vía potencial adicional y el microdominio deberá reformularse o estimar el efecto de paquete.

**Resultado:** contrato de provisión propuesto; MD-C1 abierto; MD-C4 abierto. No se afirma primera etapa sobre A_f*.

## 2. Contrato de B: qué hace y qué no hace

B es una política asignada de provisión/configuración de la dependencia focal. Puede incluir: obtener artefacto con identidad/version fijadas; verificar origen, firma/hash e integridad; instalarlo en runtime aislado; registrar compatibilidad con interfaz/entorno; habilitar canal restringido de invocación; realizar comprobaciones técnicas que no conviertan ni apliquen configuraciones; registrar versión recibida, fallos, recursos y reversibilidad.

B NO:
- lee ni transforma el contenido funcional de la configuración fuente, salvo metadatos técnicos mínimos;
- ejecuta F1/τ2, F2, A1 o A2;
- aplica cambios al entorno destino;
- modifica F*, esquemas, datos fuente/destino u oráculo;
- amplía permisos funcionales ni altera C_auth basal;
- cambia dependencias, configuración o permisos de A1/A2;
- modifica reglas de Value, Outcome, incentivos o información de agentes;
- elimina artefactos o snapshots basales.

La verificación de instalación no equivale a accesibilidad completa. Un adaptador instalado puede seguir inaccesible si fallan identidad, relación/canal, autorización, recursos, condiciones, compatibilidad contextual o bloqueos.

## 3. Manifiesto de cambios: catálogo requerido

Cada fila debe completarse para la implementación candidata. “NO INVENTARIADO” significa ausencia de evidencia, no ausencia de cambio.

| ID | Superficie | Cambio potencial de B | Estado actual | Evidencia mínima | Vía si cambia |
|---|---|---|---|---|---|
| B-M01 | Artefacto | Binario/paquete del adaptador añadido | NO INVENTARIADO | ID, versión, hash, firma, SBOM | B→DEP→A_f*; vulnerabilidades/calidad |
| B-M02 | Runtime | Runtime, contenedor o proceso aislado añadido | NO INVENTARIADO | Imagen/hash, configuración, permisos | B→RES/SEC/latencia |
| B-M03 | Host | Paquetes, librerías o variables del host modificados | NO INVENTARIADO | Diff de paquetes/configuración pre-post | B→A1/A2, compatibilidad, seguridad |
| B-M04 | Interfaz | Endpoint/canal de invocación habilitado | NO INVENTARIADO | API/schema, ACL, puertos, rutas | B→REL/AUTH/latencia |
| B-M05 | Permisos | ACL, credenciales, tokens o roles creados | NO INVENTARIADO | Diff de permisos y alcance | B→AUTH/App/A_f*/V |
| B-M06 | Datos | Configuración fuente/destino o metadatos modificados | NO INVENTARIADO | Hashes y snapshots | B→estado/App/F* |
| B-M07 | Recursos | CPU, RAM, almacenamiento, I/O, slots reservados/consumidos | NO INVENTARIADO | Cuotas y medición por componente | B→RES/CAP→rutas/Outcome |
| B-M08 | Red | DNS, proxy, firewall, rutas o puertos modificados | NO INVENTARIADO | Diff de reglas/topología | B→REL/A1/A2/seguridad |
| B-M09 | Seguridad | Superficie de ataque, políticas, certificados o sandbox | NO INVENTARIADO | Revisión de seguridad | B→riesgo/coste/Value |
| B-M10 | Observabilidad | Logs, métricas, telemetría añadidos | NO INVENTARIADO | Esquema y retención | B→información/conocimiento |
| B-M11 | Estado | Cachés, registros, índices o estado persistente | NO INVENTARIADO | Inventario y snapshots | B→estado fuente/destino/rutas |
| B-M12 | Rendimiento | Latencia, throughput, contención o prioridad | NO INVENTARIADO | Medición comparable por brazo | B→tiempo/coste/calidad |
| B-M13 | Oráculo | Validador, reglas F* o dataset de referencia | PROHIBIDO EN B | Hash/version inmutables pre/post | B→medición/F* circular |
| B-M14 | Alternativa | Exportador/importador nativo A1/A2 | PROHIBIDO EN B | Hash/version y pruebas funcionales pre/post | B→ruta alternativa/Reach |
| B-M15 | Reversibilidad | Desinstalación, rollback, residuos | NO INVENTARIADO | Procedimiento y diff post-rollback | Persistencia/vías residuales |

No se completa una fila por inferencia. Para declarar que una superficie no cambia se necesita comparación verificable pre/post con cobertura explícita.

## 4. Arquitectura candidata y grafo lógico

Propuesta de grafo:

- Z asigna la política B.
- B provisiona paquete adaptador en runtime aislado, con hash/version fijados y cuotas/ACL limitadas.
- El runtime expone un endpoint focal; C_dep verifica el estado técnico.
- A_f* evalúa todos los predicados de accesibilidad de τ2.
- F1/τ2 realiza la conversión solo tras selección/inicio.
- F2 aplica y valida en destino.
- En paralelo, baseline independiente: S0 → A1 exportador neutral → artefacto de intercambio → A2 importador nativo → mismo destino/F*.
- El oráculo F* es solo lectura, fijo, versionado y ciego a Z/B/O/V.

Clases de dependencia:

| Clase | Ejemplos | Tratamiento |
|---|---|---|
| D-Focal | Adaptador, runtime, librerías exclusivas, endpoint | Puede cambiar por B; inventario y pinning |
| D-Alternativa | Exportador neutral, formato, importador nativo | Debe permanecer funcionalmente invariante en R0/R1 |
| D-Común-medición | Oráculo F*, validador | Compartible si solo mide, inmutable, ciego y no genera rutas |
| D-Común-infraestructura | Host, CPU, RAM, almacenamiento, red, SO | Riesgo de interferencia/vía colateral; aislar o modelar |
| D-Compartida-crítica | Librería/API/servicio usado por ambas rutas | Compromete independencia si B lo cambia/degrada; R2 |
| D-Externa | Servicios/paquetes fuera de frontera | Declarar frontera, versión, disponibilidad y límites; sin observabilidad, Reach=? |

Por cada nodo se requiere: component_id, semantic_role, TID/SID/RID, version, hash, owner, install_time, dependency_type, parent_component, consumers, permissions, resource_profile, network_edges, mutable_state y evidence_ref.

Por cada arista: source, target, relation (calls/loads/reads/writes/shares_resource/authenticates/validates), direction, time_window, version_constraint, evidence, coverage y status (1/0/?). Una lista de paquetes sin relaciones/consumidores no es inventario suficiente.

## 5. Recursos, permisos y estado

**Recursos.** Distinguir capacidad instalada del sistema, recursos compartidos por sistema-tiempo, recursos reservados/asignados a unidad, aportados por unidad y consumidos durante ejecución. B puede reservar cuota para instalación/runtime; el consumo de F1 ocurre después, en t7, y no se retrotrae como accesibilidad basal. La reserva no debe reducir cuota de A1/A2/F2 en R0/R1. Si existe contención, medirla como vía causal y clasificar escenario colateral o modelar interferencia.

**Permisos.** Permisos mínimos, explícitos, no heredados de credenciales de usuario y limitados a la interfaz necesaria. B no cambia autorizaciones funcionales ni permisos del destino. Si requiere hacerlo, C_auth pasa a ser variable intervenida y la atribución focal queda comprometida. Credenciales/tokens/expiración se versionan sin registrar secretos.

**Estado.** B no altera configuración fuente/destino. Artefactos temporales se separan de estados funcionales. Capturar snapshots/hash antes de B, después de B y tras rollback. Residuos que afecten alternativas, seguridad o rendimiento impiden declarar reversibilidad completa.

## 6. No-afectación de A1/A2 en R0/R1

No-afectación no se demuestra por identidad nominal ni por no invocar A1/A2 durante B. Debe verificarse:
1. identidad/version/hash de exportador, formato e importador pre/post;
2. dependencias transitivas y librerías compartidas;
3. permisos, credenciales y canales de red;
4. recursos disponibles y cuotas durante las ventanas de la ruta alternativa;
5. estado/configuración fuente y destino;
6. latencia, tasa de éxito, integridad, seguridad y calidad de salida de A1/A2 bajo condiciones equivalentes;
7. mismo oráculo F*, versión y tolerancias;
8. ausencia de cambios en información/conocimiento del agente que afecten selección;
9. rollback sin residuos funcionalmente relevantes.

Estos son criterios propuestos; no hay evidencia de que se hayan satisfecho. La prueba requiere comportamiento funcional, no solo hashes.

**R1:** A1/A2 deben seguir satisfaciendo F* bajo B=0 y B=1 dentro de tolerancias predefinidas; márgenes de equivalencia justificados antes de observar resultados. No usar ausencia de significación como equivalencia.

**R0:** ausencia de alternativa respecto de catálogo finito de mecanismos, formatos, versiones, permisos y recursos con cobertura documentada. Fuera del universo, F_alt,0=?.

## 7. Reversibilidad y snapshots

Snapshots mínimos:
- S_preB: host, configuración fuente/destino, permisos, recursos, red, componentes y rutas.
- S_postB: mismos campos tras provisión/verificación y antes de F1.
- S_rollback: mismos campos tras retirada/rollback.
- S_routeA: comportamiento A1/A2 pre/post B bajo fixture funcional de referencia.

Snapshots inmutables, fechados, identificados por hash y ligados a unidad/versión. No comparar granularidades distintas sin mapping. Rollback completo solo si no quedan cambios relevantes ni efectos residuales; incertidumbre se marca ?.

## 8. Arquitecturas candidatas

| ID | Alternativa | Ventaja | Riesgo | Estado |
|---|---|---|---|---|
| ARCH-B1 | Adaptador sidecar/runtime aislado, aditivo y con cuotas | Reduce cambios de host y dependencias compartidas | Interfaz/recursos | RECOMENDADA PARA EVALUAR, no aprobada |
| ARCH-B2 | Instalación en runtime/host compartido | Simplicidad | Vías colaterales/dependencias transitivas | No preferida para escenario aislado |
| ARCH-B3 | Servicio externo gestionado | Aislamiento del host local | Red, disponibilidad, seguridad y dependencia externa | Alternativa si se modela |

No se instala ningún componente en este bloque documental.

## 9. Criterios de cierre

**MD-C1 — Manifiesto B:** cerrar solo cuando M01–M15 tengan estado/evidencia; versiones/hash/firmas/dependencias identificadas; permisos, recursos, red y datos comparados; B no ejecuta transformaciones ni cambia F*/oráculo; reversibilidad/residuos caracterizados; vías directas incorporadas al DGP.

**MD-C4 — Independencia A1/A2:** cerrar solo cuando catálogo/grafo completos dentro de frontera explícita; componentes alternativos identificados/versionados; recursos, permisos y configuración no modificados/degradados por B; equivalencia funcional pre/post evaluada con margen preespecificado; si no se prueba no-afectación, R2/efecto paquete permanece y no se interpreta IV focal.

## 10. Contratos documentales para futuro verificador

| ID | Aserción |
|---|---|
| PROV-01 | B instala/habilita adaptador sin ejecutar F1/F2/A1/A2 |
| PROV-02 | B no modifica F*, dataset ni oráculo |
| PROV-03 | Snapshots preB/postB/rollback cubren host, configuración, permisos, red y componentes |
| PROV-04 | Dependencias transitivas y consumidores están inventariados |
| PROV-05 | Recursos de B no reducen disponibilidad A1/A2/F2 en R0/R1 |
| PROV-06 | Permisos B son mínimos y no amplían C_auth funcional |
| PROV-07 | B no altera fuente/destino ni estado funcional basal |
| PROV-08 | A1/A2 conservan conformidad F* pre/post B dentro de margen justificado |
| PROV-09 | B no modifica librerías/APIs/servicios críticos compartidos |
| PROV-10 | Rollback no deja residuos funcionales relevantes |
| PROV-11 | Nodo/arista desconocido propaga cobertura incompleta y Reach=? cuando corresponda |
| PROV-12 | Primera etapa C_dep no se etiqueta como primera etapa A_f* sin verificar predicados restantes |

Contratos no implementados ni ejecutados.

## 11. Límites y siguiente operación

No existe inventario técnico real; no se han fijado formatos, runtime, SO, librerías, interfaces, hashes, cuotas, permisos ni ventanas. No se ha demostrado no-afectación A1/A2 ni que B modifique A_f*. D1/D2 sigue abierto y no se resuelve la tensión p0=.20 frente a elegibilidad basal A_f,0*=0. F*, Value, horizonte y población final permanecen abiertos.

Siguiente operación documental: matriz de cobertura del grafo y estados de evidencia 1/0/? por nodo/arista y predicado de accesibilidad/ruta. Solo después se determinará si el universo es exhaustivo o Reach/F_alt deben quedar indeterminados.

Ningún NO INVENTARIADO equivale a “sin cambio”; ningún hash idéntico prueba equivalencia funcional; ningún nombre distinto prueba independencia; ningún test documental equivale a ejecución o PASS.


---

## 12. Auditoría causal de vías colaterales para D2 — reconciliación especializada

**Estado:** auditoría conceptual/documental especializada, recuperada y ampliada a partir del material conversacional aportado el 2026-11-06 y reconciliada con B-M01…15, PROV-01…12, la matriz U_G y la arquitectura causal. **DRAFT / NO APROBADA / NO CONGELADA / NO EJECUTADA.** No certifica aislamiento material de B ni cierre MD-C1/MD-C4.

### 12.1. Dictamen

El contrato material aceptado en DEC-C10-067 define conceptualmente la política de provisión, pero no demuestra que una implementación concreta sea una intervención técnica aislada sobre accesibilidad. ARCH-B1 (sidecar/runtime separado, aditivo, versionado, permisos mínimos y cuotas propias) es recomendación para evaluar, no arquitectura aprobada ni instalada. El inventario real permanece no disponible: `NO INVENTARIADO` no significa ausencia.

La vía focal candidata es:

`Z → B → W_attempt → C_dep* → A_f* → D_f* → ΔT_acc* → Reach → Π_H → Execution → Outcome → Value`

Debe distinguirse de cualquier cambio concurrente en condiciones constitutivas adicionales, rutas alternativas, resultados, información/conocimiento o medición. Si B afecta vías distintas de la focal, el ITT sigue siendo efecto de la política material asignada, pero no puede atribuirse exclusivamente a `ΔT_acc*` sin identificación adicional.

### 12.2. Dominios B-M01…15 y riesgos que deben auditarse

| Dominio | Qué comprobar | Vía/riesgo si cambia diferencialmente |
|---|---|---|
| B-M01 Artefacto y versión | Identidad, versión, hash y firma del componente focal | Confundir cambio de dependencia con cambio de funcionalidad |
| B-M02 Runtime | Runtime/imagen/configuración donde se aloja el adaptador | Dependencias o comportamiento compartido |
| B-M03 Host | Cambios en host, sistema operativo y paquetes modificados | B→A1/A2, compatibilidad y seguridad |
| B-M04 Interfaz | Endpoint/canal de invocación realmente habilitado | B→REL/AUTH/latencia; rutas adicionales |
| B-M05 Permisos | ACL, credenciales, tokens y roles creados; alcance y expiración | B→AUTH/App/A_f*/Value |
| B-M06 Datos | Configuración fuente/destino, metadatos y datos funcionales modificados | B→estado/App/F*/Outcome |
| B-M07 Recursos | CPU, RAM, almacenamiento, I/O y slots reservados/consumidos | B→RES/CAP→rutas/Outcome |
| B-M08 Red | DNS, proxy, firewall, rutas y puertos | B→REL/A1/A2/seguridad |
| B-M09 Seguridad | Superficie de ataque, políticas, certificados y sandbox | Bloqueos, habilitaciones, riesgo/coste/Value |
| B-M10 Observabilidad | Logs, métricas y telemetría añadidos; acceso de agente/evaluador | Vía informativa o sesgo de medición |
| B-M11 Estado | Cachés, registros, índices y estado persistente | B→estado fuente/destino/rutas |
| B-M12 Rendimiento | Latencia, throughput, contención, prioridad y degradación | B→tiempo/ejecución/Outcome |
| B-M13 Oráculo | Criterios, reglas, versiones y mecanismo de evaluación | Cambio artificial de resultado medido |
| B-M14 Alternativas | Inventario, disponibilidad y comportamiento de rutas alternativas | Cambio en Reach independiente de la apertura focal |
| B-M15 Reversibilidad | Rollback, residuos, dependencias y efectos persistentes | Estado postprovisión distinto aun tras rollback |

La tabla es un mapa de inspección y riesgo, no evidencia de que las alteraciones hayan ocurrido. Los estados actuales del manifiesto permanecen `NO INVENTARIADO` mientras no exista evidencia técnica observada.

### 12.3. Dos taxonomías que no deben confundirse

**A. Clases de ruta del universo candidato U_G** (taxonomía topológica de la matriz de cobertura): focal, alternativa, compartida, externa y desconocida. Se conserva tal cual; la cobertura parcial/desconocida impide declarar exhaustividad.

**B. Clases de mecanismo causal para adjudicar hallazgos** (taxonomía analítica; no sustituye U_G):

1. **Mecanismo focal:** provisión cambia `C_dep*`, que puede cambiar `A_f*` y después `T_acc*`.
2. **Cambio de condición constitutiva:** B altera autorización, recursos, capacidad u otra condición que también interviene en `A_f*`; ya no es modificación exclusiva de la dependencia focal.
3. **Vía colateral hacia resultados:** B afecta directamente Reach, trayectoria, ejecución, Outcome o Value, sin pasar necesariamente por la accesibilidad focal.
4. **Cambio epistémico/informativo:** B altera conocimiento del agente, comunicaciones, observabilidad, cobertura o adjudicación, sin que ello implique por sí mismo cambio estructural de accesibilidad.

Una modificación puede activar varias clases de mecanismo simultáneamente; no forzar exclusividad. La vía epistémica del evaluador debe mantenerse separada de cambios estructurales, y el conocimiento del agente separado de la información técnica constitutiva.

### 12.4. Pruebas de separación y evidencia exigible

Para defender D2 como contraste de provisión técnica aislada se requieren, al menos:

- **Independencia funcional:** A1/A2 y rutas alternativas conservan comportamiento y conformidad F* antes/después de B, con margen preespecificado.
- **Independencia de recursos:** B no consume ni desplaza recursos compartidos que condicionan otras transformaciones; medir cuotas, compromisos, contención y consumidores.
- **Separación de permisos:** interfaz técnica de B no modifica autorización normativa basal ni permisos funcionales del destino.
- **Invariancia informativa:** no hay comunicaciones, formación, avisos o incentivos diferenciales que cambien conocimiento/selección, salvo que se modelen como vías de política.
- **Invariancia del entorno:** datos, red, seguridad, rendimiento, latencia, estado, dependencias y oráculo no cambian de forma causalmente relevante fuera de la vía focal.
- **Reversibilidad:** rollback restituye el estado previo y no deja dependencias ni efectos residuales relevantes.

Evidencia mínima: manifiesto real con identidad/versiones/hash/firmas; grafo transitivo de componentes, dependencias y consumidores; snapshots inmutables pre-B, post-B y post-rollback; diffs de configuración/permisos/red/datos; cuotas y medidas de recursos; mediciones comparables de rendimiento; pruebas funcionales de alternativas; trazabilidad de comunicaciones y registros; adjudicación ciega cuando corresponda. Los snapshots deben asociarse a unidad, versión y ventana; no comparar granularidades distintas sin mapping.

Los contratos ya definidos siguen siendo rectores: PROV-01…12, en especial PROV-02 (F*/dataset/oráculo), PROV-03 (snapshots), PROV-04 (dependencias/consumidores), PROV-05 (no reducción de disponibilidad A1/A2/F2), PROV-06 (permisos mínimos sin ampliar C_auth funcional), PROV-08 (conformidad A1/A2), PROV-09 (no modificación de dependencias críticas compartidas), PROV-10 (rollback limpio), PROV-11 (propagación de desconocidos) y PROV-12 (no equiparar primera etapa C_dep con primera etapa A_f*).

### 12.5. Regla de adjudicación y consecuencia para los estimandos

| Hallazgo observado | Consecuencia interpretativa |
|---|---|
| Solo cambia C_dep* y después A_f*; demás condiciones y rutas permanecen bajo contrato/evidencia | Compatible con mecanismo focal, sujeto al resto de supuestos e identificación |
| Cambia otra condición constitutiva | Efecto de provisión conjunta; atribución exclusiva a accesibilidad no demostrada |
| Cambia ruta alternativa o recurso compartido | Vía paralela potencial a Reach, trayectoria u Outcome; revisar estimando/exclusión/interferencia |
| Cambia información conocida por agente | Posible mediación por conocimiento/consideración/selección; ITT es efecto de paquete si B la induce |
| Cambia oráculo, observación, cobertura o adjudicación | Cambio epistémico/medición; no confundir con cambio estructural de T_acc |
| No puede determinarse si hubo cambios | Identificación limitada; no declarar aislamiento ni ausencia de vías |

La aleatorización puede identificar el ITT de la política asignada, bajo su diseño, pero no convierte automáticamente ese ITT en efecto causal específico de `ΔT_acc*`. Tampoco debe ajustarse mecánicamente por conocimiento postratamiento: puede ser mediador inducido por B y generar sesgo si se condiciona sin estrategia de identificación apropiada.

### 12.6. Estado y condiciones de cierre

**Abierto:** inventario técnico real; grafo transitivo y cobertura; snapshots; pruebas de no-afectación; fuente/alcance de autorización; cuotas y medición de recursos/capacidad; información comunicada; oráculo y rendimiento; alternativas; reversibilidad; reglas de adjudicación de desviaciones.

**MD-C1** solo cierra cuando M01–M15 tienen estado y evidencia, componentes/versiones/hash/firmas/dependencias están identificados, permisos/recursos/red/datos se comparan, B no ejecuta transformaciones ni cambia F*/oráculo, reversibilidad/residuos se caracterizan y vías directas se incorporan al DGP.

**MD-C4** solo cierra cuando el catálogo/grafo es completo dentro de frontera explícita, componentes alternativos están identificados/versionados, recursos/permisos/configuración no se modifican ni degradan por B y la equivalencia funcional pre/post se evalúa con margen justificado. Si no se demuestra no-afectación, permanece el escenario colateral/efecto de paquete y no se interpreta IV focal.

Ningún estado `NO INVENTARIADO`, `?`, `NONE` o `PARTIAL` equivale a ausencia, invariancia o PASS. Ningún hash idéntico demuestra equivalencia funcional; ningún nombre distinto demuestra independencia. Los contratos aquí descritos son documentales y no han sido implementados ni ejecutados. No se declara aislamiento de B, cierre MD-C1/MD-C4 ni autorización científica.



## 13. Reconciliación del límite entre provisión y operación funcional (2026-11-06)

- **B/provisión:** obtiene y provisiona el artefacto adaptador, verifica identidad/integridad/compatibilidad técnica, configura runtime aislado y expone el canal previsto con permisos/recursos acotados. No ejecuta F1/F2/A1/A2, no transforma S0 ni aplica C_dst.
- **Adaptador provisionado:** artefacto/runtime/canal técnicamente dispuesto, desglosado en evidencia por componente. No significa que τ2 sea accesible para la unidad.
- **C_dep*:** describe estado técnico de dependencia; no sustituye A_f*(τ2), cobertura de rutas ni aplicabilidad de F1.
- **F1/τ2:** conversión S0→S2 tras selección/inicio; ejecución posterior a medición de accesibilidad y fuera de B.
- **F2:** aplicación S2→SF y verificación destino, con condiciones propias.
- **A1/A2:** ruta basal S0→S1→SF; no-afectación por B requiere comparación funcional pre/post y cobertura de dependencias, recursos, permisos y rendimiento, no solo hashes.
- **F*:** criterio de ruta completa, separado de Outcome/Value. PASS local no implica F*=1.

Esta reconciliación no convierte ARCH-B1 en arquitectura aprobada ni acredita aislamiento material. MD-C1 y MD-C4 permanecen OPEN hasta completar manifiesto real, grafo transitivo, snapshots y pruebas de no-afectación. NO INVENTARIADO/?/PARTIAL conservan incertidumbre.

**Estado:** clarificación documental; sin instalación, ejecución, validación ni cierre de vía colateral/exclusión.


## 14. Matriz de adjudicación MAP-05 — cobertura causal de B-M01…15 y PROV-01…12 (2026-11-09)

**Estado:** clasificación analítica documental completada; evidencia material ausente. La matriz no afirma que ninguna superficie haya cambiado ni que las salvaguardas se cumplan. Todas las filas conservan estado ? / NO INVENTARIADO salvo las prohibiciones contractuales explícitas de B-M13 y B-M14. Una prohibición en el diseño no es evidencia de que una implementación la haya respetado.

### 14.1. Reglas de clasificación
- **Focal condicionada:** cambio estrictamente necesario para provisionar la dependencia y ya representado por C_dep*/D_f*; requiere demostrar que no incorpora funciones adicionales.
- **Constitutiva:** modifica una condición de A_f* distinta de la dependencia focal o el conjunto de transformaciones factibles.
- **Colateral:** puede alcanzar Reach, trayectoria, ejecución, Outcome o Value sin quedar representada por el tratamiento focal declarado.
- **Epistémica/informativa:** cambia conocimiento, señales, comunicaciones o decisiones del agente.
- **Medición/oráculo:** cambia observabilidad, cobertura, criterios o adjudicación.
- **Interferencia/residuo:** afecta otras unidades, periodos, rutas o estados posteriores.
- Las clases no son mutuamente excluyentes.

### 14.2. Cobertura por superficie

| ID | Vía/mecanismo que debe adjudicarse | Clasificación primaria | Evidencia/falsador mínimo | Estado |
|---|---|---|---|---|
| B-M01 Artefacto | Identidad/integridad/compatibilidad→C_dep*; vulnerabilidad/calidad→riesgo/coste/Value | Focal condicionada + colateral | SBOM, firma/hash, dependencias, vulnerabilidades, licencia y prueba funcional | ? / NO INVENTARIADO |
| B-M02 Runtime | Runtime/librerías/colas→C_dep*; runtime compartido→A1/A2/F2, latencia o spillover | Focal condicionada + colateral + interferencia | Imagen/hash, aislamiento, consumidores, recursos, llamadas y pruebas concurrentes | ? / NO INVENTARIADO |
| B-M03 Host | Paquetes/variables/SO→compatibilidad, estado y rutas alternativas | Colateral + interferencia | Diffs pre/post/rollback y pruebas A1/A2/F2 comparables | ? / NO INVENTARIADO |
| B-M04 Interfaz | Endpoint/canal→REL_f*/DEP_f*; exposición adicional→seguridad, latencia o información | Focal condicionada + constitutiva/colateral | API/schema, ACL, puertos, topología, logs y alcance | ? / NO INVENTARIADO |
| B-M05 Permisos | Permiso técnico puede ser focal; autorización funcional altera AUTH_f*; credenciales visibles pueden alterar conocimiento | Focal condicionada o constitutiva + epistémica | Diff ACL/roles/tokens; separar permiso técnico de C_auth,base; probar no ampliación funcional | ? / NO INVENTARIADO |
| B-M06 Datos/estado | Cambios fuente/destino/metadatos→aplicabilidad, F*, estado, Outcome o Value | Constitutiva + colateral + medición | Hashes/snapshots, diffs semánticos y prueba de invariancia funcional | ? / NO INVENTARIADO |
| B-M07 Recursos | Reserva/consumo/contención→RES_f* o capacidad; desplazamiento→A1/A2/F2/Reach/Outcome | Constitutiva + colateral + interferencia | Capacidad utilizable, demanda concurrente, cuotas, colas, consumidores y consumo por brazo | ? / NO INVENTARIADO |
| B-M08 Red | DNS/proxy/firewall/rutas→REL_f*/DEP_f*; rutas comunes→alternativas/seguridad | Focal condicionada + constitutiva + colateral | Diff de red, flujos, rutas, puertos, ACL, consumidores y pruebas de alternativa | ? / NO INVENTARIADO |
| B-M09 Seguridad | Sandbox/certificados/políticas→BLOCK_f*/DEP_f*; riesgo/coste/confianza→Outcome/Value | Constitutiva + colateral | Threat model, políticas/certificados, superficie de ataque, costes y bloqueos | ? / NO INVENTARIADO |
| B-M10 Observabilidad | Logs/telemetría→K del agente/selección; acceso evaluador→cobertura y medición | Epistémica + medición | Esquema, acceso por rol, mensajes/notificaciones, retención y ceguera | ? / NO INVENTARIADO |
| B-M11 Estado persistente | Cachés/índices/registros→estado funcional, alternativas, contaminación entre unidades y carryover | Colateral + interferencia/residuo | Inventario de estado, snapshots, aislamiento por unidad, limpieza y rollback | ? / NO INVENTARIADO |
| B-M12 Rendimiento | Latencia/throughput/prioridad→condiciones de uso, selección, ejecución y Outcome | Colateral + constitutiva potencial + interferencia | Benchmarks preespecificados, carga equivalente, colas y medidas por ruta/unidad | ? / NO INVENTARIADO |
| B-M13 Oráculo | Modificación de F*/dataset/criterio→resultado medido artificialmente | Medición/oráculo | Identidad/hash/versionado inmutable y acceso ciego pre/post | PROHIBIDO EN B; cumplimiento ? |
| B-M14 Alternativas | Cambio de A1/A2/exportador/importador→Reach y trayectoria no focal | Colateral + interferencia | Identidad/versiones, dependencias transitivas y equivalencia funcional pre/post | PROHIBIDO EN B; cumplimiento ? |
| B-M15 Reversibilidad | Rollback incompleto→residuos, dependencias, permisos, recursos o estado persistente | Interferencia/residuo + colateral | Snapshot pre/post/rollback, diff semántico y prueba posterior de rutas | ? / NO INVENTARIADO |

### 14.3. Trazabilidad PROV-01…12

| Contrato | Qué controla | Qué NO demuestra por sí solo |
|---|---|---|
| PROV-01 | B no ejecuta F1/F2/A1/A2 | Ausencia de vías colaterales por runtime, recursos o información |
| PROV-02 | B no modifica F*/dataset/oráculo | Invariancia de observación, ceguera o cobertura |
| PROV-03 | Snapshots de host, configuración, permisos, red y componentes | Completitud semántica ni ausencia de cambios no observados |
| PROV-04 | Dependencias transitivas y consumidores | Equivalencia funcional de las rutas consumidoras |
| PROV-05 | No reducción de recursos disponibles A1/A2/F2 | Ausencia de contención en todas las cargas/ventanas sin medición |
| PROV-06 | Permisos mínimos sin ampliar autorización funcional | Que credenciales o señales no cambien conocimiento |
| PROV-07 | No alterar fuente/destino ni estado funcional basal | Ausencia de cachés, residuos o cambios semánticos no capturados |
| PROV-08 | Conformidad funcional A1/A2 pre/post dentro de margen | No-afectación de toda ruta alternativa no incluida en el catálogo |
| PROV-09 | No modificar dependencias críticas compartidas | Ausencia de degradación indirecta por recursos/red/host |
| PROV-10 | Rollback sin residuos funcionales relevantes | Ausencia de efectos temporales ya producidos o carryover no observado |
| PROV-11 | Desconocidos propagan cobertura incompleta/Reach=? | Que el universo inspeccionado sea exhaustivo |
| PROV-12 | C_dep no se equipara a primera etapa A_f* | Que la primera etapa A_f* exista o sea suficientemente fuerte |

**Regla de cobertura:** PROV-01…12 son contratos de control, no pruebas ejecutadas. No sumar PASS por contar contratos definidos. La adjudicación exige evidencia ligada a unidad, versión, ventana, nodo/arista, consumidor, resultado potencialmente afectado y cobertura. Los desconocidos no se recodifican como 0.

### 14.4. Resultado MAP-05 y regla por estimando

La matriz permite concluir qué debe probarse, no qué ocurrió. Por tanto:
- ITT_Z^D2 / efecto de política podrá estimarse como efecto de asignación a B si el diseño, asignación, seguimiento y observación lo permiten; incluirá las vías que B induzca.
- LATE_f^D2 no es interpretable como efecto focal mientras exclusión, monotonicidad, relevancia, consistencia, interferencia y mapping del tratamiento focal no estén defendidos.
- θ_Af(q_X*) / θ_A(q) requieren sus propios mappings a políticas de accesibilidad y no quedan identificados por superar una checklist técnica.
- Si B-M06/M07/M09/M11/M12/M14 activa vías no incluidas en el objeto focal, el resultado es efecto de paquete o exige rediseño/estimando alternativo. No ajustar mecánicamente por mediadores postratamiento.
- Si B-M10/B-M13 altera conocimiento u observación, separar efecto informativo del estructural y evaluar comparabilidad de Outcome y Value por separado.

**Dictamen MAP-05:** CLASSIFICATION_DEFINED / MATERIAL_EVIDENCE_NOT_AVAILABLE. MD-C1 y MD-C4 siguen OPEN; IV-G4 sigue OPEN; exclusión no demostrada; no se declara D2 aislado. Siguiente paso admisible: completar roster de evidencia/grafo por frontera, nodo/arista, consumidor, unidad, versión y ventana. No implementación, parametrización, simulación ni ejecución.



## 15. Crosswalk B-M01…15 → U*/R*/C*/X*/E_T para MED-02c (2026-11-10)

Esta tabla no cambia los estados del manifiesto ni convierte NO INVENTARIADO en ausencia. Es una regla de tipado de subcampos; no una clasificación automática de la superficie completa.

| Superficie | Tipo(s) primarios posibles | Regla |
|---|---|---|
| B-M01 artefacto/versión | U*/MET/E_T | Identidad funcional de transformación solo si es el objeto transformacional; versión/hash/provenance como MET/E_T |
| B-M02 runtime | X*/C*/E_T | Estado/versión efectiva constitutiva X*; configuración/restricción C*; imagen/hash como evidencia MET/E_T |
| B-M03 host | X*/C*/E_T | Estado efectivo host/OS X* si afecta accesibilidad; regla/restricción C*; diff y fuente E_T |
| B-M04 interfaz/canal | R*/C*/E_T | Endpoint/conexión R*; ACL/bloqueo C*; log E_T |
| B-M05 permisos | C*/E_T | Autorización/ACL efectiva C*; separar ACL técnica de C_auth,base; evidencia de cambio E_T |
| B-M06 datos/configuración | CMP/PAR/REF/RUL/C*/E_T | Estado del paquete bajo M; condición constitutiva solo si afecta realizabilidad; snapshot/hash E_T |
| B-M07 recursos | C*/X*/E_T | Disponibilidad/reserva C*; estado del pool X* solo si constitutivo; consumo posterior separado |
| B-M08 red | R*/C*/E_T | Topología/ruta R*; firewall/permiso/bloqueo C*; telemetría E_T |
| B-M09 seguridad | C*/X*/E_T | Política/restricción C*; estado contextual efectivo X* solo con regla; evidencia E_T |
| B-M10 observabilidad | E_T | Logs, métricas, cobertura y retención; conocimiento del agente es vía informativa separada |
| B-M11 estado persistente | X*/C*/U*/R*/E_T | Estado efectivo X* si cambia accesibilidad; precondición/bloqueo C*; objetos/relaciones U*/R*; diff E_T |
| B-M12 rendimiento | C*/OUTSIDE_MEDIATOR/E_T | Condición operativa solo si preespecificada como accesibilidad; de otro modo resultado downstream/externo; medición E_T |
| B-M13 oráculo | E_T/medición | No forma parte de ΔT_acc*; cambio de oráculo amenaza comparabilidad F* |
| B-M14 alternativa | U*/R*/C*/E_T | Transformaciones, relaciones y condiciones de A1/A2; independencia requiere evidencia pre/post |
| B-M15 rollback/residuos | X*/C*/U*/R*/E_T | Clasificar residuo por función y vigencia; rollback/diff como evidencia |

El manifiesto de §3/§12.2 sigue NO INVENTARIADO donde no hay evidencia. Ningún subcampo se declara cambiado o invariante sin snapshot comparable y cobertura.


## 14. Reconciliación integral PB — uso vigente del manifiesto (2026-11-11)

La lectura integrada PB queda registrada en el maestro C10-S §267. Este manifiesto sigue siendo una arquitectura candidata y un catálogo de inspección, no un inventario material. B-M01…15 no se rellenan por inferencia; NO INVENTARIADO conserva su significado. B-M13 (oráculo/F*) y B-M14 (alternativas A1/A2) continúan prohibidos como superficies modificadas por B.

Se precisa el límite de intervención: D2 actúa en P1 mediante provisión aditiva de dependencia/adaptador focal. No modifica P0 (paquete declarativo CMP/PAR/REF/RUL/MET), F*, mapping, datos fuente/destino, autorización normativa funcional basal ni alternativas. El servicio lógico C10S-SVC-REQUEST-PROCESSOR y el adaptador/dependencia focal son objetos distintos: el primero conserva su contrato funcional; el segundo es el elemento técnico que la política intenta provisionar. Permisos técnicos mínimos/ACL/endpoints no equivalen a cambiar C_auth,base.

La arquitectura aislada (runtime separado, artefacto/versiones fijados, cuotas y permisos mínimos, canal restringido) es la opción de menor riesgo, pero no demuestra aislamiento ni ausencia de vías colaterales. Se requieren snapshots/diffs y pruebas de comportamiento A1/A2, recursos, dependencias transitivas, seguridad, latencia, rollback y consumidores. PROV-05/09 siguen abiertos.

C_dep*=C_install∧C_integrity∧C_compat∧C_oper es éxito técnico de la dependencia, no A_f* completa ni D_f*. A_f* conserva la fórmula candidata depurada del maestro §67.3; DEP puede coincidir con C_dep solo bajo ruta única estipulada. C2 debe medir separadamente W_programmed, W_attempt, S_install/componentes, C_dep*, A_f*, D_f*, ΔT_acc*, evidencia E_T/ΔE_T y Reach/Π. La primera etapa IV relevante sería D_f*, no C_dep ni intento; D_f_obs no sustituye truth D_f*. s=0.80 sigue sin validar.

No hay instalación, runtime, grafo, artefacto, hash, IAM/snapshot material, prueba de no-afectación ni ejecución. No se declara MD-C1/MD-C4 cerrado ni D2 aislado. Sin implementación/fixtures/ejecución.


## 16. Reconciliación material PB con identidad B1 por UE (2026-11-11)

Se integra el resultado de `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md` como reconciliación vigente del contrato material D2. DEC-C10-067 conserva su alcance: B_g0 no programa provisión focal y B_g1 programa un intento, sin garantizar recepción/éxito. Se armoniza con `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001`: contrato/plantilla CMP común, instance_id único y versionado por UE; el adaptador/dependencia P1 es un objeto distinto de la instancia lógica del servicio CMP.

B-M01…12 y B-M15 permanecen NO INVENTARIADO donde no existe evidencia; B-M13 (F*/oráculo) y B-M14 (A1/A2) son superficies prohibidas de modificación por B. Se mantienen P0 invariante como requisito, P1 como superficie focal de provisión y P2 como perímetro causal transversal. La arquitectura sidecar sigue recomendada para evaluación, no aprobada ni probada.

No hay roster/IDs concretos por UE, IAM/C_SRC, snapshots, grafo material, artefacto/runtime, ACL/recursos medidos ni pruebas de no-afectación. PROV-05/09, MD-C1/MD-C4 y G-MAT siguen OPEN/BLOCKED. C_dep*, A_f*, D_f* y ΔT_acc* no se infieren unos de otros. No se declara D2 aislado ni se autoriza captura, implementación o ejecución.