from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    phone = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Bill_Product(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE) 
    quantity = models.FloatField(null=True)


class Bill(models.Model):
    total_amount = models.FloatField()
    paid_amount = models.FloatField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_items = models.ForeignKey(Bill_Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer
