# DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001

**Fecha:** 2026-11-11  
**Estado:** ACCEPTED — aprobación expresa del responsable científico en conversación  
**Ámbito:** C10-S / PB / variante B1 / rama `research/c10-s-consolidation-draft` / PR #116  
**Tipo:** decisión de identidad y versionado documental; no decisión de diseño científico ni autorización técnica.

## 1. Decisión aceptada

Se acepta la armonización entre `DEC-C10S-B1-UNIT-001` y `DEC-C10-069`:

1. **Contrato común:** `contract_id=C10S-SVC-REQUEST-PROCESSOR` y `contract_version=1.0.0`, comunes a las UE mientras mantengan la misma semántica contractual.
2. **Plantilla funcional común:** la definición CMP/PAR/RUL aceptada conceptualmente se mantiene como plantilla compartida, versionada por contrato. Compartir plantilla no equivale a compartir estado mutable ni instancia ejecutable.
3. **Instancia por UE:** cada UE tiene un `instance_id` propio, único en el roster C10-S, y una línea de `instance_version` monotónica e independiente. Una nueva versión conserva el `instance_id` solo cuando se mantiene la continuidad funcional conforme a las reglas de DEC-C10-069.
4. **Componentes locales:** `component_id` identifica un componente dentro de una instancia. La clave inequívoca global de referencia es compuesta: `(instance_id, component_id)`. La misma etiqueta local de componente puede aparecer en instancias distintas sin implicar identidad compartida.
5. **Instancia de referencia DEC-C10-069:** `C10S-SVC-REQUEST-PROCESSOR-001` se conserva como instancia ejemplar/de referencia documental; no se reutiliza como `instance_id` de todas las UE.
6. **Versionado contractual:** se conserva la política MAJOR.MINOR.PATCH aceptada en DEC-C10-069. `contract_version` e `instance_version` no se confunden ni se incrementan por las mismas causas.

## 2. Reglas de identidad y matching

- Unicidad de `instance_id` se comprueba contra el roster completo de UE del DGP, incluyendo instancias históricas/supersedidas según el registro de identidad.
- `instance_version` es entero positivo monotónico dentro de cada `instance_id`; las revisiones son inmutables y no sobrescriben versiones anteriores.
- El cambio de contenido compatible genera nueva versión de instancia, no nueva identidad; cambio incompatible de continuidad exige nueva identidad o relación de sucesión explícita.
- `component_id` no es global por sí solo. Toda referencia externa incluye `instance_id`; las relaciones de owner, parámetros y reglas resuelven dentro de la instancia.
- Igualdad de `contract_id`, `contract_version`, definición CMP, nombre o hash no prueba aislamiento físico ni independencia de recursos/estado.

## 3. Límites y no-claims

Esta decisión resuelve identidad lógica y versionado documental. **No demuestra aislamiento efectivo** de recursos, almacenamiento, estado, información, agentes, credenciales, dependencias, colas, latencia o infraestructura. Esos elementos permanecen sujetos al contrato material PB, IAM, auditoría de vías colaterales y pruebas de seguridad.

No asigna todavía los valores concretos de `instance_id` a cada UE: deben derivarse del roster cerrado y persistirse con provenance, sin inventar cardinalidad. No define serialización MET, schema físico, formato, hash, ACL, mapping implementado, fixtures, parser, ni oráculo validado.

No altera Opción A, DEC-C10-068, DEC-C10-069 en su alcance original, TGCV Core, RMA, Evidence→Claim Matrix, STATUS ni claims. No autoriza implementación, simulación, estimación ni ejecución científica.

## 4. Justificación

DEC-C10-069 fijó una instancia lógica ejemplar y su política de versionado. DEC-C10S-B1-UNIT-001 fijó una entidad B1 por UE asociada a un servicio aislado/versionado. La presente decisión conserva el contrato funcional común y evita colapsar las instancias aisladas en un único `instance_id`, manteniendo separadas identidad de plantilla, identidad de instancia y clave de componente.

## 5. Criterios de aceptación documental

- [x] Aprobación expresa del usuario.
- [x] Contrato y versión comunes delimitados.
- [x] Instancia lógica única por UE establecida.
- [x] Versionado independiente por instancia.
- [x] Identidad local de componentes y clave compuesta establecidas.
- [x] Instancia de referencia DEC-C10-069 preservada.
- [ ] Roster completo de UE y asignación concreta de IDs.
- [ ] Evidencia IAM/ACL y pruebas de aislamiento material.
- [ ] MET/schema físico y matching ejecutable.

**Resultado:** decisión aceptada y persistible; cierre documental de identidad completado. Los tres últimos puntos permanecen abiertos y no invalidan la decisión lógica aceptada.
