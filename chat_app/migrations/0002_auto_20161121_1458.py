# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(to='chat_app.Room', related_name='messages'),
        ),
    ]
