from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.User_input import UserInput
from Model.prediction import predict_output, model, version
from schema.prediction_response import PredictionResponse

app = FastAPI()


@app.get('/')
def home():
    return JSONResponse(content={"message": "Welcome to the Rainfall Prediction API"})

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok",'version': version,'model_loaded': model is not None})
    


@app.post("/predict", response_model=PredictionResponse)
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

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:

        return JSONResponse(status_code=500, content=str(e))