# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20150507_0540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='surat',
            old_name='dihapus',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='surat',
            name='file_surat',
            field=models.FileField(null=True, upload_to='/home/mujibur/PycharmProjects/simansur/static/upload', blank=True),
        ),
    ]
