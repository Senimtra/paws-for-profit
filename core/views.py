from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from . utils import check_mortimer, check_cecil


@ensure_csrf_cookie
# Main index view
def index(request):
    # Check pawfolios performance
    performance_mortimer = check_mortimer()
    performance_cecil = check_cecil()
    # Create named entries
    performances = [
        {'name': 'Mortimer', 'value': performance_mortimer},
        {'name': 'Cecil', 'value': performance_cecil},
    ]
    # Sort descending by performance
    performances_sorted = sorted(performances, key = lambda x: x['value'], reverse = True)
    # Set the highest performer as the current_entry
    current_entry = performances_sorted[0]['name']
    # Render the template
    return render(request, 'index.html', {
        'performances': performances_sorted,
        'current_entry': current_entry,
    })
