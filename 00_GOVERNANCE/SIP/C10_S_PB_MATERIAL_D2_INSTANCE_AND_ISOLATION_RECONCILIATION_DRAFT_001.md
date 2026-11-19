# C10-S — PB: reconciliación material D2, identidad B1 por UE y aislamiento

**ID:** C10-S-PB-MATERIAL-RECON-001  
**Fecha:** 2026-11-11  
**Estado:** PB_MATERIAL_CONTRACT_RECONCILED_DOCUMENTALLY / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED  
**Ámbito:** C10-S / D2 primario candidato / B1 / PB / PR #116 / `research/c10-s-consolidation-draft`  
**Precedencia:** gobernanza canónica de `main`; DEC-C10-057…069 y 074…088 en su alcance; DEC-C10S-B1-UNIT-001; DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001; PA–PE; contratos U_G, IAM, provisión, snapshots y DGP vigentes.

## 1. Dictamen ejecutivo

Esta reconciliación integra el contrato material de D2, la identidad de servicio B1 por UE, el overlay IAM/U_G, el manifiesto B-M01…15, el grafo de dependencias, los snapshots y las rutas alternativas. Reutiliza los contratos existentes y no crea un segundo inventario ni un nuevo esquema de datos.

**Resultado:** la semántica de asignación D2 y la identidad lógica de instancia B1 quedan enlazadas documentalmente. No existe, sin embargo, roster material de UE, IAM/C_SRC observado, inventario de dependencias, artefacto/runtime instalado, snapshots comparables ni evidencia de aislamiento. Por tanto, no se asignan IDs concretos por UE, no se completa el manifiesto por inferencia y no se declara intervención aislada ni primera etapa causal sobre accesibilidad.

Este ciclo cierra la reconciliación lógica del contrato material; no cierra la materialización de PB, C2, MD-C1/MD-C4, soporte ni el gate G-MAT.

## 2. Decisiones y contratos históricos reutilizados

| Fuente | Regla vigente reutilizada | No implica |
|---|---|---|
| DEC-C10-066/067 | D2 primario candidato; B_g0 no programa intento focal; B_g1 programa intento focal; intento, recepción, instalación y éxito se separan | Cumplimiento perfecto, éxito .80, A_f* o D_f* |
| DEC-C10-068/069 | Contrato funcional CMP/PAR/RUL e instancia ejemplar de referencia | Un instance_id común para todas las UE |
| DEC-C10-065/076 | Snapshot y referencias a revisiones exactas, sin resolver por latest | Que existan snapshots materiales C10-S |
| DEC-C10-079…083 | Identidad y aplicabilidad de PAR/CMP/RUL en U_G dentro de su alcance | IAM sellado, roster exhaustivo o parser ejecutable |
| DEC-C10-057…060/064 | Overlay IAM, boundary_class, semantic_role y anclaje de unidad | Nuevas tablas o captura observada |
| DEC-C10S-B1-UNIT-001 | Una entidad B1 por UE | Una solicitud, trayectoria o unidad de asignación por defecto |
| DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | Contrato/plantilla funcional común; instancia única por UE y versionado independiente | Aislamiento físico o asignación concreta de IDs |
| PROV-01…12 y B-M01…15 | Catálogo de superficies, dependencias, recursos, alternativas, rollback y no-afectación | Evidencia de que esas propiedades se cumplen |

No se reabren estas decisiones. Las interpretaciones históricas que contradigan su alcance se consideran subordinadas a la decisión aceptada aplicable, sin borrar su trazabilidad.

## 3. Identidad lógica y anclaje por UE

La identidad queda separada en cuatro niveles:

1. **Contrato funcional:** `contract_id=C10S-SVC-REQUEST-PROCESSOR`, `contract_version=1.0.0`, común mientras la semántica contractual sea la misma.
2. **Plantilla:** definición CMP/PAR/RUL común, versionada por contrato; no representa estado mutable compartido.
3. **Instancia:** cada UE tiene un `instance_id` único dentro del roster completo C10-S y una línea `instance_version` monotónica e independiente.
4. **Componente:** `component_id` es local a la instancia; la referencia inequívoca usa `(instance_id, component_id)`.

`C10S-SVC-REQUEST-PROCESSOR-001` permanece como instancia ejemplar documental de DEC-C10-069; no se replica como ID de todas las UE. Los IDs concretos se derivarán del roster cerrado y de su provenance. Este documento no fabrica roster, cardinalidad ni IDs.

**Distinción crítica:** la instancia lógica del servicio solicitante no es el adaptador/dependencia técnica focal que B intenta provisionar. El primero conserva el contrato funcional común; el segundo es un objeto técnico P1 de la intervención, con identidad, versión, dependencias y evidencia propias. No deben compartir identidad por conveniencia ni confundirse en CMP.

## 4. Frontera material P0/P1/P2 y contrato de D2

- **P0_CONFIG:** paquete declarativo CMP/PAR/REF/RUL/MET y sus propiedades funcionales basales. D2 no lo modifica.
- **P1_ENVIRONMENT:** runtime, adaptador/dependencia focal, interfaz técnica, entorno, ACL técnicas, cuotas y recursos de provisión. Es la superficie donde opera la política material D2.
- **DUAL_P0_P1:** solo cuando un artefacto indivisible contiene propiedades de ambas clases; debe justificarse y no se usa para evitar descomposición.
- **P2:** perímetro causal transversal, no valor de boundary_class; conecta intervención, agentes, recursos, rutas, medición y resultados.

B_g0 mantiene configuración basal y no programa ni inicia intento de provisión focal. Una provisión focal de fondo/crossover se registra como evento distinto, sin redefinir Z. B_g1 programa el intento de provisión focal usando artefacto/versión preidentificados; no garantiza inicio, recepción, instalación ni éxito. Ninguna política ejecuta F1/τ2, F2, A1 o A2.

La provisión no puede cambiar autorización normativa basal, datos fuente/destino, F*, oráculo, mapping semántico ni componentes alternativos. ACL/endpoints técnicos mínimos no equivalen a modificar C_auth,base. Si una superficie colateral cambia, se registra y modela; no se etiqueta el contraste como efecto puro de accesibilidad.

## 5. Crosswalk material integrado

| Objeto/registro | Identidad o contenido | Relación exigida | Estado material actual |
|---|---|---|---|
| UE | Unidad experimental según roster aprobado | Vincular a unidad de asignación y observación sin presumir igualdad | Roster no disponible en esta reconciliación |
| B1 | Una entidad solicitante-beneficiaria sintética por UE | Relación explícita UE↔B1 | Regla lógica aceptada; instancias no materializadas |
| Servicio CMP | Contrato/plantilla funcional común | CMP anchor exacto por snapshot/instancia | Semántica conocida; snapshots NONE |
| Instancia servicio | instance_id único por UE, instance_version | UE↔instancia con provenance y versión | IDs concretos pendientes |
| Adaptador/dependencia focal | Artefacto P1 separado del CMP servicio | B_g1 intenta provisionarlo; B_g0 no lo programa | No inventariado |
| IAM/U_G | NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y registros probatorios existentes | Claves y FKs exactas según DEC-C10-059/065/082 y plantilla vigente | Sin filas C10-S observadas |
| B-M01…15 | Superficies de provisión y cambio | Nodo/arista, consumidor, unidad, versión y ventana | No inventariado, salvo M13/M14 prohibidos como superficies modificadas por B |
| C_dep* | Instalación ∧ integridad ∧ compatibilidad ∧ operatividad | Evidencia separada por componente | No observado |
| A_f* | Predicados completos de accesibilidad focal | Identidad, relaciones, condiciones, autorización, recursos, dependencias y no-bloqueo | Truth/evidencia por unidad no materializados |
| D_f* | Apertura basal→post de la misma τ2 comparable | A_f,0*=0 y A_f,1*=1 con matching y snapshots válidos | No evaluable |
| ΔT_acc* | Cambio estructural completo | ΔU*, ΔR*, ΔC*, ΔX* con G/frontera/mapping fijados | No materializado |
| A1/A2 | Ruta alternativa baseline | Grafo, dependencias, recursos y comportamiento funcional pre/post B | No inventariado ni probado |
| F* / oráculo | Criterio y evaluador funcional inmutable | Versión exacta y cegamiento | No modificar por B; identidad/fixture material pendiente |

El roster mínimo de CMP/PAR/RUL ya descrito en el crosswalk de servicio no equivale al roster exhaustivo C_SRC por UE. No se infiere REF=0 ni cobertura COMPLETE.

## 6. Manifiesto B-M01…15 y regla de evidencia

Se reutiliza el manifiesto existente sin duplicarlo. B-M01…M12 y M15 conservan estado NO INVENTARIADO cuando no hay evidencia. B-M13 (oráculo/F*) y B-M14 (A1/A2) son superficies PROHIBIDAS EN B; cualquier cambio detectado se trata como desviación/amenaza a la validez, no como cumplimiento de la política.

Para cada superficie se exige, según aplicabilidad: identidad/version/hash/firma; origen/owner; dependencias transitivas y consumidores; permisos y credenciales (sin secretos en claro); recursos/cuotas/contención; red/canales; estado mutable; timestamps/ventanas; snapshot pre/post/rollback; cobertura y provenance.

Estados:
- `1`: cambio/propiedad presente o verificada con evidencia suficiente.
- `0`: ausencia/invariancia solo con universo y cobertura completos y criterio de verificación aplicable.
- `?`: desconocido, cobertura parcial, evidencia ausente/conflictiva o mapping insuficiente.

`NO INVENTARIADO`, `NONE`, `PARTIAL` o referencia inaccesible no son cero ni prueba de invariancia. Hash idéntico no prueba equivalencia funcional; nombre distinto no prueba independencia.

## 7. Snapshots, identidad y matching

Reutilizar el contrato de identidad/versionado y pinning exacto: cada objeto y relación observado debe resolver a snapshot y revisión exactos; no se permite resolver por latest, timestamp aproximado, nombre o fuzzy matching.

Mínimo conceptual de tiempos:
- basal/pre-Z: C_SRC, entorno, permisos, recursos, red, dependencias y rutas;
- post-provisión/pre-F1: estado resultante de B y evidencia de instalación;
- post-rollback: residuos y reversibilidad, si aplica;
- evaluación de rutas alternativas: comportamiento A1/A2 pre/post bajo condiciones comparables.

Los snapshots deben fijar unidad, instancia, contrato/versión, frontera, granularidad, catálogo, contexto, tiempo/ventana, mapping y provenance. Si no existe comparabilidad o mapping válido, el diff afectado es UNKNOWN/DIFF_NOT_COMPARABLE; no se calcula D_f* como transición de la misma τ2.

La captura y sellado material de estos snapshots no está autorizada por esta reconciliación.

## 8. Grafo de dependencias, aislamiento y vías colaterales

El grafo debe representar nodos y aristas tipados: llamadas, cargas, lecturas/escrituras, autenticación, validación, recursos compartidos, consumidores y dependencias externas. Debe incluir dependencias directas y transitivas, proveedor/versión y cobertura. Una lista de paquetes sin relaciones/consumidores no es suficiente.

La arquitectura sidecar/runtime separado, versión fijada, permisos mínimos, cuotas reservadas y canal restringido sigue siendo la candidata de menor riesgo, no una arquitectura aprobada ni evidencia de aislamiento.

Pruebas necesarias para sostener no-afectación:
- independencia de recursos y ausencia de contención que reduzca A1/A2/F2;
- no modificación de librerías/APIs/servicios compartidos críticos;
- permisos mínimos sin ampliar C_auth funcional;
- invariancia de configuración/datos/red y oráculo;
- equivalencia funcional de A1/A2 pre/post dentro de margen ex ante justificado;
- latencia, throughput, seguridad, calidad y rollback/residuos;
- ausencia de cambios diferenciales en información/conocimiento, incentivos, prioridad o selección.

Si no puede demostrarse la no-afectación, se conserva vía colateral/efecto de paquete y se bloquea la interpretación IV/exclusiva correspondiente. No se convierte un requisito de aislamiento en supuesto por estipulación.

## 9. Operacionalización de la política: campos aún no instanciados

DEC-C10-067 deja explícitamente pendientes: actor/rol ejecutor; artefacto, versión y hash; protocolo de recepción/aceptación; ventana temporal; reintentos, fallos parciales y rollback; detección de provisión de fondo en control; evidencia independiente de cada componente de C_dep*; inventario/cobertura de rutas alternativas y soporte.

Se conservan como campos obligatorios del futuro contrato operativo, pero sus valores permanecen OPEN. No se proponen nombres de actor, proveedor, runtime, formato, cuota, timeout, número de reintentos, tasa de éxito ni ventana por falta de base aprobada.

La secuencia que debe observarse por unidad es: Z/política asignada → intento programado → intento efectivo → recepción → instalación → verificación de instalación/integridad/compatibilidad/operatividad → C_dep* → A_f* → D_f* → ΔT_acc*/Reach/Π. Son estados distintos; no se imputan unos desde otros.

## 10. Consecuencias para C2, C3/C4 y estimandos

- ITT_Z^D2 sigue siendo efecto de asignación a la política/paquete, sujeto al cierre de unidad, asignación, población, Outcome y Value.
- C_dep* es éxito técnico de dependencia; no es primera etapa focal.
- A_f* requiere todos los predicados de accesibilidad aplicables.
- D_f* es la apertura basal→post; no se sustituye por intento, C_dep* ni D_f,obs.
- La primera etapa relevante para LATE_f es el contraste de D_f* bajo los supuestos IV, no el éxito técnico aislado.
- ΔT_acc* completo y Reach/Π deben mantenerse separados y medirse independientemente.
- Si B afecta recursos, permisos, información, coste, latencia, calidad, seguridad, alternativas o Outcome/Value por vías no mediadas por ΔT_acc*, se informa efecto de paquete o se aplica una estrategia identificadora justificada; no se atribuye a accesibilidad.
- D2→g^Af, soporte común, no interferencia, exclusión y mediación siguen sin demostrarse. s=0.80 permanece hipótesis no validada.

## 11. Matriz de cierre y criterios objetivos

| Gate | Condición documental/material | Estado actual |
|---|---|---|
| PB-I1 Identidad | Contrato/plantilla común e instancia única por UE | Lógica aceptada; IDs/roster material OPEN |
| PB-I2 IAM/C_SRC | Inventario por UE, coverage, snapshot exacto y provenance | BLOCKED: NONE |
| PB-I3 Provisión | B-M01…15 completos con evidencia y versiones | BLOCKED: NO INVENTARIADO |
| PB-I4 Dependencias | Grafo transitivo, consumidores, externos y frontera | BLOCKED: no materializado |
| PB-I5 Recursos/ACL | ACL efectivas, cuotas, recursos y no-afectación | BLOCKED: no medido |
| PB-I6 Alternativas | A1/A2 inventariadas y equivalencia funcional pre/post | BLOCKED: no probado |
| PB-I7 C_dep/A_f/D_f | Evidencia independiente por estado y predicado | BLOCKED: no observado |
| PB-I8 Snapshots/diff | Revisiones exactas, comparabilidad y mapping | BLOCKED: no capturados |
| PB-I9 D2 operativo | Actor, artefacto, recepción, ventana, reintentos, crossover | OPEN: parámetros no aprobados |
| PB-I10 Interferencia/soporte | Unidad/cluster, exposición y recursos compartidos | OPEN: no adjudicado |

El resultado actual es cierre de reconciliación documental y tipado de requisitos; los gates materiales no pasan.

## 12. Secuencia mínima de levantamiento de bloqueos

Cuando exista autorización específica para materializar el DGP, el orden de preparación será:

1. recuperar roster/definición de UE y unidad de asignación desde fuente aprobada;
2. asignar instance_id por UE y registrar contract/instance versions con provenance;
3. fijar frontera P0/P1/P2 y universo de cobertura antes de observar brazos;
4. construir IAM/U_G basal y snapshot C_SRC exacto;
5. definir e inventariar artefacto P1, runtime, permisos, recursos, red, dependencias y consumidores;
6. congelar protocolo de recepción/intento/fallos/rollback y detección de provisión de fondo;
7. capturar snapshots comparables pre/post/rollback y rutas alternativas bajo protocolo autorizado;
8. adjudicar C_dep*, A_f*, D_f* y ΔT_acc* con canales truth/evidence/evaluation segregados;
9. evaluar soporte, interferencia, vías colaterales y mapping B_D2→g^Af;
10. solo entonces reconsiderar G-MAT y los gates científicos/estadísticos relacionados.

Esta secuencia no autoriza ni ordena ahora la captura: enumera dependencias y condiciones futuras.

## 13. No-claims y autorización

No se afirma que exista una instancia material por UE, que el adaptador esté instalado, que el entorno sea aislado, que A1/A2 permanezcan invariantes, que C_dep*=1, que A_f*/D_f* se hayan abierto, que D2 sea instrumento válido o que el efecto de accesibilidad/mediación esté identificado.

No modifica Opción A, TGCV Core, RMA, Evidence→Claim Matrix, STATUS ni claims. No amplía el alcance de DEC-C10-069 ni las decisiones U_G/JCS locales. No define schema físico, formato de serialización, motor, API, parser, fixtures, datos, parámetros estadísticos o valores DGP.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`. No implementación, captura, fixtures, simulación, estimación o ejecución científica.
