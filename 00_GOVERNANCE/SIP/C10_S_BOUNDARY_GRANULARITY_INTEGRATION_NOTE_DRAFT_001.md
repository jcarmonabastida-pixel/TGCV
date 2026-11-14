# C10-S — Registro de integración del contrato de frontera y granularidad

**ID:** C10-S-BOUNDARY-INTEGRATION-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05
**Estado:** DRAFT / REGISTRO DOCUMENTAL; no implica aprobación científica.
**Rama:** research/c10-s-consolidation-draft · **PR:** #116

## 1. Artefacto incorporado

Se añade el contrato C10-S-SYSTEM-BOUNDARY-AND-GRANULARITY-001: `00_GOVERNANCE/SIP/C10_S_SYSTEM_BOUNDARY_AND_GRAPH_GRANULARITY_CONTRACT_DRAFT_001.md`.

## 2. Reconciliación con el estado previo

El contrato desarrolla el universo candidato U_G de la sección 81 y el manifiesto B de la sección 80. No sustituye ninguno de ellos ni convierte el catálogo de 23 roles de nodo y 23 aristas en un inventario real. Conserva los estados técnicos indeterminados y la cobertura NONE cuando no existe evidencia inspeccionada. No presume independencia de A1/A2, exclusión de B, exhaustividad de rutas ni primera etapa sobre A_f*.

## 3. Integraciones lógicas requeridas

- **Maestro C10-S:** registrar como sección 82, después de §81, el alcance, dictamen, reglas de frontera/granularidad, protocolo de inventario y estado abierto descritos en el contrato.
- **DGP temporal y de roles:** incorporar una sección de frontera/dependencias que remita al contrato y prohíba interpretar MISSING/NO INVENTARIADO como ausencia; exigir cierre transitivo y clasificación explícita de servicios externos/recursos compartidos.
- **Plan de cierre:** registrar Bloque 9 (frontera, granularidad e inventario), con resultado documental y pendientes MD-C1…6, AUD-005/007/010/011 y OPEN-C10-001/003/005/007.

Estas tres integraciones son una especificación de reconciliación. En este commit no se han modificado los tres documentos de destino: los intentos de actualización de los archivos extensos fueron bloqueados por controles de la herramienta. Por tanto, no afirmar que §82, DGP §9 o Plan IX ya están escritos en esos archivos. Este registro preserva el vínculo y evita presentar una integración parcial como completa.

## 4. Estado científico y operativo

El contrato y este registro son DRAFT. No se ha inventariado una implementación concreta, no se han capturado snapshots, no se ha instalado software, no se han ejecutado pruebas ni simulaciones y no se ha autorizado experimento. Opción A y sidecar siguen siendo candidatos. A_f*, F_alt,0 y Reach_H permanecen indeterminados. No hay cierre de los gates MD-C1…6 ni de auditorías abiertas.

## 5. Siguiente paso

Crear una plantilla de registro para U_G §81, sin completar valores técnicos no observados, y reconciliarla con el contrato de cobertura. Después, integrar de forma controlada las referencias de §82/DGP/Plan cuando la vía de edición del maestro extenso permita una actualización verificable.


## 6. Addendum de reintento de integración (2026-11-05)

Se releyeron 00_GOVERNANCE/README.md y el bootstrap canónico desde main, así como el maestro, DGP, plan, contrato de frontera, inventario finito, matriz de cobertura y matriz de cierre desde research/c10-s-consolidation-draft. El bloqueo previo no se reproduce en este reintento.

**Corrección de numeración tras inspección de los archivos vigentes:** el maestro pasa de §81 a §82; el DGP ya contiene §§1–40 y recibe §41 (no §9); el plan ya contiene bloques I–XIX y recibe XX (no IX). La referencia §9 / IX del cuerpo original de esta nota se conserva como registro histórico de la intención errónea y queda corregida por este addendum.

Se han actualizado físicamente los tres documentos de destino con sus secciones correspondientes. La plantilla de inventario U_G se registra como artefacto separado. Se verificará cada escritura mediante recuperación posterior y hash/blob SHA; si alguna actualización no se recupera exactamente, no se declarará integrada.

La integración es documental y DRAFT. No cambia la verdad técnica ni los estados de evidencia: no hay inventario real, cobertura NONE donde no hay inspección, y A_f*, F_alt,0 y Reach_H permanecen ?. No se ejecuta validación local porque el entorno local no está cargado en esta sesión; tampoco se ejecuta experimento ni simulación.


## 7. Verificación post-write (2026-11-05)

La recuperación posterior confirmó la presencia de §82 en el maestro (blob f8ffe74bbaea56545ae4b0634dce98febcb00bfd), §41 en el DGP (blob 350dadb00bacbf7dda1d30f923cbb6989d1cf9a2) y bloque XX en el plan (blob 120ed13329825865eac57dca40e35d95bbac3398). La plantilla U_G se creó y recuperó (blob 5ef40361a2a17ad846d67b08ee54ac17ac6f171b). Las referencias anteriores de §3 y §5 que afirmaban que esas integraciones seguían bloqueadas quedan históricamente preservadas, pero supersedidas por este addendum y su verificación.

La plantilla se ha propagado además a maestro §83, DGP §42, plan XXI, matriz de cierre §21, Decision Log §37 (DEC-C10-043 propuesta) y registro de pruebas §44. La integración sigue en Draft y no acredita inventario, evidencia técnica ni ejecución.
