from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('asteroid/<str:asteroid_id>/', views.asteroid_detail, name='asteroid_detail'),
]
