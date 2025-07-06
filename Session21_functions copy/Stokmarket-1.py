import pandas as pd                     # This imports pandas for handling tabular data (DataFrames)
import numpy as np                      # This imports numpy for numerical operations and arrays
import yfinance as yf                   # This imports yfinance to download stock data from Yahoo Finance
import matplotlib.pyplot as plt         # This imports matplotlib for plotting stock charts
import pandas_ta as ta                  # This imports pandas_ta for technical indicators (like EMA, RSI)

# Download daily stock data for RELIANCE.NS between 01 Jan 2023 and 27 June 2024
data = yf.download("RELIANCE.NS", start="2023-01-01", end="2024-06-27", interval="1d", group_by='ticker')   # Fetch OHLCV data

# If data has multi-level column names (MultiIndex), flatten it by dropping the top level
if isinstance(data.columns, pd.MultiIndex):                                                                 # Check if columns have multiple levels (e.g., ('Close', 'RELIANCE.NS'))
    data.columns = data.columns.droplevel(0)  # Remove the top level to keep just 'Open', 'High', 'Low', etc.

# Calculate 20-day Exponential Moving Average (EMA) on Close price and add to DataFrame
data.ta.ema(length=20, append=True)                                                                         # Appends a new column 'EMA_20' with 20-day EMA

# Calculate 14-day Relative Strength Index (RSI) and add to DataFrame
data.ta.rsi(length=14, append=True)                                                                         # Appends a new column 'RSI_14' with 14-day RSI values

# Plot the Close price and EMA line on a chart
plt.figure(figsize=(12, 6))                                                                                 # Set chart size to 12x6 inches
plt.plot(data["Close"], label="Close Price")                                                                # Plot the closing price
plt.plot(data["EMA_20"], label="EMA 20", linestyle='--')                                                    # Plot 20-day EMA with dashed line
plt.title("RELIANCE - Close & EMA 20")                                                                      # Set the chart title
plt.legend()                                                                                                # Display legend (labels)
plt.grid(True)                                                                                              # Show grid lines
plt.show()  # Display the plot window

# Print the last 5 rows of Close, EMA, and RSI values to the console
# print(data[["Close", "EMA_20", "RSI_14"]].tail(20))  # Show recent values for analysis/debugging
last_30_rows = data[["Close", "EMA_20", "RSI_14"]].tail(30)
print(last_30_rows)
