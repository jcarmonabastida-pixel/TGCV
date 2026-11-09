# AFLUYA — Plan de implantación ejecutable
## Versión 0.1

**Identificador:** AFLUYA-IMPL-001  
**Fecha:** 2026-11-10  
**Estado:** DRAFT — plan operativo inicial, pendiente de aprobación por fases  
**Rama:** `strategy/afluya-ecosystem-v0.2`  
**Documento estratégico de referencia:** `09_STRATEGY/AFLUYA_ECOSYSTEM_ARCHITECTURE_v0.7.md`  
**Brief jurídico relacionado:** `09_STRATEGY/AFLUYA_TRADEMARK_CLEARANCE_BRIEF_v0.1.md`

---

## 1. Propósito y alcance

Convertir la arquitectura estratégica de AFLUYA en una secuencia de implantación realizable por una sola persona sin conocimientos de programación, con asistencia paso a paso y coste inicial mínimo.

El plan cubre preparación, comprobación de dominios, identidad visual mínima, web pública en Framer, publicación documental, integración, revisión previa al lanzamiento y mantenimiento.

No implica que se hayan contratado servicios, comprado dominios, creado cuentas, publicado contenidos ni autorizado gastos. Cada fase es una propuesta hasta que el usuario apruebe su inicio y las decisiones que impliquen compromisos.

## 2. Principios de ejecución y límites

1. **Aprobación previa:** ninguna compra, registro de dominio, contratación, alta de plan de pago, activación de prueba con renovación, publicación irreversible o compromiso con terceros sin aprobación expresa.
2. **Partir de cero:** el inventario inicial declara que no hay dominios registrados ni servicios contratados. No crear cuentas por anticipado.
3. **Una tarea cada vez:** las instrucciones deben indicar dónde entrar, qué seleccionar o introducir, qué resultado esperar y cómo verificarlo.
4. **No-code primero:** preferir interfaces visuales y herramientas gratuitas cuando satisfagan la necesidad. No exigir al usuario terminal, programación o configuración técnica manual salvo que se explique y se justifique.
5. **Coste mínimo y reversibilidad:** aplazar planes de pago, integraciones y funcionalidades no esenciales. Antes de contratar, verificar precio, impuestos, renovación, límites, exportación y cancelación.
6. **GitHub como fuente maestra:** conservar en GitHub los documentos, decisiones, estructura de contenidos y procedimientos. La web pública presenta y enlaza el conocimiento; no sustituye el repositorio maestro.
7. **Separación de líneas:** la implantación de AFLUYA no modifica TGCV Core, hipótesis, RMA, Evidence→Claim Matrix, C09/C10 ni autorizaciones científicas.
8. **Honestidad de estado:** distinguir concepto, diseño, prototipo, demostrador, piloto, producto operativo y evidencia. No presentar simulaciones como evidencia empírica ni claims abiertos como validados.
9. **Propiedad y control:** las cuentas, dominios, repositorios, métodos de recuperación y activos esenciales deben permanecer bajo control del titular; activar MFA cuando proceda.
10. **No contratar apoyo técnico por defecto:** solo considerar asistencia puntual cuando exista un bloqueo real, con alcance, coste, entregable y transferencia de control previamente aprobados.

## 3. Estado inicial

| Elemento | Estado de partida | Tratamiento |
|---|---|---|
| Marca paraguas | AFLUYA, decisión estratégica de trabajo | Mantener; sujeta a búsqueda jurídica |
| Dominio preferido | `afluya.org` | NOT_VERIFIED; no comprar hasta comprobar y aprobar |
| Variantes | `afluya.com`, `afluya.es` | NOT_VERIFIED; protección opcional |
| Cuentas y servicios | Se parte de cero | No crear ni contratar hasta que sea necesario |
| Web pública | Framer, opción recomendada en arquitectura v0.7 | Confirmar alcance y plan vigente antes de alta |
| Base documental | GitHub, fuente maestra | Mantener |
| Publicación documental | Astro + Starlight + GitHub Pages, arquitectura recomendada | Implantar solo cuando se haya comprobado el flujo más ligero y gratuito |
| Identidad visual | Dirección creativa definida; sistema final pendiente | Crear sistema visual mínimo antes de maquetar |
| Presupuesto | Objetivo de coste mínimo; cifras de arquitectura sujetas a actualización | Verificar precios oficiales antes de cualquier decisión |

## 4. Gobierno de fases y puertas de aprobación

Cada fase tendrá cuatro estados posibles:

- **NOT_STARTED:** no iniciada.
- **IN_PROGRESS:** trabajo en curso, sin que ello autorice gastos.
- **READY_FOR_APPROVAL:** entregables y verificaciones preparados para decisión del usuario.
- **ACCEPTED / BLOCKED:** aceptada para continuar o bloqueada hasta resolver incidencias.

No se avanzará automáticamente de una fase a otra. El usuario aprueba expresamente cada puerta cuando la fase implique decisión de marca, gasto, publicación o cambio de arquitectura.

### Registro mínimo de cada decisión

- ID y fecha.
- Decisión solicitada y alternativas.
- Recomendación y fundamento.
- Coste inicial y recurrente, si aplica.
- Riesgos, renovación y reversibilidad.
- Decisión del usuario.
- Evidencia de comprobación y enlace pertinente.

## 5. Fases de implantación

### Fase 0 — Preparación e inventario

**Objetivo:** fijar el punto de partida y el orden de trabajo sin crear cuentas ni incurrir en gastos.

**Tareas:**
1. Confirmar el inventario inicial: sin dominios registrados ni servicios contratados.
2. Mantener como referencias la arquitectura v0.7 y el brief de anterioridades v0.1.
3. Crear un registro de decisiones, costes, cuentas y activos.
4. Confirmar que el usuario controla su cuenta GitHub y puede acceder al repositorio y a la rama estratégica.
5. Definir los criterios de aceptación de la primera publicación: portal institucional claro, contenidos iniciales revisados, acceso a conocimiento y vía de contacto/participación.
6. Preparar la lista de datos que se necesitarán para las siguientes fases, sin solicitarlos hasta que sean necesarios.

**Entregables:**
- Inventario inicial validado.
- Registro de decisiones y aprobaciones.
- Lista de fases y dependencias confirmada.

**Criterio de salida:** el usuario confirma el inventario y autoriza únicamente iniciar la comprobación de dominios. No se crea ninguna cuenta ni se compra nada.

### Fase 1 — Dominio y comprobaciones previas

**Objetivo:** comprobar la disponibilidad técnica de los dominios y separar esta comprobación de la viabilidad jurídica de la marca.

**Dominios:**
- Principal preferido: `afluya.org`.
- Variantes defensivas: `afluya.com`, `afluya.es`.

**Tareas:**
1. Consultar cada dominio en un registrador fiable y, cuando sea posible, contrastar el estado mediante RDAP/WHOIS oficial.
2. Registrar fecha, hora, fuente, estado devuelto, precio de registro, renovación, impuestos, privacidad de datos, condiciones de transferencia y posibles costes adicionales.
3. Distinguir AVAILABLE, REGISTERED, PREMIUM, RESERVED, REDEMPTION/PENDING y NOT_VERIFIED; no inferir disponibilidad ante errores o respuestas ambiguas.
4. Comprobar por separado la situación jurídica de la marca mediante el brief profesional de anterioridades. La consulta técnica del dominio no sustituye el análisis de marcas.
5. Recomendar si basta con el dominio principal o si tiene sentido proteger variantes; comparar coste total y política de renovación.
6. Presentar la recomendación sin iniciar compra.

**Entregable:** ficha comparativa de dominios y recomendación de decisión.

**Puerta G1:** el usuario decide si autoriza el registro de un dominio concreto, con registrador, precio, titularidad y condiciones identificados. Sin aprobación, no se compra.

**Criterio de bloqueo:** conflicto jurídico material, dominio no disponible, precio premium no previsto, titularidad poco clara o condiciones desfavorables.

### Fase 2 — Identidad visual mínima

**Objetivo:** disponer de un sistema visual suficiente para construir la primera web sin abrir un proyecto de branding costoso.

**Tareas:**
1. Definir un brief visual a partir de la arquitectura v0.7: orgánico, contemporáneo, limpio, editorial, científico y cálido.
2. Explorar corrientes, redes orgánicas, ramificaciones y sistemas vivos; evitar clichés visuales de IA.
3. Preparar propuestas de logotipo tipográfico provisional, paleta, tipografías, iconografía, estilo fotográfico/ilustrativo y reglas de uso.
4. Comprobar legibilidad, contraste, accesibilidad y adaptación móvil.
5. Revisar que la identidad no sugiera una entidad sin ánimo de lucro ni prometa capacidades científicas o productos no existentes.
6. Mantener los activos en formatos exportables y con licencias claras.

**Entregable:** kit visual mínimo aprobado para la primera versión web.

**Puerta G2:** aprobación del usuario antes de encargar diseño externo, comprar recursos o adoptar definitivamente un logotipo.

### Fase 3 — Web pública en Framer

**Objetivo:** construir un portal institucional ligero, editable visualmente y adecuado a la primera publicación.

**Preparación antes de crear cuenta:**
1. Verificar planes actuales de Framer, límites de páginas/CMS, dominio personalizado, formularios, analítica, ancho de banda, branding, exportación, impuestos y renovación.
2. Comparar el coste total con alternativas razonables, incluida la opción de aplazar la publicación.
3. Recomendar el plan mínimo que cumpla los requisitos reales; no contratar hasta aprobación.

**Estructura inicial de contenidos propuesta:**
- Home.
- Discover — Transformación Generativa de Sistemas.
- Community.
- Research — TGCV y publicaciones con estado de evidencia.
- Framework — VALUE e Inteligencia Transformacional.
- Explore — Playground y experiencias disponibles, claramente etiquetadas.
- Learning.
- Resources.
- About / Contact.

La navegación final se confirmará con la arquitectura v0.7 y se reducirá si la primera versión no tiene contenido suficiente. No crear páginas vacías solo para aparentar amplitud.

**Tareas de construcción:**
1. Crear proyecto y seleccionar plantilla solo después de aprobar el plan y la herramienta.
2. Configurar estilos globales, cabecera, pie, navegación y componentes reutilizables.
3. Construir primero Home y las páginas esenciales con contenido real.
4. Incorporar enlaces a la base documental; no duplicar corpus científico completo en Framer.
5. Configurar formularios solo si existe una necesidad y se ha definido qué datos se recogen, finalidad, acceso y retención.
6. Revisar móvil y escritorio, enlaces, títulos, metadatos, rendimiento y accesibilidad.
7. Mantener el proyecto como borrador/no publicado hasta superar la puerta de lanzamiento.

**Entregable:** web estructurada y revisable en entorno de previsualización.

**Puerta G3:** aprobación de contenidos, estructura y coste antes de conectar dominio o publicar.

### Fase 4 — Publicación documental

**Objetivo:** ofrecer una base de conocimiento abierta, versionada y mantenible, conservando GitHub como fuente maestra.

**Arquitectura de referencia:** GitHub + Markdown/MDX + Astro/Starlight + GitHub Pages, conforme a la arquitectura v0.7.

**Tareas:**
1. Inventariar qué documentos son publicables, cuáles requieren adaptación y cuáles deben permanecer privados o internos.
2. Definir categorías, navegación, metadatos, estado documental, fecha, versión, autoría/licencia y enlaces a fuentes.
3. Preparar una estructura mínima de documentación y un pequeño conjunto inicial de páginas.
4. Evaluar la forma más sencilla de desplegar Astro/Starlight en GitHub Pages, con pasos guiados y sin exigir programación al usuario.
5. Probar localmente o mediante una previsualización controlada antes de publicar.
6. Configurar publicación automática solo tras verificar permisos, repositorio, rama de publicación y flujo de actualización.
7. Documentar cómo añadir, revisar, corregir y retirar una página.
8. Comprobar accesibilidad, navegación, enlaces, visualización móvil, indexación y licencias.

**Regla científica:** las páginas sobre TGCV deben reflejar el estado de evidencia y los límites de los documentos canónicos. No convertir borradores, diseños o simulaciones en resultados validados.

**Entregable:** base documental navegable y publicada o, si la puerta no se supera, lista para previsualización.

**Puerta G4:** aprobación de selección documental, licencias, exposición pública y despliegue.

### Fase 5 — Integración web y documentación

**Objetivo:** que el visitante perciba un ecosistema coherente, sin duplicar fuentes ni crear dependencias innecesarias.

**Tareas:**
1. Definir el dominio/subdominio de documentación y la arquitectura de enlaces.
2. Conectar la web Framer con la base documental.
3. Verificar navegación de ida y vuelta, identidad visual mínima y consistencia de nombres.
4. Evitar que dos plataformas compitan por el mismo contenido o generen versiones divergentes.
5. Probar enlaces directos, rutas, redirecciones y comportamiento móvil.

**Entregable:** recorrido coherente entre Home, secciones institucionales y conocimiento.

**Puerta G5:** aprobación de la integración y de cualquier coste adicional de dominio o plataforma.

### Fase 6 — Revisión y lanzamiento

**Objetivo:** publicar solo cuando la primera versión sea clara, segura, accesible y honesta sobre su alcance.

**Lista de aceptación:**
- Dominio y DNS comprobados; HTTPS activo.
- Navegación clara y responsive en móvil y escritorio.
- Contenidos y enlaces revisados.
- Formularios probados y con recogida mínima de datos.
- Avisos legales y política de privacidad adecuados al tratamiento real y a la jurisdicción aplicable.
- Cookies/analítica configuradas conforme a la normativa aplicable; no activar rastreo no esencial por defecto.
- Accesibilidad básica revisada, con objetivo progresivo WCAG 2.2 AA.
- Estados, fechas, versiones y procedencia visibles cuando corresponda.
- Ninguna experiencia conceptual descrita como producto funcional.
- Ninguna simulación descrita como evidencia empírica.
- Control de cuentas, MFA, recuperación y titularidad de activos.
- Copia/exportación de contenidos y procedimiento de actualización.
- Costes, renovaciones y responsable registrados.
- Revisión final de la marca y de los riesgos jurídicos relevantes antes del lanzamiento público.

**Entregable:** versión pública mínima de AFLUYA y registro de aceptación.

**Puerta G6:** autorización expresa del usuario para publicar.

**Alcance de primera publicación:** portal institucional profesional, base de conocimiento abierta y curada, descripción transparente de las áreas y una vía sencilla de contacto/participación. No es necesario que estén operativos VALUE Explorer, TGCV Playground completo, una comunidad alojada ni ValueLabOS.

### Fase 7 — Mantenimiento y revisión trimestral

**Objetivo:** evitar que precios, condiciones o dependencias queden obsoletos y mantener la web/documentación.

**Cada trimestre:**
1. Revisar precios oficiales, impuestos, renovaciones y cambios de planes de Framer, dominio, GitHub Pages y herramientas efectivamente utilizadas.
2. Revisar límites de uso, almacenamiento, ancho de banda, formularios, analítica y condiciones de exportación.
3. Registrar cambios de producto, seguridad, privacidad, términos y dependencias.
4. Revisar enlaces rotos, formularios, certificados, copias y accesos.
5. Comprobar que los documentos publicados siguen correspondiendo a versiones aprobadas.
6. Evaluar alternativas solo si existe un cambio material de coste, riesgo o funcionalidad.
7. Presentar informe breve de costes reales, previsión anual, riesgos y decisiones necesarias.

**Entregable:** informe trimestral y registro de cambios.

**Regla de coste:** no cambiar de herramienta ni contratar un plan superior sin comparar coste total, esfuerzo de migración, pérdida de funcionalidades y reversibilidad.

## 6. Orden de ejecución y dependencias

Orden recomendado:

1. Fase 0 — Preparación.
2. Fase 1 — Dominio y comprobaciones jurídicas/técnicas.
3. Fase 2 — Identidad visual mínima.
4. Fase 3 — Web Framer.
5. Fase 4 — Publicación documental.
6. Fase 5 — Integración.
7. Fase 6 — Revisión y lanzamiento.
8. Fase 7 — Mantenimiento trimestral.

Las fases 3 y 4 pueden prepararse en paralelo a nivel de contenidos y diseño, pero no deben generar contratación ni publicación sin sus respectivas puertas. La decisión sobre el dominio precede a la conexión del dominio y a la publicación definitiva.

## 7. Reparto de responsabilidades

**Usuario / titular**
- Decide prioridades, contenidos y alcance.
- Aprueba marca, gastos, cuentas, contratación y publicación.
- Conserva titularidad y control de cuentas y activos.
- Acepta o bloquea las puertas de fase.

**Asistente**
- Investiga información pública actualizada cuando sea necesaria.
- Prepara textos, estructura, instrucciones y listas de comprobación.
- Guía paso a paso por interfaces visuales.
- Ayuda a revisar resultados y documenta decisiones.
- No afirma haber creado cuentas, comprado dominios, configurado plataformas o publicado nada sin confirmación verificable.

**Apoyo profesional puntual, solo si se aprueba**
- Atiende tareas jurídicas, fiscales, de privacidad, seguridad o técnicas que excedan el alcance razonable de la implantación guiada.
- Trabaja con alcance, precio, entregable y transferencia de control definidos.

## 8. Presupuesto y control económico

No se fija aquí un precio como vigente. Las estimaciones previas de la arquitectura v0.6/v0.7 son referencias de planificación y deben comprobarse antes de contratar.

Antes de cada gasto se documentará:
- proveedor y plan;
- coste inicial;
- coste recurrente y periodicidad;
- IVA/impuestos y moneda;
- renovación automática y fecha;
- límites y posibles costes variables;
- cancelación, reembolso y transferencia;
- alternativa gratuita y coste de migración.

El usuario aprobará cada gasto por separado. El objetivo es minimizar el coste fijo hasta validar la utilidad de la primera publicación.

## 9. Registro inicial de estado

| Fase | Estado inicial | Evidencia / condición |
|---|---|---|
| 0. Preparación | IN_PROGRESS | El usuario confirma que se parte de cero |
| 1. Dominio | NOT_STARTED | Dominios NOT_VERIFIED; sin compra |
| 2. Identidad | NOT_STARTED | Dirección visual en arquitectura; kit pendiente |
| 3. Framer | NOT_STARTED | Herramienta recomendada, cuenta/plan no contratados |
| 4. Documentación | NOT_STARTED | GitHub es fuente maestra; publicación por configurar |
| 5. Integración | NOT_STARTED | Depende de fases 3 y 4 |
| 6. Lanzamiento | NOT_STARTED | No hay publicación autorizada |
| 7. Mantenimiento | DEFINED_NOT_SCHEDULED | Revisión trimestral definida; no existe seguimiento programado |

**Situación de dominio:** afluya.org — NOT_VERIFIED; afluya.com — NOT_VERIFIED; afluya.es — NOT_VERIFIED. No se ha registrado ni comprado ningún dominio.

## 10. Próxima operación concreta

Completar el cierre de Fase 0 mediante una ficha de inventario y, a continuación, realizar la consulta técnica de los tres dominios en fuentes fiables. La consulta deberá devolver resultados con fecha y fuente, y terminar en una recomendación; no ejecutará compra ni registro.

La primera operación no requiere crear cuentas nuevas, introducir datos de pago ni contratar servicios.

## 11. Control de cambios

### v0.1 — 2026-11-10
- Se transforma la arquitectura estratégica AFLUYA v0.7 en un plan operativo de ocho fases (0–7).
- Se concretan tareas, entregables, criterios de salida y puertas de aprobación.
- Se formaliza el principio de partida desde cero, sin dominios ni servicios contratados.
- Se incorporan instrucciones adaptadas a una persona sin conocimientos de programación y con asistencia paso a paso.
- Se explicitan los controles de gasto, renovaciones, privacidad, accesibilidad, titularidad y reversibilidad.
- Se define la revisión trimestral de herramientas y costes como mantenimiento definido pero no programado.
- No se han creado cuentas, contratado servicios, comprado dominios ni publicado la web o documentación.
- No se modifica `main`, ni el Core científico, RMA, Evidence→Claim Matrix, C09, C10 o las autorizaciones científicas de TGCV.
