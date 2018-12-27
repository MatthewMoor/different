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

# Validation
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
melb_model.fit(train_X, train_y)

melb_model_prediction = melb_model.predict(val_X)
print(mean_absolute_error(val_y, melb_model_prediction))