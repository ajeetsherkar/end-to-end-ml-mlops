from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI(title="Laptop Price Prediction API")

# Load model (absolute-safe path)
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "laptop_price_model_v2.pkl"
)

model = joblib.load(MODEL_PATH)


# Input schema (MUST match training columns exactly)
class LaptopInput(BaseModel):
    Company: str
    TypeName: str
    Inches: float
    ScreenResolution: str
    Cpu: str
    Ram: str
    Memory: str
    Gpu: str
    OpSys: str
    Weight: float


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict")
def predict_price(data: LaptopInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Predict
    prediction = model.predict(input_df)[0]

    return {"predicted_price": round(float(prediction), 2)}
