# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltexamapp', '0005_auto_20161118_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beltexamapp.User'),
        ),
    ]
