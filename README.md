# 📈 Crypto Price Tracker (Multi-Exchange)

A lightweight Python project that tracks real-time cryptocurrency prices across multiple exchanges using the **CCXT** library.  
This tool fetches and displays the latest market prices of a given trading pair (e.g., `BTC/USDT`) from multiple exchanges at regular intervals.

---

## 🚀 Features

- 🔗 Track prices from **multiple crypto exchanges**
- ⚡ Fetch **live ticker data** using CCXT
- 🛡️ Graceful error handling for unsupported symbols or exchange downtime
- 🧩 Clean, modular, and extensible Python code
- ⏱️ Configurable polling interval
- 📊 Ready for extension using **Pandas** for logging or analysis

---

## 🏦 Supported Exchanges

- Binance  
- Coinbase  
- Kraken  

> Any exchange supported by CCXT can be easily added.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **CCXT** – Cryptocurrency exchange API library
- **Pandas** – Data handling & future analytics support

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git https://github.com/PranavVetkar/Multi-Exchange-Price-Tracker.git
cd Multi-Exchange-Price-Tracker
