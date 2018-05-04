# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 01:39
from __future__ import unicode_literals
from django.db import migrations, models


def migrate_history(apps, schema_editor):
    History = apps.get_registered_model('main', 'History')
    User = apps.get_registered_model('auth', 'User')
    for history in History.objects.filter(initiator_type="users"):
        history.executor = User(pk=history.initiator)
        history.initiator_type = "project"
        history.initiator = history.project_id
        history.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0038_history_executor'),
    ]
    operations = [
        migrations.AlterField(
            model_name='history',
            name='initiator_type',
            field=models.CharField(default='project', max_length=50),
        ),
        migrations.RunPython(migrate_history),
    ]
