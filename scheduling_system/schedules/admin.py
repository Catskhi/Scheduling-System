from django.contrib import admin

# Register your models here.

from .models import Event, Technical, Changes

admin.site.register(Event)
admin.site.register(Technical)
admin.site.register(Changes)