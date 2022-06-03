from django import forms
from .models import Product, Student, FileUpload, Order
from django.forms import ModelForm


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.FloatField()


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['category','name']


class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address', 'payment_method']
        # exclude = ['category','name']


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class FileModelForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'


