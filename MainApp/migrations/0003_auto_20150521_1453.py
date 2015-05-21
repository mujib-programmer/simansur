# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20150521_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disposisi',
            name='penerima',
        ),
        migrations.RemoveField(
            model_name='disposisi',
            name='pengirim',
        ),
        migrations.RemoveField(
            model_name='disposisi',
            name='surat',
        ),
        migrations.DeleteModel(
            name='Disposisi',
        ),
    ]
