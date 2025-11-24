from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
import random
from pathlib import Path # Importação crucial para tratamento de caminhos

# Imports para servir arquivos estáticos (HTML/CSS/JS)
from fastapi.staticfiles import StaticFiles

# Classe base para o modelo Pydantic do prompt
class PromptModel(BaseModel):
    text: str

# --- CONFIGURAÇÃO DE DIRETÓRIOS ---
# Definimos o caminho da pasta raiz do projeto usando pathlib para maior robustez
# A raiz é um nível acima do 'backend' (TalentMin_iot/)
# .resolve().parent.parent move-se de 'main.py' -> 'backend' -> 'TalentMin_iot/'
ROOT_DIR = Path(__file__).resolve().parent.parent

# Agora, definimos os caminhos usando a raiz do projeto.
FRONTEND_DIR = ROOT_DIR / 'frontend'
DATA_FILE = ROOT_DIR / 'data' / 'tendencias_ia.json'

# --- CONFIGURAÇÃO DE ROTEAMENTO ESTÁTICO DE PÁGINA ÚNICA ---
# 1. Cria um objeto StaticFiles que sabe como servir a pasta 'frontend'
#    'html=True' é CRUCIAL: ele força o servidor a servir o index.html
#    automaticamente quando o caminho é a raiz da montagem (/).
static_app = StaticFiles(directory=FRONTEND_DIR, html=True)

# 2. Inicializa o FastAPI 
# Desabilita docs_url na raiz para evitar conflito com o index.html.
app = FastAPI(docs_url="/docs", redoc_url=None) 

# --- 1. MIDDLEWARE CORS ---
# Permite acesso de qualquer origem, necessário para o front-end acessar a API
origins = ["*"] 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. SERVIR ARQUIVOS ESTÁTICOS NA RAIZ (Substitui @app.get("/")) ---

# Monta o StaticApp na URL raiz ( / )
# Esta montagem tem a mais alta prioridade e deve exibir o index.html.
app.mount("/", static_app, name="dashboard_files")

# --- 3. ROTAS DA API DE DADOS ---

def load_ai_data():
    """Carrega os dados de tendências a partir do arquivo JSON."""
    try:
        # Usamos Path().open() para garantir a abertura correta do arquivo
        with DATA_FILE.open('r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERRO: Arquivo de dados não encontrado em {DATA_FILE}")
        raise HTTPException(status_code=404, detail="Arquivo de dados da IA não encontrado.")
    except json.JSONDecodeError:
        print(f"ERRO: Erro ao decodificar JSON em {DATA_FILE}")
        raise HTTPException(status_code=500, detail="Erro de formatação no arquivo JSON de dados.")


@app.get("/api/tendencias")
def get_tendencias():
    """Endpoint que o dashboard usa para obter os dados de tendências."""
    try:
        data = load_ai_data()
        return {
            "status": "success",
            "source": "AI Generativa (Simulada)",
            "data": data
        }
    except HTTPException as e:
        return {"status": "error", "message": e.detail}


@app.post("/predict-future-job/")
def predict_future_job(prompt: PromptModel):
    """Endpoint para classificação da IA (simulado ou real)."""
    
    # Simulação de resposta da IA
    labels_simulados = [
        "Internet of Things (IoT) & Edge Computing", 
        "Sustentabilidade e Data Science (ESG)", 
        "Inteligência Artificial Generativa", 
        "Especialista em Ética de IA"
    ]
    
    prediction = random.choice(labels_simulados)
    confidence_score = random.uniform(0.75, 0.99)
    confidence = f"{confidence_score:.2f}%"
    
    return {
        "input_prompt": prompt.text,
        "prediction": prediction,
        "confidence": confidence
    }