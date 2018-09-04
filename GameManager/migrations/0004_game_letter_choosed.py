# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0003_auto_20180904_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='letter_choosed',
            field=models.CharField(max_length=1, default=''),
            preserve_default=False,
        ),
    ]
