from django.contrib import admin

# Register your models here.

from .models import Event, Technical, Changes, Deleted_Event

admin.site.register(Event)
admin.site.register(Technical)
admin.site.register(Changes)
admin.site.register(Deleted_Event)