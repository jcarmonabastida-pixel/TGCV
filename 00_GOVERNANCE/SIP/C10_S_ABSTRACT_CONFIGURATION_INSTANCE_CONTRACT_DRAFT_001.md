# C10-S — Contrato abstracto de instancia de configuración

**ID:** C10-S-ABSTRACT-INSTANCE-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA DOCUMENTAL; no aprobado, congelado ni implementado.  
**Decisión de cardinalidad:** DEC-C10-056.  
**Base:** DEC-C10-052/053/054/055; catálogo atómico; matriz IAM; reconciliación SM/FP; microdominio Opción A.

## 1. Propósito y límite

Define el esqueleto abstracto de una instancia de paquete de configuración comparable en origen y destino. No fija nombres concretos de componentes, claves de parámetros, valores, límites numéricos, enumeraciones, reglas sustantivas ni topología del servicio. Tampoco constituye un schema ejecutable.

Una instancia se representa como:
C = (ID_C, V_C, CMP, PAR, REF, RUL, POL?, MET)
donde POL es módulo opcional y MET contiene metadatos contractuales y de procedencia. CMP/PAR/REF/RUL son clases constitutivas; su cardinalidad concreta sigue reglas explícitas.

## 2. Cardinalidades base aprobadas

| Clase | Cardinalidad mínima | Regla |
|---|---:|---|
| CMP | 1 | Al menos un componente. Un conjunto vacío es SCOPE_ERROR, no NA. |
| PAR | 1 | Al menos un parámetro. Un conjunto vacío es SCOPE_ERROR salvo rediseño explícito y justificado del objeto antes del estudio. |
| REF | 0 | Puede ser vacío solo con inventario exhaustivo y declaración ex ante en IAM; vacío no significa cobertura desconocida. |
| RUL | 1 | Al menos una regla/restricción. Vacío es SCOPE_ERROR en el DGP base confirmatorio. |
| POL | 0 | Ausente por diseño en núcleo confirmatorio mínimo; si se incluye, módulo condicional declarado antes de Z/B. |
| MET | Obligatorio | Identidad/versión/procedencia y sellado de IAM obligatorios. |

La regla CMP≥1, PAR≥1 y RUL≥1 impide que una instancia trivial sin objeto/configuración/reglas sea clasificada como éxito. REF≥0 evita inventar dependencias donde no existen, pero exige demostrar que el inventario está completo.

## 3. Entidades abstractas

### 3.1 CMP — componentes

Cada componente contiene:
- component_id: identificador estable dentro de la instancia y versión;
- component_class: clase/rol funcional tipado;
- component_scope: pertenencia al límite de la configuración;
- referencias a parámetros y reglas según relaciones declaradas;
- estado de inclusión/exclusión y evidencia de inventario.

Identidad local de registro no equivale a identidad semántica entre origen y destino. El mapping M establece correspondencia; no se infiere por igualdad de nombre/hash.

### 3.2 PAR — parámetros

Cada parámetro contiene:
- parameter_key;
- owner_component_id;
- type ∈ {BOOL, INT, DECIMAL, ENUM, STRING, REF};
- state ∈ {ABSENT, NULL, DEFAULT, VALUE};
- value solo cuando el estado y tipo lo permiten;
- dominio/escala/unidad cuando proceda;
- requiredness REQUIRED | OPTIONAL | CONDITIONAL;
- default contract cuando exista;
- versión/procedencia del valor.

La matriz IAM fija qué predicados son obligatorios/condicionales por clave. ABSENT, NULL, DEFAULT y VALUE no son intercambiables.

### 3.3 REF — referencias

Cada referencia contiene:
- ref_id;
- source_component_id;
- target_component_id o identificador externo tipado;
- relation_type;
- direction;
- role;
- multiplicity solo cuando el contrato lo requiera;
- integridad y estado de resolución.

El conjunto REF puede ser vacío si IAM declara cardinalidad 0 y la cobertura del inventario es completa. Una referencia externa no inventariada como objeto interno debe declararse en la frontera y en dependencias técnicas externas.

### 3.4 RUL — reglas y restricciones

Cada regla contiene:
- rule_id;
- scope explícito (componente, parámetro, relación o GLOBAL);
- AST declarativo acíclico;
- tipo de resultado lógico TRUE | FALSE | UNKNOWN;
- efecto REQUIRE | FORBID;
- precedencia solo cuando sea funcionalmente significativa;
- metadatos temporales solo cuando se active semántica temporal.

Se exige al menos una regla/restricción en el DGP base. No se permite código ejecutable, llamadas arbitrarias, I/O, efectos laterales ni evaluación dependiente de red/reloj no declarado. El tratamiento de conflicto entre reglas y UNKNOWN permanece pendiente de contrato semántico específico.

### 3.5 POL — políticas

POL se omite por diseño en el núcleo confirmatorio mínimo conforme DEC-C10-053. El IAM debe consignar POL_ABSENT_BY_DESIGN. Si un escenario secundario incorpora POL, sus roles, scopes y reglas se describen; no se infiere permiso efectivo ni seguridad por mera preservación del paquete.

### 3.6 MET — metadatos

MET incluye al menos:
- contract_id, contract_version;
- instance_id, instance_version;
- source_id/version, destination_id/version;
- mapping_id/version;
- provenance_refs;
- IAM_id/version/hash;
- identidad de oráculo/criterio y versiones;
- timestamps y actor/proceso de creación/revisión;
- hash de artefactos y registro de cambios.

Hash y nombre son controles de identidad de artefacto, no prueba de identidad funcional.

## 4. Correspondencia origen/destino

Se distinguen:
- C_src: configuración fuente observada;
- M: mapping explícito versionado;
- C_dst_decl: configuración destino declarada/producida;
- C_dst_applied: estado efectivamente aplicado y observado;
- E_dst: entorno destino, registrado fuera del paquete.

M debe declarar correspondencias de CMP/PAR/REF/RUL, transformaciones tipadas, campos omitidos, defaults, conversiones, pérdida potencial y reglas de unknown extension. No se permite que ausencia de correspondencia se convierta silenciosamente en eliminación, default o NA.

El contrato no exige identidad byte-a-byte. Exige preservación de significado funcional según F*, y distingue los predicados formales FP-01, integridad FP-02, semántica FP-03, compatibilidad FP-04, seguridad FP-05, aplicación FP-06 y verificación FP-07.

## 5. Contrato de cobertura y clases vacías

IAM registra cardinalidad observada/esperada por clase y fuente de inventario. Para REF=0 debe acreditar búsqueda/cobertura exhaustiva del límite de configuración, incluidos dependencias internas y externas pertinentes. La evidencia insuficiente se codifica ?; nunca REF=0 ni NA.

CMP=0, PAR=0 o RUL=0 produce SCOPE_ERROR en el DGP base según DEC-C10-056. No se convierte en NA. Si el dominio real exige un paquete sin alguno de esos elementos, se requiere rediseñar y aprobar el contrato de unidad antes de cualquier generación/asignación; no se adapta post hoc.

## 6. Invariantes del contrato

1. Cada PAR tiene exactamente un owner CMP dentro del límite, salvo que un contrato explícito admita parámetro global.
2. Cada REF interna tiene extremos resolubles en CMP; REF externa queda tipada y declarada como dependencia externa.
3. Cada RUL tiene scope explícito, incluido GLOBAL.
4. Cada regla tiene AST tipado, acíclico y dentro del presupuesto 4/16/16 de DEC-C10-054.
5. Cada valor respeta su type/state/domain; estados no se colapsan.
6. Cada correspondencia M es explícita, versionada y adjudicable.
7. Ningún campo desconocido se descarta silenciosamente.
8. CMP/PAR/RUL no vacíos y REF posiblemente vacío se sellan en IAM pre-Z/B.
9. C_dst_decl y C_dst_applied son artefactos/estados distintos.
10. El objeto no incorpora como propiedades internas E_dst, C_dep, recursos, permisos efectivos ni runtime.

## 7. Abiertos antes de especializar instancias

- Definición de la unidad de servicio y frontera exacta del paquete.
- Clases/roles de componentes y cardinalidades máximas.
- Claves abstractas de parámetros, requiredness, dominios y valores.
- Relaciones/ref_types y reglas de multiplicidad.
- AST concreto, precedencia, conflictos y UNKNOWN.
- Mappings y conversión de estados/valores.
- Contrato de evidencia para inventarios vacíos REF.
- Criterios FP-04/05/06 y oráculo independiente.
- Diseño de IAM seguro y reproducible.

## 8. Dictamen

Este contrato convierte la decisión de cardinalidad en una estructura abstracta comparable sin introducir valores de escenario ni código ejecutable. Es una propuesta de contrato, no una instancia, schema validado, oráculo, truth, fixture ni experimento.

**Estado:** DEC-C10-056 aceptada; contrato abstracto Draft 001; parámetros concretos, instancias, IAM operativo, mapping final, oráculo y validación técnica pendientes. Sin ejecución científica autorizada.
