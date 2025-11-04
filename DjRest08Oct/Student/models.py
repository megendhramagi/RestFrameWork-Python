from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=21)

class Marks(models.Model):
    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    total = models.IntegerField()
    average = models.FloatField()
    isPass = models.BooleanField()

