📈 Stock Price Analysis using Python

This project performs a basic stock price analysis on Apple Inc. (AAPL) using historical data. It includes calculating moving averages and daily returns, and visualizing trends using Python libraries like pandas, numpy, and matplotlib.

📂 Project Structure:
Stock Price Analysis/
│
├── AAPL.csv                    
├── stock_analysis.py           
├── README.md                 
└── Output Charts/             
🛠️ Tools & Libraries Used
Python 

pandas

numpy

matplotlib

 -Features Implemented
 Read historical stock data from CSV

 Convert Date column to datetime

 Set Date as index for time series operations

 Calculate 10-day Moving Average

 Compute Daily Return (% change in closing price)

 Visualize:

Stock Price with 10-day Moving Average

Daily Returns over time

-Sample Input (AAPL.csv)
csv
Copy
Edit
Date,Open,High,Low,Close,Volume
2023-07-01,180.0,182.5,179.0,181.0,50000000
2023-07-02,181.0,183.0,180.0,182.5,48000000
2023-07-03,182.5,184.0,181.5,183.0,47000000
📤 Output Charts
- Closing Price with Moving Average

Shows the actual closing stock price vs. 10-day moving average.

Helps smooth out short-term fluctuations.
<img width="1200" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/41a45d65-e166-4fc0-adb2-edd28c3aa5ca" />


- Daily Returns

Visualizes the percentage change between consecutive closing prices.

Useful for measuring volatility or risk.
<img width="1200" height="600" alt="Figure_2" src="https://github.com/user-attachments/assets/c39e1043-e504-4493-bd33-b8fdb16ccdba" />


