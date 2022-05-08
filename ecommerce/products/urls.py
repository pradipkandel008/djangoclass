from django.urls import path
from . import views


urlpatterns = [
    path('products', views.get_products),
    path('post_student', views.post_student),
    path('get_student', views.get_student),
    path('update_student/<int:student_id>', views.update_student),
    path('delete_student/<int:student_id>', views.delete_student),

    path('post_file', views.post_file),
    path('get_file', views.get_file),
    path('update_file/<int:file_id', views.update_file),
    path('delete_file/<int:file_id', views.delete_file),
]

# 127.0.0.1:8000/products/products

# 127.0.0.1:8000/products/get_student/123

