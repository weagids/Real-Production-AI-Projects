# Day 8 — API Gateway Integration

## API Name
genai-orchestration-api

## Route
ANY /query → Lambda genai-query-orchestrator

## Security
- No public access yet
- Logs enabled (CloudWatch)
- Throttling: 50 req/sec, burst 100

## Purpose
Acts as the enterprise entry point for user queries.
Provides controlled, observable, and rate-limited access.

## Notes
- IAM auth will be added in subsequent days.
- Endpoint currently triggers minimal Lambda for validation.
