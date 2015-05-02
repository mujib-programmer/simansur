# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0013_auto_20150502_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='surat',
            name='user_terkait',
            field=models.ManyToManyField(to='MainApp.UserProfile', null=True, related_name='user_terkait'),
            preserve_default=True,
        ),
    ]
