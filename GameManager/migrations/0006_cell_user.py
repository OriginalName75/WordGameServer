# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_auto_20180903_1437'),
        ('GameManager', '0005_auto_20180904_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='cell',
            name='user',
            field=models.ForeignKey(to='UserManagement.UserInfo', null=True, blank=True, default=None, related_name='cells'),
        ),
    ]
