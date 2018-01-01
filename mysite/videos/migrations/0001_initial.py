# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('video', models.URLField(max_length=1000)),
                ('creator', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
    ]