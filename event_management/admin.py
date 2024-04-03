from django.contrib import admin

# Register your models here.
from .models import Location, EventType, EventTag, UserProfile

admin.site.register(Location)
admin.site.register(EventType)
admin.site.register(EventTag)
admin.site.register(UserProfile)
