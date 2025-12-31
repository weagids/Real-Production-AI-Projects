# Day 12 — Text Chunking & Metadata Design

## Purpose
Prepare documents for high-quality semantic retrieval in the RAG pipeline.

## Chunking Strategy
- Chunk size: ~800 tokens (word-based approximation)
- Overlap: ~100 tokens
- Reason: preserve context and improve recall

## Metadata Included
- Source document reference
- Word boundaries
- Unique chunk ID

## Design Benefits
- Improved retrieval accuracy
- Better grounding of LLM responses
- Traceable and auditable outputs
