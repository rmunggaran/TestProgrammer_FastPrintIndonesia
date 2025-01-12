from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('create/', views.produk_create, name='produk_create'),
    path('<int:id>/edit/', views.produk_edit, name='produk_edit'),
    path('<int:id>/delete/', views.produk_delete, name='produk_delete'),
]
