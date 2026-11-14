# C10-S — Reconciliación histórica y fichas controladas de F1/F2/A1/A2

**ID:** C10-S-TRANS-CARDS-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** auditoría documental y fichas abstractas candidatas; no aprobadas, no congeladas y no ejecutables.  
**Dependencias:** maestro §§47–51, 57–69, 74–76; inventario finito §74; matriz de predicados §76; contratos ACC/EVID y DGP temporal.  
**Restricción:** no se inventa un dominio sustantivo, tecnología, producto, umbral, recurso o mecanismo no contenido en las fuentes canónicas.

## 1. Hallazgo de reconstrucción histórica

La solicitud de elaborar fichas sustantivas para F1, F2, A1 y A2 no parte de cero. El historial canónico ya define:

- §§47–49: ficha de condiciones constitutivas, protocolo de accesibilidad basal, distinción dependencia/accesibilidad/substituibilidad y niveles E1–E4.
- §57: F* como capacidad/función observable independiente de Outcome y Value; exige entrada, salida, restricciones, tolerancias, H, G, C0 y evidencia.
- §§58–59: A_f*, C_dep, App_f y ΔT_acc separados; condiciones de accesibilidad, aplicabilidad, provisión y ejecución clasificadas por su rol.
- §60: accesibilidad como propiedad relacional sistema-en-relación-con-unidad; separación auxiliar T_cap/T_acc.
- §§61–64: unidad/frontera, intervención B, predicado A_f* y clasificación temporal-causal de condiciones.
- §§67–69: C_dep como conjunción de instalación, integridad, compatibilidad y operación; s=.80 solo parámetro condicional candidato y distribución conjunta no identificada por s.
- §74: F1=τ2 focal S0→S2; F2 S2→SF; A1 S0→S1; A2 S1→SF; las cuatro son aliases locales, no TID canónicas.

Por tanto, no se deben recrear fichas genéricas de elegibilidad, F*, accesibilidad o evidencia. Este documento reutiliza esas especificaciones y localiza el hueco real: **el significado transformacional sustantivo de F2, A1 y A2 no está definido; tampoco se ha concretado la función técnica de τ2 más allá de la clase general “provisión/reconfiguración técnica focal”.**

## 2. Regla semántica para las fichas

Una ficha distingue:
1. identidad/versión transformacional (TID/SID/RID);
2. función propia de la transformación (qué cambio técnico produce);
3. estado de entrada y salida y criterio verificable de transición;
4. precondiciones de aplicabilidad desde la entrada;
5. predicados de accesibilidad (ID, REL, COND, AUTH, RES, DEP, ¬BLOCK);
6. relación composicional anterior/posterior;
7. recursos, autorizaciones, duración/ventana y restricciones;
8. evidencia y cobertura para truth y observación;
9. equivalencia/substituibilidad funcional respecto de F*, si corresponde;
10. cambios de versión, reversibilidad, fallos y límites.

No se asignan valores 1/0/? a ninguna unidad ni escenario en esta etapa. La ficha define qué significaría cada predicado; el DGP posterior definirá sus valores generadores y el analizador recibirá solo observaciones permitidas.

## 3. Ficha F1 — transformación focal τ2

| Campo | Reconciliación |
|---|---|
| Alias local | F1 |
| Identidad | τ2 focal; TID/SID/RID aún no canonizadas |
| Transición abstracta | S0→S2 |
| Función documentada | Transformación/reconfiguración técnica focal habilitada por provisión de dependencia técnica; la política B despliega/configura la dependencia y habilita interfaz, pero no ejecuta τ2 |
| Entrada | S0, instancia basal elegible; detalle de configuración y dominio no concretado |
| Salida | S2, estado intermedio focal; propiedades técnicas verificables no concretadas |
| Accesibilidad | A_f*(τ2) bajo §63.2: ID, REL, COND, AUTH, RES, DEP y ausencia de BLOCK; C_dep es necesario para la ruta técnica propuesta, pero no suficiente por sí solo |
| Aplicabilidad | App*(τ2,S0), separada de accesibilidad; precondiciones concretas de S0 siguen pendientes |
| Composición | Debe habilitar F2 mediante REL(F1,F2); contrato formal de interfaz/estado intermedio pendiente |
| Recursos/tiempo | C_auth basal y recursos/capacidad constantes son supuestos candidatos del fixture aislado; cantidades, demanda, reserva, duración y ventanas abiertas |
| Evidencia | Reutilizar §§48–49 y E1–E4; protocolo técnico y fuentes aún no fijados |
| Límite | No afirmar que instalación de dependencia equivale a ejecución, aplicabilidad o éxito de F1 |

**Conclusión F1:** ficha parcialmente definida por los contratos de τ2 y B. No es todavía una especificación transformacional ejecutable ni una TID congelada.

## 4. Ficha F2 — continuación focal

| Campo | Reconciliación |
|---|---|
| Alias local | F2 |
| Identidad | TID-F2 es alias local; no hay identidad/versionado canónicos |
| Transición abstracta | S2→SF |
| Función propia | OPEN: el inventario solo la denomina “continuación posterior” |
| Entrada | S2, salida hipotética de F1 |
| Salida | SF, estado objetivo formal |
| Aplicabilidad | App*(F2,S2) requerida; precondiciones concretas no definidas |
| Accesibilidad | ACC(F2,t3) debe evaluarse independientemente de ACC(F1,t3) |
| Composición | REL(F1,F2) permitida en topología; semántica de interfaz/contrato no especificada |
| Recursos/tiempo | No hay demanda, autorización, dependencia, bloqueo, duración o ventana específicos definidos |
| Evidencia | No existe estándar sustantivo específico para F2; no transferir automáticamente evidencia E3/E4 de F1 |
| Límite | La apertura de τ2/F1 no implica F2 accesible, aplicable ni Reach(SF)=1 |

**Conclusión F2:** solo está definida su posición topológica. No se puede rellenar su función, precondiciones o recursos sin una decisión explícita de modelado.

## 5. Ficha A1 — alternativa inicial

| Campo | Reconciliación |
|---|---|
| Alias local | A1 |
| Identidad | TID-A1 es alias local; no hay identidad/versionado canónicos |
| Transición abstracta | S0→S1 |
| Función propia | OPEN: transformación alternativa inicial |
| Entrada | S0 |
| Salida | S1 |
| Aplicabilidad | App*(A1,S0) requerida; precondiciones no definidas |
| Accesibilidad | ACC(A1,t0/t3) debe evaluarse con los mismos criterios generales, adaptados a su mecanismo |
| Composición | REL(A1,A2) permitida; semántica de interfaz pendiente |
| Recursos/tiempo | No especificados; no asumir que comparte dependencias, permisos o recursos con τ2 |
| Evidencia | Ficha y evidencia específicas no definidas |
| Substituibilidad | No presumir que A1 aislada cumple F*; se evalúa la ruta completa A1→A2 mediante Sub(π,F*,G,H,C0) |
| Límite | No identificar alternativa con equivalencia funcional por el mero hecho de llegar al estado nominal SF |

**Conclusión A1:** solo existe como primer paso de una ruta alternativa candidata. Su mecanismo y condiciones están abiertos.

## 6. Ficha A2 — cierre de ruta alternativa

| Campo | Reconciliación |
|---|---|
| Alias local | A2 |
| Identidad | TID-A2 es alias local; no hay identidad/versionado canónicos |
| Transición abstracta | S1→SF |
| Función propia | OPEN: cierre de la ruta alternativa |
| Entrada | S1, salida hipotética de A1 |
| Salida | SF, estado objetivo formal |
| Aplicabilidad | App*(A2,S1) requerida; precondiciones no definidas |
| Accesibilidad | ACC(A2,t0/t3) debe evaluarse independientemente de ACC(A1) |
| Composición | REL(A1,A2) permitida; semántica de interfaz pendiente |
| Recursos/tiempo | No especificados; factibilidad conjunta de ruta no identificada |
| Evidencia | Ficha y evidencia específicas no definidas |
| Substituibilidad | La ruta A1→A2 solo es alternativa funcional si satisface F* y sus restricciones; el destino formal SF no basta |
| Límite | No declarar ruta funcionalmente substituible solo por topología abstracta |

**Conclusión A2:** solo existe como segundo paso topológico. No hay semántica funcional que permita adjudicar su contribución a F*.

## 7. Reconciliación de los escenarios R0–R3

| Escenario | Qué puede afirmarse | Qué no puede afirmarse todavía |
|---|---|---|
| R0 / S4R-A | Se postula ausencia de ruta alternativa; su verdad exige cobertura exhaustiva | Ausencia funcional real, exclusividad de τ2 o pertenencia confirmada a P*_F |
| R1 / S4R-B | Se postula ruta alternativa basal estable | Que A1→A2 cumpla F* hasta definir y evaluar la función |
| R2 / S4R-C | B puede afectar A1/A2; existe riesgo de vía colateral | Magnitud/dirección del efecto o exclusión IV |
| R3 / S4R-D | Fallo de provisión puede impedir apertura focal | Estado de F2 o alternativa sin definición y evaluación propias |

El fixture actual utiliza SF como objetivo formal. Hasta que SF se vincule a un criterio operacional F* no circular, las rutas no pueden llamarse funcionalmente equivalentes ni substituibles.

## 8. Hueco de especificación y regla para cerrarlo

El hueco no se resuelve añadiendo más predicados abstractos. Requiere un **microdominio sintético explícito** o una **descripción técnica neutral pero concreta** que permita definir las transformaciones. Cualquier elección debe ser ex ante, independiente de Outcome/Value y suficientemente rica para que:
- F1 sea la transformación focal cuya provisión B puede habilitar;
- F2 sea una continuación funcional distinta, con precondiciones propias;
- A1/A2 formen una ruta alternativa genuina, no una duplicación nominal de F1/F2;
- ambas rutas puedan compararse respecto de una F* común;
- haya condiciones de accesibilidad, aplicabilidad, recursos y evidencia verificables;
- R0–R3 puedan instanciarse sin manipular el resultado.

**Prohibición de relleno:** no asignar semánticas como “instalar módulo”, “migrar datos”, “validar identidad” u otras operaciones concretas a F2/A1/A2 sin que el usuario o una decisión documentada de diseño las haya elegido. No derivar F* de SF por tautología.

## 9. Próxima operación de diseño

Antes de especificar valores del DGP, preparar una propuesta de microdominio sintético neutral con:
1. objetivo funcional F* independiente de Outcome/Value;
2. mecanismo focal τ2 y continuación F2;
3. mecanismo alternativo A1→A2;
4. precondiciones distintas pero comparables;
5. recursos, permisos, ventanas y fallos observables;
6. evidencia E1–E4 y cobertura de alternativas.

La propuesta deberá compararse con los contratos ya definidos (§§47–69) y someterse a decisión explícita. Hasta entonces, las fichas F2/A1/A2 permanecen deliberadamente abstractas.

## 10. Dictamen

La reconstrucción evita duplicar las definiciones previas de F*, accesibilidad, C_dep, evidencia y clasificación temporal. Identifica que F1 está parcialmente especificada por el contrato τ2/B, mientras F2/A1/A2 solo tienen una función topológica en el fixture. La semántica sustantiva no está disponible en el historial recuperado y no debe inventarse.

**Estado de cierre:** fichas de reconciliación completadas como auditoría de huecos; fichas transformacionales sustantivas NO cerradas. AUD-004/005/007/010/011 y OPEN-C10-001/003/005/007 permanecen abiertos. No hay aprobación, freeze, implementación, fixtures ejecutables, generación de datos, simulación ni ejecución.

## 11. Precedencia posterior — instancia sintética abstracta autorizada por AB-03-SYN (2026-11-10)

Las conclusiones históricas §§4–10 siguen describiendo correctamente el estado documental previo: F2/A1/A2 no tenían identidad ni semántica sustantiva aprobadas, y no era admisible rellenarlas por inferencia. La aceptación expresa de AB-03-SYN autoriza ahora una **definición abstracta limitada al DGP sintético**, no una elección de mecanismo físico ni una afirmación sobre sistemas reales.

La definición se encuentra en §12 de `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md` y fija:
- F1: conversión focal S0→S2;
- F2: aplicación y verificación focal S2→SF;
- A1: exportación alternativa basal S0→S1;
- A2: importación/aplicación y verificación alternativa S1→SF.

Se asignan TID/SID sintéticos del namespace del DGP, no RID ni EID. La asignación no crea implementación, no identifica producto/formato/plataforma, no fija mappings físicos, tolerancias, recursos, autorizaciones ni tiempos, y no prueba que A1→A2 sea funcionalmente substituible o independiente de B.

Por tanto, el antiguo estado OPEN sobre la **semántica abstracta** queda resuelto por la decisión posterior; permanecen OPEN la especificación técnica, la evidencia, el universo de alternativas, la validación del oráculo y la adjudicación material. La precedencia no modifica DEC-C10-051 ni convierte la propuesta en Design Freeze.
