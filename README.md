## 🤖 TalentMind: Dashboard de Tendências de Empregos do Futuro (FIAP)

Este projeto implementa uma solução de Deep Learning integrada com outras disciplinas (Desenvolvimento Web e Mobile) para prever e apresentar tendências de empregos futuros, com foco em IoT, IoB (Internet of Behaviors) e IA Generativa.

---

## 👥 Integrante

- Diego Bassalo Canals Silva – RM558710 | Turma 2TDSPG
- Giovanni de Souza Lima – RM556536 | Turma 2TDSPH
- Vitor Tadeu Soares de Sousa – RM559105 | Turma 2TDSPH

## 🎯 Requisitos Técnicos Atendidos

O projeto utiliza uma arquitetura integrada, demonstrando o uso de dois componentes de IA:

API de IA Generativa (Simulada): Geração de insights de texto e dados salariais estruturados sobre as profissões emergentes (servido via arquivo JSON).

API de Visão Computacional (Simulada): Classificação de texto que simula a identificação de áreas de foco (ex: "Análise de Dados", "Cibersegurança") a partir de um prompt do usuário.

## 🏗️ Arquitetura do Sistema

A solução segue um modelo de arquitetura de microsserviços simples, onde o Frontend e o Backend se comunicam via REST API, garantindo a separação de responsabilidades.

Componente

Tecnologia

Função

Backend (API)

Python (FastAPI)

Expõe os endpoints de /api/tendencias (dados da IA Generativa) e /predict-future-job (Classificação).

Frontend (Dashboard)

HTML, JavaScript, Bootstrap, Chart.js

Interface funcional que consome os dados do Backend, apresentando gráficos e a interação com o modelo de IA.

## 📁 Estrutura de Pastas

### A estrutura do projeto é organizada para facilitar a execução:

TalentMind/
├── backend/                  # Servidor Python e API
│   ├── main.py               # Lógica do FastAPI e Endpoints da IA
│   └── requirements.txt      # Dependências Python (fastapi, uvicorn, etc.)
├── data/                     # Arquivos de dados
│   └── tendencias_ia.json    # Insights de empregos gerados pela IA (dados brutos)
├── frontend/                 # Interface Web (Dashboard)
│   ├── index.html            # Estrutura do Dashboard e JavaScript de integração
│   └── style.css             # Estilização CSS
└── README.md                 # Este documento


## 🚀 Como Executar o Projeto

Para rodar a aplicação, siga os passos abaixo no seu terminal.

1. Preparação do Ambiente Python

Recomendamos o uso de um ambiente virtual (.venv) para isolar as dependências.

Instale as dependências:
```
pip install -r backend/requirements.txt
```

2. Iniciar o Servidor Backend (API)

Navegue até a pasta que contém o arquivo main.py:
```
cd backend
```

Inicie o servidor Uvicorn:
```
uvicorn main:app --reload
```

O servidor estará acessível em http://127.0.0.1:8000. Mantenha este terminal aberto e rodando.




