# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 02:16
from __future__ import unicode_literals

from django.db import migrations, models
import lan.models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0005_homepageimage_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_image',
            field=models.ImageField(blank=True, help_text='Banner Image', null=True, upload_to=lan.models.upload_location),
        ),
    ]
