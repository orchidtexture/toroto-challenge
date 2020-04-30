from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CustomUser(AbstractUser):
    """ Custom user model for that with email and Carbon footprint data """ 
    # add additional fields in here
    co2_tons_per_year = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.email

@receiver(post_save, sender=CustomUser)
def define_email(sender, instance, **kwargs):
    """ Defines the instance email field as the value captured in username """
    instance.email = instance.username
