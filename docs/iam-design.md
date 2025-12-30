# IAM Design

## IAM Principles
- Least privilege
- Role-based access
- No long-lived credentials

## Key IAM Roles

### api-gateway-role
Permissions:
- Invoke Lambda
- Write access logs

### lambda-orchestration-role
Permissions:
- Read from S3
- Query vector store
- Invoke Bedrock models
- Write CloudWatch logs

### ingestion-role
Permissions:
- Read/write S3
- Generate embeddings
- Store vectors

## Security Controls
- IAM policy boundaries
- Explicit deny rules for sensitive actions
