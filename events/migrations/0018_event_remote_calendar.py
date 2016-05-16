# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20160516_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='remote_calendar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.RemoteCalendar'),
        ),
    ]
