from typing import Optional
import pandas as pd
from fastapi import FastAPI
from DataModel import DataModel
from joblib import load, dump
from Preprocessing import Preprocessing
from typing import List

app = FastAPI()

@app.post("/predict")
def make_predictions(data_models: List[DataModel]):
    data_list = [data_model.model_dump() for data_model in data_models]
    df = pd.DataFrame(data_list)
    cleaner = Preprocessing()
    data_cleaned = cleaner.fit_transform(df)
    x = data_cleaned.drop("Duracion_Estancia_Min", axis=1)
    model = load("assets/modelo.joblib")
    result = model.predict(x)
    result_list = result.tolist()
    return result_list
