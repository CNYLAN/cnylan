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
