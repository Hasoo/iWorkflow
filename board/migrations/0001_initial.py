# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('attach', models.TextField(blank=True)),
                ('secret_key', models.CharField(blank=True, max_length=16)),
            ],
        ),
    ]