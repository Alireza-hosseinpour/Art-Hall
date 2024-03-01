from django.urls import path
from . import views

app_name = 'products'



"""
we have 5 path here :
1.this is for our homepage 
2.this is for showing all products
3.this is for adding a user to favorite field of a product.
4.this is for show more informations about a product
5.and last one is for favorite products of a user( shows favorite items in a single page )
"""
urlpatterns = [

    path('', views.index, name='index'),
    path('product-list/', views.list_of_products, name='product-list'),
    path('fav/<int:product_id>/', views.favourites, name='fav'),
    path('product-detail/<int:id>/', views.product_detail, name='product-detail'),
    path('fav-list/', views.product_favourite_list, name='fav-list'),
]
