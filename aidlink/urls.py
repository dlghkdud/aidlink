from django.urls import path
from . import views

app_name = 'aidlink'

urlpatterns = [
    path('', views.index,name='index'),
    path('products/', views.products, name='products'),
    path('products_api/', views.products_api, name='products_api'),
]