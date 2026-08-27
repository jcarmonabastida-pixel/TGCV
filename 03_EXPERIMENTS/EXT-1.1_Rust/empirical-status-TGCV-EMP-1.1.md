# TGCV-EMP-1.1 — Reproducible empirical status

**Source:** ChatGPT Library artifact `TGCV_EMPIRICAL_STATUS_2026-08-26.md`  
**Status:** PRIMARY TEST PASS (computational falsification test; not universal validation)

## Key methodological correction

The historical executable MVE-1.0 rules could not be recovered from available artifacts, so historical identity is not claimed. A new explicit frozen operationalization, `TGCV-EMP-1.1`, was constructed from the stabilized architecture and sealed before confirmatory model fitting.

Because `R=F(S,C,L)`, the earlier conditional formulation involving fully observed `S` was incoherent as an incremental-information test. The valid claim is representation-level incremental utility: whether `R` adds predictive utility beyond conventional baseline representation `B`.

## Frozen architecture

- Ontological Core: `S`
- `T_acc = F(S,C,L)`
- phenomenon: `Delta T_acc`
- consequence: `Delta Reach -> Delta Trajectory`
- value: downstream `Trajectory -> Outcome -> Value`
- interaction: mechanism, not primitive

## Operationalization

- 6 potential components: A1, A2, B1, B2, C1, C2
- 3–5 initial components
- 6 transformation families
- 3 discrete resources
- 12 objectives
- horizon `H=6`
- stochastic objective-independent execution

## Pilot

20,000 episodes; five-fold out-of-sample evaluation; mean LogLoss improvement `Delta=0.08393`.

The pilot established the confirmatory threshold `delta=0.04`.

## Confirmatory

- train: 30,000 episodes
- locked test: 10,000 episodes
- algorithm: fixed HistGradientBoostingClassifier, identical in both arms
- primary metric: paired out-of-sample LogLoss improvement
- alpha: 0.05
- delta: 0.04
- paired Monte-Carlo sign-flip test: 200,000 permutations

### Result

- baseline LogLoss: `0.26679`
- TGCV LogLoss: `0.18737`
- Delta LogLoss: `+0.07942`
- baseline AUC: `0.93734`
- TGCV AUC: `0.97242`
- paired sign-flip p: `<0.000005`

Controls:

- count-only R: `Delta=+0.01809`
- permuted R: `Delta=-0.09496`
- alternative RandomForest: `Delta=+0.00430`

Primary and stronger convergent-support criteria pass.

## Structural intervention

5,000 matched pairs used degree-preserving rewiring while preserving components, resources, edge count, in-degree multiset, out-degree multiset and objective identity within each pair. Success rates: `0.2884` vs `0.2962`; paired mean difference `-0.0078`; sign-flip `p=0.0370`.

The result supports the possibility that relational structure can alter downstream outcomes under controlled conventional summaries. It does not imply that every structural modification improves outcomes.

## Interpretation

`TGCV-EMP-1.1 = PRIMARY TEST PASS`.

This is evidence for the frozen computational operationalization under the specified experiment, not universal validation. The next scientific task is independent external replication and/or empirical-domain replication without modifying the Core in response to these results.

## Reproducibility anchors

- confirmatory test dataset SHA-256: `731f4071d6658b9023290ca423bf948e49d928713c8c11300b26f38dda1c273`
- confirmatory episode file SHA-256: `d12d8c14efdc581113c2cab0eaeb975dee6bac26ac9250be2a11725da6b9be4d`
- protocol SHA-256: `55c8f5654a41fdbefbae217089448b6ffeceb646feaed70b7bc9693fee92172c`
