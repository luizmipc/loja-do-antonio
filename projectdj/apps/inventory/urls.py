from django.urls import path
from . import views

urlpatterns = [
  path('', views.active, name='active-inventory'),
]