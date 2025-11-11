from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.User_input import UserInput
app = FastAPI()


@app.get('/')
def home():
    return JSONResponse(content={"message": "Welcome to the Rainfall Prediction API"})

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"})


@app.get("/predict")
def predict_rainfall(data : UserInput):
    user_input = {
        "pressure": data.pressure,
        "dewpoint": data.dewpoint,
        "humidity": data.humidity,
        "cloud": data.cloud,
        "sunshine": data.sunshine,
        "wind_direction": data.wind_direction,
        "wind_speed": data.wind_speed
    }
    