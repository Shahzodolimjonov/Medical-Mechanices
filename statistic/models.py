from django.db import models

# Create your models here.


# Xodim
class Employee(models.Model):
    full_name = models.CharField(max_length=150)
    birthdate = models.DateField()


# Mijoz
class Client(models.Model):
    full_name = models.CharField(max_length=150)
    birthdate = models.DateField()


# Mahsulot
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


# Buyurtma
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
