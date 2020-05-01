import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CustomUser(AbstractUser):
    """ Custom user base model """ 
    # add additional fields in here
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    toroto_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email

@receiver(post_save, sender=CustomUser)
def define_email(sender, instance, **kwargs):
    """ Defines the instance email field as the value captured in username """
    instance.email = instance.username


class Subscriber(models.Model):
    """ User model for subscriber """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    co2_tons_per_year = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    creation_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email
