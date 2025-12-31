# Day 11 — S3 Document Reader

## Purpose
Provides a reusable component for securely reading enterprise documents from S3.

## Features
- Lists documents under `raw-documents/`
- Reads content using IAM role
- Logs access for auditability

## Design Principles
- Least privilege IAM
- Modular and testable
- Lambda-compatible
