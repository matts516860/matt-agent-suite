# TabPy World Cup HoT Project

A hands-on project scaffold for the **TC26 HoT: Analytics Extensions & TabPy — World Cup Exercise**.

This project packages the core ideas from the workshop into runnable Python scripts and Tableau-ready calculation snippets:

- Start and connect to a local TabPy server
- Deploy a scikit-learn regression model to predict total goals by **Year** and **Round**
- Optionally deploy a Bayesian forecasting model with PyMC for uncertainty bands
- Optionally deploy a Prophet forecast model for a lighter-weight forecasting extension
- Reuse Tableau calculated fields directly from a markdown reference

## Project Structure

```text
projects/tabpy-world-cup-hot/
├── README.md
├── requirements.txt
├── tableau-calculations.md
├── data/
│   └── world_cup_training_data.csv
└── src/
    ├── deploy_regression.py
    ├── deploy_bayesian.py
    └── deploy_prophet.py
```

## Prerequisites

- Python 3.10+
- Tableau Desktop
- TabPy

## Quick Start

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start TabPy

```bash
tabpy
```

By default, TabPy runs at `http://localhost:9004`.

### 4. Deploy the regression model

```bash
python src/deploy_regression.py
```

### 5. Optional: deploy the Bayesian extension

```bash
python src/deploy_bayesian.py
```

### 6. Optional: deploy the Prophet extension

```bash
python src/deploy_prophet.py
```

## Tableau Connection

In Tableau Desktop:

1. Go to **Help → Settings and Performance → Manage Analytics Extension Connection**
2. Choose **TabPy/External API**
3. Hostname: `localhost`
4. Port: `9004`
5. Click **Test Connection**

## Dataset Notes

The included CSV is the small historical training dataset used by the regression script. The Tableau exercise itself expects a richer match-level dataset, such as a `WorldCupMatches` sheet with fields like:

- `Year`
- `Round`
- `HomeGoals`
- `AwayGoals`

## Tableau Calculations

See [`tableau-calculations.md`](./tableau-calculations.md) for copy/paste-ready calculated fields.

## Cloud Considerations

If adapting this to Tableau Cloud:

- TabPy must be reachable over the public internet
- HTTPS/SSL should be enabled
- Tableau Cloud egress IPs should be allowlisted on the TabPy host

## Purpose

This project is intended as a workshop starter repo and demo artifact. It is structured so you can expand it into:

- a more robust demo
- a customer workshop lab
- a packaged analytics extensions example
- a proof-of-concept for external model scoring from Tableau
