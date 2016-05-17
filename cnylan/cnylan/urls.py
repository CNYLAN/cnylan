"""cnylan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

import lan.views

urlpatterns = [

    # Home page
    url(r'^$', lan.views.homepage, name='homepage'),

    # Previous LANs
    url(r'^previous-lans/', lan.views.previous_lans, name='previous-lans'),

    # About
    url(r'^about/', lan.views.about, name='about'),

    # Gallery
    url(r'^gallery/', lan.views.gallery, name='gallery'),

    # Completed purchase page
    url(r'^thank-you/', lan.views.register_complete),

    # Admin
    url(r'^admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
