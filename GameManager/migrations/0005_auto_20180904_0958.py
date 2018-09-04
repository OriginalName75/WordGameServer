# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0004_game_letter_choosed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='letter_choosed',
            field=models.CharField(null=True, blank=True, default=None, max_length=1),
        ),
    ]
