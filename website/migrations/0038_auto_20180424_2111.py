# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-24 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_auto_20180421_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchtitle',
            name='research_date',
            field=models.DateField(null=''),
        ),
    ]