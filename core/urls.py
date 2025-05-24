from django.urls import path

from . import views
from .views import get_pawformances, get_stockmood

urlpatterns = [
    # Home view
    path('', views.index, name = 'index'),
    # Pawformances update view
    path('pawformances/', get_pawformances, name = 'get_pawformances'),
    # Indices update view
    path('stockmood/', get_stockmood, name = 'get_stockmood'),
    ]
