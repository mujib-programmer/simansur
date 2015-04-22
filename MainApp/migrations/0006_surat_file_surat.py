# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20150421_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='surat',
            name='file_surat',
            field=models.FileField(null=True, upload_to='C:\\Users\\phpgeek\\PycharmProjects\\simansur\\static\\upload', blank=True),
            preserve_default=True,
        ),
    ]
