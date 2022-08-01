from django.shortcuts import render
from .models import Product, Employee

from django.urls import reverse
from django.shortcuts import redirect

from .forms import EmployeeForm


def index(request):
    if request.method == "POST":
        # fullname = request.POST.get("fullname", "test")
        # employee = Employee(fullname = fullname)
        # employee.fullname += " test"
        # employee.save()
        employee = EmployeeForm(request.POST, request.FILES)
        employee.save()
        return redirect(reverse('main:index', args=()))

    employees = Employee.objects.all()

    return render(request, 'main/index.html', {"employees": employees})


def profile(request):
    return render(request, 'main/profile.html', {})


