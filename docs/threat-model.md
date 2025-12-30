# Threat Model

## Identified Risks
- Prompt injection attacks
- Unauthorized data access
- Over-permissive IAM roles
- Hallucinated responses

## Mitigations
- Input sanitization
- Grounding responses via RAG
- Strict IAM role separation
- Output filtering and validation

## Residual Risks
- Model-level hallucinations
- Misconfigured access controls
