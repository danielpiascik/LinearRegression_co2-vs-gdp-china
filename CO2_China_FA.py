from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

app = FastAPI(debug=True)


@app.get("/docs")
def home():
    return {"Prediction of the CO2 emissions in China based on GDP per capital"}

@app.post("/predict")
def predict(GDP_per_capita: float):

    model = pickle.load(open("D:/CODS/! FAST API - Cwiczenia/CW_1_CO2_China/CO2_model_pickle.pkl", "rb"))
    make_prediction = model.predict([[GDP_per_capita]])
    output = round(make_prediction[0], 1)

    return {f"Model predict that when DGP of the Chine is equal {GDP_per_capita} dollars, then emission of the CO2 will be: {output} bln tonnes"}

if __name__ == "__main__":
    uvicorn.run(app)
