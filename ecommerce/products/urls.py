from django.urls import path
from . import views


urlpatterns = [
    path('products', views.get_products, name='products'),
    # 127.0.0.1:8000/products/products
    path('post_student', views.post_student, name='post_student'),
    path('get_student', views.get_student, name='get_student'),
    path('update_student/<int:student_id>', views.update_student),
    path('delete_student/<int:student_id>', views.delete_student),

    path('post_file', views.post_file),
    path('get_file', views.get_file),
    path('update_file/<int:file_id>', views.update_file),
    path('delete_file/<int:file_id>', views.delete_file),

    path('post_student_m', views.post_student_m),
    path('get_student_m', views.get_student_m),
    path('update_student_m/<int:student_id>', views.update_student_m),
    path('delete_student_m/<int:student_id>', views.delete_student_m),

    path('post_file_m', views.post_file_m),
    path('get_file_m', views.get_file_m),
    path('update_file_m/<int:file_id>', views.update_file_m),
    path('delete_file_m/<int:file_id>', views.delete_file_m),

    path('get_product', views.get_product),
    path('post_product', views.post_product),
    path('add_to_cart/<int:product_id>', views.add_to_cart),
    path('get_cart_items', views.get_cart_items),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    path('remove_all_cart_items', views.remove_all_cart_items),
    path('order_form/<int:product_id>/<int:cart_id>', views.order_form),
    path('esewa_verify', views.esewa_verify),
    path('my_order',views.my_order),
]

# 127.0.0.1:8000/products/products

# 127.0.0.1:8000/products/get_student/123

