from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd

# Example data
data = {
    'Temperature': [18, 20, 22, 24],
    'Humidity': [65, 70, 75, 80],
    'Precipitation': [5, 10, 15, 20],
    'Treatment_Density': [0, 1, 2, 3],
    'Symptoms': [1, 2, 3, 4],
    'Olive_Yield_kg': [15, 14, 12, 9]
    
}

df = pd.DataFrame(data)

# Features for symptoms prediction
X_symptoms = df[['Temperature', 'Humidity', 'Precipitation', 'Treatment_Density']]
y_symptoms = df['Symptoms']

# Train-test split
X_train_symptoms, X_test_symptoms, y_train_symptoms, y_test_symptoms = train_test_split(X_symptoms, y_symptoms, test_size=0.2, random_state=42)

# Train Random Forest for Symptoms
rf_symptoms = RandomForestRegressor(n_estimators=100, random_state=42)
rf_symptoms.fit(X_train_symptoms, y_train_symptoms)

# Save the symptoms model
joblib.dump(rf_symptoms, 'rf_symptoms_model.pkl')


#############################################################


# Features for olive yield prediction
X_yield = df[['Temperature', 'Humidity', 'Precipitation', 'Treatment_Density','Symptoms']]
y_yield = df['Olive_Yield_kg']

# Train-test split
X_train_yield, X_test_yield, y_train_yield, y_test_yield = train_test_split(X_yield, y_yield, test_size=0.2, random_state=42)

# Train Random Forest for Olive Yield
rf_yield = RandomForestRegressor(n_estimators=100, random_state=42)
rf_yield.fit(X_train_yield, y_train_yield)

# Save the olive yield model
joblib.dump(rf_yield, 'rf_yield_model.pkl')

