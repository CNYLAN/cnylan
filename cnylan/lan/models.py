from __future__ import unicode_literals

from django.db import models
from django.db import transaction
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField

# Create your models here.

class HomePageManager(models.Manager):
    def create_homepage(self, title):
        homepage = self.create(homepage_name=title, current_homepage=True)
        return homepage

def upload_location(instance, filename):
    """
    defines an upload location for images for the HomePage. 
    Will be served to /media/filename.extension
    """
    HomePageModel = instance.__class__
    new_id = HomePageModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model HomePage. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class TimeStampedModel(models.Model):
    """
    Abstract model for created and updated fields. Most models have a created and updated field to
    track objects over time
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class HomePage(models.Model):
    """
    Main HomePage object. It's useful to build in the HomePage in the back end. Although it does contrict the
    front end designer to specific fields. This would be more useful if requirements for homepage were defined nicely.
    Therefore, you may have to edit html directly. Although, this isn't ideal.
    """
    current_homepage = models.BooleanField(help_text="Click here if you want this page to be the current home page",)
    homepage_name = models.CharField(max_length=35)
    heading = models.CharField(max_length=200,
        help_text="The main heading for the homepage",
        default="Central New York LAN")
    subheading = models.CharField(max_length=200,
        help_text="The subheading just below the heading",
        default="Default subheading")
    banner_image = models.ImageField(upload_to=upload_location,
                    null=True,
                    blank=True,
                    help_text="Banner Image")
    featured_event = models.ForeignKey("Event", blank=True, null=True,
        help_text="If selected item from this event will be featured "
                  "on the home page.")
    featured_games = models.ManyToManyField("Game", blank=True,
        help_text="Games to show on the homepage.")
    first_content_heading = models.CharField(max_length=200,
        help_text="A heading for left side page content",
        default="Default Middle Heading Title")
    second_content_heading = models.CharField(max_length=200,
        help_text="A heading for left side page content",
        default="Default Left Heading Title")
    third_content_heading = models.CharField(max_length=200,
        help_text="A heading for left side page content",
        default="Default Right Heading Title")

    objects = HomePageManager()

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")

    @transaction.atomic
    def save(self, *args, **kwargs):
        """
        Checks to see if any other HomePage objects current_homepage
        is set to True. If one is, it will change the current object to True
        and the other object to False.

        transaction.atomic decorator protects the atomicity of the database
        see django docs for more detail
        """
        if self.current_homepage:
            HomePage.objects.filter(
                current_homepage=True).update(current_homepage=False)
        super(HomePage, self).save(*args, **kwargs)

    def __str__(self):
        return self.homepage_name

    def get_absolute_url(self):
        """
        absolute url
        """
        return reverse("lan:homepage", kwargs={})

class HomePageImage(models.Model):
    """
    This Foreign keys to HomePage in order to set up multiple images on the homepage.
    related_name set to "images". Refer to object in views as HomePage.images.all()
    for a specific HomePage object
    """
    homepage = models.ForeignKey(HomePage, related_name='images')
    image = models.ImageField(upload_to=upload_location,
                        null=True,
                        blank=True,
                        width_field="width_field",
                        height_field="height_field",
                        help_text="This is where you would select an image for a banner or jumbotron. \
                                   I haven't built this into the Html so it wouldn't show up anywhere right now.")
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    label = models.CharField(max_length=50)


class Event(TimeStampedModel):
    """
    Creates an event object to track specific events. 
    Will be useful for looking back at previous lan objects.
    For example, could have a previous lan page and a template 
    could iterate over each object or a subset of objects to display
    previous lan data
    """
    event_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(_("Event Start Date"))
    end_date  = models.DateTimeField(_("Event End Date"))
    location = models.CharField(max_length=100)
    details = models.TextField()
    ticket_cost = models.CharField(max_length=100)
    sponsors = models.ManyToManyField("Sponsor", blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ("-start_date", )


    def __str__(self):
        return self.event_name

    #def get_absolute_url(self):
    #    """
    #    absolute url not set
    #    """
    #    return reverse("lan:event_detail", kwargs={"slug": self.slug})


class Game(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    prize = models.ManyToManyField("Prize", blank=True)

    def __str__(self):
        return self.name

class Prize(models.Model):
    prize = models.CharField(max_length=100)

    def __str__(self):
        return self.prize