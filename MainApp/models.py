from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    bidang = models.CharField(max_length=40, default="")
    jabatan = models.CharField(max_length=40, default="")
    no_telepon = models.BigIntegerField()

    #def __unicode__(self): #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.user.username


class Surat(models.Model):
    no_surat = models.CharField(null=False, unique=True, max_length=15)
    no_agenda = models.CharField(null=False, max_length=15)
    perihal = models.TextField(null=True)
    tanggal_surat_masuk = models.DateField(null=True, auto_now_add=False)
    pengirim_surat_fisik = models.TextField(null=True)
    tingkat_kepentingan = models.CharField(null=True, max_length=15)
    file_surat = models.FileField(upload_to=settings.UPLOAD_PATH, null=True, blank=True)
    pencatat = models.ForeignKey(User, null=True, related_name='pencatat_surat')
    tanggal_pencatatan = models.DateTimeField(null=True,auto_now_add=True)
    status = models.CharField(null=True, max_length=15) # dilabeli, dikirim, dihapus

    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.no_surat

# berisi semua surat untuk masing-masing user
class KotakSurat(models.Model):
    id = models.AutoField(primary_key=True)
    surat = models.ForeignKey(Surat, null=False, related_name='surat_kotak_surat')
    pengirim = models.ForeignKey(User, null=True, related_name='pengirim_kotak_surat')
    penerima = models.ForeignKey(User, null=True, related_name='penerima_kotak_surat')
    status = models.CharField(null=True, max_length=15) # diterima, dibaca, didisposisi
    catatan_tambahan = models.TextField(null=True)
    jenis_pengiriman = models.CharField(null=False, max_length=15) # langsung, disposisi
    tanggal = models.DateTimeField(auto_now_add=True)

    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.no_surat

class Disposisi(models.Model):
    id = models.AutoField(primary_key=True)
    surat = models.ForeignKey(Surat, null=False, related_name='surat_disposisi')
    pengirim = models.ForeignKey(User, null=True, related_name='pengirim_disposisi')
    penerima = models.ForeignKey(User, null=True, related_name='penerima_disposisi')
    status = models.CharField(null=True, max_length=50)
    keterangan_disposisi = models.CharField(null=True, max_length=50)
    tanggal = models.DateTimeField(auto_now_add=True)

    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return str( self.surat )

class Aktivitas(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateTimeField(null=False,auto_now_add=True)
    user = models.ForeignKey(User, null=False, related_name='user_aktivitas')
    aktivitas = models.CharField(null=False, max_length=255)

    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.aktivitas

class TrackSurat(models.Model):
    id = models.AutoField(primary_key=True)
    surat = models.ForeignKey(Surat, null=False, related_name='surat_track_surat')
    tanggal = models.DateTimeField(null=False,auto_now_add=True)
    status = models.CharField(null=False, max_length=50)

    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.status