# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 00:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_recurrence_dtend'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_date',
            new_name='dtend',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='dtstart',
        ),
    ]