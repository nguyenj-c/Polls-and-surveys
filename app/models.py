from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Poll(models.Model):
    Question = models.CharField(max_length=200, blank=True, null=True)
    option_1 = models.CharField(max_length=30,blank=True, null=True)
    option_2 = models.CharField(max_length=30,blank=True, null=True)
    option_3 = models.CharField(max_length=30,blank=True, null=True)
    option_4 = models.CharField(max_length=30,blank=True, null=True)
    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)
    option_4_count = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_creation = models.DateTimeField('date creation', default=timezone.now())

    def total(self):
        return self.option_1_count + self.option_2_count + self.option_3_count + self.option_4_count

    def __str__(self):
        return f"{self.Question}"

