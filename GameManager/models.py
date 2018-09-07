import datetime
from django.db import models


# Create your models here.
class Game(models.Model):
    isStarted = models.BooleanField(default = False)
    date = models.DateField(default=datetime.date.today)
    userturn = models.ForeignKey("UserManagement.UserInfo", blank=True, null=True, default = None, \
                                 related_name = "your_turn_to_play")
    letter_choosed = models.CharField(max_length = 1, blank=True, null=True, default = None)
    userplayed = models.ForeignKey("UserManagement.UserInfo", blank=True, null=True, default = None, \
                                 related_name = "your_turn_to_choose")
    number_of_letters = models.IntegerField(default = 0)
    number_of_quit = models.IntegerField(default = 0)
    userleft = models.ForeignKey("UserManagement.UserInfo", blank=True, null=True, default = None, \
                                 related_name = "left_games")
    mmr_calculated = models.BooleanField(default = False)
class Cell(models.Model):
    game = models.ForeignKey(Game, related_name = "cells")
    row = models.IntegerField()
    col = models.IntegerField()
    letter = models.CharField(max_length = 1)
    user = models.ForeignKey("UserManagement.UserInfo", blank=True, null=True, default = None, \
                                 related_name = "cells")