# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0006_auto_20170126_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='planexercise',
            name='additional_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
