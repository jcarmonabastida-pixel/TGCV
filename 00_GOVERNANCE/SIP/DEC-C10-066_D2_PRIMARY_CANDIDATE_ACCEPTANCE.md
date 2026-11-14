# DEC-C10-066 — D2 como escenario primario candidato de C10-S

**Fecha:** 2026-11-06  
**Estado:** ACEPTADA — alcance limitado  
**Ámbito:** C10-S / comparación mecanística de provisión técnica  
**Rama de registro:** `research/c10-s-consolidation-draft`

## Decisión

Se acepta **D2 como escenario primario candidato** de C10-S para el contraste mecanístico de provisión técnica focal frente a ausencia de intento focal en el control.

**D1 se conserva como escenario secundario**, destinado al contraste incremental frente a provisión ordinaria de baja frecuencia. Su legitimidad como comparador no queda descartada en términos generales; simplemente no será el escenario primario candidato mientras no se justifique empíricamente/documentalmente que la provisión ordinaria propuesta representa el régimen de referencia pertinente.

## Semántica comparativa preservada

- D2: intento focal en control (q_0=0), intento focal en tratamiento (q_1=1).
- D1: intento focal en control (q_0=0.25), intento focal en tratamiento (q_1=1).
- El éxito técnico condicional candidato (s=0.80) permanece como parámetro de diseño no validado.
- Los estados finales candidatos de (C_{dep}) se derivan de las probabilidades de intento y del éxito condicional; no son parámetros marginales independientes.
- Intento, instalación/éxito, verificación técnica, (C_{dep}^{*}), (A_f^{*}), (D_f^{*}) y accesibilidad completa siguen siendo variables/constructos separados.

## Interpretación causal

1. ITT, primeras etapas y LATE/Wald de D2 pertenecen al comparador D2.
2. ITT, primeras etapas y LATE/Wald de D1 pertenecen al comparador D1.
3. No se agrupan ni se transportan automáticamente entre escenarios; sus poblaciones de cumplidores pueden diferir.
4. La selección de D2 no convierte (B_0/B_1) en equivalentes automáticos de (g_0/g_1).
5. La aleatorización puede identificar el efecto de asignación de la política material, pero no demuestra por sí sola exclusión, mediación ni atribución causal a accesibilidad.
6. Si existen vías colaterales de B hacia Outcome o Value, el efecto se interpreta como efecto de política/paquete salvo identificación adicional.

## Límites expresos

Esta decisión **no**:

- aprueba ni valida (s=0.80), otros parámetros, distribuciones o escenarios del DGP;
- cierra la definición material completa de (B_{g0}/B_{g1}) ni la correspondencia con (g_0/g_1);
- selecciona o aprueba la jerarquía definitiva de estimandos;
- cierra (q_X^*), poblaciones, horizonte, regla de Value, soporte o supuestos de identificación;
- aprueba fórmulas completas de accesibilidad ni los contratos de medición;
- autoriza freeze, implementación, simulación, validación ejecutable o ejecución científica.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.

## Precedencia

Esta aceptación posterior resuelve la selección del escenario primario candidato que DEC-C10-026, DEC-C10-031 y la reconciliación causal mantenían abierta. Las recomendaciones históricas de D1 como principal condicionado permanecen como antecedentes trazables, pero quedan supersedidas para la selección primaria candidata de C10-S. No se elimina D1 ni se reescribe su historial.
