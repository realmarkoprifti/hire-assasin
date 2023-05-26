from django.db import models
from django.contrib.auth.models import AbstractUser
from random import choice

# Create your models here.

class User(AbstractUser):
    pass


class AssasinProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field="username")
    hit_number = models.IntegerField(default=0)
    starting_price = models.IntegerField(default=0)
    btc_address = models.CharField(max_length=62, null=True)
    
    def __str__(self):
        return self.user.username
    

class Hit(models.Model):
    STATUS_CHOICES = (
        ("no_payment", "Hasn't Paid 🔴"),
        ("on_going", "On-Going 🟠"),
        ("completed", "Completed 🟢")
    )  
    
    id = models.AutoField(primary_key=True, auto_created=True)
    track_number = models.IntegerField(default=11111, unique=True)
    hitman = models.ForeignKey(AssasinProfile, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    target = models.CharField(max_length=250)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="no_payment")
    
    def __str__(self):
        return f"ID: {str(self.id)}, Username: {self.hitman.user}"
    