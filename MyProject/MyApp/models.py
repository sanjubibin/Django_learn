from django.db import models

# Create your models here.
class UserBio(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    class Meta:
        managed = True