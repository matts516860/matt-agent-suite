# Tableau Calculations

Copy and paste these into Tableau after connecting Tableau Desktop to your local TabPy instance.

---

## 1) Predicted Total Goals

Create a calculated field named **Predicted Total Goals**:

```tableau
SCRIPT_REAL(
"return tabpy.query('predict_total_goals',
    years=_arg1,
    rounds=_arg2
)['response']",
ATTR([Year]),
ATTR([Round])
)
```

### Notes
- `[Year]` should be numeric.
- `[Round]` should be a string dimension with values such as `Group`, `Quarter-finals`, `Semi-finals`, `Final`, or `Round of 16`.
- If your source uses a different field name, update the formula accordingly.

---

## 2) Bayesian Predicted Goals

Create a calculated field named **Bayesian Predicted Goals**:

```tableau
SCRIPT_REAL(
"return tabpy.query('predict_goals_bayesian',
    years=_arg1,
    rounds=_arg2
)['response']",
ATTR([Year]),
ATTR([Round])
)
```

---

## 3) Bayesian Lower Bound

Create a calculated field named **Bayesian Lower Bound**:

```tableau
SCRIPT_REAL(
"return tabpy.query('predict_goals_bayesian_lower',
    years=_arg1,
    rounds=_arg2
)['response']",
ATTR([Year]),
ATTR([Round])
)
```

---

## 4) Bayesian Upper Bound

Create a calculated field named **Bayesian Upper Bound**:

```tableau
SCRIPT_REAL(
"return tabpy.query('predict_goals_bayesian_upper',
    years=_arg1,
    rounds=_arg2
)['response']",
ATTR([Year]),
ATTR([Round])
)
```

---

## 5) Prophet Forecast

Create a calculated field named **Prophet Forecast Goals**:

```tableau
SCRIPT_REAL(
"return tabpy.query('predict_goals_prophet',
    years=_arg1
)['response']",
ATTR([Year])
)
```

---

## Suggested Visuals

### Regression Demo
- Columns: `Year`
- Rows: `AVG([HomeGoals] + [AwayGoals])`
- Add **Predicted Total Goals** as a dual axis or comparison line

### Bayesian Demo
- Line or circle plot using **Bayesian Predicted Goals**
- Add **Bayesian Lower Bound** and **Bayesian Upper Bound** for interval bands

### Prophet Demo
- Plot historical total goals by year
- Overlay **Prophet Forecast Goals** for future tournaments

---

## Troubleshooting

### Error: analytics extension unavailable
Check:
- TabPy is running on `localhost:9004`
- Tableau Desktop analytics extension connection is configured
- The deployment scripts were run successfully

### Error: unknown function name
Re-run the corresponding deployment script:
- `python src/deploy_regression.py`
- `python src/deploy_bayesian.py`
- `python src/deploy_prophet.py`

### Field mismatch issues
If your data uses different field names or values for rounds, standardize the values before sending them to TabPy.
