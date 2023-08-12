# Netflix Stock Price Trend Analysis Project
### Author github.com/tushar2704

# Fetching data from yfinance
"""

!pip install yfinance

import yfinance as yf

# Define the stock symbol (ticker)
stock_symbol = "NFLX"

# Fetch historical stock data using yfinance
netflix_stock = yf.Ticker(stock_symbol)

# Get historical stock prices
historical_data = netflix_stock.history(period="5y")

# Display the historical data
print(historical_data)

"""### Saving the 5y Netflix stock price"""

# Save the historical data to a CSV file
csv_filename = "netflix_stock_5y.csv"
historical_data.to_csv(csv_filename)

print(f"Data saved to {csv_filename}")