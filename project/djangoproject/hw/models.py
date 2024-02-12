from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    register_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: 
        {self.phone}, address: {self.address}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField(default=0)
    register_date = models.DateTimeField(auto_now=True)


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    register_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.register_date} - {self.product_id} - {self.cost}'
