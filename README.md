# matt-agent-suite

A curated stack of seven specialized AI agents designed for **Solution Engineering**, **Tableau / Agentforce demos**, **insurance analytics**, **local LLM apps**, and **personal workflows** (travel, home projects, YouTube, etc.).

## Agents

1. **Demo Architect** – turns messy discovery into clean demo architectures, flows, and narratives.
2. **Dataset Engineer** – generates realistic synthetic datasets (10k–100k rows) with trends and story hooks.
3. **Tableau Cloud Ops** – interprets Admin Insights / Activity logs for performance & licensing.
4. **Local App Builder** – scaffolds Node/React apps that connect VizQL Data Service ↔ local LLMs.
5. **Insurance Ops Analyst** – reads insurance datasets and produces underwriter-quality insights.
6. **Trip Concierge** – builds optimized, kid-friendly trip itineraries with backups.
7. **Home & Life Assistant** – helps with 3D printing, HVAC, Nautilus, YouTube, fitness, cats, and home projects.

Each agent has its own system prompt in `agents/` and participates in multi-agent workflows defined in `workflows/`.

---

## Repository Structure

```text
matt-agent-suite/
├── README.md
├── LICENSE
├── manifest.json
├── agents/
│   ├── demo-architect.md
│   ├── dataset-engineer.md
│   ├── tableau-cloud-ops.md
│   ├── local-app-builder.md
│   ├── insurance-ops-analyst.md
│   ├── trip-concierge.md
│   └── home-life-assistant.md
├── workflows/
│   ├── insurance-demo-flow.md
│   ├── vizql-local-llm-flow.md
│   ├── claims-pulse-weekly.md
│   ├── trip-planning-flow.md
│   └── home-projects-flow.md
├── templates/
│   ├── example-prompts.md
│   ├── semantic-model-skeleton.md
│   ├── dataset-requirements.md
│   ├── architecture-blueprint.md
│   └── insurance-kpi-definitions.md
└── .gitignore
```

---

## How to Use This Repo

### 1. As documentation for Agent Mode

Use each `agents/*.md` file as the **system prompt** for a dedicated agent in your Agent Mode or orchestration framework.

Example:

- Create an agent called **"Demo Architect"**.
- Paste the contents of `agents/demo-architect.md` into the agent’s system prompt.
- Optionally constrain that agent to specific tools (e.g., docs, code generation, data exploration).

### 2. As a pattern library for other customers

You can clone this repo and adapt:

- Agents to specific industries (Banking / Healthcare / Retail).
- Workflows to specific demo motions.
- Templates for semantic models and datasets.

---

## GitHub: How to Publish This Repo

After downloading/unzipping:

```bash
cd matt-agent-suite

# Initialize git
git init
git add .
git commit -m "Initial commit: Matt agent suite"

# Add your GitHub remote (replace USERNAME with your GitHub handle)
git branch -M main
git remote add origin git@github.com:USERNAME/matt-agent-suite.git

# Or with HTTPS:
# git remote add origin https://github.com/USERNAME/matt-agent-suite.git

git push -u origin main
```

Once pushed, you can:

- Link this repo into your agent/orchestration framework.
- Use it as a reference library.
- Share with your team as **“Matt’s Agent Stack”**.

---

## License

This project is licensed under the **MIT License** – see [`LICENSE`](./LICENSE) for details.
