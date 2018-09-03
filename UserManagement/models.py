from django.contrib.auth.models import User
from django.db import models

from GameManager.models import Game


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name = "info")
    games = models.ManyToManyField(Game, blank=True, default = None, related_name = "users")
    mmr = models.FloatField(default = 2000)
    friends_asked = models.ManyToManyField("self",symmetrical=False,blank=True, \
                                           default = None, related_name = "friend_demands")