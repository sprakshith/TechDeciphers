from django.db import models

class Tutorial(models.Model):
    tutorial_id = models.AutoField(primary_key=True)
    tutorial_image = models.ImageField(upload_to='Tutorials', blank=True, null=True)
    heading = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    content = models.TextField()
    postAuthor = models.CharField(max_length=40)
    postPublishDate = models.DateField()
    isChildPage = models.BooleanField()
    parentId = models.IntegerField(default = 0)
    previousTutorial = models.IntegerField(default = 0)
    nextTutorial = models.IntegerField(default = 0)
    isPublished = models.BooleanField(default = True)

    def __str__(self):
        return '{} by {}'.format(self.heading, self.postAuthor)
