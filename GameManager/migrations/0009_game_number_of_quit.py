# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0008_game_number_of_letters'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='number_of_quit',
            field=models.IntegerField(default=0),
        ),
    ]
