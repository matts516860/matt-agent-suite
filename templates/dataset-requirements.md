# Dataset Requirements Template

Use this when asking the Dataset Engineer Agent to build a new dataset.

## Required Fields

- Business keys (e.g., SubmissionID, PolicyID, ClaimID)
- Dates for key events (SubmissionDate, QuoteDate, BindDate, LossDate)
- Dimensions:
  - LineOfBusiness
  - Segment / Market
  - Geography (State/Region)
  - Broker / Distributor
- Metrics:
  - Premium
  - Loss amounts
  - Scores (quality, CSAT, etc.)

## Volume and Time Range

- Row count:
  - Minimum: 10,000
  - Typical: 25,000–100,000
- Time range:
  - At least 24 months of history
  - Optionally, mark last 3–6 months with notable changes

## Trends and Story Hooks

- At least one segment with **worsening KPIs**.
- At least one segment with **improving KPIs**.
- One or two **clear anomalies** (e.g., sudden spike in severity in a region).
- Behavior that lends itself to questions like:
  - “Where are things getting worse?”
  - “Which brokers are improving fastest?”
  - “What’s driving the increase in Time to Bind?”

## Data Quality

- Minimal nulls in key fields unless intentionally modeling poor data quality.
- Avoid contradictory states (e.g., `BindDate` without `QuotedPremium` unless part of the story).
- Make filtering and slicing intuitive (categorical fields should have a small, meaningful set of values).
