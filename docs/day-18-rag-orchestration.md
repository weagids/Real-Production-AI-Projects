# Day 18 — End-to-End RAG Orchestration

## Purpose
Orchestrate the complete Retrieval-Augmented Generation workflow.

## Flow
1. Receive user query
2. Generate query embedding
3. Perform vector search
4. Build grounded prompt
5. Generate LLM answer
6. Return API response

## Design Principles
- Modular architecture
- Centralized orchestration
- Robust error handling
- Production-ready logging
