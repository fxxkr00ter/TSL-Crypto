<h1 align="center">TSL-Crypto</h1>

<p align="center">
  <strong>基于多智能体 LLM 的加密货币交易分析框架</strong>
</p>

<p align="center">
  <a href="#快速开始">快速开始</a> &nbsp;|&nbsp;
  <a href="#系统架构">系统架构</a> &nbsp;|&nbsp;
  <a href="#智能体角色">智能体角色</a> &nbsp;|&nbsp;
  <a href="#配置说明">配置说明</a> &nbsp;|&nbsp;
  <a href="#支持的-llm-提供商">LLM 提供商</a>
</p>

<p align="center">
  <img alt="Python 3.10+" src="https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white">
  <img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green">
  <img alt="LangGraph" src="https://img.shields.io/badge/LangGraph-powered-orange">
  <img alt="xAI Grok" src="https://img.shields.io/badge/xAI-Grok-black">
  <img alt="Binance" src="https://img.shields.io/badge/Binance-data-F0B90B?logo=binance&logoColor=white">
</p>

---

**TSL-Crypto**（Trading Signal Lights）是一个开源的多智能体框架，模拟专业加密货币交易机构的运作方式。它部署了多个 LLM 驱动的专业智能体 —— 技术分析师、情绪分析师、新闻研究员、代币指标分析师、多空研究员、交易员以及风控管理团队 —— 通过结构化辩论与协作分析，最终生成 **BUY（买入）/ HOLD（持有）/ SELL（卖出）** 信号。

基于 **LangGraph** 进行智能体编排，**xAI Grok** 提供推理能力，**Binance** 提供实时市场数据。

> **免责声明**：本框架仅用于**研究和教育目的**。交易表现因人而异，不构成任何金融、投资或交易建议。

---

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/fxxkr00ter/TSL-Crypto.git
cd TSL-Crypto

# 2. 创建虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置 API 密钥
cp .env.example .env
# 编辑 .env 文件，填入你的 XAI_API_KEY、BINANCE_API_KEY、BINANCE_SECRET_KEY

# 5. 启动交互式 CLI
python -m cli.main
```

<details>
<summary><strong>API 密钥说明</strong></summary>

| 密钥 | 是否必需 | 说明 |
|------|---------|------|
| `XAI_API_KEY` | **必需** | xAI API 密钥，用于调用 Grok 模型 |
| `BINANCE_API_KEY` | **必需** | 币安 API 密钥 |
| `BINANCE_SECRET_KEY` | **必需** | 币安 API 私钥 |
| `OPENAI_API_KEY` | 可选 | 用于新闻搜索和 Embeddings 的备选方案 |
| `ALPHA_VANTAGE_API_KEY` | 可选 | 备选新闻与指标数据源 |

</details>

---

## 系统架构

```
                        ┌─────────────────────────────────┐
                        │          分析师团队               │
                        │  市场 ─ 情绪 ─ 新闻 ─ 代币指标    │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │          研究辩论                 │
                        │      多头  ◄──►  空头             │
                        │         (N 轮辩论)               │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │         研究经理                  │
                        │   (深度思考 LLM 裁判)             │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │          交易员                   │
                        │     (生成交易计划)                 │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │        风控管理辩论                │
                        │   激进型 ─ 保守型 ─ 中性型         │
                        │         (N 轮辩论)               │
                        └──────────────┬──────────────────┘
                                       │
                        ┌──────────────▼──────────────────┐
                        │     风控裁判 / 投资组合经理         │
                        │  (最终 BUY / HOLD / SELL 决策)    │
                        └─────────────────────────────────┘
```

---

## 智能体角色

### 分析师团队（数据采集与报告生成）

| 智能体 | 职责说明 | 数据来源 |
|--------|---------|---------|
| **市场分析师** | 技术分析：自主选择最多 8 种指标（SMA、EMA、MACD、RSI、布林带、ATR、VWMA、MFI），生成详细趋势报告 | Binance OHLCV + stockstats |
| **情绪分析师** | 社交媒体与社区情绪分析 | Google News |
| **新闻分析师** | 宏观经济与加密市场新闻分析 | Google News |
| **代币指标分析师** | 交易所级别基本面：成交量、流动性、价格变化、交易笔数 | Binance 24h Ticker |

### 研究团队（结构化辩论）

| 智能体 | 职责说明 |
|--------|---------|
| **多头研究员** | 构建基于证据的看涨论点；反驳空头观点 |
| **空头研究员** | 构建基于证据的看跌论点；反驳多头观点 |
| **研究经理** | 裁判辩论结果；生成投资计划（使用深度思考 LLM） |

### 交易团队

| 智能体 | 职责说明 |
|--------|---------|
| **交易员** | 综合研究成果，生成包含 BUY/HOLD/SELL 建议的交易计划 |

### 风控管理团队（结构化辩论）

| 智能体 | 职责说明 |
|--------|---------|
| **激进型分析师** | 主张更高风险、更高收益的策略 |
| **保守型分析师** | 主张资本保全、低风险的策略 |
| **中性型分析师** | 在风险与收益之间寻求平衡 |
| **风控裁判** | 最终决策者；输出最终的 BUY/HOLD/SELL 信号（使用深度思考 LLM） |

### 记忆系统

所有研究员、交易员和管理者均使用 **ChromaDB 向量记忆** 存储和回忆过去的市场情境与经验教训，实现跨会话的持续学习与改进。

---

## 执行流程

1. **分析师阶段** — 分析师按顺序运行，每个分析师具备工具调用能力（由 LLM 自主决定调用哪些工具）。分析结果存入共享的 `AgentState`。
2. **研究辩论** — 多头研究员与空头研究员进行 `max_debate_rounds` 轮辩论。
3. **研究经理** — 深度思考 LLM 裁判辩论结果，生成投资计划。
4. **交易员** — 基于所有报告和投资计划，生成交易方案。
5. **风控辩论** — 激进型、保守型、中性型分析师进行 `max_risk_discuss_rounds` 轮辩论。
6. **风控裁判** — 深度思考 LLM 做出最终 BUY/HOLD/SELL 决策。

---

## 技术栈

| 组件 | 技术方案 |
|------|---------|
| 智能体编排 | [LangGraph](https://github.com/langchain-ai/langgraph)（StateGraph、ToolNode、条件边） |
| LLM 提供商（默认） | [xAI Grok](https://docs.x.ai)（`grok-4-fast-reasoning`、`grok-4-fast-non-reasoning`） |
| LLM 备选方案 | OpenAI、Anthropic、Google Gemini、OpenRouter、Ollama |
| 市场数据 | [Binance API](https://binance-docs.github.io/apidocs/)（python-binance） |
| 技术指标 | [stockstats](https://github.com/jealous/stockstats) |
| 新闻数据 | Google News、OpenAI Web Search、Alpha Vantage |
| 智能体记忆 | [ChromaDB](https://www.trychroma.com/) + OpenAI Embeddings |
| 命令行界面 | [Typer](https://typer.tiangolo.com/) + [Rich](https://rich.readthedocs.io/) + [Questionary](https://questionary.readthedocs.io/) |

---

## 使用方法

### 命令行交互模式

```bash
python -m cli.main
```

CLI 将引导你完成以下步骤：
1. 输入加密货币交易对（如 `BTCUSDT`）
2. 选择分析日期
3. 选择启用的分析师团队
4. 选择研究深度（1 / 3 / 5 轮辩论）
5. 选择 LLM 提供商和模型

Rich 实时仪表板将展示所有智能体的运行进度。


### Python 编程调用

```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from dotenv import load_dotenv

load_dotenv()

config = DEFAULT_CONFIG.copy()
ta = TradingAgentsGraph(debug=True, config=config)

# 分析 BTC/USDT
final_state, decision = ta.propagate("BTCUSDT", "2026-02-07")
print(decision)  # BUY、HOLD 或 SELL

# 访问各智能体的独立报告
print(final_state["market_report"])          # 市场分析报告
print(final_state["sentiment_report"])       # 情绪分析报告
print(final_state["news_report"])            # 新闻分析报告
print(final_state["fundamentals_report"])    # 代币指标报告
print(final_state["investment_plan"])        # 投资计划
print(final_state["trader_investment_plan"]) # 交易计划
print(final_state["final_trade_decision"])   # 最终交易决策
```

### 复盘学习（可选）

在观察到实际收益/亏损后，可将结果反馈至系统以更新智能体记忆：

```python
ta.reflect_and_remember(returns_losses=1000)
```

---

## 配置说明

所有默认配置位于 `tradingagents/default_config.py`：

```python
DEFAULT_CONFIG = {
    # LLM 设置
    "llm_provider": "xai",
    "deep_think_llm": "grok-4-fast-reasoning",
    "quick_think_llm": "grok-4-fast-non-reasoning",
    "backend_url": "https://api.x.ai/v1",

    # 辩论轮次
    "max_debate_rounds": 1,        # 多空研究辩论轮次
    "max_risk_discuss_rounds": 1,  # 风控团队辩论轮次

    # 数据供应商
    "data_vendors": {
        "core_crypto_apis": "binance",       # 核心加密货币数据
        "technical_indicators": "binance",   # 技术指标数据
        "fundamental_data": "binance",       # 基本面数据
        "news_data": "google",               # 新闻数据
    },
}
```

可在运行时覆盖任意配置项：

```python
config = DEFAULT_CONFIG.copy()
config["max_debate_rounds"] = 3                    # 增加辩论轮次
config["data_vendors"]["news_data"] = "openai"     # 切换新闻源
config["llm_provider"] = "openai"                  # 切换为 OpenAI
config["deep_think_llm"] = "o4-mini"
config["quick_think_llm"] = "gpt-4o-mini"
```

---

## 项目结构

```
TSL-Crypto/
├── main.py                          # 程序入口示例
├── cli/
│   ├── main.py                      # CLI 应用（Typer + Rich）
│   ├── models.py                    # AnalystType 枚举
│   ├── utils.py                     # 用户输入辅助函数
│   └── static/welcome.txt           # ASCII 欢迎界面
├── tradingagents/
│   ├── default_config.py            # 默认配置
│   ├── agents/
│   │   ├── analysts/
│   │   │   ├── market_analyst.py    # 市场技术分析师
│   │   │   ├── fundamentals_analyst.py  # 代币指标分析师
│   │   │   ├── news_analyst.py      # 新闻分析师
│   │   │   └── social_media_analyst.py  # 情绪分析师
│   │   ├── researchers/
│   │   │   ├── bull_researcher.py   # 多头研究员
│   │   │   └── bear_researcher.py   # 空头研究员
│   │   ├── trader/
│   │   │   └── trader.py            # 交易员
│   │   ├── risk_mgmt/
│   │   │   ├── aggresive_debator.py # 激进型风控分析师
│   │   │   ├── conservative_debator.py  # 保守型风控分析师
│   │   │   └── neutral_debator.py   # 中性型风控分析师
│   │   ├── managers/
│   │   │   ├── research_manager.py  # 研究经理（辩论裁判）
│   │   │   └── risk_manager.py      # 风控裁判（最终决策）
│   │   └── utils/
│   │       ├── agent_states.py      # 状态定义（AgentState 等）
│   │       ├── agent_utils.py       # 工具导入与工具函数
│   │       ├── core_stock_tools.py  # get_crypto_data 工具
│   │       ├── technical_indicators_tools.py  # get_indicators 工具
│   │       ├── fundamental_data_tools.py      # get_token_metrics 工具
│   │       ├── news_data_tools.py   # get_news、get_global_news 工具
│   │       └── memory.py            # ChromaDB 向量记忆
│   ├── graph/
│   │   ├── trading_graph.py         # 主编排器
│   │   ├── setup.py                 # LangGraph 图构建
│   │   ├── propagation.py           # 状态初始化与传播
│   │   ├── conditional_logic.py     # 流程控制（条件路由）
│   │   ├── signal_processing.py     # BUY/SELL/HOLD 信号提取
│   │   └── reflection.py            # 交易后复盘学习
│   └── dataflows/
│       ├── interface.py             # 数据供应商路由（核心）
│       ├── config.py                # 运行时配置
│       ├── binance.py               # Binance OHLCV 与代币指标
│       ├── google.py                # Google News 新闻数据
│       ├── openai.py                # OpenAI Web Search
│       ├── y_finance.py             # yfinance / stockstats 技术指标
│       ├── alpha_vantage*.py        # Alpha Vantage 系列 API
│       └── local.py                 # Finnhub、Reddit、本地数据
├── reports/                         # 生成的分析报告
├── requirements.txt                 # Python 依赖
├── pyproject.toml                   # 项目元数据
├── setup.py                         # 包安装配置
├── .env.example                     # 环境变量模板
└── LICENSE                          # MIT 开源协议
```

---

## 支持的 LLM 提供商

| 提供商 | 配置值 | 模型示例 |
|--------|-------|---------|
| xAI | `"xai"` | `grok-4-fast-reasoning`、`grok-4-fast-non-reasoning` |
| OpenAI | `"openai"` | `gpt-4o`、`gpt-4o-mini`、`o4-mini` |
| Anthropic | `"anthropic"` | `claude-sonnet-4-0`、`claude-3-5-haiku-latest` |
| Google | `"google"` | `gemini-2.5-flash-preview-05-20` |
| OpenRouter | `"openrouter"` | `meta-llama/llama-4-scout:free` |
| Ollama | `"ollama"` | `llama3.1`、`qwen3` |

---

## 参与贡献

欢迎任何形式的贡献！无论是修复 Bug、改进文档、添加新的数据源，还是提出功能建议 —— 请随时提交 Issue 或 Pull Request。

1. Fork 本仓库
2. 创建功能分支（`git checkout -b feature/your-feature`）
3. 提交更改（`git commit -m 'Add some feature'`）
4. 推送到分支（`git push origin feature/your-feature`）
5. 创建 Pull Request

---

## 开源协议

本项目基于 [MIT 协议](LICENSE) 开源。
