# Statistical Arbitrage: Pairs Trading Strategy

This project implements a statistical arbitrage trading strategy using pairs trading. It identifies cointegrated equity pairs using the Engle-Granger test, monitors spread deviations via Z-score thresholds, and simulates long-short trades. The performance is evaluated using Sharpe ratio, drawdown analysis, and cumulative returns.

## Features
- Pull historical price data using Yahoo Finance
- Identify cointegrated pairs via Engle-Granger test
- Entry/exit logic based on Z-score thresholds
- Simulated portfolio PnL, Sharpe ratio, and trade logging
- Data visualization of trade signals and performance

## Technologies Used
- Python
- Pandas, NumPy, statsmodels
- yfinance, matplotlib, seaborn

## Folder Structure
- `data/`: stores symbol lists and raw CSVs
- `src/`: contains logic for data, strategy, and backtesting
- `notebooks/`: demo walkthroughs and visualization
- `plots/`: output plots from backtests

## Setup
```bash
pip install -r requirements.txt
```

## Author
Nimrath Khanuja
