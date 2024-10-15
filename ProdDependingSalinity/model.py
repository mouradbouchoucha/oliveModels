import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Example data for production per salinity (replace with actual data)
data = {
    'Date': ['2024-04-01', '2024-04-15', '2024-05-01', '2024-05-15'],
    'Soil_Salinity': [2.5, 3.0, 3.5, 4.0],
    'Soil_Moisture': [25, 23, 22, 20],
    'Soil_Temperature': [22, 24, 25, 26],
    'Irrigation': [5, 5.5, 6, 6.5],
    'Salt_in_Water': [50, 55, 60, 65],
    'Soil_pH': [6.5, 6.8, 7.0, 7.2],
    'Olive_Yield': [12, 11, 10, 9]  # Target variable
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Normalizing the data
scaler = MinMaxScaler()
features = ['Soil_Salinity', 'Soil_Moisture', 'Soil_Temperature', 'Irrigation', 'Salt_in_Water', 'Soil_pH']
df[features] = scaler.fit_transform(df[features])

# Predictive variables and target
X = df[features]
y = df['Olive_Yield']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Random Forest model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print the predictions and actual values
print("Predictions:", y_pred)
print("True values:", y_test.values)

# Save the trained model, not the predictions
joblib.dump(model, 'prodPerSalinity.pkl')
