# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0010_game_userleft'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='mmr_calculated',
            field=models.BooleanField(default=False),
        ),
    ]
