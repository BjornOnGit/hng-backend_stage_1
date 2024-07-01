from django.urls import path
from . import views

urlpatterns = [
    path('visitor', views.visitor_view, name='visitor'),
]
