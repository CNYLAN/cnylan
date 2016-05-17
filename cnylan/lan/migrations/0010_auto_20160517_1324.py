# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0009_auto_20160515_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='left_content_heading',
            field=models.CharField(default='Default Left Heading Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='right_content_heading',
            field=models.CharField(default='Default Right Heading Title', max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subheading',
            field=models.CharField(default='Default subheading', help_text='The subheading just below the heading', max_length=200),
        ),
    ]
