import uuid

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    subscriptor = models.OneToOneField(
        'users.Subscriptor',
        on_delete=models.CASCADE,
        related_name='subscription'
    )
    
    def __str__(self):
        return 'Subscription for ' + self.subscriptor.user.email

@receiver(pre_save, sender=Subscription)
def complete_subscription_data(sender, instance, *args, **kwargs):
    """ 
    Sets the co2_tons_per_month and monthly_fee according to the user carbon 
    footprint info 
    """
    co2_tons_per_year = instance.subscriptor.co2_tons_per_year
    # Insert Toroto's secret formula here
    instance.co2_tons_per_month =  co2_tons_per_year / 12
    instance.monthly_fee = float(instance.co2_tons_per_month) * 12.0