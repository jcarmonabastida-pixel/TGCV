# C10-S — Unidad de servicio lógico y clasificación de frontera

**ID:** C10-S-LOGICAL-SERVICE-UNIT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA DOCUMENTAL; no aprobada ni congelada.  
**Arquitectura de perímetros:** DEC-C10-057 (aceptada).  
**Base:** contrato abstracto de instancia; perfil P0/P1/P2; contrato de frontera/granularidad; U_G; estimandos C10-S.

## 1. Decisión de diseño que se propone

Delimitar el objeto como **una instancia lógica de un servicio software**, identificada por un contrato funcional y un contrato/versionado de configuración, migrada entre un entorno fuente y uno destino. No se toma como unidad un sistema empresarial completo, una plataforma, un clúster heterogéneo ni un conjunto arbitrario de microservicios.

La unidad candidata se representa como U_i = (L_i, C_src,i, E_src,i, E_dst,i, M_i, S_0,i, P2_i), donde L es la identidad/contrato del servicio lógico; C_src el paquete fuente; E_src/E_dst los entornos; M mapping fijado; S0 estado inicial; P2 frontera causal. Esta notación no decide todavía la unidad de aleatorización ni resuelve interferencia: si hay recursos o servicios compartidos, la unidad causal/analítica puede requerir clúster o mapa de exposición.

## 2. Definición operativa de servicio lógico

Un servicio lógico es una capacidad software identificable que:
1. ofrece una función/contrato de servicio distinguible para un consumidor o sistema;
2. posee identidad estable dentro del estudio, independiente de host, pod, contenedor o ubicación;
3. tiene un contrato de configuración identificable y versionable;
4. puede describirse con entradas/salidas y restricciones funcionales observables;
5. puede asociarse a un entorno fuente y uno destino sin absorber automáticamente toda la plataforma.

No se exige que el servicio sea un microservicio, proceso único, binario único o unidad de despliegue. Una aplicación monolítica puede contener más de un servicio lógico si sus contratos y configuraciones son separables; varios procesos pueden implementar un único servicio lógico si el contrato funcional/configuracional es uno. Esa decisión debe justificarse ex ante.

## 3. Criterio de inclusión en P0/P1/P2

Clasificar cada elemento por su función semántica, no por el formato, extensión, ubicación física o herramienta que lo almacena.

### 3.1 P0 — Declaración de configuración del servicio

Incluye un elemento si expresa el estado deseado/configurable del servicio y forma parte del contrato versionado migrable:
- parámetros de aplicación y sus valores tipados/estados;
- referencias declaradas a endpoints, colas, bases de datos, certificados o secretos;
- reglas/restricciones declarativas;
- manifiestos de despliegue solo en los campos que declaran configuración propia del servicio;
- variables de entorno solo cuando sean parámetros declarativos del servicio incluidos en el contrato;
- esquema/descriptor del paquete y metadatos contractuales.

La inclusión en P0 no implica que el valor sea seguro, que la referencia resuelva ni que el destino soporte su semántica.

### 3.2 P1 — Realización técnica y estado del entorno

Incluye elementos que realizan, alojan, interpretan o condicionan el servicio:
- runtime, binario, imagen, sistema operativo, librerías, orquestador y capacidad;
- réplicas, pods, hosts, redes, almacenamiento y estado operativo;
- permisos efectivos, identidades, ACL y políticas aplicadas por runtime;
- disponibilidad/resolución efectiva de endpoints y servicios externos;
- material secreto real, claves privadas, tokens y credenciales;
- valores inyectados por el entorno que no formen parte del contrato de configuración del servicio;
- datos persistentes, estado de negocio, colas y bases de datos;
- mecanismos de despliegue, importación, activación y rollback.

### 3.3 P2 — Dependencias y vías causales

Todo elemento P0/P1 se incluye en P2 en cuanto pueda afectar la intervención, accesibilidad, aplicabilidad, Reach, alternativas, selección, ejecución, Outcome, Value o medición. También se incluyen agentes, procesos manuales, fallback, proveedores opacos, recursos compartidos, canales, sidecar B y oráculo.

P0/P1 clasifican objeto y contexto; P2 es la frontera analítica que conserva relaciones causales y no debe tratarse como una tercera caja mutuamente excluyente.

## 4. Casos especiales

| Elemento | Regla propuesta |
|---|---|
| Deployment manifest | Clasificación campo a campo: desired state/configuración propia del servicio → P0; placement, recursos, replicas, runtime, scheduling y wiring de plataforma → P1; todo lo que afecte a B/rutas/Outcome → también P2 |
| Variables de entorno | P0 si la clave/valor pertenece al contrato versionado del servicio; P1 si lo inyecta la plataforma/secret store o es estado ambiental; conservar mapping y fuente |
| Secretos | P0 solo referencia/identificador/versión y requisito; valor secreto real siempre P1; no registrar valores reales en documentación/fixtures |
| Datos persistentes | Fuera de P0 por defecto; P1 si su estado afecta el comportamiento de la migración; P2 si es vía causal o fuente de interferencia |
| Migraciones de esquema de datos | Artefacto/proceso separado, fuera de F* base de configuración; incluir en P2 y registrar como cointervención si B o la ruta lo activa |
| Endpoint externo | P0 contiene declaración/reference; P1 contiene endpoint resuelto, disponibilidad, credenciales y contrato externo; P2 conserva dependencia y fallback |
| Identidad/permisos | POL declarada opcional en P0; autorización efectiva y ACL en P1; sus cambios por B quedan explícitos en P2 |
| Mapping/script | Artefacto M controlado y versionado, separado de C_src; su ejecución/entorno pertenece a P1/P2 según efecto |
| Sidecar/adaptador B | P2 como componente de intervención y P1 como dependencia técnica instalada; nunca se confunde con configuración fuente ni se omite del grafo transitivo |
| Oráculo/logs | P2; acceso, cegamiento y potencial filtración de Outcome documentados |

## 5. Regla para servicios externos y opacos

Un servicio externo no se excluye solo por ser opaco. Se registra como nodo P2 y dependencia P1 con identidad/contrato/versión conocidos, interfaz observable, condiciones de acceso, evidencia disponible de disponibilidad/compatibilidad/permisos, límites de observabilidad, rutas fallback y estado ? para predicados no verificables. No inferir ausencia de dependencia, equivalencia funcional ni seguridad por falta de visibilidad.

## 6. Unidad experimental y no interferencia

La unidad candidata es un caso de migración de un servicio lógico entre dos entornos, con paquete fuente, mapping y estado inicial fijados. No se adopta automáticamente como unidad de aleatorización. Antes de fijarla deben resolverse exclusividad/compartición de entornos, recursos, identidad, base de datos, red, orquestador o canales; afectación de B a otras unidades; rutas alternativas compartidas; y si procede aleatorización individual, por clúster o estimando bajo exposición.

La presencia de interferencia no justifica ampliar P0; exige ampliar/estructurar P2 y el diseño causal.

## 7. Evidencia y sellado ex ante

Antes de Z/B, IAM debe registrar por elemento: identificador, clase P0/P1 y relaciones P2; servicio lógico/contrato; criterio semántico de inclusión/exclusión; versión, origen, owner y fuente; sensibilidad y tratamiento de secretos; dependencia directa/transitiva/compartida; cobertura y evidencia; justificación de exclusiones y estado de incertidumbre.

Los manifiestos y variables de entorno se descomponen por campos/keys; no se clasifican enteros por extensión. Los secretos se registran por referencia sin copiar material sensible.

## 8. Recomendación y cuestiones abiertas

Se recomienda adoptar esta definición operativa de servicio lógico y las reglas semánticas de clasificación, sujeto a aprobación del usuario. Permanecen abiertos: cardinalidades máximas, taxonomía de clases CMP, lista de claves PAR, contratos de REF/RUL, tratamiento concreto de schema migration, unidad de aleatorización y diseño de interferencia.

## 9. Estado

Propuesta documental para decisión. No contiene inventario real, instancias, valores, truth, fixtures, schema ejecutable ni validación. No autoriza instalación, acceso a sistemas, generación de datos ni experimento. scientific_execution=false; execution_authorized=false.


## 10. Resolución de la propuesta — DEC-C10-058

El usuario acepta la definición operativa de servicio lógico y las reglas semánticas P0/P1/P2. La propuesta queda aceptada como contrato conceptual de clasificación y unidad de migración, sin convertirla en inventario o schema ejecutable.

Se mantienen expresamente abiertas la unidad de aleatorización/analítica, la estructura concreta de IAM, las cardinalidades y los dominios detallados CMP/PAR/REF/RUL, y la identificación de servicios/entornos reales. La decisión no autoriza acceso a sistemas, captura de snapshots, instalación ni ejecución científica.


## 10. Resolución de la propuesta — DEC-C10-058

El usuario acepta la definición operativa de servicio lógico y las reglas semánticas P0/P1/P2. La propuesta queda aceptada como contrato conceptual de clasificación y unidad de migración, sin convertirla en inventario o schema ejecutable.

Se mantienen expresamente abiertas la unidad de aleatorización/analítica, la estructura concreta de IAM, las cardinalidades y los dominios detallados CMP/PAR/REF/RUL, y la identificación de servicios/entornos reales. La decisión no autoriza acceso a sistemas, captura de snapshots, instalación ni ejecución científica.

## 11. Continuidad del inventario U_G

La operacionalización posterior reutiliza la plantilla U_G de diez registros. Véase `C10_S_IAM_SERVICE_BOUNDARY_OVERLAY_AND_CROSSWALK_DRAFT_001.md`. No se crea un inventario paralelo ni se considera que la aceptación de la unidad lógica haya generado instancias técnicas observadas.
