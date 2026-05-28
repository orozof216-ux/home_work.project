from django.urls import path
from .views import *

urlpatterns = [
    # Categories
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    # Products
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),

    # Reviews
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]