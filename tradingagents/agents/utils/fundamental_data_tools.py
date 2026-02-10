from langchain_core.tools import tool
from typing import Annotated
from tradingagents.dataflows.interface import route_to_vendor


@tool
def get_token_metrics(
    symbol: Annotated[str, "crypto symbol (e.g., BTCUSDT, ETHUSDT)"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """
    Retrieve token metrics for a given crypto symbol.
    Uses the configured fundamental_data vendor.
    Args:
        symbol (str): Crypto symbol, e.g. BTCUSDT, ETHUSDT
        curr_date (str): Current date you are trading at, yyyy-mm-dd
    Returns:
        str: A formatted report containing token metrics
    """
    return route_to_vendor("get_token_metrics", symbol, curr_date)


@tool
def get_fundamentals(
    ticker: Annotated[str, "ticker symbol"],
    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],
) -> str:
    """Backward-compatible wrapper for crypto token metrics."""
    return get_token_metrics(ticker, curr_date)