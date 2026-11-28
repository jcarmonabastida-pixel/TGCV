# C10-S — Contrato de frontera del sistema y granularidad del grafo

**ID:** C10-S-BOUNDARY-GRANULARITY-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05
**Estado:** DRAFT / NO APROBADO / NO CONGELADO / NO IMPLEMENTADO / NO EJECUTADO.

## 1. Propósito y dictamen

Este contrato define cómo delimitar la unidad/sistema, descomponer el grafo en nodos y aristas, identificar dependencias directas y transitivas, evaluar rutas funcionalmente substituibles, clasificar servicios externos y recursos compartidos, tratar versiones/cambios materiales y declarar cobertura. No afirma que el inventario técnico real de la Opción A esté completo.

U_G de §81 (23 roles de nodo y 23 aristas candidatas) es un catálogo de inspección, no un inventario observado ni prueba de exhaustividad. Los estados técnicos siguen indeterminados; donde no hay fuentes observadas la cobertura es NONE. Opción A y la arquitectura sidecar siguen siendo candidatas, no aprobadas. Este documento no autoriza instalación, implementación, simulación ni ejecución.

## 2. Criterios de independencia de nodos

Representar un elemento como nodo separado cuando tenga al menos una diferencia relevante en: intervención/cambio; identidad o versión; fallo o sustitución; interfaz; permisos; recursos; exposición causal; ruta afectada; fuente de evidencia. No separar por mero nombre, archivo, hash, paquete o despliegue si la función e identidad son equivalentes. Aplicar TID/SID/RID/EID para distinguir identidad semántica, versión de especificación, realización técnica y evento.

Agregar elementos solo si comparten función, ciclo de intervención, condiciones de fallo, exposición, recursos y evidencia, y la agregación no oculta una vía diferencial ni una ruta alternativa. Si no puede decidirse, mantener nodos separados o clasificar ?. La granularidad debe ser suficiente para detectar si B afecta de modo distinto a la ruta focal y a A1/A2.

## 3. Clases y aristas

Clases mínimas: sistema/unidad; asignación/política; componente focal; componente alternativo; componente compartido; canal/interfaz; condición/autorización; recurso; datos/estado; servicio externo; oráculo/medición; agente/observación; ejecución/Outcome/Value.

Cada arista registra origen, destino, tipo, dirección, tiempo, condición, brazos afectados, versión, evidencia, cobertura y si es necesaria para una ruta. Tipos mínimos: depende_de; carga/ejecuta; invoca/expone; autoriza; asigna/consume_recurso; transforma/entrega; lee/escribe_estado; comparte; observa/mide; controla/valida; comunica_con; provisiona; afecta/puede_afectar; sustituye_funcionalmente.

## 4. Dependencias

- Directa: relación inmediata demostrada por configuración, interfaz, importación, enlace, montaje, permiso, flujo de datos o consumo de recurso.
- Transitiva: cadena dirigida de una o más dependencias directas.
- Compartida: elemento en el cierre de dependencias de dos o más rutas/componentes.
- Crítica compartida: dependencia común cuyo fallo/cambio puede bloquear o alterar rutas.
- Independiente respecto de B: no modificada, provisionada, configurada, autorizada, priorizada ni afectada por B en alcance y horizonte declarados. Requiere evidencia pre/post y análisis transitivo; separar procesos no basta.

Construir cierre transitivo sobre grafo dirigido y versionado. Registrar ciclos, resolución dinámica, carga tardía y fallback. Una dependencia no resuelta se representa como nodo desconocido; nunca se interpreta como ausencia.

## 5. Substituibilidad funcional

Una ruta es substituible respecto de F* si, desde entrada admisible común y bajo mismo contexto C0, horizonte H, granularidad G y restricciones, alcanza resultado que satisface el mismo criterio F* con tolerancias y evidencia equivalentes, evaluado por oráculo independiente común. Evaluar cobertura de entradas, salida/tolerancias, integridad/compatibilidad, seguridad/permisos/recursos, tiempo, dependencias compartidas/externas e identidad/versiones.

Una ejecución exitosa aislada o una etiqueta funcional similar no demuestra substituibilidad. Codificación: 1 respaldada; 0 descartada con cobertura suficiente; ? indeterminada. F_alt,0=0 exige descartar todas las rutas substituibles dentro del universo declarado. Búsqueda finita no prueba por sí sola exhaustividad del catálogo.

## 6. Servicios externos y recursos compartidos

Servicio externo: operación, administración o ciclo de cambio fuera de la frontera de control declarada; ubicación/proveedor por sí solos no bastan. Registrar propietario, interfaz/protocolo/versión, identidad y permisos, dependencias, datos/estado, disponibilidad, latencia, cuotas, ventanas, cambios, observabilidad y exposición diferencial a B. Si es opaco, modelarlo como caja negra con contrato observable y nodo EXT_UNKNOWN; la opacidad no demuestra ausencia de vías colaterales.

Separar recursos en: (1) capacidad instalada; (2) disponibilidad compartida temporal; (3) reserva/asignación a unidad/ruta; (4) consumo durante ejecución. Solo niveles 1–3 pueden ser condiciones de accesibilidad según el reloj causal. Registrar capacidad, propietario, cuota, prioridades, concurrencia, contención y brazos expuestos. Recursos compartidos pueden generar interferencia o vía B→Outcome/Value ajena a A_f*.

## 7. Versiones y cambios materiales

Un cambio de hash/build no implica nueva identidad. Es material si altera función, contrato entrada/salida, precondiciones esenciales, composición, permisos, perfil de recursos, fallos o criterio de resultado de forma relevante para rutas/estimandos. Crear snapshot nuevo y evaluar continuidad. Si equivalencia incierta, ?. No mezclar versiones entre brazos sin modelar el régimen de versiones.

## 8. Universo y cobertura

Declarar unidad/frontera, microdominio/F*, entrada/S0, rutas focales/alternativas, G, C0, versiones/periodo, H/ventanas, recursos, permisos, dependencias, servicios externos, fuentes y adjudicación. Informar cobertura por dimensión: componentes/paquetes; dependencias directas; transitivas/carga dinámica; interfaces; datos/estado; permisos; recursos; alternativas; servicios externos; tiempo/versiones; observabilidad; evidencia/adjudicación.

COMPLETE significa cobertura suficiente del universo operativo declarado, con excepciones resueltas; PARTIAL indica segmentos/versiones/dependencias sin cubrir; NONE indica ausencia de inspección sistemática. COMPLETE no es exhaustividad ontológica absoluta y siempre debe calificarse por universo, versión, contexto y horizonte. MISSING/NO INVENTARIADO no equivale a 0; PARTIAL no equivale a COMPLETE.

## 9. Protocolo de inventario

1. Declarar alcance candidato; si F* o microdominio no están fijados, mantener el inventario preliminar.
2. Capturar baseline mediante snapshots inmutables de paquetes, runtime, procesos, configuración, permisos, red, recursos, datos, servicios y rutas, con fecha, origen, hash y limitaciones.
3. Enumerar dependencias mediante manifiestos, lockfiles/SBOM, análisis estático, configuración, importaciones, carga dinámica, llamadas, trazas, permisos y documentación de proveedor. Ninguna fuente aislada prueba completitud universal.
4. Construir grafo normalizado/versionado, añadir aristas directas, inferidas y desconocidas, calcular cierre transitivo y marcar ciclos/elementos compartidos.
5. Enumerar rutas focales, alternativas, nativas, fallback, manuales, externas, compartidas y de recuperación; evaluar contra F* común.
6. Comparar snapshots post-B y rollback, registrando residuos y efectos sobre alternativas, permisos, recursos, estado y observabilidad. Rollback no se presume perfecto.
7. Dos evaluadores clasifican nodos, aristas, dependencias, alternativas y cobertura sin Outcome/Value; conservar discrepancias y adjudicación.
8. Para cada ?, registrar fuente faltante, impacto, posible resolución y condición de parada. Si no se resuelve, conservar ? y limitar la afirmación.

El protocolo especifica evidencia requerida; no autoriza capturar snapshots reales ni instalar software.

## 10. Registro y reglas de parada

Cada nodo/arista/ruta debe registrar ID, identidad/versión, clase, función, frontera, relaciones, dependencias, rutas/brazos, tiempo, recursos/permisos, estado 1/0/?, cobertura, evidencia/procedencia, evaluador/cegamiento e impacto en A_f*, App, Reach, F_alt, exclusión/interferencia.

Si hay dependencia crítica desconocida, no declarar independencia. Si B puede afectar permisos, recursos, servicios, datos, seguridad, latencia, observabilidad o alternativas, mantener abierta la vía colateral. Si una alternativa no puede descartarse con cobertura suficiente, F_alt,0=? y no seleccionar automáticamente P*_F. Si cobertura parcial o Runknown, no declarar Reach_H=0. Si recursos compartidos permiten interferencia, revisar unidad/cluster y estimandos. Si no se demuestra que B difiere solo por accesibilidad, el resultado sigue siendo ITT de política/paquete, no efecto atribuible a A_f* ni LATE focal.

## 11. Estado y pendientes

Dependencias directas/transitivas, endpoints externos, recursos y cambios materiales reales no están inventariados. Independencia A1/A2 respecto de B no demostrada. Cobertura técnica NONE donde no hay fuentes. A_f*, F_alt,0 y Reach_H permanecen ?. Siguen abiertos MD-C1…6, AUD-005/007/010/011, OPEN-C10-001/003/005/007, precedencia D1/D2, q*, G/H, Value y dimensionamiento.

Siguiente operación documental: crear plantilla de registro que instancie U_G sin inventar estados técnicos y mapear fuentes, suficiencia y límites por dimensión.
