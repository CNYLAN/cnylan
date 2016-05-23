from django.conf.urls import url

from lan.views import previous, gallery

urlpatterns = [
    # Previous LANs
    url(r'^previous/', previous, name='previous'),
    # Gallery - not implemented
    url(r'^gallery/', gallery, name='gallery'),
    # Left these for examples
    # url(r'^(?P<slug>[\w-]+)/$', post_list, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
