# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okcoder', '0003_auto_20160627_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnership',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]