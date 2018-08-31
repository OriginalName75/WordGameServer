from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name = "info")
    friends = models.ManyToManyField("self", blank=True, default = None)
    mmr = models.FloatField(default = 2000)
    friends_asked = models.ManyToManyField("self",symmetrical=False,blank=True, \
                                           default = None, related_name = "friend_demands")