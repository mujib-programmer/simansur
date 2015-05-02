# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0014_surat_user_terkait'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aktivitas',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='aktivitas',
            name='user',
            field=models.ForeignKey(related_name='user', null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
