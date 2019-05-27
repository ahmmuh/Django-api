from django.db import models

# Create your models here.
class Achievement(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='achievement', null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.title