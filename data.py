import requests
import pandas as pd

def get_btc_data(days=90):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"

    params = {
    "vs_currency": "usd",
    "days": str(days),
    "interval": "daily"
    }

    response = requests.get(url, params=params)
    data = response.json()

    response.raise_for_status()

    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.drop(columns=['timestamp'])
    df = df[df['date'].dt.date < pd.Timestamp.today().date()]

    return df

