# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KeysMemory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('public_0', models.CharField(max_length=1000)),
                ('public_1', models.CharField(max_length=1000)),
                ('private_0', models.CharField(max_length=1000)),
                ('private_1', models.CharField(max_length=1000)),
                ('date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, default=None, blank=True)),
            ],
        ),
    ]
