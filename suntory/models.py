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

class DistilleryImage(models.Model):
    distillery = models.ForeignKey(Distillery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='distillery_images/', default='distillery_images/default.jpg')
    image_name = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        if not self.image_name:
            self.image_name = str(self.image)
        super().save(*args, **kwargs)


class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')