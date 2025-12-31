# Day 10 — RAG Pipeline Overview

## Purpose
Enable Retrieval-Augmented Generation (RAG) by ingesting enterprise documents and converting them to embeddings for semantic search.

## Pipeline Steps
1. Read files from S3 `raw-documents/`
2. Convert documents to plain text
3. Chunk text into 500–1000 token segments
4. Generate embeddings using Amazon Bedrock
5. Store vectors and metadata in OpenSearch / Aurora pgvector

## Considerations
- Chunk size tuned for LLM context window
- Metadata supports traceability and retrieval
- Pipeline modular for testing and future scaling
