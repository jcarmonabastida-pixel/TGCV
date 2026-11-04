# C10-S — Auditoría de compatibilidad causal del microdominio de migración de configuración

**ID:** C10-S-MD-CAUSAL-AUDIT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** auditoría conceptual-documental; propuesta condicionada; NO aprobada, NO congelada.  
**Ámbito:** Opción A frente a C10-D1, reconciliación causal, DGP temporal, P*_τ2/P*_F, D1/D2 y R0–R3.  
**No autoriza:** elección de comparador, implementación, simulación, generación de datos ni ejecución.

## 1. Dictamen ejecutivo

La Opción A es **potencialmente compatible**, pero la formulación actual no demuestra todavía una intervención autónoma sobre accesibilidad ni identifica θ_A(q). Puede servir como microdominio sintético para estudiar una política de provisión técnica que induce cambios en accesibilidad focal, siempre que se cierre una separación estricta entre provisión/configuración del adaptador (política B), estado técnico de dependencia (C_dep), accesibilidad de τ2 (A_f*), aplicabilidad (App), ejecución, continuación F2, validación funcional F* y Outcome/Value posteriores.

El principal riesgo es llamar F1 a la vez “transformación focal τ2”, “uso del adaptador para convertir” y “apertura de accesibilidad por B”. Son objetos distintos. La instalación del adaptador no puede ser simultáneamente el cambio de accesibilidad y la ejecución de τ2.

**Recomendación:** conservar Opción A como candidata condicionada, reformular sus fichas y no avanzar aún a parámetros/ecuaciones completas del DGP. No se rechaza el microdominio; tampoco se acepta.

## 2. Compatibilidad con la arquitectura C10-D1

### 2.1 Jerarquía de estimandos

La arquitectura rectora mantiene separados:
- TE_Z / ITT_Z: efecto total de asignar la política B en Value;
- θ_A(q)=E[V^{q,g1}]-E[V^{q,g0}]: contraste entre políticas factibles de accesibilidad bajo régimen común q;
- LATE_f: efecto local entre compliers inducidos por instrumento, solo bajo supuestos IV;
- θ_{L,A}: efecto conjunto de condiciones y accesibilidad, cuando el contraste cambia ambas.

Una aleatorización de Z a una política de provisión B identifica el ITT de esa política bajo supuestos de diseño. No identifica automáticamente θ_A(q), el efecto mediado por A_f*, ni el efecto de ΔT_acc.

Para aproximarse a θ_A(q), el DGP debe definir dos políticas factibles g1/g0 que difieran en la distribución de accesibilidad focal, manteniendo el mismo régimen q de condiciones basales/postbasales pertinentes. Si la provisión cambia costes, recursos, seguridad, calidad, latencia, información, autorización, capacidad o alternativas por vías distintas de A_f*, esas vías deben quedar ausentes por diseño o separadas mediante estrategia causal adicional. El residuo TE−θ_A no es automáticamente un efecto directo puro ni debe asumirse aditividad.

### 2.2 Instrumento y exclusión

Si Z solo asigna B y B solo cambia la posibilidad de invocar τ2, podría evaluarse un estimando IV focal, pero únicamente tras justificar:
- relevancia para A_f* (no solo para C_dep);
- independencia de Z;
- exclusión: Z no afecta V por vías distintas de A_f* en el contraste considerado;
- monotonicidad, consistencia/versiones, no interferencia y medición válida.

Un primer estadio de C_dep no demuestra primer estadio de A_f* ni de D_f*. Tampoco garantiza que cambie ΔT_acc completo. Deben reportarse por separado C_dep, A_f,1*, D_f*, ΔT_acc, Reach_H y F*.

## 3. Auditoría de la intervención B

La definición actual de B —desplegar/configurar el adaptador focal, habilitar interfaz y verificar instalación/integridad/compatibilidad/operación— encaja con la Candidata A de la reconciliación causal solo si se restringe a provisión técnica.

Condiciones necesarias:
1. B no ejecuta conversión, importación, aplicación ni validación.
2. B no concede ni amplía permisos normativos; C_auth debe ser basal, elegible e invariante.
3. B no modifica la configuración fuente ni destino, el contrato F*, el dataset de referencia ni el validador.
4. B no altera disponibilidad, rendimiento o permisos de A1/A2 en R0/R1.
5. Los recursos consumidos por instalación/provisión no pueden reducir diferencialmente los recursos disponibles para F2/A1/A2; si lo hacen, deben modelarse como vía causal.
6. B no debe alterar costes, latencia, seguridad, calidad, información, incentivos, prioridades ni expectativas con efecto propio sobre V.
7. Fallos de provisión y versiones recibidas se registran; no se condiciona el ITT por W_attempt, C_dep ni accesibilidad postratamiento.

**Riesgo residual:** instalar un adaptador puede modificar librerías, rutas de ejecución, configuración del entorno, superficie de seguridad, carga de recursos o dependencias compartidas. La etiqueta “provisión técnica” no prueba ausencia de vías colaterales. Se requiere manifiesto de cambios y prueba de no-afectación de canales alternativos.

## 4. Auditoría de F1/F2 y separación de roles

La propuesta debe corregirse así:

| Objeto | Definición requerida | No confundir con |
|---|---|---|
| B | Política asignada de provisión/configuración del adaptador focal | Transformación τ2 ejecutada |
| C_dep | Estado técnico verificado de la dependencia | Accesibilidad completa |
| A_f* | Accesibilidad de τ2 para unidad/contexto según ID/REL/COND/AUTH/RES/DEP/BLOCK | C_dep, App o ejecución |
| F1/τ2 | Operación de conversión de configuración fuente mediante adaptador disponible | Instalación del adaptador |
| App(F1,S0) | Aplicabilidad de la conversión a la configuración fuente concreta | Accesibilidad |
| Exec(F1) | Conversión efectivamente iniciada/realizada | Selección o disponibilidad |
| F2 | Aplicación de configuración convertida en destino | Validación F* aislada |
| F*(π) | Cumplimiento de contrato funcional común por ruta completa π | Estado nominal SF o éxito sintáctico |

F1/τ2 no debe describirse como “habilitar y utilizar” el adaptador. Habilitar pertenece a B/provisión; utilizar/convertir pertenece a ejecución de τ2. El cambio de accesibilidad se verifica en t3, la trayectoria potencial se evalúa en t4 y la ejecución ocurre después de selección, en t7.

F2 requiere predicados propios de aplicabilidad, autorización, capacidad de destino, recursos, compatibilidad y ventana. Que F1 convierta correctamente no demuestra que F2 esté accesible, aplicable o ejecutable.

## 5. F* y resultado técnico

La definición de F* de la reconciliación poblacional ya es sustantiva: modificar configuración del sistema diagnosticado para obtener una configuración objetivo bajo restricciones de seguridad, integridad y compatibilidad. La nueva propuesta de “conformidad de esquema, integridad y compatibilidad” es compatible como concreción candidata, pero no debe duplicar ni sustituir el contrato histórico.

El contrato F* debe fijar ex ante:
- estado/configuración fuente admisible;
- propiedades obligatorias y reglas de preservación;
- configuración destino y criterios de aceptación;
- esquema, tipos, relaciones e invariantes;
- integridad semántica y no solo sintáctica;
- compatibilidad y seguridad;
- campos opcionales/desconocidos y reglas de pérdida;
- tolerancias justificadas;
- oráculo independiente, ciego a Z/B y a O/V;
- universo de formatos/mecanismos y cobertura.

La validación común de F* puede ser un oráculo compartido para ambas rutas, sin que ello haga idénticos los mecanismos transformacionales. Debe evitarse que la ruta focal y la alternativa utilicen el mismo conversor, parser, librería o dependencia crítica sin registrarlo: una dependencia común puede comprometer la independencia de rutas y R1.

## 6. Auditoría de la ruta alternativa

A1/A2 solo son una ruta genuinamente alternativa si el formato neutral y el mecanismo nativo de importación no dependen del adaptador focal ni de la misma dependencia crítica que B modifica.

Se requiere inventario de código/librerías compartidos, dependencias transitivas, APIs/servicios comunes, permisos/credenciales, recursos compartidos, configuración/estado que B modifica, validadores y restricciones/ventanas.

La independencia no significa ausencia de cualquier componente común: el oráculo F* puede ser común si solo mide conformidad. Sí exige que el mecanismo que genera la ruta alternativa no sea activado, modificado o degradado por B en R0/R1.

Si B afecta A1/A2, se clasifica como R2/vía colateral y el contraste identifica el efecto de paquete. No se presenta como instrumento focal exclusivo. En R0, la ausencia de alternativa solo se establece dentro de un universo finito explícito y con cobertura exhaustiva; de lo contrario F_alt,0=? y no se confirma P*_F.

## 7. R0–R3 y relación con P* / D1-D2

| Escenario | Función en el diseño | Consecuencia |
|---|---|---|
| R0 / S4R-A | No existe ruta alternativa funcional dentro del universo cerrado y cubierto | Puede estudiar apertura focal funcional exclusiva; requiere cobertura y F* cerradas |
| R1 / S4R-B | Ruta A1→A2 basal, funcional y no afectada por B | τ2 puede abrirse sin cambiar Reach(SF); no confundir cambio T_acc con cambio de función alcanzable |
| R2 / S4R-C | B afecta también al mecanismo alternativo | Vía colateral; ITT de paquete; exclusión focal comprometida |
| R3 / S4R-D | Fallo/no cumplimiento de provisión focal | Mantener ITT; no imputar A_f*, D_f* ni ΔT_acc desde Z o intento |

D1/D2 no se resuelve al seleccionar el microdominio:
- D1 compara provisión programada con régimen ordinario; requiere justificación externa de probabilidades/condiciones ordinarias.
- D2 compara provisión con ausencia de intento focal; requiere ausencia de provisión de fondo verificable.
Son preguntas y estimandos de política diferentes. La precedencia histórica de D1 y la recomendación mecanística posterior de D2 siguen abiertas. El microdominio no justifica escoger uno.

## 8. Riesgos causales concretos y controles requeridos

| Riesgo | Vía potencial | Control/especificación requerida |
|---|---|---|
| Instalación cambia estado/configuración | B→estado fuente/destino→App/F* | Manifiesto de cambios; snapshot antes/después |
| Adaptador consume recursos | B→RES/capacidad→F2/A1/A2/Outcome | Aislar recursos o modelar disponibilidad/consumo por rama |
| Permisos añadidos | B→AUTH→A_f*/App y posiblemente V | C_auth basal común; separar cointervención |
| Cambio de seguridad/latencia/coste | B→O/V sin pasar por A_f* | Mantener invariantes o estimar paquete/vías separadas |
| Dependencias compartidas | B→A1/A2 | Grafo de dependencias y auditoría de no-afectación |
| Aprendizaje/información | B→K/selección→ejecución/V | Provisión ciega/automatizada; medir y modelar si no puede excluirse |
| Oráculo influido por tratamiento | Z/B→medición | Validador fijo, ciego, versionado y separado del generador |
| Error de medición diferencial | Z/B→A_f,obs | Validación por brazo/componente, sensibilidad y límites |
| Interferencia entre instancias | B_i→recursos/estado_j | Aislamiento o asignación por clúster/modelo de exposición |

## 9. Especificación mínima requerida antes de continuar

### Gate MD-C1 — Política B
Manifiesto exhaustivo de cambios de instalación/provisión; evidencia de que no ejecuta F1/F2 ni modifica F* o el validador; recursos consumidos; permisos; dependencias; reversibilidad.

### Gate MD-C2 — Accesibilidad focal
Definición de A_f* específica de τ2, con ID/REL/COND/AUTH/RES/DEP/BLOCK, identidad TID/SID/RID y medición independiente. Demostrar que B cambia la probabilidad de A_f*, no solo C_dep.

### Gate MD-C3 — Rutas
Contrato de entrada/salida de F1/F2/A1/A2; grafo de dependencias compartidas; prueba de que A1/A2 no se alteran en R0/R1; F2 y A2 verifican la misma F*.

### Gate MD-C4 — F*
Contrato de aceptación no circular y oráculo independiente, versionado y ciego.

### Gate MD-C5 — Estimandos/comparador
Definición material de g0/g1, q_X*/q_L*, población, horizonte y Value; decisión justificada D1/D2; estimandos y supuestos separados. El microdominio por sí solo no identifica θ_A(q).

### Gate MD-C6 — Medición y cobertura
Truth/observación separadas; sensibilidad/especificidad; cobertura del catálogo de rutas; reglas Reach 1/0/?; análisis de missingness y no interferencia.

## 10. Dictamen y próximos pasos

**Dictamen:** Opción A sigue siendo la candidata más parsimoniosa, pero su formulación actual es causalmente insuficiente para tratar B como manipulación autónoma de accesibilidad. Se mantiene como recomendación condicionada, no selección aprobada.

Orden de trabajo:
1. separar B/provisión, C_dep, A_f*, F1 ejecución y F2;
2. concretar manifiesto de cambios de B y auditar vías directas;
3. completar el grafo de dependencias e independencia de A1/A2;
4. armonizar F* con la definición histórica, sin duplicarla;
5. especificar condiciones y evidencia propias de F2/A2;
6. solo después construir ecuaciones generadoras y decidir D1/D2.

AUD-001/002, AUD-004/005/007/010/011, OPEN-C10-001/003/005/007 y CA-01…07 permanecen abiertos salvo evidencia independiente de cierre. Este documento no aprueba el microdominio, no cierra identificación causal, no fija parámetros y no autoriza implementación, simulación ni ejecución.
