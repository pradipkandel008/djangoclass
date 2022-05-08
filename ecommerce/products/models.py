from django.db import models

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


class Student(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    batch = models.IntegerField()
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

