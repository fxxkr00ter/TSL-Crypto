import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    "data_dir": os.getenv("TRADINGAGENTS_DATA_DIR", "./data"),
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    "llm_provider": "xai",
    "deep_think_llm": "grok-4-fast-reasoning",
    "quick_think_llm": "grok-4-fast-non-reasoning",
    "backend_url": "https://api.x.ai/v1",
    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Data vendor configuration
    # Category-level configuration (default for all tools in category)
    "data_vendors": {
        "core_crypto_apis": "binance",       # Options: binance
        "technical_indicators": "binance",   # Options: binance, alpha_vantage, local
        "fundamental_data": "binance",       # Options: binance, openai
        "news_data": "google",               # Options: openai, alpha_vantage, google, local
    },
    # Tool-level configuration (takes precedence over category-level)
    "tool_vendors": {
        # Example: "get_crypto_data": "binance",  # Override category default
        # Example: "get_news": "openai",               # Override category default
    },
}
