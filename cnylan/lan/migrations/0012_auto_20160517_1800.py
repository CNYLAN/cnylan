# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0011_auto_20160517_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='current_homepage',
            field=models.BooleanField(help_text='Click here if you want this page to be the current home page'),
        ),
    ]