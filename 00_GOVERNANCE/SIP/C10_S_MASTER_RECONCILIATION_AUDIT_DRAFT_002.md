> **SUPERSEDIDA (2026-11-05).** La auditoría MRA-002 corrigió la falsa laguna histórica, pero no cubrió suficientemente la no-regresión de las formulaciones vigentes §§53–130 ni los contratos estadísticos 165–183. La auditoría vigente es C10_S_MASTER_RECONCILIATION_AUDIT_DRAFT_003.md y el plan vigente es Draft 004.

---

# C10-S — Auditoría de alineación del plan con el maestro vigente
**ID:** C10-S-MRA-002 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** AUDITORÍA DOCUMENTAL ASISTIDA / NO INDEPENDIENTE  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116  
**Objeto:** comprobar cobertura histórica y alinear el plan operativo con las arquitecturas más recientes del maestro, sin reabrir recuperación ya completada.

## 1. Dictamen

La conclusión de MRA-001 sobre una laguna §§131–163 era errónea. El maestro contiene la integración histórica y no requiere recuperar esos intervalos:

| Conversación | Maestro |
|---|---|
| 130 | §16 |
| 131–137 | §§17–24 |
| 138–163 | §§25–50 |
| 164 | §51 |
| 165–183 | síntesis integrada en §52 |

El texto XSYNC-138-01…10 está en §§25–28 y su tracker auxiliar documenta estado y trazabilidad. La fuente DOCX `Notes_261104_163033.docx` cubre 165–183; su contenido se integra resumidamente en §52 y se inventaría en `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`, además de los contratos DGP, estimandos y pruebas. La síntesis no es una transcripción literal del DOCX, pero no existe una laguna de contenido que obligue a reabrir recuperación para planificar.

## 2. Fuentes y artefactos cotejados

- `00_GOVERNANCE/README.md` en `main`: regla de reconstrucción histórica, precedencia GitHub y gates.
- Maestro C10-S §§16–52: correspondencia de 130–183.
- Maestro §§53–69: especificación candidata integrada, intervención B, D1/D2, q_X*, población, unidad/interferencia, F*, medición y primera etapa.
- Maestro §§70–81: Opción A, snapshots, identidad/versionado, Reach, horizonte, predicados, fichas F1/F2/A1/A2 y compatibilidad del microdominio.
- Maestro §§82–130: U_G, evidencia/procedencia, decisiones DEC-C10-051…065, contratos y reconciliaciones documentales.
- Auxiliares: XSYNC tracker; C10-D1/S4-R estimand reconciliation; causal architecture reconciliation; integrated reconciliation audit; DGP temporal/roles; Decision Log; Closure Control Matrix; Test Contract Register; recovery register y recovery audit.

## 3. Arquitectura que el plan debe respetar

### 3.1 Intervención y microdominio

Opción A: migración de configuración entre entornos software. Unidad lógica de servicio y objeto de configuración versionado. B provisiona el adaptador/dependencia focal y no ejecuta las transformaciones funcionales. F1 es conversión; F2 aplicación/validación en destino; A1/A2 son alternativas candidatas cuya independencia debe demostrarse. F* es criterio funcional, no Value.

### 3.2 Cadena técnica y transformacional

`Z → B → W_attempt → S_install → (C_install,C_integrity,C_compat,C_oper) → C_dep* → A_f*(t) → D_f* → ΔT_acc* → Reach_H → Π_H → Known/Consider → Sel → Start → Exec → O → V`.

No colapsar asignación, provisión, intento, éxito, dependencia, accesibilidad, apertura basal→post, cambio completo del espacio, Reach, trayectoria, selección, ejecución, Outcome y Value. `C_dep*` es la conjunción de cuatro componentes; la distribución conjunta de 16 patrones debe especificarse, sin independencia por defecto. `A_f*` deriva de todos los predicados constitutivos; `D_f*=I(A_f,base*=0 ∧ A_f,post*=1)`; A_f es proyección focal de `ΔT_acc*`, no sustituto.

### 3.3 D1/D2 y estimandos

D1: intento control .25/tratamiento 1; éxito técnico condicional candidato .80; C_dep final .20/.80 y primera etapa .60. D1 principal solo condicionado a justificar el comparador ordinario. D2: intento control 0/tratamiento 1; C_dep final 0/.80 y primera etapa .80. §66 recomienda D2 como candidato preferente mecanístico y D1 como contraste incremental secundario; selección primaria sigue abierta y requiere aceptación explícita. Parámetros ilustrativos no son datos ni decisiones.

Separar ITT_Z de política, efecto de paquete, primeras etapas en C_dep/A_f/D_f/ΔT_acc, LATE_f local, θ_Af(q*) focal y θ_A(q) general C10-D1. La aleatorización no prueba exclusión. No extrapolar LATE a ATE/ATT ni equiparar D1/D2.

### 3.4 Población, régimen y condiciones

P*_{τ2} y P*_F tienen objetivos distintos. q_X* es régimen común candidato sobre condiciones/historias basales; C_c delimita condiciones constitutivas y L_m historia temporal. q_L* solo si el diseño secuencial lo requiere. Factibilidad/positividad se verifica por historia. UE/UA/UO, clúster e interferencia deben definirse. No ajustar ITT por variables postratamiento.

### 3.5 Medición, Value y ausencia

A/O/V separados y medidos independientemente; Value vectorial es recomendación provisional. P181/P182/P183 son contratos propuestos, no ejecutados. Missingness, censura, selección postasignación, cotas y sensibilidad se evalúan por estimando; ausencia no equivale a cero ni inaccesibilidad.

### 3.6 Estadística

La arquitectura estadística existe en §§18–23 y 39, 52, 66, 68–69. No está cerrada cuantitativamente: N, réplicas, potencia, precisión, error Monte Carlo, cobertura, weak-IV, δ/ε, multiplicidad, tolerancias y reglas de inconclusión requieren justificación ex ante. N=2000 y R=1000 son candidatos provisionales.

### 3.7 Evidencia U_G

U_G es infraestructura observacional/procedencia/cobertura/adjudicación, no truth del generador. DEC-C10-059…065 y OAS están especificados documentalmente, pero no hay schema freeze ni validación física del motor. La consistencia de Markdown no equivale a validación técnica.

## 4. Corrección de la documentación derivada

- El plan Draft 003 es la guía operativa vigente y sustituye Draft 001/002.
- Draft 001 y Draft 002 quedan conservados como históricos/supersedidos.
- Se retiraron del maestro los §§131–132 añadidos erróneamente en la auditoría anterior; el maestro vuelve a terminar en §130.
- MRA-001 queda invalidada como diagnóstico de laguna histórica; se conserva solo como registro del error y su corrección.
- No se cambia el estado científico C10, C10-D1, TGCV Core, RMA, Evidence→Claim Matrix, STATUS o C09.
- No se autoriza implementación, simulación ni ejecución.

## 5. Secuencia de cierre que resulta

1. Crosswalk maestro ↔ Decision Log ↔ DGP ↔ estimandos ↔ Closure Matrix ↔ Test Register.
2. Cierre de intervención B, comparador primario D1/D2, versiones y vías colaterales.
3. Cierre de población, q_X*/q_L*, C_c/L_m, unidad, interferencia, soporte y F*/alternativas.
4. DGP completo: potenciales, distribución conjunta técnica, heterogeneidad y escenarios adversariales.
5. Medición A/O/V, snapshots, validez de constructo, error, ausencia y censura.
6. Dimensionamiento y preespecificación estadística.
7. Autoauditoría de no-regresión, no independiente.
8. Freeze/aprobación documental.
9. Implementación y ejecución solo mediante autorizaciones separadas.

**Dictamen:** la cobertura histórica es suficiente para continuar. El pendiente real no es recuperar §§130–183, sino consolidar la arquitectura vigente en el plan y reconciliar los artefactos derivados. No se ha ejecutado validación técnica, simulación ni experimento.
