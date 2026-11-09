# C10-S — Registro de cierre XSYNC-138-01…10
**Trazabilidad y resolución por hallazgo — borrador 001**

**Estado:** DRAFT / AUDITORÍA DE CIERRE — NINGÚN HALLAZGO FORMALMENTE CERRADO  
**Fuente primaria recuperada:** C10-S consolidated draft 004, §§25.1–25.4, 26.6–26.10, 27.6–27.8 y 28.8–28.9.  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116.

---

## 1. Corrección de la recuperación histórica

El texto íntegro de XSYNC-138-01…10 sí está contenido en el documento consolidado C10-S, especialmente en §25.2. Además, §27.8 y §28.9 registran el estado de varias correcciones. Por tanto, la afirmación previa de que no se había recuperado el texto íntegro XSYNC era demasiado amplia: se corrige aquí.

Lo que no se ha recuperado es un acta independiente de cierre/aprobación ni una auditoría externa de las correcciones. La fuente de los hallazgos sí está recuperada; su resolución formal sigue pendiente.

## 2. Matriz de trazabilidad

| ID | Severidad fuente | Hallazgo original (síntesis fiel) | Respuesta ya contenida en C10-S | Pendiente para cierre | Estado de control |
|---|---|---|---|---|---|
| XSYNC-138-01 | P0 | Hallazgo histórico: el diseño previo confundía la intervención focal sobre autorización con políticas factibles de accesibilidad. | DEC-C10-066/067 resuelven para D2 la política primaria: provisión técnica focal con `C_auth,base=1` común e invariante. La intervención focal sobre autorización queda como escenario alternativo; `B_g^D2` no es automáticamente `g^Af`. | Completar mapping B→g^Af, factibilidad/soporte, exclusión y vías directas/colaterales; verificar consistencia con C10-D1; revisión independiente y aprobación formal. | PARCIALMENTE RESUELTO PARA D2; RESIDUAL OPEN / CIERRE FORMAL PENDIENTE |
| XSYNC-138-02 | P1 | q_X incorpora indebidamente la regla de Value | §26.8 separa q de la regla evaluativa; reconciliación nueva también mantiene Value fuera de q | Actualizar todos los usos de q_X/q_L y el contrato de Value; fijar beneficiario, criterio, escala y horizonte | CORRECCIÓN PROPUESTA; CIERRE PENDIENTE |
| XSYNC-138-03 | P1 | A_f* se aproxima indebidamente a ΔT_acc completo | §§26–27 y diccionario §43 distinguen indicador focal y cambio estructurado; h_f(ΔT_acc) es proyección focal | Auditar cada ecuación, tabla, variable y prueba para asegurar que A_f* nunca sustituye ΔT_acc | CORRECCIÓN PARCIAL; AUD-001 ABIERTO |
| XSYNC-138-04 | P1 | q*(L=1|X)=.5 y g1=.8/g0=.2 asumen factibilidad sin separar L_c/L_m ni probar soporte | §26.7 exige separar L_c/L_m, factibilidad por historia y soporte; la reconciliación nueva propone escenarios limpio/contaminación | Definir distribución q*, historia, conjunto factible por estrato, positividad y tratamiento de estratos sin soporte | CORRECCIÓN PROPUESTA; XAUD-001 ABIERTO |
| XSYNC-138-05 | P1 | θ_A^dyn se trata potencialmente como estimando listo pese a estar sin formalizar | C10-D1 §24.3 y §25.8 lo mantienen como marcador pendiente; reconciliación lo excluye del conjunto estimable | Barrer todos los usos de θ_A^dyn; marcar como no disponible, sin ecuación/estimador/resultado aparente | DELIMITACIÓN DOCUMENTAL; VERIFICACIÓN GLOBAL PENDIENTE |
| XSYNC-138-06 | P1 | Igual ΔT_acc no implica equivalencia causal de políticas/versiones | §§17.6, 26, 28 distinguen equivalencia de accesibilidad, vías relevantes para Value y versión; VER-01…06 | Ejecutar revisión de casos de prueba y demostrar rechazo de agrupación por costes, demora, riesgo/calidad o vías directas | RESPUESTA DOCUMENTAL; PRUEBAS NO EJECUTADAS |
| XSYNC-138-07 | P1 | Estados de trayectoria/selección/ejecución incompletos; riesgo de sesgo postratamiento | §§28.5–28.8 amplían conocimiento, consideración, selección, inicio, parcial, interrupción, finalización; TRJ-01…07 | Mapear cada estado al diccionario canónico y verificar trazabilidad temporal y no ajuste mecánico | RESPUESTA DOCUMENTAL; COBERTURA NO PROBADA |
| XSYNC-138-08 | P1 | Se confunde dictamen metodológico de C10-S con conclusión científica C10-D1 | §20 y §21 contienen categorías separadas; matriz maestra y reconciliación distinguen gates metodológicos y conclusiones científicas | Alinear contrato de salida y agregación; probar que un PASS sintético no emite conclusión científica de C10 | ABIERTO; CORRECCIÓN EN CURSO |
| XSYNC-138-09 | P2 | Falta contrato completo de clasificación de relevancia/equivalencia según δ y ε | §§21–23 justifican δ/ε, dimensionamiento y umbrales; C10-D1 §21.3 aporta regla interpretativa | Formalizar salidas para relevante, equivalente, adverso e inconcluso con intervalos y precisión; prohibir “p no significativo = equivalencia” | ABIERTO; CONTRATO DE SALIDA INCOMPLETO |
| XSYNC-138-10 | P2 | Enumerador validado no cubre necesariamente conocimiento/consideración/inicio/interrupción/ejecución | §§28.5–28.9 amplían el alcance y TRJ-01…07; C10-S §49 registra rutas alternativas | Decidir alcance de C10-S, mapear pruebas a cada estado, identificar lo excluido y no reclamar cobertura no probada | RESPUESTA DOCUMENTAL PARCIAL; COBERTURA NO PROBADA |

## 3. Evidencia de recuperación y localización

| Fuente | Secciones | Qué acredita |
|---|---|---|
| C10-S §25.2 | XSYNC-138-01…10 | Texto de los diez hallazgos, severidad, consecuencia y disposición requerida |
| C10-S §25.3–25.4 | TE_Z, ψ_policy, θ_A(q), θ_{L,A}, θ_A^dyn; estado | Reglas de interpretación y declaración de que todos permanecen abiertos en ese corte |
| C10-S §26.6–26.10 | XSYNC-01, mapeo de intervención y reglas del analizador | Corrección propuesta de XSYNC-01 y estado no aceptado |
| C10-S §27.6–27.8 | S4-O/S4-R y estado de XSYNC | Correcciones propuestas de 02–08 y cuestiones restantes |
| C10-S §28.8–28.9 | VER/TRJ/INT y estado | Pruebas de versiones, trayectoria y cobertura; no ejecutadas |

## 4. Criterios de cierre transversales

No cerrar XSYNC por la existencia de una sección correctiva. Para cada ID se exige:

1. referencia exacta a la regla corregida;
2. búsqueda de formulaciones contradictorias en el conjunto activo C10-S; la auditoría actual cubre los 100 archivos de PR #116, pero no certifica aún todo el repositorio, ramas históricas ni fuentes fuera del PR;
3. consistencia con C10-D1, sin cambiar su estimando;
4. ecuación/variable/diccionario y contrato de prueba coherentes;
5. prueba adversarial que falle si reaparece el error;
6. resultado independiente de revisión;
7. resolución formal con responsable, fecha, commit y estado.

Los hallazgos P0/P1 bloquean freeze causal mientras permanezcan abiertos. Los P2 deben cerrarse o delimitarse explícitamente antes de declarar cobertura metodológica integral.

## 5. Dependencias y orden recomendado

1. XSYNC-01…04: reconciliación de intervención, q, Value, constructo focal, L_c/L_m y soporte.
2. XSYNC-05…07: estimando dinámico, versiones y estados longitudinales.
3. XSYNC-08…10: separación de dictámenes, regla δ/ε y cobertura del proceso de trayectorias.
4. Auditoría independiente de conjunto y cierre formal.

## 6. Dictamen

**Texto histórico XSYNC-138-01…10: RECUPERADO EN GITHUB.**  
**Correcciones:** XSYNC-138-01 PARCIALMENTE RESUELTO PARA D2; otros hallazgos mantienen los estados de la matriz. Correcciones documentales adicionales incorporadas en el barrido del PR #116.  
**Cierre formal: NO ALCANZADO.**  
**Pruebas: NO EJECUTADAS.**

No se modifica C10-D1, Core, RMA, Evidence→Claim Matrix, STATUS ni claims. No se ejecuta simulación ni experimento. La matriz es un instrumento de cierre, no una aceptación de los hallazgos.
