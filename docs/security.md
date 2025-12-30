# Security & Governance

## Security Objectives
- Prevent data leakage
- Enforce least privilege access
- Ensure auditability
- Maintain data residency and compliance

## Identity & Access Management (IAM)
- All services use IAM roles (no static credentials)
- Principle of least privilege enforced
- Separate roles for:
  - API access
  - AI inference
  - Data ingestion
  - Logging and monitoring

## Data Protection
- Documents encrypted at rest using AWS KMS
- TLS encryption for data in transit
- No customer data used for model training (Bedrock guarantee)

## Network Security
- API Gateway as controlled entry point
- Private access to Bedrock via AWS-managed endpoints
- No public access to data stores

## Logging & Audit
- All API calls logged via CloudWatch
- Bedrock usage monitored
- IAM access tracked via CloudTrail

## Compliance Considerations
- Supports GDPR-style access controls
- Data isolation per environment (dev / prod)
- Clear data retention policies
