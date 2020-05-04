# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-04 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='FullDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_text', models.TextField(default='')),
                ('premium', models.BooleanField(default=True)),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.Catalogue')),
            ],
        ),
    ]
