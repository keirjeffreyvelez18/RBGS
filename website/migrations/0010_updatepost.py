# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-08 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20180209_0005'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdatePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_title', models.CharField(max_length=1000, null='')),
            ],
        ),
    ]
