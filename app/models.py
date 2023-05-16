from django.db import models
from django.contrib.auth.models import User
from utils.date import date2jalali
import random
import string

class Paste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=100)

class Brush(models.Model):
    OWNER_CHOICES = (
        ('father', 'پدر'),
        ('mother', 'مادر'),
        ('son', 'پسر'),
        ('daughter', 'دختر'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.CharField(max_length=10, choices=OWNER_CHOICES)
    owner_name = models.CharField(max_length=255)
    

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)

    def jdate(self):
        return date2jalali(self.datetime)
    
    def time(self):
        return self.datetime.time


def rndcode():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(20))

class MagicCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, default=rndcode, unique=True)