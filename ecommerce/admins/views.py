from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from products.models import *
from django.contrib.auth.models import User


@login_required
@admin_only
def admin_dashboard(request):
    students = Student.objects.all()
    student_count = students.count()
    files = FileUpload.objects.all()
    file_count = files.count()
    users = User.objects.all()
    user_count = users.filter(is_superuser=0, is_staff=0).count()
    admin_count = users.filter(is_superuser=1, is_staff=1).count()
    context = {
        'students': student_count,
        'files': file_count,
        'users': user_count,
        'admins': admin_count
    }
    return render(request, 'admins/admin_dashboard.html', context)


