import pandas as pd
import pandas_ta as ta
import aiohttp

class TAService:
    @staticmethod
    async def analyze_symbol(symbol: str = "BTCUSDT") -> str:
        url = f"https://api.binance.com/api/v3/klines?symbol={symbol.upper()}&interval=1h&limit=100"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return f"❌ Unable to fetch market data for `{symbol}`."
                data = await resp.json()

        df = pd.DataFrame(data, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_av", "trades", "tb_base_av", "tb_quote_av", "ignore"
        ])
        df["close"] = df["close"].astype(float)
        
        rsi = ta.rsi(df["close"], length=14)
        macd = ta.macd(df["close"])
        ema_20 = ta.ema(df["close"], length=20)
        sma_50 = ta.sma(df["close"], length=50)

        latest_price = df["close"].iloc[-1]
        latest_rsi = rsi.iloc[-1] if rsi is not None else 50.0
        
        rsi_status = "Overbought" if latest_rsi > 70 else ("Oversold" if latest_rsi < 30 else "Neutral")
        trend = "Bullish 📈" if latest_price > ema_20.iloc[-1] else "Bearish 📉"

        return (
            f"📊 **Technical Analysis: {symbol.upper()}**\n\n"
            f"💰 **Price:** `${latest_price:,.2f}`\n"
            f"📈 **Trend (EMA 20):** {trend}\n"
            f"🎯 **RSI (14):** `{latest_rsi:.2f}` ({rsi_status})\n"
            f"🔹 **SMA 50:** `${sma_50.iloc[-1]:,.2f}`\n\n"
            f"⚠️ *Analysis is for informational purposes only. Always manage risk.*"
        )
