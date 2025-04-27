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
    # Render the 'index.html' template
    return render(request, 'index.html', {'performance': [performance_mortimer, performance_cecil]})
