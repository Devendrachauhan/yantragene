# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iname', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='images/gallery')),
            ],
        ),
    ]
