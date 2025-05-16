from django.urls import path

from . import views
from .views import get_stockmood

urlpatterns = [
    # Home view
    path('', views.index, name = 'index'),
    # Indices update view
    path('stockmood/', get_stockmood, name = 'get_stockmood'),
    ]
