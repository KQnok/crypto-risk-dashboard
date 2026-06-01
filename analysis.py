import pandas as pd
import numpy as np

def add_risk_metrics(df):
    df['return'] = df['price'].pct_change() * 100
    
    mean = df['return'].mean()
    std = df['return'].std()
    
    df['z_score'] = (df['return'] - mean) / std
    df['is_anomaly'] = df['z_score'].abs() > 2
    df['volatility'] = df['return'].rolling(window=30).std()
    
    return df