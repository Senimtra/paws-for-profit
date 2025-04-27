import os
import requests

from dotenv import load_dotenv

load_dotenv('../.env')

os.environ['FINNHUB_API_KEY'] = os.getenv('FINNHUB_API_KEY')

os.environ['MORTIMER_SYMBOLS'] = os.getenv('MORTIMER_SYMBOLS')
os.environ['MORTIMER_SHARES'] = os.getenv('MORTIMER_SHARES')
os.environ['MORTIMER_PRICES'] = os.getenv('MORTIMER_PRICES')

os.environ['CECIL_SYMBOLS'] = os.getenv('CECIL_SYMBOLS')
os.environ['CECIL_SHARES'] = os.getenv('CECIL_SHARES')
os.environ['CECIL_PRICES'] = os.getenv('CECIL_PRICES')

FINNHUB_API_KEY = os.environ['FINNHUB_API_KEY']

# Extract Mortimer portfolio symbols, shares, prices
SYMBOLS_MORTIMER = os.environ['MORTIMER_SYMBOLS'].split()
SHARES_MORTIMER = os.environ['MORTIMER_SHARES'].split()
PRICES_MORTIMER = os.environ['MORTIMER_PRICES'].split()

# Extract Cecil portfolio symbols, shares, prices
SYMBOLS_CECIL = os.environ['CECIL_SYMBOLS'].split()
SHARES_CECIL = os.environ['CECIL_SHARES'].split()
PRICES_CECIL = os.environ['CECIL_PRICES'].split()


# Get stock prices from api
def get_prices(symbol):
    quote = requests.get('https://finnhub.io/api/v1/quote', params = {'symbol': symbol, 'token': FINNHUB_API_KEY}).json()
    return quote.get('c')

# Check Mortimer pawfolio
def check_mortimer():
    # Calculate invest_start
    invest_start = sum([int(share) * float(price) for share, price in zip(SHARES_MORTIMER, PRICES_MORTIMER)])
    # Calculate invest_current
    prices_current = [get_prices(symbol) for symbol in SYMBOLS_MORTIMER]
    invest_current = sum([int(share) * price for share, price in zip(SHARES_MORTIMER, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return ('Mortimer', performance)

# Check Cecil pawfolio
def check_cecil():
    # Calculate invest_start
    invest_start = sum([int(share) * float(price) for share, price in zip(SHARES_CECIL, PRICES_CECIL)])
    # Calculate invest_current
    prices_current = [get_prices(symbol) for symbol in SYMBOLS_CECIL]
    invest_current = sum([int(share) * price for share, price in zip(SHARES_CECIL, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return ('Cecil', performance)
