# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_userpreregistration_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreregistration',
            name='password',
            field=models.CharField(default='test', max_length=50),
        ),
    ]
