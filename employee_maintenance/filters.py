import django_filters
from .models import Employee



class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label='Search')

    class Meta:
        model = Employee
        fields = ['name']
