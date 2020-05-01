import uuid

from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

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
    subscriber = models.OneToOneField(
        'users.Subscriber',
        on_delete=models.CASCADE,
        related_name='subscription'
    )
    
    def __str__(self):
        return 'Subscription for ' + self.subscriber.email
