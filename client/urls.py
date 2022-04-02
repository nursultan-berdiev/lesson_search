from django.urls import path
from . import views

urlpatterns = [
    path('generate/<int:count>/', views.generate, name='generate'),
]
