# DEC-C10-067 — Aceptación del contrato material de políticas D2

**Fecha:** 2026-11-06  
**Estado:** ACEPTADA — alcance conceptual/documental  
**Ámbito:** C10-S / D2 primario candidato / definición material de políticas de provisión  
**Rama de registro:** `research/c10-s-consolidation-draft`

## Decisión

Se aceptan las definiciones materiales conceptuales de las políticas \(B_{g0}^{D2}\) y \(B_{g1}^{D2}\). La aceptación fija qué política se asigna y qué procedimiento pretende aplicar; no presupone cumplimiento, éxito técnico, accesibilidad ni ejecución de transformaciones.

### 1. Política de control \(B_{g0}^{D2}\)

- Mantener la configuración basal asignada.
- No programar ni iniciar ningún intento de provisión focal de la dependencia requerida por \(\tau_2\).
- No desplegar ni configurar el adaptador focal como parte de la intervención.
- Mantener comunes la autorización basal y las condiciones no focales constitutivas especificadas para la población elegible.
- Registrar cualquier provisión focal que aparezca por una vía ajena a la política asignada como provisión de fondo/crossover; no ocultarla ni redefinir retrospectivamente la asignación.

La ausencia de intento programado no equivale a una prohibición artificial de cualquier cambio técnico externo. La ausencia efectiva de provisión focal de fondo debe verificarse.

### 2. Política de tratamiento \(B_{g1}^{D2}\)

- Programar un intento de despliegue/configuración de la dependencia técnica focal necesaria para \(\tau_2\).
- Utilizar un artefacto y una versión identificados antes de la asignación.
- Habilitar la interfaz/canal técnico requerido, sin modificar la autorización normativa basal.
- Registrar actor responsable, inicio, recepción, finalización, versión recibida y desviaciones.
- Verificar por separado instalación, integridad, compatibilidad y operatividad.
- No ejecutar F1, F2, A1 ni A2 como parte de la provisión.

La política programa el intento; no garantiza que se inicie efectivamente, se complete o tenga éxito. La asignación, intento programado, intento efectivo, recepción, instalación, componentes verificados y estado final son registros distintos.

### 3. Secuencia temporal y constructos

\[
Z_i \rightarrow B_{gZ_i}^{D2}
\rightarrow W_{programmed,i}
\rightarrow W_{attempt,i}
\rightarrow S_{install,i}
\rightarrow C_{dep,i}^{*}
\rightarrow A_{f,i}^{*}
\rightarrow D_{f,i}^{*}
\]

- \(W_{programmed}\): intento programado por la política.
- \(W_{attempt}\): intento efectivamente iniciado.
- \(C_{dep}^{*}\) acredita el estado técnico compuesto: instalación, integridad, compatibilidad y operatividad.
- \(A_f^{*}\) exige además los predicados constitutivos aplicables (identidad, relaciones, condiciones, autorización, recursos, dependencias y ausencia de bloqueos).
- \(D_f^{*}\) representa la apertura focal basal→post; requiere inaccesibilidad focal basal.
- Ninguno de estos constructos se infiere automáticamente de Z, B o W_programmed.

### 4. Condiciones comunes del DGP aislado

Se acepta como requisito conceptual mantener comunes entre brazos:
- \(C_{auth,base}=1\), sin que B altere la autorización normativa;
- reglas de elegibilidad y definición/versionado de \(\tau_2\);
- recursos no focales, capacidad e información técnica basales;
- criterio y protocolo de medición/adjudicación;
- restantes condiciones constitutivas no focales que el DGP declare invariantes.

La provisión no debe introducir diferencialmente recursos, permisos, costes, latencia, calidad, seguridad, información, incentivos, alternativas u otras vías hacia Outcome/Value. Si alguna cambia por B, debe registrarse y modelarse como vía colateral/cointervención. El ITT conserva interpretación como efecto de la política/paquete asignado; no se etiqueta automáticamente como efecto puro de accesibilidad.

### 5. Parámetros y alcance no aprobados

El éxito técnico condicional \(s=0.80\) continúa siendo una hipótesis de diseño no validada. No se aprueban probabilidades, distribuciones conjuntas de componentes, tasa de cumplimiento, número de intentos, reintentos, calibración, parámetros de Value, potencia ni tamaño muestral.

Para D2, las probabilidades candidatas de programación son \(P(W_{programmed}=1|Z=0)=0\) y \(P(W_{programmed}=1|Z=1)=1\). La probabilidad de intento efectivo \(W_{attempt}\) depende de recepción/cumplimiento y debe medirse por separado; cualquier intento de fondo cuando no se programa debe registrarse. El valor candidato \(P(C_{dep}^{*}=1|Z=1)=0.80\) solo se deriva bajo \(s=0.80\), cumplimiento perfecto, una oportunidad y ausencia de provisión de fondo/rutas técnicas no registradas. No implica \(P(A_f^{*}=1)=0.80\) ni \(P(D_f^{*}=1)=0.80\).

D1 permanece como escenario secundario conforme a DEC-C10-066; sus reglas de provisión ordinaria de baja frecuencia no se sustituyen por las definiciones D2.

### 6. Datos operativos pendientes

No se completan por inferencia:
1. identidad/rol del actor responsable;
2. identidad, versión y hash del artefacto técnico;
3. protocolo de recepción y aceptación;
4. ventana temporal del intento y de la verificación;
5. regla de reintentos, fallos parciales, rollback y desviaciones;
6. mecanismo para detectar provisión focal de fondo en el control;
7. evidencia independiente para cada componente de \(C_{dep}^{*}\);
8. inventario/cobertura de rutas alternativas y soporte de ambas políticas.

### 7. Precedencia y autorización

Esta decisión complementa DEC-C10-066: D2 sigue siendo el escenario primario candidato y D1 el secundario. No reabre la selección del comparador ni cierra su legitimidad, estimandos, correspondencia \(B\leftrightarrow g\), población/soporte, unidad/interferencia, vías colaterales, exclusión o identificación.

**No autoriza** freeze, implementación, validación ejecutable, simulación ni ejecución científica.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.
