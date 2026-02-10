from typing import Annotated, Optional
from datetime import datetime
import os
import pandas as pd
from binance.client import Client


def _get_binance_client() -> Client:
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_SECRET_KEY")
    return Client(api_key, api_secret)


def get_binance_klines_df(
    symbol: Annotated[str, "crypto symbol (e.g., BTCUSDT, ETHUSDT)"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
    interval: Optional[str] = None,
) -> pd.DataFrame:
    client = _get_binance_client()
    interval = interval or Client.KLINE_INTERVAL_1DAY

    start_ts = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp() * 1000)
    end_ts = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp() * 1000)

    klines = client.get_historical_klines(
        symbol.upper(), interval, start_ts, end_ts
    )

    if not klines:
        return pd.DataFrame()

    columns = [
        "open_time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_volume",
        "number_of_trades",
        "taker_buy_base_asset_volume",
        "taker_buy_quote_asset_volume",
        "ignore",
    ]
    df = pd.DataFrame(klines, columns=columns)
    df["Date"] = pd.to_datetime(df["open_time"], unit="ms")
    df = df[["Date", "open", "high", "low", "close", "volume"]]
    df.rename(
        columns={
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume",
        },
        inplace=True,
    )
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")
    for col in ["Open", "High", "Low", "Close", "Volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def get_binance_crypto_data(
    symbol: Annotated[str, "crypto symbol (e.g., BTCUSDT, ETHUSDT)"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
) -> str:
    """Retrieve crypto OHLCV data from Binance."""
    datetime.strptime(start_date, "%Y-%m-%d")
    datetime.strptime(end_date, "%Y-%m-%d")

    data = get_binance_klines_df(symbol, start_date, end_date)
    if data.empty:
        return (
            f"No data found for symbol '{symbol}' between {start_date} and {end_date}"
        )

    csv_string = data.to_csv(index=False)
    header = f"# Crypto data for {symbol.upper()} from {start_date} to {end_date}\n"
    header += f"# Total records: {len(data)}\n"
    header += f"# Data retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    return header + csv_string


def get_binance_token_metrics(
    symbol: Annotated[str, "crypto symbol (e.g., BTCUSDT, ETHUSDT)"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """Get token metrics from Binance (24h stats, liquidity, volume)."""
    datetime.strptime(curr_date, "%Y-%m-%d")
    client = _get_binance_client()
    symbol = symbol.upper()

    try:
        stats = client.get_ticker(symbol=symbol)
    except Exception as exc:
        return f"Error retrieving Binance metrics for {symbol}: {exc}"

    metrics = [
        f"Symbol: {stats.get('symbol')}",
        f"Last Price: {stats.get('lastPrice')}",
        f"24h Change (%): {stats.get('priceChangePercent')}",
        f"24h High: {stats.get('highPrice')}",
        f"24h Low: {stats.get('lowPrice')}",
        f"24h Base Volume: {stats.get('volume')}",
        f"24h Quote Volume: {stats.get('quoteVolume')}",
        f"Trade Count: {stats.get('count')}",
    ]

    header = f"# Token metrics for {symbol} as of {curr_date}\n"
    header += f"# Data retrieved on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    return header + "\n".join(metrics)
