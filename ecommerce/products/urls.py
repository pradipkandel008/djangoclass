from django.urls import path
from . import views

urlpatterns = [
    path('products', views.get_products),
    path('post_student', views.post_student),
    path('get_student', views.get_student),

]

# 127.0.0.1:8000/products/products