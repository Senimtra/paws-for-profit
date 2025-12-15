import os

import yfinance as yf

from dotenv import load_dotenv


load_dotenv('../.env')

os.environ['FINNHUB_API_KEY'] = os.getenv('FINNHUB_API_KEY')

os.environ['MORTIMER_SYMBOLS'] = os.getenv('MORTIMER_SYMBOLS')
os.environ['MORTIMER_SHARES'] = os.getenv('MORTIMER_SHARES')
os.environ['MORTIMER_PRICES'] = os.getenv('MORTIMER_PRICES')

os.environ['CECIL_SYMBOLS'] = os.getenv('CECIL_SYMBOLS')
os.environ['CECIL_SHARES'] = os.getenv('CECIL_SHARES')
os.environ['CECIL_PRICES'] = os.getenv('CECIL_PRICES')

os.environ['GWENDOLYN_SYMBOLS'] = os.getenv('GWENDOLYN_SYMBOLS')
os.environ['GWENDOLYN_SHARES'] = os.getenv('GWENDOLYN_SHARES')
os.environ['GWENDOLYN_PRICES'] = os.getenv('GWENDOLYN_PRICES')

os.environ['AURELIA_SYMBOLS'] = os.getenv('AURELIA_SYMBOLS')
os.environ['AURELIA_SHARES'] = os.getenv('AURELIA_SHARES')
os.environ['AURELIA_PRICES'] = os.getenv('AURELIA_PRICES')

os.environ['TILDA_SYMBOLS'] = os.getenv('TILDA_SYMBOLS')
os.environ['TILDA_SHARES'] = os.getenv('TILDA_SHARES')
os.environ['TILDA_PRICES'] = os.getenv('TILDA_PRICES')


# Extract Mortimer portfolio symbols, shares, prices
SYMBOLS_MORTIMER = os.environ['MORTIMER_SYMBOLS'].split()
SHARES_MORTIMER = os.environ['MORTIMER_SHARES'].split()
PRICES_MORTIMER = os.environ['MORTIMER_PRICES'].split()

# Extract Cecil portfolio symbols, shares, prices
SYMBOLS_CECIL = os.environ['CECIL_SYMBOLS'].split()
SHARES_CECIL = os.environ['CECIL_SHARES'].split()
PRICES_CECIL = os.environ['CECIL_PRICES'].split()

# Extract Gwendolyn portfolio symbols, shares, prices
SYMBOLS_GWENDOLYN = os.environ['GWENDOLYN_SYMBOLS'].split()
SHARES_GWENDOLYN = os.environ['GWENDOLYN_SHARES'].split()
PRICES_GWENDOLYN = os.environ['GWENDOLYN_PRICES'].split()

# Extract Aurelia Goldwhisker portfolio symbols, shares, prices
SYMBOLS_AURELIA = os.environ['AURELIA_SYMBOLS'].split()
SHARES_AURELIA = os.environ['AURELIA_SHARES'].split()
PRICES_AURELIA = os.environ['AURELIA_PRICES'].split()

# Extract Tilda Coincroft portfolio symbols, shares, prices
SYMBOLS_TILDA = os.environ['TILDA_SYMBOLS'].split()
SHARES_TILDA = os.environ['TILDA_SHARES'].split()
PRICES_TILDA = os.environ['TILDA_PRICES'].split()


# Check today's stock mood
def check_stockMood():
    all_symbols = list(set(SYMBOLS_MORTIMER + SYMBOLS_CECIL + SYMBOLS_GWENDOLYN + SYMBOLS_AURELIA + SYMBOLS_TILDA))  # unique symbols
    up = down = flat = 0
    # Check symbols
    for symbol in all_symbols:
        try:
            # Get ticker info
            ticker = yf.Ticker(symbol)
            data = ticker.history(period = '2d')  # 2 days to ensure previous close
            if len(data) < 2:
                continue  # Not enough data
            prev_close = data['Close'].iloc[-2]
            last_price = data['Close'].iloc[-1]
            # Calculate price change
            change_pct = (last_price - prev_close) / prev_close * 100
            # Count up/down/flat
            if change_pct > 0.3: up += 1
            elif change_pct < -0.3: down += 1
            else: flat += 1
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            continue
    # Set up stock mood dict
    total = up + down + flat or 1
    return {
        'up': round(up / total * 100, 1),
        'down': round(down / total * 100, 1),
        'flat': round(flat / total * 100, 1)
    }

# Get stock prices for pawfolio calculations
def get_prices_yfinance(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period = '1d')
    return round(hist['Close'].iloc[-1], 2)

# Check Mortimer pawfolio
def check_mortimer():
    # Calculate invest_start
    invest_start = sum([float(share) * float(price) for share, price in zip(SHARES_MORTIMER, PRICES_MORTIMER)])
    # Calculate invest_current
    prices_current = [get_prices_yfinance(symbol) for symbol in SYMBOLS_MORTIMER]
    invest_current = sum([float(share) * price for share, price in zip(SHARES_MORTIMER, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return (performance, 'funded')

# Check Cecil pawfolio
def check_cecil():
    # Calculate invest_start
    invest_start = sum([float(share) * float(price) for share, price in zip(SHARES_CECIL, PRICES_CECIL)])
    # Calculate invest_current
    prices_current = [get_prices_yfinance(symbol) for symbol in SYMBOLS_CECIL]
    invest_current = sum([float(share) * price for share, price in zip(SHARES_CECIL, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    print(invest_start, prices_current, invest_current, performance)
    return (performance, 'simulated')

# Check Gwendolyn pawfolio
def check_gwendolyn():
    # Calculate invest_start
    invest_start = sum([float(share) * float(price) for share, price in zip(SHARES_GWENDOLYN, PRICES_GWENDOLYN)])
    # Calculate invest_current
    prices_current = [get_prices_yfinance(symbol) for symbol in SYMBOLS_GWENDOLYN]
    invest_current = sum([float(share) * price for share, price in zip(SHARES_GWENDOLYN, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return (performance, 'simulated')

# Check Aurelia Goldwhisker pawfolio
def check_aurelia_goldwhisker():
    # Calculate invest_start
    invest_start = sum([float(share) * float(price) for share, price in zip(SHARES_AURELIA, PRICES_AURELIA)])
    # Calculate invest_current
    prices_current = [get_prices_yfinance(symbol) for symbol in SYMBOLS_AURELIA]
    invest_current = sum([float(share) * price for share, price in zip(SHARES_AURELIA, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return (performance, 'simulated')

# Check Tilda Coincroft pawfolio
def check_tilda_coincroft():
    # Calculate invest_start
    invest_start = sum([float(share) * float(price) for share, price in zip(SHARES_TILDA, PRICES_TILDA)])
    # Calculate invest_current
    prices_current = [get_prices_yfinance(symbol) for symbol in SYMBOLS_TILDA]
    invest_current = sum([float(share) * price for share, price in zip(SHARES_TILDA, prices_current)])
    # Calculate performance
    performance = round(((invest_current * 100) / invest_start) - 100, 2)
    return (performance, 'simulated')
