from django.urls import path

import accounts.views
from . import views

urlpatterns = [
    path('', views.admin_dashboard),
    path('logout', accounts.views.logout_user)
]


#  127.0.0.1:8000/admin-dashboard/