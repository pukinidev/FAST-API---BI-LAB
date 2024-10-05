from typing import Optional
import pandas as pd
from fastapi import FastAPI
from DataModel import DataModel
from joblib import load, dump
from Preprocessing import Preprocessing

app = FastAPI()

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    data = dataModel.model_dump()
    df = pd.DataFrame([data], columns=data.keys(), index=[0])
    cleaner = Preprocessing()
    data_cleaned = cleaner.fit_transform(df)
    x = data_cleaned.drop("Duracion_Estancia_Min", axis=1)
    model = load("assets/modelo.joblib")
    result = model.predict(x)
    return result.tolist()
