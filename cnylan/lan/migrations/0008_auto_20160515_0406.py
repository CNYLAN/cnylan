# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 04:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0007_event_sponsors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='sponsor',
            new_name='name',
        ),
    ]
