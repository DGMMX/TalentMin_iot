import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

st.title("📊 FutureJobsAI – Tendências de Empregos do Futuro")

st.sidebar.header("Opções")
area = st.sidebar.text_input("Área para buscar salários (ex: 2122)")

if st.sidebar.button("Buscar Dados"):
    r = requests.get(f"http://localhost:8000/salary/?area={area}")
    st.json(r.json())

st.header("📈 Crescimento de Áreas de Tecnologia")
df = pd.DataFrame({
    "Área": ["IA", "Cloud", "Cibersegurança", "Dados"],
    "Crescimento (%)": [48, 33, 52, 41]
})

fig, ax = plt.subplots()
ax.bar(df["Área"], df["Crescimento (%)"])
st.pyplot(fig)

st.header("🤖 Previsão de Carreiras Emergentes")
prompt = st.text_area("Descreva tendências tecnológicas:")

if st.button("Prever"):
    r = requests.post("http://localhost:8000/predict-future-job/", json={"text": prompt})
    st.subheader("Profissão prevista:")
    st.write(r.json()["prediction"])
