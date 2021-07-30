from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):        
    
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    