import numpy as np
import pandas as pd

# Calculate daily returns
def calculate_returns(df, column='4. close'):
    """
    daily percentage change of specified column
    (today - yesterday) / yesterday 
    """
    return df[column].pct_change()

# Calculate moving avearge
def calculate_moving_aveage(df, column = '4. close', window = 20):
    return df[column].rolling(window = window).mean()

# calculate volatility
def calculate_volatility(df, column = '4. close', window = 20):
    """
    Volatility is typically the standard deviation of returns
    """
    returns = calculate_returns(df, column)
    return returns.rolling(window = window).std()