from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=300)
    size = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/', default='product_images/suntory.jpg')


    def __str__(self):
        return self.product_name

class Distillery(models.Model):
    distillery_name = models.CharField(max_length=50)
    distillery_country = models.CharField(max_length=50)
    distillery_description = models.CharField(max_length=1000)
    distillery_id = models.AutoField(primary_key=True)
    distillery_image = models.ImageField(upload_to='distillery_images/', default='distillery_images/default.jpg')

class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')