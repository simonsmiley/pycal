# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 23:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pycal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='dend',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
        migrations.AddField(
            model_name='event',
            name='dstart',
            field=models.DateField(default=str(datetime.date(2016, 5, 18)), verbose_name='Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='tend',
            field=models.TimeField(blank=True, null=True, verbose_name='End'),
        ),
        migrations.AddField(
            model_name='event',
            name='tstart',
            field=models.TimeField(default='23:04:12', verbose_name='From'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='dtstart',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start'),
        ),
    ]
