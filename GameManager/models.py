from django.db import models
import datetime

# Create your models here.
class Game(models.Model):
    isStarted = models.BooleanField(default = False)
    date = models.DateField(default=datetime.date.today)
