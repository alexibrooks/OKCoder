# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 15:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okcoder', '0002_auto_20160627_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=0)),
                ('overall', models.IntegerField()),
                ('learned', models.IntegerField()),
                ('workload', models.IntegerField()),
                ('again', models.IntegerField()),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='eval_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='evaluator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='okcoder.Partner'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='okcoder.Partner'),
        ),
    ]
