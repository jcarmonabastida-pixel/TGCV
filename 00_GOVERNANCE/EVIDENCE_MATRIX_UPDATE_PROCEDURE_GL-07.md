# GL-07 — Procedimiento sencillo para actualizar las matrices de evidencia

**Estado:** PERSISTIDO — regla operativa de governance  
**Ámbito:** `EVIDENCE_TO_CLAIM_MATRIX` y sus versiones acumulativas  
**Propósito:** evitar pérdida de evidencia, deriva de versiones, inconsistencias de punteros y acumulación indebida del historial de novedades en la cabecera.

## 1. Regla fundamental

Cada nueva versión de la matriz se construye como:

> **versión predecesora íntegra + cambios aditivos explícitos y autorizados.**

Esto implica dos comportamientos distintos que deben mantenerse separados:

- **Contenido evidenciario = acumulativo.** La nueva versión conserva íntegramente el contenido material de la versión anterior y añade únicamente la evidencia, modificaciones o cualificaciones autorizadas en el nuevo ciclo.
- **Trazabilidad de novedades de versión = no acumulativa.** Los elementos `X update` de la cabecera describen únicamente las novedades introducidas por **esa versión concreta**. Los `X update` de versiones anteriores no se copian a la cabecera de la nueva versión; permanecen registrados en sus respectivas versiones históricas.

Esta distinción es obligatoria y evita que la cabecera se convierta en un historial acumulativo de todos los experimentos y cambios anteriores.

## 2. Procedimiento operativo en 6 pasos

### Paso 1 — Congelar y preservar la versión anterior

Tomar como base la versión canónica inmediatamente anterior y conservarla íntegramente como artefacto histórico inmutable. No editar retrospectivamente una versión ya cerrada.

### Paso 2 — Crear la nueva versión como copia acumulativa

Crear la siguiente versión a partir de una copia completa de la versión anterior. La nueva versión debe conservar todo el contenido evidenciario previo.

### Paso 3 — Añadir únicamente los cambios autorizados del ciclo

Incorporar exclusivamente las nuevas evidencias, rutas a claims, cualificaciones, correcciones o modificaciones expresamente autorizadas en el ciclo actual. No cambiar niveles de claim, estados o interpretaciones por efecto de una mera actualización documental salvo que exista autorización específica para ello.

### Paso 4 — Actualizar la cabecera únicamente con las novedades actuales

Reescribir la sección de `X update` de la cabecera para que contenga **solo** las novedades de esta versión. No arrastrar los `X update` de la versión anterior ni de versiones más antiguas.

La cabecera es metadato de trazabilidad del ciclo de versión; no es un repositorio acumulativo de evidencia histórica.

### Paso 5 — Actualizar el puntero de versión actual

Actualizar `EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` para que apunte al contenido completo de la nueva versión canónica. El alias/puntero actual debe corresponder exactamente a la versión que acaba de cerrarse.

### Paso 6 — Verificar preservación y consistencia antes de cerrar

Comprobar, como mínimo:

1. que todo el contenido material de la versión anterior sigue presente;
2. que las nuevas adiciones están explícitamente identificadas;
3. que la cabecera contiene solo los `X update` del ciclo actual;
4. que no se ha producido ningún cambio no autorizado en niveles, estados o claims;
5. que el puntero `CURRENT` apunta exactamente a la nueva versión;
6. que la versión anterior permanece intacta y recuperable.

Solo después de esta verificación se considera cerrada la actualización de la matriz.

## 3. Regla de control de cabecera

La siguiente formulación debe tratarse como regla canónica:

> **Contenido evidenciario acumulativo; trazabilidad de novedades de versión no acumulativa.**
>
> El contenido material de evidencia se hereda íntegramente entre versiones. Los `X update` de la cabecera representan exclusivamente el ciclo de novedades de la versión actual y no se heredan de versiones anteriores.

## 4. Qué NO hacer

- No reconstruir una nueva matriz desde cero a partir de un resumen.
- No copiar mecánicamente el historial completo de `X update` a la nueva cabecera.
- No eliminar evidencia histórica para simplificar la nueva versión.
- No modificar retrospectivamente una versión cerrada.
- No cambiar niveles de claim únicamente porque se haya incorporado nueva evidencia documental, si el artefacto de propagación no autoriza expresamente ese cambio.
- No declarar una nueva versión canónica mientras el puntero `CURRENT` o la preservación del predecesor no hayan sido verificados.

## 5. Regla práctica para futuras actualizaciones

Ante cualquier nueva evidencia que deba incorporarse a la matriz, la secuencia por defecto es:

**predecesor íntegro → copia acumulativa → adiciones autorizadas → cabecera solo con novedades actuales → puntero CURRENT → verificación de preservación y consistencia → cierre.**

Esta regla constituye el procedimiento operativo sencillo para evitar iteraciones innecesarias y mantener la matriz canónica reproducible y auditable.
