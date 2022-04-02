from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='pages-login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
