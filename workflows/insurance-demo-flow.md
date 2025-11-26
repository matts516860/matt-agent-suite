# Insurance Demo Multi-Agent Workflow

This workflow shows how multiple agents collaborate to build an end-to-end insurance demo.

## 1. Input

- Discovery notes from customer (email, Slack, meeting transcript).
- Target personas: e.g., Producer, Underwriter, Claims Manager, Executive.
- High-level goals: e.g., Time to Bind reduction, Loss Ratio improvement, Broker performance.

## 2. Demo Architect Agent

- Parses discovery notes.
- Defines:
  - Personas and their journeys.
  - Required dashboards (Book of Business, Claims, Underwriting pipeline, Broker view).
  - Required KPIs: Time to Quote, Time to Bind, Submission Quality, Loss Ratio, etc.
  - Where GenAI (Pulse/Agentforce) fits in:
    - “Why is loss ratio higher this quarter?”
    - “Which brokers are driving increased Time to Bind?”

**Output:**  
Demo blueprint: sections for personas, dashboards, metrics, and story hooks.

## 3. Dataset Engineer Agent

- Takes the blueprint and generates:
  - Synthetic dataset(s) covering submissions, quotes, binds, claims.
  - 24+ months of data with:
    - Deteriorating metrics in one segment.
    - Stable or improving metrics in others.
- Produces:
  - Data dictionary
  - Metric definitions

**Output:**  
CSV schema and narrative of the key trends baked into the data.

## 4. Insurance Ops Analyst Agent

- Consumes the dataset and:
  - Confirms trends and provides additional insight framing.
  - Generates “What / Why / Now What” narratives.
  - Prepares conversational prompts:
    - “Which brokers have the worst submission quality?”
    - “Where are we seeing rising severity but stable frequency?”

**Output:**  
A set of Pulse/Agentforce-style insight scripts.

## 5. Demo Architect Agent (Refinement)

- Incorporates insights into final demo script.
- Aligns demo steps:
  - Navigate Book of Business → drill into underperforming segment → open GenAI Q&A → show “why”.
- Provides persona-specific demo variants (e.g., underwriter vs executive view).

## 6. Optional: Local App Builder Agent

- If there’s a custom front-end or local LLM component:
  - Builds Node/React boilerplate for advisor console.
  - Exposes endpoints to trigger Pulse-like questions or Agentforce flows.

**Final Outcome:**  
A ready-to-build insurance demo with data, insights, and a clear narrative.
