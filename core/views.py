from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
# Main index view
def index(request):
    # Render the 'index.html' template
    return render(request, 'index.html')
