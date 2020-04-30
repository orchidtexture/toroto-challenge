import uuid

from django.db import models

# Create your models here.

class Subscription(models.Model):
    """ Model for subscription """ 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    monthly_fee = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    co2_tons_per_month = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    creation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return 'Subscription for ' + self.user.email