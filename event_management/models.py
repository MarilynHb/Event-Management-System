from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserProfile(AbstractUser):
    biography = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    followers_count = models.IntegerField(default=0)
    # groups = models.ManyToManyField(Group, related_name='user_profiles')
    # user_permissions = models.ManyToManyField(Permission, related_name='user_profiles')

    def __str__(self):
        return self.username

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description

class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class EventTag(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.description

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    type = models.ForeignKey(EventType, on_delete=models.DO_NOTHING, null=True)
    tag = models.ForeignKey(EventTag, on_delete=models.DO_NOTHING)
    link = models.URLField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    likes_count = models.IntegerField(default=0)
    created_by_id = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='events_created')
    modified_by_id = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='events_modified')
    created_on = models.DateTimeField()
    modified_on = models.DateTimeField()

class LikedEvents(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    owner_id = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name='liked_events')
    liked_on = models.DateTimeField()