import pandas as pd                     # This imports pandas for handling tabular data (DataFrames)
import numpy as np                      # This imports numpy for numerical operations and arrays
import yfinance as yf                   # This imports yfinance to download stock data from Yahoo Finance
import matplotlib.pyplot as plt         # This imports matplotlib for plotting stock charts
import pandas_ta as ta                  # This imports pandas_ta for technical indicators (like EMA, RSI)


# Download daily stock data for RELIANCE.NS between 01 Jan 2023 and 27 June 2024
data = yf.download("RELIANCE.NS", start="2023-01-01", end="2024-06-27", interval="1d", group_by='ticker')   # Fetch OHLCV data
