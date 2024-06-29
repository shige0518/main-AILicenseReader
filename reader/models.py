from django.db import models

# Create your models here.

class Images(models.Model):    
    image = models.ImageField(upload_to='img/upload')
    description = models.CharField(null=True, blank=True, max_length=256)