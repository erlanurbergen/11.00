from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Сотрудник")
    avatar = models.FileField(verbose_name="Аватар")

    def __str__(self):

        return self.fullname

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название товара")
    price = models.IntegerField(verbose_name="Цена товара")
    rating = models.FloatField(verbose_name="Рейтинг товара")
    description = models.TextField(verbose_name="Описание товара")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name}, {self.rating}"

