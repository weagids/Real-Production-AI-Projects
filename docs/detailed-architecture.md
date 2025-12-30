# Detailed AWS Architecture

## Architecture Overview
The system is implemented using AWS managed services to ensure scalability, security, and minimal operational overhead.

## Core Components

### 1. Client Layer
- Internal web UI or enterprise application
- Authenticates users via corporate identity provider (future enhancement)

### 2. API Layer
- Amazon API Gateway
- Handles authentication, throttling, and request validation

### 3. Orchestration Layer
- AWS Lambda functions
- Coordinates query processing, retrieval, and response generation

### 4. AI Layer
- Amazon Bedrock
  - Embedding model for vector generation
  - LLM (Claude / Titan) for response generation

### 5. Knowledge Layer
- Amazon S3 for raw documents
- Vector store (OpenSearch / Aurora / managed vector DB)

### 6. Observability Layer
- Amazon CloudWatch
- AWS CloudTrail

## Data Flow (Query Path)
1. User submits query
2. API Gateway validates and forwards request
3. Lambda generates query embedding
4. Vector store retrieves top-N relevant documents
5. Lambda injects context into LLM prompt
6. Bedrock generates grounded response
7. Response returned to user

## Data Flow (Ingestion Path)
1. Documents uploaded to S3
2. Lambda processes and chunks documents
3. Embeddings generated via Bedrock
4. Vectors stored in vector store
