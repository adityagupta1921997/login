# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-17 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
