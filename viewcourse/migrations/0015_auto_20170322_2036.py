# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewcourse', '0014_auto_20170322_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingcriteria',
            name='course',
        ),
        migrations.RemoveField(
            model_name='ratingcriteria',
            name='prof',
        ),
        migrations.AddField(
            model_name='professor',
            name='clarity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='professor',
            name='easiness',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='professor',
            name='helpfulness',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.AddField(
            model_name='professor',
            name='ratetimes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='professor',
            name='textbook',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
        migrations.DeleteModel(
            name='ratingCriteria',
        ),
    ]
