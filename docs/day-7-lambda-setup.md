# Day 7 — Lambda Orchestration Function

## Function Name
genai-query-orchestrator

## Runtime
Python 3.11

## IAM Role
genai-lambda-orchestration-role

## Purpose
Acts as the orchestration layer for processing user queries and coordinating RAG workflows.

## Current Behavior
- Accepts input events
- Returns static response
- Logs execution to CloudWatch

## Notes
AI inference and retrieval logic will be added incrementally.
