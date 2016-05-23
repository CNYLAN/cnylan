from django.contrib import admin



from lan.models import HomePageImage, HomePage, Event, Game, Prize, Sponsor
# Register your models here.

class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    extra = 3

class HomePageAdmin(admin.ModelAdmin):
	fields = ( ('homepage_name', 'current_homepage'), 'banner_image', 'heading', 'subheading', 
		('first_content_heading', 'second_content_heading', 'third_content_heading'),
		('featured_event', 'featured_games'))
	inlines = [ HomePageImageInline, ]


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Event)
admin.site.register(Game)
admin.site.register(Prize)
admin.site.register(Sponsor)