# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0004_auto_20170126_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='planexercise',
            name='count',
            field=models.PositiveSmallIntegerField(default=1, help_text='How many times this exercise should be done per day'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='distance',
            field=models.FloatField(blank=True, help_text='Through distance in meters', null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='number_of_reps',
            field=models.PositiveSmallIntegerField(default=1, help_text='How many times to do this'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='weight',
            field=models.FloatField(blank=True, help_text='Weight of object in kilograms', null=True),
        ),
        migrations.AlterField(
            model_name='planexercise',
            name='distance',
            field=models.FloatField(blank=True, help_text='Through distance in meters', null=True),
        ),
        migrations.AlterField(
            model_name='planexercise',
            name='number_of_reps',
            field=models.PositiveSmallIntegerField(default=1, help_text='How many times to do this'),
        ),
        migrations.AlterField(
            model_name='planexercise',
            name='weight',
            field=models.FloatField(blank=True, help_text='Weight of object in kilograms', null=True),
        ),
    ]