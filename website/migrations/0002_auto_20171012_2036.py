# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]