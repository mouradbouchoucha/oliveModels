from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib
# Example data
data = {
    'Date': ['2024-09-01', '2024-09-02', '2024-09-03', '2024-09-04'],
    'Temperature': [25, 26, 27, 28],
    'Humidity': [70, 72, 65, 68],
    'Fly_Density': [10, 15, 20, 30],
    'Damage': [5, 8, 10, 15]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
# Predictor variables and target
# Model 1: Predict Fly Density
features_density = ['Temperature', 'Humidity']
X_density = df[features_density]
y_density = df['Fly_Density']

# Split data into training and test sets
X_train_density, X_test_density, y_train_density, y_test_density = train_test_split(X_density, y_density, test_size=0.2, random_state=42)

# Create and train Random Forest model
rf_density = RandomForestRegressor(n_estimators=100, random_state=42)
rf_density.fit(X_train_density, y_train_density)

# Predict fly density on the test set
y_pred_density = rf_density.predict(X_test_density)

# Evaluate the model
mse_density = mean_squared_error(y_test_density, y_pred_density)
print(f'Fly Density MSE: {mse_density}')


#################################################################

# Model 2: Predict Fly Damage
# Now using the predicted fly density as an additional feature
features_damage = ['Temperature', 'Humidity',  'Fly_Density']
X_damage = df[features_damage]
y_damage = df['Damage']

# Split data into training and test sets
X_train_damage, X_test_damage, y_train_damage, y_test_damage = train_test_split(X_damage, y_damage, test_size=0.2, random_state=42)

# Create and train Random Forest model for damage
rf_damage = RandomForestRegressor(n_estimators=100, random_state=42)
rf_damage.fit(X_train_damage, y_train_damage)

# Predict damage on the test set
y_pred_damage = rf_damage.predict(X_test_damage)

# Evaluate the model
mse_damage = mean_squared_error(y_test_damage, y_pred_damage)
print(f'Fly Damage MSE: {mse_damage}')

joblib.dump(rf_density,"fly_desity_model.pkl")
joblib.dump(rf_damage,"fly_damage_model.pkl")