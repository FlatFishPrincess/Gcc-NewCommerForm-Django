# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchForm', '0002_auto_20180322_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='middle_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]