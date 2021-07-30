from django.db import models

class Reserve(models.Model):        
    
    dom = models.DateField()
    color = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    serialNumber = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    