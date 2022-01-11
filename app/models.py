from django.db import models
from datetime import datetime

# Create your models here.


class Polls(models.Model):
    Sujet = models.CharField(max_length=200, blank=True, null=True)
    Question = models.CharField(max_length=200, blank=True, null=True)
    date_creation = models.DateTimeField('date creation', default=datetime.now())

    def __str__(self):
        return self.Sujet or "? (no Sujet) ?"


class Choice(models.Model):

    question = models.ForeignKey(Polls, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

