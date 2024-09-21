from django.urls import path
from . import views

urlpatterns = [
    path("", views.WishList, name="WishList"),  # Homepage listing all wishes
    path("create/", views.CreateWish, name="CreateWish"),  # URL for creating a new wish
    path("update/<int:id>/", views.UpdateWish, name="UpdateWish"),  # URL for updating a specific wish
    path("delete/<int:id>/", views.DeleteWish, name="DeleteWish"),  # URL for deleting a specific wish
    path("search/<str:text>/", views.Search, name="Search"),  # URL for searching wishes by text (newly added)
]
