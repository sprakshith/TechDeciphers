from django.db import models

class Gadgets(models.Model):
    gadgetId = models.AutoField(primary_key=True)
    gadgetImage = models.ImageField(upload_to='TechDeciphers_Gadgets', blank=True, null=True)
    typeOfGadget = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    miniHeading = models.CharField(max_length=180)
    miniContent = models.CharField(max_length=180)
    completeContent = models.TextField()
    postAuthor = models.CharField(max_length=40)
    postPublishDate = models.DateField()
    isPublished = models.BooleanField(default = False)

    def __str__(self):
        return '{} by {}'.format(self.heading, self.postAuthor)
