from django.db import models

class Aad(models.Model):        
    
    dom = models.DateField()
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    serialNumber = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    