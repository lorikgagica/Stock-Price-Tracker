# 📈 Stock Price Tracker (Python CLI Tool)

A command-line Python application for tracking live stock prices. Fetches the latest prices from Yahoo Finance, logs them to a CSV, watches for sudden changes, keeps a history, and lets you plot recent trends — all in one script!

---

## ✨ Features

- **Track real-time prices** for any stock symbol (e.g., AAPL, TSLA, NVDA)
- **Log prices to CSV** for analysis or future use
- **Alert when price changes** by a chosen threshold (e.g., ±$1)
- **View the last N prices** after each fetch, for quick review
- **Plot price history** with a simple command — see trends instantly
- **Configurable:** Choose update interval, price-move alert threshold, N for saved price history

---

## 🚀 How to Run

1. **Install Python** (requires Python 3)
2. **Install dependencies:**
    ```
    pip install requests beautifulsoup4 matplotlib
    ```
3. **Save as `stock.py`**
4. **Run the script from terminal:**
    ```
    python stock.py
    ```
5. **Follow the prompts:**  
   - Enter ticker (e.g. `AAPL`, `TSLA`)
   - Set update interval in seconds (e.g. `60`)
   - Optionally set history length and alert threshold
   - Type `"plot"` when prompted to show a chart!

---

## 🧑‍💻 Usage Example

Welcome to the Stock Price Tracker!
Enter the stock ticker symbol (e.g., AAPL, TSLA): NVDA
Enter the update interval (in seconds): 30
How many recent prices do you want to keep for review/plot (default 10)? 10
Price move alert threshold (default $1): 2
Tracking stock prices for NVDA every 30 seconds...

NVDA: $438.56 at 2025-11-04 10:10:10
Recent prices:
2025-11-04 10:10:10 - $438.56
Type 'plot' to visualize recent prices, or Enter to continue:

Alert: Price went up by $2.15 since last check!

---

## 🗂️ How It Works

- **Requests Yahoo Finance** for each ticker and parses price using BeautifulSoup
- **Logs each price and timestamp** to `prices.csv` for data retention
- **For each fetch:** Shows price and time, alerts on threshold moves, presents history
- **Lets you plot trend** (matplotlib) interactively via keyboard

---

## 📄 License

MIT License — free for learning, teaching, and tinkering.

---

A simple Python starter for investors, analysts, and anyone wanting quick stock price visibility from the terminal!
