from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Surat(models.Model):
    no_surat = models.IntegerField(unique=True)
    no_agenda = models.IntegerField(null=True)
    perihal_surat = models.TextField(null=True,)
    tanggal_surat_masuk = models.DateField(null=True, auto_now_add=False)
    keterangan_disposisi = models.TextField(null=True)
    tingkat_kepentingan = models.CharField(null=True, max_length=15)
    dari = models.TextField(null=True)
    timestamp_surat = models.DateTimeField(null=True,auto_now_add=True)
    id_penerima = models.ForeignKey(User, null=True, related_name='id_penerima')
    id_pencatat = models.ForeignKey(User, null=True, related_name='id_pencatat')
    file_surat = models.FileField(upload_to=settings.UPLOAD_PATH, null=True, blank=True)
    
    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return str( self.no_surat )

class Disposisi(models.Model):
    id_penerima_disposisi = models.ForeignKey(User, null=False, related_name='id_penerima_disposisi')
    no_surat_disposisi = models.ForeignKey(Surat, null=False, related_name='no_surat_disposisi')
    id_pengirim_disposisi = models.ForeignKey(User, null=False, related_name='id_pengirim_disposisi')
    catatan_tambahan = models.CharField(max_length=25)
    timestamp_disposisi = models.DateTimeField(auto_now_add=True)
    tanggal_surat_disposisi = models.DateField(auto_now_add=False)
    
    #def __unicode__(self):  #For Python 2, use __str__ on Python 3
    def __str__(self):
        return str( self.no_surat_disposisi )
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    # tambahan atribut untuk user
    bidang = models.CharField(max_length=40, default="")
    jabatan = models.CharField(max_length=40, default="")
    role_pencatat = models.BooleanField(default=False)
    no_telepon = models.BigIntegerField()

    #def __unicode__(self): #For Python 2, use __str__ on Python 3
    def __str__(self):
        return self.user.username

