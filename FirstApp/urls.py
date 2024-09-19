from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishList, name='WishList'),
    path('create/', views.CreateWish, name='CreateWish'),
    path('update/<int:id>/', views.UpdateWish, name='UpdateWish'),
    path('delete/<int:id>/', views.DeleteWish, name='DeleteWish'),
    path('search/<str:text>/', views.Search, name='Search'),  # Added search URL
]
