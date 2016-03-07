from django.conf.urls import patterns, url
from pitchify import views

urlpatterns = patterns('',
                       # login
                       url(r'^$', views.index, name='index'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),

                       # companies
                       url(r'^create_pitch/$', views.create_pitch, name='create_pitch'),
                       url(r'^my_pitches/$', views.my_pitches, name='my_pitches'),

                       # investors
                       url(r'^investor/pitches/$', views.investor_pitches, name='investor_pitches'),
                       url(r'^investor/pitch/(?P<pitch_id>[0-9]+)/$', views.investor_pitch, name='investor_pitch'),

                       # populate
                       url(r'^populate/$', views.populate, name='populate'),
                       )
