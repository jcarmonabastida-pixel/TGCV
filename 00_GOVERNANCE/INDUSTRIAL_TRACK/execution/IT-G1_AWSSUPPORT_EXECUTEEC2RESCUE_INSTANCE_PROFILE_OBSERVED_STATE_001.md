# IT-G1 — AWSSupport-ExecuteEC2Rescue Instance Profile Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

**Purpose:** Record the observed IAM identity associated with the controlled EC2 instance profile, without modifying IAM resources or executing the SSM Automation.

## Observed state

- Instance profile name: `IT-G1-EC2Rescue-InstanceProfile`
- Instance profile ARN: `arn:aws:iam::502731779370:instance-profile/IT-G1-EC2Rescue-InstanceProfile`
- Role name: `IT-G1-EC2Rescue-InstanceRole`
- Role ARN: `arn:aws:iam::502731779370:role/IT-G1-EC2Rescue-InstanceRole`

## Acquisition command

```powershell
aws iam get-instance-profile --profile tgcv --instance-profile-name IT-G1-EC2Rescue-InstanceProfile --query "InstanceProfile.{InstanceProfileName:InstanceProfileName,Arn:Arn,RoleName:Roles[0].RoleName,RoleArn:Roles[0].Arn}" --output table --no-cli-pager
```

## Interpretation boundary

This observation establishes the profile-to-role association only. It does **not** establish that the role has the permissions required by the EC2Rescue automation, nor that the automation's `AutomationAssumeRole`, helper instance profile, or helper security group parameters are satisfied.

No IAM modification was performed.

**Execution status:** `NOT_EXECUTED`
