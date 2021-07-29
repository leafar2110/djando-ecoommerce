from django.db import models
from users.models import User

# Create your models here.

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    line1 = models.CharField(max_length=200)
    line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    referennce = models.CharField(max_length=300)
    postal_code = models.CharField(max_length=10, null=False, blank=False)
    default = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.postal_code

    @property
    def address(self):
        return '{} - {} - {}'.format(self.city, self.state, self.country)