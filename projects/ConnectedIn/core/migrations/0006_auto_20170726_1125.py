# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170725_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/photo.jpg', null=True, upload_to='avatars/'),
        ),
    ]
