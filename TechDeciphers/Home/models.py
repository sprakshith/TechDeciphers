from django.db import models

class DropSuggestionModel(models.Model):
    suggestiontId = models.AutoField(primary_key=True)
    suggestorEmailId = models.CharField(max_length=200)
    suggestiontText = models.TextField()

    def __str__(self):
        return '{}'.format(self.suggestorEmailId)

class KeepMeUpdatedEmail(models.Model):
    newsletterId = models.AutoField(primary_key=True)
    newsletterEmailId = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.newsletterEmailId)
