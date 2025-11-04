import requests
from bs4 import BeautifulSoup
import time
import csv
from collections import deque
import matplotlib.pyplot as plt

def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page: {response.status_code}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    html = fetch_page(url)
    if not html:
        return None
    soup = parse_html(html)
    price_tag = soup.find("fin-streamer", {"data-symbol": ticker, "data-field": "regularMarketPrice"})
    if price_tag:
        try:
            return float(price_tag.text.replace(',', ''))
        except Exception as e:
            print("Could not parse price:", e)
            return None
    else:
        print("Stock price not found.")
        return None

def log_price(ticker, price):
    with open("prices.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([ticker, price, time.strftime("%Y-%m-%d %H:%M:%S")])

def plot_price_history(history, ticker):
    if len(history) < 2:
        print("Not enough data for plotting.")
        return
    timestamps = [row[2] for row in history]
    prices = [row[1] for row in history]
    plt.figure(figsize=(10,5))
    plt.plot(timestamps, prices, marker="o", linestyle='-')
    plt.xticks(rotation=45)
    plt.title(f"{ticker} Price History")
    plt.xlabel("Timestamp")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()

def track_stock_price(ticker, interval=60, n_history=10, alert_delta=1.0):
    last_price = None
    history = deque(maxlen=n_history)
    print(f"Tracking stock prices for {ticker} every {interval} seconds...")
    while True:
        price = get_stock_price(ticker)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        if price is not None:
            print(f"{ticker}: ${price} at {timestamp}")
            log_price(ticker, price)
            history.append((ticker, price, timestamp))
            if last_price is not None:
                diff = price - last_price
                if abs(diff) >= alert_delta:
                    direction = "up" if diff > 0 else "down"
                    print(f"Alert: Price went {direction} by ${abs(diff):.2f} since last check!")
            last_price = price
        else:
            print("Price fetch failed.")
        # Show last N prices
        print("Recent prices:")
        for row in list(history)[-n_history:]:
            print(f"{row[2]} - ${row[1]}")
        # Plot option
        plot_input = input("Type 'plot' to visualize recent prices, or Enter to continue: ").strip().lower()
        if plot_input == "plot":
            plot_price_history(list(history), ticker)
        time.sleep(interval)

def main():
    print("Welcome to the Stock Price Tracker!")
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, TSLA): ").upper()
    interval = int(input("Enter the update interval (in seconds): "))
    n_history = int(input("How many recent prices do you want to keep for review/plot (default 10)? ") or "10")
    alert_delta = float(input("Price move alert threshold (default $1): ") or "1")
    track_stock_price(ticker, interval, n_history, alert_delta)

if __name__ == "__main__":
    main()