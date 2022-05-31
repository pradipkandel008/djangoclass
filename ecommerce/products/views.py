from django.shortcuts import render, redirect
from .models import Product, Student, FileUpload
from .forms import ProductForm, ProductModelForm, StudentModelForm, FileModelForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import StudentFilter
from accounts.auth import user_only
from django.contrib.auth.models import User


@login_required
@user_only
def get_products(request):
    products_database = Product.objects.all()
    students = Student.objects.all()
    student_count = students.count()
    files = FileUpload.objects.all()
    file_count = files.count()
    users = User.objects.all()
    user_count = users.filter(is_superuser=0, is_staff=0).count()
    admin_count = users.filter(is_superuser=1, is_staff=1).count()

    context = {
        'products': products_database,
        'productform': ProductForm,
        'productmodelform': ProductModelForm,
        'activate_product': 'active',
        'students': student_count,
        'files': file_count,
        'users': user_count,
        'admins': admin_count
    }
    return render(request, 'products/products.html', context)


@login_required
@user_only
def post_student(request):
    if request.method == 'POST':
        firstname_form = request.POST['firstname']
        lastname_form = request.POST['lastname']
        batch_form = request.POST['batch']
        image_url_form = request.POST['image_url']
        student = Student.objects.create(
            firstname=firstname_form,
            lastname=lastname_form,
            batch=batch_form,
            image_url=image_url_form
        )
        if student:
            return redirect('/products/get_student')
        else:
            return HttpResponse("Unable to create student")
    context = {
        'activate_student': 'active'
    }
    return render(request, 'products/post_student.html', context)


@login_required
@user_only
def get_student(request):
    student_database = Student.objects.all().order_by('-created_date')
    # student_database = Student.objects.filter(firstname='Pradip')
    context = {
        'students': student_database,
        'activate_student': 'active'
    }
    return render(request, 'products/get_student.html', context)


@login_required
@user_only
def update_student(request, student_id):
    student_database = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student_database.firstname = request.POST['firstname']
        student_database.lastname = request.POST['lastname']
        student_database.batch = request.POST['batch']
        student_database.image_url = request.POST['image_url']
        student_database.save()
        return redirect('/products/get_student')
    context = {
        'student': student_database,
        'activate_student': 'active'
    }
    return render(request, 'products/update_student.html', context)


@login_required
@user_only
def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/get_student')


@login_required
@user_only
def post_file(request):
    if request.method == 'POST':
        title_fe = request.POST.get('title')
        description_fe = request.POST.get('description')
        image_fe = request.FILES.get('image')
        file_obj = FileUpload(title=title_fe, description=description_fe, image=image_fe)
        file_obj.save()
        if file_obj:
            return redirect('/products/get_file')
        else:
            return HttpResponse('Unable to add file')
    context = {
        'activate_file': 'active'
    }
    return render(request, 'products/post_file.html', context)


@login_required
@user_only
def get_file(request):
    file_database = FileUpload.objects.all()
    context = {
        'files': file_database,
        'activate_file': 'active'
    }
    return render(request, 'products/get_file.html', context)


@login_required
@user_only
def update_file(request, file_id):
    file_database = FileUpload.objects.get(id=file_id)
    context = {
        'file': file_database
    }

    if request.method == 'POST':
        if request.FILES.get('image'):
            file_database.title = request.POST.get('title')
            file_database.description = request.POST.get('description')
            file_database.image = request.FILES.get('image')
            file_database.save()
        else:
            file_database.title = request.POST.get('title')
            file_database.description = request.POST.get('description')
            file_database.save()
        return redirect('/products/get_file')
    return render(request, 'products/update_file.html', context)


@login_required
@user_only
def delete_file(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect('/products/get_file')


@login_required
@user_only
def post_student_m(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Added Successfully')
            return redirect('/products/get_student_m')
        else:
            context = {
                'form_backend': form,
            }
            messages.add_message(request, messages.ERROR, 'Please verify form fields')
            return render(request, 'products/post_student_m.html', context)
    context = {
        'form_backend': StudentModelForm,
        'activate_student_m': 'active'
    }
    return render(request, 'products/post_student_m.html', context)


from django.core.paginator import Paginator
@login_required
@user_only
def get_student_m(request):
    students_database = Student.objects.all().order_by('-id')
    paginator = Paginator(students_database, 2)
    page_number = request.GET.get('page')
    student_obj = paginator.get_page(page_number)
    #student_filter = StudentFilter(request.GET, queryset=students_database)
    #student_final = student_filter.qs
    context = {
        'students': student_obj,
        'activate_student_m': 'active',
        'student_filter': StudentFilter
    }
    return render(request, 'products/get_student_m.html', context)


@login_required
@user_only
def update_student_m(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/products/get_student_m')
    context = {
        'form_backend': StudentModelForm(instance=student),
        'activate_student_m': 'active'
    }
    return render(request, 'products/update_student_m.html', context)


@login_required
@user_only
def delete_student_m(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/get_student_m')


@login_required
@user_only
def post_file_m(request):
    if request.method == 'POST':
        form = FileModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/get_file_m')
    context = {
        'form_backend': FileModelForm,
        'activate_file_m': 'active'
    }
    return render(request, 'products/post_file_m.html', context)


@login_required
@user_only
def get_file_m(request):
    files_backend = FileUpload.objects.all()
    context = {
        'files': files_backend,
        'activate_file_m': 'active'
    }
    return render(request, 'products/get_file_m.html', context)


@login_required
@user_only
def update_file_m(request,file_id):
    file = FileUpload.objects.get(id=file_id)
    if request.method == 'POST':
        form = FileModelForm(request.POST, request.FILES, instance=file)
        if form.is_valid():
            form.save()
            return redirect('/products/get_file_m')
    context = {
        'form_backend': FileModelForm(instance=file),
        'activate_file_m': 'active'
    }
    return render(request, 'products/update_file_m.html', context)


@login_required
@user_only
def delete_file_m(request, file_id):
    file = FileUpload.objects.get(id=file_id)
    file.delete()
    return redirect('/products/get_file_m')








