import pandas as pd
import numpy as np

def backtest_strategy(prices1, prices2, signals, initial_cash=10000):
    positions = pd.DataFrame(index=signals.index, columns=['position1', 'position2'], data=0.0)
    cash = initial_cash
    portfolio_value = []

    for i in range(1, len(signals)):
        signal = signals.iloc[i]
        p1 = prices1.iloc[i]
        p2 = prices2.iloc[i]

        if signal == 'LONG':
            positions.iloc[i] = [1, -1]
        elif signal == 'SHORT':
            positions.iloc[i] = [-1, 1]
        elif signal == 'EXIT':
            positions.iloc[i] = [0, 0]
        else:
            positions.iloc[i] = positions.iloc[i - 1]

        value = cash + (positions.iloc[i, 0] * p1 + positions.iloc[i, 1] * p2)
        portfolio_value.append(value)

    returns = pd.Series(portfolio_value).pct_change().dropna()
    sharpe_ratio = (returns.mean() / returns.std()) * np.sqrt(252)
    cumulative_return = portfolio_value[-1] / initial_cash - 1

    return {
        'final_value': portfolio_value[-1],
        'cumulative_return': cumulative_return,
        'sharpe_ratio': sharpe_ratio
    }