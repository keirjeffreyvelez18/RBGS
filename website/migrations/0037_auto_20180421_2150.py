# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-21 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_auto_20180421_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchtitle',
            name='research_program',
            field=models.CharField(max_length=100, null=''),
        ),
    ]
