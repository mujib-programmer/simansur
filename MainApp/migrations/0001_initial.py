# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aktivitas',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('aktivitas', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_aktivitas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disposisi',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.CharField(null=True, max_length=50)),
                ('keterangan_disposisi', models.CharField(null=True, max_length=50)),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('penerima', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='penerima_disposisi')),
                ('pengirim', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='pengirim_disposisi')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KotakSurat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('status', models.CharField(null=True, max_length=15)),
                ('catatan_tambahan', models.TextField(null=True)),
                ('jenis_pengiriman', models.CharField(max_length=15)),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('penerima', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='penerima_kotak_surat')),
                ('pengirim', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='pengirim_kotak_surat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('no_surat', models.CharField(max_length=15, unique=True)),
                ('no_agenda', models.CharField(max_length=15)),
                ('perihal', models.TextField(null=True)),
                ('tanggal_surat_masuk', models.DateField(null=True)),
                ('pengirim_surat_fisik', models.TextField(null=True)),
                ('tingkat_kepentingan', models.CharField(null=True, max_length=15)),
                ('file_surat', models.FileField(null=True, upload_to='C:\\Users\\phpgeek\\PycharmProjects\\simansur\\static\\upload', blank=True)),
                ('tanggal_pencatatan', models.DateTimeField(null=True, auto_now_add=True)),
                ('status', models.CharField(null=True, max_length=15)),
                ('pencatat', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, related_name='pencatat_surat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TrackSurat',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('tanggal', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('surat', models.ForeignKey(to='MainApp.Surat', related_name='surat_track_surat')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('bidang', models.CharField(max_length=40, default='')),
                ('jabatan', models.CharField(max_length=40, default='')),
                ('no_telepon', models.CharField(max_length=15, default='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='kotaksurat',
            name='surat',
            field=models.ForeignKey(to='MainApp.Surat', related_name='surat_kotak_surat'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disposisi',
            name='surat',
            field=models.ForeignKey(to='MainApp.Surat', related_name='surat_disposisi'),
            preserve_default=True,
        ),
    ]
