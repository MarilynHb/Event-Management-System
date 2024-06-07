from django.contrib import admin

# Register your models here.
from .models import Location, EventType, EventTag, UserProfile, Event, FileLink, ReportEvent, Industry

admin.site.register(Location)
admin.site.register(EventType)
admin.site.register(EventTag)
admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(FileLink)
admin.site.register(ReportEvent)
admin.site.register(Industry)
