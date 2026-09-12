# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Manual Comparator Freeze 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Decision stage:** `PRE-EXECUTION`
**Comparator status:** `FROZEN — NOT EXECUTED`
**Execution authorization:** `NONE`

## 1. Comparator purpose

Freeze one deterministic manual troubleshooting route against which the operational transformation `ExecuteEC2RescueRemediation` / `AWSSupport-ExecuteEC2ResCUE` can later be compared.

The comparator is a **manual diagnostic-and-target-repair route using the already established Systems Manager access path**, restricted to the observed RDP symptom. It is not an execution of `AWSSupport-ExecuteEC2Rescue` and must not be started until the remaining IT-G1 pre-execution gates are closed.

AWS guidance identifies checks for public reachability, security-group/RDP access, routing, Windows Firewall, RDP port, Remote Desktop enablement, and `TermService`; it also documents `AWSSupport-TroubleshootRDP` as the AWS automation for checking/modifying those RDP settings. citeturn0search0turn0search10

## 2. Fixed case and success criterion

Target: `i-0b0bf56b94733718c`

Region: `eu-south-2`

Observed symptom at frozen pre-decision state: operator TCP/3389 reachability failed and target `TermService` was stopped.

**Comparator success criterion:** after the prescribed manual route, the target is again reachable through RDP from the same operator observation point on TCP/3389, without executing `AWSSupport-ExecuteEC2Rescue`.

A successful service start alone is **not** sufficient for comparator success; end-to-end RDP reachability is the primary outcome criterion.

## 3. Ordered comparator procedure

### Step M1 — Reconfirm external symptom

From the same operator observation point, test TCP connectivity to the frozen target public address on TCP/3389.

Record timestamp and complete command output. Do not alter the target during this step.

### Step M2 — Reconfirm target-side RDP service state

Through the already established SSM management path, inspect:

- `TermService` status;
- `TermService` startup type;
- TCP listener state for port 3389.

Record timestamp and output before making changes.

### Step M3 — Repair the directly observed service condition

If `TermService` remains stopped and the evidence is consistent with the frozen symptom, manually:

1. set `TermService` startup type to `Automatic`;
2. start `TermService`;
3. verify the service reaches `Running`;
4. verify a listener exists on TCP/3389.

No unrelated Windows, EC2, IAM, network, volume, or firewall change is permitted in this comparator step.

### Step M4 — Re-test end-to-end RDP reachability

From the same operator observation point, repeat the TCP/3389 test against the same target address.

If TCP/3389 succeeds, perform the defined RDP connection test using the same endpoint and valid pre-existing credentials. Record the outcome.

### Step M5 — Controlled diagnostic extension if M4 fails

If TCP/3389 remains unreachable after M3, the comparator enters `FAIL/STOP` rather than branching into an unconstrained troubleshooting tree.

No firewall modification, NLA modification, RDP-port modification, security-group modification, subnet modification, reboot, stop/start, root-volume detach, AMI creation, or other repair is permitted under this frozen comparator unless a future comparator revision explicitly adds it.

This preserves comparability and prevents outcome-driven expansion of the manual route.

## 4. Stopping conditions

### Success

`TCP_3389_REACHABILITY = PASS` from the same operator observation point and the RDP connection test succeeds.

### Failure

Any of the following:

- `TermService` cannot be started;
- no TCP/3389 listener after successful service start;
- TCP/3389 remains unreachable;
- RDP connection fails after TCP reachability is restored;
- a permitted step requires an unfreezed branch or additional intervention.

### Stop without success

The comparator stops immediately when a non-permitted diagnostic branch would be required.

## 5. Effort boundary

Comparator start event:

`T_START = timestamp immediately before M1 execution.`

Comparator stop event:

`T_STOP = timestamp when success, failure, or controlled-stop condition is first established.`

Record separately:

- active operator effort;
- elapsed wall-clock time;
- automation/waiting time attributable to SSM command execution or connection establishment.

No retrospective deletion or addition of steps is permitted after outcome knowledge.

## 6. Equivalence boundary

The comparator and `AWSSupport-ExecuteEC2Rescue` are compared on the same case and primary service-level objective:

`RESTORE_RDP_CONNECTIVITY = TRUE`

The comparison does **not** assert that the two routes are operationally identical.

`AWSSupport-ExecuteEC2Rescue` is a broader EC2Rescue-based automation and may perform operations outside the comparator, including instance stop/restart and AMI-related operations. AWS explicitly notes that its execution requires stopping and restarting the instance and can change a non-Elastic public IP. citeturn0search0

Those additional transformations remain outside the comparator and must be recorded as method-specific effects in the later execution/result analysis.

## 7. Excluded branches

The following are excluded from Comparator 001:

- `AWSSupport-ExecuteEC2Rescue`;
- `AWSSupport-TroubleshootRDP` automation;
- disabling Windows Firewall;
- changing NLA;
- changing the RDP port;
- changing security-group rules;
- modifying routes, subnet or VPC configuration;
- changing IAM permissions;
- stopping/restarting the instance;
- detaching or modifying the root volume;
- creating an AMI;
- changing instance type;
- changing public IP configuration.

These exclusions are intentional: they prevent the comparator from becoming an unbounded alternative automation or from consuming outcome knowledge to seek a favorable comparison.

## 8. Governance status

`COMPARATOR_FROZEN = TRUE`

`COMPARATOR_EXECUTED = FALSE`

`EXECUTION_AUTHORIZATION = NONE`

`AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED = FALSE`

The comparator freeze closes only the comparator-design gate. It does not authorize either comparator execution or `AWSSupport-ExecuteEC2Rescue` execution.
