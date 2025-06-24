import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
# 📂 Lecture du fichier exporté
df = pd.read_csv("data/df.csv")

st.set_page_config(page_title="Prévision ARIMA + LSTM", layout="wide")
st.title("📈 Analyse & Prévision des prix")

# 📌 Aperçu
st.subheader("Aperçu des données")
st.dataframe(df.head())

# 📊 Visualisation
st.subheader("Évolution des prix réels et prévus (ARIMA)")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['Close'], label='Données réelles')
ax.plot(df['ARIMA_Pred'], label='Prédictions ARIMA')
ax.set_title("Comparaison Close vs ARIMA")
ax.legend()
st.pyplot(fig)

# 🧮 Si les résidus sont présents
if 'residuals' in df.columns:
    st.subheader("Distribution des résidus")
    fig2, ax2 = plt.subplots()
    ax2.hist(df['residuals'].dropna(), bins=30)
    ax2.set_title("Histogramme des résidus")
    st.pyplot(fig2)
# 📈 Visualisation interactive avec Plotly
if 'Date' in df.columns:
    st.subheader("Visualisation interactive (Plotly)")
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Réel'))
    fig3.add_trace(go.Scatter(x=df['Date'], y=df['ARIMA_Pred'], mode='lines', name='ARIMA'))
    fig3.update_layout(title="Évolution temporelle interactive", xaxis_title="Date", yaxis_title="Prix")
    st.plotly_chart(fig3, use_container_width=True)

st.subheader("📌 Signal de trading MACD (Buy / Sell / Hold)")

fig_signal = px.scatter(df, x="Date", y="Close", color="signal",
                        title="Signal basé sur croisement MACD",
                        color_discrete_map={"Buy": "green", "Sell": "red", "Hold": "gray"})

st.plotly_chart(fig_signal, use_container_width=True)

# 📌 Footer
st.markdown("**Projet LSTM + ARIMA — Streamlit**")
