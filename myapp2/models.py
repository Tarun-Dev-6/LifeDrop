
from django.db import models 

class CarouselImage(models.Model):
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='carousel_images/')
     description = models.TextField(blank=True, null=True)

     def __str__(self):
        return self.title 
# Create your models here.
