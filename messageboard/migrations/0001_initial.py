# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-29 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=32)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
