# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_auto_20180903_1437'),
        ('GameManager', '0006_cell_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='userplayed',
            field=models.ForeignKey(blank=True, to='UserManagement.UserInfo', default=None, related_name='your_turn_to_choose', null=True),
        ),
    ]
