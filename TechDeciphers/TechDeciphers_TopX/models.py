from django.db import models

class TopX(models.Model):
    topXId = models.AutoField(primary_key=True)
    topXImage = models.ImageField(upload_to='TechDeciphers_TopX', blank=True, null=True)
    typeOfTopX = models.CharField(max_length=100)
    heading = models.CharField(max_length=200)
    miniHeading = models.CharField(max_length=200)
    completeContent = models.TextField()
    postAuthor = models.CharField(max_length=40)
    postPublishDate = models.DateField()
