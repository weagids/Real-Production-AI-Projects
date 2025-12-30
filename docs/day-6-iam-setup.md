# Day 6 — IAM Lambda Execution Role

## Role Name
genai-lambda-orchestration-role

## Purpose
Provides Lambda functions with minimal permissions required to:
- Read enterprise documents from S3
- Write execution logs

## Attached Policies
- AWSLambdaBasicExecutionRole
- Custom inline policy: S3ReadEnterpriseDocs

## Security Principles
- Least privilege
- No write access to data stores
- No AI model access at this stage

## Notes
Permissions will be expanded incrementally as features are added.
