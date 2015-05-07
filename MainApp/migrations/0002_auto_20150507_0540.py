# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktivitas',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='aktivitas',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_aktivitas'),
        ),
    ]
