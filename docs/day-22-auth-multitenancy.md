# Day 22 — Authentication & Multi-Tenancy

## Purpose
Secure RAG service for multiple tenants/users

## Authentication
- IAM roles for internal users
- Optional API keys or JWT for external clients

## Tenant Isolation
- tenant_id stored in chunk metadata
- Queries filtered by tenant_id
- Unauthorized access rejected

## Benefits
- Enterprise-grade multi-tenant security
- Controlled data access
- Auditability and compliance
