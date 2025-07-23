import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import itertools

def engle_granger_test(y, x):
    model = sm.OLS(y, sm.add_constant(x)).fit()
    residuals = model.resid
    adf_result = adfuller(residuals)
    return adf_result[1]  # p-value

def find_cointegrated_pairs(data, significance=0.05):
    n = data.shape[1]
    pvalues = pd.DataFrame(np.ones((n, n)), columns=data.columns, index=data.columns)
    coint_pairs = []

    for i, j in itertools.combinations(range(n), 2):
        y = data.iloc[:, i]
        x = data.iloc[:, j]
        pvalue = engle_granger_test(y, x)
        pvalues.iloc[i, j] = pvalue
        if pvalue < significance:
            coint_pairs.append((data.columns[i], data.columns[j], pvalue))

    return coint_pairs, pvalues

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    # Load price data
    data = pd.read_csv('../data/sample_prices.csv', index_col=0, parse_dates=True)

    # Drop columns with missing data
    data = data.dropna(axis=1)

    # Find cointegrated pairs
    pairs, pvals = find_cointegrated_pairs(data)

    print("Cointegrated pairs found:")
    for pair in sorted(pairs, key=lambda x: x[2]):
        print(f"{pair[0]} & {pair[1]} | p-value: {pair[2]:.4f}")