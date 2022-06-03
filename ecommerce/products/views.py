from django.shortcuts import render, redirect
from .models import Product, Student, FileUpload, Cart, Order
from .forms import ProductForm, ProductModelForm, StudentModelForm, FileModelForm, OrderModelForm
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


@login_required
@user_only
def post_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Product Added Successfully')
            return redirect('/products/get_product')
        else:
            context = {
                'form_backend': form,
            }
            messages.add_message(request, messages.ERROR, 'Please verify form fields')
            return render(request, 'products/post_product.html', context)
    context = {
        'form_backend': ProductModelForm,
        'activate_ecommerce': 'active'
    }
    return render(request, 'products/post_product.html', context)


@login_required
@user_only
def get_product(request):
    product_backend = Product.objects.all()
    context = {
        'products': product_backend,
        'activate_ecommerce': 'active'
    }
    return render(request, 'products/get_product.html', context)


@login_required
@user_only
def add_to_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    check_item_presence = Cart.objects.filter(user=user, product=product)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Product already present in cart')
        return redirect('/products/get_product')
    else:
        cart = Cart.objects.create(user=user, product=product)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Product added to the cart')
            return redirect('/products/get_product')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add product to cart')
            return redirect('/products/get_product')


@login_required
@user_only
def get_cart_items(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    context = {
        'products': cart_items,
        'activate_cart': 'active'
    }
    return render(request, 'products/get_cart_items.html', context)


def remove_cart_item(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()
    messages.add_message(request, messages.SUCCESS, 'Cart item removed')
    return redirect('/products/get_cart_items')


def remove_all_cart_items(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    cart_items.delete()
    messages.add_message(request, messages.SUCCESS, 'All Cart items removed')
    return redirect('/products/get_cart_items')


def order_form(request, product_id, cart_id):
    user = request.user
    product = Product.objects.get(id=product_id)
    cart_item = Cart.objects.get(id=cart_id)

    if request.method == "POST":
        form = OrderModelForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = product.price
            total_price = int(quantity)*int(price)
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')

            order = Order.objects.create(quantity=quantity,
                                         total_price=total_price,
                                         status='Pending',
                                         payment_method='Esewa',
                                         payment_status=False,
                                         contact_no=contact_no,
                                         contact_address=contact_address,
                                         product=product,
                                         user=user)
            if order:
                context = {
                    'order': order,
                    'cart_item': cart_item
                }
                return render(request, 'products/esewa_payment.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Please verify form fields')
            context = {
                'form_backend': form
            }
            return render(request, 'products/order_form.html', context)

    context = {
        'form_backend': OrderModelForm
    }
    return render(request, 'products/order_form.html', context)


import requests as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/products/my_order')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/products/get_cart_items')

@login_required
@user_only
def my_order(request):
    user = request.user
    items = Order.objects.filter(user=user).order_by('-id')
    context = {
        'items':items,
        'activate_myorders':'active'
    }
    return render(request, 'products/my_order.html', context)




