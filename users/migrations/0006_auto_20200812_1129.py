# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-08-12 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200811_0450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='user',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='images',
            name='user_profile',
        ),
    ]