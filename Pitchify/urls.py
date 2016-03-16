from django.conf.urls import patterns, url
from pitchify import views

urlpatterns = patterns(
    '',
    # login
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),

    # companies
    url(r'^create_pitch/$', views.create_pitch, name='create_pitch'),
    url(r'^my_pitches/$', views.my_pitches, name='my_pitches'),
    url(r'^company/accept_offer/(?P<offer_id>[0-9]+)/(?P<accept>[true|false]+)/(?P<offer_answer>.+)/$',
        views.company_accept_offer, name='company_accept_offer'),
    url(r'^company/edit_pitch/(?P<pitch_id>[0-9]+)/(?P<youtube>.+)/(?P<description>.+)/$',
        views.edit_pitch, name='edit_pitch'),

    # investors
    url(r'^investor/my_offers/$', views.investor_offers, name='investor_offers'),
    url(r'^investor/pitches/$', views.investor_pitches, name='investor_pitches'),
    url(r'^investor/remove_offer/(?P<offer_id>[0-9]+)/$', views.investor_remove_offer, name='investor_remove_offer'),
    url(r'^investor/add_offer/(?P<pitch_id>[0-9]+)/(?P<offer_stock_count>[0-9]+)/(?P<offer_stock_price>[0-9]+)/(?P<offer_message>.+)/$',
        views.investor_add_offer, name='investor_add_offer'),

    # both
    url(r'^pitch/(?P<pitch_id>[0-9]+)/$', views.pitch, name='pitch'),

    # populate
    url(r'^populate/$', views.populate, name='populate'),
)
