from django.urls import path
from .views import *
app_name = 'suntory'

urlpatterns = [
    path('', distillery_info, name='distillery_info'),
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_details, name='product_details'),
]
