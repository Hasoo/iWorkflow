# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAdmin',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('user_pass', models.CharField(max_length=64)),
                ('user_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'iw_admin',
                'managed': False,
            },
        ),
    ]
