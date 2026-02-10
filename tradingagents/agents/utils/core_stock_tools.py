from langchain_core.tools import tool
from typing import Annotated
from tradingagents.dataflows.interface import route_to_vendor


@tool
def get_crypto_data(
    symbol: Annotated[str, "crypto symbol (e.g., BTCUSDT, ETHUSDT)"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
) -> str:
    """
    Retrieve crypto price data (OHLCV) for a given symbol.
    Uses the configured core_crypto_apis vendor.
    Args:
        symbol (str): Crypto symbol, e.g. BTCUSDT, ETHUSDT
        start_date (str): Start date in yyyy-mm-dd format
        end_date (str): End date in yyyy-mm-dd format
    Returns:
        str: A formatted dataframe containing the crypto price data for the specified symbol in the specified date range.
    """
    return route_to_vendor("get_crypto_data", symbol, start_date, end_date)


@tool
def get_stock_data(
    symbol: Annotated[str, "ticker symbol of the company"],
    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],
    end_date: Annotated[str, "End date in yyyy-mm-dd format"],
) -> str:
    """Backward-compatible wrapper for crypto data."""
    return get_crypto_data(symbol, start_date, end_date)
