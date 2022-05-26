from django.db import models
from django.forms import CharField

# Create your models here.

class SuperType(models.Model):
    type = models.CharField(max_length=255)