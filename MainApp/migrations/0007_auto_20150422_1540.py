# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_surat_file_surat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surat',
            name='no_agenda',
            field=models.IntegerField(null=True),
        ),
    ]
