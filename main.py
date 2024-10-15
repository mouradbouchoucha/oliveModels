from http.client import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load the trained models
try:
    model = joblib.load('./desease/random_forest_model.pkl')
    rf_density = joblib.load('./fly_desity_damage/fly_desity_model.pkl')  # Model to predict fly density
    rf_damage = joblib.load('./fly_desity_damage/fly_damage_model.pkl')   # Model to predict fly damage
    rf_symptoms = joblib.load('./deseaseFongiques/rf_symptoms_model.pkl') # Model to predict symptoms
    rf_yield = joblib.load('./deseaseFongiques/rf_yield_model.pkl')       # Model to predict olive yield
    rf_irrigation = joblib.load('./IrregationPredict/irrigationPredictor.pkl')  # Model to predict irrigation
    rf_prodSalinity = joblib.load('./ProdDependingSalinity/prodPerSalinity.pkl')
except FileNotFoundError as e:
    raise HTTPException(status_code=500, detail=f"Model file not found: {str(e)}")
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error loading model: {str(e)}")

# Input structure for disease prediction
class InputData(BaseModel):
    temperature: float
    humidity: float
    precipitation: float
    sunlight: float
    phase: int  # Use encoded phase (0, 1, 2)

@app.post("/predict_disease")
def predict_disease(data: InputData):
    input_data = pd.DataFrame([{
        'Temperature': data.temperature,
        'Humidity': data.humidity,
        'Precipitation': data.precipitation,
        'Sunlight': data.sunlight,
        'Phase_encoded': data.phase
    }])
    prediction = model.predict(input_data)
    return {"disease_predicted": int(prediction[0])}

# Define the input structure for the fly density prediction
class FlyDensityInput(BaseModel):
    temperature: float
    humidity: float

@app.post("/predict_fly_density")
def predict_fly_density(input_data: FlyDensityInput):
    input_df = pd.DataFrame([{
        'Temperature': input_data.temperature,
        'Humidity': input_data.humidity
    }])
    
    fly_density_prediction = rf_density.predict(input_df)
    return {"fly_density_predicted": float(fly_density_prediction[0])}

# Input structure for the fly damage prediction
class FlyDamageInput(BaseModel):
    temperature: float
    humidity: float
    fly_density: float

@app.post("/predict_fly_damage")
def predict_fly_damage(input_data: FlyDamageInput):
    input_df = pd.DataFrame([{
        'Temperature': input_data.temperature,
        'Humidity': input_data.humidity,
        'Fly_Density': input_data.fly_density
    }])
    
    fly_damage_prediction = rf_damage.predict(input_df)
    return {"fly_damage_predicted": float(fly_damage_prediction[0])}

# Input structure for symptoms prediction
class SymptomsInput(BaseModel):
    temperature: float
    humidity: float
    precipitation: float
    treatment_density: int

@app.post("/predict_symptoms")
def predict_symptoms(input_data: SymptomsInput):
    input_df = pd.DataFrame([{
        'Temperature': input_data.temperature,
        'Humidity': input_data.humidity,
        'Precipitation': input_data.precipitation,
        'Treatment_Density': input_data.treatment_density
    }])

    symptoms_prediction = rf_symptoms.predict(input_df)
    return {"symptoms_predicted": float(symptoms_prediction[0])}

# Input structure for olive yield prediction
class OliveYieldInput(BaseModel):
    temperature: float
    humidity: float
    precipitation: float
    treatment_density: int
    Symptoms: int

@app.post("/predict_olive_yield")
def predict_olive_yield(input_data: OliveYieldInput):
    input_df = pd.DataFrame([{
        'Temperature': input_data.temperature,
        'Humidity': input_data.humidity,
        'Precipitation': input_data.precipitation,
        'Treatment_Density': input_data.treatment_density,
        'Symptoms': input_data.Symptoms
    }])

    olive_yield_prediction = rf_yield.predict(input_df)
    return {"olive_yield_predicted": float(olive_yield_prediction[0])}

# Input structure for irrigation prediction
class IrrigationInput(BaseModel):
    temperature: float
    soil_moisture: float
    wind_speed: float
    precipitation: float
    evapotranspiration: float

@app.post("/predict_irrigation")
def predict_irrigation(input_data: IrrigationInput):
    input_df = pd.DataFrame([{
        'Temperature': input_data.temperature,
        'Soil_Moisture': input_data.soil_moisture,
        'Wind_Speed': input_data.wind_speed,
        'Precipitation': input_data.precipitation,
        'Evapotranspiration': input_data.evapotranspiration
    }])

    irrigation_prediction = rf_irrigation.predict(input_df)
    return {"irrigation_predicted": float(irrigation_prediction[0])}

class OliveYieldInput(BaseModel):
    soil_salinity: float  # Salinity of the soil (EC)
    soil_moisture: float  # Soil moisture (%)
    soil_temperature: float  # Soil temperature (°C)
    irrigation: float  # Irrigation (L/day)
    salt_in_water: float  # Salt concentration in irrigation water (mg/L)
    soil_ph: float  # Soil pH

# POST method to predict olive yield
@app.post("/predict_salinity_yield")
def predict_olive_yield(input_data: OliveYieldInput):
    # Convert input data to a DataFrame for model prediction
    input_df = pd.DataFrame([{
        'Soil_Salinity': input_data.soil_salinity,
        'Soil_Moisture': input_data.soil_moisture,
        'Soil_Temperature': input_data.soil_temperature,
        'Irrigation': input_data.irrigation,
        'Salt_in_Water': input_data.salt_in_water,
        'Soil_pH': input_data.soil_ph
    }])

    # Use the model to predict olive yield
    yield_prediction = rf_prodSalinity.predict(input_df)

    # Return the predicted yield
    return {"predicted_olive_yield": float(yield_prediction[0])}