import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Example data with additional features (dummy values for missing data)
data = {
    'Date': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04'],
    'Temperature': [25, 28, 30, 32],
    'Soil_Moisture': [60, 55, 50, 45],
    'Wind_Speed': [15, 10, 12, 18],  # Dummy data
    'Precipitation': [2, 1, 0, 0],  # Dummy data
    'Evapotranspiration': [4, 5, 6, 7],  # Dummy data
    'Irrigation_Water': [20, 25, 30, 35]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Normalizing the data
scaler = MinMaxScaler()
features = ['Temperature', 'Soil_Moisture', 'Wind_Speed', 'Precipitation', 'Evapotranspiration']
df[features] = scaler.fit_transform(df[features])

# Predictive variables and target
X = df[['Temperature', 'Soil_Moisture', 'Wind_Speed', 'Precipitation', 'Evapotranspiration']]
y = df['Irrigation_Water']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print the predictions and actual values
print("Predictions:", y_pred)
print("True values:", y_test.values)

# Save the model
joblib.dump(model, "irrigationPredictor.pkl")
