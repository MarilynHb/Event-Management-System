from django.contrib import admin
from .models import UserProfile, Location, EventType, EventTag,Event, LikedEvents

admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(EventType)
admin.site.register(EventTag)
admin.site.register(Event)
admin.site.register(LikedEvents)

