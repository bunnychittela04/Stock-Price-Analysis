import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV file using full path
df = pd.read_csv("C:/Users/AMARA/OneDrive/Desktop/Stock Price Analysis/stock-price-analysis/AAPL.csv")

# Select Date and Close columns
df = df[['Date', 'Close']]
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')  # Fix: specify correct format
df.set_index('Date', inplace=True)  # Set Date as index

# Calculate 10-day moving average and daily return
df['Moving_Avg_10'] = df['Close'].rolling(window=10).mean()
df['Daily_Return'] = df['Close'].pct_change()

# Plot Close Price and Moving Average
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close Price')
plt.plot(df['Moving_Avg_10'], label='10-Day Moving Average', linestyle='--')
plt.title("Stock Price & 10-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()

# Plot Daily Returns
plt.figure(figsize=(12,6))
plt.plot(df['Daily_Return'], color='orange', label='Daily Return')
plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return (%)")
plt.grid(True)
plt.legend()
plt.show()
