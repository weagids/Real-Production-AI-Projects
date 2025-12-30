# Failure Scenarios & Resilience

## Scenario 1: Bedrock Throttling
**Mitigation**
- Exponential backoff
- Request rate limiting at API Gateway

## Scenario 2: Vector Store Unavailable
**Mitigation**
- Graceful degradation
- Fallback to LLM-only responses with warnings

## Scenario 3: Inaccurate Retrieval
**Mitigation**
- Top-K tuning
- Confidence scoring
- Human review for sensitive outputs

## Scenario 4: Excessive Cost
**Mitigation**
- Token limits
- CloudWatch alarms
- Budget thresholds
