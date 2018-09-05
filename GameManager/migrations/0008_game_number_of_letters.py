# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0007_game_userplayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='number_of_letters',
            field=models.IntegerField(default=0),
        ),
    ]
