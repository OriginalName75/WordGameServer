# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('CryptoMess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keysmemory',
            name='user',
            field=models.ForeignKey(related_name='key', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
