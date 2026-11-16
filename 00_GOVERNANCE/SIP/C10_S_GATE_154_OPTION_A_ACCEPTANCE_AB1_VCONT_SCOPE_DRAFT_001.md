# Gate 154 — aceptación de la opción A: alcance temporal acotado de A_B1 y V_cont

**Fecha:** 2026-11-16  
**Estado:** ACCEPTED_FOR_CURRENT_SYNTHETIC_DGP_LOGICAL_SCOPE  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)

## 1. Aceptación expresa

Se registra la aceptación expresa de la Opción A de Gate 153:

`A_B1` adjudica temporalmente el comportamiento de admisión/no-admisión exigido por ENABLED, incorporando la disponibilidad operativa y los mecanismos runtime cuando impidan efectivamente ese comportamiento.

PROFILE permanece como configuración declarada y obligación contractual de B1, pero PROFILE exposure queda fuera de la dimensión temporal adjudicada por V_cont en el DGP sintético vigente, al no disponer de trayectoria truth independiente.

## 2. Alcance de la afirmación

En el DGP vigente, V_cont puede interpretarse como continuidad temporal de la función efectiva de admisión B1, conforme al alcance delimitado aquí. No puede presentarse como:
- cumplimiento íntegro de todas las obligaciones contractuales de B1;
- demostración de continuidad de PROFILE exposure;
- medida general de Value contextual de TGCV.

La obligación contractual de exponer PROFILE no queda eliminada, satisfecha por inferencia ni convertida en UNKNOWN. Su adjudicación temporal permanece fuera del soporte actual.

## 3. Compatibilidad y preservación

Esta aceptación:
- preserva DEC-C10-099 y el operador estricto de DEC-C10-102;
- preserva las reglas temporales aceptadas de DEC-C10-100/101/104;
- preserva R150-A, R151-A8 y R152-A1…A6, delimitando expresamente su composición;
- no crea ni modifica DEC-C10-105 ni ninguna otra DEC;
- no modifica el DGP original ni §51;
- no selecciona reloj, soporte temporal, rejilla, T*, Δ ni K.

## 4. Límites operativos

Aceptación exclusivamente semántica y lógica para el DGP sintético actual. No autoriza schema, código, harness, pruebas, ejecución científica ni promoción a `main`.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`

## 5. Siguiente operación

Gate 155: traducir esta delimitación aceptada en el contrato lógico de composición A_B1 → EventHistory → IntervalAdjudication → V_cont, verificando que no se alteran las reglas de transición R144-A, identidad/completitud de historia ni la semántica {1,0,?}. La operación seguirá siendo documental y no cerrará §51.
