from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.CharField(max_length=512, default='default description')
    product_img = models.ImageField(upload_to='images/', default='default image')

    def __str__(self):
        """A string representation of the model."""
        return self.name