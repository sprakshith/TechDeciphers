from django.db import models

class Gadgets(models.Model):
    gadgetId = models.AutoField(primary_key=True)
    gadgetImage = models.ImageField(upload_to='TechDeciphers_Gadgets')
    typeOfGadget = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    miniHeading = models.CharField(max_length=200)
    miniContent = models.CharField(max_length=300)
    completeContent = models.TextField()
    postAuthor = models.CharField(max_length=40)
    postPublishDate = models.DateField()
