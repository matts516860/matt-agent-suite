import numpy as np
import pymc as pm
import pandas as pd
import tabpy_client

# Simple synthetic training data
years = np.arange(1930, 2015, 4)
goals = np.array([3.8,4.1,4.6,4.0,5.3,3.6,2.7,2.7,2.9,2.5,
                  2.6,2.8,2.5,2.2,2.7,2.6,2.5,2.3,2.2,2.6])

with pm.Model() as model:
    alpha = pm.Normal('alpha', mu=3, sigma=1)
    beta = pm.Normal('beta', mu=0, sigma=0.01)
    sigma = pm.HalfNormal('sigma', sigma=1)

    mu = alpha + beta * (years - years.mean())
    obs = pm.Normal('obs', mu=mu, sigma=sigma, observed=goals)

    trace = pm.sample(500, tune=500, progressbar=False)


def predict_goals_bayesian(years, rounds):
    years = np.array(years)
    alpha = trace.posterior['alpha'].values.mean()
    beta = trace.posterior['beta'].values.mean()
    return (alpha + beta * (years - years.mean())).tolist()


def predict_goals_bayesian_lower(years, rounds):
    years = np.array(years)
    alpha = trace.posterior['alpha'].values.mean()
    beta = trace.posterior['beta'].values.mean()
    return (alpha + beta * (years - years.mean()) - 0.5).tolist()


def predict_goals_bayesian_upper(years, rounds):
    years = np.array(years)
    alpha = trace.posterior['alpha'].values.mean()
    beta = trace.posterior['beta'].values.mean()
    return (alpha + beta * (years - years.mean()) + 0.5).tolist()

connection = tabpy_client.Client('http://localhost:9004/')

connection.deploy('predict_goals_bayesian', predict_goals_bayesian, 'Bayesian mean prediction', override=True)
connection.deploy('predict_goals_bayesian_lower', predict_goals_bayesian_lower, 'Lower bound', override=True)
connection.deploy('predict_goals_bayesian_upper', predict_goals_bayesian_upper, 'Upper bound', override=True)

print("Bayesian models deployed!")
