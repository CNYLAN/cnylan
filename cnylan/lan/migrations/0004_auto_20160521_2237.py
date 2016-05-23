# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import lan.models


class Migration(migrations.Migration):

    dependencies = [
        ('lan', '0003_auto_20160521_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', help_text="This is where you would select an image for a banner or jumbotron.                                    I haven't built this into the Html so it wouldn't show up anywhere right now.", null=True, upload_to=lan.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0)),
                ('height_field', models.IntegerField(default=0)),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lan.HomePage')),
            ],
        ),
        migrations.RemoveField(
            model_name='images',
            name='homepage',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]