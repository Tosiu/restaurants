from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    phone = models.CharField(max_length=9, validators=[RegexValidator("\d\d\d\d\d\d\d\d\d")])
    notes = models.CharField(max_length=500)


class User(AbstractUser):
    pass


class Visit(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE, primary_key=True)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



