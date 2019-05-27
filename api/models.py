from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Activities(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='activities', null=True, blank=True)
    description = models.TextField()
    week = models.IntegerField()
    where = models.CharField(max_length=120)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    contact_person = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    
    


