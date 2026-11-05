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
