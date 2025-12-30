# Day 5 — S3 Document Store Setup

## Purpose
Amazon S3 is used as the secure source of truth for enterprise knowledge documents.

## Configuration
- Region: us-east-1
- Public access: blocked
- Versioning: enabled
- Encryption: SSE-KMS (AWS-managed key)

## Folder Structure
- raw-documents/
- processed-documents/

## Security Considerations
- No public access
- IAM-only access
- Encrypted at rest and in transit

## Notes
This bucket forms the foundation of the RAG ingestion pipeline.
