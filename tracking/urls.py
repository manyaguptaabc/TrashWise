from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),           # root URL
    path('dashboard/', views.dashboard, name='dashboard'), # optional
]
