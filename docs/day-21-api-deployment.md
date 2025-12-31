# Day 21 — API Gateway & Deployment

## Purpose
Expose the RAG Lambda via secure, throttled, and monitored API endpoints.

## Configuration
- Endpoint: Regional
- Authorization: IAM
- Stages: dev, prod
- Throttling: 10 RPS / burst 20

## Deployment Automation
- Optional: CloudFormation/Terraform
- Reproducible and traceable

## Benefits
- Secure API access
- Cost control
- Production-ready GenAI service
