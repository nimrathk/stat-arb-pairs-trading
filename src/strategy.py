import pandas as pd

def calculate_zscore(spread, window=30):
    mean = spread.rolling(window=window).mean()
    std = spread.rolling(window=window).std()
    zscore = (spread - mean) / std
    return zscore

def generate_trade_signals(zscore, entry_threshold=2.0, exit_threshold=0.5):
    signals = pd.Series(index=zscore.index, dtype='object')
    position = None

    for i in range(len(zscore)):
        if position is None:
            if zscore[i] > entry_threshold:
                signals[i] = 'SHORT'
                position = 'SHORT'
            elif zscore[i] < -entry_threshold:
                signals[i] = 'LONG'
                position = 'LONG'
        elif position == 'LONG' and zscore[i] >= -exit_threshold:
            signals[i] = 'EXIT'
            position = None
        elif position == 'SHORT' and zscore[i] <= exit_threshold:
            signals[i] = 'EXIT'
            position = None

    return signals
