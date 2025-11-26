# Insurance KPI Definitions

Use or adapt these KPI definitions in data dictionaries, semantic models, and demos.

## Time to Quote (Days)

> **Time to Quote = QuoteDate − SubmissionDate**

Represents the number of days from initial submission to the generation of a quote.  
Used to:
- Measure underwriting responsiveness.
- Compare brokers, segments, or products.

## Time to Bind (Days)

> **Time to Bind = BindDate − SubmissionDate**

Days from submission to policy binding.  
Useful for:
- Evaluating operational speed.
- Identifying bottlenecks in underwriting and negotiation.

## Loss Ratio

> **Loss Ratio = (PaidLoss + CaseReserve) / EarnedPremium**

Indicates profitability of a segment or portfolio.  
Can be calculated:
- At claim, policy, LOB, broker, or portfolio level.
- Over specific periods (e.g., trailing 12 months).

## Submission Quality Score

A composite score (e.g., 0–100) measuring:
- Completeness of submissions (missing fields, docs).
- Broker behavior (frequency of incomplete submissions).
- Fit to underwriting appetite.

Implementation details can vary; the Dataset Engineer Agent can define components.

## Broker Win Rate

> **Broker Win Rate = BoundPolicies / (QuotedPolicies)**

Measures how effectively a broker converts quotes into bound policies.

## Claim Frequency

> **Claim Frequency = ClaimCount / ExposureUnit**

Where “ExposureUnit” might be:
- Policy count
- Insured units (vehicles, locations, etc.)
- Earned premium (for some analyses)

## Claim Severity

> **Claim Severity = PaidLoss / ClaimCount**

Average cost per claim.  
Often analyzed jointly with frequency to understand whether issues are driven by more claims, more expensive claims, or both.
