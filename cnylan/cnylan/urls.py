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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from lan.views import homepage, about, register_complete

urlpatterns = [

    # Home page
    url(r'^$', homepage, name='homepage'),

    url(r'^', include("lan.urls", namespace='lan')),

    # About
    url(r'^about/', about, name='about'),


    # Completed purchase page
    url(r'^thank-you/', register_complete),

    # Admin
    url(r'^admin/', admin.site.urls),

]
"""
from lan.views import HomePageView, PreviousLansView, AboutPageView, GalleryView, RegisterCompleteView

urlpatterns = [

    # Home page
    url(r'^$', HomePageView.as_view(), name='homepage'),

    # Previous LANs
    url(r'^previous-lans/', PreviousLansView.as_view(), name='previous-lans'),

    # About
    url(r'^about/', AboutPageView.as_view(), name='about'),

    # Gallery
    url(r'^gallery/', GalleryView.as_view(), name='gallery'),

    # Completed purchase page
    url(r'^thank-you/', RegisterCompleteView.as_view()),

    # Admin
    url(r'^admin/', admin.site.urls),

]
"""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)