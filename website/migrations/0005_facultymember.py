# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_newspost_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_lastname', models.CharField(max_length=100, null='')),
                ('faculty_firstname', models.CharField(max_length=100, null='')),
                ('faculty_middlename', models.CharField(max_length=100, null='')),
            ],
        ),
    ]