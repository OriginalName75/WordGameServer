import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class KeysMemory(models.Model):
    public_0 = models.CharField(max_length=1000)
    public_1 = models.CharField(max_length=1000)
    private_0 = models.CharField(max_length=1000)
    private_1 = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, blank=True, null=True, default = None)
    