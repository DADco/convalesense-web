# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0009_auto_20170126_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='steps',
            field=models.TextField(blank=True, help_text='If you would like to add a step by step guide for this exercise list it here', null=True),
        ),
    ]
