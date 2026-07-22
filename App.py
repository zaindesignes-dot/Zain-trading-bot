import ccxt
import pandas as pd
import ta

def analyze_crypto(symbol, timeframe='1h', limit=50):
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    df['rsi'] = ta.momentum.rsi(df['close'], window=14)
    df['ema_9'] = ta.trend.ema_indicator(df['close'], window=9)
    
    latest = df.iloc[-1]
    signal = "BUY" if latest['close'] > latest['ema_9'] else "SELL"
    
    print(f"Time: {latest['timestamp']}")
    print(f"Close Price: {latest['close']}")
    print(f"RSI: {latest['rsi']:.2f}")
    print(f"Signal: {signal}")

analyze_crypto('BTC/USDT')
