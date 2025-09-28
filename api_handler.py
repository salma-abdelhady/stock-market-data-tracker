import requests
import pandas as pd

API_KEY = "TPEP2CTNHWRXD6BL"

# get the data
def get_stock_data(symbol, start, end):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    time_series = data["Time Series (Daily)"]
    
    # convert to dataframe
    df = pd.DataFrame.from_dict(time_series, orient= "index")
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    
    # filter by date range entered
    mask = (df.index >= start) & (df.index <= end)
    df = df.loc[mask]
    
    return df

       

