from django.db import models

# Create your models here.

class Clothing(models.Model):
  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50)
  material = models.TextField(max_length=100)
  msrp = models.IntegerField()

  def __str__(self):
    return self.name