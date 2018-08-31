# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('mmr', models.FloatField(default=2000)),
                ('friends', models.ManyToManyField(to='UserManagement.UserInfo', related_name='_userinfo_friends_+', blank=True, null=True, default=None)),
                ('user', models.OneToOneField(related_name='info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
