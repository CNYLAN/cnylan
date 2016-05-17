"""
lan URL Configuration

"""
from django.conf.urls import  url

from .views import homepage, event_list, event_detail, games_list, sponsors

urlpatterns = [
    #url(r'^$', homepage, name='homepage'),
    #url(r'^/register/', register, name='register'),
    #url(r'^event/$', event_list, name='event_list'),
    #url(r'^event/?(P<slug>[\w-]+)/$', event_detail, name='event_detail'),
    #url(r'^sponsors/$', sponsors, name='sponsors'),
    #url(r'^games/$', games_list, name='games_list'),
]
