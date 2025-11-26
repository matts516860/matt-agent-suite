# VizQL Data Service + Local LLM App Workflow

This workflow shows how to build a small application that lets users query Tableau via VizQL Data Service and a local LLM.

## 1. Input

- Requirements for the app (e.g., “Field picker + question box, answer from local LLM”).
- Info about Tableau Cloud site and data sources.
- Info about the local LLM environment (llama.cpp, ollama, etc.).

## 2. Local App Builder Agent

- Designs architecture:
  - Frontend: React (field selector + text input + answer display).
  - Backend: Node/Express with routes:
    - `/fields` – list of fields from a data source (using VizQL Data Service).
    - `/query` – runs a query based on selected fields and filters.
    - `/ask` – sends context + question to local LLM.
- Generates:
  - File tree (`/server`, `/client`, `/shared`).
  - Code skeletons for key endpoints.
  - `.env` usage for PATs and base URLs.

**Output:**  
Code scaffolding + instructions.

## 3. Dataset Engineer Agent (Optional)

- Creates or describes a synthetic dataset:
  - So you can test the app without touching production data.
  - With interesting trends for the LLM to talk about.

## 4. Demo Architect Agent

- Defines how this app is used in a demo:
  - Scenario: Advisor asks natural language questions about Book of Business.
  - Flow:
    - Select customer segment → ask question → interpret answer.
  - Key talking points: self-service analytics, governed LLM, semantic model alignment.

## 5. Home & Life Assistant Agent (Optional)

- Helps with:
  - Local environment setup and dependencies.
  - Troubleshooting typical local dev issues (ports, node versions, etc.).

**Final Outcome:**  
A working skeleton of a VizQL + local LLM app plus a narrative for how to present it in a demo.
