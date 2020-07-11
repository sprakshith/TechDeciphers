from django.db import models

class Leaks(models.Model):
    leakId = models.AutoField(primary_key=True)
    leakImage = models.ImageField(upload_to='TechDeciphers_Leaks')
    typeOfLeak = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    miniHeading = models.CharField(max_length=200)
    completeContent = models.TextField()
    postAuthor = models.CharField(max_length=40)
    postPublishDate = models.DateField()
