from django.contrib import admin
from MainApp.models import Surat, KotakSurat, UserProfile, Aktivitas, TrackSurat

class SuratAdmin(admin.ModelAdmin):
    list_display = ('no_surat', 'no_agenda', 'perihal', 'tanggal_surat_masuk', 'pengirim_surat_fisik',
                    'tingkat_kepentingan', 'file_surat', 'pencatat', 'tanggal_pencatatan', 'status')

class KotakSuratAdmin(admin.ModelAdmin):
    list_display = ('id', 'surat', 'pengirim', 'penerima', 'status', 'catatan_tambahan', 'jenis_pengiriman', 'tanggal')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bidang', 'jabatan', 'no_telepon')

class AktivitasAdmin(admin.ModelAdmin):
    list_display = ('id', 'tanggal','user','aktivitas')

class TrackSuratAdmin(admin.ModelAdmin):
    list_display = ('id', 'surat', 'tanggal', 'status')

# Register your models here.
#admin.site.register(Surat, SuratAdmin)
#admin.site.register(KotakSurat, KotakSuratAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
#admin.site.register(Aktivitas, AktivitasAdmin)
#admin.site.register(TrackSurat, TrackSuratAdmin)
