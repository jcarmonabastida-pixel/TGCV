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



## 9. Reconciliación C_src/C_dst/M con F1/F2/A1/A2, IAM y F* (2026-11-06)

**Estado:** crosswalk documental propuesto; no modifica DEC-C10-053/054/055/056 ni congela contrato/instancia.

| Clase/objeto | C_src | F1/F2 | A1/A2 | C_dst declarado/aplicado | Control IAM/F* |
|---|---|---|---|---|---|
| CMP | Inventario, clase/rol y scope | Mapping de identidad/clase y composición explícita | Mismo criterio de identidad funcional | Cobertura, clase y duplicación sobre estado aplicado | CMP≥1; correspondencia adjudicable |
| PAR | Clave, owner, tipo, estado, valor/dominio, unidad y requiredness | Conversión tipada sin colapsar estado/semántica | Mismo significado bajo ruta neutral | Tipo, valor y estado sobre destino aplicado | PAR≥1; O/C/NA/? por propiedad |
| REF | Extremos, tipo, dirección, rol, multiplicidad e integridad | Correspondencia de extremos y referencias | Mismo universo y criterio | Integridad y dependencias declaradas | REF≥0 solo con IAM/cobertura exhaustivos |
| RUL | AST tipado, scope, efecto y UNKNOWN | Transformación sin alterar lógica/ámbito/efecto | Mismo criterio semántico | Reglas aplicadas, no Outcome/Value | RUL≥1; AST 4/16/16, REQUIRE/FORBID |
| POL | Ausente por diseño salvo módulo secundario | Mapping si se activa | Igual contrato | Política declarada separada de permisos efectivos | POL condicional; FP-05 independiente |
| MET | Identidad/versiones/procedencia | Registrar versión de F1, S2, M | Registrar versiones A1/A2 y S1 | Sellar destino declarado/aplicado | MET obligatorio; FP-08 separado |
| E_dst/runtime | Fuera de C_src | Dependencias, permisos, recursos/runtime externos | Mismas variables externas | Compatibilidad/seguridad/aplicación | FP-04/05 y C_dep fuera del objeto |

### 9.1. Pipeline de correspondencia

1. Sellar antes de Z/B C_src, contratos/versiones, universo CMP/PAR/REF/RUL, M, IAM, C0, G, H, criterios FP y oráculos.
2. M contiene correspondencias tipadas/versionadas; distingue MAPPED, UNMAPPED, AMBIGUOUS y NOT_APPLICABLE. La falta de correspondencia no se convierte tácitamente en eliminación, default o NA.
3. F1 produce S2 y F2 aplica/verifica destino; A1/A2 siguen ruta S1. S1/S2 no son C_dst aplicado.
4. Capturar C_dst declarado y C_dst aplicado por separado, con snapshot y evidencia independiente.
5. FP-01/02/03 evalúan contenido/correspondencia; FP-04/05 entorno/seguridad; FP-06 aplicación; FP-07 verificación; FP-08 gate probatorio. Evitar doble conteo.
6. F* se adjudica por ruta completa, sin compensación. Outcome y Value quedan fuera del oráculo.

### 9.2. Discrepancia DEFAULT abierta

El contrato abstracto §3.2 usa DEFAULT; la matriz M §4 distingue DEFAULT_DECLARED, DEFAULT_INHERITED y DEFAULT_ENV_RESOLVED. No son sinónimos automáticos. Propuesta no aprobada: DECLARED/INHERITED serían metadatos de resolución del estado DEFAULT; ENV_RESOLVED sería observación de E_dst, externa a C_src/C_dst. Requiere reconciliación con catálogo PAR e IAM. Hasta entonces, los casos donde cambie el significado quedan ?.

### 9.3. Cardinalidad y reglas

DEC-C10-056 prevalece sobre formulaciones anteriores que permitían RUL=0: CMP≥1, PAR≥1, RUL≥1; REF≥0 solo con IAM pre-Z/B y cobertura exhaustiva; POL ausente por diseño salvo módulo secundario; MET obligatorio. DEC-C10-054 fija AST acíclico, profundidad 4, 16 átomos/regla, 16 reglas/paquete y efectos REQUIRE/FORBID. Esto no equivale a parser validado.

### 9.4. Criterio de cierre

Siguen abiertos máximos/clases CMP; claves/dominios PAR; universo/tipos/multiplicidad REF; gramática y UNKNOWN/conflictos RUL; representación DEFAULT; M por clase y conversiones; IAM completo; evidencia de C_dst aplicado; oráculo/cegamiento/error. Sin parámetros, fixtures, implementación ni ejecución.


## 10. Reconciliación normativa de DEFAULT (DEC-C10-054)

**Estado:** interpretación documental alineada con una decisión ya aceptada; no es una nueva DEC ni amplía su alcance.

El contrato §3.2 conserva \`state ∈ {ABSENT,NULL,DEFAULT,VALUE}\` como estado de alto nivel. Cuando \`state=DEFAULT\`, exige \`default_kind ∈ {DECLARED,INHERITED}\`: DECLARED es default declarado en paquete/contrato; INHERITED es default heredado mediante regla explícita, con ámbito y procedencia identificables.

\`DEFAULT_ENV_RESOLVED\` no es estado de PAR ni valor de C_src/C_dst. Es observación de E_dst/runtime: se registra en snapshot ambiental enlazado a parameter_key, versiones, identidad del entorno, instante/ventana, valor resuelto y procedencia. No se reescribe como DECLARED o INHERITED.

Así se conserva el enum de alto nivel y se materializa la distinción tripartita ya exigida por DEC-C10-054. Si el origen no permite distinguir DECLARED de INHERITED, el mapping semántico es UNKNOWN salvo evidencia independiente suficiente. La falta de observación ambiental tampoco equivale a ausencia de default.

La equivalencia se adjudica en dos planos: (i) contrato/paquete y (ii) resolución efectiva en E_dst. Igualdad del valor resuelto no demuestra equivalencia del origen; igualdad del contrato no demuestra que el entorno resolviera el mismo valor.

**Pendiente:** campos exactos del snapshot E_dst, evidencia/procedencia, reglas de herencia por clave y predicados FP primarios. Sin instancia, parser, fixture ni ejecución.

**Precedencia interna:** La formulación de §9.2 que calificaba esta reconciliación como propuesta no aprobada queda supersedida por §10: DEC-C10-054 ya aceptó la distinción; §10 fija únicamente su representación coherente.
