# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-08 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lectures',
            new_name='Lecture',
        ),
    ]