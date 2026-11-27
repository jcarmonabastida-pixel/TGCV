# Relationships and structure in a water supply system

**Asset ID:** TV-DIA-002  
**Version:** 0.1  
**Status:** Draft — conceptual and visual review pending  
**Owner:** TRANSFORMATIONAL VALUE editorial project  
**Source format:** Mermaid flowchart  
**Purpose:** Illustrate how physical components, material flows, information/control connections and external dependencies combine to form a system structure.

## Source files

- Spanish: `source/system-relationships-water-network.es.mmd`
- English: `source/system-relationships-water-network.en.mmd`

Both language variants use the same node identifiers, connections, arrow styles and structural grouping. Reader-facing labels differ by language.

## Conceptual interpretation

The diagram presents a deliberately simplified water supply system. Solid arrows represent the principal physical flow of water through the network. Dashed arrows represent information, control signals or external support relationships, as labelled. The feedback path runs from distribution measurements through monitoring and control to pump and valve adjustments; the resulting operating conditions can then be measured again.

The electricity supply and maintenance function are shown as external dependencies for selected equipment. Their placement outside the central physical flow is a modelling choice for this illustration, not a universal boundary decision. A different analysis may include them within the system boundary.

The diagram is a teaching schematic, not an engineering design, complete process-flow diagram, control-system specification or validated model of a particular installation. It omits many real-world features, including treatment stages, storage arrangements, network topology, safety systems, demand variability and detailed control logic.

## Spanish reader-facing text

**Caption**

Esquema simplificado de una red de suministro de agua. Las flechas continuas representan el flujo físico principal; las discontinuas muestran mediciones, señales de control y dependencias externas seleccionadas. La realimentación conecta las mediciones de la red con los ajustes de bombas y válvulas.

**Alternative text**

Diagrama de izquierda a derecha. El flujo principal de agua conecta un depósito, una instalación de tratamiento, una estación de bombeo, una red de distribución y unas zonas de consumo mediante flechas continuas. Desde la red de distribución salen conexiones discontinuas hacia sensores; estos envían señales a un sistema de supervisión y control, que transmite órdenes a la estación de bombeo y ajustes a las válvulas. Las válvulas se conectan de nuevo con la red de distribución. El suministro eléctrico aporta energía a la estación de bombeo y el mantenimiento aporta inspección y reparación a la estación y a las válvulas, mediante conexiones discontinuas. El esquema diferencia flujos físicos, información y control, y dependencias externas; representa una simplificación didáctica, no una instalación completa.

## English reader-facing text

**Caption**

Simplified schematic of a water supply network. Solid arrows represent the main physical flow; dashed arrows show selected measurements, control signals and external dependencies. The feedback path connects network measurements with pump and valve adjustments.

**Alternative text**

A left-to-right diagram. The main water flow connects a reservoir, treatment facility, pumping station, distribution network and demand zones using solid arrows. Dashed connections run from the distribution network to sensors; sensors send signals to a monitoring and control system, which sends commands to the pumping station and adjustments to valves. The valves connect back to the distribution network. The electricity supply provides energy to the pumping station, while maintenance provides inspection and repair to the station and valves through dashed connections. The diagram distinguishes physical flows, information and control, and external dependencies; it is a simplified teaching schematic, not a complete installation.

## Publication checks

- [ ] Confirm conceptual accuracy and the distinction between physical flows, information/control and dependencies.
- [ ] Render both language variants and confirm identical node identities and connections.
- [ ] Check label legibility and responsive presentation at desktop and mobile widths.
- [ ] Confirm that arrow styles remain distinguishable without colour.
- [ ] Confirm the caption and alternative text against the final Chapter 1 wording in both languages.
- [ ] Confirm third-party rights and select an explicit asset licence before publication.

The two Mermaid sources are editable and language-specific. Rendering, accessibility and publication checks remain pending.
