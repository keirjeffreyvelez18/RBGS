# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-21 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0034_auto_20180418_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='researchtitle',
            name='research_program',
            field=models.TextField(default=' ', max_length=100, null=''),
            preserve_default=False,
        ),
    ]
