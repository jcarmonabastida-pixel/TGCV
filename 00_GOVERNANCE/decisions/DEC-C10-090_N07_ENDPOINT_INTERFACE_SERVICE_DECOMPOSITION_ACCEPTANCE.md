# DEC-C10-090 — Descomposición semántica de N07: endpoint, interfaz y servicio

**Fecha:** 2026-11-08
**Estado:** ACCEPTED — DOCUMENTAL
**Ámbito:** C10-S, rama `research/c10-s-consolidation-draft`

## 1. Decisión

Se acepta la descomposición conceptual de N07 en tres objetos potencialmente distintos: (i) endpoint técnico concreto; (ii) contrato/interfaz de comunicación; y (iii) servicio proveedor. La etiqueta N07 no debe tratarse como una entidad única indiferenciada.

## 2. Reglas de clasificación

1. Un endpoint (URL, socket, puerto, topic, canal o punto de acceso) no es CMP ni REF por el mero hecho de ser direccionable. Se representa como atributo/recurso de interfaz o NODE P1 separado solo si supera el criterio de granularidad y tiene identidad/versionado y relevancia material independiente.
2. Un contrato/interfaz es REF únicamente si constituye un objeto de dominio con identidad propia y extremos tipados. Si es una propiedad del CMP, permanece como atributo/artefacto contractual referenciado. No se infiere REF desde endpoint, FK o EDGE.
3. El servicio proveedor es CMP únicamente si posee identidad contractual propia (component_id, clase y versión/revisión), lifecycle y frontera funcional diferenciados. Una fachada o capacidad interna no crea automáticamente un CMP adicional.
4. Un servicio externo consumido por la instancia focal no se incorpora al roster CMP interno por el mero consumo. Se conserva como externo y se modelan sus relaciones/perímetro P2 según evidencia y contrato.
5. Una conexión observada puede representarse como EDGE; REF es un objeto de dominio con identidad propia. EDGE y REF no se infieren entre sí.
6. La falta de información se adjudica UNKNOWN, nunca como ausencia demostrada.
7. La aplicación por instancia requiere identidad, extremos, dirección, owner, boundary_class, snapshot, mapping, rutas F/A, compartición y evidencia suficientes; esta decisión no los presume.

## 3. Estado y límites

Queda aceptada la descomposición semántica y la regla de clasificación conceptual de N07. Permanecen OPEN endpoint, protocolo, contrato/interfaz, servicio proveedor, topología, identidades, mappings, rutas, snapshots, cobertura y evidencia reales.

No se asignan IDs ni se crean registros REF/EDGE/CMP. No se sella IAM, no se declara roster exhaustivo ni cobertura. No autoriza inspección técnica, llamadas de red, pruebas de conectividad, acceso a credenciales, parser, validator, fixtures, implementación, Design Freeze ni ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.