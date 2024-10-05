import pandas as pd
from fastapi import FastAPI
from DataModel import DataModel
from joblib import load, dump
from Preprocessing import Preprocessing
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
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


@app.post("/retrain_predict")
def retrain_predict(data_models: List[DataModel]):
    data_list = [data_model.model_dump() for data_model in data_models]
    df = pd.DataFrame(data_list)
    cleaner = Preprocessing()
    data_cleaned = cleaner.fit_transform(df)
    x = data_cleaned.drop("Duracion_Estancia_Min", axis=1)
    y = data_cleaned["Duracion_Estancia_Min"]
    model = load("assets/modelo.joblib")
    model.fit(x, y)
    dump(model, "assets/new_modelo.joblib")
    new_model = load("assets/new_modelo.joblib")
    result = new_model.predict(x)
    result_dict = {
         "mean_squared_error": mean_squared_error(y, result),
         "mean_absolute_error": mean_absolute_error(y, result),
         "r2_score": r2_score(y, result)
    }
    return result_dict
