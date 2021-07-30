from django.db import models
from django.contrib.auth.models import User

class Inspection(models.Model):      
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    date = models.DateField()
    container = models.ForeignKey("Container", on_delete=models.CASCADE)
    containerMainTray = models.BooleanField()
    containerReserveTray = models.BooleanField()
    containerHardware = models.BooleanField()
    containerChestStrap = models.BooleanField()
    containerLegStraps = models.BooleanField()
    containerRisers = models.BooleanField()
    containerStitching = models.BooleanField()
    containerGrommets = models.BooleanField()
    containerReserveHandle = models.BooleanField()
    containerCutawayHandle = models.BooleanField()
    containerWebbing = models.BooleanField()
    containerNotes = models.CharField(max_length=200)
    reserve = models.ForeignKey("Reserve", on_delete=models.CASCADE)
    reserveDBag = models.BooleanField()
    reserveLinks = models.BooleanField()
    reserveSuspensionLines = models.BooleanField()
    reserveBridlePilotChute = models.BooleanField()
    reserveCrossports = models.BooleanField()
    reserveSeamFabric = models.BooleanField()
    reserveSlider = models.BooleanField()
    reserveNotes = models.CharField(max_length=200)
    main = models.ForeignKey("Main", on_delete=models.CASCADE)
    mainDBag = models.BooleanField()
    mainLinks = models.BooleanField()
    mainSuspensionLines = models.BooleanField()
    mainBridlePilotChute = models.BooleanField()
    mainCrossports = models.BooleanField()
    mainSeamFabric = models.BooleanField()
    mainSlider = models.BooleanField()
    mainNotes = models.CharField(max_length=200)
    aad = models.ForeignKey("Aad", on_delete=models.CASCADE)
    aadInstallation = models.BooleanField()
    aadCables = models.BooleanField()
    aadInService = models.BooleanField()
    aadNotes = models.CharField(max_length=200)
    
