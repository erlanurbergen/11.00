from django.shortcuts import render
from .models import Product, Employee

from django.urls import reverse
from django.shortcuts import redirect

from .forms import EmployeeForm, ProductForm

from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate


def index(request):
    if request.method == "POST":
        # fullname = request.POST.get("fullname", "test")
        # employee = Employee(fullname = fullname)
        # employee.fullname += " test"
        # employee.save()
        employee = EmployeeForm(request.POST, request.FILES)
        employee.save()
        return redirect(reverse('main:index', args=()))

    products = Product.objects.all()

    return render(request, 'main/index.html', {"products": products})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse("main:profile", args=()))
        else:
            return redirect(reverse("main:login_page", args=()))
    return render(request, 'main/login_page.html', {})

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'main/profile.html', {})
    else:
        return redirect(reverse('main:login_page', args=()))

def logout_view(request):
    logout(request)
    return redirect(reverse("main:login_page"))

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        email = request.POST.get("email", None)
        first_name = request.POST.get("first_name", None)
        last_name = request.POST.get("last_name", None)

        user = User.objects.create_user(username=username,
                                        password=password,
                                        email=email,
                                        first_name=first_name,
                                        last_name=last_name)
        return redirect(reverse('main:login_page', args=()))
    return render(request, "main/register_page.html", {})


def create_products(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:index', args=()))
    return render(request, 'main/products_form.html', {"form": form})


def update_products(request, pk):
    product = Product.objects.get(id = pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('main:index', args=()))
    return render(request, 'main/products_form.html', {"form": form})


def delete_products(request, pk):
    product = Product.objects.get(id = pk)
    if request.method == 'POST':
        product.delete()
        return redirect(reverse('main:index', args=()))
    return render(request, 'main/delete.html', {"product": product})





