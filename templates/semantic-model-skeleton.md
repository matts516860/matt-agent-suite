# Semantic Model Skeleton Template

Use this as a starting point when the Demo Architect Agent defines a Tableau semantic model.

## Business Preferences

- Use business-friendly naming for fields (e.g., “Time to Bind (Days)” instead of `time_to_bind_days`).
- Hide raw technical IDs unless needed for joins.
- Group fields into logical folders:
  - Dates
  - Policy / Submission
  - Broker
  - Geography
  - Product / Line of Business
  - Metrics & KPIs

## Core Facts

- **FactSubmission**
  - SubmissionID
  - BrokerID
  - AccountID
  - SubmissionDate
  - LineOfBusiness
  - Segment (e.g., Mid-Market, Specialty)
- **FactQuote**
  - QuoteID
  - SubmissionID
  - QuoteDate
  - QuotedPremium
  - Status
- **FactBind**
  - PolicyID
  - SubmissionID
  - BindDate
  - BoundPremium
- **FactClaim**
  - ClaimID
  - PolicyID
  - LossDate
  - ReportDate
  - PaidLoss
  - CaseReserve
  - Status

## Dimensions

- **DimDate**
  - Calendar Date
  - Month, Quarter, Year
  - Fiscal attributes (if needed)
- **DimBroker**
  - BrokerID
  - BrokerName
  - ParentBroker
  - Region
- **DimProduct**
  - ProductID
  - LineOfBusiness
  - CoverageType
- **DimGeography**
  - State
  - Region
  - Territory

## Relationships (Conceptual)

- FactSubmission → FactQuote (SubmissionID)
- FactSubmission → FactBind (SubmissionID)
- FactBind → FactClaim (PolicyID)
- All facts → DimDate (on appropriate date role)
- All facts → DimBroker, DimProduct, DimGeography

## Key KPIs

- Time to Quote (days)
- Time to Bind (days)
- Hit Ratio (Bound / Quoted)
- Loss Ratio (Paid + Reserve / Premium)
- Submission Quality Score
- Broker Win Rate

This template should be adjusted by the Demo Architect Agent based on customer-specific needs.
