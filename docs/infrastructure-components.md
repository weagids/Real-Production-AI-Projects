# Infrastructure Components

## Amazon S3
Purpose:
- Store enterprise documents
- Versioned and encrypted

Key Configurations:
- SSE-KMS encryption
- Bucket policies restricting public access
- Lifecycle policies for cost control

## IAM
Purpose:
- Enforce least privilege

Roles:
- API execution role
- Lambda orchestration role
- Bedrock invocation role
- Ingestion pipeline role

## Vector Store
Options:
- Amazon OpenSearch (vector search)
- Aurora with pgvector (future)

Selection Criteria:
- Managed service
- Scalability
- Security integration

## API Gateway
Purpose:
- Controlled public/private entry point
- Rate limiting
- Authentication hooks
