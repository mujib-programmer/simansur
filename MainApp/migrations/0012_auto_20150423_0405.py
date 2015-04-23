# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_auto_20150423_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disposisi',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
