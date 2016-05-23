from django.shortcuts import render

# Create your views here.
from .models import HomePage


def homepage(request):
    """
    Builds view for homepage.
    """
    try:
        homepage = HomePage.objects.get(current_homepage=True)
    except HomePage.DoesNotExist:
        homepage = HomePage.objects.create_homepage("Automatically Created Homepage")

    banner_image = homepage.banner_image
    """
    need a better way to create viewable objects - currently not that dynamic as
    the user needs to get the label correct of 'first', 'second', 'third'.
    I can prob change widget in the admin so they can only select 1 2 or 3... look into this
    """
    first_image = homepage.images.get(label='first').image
    second_image = homepage.images.get(label='second').image
    third_image = homepage.images.get(label='third').image
    context = {
            "homepage": homepage,
            "banner_image": banner_image,
            "first_image": first_image,
            "second_image": second_image,
            "third_image": third_image,

    }
    return render(request, "index.html", context)

def contact(request):
    context = { }
    return render(request, "contact.html", context)


def information(request):
    context = { }
    return render(request, "information.html", context)

def gallery(request):
    context = { }
    return render(request, "gallery.html", context)

def previous(request):
    context = { }
    return render(request, "previous-lans.html", context)