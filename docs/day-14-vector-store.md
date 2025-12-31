# Day 14 — Vector Store with Amazon OpenSearch

## Purpose
Persist embeddings and metadata to enable semantic retrieval.

## Index Configuration
- Engine: Amazon OpenSearch
- Vector type: k-NN
- Embedding dimension: 1536 (Titan)

## Stored Fields
- Vector embedding
- Chunk text
- Metadata (source, offsets)

## Benefits
- Scalable semantic search
- Traceable retrieval results
- AWS-native security and operations
