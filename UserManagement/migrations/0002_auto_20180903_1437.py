# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameManager', '0001_initial'),
        ('UserManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='friends',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='games',
            field=models.ManyToManyField(related_name='users', to='GameManager.Game', default=None, blank=True),
        ),
    ]
