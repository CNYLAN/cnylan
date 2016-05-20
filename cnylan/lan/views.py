"""
from django.shortcuts import render

# Create your views here.
from .models import HomePage


def homepage(request):
    try:
        homepage = HomePage.objects.get(current_homepage=True)
    except HomePage.DoesNotExist:
        homepage = HomePage.objects.create_homepage("Automatically Created Homepage")
    context = {
            "homepage": homepage,
    }
    return render(request, "index.html", context)

def register_complete(request):
    context = { }
    return render(request, "thank-you.html", context)


def about(request):
    context = { }
    return render(request, "about.html", context)

def gallery(request):
    context = { }
    return render(request, "gallery.html", context)

def previous_lans(request):
    context = { }
    return render(request, "previous-lans.html", context)
"""

from django.views.generic import DetailView, ListView, TemplateView
from django.utils import timezone

# Create your views here.
from lan.models import HomePage

class HomePageView(ListView):
    model = HomePage # Not needed if a queryset is defined
    template_name = "index.html"
    context_object_name = 'homepage'
    try:
        # used filter instead of get to obtain a queryset
        queryset = HomePage.objects.get(current_homepage=True)
    except HomePage.DoesNotExist:
        # create a basic default homepage
        HomePage.objects.create_homepage("Automatically Created Homepage")
        queryset = HomePage.objects.filter(current_homepage=True)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomePageView, self).get_context_data(**kwargs)
        # Add in QuerySet of all Homepages - as an example... I don't want to do this
        # could also add in context from a seperate model ... Event.objects.all()
        #context['homepages'] = HomePage.objects.all()
        # DOes this work?
        context['now'] = timezone.now()

        # etc
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RegisterCompleteView(TemplateView):
    template_name = 'thank-you.html'

class GalleryView(TemplateView):
    template_name = 'gallery.html'

class PreviousLansView(TemplateView):
    template_name = 'previous-lans.html'
