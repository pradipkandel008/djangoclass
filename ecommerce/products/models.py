from django.db import models
from django.core import validators
from django.core.validators import *
from django.contrib.auth.models import User

# create table table_name(
#     firstname varchar(255),
#     dob date
# );

# products_product


class Product(models.Model):
    CATEGORY = (
        ('Sports', 'Sports'),
        ('Books', 'Books'),
        ('Electronics', 'Electronics')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)
    category = models.CharField(max_length=200, choices=CATEGORY, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered')
    )
    PAYMENT = (
        ('COD', 'COD'),
        ('ESewa', 'ESewa'),
        ('Khalti', 'Khalti')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=200)
    payment_method = models.CharField(choices=PAYMENT, max_length=200)
    payment_status = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=10)
    contact_address = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)


class Student(models.Model):
    firstname = models.CharField(max_length=200, validators=[validators.MinLengthValidator(2)])
    lastname = models.CharField(max_length=200, validators=[validators.MinLengthValidator(2)])
    batch = models.IntegerField(validators=[validators.MaxValueValidator(100)])
    email = models.EmailField(null=True, blank=True, validators=[validate_email])
    image_url = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname


class FileUpload(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    image = models.ImageField(upload_to='static/uploads')

    def __str__(self):
        return self.title




