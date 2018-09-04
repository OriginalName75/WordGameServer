# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0002_auto_20180904_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='game',
            field=models.ForeignKey(related_name='cells', to='GameManager.Game'),
        ),
    ]
