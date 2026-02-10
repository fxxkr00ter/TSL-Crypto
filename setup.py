"""
Setup script for the TSL-Crypto package.
"""

from setuptools import setup, find_packages

setup(
    name="tsl-crypto",
    version="0.1.0",
    description="TSL-Crypto: Multi-Agent LLM Crypto Trading Framework",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="TSL-Crypto Contributors",
    author_email="",
    url="https://github.com/fxxkr00ter/TSL-Crypto",
    packages=find_packages(),
    install_requires=[
        # LLM & Agent orchestration
        "langchain-openai>=0.3.0",
        "langchain-anthropic>=0.3.0",
        "langchain-google-genai>=2.1.0",
        "langchain-experimental>=0.3.0",
        "langgraph>=0.4.0",
        # Data & analysis
        "pandas>=2.0.0",
        "yfinance>=0.2.31",
        "python-binance>=1.0.19",
        "stockstats>=0.5.4",
        # Embeddings & memory
        "chromadb>=1.0.0",
        # News & social
        "feedparser>=6.0.0",
        "praw>=7.7.0",
        "requests>=2.31.0",
        # CLI
        "typer>=0.9.0",
        "rich>=13.0.0",
        "questionary>=2.0.1",
        # Utilities
        "python-dotenv>=1.0.0",
        "pytz>=2024.1",
        "tqdm>=4.65.0",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "tsl-crypto=cli.main:app",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
