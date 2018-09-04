# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0002_auto_20180903_1437'),
        ('GameManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('letter', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='userturn',
            field=models.ForeignKey(related_name='your_turn_to_play', null=True, default=None, to='UserManagement.UserInfo', blank=True),
        ),
        migrations.AddField(
            model_name='cell',
            name='game',
            field=models.ForeignKey(to='GameManager.Game'),
        ),
    ]
