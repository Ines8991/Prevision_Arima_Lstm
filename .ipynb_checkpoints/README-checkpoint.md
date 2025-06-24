# 📊 Prédiction des prix financiers avec ARIMA + LSTM

Ce projet utilise les modèles **ARIMA** et **LSTM** pour prévoir les prix de clôture d’un actif financier, en y ajoutant des **indicateurs techniques** comme le RSI, EMA(20) et MACD, ainsi qu’un **signal de trading** (Buy/Sell/Hold).

---

## ⚙️ Contenu

- `Prévision_ARIMA_LSTM.ipynb` : modèle, pré-traitement, calculs
- `df.csv` : fichier de données enrichi
- `app.py` : interface interactive avec Streamlit

---

## 🚀 Lancer l’application

```bash
streamlit run app.py
```

---

## 📦 Librairies requises

```bash
pip install pandas numpy matplotlib streamlit plotly ta
```

---

## 🖼️ Visualisations

- Évolution des prix (réels vs prédits)
- Résidus ARIMA
- Signal de trading MACD

---

## 📄 Licence

Projet éducatif à usage libre.
