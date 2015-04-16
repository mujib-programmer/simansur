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
    url(r'^user/$', views.user, name='user'),
)
