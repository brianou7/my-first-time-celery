from django.db import models

# Create your models here.
class Order(models.Model):

    customer = models.CharField("Customer", max_length=150)
    email = models.EmailField("Email", max_length=254)
    description = models.TextField("Order description", max_length=5000)

    class Meta:
        verbose_name = 'Order'
        ordering = ['customer']
