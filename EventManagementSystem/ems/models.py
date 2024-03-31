from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    biography = models.TextField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    followers_count = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name='user_profiles')
    user_permissions = models.ManyToManyField(Permission, related_name='user_profiles')

    def __str__(self):
        return self.username

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_description = models.CharField(max_length=100)

class EventType(models.Model):
    event_type_id = models.AutoField(primary_key=True)
    event_type_name = models.CharField(max_length=100)

class EventTag(models.Model):
    event_tag_id = models.AutoField(primary_key=True)
    event_tag_description = models.CharField(max_length=100)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=100)
    event_description = models.CharField(max_length=100)
    event_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    event_tag = models.ForeignKey(EventTag, on_delete=models.CASCADE)
    event_link = models.URLField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_likes_count = models.IntegerField()
    event_created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='events_created')
    event_modified_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='events_modified')
    event_created_on = models.DateTimeField()
    event_modified_on = models.DateTimeField()

class LikedEvents(models.Model):
    liked_events_id = models.AutoField(primary_key=True)
    liked_events_event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    liked_events_user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='liked_events')
    liked_events_liked_on = models.DateTimeField()
