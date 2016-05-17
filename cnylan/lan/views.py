from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import HomePage

from .forms import RegisterForm


def homepage(request):
    # need to order this by closest date in production, currently last object created
    homepage = HomePage.objects.get(current_homepage=True)
    #featured_lan = queryset.filter()
    #games = Game.objects.all()
   # sponsors = Sponsor.objects.all()
   # tournaments = Tournament.objects.all()

    context = {
        "homepage" : homepage,
        #"games" : games,
     #   "sponsors" : sponsors,

    }

    return render(request, "index.html", context)

def register(request):
    # need to order this by closest date in production, currently last object created
    homepage = HomePage.objects.get(current_homepage=True)
    #featured_lan = queryset.filter()
    #games = Game.objects.all()
   # sponsors = Sponsor.objects.all()
   # tournaments = Tournament.objects.all()

    context = {
        "homepage" : homepage,
        #"games" : games,
     #   "sponsors" : sponsors,

    }
    return render(request, "register.html", context)

def register_complete(request):
    context = { }
    return render(request, "thank-you.html", context)


def about(request):
    context = { }
    return render(request, "about.html", context)

def gallery(request):
    context = { }
    return render(request, "gallery.html", context)
