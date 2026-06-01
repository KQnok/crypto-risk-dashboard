# 🔴 Crypto Risk Dashboard

Detecting anomalous BTC price movements using z-score analysis.
Built as a risk monitoring tool — flags days where price behavior 
falls outside normal statistical range.

**Data source:** CoinGecko API (last 90 days, updated daily)

## What it does
- Fetches real BTC/USD price data via CoinGecko API
- Calculates daily returns and z-scores for each day
- Flags anomalies where |z-score| > 2 (statistically abnormal moves)
- Visualizes price chart with anomaly markers
- Tracks 30-day rolling volatility

## Key finding
4 anomalous days out of 90 (~4%) — all positive spikes.
BTC volatility stayed between 1.3-1.4% daily during the period.

## Stack
Python · pandas · numpy · requests · plotly · Streamlit

## Run locally
pip install -r requirements.txt
streamlit run app.py

## Why this matters for risk monitoring
In a live trading environment, z-score > 2 would trigger 
a review of open leveraged positions and margin exposure.