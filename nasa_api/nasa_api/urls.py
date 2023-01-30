from django.contrib import admin
from django.urls import path, include
from asteroids import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', include('asteroids.urls')),
]
