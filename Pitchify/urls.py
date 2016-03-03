from django.conf.urls import patterns, url
from pitchify import views

urlpatterns = patterns('',
                       # login
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),

                       # populate
                       url(r'^populate/$', views.populate, name='populate'),
                       )
