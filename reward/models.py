from django.db import models

# Create your models here.

class Reward(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Reward', null=True, blank=True)
    description = models.TextField()
    def __str__(self):
        return self.title