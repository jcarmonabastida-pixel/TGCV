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
