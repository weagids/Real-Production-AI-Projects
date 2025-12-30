# Infrastructure Overview

This directory contains infrastructure-as-code (IaC) definitions for the Enterprise GenAI Knowledge Assistant.

## IaC Principles
- Declarative infrastructure
- Environment separation (dev / prod)
- Least-privilege IAM
- Modular design

## Core Infrastructure Components
- Amazon S3 (document storage)
- IAM roles and policies
- Vector store (OpenSearch / managed vector DB)
- AWS Lambda execution roles
- API Gateway

## Deployment Strategy
- Infrastructure deployed via IaC
- Stateless services
- Rollback via versioned state
