from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class CustomUser(AbstractUser):
    # add additional fields in here
    
    def __str__(self):
        return self.email

@receiver(post_save, sender=CustomUser)
def define_email(sender, instance, **kwargs):
    instance.email = instance.username
