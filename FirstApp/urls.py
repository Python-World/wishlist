from django.urls import path
from .views import CreateWish,UpdateWish,DeleteWish,WishList

urlpatterns=[
    path('',WishList,name='WishList'),
    path('create',CreateWish,name='CreateWish'),
    path('update/<int:id>',UpdateWish,name='UpdateWish'),
    path('delete/<int:id>',DeleteWish,name='DeleteWish'),

]