from django.db import models
from users.models import Customer

# Create your models here.
class Store(models.Model):
    store_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    store_owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.store_name)

