from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name = "info")
    friends = models.ManyToManyField("self", blank=True, null=True, default = None)
    mmr = models.FloatField(default = 2000)