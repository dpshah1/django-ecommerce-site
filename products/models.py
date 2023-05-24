from django.db import models
from stores.models import Store

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product_name)
    
class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    