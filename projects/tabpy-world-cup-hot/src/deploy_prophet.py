import pandas as pd
import numpy as np
from prophet import Prophet
import tabpy_client

# Training data
df = pd.DataFrame({
    'ds': pd.date_range(start='1930', periods=20, freq='4Y'),
    'y': [3.8,4.1,4.6,4.0,5.3,3.6,2.7,2.7,2.9,2.5,
          2.6,2.8,2.5,2.2,2.7,2.6,2.5,2.3,2.2,2.6]
})

model = Prophet()
model.fit(df)


def predict_goals_prophet(years):
    future = pd.DataFrame({'ds': pd.to_datetime(years, format='%Y')})
    forecast = model.predict(future)
    return forecast['yhat'].tolist()

connection = tabpy_client.Client('http://localhost:9004/')
connection.deploy('predict_goals_prophet', predict_goals_prophet, 'Prophet forecast', override=True)

print("Prophet model deployed!")
