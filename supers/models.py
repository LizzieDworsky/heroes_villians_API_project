from django.db import models
from super_types.models import SuperType

# Create your models here.


class Power(models.Model):
    name = models.CharField(max_length=255)


class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    powers = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(SuperType, default=1, on_delete=models.PROTECT)


## Bonus 1:

#- Alter the Super model to replace primary & secondary ability with a 'powers' ManyToManyField.
#- Create a PATCH endpoint for the supers app that allows you to add a new Power to a Super by submitting the PK of the hero and the new power as path variables.