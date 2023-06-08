from django.db import models
from django.urls import reverse

# Create your models here.

class Clothing(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50)
  material = models.TextField(max_length=100)
  msrp = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse('clothing-detail', kwargs={'clothing_id': self.id})
  