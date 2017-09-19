# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-19 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0002_auto_20170919_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industries',
            name='college',
        ),
        migrations.AddField(
            model_name='industries',
            name='name',
            field=models.CharField(default='name', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurants',
            name='email',
            field=models.CharField(default='email', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_firstname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_lastname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='username', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
