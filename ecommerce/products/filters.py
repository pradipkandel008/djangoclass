import django_filters
from .models import Student
from django_filters import CharFilter


class StudentFilter(django_filters.FilterSet):
    firstname = CharFilter(field_name='firstname', lookup_expr='icontains')
    lastname = CharFilter(field_name='lastname', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'batch']