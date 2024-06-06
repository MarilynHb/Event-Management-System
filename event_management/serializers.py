from rest_framework import serializers
from event_management.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = '__all__'

class EventTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTag
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class LikedEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedEvents
        fields = '__all__'

class ReportEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportEvent
        fields = '__all__'

class FileLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLink
        fields = '__all__'