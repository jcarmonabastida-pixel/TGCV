# Independent oracle specification

The oracle independently canonicalizes U, equivalence, R1, R2 and the ex ante R3 manifest, then computes the complete five-way diff.

Classification precedence:
1. NON_COMPARABLE
2. pure U gain = EXPANSION
3. pure U loss = CONTRACTION
4. simultaneous U gain and U loss = OTHER_STRUCTURAL_CHANGE
5. U unchanged + all relations unchanged = PERSISTENCE
6. U unchanged + only one directed R3 deletion and one directed R3 addition = RECONFIGURATION_ONLY
7. otherwise OTHER_STRUCTURAL_CHANGE

R3 is a directed relation. Endpoint order is semantic and is never sorted within an edge.
