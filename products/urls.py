from django.urls import path
from products import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<int:product_id>', views.product_page, name="product")
]
