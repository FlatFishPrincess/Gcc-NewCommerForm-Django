# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-22 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street2',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='church_info',
            name='aquaintance',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='church_info',
            name='baptized_church',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='church_info',
            name='baptized_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='church_info',
            name='service_experience',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='residential_phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='duty',
            name='duty',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='family',
            name='family_relationship',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='licence_plate',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]