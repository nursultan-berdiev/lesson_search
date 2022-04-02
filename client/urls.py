from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerListView.as_view(), name = 'list_view'),
    path('products/', views.ProductListView.as_view(), name = 'product_list'),
    path('test/', views.Test.as_view(), name = 'test'),
    path('generate/<int:count>/', views.generate, name='generate'),
]
