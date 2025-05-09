import os
import requests

from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from . utils import check_mortimer, check_cecil, check_gwendolyn

from dotenv import load_dotenv

load_dotenv('../.env')

os.environ['FINNHUB_API_KEY'] = os.getenv('FINNHUB_API_KEY')


@ensure_csrf_cookie

# Main index view
def index(request):
    # Check pawfolios performance
    performance_mortimer = check_mortimer()
    performance_cecil = check_cecil()
    performance_gwendolyn = check_gwendolyn()
    # Create named entries
    performances = [
        {'name': 'Mortimer', 'value': performance_mortimer},
        {'name': 'Cecil', 'value': performance_cecil},
        {'name': 'Gwendolyn', 'value': performance_gwendolyn}
    ]
    # Sort descending by performance
    performances_sorted = sorted(performances, key = lambda x: x['value'], reverse = True)
    # Set the highest performer as the current_entry
    current_entry = performances_sorted[0]['name']
    # Set up donations
    donations = range(17, 0, -1)
    # Render the template
    return render(request, 'index.html', {
        'performances': performances_sorted,
        'current_entry': current_entry,
        'donations': donations
    })

# Indices update view
def get_indices(request):
    api_key = os.getenv('FINNHUB_API_KEY')

    indices = {
        'dow': { 'symbol': 'DIA', 'name': 'DOW' },
        'sp500': { 'symbol': 'SPY', 'name': 'S&P 500' },
        'nasdaq': { 'symbol': 'QQQ', 'name': 'NASDAQ' },
        'dax': { 'symbol': 'DAX', 'name': 'DAX' },
        'ftse': { 'symbol': 'EWU', 'name': 'FTSE 100' },
        'nikkei': { 'symbol': 'EWJ', 'name': 'Nikkei 225' },
        'hangseng': { 'symbol': 'EWH', 'name': 'Hang Seng' },
        'msci_world': { 'symbol': 'URTH', 'name': 'MSCI World' },
    }

    results = {}

    for key, info in indices.items():
        symbol = info['symbol']
        name = info['name']
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            results[key] = {
                'name': name,
                'change': data.get('d', 0),
                'percent_change': data.get('dp', 0),
            }
        except Exception as e:
            results[key] = { 'error': str(e) }

    return JsonResponse(results)
