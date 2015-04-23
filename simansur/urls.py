from django.conf.urls import patterns, include, url
from django.contrib import admin
from MainApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simansur.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.login, name='login'),
    url(r'^surat/$', views.surat, name='surat'),
    url(r'^surat/(?P<no_surat>[\w]+)/$', views.surat_detail, name='surat_detail'), # look for any sequence of alphanumeric characters (e.g. a-z, A-Z, or 0-9)
    url(r'^surat_tambah/$', views.surat_tambah, name='surat_tambah'),
    url(r'^surat_edit/(?P<no_surat>[\w]+)/$', views.surat_edit, name='surat_edit'),
    url(r'^surat_delete/(?P<no_surat>[\w]+)/$', views.surat_delete, name='surat_delete'),
    url(r'^user/$', views.user, name='user'),
)
