# C10-S — Perfil propuesto de frontera para el paquete de configuración de un servicio software

**ID:** C10-S-SERVICE-BOUNDARY-PROFILE-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA PARA DECISIÓN; no aprobada, congelada, implementada ni inventariada.  
**Base:** DEC-C10-051/052/053/055/056; contrato abstracto de instancia; contrato de frontera/granularidad; U_G §81–82; manifiesto B.

## 1. Propósito

Especializar el contrato genérico de frontera para el microdominio seleccionado: migración de configuración entre dos entornos software. El propósito es fijar qué constituye el objeto migrado, qué pertenece a los entornos de origen/destino y qué debe permanecer dentro de la frontera causal para analizar accesibilidad, rutas alternativas y posibles vías colaterales de B.

Este perfil no identifica una implementación real ni decide tecnologías, proveedores, formatos o componentes concretos. No convierte el catálogo U_G en inventario observado.

## 2. Regla central: tres perímetros anidados, no una frontera única

### P0 — Objeto de configuración migrable (C)

Es el paquete declarativo, versionado y atribuible a un servicio lógico concreto que expresa cómo debe quedar configurado ese servicio en un entorno. Comprende únicamente artefactos y registros que forman parte del contrato de configuración:

- CMP: componentes/configuración lógica del servicio incluidos en el paquete;
- PAR: claves y valores tipados, incluidos sus estados ABSENT/NULL/DEFAULT/VALUE;
- REF: referencias declaradas entre componentes o hacia recursos/servicios externos;
- RUL: reglas/restricciones declarativas que gobiernan validez o configuración;
- POL: módulo conceptual opcional, ausente por diseño en el núcleo confirmatorio mínimo;
- MET: identidad, versión, procedencia, mapping y trazabilidad.

C_src, C_dst_decl y C_dst_applied son estados/artefactos diferenciados. C_dst_applied se observa después de aplicar y no se presume equivalente a C_dst_decl.

### P1 — Envolvente de ejecución de cada entorno (E_src / E_dst)

Incluye condiciones necesarias para interpretar si el paquete puede configurarse, validarse y aplicarse en ese entorno, pero no se incorporan como contenido del paquete C salvo que un elemento se declare formalmente como configuración del servicio:

- aplicación/binario y versión del servicio;
- sistema operativo, runtime, contenedor/orquestación y librerías instaladas;
- infraestructura, capacidad y recursos disponibles;
- mecanismos efectivos de identidad, autenticación y autorización;
- estado operativo, conectividad, endpoints y disponibilidad;
- servicios externos y sus contratos/versiones;
- almacenamiento y estado externo preexistente;
- mecanismos de despliegue, carga y aplicación.

P1 se registra como contexto técnico versionado. Una REF en C puede apuntar a un recurso P1, pero no convierte el recurso, su disponibilidad ni su estado en parte del paquete.

### P2 — Sistema causal de la unidad experimental (U)

Incluye P0 y las dos envolventes P1, además de las rutas alternativas, procesos B, dependencias compartidas, agentes, mecanismos de observación, ejecución, Outcome y Value pertinentes al estimando. P2 se delimita para poder detectar:

- dependencias directas y transitivas;
- recursos, servicios o permisos compartidos;
- rutas focales, alternativas, fallback, manuales, externas y de recuperación;
- interferencia y exposición diferencial a B;
- vías B→Outcome/Value que no pasan por A_f*/ΔT_acc;
- posibles cambios de versión o contexto entre snapshots.

P2 es frontera analítica/causal, no el contenido que se migra.

## 3. Regla de inclusión y exclusión

Un elemento pertenece a P0 si cumple conjuntamente:
1. está declarado como parte del contrato de configuración del servicio;
2. tiene identidad/versión o pertenencia al paquete verificable;
3. su significado puede describirse mediante CMP/PAR/REF/RUL/POL/MET;
4. puede ser objeto de transformación/mapping entre fuente y destino;
5. su inclusión no requiere absorber el estado operativo del entorno.

Un elemento pertenece a P1 si es condición del entorno para interpretar compatibilidad, seguridad, disponibilidad, autorización, recursos o aplicación, pero no es contenido declarativo del paquete.

Un elemento pertenece a P2 si puede afectar asignación/provisión, accesibilidad, aplicabilidad, Reach, selección, ejecución, Outcome/Value, alternativas, interferencia o medición, aunque no pertenezca a P0/P1.

Si un elemento cumple más de un papel, se representa mediante registros/relaciones distintos (por ejemplo, REF declarada en P0 y recurso real apuntado en P1), sin duplicar su identidad ni confundir declaración con disponibilidad.

## 4. Casos límite y tratamiento propuesto

| Elemento | Tratamiento por defecto | Regla |
|---|---|---|
| Clave/valor de configuración propio del servicio | P0/PAR | Incluido si forma parte del contrato versionado |
| Endpoint/URI de servicio externo declarado en config | P0/REF o PAR; endpoint efectivo P1 | Separar valor declarado de resolución/disponibilidad real |
| Credencial/secret | Referencia/identificador en P0 si el contrato lo exige; material secreto fuera de P0 | No almacenar secretos reales en fixtures/documentos; disponibilidad/autorización efectiva en P1 |
| Política declarada de configuración | P0/POL solo en módulo secundario | No inferir autorización efectiva ni seguridad |
| Permisos efectivos/ACL/roles runtime | P1 | Registrar cambios y exposición a B; no confundir con POL declarada |
| Binario, librería, runtime, contenedor | P1 | Dependencia técnica/versionada, no paquete de configuración |
| Datos persistentes/estado de negocio | P1 o externo a unidad, según frontera | No migrar como configuración salvo decisión explícita que cambie el objeto |
| Esquema/contrato de configuración | MET/FP-01 en P0 | Distinguir esquema del paquete de software que lo interpreta |
| Scripts de transformación/mapping | Artefacto M/versionado y parte del protocolo de transformación, no contenido fuente C | Registrar código/versión/hash y efectos; no mezclar con paquete de entrada |
| Adaptador/sidecar provisionado por B | P2, componente de intervención/dependencia focal en P1 | No incluir en C_src/C_dst ni permitir que modifique F* u oráculo |
| Herramientas de exportación/importación alternativas A1/A2 | P2; dependencias P1 si instaladas | Evaluar funcionalidad y substituibilidad respecto del mismo F* |
| Logs/telemetría/oráculo | P2, medición/procedencia | No incorporarlos al objeto migrado ni revelar Outcome a adjudicadores cegados |

Los casos límite deben resolverse en el IAM y manifiesto de frontera antes de Z/B. Si la clasificación es incierta, registrar ? y conservar el elemento dentro de P2 como posible vía causal; no excluirlo por conveniencia.

## 5. Unidad experimental y snapshots

La unidad experimental candidata es una instancia completa de migración: un paquete C_src versionado, un entorno fuente E_src, un entorno destino E_dst, un mapping M fijado, un estado inicial S0 y una frontera P2 delimitada. La decisión final sobre unidad experimental/analítica debe reconciliarse con los estimandos y el diseño de interferencia; este perfil no la fija universalmente.

Snapshots mínimos conceptuales:
- baseline pre-Z/B: C_src, E_src, E_dst, permisos, recursos, servicios y rutas;
- post-provisión/pre-accesibilidad: cambios causados por B y sus dependencias;
- post-transformación: C_dst_decl y mapping aplicado;
- post-aplicación: C_dst_applied y estado observado de E_dst;
- rollback/final: residuos y reversibilidad, si aplica.

Cada snapshot debe identificar versiones, timestamps, fuente, hashes, cobertura y limitaciones. Capturar snapshots reales requiere autorización operativa específica; esta propuesta no la autoriza.

## 6. Consecuencias para F* y las medidas TGCV

- F* se evalúa sobre la ruta completa de producir y aplicar una configuración funcional en destino, bajo criterios declarados ex ante.
- FP-01/02/03 se evalúan principalmente sobre C y M.
- FP-04/05/06/07 cruzan C con E_dst y el estado aplicado: compatibilidad, seguridad efectiva, aplicación y verificación.
- FP-08 preserva trazabilidad de C, M, E, snapshots y oráculo como gate probatorio separado.
- REF declarada no prueba que el recurso exista o esté disponible.
- C_dep no prueba por sí solo A_f*.
- A_f* no equivale a App, Reach, selección ni ejecución.
- Un cambio en P1 puede abrir/bloquear accesibilidad sin cambiar C; un cambio en C puede no cambiar Reach si existen rutas alternativas.
- La valoración Value permanece separada del Outcome y no forma parte del contrato de configuración.

## 7. Regla de frontera causal para B

Para evaluar si B actúa principalmente mediante accesibilidad focal:
1. comparar P2 pre/post B, no solo el paquete adaptador;
2. inventariar dependencias transitivas del adaptador y recursos/servicios compartidos;
3. verificar si B cambia permisos efectivos, recursos, estado, conocimiento, latencia, observabilidad, alternativas o condiciones de ejecución;
4. preservar A1/A2 y rutas externas como nodos explícitos;
5. clasificar cualquier vía no descartada como posible vía colateral, no como inexistente;
6. si no puede defenderse exclusión, reportar ITT del paquete/política y no atribuir automáticamente el efecto a A_f*.

## 8. Decisiones aún necesarias

1. Aceptar o modificar P0/P1/P2 como arquitectura de frontera.
2. Definir qué se considera “servicio lógico” y si una instancia o un conjunto de servicios forma la unidad.
3. Resolver si deployment manifests y variables de entorno forman P0 o P1 según su semántica declarativa.
4. Fijar política de secretos y referencias sensibles.
5. Fijar tratamiento de datos persistentes, estado externo y migraciones de esquema.
6. Delimitar servicios externos opacos y evidencia mínima observable.
7. Resolver si la unidad experimental es una instancia, un par de entornos o un clúster cuando haya recursos compartidos.
8. Concretar snapshots, versiones y cobertura permitida antes de Z/B.

## 9. Dictamen

Se propone una separación en tres perímetros: paquete migrable P0, envolvente técnica P1 y sistema causal P2. La arquitectura mantiene el objeto de configuración acotado sin perder dependencias, rutas alternativas y vías colaterales relevantes para C10-S.

**Estado:** propuesta documental; no aceptada ni congelada. No hay inventario real ni evidencia de que un componente concreto pertenezca a cada perímetro. No se han generado instancias, truth o fixtures; no se ha ejecutado validación, instalación, simulación ni experimento. scientific_execution=false; execution_authorized=false.


## 10. Aceptación arquitectónica — DEC-C10-057

La arquitectura P0/P1/P2 y la clasificación por función semántica han sido aceptadas mediante DEC-C10-057. P0 es el paquete declarativo migrable; P1 es la envolvente técnica de los entornos; P2 es la frontera causal transversal que conserva dependencias, alternativas, intervención y vías hacia Outcome/Value. La aceptación no resuelve automáticamente la clasificación concreta de cada elemento ni congela el perfil como schema.

El documento complementario `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md` desarrolla la unidad candidata de servicio lógico y las reglas campo a campo para manifiestos, variables, secretos, estado persistente, servicios externos, mapping, sidecar y oráculo. Permanece como propuesta pendiente de revisión/decisión.


## 10. Reconciliación con DEC-C10-058

La unidad de migración queda delimitada como una instancia lógica de servicio software, no necesariamente coincidente con proceso, microservicio, binario o unidad de despliegue. P0/P1 se clasifican por semántica y P2 conserva la frontera causal transversal. Véase DEC-C10-058 en el Decision Log y el documento de unidad lógica. La aceptación no crea inventario real ni congela schema técnico.
