# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 18:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0005_todo_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='modified',
        ),
    ]
