from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .utils import check_mortimer, check_cecil, check_gwendolyn, check_stockMood


@ensure_csrf_cookie

# Main index view
def index(request):
    # Check pawfolios performance/status
    performance_mortimer, status_mortimer = check_mortimer()
    performance_cecil, status_cecil = check_cecil()
    performance_gwendolyn, status_gwendolyn = check_gwendolyn()
    # Pawfolio checks
    pawfolios = [
        {'name': 'Mortimer', 'perf_value': performance_mortimer,'status': status_mortimer},
        {'name': 'Cecil', 'perf_value': performance_cecil,'status': status_cecil},
        {'name': 'Gwendolyn', 'perf_value': performance_gwendolyn,'status': status_gwendolyn},
        {'name': 'Aunt Elinor', 'perf_value': 0,'status': 'simulated'},
        {'name': 'Aurelia Goldwhisker', 'perf_value': 0, 'status': 'simulated'}
    ]
    # Set up donations
    donations = range(17, 0, -1)
    # Render the template
    return render(request, 'index.html', {
        'pawfolios': pawfolios,
        'current_entry': pawfolios[0]['name'],
        'donations': donations
    })

# Pawformances view
def get_pawformances(request):
    # Update pawformances
    pawformances = {
        'Mortimer': check_mortimer(),
        'Cecil': check_cecil(),
        'Gwendolyn': check_gwendolyn(),
        'Aunt Elinor': (0, 'simulated'),
        'Aurelia Goldwhisker': (0, 'simulated')
    }
    return JsonResponse(pawformances)

# Stock mood view
def get_stockmood(request):
    # Check stock moods
    stock_mood = check_stockMood()
    return JsonResponse(stock_mood)
