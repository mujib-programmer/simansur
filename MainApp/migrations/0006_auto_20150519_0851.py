# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20150517_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surat',
            name='file_surat',
            field=models.FileField(upload_to='/home/phpgeek/PycharmProjects/simansur/static/upload', blank=True, null=True),
        ),
    ]
