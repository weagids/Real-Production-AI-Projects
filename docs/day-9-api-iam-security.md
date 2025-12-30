# Day 9 — API Gateway IAM Authorization

## Route
/query

## Authorization
- IAM (AWS Signature v4)
- Only IAM principals with invoke permissions can access

## Purpose
- Prevent unauthorized API calls
- Maintain auditability and controlled access

## Notes
- Lambda continues to log all executions to CloudWatch
- Throttling settings remain
- IAM policies enforced at API Gateway level
