from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User, Group
from MainApp.models import Surat, Disposisi, UserProfile

TINGKAT_KEPENTINGAN_SURAT_CHOICES = (
    ('normal', 'normal'),
    ('penting', 'penting'),
)

class SuratForm(forms.ModelForm):
    no_surat = forms.CharField(label='No Surat')
    no_agenda = forms.CharField(label='No Agenda')
    perihal = forms.CharField(label='Perihal Surat')
    tanggal_surat_masuk = forms.DateField(label='Tanggal Surat Masuk', widget=SelectDateWidget())
    pengirim_surat_fisik = forms.CharField(label='Pengirim Surat Fisik')
    tingkat_kepentingan = forms.ChoiceField(label='Tingkat Kepentingan', choices=TINGKAT_KEPENTINGAN_SURAT_CHOICES)
    file_surat = forms.FileField(label='File Surat')

    class Meta:
        model = Surat
        exclude = ('pencatat','tanggal_pencatatan', 'dihapus')


class DisposisiForm(forms.ModelForm):
    penerima_disposisi = forms.ModelChoiceField(label='Penerima Disposisi', queryset=UserProfile.objects.all())
    #pengirim_disposisi = forms.ModelChoiceField(label='Pengirim Disposisi', queryset=UserProfile.objects.all())
    tanggal_surat_disposisi = forms.DateField(label='Tanggal Surat Disposisi', widget=SelectDateWidget())
    catatan_tambahan = forms.CharField(label='Catatan Tambahan')

    class Meta:
        model = Disposisi
        exclude = ('surat', 'pengirim_disposisi',)

class UserProfileForm(forms.Form):
    username = forms.SlugField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget = forms.PasswordInput(render_value = True))
    email = forms.EmailField(label="Email")
    groups = forms.ModelMultipleChoiceField(label="Groups", queryset=Group.objects.all())
    first_name = forms.CharField(label="Nama Depan", max_length=30)
    last_name = forms.CharField(label="Nama Belakang", max_length=30)
    is_active = forms.BooleanField(label="Status Aktif", required=False)
    jabatan = forms.CharField(label="Jabatan", max_length=40)
    bidang = forms.CharField(label="Bidang", max_length=40)
    no_telepon = forms.IntegerField(label="No Telepon")



