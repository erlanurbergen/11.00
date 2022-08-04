from django.contrib import admin
from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('index', views.index, name = "index"),
    path('profile', views.profile, name = "profile"),
    path('login', views.login_view, name = "login_page"),
    path('logout', views.logout_view, name = "logout_page"),
    path('register', views.register, name = "register"),
    path('create_products', views.create_products, name = "create_products"),
    path('update_products/<int:pk>', views.update_products, name = "update_products"),
    path('delete_products/<int:pk>', views.delete_products, name = "delete_products"),
]