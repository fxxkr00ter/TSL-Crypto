"""
TSL-Crypto — Quick Start Example

Usage:
    1. Copy .env.example to .env and fill in your API keys.
    2. Run: python main.py
"""

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ── Create a custom config (optional) ────────────────────────────────────────
config = DEFAULT_CONFIG.copy()

# LLM settings (defaults to xAI Grok — change as needed)
# config["llm_provider"] = "xai"
# config["deep_think_llm"] = "grok-4-fast-reasoning"
# config["quick_think_llm"] = "grok-4-fast-non-reasoning"

# Debate rounds
# config["max_debate_rounds"] = 1        # Bull vs Bear debate rounds
# config["max_risk_discuss_rounds"] = 1  # Risk management debate rounds

# Data vendors
# config["data_vendors"] = {
#     "core_crypto_apis": "binance",        # Options: binance
#     "technical_indicators": "binance",    # Options: binance, alpha_vantage, local
#     "fundamental_data": "binance",        # Options: binance, openai
#     "news_data": "google",               # Options: openai, alpha_vantage, google, local
# }

# ── Initialize and run ───────────────────────────────────────────────────────
ta = TradingAgentsGraph(debug=True, config=config)

# Analyze BTC/USDT for a given date
final_state, decision = ta.propagate("BTCUSDT", "2026-02-07")
print(f"\nFinal Decision: {decision}")

# Access individual reports
# print(final_state["market_report"])
# print(final_state["sentiment_report"])
# print(final_state["news_report"])
# print(final_state["fundamentals_report"])
# print(final_state["investment_plan"])
# print(final_state["trader_investment_plan"])
# print(final_state["final_trade_decision"])

# ── Post-trade reflection (optional) ─────────────────────────────────────────
# After observing actual P&L, feed it back to improve agent memory:
# ta.reflect_and_remember(returns_losses=1000)
