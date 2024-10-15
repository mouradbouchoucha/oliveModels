Base URL:
arduino
Copy code
http://<your-server>:8000
Endpoints:

1. Predict Disease
Endpoint: /predict_disease
Method: POST
Description: Predicts the disease status of a plant based on environmental factors and growth phase.
Request Body:

json
Copy code
{
  "temperature": 25.0,
  "humidity": 60.0,
  "precipitation": 5.0,
  "sunlight": 8.0,
  "phase": 1
}
temperature: (float) Temperature in degrees Celsius.
humidity: (float) Humidity percentage.
precipitation: (float) Precipitation in mm.
sunlight: (float) Sunlight in hours.
phase: (int) Encoded phase of the plant (0, 1, 2).
Response:

json
Copy code
{
  "disease_predicted": 0
}

******************************************************


disease_predicted: (int) Predicted disease status (0 for healthy, 1 for diseased).
2. Predict Fly Density
Endpoint: /predict_fly_density
Method: POST
Description: Predicts fly density based on environmental data.
Request Body:

json
Copy code
{
  "temperature": 26.0,
  "humidity": 70.0
}
temperature: (float) Temperature in degrees Celsius.
humidity: (float) Humidity percentage.
Response:

json
Copy code
{
  "fly_density_predicted": 15.0
}
fly_density_predicted: (float) Predicted fly density.

**********************************************


3. Predict Fly Damage
Endpoint: /predict_fly_damage
Method: POST
Description: Predicts fly damage to plants based on fly density and environmental factors.
Request Body:

json
Copy code
{
  "temperature": 26.0,
  "humidity": 70.0,
  "fly_density": 15.0
}

temperature: (float) Temperature in degrees Celsius.
humidity: (float) Humidity percentage.
fly_density: (float) Fly density value.
Response:

json
Copy code
{
  "fly_damage_predicted": 8.0
}
fly_damage_predicted: (float) Predicted damage due to flies.

*************************************************************************


4. Predict Fungal Symptoms
Endpoint: /predict_symptoms
Method: POST
Description: Predicts the severity of fungal disease symptoms based on environmental data and treatment density.
Request Body:

json
Copy code
{
  "temperature": 24.0,
  "humidity": 80.0,
  "precipitation": 10.0,
  "treatment_density": 2
}
temperature: (float) Temperature in degrees Celsius.
humidity: (float) Humidity percentage.
precipitation: (float) Precipitation in mm.
treatment_density: (int) Number of treatments applied.
Response:

json
Copy code
{
  "symptoms_predicted": 3.0
}
symptoms_predicted: (float) Predicted severity of symptoms (scale from 0 to 5).

****************************************************************


5. Predict Olive Yield
Endpoint: /predict_olive_yield
Method: POST
Description: Predicts olive yield based on environmental data, treatment density, and symptoms.
Request Body:

json
Copy code
{
  "temperature": 24.0,
  "humidity": 70.0,
  "precipitation": 5.0,
  "treatment_density": 2,
  "Symptoms": 3
}
temperature: (float) Temperature in degrees Celsius.
humidity: (float) Humidity percentage.
precipitation: (float) Precipitation in mm.
treatment_density: (int) Number of treatments applied.
Symptoms: (int) Severity of symptoms (scale from 0 to 5).
Response:

json
Copy code
{
  "olive_yield_predicted": 10.5
}
olive_yield_predicted: (float) Predicted olive yield in kilograms per tree.

***************************************************************


6. Predict Irrigation Needs
Endpoint: /predict_irrigation
Method: POST
Description: Predicts the required amount of irrigation water based on environmental data.
Request Body:

json
Copy code
{
  "temperature": 30.0,
  "soil_moisture": 50.0,
  "wind_speed": 12.0,
  "precipitation": 0.0,
  "evapotranspiration": 5.0
}
temperature: (float) Temperature in degrees Celsius.
soil_moisture: (float) Soil moisture percentage.
wind_speed: (float) Wind speed in km/h.
precipitation: (float) Precipitation in mm.
evapotranspiration: (float) Evapotranspiration in mm/day.
Response:

json
Copy code
{
  "irrigation_predicted": 30.0
}
irrigation_predicted: (float) Predicted irrigation water in liters per day.

*********************************************


7. Predict Olive Yield Based on Soil Salinity
Endpoint: /predict_salinity_yield
Method: POST
Description: Predicts olive yield based on soil salinity and environmental factors.
Request Body:

json
Copy code
{
  "soil_salinity": 3.5,
  "soil_moisture": 22.0,
  "soil_temperature": 25.0,
  "irrigation": 6.0,
  "salt_in_water": 60.0,
  "soil_ph": 7.0
}
soil_salinity: (float) Soil salinity (Electrical Conductivity).
soil_moisture: (float) Soil moisture percentage.
soil_temperature: (float) Soil temperature in degrees Celsius.
irrigation: (float) Irrigation water in liters/day.
salt_in_water: (float) Salt concentration in irrigation water (mg/L).
soil_ph: (float) Soil pH level.
Response:

json
Copy code
{
  "predicted_olive_yield": 10.0
}
predicted_olive_yield: (float) Predicted olive yield based on soil salinity and other factors.
Error Responses:
500 Internal Server Error: Returned if there is an issue loading the model, e.g., if the model file is not found.
Example Error Response:

json
Copy code
{
  "detail": "Model file not found: [error message]"
}
