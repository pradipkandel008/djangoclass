from django import forms
from .models import Product, Student, FileUpload
from django.forms import ModelForm


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    price = forms.FloatField()


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['category','name']


class StudentModelForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class FileModelForm(ModelForm):
    class Meta:
        model = FileUpload
        fields = '__all__'


