# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appfaq', '0002_auto_20160515_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionreponse',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
