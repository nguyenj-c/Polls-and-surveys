from django.db import models
from datetime import datetime

# Create your models here.


class Polls(models.Model):
    Sujet = models.CharField(max_length=200, blank=True)
    Question = models.CharField(max_length=200, blank=True, null=True)
    option_1 = models.CharField(max_length=30,blank=True, null=True)
    option_2 = models.CharField(max_length=30,blank=True, null=True)
    option_3 = models.CharField(max_length=30,blank=True, null=True)
    option_4 = models.CharField(max_length=30,blank=True, null=True)
    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)
    option_4_count = models.IntegerField(default=0)
    date_creation = models.DateTimeField('date creation', default=datetime.now())

    def total(self):
        return self.option_1_count + self.option_2_count + self.option_3_count + self.option_4_count
