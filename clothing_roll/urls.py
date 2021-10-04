from django.urls import path
from . import views
urlpatterns = [
   path('', views.Index, name="index"),
   path('shop/', views.ListAllProducts, name="shop"),
   path('shop/<str:slug>/', views.ProductDetail, name="product_detail"),
]