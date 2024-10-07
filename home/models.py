from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.title

class Order(models.Model):
    name = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    age = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order by {self.name} for {self.product.title}"
