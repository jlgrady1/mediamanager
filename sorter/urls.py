from django.conf.urls import patterns, url

from sorter import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^config/$', views.config, name='config'),
        url(r'^test/$', views.test, name='test'),
)
