from rest_framework import serializers
from event_management.models import *

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry  # Specify the model associated with this serializer
        fields = '_all_'  # Or specify the fields you want to include/exclude

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
    type = EventTypeSerializer()  # Nested Serializer
    tag = EventTagSerializer()  # Nested Serializer
    location = LocationSerializer()  # Nested Serializer

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'location', 'type', 'tag', 'link', 'start_date', 'end_date', 'likes_count']

    def create(self, validated_data):
        type_data = validated_data.pop('type')
        tag_data = validated_data.pop('tag')
        location_data = validated_data.pop('location')

        event = Event.objects.create(**validated_data)

        EventType.objects.create(event=event, **type_data)
        EventTag.objects.create(event=event, **tag_data)
        Location.objects.create(event=event, **location_data)

        return event

    def update(self, instance, validated_data):
        type_data = validated_data.pop('type')
        tag_data = validated_data.pop('tag')
        location_data = validated_data.pop('location')


        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.link = validated_data.get('link', instance.link)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.likes_count = validated_data.get('likes_count', instance.likes_count)

        instance.save()

        EventType.objects.update_or_create(event=instance, defaults=type_data)
        EventTag.objects.update_or_create(event=instance, defaults=tag_data)
        Location.objects.update_or_create(event=instance, defaults=location_data)

        return instance