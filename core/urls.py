from django.urls import path

from . import views
from .views import get_indices

urlpatterns = [
    # Home view
    path('', views.index, name = 'index'),
    # Indices update view
    path('indices/', get_indices, name = 'get_indices'),
    ]
