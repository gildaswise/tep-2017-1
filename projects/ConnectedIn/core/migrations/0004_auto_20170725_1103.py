# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to='images/avatars'),
        ),
    ]
