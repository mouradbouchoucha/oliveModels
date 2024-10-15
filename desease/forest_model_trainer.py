import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib


data = {
    'Date': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04'],
    'Temperature': [26, 27, 25, 22],
    'Humidity': [70, 80, 90, 95],
    'Precipitation': [5, 10, 15, 18],
    'Sunlight': [8, 6, 4, 3],
    'Phase': ['young', 'adult', 'adult', 'adult'],
    'Disease': [0, 0, 1, 1]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
# print(df)

# Encode the categorical 'Phase' column
encoder = LabelEncoder()
df['Phase_encoded'] = encoder.fit_transform(df['Phase'])

# Normalize the features
scaler = MinMaxScaler()
features = ['Temperature', 'Humidity', 'Precipitation', 'Sunlight', 'Phase_encoded']
df[features] = scaler.fit_transform(df[features])
# print(df)

# Define features (X) and target (y)
X = df[['Temperature', 'Humidity', 'Precipitation', 'Sunlight', 'Phase_encoded']]
y = df['Disease']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:", classification_report(y_test, y_pred))

# Save the trained model to a file for future use
joblib.dump(model, 'random_forest_model.pkl')
