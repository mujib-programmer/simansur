from django.conf.urls import patterns, include, url
from django.contrib import admin
from MainApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simansur.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.user_login, name='login'),
    url(r'^accounts/logout/$', views.user_logout, name='logout'),

    url(r'^surat/$', views.surat, name='surat'),
    url(r'^surat/(?P<no_surat>[\w]+)/$', views.surat_detail, name='surat_detail'), # look for any sequence of alphanumeric characters (e.g. a-z, A-Z, or 0-9)
    url(r'^surat_tambah/$', views.surat_tambah, name='surat_tambah'),
    url(r'^surat_edit/(?P<no_surat>[\w]+)/$', views.surat_edit, name='surat_edit'),
    url(r'^surat_delete/(?P<no_surat>[\w]+)/$', views.surat_delete, name='surat_delete'),
    url(r'^surat_download/(?P<no_surat>[\w]+)/$', views.surat_download, name='surat_download'),
    url(r'^surat_kirim/(?P<no_surat>[\w]+)/$', views.surat_kirim, name='surat_kirim'),

    url(r'^disposisi_tambah/(?P<no_surat>[\w]+)/$', views.disposisi_tambah, name='disposisi_tambah'),
    url(r'^disposisi_edit/(?P<id_disposisi>[\w]+)/$', views.disposisi_edit, name='disposisi_edit'),
    url(r'^disposisi_delete/(?P<no_surat>[\w]+)/(?P<id_disposisi>[\w]+)/$', views.disposisi_delete, name='disposisi_delete'),

    url(r'^user/$', views.user, name='user'),
    url(r'^user/(?P<username>[\w\-]+)/$', views.user_detail, name='user_detail'),
    url(r'^user_tambah/$', views.user_tambah, name='user_tambah'),
    url(r'^user_edit/(?P<username>[\w\-]+)/$', views.user_edit, name='user_edit'),
    url(r'^user_delete/(?P<username>[\w\-]+)/$', views.user_delete, name='user_delete'),

    url(r'^aktivitas/$', views.aktivitas, name='aktivitas'),

    url(r'^statistik/$', views.statistik, name='statistik'),


)
