# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_auto_20150422_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surat',
            name='id_pencatat',
            field=models.ForeignKey(null=True, related_name='id_pencatat', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='surat',
            name='id_penerima',
            field=models.ForeignKey(null=True, related_name='id_penerima', to=settings.AUTH_USER_MODEL),
        ),
    ]
