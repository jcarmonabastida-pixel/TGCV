# C10-S — Opciones de microdominio sintético y recomendación de selección

**ID:** C10-S-MICRODOMAIN-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** análisis comparativo y recomendación; NO aprobado, NO congelado.  
**Dependencias:** fichas históricas §§47–69; inventario §74; reconciliaciones §§75–77; contratos DGP, ACC, Reach, identidad y evidencia.  
**Restricciones:** propuestas de modelado, no evidencia empírica. No se generan datos, no se ejecutan fixtures y no se autoriza implementación/simulación.

## 1. Propósito

El hueco identificado en C10-S no es la ausencia de predicados generales, sino la falta de semántica concreta para F2/A1/A2 y de una F* común verificable. Se comparan tres microdominios sintéticos que permiten representar: (i) provisión focal de una dependencia, (ii) una transformación focal y su continuación, (iii) una ruta alternativa genuina, (iv) condiciones y recursos observables, y (v) resultado técnico independiente de Outcome/Value.

La selección debe favorecer identificación y falsabilidad, no producir artificialmente un resultado positivo para accesibilidad.

## 2. Criterios de comparación

C1. F* observable y definible antes de Outcome/Value.  
C2. F1/τ2 habilitable por la política B ya propuesta sin que B ordene ejecutar F1.  
C3. F2 tiene función propia y precondiciones distintas de F1.  
C4. A1→A2 constituye mecanismo alternativo genuino, no una copia nominal de F1→F2.  
C5. Las dos rutas pueden evaluarse con un criterio funcional común sin exigir identidad de mecanismo.  
C6. Recursos, autorizaciones, dependencias, ventanas y fallos son especificables.  
C7. R0–R3 pueden representarse sin contradicciones.  
C8. El dominio es suficientemente simple para un DGP pequeño y suficientemente rico para que ACC≠APP≠Reach.  
C9. Se puede observar error de medición y cobertura sin usar Outcome/Value como oráculo.  
C10. Evita que el tratamiento cambie directamente la ruta alternativa en el escenario primario; ese cambio se conserva como adversarial R2.

## 3. Opción A — Migración de configuración entre dos entornos software

### F* candidata
Producir en el entorno destino una configuración que cumpla un contrato de esquema, integridad y compatibilidad predefinido, conservando los campos/propiedades obligatorios y sin violar restricciones de seguridad. F* no incluye productividad, satisfacción, valor económico ni Outcome posterior.

### Ruta focal
- **F1=τ2:** habilitar y utilizar un adaptador focal versionado que convierte la configuración fuente al formato objetivo.
- **F2:** aplicar la configuración convertida en el entorno destino y superar validaciones de esquema, integridad y compatibilidad.

### Ruta alternativa
- **A1:** exportar la configuración mediante un formato de intercambio ya disponible en baseline.
- **A2:** importar/aplicar el formato de intercambio mediante el mecanismo nativo del destino y superar los mismos criterios F*.

### B candidata
Desplegar/configurar la dependencia técnica del adaptador focal y habilitar su interfaz; no ejecuta la conversión ni aplica la configuración.

### Predicados diferenciables
- ACC(F1) depende del adaptador, su identidad/versión, integridad, compatibilidad, canal y recursos.
- APP(F1,S0) depende de que la configuración fuente esté dentro del dominio admitido.
- ACC(F2) y APP(F2,S2) se evalúan por separado: el destino puede carecer de permisos, capacidad o compatibilidad aunque F1 esté disponible.
- La ruta alternativa depende de exportador/importador baseline y de un contrato de intercambio propio.
- RES puede parametrizarse por CPU/memoria/espacio y slots; AUTH por permisos de lectura, escritura y aplicación; WIN por ventana de mantenimiento y caducidad de credenciales.

### Riesgos
- F* debe fijar tolerancias de conversión y propiedades que deben preservarse; no basta “la configuración se aplicó”.
- No confundir una validación sintáctica con integridad semántica.
- Evitar que A1/A2 sean trivialmente la misma implementación que F1/F2 bajo otro nombre.
- Las versiones y formatos pueden introducir cambios de identidad/mapping.

## 4. Opción B — Integración de datos entre sistemas heterogéneos

### F* candidata
Transferir un conjunto de datos de prueba entre origen y destino preservando un contrato de datos preespecificado: campos obligatorios, tipos, relaciones, integridad y reglas de consistencia.

### Ruta focal
- **F1=τ2:** habilitar/utilizar un conector focal que traduce el protocolo o esquema origen.
- **F2:** cargar y validar el conjunto en el destino bajo el contrato común.

### Ruta alternativa
- **A1:** exportar mediante formato neutral/intercambio preexistente.
- **A2:** importar y validar mediante la herramienta nativa del destino.

### B candidata
Provisión técnica del conector focal, sin iniciar transferencia.

### Riesgos
- F* y la calidad de los datos pueden confundirse; se requiere dataset de referencia y oráculo de integridad independiente.
- Riesgo de filtración de información sensible; aunque sea sintético, la especificación debe evitar PII.
- Es fácil introducir un segundo outcome técnico compuesto y multiplicar condiciones de calidad.
- La ruta alternativa puede depender del mismo conector o librería, comprometiendo independencia mecanística.

## 5. Opción C — Reconfiguración de flujo de trabajo organizativo

### F* candidata
Completar una reasignación protocolizada de un caso sintético entre dos equipos/colas, preservando responsabilidad, permisos, trazabilidad y SLA.

### Ruta focal
- **F1=τ2:** habilitar un módulo/permiso de enrutamiento especializado.
- **F2:** completar transferencia y aceptación por el equipo destino.

### Ruta alternativa
- **A1:** reasignación manual mediante un canal estándar.
- **A2:** aceptación y registro por el equipo destino.

### Riesgos
- La intervención puede cambiar conocimiento, incentivos, autoridad o carga, creando vías directas y confusión entre accesibilidad, decisión humana y ejecución.
- Recursos y tiempos compartidos inducen interferencia; más difícil sostener unidades independientes.
- Mayor dependencia de supuestos conductuales y de una política de control representativa.
- Menor parsimonia para el primer DGP mecanístico.

## 6. Comparación

Escala cualitativa: Alta / Media / Baja, evaluada frente a los criterios anteriores; no es un score empírico.

| Criterio | A: Configuración software | B: Integración de datos | C: Flujo organizativo |
|---|---|---|---|
| F* técnico independiente de O/V | Alta | Alta | Media |
| Separación B/provisión frente a ejecución | Alta | Alta | Media |
| F2 con precondiciones diferenciables | Alta | Alta | Media |
| Ruta alternativa genuina | Alta | Media-Alta | Alta |
| Control de recursos/ventanas | Alta | Media-Alta | Media-Baja |
| Riesgo de interferencia | Bajo si instancia aislada | Medio | Alto |
| Complejidad de medición | Media | Alta | Alta |
| Observabilidad de fallos | Alta | Alta | Media |
| Parsimonia del DGP | Alta | Media | Baja |
| Adecuación R0–R3 | Alta | Alta | Media |

## 7. Recomendación

**Recomiendo la Opción A — migración de configuración entre dos entornos software — como microdominio candidato preferente para el DGP sintético C10-S.**

Razones:
1. Permite definir F* como conformidad técnica verificable, sin recurrir a Value.
2. B puede limitarse a provisionar el adaptador; la conversión/aplicación ocurre en pasos separados.
3. F1 y F2 tienen funciones diferentes y condiciones de entrada distintas.
4. La ruta A1→A2 puede usar un mecanismo de intercambio preexistente genuinamente diferente.
5. Los recursos, permisos, versiones, ventanas, fallos y evidencias son controlables a nivel de instancia.
6. Facilita construir R0 (sin alternativa), R1 (alternativa basal estable), R2 (B afecta también al canal alternativo) y R3 (fallo de provisión).

Esta recomendación no convierte la Opción A en decisión aprobada. La especificación concreta de formatos, reglas de conversión, tolerancias, recursos y ventanas permanece abierta. Tampoco demuestra que una política de provisión afecte al valor.

## 8. Primer borrador de fichas bajo Opción A — ilustrativo, no asignado

| Alias | Función candidata | Entrada→salida | Condición propia que debe fijarse |
|---|---|---|---|
| F1/τ2 | Convertir configuración fuente usando adaptador focal recién provisionado | S0→S2 (configuración en representación objetivo) | Adaptador íntegro/compatible, esquema fuente admitido, permisos de lectura y recursos de conversión |
| F2 | Aplicar configuración convertida en destino y validarla | S2→SF (configuración destino conforme) | Permiso de escritura, destino compatible, validaciones semánticas y ventana de aplicación |
| A1 | Exportar configuración fuente a formato neutral ya disponible | S0→S1 (artefacto de intercambio válido) | Exportador baseline, permiso de lectura, esquema de intercambio |
| A2 | Importar/aplicar artefacto neutral y validar destino | S1→SF | Importador nativo, permiso de escritura, compatibilidad y mismas propiedades F* |

La tabla es una propuesta de instanciación de aliases. No se han definido TID/SID/RID, formatos, predicados truth, tasas, tolerancias ni consumos. La ruta alternativa solo será funcionalmente substituible si supera el mismo F* y sus restricciones; el hecho de que llegue a SF por definición formal no basta.

## 9. Contrato F* propuesto para desarrollar

Antes de especificar el DGP, F* deberá fijar:
- lista cerrada de propiedades obligatorias de configuración;
- reglas de preservación y equivalencia de valores;
- restricciones de integridad y compatibilidad;
- política explícita para campos opcionales/desconocidos;
- criterios de rechazo y tolerancias;
- procedimiento de validación independiente y ciego a Z/B;
- dataset sintético de referencia, sin PII;
- cobertura del catálogo de formatos y mecanismos alternativos.

No se asignan umbrales numéricos hasta justificar qué error o pérdida es admisible y por qué.

## 10. Riesgos de identificación que deben preservarse

- B debe modificar la disponibilidad del adaptador focal, no F* ni el estándar de evaluación.
- B no debe modificar A1/A2 en el escenario primario R0/R1; R2 se mantiene como escenario de vía colateral.
- C_auth, recursos generales, información y capacidad basal deben quedar constantes o explícitamente modelados.
- La disponibilidad de F1 no garantiza App(F1,S0), ACC(F2), App(F2,S2) ni Reach(SF).
- La ruta alternativa puede mantener Reach(SF)=1 antes y después de abrir F1; esto es una posibilidad teórica que el DGP debe conservar, no suprimir.
- El efecto ITT de Z/B no identifica automáticamente el efecto causal mediado por A_f*.
- La verdad del DGP y las observaciones del analizador deben permanecer separadas; el oráculo no debe filtrar truth al analizador.
- La cobertura de alternativas debe estar acotada por un universo declarado; ausencia universal no se infiere de enumeración incompleta.

## 11. Decisiones requeridas antes de completar las fichas

1. Aceptar, modificar o rechazar Opción A como microdominio de trabajo.
2. Aprobar F* técnica y sus propiedades de preservación.
3. Fijar si A1/A2 representan un mecanismo neutral independiente del adaptador focal.
4. Definir versiones/identidades, contratos de entrada/salida y mappings.
5. Especificar recursos, autorización, ventanas, caducidades y fallos.
6. Ratificar R0/R1/R2/R3 y su correspondencia con S4R.
7. Resolver D1/D2 y los parámetros del mecanismo por separado; la elección de microdominio no los decide.
8. Definir la evidencia E1–E4, cobertura y validación de error.

## 12. Dictamen

La Opción A es la recomendación más parsimoniosa para operacionalizar C10-S sin introducir dependencias humanas ni confundir la intervención con la ejecución. Las Opciones B y C se conservan como alternativas documentadas.

**Estado final:** microdominio recomendado, NO seleccionado ni aprobado. F1/F2/A1/A2 continúan como fichas ilustrativas hasta decisión explícita. No se cierran AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007. No se generan datos, no se implementa ni ejecuta el experimento.


## 13. Decisión de selección — Opción A (2026-11-05)

**DEC-C10-051 — Opción A seleccionada como microdominio de trabajo de C10-S.** Por decisión explícita del usuario, se selecciona la migración de configuración entre dos entornos software como microdominio de diseño y operacionalización del experimento sintético C10-S. Las Opciones B y C permanecen como alternativas históricas, no como líneas activas del diseño primario.

La selección no implica que el experimento esté aprobado para ejecución, que exista un entorno técnico real inventariado, ni que estén fijados formatos, versiones, mappings, recursos, ventanas, umbrales o parámetros del DGP. Tampoco decide D1/D2, R0–R3 ni los supuestos de identificación.

La definición candidata de F* se adopta como **contrato funcional de trabajo** para desarrollar las fichas y el DGP: la ruta completa debe producir y aplicar en el entorno destino una configuración que satisfaga las propiedades obligatorias preespecificadas de esquema, integridad, compatibilidad, preservación funcional y seguridad. El catálogo exacto de propiedades, mappings, tolerancias, casos frontera y oráculo permanece abierto y deberá cerrarse antes de fijar el DGP confirmatorio.

**Estado:** microdominio seleccionado para diseño; F* adoptado como contrato de trabajo candidato. No equivale a cierre de OPEN-C10-003, aprobación final del experimento, freeze, validación técnica, revisión independiente ni autorización de ejecución.
