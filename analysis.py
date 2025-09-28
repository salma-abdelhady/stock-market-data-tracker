from api_handler import get_stock_data
from analysis_metrics import calculate_returns, calculate_moving_aveage, calculate_volatility
import matplotlib.pyplot as plt
from datetime import datetime


symbol = input("Enter symbol: ").strip().upper()
start_str = input("Enter start date (YYYY-MM-DD): ").strip()
end_str = input("Enter end date (YYYY-MM-DD): ").strip()

# Check dates
try:
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.strptime(end_str, "%Y-%m-%d")
except ValueError:
    print("Error: Dates must be in YYYY-MM-DD format.")
    exit()

if start > end:
    print("Error: Start date must be before end date.")
    exit()

if (end - start).days > 90:
    print("Error: Date range cannot exceed 90 days (API limit).")
    exit()

# Fetch data
df = get_stock_data(symbol, start, end)

if df.empty:
    print(f"No data found for {symbol} in the given date range.")
    exit()

# Analysis 
df['Daily return'] = calculate_returns(df)
df['MA_5'] = calculate_moving_aveage(df, window=5)
df['MA_20'] = calculate_moving_aveage(df)
df['Volatility'] = calculate_volatility(df)

# Visualization 
fig, ax = plt.subplots()
ax.plot(df.index, df['4. close'], label='Close Price')
ax.plot(df.index, df['MA_5'], label='5-day MA')
ax.plot(df.index, df['MA_20'], label='20-day MA')
ax.set_title(f'{symbol} Close Price & Moving Averages')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
