from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from . utils import check_mortimer


@ensure_csrf_cookie
# Main index view
def index(request):
    # Check Mortimer pawfolio
    performance = check_mortimer()    
    # Render the 'index.html' template
    return render(request, 'index.html', {'performance': performance})
