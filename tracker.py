import ccxt
import time

class PriceTracker:
    def __init__(self, exchanges):
        self.exchange_instances = {ex: getattr(ccxt, ex)() for ex in exchanges}

    def fetch_prices(self, symbol):
        print(f"--- Fetching {symbol} Prices ---")
        for name, exchange in self.exchange_instances.items():
            try:
                ticker = exchange.fetch_ticker(symbol)
                last_price = ticker['last']
                print(f"{name.upper()}: ${last_price:,.2f}")
            except Exception as e:
                print(f"Could not fetch from {name}: {e}")

monitored_exchanges = ['binance', 'coinbase', 'kraken']
tracker = PriceTracker(monitored_exchanges)

for i in range(3):
    tracker.fetch_prices('BTC/USDT')
    time.sleep(10)