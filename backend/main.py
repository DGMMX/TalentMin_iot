# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import numpy as np
from transformers import pipeline

app = FastAPI()

# modelo de IA (HuggingFace zero-shot classification)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class Prompt(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "FutureJobsAI API online"}

@app.get("/salary/")
def get_salary(area: str):
    # Exemplo real: média salarial BrasilAPI
    url = f"https://brasilapi.com.br/api/cbo/v1/{area}"
    try:
        response = requests.get(url).json()
        return {"area": area, "cargos": response}
    except:
        return {"error": "Área não encontrada"}

@app.post("/predict-future-job/")
def predict_future_job(prompt: Prompt):
    labels = [
        "Engenharia de IA",
        "Cibersegurança",
        "Robótica",
        "Biotecnologia",
        "Análise de Dados",
        "Computação Quântica",
        "Energia Renovável",
    ]

    result = classifier(prompt.text, labels)
    return {
        "input": prompt.text,
        "prediction": result["labels"][0],
        "scores": result["scores"]
    }
