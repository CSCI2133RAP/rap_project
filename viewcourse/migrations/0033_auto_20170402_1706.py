# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-02 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewcourse', '0032_auto_20170402_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='coursetitle',
            field=models.CharField(max_length=40),
        ),
    ]
