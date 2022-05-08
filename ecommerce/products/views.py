from django.shortcuts import render, redirect
from .models import Product, Student, FileUpload
from .forms import ProductForm, ProductModelForm
from django.http import HttpResponse


def get_products(request):
    products_database = Product.objects.all()
    context = {
        'products': products_database,
        'productform': ProductForm,
        'productmodelform': ProductModelForm,
        'activate_product': 'active'
    }
    return render(request, 'products/products.html', context)


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


def get_student(request):
    student_database = Student.objects.all()
    context = {
        'students': student_database,
        'activate_student': 'active'
    }
    return render(request, 'products/get_student.html', context)


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


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/get_student')


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


def get_file(request):
    file_database = FileUpload.objects.all()
    context = {
        'files': file_database,
        'activate_file': 'active'
    }
    return render(request, 'products/get_file.html', context)


def update_file(request, file_id):

    return render(request, 'products/update_file.html')


def delete_file(request, file_id):
    return redirect('/products/get_file')






