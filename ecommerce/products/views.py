from django.shortcuts import render, redirect
from .models import Product, Student
from .forms import ProductForm, ProductModelForm
from django.http import HttpResponse


def get_products(request):
    products_database = Product.objects.all()
    context = {
        'products': products_database,
        'productform': ProductForm,
        'productmodelform': ProductModelForm
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
    return render(request, 'products/post_student.html')


def get_student(request):
    student_database = Student.objects.all()
    context = {
        'students': student_database
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
        'student': student_database
    }
    return render(request, 'products/update_student.html', context)


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/products/get_student')





