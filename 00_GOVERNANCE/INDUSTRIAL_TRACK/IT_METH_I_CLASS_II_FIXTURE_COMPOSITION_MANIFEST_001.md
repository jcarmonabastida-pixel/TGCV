# Class II Fixture Composition Manifest 001

**Status:** `COMPOSITION FROZEN — PRE-EXECUTION GATE REMAINS BLOCKED`

**Candidate:** `AWS-PatchAsgInstance`
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`
**Purpose:** freeze the public-source composition used for the bounded methodological experiment without asserting an observed industrial case.

## 1. Frozen public sources

### 1.1 Auto Scaling fixture source
- Repository: `aws-samples/ec2-auto-scaling-instance-refresh-sample`
- Frozen commit: `95fcf3dd19f837349098e1a710b1a6bdd9705ecc`
- File: `template.yaml`
- Git blob SHA: `530af9c38d8a2eb67842393dce98b282809bfb2a`
- Local SHA-256: `D10B323570774C9D4C07547A8035EB7D6B3D907E83CF0DDF95A8EDC73D02C339`

### 1.2 Patch-management source
- Repository: `aws-samples/aws-cloud-and-hybrid-operations-workshop`
- Frozen commit: `618d0ab6da6a3c282e87a098efaa2e62284a8c8f`
- File: `cfntemplates/ssm-workshop-resources-episode-04.yml`
- Local SHA-256: `FD1C09C1FD200BC14A8039F00BF15AB3E894DE5DBA15315A07C375FD2ECEF5E2`
- Documentary page: `episode-04-step-01-enable-patch.md`

### 1.3 Runbook source
- Runbook: `AWS-PatchAsgInstance`
- Local source file: `AWS-PatchAsgInstance_OFFICIAL_RUNBOOK.md`
- Local SHA-256: `EFC2F49FFA368EFF1BF768F71E74F7BC518C136EDE03ABAAB97D5B966DC3C4EB`

## 2. Source-defined properties

- ASG fixture defines an Auto Scaling group with desired capacity 2, min 0, max 4.
- ASG launch template uses Amazon Linux 2 via the public AWS SSM AMI parameter and grants `AmazonSSMManagedInstanceCore`.
- Patch-management source documents an Amazon Linux 2 baseline named `AmazonLinux2SecAndNonSecBaseline`.
- Documented patch group composition uses key `Patch Group` and value `App`.
- Documented baseline includes security and non-security updates and the `kernel*` approval exception.
- `AWS-PatchAsgInstance` requires `InstanceId` and accepts optional `AutomationAssumeRole` and `LambdaRoleArn`.
- Runbook defaults: `WaitForInstance=PT2M`; `WaitForReboot=PT5M`.
- `AutoPatchInstanceInASG` is an execution-control tag and is explicitly not a patch-compliance indicator.

## 3. Composition-defined properties

The following are explicit composition choices for the Class II fixture and are not claims that they occur together in a single AWS-provided fixture:

- combine the Auto Scaling structural fixture with the patch-management configuration;
- use Amazon Linux 2 as the common OS family;
- assign the documented `Patch Group=App` configuration to the target fixture instance(s);
- use `AWS-PatchAsgInstance` as the candidate transformation;
- define the comparator as an ordinary patching path under the same frozen pre-decision state and evidence boundary.

These composition choices must remain distinguishable from source-defined facts.

## 4. Not yet closed

The following remain open and therefore block experimental execution:

- concrete ASG identity;
- concrete target instance identity;
- lifecycle/health/replacement configuration at decision time;
- effective AMI/image identity for the instantiated target;
- effective patch baseline assignment and pre-decision compliance state;
- exact runbook version available in the execution environment;
- complete frozen runbook parameter vector;
- operational comparator implementation;
- accessibility predicates and independently observable decision-time variables;
- temporal cutoff;
- ex-ante discriminative metric;
- two independent reconstruction paths;
- effort convention, if effort is to be measured;
- complete evidence package for the instantiated fixture.

## 5. Execution boundary

This manifest does **not** authorize AWS deployment or invocation of `AWS-PatchAsgInstance`.

No IT-G1, IT-G5, industrial utility score, industrial performance claim, financial/value realization claim, or TGCV Core modification follows from this manifest.

## 6. Gate state

`PRE_EXECUTION_GATE = BLOCKED`

Reason: public-source composition is now byte-identified and structurally documented, but the common pre-decision fixture state and experimental comparator/measurement package are not yet frozen.

## 7. Integrity rule

The frozen source identifiers above must not be silently replaced. Any material change to source commit, source file, composition rule, comparator, metric, or mandatory input requires an amended manifest/governance decision before execution.
