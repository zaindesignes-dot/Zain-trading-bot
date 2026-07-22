import ccxt
import pandas as pd
import ta
import streamlit as st

st.title("Trading Bot Dashboard")

def fetch_data():
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', '1h', limit=50)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['ema_9'] = ta.trend.ema_indicator(df['close'], window=9)
    return df

data = fetch_data()
latest = data.iloc[-1]
signal = "BUY" if latest['close'] > latest['ema_9'] else "SELL"

st.write(f"Time: {latest['timestamp']}")
st.write(f"Close Price: {latest['close']}")
st.write(f"RSI: {latest['rsi']:.2f}")
st.write(f"Signal: {signal}")
