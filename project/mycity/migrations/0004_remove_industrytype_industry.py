# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-19 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycity', '0003_auto_20170919_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industrytype',
            name='Industry',
        ),
    ]
