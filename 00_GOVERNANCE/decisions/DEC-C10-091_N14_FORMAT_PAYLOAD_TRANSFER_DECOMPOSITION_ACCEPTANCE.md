# DEC-C10-091 — Descomposición semántica de N14: formato, payload y transferencia

**Fecha:** 2026-11-08
**Estado:** ACCEPTED — DOCUMENTAL
**Ámbito:** C10-S, rama `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta la descomposición conceptual de N14 en tres planos distintos: (i) definición versionada del formato/contrato de intercambio; (ii) payload/artefacto concreto; y (iii) eventos temporales de transferencia, recepción, parseo, validación y aplicación. Se refina el N14 existente del catálogo U_G; no se crea un nuevo objeto ni se altera el catálogo de identidades.

## 2. Reglas

1. Formato/contrato y payload tienen identidad y versionado separados. El mismo formato puede producir múltiples payloads; no se presupone cardinalidad 1:1.
2. El formato no es REF automáticamente. Solo es REF si constituye un objeto de dominio con identidad propia y extremos tipados conforme DEC-C10-077; si es propiedad/perfil del CMP, permanece como metadato o artefacto contractual referenciado.
3. El payload tiene identidad/procedencia y revisión propias. Solo se representa como NODE si tiene identidad y relevancia material independiente según el criterio de granularidad; de otro modo se conserva como artefacto de transferencia/evidencia sin forzar NODE.
4. Producción, transmisión, recepción, parseo, validación y aplicación son eventos/etapas distintos. Recibido no implica parseado, validado ni aplicado. La falta de registro no prueba que el evento no ocurriera.
5. N13/A1 y N15/A2 siguen siendo productor y consumidor separados de N14. N07 conserva el canal/endpoint técnico y M el mapping fuente→payload→destino.
6. E12 y E13 siguen siendo relaciones candidatas; no se declaran observadas por esta decisión.
7. Formato, payload, exportación e importación no mantienen cardinalidad necesariamente 1:1. Split, merge o transformaciones requieren lineage y versiones por etapa sin sobrescribir artefactos previos.
8. Un hash/digest puede respaldar integridad de bytes solo en el ámbito/etapa declarados; no demuestra equivalencia semántica, compatibilidad, aplicación ni éxito funcional.
9. DEC-C10-074 y TGCV-C10S-JCS-1 gobiernan el envelope UDG-01; no se extienden automáticamente al payload. Su serialización/canonicalización requerirá especificación propia si se necesita.
10. Una ruta alternativa A1→N14→A2 solo cuenta como funcional si se demuestra bajo el mismo F*, frontera, granularidad G, horizonte H y condiciones comparables. La existencia documental o recepción del payload no demuestra Reach ni substituibilidad.

## 3. Estado y límites

Queda aceptada la descomposición semántica y sus reglas conceptuales. Permanecen OPEN el formato, esquema, codificación, payload, identidades/revisiones reales, cardinalidades observadas, mapping M, lineage, endpoint, eventos de transferencia, compatibilidad, aplicación, F*, evidencia y cobertura.

No se asignan IDs ni se crean filas NODE/REF/EDGE/CMP. No se sella IAM, no se declara roster exhaustivo ni cobertura. No autoriza acceso técnico, captura, parser, validator, fixtures, implementación, Design Freeze ni ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.