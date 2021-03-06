# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 02:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=254)),
                ('site_code', models.CharField(max_length=2)),
                ('subscription_date', models.DateTimeField(verbose_name='date subscribed')),
            ],
        ),
    ]
