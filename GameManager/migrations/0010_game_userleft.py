# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_auto_20180903_1437'),
        ('GameManager', '0009_game_number_of_quit'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='userleft',
            field=models.ForeignKey(null=True, blank=True, related_name='left_games', default=None, to='UserManagement.UserInfo'),
        ),
    ]
