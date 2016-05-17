from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Event)
admin.site.register(models.Game)
admin.site.register(models.HomePage)
admin.site.register(models.Prize)
admin.site.register(models.Sponsor)