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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('mmr', models.FloatField(default=2000)),
                ('friends', models.ManyToManyField(related_name='_userinfo_friends_+', default=None, to='UserManagement.UserInfo', blank=True)),
                ('friends_asked', models.ManyToManyField(related_name='friend_demands', default=None, to='UserManagement.UserInfo', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='info')),
            ],
        ),
    ]
