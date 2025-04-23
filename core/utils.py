import os
import requests

from dotenv import load_dotenv

load_dotenv('../.env')

os.environ['MORTIMER_SYMBOLS'] = os.getenv('MORTIMER_SYMBOLS')
os.environ['MORTIMER_SHARES'] = os.getenv('MORTIMER_SHARES')
os.environ['MORTIMER_PRICES'] = os.getenv('MORTIMER_PRICES')
os.environ['FINNHUB_API_KEY'] = os.getenv('FINNHUB_API_KEY')

FINNHUB_API_KEY = os.environ['FINNHUB_API_KEY']

# Extract portfolio symbols, shares, prices
SYMBOLS = os.environ['MORTIMER_SYMBOLS'].split()
SHARES = os.environ['MORTIMER_SHARES'].split()
PRICES = os.environ['MORTIMER_PRICES'].split()


# Get stock prices from api
def get_prices(symbol):
    quote = requests.get('https://finnhub.io/api/v1/quote', params = {'symbol': symbol, 'token': FINNHUB_API_KEY}).json()
    return quote.get('c')

# Check Mortimer pawfolio
def check_mortimer():
    # Calculate invest_start
    invest_start = sum([int(share) * float(price) for share, price in zip(SHARES, PRICES)])
    # Calculate invest_current
    prices_current = [get_prices(symbol) for symbol in SYMBOLS]
    invest_current = sum([int(share) * price for share, price in zip(SHARES, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return performance
