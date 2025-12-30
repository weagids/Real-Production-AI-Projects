# High-Level Architecture

## Architecture Summary
The system follows a decoupled, serverless-first architecture optimized for security and scalability.

## Core Flow
1. User submits query via API
2. Query is embedded using Bedrock embeddings model
3. Relevant documents retrieved from vector store
4. Context injected into Bedrock LLM
5. Response returned with grounding

## High-Level Components
- API Gateway for request handling
- Lambda for orchestration
- Bedrock for embeddings and generation
- Vector store for semantic search
- S3 for document storage
- CloudWatch for logging and audit

## Architecture Principles
- Least privilege access
- Stateless compute
- Managed services first
- Auditability by default
