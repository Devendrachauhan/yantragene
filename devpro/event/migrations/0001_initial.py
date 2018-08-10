# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-09 11:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.IntegerField()),
                ('bran', models.CharField(max_length=200)),
                ('bimage', models.ImageField(null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coord', models.CharField(max_length=200)),
                ('cimage', models.ImageField(blank=True, upload_to='images')),
                ('mob', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('eve', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=30, null=True)),
                ('events_name', models.CharField(blank=True, max_length=30, null=True)),
                ('pname2', models.CharField(blank=True, max_length=50, null=True)),
                ('pname3', models.CharField(blank=True, max_length=50, null=True)),
                ('pname4', models.CharField(blank=True, max_length=50, null=True)),
                ('pname5', models.CharField(blank=True, max_length=50, null=True)),
                ('events', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.Event')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='coordinator',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.Event'),
        ),
    ]
