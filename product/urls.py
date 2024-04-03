from django.urls import path
from . import views

urlpatterns = [
    path('all_product/', views.ProductListView.as_view()),
    path('all_food/', views.FoodListView.as_view()),
]
