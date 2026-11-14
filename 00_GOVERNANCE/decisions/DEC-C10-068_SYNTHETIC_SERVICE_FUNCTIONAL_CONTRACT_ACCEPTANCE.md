# DEC-C10-068 — Aceptación del contrato funcional sintético del servicio de referencia

**Fecha:** 2026-11-07  
**Estado:** ACCEPTED — conceptual/documental  
**Rama de registro:** `research/c10-s-consolidation-draft`  
**Ámbito:** C10-S / Opción A / DGP sintético

## 1. Decisión

El usuario acepta el servicio lógico sintético de procesamiento de solicitudes y la regla `RUL-SVC-ENABLE-PROFILE-01` como contrato funcional de referencia de C10-S, conforme a la propuesta presentada en `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`.

La unidad de referencia es una instancia lógica versionada de un servicio software de procesamiento de solicitudes. El objeto P0 es su paquete declarativo de configuración; runtime, binarios, infraestructura, permisos efectivos, recursos y estado ambiental permanecen fuera de P0 según las fronteras ya aceptadas.

## 2. Contrato aceptado

Parámetros lógicos obligatorios de esta instancia sintética:

- `PAR-SVC-ENABLED`: BOOL, dominio `{false,true}`; declara si el servicio debe aceptar solicitudes.
- `PAR-SVC-PROFILE`: ENUM, dominio `{STANDARD, READ_ONLY, DISABLED}`; declara el modo funcional deseado.

Regla constitutiva:

- **ID:** `RUL-SVC-ENABLE-PROFILE-01`
- **Owner lógico:** `CMP-SERVICE-LOGIC` (identificador lógico provisional; la identidad/versionado de instancia se completa en el contrato de configuración).
- **Scope:** configuración declarativa completa de la unidad lógica del servicio.
- **Efecto:** `REQUIRE`.
- **Condición:** `PAR-SVC-ENABLED=true ⇒ PAR-SVC-PROFILE∈{STANDARD, READ_ONLY}`.
- **Expresión:** `OR(NEQ(PAR-SVC-ENABLED,true), IN(PAR-SVC-PROFILE,{STANDARD,READ_ONLY}))`.

Contrastes conocidos: ENABLED=true con STANDARD o READ_ONLY satisface; ENABLED=true con DISABLED viola; ENABLED=false con cualquiera de los perfiles declarados no queda restringido por esta implicación. No se añade la implicación inversa.

El contrato es la fuente constitutiva interna del mundo sintético del DGP, fijada antes de generar y analizar resultados. No es una norma externa ni una afirmación empírica sobre servicios reales.

## 3. Alcance y límites

La aceptación comprende la especialización del servicio lógico, los dos parámetros obligatorios y la regla constitutiva tal como están definidos arriba. `PAR-SVC-RETRY-COUNT` queda fuera del núcleo mínimo.

No quedan aprobados ni congelados por esta decisión:

- identificador/versionado concreto de la instancia CMP y serialización final;
- roster exhaustivo de parámetros más allá de los dos aceptados;
- tabla física de mapping, nombres de plataforma o producto;
- detalles IAM por escenario, predicados de evidencia y cobertura;
- tolerancias, oráculo, cegamiento, error de medición y adjudicación de F*;
- fixtures, parser, validadores, simulaciones, ejecución o implementación;
- estimandos, identificación causal, DGP numérico, parámetros o potencia.

La preservación semántica F1/A1 y la aplicación F2/A2 siguen siendo obligaciones de diseño y validación, no resultados ya demostrados. FP-03/06/07/08 conservan sus funciones diferenciadas.

## 4. Efecto sobre C10-S

Esta decisión cierra la elección conceptual de una regla constitutiva sintética no tautológica con verdad conocida ex ante. Permite continuar el cierre de la identidad/versionado CMP, roster IAM y mapping semántico concreto, y después completar los contratos de prueba/oráculo.

No constituye Design Freeze. No autoriza implementación, validación ejecutable, simulación ni ejecución científica.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.

## 5. Trazabilidad

- Propuesta aceptada: `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`.
- Maestro: `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, §175 (propagación de DEC).
- Plan de cierre: `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md`.
- Matriz de cierre: `00_GOVERNANCE/SIP/C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`.
