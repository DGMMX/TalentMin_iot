from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import json # Para ler o JSON
import os # Para manipular caminhos
# from transformers import pipeline # Mantenha se quiser usar a Classificação

# --- Configuração do FastAPI ---
app = FastAPI()

# Permite acesso do Frontend (Desenvolvimento Web) à API
# CORSMiddleware (no singular) foi corrigido
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite qualquer origem (pode ser restrito depois)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Modelo de IA (Você pode usar este ou o seu modelo de Classificação) ---
# classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

class Prompt(BaseModel):
    text: str

# --- 1. Endpoint: / (Raiz) ---
@app.get("/")
def read_root():
    return {"status": "FutureJobsAI API online"}

# --- 2. Endpoint: /api/tendencias (Integração com IA Generativa) ---
@app.get("/api/tendencias")
def get_ia_insights():
    """
    Serve o JSON de insights de empregos, simulando o resultado de uma
    API de IA Generativa (Geração de Texto).
    O caminho para o arquivo JSON foi ajustado para ser mais robusto, 
    assumindo a estrutura: Raiz/data/tendencias_ia.json
    """
    
    # GARANTE O CAMINHO CORRETO: 
    # os.path.dirname(os.path.abspath(__file__)) => Pasta backend
    # '..' => Volta para a pasta raiz (TalentMind)
    # 'data', 'tendencias_ia.json' => Entra na pasta data e pega o arquivo
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'tendencias_ia.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            dados_ia = json.load(f)
        
        return {
            "status": "success",
            "source": "AI Generativa (Simulada)",
            "data": dados_ia
        }
    except FileNotFoundError:
        # Retorna a mensagem de erro que você estava vendo no navegador
        return {"status": "error", "message": "Arquivo de dados da IA não encontrado! Verifique a pasta 'data'."}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# --- 3. Endpoint: /predict_future_job (Seu modelo de Classificação) ---
@app.post("/predict-future-job/")
def predict_future_job(prompt: Prompt):
    # EXEMPLO DE CLASSIFICAÇÃO: 
    # Mantenha esta parte para cumprir o requisito de Visão Computacional / Classificação
    labels = ["Engenharia de IA", "Cibersegurança", "Robótica", "Bioeconomia", "Análise de Dados"]
    
    # Se você não for usar o modelo real, simule a resposta
    if "dados" in prompt.text.lower():
        prediction = "Análise de Dados"
    elif "seguranca" in prompt.text.lower():
        prediction = "Cibersegurança"
    else:
        prediction = "Engenharia de IA"

    # Se quiser usar o modelo real, descomente e ajuste:
    # result = classifier(prompt.text, labels)
    # prediction = result['labels'][0]
    
    return {
        "input_prompt": prompt.text,
        "prediction": prediction,
        "confidence": "95% (Simulado)" # Adicione confiança para parecer mais profissional
    }

# --- REMOVIDO: Comentei ou removi o endpoint /salary para evitar erros de API externa. ---
# @app.get("/salary/{area}")
# def get_salary(area: str):
#     # ... código removido ...
#     pass # O Dashboard usará o JSON de /api/tendencias