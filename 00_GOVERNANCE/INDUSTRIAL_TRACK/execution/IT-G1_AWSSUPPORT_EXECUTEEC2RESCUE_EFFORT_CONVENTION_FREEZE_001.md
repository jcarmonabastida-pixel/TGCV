# IT-G1 — AWSSupport-ExecuteEC2Rescue
## Effort Convention Freeze 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Stage:** `PRE-EXECUTION`
**Status:** `FROZEN`
**Execution authorization:** `NONE`

## 1. Purpose

Freeze the effort measurement convention before either the manual comparator or `AWSSupport-ExecuteEC2Rescue` is executed. The convention is outcome-blind and cannot be changed retrospectively after an execution result is known.

## 2. Common measurement unit

The primary effort unit is **operator active effort in seconds**, measured from the defined start event to the defined stop event while excluding passive waiting/automation time.

Secondary measures are retained:

- elapsed wall-clock duration;
- automation/waiting duration;
- number of operator intervention events.

All timestamps shall be recorded with timezone/offset and sufficient precision to reconstruct the interval.

## 3. Manual comparator

### Start event

`T_START_MANUAL` = timestamp immediately before the operator executes comparator step M1.

### Stop event

`T_STOP_MANUAL` = timestamp at which the first frozen success, failure, or controlled-stop condition is established.

### Active operator effort

Count only periods during which the operator is actively performing or deciding a prescribed comparator action, including command preparation, execution, inspection, interpretation required by the frozen procedure, and recording the prescribed observation.

Exclude passive SSM command execution time, network wait, RDP connection establishment wait, and other unattended waiting intervals.

### Wall-clock effort

`W_MANUAL = T_STOP_MANUAL - T_START_MANUAL`

### Automation/waiting

Record the aggregate duration of SSM command execution/waiting and other explicitly identified passive intervals.

## 4. AWSSupport-ExecuteEC2Rescue

### Start event

`T_START_RESCUE` = timestamp immediately before the operator initiates the frozen `AWSSupport-ExecuteEC2Rescue` automation invocation, after all authorization gates have passed.

### Stop event

`T_STOP_RESCUE` = timestamp at which the frozen rescue execution reaches its predefined terminal success, failure, or controlled-stop condition.

### Active operator effort

Count only operator-active periods required to initiate, monitor where active intervention is required, inspect prescribed outputs, and record the terminal result.

Exclude unattended Automation/SSM/AWS service execution time.

### Wall-clock effort

`W_RESCUE = T_STOP_RESCUE - T_START_RESCUE`

### Automation/waiting

Record the aggregate time consumed by AWS Systems Manager Automation, nested workflow actions, instance operations, waits, and other unattended execution.

## 5. Comparability rule

The two methods shall report the same three categories:

| Measure | Manual comparator | EC2Rescue |
|---|---|---|
| Active operator effort | required | required |
| Wall-clock duration | required | required |
| Automation/waiting | required | required |

The primary efficiency comparison is based on **active operator effort**, not wall-clock duration alone.

Wall-clock duration is retained because an automation can reduce operator effort while increasing total elapsed time.

## 6. Outcome-blind rule

The effort convention is frozen before execution. No step may be added, removed, merged, reclassified, or re-timed because of the observed outcome.

If an execution encounters an unplanned condition outside the frozen procedure, the run stops or enters the separately governed deviation protocol; the convention itself is not rewritten.

## 7. Recording requirements

For each execution record:

- method identifier;
- `T_START`;
- `T_STOP`;
- wall-clock duration;
- active operator effort;
- automation/waiting duration;
- operator intervention count;
- terminal condition;
- any governed deviation identifier.

Durations must satisfy, subject to timestamp measurement precision:

`WALL_CLOCK >= ACTIVE_OPERATOR_EFFORT`

and

`WALL_CLOCK >= AUTOMATION_WAITING`

The two secondary categories are not required to sum exactly to wall-clock duration where there are overlapping or unclassified intervals; any such interval must be explicitly recorded rather than silently assigned.

## 8. Governance state

`EFFORT_CONVENTION_FROZEN = TRUE`

`COMPARATOR_EXECUTED = FALSE`

`AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTED = FALSE`

`EXECUTION_AUTHORIZATION = NONE`

This artifact freezes measurement only. It authorizes neither method.

## 9. Next governed gate

The next admissible operation is the independent reconstruction/control package, followed by the final integrity/provenance closure. Execution remains prohibited until all mandatory pre-execution gates are closed.
