# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20180207_0405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facultymember',
            old_name='faculty_firstsem',
            new_name='First_Semester',
        ),
        migrations.RenameField(
            model_name='facultymember',
            old_name='faculty_secondsem',
            new_name='Second_Semester',
        ),
        migrations.RenameField(
            model_name='facultymember',
            old_name='faculty_firstname',
            new_name='faculty_First_Name',
        ),
        migrations.RenameField(
            model_name='facultymember',
            old_name='faculty_lastname',
            new_name='faculty_Last_Name',
        ),
        migrations.RenameField(
            model_name='facultymember',
            old_name='faculty_middlename',
            new_name='faculty_Middle_Name',
        ),
    ]
