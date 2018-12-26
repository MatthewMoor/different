import pandas as pd
from sklearn.tree import DecisionTreeRegressor

filename = "melb_data.csv"
melb_data = pd.read_csv(filename)

# Prediction target
y = melb_data.Price

# Features
melb_data_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melb_data[melb_data_features]

print('X describe and head:')
print(X.describe())
print(X.head())

melb_model = DecisionTreeRegressor(random_state=1)

melb_model.fit(X, y)

# Predictions
print('Making predictions for the following 5 houses')
print(X.head())
print("The predictions are")
print(melb_model.predict(X.head()))