# Gate 151 — aceptación R151-A y precisión R151-A8

**Estado:** ACEPTADA para la semántica lógica del DGP sintético  
**Ámbito:** C10-S / EventHistory  
**Rama:** research/c10-s-consolidation-draft  
**PR:** #116 (Draft)

## 1. Aceptación expresa

Se registra la aceptación del usuario de R151-A, incorporando la precisión R151-A8:

1. PROFILE exposure permanece como obligación contractual de B1.
2. El DGP sintético vigente no introduce una transición independiente de pérdida de PROFILE exposure.
3. Cualquier ampliación futura de esa dinámica requiere una decisión explícita y una modificación aprobada del DGP.
4. PROFILE exposure no constituye actualmente una dimensión temporal independiente adjudicable.
5. Su cumplimiento continuo no se dará por demostrado mediante EventHistory ni se inferirá de la continuidad de admisión.

## 2. Reconciliación con R150-A

La aceptación no elimina ni debilita la obligación contractual de exponer el PROFILE declarado en ambos estados de ENABLED. Distingue esa obligación de las variables temporales efectivamente generadas y representadas en el DGP actual.

Por tanto:
- ENABLED conserva su dimensión declarativa temporal.
- La admisión efectiva conserva su dimensión funcional temporal.
- PROFILE permanece como configuración declarada/versionada y obligación contractual.
- No se presume una dinámica runtime independiente de PROFILE exposure.

## 3. Consecuencias para EventHistory y A_B1

EventHistory no generará transiciones de PROFILE exposure en el DGP vigente. El adjudicador no podrá afirmar que dicha exposición se mantuvo continuamente basándose únicamente en EventHistory, ni usar la continuidad de admisión como sustituto probatorio de esa obligación.

Esta delimitación no altera por sí misma DEC-C10-102, no selecciona reloj ni soporte temporal y no resuelve §51.

## 4. Límites y estado operativo

Aceptación exclusivamente semántica y lógica para el DGP sintético. No autoriza:
- cambios de código o schema;
- pruebas o ejecución científica;
- modificación de DEC existentes;
- promoción a `main`;
- cierre de §51 ni fijación de parámetros temporales.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`

## 5. Próxima operación

Gate 152: reconciliar A_B1, EventHistory y el operador temporal de DEC-C10-102, distinguiendo componentes temporalmente variables de obligaciones contractuales invariantes, sin reinterpretar DEC-C10-102 ni introducir decisiones no aceptadas.
