# C10-S — Corrigendum a Gate 130: semántica de G frente a g_A y θ_A

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Precedencia:** contrato integrado V_cont §1–§3; DEC-C10S-D2-ESTIMAND-SEPARATION-001; DEC-C10-103; Gates 86, 129 y 130.  
**Estado:** G_SEMANTICS_CLARIFIED / ITT_G_NOT_EQUAL_THETA_A / NO_CHANGE_TO_ESTIMAND_SELECTION / NO_EXECUTION.

## 1. Motivo

La formulación de Gate 130 sobre G podía leerse como si el benchmark integrado no asignara una intervención sintética sobre el vector focal. Eso sería demasiado categórico y no concuerda con el contrato integrado V_cont, que define explícitamente G como una asignación aleatorizada a una intervención sintética sobre el vector completo de cambio de accesibilidad.

## 2. Distinciones correctas

1. **G en el benchmark integrado V_cont:** mecanismo de asignación aleatorizada separado de Z, con niveles binarios y una intervención sintética focal sobre el vector completo de ΔT_acc*. Su mecanismo, probabilidades y vector realizado tienen identidades/provenance propios.
2. **ITT-G^{Z=0}:** contraste de asignación a G dentro de Z=0, bajo la población, soporte, outcome y régimen definidos por el contrato integrado. Es un efecto de asignación en ese benchmark.
3. **g_A0/g_A1 del estimando θ_A aceptado:** par de políticas/intervenciones conjuntas versionadas que deben satisfacer la definición de DEC-C10-103 y los contratos de q_X*, soporte por historia y r_common. No basta con que exista un indicador G binario ni con que el benchmark intervenga sobre las cuatro coordenadas.
4. **θ_A(q_X*, r_common; V_cont):** contraste focal estandarizado sobre la distribución objetivo de historias q_X* y el régimen no focal común r_common. No es el ITT-G del benchmark por mera identidad de nombre o vector.

Por tanto, no se afirma que G carezca de toda intervención focal: el benchmark G sí interviene sintéticamente sobre el vector. Lo que no está demostrado/materializado es que su par de niveles, población, soporte y régimen reproduzcan el par de políticas y la estandarización exigidos por θ_A.

## 3. Corrección interpretativa de Gate 130

Donde Gate 130 caracteriza G como «una asignación/primera etapa, no dos intervenciones directas focales», debe leerse:

> G es una asignación aleatorizada a niveles de intervención sintética sobre el vector focal en el benchmark integrado. Sin embargo, el contraste ITT-G^{Z=0} no equivale a θ_A(q_X*,r_common;V_cont) mientras no se acredite la correspondencia entre los niveles de G y el par g_A0/g_A1 aceptado, la población objetivo q_X*, la factibilidad/soporte por historia, el régimen no focal r_common y la medición válida del outcome. G tampoco representa la cadena de asignación material D2 B_g0^D2/B_g1^D2.

Se conserva la conclusión de Gate 129/130: `theta_a_truth=None` y el Analyzer actual no estima θ_A. No se modifica el estado del ITT-G ya definido ni se rebautiza como θ_A.

## 4. Alcance

Aclaración de consistencia documental, no nueva decisión científica, política, estimando o mecanismo. No crea parámetros, escenarios, IDs, fixtures ni tests. No modifica el contrato integrado, DEC, código, schemas, roster, main, RMA, Evidence→Claim Matrix o STATUS. No ejecuta pruebas, generación, simulación o estimación.

`scientific_execution=false`  
`execution_authorized=false`
