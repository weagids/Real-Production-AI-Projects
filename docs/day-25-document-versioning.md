# Day 25 — Document & Embedding Versioning

## Purpose
Support evolving knowledge without breaking auditability.

## Versioning Strategy
- Explicit document versions (v1, v2, v3)
- No overwriting embeddings

## Metadata
- document name
- version
- tenant_id
- active flag
- upload timestamp

## Query Control
- Only active versions queried
- Instant rollback supported

## Benefits
- Audit compliance
- Safe document updates
- Production-grade RAG lifecycle
