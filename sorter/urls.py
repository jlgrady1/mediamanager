from django.conf.urls import patterns, url

from sorter import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^config/$', views.config, name='config'),
        url(r'^test/$', views.test, name='test'),
)
