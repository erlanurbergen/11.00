from django import forms

from .models import Employee, Product

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["fullname", "avatar"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'