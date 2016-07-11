# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okcoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brief', models.IntegerField(default=-1)),
            ],
        ),
        migrations.RemoveField(
            model_name='partner',
            name='brief',
        ),
        migrations.AddField(
            model_name='partnership',
            name='p1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okcoder.Partner'),
        ),
        migrations.AddField(
            model_name='partnership',
            name='p2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='okcoder.Partner'),
        ),
    ]