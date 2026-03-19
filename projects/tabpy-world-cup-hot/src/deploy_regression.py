import tabpy_client
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Training data
data = {
    'Year': [1930,1934,1938,1950,1954,1958,1962,1966,1970,1974,
             1978,1982,1986,1990,1994,1998,2002,2006,2010,2014],
    'Round_Type': ['Group','Group','Group','Group','Final',
                   'Semi-finals','Quarter-finals','Group','Final','Group',
                   'Semi-finals','Quarter-finals','Group','Final','Group',
                   'Round of 16','Quarter-finals','Semi-finals','Final','Group'],
    'AvgGoals': [3.89,4.12,4.67,4.00,5.38,3.60,2.78,2.78,2.97,2.55,
                 2.68,2.81,2.54,2.21,2.71,2.67,2.52,2.30,2.27,2.67]
}

df = pd.DataFrame(data)
le = LabelEncoder()
df['Round_Encoded'] = le.fit_transform(df['Round_Type'])

X = df[['Year', 'Round_Encoded']]
y = df['AvgGoals']

model = LinearRegression()
model.fit(X, y)

def predict_total_goals(years, rounds):
    known_rounds = list(le.classes_)
    encoded = []
    for r in rounds:
        if r in known_rounds:
            encoded.append(le.transform([r])[0])
        else:
            encoded.append(0)
    features = np.column_stack([years, encoded])
    return model.predict(features).tolist()

connection = tabpy_client.Client('http://localhost:9004/')
connection.deploy(
    'predict_total_goals',
    predict_total_goals,
    'Predicts average total goals for a match given Year and Round type',
    override=True
)

print("Model deployed successfully!")
