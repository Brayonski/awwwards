# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-24 10:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awwwards', '0006_projects_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awwwards.Projects'),
        ),
    ]
