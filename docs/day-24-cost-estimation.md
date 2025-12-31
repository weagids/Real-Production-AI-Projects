# Day 24 — Cost Estimation & Controls per Tenant

## Purpose
Estimate and control per-tenant GenAI costs in production.

## Usage Tracking
- Tokens used per LLM call
- Chunks retrieved per query
- Logged per tenant

## Cost Formula
- Tenant Cost = (tokens_used / 1000) * Bedrock_rate + OpenSearch cost
- Real-time estimation

## Alerts & Throttling
- Thresholds per tenant
- CloudWatch alarms
- Optional throttling when exceeded

## Benefits
- Prevents runaway costs
- Enables SLA management
- Enterprise cost transparency
